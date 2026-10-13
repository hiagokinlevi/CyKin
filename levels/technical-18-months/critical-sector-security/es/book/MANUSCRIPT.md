# Infraestructura crítica y seguridad sectorial: práctica técnica aplicada

- Idioma: español neutro (`es`); curso técnico, dieciocho meses; aproximadamente 1.200 horas de estudio planificado (curso 069 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–18 de 18 tienen texto didáctico escrito, quince laboratorios sin conexión, los ejercicios EX001–EX072 y sus resultados resueltos correspondientes. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: operadores técnicos (técnicos de redes y de sistemas, técnicos de SCADA y de telemetría, analistas de seguridad júnior de centros de operaciones) que ya conocen las redes, los sistemas operativos y la programación básica de scripts y que ahora trabajan en sistemas que mueven agua, electricidad o el aire que respiran los pacientes. Conocimientos de entrada: redes, sistemas operativos, scripts y práctica segura de laboratorio.
- En qué se diferencia este curso de sus vecinos. El [libro de tecnólogo](../../../../technologist-3-years/critical-sector-security/es/book/MANUSCRIPT.md) enseña a los implantadores a construir, operar y traspasar un servicio supervisado completo. Los cursos [profesional](../../../../professional-6-months/critical-sector-security/en/book/MANUSCRIPT.md) y [rápido](../../../../rapid-1-month/critical-sector-security/en/book/MANUSCRIPT.md) se ocupan de las decisiones de gestión y de una primera introducción. **Este libro técnico trata de la profundidad técnica práctica**: abrir los paquetes de los protocolos industriales, auditar y bastionar equipos, configurar y verificar los cortafuegos de los conductos, detectar modos de fallo y órdenes no autorizadas, diagnosticar averías descartando hipótesis y producir evidencia que otro técnico pueda comprobar. Cada capítulo pregunta: *¿qué escribiría, leería, cambiaría o probaría exactamente, y cómo lo demostraría?*
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos y no se relicencian aquí.
- Límite educativo: este curso es un proyecto educativo independiente. No es un programa acreditado, no otorga ninguna titulación y no concede autorización para acceder, escanear, probar o modificar ninguna infraestructura, operador, dispositivo, conjunto de datos o persona reales. Toda organización, lugar, persona, dirección, registro, trama, valor y resultado numérico de un ejemplo resuelto o de un laboratorio es **sintético**, salvo que una frase cite explícitamente una fuente pública. Las direcciones IP proceden de rangos privados ([RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)) o de rangos de documentación ([RFC 5737](https://www.rfc-editor.org/rfc/rfc5737)). Nada de lo que aparece en este libro es un procedimiento operativo para una empresa de servicios, un hospital o una red eléctrica reales, y nada constituye asesoramiento jurídico, clínico o regulatorio.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los dieciocho capítulos siguen a un responsable técnico durante dieciocho meses en un centro regional de operaciones. El resultado del curso es práctico: **diagnosticar fallos, configurar controles y verificar resultados** en infraestructuras críticas, en un laboratorio reproducible y bajo supervisión.

- **Etapa 1 (capítulos 1–6)**: arquitectura del servicio y presupuestos de sondeo, decodificación de Modbus/TCP, auditoría de equipos y cuentas, análisis estricto de datos, alcance técnico y evidencia, y el modelo de sistema de zonas y conductos.
- **Etapa 2 (capítulos 7–12)**: telemetría y tiempo, modos de fallo, herramientas y comprobación de la capa de enlace de DNP3, configuración de cortafuegos, verificación mediante pruebas trazables y el primer laboratorio contenido (un respondedor Modbus con una política de escritura).
- **Etapa 3 (capítulos 13–18)**: diagnóstico guiado por hipótesis, automatización de la detección de derivas, análisis de dependencias, documentación técnica y seguridad física, el segundo laboratorio contenido (una cadena de detección) y un proyecto supervisado con un paquete de evidencia sellado.

Cada capítulo tiene resultados de aprendizaje, secciones didácticas con definiciones, un ejemplo resuelto, una actividad práctica, errores comunes y límites, cuatro ejercicios numerados y una síntesis. Quince capítulos contienen un laboratorio de Python. Los laboratorios usan solo la biblioteca estándar de Python 3 (las salidas de este borrador se produjeron con Python 3.13.5); no necesitan red, paquetes, privilegios ni datos reales, y cada salida se imprime en el texto para que pueda comprobar su ejecución. El Lab 12 usa `socket.socketpair()`, que conecta dos sockets dentro de un mismo proceso y no puede alcanzar ninguna red. Los laboratorios que escriben archivos lo hacen solo dentro de un directorio temporal que crean y eliminan. Escriba su respuesta a cada ejercicio antes de abrir los [resultados resueltos](#worked-results); la rúbrica de 0–3 muestra lo que premia un evaluador, y una respuesta distinta pero defendible puede obtener la máxima puntuación.

Mantenga cuatro etiquetas en toda nota de trabajo: **observado** (lo que una herramienta o una persona identificada registró, con hora UTC y fuente), **inferido** (lo que usted concluye y por qué), **hecho** (lo que cambió y con qué registro de cambio) y **abierto** (lo que aún se desconoce y quién es su responsable).

### El escenario sintético de este libro

| Elemento sintético | Papel en el libro | Límite |
|---|---|---|
| **Kestrel Vale**: una región ficticia | Escenario de todos los ejemplos. | Lugar inventado. |
| **Kestrel Vale Regional Operations Centre (KVROC)** | Opera los sistemas de supervisión de tres operadores. El lector es un **responsable técnico**; L. Ferreira es la responsable de seguridad; J. Tan y R. Kaur son colegas. | Inventado; ninguna organización ni persona real. |
| **Kestrel Water**: estaciones KW-01 a KW-12 (RTU en 10.10.*n*.2), A. Mensah, director de operaciones | Fuente principal de los ejemplos de Modbus/TCP. | Inventado. |
| Subestación **SS-3** de **Kestrel Grid** (dirección de estación remota DNP3 10; dirección de maestra 1; procesador de comunicaciones fep-01) | Ejemplos de DNP3. | Inventado. |
| Sistema de gestión del edificio del **Kestrel General Hospital** | Ejemplos de dependencias sanitarias. | Inventado. |
| Equipos scada-01, eng-ws-15, hmi-02, hist-02, jump-01, fw-01, ntp-ops, ad-ops, esx-02/03 y toda trama, línea de registro, valor y hora | Contexto de los laboratorios y ejercicios. | Inventado. |

Como los datos son sintéticos, el libro puede decirle lo que un técnico real rara vez sabe con certeza. Úselo para aprender cómo fallan las comprobaciones, nunca como evidencia sobre organizaciones reales.

### Política de fuentes

Toda afirmación factual sobre un protocolo, una norma, un incidente público o una orientación publicada enlaza con una fuente consultada en octubre de 2026. Las normas y las orientaciones cambian: vuelva a verificar cada una antes de basarse en ella. Al vocabulario profesional corriente no se le asigna una referencia inventada. Una cita respalda la afirmación general que la acompaña, nunca los detalles sintéticos. Los incidentes públicos se describen solo al nivel en que sus editores los publicaron, y nunca como técnica.

### Reglas de seguridad para el trabajo práctico

1. Practique solo en los laboratorios del libro, en equipos de su propiedad o en sistemas cuyo propietario le haya dado un permiso **por escrito y específico** que nombre los sistemas, las acciones y la ventana (capítulo 5).
2. No conecte nunca un escáner, un portátil de pruebas o un script a una red de control en servicio sin ese permiso y sin el acuerdo de las personas responsables del proceso físico. En la tecnología operacional, una lectura puede ser una acción.
3. No toque nunca los sistemas de protección o de seguridad funcional como parte de un trabajo de ciberseguridad (capítulo 16).
4. Si observa una debilidad en un sistema real, deténgase, registre lo que vio y comuníquelo en privado a su propietario o mediante divulgación coordinada. No la «confirme».
5. Mantenga los secretos fuera de las notas, las incidencias y las capturas de pantalla.

## Contenido

1. [Arquitectura informática y del servicio](#ch-01): capas, tres rutas y el presupuesto del ciclo de sondeo.
2. [Redes y protocolos](#ch-02): protocolos industriales sin autenticación y decodificación de Modbus/TCP.
3. [Sistemas operativos e identidades](#ch-03): configuración efectiva de SSH, UID, cuentas de servicio y grupos.
4. [Scripts y formatos de datos](#ch-04): análisis estricto de CSV/JSON, orden de validación y coordenadas del registro.
5. [Alcance de seguridad y evidencia](#ch-05): alcance técnico, primero lo pasivo, evidencia verificable.
6. [Infraestructura crítica y seguridad sectorial: modelo del sistema](#ch-06): zonas, conductos y diferencias entre sectores.
7. [Infraestructura crítica y seguridad sectorial: datos y telemetría](#ch-07): syslog, relojes y cronologías en UTC.
8. [Infraestructura crítica y seguridad sectorial: modos de fallo](#ch-08): lagunas, valores congelados, picos y reglas explicables.
9. [Infraestructura crítica y seguridad sectorial: herramientas y métodos](#ch-09): elección del método, validación de herramientas y el CRC de DNP3.
10. [Infraestructura crítica y seguridad sectorial: configuración de controles](../../en/book/MANUSCRIPT.md#ch-10): políticas de primera coincidencia, sombreado y acceso de proveedores.
11. [Infraestructura crítica y seguridad sectorial: verificación](../../en/book/MANUSCRIPT.md#ch-11): pruebas positivas y negativas trazables.
12. [Laboratorio contenido I](../../en/book/MANUSCRIPT.md#ch-12): un respondedor Modbus con una política de escritura y respuestas de excepción.
13. [Infraestructura crítica y seguridad sectorial: diagnóstico de averías](../../en/book/MANUSCRIPT.md#ch-13): hipótesis, predicciones, descarte y escalado.
14. [Infraestructura crítica y seguridad sectorial: automatización](../../en/book/MANUSCRIPT.md#ch-14): detección de derivas basada en hashes y automatización segura.
15. [Infraestructura crítica y seguridad sectorial: integración y dependencias](../../en/book/MANUSCRIPT.md#ch-15): grafos de dependencias y puntos de integración en las fronteras.
16. [Documentación técnica y seguridad física](../../en/book/MANUSCRIPT.md#ch-16): documentos ejecutables, autoridad de seguridad física y dispositivos transitorios.
17. [Laboratorio contenido II](../../en/book/MANUSCRIPT.md#ch-17): una cadena de detección integrada y que se supervisa a sí misma.
18. [Proyecto técnico supervisado](../../en/book/MANUSCRIPT.md#ch-18): fases del proyecto y un paquete de evidencia sellado.

Apéndices: [Resultados resueltos y notas de evaluación](#worked-results) · [Glosario](#glossary) · [Referencias](#references).

<a id="ch-01"></a>

## Capítulo 1 — Arquitectura informática y del servicio

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- dibujar la arquitectura técnica de un servicio de control supervisor (dispositivos de campo, enlaces de comunicación, procesadores de comunicaciones y servidores SCADA, historiador, HMI, estación de ingeniería, plano de gestión) e indicar qué hace cada componente;
- distinguir la **ruta de control**, la **ruta de supervisión** y la **ruta de gestión**, y explicar por qué un técnico protege cada una de forma distinta;
- calcular un **presupuesto del ciclo de sondeo** y usarlo para predecir qué efecto tiene un enlace lento o caído sobre la frescura de los datos del operador;
- identificar los componentes compartidos de la plataforma (servidores de virtualización, directorio, hora, almacenamiento) cuyo fallo atraviesa las fronteras entre servicios.

Este es el primer capítulo de un curso práctico. Todo lo posterior (decodificación de protocolos, bastionado, detección, diagnóstico de averías) supone que usted puede señalar una caja del diagrama y decir qué tráfico envía, qué almacena y qué se rompe si se detiene. Se dan por sabidos los conocimientos de entrada (redes, sistemas operativos, scripts); el elemento nuevo es el proceso físico que hay al otro extremo del cable.

### 1.1 Las capas de un servicio de control supervisor

La mayoría de los servicios de sectores críticos que mueven agua, electricidad, aire o personas comparten una forma en capas reconocible. La guía del NIST sobre tecnología operacional describe los mismos componentes en términos generales ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); los nombres siguientes son los que usa este libro.

- **Dispositivos de campo**: sensores (nivel, caudal, cloro, presión, temperatura, corriente), actuadores (bombas, válvulas, interruptores) y los controladores que los conectan: **PLC** (controladores lógicos programables) que ejecutan la lógica local y **RTU** (unidades terminales remotas) diseñadas para emplazamientos remotos con comunicaciones limitadas.
- **Enlaces de comunicación**: fibra, radio con licencia, routers celulares, líneas dedicadas o la red MPLS de un operador. Su latencia, sus pérdidas y su coste condicionan todo lo que hay por encima.
- **Procesador de comunicaciones (FEP) o servidor SCADA**: sondea los dispositivos de campo, aplica escalados y alarmas y mantiene el estado actual del proceso.
- **Historiador**: almacena series temporales para informes, investigaciones y registros reglamentarios.
- **HMI** (interfaz hombre-máquina): las pantallas del operador, desde las que se emiten órdenes como «arrancar la bomba 2».
- **Estación de ingeniería**: guarda los proyectos de los controladores y las herramientas del fabricante que cambian su lógica; es el ordenador más poderoso de todo el sistema.
- **Plano de gestión**: servidores de salto, servicios de directorio, servidores de hora, copias de seguridad, gestión de la virtualización y el colector de supervisión.

### 1.2 Tres rutas, tres problemas de protección

Un técnico debe ser capaz de trazar tres rutas distintas en el diagrama. La **ruta de control** lleva las órdenes al proceso: HMI → servidor SCADA → enlace → controlador → actuador. La integridad y la disponibilidad de esta ruta son lo que mantiene a salvo a las personas; una escritura no autorizada o corrompida en ella es el peor caso de este libro. La **ruta de supervisión** trae de vuelta las mediciones: sensor → controlador → enlace → servidor SCADA → historiador y HMI. Si es errónea, los operadores actúan sobre información falsa, un fallo que puede ser tan peligroso como una orden incorrecta y más difícil de advertir.

La **ruta de gestión** cambia el propio sistema: un ingeniero que descarga lógica nueva, un administrador que aplica parches al historiador, un proveedor que se conecta para diagnosticar una avería. Se usa poco, pero concentra los mayores privilegios, y es por donde, según los informes, ha comenzado la mayoría de las intrusiones reales en entornos de control; la alerta de CISA sobre los ataques de diciembre de 2015 contra empresas de distribución ucranianas describe el acceso remoto y el uso de credenciales que precedieron al impacto operativo ([CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01)).

Las tres rutas comparten a menudo cables, conmutadores y servidores. Dibujarlas por separado es la manera de descubrir que un portátil «de supervisión» conectado al conmutador del centro de control también puede alcanzar los puertos de programación de los controladores.

### 1.3 Sondeo y frescura

La mayoría de los protocolos de estación de este libro son de **petición-respuesta**: el servidor SCADA pregunta y el dispositivo contesta. El tiempo necesario para refrescar una vez cada estación es el **ciclo de sondeo**. Para cada estación es aproximadamente *sondeos por ciclo × (tiempo de ida y vuelta del enlace + tiempo de respuesta del dispositivo)*. Si el servidor sondea las estaciones una tras otra por un único canal, el ciclo es la **suma** de las estaciones; si dispone de un canal independiente por estación, el ciclo lo fija la estación **más lenta**.

Para el trabajo de seguridad importan dos consecuencias. Primera: un enlace lento (un router celular congestionado, un trayecto de radio degradado) alarga el ciclo de todas las estaciones sondeadas después. Segunda: un dispositivo que no responde cuesta el **tiempo de espera** completo en cada sondeo, de modo que una estación caída puede alargar el ciclo más que una lenta. Los requisitos de frescura («cada estación refrescada al menos cada 5 s») dependen por tanto de los tiempos de espera y del número de reintentos, además de la velocidad del enlace, y un control de seguridad que añade latencia (una VPN, un proxy de inspección) debe contrastarse con este presupuesto antes de instalarse.

### 1.4 Plataformas compartidas

Los centros de control modernos ejecutan sus servidores SCADA, historiadores y directorio en servidores de virtualización, a menudo compartidos entre servicios. Un hipervisor, un directorio, una fuente de hora o una cabina de almacenamiento compartidos son un punto en el que un fallo de un sector se convierte en un fallo de varios. El Lab 15 del capítulo 15 traza estas dependencias con código; aquí, basta con aprender a marcar en el diagrama cada componente compartido con los servicios que dependen de él. En el KVROC, el servidor esx-02 ejecuta el servidor SCADA, el historiador y el servidor del BMS del hospital, de modo que una caída o un parche defectuoso pueden afectar a la vez a la supervisión del agua y a la sanitaria. Marque cada componente compartido con todos los servicios que dependen de él y pregunte quién es el responsable del servidor cuando esos servicios discrepan sobre una ventana de cambio.

### 1.5 Ejemplo resuelto: el centro de operaciones de Kestrel Vale (sintético)

Usted es responsable técnico en el **Kestrel Vale Regional Operations Centre (KVROC)**, que opera los sistemas de supervisión de **Kestrel Water** (12 estaciones, KW-01 a KW-12), la supervisión de los sistemas de gestión del edificio del **Kestrel General Hospital** y el procesador de telecontrol de una subestación (**SS-3**) de **Kestrel Grid**. Las RTU de las estaciones están en 10.10.0.0/16 (KW-*n* es 10.10.*n*.2); el centro de control es 10.20.0.0/24 (servidor SCADA `scada-01` 10.20.0.10, estación de ingeniería `eng-ws-15` 10.20.0.15, historiador `hist-02` 10.20.0.21); los puestos corporativos están en 10.30.0.0/16; la red de gestión es 10.90.0.0/24 (servidor de salto `jump-01` 10.90.0.20). Todos los nombres y direcciones son ficticios.

Operaciones exige que cada estación se refresque en menos de 5 segundos. `scada-01` sondea las doce estaciones por un único canal. El Lab 1 calcula el presupuesto.

**Lab 1** (guárdelo como `lab01.py` y ejecútelo con `python3 lab01.py`):

```python
# Lab 1 - poll-cycle budget for a SCADA server polling stations (offline, standard library only)
# Synthetic Kestrel Water figures. Each poll = request + response over the link plus device turnaround.
stations = {  # name: (link, round-trip ms on the link, device turnaround ms, polls per cycle)
 "KW-01": ("fibre", 4, 20, 3), "KW-02": ("fibre", 4, 20, 3), "KW-03": ("fibre", 5, 25, 3),
 "KW-04": ("cellular", 180, 40, 4), "KW-05": ("cellular", 210, 40, 4), "KW-06": ("cellular", 650, 40, 4),
 "KW-07": ("radio", 420, 60, 3), "KW-08": ("radio", 460, 60, 3), "KW-09": ("cellular", 190, 40, 4),
 "KW-10": ("fibre", 4, 20, 3), "KW-11": ("radio", 440, 60, 3), "KW-12": ("cellular", 200, 40, 4),
}
REQUIRED_S = 5.0          # operations require every station refreshed at least every 5 s
TIMEOUT_MS = 1500         # a poll that gets no reply costs the full timeout
def cycle(stations, sequential=True, dead=()):
    per = {}
    for n, (link, rtt, turn, polls) in stations.items():
        per[n] = polls * (TIMEOUT_MS if n in dead else rtt + turn)
    return (sum(per.values()) if sequential else max(per.values())) / 1000, per
c, per = cycle(stations)
print(f"sequential cycle {c:.2f} s (requirement {REQUIRED_S} s) -> {'OK' if c <= REQUIRED_S else 'FAILS'}")
worst = max(per, key=per.get); print(f"slowest station {worst}: {per[worst] / 1000:.2f} s per cycle")
c2, _ = cycle(stations, dead={"KW-06"})
print(f"sequential with KW-06 not answering: {c2:.2f} s")
c3, _ = cycle(stations, sequential=False, dead={"KW-06"})
print(f"one polling channel per station, KW-06 dead: {c3:.2f} s")
```

Salida esperada (Python 3.13.5):

```text
sequential cycle 11.33 s (requirement 5.0 s) -> FAILS
slowest station KW-06: 2.76 s per cycle
sequential with KW-06 not answering: 14.57 s
one polling channel per station, KW-06 dead: 6.00 s
```

El resultado indica que el requisito ya se incumple (11,33 s), sobre todo por las estaciones celulares y de radio, y que KW-06 es la más lenta. Una KW-06 caída añade otros 3,24 s, porque cada sondeo sin respuesta cuesta 1,5 s. Incluso con un canal por estación, el ciclo es de 6,00 s mientras KW-06 está caída: los canales por estación eliminan el problema de la *suma*, pero no el del *tiempo de espera*. Un técnico al que se le pide «añadir un túnel cifrado a las estaciones celulares» sabe ahora qué preguntar primero: ¿cuántos milisegundos añade por sondeo y qué efecto tiene eso sobre un ciclo que ya falla?

### 1.6 Actividad práctica: dibuje su propio diagrama de tres rutas

A partir de la descripción del KVROC, dibuje las rutas de control, supervisión y gestión en tres colores. Marque cada componente que aparezca en más de una ruta y cada componente compartido de la plataforma. Conserve el dibujo: los capítulos 6, 10 y 15 lo irán refinando. Use tres colores o tres capas de página para que un conmutador o un servidor de salto compartido salte a la vista. Compruebe después si eng-ws-15 aparece tanto en la ruta de gestión como en la de control: si es así, comprometer esa estación de trabajo permite alcanzar todas las estaciones. Guarde el dibujo junto con el presupuesto del Lab 1, porque cualquier propuesta posterior de túnel o de cifrado tendrá que juzgarse frente a las rutas y frente al ciclo de sondeo.

### 1.7 Errores comunes y límites

- Dibujar solo la red y olvidar la ruta de gestión, que es donde residen los privilegios.
- Tratar el historiador como «simple TI»; a menudo es el puente entre las redes de control y corporativa.
- Medir la velocidad del enlace, pero no los tiempos de espera ni los reintentos; los dispositivos caídos dominan los ciclos de sondeo.
- Suponer que una arquitectura en paralelo resuelve la frescura; cambia la aritmética, no el tiempo de espera.
- El modelo del Lab 1 ignora los reintentos, la contención en las líneas serie y la sobrecarga del protocolo; trate sus cifras como una primera estimación y después mida.

- Olvidar que una estación caída cuesta el tiempo de espera completo en cada sondeo, de modo que una sola RTU que no responde puede alargar el ciclo más que una lenta.
- Dibujar las rutas de control y de supervisión y dejar fuera el servidor de salto, el directorio y el servidor de hora.
- Tratar las cifras del Lab 1 como valores medidos en lugar de como una primera estimación que aún requiere comprobar en la instalación los reintentos y la sobrecarga del protocolo.

### Ejercicios — capítulo 1

**EX001 — Clasificación de rutas.** *Objetivo:* separar las tres rutas. *Entradas:* estos flujos: HMI → scada-01 «arrancar la bomba 2»; RTU de KW-04 → scada-01 lectura de nivel; eng-ws-15 → KW-04 descarga del proyecto; jump-01 → hist-02 SSH; hist-02 → servidor corporativo de informes exportación CSV. *Pasos:* clasifique cada uno como control, supervisión o gestión (o una combinación) e indique la peor consecuencia si un tercero no autorizado pudiera alterarlo. *Evidencia esperada:* una tabla de cinco filas. *Rúbrica:* 3 = clases correctas, con la descarga del proyecto reconocida como la acción de gestión más peligrosa y la exportación CSV reconocida como un flujo de supervisión entre zonas; 2 = una clasificación errónea; 1 = clases sin consecuencias; 0 = nada.

**EX002 — Corrija el ciclo sobre el papel.** *Objetivo:* usar el modelo del ciclo de sondeo. *Entradas:* el Lab 1. *Pasos:* proponga dos cambios que lleven el ciclo secuencial por debajo de 5 s con todas las estaciones en buen estado e indique cuál de ellos limita además el efecto de una estación caída. Modifique el laboratorio para probarlos. *Evidencia esperada:* los parámetros modificados y los nuevos tiempos de ciclo impresos. *Rúbrica:* 3 = cambios realistas (canales separados para los tipos de enlace lentos, menos sondeos por ciclo para las estaciones lentas, un tiempo de espera más corto con una política de reintentos justificada) y verificados ejecutando el laboratorio; 2 = correctos pero sin verificar; 1 = solo «comprar enlaces más rápidos»; 0 = nada.

**EX003 — Impacto del túnel.** *Objetivo:* contrastar un control de seguridad con un presupuesto operativo. *Entradas:* un túnel cifrado propuesto añade 35 ms a cada ida y vuelta en las cinco estaciones celulares. *Pasos:* calcule el efecto sobre el ciclo secuencial y sobre el diseño con un canal por estación. *Evidencia esperada:* aritmética y una recomendación. *Rúbrica:* 3 = aumentos correctos (5 estaciones × 4 sondeos × 35 ms = 0,70 s en secuencial; 0,14 s en el ciclo propio de la estación celular más lenta) y una recomendación que vincule el túnel al rediseño de canales; 2 = aritmética correcta, recomendación débil; 1 = solo cualitativo; 0 = nada.

**EX004 — Lista de plataformas compartidas.** *Objetivo:* encontrar dependencias entre servicios. *Entradas:* la descripción del KVROC y su diagrama. *Pasos:* enumere cuatro componentes que probablemente compartan los servicios de agua, hospital y red eléctrica y, para cada uno, la primera pregunta que haría a su responsable. *Evidencia esperada:* cuatro filas. *Rúbrica:* 3 = por ejemplo, servidores de virtualización, directorio, fuente de hora y colector de supervisión, cada uno con una pregunta específica (margen de capacidad, grupo de administración, redundancia de la fuente de hora, comportamiento cuando se llena); 2 = preguntas genéricas; 1 = solo componentes; 0 = nada.

### Síntesis del capítulo

Un servicio de un sector crítico es un conjunto de capas unidas por tres rutas. Las órdenes, las mediciones y los cambios viajan por caminos distintos y fallan de maneras distintas; la ruta de gestión concentra los mayores privilegios. El sondeo de petición-respuesta convierte la frescura en una cuestión de aritmética, y la suelen decidir los tiempos de espera, no el ancho de banda. Cada capítulo posterior añade una técnica a una de estas rutas, así que tenga a mano el diagrama y el presupuesto.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 18

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Redes y protocolos

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- explicar por qué la mayoría de los protocolos industriales no llevan autenticación y qué significa eso para cualquiera que pueda alcanzar el puerto de un controlador;
- decodificar una trama Modbus/TCP a mano y con código: cabecera MBAP, identificador de unidad, código de función, dirección y cantidad;
- distinguir las funciones de lectura de las de escritura y reconocer las funciones de diagnóstico y de identificación que merecen revisión;
- convertir un decodificador en una primera detección: escrituras desde cualquier equipo que no sea el origen de ingeniería autorizado.

El capítulo 1 dibujó las rutas. Este capítulo abre los paquetes de las rutas de control y de supervisión para que los capítulos posteriores puedan filtrarlos, verificarlos y detectarlos.

### 2.1 Protocolos industriales y confianza

Protocolos como Modbus y DNP3 se diseñaron para redes serie cerradas en las que se suponía que todo lo que había en el cable pertenecía a ellas. Sus versiones TCP/IP mantuvieron esa suposición: un dispositivo Modbus/TCP clásico acepta una escritura válida de **cualquier** equipo que pueda abrir una conexión TCP al puerto 502. Existen variantes seguras (la Modbus Organization publica una especificación Modbus/TCP Security que usa TLS ([Modbus specifications](https://www.modbus.org/modbus-specifications)), y DNP3 dispone de Secure Authentication ([DNP Users Group overview](https://www.dnp.org/About/Overview-of-DNP3-Protocol))), pero a menudo los dispositivos instalados no las admiten. Mientras no lo hagan, **poder alcanzar equivale a estar autorizado**, y los controles de red de los capítulos 10 y 11 son la defensa principal.

### 2.2 El modelo de datos de Modbus

Un dispositivo Modbus expone cuatro tablas: **bobinas** (un bit, lectura/escritura), **entradas discretas** (un bit, solo lectura), **registros de entrada** (16 bits, solo lectura) y **registros de retención** (16 bits, lectura/escritura). Lo que *significa* un registro (el nivel en centímetros, el punto de consigna de una bomba, un indicador de modo) lo define la configuración del dispositivo y se documenta en un **mapa de registros**. El protocolo en sí transporta números, no significados, de modo que un decodificador puede decirle «escritura en el registro de retención 7», pero solo el mapa de registros le dice que el registro 7 es el punto de consigna de la bomba 2.

Los códigos de función públicos más comunes son 1 (leer bobinas), 2 (leer entradas discretas), 3 (leer registros de retención), 4 (leer registros de entrada), 5 (escribir una bobina), 6 (escribir un registro), 15 (escribir varias bobinas), 16 (escribir varios registros), 8 (diagnóstico) y 43/14 (leer la identificación del dispositivo). Los códigos de función se definen en la especificación Modbus Application Protocol que publica la Modbus Organization ([Modbus specifications](https://www.modbus.org/modbus-specifications)).

### 2.3 La cabecera MBAP

Sobre TCP, cada petición Modbus empieza con una **cabecera MBAP** de 7 bytes seguida de la unidad de datos del protocolo (PDU):

| Bytes | Campo | Notas |
|---|---|---|
| 0–1 | Identificador de transacción | Empareja una respuesta con su petición. |
| 2–3 | Identificador de protocolo | Siempre 0 en Modbus. |
| 4–5 | Longitud | Número de bytes que **siguen** a este campo (id. de unidad + PDU). |
| 6 | Identificador de unidad | Direcciona un dispositivo situado tras una pasarela; a menudo 1 o 255. |
| 7 | Código de función | Qué hacer. |
| 8– | Datos | Para los códigos 1–6: una dirección de 2 bytes y una cantidad o un valor de 2 bytes. |

Todos los campos de varios bytes son *big-endian*. El módulo `struct` de Python los decodifica con el formato `>HHHBB` ([Python struct](https://docs.python.org/3/library/struct.html)). Por tanto, la trama `00 03 00 00 00 06 01 06 00 07 01 2c` se lee así: transacción 3, protocolo 0, siguen seis bytes, unidad 1, función 6 (escribir un registro), registro 7, valor 0x012C = 300.

Dos comprobaciones de coherencia detectan la mayor parte del tráfico mal formado o no Modbus en el puerto 502: el identificador de protocolo debe ser 0 y el campo de longitud debe ser igual al número de bytes que le siguen. Una herramienta de detección que omite estas comprobaciones interpretará basura como órdenes.

### 2.4 Ejemplo resuelto: una captura de KW-04 (sintético)

Un técnico exportó ocho peticiones enviadas a la RTU de KW-04 (10.10.4.2) durante una mañana de mantenimiento. La política del KVROC dice que solo la estación de ingeniería `eng-ws-15` (10.20.0.15) puede escribir en los controladores de las estaciones; `scada-01` (10.20.0.10) solo lee. **Lab 2** (guárdelo como `lab02.py` y ejecútelo con `python3 lab02.py`):

```python
# Lab 2 - decode Modbus/TCP frames and flag writes (offline, standard library only)
# Synthetic capture from Kestrel Water station KW-04; addresses are private (RFC 1918).
import struct
ENGINEERING = {"10.20.0.15"}          # only the engineering workstation may write
WRITE_FC = {5: "write single coil", 6: "write single register",
            15: "write multiple coils", 16: "write multiple registers"}
READ_FC = {1: "read coils", 2: "read discrete inputs", 3: "read holding registers", 4: "read input registers"}
capture = [  # (source, destination, frame as hex)
    ("10.20.0.10", "10.10.4.2", "000100000006010300000004"),
    ("10.20.0.10", "10.10.4.2", "000200000006010400100002"),
    ("10.20.0.15", "10.10.4.2", "00030000000601060007012c"),
    ("10.30.3.7",  "10.10.4.2", "000400000006010500a0ff00"),
    ("10.30.3.7",  "10.10.4.2", "00050000000b011000070002040064000a"),
    ("10.20.0.10", "10.10.4.2", "0006000000060103"),
    ("10.20.0.10", "10.10.4.2", "000700010006010300000004"),
    ("10.20.0.10", "10.10.4.2", "000800000006012b0e010000"),
]
def decode(hexframe):
    b = bytes.fromhex(hexframe)
    if len(b) < 8: return None, "short frame (< 8 bytes)"
    tid, pid, length, unit, fc = struct.unpack(">HHHBB", b[:8])
    if pid != 0: return None, f"protocol id {pid} is not 0 (not Modbus)"
    if length != len(b) - 6: return None, f"length field {length} but {len(b) - 6} bytes follow"
    addr, qty = struct.unpack(">HH", b[8:12]) if len(b) >= 12 else (None, None)
    return (tid, unit, fc, addr, qty), None
for src, dst, h in capture:
    d, err = decode(h)
    if err: print(f"{src:<11} -> {dst}  MALFORMED  {err}"); continue
    tid, unit, fc, addr, qty = d
    if fc in WRITE_FC:
        verdict = "ok (engineering)" if src in ENGINEERING else "ALERT unauthorized write"
        print(f"{src:<11} -> {dst}  tid={tid} unit={unit} fc={fc:<2} {WRITE_FC[fc]:<24} addr={addr} value/qty={qty}  {verdict}")
    elif fc in READ_FC:
        print(f"{src:<11} -> {dst}  tid={tid} unit={unit} fc={fc:<2} {READ_FC[fc]:<24} addr={addr} qty={qty}  ok")
    else:
        print(f"{src:<11} -> {dst}  tid={tid} unit={unit} fc={fc:<2} {'other function':<24}  REVIEW (not on read/write list)")
```

Salida esperada (Python 3.13.5):

```text
10.20.0.10  -> 10.10.4.2  tid=1 unit=1 fc=3  read holding registers   addr=0 qty=4  ok
10.20.0.10  -> 10.10.4.2  tid=2 unit=1 fc=4  read input registers     addr=16 qty=2  ok
10.20.0.15  -> 10.10.4.2  tid=3 unit=1 fc=6  write single register    addr=7 value/qty=300  ok (engineering)
10.30.3.7   -> 10.10.4.2  tid=4 unit=1 fc=5  write single coil        addr=160 value/qty=65280  ALERT unauthorized write
10.30.3.7   -> 10.10.4.2  tid=5 unit=1 fc=16 write multiple registers addr=7 value/qty=2  ALERT unauthorized write
10.20.0.10  -> 10.10.4.2  MALFORMED  length field 6 but 2 bytes follow
10.20.0.10  -> 10.10.4.2  MALFORMED  protocol id 1 is not 0 (not Modbus)
10.20.0.10  -> 10.10.4.2  tid=8 unit=1 fc=43 other function            REVIEW (not on read/write list)
```

Leamos la salida línea por línea: las lecturas del SCADA son normales; la estación de ingeniería escribió el valor 300 en el registro 7, lo esperado si existe una incidencia de cambio; un puesto corporativo (10.30.3.7) puso la bobina 160 en ON (0xFF00 = 65280) y después escribió dos registros a partir del 7. Esas dos líneas son el hallazgo de la mañana: un equipo de la zona corporativa puede alcanzar el controlador de una estación y modificarlo. Dos tramas están mal formadas (una truncada y otra con un identificador de protocolo distinto de cero), y la función 43 (identificación del dispositivo) no es ni una lectura de datos del proceso ni una escritura, así que se marca para revisión: una consulta de identificación desde un servidor SCADA conocido puede ser una funcionalidad del fabricante; la misma consulta desde un equipo desconocido es un reconocimiento de manual (MITRE incluye el descubrimiento de información de sistemas remotos entre las técnicas de ICS: [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)).

### 2.5 Actividad práctica

Decodifique a mano las tres tramas siguientes, añádalas después al Lab 2 y confirme el resultado: `000900000006010100000010`, `000a0000000601050003 0000` (quite el espacio), `000b00000006020300640001`. Anote la función, la dirección y la cantidad o el valor de cada una, y si el identificador de unidad es el que espera para KW-04. La segunda trama lleva la función 05, la escritura de una bobina, así que anote si se espera que el servidor SCADA envíe alguna vez una a KW-04. Añada después las tramas al Lab 2 y confirme que su decodificación a mano coincide con la del script. Si una trama tiene un espacio en el hexadecimal, quítelo antes de pegarla; los espacios no forman parte de la captura.

### 2.6 Errores comunes y límites

- Tratar el tráfico del puerto 502 como Modbus sin comprobar el identificador de protocolo y la longitud.
- Leer los números de registro como significados sin el mapa de registros del dispositivo.
- Alertar de todas las consultas de la función 43, o de ninguna; lo que decide es el contexto (origen, frecuencia).
- Olvidar que las respuestas también importan: una respuesta de excepción (código de función + 0x80) le dice que una petición fue rechazada (capítulo 12).
- Un decodificador solo ve lo que ve su punto de captura: el tráfico entre dos dispositivos del mismo conmutador de estación nunca llega a un sensor del centro de control.

- Alertar de todas las escrituras sin comprobar si el origen es la estación de ingeniería que nombra la política.
- Tratar una trama mal formada como un ataque cuando puede ser una exportación truncada o una sonda que no es Modbus; notifíquela primero como mal formada.

### Ejercicios — capítulo 2

**EX005 — Decodificación a mano.** *Objetivo:* leer los campos MBAP y PDU sin código. *Entradas:* `0010000000060110000a0002` está truncada; `001100000006010f00000008`. *Pasos:* decodifique todos los campos que pueda e indique si cada trama es válida. *Evidencia esperada:* tablas de campos con razonamiento. *Rúbrica:* 3 = reconoce la primera como una función 16 a la que le faltan el recuento de bytes y los valores (la longitud 6 es coherente con lo presente, pero una fc 16 válida necesita más), y la segunda como una función 15 en la dirección 0 para 8 bobinas, también incompleta sin recuento de bytes ni datos; 2 = campos correctos, validez no detectada; 1 = parcial; 0 = nada.

**EX006 — Amplíe el decodificador.** *Objetivo:* mejorar una herramienta de detección. *Entradas:* el Lab 2. *Pasos:* (1) para la función 16, decodifique también el recuento de bytes y los valores de los registros; (2) imprima los valores de la trama de 10.30.3.7. *Evidencia esperada:* cambio de código y nueva línea de salida. *Rúbrica:* 3 = se imprimen el recuento de bytes 4 y los valores 100 y 10, con una comprobación de longitud de que el recuento de bytes es igual a 2 × cantidad; 2 = valores sin comprobación; 1 = intentado; 0 = nada.

**EX007 — Política de escritura como datos.** *Objetivo:* expresar una lista de permitidos con precisión. *Entradas:* la política del KVROC. *Pasos:* escriba una lista de permitidos con entradas (origen, rango de destino, códigos de función) para la operación normal y para una ventana de mantenimiento aprobada, e indique quién conmuta entre ambas. *Evidencia esperada:* dos tablas breves y un responsable. *Rúbrica:* 3 = SCADA con códigos de solo lectura hacia todas las estaciones; escrituras de ingeniería solo hacia la estación nombrada en la incidencia y solo durante la ventana; conmutación a cargo de la guardia del KVROC con aprobación de Kestrel Water; 2 = sin ventana; 1 = vago; 0 = nada.

**EX008 — ¿Reconocimiento o funcionalidad?** *Objetivo:* razonar sobre tráfico ambiguo. *Entradas:* consultas de la función 43 desde `scada-01` cada 24 h a todas las estaciones, y la misma consulta desde 10.20.0.31 a cuatro estaciones en tres segundos. *Pasos:* decida cuál requiere actuar y qué comprobaría primero. *Evidencia esperada:* una nota breve. *Rúbrica:* 3 = la consulta diaria del SCADA tratada como probable funcionalidad de inventario que debe confirmarse con el fabricante; la ráfaga desde un equipo desconocido tratada como hallazgo prioritario: identificar 10.20.0.31 (el capítulo 17 vuelve sobre él) sin sondearlo; 2 = prioridad correcta, comprobaciones débiles; 1 = ambas ignoradas o ambas alarmadas; 0 = nada.

### Síntesis del capítulo

Los protocolos industriales clásicos confían en quien pueda alcanzarlos, de modo que la posición en la red es autoridad. Las tramas Modbus/TCP tienen una estructura fija y comprobable; decodificarlas correctamente, incluidas las comprobaciones de longitud y de protocolo, es la base de todos los filtros y detecciones posteriores. Las escrituras desde el lugar equivocado son la primera regla; las funciones de identificación y de diagnóstico necesitan contexto; y un decodificador solo ve lo que ve su punto de captura.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 18

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Sistemas operativos e identidades

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- auditar un equipo Linux que da soporte a un servicio de control: servicios a la escucha, ajustes del demonio SSH, cuentas locales y grupos privilegiados;
- explicar por qué `sshd` toma el **primer** valor que lee para la mayoría de las palabras clave, y cómo eso frustra las ediciones descuidadas;
- identificar las cuentas equivalentes a root, las cuentas de servicio con intérprete interactivo y las cuentas que no pertenecen a ninguna persona actual;
- convertir los hallazgos en un cambio de bastionado priorizado que no deje fuera a los operadores.

Los capítulos 1–2 describieron el servicio y su tráfico. Los servidores del centro de control (historiador, servidor SCADA, servidor de salto) ejecutan sistemas operativos corrientes; este capítulo convierte su configuración en algo que usted puede comprobar, no suponer.

### 3.1 Qué significa bastionar en el nivel técnico

Bastionar es eliminar lo que no se necesita y restringir lo que sí. Para un servidor de un entorno de control eso significa: servicios a la escucha solo en las interfaces que necesitan; acceso administrativo solo a través de la ruta de gestión; ninguna cuenta compartida ni huérfana; cuentas de servicio que no pueden iniciar sesión de forma interactiva; y una configuración registrada para poder detectar las derivas (capítulo 14). La guía general de servidores del NIST ofrece la lista de comprobación más amplia ([SP 800-123](https://csrc.nist.gov/pubs/sp/800/123/final)); los Cross-Sector Cybersecurity Performance Goals de CISA resumen las prácticas de cuentas y credenciales que faltan con más frecuencia ([CISA CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)).

### 3.2 Leer correctamente la configuración de sshd

El demonio de OpenSSH lee `sshd_config` de arriba abajo y, para la mayoría de las palabras clave, **se usa el primer valor obtenido**; las líneas posteriores con la misma palabra clave se ignoran ([sshd_config(5)](https://man.openbsd.org/sshd_config)). Los comentarios empiezan por `#`. Así, un archivo que tiene `PasswordAuthentication yes` cerca del principio y la corrección posterior de alguien, `PasswordAuthentication no`, al final, sigue permitiendo contraseñas. La comprobación fiable es la configuración efectiva: en un equipo real, `sshd -T` la imprime; en el Lab 3, el analizador conserva el primer valor, como hace el demonio.

Ajustes que importan en un equipo del centro de control: `ListenAddress` restringido a la interfaz de gestión; `PermitRootLogin no`; `PasswordAuthentication no` en cuanto funcionen las claves o los certificados; `X11Forwarding no`; un `MaxAuthTries` bajo; y `AllowGroups` con el nombre de un grupo cuya pertenencia también revise.

### 3.3 Cuentas e identidades

En Linux, el privilegio es un número: **UID 0** es root, sea cual sea el nombre de la cuenta. Una cuenta adicional con UID 0 («backup2», «support») es una segunda contraseña de root que nadie rota. Las **cuentas de servicio** (por convención, UID inferiores a 1000 en muchas distribuciones) ejecutan demonios; deben tener un intérprete no interactivo como `/usr/sbin/nologin`, para que una credencial de servicio robada no pueda usarse para iniciar sesión. Las **cuentas de persona** deben corresponder a alguien de la lista actual de autorizaciones; una cuenta de proveedor que permanece de forma permanente en `sudo` es un privilegio permanente que debería estar limitado en el tiempo (capítulo 10). La pertenencia a grupos forma parte de la identidad: estar en `sudo` o en `ops-admins` suele importar más que la propia cuenta.

### 3.4 Ejemplo resuelto: auditoría de HIST-02 (sintético)

`hist-02` almacena las series temporales de Kestrel Water. Política del KVROC: SSH solo en la dirección de gestión 10.90.0.21; sin inicio de sesión de root; solo claves; como máximo tres intentos; solo J. Tan y R. Kaur autorizados. **Lab 3** (guárdelo como `lab03.py` y ejecútelo con `python3 lab03.py`):

```python
# Lab 3 - audit a host configuration and its local accounts (offline, standard library only)
# Synthetic files from historian host HIST-02 at the Kestrel Vale operations centre.
sshd_config = """
Port 22
ListenAddress 0.0.0.0
PermitRootLogin yes
PasswordAuthentication yes
# PasswordAuthentication no
PubkeyAuthentication yes
X11Forwarding yes
MaxAuthTries 6
AllowGroups ops-admins
"""
passwd = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
histsvc:x:998:998:historian service:/opt/hist:/bin/bash
jtan:x:1001:1001:J. Tan:/home/jtan:/bin/bash
rkaur:x:1002:1002:R. Kaur:/home/rkaur:/bin/bash
backup2:x:0:0:temp backup:/root:/bin/bash
vendor:x:1003:1003:vendor support:/home/vendor:/bin/bash"""
group = """ops-admins:x:1100:jtan,vendor
sudo:x:27:jtan,rkaur,vendor"""
policy = {"PermitRootLogin": "no", "PasswordAuthentication": "no", "X11Forwarding": "no",
          "ListenAddress": "10.90.0.21", "MaxAuthTries": "3"}
roster = {"jtan", "rkaur"}                     # people currently authorized on HIST-02
eff = {}
for line in sshd_config.splitlines():
    line = line.split("#", 1)[0].strip()
    if not line: continue
    key, val = line.split(None, 1)
    eff.setdefault(key, val)                   # sshd uses the FIRST value it reads for a keyword
findings = []
for k, want in policy.items():
    if eff.get(k) != want: findings.append(f"sshd {k} is {eff.get(k)!r}, policy {want!r}")
for line in passwd.splitlines():
    name, _, uid, gid, gecos, home, shell = line.split(":")
    if uid == "0" and name != "root": findings.append(f"account {name} has UID 0 (root equivalent)")
    if 0 < int(uid) < 1000 and shell.endswith("sh") and not shell.endswith("nologin"):
        findings.append(f"service account {name} has interactive shell {shell}")
    if int(uid) >= 1000 and name not in roster: findings.append(f"person account {name} not on roster")
for line in group.splitlines():
    g, _, _, members = line.split(":")
    for m in members.split(","):
        if m and m not in roster: findings.append(f"group {g} contains {m} (not on roster)")
for f in findings: print(f)
print("findings:", len(findings))
```

Salida esperada (Python 3.13.5):

```text
sshd PermitRootLogin is 'yes', policy 'no'
sshd PasswordAuthentication is 'yes', policy 'no'
sshd X11Forwarding is 'yes', policy 'no'
sshd ListenAddress is '0.0.0.0', policy '10.90.0.21'
sshd MaxAuthTries is '6', policy '3'
service account histsvc has interactive shell /bin/bash
account backup2 has UID 0 (root equivalent)
person account vendor not on roster
group ops-admins contains vendor (not on roster)
group sudo contains vendor (not on roster)
findings: 10
```

Diez hallazgos. Fíjese en la línea de `PasswordAuthentication`: el archivo contiene un `no` comentado, que algunos revisores leen como «ya corregido». Es un comentario, y el valor efectivo es `yes`. Los hallazgos más peligrosos son `backup2` con UID 0 (un segundo root sin gestionar) y `vendor` en `sudo` (acceso privilegiado permanente de un proveedor). La cuenta de servicio del historiador con `/bin/bash` importa porque las credenciales del servicio se guardan en disco para que el historiador las use.

Un orden de bastionado seguro: (1) confirmar que J. Tan y R. Kaur pueden iniciar sesión con clave desde `jump-01`; (2) restringir `ListenAddress`, `PermitRootLogin` y `PasswordAuthentication` en un único cambio, manteniendo abierta una sesión existente mientras prueba una nueva; (3) eliminar `backup2` después de conservar su historial de inicios de sesión; (4) quitar a `vendor` de `sudo` y llevar el acceso del proveedor a un procedimiento limitado en el tiempo; (5) cambiar el intérprete de la cuenta de servicio a `nologin` después de comprobar que ningún script de mantenimiento inicia sesión con ella.

### 3.5 Actividad práctica

En una máquina virtual de su propiedad, ejecute `sshd -T | sort` y compare la salida con el archivo. Añada una palabra clave duplicada más abajo en el archivo, recargue y confirme que gana el primer valor. Anote la versión exacta de OpenSSH, porque el comportamiento de los bloques `Include` y `Match` varía según la versión. Anote la versión de OpenSSH y la ruta de cada archivo que `sshd -T` muestre como incluido. Después de recargar, abra una segunda sesión antes de cerrar la primera, para que un cambio erróneo de ListenAddress o de AllowGroups no le deje fuera. Compare los valores efectivos con la tabla de política del Lab 3 y anote cualquier palabra clave que aparezca dos veces en el archivo.

### 3.6 Errores comunes y límites

- Leer el archivo en lugar de la configuración efectiva.
- Corregir los ajustes de SSH desde la única sesión abierta y dejar fuera a todo el mundo; pruebe siempre antes una segunda sesión.
- Comprobar los nombres de las cuentas en lugar de los UID.
- Quitar el intérprete de una cuenta de servicio sin comprobar los scripts que dependen de ella.
- El Lab 3 no trata ni los archivos `Include` ni los bloques `Match`; las auditorías reales deben hacerlo.

- Editar PasswordAuthentication al final del archivo mientras sigue ganando un yes anterior.
- Quitar a vendor de sudo sin un procedimiento limitado en el tiempo para la siguiente visita de soporte.
- Comprobar los nombres de las cuentas en lugar de los UID, de modo que pasa inadvertido un segundo root llamado backup2.

### Ejercicios — capítulo 3

**EX009 — Gana el primer valor.** *Objetivo:* razonar sobre la configuración efectiva. *Entradas:* el `sshd_config` del Lab 3. *Pasos:* (1) prediga el `PasswordAuthentication` efectivo si la línea comentada se descomenta y se deja donde está; (2) indique dónde debe ir la corrección. *Evidencia esperada:* predicción y ubicación. *Rúbrica:* 3 = sigue siendo `yes` porque gana la línea anterior; la corrección sustituye la primera aparición (o se borra la línea anterior), verificado con `sshd -T`; 2 = respuesta correcta, sin verificación; 1 = predice `no`; 0 = nada.

**EX010 — Priorice los hallazgos de HIST-02.** *Objetivo:* ordenar los cambios por riesgo y seguridad. *Entradas:* la salida del Lab 3. *Pasos:* agrupe los diez hallazgos en hoy / esta semana / próxima ventana de mantenimiento, con razones de una línea y un paso de conservación donde haga falta. *Evidencia esperada:* una lista en tres grupos. *Rúbrica:* 3 = `backup2` con UID 0 y `vendor` en sudo hoy, conservando antes el historial de inicios de sesión; el enlace de SSH y los ajustes de root/contraseña como un único cambio probado; el intérprete del servicio tras comprobar los scripts; 2 = sensato pero sin conservación; 1 = sin orden; 0 = nada.

**EX011 — Amplíe la auditoría.** *Objetivo:* añadir una comprobación. *Entradas:* el Lab 3. *Pasos:* añada una comprobación que marque cualquier cuenta distinta de `root` cuyo intérprete sea interactivo y cuyo directorio personal sea `/root` o `/`. Informe de la nueva salida. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = marca `backup2` (directorio personal `/root`) y solo esa; explica por qué los directorios personales compartidos ocultan la rendición de cuentas; 2 = funciona sin explicación; 1 = intentado; 0 = nada.

**EX012 — Diseño de una cuenta de servicio.** *Objetivo:* diseñar una identidad no interactiva. *Entradas:* el servicio del historiador necesita leer archivos de `/opt/hist` y escribir en su base de datos. *Pasos:* especifique el rango de UID, el intérprete, el directorio personal, el grupo, los permisos de archivo y cómo se guarda y se rota su credencial. *Evidencia esperada:* una especificación breve. *Rúbrica:* 3 = UID de sistema, intérprete `nologin`, grupo dedicado, modos de archivo de mínimo privilegio, credencial legible solo por el servicio, responsable e intervalo de rotación; 2 = una carencia; 1 = genérico; 0 = nada.

### Síntesis del capítulo

El bastionado del sistema operativo se puede comprobar: los ajustes efectivos, los UID, los intérpretes y la pertenencia a grupos pueden leerse y compararse con una política escrita. Sepa cómo lee realmente el demonio su archivo, mire los números en lugar de los nombres y ordene los cambios de modo que nunca deje fuera a las personas que operan el servicio.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Siga estudiando — capítulo 03 de 18

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Scripts y formatos de datos

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- analizar datos operativos en CSV y JSON con la biblioteca estándar, sin dividir cadenas a mano;
- validar cada registro frente a un esquema explícito: número de campos, unidades, forma numérica, finitud, formato de la marca de tiempo y rango físico;
- notificar cada problema con sus **coordenadas del registro** (archivo y línea) para que otra persona pueda encontrarlo;
- elegir entre **rechazar** y **poner en cuarentena**, y resumir los resultados en un formato legible por máquina.

Los scripts del técnico de los capítulos posteriores (decodificadores, auditores, detectores) leen todos datos que produjo otra persona. Este capítulo los vuelve estrictos con lo que aceptan, porque un script que «corrige» en silencio una entrada errónea produce respuestas equivocadas con total seguridad.

### 4.1 Formatos con los que se encontrará

- **CSV**: exportaciones de historiadores, HMI y hojas de cálculo. La RFC 4180 describe el formato común, incluido el entrecomillado: un campo que contiene una coma debe ir entre comillas dobles ([RFC 4180](https://www.rfc-editor.org/rfc/rfc4180)). Dividir las líneas por comas falla con el primer valor entrecomillado; use `csv.reader`, que además lleva la cuenta de `line_num`.
- **JSON**: API, exportaciones de configuración y salida de herramientas ([RFC 8259](https://www.rfc-editor.org/rfc/rfc8259)). Use `json.loads`; tenga en cuenta que el analizador de Python acepta los símbolos no estándar `NaN` e `Infinity` salvo que pase `parse_constant` para rechazarlos.
- **Marcas de tiempo**: use RFC 3339 / ISO 8601 con un desfase explícito, idealmente UTC con `Z` ([RFC 3339](https://www.rfc-editor.org/rfc/rfc3339)). Una marca de tiempo sin desfase es ambigua hasta en un día y en los cambios de horario de verano.
- **Tramas binarias**: la decodificación con `struct` del capítulo 2; compruebe siempre las longitudes antes de desempaquetar.

### 4.2 Un orden de validación que falla de forma cerrada

Compruebe en un orden en el que cada paso pueda suponer que los anteriores se superaron:

1. **Estructura**: el número correcto de campos. Si no lo es, no puede confiarse en nada más del registro: rechazar.
2. **Identidad y tipo**: estación y etiqueta conocidas; la unidad que indica el esquema (un nivel en pies no es un nivel en metros); el valor se analiza como número.
3. **Finitud**: `float("nan")` y `float("inf")` se analizan sin error, pero no son mediciones: rechazar.
4. **Tiempo**: la marca de tiempo se analiza en el formato acordado; no está en el futuro más allá de una pequeña tolerancia.
5. **Verosimilitud**: el valor está dentro del rango físico del instrumento y del proceso.

**Rechace** lo que no puede interpretarse (estructura errónea, unidad errónea, no es un número). **Ponga en cuarentena** lo que puede interpretarse pero es inverosímil (fuera de rango, hora futura): un fallo real de un sensor y un ataque real tienen ambos este aspecto, y un operador debe verlo en lugar de que se descarte en silencio. No fuerce nunca la conversión: convertir `"12,5"` en 12.5 o en 125 adivinando el separador decimal crea datos que nunca se midieron.

### 4.3 Coordenadas del registro

Todo hallazgo debe decir de dónde procede (archivo, línea y campo) para que otra persona pueda verificarlo. `csv.reader.line_num` cuenta las líneas físicas leídas hasta el momento, incluida la cabecera, de modo que la primera fila de datos es la línea 2. Los campos entrecomillados que contienen saltos de línea hacen que las líneas físicas difieran de los registros; `line_num` indica la línea en la que terminó el registro, que sigue siendo una coordenada utilizable. Cuando pegue un hallazgo en una incidencia, mantenga el número de línea junto al nombre de la estación, para que la siguiente persona pueda abrir la exportación e ir directamente a la fila. Si un campo entrecomillado ocupa varias líneas, indíquelo, porque la coordenada marca entonces el final del registro y no su comienzo.

### 4.4 Ejemplo resuelto: validar una exportación de estaciones (sintético)

Una exportación del historiador de Kestrel Water contiene una lectura por estación. La hora del análisis es 06:00Z del 12 de octubre de 2026. **Lab 4** (guárdelo como `lab04.py` y ejecútelo con `python3 lab04.py`):

```python
# Lab 4 - validate a telemetry export with record coordinates (offline, standard library only)
# Synthetic CSV export from Kestrel Water stations; "now" is 2026-10-12T06:00:00Z.
import csv, io, json, math
from datetime import datetime, timezone
export = """station,tag,value,unit,ts
KW-01,LEVEL_M,3.42,m,2026-10-12T05:58:00Z
KW-02,CL2_MGL,0.61,mg/L,2026-10-12T05:58:00Z
KW-03,LEVEL_M,,m,2026-10-12T05:58:00Z
KW-04,CL2_MGL,7.9,mg/L,2026-10-12T05:58:00Z
KW-05,FLOW_LS,"12,5",L/s,2026-10-12T05:58:00Z
KW-06,LEVEL_M,2.10,ft,2026-10-12T05:58:00Z
KW-07,LEVEL_M,2.95,m,2026-10-12 05:58
KW-08,LEVEL_M,nan,m,2026-10-12T05:58:00Z
KW-09,FLOW_LS,41.0,L/s,2026-10-12T07:15:00Z
KW-10,LEVEL_M,1.88,m,2026-10-12T05:58:00Z,extra
"""
SCHEMA = {"LEVEL_M": ("m", 0.0, 12.0), "CL2_MGL": ("mg/L", 0.0, 5.0), "FLOW_LS": ("L/s", 0.0, 400.0)}
now = datetime(2026, 10, 12, 6, 0, tzinfo=timezone.utc)
result = {"accept": [], "reject": [], "quarantine": []}
reader = csv.reader(io.StringIO(export))
header = next(reader)
for row in reader:
    where = f"line {reader.line_num}"
    if len(row) != len(header): result["reject"].append((where, f"{len(row)} fields, expected {len(header)}")); continue
    r = dict(zip(header, row))
    unit, lo, hi = SCHEMA[r["tag"]]
    if r["unit"] != unit: result["reject"].append((where, f"{r['station']} unit {r['unit']!r}, expected {unit!r}")); continue
    try: v = float(r["value"])
    except ValueError: result["reject"].append((where, f"{r['station']} value {r['value']!r} not a number")); continue
    if not math.isfinite(v): result["reject"].append((where, f"{r['station']} value not finite")); continue
    try:
        ts = datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError: result["reject"].append((where, f"{r['station']} timestamp {r['ts']!r} not RFC 3339 UTC")); continue
    if ts > now: result["quarantine"].append((where, f"{r['station']} timestamp {(ts - now).seconds // 60} min in the future")); continue
    if not lo <= v <= hi: result["quarantine"].append((where, f"{r['station']} {r['tag']}={v} outside {lo}-{hi}")); continue
    result["accept"].append((where, r["station"]))
for k in ("reject", "quarantine"):
    for where, why in result[k]: print(f"{k:<10} {where:<8} {why}")
print(json.dumps({k: len(v) for k, v in result.items()}))
```

Salida esperada (Python 3.13.5):

```text
reject     line 4   KW-03 value '' not a number
reject     line 6   KW-05 value '12,5' not a number
reject     line 7   KW-06 unit 'ft', expected 'm'
reject     line 8   KW-07 timestamp '2026-10-12 05:58' not RFC 3339 UTC
reject     line 9   KW-08 value not finite
reject     line 11  6 fields, expected 5
quarantine line 5   KW-04 CL2_MGL=7.9 outside 0.0-5.0
quarantine line 10  KW-09 timestamp 75 min in the future
{"accept": 2, "reject": 6, "quarantine": 2}
```

Solo se aceptan dos de diez filas. Cada rechazo indica su línea: un valor vacío (línea 4), una coma decimal dentro de un campo entrecomillado (línea 6), un nivel en pies (línea 7), una marca de tiempo sin segundos ni desfase (línea 8), `nan` (línea 9) y un campo de más (línea 11). Las filas en cuarentena son las interesantes: un cloro de 7,9 mg/L está fuera del rango del instrumento (un fallo del sensor, un error de escalado o un valor manipulado), y la marca de tiempo de KW-09 está 75 minutos en el futuro, algo que en el capítulo 7 aprenderá a sospechar como un problema de reloj. Ambas se pasan a una persona con sus coordenadas.

El resumen JSON de la última línea es deliberadamente legible por máquina, para que una tarea de supervisión pueda alertar cuando suba el número de rechazos.

### 4.5 Actividad práctica

Añada al Lab 4 una comprobación de identidad de la estación: solo son válidas de KW-01 a KW-12. Añada después una fila `KW-13,LEVEL_M,2.0,m,2026-10-12T05:58:00Z` y confirme que se rechaza con su número de línea. Por último, haga que el analizador de marcas de tiempo acepte un desfase explícito `+00:00` además de `Z`, sin aceptar marcas de tiempo sin zona. Rechace KW-13 con su número de línea y un motivo que nombre el conjunto permitido. Para las marcas de tiempo, acepte tanto Z como un desfase explícito de más cero, y siga rechazando una hora local sin zona. Vuelva a ejecutar el laboratorio y confirme que el número de rechazos del resumen JSON sube en uno por la nueva estación.

### 4.6 Errores comunes y límites

- Dividir el CSV por comas.
- Forzar la conversión de valores ambiguos en lugar de rechazarlos.
- Dejar pasar `nan` porque `nan > hi` es falso.
- Aceptar marcas de tiempo sin zona y suponer la hora local.
- Informar de «6 rechazadas» sin coordenadas, lo que nadie puede comprobar.
- El Lab 4 comprueba lecturas individuales; la velocidad de cambio y los valores congelados necesitan una serie (capítulo 8).

- Dejar pasar nan porque las comparaciones con él son falsas, de modo que una comprobación de fuera de rango nunca se dispara.
- Informar solo de totales sin coordenadas, de modo que nadie puede encontrar las filas erróneas.
- Convertir una coma decimal en un número de coma flotante y escribir el valor inventado en el historiador.

### Ejercicios — capítulo 4

**EX013 — Prediga antes de ejecutar.** *Objetivo:* razonar sobre el validador. *Entradas:* el Lab 4 con tres filas nuevas: `KW-11,LEVEL_M,12.0,m,2026-10-12T05:59:00Z`; `KW-12,LEVEL_M,inf,m,2026-10-12T05:59:00Z`; `KW-02,CL2_MGL,-0.0,mg/L,2026-10-12T05:59:00Z`. *Pasos:* prediga cada veredicto y el nuevo resumen, y después ejecute. *Evidencia esperada:* predicciones, salida real y explicación de cualquier sorpresa. *Rúbrica:* 3 = aceptar, rechazar (no finito), aceptar; resumen `{"accept": 4, "reject": 7, "quarantine": 2}`; señala que −0.0 debería normalizarse; 2 = uno erróneo pero explicado; 1 = conjeturas; 0 = nada.

**EX014 — ¿Rechazar o poner en cuarentena?** *Objetivo:* aplicar la distinción. *Entradas:* (a) caudal −3,0 L/s; (b) unidad «M» en lugar de «m»; (c) nivel de 11,9 m en un depósito de 12 m; (d) marca de tiempo 4 s en el futuro. *Pasos:* decida y justifique. *Evidencia esperada:* cuatro veredictos. *Rúbrica:* 3 = (a) cuarentena (interpretable, inverosímil; podría ser un flujo inverso o un desfase); (b) rechazar, o normalizar solo si el esquema admite explícitamente unidades sin distinguir mayúsculas, sin adivinar; (c) aceptar, quizá con una alarma de nivel alto; (d) aceptar dentro de una tolerancia de reloj acordada; 2 = una débil; 1 = rechazarlas todas; 0 = nada.

**EX015 — JSON con trampas.** *Objetivo:* bastionar el análisis de JSON. *Entradas:* `{"station": "KW-03", "value": NaN}`. *Pasos:* muestre lo que devuelve `json.loads` por defecto y escriba el cambio de una línea que lo rechaza. *Evidencia esperada:* código y comportamiento. *Rúbrica:* 3 = por defecto devuelve un float `nan`; `json.loads(s, parse_constant=lambda c: (_ for _ in ()).throw(ValueError(c)))` o una función equivalente que lance una excepción; explica que la RFC 8259 no admite NaN; 2 = funciona sin explicación; 1 = intentado; 0 = nada.

**EX016 — Resumen para la supervisión.** *Objetivo:* diseñar un resultado legible por máquina. *Entradas:* el Lab 4. *Pasos:* amplíe el resumen JSON con recuentos por motivo y por estación, y proponga una condición de alerta sobre él. *Evidencia esperada:* un JSON de ejemplo y la condición. *Rúbrica:* 3 = claves estables, recuentos por motivo, una alerta como «cualquier cuarentena de CL2_MGL, o rechazos > 10 % de las filas en dos exportaciones consecutivas»; 2 = sin desglose por motivo; 1 = solo prosa; 0 = nada.

### Síntesis del capítulo

Los datos operativos llegan mal formados, ambiguos y, a veces, hostiles. Analice con analizadores de verdad, valide en un orden que falle de forma cerrada, no fuerce nunca conversiones e informe de cada hallazgo con sus coordenadas. Rechace lo que no puede interpretar; ponga en cuarentena lo que puede interpretar pero no debería creer; y mantenga los resúmenes legibles por máquina para que el propio validador pueda supervisarse.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Siga estudiando — capítulo 04 de 18

[← Capítulo 03](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Alcance de seguridad y evidencia

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- redactar un **alcance técnico** para una tarea en un entorno crítico: sistemas, acciones permitidas, ventana temporal, contactos y condiciones de parada;
- explicar por qué, en la tecnología operacional, se prefiere una observación pasiva y una activa requiere aprobación explícita;
- recoger evidencia técnica de modo que otra persona pueda verificarla: qué, desde dónde, cuándo (UTC), quién, cómo y su hash;
- separar lo **observado**, lo **inferido**, lo **hecho** y lo **abierto** en toda nota de trabajo.

Los capítulos 1–4 le dieron herramientas. Antes de apuntar cualquiera de ellas a un sistema real, este capítulo define lo que tiene permitido tocar y cómo demostrará lo que vio.

### 5.1 El alcance es un control de seguridad

En una red de oficina, un escaneo demasiado entusiasta hace perder el tiempo. En una red de control puede detener un proceso: algunos controladores y pilas de red antiguas se comportan mal cuando se les sondea, y una «lectura» puede desencadenar diagnósticos del fabricante o llenar una tabla de sesiones. La guía de TO del NIST recomienda prudencia con el escaneo activo en entornos operativos y prefiere los métodos pasivos siempre que sea posible ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); la guía de pruebas del NIST describe reglas de enfrentamiento para cualquier evaluación ([SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)).

Un alcance técnico responde, por escrito y antes de empezar el trabajo:

- **Finalidad**: qué pregunta responde el trabajo.
- **Sistemas dentro del alcance**: equipos y direcciones nombrados; todo lo demás queda fuera.
- **Acciones permitidas**: por ejemplo, «leer la configuración en ejecución», «captura pasiva en el puerto SPAN», «una prueba de conexión TCP al puerto 502 sin petición Modbus».
- **Ventana**: fecha y horas, con el acuerdo del operador.
- **Personas**: quién lo autorizó (el propietario del sistema), quién está en la instalación, a quién se informa en la sala de control.
- **Condiciones de parada**: cualquier comportamiento inesperado de un dispositivo, una alarma o una petición de operaciones.
- **Tratamiento de la evidencia**: dónde se guardan los resultados y quién puede leerlos.

### 5.2 Primero lo pasivo

Muchas preguntas pueden responderse sin enviar un solo paquete: exportaciones de configuración, registros del cortafuegos, tablas MAC de los conmutadores, una captura pasiva desde un puerto espejo (SPAN), los propios registros del historiador. Prefiera estas fuentes. Cuando una prueba activa sea realmente necesaria (por ejemplo, para verificar una regla de denegación en el capítulo 11), hágala la prueba más pequeña que responda a la pregunta, desde un origen nombrado y a una hora acordada. Prefiera una captura SPAN o una exportación de configuración antes de cualquier prueba de conexión. Cuando haga falta una prueba activa, use una dirección de origen señalada, la acción más pequeña que responda a la pregunta y una ventana acordada, con operaciones informada al principio y al final.

### 5.3 Qué hace utilizable la evidencia técnica

Una captura de pantalla de un terminal demuestra poco. La evidencia utilizable registra:

1. **Qué**: la salida o el archivo en bruto, no un resumen.
2. **Fuente**: equipo y herramienta, con su versión.
3. **Hora**: en UTC, con el desfase del reloj del equipo si se conoce (capítulo 7).
4. **Recolector**: quién lo ejecutó.
5. **Método**: la orden o consulta exacta.
6. **Integridad**: un hash SHA-256 registrado en el momento de la recogida, para poder comprobar las copias posteriores ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)); el capítulo 18 sella un paquete completo.

La guía del NIST para integrar técnicas forenses en la respuesta a incidentes trata el orden de recogida y de conservación ([SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final)). En el nivel técnico, la regla es sencilla: **conserve antes de cambiar**. Si está a punto de corregir algo que puede ser evidencia de un uso indebido, recójalo primero.

### 5.4 Cuatro etiquetas

Toda nota que escriba en este curso usa cuatro etiquetas. **Observado**: lo que registró una herramienta o una persona, con fuente y hora. **Inferido**: lo que usted concluye y por qué. **Hecho**: lo que cambió y con qué registro de cambio. **Abierto**: lo que sigue sin saberse y quién es su responsable. Mezclarlas («la RTU estaba comprometida» cuando solo observó una sesión de configuración) es la forma en que se propagan las conclusiones erróneas. Una nota que solo dice «RTU comprometida» no supera la prueba: mezcla inferencia con observación. Escriba las cuatro etiquetas en toda nota de trabajo de este curso, incluida la comprobación de alcanzabilidad de KW-04, para que el lector vea qué se midió y qué sigue abierto.

### 5.5 Ejemplo resuelto: el alcance de la comprobación de KW-04 (sintético)

Después de que el Lab 2 mostrara escrituras desde un puesto corporativo, L. Ferreira (responsable de seguridad del KVROC) le pide que confirme si la zona corporativa puede alcanzar el puerto 502 de las estaciones. Un alcance sólido:

| Elemento | Contenido |
|---|---|
| Finalidad | Confirmar o refutar la alcanzabilidad desde la zona corporativa hasta KW-04 tcp/502. |
| Dentro del alcance | Configuración y registros de fw-01 (lectura); una conexión TCP desde el puesto de pruebas 10.30.99.9 a 10.10.4.2:502, sin carga Modbus. |
| Fuera del alcance | Todas las demás estaciones; cualquier petición Modbus; el puesto 10.30.3.7 (conservar, no tocar). |
| Ventana | 13 oct. 2026, 10:00–10:30 hora local, acordada con A. Mensah (operaciones de Kestrel Water). |
| Personas | Autoriza A. Mensah; se informa al operador de la sala de control de Kestrel Water al principio y al final. |
| Parada | Cualquier alarma de KW-04, pérdida de comunicación o petición del operador. |
| Evidencia | Exportación de la configuración del cortafuegos, salida de la prueba de conexión, líneas del registro de fw-01; hashes en la carpeta del caso. |

La nota de trabajo tras la prueba dice: *Observado*: la conexión de 10.30.99.9 a 10.10.4.2:502 no se completó a las 08:04:11Z; fw-01 la registró como bloqueada por la denegación por defecto. *Inferido*: fw-01 no permite que los puestos corporativos alcancen el Modbus de las estaciones, así que las escrituras desde 10.30.3.7 capturadas en el capítulo 2 tuvieron que usar otra ruta (capítulos 10 y 13). *Hecho*: no se cambió nada. *Abierto*: qué ruta llevó esas escrituras (responsable: L. Ferreira).

### 5.6 Actividad práctica

Redacte un alcance para una captura pasiva de 24 horas en el puerto SPAN del conmutador del centro de control. Incluya límites de almacenamiento y quién puede leer la captura, ya que contendrá valores del proceso y posiblemente credenciales enviadas en texto claro. Indique un tamaño máximo de archivo y un periodo de conservación, porque un día de valores del proceso y de credenciales en texto claro es a la vez voluminoso y sensible. Nombre quién puede leer la captura y dónde se guarda, y diga que la captura se detiene si el puerto espejo del conmutador afecta al reenvío. Señale la actividad como pasiva y enumere condiciones de parada que incluyan cualquier petición del operador.

### 5.7 Errores comunes y límites

- Empezar a trabajar con un «adelante» verbal.
- Escanear una subred para «ver qué hay» en una red de control.
- Recoger evidencia sin horas UTC ni hashes.
- Corregir primero y recoger después.
- Tratar el alcance como papeleo: es lo que impide que una prueba se convierta en un incidente.

- Partir de un visto bueno verbal y redactar el alcance después.
- Escanear una subred de una red de control para descubrir dispositivos.
- Corregir un hallazgo antes de recoger la evidencia que lo mostró. Un alcance redactado después del trabajo no puede proteger el proceso mientras se realiza.

### Ejercicios — capítulo 5

**EX017 — Repare un alcance.** *Objetivo:* encontrar los elementos que faltan. *Entradas:* «Ejecutar un escaneo de 10.10.0.0/16 el martes para encontrar puertos abiertos. Aprobado por TI». *Pasos:* enumere cada defecto y reescríbalo. *Evidencia esperada:* lista de defectos y alcance reescrito. *Rúbrica:* 3 = identifica el autorizador equivocado (hace falta el propietario del sistema), el rango sin límites, el escaneo activo en TO, la falta de ventana, de condiciones de parada y de tratamiento de la evidencia; la reescritura prefiere fuentes de inventario pasivas; 2 = la mayoría de los defectos; 1 = cosmético; 0 = nada.

**EX018 — Etiquete la nota.** *Objetivo:* separar observación e inferencia. *Entradas:* «El proveedor hackeó KW-09 anoche: la configuración de la RTU cambió y los datos se interrumpieron, así que la reinicié». *Pasos:* reescríbala con las cuatro etiquetas. *Evidencia esperada:* nota etiquetada. *Rúbrica:* 3 = observado (hora de la sesión de configuración, laguna de datos), inferido (posible cambio no aprobado; autoría desconocida), hecho (el reinicio, y la pérdida de evidencia que causó), abierto (quién, por qué; responsable); 2 = etiquetas sin advertir la pérdida de evidencia; 1 = parcial; 0 = nada.

**EX019 — Registro de evidencia.** *Objetivo:* producir evidencia verificable. *Entradas:* usted exporta el conjunto de reglas de fw-01 a `fw-01-rules-20261013.txt`. *Pasos:* escriba los campos del registro de evidencia y la orden que produce su hash en Linux. *Evidencia esperada:* el registro y `sha256sum fw-01-rules-20261013.txt`. *Rúbrica:* 3 = los seis elementos, hora UTC con la fuente del reloj, hash guardado por separado del archivo; 2 = falta uno; 1 = solo el hash; 0 = nada.

**EX020 — Alternativas pasivas.** *Objetivo:* evitar pruebas activas innecesarias. *Entradas:* tres preguntas: qué equipos hablan con KW-07; qué firmware ejecuta KW-07; si KW-07 acepta telnet. *Pasos:* proponga un método pasivo o de solo lectura para cada una e indique cuándo seguiría estando justificada una prueba activa. *Evidencia esperada:* tres filas. *Rúbrica:* 3 = registros de flujos o captura SPAN; registros de activos o la herramienta del fabricante durante una sesión de ingeniería aprobada; exportación de la configuración o documentación del fabricante, con una comprobación activa solo en una ventana delimitada y con operaciones presente; 2 = una débil; 1 = todas activas; 0 = nada.

### Síntesis del capítulo

En los entornos críticos, el alcance protege al proceso tanto como a quien hace la prueba. Redáctelo antes de empezar, prefiera los métodos pasivos y haga que cada elemento de evidencia sea verificable por otra persona: en bruto, con fuente, con hora UTC, atribuido y con hash. Conserve antes de cambiar, y mantenga separados lo observado, lo inferido, lo hecho y lo abierto.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Siga estudiando — capítulo 05 de 18

[← Capítulo 04](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Infraestructura crítica y seguridad sectorial: modelo del sistema

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- construir un modelo técnico del sistema de un servicio crítico: activos, zonas, conductos, protocolos, límites de confianza y la consecuencia física que puede causar cada zona;
- usar el vocabulario de zonas y conductos de ISA/IEC 62443 en el nivel de un técnico;
- describir en qué se diferencian técnicamente los servicios de agua, sanitarios y eléctricos: protocolos, tiempos, sistemas de seguridad funcional y quién puede cambiar qué;
- señalar en el modelo dónde se situarán los controles y las detecciones de cada capítulo posterior.

Los capítulos 1–5 fueron los fundamentos generales. A partir de aquí, el curso los aplica a los sectores críticos. El modelo del sistema es el mapa del técnico: sin él, una regla de cortafuegos, una detección o un paso de diagnóstico no tienen nada a lo que referirse.

### 6.1 Zonas y conductos

La serie ISA/IEC 62443 agrupa los activos con requisitos de seguridad similares en **zonas** y las rutas de comunicación entre ellas en **conductos** ([ISA/IEC 62443 overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). Las reglas prácticas que aplica un técnico:

- cada activo pertenece exactamente a una zona;
- cada comunicación permitida entre zonas es un conducto declarado, con finalidad, protocolo, sentido y responsable;
- lo que no está declarado no está permitido y, si se observa, es un hallazgo (el Lab 17 y el capítulo 11 lo verifican);
- la protección de una zona debe corresponder a la peor consecuencia física de los activos que contiene.

La forma común de un sistema de supervisión (campo, control, supervisión, DMZ de operaciones, empresa) aparece en NIST SP 800-82 Rev. 3 como arquitectura de ejemplo ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). Úsela como vocabulario, no como plantilla: una instalación real tiene excepciones históricas, y la tarea del modelo es mostrarlas.

### 6.2 Qué registrar de cada elemento

De cada **activo**: nombre, dirección, función, zona, responsable, versiones de software y firmware, protocolos que habla, método de gestión y la consecuencia física de su pérdida o de su uso indebido. De cada **conducto**: zona de origen, zona de destino, protocolo y puerto, sentido de iniciación, finalidad, responsable, punto de aplicación (qué regla de cortafuegos) y punto de supervisión (qué sensor lo ve). De cada **límite de confianza**: qué lo atraviesa y qué comprobaciones se hacen en él. De eng-ws-15, registre que puede programar las RTU y que su pérdida o su uso indebido tiene consecuencias en toda la zona. Para cada conducto, nombre la regla de cortafuegos que debería aplicarlo y el sensor que debería verlo, para que una verificación posterior sepa dónde mirar. No deje ningún activo sin zona ni ninguna ruta permitida sin responsable del conducto.

### 6.3 Diferencias entre sectores que importan ante el teclado

- **Agua**: estaciones muy dispersas con enlaces celulares o de radio; telemetría Modbus o DNP3; largas vidas útiles de los equipos; operadores pequeños con personal limitado. Las consecuencias incluyen la pérdida de presión, los desbordamientos y la dosificación química incorrecta. El aviso de CISA sobre los ataques contra PLC Unitronics expuestos a internet en sistemas de agua recuerda que la exposición más las credenciales por defecto bastan ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)).
- **Electricidad**: subestaciones con relés de protección cuyos tiempos se miden en milisegundos; telecontrol DNP3 o IEC 60870-5-104 hacia un centro de control; IEC 61850 dentro de las subestaciones modernas; separación estricta entre las funciones de protección y las de supervisión. Un técnico nunca cambia los ajustes de protección; pertenecen a los ingenieros de protecciones.
- **Sanidad**: sistemas de gestión del edificio (ventilación, presión en las habitaciones de aislamiento, supervisión de los gases medicinales), redes de dispositivos clínicos y sistemas de TI en un mismo edificio, que a menudo comparten infraestructura; las paradas afectan directamente a los pacientes y los cambios están sujetos a la ingeniería clínica y a las instrucciones de los fabricantes de los dispositivos.

En los tres, los **sistemas instrumentados de seguridad** y las funciones de protección están diseñados para actuar con independencia del sistema de supervisión. El modelo del técnico los muestra como zonas separadas y nunca encamina tráfico de gestión a través de ellos.

### 6.4 Ejemplo resuelto: el modelo del KVROC (sintético)

| Zona | Activos | Peor consecuencia | Notas |
|---|---|---|---|
| Z1 Campo de las estaciones (10.10.0.0/16) | RTU KW-01..12, bombas, analizadores | Dosificación errónea, desbordamiento, pérdida de suministro | Modbus/TCP, sin autenticación |
| Z2 Centro de control (10.20.0.0/24) | scada-01, hmi-02, eng-ws-15, hist-02 | Pérdida de visión y de control de todas las estaciones | eng-ws-15 puede programar las RTU |
| Z3 Subestación SS-3 | estación remota (dirección DNP3 10), relés de protección | Pérdida del telecontrol; la protección está separada | DNP3 sobre la MPLS del operador a través de fep-01 |
| Z4 BMS del hospital | bms-server, controladores | Pérdida de las alarmas de ventilación y de presión | Solo supervisado; el KVROC tiene acceso de lectura |
| Z5 Gestión (10.90.0.0/24) | jump-01, ntp-ops, ad-ops, colector | Un compromiso alcanza todas las zonas | Máximo privilegio |
| Z6 Corporativa (10.30.0.0/16) | puestos, correo, servidor de informes | Perturbación del negocio | Conectada a internet |

Entre los conductos declarados están: C1 Z2 scada-01 → Z1 tcp/502 sondeos de lectura; C2 Z2 eng-ws-15 → Z1 tcp/502 escrituras durante ventanas aprobadas; C3 Z5 jump-01 → Z2 tcp/22; C4 Z2 hist-02 → servidor de informes de Z6, envío HTTPS del CSV diario. El Lab 2 ya mostró una ruta **no declarada**: puesto de Z6 → Z1 tcp/502. En el modelo aparece como una línea roja con una pregunta: ¿qué regla la permite y desde cuándo? El capítulo 10 lo responde.

### 6.5 Actividad práctica

Amplíe el modelo con dos conductos para Z3 (de fep-01 a la estación remota y la ruta de soporte remoto del proveedor) y uno para Z4. Para cada uno, registre la finalidad, el protocolo, el iniciador, el responsable, el punto de aplicación y el punto de supervisión. Señale qué conductos podría aprovechar un único equipo de Z5 comprometido. Para la ruta de soporte remoto del proveedor hacia Z3, registre si termina en el servidor de salto o llega directamente a la estación remota. Para Z4, indique que el KVROC solo tiene acceso de lectura. Enumere después cuáles de esos conductos podría abrir un servidor de salto comprometido en Z5 y qué controles seguirían aplicándose.

### 6.6 Errores comunes y límites

- Zonas dibujadas por subred IP en lugar de por consecuencia y confianza.
- Conductos sin responsable ni finalidad, que nadie podrá retirar más tarde.
- Omitir la zona de gestión porque es «TI».
- Modelar el sistema de seguridad funcional como un controlador normal.
- Un modelo que nunca se compara con el tráfico observado; el capítulo 11 lo hace.
- Copiar el modelo de zonas de otra instalación sin comprobar cuáles de sus conductos existen realmente en esta.

- Dibujar las zonas solo por subred cuando dos equipos de la misma subred tienen consecuencias distintas.
- Poner una función de seguridad funcional o de protección en la misma zona que los controladores de supervisión corrientes.

### Ejercicios — capítulo 6

**EX021 — Sitúe los activos.** *Objetivo:* asignar zonas según la consecuencia. *Entradas:* un router celular en KW-06; la pasarela de soporte remoto del proveedor para SS-3; el servidor de informes; un portátil que usan los ingenieros de Kestrel Water en las estaciones. *Pasos:* asigne cada uno a una zona (existente o nueva) y justifíquelo. *Evidencia esperada:* cuatro ubicaciones. *Rúbrica:* 3 = router en el límite de Z1, con su gestión tratada como privilegio de nivel Z5; pasarela del proveedor en su propia zona de acceso remoto, no en Z3; servidor de informes en Z6; portátil de ingeniería como activo transitorio con sus propios controles (capítulo 16); 2 = una débil; 1 = solo por subred; 0 = nada.

**EX022 — Redacte un conducto.** *Objetivo:* declarar una ruta por completo. *Entradas:* hist-02 debe enviar un CSV diario al servidor corporativo de informes. *Pasos:* escriba la entrada del conducto con todos sus campos. *Evidencia esperada:* una entrada completa. *Rúbrica:* 3 = iniciado desde Z2 hacia fuera (envío, no extracción desde la red corporativa), HTTPS hacia un equipo y un puerto nombrados, finalidad, responsable, regla de aplicación y punto de supervisión nombrados, fecha de revisión; 2 = falta uno; 1 = «permitir hist hacia corporativa»; 0 = nada.

**EX023 — Contraste entre sectores.** *Objetivo:* reconocer las diferencias técnicas. *Entradas:* una propuesta de aplicar el mismo calendario semanal de parches y reinicios a scada-01, al procesador de comunicaciones de SS-3 y al servidor del BMS del hospital. *Pasos:* explique para cada sector qué debe comprobarse primero. *Evidencia esperada:* tres párrafos breves. *Rúbrica:* 3 = agua: redundancia e interrupción del sondeo; red eléctrica: ventanas de telecontrol acordadas con la sala de control de la red, sin efecto sobre la protección; hospital: restricciones de la ingeniería clínica y del fabricante, continuidad de las alarmas de ventilación; 2 = genérico; 1 = acepta un único calendario; 0 = nada.

**EX024 — Modelo frente a captura.** *Objetivo:* comparar lo declarado con lo observado. *Entradas:* la salida del Lab 2 y la lista de conductos de 6.4. *Pasos:* enumere cada flujo observado que no explique un conducto declarado. *Evidencia esperada:* lista con motivos. *Rúbrica:* 3 = las escrituras del puesto corporativo (sin conducto), posiblemente la consulta de identificación del dispositivo si ningún conducto la cubre, las tramas mal formadas desde scada-01 como anomalía que explicar; 2 = solo las escrituras; 1 = no encuentra ninguno; 0 = nada.

### Síntesis del capítulo

El modelo del sistema reúne activos, zonas, conductos y consecuencias en un único mapa. Dice lo que debería ocurrir, de modo que cualquier otra cosa se vuelve visible como hallazgo. Los sectores difieren en protocolos, tiempos y en quién puede cambiar qué, y las funciones de seguridad funcional y de protección se mantienen separadas de todo lo que toca un técnico.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Siga estudiando — capítulo 06 de 18

[← Capítulo 05](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Infraestructura crítica y seguridad sectorial: datos y telemetría

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- nombrar las fuentes de telemetría que usa un técnico en un entorno de control (datos del proceso, registros de dispositivos, registros del cortafuegos y de los equipos, registros de flujos, capturas pasivas) y lo que cada una puede mostrar y lo que no;
- analizar syslog RFC 5424, calcular la instalación y la severidad a partir del valor de prioridad y tratar las líneas que no son RFC 5424;
- medir y corregir los desfases de reloj frente a una referencia NTP y construir una única cronología en UTC;
- explicar cómo un reloj sin corregir invierte la causa y el efecto.

El capítulo 6 dijo dónde están las cosas. Este capítulo trata de lo que le cuentan y de si usted puede poner sus relatos en el orden correcto.

### 7.1 Fuentes y puntos ciegos

| Fuente | Muestra | No muestra |
|---|---|---|
| Datos del proceso (historiador) | Valores y alarmas a lo largo del tiempo | Quién causó un cambio |
| Registros de eventos de la HMI y del SCADA | Acciones del operador, reconocimientos de alarmas | Acciones realizadas directamente sobre el controlador |
| Registros del controlador/RTU | Sesiones de configuración, cambios de modo (si se admiten y están activados) | A menudo nada; muchos dispositivos registran poco |
| Registros del cortafuegos | Conexiones permitidas y denegadas en el límite | Tráfico dentro de una zona |
| Registros de los equipos (servidor de salto, servidores) | Inicios de sesión, órdenes, eventos de servicio | Actividad en dispositivos sin registro |
| Captura pasiva / registros de flujos | Quién habló con quién y con qué función | Contenido cifrado; tráfico que no pasa por el sensor |

La guía de gestión de registros del NIST describe la recogida, la conservación y la protección de estos registros ([SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final)). La primera tarea del técnico es saber qué fuente responde a qué pregunta, y qué preguntas no responde ninguna fuente.

### 7.2 Estructura de syslog

La RFC 5424 define el formato moderno de syslog: `<PRI>VERSION TIMESTAMP HOSTNAME APP-NAME PROCID MSGID STRUCTURED-DATA MSG` ([RFC 5424](https://www.rfc-editor.org/rfc/rfc5424)). El valor de prioridad es *instalación × 8 + severidad*: `<38>` es la instalación 4 (seguridad/autorización), severidad 6 (informativa). La marca de tiempo es RFC 3339 con desfase, y un guion (`-`) significa «nulo»; en una marca de tiempo, *el emisor no conocía la hora*. Muchos dispositivos siguen enviando el formato BSD antiguo (`<13>Oct 11 23:15:02 host app: ...`), sin año ni zona; cuente esas líneas y analícelas por separado en lugar de descartarlas.

### 7.3 Tiempo

Una cronología solo es tan buena como sus relojes. NTP (RFC 5905) permite a los equipos medir su **desfase** respecto a una referencia ([RFC 5905](https://www.rfc-editor.org/rfc/rfc5905)). En los entornos de control, algunos dispositivos no tienen cliente NTP, derivan varios minutos o están aislados deliberadamente de las fuentes de hora. Registre, para cada equipo que aporte datos a una cronología, su desfase medido en un momento conocido, y corrija sus marcas de tiempo restándolo: *corregida = notificada − (reloj del equipo − referencia)*. Convierta todo a UTC antes de ordenar; los desfases locales como `+01:00` son correctos, pero es fácil ordenarlos mal a simple vista.

### 7.4 Ejemplo resuelto: la secuencia de las 23:14 (sintético)

La noche del 11 de octubre, un operador informó de que la bomba 2 de KW-04 había arrancado de forma inesperada. Usted recogió seis líneas y midió los desfases de los relojes a la mañana siguiente (la RTU iba 212 s por detrás de la referencia). **Lab 7** (guárdelo como `lab07.py` y ejecútelo con `python3 lab07.py`):

```python
# Lab 7 - parse RFC 5424 syslog, correct clock offsets and build a UTC timeline (offline, stdlib)
# Synthetic lines from the Kestrel Vale operations centre; offsets measured against the NTP reference.
import re
from datetime import datetime, timedelta, timezone
lines = [
 "<38>1 2026-10-11T23:14:05.120Z fw-01 filterlog - - - block tcp 10.30.3.7:51544 -> 10.10.4.2:502",
 "<86>1 2026-10-12T00:13:58+01:00 jump-01 sshd 812 - - Accepted publickey for jtan from 10.90.0.40",
 "<134>1 2026-10-11T23:16:40Z hmi-02 hmi - - - operator setpoint change KW-04 PUMP2 start",
 "<38>1 2026-10-11T23:15:31Z rtu-kw04 auth - - - config session opened user=eng",
 "<13>Oct 11 23:15:02 eng-ws-15 app: project download started",
 "<38>1 - hist-02 histd - - - archive rollover",
]
offset_s = {"fw-01": 0.0, "jump-01": 0.4, "hmi-02": 0.0, "rtu-kw04": -212.0}   # host clock minus reference
pat = re.compile(r"^<(\d{1,3})>1 (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) ?(.*)$")
events, unparsed = [], []
for ln in lines:
    m = pat.match(ln)
    if not m: unparsed.append(("not RFC 5424", ln)); continue
    pri, ts, host, app, _pid, _msgid, _sd, msg = m.groups()
    if ts == "-": unparsed.append(("no timestamp", ln)); continue
    t = datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)
    t_corr = t - timedelta(seconds=offset_s.get(host, 0.0))
    fac, sev = divmod(int(pri), 8)
    events.append((t_corr, host, f"fac={fac} sev={sev}", msg, offset_s.get(host, 0.0)))
for t, host, fs, msg, off in sorted(events):
    note = f" (clock corrected {-off:+.1f} s)" if off else ""
    print(f"{t.strftime('%H:%M:%S.%f')[:-3]}Z {host:<9} {fs:<11} {msg}{note}")
for why, ln in unparsed: print("UNPARSED", why, "|", ln)
```

Salida esperada (Python 3.13.5):

```text
23:13:57.600Z jump-01   fac=10 sev=6 Accepted publickey for jtan from 10.90.0.40 (clock corrected -0.4 s)
23:14:05.120Z fw-01     fac=4 sev=6 block tcp 10.30.3.7:51544 -> 10.10.4.2:502
23:16:40.000Z hmi-02    fac=16 sev=6 operator setpoint change KW-04 PUMP2 start
23:19:03.000Z rtu-kw04  fac=4 sev=6 config session opened user=eng (clock corrected +212.0 s)
UNPARSED not RFC 5424 | <13>Oct 11 23:15:02 eng-ws-15 app: project download started
UNPARSED no timestamp | <38>1 - hist-02 histd - - - archive rollover
```

Antes de la corrección, la línea de la RTU (23:15:31Z) aparecía *antes* del cambio de punto de consigna en la HMI (23:16:40Z), lo que sugería que alguien configuró la RTU y que después actuó el operador. Tras la corrección, la sesión de la RTU ocurrió a las 23:19:03Z, **después** de la orden de arranque del operador. El relato pasa de «alguien manipuló primero» a «una sesión de ingeniería siguió a la acción del operador», lo que lleva a otra pregunta (quién abrió una sesión de configuración a las 23:19 y por qué). Dos líneas no pudieron situarse: la línea en formato BSD de la estación de ingeniería no tiene año ni zona, y la línea del historiador tiene una marca de tiempo nula. Se notifican, no se descartan; el «project download started» de la estación de ingeniería es posiblemente la línea más importante de todas, y situarla requiere su propia comprobación de reloj y los registros locales de la estación de trabajo.

### 7.5 Actividad práctica

Mida el desfase de una máquina de su propiedad frente a un servidor NTP público o local (por ejemplo, `chronyc tracking` o `ntpq -p` en Linux, `w32tm /stripchart` en Windows), regístrelo con la hora de la medición y repita al cabo de 24 horas para ver la deriva. Registre el equipo, la referencia, el desfase y la hora de la medición. Al cabo de veinticuatro horas, compare el nuevo desfase con el anterior para ver la deriva. Guarde ambas lecturas junto con el trabajo de cronología del Lab 7, para que una investigación posterior sepa cuán incierta sería una corrección hecha a partir de una sola medición.

### 7.6 Errores comunes y límites

- Ordenar por el texto de marcas de tiempo con desfases mezclados.
- Corregir los relojes en el sentido equivocado; escriba cada vez que la corregida es igual a la notificada menos el desfase.
- Descartar las líneas que no se analizan; cuéntelas y notifíquelas.
- Suponer que un desfase medido hoy se aplicaba anoche; la deriva y la resincronización lo cambian, así que indique la incertidumbre.
- Suponer que la ausencia de una línea de registro significa la ausencia de un evento; muchos dispositivos sencillamente no registran.
- Fusionar registros de dispositivos cuyos desfases se midieron en momentos distintos sin anotar la hora de cada medición junto a su desfase.
- Dar una hora corregida al segundo cuando el propio desfase solo se conoce con un margen de unos segundos.

### Ejercicios — capítulo 7

**EX025 — Decodifique prioridades.** *Objetivo:* calcular la instalación y la severidad. *Entradas:* `<86>`, `<134>`, `<11>`, `<165>`. *Pasos:* calcule cada una. *Evidencia esperada:* cuatro pares con sus nombres. *Rúbrica:* 3 = 86 → 10/6 (authpriv, informativa); 134 → 16/6 (local0, informativa); 11 → 1/3 (user, error); 165 → 20/5 (local4, aviso); 2 = aritmética correcta, faltan los nombres; 1 = parcial; 0 = nada.

**EX026 — Corrija un reloj.** *Objetivo:* aplicar la fórmula del desfase. *Entradas:* fep-01 registra un evento a las 02:10:00Z; su desfase, medido una hora después, era de +47 s (el equipo iba adelantado). *Pasos:* dé la hora corregida y la incertidumbre que indicaría. *Evidencia esperada:* hora corregida y una frase sobre la incertidumbre. *Rúbrica:* 3 = 02:09:13Z; incertidumbre porque el desfase se midió más tarde y la deriva es desconocida, p. ej., «± unos segundos; desfase medido a las 03:10Z»; 2 = hora correcta sin incertidumbre; 1 = sentido equivocado; 0 = nada.

**EX027 — Sitúe la línea BSD.** *Objetivo:* tratar con seguridad los formatos heredados. *Entradas:* la línea de `eng-ws-15` del Lab 7. *Pasos:* enumere lo que necesita para situarla en la cronología y escriba la regla de análisis que añadiría. *Evidencia esperada:* lista y regla. *Rúbrica:* 3 = el año a partir del contexto de la recogida, la zona horaria configurada en el equipo y su desfase medido; analizar con asignación explícita de zona y marcar el resultado como «zona supuesta»; 2 = regla sin registrar las suposiciones; 1 = descartarla; 0 = nada.

**EX028 — Pregunta de punto ciego.** *Objetivo:* emparejar preguntas con fuentes. *Entradas:* «¿Escribió alguien en KW-04 directamente desde el puerto local para portátil de la estación?». *Pasos:* indique qué fuentes podrían responderla, cuáles no y qué tendría que añadir. *Evidencia esperada:* análisis breve. *Rúbrica:* 3 = el cortafuegos y la captura del centro de control no pueden ver el tráfico local de la estación; los registros de la RTU podrían, si registra la configuración y las escrituras; añadir un sensor en la estación o el registro de la RTU y los registros de acceso físico; 2 = en parte; 1 = «revisar el cortafuegos»; 0 = nada.

### Síntesis del capítulo

La telemetría es un conjunto de testigos parciales. Sepa lo que puede ver cada fuente, analice los formatos de forma estricta contando lo que no puede analizar y corrija cada reloj frente a una referencia antes de ordenar los eventos. Una cronología construida sobre relojes sin corregir puede invertir la causa y el efecto; una construida sobre relojes corregidos, con sus incertidumbres indicadas, es evidencia.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Siga estudiando — capítulo 07 de 18

[← Capítulo 06](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Infraestructura crítica y seguridad sectorial: modos de fallo

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- nombrar los modos de fallo técnicos habituales de la telemetría y del control (laguna, valor congelado, pico, deriva, fuera de rango, marca de tiempo obsoleta, pérdida de la autoridad de control) y sus causas habituales;
- detectarlos en una serie temporal con reglas sencillas y explicables;
- explicar por qué un valor dentro de rango puede seguir siendo falso y por qué un valor perfectamente constante es sospechoso;
- mantener abiertas a la vez las hipótesis de fallo y de ataque hasta que la evidencia las separe.

El capítulo 7 puso los eventos en orden. Este capítulo pregunta de cada medición: ¿es verdadera? Muchos eventos de seguridad aparecen primero como «datos erróneos», y muchos eventos de datos erróneos son fallos corrientes. Un técnico debe reconocer ambos.

### 8.1 Un catálogo de modos de fallo

| Modo | Aspecto | Causas corrientes | Causas relevantes para la seguridad |
|---|---|---|---|
| **Laguna** | Muestras que faltan | Caída del enlace, sobrecarga del sondeo (capítulo 1), reinicio del dispositivo | Tráfico bloqueado o descartado, denegación de servicio |
| **Congelado / línea plana** | Valores idénticos durante más tiempo del que el proceso permite | Sensor congelado, entrada analógica averiada, SCADA que sirve el último valor conocido | Valores reproducidos o congelados que ocultan un cambio real |
| **Pico** | Un salto más rápido de lo que permite la física | Ruido eléctrico, error de escalado, muestra errónea | Valor inyectado |
| **Deriva** | Divergencia lenta respecto a la realidad | Ensuciamiento del sensor, antigüedad de la calibración | Manipulación lenta (rara, difícil de detectar) |
| **Fuera de rango** | Valor imposible | Fallo de cableado, escalado erróneo | Valor fabricado |
| **Marca de tiempo obsoleta** | Valor con una hora antigua o futura | Error de reloj (capítulo 7), datos en búfer | Reproducción |
| **Pérdida de la autoridad de control** | Órdenes no ejecutadas o ejecutadas por otra persona | Selector local/remoto dejado en local, enclavamiento | Escritura no autorizada |

El sentido de la tabla no es que toda laguna sea un ataque. Es que el mismo síntoma tiene ambos tipos de causa, de modo que las detecciones deben notificar el **síntoma** con precisión, y la investigación (capítulo 13) separa las causas.

### 8.2 Reglas que se explican solas

Cada detección de este capítulo es una regla que una persona puede leer y verificar:

- **Laguna**: más de *N* muestras consecutivas que faltan, donde *N* se fija a partir del ciclo de sondeo y de la tolerancia del proceso.
- **Congelado**: más de *M* lecturas consecutivas idénticas, donde *M* refleja cuánto varía de forma natural un sensor sano. Un analizador de cloro que informa exactamente de 0,62 durante veinte minutos es sospechoso, porque los analizadores reales fluctúan en su último dígito.
- **Pico**: un cambio entre muestras consecutivas mayor que el **paso máximo físicamente verosímil**; un depósito de 12 m no puede subir 6,8 m en un minuto. Esto detecta valores que las comprobaciones de rango no ven.
- **Rango**: fuera de los límites del instrumento o del proceso (capítulo 4).

Estas reglas son toscas pero transparentes: cuando una se dispara, todo el mundo puede ver por qué. Los detectores de anomalías estadísticos o aprendidos pueden añadir sensibilidad más adelante; no deben sustituir a reglas que los operadores entienden.

### 8.3 Dentro de rango no es verdadero

Un valor de 9,80 m en un depósito de 12 m supera todas las comprobaciones de rango. Si el minuto anterior marcaba 2,96 m y el siguiente 2,97 m, el 9,80 es imposible como medición. A la inversa, un valor constante siempre está «dentro de rango». Las comprobaciones de rango protegen contra lo absurdo; las de **velocidad de cambio** y **variación** protegen contra lo falso de apariencia verosímil. Use un paso máximo derivado del proceso, como medio metro por minuto para el nivel de un depósito, para que una única muestra disparatada se detecte aunque esté dentro del rango del instrumento. Escriba el límite de paso junto al límite de rango en el esquema de la etiqueta y revise ambos después de cada falsa alarma.

### 8.4 Ejemplo resuelto: cuatro etiquetas, veinte minutos (sintético)

**Lab 8** (guárdelo como `lab08.py` y ejecútelo con `python3 lab08.py`):

```python
# Lab 8 - classify telemetry failure modes (offline, standard library only)
# Synthetic one-minute readings from four Kestrel Water tags, 06:00-06:19Z on 2026-10-12.
series = {
 "KW-01 LEVEL_M": [3.40,3.41,3.41,3.42,3.43,3.43,3.44,3.45,3.45,3.46,3.47,3.47,3.48,3.49,3.49,3.50,3.51,3.51,3.52,3.53],
 "KW-02 CL2_MGL": [0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62],
 "KW-05 FLOW_LS": [41.0,40.8,41.2,40.9,None,None,None,None,None,None,None,41.1,40.7,41.0,41.3,40.9,41.2,41.0,40.8,41.1],
 "KW-07 LEVEL_M": [2.95,2.96,2.95,2.97,2.96,2.96,9.80,2.97,2.96,2.98,2.97,2.97,2.98,2.97,2.99,2.98,2.98,2.99,2.98,2.99],
}
LIMITS = {"LEVEL_M": (0.0, 12.0), "CL2_MGL": (0.0, 5.0), "FLOW_LS": (0.0, 400.0)}
MAX_STEP = {"LEVEL_M": 0.5, "CL2_MGL": 0.3, "FLOW_LS": 25.0}   # physically plausible change per minute
STUCK_MIN, GAP_MIN = 15, 5
for name, xs in series.items():
    tag = name.split()[1]; lo, hi = LIMITS[tag]; out = []
    run, longest = 0, 0
    for i in range(len(xs)):                     # gaps
        run = run + 1 if xs[i] is None else 0; longest = max(longest, run)
    if longest >= GAP_MIN: out.append(f"gap: {longest} consecutive missing minutes")
    vals = [(i, v) for i, v in enumerate(xs) if v is not None]
    same, best = 1, 1
    for (i0, a), (i1, b) in zip(vals, vals[1:]):  # stuck / flatline (exact repeats)
        same = same + 1 if a == b else 1; best = max(best, same)
        if abs(b - a) > MAX_STEP[tag] and i1 - i0 == 1:
            out.append(f"spike: 06:{i1:02d}Z jump {a} -> {b} exceeds {MAX_STEP[tag]}/min")
    if best >= STUCK_MIN: out.append(f"stuck: {best} identical readings in a row")
    out += [f"range: {v} outside {lo}-{hi}" for _, v in vals if not lo <= v <= hi]
    print(f"{name:<14} {'; '.join(out) if out else 'no failure mode detected'}")
```

Salida esperada (Python 3.13.5):

```text
KW-01 LEVEL_M  no failure mode detected
KW-02 CL2_MGL  stuck: 20 identical readings in a row
KW-05 FLOW_LS  gap: 7 consecutive missing minutes
KW-07 LEVEL_M  spike: 06:06Z jump 2.96 -> 9.8 exceeds 0.5/min; spike: 06:07Z jump 9.8 -> 2.97 exceeds 0.5/min
```

KW-01 se comporta como un depósito que se llena lentamente: ningún hallazgo. El cloro de KW-02 es idéntico en las veinte lecturas: o bien el analizador se ha congelado, o la RTU devuelve un valor almacenado, o el valor lo está suministrando algo distinto del analizador. KW-05 tiene una laguna de siete minutos: compruebe primero el enlace y el sondeo (capítulo 13). KW-07 muestra una desviación de una sola muestra hasta 9,80 m y de vuelta: un fallo típico de ruido o de escalado, pero también exactamente el aspecto que tendría una escritura inyectada puntual en un registro de notificación. Cada línea es un síntoma con una descripción precisa; ninguna es todavía una causa.

### 8.5 Elegir los umbrales

Fije los umbrales a partir de la evidencia, no de conjeturas: examine una semana de datos sanos por etiqueta, encuentre el mayor paso natural y la racha natural más larga de valores idénticos, y fije la regla por encima de ellos con un margen. Anote el motivo junto a la cifra y revise tras cada falsa alarma y cada evento no detectado. Una regla de valor congelado sobre una etiqueta que legítimamente se queda en 0,00 (una bomba parada) necesita una condición; por ejemplo, aplicarla solo mientras la bomba funciona.

### 8.6 Actividad práctica

Añada al Lab 8 una comprobación de **deriva**: compare la media de cada etiqueta en los primeros cinco minutos con su media en los últimos cinco y marque un cambio mayor que un límite específico de la etiqueta. Explique por qué la subida constante de KW-01 *no* debería marcarse y qué información adicional (estado de la bomba, caudal de entrada) haría significativa la detección de derivas. La subida constante de KW-01 es comportamiento del proceso mientras una bomba llena el depósito, así que una comparación ingenua de medias la marcaría erróneamente. La deriva adquiere sentido cuando se conoce el estado de la bomba o el caudal de entrada, o cuando se comparan dos sensores que deberían coincidir. Fije el límite específico de la etiqueta a partir de una semana de datos sanos y anote el motivo junto a la cifra.

### 8.7 Errores comunes y límites

- Tratar todo valor erróneo como un ataque, o ninguno.
- Solo comprobaciones de rango.
- Reglas de valor congelado sobre etiquetas que legítimamente permanecen quietas.
- Umbrales sin justificación registrada.
- El Lab 8 ve una serie cada vez; una investigación real compara etiquetas relacionadas (una bomba en marcha con caudal cero es una incoherencia entre etiquetas).

- Aplicar una regla de valor congelado a una etiqueta que legítimamente se queda en cero mientras una bomba está parada.
- Fijar los umbrales a partir de una conjetura en lugar de a partir de datos sanos con una justificación registrada.
- Investigar una serie de forma aislada cuando un bit de bomba en marcha y un caudal cero mostrarían un fallo entre etiquetas.

### Ejercicios — capítulo 8

**EX029 — Nombre el modo.** *Objetivo:* clasificar síntomas. *Entradas:* (a) el nivel sube 0,01 m/min mientras la válvula de entrada indica que está cerrada; (b) el caudal marca 0,00 durante 40 minutos mientras la bomba 1 indica que está en marcha; (c) el historiador muestra valores con marcas de 03:00–03:10 que llegaron a las 03:25; (d) la bomba 2 no arranca tras una orden de la HMI y la RTU indica «local». *Pasos:* nombre el modo y dos causas candidatas de cada uno. *Evidencia esperada:* cuatro filas. *Rúbrica:* 3 = (a) incoherencia entre etiquetas/deriva: fallo de la realimentación de la válvula o fuga/derivación; (b) congelado o incoherencia entre etiquetas: caudalímetro averiado o valor congelado; (c) datos en búfer/obsoletos: caída del enlace con almacenamiento y reenvío, o reproducción; (d) pérdida de la autoridad de control: selector local en la instalación, o enclavamiento; 2 = modos correctos, causas escasas; 1 = parcial; 0 = nada.

**EX030 — Prediga un cambio de regla.** *Objetivo:* razonar sobre los umbrales. *Entradas:* el Lab 8 con `STUCK_MIN = 25` y `MAX_STEP["LEVEL_M"] = 7.0`. *Pasos:* prediga la nueva salida y después ejecute. *Evidencia esperada:* predicción y salida real. *Rúbrica:* 3 = KW-02 ya no se marca (20 < 25), el pico de KW-07 ya no se marca (6,84 < 7,0, 6,83 < 7,0), la laguna de KW-05 se sigue marcando; explica lo que se pierde; 2 = casi todo correcto; 1 = conjeturas; 0 = nada.

**EX031 — Regla de valor congelado condicional.** *Objetivo:* reducir las falsas alarmas. *Entradas:* una etiqueta de caudal marca legítimamente 0,0 cuando su bomba está parada. *Pasos:* escriba la regla en pseudocódigo usando el estado de la bomba. *Evidencia esperada:* regla y un caso de prueba. *Rúbrica:* 3 = aplicar la detección de valor congelado solo mientras el estado de la bomba = en marcha durante al menos el intervalo de sondeo; incluye una prueba con la bomba parada (sin alerta) y en marcha con caudal constante distinto de cero (alerta); 2 = sin prueba; 1 = desactiva la regla; 0 = nada.

**EX032 — Plan de fallo o ataque.** *Objetivo:* mantener abiertas ambas hipótesis. *Entradas:* KW-02 congelado en 0,62. *Pasos:* enumere tres comprobaciones que apuntarían a un fallo y tres que apuntarían a una manipulación, todas de solo lectura. *Evidencia esperada:* seis comprobaciones. *Rúbrica:* 3 = fallo: pantalla local del analizador, diagnóstico de la entrada analógica de la RTU, registros de mantenimiento; manipulación: escrituras inesperadas en el registro de notificación en las capturas, registros de sesiones de configuración, comparación con una muestra manual tomada por operaciones; 2 = un lado escaso; 1 = solo una hipótesis; 0 = nada.

### Síntesis del capítulo

La telemetría falla de un pequeño número de maneras reconocibles, y cada síntoma tiene causas tanto corrientes como maliciosas. Detecte los síntomas con reglas transparentes (laguna, congelado, pico, rango) cuyos umbrales procedan de datos sanos y cuyos motivos estén escritos. Estar dentro de rango no es lo mismo que ser verdadero. Notifique el síntoma con precisión y deje la causa a la investigación.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Siga estudiando — capítulo 08 de 18

[← Capítulo 07](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Infraestructura crítica y seguridad sectorial: herramientas y métodos

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- elegir la herramienta técnica adecuada para una pregunta en un entorno de control: exportación de configuración, captura pasiva, decodificador de protocolos, consulta de registros, herramienta de ingeniería del fabricante o prueba activa;
- implementar y verificar una comprobación de integridad a partir de sus parámetros publicados, con el CRC de la capa de enlace de DNP3 como ejemplo;
- explicar la diferencia entre un **código de detección de errores** y la **autenticación**, y por qué un CRC válido no demuestra nada sobre quién envió una trama;
- validar una herramienta antes de confiar en ella: pruebas de respuesta conocida, pruebas negativas y versiones documentadas.

Los capítulos 7 y 8 usaron la telemetría. Este capítulo trata de los propios instrumentos: cómo elegirlos, cómo construir bien los pequeños y cómo saber cuándo mienten.

### 9.1 Elegir un método

| Pregunta | Preferir | Evitar salvo con alcance definido |
|---|---|---|
| ¿Qué está configurado? | Exportación de configuración, vista de solo lectura de la herramienta del fabricante | Sondear puertos para deducir la configuración |
| ¿Quién habla con quién? | Registros de flujos, captura pasiva en un puerto SPAN o un derivador (*tap*) | Escaneo activo |
| ¿Qué ejecuta un dispositivo? | Registros de activos, inventario de la herramienta de ingeniería durante una sesión aprobada | Identificación de huellas mediante sondeo |
| ¿Funciona una regla de denegación? | Registros del cortafuegos más una prueba de conexión delimitada | Escaneos amplios |
| ¿Está bien formada una trama? | Decodificador con comprobaciones del protocolo (capítulo 2, este capítulo) | Mirar el hexadecimal a ojo |

La guía de seguridad de TO NIST SP 800-82 Rev. 3 trata la supervisión pasiva y los riesgos de las técnicas activas ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). Los analizadores de paquetes como Wireshark incluyen disectores para Modbus y DNP3; sus propios scripts sirven para las comprobaciones que esas herramientas no hacen por usted y para una automatización repetible y revisable.

### 9.2 DNP3 en la capa de enlace

DNP3 se usa ampliamente en el telecontrol eléctrico y del agua. Cada trama de la capa de enlace empieza con una cabecera de 10 bytes: los bytes de inicio `05 64`, un byte de **longitud**, un byte de **control**, una dirección de **destino** de 2 bytes y una de **origen** de 2 bytes (*little-endian*), y un **CRC** de 2 bytes. Los datos de usuario siguen en bloques de hasta 16 bytes, cada uno con su propio CRC. En el byte de control, el bit 7 (DIR) está activado en las tramas que envía la maestra, el bit 6 (PRM) en las tramas primarias (iniciadoras), y los cuatro bits bajos son el código de función del enlace; por ejemplo, primaria 0 «reiniciar los estados del enlace», primaria 4 «datos de usuario no confirmados», secundaria 11 «estado del enlace». El DNP Users Group publica una visión general; la norma completa es IEEE 1815 ([DNP3 overview](https://www.dnp.org/About/Overview-of-DNP3-Protocol)).

El CRC es **CRC-16/DNP**: polinomio 0x3D65, valor inicial 0, entrada y salida reflejadas, XOR final 0xFFFF, con el valor de comprobación del catálogo 0xEA82 para la cadena ASCII `123456789` ([CRC catalogue](https://reveng.sourceforge.io/crc-catalogue/16.htm)). Reflejado, el polinomio es 0xA6BC, que es la constante que se usa en una implementación bit a bit.

### 9.3 Valide primero la herramienta

Una rutina de CRC sutilmente errónea sigue produciendo números. Antes de usarla, ejecute una **prueba de respuesta conocida**: calcule el CRC de `123456789` y compárelo con 0xEA82. Después, una **prueba negativa**: cambie un bit de una trama válida y confirme que la comprobación falla. El Lab 9 hace ambas (la línea `assert` es la prueba de respuesta conocida), y anote la versión de Python, porque el resultado de cualquier herramienta solo es evidencia si la herramienta está identificada. Mantenga en el script el assert que comprueba el valor del catálogo y haga fallar la tarea si deja de cumplirse tras un cambio en la función de CRC. Anote la versión de Python junto a cada resultado que vaya a usarse como evidencia. Ejecute la prueba negativa sobre una trama que haya corrompido usted mismo, para saber que el comprobador rechaza los CRC erróneos antes de confiar en él sobre una captura.

### 9.4 Detectar errores no es autenticar

Un CRC se calcula a partir de parámetros públicos; cualquiera que pueda enviar una trama puede calcular un CRC válido. Detecta la corrupción accidental, no la falsificación. El Lab 9 lo muestra directamente: una trama de una dirección de origen desconocida (77) tiene un CRC **válido**. Distinguir lo auténtico de lo falsificado exige autenticación criptográfica (DNP3 Secure Authentication o un túnel protegido) o contexto: direcciones de origen conocidas, rutas conocidas, tiempos esperados. Compárelo con el capítulo 15 del libro de tecnólogo, que usa HMAC (RFC 2104) para la autenticidad ([RFC 2104](https://www.rfc-editor.org/rfc/rfc2104)).

### 9.5 Ejemplo resuelto: comprobación de las cabeceras de SS-3 (sintético)

La maestra de Kestrel Grid (dirección DNP3 1) sondea la estación remota de la subestación SS-3 (dirección 10) a través de fep-01. Un técnico capturó seis cabeceras de enlace. **Lab 9** (guárdelo como `lab09.py` y ejecútelo con `python3 lab09.py`):

```python
# Lab 9 - check DNP3 link-layer headers and their CRC (offline, standard library only)
# CRC-16/DNP: poly 0x3D65 (reflected 0xA6BC), init 0x0000, reflected in/out, xorout 0xFFFF.
# Synthetic frames between the Kestrel Grid master (address 1) and substation SS-3 outstation (address 10).
import struct
def crc_dnp(data: bytes) -> int:
    crc = 0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA6BC if crc & 1 else crc >> 1
    return crc ^ 0xFFFF
assert crc_dnp(b"123456789") == 0xEA82          # catalogue check value
def header(length, ctrl, dest, src):
    h = bytes([0x05, 0x64, length, ctrl]) + struct.pack("<HH", dest, src)
    return h + struct.pack("<H", crc_dnp(h))
capture = [
    ("master->SS-3", header(0x05, 0xC0, 10, 1).hex()),     # primary function 0: reset link states
    ("SS-3->master", header(0x05, 0x0B, 1, 10).hex()),     # secondary function 11: link status
    ("master->SS-3", header(0x11, 0xC4, 10, 1).hex()),     # primary function 4: unconfirmed user data
    ("master->SS-3", "056411c40a000100" + "ffff"),          # wrong CRC
    ("unknown->SS-3", header(0x11, 0xC4, 10, 77).hex()),   # source not in station table
    ("master->SS-3", "0565" + header(0x05, 0xC0, 10, 1).hex()[4:]),  # bad start bytes
]
KNOWN_SOURCES = {1}
for label, hx in capture:
    b = bytes.fromhex(hx)
    if b[:2] != b"\x05\x64": print(f"{label:<14} {hx}  REJECT start bytes {b[:2].hex()}"); continue
    got = struct.unpack("<H", b[8:10])[0]; want = crc_dnp(b[:8])
    length, ctrl, dest, src = b[2], b[3], *struct.unpack("<HH", b[4:8])
    if got != want: print(f"{label:<14} {hx}  REJECT crc {got:04x} != {want:04x}"); continue
    direction = "from master" if ctrl & 0x80 else "from outstation"
    note = "" if src in KNOWN_SOURCES or src == 10 else "  ALERT unknown source address"
    print(f"{label:<14} {hx}  ok len={length} ctrl=0x{ctrl:02x} ({direction}, fc={ctrl & 0x0F}) dest={dest} src={src}{note}")
```

Salida esperada (Python 3.13.5):

```text
master->SS-3   056405c00a000100b1ac  ok len=5 ctrl=0xc0 (from master, fc=0) dest=10 src=1
SS-3->master   0564050b01000a006ded  ok len=5 ctrl=0x0b (from outstation, fc=11) dest=1 src=10
master->SS-3   056411c40a0001000615  ok len=17 ctrl=0xc4 (from master, fc=4) dest=10 src=1
master->SS-3   056411c40a000100ffff  REJECT crc ffff != 1506
unknown->SS-3  056411c40a004d0073e6  ok len=17 ctrl=0xc4 (from master, fc=4) dest=10 src=77  ALERT unknown source address
master->SS-3   056505c00a000100b1ac  REJECT start bytes 0565
```

Tres tramas son válidas y esperadas. Una tiene el CRC `ffff` donde se esperaba `1506`: corrupción o una trama fabricada; en un enlace ruidoso, una racha de fallos de CRC es un hallazgo de calidad del enlace para el proveedor de telecomunicaciones. Otra tiene bytes de inicio erróneos y se rechaza antes de leer nada más. La línea más importante es la que *supera* el CRC: la dirección de origen 77 no está en la tabla de estaciones. El CRC dice que los bytes llegaron intactos; solo la comprobación de la dirección dice que procedían de un lugar inesperado.

### 9.6 Actividad práctica

Amplíe el Lab 9 para verificar el CRC de cada bloque de datos de usuario de 16 bytes que sigue a la cabecera. Construya una trama con 17 bytes de datos de usuario (un bloque completo y un bloque de 1 byte), calcule los CRC de ambos bloques y corrompa un byte del segundo bloque para mostrar que la comprobación lo detecta. Construya la trama con un bloque completo de dieciséis bytes y un bloque de un byte, cada uno con su propio CRC. Corrompa un byte del segundo bloque y confirme que solo falla la comprobación de ese bloque. Guarde los pasos de construcción en las notas del laboratorio para que un revisor pueda reconstruir la misma trama.

### 9.7 Errores comunes y límites

- Confiar en un comprobador casero sin una prueba de respuesta conocida.
- Equivocarse con el orden de los bytes: las direcciones y el CRC de DNP3 son *little-endian*; los campos de Modbus son *big-endian*.
- Tratar «CRC válido» como «auténtico».
- Sondear activamente cuando una fuente pasiva responde a la pregunta.
- El Lab 9 solo comprueba las cabeceras; las capas de transporte y de aplicación llevan las órdenes y necesitan su propia decodificación.
- Decodificar una captura sin anotar la versión de la herramienta ni los ajustes de orden de bytes usados, de modo que nadie puede reproducir el resultado.

- Leer la ALERT del Lab 9 para la dirección de origen 77 como prueba de un ataque; solo muestra una dirección que falta en la lista de la maestra.

### Ejercicios — capítulo 9

**EX033 — Prueba de respuesta conocida.** *Objetivo:* validar una herramienta. *Entradas:* la función `crc_dnp` del Lab 9. *Pasos:* (1) sustituya `0xA6BC` por `0x3D65` y ejecute; (2) explique el resultado. *Evidencia esperada:* salida y explicación. *Rúbrica:* 3 = el assert falla porque un algoritmo con desplazamiento a la derecha (reflejado) necesita el polinomio reflejado; la prueba de respuesta conocida detectó un error verosímil antes de juzgar ninguna trama; 2 = observa el fallo sin explicarlo; 1 = intentado; 0 = nada.

**EX034 — Decodifique el byte de control.** *Objetivo:* leer los campos de enlace de DNP3. *Entradas:* los bytes de control 0xC9, 0x44 y 0x0B. *Pasos:* dé DIR, PRM y el código de función de cada uno y nombre la función. *Evidencia esperada:* tres filas. *Rúbrica:* 3 = 0xC9: DIR 1, PRM 1, fc 9 solicitar el estado del enlace; 0x44: DIR 0, PRM 1, fc 4 datos de usuario no confirmados desde una estación remota (por ejemplo, una respuesta no solicitada); 0x0B: DIR 0, PRM 0, fc 11 estado del enlace; 2 = uno erróneo; 1 = solo los bits; 0 = nada.

**EX035 — Experimento mental de falsificación.** *Objetivo:* separar integridad y autenticidad. *Entradas:* una trama con CRC válido, dirección de origen 1 y destino 10, que llega a la estación remota desde una dirección de la red MPLS que no es fep-01. *Pasos:* explique lo que muestra el CRC, lo que muestra la dirección y lo que establecería realmente la autenticidad. *Evidencia esperada:* explicación breve. *Rúbrica:* 3 = el CRC muestra que no hubo corrupción accidental; la dirección DNP3 1 la declara el propio emisor; la autenticidad requiere Secure Authentication o un túnel criptográfico que termine en extremos conocidos, más la aplicación de la ruta en la red; 2 = parcial; 1 = «CRC válido, luego auténtica»; 0 = nada.

**EX036 — Selección del método.** *Objetivo:* elegir el método menos intrusivo. *Entradas:* preguntas: (a) qué direcciones de maestra DNP3 ha visto SS-3 este mes; (b) si el cortafuegos de fep-01 solo permite la estación remota; (c) la versión de firmware de la estación remota. *Pasos:* elija un método para cada una y justifíquelo. *Evidencia esperada:* tres elecciones. *Rúbrica:* 3 = (a) captura pasiva o registros de fep-01 analizados con un decodificador; (b) exportación de configuración más registros y, después, una prueba delimitada si hace falta; (c) registro de activos o herramienta del fabricante durante una sesión aprobada con el acuerdo del ingeniero de protecciones; 2 = una elección intrusiva; 1 = escaneo; 0 = nada.

### Síntesis del capítulo

Elija el método menos intrusivo que responda a la pregunta y valide toda herramienta antes de confiar en ella: pruebas de respuesta conocida, pruebas negativas, versiones registradas. El CRC de la capa de enlace de DNP3 muestra esta disciplina en miniatura (implementarlo a partir de los parámetros publicados, comprobarlo con el valor del catálogo) y también su límite: la detección de errores demuestra que los bytes llegaron intactos, nunca quién los envió.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Siga estudiando — capítulo 09 de 18

[← Capítulo 08](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 →](../../en/book/MANUSCRIPT.md#ch-10)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resultados resueltos y notas de evaluación

Cada resultado resuelto muestra una respuesta defendible y lo que premia la rúbrica. Una respuesta distinta obtiene la máxima puntuación cuando cumple el mismo nivel de exigencia en cuanto a evidencia, alcance y honestidad sobre los límites. Los resultados numéricos proceden de los laboratorios sin conexión de este libro, ejecutados con Python 3.13.5 y solo con la biblioteca estándar; cuando un resultado depende de un laboratorio modificado, se describe la modificación para que pueda reproducirla. Todas las cifras describen datos sintéticos; no las presente nunca como hallazgos sobre operadores reales.

### Capítulo 1: EX001–EX004

**EX001 — Clasificación de rutas.** HMI → scada-01 «arrancar la bomba 2»: control; el peor caso es un arranque o una parada no autorizados de una bomba (desbordamiento, transitorio de presión). KW-04 → scada-01 lectura: supervisión; el peor caso es que los operadores actúen sobre un nivel falso. eng-ws-15 → KW-04 descarga del proyecto: gestión (e indirectamente control); el peor caso es la sustitución de la lógica del controlador, la acción más peligrosa de la lista, porque cambia lo que hace el controlador aunque no se envíe ninguna orden más. jump-01 → hist-02 SSH: gestión; el peor caso son registros históricos alterados o borrados, o un punto de apoyo en Z2. hist-02 → CSV corporativo: datos de supervisión que salen de la zona de control; el peor caso es la divulgación de datos operativos o, si se implementa como extracción iniciada desde fuera, una credencial corporativa dentro de Z2 (capítulo 15).

**EX002 — Corrija el ciclo sobre el papel.** Ejemplo: (1) sondear las cuatro estaciones de fibra y las cinco celulares por canales separados de los de las tres estaciones de radio (tres canales: fibra 0,31 s, celular 6,52 s, radio 4,50 s; el celular sigue siendo demasiado lento); (2) reducir los sondeos por ciclo de las celulares de 4 a 2 combinando las lecturas de registros en una sola petición (canal celular 3,26 s) y dar a KW-06 su propio canal (2 sondeos × 690 ms = 1,38 s; resto de celulares 1,88 s). Con canales de ≤ 4,5 s, todas las estaciones en buen estado cumplen los 5 s. Para limitar el efecto de una estación caída: un tiempo de espera de 800 ms sin reintento inmediato mantiene una KW-06 caída en 1,6 s en su propio canal. La máxima puntuación verifica editando `stations`, `TIMEOUT_MS` y la función `cycle` e informa de los valores impresos; cualquier configuración que se ejecute y cumpla el requisito obtiene puntuación si el tiempo de espera se justifica frente a la latencia real del enlace.

**EX003 — Impacto del túnel.** Secuencial: 5 estaciones celulares × 4 sondeos × 35 ms = 700 ms, de modo que 11,33 → 12,03 s. Canales por estación: el ciclo propio de cada estación celular sube 4 × 35 = 140 ms; KW-06 pasa a 2,90 s, todavía por debajo de 5 s. Recomendación: el túnel solo es aceptable junto con el rediseño de canales (EX002), y su latencia debe medirse en un piloto, no suponerse.

**EX004 — Lista de plataformas compartidas.** Servidores de virtualización: «¿Qué margen de capacidad queda si falla un servidor y qué invitados se reinician y dónde?». Directorio: «¿Quién está en los grupos de administradores y pueden los operadores iniciar sesión en la HMI si el directorio no está accesible?». Fuente de hora: «¿Cuál es la referencia, hay una segunda y se supervisa el desfase?». Colector de supervisión: «¿Qué ocurre cuando se llena su disco o se detiene? ¿Almacenan en búfer las fuentes y recibe alguien una alerta?».

### Capítulo 2: EX005–EX008

**EX005 — Decodificación a mano.** Trama 1: tid 0x0010 = 16, protocolo 0, longitud 6, unidad 1, función 16 (escribir varios registros), dirección inicial 10, cantidad 2; pero la función 16 debe llevar además un recuento de bytes (4) y cuatro bytes de valores, así que la PDU está incompleta; un analizador correcto la rechaza aunque la longitud MBAP coincida con los bytes presentes. Trama 2: tid 17, longitud 6, unidad 1, función 15 (escribir varias bobinas), dirección 0, cantidad 8; también le faltan su recuento de bytes (1) y el byte de bobinas. La máxima puntuación señala que las comprobaciones MBAP por sí solas no validan una PDU; cada función tiene su propia estructura.

**EX006 — Amplíe el decodificador.** En la rama de escritura: `if fc in (15, 16): bc = b[12]; data = b[13:13 + bc]` y, para la 16, `vals = struct.unpack(f">{qty}H", data)` tras comprobar `bc == 2 * qty and len(data) == bc`. Para la trama de 10.30.3.7 `...011000070002040064000a`, el recuento de bytes es 4 y los valores son 100 y 10: dos registros a partir del 7 (el punto de consigna y el registro siguiente).

**EX007 — Política de escritura como datos.** Normal: (10.20.0.10, 10.10.0.0/16, {1, 2, 3, 4}). Ventana de mantenimiento: añadir (10.20.0.15, la estación nombrada en la incidencia, {3, 5, 6, 15, 16}) solo durante la ventana. La guardia del KVROC activa y desactiva la política conforme a una incidencia aprobada por operaciones de Kestrel Water; la conmutación queda registrada y la ventana caduca automáticamente.

**EX008 — ¿Reconocimiento o funcionalidad?** La consulta diaria desde scada-01 es coherente con una funcionalidad de inventario; confírmelo en la documentación del fabricante del SCADA y añádala al modelo como flujo esperado. La ráfaga de tres segundos desde 10.20.0.31 es prioritaria: un equipo desconocido en Z2 que consulta la identificación de varias estaciones tiene forma de reconocimiento. Las primeras comprobaciones son de solo lectura: registros de DHCP y del conmutador para esa dirección, el inventario de activos, los registros del servidor de salto y del directorio para ese equipo. No lo sondee. El capítulo 17 muestra lo que hizo después.

### Capítulo 3: EX009–EX012

**EX009 — Gana el primer valor.** Si la línea comentada se descomenta donde está (después de `PasswordAuthentication yes`), el valor efectivo sigue siendo `yes`, porque sshd usa el primer valor que lee. La corrección debe sustituir la primera aparición (o borrarla) y confirmarse después con `sshd -T | grep -i passwordauthentication`.

**EX010 — Priorice los hallazgos de HIST-02.** Hoy: conservar `last`/`lastlog`/los registros de autenticación de `backup2` y `vendor`; eliminar `backup2` (UID 0) y quitar a `vendor` de `sudo` y de `ops-admins`. Esta semana, como un único cambio probado desde una sesión abierta: `ListenAddress 10.90.0.21`, `PermitRootLogin no`, `PasswordAuthentication no` (tras confirmar los inicios de sesión con clave de las dos personas autorizadas), `X11Forwarding no`, `MaxAuthTries 3`. Próxima ventana: cambiar el intérprete de `histsvc` a `/usr/sbin/nologin` tras comprobar las tareas programadas y los scripts. El acceso del proveedor pasa al proceso limitado en el tiempo del capítulo 10.

**EX011 — Amplíe la auditoría.** Añada dentro del bucle de passwd: `if name != "root" and home in ("/root", "/") and not shell.endswith("nologin"): findings.append(f"account {name} has interactive shell and home {home}")`. La salida añade `account backup2 has interactive shell and home /root`, findings 11. Un directorio personal compartido mezcla el historial del intérprete y las claves entre identidades, de modo que las acciones no pueden atribuirse.

**EX012 — Diseño de una cuenta de servicio.** UID de sistema (por ejemplo, 998), intérprete `/usr/sbin/nologin`, directorio personal `/opt/hist` propiedad de root y legible por el grupo `histsvc`; directorio de datos con escritura solo para `histsvc`; credencial de la base de datos en un archivo con modo 0400 propiedad de `histsvc`, o en el almacén de secretos de la plataforma; rotada anualmente y tras cualquier cambio de personal con acceso, con el equipo de plataforma del KVROC como responsable; la cuenta nunca la usan personas.

### Capítulo 4: EX013–EX016

**EX013 — Prediga antes de ejecutar.** KW-11 12.0 → aceptar (rango inclusivo); KW-12 `inf` → rechazar `value not finite` (línea 13); KW-02 −0.0 → aceptar. Resumen `{"accept": 4, "reject": 7, "quarantine": 2}` (verificado ejecutándolo). Normalice −0.0 a 0.0 antes de almacenarlo.

**EX014 — ¿Rechazar o poner en cuarentena?** (a) Cuarentena: interpretable pero fuera de rango; flujo inverso, desfase del sensor o manipulación. (b) Rechazar, salvo que el esquema defina explícitamente las unidades sin distinguir mayúsculas; no adivine nunca. (c) Aceptar; una alarma de proceso de nivel alto es la herramienta del operador, no la del validador. (d) Aceptar si está dentro de una tolerancia de reloj acordada (por ejemplo, 5 s); en caso contrario, cuarentena como problema de reloj.

**EX015 — JSON con trampas.** `json.loads('{"station": "KW-03", "value": NaN}')` devuelve `{'station': 'KW-03', 'value': nan}`. Defina `def no_const(c): raise ValueError(f"non-standard JSON constant {c}")` y llame a `json.loads(s, parse_constant=no_const)`; ahora lanza una excepción. La RFC 8259 no admite NaN ni Infinity.

**EX016 — Resumen para la supervisión.** Ejemplo: `{"accept": 2, "reject": 6, "quarantine": 2, "by_reason": {"not a number": 2, "unit": 1, "timestamp": 1, "not finite": 1, "field count": 1, "range": 1, "future": 1}, "by_station": {"KW-03": 1, ...}}`. Alerta: cualquier cuarentena de una etiqueta CL2_MGL, o rechazos por encima del 10 % de las filas en dos exportaciones consecutivas, o que falte por completo la exportación.

### Capítulo 5: EX017–EX020

**EX017 — Repare un alcance.** Defectos: «TI» no es el propietario del sistema (debe autorizar Kestrel Water); 10.10.0.0/16 son todas las estaciones; escaneo activo en una red de control; sin ventana ni hora; sin acciones permitidas; sin condiciones de parada; sin contactos; sin tratamiento de la evidencia. Reescritura: finalidad «establecer los servicios expuestos por las RTU de las estaciones»; método, primero a partir de los registros de activos, las exportaciones de configuración y una captura pasiva de 24 h; si queda una laguna, una prueba de conexión por puerto nombrado en una estación nombrada, en una ventana acordada y con la sala de control informada, autorizada por A. Mensah, con parada ante cualquier alarma y la evidencia con hash en la carpeta del caso.

**EX018 — Etiquete la nota.** *Observado:* sesión de configuración en la RTU de KW-09 a las 06:41Z (reloj corregido); las lecturas se interrumpieron a las 07:05Z. *Inferido:* posible cambio no aprobado; se desconoce quién lo hizo; «el proveedor» no está establecido. *Hecho:* RTU reiniciada a las 07:30Z por mí, sin conservación; la configuración en ejecución y el registro de la sesión previos al reinicio pueden haberse perdido. *Abierto:* quién abrió la sesión y por qué; si existe una exportación de configuración o una copia de seguridad de antes del reinicio; responsable L. Ferreira.

**EX019 — Registro de evidencia.** Qué: `fw-01-rules-20261013.txt` (exportación en bruto). Fuente: fw-01, CLI de gestión, versión de firmware registrada. Hora: 2026-10-13T08:12:40Z, equipo recolector sincronizado con ntp-ops (desfase +0,1 s). Recolector: R. Kaur. Método: la orden de exportación exacta. Integridad: la salida de `sha256sum fw-01-rules-20261013.txt` registrada en el expediente del caso, guardada por separado del archivo.

**EX020 — Alternativas pasivas.** Quién habla con KW-07: registros de flujos de fw-01 y del router o una captura SPAN. Firmware: registros de activos, el inventario de la herramienta del fabricante durante una sesión de ingeniería aprobada. Telnet: la exportación de configuración de la RTU y la documentación del fabricante sobre los servicios por defecto. Una prueba activa solo se justifica si los registros se contradicen, en una ventana delimitada con operaciones presente y como una única prueba de conexión.

### Capítulo 6: EX021–EX024

**EX021 — Sitúe los activos.** Router celular de KW-06: en el límite de Z1; su interfaz de gestión es tan privilegiada como Z5 y debe figurar en el inventario y en las comprobaciones de deriva. Pasarela del proveedor para SS-3: su propia zona de acceso remoto, que solo se conecta a través de jump-01 y nunca se sitúa en Z3. Servidor de informes: Z6. Portátil de ingeniería: un activo transitorio con sus propios controles (capítulo 16), nunca de forma permanente en ninguna zona.

**EX022 — Redacte un conducto.** C4: origen hist-02 (Z2) → destino report-01 (Z6) tcp/443; iniciado desde Z2 (envío); finalidad, CSV diario del informe de operaciones; responsable, el responsable de datos de operaciones de Kestrel Water; aplicación, regla de fw-01 con incidencia; supervisión, alerta del colector si no hay envío antes de las 06:30 o ante cualquier conexión de Z6 hacia hist-02; revisión anual.

**EX023 — Contraste entre sectores.** Agua: confirmar que hay un servidor SCADA redundante o programar fuera de los periodos críticos; duración de la interrupción del sondeo acordada con operaciones. Red eléctrica: reinicios del procesador de comunicaciones acordados con la sala de control de la red, con los procedimientos ante pérdida del telecontrol preparados; la protección no se ve afectada, pero confírmelo. Hospital: la ingeniería clínica y el nivel de parches admitido por el fabricante del BMS; continuidad de las alarmas de ventilación y de las habitaciones de aislamiento durante el reinicio. Un único calendario semanal no sirve para ninguno de ellos.

**EX024 — Modelo frente a captura.** No lo explican los conductos declarados: las escrituras de 10.30.3.7 → KW-04 (no hay conducto de la red corporativa a Z1); la consulta de la función 43 desde scada-01 si C1 se declara solo como «sondeos de lectura» (añádala explícitamente si se confirma como funcionalidad); dos tramas mal formadas desde scada-01, una anomalía que explicar (fallo del controlador de software o un programa distinto en ese equipo).

### Capítulo 7: EX025–EX028

**EX025 — Decodifique prioridades.** `<86>`: 86 = 10 × 8 + 6 → instalación 10 (authpriv), severidad 6 (informativa). `<134>`: 16 × 8 + 6 → local0, informativa. `<11>`: 1 × 8 + 3 → user, error. `<165>`: 20 × 8 + 5 → local4, aviso.

**EX026 — Corrija un reloj.** Un desfase de +47 s significa que el equipo va adelantado; corregida = 02:10:00 − 47 s = **02:09:13Z**. Indique la incertidumbre: «desfase medido hacia las 03:10Z; deriva durante esa hora desconocida; tratar como ±5 s salvo que se disponga de datos de deriva».

**EX027 — Sitúe la línea BSD.** Se necesitan: el año (a partir del contexto de la recogida, la fecha de la exportación), la zona horaria configurada en la estación de trabajo y su desfase medido. Regla: las líneas que coinciden con `^<\d+>[A-Z][a-z]{2} [ \d]\d \d\d:\d\d:\d\d ` se analizan con un año y una zona explícitos tomados de una tabla por equipo, y el evento se marca con `assumed_zone=true` en la cronología. Si se desconocen la zona o el desfase del equipo, póngalo en una lista aparte de «sin situar» en lugar de adivinar.

**EX028 — Pregunta de punto ciego.** Los registros del cortafuegos del centro de control y el sensor de Z2 no pueden ver el tráfico entre un portátil y la RTU por el conmutador local o el puerto serie de la estación. Los registros de la propia RTU podrían, si registra las sesiones de configuración y las escrituras y si el registro está activado. Añadir: registro de eventos de la RTU reenviado cuando el enlace está activo, un sensor pasivo en la estación donde esté justificado y registros de acceso físico (alarmas de puertas, registro de visitas a la instalación).

### Capítulo 8: EX029–EX032

**EX029 — Nombre el modo.** (a) Incoherencia entre etiquetas o deriva: fallo de la realimentación de posición de la válvula, o caudal que entra por otra vía (derivación, fuga, válvula manual). (b) Valor congelado / incoherencia entre etiquetas: caudalímetro averiado, o un valor congelado o sustituido. (c) Datos obsoletos/en búfer: almacenamiento y reenvío tras una caída del enlace, o una reproducción. (d) Pérdida de la autoridad de control: selector local/remoto dejado en «local» después del mantenimiento, o un enclavamiento que impide el arranque.

**EX030 — Prediga un cambio de regla.** Con `STUCK_MIN = 25` y `MAX_STEP = 7.0` para el nivel: KW-02 ya no se marca (20 < 25); los pasos de 6,84 y 6,83 de KW-07 están por debajo de 7,0, así que no hay pico; la laguna de KW-05 se sigue notificando; KW-01 sin cambios. Salida verificada: solo `KW-05 FLOW_LS gap: 7 consecutive missing minutes`. Lo que se pierde: el analizador congelado y la desviación de una sola muestra, ambos potencialmente relevantes para la seguridad física.

**EX031 — Regla de valor congelado condicional.** `if pump_state == "running" for the whole run and run_length_identical(flow) >= M: alert("flow stuck while pump running")`. Pruebas: bomba parada durante 40 min con caudal 0,0 → sin alerta; bomba en marcha con caudal exactamente 41,0 durante M muestras → alerta; bomba en marcha con variación natural → sin alerta.

**EX032 — Plan de fallo o ataque.** Indicadores de fallo: la pantalla local del analizador difiere del valor notificado o muestra un código de fallo; diagnóstico de la entrada analógica de la RTU (lazo abierto, entrada congelada); registros de mantenimiento que muestran una calibración o trabajos en el analizador. Indicadores de manipulación: escrituras capturadas en el registro de notificación o en un registro de escalado relacionado; una sesión de configuración de la RTU en la ventana; una muestra manual puntual tomada por operaciones que discrepa de 0,62 mientras la pantalla del analizador coincide con la muestra. Todas son de solo lectura o las realiza operaciones.

### Capítulo 9: EX033–EX036

**EX033 — Prueba de respuesta conocida.** Con `0x3D65` en el bucle con desplazamiento a la derecha, el assert falla (`AssertionError`) y el programa se detiene antes de juzgar ninguna trama. Una implementación con bits reflejados (primero el menos significativo) debe usar el polinomio reflejado 0xA6BC; la forma normal 0x3D65 corresponde a las implementaciones que empiezan por el bit más significativo. La prueba de respuesta conocida convirtió un error silencioso y verosímil en un fallo inmediato.

**EX034 — Decodifique el byte de control.** 0xC9 = 1100 1001: DIR 1 (desde la maestra), PRM 1, función 9, solicitar el estado del enlace. 0x44 = 0100 0100: DIR 0 (desde la estación remota), PRM 1 (primaria), función 4, datos de usuario no confirmados, como los que usa, por ejemplo, la respuesta no solicitada de una estación remota. 0x0B = 0000 1011: DIR 0, PRM 0, función 11, estado del enlace (secundaria).

**EX035 — Experimento mental de falsificación.** El CRC solo muestra que los bytes no se corrompieron accidentalmente. La dirección de origen DNP3 1 es un campo que escribe el emisor; cualquier equipo puede atribuírsela. La autenticidad requiere protección criptográfica (DNP3 Secure Authentication, o un túnel cuyos extremos estén autenticados, por ejemplo TLS que termine en fep-01 y en la estación remota o su pasarela), más la aplicación en la red de que solo la ruta de fep-01 alcanza la estación remota. El origen de red inesperado es en sí mismo el hallazgo.

**EX036 — Selección del método.** (a) Pasivo: decodificar una captura en fep-01 o sus registros a lo largo del mes y enumerar las direcciones de origen. (b) Exportación de la configuración del cortafuegos de fep-01 y sus registros; una única prueba de conexión delimitada solo si la exportación es ambigua. (c) Registro de activos; si no, la herramienta del fabricante en modo de solo lectura durante una sesión aprobada y organizada con el ingeniero de protecciones o de telecontrol de Kestrel Grid; nunca sondeando la estación remota.

<a id="glossary"></a>

## Glosario

- **Conducto**: ruta de comunicación declarada entre zonas, con finalidad, protocolo, sentido y responsable (capítulo 6).
- **Laboratorio contenido**: laboratorio que técnicamente no puede afectar a nada fuera de sí mismo (capítulo 12).
- **CRC**: comprobación de redundancia cíclica; detecta la corrupción accidental, no la falsificación (capítulo 9).
- **Deriva**: diferencia entre la configuración real de un equipo y su manifiesto aprobado (capítulo 14).
- **Configuración efectiva**: los ajustes que un programa usa realmente después de analizar sus archivos, por ejemplo `sshd -T` (capítulo 3).
- **Episodio**: grupo de alertas relacionadas que se notifica como un único elemento, con un recuento y un intervalo de tiempo (capítulo 17).
- **Respuesta de excepción (Modbus)**: respuesta cuyo código de función tiene activado el bit alto, con un código de excepción como 01, 02 o 03 (capítulo 12).
- **Prueba de respuesta conocida**: comprobación de una herramienta con una entrada y una salida publicadas antes de confiar en ella (capítulo 9).
- **Cabecera MBAP**: la cabecera de 7 bytes del Modbus Application Protocol sobre TCP (capítulo 2).
- **Prueba negativa / positiva**: prueba de que una acción prohibida falla / de que una función necesaria sigue funcionando (capítulo 11).
- **Ciclo de sondeo**: tiempo necesario para refrescar una vez todos los dispositivos sondeados (capítulo 1).
- **Cuarentena**: conservación, para su revisión, de una entrada interpretable pero inverosímil (capítulo 4).
- **Coordenadas del registro**: archivo, línea y campo que identifican de dónde procede un hallazgo (capítulo 4).
- **Sello**: el resumen criptográfico de un manifiesto de evidencia, registrado fuera del paquete (capítulo 18).
- **Regla sombreada**: regla de cortafuegos que nunca llega a aplicarse porque una regla anterior coincide con todo su tráfico con la acción contraria (capítulo 10).
- **Valor congelado**: lectura que se repite durante más tiempo del que el proceso permite (capítulo 8).
- **Trazabilidad**: el vínculo entre cada requisito y las pruebas y la evidencia que lo verifican (capítulo 11).
- **Dispositivo transitorio**: portátil o soporte que se desplaza entre zonas o instalaciones (capítulo 16).
- **UID 0**: la identidad root en Linux, sea cual sea el nombre de la cuenta (capítulo 3).
- **Zona**: grupo de activos con requisitos de seguridad similares (capítulo 6).

<a id="references"></a>

## Referencias

Las normas, las orientaciones y las páginas públicas cambian. Las versiones y fechas que siguen son las consultadas para este borrador (octubre de 2026); vuelva a verificarlas antes de basarse en ellas. Una cita respalda la afirmación general que la acompaña en el texto, nunca los detalles del caso sintético. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

### Estándares y orientaciones

- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency. [IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors, Including US Water and Wastewater Systems Facilities (AA23-335A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a). December 2023.
- Cybersecurity and Infrastructure Security Agency. [PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure (AA24-038A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a). February 2024.
- Cybersecurity and Infrastructure Security Agency. [Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology).
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- DNP Users Group. [Overview of DNP3 Protocol](https://www.dnp.org/About/Overview-of-DNP3-Protocol). (The full protocol is standardized as IEEE Std 1815.)
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- Modbus Organization. [Modbus specifications](https://www.modbus.org/modbus-specifications) — Modbus Application Protocol, Messaging on TCP/IP Implementation Guide, and Modbus/TCP Security.
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final).
- National Institute of Standards and Technology. [SP 800-41 Rev. 1, Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- National Institute of Standards and Technology. [SP 800-86, Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final).
- National Institute of Standards and Technology. [SP 800-92, Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final).
- National Institute of Standards and Technology. [SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final).
- National Institute of Standards and Technology. [SP 800-123, Guide to General Server Security](https://csrc.nist.gov/pubs/sp/800/123/final).
- National Institute of Standards and Technology. [SP 800-128, Guide for Security-Focused Configuration Management of Information Systems](https://csrc.nist.gov/pubs/sp/800/128/upd1/final).
- National Institute of Standards and Technology. [SP 800-137, Information Security Continuous Monitoring (ISCM)](https://csrc.nist.gov/pubs/sp/800/137/final).

### Protocolos, algoritmos y documentación de software

- Arkko, J., Cotton, M., and Vegoda, L. [RFC 5737: IPv4 Address Blocks Reserved for Documentation](https://www.rfc-editor.org/rfc/rfc5737). IETF, 2010.
- Bray, T. (ed.). [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259). IETF, 2017.
- Cook, G. [Catalogue of parametrised CRC algorithms with 16-bit width (CRC-16/DNP)](https://reveng.sourceforge.io/crc-catalogue/16.htm).
- Gerhards, R. [RFC 5424: The Syslog Protocol](https://www.rfc-editor.org/rfc/rfc5424). IETF, 2009.
- Klyne, G., and Newman, C. [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339). IETF, 2002.
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, 1997.
- Mills, D., Martin, J., Burbank, J., and Kasch, W. [RFC 5905: Network Time Protocol Version 4](https://www.rfc-editor.org/rfc/rfc5905). IETF, 2010.
- OpenBSD project. [sshd_config(5) manual page](https://man.openbsd.org/sshd_config).
- Python Software Foundation. [struct](https://docs.python.org/3/library/struct.html), [socket](https://docs.python.org/3/library/socket.html), [hashlib](https://docs.python.org/3/library/hashlib.html) and [ipaddress](https://docs.python.org/3/library/ipaddress.html). Python 3 documentation.
- Rekhter, Y., et al. [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918). IETF, 1996.
- Shafranovich, Y. [RFC 4180: Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://www.rfc-editor.org/rfc/rfc4180). IETF, 2005.

### Investigación

- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems Magazine*, 21(6), 11–25, 2001.
