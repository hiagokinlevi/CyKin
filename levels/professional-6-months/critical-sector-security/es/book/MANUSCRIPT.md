# Infraestructura crítica y seguridad sectorial: coordinación, gobernanza y ejercicios para profesionales

- Idioma: español neutro (`es`); curso profesional, seis meses; aproximadamente 360 horas de estudio planificado (curso 046 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–12 de 12 tienen texto didáctico escrito, cinco laboratorios sin conexión, los ejercicios EX001–EX060 y sus resultados resueltos correspondientes. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: profesionales principiantes que van a **coordinar** la seguridad en una organización que presta un servicio esencial: coordinadores de seguridad o de resiliencia recién nombrados, supervisores de operaciones que han heredado funciones de ciberseguridad, responsables de riesgos y de cumplimiento, planificadores de continuidad y jefes de proyecto en agua, energía, sanidad, transporte, finanzas y servicios públicos. Conocimientos de entrada: nociones básicas de seguridad y una comprensión práctica de cómo se presta el servicio correspondiente.
- En qué se diferencia este curso de sus vecinos. El [libro técnico](../../../../technical-18-months/critical-sector-security/es/book/MANUSCRIPT.md) enseña profundidad práctica: decodificar protocolos, bastionar equipos, configurar cortafuegos. El [libro de tecnólogo](../../../../technologist-3-years/critical-sector-security/es/book/MANUSCRIPT.md) enseña a los implantadores a construir y traspasar un servicio supervisado. El [libro rápido](../../../../rapid-1-month/critical-sector-security/en/book/MANUSCRIPT.md) es una primera introducción. **Este libro profesional trata de coordinación y gobernanza**: quién decide, a quién se informa, quién rinde cuentas, cómo se clasifica y se acepta el riesgo, cómo se exigen responsabilidades a los proveedores, cómo se diseña y se evalúa un ejercicio de mesa y cómo se demuestra todo ello con evidencia ante un consejo de administración o un regulador. En este libro no configurará nada. Aprenderá a hacer las preguntas que garantizan que las personas adecuadas configuran lo adecuado, en el orden adecuado, y pueden demostrarlo.
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
4. [Métodos fundamentales](../../en/book/MANUSCRIPT.md#ch-04): un registro de riesgos guiado por la consecuencia, titularidad y aceptación. Lab 4.
5. [Herramientas e interpretación](../../en/book/MANUSCRIPT.md#ch-05): marcos, evaluaciones, puntuaciones de madurez y métricas leídos con espíritu crítico.
6. [Flujo de trabajo operativo](../../en/book/MANUSCRIPT.md#ch-06): funciones, una matriz RACI, gobernanza de cambios de TI/TO y escalado. Lab 6.
7. [Controles y verificación](../../en/book/MANUSCRIPT.md#ch-07): titularidad de los controles, niveles de aseguramiento y excepciones limitadas en el tiempo.
8. [Análisis supervisado de un caso](../../en/book/MANUSCRIPT.md#ch-08): un caso de acceso remoto de proveedores y la gobernanza de terceros. Lab 8.
9. [Comunicación, ética e informes](../../en/book/MANUSCRIPT.md#ch-09): relojes de notificación, clientes críticos, declaraciones provisionales y honestidad. Lab 9.
10. [Calidad y diagnóstico de averías](../../en/book/MANUSCRIPT.md#ch-10): diagnosticar un programa de coordinación que no funciona. Lab 10.
11. [Laboratorio supervisado](../../en/book/MANUSCRIPT.md#ch-11): diseñar, conducir y evaluar un ejercicio de mesa.
12. [Portafolio de práctica y revisión final](../../en/book/MANUSCRIPT.md#ch-12): portafolio, sesión informativa para el consejo y un plan de 90 días.

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

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 12

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

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

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

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

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Siga estudiando — capítulo 03 de 12

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](../../en/book/MANUSCRIPT.md#ch-04)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

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
