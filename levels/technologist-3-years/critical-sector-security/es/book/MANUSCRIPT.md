# Infraestructura crítica y seguridad sectorial: práctica aplicada para tecnólogos

- Idioma: español neutro (`es`); curso de tecnólogo, tres años; aproximadamente 2.400 horas de estudio planificado (curso 092 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–30 de 30 tienen texto didáctico escrito, diecisiete laboratorios sin conexión, los ejercicios EX001–EX090 y sus resultados resueltos correspondientes. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: profesionales que implantan y administran tecnología (administradores de sistemas y de redes, técnicos de TO y de sistemas de edificios, personal del centro de servicios y de plataformas, analistas de seguridad júnior) que ya se ganan la vida gestionando ordenadores y ahora tienen que **construir, operar y evidenciar** la seguridad de un servicio del que dependen las personas. Conocimientos de entrada: fundamentos de informática e introducción a las operaciones de seguridad; soltura con la línea de órdenes; capacidad de leer y modificar ligeramente un script breve de Python.
- En qué se diferencia este curso de sus vecinos. El [libro de grado](../../../../bachelors-4-years/critical-sector-security/es/book/MANUSCRIPT.md) construye los fundamentos conceptuales del campo asignatura por asignatura. El [libro de ingeniería](../../../../engineering-5-years/critical-sector-security/es/book/MANUSCRIPT.md) diseña, modela y verifica sistemas a partir de los requisitos. El [libro de posgrado](../../../../postgraduate-2-years/critical-sector-security/es/book/MANUSCRIPT.md) enseña a los especialistas a dirigir y justificar decisiones a escala de la organización. **Este libro de tecnólogo trata de la implantación y la operación**: tomar un diseño que otra persona aprobó, construirlo correctamente, operarlo cada día, demostrar con evidencia que sus controles funcionan, descubrir rápidamente cuándo dejan de funcionar y traspasarlo para que el siguiente turno pueda continuar. Explica la teoría solo hasta donde un implantador la necesita para tomar decisiones acertadas ante el teclado y en la reunión de cambios.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos y no se relicencian aquí.
- Límite educativo: este curso es un proyecto educativo independiente. No es un programa acreditado, no otorga ninguna titulación y no concede autorización para acceder, escanear, probar o modificar ninguna infraestructura, operador, dispositivo, conjunto de datos o persona reales. Toda organización, lugar, persona, dirección, registro, valor y resultado numérico de un ejemplo resuelto o de un laboratorio es **sintético**, salvo que una frase cite explícitamente una fuente pública. Las direcciones IP proceden de rangos privados ([RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)) o de rangos de documentación ([RFC 5737](https://www.rfc-editor.org/rfc/rfc5737)). Nada de lo que aparece en este libro es un procedimiento operativo para una empresa de servicios, un hospital, un operador de transporte o una red eléctrica reales, y nada constituye asesoramiento jurídico, clínico o regulatorio.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los treinta capítulos siguen a un tecnólogo durante tres años mientras construye y opera un único servicio. El resultado del curso es práctico: **implantar un servicio de extremo a extremo con controles monitorizados** en un entorno de un sector crítico, y ser capaz de mostrar, con evidencia operativa y no con afirmaciones, que funciona.

- **Etapa 1 (capítulos 1–5)**: repasa la informática, las redes, la programación, los datos y la cultura de seguridad, siempre a través de la pregunta «¿qué significa esto para un servicio que no puede detenerse?».
- **Etapa 2 (capítulos 6–10)**: trata los sistemas operativos y la virtualización, la identidad y el acceso, la arquitectura, la medición y una orientación sobre los sectores críticos.
- **Etapa 3 (capítulos 11–15)**: los aplica al servicio: activos, flujos de datos, escenarios de riesgo, un primer conjunto de métodos y la construcción guiada del componente central.
- **Etapa 4 (capítulos 16–20)**: trata de operarlo: métodos de bastionado y de cambio, herramientas, controles, monitorización y resolución de problemas.
- **Etapa 5 (capítulos 21–25)**: integra el servicio con sus vecinos, automatiza con seguridad, evalúa si los controles funcionan, introduce los métodos de investigación aplicada y trabaja en equipo.
- **Etapa 6 (capítulos 26–30)**: traspasa el servicio, lo despliega y lo valida, practica sobre el terreno, completa la construcción del proyecto final y lo evalúa.

Cada capítulo tiene resultados de aprendizaje, secciones didácticas con definiciones, un ejemplo resuelto, una actividad práctica, una lista de errores comunes y límites, tres ejercicios numerados y una síntesis. Diecisiete capítulos contienen un laboratorio de Python. Los laboratorios usan solo la biblioteca estándar de Python 3 (las salidas de este borrador se produjeron con Python 3.13.5); no necesitan red, paquetes, privilegios ni datos reales, y cada salida está impresa en el texto para que pueda comprobar su ejecución. Un laboratorio que escribe archivos lo hace solo dentro de un directorio temporal que crea y elimina. Escriba su respuesta a cada ejercicio antes de abrir los [resultados resueltos](#worked-results). Muchos ejercicios tienen más de una respuesta defendible: el resultado resuelto muestra una, y la rúbrica (0–3) muestra lo que premiaría un evaluador.

Mantenga cuatro etiquetas en cada nota de trabajo, porque los registros operativos los leen después personas que no estaban presentes: **observado** (lo que registró una herramienta o una persona identificada, con la hora y la fuente), **inferido** (lo que usted concluye y por qué), **hecho** (lo que cambió, y con qué registro de cambio) y **abierto** (lo que aún se desconoce o está sin terminar, y quién es su titular). El fallo más común en el nivel de tecnólogo no es desconocer un control; es un control que se instaló una vez, nunca se probó, dejó de funcionar sin que nadie lo notara y seguía comunicándose como «implantado».

### El entorno sintético que se usa en este libro

| Elemento sintético | Papel en el libro | Límite |
|---|---|---|
| **Fallowmere**: un distrito de unas 60.000 personas | Escenario de todos los ejemplos resueltos. | Lugar inventado. |
| **Fallowmere Shared Technology Services (FSTS)** | Un servicio compartido del sector público que gestiona la TI y parte del soporte de TO de tres operadores locales. El lector es un **tecnólogo de seguridad** de su equipo de Plataforma y Seguridad. | Inventado; ninguna organización, persona ni sistema reales. |
| **Fallowmere Water**: 14 estaciones de bombeo (PS-01 a PS-14), una planta de tratamiento y un emplazamiento central | El principal cliente del servicio que se construye en este libro. | Inventado. |
| **Fallowmere Community Hospital** y **Fallowmere Transit** (cochera de autobuses) | Otros dos clientes que comparten personal, redes y proveedores de FSTS. | Inventados. |
| **LANTERN**: el servicio de retransmisión de telemetría | El servicio de extremo a extremo que implanta el lector: estaciones → retransmisor autenticado (RLY-01..03) → historiador (HIST-01) → informes, con la monitorización de la plataforma de monitorización de seguridad de FSTS (SIEM-01). | Diseño inventado para la enseñanza; no es una arquitectura de referencia para una empresa de servicios real. |
| Los proveedores **Kell Instruments**, **Arlen Controls**, **Halden Cloud** y **BayTel** | Proveedor de las RTU de las estaciones, proveedor de los PLC, proveedor de alojamiento en la nube y operador de telecomunicaciones. | Empresas inventadas; cualquier parecido con empresas reales es casual. |
| Personas como A. Okafor (operaciones de Water), B. Lind (responsable de seguridad de FSTS), E. Strand (ingeniera de plataformas), y cada dirección, cuenta, línea de registro, valor y hora | Contexto para los ejercicios. | Inventados. |

Como los datos son sintéticos, el libro puede a veces decirle lo que un operador real nunca sabe; por ejemplo, que una laguna en la telemetría la causó un reloj y no un atacante. Use ese privilegio para aprender cómo fallan las comprobaciones, nunca como evidencia sobre organizaciones reales.

### Política de fuentes

Toda afirmación factual sobre una ley, un estándar, un protocolo, un incidente público o una orientación publicada enlaza con una fuente consultada en octubre de 2026. Los estándares y las orientaciones cambian: cada uno se cita con su versión o su fecha y debe volver a verificarse antes de basarse en él, y nada de lo que aparece aquí interpreta una ley para una organización concreta. Cuando una afirmación pertenece al vocabulario profesional ordinario (por ejemplo, que una función hash transforma una entrada de cualquier longitud en un resumen de longitud fija), el texto no inventa una referencia para ella. Una cita respalda la afirmación general que la acompaña, nunca los detalles sintéticos. Los incidentes públicos se describen solo en el nivel de detalle que publicaron sus editores.

### Normas de seguridad para el trabajo práctico

1. Practique solo con los laboratorios del libro, con equipos de su propiedad o con sistemas cuyo titular le haya dado un permiso **escrito y específico** que nombre los sistemas, la ventana temporal y las acciones permitidas (el capítulo 23 ofrece una plantilla).
2. No conecte nunca un escáner, un portátil de pruebas o un «script rápido» a una red de control en vivo sin ese permiso y sin el acuerdo de la persona responsable del proceso físico. En la tecnología operativa, una lectura puede ser una acción: algunos dispositivos se comportan mal cuando se les sondea.
3. Si se topa con una debilidad en un sistema real, deténgase, anote lo que vio y comuníqueselo en privado a su titular o a través de una divulgación coordinada. No la «confirme».
4. Mantenga los secretos fuera de las notas, los tiques y las capturas de pantalla. La clave del laboratorio del capítulo 15 se imprime precisamente porque es falsa.

## Contenido

1. [Sistemas informáticos](#ch-01): recursos, capacidad y fallos en un equipo que debe seguir funcionando.
2. [Redes y servicios de internet](#ch-02): zonas, conductos, servicios y cómo comprobar lo que realmente transporta la red.
3. [Fundamentos de programación](#ch-03): escribir herramientas pequeñas, correctas y comprobables; validar las entradas no fiables.
4. [Modelos de datos](#ch-04): inventarios, esquemas y restricciones que hacen fiables los datos operativos.
5. [Cultura de seguridad](#ch-05): el vocabulario de las amenazas, los controles y la evidencia para un servicio esencial.
6. [Sistemas operativos y virtualización](#ch-06): bastionado, servicios, integridad de archivos y plataformas virtuales.
7. [Fundamentos de identidad y acceso](#ch-07): cuentas, autenticación, privilegios y revisión de accesos.
8. [Fundamentos de arquitectura de seguridad](#ch-08): zonas y conductos, defensa en profundidad y diseño para la operabilidad.
9. [Evidencia y medición](#ch-09): métricas que dicen la verdad, denominadores y honestidad con muestras pequeñas.
10. [Infraestructura crítica y seguridad sectorial: orientación](#ch-10): qué hace crítico un servicio y en qué se diferencian los sectores.
11. [Infraestructura crítica y seguridad sectorial: activos y contexto](#ch-11): inventario, titularidad, dependencias y estado del soporte.
12. [Infraestructura crítica y seguridad sectorial: flujos de datos](#ch-12): registros de flujos, clasificación, conservación y verificación.
13. [Infraestructura crítica y seguridad sectorial: escenarios de riesgo](#ch-13): redactar escenarios y ordenarlos por su consecuencia.
14. [Infraestructura crítica y seguridad sectorial: métodos I](#ch-14): líneas base, bastionado y control de cambios como métodos diarios.
15. [Infraestructura crítica y seguridad sectorial: laboratorio guiado](#ch-15): construir el retransmisor autenticado con protección frente a la reproducción.
16. [Infraestructura crítica y seguridad sectorial: métodos II](#ch-16): gestión de vulnerabilidades y parches, copias de seguridad y recuperación.
17. [Infraestructura crítica y seguridad sectorial: herramientas](#ch-17): registro, hora, normalización y construcción de una herramienta en la que se pueda confiar.
18. [Infraestructura crítica y seguridad sectorial: controles](#ch-18): elegir, implantar y documentar controles con evidencia.
19. [Infraestructura crítica y seguridad sectorial: monitorización](#ch-19): reglas de detección, la ausencia como señal y la calidad de las alertas.
20. [Infraestructura crítica y seguridad sectorial: resolución de problemas](#ch-20): un método para fallos que pueden ser ataques o no.
21. [Infraestructura crítica y seguridad sectorial: integración del servicio](#ch-21): integrarse con operadores, proveedores, el SOC y los planes de emergencia.
22. [Infraestructura crítica y seguridad sectorial: automatización](../../en/book/MANUSCRIPT.md#ch-22): configuración como código, detección de desviaciones y automatización segura.
23. [Infraestructura crítica y seguridad sectorial: evaluación](../../en/book/MANUSCRIPT.md#ch-23): comprobar si los controles funcionan y decir con cuánta seguridad se sabe.
24. [Métodos de investigación aplicada](../../en/book/MANUSCRIPT.md#ch-24): responder a una pregunta operativa con un estudio pequeño y honesto.
25. [Taller de proyecto en equipo](../../en/book/MANUSCRIPT.md#ch-25): trabajar como equipo de entrega en un servicio compartido.
26. [Infraestructura crítica y seguridad sectorial: traspaso operativo](../../en/book/MANUSCRIPT.md#ch-26): manuales de operación, titularidad y un traspaso que sobreviva al turno de noche.
27. [Despliegue y validación](../../en/book/MANUSCRIPT.md#ch-27): comprobaciones previas, despliegues canario, vuelta atrás y validación posterior al despliegue.
28. [Práctica sobre el terreno](../../en/book/MANUSCRIPT.md#ch-28): trabajar con seguridad en emplazamientos remotos y con el personal de operaciones.
29. [Construcción del proyecto final](../../en/book/MANUSCRIPT.md#ch-29): el servicio monitorizado de extremo a extremo y su registro de evidencia.
30. [Evaluación del proyecto final](../../en/book/MANUSCRIPT.md#ch-30): revisión del diseño, evidencia operativa y evaluación del proyecto de integración.

Apéndices: [Resultados resueltos y notas de evaluación](#worked-results) · [Glosario](#glossary) · [Referencias](#references).

<a id="ch-01"></a>

## Capítulo 1 — Sistemas informáticos

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- describir un equipo en función de los cuatro recursos que realmente se le agotan a un operador (cómputo, memoria, almacenamiento y E/S) y del recurso que la gente olvida, el **tiempo**;
- prever cuándo se agotará un recurso a partir de una serie corta de mediciones e indicar hasta qué punto puede confiarse en la previsión;
- explicar por qué un equipo que presta una función esencial necesita **margen de capacidad**, y no solo «lo suficiente»;
- reconocer las formas habituales en que un equipo falla en silencio y escribir las primeras comprobaciones que lo detectarían.

El curso de entrada le enseñó cómo funciona un ordenador. Este capítulo plantea una pregunta más estrecha que recorre todo el libro: *¿qué debe seguir siendo cierto en este ordenador para que el servicio que funciona sobre él siga funcionando, y cómo sabría usted que ha dejado de serlo?* El equipo retransmisor de LANTERN, RLY-01, es la primera máquina que conocerá; en el capítulo 29 será una de tres.

### 1.1 Un equipo como conjunto de recursos finitos

Todo servicio que usted opera se ejecuta en un equipo con recursos finitos. El **cómputo** (tiempo de CPU) limita cuánto trabajo puede hacerse por segundo. La **memoria** limita cuánto puede mantenerse a la vez; cuando se agota, el sistema operativo o bien pagina a disco (y todo se ralentiza) o bien termina procesos. El **almacenamiento** limita lo que puede conservarse; cuando un disco se llena, las escrituras fallan, y muchos programas fallan mal: una base de datos puede dejar de aceptar escrituras, un demonio de registro puede descartar mensajes en silencio, un retransmisor puede caerse. La **E/S** (el rendimiento del disco y de la red) limita la rapidez con que los datos pueden entrar y salir.

El recurso que la gente olvida es el **tiempo**: el reloj del equipo. Un reloj erróneo no detiene un servicio, pero hace que sus registros discrepen de los de todos los demás, rompe la validación de certificados y las comprobaciones de ventanas temporales, y hace que las investigaciones resulten engañosas. Los capítulos 17 y 20 vuelven con detalle sobre el tiempo.

Para un servicio crítico, la pregunta útil sobre cada recurso no es «¿cuánto se usa?», sino «¿cuánto falta para que este recurso detenga el servicio, y con cuánta antelación nos avisaremos?».

### 1.2 Utilización, saturación y errores

Una forma práctica de examinar cualquier recurso es preguntarse tres cosas sobre él: su **utilización** (lo ocupado que está, como fracción de su capacidad), su **saturación** (cuánto trabajo espera porque está ocupado: una cola de ejecución, una cola de disco, paquetes descartados) y sus **errores** (operaciones fallidas). Una CPU al 60 % de utilización sin cola está bien; un disco al 40 % de utilización con una cola larga, no. La utilización por sí sola oculta el problema que perciben los usuarios, que es la espera.

De ello se derivan dos hábitos. Primero, mida en un percentil, no en una media: el percentil 95 de la CPU a lo largo de un día le informa de los momentos de mayor actividad, que son los que importan; la media diaria los oculta. Segundo, mida durante un periodo lo bastante largo como para ver el ritmo del servicio. Los retransmisores de telemetría están más ocupados cuando se ejecutan los informes y cuando las estaciones suben datos por lotes tras un corte de red; los sistemas hospitalarios alcanzan su máximo en los cambios de turno; los sistemas de transporte, en la hora punta.

### 1.3 El margen de capacidad, y por qué «suficiente» no basta

El **margen de capacidad** es la capacidad sobrante entre la carga máxima normal y el punto en que el servicio se degrada. Un servicio esencial necesita margen por tres razones: la demanda crece de forma inesperada (una tormenta, un suceso con víctimas en masa, un corte en otro lugar que le envía tráfico); la propia recuperación consume recursos (las estaciones que estaban desconectadas suben su acumulado cuando vuelven; una restauración escribe intensamente en disco); y las herramientas de seguridad consumen recursos (un escaneo, una comprobación de integridad o una actualización del antivirus pueden duplicar el uso de CPU durante minutos). Un equipo dimensionado para tener «justo lo suficiente» en un día normal está dimensionado para fallar el día en que más importa.

### 1.4 Prever el agotamiento

En los recursos que crecen de forma constante (el disco que se llena con registros y datos es el caso clásico), un ajuste lineal sobre las mediciones diarias recientes da una previsión utilizable: el crecimiento por día y los días que faltan hasta un umbral de alarma y hasta llenarse. Es una previsión, no una promesa. Supone que el crecimiento continúa al ritmo reciente. Será errónea si cambia la conservación, si un proceso ruidoso empieza a registrar en nivel de depuración o si a un corte le sigue una ráfaga de datos acumulados. Úsela para programar acciones mucho antes del umbral, y vuelva a calcularla tras cualquier cambio.

Un cálculo complementario útil es el tamaño en **régimen estacionario**: si los datos se conservan durante *R* días y llegan a razón de *g* GB al día, el volumen conservado se estabiliza en torno a *g × R*. Si esa cifra supera el disco, ninguna «limpieza» salvará al equipo; tiene que cambiar la conservación, el volumen o la capacidad.

### 1.5 Modos de fallo silenciosos

Los equipos de los servicios que funcionan durante mucho tiempo tienden a fallar de un pequeño número de formas silenciosas: se llena un disco o una partición; un trabajo de rotación de registros se detiene y un archivo crece sin límite; caduca un certificado; el reloj se desvía después de que su fuente de hora deje de ser accesible; un proceso pierde memoria y el gestor del sistema lo reinicia cada pocos días, con lo que se pierden los datos en tránsito; un trabajo programado (copia de seguridad, informe) falla y nadie lee su correo. Cada uno de ellos puede detectarse con una comprobación que no cuesta casi nada, siempre que alguien escriba la comprobación y alguien lea su resultado. El capítulo 19 convierte esas comprobaciones en monitorización.

### 1.6 Ejemplo resuelto: el disco de RLY-01 (sintético)

E. Strand le pregunta si RLY-01, que almacena temporalmente la telemetría de las estaciones y conserva sus propios registros durante 30 días, necesita un disco más grande antes del invierno. Usted recoge 14 días de uso del disco (disco de 200 GB) y el percentil 95 diario de la CPU. El disco crece unos 1,9 GB al día y está en 120,9 GB. La alarma de operaciones salta al 85 % (170 GB). A este ritmo, la alarma saltará en unos 26 días y el disco estará lleno en unos 41 días. Con una conservación de 30 días, el volumen de registros en régimen estacionario es de unos 57 GB, pero el disco ya está muy por encima de esa cifra, lo que indica que el crecimiento no se debe solo a los registros dentro del plazo de conservación. Algo conserva datos durante más de 30 días. Es una cuestión de configuración, no de capacidad, y debe responderse antes de comprar un disco.

La serie de la CPU muestra una pauta semanal: los días 6 y 7 de cada semana funcionan en torno al 62 %, frente a alrededor del 42 % los demás días. Usted pregunta a operaciones de Water y se entera de que esos días se ejecutan los informes semanales de cumplimiento. Es una carga normal, pero es la carga para la que hay que dimensionar.

### 1.7 Actividad práctica: margen de capacidad

Ejecute el Lab 1. Ajusta una recta a la serie del disco, informa de los días que faltan hasta la alarma y hasta llenarse, del volumen de registros en régimen estacionario con una conservación de 30 días, y compara la CPU de los días de informes con la de los demás días. **Lab 1** (guárdelo como `lab01.py` y ejecútelo con `python3 lab01.py`):

```python
# Lab 1 - capacity headroom for the relay host (offline, standard library only)
# Synthetic: Fallowmere relay host RLY-01. Daily samples over 14 days.
disk_total_gb = 200.0
disk_used_gb = [96.0, 97.9, 99.7, 101.8, 103.6, 105.5, 107.6, 109.4, 111.3, 113.2, 115.1, 117.0, 118.8, 120.9]
cpu_p95 = [41, 43, 40, 44, 42, 61, 63, 42, 41, 44, 43, 40, 62, 64]  # percent, 95th percentile per day
alarm_at = 0.85  # operations alarm when disk reaches 85 % full

n = len(disk_used_gb)
xs = list(range(n))
mx, my = sum(xs) / n, sum(disk_used_gb) / n
slope = sum((x - mx) * (y - my) for x, y in zip(xs, disk_used_gb)) / sum((x - mx) ** 2 for x in xs)
print(f"growth: {slope:.2f} GB/day")
for limit, label in ((alarm_at * disk_total_gb, "85% alarm"), (disk_total_gb, "full")):
    days = (limit - disk_used_gb[-1]) / slope
    print(f"days until {label}: {days:.1f}")
# retention: logs kept 30 days; growth comes from logs (synthetic assumption)
print(f"steady-state log volume at 30-day retention: {slope*30:.1f} GB")
weekly = [cpu_p95[i] for i in range(n) if i % 7 in (5, 6)]
weekday = [cpu_p95[i] for i in range(n) if i % 7 not in (5, 6)]
print(f"cpu p95 mean weekday {sum(weekday)/len(weekday):.1f}% vs days 6-7 of each week {sum(weekly)/len(weekly):.1f}%")
```

Salida esperada (Python 3.13.5):

```text
growth: 1.91 GB/day
days until 85% alarm: 25.7
days until full: 41.4
steady-state log volume at 30-day retention: 57.3 GB
cpu p95 mean weekday 42.0% vs days 6-7 of each week 62.5%
```

Anote las cuatro cifras en su nota de trabajo como **observado**; después, escriba una frase **inferida** y un elemento **abierto**. Un buen elemento abierto nombra una pregunta y un titular: «¿Por qué conserva RLY-01 más de 30 días de datos? — E. Strand, antes del viernes».

### 1.8 Errores comunes y límites

- Informar de la CPU media y concluir que hay margen, cuando el máximo (el momento que importa) está cerca de la saturación.
- Tratar una previsión lineal como una garantía; supone que el futuro se parecerá a las dos últimas semanas.
- Resolver un fallo de conservación o de registro comprando capacidad, lo que oculta el fallo hasta que se llena el disco nuevo.
- Olvidar que la recuperación y la actividad de seguridad consumen recursos.
- Fijar una alarma en un umbral que deja menos tiempo de aviso del que se tarda en adquirir, aprobar e instalar más capacidad.
- Ignorar el reloj porque «solo es la hora».

Catorce muestras son una base pequeña para cualquier previsión. El valor del método es que convierte una impresión («parece que el disco se está llenando») en una cifra con un supuesto explícito que alguien puede comprobar.

### Ejercicios — capítulo 1

**EX001 — Plazo de suministro frente a tiempo de aviso.** *Objetivo:* fijar un umbral de alarma a partir del plazo operativo de suministro. *Entradas:* la salida del Lab 1; la adquisición e instalación aprobada de un disco nuevo tarda 21 días laborables (unos 30 días naturales). *Restricciones:* mantenga el mismo ritmo de crecimiento. *Pasos:* (1) calcule el nivel de llenado en el que debe presentar la solicitud para que el disco se instale antes de llenarse, con 7 días de margen; (2) expréselo como porcentaje del disco; (3) indique si la alarma del 85 % es adecuada. *Evidencia esperada:* cálculo y una recomendación de dos frases. *Rúbrica:* 3 = umbral correcto (se necesitan 37 días × 1,91 GB ≈ 71 GB de espacio libre, es decir, presentar la solicitud a unos 129 GB o al 65 %, que RLY-01 alcanza en unos cuatro días) y un juicio claro de que el 85 % es demasiado tarde para este plazo de suministro; 2 = método correcto, error aritmético; 1 = umbral elegido sin tener en cuenta el plazo de suministro; 0 = nada.

**EX002 — Explique el crecimiento.** *Objetivo:* separar un problema de capacidad de un problema de configuración. *Entradas:* el ejemplo resuelto. *Restricciones:* no toque ningún sistema real; razone a partir de las cifras. *Pasos:* (1) calcule cuántos días de datos a 1,91 GB/día representan los 120,9 GB actuales; (2) indique dos causas de configuración plausibles; (3) describa la comprobación que permitiría distinguirlas. *Evidencia esperada:* nota breve con las etiquetas observado / inferido / abierto. *Rúbrica:* 3 = unos 63 días calculados, dos causas concretas (por ejemplo, la rotación no borra, no se purga el búfer de un destino desconectado o un segundo flujo de registros queda fuera de la política de conservación) y una comprobación para cada una; 2 = causas genéricas; 1 = recomienda solo un disco más grande; 0 = nada.

**EX003 — Lista de comprobación de fallos silenciosos.** *Objetivo:* convertir los modos de fallo silenciosos en comprobaciones. *Entradas:* el capítulo 1 («Modos de fallo silenciosos»). *Restricciones:* cinco comprobaciones; cada una debe nombrar lo que se mide, el umbral y quién lee el resultado. *Pasos:* escriba una tabla con las columnas: modo de fallo, medición, umbral, lector, acción. *Evidencia esperada:* tabla. *Rúbrica:* 3 = cinco modos de fallo distintos, umbrales medibles con tiempo de aviso, un lector designado y una acción para cada uno; 2 = una columna débil; 1 = un genérico «monitorizar el servidor»; 0 = nada.

### Síntesis del capítulo

Un equipo es un conjunto de recursos finitos más un reloj. Para un servicio esencial, la pregunta sobre cada recurso es cuánto falta para que detenga el servicio y con cuánta antelación se le avisará. Mida la utilización, la saturación y los errores en percentiles a lo largo del ritmo natural del servicio; mantenga margen para los días malos, la recuperación y el trabajo de seguridad; prevea el agotamiento con supuestos explícitos; y escriba comprobaciones baratas para los fallos silenciosos que de verdad hacen caer los servicios. Cuando las cifras no coincidan con lo esperado, como ocurrió con el disco de RLY-01, busque una causa de configuración antes de comprar capacidad.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 30

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Redes y servicios de internet

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- describir una red en términos de **zonas** (grupos de sistemas con confianza y función similares) y **conductos** (los caminos permitidos entre ellas);
- leer un registro de flujo y asignarlo a zonas, protocolos y puertos;
- comparar lo que la red transporta realmente con lo que se declaró, y clasificar cada diferencia;
- explicar por qué un flujo declarado que **no** transporta tráfico también es un hallazgo.

El capítulo 1 examinó un equipo. Un servicio son muchos equipos que se comunican entre sí. En la infraestructura crítica, la red es donde se supone que se aplica la mayor parte de la separación entre los sistemas de negocio, los sistemas de control y el mundo exterior, y donde esa separación se erosiona con más frecuencia, una regla «temporal» cada vez.

### 2.1 De las direcciones a las zonas

Una dirección IP le dice a dónde va un paquete; no le dice para qué sirve el destino. Por eso los operadores agrupan los sistemas en **zonas**: en el diseño de LANTERN, la zona de *estaciones* (PLC y RTU en las estaciones de bombeo), la zona del *retransmisor* (equipos RLY), la zona *corporativa* (sistemas de negocio de FSTS y los usuarios de informes del historiador) y la *externa* (todo lo de fuera, incluidos los proveedores). La idea de zonas y conductos procede de la práctica de seguridad en automatización industrial: la serie ISA/IEC 62443 usa exactamente estos términos ([ISA overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)), y la guía de TO del NIST recomienda segmentar las redes de control respecto de las redes de negocio ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

Un **conducto** es un camino declarado y justificado entre dos zonas: zona de origen, zona de destino, protocolo, puerto y propósito. LANTERN declara cuatro: las estaciones envían Modbus/TCP (tcp/502) al retransmisor; el retransmisor envía HTTPS (tcp/443) al historiador en la zona corporativa; los administradores de la zona corporativa acceden al retransmisor por SSH (tcp/22); y el retransmisor sirve la hora (udp/123, NTP) a las estaciones.

### 2.2 Servicios, puertos y lo que implican

Un número de puerto es una convención, no una garantía: tcp/443 suele transportar TLS, pero cualquier cosa puede escuchar ahí. Aun así, la convención le dice qué esperar y qué cuestionar. Los protocolos industriales como Modbus/TCP se diseñaron para redes cerradas y no tienen autenticación incorporada; un dispositivo que acepta escrituras Modbus las aceptará de cualquiera que pueda alcanzarlo. Por eso el camino importa tanto: *si un portátil corporativo puede alcanzar un PLC en tcp/502, lo único que se interpone entre un error (o un atacante) y una bomba es que nadie lo haya intentado.*

Los servicios de internet (DNS, NTP, HTTPS, SSH) son la fontanería de todo servicio moderno. Cada uno tiene un modo de fallo que importa en la operación: un fallo de DNS impide resolver los nombres aunque los equipos estén bien; un fallo de NTP deja que los relojes se desvíen; un fallo de TLS (un certificado caducado) convierte un servicio que funciona en uno inalcanzable; un SSH expuesto a internet atrae intentos constantes de adivinar contraseñas.

### 2.3 Lo declarado frente a lo observado

Una base de reglas de cortafuegos o un diagrama de diseño dice lo que *debería* ocurrir. Los **registros de flujo** (resúmenes de conversaciones recogidos por cortafuegos, conmutadores o sensores) dicen lo que *ocurrió*. Comparar ambos es una de las tareas rutinarias de mayor valor que puede hacer un tecnólogo, y no necesita herramientas de ataque: consiste en leer sus propios registros. Cada diferencia cae en una de cuatro clases:

1. **Observado y declarado**: lo esperado; compruebe aun así que los volúmenes parecen normales.
2. **Observado pero no declarado**: existe un camino que nadie justificó. O la declaración está incompleta (actualícela, con un responsable y un propósito) o la base de reglas es demasiado permisiva (corríjala).
3. **Declarado pero no observado**: o el servicio no funciona (una estación está en silencio), o el conducto declarado está obsoleto y debe eliminarse.
4. **Observado hacia una zona desconocida**: una dirección que usted no sabe ubicar; su inventario está incompleto.

### 2.4 Ejemplo resuelto: los flujos de una noche (sintético)

B. Lind le entrega una exportación de flujos del cortafuegos central correspondiente a una noche. La mayoría de los flujos coinciden con conductos. Tres no: una estación de trabajo corporativa, 10.40.3.7, habló Modbus directamente con el PLC de PS-04 (12 conversaciones); una dirección externa, 192.0.2.44, alcanzó el retransmisor por SSH (3 conversaciones); y el retransmisor abrió una conexión HTTPS hacia una dirección externa, 192.0.2.80. Un origen declarado, la RTU de PS-09 en 10.20.0.13, no envió nada. Nada de esto prueba un ataque. El flujo de la zona corporativa al PLC podría ser un ingeniero que usa una herramienta de configuración desde la red equivocada; el SSH externo podría ser ruido de fondo de internet que llega a un puerto expuesto; el HTTPS saliente del retransmisor podría ser una actualización de paquetes. Aun así, cada uno es un hallazgo, porque cada uno es un camino que el diseño no permite. La estación en silencio es ante todo un problema operativo: puede que Operaciones de Agua esté operando PS-09 a ciegas.

### 2.5 Actividad práctica: flujos frente a conductos

Ejecute el Lab 2. Asigna cada dirección a una zona con el módulo `ipaddress`, compara cada flujo con los conductos declarados e informa de los flujos declarados sin tráfico. **Lab 2** (guárdelo como `lab02.py` y ejecútelo con `python3 lab02.py`):

```python
# Lab 2 - observed flows versus the declared conduit list (offline, standard library only)
# Synthetic: Fallowmere Water pumping-station network. Addresses are documentation/private ranges.
import ipaddress
zones = {
    "station": ipaddress.ip_network("10.20.0.0/24"),
    "relay":   ipaddress.ip_network("10.30.0.0/28"),
    "corp":    ipaddress.ip_network("10.40.0.0/16"),
    "vendor":  ipaddress.ip_network("192.0.2.0/24"),   # TEST-NET-1, stands in for internet
}
declared = {("station", "relay", "tcp", 502), ("relay", "corp", "tcp", 443),
            ("corp", "relay", "tcp", 22), ("relay", "station", "udp", 123)}
flows = """10.20.0.11,10.30.0.5,tcp,502,1840
10.20.0.12,10.30.0.5,tcp,502,1790
10.30.0.5,10.40.8.20,tcp,443,3600
10.40.3.7,10.30.0.5,tcp,22,4
10.30.0.5,10.20.0.11,udp,123,96
10.40.3.7,10.20.0.11,tcp,502,12
192.0.2.44,10.30.0.5,tcp,22,3
10.30.0.5,192.0.2.80,tcp,443,1
10.20.0.13,10.30.0.5,tcp,502,0"""
def zone(a):
    ip = ipaddress.ip_address(a)
    return next((z for z, net in zones.items() if ip in net), "unknown")
seen = set()
for line in flows.splitlines():
    s, d, p, port, count = line.split(",")
    key = (zone(s), zone(d), p, int(port))
    if int(count) == 0:
        print(f"SILENT  {s:>12} -> {d:<12} {p}/{port}  (declared flow with no traffic)")
        continue
    seen.add(key)
    tag = "OK     " if key in declared else "UNDECL "
    print(f"{tag} {s:>12} -> {d:<12} {p}/{port} {key[0]}->{key[1]} n={count}")
for k in sorted(declared - seen):
    print("NOT SEEN", k)
```

Salida esperada (Python 3.13.5):

```text
OK        10.20.0.11 -> 10.30.0.5    tcp/502 station->relay n=1840
OK        10.20.0.12 -> 10.30.0.5    tcp/502 station->relay n=1790
OK         10.30.0.5 -> 10.40.8.20   tcp/443 relay->corp n=3600
OK         10.40.3.7 -> 10.30.0.5    tcp/22 corp->relay n=4
OK         10.30.0.5 -> 10.20.0.11   udp/123 relay->station n=96
UNDECL     10.40.3.7 -> 10.20.0.11   tcp/502 corp->station n=12
UNDECL    192.0.2.44 -> 10.30.0.5    tcp/22 vendor->relay n=3
UNDECL     10.30.0.5 -> 192.0.2.80   tcp/443 relay->vendor n=1
SILENT    10.20.0.13 -> 10.30.0.5    tcp/502  (declared flow with no traffic)
```

Escriba cada hallazgo en una línea: qué se observó, a qué clase pertenece, la explicación benigna más probable, la explicación más preocupante y la siguiente comprobación. No «pruebe» usted ningún camino; pregunte al responsable.

Aplicadas a la exportación de esa noche, las cuatro líneas quedan así. De la zona corporativa 10.40.3.7 a PS-04 por Modbus, 12 conversaciones: camino no declarado; benigna, la herramienta de configuración de un ingeniero en la red equivocada; preocupante, una estación de trabajo comprometida que alcanza un PLC; siguiente comprobación, preguntar a Ingeniería de Agua quién usa ese equipo. De la dirección externa 192.0.2.44 al retransmisor por SSH: exposición; siguiente comprobación, por qué el puerto 22 responde desde fuera. Del retransmisor a 192.0.2.80 por HTTPS: salida no declarada. PS-09 en silencio: flujo declarado sin tráfico, que se plantea primero a Operaciones de Agua.

### 2.6 Errores frecuentes y límites

- Leer una base de reglas y creer que describe el tráfico; las reglas son intenciones, los flujos son hechos.
- Tratar «no declarado» como «malicioso», o como «inofensivo porque es interno».
- Ignorar los flujos declarados en silencio; una estación que deja de hablar es una interrupción del servicio antes que una cuestión de seguridad.
- Suponer que un puerto identifica una aplicación.
- Recoger flujos solo en el borde de internet, donde los caminos de mayores consecuencias (de la zona corporativa a la de control) son invisibles.

Los registros de flujo muestran quién habló con quién, en qué puerto y cuánto; no muestran el contenido ni la intención, y pueden estar muestreados. Son excelentes para comprobar la arquitectura y pobres para probar lo que se hizo.

### Ejercicios — capítulo 2

**EX004 — Clasifique y priorice.** *Objetivo:* clasificar las diferencias de flujo y ordenar el seguimiento. *Entradas:* la salida del Lab 2. *Restricciones:* cuatro hallazgos; como máximo una frase de explicación cada uno. *Pasos:* (1) asigne cada hallazgo a una clase del capítulo 2 («Lo declarado frente a lo observado»); (2) ordénelos para el seguimiento según su posible consecuencia para el servicio de agua; (3) nombre el responsable al que contactaría primero en cada caso. *Evidencia esperada:* tabla. *Rúbrica:* 3 = el Modbus de la zona corporativa a la estación queda primero porque alcanza el proceso físico, el silencio de PS-09 se trata como prioridad operativa, el SSH externo y la salida del retransmisor se ordenan con sensatez, se nombran los responsables; 2 = clases correctas, orden poco justificado; 1 = ordena por número de conversaciones; 0 = nada.

**EX005 — Actualice la declaración.** *Objetivo:* decidir entre cambiar el diseño y cambiar la red. *Entradas:* Operaciones de Agua confirma que el HTTPS saliente del retransmisor fue una actualización del sistema operativo desde un espejo del proveedor; el tráfico de la zona corporativa al PLC fue el portátil de un ingeniero. *Restricciones:* cada conducto necesita origen, destino, protocolo/puerto, propósito y responsable. *Pasos:* (1) decida en cada caso si añadir un conducto o eliminar el camino; (2) para cualquier conducto añadido, escriba su entrada completa; (3) para el acceso del ingeniero, proponga el camino declarado que debería sustituirlo. *Evidencia esperada:* lista de conductos actualizada y justificación. *Rúbrica:* 3 = camino de actualización añadido de forma acotada (espejo concreto, a través de un proxy o un servidor de actualizaciones, responsable nombrado) o sustituido por una fuente de actualizaciones interna; el acceso de ingeniería se traslada a un camino de salto declarado y autenticado, no de la zona corporativa al PLC; 2 = entradas sensatas pero incompletas; 1 = simplemente permite todo lo observado; 0 = nada.

**EX006 — Amplíe el laboratorio.** *Objetivo:* hacer más útil la herramienta de comparación. *Entradas:* el Lab 2. *Restricciones:* solo la biblioteca estándar; no cambie los datos sintéticos salvo en lo indicado. *Pasos:* (1) añada un flujo de 10.50.1.9 al retransmisor por tcp/443; (2) modifique el script para que las direcciones que no pertenecen a ninguna zona se notifiquen como "UNKNOWN ZONE" en lugar de compararse; (3) muestre la nueva salida. *Evidencia esperada:* diferencias del código y salida. *Rúbrica:* 3 = la dirección desconocida se notifica de forma diferenciada y la ejecución lo muestra; 2 = funciona pero el mensaje es poco claro; 1 = no se ejecutó; 0 = nada.

### Síntesis del capítulo

Piense en la red como zonas unidas por conductos declarados, cada uno con un propósito y un responsable. Las reglas expresan intenciones; los registros de flujo expresan hechos. Comparar ambos con regularidad (observado y declarado, observado pero no declarado, declarado pero en silencio, desconocido) es barato, seguro y de lo más valioso que hace un implementador. En la infraestructura crítica, el camino no declarado de mayores consecuencias es el que alcanza el proceso físico.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 30

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programación

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- escribir una herramienta pequeña cuyo comportamiento ante entradas erróneas se decide de antemano, no se descubre en producción;
- validar entradas no confiables mediante una **lista de permitidos** de estructura, tipo, rango y orden;
- separar los resultados **rechazar**, **poner en cuarentena** y **aceptar**, y explicar por qué un sistema en operación necesita los tres;
- probar una herramienta con casos deliberadamente erróneos y registrar los resultados como evidencia.

Los implementadores de servicios críticos escriben mucho código pequeño: analizadores, código de unión entre sistemas, comprobaciones, generadores de informes. Casi nunca se revisa. Este capítulo trata de escribir ese código de modo que falle de forma segura, porque en LANTERN el código que lee los mensajes de las estaciones decide lo que el historiador (y, por tanto, los operadores) cree sobre la red de agua.

### 3.1 Entradas no confiables

Una **entrada no confiable** es cualquier dato cuyo contenido usted no controla: mensajes de dispositivos de campo, archivos de proveedores, campos que teclean los usuarios, registros del sistema de otra organización. Incluso un dispositivo propio pasa a ser no confiable en cuanto recuerda que puede estar mal configurado, averiado, sustituido o suplantado. La regla es sencilla: compruebe la entrada frente a lo que espera *antes* de actuar sobre ella, y decida de antemano qué ocurre cuando no supera la comprobación. La guía del proyecto OWASP sobre validación de entradas recomienda usar listas de permitidos (aceptar solo formas conocidas como válidas) en lugar de listas de bloqueo (bloquear formas conocidas como maliciosas), validar tanto la sintaxis como el significado y hacerlo lo antes posible ([OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)).

### 3.2 Capas de validación

Para un mensaje de telemetría con la forma `STATION|TAG|VALUE|UNIX_TIME|SEQ`, la validación tiene capas, y el orden importa:

1. **Estructura**: exactamente cinco campos. Un número de campos erróneo significa que el mensaje no puede interpretarse en absoluto.
2. **Identidad y vocabulario**: el identificador de estación coincide exactamente con el patrón permitido (`PS-` y dos dígitos) y la etiqueta es una que el sistema conoce. Las etiquetas desconocidas se rechazan, no se almacenan «por si acaso».
3. **Tipo**: el valor, la hora y la secuencia se interpretan como números. Los valores que se interpretan pero no son finitos (`nan`, `inf`) se rechazan; muchos lenguajes los aceptan sin problema.
4. **Significado físico**: el valor está dentro de lo que el proceso físico puede producir (un nivel de depósito entre 0 y 12 metros; cloro entre 0 y 5 mg/L en este diseño sintético). Un valor fuera de ese rango no es necesariamente malicioso (los sensores fallan), así que se **pone en cuarentena** para que una persona lo revise, en lugar de descartarse o almacenarse en silencio.
5. **Tiempo**: la marca de tiempo del mensaje está cerca del reloj del receptor. Una diferencia grande indica un problema de reloj o un mensaje antiguo; póngalo en cuarentena.
6. **Orden**: el número de secuencia es mayor que el último aceptado para esa estación. Un número repetido o menor es una reproducción o una reordenación; rechácelo.

### 3.3 Rechazar, poner en cuarentena, aceptar

Una función de validación que solo devuelve «válido» o «no válido» obliga a una mala elección con los datos dudosos: o se tira una lectura que un operador podría necesitar, o se almacena una que podría inducir a error. Los sistemas en operación necesitan un tercer resultado. **Rechazar** significa que la entrada no puede considerarse fiable ni interpretarse, y se registra y descarta. **Poner en cuarentena** significa que la entrada es interpretable pero inverosímil; se guarda aparte, se marca y se revisa. **Aceptar** significa que superó todas las comprobaciones y puede usarse para actuar. Cada resultado se cuenta: un aumento repentino de rechazos es en sí mismo una señal de monitorización (capítulo 19).

### 3.4 Disciplina del código pequeño

Cuatro hábitos hacen fiables las herramientas pequeñas. Mantenga **una función por decisión**, para poder probarla por separado. Haga **explícito el estado**: la última secuencia vista por estación se pasa como argumento, no se esconde en una variable global. **Falle de forma cerrada**: cualquier camino que no previó termina en rechazo, no en aceptación. Y **pruebe primero con casos erróneos**: para cada comprobación, escriba al menos una entrada que deba fallarla, y ejecútelas todas después de cada cambio. El Lab 3 sigue los cuatro a pequeña escala: todas las decisiones están en una única función corta, `validate()`, que puede probarse por separado. La comprobación de secuencia recibe como argumento el último número aceptado por estación, y por eso el 102 repetido puede probarse por sí solo; y la regla de plausibilidad del cloro es un paso separado, guiado por la tabla `LIMITS` después de interpretar el valor, y por eso 9,80 mg/L puede ponerse en cuarentena en lugar de rechazarse sin tocar el analizador.

### 3.5 Ejemplo resuelto: el validador de mensajes de las estaciones (sintético)

El Lab 3 implementa las seis capas. Al ejecutarlo sobre once mensajes sintéticos se obtienen tres aceptaciones, seis rechazos y dos cuarentenas. Fíjese en los casos que un analizador ingenuo resolvería mal: `nan` se interpreta como número de coma flotante y se almacenaría; `210.5;DROP` se detecta solo porque el valor se interpreta como número en lugar de pasarse como texto; `PS-7` falla porque el patrón se compara completo; un número de secuencia 102 repetido se rechaza como reproducción aunque el mensaje sea por lo demás perfecto; y un valor de cloro de 9,80 mg/L se pone en cuarentena, no se rechaza, porque una persona necesita saber si el analizador de PS-07 ha fallado.

### 3.6 Actividad práctica: validador y casos de prueba

**Lab 3** (guárdelo como `lab03.py` y ejecútelo con `python3 lab03.py`):

```python
# Lab 3 - validating telemetry messages before they reach the historian (offline, standard library only)
# Synthetic message format from Fallowmere pumping stations:  STATION|TAG|VALUE|UNIX_TIME|SEQ
import re
LIMITS = {"LEVEL_M": (0.0, 12.0), "FLOW_LS": (0.0, 450.0), "CL2_MGL": (0.0, 5.0)}
STATION = re.compile(r"PS-\d{2}")
def validate(line, now, last_seq):
    parts = line.strip().split("|")
    if len(parts) != 5:
        return "reject: field count"
    st, tag, val, ts, seq = parts
    if not STATION.fullmatch(st):
        return "reject: station id"
    if tag not in LIMITS:
        return "reject: unknown tag"
    try:
        v, t, q = float(val), int(ts), int(seq)
    except ValueError:
        return "reject: not numeric"
    if v != v or v in (float("inf"), float("-inf")):
        return "reject: not finite"
    lo, hi = LIMITS[tag]
    if not lo <= v <= hi:
        return "quarantine: out of physical range"
    if abs(now - t) > 300:
        return "quarantine: clock skew >300 s"
    if q <= last_seq.get(st, -1):
        return "reject: replay or reorder"
    last_seq[st] = q
    return "accept"
now = 1_790_000_000
msgs = ["PS-04|LEVEL_M|3.42|1789999990|101", "PS-04|LEVEL_M|3.44|1789999995|102",
        "PS-04|LEVEL_M|3.44|1789999995|102", "PS-07|CL2_MGL|0.61|1789999801|55",
        "PS-07|CL2_MGL|9.80|1789999990|56", "PS-07|FLOW_LS|nan|1789999990|57",
        "PS-7|FLOW_LS|120|1789999990|58", "PS-09|PRESS_BAR|2.1|1789999990|9",
        "PS-09|FLOW_LS|210.5|1789990000|10", "PS-09|FLOW_LS|210.5;DROP|1789999990|11",
        "PS-04|LEVEL_M|3.47|1789999999"]
state = {}
counts = {}
for m in msgs:
    r = validate(m, now, state)
    counts[r.split(":")[0]] = counts.get(r.split(":")[0], 0) + 1
    print(f"{m:<38} {r}")
print(counts)
```

Salida esperada (Python 3.13.5):

```text
PS-04|LEVEL_M|3.42|1789999990|101      accept
PS-04|LEVEL_M|3.44|1789999995|102      accept
PS-04|LEVEL_M|3.44|1789999995|102      reject: replay or reorder
PS-07|CL2_MGL|0.61|1789999801|55       accept
PS-07|CL2_MGL|9.80|1789999990|56       quarantine: out of physical range
PS-07|FLOW_LS|nan|1789999990|57        reject: not finite
PS-7|FLOW_LS|120|1789999990|58         reject: station id
PS-09|PRESS_BAR|2.1|1789999990|9       reject: unknown tag
PS-09|FLOW_LS|210.5|1789990000|10      quarantine: clock skew >300 s
PS-09|FLOW_LS|210.5;DROP|1789999990|11 reject: not numeric
PS-04|LEVEL_M|3.47|1789999999          reject: field count
{'accept': 3, 'reject': 6, 'quarantine': 2}
```

Antes de cambiar nada, anote lo que espera que imprima cada línea. Después, ejecútelo. Cualquier línea en la que su expectativa fue errónea es un lugar donde su modelo mental del código era erróneo, y ese es el propósito del ejercicio.

Tres líneas suelen sorprender a los lectores: que `nan` se rechace en lugar de almacenarse, que `PS-7` no supere el patrón del identificador aunque parezca inofensivo, y que la lectura de cloro de 9,80 mg/L acabe en cuarentena en lugar de en rechazo. Si predijo mal alguna, anote por qué; después añada a la lista de mensajes un caso erróneo propio, como un número de secuencia menor que 102 o un identificador con un espacio al final, y confirme que el validador lo rechaza antes de fiarse del cambio.

### 3.7 Errores frecuentes y límites

- Validar con una lista de bloqueo («rechazar si contiene un punto y coma») en lugar de con una lista de permitidos de lo que es aceptable.
- Usar una coincidencia parcial para los identificadores, de modo que `PS-7`, `XPS-04` o `PS-04-test` pasen.
- Olvidar `nan` y el infinito.
- Descartar en silencio los valores fuera de rango, de modo que un sensor averiado parezca una estación tranquila.
- Actualizar el estado de reproducción antes de que se hayan superado todas las demás comprobaciones: un mensaje autenticado pero mal formado o inverosímil puede entonces bloquear los mensajes legítimos que lo siguen (lo verá en el capítulo 29).
- Escribir pruebas solo para el camino feliz.

La validación protege al receptor de los datos mal formados e inverosímiles. **No** prueba que los datos sean auténticos: un mensaje perfectamente formado y verosímil puede seguir siendo falso. La autenticación se añade en el capítulo 15.

### Ejercicios — capítulo 3

**EX007 — Prediga y después ejecute.** *Objetivo:* poner a prueba su modelo del orden de validación. *Entradas:* el Lab 3. *Restricciones:* escriba las predicciones antes de ejecutar. *Pasos:* (1) añada tres mensajes: `PS-04|LEVEL_M|inf|1789999999|103`, `PS-04|LEVEL_M|12.0|1789999999|103`, `PS-04|LEVEL_M|-0.0|1789999999|104`; (2) prediga cada resultado; (3) ejecute y explique cualquier sorpresa. *Evidencia esperada:* predicciones, salida y explicación. *Rúbrica:* 3 = inf rechazado por no finito, 12.0 aceptado (límite inclusivo), -0.0 aceptado porque −0,0 es igual a 0,0 y la secuencia avanzó, con un comentario sobre si −0,0 debería normalizarse; 2 = resultados correctos, explicación escasa; 1 = no se ejecutó; 0 = nada.

**EX008 — Diseño de la cuarentena.** *Objetivo:* diseñar el camino de cuarentena. *Entradas:* el capítulo 3 («Rechazar, poner en cuarentena, aceptar») y el caso del cloro de PS-07. *Restricciones:* no se requiere código. *Pasos:* (1) indique dónde se almacenan los mensajes en cuarentena y durante cuánto tiempo; (2) indique quién los revisa, con qué rapidez y qué desencadena el escalado a Operaciones de Agua; (3) indique qué debe mostrar la pantalla del operador mientras un valor está en cuarentena. *Evidencia esperada:* diseño de media página. *Rúbrica:* 3 = almacén separado con conservación, revisor nombrado y tiempo de respuesta, regla de escalado ligada al proceso físico (por ejemplo, dos lecturas de cloro inverosímiles consecutivas → llamar a la sala de control), la pantalla muestra «valor retenido: en revisión» en lugar del último valor bueno como si fuera actual; 2 = falta un elemento; 1 = «lo comprueba un administrador»; 0 = nada.

**EX009 — Falle de forma cerrada.** *Objetivo:* encontrar un camino que falla de forma abierta. *Entradas:* este fragmento: `try: v = float(val) except: pass; if v > hi: return "quarantine"; return "accept"`. *Restricciones:* identifique, explique y corrija. *Pasos:* (1) muestre una entrada para la que devuelve accept erróneamente; (2) explíquelo; (3) reescríbalo. *Evidencia esperada:* entrada, explicación y código corregido. *Rúbrica:* 3 = muestra que un valor no numérico deja `v` sin asignar o con un valor antiguo (un `NameError` en el primer mensaje, o el valor del mensaje anterior reutilizado después), señala la falta de límite inferior y el `except` desnudo, y lo reescribe para devolver rechazo ante cualquier fallo de interpretación, con ambos límites y una comprobación de finitud; 2 = encuentra un problema; 1 = vago; 0 = nada.

### Síntesis del capítulo

El código pequeño decide lo que ven los operadores. Trate cada mensaje como no confiable, valídelo por capas (estructura, identidad, tipo, significado físico, tiempo, orden) y dé a los datos dudosos un camino de cuarentena, de modo que los fallos no se oculten ni se almacenen como verdad. Mantenga las decisiones en funciones pequeñas que puedan probarse, haga explícito el estado, falle de forma cerrada y pruebe primero los casos erróneos. La validación no es autenticación; esta llega más adelante.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Siga estudiando — capítulo 03 de 30

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Modelos de datos

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- modelar registros operativos (activos, responsables, estado del soporte) como tablas relacionadas mediante claves;
- usar **restricciones** para que la base de datos rechace los registros que no pueden ser ciertos;
- escribir consultas que respondan a preguntas operativas («¿qué activos críticos no tienen responsable?») en lugar de producir listas;
- explicar por qué un valor ausente (`NULL`) es información y debe tratarse de forma deliberada.

Todos los capítulos posteriores dependen de registros: inventarios, registros de flujos de datos, registros de riesgos, listas de acceso, registros de evidencia. Cuando viven en hojas de cálculo que editan muchas personas, se degradan: filas duplicadas, responsables en texto libre, «pendiente» en campos de fecha. Este capítulo muestra el modelado de datos mínimo que necesita un implementador para que los registros operativos sigan siendo fiables.

### 4.1 Entidades, atributos y claves

Un **modelo de datos** indica qué tipos de cosas describen los registros (**entidades**: activo, responsable, contrato de soporte), qué se registra de cada una (**atributos**: modelo, firmware, emplazamiento, criticidad) y cómo se relacionan. Cada entidad tiene una **clave primaria**, un valor que identifica exactamente un registro, como una etiqueta de activo. Una **clave foránea** en una tabla apunta a la clave primaria de otra: el `owner_id` de un activo hace referencia a una fila de la tabla de responsables. Esa única decisión de diseño sustituye los nombres de responsable en texto libre, que se desvían («Water Ops», «water operations», «A. Okafor (left)»), por una referencia que o bien apunta a un responsable real o bien no.

### 4.2 Restricciones: hacer imposibles los registros imposibles

Una **restricción** es una regla que la base de datos aplica en cada escritura. `NOT NULL` indica que debe haber un valor; `CHECK (criticality BETWEEN 1 AND 3)` indica que solo se permiten esos valores; una clave foránea indica que la fila referenciada debe existir (en SQLite, la aplicación de las claves foráneas debe activarse en cada conexión, un detalle que conviene conocer porque sorprende a la gente). Las restricciones trasladan la validación de «alguien debería comprobarlo» a «el sistema se niega». Son la validación de entradas del capítulo 3 aplicada a los registros. En el Lab 4, la última consulta es exactamente esto: insertar un activo con criticidad 7 falla en la base de datos, sea quien sea quien haya escrito el script.

### 4.3 Los valores ausentes son hallazgos

En un inventario, un valor ausente no es un blanco; es la afirmación de que algo se desconoce. Un activo sin responsable es un activo que nadie parcheará, revisará ni dará de baja. Un activo con firmware desconocido es uno cuyas vulnerabilidades no pueden evaluarse. Por tanto, las consultas deben buscar *expresamente* los valores ausentes, no ignorarlos. El `NULL` de SQL se comporta de forma especial: `owner_id = NULL` nunca es verdadero; hay que escribir `owner_id IS NULL`. Muchos errores silenciosos en los informes nacen de olvidarlo. El activo de criticidad 1 sin responsable del Lab 4, la RTU de PS-09, solo aparece porque la consulta lo busca.

### 4.4 Las combinaciones responden a las preguntas reales

Las preguntas operativas suelen abarcar varias tablas. «¿Qué activos funcionan con un modelo cuyo soporte del proveedor ha terminado?» requiere combinar la tabla de activos con la de soporte por el modelo. «¿Cuántos activos de criticidad 1 tiene cada responsable?» requiere combinar activos y responsables con una **combinación externa izquierda** (*left join*), para que los activos sin responsable aparezcan como "(none)" en lugar de desaparecer del recuento. La diferencia entre una combinación interna y una externa izquierda suele ser la diferencia entre un informe que oculta un problema y uno que lo muestra.

### 4.5 Ejemplo resuelto: extracto del inventario de FSTS (sintético)

El Lab 4 construye un inventario pequeño en una base de datos SQLite en memoria (el módulo `sqlite3` de Python, [documentation](https://docs.python.org/3/library/sqlite3.html)) y plantea cinco preguntas. Cada respuesta permite actuar. La RTU de PS-09 no tiene responsable, es de criticidad 1 y el soporte del proveedor para su modelo terminó el 2025-12-31: tres motivos para actuar sobre el mismo activo, que una hoja de cálculo ordenada por emplazamiento nunca habría reunido. El conmutador de la estación PS-04 tiene firmware desconocido. Dos servidores ejecutan versiones de sistema operativo que figuran en la lista propia de FSTS de retirada obligatoria por política. La consulta de criticidad por responsable muestra un activo de criticidad 1 que no pertenece a nadie. Por último, la restricción `CHECK` rechaza un intento de insertar un activo con criticidad 7.

### 4.6 Actividad práctica: consultas al inventario

**Lab 4** (guárdelo como `lab04.py` y ejecútelo con `python3 lab04.py`):

```python
# Lab 4 - an asset inventory as a relational model (offline, standard library only: sqlite3)
# Synthetic: Fallowmere Shared Technology Services inventory extract.
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE owner(id INTEGER PRIMARY KEY, name TEXT NOT NULL, service TEXT NOT NULL);
CREATE TABLE asset(id TEXT PRIMARY KEY, kind TEXT NOT NULL, model TEXT, firmware TEXT,
  site TEXT NOT NULL, owner_id INTEGER REFERENCES owner(id), criticality INTEGER CHECK (criticality BETWEEN 1 AND 3));
CREATE TABLE support(model TEXT PRIMARY KEY, vendor_end TEXT);
INSERT INTO owner VALUES (1,'Water Ops','drinking water'),(2,'Clinical Eng','hospital'),(3,'Depot IT','transit');
INSERT INTO asset VALUES
 ('PS04-PLC','plc','Arlen 300','4.2','PS-04',1,1),('PS07-PLC','plc','Arlen 300','3.9','PS-07',1,1),
 ('PS09-RTU','rtu','Kell R2','1.1','PS-09',NULL,1),('RLY-01','server','generic x86','deb12','Hub',1,1),
 ('HIST-01','server','generic x86','win2016','Hub',1,2),('INF-PUMP-12','infusion','Moro IP5','2.0','Ward 3',2,1),
 ('PACS-GW','server','generic x86','win2012r2','Hospital',2,2),('DEPOT-KIOSK','kiosk','Tella K1','8.1','Depot',3,3),
 ('SW-STN-04','switch','Brack 24',NULL,'PS-04',1,2);
INSERT INTO support VALUES ('Arlen 300','2027-06-30'),('Kell R2','2025-12-31'),('Moro IP5','2029-01-01'),('Tella K1','2026-03-31');
""")
q = {
 "no owner": "SELECT id, site FROM asset WHERE owner_id IS NULL",
 "unknown firmware": "SELECT id, site FROM asset WHERE firmware IS NULL",
 "vendor support ended (as of 2026-10-12)":
   "SELECT a.id, s.vendor_end FROM asset a JOIN support s ON a.model=s.model WHERE s.vendor_end < '2026-10-12'",
 "OS on the service's retire-by-policy list (synthetic)": "SELECT id, firmware FROM asset WHERE firmware IN ('win2012r2','win2016')",
 "criticality-1 assets by owner": """SELECT COALESCE(o.name,'(none)'), COUNT(*) FROM asset a LEFT JOIN owner o
   ON a.owner_id=o.id WHERE a.criticality=1 GROUP BY o.name ORDER BY 2 DESC""",
}
for title, sql in q.items():
    print(f"-- {title}")
    for row in db.execute(sql):
        print("  ", row)
try:
    db.execute("INSERT INTO asset VALUES ('X','plc','m','1','PS-01',1,7)")
except sqlite3.IntegrityError as e:
    print("constraint rejected bad row:", e)
```

Salida esperada (Python 3.13.5):

```text
-- no owner
   ('PS09-RTU', 'PS-09')
-- unknown firmware
   ('SW-STN-04', 'PS-04')
-- vendor support ended (as of 2026-10-12)
   ('PS09-RTU', '2025-12-31')
   ('DEPOT-KIOSK', '2026-03-31')
-- OS on the service's retire-by-policy list (synthetic)
   ('HIST-01', 'win2016')
   ('PACS-GW', 'win2012r2')
-- criticality-1 assets by owner
   ('Water Ops', 3)
   ('Clinical Eng', 1)
   ('(none)', 1)
constraint rejected bad row: CHECK constraint failed: criticality BETWEEN 1 AND 3
```

Lea la salida como una lista de trabajo y no como un informe. La RTU de PS-09 es la primera línea de trabajo, porque en un mismo activo coinciden tres hallazgos: sin responsable, criticidad 1 y soporte del proveedor terminado el 2025-12-31. El firmware desconocido del conmutador de la estación PS-04 se convierte en una pregunta para el ingeniero de Agua, no en una suposición. Los dos servidores de la lista de retirada obligatoria de FSTS pasan al responsable de la plataforma con sus fechas de sustitución. Por último, compruebe la inserción rechazada: si la fila de criticidad 7 se hubiera aceptado, la aplicación de las claves foráneas y de `CHECK` no estaba activa en esa conexión, y todas las respuestas anteriores merecerían menos confianza.

### 4.7 Errores frecuentes y límites

- Campos de texto libre para cualquier cosa que debería hacer referencia a otro registro (responsables, emplazamientos, modelos).
- Comparar con `= NULL`, de modo que los valores ausentes quedan excluidos en silencio.
- Combinaciones internas en los informes de cobertura, que eliminan precisamente los registros con vínculos ausentes.
- Almacenar fechas como texto libre en formatos mezclados, de modo que las comparaciones ordenan mal; almacene ISO 8601 (`YYYY-MM-DD`), que se ordena correctamente como texto.
- Creer que la base de datos es la verdad. Solo es tan buena como el proceso de descubrimiento y actualización que la respalda (capítulo 11).

Un modelo de datos no puede decirle que un activo existe si nadie lo registró. Puede asegurar que lo registrado es coherente y que las lagunas son visibles.

### Ejercicios — capítulo 4

**EX010 — Encuentre el activo oculto.** *Objetivo:* ver cómo una combinación interna oculta un problema. *Entradas:* el Lab 4. *Restricciones:* cambie solo la última consulta. *Pasos:* (1) cambie `LEFT JOIN` por `JOIN` en la consulta de criticidad por responsable; (2) ejecute y compare; (3) explique en dos frases qué activo desapareció y por qué importa en un informe de cobertura. *Evidencia esperada:* ambas salidas y la explicación. *Rúbrica:* 3 = desaparece la fila de PS09-RTU, el recuento total de criticidad 1 baja de 5 a 4, la explicación lo relaciona con activos sin responsable que desaparecen de los informes de gestión; 2 = lo observa, explicación débil; 1 = no se ejecutó; 0 = nada.

**EX011 — Añada una restricción y una tabla.** *Objetivo:* ampliar el modelo de forma segura. *Entradas:* el Lab 4. *Restricciones:* solo la biblioteca estándar. *Pasos:* (1) añada una tabla `review` (id del activo, fecha de revisión, revisor, resultado) con una clave foránea a asset y un `CHECK` de que el resultado es `ok`, `issue` o `not-reachable`; (2) active las claves foráneas con `PRAGMA foreign_keys = ON`; (3) muestre que insertar una revisión de un activo inexistente falla; (4) escriba una consulta que liste los activos de criticidad 1 sin revisión en los últimos 90 días. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = restricción y clave foránea aplicadas, la consulta usa una combinación externa izquierda o `NOT EXISTS` para que aparezcan los activos nunca revisados; 2 = funciona pero omite los activos nunca revisados; 1 = solo el esquema; 0 = nada.

**EX012 — De la hoja de cálculo al modelo.** *Objetivo:* reconocer fallos de calidad de datos. *Entradas:* un conjunto sintético de filas de hoja de cálculo: `PS-03 PLC | owner: Water Ops | fw: 4.2 | support: Jun 2027`; `PS-03 plc | owner: water operations | fw: ? | support: 30/06/27`; `PS-05 PLC | owner: A. Okafor (left) | fw: 4.1 | support: TBC`. *Restricciones:* no se necesita código. *Pasos:* (1) enumere todos los fallos de calidad de datos; (2) indique qué restricción o decisión de diseño de las pautas del capítulo 4 sobre claves, restricciones y valores ausentes evita cada uno. *Evidencia esperada:* tabla. *Rúbrica:* 3 = activo duplicado con mayúsculas incoherentes, variantes de responsable en texto libre, una persona en lugar de una función como responsable y además una baja, firmware desconocido como "?", formatos de fecha mezclados, "TBC"; cada uno asignado a clave primaria, clave foránea, NOT NULL/desconocido explícito o fechas ISO; 2 = la mayoría encontrados; 1 = pocos; 0 = nada.

### Síntesis del capítulo

Los registros operativos solo son útiles si se mantienen coherentes. Modélelos como entidades con claves, vincúlelos con claves foráneas en lugar de texto libre y deje que las restricciones rechacen los registros imposibles. Trate los valores ausentes como hallazgos, búsquelos expresamente y use combinaciones externas izquierdas en cualquier informe de cobertura. Un buen modelo hace visibles las lagunas; no puede encontrar activos que nadie registró.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Siga estudiando — capítulo 04 de 30

[← Capítulo 03](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Alfabetización en seguridad

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- usar el vocabulario básico (activo, amenaza, vulnerabilidad, exposición, control, riesgo, incidente, evidencia) de forma precisa y coherente;
- explicar en qué se diferencian las prioridades de seguridad de un servicio esencial de las de una oficina corriente: la **disponibilidad y la seguridad física** del servicio suelen ir primero;
- describir un control por lo que **previene, detecta o ayuda a recuperar**, y por la evidencia de que funciona;
- leer un informe público de incidente para extraer sus lecciones sin convertirlo en una técnica.

Los capítulos 1 a 4 trataban de informática. Este capítulo aporta el lenguaje común que usará con operadores, directivos, auditores y proveedores durante el resto del libro. Las palabras imprecisas causan fallos reales: «el PLC es seguro» no significa nada; «el PLC acepta escrituras solo desde la subred del retransmisor, verificado mediante una revisión de flujos el 3 de octubre» significa algo.

### 5.1 Términos básicos

- **Activo**: cualquier cosa de valor para el servicio: un controlador de bomba, un historiador, una credencial, un conjunto de datos, el conocimiento de una persona.
- **Amenaza**: una causa potencial de daño: un grupo criminal, un cambio descuidado, una inundación, un proveedor que falla.
- **Vulnerabilidad**: una debilidad que una amenaza podría aprovechar: un fallo sin parchear, una contraseña compartida, un camino no documentado, una copia de seguridad sin probar.
- **Exposición**: si una amenaza puede alcanzar realmente la vulnerabilidad. Un fallo sin parchear en un dispositivo aislado está menos expuesto que el mismo fallo alcanzable desde internet.
- **Control**: una medida que reduce el riesgo: técnica (una regla de cortafuegos), de procedimiento (una aprobación de cambios) o física (un armario cerrado con llave).
- **Riesgo**: la combinación de lo probable que es un daño y lo grave que sería, para las personas que dependen del servicio. El capítulo 13 lo concreta.
- **Incidente**: un suceso que realmente daña, o amenaza con dañar, la confidencialidad, la integridad o la disponibilidad o, en la infraestructura crítica, la seguridad física.
- **Evidencia**: un registro que permite a alguien distinto de usted comprobar una afirmación.

El Marco de Ciberseguridad 2.0 del NIST organiza los resultados en Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar ([NIST CSWP 29](https://doi.org/10.6028/NIST.CSWP.29)); es un mapa útil del territorio, no una lista de casillas que marcar.

### 5.2 Prioridades en un servicio esencial

La seguridad de la TI de oficina suele describirse en términos de confidencialidad, integridad y disponibilidad, con la confidencialidad en primer lugar. En una red de agua, un hospital o un sistema de transporte, el orden cambia. La primera preocupación suele ser que el servicio físico continúe y que nadie sufra daños; la integridad de los datos de control y de medición le sigue de cerca (un operador que actúa sobre una lectura falsa puede causar daños); la confidencialidad importa (historias clínicas, datos de clientes, diagramas de red), pero rara vez justifica una interrupción. La guía de TO del NIST analiza en qué se diferencian estas prioridades en la tecnología operativa ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

Esto tiene consecuencias prácticas para un implementador. Un control que podría detener un proceso (un bloqueo automático en una estación de trabajo de operador, un reinicio forzado para aplicar un parche) necesita en TO una aprobación y un momento distintos que en una oficina. Un control que en TI falla «cerrado» puede necesitar fallar «abierto» en un sistema relevante para la seguridad física, y esa elección deben tomarla deliberadamente personas que entienden el proceso, no venir por defecto en la configuración de un proveedor.

### 5.3 Prevenir, detectar, recuperar

Clasificar los controles por su función ayuda a ver las lagunas. Los controles **preventivos** impiden que algo ocurra (autenticación, segmentación, listas de permitidos). Los controles **detectivos** advierten que está ocurriendo (alertas, comprobaciones de integridad, revisiones). Los controles **correctivos** o **de recuperación** restablecen el servicio (copias de seguridad, equipos de repuesto, procedimientos de operación manual). Un servicio protegido solo por controles preventivos no tiene forma de advertir cuándo fallan; uno con solo controles detectivos advierte el daño sin poder detenerlo ni deshacerlo. Todo riesgo importante debería tener al menos un control de cada tipo, y todo control debería tener una pieza de **evidencia** declarada que muestre que funciona, no solo que está configurado.

### 5.4 Leer incidentes públicos

Los informes públicos de incidentes son el mejor material didáctico de que dispone el sector, si se leen correctamente. Léalos en busca de **supuestos fallidos** y **lecciones**: ¿qué creía el operador que no era cierto? El aviso de CISA sobre el suceso de 2021 en la planta de tratamiento de agua de Oldsmar (Florida) describió el software de acceso remoto, las contraseñas compartidas y un sistema conectado a internet como condiciones que había que corregir ([CISA AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a)); un antiguo responsable municipal declaró más tarde que el suceso fue probablemente un error de un empleado y no una intrusión ([WUSF, 13 April 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)). Ambos relatos enseñan la misma lección al implementador: el acceso remoto a un sistema de control con credenciales compartidas y un registro deficiente hace imposible saber después qué ocurrió. Fíjese también en la lección sobre la evidencia: un primer relato puede revisarse.

### 5.5 Ejemplo resuelto: reescribir afirmaciones vagas (sintético)

Un informe de situación de FSTS dice: «LANTERN es seguro. Los cortafuegos están instalados. Las copias de seguridad se hacen. La monitorización está activa». Reescrito con el vocabulario de este capítulo, y con evidencia:

| Afirmación vaga | Afirmación precisa | Evidencia |
|---|---|---|
| «LANTERN es seguro» | (no es una afirmación utilizable; elimínela) | — |
| «Los cortafuegos están instalados» | Las estaciones aceptan Modbus solo desde la subred del retransmisor (preventivo). | Revisión de flujos del 3 de oct.; se encontró y cerró un camino no declarado de la zona corporativa a PS-04 (CHG-121). |
| «Las copias de seguridad se hacen» | Las configuraciones del retransmisor y del historiador se copian cada noche; los datos del historiador, cada semana (recuperación). | Última prueba de restauración el 28 de sept.: historiador restaurado en 3 h 10 min frente a un objetivo de 4 h. |
| «La monitorización está activa» | Las ráfagas de inicios de sesión fallidos, el Modbus de la zona corporativa a las estaciones y el silencio de una estación generan alertas (detectivo). | Pruebas de reglas del 1 de oct.: 12/12, 7/10, 8/8 detectadas (capítulo 23). |

### 5.6 Actividad práctica: una ficha de control

Elija un control de LANTERN de los capítulos 2 a 4 (por ejemplo, el validador de mensajes). Escriba una **ficha de control** de una página: nombre; riesgo que aborda; tipo (prevenir / detectar / recuperar); dónde se implementa; responsable; cómo podría fallar; evidencia de que funciona; fecha de la última evidencia. Ampliará estas fichas en el capítulo 18. Para el validador de mensajes, una ficha completa dice: riesgo, mensajes de estación falsificados, reproducidos o mal formados que llegan al historiador; tipo, prevenir; implementado en la ruta de entrada del retransmisor; responsable, FSTS Platform; podría fallar si el estado de reproducción se pierde al reiniciar o si la lista de permitidos va por detrás de una estación nueva como PS-11; evidencia, las tres aceptaciones, seis rechazos y dos cuarentenas del Lab 3, más los recuentos de rechazos del retransmisor; última evidencia, la fecha de la ejecución más reciente.

### 5.7 Errores frecuentes y límites

- Usar «seguro» como un estado en lugar de describir protecciones concretas y su evidencia.
- Tratar la confidencialidad como la máxima prioridad en un sistema de control y aceptar el riesgo de interrupción para protegerla.
- Contar controles en lugar de preguntar qué previene, detecta o recupera cada uno.
- Leer los informes de incidentes como guías prácticas, o repetir un primer relato después de que se haya revisado.
- Llamar incidente a cualquier suceso, lo que agota a quienes responden; o no llamar incidente a nada, lo que retrasa la respuesta.

Tres de estos errores aparecen en el informe de situación de este capítulo antes de reescribirse. «LANTERN es seguro» es el primero. «Los cortafuegos están instalados» cuenta un control sin decir que hubo que cerrar un camino no declarado de la zona corporativa a PS-04 con el cambio CHG-121. «La monitorización está activa» ocultaba que la regla B solo detectó 7 de 10 pruebas.

### Ejercicios — capítulo 5

**EX013 — Precisión terminológica.** *Objetivo:* usar el vocabulario correctamente. *Entradas:* la frase «La cuenta del proveedor es una amenaza porque la RTU es un riesgo sin control». *Restricciones:* reescríbala en no más de tres frases. *Pasos:* (1) identifique cada término mal usado; (2) reescríbala correctamente usando activo, vulnerabilidad, exposición, amenaza y control. *Evidencia esperada:* texto reescrito con una nota de una línea por corrección. *Rúbrica:* 3 = la cuenta del proveedor se identifica como vulnerabilidad o vía de exposición (no como amenaza), la RTU como activo, el riesgo se describe como probabilidad y consecuencia, se nombra un control concreto que falta; 2 = casi todo correcto; 1 = cambios cosméticos; 0 = nada.

**EX014 — Prevenir, detectar, recuperar.** *Objetivo:* ver las lagunas de control por función. *Entradas:* el riesgo «un cambio de configuración en el retransmisor hace que se descarten datos de las estaciones». *Restricciones:* un control por función, implementable por FSTS. *Pasos:* (1) proponga un control preventivo, uno detectivo y uno de recuperación; (2) indique para cada uno la evidencia de que funciona. *Evidencia esperada:* tabla de tres filas. *Rúbrica:* 3 = por ejemplo, aprobación de cambios con revisión por pares (prevenir), alerta de integridad de archivos y alerta de silencio de estación (detectar), configuración versionada con vuelta atrás probada (recuperar), cada uno con evidencia comprobable; 2 = uno débil; 1 = todos preventivos; 0 = nada.

**EX015 — Lectura de un informe de incidente.** *Objetivo:* extraer lecciones para el implementador de una fuente pública. *Entradas:* CISA AA21-042A y el artículo de WUSF. *Restricciones:* solo lecciones; ninguna técnica de ataque. *Pasos:* (1) enumere tres condiciones que el aviso recomendaba corregir; (2) indique qué cambia el relato posterior y qué no; (3) escriba una regla de diseño de LANTERN que respalde cada lección. *Evidencia esperada:* nota de media página que cite ambas fuentes. *Rúbrica:* 3 = condiciones como el software de acceso remoto, las credenciales compartidas y la exposición a internet extraídas correctamente del aviso; reconoce que la revisión cambia la atribución, no el valor de las lecciones de higiene; las reglas de diseño son concretas; 2 = un elemento débil; 1 = repite el primer relato como un hecho establecido; 0 = nada.

### Síntesis del capítulo

El vocabulario preciso es un control de seguridad: hace comprobables las afirmaciones. En los servicios esenciales, la continuidad y la seguridad física del servicio suelen ir primero, lo que cambia cómo se eligen los controles, cuándo se aplican y cómo se les permite fallar. Describa cada control por lo que previene, detecta o recupera, y por la evidencia de que funciona. Lea los incidentes públicos en busca de supuestos fallidos y siga sus revisiones.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Siga estudiando — capítulo 05 de 30

[← Capítulo 04](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operativos y virtualización

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- bastionar un servidor eliminando lo que no necesita y restringiendo lo que sí necesita;
- ejecutar un servicio con una cuenta dedicada y sin privilegios, con solo los archivos y puertos que necesita;
- construir y usar una **línea base de integridad de archivos** para detectar cambios no aprobados;
- explicar qué cambia la virtualización para la seguridad, y qué no cambia.

Los retransmisores y el historiador de LANTERN son servidores corrientes. La mayoría de los compromisos de este tipo de servidores, y muchas interrupciones, no proceden de fallos exóticos, sino de cosas que se dejaron en ellos: un servicio sin usar que escucha en todas las interfaces, una opción de depuración, un archivo con permiso de escritura para todos, una cuenta antigua. Este capítulo trata de mantener un servidor pequeño, conocido y comprobable.

### 6.1 El bastionado como sustracción

**Bastionar** significa reducir un sistema a lo que exige su función y configurar de forma segura lo que queda. La guía de seguridad de servidores del NIST recomienda eliminar o desactivar los servicios, aplicaciones y protocolos de red innecesarios, configurar la autenticación y los controles de recursos, y mantener el sistema parcheado y monitorizado ([NIST SP 800-123](https://csrc.nist.gov/pubs/sp/800/123/final)). Para un retransmisor, eso significa: ningún entorno de escritorio, ningún compilador, ningún servicio de compartición de archivos, SSH escuchando solo en la interfaz de gestión, el proceso del retransmisor escuchando solo en su dirección y puerto declarados, y nada escuchando en `0.0.0.0` sin un motivo por escrito.

### 6.2 Cuentas de servicio y mínimo privilegio

Ejecute cada servicio con su propia cuenta sin privilegios (`relay`, no `root`). Dé a esa cuenta acceso de lectura a su configuración, acceso de escritura solo a sus propios directorios de datos y de registros, y ningún inicio de sesión con intérprete de órdenes. Use el gestor de servicios del sistema operativo para reiniciarlo si falla y para aplicar restricciones adicionales (por ejemplo, una vista de solo lectura de la mayor parte del sistema de archivos). Si el proceso del retransmisor llega a verse comprometido, estas decisiones determinan si el atacante controla un servicio o el equipo entero. En RLY-01, esta es la definición del servicio cuyos permisos cambiaron a `0666`.

### 6.3 Los archivos de configuración son relevantes para la seguridad

En un retransmisor, los archivos más relevantes para la seguridad son su configuración (en qué escucha, a dónde reenvía, dónde está su clave), su lista de estaciones permitidas y su definición de servicio (con qué cuenta se ejecuta y con qué restricciones). Un cambio en cualquiera de ellos cambia la seguridad del servicio. Los permisos de los archivos importan tanto como su contenido: una definición de servicio que se ha vuelto modificable por cualquier usuario permite a cualquier usuario local decidir qué se ejecuta como el servicio. RLY-01 mostró ambos tipos: un cambio de contenido, `debug_listen 0.0.0.0:9000`, y un cambio de permisos a `0666`.

### 6.4 Líneas base de integridad de archivos

Una **línea base de integridad de archivos** registra un hash criptográfico y los permisos de cada archivo importante en un momento conocido como correcto. Las instantáneas posteriores se comparan con ella; cada diferencia o bien se explica mediante un registro de cambio aprobado, o bien se investiga. SHA-256, especificado en [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final), es una elección estándar: cualquier cambio en el contenido del archivo cambia su resumen. La propia línea base debe protegerse (almacenada fuera del equipo o firmada), porque un atacante que puede cambiar un archivo y también la línea base puede ocultar el cambio.

### 6.5 Virtualización

La virtualización ejecuta varios sistemas operativos en un único equipo físico mediante un **hipervisor**. Ayuda a la operación (instantáneas, reconstrucciones rápidas, invitados separados para funciones separadas) y crea cosas nuevas que proteger. La guía del NIST sobre virtualización completa señala que el hipervisor y sus interfaces de gestión se convierten en objetivos de alto valor, y que los invitados de un mismo equipo comparten recursos físicos y pueden afectarse entre sí ([NIST SP 800-125](https://csrc.nist.gov/pubs/sp/800/125/final)). Consecuencias prácticas: la red de gestión del hipervisor es una zona propia; quien administra el hipervisor administra en la práctica todos los invitados; las instantáneas contienen secretos y deben protegerse como las copias de seguridad; y colocar en el mismo equipo un retransmisor orientado a las estaciones y un servidor de informes orientado a la zona corporativa une dos zonas mediante hardware compartido y un administrador compartido.

### 6.6 Ejemplo resuelto: una línea base detecta un puerto de depuración (sintético)

Usted crea la línea base de los tres archivos de configuración de RLY-01. Una semana después, la comparación muestra cuatro diferencias. La lista de permitidos ganó `PS-11` con el cambio aprobado CHG-118: explicado. La configuración del retransmisor ganó `debug_listen 0.0.0.0:9000` sin registro de cambio: alguien habilitó un puerto de depuración en todas las interfaces, quizá mientras resolvía un problema, y lo dejó así. Los permisos de la definición del servicio pasaron de `0640` a `0666`: cualquier usuario local puede ahora reescribirla. Apareció un archivo nuevo, `helper.sh`, en el directorio de unidades. Tres cambios no aprobados en un equipo crítico son una investigación, no una limpieza: antes de revertir nada, conserve los archivos actuales y la salida de la comparación, y pregunte quién cambió qué (capítulo 20).

### 6.7 Actividad práctica: línea base de integridad de archivos

**Lab 6** (guárdelo como `lab06.py` y ejecútelo con `python3 lab06.py`):

```python
# Lab 6 - a file-integrity baseline for the relay host's configuration (offline, standard library only)
# Synthetic files are created in a temporary directory; nothing outside it is read or changed.
import hashlib, json, os, tempfile
def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()
def snapshot(root):
    out = {}
    for d, _, files in os.walk(root):
        for name in sorted(files):
            p = os.path.join(d, name)
            st = os.stat(p)
            out[os.path.relpath(p, root)] = {"sha256": digest(p), "mode": oct(st.st_mode & 0o777)}
    return out
with tempfile.TemporaryDirectory() as root:
    files = {"relay.conf": "listen 10.30.0.5:8443\nupstream hist-01:443\nhmac_key_file /etc/relay/key\n",
             "allow.list": "PS-04\nPS-07\nPS-09\n", "units/relay.service": "[Service]\nUser=relay\n"}
    for rel, text in files.items():
        p = os.path.join(root, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as f: f.write(text)
        os.chmod(p, 0o640)
    base = snapshot(root)
    print("baseline entries:", len(base), "| relay.conf", base["relay.conf"]["sha256"][:16])
    # simulated changes: one approved (change ticket CHG-118), one not, one permission change, one new file
    with open(os.path.join(root, "allow.list"), "a") as f: f.write("PS-11\n")
    with open(os.path.join(root, "relay.conf"), "a") as f: f.write("debug_listen 0.0.0.0:9000\n")
    os.chmod(os.path.join(root, "units/relay.service"), 0o666)
    with open(os.path.join(root, "units/helper.sh"), "w") as f: f.write("#!/bin/sh\n")
    approved = {"allow.list": "CHG-118"}
    now = snapshot(root)
    for rel in sorted(set(base) | set(now)):
        b, n = base.get(rel), now.get(rel)
        if b == n: continue
        kind = "added" if b is None else "removed" if n is None else "content" if b["sha256"] != n["sha256"] else "mode " + b["mode"] + "->" + n["mode"]
        print(f"{rel:<20} {kind:<16} {'approved ' + approved[rel] if rel in approved else 'UNAPPROVED - investigate'}")
    print("baseline json bytes:", len(json.dumps(base, sort_keys=True)))
```

Salida esperada (Python 3.13.5):

```text
baseline entries: 3 | relay.conf 1defd9289ede0120
allow.list           content          approved CHG-118
relay.conf           content          UNAPPROVED - investigate
units/helper.sh      added            UNAPPROVED - investigate
units/relay.service  mode 0o640->0o666 UNAPPROVED - investigate
baseline json bytes: 342
```

El script crea sus archivos en un directorio temporal, así que puede ejecutarlo en cualquier sitio. Observe que el resumen impreso para `relay.conf` depende solo del contenido del archivo: si cambia un carácter del contenido sintético en el script, el resumen cambia por completo.

Compare la salida con la semana de RLY-01 descrita arriba: cuatro diferencias, de las que solo la entrada `PS-11` de la lista de permitidos, con CHG-118, tiene registro de cambio. Después haga una modificación propia dentro del script, por ejemplo añadir una segunda línea de depuración o cambiar un modo de `0640` a `0644`, vuelva a ejecutarlo y confirme que la comparación informa exactamente de esa diferencia y de nada más. Una línea base que informa de más o de menos de lo que usted cambió todavía no es lo bastante fiable para servir de evidencia en una investigación.

### 6.8 Errores frecuentes y límites

- Bastionar una vez al construir el sistema y no volver a comprobarlo nunca.
- Ejecutar servicios como root «porque así era más fácil que funcionara».
- Guardar la línea base de integridad en el mismo equipo, modificable por los mismos administradores.
- Alertar de cada cambio de archivo en un sistema con mucha actividad, de modo que las alertas se ignoran; cree la línea base de los archivos que importan.
- Tratar una instantánea como una copia de seguridad sin probar la restauración, o dejar sin proteger instantáneas que contienen claves.
- Alojar invitados de zonas distintas en un mismo hipervisor sin registrar que esas zonas comparten ahora un fallo y un administrador.

La integridad de archivos detecta cambios; no le dice si el cambio fue malicioso, y no dice nada de los cambios en memoria ni en archivos que no incluyó en la línea base.

### Ejercicios — capítulo 6

**EX016 — Revisión de bastionado.** *Objetivo:* aplicar el bastionado como sustracción. *Entradas:* un listado sintético de RLY-02: escucha en `0.0.0.0:22`, `10.30.0.6:8443`, `0.0.0.0:9000`, `0.0.0.0:111`; los paquetes instalados incluyen un compilador y un entorno de escritorio; el retransmisor se ejecuta como `root`. *Restricciones:* proponga solo cambios; cada uno necesita un motivo. *Pasos:* (1) enumere todos los cambios; (2) marque cuáles necesitan una solicitud de cambio y cuáles pueden hacerse en el próximo cambio estándar. *Evidencia esperada:* tabla. *Rúbrica:* 3 = SSH limitado a la interfaz de gestión, eliminado el puerto de depuración 9000, desactivado el puerto 111 (RPC), eliminados el compilador y el escritorio, retransmisor trasladado a una cuenta sin privilegios con restricciones; clasificación sensata de los cambios; 2 = la mayoría; 1 = genérico; 0 = nada.

**EX017 — Proteja la línea base.** *Objetivo:* diseñar el almacenamiento de la línea base. *Entradas:* el Lab 6. *Restricciones:* dos diseños. *Pasos:* (1) describa el almacenamiento de la línea base fuera del equipo, en una ubicación de escritura única; (2) describa la firma de la línea base con una clave que no esté en el retransmisor; (3) compare frente a qué protege cada uno. *Evidencia esperada:* media página. *Rúbrica:* 3 = ambos diseños correctos; señala que un atacante con root en el retransmisor puede cambiar archivos pero no puede cambiar sin ser detectado una línea base externa o firmada; señala que la propia herramienta de comparación en el equipo puede subvertirse, así que la comparación debería ejecutarse también desde fuera; 2 = un diseño; 1 = vago; 0 = nada.

**EX018 — Ubicación en el hipervisor.** *Objetivo:* razonar sobre plataformas compartidas. *Entradas:* propuesta de ejecutar RLY-01 (orientado a las estaciones), HIST-01 (orientado a la zona corporativa) y la pasarela clínica del hospital como invitados de un único hipervisor de FSTS para ahorrar costes. *Restricciones:* no la rechace automáticamente; indique condiciones. *Pasos:* (1) enumere lo que las zonas compartirían a partir de entonces; (2) enumere las condiciones con las que la aceptaría; (3) nombre el riesgo residual y su responsable. *Evidencia esperada:* una página. *Rúbrica:* 3 = hardware, administradores del hipervisor, red de gestión y almacenamiento compartidos, y un único punto de fallo para dos sectores; condiciones como zona de gestión separada, grupo de administración restringido con MFA, redes virtuales separadas sin puentes, margen de capacidad documentado y un plan para la pérdida del equipo; riesgo residual asumido por responsables de servicio con nombre; 2 = parcial; 1 = un sí o no sin matices; 0 = nada.

### Síntesis del capítulo

Mantenga los servidores pequeños y conocidos: elimine lo que la función no necesita, ejecute los servicios con cuentas dedicadas sin privilegios, vincule los puertos de escucha a direcciones declaradas y trate los archivos de configuración y sus permisos como relevantes para la seguridad. Cree una línea base de los archivos que importan con un hash criptográfico, proteja esa línea base e investigue cada diferencia sin explicar. La virtualización simplifica la operación, pero concentra el control en el hipervisor y sus administradores; registre qué zonas comparten un equipo.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Siga estudiando — capítulo 06 de 30

[← Capítulo 05](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Fundamentos de identidad y acceso

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- distinguir identificación, autenticación y autorización, y decir qué control actúa en cada paso;
- elegir la robustez de la autenticación según lo que puede hacer una cuenta, no según quién la tiene;
- gestionar los cuatro tipos de cuenta presentes en todo servicio crítico (personales, privilegiadas, de servicio y de proveedor) y las cuentas compartidas que no deberían existir;
- realizar una **revisión de accesos** que compare las cuentas con una plantilla de referencia y una declaración de necesidades.

En los informes de incidentes del capítulo 5, el acceso es un hilo recurrente: acceso remoto con contraseñas compartidas, cuentas de proveedor que nunca se eliminaron. Para un implementador, la identidad no es un producto; es un conjunto de registros y rutinas que deben mantenerse exactos a medida que las personas se incorporan, cambian de puesto y se van.

### 7.1 Identificar, autenticar, autorizar

La **identificación** consiste en declarar una identidad («soy b.lind»). La **autenticación** consiste en demostrarla, con algo que se sabe (una contraseña), que se tiene (una llave de hardware, una aplicación de autenticación) o que se es (un rasgo biométrico). La **autorización** consiste en decidir qué puede hacer esa identidad. Las directrices de identidad digital del NIST describen los tipos de autenticadores y los niveles de garantía, y recomiendan una autenticación multifactor resistente al phishing para los accesos de mayor garantía ([NIST SP 800-63B](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final)). En la práctica: todo acceso privilegiado o remoto a un equipo de LANTERN requiere autenticación multifactor (MFA), y el factor debería resistir el phishing cuando la plataforma lo permita.

### 7.2 Tipos de cuenta

- Las **cuentas personales** pertenecen a una persona y son la opción por defecto para todo ser humano.
- Las **cuentas privilegiadas** pueden cambiar la configuración, las cuentas o los ajustes de seguridad. Deberían estar separadas de la cuenta cotidiana de la persona, exigir MFA y ser pocas.
- Las **cuentas de servicio** las usa el software (el retransmisor que escribe en el historiador). Deberían tener solo los permisos que el software necesita, ningún inicio de sesión interactivo y credenciales que se rotan y se guardan en un lugar protegido, no en un script.
- Las **cuentas de proveedor** dan acceso a un tercero. Deberían estar **limitadas en el tiempo**: habilitadas para un trabajo concreto, vigiladas mientras se usan y deshabilitadas después.
- Las **cuentas compartidas** ("opsuser") las usan varias personas. Destruyen la rendición de cuentas (el registro dice que lo hizo "opsuser") y su contraseña se filtra con cada baja. Cuando un dispositivo realmente no admite cuentas individuales, controle la credencial compartida en una bóveda que registre quién la retiró y cuándo.

### 7.3 El proceso de altas, cambios y bajas

Las cuentas fallan en las transiciones. Una **alta** recibe un acceso copiado de un compañero y hereda privilegios que no necesita. Un **cambio** de puesto conserva el acceso antiguo al obtener el nuevo. Las cuentas de una **baja** siguen habilitadas porque nadie avisó al responsable del sistema. La solución es un proceso vinculado a una fuente de referencia (la plantilla de Recursos Humanos) y una **revisión de accesos** periódica que detecte lo que el proceso no captó. La exportación del Lab 7 muestra los tres fallos: `c.mendes` es una baja cuya cuenta siguió habilitada después del 31 de agosto, `d.reyes` conserva un acceso de administración al historiador que Ingeniería Clínica no necesita, y `vendor-kell` es un acceso permanente de proveedor que nunca se vinculó a una incidencia.

### 7.4 La revisión de accesos

Una revisión de accesos compara tres cosas: las **cuentas** que existen en un sistema (exportadas de él, no de memoria), la **plantilla** de personas y su situación, y una declaración de **necesidades**: qué funciones requiere cada equipo en cada sistema. Los hallazgos son de tipos reconocibles: huérfanas (cuentas sin persona correspondiente), bajas aún habilitadas (peor si se usaron después de la baja), funciones no justificadas, accesos privilegiados sin MFA, cuentas inactivas, cuentas compartidas y accesos permanentes de proveedor. Para RLY-01 y HIST-01, la exportación enumera nueve cuentas y la plantilla le indica que `f.ito` no corresponde a nadie.

### 7.5 Ejemplo resuelto: revisión trimestral de RLY-01 y HIST-01 (sintético)

La exportación tiene nueve cuentas; el Lab 7 encuentra nueve hallazgos repartidos en cinco de ellas. Dos exigen actuar de inmediato, no una incidencia para el próximo trimestre. `c.mendes` se fue el 31 de agosto y la cuenta se **usó el 14 de septiembre**: es un posible incidente, no una limpieza administrativa; conserve los registros, deshabilite la cuenta y averigüe si otra persona usó las credenciales (capítulo 20). `vendor-kell` es una cuenta de administrador permanente en el retransmisor, sin MFA, inactiva desde hace 85 días. Los demás hallazgos son graves pero rutinarios: `d.reyes` tiene acceso de administración al historiador, que Ingeniería Clínica no necesita, sin MFA, y no ha iniciado sesión en 224 días; `opsuser` es un administrador compartido sin MFA; `f.ito` no figura en absoluto en la plantilla: quizá un contratista registrado en otro sitio, quizá una cuenta que nadie sabe explicar.

Fíjese en lo que el script *no* señala: `svc-relay` no tiene MFA, lo que es normal en una cuenta de servicio, pero el almacenamiento y la rotación de su credencial no son visibles en esta exportación y deben comprobarse por separado.

### 7.6 Actividad práctica: revisión de accesos

**Lab 7** (guárdelo como `lab07.py` y ejecútelo con `python3 lab07.py`):

```python
# Lab 7 - quarterly access review for the relay and historian (offline, standard library only)
# Synthetic account export and HR roster; "today" is 2026-10-12.
from datetime import date
today = date(2026, 10, 12)
roster = {"a.okafor": ("Water Ops", "active"), "b.lind": ("FSTS Security", "active"),
          "c.mendes": ("Water Ops", "left 2026-08-31"), "d.reyes": ("Clinical Eng", "active"),
          "e.strand": ("FSTS Platform", "active")}
accounts = [  # name, system, role, last_login, mfa, kind
    ("a.okafor", "HIST-01", "operator", "2026-10-10", True, "person"),
    ("b.lind", "RLY-01", "admin", "2026-10-11", True, "person"),
    ("c.mendes", "HIST-01", "engineer", "2026-09-14", True, "person"),
    ("d.reyes", "HIST-01", "admin", "2026-03-02", False, "person"),
    ("e.strand", "RLY-01", "admin", "2026-10-01", True, "person"),
    ("opsuser", "HIST-01", "admin", "2026-10-11", False, "shared"),
    ("svc-relay", "HIST-01", "writer", "2026-10-12", False, "service"),
    ("vendor-kell", "RLY-01", "admin", "2026-07-19", False, "vendor"),
    ("f.ito", "RLY-01", "operator", "2026-10-05", True, "person")]
need = {("Water Ops", "HIST-01"): {"operator", "engineer"}, ("FSTS Security", "RLY-01"): {"admin"},
        ("FSTS Platform", "RLY-01"): {"admin"}, ("Clinical Eng", "HIST-01"): set()}
findings = []
for name, sysid, role, last, mfa, kind in accounts:
    idle = (today - date.fromisoformat(last)).days
    if kind == "person":
        if name not in roster: findings.append((name, sysid, "not on HR roster (orphan)"))
        else:
            dept, status = roster[name]
            if status != "active": findings.append((name, sysid, f"leaver ({status}) still enabled; used after leaving" if last > status[5:] else f"leaver ({status})"))
            elif role not in need.get((dept, sysid), set()): findings.append((name, sysid, f"role {role} not justified for {dept}"))
    if kind == "shared": findings.append((name, sysid, "shared account: no individual accountability"))
    if kind == "vendor" and idle > 30: findings.append((name, sysid, f"vendor account standing, idle {idle} d: make time-bound"))
    if role == "admin" and not mfa and kind != "service": findings.append((name, sysid, "privileged without MFA"))
    if idle > 90 and kind == "person": findings.append((name, sysid, f"dormant {idle} d"))
for f in findings: print(f"{f[0]:<12} {f[1]:<8} {f[2]}")
print("accounts:", len(accounts), "findings:", len(findings), "accounts with >=1 finding:", len({f[0] for f in findings}))
```

Salida esperada (Python 3.13.5):

```text
c.mendes     HIST-01  leaver (left 2026-08-31) still enabled; used after leaving
d.reyes      HIST-01  role admin not justified for Clinical Eng
d.reyes      HIST-01  privileged without MFA
d.reyes      HIST-01  dormant 224 d
opsuser      HIST-01  shared account: no individual accountability
opsuser      HIST-01  privileged without MFA
vendor-kell  RLY-01   vendor account standing, idle 85 d: make time-bound
vendor-kell  RLY-01   privileged without MFA
f.ito        RLY-01   not on HR roster (orphan)
accounts: 9 findings: 9 accounts with >=1 finding: 5
```

Ordene los nueve hallazgos según lo que debe ocurrir hoy. `c.mendes`, usada el 14 de septiembre después de la baja del 31 de agosto, pasa al proceso de incidentes: conserve los registros de autenticación antes de deshabilitar la cuenta. `vendor-kell`, un administrador permanente en el retransmisor sin MFA y con 85 días de inactividad, se deshabilita y solo se vuelve a habilitar mediante incidencia. `d.reyes`, `opsuser` y `f.ito` se convierten en incidencias con responsable. Después busque lo que el script no puede ver, como la forma en que se guarda la credencial de `svc-relay` y cuándo se rotó por última vez.

### 7.7 Errores frecuentes y límites

- Revisar las cuentas a partir de una lista que alguien tecleó, en lugar de una exportación del sistema.
- Copiar el acceso de un compañero para una alta.
- Tratar como un asunto de mantenimiento la cuenta de una baja que se *usó* después de irse.
- Dar a las cuentas de proveedor acceso permanente «para ganar tiempo en una emergencia»; diseñe en su lugar un proceso de habilitación rápido y registrado.
- Exigir MFA a las personas pero dejar los secretos de las cuentas de servicio en scripts en texto plano.
- Eliminar una cuenta compartida en un dispositivo de control antes de confirmar cómo iniciarán sesión los operadores durante una emergencia.

Una revisión de accesos muestra el estado de las cuentas en un momento dado. No muestra cómo se usan las credenciales, para lo que se necesitan registros (capítulo 17), y solo es tan buena como la plantilla y la declaración de necesidades.

### Ejercicios — capítulo 7

**EX019 — Priorice los hallazgos.** *Objetivo:* separar los incidentes del mantenimiento. *Entradas:* la salida del Lab 7. *Restricciones:* tres franjas de prioridad: hoy, esta semana, este trimestre. *Pasos:* (1) ponga cada hallazgo en una franja; (2) para cada elemento de «hoy», escriba en orden las dos primeras acciones. *Evidencia esperada:* tabla. *Rúbrica:* 3 = el uso de c.mendes tras la baja y el administrador permanente del proveedor sin MFA en «hoy», con «conservar registros» antes de «deshabilitar» para c.mendes y confirmación con Kell antes de deshabilitar cuando la operación dependa de ello; d.reyes y opsuser esta semana; f.ito investigada esta semana; 2 = franjas sensatas, acciones en orden erróneo; 1 = todo «hoy»; 0 = nada.

**EX020 — Acceso de proveedor limitado en el tiempo.** *Objetivo:* diseñar un proceso de habilitación de proveedores. *Entradas:* Kell Instruments necesita acceso de administración al retransmisor unas cuatro veces al año, a veces con urgencia por la noche. *Restricciones:* debe poder usarlo a las 03:00 el tecnólogo de guardia; debe dejar evidencia. *Pasos:* (1) describa la solicitud, la aprobación, la habilitación, la vigilancia y la deshabilitación; (2) indique el tiempo máximo de habilitación; (3) indique qué evidencia se conserva. *Evidencia esperada:* procedimiento de diez pasos como máximo. *Rúbrica:* 3 = solicitud vinculada a una incidencia, aprobación de la guardia con información a operaciones, cuenta habilitada durante una ventana fija con MFA, sesión grabada o registrada, caducidad automática, revisión el siguiente día laborable; 2 = falta la caducidad o la evidencia; 1 = «habilitar cuando lo pidan»; 0 = nada.

**EX021 — Amplíe la revisión.** *Objetivo:* añadir una comprobación a la herramienta. *Entradas:* el Lab 7. *Restricciones:* solo la biblioteca estándar. *Pasos:* (1) añada una comprobación que señale a cualquier persona con acceso de administración tanto en RLY-01 como en HIST-01 (una concentración de privilegios); (2) añada una cuenta `b.lind` en `HIST-01` como `admin`, con MFA y la fecha de hoy como último inicio de sesión; (3) ejecute e informe del nuevo hallazgo. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = comprobación implementada sobre toda la lista de cuentas, b.lind señalada, sin falsos positivos; además señala que la propia cuenta nueva no está justificada porque FSTS Security no tiene necesidades declaradas en HIST-01; 2 = funciona sin advertir el hallazgo de necesidad; 1 = no se ejecutó; 0 = nada.

### Síntesis del capítulo

La identidad es un conjunto de registros y rutinas. Autentique según lo que puede hacer una cuenta; separe las cuentas personales, privilegiadas, de servicio y de proveedor, y elimine las compartidas o contrólelas en una bóveda; vincule las cuentas al proceso de altas, cambios y bajas; y revíselas con regularidad frente a una exportación, una plantilla y una declaración de necesidades. Algunos hallazgos de la revisión (la cuenta de una baja usada después de irse) son incidentes, y la evidencia va antes que la limpieza.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Siga estudiando — capítulo 07 de 30

[← Capítulo 06](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Fundamentos de arquitectura de seguridad

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- leer y dibujar una arquitectura de **zonas y conductos** de un servicio, incluidos los caminos de gestión;
- aplicar la defensa en profundidad y el mínimo privilegio para que un control fallido no sea un servicio fallido;
- diseñar para la **operabilidad**: mantenimiento, acceso de emergencia y modos de fallo como parte de la arquitectura;
- reconocer los atajos arquitectónicos que erosionan la separación con el tiempo.

El capítulo 2 comparó los flujos observados con los conductos declarados. Este capítulo trata de la propia declaración: por qué LANTERN tiene la forma que tiene y qué debe proteger un implementador al construirlo. Rara vez diseñará usted solo un sistema crítico completo, pero tomará decenas de pequeñas decisiones que preservan el diseño o lo deshacen sin hacer ruido.

### 8.1 Zonas, conductos y el sentido de la confianza

En LANTERN, los datos fluyen *hacia arriba*: estaciones → retransmisor → historiador → informes. Las órdenes a las estaciones no pasan en absoluto por LANTERN; los operadores controlan las estaciones desde el sistema independiente de la sala de control. Esta es la propiedad más importante del diseño. Si el retransmisor se ve comprometido, un atacante puede falsificar o bloquear la telemetría (algo grave), pero no puede dar órdenes a una bomba a través de él. Cada cambio propuesto debería contrastarse con esta propiedad: «¿crea esto un camino para que las órdenes, o los sistemas corporativos, alcancen la zona de estaciones?».

La segmentación de las redes de control respecto de las redes de negocio, con caminos controlados y vigilados entre ellas, es una pauta constante en las fuentes de seguridad de TO ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443 overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). Los cortafuegos la implementan; la guía del NIST sobre cortafuegos recomienda políticas de denegación por defecto que solo permitan el tráfico necesario ([NIST SP 800-41 Rev. 1](https://csrc.nist.gov/pubs/sp/800/41/r1/final)).

### 8.2 Defensa en profundidad y mínimo privilegio

La **defensa en profundidad** consiste en varios controles independientes, de modo que un fallo no lleve directamente a un daño. Para que un mensaje de telemetría falsificado engañe a un operador, tendría que alcanzar el retransmisor (segmentación), llevar un código de autenticación válido (capítulo 15), superar la validación (capítulo 3) y no disparar las alertas sobre valores inverosímiles (capítulo 19). Cada capa debe ser *independiente*: dos controles que dependen de la misma contraseña son un solo control. El **mínimo privilegio** (dar a cada usuario y proceso solo el acceso que necesita) figura entre los principios de diseño clásicos de Saltzer y Schroeder ([Saltzer and Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939)), junto con los valores por defecto a prueba de fallos y la economía de mecanismo. Para un implementador son concretos: la cuenta de servicio del retransmisor no puede escribir en su propia configuración; la cuenta del historiador que usa el retransmisor puede insertar telemetría, pero no borrarla.

### 8.3 Los caminos de gestión forman parte de la arquitectura

Muchos diagramas muestran el camino de los datos y omiten el **camino de gestión**: cómo llegan a cada equipo los administradores, los sistemas de copia de seguridad, los agentes de monitorización y los proveedores. Los caminos de gestión suelen transportar el acceso más poderoso del sistema. En LANTERN, la administración llega a los retransmisores solo desde un servidor de salto de gestión en la zona corporativa, con MFA; los proveedores llegan al servidor de salto mediante una cuenta limitada en el tiempo (capítulo 7); la monitorización recibe los registros que los retransmisores envían *desde* ellos, en lugar de iniciar sesión en ellos. El RLY-02 del Lab 22, que consulta servidores de hora públicos, es un camino de gestión que nadie dibujó.

### 8.4 Diseñar para la operabilidad

Un diseño seguro que los operadores no pueden hacer funcionar acabará eludiéndose. Pregunte por cada control: ¿cómo se mantiene? ¿Qué ocurre a las 03:00 cuando falla? ¿Cómo obtiene un ingeniero acceso de emergencia y cómo queda registrado ese acceso? ¿Qué hace el servicio cuando el retransmisor está caído: saben los operadores que su vista del historiador está desfasada? Diseñe los **modos degradados** de forma deliberada: las estaciones de LANTERN almacenan localmente 24 horas de lecturas, así que un corte del retransmisor hace perder actualidad, no datos; la pantalla del operador muestra la antigüedad de cada valor.

### 8.5 Erosión: cómo se degradan las arquitecturas

Las arquitecturas se erosionan mediante excepciones que parecen razonables: una regla de cortafuegos «temporal» para un proveedor, un portátil conectado a dos redes usado para configurar, un servidor de informes trasladado a la zona de control «para que vaya más rápido», una cuenta de administrador compartida por comodidad. Cada una es pequeña; juntas eliminan la separación. Las defensas son rutinarias: conductos registrados con responsable y caducidad (capítulo 2), revisiones de flujos, revisiones de reglas y la negativa a aceptar excepciones no documentadas. Fallowmere muestra cada tipo. La estación de trabajo corporativa que habla Modbus con PS-04 es un hábito de conexión a dos redes; el módem celular que Kell dejó en el PLC de PS-07 es una excepción de proveedor olvidada que ningún registro de flujo muestra; y la petición de enviar puntos de consigna recomendados del historiador a PS-07 habría sido una excepción de apariencia razonable que invertía el sentido de la confianza.

### 8.6 Ejemplo resuelto: una petición que cruza zonas (sintético)

Operaciones de Agua pide que el historiador envíe cada semana un archivo de «punto de consigna recomendado» al PLC de PS-07, para automatizar una optimización. Contrastada con el capítulo 8 («Zonas, conductos y el sentido de la confianza»), la petición rompe la propiedad más importante: crea un camino de la zona corporativa a la zona de estaciones que transporta información de *control*. No la rechace de plano; devuelva la cuestión de diseño a su responsable con alternativas: que un operador revise la recomendación en el sistema de la sala de control y la aplique allí; o que el archivo vaya al sistema de la sala de control, que lo valida y lo deja preparado para la aprobación del operador. Cualquiera de las dos preserva el sentido de la confianza. Su papel es mostrar la consecuencia y las alternativas, y registrar la decisión.

### 8.7 Actividad práctica: dibuje el camino de gestión

Dibuje las zonas y los conductos de LANTERN del capítulo 2 y añada después todos los caminos de gestión: SSH de administración a través del servidor de salto, acceso de proveedores, copia de seguridad, monitorización, hora, actualizaciones de paquetes. Para cada uno, registre origen, destino, protocolo, autenticación y responsable. Marque cualquier camino que permita a una sola credencial alcanzar tanto la zona corporativa como la de estaciones. En LANTERN, el camino que hay que vigilar es la vía del proveedor: la cuenta limitada en el tiempo de Kell llega al servidor de salto, y el servidor de salto llega a los retransmisores. Si esa misma cuenta, o una credencial compartida `opsuser`, abre también el recurso compartido de archivos corporativo, una sola contraseña robada cruza ambas zonas. Marque también el camino de la hora, ya que se descubrió que el RLY-02 del Lab 22 usaba servidores de hora públicos que ningún diagrama mostraba.

### 8.8 Errores frecuentes y límites

- Diagramas que solo muestran caminos de datos.
- Tratar como independientes dos controles que comparten una credencial, un administrador o un proveedor.
- Permitir un camino bidireccional porque el protocolo «solo lee».
- Diseñar solo para el día normal, sin modos degradados ni acceso de emergencia.
- Aceptar excepciones sin responsable ni caducidad.

La arquitectura limita lo que puede ocurrir; no muestra lo que ocurre. La verificación necesita flujos, registros y pruebas (capítulos 2, 19 y 23). Un ejemplo de Fallowmere: las fichas de control del riesgo R2 (capítulo 18) serían menos independientes de lo que parecen si el registro de sesiones del proveedor y la cuenta del proveedor se administraran con el mismo inicio de sesión de Kell.

### Ejercicios — capítulo 8

**EX022 — Compruebe el sentido de la confianza.** *Objetivo:* evaluar peticiones de cambio frente a la propiedad clave del diseño. *Entradas:* tres peticiones: (a) el retransmisor descarga cada hora una nueva lista de estaciones permitidas desde el historiador; (b) el SIEM envía una orden de bloqueo automática al cortafuegos de las estaciones cuando ve un ataque; (c) el retransmisor reenvía telemetría a Halden Cloud para una prueba de analítica. *Restricciones:* acepte, rechace o rediseñe cada una con un párrafo. *Pasos:* evalúe cada una frente a las cuatro propiedades de diseño del capítulo 8 (sentido de la confianza, mínimo privilegio, caminos de gestión, operabilidad). *Evidencia esperada:* tres párrafos. *Rúbrica:* 3 = (a) rediseñar: la configuración debería llegar desde el control de versiones mediante el proceso de cambios, no descargarse desde una zona de menor confianza; (b) rediseñar con cuidado: el bloqueo automático en un camino de TO necesita el acuerdo de operaciones, un fallo seguro y confirmación manual; (c) aceptable solo como un nuevo conducto declarado con entrada en el registro de flujos de datos (capítulo 12), contrato y monitorización; 2 = dos bien argumentadas; 1 = respuestas sin matices; 0 = nada.

**EX023 — Independencia de las capas.** *Objetivo:* poner a prueba la defensa en profundidad. *Entradas:* capas propuestas para proteger el retransmisor: cortafuegos gestionado por E. Strand; administración del retransmisor por E. Strand; clave HMAC generada y guardada por E. Strand en el retransmisor; reglas de monitorización escritas por E. Strand. *Restricciones:* no suponga mala intención. *Pasos:* (1) identifique la dependencia común; (2) indique qué suceso único anula todas las capas; (3) proponga dos cambios que restablezcan la independencia. *Evidencia esperada:* media página. *Rúbrica:* 3 = una sola persona y un solo conjunto de credenciales; el compromiso o el error de una cuenta anula todo; cambios como funciones de administración separadas, clave guardada en un almacén aparte con custodios distintos, reglas de monitorización a cargo del equipo de seguridad, que también las revisa; 2 = parcial; 1 = «añadir más controles»; 0 = nada.

**EX024 — Modo degradado.** *Objetivo:* diseñar la operabilidad. *Entradas:* el retransmisor está caído durante cuatro horas por la noche. *Restricciones:* tenga en cuenta a los operadores, los datos y las alertas. *Pasos:* (1) describa lo que ven los operadores; (2) qué ocurre con los datos; (3) qué alertas saltan y quién las recibe; (4) qué ocurre cuando vuelve el retransmisor. *Evidencia esperada:* una página. *Rúbrica:* 3 = las pantallas muestran la antigüedad del dato, no valores congelados como si fueran actuales; las estaciones almacenan localmente; las alertas de silencio de estación y de salud del retransmisor llegan a la guardia; el regreso provoca una carga del atraso que necesita margen (capítulo 1) y no dispara erróneamente las comprobaciones de reproducción; 2 = falta un aspecto; 1 = genérico; 0 = nada.

### Síntesis del capítulo

La propiedad arquitectónica más importante de LANTERN es el sentido de la confianza: los datos fluyen hacia arriba y las órdenes nunca bajan a través de él. Proteja esa propiedad en cada cambio, mantenga las capas realmente independientes, ponga los caminos de gestión en el diagrama y diseñe de forma deliberada los modos degradados y el acceso de emergencia. Las arquitecturas se degradan mediante excepciones; registre cada una con un responsable y una caducidad, y compruébelas.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Siga estudiando — capítulo 08 de 30

[← Capítulo 07](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Evidencia y medición

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- elegir una medida que responda a una pregunta operativa e indicar su **numerador, denominador y periodo**;
- informar de las distribuciones con medianas y percentiles altos, y decir qué oculta una media;
- incluir **lo que aún no ha ocurrido** (los elementos abiertos) en las medidas de latencia;
- informar de una tasa de éxito obtenida con pocos ensayos mediante un intervalo honesto.

Todos los capítulos posteriores le piden demostrar algo con evidencia: que un control funciona, que los parches se aplican a tiempo, que una restauración cumple su objetivo. Medir es la forma en que un implementador convierte «está bien» en una afirmación que otra persona puede comprobar. También es la forma en que las organizaciones se engañan a sí mismas, normalmente no mintiendo, sino eligiendo un denominador conveniente.

### 9.1 Lo que indica una buena medida

Una medida es útil cuando otra persona podría volver a calcularla. Indique la **pregunta** («¿con qué rapidez instalamos las correcciones del proveedor en los controladores de las estaciones?»), la **población** (qué activos, qué correcciones), el **numerador y el denominador**, el **periodo**, la **fuente** de los datos y qué se **excluye** y por qué. Una cifra de cumplimiento de parches del «96 %» sin denominador podría referirse al 96 % de los portátiles de oficina, lo que no dice nada de las estaciones de bombeo. La mediana conjunta de 9 días del Lab 9 no supera esta prueba: no indica población, y su denominador excluye en silencio siete correcciones abiertas.

### 9.2 Distribuciones, no solo medias

Las magnitudes operativas (tiempo hasta el parche, tiempo hasta la restauración, tiempo de respuesta a una alerta) suelen ser asimétricas: la mayoría son rápidas, unas pocas son muy lentas, y las lentas son las que importan. La **mediana** describe el caso típico; el **percentil 90** (p90) describe los casos malos; la **media** se ve arrastrada por los valores atípicos y no describe bien ninguno de los dos. Informe de la mediana y del p90 juntos, y mire el máximo. En el Lab 9, la mediana de 95 días de los controladores de las estaciones, con cinco correcciones aún abiertas, es la cifra que ocultaba la mediana conjunta.

### 9.3 Elementos abiertos y supervivencia

Un error frecuente en las medidas de latencia es calcularlas solo sobre los elementos **completados**. Si se han publicado cinco correcciones para los controladores de las estaciones pero no se han instalado, son las más lentas de todas, y son invisibles para una mediana calculada sobre las correcciones instaladas. Informe siempre de cuántos elementos siguen abiertos y de su antigüedad. La guía del NIST sobre gestión de parches en la empresa trata la aplicación de parches como un proceso de respuesta al riesgo con una puntualidad medible, y recomienda métricas que la reflejen ([NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final)).

Agrupar conjuntos con comportamientos muy distintos es la trampa relacionada. Una única mediana para la TI de oficina, los servidores y los controladores de las estaciones queda dominada por el grupo con más elementos (normalmente la TI de oficina) y oculta el grupo de mayores consecuencias.

### 9.4 Las muestras pequeñas necesitan intervalos

Las pruebas en servicios críticos son caras, así que las muestras son pequeñas: diez simulacros de restauración, ocho alertas de prueba inyectadas. «9 de 10 simulacros cumplieron el objetivo» es un hecho; «nuestra tasa de éxito en restauraciones es del 90 %» es una afirmación excesiva. Un **intervalo de confianza** muestra el rango de tasas subyacentes compatibles con los datos. Para proporciones de muestras pequeñas, el **intervalo de puntuación de Wilson** se comporta bien ([Wilson, 1927](https://doi.org/10.1080/01621459.1927.10502953)). Para 9 de 10, el intervalo de Wilson al 95 % va aproximadamente de 0,60 a 0,98: la tasa real podría ser razonablemente tan baja como el 60 %. Por eso la restauración de copias de seguridad del Lab 23, con 9 de 10 simulacros dentro del objetivo, sigue sin cumplir una regla de afirmación cuyo límite inferior debe llegar a 0,70.

### 9.5 Ejemplo resuelto: latencia de parches y simulacros de restauración (sintético)

El informe mensual de FSTS dice: «latencia mediana de parches: 9 días». El Lab 9 la vuelve a calcular por grupos. TI corporativa: 12 de 12 correcciones instaladas, mediana de 5,5 días, p90 de unos 9. Retransmisor/historiador: 6 de 8 instaladas, mediana de 18,5 días, p90 de unos 31,5, dos aún abiertas. PLC/RTU de las estaciones: solo 3 de 8 instaladas, mediana de 95 días, cinco aún abiertas. La mediana conjunta de 9 días es aritméticamente correcta y operativamente engañosa: describe portátiles y omite las siete correcciones abiertas, cinco de ellas en los activos de mayores consecuencias.

Los controladores de las estaciones tardan más en parchearse por buenas razones: los proveedores deben certificar las correcciones, y la instalación puede requerir una visita a la instalación y una ventana de corte acordada con operaciones (capítulo 16). La medida no debería castigarlo; debería mostrarlo, para que puedan justificarse controles compensatorios durante el periodo de exposición.

### 9.6 Actividad práctica: medidas honestas

**Lab 9** (guárdelo como `lab09.py` y ejecútelo con `python3 lab09.py`):

```python
# Lab 9 - measuring patch latency and a restore drill honestly (offline, standard library only)
# Synthetic: days from vendor fix release to installation, Fallowmere estate, last two quarters.
import math, statistics as st
latency = {"corp IT": [3, 5, 4, 9, 6, 2, 7, 5, 30, 4, 6, 8],
           "relay/historian": [12, 19, 15, 41, 22, 18],
           "station PLC/RTU": [64, 140, 95]}
not_yet = {"corp IT": 0, "relay/historian": 2, "station PLC/RTU": 5}  # fixes released but not installed
def pct(xs, p):
    xs = sorted(xs); k = (len(xs) - 1) * p; f = math.floor(k); c = math.ceil(k)
    return xs[f] + (xs[c] - xs[f]) * (k - f)
for g, xs in latency.items():
    n = len(xs) + not_yet[g]
    print(f"{g:<16} installed {len(xs):>2}/{n:<2} median {st.median(xs):>5.1f} d  p90 {pct(xs, .9):>6.1f} d  mean {st.mean(xs):>5.1f} d")
allx = [x for xs in latency.values() for x in xs]
print(f"pooled (misleading) median {st.median(allx):.1f} d over {len(allx)} installed fixes; {sum(not_yet.values())} still open are invisible to it")
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n; c = (p + z*z/(2*n)) / d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
k, n = 9, 10  # restore drills that met the 4-hour target
lo, hi = wilson(k, n)
print(f"restore drills within target: {k}/{n} = {k/n:.0%}, 95% Wilson interval [{lo:.2f}, {hi:.2f}]")
```

Salida esperada (Python 3.13.5):

```text
corp IT          installed 12/12 median   5.5 d  p90    8.9 d  mean   7.4 d
relay/historian  installed  6/8  median  18.5 d  p90   31.5 d  mean  21.2 d
station PLC/RTU  installed  3/8  median  95.0 d  p90  131.0 d  mean  99.7 d
pooled (misleading) median 9.0 d over 21 installed fixes; 7 still open are invisible to it
restore drills within target: 9/10 = 90%, 95% Wilson interval [0.60, 0.98]
```

Escriba la línea de informe que enviaría en lugar de «latencia mediana de parches: 9 días». Debería caber en dos frases.

Una línea de dos frases que aprobaría: «La TI corporativa instaló 12 de 12 correcciones, con una mediana de 5,5 días; el retransmisor y el historiador, 6 de 8, con una mediana de 18,5 días y dos abiertas. Los controladores de las estaciones instalaron 3 de 8, con una mediana de 95 días y cinco correcciones abiertas bajo controles compensatorios y con planes fechados». Es más larga que «9 días», pero ahora el lector puede ver dónde está el riesgo, y los controladores de las estaciones ya no quedan ocultos detrás de los portátiles de oficina.

### 9.7 Errores frecuentes y límites

- Informar de un porcentaje sin su denominador.
- Medias para magnitudes asimétricas.
- Calcular la latencia solo sobre los elementos cerrados.
- Agrupar conjuntos de modo que el grupo grande y de pocas consecuencias oculte el pequeño y de muchas consecuencias.
- Convertir un número pequeño de ensayos con éxito en una tasa sin intervalo.
- Cambiar la definición de una medida entre informes sin decirlo.

Las medidas describen lo que se registró. Si los datos de origen están incompletos (correcciones no registradas, simulacros no anotados), ninguna estadística lo reparará. En el Lab 9, la mediana conjunta muestra tres de estos errores a la vez: sin denominador, con los elementos abiertos excluidos y con los grupos agrupados.

### Ejercicios — capítulo 9

**EX025 — Reescriba la línea del informe.** *Objetivo:* comunicar una medida con honestidad. *Entradas:* la salida del Lab 9. *Restricciones:* dos frases como máximo; incluya denominadores y elementos abiertos. *Pasos:* escríbala y después enumere lo que dejó fuera y por qué. *Evidencia esperada:* la línea y una nota. *Rúbrica:* 3 = medianas o p90 por grupo con recuentos de instaladas/total, correcciones abiertas de las estaciones mencionadas expresamente, ninguna cifra conjunta presentada como titular; 2 = en su mayor parte; 1 = repite la mediana conjunta; 0 = nada.

**EX026 — Calcule la antigüedad de los elementos abiertos.** *Objetivo:* incluir los elementos abiertos en la medida. *Entradas:* las cinco correcciones abiertas de las estaciones se publicaron hace 20, 45, 70, 130 y 200 días; las dos correcciones abiertas del retransmisor/historiador, hace 10 y 35 días. *Restricciones:* trate la antigüedad de cada corrección abierta como un límite inferior de su latencia. *Pasos:* (1) combine las latencias instaladas con las antigüedades abiertas de los PLC/RTU de las estaciones; (2) calcule una mediana que sea un límite inferior; (3) explique por qué es un límite inferior y no una estimación. *Evidencia esperada:* cálculo y explicación. *Rúbrica:* 3 = valores combinados 20, 45, 64, 70, 95, 130, 140, 200 → límite inferior de la mediana 82,5 días, correctamente explicado (los elementos abiertos solo pueden envejecer); 2 = error aritmético; 1 = ignora los elementos abiertos; 0 = nada.

**EX027 — ¿Cuántos simulacros?** *Objetivo:* planificar el tamaño de la muestra a partir de un intervalo. *Entradas:* la función de Wilson del Lab 9. *Restricciones:* suponga que todos los simulacros tienen éxito. *Pasos:* (1) encuentre el menor número de simulacros consecutivos con éxito para el que el límite inferior de Wilson al 95 % sea al menos 0,80; (2) indique si es asumible a un simulacro por mes y qué haría en su lugar. *Evidencia esperada:* el número, con la ejecución que lo muestra, y un párrafo. *Rúbrica:* 3 = 16 simulacros (límite inferior ≈ 0,806; 15 da ≈ 0,796), reconocidos como 16 meses a uno por mes, con alternativas sensatas como restauraciones parciales más pequeñas y frecuentes o pruebas de restauración automatizadas; 2 = número correcto, sin plan; 1 = adivinado; 0 = nada.

### Síntesis del capítulo

Una medida es útil cuando indica su pregunta, población, numerador, denominador, periodo, fuente y exclusiones. Informe de medianas con percentiles altos para las magnitudes asimétricas; incluya los elementos abiertos; no agrupe conjuntos con consecuencias distintas; y acompañe de intervalos las tasas de éxito de muestras pequeñas. El objetivo no es una cifra favorecedora, sino una que otra persona pueda volver a calcular y sobre la que pueda actuar.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Siga estudiando — capítulo 09 de 30

[← Capítulo 08](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Infraestructura crítica y seguridad sectorial: orientación

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- explicar qué hace que un servicio sea **crítico**: la consecuencia de su pérdida para las personas, para otros servicios y para la sociedad;
- describir en qué se diferencian el agua, la salud, la energía, el transporte y las finanzas en lo que protegen, en la rapidez con que llega el daño y en quién los regula;
- identificar las **dependencias e interdependencias** que convierten un fallo local en uno regional;
- situar su propio trabajo como implementador dentro de las obligaciones que asume un operador.

Los capítulos 1 a 9 construyeron capacidades generales. A partir de aquí, el libro las aplica específicamente a los servicios críticos. Este capítulo es de orientación: la forma del campo, lo suficiente para entender por qué un tecnólogo de FSTS debe pensar de manera distinta en una estación de bombeo, un hospital y unas cocheras de autobuses aunque los servidores se parezcan.

### 10.1 Qué hace que un servicio sea crítico

Un servicio es crítico cuando su interrupción dañaría gravemente la salud, la seguridad, la protección, la actividad económica o el funcionamiento de la sociedad. Los gobiernos lo formalizan de maneras distintas. Estados Unidos describe **funciones críticas nacionales** (funciones tan vitales que su interrupción tendría un efecto debilitante) en lugar de limitarse a listas de sectores ([CISA National Critical Functions](https://www.cisa.gov/national-critical-functions-set)). La Directiva NIS2 de la Unión Europea establece obligaciones de gestión de riesgos de ciberseguridad y de notificación para entidades de sectores de alta criticidad ([Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/)), y la Directiva CER aborda la resiliencia física y, en sentido amplio, de las entidades críticas ([Directive (EU) 2022/2557](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)). Estos textos cambian; compruebe la versión vigente y cómo la aplica su jurisdicción. Este libro no ofrece asesoramiento jurídico.

Para un implementador, el significado práctico es más sencillo: **la unidad de daño son las personas y el tiempo**, no solo los registros de datos o el dinero. «41.000 personas sin información fiable sobre el agua durante seis horas» es el tipo de afirmación que debería orientar las prioridades.

### 10.2 En qué se diferencian los sectores

| Sector (ejemplo sintético de Fallowmere) | Qué se protege primero | Con qué rapidez llega el daño | Tecnología típica |
|---|---|---|---|
| Agua (Fallowmere Water) | Agua potable segura, continuidad del suministro | De horas a días; el daño por calidad puede ser más rápido | PLC, RTU, SCADA, telemetría por enlaces de operador |
| Salud (Community Hospital) | Seguridad del paciente, continuidad asistencial | Minutos en algunos sistemas clínicos | Dispositivos médicos, pasarelas clínicas, historias electrónicas |
| Transporte (cocheras de transporte) | Seguridad de los pasajeros, continuidad del servicio | De minutos a horas | Sistemas de flota, venta de billetes, TI de las cocheras |
| Energía (no gestionada por FSTS) | Estabilidad de la red, suministro | De segundos a horas | Relés de protección, centros de control |
| Finanzas (no gestionadas por FSTS) | Integridad de las transacciones, disponibilidad | Minutos | Sistemas de pago, centros de datos |

Las diferencias cambian las decisiones de implementación. Un parche en la pasarela de las bombas de infusión de un hospital necesita la conformidad de ingeniería clínica; un cambio de cortafuegos en una estación de bombeo puede necesitar una visita a la instalación y una ventana de corte; un quiosco de las cocheras normalmente puede reconstruirse el mismo día. Tratarlos todos con un único proceso de cambios de TI o bien ralentiza los cambios seguros, o bien precipita los peligrosos.

### 10.3 Dependencias e interdependencias

Los servicios críticos dependen unos de otros: el agua necesita electricidad para las bombas y telecomunicaciones para la telemetría; los hospitales necesitan agua, electricidad y telecomunicaciones; todos dependen de un número reducido de proveedores. El artículo clásico de Rinaldi y sus colegas clasifica las interdependencias en físicas, cibernéticas, geográficas y lógicas ([Rinaldi, Peerenboom and Kelly, 2001](https://doi.org/10.1109/37.969131)). En FSTS, la interdependencia más importante es organizativa: el mismo equipo reducido, el mismo servidor de salto y los mismos proveedores atienden a los tres operadores. Una sola cuenta de administrador de FSTS comprometida alcanza a la vez el agua, la salud y el transporte.

### 10.4 Las obligaciones del operador y su parte en ellas

Los operadores de servicios esenciales suelen asumir obligaciones de gestionar el riesgo cibernético, notificar los incidentes significativos en plazos establecidos, mantener planes de continuidad y cooperar con las autoridades. Marcos como el Cyber Assessment Framework del NCSC del Reino Unido las expresan como resultados que deben alcanzarse ([NCSC CAF](https://www.ncsc.gov.uk/collection/caf)); los objetivos intersectoriales de desempeño en ciberseguridad de CISA ofrecen una base de prácticas ([CISA CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)). Un implementador rara vez es titular de estas obligaciones, pero produce la mayor parte de la evidencia que las respalda: listas de activos, revisiones de accesos, registros, resultados de pruebas, cronologías de incidentes. Si esa evidencia llega tarde o es errónea, la notificación del operador llega tarde o es errónea.

### 10.5 Ejemplo resuelto: un fallo, tres clientes (sintético)

A las 02:10 falla un disco del servidor de salto de FSTS. Operaciones de Agua pierde la administración remota de los retransmisores, pero conserva la telemetría (los retransmisores siguen funcionando). Los ingenieros clínicos del hospital no pueden acceder a la pasarela de las bombas de infusión para cargar una actualización de la biblioteca de fármacos programada para las 06:00. Las cocheras no pueden enviar un cambio de horarios a los quioscos. El mismo fallo tiene tres consecuencias distintas con tres plazos distintos. El tecnólogo de guardia que lo reconoce llama primero a Ingeniería Clínica, porque la actualización de las 06:00 tiene una finalidad de seguridad del paciente, aunque Agua sea el cliente más grande.

### 10.6 Actividad práctica: tabla de consecuencias y plazos

Para cada cliente de Fallowmere, enumere tres sistemas gestionados por FSTS. Para cada sistema, escriba: qué pierden las personas si se detiene, con qué rapidez esa pérdida se vuelve dañina, quién decide la acción de emergencia y de qué otro sistema depende. Guarde esta tabla; el capítulo 11 la convierte en un inventario con dependencias. Para Fallowmere Community Hospital, una fila podría decir: pasarela de las bombas de infusión; pérdida, no pueden cargarse las actualizaciones de la biblioteca de fármacos; dañina en cuestión de horas si se pierde una actualización programada como la de las 06:00; decide Ingeniería Clínica; depende del servidor de salto de FSTS. Esa fila es la razón por la que, en el ejemplo resuelto, el fallo del servidor de salto se escaló al hospital antes que a Agua.

### 10.7 Errores frecuentes y límites

- Tratar todos los sistemas que gestiona un equipo de TI como si tuvieran la misma consecuencia.
- Medir el daño solo en datos o en dinero.
- Ignorar como dependencias a las personas, las herramientas y los proveedores compartidos.
- Citar la normativa de memoria; su alcance y sus plazos cambian y difieren según la jurisdicción.
- Suponer que el implementador no tiene ningún papel en las obligaciones del operador.

El fallo del servidor de salto muestra juntos el primer y el tercer error: un único equipo compartido de FSTS tuvo tres consecuencias con tres plazos.

Medir el daño solo en dinero habría situado a Agua en primer lugar aquella noche, por ser el cliente más grande, y habría pasado por alto la actualización de la biblioteca de fármacos de las 06:00.

### Ejercicios — capítulo 10

**EX028 — La consecuencia en personas y tiempo.** *Objetivo:* expresar el daño en unidades de servicio. *Entradas:* el escenario del capítulo 10 («Ejemplo resuelto: un fallo, tres clientes»). *Restricciones:* solo cifras sintéticas; indique los supuestos. *Pasos:* para cada cliente, escriba una frase del tipo «N personas pierden X durante T, lo que se vuelve dañino al cabo de D porque…». *Evidencia esperada:* tres frases con supuestos. *Rúbrica:* 3 = tres afirmaciones concretas, verosímiles y con los supuestos señalados, que muestran plazos distintos e identifican el plazo de seguridad del paciente del hospital como el más temprano; 2 = una genérica; 1 = todo en dinero; 0 = nada.

**EX029 — Mapa de dependencias compartidas.** *Objetivo:* encontrar las interdependencias que crea un servicio compartido. *Entradas:* FSTS gestiona un servidor de salto, un SIEM, un directorio de identidades y un sistema de copias de seguridad para los tres clientes; Kell suministra las RTU de agua, y BayTel transporta la telemetría del agua y la conexión a internet del hospital. *Restricciones:* use los cuatro tipos de Rinaldi. *Pasos:* (1) clasifique cada dependencia; (2) nombre el fallo único de efecto más amplio; (3) proponga un cambio para reducirlo. *Evidencia esperada:* tabla y párrafo. *Rúbrica:* 3 = los sistemas compartidos de FSTS como cibernéticos/lógicos, BayTel como operador común cibernético/físico, el personal como lógico; el compromiso del directorio de identidades o del servidor de salto identificado como el más amplio; un cambio práctico como niveles privilegiados por cliente o un segundo camino de operador para la telemetría; 2 = clasificación débil; 1 = solo una lista; 0 = nada.

**EX030 — La evidencia que usted debe.** *Objetivo:* conectar el trabajo diario con las obligaciones del operador. *Entradas:* los CPG de CISA o el CAF del NCSC (elija uno; cite la versión que leyó). *Restricciones:* tres resultados u objetivos. *Pasos:* para cada uno, nombre la evidencia que produce un tecnólogo de FSTS, con qué frecuencia y dónde se guarda. *Evidencia esperada:* tabla con la cita. *Rúbrica:* 3 = tres resultados u objetivos citados correctamente (por ejemplo, inventario de activos, MFA, recogida de registros), cada uno con evidencia concreta producida con regularidad; 2 = evidencia vaga; 1 = sin cita; 0 = nada.

### Síntesis del capítulo

Un servicio es crítico por lo que su pérdida causa a las personas, medido en personas y tiempo. Los sectores se diferencian en lo que protegen primero y en la rapidez con que llega el daño, así que el mismo fallo técnico necesita respuestas distintas. Los servicios compartidos como FSTS crean interdependencias a través de las personas, las herramientas y los proveedores. Los operadores asumen las obligaciones legales; los implementadores producen la mayor parte de la evidencia que muestra que se cumplen.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Siga estudiando — capítulo 10 de 30

[← Capítulo 09](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Infraestructura crítica y seguridad sectorial: activos y contexto

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- construir y mantener un inventario de activos para un servicio mixto de TI/TO a partir de varias fuentes;
- registrar para cada activo su **responsable, función, criticidad, ubicación, versión de software o firmware, estado del soporte y dependencias**;
- usar métodos de descubrimiento **pasivos**, seguros para las redes operativas;
- conciliar fuentes que discrepan y tratar la discrepancia como un hallazgo.

El capítulo 4 mostró cómo modelar un inventario. Este capítulo trata de llenarlo con veracidad. Los objetivos intersectoriales de desempeño de CISA incluyen mantener un inventario de activos, también de los activos de TO ([CISA CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)); no puede proteger, parchear ni monitorizar lo que no ha registrado.

### 11.1 Qué registrar y por qué

| Atributo | Por qué lo necesita un implementador |
|---|---|
| Identificador y ubicación | Para encontrarlo, físicamente y en la red. |
| Función y criticidad | Para decidir la prioridad en parches, monitorización y respuesta. |
| Responsable (una función, no una persona) | Alguien debe aprobar los cambios y aceptar el riesgo. |
| Modelo y versión de firmware/software | Para cotejar avisos y correcciones del proveedor. |
| Estado del soporte del proveedor | Los activos sin soporte necesitan controles compensatorios y planes de sustitución. |
| Direcciones de red y zona | Para comprobar los flujos (capítulo 2). |
| Dependencias | Para entender qué más falla con él (capítulo 10). |
| Última verificación (fecha, método) | Para que los registros desfasados sean visibles. |

### 11.2 Las fuentes y sus puntos ciegos

Ninguna fuente es completa por sí sola. Los **registros de compras y contratos** saben qué se compró, pero no a dónde fue. Los **registros de gestión de la configuración o de ingeniería** conocen el diseño, pero pueden ir por detrás de la realidad. La **observación de la red** (tablas de los conmutadores, registros de flujo, un sensor pasivo) ve lo que habla, pero no lo que está en silencio. Los **reconocimientos en la instalación** ven lo que está físicamente presente, pero son caros y poco frecuentes. Los **portales de los proveedores** conocen las versiones de firmware de lo que soportan. Combine al menos dos fuentes y registre qué fuente dijo qué. PS-09 muestra por qué: solo los registros de flujo sabían que la estación se había quedado en silencio.

### 11.3 Descubrimiento seguro en redes operativas

El escaneo activo (enviar sondas a todas las direcciones) es rutinario en las redes de oficina y arriesgado en las redes de control: algunos controladores antiguos y dispositivos embebidos pueden comportarse mal o reiniciarse cuando se les sondea de forma inesperada. La guía de TO del NIST aconseja prudencia con el escaneo activo en entornos de TO y da preferencia a los métodos pasivos o a un trabajo activo cuidadosamente planificado y coordinado ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). Para un implementador, la regla es: en la zona de estaciones, use fuentes pasivas (registros de flujo, tablas de los conmutadores, las exportaciones de configuración de los propios controladores realizadas por sus ingenieros), salvo que se haya acordado un método activo con operaciones, se haya probado en un equipo de repuesto y se haya programado.

### 11.4 Conciliación

Cuando las fuentes discrepan, la discrepancia es información. Un activo que figura en los registros de compras pero nunca se ha visto en la red puede estar en un armario, o conectado en algún lugar inesperado. Una dirección vista en los flujos pero ausente de todos los registros es un dispositivo desconocido. Una versión de firmware que difiere entre el registro de ingeniería y el portal del proveedor significa que uno de los dos es erróneo; y si lo es el registro de ingeniería, puede que se haya aplicado una corrección, o no, sin documentarla. Siga cada discrepancia como una incidencia con responsable hasta que se resuelva.

### 11.5 Activos sin soporte

Los servicios críticos suelen mantener equipos en funcionamiento después de que termine el soporte del proveedor, porque sustituirlos exige inversión, cortes y nueva certificación. El inventario debe hacerlo visible, con un plan de **controles compensatorios** para cada activo sin soporte: segmentación más estricta, listas de permitidos más rigurosas, monitorización adicional, repuestos y una fecha de sustitución a cargo de alguien con presupuesto. La RTU Kell R2 de PS-09, sin soporte desde el 2025-12-31 y todavía de criticidad 1, es el caso de Fallowmere. Su plan nombraría la entrada de la lista de permitidos del retransmisor y el conducto como los controles reforzados, la regla C como monitorización adicional, una RTU de repuesto en poder de Agua y una fecha de sustitución a cargo de Operaciones de Agua, que gestiona el presupuesto de inversión.

### 11.6 Ejemplo resuelto: conciliar PS-09 (sintético)

Tres fuentes describen la estación de bombeo PS-09. El registro de compras incluye una RTU Kell R2 comprada en 2017. El registro de ingeniería indica el firmware 1.1 y el responsable "Water Ops". Los registros de flujo muestran a 10.20.0.13 comunicándose con el retransmisor hasta hace tres semanas, y nada desde entonces (la estación en silencio del capítulo 2). El inventario (capítulo 4) no tiene responsable para PS09-RTU y registra que el soporte del proveedor terminó el 2025-12-31. Usted registra cuatro discrepancias: falta el responsable en el inventario, pero figura en el registro de ingeniería (corrija el registro, después de confirmarlo con Water Ops); soporte terminado (necesita un plan de controles compensatorios); estación en silencio (problema operativo, planteado a Operaciones de Agua el mismo día); y firmware no verificado de forma independiente (pida al ingeniero de Agua que exporte la configuración de la RTU en la próxima visita a la instalación; capítulo 28).

### 11.7 Actividad práctica: conciliación de tres fuentes

Con el inventario del Lab 4 y los flujos del Lab 2, enumere cada activo o dirección que aparece en una fuente pero no en la otra, y cada atributo que difiere. Para cada uno, escriba la siguiente acción y el responsable. No sondee ningún dispositivo para resolver una discrepancia; pregunte al responsable. Cuente con que la RTU de PS-09 en 10.20.0.13 aparezca en ambas fuentes, pero con discrepancias: presente en el inventario, en silencio en los flujos. Cuente también con que los flujos del Lab 2 muestren direcciones que faltan en el inventario, como la estación de trabajo corporativa 10.40.3.7; registre su responsable como una pregunta para Ingeniería de Agua, no como una suposición.

### 11.8 Errores frecuentes y límites

- Tratar una sola fuente como el inventario.
- Hacer escaneos activos en redes de control «solo para asegurarse».
- Registrar a una persona como responsable en lugar de una función.
- Registrar el firmware una vez y no volver a verificarlo nunca.
- Enumerar los activos sin soporte sin controles compensatorios ni responsable de la sustitución.
- Ocultar las discrepancias para que el inventario parezca completo.

Un inventario es un modelo de la realidad, siempre algo desactualizado. Su calidad se mide por lo reciente que es la verificación de cada registro y por la rapidez con que se cierran las discrepancias. El módem celular de PS-07, descubierto solo mediante una visita a la instalación, es el argumento contra fiarse de una sola fuente.

### Ejercicios — capítulo 11

**EX031 — Concilie.** *Objetivo:* encontrar discrepancias entre fuentes. *Entradas:* el inventario del Lab 4 y los flujos del Lab 2. *Restricciones:* solo las zonas de estaciones, del retransmisor y corporativa. *Pasos:* (1) enumere las direcciones de los flujos sin registro en el inventario (suponga que el inventario asigna PS04-PLC a 10.20.0.11, PS07-PLC a 10.20.0.12, PS09-RTU a 10.20.0.13, RLY-01 a 10.30.0.5 y HIST-01 a 10.40.8.20); (2) enumere los activos del inventario en esas zonas que nunca se vieron en los flujos; (3) indique una acción y un responsable para cada uno. *Evidencia esperada:* tabla. *Rúbrica:* 3 = 10.40.3.7 (estación de trabajo corporativa, ausente del extracto) identificada como no registrada y como origen del Modbus no declarado; SW-STN-04 no vista (lo esperable en un conmutador; explíquelo); PS09-RTU en silencio; acciones con responsable; 2 = parcial; 1 = solo una lista; 0 = nada.

**EX032 — Controles compensatorios.** *Objetivo:* planificar para un activo sin soporte. *Entradas:* PS09-RTU, criticidad 1, soporte del proveedor terminado, presupuesto de sustitución disponible dentro de 14 meses. *Restricciones:* controles que FSTS y Agua pueden implementar sin correcciones del proveedor. *Pasos:* enumere cuatro controles compensatorios con evidencia para cada uno, y el responsable de la sustitución. *Evidencia esperada:* tabla. *Rúbrica:* 3 = conducto restringido solo al retransmisor y verificado, validación y cuarentena por rango en el retransmisor, alertas de silencio de estación y de valor inverosímil, unidad de repuesto o procedimiento manual probado, copia de seguridad de la configuración; sustitución a cargo de una función de Agua, con fecha; 2 = tres; 1 = «vigilarlo»; 0 = nada.

**EX033 — Plan de descubrimiento.** *Objetivo:* planificar un descubrimiento seguro. *Entradas:* Operaciones de Agua quiere una lista completa de los dispositivos de las 14 estaciones en tres meses. *Restricciones:* ningún escaneo activo sin acuerdo; como máximo dos visitas a instalaciones por semana. *Pasos:* (1) enumere las fuentes pasivas que usará primero; (2) indique cuándo estaría justificado un método activo y cómo lo haría seguro; (3) dé un calendario. *Evidencia esperada:* plan de una página. *Rúbrica:* 3 = primero las fuentes pasivas (flujos, tablas de los conmutadores, exportaciones de ingeniería, registros de compras); método activo solo con acuerdo de operaciones, probado en un repuesto, con limitación de ritmo, dentro de una ventana y con alguien en la instalación; calendario realista; 2 = plan sólido pero vago en cuanto a seguridad; 1 = «escanear la subred»; 0 = nada.

### Síntesis del capítulo

Un inventario registra, para cada activo, qué es, dónde está, quién es su responsable, qué ejecuta, si tiene soporte, de qué depende y cuándo se verificó todo ello por última vez. Constrúyalo a partir de varias fuentes, haga el descubrimiento de forma segura en las redes de control, trate las discrepancias entre fuentes como hallazgos y dé a cada activo sin soporte controles compensatorios y un responsable de su sustitución.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Siga estudiando — capítulo 11 de 30

[← Capítulo 10](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Infraestructura crítica y seguridad sectorial: flujos de datos

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- mantener un **registro de flujos de datos** que recoja, para cada flujo, su origen, destino, clase de datos, protección y conservación;
- clasificar los datos de un servicio crítico: telemetría operativa, configuración, datos personales y vinculados a pacientes, registros de seguridad;
- verificar el registro frente a lo que los sistemas realmente envían y conservan;
- reconocer cuándo un flujo nuevo necesita una revisión de privacidad, contractual o de seguridad física antes de empezar.

El capítulo 2 comparó los flujos de red con los conductos declarados. Un conducto dice que *un camino está permitido*; un registro de flujos de datos dice *qué datos viajan por él, cómo se protegen y cuánto tiempo se conservan en el otro extremo*. En los servicios compartidos, la segunda pregunta suele ser la que mete en problemas a una organización, porque los datos sobreviven al motivo por el que se recogieron.

### 12.1 El registro

Cada entrada del registro de LANTERN recoge: identificador; origen y destino (sistemas, no solo direcciones); **clase de datos**; si el flujo va cifrado en tránsito; cuánto tiempo conserva los datos el destino; el propósito; el responsable; y, para los datos personales, la base jurídica registrada por el responsable de los datos. El registro es un documento que las personas leen durante un incidente («¿qué salió de la pasarela clínica?») y ante una solicitud de privacidad («¿a dónde van los datos de la bomba de este paciente?»). DF5 es una entrada modelo: de la pasarela clínica a Halden Cloud, vinculada a pacientes, cifrada, 30 días registrados.

### 12.2 Clases de datos

Para un implementador, cuatro clases cubren la mayor parte de un servicio crítico compartido:

- **Telemetría operativa**: lecturas y estados (niveles, caudales, cloro). Normalmente no es personal, pero su integridad es crítica y a veces es sensible en conjunto (revela cómo funciona la red).
- **Datos de configuración e ingeniería**: programas de los controladores, diagramas de red, puntos de consigna, configuración del retransmisor. Muy sensibles: son un mapa para un atacante.
- **Datos personales y vinculados a pacientes**: cualquier cosa sobre una persona identificable. En el hospital, los registros de eventos de las bombas de infusión vinculados a una planta y una hora pueden identificar a un paciente. Se aplica la legislación de protección de datos; en la UE, el RGPD ([Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)) exige, entre otros principios, que los datos personales no se conserven más tiempo del necesario para su finalidad. *Nota para el lector hispanohablante:* en España, el RGPD se complementa con la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales; en América Latina rige la ley de cada país, por ejemplo la Ley 25.326 en Argentina o la Ley 1581 de 2012 en Colombia.
- **Registros de seguridad**: autenticación, flujos, alertas. A menudo contienen datos personales (nombres de usuario, direcciones) y deben protegerse y conservarse según la política.

El Marco de Privacidad del NIST ofrece una estructura para gestionar el riesgo de privacidad junto con el riesgo de ciberseguridad ([NIST Privacy Framework](https://www.nist.gov/privacy-framework)).

### 12.3 Verificar el registro

Los registros se degradan igual que los inventarios. Verifíquelos muestreando lo que ocurre de verdad: qué sistemas envían a cuáles (flujos), qué clase de datos va en las cargas útiles (muestreo de metadatos por parte del responsable de los datos, no leyendo historias de pacientes), si el transporte va cifrado y cuánto tiempo conserva realmente los datos el destino (su configuración de conservación y la antigüedad de sus registros más antiguos). Las diferencias son de tipos conocidos: flujos no registrados; flujos que envían una clase distinta de la registrada; cifrado registrado pero ausente; conservación más larga que la registrada.

### 12.4 Los flujos nuevos necesitan revisión antes de empezar

La mayoría de los problemas de flujos de datos empiezan con una petición razonable: un proveedor quiere telemetría para diagnóstico remoto; un equipo de informes quiere una copia de los eventos de la pasarela clínica. Antes de que empiece un flujo así, se redacta y se revisa la entrada del registro: la revisan el responsable de los datos, seguridad (protección y conducto) y, cuando hay datos personales, la función de privacidad. Si transporta datos de control o de configuración, se aplica la regla de arquitectura del capítulo 8. La petición de Kell de recibir telemetría horaria de los retransmisores es el caso de Fallowmere: la entrada debe redactarse y revisarse antes de que se envíe la primera hora.

### 12.5 Ejemplo resuelto: el registro frente a la realidad (sintético)

El Lab 12 compara cinco entradas del registro con siete flujos observados. Cuatro flujos registrados coinciden. Tres diferencias importan:

1. **DF5 (de la pasarela clínica a Halden Cloud) conserva datos vinculados a pacientes durante 400 días frente a los 30 registrados.** El flujo está registrado y cifrado, pero la conservación en el destino no coincide. Es una cuestión de privacidad y de contrato; hay que informar al responsable de los datos del hospital y cotejar la configuración de conservación de Halden con el contrato.
2. **Un flujo no registrado del historiador a un sistema de soporte del proveedor, en texto claro.** Transporta telemetría (no personal, pero sensible desde el punto de vista operativo) sin cifrado y sin que nadie lo haya aprobado.
3. **Un flujo no registrado de la pasarela clínica al servidor de informes que transporta datos vinculados a pacientes.** Cifrado, pero nadie lo aprobó, y el servidor de informes está en la zona corporativa que usa el personal de agua.

El tercero es el más grave pese a ir cifrado: los datos vinculados a pacientes han llegado a un sistema y a un público sin ninguna finalidad registrada. El cifrado en tránsito protege el trayecto, no el destino.

### 12.6 Actividad práctica: comprobación del registro

**Lab 12** (guárdelo como `lab12.py` y ejecútelo con `python3 lab12.py`):

```python
# Lab 12 - checking a data-flow register against what the service actually sends (offline, standard library only)
# Synthetic: Fallowmere shared services. Each register entry: id, source, destination, data class, encrypted, retention days.
register = [
 ("DF1", "PS-*", "RLY-01", "telemetry", False, 0),
 ("DF2", "RLY-01", "HIST-01", "telemetry", True, 730),
 ("DF3", "HIST-01", "REPORTS", "telemetry-aggregate", True, 365),
 ("DF4", "WARD-PUMPS", "CLIN-GW", "patient-linked", True, 30),
 ("DF5", "CLIN-GW", "HALDEN-CLOUD", "patient-linked", True, 30),
]
observed = [  # source, destination, data class seen by sampling payload metadata, tls?, stored days at destination
 ("PS-04", "RLY-01", "telemetry", False, 0), ("RLY-01", "HIST-01", "telemetry", True, 730),
 ("HIST-01", "REPORTS", "telemetry-aggregate", True, 365), ("WARD-PUMPS", "CLIN-GW", "patient-linked", True, 30),
 ("CLIN-GW", "HALDEN-CLOUD", "patient-linked", True, 400), ("HIST-01", "VENDOR-SUPPORT", "telemetry", False, None),
 ("CLIN-GW", "REPORTS", "patient-linked", True, 365),
]
sensitive = {"patient-linked"}
def match(src, dst):
    for r in register:
        if (r[1] == src or (r[1].endswith("*") and src.startswith(r[1][:-1]))) and r[2] == dst:
            return r
for src, dst, cls, enc, keep in observed:
    r = match(src, dst)
    if r is None:
        sev = "HIGH" if cls in sensitive else "MED"
        print(f"{sev:<4} unregistered flow {src}->{dst} ({cls}, encrypted={enc})")
        continue
    issues = []
    if r[3] != cls: issues.append(f"class {cls} != registered {r[3]}")
    if r[4] and not enc: issues.append("registered encrypted but sent clear")
    if keep is not None and keep > r[5]: issues.append(f"kept {keep} d > registered {r[5]} d")
    print(f"{'OK  ' if not issues else 'HIGH' if cls in sensitive else 'MED '} {r[0]} {src}->{dst} {'; '.join(issues)}")
```

Salida esperada (Python 3.13.5):

```text
OK   DF1 PS-04->RLY-01 
OK   DF2 RLY-01->HIST-01 
OK   DF3 HIST-01->REPORTS 
OK   DF4 WARD-PUMPS->CLIN-GW 
HIGH DF5 CLIN-GW->HALDEN-CLOUD kept 400 d > registered 30 d
MED  unregistered flow HIST-01->VENDOR-SUPPORT (telemetry, encrypted=False)
HIGH unregistered flow CLIN-GW->REPORTS (patient-linked, encrypted=True)
```

La salida reproduce las tres diferencias anteriores. Antes de actuar, decida quién recibe cada una: la conservación de 400 días de DF5 va al responsable de los datos del hospital y a quien gestione el contrato con Halden; el flujo en texto claro del historiador al sistema de soporte del proveedor va al responsable de los datos de Agua y a FSTS Security; y el flujo no registrado de datos vinculados a pacientes hacia el servidor de informes va primero a la función de privacidad del hospital, porque un público de la zona corporativa puede haber visto ya los datos.

### 12.7 Errores frecuentes y límites

- Registrar caminos (conductos), pero no clases de datos ni conservación.
- Suponer que «cifrado» significa «aceptable».
- Tratar la telemetría operativa como inofensiva porque no es personal.
- Verificar las clases de datos leyendo usted mismo datos personales, en lugar de pedir al responsable de los datos que muestree metadatos.
- Dejar que empiece un flujo de proveedor o de informes antes de revisar la entrada.

El registro muestra lo que se conoce; los flujos que salen por rutas inesperadas (soportes extraíbles, el portátil de un proveedor) necesitan otros controles. El flujo no registrado de la pasarela clínica al servidor de informes es el segundo error en acción: cifrado y, aun así, inaceptable.

### Ejercicios — capítulo 12

**EX034 — Clasifique las diferencias por prioridad.** *Objetivo:* priorizar los hallazgos sobre flujos de datos. *Entradas:* la salida del Lab 12. *Restricciones:* una acción y un responsable por hallazgo. *Pasos:* (1) ordene los tres hallazgos; (2) indique la primera acción y el responsable; (3) indique cuál debe comunicarse a alguien ajeno a FSTS. *Evidencia esperada:* tabla. *Rúbrica:* 3 = CLIN-GW→REPORTS primero (datos vinculados a pacientes no aprobados ante un público equivocado: detener el flujo con el acuerdo del responsable de los datos del hospital, evaluar), la conservación de DF5 segundo (responsable de los datos del hospital y contrato con Halden), el texto claro hacia el soporte del proveedor tercero (detener o cifrar, registrar); reconoce que la necesidad de comunicarlo externamente la deciden el responsable de los datos y la función de privacidad; 2 = orden defendible, responsables vagos; 1 = ordena solo por cifrado; 0 = nada.

**EX035 — Redacte una entrada del registro.** *Objetivo:* especificar un flujo nuevo antes de que empiece. *Entradas:* Kell Instruments pide telemetría horaria de PS-09 para diagnóstico remoto. *Restricciones:* todos los campos del capítulo 12 («El registro»); incluya el conducto y la protección. *Pasos:* redacte la entrada y enumere quién debe aprobarla. *Evidencia esperada:* entrada y aprobadores. *Rúbrica:* 3 = origen y destino concretos (exportación del retransmisor o del historiador, no la RTU directamente), clase de datos telemetría operativa, transporte cifrado, campos y frecuencia mínimos, conservación limitada y contractual, propósito, responsable, aprobaciones del responsable de los datos de Agua y de seguridad de FSTS, con fecha de caducidad; 2 = un campo débil; 1 = «enviar datos a Kell»; 0 = nada.

**EX036 — Amplíe la comprobación.** *Objetivo:* añadir una comprobación a la herramienta. *Entradas:* el Lab 12. *Restricciones:* solo la biblioteca estándar. *Pasos:* (1) añada una comprobación que señale cualquier flujo de datos `patient-linked` cuyo destino no esté en una lista aprobada `{"CLIN-GW", "HALDEN-CLOUD"}`, aunque esté registrado; (2) registre `("DF6", "CLIN-GW", "REPORTS", "patient-linked", True, 365)` y vuelva a ejecutar; (3) explique por qué el mero registro no debería hacer aceptable ese flujo. *Evidencia esperada:* código, salida y explicación. *Rúbrica:* 3 = el flujo hacia REPORTS sigue señalado tras registrarlo; explicación de que el registro recoge decisiones, y de que un flujo registrado hacia un público no aprobado es una mala decisión que hay que revisar, no un resultado limpio; 2 = el código funciona, explicación escasa; 1 = no se ejecutó; 0 = nada.

### Síntesis del capítulo

Un registro de flujos de datos recoge qué datos viajan a dónde, cómo se protegen y cuánto tiempo se conservan. Clasifique los datos (telemetría, configuración, datos personales y vinculados a pacientes, registros de seguridad) y verifique el registro frente a lo que los sistemas realmente envían y conservan. El cifrado protege el trayecto, no el destino. Los flujos nuevos se revisan antes de empezar: los revisan el responsable de los datos, seguridad y, cuando hay datos personales, la función de privacidad.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Siga estudiando — capítulo 12 de 30

[← Capítulo 11](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Infraestructura crítica y seguridad sectorial: escenarios de riesgo

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- redactar un **escenario** de riesgo como una historia concreta: causa, camino, activo afectado, consecuencia para las personas y controles existentes;
- asignar franjas de consecuencia y de probabilidad con motivos explícitos, midiendo la consecuencia en personas y tiempo;
- ordenar los escenarios **primero por consecuencia** cuando interviene la seguridad física, y explicar por qué el producto probabilidad × consecuencia puede inducir a error;
- convertir los escenarios principales en trabajo de implementación con responsables.

La evaluación de riesgos puede hacerse con muchos niveles de profundidad; la guía del NIST describe un proceso completo para las organizaciones ([NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)). Este capítulo enseña la versión del implementador: redactar escenarios lo bastante precisos para que un tecnólogo pueda construir, probar y monitorizar los controles que implican.

### 13.1 Escenarios, no categorías

«Ransomware» es una categoría. Un escenario es: «Un ransomware entregado mediante un correo de phishing cifra HIST-01; los datos de las estaciones siguen llegando al retransmisor, que los almacena; los operadores pierden las pantallas de tendencias y los informes semanales de cumplimiento hasta que se restaura el historiador». Un buen escenario nombra la **causa**, el **camino**, el **activo afectado**, la **consecuencia** para las personas y el servicio, y los **controles existentes**. Así puede probarse («¿de verdad almacena el retransmisor? ¿durante cuánto tiempo?») y monitorizarse. R2 supera la prueba: credencial de proveedor robada, acceso remoto del proveedor, el punto de consigna de dosificación de PS-07, un cambio de cloro en el agua que bebe la gente.

### 13.2 Primero la consecuencia

La consecuencia describe lo que les ocurre a las personas: cuántas, durante cuánto tiempo y si alguien podría sufrir daños. Una clasificación por franjas sencilla usa personas × horas de interrupción, y cualquier efecto creíble sobre la seguridad física se sitúa en la franja más alta sean cuales sean las cifras. La **probabilidad** es una franja de juicio (de 1 a 5) basada en la exposición, las amenazas conocidas y el historial. Escriba el motivo de cada franja; una franja sin motivo no puede rebatirse.

Muchos registros ordenan por el producto probabilidad × consecuencia. El producto es cómodo y peligroso: trata como iguales una molestia frecuente y una catástrofe rara si los productos coinciden, y deja que un problema visto a menudo pero recuperable supere a un escenario de seguridad física. Cuando la seguridad física está en juego, ordene primero por consecuencia y después por probabilidad dentro de la franja; use el producto, si acaso, solo dentro de una misma franja de consecuencia. Los métodos basados en la consecuencia desarrollados para la infraestructura crítica adoptan la misma perspectiva: partir de los resultados que no deben ocurrir ([INL CCE](https://inl.gov/national-security/cce/)).

### 13.3 Controles existentes y riesgo residual

Para cada escenario, registre los controles que ya lo reducen y si se han probado (capítulo 23). Un control sin probar es una esperanza, y no debería rebajar mucho la franja. El **riesgo residual** (lo que queda después de los controles) necesita un responsable que lo haya aceptado, identificado por su función, con una fecha de revisión. Para R1, el ransomware en el historiador, el control clave es que el retransmisor almacene los datos de las estaciones mientras HIST-01 está caído. Mientras ese almacenamiento no se haya probado deteniendo el historiador a propósito y comprobando cuántas horas aguanta el retransmisor, es una esperanza, y la franja baja de R1 descansa en ella. El responsable del riesgo residual de R1 sería Operaciones de Agua, porque los informes de cumplimiento son suyos.

### 13.4 De los escenarios al trabajo

El valor del registro es el trabajo que produce. Para cada uno de los escenarios principales, enumere las tareas de implementación que reducirían la consecuencia o la probabilidad, y la monitorización que lo detectaría mientras ocurre. Un registro que no produce tareas es un documento; uno que produce tareas con responsables es un plan. Para R3, el llenado del disco del retransmisor, el trabajo es concreto: averiguar qué conserva los datos de RLY-01 más allá de 30 días, configurar una alerta de disco antes de la alarma del 85 % y probar el comportamiento del búfer cuando el disco está lleno. Para R2, son los controles de la cuenta del proveedor y la alerta de cloro fuera de banda que aparecen como fichas de control en el capítulo 18.

### 13.5 Ejemplo resuelto: seis escenarios de Fallowmere (sintético)

El Lab 13 ordena seis escenarios. Dos llevan la marca de seguridad física (una credencial de proveedor robada que se usa para cambiar el punto de consigna de dosificación de PS-07, R2, y una caída de la pasarela clínica que impide actualizar la biblioteca de fármacos de las bombas de infusión, R4) y pasan a la franja de consecuencia 5. Ordenados primero por consecuencia, R2 y R4 van en cabeza, seguidos del llenado del disco del retransmisor (R3) y del corte del operador de telecomunicaciones (R6). Ordenados por el producto, R3 (16) y R6 (12) superan a ambos escenarios de seguridad física (10 cada uno). La ordenación por producto enviaría el esfuerzo del próximo trimestre a la capacidad de disco: útil, pero no donde es posible el daño a las personas.

Fíjese también en R1, el ransomware en el historiador, al final con consecuencia 1. Eso refleja el diseño: la telemetría y el control continúan sin el historiador. No es un motivo para ignorar R1 (los informes de cumplimiento y las investigaciones dependen del historiador), sino un motivo para confiar en la propiedad de diseño del capítulo 8, *siempre que* se haya probado el almacenamiento del retransmisor.

R2 merece una nota. LANTERN no transporta órdenes, así que el camino de R2 no pasa por LANTERN. Pasa por el acceso remoto del proveedor al sistema de control. El registro de riesgos de un tecnólogo debería incluir escenarios que el servicio *no causa*, pero que *debe detectar o apoyar*: la telemetría de LANTERN es la forma en que los operadores advertirían un cambio inesperado de dosificación.

### 13.6 Actividad práctica: ordenación de escenarios

**Lab 13** (guárdelo como `lab13.py` y ejecútelo con `python3 lab13.py`):

```python
# Lab 13 - a small risk-scenario register ranked by consequence first (offline, standard library only)
# Synthetic: Fallowmere scenarios. Likelihood band 1-5 (judgement), consequence in service units.
scenarios = [  # id, scenario, likelihood band, people affected, hours of disruption, safety flag
 ("R1", "Ransomware encrypts historian; station data still reaches relay", 3, 0, 0, False),
 ("R2", "Stolen vendor credential used to change PS-07 dosing setpoint", 2, 41000, 24, True),
 ("R3", "Relay disk fills; telemetry dropped for remote stations", 4, 41000, 6, False),
 ("R4", "Clinical gateway outage stops infusion-pump library updates", 2, 300, 72, True),
 ("R5", "Depot kiosk defaced", 4, 0, 2, False),
 ("R6", "Upstream carrier outage isolates 6 stations", 3, 18000, 8, False),
]
def consequence_band(people, hours, safety):
    ph = people * hours
    band = 1 if ph == 0 else 2 if ph < 10_000 else 3 if ph < 100_000 else 4 if ph < 1_000_000 else 5
    return 5 if safety else band  # any credible safety effect goes to the top band
rows = []
for sid, text, lik, people, hours, safety in scenarios:
    c = consequence_band(people, hours, safety)
    rows.append((c, lik, sid, text, c * lik))
print("ranked by consequence, then likelihood:")
for c, lik, sid, text, prod in sorted(rows, key=lambda r: (-r[0], -r[1])):
    print(f"  {sid} C{c} L{lik} CxL={prod:>2}  {text}")
print("ranked by CxL product only:")
print("  " + " ".join(sid for c, lik, sid, text, prod in sorted(rows, key=lambda r: -r[4])))
```

Salida esperada (Python 3.13.5):

```text
ranked by consequence, then likelihood:
  R2 C5 L2 CxL=10  Stolen vendor credential used to change PS-07 dosing setpoint
  R4 C5 L2 CxL=10  Clinical gateway outage stops infusion-pump library updates
  R3 C4 L4 CxL=16  Relay disk fills; telemetry dropped for remote stations
  R6 C4 L3 CxL=12  Upstream carrier outage isolates 6 stations
  R5 C1 L4 CxL= 4  Depot kiosk defaced
  R1 C1 L3 CxL= 3  Ransomware encrypts historian; station data still reaches relay
ranked by CxL product only:
  R3 R6 R2 R4 R5 R1
```

Ejecútelo y compare las dos ordenaciones. Ordenados primero por consecuencia, R2 y R4 van en cabeza porque ambos llevan la marca de seguridad física en la franja 5. Ordenados por producto, R3 con 16 y R6 con 12 los adelantan, y R1 queda al final en ambos casos. Después cambie un dato de entrada que considere incierto, como la probabilidad de R2, y vea si desplaza a R2 por debajo de R3. Si la ordenación por consecuencia resiste su cambio y la ordenación por producto no, ese es el argumento que debe presentar a quienes asignan el trabajo del próximo trimestre.

### 13.7 Errores frecuentes y límites

- Redactar categorías en lugar de escenarios.
- Franjas sin motivos.
- Ordenar por producto cuando interviene la seguridad física.
- Rebajar la probabilidad por controles que nunca se han probado.
- Riesgo residual sin responsable.
- Dejar fuera escenarios ajenos a su sistema que su sistema debe detectar.

Las franjas son juicios. Su valor está en que hacen el razonamiento explícito y comparable, no en que midan el riesgo con precisión. El Lab 13 muestra el tercer error: ordenar por producto pone la capacidad de disco por encima de la dosificación de cloro.

Dejar fuera R2 porque LANTERN no transporta órdenes sería el sexto error: la telemetría de LANTERN es la forma en que los operadores advierten un cambio inesperado de dosificación.

### Ejercicios — capítulo 13

**EX037 — Redacte dos escenarios.** *Objetivo:* redactar escenarios que puedan probarse. *Entradas:* el diseño de LANTERN de los capítulos 2 y 8. *Restricciones:* cada uno debe nombrar causa, camino, activo, consecuencia (personas y tiempo) y controles existentes. *Pasos:* redacte un escenario sobre el operador BayTel y otro sobre el servidor de salto de FSTS. *Evidencia esperada:* dos escenarios de 80 a 120 palabras. *Rúbrica:* 3 = concretos, comprobables, con consecuencias en personas y tiempo y controles nombrados con su estado de prueba; 2 = un elemento vago; 1 = categorías; 0 = nada.

**EX038 — Producto frente a consecuencia.** *Objetivo:* explicar a un directivo una decisión de ordenación. *Entradas:* la salida del Lab 13. *Restricciones:* 150 palabras; sin jerga. *Pasos:* explique por qué R2 y R4 deberían abordarse antes que R3 aunque R3 puntúe más por producto, y qué sigue necesitando R3. *Evidencia esperada:* párrafo. *Rúbrica:* 3 = argumento claro sobre el posible daño a las personas, la irrecuperabilidad y el defecto del producto de dar el mismo peso a todo; reconoce que R3 sigue necesitando una acción de capacidad (capítulo 1) y que es barato de corregir; 2 = argumento parcial; 1 = solo «primero la seguridad»; 0 = nada.

**EX039 — Del escenario al trabajo.** *Objetivo:* producir tareas de implementación. *Entradas:* R2 (credencial de proveedor usada para cambiar un punto de consigna de dosificación). *Restricciones:* tareas que FSTS o Agua puedan ejecutar; cada una con responsable y evidencia de que se completó. *Pasos:* enumere tres tareas de prevención o reducción y dos de detección. *Evidencia esperada:* tabla. *Rúbrica:* 3 = por ejemplo, acceso de proveedor limitado en el tiempo con MFA (capítulo 7), registro de sesiones, límites de los puntos de consigna del PLC diseñados por Agua, alerta de telemetría ante un cambio de cloro o de dosificación fuera de una ventana aprobada y comparación de los valores de los puntos de consigna con una línea base aprobada; responsables y evidencia nombrados; 2 = tareas genéricas; 1 = menos de tres; 0 = nada.

### Síntesis del capítulo

Redacte los riesgos como escenarios concretos (causa, camino, activo, consecuencia y controles) para que puedan probarse y monitorizarse. Mida la consecuencia en personas y tiempo, sitúe arriba los efectos creíbles sobre la seguridad física y ordene primero por consecuencia; el producto probabilidad × consecuencia puede hacer que las molestias superen al daño. Asigne un responsable al riesgo residual, incluya los escenarios que su servicio debe detectar y convierta el registro en tareas.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Siga estudiando — capítulo 13 de 30

[← Capítulo 12](#ch-12) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Infraestructura crítica y seguridad sectorial: métodos I

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- redactar una **línea base de configuración** para una clase de equipo y mantenerla bajo control de versiones;
- aplicar un **control de cambios** proporcionado: cambios estándar, normales y de emergencia;
- planificar un cambio en un entorno operativo con comprobaciones previas, una ventana, una reversión y un paso de verificación;
- vincular cada cambio con evidencia de que se hizo tal como se aprobó.

Los capítulos 1 a 13 describieron sistemas, datos y riesgos. Este capítulo y el capítulo 16 tratan de *métodos*: las rutinas que un tecnólogo ejecuta cada semana. Métodos I cubre las líneas base y los cambios, porque casi todos los demás controles dependen de saber cómo debería ser un sistema y de controlar cómo cambia.

### 14.1 Líneas base de configuración

Una **línea base** es la configuración aprobada para una clase de sistema: paquetes instalados y sus versiones, servicios habilitados y sus direcciones de escucha, cuentas y grupos, permisos de archivos, ajustes de registro y de hora, y parámetros de seguridad. La guía del NIST sobre la gestión de la configuración orientada a la seguridad describe cómo establecer líneas base, controlar sus cambios y vigilar las desviaciones ([NIST SP 800-128](https://csrc.nist.gov/pubs/sp/800/128/upd1/final)). Escriba la línea base como un archivo bajo control de versiones, no como un documento en la carpeta de alguien: el capítulo 22 la usa para detectar la deriva automáticamente.

### 14.2 Un control de cambios que la gente use

El control de cambios existe para impedir que cambios sin revisar causen interrupciones o debiliten la seguridad. Los procesos demasiado pesados se eluden; así aparecen los servicios de depuración a la escucha y los scripts auxiliares sin explicación (capítulo 6). Un esquema proporcionado tiene tres tipos de cambio:

- **Cambios estándar**: preaprobados, de bajo riesgo y repetibles (añadir una estación a la lista de permitidos a partir de una solicitud aprobada). Siguen un procedimiento escrito y se registran.
- **Cambios normales**: se revisan y aprueban antes de implantarse, con un plan y una reversión.
- **Cambios de emergencia**: se hacen con rapidez para restablecer el servicio o contener un incidente, los aprueba una autoridad de guardia designada y se revisan después.

En TO, la aprobación de cualquier cambio que pueda afectar al proceso físico incluye al responsable de operaciones, no solo a TI.

### 14.3 Planificar un cambio en un entorno operativo

Un plan de cambio para LANTERN indica: qué cambiará y por qué; los sistemas y clientes afectados; las comprobaciones previas (copias de seguridad hechas, reversión preparada, operaciones informadas); la **ventana** (acordada con operaciones: no durante el pico de demanda de la mañana ni durante la ejecución programada de un informe); la implantación paso a paso; la **verificación** (cómo sabrá que funcionó: comprobaciones concretas, no «probar el servicio»); los criterios y pasos de **reversión**; y a quién llamar. El capítulo 27 amplía esto a los despliegues con canarios.

Mover el servicio SSH a la escucha de RLY-02 es un caso típico: la reversión no debe depender de SSH.

### 14.4 Evidencia del cambio

Después de un cambio, tres cosas deberían coincidir: el registro del cambio (lo que se aprobó), la línea base bajo control de versiones (lo que ahora debería ser cierto) y el propio sistema (lo que es cierto, verificado con la comprobación de integridad del capítulo 6 y la comprobación de deriva del capítulo 22). Cuando no coinciden, o el cambio no se hizo tal como se aprobó o el registro es erróneo. Ambas cosas son hallazgos. Después de CHG-118, las tres coincidían para `allow.list` y no coincidían para el servicio de depuración a la escucha.

Para el servicio de depuración no existía ningún registro de cambio, así que la propia discrepancia era el hallazgo, y condujo a la investigación del capítulo 6.

### 14.5 Ejemplo resuelto: añadir PS-11 (sintético)

Operaciones de Agua pone en servicio una estación nueva, PS-11. Añadirla a LANTERN es un cambio estándar con un procedimiento escrito: (1) recibir la solicitud de puesta en servicio con el ID de la estación, su dirección y su responsable; (2) confirmar que el conducto ya cubre la subred de la estación; (3) añadir `PS-11` a la lista de permitidos bajo control de versiones, con la revisión de un segundo tecnólogo; (4) desplegar la lista de permitidos en los retransmisores; (5) verificar: los primeros mensajes de PS-11 aparecen como `accept` en el registro del retransmisor; la comprobación de integridad muestra que `allow.list` cambió con CHG-118 y nada más; (6) actualizar el inventario y el registro de flujos de datos. En el laboratorio del capítulo 6, esta fue la única diferencia *aprobada*. Las otras tres diferencias no tenían registro de cambio, y así fue como el método las reveló.

### 14.6 Actividad práctica: redacte un plan de cambio normal

Redacte un plan de cambio completo para: «Mover el servicio SSH a la escucha de RLY-02 de todas las interfaces solo a la interfaz de gestión». Incluya todos los elementos del capítulo 14 («Planificar un cambio en un entorno operativo»). Preste atención al riesgo de quedarse fuera: ¿cómo llegará al equipo si el cambio falla? Para el cambio de RLY-02, un plan seguro mantiene una segunda vía de entrada: el acceso de consola a través del hipervisor, o una sesión abierta en la interfaz de gestión, probada antes de mover el servicio. La verificación es concreta: SSH responde en la dirección de gestión, no responde en la dirección orientada a las estaciones, y la comprobación de deriva muestra que solo cambió la línea prevista. Elija la ventana con operaciones de Agua, evitando el pico de demanda de la mañana y las ejecuciones semanales del informe los días 6 y 7.

### 14.7 Errores frecuentes y límites

- Líneas base guardadas como documentos que nadie compara con los sistemas.
- Procesos de cambio tan pesados que la gente los elude.
- Ventanas de cambio elegidas por comodidad de TI y no de operaciones.
- «Verificar que el servicio funciona» como paso de verificación.
- Planes de reversión que nunca se probaron.
- Cambios de emergencia que nunca se revisan después y acaban siendo permanentes.

El control de cambios controla los cambios *autorizados*. No detecta los cambios no autorizados; esa es la tarea de las comprobaciones de integridad y de deriva.

La fusión de NTP del capítulo 25 es el cuarto error en la práctica: su criterio de aceptación decía solo «actualizar los servidores NTP».

### Ejercicios — capítulo 14

**EX040 — Clasifique cambios.** *Objetivo:* aplicar un control de cambios proporcionado. *Entradas:* (a) añadir una estación a la lista de permitidos; (b) actualizar el software del retransmisor a una nueva versión menor; (c) deshabilitar a las 02:00 una cuenta de proveedor comprometida; (d) cambiar la conservación del historiador de 730 a 365 días; (e) rotar la clave HMAC del retransmisor. *Restricciones:* estándar, normal o de emergencia para cada uno, con un motivo. *Pasos:* clasifique e indique quién aprueba. *Evidencia esperada:* tabla. *Rúbrica:* 3 = (a) estándar, (b) normal, (c) de emergencia con aprobación de guardia y revisión, (d) normal con aprobación del responsable de los datos porque afecta a los registros y a las obligaciones, (e) normal (o estándar una vez que exista un procedimiento probado) coordinado con las estaciones; aprobadores razonables; 2 = uno mal clasificado; 1 = todos normales; 0 = nada.

**EX041 — Pasos de verificación.** *Objetivo:* redactar una verificación concreta. *Entradas:* el cambio «el retransmisor reenvía a HIST-01 sobre TLS 1.3 en lugar de TLS 1.2». *Restricciones:* al menos cuatro comprobaciones; cada una observable. *Pasos:* enumere las comprobaciones y la evidencia que produce cada una. *Evidencia esperada:* lista. *Rúbrica:* 3 = por ejemplo, el registro de conexiones muestra TLS 1.3 negociado, el historiador recibe lecturas de todas las estaciones con la latencia normal, no aumentan los errores ni los rechazos del retransmisor, la validación de certificados sigue aplicándose y la comprobación de integridad muestra que solo cambió el archivo aprobado; 2 = tres; 1 = «probarlo»; 0 = nada.

**EX042 — Revise un cambio de emergencia.** *Objetivo:* cerrar el ciclo del cambio de emergencia. *Entradas:* durante una interrupción a las 03:00, un ingeniero abrió tcp/22 desde la zona corporativa directamente a todos los retransmisores «temporalmente». *Restricciones:* revisión posterior al cambio en un día laborable. *Pasos:* (1) enumere las preguntas que plantea la revisión; (2) decida qué ocurre con la regla; (3) indique qué cambio de proceso evita que se repita. *Evidencia esperada:* nota de revisión. *Rúbrica:* 3 = pregunta por qué falló la ruta del servidor de salto, quién aprobó y a qué se accedió durante la ventana (registros), elimina o restringe la regla con un registro de cambio y corrige la resiliencia del servidor de salto o el diseño del acceso de emergencia; 2 = regla eliminada pero sin causa raíz; 1 = regla mantenida; 0 = nada.

### Síntesis del capítulo

Escriba las configuraciones aprobadas como líneas base bajo control de versiones. Aplique el control de cambios de forma proporcionada (estándar, normal y de emergencia), con operaciones aprobando los cambios que puedan afectar al proceso físico. Planifique los cambios con comprobaciones previas, una ventana acordada, una verificación concreta y una reversión probada. Después de cada cambio, el registro, la línea base y el sistema deberían coincidir; cuando no coinciden, tiene usted un hallazgo.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Siga estudiando — capítulo 14 de 30

[← Capítulo 13](#ch-13) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Infraestructura crítica y seguridad sectorial: laboratorio guiado

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- explicar qué demuestra un **código de autenticación de mensajes** (MAC) y qué no demuestra;
- implementar el sellado y la verificación con HMAC-SHA-256 mediante una comparación en tiempo constante;
- añadir **frescura** (ventana temporal) y **orden** (números de secuencia) para frustrar la reproducción;
- probar la construcción con mensajes deliberadamente erróneos y registrar los resultados como evidencia.

Esta es la primera construcción guiada del componente central de LANTERN. El validador del capítulo 3 comprueba que los mensajes estén bien formados y sean plausibles; no puede saber si un mensaje procede realmente de una estación. Aquí se añade la autenticación. El diseño es deliberadamente sencillo para que cada línea pueda entenderse; un diseño de producción añadiría la gestión de claves y la seguridad del transporte (véase «Lo que esta construcción no hace», más abajo).

### 15.1 Integridad y autenticidad

Un **hash** como SHA-256 detecta los cambios accidentales, pero cualquiera puede calcularlo, de modo que un atacante que modifica un mensaje también puede recalcular su hash. Un **MAC** se calcula con una clave secreta; solo quienes poseen la clave pueden producir un MAC válido. HMAC, definido en el [RFC 2104](https://www.rfc-editor.org/rfc/rfc2104), construye un MAC a partir de una función hash. Si un mensaje lleva un HMAC válido con la clave de una estación, el receptor sabe que lo produjo un poseedor de la clave y que no se modificó en tránsito.

Un MAC **no** proporciona confidencialidad (el mensaje sigue siendo legible), no demuestra que el *sensor* de la estación sea correcto y no impide que un atacante reenvíe un mensaje capturado anteriormente: una **reproducción**.

### 15.2 Forma canónica

Un MAC se calcula sobre bytes. Si el emisor y el receptor serializan el mismo mensaje de forma distinta (otro orden de claves, otros espacios), la verificación falla. Los mensajes de LANTERN se serializan como JSON con las claves ordenadas y sin espacios, y el MAC se calcula exactamente sobre esos bytes. Defina siempre la forma canónica de manera explícita. Un retransmisor que vuelve a serializar el JSON analizado antes de comprobar el MAC puede aceptar bytes que la estación nunca firmó.

El Lab 15 serializa con las claves ordenadas y sin espacios en ambos lados, de modo que la pasarela de la estación y el retransmisor calculan el MAC sobre bytes idénticos; una actualización del firmware de la pasarela que cambiara los espacios se manifestaría de inmediato como una ráfaga de fallos de MAC de esa estación.

### 15.3 Comparación en tiempo constante

Comparar el MAC recibido con el esperado mediante una comparación de cadenas ordinaria puede revelar, a través del tiempo de respuesta, cuántos caracteres iniciales coincidieron. La función `hmac.compare_digest` de Python compara en un tiempo que no depende de dónde difieren las entradas ([documentación de hmac de Python](https://docs.python.org/3/library/hmac.html)). Úsela en todas las comparaciones de MAC. Tanto el Lab 15 como el Lab 29 usan `hmac.compare_digest`, nunca `==`, y el retransmisor que rechazó 40 de 40 pruebas de fallo de MAC en el capítulo 23 debe hacer lo mismo.

Una comparación ordinaria permitiría a un atacante situado en la red de las estaciones averiguar, carácter a carácter, un MAC válido para una lectura de cloro falsificada.

### 15.4 Frescura y orden

Dos comprobaciones baratas frustran la reproducción. Una **ventana temporal** rechaza los mensajes cuya marca de tiempo se aleja del reloj del receptor más de un número fijado de segundos (aquí, 120 s); depende de que ambos relojes sean correctos (capítulo 17). Un **número de secuencia** por estación, que aumenta con cada mensaje, permite al receptor rechazar cualquier mensaje cuyo número no sea mayor que el último aceptado. Ambos valores van dentro del cuerpo protegido por el MAC, así que un atacante no puede cambiarlos sin invalidar el MAC.

El error de reloj de 422 segundos de PS-09 muestra el coste: sus mensajes legítimos no superarían la ventana de 120 s.

### 15.5 Construcción guiada

El laboratorio siguiente implementa `seal` (el lado de la estación) y `Relay.receive` (el lado del retransmisor) y ejecuta siete pruebas: dos mensajes correctos, una reproducción, un valor manipulado, un mensaje sellado con la clave equivocada, un mensaje caducado y un mensaje truncado. **Lab 15** (guárdelo como `lab15.py` y ejecútelo con `python3 lab15.py`):

```python
# Lab 15 - guided build: an authenticated telemetry relay message with replay protection (offline, stdlib only)
# Synthetic key and messages. A real deployment keeps the key in a protected store, never in source code.
import hmac, hashlib, json
KEY = bytes.fromhex("6c616e7465726e2d6c61622d6b65792d6e6f742d7265616c2d30303031")  # "lantern-lab-key-not-real-0001"
WINDOW = 120  # seconds
def seal(station, tag, value, ts, seq, key=KEY):
    body = json.dumps({"st": station, "tag": tag, "v": value, "ts": ts, "seq": seq}, sort_keys=True, separators=(",", ":"))
    mac = hmac.new(key, body.encode(), hashlib.sha256).hexdigest()
    return body + "." + mac
class Relay:
    def __init__(self, key): self.key, self.last = key, {}
    def receive(self, wire, now):
        try:
            body, mac = wire.rsplit(".", 1)
        except ValueError:
            return "reject: malformed"
        good = hmac.new(self.key, body.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(good, mac):
            return "reject: bad MAC"
        m = json.loads(body)
        if abs(now - m["ts"]) > WINDOW:
            return "reject: outside time window"
        if m["seq"] <= self.last.get(m["st"], -1):
            return "reject: replay"
        self.last[m["st"]] = m["seq"]
        return f"accept {m['st']} {m['tag']}={m['v']}"
r = Relay(KEY)
now = 1_790_000_000
a = seal("PS-04", "LEVEL_M", 3.42, now - 5, 1)
b = seal("PS-04", "LEVEL_M", 3.44, now - 1, 2)
tampered = a.replace('"v":3.42', '"v":9.42')
forged = seal("PS-04", "LEVEL_M", 1.00, now, 3, key=b"guessed-key")
old = seal("PS-07", "CL2_MGL", 0.6, now - 900, 1)
tests = [("first", a), ("second", b), ("replay of first", a), ("tampered value", tampered),
         ("wrong key", forged), ("stale", old), ("truncated", a[:20])]
for name, wire in tests:
    print(f"{name:<16} {r.receive(wire, now)}")
print("MAC length (hex chars):", len(a.rsplit('.', 1)[1]))
```

Salida esperada (Python 3.13.5):

```text
first            accept PS-04 LEVEL_M=3.42
second           accept PS-04 LEVEL_M=3.44
replay of first  reject: replay
tampered value   reject: bad MAC
wrong key        reject: bad MAC
stale            reject: outside time window
truncated        reject: malformed
MAC length (hex chars): 64
```

Trabájelo en este orden: (1) lea `seal` e identifique la forma canónica; (2) lea `receive` y enumere las comprobaciones en orden; (3) prediga el resultado de cada prueba; (4) ejecútelo; (5) para cada rechazo, nombre la comprobación que lo detectó. Después cambie el orden de las comprobaciones para que la comprobación de reproducción *y su actualización de estado* se ejecuten antes que la comprobación del MAC, y piense en lo que podría hacer ahora un atacante: enviar mensajes sin autenticar con números de secuencia altos y bloquear una estación. El orden importa: primero autentique y después confíe en el contenido.

### 15.6 Lo que esta construcción no hace

La clave del laboratorio aparece en el código fuente porque es falsa; en producción, la clave reside en un almacén protegido, legible solo por la cuenta de servicio del retransmisor, y cada estación tiene su propia clave para que una clave robada no permita a un atacante suplantar a todas las estaciones. Las claves necesitan procedimientos de generación, distribución, rotación y revocación (capítulo 18). Aquí el transporte no está cifrado; en producción, el tramo entre el retransmisor y el historiador usa TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)), y que el tramo de las estaciones pueda usar TLS depende de lo que admitan los dispositivos de campo. Muchos dispositivos de campo antiguos no pueden calcular HMAC en absoluto; en ese caso, el MAC lo aplica una pequeña pasarela en la estación, y el enlace entre la pasarela y el dispositivo debe protegerse físicamente.

### 15.7 Errores frecuentes y límites

- Usar un hash simple y llamarlo autenticación.
- Calcular el MAC sobre un objeto vuelto a serializar en lugar de sobre los bytes recibidos.
- Comparar los MAC con `==`.
- Actualizar el estado de reproducción antes de la autenticación, o antes de que se hayan superado todas las demás comprobaciones.
- Una sola clave compartida por todas las estaciones.
- Claves en el código fuente, en repositorios de configuración o en incidencias.
- Suponer que un MAC válido significa una lectura correcta.

Cada uno tiene una consecuencia en LANTERN. Un hash simple permite a cualquiera que alcance el retransmisor calcular un resumen de aspecto válido. Una sola clave para todas las estaciones significa que una clave extraída de la pasarela de PS-07, donde el archivo de la clave estaba en una tarjeta extraíble, falsifica mensajes de las catorce estaciones. Y un MAC válido en una lectura de cloro de 9,80 mg/L solo demuestra que la envió PS-07, no que el analizador sea correcto.

### Ejercicios — capítulo 15

**EX043 — Orden de las comprobaciones.** *Objetivo:* ver por qué la autenticación va primero. *Entradas:* el Lab 15. *Restricciones:* modifique una copia. *Pasos:* (1) mueva la comprobación de reproducción antes de la comprobación del MAC, dejando la actualización de estado donde está; (2) construya un mensaje sin autenticar para PS-04 con `seq` 1000000 y un MAC erróneo; (3) envíelo y después un mensaje legítimo con `seq` 3; (4) informe de lo que ocurre y de por qué el orden original es más seguro. *Evidencia esperada:* código, salida y explicación. *Rúbrica:* 3 = muestra que, con el estado actualizado antes de la autenticación, un atacante puede bloquear los mensajes futuros de una estación (o, si la actualización de estado sigue después de la comprobación del MAC, muestra que no hay bloqueo y explica por qué la posición de la actualización es la verdadera salvaguarda); la explicación enlaza con «autenticar y después confiar»; 2 = observación sin explicación; 1 = no ejecutado; 0 = nada.

**EX044 — Claves por estación.** *Objetivo:* ampliar el diseño. *Entradas:* el Lab 15. *Restricciones:* solo la biblioteca estándar. *Pasos:* (1) dé a cada estación su propia clave en un diccionario; (2) busque la clave por el ID de estación, pero tenga en cuenta que el ID de estación está dentro del cuerpo; (3) explique cómo puede leer con seguridad el ID de estación antes de verificar el MAC y qué no debe hacer con él antes de la verificación. *Evidencia esperada:* código y explicación. *Rúbrica:* 3 = analiza el cuerpo solo para seleccionar una clave, verifica el MAC con esa clave antes de usar cualquier otro campo o de actualizar el estado y rechaza las estaciones desconocidas; explica que el ID sin verificar es solo un selector de clave; 2 = funciona, explicación escasa; 1 = usa una sola clave; 0 = nada.

**EX045 — Tamaño de la ventana.** *Objetivo:* elegir la ventana de frescura. *Entradas:* los relojes de las estaciones se mantienen dentro de ±2 s mediante NTP desde el retransmisor; el operador de telecomunicaciones retrasa a veces los mensajes hasta 40 s; tras una caída del operador, las estaciones suben una acumulación de 24 horas. *Restricciones:* un único diseño que resuelva los tres casos. *Pasos:* (1) elija una ventana para los mensajes en vivo; (2) explique cómo deben tratarse las subidas de la acumulación sin abrir una brecha de reproducción. *Evidencia esperada:* media página. *Rúbrica:* 3 = ventana en vivo de unos 60–120 s razonada; acumulación aceptada por una vía separada y explícita (por ejemplo, un modo de acumulación marcado que siga exigiendo un MAC válido y números de secuencia estrictamente crecientes, con una antigüedad acotada y una alerta cuando se use); 2 = ventana correcta, acumulación insegura o vaga; 1 = ventana muy grande para todo; 0 = nada.

### Síntesis del capítulo

Autentique los mensajes con HMAC sobre una forma canónica definida, compare los MAC en tiempo constante y frustre la reproducción con una ventana temporal y números de secuencia por estación incluidos en el cuerpo autenticado. Primero autentique; después confíe en el contenido y regístrelo. Un MAC demuestra el origen y la integridad, no la confidencialidad ni la corrección del sensor. Las claves necesitan su propio ciclo de vida, y cada estación debería tener la suya.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Siga estudiando — capítulo 15 de 30

[← Capítulo 14](#ch-14) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Infraestructura crítica y seguridad sectorial: métodos II

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- aplicar una rutina de gestión de vulnerabilidades: recepción, aplicabilidad, priorización, tratamiento y verificación;
- priorizar las correcciones a partir de la evidencia de explotación, la exposición y la consecuencia para el activo, y no solo de la puntuación de gravedad;
- planificar la aplicación de parches cuando el dispositivo no puede parchearse con rapidez, mediante controles compensatorios con fecha de fin;
- diseñar, ejecutar y registrar copias de seguridad y **pruebas de restauración** que demuestren la recuperación dentro de un tiempo objetivo.

Métodos I (capítulo 14) controlaba los cambios. Métodos II cubre las dos rutinas que con más frecuencia deciden lo malo que llega a ser un mal día: ocuparse de las vulnerabilidades antes de que se exploten y recuperarse cuando, aun así, algo se pierde.

### 16.1 Recepción de vulnerabilidades y aplicabilidad

Los avisos llegan de fabricantes, agencias nacionales y listas de correo de seguridad. La primera pregunta es la **aplicabilidad**: ¿usamos el producto y la versión afectados, en una configuración en la que el fallo importa? Esto depende de que el inventario (capítulo 11) sea exacto en las versiones. Registre la decisión («aplicable», «no aplicable (motivo)», «desconocido (acción para averiguarlo)») para cada aviso que afecte a un producto del inventario. «Desconocido» es habitual en TO y debe tener un responsable. Para el aviso del Arlen 300, el inventario contenía ambas versiones: PS04-PLC con la 4.2 y PS07-PLC con la 3.9.

### 16.2 Priorización

Una puntuación de gravedad describe el fallo en general; su prioridad depende de su situación. Tres preguntas la afinan. **¿Se está explotando?** El catálogo de vulnerabilidades explotadas conocidas de la CISA enumera los fallos con evidencia de explotación activa ([CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)); esas entradas pasan al frente. **¿Está expuesto?** Un fallo alcanzable desde internet o desde la zona corporativa es más urgente que uno alcanzable solo desde dentro de un conducto bien controlado. **¿Cuál es la consecuencia?** Un fallo en un activo de criticidad 1 de la zona de estaciones importa más que uno en un quiosco de las cocheras. Las guías de gestión de parches lo tratan como una planificación basada en el riesgo, con planes de mantenimiento definidos para los distintos grupos de activos ([NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final)).

### 16.3 Tratamiento cuando no se puede parchear con rapidez

Los controladores de las estaciones pueden necesitar firmware certificado por el fabricante, una visita a la instalación, una ventana de interrupción y una nueva prueba del proceso. El tratamiento tiene entonces dos partes: **controles compensatorios ya** (restringir más el conducto, deshabilitar la función vulnerable si no se usa, añadir monitorización de los intentos de explotación, intensificar la revisión de la configuración del dispositivo) y **un plan con fecha** para la corrección. Registre ambas cosas, y también al responsable del riesgo residual (capítulo 13). Recuerde el capítulo 9: estos elementos abiertos durante mucho tiempo deben aparecer en sus medidas de parcheo.

PS04-PLC y PS07-PLC son el caso de Fallowmere: deshabilitar la interfaz web que no se usa, cerrar la ruta corporativa→PS-04, alertar sobre el puerto web y, después, el firmware 4.3 en las próximas visitas a las instalaciones.

### 16.4 Verificación

Una corrección está completa cuando se verifica en el dispositivo: la versión se confirma (desde el dispositivo o su exportación de ingeniería, no desde la incidencia), el servicio funciona (las comprobaciones del capítulo 27) y los controles compensatorios que ya no hacen falta se eliminan con control de cambios; de lo contrario, las reglas temporales se acumulan. Para PS07-PLC, la versión se leyó del dispositivo en la visita a la instalación: 3.9, tal como estaba registrada, así que la corrección sigue abierta. Cuando se instale la 4.3, la evidencia será la exportación del ingeniero que muestre la 4.3, y la alerta sobre el puerto web del PLC se mantendrá o se eliminará con su propio registro de cambio.

### 16.5 Copias de seguridad y pruebas de restauración

Una copia de seguridad que no se ha restaurado es una esperanza. La guía del NIST sobre planificación de contingencias cubre la planificación y la prueba de las copias de seguridad y de la recuperación ([NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)), y la guía del NIST sobre la recuperación tras ciberincidentes insiste en preparar y ejercitar la recuperación de antemano ([NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final)). Para LANTERN:

- **Qué** se copia: la configuración del retransmisor y la lista de permitidos (ya bajo control de versiones), las claves (en la copia de seguridad propia de su almacén protegido), la base de datos del historiador, los programas y configuraciones de los controladores (a cargo de los ingenieros de Agua) y la documentación necesaria para reconstruir.
- **Dónde**: al menos una copia fuera de línea o inmutable, para que un *ransomware* o un error de un administrador no puedan borrar todas las copias.
- **Objetivos**: un **objetivo de tiempo de recuperación** (RTO: con qué rapidez debe volver el servicio) y un **objetivo de punto de recuperación** (RPO: cuánta pérdida de datos es tolerable). Para HIST-01 en Fallowmere: RTO de 4 horas y RPO de 24 horas.
- **Pruebas de restauración**: programadas, cronometradas y registradas, con el resultado comparado con los objetivos; el capítulo 9 muestra cómo informar de ellas con honestidad.

### 16.6 Ejemplo resuelto: un aviso para el Arlen 300 (sintético)

Un aviso informa de un fallo en la interfaz web de gestión del PLC Arlen 300, con firmware anterior a la 4.3, que ya figura como explotado en otros lugares (sintético). Aplicabilidad: PS04-PLC ejecuta la 4.2 y PS07-PLC la 3.9; ambos son aplicables. Exposición: la interfaz web solo debería ser alcanzable desde la ruta de salto de ingeniería; pero la revisión de flujos del capítulo 2 encontró una estación de trabajo corporativa comunicándose directamente con PS-04. Prioridad: alta en las tres preguntas. Tratamiento: hoy, confirmar con el ingeniero de Agua si se usa la interfaz web y, si no, deshabilitarla; cerrar la ruta corporativa→PS-04 (ya notificada); añadir una alerta ante cualquier conexión al puerto web de los PLC. Corrección: firmware 4.3 en las próximas visitas a las instalaciones, con las pruebas del proceso de Agua. Verificación: versión leída de la exportación de ingeniería; alerta y conducto probados.

### 16.7 Actividad práctica: registro de vulnerabilidad

Redacte el registro completo del aviso del capítulo 16 («Ejemplo resuelto: un aviso para el Arlen 300»): aplicabilidad por activo, prioridad con los motivos de cada una de las tres preguntas, controles compensatorios con evidencia, plan de corrección con fechas y responsables, pasos de verificación y responsable del riesgo residual. La prioridad de PS04-PLC descansa en tres respuestas: aplicable (la 4.2 es anterior a la 4.3), explotado en otros lugares y expuesto, porque la revisión de flujos vio una estación de trabajo corporativa comunicándose con PS-04. PS07-PLC es aplicable y explotado, pero no se ha visto ninguna ruta no declarada, así que su motivo de exposición es más débil. Designe a operaciones de Agua como responsable del riesgo residual hasta que la 4.3 esté verificada en ambos.

### 16.8 Errores frecuentes y límites

- Priorizar solo por la puntuación de gravedad.
- Marcar «no aplicable» sin comprobar las versiones.
- Dejar «desconocido» sin responsable.
- Controles compensatorios sin fecha de fin, que acaban siendo permanentes.
- Cerrar la incidencia cuando el parche está programado, no cuando está verificado.
- Copias de seguridad guardadas donde la misma cuenta de administrador puede borrar todas las copias.
- Medir el éxito de las copias por la finalización de los trabajos en lugar de por las pruebas de restauración.

Ambos PLC muestran el riesgo del quinto error: la incidencia se cerraría en «firmware 4.3 programado», mientras la 3.9 sigue funcionando en PS-07.

La 4.2 de PS04-PLC habría quedado marcada como no aplicable por cualquiera que leyera solo la puntuación del aviso.

### Ejercicios — capítulo 16

**EX046 — Priorice tres avisos.** *Objetivo:* aplicar explotación, exposición y consecuencia. *Entradas:* (a) fallo de gravedad crítica en el navegador del quiosco de las cocheras, sin explotación conocida, quiosco en la red de las cocheras con acceso a internet; (b) fallo de gravedad media en el servidor SSH del retransmisor, incluido en el KEV, con SSH alcanzable solo desde el servidor de salto; (c) fallo de gravedad alta en la base de datos de HIST-01, sin explotación conocida, alcanzable desde la zona corporativa. *Restricciones:* ordene y justifique con una frase cada uno. *Pasos:* ordene y después dé una fecha objetivo para cada uno. *Evidencia esperada:* tabla. *Rúbrica:* 3 = (b) primero por la explotación activa y la criticidad, pese a la puntuación media y la exposición restringida; después, un orden defendible de (c) y (a) con motivos (consecuencia del historiador frente a exposición a internet del quiosco); fechas proporcionadas; 2 = orden defendible, motivos escasos; 1 = solo por gravedad; 0 = nada.

**EX047 — Plan de controles compensatorios.** *Objetivo:* tratar una vulnerabilidad que no puede parchearse con rapidez. *Entradas:* el capítulo 16 («Ejemplo resuelto: un aviso para el Arlen 300»); el firmware 4.3 solo puede instalarse en PS-07 dentro de 10 semanas. *Restricciones:* al menos tres controles, cada uno con evidencia y fecha de fin. *Pasos:* redacte el plan. *Evidencia esperada:* tabla. *Rúbrica:* 3 = deshabilitar la interfaz web si no se usa (evidencia: exportación de ingeniería), restricción del conducto verificada mediante la revisión de flujos, alerta ante conexiones al puerto web probada, comparación de la configuración intensificada; todo termina cuando la 4.3 esté verificada; 2 = sin fechas de fin; 1 = «monitorizar»; 0 = nada.

**EX048 — Diseño de una prueba de restauración.** *Objetivo:* diseñar una prueba de restauración que demuestre el RTO. *Entradas:* HIST-01, RTO de 4 h, RPO de 24 h. *Restricciones:* no debe perturbar la producción; debe ser repetible. *Pasos:* (1) describa el entorno de prueba; (2) los pasos y los puntos de cronometraje; (3) los criterios de superación; (4) lo que se registra. *Evidencia esperada:* una página. *Rúbrica:* 3 = destino de restauración aislado, parte de la copia fuera de línea o inmutable, cronometra desde «decisión de restaurar» hasta «los operadores pueden consultar los datos», comprueba la antigüedad de los datos frente al RPO, registra tiempos, carencias y lecciones, y se programa con regularidad; 2 = falta el cronometraje o la comprobación del RPO; 1 = «comprobar que el trabajo de copia terminó bien»; 0 = nada.

### Síntesis del capítulo

Gestione las vulnerabilidades como una rutina: decida la aplicabilidad a partir del inventario, priorice por explotación, exposición y consecuencia, aplique controles compensatorios con fechas de fin cuando el parcheo sea lento y verifique las correcciones en el dispositivo. Copie lo que necesita para reconstruir, conserve una copia que no puedan borrar las mismas personas que gestionan la producción, fije el RTO y el RPO, y demuéstrelos con pruebas de restauración cronometradas.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Siga estudiando — capítulo 16 de 30

[← Capítulo 15](#ch-15) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Infraestructura crítica y seguridad sectorial: herramientas

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- configurar los sistemas para que produzcan registros que respondan a preguntas operativas y de seguridad;
- mantener los relojes sincronizados y registrar la hora en un formato único y sin ambigüedad;
- **normalizar** los registros de distintas fuentes en una estructura común;
- escribir y probar una herramienta pequeña para poder confiar en su salida, y saber cuándo usar en su lugar una ya existente.

La monitorización (capítulo 19), la resolución de problemas (capítulo 20) y la evaluación (capítulo 23) dependen de los registros. La mayoría de los fallos de registro no se deben a productos que faltan, sino a aspectos básicos que faltan: una fuente que nunca reenvió, una marca de tiempo sin zona horaria, un analizador que descarta en silencio las líneas que no entiende.

### 17.1 Qué registrar

Registre lo que necesitará para responder a las preguntas que le harán: quién inició sesión, desde dónde y con qué resultado; qué configuración cambió; qué aceptó, rechazó y puso en cuarentena el retransmisor, con recuentos; qué flujos cruzaron los límites de zona; cuándo se iniciaron, se detuvieron o fallaron los servicios. La guía del NIST sobre la gestión de registros cubre la planificación, la generación, la transmisión, el almacenamiento y el análisis de los registros ([NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final)). Reenvíe los registros fuera del equipo con prontitud (no puede confiarse en que un equipo comprometido o averiado conserve sus propios registros) y vigile que el reenvío continúe.

### 17.2 La hora

Ordenar los eventos entre sistemas exige una hora acordada. Sincronice cada equipo con una fuente de hora de confianza mediante NTP ([RFC 5905](https://www.rfc-editor.org/rfc/rfc5905)); en LANTERN, los retransmisores toman la hora de dos servidores internos y la sirven a las estaciones. Registre las marcas de tiempo en un formato con desfase explícito, como los definidos en el [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339), y conviértalas a UTC para el análisis. Vigile el propio desfase del reloj: un equipo cuya fuente de hora ha fallado deriva de forma lenta y silenciosa.

### 17.3 Registros estructurados y syslog

El protocolo syslog, [RFC 5424](https://www.rfc-editor.org/rfc/rfc5424), define un mensaje con prioridad (instalación y gravedad), versión, marca de tiempo, nombre de equipo, nombre de aplicación, ID de proceso, ID de mensaje, **datos estructurados** (parámetros clave–valor entre corchetes) y un mensaje de texto libre. Los datos estructurados son lo que hace que los registros puedan buscarse: `src="192.0.2.44" user="root"` puede contarse y filtrarse; la misma información enterrada en prosa debe adivinarse con patrones. Los dispositivos antiguos suelen enviar el formato BSD anterior, sin año ni zona horaria; registre esas fuentes como de menor calidad y conviértalas con cuidado.

### 17.4 Normalización

Un **normalizador** convierte el formato de cada fuente en un registro común: hora UTC, equipo, aplicación, gravedad y campos con nombre como `src`, `user`, `dst`, `dport` o `action`. Así, las reglas posteriores (capítulo 19) se escriben una sola vez. Un normalizador debe **contar lo que no puede analizar** e informar de ello: los descartes silenciosos son la forma en que un sistema de monitorización se queda ciego ante la única fuente que cambió de formato. La línea en formato BSD del retransmisor en la noche resuelta muestra por qué: sin un recuento de líneas no analizadas, simplemente habría desaparecido.

La línea del quiosco sin ninguna marca de tiempo es el otro caso: el normalizador debe marcarla, no ponerle la hora de llegada.

### 17.5 Herramientas en las que se puede confiar

Los implementadores escriben herramientas pequeñas constantemente. La confianza en la salida de una herramienta procede de: una declaración clara de lo que trata y lo que no; pruebas con casos erróneos y límite (capítulo 3); recuentos de entradas, salidas y rechazos que cuadren; una salida determinista para la misma entrada; y el control de versiones. Escriba su propia herramienta cuando la tarea sea pequeña y concreta; use una herramienta consolidada y mantenida cuando la tarea sea general (un recopilador syslog completo, una biblioteca TLS, una base de datos). No escriba nunca su propia criptografía: use la de la biblioteca estándar.

### 17.6 Ejemplo resuelto: los registros de una noche (sintético)

El Lab 17 analiza siete líneas del retransmisor, el cortafuegos, el historiador y el quiosco de las cocheras. Seis se analizan y una no: una línea en formato BSD de la propia aplicación del retransmisor, que revela que un componente de LANTERN nunca se configuró con el formato acordado. Una línea no tiene ninguna marca de tiempo (la del quiosco). La línea del historiador lleva `+01:00`; convertida a UTC son las 22:02:11, *antes* de los eventos de SSH, no después, como sugiere su hora local. Ordenada en UTC, la noche se lee así: error de cuota de disco del historiador a las 22:02, un inicio de sesión legítimo de un administrador a las 22:14, dos inicios de sesión fallidos como root desde una dirección externa a las 22:15 y un flujo Modbus de la red corporativa a PS-04 a las 22:16 desde la misma estación de trabajo usada para el inicio de sesión del administrador.

### 17.7 Actividad práctica: normalizador

**Lab 17** (guárdelo como `lab17.py` y ejecútelo con `python3 lab17.py`):

```python
# Lab 17 - normalizing RFC 5424-style syslog lines into JSON records (offline, standard library only)
# Synthetic log lines from the relay, historian and firewall. Simplified parser for teaching, not a full RFC 5424 implementation.
import json, re
from datetime import datetime, timezone
LINE = re.compile(r"<(?P<pri>\d{1,3})>1 (?P<ts>\S+) (?P<host>\S+) (?P<app>\S+) (?P<proc>\S+) (?P<msgid>\S+) (?P<sd>-|\[.*?\]) ?(?P<msg>.*)")
SEV = ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug"]
lines = [
 '<86>1 2026-10-11T22:14:03.120Z rly-01 sshd 812 AUTH [meta src="10.40.3.7" user="b.lind"] Accepted publickey',
 '<84>1 2026-10-11T22:15:40.004Z rly-01 sshd 813 AUTH [meta src="192.0.2.44" user="root"] Failed password',
 '<84>1 2026-10-11T22:15:41.917Z rly-01 sshd 813 AUTH [meta src="192.0.2.44" user="root"] Failed password',
 '<134>1 2026-10-11T22:16:00.000Z fw-hub filter - FLOW [flow src="10.40.3.7" dst="10.20.0.11" dport="502" act="allow"]',
 '<131>1 2026-10-11T23:02:11+01:00 hist-01 histsvc 4410 DBERR - write failed: disk quota',
 'Oct 11 22:17:00 rly-01 relay: legacy BSD-format line',
 '<13>1 - kiosk-depot app - - - no timestamp supplied',
]
SDPARAM = re.compile(r'(\w+)="((?:[^"\\]|\\.)*)"')
out, bad = [], 0
for raw in lines:
    m = LINE.fullmatch(raw)
    if not m:
        bad += 1; print("UNPARSED:", raw[:40]); continue
    pri = int(m["pri"])
    rec = {"ts": None if m["ts"] == "-" else m["ts"], "host": m["host"], "app": m["app"],
           "facility": pri // 8, "severity": SEV[pri % 8], "msgid": m["msgid"], "msg": m["msg"]}
    rec.update(dict(SDPARAM.findall(m["sd"])))
    if rec["ts"]:  # normalize every timestamp to UTC so sources can be ordered together
        rec["ts_utc"] = datetime.fromisoformat(rec["ts"]).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    out.append(rec)
for r in sorted(out, key=lambda r: r.get("ts_utc") or ""):
    print(r.get("ts_utc"), r["host"], r["severity"], r.get("src", "-"), r["msg"] or r["msgid"])
print(json.dumps(out[1], sort_keys=True))
print(f"parsed {len(out)}, unparsed {bad}, missing timestamp {sum(r['ts'] is None for r in out)}")
```

Salida esperada (Python 3.13.5):

```text
UNPARSED: Oct 11 22:17:00 rly-01 relay: legacy BSD
None kiosk-depot notice - no timestamp supplied
2026-10-11T22:02:11.000Z hist-01 err - write failed: disk quota
2026-10-11T22:14:03.120Z rly-01 info 10.40.3.7 Accepted publickey
2026-10-11T22:15:40.004Z rly-01 warning 192.0.2.44 Failed password
2026-10-11T22:15:41.917Z rly-01 warning 192.0.2.44 Failed password
2026-10-11T22:16:00.000Z fw-hub info 10.40.3.7 FLOW
{"app": "sshd", "facility": 10, "host": "rly-01", "msg": "Failed password", "msgid": "AUTH", "severity": "warning", "src": "192.0.2.44", "ts": "2026-10-11T22:15:40.004Z", "ts_utc": "2026-10-11T22:15:40.004Z", "user": "root"}
parsed 6, unparsed 1, missing timestamp 1
```

Compruebe dos cosas en la salida. Primero, el recuento de líneas no analizadas es 1, la línea en formato BSD de la aplicación del retransmisor, que es un fallo de configuración en un componente de LANTERN, no ruido. Segundo, la línea `+01:00` del historiador, convertida a UTC, queda a las 22:02:11, antes del inicio de sesión del administrador de las 22:14 y de los inicios de sesión fallidos como root de las 22:15, y no después. Ordenado así, el flujo Modbus de la red corporativa a PS-04 de las 22:16 sigue a un inicio de sesión de administrador desde la misma estación de trabajo, que es la secuencia que la regla B marcará más adelante.

### 17.8 Errores frecuentes y límites

- Registrarlo todo en el nivel de depuración, lo que llena los discos (capítulo 1) y oculta los eventos que importan.
- Registros guardados solo en el equipo que los produjo.
- Marcas de tiempo sin zona horaria; mezclar la hora local y UTC en un mismo análisis.
- Analizadores que descartan las líneas no analizables sin contarlas.
- Suponer que el reenvío de registros sigue funcionando porque funcionaba el mes pasado.
- Construir una herramienta casera donde existe una mantenida, o criptografía casera en cualquier caso.

El analizador del laboratorio es una simplificación didáctica del RFC 5424: no trata todas las secuencias de escape ni varios elementos de datos estructurados. Informa de lo que no puede analizar, que es la propiedad que más importa.

### Ejercicios — capítulo 17

**EX049 — Corrija el formato del retransmisor.** *Objetivo:* tratar una fuente que no se ajusta al formato. *Entradas:* la línea no analizada del Lab 17. *Restricciones:* dos opciones. *Pasos:* (1) describa la corrección en el origen (cambio de configuración en el retransmisor); (2) describa la adición de un segundo analizador para el formato BSD; (3) indique cuál haría primero y por qué, y qué no puede recuperar el analizador BSD. *Evidencia esperada:* media página. *Rúbrica:* 3 = corregir primero en el origen (es nuestro propio componente, bajo control de cambios) y el analizador BSD como alternativa para dispositivos de terceros; las líneas BSD carecen de año y de zona, así que el analizador debe suponerlos y marcar los registros como de menor calidad; 2 = una opción; 1 = «ignorarla»; 0 = nada.

**EX050 — Orden de los eventos.** *Objetivo:* ver el efecto de las zonas horarias. *Entradas:* la salida del Lab 17. *Restricciones:* ninguna. *Pasos:* (1) enumere los eventos en el orden de sus marcas de tiempo *escritas*, sin tener en cuenta los desfases; (2) enumérelos en orden UTC; (3) explique cómo un investigador que usara el primer orden malinterpretaría el evento del historiador. *Evidencia esperada:* dos listas y una explicación. *Rúbrica:* 3 = el evento del historiador aparece el último en el orden escrito (23:02) pero el primero en UTC (22:02); el investigador podría vincular erróneamente el error de cuota de disco con los inicios de sesión fallidos; 2 = listas correctas, explicación escasa; 1 = una lista; 0 = nada.

**EX051 — Cuente lo que descarta.** *Objetivo:* añadir una autocomprobación a la herramienta. *Entradas:* el Lab 17. *Restricciones:* solo la biblioteca estándar. *Pasos:* (1) añada una comprobación de que el número de líneas de entrada es igual a las analizadas más las no analizadas y termine con un error en caso contrario; (2) añada un recuento por equipo de las líneas no analizadas; (3) explique por qué un sistema de monitorización debería alertar cuando aumenta el recuento de líneas no analizadas de un equipo. *Evidencia esperada:* código, salida y explicación. *Rúbrica:* 3 = invariante aplicada, recuentos por equipo impresos (rly-01: 1), explicación de que un cambio de formato en una fuente deja ciegas las reglas en silencio; 2 = parcial; 1 = no ejecutado; 0 = nada.

### Síntesis del capítulo

Registre lo que necesitará para responder, reenvíelo fuera del equipo y compruebe que el reenvío continúa. Sincronice los relojes, registre la hora con desfases explícitos y analice en UTC. Normalice las fuentes en una estructura única, cuente todo lo que no pueda analizar y construya herramientas pequeñas con pruebas e invariantes para que pueda confiarse en su salida; use herramientas consolidadas para los trabajos generales y no invente nunca criptografía.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Siga estudiando — capítulo 17 de 30

[← Capítulo 16](#ch-16) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Infraestructura crítica y seguridad sectorial: controles

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- seleccionar controles para un escenario asignando la causa y el camino a las funciones de prevenir, detectar y recuperar;
- implementar un control de modo que tenga **responsable, documentación, posibilidad de prueba y monitorización**;
- usar un catálogo de controles como NIST SP 800-53 para comprobar la exhaustividad sin copiarlo entero;
- gestionar el ciclo de vida de una clave como ejemplo de control que es un proceso, no un ajuste.

El capítulo 5 presentó las fichas de control; el capítulo 13 produjo escenarios. Este capítulo los conecta: qué controles necesita LANTERN, cómo implementar cada uno para que siga siendo eficaz y cómo demostrar que lo es.

### 18.1 Del escenario al conjunto de controles

Para cada escenario principal, recorra su camino paso a paso y pregúntese en cada paso: ¿qué podría impedir este paso, qué lo detectaría y qué permitiría recuperarse de él? Para R2 (una credencial de proveedor robada que se usa para cambiar el punto de consigna de dosificación de PS-07, capítulo 13), los pasos son: credencial robada → se usa para iniciar sesión → alcanza el sistema de control → cambia el punto de consigna → cambia la calidad del agua. Los controles se asocian a cada paso: MFA resistente al phishing y habilitación limitada en el tiempo (impedir el uso); registro de sesiones y alertas ante inicios de sesión del proveedor fuera de una ventana aprobada (detectar); límites de los puntos de consigna diseñados en el PLC (impedir el daño); alerta de telemetría de LANTERN cuando el cloro sale de su banda (detectar el efecto); procedimiento de dosificación manual y muestreo de la calidad del agua (recuperar). La defensa en profundidad (capítulo 8) es el resultado de hacer este recorrido con honestidad.

### 18.2 Los catálogos como listas de comprobación de la exhaustividad

Los catálogos de controles (NIST SP 800-53 Rev. 5 es el más completo, [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)) describen los controles por familias: control de acceso, auditoría y rendición de cuentas, gestión de la configuración, planificación de contingencias, respuesta a incidentes, protección de sistemas y comunicaciones, y otras. Use un catálogo después del recorrido del escenario para preguntarse «¿hemos olvidado alguna familia?», no como una lista que haya que implantar entera. En TO, contraste los controles del catálogo con las restricciones operativas descritas en NIST SP 800-82, que ofrece orientación específica para TO y una superposición (*overlay*) para SP 800-53 ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

### 18.3 Cualidades de la implementación

Es habitual un control que existe el primer día y es ineficaz el día noventa. Implemente cada control con cinco cualidades:

1. **Con responsable**: un rol que lo mantiene y responde de él.
2. **Documentado**: una ficha de control (capítulo 5) que diga qué hace, dónde y cómo falla.
3. **Configurado como código** cuando sea posible, para que su estado deseado esté bajo control de versiones y la deriva pueda detectarse (capítulo 22).
4. **Comprobable**: una forma segura de demostrar que funciona, ejecutada de forma programada (capítulo 23).
5. **Monitorizado**: una señal cuando deja de funcionar: un latido, un recuento, una comprobación de salud.

### 18.4 Un control que es un proceso: el ciclo de vida de las claves

Las claves HMAC de LANTERN (capítulo 15) muestran por qué algunos controles son procesos. Cada clave de estación debe **generarse** con una fuente aleatoria criptográficamente segura; **distribuirse** a la pasarela de la estación y al retransmisor por una vía protegida; **almacenarse** donde solo pueda leerla el servicio previsto; **rotarse** de forma programada y cuando se marche personal con acceso; **revocarse** cuando se retire una estación o una clave pueda haber quedado expuesta; y **registrarse**: qué versión de clave está activa y dónde, sin registrar la propia clave. Una clave que nunca se ha rotado es una clave cuya exposición no detectaría. La rotación debe ensayarse: si las estaciones y el retransmisor discrepan sobre la clave activa, todos los mensajes fallan en la comprobación del MAC y la estación queda en silencio.

### 18.5 Evidencia de que un control funciona

La evidencia difiere según el tipo de control. Para un control de **configuración** (SSH vinculado a la interfaz de gestión), la evidencia es el resultado de la comprobación de deriva y un intento de conexión, en una prueba, desde una dirección permitida y otra no permitida. Para un control **detectivo**, la evidencia es un evento de prueba que produjo una alerta en un tiempo medido. Para un control de **proceso** (revisión de accesos, rotación de claves), la evidencia es el registro fechado de la última ejecución y sus hallazgos. Para un control de **recuperación**, la evidencia es una restauración cronometrada. «Configurado» no es evidencia de que funcione.

### 18.6 Ejemplo resuelto: fichas de control para R2 (sintético)

| Control | Función | Responsable | Evidencia de que funciona | Monitorizado mediante |
|---|---|---|---|---|
| Cuenta de proveedor limitada en el tiempo, MFA | Prevenir | FSTS Security | Registro de habilitación; caducidad probada cada mes | Alerta ante inicio de sesión del proveedor fuera de la ventana |
| Registro de las sesiones del proveedor | Detectar | FSTS Security | Muestra de sesiones revisada cada semana | Alerta si se detiene el servicio de grabación |
| Límites del punto de consigna de dosificación en el PLC | Impedir el daño | Ingeniería de Agua | Registro de la prueba de ingeniería; valor releído en la visita a la instalación | Comparación con la línea base aprobada de puntos de consigna |
| Alerta de telemetría de cloro fuera de banda | Detectar el efecto | Monitorización de FSTS | Una lectura de prueba inyectada generó la alerta en 2 min | Latido de la regla (capítulo 19) |
| Procedimiento de dosificación manual y muestreo | Recuperar | Operaciones de Agua | Registro de un ejercicio en los últimos 12 meses | Calendario de ejercicios |

### 18.7 Actividad práctica: manual de operación para la rotación de claves

Redacte un manual de operación para la rotación de la clave de una estación: preparación (nueva clave generada y almacenada, retransmisor configurado para aceptar la antigua *y* la nueva durante un breve solapamiento), conmutación en la pasarela de la estación, verificación (mensajes aceptados con la nueva versión de clave; fallos de MAC contados), eliminación de la clave antigua y reversión. Indique la duración del solapamiento y por qué. Para PS-07, cuya clave de pasarela estaba en una tarjeta extraíble dentro de un armario sin cerrar, la rotación ya no es un mantenimiento rutinario: es la respuesta a un hallazgo físico. Un solapamiento de unas pocas horas, suficiente para confirmar mensajes aceptados con la nueva versión de clave, mantiene a la estación informando durante la conmutación.

### 18.8 Errores frecuentes y límites

- Seleccionar controles de un catálogo sin recorrer un escenario, lo que produce muchos controles y huecos entre ellos.
- Controles sin responsable, o cuyo responsable es una persona y no un rol.
- Tratar «configurado» como «eficaz».
- Rotación de claves nunca ensayada, por lo que se evita.
- Retirar un control compensatorio cuando la corrección está programada en lugar de verificada.

Las fichas de R2 evitan estos errores: cada control tiene un rol responsable y evidencia, y la prueba de la alerta de cloro generó una alerta en 2 minutos.

La rotación de claves de PS-07 se evitó durante años por el cuarto motivo.

### Ejercicios — capítulo 18

**EX052 — Recorra un escenario.** *Objetivo:* construir un conjunto de controles a partir de un camino. *Entradas:* R3 del capítulo 13 (el disco del retransmisor se llena; se pierde telemetría). *Restricciones:* al menos un control por paso y por función. *Pasos:* (1) escriba el camino en pasos; (2) asocie controles de prevención, detección y recuperación; (3) nombre la evidencia de cada uno. *Evidencia esperada:* tabla. *Rúbrica:* 3 = pasos como crecimiento → umbral → fallo de escritura → mensajes perdidos, con controles como la aplicación de la conservación, la previsión de capacidad y una alarma con plazo de antelación (capítulo 1), la alarma de disco y la alerta por recuento de rechazos o pérdidas, el almacenamiento en las estaciones y la subida de la acumulación; evidencia especificada; 2 = falta una función; 1 = un solo control; 0 = nada.

**EX053 — Comprobación con el catálogo.** *Objetivo:* usar un catálogo para comprobar la exhaustividad. *Entradas:* las fichas de control de R2 del capítulo 18 («Ejemplo resuelto: fichas de control para R2») y la lista de familias de controles de SP 800-53 Rev. 5. *Restricciones:* cite las familias por su identificador. *Pasos:* (1) asigne cada ficha a una familia; (2) nombre una familia relevante para R2 que no tenga ficha; (3) proponga una ficha para ella. *Evidencia esperada:* tabla con cita. *Rúbrica:* 3 = asignaciones razonables (por ejemplo, AC, AU, CM/SI, IR o CP) y una familia ausente creíble, como la seguridad del personal para el personal del proveedor, la gestión de riesgos de la cadena de suministro (SR) para la propia seguridad del proveedor o la respuesta a incidentes (IR) para un incidente de dosificación, con una ficha concreta; 2 = asignación correcta, familia ausente débil; 1 = sin cita; 0 = nada.

**EX054 — Duración del solapamiento.** *Objetivo:* razonar sobre la rotación de claves. *Entradas:* las estaciones almacenan hasta 24 horas; los mensajes acumulados se sellan con la clave activa en el momento en que se crearon. *Restricciones:* el retransmisor debería aceptar el menor número de claves posible durante el menor tiempo posible. *Pasos:* (1) indique durante cuánto tiempo debe seguir aceptando el retransmisor la clave antigua después de la conmutación; (2) explique cómo sabe el retransmisor qué clave probar. *Evidencia esperada:* párrafo. *Rúbrica:* 3 = clave antigua aceptada al menos durante el periodo de almacenamiento de 24 h (más un margen) porque los mensajes acumulados llevan MAC con la clave antigua; los mensajes llevan un identificador de versión de clave dentro del cuerpo autenticado o junto a él para que el retransmisor seleccione la clave en lugar de probarlas todas; después se elimina la clave antigua y se verifica la eliminación; 2 = solapamiento correcto, selección vaga; 1 = sin solapamiento; 0 = nada.

### Síntesis del capítulo

Seleccione los controles recorriendo el camino de cada escenario y asociando a sus pasos controles de prevención, detección y recuperación; use los catálogos para comprobar la exhaustividad. Implemente cada control con responsable, documentado, configurado como código cuando sea posible, comprobable y monitorizado. Algunos controles son procesos (el ciclo de vida de las claves es el ejemplo más claro) y deben ensayarse. «Configurado» nunca es lo mismo que «funciona».

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Siga estudiando — capítulo 18 de 30

[← Capítulo 17](#ch-17) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Infraestructura crítica y seguridad sectorial: monitorización

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- redactar reglas de detección a partir de escenarios y de la arquitectura declarada;
- detectar la **ausencia** (latidos que faltan, fuentes en silencio) además de la presencia;
- ajustar las reglas para que alerten una vez por **episodio** en lugar de una vez por evento, sin perder información;
- monitorizar la monitorización: saber cuándo una regla, una fuente o un reenviador ha dejado de funcionar.

El capítulo 17 produjo registros normalizados. Este capítulo los convierte en alertas sobre las que pueda actuar una persona de guardia. El objetivo no son muchas alertas, sino las pocas adecuadas, cada una de las cuales apunta a un escenario y a una primera acción.

### 19.1 De dónde salen las reglas

Tres fuentes producen las reglas de LANTERN. Los **escenarios** (capítulo 13): cada paso de un camino que deja rastro es una regla candidata, como un inicio de sesión del proveedor fuera de una ventana aprobada o el cloro fuera de su banda. La **arquitectura** (capítulos 2 y 8): cualquier flujo que incumpla un conducto declarado (de la red corporativa a una estación por un puerto industrial) es una regla que no necesita inteligencia de amenazas, porque la define su propio diseño. Los **comportamientos conocidos**: conviene saber de los inicios de sesión fallidos repetidos desde un mismo origen. La matriz ATT&CK for ICS de MITRE cataloga los comportamientos de adversarios observados contra sistemas industriales y ayuda a comprobar si las reglas cubren las técnicas más relevantes para sus escenarios ([MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)).

### 19.2 La ausencia es una señal

En los servicios críticos, muchas de las alertas más importantes tratan de cosas que *dejan* de ocurrir: una estación que deja de informar, un retransmisor que deja de reenviar, una fuente de registros que queda en silencio, una copia de seguridad que no se ejecuta. Las reglas de ausencia necesitan un **ritmo esperado** (un latido cada cinco minutos) y una **tolerancia** (alertar tras 15 minutos de silencio). Detectan interrupciones, dispositivos averiados, cables cortados, errores de configuración y atacantes que deshabilitan el registro. La regla C marcó a las 23:00 el silencio de 40 minutos de PS-09, 15 minutos después de su último latido; esa tolerancia de 15 minutos es la decisión de diseño.

### 19.3 Eventos, episodios y calidad de las alertas

Una regla que salta con cada evento coincidente inunda al tecnólogo de guardia: 14 inicios de sesión fallidos se convierten en 14 alertas. Las reglas mejores alertan una vez por **episodio** (el primer evento de una ventana, con un recuento del resto) y adjuntan contexto: zona de origen, criticidad del activo y eventos recientes relacionados. Haga un seguimiento de la **tasa de falsas alarmas** y del **tiempo de respuesta** de cada regla. Una regla que ha saltado cien veces sin ningún verdadero positivo está enseñando a la gente a ignorarla; ajústela, cambie su umbral o envíela a un informe diario en lugar de a un aviso al busca.

### 19.4 Encaminamiento y primera acción

Toda alerta necesita un responsable y una **primera acción** escrita en la regla: «Modbus de la red corporativa a una estación: comprobar si hay en curso una sesión de ingeniería aprobada (calendario de cambios); si no, llamar a la sala de control de Agua y, después, conservar los registros de flujos». Las alertas que afectan al proceso físico van a operaciones de Agua además de a FSTS. Redacte las primeras acciones antes de activar una regla. La primera acción de la regla B cumplió su función en la noche resuelta: primero el calendario de cambios y después la sala de control de Agua.

La primera acción de la regla C, tras el estudio del capítulo 24, es «llamar a la sala de control de Agua y, después, comprobar el estado del operador».

### 19.5 Monitorizar la monitorización

Las reglas, las fuentes y los reenviadores fallan en silencio. Monitorice: la tasa de eventos de cada fuente (una regla de ausencia para los registros); el recuento de líneas no analizadas del normalizador (capítulo 17); la hora de la última evaluación de cada regla; y **eventos de prueba** periódicos que deberían producir alertas conocidas (capítulo 23). La guía del NIST sobre la monitorización continua de la seguridad de la información insiste en saber de forma permanente si los controles siguen siendo eficaces ([NIST SP 800-137](https://csrc.nist.gov/pubs/sp/800/137/final)).

Los fallos de la regla B en el Lab 23, flujos de un conmutador de estación que nunca se exportaban al SIEM, muestran el coste de no monitorizar las fuentes: la regla era correcta, faltaba su entrada.

### 19.6 Ejemplo resuelto: una noche, tres reglas (sintético)

El Lab 19 aplica tres reglas a una noche de eventos y latidos. La regla A (≥10 inicios de sesión fallidos desde un origen en 5 minutos) salta una vez para 192.0.2.44. La regla B (Modbus de la red corporativa a una estación) salta dos veces para la misma estación de trabajo, a las 22:16 y a las 22:31: dos avisos para un episodio; debería ajustarse para alertar una vez y actualizar un recuento. La regla C (latido ausente durante > 15 minutos) salta a las 23:00 para PS-09, que estuvo en silencio 40 minutos. Observe lo que **no** salta: un único inicio de sesión fallido de `e.strand` desde una dirección interna, por debajo del umbral de la regla A; con razón, ya que una contraseña mal tecleada no es un episodio.

Junto con la cronología del capítulo 17, la regla B es la alerta que más importa: la estación de trabajo que inició sesión como administrador a las 22:14 habló después Modbus con un PLC. Primera acción: comprobar el calendario de cambios; si no se aprobó ninguna sesión de ingeniería, llamar a la sala de control de Agua.

### 19.7 Actividad práctica: reglas sobre eventos

**Lab 19** (guárdelo como `lab19.py` y ejecútelo con `python3 lab19.py`):

```python
# Lab 19 - three monitoring rules over normalized events, including "absence" (offline, standard library only)
# Synthetic events for one night at Fallowmere (times are minutes after 22:00 UTC).
events = [  # minute, host, type, fields
 (14, "rly-01", "auth_ok", {"src": "10.40.3.7", "user": "b.lind"}),
 *[(15 + i // 4, "rly-01", "auth_fail", {"src": "192.0.2.44", "user": "root"}) for i in range(14)],
 (16, "fw-hub", "flow", {"src": "10.40.3.7", "dst": "10.20.0.11", "dport": 502}),
 (31, "fw-hub", "flow", {"src": "10.40.3.7", "dst": "10.20.0.11", "dport": 502}),
 (44, "rly-01", "auth_fail", {"src": "10.40.9.9", "user": "e.strand"}),
]
heartbeats = {"PS-04": list(range(0, 120, 5)), "PS-07": list(range(0, 120, 5)),
              "PS-09": [m for m in range(0, 120, 5) if not 50 <= m < 85]}
alerts = []
# Rule A: >=10 failed logins from one source within 5 minutes
fails = [(m, f["src"]) for m, h, t, f in events if t == "auth_fail"]
for src in {s for _, s in fails}:
    times = sorted(m for m, s in fails if s == src)
    for i in range(len(times)):
        if sum(1 for t in times if times[i] <= t < times[i] + 5) >= 10:
            alerts.append((times[i], "A brute-force", src)); break
# Rule B: any flow from corp to a station on an industrial port (not a declared conduit)
for m, h, t, f in events:
    if t == "flow" and f["src"].startswith("10.40.") and f["dst"].startswith("10.20.") and f["dport"] == 502:
        alerts.append((m, "B corp->station Modbus", f"{f['src']}->{f['dst']}"))
# Rule C: heartbeat missing for > 15 minutes (silence is a signal)
for st, beats in heartbeats.items():
    for a, b in zip(beats, beats[1:]):
        if b - a > 15:
            alerts.append((a + 15, "C station silent", f"{st} gap {b - a} min"))
for m, rule, detail in sorted(alerts):
    print(f"22:{m:02d}+  {rule:<24} {detail}" if m < 60 else f"23:{m-60:02d}+  {rule:<24} {detail}")
print("alerts:", len(alerts), "| rule B fired per event, not per episode:", sum(1 for a in alerts if a[1].startswith("B")))
```

Salida esperada (Python 3.13.5):

```text
22:15+  A brute-force            192.0.2.44
22:16+  B corp->station Modbus   10.40.3.7->10.20.0.11
22:31+  B corp->station Modbus   10.40.3.7->10.20.0.11
23:00+  C station silent         PS-09 gap 40 min
alerts: 4 | rule B fired per event, not per episode: 2
```

Cuente las alertas por episodio, no por línea: las cuatro alertas de la salida son tres episodios, y ajustar la regla B para que alerte una vez y actualice un recuento las deja en tres.

### 19.8 Errores frecuentes y límites

- Reglas sin escenario, responsable ni primera acción.
- Solo reglas de presencia; nada advierte el silencio.
- Una alerta por evento, que inunda a quienes responden.
- Umbrales que nunca se revisan.
- Suponer que una regla funciona porque se desplegó; debe probarse (capítulo 23).
- Enviar las alertas relevantes para el proceso solo a TI.

Las reglas detectan lo que se previó. El comportamiento imprevisto necesita personas que miren los datos (búsqueda proactiva de amenazas, revisiones) y reglas de ausencia, que detectan los efectos sin conocer las causas.

Los dos avisos de la regla B para un solo episodio en la noche resuelta son el tercer error.

### Ejercicios — capítulo 19

**EX055 — Regla por episodios.** *Objetivo:* reducir el ruido de las alertas sin perder información. *Entradas:* el Lab 19. *Restricciones:* solo la biblioteca estándar. *Pasos:* (1) cambie la regla B para que genere una alerta por par origen–destino cada 60 minutos, registrando el recuento de eventos coincidentes; (2) ejecútela y muestre la salida; (3) explique qué información se conserva. *Evidencia esperada:* código, salida y explicación. *Rúbrica:* 3 = una alerta de la regla B con recuento 2 y horas primera y última; explicación de que los recuentos y las horas se conservan para la investigación mientras el aviso salta una sola vez; 2 = funciona, falta el recuento; 1 = no ejecutado; 0 = nada.

**EX056 — Primeras acciones.** *Objetivo:* redactar alertas accionables. *Entradas:* las reglas A, B y C. *Restricciones:* como máximo tres pasos cada una; deben incluir a quién llamar. *Pasos:* redacte la primera acción de cada una. *Evidencia esperada:* tres procedimientos breves. *Rúbrica:* 3 = A: confirmar la exposición de SSH, comprobar si hubo algún éxito desde ese origen, bloquear en el perímetro mediante un cambio estándar; B: comprobar el calendario de cambios, llamar a la sala de control de Agua si no está aprobado, conservar los flujos; C: llamar a la sala de control de Agua para confirmar el estado de la estación, comprobar el estado del operador, revisar los registros del retransmisor en busca de fallos de MAC; 2 = una débil; 1 = genéricas; 0 = nada.

**EX057 — Monitorice el monitor.** *Objetivo:* diseñar la automonitorización. *Entradas:* la cadena de monitorización de LANTERN: fuentes → reenviador → normalizador → reglas → avisos. *Restricciones:* una comprobación por etapa. *Pasos:* enumere la comprobación, su umbral y a quién se alerta. *Evidencia esperada:* tabla. *Rúbrica:* 3 = ausencia en la tasa de eventos de las fuentes, cola o acumulación del reenviador, tasa de líneas no analizadas del normalizador, hora de la última ejecución de las reglas, prueba de avisos (aviso sintético programado y confirmado); umbrales y destinatarios razonables; 2 = cuatro etapas; 1 = genérica; 0 = nada.

### Síntesis del capítulo

Derive las reglas de los escenarios, de su propia arquitectura y de los comportamientos conocidos; asigne a cada una un responsable y una primera acción. Detecte la ausencia además de la presencia. Alerte por episodio con recuentos y contexto, haga un seguimiento de las falsas alarmas y de los tiempos de respuesta, y envíe a operaciones las alertas relevantes para el proceso. Monitorice la monitorización, porque cada una de sus etapas puede fallar en silencio.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Siga estudiando — capítulo 19 de 30

[← Capítulo 18](#ch-18) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Infraestructura crítica y seguridad sectorial: resolución de problemas

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- seguir un método disciplinado de resolución de problemas que funcione tanto si una avería resulta ser técnica como humana o maliciosa;
- **conservar la evidencia antes de cambiar nada**, y saber cuándo una avería debe convertirse en un incidente;
- distinguir las causas habituales de los «datos que faltan» (pérdida, retraso, error de reloj, filtrado) usando los propios datos;
- redactar un breve registro del problema que la siguiente persona pueda usar.

La mayor parte de la vida laboral de un implementador se dedica a las averías. En los servicios críticos, algunas averías son ataques y algunos ataques parecen averías; el método debe funcionar para ambos sin frenar las reparaciones ordinarias.

### 20.1 Un método

1. **Defina el síntoma con precisión**: qué falla, desde cuándo, para quién y medido cómo. «PS-07 y PS-09 muestran huecos en el panel desde aproximadamente las 22:50», no «la telemetría no funciona».
2. **Compruebe primero el impacto y la seguridad física**: ¿alguien tiene que actuar ahora sobre el proceso físico? Diga a operaciones de Agua en qué pueden confiar y en qué no.
3. **Conserve antes de cambiar**: copie los registros, configuraciones y salidas pertinentes, con sus horas, antes de reiniciar o reconfigurar nada (véase «Conserve antes de cambiar», más abajo).
4. **Enumere hipótesis**, incluida al menos una explicación no maliciosa y otra maliciosa, y qué evidencia las distinguiría.
5. **Pruebe primero la hipótesis discriminante más barata**, con lecturas antes que escrituras.
6. **Cambie una sola cosa cada vez**, con el tipo de cambio adecuado (capítulo 14), registrando cada cambio.
7. **Verifique** la corrección frente al síntoma original y vigile si se repite.
8. **Registre** la causa, la evidencia, las acciones y los elementos abiertos.

### 20.2 Conserve antes de cambiar

Reiniciar un servicio borra su memoria, rota los registros y puede destruir la única evidencia de lo ocurrido. Las recomendaciones del NIST sobre respuesta a incidentes insisten en conservar la evidencia y en coordinar la respuesta con la gestión de riesgos de la organización ([NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). Para un implementador, conservar suele ser rápido: copie los registros y la configuración del servicio, exporte los registros de flujos y de alertas pertinentes, anote los procesos en ejecución y las conexiones de red, calcule los hashes de lo copiado y anote la hora. Si la avería afecta al proceso físico, restablecer el servicio puede ir legítimamente primero, pero dígalo y registre lo que se perdió.

### 20.3 Cuándo una avería se convierte en incidente

Escale al proceso de incidentes cuando se cumpla cualquiera de estas condiciones: hay evidencia de un acceso o un cambio no autorizados (una diferencia de configuración no aprobada, el uso de la cuenta de alguien que se ha marchado, capítulo 7); un control de seguridad ha fallado de una forma que podría explotarse; los datos pueden haber ido adonde no deberían (capítulo 12); o no se encuentra la causa y una causa maliciosa es plausible. Escalar no es una acusación. Incorpora a personas con otra autoridad y otras obligaciones, incluidas las obligaciones de notificación del operador (capítulo 10).

El inicio de sesión de `c.mendes` el 14 de septiembre es el desencadenante más claro de Fallowmere.

### 20.4 Datos que faltan: cuatro causas habituales

La telemetría que falta es el síntoma más común de LANTERN. Los propios datos suelen discriminar entre las causas:

- **Pérdida**: los números de secuencia tienen huecos (capítulo 15); los mensajes nunca se recibieron.
- **Retraso**: la secuencia está completa, pero la hora de recepción va muy por detrás de la hora de la estación, a menudo tras un problema del operador.
- **Error de reloj**: la secuencia está completa y la llegada es puntual, pero las marcas de tiempo de la estación están desplazadas una cantidad constante; los datos se archivan en la ventana temporal equivocada, así que un panel que consulta por la hora de la estación muestra un hueco.
- **Filtrado**: los mensajes se reciben, pero se rechazan o se ponen en cuarentena (recuentos de rechazos crecientes en el registro del retransmisor).

### 20.5 Ejemplo resuelto: dos huecos, dos causas (sintético)

Los operadores informan de huecos en el panel para PS-07 y PS-09. El Lab 20 examina doce números de secuencia de cada estación. A PS-07 le faltan los números de secuencia 5–8, con llegada puntual del resto: los datos se perdieron. PS-09 tiene todos los números de secuencia y llega puntualmente según el reloj del retransmisor, pero las marcas de tiempo de la estación van unos 422 segundos por detrás: su reloj está mal, y la ventana del panel no recoge ninguno de sus puntos. Los dos síntomas parecían idénticos en el panel; las causas y las correcciones son completamente distintas.

Para PS-09, la siguiente pregunta es *por qué* está mal el reloj: ¿ha perdido la estación su ruta NTP hacia el retransmisor (¿un cambio en el conducto?, capítulo 2), o alguien ha cambiado la configuración horaria de la estación? Lo primero es una avería; lo segundo puede ser un evento de seguridad. Un desfase constante de unos siete minutos en todos los mensajes es inusual para una deriva, que es gradual. Conserve los registros NTP del retransmisor y la configuración del conducto antes de que nadie reajuste el reloj.

Para PS-07, el hueco de cuatro mensajes consecutivos podría deberse a una caída del operador, a un reinicio de la estación o a rechazos del retransmisor. Revise el registro de rechazos del retransmisor para esas horas antes de llamar a BayTel: si en ese momento hubo fallos de MAC en PS-07, la causa está en la gestión de claves (capítulo 18), no en el operador.

### 20.6 Actividad práctica: discrimine las causas

**Lab 20** (guárdelo como `lab20.py` y ejecútelo con `python3 lab20.py`):

```python
# Lab 20 - troubleshooting "missing telemetry": sequence gaps versus clock skew (offline, standard library only)
# Synthetic historian extract: station, sequence number, station timestamp (s), relay receive time (s).
rows = {
 "PS-04": [(s, 1000 + 10*s, 1000 + 10*s + 1) for s in range(1, 13)],
 "PS-07": [(s, 1000 + 10*s, 1000 + 10*s + 1) for s in range(1, 13) if s not in (5, 6, 7, 8)],
 "PS-09": [(s, 1000 + 10*s - 420, 1000 + 10*s + 2) for s in range(1, 13)],
}
for st, rs in rows.items():
    seqs = [r[0] for r in rs]
    missing = sorted(set(range(seqs[0], seqs[-1] + 1)) - set(seqs))
    offsets = [recv - ts for _, ts, recv in rs]
    avg = sum(offsets) / len(offsets)
    dx = "data lost in transit or at source" if missing else ("clock skew: station clock behind by ~%d s; data present but filed in the wrong window" % round(avg) if abs(avg) > 60 else "healthy")
    print(f"{st}: received {len(rs)}/{seqs[-1]-seqs[0]+1}, missing seq {missing or '-'}, mean recv-ts offset {avg:+.0f} s -> {dx}")
# A dashboard that queries by station timestamp for window [1050, 1130) would show:
for st, rs in rows.items():
    print(st, "points in dashboard window:", sum(1 for _, ts, _ in rs if 1050 <= ts < 1130))
```

Salida esperada (Python 3.13.5):

```text
PS-04: received 12/12, missing seq -, mean recv-ts offset +1 s -> healthy
PS-07: received 8/12, missing seq [5, 6, 7, 8], mean recv-ts offset +1 s -> data lost in transit or at source
PS-09: received 12/12, missing seq -, mean recv-ts offset +422 s -> clock skew: station clock behind by ~422 s; data present but filed in the wrong window
PS-04 points in dashboard window: 8
PS-07 points in dashboard window: 4
PS-09 points in dashboard window: 0
```

Mire las columnas de las dos estaciones una junto a otra. Los números de secuencia de PS-07 saltan de 4 a 9, así que cuatro mensajes nunca llegaron. Los números de secuencia de PS-09 están completos, pero sus marcas de tiempo de estación van unos 422 segundos por detrás de las horas de llegada al retransmisor en todos los mensajes. Lo primero es pérdida; lo segundo, hora. Después redacte la siguiente comprobación para cada una: el registro de rechazos del retransmisor y el estado de BayTel para el hueco de PS-07, y la ruta NTP y la configuración horaria de PS-09, conservadas antes de que nadie reajuste el reloj.

### 20.7 Errores frecuentes y límites

- Reiniciar primero e investigar después.
- Una sola hipótesis, normalmente la más conocida.
- Varios cambios a la vez, de modo que nadie sabe cuál lo arregló, o cuál estropeó otra cosa.
- Tratar todas las averías como ataques, o ninguna.
- «Arreglar» un reloj o una configuración antes de registrar cómo estaba.
- Cerrar la incidencia sin un registro de la causa y la evidencia.

Reajustar primero el reloj de PS-09 habría destruido la evidencia para la pregunta de los 422 segundos.

Llamar a BayTel por el hueco de PS-07 antes de revisar el registro de rechazos del retransmisor sería el segundo error: una sola hipótesis, la más conocida, probada en primer lugar y quizá en exclusiva.

### Ejercicios — capítulo 20

**EX058 — Hipótesis y discriminantes.** *Objetivo:* razonar antes de actuar. *Entradas:* síntoma: «el recuento de rechazos del retransmisor para PS-04 subió de 0 a 300 por hora a las 09:00; desde entonces el panel no muestra datos de PS-04». *Restricciones:* cuatro hipótesis, al menos una maliciosa. *Pasos:* para cada una, indique la evidencia que la apoyaría o la descartaría y la comprobación más barata. *Evidencia esperada:* tabla. *Rúbrica:* 3 = por ejemplo, clave rotada en la estación pero no en el retransmisor (fallos de MAC en los motivos de rechazo, calendario de cambios), salto del reloj de la estación (rechazos por ventana), estado de reproducción envenenado (rechazos por reproducción tras una secuencia alta, capítulo 29), tráfico falsificado (fallos de MAC desde una dirección de origen inesperada); las comprobaciones son lecturas; 2 = tres; 1 = una; 0 = nada.

**EX059 — Lista de conservación.** *Objetivo:* conservar la evidencia con rapidez. *Entradas:* el caso del desfase del reloj de PS-09. *Restricciones:* diez minutos como máximo; ningún cambio en los sistemas. *Pasos:* enumere lo que copiaría o registraría, en orden, y cómo demostraría después que las copias no se alteraron. *Evidencia esperada:* lista. *Rúbrica:* 3 = registros NTP y del retransmisor, configuración del conducto o del cortafuegos y registro de cambios reciente, extracto del historiador, salida de un análisis al estilo del Lab 20, hora de la recogida, hashes anotados en la incidencia y copias guardadas fuera del equipo; 2 = faltan los hashes o las horas; 1 = «hacer una captura de pantalla»; 0 = nada.

**EX060 — Registro del problema.** *Objetivo:* redactar un registro útil. *Entradas:* el capítulo 20 («Ejemplo resuelto: dos huecos, dos causas») y suponga que la causa de PS-09 fue un cambio en el cortafuegos que bloqueó udp/123 del retransmisor a la estación dos días antes. *Restricciones:* como máximo 250 palabras; etiquetas observado / inferido / hecho / abierto. *Pasos:* redacte el registro. *Evidencia esperada:* el registro. *Rúbrica:* 3 = síntoma preciso, evidencia (desfase de ~422 s, secuencia completa), causa con el cambio identificado, corrección con control de cambios, verificación y elementos abiertos (por qué el cambio eliminó NTP; por qué no saltó ninguna alerta por el desfase del reloj: añadir una); 2 = falta un elemento; 1 = solo narración; 0 = nada.

### Síntesis del capítulo

Resuelva los problemas con un método: síntoma preciso, seguridad física e impacto primero, conservar antes de cambiar, varias hipótesis incluida una maliciosa, la comprobación discriminante más barata primero, un cambio cada vez, verificar y registrar. Escale a incidente cuando la evidencia sugiera actividad no autorizada o exposición. Para los datos que faltan, los propios datos (secuencia, llegada, marcas de tiempo, recuentos de rechazos) suelen distinguir la pérdida, el retraso, el error de reloj y el filtrado.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Siga estudiando — capítulo 20 de 30

[← Capítulo 19](#ch-19) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Capítulo 21 — Infraestructura crítica y seguridad sectorial: integración del servicio

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

- integrar un servicio técnico con las personas y organizaciones que lo rodean: operadores, el centro de monitorización de seguridad, proveedores y planificadores de emergencias;
- definir **interfaces** (qué se entrega, en qué forma, con qué rapidez y a quién), no solo formatos de datos;
- redactar una matriz de responsabilidades para un servicio compartido y probarla con un escenario;
- conectar la gestión de incidentes del servicio con los planes de continuidad y de emergencia del operador.

A estas alturas, LANTERN es un servicio técnico que funciona. Un servicio está integrado cuando todos los que dependen de él, o de quienes él depende, saben qué esperar y qué hacer. La mayoría de los fallos en esta etapa no son técnicos: una alerta sin responsable, un proveedor al que nunca se avisó de un cambio, un operador que no sabía que el panel podía mostrar datos desactualizados.

### 21.1 Las interfaces son acuerdos

Para cada vecino, ponga por escrito la interfaz como un acuerdo:

- **Operaciones de Agua**: lo que proporciona LANTERN (telemetría al historiador en 60 s, mostrando la antigüedad del valor), lo que proporciona Agua (solicitudes de puesta en servicio de estaciones, exportaciones de ingeniería, aprobaciones relevantes para el proceso), cómo llegan a la sala de control las alertas que afectan al proceso y cómo notifica Agua un problema sospechado de telemetría.
- **Monitorización de seguridad de FSTS (SOC)**: qué registros y alertas envía LANTERN, en qué formato y con qué primeras acciones; cómo escala el SOC a la guardia de LANTERN; qué puede hacer el SOC sin preguntar (por ejemplo, deshabilitar una cuenta de proveedor) y qué no debe hacer (por ejemplo, bloquear los conductos de las estaciones).
- **Proveedores (Kell, Arlen, BayTel, Halden)**: cómo se les avisa de los cambios que les afectan, cómo notifican problemas y vulnerabilidades, cómo funciona su acceso (capítulo 7) y con qué antelación avisan de sus propios cambios.
- **Planificación de emergencias**: cómo se reflejan una interrupción o un compromiso de LANTERN en los planes de continuidad de Agua y del hospital.

### 21.2 Matrices de responsabilidades

Una matriz **RACI** registra para cada actividad quién es responsable de ejecutarla (R, *Responsible*: la hace), quién rinde cuentas (A, *Accountable*: es dueño del resultado; exactamente uno), a quién se consulta (C, *Consulted*) y a quién se informa (I, *Informed*). Pruébela con un escenario: recorra «retransmisor comprometido a las 02:00» y compruebe que cada paso tiene exactamente un rol que rinde cuentas, que no hace falta consultar a nadie que no pueda localizarse a las 02:00 y que las personas que deben actuar sobre el proceso físico reciben la información pronto.

Recorrer «retransmisor comprometido a las 02:00» sobre el borrador de Fallowmere puso de manifiesto el problema que describe el ejemplo resuelto: nadie rendía cuentas de decir a los operadores de Agua que desconfiaran de la telemetría.

### 21.3 Integración de los proveedores

Los proveedores forman parte del servicio. Su acceso remoto es un camino hacia él; sus actualizaciones de software son cambios en él; sus interrupciones son sus interrupciones. Integrarlos significa: su acceso por el camino declarado; sus avisos de cambio en su calendario de cambios; sus avisos de seguridad en su rutina de vulnerabilidades (capítulo 16); y cláusulas contractuales que exijan la notificación de los incidentes que le afecten. La iniciativa Secure by Design de la CISA anima a los fabricantes a asumir la responsabilidad de los resultados de seguridad de sus clientes ([CISA Secure by Design](https://www.cisa.gov/securebydesign)); como cliente, pregunte a los proveedores cómo cumplen esas expectativas y registre las respuestas.

### 21.4 La gestión de incidentes se encuentra con la continuidad

Un incidente en LANTERN lo gestiona el proceso de incidentes de FSTS, pero sus consecuencias las gestionan los mecanismos de continuidad y de emergencia de Agua y del hospital. El punto de integración es una lista breve de **desencadenantes**: condiciones en las que FSTS dice a Agua «suponga que la telemetría no es fiable: pase a lecturas manuales en las estaciones» o dice al hospital «suponga que la pasarela clínica no está disponible: use el procedimiento en papel de la biblioteca de fármacos». Los desencadenantes deben acordarse y ejercitarse de antemano (capítulo 28), porque a las 02:00 nadie debería estar negociando qué significa «no fiable».

### 21.5 Ejemplo resuelto: una RACI que no superó su prueba (sintético)

El borrador de la RACI para «sospecha de compromiso de un retransmisor» indica: guardia de FSTS, R; responsable de seguridad de FSTS, A; operaciones de Agua, I; SOC, C; Kell, I. Recorrer el escenario revela tres problemas. Primero, la decisión de decir a los operadores de Agua que desconfíen de la telemetría no tiene ningún rol que rinda cuentas: FSTS Security no puede juzgar el impacto en el proceso, y Agua solo está informada. Corrección: el jefe de turno de Agua rinde cuentas de la respuesta operativa y el responsable de seguridad de FSTS de la respuesta técnica, con un desencadenante designado para el traspaso. Segundo, Kell solo está informada, pero si el compromiso llegó por el camino del proveedor, la cuenta de Kell debe deshabilitarse de inmediato y hay que consultar a Kell sobre su propia exposición. Tercero, el SOC figura como «consultado», pero en la práctica detecta la mayoría de los incidentes; debería ser responsable de los primeros pasos del triaje.

### 21.6 Actividad práctica: acuerdos de interfaz

Redacte un acuerdo de interfaz de una página entre LANTERN y operaciones de Agua que cubra: lo que proporciona cada parte, los niveles de servicio (puntualidad, visualización de la antigüedad del valor), el encaminamiento de las alertas, cómo se notifica un problema sospechado de telemetría, los desencadenantes de «telemetría no fiable» y la frecuencia de revisión. Haga que los desencadenantes sean medibles: por ejemplo, se declara «telemetría no fiable» cuando los fallos de MAC del retransmisor superan una tasa fijada en más de una estación, cuando dos o más estaciones muestran desfases de reloj como los 422 segundos de PS-09, o cuando FSTS sospecha el compromiso de un retransmisor. Indique quién lo declara (el jefe de turno de Agua, con el asesoramiento de FSTS), cómo se informa a la sala de control y que se ejercita cada año.

### 21.7 Errores frecuentes y límites

- Tratar la integración solo como formatos de datos e interfaces de programación (API).
- Matrices RACI con varios roles que rinden cuentas, o con ninguno.
- Proveedores fuera de los procesos de cambios y de vulnerabilidades.
- Planes de continuidad que suponen que el servicio de TI está o totalmente activo o totalmente caído, sin un estado «activo pero no fiable».
- Desencadenantes definidos pero nunca ejercitados.

El primer borrador de la RACI muestra el segundo error: ningún rol rendía cuentas de la respuesta operativa.

La exclusión de Kell de los roles consultados en el borrador de la RACI muestra el tercero: a un proveedor cuya cuenta puede ser la vía de entrada solo se le iba a informar.

### Ejercicios — capítulo 21

**EX061 — Repare la RACI.** *Objetivo:* corregir una matriz de responsabilidades. *Entradas:* el borrador del capítulo 21 («Ejemplo resuelto: una RACI que no superó su prueba»). *Restricciones:* exactamente una A por actividad; divida actividades si es necesario. *Pasos:* redacte la matriz reparada para las actividades: detectar y hacer el triaje; contener en el retransmisor; deshabilitar el acceso del proveedor; decidir la respuesta operativa; notificar a los reguladores si es obligatorio; restablecer el servicio. *Evidencia esperada:* matriz. *Rúbrica:* 3 = una A por fila; el SOC, R en el triaje; FSTS Security, A en la contención técnica; el jefe de turno de Agua, A en la respuesta operativa; la A de la notificación regulatoria recae en el rol designado del operador, no en FSTS; Kell, C en el acceso del proveedor; 2 = una fila errónea; 1 = siguen varias A; 0 = nada.

**EX062 — Defina un desencadenante.** *Objetivo:* precisar «telemetría no fiable». *Entradas:* las alertas de LANTERN del capítulo 19 y los resultados de validación del capítulo 3. *Restricciones:* condiciones medibles; no debe activarse con averías ordinarias de una sola estación. *Pasos:* (1) redacte las condiciones del desencadenante; (2) indique quién lo declara y quién lo da por terminado; (3) indique qué hace Agua cuando se declara. *Evidencia esperada:* media página. *Rúbrica:* 3 = condiciones como un cambio no autorizado confirmado en un retransmisor, fallos de MAC en varias estaciones o un fallo de integridad del retransmisor; lo declara el responsable de seguridad de FSTS con el jefe de turno de Agua; Agua pasa a lecturas manuales y muestreo; la condición de fin exige un estado limpio verificado; 2 = condiciones vagas; 1 = «cuando parezca que algo va mal»; 0 = nada.

**EX063 — Preguntas al proveedor.** *Objetivo:* integrar a un proveedor. *Entradas:* Kell Instruments. *Restricciones:* seis preguntas; cada una vinculada a un proceso de LANTERN. *Pasos:* redacte las preguntas y el proceso al que alimenta cada una. *Evidencia esperada:* lista. *Rúbrica:* 3 = por ejemplo, cómo notifica Kell las vulnerabilidades (capítulo 16), cómo se controla y revoca el acceso de su personal (capítulo 7), su compromiso de notificar incidentes (este capítulo), cómo se firma el firmware (capítulo 27), las fechas de fin de soporte (capítulo 11) y la disponibilidad de una SBOM ([CISA SBOM](https://www.cisa.gov/sbom)); 2 = cuatro o cinco; 1 = genéricas; 0 = nada.

### Síntesis del capítulo

Un servicio está integrado cuando cada vecino (operadores, el SOC, proveedores, planificadores de emergencias) tiene una interfaz acordada: qué se proporciona, con qué rapidez, a quién y qué ocurre cuando falla. Pruebe las matrices de responsabilidades con escenarios hasta que cada actividad tenga un solo rol que rinda cuentas. Incorpore a los proveedores a los procesos de cambios, vulnerabilidades e incidentes. Acuerde y ejercite los desencadenantes que conectan un incidente técnico con los planes de continuidad del operador, incluido el estado «activo pero no fiable».

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Siga estudiando — capítulo 21 de 30

[← Capítulo 20](#ch-20) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 22 →](../../en/book/MANUSCRIPT.md#ch-22)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resultados resueltos y notas de evaluación

Cada resultado resuelto muestra una respuesta defendible y explica lo que premia la rúbrica. Una respuesta distinta puede obtener la máxima puntuación cuando cumple el mismo nivel de exigencia en cuanto a evidencia, alcance y honestidad sobre los límites. Los resultados numéricos proceden de los laboratorios sin conexión de este libro, ejecutados con Python 3.13.5 y solo con la biblioteca estándar; si su salida difiere, compruebe primero la versión de Python y si ha cambiado los datos sintéticos. Todas las cifras describen datos sintéticos; no las presente nunca como hallazgos sobre operadores reales.

### Capítulo 1: EX001–EX003

**EX001 — Plazo de suministro frente a tiempo de aviso.** Espacio libre necesario cuando se presenta la solicitud = (30 días de plazo + 7 días de margen) × 1,91 GB/día ≈ 70,7 GB. Presente la solicitud cuando el espacio usado llegue a unos 200 − 70,7 ≈ 129 GB, es decir, con el disco lleno en torno al 65 %. RLY-01 está en 120,9 GB y llegará a 129 GB en unos (129,3 − 120,9) / 1,91 ≈ 4,4 días. La alarma del 85 % salta cuando solo quedan unos 15,7 días de crecimiento antes de llenarse (la mitad del plazo de adquisición), así que llega demasiado tarde como *desencadenante de la compra*; manténgala como alarma operativa y añada un umbral del 65 % para «presentar la solicitud de capacidad». La máxima puntuación señala además que corregir la conservación (EX002) puede hacer innecesaria la compra.

**EX002 — Explique el crecimiento.** 120,9 GB ÷ 1,91 GB/día ≈ 63 días de datos, más del doble de los 30 días de conservación. *Observado:* uso del disco y ritmo de crecimiento. *Inferido:* se están conservando datos de más de 30 días. Causas plausibles: (a) la rotación de registros se ejecuta pero no se borran los archivos antiguos (número de rotaciones demasiado alto, o compresión sin borrado); (b) el búfer hacia el destino del retransmisor conservó mensajes durante un antiguo corte del historiador y nunca los purgó; (c) un segundo flujo de registros (de depuración o de auditoría) queda fuera de la política de rotación. Comprobaciones (de solo lectura): listar los archivos más antiguos por directorio y fecha de modificación; comparar la configuración de la rotación con la política; comprobar el tamaño del directorio del búfer y su entrada más antigua. *Abierto:* causa confirmada — E. Strand, antes del viernes.

**EX003 — Lista de comprobación de fallos silenciosos.** Filas de ejemplo: (1) disco que se llena — % usado y previsión de días hasta llenarse — aviso al 65 % / alarma al 85 % — guardia de plataforma — aumentar la capacidad o corregir la conservación; (2) rotación de registros detenida — antigüedad del archivo de registro activo más antiguo — > 2 días — guardia de plataforma — corregir la rotación; (3) caducidad de certificados — días hasta la caducidad de los certificados del retransmisor y del historiador — < 30 días — equipo de plataforma — renovarlos mediante un cambio estándar; (4) desviación del reloj — desfase respecto del NTP interno — aviso > 1 s, alarma > 2 s — guardia — comprobar la fuente de hora; (5) trabajo programado fallido — resultado del trabajo de copia de seguridad y antigüedad de la prueba de restauración — cualquier fallo, o prueba de restauración > 90 días — responsable del servicio — volver a ejecutarlo e investigar. La máxima puntuación exige umbrales medibles con tiempo de aviso y un lector designado.

### Capítulo 2: EX004–EX006

**EX004 — Clasifique y priorice.** (1) Zona corporativa 10.40.3.7 → PS-04 tcp/502: observado pero no declarado; primero, porque alcanza el proceso físico con un protocolo sin autenticación; contacte con Operaciones de Agua y con el responsable de la estación de trabajo. (2) RTU de PS-09 en silencio: declarado pero no observado; prioridad operativa, porque Agua puede estar operando a ciegas; contacte con la sala de control de Agua ese mismo día. (3) Externa 192.0.2.44 → retransmisor tcp/22: observado pero no declarado; SSH expuesto más allá del servidor de salto; responsable de la plataforma de FSTS; compruebe si algún inicio de sesión tuvo éxito (capítulo 17). (4) Retransmisor → externa tcp/443: observado pero no declarado; probablemente tráfico de actualización, la menor consecuencia; responsable de la plataforma. Ordenar por número de conversaciones pondría erróneamente primero el tráfico entre retransmisor e historiador o los flujos de las estaciones; decide la consecuencia.

**EX005 — Actualice la declaración.** Actualizaciones del retransmisor: o bien añadir un conducto acotado (retransmisor → espejo de actualizaciones con nombre o, mejor, un servidor interno de actualizaciones de FSTS, tcp/443, propósito «actualizaciones del sistema operativo», responsable FSTS Platform, revisión anual), o bien eliminar el acceso directo a internet y apuntar el retransmisor al servidor interno de actualizaciones; se prefiere lo segundo, porque el retransmisor no debería alcanzar internet. Portátil del ingeniero: eliminar el camino de la zona corporativa a la estación; declarar un camino de ingeniería desde el servidor de salto de gestión (MFA, registro de sesiones) hasta la interfaz de ingeniería de la estación, responsable Ingeniería de Agua, propósito «configuración de PLC», habilitado solo para trabajos aprobados. La máxima puntuación se niega a «permitir lo observado» y pone responsables y propósitos en cada entrada nueva.

**EX006 — Amplíe el laboratorio.** Un cambio mínimo: en el bucle, después de calcular `key`, añada `if "unknown" in key[:2]: print(f"UNKNOWN ZONE {s:>12} -> {d:<12} {p}/{port} n={count}"); continue`. Con la línea añadida `10.50.1.9,10.30.0.5,tcp,443,5`, la nueva salida incluye `UNKNOWN ZONE    10.50.1.9 -> 10.30.0.5    tcp/443 n=5`. La máxima puntuación explica que «zona desconocida» significa que el inventario o el mapa de zonas está incompleto, un hallazgo distinto de un camino no declarado entre zonas conocidas.

### Capítulo 3: EX007–EX009

**EX007 — Prediga y después ejecute.** Salida para las tres líneas añadidas: `inf` → `reject: not finite`; `12.0` → `accept` (la comprobación de rango es inclusiva); `-0.0` → `accept` (−0,0 es igual a 0,0, así que está dentro del rango, y la secuencia 104 es mayor que 103). Los recuentos pasan a ser `{'accept': 5, 'reject': 7, 'quarantine': 2}`. Un buen comentario señala que −0,0 es inofensivo pero debería normalizarse a 0,0 antes de almacenarse, para que las comparaciones y visualizaciones posteriores sean coherentes, y que un nivel exactamente en el límite de 12,0 m podría merecer revisión por sí mismo si 12,0 es la altura de rebose.

**EX008 — Diseño de la cuarentena.** Los mensajes en cuarentena van a una tabla separada con el mensaje en bruto, el motivo y la hora, y se conservan 90 días (más si forman parte de un incidente). La monitorización de FSTS los revisa en menos de una hora laborable durante el día, y por la noche lo hace la guardia cuando salta la regla siguiente. Escalado: dos o más lecturas inverosímiles consecutivas de cloro o de nivel de una misma estación, o cualquier lectura de cloro inverosímil durante una ventana de cambio de dosificación, desencadenan una llamada a la sala de control de Agua. La pantalla del operador muestra «valor retenido: en revisión» con la antigüedad del último valor bueno, nunca el último valor bueno como si fuera actual. La máxima puntuación vincula el escalado al proceso físico y asigna un responsable a cada paso.

**EX009 — Falle de forma cerrada.** Con el `except: pass` desnudo, un valor no numérico como `abc` deja `v` sin asignar en el primer mensaje (un `NameError`, que puede hacer caer el retransmisor: una denegación de servicio) o, dentro de un bucle, conserva el valor del mensaje *anterior*, que entonces se comprueba y posiblemente se acepta como si perteneciera a este mensaje. Tampoco hay límite inferior, así que se aceptan valores negativos, y `nan` pasa porque `nan > hi` es falso. Corregido: `try: v = float(val) except ValueError: return "reject: not numeric"`; `if not math.isfinite(v): return "reject: not finite"`; `if not lo <= v <= hi: return "quarantine: out of physical range"`; después, las comprobaciones posteriores; y el `return "accept"` final solo tras todas las comprobaciones.

### Capítulo 4: EX010–EX012

**EX010 — Encuentre el activo oculto.** Con `JOIN`, la consulta de criticidad 1 imprime solo `('Water Ops', 3)` y `('Clinical Eng', 1)`; la fila `('(none)', 1)` desaparece, así que el total baja de 5 a 4. PS09-RTU desaparece porque no tiene responsable y una combinación interna conserva solo las filas que tienen correspondencia. En un informe de gestión, esto significa que el único activo crítico que no pertenece a nadie (el que tiene más probabilidades de quedar desatendido) falta en el recuento que supuestamente muestra la cobertura.

**EX011 — Añada una restricción y una tabla.** Esquema: `CREATE TABLE review(asset_id TEXT NOT NULL REFERENCES asset(id), reviewed TEXT NOT NULL, reviewer TEXT NOT NULL, result TEXT NOT NULL CHECK (result IN ('ok','issue','not-reachable')))`, ejecutando antes `PRAGMA foreign_keys = ON` en la conexión. Insertar `('NOPE','2026-10-01','b.lind','ok')` lanza `sqlite3.IntegrityError: FOREIGN KEY constraint failed`. Consulta: `SELECT a.id FROM asset a WHERE a.criticality = 1 AND NOT EXISTS (SELECT 1 FROM review r WHERE r.asset_id = a.id AND r.reviewed >= '2026-07-14')`; sin revisiones insertadas, aparecen los cinco activos de criticidad 1. La máxima puntuación advierte que una combinación interna con `review` no habría devuelto *ninguno* de los activos nunca revisados.

**EX012 — De la hoja de cálculo al modelo.** Fallos: registro duplicado del PLC de PS-03 con distinta capitalización ("PLC"/"plc"), que evita una clave primaria sobre la etiqueta del activo; variantes de responsable "Water Ops"/"water operations", que evita una clave foránea a una tabla de responsables; responsable registrado como una persona que se ha ido, que evita un responsable como función, con actualizaciones de altas, cambios y bajas (capítulo 7); firmware "?", que evita un `NULL` explícito con el significado de desconocido, consultado como hallazgo; formatos de fecha mezclados "Jun 2027"/"30/06/27", que evitan las fechas ISO 8601; "TBC" en un campo de fecha, que evita un `NULL` más una incidencia, nunca texto en una columna de fecha. La máxima puntuación asigna cada fallo a una decisión de diseño.

### Capítulo 5: EX013–EX015

**EX013 — Precisión terminológica.** Reescritura: «La RTU de PS-09 es un activo crítico. La cuenta remota permanente del proveedor sin MFA es una vulnerabilidad y, como es alcanzable desde fuera, es una exposición que un grupo criminal o un técnico descuidado del proveedor (amenazas) podrían aprovechar. La habilitación limitada en el tiempo con MFA es el control que falta». Correcciones: la cuenta no es una amenaza; la RTU es un activo, no un riesgo; el riesgo es la probabilidad y la consecuencia de un daño, no un objeto; «sin control» debería nombrar el control concreto que falta.

**EX014 — Prevenir, detectar, recuperar.** Prevenir: cambios en la configuración del retransmisor solo a través de un estado deseado bajo control de versiones con revisión por pares (evidencia: configuración de rama protegida y registros de revisión). Detectar: alerta de integridad de archivos sobre la configuración del retransmisor y regla de silencio de estación (evidencia: un cambio de prueba inyectado y un silencio de prueba produjeron cada uno una alerta dentro del objetivo; capítulo 23). Recuperar: configuración versionada con un manual de vuelta atrás probado (evidencia: vuelta atrás cronometrada en un retransmisor de prueba). La máxima puntuación aporta evidencia comprobable, no «configurado».

**EX015 — Lectura de un informe de incidente.** Según CISA AA21-042A, el aviso recomendaba, entre otras medidas, restringir y proteger el software de acceso remoto, no compartir contraseñas, usar sistemas operativos actualizados y con soporte y mantener los sistemas de control sin exposición directa a internet, con cortafuegos. El relato de WUSF (abril de 2023) informa de que un antiguo responsable municipal dijo que el suceso fue probablemente un error de un empleado; eso cambia la *atribución*, no el valor de las lecciones de higiene, y muestra que los primeros relatos pueden revisarse. Reglas de LANTERN: ninguna herramienta de acceso remoto en ningún equipo de control o retransmisor salvo a través del camino de salto (capítulo 8); ninguna cuenta de administrador compartida (capítulo 7); toda sesión privilegiada registrada para poder responder después a «qué ocurrió» (capítulo 17).

### Capítulo 6: EX016–EX018

**EX016 — Revisión de bastionado.** Limitar SSH a la interfaz de gestión (cambio normal, porque un error deja fuera a los administradores); eliminar el puerto de depuración en 0.0.0.0:9000 (cambio normal, después de conservar la evidencia de quién lo habilitó; capítulo 20); desactivar RPC en el puerto 111 (cambio estándar si existe un procedimiento); eliminar el compilador y el entorno de escritorio (cambio estándar); trasladar el retransmisor de `root` a una cuenta dedicada `relay` con restricciones del sistema de archivos (cambio normal con pruebas). Cada cambio tiene un motivo vinculado a las secciones 6.1 y 6.2.

**EX017 — Proteja la línea base.** Diseño 1: tras cada cambio aprobado, la línea base se exporta a un almacén de escritura única fuera del equipo (un contenedor de solo anexado o un servidor que los administradores del retransmisor no pueden modificar). Diseño 2: el archivo de la línea base se firma con una clave que custodia el equipo de seguridad, no el retransmisor; la comparación verifica primero la firma. Un atacante con root en el retransmisor puede alterar archivos e incluso la copia local de la línea base, pero no puede alterar sin ser detectado la línea base externa o firmada. Como la propia herramienta de comparación del retransmisor podría subvertirse, ejecute también la comparación desde fuera (recogiendo los hashes de forma remota o comparando fuera del equipo los archivos recogidos).

**EX018 — Ubicación en el hipervisor.** Compartido: el hardware físico y sus fallos; los administradores del hipervisor (que en la práctica administran todos los invitados); la red de gestión; el almacenamiento y las instantáneas; el calendario de parches. Condiciones para aceptarla: gestión del hipervisor en una zona propia, alcanzable solo desde el servidor de salto; un grupo pequeño de administración del hipervisor con MFA y registro; redes virtuales separadas sin puentes entre los invitados orientados a las estaciones y los orientados a la zona corporativa; margen de capacidad documentado para todos los invitados en el pico; plan probado para la pérdida del equipo (qué falla a la vez para el agua *y* para el hospital). Riesgo residual: un compromiso o fallo del hipervisor afecta a dos sectores; lo aceptan conjuntamente los responsables de los servicios de Agua y del hospital. Rechazarla de plano sin condiciones obtiene menos puntuación que esto.

### Capítulo 7: EX019–EX021

**EX019 — Priorice los hallazgos.** Hoy: `c.mendes`, usada después de la baja: (1) conservar los registros de autenticación y de sesión de HIST-01, (2) deshabilitar la cuenta y abrir un incidente; `vendor-kell`, administrador permanente sin MFA: (1) confirmar con Agua que no hay ningún trabajo de Kell en curso, (2) deshabilitar la cuenta y pasar a una habilitación limitada en el tiempo. Esta semana: `d.reyes` (retirar el acceso de administración, confirmar la necesidad con Ingeniería Clínica), `opsuser` (planificar la migración a cuentas personales o a una bóveda sin romper la operación de emergencia), `f.ito` (identificarla; deshabilitarla si nadie responde por ella). Este trimestre: correcciones del proceso para las fuentes de altas y bajas. La máxima puntuación pone la conservación antes de la deshabilitación.

**EX020 — Acceso de proveedor limitado en el tiempo.** (1) Kell abre una incidencia o llama a la guardia de FSTS con una referencia de trabajo; (2) la guardia comprueba el trabajo con el jefe de turno de Agua; (3) la guardia habilita `vendor-kell` mediante la herramienta de acceso durante una ventana fija (por ejemplo, cuatro horas), con el objetivo de tardar menos de 15 minutos desde la solicitud; (4) Kell se autentica con MFA a través del servidor de salto; (5) la sesión se graba o se registra; (6) salta una alerta ante cualquier inicio de sesión de Kell fuera de una ventana habilitada; (7) la cuenta caduca automáticamente; (8) el siguiente día laborable, FSTS Security revisa el registro de la sesión frente al trabajo. Evidencia conservada: incidencia, aprobación, registros de habilitación y caducidad, grabación de la sesión y nota de revisión.

**EX021 — Amplíe la revisión.** Añada después del bucle: construya `admins = {}`, que asigna a cada persona el conjunto de sistemas en los que tiene acceso de administración, y señale a quien tenga a la vez `RLY-01` y `HIST-01`. Con la cuenta nueva `("b.lind", "HIST-01", "admin", "2026-10-12", True, "person")`, la salida añade `b.lind       HIST-01  role admin not justified for FSTS Security` y el hallazgo de concentración `b.lind admin on both RLY-01 and HIST-01`. No se señala a ninguna otra persona (e.strand y d.reyes tienen acceso de administración en un solo sistema cada una). La máxima puntuación advierte el hallazgo «no justificado»: la tabla de necesidades no da a FSTS Security ninguna función en HIST-01.

### Capítulo 8: EX022–EX024

**EX022 — Compruebe el sentido de la confianza.** (a) Rediseñar: una lista de estaciones permitidas descargada del historiador convierte un sistema de la zona corporativa en la fuente de la configuración de seguridad del retransmisor; en su lugar, la lista procede del control de versiones a través del proceso de cambios (capítulo 14) y se despliega en los retransmisores. (b) Rediseñar con cuidado: el bloqueo automático en el cortafuegos de las estaciones podría cortar telemetría legítima o el acceso de ingeniería durante un incidente; necesita el acuerdo de Agua, un modo de fallo seguro y un alcance limitado al tráfico ajeno al proceso, o bien limitarse a alertar con una confirmación humana de un solo clic. (c) Aceptable solo con un nuevo conducto declarado, una entrada en el registro de flujos de datos (capítulo 12), condiciones contractuales y de conservación con Halden, cifrado y monitorización, y la fecha de fin de la prueba.

**EX023 — Independencia de las capas.** La dependencia común es una persona y un conjunto de credenciales: el cortafuegos, la administración del retransmisor, la custodia de la clave y la monitorización dependen de E. Strand. Un único suceso (el compromiso de la cuenta de E. Strand, o un error bienintencionado) puede desactivar todas las capas y también su detección. Cambios: separar las funciones (el equipo de red es responsable del cortafuegos; el de plataforma, del retransmisor; el de seguridad, de las reglas de monitorización y de su revisión), y guardar las claves en un almacén con custodios distintos, para que los administradores del retransmisor no puedan leerlas ni sustituirlas sin que se note.

**EX024 — Modo degradado.** Operadores: las pantallas del historiador muestran que la antigüedad de los valores aumenta y un aviso de «retransmisor fuera de línea», no valores congelados presentados como actuales. Datos: las estaciones almacenan localmente (24 h). Alertas: las alertas de salud del retransmisor y de silencio de estación llegan a la guardia de FSTS y a la sala de control de Agua en 15 a 20 minutos. Regreso: las estaciones cargan el atraso; el retransmisor necesita margen para la ráfaga (capítulo 1); los mensajes atrasados son más antiguos que la ventana temporal en vivo y deben aceptarse por un camino explícito para el atraso que siga comprobando el MAC y la secuencia (capítulo 15), de modo que la comprobación de reproducción no los rechace erróneamente y tampoco se convierta en un hueco para reproducciones.

### Capítulo 9: EX025–EX027

**EX025 — Reescriba la línea del informe.** «Correcciones del proveedor instaladas: TI corporativa 12/12 (mediana de 5,5 días); retransmisor/historiador 6/8 (mediana de 18,5 días, 2 abiertas); controladores de las estaciones 3/8 (mediana de 95 días, 5 aún abiertas, todas bajo controles compensatorios). No se informa de la mediana conjunta de 9 días porque mezcla grupos y excluye las correcciones abiertas». Se deja fuera: los valores p90 y las medias (disponibles en el anexo del informe), para que el titular sea breve.

**EX026 — Calcule la antigüedad de los elementos abiertos.** Valores de las estaciones: instaladas 64, 95, 140; antigüedades abiertas 20, 45, 70, 130, 200. Ordenados: 20, 45, 64, 70, 95, 130, 140, 200; mediana = (70 + 95) / 2 = 82,5 días. Es un límite inferior porque la latencia final de cada corrección abierta será al menos su antigüedad actual; la mediana real solo puede subir a medida que envejecen las correcciones abiertas. Difiere de la mediana calculada solo con las instaladas (95 días), aquí más baja porque varias correcciones abiertas son recientes, lo que muestra por qué deben comunicarse ambas juntas en lugar de elegir una.

**EX027 — ¿Cuántos simulacros?** Al calcular el límite inferior de Wilson para n éxitos de n: 15/15 da alrededor de 0,796 y 16/16, alrededor de 0,806. Así que se necesitan 16 simulacros consecutivos con éxito: 16 meses a un simulacro por mes. Alternativas: hacer restauraciones parciales más pequeñas y frecuentes (una tabla o un día de datos cada semana), automatizar pruebas de restauración en una instancia de pruebas y mantener el simulacro completo cada trimestre; informe de cada tipo por separado para que la afirmación corresponda a la prueba.

### Capítulo 10: EX028–EX030

**EX028 — La consecuencia en personas y tiempo.** Supuestos señalados como sintéticos. Agua: «Unas 41.000 personas no pierden nada de inmediato (la telemetría continúa), pero FSTS no puede modificar los retransmisores mientras dure el corte; esto solo se vuelve dañino si se produce un fallo de un retransmisor antes de la reparación». Hospital: «Los pacientes con bombas de infusión de la planta 3 (unos 30 a la vez) pueden recibir el tratamiento con una biblioteca de fármacos desactualizada si se pierde la actualización de las 06:00; dañino a partir de las 06:00, porque la actualización corrige un límite de dosificación». Cocheras: «Los pasajeros ven un horario desactualizado en los quioscos desde el primer autobús de la mañana; molesto, no dañino». El plazo de seguridad del paciente de las 06:00 del hospital es el más temprano.

**EX029 — Mapa de dependencias compartidas.** Servidor de salto, SIEM, directorio de identidades, sistema de copias de seguridad: interdependencias cibernéticas y lógicas entre los tres clientes. BayTel: un operador común cibernético/físico para la telemetría del agua y la conexión a internet del hospital; geográfica si ambos usan la misma central telefónica. Personal de FSTS: lógica. Fallo único de efecto más amplio: el compromiso del directorio de identidades (o de una cuenta privilegiada de FSTS en él), que da acceso a los sistemas de todos los clientes. Cambio: niveles privilegiados separados por cliente, con cuentas de administración separadas y MFA, de modo que una cuenta comprometida no abarque varios sectores; y un segundo camino de operador para la telemetría del agua.

**EX030 — La evidencia que usted debe.** Ejemplo con los CPG de CISA (versión consultada y citada): objetivo de inventario de activos; evidencia: el inventario con fechas de última verificación y el informe mensual de conciliación (capítulo 11), guardados en el sistema de inventario. Objetivo de MFA; evidencia: salida trimestral de la revisión de accesos con el estado de MFA (capítulo 7), guardada con la incidencia de la revisión. Objetivo de recogida de registros; evidencia: informe diario de vigencia de las fuentes de registros y recuentos del normalizador (capítulos 17 y 19), guardado en el SIEM. La máxima puntuación cita la fuente y la versión e indica la frecuencia y el lugar.

### Capítulo 11: EX031–EX033

**EX031 — Concilie.** Direcciones de los flujos sin registro en el inventario: 10.40.3.7 (una estación de trabajo corporativa; también es el origen de los flujos Modbus no declarados; responsable, el equipo de puestos de trabajo de FSTS; regístrela y averigüe quién la usa). Activos del inventario en estas zonas que nunca se vieron en los flujos: SW-STN-04, lo esperable, porque un conmutador reenvía tráfico en lugar de originarlo en estos registros de flujo; verifíquelo en su lugar con los datos de gestión del conmutador; PS09-RTU, vista solo como origen declarado sin tráfico: la estación en silencio (Operaciones de Agua, el mismo día). HIST-01 (10.40.8.20) y los PLC concilian. La máxima puntuación explica por qué «no visto» significa cosas distintas para un conmutador y para una RTU.

**EX032 — Controles compensatorios.** (1) Conducto restringido para que PS09-RTU solo pueda comunicarse con el retransmisor por tcp/502; evidencia: la regla del cortafuegos y la revisión mensual de flujos. (2) Validación y cuarentena por rango en el retransmisor para las etiquetas de PS-09; evidencia: pruebas al estilo del Lab 3 en el retransmisor. (3) Alertas de silencio de estación y de valor inverosímil para PS-09; evidencia: pruebas inyectadas (capítulo 23). (4) RTU de repuesto en el almacén o un procedimiento manual de lectura probado; evidencia: registro del almacén o registro del ejercicio. (5) Copia de seguridad de la configuración de la RTU por parte de Ingeniería de Agua; evidencia: exportación fechada. Sustitución a cargo del jefe de Ingeniería de Agua, con fecha objetivo dentro de 14 meses; los controles terminan cuando se verifica la sustitución.

**EX033 — Plan de descubrimiento.** Semanas 1 a 3: fuentes pasivas (registros de flujo de los cortafuegos central y de las estaciones, tablas MAC/ARP de los conmutadores exportadas por el ingeniero de red de Agua, exportaciones de ingeniería de las configuraciones de PLC/RTU, registros de compras y mantenimiento); construya un inventario preliminar con columnas de «fuente». Semanas 4 a 12: dos visitas por semana (capítulo 28) a las estaciones con más discrepancias, para confirmar los dispositivos físicos y el firmware con el ingeniero de Agua. Un método activo solo está justificado si las fuentes pasivas no pueden ver un segmento; en ese caso: acordado con Operaciones de Agua, probado primero en un dispositivo de repuesto del mismo modelo, con limitación de ritmo, dentro de una ventana aprobada, con un ingeniero en la instalación y una condición de parada. Calendario realista: 14 estaciones a dos visitas por semana caben en siete semanas.

### Capítulo 12: EX034–EX036

**EX034 — Clasifique las diferencias por prioridad.** (1) CLIN-GW → REPORTS, vinculado a pacientes, no registrado: primera acción, informar al responsable de los datos del hospital y acordar detener el flujo mientras se evalúa; responsable: el responsable de los datos del hospital junto con FSTS Security. (2) Conservación de DF5 de 400 días frente a 30 en Halden: informar al responsable de los datos del hospital; cotejar la configuración de conservación de Halden con el contrato; responsable: el responsable de los datos del hospital junto con el gestor de proveedores de FSTS. (3) HIST-01 → VENDOR-SUPPORT, texto claro, no registrado: detenerlo o trasladarlo a un flujo cifrado y registrado; responsable: el responsable de los datos de Agua junto con FSTS Platform. Si alguno de los dos primeros debe comunicarse fuera de FSTS (por ejemplo, como violación de la seguridad de los datos personales) lo decide la función de protección de datos del hospital, no el tecnólogo.

**EX035 — Redacte una entrada del registro.** DF7; origen: tarea de exportación de HIST-01 (no la RTU); destino: punto de acceso de diagnóstico remoto de Kell; clase de datos: telemetría operativa, solo las etiquetas LEVEL_M de PS-09, agregados horarios; cifrado: TLS 1.3; conservación en Kell: 30 días, según una cláusula del contrato; propósito: diagnóstico de fallos de la RTU durante el periodo de soporte; responsable: el jefe de Ingeniería de Agua; conducto: nuevo conducto declarado HIST-01 → punto de acceso de Kell por tcp/443; aprobaciones: responsable de los datos de Agua, FSTS Security; caducidad: 6 meses, renovable tras revisión. La máxima puntuación envía los datos desde un sistema de nivel superior en lugar de dejar que el proveedor alcance la estación.

**EX036 — Amplíe la comprobación.** Añada `APPROVED_PATIENT_DESTS = {"CLIN-GW", "HALDEN-CLOUD"}` y, para cada flujo observado de clase `patient-linked` cuyo destino no esté en ese conjunto, añada la incidencia "patient-linked data to unapproved destination". Tras registrar DF6, la línea CLIN-GW → REPORTS pasa a ser `HIGH DF6 CLIN-GW->REPORTS patient-linked data to unapproved destination` en lugar de «no registrado». Explicación: el registro recoge decisiones; un flujo registrado puede seguir siendo una mala decisión. Registrarlo sin revisión haría que la comprobación se superara mientras los datos de los pacientes siguen en un sistema corporativo de informes que usa el personal de agua.

### Capítulo 13: EX037–EX039

**EX037 — Redacte dos escenarios.** BayTel: «Una avería en una central telefónica de BayTel corta durante ocho horas los enlaces de operador de seis estaciones (de PS-08 a PS-13). Las estaciones almacenan localmente; los operadores pierden las lecturas en vivo del área de suministro de unas 18.000 personas y deben enviar personal a tomar lecturas manuales. Controles existentes: almacenamiento en las estaciones (probado cada trimestre), alertas de silencio de estación (probadas, 8/8), procedimiento de lectura manual (ejercitado el año pasado). Franja de consecuencia 4». Servidor de salto: «El servidor de salto de FSTS se ve comprometido mediante una credencial de administrador robada; el atacante alcanza la administración del retransmisor y de la pasarela del hospital. Consecuencia: posible falsificación de la telemetría para 41.000 personas e interrupción de la pasarela clínica. Controles existentes: MFA (configurada; resistencia al phishing no probada), registro de sesiones (sin probar), alertas de deriva (probadas)». Ambos son concretos y nombran su estado de prueba.

**EX038 — Producto frente a consecuencia.** «R3, el llenado del disco del retransmisor, ocurre con más frecuencia, así que puntúa más cuando multiplicamos lo probable que es por lo grave que es. Pero si ocurre R3, perdemos algunas lecturas durante unas horas y podemos recuperarlas. R2 y R4 podrían dañar a personas: una dosis de cloro errónea o un límite de fármaco erróneo en una bomba de infusión. Multiplicar trata «frecuente y recuperable» igual que «raro y dañino», y no es así como queremos repartir el esfuerzo. Por eso abordamos primero R2 y R4. R3 sigue necesitando una acción, y es barata: corregir este mes el fallo de conservación y configurar una alarma de capacidad más temprana».

**EX039 — Del escenario al trabajo.** Prevención/reducción: (1) acceso de Kell limitado en el tiempo con MFA resistente al phishing; responsable: FSTS Security; evidencia: registros de habilitación y caducidad; (2) registro de las sesiones remotas del proveedor; FSTS Security; evidencia: revisión de una muestra de sesiones; (3) límites de los puntos de consigna de dosificación diseñados en el PLC de PS-07; Ingeniería de Agua; evidencia: registro de la prueba de ingeniería releído en la instalación. Detección: (4) alerta de LANTERN cuando el cloro sale de la banda aprobada o cambia más rápido que un ritmo fijado; monitorización de FSTS; evidencia: lectura de prueba inyectada; (5) comparación de los valores de los puntos de consigna del PLC con una línea base aprobada en cada exportación de ingeniería; Ingeniería de Agua; evidencia: comparación fechada.

### Capítulo 14: EX040–EX042

**EX040 — Clasifique cambios.** (a) Estándar: sigue el procedimiento de PS-11; aprobado por procedimiento y registrado. (b) Normal: plan revisado, canario y reversión (capítulo 27); aprobador: el responsable del servicio, con Agua informada. (c) De emergencia: aprobado por la autoridad de seguridad de guardia; revisado el siguiente día laborable. (d) Normal: afecta a los registros y posiblemente a las obligaciones; aprobador: el responsable de los datos de Agua, con el responsable del servicio de FSTS. (e) Normal (pasa a estándar cuando exista un manual de operación probado): coordinado con Agua porque las estaciones quedan en silencio si las claves no coinciden.

**EX041 — Pasos de verificación.** (1) El registro de conexiones del retransmisor muestra TLS 1.3 negociado con HIST-01; (2) el historiador recibe lecturas de todas las estaciones con la latencia normal de 60 s durante una hora; (3) los recuentos de errores y rechazos del retransmisor no cambian respecto a la hora anterior; (4) la validación de certificados sigue aplicándose: una conexión de prueba a un equipo con un certificado no confiable falla; (5) la comprobación de integridad muestra que solo cambió el archivo de configuración de TLS, con el número de cambio.

**EX042 — Revise un cambio de emergencia.** Preguntas: ¿por qué falló la ruta del servidor de salto? ¿Quién aprobó la regla y bajo qué autoridad de emergencia? ¿Qué sistemas se alcanzaron a través de ella durante la ventana, y quién lo hizo (registros)? ¿Sigue vigente la regla? Decisión: eliminar la regla con un registro de cambio; si sigue haciendo falta, restringirla a una única dirección de administrador durante un tiempo fijo. Cambio de proceso: hacer resiliente el servidor de salto (un segundo servidor de salto o una vía de acceso de emergencia probada, con registro y alertas) y añadir las «reglas temporales», con su caducidad, al informe diario de salud.

### Capítulo 15: EX043–EX045

**EX043 — Orden de las comprobaciones.** Si solo se mueve la *comprobación* de reproducción antes de la comprobación del MAC (con la actualización de estado aún después del MAC), el mensaje del atacante con seq 1000000 supera la comprobación de reproducción, falla en el MAC y se rechaza sin actualizar el estado; después se acepta el seq 3 legítimo. Si la actualización de estado se mueve con ella, el mensaje del atacante fija la última secuencia de PS-04 en 1000000 antes de fallar en la autenticación, y el seq 3 legítimo se rechaza como reproducción: el atacante ha bloqueado la estación con mensajes sin autenticar. La regla segura: autenticar primero y actualizar el estado solo después de que se superen todas las comprobaciones.

**EX044 — Claves por estación.** Analice el cuerpo (`json.loads`) solo para leer `st`, busque `KEYS.get(st)` y rechace si no existe; verifique el MAC con esa clave; solo después de la verificación lea cualquier otro campo o toque el estado. El ID de estación sin verificar es un mero selector de clave: si un atacante miente sobre él, la comprobación del MAC falla porque no posee la clave de esa estación. No registre como hechos los campos sin verificar, no actualice el estado con ellos y no los use para ninguna decisión que no sea la selección de la clave.

**EX045 — Tamaño de la ventana.** Ventana en vivo: unos 60–120 s, que cubren el error de reloj de ±2 s y el retraso de 40 s del operador con margen; 120 s, como en el laboratorio, es razonable. Acumulación: las estaciones marcan las subidas de la acumulación (un indicador dentro del cuerpo autenticado); el retransmisor las acepta por una vía separada que sigue exigiendo un MAC válido y números de secuencia estrictamente crecientes, acepta marcas de tiempo de hasta 24 h de antigüedad solo en este modo, emite una alerta informativa cada vez que se usa el modo de acumulación y termina ese modo cuando los mensajes de la estación alcanzan el tiempo real. Una única ventana de 24 horas para todos los mensajes facilitaría mucho la captura y la reproducción.

### Capítulo 16: EX046–EX048

**EX046 — Priorice tres avisos.** Primero (b), el fallo de SSH del retransmisor: explotado activamente (KEV) en un equipo de criticidad 1; la exposición restringida reduce la urgencia, pero no la elimina (el propio servidor de salto es un objetivo); objetivo: en pocos días. Segundo (c), la base de datos del historiador: gravedad alta y alcanzable desde toda la zona corporativa, en un equipo de criticidad 2 cuya pérdida afecta a los informes y a las investigaciones; objetivo: entre dos y cuatro semanas, antes si aparece explotación. Tercero (a), el navegador del quiosco: gravedad crítica y expuesto a internet, pero de consecuencia baja y rápido de reconstruir; objetivo: dentro del ciclo mensual normal, o retirar el acceso a internet. Una alternativa defendible intercambia (a) y (c) si el quiosco comparte red con sistemas de las cocheras de mayor consecuencia.

**EX047 — Plan de controles compensatorios.** (1) Deshabilitar la interfaz web del PLC si Agua confirma que no se usa; evidencia: exportación de ingeniería que la muestra desactivada; termina cuando se verifique la 4.3. (2) Restricción del conducto: solo la ruta de salto de ingeniería puede alcanzar el puerto web; evidencia: regla del cortafuegos y revisión de flujos que no muestra otros orígenes; termina con la 4.3. (3) Alerta ante cualquier conexión al puerto web del PLC; evidencia: probada con una conexión de prueba marcada en el PLC de repuesto; termina con la 4.3. (4) Comparación semanal de la configuración de PS-07; evidencia: comparaciones fechadas; termina con la 4.3. Responsable del riesgo residual: el jefe de ingeniería de Agua hasta la verificación.

**EX048 — Diseño de una prueba de restauración.** Entorno: un equipo de restauración aislado en una red de pruebas, sin conexión con la producción. Pasos: (T0) se registra la decisión de restaurar; se recupera la copia inmutable más reciente; se restaura la base de datos; se inicia el servicio del historiador; (T1) la cuenta de prueba de los operadores puede consultar los datos más recientes. Criterios de superación: T1 − T0 ≤ 4 h; los datos restaurados más recientes no son más de 24 h anteriores al momento de la copia (RPO); las sumas de comprobación o los recuentos de filas coinciden con el manifiesto de la copia. Registro: tiempos, antigüedad de los datos, problemas, desviaciones respecto al manual de operación y quién la realizó. Programación: prueba completa trimestral; prueba parcial mensual. Un mensaje de trabajo terminado no es una prueba de restauración.

### Capítulo 17: EX049–EX051

**EX049 — Corrija el formato del retransmisor.** Corregir primero en el origen: el retransmisor es un componente propio de FSTS, así que se configura su biblioteca de registro para que emita RFC 5424 con datos estructurados, mediante un cambio normal, verificado porque el recuento de líneas no analizadas del normalizador baja a cero. Añadir un analizador del formato BSD como alternativa para los dispositivos de terceros que no pueden cambiarse. Una línea BSD no tiene año ni zona horaria ("Oct 11 22:17:00"), así que el analizador debe suponer ambos (por ejemplo, el año del recopilador y la zona configurada en el dispositivo) y marcar el registro como de hora de menor calidad; tampoco tiene datos estructurados, así que los campos deben extraerse mediante patrones.

**EX050 — Orden de los eventos.** Orden escrito (sin tener en cuenta los desfases): 22:14:03 inicio de sesión en rly-01; 22:15:40 fallido; 22:15:41 fallido; 22:16:00 FLOW; 23:02:11 error de cuota de disco del historiador (la línea del quiosco no tiene hora). Orden UTC: 22:02:11 historiador; 22:14:03; 22:15:40; 22:15:41; 22:16:00. Un investigador que usara el orden escrito vería el error del historiador 46 minutos *después* de los inicios de sesión fallidos como root y podría vincularlo con ellos como consecuencia de un ataque; en UTC ocurrió *antes*, así que no pudieron causarlo.

**EX051 — Cuente lo que descarta.** Añada `assert len(out) + bad == len(lines), "input/output mismatch"` (o termine con un error) después del bucle; mantenga `unparsed_by_host` tomando como equipo el cuarto elemento separado por espacios de las líneas no analizadas, cuando exista (para la línea BSD, `rly-01`). La salida añade `unparsed by host: {'rly-01': 1}`. Un recuento creciente de líneas no analizadas de un equipo significa que esa fuente cambió de formato o se averió; todas las reglas que dependen de ella quedan ciegas en silencio, así que el sistema de monitorización debería alertar sobre ello (capítulo 19).

### Capítulo 18: EX052–EX054

**EX052 — Recorra un escenario.** Camino: (1) los datos conservados más allá de la política hacen crecer el disco → (2) el disco supera los umbrales → (3) fallan las escrituras → (4) el retransmisor pierde mensajes. Prevenir: aplicación de la conservación y rotación (evidencia: comprobación de la antigüedad del archivo más antiguo); previsión de capacidad con un umbral de plazo de antelación (capítulo 1) (evidencia: previsión mensual). Detectar: alarma de uso del disco al 65 %/85 % (probada con una prueba sintética de umbral); alerta por recuento de pérdidas/rechazos del retransmisor y alerta de silencio de estación (pruebas inyectadas). Recuperar: almacenamiento en las estaciones y subida de la acumulación (probados cada trimestre); manual de operación para liberar espacio con seguridad. Cada uno tiene una evidencia nombrada.

**EX053 — Comprobación con el catálogo.** Asignaciones en SP 800-53 Rev. 5: MFA del proveedor limitada en el tiempo → AC (*Access Control*, control de acceso) e IA (*Identification and Authentication*, identificación y autenticación); registro de sesiones → AU (*Audit and Accountability*, auditoría y rendición de cuentas); límites de los puntos de consigna del PLC → SI (*System and Information Integrity*, integridad del sistema y de la información) o CM (*Configuration Management*, gestión de la configuración); alerta de cloro → SI (monitorización del sistema); procedimiento de dosificación manual → CP (*Contingency Planning*, planificación de contingencias). Familia ausente: SR (*Supply Chain Risk Management*, gestión de riesgos de la cadena de suministro): las propias prácticas de seguridad de Kell determinan la probabilidad de que les roben las credenciales. Ficha propuesta: «Aseguramiento de la seguridad del proveedor: cuestionario anual y cláusulas contractuales que exijan MFA, revocación del acceso del personal en 24 h y notificación de incidentes; responsable: gestor de proveedores de FSTS; evidencia: contrato firmado y respuesta anual». También es aceptable IR (*Incident Response*, respuesta a incidentes) para un incidente de dosificación.

**EX054 — Duración del solapamiento.** El retransmisor debe aceptar la clave antigua durante al menos 24 horas después de la conmutación, más un margen (por ejemplo, 26–48 horas), porque los mensajes acumulados creados antes de la conmutación llevan MAC con la clave antigua. Cada mensaje lleva un identificador de versión de clave (dentro del cuerpo autenticado, o como selector sin autenticar, como el ID de estación del EX044); el retransmisor selecciona la clave por su versión en lugar de probarlas todas. Tras el solapamiento, se elimina la clave antigua y se verifica la eliminación: un mensaje de prueba sellado con la clave antigua debe ser rechazado entonces.

### Capítulo 19: EX055–EX057

**EX055 — Regla por episodios.** Agrupe los eventos de la regla B por (origen, destino); para cada grupo, abra un episodio en el primer evento y añádale los eventos posteriores que caigan dentro de 60 minutos. Salida: una línea como `22:16+  B corp->station Modbus 10.40.3.7->10.20.0.11 (2 events, last 22:31)`; el total de alertas baja de 4 a 3. Se conservan el recuento, las horas primera y última y el par, de modo que los investigadores no pierden nada mientras la persona de guardia recibe un aviso en lugar de dos.

**EX056 — Primeras acciones.** Regla A: (1) confirmar si SSH está expuesto más allá del servidor de salto (no debería estarlo: hallazgo del capítulo 2); (2) comprobar si hubo algún inicio de sesión correcto desde ese origen; (3) bloquear el origen en el perímetro mediante un cambio estándar y notificar la exposición como hallazgo. Regla B: (1) comprobar en el calendario de cambios si hay una sesión de ingeniería aprobada; (2) si no la hay, llamar a la sala de control de Agua y pedirle que vigile PS-04; (3) conservar los registros de flujos e identificar al usuario de la estación de trabajo. Regla C: (1) llamar a la sala de control de Agua para confirmar el estado de la estación; (2) comprobar el estado de BayTel; (3) revisar los registros del retransmisor en busca de rechazos por MAC o por ventana de esa estación (la carencia del capítulo 26).

**EX057 — Monitorice el monitor.** Fuentes: regla de ausencia por tasa de eventos de cada fuente (ningún evento durante 15 min de una fuente que normalmente envía cada minuto) → SOC. Reenviador: longitud de la cola o acumulación > 10 min → guardia de plataforma. Normalizador: proporción de líneas no analizadas > 1 % por equipo, o cualquier equipo nuevo con líneas no analizadas → guardia de plataforma. Reglas: última evaluación hace > 5 min → responsable del SOC. Avisos: un aviso sintético programado cada día a las 10:00 debe confirmarse en 15 min → si no, al responsable de guardia.

### Capítulo 20: EX058–EX060

**EX058 — Hipótesis y discriminantes.** (1) Claves que no coinciden tras una rotación en la estación pero no en el retransmisor: los rechazos son «bad MAC»; revisar el calendario de cambios y los registros de versión de clave. (2) Salto del reloj de la estación: los rechazos son «outside time window»; comparar las marcas de tiempo de la estación con las horas de recepción (método del Lab 20). (3) Estado de reproducción envenenado por un mensaje auténtico con un número de secuencia alto: los rechazos son «replay»; buscar un gran salto de secuencia justo antes de las 09:00 (capítulo 29). (4) Tráfico falsificado: «bad MAC» desde una dirección de origen inesperada o a un ritmo inusual mientras también llegan mensajes legítimos; revisar los flujos. Todas las comprobaciones son lecturas de registros.

**EX059 — Lista de conservación.** En orden, en diez minutos: (1) anotar la hora y abrir la incidencia; (2) copiar los registros del retransmisor (incluidos los de NTP y de rechazos) de los últimos 7 días; (3) exportar la configuración del cortafuegos y su historial de cambios reciente para el conducto entre el retransmisor y las estaciones; (4) exportar el extracto del historiador de PS-09 y la salida del análisis al estilo del Lab 20; (5) guardar como texto la salida de estado de `timedatectl`/NTP del retransmisor; (6) calcular el hash de cada archivo (SHA-256) y anotar los hashes en la incidencia; (7) guardar copias fuera del equipo en el almacén de evidencias. No se cambia nada en los sistemas.

**EX060 — Registro del problema.** *Observado:* hueco de PS-09 en el panel desde aproximadamente las 22:50 del 9 de octubre; todos los números de secuencia presentes; marcas de tiempo de la estación unos 422 s por detrás de la hora de recepción del retransmisor; el registro NTP del retransmisor no muestra ninguna petición de hora de PS-09 respondida desde el 7 de octubre. *Inferido:* PS-09 perdió su fuente de hora; los datos se archivaron en la ventana equivocada, no se perdieron. *Causa:* el cambio del cortafuegos CHG-131 del 7 de octubre sustituyó el conjunto de reglas del retransmisor a las estaciones y omitió udp/123. *Hecho:* udp/123 restablecido con CHG-135; desfase de PS-09 < 1 s en 30 min; el panel muestra datos; registros del historiador reindexados por hora de recepción para el periodo afectado (CHG-136). *Abierto:* por qué la revisión del cambio no detectó la omisión de NTP (lista de comprobación de revisión, capítulo 25) y por qué no saltó ninguna alerta por el desfase del reloj (nueva regla: desfase de estación > 30 s; monitorización de FSTS, antes del 20 de octubre).

### Capítulo 21: EX061–EX063

**EX061 — Repare la RACI.**

| Actividad | SOC | Guardia de FSTS | Responsable de seguridad de FSTS | Jefe de turno de Agua | Kell | Rol de cumplimiento designado por el operador |
|---|---|---|---|---|---|---|
| Detectar y hacer el triaje | R | C | A | I | — | — |
| Contener en el retransmisor | C | R | A | C | I | — |
| Deshabilitar el acceso del proveedor | R | R | A | I | C | — |
| Decidir la respuesta operativa (confianza en la telemetría, lecturas manuales) | I | C | C | A/R | — | I |
| Notificar a los reguladores si es obligatorio | — | — | C | C | — | A/R |
| Restablecer el servicio | I | R | A | C | C | I |

Cada fila tiene exactamente una A. La decisión operativa corresponde a Agua, y la notificación regulatoria al rol designado del operador, nunca a FSTS.

**EX062 — Defina un desencadenante.** Se declara «telemetría no fiable» cuando se cumple cualquiera de estas condiciones: (1) un cambio no autorizado confirmado en cualquier retransmisor (un hallazgo de integridad o de deriva que ningún registro de cambio explica en 30 minutos); (2) fallos de MAC de tres o más estaciones en 15 minutos; (3) un fallo de la comprobación de integridad del retransmisor o evidencia de su compromiso. Los fallos de MAC o el silencio de una sola estación *no* lo activan (se tratan con el manual de operación de la regla C). Lo declaran conjuntamente el responsable de seguridad de FSTS y el jefe de turno de Agua; Agua pasa las estaciones afectadas a lecturas manuales y aumenta el muestreo de la calidad del agua. Se da por terminado conjuntamente cuando se verifica que los retransmisores están limpios (reconstrucción o integridad confirmada con una línea base fuera del equipo) y las lecturas coinciden con las muestras manuales.

**EX063 — Preguntas al proveedor.** (1) ¿Cómo notifican a los clientes las vulnerabilidades del firmware de Kell R2 y con qué rapidez? → rutina de vulnerabilidades (capítulo 16). (2) ¿Cómo se protegen las credenciales de su personal y cómo se revocan cuando alguien se marcha? → acceso (capítulo 7). (3) ¿Cuál es su compromiso de notificarnos los incidentes que afecten a sus sistemas de asistencia remota? → integración e incidentes (este capítulo). (4) ¿Están firmadas las imágenes de firmware y cómo las verificamos? → despliegue (capítulo 27). (5) ¿Cuáles son las fechas de fin de soporte de cada modelo que usamos? → inventario (capítulo 11). (6) ¿Pueden facilitar una SBOM del firmware de la RTU ([CISA SBOM](https://www.cisa.gov/sbom))? → aplicabilidad de las vulnerabilidades (capítulo 16).

<a id="glossary"></a>

## Glosario

- **Criterios de aceptación**: condiciones comprobables, que producen evidencia, que definen cuándo está terminado un elemento de trabajo (capítulo 25).
- **Revisión de accesos**: comparación periódica de las cuentas de un sistema con una plantilla de referencia autorizada y con una declaración de necesidad (capítulo 7).
- **Lista de permitidos**: lista de lo que está permitido; todo lo que no figura en ella se rechaza (capítulos 3 y 15).
- **Línea base (de configuración)**: la configuración aprobada para una clase de sistema, guardada en control de versiones (capítulo 14).
- **Línea base (de integridad de archivos)**: hashes y permisos de los archivos importantes registrados en un momento en que se sabe que eran correctos (capítulo 6).
- **Revisión sin culpables**: revisión de un fallo que busca condiciones que cambiar en lugar de personas a las que culpar (capítulo 25).
- **Canario**: un primer despliegue limitado que se compara con equipos que siguen en la versión anterior antes de un despliegue más amplio (capítulo 27).
- **Regla de afirmación**: criterio, fijado antes de las pruebas, para declarar eficaz un control (capítulo 23).
- **Control compensatorio**: control temporal o alternativo que se usa cuando todavía no es posible la corrección normal (capítulos 11 y 16).
- **Conducto**: vía de comunicación declarada y justificada entre dos zonas (capítulo 2).
- **Franja de consecuencia**: juicio sobre lo grave que sería para las personas el resultado de un escenario, medido en personas y tiempo (capítulo 13).
- **Registro de flujos de datos**: registro de qué datos circulan entre sistemas, con su clase, su protección y su conservación (capítulo 12).
- **Defensa en profundidad**: varios controles independientes para que un solo fallo no conduzca directamente al daño (capítulo 8).
- **Modo degradado**: forma diseñada deliberadamente para que un servicio funcione con un componente no disponible (capítulo 8).
- **Sentido de la confianza**: en LANTERN, la propiedad de que los datos fluyen hacia arriba desde las estaciones y las órdenes nunca fluyen hacia abajo a través del servicio (capítulo 8).
- **Desviación**: diferencia entre la configuración real de un equipo y su estado deseado (capítulo 22).
- **Episodio (de alertas)**: grupo de eventos relacionados que se comunica como una sola alerta con un recuento (capítulo 19).
- **Exposición**: si una amenaza puede realmente alcanzar una vulnerabilidad (capítulo 5).
- **Margen de capacidad**: capacidad sobrante entre la carga máxima normal y el punto de degradación (capítulo 1).
- **HMAC**: código de autenticación de mensajes construido a partir de una función hash y una clave secreta ([RFC 2104](https://www.rfc-editor.org/rfc/rfc2104)) (capítulo 15).
- **Normalización**: conversión de los registros de distintas fuentes a una estructura de registro común (capítulo 17).
- **Cuarentena**: apartar para su revisión una entrada interpretable pero inverosímil, en lugar de rechazarla o aceptarla (capítulo 3).
- **RACI**: *Responsible, Accountable, Consulted, Informed* (responsable, rinde cuentas, consultado, informado): una matriz de responsabilidades con un único rol que rinde cuentas por actividad (capítulo 21).
- **Reproducción**: reenvío de un mensaje válido capturado previamente (capítulo 15).
- **RPO / RTO**: objetivo de punto de recuperación (pérdida de datos tolerable) y objetivo de tiempo de recuperación (tiempo para restablecer el servicio) (capítulo 16).
- **Reglas de enfrentamiento**: condiciones firmadas de una prueba: alcance, acciones, ventana, comunicación y condiciones de parada (capítulo 23).
- **Manual de operación (*runbook*)**: procedimiento paso a paso escrito para un colega competente que trabaja bajo presión de tiempo (capítulo 26).
- **Escenario (de riesgo)**: relato concreto de la causa, la vía, el activo, la consecuencia y los controles existentes (capítulo 13).
- **Intervalo de Wilson**: intervalo de confianza para una proporción que se comporta bien con muestras pequeñas (capítulo 9).
- **Zona**: grupo de sistemas con una confianza y una función similares (capítulo 2).

<a id="references"></a>

## Referencias

Las leyes, las orientaciones y las páginas públicas cambian. Las versiones y fechas que siguen son las consultadas para este borrador (octubre de 2026); vuelva a verificarlas antes de basarse en ellas. Una cita respalda la afirmación general que la acompaña en el texto, nunca los detalles del caso sintético. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

### Estándares, orientaciones y derecho

- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Secure by Design](https://www.cisa.gov/securebydesign).
- Cybersecurity and Infrastructure Security Agency. [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom).
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Official Journal, 4 May 2016.
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final).
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final).
- National Institute of Standards and Technology. [SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final).
- National Institute of Standards and Technology. [SP 800-40 Rev. 4, Guide to Enterprise Patch Management Planning](https://csrc.nist.gov/pubs/sp/800/40/r4/final).
- National Institute of Standards and Technology. [SP 800-41 Rev. 1, Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final).
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- National Institute of Standards and Technology. [SP 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- National Institute of Standards and Technology. [SP 800-92, Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final).
- National Institute of Standards and Technology. [SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final).
- National Institute of Standards and Technology. [SP 800-123, Guide to General Server Security](https://csrc.nist.gov/pubs/sp/800/123/final).
- National Institute of Standards and Technology. [SP 800-125, Guide to Security for Full Virtualization Technologies](https://csrc.nist.gov/pubs/sp/800/125/final).
- National Institute of Standards and Technology. [SP 800-128, Guide for Security-Focused Configuration Management of Information Systems](https://csrc.nist.gov/pubs/sp/800/128/upd1/final).
- National Institute of Standards and Technology. [SP 800-137, Information Security Continuous Monitoring (ISCM)](https://csrc.nist.gov/pubs/sp/800/137/final).
- National Institute of Standards and Technology. [SP 800-184, Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final).
- National Institute of Standards and Technology. [SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://doi.org/10.6028/NIST.CSWP.29). February 2024.
- National Institute of Standards and Technology. [NIST Privacy Framework](https://www.nist.gov/privacy-framework).
- OWASP Foundation. [Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html).

### Protocolos y documentación de software

- Gerhards, R. [RFC 5424: The Syslog Protocol](https://www.rfc-editor.org/rfc/rfc5424). IETF, 2009.
- Klyne, G., and Newman, C. [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339). IETF, 2002.
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, 1997.
- Mills, D., Martin, J., Burbank, J., and Kasch, W. [RFC 5905: Network Time Protocol Version 4](https://www.rfc-editor.org/rfc/rfc5905). IETF, 2010.
- Python Software Foundation. [hmac — Keyed-Hashing for Message Authentication](https://docs.python.org/3/library/hmac.html) and [sqlite3 — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html). Python 3 documentation.
- Rekhter, Y., et al. [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918). IETF, 1996.
- Arkko, J., Cotton, M., and Vegoda, L. [RFC 5737: IPv4 Address Blocks Reserved for Documentation](https://www.rfc-editor.org/rfc/rfc5737). IETF, 2010.
- Rescorla, E. [RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446). IETF, 2018.

### Incidentes, operaciones y métodos

- Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. (eds.). [Site Reliability Engineering, Chapter 15: Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/). O'Reilly / Google, 2016.
- Beyer, B., Murphy, N. R., Rensin, D. K., Kawahara, K., and Thorne, S. (eds.). [The Site Reliability Workbook, Chapter 16: Canarying Releases](https://sre.google/workbook/canarying-releases/). O'Reilly / Google, 2018.
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *Proceedings of the National Academy of Sciences*, 115(11), 2600–2606, 2018.
- Reason, J. [Human Error: Models and Management](https://doi.org/10.1136/bmj.320.7237.768). *BMJ*, 320, 768–770, 2000.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems Magazine*, 21(6), 11–25, 2001.
- Saltzer, J. H., and Schroeder, M. D. [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939). *Proceedings of the IEEE*, 63(9), 1278–1308, 1975.
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.
- Wilson, E. B. [Probable Inference, the Law of Succession, and Statistical Inference](https://doi.org/10.1080/01621459.1927.10502953). *Journal of the American Statistical Association*, 22(158), 209–212, 1927.
