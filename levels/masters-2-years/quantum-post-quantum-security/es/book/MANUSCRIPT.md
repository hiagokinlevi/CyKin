# Seguridad cuántica y poscuántica: métodos de investigación y práctica del trabajo de fin de máster

- Idioma: español (`es`), edición en español neutro internacional; maestría, dos años; aproximadamente 1200 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Los capítulos 1–8 de 8 tienen texto didáctico escrito, los ejercicios EX001–EX050 y sus resultados resueltos correspondientes. Siguen abiertas la revisión independiente de la materia, la nueva verificación de las fuentes, la revisión de accesibilidad, la revisión lingüística y la verificación de 300 páginas A4.
- Público: investigadores principiantes con una base sólida en el área y formación en métodos de investigación que van a formular una pregunta, evaluar el trabajo previo y producir hallazgos reproducibles en seguridad cuántica y poscuántica. Conocimientos de entrada: el contenido de [posgrado](../../../../postgraduate-2-years/quantum-post-quantum-security/en/book/PLAN.md) o de [ingeniería](../../../../engineering-5-years/quantum-post-quantum-security/en/book/PLAN.md) de esta área o equivalente: TLS 1.3, criptografía de clave pública, estadística básica.
- Relación con el [curso de doctorado](../../../../doctorate-2-years/quantum-post-quantum-security/es/book/MANUSCRIPT.md): el doctorado estudia el descubrimiento de la criptografía vulnerable a la computación cuántica en toda una organización. **Este libro estudia en profundidad una sola pregunta de despliegue** —qué ocurre con las conexiones reales cuando se activa un intercambio de claves híbrido poscuántico/tradicional (PQ/T)— y enseña en torno a ella el ciclo completo de un trabajo de fin de máster.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos.
- Límite educativo: no es un título acreditado y no concede autorización para probar ninguna red ni ningún producto. Toda organización, registro, participante y número de un ejemplo resuelto es **sintético**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los ocho capítulos siguen un trabajo de fin de máster desde la pregunta hasta la defensa. Cada capítulo tiene resultados de aprendizaje, secciones didácticas, un ejemplo resuelto, una actividad práctica (con la biblioteca estándar de Python 3 y sin conexión cuando es útil), errores comunes, ejercicios puntuados de 0 a 3 (0 ausente o inseguro; 1 laguna importante; 2 lagunas menores; 3 completo, acotado y justificado) y un bloque **Siga estudiando**. Intente los ejercicios antes de abrir los [resultados resueltos](#worked-results).

### El trabajo de fin de máster sintético: el Estudio Fragment

La *Universidad de Larkspur* (sintética: 30.000 usuarios y una red de campus con dos vías de salida, una vía directa moderna y un proxy heredado con inspección que usa el ala del hospital universitario) activó el grupo híbrido de TLS 1.3 X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) en sus navegadores gestionados. Aumentaron las incidencias del servicio de asistencia sobre «sitios que no cargan». La pregunta del estudiante: **¿qué parte del aumento de los saludos TLS fallidos tras activar el grupo híbrido es atribuible a mensajes ClientHello que ya no caben en un solo paquete, frente a causas en competencia, y en qué vías de red?** El corpus ficticio de registros se llama **LK-HS-1**; un segundo campus, el *Fenwick College*, aporta los datos de validación. Los codificadores **C1–C2** y las personas entrevistadas **I01–I06** son ficticios.

