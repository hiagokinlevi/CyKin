# Seguridad de TO, IoT y sistemas ciberfísicos: libro de práctica para tecnólogos

- Idioma: español neutro (`es`); curso de tecnólogo, tres años; aproximadamente 2.400 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–30 de 30 tienen texto didáctico escrito a mano; los ejercicios EX001–EX090 tienen sus resultados resueltos correspondientes; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas se incluyen a partir de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4.
- Público: tecnólogos que instalarán, operarán, supervisarán y mejorarán la seguridad de sistemas de TO e IoT en emplazamientos reales.
- Relación con los libros vecinos: el [libro del curso técnico](../../../../technical-18-months/ot-iot-security/en/book/MANUSCRIPT.md) es más breve y más procedimental; el [libro de grado](../../../../bachelors-4-years/ot-iot-security/es/book/MANUSCRIPT.md) añade teoría e investigación. **Este libro se centra en la implantación.**
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado. No concede autorización para acceder a emplazamientos reales. Todos los emplazamientos, personas y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los capítulos 1–9 construyen los fundamentos de informática, redes, scripting y evidencia; los capítulos 10–23 son el núcleo de TO/IoT, con el laboratorio guiado en el capítulo 15; los capítulos 24–30 tratan de investigación, un taller en equipo, traspaso, despliegue, práctica de campo y el proyecto final. Cada capítulo tiene resultados de aprendizaje, enseñanza, un ejemplo resuelto, un caso sintético etiquetado, errores y límites, tres ejercicios puntuados de 0 a 3, una síntesis y un bloque **Siga estudiando**. Los laboratorios solo leen datos locales (`python3 file.py`).

### Caso de estudio sintético

| Elemento | Función | Límite |
|---|---|---|
| **Northgate Cold Storage (NCS)**: controladores de refrigeración por amoníaco PLC-R1/PLC-R2, HMI-C, historiador HIST, registradores de temperatura inalámbricos que envían a la nube de un proveedor mediante GW-LOG, cámaras del muelle | Emplazamiento estudiado a lo largo del libro | Inventado |
| **Priya Nair** | Tecnóloga en formación en NCS | Inventada |

