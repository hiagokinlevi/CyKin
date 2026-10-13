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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](../../en/book/MANUSCRIPT.md#ch-07) · [8](../../en/book/MANUSCRIPT.md#ch-08) · [9](../../en/book/MANUSCRIPT.md#ch-09) · [10](../../en/book/MANUSCRIPT.md#ch-10) · [11](../../en/book/MANUSCRIPT.md#ch-11) · [12](../../en/book/MANUSCRIPT.md#ch-12) · [13](../../en/book/MANUSCRIPT.md#ch-13) · [14](../../en/book/MANUSCRIPT.md#ch-14) · [15](../../en/book/MANUSCRIPT.md#ch-15) · [16](../../en/book/MANUSCRIPT.md#ch-16) · [17](../../en/book/MANUSCRIPT.md#ch-17) · [18](../../en/book/MANUSCRIPT.md#ch-18) · [19](../../en/book/MANUSCRIPT.md#ch-19) · [20](../../en/book/MANUSCRIPT.md#ch-20) · [21](../../en/book/MANUSCRIPT.md#ch-21) · [22](../../en/book/MANUSCRIPT.md#ch-22) · [23](../../en/book/MANUSCRIPT.md#ch-23) · [24](../../en/book/MANUSCRIPT.md#ch-24) · [25](../../en/book/MANUSCRIPT.md#ch-25) · [26](../../en/book/MANUSCRIPT.md#ch-26) · [27](../../en/book/MANUSCRIPT.md#ch-27) · [28](../../en/book/MANUSCRIPT.md#ch-28) · [29](../../en/book/MANUSCRIPT.md#ch-29) · [30](../../en/book/MANUSCRIPT.md#ch-30) |

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

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](../../en/book/MANUSCRIPT.md#ch-07)

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
