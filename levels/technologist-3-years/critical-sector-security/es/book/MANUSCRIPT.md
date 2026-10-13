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
2. [Redes y servicios de internet](../../en/book/MANUSCRIPT.md#ch-02): zonas, conductos, servicios y cómo comprobar lo que realmente transporta la red.
3. [Fundamentos de programación](../../en/book/MANUSCRIPT.md#ch-03): escribir herramientas pequeñas, correctas y comprobables; validar las entradas no fiables.
4. [Modelos de datos](../../en/book/MANUSCRIPT.md#ch-04): inventarios, esquemas y restricciones que hacen fiables los datos operativos.
5. [Cultura de seguridad](../../en/book/MANUSCRIPT.md#ch-05): el vocabulario de las amenazas, los controles y la evidencia para un servicio esencial.
6. [Sistemas operativos y virtualización](../../en/book/MANUSCRIPT.md#ch-06): bastionado, servicios, integridad de archivos y plataformas virtuales.
7. [Fundamentos de identidad y acceso](../../en/book/MANUSCRIPT.md#ch-07): cuentas, autenticación, privilegios y revisión de accesos.
8. [Fundamentos de arquitectura de seguridad](../../en/book/MANUSCRIPT.md#ch-08): zonas y conductos, defensa en profundidad y diseño para la operabilidad.
9. [Evidencia y medición](../../en/book/MANUSCRIPT.md#ch-09): métricas que dicen la verdad, denominadores y honestidad con muestras pequeñas.
10. [Infraestructura crítica y seguridad sectorial: orientación](../../en/book/MANUSCRIPT.md#ch-10): qué hace crítico un servicio y en qué se diferencian los sectores.
11. [Infraestructura crítica y seguridad sectorial: activos y contexto](../../en/book/MANUSCRIPT.md#ch-11): inventario, titularidad, dependencias y estado del soporte.
12. [Infraestructura crítica y seguridad sectorial: flujos de datos](../../en/book/MANUSCRIPT.md#ch-12): registros de flujos, clasificación, conservación y verificación.
13. [Infraestructura crítica y seguridad sectorial: escenarios de riesgo](../../en/book/MANUSCRIPT.md#ch-13): redactar escenarios y ordenarlos por su consecuencia.
14. [Infraestructura crítica y seguridad sectorial: métodos I](../../en/book/MANUSCRIPT.md#ch-14): líneas base, bastionado y control de cambios como métodos diarios.
15. [Infraestructura crítica y seguridad sectorial: laboratorio guiado](../../en/book/MANUSCRIPT.md#ch-15): construir el retransmisor autenticado con protección frente a la reproducción.
16. [Infraestructura crítica y seguridad sectorial: métodos II](../../en/book/MANUSCRIPT.md#ch-16): gestión de vulnerabilidades y parches, copias de seguridad y recuperación.
17. [Infraestructura crítica y seguridad sectorial: herramientas](../../en/book/MANUSCRIPT.md#ch-17): registro, hora, normalización y construcción de una herramienta en la que se pueda confiar.
18. [Infraestructura crítica y seguridad sectorial: controles](../../en/book/MANUSCRIPT.md#ch-18): elegir, implantar y documentar controles con evidencia.
19. [Infraestructura crítica y seguridad sectorial: monitorización](../../en/book/MANUSCRIPT.md#ch-19): reglas de detección, la ausencia como señal y la calidad de las alertas.
20. [Infraestructura crítica y seguridad sectorial: resolución de problemas](../../en/book/MANUSCRIPT.md#ch-20): un método para fallos que pueden ser ataques o no.
21. [Infraestructura crítica y seguridad sectorial: integración del servicio](../../en/book/MANUSCRIPT.md#ch-21): integrarse con operadores, proveedores, el SOC y los planes de emergencia.
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

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](../../en/book/MANUSCRIPT.md#ch-02)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resultados resueltos y notas de evaluación

Cada resultado resuelto muestra una respuesta defendible y explica lo que premia la rúbrica. Una respuesta distinta puede obtener la máxima puntuación cuando cumple el mismo nivel de exigencia en cuanto a evidencia, alcance y honestidad sobre los límites. Los resultados numéricos proceden de los laboratorios sin conexión de este libro, ejecutados con Python 3.13.5 y solo con la biblioteca estándar; si su salida difiere, compruebe primero la versión de Python y si ha cambiado los datos sintéticos. Todas las cifras describen datos sintéticos; no las presente nunca como hallazgos sobre operadores reales.

### Capítulo 1: EX001–EX003

**EX001 — Plazo de suministro frente a tiempo de aviso.** Espacio libre necesario cuando se presenta la solicitud = (30 días de plazo + 7 días de margen) × 1,91 GB/día ≈ 70,7 GB. Presente la solicitud cuando el espacio usado llegue a unos 200 − 70,7 ≈ 129 GB, es decir, con el disco lleno en torno al 65 %. RLY-01 está en 120,9 GB y llegará a 129 GB en unos (129,3 − 120,9) / 1,91 ≈ 4,4 días. La alarma del 85 % salta cuando solo quedan unos 15,7 días de crecimiento antes de llenarse (la mitad del plazo de adquisición), así que llega demasiado tarde como *desencadenante de la compra*; manténgala como alarma operativa y añada un umbral del 65 % para «presentar la solicitud de capacidad». La máxima puntuación señala además que corregir la conservación (EX002) puede hacer innecesaria la compra.

**EX002 — Explique el crecimiento.** 120,9 GB ÷ 1,91 GB/día ≈ 63 días de datos, más del doble de los 30 días de conservación. *Observado:* uso del disco y ritmo de crecimiento. *Inferido:* se están conservando datos de más de 30 días. Causas plausibles: (a) la rotación de registros se ejecuta pero no se borran los archivos antiguos (número de rotaciones demasiado alto, o compresión sin borrado); (b) el búfer hacia el destino del retransmisor conservó mensajes durante un antiguo corte del historiador y nunca los purgó; (c) un segundo flujo de registros (de depuración o de auditoría) queda fuera de la política de rotación. Comprobaciones (de solo lectura): listar los archivos más antiguos por directorio y fecha de modificación; comparar la configuración de la rotación con la política; comprobar el tamaño del directorio del búfer y su entrada más antigua. *Abierto:* causa confirmada — E. Strand, antes del viernes.

**EX003 — Lista de comprobación de fallos silenciosos.** Filas de ejemplo: (1) disco que se llena — % usado y previsión de días hasta llenarse — aviso al 65 % / alarma al 85 % — guardia de plataforma — aumentar la capacidad o corregir la conservación; (2) rotación de registros detenida — antigüedad del archivo de registro activo más antiguo — > 2 días — guardia de plataforma — corregir la rotación; (3) caducidad de certificados — días hasta la caducidad de los certificados del retransmisor y del historiador — < 30 días — equipo de plataforma — renovarlos mediante un cambio estándar; (4) desviación del reloj — desfase respecto del NTP interno — aviso > 1 s, alarma > 2 s — guardia — comprobar la fuente de hora; (5) trabajo programado fallido — resultado del trabajo de copia de seguridad y antigüedad de la prueba de restauración — cualquier fallo, o prueba de restauración > 90 días — responsable del servicio — volver a ejecutarlo e investigar. La máxima puntuación exige umbrales medibles con tiempo de aviso y un lector designado.

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
