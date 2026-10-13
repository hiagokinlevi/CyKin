# Seguridad de TO, IoT y sistemas ciberfísicos: guía para profesionales en ejercicio

- Idioma: español neutro (`es`); curso profesional, seis meses; aproximadamente 360 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–12 de 12 tienen texto didáctico escrito a mano; los ejercicios EX001–EX060 tienen sus resultados resueltos correspondientes; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas se incluyen a partir de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4.
- Público: profesionales de seguridad de nivel inicial que se incorporan a una organización, aquí un hospital, cuyos sistemas del edificio y de las instalaciones son ciberfísicos.
- Relación con los libros vecinos: el [libro del curso rápido](../../../../rapid-1-month/ot-iot-security/en/book/MANUSCRIPT.md) es una introducción de cuatro capítulos; el [libro técnico](../../../../technical-18-months/ot-iot-security/es/book/MANUSCRIPT.md) profundiza en los procedimientos de planta. **Este libro es una guía compacta para profesionales construida sobre los sistemas del edificio.**
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado. No concede autorización para acceder a emplazamientos reales. Todos los emplazamientos, personas y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los capítulos 1–3 explican los sistemas del edificio de un hospital, la seguridad del paciente y las redes del edificio; los capítulos 4–10 tratan el inventario, las cuentas, la exposición a internet, el acceso de contratistas, la segmentación, la supervisión y los avisos; el capítulo 11 trata la respuesta a incidentes y el 12 el informe de riesgos del proyecto final. Cada capítulo tiene resultados de aprendizaje, enseñanza, un ejemplo resuelto, un caso sintético etiquetado, errores y límites, cinco ejercicios puntuados de 0 a 3, una síntesis y un bloque **Siga estudiando**. Los laboratorios de los capítulos 4, 6 y 9 solo leen datos locales (`python3 file.py`).

### Caso de estudio sintético

| Elemento | Función | Límite |
|---|---|---|
| **Millbrook Hospital Building Systems**: unidades de tratamiento de aire de quirófano AHU-OT1/2, CHILLER-1, panel de alarma de gases medicinales MGAS-PANEL, LIFT-CTRL, control de accesos DOOR-SRV, estación de trabajo BMS-WS | Hospital estudiado a lo largo del libro | Inventado |
| **Aisha Bello** | Analista de seguridad júnior en Millbrook | Inventada |

