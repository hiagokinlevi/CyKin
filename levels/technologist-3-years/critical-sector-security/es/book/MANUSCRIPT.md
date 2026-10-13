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

[← Capítulo 04](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 →](../../en/book/MANUSCRIPT.md#ch-06)

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
