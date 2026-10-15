# Infraestructura crítica y seguridad sectorial: coordinación, gobernanza y ejercicios para profesionales

- Idioma: español neutro (`es`); curso profesional, seis meses; aproximadamente 360 horas de estudio planificado (curso 046 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Los capítulos 1–12 de 12 tienen texto didáctico escrito, cinco laboratorios sin conexión, los ejercicios EX001–EX060 y sus resultados resueltos correspondientes. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: profesionales principiantes que van a **coordinar** la seguridad en una organización que presta un servicio esencial: coordinadores de seguridad o de resiliencia recién nombrados, supervisores de operaciones que han heredado funciones de ciberseguridad, responsables de riesgos y de cumplimiento, planificadores de continuidad y jefes de proyecto en agua, energía, sanidad, transporte, finanzas y servicios públicos. Conocimientos de entrada: nociones básicas de seguridad y una comprensión práctica de cómo se presta el servicio correspondiente.
- En qué se diferencia este curso de sus vecinos. El [libro técnico](../../../../technical-18-months/critical-sector-security/es/book/MANUSCRIPT.md) enseña profundidad práctica: decodificar protocolos, bastionar equipos, configurar cortafuegos. El [libro de tecnólogo](../../../../technologist-3-years/critical-sector-security/es/book/MANUSCRIPT.md) enseña a los implantadores a construir y traspasar un servicio supervisado. El [libro rápido](../../../../rapid-1-month/critical-sector-security/es/book/MANUSCRIPT.md) es una primera introducción. **Este libro profesional trata de coordinación y gobernanza**: quién decide, a quién se informa, quién rinde cuentas, cómo se clasifica y se acepta el riesgo, cómo se exigen responsabilidades a los proveedores, cómo se diseña y se evalúa un ejercicio de mesa y cómo se demuestra todo ello con evidencia ante un consejo de administración o un regulador. En este libro no configurará nada. Aprenderá a hacer las preguntas que garantizan que las personas adecuadas configuran lo adecuado, en el orden adecuado, y pueden demostrarlo.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos y no se relicencian aquí.
- Límite educativo: este curso es un proyecto educativo independiente. No es un programa acreditado, no otorga ninguna titulación y no concede autoridad sobre ninguna infraestructura, operador, conjunto de datos o persona reales, ni acceso a ellos. Toda organización, lugar, persona, contrato, plazo, línea de registro y cifra de un ejemplo resuelto o de un laboratorio es **sintética**, salvo que una frase cite explícitamente una fuente pública. Los plazos de notificación de «Kestrel Vale» son ilustrativos: las obligaciones reales proceden de su propia ley, de su regulador, de su licencia y de sus contratos. Nada de lo que aparece en este libro constituye asesoramiento jurídico, clínico o regulatorio.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los doce capítulos siguen a una **coordinadora de ciberresiliencia** recién nombrada durante seis meses en una empresa de agua de tamaño medio. El resultado del curso es **operar un flujo de coordinación repetible y comunicar los hallazgos** sobre la seguridad de las infraestructuras críticas, bajo supervisión.

- **Meses 1–2 (capítulos 1–4)**: construyen la base: para qué sirve un coordinador, el servicio y sus partes interesadas, el trabajo autorizado y los registros de decisión, y un registro de riesgos guiado por la consecuencia.
- **Meses 3–4 (capítulos 5–8)**: lo convierten en un programa en marcha: marcos y evaluaciones leídos con espíritu crítico, funciones y una matriz RACI, controles con responsable y verificados con evidencia, y un caso supervisado de acceso de proveedores.
- **Meses 5–6 (capítulos 9–12)**: lo ponen a prueba y lo presentan: notificación y comunicación de crisis, detección y corrección de fallos en el propio programa, un ejercicio de mesa completo y un portafolio final con una sesión informativa para el consejo.

Cada capítulo tiene resultados de aprendizaje, secciones didácticas con definiciones, un ejemplo resuelto, una actividad práctica, errores comunes y límites, cinco ejercicios numerados y una síntesis. Cinco capítulos contienen un breve laboratorio de Python. Los laboratorios no son lecciones de programación: cada uno es una lista de comprobación convertida en ejecutable, para que pueda ver exactamente qué regla señala qué registro y discutir con la regla. Usan solo la biblioteca estándar de Python 3 (las salidas de este borrador se produjeron con Python 3.13.5), no necesitan red, paquetes, privilegios ni datos reales, y cada salida se imprime en el texto. Puede completar todos los ejercicios sin ejecutar código leyendo la salida impresa. Escriba su respuesta a cada ejercicio antes de abrir los [resultados resueltos](#worked-results); la rúbrica de 0–3 muestra lo que premia un evaluador, y una respuesta distinta pero defendible puede obtener la máxima puntuación.

Mantenga cuatro etiquetas en toda nota de coordinación: **decidido** (qué se decidió, quién, cuándo y con qué fundamento), **supuesto** (aquello de lo que depende la decisión y que nadie ha comprobado), **debido** (lo que alguien ha prometido, a quién y para cuándo) y **abierto** (lo que se desconoce y quién lo está averiguando).

### El escenario sintético de este libro

| Elemento sintético | Papel en el libro | Límite |
|---|---|---|
| **Kestrel Vale**: una región ficticia con su propio regulador y su propio CSIRT nacional, también ficticios | Escenario de todos los ejemplos. | Lugar y ley inventados. |
| **Kestrel Water**: empresa de agua potable, 180.000 personas, planta de tratamiento KW-TW y estaciones de bombeo y dosificación KW-01 a KW-12 | La organización donde trabaja el lector. El lector es la **coordinadora de ciberresiliencia**, que depende del director de operaciones. | Inventado. |
| Personas: A. Mensah (jefe de operaciones), L. Ferreira (responsable de seguridad, a tiempo parcial desde el departamento de TI), J. Tan (ingeniero de sistemas de control), C. Okafor (atención al cliente y facturación), R. Adeyemi (comunicación), M. Holt (consejero delegado), E. Varga (director de operaciones), T. Lindqvist (presidente de la comisión de auditoría y riesgos del consejo) | Colegas. | Inventadas; ninguna persona real. |
| **Kestrel Vale Regional Operations Centre (KVROC)** | Servicio de supervisión compartido que usa la empresa. | Inventado. |
| **Kestrel Grid**, **Kestrel General Hospital** | Proveedor de electricidad y el cliente más crítico. | Inventados. |
| Proveedores HydroLogic Ltd, ScadaCo, Vale Pumps, MeterWorks, Northgate Integration | Terceros de los capítulos 8–11. | Inventados; cualquier parecido con empresas reales es accidental. |

Como los datos son sintéticos, el libro puede decirle lo que un coordinador real rara vez sabe con certeza. Úselo para aprender cómo fallan los programas, nunca como evidencia sobre organizaciones reales.

### Política de fuentes

Toda afirmación factual sobre un marco, una ley, una norma, un incidente público o una orientación publicada enlaza con una fuente consultada en octubre de 2026. Las normas, las orientaciones y las leyes cambian y difieren entre jurisdicciones: vuelva a verificar cada una antes de basarse en ella. El vocabulario corriente de gestión (RACI, dueño del riesgo, declaración provisional) no recibe una referencia inventada. Una cita respalda la afirmación general que la acompaña, nunca los detalles sintéticos. Los incidentes públicos se describen solo al nivel de detalle que publicaron sus autores.

### Reglas profesionales del trabajo de coordinación

1. Usted coordina; no se autoriza a sí mismo. Toda evaluación, prueba, sesión de proveedor o cambio necesita la aprobación de la persona dueña del servicio afectado (capítulo 3).
2. Operaciones tiene la última palabra sobre la seguridad física. Una recomendación de seguridad que pueda afectar al tratamiento, a la presión o a la dosificación pasa por el jefe de operaciones, siempre.
3. No pida nunca a nadie que «solo eche un vistazo» a un sistema de control en funcionamiento sin esa aprobación, y no reenvíe nunca credenciales, diagramas de red ni mapas de registros por correo electrónico o chat ordinarios.
4. Informe de lo que sabe, etiquete lo que supone y corrija con prontitud lo que se equivocó (capítulo 9).
5. Trate a las personas como la fortaleza del sistema. Los ejercicios ponen a prueba los planes, no a los individuos (capítulo 11).

## Contenido

1. [Fundamentos de seguridad para profesionales](#ch-01): servicios esenciales, consecuencia, el trabajo del coordinador y el lenguaje del riesgo.
2. [Contexto del servicio y de las partes interesadas](#ch-02): funciones críticas, dependencias y las personas que deben estar en la sala.
3. [Práctica autorizada y tratamiento de la evidencia](#ch-03): quién puede autorizar qué, registros de decisión e intercambio de información.
4. [Métodos fundamentales](#ch-04): un registro de riesgos guiado por la consecuencia, titularidad y aceptación. Lab 4.
5. [Herramientas e interpretación](#ch-05): marcos, evaluaciones, puntuaciones de madurez y métricas leídos con espíritu crítico.
6. [Flujo de trabajo operativo](#ch-06): funciones, una matriz RACI, gobernanza de cambios de TI/TO y escalado. Lab 6.
7. [Controles y verificación](#ch-07): titularidad de los controles, niveles de aseguramiento y excepciones limitadas en el tiempo.
8. [Análisis supervisado de un caso](#ch-08): un caso de acceso remoto de proveedores y la gobernanza de terceros. Lab 8.
9. [Comunicación, ética e informes](#ch-09): relojes de notificación, clientes críticos, declaraciones provisionales y honestidad. Lab 9.
10. [Calidad y diagnóstico de averías](#ch-10): diagnosticar un programa de coordinación que no funciona. Lab 10.
11. [Laboratorio supervisado](#ch-11): diseñar, conducir y evaluar un ejercicio de mesa.
12. [Portafolio de práctica y revisión final](#ch-12): portafolio, sesión informativa para el consejo y un plan de 90 días.

<a id="ch-01"></a>

## Capítulo 1 — Fundamentos de seguridad para profesionales

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- explicar qué hace que un servicio sea «esencial» y por qué su seguridad se juzga por la **consecuencia** para las personas, no por el daño a los ordenadores;
- describir el trabajo del coordinador y distinguirlo del del ingeniero, del analista de seguridad y del directivo;
- usar el vocabulario básico del riesgo (activo, amenaza, vulnerabilidad, probabilidad, consecuencia, dueño del riesgo, apetito de riesgo) con la precisión suficiente para que los colegas puedan actuar a partir de sus frases;
- situar su trabajo dentro de un marco reconocido (las seis funciones del NIST Cybersecurity Framework 2.0) sin confundir el marco con el trabajo.

Este capítulo solo presupone nociones básicas de seguridad. Todo lo que viene después en el libro se apoya en las distinciones que se hacen aquí.

### 1.1 Qué es un servicio esencial

Un **servicio esencial** es aquel cuya interrupción perjudica a las personas, a la economía o al orden público con rapidez y a gran escala: agua potable, electricidad, sanidad, transporte, pagos, comunicaciones de emergencia. Los gobiernos los enumeran de forma distinta. Estados Unidos agrupa dieciséis sectores de infraestructura crítica ([CISA, Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors)) y describe las **funciones críticas nacionales** subyacentes (por ejemplo, «suministrar agua» o «prestar atención médica») que atraviesan los sectores ([CISA, National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set)). La Directiva NIS2 de la Unión Europea nombra sectores de «alta criticidad» e impone obligaciones a las entidades esenciales e importantes, también a sus órganos de dirección ([Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)).

La idea útil de todas estas listas es la misma: lo que hay que proteger es una **función prestada a las personas**, no un edificio ni un servidor. Kestrel Water no existe para hacer funcionar ordenadores; existe para que 180.000 personas puedan beber agua segura a una presión adecuada a todas horas, todos los días. Sus ordenadores importan en la medida en que la función depende de ellos.

### 1.2 Primero, la consecuencia

En una oficina, la tríada clásica de la seguridad suele recitarse como confidencialidad, integridad y disponibilidad, en ese orden. En un servicio esencial, el orden de preocupación suele cambiar. La guía del NIST sobre seguridad de la tecnología operativa señala que los sistemas de TO afectan directamente al mundo físico y que sus prioridades (la seguridad de las personas, la disponibilidad y la integridad del control) difieren de las prioridades habituales de TI ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

Para un coordinador esto tiene un significado práctico. Cuando clasifique un problema, pregunte en este orden:

1. **¿Podría hacer daño a alguien?** (dosis química errónea, pérdida de presión en un hospital, un trabajador expuesto a una bomba en movimiento);
2. **¿Podría detener el servicio, durante cuánto tiempo y para cuántas personas?**
3. **¿Podría hacer que el servicio deje de ser fiable**, con operadores que ya no están seguros de que las pantallas muestren la verdad?
4. **¿Podría exponer información**: datos de clientes, diseños de red, informes de vulnerabilidades?

Una brecha de datos en el sistema de facturación es grave y puede acarrear obligaciones legales, pero un cambio silencioso en una consigna de cloro es un problema de otra categoría. Un coordinador que no sepa explicar esa diferencia en una frase ante un consejo verá cómo el dinero va al lugar equivocado.

### 1.3 El trabajo del coordinador

El director de operaciones de Kestrel Water, E. Varga, redactó la descripción del nuevo puesto. Su núcleo son tres verbos: **conectar**, **posibilitar decisiones** y **evidenciar**.

- **Conectar.** Operaciones, TI, ingeniería, atención al cliente, comunicación, los proveedores y la dirección tienen cada uno una parte del panorama. El coordinador se asegura de que las partes se encuentren: de que las personas adecuadas se enteren a tiempo de un riesgo, un cambio o un incidente.
- **Posibilitar decisiones.** El coordinador rara vez toma las decisiones importantes. El jefe de operaciones decide si una estación funciona en manual; el consejero delegado decide qué decir al público. El coordinador se asegura de que la decisión tenga un responsable, la información que necesita, un plazo y un registro.
- **Evidenciar.** El coordinador puede mostrar a un consejo, a un auditor o a un regulador qué se decidió, por qué y si se llevó a cabo.

El coordinador **no** es el ingeniero que reconfigura el cortafuegos, ni el analista que lee los registros, ni el directivo que acepta el riesgo. Confundir estas funciones es el fallo más común de los coordinadores nuevos: o intentan hacer ellos mismos el trabajo técnico (y pierden de vista el programa) o toman decisiones que corresponden a alguien con autoridad sobre el servicio (y después son desautorizados o culpados).

### 1.4 El vocabulario del riesgo

Las palabras precisas ahorran horas de reuniones. Las definiciones siguientes siguen el uso común de [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), simplificado para la práctica:

- **Activo**: cualquier cosa de la que depende el servicio: equipos, software, datos, personas, proveedores, edificios.
- **Amenaza**: circunstancia o actor con potencial de causar daño (un grupo delictivo, una actualización descuidada, una inundación).
- **Vulnerabilidad**: debilidad que una amenaza podría explotar (una cuenta de proveedor sin autenticación multifactor).
- **Probabilidad**: lo probable que es que el daño se produzca en un periodo dado, teniendo en cuenta los controles existentes.
- **Consecuencia** (o impacto): lo que les ocurre al servicio y a las personas si se produce.
- **Riesgo**: la combinación: una afirmación de qué podría ocurrir, cómo, con qué probabilidad y con qué gravedad.
- **Dueño del riesgo**: la persona con autoridad y presupuesto para decidir cómo se trata el riesgo. Normalmente, un responsable del servicio afectado, no el coordinador.
- **Apetito de riesgo**: cuánto riesgo está dispuesta a aceptar la dirección de la organización para alcanzar sus objetivos, declarado de antemano.
- **Tratamiento**: reducir, evitar, transferir (por ejemplo, mediante un seguro o un contrato) o aceptar el riesgo.

Una declaración de riesgo bien formada tiene una causa, un evento y una consecuencia: «*Como* la cuenta remota del proveedor de bombas no tiene segundo factor, *un atacante con la contraseña del proveedor podría* iniciar sesión en los controladores de las estaciones *y cambiar las consignas de las bombas, causando* pérdida de presión a hasta 20.000 clientes, entre ellos el hospital». Compárela con «riesgo de acceso de proveedores», que nadie puede asumir como dueño ni tratar.

### 1.5 Los marcos como mapas

El NIST Cybersecurity Framework 2.0 organiza los resultados en seis funciones: **Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar** (*Govern, Identify, Protect, Detect, Respond, Recover*) ([NIST CSWP 29, The NIST Cybersecurity Framework 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)). La versión 2.0 añadió Gobernar, que abarca la estrategia, las funciones, la política, la gestión de riesgos y el riesgo de la cadena de suministro: la mayor parte de lo que trata este libro. El Cyber Assessment Framework del Reino Unido, escrito para operadores de servicios esenciales, se organiza en torno a objetivos como gestionar el riesgo de seguridad y minimizar el impacto de los incidentes ([NCSC, Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf)).

Un marco es un mapa de resultados. Le dice lo que consigue un buen programa, no cómo debe conseguirlo su empresa de servicios, y desde luego no que usted ya lo haya conseguido. El capítulo 5 muestra cómo leer las evaluaciones basadas en marcos sin dejarse engañar por ellas.

### 1.6 Ejemplo resuelto: la primera semana (sintético)

El primer día, la nueva coordinadora recibe tres peticiones:

1. El departamento de TI le pide que «dé el visto bueno» a un nuevo antivirus para los ordenadores de la sala de control antes del viernes.
2. El presidente de la comisión de auditoría del consejo, T. Lindqvist, pide «nuestra puntuación de riesgo cibernético» para la comisión del mes que viene.
3. El jefe de operaciones, A. Mensah, menciona que un proveedor de bombas «a veces se conecta desde casa» para reparar la estación KW-07.

Una respuesta débil las trata como tres tareas. La respuesta de una coordinadora las ordena por consecuencia y por quién es dueño de la decisión:

| Petición | Pregunta sobre la consecuencia | ¿De quién es la decisión? | Acción de la coordinadora |
|---|---|---|---|
| Antivirus en los PC de la sala de control | ¿Podría el producto bloquear o ralentizar las pantallas del operador? (NIST SP 800-82 advierte de que las herramientas de TI pueden perturbar la TO) | Jefe de operaciones, asesorado por el ingeniero de sistemas de control y el proveedor | Preguntar a J. Tan si el proveedor del sistema de control admite el producto; organizar una prueba en una máquina que no sea de producción; **no** dar el visto bueno en solitario. |
| La «puntuación de riesgo» del consejo | ¿Qué decisión tomará el consejo con ella? | Consejo (apetito); dirección (tratamiento) | Ofrecer, en lugar de un único número, una lista breve de los principales riesgos ordenados por consecuencia, con responsables y fechas (capítulo 4). |
| Conexiones del proveedor desde casa | ¿Podría otra persona usar ese acceso para cambiar los ajustes de las bombas? | El jefe de operaciones es dueño de la estación; el responsable de seguridad asesora | Registrarlo como riesgo candidato con una declaración completa de causa, evento y consecuencia; programar una revisión del acceso de proveedores (capítulo 8). |

El tercer asunto, mencionado de pasada, es el de mayor consecuencia. Los coordinadores aprenden a oír el riesgo en la conversación.

### 1.7 Actividad práctica

Elija un servicio esencial que conozca (su propio empleador o uno público descrito en una noticia). Escriba, en no más de una página: la función que presta a las personas; tres cosas de las que depende; y una declaración de riesgo bien formada, con causa, evento y consecuencia. Marque qué partes conoce y cuáles supone. Después entregue la página a un colega y pídale que nombre al dueño del riesgo solo a partir de su declaración. Si no puede, probablemente la consecuencia o el servicio afectado son demasiado vagos. Compare su función con la frase de Kestrel Water sobre agua segura a una presión adecuada para 180.000 personas: nombra a quién se sirve y qué necesita.

### 1.8 Errores comunes y límites

- Tratar la «seguridad» como propiedad del departamento de TI. En un servicio esencial, operaciones es dueño de la consecuencia.
- Escribir los riesgos como sustantivos («ransomware», «personal interno») en lugar de como afirmaciones que alguien pueda asumir.
- Pedir una única puntuación de riesgo. Las puntuaciones ocultan qué servicio, qué personas y qué decisión.
- Confundir un perfil del marco con evidencia de que los controles funcionan.
- Este capítulo simplifica: los métodos reales de riesgo (capítulo 4) necesitan calibración, datos y juicio, y las leyes difieren entre países.

- Dar el visto bueno a un cambio que corresponde a otra persona, como evitó la coordinadora con la petición del antivirus para los ordenadores de la sala de control.
- Tratar un comentario de pasada, como el de un proveedor que a veces se conecta desde casa, como charla trivial en lugar de como un riesgo candidato.

### Ejercicios — capítulo 1

**EX001 — Reescriba los riesgos.** *Objetivo:* producir declaraciones de riesgo que alguien pueda asumir. *Insumos:* las entradas del registro «ransomware», «PC antiguos» y «acceso de proveedores». *Pasos:* reescribir cada una como una declaración de causa, evento y consecuencia situada en Kestrel Water. *Evidencia esperada:* tres declaraciones. *Rúbrica:* 3 = cada una tiene una causa, un evento y una consecuencia para el servicio medida en personas o en tiempo, y nombra la función afectada; 2 = a una le falta la consecuencia; 1 = siguen siendo genéricas; 0 = nada.

**EX002 — Orden de preocupación.** *Objetivo:* aplicar la clasificación por consecuencia. *Insumos:* cuatro eventos: (a) un intruso copia la base de datos de facturación; (b) las pantallas del operador en KW-03 se congelan durante 40 minutos; (c) la consigna de cloro de KW-05 se cambia sin aprobación; (d) un diagrama de la red interna se envía por correo a una dirección equivocada. *Pasos:* ordenarlos y justificarlo. *Evidencia esperada:* clasificación con una frase para cada uno. *Rúbrica:* 3 = (c) primero por razones de seguridad de las personas, (b) segundo por la pérdida de visión y la posible pérdida de control, después (d) y (a) con un razonamiento sobre a quién se perjudica y cómo; señala que las obligaciones legales pueden hacer que (a) siga siendo urgente; 2 = solo los dos primeros correctos; 1 = pone (a) primero sin razonamiento; 0 = nada.

**EX003 — Límites de la función.** *Objetivo:* separar la coordinación de la autoridad. *Insumos:* la petición del antivirus de 1.6. *Pasos:* escribir el correo que enviaría a TI y a A. Mensah. *Evidencia esperada:* dos mensajes breves. *Rúbrica:* 3 = rechaza dar el visto bueno en solitario, nombra al dueño de la decisión, pide la compatibilidad del proveedor, una prueba fuera de producción y un plan de reversión, y propone una fecha; 2 = dueño correcto sin pedir la prueba; 1 = da el visto bueno; 0 = nada.

**EX004 — Asociación con el CSF 2.0.** *Objetivo:* usar un marco como mapa. *Insumos:* las tres peticiones de 1.6. *Pasos:* asignar cada una a una o más funciones del CSF 2.0 y explicarlo. *Evidencia esperada:* tres asignaciones. *Rúbrica:* 3 = antivirus → Proteger (y Gobernar por los derechos de decisión); puntuación de riesgo → Gobernar; conexiones del proveedor → Gobernar (cadena de suministro) e Identificar/Proteger; señala que la etiqueta de una función no es evidencia; 2 = etiquetas sin razones; 1 = una etiqueta; 0 = nada.

**EX005 — Oiga el riesgo.** *Objetivo:* detectar el riesgo en la conversación. *Insumos:* el comentario «el turno de noche deja la puerta de la estación calzada abierta porque el lector de tarjetas es lento». *Pasos:* escribir una declaración de riesgo, nombrar a un probable dueño y una pregunta que haría antes de proponer cualquier solución. *Evidencia esperada:* declaración, dueño, pregunta. *Rúbrica:* 3 = la declaración vincula el acceso físico con los equipos de control y la consecuencia; el dueño es el responsable de la estación o el jefe de operaciones; la pregunta respeta por qué lo hace el personal (por ejemplo, cuánto tarda y si la puerta se necesita como salida de emergencia); 2 = sin pregunta; 1 = culpa al personal; 0 = nada.

### Síntesis del capítulo

Un servicio esencial es una función prestada a las personas, y su seguridad se mide por la consecuencia: seguridad de las personas, continuidad, fiabilidad y, después, confidencialidad. El coordinador conecta a las personas que tienen partes del panorama, se asegura de que las decisiones tengan responsables y registros, y conserva la evidencia. Las declaraciones de riesgo precisas y un marco usado como mapa (no como prueba) son las primeras herramientas del oficio.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 12

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Infraestructura crítica y seguridad sectorial: contexto del servicio y de las partes interesadas

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- describir un servicio crítico como una cadena de funciones y dependencias, aguas arriba y aguas abajo;
- construir un mapa de partes interesadas que distinga quién decide, a quién hay que informar y quién puede ayudar;
- reconocer en qué difieren los sectores (agua, energía, sanidad, transporte, finanzas) en cuanto a lo que significa «daño» y quién lo regula;
- identificar los efectos en cascada entre sectores y la coordinación que exigen.

El capítulo 1 definió el servicio por su consecuencia. Este capítulo dibuja las personas y las dependencias que lo rodean.

### 2.1 Un servicio es una cadena

El agua potable de Kestrel Water recorre una cadena: captación del río, tratamiento en KW-TW, dosificación química, bombeo y almacenamiento en KW-01 a KW-12, distribución, medición y facturación. Cada eslabón depende de cosas que la empresa no controla del todo: la electricidad de Kestrel Grid, los productos químicos que llegan por carretera, las telecomunicaciones para la telemetría, un servicio de supervisión en el KVROC, el software y el mantenimiento de los proveedores, y personas con competencias escasas. Las funciones críticas nacionales de la CISA describen esta visión a escala nacional: funciones como «suministrar agua» dependen de otras como «suministrar electricidad» y «prestar servicios de contenidos, información y comunicación basados en internet» ([CISA, National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set)). La versión del coordinador es local y concreta: un mapa de dependencias de una página que un responsable nuevo pueda leer en cinco minutos.

### 2.2 Aguas arriba, aguas abajo, compartidas

A un coordinador le importan tres tipos de dependencia:

- **Aguas arriba**: lo que necesita el servicio: electricidad, productos químicos, comunicaciones, proveedores, personal.
- **Aguas abajo**: quién necesita el servicio y con qué urgencia: hogares, escuelas, la unidad de esterilización y la diálisis del hospital, los hidrantes contra incendios, los negocios de alimentación.
- **Compartidas**: componentes o personas de los que dependen varias funciones a la vez: un único operador de telecomunicaciones para toda la telemetría, un único ingeniero del proveedor que conoce todas las estaciones, un único centro de supervisión compartido.

Las dependencias compartidas son el lugar donde un evento aislado se convierte en una interrupción extensa. A menudo, la pregunta más valiosa de un coordinador en cualquier reunión es: «*¿Qué más usa eso?*».

### 2.3 Las partes interesadas y sus funciones

Una **parte interesada** es cualquiera que influye en la seguridad del servicio o se ve afectado por ella. Para coordinar, clasifique a cada una según lo que necesita de ella:

| Clase | Significado | Ejemplos en Kestrel Water |
|---|---|---|
| **Decide** | Tiene autoridad sobre el servicio, el presupuesto o el mensaje público | Consejero delegado, director de operaciones, jefe de operaciones, consejo |
| **Ejecuta** | Lleva a cabo el trabajo | Ingeniero de sistemas de control, TI, proveedores, analistas del KVROC, operadores de turno |
| **Debe ser informada** | Tiene derecho legal, contractual o de seguridad a saber | Regulador y CSIRT nacional, Kestrel General Hospital, autoridad de salud pública, aseguradora |
| **Puede ayudar** | Ofrece capacidad o información | Grupo sectorial de intercambio de información, CSIRT nacional, socios de ayuda mutua, sala de control de Kestrel Grid |
| **Se ve afectada** | Sufre la consecuencia | Clientes, personal, empresas de servicios vecinas |

Una misma parte interesada puede estar en varias clases. El hospital «debe ser informado» cuando la calidad del agua o la presión están en riesgo y también «se ve afectado»; además puede «ayudar» diciéndole cuáles de sus sistemas necesitan más el agua.

### 2.4 En qué difieren los sectores

El patrón de coordinación es común, pero el significado del daño y el panorama regulatorio difieren:

- **Agua**: la salud pública es la consecuencia dominante; los operadores suelen gestionar instalaciones pequeñas con poco personal; con frecuencia es posible operar en manual durante un tiempo. La CISA y sus socios han publicado avisos específicos para el agua tras ataques a controladores expuestos a internet ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)).
- **Electricidad**: equilibrio en tiempo real y fallos en cascada entre redes; las interrupciones afectan a todos los demás sectores. Los ataques de 2015 contra empresas de distribución ucranianas causaron cortes a los clientes y fueron seguidos de una restauración manual ([CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01)).
- **Sanidad**: seguridad del paciente y continuidad clínica; muchos dispositivos médicos conectados; el personal clínico decide sobre el desvío de pacientes y los procedimientos de funcionamiento degradado.
- **Transporte y oleoductos**: seguridad de los desplazamientos y del suministro de combustible; los sistemas de negocio pueden forzar paradas operativas aunque los sistemas de control no se hayan tocado. En el caso del ransomware DarkSide de 2021, la CISA y el FBI publicaron un aviso sobre ataques a la red de TI de una empresa de infraestructura crítica ([CISA AA21-131A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a)).
- **Finanzas**: integridad de las transacciones y confianza pública; una regulación ya sólida de la resiliencia operativa.

La lección profesional: cuando coordine entre sectores (agua con electricidad, hospital con agua), traduzca su consecuencia a la de ellos. «Estación KW-02 fuera de servicio» no significa nada para el hospital; «presión más baja en la zona este desde las 14:00 hasta cerca de las 18:00, con el agua apta para beber» sí.

### 2.5 Ejemplo resuelto: la dependencia del hospital (sintético)

El Kestrel General Hospital se abastece de la zona este, alimentada por las estaciones KW-02 y KW-07. La coordinadora hace cuatro preguntas y registra las respuestas:

| Pregunta | Respuesta (sintética) | Fuente |
|---|---|---|
| ¿Para qué usa el hospital el agua que no puede esperar? | Servicios de esterilización, diálisis, cocinas, extinción de incendios, refrigeración de la unidad de diagnóstico por imagen | Responsable de instalaciones del hospital, reunión del 12 de febrero |
| ¿Cuánto tiempo puede arreglárselas sin suministro de la red? | Unas 6 horas con agua almacenada para los usos prioritarios | Plan de continuidad de negocio del propio hospital (no visto; supuesto) |
| ¿A quién del hospital hay que llamar, de día y de noche? | Guardia de instalaciones; fuera de horario, el responsable de turno del centro | Confirmado por la centralita del hospital |
| ¿Qué promete nuestro contrato o acuerdo? | Una llamada en las 2 horas siguientes a cualquier evento que pueda afectar al suministro o a la calidad | Acuerdo de suministro, cláusula 7 |

A continuación, la coordinadora marca «6 horas» como **supuesto**, porque no ha visto el plan. Un supuesto del que depende una decisión es una tarea: pide ver la sección correspondiente. Este patrón (registrar la fuente y el grado de confianza de cada dato de dependencia) recorre todo el libro.

### 2.6 Actividad práctica

Dibuje un mapa de dependencias de un servicio esencial con al menos cinco dependencias aguas arriba, tres aguas abajo y una compartida. Para cada una, nombre un contacto e indique si ha verificado la información o la ha supuesto. Use la tabla del hospital como modelo: para cada dependencia, registre la respuesta, su fuente y si vio usted mismo la evidencia. Todo dato marcado como supuesto debería convertirse en una tarea, con una persona a quien preguntar. Feche el mapa e indique quién lo revisará, porque los proveedores, los contactos y los tiempos de autonomía cambian. Un mapa sin ninguna dependencia compartida suele significar que aún no ha preguntado qué más usa el operador de telecomunicaciones, el servicio de supervisión o ese único ingeniero que conoce todas las estaciones.

### 2.7 Errores comunes y límites

- Cartografiar sistemas en lugar de funciones: una lista de servidores no es un mapa de dependencias.
- Olvidar a las personas como dependencias (un único experto, un único responsable de guardia).
- Tratar a las partes interesadas que «deben ser informadas» como opcionales hasta que hay un incidente.
- Los mapas de dependencias se quedan obsoletos; féchelos y asigne un responsable de la revisión.

- Aceptar el tiempo de autonomía de un cliente crítico sin ver el plan del que procede, como evitó la coordinadora con las seis horas del hospital.
- Describir una interrupción en sus propios términos a otro sector, en lugar de decir lo que significa para él, como una presión más baja desde las 14:00 hasta cerca de las 18:00 con el agua apta para beber.

### Ejercicios — capítulo 2

**EX006 — Clasifique a las partes interesadas.** *Objetivo:* usar las cinco clases. *Insumos:* el regulador, el KVROC, HydroLogic Ltd, una escuela local, el consejero delegado, la sala de control de Kestrel Grid. *Pasos:* clasificar a cada uno, admitiendo más de una clase. *Evidencia esperada:* tabla con una razón por fila. *Rúbrica:* 3 = clases defendibles, con varias clases donde se justifica (por ejemplo, Kestrel Grid como dependencia aguas arriba, «puede ayudar» y también «debe ser informada» si cambia la carga de la empresa); 2 = una clase para cada uno; 1 = varias erróneas; 0 = nada.

**EX007 — Encuentre la dependencia compartida.** *Objetivo:* identificar puntos únicos. *Insumos:* la telemetría de las doce estaciones usa un único operador de telecomunicaciones; el KVROC supervisa tres empresas de servicios; un único ingeniero de HydroLogic atiende todas las estaciones. *Pasos:* explicar la consecuencia de perder cada uno y la pregunta de coordinación que plantearía. *Evidencia esperada:* tres análisis breves. *Rúbrica:* 3 = reconoce la pérdida de visión de todas las estaciones (operador), el impacto compartido entre empresas y la supervisión reducida (KVROC) y el riesgo de persona clave (ingeniero); plantea «qué más usa eso» y la contingencia; 2 = dos de tres; 1 = solo enumera; 0 = nada.

**EX008 — Traduzca la consecuencia.** *Objetivo:* comunicarse entre sectores. *Insumos:* «KW-07 funcionará en manual desde las 10:00 durante seis horas por una sospecha de compromiso del enlace del proveedor». *Pasos:* reescribirlo para el responsable de instalaciones del hospital. *Evidencia esperada:* mensaje de menos de 80 palabras. *Rúbrica:* 3 = expone el efecto sobre el suministro en los términos del hospital (presión, seguridad, duración), lo que el hospital debe hacer, la hora de la próxima actualización y el contacto; evita los detalles técnicos y la especulación; 2 = falta la próxima actualización; 1 = reenvía la frase técnica; 0 = nada.

**EX009 — Verifique un supuesto.** *Objetivo:* gestionar el grado de confianza. *Insumos:* el supuesto de las «6 horas» de 2.5. *Pasos:* describir cómo lo verificaría y qué haría si la cifra real fuera de 2 horas. *Evidencia esperada:* plan y consecuencia. *Rúbrica:* 3 = pide la sección concreta del plan o una reunión con instalaciones y registra la fecha y la fuente; con 2 horas, la promesa de notificación en 2 horas se vuelve insuficiente, así que se revisa el acuerdo y se planifica con el hospital un suministro alternativo (camiones cisterna); 2 = solo verificación; 1 = acepta el supuesto; 0 = nada.

**EX010 — Diferencia entre sectores.** *Objetivo:* reconocer el significado sectorial del daño. *Insumos:* la misma infección de ransomware en la TI de negocio de (a) una empresa de agua y (b) un operador de oleoductos de combustible. *Pasos:* explicar por qué cada uno podría parar las operaciones aunque los sistemas de control estén limpios, citando el aviso público pertinente cuando proceda. *Evidencia esperada:* dos párrafos. *Rúbrica:* 3 = explica la dependencia de las operaciones respecto de las funciones de negocio (facturación, programación, supervisión) y la cautela ante la propagación, cita AA21-131A solo al nivel en que se publicó y evita afirmaciones que vayan más allá; 2 = genérico; 1 = supone que se atacó la TO; 0 = nada.

### Síntesis del capítulo

Un servicio crítico es una cadena de funciones con dependencias aguas arriba, aguas abajo y compartidas, y un conjunto de partes interesadas que deciden, ejecutan, deben ser informadas, pueden ayudar o se ven afectadas. Los sectores difieren en lo que significa el daño, así que un coordinador traduce las consecuencias a los términos del sector que las recibe. Registre la fuente y el grado de confianza de cada dato de dependencia; un supuesto sin verificar detrás de una decisión es una tarea.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Práctica autorizada y tratamiento de la evidencia

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- explicar quién puede autorizar trabajos de seguridad en un servicio esencial y qué contiene una autorización válida;
- redactar un **registro de decisión** que resistiría las preguntas de un regulador o de un auditor un año después;
- gestionar la evidencia que produce un programa de coordinación: qué conservar, dónde, durante cuánto tiempo y quién puede verla;
- compartir información sensible con los socios usando un esquema de marcado acordado (el Traffic Light Protocol).

El capítulo 2 identificó quién decide. Este capítulo hace que sus decisiones sean explícitas, queden registradas y puedan compartirse con seguridad.

### 3.1 Por qué la autorización es un problema de coordinación

El trabajo de seguridad en un servicio esencial (una evaluación, un escaneo de vulnerabilidades, una sesión de mantenimiento de un proveedor, una prueba de penetración, incluso «solo mirar» la configuración de un controlador) puede afectar al servicio. En los entornos de control, el NIST señala que algunas actividades rutinarias de TI, entre ellas el escaneo activo, pueden perturbar las operaciones ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). La autorización existe para que la persona responsable de la consecuencia acepte de antemano lo que va a ocurrir y para que todos puedan demostrar después lo que se acordó.

El coordinador suele ser la persona que **prepara** una autorización: redacta el alcance, obtiene las firmas adecuadas, la distribuye y la conserva. Rara vez es la persona que la **concede**.

### 3.2 Qué contiene una autorización válida

Use los elementos siguientes para cualquier evaluación, prueba o trabajo de terceros en sistemas operativos de la planta. La guía de pruebas del NIST describe reglas de actuación con un contenido similar para las evaluaciones técnicas ([NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)).

| Elemento | Pregunta a la que responde |
|---|---|
| Finalidad | ¿Por qué se hace este trabajo? |
| Sistemas dentro y fuera del alcance | Exactamente qué instalaciones, sistemas y cuentas; y cuáles quedan excluidos (por ejemplo, los controladores de dosificación y los sistemas de seguridad) |
| Actividades permitidas y prohibidas | Qué se puede hacer (leer la configuración, revisar documentos) y qué no (escribir, reiniciar, escanear activamente) |
| Personas | Quién hará el trabajo, con nombre, y quién lo supervisa |
| Ventana | Fecha y hora de inicio y de fin, con zona horaria |
| Condiciones | Presencia de operaciones; condiciones de parada; canal de comunicación |
| Tratamiento de los datos | Qué se puede copiar, dónde se guarda y cuándo se destruye |
| Autoridad | Nombre, cargo y firma del dueño del servicio (y del responsable del proveedor cuando proceda) |

Una **condición de parada** es un evento acordado de antemano que pone fin al trabajo de inmediato: «cualquier alarma inesperada en la estación; cualquier petición de un operador; cualquier pérdida de visión en las pantallas del operador». Las condiciones de parada convierten el «tenga cuidado» en algo comprobable.

### 3.3 Registros de decisión

La coordinación produce decisiones: aceptar un riesgo, aplazar un parche, aislar una estación, notificar a un regulador. Un **registro de decisión** es una nota breve y fechada que recoge:

1. la decisión, en una frase;
2. quién la tomó y con qué autoridad;
3. las opciones consideradas y por qué se eligió esta;
4. la información disponible en ese momento y lo que se desconocía;
5. las condiciones y la fecha de revisión («revisar si el proveedor publica una corrección, o antes del 30 de junio»);
6. a quién se informó.

El sentido del punto 4 es la equidad con quien toma la decisión. Una decisión tomada a las 02:00 con información parcial puede ser buena aunque el resultado sea malo. Sin un registro, la retrospectiva reescribe la historia. Con él, una organización puede aprender qué decisiones fueron malas y cuáles tuvieron mala suerte.

### 3.4 Tratamiento de la evidencia para un coordinador

Un coordinador maneja evidencia de tres tipos:

- **Evidencia de gobernanza**: autorizaciones, registros de decisión, aceptaciones de riesgo, actas de reuniones, informes de ejercicios. Se conserva como registro de la organización; proteja su integridad (quién cambió qué) y consérvela según la política.
- **Evidencia de incidentes**: registros, imágenes y correos reunidos durante un incidente. Su recopilación es trabajo técnico; el coordinador se asegura de que se solicite pronto, de que se registre su custodia y de que el acceso esté limitado. La orientación del NIST sobre respuesta a incidentes insiste en prepararse para la recopilación de evidencia antes de que ocurran los incidentes ([NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)).
- **Información de diseño sensible**: diagramas de red, informes de vulnerabilidades, listas de acceso de proveedores. No es evidencia de una infracción, pero resulta muy útil para un atacante. Guárdela en una ubicación con control de acceso, nunca en hilos de correo generales.

Tres reglas prácticas: una única ubicación de referencia por tipo de registro; un responsable con nombre para cada ubicación; y ningún secreto (contraseñas, claves) en ningún registro.

### 3.5 Compartir: el Traffic Light Protocol

Los socios (el CSIRT nacional, un grupo sectorial de intercambio de información, el hospital) necesitan información para protegerse. El **Traffic Light Protocol (TLP)** es un esquema de marcado de uso extendido que indica a los destinatarios hasta dónde pueden compartirla ([FIRST, TLP 2.0](https://www.first.org/tlp/)):

- **TLP:RED**: solo para los destinatarios nombrados;
- **TLP:AMBER**: los destinatarios pueden compartirla dentro de su organización y con sus clientes cuando necesiten conocerla; **TLP:AMBER+STRICT** la limita a la organización del destinatario;
- **TLP:GREEN**: puede compartirse dentro de la comunidad del destinatario, no públicamente;
- **TLP:CLEAR**: sin restricción más allá de los derechos de autor habituales.

El TLP marca el permiso para compartir, no una clasificación de confidencialidad, y no sustituye a las obligaciones legales. Marque la línea de asunto y el comienzo del mensaje, y elija la etiqueta menos restrictiva que siga protegiendo a las personas.

### 3.6 Ejemplo resuelto: autorizar la evaluación de un proveedor (sintético)

ScadaCo ofrece una «revisión del estado de seguridad» gratuita del sistema de control de la planta de tratamiento. La coordinadora redacta la autorización:

- **Finalidad:** revisar la configuración de los servidores de supervisión frente a la guía de bastionado de ScadaCo.
- **Dentro del alcance:** los dos servidores de supervisión de KW-TW y su documentación. **Fuera del alcance:** todos los controladores de las estaciones, el sistema de dosificación y el cortafuegos de red.
- **Permitido:** revisión de solo lectura de los archivos de configuración exportados y entrevista supervisada con J. Tan. **Prohibido:** escanear la red, instalar software, cambiar cualquier ajuste, copiar datos fuera de la instalación salvo el informe final.
- **Personas:** M. Ilic (ScadaCo), supervisado por J. Tan.
- **Ventana:** 21 de abril de 2026, de 09:00 a 13:00, hora local.
- **Condiciones de parada:** cualquier petición de un operador; cualquier alarma en KW-TW.
- **Tratamiento de los datos:** el informe se marca TLP:AMBER+STRICT, se entrega mediante el servicio seguro de transferencia de archivos acordado y se guarda en la biblioteca de registros de seguridad; ScadaCo borra las notas de trabajo en un plazo de 14 días y lo confirma por escrito.
- **Autoridad:** A. Mensah (jefe de operaciones, dueño de KW-TW); el responsable de servicio de ScadaCo refrenda.

Ese día, M. Ilic pide «ejecutar rápidamente una herramienta de descubrimiento para comprobar las versiones». J. Tan se niega, porque la autorización prohíbe el escaneo, y registra la petición. El registro de decisión anota la negativa y que la comprobación de versiones se hará a partir de la documentación. Así es como debe funcionar la autorización.

### 3.7 Actividad práctica

Tome cualquier visita rutinaria de un proveedor en una organización que conozca y escriba su autorización con el formato de tabla de 3.2. Marque qué elementos no pudo completar; esas son las lagunas de la práctica de esa organización. Elija una visita que afecte a un sistema que preocuparía a alguien, como una sesión de mantenimiento de un controlador, y no la del personal de limpieza o una entrega. Escriba las condiciones de parada como eventos que cualquiera en la instalación pueda reconocer. Después pregunte a la persona que firmaría como dueña del servicio si está de acuerdo con su alcance y sus exclusiones; su respuesta suele revelar un sistema que olvidó. Guarde juntos su borrador y los comentarios de esa persona como evidencia de la laguna que encontró.

### 3.8 Errores comunes y límites

- Un «OK verbal» de alguien sin autoridad sobre el servicio.
- Un alcance redactado como «la red de TO», sin exclusiones.
- Sin condiciones de parada, o con condiciones de parada que nadie en la instalación conoce.
- Registros de decisión redactados después de conocerse el resultado.
- Enviar información de diseño como adjuntos de correo ordinarios.
- Usar el TLP como si fuera una clasificación legal o para ocultar información a quien la necesita.

- Dejar que el proveedor redefina el trabajo el mismo día, como habría hecho la petición de ScadaCo de ejecutar una herramienta de descubrimiento si J. Tan no la hubiera rechazado.
- No dejar constancia de una negativa, de modo que un revisor posterior no puede ver que la autorización se hizo cumplir.

### Ejercicios — capítulo 3

**EX011 — Repare una autorización.** *Objetivo:* encontrar los elementos que faltan. *Insumos:* «OK para que Northgate haga una prueba de penetración en la red de TO la semana que viene — A. Mensah (por chat)». *Pasos:* enumerar los elementos que faltan y reescribirla. *Evidencia esperada:* lista de lagunas y reescritura. *Rúbrica:* 3 = identifica finalidad, alcance y exclusiones, actividades permitidas/prohibidas, personas con nombre, ventana con zona horaria, condiciones de parada, tratamiento de los datos y autoridad escrita; la reescritura excluye los sistemas de seguridad y de dosificación y prefiere métodos no intrusivos; 2 = la mayoría de los elementos; 1 = retoques menores; 0 = nada.

**EX012 — Redacte un registro de decisión.** *Objetivo:* registrar una decisión con equidad. *Insumos:* a las 02:10, el responsable de turno decidió mantener KW-05 en automático pese a un inicio de sesión remoto sin explicar, porque operar en manual exigía llamar al personal, con 90 minutos de espera. *Pasos:* redactar el registro de seis partes. *Evidencia esperada:* el registro. *Rúbrica:* 3 = las seis partes, con las incógnitas del momento (si el inicio de sesión era malicioso), las condiciones (vigilar los valores de dosificación, revisar a las 06:00) y a quién se informó; 2 = faltan opciones o incógnitas; 1 = solo una narración; 0 = nada.

**EX013 — Elija una etiqueta TLP.** *Objetivo:* aplicar TLP 2.0. *Insumos:* (a) indicadores de una campaña de phishing dirigida a empresas de agua, para enviar al grupo sectorial; (b) un informe que nombra los modelos de controlador sin parchear de Kestrel Water, para el KVROC; (c) una nota pública de consejos para los clientes. *Pasos:* elegir las etiquetas y justificarlas. *Evidencia esperada:* tres etiquetas. *Rúbrica:* 3 = (a) GREEN (beneficio para la comunidad), (b) AMBER+STRICT o RED (sensible para la empresa; el KVROC lo necesita), (c) CLEAR; con razones; 2 = etiquetas sin razones; 1 = todo RED; 0 = nada.

**EX014 — Ubicaciones de la evidencia.** *Objetivo:* organizar la evidencia de gobernanza. *Insumos:* autorizaciones en la bandeja de entrada de un ingeniero, aceptaciones de riesgo en las actas del consejo, informes de ejercicios en una unidad compartida, listas de acceso de proveedores en una hoja de cálculo enviada por correo cada mes. *Pasos:* proponer un esquema. *Evidencia esperada:* esquema de un párrafo con responsables. *Rúbrica:* 3 = una única ubicación de referencia con control de acceso por tipo de registro, responsables con nombre, conservación, historial de versiones, dejar de enviar por correo las listas de acceso; 2 = ubicación sin responsables; 1 = «usar SharePoint»; 0 = nada.

**EX015 — Prueba de las condiciones de parada.** *Objetivo:* hacer comprobable la cautela. *Insumos:* una actualización de firmware de un proveedor en KW-09, programada de 13:00 a 15:00. *Pasos:* escribir tres condiciones de parada e indicar quién tiene autoridad para invocarlas. *Evidencia esperada:* condiciones y autoridad. *Rúbrica:* 3 = condiciones observables (alarma inesperada, pérdida de visión, prolongación más allá de las 15:00, petición del operador) y el operador de turno o el jefe de operaciones pueden parar sin justificarlo; 2 = condiciones vagas; 1 = decide el proveedor; 0 = nada.

### Síntesis del capítulo

La autorización hace que el dueño de la consecuencia acepte de antemano exactamente lo que va a ocurrir y permite que todos lo demuestren después. Una autorización válida tiene un alcance con exclusiones, actividades permitidas y prohibidas, personas con nombre, una ventana, condiciones de parada, tratamiento de los datos y autoridad escrita. Los registros de decisión recogen lo que se sabía en ese momento; la evidencia de gobernanza reside en ubicaciones controladas y con responsable; el TLP indica a los socios hasta dónde pueden compartir.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Siga estudiando — capítulo 03 de 12

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Infraestructura crítica y seguridad sectorial: métodos fundamentales

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- conducir un ciclo de evaluación de riesgos sencillo y repetible para un servicio esencial y mantener un registro de riesgos útil;
- explicar por qué multiplicar la probabilidad por la consecuencia puede inducir a error en las infraestructuras críticas y cómo clasificar primero por consecuencia;
- asegurarse de que cada riesgo tenga un dueño, un tratamiento, una fecha límite y una fecha de revisión, y detectar cuándo no los tiene;
- registrar correctamente la aceptación de un riesgo, con autoridad, condiciones y caducidad.

Los capítulos 1–3 le dieron el lenguaje, el contexto y los registros. Este capítulo los convierte en el método central del coordinador.

### 4.1 El ciclo de evaluación de riesgos

El NIST describe la evaluación de riesgos como un proceso de preparar, realizar, comunicar y mantener la evaluación ([NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)). Para un coordinador, un ciclo practicable tiene cinco pasos:

1. **Enmarcar**: qué servicio, qué horizonte temporal, qué consecuencias cuentan y cuál es el apetito de la dirección.
2. **Identificar**: reunir riesgos candidatos a partir de incidentes, auditorías, conversaciones con el personal, revisiones de proveedores, avisos y ejercicios.
3. **Analizar**: escribir cada uno como causa, evento y consecuencia; estimar la probabilidad y la consecuencia con las personas que conocen el tema.
4. **Decidir**: el dueño del riesgo elige un tratamiento y una fecha; la aceptación se eleva al nivel de autoridad adecuado.
5. **Supervisar**: revisar según un calendario y cuando algo cambia; informar hacia arriba de los principales riesgos.

El registro es la memoria de este ciclo. Si el registro está desactualizado, el ciclo se ha detenido, diga lo que diga la política.

### 4.2 Las escalas y sus límites

La mayoría de las organizaciones puntúan la probabilidad y la consecuencia en escalas de 1 a 5. Deles sentido anclando cada nivel en los términos de su servicio. Una escala de consecuencia para Kestrel Water podría ser:

| Nivel | Consecuencia (anclada) |
|---|---|
| 5 | Riesgo para la salud o la vida; llega agua no segura a los clientes; o pérdida del suministro a un cliente crítico más allá de su tiempo de autonomía |
| 4 | Pérdida de suministro o de presión para más de 10.000 personas durante más de 12 horas; probable actuación sancionadora del regulador |
| 3 | Pérdida localizada del suministro; coste significativo; exposición de datos de clientes con obligación de notificar |
| 2 | Perturbación absorbida mediante operación manual; coste interno |
| 1 | Efecto insignificante sobre el servicio |

El producto habitual, probabilidad × consecuencia, es cómodo, pero tiene dos problemas conocidos. Primero, permite que un problema menor y frecuente supere a uno catastrófico y raro (4 × 3 = 12 gana a 2 × 5 = 10). Segundo, los números son etiquetas ordinales, no mediciones, así que la aritmética con ellos es más débil de lo que parece. En los servicios esenciales, una convención sensata es clasificar **primero por consecuencia** (todo lo que pueda dañar a las personas o superar el tiempo de autonomía de un cliente crítico va arriba) y usar el producto solo para ordenar riesgos de consecuencia similar. Sea cual sea la regla que elija, póngala por escrito para que la clasificación sea reproducible y discutible.

### 4.3 Titularidad e higiene

Un riesgo sin dueño es una preocupación, no un riesgo gestionado. La higiene del registro significa que cada entrada tiene: un dueño con autoridad sobre el servicio afectado; una decisión de tratamiento; una fecha límite para el tratamiento; una fecha de última revisión; y un enlace a la evidencia del avance. Un coordinador comprueba la higiene con regularidad, porque el deterioro del registro es silencioso: nadie se da cuenta de que un riesgo «alto» se revisó por última vez hace ocho meses hasta que ocurre algo.

En el Lab 4, R02 muestra los tres fallos a la vez: sin dueño, una revisión de hace siete meses y un tratamiento vencido, en un riesgo de nivel 5.

### 4.4 Aceptar el riesgo

La aceptación es un tratamiento legítimo: ninguna organización puede arreglarlo todo a la vez. Una aceptación correcta registra quién aceptó el riesgo (con un nivel de autoridad acorde con su consecuencia), qué medidas compensatorias se aplican, en qué condiciones decae la aceptación y cuándo caduca. La NIS2 exige que los órganos de dirección de las entidades esenciales e importantes aprueben las medidas de gestión de riesgos de ciberseguridad y supervisen su aplicación ([Directive (EU) 2022/2555, Article 20](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)). Sea cual sea su jurisdicción, los riesgos con consecuencias de nivel 5 deben ser aceptados por la dirección o por el consejo, nunca discretamente por el coordinador.

### 4.5 Ejemplo resuelto: revisar el registro (sintético)

En marzo, la coordinadora revisa el registro de Kestrel Water antes de la comisión de auditoría y riesgos del consejo. Usa el **Lab 4**, que codifica la convención de clasificación y las comprobaciones de higiene para que cualquiera pueda volver a ejecutarlas. **Lab 4** (guárdelo como `lab04.py` y ejecútelo con `python3 lab04.py`):

```python
# Lab 4 - consequence-led risk register review (offline, standard library only; all data synthetic)
import datetime as dt
TODAY = dt.date(2026, 3, 2)
# id, title, owner, likelihood 1-5, consequence 1-5, service affected, last review, treatment due
REGISTER = [
    ("R01", "Remote vendor access to station RTUs without MFA", "A. Mensah", 4, 5, "drinking water", "2026-01-10", "2026-04-30"),
    ("R02", "Single engineer knows chlorine dosing logic",       "",          3, 5, "drinking water", "2025-08-01", "2026-02-01"),
    ("R03", "Billing portal phishing of customer accounts",      "C. Okafor", 5, 3, "billing",        "2026-02-20", "2026-06-30"),
    ("R04", "Historian backups never test-restored",             "J. Tan",    3, 4, "drinking water", "2025-12-15", "2026-01-31"),
    ("R05", "Grid supply loss at pumping station KW-07",         "A. Mensah", 2, 5, "drinking water", "2026-02-01", "2026-09-30"),
    ("R06", "Office printer firmware outdated",                  "IT desk",   4, 1, "office IT",      "2026-02-25", "2026-05-31"),
    ("R07", "Hospital not told of planned pressure work",        "L. Ferreira",3, 4, "hospital supply","2025-06-30", "2026-03-31"),
]
SERVICE_WEIGHT = {"drinking water": 3, "hospital supply": 3, "billing": 1, "office IT": 0}
rows = []
for rid, title, owner, l, c, svc, rev, due in REGISTER:
    score = l * c
    flags = []
    if not owner: flags.append("NO OWNER")
    if (TODAY - dt.date.fromisoformat(rev)).days > 180: flags.append("REVIEW STALE")
    if dt.date.fromisoformat(due) < TODAY: flags.append("TREATMENT OVERDUE")
    if c == 5: flags.append("SEVERE CONSEQUENCE")
    rows.append((score, c, SERVICE_WEIGHT[svc], rid, title, flags))
print("Ranked by score only:")
for score, c, w, rid, title, flags in sorted(rows, key=lambda r: (-r[0], r[3])):
    print(f"  {rid} score={score:2d}")
print("Ranked by consequence, then service weight, then score:")
for i, (score, c, w, rid, title, flags) in enumerate(sorted(rows, key=lambda r: (-r[1], -r[2], -r[0], r[3])), 1):
    print(f"  {i}. {rid} c={c} w={w} score={score:2d} {'; '.join(flags) or 'ok'}")
print("Needs governance action:", ", ".join(r[3] for r in sorted(rows, key=lambda r: r[3]) if any(f != 'SEVERE CONSEQUENCE' for f in r[5])))
```

Salida esperada (Python 3.13.5):

```text
Ranked by score only:
  R01 score=20
  R02 score=15
  R03 score=15
  R04 score=12
  R07 score=12
  R05 score=10
  R06 score= 4
Ranked by consequence, then service weight, then score:
  1. R01 c=5 w=3 score=20 SEVERE CONSEQUENCE
  2. R02 c=5 w=3 score=15 NO OWNER; REVIEW STALE; TREATMENT OVERDUE; SEVERE CONSEQUENCE
  3. R05 c=5 w=3 score=10 SEVERE CONSEQUENCE
  4. R04 c=4 w=3 score=12 TREATMENT OVERDUE
  5. R07 c=4 w=3 score=12 REVIEW STALE
  6. R03 c=3 w=1 score=15 ok
  7. R06 c=1 w=0 score= 4 ok
Needs governance action: R02, R04, R07
```

Lea las dos clasificaciones. Solo por puntuación, el riesgo de phishing de facturación R03 (15) empata con R02 y queda por encima de R05, una pérdida del suministro eléctrico en una estación de bombeo que podría dejar sin agua a miles de personas. Clasificados por consecuencia y después por la importancia del servicio afectado, los tres riesgos de nivel 5 sobre el agua potable van primero. Los indicadores de higiene muestran dónde falla la gobernanza, no la tecnología: R02 (un único ingeniero que entiende la lógica de dosificación de cloro) **no tiene dueño**, lleva siete meses sin revisarse y su tratamiento está vencido; la prueba de restauración de R04 está vencida; la revisión de R07 está obsoleta. Estos tres van a la comisión como **acciones de gobernanza**, con una propuesta de dueño para R02 (A. Mensah, dueño de la dosificación).

Fíjese en lo que el laboratorio no hace. No le dice si la «probabilidad 4» de R01 es correcta; eso sale de la conversación con las personas que conocen al proveedor y la amenaza. Hace explícita la regla de clasificación y repetibles las comprobaciones de higiene; no emite el juicio por usted.

### 4.6 Actividad práctica

Cambie la clave de clasificación del Lab 4 para ordenar solo por puntuación y muestre el resultado a un colega. Pregúntele qué orden defendería en una reunión del consejo tras un fallo de presión en el hospital. Después escriba en dos frases la regla de clasificación de su organización. Fíjese en dónde quedan R03 y R05 en cada orden, porque esa es la discusión a la que se enfrentaría tras una interrupción: un riesgo de phishing de facturación clasificado por encima de una pérdida de suministro en una estación de bombeo es difícil de defender. Después añada un riesgo inventado con consecuencia 5 y probabilidad 1 y compruebe dónde cae con cada regla. Por último, ejecute las comprobaciones de higiene con otra fecha TODAY, por ejemplo seis meses después, y vea qué revisiones y tratamientos se vuelven obsoletos o vencen sin que nadie lo note.

### 4.7 Errores comunes y límites

- Escalas sin anclas, de modo que un «4» significa cosas distintas para personas distintas.
- Aritmética con puntuaciones ordinales presentada como precisión («riesgo 13,6»).
- Dueños que son coordinadores o comités en lugar de responsables con autoridad.
- Aceptaciones sin caducidad, que se vuelven permanentes por defecto.
- Registros que enumeran tecnologías («SCADA») en lugar de declaraciones de riesgo.
- Tratar el registro como el objetivo; es solo la memoria de las decisiones.

- Dejar un riesgo de nivel 5 sin dueño porque nadie lo quiere, como le ocurrió a R02 durante meses.
- Puntuar la probabilidad sin hablar con las personas que conocen al proveedor o la amenaza, de modo que el número refleja la conjetura del coordinador.

### Ejercicios — capítulo 4

**EX016 — Ancle una escala.** *Objetivo:* dar sentido a la probabilidad. *Insumos:* la escala de consecuencia de 4.2. *Pasos:* escribir una escala de probabilidad de cinco niveles anclada en el tiempo y en la evidencia. *Evidencia esperada:* la escala. *Rúbrica:* 3 = niveles ligados a periodos o a evidencia (por ejemplo, 5 = ha ocurrido aquí en el último año o se está intentando activamente en el sector; 1 = sin casos conocidos en el sector, necesitaría varias condiciones improbables); señala que se tienen en cuenta los controles existentes; 2 = solo periodos; 1 = palabras como «alto»; 0 = nada.

**EX017 — Lea el Lab 4.** *Objetivo:* interpretar la clasificación y la higiene. *Insumos:* la salida del Lab 4. *Pasos:* explicar por qué R03 pasa de segundo empatado a sexto y por qué R05 sube; enumerar las acciones de gobernanza y quién debería ser dueño de cada una. *Evidencia esperada:* explicación y lista. *Rúbrica:* 3 = R03 tiene consecuencia 3 sobre la facturación; R05 tiene consecuencia 5 sobre el agua potable; acciones: dueño de R02 (A. Mensah) y tratamiento vencido, prueba de restauración vencida de R04 (J. Tan, con A. Mensah como dueño del servicio), revisión obsoleta de R07 (L. Ferreira, o traspasarla a la coordinadora por la relación con el hospital); 2 = explicación sin dueños; 1 = repite la salida; 0 = nada.

**EX018 — Acepte un riesgo correctamente.** *Objetivo:* registrar la aceptación. *Insumos:* el consejo decide que este año no puede financiar la sustitución de los controladores de la estación KW-10. *Pasos:* redactar el registro de aceptación. *Evidencia esperada:* el registro. *Rúbrica:* 3 = nombra la declaración de riesgo, la autoridad que acepta (consejero delegado o consejo, dada la consecuencia), las medidas compensatorias (por ejemplo, sin acceso remoto, supervisión por el KVROC, piezas de repuesto), las condiciones que ponen fin a la aceptación (nuevo aviso, incidente), la fecha de caducidad y el responsable de la revisión; 2 = sin caducidad; 1 = «aceptado»; 0 = nada.

**EX019 — Amplíe el laboratorio.** *Objetivo:* codificar otra regla de higiene. *Insumos:* el Lab 4. *Pasos:* añadir un indicador «ACCEPTANCE EXPIRED» usando un campo nuevo, probarlo con una aceptación caducada y otra válida y mostrar la salida. *Evidencia esperada:* cambio de código y salida. *Rúbrica:* 3 = campo añadido en todas las filas, regla correcta, dos casos de prueba que demuestran ambos resultados, y «Needs governance action» incluye la caducada; 2 = funciona sin pruebas; 1 = solo la regla; 0 = nada.

**EX020 — Presente ante la comisión.** *Objetivo:* comunicar el registro. *Insumos:* la salida del Lab 4. *Pasos:* escribir el resumen de una página para la comisión de auditoría y riesgos. *Evidencia esperada:* el resumen. *Rúbrica:* 3 = principales riesgos clasificados por consecuencia en lenguaje llano, con dueños y fechas; acciones de gobernanza con las decisiones solicitadas; declaración explícita de la regla de clasificación y sus límites; ninguna «puntuación» única; 2 = enumera riesgos sin peticiones; 1 = pega la tabla; 0 = nada.

### Síntesis del capítulo

La evaluación de riesgos es un ciclo (enmarcar, identificar, analizar, decidir, supervisar) y el registro es su memoria. Ancle las escalas en los términos de su servicio, clasifique primero por consecuencia en los servicios esenciales y trate las puntuaciones como ordinales. Todo riesgo necesita un dueño con autoridad, un tratamiento, fechas y evidencia; la aceptación solo es legítima con la autoridad, las condiciones y la caducidad que le corresponden.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Siga estudiando — capítulo 04 de 12

[← Capítulo 03](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Infraestructura crítica y seguridad sectorial: herramientas e interpretación

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- elegir entre los principales marcos y líneas base públicos para un servicio esencial y explicar para qué sirve cada uno;
- leer con espíritu crítico una autoevaluación o una puntuación de madurez: qué mide, quién la produjo y qué no puede mostrar;
- diseñar un pequeño conjunto de métricas del programa que impulsen decisiones en lugar de decorar informes;
- interpretar los hallazgos técnicos que le entreguen ingenieros y proveedores lo bastante bien como para hacer las preguntas de seguimiento adecuadas.

Las «herramientas» del coordinador son sobre todo documentos y medidas. El capítulo 4 construyó el registro; este capítulo aporta las varas de medir externas y las cifras que informan sobre él.

### 5.1 El panorama de los marcos

Se encontrará con varias referencias que se solapan. Cada una tiene una finalidad distinta:

| Referencia | Para qué sirve | Uso típico por un coordinador |
|---|---|---|
| [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) | Taxonomía de resultados (Gobernar, Identificar, Proteger, Detectar, Responder, Recuperar) | Estructurar el programa y los perfiles; hablar con la dirección |
| [CISA Cross-Sector Cybersecurity Performance Goals (CPGs)](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals) | Un subconjunto priorizado de prácticas de alto impacto para las infraestructuras críticas | Línea base rápida; encontrar primero las lagunas evidentes |
| [NCSC Cyber Assessment Framework (CAF)](https://www.ncsc.gov.uk/collection/caf) | Evaluación basada en resultados para operadores de servicios esenciales, con indicadores de buenas prácticas | Autoevaluación estructurada, diálogo con el regulador (contexto británico) |
| [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | Normas para la seguridad de los sistemas de automatización y control industrial, que abarcan a propietarios de activos, integradores y proveedores de productos | Requisitos de compras y de proveedores; expectativas del programa para la TO |
| [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | Orientaciones para proteger la TO | Vocabulario compartido con los ingenieros |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Catálogo de controles de seguridad y privacidad | Lenguaje detallado de controles cuando hace falta |

La regla del coordinador: **una estructura principal** (por ejemplo, el CSF 2.0) para el programa, con las demás referencias asociadas a ella, en lugar de cuatro hojas de cálculo paralelas. Los requisitos regulatorios de su jurisdicción van primero; los marcos le ayudan a cumplirlos, no los sustituyen.

### 5.2 Leer una evaluación

Un resultado de evaluación como «Proteger: 2,4 / 4» o «cobertura de los CPG del 71%» invita a una falsa confianza. Antes de repetirlo, haga cinco preguntas:

1. **¿Qué se evaluó?** ¿Qué instalaciones, sistemas y procesos, y cuáles no?
2. **¿Quién evaluó y cómo?** ¿Autoevaluación del dueño del sistema, de un par, de un evaluador independiente? ¿Mediante entrevista, revisión documental o prueba?
3. **¿Qué cuenta como «cumplido»?** ¿Una política escrita, una política en uso o una política que se ha demostrado que funciona?
4. **¿Cuándo?** Las evaluaciones envejecen rápido tras reorganizaciones, cambios de proveedor e incidentes.
5. **¿Qué decisión respalda?** Si ninguna decisión cambia en función del número, es decoración.

Una autoevaluación es valiosa (es barata y genera comprensión), pero mide lo que creen los dueños. El capítulo 7 añade formas de obtener evidencia más sólida.

### 5.3 Métricas que impulsan decisiones

Las buenas métricas del programa comparten tres propiedades: se relacionan con una consecuencia o con un control que protege frente a ella; su responsable puede modificarlas; y un umbral desencadena una acción conocida. Compare:

| Métrica débil | Métrica mejor | Acción al superar el umbral |
|---|---|---|
| Número de políticas de seguridad | % de riesgos de nivel 5 con dueño y tratamiento en plazo | Por debajo del 100% → escalado a la dirección |
| Correos de phishing bloqueados | Mediana del tiempo entre el fin del contrato de un proveedor y la eliminación de su cuenta | Más de 5 días laborables → revisión del proceso de acceso |
| Vulnerabilidades encontradas | % de interfaces operativas expuestas a internet (debería ser cero) | Cualquiera → notificación inmediata al dueño |
| Formación completada | % de responsables de guardia que participaron en un ejercicio en los últimos 12 meses | Por debajo del 80% → programar un ejercicio |

Los recuentos de actividad («bloqueamos 40.000 ataques») son fáciles de producir y rara vez útiles para decidir. Prefiera medidas de exposición, puntualidad y cobertura de lo que más importa.

### 5.4 Interpretar hallazgos técnicos

Los ingenieros, el KVROC y los proveedores envían hallazgos. No necesita verificarlos técnicamente, pero debe hacer preguntas que los dejen listos para decidir:

- **¿Qué está afectado?** ¿Qué instalación, qué función, qué nivel de consecuencia?
- **¿Cómo lo sabe?** ¿Observado directamente, inferido o comunicado por una herramienta que puede equivocarse?
- **¿Cuál es la exposición?** ¿Accesible desde internet, desde la red de oficina, solo in situ?
- **¿Cuál es la acción recomendada, quién la ejecuta, para cuándo y qué perturba?**
- **¿Hay un aviso público?** Si lo hay, enlácelo; avisos como la alerta de la CISA para el sector del agua sobre controladores expuestos a internet con contraseñas predeterminadas ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)) ayudan a la dirección a entender que un hallazgo no es hipotético.

### 5.5 Ejemplo resuelto: una autoevaluación con los CPG (sintético)

L. Ferreira completó una lista de comprobación de los CPG para Kestrel Water e informa de «71% de objetivos cumplidos». La coordinadora hace las cinco preguntas y descubre que la evaluación abarcó la red corporativa y la planta de tratamiento, pero **no** las doce estaciones; que las respuestas eran «sí» si existía una política; y que se hizo antes de que cambiara el acuerdo de acceso remoto de HydroLogic. Dos elementos «cumplidos» (la autenticación multifactor para el acceso remoto y la revocación de credenciales del personal que se marcha) no tienen evidencia para las cuentas de proveedores.

Informa a la dirección: «*Una autoevaluación de la TI corporativa y de la planta de tratamiento encontró la mayoría de las prácticas de base implantadas sobre el papel. No abarcó las estaciones, y dos elementos que son los que más importan para ellas (la autenticación multifactor para el acceso remoto y la eliminación a tiempo de las cuentas) no están verificados para los proveedores. Propongo una revisión del acceso de proveedores en mayo (capítulo 8) y repetir la evaluación, incluidas las estaciones, antes de septiembre.*». El 71% se queda en un anexo.

### 5.6 Actividad práctica

Tome cualquier panel público o afirmación de un informe anual sobre ciberseguridad (por ejemplo, «100% del personal formado»). Aplique las cinco preguntas y reescríbala como una afirmación lista para decidir, anotando lo que necesitaría saber. Escriba su reescritura con la misma forma que el informe de la coordinadora sobre la autoevaluación con los CPG: qué se abarcó, cómo se juzgó, qué quedó fuera y qué decisión se deriva. Si la afirmación no respalda ninguna decisión, dígalo; eso ya es un hallazgo. Conserve la cifra original, pero colóquela después del contexto y no al principio. Anote la fecha de la afirmación y si algo ha cambiado desde entonces, como una reorganización o un proveedor nuevo.

### 5.7 Errores comunes y límites

- Aplicar varios marcos en paralelo sin asociarlos entre sí.
- Elegir métricas porque los datos son fáciles de obtener.
- Tratar el marketing de un proveedor («conforme a la 62443») como una evaluación de su instalación.
- Olvidar que los marcos y las líneas base se revisan; cite la versión y la fecha.

- Dar un objetivo por cumplido porque existe una política, como hizo la autoevaluación con los CPG, sin preguntar si está en uso o si se ha demostrado que funciona.
- Dejar fuera parte del servicio, como las doce estaciones, y aun así comunicar una sola cifra para toda la empresa, o comunicar porcentajes sin alcance ni método.
- Repetir un resultado de evaluación ante la dirección antes de preguntar cuándo se hizo y qué ha cambiado desde entonces.

### Ejercicios — capítulo 5

**EX021 — Elija una estructura principal.** *Objetivo:* seleccionar y asociar marcos. *Insumos:* Kestrel Water debe informar a su regulador, compra sistemas de TO a proveedores y tiene un consejo poco familiarizado con la seguridad. *Pasos:* proponer una estructura principal y cómo se relacionan con ella los CPG y la 62443. *Evidencia esperada:* una justificación breve. *Rúbrica:* 3 = primero los requisitos regulatorios, el CSF 2.0 como estructura del programa para el consejo, los CPG como línea base priorizada asociada a él, la 62443 usada para los requisitos de proveedores y de compras; 2 = elección sin asociación; 1 = «hacerlo todo»; 0 = nada.

**EX022 — Interrogue una puntuación.** *Objetivo:* aplicar las cinco preguntas. *Insumos:* «Madurez de Detectar 3,1/5, frente a 2,6». *Pasos:* escribir las cinco preguntas aplicadas a esta puntuación e indicar qué respuesta haría creíble la mejora. *Evidencia esperada:* preguntas y criterios. *Rúbrica:* 3 = pregunta por el alcance, el evaluador y el método, la definición de los niveles, la fecha y la decisión que respalda; creíble si el alcance y el método son los mismos, si es independiente o se basa en evidencia, y si se vincula a un resultado observado (por ejemplo, la detección de una inyección de un ejercicio); 2 = solo preguntas; 1 = la acepta; 0 = nada.

**EX023 — Arregle las métricas.** *Objetivo:* diseñar métricas que impulsen decisiones. *Insumos:* el informe mensual actual: correos bloqueados, detecciones del antivirus, políticas aprobadas, personal formado. *Pasos:* sustituirlas por cuatro métricas con responsable y acción al superar el umbral. *Evidencia esperada:* tabla. *Rúbrica:* 3 = métricas ligadas a la consecuencia y al control (por ejemplo, higiene de los riesgos de nivel 5, tiempo de eliminación de cuentas de proveedores, exposición de interfaces operativas, participación en ejercicios), cada una con responsable y acción; 2 = métricas sin acciones; 1 = cambios cosméticos; 0 = nada.

**EX024 — Deje un hallazgo listo para decidir.** *Objetivo:* interrogar un hallazgo técnico. *Insumos:* correo del KVROC: «Vimos RDP desde internet hacia hmi-02 anoche, recomendamos bloquearlo». *Pasos:* redactar la respuesta. *Evidencia esperada:* la respuesta. *Rúbrica:* 3 = pregunta a qué instalación y función sirve hmi-02, si la conexión tuvo éxito, el origen y la evidencia, y si sigue expuesto; pregunta quién puede bloquearlo y qué perturba el bloqueo (¿el acceso de un proveedor?); implica al dueño de operaciones; lo trata como potencialmente urgente; 2 = pregunta algunas cosas; 1 = «bloquéenlo, por favor»; 0 = nada.

**EX025 — Informe con honestidad.** *Objetivo:* comunicar los límites de una evaluación. *Insumos:* el ejemplo resuelto 5.5. *Pasos:* reescribir el mensaje a la dirección para el consejo en menos de 100 palabras. *Evidencia esperada:* el mensaje. *Rúbrica:* 3 = expone con claridad la laguna de cobertura y los elementos no verificados, da el plan y la fecha, y evita el porcentaje como titular; 2 = menciona primero el porcentaje pero incluye los límites; 1 = «71% de cumplimiento»; 0 = nada.

### Síntesis del capítulo

Los marcos y las líneas base son varas de medir: elija una estructura principal, cumpla primero la ley y asocie el resto. Lea toda evaluación por su alcance, su método, su definición, su fecha y la decisión que respalda. Mida la exposición, la puntualidad y la cobertura de lo que importa, con responsables y acciones de umbral. Deje los hallazgos técnicos listos para decidir preguntando qué está afectado, cómo se sabe, cuál es la exposición, quién actúa y qué perturba.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Siga estudiando — capítulo 05 de 12

[← Capítulo 04](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Infraestructura crítica y seguridad sectorial: flujo de trabajo operativo

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- definir las funciones que necesita un programa de seguridad de infraestructuras críticas y cómo se relacionan con las operaciones;
- construir y comprobar una matriz RACI para que cada actividad clave tenga exactamente una persona que rinde cuentas y un responsable principal claro;
- gobernar los cambios en TI y TO sin bloquear las operaciones ni saltarse la seguridad de las personas;
- diseñar una vía de escalado, desde un operador de turno hasta la dirección, que funcione a las 03:00 de un domingo.

El capítulo 5 le dio las varas de medir. Este capítulo hace que el programa funcione en el día a día.

### 6.1 Funciones

Con el tamaño de Kestrel Water, las funciones siguientes pueden repartirse entre un puñado de personas. Lo que importa es que cada una esté asignada:

- **Patrocinador ejecutivo** (director de operaciones): es dueño del programa, acepta los riesgos altos y resuelve los conflictos entre departamentos.
- **Dueños de servicio** (el jefe de operaciones para el tratamiento y las estaciones; el responsable de atención al cliente para la facturación): son dueños de los riesgos y las decisiones de sus servicios.
- **Coordinador**: conduce el ciclo: registro, registros de decisión, ejercicios, informes, revisiones de proveedores.
- **Responsable de seguridad**: asesoramiento técnico de seguridad y enlace de supervisión con el KVROC.
- **Ingeniero de sistemas de control**: configuración y cambios en los sistemas operativos de la planta.
- **Responsable de comunicación**: mensajes públicos y a los medios.
- **Responsable del incidente** (rotatorio, de guardia): dirige la respuesta cuando se declara un incidente.
- **Proveedores**: trabajan con autorización; nunca son dueños de decisiones sobre su servicio.

La orientación del NIST sobre respuesta a incidentes insiste en definir las funciones y responsabilidades, incluidas las de fuera del equipo de seguridad, antes de que ocurran los incidentes ([NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)).

### 6.2 RACI

Una matriz **RACI** enumera actividades frente a personas, con una letra para cada una: **R** (*Responsible*, ejecuta el trabajo), **A** (*Accountable*, responde del resultado y lo da por bueno; exactamente una por actividad), **C** (*Consulted*, aportación en ambos sentidos antes de la decisión), **I** (*Informed*, se le informa después). Dos reglas detectan la mayoría de los defectos:

1. Exactamente una **A** por actividad. Cero significa que nadie responde; dos significa que cada uno da por hecho que lo hará el otro.
2. Al menos una **R** y, cuando hay varias, un responsable principal con nombre.

Añada dos comprobaciones de coordinador: nadie debe rendir cuentas de la aprobación de su propio acceso o trabajo; y nadie debe acumular tantas entradas R y A en un incidente que se convierta en un cuello de botella.

### 6.3 Gobernanza de cambios en TI y TO

Los cambios en los sistemas operativos de la planta pueden afectar al proceso físico. Un proceso de cambios practicable para una empresa de servicios pequeña tiene tres clases:

- **Estándar**: preaprobado, de bajo riesgo y repetible (sustituir un teclado de operador averiado): se registra.
- **Normal**: evaluado y aprobado por el dueño del servicio, con un plan de prueba o de reversión y una ventana acordada con operaciones.
- **De emergencia**: necesario ahora para proteger a las personas o el servicio; aprobado verbalmente por el responsable del incidente o el dueño del servicio, registrado en las 24 horas siguientes y revisado después.

Al coordinador le interesa que los cambios relevantes para la seguridad (nuevos accesos remotos, cambios de reglas del cortafuegos, nuevos proveedores, software en los ordenadores de la sala de control) no puedan colarse como «estándar», y que los cambios de emergencia hechos durante los incidentes se revisen en lugar de volverse permanentes.

### 6.4 Escalado

Una vía de escalado responde, para cada nivel de gravedad: a quién se llama, quién llama, cómo, en cuánto tiempo y qué ocurre si no contesta. Escríbala como una tabla con suplentes, pruébela (capítulo 11) y colóquela donde los operadores del turno de noche puedan encontrarla sin un ordenador (una tarjeta impresa en la sala de control), porque el incidente podría haberse llevado los ordenadores. La tarjeta de Kestrel Water enumera al responsable del incidente, al jefe de operaciones y a la responsable de seguridad, con un suplente con nombre para cada uno, además de números de móvil que no dependen de la red corporativa.

### 6.5 Ejemplo resuelto: comprobar la RACI de incidentes (sintético)

La coordinadora redacta la RACI de incidentes de Kestrel Water y ejecuta el **Lab 6**, que aplica las reglas de 6.2. **Lab 6** (guárdelo como `lab06.py` y ejecútelo con `python3 lab06.py`):

```python
# Lab 6 - RACI matrix check for incident coordination (offline, standard library only; synthetic)
PEOPLE = ["Coordinator", "Ops manager", "Security lead", "Comms", "Vendor", "CEO"]
# activity -> one letter per person (R responsible, A accountable, C consulted, I informed, - none)
RACI = {
    "Declare cyber incident":            "R A C I - I",
    "Decide to isolate stations":        "C A R I C I",
    "Switch stations to manual operation":"I A - - - I",
    "Notify regulator":                  "R - C C - A",
    "Brief hospital (critical customer)":"R C I R - A",
    "Approve vendor remote session":     "C A A - R -",
    "Public statement":                  "C C C R - -",
}
issues = []
load = {p: 0 for p in PEOPLE}
for act, codes in RACI.items():
    c = codes.split()
    assert len(c) == len(PEOPLE), act
    a = [p for p, x in zip(PEOPLE, c) if x == "A"]
    r = [p for p, x in zip(PEOPLE, c) if x == "R"]
    for p, x in zip(PEOPLE, c):
        if x in "RA": load[p] += 1
    if len(a) != 1: issues.append(f"{act}: {len(a)} accountable ({', '.join(a) or 'none'})")
    if not r: issues.append(f"{act}: nobody responsible")
    if len(r) > 1: issues.append(f"{act}: {len(r)} responsible ({', '.join(r)}) - name a lead")
    if act.startswith("Approve") and c[PEOPLE.index("Vendor")] in "RA":
        issues.append(f"{act}: vendor is responsible for approving its own access")
for i in issues: print("ISSUE", i)
print("R/A load:", ", ".join(f"{p}={n}" for p, n in load.items()))
print(f"{len(issues)} issues in {len(RACI)} activities")
```

Salida esperada (Python 3.13.5):

```text
ISSUE Switch stations to manual operation: nobody responsible
ISSUE Brief hospital (critical customer): 2 responsible (Coordinator, Comms) - name a lead
ISSUE Approve vendor remote session: 2 accountable (Ops manager, Security lead)
ISSUE Approve vendor remote session: vendor is responsible for approving its own access
ISSUE Public statement: 0 accountable (none)
R/A load: Coordinator=3, Ops manager=4, Security lead=2, Comms=2, Vendor=1, CEO=2
5 issues in 7 activities
```

Cinco defectos en siete actividades:

- **Pasar las estaciones a operación manual** tiene una persona que rinde cuentas (el jefe de operaciones), pero nadie que lo ejecute: en la práctica lo hacen los operadores de turno y los técnicos de guardia, que faltan en la matriz. La corrección es añadir al supervisor de turno como R.
- **Informar al hospital** tiene dos R. La coordinadora y comunicación podrían pensar cada una que llamó la otra. Nombre a la coordinadora como responsable principal (es un enlace operativo), con comunicación consultada sobre la redacción.
- **Aprobar la sesión remota del proveedor** tiene dos A y señala al proveedor como R. El jefe de operaciones debería ser la única A (es dueño de las estaciones); la responsable de seguridad es C; el proveedor *solicita* el acceso y es I respecto de la decisión: una parte nunca debe aprobar su propio acceso.
- **Declaración pública** no tiene a nadie que rinda cuentas. El consejero delegado debería ser A, y comunicación, R.

La línea de carga muestra que el jefe de operaciones acumula cuatro entradas R/A: durante un incidente, esa misma persona está dirigiendo la planta. La coordinadora propone un suplente para las entradas relacionadas con el incidente. El laboratorio solo comprueba la estructura; si se eligió a las personas adecuadas es un juicio que corresponde al patrocinador ejecutivo.

### 6.6 Actividad práctica

Escriba una RACI para «incorporar un nuevo proveedor con acceso remoto» usando al menos cinco funciones y después compruébela frente a las cuatro reglas a mano o editando el Lab 6. Incluya al proveedor como función y asegúrese de que nunca apruebe su propio acceso, algo que el Lab 6 comprueba explícitamente. Indique quién rinde cuentas de la creación de la cuenta, quién comprueba que el contrato tenga las cláusulas de seguridad y a quién se informa cuando se activa la cuenta. Después cuente las entradas R y A de cada persona: si un nombre aparece en casi todas las líneas, la incorporación se atascará siempre que esa persona esté de vacaciones. Muestre el resultado al jefe de operaciones y pregúntele si falta alguien.

### 6.7 Errores comunes y límites

- Comités como responsables que rinden cuentas («el comité de seguridad»).
- RACI escritas solo para los días normales, no para los incidentes.
- Cambios de emergencia que nunca se revisan.
- Listas de escalado sin suplentes, o guardadas solo en la red.
- Una RACI es un contrato social: publíquela, repásela con cada persona y actualícela tras las reorganizaciones.

- Dejar fuera de la matriz a las personas que realmente hacen el trabajo, como descubrió el Lab 6 con los operadores de turno para la operación manual.
- Permitir que una parte apruebe su propio acceso, como un proveedor marcado como responsable de aprobar su sesión remota.
- Dar a una persona tantas entradas R y A que el incidente dependa solo de ella.

### Ejercicios — capítulo 6

**EX026 — Corrija la RACI.** *Objetivo:* corregir los defectos. *Insumos:* la matriz del Lab 6. *Pasos:* proponer filas corregidas para los cinco problemas y volver a ejecutar la comprobación (a mano o con código). *Evidencia esperada:* matriz corregida y resultado limpio. *Rúbrica:* 3 = cero problemas, el proveedor nunca es A ni R de la aprobación, se añade una función de turno para la operación manual, un único responsable principal para informar al hospital, el consejero delegado rinde cuentas de la declaración pública; 2 = queda un problema; 1 = parcial; 0 = nada.

**EX027 — Clasifique los cambios.** *Objetivo:* aplicar las clases de cambio. *Insumos:* (a) una nueva regla del cortafuegos que permite la VPN de un proveedor; (b) sustituir una batería averiada del SAI en un armario de estación; (c) desactivar una cuenta comprometida durante un incidente; (d) instalar un agente de supervisión en el historiador. *Pasos:* clasificarlos y justificarlo. *Evidencia esperada:* cuatro clases. *Rúbrica:* 3 = (a) normal (relevante para la seguridad), (b) estándar si existe un procedimiento preaprobado, (c) de emergencia con revisión posterior, (d) normal con comprobación de compatibilidad del proveedor; 2 = tres correctas; 1 = todas estándar; 0 = nada.

**EX028 — Tarjeta de escalado.** *Objetivo:* diseñar una vía de escalado utilizable. *Insumos:* las funciones de 6.1. *Pasos:* escribir la tarjeta impresa para los operadores del turno de noche ante una sospecha de evento cibernético. *Evidencia esperada:* contenido de la tarjeta. *Rúbrica:* 3 = desencadenantes observables, primera llamada y suplente con números de teléfono como marcadores de posición, límites de tiempo, qué hacer mientras tanto (primero la seguridad, no apagar ordenadores sin instrucciones, anotar las horas), cuándo llamar directamente al responsable del incidente; 2 = sin suplentes; 1 = «llamar a TI»; 0 = nada.

**EX029 — Análisis de cuellos de botella.** *Objetivo:* usar la línea de carga. *Insumos:* la salida de carga del Lab 6. *Pasos:* proponer cómo reducir la carga del jefe de operaciones durante un incidente sin debilitar la autoridad sobre la seguridad de las personas. *Evidencia esperada:* propuesta. *Rúbrica:* 3 = mantiene las decisiones de seguridad de las personas en operaciones, pero delega el enlace y la aprobación del proveedor en un suplente con nombre o en el responsable del incidente, con el jefe de operaciones consultado; 2 = delegación sin salvedad de seguridad; 1 = traspasa las decisiones de seguridad de las personas a TI; 0 = nada.

**EX030 — Revisión de un cambio de emergencia.** *Objetivo:* cerrar los cambios de emergencia. *Insumos:* durante un incidente, un ingeniero añadió una regla del cortafuegos que bloquea todo acceso de proveedores y creó una cuenta temporal de administrador local. *Pasos:* describir la revisión posterior al incidente. *Evidencia esperada:* pasos de la revisión. *Rúbrica:* 3 = enumerar los cambios de emergencia a partir del registro, decidir para cada uno mantener/modificar/revertir con un responsable, eliminar la cuenta temporal, restablecer el acceso de proveedores solo mediante el proceso normal, actualizar la documentación; 2 = algunos pasos; 1 = «dejarlo así»; 0 = nada.

### Síntesis del capítulo

Un programa funciona con funciones asignadas, una RACI con una sola persona que rinde cuentas por actividad y un responsable principal con nombre, una gobernanza de cambios que mantiene visibles los cambios relevantes para la seguridad y una vía de escalado que funciona sin conexión de noche. Compruebe en la RACI la estructura, la titularidad de las aprobaciones y la carga durante los incidentes; revise todo cambio de emergencia después del evento.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Siga estudiando — capítulo 06 de 12

[← Capítulo 05](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Infraestructura crítica y seguridad sectorial: controles y verificación

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- describir un control en términos que un responsable pueda asumir: objetivo, dueño, funcionamiento y evidencia;
- distinguir los niveles de aseguramiento (declarado, documentado, observado, probado) y decidir qué nivel necesita cada control;
- planificar un programa de verificación proporcionado para los controles que protegen frente a consecuencias de nivel 5;
- gestionar las excepciones a los controles como decisiones de riesgo limitadas en el tiempo y con dueño.

El capítulo 6 puso en marcha el programa. Este capítulo pregunta si sus protecciones funcionan de verdad.

### 7.1 Qué es un control, para un responsable

Un **control** es una medida que modifica el riesgo ([NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) cataloga miles de ellos). A efectos de coordinación, describa cada control importante en una ficha:

- **Objetivo**: qué riesgo aborda y cómo («impide usar una contraseña robada de un proveedor para iniciar sesión en las estaciones»);
- **Dueño**: quién responde de que funcione;
- **Funcionamiento**: qué ocurre, con qué frecuencia y quién lo hace («la pasarela de acceso remoto exige un segundo factor para todas las cuentas de proveedores»);
- **Evidencia**: qué mostraría que funciona y dónde se guarda;
- **Señal de fallo**: qué vería si dejara de funcionar.

Los controles sin dueño se deterioran igual que los riesgos sin dueño.

### 7.2 Niveles de aseguramiento

¿Hasta qué punto está seguro de que un control funciona? Cuatro niveles útiles:

| Nivel | Significado | Evidencia de ejemplo |
|---|---|---|
| Declarado | Alguien dice que existe | «Sí, los proveedores usan MFA», en una reunión |
| Documentado | Una política o un diseño lo describe | Norma de acceso remoto v2 |
| Observado | Los registros muestran que funciona | Exportación de la configuración de la pasarela; registros de inicio de sesión que muestran eventos de segundo factor |
| Probado | Una prueba deliberada mostró que detiene lo que debe | Un intento supervisado de iniciar sesión solo con contraseña es rechazado, y queda registrado en un informe de prueba |

Los niveles más altos cuestan más. Un programa proporcionado aspira al nivel **probado** en los controles que protegen frente a consecuencias de nivel 5, al **observado** para los niveles 3–4, y acepta el **documentado** para el resto. Las orientaciones del NIST sobre supervisión continua describen cómo mantener un conocimiento permanente de si los controles siguen siendo eficaces ([NIST SP 800-137](https://csrc.nist.gov/pubs/sp/800/137/final)).

### 7.3 Quién verifica

- **Primera línea**: los dueños de los controles comprueban sus propios controles (autoevaluación, comprobaciones rutinarias).
- **Segunda línea**: la coordinadora o la función de seguridad revisan la evidencia y toman muestras.
- **Tercera línea**: la auditoría interna o un evaluador independiente dan garantías al consejo.

El coordinador suele diseñar el plan de verificación y realizar las comprobaciones de segunda línea. Las pruebas en sistemas operativos de la planta deben autorizarse como cualquier otro trabajo (capítulo 3), y en los entornos de control una «prueba» suele ser una revisión de la configuración y de los registros más que un intento activo.

Las comprobaciones de segunda línea deben tomar muestras de la evidencia directamente en lugar de aceptar el resumen del dueño.

### 7.4 Excepciones

A veces no se puede aplicar un control: un controlador antiguo de una estación no admite un segundo factor; un dispositivo médico no puede parchearse sin perder su certificación. Una **excepción** es una decisión registrada y con dueño de operar sin el control, que es una forma de aceptación del riesgo (capítulo 4). Necesita: el control y el sistema afectados; el motivo; las medidas compensatorias; la autoridad que la acepta; una fecha de caducidad; y un plan para eliminar la excepción. El registro de excepciones se revisa junto con el registro de riesgos.

En Kestrel Water, la excepción del controlador de KW-10 llegó al consejo con caducidad en marzo.

### 7.5 Ejemplo resuelto: verificar tres controles (sintético)

La coordinadora elige tres controles que protegen frente a riesgos de nivel 5 y comprueba cada uno:

| Control | Declarado / documentado | Observado | Probado | Hallazgo |
|---|---|---|---|---|
| C1: MFA para todo acceso remoto de proveedores | Sí: norma de acceso remoto v2 | La exportación de la pasarela muestra MFA en 5 de 6 cuentas de proveedores | Aún no | La cuenta de ScadaCo no tiene MFA (confirmado después en el Lab 8). **Laguna.** |
| C2: copias de seguridad del historiador restaurables en 24 h | Sí: procedimiento de copias de seguridad | Los trabajos de copia terminan bien cada noche | Última prueba de restauración: nunca | **Sin verificar**: una copia correcta ≠ una restauración correcta (vinculado al riesgo R04). |
| C3: límites de dosificación aplicados en la lógica del controlador | Sí: documento de diseño | Límites visibles en la revisión de la configuración hecha por J. Tan | Prueba en banco supervisada por el proveedor en un controlador de repuesto, registrada el 3 de febrero | **Verificado** al nivel de prueba para el repuesto; la configuración de producción coincide por suma de comprobación. |

El plan de verificación que se deriva: corregir C1 en 30 días (dueño, A. Mensah); programar una prueba de restauración de C2 en 60 días con un resultado cronometrado (dueño, J. Tan); repetir la comprobación de C3 tras cualquier cambio de lógica. La coordinadora comunica el nivel de aseguramiento de cada control, no una única afirmación de «controles eficaces».

### 7.6 Actividad práctica

Escriba fichas de control (objetivo, dueño, funcionamiento, evidencia, señal de fallo) para dos controles de una organización que conozca y asigne a cada uno un nivel de aseguramiento actual, con su justificación. En cada ficha, diga cómo sería en la práctica la señal de fallo, por ejemplo un inicio de sesión de un proveedor sin evento de segundo factor en el registro de la pasarela. Explique por qué eligió el nivel de aseguramiento, citando la evidencia que vio realmente. Después decida qué nivel debería alcanzar el control, dada la consecuencia frente a la que protege, y qué paso concreto lo elevaría, por ejemplo una prueba de restauración para una copia de seguridad que solo se ha observado terminar bien. Mantenga las fichas lo bastante breves para que un dueño las actualice.

### 7.7 Errores comunes y límites

- Equiparar «el trabajo terminó bien» con «el control funciona» (copias de seguridad, parches).
- Verificar los controles críticos solo al nivel declarado o documentado.
- Hacer pruebas activas en sistemas operativos de la planta sin autorización ni acuerdo de operaciones.
- Excepciones sin caducidad, que se convierten silenciosamente en el diseño.
- Informar de controles como «eficaces» sin decir cómo se estableció.

- Tratar la propia afirmación de un proveedor de que la MFA está activada como evidencia observada, cuando solo la exportación de la pasarela lo muestra.
- Verificar un control una vez y nunca más, de modo que un cambio de configuración posterior lo elimina silenciosamente.
- Probar un sistema de repuesto o de banco y olvidar confirmar que producción coincide, como hizo C3 mediante la suma de comprobación.

### Ejercicios — capítulo 7

**EX031 — Escriba una ficha de control.** *Objetivo:* hacer que un control pueda asumirse. *Insumos:* «Las cuentas de proveedores se eliminan cuando terminan los contratos». *Pasos:* escribir la ficha de cinco partes. *Evidencia esperada:* la ficha. *Rúbrica:* 3 = objetivo ligado a un riesgo, dueño con autoridad (jefe de operaciones o dueño del contrato), funcionamiento con desencadenante y plazo, evidencia (conciliación mensual de las cuentas con los contratos), señal de fallo (existen cuentas de contratos terminados); 2 = falta la señal de fallo; 1 = repite la frase; 0 = nada.

**EX032 — Asigne objetivos de aseguramiento.** *Objetivo:* aplicar la proporcionalidad. *Insumos:* controles: MFA para el acceso de proveedores; política de contraseñas para los portátiles de oficina; procedimiento de operación manual de las estaciones; tarjetas de visitante en la sede central. *Pasos:* asignar niveles de aseguramiento objetivo y justificarlos por la consecuencia. *Evidencia esperada:* cuatro objetivos. *Rúbrica:* 3 = probado para la MFA de proveedores y la operación manual (mediante ejercicio o simulacro), documentado u observado para los demás, con razonamiento; 2 = objetivos sin razones; 1 = todo probado; 0 = nada.

**EX033 — Diseñe una prueba de restauración.** *Objetivo:* verificar C2. *Insumos:* el ejemplo resuelto. *Pasos:* esbozar la prueba, los criterios de éxito y la autorización. *Evidencia esperada:* esbozo. *Rúbrica:* 3 = restauración en un entorno aislado, no en producción; cronometrada frente al objetivo de 24 h; comprueba la integridad de los datos de un periodo elegido; autorizada por el dueño del servicio; resultado registrado con fecha y evidencia; 2 = sin criterios de éxito; 1 = «comprobar los registros de las copias»; 0 = nada.

**EX034 — Redacte una excepción.** *Objetivo:* gestionar una laguna de control. *Insumos:* el controlador de KW-10 no admite MFA para el acceso local de ingeniería. *Pasos:* redactar la excepción. *Evidencia esperada:* registro de la excepción. *Rúbrica:* 3 = control y sistema, motivo, medidas compensatorias (ninguna ruta remota, control de acceso físico, supervisión de cambios), autoridad que acepta acorde con la consecuencia, caducidad, plan de eliminación; 2 = sin caducidad; 1 = «no es posible»; 0 = nada.

**EX035 — Informe del aseguramiento.** *Objetivo:* comunicar la verificación con honestidad. *Insumos:* la tabla del ejemplo resuelto. *Pasos:* escribir tres líneas para la dirección, una por control. *Evidencia esperada:* tres líneas. *Rúbrica:* 3 = cada una indica el nivel de aseguramiento alcanzado, la laguna o el resultado, el dueño y la fecha; evita «eficaz» sin evidencia; 2 = faltan fechas; 1 = «controles eficaces»; 0 = nada.

### Síntesis del capítulo

Un control es algo que un responsable puede asumir: objetivo, dueño, funcionamiento, evidencia y señal de fallo. El aseguramiento sube de declarado a documentado, observado y probado; aspire al nivel probado en los controles que protegen frente a las peores consecuencias. Verifique de forma proporcionada a través de tres líneas, autorice las pruebas como cualquier otro trabajo y mantenga las excepciones con dueño, compensadas y limitadas en el tiempo.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Siga estudiando — capítulo 07 de 12

[← Capítulo 06](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Infraestructura crítica y seguridad sectorial: análisis supervisado de un caso

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- analizar un problema de acceso de proveedores como un caso de gobernanza: contratos, cuentas, personas y evidencia;
- realizar una revisión periódica del acceso remoto de terceros y actuar de forma proporcionada sobre sus hallazgos;
- incorporar requisitos de seguridad para los proveedores en los contratos y en la incorporación;
- presentar el análisis de un caso a un supervisor con las decisiones solicitadas, la evidencia adjunta y la incertidumbre etiquetada.

Este es el primer caso supervisado del libro. Reúne el riesgo (capítulo 4), las funciones (capítulo 6) y la verificación de controles (capítulo 7).

### 8.1 Por qué los proveedores importan tanto aquí

Los servicios esenciales dependen de los proveedores para los equipos, el software, el mantenimiento y la supervisión. El acceso remoto de los proveedores es cómodo (un experto en bombas puede resolver un problema de noche a 200 kilómetros de distancia) y es también una vía de compromiso recurrente. Las orientaciones de la CISA sobre mitigaciones principales para la TO incluyen entre sus prioridades reducir la exposición y proteger el acceso remoto ([CISA, Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology)). Las orientaciones del NIST sobre la cadena de suministro tratan a los proveedores como parte del riesgo de la organización y recomiendan integrar la gestión del riesgo de la cadena de suministro en la gobernanza y en las adquisiciones ([NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final)). La NIS2 incluye la seguridad de la cadena de suministro entre las medidas de gestión de riesgos que deben adoptar las entidades ([Directive (EU) 2022/2555, Article 21](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)).

### 8.2 El ciclo de vida del proveedor

La gobernanza de un proveedor con acceso sigue un ciclo de vida:

1. **Seleccionar**: preguntas de seguridad en la compra, proporcionadas al acceso solicitado.
2. **Contratar**: obligaciones de seguridad: personas con nombre, MFA, notificación de incidentes y de salidas de personal, derecho de revisión, tratamiento de los datos, apoyo a su respuesta a incidentes.
3. **Incorporar**: cuentas creadas por persona nombrada, acceso mínimo, proceso de aprobación de las sesiones (capítulo 6).
4. **Operar**: sesiones aprobadas, registradas y revisadas; revisiones periódicas del acceso.
5. **Cambiar**: personal nuevo, sistemas nuevos, fusiones: nueva revisión.
6. **Salir**: cuentas eliminadas, datos devueltos o destruidos, confirmación registrada.

La mayoría de los problemas reales están en las juntas: un contrato que terminó pero cuya cuenta sobrevivió; un ingeniero que dejó al proveedor pero cuya contraseña no lo hizo.

### 8.3 La revisión del acceso

Una **revisión del acceso** periódica concilia tres fuentes: la lista de cuentas (lo que existe), el registro de contratos (lo que debería existir) y los registros de sesiones (lo que se usa). Hallazgos típicos y respuestas proporcionadas:

| Hallazgo | Por qué importa | Respuesta proporcionada |
|---|---|---|
| Cuenta de un contrato terminado | Nadie rinde cuentas de su uso | Desactivarla ya; confirmarlo con el proveedor |
| Sin uso durante más de 90 días | Exposición innecesaria | Desactivarla; reactivarla a petición mediante el proceso |
| Cuenta compartida o sin nombre | Las acciones no pueden atribuirse | Sustituirla por cuentas nominativas; mientras tanto, restringirla |
| Sin MFA | Basta la contraseña para acceder | Corregirlo o registrar una excepción limitada en el tiempo |
| Uso muy por encima de lo esperado | Puede ser un proyecto legítimo, un mal uso o un compromiso | Preguntar al proveedor y al dueño interno; revisar los registros de sesiones antes de concluir |

La última fila exige cuidado. Un volumen inusual es una **pregunta**, no una acusación.

### 8.4 Caso resuelto: la revisión de mayo (sintético)

Tras las lagunas de control del capítulo 7, la coordinadora realiza la primera revisión del acceso de proveedores el 4 de mayo de 2026, con una autorización de A. Mensah que permite exportar en modo de solo lectura la lista de cuentas y el registro de sesiones de la pasarela. El **Lab 8** reproduce la conciliación. **Lab 8** (guárdelo como `lab08.py` y ejecútelo con `python3 lab08.py`):

```python
# Lab 8 - third-party remote-access review (offline, standard library only; all data synthetic)
import datetime as dt
TODAY = dt.date(2026, 5, 4)
# account, supplier, named person, MFA, contract end, last session, sessions in 90 days
ACCOUNTS = [
    ("v-hydro1",  "HydroLogic Ltd",  "P. Novak",  True,  "2027-03-31", "2026-04-28", 6),
    ("v-hydro2",  "HydroLogic Ltd",  "",          True,  "2027-03-31", "2026-04-30", 11),
    ("v-scadaco", "ScadaCo",         "M. Ilic",   False, "2026-12-31", "2026-03-15", 2),
    ("v-pumps",   "Vale Pumps",      "D. Ruiz",   True,  "2025-11-30", "2026-02-10", 1),
    ("v-meter",   "MeterWorks",      "K. Sato",   True,  "2026-09-30", "2025-10-02", 0),
    ("v-integr",  "Northgate Integration", "S. Brandt", True, "2026-08-31", "2026-05-01", 19),
]
SESSIONS_EXPECTED = {"HydroLogic Ltd": 8, "ScadaCo": 4, "Vale Pumps": 2, "MeterWorks": 2, "Northgate Integration": 4}
for acct, sup, person, mfa, end, last, n90 in ACCOUNTS:
    f = []
    if not person: f.append("shared/unnamed account")
    if not mfa: f.append("no MFA")
    if dt.date.fromisoformat(end) < TODAY: f.append("contract ended - disable")
    if (TODAY - dt.date.fromisoformat(last)).days > 90: f.append("unused >90 days - disable")
    if n90 > 2 * SESSIONS_EXPECTED[sup]: f.append(f"{n90} sessions vs ~{SESSIONS_EXPECTED[sup]} expected - ask why")
    print(f"{acct:10s} {sup:22s} {'OK' if not f else '; '.join(f)}")
```

Salida esperada (Python 3.13.5):

```text
v-hydro1   HydroLogic Ltd         OK
v-hydro2   HydroLogic Ltd         shared/unnamed account
v-scadaco  ScadaCo                no MFA
v-pumps    Vale Pumps             contract ended - disable
v-meter    MeterWorks             unused >90 days - disable
v-integr   Northgate Integration  19 sessions vs ~4 expected - ask why
```

El análisis de la coordinadora, etiquetado:

- **Decidido (por A. Mensah, 4 de mayo):** desactivar hoy `v-pumps` (el contrato de Vale Pumps terminó en noviembre) y `v-meter` (sin uso desde octubre); sustituir `v-hydro2` por una cuenta nominativa en 14 días y, mientras tanto, restringirla a sesiones supervisadas.
- **Debido:** ScadaCo debe activar la MFA en `v-scadaco` en 30 días, o se propondrá una excepción con medidas compensatorias (capítulo 7); dueño, A. Mensah.
- **Abierto:** `v-integr`: Northgate Integration tuvo 19 sesiones en 90 días frente a unas 4 esperadas. La coordinadora **no** concluye que haya un mal uso. Pregunta a J. Tan si un proyecto lo explica y pide el registro de trabajo al gestor de cuenta de Northgate. J. Tan responde que Northgate está poniendo en servicio el nuevo enlace de telemetría de KW-11, aprobado en marzo; el registro de trabajo coincide con 17 de las 19 sesiones. Dos sesiones, el 12 y el 19 de abril a las 02:00, no figuran en el registro de trabajo. Esas dos se pasan a la responsable de seguridad y al KVROC para que revisen los registros de sesiones, por la vía de escalado de incidentes, y al proveedor solo se le informa después de que la responsable de seguridad lo acepte.
- **Supuesto:** la exportación de la pasarela está completa. (Próxima revisión: comparar también con los orígenes permitidos del cortafuegos).

El caso muestra la disciplina de la coordinadora: actuar con rapidez ante los fallos claros de gobernanza, preguntar antes de acusar, escalar por la vía adecuada la actividad que sigue sin explicación y registrar lo que se supone.

### 8.5 Requisitos para contratos e incorporación

A partir del caso, la coordinadora redacta cláusulas estándar para los nuevos contratos de proveedores con acceso remoto: solo personas con nombre; MFA; sesiones solo a través de la pasarela de la empresa, aprobadas por sesión o por ventana programada; el proveedor notificará a la empresa en las 24 horas siguientes la salida de un empleado y, con prontitud, cualquier incidente de seguridad que pueda afectar a la empresa; registros de trabajo disponibles a petición; cooperación en la respuesta a incidentes; borrado de los datos de la empresa al terminar el contrato, confirmado por escrito. La ISA/IEC 62443 incluye requisitos para proveedores de servicios e integradores que pueden orientar esas cláusulas ([ISA/IEC 62443 overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). La redacción jurídica corresponde a su equipo jurídico; su trabajo es especificar el resultado de seguridad.

### 8.6 Presentación supervisada

Presente el caso a su supervisor (aquí, E. Varga) en cinco partes: qué se revisó y con qué autoridad; los hallazgos, con evidencia; las decisiones ya tomadas y quién las tomó; las decisiones que se solicitan al supervisor (presupuesto para la MFA del lado de ScadaCo, aprobación de las cláusulas contractuales); y las preguntas abiertas, con responsables y fechas. Mantenga cada parte breve y etiquetada, para que el supervisor pueda interrumpirle en cualquier momento y aun así saber qué está decidido y qué se pide. En la revisión de mayo, las dos sesiones de Northgate sin explicar van en las preguntas abiertas con su responsable, no en los hallazgos. Lleve como adjuntos la salida del Lab 8 y la autorización, y diga con claridad lo que se supuso, como que la exportación de la pasarela estaba completa. Termine repitiendo las decisiones solicitadas y la fecha para la que se necesitan.

### 8.7 Errores comunes y límites

- Tratar una actividad inusual como prueba de compromiso, o ignorarla como «probablemente el proyecto».
- Retirar un acceso necesario para el soporte crítico para la seguridad sin una alternativa.
- Revisiones que usan una sola fuente (cuentas sin contratos ni sesiones).
- Cláusulas contractuales que no pueden comprobarse.
- El laboratorio modela una sola pasarela; los entornos reales tienen varias rutas de acceso (marcación telefónica, módems celulares, herramientas remotas instaladas por el proveedor) que la revisión debe encontrar.

- Desactivar la cuenta de un proveedor cuyo soporte se necesita para un problema de dosificación en curso, sin organizar una alternativa.
- Cerrar una revisión una vez corregidos los hallazgos evidentes, mientras dos sesiones sin explicar siguen abiertas sin responsable.

### Ejercicios — capítulo 8

**EX036 — Lea el Lab 8.** *Objetivo:* interpretar los resultados de la revisión. *Insumos:* la salida del Lab 8. *Pasos:* para cada cuenta, indicar el hallazgo, el riesgo y la respuesta proporcionada con su responsable. *Evidencia esperada:* seis filas. *Rúbrica:* 3 = coincide con 8.4, incluida la contención con `v-integr` y una alternativa para `v-scadaco`; 2 = acciones correctas, pero acusatorio con `v-integr`; 1 = lo desactiva todo; 0 = nada.

**EX037 — Amplíe la revisión.** *Objetivo:* añadir una fuente. *Insumos:* el Lab 8. *Pasos:* añadir por cuenta una fecha de «última confirmación del personal» y señalar las cuentas cuyo proveedor no haya confirmado su lista de personal en 180 días; mostrar la salida. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = campo añadido en todas las filas con valores de prueba que activan y que no activan la regla, salida mostrada, explica por qué importa la confirmación del personal (salidas); 2 = sin explicación; 1 = solo la regla; 0 = nada.

**EX038 — Redacte cláusulas contractuales.** *Objetivo:* especificar las obligaciones del proveedor. *Insumos:* 8.5. *Pasos:* escribir cinco cláusulas comprobables en lenguaje llano. *Evidencia esperada:* las cláusulas. *Rúbrica:* 3 = cada cláusula tiene una obligación medible y una forma de verificarla (por ejemplo, aviso de salida de personal en 24 horas, verificado en la revisión trimestral); 2 = no comprobables; 1 = «el proveedor será seguro»; 0 = nada.

**EX039 — Gestione las dos sesiones nocturnas.** *Objetivo:* escalar adecuadamente la actividad sin explicar. *Insumos:* 8.4. *Pasos:* escribir el mensaje a la responsable de seguridad y la decisión que necesita. *Evidencia esperada:* el mensaje. *Rúbrica:* 3 = hechos con horas en UTC y fuente, lo que se sabe (17 de 19 explicadas), lo que no, solicitud de revisión de los registros de sesiones por la vía de escalado, indicación de no alertar todavía al proveedor, tratamiento sensible (TLP:RED o AMBER+STRICT), hora de la próxima comprobación; 2 = sin indicaciones de tratamiento; 1 = «por favor, investigue a Northgate»; 0 = nada.

**EX040 — Presente el caso.** *Objetivo:* presentación supervisada. *Insumos:* 8.6. *Pasos:* escribir la sesión informativa de cinco partes en menos de 300 palabras. *Evidencia esperada:* la sesión informativa. *Rúbrica:* 3 = las cinco partes, decisiones solicitadas de forma explícita, incertidumbre etiquetada, ninguna acusación sin fundamento; 2 = faltan las decisiones solicitadas; 1 = solo una narración; 0 = nada.

### Síntesis del capítulo

El acceso de proveedores se gobierna a lo largo de un ciclo de vida (seleccionar, contratar, incorporar, operar, cambiar, salir) y la mayoría de los fallos están en las juntas. Una revisión del acceso concilia cuentas, contratos y sesiones; responda de forma proporcionada, trate las anomalías como preguntas y escale por la vía adecuada lo que siga sin explicación. Convierta las lecciones en requisitos contractuales comprobables y presente los casos con las decisiones solicitadas y la incertidumbre etiquetada.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Siga estudiando — capítulo 08 de 12

[← Capítulo 07](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Comunicación, ética e informes

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- identificar todas las obligaciones de notificación que puede desencadenar un incidente (legales, regulatorias, contractuales, de seguros) y gestionar sus relojes;
- redactar una declaración provisional y una sesión informativa para un cliente crítico que sean exactas, útiles y honestas sobre la incertidumbre;
- aplicar principios éticos a la comunicación: veracidad, proporcionalidad, equidad con las personas y corrección de los errores;
- informar de los incidentes y del estado del programa a la dirección y al consejo de una forma que respalde las decisiones.

Los capítulos 1–8 construyeron y ejercitaron el programa hacia dentro. Este capítulo mira hacia fuera.

### 9.1 A quién hay que informar y cuándo

Un incidente en un servicio esencial puede poner en marcha varios relojes a la vez. Con la NIS2, por ejemplo, las entidades deben enviar al CSIRT nacional o a la autoridad competente una **alerta temprana en 24 horas** desde que tienen conocimiento de un incidente significativo, una **notificación del incidente en 72 horas** y un **informe final en el plazo de un mes** desde la notificación ([Directive (EU) 2022/2555, Article 23](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)). Otras jurisdicciones, sectores y contratos fijan desencadenantes y plazos distintos; las brechas de datos personales pueden acarrear obligaciones separadas; las aseguradoras suelen exigir un aviso rápido. Un coordinador prepara de antemano un **registro de notificaciones**: cada obligación, su desencadenante, destinatario, plazo, contenido, responsable y canal.

Dos detalles deciden si cumple un reloj: **qué lo pone en marcha** (la detección, el conocimiento, la determinación de que el incidente es «significativo») y **quién registra ese momento**. Acuerde ambos antes de los incidentes y registre la hora de inicio en UTC en el registro de decisiones.

### 9.2 Clientes críticos

Los hospitales, las residencias, los pacientes de diálisis, otras empresas de servicios y los servicios de emergencia pueden necesitar actuar antes que el público. Sus necesidades son prácticas: qué está afectado, qué deben hacer, durante cuánto tiempo, cuándo llega la próxima actualización y a quién llamar. Los acuerdos con ellos (capítulo 2) suelen prometer una llamada en un plazo corto. Mantenga probados sus contactos y mantenga el mensaje libre de detalles técnicos. El acuerdo del Kestrel General Hospital promete una llamada en las dos horas siguientes a cualquier evento que pueda afectar al suministro o a la calidad; los contactos son la guardia de instalaciones y, fuera de horario, el responsable de turno del centro.

### 9.3 Comunicación pública

Una **declaración provisional** es un mensaje breve y factual que se emite pronto, antes de conocer el panorama completo. Dice lo que se sabe, lo que está haciendo la organización, lo que debe hacer el público (si debe hacer algo) y cuándo habrá más información. No especula sobre la causa ni la atribución, no minimiza («sin impacto») sin evidencia y no revela detalles útiles para un atacante. La redacta el responsable de comunicación; la aprueba el directivo que rinde cuentas (capítulo 6); operaciones confirma que cualquier afirmación sobre la seguridad («el agua es apta para beber») es cierta.

### 9.4 Ética

La comunicación sobre los servicios esenciales tiene peso para la seguridad pública. Cuatro principios:

- **Veracidad**: no afirme nunca como hecho lo que es un supuesto; no niegue nunca lo que sabe.
- **Proporcionalidad**: detalle suficiente para que las personas se protejan, no más; evite causar alarma innecesaria y evite ayudar a los atacantes.
- **Equidad con las personas**: no nombre ni culpe públicamente a un empleado o a un proveedor con información incompleta; el error humano suele ser un problema del sistema.
- **Corrección**: cuando una declaración resulte errónea, corríjala con prontitud y de forma visible.

Internamente, una cultura de notificación **sin culpa** (las personas comunican errores y casi accidentes sin miedo) da al coordinador las señales tempranas de las que depende la comunicación externa.

### 9.5 Ejemplo resuelto: los relojes del sábado (sintético)

El sábado 13 de junio de 2026, a las 21:40 UTC, el responsable del incidente determina que un acceso no autorizado a la red de supervisión es un incidente significativo. Las normas ficticias de Kestrel Vale reproducen el patrón de 24 h / 72 h / un mes de la NIS2; el acuerdo del hospital exige una llamada en 2 horas; la póliza de seguro exige un aviso en 48 horas. El martes por la tarde, la coordinadora comprueba el registro con el **Lab 9**. **Lab 9** (guárdelo como `lab09.py` y ejecútelo con `python3 lab09.py`):

```python
# Lab 9 - notification clocks after an incident (offline, standard library only; synthetic obligations)
# The deadlines are ILLUSTRATIVE for the fictional Kestrel Vale jurisdiction; real duties come from your own
# law, regulator and contracts. The 24 h / 72 h / one-month pattern mirrors EU NIS2 Article 23.
from datetime import datetime, timedelta, timezone
UTC = timezone.utc
aware = datetime(2026, 6, 13, 21, 40, tzinfo=UTC)        # incident judged significant (Saturday evening)
OBLIGATIONS = [  # name, hours after awareness, recipient
    ("Critical-customer call (contract)", 2,      "Kestrel General Hospital"),
    ("Regulator early warning",          24,     "Kestrel Vale CSIRT"),
    ("Insurer notice (policy)",          48,     "insurer"),
    ("Regulator incident notification",  72,     "Kestrel Vale CSIRT"),
    ("Regulator final report",           24*30,  "Kestrel Vale CSIRT"),   # 'one month' modelled as 30 days
]
SENT = {"Critical-customer call (contract)": datetime(2026, 6, 13, 23, 55, tzinfo=UTC),
        "Regulator early warning": datetime(2026, 6, 14, 18, 5, tzinfo=UTC),
        "Regulator incident notification": datetime(2026, 6, 16, 22, 30, tzinfo=UTC)}
NOW = datetime(2026, 6, 16, 23, 0, tzinfo=UTC)
for name, h, who in OBLIGATIONS:
    due = aware + timedelta(hours=h)
    sent = SENT.get(name)
    if sent:
        delta = (sent - due).total_seconds() / 3600
        state = f"sent {sent:%a %d %H:%M}Z, {'LATE by' if delta > 0 else 'early by'} {abs(delta):.2f} h"
    else:
        state = "OVERDUE - not sent" if NOW > due else f"open, {(due - NOW).total_seconds()/3600:.1f} h left"
    print(f"{name:35s} due {due:%a %d %b %H:%M}Z  {state}")
```

Salida esperada (Python 3.13.5):

```text
Critical-customer call (contract)   due Sat 13 Jun 23:40Z  sent Sat 13 23:55Z, LATE by 0.25 h
Regulator early warning             due Sun 14 Jun 21:40Z  sent Sun 14 18:05Z, early by 3.58 h
Insurer notice (policy)             due Mon 15 Jun 21:40Z  OVERDUE - not sent
Regulator incident notification     due Tue 16 Jun 21:40Z  sent Tue 16 22:30Z, LATE by 0.83 h
Regulator final report              due Mon 13 Jul 21:40Z  open, 646.7 h left
```

Surgen tres problemas. La llamada al hospital llegó 15 minutos tarde: la coordinadora estaba al teléfono con el oficial de guardia del regulador y el responsable de comunicación creía que ella llamaría al hospital; es el defecto de los dos R del capítulo 6 en la vida real. Nunca se avisó a la aseguradora: nadie tenía la póliza en el registro de notificaciones. La notificación de 72 horas al regulador llegó 50 minutos tarde porque la aprobación del consejero delegado se pidió a las 21:00 para un plazo de las 21:40. La alerta temprana, preparada a partir de una plantilla, salió con antelación.

La coordinadora registra estos hechos en el registro de decisiones sin culpar a nadie, avisa de inmediato a la aseguradora con una explicación y añade dos acciones para la revisión: incluir la obligación del seguro en el registro con un responsable y fijar plazos internos para las aprobaciones (por ejemplo, «aprobación solicitada a más tardar 6 horas antes del plazo externo»). El laboratorio calcula los relojes; no decide qué cuenta como «tener conocimiento», que sigue siendo un juicio documentado.

### 9.6 Informar a la dirección y al consejo

Un informe breve de incidente para la dirección abarca: qué ocurrió (hechos, con el grado de confianza etiquetado); el impacto sobre el servicio y las personas; lo que se ha hecho y decidido; las obligaciones cumplidas e incumplidas; los riesgos actuales; las decisiones necesarias. Los informes del programa (mensuales o trimestrales) usan las métricas que impulsan decisiones del capítulo 5 y los principales riesgos clasificados por consecuencia del capítulo 4. Para el incidente del sábado, el informe a la dirección mostraría que la llamada al hospital llegó quince minutos tarde, que no se avisó a la aseguradora y que la notificación de 72 horas fue tardía, con las causas encontradas en lugar de nombres. Terminaría con las dos acciones para el registro y los plazos de aprobación, y pediría a la dirección que confirme ambas. Manténgalo en una página y adjunte los cálculos de los relojes, para que un lector pueda comprobar cada hora sin fiarse del resumen.

### 9.7 Actividad práctica

Redacte un registro de notificaciones para una organización que conozca, con al menos cinco obligaciones. Para cada una, escriba qué pone en marcha el reloj y quién lo registra. Marque toda obligación cuya fuente no haya verificado. Incluya los contratos y los seguros además de la ley, ya que el incidente del sábado mostró que el plazo de aviso de una aseguradora puede incumplirse simplemente porque nadie lo había anotado. Para cada obligación, nombre un responsable, fije un plazo interno de aprobación anterior al externo y registre el documento de origen con su cláusula. Compruebe si dos obligaciones se ponen en marcha en el mismo momento; si es así, acuerde quién registra ese momento y en qué zona horaria. Revise el registro cada vez que se renueve un contrato o una póliza.

### 9.8 Errores comunes y límites

- Obligaciones de notificación descubiertas durante el incidente.
- Ningún plazo interno para las aprobaciones, de modo que se incumple el plazo externo.
- Declaraciones provisionales que prometen «sin impacto» antes de que exista evidencia.
- Nombrar prematuramente a personas o proveedores.
- Las obligaciones legales reales varían; confirme las suyas con su asesoría jurídica y con su regulador. Los relojes de este libro son ilustrativos.

- Dejar una llamada, como la sesión informativa al hospital, en manos de dos personas que dan por hecho que la hará la otra.
- Poner en marcha cada reloj desde un momento distinto porque nadie acordó qué cuenta como tener conocimiento.
- Olvidar las obligaciones contractuales y de seguros porque el registro solo enumera reguladores.

### Ejercicios — capítulo 9

**EX041 — Lea el Lab 9.** *Objetivo:* interpretar los relojes de notificación. *Insumos:* la salida del Lab 9. *Pasos:* para cada obligación, indicar el estado y la causa raíz de cualquier incumplimiento usando 9.5. *Evidencia esperada:* cinco filas. *Rúbrica:* 3 = hospital tarde por 0,25 h (responsabilidad poco clara), alerta temprana cumplida, aseguradora vencida (no figuraba en el registro), notificación tarde por 0,83 h (aprobación tardía), informe final abierto con 646,7 h; las causas raíz son de proceso, no de personas; 2 = solo los estados; 1 = parcial; 0 = nada.

**EX042 — Redacte una declaración provisional.** *Objetivo:* comunicar pronto y con honestidad. *Insumos:* la empresa investiga un acceso no autorizado a sistemas que supervisan el tratamiento del agua; el personal de operaciones gestiona dos estaciones en manual; los análisis de calidad del agua son normales. *Pasos:* redactar una declaración de menos de 120 palabras. *Evidencia esperada:* la declaración. *Rúbrica:* 3 = solo hechos, lo que se está haciendo, lo que deben hacer los clientes (nada salvo que se les indique; cómo llegarán las actualizaciones), hora de la próxima actualización, sin especulación ni detalles útiles para un atacante, afirmación de seguridad solo tal como la confirme operaciones; 2 = especulación menor; 1 = «sin impacto, todo bien»; 0 = nada.

**EX043 — Informe al hospital.** *Objetivo:* comunicación con un cliente crítico. *Insumos:* el mismo incidente; la presión de la zona este puede bajar hasta 4 horas mañana durante una conmutación controlada. *Pasos:* escribir el guion de la llamada. *Evidencia esperada:* el guion. *Rúbrica:* 3 = efecto en los términos del hospital, horario, seguridad del agua, lo que el hospital puede necesitar hacer (agua almacenada, prioridades), próxima actualización, contacto 24 h; pregunta qué necesita el hospital; 2 = ninguna pregunta al hospital; 1 = detalles técnicos; 0 = nada.

**EX044 — Dilema ético.** *Objetivo:* aplicar los principios. *Insumos:* un periodista pregunta si el ingeniero de un proveedor causó el incidente; la evidencia interna sugiere que estuvo implicado el portátil robado del proveedor, sin confirmar. *Pasos:* redactar la respuesta y justificarla. *Evidencia esperada:* respuesta y razonamiento. *Rúbrica:* 3 = se niega a atribuir o nombrar con información sin confirmar, explica que la investigación sigue abierta, se compromete a actualizar, el razonamiento cita la veracidad y la equidad; 2 = respuesta correcta sin razonamiento; 1 = nombra al proveedor; 0 = nada.

**EX045 — Arregle el proceso de aprobación.** *Objetivo:* evitar las notificaciones tardías. *Insumos:* 9.5. *Pasos:* diseñar plazos internos y delegaciones para los tres relojes externos. *Evidencia esperada:* el diseño. *Rúbrica:* 3 = plazos internos antes de cada plazo externo, aprobadores suplentes con nombre cuando el consejero delegado no está disponible, plantillas preparadas, inicio del reloj registrado en UTC por el responsable del incidente, aseguradora añadida al registro; 2 = solo plazos; 1 = «ser más rápidos»; 0 = nada.

### Síntesis del capítulo

Los incidentes ponen en marcha varios relojes a la vez; conózcalos de antemano, acuerde qué pone en marcha cada uno y quién lo registra, y fije plazos internos de aprobación anteriores a los externos. Los clientes críticos necesitan mensajes prácticos y tempranos; el público necesita declaraciones provisionales veraces y proporcionadas. Comunique sin culpar ni especular, corrija los errores de forma visible e informe a la dirección con hechos, impacto, decisiones y obligaciones.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Siga estudiando — capítulo 09 de 12

[← Capítulo 08](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Infraestructura crítica y seguridad sectorial: calidad y diagnóstico de averías

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- reconocer los patrones de fallo habituales de los programas de coordinación de la seguridad;
- diagnosticar con método un fallo de coordinación (síntoma, hipótesis, evidencia, causa, corrección) en lugar de culpar a las personas;
- medir la calidad de las decisiones en un ejercicio o en un incidente, no solo su rapidez;
- conducir un proceso de acciones correctivas que de verdad cierre las acciones.

El capítulo 9 dejó al descubierto fallos reales de coordinación. Este capítulo trata el propio programa como un sistema que puede diagnosticarse y mejorarse.

### 10.1 Cómo fallan los programas

La mayoría de los fallos de coordinación encajan en unos pocos patrones:

- **Lagunas de titularidad**: actividades o riesgos sin nadie que rinda cuentas (capítulos 4 y 6).
- **Responsabilidad duplicada**: dos personas creen cada una que actuó la otra.
- **Información obsoleta**: contactos, mapas de dependencias, listas de proveedores o registros que eran correctos el año pasado.
- **Controles de papel**: documentados, pero nunca observados ni probados (capítulo 7).
- **Cuellos de botella**: una misma persona en todas las rutas críticas.
- **Deterioro de las acciones**: lecciones identificadas tras cada ejercicio y nunca aplicadas.
- **Rapidez sin calidad**: decisiones tomadas a tiempo, pero sin justificación, con información errónea o sin las personas adecuadas.

### 10.2 Diagnosticar un fallo de coordinación

Use la misma disciplina que usan los ingenieros con las averías técnicas:

1. **Enuncie el síntoma** con precisión («se llamó al hospital 15 minutos después de las 2 horas contractuales»).
2. **Enumere hipótesis** («nadie era responsable de la llamada»; «el número de contacto era erróneo»; «el reloj de 2 horas empezó en un momento distinto para personas distintas»).
3. **Reúna evidencia** (registros de decisiones, registros de llamadas, entrevistas) sin culpar a nadie.
4. **Descarte** las hipótesis que contradice la evidencia.
5. **Corrija la causa**, no el síntoma, y decida cómo verificará la corrección.

Un hábito útil: preguntar «¿qué hizo que esto fuera lo razonable en aquel momento?». Las personas rara vez actúan con descuido en una crisis; actúan con la información y las funciones que tenían.

### 10.3 Calidad de las decisiones

La puntualidad es fácil de medir; la calidad es más difícil, pero más importante. Para cada decisión clave de un ejercicio o un incidente, compruebe: ¿tenía un responsable? ¿Se tomó dentro del tiempo objetivo? ¿Se registró la justificación? ¿Se consultó a quienes había que consultar? ¿Se basó en información verificada, con los supuestos etiquetados? La guía del NIST sobre programas de pruebas, formación y ejercicios describe cómo evaluar los ejercicios frente a sus objetivos y recoger las lecciones ([NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final)).

### 10.4 Ejemplo resuelto: el registro del ejercicio de mesa de mayo (sintético)

En el ejercicio de mesa de mayo DRY CREEK (su diseño es el ejemplo resuelto del capítulo 11), un evaluador llevó un registro de decisiones. El **Lab 10** lo comprueba. **Lab 10** (guárdelo como `lab10.py` y ejecútelo con `python3 lab10.py`):

```python
# Lab 10 - tabletop decision-log quality check (offline, standard library only; synthetic exercise log)
import csv, io
LOG = """minute,inject,decision,owner,target_min,taken_min,recorded_rationale
0,I1 HMI shows unexpected setpoint change,convene incident team,Coordinator,15,9,yes
20,I2 vendor reports stolen laptop,suspend vendor remote access,Ops manager,30,52,yes
35,I3 station KW-04 dosing alarm,switch KW-04 to manual,Ops manager,10,6,no
50,I4 journalist calls,holding statement,,30,41,yes
65,I5 hospital asks about water safety,brief hospital,Coordinator,20,,no
80,I6 regulator early-warning clock,send early warning,Coordinator,60,44,yes
"""
rows = list(csv.DictReader(io.StringIO(LOG)))
met = 0
for r in rows:
    f = []
    if not r["owner"]: f.append("no owner")
    if not r["taken_min"]: f.append("no decision taken")
    elif int(r["taken_min"]) > int(r["target_min"]): f.append(f"late {int(r['taken_min'])-int(r['target_min'])} min")
    else: met += 1
    if r["recorded_rationale"] != "yes": f.append("no rationale recorded")
    print(f"{r['inject'][:2]} {r['decision']:30s} {'ok' if not f else '; '.join(f)}")
print(f"decisions within target: {met}/{len(rows)}")
```

Salida esperada (Python 3.13.5):

```text
I1 convene incident team          ok
I2 suspend vendor remote access   late 22 min
I3 switch KW-04 to manual         no rationale recorded
I4 holding statement              no owner; late 11 min
I5 brief hospital                 no decision taken; no rationale recorded
I6 send early warning             ok
decisions within target: 3/6
```

El titular «3/6 dentro del objetivo» oculta más de lo que muestra:

- La decisión de I3 de pasar KW-04 a manual fue rápida (6 minutos frente a 10) y se contó como puntual, pero **no se registró ninguna justificación**. En una decisión relacionada con la seguridad de las personas, eso importa: en un incidente real, la revisión no sabría si se tomó por los datos de dosificación, por precaución o por una conjetura.
- La declaración provisional de I4 **no tenía responsable** (otra vez el defecto de comunicación del capítulo 6) y llegó tarde.
- I5, la sesión informativa al hospital, **nunca se decidió**. En la puesta en común en caliente, los jugadores dijeron que «daban por hecho que se encargaba comunicación».
- I2, la suspensión del acceso del proveedor, llegó 22 minutos tarde. Los jugadores explicaron que nadie sabía si suspender el acceso de HydroLogic detendría el soporte a un problema de dosificación que estaba en curso. Esa es una causa de **información que faltaba**, no de lentitud.

La tabla de diagnóstico de la coordinadora:

| Síntoma | Hipótesis | Evidencia | Causa | Corrección | Verificar mediante |
|---|---|---|---|---|---|
| I5: sesión informativa al hospital no realizada | Sin responsable; contacto desconocido; olvido bajo presión | Puesta en común: «dábamos por hecho que se encargaba comunicación»; la RACI tenía dos R | Responsabilidad duplicada | Un único responsable principal en la RACI; llamada al hospital en la lista de comprobación del incidente | Inyección sobre el hospital en el próximo ejercicio |
| I2: suspensión del proveedor tardía | Aprobación poco clara; impacto desconocido | Los jugadores preguntaron quién depende del acceso de HydroLogic | Faltaba información de dependencias | Añadir «quién depende del acceso de este proveedor» al registro de proveedores | La revisión del Lab 8 incluye una columna de dependencias |
| I3: sin justificación | A la plantilla del registro le falta el campo; presión de tiempo | La plantilla no tiene columna de justificación | Diseño de la herramienta | Añadir el campo de justificación; función de secretario de actas | Al volver a ejecutar el Lab 10 aparece la justificación |

### 10.5 Cerrar las acciones correctivas

Las lecciones no mejoran nada hasta que se convierten en acciones con responsables, fechas y verificación, y se cierran. Haga su seguimiento en un solo lugar, revíselas en el comité de riesgos y verifique cada cierre con evidencia (el próximo ejercicio, una prueba, un documento). Una métrica útil del programa es el porcentaje de acciones de ejercicios cerradas y verificadas dentro de su plazo. En la revisión de DRY CREEK, cada corrección tiene su verificación correspondiente: la próxima inyección del ejercicio sobre el hospital, un registro de proveedores con una columna de dependencias comprobado en la próxima revisión del acceso y una nueva ejecución del Lab 10 que muestre las justificaciones registradas.

### 10.6 Actividad práctica

Tome un fallo reciente de cualquier equipo que conozca (un plazo incumplido, una tarea duplicada). Rellene la tabla de diagnóstico sin nombrar a personas y proponga una corrección con un método de verificación. Escriba el síntoma como un hecho preciso con horas o recuentos, como en el ejemplo del hospital, y no como un juicio. Enumere al menos tres hipótesis antes de buscar evidencia y anote qué evidencia descartó cada una. Pregunte qué hizo que la acción fuera razonable para las personas implicadas en aquel momento. Después elija una corrección que cambie una función, una herramienta o una información, no una que pida a las personas que se esfuercen más, y diga cómo sabrá que funcionó, por ejemplo en el próximo ejercicio o revisión.

### 10.7 Errores comunes y límites

- Concluir «error humano» y detenerse ahí.
- Acciones sin verificación, cerradas por la palabra del responsable.
- Corregir en exceso con procesos pesados que ralentizan las respuestas reales; mantenga las correcciones proporcionadas.

- Corregir el síntoma con una exhortación («comunicarse mejor»), como recordar al personal que llame al hospital, mientras la RACI sigue mostrando dos R.
- Medir el éxito de un ejercicio solo por la rapidez, contando como buena una decisión rápida sin justificación registrada, como el paso de KW-04 a manual en DRY CREEK.
- Hacer el seguimiento de las acciones en varios lugares, de modo que nadie puede ver cuáles están vencidas.

### Ejercicios — capítulo 10

**EX046 — Lea el Lab 10.** *Objetivo:* interpretar la calidad de las decisiones. *Insumos:* la salida del Lab 10. *Pasos:* explicar por qué «3/6 dentro del objetivo» exagera el desempeño y nombrar el defecto más grave. *Evidencia esperada:* la explicación. *Rúbrica:* 3 = I3 contado como puntual sin justificación; I5 no se tomó en absoluto (riesgo para un cliente crítico); I4 sin responsable; el más grave es I5 o I3, con razonamiento; 2 = enumera los defectos sin juicio; 1 = acepta el 3/6; 0 = nada.

**EX047 — Añada una regla de calidad.** *Objetivo:* codificar otra comprobación. *Insumos:* el Lab 10. *Pasos:* añadir las columnas `safety` y `consulted`; señalar toda decisión relacionada con la seguridad de las personas cuyo responsable no sea el jefe de operaciones y en la que no se consultara al jefe de operaciones; probarlo con las seis filas originales más una fila inventada en la que la responsable de seguridad decide aislar una estación sin consultar a operaciones; mostrar la salida. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = columnas rellenadas en todas las filas, regla limitada a las decisiones de seguridad de las personas, la fila inventada señalada e I3 (cuyo responsable es operaciones) no señalada, con ese resultado explicado; 2 = la regla señala todas las filas sin entrada de consulta; 1 = solo la regla; 0 = nada.

**EX048 — Diagnostique I4.** *Objetivo:* aplicar 10.2. *Insumos:* la fila de I4 y la RACI del capítulo 6. *Pasos:* rellenar la tabla de diagnóstico para la declaración provisional. *Evidencia esperada:* una fila de la tabla con hipótesis. *Rúbrica:* 3 = al menos dos hipótesis, evidencia (la RACI no tenía A para la declaración pública), causa, corrección (consejero delegado A, comunicación R, plantilla), verificación (próximo ejercicio); 2 = sin verificación; 1 = «comunicación fue lenta»; 0 = nada.

**EX049 — Diagnostique información obsoleta.** *Objetivo:* reconocer el deterioro. *Insumos:* durante un incidente, el número fuera de horario del hospital daba a una línea desconectada. *Pasos:* proponer un análisis de causas y una corrección duradera. *Evidencia esperada:* análisis y corrección. *Rúbrica:* 3 = causa: ningún responsable ni calendario para verificar los contactos; corrección: llamadas de prueba trimestrales con responsable, actualización ante las reorganizaciones del hospital, segunda vía de contacto; métrica de verificación; 2 = actualización puntual; 1 = culpa; 0 = nada.

**EX050 — Cierre las acciones.** *Objetivo:* diseñar el seguimiento de las acciones correctivas. *Insumos:* las tres correcciones de 10.4. *Pasos:* escribir un registro de acciones con responsable, fecha límite, evidencia de cierre y método de verificación. *Evidencia esperada:* el registro. *Rúbrica:* 3 = cada una tiene un responsable con autoridad, una fecha realista, una evidencia de cierre distinta de la afirmación del responsable y una verificación en un ejercicio o una revisión posteriores; 2 = sin verificación; 1 = solo una lista; 0 = nada.

### Síntesis del capítulo

Los programas de coordinación fallan de maneras reconocibles: lagunas de titularidad, responsabilidad duplicada, información obsoleta, controles de papel, cuellos de botella, deterioro de las acciones y rapidez sin calidad. Diagnostíquelos como averías, del síntoma a las hipótesis y la evidencia hasta la causa, sin culpar a nadie. Mida la calidad de las decisiones, no solo la rapidez, y cierre las acciones correctivas solo con evidencia verificada.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Siga estudiando — capítulo 10 de 12

[← Capítulo 09](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Laboratorio supervisado

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- diseñar un **ejercicio de mesa** basado en la discusión para un servicio esencial, con objetivos, escenario, inyecciones, funciones y criterios de evaluación;
- conducirlo de forma segura y justa, de modo que siga siendo una prueba de los planes y no de las personas;
- evaluarlo con una puesta en común en caliente, un informe posterior a la acción y un plan de mejora;
- evaluar el diseño de un ejercicio frente a una rúbrica, bajo supervisión.

Para una coordinadora profesional, el laboratorio es la sala del ejercicio. Este capítulo reúne todo lo visto hasta ahora (partes interesadas, autorización, riesgo, RACI, acceso de proveedores, relojes de notificación, calidad de las decisiones) en un único ejercicio supervisado.

### 11.1 Tipos de ejercicio

Los programas de ejercicios distinguen los ejercicios **basados en la discusión** (seminarios, talleres, ejercicios de mesa), en los que los participantes recorren de palabra un escenario, de los ejercicios **basados en operaciones** (simulacros, ejercicios funcionales, ejercicios a escala real), en los que ejecutan acciones. El Homeland Security Exercise and Evaluation Program (HSEEP) de Estados Unidos expone esta progresión y un ciclo de diseñar, conducir, evaluar y mejorar ([FEMA, HSEEP](https://www.fema.gov/emergency-managers/national-preparedness/exercises/hseep)). La guía del NIST abarca los programas de pruebas, formación y ejercicios para los planes de TI ([NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final)). La CISA publica paquetes de ejercicios de mesa listos para usar con escenarios de infraestructuras críticas ([CISA Tabletop Exercise Packages](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages)), y el NCSC británico ofrece «Exercise in a Box» ([NCSC, Exercise in a Box](https://www.ncsc.gov.uk/information/exercise-in-a-box)).

Un ejercicio de mesa es el primer paso adecuado: barato, seguro (nada toca un sistema en funcionamiento) y excelente para sacar a la luz lagunas en las funciones, la información y la comunicación.

### 11.2 Diseño

Un documento de diseño tiene siete partes:

1. **Objetivos**: de tres a cinco, cada uno **observable**: «En los 30 minutos siguientes a la inyección correspondiente, el equipo decide si suspende el acceso del proveedor, con responsable y justificación registrados». Evite «probar nuestra respuesta».
2. **Alcance y supuestos**: qué planes se ponen a prueba, qué equipos juegan, qué queda fuera del alcance («no se juega el proceso técnico forense»).
3. **Escenario**: verosímil, sintético, adecuado al sector, basado en información pública sobre amenazas a un nivel general; nunca en el error de un colega real.
4. **Inyecciones**: datos nuevos programados en el tiempo (una alarma, una llamada telefónica, un periodista, un plazo del regulador). Cada inyección se asocia al menos a un objetivo y tiene una decisión esperada.
5. **Funciones**: jugadores (deciden como lo harían en la realidad), facilitador (controla el reloj, presenta las inyecciones, mantiene viva la discusión), evaluadores (observan frente a los objetivos, llevan el registro de decisiones), secretario de actas y un **responsable de seguridad** o agente de confianza que puede pausar el ejercicio.
6. **Criterios de evaluación**: qué significa «cumplido», «cumplido en parte» y «no cumplido» para cada objetivo.
7. **Logística y reglas**: fecha, sala, ningún sistema real tocado, «ejercicio, ejercicio, ejercicio» en cada inyección escrita para que nada pueda confundirse con un evento real, y una frase de parada para el mundo real.

### 11.3 Facilitación

Empiece con las reglas básicas: esto pone a prueba los planes, no a las personas; no hay preguntas trampa; decidan como lo harían en la realidad; digan cuándo necesitarían información que no tienen. Mantenga el reloj con honestidad y resista la tentación de rescatar a los jugadores: si el equipo no tiene forma de contactar con el hospital, la laguna es el hallazgo. Registre las decisiones, no opiniones sobre el desempeño. En DRY CREEK, el facilitador no proporcionó el contacto del hospital que faltaba ni asignó la llamada cuando los jugadores dudaron; ese silencio produjo el hallazgo más claro del ejercicio.

### 11.4 Evaluación y mejora

Inmediatamente después: una **puesta en común en caliente**, en la que cada participante dice qué funcionó y qué no. En dos semanas: un **informe posterior a la acción** (AAR) que califica cada objetivo con evidencia del registro de decisiones, y un **plan de mejora** que convierte los hallazgos en acciones con responsable, fecha y verificación (capítulo 10). El AAR se comparte con el nivel de TLP adecuado; nombra lagunas de los planes y de las herramientas, no a personas. El informe de DRY CREEK calificó O3 como no cumplido y lo convirtió en una acción con un responsable, una fecha y una inyección de nueva prueba.

### 11.5 Ejemplo resuelto: el ejercicio «DRY CREEK» (sintético)

**Objetivos.** (O1) Declarar o descartar un incidente cibernético en los 15 minutos siguientes al primer indicador, con justificación. (O2) Decidir sobre la suspensión del acceso remoto de un proveedor en 30 minutos, sabiendo qué operaciones dependen de él. (O3) Informar al hospital dentro de las 2 horas de su acuerdo, con un único responsable principal con nombre. (O4) Cumplir el plazo ilustrativo de alerta temprana del regulador con un mensaje aprobado. (O5) Emitir una declaración provisional con un aprobador que rinda cuentas en los 45 minutos siguientes al contacto de los medios.

**Escenario.** Un viernes por la tarde se denuncia el robo del portátil de un ingeniero de HydroLogic; una hora después, el KVROC comunica una sesión remota a la estación KW-04 desde la cuenta de HydroLogic a una hora inusual, y un operador ve un cambio inesperado de la consigna de dosificación, que los límites del controlador rechazan. Todo sintético.

**Tabla de inyecciones (extracto).**

| Hora | Inyección | Objetivos | Decisión esperada |
|---|---|---|---|
| 00:00 | Llamada del KVROC: sesión inusual de un proveedor a KW-04 | O1 | Convocar al equipo de incidentes; registrar la hora de inicio |
| 00:10 | Operador: intento de cambio de consigna, rechazado por los límites | O1 | Declarar el incidente; evaluación de seguridad por operaciones |
| 00:20 | HydroLogic: robaron ayer el portátil del ingeniero | O2 | Suspender el acceso de HydroLogic; organizar un soporte alternativo para la dosificación |
| 00:40 | Instalaciones del hospital llama preguntando por rumores | O3 | El responsable principal con nombre informa al hospital; se fija la próxima actualización |
| 00:55 | Un periodista local llama a comunicación | O5 | Declaración provisional aprobada por el consejero delegado |
| 01:20 | Facilitador: «han pasado 20 horas desde la determinación» | O4 | Alerta temprana aprobada y enviada |

**Funciones.** Jugadores: E. Varga (dirección), A. Mensah, L. Ferreira, R. Adeyemi, el ingeniero de guardia y M. Holt, que se incorpora a las 00:55. Facilitadora: la coordinadora. Evaluadores: un auditor interno y una coordinadora homóloga de una empresa de servicios vecina, con un acuerdo de confidencialidad. Responsable de seguridad: el supervisor de turno, con la frase de parada «mundo real, mundo real».

**Evaluación (a partir del registro del evaluador, analizado con el método del Lab 10).** O1 cumplido (9 minutos, justificación registrada). O2 cumplido en parte: decisión a los 52 minutos porque nadie sabía quién más dependía del acceso de HydroLogic. O3 no cumplido: la llamada al hospital nunca se asignó. O4 cumplido. O5 cumplido en parte: declaración emitida tarde, sin responsable hasta que llegó el consejero delegado. Estos hallazgos alimentaron directamente las acciones correctivas del capítulo 10.

### 11.6 Rúbrica de diseño de ejercicios

| Criterio | 3 (excelente) | 1 (débil) |
|---|---|---|
| Objetivos | Observables, con plazo, vinculados a los planes | «Probar la respuesta» |
| Escenario | Verosímil, sintético, específico del sector, proporcionado | De Hollywood o basado en el error de un colega real |
| Inyecciones | Cada una asociada a objetivos con decisiones esperadas | Sorpresas aleatorias |
| Funciones y seguridad | Facilitador, evaluadores, responsable de seguridad, frase de parada; ningún sistema en funcionamiento | Los jugadores se evalúan a sí mismos; se tocan sistemas en funcionamiento |
| Evaluación | Criterios fijados de antemano; registro de decisiones; AAR y plan de mejora con responsables | Puesta en común basada en impresiones |
| Ética | Pone a prueba los planes, no a las personas; hallazgos anonimizados | Puntúa a individuos |

Use la rúbrica con el diseño de DRY CREEK: sus objetivos son observables y tienen plazo, y cada inyección se asocia a uno.

### 11.7 Actividad práctica (supervisada)

Diseñe un ejercicio de mesa de 90 minutos para un servicio esencial de su elección usando las siete partes de 11.2, con al menos cuatro objetivos y seis inyecciones. Pida a su supervisor o a un colega que lo puntúe con la rúbrica antes de conducirlo. Base el escenario en información pública sobre amenazas a un nivel general, como DRY CREEK usó un portátil robado de un proveedor y una sesión remota inusual, y nunca en el error de un colega real. Asocie cada inyección a un objetivo con una decisión esperada y nombre a un responsable de seguridad con una frase de parada. Marque cada inyección escrita como ejercicio. Tras la puntuación, revise el diseño y registre lo que cambió el revisor, para que el supervisor pueda ver cómo se aprovecharon los comentarios.

### 11.8 Errores comunes y límites

- Demasiados objetivos; nada se evalúa como es debido.
- Escenarios tan graves que todos los planes fallan y no se aprende nada concreto.
- Facilitadores que rescatan a los jugadores o dejan que dominen los cargos superiores.
- Inyecciones del ejercicio que podrían confundirse con mensajes reales.
- AAR que nunca se convierten en acciones.
- Un ejercicio de mesa muestra si los planes y las funciones tienen sentido; no muestra que los procedimientos puedan ejecutarse con rapidez; para eso hacen falta simulacros.

- Elegir evaluadores que también son jugadores, de modo que nadie observa las decisiones de forma independiente.
- Ignorar un comentario de la puesta en común como «dábamos por hecho que se encargaba comunicación», que en DRY CREEK apuntaba a la causa real.

### Ejercicios — capítulo 11

**EX051 — Haga observables los objetivos.** *Objetivo:* redactar objetivos evaluables. *Insumos:* «Probar nuestra comunicación», «Comprobar la gestión de proveedores», «Ver si la gente conoce el plan». *Pasos:* reescribir cada uno. *Evidencia esperada:* tres objetivos. *Rúbrica:* 3 = cada uno indica una decisión o acción, un plazo y lo que se registra; 2 = sin plazos; 1 = siguen siendo vagos; 0 = nada.

**EX052 — Redacte inyecciones.** *Objetivo:* asociar inyecciones a objetivos. *Insumos:* los objetivos de DRY CREEK. *Pasos:* redactar dos inyecciones nuevas que pongan a prueba O2 y O4 con más profundidad, con sus decisiones esperadas. *Evidencia esperada:* dos filas de inyecciones. *Rúbrica:* 3 = verosímiles, sintéticas, cada una asociada con una decisión esperada (por ejemplo, HydroLogic pide volver a conectarse para arreglar la dosificación; el oficial de guardia del regulador pide una actualización antes del plazo); marcadas como «ejercicio»; 2 = sin asociar; 1 = poco realistas; 0 = nada.

**EX053 — Puntúe un diseño.** *Objetivo:* aplicar la rúbrica. *Insumos:* el diseño de un colega: un único objetivo, «probar la respuesta a incidentes»; el escenario es un ataque de un Estado que provoca el fallo de una presa; el consejero delegado evalúa; las inyecciones se envían desde la cuenta de correo real del consejero delegado. *Pasos:* puntuar cada criterio y proponer correcciones. *Evidencia esperada:* puntuaciones y correcciones. *Rúbrica:* 3 = puntuaciones bajas en objetivos, proporción del escenario, funciones/independencia de la evaluación y seguridad (el correo real puede causar confusión); correcciones para cada uno; 2 = correcciones sin puntuaciones; 1 = lo acepta; 0 = nada.

**EX054 — Redacte el resumen del AAR.** *Objetivo:* evaluar frente a los objetivos. *Insumos:* la evaluación de DRY CREEK en 11.5. *Pasos:* redactar la tabla resumen del AAR con calificación, evidencia y acción recomendada por objetivo. *Evidencia esperada:* cinco filas. *Rúbrica:* 3 = calificaciones coherentes con la evidencia, acciones con responsable y verificables, nadie culpado individualmente; 2 = acciones vagas; 1 = narración; 0 = nada.

**EX055 — Un reto de facilitación.** *Objetivo:* gestionar un problema de facilitación. *Insumos:* en el ejercicio, el consejero delegado domina la sesión y lo decide todo, incluido el aislamiento técnico. *Pasos:* describir lo que hace el facilitador durante el ejercicio y después. *Evidencia esperada:* acciones. *Rúbrica:* 3 = durante: invitar por su nombre a los dueños de cada función, preguntar «¿quién decidiría esto en la realidad?», registrar; después: plantearlo en el AAR como un hallazgo de claridad del plan o de las funciones, informar al consejero delegado en privado y con respeto; 2 = solo después; 1 = lo ignora; 0 = nada.

### Síntesis del capítulo

Un ejercicio de mesa es el laboratorio del coordinador: seguro, barato y eficaz para sacar a la luz lagunas en las funciones, la información y la comunicación. Diséñelo con objetivos observables, un escenario sintético verosímil, inyecciones asociadas a los objetivos, evaluadores independientes y un responsable de seguridad. Condúzcalo para poner a prueba los planes, no a las personas; evalúelo con una puesta en común en caliente, un informe posterior a la acción y un plan de mejora cuyas acciones tengan responsable y se verifiquen.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Siga estudiando — capítulo 11 de 12

[← Capítulo 10](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Portafolio de práctica y revisión final

### Resultados de aprendizaje y conexión

Al terminar este capítulo debería ser capaz de:

- reunir un portafolio profesional que muestre, con evidencia, lo que sabe hacer como coordinador;
- informar a un consejo sobre la seguridad de las infraestructuras críticas en diez minutos, con decisiones solicitadas;
- redactar un plan realista de 90 días para un nuevo puesto de coordinación;
- evaluar su propio trabajo frente al resultado del curso e identificar lo que aún necesita aprender.

Este capítulo cierra el curso: reúne los productos de los capítulos 1–11 y comprueba si es capaz de **operar un flujo de trabajo repetible y comunicar los hallazgos**.

### 12.1 El portafolio

El portafolio de un coordinador no es un certificado; es un conjunto de productos de trabajo que otra persona podría comprobar. Constrúyalo a partir de los ejercicios que completó, depurados y marcados con claridad como trabajo del curso sobre datos sintéticos:

| Producto | Del capítulo | Qué muestra |
|---|---|---|
| Mapa de dependencias y de partes interesadas | 2 | Ve el servicio y a sus personas |
| Autorización y registro de decisión | 3 | Hace que el trabajo y las decisiones rindan cuentas |
| Extracto del registro de riesgos con la regla de clasificación | 4 | Sabe clasificar por consecuencia y mantener la higiene |
| Conjunto de métricas con umbrales | 5 | Mide lo que impulsa las decisiones |
| RACI corregida y tarjeta de escalado | 6 | Hace inequívocas las funciones |
| Fichas de control y plan de verificación | 7 | Conoce la diferencia entre declarado y probado |
| Sesión informativa del caso de acceso de proveedores | 8 | Sabe analizar y presentar un caso con equidad |
| Registro de notificaciones y declaración provisional | 9 | Sabe mirar hacia fuera con honestidad y a tiempo |
| Tabla de diagnóstico y registro de acciones | 10 | Mejora el programa, no solo informa de él |
| Diseño del ejercicio de mesa, AAR y plan de mejora | 11 | Sabe poner a prueba todo el sistema con seguridad |

Añada una **reflexión** de una página: qué haría de otra manera y un área sobre la que necesita aprender más (por ejemplo, los fundamentos técnicos de la TO del curso técnico, o las obligaciones legales de su jurisdicción).

### 12.2 La sesión informativa para el consejo

Los consejos de los operadores de servicios esenciales asumen cada vez más una responsabilidad explícita sobre la gestión de los riesgos de ciberseguridad (por ejemplo, los requisitos de la NIS2 sobre los órganos de dirección, [Directive (EU) 2022/2555, Article 20](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)). Una sesión informativa de diez minutos tiene cinco partes:

1. **Contexto**: el servicio, la consecuencia que importa y el panorama de amenazas al nivel de los avisos públicos.
2. **Dónde estamos**: los principales riesgos clasificados por consecuencia, con dueños y fechas; los niveles de aseguramiento de los controles clave.
3. **Qué aprendimos**: el último ejercicio o incidente, en dos o tres hallazgos.
4. **Qué estamos haciendo**: el plan, con el avance logrado.
5. **Qué necesitamos de ustedes**: decisiones: aceptaciones de riesgo, presupuesto, declaraciones de apetito, prioridades.

Evite la jerga, las puntuaciones únicas y el miedo. Los consejos actúan a partir de consecuencias claras, planes creíbles y peticiones concretas.

### 12.3 El plan de 90 días

Los primeros 90 días de un coordinador nuevo, destilados de este libro:

- **Días 1–30: escuchar y cartografiar.** Reunirse con todas las partes interesadas que «deciden» y que «deben ser informadas»; esbozar el mapa de dependencias; leer el registro de riesgos, el historial de incidentes y la lista de proveedores; registrar lo que se supone.
- **Días 31–60: resolver la titularidad.** Dueños para todos los riesgos de nivel 5; una RACI de incidentes; una tarjeta de escalado; un registro de notificaciones; una primera revisión del acceso de proveedores.
- **Días 61–90: probar e informar.** Un primer ejercicio de mesa sobre el escenario de alta consecuencia más probable; un AAR y un plan de mejora; una primera sesión informativa para el consejo con decisiones solicitadas.

Resista la tentación de empezar con un marco nuevo, una herramienta nueva o una política larga. Primero, la titularidad, la información y el ensayo.

### 12.4 Ejemplo resuelto: la sesión informativa al consejo de octubre (sintético)

La sesión informativa de diez minutos de la coordinadora ante la comisión de auditoría y riesgos de Kestrel Water, presidida por T. Lindqvist, en resumen:

1. *Contexto.* «Nuestro trabajo es el agua segura para 180.000 personas, entre ellas el Kestrel General Hospital. Los avisos públicos describen ataques a controladores de agua expuestos a internet ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)); lo hemos comprobado y no tenemos ninguno expuesto, confirmado en septiembre».
2. *Dónde estamos.* «Tres riesgos podrían afectar a la salud o al hospital; todos tienen ya dueño. La MFA de proveedores está implantada en cinco de seis proveedores y verificada mediante prueba en dos; la restauración del historiador se probó en agosto en 19 horas, frente a un objetivo de 24 horas».
3. *Qué aprendimos.* «El ejercicio DRY CREEK mostró que no sabíamos quién llama al hospital y que suspender a un proveedor es lento cuando no sabemos quién depende de él. Ambas cosas están corregidas; volveremos a probarlas en enero».
4. *Qué estamos haciendo.* «Cinco de las siete acciones del ejercicio están cerradas y verificadas; dos vencen en noviembre».
5. *Qué necesitamos.* «Primero, aceptar la excepción del controlador de KW-10 hasta marzo, con medidas compensatorias. Segundo, aprobar las cláusulas contractuales de proveedores para todas las renovaciones. Tercero, fijar una declaración de apetito: ningún riesgo de nivel 5 sin un tratamiento financiado durante más de 12 meses».

Cada cifra tiene una fuente en el portafolio. Nada es una puntuación única.

### 12.5 Revisión final

El resultado del curso le pide operar un flujo de trabajo repetible y comunicar los hallazgos. Compruébese frente al ciclo:

- **Enmarcar e identificar**: ¿sabe describir un servicio por su consecuencia y encontrar riesgos en la conversación?
- **Analizar y decidir**: ¿sabe escribir riesgos que alguien pueda asumir, clasificarlos de forma reproducible y registrar decisiones y aceptaciones?
- **Organizar**: ¿sabe asignar funciones, gobernar los cambios y escalar?
- **Verificar**: ¿sabe distinguir lo declarado de lo probado y diseñar comprobaciones proporcionadas?
- **Comunicar**: ¿sabe cumplir los relojes e informar con honestidad a los clientes, al público y al consejo?
- **Mejorar**: ¿sabe poner a prueba con un ejercicio y cerrar acciones con evidencia?

Cuando la respuesta sea «todavía no», el número de capítulo le indica adónde volver.

### 12.6 Actividad práctica

Reúna su portafolio a partir de sus respuestas a los ejercicios. Pida a un colega que lo revise frente a la rúbrica final (EX060) y que intente verificar tres afirmaciones solo a partir de su evidencia. Elija afirmaciones que importen, como «MFA de proveedores verificada mediante prueba en dos proveedores» o «historiador restaurado en 19 horas», y compruebe si su colega puede encontrar, solo con el portafolio, el registro, la fecha y el responsable que hay detrás de cada una. Cuando no pueda, corrija la evidencia, no la redacción. Marque cada elemento con claridad como trabajo del curso sobre datos sintéticos y elimine todo lo que pudiera identificar a una organización o a una persona reales antes de compartirlo.

### 12.7 Errores comunes y límites

- Portafolios de certificados en lugar de productos de trabajo.
- Sesiones informativas para el consejo sin peticiones.
- Planes de 90 días que empiezan por las herramientas.
- Presentar el trabajo sintético del curso como hallazgos reales de una organización.
- Este curso no le convierte en especialista técnico en TO ni en abogado; sepa cuándo llamar a uno.

- Comunicar una afirmación al consejo sin una fuente en el portafolio, de modo que nadie pueda comprobarla después.
- Pedir una decisión al consejo sin decir qué ocurre si la rechaza, como cuánto tiempo seguiría vigente, en caso contrario, la excepción de KW-10.
- Actualizar el portafolio una vez y dejar que se quede obsoleto cuando termina el curso.

### Ejercicios — capítulo 12

**EX056 — Índice del portafolio.** *Objetivo:* reunir la evidencia. *Insumos:* sus respuestas a los ejercicios. *Pasos:* elaborar el índice del portafolio con el producto, el capítulo y la afirmación que respalda cada uno. *Evidencia esperada:* índice de al menos ocho productos. *Rúbrica:* 3 = cada producto vinculado a una afirmación y a un ejercicio concretos, depurado y etiquetado como sintético; 2 = índice sin afirmaciones; 1 = lista de capítulos; 0 = nada.

**EX057 — Sesión informativa para el consejo.** *Objetivo:* comunicar a los órganos de gobierno. *Insumos:* 12.2 y su portafolio. *Pasos:* redactar el guion de la sesión informativa (máximo 600 palabras). *Evidencia esperada:* el guion. *Rúbrica:* 3 = cinco partes, consecuencias en lenguaje llano, cifras con fuente, niveles de aseguramiento indicados, tres peticiones concretas; ninguna puntuación única; 2 = sin peticiones; 1 = informe técnico; 0 = nada.

**EX058 — Plan de 90 días.** *Objetivo:* planificar un puesto. *Insumos:* un nuevo puesto de coordinador en una red hospitalaria regional. *Pasos:* redactar el plan de 90 días con tres fases y entregables. *Evidencia esperada:* el plan. *Rúbrica:* 3 = se adapta a la sanidad (la dirección clínica como responsable de las decisiones, los dispositivos médicos, la seguridad del paciente, las dependencias internas críticas), la titularidad antes que las herramientas, ejercicio e informe al consejo antes del día 90; 2 = genérico; 1 = empieza por las herramientas; 0 = nada.

**EX059 — Verifique una afirmación.** *Objetivo:* poner a prueba la evidencia. *Insumos:* la afirmación «la restauración del historiador se probó en agosto en 19 horas». *Pasos:* enumerar la evidencia que esperaría encontrar en el portafolio para respaldarla y dos preguntas que haría un auditor escéptico. *Evidencia esperada:* lista y preguntas. *Rúbrica:* 3 = plan de prueba, autorización, registro cronometrado, registro del resultado, comprobación de la integridad de los datos; preguntas sobre el alcance (restauración completa o parcial) y el entorno (aislado o similar a producción); 2 = solo la evidencia; 1 = «confiar en el ingeniero»; 0 = nada.

**EX060 — Autoevaluación.** *Objetivo:* reflexionar frente al resultado del curso. *Insumos:* 12.5. *Pasos:* puntuarse de 0 a 3 en las seis áreas del ciclo, con evidencia para cada una, y un plan de aprendizaje para las dos más bajas. *Evidencia esperada:* seis puntuaciones y un plan. *Rúbrica:* 3 = puntuaciones honestas, cada una respaldada por un producto del portafolio, plan de aprendizaje concreto con recursos y fechas; 2 = puntuaciones sin evidencia; 1 = todo 3; 0 = nada.

### Síntesis del capítulo

Un coordinador profesional demuestra su competencia mediante productos de trabajo comprobables: mapas, registros, RACI, fichas de control, sesiones informativas de casos, registros de notificaciones, informes de ejercicios y planes de mejora. Informe a los consejos con consecuencias, evidencia y peticiones concretas; empiece un puesto nuevo con titularidad, información y ensayo; y evalúese con honestidad frente al ciclo completo: enmarcar, decidir, organizar, verificar, comunicar, mejorar.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Siga estudiando — capítulo 12 de 12

[← Capítulo 11](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Siguiente curso desde el índice de capítulos →](../SUBJECTS.md)

Este es el último capítulo de este curso; el índice enlaza con el siguiente curso del itinerario completo de estudio.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resultados resueltos y notas de evaluación

Estas son respuestas modelo. Una respuesta distinta que cumpla el nivel de exigencia de la rúbrica en cuanto a evidencia y honestidad sobre los límites obtiene la máxima puntuación. Todas las organizaciones, personas y datos son sintéticos.

### Capítulo 1

**EX001.** (1) «Como los ordenadores de oficina y los de la sala de control comparten red y servicios de escritorio remoto sin parchear, un ransomware que entre mediante phishing podría cifrar las estaciones de trabajo de los operadores en KW-TW, obligando a operar el tratamiento en manual durante días y poniendo en riesgo el suministro a 180.000 personas». (2) «Como los PC de la sala de control usan un sistema operativo sin soporte para el que no se publican correcciones, un fallo conocido podría usarse para inutilizar las pantallas del operador, causando la pérdida de visión de la dosificación y la presión hasta que se instalen equipos de sustitución». (3) «Como la cuenta remota de un proveedor de bombas no tiene segundo factor, cualquiera con su contraseña podría iniciar sesión en los controladores de las estaciones y cambiar las consignas de las bombas, causando pérdida de presión a hasta 20.000 clientes, entre ellos el hospital». Cada una nombra causa, evento y consecuencia en personas o en tiempo.

**EX002.** (c) primero: un cambio de cloro no aprobado amenaza directamente la salud. (b) segundo: 40 minutos sin visión significan que los operadores no pueden ver ni corregir el proceso, y puede indicar una interferencia. (d) tercero: el diagrama ayuda a un atacante a planificar y debe recuperarse y evaluarse. (a) cuarto por consecuencia operativa, pero puede acarrear obligaciones de notificación sobre datos personales con plazos cortos, así que puede ser el primero en **urgencia de actuación** para el equipo jurídico. Clasificar por consecuencia no significa ignorar las obligaciones.

**EX003.** A TI: «Gracias. No puedo dar el visto bueno yo sola, porque se ejecuta en las estaciones de trabajo de los operadores y podría afectar al sistema de control. La decisión corresponde a A. Mensah como dueño. ¿Podrían preguntar al proveedor del sistema de control si el producto está admitido y proponer una prueba en una máquina que no sea de producción, con un plan de reversión? Reservaré 30 minutos con Operaciones el martes que viene». A A. Mensah: un resumen, la petición y la fecha propuesta. La máxima puntuación exige no dar el visto bueno en solitario y nombrar a un dueño.

**EX004.** Antivirus: Proteger (seguridad de la plataforma) y Gobernar (quién decide sobre los cambios en los sistemas de operación). Puntuación de riesgo: Gobernar (estrategia de gestión de riesgos, supervisión). Conexiones del proveedor: Gobernar (gestión del riesgo de la cadena de suministro), Identificar (activos y riesgo), Proteger (identidad y acceso). Una etiqueta muestra dónde se sitúa el tema, no si algo funciona.

**EX005.** Riesgo: «Como la puerta de la estación se deja calzada abierta por la noche, una persona no autorizada podría entrar en KW-03 y manipular los equipos de control, causando una operación insegura o la pérdida del suministro». Dueño: jefe de operaciones (o responsable de la estación). Pregunta: «¿Cuánto tarda el lector y la puerta también se usa como salida de emergencia o para entregas por la noche?»; la solución puede ser un lector más rápido, no una reprimenda.

### Capítulo 2

**EX006.** Regulador: debe ser informado; puede ayudar (orientaciones). KVROC: ejecuta (supervisión); puede ayudar; dependencia compartida. HydroLogic: ejecuta; dependencia aguas arriba; debe ser informada de los incidentes pertinentes según el contrato. Escuela: se ve afectada; posiblemente debe ser informada si acoge a personas vulnerables (política local). Consejero delegado: decide. Sala de control de Kestrel Grid: dependencia aguas arriba; puede ayudar (prioridades de restablecimiento); debe ser informada cuando se planifiquen grandes cambios de carga.

**EX007.** Operador de telecomunicaciones: perderlo elimina a la vez la telemetría de las doce estaciones y los operadores pierden la visión en todas partes; pregunta: ¿hay una segunda ruta o un plan de lectura manual? KVROC: una interrupción o un compromiso afecta a tres empresas y reduce la detección; pregunta: ¿qué ocurre con la supervisión si el KVROC no está disponible y quién más depende de él? Ingeniero de HydroLogic: riesgo de persona clave; una enfermedad o una baja deja a nadie capaz de reparar las estaciones; pregunta: ¿está documentado el conocimiento y hay un segundo ingeniero? La pregunta común: «¿Qué más usa eso?».

**EX008.** «De Kestrel Water a Instalaciones del Hospital: desde las 10:00 de hoy y durante unas seis horas operamos en control manual, por precaución, la estación de bombeo que abastece a su centro. El agua sigue siendo apta para beber. La presión puede ser algo más baja; no prevemos una interrupción. Por si acaso, asegúrense de tener listo su plan de agua almacenada. Próxima actualización a las 12:00 o antes si algo cambia. Contacto: coordinador de guardia, [número 24 h]». (Menos de 80 palabras, sin detalles técnicos).

**EX009.** Pedir al responsable de instalaciones la sección correspondiente del plan de continuidad del hospital o una reunión breve; registrar la fecha y la fuente; cambiar la entrada de «supuesto» a «verificado (fuente, fecha)». Si la cifra real es de 2 horas, prometer una llamada «en 2 horas» no deja tiempo para actuar: renegociar una notificación mucho más corta (por ejemplo, 30 minutos), planificar con el hospital un suministro alternativo (camiones cisterna, válvulas prioritarias) y dar de alta un riesgo de nivel 5 para la dependencia.

**EX010.** Empresa de agua: si la facturación, la programación o la supervisión remota están cifradas, los responsables pueden parar o restringir la operación automatizada por precaución ante la propagación y porque no pueden ver ni cobrar el servicio; la operación puede continuar en manual. Oleoducto de combustible: el aviso AA21-131A de la CISA describe el ransomware DarkSide dirigido contra la red de TI de una empresa de infraestructura crítica e insta a adoptar medidas para evitar la interrupción del negocio; las operaciones pueden detenerse cuando los sistemas de negocio necesarios para gestionarlas no están disponibles o cuando el operador opta por la cautela. La máxima puntuación evita afirmar que se comprometieron los sistemas de control y se mantiene al nivel del aviso.

### Capítulo 3

**EX011.** Faltan: la finalidad; los sistemas exactos y las exclusiones; las actividades permitidas y prohibidas; los evaluadores y el supervisor con nombre; la ventana con zona horaria; las condiciones de parada; el tratamiento de los datos; la autoridad escrita (un chat no es un registro; ¿quién refrenda en Northgate?). Reescritura: «Finalidad: evaluar la exposición de la red de supervisión desde la red de oficina. Dentro del alcance: el cortafuegos entre las zonas de oficina y de supervisión, y los dos servidores de supervisión de KW-TW. Fuera del alcance: los controladores de las estaciones, el sistema de dosificación y los enclavamientos de seguridad. Permitido: revisión de la configuración y revisión pasiva del tráfico desde un puerto espejo aprobado; prohibido: escaneo activo de los controladores, explotación, cualquier escritura. Personas: S. Brandt (Northgate), supervisado por J. Tan. Ventana: 9 de junio de 2026, de 09:00 a 15:00, hora local. Parada: cualquier alarma, pérdida de visión o petición del operador. Datos: informe TLP:AMBER+STRICT mediante transferencia segura; notas de trabajo borradas en un plazo de 14 días. Autoridad: A. Mensah (firmado), responsable de servicio de Northgate (refrendado)».

**EX012.** Decisión: mantener KW-05 en automático. Por: el responsable de turno, conforme al procedimiento de incidentes de operaciones, 02:10 hora local. Opciones: (a) operación manual, con 90 minutos de espera para llamar al personal y riesgo de errores de manejo de noche; (b) seguir en automático con vigilancia, la elegida. Conocido: un inicio de sesión remoto sin explicar a las 01:52; valores de dosificación normales; límites activos. Desconocido: si el inicio de sesión era malicioso; si la cuenta se usó indebidamente en otro lugar. Condiciones: el operador vigila la dosificación y la presión cada 15 minutos; pasar a manual ante cualquier cambio inesperado; revisar a las 06:00 con la responsable de seguridad. Informados: responsable de seguridad, responsable del incidente, jefe de operaciones (mensaje de las 02:15).

**EX013.** (a) TLP:GREEN: el sector se beneficia y la información no es específica de la empresa. (b) TLP:AMBER+STRICT (o RED si solo la necesitan analistas del KVROC con nombre): revela las debilidades de la empresa. (c) TLP:CLEAR: destinada al público.

**EX014.** Una biblioteca de registros con control de acceso y carpetas por tipo de registro: autorizaciones y registros de decisión (responsable: la coordinadora); aceptaciones de riesgo y excepciones (responsable: la coordinadora; decisiones de autoridades con nombre, enlazadas desde las actas del consejo); informes de ejercicios (responsable: la coordinadora); listas de acceso de proveedores (responsable: el jefe de operaciones; exportadas desde la pasarela, nunca enviadas por correo). Historial de versiones activado, conservación según la política, acceso revisado dos veces al año.

**EX015.** Parar si: cualquier alarma inesperada en KW-09 o en sus vecinas; cualquier pérdida de visión en las pantallas del operador; la actualización se prolonga más allá de las 15:00; el controlador no vuelve a su estado esperado en el tiempo previsto; el operador de turno lo pide. El operador de turno y el jefe de operaciones pueden detener el trabajo en cualquier momento sin justificarlo; el proveedor debe parar y dejar el sistema en el estado seguro acordado.

### Capítulo 4

**EX016.** 5: ha ocurrido aquí en los últimos 12 meses o se está intentando activamente ahora contra operadores similares (aviso público). 4: ha ocurrido en el sector en los últimos 2 años y las condiciones están presentes aquí. 3: ha ocurrido en el sector; aquí necesitaría una condición más. 2: conocido en otros sectores; necesitaría varias condiciones. 1: sin casos conocidos; necesitaría varias condiciones improbables. Las valoraciones tienen en cuenta los controles que existen y están verificados (capítulo 7).

**EX017.** R03 tiene la segunda puntuación empatada (15), pero consecuencia 3 sobre la facturación (peso del servicio 1), así que cae al sexto puesto con la regla de primero la consecuencia. La puntuación de R05 es 10, pero la consecuencia 5 sobre el agua potable lo eleva al tercer puesto. Acciones de gobernanza: R02, asignar dueño (A. Mensah, dueño de la dosificación), fijar una nueva fecha de tratamiento y revisarlo ya; R04, prueba de restauración vencida (la ejecuta J. Tan, con A. Mensah como dueño del servicio); R07, revisión obsoleta (la coordinadora, como enlace con el hospital, o L. Ferreira como dueña registrada, la revisa con el hospital).

**EX018.** «Riesgo R10: como los controladores de la estación KW-10 no tienen soporte y no pueden corregirse, una debilidad conocida podría usarse para detener el bombeo, causando la pérdida del suministro a unas 8.000 personas. Aceptado por: el consejero delegado, M. Holt, en nombre del consejo, el 14 de octubre de 2026. Medidas compensatorias: ningún acceso remoto a KW-10; supervisión de la red de la estación por el KVROC; control de acceso físico; controladores de repuesto en almacén; procedimiento de operación manual ensayado. Decae si: un aviso público muestra explotación activa, se produce un incidente en KW-10 o falla una medida compensatoria. Caducidad: 31 de marzo de 2027. Responsable de la revisión: A. Mensah; seguimiento por la coordinadora».

**EX019.** Añadir un octavo campo `acceptance_expiry` (None donde no hay aceptación), por ejemplo R05 "2026-02-28" (caducada) y R06 "2026-12-31" (válida). Regla: `if exp and dt.date.fromisoformat(exp) < TODAY: flags.append("ACCEPTANCE EXPIRED")`. La salida muestra ahora R05 con «ACCEPTANCE EXPIRED» y R06 sin él, y «Needs governance action» pasa a ser R02, R04, R05, R07. La máxima puntuación muestra ambos casos.

**EX020.** Resumen: «Nuestra regla de clasificación pone primero todo lo que pueda afectar a la salud o al hospital y después usa la probabilidad. Principales riesgos: (1) acceso remoto de proveedores sin MFA; dueño A. Mensah, corrección antes del 30 de abril; (2) solo un ingeniero entiende la lógica de dosificación; ahora mismo sin dueño; pedimos a la comisión que confirme a A. Mensah como dueño y financie la documentación y un segundo ingeniero antes de septiembre; (3) pérdida del suministro eléctrico en KW-07; estudio del generador de reserva previsto para septiembre. Acciones de gobernanza: la prueba de restauración del historiador está vencida (ahora programada para abril) y la revisión del riesgo de suministro al hospital está obsoleta (reunión fijada en marzo). Límites: las valoraciones de probabilidad son juicios de expertos; la clasificación es reproducible a partir de la regla adjunta». Ninguna puntuación única.

### Capítulo 5

**EX021.** Primero los requisitos regulatorios (son obligatorios). Usar el CSF 2.0 como estructura del programa y para informar al consejo, porque se basa en resultados e incluye Gobernar. Usar los CPG como línea base priorizada asociada a las funciones del CSF, para encontrar rápido las lagunas de alto impacto. Usar la ISA/IEC 62443 para las compras de TO y los requisitos de proveedores (requisitos para proveedores de servicios y de productos), referenciada desde los resultados de cadena de suministro de Gobernar.

**EX022.** Alcance: ¿los mismos sistemas e instalaciones que la evaluación de 2,6? Evaluador y método: ¿autoevaluación, par o independiente; entrevista o evidencia? Definición: ¿qué significa el nivel 3 y ha cambiado? Fecha: ¿antes o después del cambio de contrato con el KVROC? Decisión: ¿qué haremos de otra manera por el 3,1? Creíble si el alcance y el método son los mismos, si se basa en evidencia o es independiente, y si se vincula a un resultado observado, como que el KVROC detecte las inyecciones del ejercicio dentro del tiempo objetivo.

**EX023.** (1) % de riesgos de nivel 5 con dueño y tratamiento en plazo; responsable: la coordinadora; < 100% → escalado a la dirección. (2) Mediana de días laborables entre el fin del contrato de un proveedor o la salida de un empleado y la eliminación de la cuenta; responsable: el jefe de operaciones; > 5 → revisión del proceso de acceso. (3) Número de interfaces operativas accesibles desde internet; responsable: la responsable de seguridad; > 0 → notificación inmediata al dueño y corrección. (4) % de responsables de guardia que han participado en un ejercicio en 12 meses; responsable: la coordinadora; < 80% → programar un ejercicio.

**EX024.** «Gracias; esto podría ser urgente. ¿A qué instalación y función sirve hmi-02? ¿La conexión tuvo éxito o solo se intentó, y cuál es el origen y la evidencia (extracto del registro con horas UTC)? ¿Sigue siendo accesible ahora? El bloqueo puede cortar el acceso legítimo de un proveedor: ¿quién usa esa ruta? Llamo ahora a A. Mensah como dueño; por favor, quédense preparados para bloquear con su aprobación y trátenlo por la vía de escalado de incidentes hasta que sepamos más».

**EX025.** «Evaluamos la TI de oficina y la planta de tratamiento frente a una línea base nacional; la mayoría de las prácticas existen sobre el papel. Las doce estaciones de bombeo no se incluyeron, y dos prácticas que son las que más importan para ellas (la autenticación robusta para el acceso de proveedores y la eliminación rápida de cuentas) no están verificadas. Revisaremos el acceso de proveedores en mayo y repetiremos la evaluación, incluidas las estaciones, antes de septiembre».

### Capítulo 6

**EX026.** Añadir una séptima función, «Shift supervisor» (supervisor de turno), y corregir las filas (Coordinator, Ops manager, Security lead, Comms, Vendor, CEO, Shift supervisor): pasar las estaciones a operación manual, `I A - - - I R`; informar al hospital, `R C I C - A -` (la coordinadora es la única responsable principal y comunicación se consulta sobre la redacción); aprobar la sesión remota del proveedor, `C A R - I - I` (el jefe de operaciones es la única A, la responsable de seguridad comprueba la solicitud y al proveedor solo se le informa); declaración pública, `C C C R - A -`; las demás filas reciben `I`, `C` o `-` para el supervisor de turno. Al volver a ejecutar el Lab 6 con estas filas se imprime «0 issues in 7 activities» y la línea de carga `Coordinator=3, Ops manager=4, Security lead=2, Comms=1, Vendor=0, CEO=3, Shift supervisor=1`. El jefe de operaciones sigue acumulando cuatro entradas R/A, de lo que se ocupa EX029.

**EX027.** (a) Normal: nueva ruta de acceso relevante para la seguridad; aprobación del dueño, revisión de la regla y caducidad. (b) Estándar, si existe un procedimiento preaprobado para sustituir baterías; si no, normal. (c) De emergencia: aprobado por el responsable del incidente, registrado en las 24 horas siguientes y revisado después. (d) Normal: comprobación de compatibilidad del proveedor, prueba, plan de reversión.

**EX028.** Tarjeta: «Sospecha de evento cibernético; llame si: las pantallas muestran cambios que nadie hizo; hay inicios de sesión o mensajes inesperados; los controles no responden; llama el KVROC. 1) Mantenga seguro el proceso: siga los procedimientos normales de operación; pase a manual solo cuando los procedimientos lo permitan. 2) No apague ni reinicie los ordenadores salvo que se le indique. 3) Anote las horas y lo que vio. 4) Llame al responsable del incidente de guardia [número]; sin respuesta en 10 minutos → suplente [número]; después, jefe de operaciones [número]. 5) Peligro inmediato para las personas o para la calidad del agua → directamente al jefe de operaciones y procedimientos de emergencia».

**EX029.** Mantener en el jefe de operaciones las decisiones de seguridad de las personas (operación manual, aislamientos que afecten al proceso). Durante los incidentes, delegar la aprobación de las sesiones de proveedores en un suplente de operaciones con nombre o en el responsable del incidente, con operaciones consultado; traspasar el enlace con el hospital a la coordinadora; asegurar que haya un jefe de operaciones suplente de guardia para que la planta tenga siempre a alguien centrado en ella.

**EX030.** Enumerar los cambios de emergencia a partir del registro del incidente; para cada uno, decidir mantener, modificar o revertir, con un responsable: la regla de «bloquear todo acceso de proveedores» pasa a ser un cambio normal, y el acceso se restablece proveedor a proveedor mediante el proceso normal de aprobación una vez terminada la revisión; eliminar la cuenta temporal de administrador local y verificar su eliminación; actualizar los diagramas y los registros; registrar la revisión como un registro de decisión.

### Capítulo 7

**EX031.** Objetivo: impide el uso de cuentas de proveedores por personas que ya no están bajo contrato (riesgo R01 y riesgos por salida de personal del proveedor). Dueño: el jefe de operaciones (como dueño del contrato y de las estaciones). Funcionamiento: cuando termina un contrato o el proveedor notifica la salida de un empleado, la cuenta se desactiva en 5 días laborables; cada mes, la coordinadora concilia las cuentas de la pasarela con el registro de contratos. Evidencia: registro de conciliación y exportación de la pasarela, guardados en la biblioteca de registros. Señal de fallo: cualquier cuenta cuyo contrato haya terminado o cuya persona nombrada se haya marchado.

**EX032.** MFA de proveedores: probado (protege frente a consecuencias de nivel 5; un inicio de sesión supervisado solo con contraseña es rechazado). Procedimiento de operación manual: probado mediante simulacros o ejercicios (es la alternativa de seguridad). Política de contraseñas de los portátiles de oficina: observado (exportación de la configuración); consecuencia de nivel 3. Tarjetas de visitante de la sede central: documentado u observado; menor consecuencia para el servicio.

**EX033.** Restaurar la última copia de seguridad del historiador en un entorno aislado (no en producción), con autorización de A. Mensah y ejecutada por J. Tan. Poner en marcha un cronómetro en el momento de la decisión de restaurar; éxito si el historiador es utilizable en 24 horas y los datos de un periodo elegido de 7 días están completos frente a una referencia conocida. Registrar horas, pasos, problemas y resultado en un informe de prueba; archivarlo y actualizar el nivel de aseguramiento del control C2 a «probado», con la fecha.

**EX034.** «Excepción E-07: el control "MFA para el acceso de ingeniería" no se aplica a la interfaz local de ingeniería de KW-10. Motivo: el firmware del controlador no lo admite; sustitución prevista. Compensación: ninguna ruta remota a KW-10; armario cerrado con llaves registradas; sumas de comprobación de la configuración comparadas cada semana; alertas del KVROC ante cualquier sesión de ingeniería. Aceptada por: el director de operaciones, E. Varga (consecuencia 4), el 1 de octubre de 2026. Caducidad: 31 de marzo de 2027. Plan de eliminación: sustitución del controlador en el programa de inversiones de 2027; dueño, A. Mensah».

**EX035.** C1 MFA de proveedores: observado en 5 de 6 cuentas; la laguna de ScadaCo se corregirá antes del 3 de junio (A. Mensah). C2 restauración del historiador: copias observadas cada noche, pero la restauración nunca se ha probado; prueba programada en 60 días (J. Tan). C3 límites de dosificación: probado en un controlador de repuesto el 3 de febrero y producción coincidente por suma de comprobación; nueva comprobación tras cualquier cambio de lógica (J. Tan).

### Capítulo 8

**EX036.** `v-hydro1`: sin hallazgo; se mantiene. `v-hydro2`: cuenta sin nombre, acciones no atribuibles; sustituirla por una cuenta nominativa en 14 días, con sesiones supervisadas mientras tanto (A. Mensah). `v-scadaco`: sin MFA, basta la contraseña para acceder; ScadaCo debe activarla en 30 días o se registra una excepción con medidas compensatorias; mantener una alternativa supervisada para el soporte urgente (A. Mensah). `v-pumps`: contrato terminado; desactivarla ya y confirmarlo con Vale Pumps. `v-meter`: sin uso > 90 días; desactivarla; reactivarla a petición. `v-integr`: 19 frente a ~4 sesiones; preguntar a J. Tan y a Northgate; un proyecto explica 17; escalar las dos sesiones nocturnas sin explicar a la responsable de seguridad. Ninguna acusación.

**EX037.** Añadir un campo `staff_confirmed` (fecha en que el proveedor confirmó por última vez su lista de personas con acceso), por ejemplo "2026-04-01" para HydroLogic y "2025-09-15" para Northgate. Regla: `if (TODAY - dt.date.fromisoformat(conf)).days > 180: f.append("staff list unconfirmed >180 days")`. La salida muestra entonces el indicador en `v-integr` y no en `v-hydro1`. Importa porque las salidas de personal de los proveedores son una vía habitual por la que credenciales válidas sobreviven a sus dueños.

**EX038.** (1) Solo pueden acceder las personas con nombre que figuran en el anexo A; los cambios se notifican por escrito antes del acceso (verificado en cada revisión trimestral). (2) Toda sesión remota usa la pasarela de la empresa con autenticación multifactor (verificado a partir de la configuración y los registros de la pasarela). (3) El proveedor notifica a la empresa en 24 horas cuando una persona de la lista se marcha o pierde un dispositivo usado para el acceso (verificado mediante la confirmación trimestral de la lista de personal). (4) El proveedor entrega los registros de trabajo de cualquier sesión en los 2 días laborables siguientes a la solicitud (verificado por muestreo). (5) Al terminar el contrato, el proveedor confirma por escrito en 14 días que se han borrado los datos de la empresa (verificado mediante el registro en la biblioteca).

**EX039.** «TLP:AMBER+STRICT. L.: la revisión del acceso de proveedores encontró 19 sesiones de Northgate en 90 días. J. Tan y el registro de trabajo de Northgate explican 17 (puesta en servicio de la telemetría de KW-11, aprobada en marzo). Dos siguen sin explicar: el 12 y el 19 de abril, ambas iniciadas a las 02:00 hora local (01:00 UTC); origen y destino en la exportación de la pasarela adjunta. Desconocido: quién se conectó y qué se hizo. Te pido que revises los registros de sesiones por la vía de escalado de incidentes y me indiques si conviene restringir la cuenta. Por favor, no contactes con Northgate hasta que lo hayas decidido. Vuelvo a consultarte a las 16:00».

**EX040.** (1) Revisado: las seis cuentas de proveedores de la pasarela de acceso remoto, 4 de mayo, exportación de solo lectura autorizada por A. Mensah. (2) Hallazgos: una cuenta sin nombre, una sin MFA, una de un contrato terminado, una sin uso, una con un volumen inusual (evidencia adjunta). (3) Decidido por A. Mensah: dos cuentas desactivadas; sustitución nominativa en 14 días. (4) Se le solicita: aprobar cláusulas contractuales estándar para las renovaciones; aprobar presupuesto para la MFA de ScadaCo si no pueden financiarla; confirmar revisiones mensuales. (5) Abierto: dos sesiones nocturnas de Northgate sin explicar, en manos de la responsable de seguridad, actualización el viernes; supuesto de que la pasarela es la única ruta de acceso, comparación con el cortafuegos antes de junio (J. Tan).

### Capítulo 9

**EX041.** Llamada al hospital: vencía el sábado a las 23:40Z, se hizo a las 23:55Z, 0,25 h tarde; causa: dos personas creían que llamaría la otra (responsabilidad duplicada). Alerta temprana: vencía el domingo a las 21:40Z, se envió a las 18:05Z, 3,58 h de antelación; la plantilla funcionó. Aseguradora: vencía el lunes a las 21:40Z; vencida, no enviada; causa: la obligación no figuraba en el registro. Notificación del incidente: vencía el martes a las 21:40Z, se envió a las 22:30Z, 0,83 h tarde; causa: la aprobación se pidió 40 minutos antes del plazo. Informe final: abierto, quedan 646,7 h. Todas las causas son lagunas de proceso.

**EX042.** «Kestrel Water está investigando un acceso no autorizado a sistemas informáticos que nos ayudan a supervisar el tratamiento del agua. Como precaución, nuestros operadores gestionan en manual dos estaciones de bombeo. Los análisis de calidad del agua son normales y el agua del grifo sigue siendo apta para beber. No necesita hacer nada. Trabajamos con las autoridades competentes y actualizaremos esta página y nuestras redes sociales antes de las 18:00 de hoy, o antes si algo cambia».

**EX043.** «Le habla [nombre], coordinadora de guardia de Kestrel Water. Mañana, entre las 09:00 y las 13:00, conmutaremos de forma controlada las estaciones que abastecen a su centro. El agua sigue siendo apta para beber. La presión puede bajar en la zona este hasta cuatro horas; el suministro no debería interrumpirse. Por favor, revisen sus disposiciones de agua almacenada para los servicios de esterilización y la diálisis. ¿Hay algo en su centro que necesite presión plena en esa franja, o un horario que les vendría peor? Volveré a llamar mañana a las 08:00 para confirmarlo; nuestro número 24 horas es [número]».

**EX044.** «Estamos investigando con las autoridades competentes y no sería correcto especular sobre la causa ni sobre ninguna persona o empresa mientras continúa ese trabajo. Compartiremos lo que podamos cuando podamos confirmarlo». Razonamiento: la información no está confirmada (veracidad); nombrar a un proveedor o a una persona podría perjudicarles injustamente y puede ser erróneo (equidad); nos comprometemos a actualizar (corrección y transparencia).

**EX045.** Plazos internos: llamada al hospital, la responsable (la coordinadora) llama en los 60 minutos siguientes al inicio del reloj; alerta temprana, borrador a las 12 h y aprobación solicitada antes de las 18 h; notificación del incidente, borrador a las 48 h y aprobación solicitada antes de las 60 h; aseguradora, añadida al registro y avisada junto con la alerta temprana. Delegación: si el consejero delegado no está disponible, aprueba el director de operaciones (COO) y, después, el director del área de operaciones. Plantillas preparadas para cada caso. El responsable del incidente registra el inicio del reloj en UTC en el registro de decisiones.

### Capítulo 10

**EX046.** El «3/6» cuenta I3 como un éxito aunque no se registró ninguna justificación para una decisión de seguridad de las personas, y trata I5 (un cliente crítico al que nunca se informó) como un fallo más entre seis. I4 no tenía responsable. El defecto más grave es I5: en un incidente real, no se habría avisado al hospital (o I3, si se argumenta que las decisiones de seguridad no registradas son peores; se exige razonamiento).

**EX047.** Añadir las columnas `safety` (yes para I2 e I3) y `consulted` (por ejemplo, I3 "Security lead", I2 "Coordinator") y la regla `if r["safety"] == "yes" and r["owner"] != "Ops manager" and "Ops manager" not in r["consulted"]: f.append("operations not consulted")`. Con las seis filas originales, el nuevo indicador nunca salta: I2 e I3 tienen como responsable al jefe de operaciones, así que la autoridad sobre la seguridad estaba donde debía. La fila inventada `95,I7 station alarm,isolate KW-09 network,Security lead,15,12,yes,yes,Coordinator` aparece señalada con «operations not consulted». Explicar por qué I3 no se señala, correctamente, obtiene la máxima puntuación; forzar un indicador sobre I3 no.

**EX048.** Síntoma: declaración provisional 11 minutos tarde y sin responsable. Hipótesis: (1) ningún aprobador que rinda cuentas; (2) ninguna plantilla; (3) el responsable de comunicación no sabía qué podía decirse. Evidencia: la RACI del capítulo 6 no tenía A para la declaración pública; en la puesta en común se dijo «esperando a alguien con rango». Causa: laguna de titularidad. Corrección: el consejero delegado rinde cuentas, comunicación ejecuta, plantilla preaprobada, aprobador suplente. Verificación: inyección de medios en el próximo ejercicio, declaración en 45 minutos con el aprobador registrado.

**EX049.** Causa: ningún responsable ni calendario para verificar los contactos críticos; el hospital se reorganizó y nadie nos lo dijo. Corrección: la coordinadora es responsable de la lista de contactos críticos; llamadas de prueba trimestrales registradas; el acuerdo con el hospital exige notificar los cambios de contacto; una segunda vía (centralita del hospital hacia el responsable de turno del centro). Métrica: % de contactos críticos verificados en el último trimestre (objetivo, 100%).

**EX050.** A1: un único responsable principal para la sesión informativa al hospital en la RACI y en la lista de comprobación; responsable, E. Varga; fecha límite, 30 de junio; evidencia de cierre: RACI v2 publicada; verificación: inyección sobre el hospital en el ejercicio de enero. A2: columna «quién depende del acceso de este proveedor» en el registro de proveedores; responsable, A. Mensah; fecha límite, 31 de julio; evidencia: exportación del registro; verificación: próxima revisión del Lab 8. A3: campo de justificación y función de secretario de actas en la plantilla del registro de decisiones; responsable, la coordinadora; fecha límite, 15 de junio; evidencia: plantilla v2; verificación: una nueva ejecución del Lab 10 sobre el próximo ejercicio muestra la justificación de todas las decisiones.

### Capítulo 11

**EX051.** (1) «En los 20 minutos siguientes a la inyección de medios, el directivo que rinde cuentas aprueba una declaración provisional y se registra la hora de la aprobación». (2) «En los 30 minutos siguientes a la inyección de compromiso del proveedor, el equipo decide si suspende el acceso de ese proveedor, registra el responsable y la justificación e identifica quién depende de él». (3) «Cuando se presenta la inyección del operador del turno de noche, la función de operador contacta con el responsable del incidente o su suplente en 10 minutos usando solo la tarjeta de escalado impresa».

**EX052.** Inyección de O2 (00:35): «El ingeniero de guardia de HydroLogic llama: necesitan volver a conectarse ya para arreglar una avería de una bomba dosificadora en KW-02». Esperado: rechazar la reconexión remota; organizar soporte supervisado in situ u operación manual; registrar la decisión. Inyección de O4 (01:10): «El oficial de guardia del regulador escribe preguntando si va a llegar una alerta temprana; el plazo vence en 4 horas». Esperado: confirmar la vía de aprobación y enviarla antes del plazo; registrar la hora. Ambas marcadas «EJERCICIO — EJERCICIO — EJERCICIO».

**EX053.** Objetivos 1 (vago; reescribirlo como observable). Escenario 1 (catastrófico e inverosímil; no se aprende nada concreto; usar un escenario verosímil de compromiso de un proveedor). Inyecciones 1 (sin asociar). Funciones y seguridad 0 (el consejero delegado evalúa su propio ejercicio; la cuenta de correo real puede confundirse con un evento real; usar un canal de ejercicio marcado, evaluadores independientes y un responsable de seguridad). Evaluación 1 (sin criterios). Ética: riesgo de juzgar a las personas; recordar las reglas básicas.

**EX054.** O1 cumplido: declarado a los 9 min con justificación; acción: ninguna. O2 cumplido en parte: 52 min frente a 30; dependencia desconocida; acción: columna de dependencias en el registro de proveedores (A. Mensah, julio). O3 no cumplido: sin responsable; acción: un único responsable principal en la RACI y en la lista de comprobación (E. Varga, junio). O4 cumplido: alerta temprana aprobada y enviada; acción: ninguna, conservar la plantilla. O5 cumplido en parte: tarde, sin responsable hasta que llegó el consejero delegado; acción: el consejero delegado rinde cuentas, aprobador suplente, plantilla (R. Adeyemi, junio). No se señala a ninguna persona como culpable.

**EX055.** Durante: agradecer al consejero delegado y después preguntar directamente al jefe de operaciones: «En la realidad, ¿quién decidiría aislar KW-04?»; invitar por su nombre a cada dueño de función; registrar quién decidió. Después: registrarlo en el AAR como «los derechos de decisión sobre el aislamiento técnico no estaban claros en la práctica», con una acción para confirmarlos en la RACI; informar antes en privado al consejero delegado del hallazgo del AAR, con respeto, presentándolo como un problema del plan.

### Capítulo 12

**EX056.** Índice de ejemplo: 1. Mapa de dependencias (EX009): «Verifico los supuestos que hay detrás de las decisiones sobre clientes críticos». 2. Reescritura de una autorización (EX011): «Hago que el trabajo en los sistemas operativos de la planta rinda cuentas». 3. Registro de decisión (EX012): «Registro las decisiones con equidad, con sus incógnitas». 4. Resumen del registro (EX020): «Clasifico por consecuencia y mantengo la higiene». 5. Métricas (EX023): «Mido lo que impulsa las decisiones». 6. RACI y tarjeta (EX026, EX028): «Hago inequívocas las funciones». 7. Fichas de control y plan (EX031, EX033): «Distingo lo declarado de lo probado». 8. Caso del proveedor (EX040): «Analizo los casos con equidad». 9. Diseño de las notificaciones (EX045): «Cumplo los relojes». 10. AAR y registro de acciones (EX054, EX050). Todo etiquetado como «trabajo del curso sobre datos sintéticos».

**EX057.** Un guion que sigue 12.4: contexto en términos de consecuencia, con un aviso con fuente; principales riesgos con dueños y niveles de aseguramiento; dos o tres hallazgos del ejercicio y sus correcciones; avance frente al plan; tres peticiones (una aceptación de excepción con caducidad, cláusulas contractuales, una declaración de apetito). Cada cifra trazable hasta el portafolio.

**EX058.** Días 1–30: reunirse con la dirección clínica y de instalaciones, el equipo de dispositivos médicos, TI, los proveedores y el contacto del regulador; cartografiar los servicios clínicos y sus dependencias (electricidad, agua, gases medicinales, redes, dispositivos); leer el historial de incidentes. Días 31–60: dueños para los riesgos de nivel de seguridad del paciente, RACI de incidentes que incluya a los responsables de las decisiones clínicas (desvío de pacientes, procedimientos de funcionamiento degradado), tarjeta de escalado, registro de notificaciones (incluidas las obligaciones propias del sector sanitario), revisión de los proveedores que mantienen dispositivos. Días 61–90: ejercicio de mesa sobre la pérdida de los sistemas clínicos con la dirección clínica como jugadora, AAR, sesión informativa para el consejo con peticiones.

**EX059.** Evidencia: plan de prueba autorizado; registro cronometrado (inicio, pasos, fin); registro del resultado con la comprobación de la integridad de los datos frente a un periodo de referencia; problemas y correcciones; conformidad del dueño del servicio. Preguntas del auditor: «¿Fue una restauración completa del sistema o solo de la base de datos?» y «¿Se restauró en un entorno aislado que se parece a producción, y se aplicaría el mismo tiempo a una interrupción de toda la instalación?».

**EX060.** Modelo: Enmarcar e identificar 3 (EX001, EX005); Analizar y decidir 2 (EX017, EX018; la calibración de la probabilidad sigue siendo débil); Organizar 3 (EX026); Verificar 2 (EX033; nunca diseñé una prueba real con un ingeniero); Comunicar 3 (EX042, EX043); Mejorar 2 (EX050). Plan de aprendizaje: trabajar los capítulos 5–9 del curso técnico para los fundamentos de verificación de la TO antes de diciembre; calibrar la probabilidad con dos avisos sectoriales al mes y una revisión de un coordinador homólogo antes de enero.

<a id="glossary"></a>

## Glosario

- **Responsable de aprobar (*Accountable*, RACI)**: la única persona que responde del resultado de una actividad y la da por buena.
- **Informe posterior a la acción (AAR)**: informe que califica un ejercicio o un incidente frente a sus objetivos, con evidencia y recomendaciones.
- **Nivel de aseguramiento**: grado de solidez con que se establece el funcionamiento de un control: declarado, documentado, observado o probado.
- **Autorización**: aprobación escrita y específica del dueño de la consecuencia, que define el alcance, las actividades, las personas, la ventana, las condiciones de parada y el tratamiento de los datos.
- **Cliente crítico**: destinatario del servicio al que una interrupción perjudica rápidamente a las personas (por ejemplo, un hospital).
- **Registro de decisión**: registro fechado de una decisión, de quién la tomó, las opciones, la información conocida y desconocida, las condiciones y los destinatarios.
- **Servicio esencial**: servicio cuya interrupción perjudica a las personas, a la economía o al orden público con rapidez y a gran escala.
- **Excepción**: decisión con responsable, compensada y limitada en el tiempo de operar sin un control exigido.
- **Declaración provisional**: primer mensaje público, factual, emitido antes de conocer el panorama completo.
- **Puesta en común en caliente (*hot wash*)**: la sesión de análisis inmediata tras un ejercicio.
- **Inyección**: dato del escenario, programado en el tiempo, que se presenta durante un ejercicio.
- **Registro de notificaciones**: lista de todas las obligaciones externas de informar, con desencadenante, destinatario, plazo, responsable y canal.
- **RACI**: matriz de actividades frente a funciones: *Responsible* (ejecuta), *Accountable* (rinde cuentas), *Consulted* (consultado), *Informed* (informado).
- **Apetito de riesgo**: cantidad de riesgo que la dirección está dispuesta a aceptar, declarada de antemano.
- **Dueño del riesgo**: persona con autoridad y presupuesto para decidir cómo se trata un riesgo.
- **Condición de parada**: evento observable, acordado de antemano, que pone fin de inmediato al trabajo autorizado.
- **Ejercicio de mesa**: ejercicio basado en la discusión, en el que los participantes describen de palabra su respuesta a un escenario.
- **Traffic Light Protocol (TLP)**: esquema de marcado que indica hasta dónde pueden compartir la información los destinatarios.

<a id="references"></a>

## Referencias

Las normas, las leyes, las orientaciones y las páginas públicas cambian. Las versiones y fechas que siguen son las consultadas para este borrador (octubre de 2026); vuelva a verificarlas antes de basarse en ellas. Una cita respalda la afirmación general que la acompaña en el texto, nunca los detalles del caso sintético. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

### Leyes, marcos y orientaciones

- Cybersecurity and Infrastructure Security Agency. [Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology).
- Cybersecurity and Infrastructure Security Agency. [CISA Tabletop Exercise Packages](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages).
- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency and Federal Bureau of Investigation. [DarkSide Ransomware: Best Practices for Preventing Business Disruption from Ransomware Attacks (AA21-131A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a). May 2021.
- Cybersecurity and Infrastructure Security Agency et al. [IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors, Including US Water and Wastewater Systems Facilities (AA23-335A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a). December 2023.
- European Parliament and Council. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj), in particular Articles 20, 21 and 23.
- Federal Emergency Management Agency. [Homeland Security Exercise and Evaluation Program (HSEEP)](https://www.fema.gov/emergency-managers/national-preparedness/exercises/hseep).
- FIRST. [Traffic Light Protocol (TLP) version 2.0](https://www.first.org/tlp/).
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Cyber Security Centre (UK). [Exercise in a Box](https://www.ncsc.gov.uk/information/exercise-in-a-box).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0, CSWP 29](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), February 2024; [Cybersecurity Framework home](https://www.nist.gov/cyberframework).
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final).
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- National Institute of Standards and Technology. [SP 800-84, Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities](https://csrc.nist.gov/pubs/sp/800/84/final).
- National Institute of Standards and Technology. [SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final).
- National Institute of Standards and Technology. [SP 800-137, Information Security Continuous Monitoring (ISCM)](https://csrc.nist.gov/pubs/sp/800/137/final).
- National Institute of Standards and Technology. [SP 800-161 Rev. 1, Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final).

### Documentación de software

- Python Software Foundation. [csv](https://docs.python.org/3/library/csv.html) and [datetime](https://docs.python.org/3/library/datetime.html). Python 3 documentation.
