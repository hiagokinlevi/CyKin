# Seguridad de TO, IoT y sistemas ciberfísicos: cuaderno de trabajo del operador técnico

- Idioma: español neutro (`es`); curso técnico, dieciocho meses; aproximadamente 1.200 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Los capítulos 1–18 de 18 tienen texto didáctico escrito a mano; los ejercicios EX001–EX072 tienen sus resultados resueltos correspondientes; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas se incluyen a partir de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

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

Los dispositivos pueden tener una segunda tarjeta de red, un puerto serie o un módem celular que no aparecen en el plano. Pida al responsable todas las interfaces, no solo la dirección principal. Registre cada una en el registro de activos. Un módem celular añadido por un fabricante de máquinas para el soporte remoto es un ejemplo habitual, y puede eludir FW-1 por completo. Si el responsable no sabe si un dispositivo tiene otras interfaces, consulte el manual o pregunte al proveedor antes de suponer que no las tiene.

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

Tomás ve en HMI-1 una nota adhesiva que dice «admin / Harbor2024». La fotografía como evidencia, la retira, avisa al supervisor y al ingeniero de control y redacta un informe breve.

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

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Soportes extraíbles y portátiles

### Resultados de aprendizaje

Usted podrá (1) explicar cómo las memorias USB y los portátiles introducen malware en las plantas; (2) aplicar una rutina de análisis y registro para los soportes; y (3) decidir qué portátiles pueden conectarse a la línea.

### 7.1 Cómo cruza el malware el aislamiento

Las líneas sin conexión a internet siguen recibiendo archivos: actualizaciones de firmware, archivos de recetas, herramientas de proveedores y fotografías. Cada uno llega en una memoria USB o en un portátil que ha estado en otros sitios. NIST SP 800-82r3 señala los soportes extraíbles como una vía habitual de entrada a la TO, y hay incidentes muy conocidos que se propagaron exactamente así. En HPFL, que un proveedor llegue con un archivo de receta en una memoria personal es algo rutinario. El archivo puede ser inofensivo, pero la memoria ha estado en otras plantas y oficinas. Trate cada archivo que entra en la línea como sujeto a la misma rutina, por fiable que sea su origen.

### 7.2 Una rutina para los soportes

Use solo memorias proporcionadas por el emplazamiento. Antes de que una memoria llegue a un dispositivo de la línea, analícela en una estación de análisis dedicada y actualizada situada fuera de la línea, anote en un registro el número de la memoria, los nombres de los archivos, el resultado del análisis y la persona, y mantenga la memoria bajo control hasta que se use. Las memorias desconocidas encontradas en el suelo se entregan a seguridad; nunca se conectan «para ver de quién son».

En HPFL la estación de análisis está fuera de la línea y las memorias del emplazamiento están numeradas, por ejemplo HP-07. El registro permite a cualquiera rastrear un archivo hasta su origen si más adelante aparece un problema. Revise el registro durante los recorridos; una memoria que no figura en él es un hallazgo.

### 7.3 Portátiles

Solo ENG-LT y los portátiles de proveedores aprobados se conectan a los equipos de la línea. Un portátil aprobado tiene los parches al día, ejecuta antimalware, no tiene software personal y se revisa antes de cada visita. Si el portátil de un proveedor no puede cumplir esa norma, se usa en su lugar un portátil del emplazamiento con las herramientas del proveedor instaladas. Mantenga en el registro una lista de los portátiles aprobados con su responsable y la fecha de la última revisión de cada uno. En HPFL, ENG-LT es el único portátil del emplazamiento autorizado para programar los PLC. Un portátil cuya última revisión sea anterior a la visita se revisa de nuevo antes de conectarse.

### 7.4 Transferir archivos sin USB

Algunos emplazamientos mueven los archivos mediante un servidor de transferencia controlado en la DMZ en lugar de memorias. Así queda constancia de cada archivo y desaparece por completo la necesidad de conectar soportes a los dispositivos de la línea. En HPFL la DMZ ya alberga un servidor de transferencia de archivos. Los archivos que llegan a él pueden analizarse automáticamente y registrarse con el remitente y la hora, y los dispositivos de la línea los recogen a través de un conducto documentado. Sacar las memorias de la rutina también elimina el riesgo de que una se pierda en la planta.

### Ejemplo resuelto (HPFL sintética)

Un proveedor llega con un archivo de receta en una memoria personal. Tomás lleva la memoria a la estación de análisis, copia el archivo en la memoria del emplazamiento HP-07 tras un análisis limpio, anota «HP-07, recipe_v12.csv, limpio, Tomás, 09:30» y entrega HP-07 al ingeniero de control. La memoria personal vuelve al proveedor sin haberse conectado a nada de la línea.

> **Caso sintético — HPFL.** El proveedor, los números de las memorias y el archivo son inventados.

### Errores y límites

Un análisis limpio solo significa que no se encontró malware conocido; un malware nuevo puede pasar. Mantenga la rutina de todos modos: reduce la mayor parte del riesgo y deja constancia si algo sale mal.

### Ejercicios — capítulo 7

- **EX025 — Encontrada en el suelo.** Junto a HMI-1 hay una memoria USB etiquetada «Nóminas 2026». ¿Qué hace usted? *Rúbrica:* 3 = no conectarla; entregarla a seguridad o al supervisor; anotar dónde se encontró; 2 = solo entregarla; 1 = revisarla en un PC de oficina; 0 = conectarla a la HMI.
- **EX026 — Campos del registro de soportes.** Enumere cuatro campos del registro de soportes. *Rúbrica:* 3 = identificador de la memoria, archivos, resultado del análisis, persona y hora; 2 = tres; 1 = uno; 0 = nada.
- **EX027 — Qué significa un análisis limpio.** Un compañero dice: «el análisis salió limpio, así que el archivo es seguro». Corrija la afirmación. *Rúbrica:* 3 = solo que no se encontró malware conocido; son posibles amenazas nuevas; la rutina sigue reduciendo el riesgo; 2 = parcial; 1 = estar de acuerdo; 0 = nada.
- **EX028 — Rechazo del portátil del proveedor.** El portátil del proveedor no tiene antimalware. ¿Qué alternativa permite seguir con el trabajo? *Rúbrica:* 3 = portátil del emplazamiento con las herramientas del proveedor, o transferir los archivos por la estación de análisis; 2 = solo reprogramar; 1 = permitirlo igualmente; 0 = nada.

### Síntesis del capítulo

Todo archivo que entra en la línea sigue un camino analizado, registrado y controlado; los soportes desconocidos nunca tocan los dispositivos de la línea.

### Siga estudiando — capítulo 07 de 18