### Fuentes principales

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [serie ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Lista completa en [Referencias](#references).

## Contenido

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](../../en/book/MANUSCRIPT.md#ch-04) · [5](../../en/book/MANUSCRIPT.md#ch-05) · [6](../../en/book/MANUSCRIPT.md#ch-06) · [7](../../en/book/MANUSCRIPT.md#ch-07) · [8](../../en/book/MANUSCRIPT.md#ch-08) · [9](../../en/book/MANUSCRIPT.md#ch-09) · [10](../../en/book/MANUSCRIPT.md#ch-10) · [11](../../en/book/MANUSCRIPT.md#ch-11) · [12](../../en/book/MANUSCRIPT.md#ch-12) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Los sistemas del edificio como sistemas ciberfísicos

### Resultados de aprendizaje

Usted podrá (1) enumerar los sistemas del edificio de los que depende un hospital; (2) explicar cómo cada uno se convierte en un sistema ciberfísico en cuanto se conecta a la red; y (3) describir las consecuencias de su fallo para los pacientes.

### 1.1 Qué hace funcionar el edificio de un hospital

Detrás de las plantas de hospitalización están las unidades de tratamiento de aire que mantienen los quirófanos a una temperatura, humedad y presión controladas; las enfriadoras y las calderas; los paneles de alarma de gases medicinales que avisan cuando baja la presión de oxígeno; los ascensores que trasladan a los pacientes entre plantas; y el control de accesos de las puertas de farmacia y de maternidad. Un sistema de gestión del edificio (BMS) une muchos de ellos en una red con una estación de trabajo central.

La mayoría de estos sistemas son invisibles para los pacientes y para buena parte del personal hasta que fallan. En Millbrook incluyen las dos unidades de tratamiento de aire de los quirófanos, una enfriadora, un panel de alarma de gases medicinales, el controlador de los ascensores y el servidor de control de accesos, todos accesibles desde una sola estación de trabajo BMS. Conocer la lista es el primer paso para preguntar quién protege cada elemento.

### 1.2 Por qué son ciberfísicos

Cada sistema lee sensores y acciona equipos del mundo físico mediante controladores. En cuanto esos controladores se conectan a la red, un cambio hecho en una pantalla desde cualquier punto de la red puede mover una compuerta, detener una bomba o desbloquear una puerta. NIST SP 800-82r3 incluye expresamente la automatización de edificios dentro de la tecnología operacional precisamente por este motivo. En Millbrook, un punto de consigna tecleado en BMS-WS puede cambiar el aire de un quirófano, y un horario en DOOR-SRV decide qué puertas se abren. Ninguno de esos cambios necesita que haya alguien en una sala de máquinas. Eso es lo que convierte estos sistemas en una cuestión de seguridad: quien puede llegar a la pantalla puede llegar al equipo que hay detrás.

### 1.3 Consecuencias para los pacientes

Los fallos de la informática de oficina retrasan el trabajo. Los fallos de los sistemas del edificio pueden dañar a los pacientes: un quirófano que pierde la presión positiva arriesga una infección quirúrgica; una alarma de gases silenciada oculta una caída real; un ascensor atascado retrasa un traslado urgente. La planificación de la seguridad en un hospital empieza por preguntar qué fallo haría daño a alguien, y con qué rapidez. Escriba la respuesta para cada sistema en una frase que un profesional clínico reconozca, y anote cuánto tiempo puede aguantar el hospital antes de que el daño sea probable. Un quirófano puede aguantar minutos antes de que se cancele una sesión quirúrgica; una planta puede arreglárselas horas con llaves ante el fallo de una puerta. Esos plazos deciden después qué riesgos van primero en la planificación y en un incidente.

### 1.4 Quién es su responsable

Los sistemas del edificio suelen pertenecer a los equipos de mantenimiento e instalaciones, los mantienen contratistas y son invisibles para el personal de seguridad informática del hospital. Cerrar esa brecha, es decir, acordar quién es responsable de la seguridad de cada sistema, suele ser el primer logro práctico. En Millbrook, la primera reunión de Aisha es con el jefe de mantenimiento e instalaciones y no con el equipo de informática, porque es mantenimiento quien gestiona el BMS y quien mantiene la relación con los contratistas. El resultado que busca es una lista breve con un responsable nominal por sistema, acordada por ambas partes. Sin ella, cada hallazgo posterior corre el riesgo de pasar de un equipo a otro sin que nadie actúe.

### Ejemplo resuelto (Millbrook sintético)

Aisha Bello, recién contratada como analista de seguridad júnior en el hospital Millbrook, se reúne con el jefe de mantenimiento e instalaciones y enumera los sistemas en una pizarra con una consecuencia para cada uno. «AHU-OT1: el quirófano 1 pierde presión; cirugía aplazada o riesgo de infección.» «MGAS-PANEL: alarma de presión de oxígeno silenciada; el personal de planta no sabe que hay un fallo en el suministro.»

> **Caso sintético — Millbrook Hospital Building Systems.** El hospital, Aisha Bello y todas las cifras de este libro se han inventado con fines didácticos.

### Errores y límites

Las consecuencias deben confirmarse con el personal clínico y de mantenimiento; la suposición de un analista es solo un punto de partida.

### Ejercicios — capítulo 1

- **EX001 — Cinco sistemas.** Enumere cinco sistemas del edificio de un hospital y lo que controla cada uno. *Rúbrica:* 3 = cinco sistemas, cada uno con una función correcta; 2 = cuatro; 1 = dos; 0 = nada.
- **EX002 — Convertirse en ciberfísico.** Explique en dos frases cómo la conexión a la red convierte una unidad de tratamiento de aire en una cuestión de seguridad ciberfísica. *Rúbrica:* 3 = el controlador en red permite que una pantalla remota modifique un equipo físico; se nombra la consecuencia; 2 = un punto; 1 = vago; 0 = nada.
- **EX003 — Presión del quirófano.** ¿Por qué importa la pérdida de presión positiva en un quirófano? *Rúbrica:* 3 = entra aire sin filtrar, riesgo de infección quirúrgica, cirugía aplazada; 2 = uno; 1 = comodidad; 0 = nada.
- **EX004 — Alarma de gases silenciada.** Describa el daño si las alarmas de MGAS-PANEL se desactivan durante una caída real de presión. *Rúbrica:* 3 = el personal no se entera, los pacientes con oxígeno corren riesgo, respuesta tardía; 2 = parcial; 1 = «deja de sonar»; 0 = nada.
- **EX005 — Brecha de responsabilidad.** ¿Por qué acordar quién es responsable de la seguridad de los sistemas del edificio es un logro temprano? *Rúbrica:* 3 = la brecha entre mantenimiento, contratistas e informática deja a nadie aplicando parches ni supervisando; un responsable claro hace posible cada paso siguiente; 2 = parcial; 1 = papeleo; 0 = nada.

### Síntesis del capítulo

Los sistemas del edificio de un hospital mueven aire, gases, personas y puertas; su fallo puede dañar a los pacientes, así que su seguridad necesita un responsable.

### Siga estudiando — capítulo 01 de 12

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Seguridad del paciente, contingencia y autoridad

### Resultados de aprendizaje

Usted podrá (1) explicar por qué la seguridad clínica prevalece sobre la comodidad de la ciberseguridad; (2) describir los planes de contingencia del hospital para los sistemas del edificio; y (3) identificar quién puede autorizar cambios en las áreas clínicas.

### 2.1 Primero la seguridad clínica

Una corrección de seguridad que apaga la ventilación de un quirófano durante una cirugía es peor que el riesgo que corrige. Cada tarea de seguridad en las áreas clínicas se planifica con las personas responsables de los pacientes y se programa en función de ellas. En la práctica, esto significa preguntar al supervisor del bloque quirúrgico cuándo hay sesiones quirúrgicas antes de reservar cualquier trabajo en AHU-OT1 o AHU-OT2, y elegir un momento en que ningún paciente dependa del sistema. Un retraso de unos días para encontrar una franja segura suele ser aceptable. Un cambio de seguridad hecho con prisas durante una cirugía no lo es.

### 2.2 La contingencia ya existe

Los hospitales se preparan para los fallos del edificio con independencia de los ciberataques: oxígeno en botellas cuando falla el suministro canalizado, refrigeración portátil, llaves manuales de las puertas, procedimientos de rescate en ascensores. Estos son también el recurso alternativo cuando no se puede confiar en un sistema en red. Conocerlos permite al personal de seguridad proponer el aislamiento de un sistema sin dejar a los pacientes sin soporte. Pregunte a mantenimiento cuándo se ejercitó por última vez cada recurso alternativo y quién lo pondría en marcha de noche. Un suministro de botellas que nadie ha revisado, o unas llaves manuales que no aparecen, no son un recurso alternativo. Anotar estos planes junto a cada sistema en el inventario permite al personal de seguridad proponer el aislamiento en un incidente sabiendo qué mantendrá mientras tanto a salvo a los pacientes.

### 2.3 Autoridad

Los responsables de mantenimiento autorizan el trabajo en las instalaciones del edificio; los supervisores del bloque quirúrgico deciden cuándo está disponible un quirófano; la persona autorizada para gases medicinales controla los sistemas de gases; la seguridad informática asesora. Los contratistas trabajan con un permiso de mantenimiento. Los analistas nunca ordenan directamente a un contratista que modifique un sistema clínico. Para Aisha esto significa que cada petición pasa por la persona con autoridad. Si encuentra una contraseña débil en un controlador, lo notifica al jefe de mantenimiento, que organiza que el contratista la cambie con un permiso. Dar instrucciones directamente al contratista, aunque sea con buena intención, se salta los controles que protegen a los pacientes y no deja constancia de quién aprobó el cambio.

### 2.4 Permisos en los hospitales

El trabajo en áreas clínicas a menudo necesita la aprobación de control de infecciones además de un permiso de mantenimiento: un técnico que abre un panel del techo en un quirófano puede liberar polvo. Incluso una comprobación no invasiva puede necesitar reservar una franja horaria. Pregunte pronto qué aprobaciones necesita una tarea, porque acordar una franja para la sala de máquinas de un quirófano puede llevar días. La comprobación del firmware de Aisha necesitó un permiso de mantenimiento, la confirmación del supervisor del bloque quirúrgico y el acompañamiento de un contratista. Anote cada aprobación en el registro del trabajo y cierre el permiso cuando termine el trabajo, aunque no se haya cambiado nada.

### 2.5 Hablar con los profesionales clínicos

Explique el trabajo de seguridad en el lenguaje del riesgo para el paciente y del tiempo de quirófano. «Necesitamos una hora el sábado para que nadie pueda cambiar el aire del quirófano desde fuera» consigue el acuerdo más rápido que una lista de protocolos. Pregunte a los profesionales clínicos qué les preocuparía, como un cambio de temperatura no planificado durante una operación, y relacione el trabajo de seguridad con esa preocupación. Haga peticiones breves y concretas: qué quirófano, a qué hora, qué se hará y cómo se comprobará. Informe después del trabajo, para que la siguiente petición sea más fácil de acordar.

### Ejemplo resuelto (Millbrook sintético)

Aisha quiere leer las etiquetas de firmware de los controladores de tratamiento de aire de los quirófanos en la sala de máquinas de la cubierta. El jefe de mantenimiento emite un permiso para el sábado de 07:00 a 08:00, cuando no hay sesiones quirúrgicas; el supervisor del bloque quirúrgico lo confirma; un contratista la acompaña; no se toca ningún ajuste. Fotografía las etiquetas y el permiso se cierra a las 07:40.

> **Caso sintético — Millbrook.** El permiso y los horarios son inventados.

### Errores y límites

Los cargos locales tienen nombres distintos; aprenda la lista de su hospital. Los planes de contingencia pueden no estar probados; pregunte cuándo se ejercitaron por última vez.

### Ejercicios — capítulo 2

- **EX006 — Una corrección que daña.** Dé un ejemplo de corrección de seguridad que podría dañar a los pacientes si se programa mal. *Rúbrica:* 3 = acción concreta (p. ej., reiniciar el controlador de una AHU) con consecuencia clínica; 2 = genérica; 1 = sin consecuencia clínica; 0 = nada.
- **EX007 — Asociar la contingencia.** Asocie cada recurso de contingencia con su sistema: oxígeno en botellas, llaves manuales, refrigeración portátil. *Rúbrica:* 3 = suministro de gases, control de accesos, climatización o enfriadoras; 2 = dos; 1 = uno; 0 = nada.
- **EX008 — Quién autoriza el trabajo con gases.** ¿Quién controla el trabajo en los sistemas de gases medicinales en Millbrook? *Rúbrica:* 3 = la persona autorizada para gases medicinales, dentro de mantenimiento; 2 = solo mantenimiento; 1 = informática; 0 = nada.
- **EX009 — Control de infecciones.** ¿Por qué una comprobación de etiquetas de firmware en un quirófano podría necesitar la aprobación de control de infecciones? *Rúbrica:* 3 = abrir paneles o acceder puede liberar polvo o vulnerar la zona limpia; 2 = vago; 1 = sin motivo; 0 = nada.
- **EX010 — Propuesta de aislamiento.** ¿Cómo ayuda conocer los planes de contingencia al proponer aislar el BMS durante un incidente? *Rúbrica:* 3 = permite mostrar que los pacientes siguen atendidos mediante medios manuales o alternativos, así que el aislamiento es aceptable; 2 = parcial; 1 = irrelevante; 0 = nada.

### Síntesis del capítulo

La seguridad clínica marca los tiempos; los planes de contingencia hacen posibles las acciones de seguridad; los cargos con nombre las autorizan.

### Siga estudiando — capítulo 02 de 12

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Redes y protocolos en los sistemas del edificio

### Resultados de aprendizaje

Usted podrá (1) describir cómo se comunican los controladores del BMS; (2) explicar por qué los protocolos de los edificios suelen carecer de autenticación; y (3) identificar dónde tocan las redes del edificio la red del hospital.

### 3.1 Capas de campo y de supervisión

Los sensores y los actuadores se conectan por cable a los controladores de campo. Los controladores se comunican entre sí y con el servidor del BMS a través de una red del edificio. Entre los protocolos habituales están BACnet, transportado normalmente sobre UDP en el puerto 47808 como BACnet/IP, y Modbus/TCP para algunas instalaciones como las enfriadoras. Muchos dispositivos ofrecen además una interfaz web para su configuración. En Millbrook el BMS está en la VLAN 300, y los controladores de tratamiento de aire de los quirófanos le informan mediante BACnet/IP. La enfriadora puede usar Modbus/TCP. Anote en el inventario qué protocolo usa cada dispositivo, porque determina qué debe permitir una regla de cortafuegos y qué puede ver la supervisión.

### 3.2 Confianza por defecto

Como muchos protocolos industriales, las instalaciones clásicas de BACnet y Modbus aceptan órdenes de cualquier cosa que pueda alcanzarlas. Un portátil en la misma red normalmente puede leer todos los puntos y a menudo escribir puntos de consigna. Existen variantes seguras, pero aún no son habituales en los edificios ya instalados. Eso significa que el límite de la red es el control principal. Si un PC corporativo o el portátil de un contratista puede alcanzar la VLAN 300, probablemente pueda leer las temperaturas de los quirófanos y cambiar puntos de consigna sin contraseña. Trate cualquier camino hacia la red del edificio como un camino hacia los equipos, y diseñe las reglas partiendo de ese supuesto.

### 3.3 Dónde se encuentran las redes

La estación de trabajo del BMS puede estar en la red corporativa del hospital para que el personal de mantenimiento la alcance desde las oficinas. Los contratistas añaden acceso remoto para el soporte. Los ascensores pueden tener su propio enlace celular con el fabricante. Cada punto de encuentro es un lugar por el que un atacante presente en la red del hospital podría entrar en el control del edificio. En Millbrook el punto de encuentro más importante es BMS-WS, que está a la vez en la VLAN del edificio y en la red corporativa. Cada punto así debe figurar en una lista con su responsable y su finalidad. Los capítulos posteriores sobre acceso remoto y segmentación parten de esta lista, así que una ruta que se omita aquí también se omitirá allí.

### 3.4 Qué hace un analista

Pida al equipo de mantenimiento y al contratista un plano de red; compárelo con la configuración de los conmutadores y del cortafuegos que guarda el equipo de redes; nunca escanee los controladores del edificio para averiguarlo. Algunos controladores antiguos se bloquean con los escaneos. Anote qué fuente aportó cada dato y marque como no confirmado todo lo que solo se vea en un plano hasta que se contraste con los datos de los conmutadores o del cortafuegos. Cuando las fuentes no coincidan, pregunte al contratista y al equipo de redes a la vez. Algunas respuestas exigirán una visita a una sala de máquinas, reservada a través de mantenimiento.

### 3.5 Inalámbrico

Algunos sensores informan mediante enlaces inalámbricos a pasarelas. Pregunte dónde se conecta cada pasarela y quién gestiona sus claves. Una pasarela inalámbrica puede ser una vía de entrada a la red del edificio que no figura en ninguna lista, y puede que sus claves no se hayan cambiado nunca desde la instalación. Anote cada pasarela en el inventario con su ubicación, la red a la que se conecta, quién tiene sus claves y cuándo se cambiaron por última vez. Trate una pasarela que alcanza la VLAN 300 como parte de la zona del BMS. Pida esta lista por escrito al contratista.

### Ejemplo resuelto (Millbrook sintético)

El plano del contratista muestra el BMS en la VLAN 300, con la estación de trabajo BMS-WS conectada a dos redes: una tarjeta de red en la VLAN 300 y otra en la VLAN corporativa. Aisha anota que BMS-WS hace de puente entre la red corporativa y la del edificio (quien la comprometa alcanza todos los controladores) y la añade a su lista de riesgos.

> **Caso sintético — Millbrook.** Las VLAN y los equipos son inventados.

### Errores y límites

Los nombres de los protocolos y los puertos varían según la instalación; confírmelos con el integrador. Un plano no demuestra lo que está cableado.

### Ejercicios — capítulo 3

- **EX011 — Dos capas.** Describa las capas de campo y de supervisión de un BMS. *Rúbrica:* 3 = sensores y actuadores cableados a los controladores; controladores y servidor en la red del edificio; 2 = parcial; 1 = una; 0 = nada.
- **EX012 — Confianza en BACnet.** ¿Qué puede hacer normalmente un portátil en la VLAN 300 con los controladores BACnet/IP? *Rúbrica:* 3 = leer puntos y a menudo escribir puntos de consigna sin autenticación; 2 = solo leer; 1 = vago; 0 = nada.
- **EX013 — Estación de trabajo con dos redes.** ¿Por qué es un riesgo la segunda tarjeta de red de BMS-WS? *Rúbrica:* 3 = une la red corporativa con la del edificio eludiendo el cortafuegos; comprometerla da acceso a los controladores; 2 = parcial; 1 = velocidad; 0 = nada.
- **EX014 — Puntos de encuentro.** Nombre tres lugares donde las redes del edificio de Millbrook pueden encontrarse con otras redes. *Rúbrica:* 3 = estación de trabajo con dos redes, acceso remoto del contratista, enlace celular de los ascensores (o similar); 2 = dos; 1 = uno; 0 = nada.
- **EX015 — Sin escaneos.** Dé dos motivos por los que Aisha no escanea los controladores del edificio para cartografiarlos. *Rúbrica:* 3 = los controladores antiguos pueden bloquearse; no está autorizada o hay riesgo para las áreas clínicas; existen fuentes mejores; 2 = uno; 1 = «es lento»; 0 = nada.

### Síntesis del capítulo

Los controladores del edificio confían en quien los alcanza, así que importa cada punto donde se encuentran las redes del edificio y del hospital.

### Siga estudiando — capítulo 03 de 12

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](../../en/book/MANUSCRIPT.md#ch-04)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo para EX001–EX060. Millbrook Hospital Building Systems, Aisha Bello y todas las cifras son sintéticos. Cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación.

**EX001.** Las unidades de tratamiento de aire controlan la temperatura, la humedad y la presión de los quirófanos; las enfriadoras proporcionan agua fría; los paneles de alarma de gases medicinales avisan de fallos de presión de los gases; los controladores de los ascensores mueven las cabinas entre plantas; el control de accesos bloquea y desbloquea las puertas restringidas.

**EX002.** Cuando el controlador de la unidad de tratamiento de aire se une a la red, cualquiera que lo alcance puede cambiar las velocidades de los ventiladores o los puntos de consigna desde una pantalla lejos de la sala de máquinas. Un quirófano podría perder el control de la presión o de la temperatura sin que nadie toque la unidad.

**EX003.** La presión positiva impide que el aire sin filtrar del pasillo llegue al campo estéril; perderla aumenta el riesgo de infección del sitio quirúrgico y puede obligar a aplazar la cirugía.

**EX004.** El personal de planta no sabría que la presión de oxígeno ha bajado, así que los pacientes que dependen del oxígeno canalizado podrían sufrir daños antes de que alguien lo advirtiera y pasara a las botellas.

**EX005.** Los sistemas del edificio suelen quedar entre mantenimiento, los contratistas e informática, así que nadie aplica parches, supervisa ni revisa los accesos; nombrar un responsable hace posible cualquier control posterior.

**EX006.** Reiniciar el controlador de AHU-OT1 para cargar un parche durante una sesión quirúrgica detendría el suministro de aire y el control de presión mientras un paciente está abierto en la mesa.

**EX007.** El oxígeno en botellas respalda el suministro canalizado de gases medicinales; las llaves manuales respaldan el control de accesos electrónico; la refrigeración portátil respalda las instalaciones de climatización y las enfriadoras.

**EX008.** La persona autorizada para gases medicinales, dentro del sistema de permisos de mantenimiento, controla cualquier trabajo en los sistemas de gases medicinales, incluido el panel de alarma.

**EX009.** Llegar a algunos controladores obliga a abrir paneles del techo o de la pared dentro de una zona limpia o cerca de ella, lo que puede liberar polvo y contaminar el quirófano salvo que control de infecciones acuerde el momento y las precauciones.

**EX010.** Si las botellas, las llaves manuales y la refrigeración portátil pueden mantener seguras las plantas, Aisha puede demostrar que desconectar la red del BMS deja a los pacientes atendidos, lo que hace la decisión aceptable para los responsables clínicos.

**EX011.** En la capa de campo, los sensores y los actuadores están cableados a controladores locales; en la capa de supervisión, esos controladores se comunican entre sí y con el servidor y la estación de trabajo del BMS a través de la red del edificio.

**EX012.** Normalmente puede leer todos los puntos y a menudo escribir puntos de consigna u órdenes, porque las instalaciones clásicas de BACnet/IP no autentican al remitente.

**EX013.** BMS-WS conecta directamente la VLAN corporativa con la VLAN 300 sin pasar por un cortafuegos, así que un malware o un atacante en la estación de trabajo obtiene acceso a todos los controladores del edificio.

**EX014.** La estación BMS-WS conectada a dos redes, el enlace de acceso remoto del contratista y la conexión celular del fabricante de los ascensores.

**EX015.** Algunos controladores antiguos fallan al escanearlos, lo que podría detener la ventilación de las áreas clínicas; y los planos junto con la configuración de los conmutadores ofrecen la misma imagen sin tocar instalaciones en funcionamiento.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; vuelva a verificar las ediciones antes de citarlas. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA. Cybersecurity advisories index (ICS advisories). <https://www.cisa.gov/news-events/cybersecurity-advisories>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- ISA/IEC 62443 series of standards (overview; zones and conduits from 62443-3-2, component requirements in 62443-4-2). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS: T0883 Internet Accessible Device, T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
