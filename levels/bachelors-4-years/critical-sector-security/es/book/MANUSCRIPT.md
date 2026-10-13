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
5. [Cultura de seguridad](#ch-05)
6. [Estructuras discretas](#ch-06)
7. [Redes y protocolos](#ch-07)
8. [Programación II](#ch-08)
9. [Datos y bases de datos](#ch-09)
10. [Ética y práctica autorizada](#ch-10)
11. [Sistemas operativos](#ch-11)
12. [Probabilidad y estadística](#ch-12)
13. [Identidad y acceso](#ch-13)
14. [Fundamentos de privacidad](#ch-14)
15. [Evidencia y medición](#ch-15)
16. [Arquitectura de seguridad](#ch-16)
17. [Conceptos de criptografía](#ch-17)
18. [Métodos de investigación I](#ch-18)
19. [Infraestructura crítica y seguridad sectorial: alcance y teoría](#ch-19)
20. [Infraestructura crítica y seguridad sectorial: casos fundacionales](#ch-20)
21. [Infraestructura crítica y seguridad sectorial: modelos de sistemas](#ch-21)
22. [Infraestructura crítica y seguridad sectorial: datos y dependencias](#ch-22)
23. [Infraestructura crítica y seguridad sectorial: métodos I](#ch-23)
24. [Infraestructura crítica y seguridad sectorial: controles](#ch-24)
25. [Laboratorio I](#ch-25)
26. [Infraestructura crítica y seguridad sectorial: métodos II](#ch-26)
27. [Infraestructura crítica y seguridad sectorial: verificación](#ch-27)
28. [Infraestructura crítica y seguridad sectorial: análisis de fallas](#ch-28)
29. [Infraestructura crítica y seguridad sectorial: operaciones](#ch-29)
30. [Laboratorio II](#ch-30)
31. [Infraestructura crítica y seguridad sectorial: casos avanzados](#ch-31)
32. [Infraestructura crítica y seguridad sectorial: interfaces interdisciplinarias](#ch-32)
33. [Métodos de investigación II](#ch-33)
34. [Proyecto comparativo](#ch-34)
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

[← Capítulo 03](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Cultura de seguridad

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) definir confidencialidad, integridad y disponibilidad y explicar por qué los servicios críticos suelen ordenarlas de forma distinta que la TI de oficina; (2) usar correctamente el vocabulario activo, amenaza, vulnerabilidad, probabilidad, impacto, riesgo y control; (3) describir en el plano conceptual las principales clases de actores de amenaza y de técnicas de ataque; y (4) leer un aviso de seguridad y extraer lo que significa para una organización concreta. Se apoya en los capítulos 1–4 y prepara el capítulo 16 (arquitectura) y el capítulo 19 (el alcance del campo).

### 5.1 El vocabulario

Un **activo** es algo de valor: un servicio, un sistema, datos, un edificio, el tiempo de las personas. Una **amenaza** es una causa potencial de daño: un actor (un grupo criminal, un infiltrado, un Estado) o un evento (una inundación, una actualización fallida). Una **vulnerabilidad** es una debilidad que una amenaza puede explotar: un defecto sin parchear, una contraseña compartida, una única ruta de cable. La **probabilidad** indica cuán probable es que una amenaza explote una vulnerabilidad en un período; el **impacto** es el daño si lo hace. El **riesgo** los combina, informalmente como «probabilidad × impacto», aunque el capítulo 23 muestra por qué la multiplicación a menudo induce a error. Un **control** (o salvaguarda) es una medida que reduce la probabilidad o el impacto. La guía de evaluación de riesgos del NIST expone este vocabulario y este proceso ([SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)).

### 5.2 La tríada CIA en los servicios críticos

La **confidencialidad** significa que la información solo se revela a quienes están autorizados; la **integridad**, que la información y los sistemas no se alteran sin autorización; la **disponibilidad**, que funcionan cuando se necesitan. La TI de oficina suele poner primero la confidencialidad porque las filtraciones de datos personales tienen costos legales y reputacionales. En la TO, el orden suele invertirse: a una empresa de agua le importa ante todo que las bombas funcionen (disponibilidad) y que las órdenes y las lecturas sean auténticas (integridad); el secreto del nivel de un tanque importa mucho menos. La guía de TO del NIST señala este punto y añade la **seguridad funcional** como preocupación prioritaria ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). La atención sanitaria mezcla ambas cosas: los historiales de los pacientes exigen confidencialidad, mientras que las bombas de infusión y los ventiladores exigen integridad y disponibilidad. Un profesional de la seguridad en un sector crítico debe preguntarse, para cada activo, qué propiedad dañaría primero a las personas si fallara.

### 5.3 Actores y técnicas

Los actores de amenaza difieren en motivación y capacidad. Los **grupos criminales** buscan dinero, sobre todo mediante ransomware que cifra los datos y amenaza con publicarlos. Los **grupos patrocinados por Estados** pueden buscar inteligencia o la capacidad de perturbar servicios en una crisis. Los **hacktivistas** buscan atención. Los **infiltrados** pueden actuar con malicia o, con mucha más frecuencia, cometer errores. Los **accidentes** (actualizaciones fallidas, configuraciones erróneas, cables cortados) causan muchas interrupciones sin ningún adversario. Las técnicas se catalogan en bases de conocimiento públicas como MITRE ATT&CK; la versión para sistemas de control industrial enumera tácticas que van desde el acceso inicial hasta "impair process control", es decir, perjudicar el control del proceso ([MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)). En el nivel de grado usted debe poder leer un catálogo así y decir qué técnicas aborda un control; no se le pide que las ejecute.

### 5.4 Ejemplo resuelto: lectura de un aviso para CPN (sintético)

**Este caso es sintético.** Un aviso de un fabricante (inventado) indica: «Las versiones de la pasarela de acceso remoto VPN-G anteriores a la 9.3 permiten que un atacante no autenticado ejecute código. Se ha observado su explotación. Corregido en la 9.3». Calder Power Networks utiliza VPN-G 9.1 en su sede central, accesible desde internet, y sus ingenieros la usan para llegar a la red de control. Extracción: *activo*, la pasarela y todo lo que es accesible a través de ella; *vulnerabilidad*, el defecto de la 9.1; *amenaza*, cualquier actor que escanee internet, más probable porque se ha observado explotación; *impacto*, posible acceso a la red de control y, por tanto, a la operación de los alimentadores; *opciones de control*, actualizar a la 9.3 ahora, o desactivar la pasarela hasta actualizarla y usar una alternativa supervisada. Los catálogos públicos como el Known Exploited Vulnerabilities de CISA existen precisamente para elevar la prioridad de los defectos explotados en la práctica ([CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)). La decisión no es difícil; la cultura de seguridad consiste en reconocer que «acceso remoto a la TO», más «explotado», más «expuesto a internet» pesa más que un defecto con una puntuación mayor en un dispositivo aislado.

### 5.5 Actividad práctica

Elija un aviso reciente de los [avisos de ICS de CISA](https://www.cisa.gov/news-events/ics-advisories). Sin probar nada, extraiga el activo, la vulnerabilidad, las versiones afectadas, el estado de explotación, la corrección del fabricante y las mitigaciones recomendadas. Después, escriba dos frases sobre cómo cambiaría la prioridad para un operador cuyo dispositivo está (a) expuesto a internet y (b) en una red aislada. Escriba la respuesta sobre la exposición como un cambio de prioridad con una razón, no como una nueva puntuación. Expuesto a internet y explotado suele llevar un aviso a la gestión de emergencia, como ocurre con la VPN-G 9.1 de CPN; el mismo defecto en un dispositivo accesible solo desde una celda aislada puede esperar a la siguiente ventana planificada si se comprueban los controles compensatorios.

### 5.6 Errores comunes y límites

- Usar «amenaza», «vulnerabilidad» y «riesgo» como sinónimos.
- Suponer que la confidencialidad siempre va primero.
- Tratar todo incidente como un ataque; muchas interrupciones son accidentes, y la respuesta es distinta.
- Aprender técnicas de ataque de forma operativa sin autorización (capítulo 10).

EX010 muestra el primer error: llamar vulnerabilidad al corte del cable confunde la amenaza (las obras viales) con la debilidad (una única ruta de cable). El segundo hace que un controlador de dosificación de CW parezca un problema de privacidad cuando lo que protege a los clientes es la integridad. El tercero trata un cable cortado o una actualización fallida como un incidente en el que hay que buscar a un atacante, lo que retrasa la reparación. El cuarto es la razón por la que todos los laboratorios de este libro funcionan sin conexión.

### Ejercicios — capítulo 5

**EX009 — Ordenar las propiedades.** *Objetivo:* aplicar la tríada CIA activo por activo. *Entradas:* los historiales de pacientes del CVH; el controlador de dosificación de cloro de CW; el servicio de autorización de tarjetas de Calder Mutual; las grabaciones de llamadas del CEDC. *Pasos:* ordene C, I y A para cada uno y justifique en una frase la propiedad principal. *Evidencia esperada:* una tabla. *Rúbrica:* 3 = ordenaciones defendibles con razones basadas en el daño (dosificación: primero integridad y seguridad funcional); 2 = una débil; 1 = ordenaciones sin razones; 0 = nada.

**EX010 — Vocabulario bajo presión.** *Objetivo:* usar los términos con precisión. *Entradas:* «El riesgo es que unas obras viales corten el cable, lo cual es una vulnerabilidad para el CEDC». *Pasos:* reescríbalo usando correctamente activo, amenaza, vulnerabilidad e impacto. *Evidencia esperada:* una o dos frases. *Rúbrica:* 3 = obras viales como amenaza, única ruta de cable como vulnerabilidad, disponibilidad del despacho como impacto; 2 = un término mal situado; 1 = dos mal situados; 0 = nada.

### Síntesis del capítulo

La cultura de seguridad es vocabulario preciso aplicado a consecuencias reales. Activos, amenazas, vulnerabilidades, probabilidad, impacto y controles son ideas distintas. En los servicios críticos, la disponibilidad, la integridad y la seguridad funcional suelen pesar más que la confidencialidad, y la prioridad correcta de un aviso depende de la exposición y de la explotación, no solo de una puntuación.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Siga estudiando — capítulo 05 de 40

[← Capítulo 04](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Estructuras discretas

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) usar conjuntos y operaciones de conjuntos para razonar sobre inventarios y permisos; (2) escribir condiciones lógicas y comprobarlas con tablas de verdad; (3) modelar las dependencias entre servicios como un grafo dirigido y calcular qué resulta afectado cuando falla un nodo; y (4) reconocer cuándo es factible una comprobación exhaustiva y cuándo el número de estados la hace imposible. Se apoya en la programación del capítulo 3 y prepara el capítulo 13 (acceso), el capítulo 22 (dependencias) y el capítulo 28 (análisis de fallas).

### 6.1 Conjuntos y relaciones

Un **conjunto** es una colección de elementos distintos. Los dispositivos de la red clínica forman un conjunto $C$; los dispositivos que han superado el fin de su soporte forman un conjunto $U$; su **intersección** $C \cap U$ es el conjunto que hay que aislar primero. La **unión** $A \cup B$ reúne los elementos que están en cualquiera de los dos; la **diferencia** $A \setminus B$ conserva los elementos que están en $A$ pero no en $B$. El control de acceso es razonamiento con conjuntos: los permisos efectivos de un usuario son la unión de los permisos de sus roles, y una regla de separación de funciones dice que ciertos pares nunca deben estar ambos en esa unión (capítulo 13). Una **relación** conecta elementos de dos conjuntos: «el usuario *u* tiene el rol *r*», «el servicio *s* depende del servicio *t*». Muchas preguntas de seguridad son preguntas sobre relaciones: quién puede llegar a qué, qué depende de qué.

### 6.2 Lógica

Una **proposición** es verdadera o falsa. Las proposiciones se combinan con **y** ($\wedge$), **o** ($\vee$) y **no** ($\neg$). Una regla como «un pago superior a £10.000 solo se libera si lo crea una persona y lo aprueba otra distinta, o si es una transferencia de emergencia aprobada por dos directores» es una expresión lógica; escribirla formalmente deja al descubierto sus lagunas («¿y si quien lo crea también es director?»). Una **tabla de verdad** enumera todas las combinaciones de entradas; con $n$ entradas tiene $2^n$ filas. Con 4 entradas son 16 filas, algo fácil. Con 40 entradas son unas $10^{12}$ filas, imposibles de comprobar a mano, y por eso los sistemas complejos necesitan estructura, pruebas y argumentación en lugar de enumeración exhaustiva. Las **leyes de De Morgan**, $\neg(A \wedge B) \equiv \neg A \vee \neg B$, permiten reescribir las condiciones de «no permitido» como condiciones de «permitido» y comprobar que ambas dicen lo mismo.

### 6.3 Grafos

Un **grafo** es un conjunto de nodos y aristas. En un **grafo dirigido**, las aristas tienen dirección; escribimos $u \to v$ para indicar que «$v$ depende de $u$». A partir de un nodo que ha fallado, una **búsqueda en anchura** visita todos los nodos alcanzables siguiendo las aristas: ese conjunto es todo lo que puede resultar afectado. El número de nodos alcanzables desde un nodo es su **alcance**; los nodos con alto alcance son candidatos a protección o respaldo adicionales. Los grafos también dejan ver los **puntos únicos de falla**: nodos cuya eliminación desconecta servicios de lo que necesitan. El artículo clásico de Rinaldi, Peerenboom y Kelly describe las infraestructuras como interdependientes exactamente en este sentido: física, cibernética, geográfica y lógicamente ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131)).

### 6.4 Ejemplo resuelto y Lab 3: dependencias del condado de Calder (sintético)

**Este caso es sintético.** La CRP trazó un primer mapa de dependencias: la subestación eléctrica alimenta las bombas de agua, el suministro de red del hospital, la central de telecomunicaciones y la señalización ferroviaria; la central de telecomunicaciones transporta el despacho, los pagos con tarjeta, la telemetría del agua y el archivo de imágenes en la nube del hospital.

```python
# Lab 3 - cross-sector dependency closure on a directed graph (synthetic Calder County, offline)
from collections import deque
# edge u -> v means "v depends on u"
DEPENDS = {
    "grid-substation-N": ["water-pumps", "hospital-main", "telecom-exchange", "rail-signalling"],
    "telecom-exchange": ["dispatch-cad", "card-payments", "water-telemetry", "hospital-pacs-cloud"],
    "water-pumps": ["hospital-water"],
    "water-telemetry": ["water-pumps"],
    "dispatch-cad": ["ambulance-dispatch"],
    "hospital-main": [],
    "card-payments": ["fuel-retail"],
    "rail-signalling": [], "hospital-water": [], "hospital-pacs-cloud": [],
    "ambulance-dispatch": [], "fuel-retail": [],
}
def affected(start):
    seen, q = {start}, deque([start])
    while q:
        for v in DEPENDS.get(q.popleft(), []):
            if v not in seen:
                seen.add(v); q.append(v)
    return sorted(seen - {start})
for node in ("grid-substation-N", "telecom-exchange", "water-telemetry"):
    a = affected(node)
    print(f"{node}: {len(a)} affected -> {', '.join(a)}")
fan = sorted(((len(affected(n)), n) for n in DEPENDS), reverse=True)[:3]
print("highest reach:", fan)
```

Salida esperada:

```text
grid-substation-N: 11 affected -> ambulance-dispatch, card-payments, dispatch-cad, fuel-retail, hospital-main, hospital-pacs-cloud, hospital-water, rail-signalling, telecom-exchange, water-pumps, water-telemetry
telecom-exchange: 8 affected -> ambulance-dispatch, card-payments, dispatch-cad, fuel-retail, hospital-pacs-cloud, hospital-water, water-pumps, water-telemetry
water-telemetry: 2 affected -> hospital-water, water-pumps
highest reach: [(11, 'grid-substation-N'), (8, 'telecom-exchange'), (2, 'water-telemetry')]
```

Lea el resultado con cuidado. El grafo dice *puede resultar afectado*, no *fallará*: ignora la energía de respaldo, el almacenamiento y la operación manual. Es deliberado: el primer mapa indica dónde mirar; el capítulo 22 añade el tiempo y la autonomía de respaldo. También revela una decisión de modelado: aquí las bombas de agua dependen de la telemetría solo si no pueden funcionar localmente. Cada arista es una afirmación que alguien debería poder justificar.

### 6.5 Actividad práctica

Añada una arista que crea que falta (por ejemplo, el agua del hospital depende de la planta de tratamiento, que depende de la subestación) y un camino alternativo (una segunda central de telecomunicaciones). Vuelva a calcular el alcance. Escriba tres frases sobre lo que el cambio muestra y lo que no muestra. Añadir «planta de tratamiento → agua del hospital» y «subestación → planta de tratamiento» aumenta aún más el alcance de la subestación, mientras que una segunda central no resta nada al recuento simple de alcanzabilidad: la búsqueda sigue marcando todos los nodos a los que puede llegar un solo camino. Esa es la limitación que EX012 le pide explicar, y es la razón para escribir de forma distinta las dependencias AND y OR.

### 6.6 Errores comunes y límites

- Confundir la dirección de las aristas («depende de» frente a «suministra»); escriba la convención en la parte superior de cada diagrama.
- Tratar la alcanzabilidad como certeza de falla.
- Construir un grafo desde la visión de una sola organización: otros operadores conocen dependencias que usted ignora.
- Intentar enumerar espacios de estados de tamaño exponencial.

En el Lab 3, la línea de convención `edge u -> v means "v depends on u"` es lo que hace legible el alcance de 11 nodos de la subestación; invertida, la misma lista afirmaría que la subestación depende de la venta minorista de combustible. Un alcance de 11 significa exposición, no falla, ya que el hospital tiene 72 horas de autonomía con sus generadores. El mapa es la primera visión de la CRP y carece de lo que saben los ingenieros de CW y de CPN. Y el argumento de la tabla de verdad escala en sentido contrario: 40 entradas binarias dan alrededor de un billón de filas.

### Ejercicios — capítulo 6

**EX011 — Conjuntos para la clasificación.** *Objetivo:* usar operaciones de conjuntos. *Entradas:* C = {INF-01, INF-02, IMG-01, IMG-02, ADM-02}; U = {INF-02, IMG-01, IMG-02, LAB-01, ADM-02}; K (dispositivos con un defecto con explotación conocida) = {IMG-01, ADM-02}. *Pasos:* calcule $C \cap U$, $(C \cap U) \cap K$ y $U \setminus C$; diga sobre qué conjunto actuaría primero y por qué. *Evidencia esperada:* tres conjuntos y una razón. *Rúbrica:* 3 = todo correcto y prioridad para $(C \cap U) \cap K$ = {IMG-01, ADM-02}; 2 = un error; 1 = dos errores; 0 = nada.

**EX012 — Un camino alternativo.** *Objetivo:* ver cómo cambia el alcance con la redundancia. *Entradas:* el Lab 3. *Pasos:* modele que dispatch-cad también puede usar un enlace satelital independiente de la central, de modo que perder solo la central ya no detiene el despacho. Explique por qué una búsqueda simple de alcanzabilidad no puede expresarlo y proponga un cambio de modelado. *Evidencia esperada:* la explicación y la propuesta. *Rúbrica:* 3 = reconoce la dependencia OR (necesita uno cualquiera de varios proveedores) frente a la dependencia AND y propone nodos que requieren todas o alguna de sus entradas; 2 = solo reconoce el problema; 1 = edita las aristas de forma incorrecta; 0 = nada.

### Síntesis del capítulo

Los conjuntos describen inventarios y permisos; la lógica hace que las reglas sean exactas y comprobables; los grafos hacen visibles y calculables las dependencias. Cada modelo responde a una pregunta más estrecha de lo que parece: la alcanzabilidad muestra exposición, no falla, y la comprobación exhaustiva solo funciona mientras el espacio de estados es pequeño.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Siga estudiando — capítulo 06 de 40

[← Capítulo 05](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Redes y protocolos

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) explicar las capas, el direccionamiento, los puertos y la diferencia entre el cliente y el servidor de una conexión; (2) describir en qué se diferencian los supuestos de seguridad de protocolos industriales como Modbus de los de los protocolos modernos de internet; (3) expresar una política de segmentación de red como zonas, conductos y una lista de permitidos; y (4) contrastar los flujos observados con esa política e interpretar las infracciones. Se apoya en los capítulos 3 y 6 y prepara el capítulo 16 (arquitectura) y el capítulo 24 (controles).

### 7.1 Capas, direcciones y puertos

Las redes se construyen por capas. La capa de **enlace** mueve tramas entre dispositivos vecinos (Ethernet, Wi-Fi). La capa de **internet** mueve paquetes entre redes mediante direcciones IP. La capa de **transporte** proporciona un flujo de bytes fiable (TCP; véase [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)) o datagramas individuales (UDP), y usa **números de puerto** para identificar el servicio en un equipo. La capa de **aplicación** transporta el significado: HTTPS para la web, Modbus/TCP en el puerto 502 para el sondeo industrial, OPC UA habitualmente en el puerto 4840. En una conexión TCP, el **cliente** abre la conexión hacia el puerto de escucha del servidor; la respuesta usa la misma conexión. Quién inicia es relevante para la seguridad: un controlador de campo que de repente *abre* conexiones hacia la sala de control se comporta de forma distinta a uno que solo responde.

### 7.2 Los protocolos industriales y sus supuestos

Muchos protocolos industriales se diseñaron para enlaces serie cerrados entre los años setenta y noventa. Modbus, por ejemplo, define códigos de función para leer y escribir registros y bobinas, y su forma clásica no tiene autenticación: cualquier dispositivo que pueda enviar a un controlador una petición bien formada puede pedirle que escriba ([especificación de Modbus](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf)). No es un error de una implementación; es el supuesto de diseño de que solo los dispositivos de confianza pueden llegar al cable. Cuando estos protocolos funcionan sobre redes IP, ese supuesto debe imponerlo la red: segmentación, listas de permitidos y supervisión. Los protocolos modernos añaden seguridad (TLS 1.3 proporciona canales autenticados y cifrados; [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)), pero actualizar miles de dispositivos de campo lleva décadas.

### 7.3 Zonas, conductos y listas de permitidos

Una **zona** es un grupo de activos con requisitos de seguridad similares; un **conducto** es la vía de comunicación controlada entre zonas. La serie ISA/IEC 62443 usa estos términos para los sistemas industriales ([presentación de ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). Una empresa de servicios típica tiene una zona corporativa, una zona desmilitarizada (DMZ) en la que se intercambian datos, una zona de control (servidores SCADA, HMI de los operadores) y una zona de campo (controladores, RTU). Una política de **lista de permitidos** nombra los flujos permitidos (zona de origen, zona de destino, puerto, propósito) y deniega todo lo demás. La política es solo la mitad del control; la otra mitad es comprobar que el tráfico observado se ajusta a ella.

### 7.4 Ejemplo resuelto y Lab 4: comprobación de los flujos de CW (sintético)

**Este caso es sintético.** Calder Water permite tres conductos: los usuarios corporativos consultan el historiador de la DMZ por HTTPS; un recolector de la DMZ lee de la zona de control por OPC UA; el servidor SCADA sondea los controladores de campo por Modbus/TCP. Se contrasta con la política un resumen de los flujos de una hora.

```python
# Lab 4 - check observed flows against a zone-and-conduit allowlist (synthetic, offline)
ALLOW = {  # (source zone, destination zone, destination port): purpose
    ("corporate", "dmz", 443): "historian web view",
    ("dmz", "control", 4840): "OPC UA read from historian replica collector",
    ("control", "field", 502): "Modbus/TCP polling of field controllers",
}
ZONE = {"10.1.": "corporate", "10.5.": "dmz", "10.20.": "control", "10.30.": "field"}
def zone(ip):
    return next((z for p, z in ZONE.items() if ip.startswith(p)), "unknown")
FLOWS = [  # src, dst, dport  (synthetic NetFlow-style summary)
    ("10.1.4.22", "10.5.0.10", 443), ("10.5.0.11", "10.20.0.5", 4840),
    ("10.20.0.5", "10.30.1.7", 502), ("10.1.4.80", "10.20.0.5", 3389),
    ("10.20.0.9", "198.51.100.23", 443), ("10.30.1.7", "10.20.0.5", 502),
]
for s, d, p in FLOWS:
    key = (zone(s), zone(d), p)
    verdict = ALLOW.get(key)
    print(f"{s:>13} -> {d:<14} :{p:<5} {key[0]:>9}->{key[1]:<8} {'ALLOW ' + verdict if verdict else 'VIOLATION'}")
```

Salida esperada:

```text
    10.1.4.22 -> 10.5.0.10      :443   corporate->dmz      ALLOW historian web view
    10.5.0.11 -> 10.20.0.5      :4840        dmz->control  ALLOW OPC UA read from historian replica collector
    10.20.0.5 -> 10.30.1.7      :502     control->field    ALLOW Modbus/TCP polling of field controllers
    10.1.4.80 -> 10.20.0.5      :3389  corporate->control  VIOLATION
    10.20.0.9 -> 198.51.100.23  :443     control->unknown  VIOLATION
    10.30.1.7 -> 10.20.0.5      :502       field->control  VIOLATION
```

Tres infracciones, tres significados distintos. Una conexión de escritorio remoto (puerto 3389) desde la zona corporativa directamente a la zona de control evita la DMZ: quizá un atajo de un ingeniero, quizá un intruso. Un equipo de la zona de control que llega a una dirección de internet (198.51.100.23 es una dirección de documentación que sustituye a una real) puede ser la comprobación de actualizaciones de un fabricante o datos que salen. Un dispositivo de campo que *inicia* Modbus hacia el servidor SCADA invierte la dirección normal. Ninguna prueba un ataque; cada una necesita un responsable que la explique, y la explicación se convierte en evidencia (capítulo 15).

### 7.5 Actividad práctica

En un computador de su propiedad, enumere sus propias conexiones activas (por ejemplo, con `netstat` o `ss`) y clasifique cinco como cliente o servidor, local o remota, y esperada o inesperada. No escanee ningún otro sistema. Use la columna de estado de `ss` o de `netstat`: una dirección local con un puerto en escucha es un servidor; una conexión a un puerto remoto 443 es un cliente. Marque todo lo que no pueda explicar y encuentre el programa que hay detrás con las herramientas de su sistema operativo, en su propia máquina.

### 7.6 Errores comunes y límites

- Escribir listas de permitidos solo por puerto, ignorando las zonas de origen y destino.
- Suponer que «interno» significa «de confianza».
- Confundir el tráfico de respuesta con las conexiones iniciadas al leer los registros de flujos.
- Tratar una infracción como prueba de compromiso en lugar de como una pregunta.

El Lab 4 muestra por qué: una regla solo por puerto que permitiera el 502 habría dejado pasar al dispositivo de campo que inició Modbus hacia el servidor SCADA, una inversión de la dirección normal. La conexión RDP corporativa hacia el control es «interna» y aun así es una infracción. En los registros de flujos, las respuestas de los controladores de campo desde el puerto 502 hacia el servidor SCADA no son conexiones nuevas y no deben leerse como tales. Y cada una de las tres infracciones llega primero a un responsable como pregunta.

### Ejercicios — capítulo 7

**EX013 — Explicar las infracciones.** *Objetivo:* razonar desde los flujos hasta las hipótesis. *Entradas:* la salida del Lab 4. *Pasos:* para cada infracción, dé una explicación benigna y una maliciosa, y la evidencia que permitiría distinguirlas. *Evidencia esperada:* una tabla de tres filas. *Rúbrica:* 3 = pares plausibles y evidencia distintiva concreta (solicitudes de cambio, inicios de sesión de usuarios, titularidad del destino, configuración del dispositivo); 2 = evidencia genérica; 1 = solo explicaciones; 0 = nada.

**EX014 — Flujo mínimo.** *Objetivo:* endurecer una política. *Entradas:* la tabla ALLOW. *Pasos:* proponga dos refinamientos que estrechen la política sin romper sus propósitos (por ejemplo, reglas por equipo en lugar de por zona, códigos de función de solo lectura) y diga cómo se impondría y se comprobaría cada uno. *Evidencia esperada:* dos refinamientos con su imposición y su comprobación. *Rúbrica:* 3 = ambos más estrechos, imponibles y comprobables; 2 = uno; 1 = vagos; 0 = nada.

### Síntesis del capítulo

Las redes llevan consigo los supuestos de sus protocolos. Los protocolos industriales clásicos confían en cualquiera que pueda alcanzarlos, por lo que los servicios críticos imponen la confianza con zonas, conductos y listas de permitidos, y después contrastan los flujos observados con la política. Una infracción es una pregunta para un responsable, no un veredicto.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Siga estudiando — capítulo 07 de 40

[← Capítulo 06](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Programación II

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) validar entradas no confiables con reglas explícitas y rechazar lo que no se ajuste a ellas; (2) gestionar los errores para que un programa falle de forma segura y visible; (3) escribir pruebas unitarias, incluidas pruebas de casos límite y mal formados; y (4) explicar por qué el análisis sintáctico de la entrada es una frontera de seguridad. Se apoya en los capítulos 3 y 7 y prepara el capítulo 9 (datos) y el capítulo 27 (verificación).

### 8.1 La entrada es una frontera de seguridad

Todo programa que lee datos del exterior (un archivo, un mensaje de red, lo que introduce un operador) hace suposiciones sobre ellos. Cuando las suposiciones son erróneas, los programas se bloquean, calculan mal o, peor aún, hacen algo que eligió un atacante. Los catálogos de debilidades del software están dominados por errores en el tratamiento de la entrada: inyección, lecturas y escrituras fuera de límites, validación incorrecta de la entrada ([CWE Top 25](https://cwe.mitre.org/top25/)). El patrón defensivo es **analizar, no adivinar**: definir con exactitud cómo es una entrada válida, convertir el texto bruto en valores tipados en un único lugar y rechazar todo lo demás con un error claro.

### 8.2 Reglas de validación

Para un punto de consigna enviado a una estación de bombeo, una entrada válida podría ser: un número; finito (no «NaN» ni infinito); dentro de los límites de ingeniería (0,5–4,5 m); que no cambie más de 0,5 m respecto del valor actual; procedente de una fuente autorizada. Cada regla debe ser explícita, estar probada y registrarse cuando rechaza algo. La **lista de permitidos** (aceptar solo las formas conocidas como buenas) es más sólida que la **lista de denegados** (rechazar las formas conocidas como malas), porque los atacantes encuentran formas en las que usted no pensó. En Python, `float("nan")` funciona, y tanto `nan < 0.5` como `nan > 4.5` son falsos, de modo que una comprobación de rango escrita como «rechazar si está por debajo o por encima» *acepta* NaN sin hacer ruido. La comprobación robusta es «aceptar solo si `math.isfinite(x)` y `0.5 <= x <= 4.5`».

### 8.3 Errores y fallar de forma segura

Cuando la validación falla, el programa debe hacer algo definido: rechazar la orden y conservar el último valor bueno, generar una alarma, registrar el motivo. No debe continuar con un valor predeterminado que resulte peligroso (un punto de consigna de cero) ni tragarse el error en silencio (`except: pass`). En contextos de control, «seguro» es una decisión del proceso (una válvula puede necesitar fallar cerrada para el cloro pero abierta para el agua de refrigeración), por lo que el programador implementa un estado de falla que ha especificado el responsable del proceso, en lugar de inventarlo.

### 8.4 Pruebas

Una **prueba unitaria** comprueba una función con casos conocidos. Los buenos conjuntos de pruebas incluyen valores **típicos**, **límites** (exactamente 0,5 y 4,5), valores **justo fuera** de los límites (0,49, 4,51), entradas **mal formadas** (cadena vacía, "abc", "1e309", "nan") y casos **dependientes del estado** (un valor válido que cambia demasiado rápido). El módulo `unittest` incorporado en Python o simples sentencias `assert` bastan en este nivel. Una prueba que nunca ha fallado nunca ha demostrado que funcione: ejecute cada prueba nueva una vez contra una versión estropeada a propósito.

Para el validador de puntos de consigna de CW, la versión contra la que fallar es la v1: su prueba de "nan" devuelve True y su prueba de "abc" lanza una excepción, de modo que dos de las siete pruebas fallan antes de la corrección y ninguna después.

### 8.5 Ejemplo resuelto: validador de puntos de consigna de CW (sintético)

**Este caso es sintético.** La interfaz de operador de Calder Water envía como texto los puntos de consigna del nivel de los tanques. Versión 1 del validador:

```python
def accept_v1(text, current):
    x = float(text)
    if x < 0.5 or x > 4.5: return False
    if abs(x - current) > 0.5: return False
    return True
```

`accept_v1("nan", 3.0)` devuelve True: ambas comparaciones con NaN son falsas, y `abs(nan - 3.0) > 0.5` también es falsa. `accept_v1("abc", 3.0)` lanza una excepción que, según quién llame, puede bloquear la interfaz. Versión 2:

```python
import math
def accept_v2(text, current):
    try:
        x = float(text)
    except ValueError:
        return False
    return math.isfinite(x) and 0.5 <= x <= 4.5 and abs(x - current) <= 0.5
```

La versión 2 dice qué es aceptable en lugar de qué no lo es. Pruebas: `("3.2", 3.0)` → True; `("4.5", 4.2)` → True; `("4.51", 4.2)` → False; `("nan", 3.0)` → False; `("inf", 3.0)` → False; `("abc", 3.0)` → False; `("2.0", 3.0)` → False (paso demasiado grande).

El bloque `try` convierte un bloqueo en un rechazo, y `math.isfinite` elimina NaN e infinito antes de cualquier comparación. Lo que la v2 todavía no hace es decir por qué rechazó: la interfaz de operador debería registrar qué regla falló.

### 8.6 Actividad práctica

Implemente ambas versiones y las siete pruebas anteriores. Ejecute las pruebas contra la v1 y anote cuáles fallan; después, contra la v2. Añada dos pruebas propias que crea que la v2 todavía podría resolver mal (pista: espacios en blanco, cadenas muy largas, una coma como separador decimal) y decida si el comportamiento es aceptable. Contra la v1, espere que la prueba de "nan" falle (devuelve True) y que "abc" lance una excepción en lugar de devolver False. Contra la v2 deberían pasar las siete. En sus propias pruebas, `float` de Python acepta " 3.2 " con espacios, lo que probablemente está bien; "3,2" se rechaza, lo que puede sorprender a un operador que use la coma decimal. Decida si ese rechazo debería producir un mensaje claro en lugar de una negativa silenciosa.

### 8.7 Errores comunes y límites

- Comprobaciones de rango que dejan pasar NaN.
- Capturar todas las excepciones y continuar.
- Validar solo en la interfaz de usuario y no donde se ejecuta la orden.
- Pruebas que solo cubren valores típicos.
- Creer que la validación hace auténtico un canal: una orden falsificada de apariencia válida sigue pasando (el capítulo 17 añade la autenticación).

En CW el tercer error es el peligroso: si solo la interfaz de operador comprueba los puntos de consigna, cualquier otro cliente que pueda llegar al PLC por Modbus evita por completo la validación, como muestra el conducto de la zona de campo del Lab 4. El quinto error enlaza con el Lab 8: un punto de consigna bien formado de 2,0 m pasa la v2 tanto si lo envió un operador como si lo envió un intruso.

### Ejercicios — capítulo 8

**EX015 — Romper la v1.** *Objetivo:* encontrar entradas que burlen una comprobación por lista de denegados. *Entradas:* `accept_v1`. *Pasos:* encuentre tres entradas distintas para las que la v1 da un resultado inseguro o indefinido y explique cada una. *Evidencia esperada:* las entradas y las explicaciones. *Rúbrica:* 3 = NaN aceptado; texto no numérico (o una cadena vacía) que lanza una excepción no gestionada; y un tercer caso distinto, como un valor *actual* NaN, que hace que la comprobación del paso se supere para cualquier punto de consigna dentro de rango; 2 = dos; 1 = una; 0 = nada.

**EX016 — Especificar el estado de falla.** *Objetivo:* conectar el código con la seguridad funcional del proceso. *Entradas:* un punto de consigna rechazado en una bomba de dosificación de cloro y en una válvula de entrada de agua bruta. *Pasos:* para cada caso, indique qué debe hacer el programa ante el rechazo, quién debe decidirlo y qué debe registrarse. *Evidencia esperada:* dos especificaciones breves. *Rúbrica:* 3 = conservar el último valor bueno más alarma, decide el responsable del proceso, campos del registro nombrados (hora, fuente, entrada bruta, regla que falló); 2 = parcial; 1 = genérico; 0 = nada.

### Síntesis del capítulo

El análisis de la entrada es una frontera de seguridad. Defina con precisión la entrada válida, acepte solo esa, falle hacia un estado elegido por el responsable del proceso, registre cada rechazo y pruebe los límites y los casos mal formados. La validación detecta la entrada mal formada; no demuestra que una entrada bien formada procediera de alguien autorizado.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Siga estudiando — capítulo 08 de 40

[← Capítulo 07](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Datos y bases de datos

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) diseñar un esquema relacional pequeño con claves; (2) escribir consultas SQL que filtran, combinan y ordenan; (3) explicar por qué importan los tipos de datos, con los números de versión como ejemplo; y (4) prevenir la inyección SQL con consultas parametrizadas. Se apoya en los capítulos 3 y 8 y prepara el capítulo 14 (privacidad), el capítulo 15 (medición) y el capítulo 22 (dependencias).

### 9.1 Por qué datos relacionales

Las preguntas de seguridad combinan hechos guardados en lugares distintos: qué activos existen, qué software ejecutan, qué avisos afectan a ese software, quién es responsable de cada activo, cuáles están expuestos a internet. Una **base de datos relacional** almacena cada tipo de hecho una sola vez, en una **tabla** de filas y columnas, y conecta las tablas mediante **claves** ([Codd, 1970](https://doi.org/10.1145/362384.362685)). Una **clave primaria** identifica una fila de forma única (el ID de un activo); una **clave foránea** hace referencia a una fila de otra tabla (el nombre de producto de un activo, que coincide con el producto de un aviso). Una **combinación** (*join*) reúne las filas que coinciden. Almacenar cada hecho una sola vez evita la falla conocida de las hojas de cálculo: dos copias que no concuerdan.

### 9.2 SQL en cuatro cláusulas

`SELECT` nombra las columnas que quiere; `FROM ... JOIN ... ON` nombra las tablas y cómo coinciden; `WHERE` filtra las filas; `ORDER BY` ordena. `GROUP BY` con `COUNT` resume. La biblioteca estándar de Python incluye `sqlite3`, una base de datos integrada completa, de modo que puede practicar sin servidor. Dos advertencias. Primera, una combinación descarta en silencio las filas sin coincidencia: un activo cuyo nombre de producto está mal escrito simplemente desaparece de un informe de vulnerabilidades. Use un `LEFT JOIN` y busque valores nulos cuando importe la completitud. Segunda, los **tipos** deciden las comparaciones. Las cadenas de versión comparadas como texto ponen "3.10" antes que "3.4", porque el carácter "1" se ordena antes que "4".

### 9.3 Inyección

Si un programa construye SQL pegando la entrada del usuario en una cadena (`"... WHERE id = '" + user_input + "'"`), una entrada como `x' OR '1'='1` cambia el significado de la consulta. Es la **inyección SQL**, que figura de forma persistente entre las debilidades de software más peligrosas ([CWE Top 25](https://cwe.mitre.org/top25/)). La corrección es estructural: las **consultas parametrizadas** (`db.execute("... WHERE id = ?", (user_input,))`) envían los datos separados del código, de modo que la entrada nunca puede convertirse en SQL. En el Lab 5, toda consulta con una entrada, como buscar un activo por su ID, debe usar un marcador `?`.

### 9.4 Ejemplo resuelto y Lab 5: correspondencia de avisos en CPN (sintético)

**Este caso es sintético.** Calder Power Networks mantiene una tabla de activos e importa los avisos de los fabricantes. La pregunta: ¿qué activos ejecutan una versión anterior a la versión corregida, ordenados de modo que primero aparezcan los elementos con explotación conocida y expuestos a internet? Una pequeña función propia compara las versiones numéricamente.

```python
# Lab 5 - asset and vulnerability joins in SQLite (synthetic Calder Power data, offline)
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE asset(id TEXT PRIMARY KEY, site TEXT, role TEXT, product TEXT, version TEXT, internet_exposed INTEGER);
CREATE TABLE advisory(product TEXT, fixed_in TEXT, severity TEXT, known_exploited INTEGER);
INSERT INTO asset VALUES
 ('RTU-11','Substation North','feeder RTU','RTU-K','3.2',0),
 ('RTU-12','Substation North','feeder RTU','RTU-K','3.4',0),
 ('HMI-01','Control room','operator HMI','HMI-S','7.0',0),
 ('VPN-01','Head office','remote access gateway','VPN-G','9.1',1),
 ('HIS-01','DMZ','historian replica','HIST-P','5.5',0);
INSERT INTO advisory VALUES
 ('RTU-K','3.4','high',0), ('VPN-G','9.3','critical',1), ('HIST-P','5.1','medium',0);
""")
def vkey(v): return tuple(int(x) for x in v.split("."))
db.create_function("vlt", 2, lambda a, b: int(vkey(a) < vkey(b)))
q = """SELECT a.id, a.role, a.version, v.fixed_in, v.severity, v.known_exploited, a.internet_exposed
       FROM asset a JOIN advisory v ON a.product = v.product
       WHERE vlt(a.version, v.fixed_in)
       ORDER BY v.known_exploited DESC, a.internet_exposed DESC, v.severity"""
for row in db.execute(q):
    print(row)
print("string comparison '3.10' < '3.4':", "3.10" < "3.4", "| numeric:", vkey("3.10") < vkey("3.4"))
```

Salida esperada:

```text
('VPN-01', 'remote access gateway', '9.1', '9.3', 'critical', 1, 1)
('RTU-11', 'feeder RTU', '3.2', '3.4', 'high', 0, 0)
string comparison '3.10' < '3.4': True | numeric: False
```

Dos activos necesitan actuación, primero la pasarela (es el aviso del capítulo 5). HMI-01 no tiene aviso y no aparece; HIS-01 ya ha superado la corrección. Observe que `ORDER BY v.severity` ordena las *palabras* alfabéticamente ("critical" < "high" < "medium"), lo que aquí resulta correcto por casualidad y sería erróneo con "low". Una columna con el rango de gravedad es el diseño robusto.

### 9.5 Actividad práctica

(1) Cambie la combinación por un `LEFT JOIN` y enumere los activos sin registro de aviso: ¿es «sin aviso» lo mismo que «sin vulnerabilidad»? (2) Escriba una consulta parametrizada que devuelva un activo por su ID; después, muestre con una consulta construida a propósito de forma insegura mediante cadenas, solo sobre su base de datos en memoria, cómo `' OR '1'='1` devuelve todas las filas. El `LEFT JOIN` muestra HMI-01 con nulos en las columnas del aviso. «Sin aviso» significa que no hay aviso en esta fuente para el producto HMI-S, no que la HMI no tenga defectos; puede tener un boletín del fabricante fuera de la fuente o no tener ninguno publicado todavía. En la parte (2), la consulta insegura solo debe ejecutarse contra su base de datos en memoria, nunca contra una real.

### 9.6 Errores comunes y límites

- Comparar versiones, fechas o números almacenados como texto.
- Combinaciones internas que descartan en silencio las filas sin coincidencia.
- Construir SQL concatenando cadenas.
- Confiar en que los nombres de producto coincidan exactamente entre las fuentes de los fabricantes y los inventarios locales.

El Lab 5 muestra dónde morderían tres de estos errores. La comparación de versiones trataría "3.10" como anterior a "3.4" si se hiciera como texto, y marcaría erróneamente como vulnerable una RTU actualizada. La combinación interna descarta HMI-01 en silencio. Y los nombres de producto "RTU-K" y "VPN-G" solo se combinan porque la muestra se escribió de forma coherente; las fuentes reales de los fabricantes escriben los productos de forma distinta y necesitan una tabla de correspondencias.

### Ejercicios — capítulo 9

**EX017 — Recuento por sitio.** *Objetivo:* resumir con SQL. *Entradas:* el Lab 5. *Pasos:* escriba una consulta que devuelva, por sitio, el número de activos que necesitan una actualización. *Evidencia esperada:* la consulta y el resultado. *Rúbrica:* 3 = `GROUP BY` correcto con el filtro de versión, resultado Head office 1, Substation North 1; 2 = cuenta todos los activos; 1 = solo la sintaxis; 0 = nada.

**EX018 — Orden por gravedad.** *Objetivo:* corregir una ordenación frágil. *Entradas:* el Lab 5 con un aviso adicional de gravedad "low". *Pasos:* explique por qué `ORDER BY severity` colocaría mal "low" y dé dos correcciones. *Evidencia esperada:* la explicación y las correcciones. *Rúbrica:* 3 = el orden alfabético pone "low" antes que "medium"; correcciones: una columna de rango numérico o una tabla de consulta o una expresión `CASE`; 2 = una corrección; 1 = solo la explicación; 0 = nada.

### Síntesis del capítulo

Los datos relacionales permiten responder con una sola consulta a preguntas de seguridad transversales, si las claves, los tipos y las combinaciones son correctos. Compare las versiones numéricamente, busque lo que descartan las combinaciones, ordene las gravedades con números y nunca construya SQL a partir de cadenas no confiables.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Siga estudiando — capítulo 09 de 40

[← Capítulo 08](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Ética y práctica autorizada

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) explicar por qué es la autorización, y no la capacidad técnica, lo que define el trabajo de seguridad legítimo; (2) redactar un documento sencillo de reglas de enfrentamiento para un ejercicio; (3) gestionar un descubrimiento accidental sobre un sistema real mediante la divulgación coordinada; y (4) razonar sobre los conflictos entre seguridad, seguridad funcional, privacidad y continuidad del servicio con la ayuda de un código profesional. Se apoya en los capítulos 1–9 y rige todas las actividades prácticas del resto del libro.

### 10.1 La autorización es la línea

La misma orden puede ser mantenimiento o un delito. Lo que las separa es la **autorización**: el permiso explícito de alguien facultado para darlo, para un alcance, un tiempo y un método definidos. La mayoría de las jurisdicciones tipifican como delito el acceso no autorizado a sistemas informáticos y, en los servicios críticos, las pruebas no autorizadas también pueden poner en peligro a las personas: un escaneo inofensivo para un portátil puede bloquear un controlador. Por eso la regla de este libro es simple y absoluta: el trabajo práctico usa los laboratorios sintéticos del libro, sistemas de su propiedad o sistemas cuyo propietario ha dado un permiso escrito y específico. La curiosidad por un dispositivo expuesto de una empresa de servicios real no es un permiso.

### 10.2 Reglas de enfrentamiento

Los ejercicios autorizados se ponen por escrito en unas **reglas de enfrentamiento** (RoE): quién autoriza (con nombre y función); el alcance (qué sistemas, qué direcciones y, de forma explícita, qué queda excluido; los sistemas de seguridad funcional suelen estarlo); la ventana de tiempo; los métodos permitidos; las condiciones de parada («ante cualquier alarma inesperada del proceso: parar y llamar al ingeniero de turno»); el plan de comunicación; el tratamiento de los datos encontrados; y cómo se informarán los resultados. Unas RoE protegen al servicio, a la organización y a quien realiza la prueba. En la TO, las RoE suelen acordarse con los ingenieros de operaciones y de seguridad funcional, no solo con el equipo de seguridad de TI, y a menudo limitan las pruebas a la observación pasiva o a réplicas sin conexión.

### 10.3 Divulgación

Si encuentra una vulnerabilidad por accidente (una página pública que expone una interfaz de control, un correo enviado por error), el camino ético es detenerse, no seguir explorando, e informar en privado al propietario o a través de un coordinador. La **divulgación coordinada de vulnerabilidades** da al propietario o al fabricante tiempo para corregir antes de que se publiquen los detalles; organismos nacionales como CISA gestionan programas que coordinan a quienes descubren con los fabricantes ([programa CVD de CISA](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program)). Anote qué vio y cuándo, manténgalo en confidencialidad y no conserve datos a los que no tenía derecho a acceder.

### 10.4 Códigos profesionales y conflictos

El Código de Ética de la ACM pide a los profesionales de la informática que contribuyan a la sociedad y al bienestar humano, eviten el daño, sean honestos y respeten la privacidad, y que "access computing and communication resources only when authorized or when compelled by the public good", es decir, que accedan a recursos informáticos y de comunicación solo cuando estén autorizados o cuando lo exija el bien público ([ACM Code, 2018](https://www.acm.org/code-of-ethics)). Los dilemas reales enfrentan estos deberes entre sí. ¿Debe un hospital retrasar un parche de seguridad para su flota de ventiladores porque la actualización exige retirar dispositivos del servicio durante un pico de enfermedades respiratorias? ¿Debe una empresa de servicios compartir los detalles de un incidente con otras empresas cuando sus abogados aconsejan silencio? Un enfoque estructurado ayuda: identificar a las partes interesadas y los daños; identificar los deberes y quién los tiene; considerar alternativas (parchear un subconjunto, añadir un control compensatorio); decidir; registrar el razonamiento y quién aceptó el riesgo residual.

### 10.5 Ejemplo resuelto: la HMI abierta (sintético)

**Este caso es sintético.** Un estudiante que busca información sobre prácticas en el sitio web público de Calder Water sigue un enlace que abre una página web titulada «Pump Station 4 — operator view». No se le pidió ninguna contraseña. La respuesta ética: no hacer clic en nada de la página, no probar otros enlaces, tomar una captura de pantalla solo de la barra de direcciones y del título si hace falta para informar, cerrar la página y escribir al contacto de seguridad publicado por CW (o, si no lo hay, al CERT o CSIRT nacional) indicando qué vio, cuándo y cómo llegó a ello. No publicar nada al respecto. No «comprobar si de verdad está en funcionamiento». Debe informarse al asesor de ética de la universidad del estudiante. En este caso sintético, CW agradece al estudiante, elimina el enlace y descubre que la página era una demostración de un fabricante olvidada en un servidor web, un recordatorio de que quien descubre rara vez conoce el panorama completo.

### 10.6 Actividad práctica

Escriba unas RoE de una página para el Laboratorio I (capítulo 25), que solo ejecuta los laboratorios sin conexión del libro en su propio computador. Incluso con un alcance trivial, complete todos los encabezados: quién autoriza, alcance, exclusiones, ventana, métodos, condiciones de parada, tratamiento de los datos e informe. Como condición de parada, «cualquier comportamiento inesperado de mi propio computador, o cualquier intento de un script de acceder a la red» es específica y observable. Nómbrese a sí mismo como quien autoriza y quien prueba dentro del alcance, y a su tutor como la persona a quien se avisa si se produce una condición de parada.

### 10.7 Errores comunes y límites

- «Era accesible públicamente, así que estaba permitido».
- La autorización verbal, o la autorización de alguien que no es propietario del sistema.
- La ampliación progresiva del alcance durante una prueba («ya que estoy aquí…»).
- Conservar los datos encontrados durante una prueba una vez terminado el encargo.
- Tratar la ética como una lista de comprobación de cumplimiento en lugar de como un deber de razonamiento.

El ejemplo resuelto de la HMI abierta pone a prueba los tres primeros. La página era accesible públicamente, pero nadie en CW autorizó una visita; un compañero de clase que dice «adelante» no es propietario del sistema; y hacer clic en «solo un enlace más» para comprobar si está en funcionamiento es ampliar el alcance. El cuarto se aplicaría si el estudiante conservara la captura de pantalla después de informar. El quinto es la razón por la que el estudiante también avisó al asesor de ética.

### Ejercicios — capítulo 10

**EX019 — Redactar las condiciones de parada.** *Objetivo:* proteger un servicio en funcionamiento durante una prueba autorizada. *Entradas:* CPN autoriza una captura pasiva del tráfico de red en su sala de control durante un día. *Pasos:* redacte cinco condiciones de parada e indique a quién se llama en cada una. *Evidencia esperada:* una lista. *Rúbrica:* 3 = cinco condiciones específicas y observables (alarma del proceso, comportamiento inesperado de un dispositivo, descubrimiento de tráfico de sistemas de seguridad funcional fuera del alcance, petición de un operador, datos de tipo sensible) con funciones nombradas; 2 = genéricas; 1 = menos de tres; 0 = nada.

**EX020 — El dilema del parche.** *Objetivo:* estructurar una decisión ética. *Entradas:* el ejemplo del parche de los ventiladores de la discusión de este capítulo sobre los códigos profesionales. *Pasos:* enumere las partes interesadas y los daños, dos alternativas a «parchear todo ahora» o «no parchear nada», y redacte un registro de decisión de 150 palabras que nombre a quien acepta el riesgo residual. *Evidencia esperada:* el análisis y el registro. *Rúbrica:* 3 = daños en ambos lados, alternativas creíbles (parcheo escalonado, aislamiento más supervisión), responsables clínico y de seguridad nombrados; 2 = solo un lado; 1 = opinión sin estructura; 0 = nada.

### Síntesis del capítulo

La autorización define el trabajo de seguridad legítimo. Redacte reglas de enfrentamiento, deténgase cuando tropiece con algo real e infórmelo en privado, y razone de forma explícita los conflictos entre deberes, registrando quién aceptó qué riesgo. En los servicios críticos, las pruebas descuidadas pueden dañar a las personas.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Siga estudiando — capítulo 10 de 40

[← Capítulo 09](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operativos

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) explicar los procesos, la protección de memoria, los permisos de archivo y los privilegios; (2) describir cómo un sistema operativo aplica el mínimo privilegio y dónde no puede hacerlo; (3) comparar los sistemas operativos de propósito general, de tiempo real y embebidos en los servicios críticos; y (4) elaborar una lista de comprobación de bastionado y una decisión de parcheo para un dispositivo que no puede reiniciarse a voluntad. Se apoya en las capas del capítulo 2 y prepara el capítulo 13 (identidad) y el capítulo 24 (controles).

### 11.1 Qué hace el sistema operativo

El **sistema operativo** (SO) reparte una sola máquina entre muchos programas y usuarios. Un **proceso** es un programa en ejecución con su propia memoria; el SO usa la protección de memoria del hardware para que un proceso no pueda leer ni sobrescribir la memoria de otro. El **núcleo** (*kernel*) es el componente central privilegiado que gestiona el hardware; los programas de usuario le piden servicios mediante **llamadas al sistema**. Los archivos llevan **permisos** (en los sistemas tipo Unix, lectura, escritura y ejecución para el propietario, un grupo y los demás) y el SO los comprueba en cada acceso. El **privilegio** es la capacidad de saltarse esas comprobaciones: la cuenta root de Unix, el Administrador de Windows. Los principios de **mínimo privilegio** y **mediación completa** de Saltzer y Schroeder (cada acceso comprobado, cada programa con solo los derechos que necesita) siguen siendo la base ([Saltzer and Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939)).

### 11.2 Tipos de SO en los servicios críticos

Los sistemas de **propósito general** (Windows, Linux, macOS) hacen funcionar servidores, estaciones de trabajo de operadores y PC de oficina; tienen muchas funciones, se parchean con frecuencia y son muy atacados. Los **sistemas operativos de tiempo real** (RTOS) garantizan que las tareas cumplan sus plazos (un relé de protección debe actuar en milisegundos) y funcionan en controladores, relés y dispositivos médicos; son pequeños y se parchean con menos frecuencia. El **firmware embebido** de sensores y dispositivos sencillos puede no tener ninguna separación entre programas. La consecuencia: las protecciones de SO más fuertes están en las máquinas más fáciles de sustituir, y las más débiles en las máquinas que más duran.

### 11.3 Bastionado

El **bastionado** reduce lo que un atacante puede aprovechar. Una lista de comprobación práctica: eliminar o desactivar los servicios y el software que no se usan; cambiar las cuentas y contraseñas por defecto; ejecutar los servicios con cuentas sin privilegios; activar el registro de eventos y enviar los registros fuera del equipo; restringir los soportes extraíbles; activar las listas de aplicaciones permitidas donde la carga de trabajo es estable (las estaciones de trabajo de operadores son buenas candidatas: ejecutan los mismos pocos programas durante años); mantener la hora sincronizada para poder correlacionar los registros. Cada elemento debe poder comprobarse: una norma de bastionado que no puede verificarse es un deseo.

### 11.4 El parcheo en operaciones

En la TI de oficina, parchear es una rutina. En una estación de trabajo de operador o en un controlador, un parche puede requerir la validación del fabricante, una ventana de mantenimiento y un plan de vuelta atrás, porque una actualización fallida puede detener el proceso. Una **decisión de parcheo basada en el riesgo** se pregunta: ¿es explotable la falla en este dispositivo tal como está desplegado (¿es alcanzable?, ¿requiere acceso local?); ¿se sabe que se está explotando; qué controla el dispositivo; qué controles compensatorios existen; cuándo es la próxima ventana? El resultado es uno de estos: parchear ya (cambio de emergencia), parchear en la próxima ventana, mitigar y supervisar hasta la sustitución, o aceptar con un responsable nombrado. La guía de TO del NIST analiza estos compromisos ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

### 11.5 Ejemplo resuelto: estación de trabajo de señalización de CT (sintético)

**Este caso es sintético.** La estación de trabajo de control de señalización de Calder Transit funciona con un SO de propósito general. Una actualización mensual corrige una falla que permite a un usuario local con pocos privilegios convertirse en administrador. La estación no tiene acceso a internet ni correo electrónico, tiene activada la lista de aplicaciones permitidas y solo inician sesión tres señalistas con nombre. El fabricante valida las actualizaciones del SO cada trimestre; el próximo paquete validado llega dentro de siete semanas. Decisión: **parchear en la próxima ventana**, porque la explotación necesita una cuenta local en una máquina estrictamente controlada; mientras tanto, confirmar que la lista de permitidos se aplica y revisar las tres cuentas. Si la falla hubiera sido explotable de forma remota a través de un servicio de red que la estación expone, la respuesta habría sido un cambio de emergencia o desactivar ese servicio.

### 11.6 Actividad práctica

En su propio ordenador, enumere los procesos en ejecución y la cuenta con la que se ejecuta cada uno; busque un servicio que no use y averigüe cómo podría desactivarse (no desactive nada de lo que no esté seguro). Redacte una lista de comprobación de bastionado de cinco elementos para una estación de trabajo de atención de llamadas del CEDC, cada uno con la forma de verificarlo. Para la estación del CEDC, redacte elementos como «los operadores de llamadas inician sesión con cuentas individuales sin derechos de administrador; comprobación: listar los administradores locales cada mes» o «almacenamiento USB bloqueado; comprobación: insertar una unidad de prueba durante la revisión trimestral».

### 11.7 Errores comunes y límites

- Ejecutarlo todo como administrador «para evitar problemas de permisos».
- Bastionar una vez y no verificar nunca la deriva.
- Aplicar a la TO la cadencia de parcheo de la TI de oficina sin validación ni vuelta atrás.
- Suponer que un dispositivo sin interfaz de usuario del SO no tiene SO.

La estación de señalización de CT muestra las alternativas: la lista de permitidos y tres cuentas con nombre en lugar del uso de administrador, un paquete trimestral validado por el fabricante en lugar de la cadencia mensual de la oficina, y una revisión que comprueba que la lista de permitidos se sigue aplicando. El cuarto error abarca las bombas de infusión del CVH, que funcionan con un RTOS que necesita actualizaciones del fabricante.

### Ejercicios — capítulo 11

**EX021 — Decisión de parcheo.** *Objetivo:* aplicar las preguntas basadas en el riesgo. *Entradas:* una falla explotable de forma remota en la interfaz web de un controlador del BMS del CVH; la interfaz es alcanzable desde la red corporativa; la corrección del fabricante requiere reiniciar el controlador durante 30 minutos; la ventilación de los quirófanos depende del BMS. *Pasos:* responda las cinco preguntas de la decisión de parcheo basada en el riesgo de este capítulo y haga una recomendación. *Evidencia esperada:* respuestas y recomendación con controles provisionales. *Rúbrica:* 3 = restringir de inmediato el acceso a la interfaz, programar el reinicio con mantenimiento de instalaciones y quirófanos en una ventana planificada, supervisar; 2 = resultado correcto, controles provisionales débiles; 1 = «parchear de inmediato» sin tener en cuenta la ventilación; 0 = nada.

**EX022 — Bastionado verificable.** *Objetivo:* hacer que los controles se puedan comprobar. *Entradas:* tres elementos vagos: «proteger las cuentas», «activar el registro», «bloquear el USB». *Pasos:* reescriba cada uno como una afirmación específica y verificable, con su comprobación. *Evidencia esperada:* tres elementos reescritos. *Rúbrica:* 3 = específicos, observables, con un método de comprobación; 2 = específicos pero sin comprobación; 1 = siguen siendo vagos; 0 = nada.

### Síntesis del capítulo

El SO aplica la separación, los permisos y los privilegios; el mínimo privilegio y la mediación completa son sus ideas rectoras. En los servicios críticos, los dispositivos más duraderos suelen tener las protecciones más débiles, por lo que el bastionado debe ser verificable y el parcheo debe basarse en el riesgo, estar programado y ser reversible.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Siga estudiando — capítulo 11 de 40

[← Capítulo 10](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Probabilidad y estadística

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) aplicar las reglas de la suma, del complemento y de la multiplicación, y decir cuándo los eventos son independientes; (2) usar el teorema de Bayes para interpretar una alerta, incluido el efecto de la tasa base; (3) calcular la probabilidad de al menos una falla en ensayos repetidos y la probabilidad de que haya suficientes de $n$ unidades redundantes disponibles; y (4) resumir datos asimétricos con medianas y percentiles. Se apoya en el capítulo 1 y prepara los capítulos 15, 27 y 29.

### 12.1 Reglas que usará constantemente

Las probabilidades son números entre 0 y 1. La regla del **complemento**: $P(\text{not } A) = 1 - P(A)$. Para eventos **independientes**, $P(A \text{ and } B) = P(A)P(B)$. Para cualesquiera eventos, $P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$: sumar sin restar la intersección cuenta dos veces lo mismo. Los problemas de «al menos uno» se resuelven más fácilmente por el complemento: si una copia de seguridad falla de forma silenciosa en un día dado con probabilidad $p$, de forma independiente cada día, la probabilidad de al menos una falla silenciosa en $n$ días es $1 - (1-p)^n$. La independencia es una suposición, a menudo falsa: dos generadores alimentados desde el mismo depósito de combustible fallan juntos. Estas fallas de **causa común** son la razón de que la redundancia sea más débil de lo que sugiere la regla de la multiplicación.

### 12.2 Probabilidad condicional y Bayes

$P(A \mid B)$ es la probabilidad de $A$ dado que ocurrió $B$. El teorema de Bayes relaciona los dos sentidos:
$$P(\text{malicious} \mid \text{alert}) = \frac{P(\text{alert} \mid \text{malicious})\,P(\text{malicious})}{P(\text{alert})}.$$
Un detector con una **tasa de verdaderos positivos** del 95 % y una **tasa de falsos positivos** del 1 % parece excelente. Si solo 1 evento de cada 1000 es malicioso, la mayoría de las alertas siguen siendo falsas: la **tasa base** domina. Esta es la idea estadística más importante de las operaciones de seguridad, y explica por qué los analistas se ahogan en alertas.

### 12.3 Razonamiento binomial para la redundancia

Si $n$ unidades idénticas están disponibles cada una con probabilidad $1-p$, de forma independiente, el número de unidades disponibles sigue una distribución **binomial**: $P(k \text{ available}) = \binom{n}{k}(1-p)^k p^{n-k}$. Una estación de bombeo que necesita al menos 10 de sus 12 bombas puede calcular con qué frecuencia satisface la demanda. Para la estación de 12 bombas del Lab 6, con cada bomba no disponible el 10 % del tiempo, la suma para 10, 11 y 12 bombas disponibles da 0,889. Un equipo de mantenimiento compartido o una única acometida eléctrica rompen la suposición de independencia, así que la cifra real es menor. Añadir una decimotercera bomba eleva el resultado a cerca de 0,966, que es el tipo de comparación que necesita una solicitud de inversión.

### 12.4 Describir los datos

Los tiempos de detección y de recuperación de incidentes son **asimétricos**: la mayoría son cortos y unos pocos son muy largos. La **media** se ve arrastrada hacia arriba por la cola larga; la **mediana** (el valor central) no; los **percentiles** (el percentil 90, p90) describen la cola. Informe la mediana y el p90 juntos, con el tamaño de la muestra (capítulo 29, Lab 12). El Lab 12 muestra el efecto: su tiempo medio de detección es de 27,2 horas, mientras que la mediana es de 4,0. Para un consejo de administración, la frase «la mitad de los incidentes se detectaron en 4 horas; uno de cada diez tardó más de unas 56» transmite más información que cualquier promedio aislado.

### 12.5 Ejemplo resuelto y Lab 6 (sintético)

**Este caso es sintético.** El servicio de supervisión de Calder Mutual ve 20 000 eventos al día; los analistas estiman que 1 de cada 1000 es malicioso; las tasas del detector son las indicadas arriba. La copia de seguridad nocturna de la telemetría de CW falla de forma silenciosa con probabilidad 0,002 al día. Una estación de bombeo tiene 12 bombas, cada una no disponible el 10 % del tiempo.

```python
# Lab 6 - base rates, alarm volume and repeated trials (synthetic, offline)
from math import comb
prior, tpr, fpr = 0.001, 0.95, 0.01
ppv = tpr * prior / (tpr * prior + fpr * (1 - prior))
print(f"P(malicious | alert) = {ppv:.3f}")
events_per_day = 20_000
print(f"expected false alerts/day = {events_per_day * (1 - prior) * fpr:.0f}; true = {events_per_day * prior * tpr:.0f}")
p_day = 0.002   # chance per day that a given backup fails silently
for days in (30, 365):
    print(f"P(at least one silent backup failure in {days} days) = {1 - (1 - p_day) ** days:.3f}")
n, p = 12, 0.1  # 12 independent pumps, each unavailable 10% of the time
need = 10
print(f"P(at least {need} of {n} available) = {sum(comb(n, k) * (1-p)**k * p**(n-k) for k in range(need, n+1)):.3f}")
```

Salida esperada:

```text
P(malicious | alert) = 0.087
expected false alerts/day = 200; true = 19
P(at least one silent backup failure in 30 days) = 0.058
P(at least one silent backup failure in 365 days) = 0.518
P(at least 10 of 12 available) = 0.889
```

Menos de 1 alerta de cada 11 es real; los analistas se enfrentan a unas 200 alertas falsas al día. Una falla «rara» diaria de la copia de seguridad es más probable que improbable a lo largo de un año, razón por la cual los simulacros de restauración, y no los registros de las copias, son la evidencia que importa. Y una estación que necesita 10 de 12 bombas se queda corta cerca del 11 % del tiempo con estas suposiciones: si las indisponibilidades de las bombas comparten una causa (un único equipo de mantenimiento, una única acometida eléctrica), será peor.

### 12.6 Errores comunes y límites

- Ignorar la tasa base (la falacia del «95 % de precisión»).
- Multiplicar las probabilidades de eventos que comparten una causa.
- Informar una media de tiempos asimétricos sin la mediana ni la cola.
- Tratar como exactas las entradas estimadas; las salidas heredan su incertidumbre.

El Lab 6 pone una cifra a cada uno: una detección del 95 % sigue dando una probabilidad de 0,087 de que una alerta sea real; dos generadores que comparten combustible fallan juntos con mucha más frecuencia que 0,05 al cuadrado (EX024); el tiempo medio de detección de 27,2 horas del Lab 12 no describe ningún incidente; y la tasa diaria de falla de la copia de seguridad de 0,002 es en sí una estimación, por lo que la cifra anual de 0,518 hereda su incertidumbre.

### Ejercicios — capítulo 12

**EX023 — Cambiar la tasa base.** *Objetivo:* ver cómo la probabilidad previa y la tasa de falsos positivos determinan el valor de una alerta. *Entradas:* Lab 6. *Pasos:* calcule $P(\text{malicious}\mid\text{alert})$ para una probabilidad previa de 0,01 y, por separado, para una previa de 0,001 con FPR 0,001. Explique qué cambio ayuda más y qué significa en la operación. *Evidencia esperada:* dos valores y una explicación. *Rúbrica:* 3 = ≈ 0,490 y ≈ 0,487, con una explicación de que reducir la FPR (ajuste, enriquecimiento) es la palanca que controlan los analistas; 2 = solo los valores; 1 = un valor; 0 = nada.

**EX024 — Causa común.** *Objetivo:* cuantificar el efecto de las causas compartidas. *Entradas:* dos generadores de respaldo que fallan al arrancar cada uno con probabilidad 0,05; con probabilidad 0,02, una causa compartida (combustible común contaminado) hace fallar a ambos. *Pasos:* calcule la probabilidad de que fallen ambos suponiendo independencia, después con la causa común (aproximada como $0.02 + 0.05^2$), y comente. *Evidencia esperada:* dos números y un comentario. *Rúbrica:* 3 = 0,0025 frente a ≈ 0,0225, unas nueve veces peor, y un remedio (combustible separado, análisis del combustible); 2 = solo los números; 1 = un número; 0 = nada.

### Síntesis del capítulo

Las reglas de la probabilidad son sencillas; sus suposiciones no lo son. Las tasas base deciden si merece la pena leer una alerta, lo «raro por día» se vuelve «probable por año», la redundancia se debilita por las causas comunes y los datos asimétricos necesitan medianas y percentiles. Declare las suposiciones de independencia y pruebe qué ocurre cuando no se cumplen.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Siga estudiando — capítulo 12 de 40

[← Capítulo 11](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Identidad y acceso

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) distinguir identificación, autenticación y autorización; (2) comparar los factores de autenticación y explicar por qué los métodos resistentes al phishing importan para el acceso remoto a los sistemas críticos; (3) diseñar un acceso basado en roles con segregación de funciones; y (4) realizar una revisión de accesos que encuentre cuentas huérfanas, inactivas, compartidas y con combinaciones tóxicas. Se apoya en el capítulo 6 (conjuntos) y el capítulo 11 (privilegios) y prepara el capítulo 16 (arquitectura) y el capítulo 24 (controles).

### 13.1 Tres preguntas

La **identificación** responde a «¿quién dice usted que es?» (un nombre de usuario). La **autenticación** responde a «demuéstrelo», con algo que usted sabe (una contraseña), tiene (un token o un teléfono) o es (una huella dactilar). La **autorización** responde a «¿qué puede hacer?»: los permisos asociados a la identidad autenticada. Los errores de cada etapa son distintos: una autenticación débil deja entrar a la persona equivocada; una autorización excesiva permite a la persona correcta (o a quien le robó la sesión) hacer demasiado. Las directrices de identidad digital del NIST fijan requisitos para los autenticadores y recomiendan opciones resistentes al phishing para los niveles de garantía más altos ([SP 800-63B](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final)).

### 13.2 Factores y acceso remoto

Las contraseñas se adivinan, se reutilizan y se roban por phishing. Los códigos de un solo uso enviados por SMS o tecleados desde una aplicación añaden un segundo factor, pero una página de inicio de sesión falsa convincente puede retransmitirlos. Los autenticadores **resistentes al phishing** vinculan criptográficamente el inicio de sesión al sitio auténtico, de modo que un sitio falso no recibe nada aprovechable. Para el acceso remoto a la TO y a otros sistemas críticos (la vía del aviso de CPN del capítulo 5), una autenticación fuerte es necesaria pero no suficiente: la sesión debe llegar a un servidor de salto controlado, tener un tiempo limitado, ser aprobada sesión a sesión en el caso de los fabricantes y quedar grabada.

### 13.3 Roles y segregación de funciones

En el **control de acceso basado en roles** (RBAC), los permisos se asocian a roles («scada-operator», «payments-approve») y las personas reciben roles. Los roles hacen manejables las revisiones: se comprueban cincuenta roles, no cincuenta mil permisos individuales. La **segregación de funciones** prohíbe ciertas combinaciones: quien crea un pago no debe aprobarlo; el ingeniero que cambia la lógica de control no debería controlar también el cortafuegos que registra el cambio. Expresada con conjuntos (capítulo 6), una **combinación tóxica** $T$ se infringe cuando $T \subseteq \text{roles}(u)$.

El Lab 7 codifica ambas reglas como conjuntos TOXIC y señala a chloe, que tiene payments-create y payments-approve, y a dev, que tiene scada-engineer y firewall-admin y además lleva 214 días inactivo.

### 13.4 El ciclo de vida de las cuentas y las revisiones

Las cuentas se crean cuando las personas se incorporan (**alta**), se modifican cuando cambian de puesto (**cambio**) y se eliminan cuando se marchan (**baja**). Las fallas se acumulan en cada paso: quienes cambian de puesto conservan roles antiguos («acumulación de privilegios»), las cuentas de quienes se marchan perduran, las cuentas de fabricantes se crean para un proyecto y nunca se eliminan, y las cuentas compartidas de operador hacen que las acciones no se puedan rastrear. Una **revisión de accesos** compara las cuentas con una fuente autorizada (el sistema de RR. HH., el registro de contratos con fabricantes) y con el uso.

El Lab 7 muestra cada falla: *ben* se marchó pero conservó su cuenta, *vendorx* no tiene responsable en RR. HH. y no ha iniciado sesión en 304 días, y *ops1* es compartida. Los datos de uso importan tanto como el estado en RR. HH.: *dev* está activo en RR. HH. pero lleva 214 días inactivo en un rol privilegiado.

### 13.5 Ejemplo resuelto y Lab 7 (sintético)

**Este caso es sintético.** Una revisión conjunta de las cuentas del sistema de control de CPN y del sistema de pagos de Calder Mutual (combinados aquí solo con fines didácticos) usa el estado en RR. HH., el último inicio de sesión y dos combinaciones tóxicas.

```python
# Lab 7 - access review: orphans, dormant accounts and toxic combinations (synthetic, offline)
from datetime import date
TODAY = date(2026, 10, 1)
HR = {"ana": "active", "ben": "left", "chloe": "active", "dev": "active"}
ACCOUNTS = [  # user, roles, last login, shared?
    ("ana",   {"scada-operator"},                       date(2026, 9, 30), False),
    ("ben",   {"scada-engineer"},                       date(2026, 5, 2),  False),
    ("chloe", {"payments-create", "payments-approve"},  date(2026, 9, 29), False),
    ("dev",   {"scada-engineer", "firewall-admin"},     date(2026, 3, 1),  False),
    ("ops1",  {"scada-operator"},                       date(2026, 9, 30), True),
    ("vendorx", {"remote-support"},                     date(2025, 12, 1), False),
]
TOXIC = [{"payments-create", "payments-approve"}, {"scada-engineer", "firewall-admin"}]
for user, roles, last, shared in ACCOUNTS:
    issues = []
    if user not in HR: issues.append("no HR owner")
    elif HR[user] != "active": issues.append("owner has left")
    if (TODAY - last).days > 90: issues.append(f"dormant {(TODAY - last).days} d")
    if shared: issues.append("shared account")
    issues += ["toxic: " + "+".join(sorted(t)) for t in TOXIC if t <= roles]
    print(f"{user:8} {', '.join(issues) if issues else 'ok'}")
```

Salida esperada:

```text
ana      ok
ben      owner has left, dormant 152 d
chloe    toxic: payments-approve+payments-create
dev      dormant 214 d, toxic: firewall-admin+scada-engineer
ops1     no HR owner, shared account
vendorx  no HR owner, dormant 304 d
```

Acciones: desactivar ya a *ben* (baja); retirar uno de los roles de pago de *chloe*; retirar los roles privilegiados inactivos de *dev* y preguntar si necesita alguno; *ops1* es un inicio de sesión compartido de la sala de control (habitual en operaciones 24/7, donde importa un relevo rápido), así que conviene sustituirlo por inicios de sesión individuales con cambio rápido de usuario o, como mínimo, registrar quién está de turno; *vendorx* debería desactivarse y reactivarse en cada sesión de soporte bajo un patrocinador nombrado. Observe lo que el script no puede ver: si el rol de *ana* sigue correspondiendo a su trabajo.

### 13.6 Errores comunes y límites

- Equiparar «autenticado» con «autorizado».
- Revisiones que confirman que las cuentas existen en lugar de si son necesarias.
- Eliminar las cuentas compartidas de una sala de control sin una alternativa viable, de modo que el personal comparte contraseñas en su lugar.
- Olvidar las cuentas de servicio y de fabricantes, que no tienen registro en RR. HH.

En el Lab 7, el script confirma que la cuenta de *ana* está «ok» solo en el sentido de que está activa y no inactiva; si todavía necesita `scada-operator` es algo que debe decir su responsable. Eliminar *ops1* sin más llevaría a la sala de control a compartir la contraseña de una persona, lo cual es peor. Y tanto *ops1* como *vendorx* muestran «no HR owner», que es la señal de que las cuentas de servicio y de fabricantes necesitan otra fuente autorizada, como el registro de contratos.

### Ejercicios — capítulo 13

**EX025 — Diseñar los roles.** *Objetivo:* aplicar el mínimo privilegio y la segregación de funciones. *Entradas:* el CEDC necesita operadores de llamadas, despachadores, supervisores, un administrador del CAD y un ingeniero de soporte del fabricante. *Pasos:* defina cinco roles con sus permisos clave y dos combinaciones tóxicas. *Evidencia esperada:* tabla de roles y combinaciones. *Rúbrica:* 3 = roles razonables de mínimo privilegio, pares tóxicos justificados (p. ej., administrador del CAD + administrador del registro de auditoría; soporte del fabricante + acceso permanente); 2 = roles sin combinaciones; 1 = vago; 0 = nada.

**EX026 — Ampliar la revisión.** *Objetivo:* añadir una regla. *Entradas:* Lab 7. *Pasos:* añada una comprobación que señale cualquier cuenta con un rol privilegiado (`scada-engineer`, `firewall-admin`, `payments-approve`) que no se haya vuelto a aprobar en 180 días, dado un nuevo campo `approved` (una fecha). Elija las fechas de modo que al menos una cuenta quede señalada y muestre la salida. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = lógica correcta, datos de prueba elegidos para mostrar casos señalados y no señalados; 2 = funciona, prueba débil; 1 = error de lógica; 0 = nada.

### Síntesis del capítulo

La identidad responde a tres preguntas distintas. Use una autenticación fuerte y resistente al phishing para el acceso remoto crítico, conceda permisos mediante roles, prohíba las combinaciones tóxicas y revise las cuentas frente a fuentes autorizadas y al uso real. Las cuentas compartidas y de fabricantes necesitan alternativas viables, no solo prohibiciones.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Siga estudiando — capítulo 13 de 40

[← Capítulo 12](#ch-12) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos de privacidad

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) explicar la diferencia entre seguridad y privacidad; (2) aplicar principios de protección de datos como la licitud, la limitación de la finalidad, la minimización y la limitación del plazo de conservación; (3) identificar datos personales en los sistemas de los servicios críticos, incluidos los datos que se vuelven personales al combinarse; y (4) recomendar diseños que protejan la privacidad para la supervisión y los datos de incidentes. Se apoya en el capítulo 9 (datos) y el capítulo 10 (ética) y prepara el capítulo 29 (operaciones) y los requisitos éticos del proyecto final.

### 14.1 La seguridad no es privacidad

La seguridad protege los sistemas y la información frente al acceso, la modificación y la pérdida no autorizados. La **privacidad** se ocupa de si el tratamiento de información sobre las personas, incluso el tratamiento autorizado, es apropiado, proporcionado y justo. Una base de datos hospitalaria perfectamente segura puede vulnerar igualmente la privacidad si se usa para una finalidad de la que nunca se informó a los pacientes. El [NIST Privacy Framework](https://www.nist.gov/privacy-framework) trata el riesgo para la privacidad como algo que surge del propio tratamiento de datos, solapado con el riesgo de ciberseguridad pero distinto de él.

La detección de clones de CT es el ejemplo: almacenar de forma segura dos años de validaciones seguiría siendo un problema de privacidad.

### 14.2 Principios

El Reglamento General de Protección de Datos de la UE establece principios que se reproducen ampliamente en otros lugares: licitud, lealtad y transparencia; limitación de la finalidad; minimización de datos; exactitud; limitación del plazo de conservación; integridad y confidencialidad; y responsabilidad proactiva ([Regulation (EU) 2016/679, Article 5](https://eur-lex.europa.eu/eli/reg/2016/679/oj)). Los datos de salud son una **categoría especial** que exige condiciones adicionales. *Nota para el lector hispanohablante:* en España, el RGPD se complementa con la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales; en América Latina rige la ley de cada país, por ejemplo la Ley 25.326 en Argentina o la Ley 1581 de 2012 en Colombia. No hace falta que se convierta en jurista, pero debe reconocer cuándo una cuestión de diseño es también una cuestión de protección de datos e implicar al delegado de protección de datos de la organización, y nunca debe presentar el resumen de este libro como asesoramiento jurídico para un caso concreto.

### 14.3 Datos personales en lugares inesperados

Los servicios críticos tienen datos personales evidentes (historias clínicas, cuentas bancarias, llamadas de emergencia) y otros menos evidentes. Las lecturas de un contador inteligente a intervalos cortos pueden revelar cuándo hay alguien en casa. Los datos de validación de una tarjeta de transporte trazan los desplazamientos de una persona. Los registros de seguridad anotan quién inició sesión, desde dónde y cuándo: datos personales sobre el personal. La **combinación** importa: ni un código postal ni una fecha de nacimiento suelen identificar a alguien por sí solos, pero junto con el sexo a menudo sí. La seudonimización (sustituir los nombres por códigos) reduce el riesgo, pero no es anonimización si la clave existe o si la reidentificación es posible.

### 14.4 La privacidad en las operaciones de seguridad

La supervisión de seguridad recoge, por diseño, datos sobre las personas. Una práctica que protege la privacidad: recoger lo que necesita la finalidad de detección, no todo lo disponible; restringir el acceso a los registros en bruto; fijar plazos de conservación; seudonimizar donde el análisis no necesita nombres; documentar la finalidad y la base jurídica; y, en un incidente, compartir indicadores (direcciones, hashes de archivos) en lugar de datos personales siempre que sea posible. Durante una brecha que afecte a datos personales pueden aplicarse obligaciones de notificación en plazos cortos, por lo que los planes de incidentes incluyen al delegado de protección de datos desde el principio.

El diseño revisado de CT aplica cuatro de estas prácticas: detalle durante 30 días, seudónimos con clave, dos analistas con nombre y una finalidad declarada.

### 14.5 Ejemplo resuelto: analítica de validaciones de CT (sintético)

**Este caso es sintético.** El equipo de seguridad de Calder Transit quiere detectar tarjetas de transporte clonadas buscando la misma tarjeta usada en dos estaciones demasiado alejadas en un tiempo demasiado corto. El diseño propuesto copia todas las validaciones de tarjeta (ID de la tarjeta, estación, hora) durante dos años en la plataforma de analítica de seguridad. Una revisión de privacidad pregunta: ¿hacen falta dos años? (La detección de clones necesita de minutos a días; conservar el detalle completo durante 30 días y después agregar). ¿Hace falta el ID de la tarjeta en claro? (Un seudónimo con clave basta para emparejar; solo los casos confirmados se reidentifican, por parte del equipo de fraude). ¿Quién puede consultarlo? (Dos analistas con nombre, con registro). ¿Se está creando como efecto secundario un historial de viajes de los pasajeros? (Sí, y por eso el diseño limita la conservación y el acceso). El diseño revisado cumple la finalidad de detección con una fracción del riesgo para la privacidad.

### 14.6 Actividad práctica

Elija un servicio que use (una tarjeta de transporte, un contador inteligente, una aplicación de un hospital). A partir de su aviso de privacidad público, enumere los datos personales recogidos, las finalidades declaradas y la conservación. Identifique un dato cuya finalidad no esté clara y redacte una pregunta que podría enviar al proveedor. Fíjese en si el aviso indica la conservación en días o años, o solo «durante el tiempo necesario»; esto último es algo que merece la pena preguntar. Anote si la supervisión de seguridad figura siquiera como finalidad. Redacte su pregunta con cortesía y precisión, por ejemplo preguntando cuánto tiempo se conservan los datos de cada viaje antes de agregarlos y quién puede acceder a ellos.

### 14.7 Errores comunes y límites

- «Somos seguros, por lo tanto cumplimos».
- Recogerlo todo «por si resulta útil».
- Llamar anónimos a los datos seudonimizados.
- Olvidar los datos del personal en los registros.
- Dar conclusiones jurídicas sin los asesores jurídicos y de protección de datos de la organización.

Cada uno aparece en los ejemplos de este capítulo. La copia original de dos años de validaciones de CT era segura y aun así desproporcionada. «Por si resulta útil» es la forma en que el ID completo de la tarjeta acabó en la plataforma de analítica. Los seudónimos con clave son reversibles por el equipo de fraude, así que no son anónimos. La propuesta de supervisión de accesos del CVH en el EX027 registra nombres del personal, que son datos personales del personal. Y ninguno de estos diseños debería calificarse de lícito sin el delegado de protección de datos.

### Ejercicios — capítulo 14

**EX027 — Minimizar un registro.** *Objetivo:* aplicar la minimización a la supervisión de seguridad. *Entradas:* una propuesta del CVH para registrar cada acceso del personal a las historias clínicas con el nombre completo del paciente, el diagnóstico, el nombre del miembro del personal, la estación de trabajo y la hora, conservados indefinidamente, para detectar accesos inapropiados. *Pasos:* proponga un diseño minimizado que cumpla la misma finalidad. *Evidencia esperada:* lista de campos, conservación, acceso y una frase sobre la finalidad. *Rúbrica:* 3 = identificador de la historia en lugar del diagnóstico, conservación definida, acceso restringido, finalidad declarada, personal informado; 2 = parcial; 1 = «registrar menos» sin diseño; 0 = nada.

**EX028 — Riesgo de combinación.** *Objetivo:* reconocer la reidentificación. *Entradas:* CW publica el consumo horario «anonimizado» de cada contador con el código postal y el tipo de inmueble. *Pasos:* explique dos riesgos de reidentificación y dos mitigaciones. *Evidencia esperada:* explicación. *Rúbrica:* 3 = los códigos postales pequeños con tipos de inmueble únicos identifican hogares, la ocupación puede inferirse de los patrones horarios; mitigaciones: umbrales de agregación, tiempo o ubicación menos detallados, acuerdos de acceso; 2 = uno de cada; 1 = vago; 0 = nada.

### Síntesis del capítulo

La privacidad pregunta si el tratamiento de datos sobre las personas es apropiado, no solo si es seguro. Aplique la limitación de la finalidad, la minimización y la limitación del plazo de conservación (especialmente a la propia supervisión de seguridad), reconozca que las combinaciones reidentifican e implique a especialistas en protección de datos en lugar de ofrecer conclusiones jurídicas.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Siga estudiando — capítulo 14 de 40

[← Capítulo 13](#ch-13) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Evidencia y medición

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) distinguir una medición, un indicador y una afirmación; (2) juzgar la evidencia por su fuente, su método, su actualidad y su independencia; (3) diseñar una métrica de seguridad válida, fiable y difícil de manipular; y (4) usar el análisis de sensibilidad para decidir si una evidencia incierta es suficiente para una decisión. Se apoya en los capítulos 1, 4 y 12 y prepara el capítulo 18 (métodos de investigación), el capítulo 27 (verificación) y el capítulo 37 (revisión de la evidencia).

### 15.1 Qué cuenta como evidencia

Una **afirmación** es un enunciado de que algo es cierto («nuestras copias de seguridad pueden restaurar el sistema de despacho en cuatro horas»). La **evidencia** es lo que la respalda o la debilita. La evidencia varía en solidez. Una **demostración** (un simulacro de restauración cronometrado sobre la configuración de producción, el mes pasado) es más sólida que un **documento** (una política de copias de seguridad), que a su vez es más sólido que una **aseveración** («el fabricante dice que funciona»). Hágale cuatro preguntas a cualquier evidencia: *Fuente*: ¿quién la produjo y tiene interés en la respuesta? *Método*: ¿cómo se produjo y podría alguien repetirlo? *Actualidad*: ¿sigue describiendo el sistema tal como es ahora? *Independencia*: ¿la comprobó alguien distinto de quien hizo la afirmación?

### 15.2 Medición y métricas

Una **medición** es un valor obtenido mediante un procedimiento definido (el tiempo de restauración en minutos, medido desde el inicio hasta la primera transacción de despacho correcta). Un **indicador** o **métrica** es una medición que se usa para seguir algo que nos importa. Las buenas métricas son **válidas** (miden lo que importa: el porcentaje de activos críticos con una restauración probada, no el número de trabajos de copia), **fiables** (dos personas que miden obtienen el mismo resultado), **oportunas** y **difíciles de manipular**. Se aplica la advertencia de Goodhart: en cuanto una medida se convierte en objetivo, la gente optimiza la medida. Una métrica de parcheo como el «porcentaje de sistemas parcheados en 30 días» incentiva excluir del denominador los sistemas difíciles; informe el denominador y las exclusiones.

### 15.3 Incertidumbre y sensibilidad

La mayor parte de la evidencia de seguridad es incierta: muestras pequeñas (capítulo 12), estimaciones (capítulo 1), indicadores indirectos. El **análisis de sensibilidad** pregunta cuánto cambia la decisión cuando cambia una entrada incierta. Si una recomendación se mantiene en todo el intervalo plausible, la evidencia es adecuada para esa decisión aunque sea imprecisa. Si se invierte, hay que reunir mejor evidencia sobre esa entrada o tomar una decisión robusta (elegir la opción que es aceptable en todo el intervalo). Es un antídoto práctico tanto contra la falsa precisión como contra la parálisis.

El Lab 1 es el modelo: B sigue por delante cuando cualquiera de las probabilidades se reduce a la mitad o se duplica.

### 15.4 Ejemplo resuelto: ¿se puede restaurar el despacho del CEDC? (sintético)

**Este caso es sintético.** El consejo del CEDC pregunta: «¿Podemos restaurar el despacho asistido por ordenador en cuatro horas tras un ransomware?». Evidencia disponible:

| Evidencia | Tipo | Fuente | Actualidad | ¿Independiente? |
|---|---|---|---|---|
| La política de copias indica copias nocturnas y un objetivo de restauración de 4 h | Documento | Equipo de TI | 2024 | No |
| El software de copias informa de 362/365 trabajos correctos | Medición (de la copia, no de la restauración) | Herramienta | Último año | No |
| Simulacro de restauración: base de datos restaurada en 2 h 40 min, aplicación no probada | Demostración parcial | Equipo de TI | Hace 8 meses | No |
| Declaración del fabricante: «una restauración completa suele tardar menos de 3 horas» | Aseveración | Fabricante | Sin fecha | No |

Valoración: ninguna evidencia demuestra la *afirmación*: una restauración de todo el servicio de despacho, incluidos los servidores de aplicaciones, las integraciones y las credenciales, en condiciones de ransomware (en las que el propio servidor de copias puede estar cifrado). La respuesta honesta al consejo es «desconocido, con evidencia parcial de que la base de datos por sí sola se restaura en menos de cuatro horas». Recomendación: un simulacro de restauración de extremo a extremo en un entorno aislado, observado por auditoría interna, que mida el tiempo hasta el primer despacho de prueba correcto; y la confirmación de que al menos una copia está fuera de línea o es inmutable.

### 15.5 Actividad práctica

Tome una afirmación sobre un servicio que use («mi teléfono hace copia de seguridad de mis fotos»). Enumere la evidencia que tiene, clasifique cada elemento por tipo, fuente, actualidad e independencia, y diseñe una prueba que demostraría la afirmación. No ejecute nada en sistemas que no sean de su propiedad. Para la copia de un teléfono, la prueba más sólida es restaurar una foto en otro dispositivo de su propiedad, cronometrando y anotando la fecha. El «última copia: hoy» de una aplicación de copias es una medición de la copia, no de la restauración.

### 15.6 Errores comunes y límites

- Tratar el éxito de la copia como evidencia de restauración.
- Métricas que cuentan actividad en lugar de resultados.
- Denominadores que excluyen en silencio los casos más difíciles.
- Ignorar el interés de la fuente de la evidencia.
- Exigir una precisión que la decisión no necesita, o aceptar una confianza que no se ha ganado.

La tabla de evidencia del CEDC muestra el primero: 362 de 365 trabajos correctos no dicen nada sobre restaurar la aplicación. El segundo aparece cuando un equipo informa del número de trabajos de copia en lugar de las restauraciones probadas. El tercero es la métrica de parcheo con los sistemas difíciles fuera. El cuarto es el «menos de 3 horas» sin fecha del fabricante. El quinto corta en ambos sentidos: el consejo no necesita minutos, pero no puede aceptar un «probablemente bien».

### Ejercicios — capítulo 15

**EX029 — Calificar la evidencia.** *Objetivo:* aplicar las cuatro preguntas. *Entradas:* la afirmación «el servicio de tarjetas de Calder Mutual conmuta a su segundo centro de datos en 15 minutos»; evidencia: diagrama de arquitectura (2025), el informe de la prueba de conmutación del año pasado elaborado por el equipo de operaciones (14 min), una nota del auditor de que la prueba se anunció con una semana de antelación. *Pasos:* califique cada elemento e indique lo que la evidencia muestra y lo que no. *Evidencia esperada:* tabla y dos frases. *Rúbrica:* 3 = reconoce la prueba como una demostración real pero anunciada y no independiente, y pide una prueba no anunciada u observada de forma independiente con carga realista; 2 = parcial; 1 = acepta la afirmación; 0 = nada.

**EX030 — Corregir una métrica.** *Objetivo:* diseñar una métrica válida y difícil de manipular. *Entradas:* «número de cursos de concienciación sobre phishing completados». *Pasos:* proponga una métrica mejor para el riesgo de robo de credenciales por phishing, defina su medición y nombre una forma en que podría manipularse. *Evidencia esperada:* definición y riesgo de manipulación. *Rúbrica:* 3 = métrica orientada a resultados (p. ej., proporción de cuentas privilegiadas con autenticación resistente al phishing, o tasa de notificación en simulaciones autorizadas) con procedimiento definido y un riesgo de manipulación honesto; 2 = mejor pero poco definida; 1 = métrica de actividad; 0 = nada.

### Síntesis del capítulo

La evidencia tiene una fuente, un método, una fecha y un grado de independencia. Mida resultados en lugar de actividad, informe los denominadores y use el análisis de sensibilidad para decidir si una evidencia incierta es suficiente. «Desconocido, con evidencia parcial» suele ser la respuesta más honesta y útil.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Siga estudiando — capítulo 15 de 40

[← Capítulo 14](#ch-14) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Arquitectura de seguridad

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) aplicar los principios de diseño clásicos: mínimo privilegio, valores predeterminados a prueba de fallos, economía de mecanismos, mediación completa y separación de privilegios; (2) describir una arquitectura de referencia por capas para un operador de servicios críticos, desde la empresa hasta el campo; (3) explicar la defensa en profundidad y la confianza cero, y sus límites en la tecnología operativa; y (4) diseñar un acceso remoto seguro para fabricantes. Se apoya en los capítulos 7, 11 y 13 y prepara el capítulo 21 (modelos de sistemas) y el capítulo 24 (controles).

### 16.1 Principios que perduran

Los principios de Saltzer y Schroeder de 1975 siguen enmarcando la arquitectura de seguridad ([Saltzer and Schroeder](https://doi.org/10.1109/PROC.1975.9939)): **economía de mecanismos** (mantenerlo lo bastante simple como para poder verificarlo); **valores predeterminados a prueba de fallos** (denegar salvo que se permita); **mediación completa** (comprobar cada acceso); **diseño abierto** (la seguridad no debe depender del secreto del diseño); **separación de privilegios** (exigir más de una condición: dos personas, dos llaves); **mínimo privilegio**; **mínimo mecanismo común** (minimizar los componentes compartidos); y **aceptabilidad psicológica** (si es demasiado difícil de usar, la gente lo esquiva). Cada uno es una lente para revisar un diseño: «¿qué no está mediado aquí?, ¿qué se comparte?, ¿qué esquivarán los operadores a las 03:00?».

### 16.2 Una arquitectura de referencia por capas

Los operadores de servicios críticos suelen separar: la zona **corporativa** (correo electrónico, ofimática, sistemas de negocio); una **DMZ** para el intercambio de datos (réplicas del historiador, servidores de parches, servidores de salto para el acceso remoto); **operaciones/control** (servidores SCADA, HMI, estaciones de trabajo de ingeniería); **campo** (controladores, RTU, relés de protección); y los sistemas de **seguridad funcional**, que actúan de forma independiente para evitar daños. El tráfico entre capas pasa por conductos con reglas explícitas (capítulo 7). La guía de TO del NIST y la serie ISA/IEC 62443 describen estas arquitecturas ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). Lo importante no es el dibujo, sino la **propiedad** que debe garantizar: ninguna vía directa desde internet o el correo electrónico hasta nada que controle un proceso físico.

### 16.3 Defensa en profundidad y confianza cero

La **defensa en profundidad** superpone controles independientes para que una sola falla no sea catastrófica: segmentación, bastionado, autenticación, supervisión, copias de seguridad, respaldo manual. Su debilidad es el **modo común**: las capas que comparten una cuenta de administrador o un servidor de gestión caen juntas. La **confianza cero** elimina la confianza implícita basada en la ubicación en la red; cada solicitud se autentica y autoriza por recurso ([NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)). En la TI corporativa es una dirección sólida. En la TO, muchos dispositivos no pueden autenticar solicitudes individuales, por lo que las ideas de confianza cero se aplican sobre todo en los límites (usuarios, estaciones de trabajo de ingeniería, acceso remoto), mientras la segmentación protege a los dispositivos que no pueden protegerse por sí mismos.

### 16.4 Acceso remoto

Los fabricantes y los ingenieros necesitan acceso remoto; el acceso remoto sin control es una de las vías de entrada más comunes a la TO. Un patrón defendible: el acceso termina en un **servidor de salto** en la DMZ, nunca directamente en la zona de control; autenticación **multifactor resistente al phishing**; **aprobación por sesión** de los fabricantes por parte del operador de turno; cuentas de **tiempo limitado**; **grabación de sesiones**; y un **interruptor de corte** que la sala de control pueda usar. Cada elemento responde a una falla concreta.

El rediseño de CPN usa todos los elementos: un servidor de salto en la DMZ, cuentas de fabricantes activadas por ticket durante un máximo de cuatro horas, MFA resistente al phishing, sesiones grabadas y un interruptor en la sala de control. Lo que no puede impedir es el mal uso dentro de una sesión de fabricante aprobada de cuatro horas.

### 16.5 Ejemplo resuelto: el acceso remoto de CPN (sintético)

**Este caso es sintético.** El diseño actual de CPN: la pasarela VPN-G expuesta a internet (capítulo 5) coloca a los usuarios directamente en la red de control; tres fabricantes tienen cuentas permanentes; solo contraseñas. Rediseño: VPN-G actualizada y trasladada para terminar en un servidor de salto en la DMZ; cuentas de fabricantes desactivadas por defecto y activadas por ticket por el supervisor de la sala de control durante un máximo de cuatro horas; MFA resistente al phishing para el personal; sesiones grabadas en un servidor que los fabricantes no pueden alcanzar; un interruptor físico en la sala de control que desactiva el conducto de acceso remoto. Riesgo residual, declarado: una sesión de fabricante aprobada sigue gozando de confianza durante su ventana; la grabación facilita la detección y la rendición de cuentas, pero no impide el mal uso en tiempo real.

### 16.6 Actividad práctica

Dibuje la arquitectura de Calder Water del capítulo 7 con sus zonas y los tres conductos permitidos. Anote en cada conducto el principio al que sirve y el control que lo aplica. Marque el componente cuyo compromiso haría más daño y explique por qué. En la arquitectura de CW, cada conducto sirve a un principio: la vista HTTPS de la red corporativa a la DMZ aplica el mínimo privilegio, la lectura OPC UA del recolector de la DMZ aplica la mediación completa en el conducto, y el sondeo Modbus del SCADA al campo se apoya en los valores predeterminados a prueba de fallos al denegar todo lo demás. El servidor SCADA es un firme candidato a ser el componente cuyo compromiso más daño haría, porque puede ver y dar órdenes a todos los controladores de campo.

### 16.7 Errores comunes y límites

- Diagramas de arquitectura que muestran las conexiones previstas, no las reales.
- Máquinas con «doble conexión» que unen zonas y esquivan el conducto.
- Capas que comparten administradores, credenciales o herramientas de gestión.
- Aplicar eslóganes de confianza cero a dispositivos que no pueden autenticarse.

En el caso de CW, la conexión RDP del Lab 4 desde la red corporativa directamente al control es el primer error: una vía que el diagrama no muestra. Un portátil de ingeniería con doble conexión es la causa habitual. El servidor de gestión del CVH que administra cortafuegos, protección de endpoints y copias de seguridad con una sola cuenta (EX032) es el tercero. El cuarto se aplica a las RTU y los PLC.

### Ejercicios — capítulo 16

**EX031 — Revisión por principios.** *Objetivo:* usar los principios como lentes de revisión. *Entradas:* el diseño original de acceso remoto de CPN del ejemplo resuelto de este capítulo. *Pasos:* nombre cuatro principios de Saltzer–Schroeder que infringe y cómo. *Evidencia esperada:* cuatro pares principio–infracción. *Rúbrica:* 3 = cuatro correctos (mínimo privilegio, valores predeterminados a prueba de fallos, mediación completa, separación de privilegios o mínimo mecanismo común) con una explicación específica; 2 = tres; 1 = uno o dos; 0 = nada.

**EX032 — Modo común.** *Objetivo:* encontrar dependencias compartidas ocultas. *Entradas:* el CVH tiene cortafuegos de segmentación, protección de endpoints y copias de seguridad, todo administrado desde un único servidor de gestión con una única cuenta de administrador del dominio. *Pasos:* explique el riesgo de modo común y proponga dos cambios. *Evidencia esperada:* explicación y cambios. *Rúbrica:* 3 = el compromiso de la cuenta o del servidor desactiva las tres capas; cambios como niveles y credenciales de administración separados y copias fuera de línea; 2 = un cambio; 1 = vago; 0 = nada.

### Síntesis del capítulo

La arquitectura convierte los principios en propiedades aplicadas: ninguna vía directa desde internet hasta nada que mueva el mundo físico. Superponga controles independientes, vigile los modos comunes, aplique la confianza cero donde los dispositivos pueden participar y segmente donde no pueden, y trate el acceso remoto como el conducto más importante que hay que diseñar bien.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Siga estudiando — capítulo 16 de 40

[← Capítulo 15](#ch-15) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Conceptos de criptografía

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) explicar qué garantiza y qué no garantiza cada uno de estos elementos: el hash, el cifrado simétrico, los códigos de autenticación de mensajes, el cifrado de clave pública y las firmas digitales; (2) explicar por qué la integridad y la autenticidad, más que el secreto, son las necesidades criptográficas de los sistemas de control; (3) usar HMAC con un número de secuencia para rechazar órdenes alteradas y reproducidas; y (4) hacer que un registro deje evidencia de manipulación con una cadena de hashes y un ancla externa. Se apoya en los capítulos 5 y 8 y prepara el capítulo 24 (controles) y el capítulo 29 (operaciones).

### 17.1 Las herramientas y sus garantías

Una **función hash criptográfica** como SHA-256 transforma cualquier entrada en un resumen de tamaño fijo; es inviable encontrar dos entradas con el mismo resumen o recuperar la entrada ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)). Un hash por sí solo no demuestra nada sobre *quién* produjo los datos: cualquiera puede volver a calcularlo. El **cifrado simétrico** (p. ej., AES, [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final)) proporciona confidencialidad con una clave compartida. Un **código de autenticación de mensajes** (MAC) como HMAC ([RFC 2104](https://www.rfc-editor.org/rfc/rfc2104); [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final)) permite a quien tiene la clave compartida verificar que un mensaje lo produjo otro poseedor de la clave y que no se alteró. La criptografía de **clave pública** ([Diffie and Hellman, 1976](https://doi.org/10.1109/TIT.1976.1055638); [Rivest, Shamir and Adleman, 1978](https://doi.org/10.1145/359340.359342)) permite las **firmas digitales**: cualquiera con la clave pública puede verificar y solo quien tiene la clave privada puede firmar, lo que constituye la base del firmware firmado y de los certificados. Protocolos como TLS 1.3 combinan estos elementos para ofrecer canales autenticados y cifrados ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)).

### 17.2 Lo que necesitan los sistemas de control

En una orden a un interruptor, el secreto rara vez es lo importante; lo son la **autenticidad** (procede del centro de control), la **integridad** (no se alteró) y la **frescura** (no es una orden antigua reproducida). Un MAC proporciona las dos primeras. La frescura necesita un **número de secuencia** o una marca de tiempo dentro del mensaje autenticado, y un receptor que rechace todo lo que no sea más reciente que el último valor aceptado. Sin frescura, un atacante que grabó ayer una orden «OPEN» válida puede reproducirla hoy.

El Lab 8 demuestra ambas cosas: el nombre del interruptor alterado no supera el MAC y la secuencia 41 se rechaza una vez que ya se ha aceptado.

### 17.3 Las claves son la parte difícil

La criptografía traslada el problema de proteger los datos a proteger las claves. Quién genera las claves, dónde se almacenan, cómo se rotan y revocan, y qué ocurre cuando se filtra la clave de un dispositivo de campo: esto es lo que determina la seguridad real. Las claves nunca deben estar incrustadas en código publicado (la clave del Lab 8 es pública a propósito), nunca deben compartirse entre todos los dispositivos y, cuando sea posible, deben residir en hardware. Planificar con antelación también importa: el NIST finalizó sus primeras normas de criptografía poscuántica en 2024 ([NIST, 2024](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)), y una infraestructura con vidas útiles de 20 años necesita la capacidad de cambiar de algoritmo («agilidad criptográfica»).

### 17.4 Ejemplo resuelto y Lab 8 (sintético)

**Este caso es sintético.** CPN autentica las órdenes a los interruptores con HMAC-SHA-256 sobre un mensaje que contiene un número de secuencia, y mantiene un registro encadenado por hashes de las acciones de los operadores cuya cabeza más reciente se copia cada hora en un servidor separado (el **ancla**).

```python
# Lab 8 - HMAC message authentication and a hash-chained log (synthetic; DEMO KEY ONLY, offline)
import hmac, hashlib
KEY = b"demo-key-published-in-a-textbook-never-use"
def tag(msg): return hmac.new(KEY, msg, hashlib.sha256).hexdigest()[:16]
cmd = b"seq=41;breaker=F7;op=OPEN"
t = tag(cmd)
print("tag:", t)
print("valid original:", hmac.compare_digest(t, tag(cmd)))
print("valid altered :", hmac.compare_digest(t, tag(b"seq=41;breaker=F2;op=OPEN")))
last_seq = 41
print("replay of seq 41 accepted?", 41 > last_seq)
# hash chain: each entry commits to the previous head
def chain(entries):
    head, heads = "0" * 64, []
    for e in entries:
        head = hashlib.sha256((head + e).encode()).hexdigest(); heads.append(head)
    return heads
log = ["08:00 login ana", "08:05 setpoint PS2 4.1m", "08:09 logout ana"]
good = chain(log)
log[1] = "08:05 setpoint PS2 2.0m"
bad = chain(log)
print("anchored head:", good[-1][:12], "| recomputed after edit:", bad[-1][:12])
print("first differing entry:", next(i for i, (a, b) in enumerate(zip(good, bad)) if a != b))
```

Salida esperada:

```text
tag: 347e6a26d1844d03
valid original: True
valid altered : False
replay of seq 41 accepted? False
anchored head: c5754d1d1639 | recomputed after edit: 65e0b2a20fac
first differing entry: 1
```

El nombre del interruptor alterado no supera la verificación; el número de secuencia reproducido se rechaza; el registro editado ya no coincide con la cabeza anclada, y la comparación muestra la primera entrada alterada. Truncar la etiqueta a 64 bits mantiene breve la salida impresa; los sistemas reales usan la etiqueta completa o un truncamiento normalizado. La cadena de hashes detecta la edición **solo** si el ancla está fuera del alcance de quien edita: alguien que controla tanto el registro como el ancla puede reconstruir toda la cadena.

### 17.5 Errores comunes y límites

- Usar un hash simple donde se necesita un MAC o una firma.
- Autenticar mensajes sin frescura.
- Comparar etiquetas con `==` en lugar de con una comparación de tiempo constante.
- Una sola clave compartida para todos los dispositivos.
- Creer que el cifrado hace digno de confianza un extremo comprometido.

En el Lab 8, un SHA-256 simple de la orden permitiría a cualquiera que la cambie calcular un resumen nuevo. El MAC sin `seq=` aceptaría la orden OPEN de ayer. El laboratorio usa `hmac.compare_digest` en lugar de `==`. Una sola clave en todas las RTU significa que una clave filtrada compromete la red. Y el cifrado no ayudaría si la propia HMI del centro de control envía órdenes falsificadas.

### Ejercicios — capítulo 17

**EX033 — Elegir la primitiva.** *Objetivo:* asociar necesidades con herramientas. *Entradas:* (a) actualizaciones de firmware del fabricante para las bombas de infusión del CVH; (b) órdenes del centro de control de CPN a sus propias RTU; (c) historias clínicas en un portátil perdido; (d) detectar ediciones en un registro de auditoría. *Pasos:* elija una primitiva para cada caso y justifíquela. *Evidencia esperada:* cuatro elecciones. *Rúbrica:* 3 = firmas, MAC con frescura (o un canal autenticado), cifrado simétrico con protección de la clave, cadena de hashes con ancla externa; 2 = una errónea; 1 = dos erróneas; 0 = nada.

**EX034 — Romper el ancla.** *Objetivo:* razonar sobre la confianza en el ancla. *Entradas:* Lab 8. *Pasos:* explique cómo un administrador con acceso de escritura tanto al servidor de registros como al ancla podría ocultar una edición, y proponga dos cambios de diseño que lo impidan. *Evidencia esperada:* descripción del ataque y cambios. *Rúbrica:* 3 = recalcular la cadena y sobrescribir el ancla; cambios: ancla custodiada por otro equipo u otro sistema con almacenamiento de solo anexado, publicación externa periódica o marcas de tiempo firmadas; 2 = un cambio; 1 = solo la descripción; 0 = nada.

### Síntesis del capítulo

Cada primitiva garantiza algo concreto: los hashes detectan cambios solo frente a una referencia de confianza, los MAC y las firmas dan autenticidad, los números de secuencia dan frescura y el cifrado da secreto. En los sistemas de control, lo que más importa es la autenticidad, la integridad y la frescura, y la seguridad real depende de la gestión de claves y de mantener las anclas fuera del alcance de un atacante.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Siga estudiando — capítulo 17 de 40

[← Capítulo 16](#ch-16) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Métodos de investigación I

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) convertir un tema en una pregunta investigable; (2) elegir entre diseños descriptivos, comparativos, experimentales y de estudio de caso; (3) buscar, cribar y resumir la bibliografía de forma sistemática y registrar cómo lo hizo; y (4) identificar las amenazas a la validez en un estudio de seguridad. Se apoya en los capítulos 4, 12 y 15 y prepara el capítulo 23 (métodos de riesgo), el capítulo 33 (métodos de investigación II) y la propuesta del proyecto final (capítulo 35).

### 18.1 Del tema a la pregunta

«El ransomware en los hospitales» es un tema. Una **pregunta de investigación** es lo bastante específica como para que la evidencia pueda responderla y alguien pueda discrepar: «En los incidentes de ransomware notificados públicamente que afectaron a hospitales entre 2017 y 2024, ¿con qué frecuencia describieron los informes un recurso a procesos en papel y qué límites de ese recurso mencionaron?». Una buena pregunta nombra la población (qué hospitales, qué incidentes), las variables (recurso descrito, límites mencionados), el marco temporal y el tipo de respuesta (una proporción y unos temas). En el nivel de grado, las preguntas que comparan (opciones, sectores, métodos) se ajustan mejor al resultado del curso que las que pretenden descubrir algo nuevo.

### 18.2 Diseños

Los estudios **descriptivos** dicen lo que hay (una encuesta de inventario; un recuento de avisos por sector). Los estudios **comparativos** contrastan grupos u opciones con los mismos criterios. Los estudios **experimentales** cambian una cosa de forma deliberada y miden el efecto, idealmente frente a un control (el experimento con el umbral del detector del capítulo 27). Los **estudios de caso** examinan uno o unos pocos casos en profundidad, con varias fuentes; explican el cómo y el porqué, pero generalizan con cautela. Elija el diseño que necesita la pregunta, no el que parece más científico.

Para la pregunta sobre las copias de seguridad del CEDC, el diseño adecuado es el comparativo: tres estrategias puntuadas con los mismos criterios. Un experimento compararía simulacros en condiciones controladas, y un estudio de caso examinaría a fondo una restauración pasada. Cada uno responde a una pregunta distinta, así que elija el diseño después de redactar la pregunta.

### 18.3 La bibliografía, de forma sistemática

Buscar fuentes es en sí un método y debe registrarse: bases de datos y sitios consultados, términos de búsqueda, fecha, criterios de inclusión y exclusión, cantidades encontradas y conservadas. Distinga las fuentes **primarias** (un aviso de una agencia, el informe de un regulador, un estudio revisado por pares) de las **secundarias** (un artículo de prensa o un blog que las resume). Prefiera las primarias, cite lo que ha leído (capítulo 4) y registre por qué excluyó lo que excluyó para que otra persona pueda repetir el cribado. Basta con una hoja de cálculo sencilla: fuente, tipo, fecha, pertinencia, hallazgo clave, límites.

### 18.4 Validez

Cuatro amenazas clásicas. **Validez de constructo**: ¿capta la medida el concepto? (Contar los «incidentes notificados» mide la notificación, no los incidentes). **Validez interna**: ¿es la causa alegada realmente la causa? (Los hospitales con más personal de seguridad pueden notificar más incidentes porque detectan más). **Validez externa**: ¿se generaliza el resultado? (Los hallazgos de grandes hospitales urbanos pueden no aplicarse a clínicas rurales). **Fiabilidad**: ¿obtendría otro investigador el mismo resultado? (Dos codificadores que clasifican informes de incidentes deberían coincidir; mida su concordancia). La crítica de Sommer y Paxson a la detección de intrusiones con aprendizaje automático es un ejemplo clásico de problemas de validez externa en la investigación en seguridad ([Sommer and Paxson, 2010](https://doi.org/10.1109/SP.2010.25)).

### 18.5 Ejemplo resuelto: una pregunta comparativa (plan sintético)

**Este plan es sintético.** Un estudiante del programa de prácticas de la CRP pregunta: «¿Cuál de tres estrategias de copia de seguridad respalda mejor la restauración en cuatro horas del servicio de despacho del CEDC?». Diseño: comparativo, con los mismos criterios (tiempo de restauración medido en un simulacro aislado, resiliencia frente al compromiso del servidor de copias, carga operativa, coste). Datos: tres restauraciones cronometradas en un entorno de pruebas aislado proporcionado por el CEDC con autorización escrita, documentación del fabricante y entrevistas con dos administradores. Notas de validez: tres simulacros son una muestra pequeña (informar intervalos, capítulo 37); el entorno de pruebas puede diferir de producción (validez externa: documentar las diferencias); el estudiante diseñó los simulacros (fiabilidad: pedir a un administrador que repita uno). Resultado: una recomendación con las suposiciones declaradas, no una afirmación universal sobre productos de copia de seguridad.

### 18.6 Actividad práctica

Redacte tres preguntas de investigación sobre un tema de su elección en seguridad de sectores críticos: una descriptiva, una comparativa y una de estudio de caso. Para cada una, nombre la población, las variables, el marco temporal y el tipo de evidencia que necesitaría. Por ejemplo, sobre dispositivos médicos sin soporte: descriptiva, «¿cuántos dispositivos clínicos del CVH habían superado el fin del soporte en 2026?»; comparativa, «¿cuál de tres enfoques reduce más la exposición dentro de un presupuesto?»; estudio de caso, «¿cómo gestionó un hospital sus estaciones de trabajo de imagen durante un retraso en la sustitución?». Anote para cada una si la evidencia puede obtenerse con autorización.

### 18.7 Errores comunes y límites

- Preguntas demasiado amplias para responderlas o demasiado estrechas para que importen.
- Búsquedas bibliográficas no registradas que no pueden repetirse.
- Generalizar en exceso a partir de un solo caso.
- Confundir la correlación en los datos de incidentes con la causa.
- Recoger datos sobre personas o sistemas reales sin aprobación ética ni autorización (capítulo 10).

El plan sobre las copias del CEDC evita estos errores al nombrar la población (el servicio de despacho del CEDC), limitar la afirmación a tres estrategias, registrar las fuentes y tratar tres simulacros como una muestra pequeña. Un estudio sobre «el ransomware en los hospitales» no superaría la primera prueba. Un estudiante que entrevistara a administradores del CEDC sin consentimiento no superaría la quinta, fuera cual fuera la calidad del análisis.

### Ejercicios — capítulo 18

**EX035 — Afinar la pregunta.** *Objetivo:* hacer investigable un tema. *Entradas:* el tema «el phishing en el sector energético». *Pasos:* redacte una pregunta de investigación con población, variables, marco temporal y tipo de respuesta; indique qué diseño encaja. *Evidencia esperada:* pregunta y diseño. *Rúbrica:* 3 = específica, respondible con evidencia obtenible, diseño justificado; 2 = específica, pero con evidencia no obtenible; 1 = sigue siendo un tema; 0 = nada.

**EX036 — Nombrar la amenaza.** *Objetivo:* identificar amenazas a la validez. *Entradas:* «Los hospitales que compraron el producto X tuvieron un 40 % menos de incidentes de ransomware notificados, así que X previene el ransomware». *Pasos:* nombre y explique tres amenazas a la validez. *Evidencia esperada:* tres amenazas. *Rúbrica:* 3 = de constructo (notificados frente a reales), interna (factores de confusión como el presupuesto o la madurez, selección), externa (qué hospitales) o fiabilidad; 2 = dos; 1 = una; 0 = nada.

### Síntesis del capítulo

La investigación empieza con una pregunta lo bastante específica como para ser respondida y discutida. Elija el diseño que necesita la pregunta, busque y criba la bibliografía de un modo que otra persona pueda repetir, y nombre las amenazas a la validez antes de que lo haga un revisor.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Siga estudiando — capítulo 18 de 40

[← Capítulo 17](#ch-17) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Infraestructura crítica y seguridad sectorial: alcance y teoría

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) explicar qué hace que una infraestructura sea «crítica» y comparar cómo la definen y organizan los Estados Unidos, la Unión Europea y el Reino Unido; (2) usar las ideas de funciones críticas, interdependencia y resiliencia para analizar un servicio; (3) comparar tres lentes teóricas (riesgo, resiliencia y seguridad funcional/sistemas) y decir qué ve y qué pasa por alto cada una; y (4) situar a una organización en su contexto regulatorio y sectorial. Abre el núcleo disciplinar del libro y se apoya en todos los capítulos 1–18.

### 19.1 Qué significa «crítica»

Una infraestructura es **crítica** cuando su interrupción dañaría gravemente la salud, la seguridad, la seguridad económica o el funcionamiento de la sociedad. Los gobiernos lo concretan de formas distintas. Los Estados Unidos designan dieciséis sectores de infraestructura crítica, desde la energía y el agua hasta la sanidad y los servicios financieros ([CISA, Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors)), y complementan los sectores con un conjunto de **Funciones Críticas Nacionales**: funciones como «suministrar agua» o «prestar atención médica» cuya interrupción sería debilitante ([CISA, NCF set](https://www.cisa.gov/national-critical-functions-set)). La Unión Europea regula la ciberseguridad de las entidades «esenciales» e «importantes» de muchos sectores mediante la Directiva NIS2 ([Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/)), la resiliencia física y operativa más amplia de las «entidades críticas» mediante la Directiva CER ([Directive (EU) 2022/2557](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)) y la resiliencia operativa digital de las entidades financieras mediante DORA ([Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)). El National Cyber Security Centre del Reino Unido publica el Cyber Assessment Framework, que se usa para evaluar a los operadores de servicios esenciales ([NCSC CAF](https://www.ncsc.gov.uk/collection/caf)).

La **visión por funciones** suele ser más útil que la visión por sectores. El Calder Valley Hospital pertenece a la «sanidad», pero la función que necesitan las personas es «prestar atención de urgencias», que depende de la electricidad, el agua, las comunicaciones, el despacho y las cadenas de suministro gestionadas por otros sectores.

### 19.2 Tres lentes

El **riesgo** (capítulo 23) pregunta: ¿qué podría ocurrir, con qué probabilidad, con qué gravedad y qué controles lo reducen más por el dinero invertido? Su fortaleza es la priorización; su debilidad, que las estimaciones de probabilidad captan mal los eventos raros, nuevos o en cascada. La **resiliencia** pregunta: cuando se produce una interrupción, sea cual sea su causa, ¿cómo absorbe el servicio el golpe, se adapta y se recupera? Haimes define la resiliencia como la capacidad de soportar una interrupción importante con una degradación aceptable y de recuperarse en un tiempo y con un coste aceptables ([Haimes, 2009](https://doi.org/10.1111/j.1539-6924.2009.01216.x)); Bruneau y sus colegas la midieron como la pérdida de calidad del servicio a lo largo del tiempo ([Bruneau et al., 2003](https://doi.org/10.1193/1.1623497)). La guía de ingeniería de ciberresiliencia del NIST aplica estas ideas a los sistemas ([SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1)). Las visiones de **seguridad funcional y sistemas** tratan los accidentes como el resultado de un control inadecuado sobre componentes que interactúan, más que de fallas aisladas ([Leveson, 2004](https://doi.org/10.1016/S0925-7535(03)00047-X)), y nos recuerdan que el error humano suele ser un síntoma del diseño del sistema ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)). Un analista competente usa las tres: el riesgo para priorizar, la resiliencia para prepararse para lo que el análisis de riesgos pasó por alto y el pensamiento sistémico para entender cómo fallan juntas las organizaciones y la tecnología.

### 19.3 Qué tiene de distintivo el campo

Cinco rasgos se repiten en todos los sectores: las **consecuencias físicas** (daño a las personas y al medio ambiente, no solo a los datos); la **tecnología de larga vida** (capítulo 2); la **interdependencia** (capítulo 22); la **regulación y la rendición de cuentas pública**; y la **propiedad mixta**: la mayor parte de la infraestructura la operan empresas privadas, pero la sociedad depende de ella, así que los incentivos para invertir en protección frente a eventos raros son débiles. Estos rasgos explican por qué fracasa «aplicar el manual de la TI corporativa» y por qué importa el conocimiento específico de cada sector.

En Calder estos rasgos son concretos: el daño del CVH es físico (pacientes), las RTU de CPN duran décadas, la subestación alimenta a otros cuatro servicios (Lab 3), cada operador responde ante su propio regulador y la mayoría son empresas privadas cuya falla perjudica a residentes del condado que no son sus clientes.

### 19.4 Ejemplo resuelto: perfil del CEDC (sintético)

**Este caso es sintético.** Un perfil sectorial del County Emergency Dispatch Centre: *función*: recibir llamadas de emergencia y despachar ambulancias, bomberos y policía; *daño por pérdida*: retraso de la respuesta en cuestión de minutos; *dependencias*: telecomunicaciones (llamadas y datos del CAD), electricidad (SAI y generador), servicios en la nube del fabricante del CAD, personal; *contexto regulatorio*: obligaciones de servicio público y, según la jurisdicción, obligaciones de ciberseguridad para entidades esenciales (a verificar con asesoría jurídica); *lentes*: riesgo, el ransomware en el CAD es el escenario principal; resiliencia, el respaldo con papel y radio debe sostener el despacho durante horas; sistemas, un paso al papel a las 2 de la madrugada es tanto un problema de factores humanos como técnico. El perfil aún no dice qué hacer; dice qué preguntas importan.

### 19.5 Actividad práctica

Elija un sector real de su país. A partir de fuentes oficiales, averigüe quién lo designa como crítico, qué ley o marco fija sus obligaciones de ciberseguridad, qué organismo lo supervisa y qué orientación pública se aplica. Registre cada fuente con su fecha. No dé por hecho que el modelo de la UE, de los EE. UU. o del Reino Unido se aplica en otros lugares. Registre la jurisdicción y la fecha de cada fuente, porque las definiciones cambian: la UE sustituyó su anterior directiva de seguridad de las redes por la NIS2, y las fechas de transposición nacional difieren. Cuando un marco solo se aplica por encima de un umbral de tamaño, anote el umbral y si el operador elegido lo supera.

### 19.6 Errores comunes y límites

- Equiparar «infraestructura crítica» con «TO».
- Leer una lista de sectores como una lista de sectores independientes.
- Usar una sola lente e ignorar lo que revelan las demás.
- Afirmar obligaciones legales sin comprobar el texto vigente y la jurisdicción.

El CEDC muestra el primer error: un centro de despacho casi no tiene TO y aun así es crítico. El Lab 3 muestra el segundo: las entradas de la subestación, las telecomunicaciones y el agua dependen unas de otras. Usar solo la lente del riesgo con el CEDC pasaría por alto el problema del paso al papel a las 2 de la madrugada. Y el perfil del CEDC deja a propósito sus obligaciones legales «a verificar con asesoría jurídica».

### Ejercicios — capítulo 19

**EX037 — Funciones, no sectores.** *Objetivo:* aplicar la visión por funciones. *Entradas:* Calder Mutual. *Pasos:* nombre dos funciones críticas que respalda, sus dependencias de otros sectores y la cronología del daño si cada una se detiene. *Evidencia esperada:* perfil breve. *Rúbrica:* 3 = funciones como «prestar servicios de pago» y «dar acceso al efectivo», dependencias de la electricidad, las telecomunicaciones y otras infraestructuras financieras, cronología del daño (horas para los pagos, días para salarios y prestaciones); 2 = solo a nivel de sector; 1 = vago; 0 = nada.

**EX038 — Tres lentes.** *Objetivo:* comparar teorías sobre un caso. *Entradas:* la planta de tratamiento de CW. *Pasos:* escriba una pregunta que haría cada lente y una cosa que cada una podría pasar por alto. *Evidencia esperada:* tres pares. *Rúbrica:* 3 = riesgo (escenarios probables; pasa por alto cascadas nuevas), resiliencia (recuperación y modos degradados; puede infravalorar la economía de la prevención), sistemas (estructura de control, factores humanos y organizativos; más difícil de cuantificar); 2 = dos lentes; 1 = una; 0 = nada.

### Síntesis del capítulo

Una infraestructura es crítica porque la sociedad depende de sus funciones. Las jurisdicciones la organizan de forma distinta mediante sectores, funciones y leyes como NIS2, CER y DORA. El riesgo, la resiliencia y el pensamiento sistémico son lentes complementarias, y los rasgos distintivos del campo (consecuencias físicas, longevidad, interdependencia, regulación y propiedad mixta) explican por qué necesita su propia disciplina.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Siga estudiando — capítulo 19 de 40

[← Capítulo 18](#ch-18) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Infraestructura crítica y seguridad sectorial: casos fundacionales

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) resumir seis casos públicos que dieron forma al campo a partir de sus fuentes primarias o autorizadas; (2) separar lo que establecen las fuentes de lo que se repite habitualmente; (3) extraer lecciones trasladables y compararlas entre sectores; y (4) tratar con honestidad los relatos revisados. Se apoya en el capítulo 19 y prepara el capítulo 31 (casos avanzados) y el proyecto final. Todas las descripciones se mantienen al nivel de las fuentes citadas; ningún caso se enseña como técnica.

### 20.1 Leer un caso

Para cada caso, registre: **fecha y sector**; **qué le ocurrió al servicio** (alcance, duración, personas afectadas); **acceso inicial y propagación**, solo tal como los describe la fuente; **respuesta**; **tipo de fuente** (aviso gubernamental, informe de auditoría, análisis revisado por pares, comunicado de la empresa, periodismo); y **qué sigue siendo incierto**. Los primeros informes a menudo se equivocan; los posteriores a menudo los corrigen. Un buen analista cita ambos. Para Oldsmar este registro tiene dos fechas: el aviso de 2021 y la declaración de 2023 que lo revisó. Ambos forman parte del registro, con el relato del aviso etiquetado como superado en lugar de eliminado.

### 20.2 Seis casos

**Distribución eléctrica en Ucrania, diciembre de 2015.** La alerta de CISA describe ataques coordinados contra tres empresas regionales de distribución que causaron cortes que afectaron a unos 225 000 clientes, con operación remota de interruptores, destrucción de algunos sistemas e interrupción de los centros de atención telefónica; el suministro se restableció pasando a la operación manual ([CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01); véase también el [análisis de E-ISAC/SANS](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and)). *Lección:* el respaldo manual y un personal capaz de operar sin automatización fueron decisivos.

**WannaCry y el NHS, mayo de 2017.** La National Audit Office del Reino Unido concluyó que el ransomware afectó al menos a un tercio de los *trusts* del NHS en Inglaterra, provocó la cancelación de citas y el desvío de ambulancias, y que las organizaciones afectadas tenían sistemas Windows sin parchear o sin soporte; el NHS no había ensayado una respuesta nacional ([NAO, 2017](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/)). *Lección:* el malware no dirigido puede causar daño clínico; la higiene básica y la coordinación ensayada importan.

**TRITON/HatMan, 2017.** El informe de análisis de malware de CISA describe un malware diseñado para interactuar con un controlador concreto de un sistema instrumentado de seguridad, la capa destinada a evitar daños físicos ([CISA MAR-17-352-01](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf)). *Lección:* los sistemas de seguridad funcional son objetivos, y su independencia de las redes de control debe ser real.

**Tratamiento de agua de Oldsmar, febrero de 2021.** El aviso de CISA informó de que actores no identificados accedieron al sistema de control de una planta de tratamiento de agua a través de un software de acceso remoto y aumentaron el punto de consigna del hidróxido de sodio, algo que un operador advirtió y revirtió ([CISA AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a)). En 2023, un antiguo administrador municipal dijo que el evento fue probablemente un error de un empleado y no una intrusión ([WUSF, 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)). *Lección:* fuera cual fuera la causa, el acceso remoto sin gestionar y la dependencia de un único operador atento eran debilidades; y los relatos públicos pueden revisarse.

**Colonial Pipeline, mayo de 2021.** El aviso conjunto de CISA y el FBI sobre el ransomware DarkSide informa de que los actores desplegaron ransomware contra la red de TI de una empresa de oleoductos, de que no había indicios de que sus redes de TO se hubieran visto afectadas directamente y de que la empresa desconectó de forma proactiva ciertos sistemas de TO para garantizar su seguridad ([CISA AA21-131A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a)). La retrospectiva de CISA a los dos años nombra a la empresa y recuerda las colas de combustible a lo largo de la costa este que siguieron ([CISA, 2023](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years)). *Lección:* un compromiso de la TI puede detener las operaciones de TO a través de dependencias de negocio y decisiones de precaución, sin tocar el sistema de control.

**Actualización de CrowdStrike, julio de 2024.** Una actualización defectuosa de un software de seguridad bloqueó equipos Windows en todo el mundo; Microsoft estimó que se vieron afectados unos 8,5 millones de dispositivos, con interrupciones en aerolíneas, hospitales y bancos ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)). *Lección:* no hace falta un adversario; una dependencia de software compartida es un punto único de falla para varios sectores.

### 20.3 Comparar los casos

| Caso | Causa | Efecto en el sector | Lección trasladable |
|---|---|---|---|
| Ucrania 2015 | Ataque deliberado | Corte eléctrico | Capacidad de operación manual |
| WannaCry 2017 | Malware no dirigido | Interrupción clínica | Higiene, coordinación ensayada |
| TRITON 2017 | Malware dirigido | Capa de seguridad funcional amenazada | Independencia de los sistemas de seguridad funcional |
| Oldsmar 2021 | Discutida | Casi accidente en la dosificación química | Gobierno del acceso remoto; relatos revisados |
| Colonial 2021 | Ransomware en la TI | Parada de precaución de la TO | Dependencia de negocio entre TI y TO |
| CrowdStrike 2024 | Actualización defectuosa | Interrupción intersectorial | Concentración en dependencias compartidas |

La tabla comprime cada caso en una lección para poder compararlos; no es un resumen de lo que ocurrió. Lea la columna «Causa»: dos de los seis no implican ningún ataque dirigido contra el sistema de control.

### 20.4 Ejemplo resuelto: lecciones para el CVH (aplicación sintética)

**La aplicación es sintética; los casos están citados arriba.** Para el Calder Valley Hospital, las lecciones trasladables son: (1) ensayar la operación sin TI (procesos en papel, como hicieron los operadores ucranianos sin automatización); (2) inventariar y aislar los dispositivos sin soporte (WannaCry); (3) confirmar que un compromiso del BMS no puede detener los controles de seguridad locales de la ventilación de los quirófanos (la lección de TRITON sobre las capas independientes); (4) gobernar el acceso remoto al BMS (Oldsmar); (5) cartografiar qué procesos clínicos dependen de la TI de negocio, como la admisión de pacientes (Colonial); y (6) planificar la falla masiva de un producto de endpoint compartido (CrowdStrike).

### 20.5 Errores comunes y límites

- Repetir detalles llamativos que ninguna fuente primaria respalda.
- Citar el primer relato e ignorar la corrección.
- Tratar cada caso como un ataque.
- Convertir un estudio de caso en una receta de ataque.

Ejemplos habituales: afirmar que Oldsmar fue «un hackeo» sin la revisión de 2023; repetir duraciones de cortes que no figuran en la fuente citada; llamar ataque a lo de CrowdStrike; o describir las técnicas de Stuxnet cuando la lección es la suposición que falló. Cada uno de los seis resúmenes de aquí se mantiene al nivel que su fuente respalda, y el EX039 le pide que compruebe uno.

### Ejercicios — capítulo 20

**EX039 — Comprobación de la fuente primaria.** *Objetivo:* separar la fuente de la repetición. *Entradas:* uno de los seis casos de este capítulo. *Pasos:* lea la fuente citada y enumere tres hechos que afirma, una afirmación repetida habitualmente que no hace (búsquela en un artículo de prensa o un blog) y cómo redactaría el caso para un informe. *Evidencia esperada:* lista y redacción. *Rúbrica:* 3 = hechos exactos con su ubicación en la fuente, una afirmación sin respaldo identificada, redacción cuidadosa; 2 = solo hechos; 1 = hechos de fuentes secundarias; 0 = nada.

**EX040 — Lección intersectorial.** *Objetivo:* trasladar una lección. *Entradas:* Colonial Pipeline. *Pasos:* aplique su lección a Calder Transit: ¿qué sistemas de TI de negocio podrían forzar una parada de precaución de las operaciones ferroviarias y qué podría evitarlo? *Evidencia esperada:* dos dependencias y dos medidas. *Rúbrica:* 3 = p. ej., venta de billetes/ingresos, programación de tripulaciones, información a los pasajeros; medidas como reglas de operación degradada acordadas de antemano y la separación de las dependencias operativas respecto de las de negocio; 2 = una de cada; 1 = genérico; 0 = nada.

### Síntesis del capítulo

Los casos fundacionales del campo enseñan mediante la comparación: respaldo manual, higiene, independencia de los sistemas de seguridad funcional, gobierno del acceso remoto, dependencia de negocio entre TI y TO, y concentración en dependencias compartidas. Lea las fuentes primarias, tenga presentes las revisiones y traslade lecciones, no técnicas.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Siga estudiando — capítulo 20 de 40

[← Capítulo 19](#ch-19) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Capítulo 21 — Infraestructura crítica y seguridad sectorial: modelos de sistemas

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) describir un lazo de control y los componentes de un sistema SCADA o de control industrial; (2) situar los activos en un modelo de referencia por capas, desde los dispositivos de campo hasta la empresa; (3) modelar un servicio como una cadena de funciones con modos degradados; y (4) indicar a qué tipos de ataque o falla está expuesta cada parte del modelo. Se apoya en los capítulos 7, 16 y 19 y prepara el capítulo 22 (datos y dependencias) y el capítulo 28 (análisis de fallas).

### 21.1 El lazo de control

Todo proceso físico controlado por computadoras sigue un lazo: un **sensor** mide (nivel de un depósito, corriente de una línea, posición de un tren); un **controlador** compara la medición con un **punto de consigna** y calcula una acción; un **actuador** actúa (velocidad de una bomba, disparo de un interruptor, aspecto de una señal); el proceso responde; el sensor vuelve a medir. Los **controladores lógicos programables** (PLC) y las **unidades terminales remotas** (RTU) ejecutan el lazo localmente. Un sistema **SCADA** (supervisión, control y adquisición de datos) supervisa muchos lazos en un área extensa: recoge mediciones, las muestra a los operadores en **interfaces hombre-máquina** (HMI), almacena el histórico en un **historiador** y envía puntos de consigna y órdenes. Los **sistemas instrumentados de seguridad** (SIS) vigilan las condiciones peligrosas y actúan de forma independiente para llevar el proceso a un estado seguro ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

El lazo ofrece un vocabulario preciso para lo que puede fallar: **mediciones** falsas (el controlador actúa sobre una mentira), **órdenes** falsas (el actuador hace algo no previsto), pérdida de **vista** (los operadores no pueden ver), pérdida de **control** (los operadores no pueden actuar) y compromiso de la **protección** (el SIS no puede actuar). MITRE ATT&CK for ICS organiza los impactos en términos similares, como pérdida de vista, pérdida de control y manipulación del control ([ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)).

### 21.2 Un modelo de referencia por capas

Un modelo por capas, ampliamente conocido como modelo Purdue, sitúa los activos según su función: nivel 0, el proceso físico con sensores y actuadores; nivel 1, el control básico (PLC, RTU, SIS); nivel 2, el control de supervisión (HMI, SCADA local); nivel 3, las operaciones del emplazamiento (historiadores, estaciones de ingeniería); una DMZ; y los niveles 4–5, la TI corporativa. El modelo es una ayuda para la enseñanza y la segmentación, no una ley de la naturaleza: los sensores conectados a la nube, los servicios remotos de los proveedores y los dispositivos de campo inalámbricos cruzan niveles. Úselo para preguntar: «¿qué rutas cruzan niveles y están controladas?».

### 21.3 Cadenas de servicio y modos degradados

A los operadores les importan los servicios, no los niveles. Modele un servicio como una cadena de funciones con **modos degradados**: el servicio «suministrar agua segura» de Calder Water = captar agua bruta → tratar → vigilar la calidad → almacenar → bombear → distribuir. Cada función tiene estados normal, degradado y fallido. «Vigilar la calidad» degradado podría significar muestreo manual cada hora en lugar de analizadores continuos; «bombear» degradado podría significar control local por parte del personal en la estación sin SCADA. Un modelo de servicio que incluye los modos degradados muestra cuánto tiempo puede continuar el servicio cuando se pierde la automatización, la pregunta que respondieron los operadores ucranianos en 2015 (capítulo 20).

### 21.4 Ejemplo resuelto: restablecimiento de un alimentador de CPN (sintético)

**Este caso es sintético.** El servicio «restablecer el suministro tras una falla en un alimentador» de Calder Power Networks: un relé de protección dispara la sección en falla (nivel 1, independiente del SCADA); la RTU informa del disparo (nivel 1→2); el operador lo ve en la HMI (nivel 2) y realiza un reenganche remoto o reconfigura (nivel 2→1); se informa a los clientes mediante el sistema de gestión de cortes (nivel 4). Análisis de fallas por elemento: si falla el relé, la falla persiste, un problema de seguridad; si falla el enlace de la RTU, los operadores pierden la vista de ese alimentador, modo degradado: enviar una cuadrilla; si la HMI está comprometida, un estado falso podría llevar a los operadores a energizar una línea en la que trabajan cuadrillas, un problema de seguridad que los procedimientos (bloqueos, permisos, confirmación verbal) deben detectar; si falla el sistema de gestión de cortes, no se informa a los clientes, un problema de calidad del servicio. El modelo muestra que las consecuencias más graves se sitúan donde la manipulación cibernética se encuentra con los procedimientos de seguridad de las personas.

### 21.5 Actividad práctica

Dibuje el lazo de control y el modelo por capas de un servicio de Calder distinto del agua o la electricidad (señalización ferroviaria o ventilación de quirófanos). Etiquete cada componente con su nivel, cuál de vista/control/protección respalda y un modo degradado.

Para la ventilación de quirófanos, el sensor podría ser un sensor de presión en conducto o de renovaciones de aire en el nivel 0, el controlador del BMS en el nivel 1, la estación de trabajo de mantenimiento de instalaciones en el nivel 2 y el servidor del BMS en el nivel 3. Un modo degradado es el control manual local de las unidades de tratamiento de aire. Marque qué componente respalda la vista, el control o la protección; un enclavamiento cableado de caudal mínimo de aire, si existe, es protección.

### 21.6 Errores comunes y límites

- Tratar el modelo por capas como una descripción del tráfico real.
- Ignorar los sistemas de seguridad o suponer que siempre son independientes.
- Modelar los activos sin el servicio que respaldan.
- Suponer que la pérdida del SCADA significa la pérdida del servicio.

El modelo del alimentador de CPN muestra los dos primeros: el relé se sitúa en el nivel 1 y actúa sin SCADA, pero si estuviera conectado en red con la HMI su independencia necesitaría evidencia. El tercer error enumeraría las RTU sin decir que sirven al restablecimiento de alimentadores. El cuarto ignora el modo degradado de enviar una cuadrilla cuando falla el enlace de una RTU.

### Ejercicios — capítulo 21

**EX041 — Nombre la pérdida.** *Objetivo:* usar el vocabulario del lazo. *Entradas:* (a) una caída del historiador; (b) una HMI que muestra valores congelados; (c) un punto de consigna falsificado aceptado por un PLC; (d) un disparo del SIS deshabilitado. *Pasos:* clasifique cada uno como pérdida de vista, pérdida de control, manipulación o pérdida de protección, e indique el riesgo inmediato. *Evidencia esperada:* cuatro clasificaciones. *Rúbrica:* 3 = (a) pérdida de la vista histórica, riesgo inmediato bajo; (b) pérdida de vista, peligrosa porque los operadores pueden actuar con datos obsoletos; (c) manipulación del control; (d) pérdida de protección, máxima gravedad; 2 = una errónea; 1 = dos erróneas; 0 = nada.

**EX042 — Modos degradados.** *Objetivo:* modelar la continuidad sin automatización. *Entradas:* el servicio «operar un servicio ferroviario seguro» de Calder Transit. *Pasos:* escriba la cadena de funciones y un modo degradado para tres funciones, con la restricción que impone cada uno (p. ej., menor frecuencia). *Evidencia esperada:* cadena y modos. *Rúbrica:* 3 = cadena razonable (señalización, control de trenes, comunicación con la tripulación, información a los pasajeros, venta de billetes) con modos degradados y restricciones realistas; 2 = cadena sin restricciones; 1 = vago; 0 = nada.

### Síntesis del capítulo

Los sistemas de control son lazos de medición, decisión y actuación, supervisados por el SCADA y protegidos por sistemas de seguridad independientes. Los modelos por capas ayudan a la segmentación; las cadenas de servicio con modos degradados muestran cuánto tiempo puede sobrevivir un servicio sin automatización. Las peores consecuencias surgen donde la manipulación se encuentra con la seguridad y el procedimiento humano.

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Siga estudiando — capítulo 21 de 40

[← Capítulo 20](#ch-20) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 22 →](#ch-22)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-22"></a>

## Capítulo 22 — Infraestructura crítica y seguridad sectorial: datos y dependencias

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) construir y mantener un inventario de activos y dependencias a partir de varias fuentes imperfectas; (2) añadir el tiempo a un modelo de dependencias mediante la autonomía de los respaldos; (3) calcular qué servicios se pierden en cortes de distinta duración e identificar los eslabones débiles; y (4) indicar los límites de calidad de los datos de estos modelos. Se apoya en los capítulos 6, 9 y 21 y prepara el capítulo 23 (métodos de riesgo) y el capítulo 28 (análisis de fallas).

### 22.1 El inventario es evidencia, no una lista

Ninguna organización sabe exactamente lo que tiene. Los datos de activos proceden de los registros de compras, las observaciones de la red, las bases de datos de configuración, la documentación de los proveedores y los recorridos por el emplazamiento; a cada fuente se le escapa algo. Trate el inventario como evidencia con fuentes y fechas (capítulo 15): para cada activo, registre quién lo confirmó y cuándo. La observación **pasiva** de la red encuentra los dispositivos que se comunican; se le escapan los inactivos y los de comunicación serie. El escaneo **activo** encuentra más, pero puede perturbar dispositivos de TO frágiles y solo debe realizarse con autorización y con el acuerdo de operaciones (capítulo 10). Las dependencias son aún más difíciles: viven en la cabeza de las personas, en los contratos y en hábitos no escritos.

### 22.2 Tipos de dependencia

Rinaldi y sus colegas distinguen interdependencias **físicas** (electricidad para las bombas), **cibernéticas** (telemetría sobre telecomunicaciones), **geográficas** (cables en la misma zanja) y **lógicas** (vínculos financieros o regulatorios) ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131)). Añada las **personas** (un único ingeniero que conoce el sistema heredado) y los **proveedores** (un único proveedor de CAD, una región de la nube). El grafo del capítulo 6 mostraba *qué puede verse afectado*; el tiempo lo convierte en *qué se perderá y cuándo*. Cada servicio tiene **autonomía**: cuánto tiempo continúa con su propio respaldo (baterías, generadores y combustible, agua almacenada, procesos en papel).

### 22.3 Ejemplo resuelto y Lab 9 (sintético)

**Este caso es sintético.** La CRP recopiló la autonomía de los respaldos de los servicios clave durante un corte de la red eléctrica regional. Los pagos con tarjeta dependen de la central telefónica A, que solo tiene baterías; la central B también tiene un generador.

```python
# Lab 9 - which services survive a grid outage of a given length? (synthetic backup autonomy, offline)
AUTONOMY_H = {  # hours each service keeps running on its own backup
    "hospital (generator, fuel on site)": 72, "telecom exchange A (batteries)": 4,
    "telecom exchange B (batteries + generator)": 48, "water pumps (no generator)": 0,
    "water treated storage": 10, "dispatch centre (UPS + generator)": 24,
    "card payments (relies on telecom)": None, "rail signalling (UPS)": 2,
}
for outage in (1, 6, 30):
    down = []
    for s, h in AUTONOMY_H.items():
        if h is None:   # dependent service: fails when 4-h exchange A fails
            h = AUTONOMY_H["telecom exchange A (batteries)"]
        if h < outage: down.append(s.split(" (")[0])
    print(f"outage {outage:>2} h -> {len(down)} services lost: {', '.join(down) or 'none'}")
```

Salida esperada:

```text
outage  1 h -> 1 services lost: water pumps
outage  6 h -> 4 services lost: telecom exchange A, water pumps, card payments, rail signalling
outage 30 h -> 6 services lost: telecom exchange A, water pumps, water treated storage, dispatch centre, card payments, rail signalling
```

Interpretación: las autonomías más cortas marcan el inicio de la historia: las bombas se detienen de inmediato (los clientes siguen recibiendo agua almacenada durante unas 10 horas), la señalización ferroviaria se detiene a las 2 horas y los pagos con tarjeta fallan a las 4 horas porque la central A no tiene generador. A las 30 horas se pierden el suministro de agua y el despacho. Las 72 horas del hospital parecen tranquilizadoras, pero su agua llega de un almacenamiento que dura 10 horas: un edificio puede tener electricidad y aun así ser inutilizable. El modelo es tosco, ya que ignora las dependencias de los propios respaldos (¿quién reabastece el generador del centro de despacho después de 24 horas, y por qué carreteras?), pero ya identifica tres preguntas baratas: ¿puede la central A tener un generador?; ¿pueden las bombas de agua tener un punto de conexión para un generador móvil?; y ¿qué acuerdos de suministro de combustible existen entre los operadores?

### 22.4 Calidad de los datos

Cada número anterior es una afirmación de un operador. La autonomía de un generador depende del combustible que realmente hay en el depósito, de la fiabilidad del arranque (capítulo 12, EX024) y de la carga. La autonomía de las baterías se degrada con la edad. Registre la evidencia que respalda cada autonomía (una prueba, una cifra de diseño, una estimación) y ejecute el modelo con valores pesimistas. Un modelo de dependencias solo es tan bueno como su número menos comprobado. En el Lab 9, reducir a la mitad todas las autonomías (EX043) hace que el almacenamiento de agua tratada pase a la lista de pérdidas a las 6 horas. Para el generador del CEDC, la evidencia sería la fecha de la última prueba de carga y el nivel de combustible el día de la inspección.

### 22.5 Errores comunes y límites

- Tratar una fuente de inventario como completa.
- Registrar dependencias sin tiempo.
- Tomar cifras de autonomía de los documentos de diseño sin pruebas.
- Olvidar las dependencias de segundo orden de los respaldos (combustible, personal, carreteras).
- Escanear activamente la TO sin autorización ni acuerdo operativo.

El Lab 9 ilustra los tres primeros: una autonomía de diseño de 72 horas para el hospital supone un depósito lleno, y las 4 horas de la central A suponen baterías en buen estado. El cuarto es la pregunta de reabastecimiento que hay detrás de las 24 horas del centro de despacho. El quinto explica por qué el inventario de la CRP se basó en la observación pasiva y en las declaraciones de los operadores en lugar de en el escaneo.

### Ejercicios — capítulo 22

**EX043 — Corrija el eslabón débil.** *Objetivo:* probar una intervención. *Entradas:* el Lab 9. *Pasos:* dé a los pagos con tarjeta la autonomía de la central B (48 h) y vuelva a ejecutar. Después reduzca a la mitad todas las autonomías (caso pesimista) y vuelva a ejecutar para 6 h. Informe de ambos resultados y formule una recomendación. *Evidencia esperada:* dos salidas y una recomendación. *Rúbrica:* 3 = los pagos con tarjeta sobreviven hasta las 48 h en la primera ejecución; la ejecución pesimista de 6 h pierde la central telefónica A, las bombas de agua, el almacenamiento de agua tratada, los pagos con tarjeta y la señalización ferroviaria (5 servicios); la recomendación aborda la evidencia de las cifras de autonomía; 2 = ejecuciones sin recomendación; 1 = una ejecución; 0 = nada.

**EX044 — Dependencias de segundo orden.** *Objetivo:* mirar detrás de los respaldos. *Entradas:* el generador de 24 horas del centro de despacho. *Pasos:* enumere cuatro dependencias de ese propio respaldo y una forma de evidenciar cada una. *Evidencia esperada:* lista. *Rúbrica:* 3 = contrato de suministro de combustible y ruta de entrega, personal para operarlo y reabastecerlo, fiabilidad del arranque del generador (registros de pruebas), refrigeración/ventilación o aparamenta; cada una con evidencia; 2 = tres; 1 = una o dos; 0 = nada.

### Síntesis del capítulo

Los inventarios y los mapas de dependencias son evidencia con fuentes, fechas y lagunas. Añadir el tiempo (la autonomía de los respaldos) convierte la exposición en una cronología de pérdidas, pone de manifiesto eslabones débiles como una central solo con baterías y revela que un edificio con electricidad puede seguir siendo inutilizable. Ponga a prueba las afirmaciones de autonomía y mire detrás de cada respaldo hacia sus propias dependencias.

<!-- cyberabc:chapter-navigation:start ch-22 -->
### Siga estudiando — capítulo 22 de 40

[← Capítulo 21](#ch-21) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 23 →](#ch-23)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-23"></a>

## Capítulo 23 — Infraestructura crítica y seguridad sectorial: métodos I

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) realizar una evaluación de riesgos estructurada siguiendo las etapas de NIST SP 800-30; (2) explicar las debilidades de las matrices de riesgo; (3) aplicar un enfoque centrado primero en las consecuencias que parte de los peores efectos sobre el servicio; y (4) comparar ambos enfoques en un caso e indicar cuándo es adecuado cada uno. Se apoya en los capítulos 1, 12, 15 y 19–22 y prepara el capítulo 24 (controles) y el capítulo 26 (métodos II).

### 23.1 Una evaluación de riesgos estructurada

NIST SP 800-30 describe la evaluación de riesgos por etapas: **preparar** (propósito, alcance, supuestos, fuentes); **realizar** (identificar las fuentes y los eventos de amenaza, las vulnerabilidades y las condiciones predisponentes, determinar la probabilidad y el impacto, determinar el riesgo); **comunicar** los resultados; y **mantener** la evaluación a medida que cambian las cosas ([SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)). La fortaleza del método es la disciplina: le obliga a dejar por escrito el alcance y los supuestos, y a indicar de dónde procede cada juicio. Sus resultados suelen ser calificaciones cualitativas (de muy bajo a muy alto) en escalas que define la organización.

### 23.2 El problema de las matrices

Muchas organizaciones combinan las calificaciones de probabilidad e impacto en una **matriz de riesgo** de 5×5. Las matrices son fáciles de comunicar, pero tienen problemas conocidos. Las etiquetas ordinales («3 = posible») se multiplican como si fueran números. Riesgos muy distintos reciben la misma celda. Los eventos raros y catastróficos acaban en el mismo color que los frecuentes y menores. Las calificaciones dependen mucho de quién esté en la sala. El hábito del capítulo 1 ayuda: siempre que sea posible, ponga cantidades aproximadas detrás de las etiquetas (un intervalo de probabilidad anual, una duración de la interrupción, un daño) y muestre la peor consecuencia creíble por separado de la calificación.

### 23.3 Primero las consecuencias

En los servicios críticos, la probabilidad suele ser el dato menos conocible: los adversarios se adaptan y los eventos que más importan son raros. Un enfoque **centrado primero en las consecuencias** parte del otro extremo: identifique los resultados que no deben ocurrir (pérdida del suministro de agua al hospital durante más de 8 horas; dosificación de cloro sin control), rastree qué funciones y sistemas podrían causarlos y pregúntese qué necesitaría lograr un adversario o una falla para provocar cada uno. La **Consequence-driven Cyber-informed Engineering** (CCE) del Idaho National Laboratory formaliza esto: identificar los eventos de alta consecuencia, cartografiar los sistemas implicados, iluminar las rutas que seguiría un adversario y mitigar, preferiblemente con cambios de ingeniería que eliminen la posibilidad en lugar de detectarla ([INL CCE](https://inl.gov/national-security/cce/)). ISA/IEC 62443-3-2 también basa su evaluación de riesgos para el diseño de sistemas en zonas, conductos y consecuencias ([página del catálogo de IEC 62443-3-2](https://webstore.iec.ch/en/publication/30727)).

### 23.4 Ejemplo resuelto: dosificación de cloro en CW (sintético)

**Este caso es sintético.** *Visión de la matriz de riesgo:* la amenaza «cambio no autorizado del punto de consigna de dosificación de cloro» se califica con probabilidad 2 (improbable) e impacto 5 (grave) = 10, ámbar. El registro dice «vigilar». *Visión centrada primero en las consecuencias:* el resultado inaceptable es «agua que sale de la planta con cloro fuera de los límites seguros durante el tiempo suficiente para dañar a los clientes». Rutas: un cambio del punto de consigna desde la HMI (error del operador o compromiso); una orden falsificada al PLC de dosificación a través de la red de control; un sensor que informa de un cloro residual falso de modo que el controlador sobredosifica; un portátil de un proveedor conectado al PLC. Mitigaciones de ingeniería que no dependen de detectar al atacante: un caudal máximo cableado de la bomba dosificadora; un analizador independiente de cloro residual en la salida que dispara la válvula de salida mediante un circuito separado; un interruptor de llave físico para el modo de programación del PLC. La matriz decía «vigilar»; el análisis de consecuencias produjo tres cambios concretos, uno de los cuales (el límite físico) elimina el resultado más peligroso independientemente de cómo haya entrado el atacante.

### 23.5 Actividad práctica

Tome la señalización del tren ligero de Calder Transit. Escriba una consecuencia inaceptable, tres rutas hacia ella (al menos una no maliciosa) y una mitigación de ingeniería que elimine o acote la consecuencia. Después califique el mismo escenario en una matriz de 5×5 y compare lo que le dijo cada enfoque.

Para la señalización, una consecuencia inaceptable podría ser «dos trenes autorizados a entrar en el mismo cantón». Las rutas incluyen una configuración corrupta del enclavamiento tras un mantenimiento (no maliciosa), una orden falsificada desde una estación de control comprometida y un circuito de vía averiado que se interpreta erróneamente como libre. Una mitigación de ingeniería es la propia lógica de seguridad del enclavamiento, independiente de la estación de control. En una matriz de 5×5, el mismo escenario puede puntuar 5 en impacto y 1 en probabilidad, lo que da una celda que lo infravalora.

### 23.6 Errores comunes y límites

- Multiplicar etiquetas ordinales como si fueran mediciones.
- Calificar la probabilidad de acciones adversarias novedosas con falsa confianza.
- Tratar «vigilar» como una mitigación.
- Un análisis centrado primero en las consecuencias que solo enumera consecuencias y nunca cartografía rutas ni mitigaciones.
- Ignorar las rutas no maliciosas hacia la misma consecuencia.

El ejemplo del cloro muestra directamente el tercer error: el resultado «vigilar» de la matriz dejaba posible el resultado peligroso. El primer error produjo su puntuación de 10. El análisis de consecuencias evitó el cuarto al nombrar rutas y mitigaciones, y el quinto al incluir el error del operador y las lecturas falsas de los sensores como rutas junto al compromiso.

### Ejercicios — capítulo 23

**EX045 — Misma celda, riesgo distinto.** *Objetivo:* poner de manifiesto los límites de la matriz. *Entradas:* riesgo A: probabilidad 5, impacto 2 (cortes molestos diarios de la wifi del personal); riesgo B: probabilidad 2, impacto 5 (pérdida de la ventilación de los quirófanos del CVH). *Pasos:* calcule ambas puntuaciones de la matriz, explique por qué la igualdad de puntuación induce a error y proponga cómo presentarlos en su lugar. *Evidencia esperada:* puntuaciones y explicación. *Rúbrica:* 3 = ambas 10; explica el mal uso de las escalas ordinales y la distinta naturaleza del daño; propone una columna separada de peor consecuencia creíble o intervalos cuantitativos; 2 = parcial; 1 = solo las puntuaciones; 0 = nada.

**EX046 — Primero las consecuencias.** *Objetivo:* aplicar el método. *Entradas:* el conmutador de pagos de Calder Mutual. *Pasos:* defina una consecuencia inaceptable, cartografíe tres rutas y dé una mitigación de ingeniería y una procedimental. *Evidencia esperada:* el análisis. *Rúbrica:* 3 = consecuencia específica (p. ej., transferencias fraudulentas de alto valor liberadas, o pagos no disponibles > 4 h el día de pago de las nóminas), rutas plausibles que incluyen a personas internas o errores, mitigación de ingeniería (límites estrictos por transacción, confirmación fuera de banda) y una procedimental; 2 = genérico; 1 = solo la consecuencia; 0 = nada.

### Síntesis del capítulo

La evaluación de riesgos estructurada aporta disciplina al alcance, los supuestos y el juicio; las matrices de riesgo simplifican la comunicación pero distorsionan las comparaciones. Los métodos centrados primero en las consecuencias, como la CCE, parten de lo que no debe ocurrir y favorecen mitigaciones de ingeniería que acotan el daño independientemente del atacante. Use ambos e indique cuál impulsa cada recomendación.

<!-- cyberabc:chapter-navigation:start ch-23 -->
### Siga estudiando — capítulo 23 de 40

[← Capítulo 22](#ch-22) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 24 →](#ch-24)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-24"></a>

## Capítulo 24 — Infraestructura crítica y seguridad sectorial: controles

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) usar un marco (NIST CSF 2.0, el CAF del Reino Unido u objetivos sectoriales) para organizar los controles; (2) clasificar los controles por tipo (preventivo, detectivo, correctivo) y por naturaleza (técnica, procedimental, física, de ingeniería); (3) relacionar los controles con los escenarios y las técnicas que abordan y encontrar lagunas; y (4) elegir controles adecuados a las restricciones de la TO. Se apoya en los capítulos 16 y 23 y prepara el Laboratorio I (capítulo 25) y el capítulo 27 (verificación).

### 24.1 Los marcos como organizadores

Un **marco** organiza los resultados para que no se olvide nada importante. El Cybersecurity Framework 2.0 del NIST agrupa los resultados en seis funciones: Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar ([NIST CSF 2.0](https://www.nist.gov/cyberframework)). El CAF del Reino Unido expresa resultados e indicadores de buenas prácticas para los operadores de servicios esenciales ([NCSC CAF](https://www.ncsc.gov.uk/collection/caf)). También existen objetivos sectoriales; por ejemplo, los objetivos de desempeño en ciberseguridad sanitaria del Departamento de Salud y Servicios Humanos de EE. UU. ([HHS HPH CPGs](https://hphcyber.hhs.gov/performance-goals.html)). Los catálogos detallados de controles, como NIST SP 800-53, enumeran controles específicos ([SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)). Los marcos le dicen *qué resultados* alcanzar; no le dicen qué riesgo importa más para su servicio, eso procede del capítulo 23.

### 24.2 Tipos de control

Los controles **preventivos** detienen un evento (lista de permitidos, autenticación, un límite cableado). Los controles **detectivos** lo advierten (supervisión, comprobaciones de integridad, alarmas). Los controles **correctivos** o **de recuperación** restablecen el servicio (copias de seguridad, procedimientos manuales, equipos de repuesto). Por su naturaleza, los controles son **técnicos**, **procedimentales** (aprobación por dos personas, gestión de cambios), **físicos** (armarios cerrados con llave, interruptores de llave) o **de ingeniería** (diseños que hacen imposible un estado dañino, como una bomba dimensionada de modo que no pueda sobredosificar). En la TO, los controles de ingeniería y físicos suelen ser los más fiables, porque siguen funcionando cuando las computadoras están comprometidas.

### 24.3 Correspondencias y lagunas

Un control solo tiene valor frente a algo. Construya una **correspondencia** entre los escenarios (o técnicas catalogadas, por ejemplo de [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)) y los controles, marcando cada control como preventivo, detectivo o correctivo. Las lagunas aparecen como escenarios con solo controles detectivos (lo sabrá, pero no lo detendrá), sin ningún control correctivo (no podrá recuperarse) o cubiertos solo por controles que comparten un punto único de falla (el modo común del capítulo 16). La correspondencia también pone de manifiesto los **controles huérfanos**, que no abordan nada de su lista: candidatos a revisión.

### 24.4 Restricciones de la TO

Algunos controles habituales en TI son arriesgados o imposibles en TO: los agentes de *endpoint* que consumen recursos del controlador, la aplicación automática de parches, el escaneo activo, el bloqueo de cuentas en una HMI de operador durante una emergencia (bloquear al operador puede ser más peligroso que el atacante). Las alternativas incluyen la supervisión pasiva de la red, la lista de permitidos de aplicaciones en estaciones de trabajo estables, los diodos de datos de solo lectura para flujos unidireccionales, los interruptores de llave físicos para los modos de programación y los controles procedimentales vinculados al registro de turno del operador. El mapa del BMS del CVH los aplica: supervisión pasiva de la VLAN del BMS en lugar de agentes en el controlador, y un enclavamiento cableado de caudal mínimo de aire para la ventilación de los quirófanos en lugar de depender del bloqueo o de los parches.

### 24.5 Ejemplo resuelto: mapa de controles del BMS del CVH (sintético)

**Este caso es sintético.**

| Escenario | Preventivo | Detectivo | Correctivo | Laguna |
|---|---|---|---|---|
| Compromiso remoto del BMS a través de la red corporativa | Lista de permitidos del cortafuegos hacia el servidor del BMS; MFA para la administración del BMS | Supervisión pasiva de la VLAN del BMS | Control manual local de las unidades de tratamiento de aire | Ninguna evidente; verificar el simulacro de control manual |
| Cambio malicioso o erróneo de los puntos de consigna de la ventilación de quirófanos | Derechos de cambio basados en roles | Alarma por renovaciones de aire fuera de rango | La guardia de mantenimiento de instalaciones restablece los puntos de consigna | Ningún límite independiente: añadir un enclavamiento cableado de caudal mínimo de aire |
| Portátil de un proveedor en el controlador del BMS | Armarios cerrados con llave; acompañamiento del proveedor | — | Restaurar la configuración del controlador desde la copia de seguridad | Sin detección; copia de seguridad de la configuración no probada |

El mapa convierte un vago «el BMS es un riesgo» en dos acciones concretas: un enclavamiento de ingeniería y una restauración de la configuración probada.

### 24.6 Errores comunes y límites

- Tratar el cumplimiento de un marco como reducción del riesgo.
- Contar controles en lugar de relacionarlos con escenarios.
- Depender únicamente de la detección para consecuencias que requieren prevención.
- Importar controles de TI a la TO sin considerar la seguridad operativa.

El mapa del BMS del CVH evita cada uno: no cuenta controles, los relaciona con tres escenarios, añade un enclavamiento de ingeniería donde solo existía detección y rechaza controles de TI como la aplicación automática de parches al controlador del BMS. Una puntuación del marco de «Proteger: implementado» no le habría dicho nada al hospital sobre el caudal de aire de los quirófanos.

### Ejercicios — capítulo 24

**EX047 — Clasifique los controles.** *Objetivo:* usar el tipo y la naturaleza. *Entradas:* copias de seguridad fuera de línea; aprobación de pagos por dos personas; analizador de cloro en la salida que dispara una válvula; alerta del SIEM ante nuevas cuentas de administrador; interruptor de llave para la programación del PLC. *Pasos:* clasifique cada uno por tipo y naturaleza. *Evidencia esperada:* tabla. *Rúbrica:* 3 = copias de seguridad correctivo/técnico; aprobación por dos personas preventivo/procedimental; disparo del analizador preventivo (limita la consecuencia)/de ingeniería; alerta del SIEM detectivo/técnico; interruptor de llave preventivo/físico; 2 = un error; 1 = dos errores; 0 = nada.

**EX048 — Encuentre la laguna.** *Objetivo:* relacionar y juzgar. *Entradas:* la tabla del CVH. *Pasos:* añada un escenario (ransomware en el servidor del BMS) con controles en cada columna, después nombre la mejora más valiosa y justifíquela. *Evidencia esperada:* fila y justificación. *Rúbrica:* 3 = controles plausibles que incluyen una restauración probada y el control manual local; mejora justificada por la consecuencia; 2 = fila sin justificación; 1 = fila incompleta; 0 = nada.

### Síntesis del capítulo

Los marcos organizan los resultados; el análisis de riesgos decide las prioridades; las correspondencias conectan los controles con los escenarios que abordan y revelan lagunas. Prefiera combinaciones de prevención, detección y recuperación y, en la TO, favorezca los controles de ingeniería y físicos que siguen funcionando cuando las computadoras no lo hacen.

<!-- cyberabc:chapter-navigation:start ch-24 -->
### Siga estudiando — capítulo 24 de 40

[← Capítulo 23](#ch-23) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 25 →](#ch-25)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-25"></a>

## Capítulo 25 — Laboratorio I

### Resultados de aprendizaje y conexión

Después de este laboratorio usted podrá (1) combinar evidencias de inventario, flujos de red, vulnerabilidades y accesos en una única evaluación de un operador sintético; (2) registrar métodos, versiones y salidas para que otra persona pueda reproducir sus resultados; (3) separar hallazgos, interpretaciones y recomendaciones; y (4) evaluar su propio trabajo con una rúbrica. Integra los laboratorios 2, 4, 5 y 7 (capítulos 3, 7, 9 y 13) y los métodos de los capítulos 15, 23 y 24. Es el primer punto de control del proyecto del curso.

### 25.1 Propósito y reglas

Este laboratorio es una evaluación acotada de los operadores **sintéticos** de Calder que usa únicamente los laboratorios sin conexión del libro. Se aplican sus reglas de enfrentamiento (capítulo 10, actividad práctica): su propia computadora, sin acceso de red a sistemas reales, sin datos reales. La habilidad que se evalúa no es ejecutar código (esa es la parte fácil), sino **reunir la evidencia en un juicio defendible** y documentarlo para que otro estudiante pueda reproducirlo. Sus condiciones de parada también se aplican aquí: si algún script de laboratorio de Calder intenta acceder a la red, deténgase, registre el *hash* del script e infórmele a su tutor.

### 25.2 La tarea

Usted es becario de la County Resilience Partnership. Elabore una **nota de evaluación** de 1500 palabras que responda: «Considerando la evidencia disponible, ¿cuáles son las tres mejoras de seguridad de mayor prioridad para los operadores de Calder y qué confianza tenemos?». Use:

1. **Lab 2** (inventario del CVH): dispositivos sin soporte y mal ubicados.
2. **Lab 4** (flujos de CW): infracciones de la política de conductos.
3. **Lab 5** (avisos de CPN): activos vulnerables, ordenados por explotación y exposición.
4. **Lab 7** (revisión de accesos): cuentas huérfanas, inactivas, compartidas y tóxicas.

La pregunta pide tres prioridades para cuatro operadores, lo que obliga a comparar: una infracción de conducto en CW y una vulnerabilidad de la pasarela de CPN deben clasificarse una frente a otra por su consecuencia, no presentarse en listas separadas.

### 25.3 Método y reproducibilidad

Registre para cada laboratorio: el nombre del archivo y un *hash* SHA-256 del script que ejecutó (`python3 -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" lab05.py`), la versión de Python, la salida exacta y cualquier cambio que haya hecho. La reproducibilidad es evidencia: un lector que vuelve a ejecutar su script y obtiene la misma salida puede confiar en su sección de hallazgos sin tener que confiar en usted ([Sandve et al., 2013](https://doi.org/10.1371/journal.pcbi.1003285)). Si cambió la lista de versiones del Lab 5 para probar VPN-01 frente a otra versión con la corrección, el *hash* de su apéndice debe ser el de ese archivo editado, con el cambio indicado a su lado.

### 25.4 Estructura de la nota

1. **Resumen**: tres prioridades, una frase cada una, con el nivel de confianza (alto/medio/bajo) y su motivo.
2. **Alcance y método**: qué se examinó, cómo y qué no.
3. **Hallazgos**: solo hechos procedentes de las salidas (p. ej., «VPN-01 ejecuta la 9.1; la corrección es la 9.3; el aviso indica explotación»).
4. **Análisis**: razonamiento centrado primero en las consecuencias (capítulo 23): qué hallazgos podrían conducir a los peores resultados y para qué servicio.
5. **Recomendaciones**: cada una relacionada con hallazgos, con el tipo de control (capítulo 24) y un responsable.
6. **Límites**: tamaño de la muestra, datos sintéticos, afirmaciones no verificadas.
7. **Apéndice**: *hashes*, versiones, salidas.

«VPN-01 ejecuta la 9.1; la corrección es la 9.3» pertenece a los hallazgos; «por tanto, el acceso remoto de CPN es la prioridad 1» pertenece al análisis, donde el razonamiento sobre las consecuencias puede cuestionarse por separado.

### 25.5 Ejemplo resuelto: una prioridad, argumentada por completo (sintético)

**Prioridad 1: actualizar y rediseñar el acceso remoto de CPN (confianza: alta).** *Hallazgo:* VPN-01 (expuesto a internet) ejecuta una versión anterior a la corrección de una vulnerabilidad crítica explotada (Lab 5). *Hallazgo:* el diseño original sitúa a los usuarios remotos directamente en la red de control (capítulo 16). *Análisis:* esta es la ruta más corta desde internet hasta el control de los alimentadores; la consecuencia es la pérdida de control de la distribución, el resultado más grave del modelo de servicio de CPN (capítulo 21). *Recomendación:* actualización de emergencia a la 9.3 (correctivo/técnico; responsable: jefe de infraestructura de CPN, esta semana) y, después, terminar el acceso remoto en un servidor de salto de la DMZ con aprobación del proveedor por sesión (preventivo/técnico y procedimental; responsable: seguridad de TO de CPN, el próximo trimestre). *Confianza:* alta, porque el hallazgo procede directamente de los datos de versión y del aviso, y la consecuencia se deriva de la arquitectura. *Límite:* el laboratorio no puede mostrar si la vulnerabilidad ya ha sido explotada; se recomienda una evaluación de compromiso de VPN-01.

### 25.6 Rúbrica de evaluación

| Criterio | 3 (sólido) | 2 | 1 | 0 |
|---|---|---|---|---|
| Uso de la evidencia | Todo hallazgo es trazable hasta una salida de laboratorio | Mayoritariamente trazable | Algunas afirmaciones sin respaldo | Sin evidencia |
| Priorización | Primero las consecuencias, comparadas entre operadores | Razonada dentro de cada operador | Ordenada solo por etiquetas de gravedad | Ninguna |
| Recomendaciones | Relacionadas con hallazgos, tipificadas, con responsable y fecha | Relacionadas, sin responsables | Genéricas | Ninguna |
| Límites y confianza | Específicos y honestos | Genéricos | Simbólicos | Ausentes |
| Reproducibilidad | *Hashes*, versiones, salidas | Solo salidas | Parcial | Ninguna |

La rúbrica premia los mismos hábitos que la prioridad resuelta: cada hallazgo trazado hasta una salida, consecuencias comparadas entre operadores, responsables y fechas en las recomendaciones, límites honestos y un apéndice reproducible. Una nota que obtiene un 3 en evidencia pero un 1 en priorización ha enumerado hallazgos sin juzgarlos.

### 25.7 Errores comunes y límites

- Enumerar todos los hallazgos en lugar de priorizar.
- Recomendaciones que no se derivan de ningún hallazgo.
- Mezclar hechos e interpretaciones en la sección de hallazgos.
- Afirmar una certeza que los datos sintéticos no pueden proporcionar.

Una nota que enumera los seis flujos del Lab 4, los cinco dispositivos sin soporte y todas las cuentas del Lab 7 ha cometido el primer error. Recomendar MFA para CW sin un hallazgo sobre las cuentas de CW es el segundo. Escribir «la conexión RDP es un intruso» en los hallazgos es el tercero. Afirmar una confianza alta sobre la explotación en el mundo real a partir de datos sintéticos es el cuarto.

### Ejercicios — capítulo 25

**EX049 — Prioridades 2 y 3.** *Objetivo:* completar la evaluación. *Entradas:* laboratorios 2, 4 y 7. *Pasos:* escriba las prioridades 2 y 3 con el formato de la prioridad resuelta anterior. *Evidencia esperada:* dos prioridades argumentadas. *Rúbrica:* use la rúbrica de evaluación del laboratorio; 3 = p. ej., los flujos RDP corporativo→control y control→internet de CW investigados y cerrados (Lab 4), y las cuentas de bajas, tóxicas y de proveedores (Lab 7) o el aislamiento de los dispositivos clínicos sin soporte (Lab 2), cada una con razonamiento sobre las consecuencias, responsable y confianza; puntuaciones inferiores según la rúbrica.

**EX050 — Comprobación de reproducibilidad.** *Objetivo:* verificar el trabajo de un compañero. *Entradas:* el apéndice de un compañero (o el suyo, intercambiado). *Pasos:* vuelva a ejecutar cada script, compare *hashes* y salidas, y escriba una declaración de verificación de 100 palabras. *Evidencia esperada:* la declaración. *Rúbrica:* 3 = *hashes* y salidas comparados, cualquier discrepancia explicada (p. ej., script editado, versión de Python); 2 = solo salidas; 1 = declaración sin volver a ejecutar; 0 = nada.

### Síntesis del capítulo

El Laboratorio I convierte ejercicios separados en un único juicio. Trace cada hallazgo hasta una salida reproducible, razone a partir de las consecuencias entre operadores, relacione las recomendaciones con los hallazgos y los responsables, y declare explícitamente la confianza y los límites.

<!-- cyberabc:chapter-navigation:start ch-25 -->
### Siga estudiando — capítulo 25 de 40

[← Capítulo 24](#ch-24) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 26 →](#ch-26)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-26"></a>

## Capítulo 26 — Infraestructura crítica y seguridad sectorial: métodos II

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) construir modelos de amenazas estructurados de un sistema mediante diagramas de flujo de datos y una lista de comprobación de amenazas; (2) aplicar el análisis de peligros basado en la teoría de sistemas (STPA) para encontrar acciones de control inseguras; (3) diseñar y conducir un ejercicio de mesa como método para poner a prueba los planes; y (4) comparar estos métodos con los métodos de riesgo del capítulo 23 y elegir entre ellos. Se apoya en los capítulos 21–24 y prepara el capítulo 27 (verificación) y el capítulo 28 (análisis de fallas).

### 26.1 Modelado de amenazas con flujos de datos

Un **diagrama de flujo de datos** muestra procesos, almacenes de datos, entidades externas, flujos y **límites de confianza** (donde los datos pasan de un nivel de confianza a otro). El modelado de amenazas recorre cada elemento y plantea una lista de preguntas. Una lista muy utilizada, STRIDE (acrónimo de las iniciales de los términos en inglés), pregunta por la suplantación de identidad (**S**), la manipulación de datos (**T**), el repudio (**R**, negar una acción), la divulgación de información (**I**), la denegación de servicio (**D**) y la elevación de privilegios (**E**). Cada flujo que cruza un límite de confianza merece la lista completa. El resultado es una lista de amenazas con el elemento, el tipo de amenaza y una mitigación propuesta.

### 26.2 STPA: peligros a partir de la estructura de control

El modelo **STAMP** de Leveson trata los accidentes como el resultado de un control inadecuado y no como cadenas de fallas de componentes ([Leveson, 2004](https://doi.org/10.1016/S0925-7535(03)00047-X)). Su método de análisis, **STPA**, procede así: definir las pérdidas y los peligros; modelar la **estructura de control** (quién controla qué y con qué realimentación); para cada acción de control, identificar las **acciones de control inseguras** (UCA) en cuatro formas: no proporcionada cuando se necesita, proporcionada cuando es insegura, proporcionada demasiado pronto, demasiado tarde o fuera de orden, detenida demasiado pronto o aplicada demasiado tiempo; y después encontrar escenarios causales, incluidas la realimentación o las órdenes manipuladas. STPA se adapta bien a los servicios críticos porque trata a los operadores, los procedimientos, el software y los atacantes dentro de una misma estructura.

### 26.3 Ejercicios de mesa

Un **ejercicio de mesa** conduce a un equipo por un escenario mediante la discusión, paso a paso, con inyecciones («son las 03:40; las pantallas del CAD muestran una nota de rescate»). Pone a prueba los planes, los roles y la comunicación sin tocar los sistemas en producción. Los buenos ejercicios de mesa tienen objetivos (p. ej., «poner a prueba la decisión de pasar al despacho en papel»), un escenario sintético realista, un facilitador, observadores que registran las decisiones y los tiempos, y una **revisión en caliente** seguida de un plan de mejora. Son evidencia de preparación solo en la medida en que se actúa sobre sus hallazgos.

### 26.4 Elegir los métodos

| Método | Más adecuado para | Debilidad |
|---|---|---|
| Evaluación de riesgos (cap. 23) | Priorizar entre muchos escenarios | Estimaciones de probabilidad débiles para amenazas novedosas |
| Primero las consecuencias / CCE | Peores resultados, mitigaciones de ingeniería | Puede descuidar los daños moderados frecuentes |
| Modelo de amenazas STRIDE | Software y flujos de datos | Débil en el proceso físico y las personas |
| STPA | Estructuras de control, interacciones entre personas y software | Laborioso; requiere conocer el proceso |
| Ejercicio de mesa | Planes, roles, comunicación | Discutir no es ejecutar |

Para el CEDC, la tabla sugiere STPA para el control del despacho y un ejercicio de mesa para el respaldo en papel, como hace el capítulo; después, una evaluación de riesgos clasifica el trabajo resultante.

### 26.5 Ejemplo resuelto: STPA para el despacho del CEDC (sintético)

**Este caso es sintético.** Pérdida: respuesta de emergencia retrasada. Peligro: no se despacha una ambulancia a una llamada con riesgo vital dentro del tiempo objetivo. Estructura de control: operador de llamadas → CAD → despachador → tripulación de la ambulancia (por radio y terminales móviles de datos); realimentación del sistema de localización de vehículos al CAD. Acción de control: «asignar la ambulancia disponible más cercana». UCA: *no proporcionada*: la cola del CAD queda congelada tras una actualización fallida; *proporcionada cuando es insegura*: el CAD asigna una unidad que figura como «disponible» porque la realimentación de localización está obsoleta o suplantada; *demasiado tarde*: el respaldo manual se adopta solo al cabo de 20 minutos porque nadie es responsable de la decisión; *detenida demasiado pronto*: un despachador cancela una asignación tras un error al fusionar llamadas duplicadas. Cada UCA da lugar a requisitos: una alarma de congelación del CAD, indicadores de obsolescencia en las localizaciones de los vehículos, un responsable designado de la decisión de respaldo con un disparador a los 5 minutos y una confirmación antes de cancelar una asignación de alta prioridad. Observe que dos UCA no implican a ningún atacante.

### 26.6 Errores comunes y límites

- Modelos de amenazas sin límites de confianza.
- STPA reducido a una lista de fallas de componentes.
- Ejercicios de mesa sin objetivos ni seguimiento.
- Elegir el método más impresionante en lugar del que necesita la pregunta.

El STPA del CEDC evitó el segundo error al nombrar acciones de control inseguras, dos de ellas sin atacante alguno. Una revisión STRIDE del flujo del historiador de CW que no marcara el límite de confianza entre la DMZ y el control cometería el primero. Un ejercicio de mesa sin el objetivo «decidir sobre el despacho en papel» comete el tercero. Y elegir STPA para impresionar cuando la pregunta es «qué estrategia de respaldo» comete el cuarto.

### Ejercicios — capítulo 26

**EX051 — Aplique STRIDE a un flujo.** *Objetivo:* aplicar la lista de comprobación. *Entradas:* el flujo de CW «el colector del historiador en la DMZ lee OPC UA del servidor SCADA». *Pasos:* escriba una amenaza para cada letra de STRIDE con una mitigación. *Evidencia esperada:* seis filas. *Rúbrica:* 3 = seis amenazas plausibles con las mitigaciones correspondientes (p. ej., colector suplantado → certificados mutuos; manipulación → sesión firmada/autenticada; DoS → límites de tasa en el lado del SCADA); 2 = cuatro o cinco; 1 = menos; 0 = nada.

**EX052 — Diseñe un ejercicio de mesa.** *Objetivo:* planificar un ejercicio. *Entradas:* CVH, escenario «un ransomware cifra el sistema de administración de pacientes un sábado por la noche». *Pasos:* escriba los objetivos (dos), los participantes, cuatro inyecciones con sus horas y la evidencia que registrará. *Evidencia esperada:* plan. *Rúbrica:* 3 = objetivos medibles, participantes clínicos y técnicos, inyecciones realistas y crecientes (incluidas decisiones de protección de datos y de comunicación), tiempos y decisiones registrados; 2 = parcial; 1 = solo el escenario; 0 = nada.

### Síntesis del capítulo

El modelado de amenazas encuentra amenazas donde los datos cruzan límites de confianza; STPA encuentra acciones de control inseguras en estructuras sociotécnicas; los ejercicios de mesa ponen a prueba los planes y las personas. Cada uno ve lo que los demás pasan por alto, así que elija según la pregunta y recuerde que muchos peligros no implican a ningún adversario.

<!-- cyberabc:chapter-navigation:start ch-26 -->
### Siga estudiando — capítulo 26 de 40

[← Capítulo 25](#ch-25) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 27 →](#ch-27)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-27"></a>

## Capítulo 27 — Infraestructura crítica y seguridad sectorial: verificación

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) distinguir la verificación («construido correctamente») de la validación («se construyó lo correcto») en los controles de seguridad; (2) diseñar una prueba que pueda mostrar que un control *no* funciona; (3) evaluar un detector mediante la precisión y la exhaustividad y elegir un umbral con compromisos explícitos; y (4) informar de los resultados de la verificación con sus condiciones y límites. Se apoya en los capítulos 8, 12, 15 y 24 y prepara el capítulo 29 (operaciones) y el Laboratorio II (capítulo 30).

### 27.1 Verificación y validación

La **verificación** comprueba que un control hace lo que dice su especificación: el cortafuegos bloquea el puerto 3389 desde la red corporativa hacia la de control; el validador de puntos de consigna rechaza NaN. La **validación** comprueba que el control logra su propósito en el entorno real: los usuarios corporativos no pueden alcanzar los sistemas de control por *ninguna* ruta; los operadores no pueden enviar puntos de consigna inseguros. Un control puede superar la verificación y fallar la validación (la regla del cortafuegos funciona, pero un portátil de ingeniería con doble conexión la elude). Una buena verificación es **falsable**: está diseñada para que un control defectuoso no supere la prueba. Una prueba que se superaría tanto si el control funciona como si no, no demuestra nada.

### 27.2 Tipos de prueba

La **revisión de la configuración** compara los ajustes con una línea base. Las **pruebas funcionales** ejercitan el control con entradas esperadas y prohibidas (las pruebas de límites del capítulo 8). Las **pruebas de flujo** confirman que las rutas no permitidas están bloqueadas (capítulo 7, con autorización). Los **simulacros de restauración** verifican de extremo a extremo los controles de recuperación (capítulo 15). Las **pruebas de detección** reproducen actividad sintética etiquetada o benigna pero sospechosa para ver si la supervisión genera alertas. En la TO, las pruebas sobre el proceso en producción están restringidas; use bancos de pruebas, réplicas fuera de línea o ventanas planificadas acordadas con operaciones. Para la regla de CW entre la red corporativa y la de control, una prueba de flujo desde un equipo corporativo autorizado hacia direcciones de control en una ventana planificada es funcional; una revisión de la configuración por sí sola no lo es.

### 27.3 Evaluar detectores

Un detector produce puntuaciones; un umbral las convierte en alertas. Compare las alertas con las etiquetas de la verdad de referencia: **verdaderos positivos** (TP), **falsos positivos** (FP), **falsos negativos** (FN). **Precisión** = TP/(TP+FP): de las alertas, ¿cuántas eran reales? **Exhaustividad** = TP/(TP+FN): de los eventos reales, ¿cuántos se detectaron? Subir el umbral suele aumentar la precisión y reducir la exhaustividad. Con eventos maliciosos raros (la tasa base del capítulo 12), la precisión puede ser mala incluso con tasas de error por evento excelentes. Elija un umbral preguntándose cuánto le cuesta al servicio cada omisión y cada falsa alarma, y recuerde que los datos de evaluación etiquetados rara vez coinciden con las condiciones reales ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp)).

### 27.4 Ejemplo resuelto y Lab 10 (sintético)

**Este caso es sintético.** Calder Mutual evalúa un detector de anomalías sobre 5025 eventos etiquetados, 25 de ellos maliciosos (semilla 10).

```python
# Lab 10 - detection evaluation on a labelled synthetic event set (offline)
import random
random.seed(10)
events = []  # (score from a detector, truly malicious?)
for _ in range(5000):
    events.append((random.gauss(0.30, 0.12), False))
for _ in range(25):
    events.append((random.gauss(0.70, 0.15), True))
for thr in (0.5, 0.6, 0.7):
    tp = sum(1 for s, m in events if s >= thr and m)
    fp = sum(1 for s, m in events if s >= thr and not m)
    fn = sum(1 for s, m in events if s < thr and m)
    prec = tp / (tp + fp) if tp + fp else 0
    print(f"threshold {thr}: TP={tp:2} FP={fp:3} FN={fn:2} precision={prec:.2f} recall={tp/(tp+fn):.2f}")
```

Salida esperada:

```text
threshold 0.5: TP=23 FP=215 FN= 2 precision=0.10 recall=0.92
threshold 0.6: TP=20 FP= 36 FN= 5 precision=0.36 recall=0.80
threshold 0.7: TP=18 FP=  2 FN= 7 precision=0.90 recall=0.72
```

Con 0,5, el equipo detecta 23 de 25, pero tiene que abrirse paso entre 215 falsas alertas; con 0,7, casi todas las alertas son reales, pero se pasan por alto 7 ataques. Ninguno es «correcto». Una elección defendible podría usar 0,7 para avisar al analista de guardia y 0,5 para una cola de revisión diaria: dos umbrales para dos costes. El informe declara las condiciones: puntuaciones sintéticas, una sola semilla, 25 positivos (por lo que las estimaciones de exhaustividad son gruesas; capítulo 37) y una similitud desconocida con el tráfico real.

### 27.5 Errores comunes y límites

- Pruebas que no pueden fallar.
- Informar de la exactitud con datos desequilibrados (aquí, un 99,5 % de «exactitud» sin alertar nunca).
- Elegir umbrales sin declarar los costes.
- Evaluar con datos que se parecen más a los de entrenamiento que a la realidad.
- Verificar en un laboratorio y afirmar la validación en producción.

El Lab 10 muestra numéricamente el segundo error: no alertar nunca obtiene un 99,5 % de exactitud. Elegir 0,5 o 0,7 sin decir cuánto cuesta un ataque no detectado o 215 falsas alertas adicionales es el tercero. Una regla de cortafuegos probada solo desde la réplica del laboratorio es el quinto. Una prueba que informaría de «bloqueado» porque el equipo de prueba estaba apagado es el primero.

### Ejercicios — capítulo 27

**EX053 — Hágala falsable.** *Objetivo:* diseñar una prueba significativa. *Entradas:* la afirmación «el cortafuegos de CW impide que los usuarios corporativos alcancen la zona de control». *Pasos:* diseñe una prueba de verificación y una de validación, cada una con un resultado que demostraría que la afirmación es falsa, y la autorización necesaria. *Evidencia esperada:* dos diseños de prueba. *Rúbrica:* 3 = prueba a nivel de regla desde un equipo corporativo hacia las direcciones de control en todos los puertos en una ventana planificada, más una validación que busca rutas alternativas (equipos con doble conexión, acceso remoto, inalámbrico) mediante la revisión de la configuración y de los flujos; autorización declarada; 2 = una prueba; 1 = no falsable; 0 = nada.

**EX054 — La trampa de la exactitud.** *Objetivo:* ver por qué la exactitud induce a error. *Entradas:* el Lab 10. *Pasos:* calcule la exactitud para el umbral 0,7 y para un detector que nunca alerta; explique por qué ambos parecen «excelentes». *Evidencia esperada:* dos números y una explicación. *Rúbrica:* 3 = (5025−2−7)/5025 ≈ 0,9982 y 5000/5025 ≈ 0,9950; explica el desequilibrio de clases y recomienda la precisión y la exhaustividad; 2 = solo los números; 1 = un número; 0 = nada.

### Síntesis del capítulo

La verificación pregunta si un control funciona según lo especificado; la validación pregunta si logra su propósito. Diseñe pruebas que puedan fallar, evalúe los detectores con la precisión y la exhaustividad en umbrales elegidos según costes declarados, e informe de las condiciones y los límites junto con los números.

<!-- cyberabc:chapter-navigation:start ch-27 -->
### Siga estudiando — capítulo 27 de 40

[← Capítulo 26](#ch-26) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 28 →](#ch-28)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-28"></a>

## Capítulo 28 — Infraestructura crítica y seguridad sectorial: análisis de fallas

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) construir un árbol de fallas sencillo con puertas AND y OR y calcular la probabilidad del evento superior bajo independencia; (2) realizar un análisis de modos de falla y sus efectos (FMEA) de un sistema pequeño; (3) añadir una ruta cibernética a un análisis de seguridad y ver cómo cambia el resultado; y (4) conducir una revisión posincidente sin culpables que busque las causas en el sistema. Se apoya en los capítulos 12, 21, 22 y 26 y prepara el capítulo 29 (operaciones) y el capítulo 31 (casos avanzados).

### 28.1 Árboles de fallas

Un **árbol de fallas** parte de un **evento superior** no deseado y lo descompone en causas conectadas por **puertas**. Una puerta **AND** significa que deben producirse todas las entradas; una puerta **OR** significa que basta con una cualquiera. Con eventos básicos independientes, AND multiplica las probabilidades y OR las combina como $1 - \prod (1 - p_i)$. Los árboles de fallas hacen explícitos los supuestos y muestran qué eventos básicos dominan. Tradicionalmente se construyen para fallas aleatorias; el análisis de seguridad añade rutas en las que un adversario puede hacer que un evento ocurra a propósito, y la «probabilidad» de un adversario no es una propiedad del hardware.

### 28.2 FMEA

El **análisis de modos de falla y sus efectos** trabaja de abajo arriba: para cada componente, enumere las formas en que puede fallar (no arranca, falla en posición abierta, da una lectura falsa), el efecto sobre el sistema, cómo se detectaría y los controles existentes; después, clasifique. El FMEA encuentra bien los problemas de un solo componente y mal las interacciones, por lo que se combina con STPA (capítulo 26) y con los árboles de fallas. El EX056 aplica el FMEA a la bomba dosificadora y al analizador de CW. Una fila para la bomba dosificadora de CW dice: componente, bomba dosificadora; modo, funciona al caudal máximo; efecto, sobrecloración en la salida; detección, alarma del analizador de residual en la salida; control existente, caudal máximo de la bomba cableado.

### 28.3 Ejemplo resuelto y Lab 11 (sintético)

**Este caso es sintético.** Evento superior en el CVH: «el hospital pierde la alimentación de calidad de red en las cargas críticas». Físicamente, esto requiere un corte de la red eléctrica AND una falla del respaldo (el generador no arranca OR el combustible está contaminado OR falla el conmutador de transferencia automática). Por otra parte, el BMS del hospital puede dar órdenes al cuadro de suministro esencial; un compromiso del BMS podría desconectar cargas críticas con independencia de la red.

```python
# Lab 11 - a small fault tree for "hospital loses mains-quality power" (synthetic annual probabilities)
P = {"grid": 0.05, "gen_fails_start": 0.02, "fuel_contaminated": 0.005, "ats_fails": 0.01, "cyber_bms": 0.002}
# top = grid AND (backup fails); backup fails = gen_fails_start OR fuel_contaminated OR ats_fails
# separately: a compromised building-management system can shed critical loads whatever the grid state
backup_fails = 1 - (1 - P["gen_fails_start"]) * (1 - P["fuel_contaminated"]) * (1 - P["ats_fails"])
top_physical = P["grid"] * backup_fails
top = 1 - (1 - top_physical) * (1 - P["cyber_bms"])
print(f"P(backup fails on demand) = {backup_fails:.5f}")
print(f"P(top) physical only = {top_physical:.6f}")
print(f"P(top) with BMS path  = {top:.6f}")
print(f"share from cyber path ~ {P['cyber_bms'] / top:.0%}")
```

Salida esperada:

```text
P(backup fails on demand) = 0.03465
P(top) physical only = 0.001733
P(top) with BMS path  = 0.003729
share from cyber path ~ 54%
```

Con estos números sintéticos, el diseño físico es bueno: se necesitan dos fallas independientes. La ruta cibernética es un único evento que elude la puerta AND y aproximadamente duplica la probabilidad del evento superior. La cuestión de fondo no depende de la estimación de 0,002: un atacante no falla al azar, de modo que una ruta que solo necesita un «evento» bajo el control del adversario puede dominar sea cual sea el número que usted escriba. La respuesta de ingeniería es restablecer la estructura AND (hacer imposible desconectar las cargas críticas desde el BMS mediante un bloqueo cableado, o limitar el control del BMS a los cuadros no críticos) en lugar de limitarse a reducir la probabilidad estimada.

### 28.4 Revisión posincidente sin culpables

Cuando se producen fallas, una **revisión sin culpables** pregunta cómo permitió el sistema que la acción de una persona razonable causara daño, no a quién castigar. El modelo de accidentes organizacionales de Reason describe las defensas como capas con agujeros que de vez en cuando se alinean ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)). Pregunte: ¿qué sabían las personas en ese momento?; ¿qué hizo que su acción pareciera correcta?; ¿qué defensas faltaban o se eludieron?; ¿qué cambiaremos en el sistema? La culpa reprime la notificación, y los casi accidentes no notificados son evidencia perdida. En el caso del Lab 11, una revisión sin culpables de un evento de pérdida de alimentación preguntaría por qué el BMS podía siquiera desconectar cargas críticas.

### 28.5 Errores comunes y límites

- Multiplicar probabilidades de eventos con causas comunes (capítulo 12).
- Tratar las acciones del adversario como fallas aleatorias.
- FMEA sin interacciones; árboles de fallas sin el factor humano.
- Revisiones que terminan en «error humano» y una nueva formación.

El Lab 11 supone la independencia entre la falla del generador y la contaminación del combustible; el EX024 muestra cómo un depósito de combustible compartido rompe esa independencia. La ruta del BMS es el segundo error hecho explícito: 0,002 no es una propiedad del BMS. El tercero aparece si un FMEA del generador ignora al operador que debe arrancarlo manualmente. Una revisión que termina en «error del ingeniero de mantenimiento; volver a formarlo» es el cuarto.

### Ejercicios — capítulo 28

**EX055 — Restablezca la puerta AND.** *Objetivo:* ver el efecto de una corrección de ingeniería. *Entradas:* el Lab 11. *Pasos:* modele una corrección en la que el BMS solo pueda desconectar cargas críticas si también hay un corte de la red (es decir, la ruta cibernética se incorpora a la puerta AND de la red como una causa más de falla del respaldo). Calcule la nueva probabilidad del evento superior. *Evidencia esperada:* código modificado y valor. *Rúbrica:* 3 = falla del respaldo = 1−(0,98)(0,995)(0,99)(0,998) ≈ 0,03658, evento superior ≈ 0,001829, con el comentario de que la ruta cibernética necesita ahora un corte de la red coincidente; 2 = enfoque correcto, error aritmético; 1 = estructura sin cambios; 0 = nada.

**EX056 — Filas de FMEA.** *Objetivo:* aplicar el análisis de abajo arriba. *Entradas:* la bomba dosificadora de cloro de CW y su analizador de residual. *Pasos:* escriba cuatro filas de FMEA (componente, modo de falla, efecto, detección, control existente). *Evidencia esperada:* tabla. *Rúbrica:* 3 = modos realistas (la bomba funciona al máximo, la bomba se detiene, el analizador lee bajo, el analizador está congelado) con efectos sobre la seguridad del agua y detecciones creíbles; 2 = tres; 1 = vago; 0 = nada.

### Síntesis del capítulo

Los árboles de fallas y el FMEA hacen explícitos los supuestos sobre las fallas, de arriba abajo y de abajo arriba. Añadir rutas cibernéticas revela eventos únicos que eluden la redundancia diseñada; la respuesta más sólida restablece la independencia estructural en lugar de ajustar una estimación. Cuando se producen fallas, revise el sistema, no a la persona.

<!-- cyberabc:chapter-navigation:start ch-28 -->
### Siga estudiando — capítulo 28 de 40

[← Capítulo 27](#ch-27) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 29 →](#ch-29)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-29"></a>

## Capítulo 29 — Infraestructura crítica y seguridad sectorial: operaciones

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) describir las operaciones de seguridad de un operador de servicios críticos: supervisión, triaje, escalado, gestión de cambios y de vulnerabilidades; (2) adaptar la respuesta a incidentes a la tecnología operativa, donde mantener seguro el proceso es lo primero; (3) medir el desempeño operativo con el tiempo de detección y el tiempo de recuperación mediante medianas y percentiles; y (4) redactar un paso de un manual de respuesta que respete tanto la seguridad como las operaciones. Se apoya en los capítulos 12, 15, 24, 27 y 28 y prepara el Laboratorio II (capítulo 30).

### 29.1 Qué hacen las operaciones de seguridad

En el día a día, una función de operaciones de seguridad **supervisa** (registros, tráfico de red, alertas), **hace el triaje** (¿es real?, ¿qué gravedad tiene?), **escala** (¿a quién?, ¿con qué rapidez?), **coordina los cambios** (ningún cambio por sorpresa en los sistemas de TO) y **gestiona las vulnerabilidades** (capítulos 5, 9 y 11). Para un operador de servicios críticos, el rasgo definitorio es la colaboración con **operaciones**: el personal de la sala de control, los ingenieros y los clínicos saben cómo es la normalidad del proceso y son responsables de las decisiones que lo afectan. Unas operaciones de seguridad que no hablan con la sala de control interpretarán mal las alertas y, peor aún, tomarán medidas que dañen el servicio.

### 29.2 Respuesta a incidentes en TO

Las recomendaciones del NIST sobre respuesta a incidentes, revisadas en 2025, sitúan la respuesta dentro de la gestión global del riesgo de ciberseguridad y de las funciones del CSF 2.0 ([SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). En la TO cambia el orden de prioridades: **primero mantener seguro el proceso** (lo que puede implicar pasar a control manual o local), **después contener** (aislar los segmentos de TI o TO afectados sin cortar lo que el proceso necesita) y **después investigar y recuperar**. Desconectar un servidor comprometido es un acto reflejo en TI; en TO, el operador debe saber primero qué hace ese servidor: desconectar el historiador es inocuo, desconectar el único servidor SCADA puede dejar ciegos a los operadores durante una tormenta. También debe preservarse la evidencia: imágenes de las estaciones de ingeniería, configuraciones de los controladores, capturas de red y el registro del operador. Los manuales de respuesta se acuerdan de antemano con operaciones, seguridad funcional y, cuando puedan intervenir datos personales, protección de datos (capítulo 14).

### 29.3 Medir las operaciones

Las medidas habituales son el **tiempo de detección** (TTD: desde la primera actividad maliciosa o defectuosa hasta la detección) y el **tiempo de recuperación** (TTR: desde la detección hasta el servicio restablecido). Sus distribuciones son asimétricas (capítulo 12): la mayoría de los incidentes se resuelven rápidamente; unos pocos llevan días. Informe de la **mediana**, el **percentil 90** y el **tamaño de la muestra**, e inspeccione los valores atípicos uno por uno: la cola larga es donde están las lecciones. Cuidado con los incentivos: un objetivo de TTD puede animar a registrar con generosidad la hora de «detección». Los 15 registros del Lab 12 muestran por qué: media de 27,2 horas, mediana de 4. Inspeccione individualmente la detección de 240 horas; fue un uso indebido lento de credenciales.

### 29.4 Ejemplo resuelto y Lab 12 (sintético)

**Este caso es sintético.** Los miembros de la CRP pusieron en común 15 registros de incidentes depurados de los dos últimos años.

```python
# Lab 12 - time to detect and recover: mean, median and percentiles from synthetic tickets (offline)
import statistics as st
TTD_H = [0.5, 1, 1, 2, 2, 3, 3, 4, 6, 8, 12, 20, 36, 70, 240]   # hours from first malicious activity to detection
TTR_H = [2, 3, 3, 4, 5, 5, 6, 8, 8, 10, 12, 16, 24, 48, 96]
for name, xs in (("time to detect", TTD_H), ("time to recover", TTR_H)):
    q = st.quantiles(xs, n=10, method="inclusive")
    print(f"{name}: n={len(xs)} mean={st.mean(xs):.1f} median={st.median(xs):.1f} p90={q[8]:.1f} max={max(xs)}")
print("mean TTD without the 240 h outlier:", round(st.mean(TTD_H[:-1]), 1))
```

Salida esperada:

```text
time to detect: n=15 mean=27.2 median=4.0 p90=56.4 max=240
time to recover: n=15 mean=16.7 median=8.0 p90=38.4 max=96
mean TTD without the 240 h outlier: 12.0
```

El tiempo medio de detección (27,2 h) no describe ningún incidente real: la mitad se detectaron en 4 horas y uno tardó diez días. Eliminar ese único registro reduce la media a menos de la mitad. El informe útil dice: «mediana de 4 h, percentil 90 de unas 56 h, n = 15; el caso de 240 horas fue un uso indebido lento de credenciales descubierto durante una revisión de accesos», y después pregunta por qué la supervisión no lo detectó. Los percentiles sobre 15 registros son aproximados; debe indicarse el método para calcularlos (aquí, el método «inclusive» de `statistics.quantiles` de Python).

### 29.5 Un paso de un manual de respuesta (sintético)

*Manual de respuesta de CPN, paso 3: sospecha de compromiso de una estación de ingeniería:* (1) El analista de seguridad informa al supervisor de la sala de control; el supervisor confirma que ninguna maniobra depende ahora de la estación. (2) El supervisor autoriza el aislamiento; el analista aísla el puerto de red de la estación y la deja encendida (para preservar la memoria). (3) Un ingeniero comprueba las configuraciones de los controladores que la estación podría haber cambiado, comparándolas con la última copia de seguridad conocida como buena. (4) El analista registra las horas, las decisiones y quién las autorizó en el registro del incidente. Cada paso indica quién decide y por qué importa el orden. Si un ingeniero de CPN estuviera a mitad de una maniobra de transferencia de carga en torno a la Subestación Norte desde esa estación, desconectar su puerto de red dejaría la operación a medias, con la sala de control sin saber qué interruptores se habían movido.

### 29.6 Errores comunes y límites

- Equipos de seguridad que actúan sobre la TO sin autorización de operaciones.
- Cortar la alimentación o borrar sistemas antes de preservar la evidencia.
- Informar de tiempos medios con datos asimétricos.
- Manuales de respuesta que solo existen en los sistemas que el incidente ha inutilizado.

El manual de CPN evita los dos primeros haciendo que el supervisor autorice el aislamiento y dejando encendida la estación. El Lab 12 muestra el tercero. El cuarto explica por qué los miembros de la CRP guardan copias impresas de los manuales en cada sala de control, ya que un incidente puede inutilizar el sistema documental que los contiene.

### Ejercicios — capítulo 29

**EX057 — Informe de la cola.** *Objetivo:* resumir con honestidad datos asimétricos. *Entradas:* el Lab 12. *Pasos:* escriba un resumen de 100 palabras para el consejo de la CRP sobre el TTD y el TTR, que incluya el tamaño de la muestra, una limitación y una pregunta sobre el caso más largo. *Evidencia esperada:* el resumen. *Rúbrica:* 3 = medianas y p90 con n, se señala la distorsión de la media, limitación (pocos registros, depurados, horas de detección autodeclaradas), pregunta incisiva; 2 = números sin salvedades; 1 = solo medias; 0 = nada.

**EX058 — Contención segura.** *Objetivo:* ordenar las acciones de respuesta en TO. *Entradas:* se detecta ransomware en el servidor historiador de CW en la zona de control; los servidores SCADA parecen no estar afectados. *Pasos:* escriba las cinco primeras acciones en orden, con quién decide cada una. *Evidencia esperada:* lista ordenada. *Rúbrica:* 3 = confirmar el estado del proceso con operaciones; preparar la operación manual/local; aislar el historiador de la zona de control con la aprobación de operaciones; preservar la evidencia; comprobar el SCADA y los controladores frente a una referencia conocida como buena, con los roles nombrados; 2 = razonable pero sin orden o sin roles; 1 = al estilo de TI, «apagarlo todo»; 0 = nada.

### Síntesis del capítulo

Las operaciones de seguridad en los servicios críticos trabajan codo con codo con operaciones: primero mantener seguro el proceso, contener sin dejar ciegos a los operadores, preservar la evidencia y recuperar. Mida con medianas, percentiles y tamaños de muestra, e investigue los valores atípicos que los promedios ocultan.

<!-- cyberabc:chapter-navigation:start ch-29 -->
### Siga estudiando — capítulo 29 de 40

[← Capítulo 28](#ch-28) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 30 →](#ch-30)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-30"></a>

## Capítulo 30 — Laboratorio II

### Resultados de aprendizaje y conexión

Después de este laboratorio usted podrá (1) conducir un ejercicio acotado en dos partes (un ejercicio de mesa facilitado y un análisis de evidencias sin conexión) para un escenario intersectorial; (2) reconstruir una cronología a partir de registros sintéticos y verificar la integridad de los registros; (3) evaluar las decisiones frente a los planes y las medidas; y (4) redactar un informe posterior a la acción con un plan de mejora. Integra los capítulos 17, 21, 22, 26, 27 y 29 y es el segundo punto de control del proyecto.

### 30.1 Escenario (sintético)

**Este escenario es sintético.** A las 02:10 de una noche de invierno, la sala de control de Calder Water informa de que el punto de consigna de nivel de la estación de bombeo PS2 cambió de 4,1 m a 2,0 m a las 01:52. Nadie admite haber hecho el cambio. A las 02:30, CPN informa de una falla en la Subestación Norte cuya reparación llevará 6 horas. El responsable de guardia del CEDC pregunta si el suministro de agua del hospital está en riesgo. Equipos de cuatro personas desempeñan los papeles de operaciones de CW, seguridad de CW, control de CPN y mantenimiento de instalaciones del CVH; un facilitador introduce las inyecciones. Calder Water podría investigar el cambio del punto de consigna de PS2, y CPN podría reparar la Subestación Norte en 6 horas; juntos plantean la pregunta que ninguno puede responder por separado: si el agua del hospital aguanta mientras ninguno de los dos problemas está resuelto.

### 30.2 Parte A: ejercicio de mesa (90 minutos)

Objetivos: (1) decidir en 20 minutos si se pasa PS2 a control local; (2) elaborar un estado consolidado de todos los operadores para el CEDC antes de las 03:00; (3) decidir qué evidencia preservar. Inyecciones: 02:40, seguridad de CW descubre que una sesión remota de un proveedor estuvo activa de 01:45 a 01:58; 02:55, mantenimiento de instalaciones del CVH informa de que tiene combustible para 72 h en el generador, pero pregunta por el agua; 03:20, un periodista local llama a CW. Los observadores registran las horas de las decisiones, quién decidió y con qué evidencia. Los observadores deben anotar el minuto en que se tomó cada decisión, quién la tomó y con qué evidencia, para que el informe posterior a la acción pueda comparar los tiempos con los objetivos. El objetivo de 20 minutos para PS2 empieza a contar a las 02:10.

### 30.3 Parte B: análisis de evidencias (sin conexión)

Con la función de cadena de *hashes* del Lab 8, los equipos reciben tres archivos: el registro del operador, la cabeza anclada procedente del servidor de anclaje separado y el registro de la sesión del proveedor. Recalculan la cadena, encuentran qué entrada (si la hay) se alteró y la alinean con las horas de la sesión. Con el modelo de autonomía del Lab 9 (capítulo 22) y el corte de 6 horas, indican qué servicios se pierden y cuándo, y si el agua del hospital depende de PS2. Todo resultado debe ser reproducible: *hash* del script, versión de Python, salida. Con 10 horas de almacenamiento de agua tratada frente a un corte de 6 horas, el agua del hospital debería aguantar según las cifras del Lab 9; la pregunta abierta para los equipos es si esa cifra de almacenamiento sigue siendo válida con el punto de consigna de PS2 en 2,0 m en lugar de los 4,1 m habituales.

### 30.4 Ejemplo resuelto: la cronología y sus límites (sintético)

| Hora | Evento | Fuente | Confianza |
|---|---|---|---|
| 01:45 | Se abre la sesión remota del proveedor | Registro de acceso remoto | Alta (registro del sistema) |
| 01:52 | Punto de consigna de PS2 4,1 → 2,0 m | Entrada 2 del registro del operador | Media: el recálculo de la cadena muestra que la entrada 2 no coincide con la cabeza anclada, por lo que el registro se alteró a posteriori |
| 01:58 | Se cierra la sesión del proveedor | Registro de acceso remoto | Alta |
| 02:10 | Los operadores lo advierten | Registro de turno | Alta |
| 02:30 | Falla en la Subestación Norte (6 h) | Control de CPN | Alta |

Interpretación: el cambio del punto de consigna coincide con la sesión del proveedor, y la entrada del registro que lo recoge fue alterada, lo que es coherente con un cambio malicioso o descuidado ocultado después, pero no prueba quién lo hizo. Intersectorial: con un corte de la red de 6 horas, las bombas de CW se detienen de inmediato y el almacenamiento de agua tratada (10 h) mantiene el suministro (Lab 9); un punto de consigna rebajado significa menos agua almacenada de lo previsto, lo que acorta esa autonomía: la interacción peligrosa se da entre dos eventos que, por separado, son manejables. Decisiones: pasar PS2 a control local y restablecer el punto de consigna (operaciones); suspender el acceso remoto de los proveedores (seguridad, con el director de CW); preservar el registro de la sesión del proveedor, la imagen del servidor de registros y el ancla (seguridad); informar al CEDC y al CVH con un intervalo estimado de autonomía del agua (operaciones, antes de las 03:00); y remitir a los medios al portavoz acordado.

### 30.5 Informe posterior a la acción

Estructura: objetivos y si se cumplieron (con horas); qué salió bien; qué no; causas raíz (sistémicas, sin culpables; capítulo 28); acciones de mejora con responsables y fechas; apéndice de evidencias. Distinga los **artefactos del ejercicio** (cosas que ocurrieron solo porque era un ejercicio) de los hallazgos reales. En este escenario, la llamada del periodista a las 03:20 pone a prueba un procedimiento real; una inyección tardía del facilitador es un artefacto del ejercicio. Las acciones de mejora se derivan de las causas raíz, como el acceso remoto sin gestionar de los proveedores, no de errores individuales. Para la acción sobre el acceso de los proveedores, la verificación consistiría en comprobar que la cuenta del proveedor está deshabilitada fuera de los tiques aprobados y que puede recuperarse el registro de la sesión de las 01:52.

### 30.6 Rúbrica de evaluación

| Criterio | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| Decisiones | Oportunas, con responsable, basadas en evidencia | Oportunas o basadas en evidencia | Tardías o sin responsable | Ninguna |
| Cronología | Con fuentes, confianza graduada, integridad comprobada | Con fuentes | Sin fuentes | Ninguna |
| Razonamiento intersectorial | Interacción identificada y cuantificada | Identificada | Un solo sector | Ninguno |
| Informe | Acciones con responsable y fecha; artefactos separados | Acciones vagas | Solo narración | Ninguno |

Un equipo que restablece rápidamente el punto de consigna pero no sabe decir quién lo decidió obtiene un 2 en decisiones. Una cronología cuya fila de las 01:52 se marca con confianza alta pese a la entrada alterada del registro obtiene un 1. El razonamiento intersectorial obtiene un 3 solo si se estima la autonomía del agua acortada, no si solo se menciona.

### Ejercicios — capítulo 30

**EX059 — Gradación de la confianza.** *Objetivo:* justificar el peso de la evidencia. *Entradas:* la cronología resuelta de este laboratorio. *Pasos:* explique la confianza de cada fila y qué evidencia adicional elevaría la fila de las 01:52 a alta. *Evidencia esperada:* explicaciones. *Rúbrica:* 3 = registros del sistema, alta; entrada del registro alterada, media, porque se desconocen la hora y el valor de la entrada original; para elevarla se necesitan los registros de eventos del PLC o controlador, la tendencia del punto de consigna en el historiador y la grabación de la sesión en el lado del proveedor; 2 = parcial; 1 = afirmaciones; 0 = nada.

**EX060 — Plan de mejora.** *Objetivo:* convertir los hallazgos en acciones. *Entradas:* el escenario. *Pasos:* escriba cinco acciones de mejora con responsable, fecha y cómo se verificará su cumplimiento. *Evidencia esperada:* tabla. *Rúbrica:* 3 = p. ej., aprobación y grabación de las sesiones de los proveedores por sesión, alarmas de cambio del punto de consigna con límites, ancla en el sistema de otro equipo, plantilla de estado común a los operadores, ejercicio conjunto con CPN; cada una verificable; 2 = acciones sin verificación; 1 = vago; 0 = nada.

### Síntesis del capítulo

El Laboratorio II combina personas y evidencias: decidir bajo presión de tiempo, reconstruir cronologías a partir de fuentes con confianza graduada, verificar la integridad y razonar entre sectores. Las situaciones más peligrosas suelen surgir de la interacción de dos eventos que, por separado, son manejables.

<!-- cyberabc:chapter-navigation:start ch-30 -->
### Siga estudiando — capítulo 30 de 40

[← Capítulo 29](#ch-29) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 31 →](#ch-31)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-31"></a>

## Capítulo 31 — Infraestructura crítica y seguridad sectorial: casos avanzados

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) analizar casos en los que el daño llegó a través del proceso físico, los sistemas de seguridad o los proveedores compartidos, y no mediante el robo de datos; (2) comparar casos sistemáticamente según la causa, la ruta, la consecuencia, la detección y la recuperación; (3) razonar sobre el riesgo de la cadena de suministro y de concentración entre sectores; y (4) extraer lecciones defendibles y acotadas para un operador. Se apoya en el capítulo 20 y en los capítulos 21–30, y prepara el proyecto comparativo (capítulo 34).

### 31.1 Más allá del titular

El análisis avanzado de casos no pregunta «¿qué ocurrió?», sino «¿qué supuesto falló y está presente aquí ese supuesto?». Tres familias de casos ilustran supuestos en los que se apoyan los servicios críticos. **Manipulación del proceso diseñada para pasar inadvertida.** El análisis de Langner sobre Stuxnet describe un malware que manipulaba controladores industriales que accionaban centrifugadoras mientras mostraba a los operadores valores de apariencia normal ([Langner, 2011](https://doi.org/10.1109/MSP.2011.67)). *Supuesto fallido:* lo que ve el operador es lo que hace el proceso. *Lección trasladable:* rutas de medición independientes para las variables críticas y límites físicos que no dependan del controlador.

**Ataques a la capa de seguridad funcional.** El análisis de TRITON/HatMan describe un malware dirigido contra un controlador de un sistema instrumentado de seguridad ([CISA MAR-17-352-01](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf)). *Supuesto fallido:* el sistema de seguridad funcional es independiente de las redes a las que puede llegar un atacante. *Lección:* imponer físicamente los modos de programación del SIS (interruptores de llave), separar las redes del SIS y tratar las estaciones de ingeniería del SIS como los activos más sensibles.

**Falla de una dependencia compartida.** La actualización de seguridad defectuosa de julio de 2024, que bloqueó unos 8,5 millones de dispositivos Windows ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)), y la parada de precaución de 2021 tras un ransomware en la red de TI de una empresa de oleoductos ([CISA AA21-131A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a)) muestran daños que llegan a través de las dependencias y no del sistema de control. *Supuesto fallido:* nuestro riesgo está acotado por nuestros propios sistemas. *Lección:* cartografiar la concentración (muchos servicios que dependen de un mismo producto, proveedor o región de la nube), escalonar las actualizaciones y planificar una operación degradada que no necesite la TI de negocio.

### 31.2 Cadenas de suministro

Todo operador ejecuta software y hardware construidos por otros, a menudo a través de largas cadenas de componentes. Entre las medidas públicas figuran las **listas de materiales de software** (SBOM), que enumeran los componentes ([CISA SBOM](https://www.cisa.gov/sbom)), los marcos para la integridad de la compilación como SLSA ([SLSA](https://slsa.dev/)), las prácticas de desarrollo seguro para los proveedores ([NIST SSDF, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)) y las expectativas de «seguridad desde el diseño» para los fabricantes ([CISA Secure by Design](https://www.cisa.gov/securebydesign)). En el nivel de grado, las palancas del operador son principalmente contractuales y arquitectónicas: exigir SBOM y divulgación de vulnerabilidades, probar las actualizaciones antes de desplegarlas, escalonar los despliegues, conservar la capacidad de revertirlos y evitar que la falla de un solo proveedor detenga a la vez varias funciones críticas.

### 31.3 Un marco de comparación

| Dimensión | Stuxnet (según el análisis) | TRITON/HatMan | Interrupción por la actualización de 2024 |
|---|---|---|---|
| Causa | Deliberada, dirigida | Deliberada, dirigida | Accidental |
| Ruta | Hacia los controladores | Hacia el controlador de seguridad | A través de un producto compartido |
| Consecuencia | Daño físico oculto a la vista | Posible pérdida de la protección | Pérdida masiva de disponibilidad |
| Supuesto fallido | Vista = realidad | Independencia del SIS | Riesgo acotado por los propios sistemas |
| Control genérico | Medición independiente, límites físicos | Controles físicos del SIS, segregación | Actualizaciones escalonadas, cartografía de la concentración, modos degradados |

Lea primero la fila «Supuesto fallido»; es la parte trasladable. Cada control genérico aborda ese supuesto y no la técnica concreta.

### 31.4 Ejemplo resuelto: concentración en Calder (sintético)

**Este caso es sintético.** La CRP encuesta a sus miembros: el CVH, el CEDC y Calder Mutual usan el mismo producto de seguridad de *endpoint*, configurado con actualizaciones automáticas; el CEDC y CT usan la misma región de la nube para el CAD y la programación; CW y CPN usan el mismo integrador de TO, con acceso remoto a ambos. Eventos únicos que podrían afectar a la vez a varios sectores: una actualización defectuosa del *endpoint* (hospital, despacho y banco simultáneamente); una caída de la región de la nube (despacho y transporte); un compromiso del integrador (agua y electricidad). Recomendaciones: escalonar las actualizaciones del *endpoint* (primero un pequeño grupo canario, las consolas críticas de despacho al final); confirmar que el respaldo de papel y radio del CEDC no necesita la nube; exigir aprobación por sesión y credenciales separadas para el integrador en cada operador, e incluirlo en el ejercicio conjunto. La cuestión no es que estos proveedores sean malos; es que el riesgo del condado es compartido y debe analizarse de forma conjunta.

### 31.5 Errores comunes y límites

- Extraer lecciones de detalles llamativos pero sin fuentes.
- Tratar las operaciones estatales dirigidas como la amenaza típica para todo operador.
- Ignorar las fallas accidentales de dependencias compartidas porque no interviene ningún adversario.
- Enseñar técnicas en lugar de supuestos fallidos.

El ejemplo de concentración de Calder los evita: no usa ningún detalle técnico, trata una actualización accidental del *endpoint* con la misma seriedad que un compromiso del integrador y no presupone un actor estatal. Repetir afirmaciones sin fuentes sobre el origen de Stuxnet sería el primer error. El cuarto error convertiría una lección de TRITON en una descripción de cómo llegar a un controlador de seguridad.

### Ejercicios — capítulo 31

**EX061 — Encuentre el supuesto.** *Objetivo:* abstraer un caso. *Entradas:* el caso de Ucrania 2015 (capítulo 20). *Pasos:* indique dos supuestos que fallaron y uno que se mantuvo y ayudó a la recuperación, con respaldo de las fuentes. *Evidencia esperada:* tres supuestos. *Rúbrica:* 3 = p. ej., el acceso remoto y las estaciones de los operadores eran de confianza (falló), los centros de atención telefónica seguirían accesibles (falló), la operación manual era posible (se mantuvo), cada uno vinculado a la alerta de CISA; 2 = dos; 1 = uno; 0 = nada.

**EX062 — Mapa de concentración.** *Objetivo:* identificar las dependencias compartidas. *Entradas:* la encuesta de concentración de Calder del ejemplo resuelto de este capítulo. *Pasos:* dibuje un mapa bipartito (proveedores ↔ operadores), marque el proveedor con mayor alcance y proponga una medida por proveedor. *Evidencia esperada:* mapa y medidas. *Rúbrica:* 3 = el producto de *endpoint* alcanza a tres operadores de tres sectores (el mayor), medidas específicas (actualizaciones escalonadas, independencia de los respaldos, controles sobre el integrador); 2 = mapa sin medidas; 1 = lista; 0 = nada.

### Síntesis del capítulo

Los casos avanzados enseñan a través de los supuestos fallidos: lo que ven los operadores es real, los sistemas de seguridad son independientes, el riesgo está acotado por nuestros propios sistemas. Compare los casos según la causa, la ruta, la consecuencia y el supuesto; gestione el riesgo de la cadena de suministro y de concentración de forma conjunta entre operadores; y convierta las lecciones en controles genéricos y no en conocimiento de técnicas.

<!-- cyberabc:chapter-navigation:start ch-31 -->
### Siga estudiando — capítulo 31 de 40

[← Capítulo 30](#ch-30) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 32 →](#ch-32)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-32"></a>

## Capítulo 32 — Infraestructura crítica y seguridad sectorial: interfaces interdisciplinarias

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) explicar cómo el derecho y la regulación, la economía, la ingeniería de seguridad funcional, los factores humanos y la comunicación pública dan forma a las decisiones de seguridad en los servicios críticos; (2) traducir un hallazgo técnico para juristas, responsables financieros, clínicos, ingenieros y el público; (3) reconocer cuándo un problema de seguridad es en realidad un problema de incentivos u organizativo; y (4) trabajar entre disciplinas sin sobrepasar su propia competencia. Se apoya en los capítulos 10, 14, 19 y 28–31 y prepara la práctica de campo (capítulo 36) y el proyecto final.

### 32.1 Derecho y regulación

Los servicios críticos están regulados. Ejemplos consultados para este libro: la Directiva NIS2 de la UE establece obligaciones de gestión de riesgos y de notificación de incidentes para las entidades esenciales e importantes ([NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/)); DORA establece requisitos de riesgo de las TIC para las entidades financieras ([DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)); en Norteamérica, las normas de protección de infraestructuras críticas (CIP) de NERC se aplican al sistema eléctrico de gran escala ([NERC CIP](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx)); en el sector del agua de EE. UU., la America's Water Infrastructure Act de 2018 exigió evaluaciones de riesgo y resiliencia y planes de respuesta a emergencias a los sistemas comunitarios de agua por encima de un umbral de tamaño ([EPA, AWIA](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans)). Como profesional de la seguridad, usted necesita saber que existen estas obligaciones, dónde encontrar el texto vigente y cuándo recurrir a la asesoría jurídica, no interpretarlas por su cuenta. El cumplimiento es un mínimo: cumplir una norma no demuestra que el servicio sea resiliente.

### 32.2 Economía e incentivos

Gran parte de la infraestructura está operada por empresas privadas, pero su falla perjudica a personas que no son sus clientes: una **externalidad**. Las inversiones que protegen frente a eventos raros compiten con costes visibles y a corto plazo, y el beneficio (un corte que no se produjo) es invisible. La regulación, los seguros, los requisitos de contratación y la información pública son formas de cambiar los incentivos. Reconocer un problema de incentivos evita un error habitual: proponer un control técnicamente excelente que ningún responsable presupuestario tiene motivos para financiar. El planteamiento de la pérdida esperada y del peor evento creíble del capítulo 1 es el puente hacia un público financiero.

### 32.3 Ingeniería de seguridad funcional y factores humanos

Los ingenieros de seguridad funcional tienen una larga práctica en el análisis de peligros, las capas de protección independientes y la gestión del cambio (capítulos 26 y 28). La seguridad de la información y la seguridad funcional pueden entrar en conflicto (un bloqueo de cuenta que impide actuar a un operador en una emergencia; un parche que invalida una certificación de seguridad funcional) y deben conciliarse de forma conjunta. Los especialistas en factores humanos estudian cómo trabajan realmente las personas: avalanchas de alarmas, fatiga en los turnos de noche, atajos cuando los procedimientos no se ajustan a la realidad. El trabajo de Reason presenta los errores como consecuencias del diseño del sistema ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)). Un control que los operadores no pueden usar bajo estrés acabará eludiéndose (la aceptabilidad psicológica de Saltzer y Schroeder).

### 32.4 Comunicación

Públicos distintos necesitan traducciones distintas del mismo hallazgo. Los **clínicos** necesitan conocer el efecto sobre la atención a los pacientes y qué deben hacer de otra manera. Los **ingenieros** necesitan el mecanismo técnico y las restricciones. **Finanzas** necesita los costes, las pérdidas evitadas y las opciones. Los **juristas** necesitan hechos, fechas y las obligaciones que se activan. **El público** necesita información honesta y oportuna sobre el servicio y sobre lo que debe hacer, sin detalles que ayuden a los atacantes. Los portavoces acordados y las plantillas de mensajes aprobadas de antemano forman parte de la preparación ante incidentes (la inyección del periodista del capítulo 30). El hallazgo sobre el BMS del CVH se traduce así a continuación: una comprobación de la ventilación para el responsable de quirófanos, los detalles de la VLAN y del enclavamiento para mantenimiento de instalaciones, unas 25 000 £ frente a la cancelación de intervenciones para finanzas y una declaración de ausencia de obligaciones para el área jurídica.

### 32.5 Ejemplo resuelto: un hallazgo, cuatro públicos (sintético)

**Este caso es sintético.** Hallazgo: la ventilación de los quirófanos del CVH puede modificarse desde el BMS, que es accesible desde la red corporativa con autenticación solo por contraseña.

- *Responsable de quirófanos:* «Un uso indebido del sistema del edificio podría reducir las renovaciones de aire de los quirófanos. Hasta que lo corrijamos, mantenimiento de instalaciones comprobará las lecturas de ventilación al inicio de cada sesión quirúrgica, y usted debe notificar de inmediato cualquier alarma».
- *Ingeniero de mantenimiento de instalaciones:* «Interfaz de administración del BMS accesible desde la VLAN corporativa; solo contraseña. Propuesta: lista de permitidos limitada a dos estaciones de mantenimiento, MFA, enclavamiento cableado de caudal mínimo de aire».
- *Finanzas:* «Coste de unas 25 000 £, pago único; aborda un escenario cuyo peor resultado creíble es la cancelación de intervenciones quirúrgicas durante varios días. Se adjuntan las alternativas y sus costes».
- *Protección de datos y asesoría jurídica:* «No intervienen datos personales; el hallazgo por sí mismo no activa ninguna obligación de notificación; lo reevaluaremos si se detecta una explotación».

### 32.6 Errores comunes y límites

- Emitir opiniones jurídicas sin asesoría jurídica.
- Proponer controles sin un argumento de financiación.
- Ignorar las consecuencias para la seguridad funcional o clínicas de los controles de seguridad.
- Un mismo mensaje para todos los públicos.

El ejemplo resuelto evita cada uno: el mensaje jurídico dice qué se comprobó y cuándo se reevaluará; el mensaje financiero da un coste y su peor resultado creíble; el mensaje para quirófanos nombra la comprobación clínica; y cuatro públicos reciben cuatro mensajes. Un único correo técnico para todos habría fallado al responsable de quirófanos y a finanzas.

### Ejercicios — capítulo 32

**EX063 — Tradúzcalo para el consejo.** *Objetivo:* comunicar entre disciplinas. *Entradas:* el resultado del Lab 11 (la ruta cibernética aproximadamente duplica la probabilidad de perder la alimentación crítica en el modelo sintético). *Pasos:* escriba una nota de 120 palabras para el consejo del CVH con el hallazgo, la corrección de ingeniería propuesta, el planteamiento de costes y los límites del modelo. *Evidencia esperada:* nota. *Rúbrica:* 3 = lenguaje claro, consecuencia para los pacientes, la corrección restablece la independencia, honestidad sobre los números sintéticos y sobre el comportamiento no aleatorio del adversario; 2 = parcial; 1 = jerga; 0 = nada.

**EX064 — Conflicto entre seguridad funcional y seguridad.** *Objetivo:* conciliar deberes. *Entradas:* una política de bloquear las cuentas de la HMI tras cinco intentos fallidos de inicio de sesión. *Pasos:* explique el riesgo para la seguridad funcional y proponga una alternativa que cumpla el propósito de seguridad. *Evidencia esperada:* explicación y alternativa. *Rúbrica:* 3 = operador bloqueado durante una emergencia; alternativas como una consola con control de acceso físico y supervisión, limitación de tasa sin bloqueo, alertas ante fallos, anulación de emergencia con auditoría; 2 = una; 1 = vago; 0 = nada.

### Síntesis del capítulo

La seguridad en los servicios críticos se sitúa entre el derecho, la economía, la seguridad funcional, los factores humanos y la comunicación. Sepa dónde están las obligaciones y cuándo llamar a la asesoría jurídica, reconozca los problemas de incentivos, concilie de forma conjunta la seguridad funcional y la seguridad, diseñe para personas bajo estrés y traduzca cada hallazgo para el público que debe actuar en consecuencia.

<!-- cyberabc:chapter-navigation:start ch-32 -->
### Siga estudiando — capítulo 32 de 40

[← Capítulo 31](#ch-31) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 33 →](#ch-33)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-33"></a>

## Capítulo 33 — Métodos de investigación II

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) diseñar entrevistas y análisis documentales como métodos cualitativos, incluidos la aprobación ética y el consentimiento; (2) codificar datos cualitativos con un libro de códigos y comprobar el acuerdo entre codificadores; (3) hacer reproducible un análisis cuantitativo; y (4) combinar evidencia cualitativa y cuantitativa en un diseño de métodos mixtos. Se apoya en el capítulo 18 y prepara el proyecto comparativo (capítulo 34) y el proyecto final (capítulos 35–40).

### 33.1 Métodos cualitativos

Muchas preguntas importantes de la seguridad de los sectores críticos tratan sobre personas y organizaciones: por qué los operadores eluden un control, cómo se tomaron las decisiones durante un incidente, qué creen los profesionales que funciona. Las **entrevistas semiestructuradas** siguen una guía de preguntas abiertas y permiten repreguntar. El **análisis documental** examina planes, informes y políticas. Ambos requieren la **aprobación ética** de su institución cuando implican a personas, el **consentimiento informado** (los participantes conocen el propósito, qué se registrará y cómo se almacenará, y pueden retirarse) y la protección de los participantes y de sus organizaciones: en su tesis no debe aparecer ningún detalle que identifique a una persona o exponga una vulnerabilidad de un operador real. Las notas de entrevistas sobre debilidades de seguridad son datos sensibles; almacénelas cifradas y elimínelas según el calendario previsto (capítulo 14).

### 33.2 Codificación y acuerdo

La **codificación** asigna etiquetas a los fragmentos: «respaldo en papel», «dependencia de un proveedor», «responsable de la decisión poco claro». Un **libro de códigos** define cada código con reglas de inclusión y exclusión y un ejemplo. Para comprobar la **fiabilidad**, dos personas codifican la misma muestra de forma independiente y miden el acuerdo. El porcentaje de acuerdo bruto sobrestima la fiabilidad porque parte del acuerdo se produce por azar; el **kappa de Cohen** lo corrige: $\kappa = (p_o - p_e)/(1 - p_e)$, donde $p_o$ es el acuerdo observado y $p_e$ el acuerdo esperado por azar a partir de las frecuencias de etiquetado de cada codificador. Los desacuerdos no son fracasos; discutirlos afina el libro de códigos.

### 33.3 Análisis cuantitativo reproducible

Un análisis reproducible mantiene inalterados los datos brutos, realiza todas las transformaciones mediante scripts, registra las versiones y las semillas aleatorias y produce cada número del informe a partir del código ([Sandve et al., 2013](https://doi.org/10.1371/journal.pcbi.1003285)). Los laboratorios de este libro siguen estas reglas: semillas fijas, solo la biblioteca estándar, salidas impresas reproducidas en el texto. Si se usa una simulación o un modelo, indique cómo se contrastó con la realidad: la verificación y validación de modelos de simulación es una disciplina en sí misma ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20)).

### 33.4 Métodos mixtos

La evidencia cuantitativa dice **cuánto**; la evidencia cualitativa dice **cómo y por qué**. Un diseño de métodos mixtos podría contar, en 30 informes públicos de incidentes, cuántos mencionan un paso a la operación manual como respaldo (cuantitativo) y después entrevistar a cuatro operadores sobre qué hace que funcione el respaldo manual (cualitativo). La combinación es más sólida que cualquiera de las dos partes por separado, siempre que cada parte se haga correctamente y que la integración (cómo informa una a la otra) sea explícita. En el diseño de los 30 informes, el vínculo se fija antes de la recogida: cualquier condición del respaldo que aparezca en al menos cinco informes se convierte en una pregunta de la entrevista.

En el ejemplo de los 30 informes, el recuento le dice con qué frecuencia mencionan los informes el respaldo manual, y las entrevistas explican por qué el respaldo falla a veces, por ejemplo porque el personal no lo ha practicado. Integración significa que la guía de entrevista pregunta por las condiciones que reveló el recuento.

### 33.5 Ejemplo resuelto: codificación de informes de incidentes (datos sintéticos)

**Los datos son sintéticos.** Dos estudiantes codifican 20 extractos de informes de incidentes según la presencia del código «responsable de la decisión poco claro». Coinciden en 16 de 20 ($p_o = 0.80$). El estudiante A aplicó el código a 8 extractos; el estudiante B, a 6. Acuerdo por azar: ambos «sí» $= (8/20)(6/20) = 0.12$; ambos «no» $= (12/20)(14/20) = 0.42$; $p_e = 0.54$. Kappa $= (0.80 - 0.54)/(1 - 0.54) = 0.26/0.46 \approx 0.57$: acuerdo moderado. Los estudiantes revisan los cuatro desacuerdos, descubren que uno codificó «decisión retrasada» como «responsable poco claro» incluso cuando el responsable estaba nombrado, y precisan la definición: «se aplica solo cuando el informe afirma o muestra que los participantes no sabían quién tenía la decisión».

### 33.6 Errores comunes y límites

- Entrevistar a profesionales sin aprobación ética ni consentimiento.
- Publicar detalles identificables de las debilidades de operadores reales.
- Presentar el porcentaje de acuerdo como fiabilidad.
- Pasos del análisis hechos a mano y no registrados.
- «Métodos mixtos» que son dos estudios separados que nunca se integran.

En el ejemplo de codificación, informar de un 80 % de acuerdo en lugar de un kappa de 0,57 sería el tercer error. Entrevistar a ingenieros de la CRP sobre el acceso remoto sin consentimiento ni aprobación sería el primero, y citar la pasarela sin parchear de un operador identificado sería el segundo. Una hoja de cálculo editada a mano sin registro sería el cuarto.

### Ejercicios — capítulo 33

**EX065 — Calcule kappa.** *Objetivo:* medir la fiabilidad. *Entradas:* dos codificadores, 40 extractos, coinciden en 34; el codificador A aplicó el código 10 veces y el codificador B, 12. *Pasos:* calcule $p_o$, $p_e$ y $\kappa$, e interprételos. *Evidencia esperada:* cálculos e interpretación. *Rúbrica:* 3 = $p_o = 0.85$; $p_e = 0.25 \times 0.30 + 0.75 \times 0.70 = 0.075 + 0.525 = 0.60$; $\kappa = 0.625$, acuerdo entre sustancial y moderado, con la observación de que las escalas de interpretación son convenciones; 2 = error aritmético; 1 = solo $p_o$; 0 = nada.

**EX066 — Consentimiento y protección.** *Objetivo:* diseñar un trabajo cualitativo ético. *Entradas:* el plan de entrevistar a ingenieros de tres operadores de la CRP sobre sus prácticas de acceso remoto. *Pasos:* escriba la información para el consentimiento (cinco puntos) y tres medidas de protección de datos. *Evidencia esperada:* listas. *Rúbrica:* 3 = propósito, participación voluntaria/retirada, qué se registra, almacenamiento/conservación, cómo se anonimizan los resultados, más cifrado, seudónimos y ningún detalle de vulnerabilidades en los resultados/revisión por la organización anfitriona; 2 = parcial; 1 = genérico; 0 = nada.

### Síntesis del capítulo

Los métodos cualitativos responden al cómo y al porqué; necesitan aprobación ética, consentimiento y protección de los participantes y de las organizaciones. Los libros de códigos y kappa hacen fiable la codificación; los scripts, las semillas y las versiones hacen reproducible el análisis cuantitativo; los métodos mixtos solo valen lo que valga su integración.

<!-- cyberabc:chapter-navigation:start ch-33 -->
### Siga estudiando — capítulo 33 de 40

[← Capítulo 32](#ch-32) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 34 →](#ch-34)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-34"></a>

## Capítulo 34 — Proyecto comparativo

### Resultados de aprendizaje y conexión

Después de este proyecto usted podrá (1) comparar tres o más opciones según criterios explícitos con pesos y evidencias; (2) comprobar la sensibilidad de la clasificación a los pesos; (3) presentar una comparación que un responsable de la decisión pueda cuestionar; y (4) reconocer cuándo una puntuación ponderada oculta una consideración decisiva. Se apoya en los capítulos 1, 15, 23 y 24 y prepara la propuesta del proyecto final (capítulo 35). Es la expresión central del resultado del curso: comparar métodos, evaluar evidencias y diseñar soluciones defendibles.

### 34.1 Comparación multicriterio

Las decisiones sobre servicios críticos implican varios criterios que no comparten unidad: reducción de la consecuencia, carga operativa, coste, plazo de implantación, solidez de la evidencia de que la opción funciona. El **análisis de decisión multicriterio** puntúa cada opción en cada criterio, pondera los criterios y los combina, en el caso más sencillo como una suma ponderada. Su valor reside menos en el número final que en hacer visibles los criterios, las puntuaciones y los pesos para que las personas puedan discutirlos de forma productiva. En la evaluación de los dispositivos sin soporte del proyecto final (capítulo 39), el peso del coste se imprime junto a cada puntuación, y así es como un lector puede ver que la pasarela del proveedor gana cuando ese peso supera 0,45.

### 34.2 Hacerlo con honestidad

Defina cada criterio de modo que más alto sea mejor (invierta los costes y las cargas). Puntúe en una escala anclada («5 = elimina la peor consecuencia creíble; 1 = ningún efecto medible»). Registre la evidencia detrás de cada puntuación (capítulo 15). Fije los pesos *antes* de puntuar, idealmente con las partes interesadas, para evitar ajustar los pesos a una opción favorita. Después realice un **análisis de sensibilidad**: varíe los pesos y vea si cambia la ganadora. Si solo cambia con pesos inverosímiles, la decisión es robusta; si pequeños cambios la invierten, informe de que la decisión depende de un juicio de valor y nómbrelo.

### 34.3 Cuando una puntuación no basta

Algunas consideraciones son **restricciones**, no criterios: una obligación legal, un requisito de seguridad funcional, un nivel mínimo de servicio. Una opción que vulnera una restricción queda excluida, sea cual sea su puntuación. Otras son **vetos** de personas con autoridad (el rechazo de un director clínico a una opción que perturba los quirófanos). Trátelas explícitamente antes de puntuar. Para el CEDC, el requisito del regulador de restablecer el servicio en cuatro horas es una restricción (EX068), que excluye las opciones que no puedan demostrarlo. El veto de un director clínico a una opción que cierra los quirófanos durante una semana se trata del mismo modo.

### 34.4 Ejemplo resuelto y Lab 13 (sintético)

**Este caso es sintético.** La CRP compara tres opciones de resiliencia frente al ransomware para el CEDC con cuatro criterios y pesos de 0,4, 0,2, 0,2 y 0,2.

```python
# Lab 13 - weighted comparison of three options and weight sensitivity (synthetic scores, offline)
CRITERIA = ["consequence reduction", "operational burden (inverted)", "cost (inverted)", "evidence strength"]
W = [0.4, 0.2, 0.2, 0.2]
SCORES = {  # 1-5, higher is better
    "network segmentation project": [5, 2, 2, 4],
    "managed detection service":    [3, 4, 3, 3],
    "offline backups + restore drills": [4, 4, 4, 5],
}
def total(s, w): return sum(a * b for a, b in zip(s, w))
for name, s in SCORES.items():
    print(f"{name:33} {total(s, W):.2f}")
print("weight on consequence needed for segmentation to win:")
for wc in (0.4, 0.5, 0.6, 0.7, 0.8):
    rest = (1 - wc) / 3
    w = [wc, rest, rest, rest]
    best = max(SCORES, key=lambda k: total(SCORES[k], w))
    print(f"  w_consequence={wc:.1f} -> {best}")
```

Salida esperada:

```text
network segmentation project      3.60
managed detection service         3.20
offline backups + restore drills  4.20
weight on consequence needed for segmentation to win:
  w_consequence=0.4 -> offline backups + restore drills
  w_consequence=0.5 -> offline backups + restore drills
  w_consequence=0.6 -> offline backups + restore drills
  w_consequence=0.7 -> network segmentation project
  w_consequence=0.8 -> network segmentation project
```

Las copias de seguridad con simulacros de restauración ganan con los pesos acordados y siguen por delante hasta que la reducción de la consecuencia representa entre 0,6 y 0,7 del peso total. Por tanto, el informe dice: «Recomendación: copias de seguridad fuera de línea con simulacros de restauración. La recomendación solo se invierte si la asociación otorga a la reducción de la consecuencia más de aproximadamente 0,63 de la decisión (el EX067 deduce el punto de cruce exacto), en cuyo caso se prefiere la segmentación. Las opciones no son excluyentes; la segmentación es la candidata más sólida para el segundo año». Observe lo que las puntuaciones no recogen: las copias de seguridad permiten recuperarse del ransomware, pero no impiden el robo de datos que a menudo lo acompaña, una consideración que debe declararse explícitamente y no esconderse en un número.

### 34.5 Entregable del proyecto

Un informe comparativo de 2500 palabras sobre una pregunta de su elección dentro del caso Calder o sobre un tema público documentado (por ejemplo, tres enfoques del acceso remoto, tres estrategias de copia de seguridad, tres opciones de supervisión): restricciones, criterios con escalas ancladas, evidencia de cada puntuación, pesos fijados de antemano, análisis de sensibilidad, recomendación con condiciones de inversión y límites. Para la comparación de los dispositivos sin soporte del proyecto final (capítulo 39), ese peso es 0,45 en el coste; por debajo gana el aislamiento con supervisión, por encima gana la pasarela del proveedor. Declare la condición de inversión con palabras, como hace el informe del Lab 13: el peso con el que cambiaría la recomendación y el juicio de valor que representa ese peso.

### 34.6 Errores comunes y límites

- Puntuar primero y elegir los pesos después.
- Puntuaciones sin anclar («un 4 porque me parece bien»).
- Ignorar las restricciones y los vetos.
- Presentar un total ponderado como una verdad objetiva.
- Tratar las opciones como mutuamente excluyentes cuando pueden combinarse.

El Lab 13 evita el primero al fijar los pesos en 0,4, 0,2, 0,2 y 0,2 antes de puntuar. El informe también señala que la segmentación y las copias de seguridad pueden combinarse, con lo que evita el quinto error. Una puntuación de 4 en solidez de la evidencia necesita los registros de los simulacros que la respaldan; sin ellos, es el segundo error. Presentar 4,20 como una prueba sería el cuarto.

### Ejercicios — capítulo 34

**EX067 — Encuentre el punto de cruce.** *Objetivo:* localizar el punto de inversión. *Entradas:* el Lab 13. *Pasos:* calcule el peso exacto de la consecuencia con el que la segmentación y las copias de seguridad empatan, usando la regla de reparto igualitario para los demás pesos. *Evidencia esperada:* deducción y valor. *Rúbrica:* 3 = segmentación $5w + (2+2+4)(1-w)/3$, copias de seguridad $4w + (4+4+5)(1-w)/3$; empate cuando $w = 5(1-w)/3$, por lo que $w = 5/8 = 0.625$; 2 = búsqueda numérica hasta 0,62–0,63; 1 = solo el intervalo 0,6–0,7; 0 = nada.

**EX068 — Añada una restricción.** *Objetivo:* tratar un requisito no compensatorio. *Entradas:* el regulador del CEDC exige un restablecimiento demostrado en 4 horas. *Pasos:* explique cómo cambia esto el análisis y qué evidencia debe aportar cada opción. *Evidencia esperada:* explicación. *Rúbrica:* 3 = tratado como restricción y no como criterio; solo cumplen las opciones que demuestran el restablecimiento (las copias de seguridad con simulacros, directamente; la segmentación y la detección no restablecen, por lo que deben combinarse con una capacidad de recuperación); 2 = tratado como un peso elevado; 1 = ignorado; 0 = nada.

### Síntesis del capítulo

La comparación es la habilidad central del grado: criterios explícitos, puntuaciones ancladas, evidencias, pesos fijados de antemano, análisis de sensibilidad y condiciones de inversión declaradas. Las restricciones y los vetos van antes de puntuar, y un total ponderado es un argumento estructurado, no un veredicto.

<!-- cyberabc:chapter-navigation:start ch-34 -->
### Siga estudiando — capítulo 34 de 40

[← Capítulo 33](#ch-33) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 35 →](../../en/book/MANUSCRIPT.md#ch-35)

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

**EX009.** Historiales de pacientes: C > I > A (la divulgación daña a los pacientes e infringe la ley; la integridad también importa para la atención). Dosificación de cloro: I/seguridad funcional > A > C (un punto de consigna erróneo envenena el agua o la desinfecta de forma insuficiente). Autorización de tarjetas: I ≈ A > C (pagos fraudulentos o no disponibles; la confidencialidad de los datos de tarjetas también está regulada: acepte una C alta si está razonada). Grabaciones de llamadas: C ≈ I > A (contenido personal sensible; integridad probatoria; la disponibilidad se necesita para la revisión, pero no en tiempo real).

**EX010.** «El activo es el servicio de despacho del CEDC. Un cable cortado por obras viales es una amenaza; la única ruta de cable es una vulnerabilidad; el impacto sería la pérdida de conectividad del despacho, lo que retrasaría la respuesta a emergencias».

**EX011.** $C \cap U$ = {INF-02, IMG-01, IMG-02, ADM-02}. $(C\cap U)\cap K$ = {IMG-01, ADM-02}. $U \setminus C$ = {LAB-01}. Actúe primero sobre {IMG-01, ADM-02}: sin soporte, en la red clínica y con un defecto con explotación conocida. ADM-02 es además el más barato de corregir.

**EX012.** La alcanzabilidad trata cada arista como «falla si falla el proveedor» (AND sobre todos los proveedores). Con una alternativa satelital, el despacho solo falla si fallan **a la vez** la central y el enlace satelital (OR sobre los proveedores). Cambio de modelado: marque cada nodo como necesitado de **todas** sus entradas o de **una cualquiera** de ellas, y propague la falla en consecuencia (un grafo de dependencias AND/OR, como los que se usan en los árboles de fallas, capítulo 28).

**EX013.** RDP corporativo→control: benigna, un atajo no documentado de un ingeniero; maliciosa, un intruso que pivota desde un PC víctima de phishing; se distinguen por las solicitudes de cambio, el usuario con sesión iniciada en 10.1.4.80, los registros de autenticación de 10.20.0.5 y si la sesión siguió a una alerta de phishing. Control→internet: benigna, la comprobación de actualizaciones del software de un fabricante; maliciosa, mando y control o exfiltración de datos; se distinguen por la titularidad del destino, el proceso que realiza la conexión, el volumen y la periodicidad. Inicio de Modbus campo→control: benigna, un dispositivo mal configurado tras un mantenimiento; maliciosa, un dispositivo de campo comprometido que sondea; se distinguen por la configuración del dispositivo frente a su línea base, los registros de mantenimiento y los códigos de función usados.

**EX014.** (1) Reglas por equipo: permitir solo que el recolector 10.5.0.11 llegue solo al servidor SCADA 10.20.0.5 en el 4840, en lugar de cualquier equipo de la DMZ a cualquier equipo de control; se impone en el cortafuegos y se comprueba con los registros de flujos. (2) Restringir Modbus a los códigos de función de lectura desde el servidor SCADA, salvo para registros de escritura designados, mediante un cortafuegos que entienda los protocolos industriales; se comprueba revisando los registros de escrituras rechazadas. Otros refinamientos válidos: transferencia unidireccional para el historiador y reglas por franja horaria para el acceso de ingeniería.

**EX015.** (1) `"nan"` se acepta porque toda comparación con NaN es falsa. (2) `"abc"` (o `""`) lanza `ValueError`, lo que bloquea a quien llama o lo deja en un estado indefinido. (3) Si `current` es NaN (por ejemplo, por una lectura fallida del sensor), `abs(x - current) > 0.5` es falsa para cualquier `x`, de modo que cualquier punto de consigna dentro de rango supera la comprobación del paso. `"inf"` se rechaza en la comprobación de rango, pero solo porque es mayor que 4,5, lo que es suerte, no diseño.

**EX016.** Bomba de dosificación de cloro: conservar el último punto de consigna bueno, generar una alarma para el operador y no moverse hacia el máximo; el responsable del proceso (el responsable de calidad del agua) decide este comportamiento ante la falla. Válvula de entrada de agua bruta: conservar la última posición buena y generar una alarma; operaciones decide si se necesita una posición de respaldo para proteger la capacidad de tratamiento. Registro en ambos casos: marca de tiempo, fuente (usuario o estación), entrada bruta, valor analizado si lo hay, regla que falló, valor actual y acción realizada.

**EX017.** `SELECT a.site, COUNT(*) FROM asset a JOIN advisory v ON a.product = v.product WHERE vlt(a.version, v.fixed_in) GROUP BY a.site;` → Head office 1; Substation North 1.

**EX018.** La ordenación como texto da "critical" < "high" < "low" < "medium", de modo que "low" queda antes que "medium", lo cual es erróneo. Correcciones: almacenar un `severity_rank` numérico (critical 4, high 3, medium 2, low 1) y ordenar por él; u ordenar con `CASE severity WHEN 'critical' THEN 4 ... END`, o combinar con una tabla de consulta.

**EX019.** Condiciones de parada y llamadas: (1) cualquier alarma inesperada del proceso o anomalía notificada por un operador: supervisor de la sala de control; (2) cualquier cambio de comportamiento de un dispositivo que coincida con la conexión del equipo de captura: supervisor e ingeniero de TO; (3) observar tráfico de sistemas de seguridad funcional o redes fuera del alcance: detener la captura y avisar al responsable de seguridad de TO; (4) un operador o el supervisor piden parar: obedecer de inmediato; (5) descubrimiento de datos personales o credenciales en claro: parar, proteger los archivos y avisar al delegado de protección de datos y al responsable de seguridad de TO.

**EX020.** Partes interesadas: pacientes con ventilación, personal clínico, ingeniería clínica, seguridad, dirección del hospital, fabricante. Daños de parchear todo ahora: dispositivos no disponibles durante el pico de demanda, posibles fallas de la actualización. Daños de no parchear: exposición a una explotación que provoque un mal funcionamiento del dispositivo. Alternativas: parchear por lotes a medida que los dispositivos dejan de usarse; aislar la flota en un segmento de red dedicado con supervisión hasta que esté parcheada; actualización con apoyo del fabricante a pie de cama durante períodos de baja dependencia. El registro de la decisión nombra al director clínico y al responsable de seguridad como responsables conjuntos del riesgo, y registra la justificación, los controles provisionales y una fecha de finalización.

**EX021.** Explotable tal como está desplegado: sí, de forma remota desde la red corporativa. Explotación conocida: suponer que se desconoce; comprobarlo. Qué controla: la ventilación de los quirófanos, de consecuencia alta. Controles compensatorios: restringir ya el acceso a la interfaz a dos estaciones de trabajo de mantenimiento de instalaciones; supervisar. Ventana: programar el reinicio de 30 minutos con mantenimiento de instalaciones y quirófanos cuando los quirófanos no estén en uso (p. ej., una noche de fin de semana), con comprobaciones manuales de la ventilación. Recomendación: restringir ya, parchear en la primera ventana segura, confirmar después.

**EX022.** «Proteger las cuentas» → «Cada inicio de sesión en la HMI es una cuenta individual con nombre; no hay cuentas por defecto del fabricante activadas; se comprueba cada mes exportando la lista de cuentas y comparándola con la plantilla». «Activar el registro» → «Los registros de seguridad y de aplicación se reenvían al servidor central de registros en menos de 5 minutos; se comprueba cada semana confirmando el último evento de cada equipo». «Bloquear el USB» → «El almacenamiento masivo USB está desactivado por directiva en las estaciones de trabajo de operadores; se comprueba con una exportación trimestral de la directiva y una prueba con un dispositivo aprobado».

**EX023.** Probabilidad previa 0,01: $0.95 \times 0.01/(0.95\times0.01 + 0.01\times0.99) \approx 0.490$. Previa 0,001, FPR 0,001: $0.95\times0.001/(0.95\times0.001 + 0.001\times0.999) \approx 0.487$. Una tasa de falsos positivos diez veces menor ayuda tanto como una tasa base diez veces mayor. Los analistas no pueden cambiar la tasa base, pero sí reducir la FPR mediante el ajuste, el enriquecimiento con contexto y las listas de permitidos: la palanca práctica.

**EX024.** Independientes: $0.05^2 = 0.0025$. Con causa común: ≈ $0.02 + 0.0025 = 0.0225$, unas nueve veces peor. Remedio: suministros de combustible separados o análisis y filtrado del combustible, modelos de generador o sistemas de arranque distintos, y pruebas de carga periódicas.

**EX025.** Roles: operador de llamadas (crear incidentes, consultar el CAD); despachador (asignar unidades, actualizar incidentes); supervisor (anular, reasignar, consultar informes); administrador del CAD (configurar el sistema, gestionar cuentas; sin despacho); soporte del fabricante (acceso de tiempo limitado, aprobado por sesión, al entorno de pruebas por defecto). Pares tóxicos: administrador del CAD + administrador del registro de auditoría (podría ocultar sus propios cambios); soporte del fabricante + acceso permanente a producción; despachador + administrador del CAD (podría alterar las reglas y actuar según ellas sin ser visto).

**EX026.** Añada fechas `approved` a cada tupla; señale si `roles & PRIV` y `(TODAY - approved).days > 180`. Con, por ejemplo, *dev* aprobado el 2025-11-01 (334 días) y *chloe* aprobada el 2026-07-01 (92 días), la salida añade «re-approval overdue 334 d» solo a *dev*. La prueba debe mostrar una cuenta privilegiada señalada y otra no señalada.

**EX027.** Diseño minimizado: registrar el ID del miembro del personal, el identificador de la historia clínica del paciente (no el nombre ni el diagnóstico), la estación de trabajo, la marca de tiempo y el tipo de acceso; conservar 2 años (o el plazo que fije la política del hospital), con acceso restringido al responsable de privacidad y a dos auditores con nombre; finalidad declarada como detección de accesos inapropiados; personal informado mediante la política y un aviso al iniciar sesión; reidentificación del paciente solo en investigaciones confirmadas.

**EX028.** Riesgos: en los códigos postales pequeños, un tipo de inmueble único (p. ej., la única casa unifamiliar aislada) identifica un hogar; los patrones horarios revelan la ocupación, las rutinas y las ausencias. Mitigaciones: publicar solo agregados sobre un número mínimo de contadores (p. ej., ≥ 10), reducir el detalle temporal (diario) o de ubicación; facilitar los datos detallados solo con acuerdos de acceso a investigadores aprobados.

**EX029.** Diagrama (2025): documento, producido por el equipo, de hace un año, no independiente; solo muestra la intención del diseño. Informe de la prueba de conmutación (14 min): demostración, de operaciones, del año pasado, no independiente; evidencia real de que la conmutación *puede* funcionar. Nota del auditor: independiente, reciente; muestra que la prueba se anunció, de modo que el personal estaba preparado y las condiciones eran favorables. Conclusión: hay evidencia de que la conmutación puede cumplir los 15 minutos en condiciones preparadas; no de que lo haría durante una falla no anunciada y con carga. Pida una prueba no anunciada u observada de forma independiente, con la carga registrada.

**EX030.** Métrica: «proporción de cuentas privilegiadas y de acceso remoto que usan autenticación resistente al phishing», medida cada mes desde el sistema de identidades como (cuentas con autenticadores resistentes al phishing) / (todas las cuentas privilegiadas y de acceso remoto), informando el denominador y las exclusiones. Riesgo de manipulación: reclasificar cuentas como no privilegiadas para reducir el denominador, mitigado con una definición independiente de privilegio. (También es aceptable una tasa de notificación en simulaciones autorizadas, con manipulación mediante simulaciones predecibles).

**EX031.** Mínimo privilegio: los usuarios remotos llegan a toda la red de control; valores predeterminados a prueba de fallos: cuentas de fabricantes activadas de forma permanente; mediación completa: no hay comprobación por sesión de quién se conecta ni por qué; separación de privilegios: una contraseña por sí sola da acceso, sin segundo factor ni aprobación del operador; mínimo mecanismo común: una sola pasarela compartida por todos los usuarios y fabricantes, directamente hacia el control.

**EX032.** El compromiso de una cuenta o un servidor desactiva a la vez las reglas del cortafuegos, la protección de endpoints y las copias de seguridad: las tres «capas» comparten un único mecanismo. Cambios: niveles administrativos y credenciales (y equipos de gestión) separados para los sistemas de red, de endpoints y de copias, con MFA resistente al phishing; mantener al menos una copia fuera de línea o inmutable y gestionada fuera del dominio.

**EX033.** (a) Firmas digitales: cualquiera puede verificar, solo el fabricante puede firmar. (b) MAC con números de secuencia (o un canal con autenticación mutua como TLS, donde los dispositivos lo admitan): autenticidad, integridad y frescura. (c) Cifrado simétrico del disco con la clave protegida por hardware y por la autenticación del usuario. (d) Cadena de hashes con un ancla custodiada externamente (o entradas de registro firmadas).

**EX034.** Un administrador con acceso al registro y al ancla edita una entrada, recalcula todas las cabezas siguientes y sobrescribe el ancla con la nueva cabeza; la verificación entonces se supera. Prevención: custodiar el ancla en un sistema administrado por otro equipo con almacenamiento de solo anexado; publicar o refrendar periódicamente las cabezas con un servicio de sellado de tiempo de confianza; alertar ante cualquier reescritura del ancla.

**EX035.** Ejemplo: «Entre los operadores de distribución eléctrica de [un país] que publicaron informes de incidentes o informes anuales entre 2020 y 2025, ¿con qué frecuencia se mencionan incidentes iniciados por phishing y qué mitigaciones describen los informes?»: descriptiva con un elemento comparativo (las mitigaciones), con evidencia procedente de informes públicos. Otra opción es una pregunta comparativa sobre dos enfoques de autenticación resistente al phishing en un laboratorio.

**EX036.** De constructo: los «incidentes notificados» miden la notificación y la detección, no los ataques. Interna: los hospitales que compran X también pueden tener presupuestos mayores, más personal o una exposición distinta (confusión); selección: los compradores difieren de forma sistemática. Externa: los hallazgos de los hospitales estudiados pueden no ser trasladables. Fiabilidad: definiciones distintas de «incidente de ransomware» entre hospitales.

**EX037.** Funciones: «prestar servicios de pago» (autorización de tarjetas, transferencias) y «dar acceso al efectivo». Dependencias: electricidad, telecomunicaciones (centrales, operadores), sistemas nacionales de pago y compensación, redes de tarjetas, proveedores de nube, personal. Cronología del daño: las fallas en los pagos con tarjeta hacen daño en horas (compras de combustible y alimentos); los pagos de salarios y prestaciones, en días; la pérdida de acceso al efectivo agrava el daño si los pagos con tarjeta también están caídos.

**EX038.** Riesgo: «¿qué escenarios de la planta son más probables y dañinos?»; puede pasar por alto cascadas nuevas o la adaptación del adversario. Resiliencia: «¿cuánto tiempo puede la planta suministrar agua segura en modos degradados y con qué rapidez se recupera?»; puede infravalorar la prevención rentable. Sistemas: «¿qué acciones de control de operadores, software y procedimientos podrían ser inseguras?»; más difícil de cuantificar y priorizar.

**EX039.** Ejemplo (Oldsmar): CISA afirma que actores no identificados accedieron al sistema SCADA mediante un software de acceso remoto, aumentaron el punto de consigna del hidróxido de sodio y un operador revirtió el cambio. Repetido habitualmente, pero sin respaldo en ese aviso: afirmaciones sobre la identidad del atacante. Redacción para el informe: «En febrero de 2021, CISA informó de un aparente cambio no autorizado en la dosificación química de una planta de agua de Florida; en 2023, un antiguo cargo municipal dijo que probablemente fue un error de un empleado. En cualquier caso, el caso ilustra el riesgo del acceso remoto sin gestionar».

**EX040.** Dependencias: sistemas de venta de billetes e ingresos (puede rechazarse operar sin recaudación), planificación de turnos y programación de tripulaciones, sistemas de información a los pasajeros, gestión del mantenimiento (registros de defectos críticos para la seguridad funcional). Medidas: reglas de operación degradada acordadas de antemano (p. ej., viaje gratuito, turnos en papel) aprobadas por la dirección con antelación; separación y copia de seguridad de los datos operativamente necesarios, como los registros de defectos; ejercicios periódicos de circulación de trenes sin TI de negocio.

**EX041.** (a) Pérdida de la vista histórica: riesgo inmediato bajo, menor análisis de tendencias. (b) Pérdida de vista: peligrosa, los operadores pueden actuar con datos obsoletos. (c) Manipulación del control: efecto directo en el proceso. (d) Pérdida de protección: máxima gravedad, ha desaparecido la última barrera automática.

**EX042.** Cadena: señalización (establecimiento de itinerarios y detección de trenes) → control y conducción de los trenes → comunicación entre la tripulación y el puesto de control → información a los pasajeros → venta de billetes. Modos degradados: falla de la señalización, autorización manual para circular con velocidad y frecuencia reducidas; falla de la radio, teléfonos fijos en las estaciones y trenes retenidos en los andenes; falla de la información a los pasajeros, avisos del personal y comunicados de servicio reducido; falla de la venta de billetes, viaje gratuito o billetes en papel. Restricciones: menor capacidad, más personal, tiempos de viaje más largos.

**EX043.** Con 48 h de autonomía para los pagos con tarjeta: a las 6 h se pierden 3 servicios (central A, bombas de agua, señalización ferroviaria); a las 30 h se pierden 5 (los pagos con tarjeta sobreviven). Con las autonomías reducidas a la mitad, a las 6 h se pierden 5 servicios: central telefónica A (2 h), bombas de agua, almacenamiento de agua tratada (5 h), pagos con tarjeta (2 h) y señalización ferroviaria (1 h). Recomendación: trasladar los pagos con tarjeta a la central B o añadir un generador en la central A, y sustituir las autonomías basadas en cifras de diseño por valores probados, ya que el caso pesimista pierde el almacenamiento de agua antes de 6 h.

**EX044.** Contrato de suministro de combustible y ruta de entrega (evidencia: contrato, prueba de entrega durante un ejercicio); personal para operarlo y reabastecerlo (evidencia: cuadrante de turnos y registros de formación); fiabilidad del arranque y de la carga del generador (evidencia: registros de pruebas mensuales bajo carga); aparamenta/conmutador de transferencia y refrigeración (evidencia: registros de mantenimiento, prueba de la transferencia automática).

**EX045.** Ambos puntúan 10. La igualdad de puntuación oculta que A es frecuente y menor, mientras que B es raro y grave (cancelación de intervenciones quirúrgicas, daño a pacientes), y que las etiquetas ordinales no pueden multiplicarse de forma significativa. Presente una columna de peor consecuencia creíble e intervalos cuantitativos aproximados (frecuencia anual, duración de la interrupción, daño), o trate B mediante un análisis centrado primero en las consecuencias.

**EX046.** Consecuencia: «transferencias fraudulentas de alto valor liberadas» (o «pagos no disponibles > 4 h el día de pago de las nóminas»). Rutas: credenciales de operador comprometidas; una persona interna que crea y aprueba mediante una combinación tóxica de roles (Lab 7); un cambio malicioso en las reglas del conmutador de pagos; la carga por error de un archivo masivo. Ingeniería: límites estrictos por transacción y diarios aplicados en el conmutador, confirmación fuera de banda para las transferencias por encima de un umbral. Procedimental: aprobación por dos personas con roles separados.

**EX047.** Copias de seguridad fuera de línea: correctivo, técnico. Aprobación por dos personas: preventivo, procedimental. Analizador de cloro en la salida que dispara una válvula: preventivo (acota la consecuencia), de ingeniería. Alerta del SIEM ante nuevas cuentas de administrador: detectivo, técnico. Interruptor de llave para la programación del PLC: preventivo, físico.

**EX048.** Fila: «Ransomware en el servidor del BMS»; preventivo: lista de permitidos de aplicaciones, acceso de administración restringido, segmentación respecto de la red corporativa; detectivo: supervisión del servidor del BMS y de las copias de seguridad; correctivo: restauración probada del servidor del BMS y de las configuraciones, control manual local del tratamiento de aire. Mejora más valiosa: una restauración probada junto con un procedimiento de control local ensayado, porque el control local mantiene seguros los quirófanos sea cual sea la causa de la pérdida del BMS.

**EX049.** Prioridad 2 (confianza: media): investigar y cerrar el flujo RDP corporativo→control y el flujo control→internet de CW (Lab 4); eluden la DMZ y la ruta de consecuencias conduce al control del tratamiento del agua; responsables: seguridad de TO de CW (investigar esta semana), equipo de red de CW (reglas). Prioridad 3 (confianza: alta): deshabilitar la cuenta de la persona dada de baja, eliminar las combinaciones tóxicas y pasar el acceso de los proveedores a aprobación por sesión (Lab 7); son rutas directas hacia acciones de control no autorizadas y fraude en los pagos; responsables: propietarios de los sistemas, en el plazo de una semana. El aislamiento de los dispositivos clínicos sin soporte (Lab 2) es una tercera prioridad alternativa aceptable si se acompaña de razonamiento sobre las consecuencias.

**EX050.** Declaración modelo: «Volví a ejecutar los laboratorios 2, 4, 5 y 7 del apéndice con Python 3.13. Los *hashes* de lab02, lab04 y lab07 coincidieron; el de lab05 no, porque el autor había añadido una consulta LEFT JOIN, documentada en sus notas de cambios. Todas las salidas impresas coincidieron con el apéndice, incluida la salida de la consulta adicional. La sección de hallazgos es reproducible».

**EX051.** S: un equipo no autorizado suplanta al colector; autenticación mutua con certificados, reglas a nivel de equipo. T: valores alterados en tránsito; sesión OPC UA autenticada y con protección de integridad. R: el colector niega haber realizado consultas; registro en el lado del SCADA con sincronización horaria. I: el colector expone más etiquetas de las necesarias; cuenta de solo lectura limitada a las etiquetas requeridas. D: un sondeo excesivo sobrecarga el servidor SCADA; límites de tasa y supervisión de recursos. E: la cuenta del colector puede escribir; rol de solo lectura, aplicado en el lado del servidor.

**EX052.** Objetivos: (1) decidir en 30 minutos si se pasa a la administración de pacientes en papel; (2) realizar la evaluación de protección de datos y decidir sobre la notificación dentro del plazo del plan. Participantes: directivo de guardia, responsable del servicio de urgencias, guardia de TI, delegado de protección de datos, comunicación, mantenimiento de instalaciones. Inyecciones: 23:10 nota de rescate en las pantallas de administración; 23:40 urgencias no puede ver el estado de las camas; 00:30 evidencia de que se copiaron datos de pacientes al exterior; 01:30 consulta de un periodista. Registrar: horas de las decisiones, responsables de las decisiones, información utilizada, desviaciones respecto del plan.

**EX053.** Verificación: en una ventana autorizada, desde un equipo de prueba en la red corporativa, intente conexiones a cada dirección de la zona de control en una lista definida de puertos; la afirmación es falsa si alguna conexión tiene éxito. Validación: revise las configuraciones y los registros de flujos en busca de rutas alternativas (equipos con doble conexión, pasarelas de acceso remoto, puentes inalámbricos, módems de proveedores); la afirmación es falsa si existe alguna ruta de la red corporativa a la de control. Autorización: reglas de enfrentamiento (RoE) por escrito de operaciones y seguridad de CW, con condiciones de parada.

**EX054.** Umbral 0,7: errores = FP 2 + FN 7 = 9; exactitud = 5016/5025 ≈ 0,9982. Sin alertar nunca: exactitud = 5000/5025 ≈ 0,9950. Ambos parecen excelentes porque el 99,5 % de los eventos son benignos; la exactitud premia ignorar la clase rara. Informe de la precisión y la exhaustividad (0,90/0,72 frente a indefinida/0).

**EX055.** Con la ruta del BMS que ahora requiere un corte de la red: falla del respaldo = $1 - 0.98 \times 0.995 \times 0.99 \times 0.998 \approx 0.03658$; evento superior = $0.05 \times 0.03658 \approx 0.001829$, aproximadamente la mitad del 0,003729 anterior y solo ligeramente por encima del 0,001733 del caso solo físico. La ruta cibernética necesita ahora un corte de la red coincidente, lo que restablece la estructura de dos eventos; un adversario capaz de provocar también un corte de la red sigue siendo un riesgo residual.

**EX056.** La bomba dosificadora funciona al máximo: sobredosificación, agua insegura; detectado por la alarma de valor alto del analizador de salida; límite de caudal cableado, disparo por el analizador. La bomba se detiene: desinfección insuficiente; alarma de valor bajo del analizador, señal de bomba en marcha; bomba de servicio/reserva. El analizador lee bajo (deriva): el controlador aumenta la dosificación; comparación con una muestra manual o un segundo analizador; programa de calibración. El analizador está congelado: no responde a los cambios reales; alarma de «valor obsoleto» ante una lectura invariable; comprobaciones de mantenimiento.

**EX057.** Modelo: «De los 15 incidentes compartidos por los miembros de la CRP, la mitad se detectaron en 4 horas; el percentil 90 fue de unas 56 horas; un caso tardó 240 horas. La recuperación llevó una mediana de 8 horas (percentil 90 de unas 38 horas). El tiempo medio de detección (27 h) está distorsionado por el único caso más largo. Los registros son pocos, están depurados y dependen de horas de inicio autodeclaradas. ¿Por qué la supervisión no detectó durante diez días el uso indebido de credenciales de 240 horas?».

**EX058.** (1) Operaciones confirma el estado del proceso y que el SCADA y los controladores se comportan con normalidad: supervisor de la sala de control. (2) Preparar la operación local/manual de las estaciones críticas por si el SCADA se ve afectado: director de operaciones. (3) Aislar el historiador de la zona de control (y de los conductos de la DMZ): analista de seguridad con la autorización del supervisor. (4) Preservar la evidencia: imagen de memoria y de disco del historiador, registros del cortafuegos y de flujos: seguridad. (5) Comprobar los servidores SCADA, las estaciones de ingeniería y las configuraciones de los controladores frente a líneas base conocidas como buenas: ingeniero de TO con seguridad. Después, las decisiones de recuperación y notificación.

**EX059.** Los registros del sistema (registros de acceso remoto, control de CPN) tienen confianza alta porque los generan automáticamente sistemas separados. Que los operadores lo advirtieran a las 02:10 tiene confianza alta (registro de turno, varios testigos). El cambio del punto de consigna de las 01:52 tiene confianza media: la cabeza anclada muestra que el registro se alteró, por lo que no puede confiarse ni en la hora ni en el valor registrados. Para elevarla a alta se necesitan el propio registro de eventos del PLC o su pista de auditoría de puntos de consigna, la tendencia del punto de consigna y del nivel del depósito en el historiador, y la grabación de la sesión del proveedor.

**EX060.** Acciones: aprobación por sesión de los proveedores con grabación (seguridad de TO de CW, 1 mes; verificar mediante los registros de sesiones); alarma ante cambios del punto de consigna fuera de límites o de ritmo (ingeniería de CW, 2 meses; verificar con un cambio de prueba); trasladar el ancla del registro a un sistema gestionado por otro equipo (TI de CW, 1 mes; verificar mediante una revisión de accesos); plantilla de estado común a los operadores y lista de contactos (coordinador de la CRP, 6 semanas; verificar en el próximo ejercicio); ejercicio conjunto de CW y CPN sobre eventos combinados de la red eléctrica y del proceso (CRP, 6 meses; verificar mediante el informe posterior a la acción).

**EX061.** Fallaron: que las estaciones de los operadores y el acceso remoto solo podían usarlos el personal legítimo (CISA informa de la operación remota de interruptores); que los centros de atención telefónica seguirían disponibles para los clientes (CISA informa de la interrupción de los centros de atención telefónica a los clientes). Se mantuvo: que la operación manual de las subestaciones era posible; CISA informa de que el suministro se restableció pasando al modo manual.

**EX062.** Mapa: producto de *endpoint* ↔ CVH, CEDC, Calder Mutual (alcance 3, tres sectores: el mayor); región de la nube ↔ CEDC, CT (alcance 2); integrador de TO ↔ CW, CPN (alcance 2). Medidas: actualizaciones escalonadas del *endpoint* con grupos canario y una reversión probada; confirmar que los respaldos del CEDC y de CT funcionan sin la región de la nube; credenciales del integrador separadas por operador, aprobación por sesión y supervisión conjunta.

**EX063.** Modelo: «Nuestro modelo de resiliencia eléctrica (con números sintéticos) muestra que el diseño de respaldo del CVH necesita dos fallas para cortar la alimentación a las áreas críticas: un corte de la red y una falla del respaldo. Una debilidad elude esto: el sistema de gestión del edificio puede desconectar por sí solo los circuitos críticos. Si se usara indebidamente, los pacientes de quirófanos y cuidados intensivos podrían quedarse sin alimentación sin ningún problema en la red. Proponemos un cambio de ingeniería (unas 25 000 £, cifra ilustrativa) para que el sistema del edificio no pueda desconectar los circuitos críticos. Las probabilidades del modelo son estimaciones y un atacante no se comporta de forma aleatoria, por lo que el argumento se basa en eliminar el punto único de falla, no en los números exactos».

**EX064.** Riesgo: un operador que teclea mal una contraseña bajo estrés, o un atacante que introduce deliberadamente contraseñas erróneas, bloquea la HMI durante una emergencia e impide el control. Alternativas: ningún bloqueo en las HMI de la sala de control, combinado con control de acceso físico a la sala, limitación de tasa, alertas ante fallos repetidos y un procedimiento de anulación de emergencia con auditoría; autenticación robusta donde no obstaculice la respuesta (p. ej., tarjetas inteligentes).

**EX065.** $p_o = 34/40 = 0.85$. Codificador A: 10/40 = 0,25 «sí»; B: 12/40 = 0,30 «sí». $p_e = 0.25 \times 0.30 + 0.75 \times 0.70 = 0.075 + 0.525 = 0.60$. $\kappa = (0.85 - 0.60)/(1 - 0.60) = 0.625$. Convencionalmente se describe como acuerdo sustancial; las escalas son convenciones, así que informe del valor, discuta los desacuerdos y afine el libro de códigos.

**EX066.** Información para el consentimiento: propósito del estudio; participación voluntaria y derecho a retirarse hasta una fecha indicada; qué se registra (notas o audio) y por qué; cómo se almacenan los datos, durante cuánto tiempo y quién los ve; cómo se presentarán los resultados (anonimizados, sin detalles que identifiquen a la organización ni vulnerabilidades, revisión por la organización anfitriona). Protección de datos: almacenamiento cifrado, seudónimos para personas y organizaciones, eliminación de las notas brutas tras la transcripción y según el calendario previsto, y ningún detalle técnico de vulnerabilidades en ningún resultado.

**EX067.** Puntuación de la segmentación $= 5w + 8(1-w)/3$; copias de seguridad $= 4w + 13(1-w)/3$. Empate: $w = 5(1-w)/3 \Rightarrow 3w = 5 - 5w \Rightarrow w = 5/8 = 0.625$. Ambas puntúan 4,125 en ese punto. Por encima de 0,625 gana la segmentación.

**EX068.** El requisito es una restricción, no un criterio ponderado: una opción que no puede demostrar el restablecimiento en 4 horas queda excluida. Las copias de seguridad con simulacros de restauración pueden aportar la demostración directamente (registros de los simulacros, idealmente observados por terceros independientes). La segmentación y la detección gestionada reducen la probabilidad o la propagación del ransomware, pero no restablecen el servicio; solo cumplen si se combinan con una capacidad de recuperación demostrada. La comparación pasa a ser entre combinaciones que cumplen la restricción.

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
