# Seguridad de TO, IoT y sistemas ciberfísicos: guía para profesionales en ejercicio

- Idioma: español neutro (`es`); curso profesional, seis meses; aproximadamente 360 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Los capítulos 1–12 de 12 tienen texto didáctico escrito a mano; los ejercicios EX001–EX060 tienen sus resultados resueltos correspondientes; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas se incluyen a partir de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4.
- Público: profesionales de seguridad de nivel inicial que se incorporan a una organización, aquí un hospital, cuyos sistemas del edificio y de las instalaciones son ciberfísicos.
- Relación con los libros vecinos: el [libro del curso rápido](../../../../rapid-1-month/ot-iot-security/es/book/MANUSCRIPT.md) es una introducción de cuatro capítulos; el [libro técnico](../../../../technical-18-months/ot-iot-security/es/book/MANUSCRIPT.md) profundiza en los procedimientos de planta. **Este libro es una guía compacta para profesionales construida sobre los sistemas del edificio.**
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

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

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Un inventario de los dispositivos del edificio

### Resultados de aprendizaje

Usted podrá (1) elaborar un inventario de los dispositivos del edificio agrupado por sistema; (2) señalar los dispositivos sin soporte del fabricante; y (3) explicar cómo el estado del soporte cambia las decisiones de riesgo.

### 4.1 Qué registrar

Sistema, nombre del dispositivo, ubicación, responsable, modelo de controlador, firmware, año de instalación, dirección de red, estado del soporte del fabricante y consecuencia clínica. Las instalaciones de un edificio duran veinte años o más, así que el estado del soporte importa aquí más que en la informática de oficina. Cada campo responde a una pregunta que alguien hará. El responsable le dice a quién llamar; el firmware y el estado del soporte le dicen si existen correcciones; la dirección de red le dice qué reglas de cortafuegos se aplican; la consecuencia clínica le dice cuán urgente es un hallazgo. Un campo vacío es en sí mismo un hallazgo que hay que completar, no un hueco que ignorar.

### 4.2 Agrupación

Agrupar por sistema muestra con quién hablar: los dispositivos de climatización (HVAC) van al responsable mecánico de mantenimiento, el panel de gases a la persona autorizada para gases medicinales y el ascensor a su empresa contratista de mantenimiento.

```python
"""Lab 4: group a synthetic Millbrook building-device list by system and flag unsupported firmware."""
devices = [("AHU-OT1", "HVAC", "2019", True), ("AHU-OT2", "HVAC", "2019", True),
           ("CHILLER-1", "HVAC", "2015", False), ("MGAS-PANEL", "medical gas alarm", "2021", True),
           ("LIFT-CTRL", "elevator", "2012", False), ("DOOR-SRV", "access control", "2020", True)]
by = {}
for name, system, year, supported in devices:
    by.setdefault(system, []).append(name)
    if not supported:
        print(f"UNSUPPORTED {name:10} system={system} installed={year}")
for system, names in sorted(by.items()):
    print(f"{system:18} {len(names)} device(s): {', '.join(names)}")
```

Ejecútelo con `python3 lab_bms.py`. Salida verificada:

```text
UNSUPPORTED CHILLER-1  system=HVAC installed=2015
UNSUPPORTED LIFT-CTRL  system=elevator installed=2012
HVAC               3 device(s): AHU-OT1, AHU-OT2, CHILLER-1
access control     1 device(s): DOOR-SRV
elevator           1 device(s): LIFT-CTRL
medical gas alarm  1 device(s): MGAS-PANEL
```

La agrupación también muestra dónde una misma debilidad afecta a varios dispositivos. Los tres dispositivos de climatización pueden compartir contratista y política de contraseñas, así que un problema hallado en uno debe comprobarse en todos. El Lab 4 agrupa por sistema los seis dispositivos de Millbrook y señala los que no tienen soporte del fabricante.

### 4.3 Lectura de la salida

Dos dispositivos carecen de soporte: CHILLER-1, instalado en 2015, y LIFT-CTRL, de 2012. «Sin soporte» significa que el fabricante no publicará correcciones para debilidades nuevas. No se pueden sustituir sin más (una enfriadora cuesta una suma considerable y su sustitución requiere planificación), así que necesitan controles compensatorios: un aislamiento de red más estricto, ningún acceso remoto y una supervisión más cercana. Anote los controles compensatorios junto a cada dispositivo sin soporte en el inventario, con un responsable y una fecha, para que no se olviden. Anote también cuándo está prevista la sustitución del dispositivo, porque los controles compensatorios son un puente, no una respuesta permanente. Confirme el estado del soporte con el fabricante antes de dar por definitiva la marca del laboratorio.

### 4.4 Uso del inventario

El inventario alimenta la correspondencia con avisos de seguridad (capítulo 10), la segmentación (capítulo 8) y el informe de riesgos del proyecto final (capítulo 12). Manténgalo bajo control de acceso. Como el inventario nombra dispositivos, versiones y direcciones, también es un mapa útil para un atacante. Compártalo con quienes lo necesitan, como mantenimiento, el equipo de redes y los contratistas para sus propios sistemas, y mantenga las copias antiguas fuera del correo electrónico. Registre quién lo modificó y cuándo, para que un lector pueda confiar en su contenido. Revise cada trimestre quién tiene acceso a él.

### 4.5 De dónde salen los datos

El expediente de entrega del contratista del BMS, los registros de mantenimiento, las órdenes de compra, las tablas de los conmutadores del equipo de redes y los recorridos por las salas de máquinas contribuyen todos. Cada fuente omite algo: los expedientes de entrega son anteriores a las ampliaciones posteriores, los registros de compra omiten lo que compraron los contratistas y las salas de máquinas albergan dispositivos que nadie anotó. Compararlas, y registrar qué fuente aportó cada campo, hace que el inventario sea fiable.

En Millbrook el expediente de entrega del contratista del BMS es el punto de partida, pero las tablas de los conmutadores del equipo de redes muestran en la VLAN 300 dispositivos que el expediente omite. Los recorridos por las salas de máquinas se reservan a través de mantenimiento. Cuando las fuentes no coincidan, anote ambos valores y resuélvalos con el responsable, en lugar de elegir uno en silencio.

### 4.6 Columna de consecuencia

Escriba con palabras sencillas la consecuencia clínica de cada dispositivo, acordada con los responsables de mantenimiento y clínicos, para que las prioridades queden claras a quienes no son especialistas; como señala la sección 4.1, es el campo que indica la urgencia de un hallazgo. Por ejemplo: AHU-OT1, el quirófano 1 pierde el control de presión; MGAS-PANEL, el personal no recibe aviso de un fallo en el suministro de oxígeno; LIFT-CTRL, traslados de pacientes entre plantas con retraso. La columna determina después el orden del trabajo en el informe de riesgos, así que su redacción debe ser clara para directivos que nunca han visto las instalaciones. Revise la redacción cada año.

### Ejemplo resuelto (Millbrook sintético)

Aisha lleva los dos dispositivos sin soporte al jefe de mantenimiento e instalaciones. Acuerdan lo siguiente: CHILLER-1 se coloca tras una regla de cortafuegos dedicada que solo permite BMS-WS, y el enlace celular de LIFT-CTRL se revisa con el contratista del ascensor. Ambos se añaden al plan de inversiones de sustitución con años objetivo.

> **Caso sintético — Millbrook.** Los dispositivos y los años son inventados.

### Errores y límites

El estado del soporte debe confirmarse con el fabricante; el año de instalación por sí solo es un indicio. Los inventarios envejecen; revíselos cada trimestre.

### Ejercicios — capítulo 4

- **EX016 — Campos del inventario.** Enumere seis campos de un inventario de dispositivos del edificio. *Rúbrica:* 3 = seis campos correctos, incluidos el estado del soporte y la consecuencia; 2 = cuatro; 1 = dos; 0 = nada.
- **EX017 — Ampliar el laboratorio.** Añada `("BOILER-2", "HVAC", "2010", False)`. ¿Qué líneas nuevas imprime el laboratorio? *Rúbrica:* 3 = `UNSUPPORTED BOILER-2   system=HVAC installed=2010` y HVAC con 4 dispositivos; 2 = una línea; 1 = incorrecto; 0 = nada.
- **EX018 — Qué significa sin soporte.** Explique al jefe de mantenimiento e instalaciones qué significa «sin soporte» para CHILLER-1. *Rúbrica:* 3 = no habrá correcciones del fabricante para fallos nuevos; el riesgo crece; compensar y planificar la sustitución; 2 = parcial; 1 = «averiado»; 0 = nada.
- **EX019 — Controles compensatorios.** Proponga tres controles compensatorios para LIFT-CTRL. *Rúbrica:* 3 = aislamiento, retirar o restringir el enlace celular, supervisión, plan de sustitución; 2 = dos; 1 = uno; 0 = nada.
- **EX020 — A quién llamar.** Según la agrupación, ¿quién recibe la entrada de MGAS-PANEL? *Rúbrica:* 3 = la persona autorizada para gases medicinales; 2 = mantenimiento; 1 = informática; 0 = nada.