### Fuentes principales

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [serie ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Lista completa en [Referencias](#references).

## Contenido

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](../../en/book/MANUSCRIPT.md#ch-16) · [17](../../en/book/MANUSCRIPT.md#ch-17) · [18](../../en/book/MANUSCRIPT.md#ch-18) · [19](../../en/book/MANUSCRIPT.md#ch-19) · [20](../../en/book/MANUSCRIPT.md#ch-20) · [21](../../en/book/MANUSCRIPT.md#ch-21) · [22](../../en/book/MANUSCRIPT.md#ch-22) · [23](../../en/book/MANUSCRIPT.md#ch-23) · [24](../../en/book/MANUSCRIPT.md#ch-24) · [25](../../en/book/MANUSCRIPT.md#ch-25) · [26](../../en/book/MANUSCRIPT.md#ch-26) · [27](../../en/book/MANUSCRIPT.md#ch-27) · [28](../../en/book/MANUSCRIPT.md#ch-28) · [29](../../en/book/MANUSCRIPT.md#ch-29) · [30](../../en/book/MANUSCRIPT.md#ch-30) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Sistemas informáticos

### Resultados de aprendizaje

Usted será capaz de (1) nombrar los dispositivos informáticos de un almacén frigorífico y lo que hace cada uno; (2) distinguir los controladores embebidos de los ordenadores de propósito general; (3) explicar por qué difieren las expectativas de disponibilidad; y (4) empezar el cuaderno de activos que se usa durante todo el curso.

### 1.1 Muchos ordenadores, pocos evidentes

El almacén sintético Northgate Cold Storage (NCS) conserva alimentos congelados a −22 °C y productos refrigerados a 2–4 °C. Sus ordenadores evidentes son los PC de la oficina. Menos evidentes son dos controladores de refrigeración (PLC-R1 y PLC-R2) que hacen funcionar los compresores de amoníaco, una pantalla de operador (HMI-C), un historiador (HIST), cuarenta registradores de temperatura inalámbricos que informan a través de una pasarela (GW-LOG) a un servicio en la nube, y cámaras IP en el muelle de carga. La primera tarea de un tecnólogo es verlos todos.

La primera fila del cuaderno de Priya, para GW-LOG, ya muestra por qué: si se detiene, la refrigeración continúa, pero el registro de temperaturas tiene un hueco.

### 1.2 Embebido frente a propósito general

Un PLC ejecuta un único programa de control en un bucle fijo y puede permanecer encendido durante una década. Una HMI con Windows ejecuta muchos procesos, recibe actualizaciones y puede infectarse con malware corriente. Los registradores son microcontroladores con radio y batería; no pueden ejecutar ningún antivirus. Cada clase necesita un enfoque de protección distinto, y por eso NIST SP 800-82r3 trata por separado los tipos de dispositivos de TO. El cuaderno de Priya registra la clase en su columna de tipo, y las tres clases dan lugar a tres planes. PLC-R1 y PLC-R2 se protegen controlando quién puede llegar a ellos, porque no pueden ejecutar software de seguridad. HMI-C se bastiona como un equipo Windows dentro de la compilación certificada por el proveedor. Los cuarenta registradores dependen por completo del firmware del proveedor y de la pasarela que tienen delante.

### 1.3 Primero, la disponibilidad

Si un PC de la oficina se reinicia, alguien pierde diez minutos. Si PLC-R1 se detiene, la presión de aspiración de los compresores deriva y la cámara de congelación se calienta aproximadamente un grado cada 15–20 minutos; al cabo de unas horas, pueden desecharse existencias por valor de cientos de miles. Esa consecuencia condiciona todas las decisiones posteriores: cuándo aplicar parches, cómo probar, quién debe estar presente. En NCS, por eso una corrección de firmware de PLC-R1 espera a una ventana de mantenimiento con la empresa de refrigeración presente, y por eso el cambio de cortafuegos que Priya hace más adelante, en el capítulo 27, tiene una reversión ensayada de dos minutos: un flujo que falte y deje al historiador sin registrar durante una hora importa más que el propio cambio.

### Ejemplo resuelto (NCS sintética)

Priya Nair, tecnóloga en formación, construye su cuaderno de activos: dispositivo, tipo (embebido o de propósito general), función, ubicación, quién lo modifica y qué ocurre si se detiene. Su fila para GW-LOG dice: «pasarela embebida; reenvía las lecturas de los registradores a la nube; sala de comunicaciones; el proveedor la actualiza de forma remota; si se detiene, los registros de temperatura tienen un hueco y se pierde evidencia de seguridad alimentaria, pero la refrigeración continúa».

> **Caso sintético — Northgate Cold Storage.** NCS, Priya Nair y todos los nombres de dispositivos se han inventado con fines didácticos.

### Errores y límites

No dé por hecho un «aislamiento físico» sin comprobar si hay módems celulares o portátiles de proveedores. Las velocidades de calentamiento dependen de las aperturas de puertas y de la carga; use los datos de la propia planta antes de citar una cifra.

### Ejercicios — capítulo 1

- **EX001 — ¿Embebido o de propósito general?** Clasifique HMI-C, PLC-R2 y un registrador de temperatura, con un motivo para cada uno. *Rúbrica:* 3 = propósito general, embebido, embebido, con motivos; 2 = clases correctas, motivos débiles; 1 = uno correcto; 0 = nada.
- **EX002 — Consecuencia de una pasarela detenida.** Indique qué pierde NCS si GW-LOG falla durante seis horas y qué no pierde. *Rúbrica:* 3 = pierde los registros/alertas de temperatura, la refrigeración continúa; 2 = un solo lado; 1 = dice que los congeladores se detienen; 0 = nada.
- **EX003 — Fila del cuaderno para PLC-R1.** Escriba la fila de seis columnas del cuaderno de activos para PLC-R1. *Rúbrica:* 3 = las seis columnas plausibles; 2 = cuatro o cinco; 1 = solo el nombre; 0 = nada.

### Síntesis del capítulo

Ver todos los ordenadores de una instalación, y saber lo que cuesta el fallo de cada uno, es la base del trabajo de seguridad de TO.

### Siga estudiando — capítulo 01 de 30

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Redes y servicios de internet

### Resultados de aprendizaje

Usted será capaz de (1) leer un plan de direccionamiento IP e identificar subredes; (2) explicar lo que hacen una VLAN y una regla de cortafuegos; (3) seguir el recorrido de un registrador conectado a la nube hasta internet; y (4) reconocer los servicios que una instalación expone hacia fuera.

### 2.1 Direcciones y subredes

NCS usa 10.10.0.0/24 para las oficinas, 10.20.0.0/24 para el control de refrigeración y 10.30.0.0/24 para los registradores y las cámaras. Una máscara /24 significa que los tres primeros números nombran la red y el último nombra el equipo. Dos dispositivos de la misma subred hablan directamente a través del conmutador; los dispositivos de subredes distintas deben pasar por un router o un cortafuegos, que es donde puede aplicarse una política. El seguimiento que hace Priya de una lectura de un registrador muestra las fronteras en uso: el registrador informa a GW-LOG en 10.30.0.5, y la regla 21 del cortafuegos permite que 10.30.0.5 llegue a la nube del proveedor por TCP 443. El mismo cortafuegos contiene la regla 9, «any to 10.20.0.0/24, TCP 502, allow», que permite a cualquier dirección de la oficina llegar al puerto Modbus de los controladores de refrigeración.

### 2.2 VLAN y cortafuegos

Una VLAN separa el tráfico de forma lógica en conmutadores compartidos. Las VLAN por sí solas no filtran: el filtrado ocurre donde el tráfico se enruta entre ellas. Una regla de cortafuegos nombra el origen, el destino, el protocolo y el puerto, y si se permite o se deniega. Un valor por defecto sensato es «denegar todo lo que no esté permitido explícitamente». La regla 9 es el ejemplo de NCS de una regla que anula ese valor por defecto. Se añadió durante la puesta en marcha para que la empresa contratista pudiera trabajar desde cualquier puerto, y nadie la quitó. Con la regla 9 en vigor, las VLAN siguen separando el tráfico de difusión, pero el cortafuegos entre 10.10.0.0/24 y 10.20.0.0/24 permite exactamente el flujo que más importa: Modbus desde la oficina hacia PLC-R1 y PLC-R2. El laboratorio posterior de Priya encuentra a OFFICE-7 usándolo.

### 2.3 Conexiones salientes a la nube

GW-LOG abre una conexión HTTPS saliente (TCP 443) hacia la nube del proveedor de los registradores. Las conexiones salientes son más fáciles de proteger que las entrantes, porque nadie en internet puede iniciar una sesión hacia la pasarela, siempre que el cortafuegos no le reenvíe también un puerto entrante. Las herramientas de soporte remoto a menudo añaden justo ese reenvío, y así es como muchos dispositivos quedan expuestos a internet. En NCS, la regla 21 es solo saliente; Priya comprobó que no existe ningún reenvío de puertos hacia 10.30.0.5 y registró esa comprobación, para que la afirmación pueda volver a verificarse tras la próxima visita del proveedor.

### 2.4 Resolución de nombres

La pasarela encuentra la nube mediante DNS. Si la pasarela usa un servidor DNS interno, un error de configuración en él puede interrumpir el registro en toda la planta; si usa directamente un resolvedor público, el cortafuegos también debe permitirlo. Anote cuál de los dos. Para GW-LOG, Priya comprobó que usaba el servidor DNS interno del emplazamiento, así que el conjunto de reglas no necesitaba ninguna excepción para un resolvedor público. Eso tiene consecuencias para los fallos de certificados del capítulo 22: cuando LOG-03 dejó de subir datos el 5 de octubre, el DNS era una de las dependencias que había que descartar antes de culpar al certificado caducado. Una nota de una línea en el inventario, «resolvedor de GW-LOG: DNS interno, 10.10.0.2», habría respondido a esa pregunta en segundos.

### Ejemplo resuelto (NCS sintética)

Priya sigue el recorrido de una lectura de un registrador: registrador → radio → GW-LOG (10.30.0.5) → regla 21 del cortafuegos «10.30.0.5 to vendor cloud, TCP 443, allow» → internet. También encuentra la regla 9, «any to 10.20.0.0/24, TCP 502, allow», que quedó de la puesta en marcha. La regla 9 permite que los PC de la oficina lleguen al puerto Modbus de los controladores de refrigeración; la marca para revisión.

> **Caso sintético — Northgate Cold Storage.** Las direcciones y los números de regla son inventados.

### Errores y límites

Un diagrama puede no coincidir con el cortafuegos; la exportación de la configuración es la evidencia. Nunca pruebe reglas enviando tráfico a controladores en producción sin un permiso de trabajo.

### Ejercicios — capítulo 2

- **EX004 — ¿Misma subred o no?** ¿Están 10.20.0.11 y 10.20.0.40 en la misma /24? ¿Y 10.20.0.11 y 10.30.0.11? *Rúbrica:* 3 = sí, no, con el motivo; 2 = solo las respuestas; 1 = una correcta; 0 = nada.
- **EX005 — Reescribir la regla 9.** Reescriba la regla 9 para que solo HMI-C (10.20.0.20) pueda llegar a los controladores por TCP 502. *Rúbrica:* 3 = origen 10.20.0.20, destinos las direcciones de los PLC, TCP 502, permitir, más denegación por defecto; 2 = laguna menor; 1 = sigue siendo «any»; 0 = nada.
- **EX006 — Entrante frente a saliente.** Explique por qué el HTTPS saliente de GW-LOG tiene menos riesgo que un reenvío de puertos hacia ella. *Rúbrica:* 3 = ninguna sesión entrante no solicitada desde internet; 2 = parcial; 1 = vago; 0 = nada.

### Síntesis del capítulo

Las direcciones, las VLAN, las reglas y el DNS determinan qué conversaciones son posibles; leerlos es la manera en que un tecnólogo encuentra las no previstas.

### Siga estudiando — capítulo 02 de 30

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programación

### Resultados de aprendizaje

Usted será capaz de (1) escribir programas breves en Python usando solo la biblioteca estándar; (2) usar listas, diccionarios y bucles para procesar registros; (3) tratar los datos ausentes de forma explícita; y (4) mantener los scripts legibles para colegas que no son programadores.

### 3.1 Por qué los tecnólogos escriben scripts

Gran parte del trabajo de seguridad de TO consiste en comparar listas: los activos de la documentación frente a los activos vistos en la red, los flujos aprobados frente a los observados, las fechas de los certificados frente a la fecha de hoy. Hacerlo a ojo con cientos de filas es lento y propenso a errores. Un script de veinte líneas lo hace siempre de la misma manera, y su salida puede adjuntarse a un ticket. El primer script de este tipo de Priya comparaba la documentación de la empresa contratista con una observación pasiva y producía la salida de cinco líneas del capítulo 11: dos coincidencias, una cámara solo en la red, HMI-C solo en los documentos y el conflicto de versiones de PLC-R2.

### 3.2 Diccionarios para búsquedas

Un diccionario de Python asocia una clave (el nombre del dispositivo) a un valor (la versión de firmware). Comprobar «¿está documentado este dispositivo?» se convierte en `name in docs`, que es rápido y legible. Los conjuntos dan la unión y la diferencia directamente: `set(a) - set(b)` enumera lo que está en `a` pero no en `b`. El script de inventario de Priya mantiene un diccionario procedente de los documentos de la empresa contratista y otro procedente de la observación pasiva, cada uno de los cuales asocia el nombre de un dispositivo a su cadena de firmware. La unión de los dos conjuntos de claves es la lista completa de dispositivos sobre los que informar; las diferencias son los dos grupos interesantes: CAM-DOCK, solo en la red, y HMI-C, solo en los documentos.

### 3.3 Los datos ausentes son un resultado

Cuando falta un valor, dígalo en la salida. `dict.get(key)` devuelve `None` en lugar de provocar un fallo, y el script puede imprimir «-» y un estado como «only-in-docs». Omitir en silencio las filas incompletas es la manera en que las brechas desaparecen de los informes. El primer borrador de Priya hacía exactamente eso: solo recorría las coincidencias, así que CAM-DOCK, que faltaba en los documentos, nunca aparecía. Un colega preguntó dónde estaba la cámara. Su corrección fue de una línea, recorrer `sorted(set(docs) | set(seen))`, de modo que cada dispositivo se imprime con un estado y el que falta lo indica. La salida del capítulo 11 muestra ahora `docs=-` para CAM-DOCK en lugar de omitirla.

### 3.4 Salida legible

Alinee las columnas con anchos de f-string (`f"{name:9}"`) y ponga la decisión al final de cada línea. Así, un revisor puede recorrer la última columna en busca de cualquier cosa que no sea «match». En la salida del capítulo 11, la última columna dice `only-on-network`, `match`, `only-in-docs`, `match` y `VERSION-CONFLICT`, así que un responsable de instalaciones puede encontrar las tres líneas que requieren acción sin leer las cadenas de firmware. Los nombres de dispositivo se rellenan hasta nueve caracteres, lo que mantiene alineadas las columnas de documentación y de red incluso para CAM-DOCK. Un revisor que vea un estado que no es ninguno de los cinco valores documentados sabe que el script se ha encontrado con una entrada que no entiende.

### Ejemplo resuelto (NCS sintética)

Priya escribe un bucle sobre dos diccionarios, uno procedente de la documentación de la empresa de refrigeración y otro de una observación pasiva de la red. Su primer borrador solo imprimía las coincidencias; un colega preguntó dónde estaba CAM-DOCK. Lo reescribió para recorrer la unión de las claves, de modo que cada dispositivo aparezca con un estado. La versión completa es el laboratorio del capítulo 11.

> **Caso sintético — Northgate Cold Storage.** Los datos son inventados.

### Errores y límites

Los scripts que leen dispositivos en funcionamiento necesitan un permiso de trabajo y límites de frecuencia cuidadosos; los scripts de este curso solo leen archivos. Nombre las variables por lo que contienen, no `x` e `y`.

### Ejercicios — capítulo 3

- **EX007 — Diferencia de conjuntos.** Dados `docs = {"A", "B", "C"}` y `seen = {"B", "C", "D"}`, ¿qué devuelven `docs - seen` y `seen - docs`? *Rúbrica:* 3 = {"A"} y {"D"} con su significado; 2 = solo los valores; 1 = uno; 0 = nada.
- **EX008 — Tratar una clave ausente.** ¿Qué devuelve `{"PLC-R1": "2.4"}.get("PLC-R9")` y qué debería imprimir el script? *Rúbrica:* 3 = None; imprimir «-» más un estado; 2 = solo el valor; 1 = dice KeyError; 0 = nada.
- **EX009 — Corregir el error de solo coincidencias.** Escriba el cambio de una línea que hace que el bucle de Priya muestre todos los dispositivos. *Rúbrica:* 3 = recorrer `sorted(set(docs) | set(seen))`; 2 = idea correcta; 1 = vago; 0 = nada.

### Síntesis del capítulo

Los scripts pequeños y legibles que informan de cada fila, incluidas las ausentes, convierten la comparación de listas en evidencia repetible.

### Siga estudiando — capítulo 03 de 30

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Modelos de datos

### Resultados de aprendizaje

Usted será capaz de (1) diseñar una tabla de activos sencilla con claves y atributos; (2) elegir identificadores que sobrevivan a la sustitución de dispositivos; (3) representar relaciones como «la pasarela da servicio a los registradores»; y (4) mantener los atributos sensibles fuera de las tablas generales.

### 4.1 Tablas, claves y atributos

Una tabla de activos contiene una fila por activo. La clave debe ser única y estable. Las direcciones IP son malas claves porque cambian cuando se cambia la dirección de un dispositivo; los números de serie cambian cuando se sustituye un dispositivo. NCS usa una etiqueta de activo pintada en el equipo (por ejemplo, «MP-1/PLC-R1»), que permanece con la función. El esquema de Priya usa esa etiqueta como clave de todas las tablas, y así las tablas de activos, registradores y flujos se combinan limpiamente incluso después de descubrirse que el firmware documentado de PLC-R2 era erróneo.

### 4.2 Relaciones

Cuarenta registradores informan a través de GW-LOG. Guardar la «pasarela» como atributo de cada fila de registrador crea una relación de uno a muchos que permite a una consulta responder en una línea a «¿qué registradores se quedan a oscuras si falla GW-LOG?». Del mismo modo, una tabla de flujos con claves de origen y destino vincula los activos en el panorama de comunicaciones que se usa en el capítulo 12. La tabla de registradores de Priya contiene tag, room y gateway_tag. Su consulta `select tag, room from loggers where gateway_tag = 'GW-LOG'` enumera los cuarenta registradores con sus salas, y esa lista se convirtió en la tabla de impacto del plan de continuidad de NCS.

### 4.3 Qué no guardar

Las contraseñas, las claves privadas y las copias de seguridad completas de configuración no pertenecen a una tabla de activos compartida. Guarde una referencia («credencial custodiada en la entrada OT-17 del almacén de secretos») y conserve el secreto en un sistema diseñado para ello. Una hoja de cálculo de contraseñas en una unidad compartida es un hallazgo habitual en las evaluaciones de TO. En el esquema de Priya, la tabla de activos tiene una columna de titular y una columna de fuente, pero ninguna columna de credenciales. La contraseña del administrador local de HMI-C, que más tarde encuentra en una nota adhesiva, debe estar en el almacén de secretos con una referencia como OT-17 en la tabla, no en una celda que pueda leer cualquiera que tenga la hoja de cálculo.

### 4.4 Campos de calidad de los datos

Añada a cada fila la «fuente» (documentación, observación de la red, recorrido por la planta) y la fecha de «última verificación». Un inventario sin fechas no es fiable al cabo de un año. PLC-R2 muestra por qué. Su firmware documentado, 2.4, procedía de los registros de puesta en marcha de la empresa contratista; la captura pasiva indicaba 2.1; y el recorrido por la planta de Priya leyó 2.1 en el panel frontal. Con una columna de fuente, la fila dice ahora firmware 2.1, fuente recorrido por la planta, última verificación en la fecha de la visita, y el lector puede ver que el valor antiguo procedía de documentos que nunca se actualizaron tras la puesta en marcha. Sin la fecha, nadie sabría si la lectura del recorrido era de la semana pasada o de hace dos años.

### Ejemplo resuelto (NCS sintética)

Esquema de Priya: assets(tag, type, function, zone, firmware, owner, source, last_verified); loggers(tag, room, gateway_tag); flows(src_tag, dst_tag, protocol, port, approved). Su consulta «select tag, room from loggers where gateway_tag = 'GW-LOG'» enumera los 40 registradores y sus salas, lo que se convirtió en la lista de impacto del plan de continuidad de la instalación.

> **Caso sintético — Northgate Cold Storage.** El esquema y los recuentos son inventados.

### Errores y límites

Un modelo solo vale lo que valga su mantenimiento; asígnele un titular. Normalizar en exceso los datos de una instalación pequeña puede hacerlos más difíciles de usar que una única tabla bien mantenida.

### Ejercicios — capítulo 4

- **EX010 — Elegir una clave.** ¿Por qué la etiqueta de activo pintada es mejor clave que la dirección IP para PLC-R1? *Rúbrica:* 3 = estable ante cambios de dirección y sustituciones; ligada a la función; 2 = parcial; 1 = «más fácil»; 0 = nada.
- **EX011 — Consulta para una lista de impacto.** Escriba una consulta SQL que enumere los registradores de la sala «Freezer-2» a los que da servicio GW-LOG. *Rúbrica:* 3 = cláusula `where` correcta sobre ambas columnas; 2 = una condición; 1 = solo la sintaxis; 0 = nada.
- **EX012 — Tratar un campo de credenciales.** Un colega añade una columna «password». ¿Con qué la sustituye? *Rúbrica:* 3 = referencia al almacén de secretos, secreto en otro sitio, acceso controlado; 2 = solo quitarla; 1 = cifrar la hoja; 0 = mantenerla.

### Síntesis del capítulo

Un modelo de datos pequeño y estable, con claves, relaciones y fechas, es lo que convierte un inventario en respuestas.

### Siga estudiando — capítulo 04 de 30

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Alfabetización en seguridad

### Resultados de aprendizaje

Usted será capaz de (1) explicar la seguridad funcional, la disponibilidad, la integridad y la confidencialidad en un almacén frigorífico; (2) describir las fuentes de amenaza habituales en TO; (3) leer un aviso público y extraer lo que importa; y (4) usar correctamente los identificadores de ATT&CK for ICS.

### 5.1 Qué importa en NCS

El peor resultado en NCS es una fuga de amoníaco, un evento de seguridad funcional que gestionan una detección de gas y una ventilación de emergencia independientes. Después viene la pérdida de refrigeración y el desecho de existencias. Luego, la integridad de los registros de temperatura, de la que dependen los clientes y los inspectores de seguridad alimentaria. La confidencialidad importa para los contratos con clientes y las grabaciones de las cámaras. El orden indica dónde invertir esfuerzo primero. La clasificación de Priya sigue este orden: la seguridad frente al amoníaco sigue en manos del sistema de detección de gas y del ingeniero de refrigeración; su trabajo de seguridad empieza por las rutas que podrían detener la refrigeración o falsear los registros de temperatura.

### 5.2 Fuentes de amenaza

La mayoría de los incidentes de TO no son ataques de élite. Incluyen ransomware corriente que se propaga desde las redes de oficina a las HMI con Windows, el uso indebido del acceso remoto de proveedores, errores durante el mantenimiento y dispositivos expuestos a internet con contraseñas por defecto. El aviso AA21-042A de CISA, sobre una instalación de tratamiento de agua, describe un acceso mediante software de escritorio compartido combinado con contraseñas débiles, un patrón que encaja con muchos emplazamientos pequeños.

Priya encontró los cuatro patrones en NCS: una herramienta de escritorio compartido en HMI-C, una contraseña compartida de la HMI en una nota adhesiva, un router celular olvidado y una cámara expuesta a internet.

### 5.3 Leer un aviso

De cualquier aviso, extraiga: el producto y las versiones afectados, la debilidad, si se ha observado explotación y las mitigaciones recomendadas. Después pregunte si NCS tiene ese producto (su tabla de activos lo responde) y si la mitigación es viable. Priya lo aplicó a AA21-042A y encontró tres paralelismos en NCS: la herramienta de escritorio compartido de la empresa contratista en HMI-C, un sistema operativo de la HMI cercano al fin de su soporte y una contraseña compartida de la HMI escrita en una nota adhesiva. Su tabla de activos respondió a la primera pregunta; la mitigación, sesiones supervisadas en lugar de una herramienta siempre activa, era viable porque la empresa contratista solo acude unas pocas veces al mes.

### 5.4 ATT&CK for ICS

MITRE ATT&CK for ICS da nombres e identificadores a comportamientos adversarios observados. T0886 *Remote Services* abarca el uso de servicios de acceso remoto para llegar a sistemas de control; T0883 *Internet Accessible Device* abarca los dispositivos alcanzables desde internet. Use los identificadores para etiquetar los hallazgos de forma coherente, no para afirmar exhaustividad. Priya etiqueta como T0886 la herramienta de escritorio compartido siempre activa de la empresa contratista en HMI-C, y como T0883 la cámara del muelle alcanzable desde internet. Ninguna etiqueta dice que el emplazamiento haya sido atacado; cada una dice qué tipo de comportamiento observado permitiría el hallazgo. Cuando más adelante un aviso de CISA cita T0886 para una familia de productos, ella puede buscar ese identificador en sus hallazgos y saber de inmediato qué elementos de NCS son pertinentes.

### Ejemplo resuelto (NCS sintética)

Priya lee AA21-042A y anota tres paralelismos en NCS: la empresa de refrigeración usa una herramienta de escritorio compartido en HMI-C; HMI-C ejecuta un sistema operativo cercano al fin de su soporte; y la contraseña compartida de la HMI está en una nota adhesiva. Etiqueta el primer hallazgo como T0886 y propone retirar la herramienta siempre activa en favor de sesiones supervisadas.

> **Caso sintético — Northgate Cold Storage.** Los paralelismos son inventados; el aviso es real.

### Errores y límites

Los avisos describen una situación concreta; no copie sus mitigaciones sin comprobar que encajan. Los sistemas de seguridad funcional de detección de gas quedan fuera de la autoridad de un tecnólogo de seguridad para modificarlos.

### Ejercicios — capítulo 5

- **EX013 — Clasificar las preocupaciones de NCS.** Ordene por prioridad: filtración de grabaciones de las cámaras, fuga de amoníaco, registros de temperatura falseados, pérdida de refrigeración. *Rúbrica:* 3 = fuga, refrigeración, registros, grabaciones, con motivos; 2 = solo el orden; 1 = en parte correcto; 0 = nada.
- **EX014 — Cuatro datos de un aviso.** Enumere los cuatro elementos que hay que extraer de un aviso ICS. *Rúbrica:* 3 = producto/versiones, debilidad, estado de explotación, mitigaciones; 2 = tres; 1 = dos; 0 = nada.
- **EX015 — Etiquetar un hallazgo.** ¿Qué identificador de ATT&CK for ICS encaja con «la empresa contratista llega a HMI-C mediante software de escritorio compartido»? *Rúbrica:* 3 = T0886 Remote Services; 2 = nombre correcto, sin identificador; 1 = T0883; 0 = nada.

### Síntesis del capítulo

La alfabetización en seguridad consiste en clasificar las consecuencias con honestidad, reconocer las fuentes de amenaza cotidianas y leer con cuidado los avisos y las etiquetas de ATT&CK.

### Siga estudiando — capítulo 05 de 30

[← Capítulo 04 (borrador)](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 (borrador) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operativos y virtualización

### Resultados de aprendizaje

Usted será capaz de (1) identificar los riesgos a nivel de sistema operativo en las HMI y los historiadores; (2) explicar qué cambia la virtualización para los servidores de TO; (3) planificar instantáneas y copias de seguridad que de verdad se restauren; y (4) respetar las restricciones de soporte del proveedor al bastionar.

### 6.1 La HMI como equipo Windows

HMI-C ejecuta una edición de Windows de mantenimiento a largo plazo con el software de HMI del proveedor de refrigeración. Sus riesgos son corrientes: servicios sin parches, cuentas locales compartidas, memorias USB y herramientas de escritorio remoto. Sus restricciones no lo son: el proveedor certifica compilaciones concretas del sistema operativo, y una actualización no probada puede detener el entorno de ejecución de la HMI. Por eso el bastionado pasa por una unidad de pruebas o por una lista aprobada por el proveedor.

En NCS, eso significa que la lista de parches aprobados por el proveedor para HMI-C se comprueba antes de cada ventana de mantenimiento, y todo lo que no figura en ella se prueba primero en la unidad de pruebas de la empresa contratista.

### 6.2 Historiadores virtualizados

NCS ejecuta HIST como una máquina virtual en un pequeño servidor anfitrión de la sala de comunicaciones. La virtualización ayuda a la recuperación (una VM puede restaurarse desde una instantánea en minutos), pero concentra el riesgo: el compromiso o el fallo del hipervisor afecta a todas las VM que aloja. Las interfaces de gestión del hipervisor deben estar en una red de gestión aislada, nunca en la VLAN de la oficina. La revisión de HIST que hizo Priya encontró la consola del hipervisor alcanzable desde la VLAN de la oficina; su plan la trasladó a la VLAN de gestión, donde solo puede llegar a ella el equipo de gestión de TO.

### 6.3 Las instantáneas no son copias de seguridad

Una instantánea reside en el mismo almacenamiento que la VM; si el almacenamiento falla o un ransomware lo cifra, se pierden las dos. Una copia de seguridad es una copia separada, idealmente sin conexión o inmutable, con una restauración probada. Registre la fecha de la prueba de restauración: una copia de seguridad no probada es una esperanza. HIST tenía una instantánea, de hacía ocho meses, y ninguna copia de seguridad separada. El plan de Priya añade una copia de seguridad nocturna de la VM en un NAS de la VLAN de gestión de TO, con una copia semanal sin conexión, y una prueba de restauración en una red aislada el mes próximo.

### 6.4 Mínimo privilegio en los equipos

Los operadores usan una cuenta nominativa sin privilegios de administrador; el entorno de ejecución del proveedor usa una cuenta de servicio que no puede iniciar sesión de forma interactiva; los derechos de administrador se conceden por tarea y quedan registrados. En NCS, esto sustituyó al inicio de sesión compartido «shift» de HMI-C: los operadores inician ahora sesión con cuentas nominativas que no pueden instalar software, y el entorno de ejecución del proveedor de refrigeración funciona con una cuenta de servicio sin inicio de sesión interactivo. Cuando Priya necesitó derechos de administrador para aplicar la política de lista de permitidos, los solicitó para ese ticket de cambio, y la elevación quedó registrada con el número del ticket. El entorno de ejecución de la HMI del proveedor siguió funcionando porque su cuenta de servicio, y no un operador, es la titular de los procesos que se comunican con PLC-R1 y PLC-R2.

### Ejemplo resuelto (NCS sintética)

Priya revisa HIST: una instantánea de hace ocho meses, ninguna copia de seguridad separada, consola del hipervisor alcanzable desde la VLAN de la oficina. Su plan: copia de seguridad nocturna de la VM de HIST en un NAS separado de la VLAN de gestión de TO, con una copia semanal sin conexión; trasladar la consola del hipervisor a la VLAN de gestión; realizar y registrar una prueba de restauración en una red aislada el mes próximo.

> **Caso sintético — Northgate Cold Storage.** Los hallazgos son inventados.

### Errores y límites

Restaurar una VM en la red en funcionamiento puede crear un equipo duplicado que entre en conflicto con el original; pruebe las restauraciones en aislamiento. Algunas HMI de proveedores no tienen soporte en máquinas virtuales.

### Ejercicios — capítulo 6

- **EX016 — ¿Instantánea o copia de seguridad?** Explique por qué la instantánea de ocho meses de HIST no cuenta como copia de seguridad. *Rúbrica:* 3 = mismo almacenamiento, no independiente, desactualizada, nunca restaurada; 2 = dos motivos; 1 = uno; 0 = nada.
- **EX017 — Trasladar la consola del hipervisor.** Indique el riesgo de que la consola sea alcanzable desde la VLAN de la oficina. *Rúbrica:* 3 = un malware o usuario de la oficina podría controlar o destruir todas las VM; 2 = parcial; 1 = vago; 0 = nada.
- **EX018 — Una prueba de restauración segura.** Describa cómo probar la restauración de HIST sin perturbar la operación. *Rúbrica:* 3 = restaurar en una red aislada, verificar los datos y los servicios, registrar la fecha; 2 = dos; 1 = restaurar sobre la VM en funcionamiento; 0 = nada.

### Síntesis del capítulo

La seguridad de los sistemas operativos y la virtualización en TO consiste sobre todo en fundamentos aplicados con disciplina (mínimo privilegio, gestión aislada y copias de seguridad demostradas mediante restauración) dentro de las restricciones del proveedor.

### Siga estudiando — capítulo 06 de 30

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Fundamentos de identidad y acceso

### Resultados de aprendizaje

Usted será capaz de (1) sustituir las cuentas compartidas por cuentas nominativas y roles; (2) diseñar el acceso de empresas contratistas con límites de tiempo; (3) aplicar la autenticación multifactor donde encaje en TO; y (4) revisar el acceso con regularidad.

### 7.1 Contraseñas compartidas

En muchos emplazamientos, una única contraseña de la HMI la comparten todos los turnos y la conocen antiguos empleados. No puede decirle a un investigador quién cambió el punto de consigna de un congelador, y no puede revocarse para una sola persona. Las cuentas nominativas recuperan tanto la atribución como la revocación. IEC 62443-3-3 hace de la identificación única de los usuarios humanos un requisito del sistema dentro de su primer requisito fundamental. La revisión de accesos de Priya en NCS encontró exactamente esto: una cuenta compartida «shift» entre 11 cuentas de la HMI, además de dos cuentas de antiguos empleados.

Una cuenta compartida también debilita el registro de evidencia: una alarma reconocida como «shift» no puede vincularse a una persona.

### 7.2 Roles

NCS necesita tres roles en la HMI: observador (el vigilante de seguridad nocturno que comprueba las temperaturas), operador (reconocer alarmas, ajustar puntos de consigna dentro de los límites) e ingeniero (cambiar límites y configuraciones de alarmas). El portátil de la empresa contratista que programa PLC-R1 es, a su vez, un privilegio aparte, controlado por la posesión del portátil y por la contraseña de su proyecto. El rol de observador importa más de lo que parece. El vigilante de seguridad nocturno de NCS comprueba las temperaturas de los congeladores en HMI-C durante sus rondas; con un inicio de sesión de operador compartido, el vigilante también podría haber reconocido alarmas o cambiado un punto de consigna. Una cuenta de observador lo impide por diseño. El portátil de programación de la empresa contratista queda fuera de estos roles porque es el archivo de proyecto de PLC-R1, y no HMI-C, lo que controla qué puede descargarse en el controlador.

### 7.3 Empresas contratistas

La empresa de refrigeración necesita acceso unas pocas veces al mes. Dé a la empresa contratista cuentas nominativas deshabilitadas por defecto, habilitadas para un ticket y una franja horaria, y revisadas después. Retire la herramienta de acceso remoto siempre activa identificada en el capítulo 5. En NCS, las dos cuentas de la empresa contratista estaban siempre habilitadas. Priya las configuró como deshabilitadas por defecto; el responsable de instalaciones habilita una para un ticket y una franja horaria, y la sesión pasa por el servidor de salto, que la graba. Tras la visita, la cuenta vuelve a deshabilitarse y el registro de la sesión se archiva con el ticket. El paquete para visitas de la empresa contratista del capítulo 25 convierte estos pasos en un formulario de una página que se completa en cuatro minutos.

### 7.4 Autenticación multifactor

Use MFA para el acceso remoto y para las herramientas de ingeniería. En la HMI de la sala de control, una solicitud de MFA lenta durante una alarma puede ser perjudicial; la seguridad física de la sala y tiempos cortos de bloqueo de pantalla pueden ser un mejor equilibrio. Documente la elección. La elección de Priya en NCS: MFA en el servidor de salto para las sesiones de la empresa contratista y en las herramientas de ingeniería, pero no en la propia HMI-C. La sala de control está cerrada con llave, HMI-C se bloquea tras un breve período de inactividad y los operadores inician sesión con cuentas nominativas. Una solicitud de MFA que retrasara a un operador al reconocer una alarma de temperatura alta en Freezer-2 crearía un riesgo peor que el que elimina, y ese razonamiento está escrito en la política de acceso.

### 7.5 Revisiones

Cada trimestre, enumere las cuentas habilitadas y compárelas con la lista de personal y de empresas contratistas. Deshabilite las cuentas de quienes se marchan el mismo día en que recursos humanos se lo notifique. En NCS, esta revisión encontró 11 cuentas de la HMI: 6 de personal actual, 2 de antiguos empleados, 1 cuenta compartida «shift» y 2 cuentas de la empresa contratista que estaban siempre habilitadas. Las dos cuentas de antiguos empleados se deshabilitaron el mismo día; la cuenta compartida se sustituyó por cuentas nominativas de operador en un mes; las cuentas de la empresa contratista pasaron a estar deshabilitadas por defecto. La revisión del trimestre siguiente debe partir de esa lista y confirmar que ninguno de los cuatro problemas ha vuelto, por ejemplo una nueva cuenta de la empresa contratista creada durante una visita de emergencia y nunca deshabilitada.

### Ejemplo resuelto (NCS sintética)

La revisión de accesos de Priya encuentra 11 cuentas de la HMI: 6 de personal actual, 2 de antiguos empleados, 1 cuenta compartida «shift» y 2 cuentas de la empresa contratista siempre habilitadas. Acciones: deshabilitar hoy las 2 cuentas de antiguos empleados; sustituir «shift» por cuentas nominativas de operador en un mes; configurar las cuentas de la empresa contratista como deshabilitadas por defecto, con habilitación por ticket.

> **Caso sintético — Northgate Cold Storage.** Los recuentos son inventados.

### Errores y límites

El bloqueo de cuentas en las pantallas de la sala de control puede impedir actuar a un operador durante una emergencia; prefiera alertas y retardos. Algunos PLC heredados no tienen ninguna cuenta de usuario; protéjalos mediante controles de red.

### Ejercicios — capítulo 7

- **EX019 — Elegir un rol.** El vigilante nocturno debe comprobar las temperaturas de los congeladores en HMI-C. ¿Qué rol y por qué? *Rúbrica:* 3 = observador, mínimo privilegio, sin cambios de punto de consigna; 2 = solo el rol; 1 = operador; 0 = ingeniero.
- **EX020 — Diseño del acceso de la empresa contratista.** Escriba tres reglas para las cuentas de la HMI de la empresa contratista. *Rúbrica:* 3 = nominativas, deshabilitadas por defecto, habilitadas por ticket/franja con revisión; 2 = dos; 1 = una; 0 = nada.
- **EX021 — Dónde encaja la MFA.** Nombre una ruta de acceso de NCS que debe tener MFA y otra en la que documentaría una alternativa. *Rúbrica:* 3 = acceso remoto/ruta de ingeniería; HMI de la sala de control con control físico; 2 = una; 1 = MFA en todas partes sin reflexión; 0 = nada.

### Síntesis del capítulo

Las cuentas nominativas, los roles ajustados, el acceso de las empresas contratistas limitado en el tiempo y las revisiones periódicas dan a la identidad en TO tanto rendición de cuentas como seguridad funcional.

### Siga estudiando — capítulo 07 de 30

[← Capítulo 06 (borrador)](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 (borrador) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Fundamentos de arquitectura de seguridad

### Resultados de aprendizaje

Usted será capaz de (1) dividir una instalación pequeña en zonas; (2) definir conductos entre zonas con el tráfico permitido; (3) situar una DMZ para los servicios compartidos; y (4) explicar la defensa en profundidad con capas concretas.

### 8.1 Zonas para NCS

IEC 62443-3-2 introduce las zonas (grupos de activos con requisitos de seguridad comunes) y los conductos (las rutas de comunicación entre ellas). NCS necesita al menos cuatro zonas: oficina, control de refrigeración (PLC-R1, PLC-R2, HMI-C), registro y cámaras (registradores, GW-LOG, CAM-DOCK), y una pequeña DMZ que contiene la réplica del historiador y el servidor de salto para el acceso remoto. El diagrama de zonas de Priya mostraba la regla 9 cruzando directamente de oficina a control; como ningún conducto de la lista lo permitía, el propio documento de arquitectura dio el motivo para eliminarla.

El diagrama también hizo concreto el propósito de la DMZ: es donde los usuarios de la oficina leen datos sin entrar en la zona de control.

### 8.2 Conductos

Cada conducto enumera lo que puede atravesarlo. Oficina → DMZ: HTTPS hacia los informes de la réplica del historiador. DMZ → control: nada iniciado desde la DMZ, salvo la sesión del servidor de salto hacia HMI-C cuando está habilitada. Control → DMZ: replicación del historiador. Zona de registro → internet: solo GW-LOG hacia la nube del proveedor por el 443. Todo lo demás se deniega. La tabla de conductos de Priya tiene cinco columnas: zona de origen, zona de destino, protocolo, iniciador y propósito. La columna del iniciador es la que más importa: la replicación de control a DMZ la inicia el lado de control, así que la DMZ nunca necesita una regla que le permita abrir sesiones hacia dentro.

### 8.3 Por qué una DMZ

Sin una DMZ, los usuarios de la oficina que necesitan informes de temperatura se conectan directamente a la zona de control. Con ella, llegan a una copia, y la zona de control no acepta ninguna sesión desde la oficina. Ese único cambio elimina la ruta que usa la mayor parte del ransomware corriente para llegar a las HMI. En NCS, los informes que quieren los usuarios son certificados de temperatura y horas de funcionamiento de los compresores. La macro de energía de OFFICE-7 leía las horas de funcionamiento directamente de PLC-R2 a través de la regla 9; la corrección de Priya hizo que leyera los mismos valores de la réplica del historiador en la DMZ, y solo entonces se bloqueó el paso de oficina a control.

### 8.4 Defensa en profundidad

Capas en NCS: cortafuegos entre zonas; cuentas nominativas; lista de permitidos en HMI-C; supervisión pasiva de la zona de control; copias de seguridad sin conexión; y, fuera del control del equipo de seguridad, la detección de amoníaco y la ventilación de emergencia independientes. Cada capa supone que la anterior puede fallar. La evaluación de Priya en el capítulo 23 muestra esa suposición en acción: cinco de seis controles se superaron, pero la regla de la zona de cámaras permitía que CAM-DOCK llegara a HIST por un puerto web. Las demás capas (cuentas nominativas, lista de permitidos en HMI-C y supervisión pasiva) seguían en su sitio mientras se restringía la regla.

### Ejemplo resuelto (NCS sintética)

Priya dibuja el diagrama de zonas y enumera los conductos en una tabla con zona de origen, zona de destino, protocolo, iniciador y propósito. Al compararla con el cortafuegos actual, encuentra la regla de la puesta en marcha del capítulo 2 cruzando directamente de oficina a control. El documento de arquitectura da el motivo para eliminarla: no es un conducto de la lista.

> **Caso sintético — Northgate Cold Storage.** Las zonas son un diseño didáctico.

### Errores y límites

Las zonas sobre el papel no significan nada hasta que se imponen en los conmutadores y los cortafuegos. Las cámaras a menudo se olvidan; son dispositivos de red con sus propias vulnerabilidades y también deben pertenecer a una zona.

### Ejercicios — capítulo 8

- **EX022 — Situar CAM-DOCK.** ¿A qué zona de NCS deben incorporarse las cámaras del muelle y por qué no a la zona de control? *Rúbrica:* 3 = zona de registro/cámaras (o una zona propia); sin relación con el control y con vulnerabilidades frecuentes; 2 = solo la zona; 1 = zona de control; 0 = nada.
- **EX023 — Una fila de la tabla de conductos.** Escriba la fila de la replicación del historiador. *Rúbrica:* 3 = control → DMZ, protocolo/puerto, iniciador el lado de control, propósito; 2 = tres campos; 1 = vago; 0 = nada.
- **EX024 — Capas que suponen el fallo.** Nombre dos capas de NCS y diga qué fallo cubre cada una. *Rúbrica:* 3 = dos capas con el fallo concreto que cubren; 2 = solo las capas; 1 = una; 0 = nada.

### Síntesis del capítulo

Las zonas, los conductos y una DMZ convierten «segmentar la red» en un diseño comprobable, y la defensa en profundidad hace que el fallo de cada capa sea superable.

### Siga estudiando — capítulo 08 de 30

[← Capítulo 07 (borrador)](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 (borrador) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Evidencia y medición

### Resultados de aprendizaje

Usted será capaz de (1) reunir evidencia con marcas de tiempo, fuentes y hashes; (2) separar lo que vio de lo que concluyó; (3) contar con denominadores; y (4) presentar una medición con su incertidumbre.

### 9.1 Registrar la evidencia

Para cada observación, registre: qué se observó, dónde, cuándo (con la fuente del reloj), quién y cómo. Para los archivos exportados, añada un hash SHA-256, calculado con `hashlib.sha256(open(path, "rb").read()).hexdigest()`, para que cualquiera pueda confirmar que el archivo no ha cambiado. La entrada E-014 de Priya es el modelo: marca de tiempo 2026-03-03 10:22 con el reloj del portátil sincronizado por NTP, su nombre, la configuración del cortafuegos exportada desde la interfaz web de FW-1 como fw1-0303.txt y un hash SHA-256 registrado junto al archivo.

El hash, que empieza por 9c1e…, permite a cualquiera confirmar más adelante que el archivo no ha cambiado desde esa entrada.

### 9.2 Observación y conclusión

«La regla 9 permite cualquier origen hacia TCP 502 en 10.20.0.0/24 (exportación del cortafuegos del 3 de marzo, hash registrado)» es una observación. «Un ransomware de la oficina podría llegar a los PLC» es una conclusión. Ambas pertenecen a un informe, etiquetadas. Los lectores confían en los informes que hacen visible la línea entre ellas. La entrada E-014 de Priya mantiene las dos en líneas separadas: la observación de que la regla 9 permite cualquier origen hacia TCP 502 en 10.20.0.0/24 y, en su propia línea, la conclusión de que los equipos de la oficina pueden llegar a los puertos Modbus de los PLC. Un lector que no esté de acuerdo con la conclusión puede seguir confiando en la observación y contrastarla con la exportación con hash.

### 9.3 Denominadores

«Cinco registradores tienen certificados caducados» significa poco sin «de 40». «Dos de 11 cuentas pertenecen a antiguos empleados» es más claro que «existen algunas cuentas de personas que se marcharon». Los porcentajes sin recuentos ocultan las muestras pequeñas. En NCS, los denominadores proceden de las propias tablas de Priya: 2 cuentas de antiguos empleados de 11 cuentas de la HMI, 1 certificado de registrador caducado de los 4 que comprueba el laboratorio del capítulo 22, 2 flujos no aprobados de 5 conversaciones vistas. Cada recuento dice al lector tanto el tamaño del problema como el tamaño de lo que se comprobó. Un informe que dijera «algunas cuentas pertenecen a personas que se marcharon» invitaría al lector a adivinar si eran 2 o 20.

### 9.4 Incertidumbre

Si comprobó 10 de 40 registradores y encontró 2 con contraseñas por defecto, la tasa de toda la flota es incierta. Diga: «2 de 10 muestreados; los 30 restantes todavía no se han comprobado». Evite extrapolar «el 20 % de la flota» salvo que la muestra fuera aleatoria y usted indique la incertidumbre. En NCS, la respuesta del proveedor de que cada registrador tiene una contraseña única impresa en su etiqueta es una afirmación sobre los 40; una muestra de 10 comprobada en el banco la pone a prueba. Si los 10 coinciden con la afirmación, escriba «10 de 10 muestreados la cumplían; 30 sin comprobar», no «la flota cumple 5.1».

### Ejemplo resuelto (NCS sintética)

Entrada del registro de evidencia de Priya: «E-014, 2026-03-03 10:22 (reloj del portátil sincronizado por NTP), Priya Nair, configuración del cortafuegos exportada desde la interfaz web de FW-1, archivo fw1-0303.txt, SHA-256 que empieza por 9c1e…, observación: la regla 9 permite any → 10.20.0.0/24 TCP 502; conclusión (en línea aparte): los equipos de la oficina pueden llegar a los puertos Modbus de los PLC».

> **Caso sintético — Northgate Cold Storage.** Los identificadores de evidencia y los hashes son inventados.

### 9.5 Cadena de custodia en un emplazamiento pequeño

Los emplazamientos pequeños rara vez tienen armarios para evidencias. Un mínimo práctico en NCS es una carpeta cifrada por investigación, una copia de solo lectura de cada exportación original y un registro de custodia que enumere cada transferencia: quién entregó qué a quién, cuándo y por qué. Si el caso llega más tarde a una aseguradora o a la policía, ese registro es lo que demuestra que la evidencia no se alteró entre el cortafuegos y el informe. Guarde el registro con la evidencia, no en el correo electrónico de alguien.

La exportación E-014 de Priya es la primera entrada de un registro así.

### Errores y límites

Los relojes de los dispositivos derivan; anote de qué reloj procede cada marca de tiempo. Un hash demuestra que un archivo no ha cambiado desde que se calculó, no que su contenido fuera verdadero.

### Ejercicios — capítulo 9

- **EX025 — ¿Observación o conclusión?** Etiquete: (a) «HMI-C tenía un servicio de escritorio compartido en ejecución a las 14:05»; (b) «la empresa contratista lo estaba usando». *Rúbrica:* 3 = observación, conclusión; 2 = con razonamiento débil; 1 = al revés; 0 = nada.
- **EX026 — Reescribir con un denominador.** Reescriba «varios registradores necesitan certificados nuevos». *Rúbrica:* 3 = recuento sobre el total, con fecha; 2 = solo el recuento; 1 = solo el porcentaje; 0 = nada.
- **EX027 — Informar de una muestra parcial.** Escriba la frase que informa de 2 registradores con contraseña por defecto entre 10 comprobados. *Rúbrica:* 3 = 2 de 10 muestreados, 30 sin comprobar, sin extrapolar; 2 = parcial; 1 = «el 20 % de la flota»; 0 = nada.

### Síntesis del capítulo

La evidencia se vuelve fiable cuando tiene marca de tiempo y hash, se cuenta frente a un denominador y se mantiene separada de la interpretación.

### Siga estudiando — capítulo 09 de 30

[← Capítulo 08 (borrador)](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 (borrador) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Seguridad de TO, IoT y sistemas ciberfísicos: orientación

### Resultados de aprendizaje

Usted será capaz de (1) definir TO, IoT y sistemas ciberfísicos en los términos de NCS; (2) describir el lazo de control de la refrigeración; (3) nombrar los principales documentos de orientación y a quién se dirigen; y (4) explicar por qué los sistemas de seguridad funcional quedan fuera de los cambios de seguridad.

### 10.1 Tres términos que se solapan

La tecnología operacional supervisa y controla procesos físicos; aquí, compresores, ventiladores de evaporador y válvulas. Los dispositivos IoT son sensores y actuadores conectados a la red; aquí, los registradores inalámbricos de temperatura y las cámaras. Un sistema ciberfísico es el lazo de medir, calcular y actuar sobre el mundo físico. NCS es las tres cosas a la vez. En NCS el solapamiento se ve en una sola sala: la sonda del Congelador 2 alimenta a PLC-R1, mientras que un registrador inalámbrico en la misma sala informa a la nube a través de GW-LOG. Uno es TO, el otro IoT, y ambos describen la misma temperatura física, que es lo que hace posible la comparación de dos sondas del capítulo 24.

### 10.2 El lazo de refrigeración

Una sonda de temperatura del Congelador 2 informa de −21 °C; PLC-R1 la compara con el punto de consigna de −22 °C y aumenta la capacidad del compresor; se evapora más refrigerante, la sala se enfría y la sonda vuelve a informar. Un atacante que cambie el punto de consigna, falsifique la sonda o anule la orden al compresor rompe el lazo. La técnica T0836 *Modify Parameter* de ATT&CK for ICS cubre el caso del punto de consigna. El mapa de Priya de este lazo, sonda TT-F2 → PLC-R1 → compresor C-1 → evaporador → sala → TT-F2, añade dos caminos independientes: la segunda vista de la temperatura del registrador inalámbrico y el panel de detección de gas que dispara la ventilación sin PLC-R1.

### 10.3 Mapa de orientaciones

NIST SP 800-82r3 orienta los programas de seguridad de TO para propietarios de activos como NCS. La serie IEC 62443 cubre los sistemas de automatización y control industrial para propietarios, integradores y proveedores de productos. NIST IR 8259 describe las actividades de ciberseguridad para fabricantes de dispositivos IoT, y ETSI EN 303 645 fija una base para productos IoT de consumo, útil como lista de comprobación para comprar registradores y cámaras. Priya usa EN 303 645 exactamente con ese fin: su cuestionario para el proveedor de los registradores plantea las preguntas de 5.1, 5.2, 5.3, 5.5 y 5.8 antes de que NCS compre más. Las respuestas deciden después si hace falta un control compensatorio, como comparar las sondas de los registradores y del PLC.

### 10.4 La seguridad funcional queda aparte

La detección de amoníaco y la ventilación de emergencia son sistemas de seguridad para las personas. El trabajo de seguridad puede observarlos e informar sobre ellos, pero los cambios pasan por el responsable de seguridad funcional y el ingeniero de refrigeración, nunca como efecto secundario de un proyecto de cortafuegos. En NCS esta regla se aplica directamente al trabajo de Priya con el cortafuegos. Cuando trasladó las cámaras del muelle a su propia zona, confirmó con el ingeniero de refrigeración que el panel de detección de gas no tenía ninguna conexión de red a la que el cambio pudiera afectar. Si la hubiera tenido, el cambio habría ido primero al responsable de seguridad funcional. Sus informes pueden señalar que el panel de detección de gas dispara la ventilación sin PLC-R1, lo que reduce varios escenarios cibernéticos, pero ella no lo prueba ni lo reconfigura.

### Ejemplo resuelto (NCS sintética)

Priya traza el lazo del Congelador 2: sonda TT-F2 → PLC-R1 → compresor C-1 → evaporador → sala → TT-F2. Al lado anota los caminos independientes: los registradores inalámbricos dan a la nube una segunda vista de la temperatura, y el panel de detección de gas dispara la ventilación sin PLC-R1. Ambos reducen la probabilidad de que un solo compromiso oculte un problema.

> **Caso sintético — Northgate Cold Storage.** Los nombres de las etiquetas son inventados.

### Errores y límites

Las normas de IoT de consumo no se aplican automáticamente a los dispositivos industriales; úselas como preguntas de referencia. Los diagramas de lazo simplifican; los sistemas reales tienen cascadas y enclavamientos.

### Ejercicios — capítulo 10

- **EX028 — Tres puntos de ataque en el lazo del Congelador 2.** Nombre uno por elemento: sensor, controlador, actuador. *Rúbrica:* 3 = tres puntos plausibles; 2 = dos; 1 = uno; 0 = nada.
- **EX029 — Elegir una lista de comprobación de compra.** ¿Qué documento usaría para redactar preguntas de compra para nuevos registradores de temperatura? *Rúbrica:* 3 = ETSI EN 303 645 (o NIST IR 8259 para las actividades del fabricante) con su razón; 2 = solo el nombre; 1 = solo SP 800-82; 0 = nada.
- **EX030 — Por qué los registradores ayudan a la integridad.** Explique cómo los registradores en la nube reducen el impacto de una lectura falsificada de TT-F2. *Rúbrica:* 3 = un camino de medición independiente revela el desacuerdo; 2 = parcial; 1 = vago; 0 = nada.

### Síntesis del capítulo

Orientarse significa ver el lazo físico, saber qué orientación corresponde a qué papel y mantener los sistemas de seguridad funcional a salvo de efectos secundarios del trabajo de seguridad.

### Siga estudiando — capítulo 10 de 30

[← Capítulo 09 (borrador)](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 (borrador) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Seguridad de TO, IoT y sistemas ciberfísicos: activos y contexto

### Resultados de aprendizaje

Usted será capaz de (1) construir un inventario combinando la documentación con la observación pasiva; (2) interpretar los conflictos entre fuentes; (3) añadir a cada activo su contexto de negocio, función y consecuencia; y (4) decidir qué hacer con los dispositivos desconocidos.

### 11.1 Dos fuentes, ninguna completa

La documentación de la empresa contratista de refrigeración enumera lo que se instaló; la observación pasiva del tráfico de red muestra lo que está comunicándose ahora. A la documentación se le escapan las incorporaciones posteriores; a la observación, los dispositivos silenciosos o apagados. NIST SP 800-82r3 recomienda combinar métodos en lugar de depender del escaneo activo, que puede perturbar a los dispositivos frágiles.

```python
"""Lab 11: merge two synthetic NCS asset lists and flag conflicts (no scanning)."""
eng = {"PLC-R1": "fw 2.4", "PLC-R2": "fw 2.4", "HMI-C": "win10-ltsc", "GW-LOG": "fw 1.9"}
seen = {"PLC-R1": "fw 2.4", "PLC-R2": "fw 2.1", "GW-LOG": "fw 1.9", "CAM-DOCK": "fw ?"}
for a in sorted(set(eng) | set(seen)):
    e, s = eng.get(a), seen.get(a)
    status = "match" if e == s else ("only-in-docs" if s is None else "only-on-network" if e is None else "VERSION-CONFLICT")
    print(f"{a:9} docs={e or '-':11} network={s or '-':8} {status}")
```

Ejecútelo con `python3 lab_inv.py`. Salida verificada:

```text
CAM-DOCK  docs=-           network=fw ?     only-on-network
GW-LOG    docs=fw 1.9      network=fw 1.9   match
HMI-C     docs=win10-ltsc  network=-        only-in-docs
PLC-R1    docs=fw 2.4      network=fw 2.4   match
PLC-R2    docs=fw 2.4      network=fw 2.1   VERSION-CONFLICT
```

En NCS, a la documentación le faltaba CAM-DOCK y a la observación le faltaba HMI-C; ninguna de las dos fuentes por sí sola era el inventario. La comparación también reveló el conflicto de versión de PLC-R2, que solo un recorrido por la planta podía resolver.

### 11.2 Leer los conflictos

CAM-DOCK aparece solo en la red: alguien instaló una cámara sin actualizar los registros. HMI-C aparece solo en la documentación: puede que estuviera en silencio durante la ventana de observación o que su tráfico no se capturara. PLC-R2 muestra un conflicto de versión (la documentación dice 2.4 y la red muestra 2.1), lo que importa porque un aviso de seguridad podría afectar a la 2.1 pero no a la 2.4. Priya resolvió el conflicto de PLC-R2 recorriendo la sala de máquinas con la empresa contratista y leyendo la versión en el panel frontal: 2.1. La documentación estaba equivocada; el controlador nunca se había actualizado. Corrigió el inventario con el recorrido por la planta como fuente.

### 11.3 Contexto

Para cada activo añada función, zona, responsable y consecuencia de su pérdida. La consecuencia de la cámara es baja para la refrigeración, pero puede ser un punto de entrada; la consecuencia de PLC-R2 es alta, así que su conflicto de versión va primero. El cuaderno de Priya da a cada una de las cinco filas esos cuatro campos. PLC-R2: control de compresores, zona de control de refrigeración, empresa contratista y responsable de instalaciones, pérdida de refrigeración en cuestión de horas. CAM-DOCK: vídeo del muelle, actualmente en la red de registradores, equipo de logística, consecuencia baja para la refrigeración pero posible punto de apoyo. La columna de consecuencias es lo que convierte cinco estados en una lista de trabajo ordenada.

### 11.4 Dispositivos desconocidos

Un dispositivo desconocido se investiga físicamente antes que nada: encontrarlo, identificar a su responsable, decidir si debe estar ahí. Nunca «pruebe» un dispositivo desconocido enviándole tráfico. En NCS, la dirección desconocida 10.4.2.77 vista en el capítulo 19 se rastreó así: una búsqueda física encontró una impresora del muelle conectada a un puerto de la zona de cámaras, instalada por el equipo de logística con una dirección copiada del plan de otro emplazamiento. Nadie le envió un paquete para averiguar qué era. Se trasladó, se le asignó una nueva dirección y se añadió al inventario con logística como responsable.

### Ejemplo resuelto (NCS sintética)

Priya recorre la sala de máquinas con la empresa contratista y lee la versión de PLC-R2 en la pantalla de su panel frontal: 2.1. La documentación estaba equivocada; el controlador nunca se actualizó. Corrige el inventario, registra el recorrido por la planta como fuente y abre un tique para planificar la actualización con la empresa contratista.

> **Caso sintético — Northgate Cold Storage.** Los datos del laboratorio y el recorrido por la planta son inventados.

### Errores y límites

La observación pasiva depende del lugar de captura; un puerto espejo en un conmutador solo ve el tráfico de ese conmutador. La cadena de versión que comunica un dispositivo puede ser errónea o estar falseada.

### Ejercicios — capítulo 11

- **EX031 — Explicar `only-in-docs`.** Dé dos razones posibles por las que HMI-C no apareció en la observación de la red. *Rúbrica:* 3 = en silencio o apagada durante la ventana; el punto de captura no veía su tráfico; 2 = una; 1 = «no existe»; 0 = nada.
- **EX032 — Priorizar los conflictos.** ¿Qué conflicto atiende Priya primero y por qué? *Rúbrica:* 3 = la versión de PLC-R2, por su consecuencia alta y la relevancia de los avisos; 2 = solo la elección; 1 = la cámara; 0 = nada.
- **EX033 — Añadir un quinto dispositivo.** Añada `"SENS-NH3": "fw 3.0"` solo a `seen`. ¿Qué imprime el laboratorio para él? *Rúbrica:* 3 = `SENS-NH3 docs=- network=fw 3.0 only-on-network`; 2 = solo el estado; 1 = `match`; 0 = nada.

### Síntesis del capítulo

Un inventario digno de confianza concilia documentos, observación y recorridos por la planta, y pone la consecuencia al lado de cada fila.

### Siga estudiando — capítulo 11 de 30

[← Capítulo 10 (borrador)](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 (borrador) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Seguridad de TO, IoT y sistemas ciberfísicos: flujos de datos

### Resultados de aprendizaje

Usted será capaz de (1) redactar una matriz de flujos aprobados; (2) comparar con ella los flujos observados; (3) interpretar los flujos no aprobados y los aprobados que no se usan; y (4) convertir la comparación en cambios del cortafuegos.

### 12.1 La matriz de flujos

Una matriz de flujos enumera cada conversación permitida: origen, destino, puerto y propósito. Es la tabla de conductos del capítulo 8 hecha lo bastante precisa como para ponerla a prueba. NCS tiene cuatro flujos aprobados: HMI-C hacia cada PLC por Modbus/TCP 502, el historiador consultando a PLC-R1 y GW-LOG hacia la nube del proveedor por 443.

```python
"""Lab 12: compare observed synthetic flows with the approved flow matrix."""
approved = {("HMI-C", "PLC-R1", 502), ("HMI-C", "PLC-R2", 502), ("GW-LOG", "CLOUD-LOG", 443), ("HIST", "PLC-R1", 502)}
observed = [("HMI-C", "PLC-R1", 502), ("GW-LOG", "CLOUD-LOG", 443), ("OFFICE-7", "PLC-R2", 502),
            ("HIST", "PLC-R1", 502), ("GW-LOG", "PLC-R1", 502)]
for f in observed:
    print(f"{f[0]:8} -> {f[1]:9} :{f[2]:<4} {'approved' if f in approved else 'UNAPPROVED'}")
print("approved but not seen:", sorted(approved - set(observed)))
```

Ejecútelo con `python3 lab_flows.py`. Salida verificada:

```text
HMI-C    -> PLC-R1    :502  approved
GW-LOG   -> CLOUD-LOG :443  approved
OFFICE-7 -> PLC-R2    :502  UNAPPROVED
HIST     -> PLC-R1    :502  approved
GW-LOG   -> PLC-R1    :502  UNAPPROVED
approved but not seen: [('HMI-C', 'PLC-R2', 502)]
```

El laboratorio compara esos cuatro flujos aprobados con cinco conversaciones observadas. Las dos filas no aprobadas, OFFICE-7 comunicándose con PLC-R2 y GW-LOG llegando a PLC-R1, son las que hay que investigar primero, mientras que el flujo HMI-C hacia PLC-R2 que no se vio puede simplemente no haberse producido durante la captura. El capítulo 27 muestra más adelante que a la lista le faltaba la consulta del historiador a PLC-R2, un flujo aprobado que nadie había anotado.

### 12.2 Flujos no aprobados

Que OFFICE-7 hable Modbus con PLC-R2 es exactamente lo que permitía la regla 9. Podría ser la macro de una hoja de cálculo de un ingeniero, o software malicioso. En cualquier caso, es un camino desde la oficina hasta un controlador de compresores. Que GW-LOG hable con PLC-R1 es más extraño: la pasarela de los registradores no tiene ningún motivo para hablar Modbus. Podría ser una función de «integración» del proveedor o un indicio de compromiso. Priya rastreó ambos. OFFICE-7 ejecutaba una macro de informe energético que leía las horas de funcionamiento de los compresores en PLC-R2; el proveedor de los registradores confirmó en GW-LOG una función de «integración con PLC» no utilizada y activada por defecto, que se desactivó.

### 12.3 Aprobados pero sin uso

HMI-C → PLC-R2 no apareció. Quizá la ventana fue corta; quizá la HMI lee PLC-R2 a través de PLC-R1. Las aprobaciones sin uso son candidatas a eliminarse tras consultarlo con operaciones: menos caminos abiertos, menos que defender. El capítulo 27 muestra el riesgo de leer esto demasiado deprisa. La ventana de observación tampoco captó al historiador consultando a PLC-R2, así que la matriz de flujos solo recogía HIST → PLC-R1. Cuando el nuevo conjunto de reglas entró en servicio, HIST dejó de recibir etiquetas de PLC-R2 en cuatro minutos y Priya revirtió el cambio. Un flujo aprobado pero no visto es una pregunta para operaciones y los proveedores, no una prueba de que el flujo no se use.

### 12.4 De la comparación al cambio

Cada flujo no aprobado recibe un responsable y una decisión: aprobarlo con justificación (y actualizar la matriz) o bloquearlo. El bloqueo se hace en una ventana planificada y con operaciones informada, porque un flujo «misterioso» puede resultar ser algo que la planta necesita. Las dos decisiones de Priya: la macro energética de OFFICE-7 pasó a leer las horas de funcionamiento en la réplica del historiador en la DMZ, y el tráfico oficina → control se bloqueó en la ventana de mantenimiento del 20 de marzo, después del cambio; la función de «integración con PLC» de GW-LOG se desactivó con el acuerdo del proveedor de los registradores, y el flujo desapareció sin ningún cambio en el cortafuegos.

### Ejemplo resuelto (NCS sintética)

Priya pregunta en la oficina: OFFICE-7 ejecuta una macro de informe energético que lee directamente en PLC-R2 las horas de funcionamiento de los compresores. Propone leer los mismos valores en la réplica del historiador en la DMZ y después bloquear oficina → control. Para GW-LOG → PLC-R1 contacta con el proveedor de los registradores, que confirma una función de «integración con PLC» no utilizada y activada por defecto; se desactiva y el flujo desaparece.

> **Caso sintético — Northgate Cold Storage.** Los flujos y las explicaciones son inventados.

### Errores y límites

Las ventanas de observación no captan flujos mensuales o estacionales, como los programas de desescarche o los informes de fin de mes. Los puertos no prueban el protocolo; un flujo en el 502 puede no ser Modbus.

### Ejercicios — capítulo 12

- **EX034 — Clasificar una observación nueva.** Añada `("HMI-C", "PLC-R2", 502)` a `observed`. ¿Qué cambia en la salida? *Rúbrica:* 3 = se imprime `approved` y la lista de no vistos queda vacía; 2 = un efecto; 1 = `UNAPPROVED`; 0 = nada.
- **EX035 — Decisión para OFFICE-7.** Redacte el registro de decisión del flujo de OFFICE-7. *Rúbrica:* 3 = causa, camino sustitutivo a través de la DMZ, fecha del bloqueo, responsable; 2 = tres; 1 = «bloquearlo»; 0 = nada.
- **EX036 — Por qué GW-LOG → PLC-R1 es sospechoso.** Explíquelo en dos frases. *Rúbrica:* 3 = no hay necesidad de negocio de que la pasarela de los registradores hable Modbus; conecta una zona expuesta a internet con el control; 2 = una; 1 = vago; 0 = nada.

### Síntesis del capítulo

Comparar los flujos observados con una matriz aprobada encuentra los caminos que nadie pretendía, y cada uno termina en una decisión con responsable.

### Siga estudiando — capítulo 12 de 30

[← Capítulo 11 (borrador)](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 (borrador) →](#ch-13)

<a id="ch-13"></a>

## Capítulo 13 — Seguridad de TO, IoT y sistemas ciberfísicos: escenarios de riesgo

### Resultados de aprendizaje

Usted será capaz de (1) redactar escenarios de riesgo que vinculen una amenaza, un camino y una consecuencia física; (2) estimar probabilidad y consecuencia en escalas sencillas; (3) identificar las salvaguardas existentes; y (4) ordenar los escenarios para actuar.

### 13.1 Estructura del escenario

Un escenario útil se lee así: «[Amenaza] usa [camino] para provocar [acción], lo que lleva a [consecuencia], salvo que [salvaguarda] funcione». Para NCS: «Un ransomware de la oficina usa el flujo oficina → control para cifrar HMI-C y deja a los operadores sin pantalla; la refrigeración continúa con la lógica de los PLC, pero las alarmas son invisibles hasta que se restablece la pantalla, salvo que las alertas de los registradores en la nube lleguen al teléfono del responsable de turno». Los tres escenarios de Priya para NCS siguen esta forma: la herramienta remota de la empresa contratista usada indebidamente para cambiar los puntos de consigna de los congeladores, un ransomware de la oficina que llega a HMI-C y una cámara expuesta a internet usada como punto de apoyo.

### 13.2 Escalas

Una escala de consecuencias de tres puntos se adapta a un emplazamiento pequeño: 1 = molestia, 2 = pérdida de existencias o problema normativo, 3 = daño a las personas o pérdida del negocio. La probabilidad, también de 1 a 3, es un juicio basado en la exposición y en la actividad de amenazas conocida. Escriba la razón al lado de cada puntuación. Las puntuaciones de Priya muestran la escala en uso: el escenario de la herramienta de la empresa contratista tiene consecuencia 2, porque un punto de consigna cambiado supone pérdida de existencias y no daño a las personas, y probabilidad 2, porque la herramienta estaba siempre activa pero no se sabía que las credenciales de la empresa contratista estuvieran expuestas. El punto de apoyo de la cámara tiene consecuencia 1 y probabilidad 2. Cada puntuación lleva su razón escrita al lado.

### 13.3 Salvaguardas

Las salvaguardas existentes cambian la historia. La detección independiente de amoníaco hace improbable que una fuga de gas causada por un ciberataque pase desapercibida. Las alertas de los registradores en la nube aportan una segunda vista de la temperatura. La lógica de los PLC mantiene la refrigeración si se pierde la HMI. Enumerar las salvaguardas evita que los escenarios suenen peor de lo que son y muestra qué salvaguarda está haciendo mucho trabajo. En NCS, las alertas de los registradores en la nube sostienen el escenario de la herramienta de la empresa contratista: son la salvaguarda que revelaría un punto de consigna cambiado. Si una herramienta de la empresa contratista cambiara un punto de consigna, las alertas mostrarían que la sala se calienta antes de que las existencias se echaran a perder.

### 13.4 Ordenación

Ordene primero por consecuencia, después por probabilidad y después por lo barato que sea reducir el escenario. Un escenario de consecuencia 2 con una solución fácil merece a menudo actuar antes que un escenario de consecuencia 3 cuya salvaguarda ya es sólida. La ordenación de Priya sigue esta regla. Los escenarios de la herramienta de la empresa contratista y del ransomware de la oficina puntúan ambos consecuencia 2 y probabilidad 2; el ransomware queda segundo solo porque su salvaguarda, la lógica de los PLC que mantiene la refrigeración sin HMI-C, es más sólida que las alertas en la nube que protegen frente a un punto de consigna cambiado. Eliminar la regla 9 fue entonces el primero de los controles, porque era barato y reducía dos escenarios a la vez, como explica el capítulo 18.

### Ejemplo resuelto (NCS sintética)

Los tres primeros de Priya: (1) herramienta remota de la empresa contratista usada indebidamente para cambiar los puntos de consigna de los congeladores (consecuencia 2, probabilidad 2, salvaguarda: alertas de los registradores en la nube; solución: sesiones supervisadas); (2) un ransomware de la oficina llega a HMI-C (2, 2, salvaguarda: el PLC mantiene la refrigeración; solución: eliminar la regla 9); (3) cámara expuesta a internet usada como punto de apoyo (1, 2; solución: trasladarla a la zona de cámaras).

> **Caso sintético — Northgate Cold Storage.** Las puntuaciones son ilustrativas.

### Errores y límites

Las escalas sencillas ocultan diferencias dentro de una categoría. La probabilidad de un ataque deliberado cambia deprisa con las noticias de campañas; revísela.

### Ejercicios — capítulo 13

- **EX037 — Completar la frase de un escenario.** Redacte un escenario de «lecturas falsificadas de los registradores» con la estructura de cinco partes. *Rúbrica:* 3 = las cinco partes; 2 = cuatro; 1 = vago; 0 = nada.
- **EX038 — Puntuar con razones.** Puntúe la consecuencia del escenario 1 y justifíquela. *Rúbrica:* 3 = 2, con un razonamiento sobre existencias o seguridad alimentaria y la salvaguarda indicada; 2 = solo la puntuación; 1 = 3 sin razón; 0 = nada.
- **EX039 — Una salvaguarda que soporta mucho peso.** ¿Qué salvaguarda aparece en más de un escenario y qué implica eso? *Rúbrica:* 3 = las alertas de los registradores en la nube (o la autonomía de los PLC); un punto único que proteger y probar; 2 = solo el nombre; 1 = errónea; 0 = nada.

### Síntesis del capítulo

Los escenarios conectan los caminos cibernéticos con las consecuencias físicas y las salvaguardas, y unas puntuaciones sencillas y razonadas bastan para ordenar la actuación en un emplazamiento pequeño.

### Siga estudiando — capítulo 13 de 30

[← Capítulo 12 (borrador)](#ch-12) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 14 (borrador) →](#ch-14)

<a id="ch-14"></a>

## Capítulo 14 — Seguridad de TO, IoT y sistemas ciberfísicos: métodos I

### Resultados de aprendizaje

Usted será capaz de (1) realizar un recorrido estructurado por el emplazamiento; (2) entrevistar con eficacia a operadores y empresas contratistas; (3) revisar exportaciones de configuración de forma segura; y (4) reunir hallazgos con referencias a la evidencia.

### 14.1 Recorrido por la planta

Recorra el emplazamiento con alguien que sea su responsable. Busque tomas de red en lugares extraños, routers celulares dentro de los cuadros, etiquetas con contraseñas, portátiles que se han dejado conectados, memorias USB en las HMI y dispositivos que no están en el inventario. Haga fotografías solo con permiso y evite captar pantallas que muestren datos de clientes. El recorrido de Priya por NCS encontró el elemento más importante de esta lista: un pequeño router celular en el cuadro MP-2 etiquetado «contractor backup access», instalado dos años antes durante una caída de la red y olvidado. Proporcionaba un segundo camino remoto hacia PLC-R2 que ninguna regla del cortafuegos mostraba.

### 14.2 Entrevistas

Pregunte a los operadores qué hacen cuando la HMI se bloquea, quién llama a la empresa contratista y qué ha cambiado recientemente. Pregunte a la empresa contratista cómo se conecta, qué herramientas usa y dónde se guardan las copias de seguridad. Las preguntas abiertas («cuénteme paso a paso una llamada de soporte remoto») revelan más que las listas de sí o no. Tome notas con el nombre, el cargo de la persona entrevistada y la fecha; separe lo que dijo de lo que usted vio.

La entrevista con la empresa contratista explicó el router de MP-2 en una sola frase, registrada como I-04. El técnico de la empresa contratista dijo que el router se instaló durante una caída de internet de dos días para poder seguir llegando a PLC-R2, y que nadie lo retiró.

### 14.3 Revisión de la configuración

Exporte las configuraciones mediante interfaces admitidas y con cuentas de solo lectura: conjuntos de reglas del cortafuegos, ajustes de VLAN de los conmutadores, listas de usuarios de la HMI. Revise las exportaciones en su propia estación de trabajo, no en el dispositivo. Calcule el hash de las exportaciones como en el capítulo 9. En NCS la exportación del cortafuegos salió de la interfaz web de FW-1 con una cuenta de solo lectura, se guardó como fw1-0303.txt y se registró con su hash como E-014. La lista de usuarios de HMI-C se obtuvo del mismo modo, y de ahí salieron las 11 cuentas del capítulo 7. Revisar en la estación de trabajo de Priya le permitió buscar y anotar en el conjunto de reglas sin ningún riesgo de guardar por accidente un cambio en FW-1, y el hash demuestra más adelante que el archivo que revisó es el archivo que exportó.

### 14.4 Reunir los hallazgos

Cada hallazgo: título, identificadores de evidencia, activos afectados, vínculo con un escenario, recomendación y responsable. Un hallazgo por problema; combinar problemas que no guardan relación hace imposible cerrarlos. El hallazgo F-07 de Priya sigue esta forma: título, router celular no documentado en MP-2; evidencia, la foto E-021 y la entrevista I-04; activo afectado, PLC-R2; vínculo con el escenario de acceso remoto de la empresa contratista, porque es un segundo camino remoto; recomendación, retirarlo o mantenerlo apagado y encenderlo solo a petición con la aprobación del responsable de instalaciones; responsable, el responsable de instalaciones. No menciona la contraseña compartida de la HMI, que es un hallazgo aparte con su propio responsable y fecha de cierre, aunque Priya encontró ambos en la misma semana.

### Ejemplo resuelto (NCS sintética)

Durante el recorrido por la planta, Priya encuentra un pequeño router celular en el cuadro MP-2 etiquetado «contractor backup access». La empresa contratista explica que se instaló durante una caída de la red hace dos años y que se olvidó. Hallazgo F-07: «Un router celular no documentado en MP-2 proporciona un segundo camino remoto hacia PLC-R2 (evidencia: foto E-021, entrevista I-04)». Recomendación: retirarlo, o mantenerlo apagado y encenderlo solo a petición con la aprobación del responsable de instalaciones.

> **Caso sintético — Northgate Cold Storage.** Los identificadores de cuadros y de hallazgos son inventados.

### Errores y límites

Las entrevistas reflejan la memoria; confírmelas con evidencia. Nunca reinicie ni desconecte dispositivos durante un recorrido por la planta salvo que el responsable lo pida y operaciones esté de acuerdo.

### Ejercicios — capítulo 14

- **EX040 — Tres objetivos del recorrido por la planta.** Enumere tres cosas que buscar en un cuadro de control. *Rúbrica:* 3 = tres pertinentes (módems, etiquetas con contraseñas, dispositivos desconocidos, portátiles conectados); 2 = dos; 1 = una; 0 = nada.
- **EX041 — Una pregunta abierta de entrevista.** Escriba una pregunta abierta para la empresa contratista sobre el acceso remoto. *Rúbrica:* 3 = abierta y específica del proceso; 2 = abierta pero genérica; 1 = de sí o no; 0 = nada.
- **EX042 — Redactar las opciones de recomendación del hallazgo F-07.** Dé dos opciones aceptables para el router celular y la condición de cada una. *Rúbrica:* 3 = retirarlo; o apagado por defecto y encendido previa aprobación; condiciones indicadas; 2 = solo las opciones; 1 = dejarlo como está; 0 = nada.

### Síntesis del capítulo

Los recorridos por la planta, las entrevistas y las revisiones de configuración de solo lectura, enlazados por identificadores de evidencia, encuentran lo que los diagramas nunca muestran.

### Siga estudiando — capítulo 14 de 30

[← Capítulo 13 (borrador)](#ch-13) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 15 (borrador) →](#ch-15)

<a id="ch-15"></a>

## Capítulo 15 — Seguridad de TO, IoT y sistemas ciberfísicos: laboratorio guiado

### Resultados de aprendizaje

Usted será capaz de (1) analizar datos sintéticos de registradores en busca de desviaciones de temperatura; (2) relacionar el retardo de la alarma con la consecuencia para la seguridad alimentaria; (3) reconocer cómo cambiarían el resultado unos datos falsificados; y (4) documentar el resultado de un laboratorio con sus entradas y su salida.

### 15.1 La pregunta del laboratorio

¿Se mantuvo la antecámara refrigerada del Congelador 2 a 5 °C o menos y, si no, durante cuánto tiempo y saltó la alarma? El laboratorio usa diez lecturas sintéticas tomadas cada cinco minutos y una alarma que solo salta cuando una desviación dura al menos 10 minutos, un retardo que evita las alarmas molestas por la apertura de puertas.

```python
"""Lab 15: find cold-room temperature excursions in synthetic logger data (minutes, degC)."""
readings = [(0, 2.1), (5, 2.4), (10, 3.0), (15, 5.6), (20, 7.2), (25, 8.4), (30, 6.9), (35, 4.8), (40, 3.9), (45, 2.6)]
LIMIT, ALARM_DELAY = 5.0, 10
start = None
for t, v in readings:
    if v > LIMIT and start is None: start = t
    if v <= LIMIT and start is not None:
        dur = t - start
        print(f"excursion {start}-{t} min, duration {dur} min, peak {max(x for s, x in readings if start <= s < t)} C, alarm {'raised' if dur >= ALARM_DELAY else 'not raised'} (delay {ALARM_DELAY} min)")
        start = None
```

Ejecútelo con `python3 lab_excursion.py`. Salida verificada:

```text
excursion 15-35 min, duration 20 min, peak 8.4 C, alarm raised (delay 10 min)
```

Los datos de la antecámara son el conjunto sintético A, que Priya usó en su informe más abajo. El conjunto A tiene un muestreo de 5 minutos, un límite de 5 °C y un retardo de alarma de 10 minutos, los valores que repite su registro.

### 15.2 Interpretación

La desviación empezó en el minuto 15 y terminó en el 35, duró 20 minutos y alcanzó un máximo de 8,4 °C. La alarma saltó porque 20 ≥ 10. La salida también nos indica el límite de resolución: con muestras cada cinco minutos, el inicio real podría estar en cualquier punto entre los minutos 10 y 15. Esa incertidumbre de cinco minutos importa en un registro de seguridad alimentaria: un contrato con un cliente que admita desviaciones de hasta 20 minutos se cumpliría o se incumpliría según el punto de esa ventana en que la desviación empezara realmente. El informe de Priya indica una duración de 20 minutos, con un inicio incierto de hasta cinco, y deja el juicio contractual al responsable de calidad.

### 15.3 Qué cambiaría un atacante

Si las lecturas de los minutos 15–30 se sustituyeran por valores en torno a 4 °C, el script no informaría de ninguna desviación: el registro mostraría cumplimiento mientras la mercancía se calentaba. Por eso el escenario del capítulo 13 compara los datos de los registradores en la nube con la sonda propia del PLC en el historiador: dos registros independientes son mucho más difíciles de falsificar de forma coherente. El informe de Priya recoge como limitación la falta de esa comprobación cruzada: el conjunto sintético A no tiene una sonda de HIST con la que comparar. En los datos reales de NCS, la sonda de HIST en la antecámara sería la comprobación cruzada: una lectura del registrador que discrepe de ella es una pregunta antes que una desviación.

### 15.4 Registrar el resultado

Registre el archivo de entrada (o su hash), la versión del script, los parámetros de límite y retardo, y la salida. Otro tecnólogo debe poder reproducirlo exactamente. El registro de Priya dice: «Laboratorio 15 sobre las lecturas de la antecámara (conjunto sintético A): una desviación de 15 a 35 min, 20 min, máximo de 8,4 °C, alarma activada con retardo de 10 min. Resolución: muestreo de 5 min, por lo que el inicio es incierto hasta 5 min. Comprobación de integridad: comparación con la sonda TT-A1 de HIST, no disponible en el conjunto sintético; recogida como limitación». Con el hash del archivo de entrada y el límite de 5 °C y el retardo de 10 minutos registrados, otro tecnólogo puede volver a ejecutarlo y obtener la misma línea.

### Ejemplo resuelto (NCS sintética)

Priya escribe: «Laboratorio 15 sobre las lecturas de la antecámara (conjunto sintético A): una desviación de 15 a 35 min, 20 min, máximo de 8,4 °C, alarma activada con retardo de 10 min. Resolución: muestreo de 5 min, por lo que el inicio es incierto hasta 5 min. Comprobación de integridad: comparación con la sonda TT-A1 de HIST, no disponible en el conjunto sintético; recogida como limitación».

> **Caso sintético — Northgate Cold Storage.** Todas las lecturas son inventadas.

### Errores y límites

El script supone que las lecturas están ordenadas y espaciadas por igual. Una desviación que sigue en curso en la última muestra no se notifica: un error que merece la pena corregir.

### Ejercicios — capítulo 15

- **EX043 — Cambiar el retardo de la alarma.** Si `ALARM_DELAY = 25`, ¿qué imprime el laboratorio? *Rúbrica:* 3 = la misma desviación, `alarm not raised (delay 25 min)`; 2 = solo el estado de la alarma; 1 = ninguna desviación; 0 = nada.
- **EX044 — El error de la desviación sin terminar.** Añada `(50, 6.0)` a las lecturas. ¿Qué ocurre y cómo lo corregiría? *Rúbrica:* 3 = la segunda desviación no se imprime; añadir una comprobación final tras el bucle; 2 = una de las dos; 1 = dice que se imprime; 0 = nada.
- **EX045 — Comprobación de falsificación.** Describa una comprobación que revelaría lecturas sustituidas. *Rúbrica:* 3 = comparar con una sonda independiente del PLC o del historiador o con un segundo registrador, y señalar la discrepancia; 2 = parcial; 1 = vago; 0 = nada.

### Síntesis del capítulo

Un laboratorio guiado convierte lecturas en bruto en una afirmación reproducible y acotada, y muestra exactamente dónde se esconderían los datos falsificados.

### Siga estudiando — capítulo 15 de 30

[← Capítulo 14 (borrador)](#ch-14) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 16 (borrador) →](../../en/book/MANUSCRIPT.md#ch-16)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo para EX001–EX090. Northgate Cold Storage, Priya Nair y todas las cifras son sintéticos. Cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación.

**EX001.** HMI-C: de propósito general, un PC con Windows que ejecuta muchos procesos y recibe actualizaciones. PLC-R2: embebido, un único programa de control en un bucle de escaneo fijo. Registrador: embebido, un microcontrolador con batería y radio, sin sistema operativo general.

**EX002.** NCS pierde durante seis horas el registro de temperaturas en la nube y cualquier alerta remota, un hueco en la evidencia de seguridad alimentaria; no pierde la refrigeración, porque los compresores los controlan PLC-R1/R2 con independencia de la pasarela.

**EX003.** PLC-R1 | controlador embebido | hace funcionar los compresores de amoníaco 1–2 y el control de la presión de aspiración | cuadro MP-1 de la sala de máquinas | empresa de refrigeración mediante portátil de ingeniería | la cámara de congelación se calienta y las existencias están en riesgo en cuestión de horas.

**EX004.** 10.20.0.11 y 10.20.0.40 comparten la red 10.20.0 con una máscara /24, así que sí. 10.20.0.11 y 10.30.0.11 difieren en el tercer octeto, así que están en subredes distintas y el tráfico debe enrutarse.

**EX005.** «Regla 9: permitir TCP 502 desde 10.20.0.20 (HMI-C) hacia 10.20.0.11 y 10.20.0.12 (PLC-R1, PLC-R2)», con la regla final existente «deny any to any» debajo. (Como HMI-C y los PLC comparten subred, la regla solo actúa donde el tráfico se enruta; el cambio clave es eliminar el acceso desde otras subredes).

**EX006.** Con HTTPS solo saliente, la pasarela inicia todas las sesiones y el cortafuegos descarta los paquetes entrantes no solicitados, así que los equipos de internet no pueden llegar a los servicios de la pasarela; un reenvío de puertos permite que cualquiera en internet intente conectarse a ella.

**EX007.** `docs - seen` = {"A"} (documentado pero no observado); `seen - docs` = {"D"} (observado en la red pero no documentado).

**EX008.** Devuelve `None`. El script debería imprimir «-» para el valor y un estado como «only-on-network» o «missing», en lugar de fallar u omitir la fila.

**EX009.** `for name in sorted(set(docs) | set(seen)):`: recorrer la unión garantiza que los dispositivos presentes en una sola fuente sigan produciendo una línea de salida.

**EX010.** La etiqueta pintada identifica la función en una ubicación fija; sobrevive a los cambios de dirección (que cambian la IP) y a la sustitución del hardware (que cambia el número de serie), así que el historial y los hallazgos siguen asociados a la fila correcta.

**EX011.** `select tag from loggers where room = 'Freezer-2' and gateway_tag = 'GW-LOG';`

**EX012.** Sustitúyala por una columna de «referencia de credencial» que contenga el ID de la entrada del almacén de secretos (p. ej., OT-17); la propia contraseña reside en el almacén de secretos, con acceso controlado y registro, nunca en la tabla compartida.

**EX013.** Primero, la fuga de amoníaco (daño a las personas); segundo, la pérdida de refrigeración (pérdida de existencias, seguridad alimentaria); tercero, los registros de temperatura falseados (evidencia de seguridad alimentaria y confianza de los clientes); cuarto, la filtración de grabaciones de las cámaras (privacidad y confidencialidad).

**EX014.** El producto y las versiones afectados; la debilidad descrita; si se ha observado explotación; y las mitigaciones recomendadas (corrección del proveedor o solución alternativa).

**EX015.** T0886 Remote Services: el acceso de la empresa contratista usa un servicio remoto para llegar a un equipo del sistema de control.

**EX016.** Reside en el mismo almacenamiento que la VM (un fallo del almacenamiento o un ransomware se llevan ambas), tiene ocho meses de antigüedad y nunca se ha restaurado, así que no hay evidencia de que funcionaría.

**EX017.** Cualquier persona o malware de la VLAN de la oficina que obtenga las credenciales de la consola puede detener, borrar o cifrar de una sola vez todas las VM del servidor anfitrión, incluida HIST.

**EX018.** Restaurar la copia de seguridad en una VM conectada a una red de pruebas aislada sin ruta hacia producción, arrancarla, comprobar que el servicio del historiador funciona y que están los datos recientes, y después registrar la fecha, la duración y el resultado.

**EX019.** Observador: el vigilante solo necesita leer temperaturas y alarmas, así que el mínimo privilegio excluye reconocer alarmas o cambiar puntos de consigna.

**EX020.** (1) Cada ingeniero de la empresa contratista tiene una cuenta nominativa; no hay un inicio de sesión compartido de la empresa contratista. (2) Las cuentas están deshabilitadas por defecto. (3) Una cuenta solo se habilita para un ticket aprobado y una franja horaria fija, y la sesión se revisa después.

**EX021.** MFA obligatoria: la sesión remota de la empresa contratista hacia la red de TO (y el inicio de sesión del proyecto en el portátil de ingeniería). Alternativa documentada: la consola HMI-C de la sala de control, protegida por una sala cerrada con llave y un tiempo corto de bloqueo de pantalla en lugar de una solicitud de MFA durante las alarmas.

**EX022.** La zona de registro y cámaras (o una zona dedicada a las cámaras): las cámaras no tienen ninguna función en el control de la refrigeración y a menudo ejecutan firmware vulnerable, así que situarlas en la zona de control daría a un dispositivo débil una ruta directa hacia PLC-R1/R2.

**EX023.** Zona de origen: control de refrigeración (HIST). Destino: DMZ (réplica del historiador). Protocolo: el servicio de replicación del historiador en su puerto TCP fijo. Iniciador: el lado de control. Propósito: proporcionar informes a la oficina sin que la oficina acceda a la zona de control.

**EX024.** La lista de permitidos en HMI-C cubre el fallo del cortafuegos para detener un malware que llega por USB; las copias de seguridad sin conexión cubren el fallo de todas las capas preventivas cuando un ransomware cifra HIST.

**EX025.** (a) Observación: un estado registrado en un momento dado. (b) Conclusión: es una inferencia; requiere registros de sesión o la confirmación de la empresa contratista.

**EX026.** «El 12 de octubre, 2 de los 4 certificados de registradores de temperatura comprobados estaban caducados o vencían en menos de 30 días; los otros 36 registradores todavía no se han comprobado», usando el recuento real de la comprobación de certificados.

**EX027.** «De 10 registradores comprobados el 4 de marzo, 2 seguían aceptando la contraseña por defecto del proveedor; los otros 30 registradores todavía no se han comprobado».

**EX028.** Sensor: falsificar o desconectar TT-F2 para que marque menos temperatura que la real. Controlador: cambiar el punto de consigna del Congelador 2 en PLC-R1 (T0836). Actuador: forzar el apagado del compresor C-1 mediante una anulación manual o la manipulación de salidas.

**EX029.** ETSI EN 303 645: sus disposiciones (sin contraseñas por defecto universales, divulgación de vulnerabilidades, software actualizable, comunicación segura) se traducen directamente en preguntas de compra; NIST IR 8259 es un buen complemento para preguntar qué hace el fabricante.

**EX030.** Los registradores miden el Congelador 2 de forma independiente e informan por otro camino; si TT-F2 se falsifica para que marque −22 °C mientras la sala se calienta, los datos del registrador discreparán y revelarán el problema.

**EX031.** HMI-C puede haber estado inactiva o apagada durante la ventana de observación, o el puerto espejo no veía su tráfico (por ejemplo, se comunica con los PLC a través de un conmutador que no se supervisaba).

**EX032.** El conflicto de versión de PLC-R2: controla los compresores (consecuencia alta), y el firmware real (2.1) determina si los avisos le afectan, mientras que la cámara tiene una consecuencia baja para la refrigeración.

**EX033.** `SENS-NH3  docs=-           network=fw 3.0   only-on-network`: aparece porque el bucle recorre la unión de ambas fuentes.

**EX034.** Aparece una línea nueva `HMI-C -> PLC-R2 :502 approved`, y `approved but not seen` se convierte en una lista vacía `[]`, porque ya se han observado todos los flujos aprobados.

**EX035.** «Flujo OFFICE-7 → PLC-R2:502: macro de informe energético que lee las horas de funcionamiento de los compresores. Sustitución: leer las horas de funcionamiento en la réplica del historiador en la DMZ. Bloquear oficina → control el 20 de marzo en la ventana de mantenimiento, una vez cambiada la macro. Responsable: Priya Nair con el responsable de instalaciones».

**EX036.** La única función de la pasarela de los registradores es reenviar temperaturas a la nube, así que no necesita hablar Modbus con un controlador de compresores. Como está conectada a internet, un flujo así enlaza un servicio externo con la zona de control.

**EX037.** «Una cuenta comprometida en la nube del proveedor de los registradores (amenaza) usa el portal del proveedor (camino) para alterar las lecturas almacenadas del Congelador 2 (acción), de modo que los registros de seguridad alimentaria muestran cumplimiento durante una desviación real y se expiden existencias echadas a perder (consecuencia), salvo que el registro independiente de temperatura del PLC en HIST se compare con los datos de la nube (salvaguarda)».

**EX038.** Consecuencia 2: un cambio de punto de consigna puede calentar los congeladores y obligar a desechar existencias o incumplir las normas de seguridad alimentaria, pero es improbable que dañe a las personas, porque la seguridad del amoníaco es independiente, y las alertas de los registradores en la nube limitan el tiempo que pasa desapercibido.

**EX039.** Las alertas de los registradores en la nube aparecen como salvaguarda frente al uso indebido de los puntos de consigna y también dan la segunda vista cuando se pierde HMI-C; NCS debería vigilar que el propio camino de alerta funciona (alertas de prueba, estado de la pasarela), porque muchos escenarios se apoyan en él.

**EX040.** Routers celulares o wifi dentro del cuadro; etiquetas o notas que muestren contraseñas; dispositivos o cables que no estén en el inventario (por ejemplo, un portátil que se ha dejado conectado a un puerto de un PLC).

**EX041.** «Cuénteme paso a paso la última vez que se conectó a NCS en remoto, desde su oficina hasta el momento en que vio la pantalla de la HMI».

**EX042.** Opción 1: retirar el router si la empresa contratista confirma que el camino remoto principal cubre todas las necesidades de soporte. Opción 2: mantenerlo apagado y encenderlo solo a petición, con la aprobación del responsable de instalaciones y por un tiempo indicado, si de verdad se necesita un camino de respaldo durante las caídas de la red.

**EX043.** `excursion 15-35 min, duration 20 min, peak 8.4 C, alarm not raised (delay 25 min)`: la desviación no cambia, pero 20 < 25.

**EX044.** La lectura del minuto 50 inicia una nueva desviación (`start = 50`), pero el bucle termina antes de que ninguna lectura vuelva a ≤ 5 °C, así que no se imprime nada. Corrección: tras el bucle, si `start is not None`, imprimir la desviación abierta con «en curso en la última muestra».

**EX045.** Comparar cada lectura del registrador con la sonda propia del PLC registrada en HIST (o con un segundo registrador en la misma sala) y señalar cualquier intervalo en que difieran más de una tolerancia acordada, por ejemplo 2 °C.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; vuelva a verificar las ediciones antes de citarlas. Los DOI se comprobaron en Crossref. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ISA/IEC 62443 series of standards (overview; parts 3-2 and 3-3 and 4-2 are cited in the text). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS, including T0836 Modify Parameter, T0883 Internet Accessible Device and T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
