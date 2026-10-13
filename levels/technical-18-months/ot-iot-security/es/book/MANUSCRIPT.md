# Seguridad de TO, IoT y sistemas ciberfísicos: cuaderno de trabajo del operador técnico

- Idioma: español neutro (`es`); curso técnico, dieciocho meses; aproximadamente 1.200 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–18 de 18 tienen texto didáctico escrito a mano; los ejercicios EX001–EX072 tienen sus resultados resueltos correspondientes; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas se incluyen a partir de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4.
- Público: operadores técnicos y técnicos de mantenimiento que trabajan en líneas industriales o junto a ellas y deben reconocer problemas de seguridad, notificarlos y ayudar a recuperarse de ellos.
- Relación con los libros vecinos: el [libro del curso profesional](../../../../professional-6-months/ot-iot-security/en/book/MANUSCRIPT.md) es más breve; el [libro de tecnólogo](../../../../technologist-3-years/ot-iot-security/es/book/MANUSCRIPT.md) añade implantación y diseño. **Este libro es procedimental y se centra en la planta.**
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado. No concede autorización para acceder a emplazamientos reales. Todos los emplazamientos, personas y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los capítulos 1–4 explican la línea, la seguridad física, las redes y los protocolos; los capítulos 5–13 tratan los controles diarios (registro, cuentas, soportes, acceso de proveedores, registros, avisos, copias de seguridad, segmentación, IoT); los capítulos 14–17 tratan de detectar, notificar, recuperar y controlar los cambios; el capítulo 18 es el recorrido del proyecto final. Cada capítulo tiene resultados de aprendizaje, enseñanza, un ejemplo resuelto, un caso sintético etiquetado, errores y límites, cuatro ejercicios puntuados de 0 a 3, una síntesis y un bloque **Siga estudiando**. Los laboratorios de los capítulos 5, 9 y 11 solo leen datos locales (`python3 file.py`).

### Caso de estudio sintético

| Elemento | Función | Límite |
|---|---|---|
| **Harbor Point Food Packaging Line (HPFL)**: PLC de la llenadora PLC-FILL, PLC de la envolvedora PLC-WRAP, panel HMI-1, cámara de visión VIS-CAM, portátil de ingeniería ENG-LT, cortafuegos FW-1 | Línea estudiada a lo largo del libro | Inventada |
| **Tomás Reyes** | Técnico de mantenimiento en HPFL | Inventado |