### Síntesis del capítulo

Un inventario agrupado por sistema y con el estado del soporte muestra a los responsables y dónde los controles compensatorios deben soportar el riesgo.

### Siga estudiando — capítulo 04 de 12

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Cuentas, valores por defecto y configuraciones de referencia de los dispositivos

### Resultados de aprendizaje

Usted podrá (1) encontrar cuentas por defecto y compartidas en los sistemas del edificio; (2) aplicar las ideas de ETSI EN 303 645 y NIST IR 8259 a las compras; y (3) fijar normas prácticas de contraseñas para el personal de mantenimiento.

### 5.1 Valores por defecto en los edificios

Los controladores y las interfaces web a menudo salen de fábrica con nombres de usuario y contraseñas documentados. Los integradores a veces mantienen una misma contraseña en todos los centros que atienden. Ambas cosas significan que cualquiera que haya leído un manual o haya trabajado para ese integrador puede iniciar sesión. En Millbrook, la interfaz web de DOOR-SRV aún aceptaba la contraseña de fábrica que figura en su manual público. Una comprobación de valores por defecto debe abarcar todos los controladores e interfaces web del inventario, hecha por el contratista o con él durante una franja reservada, sin probar contraseñas por su cuenta contra sistemas en funcionamiento. Registre cada resultado y la fecha en que se comprobó.

### 5.2 Cuentas compartidas de mantenimiento

La estación de trabajo del BMS puede tener un único inicio de sesión que usan todos los ingenieros de turno. Eso hace que los cambios no se puedan rastrear. Las cuentas individuales, aunque solo existan en el servidor del BMS, permiten que el registro de tendencias nombre a la persona que cambió un punto de consigna. Las cuentas nominativas también ayudan cuando algo sale mal. Si un punto de consigna de un quirófano cambia de noche, un inicio de sesión compartido no puede decir quién hizo el cambio, mientras que uno nominativo sí, como muestra la revisión de tendencias del capítulo 9. Cuando un controlador solo admita una cuenta, guarde la contraseña en el almacén de secretos y registre cada uso con el nombre del ingeniero.

### 5.3 Una configuración de referencia para las compras

ETSI EN 303 645 exige, entre otras disposiciones, que no haya contraseñas por defecto universales, una política de divulgación de vulnerabilidades, actualizaciones de software y comunicación segura; NIST IR 8259 enumera actividades fundamentales que deberían realizar los fabricantes. El departamento de compras del hospital puede convertirlas en preguntas contractuales para los nuevos dispositivos del edificio, de modo que el problema se reduzca con el tiempo. Para cada nuevo dispositivo del edificio, pregunte por escrito al proveedor: ¿tiene cada unidad una contraseña única?, ¿existe una vía publicada para notificar vulnerabilidades?, ¿durante cuánto tiempo se ofrecerán actualizaciones? y ¿está protegida la comunicación? Guarde las respuestas con el registro de compra. Un proveedor que no sabe responder es en sí mismo información útil para el comprador.

### 5.4 Normas que el personal de mantenimiento pueda seguir

Contraseñas únicas por dispositivo guardadas en un almacén de contraseñas gestionado; cuentas nominativas en el BMS; derechos de administración solo para trabajos planificados; contraseñas cambiadas cuando se marcha personal de un contratista. Escriba las normas en una página, acordadas con el jefe de mantenimiento e instalaciones, y compruebe que el almacén está disponible en los turnos que lo necesitan. Cuando una norma sea difícil de cumplir, como cambiar las contraseñas cada vez que se marcha personal de un contratista, acuerde cómo se enterará el hospital de la marcha. Revise las normas después de cualquier incidente en el que haya intervenido una cuenta.

### 5.5 Comprobar que el cambio funcionó

Después de cambiar una contraseña, pruebe la antigua desde la estación de trabajo del BMS en la misma franja reservada para confirmar que falla, y confirme que los operadores aún pueden iniciar sesión con el nuevo esquema. Registre ambos resultados en el ticket de cambio. Si la contraseña antigua sigue funcionando, el cambio no ha surtido efecto, quizá porque el dispositivo tiene más de una cuenta o interfaz. Si los operadores no pueden iniciar sesión con el nuevo esquema, puede que vuelvan a una contraseña compartida, lo que deshace el trabajo; resuelva el problema de acceso en la misma franja.

### Ejemplo resuelto (Millbrook sintético)

Aisha y el contratista del BMS revisan DOOR-SRV, el servidor de control de accesos. Su interfaz web aún acepta la contraseña de fábrica que figura en el manual público. El contratista la cambia durante una franja reservada, la registra en el almacén del hospital y crea cuentas nominativas para los tres vigilantes de seguridad que gestionan los horarios de las puertas.

> **Caso sintético — Millbrook.** El dispositivo y las cuentas son inventados.

### Errores y límites

ETSI EN 303 645 se dirige al IoT de consumo; para los controladores de edificio de grado industrial, los requisitos de componentes de IEC 62443-4-2 encajan mejor. Algunos controladores antiguos solo admiten una cuenta.

### Ejercicios — capítulo 5

- **EX021 — Por qué importan las contraseñas del integrador.** Explique el riesgo de una contraseña del integrador reutilizada en muchos hospitales. *Rúbrica:* 3 = una filtración o un antiguo empleado abre todos los centros; 2 = parcial; 1 = vago; 0 = nada.
- **EX022 — Cambios rastreables.** ¿Cómo ayudan las cuentas nominativas del BMS tras un cambio inesperado de un punto de consigna? *Rúbrica:* 3 = el registro de tendencias o de auditoría muestra quién lo cambió; apoya la investigación; 2 = parcial; 1 = vago; 0 = nada.
- **EX023 — Preguntas contractuales.** Convierta tres disposiciones de ETSI EN 303 645 en preguntas para un contrato de compra. *Rúbrica:* 3 = tres preguntas precisas (valores por defecto, divulgación, actualizaciones o cifrado); 2 = dos; 1 = una; 0 = nada.
- **EX024 — Baja en el contratista.** Un ingeniero del contratista que conocía contraseñas de Millbrook deja la empresa. ¿Qué ocurre? *Rúbrica:* 3 = cambiar en el almacén las contraseñas afectadas, revisar los accesos, registrarlo; 2 = algo; 1 = vago; 0 = nada.
- **EX025 — La norma adecuada.** ¿Qué norma encaja mejor que ETSI EN 303 645 para un controlador industrial de BMS, y por qué? *Rúbrica:* 3 = IEC 62443-4-2; requisitos de componentes para la automatización industrial; 2 = solo el nombre; 1 = incorrecto; 0 = nada.

### Síntesis del capítulo

Los valores por defecto cambiados, las cuentas nominativas, las contraseñas en el almacén y las preguntas contractuales de referencia cierran las puertas más fáciles.

### Siga estudiando — capítulo 05 de 12

