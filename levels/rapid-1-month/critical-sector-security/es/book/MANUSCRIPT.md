# Infraestructura crítica y seguridad sectorial: una primera introducción

- Idioma: español neutro (`es`); curso rápido, un mes; aproximadamente 80 horas de estudio planificado (curso 023 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–4 de 4 tienen texto didáctico escrito, un laboratorio sin conexión, los ejercicios EX001–EX050 y sus resultados resueltos correspondientes. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: **principiantes** sin función de seguridad y con alfabetización digital básica: estudiantes, personas que cambian de profesión y personal o voluntariado que acaba de incorporarse a un hospital, un centro de salud, una empresa de agua o de electricidad, un operador de transporte, un banco, un centro educativo o un ayuntamiento y quiere entender por qué su lugar de trabajo se considera «crítico».
- En qué se diferencia este curso de sus vecinos. El [libro profesional](../../../../professional-6-months/critical-sector-security/es/book/MANUSCRIPT.md) enseña a los coordinadores a gestionar la gobernanza: registros de riesgos, RACI, contratos con proveedores, relojes de notificación y ejercicios de mesa. El [libro técnico](../../../../technical-18-months/critical-sector-security/es/book/MANUSCRIPT.md) enseña profundidad práctica en protocolos y bastionado. **Este libro rápido es una primera mirada y una primera práctica segura.** Le enseña a reconocer qué hace crítico a un servicio, a explicar sus riesgos principales con palabras sencillas, a mantenerse dentro de lo que se le permite hacer, a ver cómo dependen unos servicios de otros y a completar una pequeña tarea guiada. No le convierte en coordinador, ingeniero ni respondedor de incidentes, y nunca le pide que toque un sistema real.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos y no se relicencian aquí.
- Límite educativo: este curso es un proyecto educativo independiente. No es un programa acreditado, no otorga ninguna titulación y no concede autoridad sobre ninguna infraestructura, operador, conjunto de datos o persona reales, ni acceso a ellos. Todo lugar, organización, persona, mensaje, cifra y dependencia de un ejemplo resuelto o del laboratorio es **sintético**, salvo que una frase cite explícitamente una fuente pública. Nada de lo que aparece en este libro constituye asesoramiento jurídico, clínico o regulatorio.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

El curso dura cuatro semanas, un capítulo por semana, unas 20 horas cada una. El resultado del curso es **reconocer y explicar los riesgos principales de las infraestructuras críticas y completar una tarea guiada** con seguridad.

- **Semana 1 (capítulo 1)**: qué son las infraestructuras críticas, por qué la consecuencia importa más que los datos y cómo escribir una frase de riesgo clara.
- **Semana 2 (capítulo 2)**: qué puede y qué no puede hacer, cómo comunicar algo extraño y cómo compartir la información con cuidado.
- **Semana 3 (capítulo 3)**: las partes de un servicio esencial (personas, TI, tecnología operativa, datos, proveedores) y cómo dependen unos servicios de otros.
- **Semana 4 (capítulo 4)**: un laboratorio guiado que sigue qué falla cuando falla un servicio, y un pequeño producto anotado (una «ficha del servicio» de una página) que reúne todo el curso.

Cada capítulo tiene resultados de aprendizaje, secciones didácticas breves con definiciones, un ejemplo resuelto, una actividad práctica, errores comunes y límites, ejercicios numerados y una síntesis. Cada ejercicio indica su objetivo, los insumos, los pasos, la evidencia esperada y una rúbrica de 0–3. Escriba primero su respuesta y después compárela con los [resultados resueltos](#worked-results). Una respuesta distinta que cumpla la rúbrica obtiene la máxima puntuación.

El único laboratorio (capítulo 4) son unas veinte líneas de Python 3 que usan solo la biblioteca estándar. No necesita red, paquetes, privilegios ni datos reales, y su salida está impresa en el libro, así que puede hacer todos los ejercicios sin ejecutarlo. La salida impresa se produjo con Python 3.13.5.

### El escenario sintético de este libro

| Elemento sintético | Papel en el libro | Límite |
|---|---|---|
| **Larkfield**: una pequeña ciudad ficticia de unas 20.000 personas | Escenario de todos los ejemplos. | Lugar inventado. |
| **Larkfield Community Clinic**: un centro de salud sin cita previa con una pequeña farmacia | Donde el lector, **Sam Reyes**, acaba de empezar en un puesto administrativo de recepción. | Inventado. |
| **Larkfield Water** (bombas y una planta de tratamiento), **Larkfield Power** (distribuidora local de electricidad), **Larkfield Bus** | Servicios esenciales vecinos. | Inventados. |
| Personas: Dr. P. Osei (director del centro de salud), H. Novak (gerente del centro, de quien depende Sam), K. Ito (técnico de TI del centro a tiempo parcial, contratado externamente), D. Brandt (operador de turno en Larkfield Water) | Colegas y vecinos. | Inventadas; ninguna persona real. |
| **MedBook** (proveedor del software de citas), **LinkNet** (proveedor de teléfono e internet) | Proveedores. | Inventados; cualquier parecido con empresas reales es accidental. |

Como los datos son sintéticos, el libro puede mostrarle cosas que un recién llegado rara vez vería. Úselas para aprender ideas, nunca como evidencia sobre organizaciones reales.

### Política de fuentes

Toda afirmación factual sobre un marco público, una ley, una orientación o un incidente enlaza con una fuente consultada en octubre de 2026. Las leyes y las orientaciones cambian y difieren entre países: vuelva a verificarlas antes de basarse en ellas. Una cita respalda la afirmación general que la acompaña, nunca los detalles sintéticos de Larkfield. Los incidentes públicos se describen solo al nivel de detalle que publicaron sus autores.

### Cinco reglas para este curso

1. **Mire, aprenda y comunique; no toque.** Nunca pruebe, escanee, inicie sesión ni cambie un sistema que no esté autorizado explícitamente a usar para ese fin (capítulo 2).
2. **Primero, la seguridad de las personas.** En un servicio esencial, el daño a las personas importa más que los datos perdidos.
3. **Diga lo que sabe y lo que supone.** Marque los supuestos como supuestos.
4. **Comunique pronto, por el canal adecuado.** Una falsa alarma comunicada con rapidez cuesta poco; un problema real comunicado tarde puede costar mucho.
5. **Practique solo con material sintético o de estudio**, como los ejemplos y el laboratorio de este libro.

## Contenido

1. [Fundamentos y decisiones](#ch-01): servicios esenciales, sectores y funciones, primero la consecuencia, una primera frase de riesgo y las tres decisiones del recién llegado.
2. [Alcance, permiso y práctica segura](../../en/book/MANUSCRIPT.md#ch-02): qué significa la autorización, los límites del recién llegado, la comunicación y el intercambio cuidadoso de información.
3. [Sistemas, datos y dependencias](../../en/book/MANUSCRIPT.md#ch-03): personas, TI, tecnología operativa, datos, proveedores; dependencias aguas arriba y aguas abajo; puntos únicos de fallo.
4. [Laboratorio guiado y síntesis aplicada](../../en/book/MANUSCRIPT.md#ch-04): el Lab 4 (¿qué más falla?), una ficha del servicio de una página y una autocomprobación del curso.
- [Resultados resueltos](#worked-results) · [Glosario](#glossary) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Infraestructura crítica y seguridad sectorial: fundamentos y decisiones

### Resultados de aprendizaje y conexión

Al terminar este capítulo será capaz de:

- explicar con sus propias palabras qué son las infraestructuras críticas y los servicios esenciales, y nombrar varios sectores;
- explicar por qué, en estos servicios, **la seguridad de las personas y la disponibilidad suelen ir antes que la confidencialidad**;
- describir, a grandes rasgos, tres incidentes públicos y lo que enseña cada uno;
- escribir una frase de riesgo clara con una causa, un evento y una consecuencia;
- elegir con sensatez entre las tres decisiones a las que se enfrenta todo recién llegado: darse cuenta, comunicarlo o dejarlo en manos del dueño.

El capítulo se apoya en la alfabetización digital cotidiana. Prepara el capítulo 2, que fija los límites de lo que puede hacer con esa comprensión.

### 1.1 Qué hace que un servicio sea «crítico»

La mayoría de las personas solo se encuentran con las infraestructuras críticas cuando dejan de funcionar: el grifo se seca, se va la luz, el datáfono dice «denegada», el autobús no llega. Las **infraestructuras críticas** son el conjunto de sistemas, activos y servicios cuya perturbación dañaría gravemente la seguridad, la salud, la economía o el orden público de una sociedad. Un **servicio esencial** es una de las cosas que esas infraestructuras prestan a las personas: agua limpia, electricidad, atención de urgencias, pagos, transporte.

Los gobiernos enumeran estos sectores para poder planificar en torno a ellos. Estados Unidos, por ejemplo, reconoce dieciséis sectores de infraestructura crítica, entre ellos la energía, el agua y las aguas residuales, la sanidad y la salud pública, el transporte, los servicios financieros, las comunicaciones y los servicios de emergencia ([CISA, Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors)). La Directiva NIS2 de la Unión Europea impone obligaciones a las entidades «esenciales» e «importantes» de sectores como la energía, el transporte, la banca, la sanidad, el agua potable y la infraestructura digital ([Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)). Las listas difieren entre países, pero la idea es la misma: algunos servicios importan tanto que su fallo es un problema de todos.

Una segunda idea útil es la **función** en lugar de la organización. La CISA describe un conjunto de funciones críticas nacionales (como «suministrar agua» o «prestar atención médica») agrupadas bajo cuatro verbos: conectar, distribuir, gestionar y suministrar ([CISA, National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set)). Pensar en funciones ayuda a un recién llegado a hacer la pregunta adecuada: no «¿qué posee mi empleador?», sino «¿qué *hace* mi lugar de trabajo por las personas y qué les ocurre si deja de hacerlo?».

### 1.2 Primero, la consecuencia

En una oficina corriente, la preocupación clásica es que roben información. En un servicio esencial, la primera preocupación suele ser que **se dañe a las personas** o que **el servicio se detenga**. Un orden de preocupación útil para este curso es:

| Orden | Pregunta | Ejemplo de Larkfield (sintético) |
|---|---|---|
| 1. Seguridad de las personas | ¿Podría resultar herido alguien? | Una dosis química errónea en la planta de agua. |
| 2. Disponibilidad (continuidad) | ¿Sigue funcionando el servicio? | El centro de salud no puede ver las citas ni las recetas. |
| 3. Integridad (fiabilidad) | ¿Podemos creer lo que muestra el sistema? | Una pantalla muestra una bomba en marcha cuando se ha parado. |
| 4. Confidencialidad | ¿Se ha filtrado información privada? | Un extraño copia historias clínicas de pacientes. |

Este es un orden para **pensar en el daño**, no una regla según la cual la confidencialidad no importa. Una filtración de historias clínicas es grave y puede acarrear obligaciones legales de informar con rapidez a las personas afectadas. Lo importante es que un recién llegado que solo piense en contraseñas y datos pasará por alto los riesgos que más importan en estos sectores. El NIST Cybersecurity Framework 2.0, una guía de alto nivel de uso extendido, organiza los resultados de seguridad en seis funciones (Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar) precisamente porque mantener un servicio en marcha y restablecerlo importa tanto como mantener los datos en secreto ([NIST CSF 2.0](https://www.nist.gov/cyberframework)).

### 1.3 Tres incidentes públicos, en breve

No necesita detalles técnicos para aprender de hechos reales. Lea usted mismo cada fuente; los resúmenes siguientes se quedan al nivel que publicaron sus autores.

- **La electricidad en Ucrania, diciembre de 2015.** La CISA informa de que los atacantes causaron cortes de electricidad que afectaron a unos 225.000 clientes, accionando interruptores a distancia y dificultando la recuperación; las empresas restablecieron el suministro pasando a operación manual ([CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01)). *Lección:* los ataques a los ordenadores pueden alcanzar el mundo físico, y las personas capaces de hacer funcionar las cosas a mano forman parte de la resiliencia.
- **WannaCry y el NHS de Inglaterra, mayo de 2017.** La National Audit Office del Reino Unido concluyó que el ransomware perturbó al menos a un tercio de los *trusts* del NHS en Inglaterra y provocó la cancelación de miles de citas y operaciones ([NAO, Investigation: WannaCry cyber attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/)). *Lección:* un malware corriente de TI se convierte en un problema de disponibilidad sanitaria; lo sufren los pacientes, no solo los ordenadores.
- **Instalaciones de agua, 2023.** La CISA y otras agencias asociadas informaron de que unos actores comprometieron controladores industriales expuestos a internet en varias instalaciones de agua y aguas residuales de Estados Unidos, probablemente usando contraseñas predeterminadas ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)). *Lección:* debilidades simples (un dispositivo accesible desde internet con la contraseña de fábrica) pueden bastar.

### 1.4 Escribir una frase de riesgo

«Ransomware» es una palabra, no un riesgo. Un **riesgo** es algo que podría ocurrir y que importaría. Una frase de riesgo clara tiene tres partes:

> **Como** (causa o debilidad), **podría ocurrir (algo)** (evento), **lo que llevaría a** (consecuencia para las personas o el servicio).

Ejemplo (sintético): «*Como* los PC de citas del centro de salud comparten una contraseña escrita en una nota adhesiva, *alguien que pase junto al mostrador podría iniciar sesión y cambiar o borrar citas*, *lo que llevaría a* que los pacientes se quedaran sin atención y el personal perdiera una mañana en reconstruir la lista».

Las buenas frases de riesgo nombran una consecuencia real (personas, tiempo, servicio), no solo «pérdida de datos». También dejan claro **quién debería ser dueño** del problema: aquí, la gerencia del centro, no la persona que se dio cuenta.

### 1.5 Las tres decisiones del recién llegado

Como principiante no se espera que arregle la seguridad. Se espera que **se dé cuenta**, que lo **comunique** por el canal adecuado y que **deje la corrección en manos del dueño**. Ante algo que parece ir mal, pregúntese:

1. *¿Hay alguien en peligro ahora?* Si es así, siga primero el procedimiento de seguridad o de emergencia; la ciberseguridad va después.
2. *¿Necesita saberlo alguien?* Si podría afectar al servicio, a las personas o a datos privados, comuníquelo hoy a su supervisor o por el canal establecido.
3. *¿Me corresponde cambiarlo?* Casi siempre, no. Describa lo que vio; no lo «compruebe un momento» ni lo «arregle un momento».

### 1.6 Ejemplo resuelto: la primera semana de Sam (sintético)

Sam Reyes empieza en la recepción del Larkfield Community Clinic. En la primera semana, Sam se fija en cuatro cosas:

| Lo que Sam observa | Orden de preocupación | La decisión de Sam |
|---|---|---|
| (a) La puerta trasera del almacén de la farmacia queda calzada abierta por la tarde. | Seguridad/integridad: podrían llevarse o manipular medicamentos. | Comunicarlo hoy a H. Novak; no sermonear a los colegas. |
| (b) Un correo «de MedBook» pide al personal que vuelva a introducir su contraseña en un enlace. | Disponibilidad y confidencialidad: un inicio de sesión robado podría bloquear el sistema de citas. | No hacer clic; comunicarlo por la vía de «notificar correo sospechoso» del centro. |
| (c) El PC de recepción muestra «actualizaciones pendientes; es necesario reiniciar» desde hace una semana. | Disponibilidad, más adelante. | Mencionarlo a H. Novak, que lo traslada a K. Ito (TI). No reiniciar por su cuenta un PC clínico compartido en mitad del turno. |
| (d) Una amistad que trabaja en Larkfield Water comenta que la planta todavía usa una herramienta de acceso remoto «con la contraseña antigua». | Posible problema de seguridad física en otra organización. | No es un sistema de Sam. Sugerirle que lo plantee a su propio supervisor; no probar la herramienta, no pedir la contraseña ni publicar nada al respecto. |

Sam escribe una frase de riesgo para (b): «Como el personal está recibiendo correos falsos de MedBook muy convincentes, alguien podría introducir su contraseña en una página falsa, lo que llevaría a que un extraño bloqueara o cambiara las citas y el centro no pudiera atender a los pacientes durante horas». Sam marca un supuesto: «*Supuesto:* los inicios de sesión de MedBook no están protegidos por un segundo factor; no lo sé».

Fíjese en lo que Sam *no* hizo: investigar, probar el enlace, reiniciar el PC o tocar nada de Larkfield Water. Cada decisión es pequeña, pero juntas son exactamente lo que aporta un recién llegado.

### 1.7 Actividad práctica

Elija un servicio esencial que use (su empresa de agua, el hospital local, la compañía de autobuses o su banco). En no más de una página, escriba: la función que presta a las personas; quién resultaría perjudicado primero si se detuviera durante un día; una frase de riesgo con causa, evento y consecuencia; y una cosa que esté suponiendo. Manténgalo en términos generales: use solo información pública y no sondee el servicio de ninguna manera. Intercambie las páginas con un compañero que haya elegido un servicio distinto y revisen la frase de riesgo del otro: ¿nombra una causa, un evento y una consecuencia para las personas? Después comparen a quién dijeron que perjudicaría primero. Un hospital y una compañía de autobuses dan respuestas muy distintas, que es justamente la razón de pensar en funciones.

### 1.8 Errores comunes y límites

- Pensar que la seguridad solo trata de contraseñas y datos. En los servicios esenciales, empiece por la seguridad de las personas y la continuidad.
- Escribir los riesgos como palabras sueltas («hackers», «virus») en lugar de como frases a partir de las cuales alguien pueda actuar.
- Intentar arreglar las cosas usted mismo. Su trabajo a este nivel es darse cuenta y comunicarlo.
- Tomar el resumen de un incidente como la historia completa. Los informes públicos son incompletos a propósito.
- Este capítulo simplifica: las organizaciones reales usan métodos formales de riesgo, y las leyes sobre los servicios críticos difieren entre países.

- Dar por hecho que quien detectó un problema debe ser su dueño. Sam se fijó en la contraseña de la nota adhesiva, pero es la gerencia del centro quien decide qué hacer al respecto.
- Olvidar marcar los supuestos. La nota de Sam de que los inicios de sesión de MedBook podrían carecer de segundo factor está etiquetada como desconocida, no afirmada como un hecho.

### Ejercicios — capítulo 1

**EX001 — Identifique los servicios esenciales.** *Objetivo:* reconocer los servicios esenciales. *Insumos:* una lista: agua potable, un cine, un servicio de urgencias hospitalario, una red de pagos con tarjeta, una tienda de ropa, una red eléctrica regional, una red de autobuses urbanos, un servidor de videojuegos. *Pasos:* marcar cada uno como esencial o no y dar una razón de una línea. *Evidencia esperada:* ocho marcas con razones. *Rúbrica:* 3 = agua, urgencias, pagos, red eléctrica y autobuses marcados como esenciales con razones basadas en el daño, los demás no, con una nota de que «esencial» depende del contexto; 2 = marcas correctas, razones débiles; 1 = varios errores; 0 = nada.

**EX002 — Asocie con el sector.** *Objetivo:* relacionar servicios con sectores. *Insumos:* los cinco servicios esenciales de EX001. *Pasos:* nombrar el sector al que pertenece cada uno usando la lista de sectores de la CISA. *Evidencia esperada:* cinco parejas. *Rúbrica:* 3 = todas correctas (agua y aguas residuales; sanidad y salud pública; servicios financieros; energía; sistemas de transporte); 2 = cuatro correctas; 1 = dos o tres; 0 = menos.

**EX003 — La función, no la organización.** *Objetivo:* pensar en funciones. *Insumos:* Larkfield Community Clinic, Larkfield Water, Larkfield Bus. *Pasos:* escribir como una expresión verbal la función que cada uno presta a las personas. *Evidencia esperada:* tres expresiones. *Rúbrica:* 3 = «prestar atención médica / dispensar medicamentos», «suministrar agua limpia», «transportar a las personas» o equivalentes, cada una centrada en las personas; 2 = una describe la organización; 1 = enumera edificios o software; 0 = nada.

**EX004 — Orden de preocupación.** *Objetivo:* aplicar primero la consecuencia. *Insumos:* (a) se copian las direcciones de los pacientes; (b) se cambia sin aprobación una dosis del tratamiento del agua; (c) el sistema de citas del centro de salud no está disponible durante una mañana; (d) una pantalla de una bomba muestra «en marcha» cuando la bomba se ha parado. *Pasos:* ordenarlos de más a menos preocupante y justificar cada uno. *Evidencia esperada:* clasificación con razones. *Rúbrica:* 3 = (b) primero (seguridad de las personas), después (c) o (d) con un razonamiento sobre continuidad frente a fiabilidad, (a) último por daño inmediato pero señalado como grave desde el punto de vista legal; 2 = solo el primero correcto; 1 = (a) primero sin razonamiento; 0 = nada.

**EX005 — ¿Por qué no «primero los datos»?** *Objetivo:* explicar el cambio de prioridad. *Insumos:* la sección 1.2. *Pasos:* en tres o cuatro frases, explicar a un amigo por qué los servicios esenciales piensan en la seguridad de las personas y la disponibilidad antes que en la confidencialidad. *Evidencia esperada:* párrafo breve. *Rúbrica:* 3 = menciona el daño físico, que las personas dependen de la continuidad y que la confidencialidad sigue importando; 2 = dos de ellos; 1 = uno; 0 = nada.

**EX006 — Lección de un incidente: Ucrania 2015.** *Objetivo:* extraer una lección de una fuente pública. *Insumos:* [CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). *Pasos:* leer el resumen y escribir el número de clientes afectados, cómo se restableció la electricidad y una lección para un recién llegado. *Evidencia esperada:* tres respuestas breves. *Rúbrica:* 3 = unos 225.000 clientes, operación manual, una lección sobre la consecuencia física o la alternativa manual; 2 = dos correctas; 1 = una; 0 = nada.

**EX007 — Lección de un incidente: WannaCry y el NHS.** *Objetivo:* relacionar el malware de TI con el daño al servicio. *Insumos:* el resumen del [informe de la NAO](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). *Pasos:* escribir quién resultó perjudicado y cómo, en dos frases, sin términos técnicos. *Evidencia esperada:* dos frases. *Rúbrica:* 3 = pacientes perjudicados por citas y operaciones canceladas y *trusts* perturbados, planteado como disponibilidad; 2 = menciona la perturbación sin las personas; 1 = solo «se cifraron los ordenadores»; 0 = nada.

**EX008 — Lección de un incidente: controladores de agua.** *Objetivo:* reconocer debilidades simples. *Insumos:* [CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a). *Pasos:* nombrar las dos condiciones simples que hicieron posible el compromiso y decir por qué cada una es una lección de nivel principiante. *Evidencia esperada:* dos condiciones con razones. *Rúbrica:* 3 = exposición a internet y contraseñas predeterminadas, cada una explicada como un fallo de higiene cotidiana; 2 = ambas nombradas, sin razones; 1 = una; 0 = nada.

**EX009 — Reescriba tres riesgos.** *Objetivo:* escribir frases de riesgo. *Insumos:* las palabras «phishing», «ordenador viejo» y «puerta abierta», situadas en el centro de salud de Larkfield. *Pasos:* reescribir cada una como «Como…, podría ocurrir…, lo que llevaría a…». *Evidencia esperada:* tres frases. *Rúbrica:* 3 = cada una tiene causa, evento y una consecuencia para las personas o el servicio; 2 = a una le falta la consecuencia; 1 = siguen siendo genéricas; 0 = nada.

**EX010 — Encuentre al dueño.** *Objetivo:* ver que los riesgos tienen dueño. *Insumos:* sus tres frases de EX009 y la lista de personas de Larkfield. *Pasos:* nombrar quién debería ser dueño de cada riesgo y por qué no es Sam. *Evidencia esperada:* tres dueños con razones. *Rúbrica:* 3 = la gerencia o la dirección del centro para los procesos y las instalaciones, el técnico de TI contratado para el ordenador (con la gerencia decidiendo), razones basadas en la autoridad; 2 = dueños sin razones; 1 = se nombra a Sam como dueño; 0 = nada.

**EX011 — Tres decisiones.** *Objetivo:* aplicar darse cuenta / comunicar / dejarlo al dueño. *Insumos:* un colega dice: «la alarma de la nevera de las vacunas pitó toda la noche, pero la apagué». *Pasos:* recorrer las tres preguntas de la sección 1.5. *Evidencia esperada:* tres respuestas breves. *Rúbrica:* 3 = reconoce primero un posible problema de seguridad del paciente, lo comunica hoy a la gerencia del centro, no ajusta la nevera ni la alarma; 2 = lo comunica, pero no ve el aspecto de seguridad; 1 = intenta arreglarlo; 0 = nada.

**EX012 — Saber frente a suponer.** *Objetivo:* separar los hechos de los supuestos. *Insumos:* la frase de riesgo de Sam para (b) en 1.6. *Pasos:* enumerar dos hechos que Sam conoce y dos cosas que Sam supone. *Evidencia esperada:* cuatro elementos. *Rúbrica:* 3 = hechos: llegaron correos falsos, piden contraseñas; supuestos: no hay segundo factor, que el correo es falso y no un aviso real de MedBook (o similar); 2 = tres correctos; 1 = los mezcla; 0 = nada.

**EX013 — No es su sistema.** *Objetivo:* respetar los límites fuera de su lugar de trabajo. *Insumos:* el punto (d) de 1.6. *Pasos:* escribir el mensaje que Sam podría enviar a esa amistad. *Evidencia esperada:* dos o tres frases. *Rúbrica:* 3 = anima a la amistad a decírselo a su supervisor o a su contacto de seguridad, no pide detalles ni contraseñas, no sugiere probar la herramienta; 2 = anima a comunicarlo, pero pide detalles; 1 = sugiere comprobarlo; 0 = nada.

### Síntesis del capítulo

Las infraestructuras críticas prestan funciones de las que las personas no pueden prescindir, y su seguridad se juzga por la consecuencia: primero la seguridad de las personas, después la continuidad, la fiabilidad y la confidencialidad. Los incidentes reales muestran que los problemas informáticos llegan a los pacientes, a los hogares y a las calles, y que a menudo bastan debilidades simples. Las herramientas de un recién llegado son una frase de riesgo clara, una marca honesta en lo que se supone y tres decisiones: darse cuenta, comunicarlo y dejar la corrección en manos del dueño.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 04

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](../../en/book/MANUSCRIPT.md#ch-02)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resultados resueltos y notas de evaluación

Estas son respuestas modelo. Una respuesta distinta que cumpla el nivel de exigencia de la rúbrica en cuanto a razonamiento, seguridad y honestidad sobre los límites obtiene la máxima puntuación. Todas las organizaciones, personas y datos de Larkfield son sintéticos.

### Capítulo 1

**EX001.** Esenciales: agua potable (enfermedades y problemas de saneamiento en cuestión de horas), urgencias hospitalarias (retrasos que ponen en peligro la vida), red de pagos con tarjeta (las personas no pueden comprar comida ni combustible), red eléctrica regional (casi todos los demás servicios dependen de ella), red de autobuses urbanos (las personas no pueden llegar al trabajo, a la escuela ni a recibir atención). No esenciales en la mayoría de los contextos: cine, tienda de ropa, servidor de videojuegos. El contexto importa: un servidor de juegos no es esencial, pero el mismo centro de datos podría alojar también los sistemas de un hospital.

**EX002.** Agua → agua y aguas residuales; urgencias → sanidad y salud pública; pagos con tarjeta → servicios financieros; red eléctrica → energía; autobuses → sistemas de transporte.

**EX003.** Centro de salud: «prestar atención médica y dispensar medicamentos a los vecinos». Agua: «suministrar agua potable segura». Autobús: «transportar a las personas por la ciudad». Cada expresión parte de lo que reciben las personas, no de los edificios ni del software.

**EX004.** (b) primero: un cambio de dosis no aprobado puede enfermar a las personas. Después (d) o (c): (d) es peligroso porque los operadores actúan sobre una imagen falsa (el depósito podría vaciarse mientras la pantalla parece normal); (c) detiene la atención durante una mañana, pero es visible y tiene soluciones alternativas. Cualquiera de los dos órdenes es aceptable con este razonamiento. (a) último por daño físico inmediato, pero es grave y puede desencadenar obligaciones legales de notificar con rapidez a las personas y a los reguladores.

**EX005.** «En un hospital o en una planta de agua, un problema informático puede dañar directamente a las personas: una dosis equivocada, una operación que no se hace. Además, miles de personas dependen de que el servicio funcione a todas horas, así que detenerlo ya es un daño. Por eso piensan primero en la seguridad de las personas y en mantener el servicio. La privacidad sigue importando; solo que no suele ser el primer peligro».

**EX006.** Unos 225.000 clientes se quedaron sin electricidad; el suministro se restableció pasando a operación manual. Lección: los ciberataques pueden tener efectos físicos, y el personal capaz de hacer funcionar las cosas a mano forma parte de la resiliencia.

**EX007.** «A los pacientes se les cancelaron citas y operaciones porque los ordenadores de los hospitales dejaron de funcionar. Muchos *trusts* del NHS se vieron perturbados, así que el daño consistió en que la atención no estaba disponible, no solo en los ordenadores».

**EX008.** (1) Los controladores eran accesibles desde internet; (2) probablemente seguían usando contraseñas predeterminadas. Ambos son fallos de higiene cotidiana que no exigen ninguna habilidad avanzada para explotarlos (ni para evitarlos), y por eso los principiantes deben reconocerlos.

**EX009.** (1) «Como el personal recibe correos falsos muy convincentes, alguien podría introducir su contraseña en una página de inicio de sesión falsa, lo que llevaría a que un extraño bloqueara el sistema de citas y se rechazara a los pacientes». (2) «Como el PC de recepción lleva meses sin actualizarse, un malware podría explotar un fallo conocido y dejarlo inservible, lo que llevaría a retrasos en el registro de los pacientes». (3) «Como la puerta del almacén de la farmacia queda calzada abierta, alguien podría llevarse o manipular medicamentos, lo que llevaría a daños a los pacientes o a desabastecimiento».

**EX010.** Phishing: la gerencia del centro (H. Novak) es dueña de la concienciación y la comunicación del personal, con K. Ito para los controles técnicos. Ordenador viejo: decide la gerencia del centro; K. Ito realiza las actualizaciones. Puerta abierta: la gerencia o la dirección del centro es dueña de la seguridad de las instalaciones y de los medicamentos. No Sam: Sam no tiene autoridad sobre presupuestos, normas del personal ni cambios de TI; su función es darse cuenta y comunicarlo.

**EX011.** (1) ¿Peligro? Posiblemente: las vacunas conservadas a una temperatura incorrecta pueden perder eficacia, lo que es un problema de seguridad del paciente. (2) Comunicarlo hoy a H. Novak (o al personal de enfermería responsable), con la hora a la que se apagó la alarma. (3) No le corresponde a Sam cambiarlo: no ajustar la nevera ni la alarma; el dueño decide si las vacunas deben ponerse en cuarentena.

**EX012.** Sabido: llegaron correos de MedBook de aspecto falso; piden contraseñas en un enlace. Supuesto: los inicios de sesión de MedBook no tienen segundo factor; los correos son falsos y no un aviso auténtico pero mal diseñado; alguien ha llegado a introducir su contraseña.

**EX013.** «Gracias por contármelo; parece algo que merece la pena plantear a tu supervisor o a quien se ocupe de la seguridad en la planta, porque son quienes pueden comprobarlo y arreglarlo. Mejor no compartas los detalles conmigo ni con nadie de fuera, y desde luego no pruebes la herramienta tú».

<a id="glossary"></a>

## Glosario

- **Actuador**: dispositivo que actúa sobre el mundo físico, como el motor de una bomba o una válvula.
- **Autorización**: permiso específico del dueño de un sistema para hacer con él algo definido, normalmente por escrito.
- **Disponibilidad**: el servicio o la información están ahí cuando se necesitan.
- **Respaldo**: alternativa que puede sustituir a una dependencia, como un generador para la electricidad de la red.
- **Cascada**: fallo que se propaga de un servicio a los que dependen de él.
- **Confidencialidad**: la información solo la ven quienes tienen permiso para verla.
- **Infraestructura crítica**: sistemas, activos y servicios cuya perturbación dañaría gravemente la seguridad, la salud, la economía o el orden público.
- **Dependencia**: algo que un servicio necesita para funcionar; aguas arriba, aguas abajo o compartida.
- **Servicio esencial**: servicio del que las personas no pueden prescindir durante mucho tiempo, como el agua, la electricidad, la sanidad o los pagos.
- **HMI (interfaz persona-máquina)**: la pantalla y los mandos del operador para un proceso.
- **Integridad**: la información y los sistemas son exactos y no se han modificado indebidamente.
- **Alternativa manual**: forma de mantener un servicio a mano cuando falla un sistema.
- **TO (tecnología operativa)**: ordenadores y dispositivos que miden y controlan procesos físicos.
- **PLC (controlador lógico programable)**: pequeño ordenador robusto que lee sensores y controla actuadores.
- **Frase de riesgo**: «Como (causa), podría ocurrir (evento), lo que llevaría a (consecuencia)».
- **SCADA**: supervisión, control y adquisición de datos; reúne datos y supervisión de muchas instalaciones.
- **Alcance**: el límite exacto de una autorización.
- **Sensor**: dispositivo que mide algo, como un nivel o una presión.
- **Ficha del servicio**: el resumen anotado de una página de un servicio esencial que se elabora en este curso.
- **Punto único de fallo**: elemento cuya pérdida detiene un servicio porque no hay alternativa.
- **TLP (Traffic Light Protocol)**: etiquetas (RED, AMBER+STRICT, AMBER, GREEN, CLEAR) que indican hasta dónde puede compartirse la información.

<a id="references"></a>

## Referencias

Todos los enlaces se consultaron en octubre de 2026. Vuelva a verificarlos antes de basarse en ellos; las leyes y las orientaciones cambian y difieren entre jurisdicciones. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

### Sectores, funciones y marcos

- Cybersecurity and Infrastructure Security Agency. [Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology).
- European Parliament and Council. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj).
- National Institute of Standards and Technology. [Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- National Institute of Standards and Technology. [SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final).

### Incidentes públicos

- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency and Federal Bureau of Investigation. [DarkSide Ransomware: Best Practices for Preventing Business Disruption from Ransomware Attacks (AA21-131A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a). May 2021.
- Cybersecurity and Infrastructure Security Agency et al. [IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors, Including US Water and Wastewater Systems Facilities (AA23-335A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a). December 2023.
- National Audit Office (UK). [Investigation: WannaCry cyber attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.

### Práctica segura, notificación e intercambio de información

- Cybersecurity and Infrastructure Security Agency. [Report to CISA](https://www.cisa.gov/report).
- Cybersecurity and Infrastructure Security Agency. [Secure Our World](https://www.cisa.gov/secure-our-world).
- FIRST. [Traffic Light Protocol (TLP) 2.0](https://www.first.org/tlp/).
- National Cyber Security Centre (UK). [Exercise in a Box](https://www.ncsc.gov.uk/information/exercise-in-a-box).

### Herramientas del laboratorio

- Python Software Foundation. [Python 3 documentation](https://docs.python.org/3/).
