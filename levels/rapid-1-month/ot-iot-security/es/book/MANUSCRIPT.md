# Seguridad de TO, IoT y sistemas ciberfísicos: una introducción rápida

- Idioma: español neutro (`es`); curso rápido, un mes; aproximadamente 80 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–4 de 4 tienen texto didáctico escrito a mano; los ejercicios EX001–EX050 tienen sus resultados resueltos correspondientes; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas se incluyen a partir de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4.
- Público: personas que empiezan, sin conocimientos previos de TO.
- Relación con los libros vecinos: el [libro del curso profesional](../../../../professional-6-months/ot-iot-security/es/book/MANUSCRIPT.md) desarrolla cada tema en la práctica. **Este libro es una introducción de cuatro capítulos.**
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado. No concede autorización para acceder a emplazamientos reales. Todos los emplazamientos, personas y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

El capítulo 1 define TO, IoT y CPS; el capítulo 2 trata los activos, las redes y la exposición; el capítulo 3 trata cómo reconocer y notificar problemas; el capítulo 4 trata los hábitos, las nociones de respuesta, los límites y los próximos pasos. Cada capítulo tiene resultados de aprendizaje, enseñanza, un ejemplo resuelto, un caso sintético etiquetado, errores y límites, doce o trece ejercicios puntuados de 0 a 3, una síntesis y un bloque **Siga estudiando**. Los laboratorios de los capítulos 2 y 3 solo leen datos locales (`python3 file.py`).

### Caso de estudio sintético

| Elemento | Función | Límite |
|---|---|---|
| **Elmstead Solar and Battery Site**: inversores INV-01 a INV-04, sistema de almacenamiento de energía en baterías con su sistema de gestión de baterías, controlador de planta SC-1, cámaras, portal de supervisión del fabricante | Emplazamiento estudiado a lo largo del libro | Inventado |
| **Jonah Park** | Persona en prácticas en Elmstead | Inventada |