[← Capítulo 04 (borrador)](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 (borrador) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Exposición a internet de los sistemas del edificio

### Resultados de aprendizaje

Usted podrá (1) explicar por qué las interfaces del edificio acaban en internet; (2) comparar una exportación de exposición con una lista aprobada; y (3) responder a una exposición no aprobada.

### 6.1 Cómo ocurre

Un contratista abre un puerto para alcanzar desde casa la página web del BMS; una empresa de ascensores añade un enrutador; una regla de cortafuegos de un proyecto nunca se retira. MITRE ATT&CK for ICS recoge la técnica T0883 Internet Accessible Device precisamente para esta situación, y los avisos de CISA instan una y otra vez a retirar las interfaces de los sistemas de control del acceso directo desde internet. En Millbrook, una regla añadida en 2023 para la puesta en marcha de la enfriadora expuso directamente a internet BACnet y el inicio de sesión web del BMS, y nadie la retiró tras el proyecto. Toda apertura de este tipo empieza con una petición razonable por comodidad. La tarea consiste en dar a los contratistas una vía con soporte para que no necesiten pedir puertos.

### 6.2 Comprobar la exposición

El equipo de redes del hospital, o un servicio autorizado, elabora una lista de las direcciones públicas del hospital y de los servicios abiertos. El analista la compara con la lista aprobada, que normalmente contiene solo la pasarela de acceso remoto.

```python
"""Lab 6: compare a synthetic external-exposure export with approved internet-facing services."""
approved = {("203.0.113.10", 443)}
found = [("203.0.113.10", 443, "VPN gateway"), ("203.0.113.24", 47808, "BACnet/IP"),
         ("203.0.113.24", 80, "BMS web login")]
for ip, port, svc in found:
    print(f"{ip}:{port:<6} {svc:14} {'approved' if (ip, port) in approved else 'NOT APPROVED - report'}")
print("unapproved:", sum((ip, port) not in approved for ip, port, _ in found))
```

Ejecútelo con `python3 lab_exposure.py`. Salida verificada:

```text
203.0.113.10:443    VPN gateway    approved
203.0.113.24:47808  BACnet/IP      NOT APPROVED - report
203.0.113.24:80     BMS web login  NOT APPROVED - report
unapproved: 2
```

Obtenga la exportación de quienes son dueños de las direcciones, y no sondee usted mismo las direcciones del hospital salvo que el equipo de redes lo haya autorizado. La lista aprobada debe ser corta y nombrar un responsable para cada entrada. El Lab 6 compara la exportación de Millbrook con una lista aprobada que solo contiene la pasarela VPN.

### 6.3 Lectura del resultado

La pasarela VPN en 203.0.113.10, puerto 443, está aprobada. La dirección 203.0.113.24 expone BACnet/IP en el 47808 y un inicio de sesión web del BMS en el 80. Ninguno de los dos está aprobado: cualquiera en internet podría intentar leer u ordenar a los controladores, o adivinar la contraseña web. La exposición importa más por lo que hay detrás. BACnet acepta órdenes de cualquiera que pueda alcanzarlo, así que no es solo una fuga de datos sino una vía hacia los ajustes del aire de los quirófanos y de la enfriadora. Esa combinación la sitúa en lo más alto del informe del analista al equipo de redes y a mantenimiento.

### 6.4 Respuesta

Informe de inmediato al equipo de redes y a mantenimiento; pida al responsable de la red que cierre la exposición mediante un cambio de emergencia; revise los registros en busca de conexiones desde el exterior; averigüe quién la abrió y por qué, y ofrézcale en su lugar una vía con soporte. Guarde la exportación, las horas y los extractos de registro con el informe, porque muestran cuánto duró la exposición y si alguien la usó. En Millbrook, los registros del cortafuegos mostraron muchos intentos externos de alcanzar el puerto 47808 en los últimos meses. Ese hallazgo se traslada a mantenimiento para que compruebe los ajustes de los controladores y los registros de tendencias en busca de cambios en el mismo periodo.

### 6.5 Evitar que se repita

Añada una comprobación mensual de exposición al calendario del equipo de redes, exija una fecha de fin en toda regla de cortafuegos abierta para un proyecto y haga que los contratistas soliciten el acceso remoto mediante el proceso de la pasarela en lugar de pedir puertos. Cada medida cierra una causa. La comprobación mensual detecta lo que se escapa; las fechas de fin hacen que las reglas de proyecto caduquen; el proceso de la pasarela da a los contratistas una vía que no necesita puertos abiertos. Lleve el seguimiento de la comprobación mensual en el registro con la fecha y el resultado, para que un mes omitido quede a la vista.

### Ejemplo resuelto (Millbrook sintético)

El equipo de redes rastrea 203.0.113.24 hasta una regla de cortafuegos añadida en 2023 para un proyecto de puesta en marcha de la enfriadora. La retiran en menos de una hora; los registros del cortafuegos muestran muchos intentos de conexión externos al puerto 47808 en los últimos meses. Al contratista se le dan cuentas en la pasarela en su lugar.

> **Caso sintético — Millbrook.** Las direcciones pertenecen al rango de documentación 203.0.113.0/24 y los hechos son inventados.

### Errores y límites

Las listas de exposición son instantáneas; repítalas cada mes. Pruebe solo direcciones que pertenezcan a su organización, por medios autorizados.

### Ejercicios — capítulo 6

- **EX026 — Cómo se produce la exposición.** Describa dos formas en que una interfaz del BMS llega a ser accesible desde internet. *Rúbrica:* 3 = dos vías concretas (puerto del contratista, regla olvidada, enrutador del fabricante); 2 = una; 1 = vago; 0 = nada.
- **EX027 — Tercer hallazgo.** Si la exportación encontrara también 203.0.113.10 en el puerto 22, ¿qué imprimiría el laboratorio para ese hallazgo y para el total? *Rúbrica:* 3 = una línea NOT APPROVED y `unapproved: 3`; 2 = una de las dos; 1 = aprobado; 0 = nada.
- **EX028 — Nombre de la técnica.** ¿Qué técnica de ATT&CK for ICS describe la situación de 203.0.113.24? *Rúbrica:* 3 = T0883 Internet Accessible Device; 2 = solo el nombre; 1 = incorrecto; 0 = nada.
- **EX029 — Pasos de respuesta.** Enumere los pasos de respuesta tras encontrar una exposición no aprobada. *Rúbrica:* 3 = informar, cierre de emergencia por el responsable, revisar registros, averiguar la causa, ofrecer una alternativa segura; 2 = tres; 1 = uno; 0 = nada.
- **EX030 — Límite de las pruebas.** ¿Por qué Aisha no prueba las direcciones de otros hospitales «para comparar»? *Rúbrica:* 3 = no está autorizada, puede ser ilegal, podría causar interrupciones; 2 = uno; 1 = no pasa nada; 0 = nada.

### Síntesis del capítulo

Solo la pasarela da a internet; cualquier otra cosa que se encuentre se notifica, se cierra y se sustituye por una vía con soporte.

### Siga estudiando — capítulo 06 de 12

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Acceso remoto de contratistas y fabricantes

### Resultados de aprendizaje

Usted podrá (1) inventariar todas las vías remotas hacia los sistemas del edificio; (2) aplicar las lecciones de CISA AA21-042A; y (3) diseñar un proceso de acceso remoto controlado para los contratistas.

### 7.1 Muchas manos

Un hospital puede tener contratistas distintos para el BMS, las enfriadoras, los ascensores, las alarmas de incendio y el control de accesos, y cada uno quiere soporte remoto. Sin una política, cada uno instala su propia vía: una herramienta de escritorio remoto en la estación de trabajo, un enrutador, un módem celular. En Millbrook Aisha encontró cuatro vías distintas, tres de ellas instaladas por contratistas para su propia comodidad. Ninguna era maliciosa, pero cada una era una entrada que el hospital no controlaba. La primera tarea es enumerar todas las vías, con quién las instaló, qué alcanzan y si alguien las sigue usando.

### 7.2 Lecciones de AA21-042A

El aviso de CISA sobre el compromiso en 2021 de una instalación de tratamiento de agua de EE. UU. describe cómo se usó software de acceso remoto para alcanzar un sistema de control. Entre sus recomendaciones están la autenticación multifactor, contraseñas robustas para el escritorio remoto, el cierre de los puertos de escritorio remoto sin uso y la auditoría de las conexiones remotas. MITRE ATT&CK for ICS describe el uso indebido de estas vías como T0886 Remote Services. En Millbrook las lecciones se aplican directamente a las vías que encontró Aisha. Una herramienta de escritorio remoto en BMS-WS es el mismo tipo de vía que describe el aviso. Exigir autenticación multifactor, auditar las conexiones y cerrar el acceso por escritorio remoto sin uso son pasos prácticos que mantenimiento y los contratistas pueden acordar sin esperar a un proyecto mayor.

### 7.3 Un proceso controlado

Una única pasarela de acceso remoto propiedad del hospital; una cuenta nominativa y con autenticación multifactor para cada ingeniero del contratista; cuentas desactivadas por defecto y activadas por ticket; acceso limitado al sistema concreto que mantiene el contratista; sesiones grabadas cuando sea posible; la cuenta desactivada al terminar la sesión. Escriba el proceso en un documento breve que firmen los contratistas, para que sepan cómo obtener acceso tanto en una emergencia como para el trabajo planificado. Pruébelo una vez con cada contratista antes de retirar las vías antiguas. Revise las cuentas de la pasarela cada semana, porque las cuentas que quedan activadas tras una sesión son en sí mismas un hallazgo, como muestra después el informe de riesgos de Millbrook.

### 7.4 Retirar las vías antiguas

Una vez que la pasarela esté en servicio, retire las herramientas de escritorio remoto instaladas directamente en las estaciones de trabajo del edificio y desconecte los módems no gestionados, de acuerdo con el contratista y con mantenimiento, en un momento planificado, para que no se pierda el soporte durante una emergencia. En Millbrook el orden se acordó con mantenimiento: la herramienta de escritorio remoto se retiró solo después de que funcionara la cuenta del contratista del BMS en la pasarela, el enrutador de la enfriadora una semana después, y el enlace del ascensor se restringió en lugar de retirarse. Registre cada retirada con la fecha y quién la confirmó, y vuelva a comprobar después el inventario de vías para asegurarse de que nada ha reaparecido.

### Ejemplo resuelto (Millbrook sintético)

El inventario de vías de Aisha encuentra cuatro entradas: la pasarela, una herramienta de escritorio remoto en BMS-WS instalada por el contratista del BMS, el enlace celular del ascensor y el enrutador de un fabricante de enfriadoras. Mantenimiento acuerda un plan: la herramienta de escritorio remoto se retira en la semana 1, después de que funcione la cuenta del contratista en la pasarela; el enrutador de la enfriadora, en la semana 2; el enlace del ascensor se restringe al centro de servicio del contratista del ascensor y exige un ticket.

> **Caso sintético — Millbrook.** Las vías y los plazos son inventados.

### Errores y límites

Algunos enlaces de ascensores y de alarmas de incendio son necesarios para la supervisión de la seguridad; restrínjalos y regístrelos en lugar de retirarlos a ciegas.

### Ejercicios — capítulo 7

- **EX031 — Contar las vías.** Enumere las cuatro vías remotas que encontró Aisha. *Rúbrica:* 3 = pasarela, escritorio remoto en BMS-WS, enlace celular del ascensor, enrutador de la enfriadora; 2 = tres; 1 = una; 0 = nada.
- **EX032 — Aplicar el aviso.** Aplique dos recomendaciones de AA21-042A al acceso del contratista del BMS. *Rúbrica:* 3 = MFA en la cuenta de la pasarela y auditoría de las sesiones (o cerrar el puerto RDP o contraseña robusta); 2 = una; 1 = vago; 0 = nada.
- **EX033 — Límites por sistema.** ¿Por qué la cuenta del contratista de la enfriadora no debe alcanzar el servidor de control de accesos? *Rúbrica:* 3 = mínimo privilegio; el compromiso de un contratista queda limitado a su sistema; 2 = parcial; 1 = sin motivo; 0 = nada.
- **EX034 — Momento de la retirada.** ¿Por qué la herramienta de escritorio remoto se retira solo después de que funcione la cuenta de la pasarela? *Rúbrica:* 3 = evitar perder el soporte durante una emergencia; probar antes el sustituto; 2 = parcial; 1 = sin motivo; 0 = nada.
- **EX035 — Enlace de seguridad.** El enlace de supervisión de la alarma de incendios usa un módem celular. ¿Debe desconectarse? *Rúbrica:* 3 = no; supervisión de la seguridad; restringir, documentar y revisar con el responsable; 2 = solo «no»; 1 = sí; 0 = nada.

### Síntesis del capítulo

Toda ayuda remota pasa por una única pasarela con cuentas nominativas, con autenticación multifactor y asociadas a un ticket; las vías heredadas se retiran con cuidado.

### Siga estudiando — capítulo 07 de 12

[← Capítulo 06 (borrador)](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 (borrador) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Segmentación de las redes del edificio

### Resultados de aprendizaje

Usted podrá (1) definir zonas y conductos para los sistemas del edificio de Millbrook con la terminología de IEC 62443; (2) redactar un conjunto mínimo de reglas; y (3) planificar la migración sin perturbar las áreas clínicas.

### 8.1 Zonas

IEC 62443-3-2 describe cómo agrupar los activos en zonas con requisitos de seguridad similares y conectarlas mediante conductos. En Millbrook un comienzo sensato es: una zona del BMS (controladores y servidor del BMS), una zona relevante para la seguridad (alarma de gases medicinales y ascensor, cada uno por separado), una zona de control de accesos, una DMZ para la pasarela y las exportaciones de datos, y la zona corporativa. Anote cada zona con sus miembros, su responsable y la consecuencia si se compromete. Las alarmas de gases medicinales y los ascensores se mantienen en zonas separadas porque sus fallos importan para la seguridad de los pacientes y sus contratistas son distintos. Un diagrama de zonas que acepten tanto mantenimiento como el equipo de redes es el punto de partida de cualquier tabla de reglas.

### 8.2 Conductos y reglas

Escriba cada conducto como un pequeño conjunto de reglas: de BMS-WS (trasladada a la zona del BMS) a los controladores por BACnet/IP; de la pasarela a BMS-WS para las sesiones de los contratistas; del servidor del BMS a un servidor de datos en la DMZ para los informes de energía. Todo lo demás se deniega. Los PC corporativos nunca se conectan directamente a los controladores. Escriba cada regla con su origen, destino, protocolo y puerto, un motivo y un responsable, para que pueda revisarse más adelante. Contraste las reglas con el inventario de vías, para que no se bloquee nada aprobado ni quede nada sin aprobar. Una regla sin responsable debe tratarse como candidata a retirarse.

### 8.3 Corregir la estación de trabajo conectada a dos redes

Retirar la tarjeta de red corporativa de BMS-WS cierra el puente del capítulo 3. El personal de mantenimiento que necesite ver el BMS desde las oficinas usa un panel de solo lectura en el servidor de la DMZ, o un servidor de salto al que se llega a través de la pasarela. Antes de retirar la tarjeta, acuerde con mantenimiento qué tareas de oficina la usaban y pruebe la vía sustituta con el personal que la usará. Haga el cambio en una franja reservada y confirme después que BMS-WS sigue alcanzando sus controladores. Registre el cambio en la entrada de la lista de riesgos que Aisha creó al encontrar el puente.

### 8.4 Migrar con seguridad

Cambie un conducto cada vez, en momentos acordados con mantenimiento y con los supervisores del bloque quirúrgico; vigile si se pierden puntos en el BMS después de cada paso; tenga lista la configuración anterior para restaurarla. Acuerde de antemano qué puntos del BMS se comprobarán después de cada paso y quién los comprobará. En Millbrook, después del segundo paso dos controladores dejaron de informar porque se había olvidado un conducto hacia un servidor de hora; se detectó porque los puntos se comprobaron de inmediato. Anote estas sorpresas en la tabla de reglas para que el siguiente cambio las evite.

### 8.5 Documentación

Publique el diagrama de zonas y la tabla de reglas con números de revisión y responsables, para que los contratistas puedan solicitar cambios sobre ellos. Guarde el diagrama y la tabla en un lugar que puedan leer mantenimiento, el equipo de redes y los contratistas, y cítelos en cada solicitud de cambio. Cuando se haga un cambio, actualice el número de revisión y anote quién lo aprobó. Una documentación desactualizada lleva a los contratistas a pedir reglas que ya existen o que contradicen el diseño. Conserve las revisiones superadas para poder rastrear las decisiones pasadas.

### Ejemplo resuelto (Millbrook sintético)

A lo largo de tres mañanas de sábado planificadas, el equipo de redes crea las zonas, traslada BMS-WS por completo a la zona del BMS y despliega las reglas. Después del paso 2, dos controladores dejan de informar; la causa es un conducto olvidado hacia un servidor de hora, que se añade dentro del mismo cambio. Los informes de energía salen ahora del servidor de la DMZ.

> **Caso sintético — Millbrook.** Los pasos y los hallazgos son inventados.

### Errores y límites

La segmentación no detiene a un atacante que ya tiene credenciales de la pasarela; limita adónde puede ir. Los diseños de zonas deben revisarse cuando se añaden sistemas.

### Ejercicios — capítulo 8

- **EX036 — Lista de zonas.** Proponga cinco zonas para Millbrook. *Rúbrica:* 3 = BMS, relevante para la seguridad (gases y ascensor), control de accesos, DMZ, corporativa; 2 = cuatro; 1 = dos; 0 = nada.
- **EX037 — Redactar un conducto.** Escriba la regla que permite al servidor del BMS enviar datos de energía al servidor de la DMZ. *Rúbrica:* 3 = origen servidor del BMS, destino servidor de datos de la DMZ, puerto concreto, permitir; más denegación por defecto; 2 = sin denegación; 1 = cualquiera; 0 = nada.
- **EX038 — Visualización desde la oficina.** ¿Cómo ve el BMS desde sus oficinas el personal de mantenimiento después de que BMS-WS pierda su tarjeta corporativa? *Rúbrica:* 3 = panel de solo lectura en la DMZ o servidor de salto a través de la pasarela; 2 = parcial; 1 = volver a poner la tarjeta; 0 = nada.
- **EX039 — Puntos perdidos.** Dos controladores dejan de informar tras un cambio de reglas. ¿Cuál es la respuesta segura? *Rúbrica:* 3 = comprobar el impacto clínico, restaurar la configuración anterior si hace falta, encontrar el conducto que falta, corregirlo dentro del cambio; 2 = parcial; 1 = ignorarlo; 0 = nada.
- **EX040 — Límite de la segmentación.** ¿Contra qué no protege la segmentación? *Rúbrica:* 3 = uso indebido de credenciales legítimas de la pasarela o de un interno dentro de los conductos permitidos; 2 = vago; 1 = todo protegido; 0 = nada.

### Síntesis del capítulo

Las zonas con conductos estrechos impiden que los compromisos de la oficina alcancen los controladores; migre un conducto cada vez.

### Siga estudiando — capítulo 08 de 12

[← Capítulo 07 (borrador)](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 (borrador) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Supervisión de tendencias y registros

### Resultados de aprendizaje

Usted podrá (1) usar los registros de tendencias del BMS como evidencia de seguridad; (2) señalar con un script breve los cambios fuera de las ventanas aprobadas; y (3) combinar evidencias de tendencias, de inicios de sesión y de red.

### 9.1 Las tendencias como evidencia

Un BMS registra valores a lo largo del tiempo (temperaturas, puntos de consigna, posiciones de válvulas), sobre todo para los ingenieros. Esos mismos registros muestran cuándo cambió un punto de consigna y, con cuentas nominativas, quién lo cambió. A menudo son la mejor evidencia de una manipulación en un sistema del edificio. Para Aisha, el registro de tendencias suele ser el primer lugar donde mirar cuando algo parece ir mal, porque muestra directamente el efecto físico. Averigüe con qué frecuencia se muestrea cada punto y cuánto tiempo se conservan los registros antes de confiar en ellos. Donde las cuentas son compartidas, la tendencia muestra qué cambió pero no quién lo cambió.

### 9.2 Ventanas de cambio

Mantenimiento acuerda ventanas para los cambios planificados de puntos de consigna, por ejemplo las mañanas de los días laborables. Un cambio fuera de una ventana no es necesariamente malicioso, pero necesita una explicación.

```python
"""Lab 9: flag operating-theatre temperature setpoint changes outside a synthetic change window."""
trend = [("01:00", 20.0), ("02:00", 20.0), ("03:00", 26.0), ("04:00", 26.0), ("09:00", 21.0)]
window = ("08:00", "10:00")
prev = None
for t, sp in trend:
    if prev is not None and sp != prev:
        inside = window[0] <= t <= window[1]
        print(f"{t} setpoint {prev}->{sp} {'in window' if inside else 'OUTSIDE WINDOW - review'}")
    prev = sp
```

Ejecútelo con `python3 lab_trend.py`. Salida verificada:

```text
03:00 setpoint 20.0->26.0 OUTSIDE WINDOW - review
09:00 setpoint 26.0->21.0 in window
```

Las ventanas deben acordarse con mantenimiento y ponerse por escrito, con las excepciones que haya, como las reparaciones de emergencia. Fuera de la ventana, la pregunta es simplemente qué ocurrió y quién lo hizo. El Lab 9 comprueba la tendencia de un punto de consigna de un quirófano frente a una ventana de mañana y señala cualquier cambio fuera de ella. Revise las ventanas con mantenimiento cada año.

### 9.3 Lectura de la salida

A las 03:00 el punto de consigna del quirófano subió de 20 °C a 26 °C, fuera de la ventana de 08:00 a 10:00; a las 09:00 volvió a fijarse en 21 °C, dentro de la ventana. El cambio de las 03:00 es el que hay que revisar. La vuelta a 21 °C a las 09:00 está dentro de la ventana, pero aun así merece anotarse, porque sugiere que alguien advirtió el cambio anterior y lo corrigió. Ambos cambios entran en la revisión, con las preguntas de quién hizo cada uno y por qué. El laboratorio muestra solo el punto de consigna; la tendencia de la temperatura real del quirófano mostraría si el cambio tuvo consecuencias.

### 9.4 Combinar fuentes

Compruebe en el registro de auditoría del BMS quién tenía la sesión iniciada a las 03:00; en el registro de la pasarela, las sesiones remotas; en el registro del cortafuegos, las conexiones a la zona del BMS. La coincidencia entre fuentes refuerza la conclusión, sea cual sea. Anote lo que mostró cada fuente, incluidas las que no mostraron nada. En Millbrook el registro de la pasarela no tenía sesiones a las 03:00, lo que hacía improbable un cambio remoto, y el registro de auditoría del BMS nombraba al ingeniero de noche. El registro del cortafuegos también se habría comprobado si las dos primeras fuentes no hubieran coincidido.

### 9.5 Alertas

Donde el BMS lo permita, genere una alarma para los cambios de puntos de consigna fuera de las ventanas en las unidades críticas, enviada al ingeniero de guardia de mantenimiento. Acuerde con mantenimiento qué unidades cuentan como críticas, como las unidades de tratamiento de aire de los quirófanos, y qué debe hacer el ingeniero de guardia al recibir la alarma. Una alarma a la que nadie responde pronto se ignora. Pruébela una vez después de configurarla, durante un cambio planificado, y registre el resultado. Revise la lista de alarmas cada trimestre con los ingenieros de guardia, retirando las unidades que ya no la necesiten.

### 9.6 Conservar la evidencia

Cuando un cambio necesite revisión, exporte ese mismo día los registros de tendencias y de auditoría pertinentes, anote la hora de la exportación y guárdelos con las notas de la revisión; la retención del BMS suele ser corta. Guarde las exportaciones donde solo puedan leerlas las personas que revisan el cambio, con una nota sobre la procedencia de cada una. En Millbrook los registros de tendencias se conservaban solo 14 días, lo que más tarde se convirtió en un hallazgo del informe de riesgos de Aisha. Mientras no se amplíe la retención, exportar el mismo día es la única práctica segura.

### Ejemplo resuelto (Millbrook sintético)

Aisha comprueba los registros: no hay sesiones en la pasarela a las 03:00, pero el registro de auditoría del BMS muestra que el ingeniero de noche subió el punto de consigna durante una avería de la enfriadora para reducir la carga, y olvidó anotarlo. La explicación se documenta, y el procedimiento de guardia gana un paso: anotar en el registro del turno cualquier cambio fuera de ventana.

> **Caso sintético — Millbrook.** La tendencia y la explicación son inventadas.

### Errores y límites

Los registros de tendencias pueden muestrear con poca frecuencia y omitir cambios breves; los relojes deben estar sincronizados. La retención puede ser de solo unas semanas: exporte lo que necesite.

### Ejercicios — capítulo 9

- **EX041 — Lógica de la ventana.** ¿Por qué no se señala el cambio de las 09:00? *Rúbrica:* 3 = las 09:00 caen dentro de la ventana de 08:00 a 10:00; 2 = «está permitido»; 1 = incorrecto; 0 = nada.
- **EX042 — Tendencia modificada.** Si la ventana fuera de 02:00 a 04:00, ¿qué imprimiría el laboratorio? *Rúbrica:* 3 = 03:00 `in window`, 09:00 `OUTSIDE WINDOW - review`; 2 = una; 1 = lo mismo; 0 = nada.
- **EX043 — Tres fuentes.** ¿Qué tres registros combina Aisha con la tendencia? *Rúbrica:* 3 = auditoría del BMS, pasarela, cortafuegos; 2 = dos; 1 = uno; 0 = nada.
- **EX044 — Impacto clínico.** ¿Qué impacto clínico podría tener durante la noche un punto de consigna de 26 °C en un quirófano? *Rúbrica:* 3 = quirófano inutilizable o fuera de especificación al inicio de la sesión quirúrgica, retraso o problema de control de infecciones; 2 = parcial; 1 = vago; 0 = nada.
- **EX045 — Mejora del proceso.** ¿Qué cambio evita el próximo cambio fuera de ventana sin explicar? *Rúbrica:* 3 = anotación obligatoria en el registro del turno, alarma ante cambios fuera de ventana; 2 = uno; 1 = buscar culpables; 0 = nada.

### Síntesis del capítulo

Los registros de tendencias muestran qué cambió y cuándo; combinados con los registros de acceso, lo explican.

### Siga estudiando — capítulo 09 de 12

[← Capítulo 08 (borrador)](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 (borrador) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Avisos y parches para los sistemas del edificio

### Resultados de aprendizaje

Usted podrá (1) hacer corresponder los avisos con el inventario del edificio; (2) decidir entre aplicar un parche o una mitigación; y (3) hacer el seguimiento de las decisiones a lo largo del tiempo.

### 10.1 Fuentes

El índice de avisos de CISA incluye muchos productos de automatización de edificios, control de accesos y ascensores, junto con los avisos de los fabricantes. Suscríbase a los que sean pertinentes para los fabricantes de Millbrook. Use el inventario para elegir qué fabricantes y productos seguir, incluidos los controladores del BMS, el servidor de control de accesos y el controlador del ascensor. Consulte con regularidad el índice de CISA y las páginas de los fabricantes, y registre la fecha de cada consulta. Un aviso que llega después de un incidente es mucho menos útil que uno leído la semana en que se publicó.

### 10.2 Correspondencia

Para cada aviso: ¿está el producto en nuestro inventario, en una versión afectada y accesible de la forma que describe el aviso? Los dispositivos sin soporte (capítulo 4) suelen corresponder a avisos antiguos que nunca se corregirán. Registre la respuesta a cada pregunta en el registro de avisos, incluso cuando el producto no esté presente. Para los dispositivos sin soporte, como CHILLER-1 y LIFT-CTRL, un aviso sin corrección lleva directamente a los controles compensatorios: un aislamiento más estricto, ningún acceso remoto y una supervisión más cercana, como se acordó para esos dispositivos en el trabajo de inventario.

### 10.3 Elegir

Aplicar un parche a un controlador del BMS suele requerir una visita del contratista, una franja reservada y la comprobación posterior de todos los puntos. Las mitigaciones (reglas de cortafuegos, desactivar una interfaz web, restringir la cuenta de la pasarela) a menudo pueden aplicarse antes. Registre qué eligió y por qué. La elección depende de la consecuencia y de cuándo haya disponible una franja segura. Una mitigación aplicada hoy puede ser mejor que un parche el mes que viene, siempre que se compruebe que bloquea la vía que describe el aviso. Anote la decisión en el registro con la fecha, el responsable y la fecha de revisión.

### 10.4 Seguimiento

Un registro sencillo: aviso, productos afectados aquí, decisión, mitigación, fecha del parche, responsable, fecha de revisión. Informe cada mes al jefe de mantenimiento e instalaciones de los elementos abiertos de consecuencia alta. Guarde el registro en el mismo lugar que el inventario, para que un aviso nuevo pueda cotejarse con rapidez. Revíselo cada mes con el jefe de mantenimiento e instalaciones y cierre los elementos solo cuando se haya demostrado que están completados, por ejemplo con una comprobación de versión tras el parche. Los elementos que llevan mucho tiempo abiertos necesitan una decisión nueva, no un envejecimiento silencioso.

### 10.5 Pruebas tras el parche

Después, el contratista confirma que todos los puntos informan, que las alarmas funcionan y que los horarios son correctos; mantenimiento da la conformidad. Acuerde las comprobaciones antes del parche, con una lista de puntos y alarmas que probar y la persona que los probará. Tenga lista una alternativa, como el firmware anterior o llaves manuales para las puertas. Registre los resultados y la conformidad en el registro de avisos, para que el elemento pueda cerrarse con evidencia. Siempre que sea posible, aplique primero el parche a una sola unidad y compruébela antes de pasar a la siguiente.

### 10.6 Contacto con el fabricante

Cuando un aviso no sea claro sobre las configuraciones de los edificios, pregunte directamente al fabricante o al integrador: qué modelos y opciones están afectados, si la función vulnerable está activada por defecto y si se ha probado una mitigación en sistemas como el de Millbrook. Registre la respuesta y quién la dio. Los equipos de seguridad de producto de los fabricantes suelen responder antes cuando la pregunta nombra el modelo y la versión exactos que figuran en el inventario. Guarde las respuestas del fabricante con el aviso en el registro, y repita la pregunta si la respuesta no es clara. Si el fabricante confirma que una mitigación funciona, compruébela igualmente en Millbrook, porque la configuración local puede ser distinta.

### Ejemplo resuelto (Millbrook sintético)

Un aviso sintético advierte de que la interfaz web de DOOR-SRV permite eludir la autenticación en la versión 4.1; Millbrook usa la 4.1. Tras el capítulo 8, la interfaz solo es accesible desde la zona de control de accesos, y la corrección del fabricante, la 4.2, requiere una interrupción de 30 minutos de los horarios de las puertas. La decisión: restringir hoy la interfaz a la estación de trabajo de la oficina de seguridad y aplicar el parche el domingo a las 06:00, con llaves manuales entregadas a los supervisores de planta durante la interrupción.

> **Caso sintético — Millbrook.** El aviso y las versiones son inventados; CISA publica la lista de los avisos reales.

### Errores y límites

Los avisos pueden omitir detalles; pregunte a los fabricantes. Hay que comprobar que una mitigación bloquea realmente la vía descrita.

### Ejercicios — capítulo 10

- **EX046 — Tres preguntas de correspondencia.** Formule las tres preguntas que deciden si un aviso importa aquí. *Rúbrica:* 3 = producto presente, versión afectada, accesible como se describe; 2 = dos; 1 = una; 0 = nada.
- **EX047 — Correspondencia sin soporte.** Un aviso afecta a LIFT-CTRL y no hay corrección prevista. ¿Cuál es la decisión? *Rúbrica:* 3 = aislamiento y supervisión compensatorios, registrarlo, adelantar la sustitución; 2 = parcial; 1 = ignorarlo; 0 = nada.
- **EX048 — Plan para la interrupción de las puertas.** ¿Por qué se entregan llaves manuales durante el parche de DOOR-SRV? *Rúbrica:* 3 = los horarios de las puertas no están disponibles, las áreas restringidas deben seguir controladas y accesibles; 2 = parcial; 1 = sin motivo; 0 = nada.
- **EX049 — Entrada del registro.** Redacte la entrada de seguimiento del aviso de DOOR-SRV. *Rúbrica:* 3 = aviso, producto y versión, decisión, mitigación, fecha del parche, responsable, revisión; 2 = la mayoría; 1 = poco; 0 = nada.
- **EX050 — Comprobar una mitigación.** ¿Cómo confirmaría que la restricción de la interfaz funciona? *Rúbrica:* 3 = el responsable de la red confirma la regla; una prueba autorizada falla desde otra zona y funciona desde la oficina de seguridad; 2 = parcial; 1 = suponerlo; 0 = nada.

### Síntesis del capítulo

Los avisos se cotejan, se mitigan con rapidez, se parchean en franjas reservadas con alternativas preparadas y se siguen hasta su cierre.

### Siga estudiando — capítulo 10 de 12

[← Capítulo 09 (borrador)](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 (borrador) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Respuesta a incidentes en los sistemas del edificio de un hospital

### Resultados de aprendizaje

Usted podrá (1) adaptar los pasos de respuesta a incidentes a los sistemas del edificio; (2) decidir cuándo aislar el BMS; y (3) coordinarse con los equipos clínicos, de mantenimiento y de informática.

### 11.1 Planificar con antelación

NIST SP 800-82r3 insiste en preparar la respuesta a incidentes de TO junto con el personal de operación. En un hospital eso significa que mantenimiento, los responsables clínicos de guardia del centro, el equipo de seguridad informática y los contratistas acuerdan de antemano quién dirige, cuál es la alternativa manual de cada sistema y cómo localizar a los contratistas de noche. Ponga el acuerdo por escrito en un plan breve con números de teléfono, la alternativa de cada sistema crítico y quién puede ordenar el aislamiento. Ensáyelo al menos una vez con mantenimiento y un contratista, quizá un fin de semana tranquilo. El primer incidente es el peor momento para descubrir que el contratista de la enfriadora no tiene contacto nocturno.

### 11.2 Detectar y evaluar

Una alarma, un punto de consigna fuera de ventana o una nota de rescate en BMS-WS ponen en marcha el proceso. La primera pregunta es clínica: ¿hay ahora alguna zona insegura? El responsable clínico de guardia y mantenimiento deciden las medidas de protección inmediatas, como trasladar una sesión quirúrgica o pasar a alarmas de oxígeno en botellas vigiladas por el personal. Solo cuando el panorama clínico está claro empieza la evaluación de seguridad: qué está afectado, cómo empezó y si se está extendiendo. En Millbrook, la primera llamada la noche del rescate fue a mantenimiento, que confirmó que los quirófanos estaban vacíos y las plantas con normalidad antes de que actuara el equipo de redes.

### 11.3 Contener

Si no se puede confiar en el BMS, los controladores normalmente pueden seguir ejecutando sus últimos horarios programados sin el servidor. Aislar la zona del BMS en su cortafuegos detiene nuevas órdenes remotas mientras las instalaciones siguen funcionando localmente. El personal de mantenimiento recorre las salas de máquinas y comprueba a mano los valores críticos. Antes de aislar, compruebe cómo se comporta cada controlador crítico sin el servidor, porque algunos vuelven a valores por defecto distintos del funcionamiento normal. En Millbrook los conductos se bloquearon a las 22:55 y los controladores siguieron con sus horarios, mientras los ingenieros de mantenimiento hacían rondas cada hora. Anote la hora de cada paso de contención para el registro del incidente.

### 11.4 Evidencia y recuperación

Conserve los registros y las imágenes antes de reconstruir; restaure BMS-WS y el servidor a partir de copias de seguridad verificadas; compare cada punto crítico con las lecturas locales; vuelva a conectar los conductos de uno en uno. Acuerde de antemano dónde se guardará la evidencia y quién la tomará, para que la reconstrucción no se retrase. En Millbrook el responsable del incidente hizo copiar al almacén de evidencias la imagen del disco de BMS-WS y el extracto del registro del cortafuegos de 22:00 a 23:00 antes de que empezara la reconstrucción. Conserve la evidencia hasta que el responsable del incidente decida que ya no es necesaria. Registre cada paso y su hora.

### 11.5 Comunicación

El responsable del incidente informa a la dirección del hospital, que decide sobre la notificación externa. Los analistas no se ponen en contacto por su cuenta con la prensa ni con los reguladores. Los analistas apoyan al responsable del incidente aportando hechos claros con horas y fuentes. Deben evitar mensajes informales a compañeros o contratistas que puedan difundir información inexacta. Si un regulador o un periodista se pone en contacto directamente con un analista, este traslada la petición al responsable del incidente sin hacer comentarios. Guarde una copia de cada actualización enviada, con su hora, para que el registro del incidente muestre qué se dijo y cuándo.

### Ejemplo resuelto (Millbrook sintético)

A las 22:40 BMS-WS muestra un mensaje de rescate. Mantenimiento confirma que los quirófanos están vacíos y las plantas con normalidad. El equipo de redes bloquea los conductos de la zona del BMS a las 22:55; los controladores siguen con sus horarios. Los ingenieros de mantenimiento hacen rondas cada hora. A la mañana siguiente BMS-WS se reconstruye a partir de una imagen verificada, se comprueba el servidor y los conductos quedan restaurados a las 14:00, tras comprobar los puntos.

> **Caso sintético — Millbrook.** El incidente es inventado.

### Errores y límites

Algunos controladores pasan a valores seguros por defecto que difieren del funcionamiento normal; conózcalos antes de aislar. La supervisión mediante rondas no puede durar indefinidamente; planifique el personal.

### Ejercicios — capítulo 11

- **EX051 — Primera pregunta.** ¿Cuál es la primera pregunta cuando BMS-WS muestra un mensaje de rescate, y quién la responde? *Rúbrica:* 3 = ¿hay alguna zona clínica insegura?; responsable clínico de guardia y mantenimiento; 2 = solo la pregunta; 1 = una pregunta informática; 0 = nada.
- **EX052 — Por qué el aislamiento es aceptable.** Explique por qué bloquear los conductos de la zona del BMS no detuvo la ventilación. *Rúbrica:* 3 = los controladores ejecutan horarios locales sin el servidor; 2 = parcial; 1 = sí la detuvo; 0 = nada.
- **EX053 — Supervisión manual.** ¿Qué sustituye a la supervisión del BMS mientras está aislado? *Rúbrica:* 3 = rondas de mantenimiento leyendo los valores locales, comprobación de alarmas por el personal; 2 = parcial; 1 = vago; 0 = nada.
- **EX054 — Reconexión.** Describa cómo se restauran los conductos tras la recuperación. *Rúbrica:* 3 = de uno en uno, comparando los puntos con las lecturas locales; 2 = parcial; 1 = todos a la vez; 0 = nada.
- **EX055 — Valores seguros por defecto.** ¿Por qué debe conocer Aisha el comportamiento a prueba de fallos de los controladores antes de recomendar el aislamiento? *Rúbrica:* 3 = algunos valores por defecto cambian el funcionamiento (p. ej., ventiladores parados o al máximo) y podrían afectar a los pacientes; 2 = parcial; 1 = no hace falta; 0 = nada.

### Síntesis del capítulo

La seguridad clínica va primero, el control local mantiene las instalaciones, el aislamiento detiene el daño remoto y la evidencia precede a la recuperación.

### Siga estudiando — capítulo 11 de 12

[← Capítulo 10 (borrador)](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 (borrador) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Proyecto final: un informe de riesgos de los sistemas del edificio

### Resultados de aprendizaje

Usted podrá (1) reunir en un informe de riesgos los hallazgos de inventario, exposición, acceso, segmentación y supervisión; (2) priorizar por consecuencia clínica y probabilidad; y (3) presentarlo a la dirección del hospital.

### 12.1 Estructura

Alcance y método; sistemas incluidos, con sus responsables; hallazgos, cada uno con su evidencia; valoración del riesgo; acciones recomendadas con responsables y fechas; riesgo residual que acepta el hospital. Limítelo a unas pocas páginas, con un anexo para la evidencia. Escriba primero el alcance, nombrando qué sistemas se revisaron y cuáles no, para que los lectores sepan qué cubre el informe. Cada hallazgo debe remitir a su evidencia en el anexo, y cada acción a un responsable. La parte de riesgo residual debe decir quién lo aceptó, según lo decidido por la dirección del hospital.

### 12.2 Valoración

Valore la consecuencia (daño a los pacientes, pérdida de servicio) y la probabilidad (exposición, facilidad, actividad conocida) con escalas sencillas de tres niveles, acordadas con los responsables de mantenimiento y clínicos. Una probabilidad media con una consecuencia grave para los pacientes suele estar por encima de una probabilidad alta con una consecuencia menor. Acuerde las escalas antes de valorar ningún hallazgo, y escriba una frase que explique cada nivel para que distintos lectores las apliquen de la misma manera. En Millbrook el controlador del ascensor obtuvo consecuencia alta y probabilidad media, lo que lo situó en lo más alto de la lista. Las valoraciones deben revisarse cuando cambie la evidencia.

### 12.3 Recomendaciones

Cada una nombra un cambio concreto, un responsable, una fecha y cómo se demostrará que está completada. Incluya mejoras rápidas (cerrar la exposición, retirar herramientas remotas antiguas) y proyectos más largos (sustituir instalaciones sin soporte). En Millbrook las recomendaciones incluyeron la sustitución de LIFT-CTRL y una comprobación semanal de las cuentas de la pasarela. Cada una se redactó con un responsable, una fecha y la evidencia que demostraría que está completada, como una orden de compra o un informe semanal de cuentas. Las recomendaciones vagas y sin responsable rara vez conducen a un cambio. Separe en la lista las mejoras rápidas de los proyectos.

### 12.4 Presentación

Empiece por los tres riesgos principales expresados en términos de pacientes; muestre lo que ya ha mejorado; pida decisiones, no admiración. Mantenga la presentación breve, con una diapositiva por cada riesgo principal y una diapositiva de mejoras. Lleve el anexo de evidencia por si la dirección pregunta, pero no lo presente. Termine con las decisiones concretas que se necesitan, como la financiación para sustituir LIFT-CTRL, y confirme quién actuará sobre cada decisión. Envíe después las diapositivas con el resumen, para que los directivos ausentes vean las mismas decisiones y responsables.

### 12.5 Anexo de evidencia

Para cada hallazgo, conserve la fotografía, el extracto de registro o el fragmento de configuración que lo respalda, con la fecha y quién lo recogió. La dirección rara vez lee el anexo, pero los auditores y el siguiente analista sí lo harán, y permite a cualquiera comprobar que el hallazgo era real. Guarde el anexo con controles de acceso, porque contiene detalles sobre dispositivos, direcciones y debilidades. Vincule cada elemento a su número de hallazgo y registre dónde se guarda la evidencia original. Un hallazgo sin ningún elemento que lo respalde debe marcarse como no confirmado hasta que se recoja evidencia.

### 12.6 Después de la reunión

Registre en el registro de seguimiento las decisiones tomadas, los responsables y las fechas, envíe un resumen de una página a los asistentes y reserve la revisión de los seis meses. El avance en las acciones se convierte en la diapositiva inicial de la próxima vez, lo que mantiene la atención en el cambio y no en los hallazgos nuevos. En la revisión de los seis meses, compruebe si se completó cada acción y actualice las valoraciones donde haya cambiado la evidencia. Las acciones retrasadas necesitan una fecha nueva y un motivo. Mantenga el resumen breve para que los asistentes lo lean, y archívelo con el informe.

### Ejemplo resuelto (Millbrook sintético)

El informe de Aisha enumera: (1) LIFT-CTRL sin soporte y con un enlace celular: consecuencia alta (traslados de pacientes), probabilidad media; (2) cuentas residuales de contratistas no desactivadas tras las sesiones: consecuencia alta, probabilidad media; (3) registros de tendencias conservados solo 14 días: consecuencia media, probabilidad alta. Ya corregido: la exposición de BACnet a internet, la estación BMS-WS conectada a dos redes y la contraseña por defecto de DOOR-SRV. La dirección aprueba financiar la sustitución de LIFT-CTRL el año que viene y una comprobación semanal de las cuentas de la pasarela.

> **Caso sintético — Millbrook.** El informe y las valoraciones son inventados.

### Errores y límites

Un informe refleja la evidencia disponible en su fecha; programe una revisión. No es una evaluación formal según IEC 62443.

### Ejercicios — capítulo 12

- **EX056 — Secciones del informe.** Enumere las seis secciones del informe de riesgos. *Rúbrica:* 3 = alcance y método, sistemas y responsables, hallazgos y evidencia, valoración, acciones, riesgo residual; 2 = cuatro; 1 = dos; 0 = nada.
- **EX057 — Ordenar dos riesgos.** Ordene «retención de tendencias del BMS de 14 días» frente a «ascensor sin soporte con enlace celular» y justifíquelo. *Rúbrica:* 3 = primero el ascensor; la consecuencia en los traslados de pacientes pesa más que la pérdida de evidencia; 2 = orden correcto; 1 = invertido; 0 = nada.
- **EX058 — Redactar una recomendación.** Redacte una recomendación completa para las cuentas residuales de contratistas. *Rúbrica:* 3 = cambio concreto, responsable, fecha, evidencia de que está completada; 2 = tres; 1 = vago; 0 = nada.
- **EX059 — Abrir la presentación.** Escriba la frase inicial de la presentación de Aisha a la dirección. *Rúbrica:* 3 = el riesgo principal en términos de pacientes, con la petición; 2 = clara pero técnica; 1 = jerga; 0 = nada.
- **EX060 — Riesgo residual.** Indique un riesgo residual que Millbrook debe aceptar hasta el año que viene y por qué es aceptable. *Rúbrica:* 3 = LIFT-CTRL hasta su sustitución, nombrando los controles compensatorios; 2 = solo el riesgo; 1 = ninguno aceptado; 0 = nada.

### Síntesis del capítulo

Un informe breve, respaldado por evidencia, ordenado por consecuencia y con acciones asignadas convierte los hallazgos en cambios financiados.

### Siga estudiando — capítulo 12 de 12

[← Capítulo 11 (borrador)](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Resultados resueltos ↓](#worked-results) · [Siguiente curso a través del índice de capítulos →](../SUBJECTS.md)

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

**EX016.** Sistema, nombre del dispositivo, ubicación, responsable, versión de firmware, estado del soporte del fabricante, dirección de red y consecuencia clínica de un fallo.

**EX017.** Imprime `UNSUPPORTED BOILER-2   system=HVAC installed=2010` y la línea de HVAC pasa a ser `HVAC               4 device(s): AHU-OT1, AHU-OT2, CHILLER-1, BOILER-2`.

**EX018.** El fabricante de la enfriadora no publicará correcciones para las debilidades que se descubran a partir de ahora, así que su riesgo crece con el tiempo; debemos protegerla de otras formas y planificar su sustitución.

**EX019.** Colocar LIFT-CTRL en su propio segmento de red, accesible solo desde su pasarela de mantenimiento; restringir o retirar el enlace celular salvo cuando se use con un ticket; supervisar sus conexiones; programar la sustitución en el plan de inversiones.

**EX020.** La persona autorizada para gases medicinales, porque el sistema de alarma de gases medicinales es suyo.

**EX021.** Si esa única contraseña se filtra, o si un ingeniero que la conocía se marcha en malos términos, todos los hospitales que atiende el integrador quedan abiertos a la vez.

**EX022.** El registro de auditoría o de tendencias del BMS anota qué cuenta nominativa hizo el cambio, así que el hospital puede preguntar a esa persona el motivo y distinguir rápidamente un error de un uso indebido.

**EX023.** «¿Se entrega cada dispositivo con una contraseña única o obliga a fijar una durante la configuración?» «¿Publican una política de divulgación de vulnerabilidades y un contacto?» «¿Durante cuántos años ofrecerán actualizaciones de seguridad, y está cifrada la comunicación?»

**EX024.** Cambiar todas las contraseñas que conocía ese ingeniero, guardando los nuevos valores en el almacén; revisar qué cuentas y accesos remotos tenía y desactivarlos; registrar el cambio.

**EX025.** IEC 62443-4-2, porque fija requisitos de seguridad para los componentes de los sistemas de automatización y control industrial, que es lo que son los controladores del BMS.

**EX026.** Un contratista redirige un puerto para que la página web del BMS funcione desde casa; una regla de cortafuegos de un proyecto permanece tras terminar la puesta en marcha.

**EX027.** `203.0.113.10:22 ... NOT APPROVED - report` para la nueva entrada, y el total pasa a ser `unapproved: 3`, ya que en esa dirección solo está aprobado el puerto 443.

**EX028.** T0883 Internet Accessible Device.

**EX029.** Informar al equipo de redes y a mantenimiento; hacer que el responsable lo cierre mediante un cambio de emergencia; revisar los registros en busca de conexiones externas; averiguar quién lo abrió y por qué; dar a esa parte acceso por la pasarela en su lugar.

**EX030.** No tiene autorización sobre sistemas que no pertenecen a Millbrook; sondearlos podría infringir la ley y perturbar las instalaciones de otro hospital.

**EX031.** La pasarela de acceso remoto del hospital; una herramienta de escritorio remoto en BMS-WS; el enlace celular del ascensor; el enrutador del fabricante de la enfriadora.

**EX032.** Dar a los ingenieros del contratista del BMS cuentas individuales en la pasarela con autenticación multifactor, y revisar los registros de sesión de la pasarela después de cada visita de soporte.

**EX033.** Cada contratista solo necesita su propio sistema; limitar la cuenta significa que una contraseña robada al contratista de la enfriadora no puede abrir las puertas de farmacia o de maternidad.

**EX034.** Si se retira primero la herramienta antigua y la cuenta de la pasarela falla, el contratista no podría ayudar durante una avería de las instalaciones; probar antes el sustituto mantiene el soporte sin interrupción.

**EX035.** No: la supervisión de la alarma de incendios es una función de seguridad de las personas; documente el enlace, confirme con el responsable de seguridad contra incendios que solo alcanza la central de supervisión y revíselo, en lugar de desconectarlo.

**EX036.** Una zona del BMS; una zona de alarma de gases medicinales y una zona del ascensor (relevantes para la seguridad); una zona de control de accesos; una DMZ; la zona corporativa.

**EX037.** «Servidor del BMS → servidor de datos de la DMZ en el puerto de exportación acordado, permitir», con la regla final «cualquiera → cualquiera, denegar» que captura todo lo que no figura en la lista.

**EX038.** Abren un panel de solo lectura en el servidor de datos de la DMZ o, para hacer cambios, se conectan a través de la pasarela a un servidor de salto dentro de la zona del BMS.

**EX039.** Confirmar con mantenimiento si los puntos que faltan afectan a áreas clínicas, restaurar la configuración anterior si es así, identificar el conducto que falta (aquí, un servidor de hora) y añadirlo dentro del mismo registro de cambio.

**EX040.** No impide que alguien que use credenciales válidas de la pasarela, o un interno, cause daños dentro de los conductos permitidos.

**EX041.** El script solo señala un cambio cuya hora queda fuera de 08:00–10:00, y las 09:00 están dentro de esa ventana.

**EX042.** `03:00 setpoint 20.0->26.0 in window` y `09:00 setpoint 26.0->21.0 OUTSIDE WINDOW - review`.

**EX043.** El registro de auditoría del BMS, el registro de la pasarela de acceso remoto y el registro del cortafuegos de la zona del BMS.

**EX044.** El quirófano estaría fuera de su intervalo de temperatura al empezar la sesión quirúrgica de la mañana, así que la cirugía podría retrasarse hasta que se recuperen las condiciones, y el confort del personal y las condiciones de esterilidad se verían comprometidos.

**EX045.** Exigir que todo cambio fuera de ventana se anote en el registro del turno con el motivo, y configurar una alarma del BMS dirigida al ingeniero de guardia cuando un punto de consigna crítico cambie fuera de la ventana.

**EX046.** ¿Tenemos el producto? ¿Usamos una versión afectada? ¿Se puede alcanzar la debilidad de la forma que describe el aviso?

**EX047.** Registrar que el aviso se aplica y no puede parchearse, mantener LIFT-CTRL aislado con solo su vía de mantenimiento, supervisar sus conexiones y subir la prioridad de su sustitución en el plan de inversiones.

**EX048.** Durante la interrupción de 30 minutos los horarios electrónicos de las puertas pueden no funcionar, así que los supervisores de planta necesitan llaves para mantener las puertas de farmacia y de maternidad a la vez seguras y utilizables.

**EX049.** «Aviso: elusión de la autenticación web de DOOR-SRV, v4.1 (la nuestra). Decisión: mitigar y después parchear. Mitigación: interfaz limitada a la estación de trabajo de la oficina de seguridad. Parche 4.2 el domingo a las 06:00 con llaves manuales. Responsable: responsable de sistemas de seguridad de mantenimiento. Revisión tras el parche.»

**EX050.** Pedir al responsable de la red que muestre la regla y después, en una prueba acordada, confirmar que la página web carga desde la estación de trabajo de la oficina de seguridad y falla desde otro equipo de la zona de control de accesos.

**EX051.** «¿Hay ahora mismo alguna zona clínica insegura?», que responde el responsable clínico de guardia junto con mantenimiento, antes de cualquier acción técnica.

**EX052.** Los controladores de campo guardan sus propios programas y horarios y siguen haciendo funcionar las unidades de tratamiento de aire sin el servidor ni la estación de trabajo del BMS; el cortafuegos solo detuvo las órdenes procedentes de fuera de la zona.

**EX053.** Rondas de mantenimiento cada hora leyendo las pantallas locales en las salas de máquinas, y el personal de las plantas y de los quirófanos vigilando las alarmas locales, incluidos los paneles de gases medicinales.

**EX054.** Tras la reconstrucción, el equipo de redes reactiva un conducto cada vez, y mantenimiento compara cada punto crítico del BMS con las lecturas locales antes de restaurar el siguiente conducto.

**EX055.** Algunos controladores vuelven a valores por defecto, como ventiladores a velocidad fija o compuertas cerradas, cuando pierden el servidor, lo que podría alterar la presión de los quirófanos, así que la recomendación debe tener en cuenta ese comportamiento.

**EX056.** Alcance y método; sistemas incluidos y responsables; hallazgos con evidencia; valoración del riesgo; acciones recomendadas con responsables y fechas; riesgo residual aceptado.

**EX057.** El ascensor va primero: si se usa indebidamente o falla, los traslados de pacientes entre plantas se retrasan, un daño clínico directo, mientras que una retención corta de las tendencias debilita sobre todo las investigaciones.

**EX058.** «Las cuentas de la pasarela se desactivan automáticamente al terminar cada sesión asociada a un ticket; responsable: jefe del equipo de redes; plazo: final del mes que viene; evidencia: informe semanal que muestre que no hay cuentas de contratistas activadas fuera de tickets abiertos.»

**EX059.** «Nuestros ascensores trasladan pacientes entre los quirófanos y las plantas, y su controlador ya no puede recibir parches; les pedimos que financien su sustitución el año que viene.»

**EX060.** LIFT-CTRL sigue en servicio hasta su sustitución; es aceptable porque está aislado en su propia zona, su enlace celular está restringido al centro de servicio del contratista y sujeto a tickets, y sus conexiones se supervisan.

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