[← Capítulo 06 (borrador)](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 (borrador) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Acceso remoto de los proveedores

### Resultados de aprendizaje

Usted podrá (1) describir cómo acceden los proveedores a distancia a los sistemas de la planta; (2) explicar las lecciones del aviso de 2021 sobre la planta de agua de Oldsmar; y (3) llevar una sesión remota siguiendo una lista de comprobación sencilla.

### 8.1 Por qué se conectan los proveedores

Los fabricantes de máquinas dan soporte remoto a sus equipos para diagnosticar averías sin desplazarse. Es útil, pero un enlace permanente y siempre activo hacia la línea es también una entrada permanente para cualquiera que robe las credenciales. En HPFL, el fabricante de la envolvedora necesita de vez en cuando leer los registros de averías. Esa necesidad es real, y rechazar todo acceso remoto supondría esperar días a una visita. La respuesta es permitir el acceso solo por una ruta controlada, para un trabajo concreto y bajo la vigilancia del emplazamiento.

### 8.2 Qué encontró el aviso

El aviso de CISA AA21-042A describe el compromiso de una instalación de tratamiento de agua de EE. UU. en 2021 en el que se usó software de acceso remoto para llegar a un sistema de control. Sus recomendaciones incluyen usar autenticación multifactor, contraseñas robustas para el escritorio remoto, cerrar los puertos de escritorio remoto que no se usen y auditar las conexiones remotas. Esos puntos se aplican directamente a una línea de envasado. En HPFL eso significa comprobar que no se ejecuta software de escritorio remoto directamente en HMI-1 ni en ENG-LT, que las cuentas de los proveedores usan autenticación multifactor y que las sesiones remotas se registran y se revisan. La reunión de lecciones aprendidas del capítulo 16 encontró más tarde un puerto de escritorio remoto en HMI-1 abierto por un contratista, justo el tipo de ruta contra el que advierte el aviso.

### 8.3 Un patrón más seguro

El acceso remoto pasa por una única pasarela controlada por el emplazamiento en la DMZ, nunca por software instalado directamente en las HMI. Cada proveedor tiene una cuenta nominativa con autenticación multifactor. La conexión está desactivada por defecto y se activa para la ventana de una sesión con ticket. Alguien del emplazamiento vigila la sesión y puede terminarla. Las sesiones se registran y se revisan. Recoja el patrón en un procedimiento breve que los proveedores reciban antes de su primera sesión. El supervisor abre un ticket con una franja horaria; el técnico activa la cuenta y vigila. Si un proveedor pide acceso permanente, la petición va al supervisor y normalmente se rechaza.

### 8.4 Terminar la sesión

Cuando termina el trabajo, la cuenta se vuelve a desactivar, se deja constancia del cambio y el operador confirma que la línea se comporta con normalidad. Una sesión que se deja activada «para la próxima vez» es el fallo más común. En HPFL, Tomás desactivó la cuenta del proveedor a las 14:38, antes de que se cerrara la ventana, y anotó en el ticket las horas de inicio y fin. Revise las cuentas de proveedores cada semana para confirmar que ninguna se ha quedado activada. Una cuenta encontrada activada fuera de un ticket se notifica como hallazgo. Confirme también que el cambio del proveedor figura en el registro.

### Ejemplo resuelto (HPFL sintética)

El fabricante de la envolvedora necesita leer un registro de averías. El supervisor abre el ticket 4471 para las 14:00–14:45. Tomás activa la cuenta del proveedor en la pasarela, vigila la pantalla compartida, ve que el ingeniero solo abre el visor de averías y desactiva la cuenta a las 14:38.

> **Caso sintético — HPFL.** El ticket, el proveedor y los horarios son inventados.

### Errores y límites

Algunas máquinas llegan con módems celulares integrados para el soporte del proveedor; eluden por completo la pasarela y hay que localizarlos y controlarlos. Vigilar una sesión no permite detectarlo todo; el registro y la revisión añaden una segunda comprobación.

### Ejercicios — capítulo 8

- **EX029 — Recomendaciones del aviso.** Nombre tres recomendaciones de AA21-042A. *Rúbrica:* 3 = tres entre MFA, contraseñas robustas de RDP, cerrar los puertos RDP sin uso, auditar las conexiones remotas; 2 = dos; 1 = una; 0 = nada.
- **EX030 — Enlace siempre activo.** Explique por qué «el enlace del proveedor está siempre activo para que el soporte sea más rápido» es un riesgo. *Rúbrica:* 3 = entrada permanente para credenciales robadas, uso sin vigilancia; 2 = riesgo vago; 1 = estar de acuerdo; 0 = nada.
- **EX031 — Registro de la sesión.** ¿Qué debería escribir Tomás en el ticket 4471 tras la sesión? *Rúbrica:* 3 = nombre o cuenta del proveedor, inicio y fin, qué se hizo, cuenta desactivada, línea normal; 2 = parte; 1 = «hecho»; 0 = nada.
- **EX032 — El módem oculto.** Durante un recorrido por la planta, Tomás encuentra un módem celular en el armario de la llenadora. ¿Por qué es importante? *Rúbrica:* 3 = elude la pasarela, la MFA y el registro; camino no gestionado; notificarlo al responsable; 2 = uno; 1 = retirarlo él mismo; 0 = nada.

### Síntesis del capítulo

El acceso de los proveedores pasa por una sola pasarela, con cuentas nominativas y multifactor, activadas solo durante ventanas vigiladas y registradas.

### Siga estudiando — capítulo 08 de 18

[← Capítulo 07 (borrador)](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 (borrador) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Leer registros y alarmas

### Resultados de aprendizaje

Usted podrá (1) distinguir las alarmas de proceso de los eventos relevantes para la seguridad; (2) filtrar un registro con un script breve; y (3) decidir cuándo un patrón exige escalarlo.

### 9.1 Dos tipos de mensajes

Las HMI y los PLC notifican alarmas de proceso, como falta de película o un atasco. También registran inicios de sesión, cambios de configuración y descargas de programas. Las alarmas de proceso las gestionan los operadores; el segundo tipo le dice quién hizo qué al sistema, y ahí es donde suelen aparecer las pistas de seguridad. Los inicios de sesión, los cambios de puntos de consigna y las descargas de programas son los registros que hay que exportar y conservar. Separar ambos tipos mantiene la revisión de seguridad lo bastante breve como para hacerla todos los días. Los operadores siguen avisando al supervisor de un patrón extraño de alarmas de proceso, porque puede ser la primera señal visible de un problema de seguridad.

### 9.2 Patrones que importan

Varios inicios de sesión fallidos seguidos de uno correcto pueden significar que alguien adivinó una contraseña. Un punto de consigna cambiado fuera de un trabajo planificado, una descarga de programa que nadie esperaba o un inicio de sesión de administrador a una hora extraña merecen una revisión. Un evento aislado suele ser inocente; lo que importa es la secuencia.

```python
"""Lab 9: filter a synthetic HMI event log for security-relevant entries."""
log = """06:02 HMI-1 login operator1 ok
06:15 PLC-FILL alarm low-film
07:40 HMI-1 login admin fail
07:41 HMI-1 login admin fail
07:41 HMI-1 login admin fail
07:43 HMI-1 login admin ok
07:45 PLC-WRAP setpoint speed 120->180 by admin
08:10 PLC-FILL alarm jam-cleared"""
fails = 0
for line in log.splitlines():
    t, dev, kind, *rest = line.split()
    if kind == "login" and rest[-1] == "fail":
        fails += 1
    if kind == "setpoint" or (kind == "login" and rest[0] == "admin" and rest[-1] == "ok"):
        print("REVIEW", line)
print("failed logins:", fails)
```

Ejecútelo con `python3 lab_logs.py`. Salida verificada:

```text
REVIEW 07:43 HMI-1 login admin ok
REVIEW 07:45 PLC-WRAP setpoint speed 120->180 by admin
failed logins: 3
```

En HPFL el laboratorio muestra exactamente este tipo de secuencia: tres inicios de sesión de administrador fallidos, uno correcto y, dos minutos después, un cambio de velocidad. Cada evento por separado podría pasarse por alto. Juntos plantean una pregunta que necesita respuesta del supervisor.

### 9.3 Leer la salida

El script cuenta tres inicios de sesión de administrador fallidos y después muestra un inicio de sesión de administrador correcto a las 07:43 y un cambio de velocidad de la envolvedora de 120 a 180 dos minutos después. En conjunto es una historia que merece comprobarse: ¿había un cambio planificado a las 07:45 y quién tenía la sesión iniciada? El script no explica lo que ocurrió; solo selecciona las líneas sobre las que conviene preguntar. El paso siguiente es comprobar si había un cambio planificado y quién estaba de turno. En HPFL la respuesta resultó ser inocente, pero aun así la secuencia merecía comprobarse.

### 9.4 Escale, no investigue solo

El trabajo de Tomás es advertir y notificar con evidencia: las líneas del registro, la hora y lo que hizo la línea. El ingeniero de control y el responsable de seguridad deciden lo que ocurre después. Notifique adjuntando las líneas del registro, la hora en que las advirtió y lo que estaba haciendo la línea en ese momento. No inicie sesión en los dispositivos para indagar más ni cambie contraseñas por su cuenta. Si el ingeniero de control pide más evidencia, le dirá qué recoger y cómo. Guarde una copia de lo que notificó y de cuándo lo envió.

### 9.5 La hora importa

Los registros solo son comparables si los relojes de los dispositivos coinciden. Indique en su informe cualquier diferencia de reloj que conozca. Si HMI-1 y PLC-WRAP difieren en varios minutos, un cambio de punto de consigna podría parecer anterior al inicio de sesión que lo causó. Pregunte al ingeniero de control cómo se ajustan los relojes en la línea y anote en el registro de activos cualquier desfase conocido. Al exportar registros, anote la hora de su reloj y la hora que muestra cada dispositivo, para poder corregir la diferencia más tarde. Un reloj que deriva varios minutos puede hacer que una secuencia inocente parezca sospechosa, u ocultar una sospechosa.

### Ejemplo resuelto (HPFL sintética)

Tomás pregunta al supervisor; no había ningún cambio planificado. El operador del turno de noche explica que olvidó la contraseña de administrador, lo intentó tres veces, luego la recordó y subió la velocidad para recuperar un retraso en la producción. El cambio se revierte, se deja constancia de él y se retira a los operadores el uso de la cuenta de administrador para cambiar la velocidad.

> **Caso sintético — HPFL.** El registro y la explicación son inventados.

### Errores y límites

Los registros de los dispositivos pequeños son cortos y pueden sobrescribirse en pocos días, así que expórtelos con regularidad. Una explicación inocente también debe quedar registrada.

### Ejercicios — capítulo 9

- **EX033 — Clasificar las entradas.** ¿Qué líneas del registro del laboratorio son alarmas de proceso y cuáles son relevantes para la seguridad? *Rúbrica:* 3 = `low-film` y `jam-cleared` son de proceso; los inicios de sesión y el punto de consigna, de seguridad; 2 = la mayoría; 1 = una; 0 = nada.
- **EX034 — Cinco fallos.** Si se añaden dos líneas más de administrador fallidas antes de las 07:43, ¿qué imprime la última línea? *Rúbrica:* 3 = `failed logins: 5`; 2 = 5; 1 = 3; 0 = nada.
- **EX035 — Por qué importa la secuencia.** Explique por qué el inicio de sesión de las 07:43 importa más tras los fallos que por sí solo. *Rúbrica:* 3 = un acierto tras varios fallos sugiere que se adivinó la contraseña; ligado al cambio de punto de consigna; 2 = un punto; 1 = «es administrador»; 0 = nada.
- **EX036 — Contenido del informe.** Escriba los cuatro hechos que incluye Tomás al notificar el cambio de las 07:45. *Rúbrica:* 3 = hora, dispositivo, valores del cambio, cuenta y secuencia de inicios de sesión (más el efecto en la línea); 2 = tres; 1 = uno; 0 = nada.

### Síntesis del capítulo

Las pistas de seguridad están en los registros de inicios de sesión y de cambios; son las secuencias, no las líneas sueltas, las que justifican escalar.

### Siga estudiando — capítulo 09 de 18

[← Capítulo 08 (borrador)](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 (borrador) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Parches y avisos de seguridad

### Resultados de aprendizaje

Usted podrá (1) leer un aviso de ICS y encontrar los datos que importan; (2) cotejar un aviso con el registro de activos; y (3) explicar por qué las plantas suelen mitigar antes de aplicar el parche.

### 10.1 De dónde vienen los avisos

Los fabricantes y CISA publican avisos sobre productos industriales; el índice de CISA los enumera con los nombres de los productos, las versiones afectadas, el impacto y las mitigaciones. Un aviso es el punto de partida, no la decisión. En HPFL, el ingeniero de control y Tomás revisan los avisos de los fabricantes de PLC-FILL, PLC-WRAP, HMI-1 y VIS-CAM. Cotejar cada uno con el registro les indica rápidamente si hace falta alguna acción, y los campos de firmware del registro son los que lo hacen posible. Anote en el expediente de dónde procede cada aviso, cuándo se leyó y si se ha revisado después.

### 10.2 Leer un aviso

Busque cinco datos: producto y modelo, versiones afectadas, qué podría hacer un atacante, si necesita acceso de red o físico, y la corrección o solución provisional del fabricante. Después consulte el registro: ¿tenemos ese modelo, con esa versión, alcanzable de esa manera? En HPFL, el aviso que afectaba a PLC-WRAP requería acceso de red a su puerto de programación, y FW-1 ya solo lo permitía desde ENG-LT. Responder a las cinco preguntas lo dejó claro en pocos minutos. Anote las respuestas en el expediente del aviso, incluso cuando el resultado sea que no hace falta ninguna acción.

### 10.3 Por qué no aplicar el parche de inmediato

Una actualización de firmware en un PLC lo detiene, puede cambiar su comportamiento y necesita probarse con el programa. Las plantas de alimentación necesitan además controles de calidad tras los cambios. Por eso el orden habitual es: confirmar la exposición, aplicar rápidamente una mitigación (por ejemplo, bloquear el servicio vulnerable en el cortafuegos) y después programar el parche para una parada planificada con un plan de vuelta atrás. En HPFL la mitigación para PLC-WRAP ya estaba aplicada en FW-1, y el parche se programó para una parada planificada tres semanas después. El plan de vuelta atrás debería nombrar el programa guardado y la versión de firmware a la que volver si la actualización causa problemas.

### 10.4 Dejar constancia de la decisión

Cada aviso tiene un expediente: si se aplica o no, por qué, la mitigación, la fecha prevista del parche y el responsable. Decidir no aplicar el parche, con los motivos y una fecha de revisión, sigue siendo una decisión. Guarde los expedientes en un solo lugar, vinculados al registro, para que un lector posterior pueda ver qué avisos se consideraron y por qué. Revise los asuntos abiertos cada mes. Un expediente sin fecha de revisión tiende a olvidarse. En HPFL el expediente del aviso de PLC-WRAP nombraba como mitigación la regla ya existente de FW-1 e indicaba la fecha de la parada planificada para el parche. Cuando se aplica el parche, el expediente se cierra con la nueva versión de firmware.

### 10.5 Actualizaciones de las HMI y los portátiles

Las HMI basadas en Windows y ENG-LT también necesitan actualizaciones del sistema operativo, pero solo las que haya aprobado el fabricante de la HMI, instaladas durante paradas planificadas. Pregunte al fabricante de la HMI qué actualizaciones están aprobadas y anote cada una en el registro y en el ticket de cambio. Tras actualizar, compruebe que las pantallas muestran valores correctos y que HMI-1 sigue comunicándose con ambos PLC. Las actualizaciones de ENG-LT siguen el mismo enfoque planificado. Conserve la imagen anterior o un punto de restauración para poder deshacer la actualización si fallan las pantallas o la comunicación. Nunca deje que una HMI se actualice sola desde internet; eso exigiría una conexión que la línea no debería tener.

### Ejemplo resuelto (HPFL sintética)

Un aviso sintético indica que el firmware 2.0 del modelo de PLC de la envolvedora permite cambios de programa sin autenticación a través de la red. El registro (tras el capítulo 5) dice que PLC-WRAP ejecuta la versión 2.0. El ingeniero de control confirma que FW-1 ya bloquea el puerto de programación para todo salvo ENG-LT, lo anota como mitigación y programa el firmware 2.3 para la siguiente parada planificada, dentro de tres semanas.

> **Caso sintético — HPFL.** El aviso y las versiones son inventados; los avisos reales están en cisa.gov.

### Errores y límites

Los avisos pueden revisarse; vuelva a comprobarlos antes de actuar. Las cadenas de versión pueden indicarse de forma distinta en las etiquetas y en el software.

### Ejercicios — capítulo 10

- **EX037 — Cinco datos.** Enumere los cinco datos que hay que extraer de un aviso. *Rúbrica:* 3 = producto y modelo, versiones, impacto, acceso necesario, corrección o solución provisional; 2 = cuatro; 1 = dos; 0 = nada.
- **EX038 — ¿Se aplica?** Un aviso afecta a las versiones anteriores a la 2.2 del modelo de PLC-FILL; PLC-FILL ejecuta la 3.2. ¿Se aplica? *Rúbrica:* 3 = no, la 3.2 es posterior; anotarlo como no aplicable con el motivo; 2 = no; 1 = sí; 0 = nada.
- **EX039 — Mitigar primero.** ¿Por qué mitiga el ingeniero en FW-1 antes de aplicar el parche a PLC-WRAP? *Rúbrica:* 3 = el parche exige parada, pruebas y control de calidad; el cortafuegos reduce ya la exposición; 2 = un motivo; 1 = «pereza»; 0 = nada.
- **EX040 — Expediente de un parche aplazado.** Escriba el expediente del aviso para PLC-WRAP. *Rúbrica:* 3 = se aplica, motivo, mitigación, fecha prevista, responsable, revisión; 2 = la mayoría; 1 = «parchear más tarde»; 0 = nada.

### Síntesis del capítulo

Los avisos se cotejan con el registro, se mitigan rápidamente y el parche se aplica en una parada planificada y probada.

### Siga estudiando — capítulo 10 de 18

[← Capítulo 09 (borrador)](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 (borrador) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Copias de seguridad y restauración

### Resultados de aprendizaje

Usted podrá (1) enumerar lo que hay que copiar en una línea; (2) verificar la integridad de las copias de seguridad con hashes; y (3) explicar por qué hay que probar una restauración.

### 11.1 Qué copiar

Los programas de los PLC, los proyectos y pantallas de las HMI, los archivos de recetas, las configuraciones de los dispositivos (conmutadores, cortafuegos, ajustes de la cámara) y los datos de la licencia del software de ingeniería. Sin ellos, recuperarse de un fallo o un ataque significa reconstruirlo todo de memoria. En HPFL eso significa los programas de PLC-FILL y PLC-WRAP, el proyecto de HMI-1, los archivos de recetas, los ajustes de VIS-CAM y las configuraciones de FW-1 y de los conmutadores de la línea. Enumere cada elemento en el registro con la fecha de su última copia. Un elemento que falta en la lista probablemente falte también en las copias.

### 11.2 Dónde guardar las copias

Al menos una copia fuera de la red de la línea, idealmente sin conexión, para que un malware que cifre la línea no pueda alcanzarla. Etiquete cada una con el dispositivo, la fecha y la versión. En HPFL el ingeniero de control mantiene un almacén sin conexión, que es donde se encontró una copia más antigua y coincidente del programa de la envolvedora. Guarde al menos dos copias de cada copia de seguridad importante y anote dónde está cada una. Compruebe que la copia sin conexión es accesible durante un turno de noche. Anote quién puede sacar una copia del emplazamiento.

### 11.3 Comprobar la integridad

Un hash como SHA-256 es una huella de un archivo: cualquier cambio da un valor distinto. Anote el hash al hacer la copia; compruébelo antes de restaurar.

```python
"""Lab 11: verify synthetic PLC backup files against recorded SHA-256 values."""
import hashlib
files = {"PLC-FILL_2026-09.bak": b"fill program v3.2 rungs 1-140",
         "PLC-WRAP_2026-09.bak": b"wrap program v2.0 rungs 1-88 edited"}
recorded = {"PLC-FILL_2026-09.bak": hashlib.sha256(b"fill program v3.2 rungs 1-140").hexdigest(),
            "PLC-WRAP_2026-09.bak": hashlib.sha256(b"wrap program v2.0 rungs 1-88").hexdigest()}
for name, data in files.items():
    h = hashlib.sha256(data).hexdigest()
    print(f"{name:22} {h[:12]} {'MATCH' if h == recorded[name] else 'MISMATCH - do not restore'}")
```

Ejecútelo con `python3 lab_hash.py`. Salida verificada:

```text
PLC-FILL_2026-09.bak   0278a5f83d56 MATCH
PLC-WRAP_2026-09.bak   9974ecb17bab MISMATCH - do not restore
```

Guarde los hashes separados de las copias, por ejemplo en el ticket de cambio o en un registro, para que quien altere una copia no pueda alterar también su hash. El Lab 11 comprueba dos archivos de copia de seguridad frente a los hashes anotados y muestra cómo se ve una discrepancia.

### 11.4 Leer el resultado

La copia de la llenadora coincide con su hash anotado. La de la envolvedora no: su contenido se editó después de anotar el hash. Restaurarla podría cargar un programa que nadie aprobó, así que se aparta y se notifica. Una discrepancia no prueba un ataque; prueba que el archivo cambió después de anotarse su hash. En HPFL la edición se atribuyó a un ajuste aprobado pero no registrado. El procedimiento se actualizó para que cada cambio produzca una nueva copia y un nuevo hash en el mismo ticket.

### 11.5 Restauraciones de prueba

Una copia que nunca se ha restaurado es una esperanza, no un plan. Una o dos veces al año, restaure un programa en un PLC de repuesto o de laboratorio y compárelo con el que está en funcionamiento. Anote la restauración de prueba en el registro con la fecha, el dispositivo, la copia utilizada y el resultado. Si una restauración falla, averigüe por qué antes de que un fallo real le obligue a hacerlo. En HPFL podría usarse para ello un PLC de repuesto de la estantería, tras comprobar que figura como repuesto en el registro.

### 11.6 Con qué frecuencia

Haga una copia tras cada cambio aprobado y en una fecha mensual fija, lo que ocurra primero, para que la copia buena más reciente nunca vaya muy por detrás del programa en funcionamiento. En HPFL las copias de septiembre eran las más recientes antes de la edición del programa de la envolvedora, y por eso un cambio aprobado posterior sin copia nueva causó confusión. Vincule las copias a los tickets de cambio para que cada cambio aprobado produzca una copia y un hash nuevos. Compruebe cada mes que la copia más reciente de cada dispositivo es posterior a su último cambio aprobado. Si no lo es, haga una copia nueva y calcule su hash antes del siguiente turno.

### Ejemplo resuelto (HPFL sintética)

Tomás notifica la discrepancia. El ingeniero de control encuentra en el almacén sin conexión una copia más antigua que coincide y compara el archivo editado: alguien añadió una línea al programa de la envolvedora después de la copia de septiembre sin ticket de cambio. La edición se atribuye a un ajuste aprobado pero no registrado; se actualizan el registro y el procedimiento.

> **Caso sintético — HPFL.** Los archivos y los hashes los genera el laboratorio con contenidos inventados.

### Errores y límites

Un hash coincidente prueba que el archivo no ha cambiado desde que se anotó, no que la versión anotada fuera buena. Los hashes deben guardarse separados de las copias.

### Ejercicios — capítulo 11

- **EX041 — Lista de copias.** Nombre cinco cosas que hay que copiar en la línea HPFL. *Rúbrica:* 3 = cinco elementos correctos; 2 = cuatro; 1 = dos; 0 = nada.
- **EX042 — Decisión ante una discrepancia.** ¿Qué hace Tomás con la copia de la envolvedora marcada `MISMATCH`? *Rúbrica:* 3 = no restaurarla; apartarla; notificarla; buscar una copia verificada; 2 = solo notificarla; 1 = restaurarla igualmente; 0 = nada.
- **EX043 — Un byte cambiado.** Si se cambiara un carácter de los datos de la llenadora, ¿qué imprimiría el laboratorio para ese archivo? *Rúbrica:* 3 = un hash distinto y `MISMATCH - do not restore`; 2 = discrepancia; 1 = coincidencia; 0 = nada.
- **EX044 — Dónde guardar los hashes.** ¿Por qué se guardan los hashes aparte de los archivos de copia? *Rúbrica:* 3 = un atacante que altere las copias podría alterar también los hashes guardados en el mismo lugar; 2 = vago; 1 = espacio; 0 = nada.

### Síntesis del capítulo

Las copias se guardan sin conexión, etiquetadas, con su hash y con restauraciones de prueba; una discrepancia detiene la restauración.

### Siga estudiando — capítulo 11 de 18

[← Capítulo 10 (borrador)](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 (borrador) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Segmentación y reglas del cortafuegos

### Resultados de aprendizaje

Usted podrá (1) explicar con palabras sencillas las zonas y conductos de IEC 62443; (2) leer una tabla de reglas de cortafuegos; y (3) detectar reglas que debilitan la segmentación.

### 12.1 Zonas y conductos

IEC 62443 agrupa en zonas los activos con necesidades de seguridad similares y llama conductos a las conexiones controladas entre ellas. En HPFL: la zona de la línea (PLC, HMI, cámara), una DMZ (copia del historiador, pasarela de acceso remoto, servidor de transferencia de archivos) y la zona de oficinas. El tráfico solo cruza por conductos protegidos por cortafuegos y documentados. Describa cada conducto con su finalidad, el tráfico que permite y su responsable. En HPFL los conductos son la línea enviando datos al historiador de la DMZ, ENG-LT accediendo a los PLC y el acceso de proveedores a través de la pasarela de la DMZ. Cualquier otra cosa que cruce el límite de una zona es un hallazgo.

### 12.2 La DMZ

Los usuarios de oficina quieren datos de producción; la línea no debe aceptar conexiones desde la oficina. Por eso la línea envía los datos a un servidor de la DMZ y la oficina los lee allí. Así ninguna conexión necesita ir directamente de la oficina a la línea. En HPFL la línea envía los datos a la copia del historiador en la DMZ y los usuarios de oficina los leen allí. El acceso de proveedores y la transferencia de archivos también terminan en la DMZ. De este modo FW-1 no necesita ninguna regla que deje entrar a los equipos de oficina directamente en la línea, que es justo el tipo de regla que elimina el ejemplo resuelto siguiente.

### 12.3 Leer las reglas

Cada regla tiene origen, destino, puerto y acción, y se lee de arriba abajo; gana la primera coincidencia. Una última regla de «denegar todo» hace que quede bloqueado todo lo que no esté en la lista. Leer de arriba abajo importa porque una regla amplia de permitir situada por encima de una denegación estrecha deja inútil la denegación. Al revisar una tabla, pregunte por cada regla quién es su responsable, por qué existe y si una regla superior ya decide sobre ese mismo tráfico. La tabla de FW-1 en HPFL tiene cuatro reglas, lo que facilita practicarlo.

### 12.4 Reglas débiles

Busque orígenes «cualquiera», rangos de puertos amplios, reglas sin comentario ni responsable y reglas temporales que nunca se eliminaron. Cada una debe cuestionarse y justificarse o eliminarse mediante el control de cambios. En HPFL la regla 3, de cualquier equipo de oficina a cualquier equipo de la línea y marcada «temp 2025», mostraba a la vez todas estas señales de alerta. Se eliminó mediante el control de cambios y se probó en la siguiente parada. Anote cada pregunta planteada y su respuesta, para que una regla eliminada no vuelva a añadirse más tarde sin revisión.

### 12.5 No edite por su cuenta

Los cambios en el cortafuegos los hace el responsable de la red con un ticket de cambio y un plan de vuelta atrás; una regla equivocada puede detener la línea. Si encuentra una regla débil, notifíquela con el número de la regla y su motivo. El responsable de la red decide cómo cambiarla, prepara una vuelta atrás y prueba en una parada planificada. Su papel es advertir y explicar el riesgo. En HPFL el responsable de la red eliminó la regla 3 solo después de abrir un cambio y acordar una prueba en la siguiente parada. Una regla modificada por otra persona, por buena que sea su intención, no deja constancia ni vuelta atrás, y podría detener la línea.

### Ejemplo resuelto (HPFL sintética)

Tomás revisa la tabla de FW-1 con el responsable de la red. La regla 1 permite a ENG-LT acceder al puerto de programación de los PLC; la regla 2 deja que la línea envíe datos al historiador de la DMZ; la regla 3, «office any → line any allow — temp 2025», no tiene responsable. La regla 4 lo deniega todo. Abren un cambio para eliminar la regla 3, prueban en la siguiente parada y después la línea funciona con normalidad.

> **Caso sintético — HPFL.** La tabla de reglas es inventada.

### Errores y límites

Una buena tabla de reglas puede quedar anulada por un conmutador no gestionado o un módem que eluda el cortafuegos; los recorridos por la planta y los diagramas complementan la revisión de las reglas.

### Ejercicios — capítulo 12

- **EX045 — Zonas de HPFL.** Nombre las tres zonas de HPFL y un activo de cada una. *Rúbrica:* 3 = línea, DMZ y oficinas con activos correctos; 2 = dos; 1 = una; 0 = nada.
- **EX046 — Primera coincidencia.** Con la regla 3 por encima de la regla 4, ¿qué ocurre con el tráfico de oficina hacia HMI-1? *Rúbrica:* 3 = lo permite la regla 3 antes de que se aplique la denegación; 2 = se permite; 1 = se deniega; 0 = nada.
- **EX047 — Por qué una DMZ.** Explique cómo la DMZ permite al personal de oficina ver datos de producción sin conectarse a la línea. *Rúbrica:* 3 = la línea envía a un servidor de la DMZ, la oficina lee allí, sin regla de oficina a línea; 2 = parcial; 1 = «es más seguro»; 0 = nada.
- **EX048 — Eliminar una regla.** Describa los pasos seguros para eliminar la regla 3. *Rúbrica:* 3 = ticket de cambio, confirmación del responsable, ventana planificada, vuelta atrás, prueba, registro; 2 = parte; 1 = borrarla ya; 0 = nada.

### Síntesis del capítulo

Las zonas se separan mediante conductos documentados y con responsable; las reglas amplias o sin responsable se eliminan mediante el control de cambios.

### Siga estudiando — capítulo 12 de 18

[← Capítulo 11 (borrador)](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 (borrador) →](#ch-13)

<a id="ch-13"></a>

## Capítulo 13 — Dispositivos IoT en la planta de fabricación

### Resultados de aprendizaje

Usted podrá (1) identificar los dispositivos IoT de una línea; (2) contrastarlos con una base de disposiciones de ETSI EN 303 645; y (3) decidir cómo conectarlos de forma segura.

### 13.1 Qué cuenta aquí como IoT

Contadores de energía inteligentes, sensores de vibración inalámbricos, la cámara de visión, una impresora de etiquetas conectada a la nube y las tabletas que usa el personal de calidad. A menudo llegan a través de compras y no de ingeniería, así que nadie los revisa antes. En HPFL el equipo de calidad pidió sensores de vibración inalámbricos para los motores de la envolvedora, y la cámara de visión ya está instalada. Cada uno de estos dispositivos debería figurar en el registro, con un responsable y la red que usa. Compras debería implicar al responsable de la red antes de hacer el pedido. Pida a compras que le informe de cada dispositivo en red que se encargue.

### 13.2 Una base con la que comparar

ETSI EN 303 645 establece disposiciones básicas de seguridad para la IoT de consumo, y NIST IR 8259 describe lo que deberían hacer los fabricantes. Ambas son también listas de comprobación útiles para los dispositivos de planta. Preguntas que hacer a un proveedor: ¿hay contraseñas predeterminadas universales? ¿Hay alguna forma de notificar vulnerabilidades? ¿Se proporcionarán actualizaciones de software y durante cuánto tiempo? ¿Está cifrada la comunicación? ¿Puede restablecerse el dispositivo y borrarse sus datos? Envíe las preguntas al proveedor antes de la compra y guarde las respuestas con el expediente de compra. Cuando sea posible, compruebe las afirmaciones en la entrega: ¿obliga el dispositivo a cambiar la contraseña durante la configuración y usa realmente TLS? Una respuesta que no puede comprobarse sigue siendo útil, pero debe marcarse como afirmación del proveedor.

### 13.3 Conectar de forma segura

Los dispositivos IoT que se comunican con la nube de un proveedor van en su propio segmento, no en la VLAN de la línea. Permita solo las direcciones de la nube que necesitan, impida que alcancen los PLC y regístrelos con un responsable y un plan de actualizaciones. En HPFL el responsable de la red eligió una VLAN IoT nueva para la pasarela de VIB-1 a VIB-4, en lugar de la VLAN 20 de la línea, porque los sensores informan a la nube de un proveedor. Tras la instalación, compruebe con el responsable de la red que la pasarela no puede alcanzar los PLC, mediante una revisión de las reglas y no sondeando.

### 13.4 Fin del soporte

Cuando un proveedor deja de publicar actualizaciones, planifique la sustitución. Un sensor barato sin parches durante años en la red de la línea es un punto de apoyo fácil. Anote en el registro el periodo de soporte declarado por el proveedor, para poder planificar el fin del soporte con mucha antelación. En HPFL el proveedor de los sensores de vibración prometió actualizaciones durante cinco años; la fecha de sustitución debe figurar en el registro junto a la entrada del dispositivo. Si un dispositivo debe seguir en uso tras el fin del soporte, refuerce su aislamiento y anote la decisión con una fecha de revisión. Avise al responsable con suficiente antelación para que pueda planificarse el presupuesto.

### Ejemplo resuelto (HPFL sintética)

Calidad quiere sensores de vibración inalámbricos VIB-1 a VIB-4 en los motores de la envolvedora, que informen a la nube de un proveedor. Tomás envía al proveedor las cinco preguntas. Respuestas: contraseñas únicas por dispositivo, una dirección de divulgación publicada, actualizaciones durante cinco años, TLS hacia la nube y restablecimiento de fábrica documentado. El responsable de la red coloca la pasarela de los sensores en una VLAN IoT nueva a la que solo se permite llegar a las direcciones de la nube del proveedor.

> **Caso sintético — HPFL.** Los sensores y las respuestas del proveedor son inventados.

### Errores y límites

Las respuestas del proveedor son afirmaciones; compruebe lo que pueda (por ejemplo, que el dispositivo obligó a cambiar la contraseña durante la configuración). ETSI EN 303 645 se dirige a productos de consumo, así que los dispositivos industriales pueden necesitar requisitos adicionales de IEC 62443-4-2.

### Ejercicios — capítulo 13

- **EX049 — Detectar la IoT.** Enumere tres dispositivos IoT que podrían aparecer en HPFL fuera de los planos de ingeniería. *Rúbrica:* 3 = tres dispositivos plausibles; 2 = dos; 1 = uno; 0 = nada.
- **EX050 — Preguntas al proveedor.** Escriba las cinco preguntas básicas para un proveedor. *Rúbrica:* 3 = contraseñas predeterminadas, divulgación, periodo de actualizaciones, cifrado, restablecimiento y borrado; 2 = cuatro; 1 = dos; 0 = nada.
- **EX051 — Ubicación.** ¿Dónde debería conectarse la pasarela de los sensores VIB y qué debería poder alcanzar? *Rúbrica:* 3 = VLAN IoT separada; solo la nube del proveedor; sin acceso a los PLC; 2 = solo separada; 1 = VLAN de la línea; 0 = nada.
- **EX052 — Fin de las actualizaciones.** El proveedor de la impresora de etiquetas anuncia el fin del soporte. ¿Qué anota y planifica Tomás? *Rúbrica:* 3 = estado en el registro, nota de riesgo, aislamiento compensatorio, plan y fecha de sustitución; 2 = parte; 1 = ignorarlo; 0 = nada.

### Síntesis del capítulo

La IoT de la planta se contrasta con una base, se aísla para que solo tenga lo que necesita y se sustituye cuando termina el soporte.

### Siga estudiando — capítulo 13 de 18

[← Capítulo 12 (borrador)](#ch-12) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 14 (borrador) →](#ch-14)

<a id="ch-14"></a>

## Capítulo 14 — Reconocer el comportamiento anómalo

### Resultados de aprendizaje

Usted podrá (1) describir cómo es lo normal en la línea HPFL; (2) reconocer señales que pueden indicar un ataque o una avería; y (3) usar los nombres de ATT&CK for ICS para describir lo que vio.

### 14.1 Conocer lo normal

Los operadores conocen el sonido, el ritmo y las pantallas de la línea. Los técnicos añaden lo normal de la red y de los sistemas: qué dispositivos se comunican, qué cuentas inician sesión, con qué frecuencia cambian los programas. Déjelo por escrito; lo «normal» que solo está en la cabeza de las personas desaparece con los cambios de turno. En HPFL, Tomás ya anotó que las escrituras solo llegan desde HMI-1 y ENG-LT. Notas similares pueden cubrir las horas habituales de inicio de sesión, la frecuencia con que cambian los programas de los PLC y qué dispositivos aparecen en la red. Guárdelas en el registro o en un documento compartido, fechadas y actualizadas tras los cambios.

### 14.2 Señales que hay que notificar

Un punto de consigna cambia sin que nadie pulse un botón. Las pantallas de la HMI se congelan o muestran valores que no coinciden con los indicadores locales. Aparece en el registro una descarga de programa sin trabajo asociado. Aparece un dispositivo nuevo en la red. Se producen sesiones remotas fuera de un ticket. La línea se detiene sin causa mecánica. Notifique cualquiera de estas señales con la hora, el dispositivo y lo que vio, y adjunte fotografías o líneas del registro cuando pueda. En HPFL, una discrepancia entre HMI-1 y un termómetro portátil resultó ser un sensor averiado, pero aun así la notificación permitió un diagnóstico rápido.

### 14.3 Poner nombre a lo que vio

MITRE ATT&CK for ICS ofrece nombres compartidos: T0836 Modify Parameter para puntos de consigna alterados, T0886 Remote Services para el uso indebido del acceso remoto, T0843 Program Download para cambios de lógica inesperados. Usar estos nombres en un informe ayuda al equipo de seguridad, pero notifique lo que observó, no una suposición sobre el atacante. Los nombres ayudan cuando se comparan informes de distintos turnos o emplazamientos. Escriba primero la observación y después el nombre de la técnica si encaja: por ejemplo, la cuenta de administrador cambió la velocidad de la envolvedora de 120 a 180 a las 07:45, lo que encaja con Modify Parameter. Deje la intención y la atribución al equipo de seguridad.

### 14.4 ¿Avería o ataque?

La mayoría de los eventos anómalos son averías o errores. Al principio eso no importa: la respuesta es la misma (mantener a las personas a salvo, preservar la evidencia, notificar). La causa se decide después. En HPFL la discrepancia de temperatura era un sensor averiado, y el cambio de velocidad era un ajuste bienintencionado de un operador. Ambos se gestionaron con los mismos pasos: poner en condiciones seguras, registrar, notificar. La causa se encontró después, gracias a la evidencia que se había conservado. Tratar todos los eventos de la misma manera también evita situaciones incómodas: no se acusa a nadie y no se descarta nada demasiado pronto.

### 14.5 Qué no hacer

No reinicie dispositivos, borre registros, desconecte cables ni «arregle» valores antes de que el supervisor y el ingeniero estén de acuerdo; podría destruir la evidencia de lo ocurrido o crear un peligro nuevo. El supervisor decide si la línea sigue funcionando; el ingeniero decide cómo examinar los dispositivos. Su parte es fotografiar, anotar la hora y llamar. Si un peligro exige una acción inmediata, siga los procedimientos de seguridad habituales y anote lo que hizo. En HPFL, Tomás no restableció el sensor. Esa contención conservó la evidencia que después mostró la causa.

### Ejemplo resuelto (HPFL sintética)

HMI-1 muestra la llenadora a temperatura normal, pero el termómetro portátil del operador marca 12 °C más. Tomás fotografía ambas lecturas, anota la hora y llama al supervisor, que detiene la llenadora de forma segura. Más tarde el ingeniero encuentra un sensor averiado (una avería, no un ataque), pero la evidencia agilizó el diagnóstico.

> **Caso sintético — HPFL.** Las lecturas son inventadas.

### Errores y límites

Una lista de señales nunca es completa; confíe en los operadores con experiencia que dicen «esto no está bien». ATT&CK describe técnicas, no certezas sobre la intención.

### Ejercicios — capítulo 14

- **EX053 — La HMI no coincide con el indicador.** ¿Qué sugiere una diferencia entre la HMI y un indicador local, y cuál es la primera acción? *Rúbrica:* 3 = avería del sensor o pantalla manipulada; mantener seguro o detener a través del supervisor, registrar la evidencia; 2 = una parte; 1 = confiar en la HMI; 0 = nada.
- **EX054 — Asociar técnicas.** Asocie con ATT&CK for ICS: (a) descarga de programa no planificada; (b) sesión de proveedor fuera de ticket; (c) valor de velocidad cambiado. *Rúbrica:* 3 = T0843, T0886, T0836; 2 = dos; 1 = una; 0 = nada.
- **EX055 — La misma respuesta.** ¿Por qué la respuesta inicial es la misma ante una avería y ante un ataque? *Rúbrica:* 3 = primero la seguridad y la evidencia; al principio se desconoce la causa; 2 = parcial; 1 = «no lo es»; 0 = nada.
- **EX056 — Dejar por escrito lo normal.** Dé tres elementos para una hoja de «lo normal» de HPFL. *Rúbrica:* 3 = tres elementos concretos (quién se comunica, patrón de inicios de sesión, frecuencia de cambios, etc.); 2 = dos; 1 = vago; 0 = nada.

### Síntesis del capítulo

Conocer lo normal permite advertir lo anómalo; responda por la seguridad y la evidencia antes de decidir la causa.

### Siga estudiando — capítulo 14 de 18

[← Capítulo 13 (borrador)](#ch-13) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 15 (borrador) →](#ch-15)

<a id="ch-15"></a>

## Capítulo 15 — Notificar un incidente y primeras acciones

### Resultados de aprendizaje

Usted podrá (1) seguir los pasos de primera respuesta de HPFL; (2) redactar una primera notificación clara; y (3) explicar por qué la evidencia se preserva antes de empezar la recuperación.

### 15.1 Primeros pasos

Ponga a salvo a las personas: el supervisor decide si detener o aislar la parte afectada de la línea siguiendo los procedimientos habituales. Después llame al contacto para incidentes que figura en la hoja del emplazamiento. Anote lo que ve a medida que avanza. No intente eliminar el malware ni restaurar sistemas usted mismo. En HPFL el supervisor de noche pasó la línea a control local desde el panel y detuvo la envolvedora antes de que ocurriera nada más. Después Tomás fotografió la pantalla y llamó al contacto para incidentes. Seguir los pasos en orden mantiene a salvo a las personas y deja intacta la evidencia.

### 15.2 Una buena primera notificación

Responde a: qué advirtió, dónde, cuándo, qué dispositivos, qué está haciendo ahora la línea, qué se ha hecho hasta el momento y a quién ha avisado. Los hechos breves valen más que las teorías largas. NIST SP 800-82r3 subraya que la respuesta a incidentes de TO debe planificarse con operaciones, porque las acciones tomadas con pánico pueden dañar el proceso. En HPFL la notificación de Tomás cabía en una frase por punto y se envió en pocos minutos. Las correcciones posteriores se añadieron por escrito, sin modificar la primera notificación. Guarde una copia de cada notificación que envíe, con la hora.

### 15.3 Preservar la evidencia

Fotografíe las pantallas, lleve una cronología escrita y deje los dispositivos como están salvo que la seguridad exija lo contrario. Si hay que aislar un dispositivo, lo hace el ingeniero con un método planificado (por ejemplo, desactivando un puerto del conmutador) y anota exactamente cuándo. Mantenga la cronología escrita en el orden en que ocurrieron los hechos, con horas tomadas de una sola referencia, como su reloj, y anote cualquier diferencia de reloj conocida entre dispositivos. Las fotografías deben mostrar juntos el nombre del dispositivo y la pantalla. Guarde las fotografías junto con la cronología en un solo lugar.

### 15.4 Comunicación

Use la lista de contactos del emplazamiento. No publique nada sobre el incidente en redes sociales ni en grupos de chat. No contacte con proveedores ni autoridades por su cuenta salvo que se lo pida el responsable del incidente. En HPFL el responsable del incidente decide quién habla con proveedores, clientes y autoridades. Evite especular con los compañeros sobre la causa, porque los rumores se extienden rápido en la planta. Si alguien de fuera le pregunta por el incidente, remítalo al responsable del incidente. Use los teléfonos de la hoja del emplazamiento, no números guardados a título personal, porque esos se mantienen al día.

### 15.5 Obligaciones de notificación

Algunos sectores y países exigen notificar a los reguladores o a CISA en plazos fijados; de eso se encarga el responsable del incidente, pero es su cronología la que lo hace posible. En HPFL la cronología de Tomás, con sus horas y fotografías, dio al responsable del incidente lo necesario para cualquier notificación obligatoria. Manténgala exacta y completa, y transmita las correcciones al responsable por escrito en cuanto las detecte. Las horas son lo que más importa: cuándo se advirtió el evento, cuándo se notificó y cuándo se detuvo la línea. Anótelas en el momento en lugar de reconstruirlas después.

### Ejemplo resuelto (HPFL sintética)

A las 03:10, HMI-1 muestra un mensaje de rescate. Tomás avisa al supervisor de noche, que pasa la línea a control local desde el panel y detiene la envolvedora. Tomás fotografía la pantalla y llama al contacto para incidentes a las 03:14. Su notificación dice: «03:10 pantalla de rescate en HMI-1; línea en control local, envolvedora detenida a las 03:12; no se han visto otras pantallas afectadas; no se ha desconectado nada; supervisor informado».

> **Caso sintético — HPFL.** El incidente es inventado.

### Errores y límites

Las listas de contactos se quedan desactualizadas; revíselas cada trimestre. Una primera notificación puede ser errónea; corríjala por escrito en lugar de borrarla.

### Ejercicios — capítulo 15

- **EX057 — Ordenar los pasos.** Ordene: llamar al contacto para incidentes; el supervisor pone la línea en condiciones seguras; fotografiar la pantalla; restaurar la HMI. *Rúbrica:* 3 = seguridad, fotografía, llamada; la restauración, después y a cargo de los responsables; 2 = casi todo bien; 1 = restaurar primero; 0 = nada.
- **EX058 — Mejorar una notificación.** Reescriba «la HMI está hackeada, seguramente son rusos» como una primera notificación basada en hechos. *Rúbrica:* 3 = hora, dispositivo, observación, estado de la línea, acciones, a quién se avisó; sin especulación; 2 = parcial; 1 = sigue especulando; 0 = nada.
- **EX059 — Desconectar.** Un compañero quiere desconectar de inmediato el cable de red de HMI-1. ¿Qué le dice? *Rúbrica:* 3 = aislar solo a través del supervisor o el ingeniero, de forma planificada y registrada; seguridad y evidencia; 2 = esperar; 1 = hacerlo; 0 = nada.
- **EX060 — Quién notifica.** ¿Quién decide si se notifica a los reguladores o a CISA? *Rúbrica:* 3 = el responsable del incidente o la dirección; el técnico aporta la cronología; 2 = solo el responsable; 1 = el técnico solo; 0 = nada.

### Síntesis del capítulo

Primero la seguridad; después, hechos registrados, evidencia preservada y llamada a las personas adecuadas; la recuperación viene luego.

### Siga estudiando — capítulo 15 de 18

[← Capítulo 14 (borrador)](#ch-14) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 16 (borrador) →](#ch-16)

<a id="ch-16"></a>

## Capítulo 16 — Recuperación y vuelta a la producción

### Resultados de aprendizaje

Usted podrá (1) describir los pasos para restablecer una línea tras un incidente; (2) verificar los sistemas restaurados antes de volver a arrancar; y (3) explicar por qué las lecciones aprendidas deben cambiar algo.

### 16.1 Orden de la recuperación

La recuperación la planifican el responsable del incidente, el ingeniero de control y operaciones. Normalmente: confirmar que la causa está contenida, reconstruir los ordenadores afectados a partir de imágenes en buen estado conocido, restaurar los programas de los PLC desde copias verificadas (capítulo 11), cambiar las contraseñas que puedan estar expuestas y, después, probar. En HPFL, HMI-1 se reconstruyó a partir de la imagen del fabricante, los programas de ambos PLC se compararon con copias coincidentes y se cambió la contraseña de administrador. Seguir este orden evita volver a arrancar con un problema aún presente. Cada paso se anota con su hora y la persona que lo hizo.

### 16.2 Verificación antes de volver a arrancar

Compare los programas restaurados de los PLC con las copias verificadas, compruebe que las pantallas de la HMI muestran valores correctos frente a los indicadores locales, confirme que las reglas del cortafuegos coinciden con la tabla aprobada y haga pasar la línea en vacío por un ciclo de prueba. Calidad da su conformidad antes de que se procese producto. En HPFL el ciclo de prueba funcionó en vacío durante 30 minutos y calidad dio su conformidad a las 11:20, antes de reanudar la producción. Anote cada comprobación y su resultado en el expediente del incidente. Si alguna comprobación falla, la línea no vuelve a arrancar hasta que se entienda la causa. El expediente muestra entonces quién aprobó el rearranque y con qué evidencias.

### 16.3 Vigilar después

A veces los atacantes vuelven. Durante los días posteriores al rearranque, vigile más de cerca los inicios de sesión, las sesiones remotas y los dispositivos nuevos, y notifique de inmediato cualquier cosa inusual. Acuerde con el supervisor cuánto dura el periodo de vigilancia y quién revisa los registros cada día. En HPFL la reunión de lecciones aprendidas encontró un puerto de escritorio remoto accesible desde internet abierto por un contratista, lo que hace especialmente importante vigilar de cerca las sesiones remotas. Notifique cualquier cosa inusual al responsable del incidente, no solo a su turno. Anote en el expediente del incidente la fecha de fin del periodo de vigilancia para que no caduque sin que nadie lo note.

### 16.4 Lecciones aprendidas

Una reunión breve en las dos semanas siguientes responde a: qué ocurrió, qué funcionó, qué no y qué cambia. Cada cambio tiene un responsable y una fecha. Una sesión de lecciones aprendidas que no cambia nada ha fracasado. En HPFL la reunión de lecciones aprendidas encargó al responsable de la red cerrar el puerto de escritorio remoto de HMI-1 y hacer una comprobación mensual. Cada acción se sigue hasta que está hecha y se demuestra eficaz, y las actas de la reunión se guardan con el expediente del incidente. Invite a los operadores que estaban de turno; a menudo saben qué funcionó.

### 16.5 Conservación de registros

Guarde juntos la cronología, las fotografías, las decisiones y los resultados de las pruebas. Sirven para el seguro, los reguladores y la próxima mejora. Guarde los registros juntos en una sola carpeta o ticket, con el acceso limitado a quienes los necesitan. Incluya la primera notificación, sus correcciones, las fotografías y los resultados del ciclo de prueba. Así el siguiente recorrido podrá comprobar si se aplicaron las lecciones. Conserve los registros durante el tiempo que exija la política del emplazamiento y anote quién puede leerlos. Cuando una aseguradora o un regulador haga una pregunta meses después, la respuesta debe salir de estos registros y no de la memoria, que se desvanece rápido.

### 16.6 Comunicar el rearranque

Explique a cada turno qué ha cambiado: contraseñas nuevas, pantallas que se ven distintas y qué señales inusuales deben notificarse durante el periodo de vigilancia. En HPFL eso supuso decir a cada turno que la contraseña de administrador había cambiado y que debían notificarse las sesiones remotas inesperadas o los dispositivos nuevos. Una nota breve por escrito junto a HMI-1, sin contraseñas, ayuda a quienes se perdieron la sesión informativa. Informe en persona a los dos turnos siguientes si es posible y pídales que confirmen que lo han entendido. Las preguntas que surgen en estas sesiones suelen mostrar dónde debe aclararse el procedimiento, así que anótelas también.

### Ejemplo resuelto (HPFL sintética)

Tras el incidente del rescate, HMI-1 se reconstruye a partir de la imagen del fabricante; los programas de ambos PLC se comparan con copias coincidentes y no presentan cambios. Se cambia la contraseña de administrador. Un ciclo de prueba funciona en vacío durante 30 minutos, calidad da su conformidad a las 11:20 y se reanuda la producción. La reunión de lecciones aprendidas descubre que HMI-1 tenía un puerto de escritorio remoto accesible desde internet abierto por un contratista; la acción (cerrarlo y añadir una comprobación mensual) se asigna al responsable de la red.

> **Caso sintético — HPFL.** La recuperación es inventada.

### Errores y límites

Restaurar una copia hecha después del compromiso vuelve a cargar el problema; importan las fechas y los hashes verificados. La presión para volver a arrancar rápido es real; el ciclo de prueba no es negociable.

### Ejercicios — capítulo 16

- **EX061 — Orden de la recuperación.** Ordene: ciclo de prueba; reconstruir la HMI; conformidad de calidad; cambiar contraseñas; confirmar la contención. *Rúbrica:* 3 = contención, reconstrucción, contraseñas, prueba, conformidad; 2 = casi todo; 1 = al azar; 0 = nada.
- **EX062 — Comprobaciones de verificación.** Nombre tres comprobaciones antes de volver a arrancar la línea. *Rúbrica:* 3 = programas frente a copia verificada, HMI frente a indicadores, reglas del cortafuegos, ciclo de prueba en vacío; 2 = dos; 1 = una; 0 = nada.
- **EX063 — Copia inadecuada.** ¿Por qué podría ser un error restaurar una copia del día del incidente? *Rúbrica:* 3 = puede contener el cambio del atacante; usar una copia verificada anterior al incidente; 2 = parcial; 1 = no hay problema; 0 = nada.
- **EX064 — Convertir una lección en acción.** Escriba la acción de la reunión de lecciones aprendidas de HPFL con forma de responsable y fecha. *Rúbrica:* 3 = cerrar el puerto RDP más comprobación mensual, responsable de la red, fecha; 2 = sin responsable o fecha; 1 = «tener cuidado»; 0 = nada.

### Síntesis del capítulo

Recupere en orden, verifique antes de volver a arrancar, vigile después y convierta las lecciones en acciones con responsable.

### Siga estudiando — capítulo 16 de 18

[← Capítulo 15 (borrador)](#ch-15) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 17 (borrador) →](#ch-17)

<a id="ch-17"></a>

## Capítulo 17 — Gestión de cambios y documentación

### Resultados de aprendizaje

Usted podrá (1) explicar por qué cada cambio en la línea necesita un ticket; (2) redactar una solicitud de cambio con un plan de vuelta atrás; y (3) mantener los planos y los registros al día con la realidad.

### 17.1 Por qué el control de cambios es seguridad

La mayoría de los problemas en las plantas vienen de cambios que nadie registró: una regla de cortafuegos añadida con prisas, un programa editado durante una avería, una cámara atornillada por un contratista. El control de cambios significa que cada cambio se solicita, se revisa, se aprueba, se ejecuta y se registra. También facilita advertir un cambio no registrado, que puede ser la primera señal de un ataque. En HPFL varios problemas de este libro empezaron como cambios no registrados: el programa de la envolvedora editado del capítulo 11, la regla de cortafuegos temporal del capítulo 12 y el puerto de escritorio remoto del capítulo 16. Con un ticket, cada uno habría sido visible antes.

### 17.2 Una solicitud de cambio

Indica qué cambiará, por qué, en qué dispositivos, quién lo hace, cuándo, el riesgo para el proceso, cómo se comprueba el éxito y cómo deshacerlo. Los cambios de emergencia durante una avería están permitidos, pero se registran después, dentro del mismo turno. En HPFL la solicitud de Tomás para la actualización de VIS-CAM cubría todo esto en pocas líneas. Mantenga el formulario breve para que la gente lo use de verdad. Quien aprueba comprueba que la prueba de éxito y la vuelta atrás son realistas antes de dar su acuerdo.

### 17.3 Vuelta atrás

Antes del cambio, guarde el programa o la configuración actual y su hash. Si la comprobación falla, restáurelo. Un cambio sin vuelta atrás es una apuesta. En HPFL la vuelta atrás para VIS-CAM consistía en reinstalar el firmware 1.0.7 desde un archivo guardado con su hash anotado. Compruebe que el archivo guardado está completo antes de empezar el cambio. Si la propia vuelta atrás falla, deténgase y llame al ingeniero de control. En HPFL los hashes de los archivos guardados se anotaban en el ticket de cambio, de modo que un archivo restaurado podía comprobarse antes de cargarlo. Sin eso, una vuelta atrás podría cargar una copia corrupta o editada sin que nadie lo advirtiera.

### 17.4 Mantener los documentos al día

Actualice el registro de activos, el plano de red y la tabla de reglas en el mismo ticket. Marque los planos con un número de revisión y una fecha. En HPFL el plano de red seguía en la revisión 3 mientras que la VLAN IoT solo aparecía en los borradores de la revisión 4, algo que encontró el recorrido del proyecto final. Actualizar los documentos en el mismo ticket evita que se abra ese hueco. Cuando cambia un plano, marque la revisión antigua como superada y consérvela, para que las decisiones pasadas sigan pudiendo entenderse. Compruebe los números de revisión en cada recorrido; un plano cuya revisión va por detrás de la realidad es en sí mismo un hallazgo, como comprobó HPFL.

### 17.5 Revisores

La persona que hace un cambio no debería ser la única que lo aprueba. En HPFL el ingeniero de control revisa los cambios de programa, el responsable de la red revisa los cambios del cortafuegos y de los conmutadores, y el supervisor confirma la ventana de producción. Un segundo par de ojos detecta errores de tecleo en direcciones y valores antes de que lleguen a la línea. Anote el nombre del revisor en el ticket. Si la única persona que puede revisar no está disponible, espere a la siguiente ventana salvo que el cambio sea de emergencia.

### Ejemplo resuelto (HPFL sintética)

El proveedor de la cámara de visión necesita instalar el firmware 1.1.0 en VIS-CAM. Tomás escribe: «Cambio 512: actualizar VIS-CAM de 1.0.7 a 1.1.0 para corregir la precisión de los rechazos; lo hace el técnico de calidad; martes a las 06:00, parada planificada; riesgo: los rechazos dejan de funcionar; comprobación: 20 paquetes de prueba, incluidos 5 con sellado defectuoso, rechazados; vuelta atrás: reinstalar 1.0.7 desde el archivo guardado, con el hash anotado». La actualización supera la comprobación y el registro muestra 1.1.0.

> **Caso sintético — HPFL.** El cambio y la corrección del proveedor son inventados.

### Errores y límites

El control de cambios puede convertirse en puro papeleo; mantenga los formularios breves y exija los campos clave. Los cambios de emergencia no deben convertirse en la vía normal.

### Ejercicios — capítulo 17

- **EX065 — Campos de una solicitud.** Enumere seis campos de una solicitud de cambio. *Rúbrica:* 3 = qué, por qué, dispositivos, quién, cuándo, riesgo, comprobación, vuelta atrás (seis cualesquiera); 2 = cuatro; 1 = dos; 0 = nada.
- **EX066 — Edición durante una avería.** El ingeniero edita PLC-FILL durante una avería a las 2 de la madrugada. ¿Qué debe ocurrir después? *Rúbrica:* 3 = se registra como cambio de emergencia dentro del turno, nueva copia y hash, registro actualizado; 2 = solo registrarlo; 1 = nada; 0 = nada.
- **EX067 — Comprobación fallida.** La prueba de VIS-CAM deja pasar 2 de 5 sellados defectuosos. ¿Qué ocurre a continuación? *Rúbrica:* 3 = vuelta atrás a 1.0.7, verificar, registrar el fallo, contactar con el proveedor; 2 = vuelta atrás; 1 = funcionar igualmente; 0 = nada.
- **EX068 — Cambio no registrado.** ¿Por qué merece notificarse un cambio no registrado aunque parezca inofensivo? *Rúbrica:* 3 = puede ser no autorizado o señal de ataque; rompe la línea base y las copias; 2 = uno; 1 = ignorarlo; 0 = nada.

### Síntesis del capítulo

Los cambios solicitados, revisados, reversibles y registrados mantienen la línea conocida; los no registrados son señales de alerta.

### Siga estudiando — capítulo 17 de 18

[← Capítulo 16 (borrador)](#ch-16) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 18 (borrador) →](#ch-18)

<a id="ch-18"></a>

## Capítulo 18 — Proyecto final: un recorrido de seguridad por la línea

### Resultados de aprendizaje

Usted podrá (1) combinar las habilidades del libro en un recorrido planificado; (2) elaborar una lista breve de hallazgos con prioridades; y (3) presentarla al supervisor y al ingeniero.

### 18.1 Planificación

Acuerde con el supervisor el alcance, la fecha y el permiso: qué armarios, qué registros, ninguna conexión a dispositivos, condiciones de parada. Lleve el registro de activos, el plano de red, la tabla de reglas y los registros de soportes y de acceso remoto. Escriba el plan en el permiso: la franja horaria, los armarios que abrirá un electricista, los registros que se revisarán y las condiciones de parada. En HPFL el recorrido tenía un permiso de dos horas. Acuerde de antemano quién recibirá los hallazgos y cuándo. Reserve la fecha con antelación para que operaciones pueda organizarse.

### 18.2 Qué comprobar

Físico: armarios cerrados con llave, ningún módem ni conmutador sin explicación, ninguna contraseña en los paneles, ninguna memoria USB suelta. Registros: registro de activos completo, copias recientes y con hashes coincidentes, avisos registrados, cambios cerrados. Acceso: cuentas de proveedores desactivadas fuera de las sesiones, uso de la cuenta de administrador limitado. Use una lista de comprobación para que no se pase nada por alto y para poder comparar el siguiente recorrido con este. En HPFL la lista de comprobación llevó a Tomás hasta el módem del armario de la llenadora, las firmas antimalware antiguas de ENG-LT, el plano desactualizado y una memoria de recetas que faltaba en el registro de soportes.

### 18.3 Redactar los hallazgos

Cada hallazgo: qué vio, dónde, por qué importa (consecuencia), corrección propuesta y responsable. Guarde con él la evidencia (fotografías, extractos de registros). Redacte los hallazgos durante el recorrido o justo después, mientras los detalles están frescos. En HPFL el hallazgo del módem celular incluía su ubicación en el armario de la llenadora, una fotografía y la consecuencia de que alguien podría alcanzar la llenadora desde fuera. Cada hallazgo necesita un único responsable que acepte actuar. Limite cada hallazgo a unas pocas líneas para que pueda leerse rápido en la reunión. Separe lo que vio de lo que cree que significa.

### 18.4 Priorizar

Ordene por consecuencia y facilidad: lo que dé un camino no revisado hacia los PLC va primero; los arreglos menores, al final. Presente con claridad los tres primeros; las listas largas esconden lo importante. En HPFL el módem fue lo primero porque era un camino no revisado hacia un PLC. Las firmas antimalware antiguas de ENG-LT fueron lo segundo, porque ese portátil programa los PLC. Después venían la memoria que faltaba y el plano desactualizado. Escriba un motivo de una línea para cada posición. Acuerde el orden con el supervisor, que puede conocer motivos de producción para cambiarlo.

### 18.5 Seguimiento

Acuerde responsables y fechas en la reunión y después compruebe el avance cada mes. Anote los responsables y las fechas en una lista breve compartida con el supervisor. En cada comprobación mensual, anote lo que se completó y lo que se retrasó, con el motivo. En HPFL el siguiente recorrido debería empezar confirmando que el módem del armario de la llenadora se ha desconectado o puesto bajo control. Los hallazgos que se retrasan una y otra vez se plantean al supervisor en lugar de arrastrarlos en silencio. Cierre cada elemento solo con evidencia de que se hizo.

### 18.6 Presentar al supervisor

Use un lenguaje sencillo y consecuencias que importen al supervisor: «este módem podría permitir que alguien cambiara la llenadora desde fuera» funciona mejor que los nombres de protocolos. Lleve fotografías, no pase de diez minutos y termine con las decisiones que necesita: responsable, fecha y cualquier ventana de producción. Dé las gracias a los operadores que ayudaron; su cooperación decide si el próximo recorrido será bien recibido. Envíe después un breve resumen escrito con los hallazgos, los responsables y las fechas. Guarde una copia del resumen con la evidencia del recorrido, para que el siguiente pueda empezar comprobando qué ha cambiado desde entonces. Si el supervisor no está de acuerdo con una posición, anote el desacuerdo y el motivo.

### Ejemplo resuelto (HPFL sintética)

El recorrido de Tomás, con un permiso de dos horas, encuentra: (1) un módem celular conectado dentro del armario de la llenadora y que no figura en el registro; (2) firmas antimalware de ENG-LT con 40 días de antigüedad; (3) el plano de red en la revisión 3 mientras la VLAN IoT solo existe en los borradores de la revisión 4; (4) una memoria de recetas que falta en el registro de soportes. Sitúa el módem en primer lugar, el portátil en segundo, la memoria en tercero y el plano en cuarto, y el supervisor asigna responsables.

> **Caso sintético — HPFL.** Los hallazgos son inventados.

### Errores y límites

Un recorrido es una instantánea; los problemas reaparecen si no se repite con regularidad. No sustituye a una evaluación profesional frente a IEC 62443.

### Ejercicios — capítulo 18

- **EX069 — Alcance del permiso.** Escriba el alcance y tres condiciones de parada para el recorrido. *Rúbrica:* 3 = zonas, registros, ninguna conexión a dispositivos, tres paradas concretas; 2 = parcial; 1 = vago; 0 = nada.
- **EX070 — Formato de hallazgo.** Reescriba «módem malo» como un hallazgo completo. *Rúbrica:* 3 = qué, dónde, por qué, corrección, responsable, evidencia; 2 = cuatro partes; 1 = dos; 0 = nada.
- **EX071 — Priorización.** Justifique situar el módem por encima de las firmas antimalware antiguas. *Rúbrica:* 3 = el módem es un camino activo y no revisado hacia los PLC; el portátil solo supone riesgo cuando se conecta y está controlado; 2 = parcial; 1 = al revés; 0 = nada.
- **EX072 — Plan de seguimiento.** ¿Cómo debería asegurarse Tomás de que los cuatro hallazgos se corrigen de verdad? *Rúbrica:* 3 = responsables y fechas acordados, seguimiento, comprobación mensual, evidencia de cierre; 2 = parte; 1 = «recordárselo a la gente»; 0 = nada.

### Síntesis del capítulo

Un recorrido planificado une inventario, acceso, copias de seguridad, cambios y evidencia en correcciones priorizadas y con responsable.

### Siga estudiando — capítulo 18 de 18

[← Capítulo 17 (borrador)](#ch-17) · [Índice de capítulos del curso](../SUBJECTS.md) · [Resultados resueltos ↓](#worked-results) · [Siguiente curso a través del índice de capítulos →](../SUBJECTS.md)

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

**EX025.** Dejarla sin conectar, anotar dónde y cuándo se encontró y entregarla a seguridad o al supervisor; dejar caer memorias con etiquetas tentadoras es un truco conocido para conseguir que alguien las conecte.

**EX026.** Identificador de la memoria, nombres de los archivos, resultado del análisis, la persona que la maneja, y la fecha y la hora.

**EX027.** «Limpio» significa que el analizador no encontró malware conocido; un malware nuevo o no reconocido aún puede pasar, así que el archivo tiene menos riesgo, no es seguro, y el registro conserva un rastro por si surgen problemas.

**EX028.** Usar un portátil gestionado del emplazamiento con el software del proveedor instalado, o analizar los archivos del proveedor y llevarlos en una memoria del emplazamiento, de modo que el portátil no gestionado nunca se conecte a la línea.

**EX029.** Usar autenticación multifactor; usar contraseñas robustas para el escritorio remoto; cerrar los puertos de escritorio remoto que no se usen; auditar la actividad de las conexiones remotas.

**EX030.** Cualquiera que tenga las credenciales del proveedor puede usar un enlace permanentemente activado a cualquier hora, sin que nadie vigile, así que una contraseña robada se convierte en un camino inmediato hacia la línea.

**EX031.** Proveedor y cuenta usada, inicio a las 14:00 y fin a las 14:38, «solo se consultó el registro de averías de la envolvedora, sin cambios», cuenta desactivada, el operador confirmó el funcionamiento normal.

**EX032.** Un módem ofrece una ruta hacia la línea que se salta la pasarela, la MFA y el registro; Tomás debería fotografiarlo y notificarlo al supervisor y al ingeniero de control en lugar de desconectarlo él mismo.

**EX033.** `06:15 low-film` y `08:10 jam-cleared` son alarmas de proceso; los inicios de sesión de las 06:02 y de las 07:40–07:43 y el cambio de punto de consigna de las 07:45 son relevantes para la seguridad.

**EX034.** `failed logins: 5`: el contador aumenta con cada línea de inicio de sesión que termina en `fail`.

**EX035.** Un acierto justo después de varios fallos sugiere que la contraseña se adivinó o se encontró, y dos minutos después la misma cuenta cambió la velocidad de la envolvedora; por sí solo, un inicio de sesión de administrador podría ser simplemente un trabajo planificado.

**EX036.** A las 07:45, en PLC-WRAP, la cuenta de administrador cambió el punto de consigna de velocidad de 120 a 180; esa cuenta inició sesión a las 07:43 tras tres fallos desde las 07:40; no se conocía ningún cambio planificado.

**EX037.** Producto y modelo; versiones afectadas; qué podría hacer un atacante; si se necesita acceso de red o físico; la corrección o solución provisional del fabricante.

**EX038.** No. Solo están afectadas las versiones anteriores a la 2.2 y PLC-FILL ejecuta la 3.2; anote «no aplicable: ejecuta la 3.2» con la fecha y quién lo comprobó.

**EX039.** Actualizar el PLC exige una parada de producción, pruebas con el programa y controles de calidad, que tardan semanas en organizarse; restringir el puerto de programación en FW-1 reduce la exposición desde hoy.

**EX040.** «Se aplica: PLC-WRAP, firmware 2.0. Mitigación: FW-1 solo permite el puerto de programación desde ENG-LT. Parche a la 2.3 en la parada planificada dentro de tres semanas. Responsable: ingeniero de control. Revisar si cambia la mitigación.»

**EX041.** Los programas de PLC-FILL y PLC-WRAP, el proyecto de HMI-1, los archivos de recetas, las configuraciones de FW-1 y de los conmutadores, y los ajustes de VIS-CAM.

**EX042.** No la restaura; la etiqueta como sospechosa, notifica la discrepancia al ingeniero de control y ayuda a localizar una copia más antigua cuyo hash coincida.

**EX043.** Imprime un prefijo de hash de 12 caracteres distinto para `PLC-FILL_2026-09.bak` y `MISMATCH - do not restore`, porque cualquier cambio altera el valor SHA-256.

**EX044.** Quien pudiera modificar las copias en el mismo lugar podría reescribir también los hashes guardados para que coincidieran, y la comprobación no probaría nada.

**EX045.** Zona de la línea: PLC-WRAP; DMZ: la copia del historiador o la pasarela de acceso remoto; zona de oficinas: los PC del personal.

**EX046.** Se permite: la regla 3 coincide con el tráfico de oficina hacia cualquier equipo de la línea antes de llegar a la denegación final, así que HMI-1 es accesible desde todos los PC de oficina.

**EX047.** Los sistemas de la línea envían datos hacia un servidor de la DMZ; los usuarios de oficina solo se conectan a ese servidor, así que no hay ninguna regla que permita a los equipos de oficina iniciar conexiones hacia la zona de la línea.

**EX048.** Abrir un ticket de cambio, confirmar con el responsable de la red que nada depende de la regla 3, programar una parada planificada, conservar la configuración anterior como vuelta atrás, eliminar la regla, comprobar que funcionan la línea y los flujos hacia la DMZ, y anotar el resultado.

**EX049.** Un contador de energía inteligente conectado a la nube, una tableta del equipo de calidad y una impresora de etiquetas con wifi.

**EX050.** ¿Tiene cada dispositivo una contraseña única en lugar de una predeterminada universal? ¿Cómo les notificamos una vulnerabilidad? ¿Durante cuánto tiempo se proporcionarán actualizaciones de seguridad? ¿Está cifrada la comunicación? ¿Puede restablecerse el dispositivo y borrarse nuestros datos?

**EX051.** En una VLAN IoT dedicada cuyas reglas de cortafuegos solo permitan las direcciones de la nube del proveedor y bloqueen cualquier ruta hacia la zona de la línea, los PLC y HMI-1.

**EX052.** Marcar la impresora como «fin del soporte» en el registro con la fecha, anotar el riesgo, mantenerla aislada con el mínimo tráfico necesario y tramitar la compra de una sustituta con una fecha objetivo.

**EX053.** O el sensor o la pantalla están mal, lo que podría ser un sensor averiado o un valor manipulado; Tomás anota ambas lecturas con la hora y el supervisor lleva la llenadora a una parada segura antes de que nadie la diagnostique.

**EX054.** (a) T0843 Program Download; (b) T0886 Remote Services; (c) T0836 Modify Parameter.

**EX055.** Al principio nadie conoce la causa, y en ambos casos hay que mantener a salvo a las personas y el producto y preservar la evidencia para quien haga el diagnóstico; tratar una avería como un ataque cuesta poco, y lo contrario puede costar mucho.

**EX056.** Solo HMI-1 y ENG-LT escriben en los PLC; los inicios de sesión de administrador solo se producen durante trabajos con ticket; los programas de los PLC cambian aproximadamente una vez al mes en paradas planificadas.

**EX057.** El supervisor pone la línea en condiciones seguras; Tomás fotografía la pantalla; llama al contacto para incidentes; la restauración de HMI-1 se hace después, cuando lo decidan el responsable del incidente y el ingeniero.

**EX058.** «03:10, HMI-1 muestra un mensaje de rescate. Línea en control local, envolvedora detenida a las 03:12. No se han visto otras pantallas afectadas. No se ha desconectado nada. Supervisor de noche informado; contacto para incidentes llamado a las 03:14.»

**EX059.** Pedirle que espere al supervisor y al ingeniero: tirar del cable puede dejar sin servicio el panel del que dependen los operadores y hace perder información; el aislamiento se hace con un método planificado, como desactivar el puerto del conmutador, anotando la hora.

**EX060.** Decide el responsable del incidente junto con la dirección del emplazamiento; la cronología y las fotografías de Tomás les dan los hechos que necesitan para cumplir cualquier plazo.

**EX061.** Confirmar la contención; reconstruir HMI-1; cambiar las contraseñas; ejecutar el ciclo de prueba; calidad da su conformidad.

**EX062.** Comparar los programas de los PLC con las copias verificadas; comprobar los valores de la HMI frente a los indicadores locales; confirmar que las reglas de FW-1 coinciden con la tabla aprobada (y ejecutar un ciclo de prueba en vacío).

**EX063.** Una copia hecha el día del incidente podría contener ya los cambios o el malware del atacante, así que restaurarla reinstala el problema; use la copia más reciente verificada como anterior al compromiso.

**EX064.** «Cerrar el puerto de escritorio remoto de HMI-1 y añadir una comprobación mensual de exposición externa; responsable: responsable de la red; plazo: dos semanas.»

**EX065.** Qué cambia, por qué, en qué dispositivos, quién lo hace, cuándo, riesgo para el proceso, comprobación de éxito, método de vuelta atrás.

**EX066.** El cambio se documenta como cambio de emergencia antes de que termine el turno, se guarda una nueva copia con su hash y se actualizan el registro o los planos si algo cambió.

**EX067.** Detener la prueba, reinstalar 1.0.7 desde el archivo guardado, confirmar con paquetes de prueba que los rechazos vuelven a funcionar, anotar el intento fallido en el cambio 512 y enviar el resultado al proveedor.

**EX068.** Nadie puede saber si estaba autorizado; puede ser un cambio de un atacante, y significa que las copias y la línea base de lo normal ya no coinciden con la línea.

**EX069.** Alcance: armarios de la llenadora y de la envolvedora, zona de HMI-1, el registro de activos, las copias de seguridad y los registros de soportes y de acceso remoto; ninguna conexión a ningún dispositivo. Detenerse si aparece una alarma sin explicación, si lo piden el supervisor o los operadores, o si un armario presenta un peligro activo más allá de lo que cubre el permiso.

**EX070.** «Módem celular conectado dentro del armario de PLC-FILL (foto 3); ofrece una ruta no gestionada hacia la línea que elude FW-1 y la pasarela remota; corrección: el ingeniero de control confirma su finalidad y lo desconecta o lo sitúa detrás de la pasarela; responsable: ingeniero de control.»

**EX071.** El módem es una conexión activa y no revisada que podría alcanzar los PLC en cualquier momento, mientras que ENG-LT solo toca la línea con permiso y sus firmas pueden actualizarse antes del siguiente uso.

**EX072.** Acordar en la reunión un responsable y una fecha para cada elemento, anotarlos en la hoja de seguimiento, comprobar cada mes y cerrar cada uno solo con evidencia, como una fotografía o un registro actualizado.

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