### Fuentes principales

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [serie ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Lista completa en [Referencias](#references).

## Contenido

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Qué son la seguridad de TO, de IoT y de los sistemas ciberfísicos

### Resultados de aprendizaje

Usted podrá (1) definir la tecnología operacional, el IoT y los sistemas ciberfísicos; (2) identificarlos en una planta solar con baterías; (3) explicar por qué sus prioridades de seguridad difieren de las de la informática de oficina; y (4) nombrar las principales guías públicas.

### 1.1 Tres términos que se solapan

La tecnología operacional (TO) es el hardware y el software que supervisa o controla equipos y procesos físicos; NIST SP 800-82r3 es la principal guía estadounidense para protegerla. El Internet de las cosas (IoT) son dispositivos conectados en red que perciben el mundo o actúan sobre él, a menudo pequeños y conectados a la nube. Un sistema ciberfísico (CPS, por sus siglas en inglés) es cualquier sistema en el que la computación y los procesos físicos están estrechamente unidos. Una planta de energía moderna es las tres cosas a la vez.

Los términos son útiles porque apuntan a preocupaciones distintas. Llamar TO a un dispositivo dirige la atención al proceso que controla; llamarlo IoT la dirige a su pequeño tamaño, su configuración por defecto y su enlace con la nube; llamar CPS a toda la planta recuerda que un fallo de software puede convertirse en calor, movimiento o pérdida de suministro eléctrico.

### 1.2 Una planta solar con baterías

Las filas de paneles solares alimentan inversores que convierten la corriente continua en la corriente alterna de la red. Un sistema de almacenamiento de energía en baterías (BESS, por sus siglas en inglés) almacena energía, gestionado por un sistema de gestión de baterías que vigila las temperaturas y las tensiones de las celdas. Un controlador de planta decide cuándo cargar y descargar, siguiendo un calendario y las instrucciones del operador de la red. Las estaciones meteorológicas, las cámaras y la central de detección de incendios completan el cuadro. Muchos dispositivos informan además a las nubes de los fabricantes.

Cada una de estas partes puede fallar o usarse indebidamente de una forma distinta. Un ajuste erróneo de un inversor cambia cuánta potencia llega a la red; un sistema de gestión de baterías que calla oculta una celda que se sobrecalienta; un controlador de planta confundido carga a la hora equivocada. Saber qué hace cada parte es lo que permite a Jonah notar cuándo algo se comporta de forma extraña.

### 1.3 Prioridades

En la informática de oficina, proteger los datos confidenciales suele ir primero. En una planta de energía las primeras prioridades son la seguridad física (las baterías pueden sobrecalentarse y arder) y mantener el proceso estable y disponible. La integridad de las órdenes importa muchísimo: una falsa orden de «descargar ahora» puede dañar los equipos o perturbar la red. La confidencialidad sigue importando, pero rara vez es lo primero. Este orden cambia cómo es una buena respuesta. Apagar un dispositivo para proteger sus datos puede ser sensato en un portátil de oficina, pero en Elmstead podría dejar una batería sin gestión o cortar una potencia con la que contaba el operador de la red. Por eso el trabajo de seguridad en la planta empieza por preguntar qué está haciendo el equipo y si es seguro detenerlo.

### 1.4 Por qué es una preocupación real

Los dispositivos industriales y de IoT a menudo se diseñaron para redes cerradas y usuarios de confianza. Hoy son accesibles mediante acceso remoto, nubes y redes compartidas. CISA publica cada semana avisos sobre productos industriales, y las botnets de IoT como Mirai, estudiada por Antonakakis y sus colegas, mostraron cuántos dispositivos pueden tomarse mediante contraseñas por defecto. Una planta de energía suele combinar ambos tipos de riesgo: controladores industriales que esperan tráfico de confianza y pequeños dispositivos conectados, como las cámaras, que salen de fábrica con configuraciones débiles. Una persona en prácticas no necesita seguir todos los avisos, pero debe saber que en estos equipos se descubren y publican debilidades con regularidad, y que corregirlas depende de saber qué dispositivos tiene realmente la planta.

### 1.5 El mapa de guías

IEC 62443 es la serie internacional para la seguridad de la automatización industrial; NIST IR 8259 y ETSI EN 303 645 fijan configuraciones de referencia para los productos de IoT; MITRE ATT&CK for ICS cataloga las técnicas de los adversarios; los avisos de CISA informan de debilidades e incidentes reales. No necesita leerlas todas antes de empezar. Trátelas como lugares donde buscar cuando surja una pregunta: IEC 62443 al decidir cómo dividir la red de una planta, las configuraciones de referencia de IoT al comprar una cámara o un sensor, ATT&CK for ICS al describir lo que ha observado y los avisos de CISA al preguntarse si un producto que tiene presenta una debilidad conocida. Los capítulos posteriores usan cada una de ellas de esa manera.

### Ejemplo resuelto (Elmstead sintético)

Jonah Park entra en Elmstead Solar and Battery Site como persona en prácticas. Durante una visita anota: los inversores INV-01 a INV-04, el BESS con su sistema de gestión de baterías, el controlador de planta SC-1, una conexión con el operador de la red, dos cámaras y un portal de supervisión del fabricante. Junto a cada uno escribe una consecuencia física de un fallo.

> **Caso sintético — Elmstead Solar and Battery Site.** El emplazamiento, Jonah Park y todas las cifras de este libro son inventados con fines didácticos.

### Errores y límites

Estas definiciones se solapan; las organizaciones las usan de formas distintas. Este libro es introductorio y no concede ninguna autorización para acceder a un emplazamiento real.

### Ejercicios — capítulo 1

- **EX001 — Definir la TO.** Dé una definición de una frase de la tecnología operacional. *Rúbrica:* 3 = sistemas que supervisan o controlan procesos físicos, hardware y software; 2 = parcial; 1 = «ordenadores de fábrica»; 0 = nada.
- **EX002 — El IoT con sus propias palabras.** ¿Qué distingue a un dispositivo IoT de un portátil de oficina? *Rúbrica:* 3 = percibe el mundo físico o actúa sobre él, suele ser pequeño, conectado a una red o a la nube; 2 = parcial; 1 = vago; 0 = nada.
- **EX003 — Ejemplo de CPS.** Dé un ejemplo de sistema ciberfísico fuera del sector energético. *Rúbrica:* 3 = ejemplo válido con el vínculo entre computación y mundo físico explicado; 2 = solo el ejemplo; 1 = no es un CPS; 0 = nada.
- **EX004 — Función del inversor.** ¿Qué hace un inversor en Elmstead? *Rúbrica:* 3 = convierte la corriente continua de los paneles en la alterna de la red; 2 = «convierte la energía»; 1 = almacena; 0 = nada.
- **EX005 — Gestión de baterías.** Nombre dos cosas que vigila el sistema de gestión de baterías. *Rúbrica:* 3 = temperatura y tensión de las celdas (o estado de carga); 2 = una; 1 = incorrecto; 0 = nada.
- **EX006 — Decidir cuándo cargar.** ¿Qué dispositivo decide cuándo se carga y se descarga la batería? *Rúbrica:* 3 = el controlador de planta SC-1, siguiendo el calendario o al operador de la red; 2 = solo SC-1; 1 = el inversor; 0 = nada.
- **EX007 — Primera prioridad.** Indique la primera prioridad de seguridad en una planta de baterías y por qué. *Rúbrica:* 3 = la seguridad física, riesgo de incendio o sobrecalentamiento de las baterías para las personas; 2 = solo la seguridad física; 1 = la confidencialidad; 0 = nada.
- **EX008 — Descarga falsa.** Describa el daño de una falsa orden de «descargar ahora». *Rúbrica:* 3 = esfuerzo o daño en los equipos, perturbación de la red, incumplimiento del calendario; 2 = uno; 1 = vago; 0 = nada.
- **EX009 — Lección de una botnet.** ¿Qué mostró la botnet Mirai sobre los dispositivos IoT? *Rúbrica:* 3 = muchos dispositivos tomados a gran escala mediante contraseñas por defecto; 2 = parcial; 1 = «virus»; 0 = nada.
- **EX010 — Asociar las guías.** ¿Qué fuente corresponde a cada necesidad: (a) serie sobre la seguridad de la automatización industrial; (b) configuración de referencia para el IoT de consumo; (c) técnicas de los adversarios? *Rúbrica:* 3 = IEC 62443, ETSI EN 303 645, ATT&CK for ICS; 2 = dos; 1 = una; 0 = nada.
- **EX011 — Avisos.** ¿Quién publica en EE. UU. avisos sobre debilidades en productos industriales? *Rúbrica:* 3 = CISA (con los fabricantes); 2 = «el gobierno»; 1 = incorrecto; 0 = nada.
- **EX012 — Enumerar la planta.** Enumere cinco componentes de Elmstead de la visita. *Rúbrica:* 3 = cinco correctos; 2 = cuatro; 1 = dos; 0 = nada.
- **EX013 — Su autorización.** ¿Terminar este libro permite a Jonah iniciar sesión en los inversores de Elmstead? Explíquelo. *Rúbrica:* 3 = no; necesita la autorización del propietario o un puesto definido; el libro no concede ninguna; 2 = solo «no»; 1 = sí; 0 = nada.

### Síntesis del capítulo

La TO, el IoT y los CPS unen la computación con equipos físicos; en una planta de energía, la seguridad física y la integridad de las órdenes van primero.

### Siga estudiando — capítulo 01 de 04

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Activos, redes y exposición

### Resultados de aprendizaje

Usted podrá (1) explicar por qué el inventario va primero; (2) revisar una lista de dispositivos en busca de debilidades comunes; (3) describir cómo debe separarse la red de una planta; y (4) reconocer los riesgos de la exposición a internet y del acceso remoto.

### 2.1 Primero, el inventario

No se puede proteger lo que no se sabe que existe. NIST SP 800-82r3 sitúa el inventario de activos en la base. Para cada dispositivo, registre el nombre, la función, la ubicación, el responsable, la versión de firmware, la dirección de red y si se conecta a una nube.

```python
"""Lab 2: review a synthetic Elmstead inverter list for default passwords, old firmware and cloud links."""
inv = [("INV-01", "5.1", False, True), ("INV-02", "5.1", True, True),
       ("INV-03", "4.7", False, True), ("INV-04", "5.1", False, False)]
LATEST = "5.1"
for name, fw, default_pw, cloud in inv:
    issues = []
    if default_pw: issues.append("default-password")
    if fw != LATEST: issues.append(f"old-fw {fw}")
    print(f"{name} cloud={'yes' if cloud else 'no '} {', '.join(issues) or 'ok'}")
print("needs action:", sum(1 for _, fw, d, _ in inv if d or fw != LATEST))
```

Ejecútelo con `python3 lab_inverters.py`. Salida verificada:

```text
INV-01 cloud=yes ok
INV-02 cloud=yes default-password
INV-03 cloud=yes old-fw 4.7
INV-04 cloud=no  ok
needs action: 2
```

Un inventario útil registra también a quién llamar por cada dispositivo y cuándo se comprobó por última vez. Los registros se quedan desfasados a medida que los fabricantes cambian piezas y los ingenieros añaden equipos, así que Elmstead revisa la lista después de cada visita de mantenimiento. El Lab 2 trabaja con una versión breve de esta lista para los cuatro inversores, y muestra lo rápido que unas pocas columnas revelan lo que necesita atención.

### 2.2 Lectura del laboratorio

INV-02 todavía usa su contraseña por defecto: cualquiera que haya leído el manual podría iniciar sesión. INV-03 ejecuta el firmware 4.7, mientras que la versión vigente es la 5.1, así que puede carecer de correcciones de seguridad. INV-04 no tiene enlace con la nube ni problemas. Dos de los cuatro inversores necesitan intervención. Su corrección la hacen el propietario y el fabricante en momentos planificados, no personas en prácticas que experimentan. El laboratorio solo comprueba lo que dice la lista. Si la lista es errónea, por ejemplo porque un fabricante cambió una contraseña durante una visita y nadie actualizó el registro, el resultado también lo será. Trate la salida como una lista de preguntas para la ingeniera de la planta, y confirme cada elemento con los registros o con el fabricante antes de que nadie actúe.

### 2.3 Separar la red

IEC 62443 describe zonas (grupos de dispositivos con necesidades similares) unidas por conductos, que son conexiones controladas. En Elmstead la zona de control contiene SC-1, los inversores y el sistema de gestión de baterías; las cámaras están en su propia zona; la red de oficina está separada a su vez; una DMZ contiene el servidor que comparte datos hacia fuera. Los cortafuegos entre zonas solo permiten las conexiones necesarias. La finalidad de las zonas es que un problema en una no se extienda libremente a otra. Si una cámara se viera comprometida, el cortafuegos entre la zona de cámaras y la zona de control debería impedirle alcanzar SC-1 o los inversores. Cada conexión permitida entre zonas debe tener un motivo, un responsable y un registro, para que las reglas antiguas puedan encontrarse y retirarse.

### 2.4 Exposición y acceso remoto

Los dispositivos accesibles directamente desde internet son una debilidad habitual; MITRE ATT&CK for ICS la denomina T0883 Internet Accessible Device. El acceso remoto de los fabricantes debe pasar por una única pasarela con autenticación multifactor, activada solo cuando se necesite, recomendaciones que recoge el aviso AA21-042A de CISA tras el compromiso de una instalación de tratamiento de agua en 2021. Para Elmstead esto significa comprobar que ningún inversor, controlador o cámara responde directamente desde internet, y que la vía de soporte del fabricante termina en una pasarela propiedad de la planta. Las cuentas de esa pasarela deben pertenecer a personas con nombre, activarse para un trabajo concreto y desactivarse después. Los registros de sesión permiten a la ingeniera ver quién se conectó y qué hizo.

### 2.5 Portales en la nube

Las nubes de los fabricantes son cómodas para la supervisión, pero un portal que además puede enviar órdenes es, en la práctica, acceso remoto. Pregunte si puede controlar equipos, quién tiene cuentas y si la autenticación multifactor está activada. En Elmstead la ingeniera descubrió que el portal de supervisión del fabricante podía enviar órdenes de carga, no solo mostrar datos. Eso lo convierte en parte del panorama del acceso remoto, con las mismas preguntas sobre cuentas nominativas y segundos factores. Las respuestas deben figurar en el inventario junto a cada dispositivo que el portal puede alcanzar, para que no se olviden cuando cambien el personal o los contratos.

### Ejemplo resuelto (Elmstead sintético)

Jonah enseña la salida del laboratorio a la ingeniera de la planta. Ella reserva al fabricante de los inversores para la semana siguiente, para cambiar la contraseña de INV-02 y actualizar INV-03, y anota que el portal de supervisión puede enviar órdenes de carga, un hallazgo para el capítulo 3.

> **Caso sintético — Elmstead.** Los dispositivos, las versiones y los ajustes son inventados.

### Errores y límites

Una lista elaborada a partir de registros puede omitir dispositivos; los recorridos por la planta y los registros de red la completan. Nunca escanee una planta en funcionamiento para elaborar un inventario salvo que el propietario lo haya autorizado y planificado.

### Ejercicios — capítulo 2

- **EX014 — Por qué el inventario.** Explique en una frase por qué el inventario va antes que otros controles. *Rúbrica:* 3 = todo control depende de conocer los dispositivos; los dispositivos desconocidos quedan sin proteger; 2 = parcial; 1 = vago; 0 = nada.
- **EX015 — Campos del inventario.** Nombre cinco campos del registro de un dispositivo de Elmstead. *Rúbrica:* 3 = cinco campos pertinentes; 2 = cuatro; 1 = dos; 0 = nada.
- **EX016 — Riesgo de la contraseña por defecto.** ¿Por qué es peligrosa la contraseña por defecto de INV-02? *Rúbrica:* 3 = está publicada en los manuales; cualquiera con alcance inicia sesión; 2 = parcial; 1 = «débil»; 0 = nada.
- **EX017 — Firmware antiguo.** ¿Qué sugiere `old-fw 4.7` sobre INV-03? *Rúbrica:* 3 = puede carecer de las correcciones de seguridad de la 5.1; consultar los avisos; planificar la actualización; 2 = parcial; 1 = más lento; 0 = nada.
- **EX018 — Modificar el laboratorio.** Si el firmware de INV-04 fuera "4.9", ¿qué imprimiría el laboratorio para ese inversor y para el total? *Rúbrica:* 3 = `INV-04 cloud=no  old-fw 4.9` y `needs action: 3`; 2 = uno; 1 = `ok`; 0 = nada.
- **EX019 — Quién lo corrige.** ¿Quién cambia la contraseña de INV-02, y cuándo? *Rúbrica:* 3 = el propietario o el fabricante en un momento planificado; 2 = solo el propietario; 1 = Jonah, ahora; 0 = nada.
- **EX020 — Zonas.** Nombre las cuatro zonas propuestas para Elmstead. *Rúbrica:* 3 = control, cámaras, oficina, DMZ; 2 = tres; 1 = una; 0 = nada.
- **EX021 — Qué es un conducto.** ¿Qué es un conducto en la terminología de IEC 62443? *Rúbrica:* 3 = vía de comunicación controlada entre zonas; 2 = «conexión»; 1 = canalización de cables; 0 = nada.
- **EX022 — Ubicación de las cámaras.** ¿Por qué las cámaras no deben compartir la zona de control? *Rúbrica:* 3 = las cámaras suelen ser débiles o estar enlazadas con internet; su compromiso alcanzaría los controladores; 2 = parcial; 1 = ancho de banda; 0 = nada.
- **EX023 — Dispositivo expuesto a internet.** ¿Qué técnica de ATT&CK for ICS describe un controlador accesible desde internet? *Rúbrica:* 3 = T0883 Internet Accessible Device; 2 = solo el nombre; 1 = incorrecto; 0 = nada.
- **EX024 — Patrón de acceso del fabricante.** Describa en dos frases un patrón seguro de acceso remoto para los fabricantes. *Rúbrica:* 3 = una pasarela, MFA, cuentas nominativas, activadas según necesidad, registradas; 2 = tres elementos; 1 = uno; 0 = nada.
- **EX025 — Preguntas sobre el portal.** ¿Qué tres preguntas debe hacer Jonah sobre el portal de supervisión del fabricante? *Rúbrica:* 3 = si puede controlar, quién tiene cuentas, si hay MFA; 2 = dos; 1 = una; 0 = nada.
- **EX026 — Sin escaneos.** ¿Por qué Jonah no escanea él mismo la red de Elmstead para completar la lista? *Rúbrica:* 3 = no está autorizado; los escaneos pueden perturbar los dispositivos; usar registros y recorridos; 2 = uno; 1 = se puede escanear; 0 = nada.

### Síntesis del capítulo

Conozca todos los dispositivos, corrija las contraseñas por defecto y el firmware antiguo mediante trabajos planificados, separe las zonas y mantenga el acceso remoto acotado.

### Siga estudiando — capítulo 02 de 04

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Reconocer y notificar problemas

### Resultados de aprendizaje

Usted podrá (1) describir el comportamiento normal de Elmstead; (2) detectar una orden que no encaja con el calendario; (3) describir lo que vio con los nombres de ATT&CK for ICS; y (4) redactar un informe breve y basado en hechos.

### 3.1 Primero, lo normal

El controlador de planta sigue un calendario diario: descarga en el pico de la mañana, carga a mediodía, cuando la producción solar es alta, y vuelve a descargar por la tarde. Las órdenes proceden de SC-1. Los inicios de sesión ocurren durante los trabajos planificados. Ponerlo por escrito es lo que permite a cualquiera reconocer lo anómalo.

```python
"""Lab 3: compare synthetic battery charge commands with the agreed daily schedule."""
schedule = {"06": "discharge", "12": "charge", "18": "discharge"}
commands = [("06", "discharge", "site-controller"), ("12", "charge", "site-controller"),
            ("14", "discharge", "remote-portal"), ("18", "discharge", "site-controller")]
for hour, cmd, src in commands:
    ok = schedule.get(hour) == cmd and src == "site-controller"
    print(f"{hour}:00 {cmd:9} from {src:15} {'expected' if ok else 'UNEXPECTED - report'}")
```

Ejecútelo con `python3 lab_soc.py`. Salida verificada:

```text
06:00 discharge from site-controller expected
12:00 charge    from site-controller expected
14:00 discharge from remote-portal   UNEXPECTED - report
18:00 discharge from site-controller expected
```

Una descripción escrita de lo normal no necesita ser detallada para ser útil. El Lab 3 trabaja con tres horas programadas y un único origen esperado, y eso ya basta para que una orden extraña destaque. Cuando la planta cambie, por ejemplo cuando el operador de la red pida un patrón distinto por la tarde, el calendario escrito debe actualizarse, o el laboratorio señalará órdenes legítimas.

### 3.2 Lectura del laboratorio

Tres órdenes coinciden con el calendario y proceden de SC-1. A las 14:00 llegó una orden de descarga desde el portal remoto del fabricante: hora equivocada y origen equivocado. Puede ser una prueba del fabricante, un error o el uso indebido de credenciales robadas; no se puede saber solo con esta línea, y no hace falta. Usted lo notifica. El laboratorio tiene además un punto ciego: cualquier orden a una hora que no figure en el calendario se señala, aunque proceda de SC-1. Eso es aceptable para una lista corta, porque una falsa alarma cuesta poco, pero una planta real necesitaría un calendario más completo. Lo que importa aquí es que Jonah notifique hechos sin adivinar qué explicación es la verdadera.

### 3.3 Poner nombre a lo que vio

MITRE ATT&CK for ICS ofrece nombres compartidos: T0836 Modify Parameter para los ajustes modificados, T0886 Remote Services para el uso indebido de las vías de acceso remoto, T0831 Manipulation of Control para las órdenes no autorizadas al proceso. Úselos para describir observaciones, no para acusar. Para el suceso de las 14:00 en Elmstead, la orden en sí encaja con Manipulation of Control, y su vía a través del portal del fabricante encaja con Remote Services. Ninguna de las dos etiquetas dice quién lo hizo ni por qué. Simplemente permiten que la ingeniera, el fabricante y cualquiera que lea el informe más tarde entiendan qué tipo de comportamiento se observó, con palabras que significan lo mismo para todos.

### 3.4 Otras señales de alerta

Temperaturas de las baterías que suben sin carga; ajustes de los inversores modificados sin ticket; dispositivos nuevos en la red; pantallas que no coinciden con los medidores locales; cuentas que inician sesión a horas extrañas; alarmas silenciadas. Ninguna de estas señales demuestra un ataque; muchas se deben a sensores averiados, a un mantenimiento apresurado o a un cambio olvidado. Su valor está en que cada una difiere de lo normal por escrito y puede comprobarse. Una persona en prácticas que advierta una debe anotar cuándo y dónde la vio, conservar cualquier captura de pantalla o línea de registro y trasladarla a la persona de guardia en lugar de investigar por su cuenta.

### 3.5 Notificar

Avise de inmediato a la ingeniera de la planta o a la persona de guardia. Indique qué, dónde, cuándo, el estado actual y lo que usted ha hecho. Conserve la evidencia: capturas de pantalla, líneas de registro, horas. No cambie ajustes, no reinicie dispositivos ni contacte usted mismo con el fabricante salvo que se lo pidan. Un mensaje breve enviado con rapidez es mejor que uno completo enviado tarde. El informe de Jonah sobre la orden de las 14:00 cabe en cinco frases y aun así da a la ingeniera lo que necesita para decidir. Las horas deben incluir la zona horaria o indicar que son la hora local de la planta, porque los registros del portal y los de la planta pueden no usar el mismo reloj.

### 3.6 La seguridad física va primero

Si una batería se está sobrecalentando, siga primero el procedimiento de incendios y seguridad de la planta; las cuestiones de ciberseguridad esperan. En Elmstead eso significa dar la alarma, mantenerse alejado del recinto de las baterías y seguir los pasos de evacuación y de incendio de la ficha de la planta. La persona de guardia puede decidir más tarde si el sobrecalentamiento tuvo una causa de seguridad. La evidencia que se pierde mientras se protege a las personas es un precio aceptable; una persona herida por salvar un archivo de registro no lo es. El personal de seguridad física nunca debe esperar una respuesta de ciberseguridad.

### Ejemplo resuelto (Elmstead sintético)

Jonah notifica: «Hoy a las 14:00, el BESS recibió una orden de descarga desde el portal remoto del fabricante, fuera del calendario (el calendario indica carga de 12:00 a 18:00). La batería se está descargando ahora. No he cambiado nada. Exportación del registro guardada.» La ingeniera llama al fabricante, que no tiene constancia de ninguna sesión; la cuenta del portal se desactiva y su contraseña se restablece con MFA obligatoria.

> **Caso sintético — Elmstead.** La orden y la respuesta son inventadas.

### Errores y límites

La mayoría de los sucesos inesperados son errores o averías; notifíquelos igualmente. Los registros de las nubes pueden llegar tarde o con zonas horarias distintas.

### Ejercicios — capítulo 3

- **EX027 — Describir lo normal.** Describa el patrón diario normal de la batería de Elmstead. *Rúbrica:* 3 = descarga por la mañana, carga a mediodía, descarga por la tarde, desde SC-1; 2 = parcial; 1 = vago; 0 = nada.
- **EX028 — Dos anomalías.** ¿Qué dos cosas hacen inesperada la orden de las 14:00? *Rúbrica:* 3 = hora equivocada respecto al calendario y origen equivocado (el portal); 2 = una; 1 = vago; 0 = nada.
- **EX029 — Posibles explicaciones.** Dé tres posibles explicaciones de la orden de las 14:00. *Rúbrica:* 3 = prueba del fabricante, error, credenciales robadas; 2 = dos; 1 = una; 0 = nada.
- **EX030 — Variante del laboratorio.** Si la línea de las 14:00 procediera de `site-controller` con `charge`, ¿qué imprimiría el laboratorio? *Rúbrica:* 3 = línea UNEXPECTED, con el motivo de que la hora 14 no tiene entrada en el calendario; 2 = solo UNEXPECTED; 1 = `expected`; 0 = nada.
- **EX031 — Técnica para las órdenes.** ¿Qué técnica de ATT&CK for ICS encaja con una orden de descarga no autorizada? *Rúbrica:* 3 = T0831 Manipulation of Control; 2 = solo el nombre; 1 = incorrecto; 0 = nada.
- **EX032 — Técnica para la vía.** ¿Qué técnica encaja con el uso indebido del portal del fabricante como vía de entrada? *Rúbrica:* 3 = T0886 Remote Services; 2 = solo el nombre; 1 = incorrecto; 0 = nada.
- **EX033 — Cinco señales de alerta.** Enumere cinco señales de alerta en una planta de baterías. *Rúbrica:* 3 = cinco señales verosímiles; 2 = cuatro; 1 = dos; 0 = nada.
- **EX034 — Hechos del informe.** ¿Qué hechos debe contener el informe de Jonah? *Rúbrica:* 3 = qué, dónde, cuándo, estado actual, acciones realizadas (evidencia); 2 = cuatro; 1 = dos; 0 = nada.
- **EX035 — Sin tocar nada.** ¿Por qué Jonah no reinicia SC-1 tras detectar la orden? *Rúbrica:* 3 = podría perturbar el proceso o la seguridad física y destruir evidencia; la decisión corresponde a la ingeniera; 2 = uno; 1 = debería reiniciar; 0 = nada.
- **EX036 — Primero, el sobrecalentamiento.** Aparece una alarma de temperatura de un bastidor de baterías mientras Jonah redacta su informe. ¿Qué va primero? *Rúbrica:* 3 = el procedimiento de incendios y seguridad de la planta, avisar a la persona de guardia; el informe, después; 2 = solo avisar; 1 = terminar el informe; 0 = nada.
- **EX037 — Seguimiento con el fabricante.** ¿Qué se consiguió al desactivar la cuenta del portal y exigir MFA? *Rúbrica:* 3 = se detuvo el uso posterior de credenciales posiblemente robadas; los futuros inicios de sesión necesitan un segundo factor; 2 = parcial; 1 = vago; 0 = nada.
- **EX038 — Zonas horarias.** ¿Por qué debe anotar Jonah la zona horaria de las entradas de los registros en la nube? *Rúbrica:* 3 = la nube puede registrar en UTC; las horas desajustadas confunden la secuencia; 2 = parcial; 1 = sin motivo; 0 = nada.

### Síntesis del capítulo

Ponga por escrito lo normal, advierta lo que no encaja, descríbalo con claridad usando nombres compartidos y notifíquelo sin tocar nada.

### Siga estudiando — capítulo 03 de 04

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Hábitos seguros, nociones de respuesta y próximos pasos

### Resultados de aprendizaje

Usted podrá (1) practicar los hábitos cotidianos que protegen una instalación de TO; (2) esbozar los primeros pasos de una respuesta a incidentes; (3) explicar los límites de seguridad física y legales del trabajo de seguridad; y (4) planificar su próximo curso.

### 4.1 Hábitos cotidianos

Use solo memorias USB entregadas por la planta y analizadas antes de usarlas. Nunca conecte dispositivos desconocidos a los equipos de la planta. Bloquee la pantalla. Mantenga las contraseñas fuera de la vista y fuera del chat. Notifique con rapidez la pérdida de tarjetas de acceso y portátiles. No instale software en los ordenadores de la planta. Estos hábitos bloquean las vías más comunes por las que entran el malware y los intrusos. Cada hábito cierra una vía sencilla. Una memoria USB encontrada puede llevar malware directamente más allá de todos los cortafuegos; una pantalla desbloqueada en la sala de control permite a cualquiera enviar órdenes en su nombre; una contraseña compartida en un chat puede leerse mucho después de terminar la conversación. Estas pequeñas normas importan sobre todo en instalaciones como Elmstead, por donde pasan muchos visitantes y contratistas.

### 4.2 Responder a un incidente

NIST SP 800-82r3 insiste en planificar la respuesta junto con operaciones. En Elmstead los pasos son: poner a salvo a las personas y los equipos siguiendo los procedimientos de la planta; llamar a la ingeniera de guardia; anotar lo que ve; conservar la evidencia; dejar que la ingeniera y el responsable del incidente decidan la contención, como desconectar el portal del fabricante o poner la batería en un estado de reposo seguro; restaurar a partir de copias de seguridad verificadas; aprender y mejorar.

El papel de una persona en prácticas en esta lista corresponde sobre todo a los cuatro primeros pasos. La contención y la restauración son decisiones de quienes entienden cómo reaccionarán SC-1, los inversores y la batería, y pueden acordarlas con el operador de la red si hace falta. Elmstead tiene los pasos en una ficha en la sala de control para que nadie tenga que recordarlos bajo presión.

### 4.3 Actualizaciones y dispositivos

Los fabricantes publican correcciones de firmware; el propietario las aplica en momentos planificados tras comprobar la compatibilidad. Para los dispositivos nuevos, haga a los proveedores preguntas basadas en ETSI EN 303 645 y NIST IR 8259: contraseñas únicas, una política de divulgación de vulnerabilidades, un periodo de actualizaciones y comunicación cifrada. Las respuestas deben figurar en el inventario junto al dispositivo. Una cámara sin periodo de actualizaciones, o un controlador cuyo fabricante no dice cómo notificar una debilidad, es un riesgo que el propietario debe conocer antes de comprar y no después de instalar. Siempre que sea posible, las actualizaciones de firmware se prueban primero en una unidad, con una forma de volver a la versión anterior.

### 4.4 Límites

Nunca pruebe, escanee ni inicie sesión en sistemas que no esté autorizado a usar. Nunca eluda los sistemas de seguridad física, como la detección de incendios o la protección de las baterías. Nunca comparta código de explotación ni instrucciones de ataque. El aprendizaje se hace con simuladores y equipos de laboratorio. Estar en la planta no cambia estos límites. Una persona en prácticas que vea una página de inicio de sesión expuesta, o a la que un técnico amable del fabricante le dé una contraseña, sigue sin tener autorización para usarla. Lo correcto es notificar lo encontrado a la ingeniera. La autorización la concede el propietario, por escrito, para una tarea definida.

### 4.5 Próximos pasos

El siguiente curso de este plan de estudios trata la infraestructura crítica y la seguridad sectorial. Los cursos más largos de esta área profundizan en redes, protocolos, supervisión y diseño. Lleve un registro de los ejercicios completados. Antes de seguir, vuelva al caso de Elmstead y compruebe que puede explicar con sus propias palabras cada uno de sus sucesos: la lista de inversores, las zonas, la orden de las 14:00 y el simulacro de la cámara. Anote en qué ejercicios obtuvo menos de tres y vuelva a esos capítulos. Los cursos más largos de esta área se apoyan precisamente en estos fundamentos.

### Ejemplo resuelto (Elmstead sintético)

Durante un simulacro, Jonah encuentra una cámara que muestra una pantalla de inicio de sesión desconocida. Sigue la ficha de la pared de la sala de control: avisa a la ingeniera de guardia, fotografía la pantalla, anota la hora y no toca nada. La ingeniera aísla la zona de cámaras en su cortafuegos; la zona de control sigue funcionando. En la revisión posterior, Jonah propone añadir a la ficha el número de soporte del fabricante de las cámaras.

> **Caso sintético — Elmstead.** El simulacro es inventado.

### Errores y límites

Estos hábitos reducen el riesgo, pero no pueden eliminarlo. Los procedimientos varían según la planta; siga las normas locales.

### Ejercicios — capítulo 4

- **EX039 — Lista de hábitos.** Enumere cuatro hábitos cotidianos que protegen Elmstead. *Rúbrica:* 3 = cuatro hábitos correctos; 2 = tres; 1 = uno; 0 = nada.
- **EX040 — Memoria encontrada.** Alguien ha dejado una memoria USB en el escritorio de SC-1. ¿Qué hace usted? *Rúbrica:* 3 = no conectarla; entregarla a la ingeniera o a seguridad; anotar dónde se encontró; 2 = entregarla; 1 = revisarla; 0 = conectarla.
- **EX041 — Orden de la respuesta.** Ordene: conservar la evidencia; poner a salvo; restaurar; llamar a guardia; aprender. *Rúbrica:* 3 = poner a salvo, llamar, conservar, restaurar, aprender; 2 = casi todo; 1 = al azar; 0 = nada.
- **EX042 — Elección de la contención.** Nombre una acción de contención que podría tomar la ingeniera en Elmstead. *Rúbrica:* 3 = desconectar el portal, aislar una zona o poner la batería en reposo seguro, con el motivo; 2 = solo la acción; 1 = borrar registros; 0 = nada.
- **EX043 — Preguntas al proveedor.** Escriba dos preguntas para el proveedor de un nuevo monitor de baterías. *Rúbrica:* 3 = dos preguntas basadas en las configuraciones de referencia (contraseñas únicas, divulgación, actualizaciones, cifrado); 2 = una; 1 = el precio; 0 = nada.
- **EX044 — Momento del firmware.** ¿Por qué el firmware se aplica en momentos planificados y no de inmediato? *Rúbrica:* 3 = requiere comprobar la compatibilidad y una parada segura; riesgo de interrupción; 2 = parcial; 1 = sin motivo; 0 = nada.
- **EX045 — Entorno de práctica.** ¿Dónde debe practicar Jonah el uso de protocolos industriales? *Rúbrica:* 3 = simulador o equipos de laboratorio, no la planta en funcionamiento; 2 = parcial; 1 = en la planta, de noche; 0 = nada.
- **EX046 — Eludir la seguridad física.** Un compañero propone desactivar la protección de las baterías para «probar» una alarma. ¿Qué responde? *Rúbrica:* 3 = negarse; los sistemas de seguridad física no se tocan; escalarlo; 2 = negarse; 1 = aceptar con cuidado; 0 = aceptar.
- **EX047 — Lección del simulacro.** ¿Qué mejora propuso Jonah tras el simulacro, y por qué ayuda? *Rúbrica:* 3 = añadir a la ficha el número de soporte del fabricante; llamada correcta más rápida; 2 = solo la mejora; 1 = vago; 0 = nada.
- **EX048 — Efecto del aislamiento.** ¿Por qué pudo seguir funcionando la zona de control cuando se aisló la zona de cámaras? *Rúbrica:* 3 = zonas separadas; las cámaras no son necesarias para el control; 2 = parcial; 1 = se detuvo; 0 = nada.
- **EX049 — Compartir código de explotación.** ¿Por qué este curso se niega a compartir código de explotación? *Rúbrica:* 3 = doble uso; podría dañar instalaciones reales; el objetivo de aprendizaje es la defensa; 2 = parcial; 1 = sin motivo; 0 = nada.
- **EX050 — Siguiente curso.** ¿Qué trata el siguiente curso del plan de estudios? *Rúbrica:* 3 = infraestructura crítica y seguridad sectorial (curso 023); 2 = vago; 1 = incorrecto; 0 = nada.

### Síntesis del capítulo

Los buenos hábitos, una respuesta ensayada, el respeto de los límites de seguridad física y legales y el estudio continuado protegen las instalaciones de TO.

### Siga estudiando — capítulo 04 de 04

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Resultados resueltos ↓](#worked-results) · [Siguiente curso a través del índice de capítulos →](../SUBJECTS.md)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo para EX001–EX050. Elmstead Solar and Battery Site, Jonah Park y todas las cifras son sintéticos. Cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación.

**EX001.** La tecnología operacional es el hardware y el software que supervisa o controla dispositivos y procesos físicos, como inversores, bombas o líneas de producción.

**EX002.** Un dispositivo IoT percibe el mundo físico o actúa sobre él (una cámara, un contador o un sensor) y suele ser pequeño, de un solo propósito y estar conectado a una red o a la nube, mientras que un portátil es un ordenador de uso general para personas.

**EX003.** Una bomba de infusión hospitalaria: el software calcula y controla la dosis que entra en la vena del paciente, así que un error de cálculo se convierte en un efecto físico.

**EX004.** Convierte la corriente continua que producen los paneles solares en corriente alterna apta para la red.

**EX005.** La temperatura de las celdas de la batería y sus tensiones.

**EX006.** El controlador de planta SC-1, que sigue el calendario diario y las instrucciones del operador de la red.

**EX007.** La seguridad física va primero, porque una batería que se sobrecalienta puede arder y poner en peligro al personal y a los vecinos.

**EX008.** Podría descargar la batería en el momento equivocado, forzando las celdas, dejando sin energía almacenada al operador de la red cuando la necesite e inyectando en la red una potencia inesperada.

**EX009.** Que enormes cantidades de cámaras, enrutadores y dispositivos similares podían tomarse de forma automática probando nombres de usuario y contraseñas por defecto, y usarse después conjuntamente para ataques.

**EX010.** (a) IEC 62443; (b) ETSI EN 303 645; (c) MITRE ATT&CK for ICS.

**EX011.** CISA, la Agencia de Ciberseguridad y Seguridad de las Infraestructuras de EE. UU., los publica, a menudo junto con los fabricantes de los productos.

**EX012.** Los inversores INV-01 a INV-04, el BESS con su sistema de gestión de baterías, el controlador de planta SC-1, la conexión con el operador de la red y las cámaras.

**EX013.** No. Iniciar sesión en los equipos de la planta requiere la autorización del propietario y una función definida; un curso da conocimiento, no permiso.

**EX014.** Todos los controles posteriores (parches, segmentación, supervisión, respuesta) dependen de saber qué dispositivos existen, así que todo lo que falte en el inventario queda sin proteger.

**EX015.** Nombre del dispositivo, función, responsable, versión de firmware y dirección de red (además de la ubicación y la conexión con la nube).

**EX016.** Las contraseñas por defecto figuran en manuales públicos, así que cualquiera que pueda alcanzar INV-02 por la red o por el portal podría iniciar sesión y cambiar sus ajustes.

**EX017.** A INV-03 pueden faltarle correcciones de seguridad incluidas en la 5.1; consulte los avisos sobre la 4.7 y planifique una actualización con el fabricante.

**EX018.** `INV-04 cloud=no  old-fw 4.9` y `needs action: 3`.

**EX019.** La ingeniera del propietario de la planta, con el fabricante de los inversores, la cambia durante una visita planificada; no una persona en prácticas ni de forma improvisada.

**EX020.** La zona de control (SC-1, inversores, gestión de baterías), la zona de cámaras, la zona de oficina y la DMZ.

**EX021.** Un conducto es la vía de comunicación controlada que une dos zonas, con reglas definidas sobre lo que puede atravesarla.

**EX022.** Las cámaras suelen estar poco protegidas y enlazadas con internet; si una se viera comprometida dentro de la zona de control, el atacante podría alcanzar directamente SC-1 y los inversores.

**EX023.** T0883 Internet Accessible Device.

**EX024.** Los fabricantes solo se conectan a través de una única pasarela propiedad de la planta, con cuentas nominativas y autenticación multifactor. Las cuentas se activan para cada trabajo acordado, las sesiones se registran y el acceso se desactiva después.

**EX025.** ¿Puede el portal enviar órdenes a los equipos o solo mostrar datos? ¿Quién tiene cuentas en él? ¿Se exige autenticación multifactor en todas las cuentas?

**EX026.** No tiene autorización para hacerlo, y los escaneos pueden alterar dispositivos frágiles; los registros, los datos del equipo de redes y los recorridos por la planta permiten elaborar la lista con seguridad.

**EX027.** SC-1 descarga la batería en el pico de la mañana, la carga a mediodía, cuando la producción solar es alta, y vuelve a descargarla por la tarde, y todas las órdenes proceden de SC-1.

**EX028.** Llegó a las 14:00, cuando el calendario indica que la batería debería estar cargándose, y procedía del portal remoto del fabricante en lugar de SC-1.

**EX029.** Una prueba del fabricante no anunciada; un error de un operador o del fabricante en el portal; o alguien que usa credenciales robadas del portal.

**EX030.** `14:00 charge    from site-controller UNEXPECTED - report`: el calendario no tiene entrada para la hora 14, así que `schedule.get("14")` es `None` y la comprobación falla aunque el origen sea SC-1.

**EX031.** T0831 Manipulation of Control.

**EX032.** T0886 Remote Services.

**EX033.** Temperaturas de las baterías que suben sin carga; ajustes de los inversores modificados sin ticket; un dispositivo desconocido en la red; pantallas que no coinciden con los medidores locales; alarmas silenciadas.

**EX034.** Qué vio (una orden de descarga desde el portal), dónde (el BESS), cuándo (a las 14:00), qué está ocurriendo ahora (la batería se está descargando) y qué ha hecho (no ha cambiado nada, registro guardado).

**EX035.** Reiniciar el controlador podría interrumpir de forma insegura el calendario de la batería y de la red y borraría información sobre lo ocurrido; la ingeniera decide cualquier actuación.

**EX036.** Seguir el procedimiento de incendios y seguridad de la planta y avisar de inmediato a la persona de guardia; el informe de seguridad puede terminarse después.

**EX037.** Impidió que quien tuviera la contraseña antigua enviara más órdenes, y garantizó que cualquier inicio de sesión futuro en el portal exija un segundo factor además de la contraseña.

**EX038.** Los servicios en la nube a menudo registran las horas en UTC mientras la planta usa la hora local, así que sin la zona la secuencia de los hechos podría malinterpretarse por varias horas.

**EX039.** Usar solo memorias USB entregadas por la planta y analizadas; bloquear la pantalla al ausentarse; mantener las contraseñas fuera de la vista y fuera del chat; notificar con rapidez la pérdida de tarjetas de acceso y portátiles.

**EX040.** Dejarla sin conectar, anotar dónde y cuándo se encontró y entregarla a la ingeniera o al contacto de seguridad.

**EX041.** Poner a salvo; llamar a la ingeniera de guardia; conservar la evidencia; restaurar a partir de copias de seguridad verificadas; aprender y mejorar.

**EX042.** Desconectar el portal del fabricante para que ninguna orden remota pueda alcanzar SC-1, mientras la planta sigue funcionando con su calendario local.

**EX043.** «¿Tiene cada unidad una contraseña única u obliga a fijar una en el primer uso?» y «¿Durante cuántos años ofrecerán actualizaciones de seguridad?»

**EX044.** Hay que comprobar la compatibilidad de una actualización con SC-1 y aplicarla cuando el equipo pueda detenerse con seguridad; aplicarla en pleno funcionamiento podría interrumpir los flujos de potencia.

**EX045.** En un simulador de protocolos o en equipos de formación en un laboratorio, nunca en los dispositivos en funcionamiento de Elmstead.

**EX046.** Negarse: la protección de las baterías es un sistema de seguridad física que nunca se desactiva para hacer pruebas; notificar la propuesta a la ingeniera.

**EX047.** Añadir a la ficha de la pared el número de soporte del fabricante de las cámaras, para que la ingeniera de guardia pueda localizar de inmediato al experto adecuado en lugar de buscarlo.

**EX048.** Las cámaras están en una zona separada unida por un cortafuegos, y SC-1, los inversores y el sistema de gestión de baterías no dependen de ellas para funcionar.

**EX049.** El código de explotación es de doble uso: podría usarse contra plantas de energía reales y poner en peligro a personas, mientras que el objetivo del curso es proteger los sistemas, para lo que no se necesitan herramientas de ataque.

**EX050.** El curso 023: infraestructura crítica y seguridad sectorial.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; vuelva a verificar las ediciones antes de citarlas. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA. Cybersecurity advisories index (ICS advisories). <https://www.cisa.gov/news-events/cybersecurity-advisories>
- Antonakakis, M., et al. (2017). Understanding the Mirai Botnet. 26th USENIX Security Symposium. <https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/antonakakis>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- ISA/IEC 62443 series of standards (overview; zones and conduits from 62443-3-2, component requirements in 62443-4-2). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS: T0831 Manipulation of Control, T0836 Modify Parameter, T0883 Internet Accessible Device, T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
