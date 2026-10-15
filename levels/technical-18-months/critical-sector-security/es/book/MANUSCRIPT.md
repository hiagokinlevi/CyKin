# Infraestructura crítica y seguridad sectorial: práctica técnica aplicada

- Idioma: español neutro (`es`); curso técnico, dieciocho meses; aproximadamente 1.200 horas de estudio planificado (curso 069 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Los capítulos 1–18 de 18 tienen texto didáctico escrito, quince laboratorios sin conexión, los ejercicios EX001–EX072 y sus resultados resueltos correspondientes. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: operadores técnicos (técnicos de redes y de sistemas, técnicos de SCADA y de telemetría, analistas de seguridad júnior de centros de operaciones) que ya conocen las redes, los sistemas operativos y la programación básica de scripts y que ahora trabajan en sistemas que mueven agua, electricidad o el aire que respiran los pacientes. Conocimientos de entrada: redes, sistemas operativos, scripts y práctica segura de laboratorio.
- En qué se diferencia este curso de sus vecinos. El [libro de tecnólogo](../../../../technologist-3-years/critical-sector-security/es/book/MANUSCRIPT.md) enseña a los implantadores a construir, operar y traspasar un servicio supervisado completo. Los cursos [profesional](../../../../professional-6-months/critical-sector-security/es/book/MANUSCRIPT.md) y [rápido](../../../../rapid-1-month/critical-sector-security/es/book/MANUSCRIPT.md) se ocupan de las decisiones de gestión y de una primera introducción. **Este libro técnico trata de la profundidad técnica práctica**: abrir los paquetes de los protocolos industriales, auditar y bastionar equipos, configurar y verificar los cortafuegos de los conductos, detectar modos de fallo y órdenes no autorizadas, diagnosticar averías descartando hipótesis y producir evidencia que otro técnico pueda comprobar. Cada capítulo pregunta: *¿qué escribiría, leería, cambiaría o probaría exactamente, y cómo lo demostraría?*
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
10. [Infraestructura crítica y seguridad sectorial: configuración de controles](#ch-10): políticas de primera coincidencia, sombreado y acceso de proveedores.
11. [Infraestructura crítica y seguridad sectorial: verificación](#ch-11): pruebas positivas y negativas trazables.
12. [Laboratorio contenido I](#ch-12): un respondedor Modbus con una política de escritura y respuestas de excepción.
13. [Infraestructura crítica y seguridad sectorial: diagnóstico de averías](#ch-13): hipótesis, predicciones, descarte y escalado.
14. [Infraestructura crítica y seguridad sectorial: automatización](#ch-14): detección de derivas basada en hashes y automatización segura.
15. [Infraestructura crítica y seguridad sectorial: integración y dependencias](#ch-15): grafos de dependencias y puntos de integración en las fronteras.
16. [Documentación técnica y seguridad física](#ch-16): documentos ejecutables, autoridad de seguridad física y dispositivos transitorios.
17. [Laboratorio contenido II](#ch-17): una cadena de detección integrada y que se supervisa a sí misma.
18. [Proyecto técnico supervisado](#ch-18): fases del proyecto y un paquete de evidencia sellado.

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

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 18

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

Decodifique a mano las tres tramas siguientes, añádalas después al Lab 2 y confirme el resultado: `000900000006010100000010`, `000a0000000601050003 0000` (quite el espacio), `000b00000006020300640001`. Anote la función, la dirección y la cantidad o el valor de cada una, y si el identificador de unidad es el que espera para KW-04. La segunda trama lleva la función 05, la escritura de una bobina, así que anote si se espera que el servidor SCADA envíe alguna vez una a KW-04. Si una trama tiene un espacio en el hexadecimal, quítelo antes de pegarla; los espacios no forman parte de la captura.

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

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 18

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Siga estudiando — capítulo 03 de 18

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Siga estudiando — capítulo 04 de 18

[← Capítulo 03](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

- Recoger evidencia sin horas UTC ni hashes.
- Tratar el alcance como papeleo: es lo que impide que una prueba se convierta en un incidente.

- Partir de un visto bueno verbal y redactar el alcance después.
- Escanear una subred de una red de control para descubrir dispositivos.
- Corregir un hallazgo antes de recoger la evidencia que lo mostró. Un alcance redactado después del trabajo no puede proteger el proceso mientras se realiza.
- Seguir trabajando después de la hora de fin del alcance porque la última comprobación «solo lleva un minuto», en lugar de parar y pedir una prórroga.

### Ejercicios — capítulo 5

**EX017 — Repare un alcance.** *Objetivo:* encontrar los elementos que faltan. *Entradas:* «Ejecutar un escaneo de 10.10.0.0/16 el martes para encontrar puertos abiertos. Aprobado por TI». *Pasos:* enumere cada defecto y reescríbalo. *Evidencia esperada:* lista de defectos y alcance reescrito. *Rúbrica:* 3 = identifica el autorizador equivocado (hace falta el propietario del sistema), el rango sin límites, el escaneo activo en TO, la falta de ventana, de condiciones de parada y de tratamiento de la evidencia; la reescritura prefiere fuentes de inventario pasivas; 2 = la mayoría de los defectos; 1 = cosmético; 0 = nada.

**EX018 — Etiquete la nota.** *Objetivo:* separar observación e inferencia. *Entradas:* «El proveedor hackeó KW-09 anoche: la configuración de la RTU cambió y los datos se interrumpieron, así que la reinicié». *Pasos:* reescríbala con las cuatro etiquetas. *Evidencia esperada:* nota etiquetada. *Rúbrica:* 3 = observado (hora de la sesión de configuración, laguna de datos), inferido (posible cambio no aprobado; autoría desconocida), hecho (el reinicio, y la pérdida de evidencia que causó), abierto (quién, por qué; responsable); 2 = etiquetas sin advertir la pérdida de evidencia; 1 = parcial; 0 = nada.

**EX019 — Registro de evidencia.** *Objetivo:* producir evidencia verificable. *Entradas:* usted exporta el conjunto de reglas de fw-01 a `fw-01-rules-20261013.txt`. *Pasos:* escriba los campos del registro de evidencia y la orden que produce su hash en Linux. *Evidencia esperada:* el registro y `sha256sum fw-01-rules-20261013.txt`. *Rúbrica:* 3 = los seis elementos, hora UTC con la fuente del reloj, hash guardado por separado del archivo; 2 = falta uno; 1 = solo el hash; 0 = nada.

**EX020 — Alternativas pasivas.** *Objetivo:* evitar pruebas activas innecesarias. *Entradas:* tres preguntas: qué equipos hablan con KW-07; qué firmware ejecuta KW-07; si KW-07 acepta telnet. *Pasos:* proponga un método pasivo o de solo lectura para cada una e indique cuándo seguiría estando justificada una prueba activa. *Evidencia esperada:* tres filas. *Rúbrica:* 3 = registros de flujos o captura SPAN; registros de activos o la herramienta del fabricante durante una sesión de ingeniería aprobada; exportación de la configuración o documentación del fabricante, con una comprobación activa solo en una ventana delimitada y con operaciones presente; 2 = una débil; 1 = todas activas; 0 = nada.

### Síntesis del capítulo

En los entornos críticos, el alcance protege al proceso tanto como a quien hace la prueba. Redáctelo antes de empezar, prefiera los métodos pasivos y haga que cada elemento de evidencia sea verificable por otra persona: en bruto, con fuente, con hora UTC, atribuido y con hash. Conserve antes de cambiar, y mantenga separados lo observado, lo inferido, lo hecho y lo abierto.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Siga estudiando — capítulo 05 de 18

[← Capítulo 04](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Siga estudiando — capítulo 06 de 18

[← Capítulo 05](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Siga estudiando — capítulo 07 de 18

[← Capítulo 06](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Siga estudiando — capítulo 08 de 18

[← Capítulo 07](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

Amplíe el Lab 9 para verificar el CRC de cada bloque de datos de usuario de 16 bytes que sigue a la cabecera. Construya una trama con 17 bytes de datos de usuario (un bloque completo y un bloque de 1 byte), calcule los CRC de ambos bloques y corrompa un byte del segundo bloque para mostrar que la comprobación lo detecta. Corrompa un byte del segundo bloque y confirme que solo falla la comprobación de ese bloque. Guarde los pasos de construcción en las notas del laboratorio para que un revisor pueda reconstruir la misma trama, y anote qué byte corrompió y el CRC esperado y el calculado de ese bloque.

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

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Siga estudiando — capítulo 09 de 18

[← Capítulo 08](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Infraestructura crítica y seguridad sectorial: configuración de controles

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- traducir los conductos declarados (capítulo 6) en una política de cortafuegos de primera coincidencia con denegación por defecto;
- evaluar un conjunto de reglas frente a flujos de prueba mediante código, y detectar las reglas **sombreadas** y **redundantes**;
- reconocer los patrones de configuración que amplían el acceso en silencio: reglas amplias «temporales», «duplicados» que se solapan, permisos para cualquier puerto;
- configurar el acceso de proveedores y el acceso remoto como limitados en el tiempo, registrados y encaminados a través de la zona de gestión;
- planificar un cambio de configuración de forma que pueda verificarse (capítulo 11) y revertirse.

Los capítulos 6–9 describieron y observaron el sistema. Este capítulo lo cambia, empezando por el control que limita más directamente quién puede alcanzar un protocolo sin autenticación: el cortafuegos del conducto.

### 10.1 Los conjuntos de reglas como programas

La mayoría de los cortafuegos de red evalúan las reglas **de arriba abajo y aplican la primera coincidencia**. La guía de cortafuegos del NIST describe el diseño de políticas, la denegación por defecto y la gestión de los conjuntos de reglas ([SP 800-41 Rev. 1](https://csrc.nist.gov/pubs/sp/800/41/r1/final)). Pensar en un conjunto de reglas como en un pequeño programa aclara tres defectos:

- **Regla sombreada**: una regla posterior cuyo tráfico coincide por completo con una regla anterior de acción contraria. Nunca llega a aplicarse, aunque su comentario diga que sí.
- **Regla redundante**: una regla posterior que coincide por completo con una regla anterior de la misma acción. Inofensiva hoy; confusa mañana, cuando alguien borre la anterior.
- **«Duplicado» que amplía**: una regla que parece una copia de otra pero tiene un origen, un destino o un puerto más amplios. No es redundante; es un permiso nuevo.

El orden importa, así que todo cambio debe revisarse en su contexto, no como una línea aislada.

### 10.2 Patrones que erosionan una política

- **Reglas temporales** que sobreviven a su finalidad («permitir la red corporativa hacia el centro de control para la migración»).
- Permisos para **cualquier puerto** (`tcp any`) donde hacía falta uno solo.
- **Orígenes de subred** donde hacía falta un único equipo.
- **Reglas sin responsable, incidencia ni caducidad**.
- **Acceso de gestión desde zonas de usuarios** en lugar de a través del servidor de salto.

Las mitigaciones principales de CISA para la tecnología operacional insisten en eliminar la exposición a internet, cambiar las contraseñas por defecto, proteger el acceso remoto y segmentar la TI de la TO ([CISA primary mitigations for OT](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology)).

### 10.3 Acceso remoto y de proveedores

Configure el acceso de proveedores para que solo exista cuando haga falta: la cuenta o la ruta está desactivada por defecto; se activa para un trabajo con incidencia y una ventana fija; se autentica con autenticación multifactor en el servidor de salto; la sesión queda registrada; y se dispara una alerta ante cualquier uso fuera de una ventana activada. El aviso de CISA sobre actores patrocinados por el Estado chino describe actores que mantienen un acceso prolongado a entornos de infraestructuras críticas, también mediante cuentas válidas y acceso remoto ([CISA AA24-038A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a)); por eso el acceso permanente es un hallazgo aunque hoy nadie lo esté usando indebidamente.

### 10.4 Ejemplo resuelto: fw-01 (sintético)

La política de `fw-01` entre las zonas del KVROC tiene siete reglas. El Lab 10 la comprueba en busca de sombreados y frente a cinco flujos de prueba, cada uno con el resultado que espera la lista de conductos. **Lab 10** (guárdelo como `lab10.py` y ejecútelo con `python3 lab10.py`):

```python
# Lab 10 - evaluate a first-match firewall policy and find shadowed rules (offline, stdlib)
# Synthetic conduit policy for fw-01 between Kestrel Vale zones; addresses are RFC 1918.
from ipaddress import ip_address, ip_network
rules = [  # id, action, source, destination, protocol, port (None = any)
    ("R1", "allow", "10.20.0.10/32", "10.10.0.0/16", "tcp", 502),    # SCADA server polls stations
    ("R2", "allow", "10.20.0.15/32", "10.10.0.0/16", "tcp", 502),    # engineering workstation
    ("R3", "allow", "10.90.0.20/32", "10.20.0.0/24", "tcp", 22),     # jump host to control centre
    ("R4", "allow", "10.30.0.0/16",  "10.20.0.0/24", "tcp", None),   # "temporary" corporate access
    ("R5", "deny",  "10.30.3.0/24",  "10.20.0.0/24", "tcp", 3389),   # intended: block RDP from desks
    ("R6", "allow", "10.20.0.0/24",  "10.10.4.0/24", "tcp", 502),    # duplicate of R1 for KW-04
    ("R7", "deny",  "0.0.0.0/0",     "0.0.0.0/0",    "any", None),   # default deny
]
def matches(rule, src, dst, proto, port):
    _, _, s, d, p, pt = rule
    return (ip_address(src) in ip_network(s) and ip_address(dst) in ip_network(d)
            and p in ("any", proto) and pt in (None, port))
def covers(a, b):   # does earlier rule a match everything rule b matches?
    return (ip_network(b[2]).subnet_of(ip_network(a[2])) and ip_network(b[3]).subnet_of(ip_network(a[3]))
            and a[4] in ("any", b[4]) and a[5] in (None, b[5]))
for i, r in enumerate(rules):
    for earlier in rules[:i]:
        if covers(earlier, r):
            kind = "redundant" if earlier[1] == r[1] else "SHADOWED (never takes effect)"
            print(f"{r[0]} {kind}: fully covered by {earlier[0]}"); break
tests = [("10.20.0.10", "10.10.4.2", "tcp", 502, "allow"), ("10.30.3.7", "10.20.0.5", "tcp", 3389, "deny"),
         ("10.30.3.7", "10.10.4.2", "tcp", 502, "deny"), ("10.30.8.2", "10.20.0.5", "tcp", 445, "deny"),
         ("10.20.0.12", "10.10.4.2", "tcp", 502, "deny")]
for src, dst, proto, port, expect in tests:
    hit = next(r for r in rules if matches(r, src, dst, proto, port))
    status = "PASS" if hit[1] == expect else "FAIL"
    print(f"{status} {src}->{dst} {proto}/{port}: {hit[1]} by {hit[0]} (expected {expect})")
```

Salida esperada (Python 3.13.5):

```text
R5 SHADOWED (never takes effect): fully covered by R4
PASS 10.20.0.10->10.10.4.2 tcp/502: allow by R1 (expected allow)
FAIL 10.30.3.7->10.20.0.5 tcp/3389: allow by R4 (expected deny)
PASS 10.30.3.7->10.10.4.2 tcp/502: deny by R7 (expected deny)
FAIL 10.30.8.2->10.20.0.5 tcp/445: allow by R4 (expected deny)
FAIL 10.20.0.12->10.10.4.2 tcp/502: allow by R6 (expected deny)
```

Tres hallazgos:

1. **R4 sombrea a R5.** El comentario dice que el RDP desde los puestos corporativos está bloqueado, pero R4 ya permitía todo el TCP desde 10.30.0.0/16, de modo que R5 nunca se aplica: el «bloqueo» nunca ha funcionado.
2. **R4 es el verdadero problema.** Una regla «temporal» permite todos los puertos TCP desde toda la zona corporativa hacia el centro de control. Sus pruebas fallan (se permiten RDP y SMB). Fíjese en lo que las pruebas *no* muestran: R7 deniega el puerto 502 de las estaciones a los puestos corporativos, así que fw-01 no explica las escrituras desde el puesto corporativo capturadas en KW-04 en el capítulo 2. Esa ruta tiene que existir en otro lugar; regístrela como abierta (el capítulo 13 la encuentra).
3. **R6 no es un duplicado de R1.** Permite a toda la subred del centro de control escribir en KW-04, incluido 10.20.0.12, que no tiene nada que hacer allí.

Un cambio sólido: borrar R4 (tras confirmar con el responsable qué sigue usándola; los registros del cortafuegos lo mostrarán); subir el bloqueo de RDP por encima de cualquier permiso si sigue haciendo falta, o confiar en la denegación por defecto; sustituir R6 por nada (R1 y R2 ya cubren las rutas necesarias). Vuelva a ejecutar el evaluador con el nuevo conjunto de reglas antes del cambio, y las pruebas en servicio después (capítulo 11).

### 10.5 Planificación de cambios

Todo cambio de configuración en un entorno de control necesita: el antes y el después exactos; el motivo (hallazgo o requisito); el efecto esperado, escrito como pruebas; un plan de reversión; la ventana acordada con operaciones; y quién verifica. La guía del NIST sobre gestión de la configuración orientada a la seguridad describe las líneas base y el control de cambios ([SP 800-128](https://csrc.nist.gov/pubs/sp/800/128/upd1/final)). La exportación del cortafuegos antes y después es evidencia; calcule su hash (capítulo 5).

Exporte el conjunto de reglas y calcule su hash antes y después del cambio, y guarde ambos resúmenes en el registro de cambio. Escriba el efecto esperado como las mismas pruebas que ejecuta el Lab 10, de modo que la verificación sea una nueva ejecución y no una invención nueva. Acuerde la ventana con operaciones y nombre a quién confirmará que el sondeo del SCADA sigue cumpliendo el requisito de frescura después del cambio.

### 10.6 Actividad práctica

Reescriba la política de fw-01 a partir de la lista de conductos del capítulo 6: una regla por conducto declarado, cada una con incidencia y responsable en su comentario, y después la denegación por defecto. Ejecute el Lab 10 sobre su versión hasta que las cinco pruebas se superen y ninguna regla quede sombreada ni sea redundante. Añada dos pruebas propias para el conducto C3. Ponga cada permiso por encima de la denegación por defecto, con la incidencia y el responsable en el comentario. Elimine R4 y R6 en lugar de intentar remendarlas. Añada dos pruebas para el conducto C3: servidor de salto hacia el centro de control por tcp/22, permitido, y un puesto corporativo hacia el mismo puerto, denegado. Vuelva a ejecutar hasta que todas las pruebas se superen y ninguna regla quede sombreada ni sea redundante.

### 10.7 Errores comunes y límites

- Revisar una regla nueva sin leer las reglas que tiene encima y que quizá ya permiten o deniegan el mismo tráfico.
- Borrar una regla amplia sin comprobar en los registros quién la usa actualmente.
- Tratar «parece un duplicado» como «se puede conservar sin riesgo».
- Configurar el acceso de proveedores como permanentemente activado «para emergencias».
- El Lab 10 modela una política sin estado de primera coincidencia con contención exacta; los cortafuegos reales añaden estado, objetos, NAT y zonas, y sus propias herramientas de análisis.

- Restringir R4 para corregir los fallos de tcp/3389 y tcp/445 sin comprobar primero en los registros qué equipos corporativos dependen hoy de ella.
- Activar una cuenta de proveedor para un trabajo con incidencia y olvidar desactivarla cuando se cierra la ventana fija.

### Ejercicios — capítulo 10

**EX037 — Explique el sombreado.** *Objetivo:* razonar sobre el orden. *Entradas:* el Lab 10. *Pasos:* (1) suba R5 por encima de R4 y prediga los resultados de las pruebas; (2) ejecute y compare. *Evidencia esperada:* predicción y salida. *Rúbrica:* 3 = no se notifica ningún sombreado; la prueba 2 (RDP) se supera (denegación por R5); la prueba 4 (SMB) sigue fallando (permiso por R4); la prueba 5 sigue fallando (R6); 2 = casi todo; 1 = conjeturas; 0 = nada.

**EX038 — Corrija la política.** *Objetivo:* producir un conjunto de reglas correcto. *Entradas:* el Lab 10. *Pasos:* elimine R4 y R6 (conserve R5 o elimínela justificándolo); ejecute. *Evidencia esperada:* nueva lista de reglas y salida con cinco líneas PASS. *Rúbrica:* 3 = cinco líneas PASS; justificación sobre R5 (redundante con la denegación por defecto una vez eliminada R4, así que eliminarla o conservarla para un registro explícito); señala que antes hay que comprobar en los registros quién usa R4; 2 = se superan sin justificación; 1 = parcial; 0 = nada.

**EX039 — Configuración del acceso de proveedores.** *Objetivo:* configurar un acceso limitado en el tiempo. *Entradas:* el proveedor de los relés de SS-3 necesita acceso remoto unas dos veces al año. *Pasos:* especifique el estado de la cuenta, los pasos de activación, la ruta, la autenticación, el registro, las alertas y la caducidad. *Evidencia esperada:* una especificación de configuración. *Rúbrica:* 3 = desactivada por defecto; activada por la guardia del KVROC conforme a una incidencia aprobada por Kestrel Grid; ruta a través de jump-01 con MFA y grabación de la sesión; nunca directamente a la red de los relés; alerta ante un uso fuera de ventana; caducidad automática; revisión al día siguiente; 2 = falta un elemento; 1 = «VPN para el proveedor»; 0 = nada.

**EX040 — Detecte las ampliaciones.** *Objetivo:* ampliar el evaluador. *Entradas:* la función `covers` del Lab 10. *Pasos:* añada una comprobación que notifique cuándo una regla posterior con la misma acción se solapa *parcialmente* con una anterior y es más amplia en origen o destino. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = notifica que R6 amplía R1 (el origen /24 contiene el /32 de R1; el destino /24 está dentro del /16; mismo puerto), explica por qué merece revisión; 2 = lo detecta sin explicación; 1 = intentado; 0 = nada.

### Síntesis del capítulo

Un conjunto de reglas de cortafuegos es un programa de primera coincidencia, y sus defectos son defectos de programa: reglas sombreadas que nunca actúan, reglas redundantes que confunden y reglas de apariencia similar que amplían el acceso. Configure los conductos con una regla por finalidad declarada y denegación por defecto, mantenga desactivado el acceso de proveedores hasta que haga falta y planifique cada cambio con sus pruebas y su reversión. Después, verifique, que es el siguiente capítulo.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Siga estudiando — capítulo 10 de 18

[← Capítulo 09](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Infraestructura crítica y seguridad sectorial: verificación

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- redactar los requisitos como enunciados comprobables y vincular cada uno con al menos una prueba (**trazabilidad**);
- diseñar pruebas **positivas** (la función necesaria sigue funcionando) y **negativas** (la acción prohibida falla) para cada cambio de un control;
- negarse a contar una prueba sin evidencia, e informar de los requisitos como verificados, fallidos o sin probar;
- verificar sin dañar el proceso: pruebas pequeñas y delimitadas en ventanas acordadas.

El capítulo 10 cambió la configuración. Un cambio no termina cuando se aplica; termina cuando se demuestra que sus requisitos se cumplen. Este capítulo hace sistemática esa demostración.

### 11.1 Requisitos que se pueden probar

«El historiador está bastionado» no puede probarse. «SSH en hist-02 escucha solo en 10.90.0.21» sí. Redacte cada requisito de modo que una prueba nombrada, ejecutada por otra persona, pudiera hacerlo fallar. Divida los requisitos compuestos: «solo el servidor SCADA y la estación de ingeniería alcanzan tcp/502 en las estaciones» necesita una prueba positiva (el SCADA sigue sondeando) **y** una negativa (otro equipo del centro de control es rechazado). El REQ-1 del Lab 11 supera esta comprobación: que SSH escuche solo en 10.90.0.21 es algo que las pruebas T1 y T2 podrían haber hecho fallar. El REQ-4 muestra la división en la práctica: T5 y T6 cubren sus mitades negativa y positiva, y el requisito falla si falla cualquiera de ellas. Ponga los identificadores de los requisitos en el registro de cambio antes de empezar el trabajo.

### 11.2 Pruebas positivas y negativas

Las **pruebas negativas** muestran que un control bloquea lo que debe; las **pruebas positivas** muestran que no bloquea lo que operaciones necesita. Un cambio de cortafuegos que supera todas sus pruebas negativas pero detiene la recogida del historiador ha fallado. En los entornos de control, las pruebas positivas importan tanto como las negativas: la disponibilidad suele ser la primera prioridad. La guía de pruebas del NIST trata la planificación y la ejecución de pruebas técnicas ([SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)); las orientaciones sobre supervisión continua insisten en que la eficacia de los controles debe demostrarse de nuevo con el tiempo, no suponerse ([SP 800-137](https://csrc.nist.gov/pubs/sp/800/137/final)).

### 11.3 Reglas de evidencia

Una prueba solo cuenta si tiene: un identificador, el requisito que verifica, el método, la hora, la persona, el resultado y un archivo de evidencia (capítulo 5). Una «solo revisión de la configuración» sin salida registrada es una actividad útil, pero no un resultado de prueba. Un requisito sin ninguna prueba contada está **sin probar**: ni verificado ni fallido. Informar de lo no probado como verificado es la forma más común en que la verificación induce a error. El Lab 11 aplica la regla a T8, una revisión de la configuración del REQ-2 sin archivo de evidencia, que el script ignora. El REQ-6 del Lab 11 sigue sin probar hasta que alguien produzca una línea de denegación desde el colector; informar de él como verificado porque la regla existe ocultaría la laguna. Guarde los archivos de evidencia junto a los identificadores de las pruebas en el registro de verificación.

### 11.4 Ejemplo resuelto: verificación de CHG-2207 (sintético)

CHG-2207 bastionó SSH en hist-02 y debía cerrar el acceso corporativo al centro de control en fw-01. El registro de verificación:

**Lab 11** (guárdelo como `lab11.py` y ejecútelo con `python3 lab11.py`):

```python
# Lab 11 - requirement-to-test traceability after a hardening change (offline, stdlib)
# Synthetic verification record for change CHG-2207 on HIST-02 and fw-01, 2026-10-12.
requirements = {
 "REQ-1": "SSH listens only on management address 10.90.0.21",
 "REQ-2": "Root cannot log in over SSH",
 "REQ-3": "Corporate desks cannot reach control-centre RDP",
 "REQ-4": "Only SCADA server and engineering workstation reach station tcp/502",
 "REQ-5": "Historian still receives KW-01..KW-12 readings after change",
 "REQ-6": "Firewall denies are logged to the collector",
}
tests = [  # test id, requirement, method, positive/negative, result, evidence
 ("T1", "REQ-1", "listening-socket listing on host", "neg", "pass", "ss-output-0612.txt"),
 ("T2", "REQ-1", "connect to 10.20.0.21:22 from jump host", "neg", "pass", "conn-0614.txt"),
 ("T3", "REQ-2", "root login attempt from jump host", "neg", "pass", "auth-0615.log"),
 ("T4", "REQ-3", "RDP connect from 10.30.3.7", "neg", "fail", "conn-0618.txt"),
 ("T5", "REQ-4", "Modbus read from 10.20.0.12", "neg", "fail", "conn-0620.txt"),
 ("T6", "REQ-4", "Modbus read from SCADA 10.20.0.10", "pos", "pass", "poll-0621.txt"),
 ("T7", "REQ-5", "count stations reporting 06:30-06:40Z", "pos", "pass", "hist-count.csv"),
 ("T8", "REQ-2", "config review only", "neg", "pass", ""),
]
status = {}
for tid, req, method, kind, res, ev in tests:
    if not ev: print(f"{tid} {req} ignored: no evidence file recorded ({method})"); continue
    status.setdefault(req, []).append((tid, kind, res))
for req, text in requirements.items():
    rs = status.get(req, [])
    if not rs: verdict = "UNTESTED"
    elif any(r == "fail" for _, _, r in rs): verdict = "FAILED"
    else: verdict = "verified"
    kinds = "+".join(sorted({k for _, k, _ in rs})) or "-"
    print(f"{req} {verdict:<9} tests={','.join(t for t, _, _ in rs) or '-':<6} kinds={kinds:<7} {text}")
v = sum(1 for r in requirements if status.get(r) and all(x[2] == "pass" for x in status[r]))
print(f"verified {v}/{len(requirements)}; the change is not complete until every requirement is verified")
```

Salida esperada (Python 3.13.5):

```text
T8 REQ-2 ignored: no evidence file recorded (config review only)
REQ-1 verified  tests=T1,T2  kinds=neg     SSH listens only on management address 10.90.0.21
REQ-2 verified  tests=T3     kinds=neg     Root cannot log in over SSH
REQ-3 FAILED    tests=T4     kinds=neg     Corporate desks cannot reach control-centre RDP
REQ-4 FAILED    tests=T5,T6  kinds=neg+pos Only SCADA server and engineering workstation reach station tcp/502
REQ-5 verified  tests=T7     kinds=pos     Historian still receives KW-01..KW-12 readings after change
REQ-6 UNTESTED  tests=-      kinds=-       Firewall denies are logged to the collector
verified 3/6; the change is not complete until every requirement is verified
```

Tres requisitos verificados, dos fallidos, uno sin probar. El REQ-3 falló porque R4 se dejó en su sitio: la incidencia decía «corregir la regla de RDP», y el ingeniero corrigió R5 en lugar de la regla que la sombreaba, un patrón habitual cuando un cambio se redacta como la edición de una línea en lugar de como un requisito. El REQ-4 falló su prueba negativa (10.20.0.12 todavía puede leer las estaciones, a través de R6) mientras superaba la positiva: exactamente por eso hacen falta ambos tipos. El REQ-6 no tiene ninguna prueba; nadie comprobó que las denegaciones llegan al colector, de modo que las detecciones del capítulo 17 estarían ciegas ante los intentos denegados. T8 se ignoró porque no tiene archivo de evidencia. El cambio vuelve a «en curso» con tres elementos abiertos, cada uno con un responsable.

### 11.5 Verificación segura en redes de control

- Prefiera leer resultados que el sistema ya registra (registros del cortafuegos, recuentos del historiador) antes que generar tráfico.
- Cuando genere tráfico, use un origen de prueba señalado (por ejemplo, 10.30.99.9), la acción más pequeña posible (una conexión TCP sin carga útil) y una ventana acordada con operaciones informada.
- No verifique nunca un bloqueo de escritura intentando escribir en un controlador en servicio; verifíquelo con una prueba de conexión y el registro del cortafuegos, o frente a un dispositivo de repuesto en un laboratorio (capítulo 12).
- Deténgase ante el primer comportamiento inesperado.

Operaciones debe saber antes de la primera conexión que 10.30.99.9 es el origen de prueba, para que su tráfico no se confunda con un intruso.

### 11.6 Actividad práctica

Escriba una prueba para el REQ-6 que no toque ninguna estación: un intento de conexión desde el puesto de pruebas señalado a un puerto del centro de control que debería denegarse y, después, una consulta en el colector de la línea de denegación correspondiente en un plazo de 60 s. Añádala al Lab 11 como T9 con un nombre de archivo de evidencia y vuelva a ejecutar. Use el puesto de pruebas señalado y consulte después en el colector la denegación correspondiente en un plazo de sesenta segundos. Añada la prueba como T9 con un nombre de archivo de evidencia y vuelva a ejecutar el Lab 11 para que el REQ-6 pase de sin probar a verificado o fallido. Guarde el texto de la consulta al colector en el archivo de evidencia para que la prueba pueda repetirse.

### 11.7 Errores comunes y límites

- Ejecutar solo pruebas negativas y no advertir que se detuvo la recogida del historiador.
- Contar una prueba sin evidencia.
- Informar de «5 de 6 pruebas superadas» en lugar del estado de cada requisito.
- Verificar una vez y suponerlo para siempre; vuelva a verificar después de los cambios relacionados.
- El Lab 11 trata cualquier prueba fallida como un requisito fallido; un requisito también puede estar verificado *en parte* si una prueba solo cubre parte de su alcance; dígalo con palabras.

- Dejar el REQ-6 sin probar porque producir una línea de denegación en el colector parecía más difícil que leer la regla del cortafuegos.

### Ejercicios — capítulo 11

**EX041 — Hágalo comprobable.** *Objetivo:* reescribir requisitos. *Entradas:* «El acceso remoto es seguro», «La hora está sincronizada», «Los registros se conservan». *Pasos:* reescriba cada uno como uno o más requisitos comprobables para el KVROC. *Evidencia esperada:* requisitos reescritos con una idea de prueba para cada uno. *Rúbrica:* 3 = enunciados específicos como «el acceso del proveedor a SS-3 solo es posible a través de jump-01 con MFA durante una ventana activada», «todos los equipos de Z2 a menos de 1 s de ntp-ops», «los eventos de permiso y denegación de fw-01 llegan al colector en 60 s y se conservan 12 meses»; cada uno con una prueba; 2 = uno vago; 1 = repetidos tal cual; 0 = nada.

**EX042 — Añada la prueba que falta.** *Objetivo:* cerrar un requisito sin probar. *Entradas:* el Lab 11 y la actividad de 11.6. *Pasos:* añada T9 para el REQ-6 con resultado superado y archivo de evidencia `collector-0630.txt`; ejecute. *Evidencia esperada:* salida. *Rúbrica:* 3 = REQ-6 verificado mediante T9, total «verified 4/6»; explica que REQ-3 y REQ-4 siguen impidiendo cerrar el cambio; 2 = solo la salida; 1 = intentado; 0 = nada.

**EX043 — Pruebas positivas para un cambio de cortafuegos.** *Objetivo:* proteger la disponibilidad. *Entradas:* la corrección de fw-01 de EX038. *Pasos:* enumere las pruebas positivas necesarias antes de cerrar el cambio. *Evidencia esperada:* lista con método y evidencia. *Rúbrica:* 3 = el SCADA sondea las doce estaciones (recuento del historiador), la estación de ingeniería puede conectarse a una estación en una ventana aprobada, el SSH de jump-01 a Z2 funciona, la exportación diaria de hist-02 sigue llegando; cada una con su fuente de evidencia; 2 = algunas; 1 = ninguna positiva; 0 = nada.

**EX044 — Sin probar no es verificado.** *Objetivo:* informar con honestidad. *Entradas:* el resumen de un directivo: «CHG-2207: 7 de 8 pruebas superadas, terminado». *Pasos:* redacte el estado corregido en un párrafo. *Evidencia esperada:* párrafo. *Rúbrica:* 3 = indica el estado por requisito (3 verificados, 2 fallidos, 1 sin probar), nombra los elementos abiertos y sus responsables, dice que el cambio no está terminado; 2 = correcto pero sin responsables; 1 = retoque menor; 0 = nada.

### Síntesis del capítulo

La verificación convierte un cambio de configuración en un resultado demostrado. Redacte requisitos que puedan fallar, pruebe cada uno con pruebas positivas y negativas, cuente solo las pruebas con evidencia e informe de cada requisito como verificado, fallido o sin probar. En las redes de control, verifique con las acciones delimitadas más pequeñas, y nunca experimentando con el proceso en servicio.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Siga estudiando — capítulo 11 de 18

[← Capítulo 10](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Laboratorio contenido I

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- construir un laboratorio **contenido** en el que se pueda estudiar el comportamiento de un protocolo sin ninguna red ni dispositivo real;
- implementar un respondedor Modbus/TCP mínimo con una **política de escritura**: qué registros pueden escribirse y dentro de qué rango de valores;
- generar y leer **respuestas de excepción** de Modbus (función ilegal, dirección de datos ilegal, valor de datos ilegal);
- evaluar un laboratorio con una rúbrica: contención, reproducibilidad, evidencia y honestidad sobre lo que el laboratorio no modela.

Los capítulos 1–11 analizaron el tráfico y la configuración. Este capítulo construye algo que se puede romper sin peligro. Es el primero de dos laboratorios evaluados; el capítulo 17 es el segundo.

### 12.1 Qué significa «contenido»

Un laboratorio contenido no puede afectar a nada fuera de sí mismo. En este libro eso se garantiza técnicamente, no con buenas intenciones: el Lab 12 usa `socket.socketpair()`, que crea dos sockets conectados **dentro de un mismo proceso** ([Python socket](https://docs.python.org/3/library/socket.html)). Nada escucha en un puerto, nada se encamina, y el programa no puede alcanzar un controlador real ni siquiera por error. Los laboratorios mayores usan redes virtuales aisladas sin ruta hacia fuera, o hardware de repuesto en un banco con su cable de red sin conectar a ningún otro sitio. Anote la propiedad de contención de cada laboratorio que construya y cómo la comprobó.

### 12.2 La tarea del respondedor

Un controlador real decide si ejecuta una escritura según su propia lógica, que en los dispositivos Modbus clásicos a menudo significa «siempre». Algunos dispositivos y pasarelas de protocolo permiten proteger contra escritura por rangos de registros; muchos no. El respondedor del laboratorio hace explícita la política:

- las **lecturas** de registros de retención (función 3) se permiten dentro de la tabla, con una cantidad de 1–125 (el límite del protocolo para una lectura);
- las **escrituras** de un registro (función 6) solo se permiten en el registro 7, el punto de consigna de la bomba, y solo para valores de 100–400;
- todo lo demás devuelve una **excepción**: el código de función con su bit alto activado (código + 0x80) y un código de excepción (01 función ilegal, 02 dirección de datos ilegal, 03 valor de datos ilegal), tal como los define la especificación Modbus Application Protocol ([Modbus specifications](https://www.modbus.org/modbus-specifications)).

Una respuesta normal a la función 6 repite la petición. Una respuesta normal a la función 3 lleva un recuento de bytes y los valores de los registros.

### 12.3 El registro dentro del dispositivo

El respondedor registra cada lectura, cada escritura aceptada con su valor anterior y el nuevo, y cada excepción. En los equipos reales, estos son exactamente los registros que habría deseado tener en el capítulo 7. Una ráfaga de respuestas de excepción 02 desde un mismo origen es una señal clara de que alguien está cartografiando el espacio de registros; una racha de excepciones 03 es alguien que prueba los límites. En los equipos reales esos registros suelen faltar, y por eso el laboratorio los hace visibles. Guarde el registro del laboratorio junto con las respuestas en hexadecimal para que un revisor pueda emparejar cada excepción con una petición.

### 12.4 Ejemplo resuelto: el respondedor de banco (sintético)

**Lab 12** (guárdelo como `lab12.py` y ejecútelo con `python3 lab12.py`):

```python
# Lab 12 - contained Modbus/TCP responder with a write policy (offline, standard library only)
# Uses socket.socketpair(): both ends live inside this process; nothing touches a real network.
import socket, struct
regs = [0] * 10; regs[0], regs[1], regs[7] = 342, 61, 250      # level cm, chlorine x100, pump setpoint
WRITABLE = {7: (100, 400)}                                      # register: allowed value range
log = []
def respond(req: bytes) -> bytes:
    tid, pid, length, unit, fc = struct.unpack(">HHHBB", req[:8])
    def exc(code):
        log.append(f"tid={tid} fc={fc} exception {code}")
        return struct.pack(">HHHBBB", tid, 0, 3, unit, fc | 0x80, code)
    if pid != 0 or length != len(req) - 6: return exc(3)
    if fc == 3:
        addr, qty = struct.unpack(">HH", req[8:12])
        if not 1 <= qty <= 125 or addr + qty > len(regs): return exc(2)
        data = struct.pack(f">{qty}H", *regs[addr:addr + qty])
        log.append(f"tid={tid} read {addr}..{addr + qty - 1}")
        return struct.pack(">HHHBBB", tid, 0, 3 + len(data), unit, 3, len(data)) + data
    if fc == 6:
        addr, val = struct.unpack(">HH", req[8:12])
        if addr not in WRITABLE: return exc(2)
        lo, hi = WRITABLE[addr]
        if not lo <= val <= hi: return exc(3)
        old, regs[addr] = regs[addr], val
        log.append(f"tid={tid} WRITE reg {addr} {old}->{val}")
        return req[:12]                                         # echo is the normal fc 6 reply
    return exc(1)
client, server = socket.socketpair()
def call(tid, fc, a, b):
    client.sendall(struct.pack(">HHHBBHH", tid, 0, 6, 1, fc, a, b))
    server.sendall(respond(server.recv(260)))
    r = client.recv(260)
    return r.hex()
print("read 0..2     ", call(1, 3, 0, 3))
print("write 7=300   ", call(2, 6, 7, 300))
print("write 7=900   ", call(3, 6, 7, 900))
print("write 0=0     ", call(4, 6, 0, 0))
print("fc 8 diag     ", call(5, 8, 0, 0))
print("read 8..12    ", call(6, 3, 8, 5))
client.close(); server.close()
print("registers", regs[:3], "setpoint", regs[7])
for entry in log: print("log:", entry)
```

Salida esperada (Python 3.13.5):

```text
read 0..2      0001000000090103060156003d0000
write 7=300    00020000000601060007012c
write 7=900    000300000003018603
write 0=0      000400000003018602
fc 8 diag      000500000003018801
read 8..12     000600000003018302
registers [342, 61, 0] setpoint 300
log: tid=1 read 0..2
log: tid=2 WRITE reg 7 250->300
log: tid=3 fc=6 exception 3
log: tid=4 fc=6 exception 2
log: tid=5 fc=8 exception 1
log: tid=6 fc=3 exception 2
```

Lea las respuestas en hexadecimal. La primera es una lectura normal: `03 06` (función 3, seis bytes) seguida de 0x0156 = 342, 0x003D = 61 y 0. La escritura de 300 en el registro 7 se repite y el registro anota 250 → 300. Escribir 900 devuelve `86 03`: función 6 + 0x80, excepción 3, valor ilegal. Escribir el registro 0 devuelve `86 02`, dirección ilegal: el registro 0 es una medición y no se puede escribir. La función 8 (diagnóstico) devuelve `88 01`, función ilegal. Una lectura de cinco registros a partir del 8 se sale de la tabla de 10 registros y devuelve `83 02`. Los registros del final muestran que solo surtió efecto la escritura aprobada.

### 12.5 Rúbrica de evaluación de un laboratorio contenido

| Criterio | 3 (excelente) | 1 (débil) |
|---|---|---|
| Contención | Es técnicamente imposible alcanzar un dispositivo real; la propiedad se declara y se comprueba | Depende de «no lo apuntaré a nada» |
| Reproducibilidad | Entradas fijas; salida exacta registrada con la versión de Python | La salida varía o no se registra |
| Declaración de fidelidad | Enumera lo que el laboratorio modela y lo que no | Afirma representar dispositivos reales |
| Evidencia | Registros y salidas guardados, con hash, vinculados a los ejercicios | Solo capturas de pantalla |
| Seguridad de las ampliaciones | Cambios revisados para que no puedan eliminar la contención | Añade código de red real sin revisión |

### 12.6 Lo que el laboratorio no modela

Los dispositivos reales difieren: algunos ignoran los identificadores de unidad, algunos aceptan escrituras en cualquier registro, algunos se bloquean con peticiones mal formadas, y pocos registran algo. El respondedor atiende una petición cada vez y no tiene concurrencia, tiempos de espera ni lecturas parciales. Su valor está en hacer visibles la política y las excepciones, no en predecir el comportamiento de un fabricante concreto. No use nunca los resultados de un laboratorio para decidir cómo responderá un dispositivo en servicio a una prueba.

Si el respondedor devuelve la excepción 2 para una lectura de los registros 8 a 12, eso no dice nada sobre lo que haría una RTU real de KW-04. Los dispositivos reales difieren en el tratamiento del identificador de unidad, la protección contra escritura y el registro, y muchos se bloquean con peticiones mal formadas. Indique esas lagunas en la evaluación y limite la verificación en servicio a los métodos delimitados y autorizados del capítulo 11.

### 12.7 Actividad práctica

Añada al respondedor la función 16 (escribir varios registros) con la misma política: todos los registros del rango deben poder escribirse y todos los valores deben estar dentro de sus límites, o se rechaza la escritura completa. Pruebe cuatro casos: todo permitido; una dirección que no se puede escribir; un valor fuera de rango; un recuento de bytes incoherente con la cantidad. Anote las cuatro respuestas en hexadecimal y, junto a ellas, las líneas del registro. Por último, envíe una escritura con la función 16 que incluya un registro que su tratamiento de la función 6 ya rechaza (como el registro 0), y confirme que el registro da el mismo motivo para ambos rechazos.

### 12.8 Errores comunes y límites

- Usar un socket de red real «solo para probar» y dejarlo enlazado a todas las interfaces.
- Aceptar una escritura parcial de varios registros que cambia algunos registros antes de rechazar otros.
- Olvidar que la respuesta a la función 6 es una repetición de la petición, y analizarla mal.
- Añadir la función 16 en la actividad 12.7 sin reutilizar la política de escritura individual, de modo que el límite de 100–400 del registro 7 se aplica en una vía de escritura y no en la otra.
- Probar solo la escritura permitida y nunca las rechazadas; el registro de las respuestas de excepción es la evidencia de que la política funciona.
- Tratar el comportamiento de las excepciones del laboratorio como el de un fabricante. Declare la contención como una propiedad técnica en todo informe de laboratorio.

### Ejercicios — capítulo 12

**EX045 — Lea las respuestas.** *Objetivo:* decodificar respuestas normales y de excepción. *Entradas:* la salida del Lab 12. *Pasos:* para cada una de las seis respuestas, dé el identificador de transacción, la función (con o sin el bit de excepción) y su significado. *Evidencia esperada:* seis filas. *Rúbrica:* 3 = las seis correctas, incluidas 0x86 = excepción a la 6, 0x88 = excepción a la 8, 0x83 = excepción a la 3; 2 = una errónea; 1 = solo las respuestas normales; 0 = nada.

**EX046 — Implemente la función 16.** *Objetivo:* ampliar el respondedor con seguridad. *Entradas:* la actividad 12.7. *Pasos:* impleméntela y ejecute los cuatro casos. *Evidencia esperada:* código y salidas. *Rúbrica:* 3 = comportamiento de todo o nada; excepción 02 para una dirección que no se puede escribir, 03 para un valor fuera de rango, 03 (o un tratamiento de petición mal formada justificado) para un recuento de bytes incoherente; la respuesta normal repite solo la dirección y la cantidad; líneas de registro para cada caso; 2 = funciona con un código erróneo; 1 = acepta escrituras parciales; 0 = nada.

**EX047 — Detecte intentos de cartografiado.** *Objetivo:* usar los registros del lado del dispositivo. *Entradas:* el registro del respondedor. *Pasos:* escriba una regla que alerte del comportamiento de cartografiado o de prueba de límites y pruébela añadiendo cinco lecturas de direcciones fuera de rango desde una misma secuencia de transacciones. *Evidencia esperada:* regla y salida. *Rúbrica:* 3 = por ejemplo, «≥3 respuestas de excepción 02 en 60 s desde un mismo origen»; demuestra que se dispara con la prueba y no con las seis peticiones originales (que solo contienen dos respuestas de excepción 02; contar juntas la 02 y la 03 ya llegaría a tres y la dispararía); 2 = se dispara en ambos casos; 1 = solo la regla; 0 = nada.

**EX048 — Evalúe un laboratorio.** *Objetivo:* aplicar la rúbrica. *Entradas:* el laboratorio de un colega que ejecuta un servidor Modbus en `0.0.0.0:502` en un portátil que «solo se usa en la oficina». *Pasos:* puntúelo en contención y fidelidad y proponga una corrección. *Evidencia esperada:* puntuaciones y corrección. *Rúbrica:* 3 = contención 1 (alcanzable desde cualquier red a la que se una el portátil, y el portátil puede llevarse a las estaciones); corrección con socketpair o con enlace solo a la interfaz de bucle invertido más cortafuegos del equipo, o una red de máquinas virtuales aislada; se exige una declaración de fidelidad; 2 = corrección sin razonamiento; 1 = lo acepta; 0 = nada.

### Síntesis del capítulo

Un laboratorio contenido es aquel en el que la seguridad es una propiedad técnica. El Lab 12 construye un respondedor Modbus que aplica una política de escritura y devuelve las excepciones adecuadas, haciendo visible lo que ocultan la mayoría de los dispositivos reales: qué peticiones se rechazaron y por qué. Evalúe todo laboratorio en cuanto a contención, reproducibilidad, evidencia y una declaración franca de lo que no modela.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Siga estudiando — capítulo 12 de 18

[← Capítulo 11](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Infraestructura crítica y seguridad sectorial: diagnóstico de averías

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- aplicar un método estructurado de diagnóstico de averías: definir el síntoma, recoger observaciones de solo lectura, enumerar hipótesis, contrastar predicciones, conservar y, después, cambiar;
- descartar hipótesis comparando lo que predice cada una con lo que usted observó, de un modo que otros puedan comprobar;
- reconocer cuándo la investigación de una avería se convierte en un incidente de seguridad y qué conservar en ese momento;
- llevar un **registro de diagnóstico** que sea también evidencia.

El capítulo 8 describió los síntomas; los capítulos 7, 9 y 11 le dieron observaciones. Este capítulo las reúne bajo presión de tiempo, cuando una estación ha enmudecido y los operadores quieren recuperarla.

### 13.1 El método

1. **Defina el síntoma** con precisión: qué etiqueta, desde cuándo (UTC), cómo se detectó, qué sigue funcionando.
2. **Recoja observaciones de solo lectura** por orden de coste: el estado de las demás estaciones; los contadores del enlace y del router; los registros del cortafuegos; una prueba de conexión TCP desde el origen de sondeo habitual; una lectura del protocolo; los registros de configuración del dispositivo.
3. **Enumere hipótesis** (al menos una corriente y otra relevante para la seguridad) antes de contrastar ninguna.
4. **Escriba las predicciones de cada hipótesis**: ¿qué observaría si fuera cierta?
5. **Compare** las predicciones con las observaciones. Una hipótesis contradicha por una observación fiable queda refutada; la que es coherente con todas se mantiene.
6. **Conserve** todo lo que pueda ser evidencia antes de cambiarlo (capítulo 5).
7. **Cambie** una sola cosa, con un registro de cambio, y verifique (capítulo 11).
8. **Registre** la causa, la evidencia y lo que la habría detectado antes.

La disciplina de escribir las predicciones *antes* de comparar es lo que impide que el primer relato verosímil se convierta en la conclusión.

### 13.2 De la avería al incidente

Un ejercicio de diagnóstico se convierte en un posible incidente cuando una observación no se explica por ninguna actividad aprobada: una sesión de configuración no aprobada, un origen desconocido, un archivo modificado sin registro de cambio. En ese momento deje de cambiar cosas, conserve (configuración, registros, registros de sesiones) y traspase el asunto a través del proceso de incidentes. Las recomendaciones del NIST sobre respuesta a incidentes sitúan esta decisión dentro de la gestión de riesgos más amplia de la organización ([SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). La tarea del técnico no es decidir que hubo un ataque; es advertir que falta la explicación y mantener intacta la evidencia.

### 13.3 Ejemplo resuelto: KW-09 enmudece (sintético)

A las 07:05Z del 12 de octubre dejan de llegar las lecturas de KW-09; todas las demás estaciones funcionan. Usted recoge observaciones de solo lectura durante quince minutos y enumera cinco hipótesis. **Lab 13** (guárdelo como `lab13.py` y ejecútelo con `python3 lab13.py`):

```python
# Lab 13 - eliminate hypotheses for "KW-09 readings missing" (offline, standard library only)
# Synthetic observations collected read-only between 07:05 and 07:20Z on 2026-10-12.
observed = {
 "rtu_ping": True,              # RTU answers ICMP from the SCADA server
 "tcp502_handshake": True,      # TCP connect to 10.10.9.2:502 succeeds from SCADA server
 "modbus_reply": "exception 2", # read of registers 0..3 returns illegal data address
 "fw_denies": False,            # no fw-01 denies for 10.10.9.2 in the window
 "radio_errors": False,         # cellular router CRC/error counters flat
 "rtu_config_changed": True,    # rtu-kw09 config session at 06:41Z (clock-corrected) by user eng
 "change_ticket": False,        # no approved change ticket for KW-09 today
 "other_stations_ok": True,
}
hypotheses = {  # what each hypothesis predicts we would observe
 "H1 radio/link failure":           {"rtu_ping": False, "tcp502_handshake": False, "radio_errors": True},
 "H2 firewall change blocks polls": {"tcp502_handshake": False, "fw_denies": True},
 "H3 SCADA server fault":           {"other_stations_ok": False},
 "H4 RTU register map changed":     {"rtu_ping": True, "tcp502_handshake": True, "modbus_reply": "exception 2",
                                     "rtu_config_changed": True},
 "H5 RTU powered off":              {"rtu_ping": False},
}
for h, pred in hypotheses.items():
    clash = [k for k, v in pred.items() if observed[k] != v]
    print(f"{h:<32} {'REFUTED by ' + ', '.join(clash) if clash else 'CONSISTENT with all observations'}")
print("unapproved RTU configuration session -> preserve RTU config and session logs, then treat as possible incident"
      if observed["rtu_config_changed"] and not observed["change_ticket"] else "change was approved")
```

Salida esperada (Python 3.13.5):

```text
H1 radio/link failure            REFUTED by rtu_ping, tcp502_handshake, radio_errors
H2 firewall change blocks polls  REFUTED by tcp502_handshake, fw_denies
H3 SCADA server fault            REFUTED by other_stations_ok
H4 RTU register map changed      CONSISTENT with all observations
H5 RTU powered off               REFUTED by rtu_ping
unapproved RTU configuration session -> preserve RTU config and session logs, then treat as possible incident
```

Cuatro hipótesis quedan refutadas por observaciones concretas: el enlace está activo (ping, establecimiento de la conexión, contadores de errores planos); el cortafuegos no está denegando; el servidor SCADA sondea con éxito las demás estaciones; la RTU tiene alimentación. Una sigue siendo coherente: el mapa de registros de la RTU cambió, de modo que las lecturas del servidor SCADA apuntan ahora a direcciones que el dispositivo ya no tiene (excepción 02, exactamente como en el laboratorio del capítulo 12). Y la RTU registró una sesión de configuración a las 06:41Z (reloj corregido) sin incidencia de cambio.

Esta última observación convierte una avería en un posible incidente. Los pasos siguientes correctos son: conservar la exportación de la configuración actual de la RTU y su registro de sesiones, y los registros del servidor de salto y de la estación de ingeniería de 06:30–06:50Z; informar al jefe de turno de Kestrel Water de que los valores de KW-09 no están disponibles (quizá necesiten una visita a la instalación para tomar lecturas manuales); abrir un registro de incidente. Restaurar la configuración anterior es la corrección, pero solo después de la conservación y con el acuerdo del responsable del incidente.

### 13.4 Segundo caso: el puesto corporativo en KW-04

El capítulo 10 dejó un elemento abierto: fw-01 deniega el tráfico de los puestos corporativos hacia las estaciones y, sin embargo, una captura en KW-04 mostró escrituras desde 10.30.3.7. Hipótesis: (a) algún dispositivo tradujo la dirección de origen de la captura; (b) existe otra ruta hacia KW-04 que elude fw-01. Comprobaciones de solo lectura: la exportación de la configuración del router celular de KW-04 muestra una redirección del puerto tcp/502 desde su dirección privada del lado del operador de telecomunicaciones, y la red privada de ese operador también es alcanzable desde la VPN corporativa de acceso remoto. La hipótesis (b) es coherente; la ruta se instaló durante una puesta en servicio de 2024 y nunca se retiró. La lección es de arquitectura (capítulo 15): cada router de estación es un límite potencial, y el modelo del capítulo 6 debe incluirlo.

### 13.5 El registro de diagnóstico

Escriba sobre la marcha, en UTC, con las cuatro etiquetas: *observado*, *inferido*, *hecho*, *abierto*. Un buen registro permite que un colega que toma el relevo en el cambio de turno continúe sin preguntarle nada, y permite que un investigador reconstruya después qué se cambió y cuándo. El capítulo 16 ofrece una plantilla; el capítulo 18 lo sella como evidencia del proyecto. Incluya referencias a la evidencia de cada observación, como el hash de la exportación de configuración de la RTU y el intervalo del registro del servidor de salto. En el Lab 18, el registro se convierte en 05-troubleshooting-log.md, y el hash de su manifiesto se verifica como OK cuando se comprueba el paquete.

### 13.6 Actividad práctica

Añada al Lab 13 la hipótesis H6 «el firmware de la RTU falló y pasó a un modo degradado», con las predicciones que crea que hace, y observe si las observaciones existentes la refutan. Si no lo hacen, nombre la única observación adicional de solo lectura que lo haría. Si las observaciones existentes no refutan H6, nombre una comprobación adicional de solo lectura, como un diagnóstico del fabricante que informe del estado del firmware, que sí lo haría. Escriba las predicciones antes de inventar la comprobación, para que la nueva observación tenga algo que contradecir. Mantenga H6 en la lista hasta que quede refutada o se haga cargo el proceso de incidentes.

### 13.7 Errores comunes y límites

- Tratar una hipótesis coherente como demostrada; solo está *aún sin refutar*.
- El Lab 13 compara valores predichos exactos; las observaciones reales tienen incertidumbre, y una sola observación poco fiable no debería refutar por sí sola una hipótesis.

- Reiniciar primero y destruir la evidencia volátil.
- Detenerse en la primera hipótesis que encaja en lugar de contrastar las predicciones con todas las observaciones.
- Declarar H4, el mapa de registros de la RTU cambiado, como la causa antes de que una exportación de la configuración lo confirme; el Lab 13 solo muestra que es coherente.
- Cambiar varias cosas a la vez, de modo que la corrección no puede atribuirse.

### Ejercicios — capítulo 13

**EX049 — Primero, las predicciones.** *Objetivo:* practicar el método. *Entradas:* la laguna de siete minutos de KW-05 del capítulo 8. *Pasos:* enumere tres hipótesis con sus predicciones para el ping, el establecimiento de la conexión TCP, la respuesta Modbus, los contadores de radio y las demás estaciones. *Evidencia esperada:* una tabla. *Rúbrica:* 3 = al menos una hipótesis de enlace, una de sondeo/SCADA y una relevante para la seguridad, con predicciones distintas para que las observaciones puedan separarlas; 2 = predicciones solapadas; 1 = solo hipótesis; 0 = nada.

**EX050 — Añada H6.** *Objetivo:* ampliar el laboratorio. *Entradas:* la actividad 13.6. *Pasos:* impleméntela y ejecútela. *Evidencia esperada:* código, salida y la observación adicional. *Rúbrica:* 3 = predicciones verosímiles (por ejemplo, ping verdadero, conexión verdadera, respuesta con tiempo de espera agotado o excepción 04); reconoce que, si H6 predice la excepción 02, no queda refutada, y propone una comprobación de solo lectura como la página de diagnóstico o el contador de tiempo en funcionamiento de la RTU; 2 = se ejecuta sin razonamiento; 1 = intentado; 0 = nada.

**EX051 — El momento del escalado.** *Objetivo:* reconocer cuándo parar y conservar. *Entradas:* el caso de KW-09. *Pasos:* redacte el mensaje de escalado al responsable del incidente y la lista de elementos conservados, con sus horas. *Evidencia esperada:* mensaje y lista. *Rúbrica:* 3 = el mensaje expone los hechos observados y la sesión sin explicar, separa la inferencia, pide una decisión sobre la restauración; los elementos conservados incluyen la exportación de la configuración y el registro de sesiones de la RTU, los registros de jump-01 y eng-ws-15 de la ventana, el propio registro de diagnóstico, cada uno con hash; 2 = bueno pero sin hashes; 1 = «nos han hackeado»; 0 = nada.

**EX052 — Cierre la ruta de KW-04.** *Objetivo:* corregir el desvío encontrado en 13.4. *Entradas:* la redirección de puerto del router y la alcanzabilidad desde la VPN. *Pasos:* proponga el cambio, su paso de conservación, sus pruebas y su responsable. *Evidencia esperada:* plan de cambio. *Rúbrica:* 3 = conservar primero la configuración del router; eliminar la redirección de puerto; restringir el acceso a la red privada del operador desde la VPN corporativa; prueba negativa desde un cliente VPN señalado y prueba positiva del sondeo del SCADA; comprobar el mismo patrón en todos los demás routers de estación; responsable nombrado; 2 = corrección sin comprobación amplia; 1 = solo eliminar; 0 = nada.

### Síntesis del capítulo

El diagnóstico de averías en un servicio crítico es un método, no una corazonada: definir el síntoma, observar en solo lectura, escribir hipótesis con predicciones, descartar con evidencia, conservar y, después, cambiar una sola cosa y verificar. Cuando una observación no se explica por una actividad aprobada, la avería se ha convertido en un posible incidente: deténgase, conserve y escale. El registro que lleva es a la vez el traspaso de turno y la evidencia.

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Siga estudiando — capítulo 13 de 18

[← Capítulo 12](#ch-12) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Infraestructura crítica y seguridad sectorial: automatización

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- automatizar la **detección de derivas** de la configuración con hashes criptográficos y un manifiesto aprobado;
- clasificar las diferencias como ausentes, nuevas, cambio aprobado o cambio no aprobado, y actuar de forma distinta en cada caso;
- diseñar una automatización segura para entornos de control: solo lectura por defecto, radio de impacto pequeño, conservar antes de revertir y aprobación humana para todo lo que toque el proceso;
- proteger la propia automatización, ya que una herramienta que puede cambiar todos los equipos es un objetivo.

Los capítulos 10–13 cambiaron, verificaron y diagnosticaron a mano. Este capítulo automatiza las comprobaciones repetibles, para que la atención del técnico se dirija a las diferencias que importan.

### 14.1 Por qué hashes

Un resumen SHA-256 ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)) de un archivo cambia si cambia cualquier byte, y es inviable construir un archivo distinto con el mismo resumen. Comparar los resúmenes con un manifiesto registrado en un momento en que todo era correcto le dice **qué** archivos cambiaron, de forma barata y sin guardar copias. No le dice **cómo** cambiaron (para eso necesita la copia aprobada, guardada en control de versiones), ni **si** el cambio fue legítimo (para eso necesita los registros de cambio). El módulo `hashlib` de Python ofrece SHA-256 en la biblioteca estándar ([Python hashlib](https://docs.python.org/3/library/hashlib.html)).

### 14.2 Cuatro resultados, cuatro acciones

| Resultado | Significado | Acción |
|---|---|---|
| Sin cambios | Coincide con el manifiesto | Nada |
| Cambiado, aprobado | Lo cubre un registro de cambio | Verificar (capítulo 11) y después actualizar el manifiesto |
| Cambiado, no aprobado | Sin registro | **Conservar**, investigar y después revertir mediante un cambio |
| Nuevo o ausente | El archivo apareció o desapareció | Investigar antes de borrar o restaurar |

El error de automatización más peligroso es «revertir automáticamente toda deriva». Destruye la evidencia de un cambio no aprobado y puede deshacer una corrección de emergencia hecha a las 03:00 que aún no se ha documentado. La *detección* automatizada es barata y segura; la *corrección* automatizada necesita una lista breve y explícita de lo que puede corregirse automáticamente, y nada que toque el control del proceso.

### 14.3 Ejemplo resuelto: deriva en hist-02 (sintético)

Una tarea nocturna compara los archivos clave de hist-02 con el manifiesto aprobado después de CHG-2207. El Lab 14 simula una noche, usando un directorio temporal. **Lab 14** (guárdelo como `lab14.py` y ejecútelo con `python3 lab14.py`):

```python
# Lab 14 - detect configuration drift against an approved manifest (offline, standard library only)
# Files are created in a temporary directory that is removed at the end.
import hashlib, json, pathlib, tempfile
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    files = {"sshd_config": "ListenAddress 10.90.0.21\nPermitRootLogin no\nPasswordAuthentication no\n",
             "ntp.conf": "server 10.90.0.5 iburst\n",
             "fw-01.rules": "R1 allow 10.20.0.10 10.10.0.0/16 tcp 502\nR7 deny any any\n"}
    for n, t in files.items(): (root / n).write_text(t)
    manifest = {n: sha(root / n) for n in files}                       # approved baseline
    approved_changes = {"ntp.conf": "CHG-2210"}
    (root / "ntp.conf").write_text("server 10.90.0.5 iburst\nserver 10.90.0.6 iburst\n")   # approved
    (root / "sshd_config").write_text(files["sshd_config"].replace("PermitRootLogin no", "PermitRootLogin yes"))
    (root / "debug.sh").write_text("nc -l -p 9000\n")                  # new, unexpected file
    current = {p.name: sha(p) for p in sorted(root.iterdir())}
    for name in sorted(set(manifest) | set(current)):
        if name not in current: print(f"MISSING   {name}")
        elif name not in manifest: print(f"NEW       {name}  -> investigate before removing")
        elif current[name] != manifest[name]:
            tag = f"approved ({approved_changes[name]}) -> update baseline" if name in approved_changes else "UNAPPROVED -> preserve, then revert"
            print(f"CHANGED   {name}  {tag}")
        else: print(f"unchanged {name}")
    print("manifest digest", hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()[:16])
```

Salida esperada (Python 3.13.5):

```text
NEW       debug.sh  -> investigate before removing
unchanged fw-01.rules
CHANGED   ntp.conf  approved (CHG-2210) -> update baseline
CHANGED   sshd_config  UNAPPROVED -> preserve, then revert
manifest digest fdea74f1d09e359c
```

`fw-01.rules` no ha cambiado. `ntp.conf` cambió y CHG-2210 lo cubre (se añadió un segundo servidor NTP): verifique que la hora está sincronizada y después actualice el manifiesto. `sshd_config` cambió sin registro: alguien volvió a habilitar el inicio de sesión de root. `debug.sh` es nuevo y contiene una orden que deja algo a la escucha. Ambos se conservan (copia, hash, marcas de tiempo, la cuenta que los escribió por última vez si el equipo lo registra) antes de revertir nada, y es muy probable que el segundo se convierta en un incidente. Se imprime el resumen del propio manifiesto para que también pueda comprobarse; guarde ese resumen en un lugar que los administradores del equipo no puedan modificar (capítulo 18).

### 14.4 Automatización segura en entornos de control

- **Primero, solo lectura.** La automatización más valiosa se limita a recoger y comparar: configuraciones, versiones de firmware, listas de cuentas, reglas de cortafuegos, caducidad de certificados.
- **Radio de impacto pequeño.** Actúe sobre un equipo o unos pocos; deténgase si muchos equipos difieren de la misma manera, lo que suele significar que el estado deseado o el recolector están mal.
- **Ritmo y momento.** El tráfico de recogida hacia los dispositivos de campo debe respetar el presupuesto de sondeo (capítulo 1) y no ejecutarse nunca en periodos críticos para el proceso sin acuerdo.
- **Aprobación humana** para todo cambio que pueda afectar al proceso, por pequeño que sea.
- **Registre cada ejecución** en el colector, con lo que se leyó y lo que se cambió.

### 14.5 Proteger la automatización

La cuenta de automatización puede leer o cambiar todos los equipos que gestiona, así que: guarde sus credenciales en una bóveda y rótelas; restrinja desde dónde puede conectarse; exija revisión de los cambios en su estado deseado; alerte de las ejecuciones fuera del calendario. El aviso de CISA sobre el acceso prolongado a infraestructuras críticas describe actores que usan herramientas de administración legítimas y cuentas válidas ([CISA AA24-038A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a)); una cuenta de automatización con privilegios excesivos es exactamente una herramienta así.

Una herramienta que puede cambiar todos los equipos es tan atractiva para un adversario como una estación de ingeniería. Revise los cambios de su estado deseado igual que revisa los cambios del cortafuegos.

### 14.6 Actividad práctica

Amplíe el Lab 14 para que, ante un cambio no aprobado, escriba un registro de conservación (nombre del archivo, resumen anterior, resumen nuevo, tamaño y hora de modificación) en el directorio temporal antes de imprimir el hallazgo, e imprima el SHA-256 del propio registro de conservación. Escriba el registro de conservación antes de imprimir el hallazgo e incluya en la salida el resumen del propio registro. Así, un investigador posterior podrá demostrar que la copia tomada en el momento de la detección coincide con lo que la tarea afirmó guardar. Mantenga la limpieza del directorio temporal después de registrar los hashes.

### 14.7 Errores comunes y límites

- Solo hashes; ninguna copia aprobada con la que comparar el contenido.
- El Lab 14 ignora los permisos, la propiedad y las marcas de tiempo, que importan tanto como el contenido (un archivo de servicio con escritura para todos es una deriva).

- Revertir automáticamente toda deriva y destruir la evidencia de un cambio no aprobado.
- Guardar el manifiesto en el equipo que protege.
- Calcular hashes solo del contenido e ignorar los permisos que hacen que un archivo de servicio tenga escritura para todos.
- Sondear los dispositivos de campo de forma tan agresiva que falla el ciclo de sondeo.
- Informar de una deriva sin anotar con qué versión aprobada de la línea base se comparó.

### Ejercicios — capítulo 14

**EX053 — Clasifique y actúe.** *Objetivo:* aplicar los cuatro resultados. *Entradas:* la salida del Lab 14. *Pasos:* escriba la acción y el responsable de cada línea, en orden de ejecución. *Evidencia esperada:* lista ordenada. *Rúbrica:* 3 = conservar primero sshd_config y debug.sh (copia, hash, metadatos), avisar a la responsable de seguridad; investigar debug.sh antes de eliminarlo; revertir sshd_config mediante un cambio tras la conservación; verificar NTP y actualizar el manifiesto para ntp.conf; nada para fw-01.rules; 2 = orden erróneo; 1 = revertirlo todo; 0 = nada.

**EX054 — Lista de correcciones automáticas.** *Objetivo:* limitar la automatización. *Entradas:* correcciones automáticas candidatas: reactivar el reenvío de registros, restablecer sshd_config, reiniciar el servicio del historiador, corregir la lista de servidores NTP, aplicar reglas de cortafuegos, restablecer el punto de consigna de un PLC. *Pasos:* marque cada una como corrección automática, incidencia o no automatizar nunca, con sus motivos. *Evidencia esperada:* seis filas. *Rúbrica:* 3 = reenvío de registros y lista NTP como corrección automática (restauran la visibilidad y la hora, bajo riesgo para el proceso); sshd_config y aplicación de reglas de cortafuegos mediante incidencia (riesgo para la conservación y de quedarse fuera); reinicio del historiador mediante incidencia con operaciones; el punto de consigna del PLC nunca automatizado por herramientas de seguridad; 2 = una errónea; 1 = todas automáticas; 0 = nada.

**EX055 — Salvaguarda de detención.** *Objetivo:* reducir el radio de impacto. *Entradas:* una flota de 14 equipos; una noche, 9 muestran `ntp.conf` cambiado de forma idéntica. *Pasos:* proponga una condición de detención y explique qué significa probablemente el patrón. *Evidencia esperada:* salvaguarda y explicación. *Rúbrica:* 3 = detener cuando más de una proporción fijada (por ejemplo, el 25 %) de los equipos muestre el mismo cambio; lo más probable es un cambio deliberado de la flota sin registrar o un manifiesto erróneo: confirmarlo con el calendario de cambios antes de cualquier acción; seguir tratándolo como hallazgo hasta que se explique; 2 = salvaguarda sin interpretación; 1 = revertir los nueve; 0 = nada.

**EX056 — Registro de conservación.** *Objetivo:* ampliar el laboratorio. *Entradas:* la actividad 14.6. *Pasos:* impleméntelo y muestre la salida. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = el registro se escribe antes de la línea del hallazgo, contiene los campos requeridos y se imprime su resumen; explica por qué el resumen del registro debe guardarse fuera del equipo; 2 = registro sin resumen; 1 = intentado; 0 = nada.

### Síntesis del capítulo

Automatice las comprobaciones que nunca cambian: recoger, calcular hashes, comparar con un manifiesto aprobado y clasificar las diferencias. Actúe de forma distinta ante los elementos aprobados, no aprobados, nuevos y ausentes (conserve antes de revertir) y limite la corrección automática a una lista breve que nunca toque el proceso. Proteja la automatización como la herramienta poderosa que es.

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Siga estudiando — capítulo 14 de 18

[← Capítulo 13](#ch-13) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Infraestructura crítica y seguridad sectorial: integración y dependencias

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- modelar las dependencias técnicas (virtualización, directorio, hora, almacenamiento, telecomunicaciones, energía) como un grafo y calcular a qué afecta un único fallo;
- encontrar los componentes compartidos entre servicios y sectores, incluida la compartición indirecta a través de una dependencia de una dependencia;
- tratar cada punto de integración (routers de estación, redes de operadores de telecomunicaciones, pasarelas de proveedores, exportaciones de datos) como un límite que hay que modelar, controlar y supervisar;
- convertir un análisis de dependencias en comprobaciones y controles concretos.

El capítulo 13 encontró una ruta hacia KW-04 que eludía el cortafuegos a través de la red de un operador de telecomunicaciones. Era una dependencia que nadie había dibujado. Este capítulo las dibuja de forma sistemática.

### 15.1 Interdependencia

Las infraestructuras críticas dependen unas de otras de forma física (la energía para las bombas), a través de la información (la telemetría sobre la red de un operador), geográfica (conductos e instalaciones compartidos) y lógica (personal, software y administración compartidos). Esta clasificación procede del artículo, ampliamente citado, de Rinaldi, Peerenboom y Kelly ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131)). Para un técnico, las sorpresas más frecuentes son *lógicas*: un directorio, un clúster de hipervisores, una fuente de hora o un colector de supervisión compartidos por sistemas cuyos responsables creen, cada uno, que es suyo.

Para un técnico, las sorpresas más frecuentes son lógicas: un directorio, un hipervisor o una fuente de hora que comparten varios servicios sin que ningún responsable los reclame. Dibújelos primero, y después los enlaces físicos y de los operadores de telecomunicaciones. El Lab 15 hace visibles los nodos compartidos como recuentos entre servicios.

### 15.2 Las dependencias como grafo

Escriba cada dependencia como «A necesita B». Para averiguar qué falla cuando falla B, siga las aristas **hacia atrás**: todo lo que necesita B, todo lo que necesita eso, y así sucesivamente. Es una búsqueda en anchura sobre el grafo invertido. Importan dos resultados: el **conjunto de servicios** afectados y la **ruta** por la que se ve afectado cada uno, porque la ruta le dice dónde un control o una redundancia romperían la cadena. La compartición indirecta es el caso importante. En el modelo del KVROC, el servidor del BMS del hospital y el servidor SCADA se autentican ambos contra `ad-ops`, que se ejecuta en `esx-03`, mientras que el procesador de comunicaciones de la red eléctrica también se ejecuta en `esx-03`. Ningún responsable de servicio considera `esx-03` como «suyo»; los tres dependen de él.

### 15.3 Ejemplo resuelto: las dependencias del KVROC (sintético)

**Lab 15** (guárdelo como `lab15.py` y ejecútelo con `python3 lab15.py`):

```python
# Lab 15 - trace failure impact through technical dependencies (offline, standard library only)
# Synthetic dependency map for the Kestrel Vale operations centre: "A needs B" edges.
from collections import deque
needs = {
 "water-telemetry": ["scada-01", "cell-router-kw", "fw-01"],
 "scada-01": ["ad-ops", "ntp-ops", "hist-02", "esx-02"],
 "hist-02": ["esx-02", "san-01"],
 "hospital-bms": ["bms-server", "fw-02"],
 "bms-server": ["esx-02", "ad-ops"],
 "grid-ss3-telecontrol": ["fep-01", "telco-mpls"],
 "fep-01": ["ntp-ops", "esx-03"],
 "ad-ops": ["esx-03"],
 "ntp-ops": ["gps-clock"],
}
def impacted(failed):
    rev = {}
    for a, bs in needs.items():
        for b in bs: rev.setdefault(b, []).append(a)
    seen, q = set(), deque([failed])
    while q:
        for a in rev.get(q.popleft(), []):
            if a not in seen: seen.add(a); q.append(a)
    return sorted(seen)
services = {"water-telemetry", "hospital-bms", "grid-ss3-telecontrol"}
for comp in ["esx-02", "esx-03", "gps-clock", "san-01", "telco-mpls"]:
    hit = impacted(comp)
    print(f"{comp:<10} -> services {sorted(services & set(hit))} via {len(hit)} dependants")
counts = {c: len(services & set(impacted(c))) for c in {b for bs in needs.values() for b in bs}}
print("shared by all three services:", sorted(c for c, n in counts.items() if n == 3))
```

Salida esperada (Python 3.13.5):

```text
esx-02     -> services ['hospital-bms', 'water-telemetry'] via 5 dependants
esx-03     -> services ['grid-ss3-telecontrol', 'hospital-bms', 'water-telemetry'] via 7 dependants
gps-clock  -> services ['grid-ss3-telecontrol', 'water-telemetry'] via 5 dependants
san-01     -> services ['water-telemetry'] via 3 dependants
telco-mpls -> services ['grid-ss3-telecontrol'] via 1 dependants
shared by all three services: ['esx-03']
```

`esx-02` aloja el servidor SCADA, el historiador y el servidor del BMS, de modo que su fallo afecta a la supervisión del agua y del hospital. `esx-03` es el único componente que afecta a los tres servicios: directamente al procesador de comunicaciones de la red eléctrica e indirectamente, a través del directorio, a los otros dos. `gps-clock`, la referencia de `ntp-ops`, afecta al agua y a la red eléctrica: perderlo no detiene nada de inmediato, pero el capítulo 7 mostró lo que hacen los relojes a la deriva con toda investigación posterior. `telco-mpls` solo afecta a la red eléctrica, y `san-01` solo al agua.

De ahí se siguen acciones técnicas: el directorio necesita un segundo controlador de dominio en otro servidor (y hay que probar el comportamiento del servidor SCADA cuando el directorio no está accesible: ¿pueden los operadores seguir iniciando sesión en la HMI?); `ntp-ops` necesita una segunda referencia independiente y supervisión del desfase; la capacidad de `esx-03` y su grupo de administradores pasan a ser una cuestión intersectorial que se revisa con los tres responsables.

### 15.4 Los puntos de integración son límites

Cada lugar en el que el servicio se conecta con algo que no controla es un límite:

- **Equipos de comunicación de las estaciones**: routers celulares, radios, la red privada del operador de telecomunicaciones. La redirección de puerto del capítulo 13 estaba aquí. La configuración de cada router debe figurar en el inventario de activos, bajo control de cambios y detección de derivas (capítulo 14).
- **Pasarelas de soporte remoto de los proveedores**: capítulo 10.
- **Exportaciones de datos**: el envío diario del historiador al servidor corporativo de informes (conducto C4 del capítulo 6). Las exportaciones deben enviarse hacia fuera desde el lado de control, nunca extraerse desde un equipo corporativo con credenciales dentro de la zona de control.
- **Servicios compartidos**: directorio, hora, supervisión. Sus administradores administran de hecho todo lo que depende de ellos.

El trabajo de CISA sobre las funciones críticas nacionales enmarca estas dependencias a escala nacional ([National Critical Functions](https://www.cisa.gov/national-critical-functions-set)); el técnico aplica el mismo razonamiento a un centro de operaciones.

### 15.5 Actividad práctica

Añada un nodo `power-ups-a` que necesitan tanto `esx-02` como `esx-03`, y un nodo `cell-carrier` que necesitan tanto `cell-router-kw` como `telco-mpls`. Vuelva a ejecutar el Lab 15 y anote qué componentes comparten ahora los tres servicios. Proponga después un cambio técnico para cada uno. Tras el cambio, anote qué componentes comparten los tres servicios y proponga una respuesta técnica para cada uno, como un segundo controlador de dominio o una segunda acometida eléctrica. Mantenga las aristas nuevas en el mismo formato que el laboratorio para que el grafo siga ejecutándose. Revise las propuestas con los tres responsables de servicio antes de cualquier cambio.

### 15.6 Errores comunes y límites

- Tratar el directorio y el servicio de hora como «infraestructura» sin responsable de servicio.
- Contar dependientes en lugar de examinar qué *servicios* se ven afectados y por qué *rutas*.
- El grafo del Lab 15 es binario (necesita / no necesita); las dependencias reales tienen modos degradados y temporizadores (una credencial en caché funciona durante horas; un reloj deriva lentamente).

- Enumerar solo las dependencias directas y pasar por alto el hipervisor que hay bajo el directorio.
- Dejar gps-clock sin un responsable nombrado, aunque el Lab 15 muestra que de él dependen tanto el telecontrol de la red eléctrica como la telemetría del agua.
- Suponer sin comprobarlo que un operador de telecomunicaciones aísla las redes privadas de sus clientes.
- Clasificar esx-03 por sus siete dependientes en lugar de señalar que es el único activo que comparten los tres servicios.

### Ejercicios — capítulo 15

**EX057 — Las rutas importan.** *Objetivo:* trazar una ruta de impacto. *Entradas:* el Lab 15. *Pasos:* modifique el programa para que imprima, para `esx-03`, una ruta de dependencia desde él hasta cada servicio afectado. *Evidencia esperada:* código y tres rutas. *Rúbrica:* 3 = por ejemplo, esx-03 → fep-01 → grid-ss3-telecontrol; esx-03 → ad-ops → scada-01 → water-telemetry; esx-03 → ad-ops → bms-server → hospital-bms; explica que un segundo directorio en otro servidor rompe dos de las tres; 2 = rutas sin interpretación; 1 = intentado; 0 = nada.

**EX058 — Nuevos componentes compartidos.** *Objetivo:* realizar la actividad. *Entradas:* la actividad 15.5. *Pasos:* ejecútela e interprétela. *Evidencia esperada:* salida y dos cambios técnicos. *Rúbrica:* 3 = `power-ups-a` y `esx-03` compartidos por los tres (y `cell-carrier` afectando al agua y a la red eléctrica); cambios como alimentaciones de SAI separadas para los dos servidores y un segundo operador o una ruta de radio para las estaciones más críticas; 2 = solo la salida; 1 = parcial; 0 = nada.

**EX059 — Prueba en modo degradado.** *Objetivo:* probar el comportamiento cuando falla una dependencia. *Entradas:* ad-ops no disponible. *Pasos:* redacte un plan de prueba delimitado, en una ventana de mantenimiento, para establecer si los operadores pueden seguir iniciando sesión en la HMI y si continúa el sondeo del SCADA. *Evidencia esperada:* plan de prueba con condiciones de parada. *Rúbrica:* 3 = probar primero en una réplica de reserva o de laboratorio; en producción, bloquear solo la ruta de la HMI hacia el directorio durante una ventana breve con operaciones presente; comprobar los inicios de sesión en caché, las cuentas locales de emergencia y la continuidad del sondeo; condiciones de parada; evidencia; 2 = sin el paso de la réplica; 1 = «apagar el controlador de dominio»; 0 = nada.

**EX060 — Sentido de la exportación.** *Objetivo:* configurar correctamente un límite. *Entradas:* actualmente, el servidor corporativo de informes inicia sesión cada noche en hist-02 con una contraseña guardada para extraer el CSV. *Pasos:* rediséñelo y enumere los cambios de configuración en ambos equipos y en fw-01. *Evidencia esperada:* diseño y cambios. *Rúbrica:* 3 = hist-02 envía por HTTPS a un único punto de destino; se elimina la credencial corporativa dentro de Z2; se invierte el sentido de la regla de fw-01 (solo Z2 → Z6, equipo y puerto específicos); se comprueba la integridad del envío (resumen en la carga útil o archivo firmado); supervisión de los envíos fallidos; 2 = envío sin eliminar la credencial antigua; 1 = vago; 0 = nada.

### Síntesis del capítulo

Los servicios fallan a través de aquello de lo que dependen, y las dependencias más peligrosas son las compartidas que ningún responsable reclama. Modele las dependencias como un grafo, recórralo hacia atrás desde cada componente y examine las rutas, no solo los recuentos. Trate cada punto de integración (routers de estación, operadores de telecomunicaciones, pasarelas de proveedores, exportaciones, directorio y hora) como un límite sujeto a la misma disciplina de control, cambio y supervisión que el cortafuegos.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Siga estudiando — capítulo 15 de 18

[← Capítulo 14](#ch-14) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Documentación técnica y seguridad física

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- redactar documentos técnicos que otro técnico pueda ejecutar con seguridad: instrucciones de trabajo, registros de diagnóstico, registros de cambio y registros de la configuración tal como se construyó;
- integrar la **seguridad física y del proceso** en el trabajo técnico: permisos, aislamiento, la autoridad de operaciones y las condiciones de parada;
- controlar los **dispositivos transitorios** (portátiles y soportes extraíbles que se llevan a las instalaciones) para que no transporten malware ni datos entre zonas;
- mantener los secretos fuera de los documentos.

Los capítulos 1–15 produjeron hallazgos, cambios y evidencia. Este capítulo trata de los documentos que hacen que ese trabajo sea repetible y seguro, y de las reglas de seguridad física que prevalecen sobre cualquier plan técnico.

### 16.1 Los documentos de los que es responsable un técnico

| Documento | Finalidad | Debe contener |
|---|---|---|
| **Instrucción de trabajo** | Permite que un colega competente realice una tarea correctamente | Condiciones previas, pasos numerados con resultados esperados, condiciones de parada, reversión, a quién llamar |
| **Registro de diagnóstico** | Registra una investigación mientras ocurre | Horas UTC, cuatro etiquetas (observado, inferido, hecho, abierto), referencias a la evidencia |
| **Registro de cambio** | Autoriza y registra un cambio | Antes/después, motivo, pruebas (capítulo 11), reversión, ventana, quién aprueba, quién verifica |
| **Registro de la configuración tal como se construyó** | Indica lo que está realmente configurado | Versiones, resúmenes de la configuración (capítulo 14), desviaciones respecto al diseño y su aprobación |

Redacte los pasos como acciones en imperativo con un resultado observable: «Ejecute `sshd -T | grep -i passwordauthentication`; se espera `passwordauthentication no`». Un paso sin resultado esperado no puede comprobarse, y un documento que no puede comprobarse se irá alejando de la realidad.

### 16.2 La seguridad física es lo primero y corresponde a operaciones

En una planta de agua, una subestación o una sala de máquinas de un hospital, las personas responsables del proceso físico tienen autoridad sobre él. El trabajo de un técnico allí empieza con su permiso y se detiene a petición suya. Reglas prácticas:

- **Permisos y aislamiento**: el trabajo en los equipos del proceso o cerca de ellos sigue los procedimientos de permiso de trabajo y de aislamiento de la instalación; una tarea de seguridad no le exime.
- **Los sistemas de protección y de seguridad funcional** nunca se tocan en un trabajo de ciberseguridad: relés de protección de una subestación, sistemas instrumentados de seguridad, alarmas de gases medicinales.
- **Informe antes de actuar**: la sala de control sabe cuándo empieza, qué está haciendo y cuándo termina.
- **Las condiciones de parada** se escriben en toda instrucción de trabajo (capítulo 5) y se respetan de inmediato.

NIST SP 800-82 Rev. 3 trata la relación entre la seguridad de la TO y la seguridad funcional ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); el Cyber Assessment Framework del NCSC del Reino Unido considera que el conocimiento que tiene el operador de sus funciones esenciales es un fundamento de la seguridad ([NCSC CAF](https://www.ncsc.gov.uk/collection/caf)).

### 16.3 Dispositivos y soportes transitorios

Un portátil que visita las estaciones, el centro de control y la oficina corporativa es un puente a través de todas las zonas. Controles que puede aplicar un técnico:

- portátiles de ingeniería dedicados que nunca se unen a la red corporativa ni a internet;
- una imagen de referencia conocida y correcta, actualizada y analizada en un punto controlado antes de cada visita a una instalación;
- soportes extraíbles solo de un conjunto controlado, analizados antes de su uso, con un registro de dónde ha estado cada uno;
- ningún dispositivo personal en las redes de control;
- un registro de cada conexión hecha en una instalación (qué puerto, qué dispositivo, cuándo).

Los objetivos de rendimiento de CISA incluyen controles sobre los soportes extraíbles y sobre la configuración de los dispositivos ([CISA CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)).

### 16.4 Secretos e información sensible

Los documentos no deben contener contraseñas, claves privadas, tokens de API ni códigos de un solo uso. Escriba «credencial de la entrada de la bóveda `kw-rtu-eng`» en lugar de la credencial. Los diagramas de red, los mapas de registros y las exportaciones de cortafuegos de infraestructuras críticas son sensibles: guárdelos con control de acceso, compártalos según la necesidad de conocer y elimínelos de las incidencias que van a los proveedores. Este libro imprime algunos valores falsos solo porque son falsos.

El nombre de la entrada de la bóveda puede figurar sin riesgo en una incidencia de cambio, porque indica a un ingeniero autorizado dónde buscar sin revelar nada que un tercero pueda aprovechar. Los mapas de registros y las exportaciones de cortafuegos reales merecen el mismo cuidado que las credenciales, ya que juntos describen cómo puede cambiarse una estación y desde dónde.

### 16.5 Ejemplo resuelto: una instrucción de trabajo (sintético)

**WI-KW-07 — Exportar la configuración de la RTU de KW-04 para la línea base de derivas.** *Condiciones previas*: registro de cambio CHG-2219 aprobado; sala de control de Kestrel Water informada; portátil de ingeniería ENG-L3 analizado hoy (anotado en el registro de soportes). *Pasos*: (1) a las 10:00 hora local, llame a la sala de control; anote el nombre del operador. (2) En ENG-L3, abra la herramienta del fabricante en modo de solo lectura; resultado esperado: la barra de estado muestra «Online — read only». (3) Exporte la configuración a `KW04-20261013.cfg`; resultado esperado: tamaño del archivo entre 40 y 60 kB. (4) Ejecute `sha256sum KW04-20261013.cfg`; anote el resumen en CHG-2219. (5) Desconéctese; informe a la sala de control. *Condiciones de parada*: cualquier alarma en KW-04; la herramienta pide pasar a «online edit»; petición del operador. *Reversión*: no hace falta (solo lectura), pero si se sospecha alguna escritura, informe de inmediato a operaciones y abra un incidente. *Evidencia*: archivo, resumen, horas de las llamadas.

### 16.6 Actividad práctica

Redacte una instrucción de trabajo para el cambio del router de KW-04 de EX052, que incluya la conservación, el cambio, las pruebas positivas y negativas, la reversión y las condiciones de parada. Pida a otra persona que la lea y que enumere cada paso en el que tendría que adivinar. Incluya la conservación de la configuración del router antes del cambio, pruebas positivas y negativas después, los pasos de reversión y condiciones de parada que incluyan cualquier alarma de KW-04. Pida a un colega que marque cada paso en el que tendría que adivinar; esos pasos necesitan un resultado esperado o una captura de pantalla de la herramienta del fabricante. Guarde la copia revisada con el registro de cambio.

### 16.7 Errores comunes y límites

- Pasos sin resultados esperados.
- Documentos que contienen credenciales o se comparten demasiado.
- Tratar una visita a una instalación como una tarea de TI y saltarse el permiso o la llamada a la sala de control.
- Un portátil para todo.
- Documentación redactada después del trabajo, de memoria.

- Dejar fuera del procedimiento de la instalación la reversión de un cambio de regla de fw-01, de modo que un cambio fallido no tiene una vuelta atrás probada.
- Poner credenciales o exportaciones completas del cortafuegos en una incidencia de amplia difusión.
- Saltarse el permiso o la llamada a la sala de control porque la tarea parece TI corriente.
- Usar un mismo portátil para el trabajo corporativo, el del centro de control y el de las instalaciones.
- Redactar el documento de memoria después del trabajo.

### Ejercicios — capítulo 16

**EX061 — Repare una instrucción de trabajo.** *Objetivo:* hacer ejecutables los pasos. *Entradas:* «Inicie sesión en la RTU (contraseña Kestrel2024!) y revise los ajustes. Corrija lo que esté mal. Avise a operaciones al terminar». *Pasos:* enumere los defectos y reescríbala. *Evidencia esperada:* lista de defectos e instrucción reescrita. *Rúbrica:* 3 = elimina la credencial (y recomienda rotarla, puesto que se ha escrito), añade condiciones previas, modo de solo lectura, resultados esperados, condiciones de parada, informa antes a operaciones, sustituye «corrija lo que esté mal» por un registro de cambio; 2 = la mayoría; 1 = cosmético; 0 = nada.

**EX062 — Política de dispositivos transitorios.** *Objetivo:* controlar un puente entre zonas. *Entradas:* un ingeniero usa el mismo portátil para el correo y para el trabajo en las estaciones. *Pasos:* redacte una política técnica breve y el plan de transición. *Evidencia esperada:* política y plan. *Rúbrica:* 3 = portátiles de ingeniería dedicados con una imagen controlada, sin uso corporativo ni de internet, comprobación previa a la visita, conjunto y registro de soportes, registro de conexiones; una transición que conserve los archivos de proyecto del portátil actual tras analizarlos; 2 = política sin transición; 1 = «tenga cuidado»; 0 = nada.

**EX063 — Límites de seguridad física.** *Objetivo:* reconocer lo que está fuera de los límites. *Entradas:* durante una visita a una subestación, encuentra un relé de protección con una contraseña web por defecto. *Pasos:* indique lo que hace y lo que no hace, y cómo lo registra. *Evidencia esperada:* procedimiento breve. *Rúbrica:* 3 = no iniciar sesión ni cambiarla; registrar la observación (dispositivo, hora, cómo se advirtió); comunicarlo al ingeniero de protecciones de Kestrel Grid y a la responsable de seguridad del KVROC; los ingenieros de protecciones deciden y actúan; hallazgo sensible tratado según la necesidad de conocer; 2 = acciones correctas, registro débil; 1 = cambia la contraseña; 0 = nada.

**EX064 — Registro de la configuración tal como se construyó.** *Objetivo:* documentar la realidad. *Entradas:* fw-01 tras la corrección de EX038 y hist-02 tras CHG-2207. *Pasos:* redacte un borrador del registro con versiones, resúmenes (se admiten marcadores), desviaciones y aprobaciones. *Evidencia esperada:* registro de una página. *Rúbrica:* 3 = indica la configuración real, incluye los resúmenes y dónde se guardan, enumera las desviaciones abiertas (REQ-3/4 antes de la corrección) con sus aprobaciones o incidencias, fechado y firmado; 2 = sin desviaciones; 1 = copia el diseño; 0 = nada.

### Síntesis del capítulo

Los buenos documentos técnicos son ejecutables y comprobables: pasos numerados con resultados esperados, condiciones de parada, reversión y evidencia. La seguridad física y la autoridad de operaciones prevalecen sobre todo plan técnico; los sistemas de protección y de seguridad funcional quedan fuera de los límites. Los portátiles y los soportes que se desplazan entre zonas necesitan sus propios controles, y los secretos nunca deben figurar en los documentos.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Siga estudiando — capítulo 16 de 18

[← Capítulo 15](#ch-15) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Laboratorio contenido II

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- integrar las técnicas del curso (decodificación, capítulo 2; validación, capítulo 4; reglas de detección, capítulos 8 y 10; episodios y autocomprobaciones) en una única cadena de detección;
- redactar reglas de detección a partir del modelo del sistema, no del catálogo de un producto: interlocutor nuevo, escritura no autorizada, consulta de identificación;
- agrupar las alertas en **episodios** y explicar el compromiso que supone la ventana de agrupación;
- hacer que la cadena se supervise a sí misma: cada registro de entrada o se analiza o se cuenta como descartado;
- evaluar la cadena con una rúbrica e identificar sus puntos ciegos.

El capítulo 12 construyó un dispositivo. Este segundo laboratorio evaluado construye el vigilante, de la misma forma contenida: entradas sintéticas fijas, solo la biblioteca estándar, sin red.

### 17.1 Reglas a partir del modelo

Cada regla se deriva de un enunciado del modelo del sistema:

- **NEW-TALKER**: el modelo enumera los equipos que pueden hablar Modbus con las estaciones (scada-01, eng-ws-15). Cualquier otro origen es un hallazgo.
- **UNAUTH-WRITE**: solo la estación de ingeniería puede escribir (capítulo 2).
- **DEVICE-ID-QUERY**: la función 43 tiene forma de reconocimiento; alertar, con contexto.

Son deliberadamente sencillas y explicables (capítulo 8). MITRE ATT&CK for ICS cataloga las técnicas de los adversarios con las que se relacionan estas reglas, entre ellas el descubrimiento y los mensajes de órdenes no autorizadas ([ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)); úselo para comprobar la cobertura, no como fuente de las reglas.

### 17.2 Episodios

Un único equipo no autorizado puede generar decenas de alertas en un minuto. Agrupar las alertas con la misma regla y el mismo origen en un **episodio** (que se prolonga mientras lleguen alertas nuevas dentro de una ventana desde la anterior) da al analista un único elemento con un recuento y un intervalo de tiempo. La ventana es un compromiso: si es demasiado corta, una sola actividad se convierte en muchos episodios; si es demasiado larga, dos actividades distintas se fusionan. Anote la ventana elegida y por qué.

En el Lab 17, la ventana se mide desde la última alerta del episodio, no desde la primera, de modo que un goteo constante de alertas cada cuatro minutos prolongaría un episodio indefinidamente; limite la duración del episodio (por ejemplo, a una hora) o notifique los episodios largos como en curso con su hora más reciente. Una ventana de cinco minutos separa la escritura de las 07:12 en su propio episodio, que es lo que se quiere si, de otro modo, un analista podría pensar que la actividad se había detenido; una ventana mucho más larga la fusionaría con la ráfaga anterior y ocultaría la pausa.

### 17.3 La cadena se supervisa a sí misma

Un detector que descarta en silencio los registros que no puede analizar está ciego justo donde un atacante envía tráfico mal formado. La cadena debe dar cuenta de cada entrada: *registros = analizados + descartados*, comprobado con un assert, con los registros descartados enumerados y contados. Las orientaciones del NIST sobre supervisión continua plantean lo mismo a escala de programa: la propia supervisión debe supervisarse ([SP 800-137](https://csrc.nist.gov/pubs/sp/800/137/final)). En el Lab 17, la comprobación es la línea `assert parsed + len(dropped) == len(recs)`, y la línea de resumen imprime la propia lista de descartados: un registro, a las 07:03:03 desde 10.20.0.31, cuyo campo de longitud anuncia seis bytes a continuación cuando solo llegan dos. El descarte se cuenta, pero no genera ninguna alerta, porque las reglas solo se ejecutan sobre las tramas analizadas: la laguna que cierra la actividad práctica. Durante la guardia, trate el recuento de descartes como una señal en sí misma: un sensor que de pronto descarta muchos registros tiene un fallo de captura, un error de análisis o un interlocutor que envía tráfico mal formado a propósito, y cada una de esas causas merece una incidencia.

### 17.4 Ejemplo resuelto: la actividad de las 07:03 (sintético)

Diez registros del sensor del centro de control del 12 de octubre. **Lab 17** (guárdelo como `lab17.py` y ejecútelo con `python3 lab17.py`):

```python
# Lab 17 - contained detection pipeline for station traffic (offline, standard library only)
# Synthetic records: (UTC time, source, destination, Modbus/TCP frame hex). Rules come from Chapters 2, 9 and 10.
import struct
from datetime import datetime, timedelta
KNOWN = {"10.20.0.10": "scada-01", "10.20.0.15": "eng-ws-15"}
WRITERS = {"10.20.0.15"}
WRITE_FC = {5, 6, 15, 16}
recs = [
 ("07:00:00", "10.20.0.10", "10.10.4.2", "000100000006010300000004"),
 ("07:00:05", "10.20.0.10", "10.10.5.2", "000200000006010300000004"),
 ("07:02:10", "10.20.0.15", "10.10.4.2", "00030000000601060007012c"),
 ("07:03:00", "10.20.0.31", "10.10.4.2", "000400000006012b0e010000"),
 ("07:03:01", "10.20.0.31", "10.10.5.2", "000500000006012b0e010000"),
 ("07:03:02", "10.20.0.31", "10.10.6.2", "000600000006012b0e010000"),
 ("07:03:03", "10.20.0.31", "10.10.7.2", "0007000000060103"),
 ("07:04:40", "10.20.0.31", "10.10.4.2", "00080000000601060007ffff"),
 ("07:05:30", "10.20.0.31", "10.10.4.2", "00090000000601060007ffff"),
 ("07:12:00", "10.20.0.31", "10.10.4.2", "000a0000000601060007ffff"),
]
alerts, dropped, parsed = [], [], 0
for t, src, dst, hx in recs:
    b = bytes.fromhex(hx)
    if len(b) < 8 or struct.unpack(">H", b[4:6])[0] != len(b) - 6:
        dropped.append((t, src, "malformed")); continue
    parsed += 1; fc = b[7]
    if src not in KNOWN: alerts.append((t, "NEW-TALKER", src))
    if fc in WRITE_FC and src not in WRITERS: alerts.append((t, "UNAUTH-WRITE", src))
    if fc == 43: alerts.append((t, "DEVICE-ID-QUERY", src))
assert parsed + len(dropped) == len(recs), "pipeline lost records"
episodes = []   # merge same rule+source within 5 minutes of the previous alert in the episode
for t, rule, src in alerts:
    ts = datetime.strptime(t, "%H:%M:%S")
    e = next((e for e in episodes if e["key"] == (rule, src) and ts - e["last"] <= timedelta(minutes=5)), None)
    if e: e["count"] += 1; e["last"] = ts
    else: episodes.append({"key": (rule, src), "first": ts, "last": ts, "count": 1})
for e in episodes:
    print(f"{e['first']:%H:%M:%S}-{e['last']:%H:%M:%S}Z {e['key'][0]:<15} {e['key'][1]:<11} x{e['count']}")
print(f"records {len(recs)} parsed {parsed} dropped {len(dropped)} {dropped} alerts {len(alerts)} episodes {len(episodes)}")
```

Salida esperada (Python 3.13.5):

```text
07:03:00-07:05:30Z NEW-TALKER      10.20.0.31  x5
07:03:00-07:03:02Z DEVICE-ID-QUERY 10.20.0.31  x3
07:04:40-07:05:30Z UNAUTH-WRITE    10.20.0.31  x2
07:12:00-07:12:00Z NEW-TALKER      10.20.0.31  x1
07:12:00-07:12:00Z UNAUTH-WRITE    10.20.0.31  x1
records 10 parsed 9 dropped 1 [('07:03:03', '10.20.0.31', 'malformed')] alerts 12 episodes 5
```

Interpretación: un equipo nunca visto, 10.20.0.31, consultó la identificación de dispositivo de tres estaciones en tres segundos, envió una trama mal formada a una cuarta y después escribió 0xFFFF en el registro 7 (el punto de consigna de la bomba) de KW-04 dos veces, y otra vez seis minutos y medio después. Cinco episodios resumen doce alertas. Dos observaciones importan más allá de las propias alertas:

1. La **escritura de las 07:12** es un episodio aparte porque llegó más de cinco minutos después de la alerta anterior. Un analista que leyera solo los tres primeros episodios podría pensar que la actividad se había detenido.
2. La **trama mal formada** del interlocutor nuevo se descartó y no produjo ninguna alerta; la autocomprobación lo muestra, y es lo primero que hay que corregir: el tráfico no analizable desde un equipo desconocido debería generar por sí mismo NEW-TALKER, ya que la dirección de origen se conoce aunque la carga útil no.

El valor 0xFFFF (65.535) en un registro de punto de consigna cuyo rango de política es 100–400 es el tipo de escritura que el respondedor del Lab 12 rechazaría con la excepción 03, si el dispositivo tuviera esa política. La mayoría no la tiene, así que la detección del lado de la red y el cortafuegos (capítulo 10) son lo único que se interpone entre este equipo y el proceso. En la historia del KVROC, este es el momento de conservar, informar a Kestrel Water y abrir un incidente (capítulo 13).

### 17.5 Rúbrica de evaluación

| Criterio | 3 | 1 |
|---|---|---|
| Contención | Entradas fijas; sin red; declarada | Lee tráfico en servicio sin alcance definido |
| Procedencia de las reglas | Cada regla cita el enunciado del modelo que aplica | Reglas de una lista sin justificación |
| Autosupervisión | Se da cuenta de los registros; descartados enumerados | Descartes silenciosos |
| Diseño de los episodios | Ventana declarada con su compromiso | Arbitraria o inexistente |
| Puntos ciegos | Enumera lo que el sensor no puede ver (tráfico local de las estaciones, enlaces cifrados) | Afirma una cobertura completa |
| Reproducibilidad | Salida registrada con la versión de Python | Sin registrar |

Puntúe el Lab 17 en cada fila y escriba una mejora para cada puntuación inferior a tres. Los puntos ciegos deben incluir el tráfico local de las estaciones y cualquier ruta que no pase por el sensor del centro de control, como encontró el capítulo 13 para KW-04. Guarde la rúbrica puntuada con la salida del laboratorio y la versión de Python.

### 17.6 Actividad práctica

Cambie la cadena para que un registro descartado (mal formado) desde un origen desconocido genere NEW-TALKER, y añada una regla que alerte de cualquier escritura cuyo valor esté fuera del rango de política del registro, usando la tabla de política del Lab 12. Anote la nueva salida y cómo cambian los episodios. Antes de cambiar el código, guarde la salida actual como referencia y anote su predicción: qué episodio debería crecer y cuántas alertas debería añadir la regla de rango de valores. Tras el cambio, la línea de registros debe seguir cuadrando en diez (nueve analizados, uno descartado): corregir el descarte ciego cambia lo que produce el registro descartado, no si se cuenta. Pruebe la regla de rango de valores en ambos sentidos (debe dispararse con las escrituras de 0xFFFF y permanecer en silencio con la escritura de 300 (0x012c) de eng-ws-15 a las 07:02:10) y vuelva a puntuar después las filas de autosupervisión y de procedencia de las reglas de 17.5.

### 17.7 Errores comunes y límites

- Reglas copiadas de un catálogo sin un enunciado del modelo que las respalde.
- Episodios tan largos que la actividad diferenciada desaparece.
- Descartar en silencio los registros mal formados.
- Creer que el sensor lo ve todo: el capítulo 13 encontró una ruta hacia KW-04 que no pasaba por este sensor.
- Las marcas de tiempo de la cadena son las del sensor; corrija su reloj como cualquier otro (capítulo 7).

Comprobaciones que detectan estos errores:

- Para cada regla, cite la línea del modelo del sistema que aplica; una regla sin ella se elimina, o primero se actualiza el modelo.
- Ejecute los episodios con dos ventanas (como en EX067) y confirme que la escritura de las 07:12 sigue siendo visible, ya sea como elemento propio o como un intervalo prolongado.
- Haga fallar la ejecución cuando los registros no sean iguales a los analizados más los descartados, y revise la lista de descartados en cada turno.
- Mantenga una lista escrita de las rutas que eluden el sensor (routers celulares de las estaciones, tráfico de la HMI local de las estaciones) junto a la declaración de cobertura de la detección.

### Ejercicios — capítulo 17

**EX065 — Lea los episodios.** *Objetivo:* interpretar la salida de la cadena. *Entradas:* la salida del Lab 17. *Pasos:* redacte un resumen de cinco líneas para el jefe de turno del KVROC usando las cuatro etiquetas. *Evidencia esperada:* resumen. *Rúbrica:* 3 = observado: equipo desconocido 10.20.0.31, consultas de identificación a tres estaciones, escrituras de 65.535 en el registro 7 de KW-04 a las 07:04:40, 07:05:30 y 07:12:00, una trama mal formada; inferido: reconocimiento seguido de intentos de cambiar el punto de consigna; hecho: no se cambió nada; abierto: identidad del equipo, efecto sobre KW-04, ruta; pide a operaciones que compruebe la bomba 2 de KW-04; 2 = sin etiquetas; 1 = vago; 0 = nada.

**EX066 — Corrija el descarte ciego.** *Objetivo:* mejorar la autosupervisión. *Entradas:* la actividad 17.6 (primera mitad). *Pasos:* impleméntela y ejecútela. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = el episodio NEW-TALKER de 10.20.0.31 se amplía ahora a seis registros dentro del mismo episodio (07:03:00–07:05:30 x6), total de alertas 13; se sigue dando cuenta de los registros; 2 = funciona, recuentos sin explicar; 1 = intentado; 0 = nada.

**EX067 — Compromiso de la ventana.** *Objetivo:* razonar sobre la agrupación. *Entradas:* el Lab 17. *Pasos:* prediga el número de episodios con ventanas de 1 minuto y de 10 minutos, y después ejecute. *Evidencia esperada:* predicciones y salidas. *Rúbrica:* 3 = 1 minuto: NEW-TALKER se divide (07:03:00–07:03:02, 07:04:40–07:05:30, 07:12:00), UNAUTH-WRITE se divide en 07:04:40–07:05:30 y 07:12:00, DEVICE-ID uno → 6 episodios; 10 minutos: NEW-TALKER y UNAUTH-WRITE un episodio cada uno → 3 episodios; recomienda un valor con su motivo; 2 = casi todo correcto; 1 = conjeturas; 0 = nada.

**EX068 — Regla de rango de valores.** *Objetivo:* combinar la política del dispositivo y la detección en la red. *Entradas:* la actividad 17.6 (segunda mitad). *Pasos:* impleméntela para las funciones 6 y 16 y ejecútela. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = alerta de las tres escrituras de 0xFFFF y no de la escritura de 300 de eng-ws-15; explica que la regla detecta pero no impide, así que el cortafuegos sigue siendo necesario; 2 = solo la función 6; 1 = intentado; 0 = nada.

### Síntesis del capítulo

Una cadena de detección es un pequeño sistema con sus propios requisitos: reglas que remiten al modelo del sistema, episodios que resumen sin ocultar y una autocomprobación que da cuenta de cada registro. Construida de forma contenida y evaluada con honestidad, incluidos sus puntos ciegos, convierte las técnicas separadas del curso en algo sobre lo que un jefe de turno puede actuar.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Siga estudiando — capítulo 17 de 18

[← Capítulo 16](#ch-16) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Proyecto técnico supervisado

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- planificar y ejecutar bajo supervisión un proyecto técnico acotado en un entorno crítico: alcance, línea base, cambio, verificación, registro de diagnóstico y traspaso;
- reunir el **paquete de evidencias** de un proyecto y sellarlo con un manifiesto de resúmenes SHA-256 y un sello registrado por separado;
- detectar cualquier cambio posterior en la evidencia sellada y explicar lo que un sello demuestra y lo que no;
- presentar el proyecto para su evaluación con una rúbrica y declarar con honestidad sus puntos abiertos.

Este capítulo cierra el curso. Aplica todo lo anterior a una única tarea realista, y su resultado es lo que un empleador o un evaluador pediría ver: no una afirmación de competencia, sino la evidencia de ella.

### 18.1 Elegir un proyecto

Un buen proyecto supervisado es acotado, valioso y comprobable. Ejemplos tomados de este libro: bastionar el conducto entre la red corporativa y el centro de control y verificarlo (capítulos 10–11); cerrar la elusión por los routers de estación en todas las estaciones (capítulo 13); desplegar la detección de derivas en los servidores del centro de control (capítulo 14); construir y probar la cadena de detección con una captura saneada y reproducida (capítulo 17). Todo proyecto necesita un **supervisor** (aquí L. Ferreira) y un **autorizador** responsable de los sistemas afectados (aquí A. Mensah, por Kestrel Water).

Acuerde antes del primer día el supervisor, el responsable que firma el alcance y los criterios de éxito. Elija un conducto o una clase de equipos, no el programa entero. Anote los puntos abiertos que espera dejar, de modo que la honestidad sobre los límites se planifique en lugar de improvisarse en la evaluación.

### 18.2 Fases

1. **Alcance** (capítulo 5): propósito, sistemas, acciones, ventana, personas, condiciones de parada, tratamiento de la evidencia, firmado.
2. **Línea base**: exportaciones de configuración y resúmenes antes de cambiar nada (capítulo 14); resultados actuales de las pruebas (capítulo 11).
3. **Cambio**: bajo un registro de cambio con marcha atrás (capítulo 10).
4. **Verificación**: pruebas positivas y negativas, cada requisito verificado, fallido o sin probar.
5. **Registro de diagnóstico** durante todo el proyecto, con las cuatro etiquetas (capítulo 13).
6. **Traspaso**: registro de la configuración tal como se construyó, instrucciones de trabajo, puntos abiertos con responsables (capítulo 16).
7. **Paquete de evidencias**: todo lo anterior, sellado.

No omita los resúmenes de la línea base aunque el cambio parezca pequeño; sin ellos no puede demostrar qué cambió. Mantenga abierto el registro de diagnóstico durante toda la ventana, incluidas las interrupciones y los intentos fallidos. El paquete de evidencias va al final, cuando ya existen los documentos de traspaso que incluir en él.

### 18.3 Sellar la evidencia

Un **manifiesto** enumera cada elemento con su resumen SHA-256 ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)). El **sello** es el resumen del propio manifiesto. Registre el sello **fuera** del paquete (en el registro de cambio, en un correo al supervisor, en el formulario de evaluación), porque quien pueda editar el paquete también puede editar un manifiesto guardado dentro de él. Más adelante, recalcular los resúmenes de los elementos muestra si algo ha cambiado; recalcular el resumen del manifiesto y compararlo con el sello registrado externamente muestra si el manifiesto se ha alterado.

Lo que un sello demuestra: que los elementos son, byte a byte, lo que eran cuando se sellaron. Lo que no demuestra: que fueran ciertos, completos o creados cuando afirman. Eso depende de cómo se recogieron (capítulo 5) y de registros independientes (registros del cortafuegos en el recolector, tickets de cambio en su propio sistema). Para garantías más sólidas, las organizaciones usan firmas con claves custodiadas por un tercero o un sellado de tiempo de confianza; el principio es el mismo.

### 18.4 Ejemplo resuelto: el proyecto del conducto de KW-04 (sintético)

El proyecto de R. Kaur eliminó la regla corporativa amplia R4 de fw-01 (CHG-2215), verificó el resultado e investigó por el camino el evento de KW-09. El paquete de evidencias se sella y, una semana después, se vuelve a verificar. **Lab 18** (guárdelo como `lab18.py` y ejecútelo con `python3 lab18.py`):

```python
# Lab 18 - seal and re-verify a project evidence package (offline, standard library only)
# Synthetic artefacts from the supervised project; written only inside a temporary directory.
import hashlib, pathlib, tempfile
artefacts = {
 "01-scope.md": "Scope: KW-04 conduit hardening; authorized by A. Mensah (Kestrel Water) 2026-10-05.\n",
 "02-before-fw.txt": "R4 allow 10.30.0.0/16 10.20.0.0/24 tcp any\n",
 "03-after-fw.txt": "R4 removed CHG-2215\n",
 "04-tests.csv": "test,result\nT4,pass\nT5,pass\nT9,pass\n",
 "05-troubleshooting-log.md": "07:05Z KW-09 missing; H4 consistent; RTU config preserved as E-17.\n",
}
with tempfile.TemporaryDirectory() as tmp:
    d = pathlib.Path(tmp)
    for n, t in artefacts.items(): (d / n).write_text(t)
    lines = [f"{hashlib.sha256((d / n).read_bytes()).hexdigest()}  {n}" for n in sorted(artefacts)]
    (d / "MANIFEST.sha256").write_text("\n".join(lines) + "\n")
    seal = hashlib.sha256((d / "MANIFEST.sha256").read_bytes()).hexdigest()
    print("manifest:")
    for l in lines: print(" ", l[:16] + "...", l.split("  ")[1])
    print("seal (record this outside the package):", seal[:24])
    (d / "04-tests.csv").write_text("test,result\nT4,pass\nT5,pass\nT9,pass\nT10,pass\n")   # later edit
    for l in (d / "MANIFEST.sha256").read_text().splitlines():
        h, n = l.split("  ")
        ok = hashlib.sha256((d / n).read_bytes()).hexdigest() == h
        print(f"verify {n:<26} {'OK' if ok else 'MISMATCH'}")
```

Salida esperada (Python 3.13.5):

```text
manifest:
  72d8be01e70067c7... 01-scope.md
  8d52d15a3e02b7f8... 02-before-fw.txt
  2cd59665641b4779... 03-after-fw.txt
  d6eccc2e2ac61ecb... 04-tests.csv
  6d2525605f11521c... 05-troubleshooting-log.md
seal (record this outside the package): 062b9a1fd700dd0eac04b3a8
verify 01-scope.md                OK
verify 02-before-fw.txt           OK
verify 03-after-fw.txt            OK
verify 04-tests.csv               MISMATCH
verify 05-troubleshooting-log.md  OK
```

Cuatro elementos se verifican; `04-tests.csv` no. Alguien añadió una línea T10 después del sellado. Puede ser una prueba posterior legítima, pero debe añadirse como un elemento nuevo, fechado por separado y con su propia entrada, no editando un archivo sellado. El evaluador pide a R. Kaur que restaure la versión sellada desde el archivo (su resumen debe coincidir con el manifiesto) y que presente T10 como `06-tests-addendum.csv` en una versión nueva y resellada del paquete, con ambos sellos registrados.

### 18.5 Rúbrica de evaluación del proyecto

| Criterio | 3 (cumple el resultado técnico) | 1 |
|---|---|---|
| Alcance y autorización | Alcance firmado con responsable, ventana y condiciones de parada | Aprobación verbal |
| Corrección técnica | El cambio cumple los requisitos; sin daños colaterales | Parcial o perjudicial |
| Verificación | Todos los requisitos verificados o explícitamente abiertos, pruebas positivas y negativas con evidencia | Solo recuentos de aprobados |
| Diagnóstico | Hipótesis, predicciones, descartes, conservación | Narración |
| Documentación | Instrucciones de trabajo ejecutables, registro de la configuración tal como se construyó, sin secretos | Notas de memoria |
| Evidencia | Manifiesto, sello externo, ejecución de verificación | Carpeta de capturas de pantalla |
| Honestidad sobre los límites | Puntos abiertos con responsables; puntos ciegos declarados | «Todo hecho» |

### 18.6 Práctica continua

Después del curso, mantenga tres hábitos: verificar antes de informar, conservar antes de cambiar y corregir los relojes antes de ordenar los eventos. Mantenga los laboratorios contenidos y no pruebe nunca una infraestructura real sin la autorización escrita de su responsable. Revise las normas y orientaciones cuando cambien; todas las fuentes de este libro están fechadas en octubre de 2026. Convierta el trabajo del curso en un portafolio: planes con alcance, salidas de los laboratorios con sus versiones de Python, registros de diagnóstico y el paquete sellado de este capítulo, con cada sello registrado fuera de su paquete. Cuando pase a una versión nueva de Python, vuelva a ejecutar los laboratorios y compare las salidas; una diferencia es un hallazgo que hay que explicar, no ocultar. Busque trabajo supervisado en el que pueda repetir el ciclo completo (alcance, línea base, cambio, verificación, traspaso) sobre un sistema real con la firma de su responsable, y pida a su supervisor que lo puntúe con la rúbrica de 18.5.

### 18.7 Errores comunes y límites

- Proyectos demasiado amplios para verificarlos.
- Sellos guardados dentro del paquete.
- Editar elementos sellados en lugar de añadir otros nuevos.
- Informar solo de los éxitos.
- El Lab 18 usa texto en memoria y un directorio temporal; los paquetes reales incluyen exportaciones binarias y capturas grandes, que se resumen igual pero necesitan un almacenamiento con control de acceso.

Comprobaciones que detectan estos errores:

- Antes del primer día, escriba cada requisito como una prueba con un resultado esperado; si un requisito no puede probarse dentro de la ventana, reduzca el alcance.
- Registre el sello al menos en un lugar que los editores del paquete no puedan cambiar, como el registro de cambio (CHG-2215) o un correo al supervisor.
- Antes del traspaso, vuelva a ejecutar la verificación del manifiesto; resuelva cualquier MISMATCH restaurando el archivo sellado y añadiendo un anexo fechado (EX071), nunca resellando encima de la versión 1.
- Enumere en el traspaso los requisitos fallidos y sin probar, con sus responsables, como hace EX072.

### Ejercicios — capítulo 18

**EX069 — Alcance del proyecto.** *Objetivo:* definir un proyecto supervisado. *Entradas:* elija un proyecto de 18.1. *Pasos:* redacte el alcance, los requisitos (comprobables) y la lista de elementos que contendrá el paquete de evidencias. *Evidencia esperada:* plan de una página. *Rúbrica:* 3 = todos los elementos del alcance, al menos cuatro requisitos comprobables con pruebas positivas y negativas, elementos asociados a las fases, supervisor y autorizador nombrados; 2 = una laguna; 1 = genérico; 0 = nada.

**EX070 — Verifique un sello.** *Objetivo:* usar el sello correctamente. *Entradas:* el Lab 18. *Pasos:* modifique el programa para que, al final, recalcule también el resumen del manifiesto y lo compare con el sello registrado; después edite también `MANIFEST.sha256` para que coincida con el archivo de pruebas manipulado y muestre lo que informa la comparación del sello. *Evidencia esperada:* código y salidas de ambos casos. *Rúbrica:* 3 = primer caso: el sello coincide (manifiesto intacto) mientras un elemento no coincide; segundo caso: todos los elementos «OK» frente al manifiesto editado, pero la comparación del sello falla; explica por qué el sello debe guardarse fuera; 2 = un caso; 1 = intentado; 0 = nada.

**EX071 — Gestione la adición tardía.** *Objetivo:* gestionar los cambios en la evidencia. *Entradas:* la edición de T10. *Pasos:* redacte paso a paso el procedimiento que describió el evaluador, incluido qué se registra y dónde. *Evidencia esperada:* procedimiento. *Rúbrica:* 3 = restaurar el original sellado desde el archivo y comprobar su resumen; añadir el anexo como elemento nuevo con fecha y recolector; generar una nueva versión del manifiesto y un nuevo sello; registrar ambos sellos externamente con el motivo; no sobrescribir nunca la versión 1; 2 = falta el registro externo; 1 = «editar y resellar»; 0 = nada.

**EX072 — Autoevaluación.** *Objetivo:* aplicar la rúbrica con honestidad. *Entradas:* el proyecto de R. Kaur tal como se describe en este capítulo y en los capítulos 10–13. *Pasos:* puntúe cada criterio de la rúbrica con una frase de evidencia y enumere los puntos abiertos. *Evidencia esperada:* tabla puntuada y puntos abiertos. *Rúbrica:* 3 = puntuaciones justificadas a partir del texto (por ejemplo, verificación limitada por REQ-4 hasta que se elimine R6; criterio de evidencia rebajado por la edición posterior al sellado hasta que se corrija), los puntos abiertos incluyen R6, la elusión por el router de KW-04 en las demás estaciones, la cobertura de REQ-6 y el desenlace del incidente de KW-09, cada uno con responsable; 2 = puntuaciones sin evidencia; 1 = todo 3; 0 = nada.

### Síntesis del capítulo

Un proyecto supervisado muestra la competencia técnica como evidencia: un alcance firmado, una línea base, un cambio controlado, la verificación de cada requisito, un registro de diagnóstico, documentación ejecutable y un paquete sellado. Un sello demuestra que la evidencia no ha cambiado desde el sellado, si se registra fuera del paquete; no demuestra que la evidencia fuera cierta. Declare qué queda abierto, quién es su responsable y qué no pudo ver.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Siga estudiando — capítulo 18 de 18

[← Capítulo 17](#ch-17) · [Índice de capítulos del curso](../SUBJECTS.md) · [Siguiente curso desde el índice de capítulos →](../SUBJECTS.md)

Este es el último capítulo de este curso; el índice enlaza con el siguiente curso del itinerario completo de estudio.
<!-- open-cyber-academy:chapter-navigation:end -->

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

### Capítulo 10: EX037–EX040

**EX037 — Explique el sombreado.** Con R5 por encima de R4: no se notifica ninguna regla sombreada; pruebas: 1 PASS, 2 PASS (denegación por R5), 3 PASS, 4 FAIL (SMB permitido por R4), 5 FAIL (R6). El cambio de orden cumplió la promesa del comentario sobre RDP, pero no resolvió la regla amplia.

**EX038 — Corrija la política.** Elimine R4 y R6. Las cinco pruebas dan PASS (RDP y SMB se deniegan ahora por R7; 10.20.0.12 se deniega por R7). R5 es ahora redundante con la denegación por defecto; consérvela solo si se quiere una categoría de registro aparte para los intentos de RDP (y entonces debe situarse por encima de cualquier permiso); en caso contrario, elimínela. Antes de eliminar R4, revise 30 días de registros de fw-01 para enumerar lo que usaba R4 y dar a cada uso legítimo su propio conducto.

**EX039 — Configuración del acceso de proveedores.** `vendor-ss3` desactivada por defecto. Kestrel Grid abre una incidencia; la guardia del KVROC activa la cuenta durante una ventana fija (por ejemplo, 4 h) en la herramienta de acceso; el proveedor se conecta a jump-01 con MFA; la sesión se graba; jump-01 solo permite la dirección de gestión de la pasarela del proveedor y el puerto de ingeniería concreto de SS-3, nunca toda la red de la subestación; se dispara una alerta ante cualquier inicio de sesión fuera de una ventana activada; la cuenta se desactiva automáticamente; el siguiente día laborable se revisa el registro de la sesión frente a la incidencia.

**EX040 — Detecte las ampliaciones.** Añada: `def overlaps(a, b): return ip_network(a[2]).overlaps(ip_network(b[2])) and ip_network(a[3]).overlaps(ip_network(b[3])) and (a[4] in ("any", b[4]) or b[4] == "any") and (a[5] is None or b[5] is None or a[5] == b[5])` y, para una regla posterior con la misma acción que se solapa pero no está cubierta, notifíquela cuando su origen o su destino no sea una subred del de la anterior. La salida verificada añade `R6 broadens R1: same action, wider source 10.20.0.0/24`, lo mismo para R2, y `R7 broadens R5`; esta última es la denegación por defecto prevista y debe excluirse (por ejemplo, omitiendo las reglas cuyo origen y destino son ambos `0.0.0.0/0`). La revisión es necesaria porque, en una lectura rápida, la regla parece un duplicado, pero concede a toda la subred del centro de control acceso de escritura a KW-04.

### Capítulo 11: EX041–EX044

**EX041 — Hágalo comprobable.** «El acceso remoto es seguro» → «El acceso del proveedor a SS-3 solo es posible a través de jump-01 con MFA durante una ventana activada» (prueba: un intento fuera de la ventana se rechaza y genera una alerta). «La hora está sincronizada» → «Todos los equipos de Z2 y Z5 están a menos de 1 s de ntp-ops» (prueba: informe de desfases). «Los registros se conservan» → «Los eventos de permiso y denegación de fw-01 llegan al colector en 60 s y se conservan 12 meses» (prueba: intento de conexión señalado y consulta posterior en el colector; comprobación de la conservación del registro más antiguo).

**EX042 — Añada la prueba que falta.** Con T9 para el REQ-6, la salida muestra el REQ-6 verificado mediante T9 y «verified 4/6». REQ-3 y REQ-4 siguen fallando, así que CHG-2207 no está terminado.

**EX043 — Pruebas positivas para un cambio de cortafuegos.** El SCADA sondea las doce estaciones (el recuento del historiador para una ventana de 10 minutos es igual a 12 estaciones); conexión de eng-ws-15 a la estación de la incidencia dentro de una ventana; SSH de jump-01 a hist-02 y a scada-01; la exportación diaria de hist-02 llega al servidor de informes; las sesiones de la HMI con scada-01 no se ven afectadas. Evidencia: salida de la consulta al historiador, registros de conexión, entradas del colector.

**EX044 — Sin probar no es verificado.** «CHG-2207 no está terminado. De seis requisitos, tres están verificados con evidencia (REQ-1, REQ-2, REQ-5), dos fallaron (REQ-3: el RDP corporativo sigue permitido porque R4 continúa; REQ-4: 10.20.0.12 puede alcanzar el Modbus de las estaciones por R6) y uno está sin probar (REQ-6, registro de denegaciones). T8 fue una revisión de la configuración sin salida registrada y no se cuenta. Responsables: eliminación de R4 y R6, R. Kaur, con un nuevo cambio; prueba del REQ-6, J. Tan. Nueva verificación tras la corrección».

### Capítulo 12: EX045–EX048

**EX045 — Lea las respuestas.** tid 1: función 3, normal, 6 bytes: 342, 61, 0. tid 2: función 6, repetición normal; se escribió 300 en el registro 7. tid 3: 0x86 = excepción a la función 6, código 03 valor de datos ilegal (900 fuera de 100–400). tid 4: 0x86, código 02 dirección de datos ilegal (el registro 0 no se puede escribir). tid 5: 0x88 = excepción a la función 8, código 01 función ilegal. tid 6: 0x83 = excepción a la función 3, código 02 (el rango 8–12 excede la tabla).

**EX046 — Implemente la función 16.** Analice `addr, qty, bc = struct.unpack(">HHB", req[8:13])`; si `bc != 2 * qty or len(req) != 13 + bc`, devuelva la excepción 03; decodifique los valores; si alguna dirección de `addr..addr+qty-1` no está en WRITABLE, devuelva 02; si algún valor está fuera de su rango, devuelva 03; en caso contrario, escriba todos y devuelva `struct.pack(">HHHBBHH", tid, 0, 6, unit, 16, addr, qty)`. Registre cada resultado. Ninguna escritura parcial.

**EX047 — Detecte intentos de cartografiado.** Regla: tres o más respuestas de excepción 02 a un mismo origen en 60 s. Las seis peticiones originales producen dos respuestas de excepción 02 (tid 4 y tid 6), así que no se dispara; añadir cinco lecturas fuera de rango produce siete y se dispara. Contar juntas la 02 y la 03 ya llegaría a tres en la ejecución original (tids 3, 4, 6) y se dispararía con errores corrientes; mantener aparte la regla de prueba de límites (excepción 03) da alertas más claras.

**EX048 — Evalúe un laboratorio.** Contención 1: un servidor en `0.0.0.0:502` es alcanzable desde cualquier red a la que se una el portátil, incluida la red de una estación si el portátil se usa allí. Fidelidad: sin declaración, puntuación 1. Corrección: `socketpair()` o enlace a 127.0.0.1 con una regla del cortafuegos del equipo, o una red de máquinas virtuales aislada sin ruta hacia fuera; añadir una declaración de fidelidad; registrar las salidas con la versión de Python.

### Capítulo 13: EX049–EX052

**EX049 — Primero, las predicciones.**

| Hipótesis | Ping | TCP 502 | Respuesta Modbus | Contadores de radio/celular | Otras estaciones |
|---|---|---|---|---|---|
| Caída del enlace | falla | falla | ninguna | errores en aumento | bien |
| Sobrecarga del sondeo del SCADA (capítulo 1) | bien | bien | bien cuando se sondea, pero los sondeos llegan tarde | planos | también con retraso |
| Tráfico bloqueado o inundado por un equipo no autorizado | bien o falla | falla o lenta | tiempos de espera agotados | planos | bien |

Las observaciones que las separan son los contadores (enlace), la frescura de las demás estaciones (SCADA) y los registros del cortafuegos y de flujos (relevante para la seguridad).

**EX050 — Añada H6.** Ejemplo: `"H6 RTU firmware degraded": {"rtu_ping": True, "tcp502_handshake": True, "modbus_reply": "timeout"}` queda refutada por `modbus_reply` (se observó la excepción 2). Si en cambio predice la excepción 02 (algunos dispositivos la devuelven en modo degradado), H6 sigue siendo coherente, y la observación adicional de solo lectura es la página de diagnóstico o de estado de la RTU (tiempo en funcionamiento, modo) mediante la herramienta del fabricante en modo de solo lectura, o su registro de eventos con un reinicio.

**EX051 — El momento del escalado.** Mensaje: «07:22Z. Las lecturas de KW-09 se detuvieron a las 07:05Z. Observado: enlace, cortafuegos y SCADA en buen estado; la RTU responde con la excepción 02 a las lecturas normales; la RTU registró una sesión de configuración a las 06:41Z (reloj corregido) del usuario 'eng' sin incidencia de cambio. Inferido: esa sesión cambió el mapa de registros; se desconoce quién y por qué. Hecho: no se ha cambiado nada. Petición: decisión sobre restaurar la configuración anterior tras la conservación. Jefe de turno de Kestrel Water informado a las 07:20Z». Conservado: exportación de la configuración de la RTU (07:25Z) y registro de sesiones; registros de jump-01 y eng-ws-15 de 06:30–06:50Z; registros de fw-01 para 10.10.9.2; el registro de diagnóstico; cada uno con SHA-256 y hora de recogida.

**EX052 — Cierre la ruta de KW-04.** Conservar la configuración del router y sus registros de conexión; eliminar la redirección de tcp/502 con un cambio aprobado por Kestrel Water; pedir al operador de telecomunicaciones (a través del responsable del contrato) que elimine la alcanzabilidad desde la VPN corporativa de acceso remoto hacia la red privada de las estaciones; prueba negativa desde un cliente VPN señalado hacia la dirección de KW-04 en la red del operador; prueba positiva del sondeo del SCADA; después, exportar y revisar los otros once routers de estación en busca de redirecciones de puertos y exposición de la gestión; añadir las configuraciones de los routers a la detección de derivas. Responsable: el responsable de red del KVROC, con la aprobación de Kestrel Water.

### Capítulo 14: EX053–EX056

**EX053 — Clasifique y actúe.** (1) Conservar `sshd_config` y `debug.sh`: copias, resúmenes, tamaño, mtime, propietario y los registros de autenticación pertinentes; informar a L. Ferreira. (2) Investigar `debug.sh` (quién lo creó, si se ejecutó, si hay algo activo a la escucha) antes de eliminarlo: probable incidente. (3) Revertir `sshd_config` a la versión aprobada mediante un cambio, tras la conservación; verificar con `sshd -T`. (4) Para `ntp.conf`: verificar el desfase frente a ambos servidores y después actualizar el manifiesto con la referencia CHG-2210. (5) `fw-01.rules`: nada.

**EX054 — Lista de correcciones automáticas.** Reactivar el reenvío de registros: corrección automática (restaura la visibilidad, sin efecto sobre el proceso). Corregir la lista de servidores NTP: corrección automática (integridad de la hora, bajo riesgo). Restablecer `sshd_config`: incidencia (conservar primero; riesgo de quedarse fuera). Reiniciar el historiador: incidencia con operaciones (laguna de datos). Aplicar reglas de cortafuegos: incidencia con pruebas (puede cortar el sondeo). Restablecer el punto de consigna de un PLC: nunca automatizado por herramientas de seguridad; el control del proceso corresponde a operaciones.

**EX055 — Salvaguarda de detención.** Detener si la misma clave cambia de forma idéntica en más del 25 % de los equipos (aquí, 9 de 14 = 64 %). Lo más probable es un cambio de la flota sin registrar hecho por el equipo de plataforma o un manifiesto desactualizado; compruebe el calendario de cambios y el repositorio del estado deseado. Hasta que se explique sigue siendo un hallazgo: un atacante con la cuenta de automatización podría producir el mismo patrón.

**EX056 — Registro de conservación.** Antes de imprimir la línea del cambio no aprobado: `rec = {"file": name, "old": manifest[name], "new": current[name], "size": p.stat().st_size, "mtime": p.stat().st_mtime}`; escríbalo como JSON en `root / f"preserve-{name}.json"` e imprima su SHA-256. El resumen del registro debe guardarse fuera del equipo (expediente del caso o colector), porque, de lo contrario, un administrador del equipo podría reescribir tanto el archivo como el registro.

### Capítulo 15: EX057–EX060

**EX057 — Las rutas importan.** Mantenga un mapa `parent` en la búsqueda en anchura y recórralo hacia atrás desde cada servicio. Rutas: esx-03 → fep-01 → grid-ss3-telecontrol; esx-03 → ad-ops → scada-01 → water-telemetry; esx-03 → ad-ops → bms-server → hospital-bms. Un segundo servidor de directorio en otro equipo rompe las rutas del agua y del hospital; la ruta de la red eléctrica necesita redundancia de fep-01 en otro servidor.

**EX058 — Nuevos componentes compartidos.** Tras añadir los nodos, compartidos por los tres servicios: `esx-03` y `power-ups-a` (verificado). `cell-carrier` afecta al agua y a la red eléctrica. Cambios: alimentar esx-02 y esx-03 desde SAI y circuitos separados; dar a las estaciones más críticas y al telecontrol de SS-3 una segunda ruta de comunicación independiente (otro operador o radio con licencia).

**EX059 — Prueba en modo degradado.** Primero en una réplica o en una HMI de reserva: bloquear su tráfico hacia el directorio y probar el inicio de sesión con credenciales en caché y con la cuenta local de emergencia documentada. En producción, en una ventana acordada y con operaciones de Kestrel Water presente: bloquear durante 10 minutos en fw-01 la ruta de la HMI hacia ad-ops; confirmar que los operadores pueden iniciar sesión y actuar y que el sondeo de scada-01 continúa (recuento del historiador). Condiciones de parada: cualquier pérdida de la visión o del control del operador, cualquier alarma; eliminación inmediata de la regla como reversión. Evidencia: registro del cambio de regla, registros de inicio de sesión, recuentos del historiador.

**EX060 — Sentido de la exportación.** hist-02 envía el CSV por HTTPS a report-01 con una credencial de servicio que solo puede subir archivos; se eliminan la cuenta corporativa y la contraseña guardada que se usaban para iniciar sesión en hist-02, y se rota la contraseña; fw-01 solo permite hist-02 → report-01 tcp/443, y nada desde Z6 hacia hist-02; incluir un resumen SHA-256 del archivo en los metadatos de la subida y comprobarlo al recibirlo; alertar si no ha llegado ningún envío a las 06:30.

### Capítulo 16: EX061–EX064

**EX061 — Repare una instrucción de trabajo.** Defectos: contraseña en el documento (y, por tanto, comprometida: rótela); sin condiciones previas ni registro de cambio; sin modo de solo lectura; sin resultados esperados; «corrija lo que esté mal» autoriza cambios no planificados; a operaciones solo se le informa después; sin condiciones de parada ni reversión. Reescritura con el patrón de WI-KW-07: registro de cambio, llamada previa a la sala de control, referencia a la bóveda para la credencial, exportación de solo lectura con resultados esperados, hallazgos registrados para un cambio aparte, condiciones de parada, llamada al final.

**EX062 — Política de dispositivos transitorios.** Política: el trabajo de ingeniería en los sistemas de control solo desde portátiles dedicados construidos a partir de una imagen controlada, que nunca se usan para el correo ni para internet; actualización y análisis antimalware antes de cada visita en un puesto controlado, con registro; soportes extraíbles de un conjunto numerado, analizados y registrados; cada conexión en una instalación, registrada. Transición: analizar los archivos de proyecto del portátil actual en un sistema aislado, copiar los archivos verificados al nuevo portátil de ingeniería, registrar los resúmenes y después devolver el portátil antiguo solo al uso corporativo.

**EX063 — Límites de seguridad física.** No inicie sesión, no pruebe ni cambie nada. Registre la identidad del dispositivo, la ubicación, la hora y cómo se advirtió la situación (por ejemplo, la página de inicio de sesión mostraba un aviso de credenciales por defecto descrito en la documentación del fabricante; no hubo intento de inicio de sesión). Comuníquelo el mismo día al ingeniero de protecciones de Kestrel Grid y a L. Ferreira; los ingenieros de protecciones deciden y realizan cualquier cambio conforme a sus procedimientos. Guarde el hallazgo con acceso restringido.

**EX064 — Registro de la configuración tal como se construyó.** Ejemplo: fw-01, versión de firmware x.y; resumen del conjunto de reglas (marcador) guardado en CHG-2215 y en el colector; reglas R1, R2, R3, R7 tal como se construyeron; desviación: R5 conservada para el registro (aprobada por L. Ferreira). hist-02: versión de OpenSSH; resumen de la configuración efectiva obtenido con `sshd -T`; desviación abierta hasta completar EX010: el intérprete de `histsvc`; fechado y firmado por quien lo implantó y quien lo verificó.

### Capítulo 17: EX065–EX068

**EX065 — Lea los episodios.** «*Observado:* 07:03–07:12Z, el equipo desconocido 10.20.0.31 envió consultas de identificación de dispositivo a KW-04, KW-05 y KW-06, una trama mal formada a KW-07, y escribió 65.535 en el registro 7 de KW-04 (punto de consigna de la bomba 2) a las 07:04:40, 07:05:30 y 07:12:00. *Inferido:* reconocimiento seguido de intentos de cambiar el punto de consigna. *Hecho:* nada. *Abierto:* identidad y responsable de 10.20.0.31; si KW-04 aceptó las escrituras; cómo llegó el equipo a Z2. Petición: que Kestrel Water compruebe ahora la bomba 2 y el punto de consigna de KW-04; conservar los datos del sensor».

**EX066 — Corrija el descarte ciego.** En la rama de las tramas mal formadas, añada NEW-TALKER cuando el origen sea desconocido, antes de `continue`. Salida verificada: NEW-TALKER 07:03:00–07:05:30Z ×6, alertas 13, episodios 5, y se sigue dando cuenta de los registros (10 = 9 analizados + 1 descartado).

**EX067 — Compromiso de la ventana.** 1 minuto: 6 episodios; NEW-TALKER se divide en 07:03:00–07:03:02 (×3), 07:04:40–07:05:30 (×2) y 07:12:00 (×1); UNAUTH-WRITE en 07:04:40–07:05:30 (×2) y 07:12:00; DEVICE-ID uno. 10 minutos: 3 episodios; NEW-TALKER 07:03:00–07:12:00 ×6, DEVICE-ID ×3, UNAUTH-WRITE 07:04:40–07:12:00 ×3. Todo verificado ejecutándolo. Cinco minutos es un valor por defecto razonable para una actividad a ritmo humano; la configuración de 10 minutos mantiene visible la escritura de las 07:12 como parte de la misma actividad, lo que aquí es posiblemente mejor: anote la elección y revísela con datos reales.

**EX068 — Regla de rango de valores.** Añada `POLICY = {7: (100, 400)}`; para la función 6, decodifique `addr, val` de los bytes 8–12; para la 16, decodifique cada valor; genere la alerta `VALUE-RANGE` cuando una dirección de POLICY reciba un valor fuera de su rango. Se dispara con las tres escrituras de 0xFFFF y no con la escritura de 300 de eng-ws-15. Detecta pero no impide: el dispositivo puede seguir aceptando la escritura, así que el cortafuegos y los controles de acceso siguen siendo la capa preventiva.

### Capítulo 18: EX069–EX072

**EX069 — Alcance del proyecto.** Ejemplo (elusión por los routers de estación): propósito: eliminar las rutas no autorizadas hacia el Modbus de las estaciones a través de routers celulares; sistemas: doce routers de estación (lectura), cambios solo en los routers con hallazgos; ventana: acordada por estación con Kestrel Water; autorizador A. Mensah; supervisor L. Ferreira; condiciones de parada: cualquier pérdida de comunicación o alarma. Requisitos: ninguna redirección de puerto a tcp/502 en ningún router (negativa: comprobación de la configuración y prueba de conexión con un cliente VPN); el SCADA sondea todas las estaciones (positiva: recuento del histórico); configuraciones de los routers bajo detección de derivas (prueba: se detecta un cambio inocuo inyectado); gestión de los routers solo desde jump-01 (prueba negativa). Elementos: alcance, exportaciones de la línea base y resúmenes, registros de cambio, resultados de las pruebas, registro de diagnóstico, registro de la configuración tal como se construyó, manifiesto y sello.

**EX070 — Verifique un sello.** Tras la verificación, calcule `hashlib.sha256((d / "MANIFEST.sha256").read_bytes()).hexdigest()` y compárelo con `seal`: el caso 1 imprime «seal OK» mientras `04-tests.csv` no coincide. Caso 2: reescriba la línea del manifiesto de `04-tests.csv` con el nuevo resumen; ahora todos los elementos se verifican «OK», pero el resumen del manifiesto difiere del sello registrado, así que la comprobación del sello falla. Solo un sello guardado externamente revela que se editó el propio manifiesto.

**EX071 — Gestione la adición tardía.** (1) Recupere la versión 1 del paquete desde el archivo; compruebe cada elemento y el manifiesto frente al sello registrado externamente. (2) Restaure `04-tests.csv` al contenido sellado. (3) Guarde los resultados de T10 como `06-tests-addendum.csv` con el recolector y la hora UTC. (4) Cree la versión 2 del manifiesto con los seis elementos; calcule el sello 2. (5) Registre el sello 2 en el registro de cambio y en el formulario de evaluación con el motivo, conservando el sello 1. (6) No sobrescriba nunca la versión 1.

**EX072 — Autoevaluación.** Alcance 3 (firmado, responsable y condiciones de parada). Corrección técnica 2 (R4 eliminada; R6 sigue presente). Verificación 2 (REQ-4 falla hasta que se elimine R6; REQ-6 solo se probó después de EX042). Diagnóstico 3 (hipótesis, predicciones y conservación en KW-09). Documentación 2 (registro de la configuración tal como se construyó pendiente para los hallazgos de los routers). Evidencia 2 hasta que se corrija la edición posterior al sellado; después, 3. Honestidad 3 si se enumeran los puntos abiertos. Puntos abiertos: eliminar R6 (R. Kaur); comprobación de la elusión por los routers en todas las estaciones (responsable de red); prueba de regresión mensual de REQ-6 (J. Tan); desenlace del incidente de KW-09 (L. Ferreira).

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