La pregunta se apoya en la experiencia pública: cuando Chrome empezó a ofrecer una parte de clave híbrida Kyber, Google informó de que los mensajes ClientHello más grandes sacaban a la luz errores en algunos equipos intermedios y servidores ([Chromium Blog, 2023](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html)), y la página comunitaria [tldr.fail](https://tldr.fail/) documenta servidores que tratan mal un ClientHello dividido en varios paquetes TCP.

## Contenido

1. [Pregunta de investigación y método de revisión de la literatura](#ch-01)
2. [Seguridad cuántica y poscuántica: seminario avanzado](../../en/book/MANUSCRIPT.md#ch-02)
3. [Diseño del estudio, ética y reproducibilidad](../../en/book/MANUSCRIPT.md#ch-03)
4. [Seguridad cuántica y poscuántica: explicaciones en competencia](../../en/book/MANUSCRIPT.md#ch-04)
5. [Propuesta y piloto](../../en/book/MANUSCRIPT.md#ch-05)
6. [Recogida y análisis de datos](../../en/book/MANUSCRIPT.md#ch-06)
7. [Redacción del trabajo y limitaciones](../../en/book/MANUSCRIPT.md#ch-07)
8. [Revisión independiente y defensa](../../en/book/MANUSCRIPT.md#ch-08)
- [Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Pregunta de investigación y método de revisión de la literatura

### Resultados de aprendizaje y conexión

Usted podrá (1) convertir una queja operativa en una pregunta investigable; (2) aplicar la prueba FINER (factible, interesante, novedosa, ética y relevante, por sus siglas en inglés); (3) diseñar una búsqueda bibliográfica documentada en fuentes normativas, académicas y profesionales; y (4) construir una tabla de evidencia. El capítulo se apoya en sus conocimientos de entrada y prepara el seminario del capítulo 2.

### 1.1 De la queja a la pregunta

«Lo poscuántico ha roto internet en el ala del hospital» es una queja. Mezcla una intervención (ofrecer X25519MLKEM768), un resultado (los usuarios no pueden cargar sitios), una población (los usuarios del ala del hospital) y una causa implícita (la criptografía poscuántica). Una pregunta de investigación las separa y convierte la causa en algo que se pone a prueba en lugar de suponerse. Primer borrador: *¿aumentaron los fallos?*, que tiene respuesta, pero es descriptivo. Segundo borrador: *¿aumentaron los fallos más en la vía del proxy que en la vía directa?*, que es comparativo. Tercer borrador, la pregunta del Estudio Fragment ya citada: *¿qué parte del aumento es atribuible al tratamiento de los ClientHello de varios paquetes, y dónde?*, que es explicativo y acotado. El tercer borrador es más difícil, pero es el que debe intentar un trabajo de fin de máster, porque puede orientar una decisión (reparar el proxy o retirar el grupo) y puede resultar erróneo.

### 1.2 Por qué el tamaño es plausible

Una parte de clave X25519 tradicional ocupa 32 bytes. La clave de encapsulación de ML-KEM-768 ocupa 1.184 bytes ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), tabla 3), así que la parte del cliente de X25519MLKEM768 ocupa 1.216 bytes y la parte de respuesta del servidor —un texto cifrado de ML-KEM de 1.088 bytes más 32— ocupa 1.120 bytes (RFC 10024). Un ClientHello que antes cabía en un solo segmento TCP ahora necesita a menudo dos. TLS 1.3 lo admite ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html): los registros pueden abarcar varios segmentos), pero el software que solo lee el primer paquete para tomar una decisión de encaminamiento o de inspección puede fallar. El mecanismo es concreto, y eso lo hace comprobable.

### 1.3 FINER

Factible: el proxy y la telemetría de los navegadores de Larkspur ya registran el resultado de los saludos (sintético). Interesante: toda organización que active grupos híbridos se enfrenta a la pregunta. Novedosa: los informes públicos proceden sobre todo de fabricantes o abarcan todo un navegador; pocos estudios atribuyen los fallos dentro de una organización poniendo a prueba explicaciones en competencia. Ética: los registros pueden minimizarse a metadatos (capítulo 3). Relevante: la respuesta decide entre retirar la protección cuántica y reparar la infraestructura. Escriba la comprobación FINER en la propuesta con una frase de evidencia para cada letra, no con una simple marca. Para la factibilidad, nombre las fuentes de registros y confirme con el equipo de red que conservan el resultado de los saludos durante el tiempo suficiente. Para la novedad, remita a la tabla de evidencia, donde se ve la laguna en la atribución dentro de una organización.

### 1.4 Una búsqueda documentada

Busque por separado en tres familias de fuentes. **Normas**: RFC Editor y el datatracker del IETF, sobre intercambio de claves híbrido en TLS, ML-KEM en TLS y tamaño del ClientHello. **Académicas**: IACR ePrint y las bibliotecas digitales de ACM, IEEE y USENIX, con los términos «post-quantum TLS performance», «hybrid key exchange deployment» y «middlebox ossification». **Profesionales**: blogs de ingeniería de navegadores y CDN, que contienen la mayor parte de la evidencia de despliegue, pero están escritos por partes interesadas. Anote la fecha, la base de datos, la cadena y el número de resultados de cada búsqueda para que un lector pueda repetirla: es el equivalente, en una maestría, de un cuaderno de laboratorio.

### 1.5 Ejemplo resuelto: la tabla de evidencia

| Fuente | Tipo | Afirmación pertinente para la pregunta | Evidencia | Límite |
|---|---|---|---|---|
| RFC 10024 | Norma | Define el tamaño de las partes híbridas | Especificación | No dice nada sobre tasas de fallo |
| Chromium Blog 2023 | Profesional | Un ClientHello más grande sacó a la luz errores de equipos intermedios | Observación de despliegue | Todo el navegador; sin atribución por red |
| tldr.fail | Comunitaria | Algunos servidores tratan mal un ClientHello dividido | Lista seleccionada | No es una muestra; selección desconocida |
| FIPS 203 | Norma | Tamaños de ML-KEM | Especificación | — |

La tabla revela la laguna: existen mecanismos y anécdotas, pero no atribución dentro de una organización.

Añada una fila por cada fuente nueva a medida que avance la búsqueda y mantenga honesta la columna de límites, incluso para las fuentes que apoyan la pregunta. El artículo P-7 que se comenta en el seminario entraría en la tabla con su afirmación del 240 % y un límite que señala la tasa base ausente. Un lector debería poder ver solo con la tabla por qué hace falta el estudio.

### 1.6 Errores comunes y límites

- Dejar que la causa implícita de la queja se convierta en la hipótesis sin rivales.
- Buscar solo en bases de datos académicas en un campo donde la evidencia de despliegue está en los blogs de ingeniería.
- Tratar una lista seleccionada (tldr.fail) como una muestra aleatoria.
- Búsquedas no registradas que no pueden repetirse.

Cada error tiene una salvaguarda. Escriba los rivales antes de elegir una hipótesis, como hace el capítulo 4 con cinco de ellos. Busque en los blogs de ingeniería como una familia aparte con sus propios límites. Describa tldr.fail como una lista seleccionada, no como una muestra. Lleve un registro de búsqueda con la fecha, la base de datos, la cadena y el número de resultados de cada ejecución, para que un examinador pueda repetirla.

### Ejercicios — capítulo 1

- **EX001 — Descomponer una queja.** Separe «la PQC ha roto el wifi de la biblioteca» en intervención, resultado, población y causa implícita. Rúbrica: 3 = las cuatro más una causa rival.
- **EX002 — Tres borradores.** Escriba versiones descriptiva, comparativa y explicativa de una pregunta sobre grupos híbridos y VPN. Rúbrica: 3 = versión explicativa acotada y comprobable.
- **EX003 — Aritmética de tamaños.** Calcule el tamaño de las partes de clave del cliente y del servidor para SecP384r1MLKEM1024 con los tamaños de ML-KEM-1024 de FIPS 203 (clave de encapsulación y texto cifrado de 1.568 bytes) y un punto P-384 sin comprimir de 97 bytes. Rúbrica: 3 = ambos tamaños correctos, con fuentes.
- **EX004 — FINER.** Aplique FINER a su propia pregunta. Rúbrica: 3 = cada criterio argumentado y al menos una debilidad admitida.
- **EX005 — Registro de búsqueda.** Escriba un registro de búsqueda con tres bases de datos, cadenas y fechas. Rúbrica: 3 = repetible.
- **EX006 — Tabla de evidencia.** Añada dos filas a partir de fuentes que verifique usted mismo. Rúbrica: 3 = fuentes primarias o claramente etiquetadas como profesionales, límites declarados.
- **EX007 — Enunciado de la laguna.** Escriba la laguna en una frase. Rúbrica: 3 = nombra con precisión la evidencia que falta.

### Síntesis del capítulo

Una pregunta investigable separa intervención, resultado, población y causa, descansa en un mecanismo concreto y se apoya en una búsqueda repetible en fuentes normativas, académicas y profesionales.

### Siga estudiando — capítulo 01 de 08

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](../../en/book/MANUSCRIPT.md#ch-02)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo para la autoevaluación; cualquier respuesta que cumpla la rúbrica puntúa igual. Los números sintéticos proceden de los laboratorios.

**EX001.** Intervención: grupo híbrido activado; resultado: fallan las sesiones de wifi; población: usuarios de la biblioteca; causa implícita: la PQC. Rival: un cambio en el portal cautivo o en el firmware de los puntos de acceso esa misma semana.

**EX002.** Descriptiva: ¿cambiaron los fallos de conexión VPN tras activar el intercambio de claves híbrido en IKEv2? Comparativa: ¿cambiaron más para los usuarios remotos que para los del campus? Explicativa: ¿qué parte del cambio es atribuible al tratamiento de la fragmentación de IKE, y en qué pasarelas?

**EX003.** Parte del cliente: 97 + 1.568 = 1.665 bytes; parte del servidor: 97 + 1.568 = 1.665 bytes (el texto cifrado de ML-KEM-1024 también ocupa 1.568 bytes; FIPS 203; RFC 10024).

**EX004.** Una buena respuesta argumenta cada elemento de FINER y admite una debilidad; por ejemplo, la factibilidad depende del acceso a los registros.

**EX005.** Tres bases de datos (RFC Editor, IACR ePrint, ACM DL), cadenas exactas, fechas y número de resultados.

**EX006.** P. ej., RFC 9794 (terminología; norma; sin datos de despliegue) y SP 800-227 (uso de KEM; norma; no específica de TLS).

**EX007.** «Ningún estudio publicado atribuye los fallos de saludo posteriores a la activación híbrida dentro de una organización al tamaño de los mensajes frente a causas en competencia con un control concurrente».

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Beullens, W. (2022). Breaking Rainbow takes a weekend on a laptop. IACR ePrint 2022/214. <https://eprint.iacr.org/2022/214>
- Castryck, W., and Decru, T. (2022). An efficient key recovery attack on SIDH. IACR ePrint 2022/975. <https://eprint.iacr.org/2022/975>
- Chromium Blog (2023). Protecting Chrome Traffic with Hybrid Kyber KEM. <https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html>
- Driscoll, F., Parsons, M., and Hale, B. (2025). Terminology for Post-Quantum Traditional Hybrid Schemes. RFC 9794. <https://www.rfc-editor.org/rfc/rfc9794.html>
- IANA. TLS Supported Groups registry. <https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml>
- Kwiatkowski, K., Kampanakis, P., Westerbaan, B., and Stebila, D. (2026). Post-Quantum Traditional (PQ/T) Hybrid Key Agreement Mechanisms for TLS 1.3. RFC 10024. <https://www.rfc-editor.org/rfc/rfc10024.html>
- NIST (2024). FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard. <https://doi.org/10.6028/NIST.FIPS.203>
- NIST (2024). FIPS 204, Module-Lattice-Based Digital Signature Standard. <https://doi.org/10.6028/NIST.FIPS.204>
- NIST (2024). FIPS 205, Stateless Hash-Based Digital Signature Standard. <https://doi.org/10.6028/NIST.FIPS.205>
- NIST (2025). IR 8545, Status Report on the Fourth Round of the NIST PQC Standardization Process. <https://doi.org/10.6028/NIST.IR.8545>
- NIST (2025). SP 800-227, Recommendations for Key-Encapsulation Mechanisms. <https://doi.org/10.6028/NIST.SP.800-227>
- Regev, O. (2009). On lattices, learning with errors, random linear codes, and cryptography. *J. ACM* 56(6). <https://doi.org/10.1145/1568318.1568324>
- Rescorla, E. (2018). The Transport Layer Security (TLS) Protocol Version 1.3. RFC 8446. <https://www.rfc-editor.org/rfc/rfc8446.html>
- Shor, P. W. (1997). Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. *SIAM J. Computing* 26(5). <https://doi.org/10.1137/S0097539795293172>
- tldr.fail. Community page on servers that mishandle large or split TLS ClientHello messages. <https://tldr.fail/>