### Fuentes principales

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [serie ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Lista completa en [Referencias](#references).

## Contenido

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](../../en/book/MANUSCRIPT.md#ch-07) · [8](../../en/book/MANUSCRIPT.md#ch-08) · [9](../../en/book/MANUSCRIPT.md#ch-09) · [10](../../en/book/MANUSCRIPT.md#ch-10) · [11](../../en/book/MANUSCRIPT.md#ch-11) · [12](../../en/book/MANUSCRIPT.md#ch-12) · [13](../../en/book/MANUSCRIPT.md#ch-13) · [14](../../en/book/MANUSCRIPT.md#ch-14) · [15](../../en/book/MANUSCRIPT.md#ch-15) · [16](../../en/book/MANUSCRIPT.md#ch-16) · [17](../../en/book/MANUSCRIPT.md#ch-17) · [18](../../en/book/MANUSCRIPT.md#ch-18) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Qué es la tecnología operacional en una línea de envasado

### Resultados de aprendizaje

Usted podrá (1) nombrar los principales componentes de TO de una línea de envasado de alimentos; (2) explicar por qué las prioridades de la TO difieren de las de la informática de oficina; y (3) describir qué puede fallar físicamente cuando un sistema de control se comporta mal.

### 1.1 La línea como sistema

Una línea de envasado convierte película, bandejas y producto en paquetes sellados y etiquetados. Los controladores lógicos programables (PLC) leen sensores y accionan motores, resistencias y válvulas muchas veces por segundo. Los paneles de operador, llamados interfaces hombre-máquina (HMI), muestran el estado de la línea y permiten a los operadores arrancarla, detenerla y ajustarla. Una cámara de visión rechaza los paquetes mal sellados. Un portátil de ingeniería guarda los programas y se usa para modificarlos. NIST SP 800-82r3 llama a toda esta familia tecnología operacional: sistemas que supervisan o controlan procesos físicos.

### 1.2 Por qué difieren las prioridades

En una oficina, perder la confidencialidad de una hoja de cálculo es el daño clásico. En una línea, las primeras preguntas son: ¿puede alguien resultar herido?, ¿será inseguro el alimento?, ¿se detendrá la línea? Una resistencia de sellado que se calienta demasiado puede quemar a un trabajador o dejar paquetes sin sellar y contaminados. Por eso aquí la disponibilidad y el comportamiento seguro van antes que la confidencialidad, y por eso nunca se reinicia un controlador «a ver qué pasa». En HPFL este orden condiciona las pequeñas decisiones. Tomás no desenchufa HMI-1 porque parezca extraño; primero pregunta al supervisor si es seguro detener la línea. Una solución que protege los datos pero deja la resistencia de sellado sin control sería la solución equivocada, por sensata que parezca en una oficina.

### 1.3 Qué puede cambiar un atacante o un error

Los mismos cambios pueden venir de la malicia o del error: un punto de consigna alterado, un programa sustituido, una HMI bloqueada, una red inundada de tráfico. MITRE ATT&CK for ICS recoge, por ejemplo, T0836 Modify Parameter. Su trabajo como técnico es advertir esos cambios, notificarlos y ayudar a restablecer la situación de forma segura, no investigar los dispositivos por su cuenta. Como el mismo cambio puede venir de cualquiera de los dos orígenes, Tomás anota qué cambió, cuándo y en qué dispositivo, sin decidir por qué. En HPFL, un cambio en la velocidad de la envolvedora podría ser un operador que despeja un atasco de pedidos o alguien que usa indebidamente una contraseña; el capítulo 9 muestra un caso en que fue lo primero. El informe es igual de útil en ambos casos.

### Ejemplo resuelto (HPFL sintética)

En su primer turno, Tomás Reyes recorre la línea con el supervisor y la dibuja: la llenadora PLC-FILL, la envolvedora PLC-WRAP, el panel HMI-1, la cámara de visión VIS-CAM y el portátil de ingeniería ENG-LT. Junto a cada recuadro escribe una frase sobre lo que ocurre físicamente si falla. La frase de la envolvedora dice: «la película se detiene, los paquetes se amontonan, riesgo de atasco en la alimentación».

> **Caso sintético — Harbor Point Food Packaging Line (HPFL).** La planta, Tomás Reyes y todos los números de este libro se han inventado con fines didácticos.

### Errores y límites

Un dibujo hecho en un solo recorrido es incompleto; es fácil pasar por alto paneles de reserva y dispositivos inalámbricos. Las consecuencias se valoran con el personal de operaciones, no en solitario.

### Ejercicios — capítulo 1

- **EX001 — Nombrar las partes.** Enumere cuatro componentes de TO de la línea HPFL y la función de cada uno. *Rúbrica:* 3 = cuatro componentes, cada uno con una función correcta; 2 = tres; 1 = solo los nombres; 0 = nada.
- **EX002 — Oficina frente a línea.** Explique en dos frases por qué «reinícialo y verás» es aceptable para un PC de oficina pero no para PLC-WRAP. *Rúbrica:* 3 = consecuencia física más argumento de estado seguro o de producción; 2 = un motivo; 1 = vago; 0 = nada.
- **EX003 — Consecuencia de la resistencia.** Describa dos daños si el punto de consigna de la resistencia de sellado se eleva muy por encima de lo normal. *Rúbrica:* 3 = riesgo de quemadura o incendio y paquetes inseguros o rechazados; 2 = uno; 1 = «se rompe»; 0 = nada.
- **EX004 — Una técnica de ATT&CK.** ¿Qué técnica de ATT&CK for ICS describe un punto de consigna modificado, y podría ese mismo cambio ser accidental? *Rúbrica:* 3 = T0836 Modify Parameter y sí, por error; 2 = solo la técnica; 1 = identificador incorrecto; 0 = nada.

### Síntesis del capítulo

La seguridad de la TO en una línea parte de la consecuencia física: las personas, los alimentos y la producción van primero.

### Siga estudiando — capítulo 01 de 18

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Primero la seguridad: permisos de trabajo, consecuencias y quién decide

### Resultados de aprendizaje

Usted podrá (1) explicar cómo protegen a las personas los permisos de trabajo y el bloqueo; (2) indicar quién tiene autoridad para detener o modificar la línea; y (3) aplicar la regla de que el trabajo de ciberseguridad nunca elude los controles de seguridad funcional.

### 2.1 Los sistemas de seguridad funcional no son herramientas de ciberseguridad

Las cortinas fotoeléctricas, las paradas de emergencia y los enclavamientos de las protecciones mantienen las manos lejos de las piezas en movimiento. Los diseñan y verifican ingenieros de seguridad funcional, y deben seguir funcionando pase lo que pase con la red. Un técnico de ciberseguridad nunca los desactiva, puentea ni reconfigura, ni siquiera «temporalmente, para hacer pruebas». En HPFL eso abarca las cortinas fotoeléctricas de la alimentación de la envolvedora, las paradas de emergencia a lo largo de la línea y los enclavamientos de las puertas de protección. Si una tarea de ciberseguridad parece exigir que se modifique alguno de ellos, la que está mal es la tarea, no el dispositivo de seguridad. Deténgase, pregunte al supervisor y deje constancia de la pregunta.

### 2.2 Permisos y bloqueo

El trabajo en una planta en marcha necesita un permiso: un registro escrito de quién hace qué, dónde y cuándo, qué peligros existen y cómo se controlan. El bloqueo y etiquetado aísla la energía antes de que nadie meta las manos en una máquina. Conectar un portátil al conmutador de la envolvedora también es trabajar en la planta: puede alterar el tráfico que ve el PLC, así que pasa por el mismo proceso de permisos. El permiso nombra a la persona responsable, la franja horaria y lo que se va a tocar. En HPFL, el permiso de Tomás para fotografiar el armario de la envolvedora decía que no se introducirían herramientas ni se haría ninguna conexión. Ponerlo por escrito lo protege a él además de a la línea, porque todos saben qué incluía la tarea y qué no.

### 2.3 Quién decide

El supervisor de turno decide si la línea funciona. El ingeniero de control es el responsable de los programas de los PLC. El responsable de calidad decide si el producto puede expedirse con seguridad. El personal de ciberseguridad asesora y notifica; no toma esas decisiones por su cuenta. Conocer esta cadena ahorra tiempo en un incidente, porque se llama primero a la persona adecuada. En HPFL eso significa que una duda de calidad va al responsable de calidad, una pregunta sobre la lógica de un PLC al ingeniero de control, y todo lo relativo a detener la línea al supervisor de turno. Tenga sus nombres y teléfonos en la hoja del emplazamiento. Si no sabe quién decide, pregunte primero al supervisor; sabrá a quién más hay que implicar.

### 2.4 Condiciones de parada

Cada tarea tiene condiciones de parada escritas: por ejemplo, detenerse si aparece cualquier alarma que no tenga explicación, si un operador pide que se detenga o si un dispositivo se comporta de forma distinta a lo previsto. Detenerse nunca es un fracaso. Escriba las condiciones de parada en el permiso antes de empezar y acuérdelas con el supervisor. Cuando se dé una, detenga el trabajo, deje la zona en condiciones seguras, avise al supervisor y anote lo ocurrido. La tarea puede reanudarse más tarde con un permiso nuevo o modificado. Seguir adelante porque el trabajo está casi terminado es como las pequeñas sorpresas se convierten en incidentes.

### Ejemplo resuelto (HPFL sintética)

Tomás necesita fotografiar las etiquetas del armario de la envolvedora para el inventario. Se lo pide al supervisor, que emite un permiso para las 10:00–10:20, durante un cambio de película planificado, anota «puerta del armario abierta, ninguna herramienta dentro, ninguna conexión» y nombra al electricista que abrirá el cuadro. Tomás hace las fotografías, el electricista cierra la puerta y el permiso se cierra con firma.

> **Caso sintético — HPFL.** El permiso y los horarios son inventados.

### Errores y límites

Los formularios de permiso varían de un emplazamiento a otro; siga el local. Un permiso no convierte en segura una tarea insegura; solo deja constancia de que se tuvieron en cuenta los peligros.

### Ejercicios — capítulo 2

- **EX005 — Petición sobre la cortina fotoeléctrica.** Un compañero propone puentear la cortina fotoeléctrica de la envolvedora mientras se prueba el tráfico de red. ¿Qué hace usted? *Rúbrica:* 3 = negarse, no tocar los sistemas de seguridad funcional, escalar al supervisor o al ingeniero de seguridad funcional; 2 = solo negarse; 1 = pedir permiso para puentear; 0 = aceptar.
- **EX006 — Por qué un portátil necesita permiso.** Dé un motivo técnico por el que conectar ENG-LT al conmutador de la línea necesita un permiso. *Rúbrica:* 3 = puede alterar el tráfico o las difusiones que ven los PLC o enviar cambios, lo que afecta al proceso; 2 = riesgo genérico; 1 = «lo dicen las normas»; 0 = nada.
- **EX007 — Asignar decisiones a personas.** ¿Quién decide (a) si la línea funciona, (b) si cambia un programa de PLC, (c) si se expide el producto? *Rúbrica:* 3 = supervisor, ingeniero de control, responsable de calidad; 2 = dos correctas; 1 = una; 0 = nada.
- **EX008 — Escribir condiciones de parada.** Escriba tres condiciones de parada para fotografiar las etiquetas de un armario. *Rúbrica:* 3 = tres condiciones concretas y observables; 2 = dos; 1 = vagas; 0 = nada.

### Síntesis del capítulo

Los controles de seguridad funcional son intocables, los permisos dejan constancia del trabajo y las decisiones operativas las toman personas con nombre.

### Siga estudiando — capítulo 02 de 18

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Nociones básicas de redes en la línea

### Resultados de aprendizaje

Usted podrá (1) leer una dirección IP y una máscara de subred; (2) explicar qué hacen los conmutadores, las VLAN y los cortafuegos en una red de planta; y (3) esbozar la red de HPFL a partir de una descripción.

### 3.1 Direcciones y subredes

Cada dispositivo en red tiene una dirección IP como 10.20.1.11. Una máscara /24 significa que los tres primeros números identifican la red y el último el dispositivo, de modo que 10.20.1.11 y 10.20.1.12 son vecinos en 10.20.1.0/24. Los dispositivos de la misma subred pueden comunicarse directamente; el tráfico hacia otra subred pasa por un enrutador o un cortafuegos. En HPFL los dispositivos de la línea comparten 10.20.1.0/24, así que PLC-FILL, PLC-WRAP, HMI-1 y VIS-CAM pueden alcanzarse directamente entre sí. Las oficinas están en 10.10.0.0/16, y el tráfico entre ambas debe atravesar FW-1. Saber esto le indica a Tomás que lo que decide si un PC de oficina puede alcanzar un PLC es una regla del cortafuegos.

### 3.2 Conmutadores y VLAN

Un conmutador conecta dispositivos mediante cables. Una VLAN divide un conmutador físico en redes lógicas separadas, de modo que los dispositivos de la línea y los PC de oficina pueden compartir hardware sin compartir tráfico. Un error en la configuración de una VLAN puede conectar sin que nadie lo note dos redes que debían estar separadas; por eso los cambios en los conmutadores requieren el mismo cuidado que los cambios en los PLC. En HPFL la línea está en la VLAN 20 y las oficinas en la VLAN 10. Si un puerto de un conmutador compartido se configurara con la VLAN equivocada, un PC de oficina conectado a él aterrizaría en la red de la línea sin pasar por FW-1. Comunique cualquier duda sobre la VLAN de un puerto al responsable de la red en lugar de probarlo.

### 3.3 Cortafuegos

Un cortafuegos reenvía o bloquea el tráfico entre redes según reglas: origen, destino, puerto y acción. En una planta, el cortafuegos importante es el que está entre la red de oficinas y la línea. Las buenas reglas nombran equipos y puertos concretos; las reglas «cualquiera a cualquiera» anulan su propósito. En HPFL, FW-1 debería permitir que ENG-LT alcance los PLC y poco más. Cada regla debería llevar un comentario que diga por qué existe y quién es su responsable. El capítulo 12 muestra cómo leer la tabla de FW-1 y qué hacer con una regla que no tiene responsable.

### 3.4 Conmutadores no gestionados e inalámbricos

Los pequeños conmutadores no gestionados dentro de los armarios y los puentes inalámbricos son habituales y a menudo faltan en los planos. Importan porque crean conexiones que nadie revisa. Búsquelos durante los recorridos por la planta: un conmutador pequeño dentro de un armario con más cables de los esperados, o un puente inalámbrico en un mástil. Fotografíe lo que encuentre y notifíquelo con su ubicación. Un dispositivo que une la red de la línea con otra red sin pasar por FW-1 hace que las reglas del cortafuegos sean irrelevantes para ese camino. Pregunte al responsable de la red si cada uno es conocido y está aprobado.

### 3.5 Direcciones que no debe dar por supuestas

Los dispositivos pueden tener una segunda tarjeta de red, un puerto serie o un módem celular que no aparecen en el plano. Pida al responsable todas las interfaces, no solo la dirección principal. Registre cada interfaz en el registro de activos, no solo la dirección IP principal. Un módem celular añadido por un fabricante de máquinas para el soporte remoto es un ejemplo habitual, y puede eludir FW-1 por completo. Si el responsable no sabe si un dispositivo tiene otras interfaces, consulte el manual o pregunte al proveedor antes de suponer que no las tiene.

### Ejemplo resuelto (HPFL sintética)

El ingeniero de control le explica a Tomás: los dispositivos de la línea usan 10.20.1.0/24 en la VLAN 20, las oficinas usan 10.10.0.0/16 en la VLAN 10, un cortafuegos FW-1 las une y solo ENG-LT puede alcanzar los PLC. Tomás dibuja dos recuadros, coloca PLC-FILL (10.20.1.11), PLC-WRAP (10.20.1.12), HMI-1 (10.20.1.21) y VIS-CAM (10.20.1.31) en el recuadro de la línea y escribe en FW-1 la única regla permitida.

> **Caso sintético — HPFL.** Las direcciones y los números de VLAN son inventados.

### Errores y límites

Un plano describe la intención; el cableado real puede ser distinto. Confírmelo con el responsable de la red contrastándolo con la configuración de los conmutadores, nunca sondeando los dispositivos.

### Ejercicios — capítulo 3

- **EX009 — ¿Misma subred?** ¿Están 10.20.1.31 y 10.20.2.31 en la misma red /24? Explíquelo. *Rúbrica:* 3 = no, el tercer octeto difiere, así que son redes /24 distintas; 2 = no, sin motivo; 1 = sí; 0 = nada.
- **EX010 — Error de VLAN.** ¿Qué podría ocurrir si el puerto de una impresora de oficina se configura por error en la VLAN 20? *Rúbrica:* 3 = la impresora se une a la red de la línea, elude FW-1 y crea un camino no revisado; 2 = solo «red equivocada»; 1 = la impresora deja de funcionar; 0 = nada.
- **EX011 — Calidad de las reglas.** Reescriba «any → 10.20.1.0/24 any allow» como una regla que se ajuste a la intención de HPFL. *Rúbrica:* 3 = origen solo la dirección de ENG-LT, destino los PLC, el puerto necesario, permitir, más denegación por defecto; 2 = regla específica por equipo sin denegación; 1 = sigue siendo amplia; 0 = nada.
- **EX012 — El conmutador oculto.** ¿Por qué importa para la seguridad un conmutador no gestionado encontrado en el armario de la envolvedora? *Rúbrica:* 3 = punto de conexión no revisado, sin registros ni control de VLAN, puede extender la red; 2 = un punto; 1 = «es viejo»; 0 = nada.

### Síntesis del capítulo

Las direcciones, las VLAN y las reglas del cortafuegos deciden quién puede comunicarse con un controlador; los errores en ellas abren caminos sin que nadie lo note.

### Siga estudiando — capítulo 03 de 18

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Protocolos industriales al nivel del operador

### Resultados de aprendizaje

Usted podrá (1) describir qué transportan Modbus/TCP y otros protocolos industriales similares; (2) explicar por qué muchos carecen de autenticación; y (3) distinguir, a partir de una descripción, el uso normal de un protocolo de un uso inusual.

### 4.1 Qué transportan los protocolos

Las HMI y los PLC intercambian valores: temperaturas, velocidades, recuentos, bits de arranque y parada. Modbus, publicado por la Modbus Organization, es un ejemplo muy extendido; sobre Ethernet se llama Modbus/TCP y normalmente usa el puerto 502. Una petición dice «lee los registros 100–110» o «escribe el valor 180 en el registro 205». Otras familias habituales son EtherNet/IP y PROFINET; la idea es similar. En HPFL, HMI-1 lee de PLC-FILL y PLC-WRAP valores como velocidades y temperaturas, y envía escrituras cuando los operadores pulsan botones. ENG-LT usa una conexión de programación aparte para modificar la lógica de los PLC. Saber qué conexiones son las esperadas es lo que permite a cualquiera advertir una inesperada.

### 4.2 Por qué falta la autenticación

El Modbus clásico no tiene ninguna forma integrada de comprobar quién envía una petición. Si un dispositivo puede alcanzar el PLC en el puerto 502, normalmente puede leer y a menudo escribir. Esto era aceptable cuando la red era un cable cerrado dentro de un armario. Deja de serlo en cuanto esa red se conecta con las oficinas o con internet, y por eso la segmentación (capítulo 12) tiene tanto peso. En HPFL esto significa que el cortafuegos y las VLAN son la principal protección de PLC-FILL y PLC-WRAP. Si un PC de oficina pudiera alcanzar el puerto 502 de cualquiera de los dos PLC, podría enviar escrituras idénticas a las de HMI-1. Notifique de inmediato cualquier indicio de un camino así, sin probarlo.

### 4.3 Patrones normales

En una línea sana, el patrón es aburrido: HMI-1 lee los mismos registros cada segundo y las escrituras se producen cuando los operadores pulsan botones. Un dispositivo nuevo que envía escrituras, o lecturas de rangos de registros inusuales, merece notificarse. No necesita descodificar paquetes usted mismo; necesita saber cómo es lo normal y a quién llamar. Dejar por escrito el patrón normal también ayuda tras los cambios. Si se añade un dispositivo nuevo a la línea, el patrón esperado se actualiza en el mismo ticket de cambio. Una herramienta de supervisión gestionada por el responsable de la red puede entonces comparar el tráfico real con el patrón escrito, como en la anotación del cuaderno de Tomás.

### 4.4 No experimente

Enviar peticiones de prueba a un PLC en funcionamiento puede cambiar sus salidas. El aprendizaje de protocolos se hace en un simulador o en un PLC de laboratorio, nunca en la línea. El ingeniero de control puede organizarle tiempo en un PLC de laboratorio o en un simulador si quiere practicar. Incluso las peticiones de lectura a un controlador en funcionamiento añaden carga y pueden perturbar los dispositivos más antiguos. Si siente curiosidad por lo que contiene un registro, pregunte al ingeniero en lugar de consultar el PLC de la línea. Aprender en un PLC de laboratorio le permite equivocarse con seguridad y ver los efectos sin riesgo.

### Ejemplo resuelto (HPFL sintética)

El ingeniero de control muestra a Tomás un resumen de la herramienta de supervisión de la línea: HMI-1 lee PLC-WRAP cada segundo; ENG-LT se conectó dos veces el mes pasado durante cambios aprobados. Tomás anota en su cuaderno como patrón esperado: «escrituras solo desde HMI-1 y ENG-LT».

> **Caso sintético — HPFL.** El resumen de supervisión es inventado.

### Errores y límites

Algunas versiones más recientes de los protocolos añaden funciones de seguridad, pero las plantas mantienen dispositivos antiguos durante décadas; suponga el caso habitual más débil salvo que el responsable confirme lo contrario.

### Ejercicios — capítulo 4

- **EX013 — Una petición de escritura.** En palabras sencillas, ¿qué hace «escribe 180 en el registro 205» en PLC-WRAP si el registro 205 es la velocidad de la envolvedora? *Rúbrica:* 3 = fija la velocidad en 180, cambio físico inmediato; 2 = cambia un valor; 1 = lee; 0 = nada.
- **EX014 — Puerto 502 alcanzable.** Una tableta de un proveedor conectada a la VLAN de la línea puede alcanzar el puerto 502 de PLC-FILL. ¿Por qué es preocupante? *Rúbrica:* 3 = sin autenticación, la tableta puede leer y escribir valores del proceso; 2 = «acceso no autorizado»; 1 = red lenta; 0 = nada.
- **EX015 — Detecte el inusual.** ¿Cuál es inusual: (a) HMI-1 leyendo cada segundo, (b) VIS-CAM escribiendo en PLC-WRAP, (c) ENG-LT durante un cambio aprobado? *Rúbrica:* 3 = (b) con motivo; 2 = solo (b); 1 = otro; 0 = nada.
- **EX016 — Aprender con seguridad.** ¿Dónde debería practicar Tomás el envío de peticiones Modbus y por qué no en la línea? *Rúbrica:* 3 = simulador o PLC de laboratorio; las peticiones cambian salidas reales; 2 = solo el lugar; 1 = «fuera de horario en la línea»; 0 = nada.

### Síntesis del capítulo

Los protocolos industriales transportan valores del proceso con poca o ninguna autenticación, así que poder alcanzar un dispositivo equivale a controlarlo.

### Siga estudiando — capítulo 04 de 18

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Mantener un registro de activos

### Resultados de aprendizaje

Usted podrá (1) enumerar los campos que necesita un registro de activos de TO útil; (2) encontrar huecos en un registro con un script breve; y (3) explicar por qué un registro incompleto retrasa la respuesta a incidentes.

### 5.1 Qué registrar

Para cada dispositivo: identificador, ubicación, zona o VLAN, responsable, marca y modelo, versión de firmware, dirección de red y lo que controla. NIST SP 800-82r3 trata el inventario como un fundamento porque todas las actividades posteriores (aplicación de parches, supervisión, respuesta a incidentes) dependen de saber qué existe. En HPFL el registro abarca PLC-FILL, PLC-WRAP, HMI-1, VIS-CAM y ENG-LT, y más adelante los sensores IoT. Cada campo responde a una pregunta que alguien hará con prisas: a quién llamar, qué firmware, qué dirección. Un campo vacío es un hallazgo que hay que corregir, no un blanco que tolerar.

### 5.2 De dónde salen los datos

Registros de compras, planos de los contratistas, etiquetas de los armarios, el proyecto del software de ingeniería y, a cargo del responsable de la red, la supervisión pasiva de la red. Cada fuente omite algo, así que se comparan entre sí.

```python
"""Lab 5: check a synthetic HPFL asset register for missing owner or firmware fields (no scanning)."""
reg = [
    {"id": "PLC-FILL", "zone": "line", "owner": "maintenance", "fw": "3.2"},
    {"id": "PLC-WRAP", "zone": "line", "owner": "maintenance", "fw": ""},
    {"id": "HMI-1", "zone": "line", "owner": "", "fw": "n/a"},
    {"id": "VIS-CAM", "zone": "line", "owner": "quality", "fw": "1.0.7"},
    {"id": "ENG-LT", "zone": "office", "owner": "controls", "fw": "n/a"},
]
for r in reg:
    gaps = [k for k in ("owner", "fw") if not r[k]]
    print(f"{r['id']:9} zone={r['zone']:7} {'OK' if not gaps else 'MISSING ' + ','.join(gaps)}")
print("complete:", sum(1 for r in reg if r["owner"] and r["fw"]), "of", len(reg))
```

Ejecútelo con `python3 lab_assets.py`. Salida verificada:

```text
PLC-FILL  zone=line    OK
PLC-WRAP  zone=line    MISSING fw
HMI-1     zone=line    MISSING owner
VIS-CAM   zone=line    OK
ENG-LT    zone=office  OK
complete: 3 of 5
```

En HPFL, Tomás usó fotografías de las etiquetas de los armarios para completar la versión de firmware que faltaba de PLC-WRAP. Cuando dos fuentes no coinciden, anote ambas y pregunte al responsable cuál es la correcta. Nunca rellene huecos sondeando dispositivos de la línea; la supervisión la hace solo el responsable de la red, de forma pasiva.

### 5.3 Leer el resultado

El script muestra qué registros están incompletos. PLC-WRAP no tiene firmware registrado, así que nadie puede saber si le afecta un aviso nuevo. HMI-1 no tiene responsable, así que no se llamaría a nadie si fallara. Tres de los cinco registros están completos; esa proporción es una medida sencilla que conviene seguir cada mes. La corrección de cada hueco es una pregunta a la persona adecuada. El firmware puede salir de la etiqueta de un armario o del software del ingeniero de control; la responsabilidad la indica el supervisor. Volver a ejecutar el script tras cada respuesta muestra el avance, como ocurrió cuando Tomás lo volvió a ejecutar y los cinco registros quedaron completos.

### 5.4 Mantenerlo vivo

Un registro solo es útil si se actualiza cuando las cosas cambian. Vincule las actualizaciones a los tickets de cambio: ningún dispositivo se instala, se traslada ni se sustituye sin que su entrada cambie en el mismo ticket. Añada una comprobación del registro a la plantilla de ticket de cambio para que no pueda omitirse. Una vez al mes, compare el registro con lo que ve la supervisión del responsable de la red y con un recorrido por los armarios. Cualquier dispositivo visto pero no registrado se notifica y se añade, o se retira si nadie sabe explicarlo.

### 5.5 Repuestos y dispositivos retirados

Los PLC de repuesto en una estantería y los dispositivos retirados del servicio también deben figurar en el registro, marcados como repuesto o retirado. Un repuesto cargado con un programa antiguo puede instalarse con prisas durante una avería, y una HMI retirada y tirada a un contenedor puede seguir guardando contraseñas y configuración de red. Antes de instalar un repuesto, compruebe que su programa coincide con la copia de seguridad verificada del dispositivo al que sustituye. Antes de que un dispositivo retirado salga del emplazamiento, bórrelo siguiendo las instrucciones del fabricante y deje constancia de que se hizo. Ambos pasos se anotan en la entrada del registro de ese dispositivo.

### Ejemplo resuelto (HPFL sintética)

Tomás usa las fotografías de los armarios del capítulo 2 para leer la etiqueta de firmware de PLC-WRAP: 2.0. Pregunta al supervisor quién es el responsable de HMI-1; la respuesta es «operaciones», y lo anota. Una nueva ejecución del script muestra ahora cinco de cinco completos.

> **Caso sintético — HPFL.** El registro y las etiquetas son inventados.

### Errores y límites

Las etiquetas pueden quedar desactualizadas tras una actualización de firmware; confírmelo en el software de ingeniería con el ingeniero de control. Un registro es información sensible: también es un mapa para los atacantes, así que guárdelo con control de acceso.

### Ejercicios — capítulo 5

- **EX017 — Campos que faltan.** Nombre dos campos que faltaban o podrían faltar en PLC-WRAP y que importan ante un aviso. *Rúbrica:* 3 = versión de firmware y modelo o marca; 2 = uno; 1 = color u otro dato sin relación; 0 = nada.
- **EX018 — Proporción tras las correcciones.** Si se completa el responsable de HMI-1 pero el firmware de PLC-WRAP sigue en blanco, ¿qué imprime la última línea? *Rúbrica:* 3 = `complete: 4 of 5`; 2 = 4 sin el formato; 1 = 5; 0 = nada.
- **EX019 — Vincular al cambio.** Proponga una regla que mantenga el registro al día. *Rúbrica:* 3 = todo ticket de instalación, traslado o sustitución debe actualizar el registro antes de cerrarse; 2 = solo revisión periódica; 1 = «tener cuidado»; 0 = nada.
- **EX020 — Proteger el registro.** Dé un motivo por el que el registro no debería estar en una carpeta compartida pública. *Rúbrica:* 3 = revela a los atacantes direcciones, versiones y objetivos; 2 = «confidencial»; 1 = es grande; 0 = nada.

### Síntesis del capítulo

Un registro completo, actualizado y protegido es la base sobre la que se apoya cualquier otra tarea de seguridad de TO.

### Siga estudiando — capítulo 05 de 18

[← Capítulo 04 (borrador)](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 (borrador) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Cuentas y contraseñas en las HMI y las herramientas de ingeniería

### Resultados de aprendizaje

Usted podrá (1) explicar los riesgos de las cuentas compartidas y predeterminadas; (2) aplicar prácticas sencillas de gestión de cuentas que funcionen en la planta durante el turno; y (3) gestionar correctamente una contraseña olvidada o filtrada.

### 6.1 Cuentas compartidas

Muchas HMI vienen con una única cuenta «operador» que usan todos los turnos. Entonces los registros dicen «lo hizo operador» y nadie sabe quién fue. Donde el sistema lo permita, dé a cada persona su propia cuenta; donde no, anote quién estaba de turno y haga que la contraseña compartida solo la conozca el equipo. En HPFL los operadores usaban la cuenta de administrador de HMI-1 para cambiar la velocidad de la envolvedora, como muestra el capítulo 9, lo que dificultó rastrear el cambio. Las cuentas nominativas, o al menos un registro de turno de quién tenía la contraseña compartida, habrían mostrado de inmediato a la persona.

### 6.2 Contraseñas predeterminadas

Las credenciales predeterminadas se publican en los manuales, así que cualquiera puede consultarlas. ETSI EN 303 645 convierte «ninguna contraseña predeterminada universal» en su primera disposición para la IoT de consumo, y la misma idea se aplica a los dispositivos de planta: cambie las predeterminadas antes de que un dispositivo entre en servicio. En HPFL, compruebe las credenciales predeterminadas de cada dispositivo nuevo antes de que se una a la red de la línea, incluidos la cámara de visión y los sensores IoT. Anote en el registro que se cambió la predeterminada y cuándo. Si un dispositivo no permite cambiarla, notifíquelo para que el responsable decida otros controles.

### 6.3 Cuentas con privilegios

Las cuentas de administrador de HMI-1 y del software de ingeniería pueden modificar pantallas, usuarios y lógica. Solo se usan para trabajos planificados, por personas con nombre, y su uso se revisa. No son el inicio de sesión de todos los días. En HPFL la contraseña de administrador de HMI-1 apareció en una nota adhesiva en el panel, lo que muestra lo rápido que se extiende el acceso privilegiado cuando se usa para tareas cotidianas. Revise con regularidad los inicios de sesión de administrador frente a los trabajos planificados y retire los derechos de administrador a quienes ya no los necesitan por su función.

### 6.4 Reglas prácticas

Use frases de contraseña largas pero que puedan teclearse con guantes; no escriba contraseñas en el panel; bloquee la pantalla o cierre la sesión al marcharse; nunca comparta una contraseña por radio ni por mensaje de texto. Estas reglas se adaptan a una planta donde la gente lleva guantes, comparte paneles y trabaja con prisas. Si una regla no puede cumplirse en la práctica, notifíquelo en lugar de ignorarla en silencio; el responsable puede encontrar una forma mejor, como un inicio de sesión con tarjeta identificativa. Repase las reglas con cada nuevo equipo de turno.

### 6.5 Cuando se filtra una contraseña

Notifíquelo; después, el responsable la cambia en un momento que no perturbe la línea. Revise los inicios de sesión recientes de esa cuenta (capítulo 9). En HPFL, cuando Tomás encontró la contraseña de administrador en una nota adhesiva, el ingeniero de control la cambió en la siguiente parada planificada y revisó el registro de inicios de sesión en busca de sesiones de administrador inesperadas. Recoja la filtración, el cambio y la revisión en un solo informe. Busque inicios de sesión a horas extrañas o desde lugares inesperados, y cambios de puntos de consigna que nadie sepa explicar. Avise al equipo de turno cuando la nueva contraseña esté en uso.

### Ejemplo resuelto (HPFL sintética)

Tomás ve en HMI-1 una nota adhesiva que dice «admin / Harbor2024». La fotografía como evidencia, la retira, avisa al supervisor y al ingeniero de control y redacta un informe breve. El ingeniero cambia la contraseña de administrador en la siguiente parada planificada y revisa el registro de inicios de sesión en busca de sesiones de administrador inesperadas.

> **Caso sintético — HPFL.** La nota y la contraseña son inventadas.

### Errores y límites

Algunas HMI antiguas no admiten cuentas individuales; compénselo con registros de turno y control físico. Cambiar una contraseña en un sistema en funcionamiento puede dejar fuera a los operadores si se hace sin cuidado.

### Ejercicios — capítulo 6

- **EX021 — Registros e inicios de sesión compartidos.** ¿Por qué un único inicio de sesión compartido «operador» debilita una investigación? *Rúbrica:* 3 = no se pueden atribuir las acciones a una persona; hacen falta registros de turno; 2 = «menos seguro»; 1 = vago; 0 = nada.
- **EX022 — Riesgo de las credenciales predeterminadas.** Explique por qué las contraseñas predeterminadas son peligrosas incluso en una línea aislada. *Rúbrica:* 3 = están publicadas, cualquiera con alcance físico o de red (contratista, portátil) puede iniciar sesión; el aislamiento es imperfecto; 2 = un punto; 1 = «hackers»; 0 = nada.
- **EX023 — La nota adhesiva.** Enumere por orden los pasos de Tomás tras encontrar la nota. *Rúbrica:* 3 = fotografiar, retirar, avisar al supervisor y al ingeniero, cambio de contraseña en una parada planificada, revisión de registros; 2 = la mayoría; 1 = solo retirarla; 0 = nada.
- **EX024 — Elección del inicio de sesión diario.** ¿Debería el ingeniero de control usar la cuenta de administrador para la supervisión rutinaria? ¿Por qué? *Rúbrica:* 3 = no; mínimo privilegio, reduce los cambios accidentales y el uso indebido; 2 = solo no; 1 = sí; 0 = nada.

### Síntesis del capítulo

Las cuentas nominativas, las credenciales predeterminadas cambiadas y el uso limitado de la cuenta de administrador hacen que las acciones sean rastreables y más difíciles de aprovechar indebidamente.

### Siga estudiando — capítulo 06 de 18

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](../../en/book/MANUSCRIPT.md#ch-07)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo para EX001–EX072. Harbor Point Food Packaging Line, Tomás Reyes y todas las cifras son sintéticos. Cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación.

**EX001.** PLC-FILL controla la llenadora; PLC-WRAP acciona los motores y las resistencias de la envolvedora; HMI-1 muestra el estado y recibe las órdenes del operador; VIS-CAM inspecciona los sellados y rechaza los paquetes defectuosos; ENG-LT guarda y modifica los programas de los PLC.

**EX002.** Reiniciar un PC de oficina hace perder, como mucho, el trabajo no guardado, mientras que reiniciar PLC-WRAP detiene motores y resistencias a mitad de ciclo, puede atascar la película o dejar el producto en condiciones inseguras, y debe seguir el procedimiento de parada de la línea con el acuerdo de operaciones.

**EX003.** Una temperatura de sellado mucho más alta puede chamuscar la película, provocar un incendio o quemar a un trabajador que despeja un atasco, y puede producir paquetes dañados o mal sellados que deben rechazarse por riesgo para la seguridad alimentaria.

**EX004.** T0836 Modify Parameter; sí: un operador que teclea mal un valor causa el mismo efecto físico, y por eso los cambios se registran y se comprueban sea cual sea su causa.

**EX005.** Negarse y detener el plan: la cortina fotoeléctrica es una función de seguridad que nunca debe eludirse para un trabajo de ciberseguridad; comunique la propuesta al supervisor y busque un método de prueba que no toque la seguridad funcional, como observar desde un puerto espejo durante una parada planificada.

**EX006.** Un portátil conectado puede enviar difusiones, solicitar direcciones o ejecutar software que envíe tráfico a PLC-WRAP, lo que puede ralentizar su comunicación o cambiar su lógica; el proceso podría verse afectado, así que el trabajo debe planificarse y autorizarse.

**EX007.** (a) El supervisor de turno; (b) el ingeniero de control responsable de los programas de los PLC; (c) el responsable de calidad.

**EX008.** Detenerse si el supervisor o un operador lo pide; detenerse si queda expuesto algún conductor en tensión o pieza en movimiento más allá de la vista acordada; detenerse si aparece en HMI-1 una alarma sin explicación mientras la puerta está abierta.

**EX009.** No. Con una máscara /24, los tres primeros octetos son la red; 10.20.1 y 10.20.2 difieren, así que el tráfico entre ellas debe pasar por un enrutador o un cortafuegos.

**EX010.** La impresora quedaría en la VLAN de la línea con acceso directo a los PLC y a HMI-1, eludiendo las reglas de FW-1; cualquier compromiso de la impresora, o los usuarios de oficina que imprimen en ella, crearían un camino que nadie ha revisado.

**EX011.** «ENG-LT (su dirección de oficina) → PLC-FILL y PLC-WRAP solo en el puerto de programación, permitir», seguida de «cualquiera → 10.20.1.0/24, denegar», para que nada más de la oficina alcance la línea.

**EX012.** Cualquiera con un cable puede unirse a través de él a la red de la línea, no tiene VLAN ni registros y puede enlazar el armario con dispositivos que no figuran en ningún plano, así que crea conexiones que nadie revisa.

**EX013.** Fija de inmediato el valor de velocidad de la envolvedora en 180; el motor acelera sin ninguna confirmación adicional, lo que puede provocar atascos o una tensión de película insegura.

**EX014.** El Modbus clásico no comprueba la identidad, así que cualquier cosa que alcance el puerto 502 puede leer y posiblemente escribir valores de PLC-FILL; una tableta de proveedor no gestionada podría modificar la llenadora por error o si estuviera comprometida.

**EX015.** (b) VIS-CAM escribiendo en PLC-WRAP: la cámara solo debería enviar señales de rechazo por su camino definido, y una escritura suya queda fuera del patrón esperado de HMI-1 y ENG-LT.

**EX016.** En un simulador de protocolos o en un PLC de laboratorio en un banco aislado, porque cualquier petición a la línea puede cambiar salidas reales y detener o poner en peligro la producción.

**EX017.** La versión de firmware (para cotejarla con los avisos) y la marca y el modelo exactos (los avisos nombran productos concretos); sin ellos no se puede decidir si PLC-WRAP está afectado.

**EX018.** `complete: 4 of 5`: HMI-1 pasa a `OK`, pero PLC-WRAP sigue mostrando `MISSING fw`.

**EX019.** Un ticket de cambio que instala, traslada o sustituye un dispositivo no puede cerrarse hasta que se actualiza la entrada del registro de activos y se anota en el ticket el nombre de quien la actualizó.

**EX020.** Enumera la dirección, el modelo y el firmware de cada dispositivo, lo que indica a un atacante exactamente qué objetivos existen y qué debilidades conocidas probar.

**EX021.** Todas las acciones aparecen bajo un mismo nombre, así que el registro no puede mostrar qué persona cambió un punto de consigna; los investigadores deben reconstruirlo a partir de los cuadrantes de turno y de la memoria, lo que es lento y poco fiable.

**EX022.** Las contraseñas predeterminadas están en manuales públicos, y las líneas «aisladas» siguen recibiendo portátiles de contratistas, dispositivos USB y enlaces remotos; cualquiera con algún tipo de alcance puede iniciar sesión sin ningún esfuerzo.

**EX023.** Fotografiar la nota como evidencia, retirarla, avisar al supervisor y al ingeniero de control y redactar un informe breve; el ingeniero cambia la contraseña en una parada planificada y revisa los inicios de sesión de administrador recientes.

**EX024.** No. La supervisión rutinaria solo necesita derechos de visualización; usar la cuenta de administrador a diario hace más probables los cambios accidentales y los daños por robo de sesión, así que se reserva para los trabajos planificados.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; vuelva a verificar las ediciones antes de citarlas. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA. Cybersecurity advisories index (ICS advisories). <https://www.cisa.gov/news-events/cybersecurity-advisories>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- ISA/IEC 62443 series of standards (overview; zones and conduits from 62443-3-2, component requirements in 62443-4-2). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS: T0836 Modify Parameter, T0843 Program Download, T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- Modbus Organization. Modbus specifications. <https://www.modbus.org/modbus-specifications>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
