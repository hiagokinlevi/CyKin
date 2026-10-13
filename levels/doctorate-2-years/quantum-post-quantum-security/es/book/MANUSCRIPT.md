# Seguridad cuántica y poscuántica: métodos de investigación doctoral y práctica de la tesis

- Idioma: español (`es`), edición en español neutro internacional; programa de investigación doctoral, dos años; aproximadamente 1600 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–8 de 8 tienen texto didáctico escrito, los ejercicios EX001–EX050 y sus resultados resueltos correspondientes. Siguen abiertas la revisión independiente de la materia, la nueva verificación de las fuentes, la revisión de accesibilidad, la revisión lingüística y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: investigadores avanzados con experiencia de investigación y una pregunta defendible sobre las consecuencias para la seguridad de la computación cuántica, la migración a la criptografía poscuántica (PQC), los protocolos híbridos poscuánticos/tradicionales (PQ/T) o la agilidad criptográfica. Conocimientos de entrada: el contenido previsto para el programa de [maestría](../../../../masters-2-years/quantum-post-quantum-security/en/book/PLAN.md) de esta área o una experiencia equivalente, además de soltura práctica en criptografía de clave pública, probabilidad discreta, álgebra lineal básica sobre anillos finitos y una familia de protocolos como TLS 1.3, la PKI X.509 o IKEv2.
- Relación con los cursos vecinos: un curso general de criptografía estudia cómo se construyen y se demuestran las primitivas. **Este libro estudia la transición**: cómo una comunidad llega a saber si la criptografía vulnerable a la computación cuántica se ha encontrado, sustituido, combinado con PQC y vuelto a hacer sustituible, y cómo un investigador produce evidencia sobre esa transición que resista la crítica.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos.
- Límite educativo: este programa es un plan educativo independiente. No es un programa de doctorado acreditado, no otorga ningún título y no concede autorización para escanear, interceptar, degradar o probar ninguna red, producto, autoridad de certificación o persona reales. Toda organización, conjunto de datos, corpus, participante y resultado numérico de un ejemplo resuelto es **sintético**, salvo que una frase cite explícitamente una fuente pública. El código de retículos de juguete de este libro es deliberadamente inseguro y nunca debe proteger datos reales.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Lea los ocho capítulos en orden; siguen el arco de un único proyecto doctoral. El capítulo 1 fija normas de integridad para investigar en un campo en el que los plazos son inciertos y las afirmaciones de los fabricantes, ruidosas. El capítulo 2 cartografía la frontera —estimaciones de recursos del criptoanálisis cuántico, las normas del NIST, los protocolos híbridos, la seguridad de las implementaciones y la agilidad— y aísla una pregunta abierta. El capítulo 3 convierte esa pregunta en una contribución falsable. El capítulo 4 replica las líneas base y pilota el método en un corpus modelo. El capítulo 5 ejecuta el estudio principal y lo valida en un segundo corpus independiente. El capítulo 6 somete las afirmaciones a una crítica adversarial. El capítulo 7 ensambla la tesis y un archivo de reproducibilidad por niveles. El capítulo 8 prepara la defensa, la divulgación coordinada y un plan de publicación.

Cada capítulo contiene resultados de aprendizaje, secciones didácticas, un ejemplo resuelto, una actividad práctica con código en Python 3 que solo usa la biblioteca estándar y funciona sin conexión cuando es útil, errores comunes y límites, ejercicios numerados con una rúbrica de 0 a 3, una síntesis y un bloque **Siga estudiando**. Intente cada ejercicio antes de abrir los [resultados resueltos](#worked-results).

Mantenga cinco etiquetas en cada nota de investigación: **observación** (lo que registró un instrumento o una fuente con nombre), **inferencia** (lo que concluye y con qué supuestos), **afirmación** (lo que defenderá, con su alcance), **decisión** (lo que alguien eligió a causa de ello) y **exposición** (qué datos, firmas o sistemas siguen siendo vulnerables a la computación cuántica, y durante cuánto tiempo). La investigación en PQC se tuerce sobre todo cuando una observación sobre la negociación de un protocolo se convierte en silencio en una afirmación sobre el riesgo cuántico de una organización.

### El corpus de investigación sintético

El libro sigue un proyecto inventado, el **Estudio Ciphertrail**, que pregunta: *¿un inventario criptográfico de doble fuente —telemetría pasiva de los saludos de conexión (handshakes) fusionada con el análisis estático de código y configuración— recupera los usos de establecimiento de claves y de firma vulnerables a la computación cuántica de forma más completa que el análisis estático por sí solo, con qué precisión, y en qué clases de activos desaparece la ventaja?*

| Elemento sintético | Función | Límite |
|---|---|---|
| **Halden Regional Health Network (HRHN)**: 3 hospitales, 1200 servicios, una PKI privada, un concentrador de VPN, dispositivos médicos en una red segregada | Contexto del corpus principal (capítulos 1 y 3–5). | Organización inventada; ningún hospital, paciente ni registro real. |
| **Marrow Logistics**: una empresa de transporte de mercancías con otra pila tecnológica, usada como segundo corpus intacto | Validación independiente (capítulos 5–6). | Inventada. |
| **InvBench-22** | Un banco de referencia de inventario sintético «publicado» cuya exhaustividad declarada no puede reproducirse (capítulo 4). | Inventado; no lo busque. |
| Estudios sintéticos **Q1–Q8** | Artículos ficticios usados para practicar la evaluación crítica (capítulo 2). | Inventados. |
| Ingenieros **E01–E10** | Profesionales ficticios de una adjudicación ciega de hallazgos de inventario (capítulo 5). | Inventados; no aparecen datos de personas participantes. |

### Política de fuentes

Las fuentes primarias se citan por un identificador estable y se comprobaron el 12 de octubre de 2026. Las normas cambian: en esa fecha, FIPS 206 (FN-DSA, derivada de Falcon) y la norma HQC seguían en elaboración, y NIST IR 8547 seguía siendo un borrador público inicial. Vuelva a verificar cada estado antes de basarse en él. Las estimaciones de recursos de los ataques cuánticos son resultados de investigación con supuestos, no previsiones. La sección de [referencias](#references) enumera todas las fuentes externas.

## Contenido

1. [Integridad y métodos avanzados de investigación](#ch-01)
2. [Seguridad cuántica y poscuántica: frontera de la investigación](#ch-02)
3. [Propuesta de contribución original](#ch-03)
4. [Replicación de las líneas base y piloto](#ch-04)
5. [Estudio principal y validación independiente](../../en/book/MANUSCRIPT.md#ch-05)
6. [Crítica de pares y revisión](../../en/book/MANUSCRIPT.md#ch-06)
7. [Síntesis de la tesis y archivo de reproducibilidad](../../en/book/MANUSCRIPT.md#ch-07)
8. [Defensa y plan de publicación](../../en/book/MANUSCRIPT.md#ch-08)
- [Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Integridad y métodos avanzados de investigación

### Resultados de aprendizaje y conexión

Al terminar este capítulo podrá (1) separar los cinco tipos de enunciado que produce la investigación en PQC y mantenerlos etiquetados; (2) explicar por qué las afirmaciones sobre los plazos cuánticos deben formularse como supuestos condicionales y no como predicciones; (3) diseñar un estudio de inventario que no pueda dañar los sistemas que observa; (4) elegir métricas que resistan las formas más comunes de hacer que una migración parezca terminada; y (5) redactar un protocolo acotado que un comité de revisión pudiera aprobar. El capítulo se apoya en su experiencia de investigación de entrada y prepara la cartografía de la literatura del capítulo 2.

### 1.1 El objeto de estudio: una transición, no una primitiva

La mayor parte de la investigación en criptografía estudia un objeto que se queda quieto: un esquema, una reducción, una implementación. La investigación en seguridad poscuántica suele estudiar algo que se mueve. Las organizaciones están sustituyendo RSA, el Diffie–Hellman de cuerpo finito y los algoritmos de curva elíptica —que el algoritmo de Shor rompería en un ordenador cuántico tolerante a fallos suficientemente grande ([Shor 1997](https://doi.org/10.1137/S0097539795293172))— por algoritmos normalizados por su resistencia cuántica: ML-KEM en [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), ML-DSA en [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) y SLH-DSA en [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205), además de las firmas basadas en *hash* con estado LMS y XMSS perfiladas en [NIST SP 800-208](https://doi.org/10.6028/NIST.SP.800-208). Lo que se mide es una frontera móvil entre el uso vulnerable a la computación cuántica y el uso resistente a ella, a través de protocolos, productos y décadas de datos almacenados.

Eso cambia lo que cuenta como rigor. Una demostración por reducción puede comprobarse una vez. Una afirmación como «HRHN ha migrado el 80 % de su establecimiento de claves» depende de cómo se contó el «uso», de quién podía ver qué sistemas, de cuándo se tomó la instantánea y de si la negociación híbrida ocurrió de verdad o solo estaba configurada. La primera disciplina de este libro es, por tanto, saber qué objeto describe una frase: una primitiva, un protocolo, un despliegue, una organización o un ecosistema.

### 1.2 Una escalera de afirmaciones

Suba de peldaño en peldaño y no se salte nunca uno por escrito:

1. **Observación**: «El sensor pasivo registró 41 212 saludos TLS 1.3 en el segmento B entre el 1 y el 7 de marzo (sintético); el 63 % seleccionó el grupo X25519MLKEM768». Es una medición de un instrumento con nombre.
2. **Inferencia**: «La mayoría de las sesiones originadas en navegadores del segmento B están protegidas frente a la recogida de su intercambio de claves para descifrarlo más adelante (*harvest now, decrypt later*), suponiendo que ML-KEM-768 siga siendo seguro o que X25519 siga siendo seguro». Observe el supuesto explícito: un híbrido PQ/T ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)) está diseñado para seguir siendo seguro si se mantiene *cualquiera* de sus componentes.
3. **Afirmación**: «El inventario de doble fuente recupera el establecimiento de claves vulnerable a la computación cuántica en el corpus de HRHN con una exhaustividad de 0,91 (IC del 95 %: 0,88–0,94)». Una afirmación tiene alcance, incertidumbre y un método.
4. **Decisión**: «El grupo de dirección dio prioridad al concentrador de VPN». Una decisión la toman personas y puede ser acertada por razones ajenas a su evidencia.
5. **Exposición**: «Los estudios de imagen archivados que se cifraron con claves envueltas con RSA antes de 2026 seguirán siendo descifrables por un futuro CRQC mientras existan copias del texto cifrado». La exposición es la consecuencia que en último término le importa, y a menudo queda fuera de lo que puede ver cualquier sensor.

El fallo de integridad más común en este campo es saltarse peldaños: un escaneo de un fabricante (peldaño 1) se convierte en «la organización es segura frente a la computación cuántica» (un enunciado de exposición) sin ninguna inferencia, afirmación ni alcance entre medias.

### 1.3 Los plazos como supuestos

Hoy nadie puede observar cuándo existirá un ordenador cuántico criptográficamente relevante (CRQC). Lo que sí puede observarse es una sucesión de estimaciones de recursos publicadas. [Gidney y Ekerå (2021)](https://doi.org/10.22331/q-2021-04-15-433) estimaron que RSA-2048 podría factorizarse en unas ocho horas con veinte millones de cúbits ruidosos, con unos supuestos de *hardware* declarados; [Gidney (2025)](https://arxiv.org/abs/2505.15917) revisó la estimación a menos de un millón de cúbits ruidosos funcionando durante menos de una semana, de nuevo con supuestos explícitos sobre tasas de error, tiempo de ciclo y conectividad. Son resultados sobre *algoritmos y sobrecostes de la corrección de errores*, no previsiones del progreso de la ingeniería.

[Mosca (2018)](https://doi.org/10.1109/MSP.2018.3761723) planteó la pregunta de planificación como una desigualdad: si la vida útil de confidencialidad de los datos (*x*) más el tiempo de migración (*y*) supera el tiempo que falta hasta un CRQC (*z*), los datos cifrados hoy están en riesgo. Una tesis doctoral puede usar este marco, pero debe tratar *z* como un parámetro que se recorre sobre un intervalo e informar de cómo cambian las conclusiones, nunca como un único número tomado de una encuesta. El Lab 1 concreta esa sensibilidad.

Las fechas de las políticas son, a su vez, otro tipo de objeto. [NIST IR 8547 (borrador público inicial)](https://doi.org/10.6028/NIST.IR.8547.ipd) propone declarar obsoletos los algoritmos de clave pública vulnerables a la computación cuántica de 112 bits después de 2030 y prohibirlos después de 2035, y el [aviso CNSA 2.0](https://media.defense.gov/2022/Sep/07/2003071834/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS_.PDF) de la NSA fija sus propios objetivos de transición para los sistemas de seguridad nacional. Son decisiones de instituciones; cítelas como decisiones, con su estado, no como evidencia sobre el *hardware* cuántico.

### 1.4 No causar daño al observar la criptografía

La investigación de inventario toca sistemas en funcionamiento. El escaneo TLS activo de una red interna puede disparar la prevención de intrusiones, agotar las tablas de conexiones de dispositivos embebidos o, en un hospital, perturbar un dispositivo médico. La captura pasiva registra metadatos que pueden revelar quién habló con quién. El análisis de código puede sacar a la luz secretos. Por eso, un protocolo sólido especifica: autorización escrita del dueño del sistema; recogida pasiva por defecto; sondeo activo solo contra una lista acordada, con límite de tasa y fuera del horario clínico; captura limitada a los metadatos del saludo (sin carga útil de la aplicación ni claves privadas); borrado inmediato de cualquier credencial descubierta; y una persona con nombre con autoridad para detenerlo. Los experimentos de degradación —obligar a un cliente a pasar de los grupos híbridos a los clásicos— solo caben en un banco de pruebas aislado, porque debilitan deliberadamente una protección real.

Los principios del Informe Menlo ([Dittrich y Kenneally 2012](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf)) —respeto a las personas, beneficencia, justicia y respeto a la ley y al interés público— se corresponden directamente con estas decisiones. La beneficencia, en particular, significa que el hallazgo de un dispositivo heredado débil se comunica al dueño antes de publicarse.

### 1.5 Niveles de datos

Clasifique cada artefacto antes de que exista. **Nivel 0** (público): código, datos sintéticos, recuentos agregados. **Nivel 1** (restringido): metadatos de saludos desidentificados, con los nombres de equipo sustituidos por seudónimos estables. **Nivel 2** (confidencial): capturas de paquetes sin procesar, archivos de configuración, inventarios de certificados que revelan la arquitectura interna. **Nivel 3** (nunca se recoge): claves privadas, claves de sesión, carga útil de la aplicación, datos de pacientes. Un protocolo que no sabe decir a qué nivel pertenece un artefacto no está listo para la revisión.

En el Estudio Ciphertrail, la exportación seudonimizada de los saludos es de nivel 1 y las capturas sin procesar de los segmentos de HRHN se quedan en el nivel 2, en las instalaciones de HRHN. Cualquier credencial descubierta en el análisis de código pasa de inmediato al tratamiento de nivel 3: se borra, se avisa a su dueño y el incidente se registra sin el valor. El nivel se escribe en el propio archivo, además de en el protocolo.

### 1.6 Métricas que resisten la manipulación

«Porcentaje de sistemas migrados» es la métrica con más probabilidades de inducir a error. Puede aumentarse redefiniendo «sistema», contando los algoritmos configurados en lugar de los negociados o excluyendo los dispositivos que el escáner no alcanza. Prefiera métricas con un denominador que otra persona pueda auditar: la **exhaustividad** (*recall*) de los usos vulnerables a la computación cuántica frente a una verdad de referencia adjudicada; la **precisión** de los hallazgos comunicados; la **proporción híbrida negociada**, ponderada por la sensibilidad de los datos; la **proporción desconocida** —la fracción de activos cuya criptografía no pudo determinarse—, comunicada por separado en lugar de tratarse en silencio como segura; y el **tiempo de sustitución** de un algoritmo elegido, que mide la agilidad y no una migración puntual.

### 1.7 Ejemplo resuelto: la primera revisión del protocolo del Estudio Ciphertrail

El primer borrador del doctorando propone un escaneo activo de los 1200 servicios de HRHN e informa de un «% seguro frente a la computación cuántica». El comité de revisión (sintético) devuelve cinco objeciones. (a) El escaneo activo de la red segregada de dispositivos médicos no está justificado cuando basta la captura pasiva en el perímetro; el protocolo revisado restringe los sondeos activos a 140 servicios de TI y los programa. (b) «Seguro frente a la computación cuántica» no está definido; la revisión lo sustituye por la exhaustividad, la precisión y la proporción desconocida frente a una muestra adjudicada. (c) Las capturas de paquetes contendrían nombres de equipo que identifican a pacientes; la revisión seudonimiza en el sensor y mantiene las capturas sin procesar en el nivel 2, en las instalaciones de HRHN. (d) La fecha del CRQC se cita de un único blog; la revisión recorre *z* y cita estimaciones de recursos primarias. (e) No se nombra a nadie con autoridad para detener el estudio; la revisión nombra a la jefatura de ingeniería clínica de HRHN. Cada objeción obligó a bajar una afirmación hasta un peldaño que la evidencia pudiera sostener de verdad.

### 1.8 Actividad práctica — Lab 1: la desigualdad de Mosca con incertidumbre

Ejecute el *script* sin conexión con Python 3. Trata *z* como una distribución elegida solo con fines didácticos y pregunta con qué frecuencia *x* + *y* > *z* para cuatro clases de registros de HRHN.

```python
# Lab 1 (synthetic): Mosca's inequality x + y > z under uncertainty.
# x = years the data must stay confidential, y = years to migrate,
# z = years until a cryptographically relevant quantum computer (CRQC).
# The z distribution below is an ARBITRARY teaching assumption, not a forecast.
import random
random.seed(7)
def p_exposed(x, y, trials=20000, z_lo=8, z_hi=30):
    hits = 0
    for _ in range(trials):
        z = random.triangular(z_lo, z_hi, 15)  # mode 15 years: illustrative only
        if x + y > z:
            hits += 1
    return hits / trials
for name, x, y in [("appointment logs", 1, 4), ("lab results", 10, 4),
                   ("genomic archive", 50, 4), ("lab results, slow migration", 10, 9)]:
    print(f"{name:30s} x={x:2d} y={y:2d}  P(x+y>z) = {p_exposed(x, y):.3f}")
# Sensitivity: the same record class under a different z assumption
print("lab results, z in [15,40]     ", f"{p_exposed(10, 4, z_lo=15, z_hi=40):.3f}")
```

Salida esperada (con semilla):

```text
appointment logs               x= 1 y= 4  P(x+y>z) = 0.000
lab results                    x=10 y= 4  P(x+y>z) = 0.234
genomic archive                x=50 y= 4  P(x+y>z) = 1.000
lab results, slow migration    x=10 y= 9  P(x+y>z) = 0.631
lab results, z in [15,40]      0.000
```

Lea la salida como un enunciado sobre el *modelo*, no sobre el mundo. El archivo genómico está expuesto con cualquier supuesto, porque su vida útil de confidencialidad por sí sola supera cualquier *z* verosímil; la velocidad de migración no puede salvar unos datos que ya se han recogido. Los resultados de laboratorio pasan de 0,23 a 0,63 cuando la migración se ralentiza, y a 0 con un intervalo de *z* más optimista, que es justo la razón por la que una tesis debe publicar la sensibilidad y no una probabilidad única.

### 1.9 Errores comunes y límites

- Tratar una estimación de recursos como una fecha. Las estimaciones acotan el coste con unos supuestos; no ponen calendario a la ingeniería.
- Contar la configuración como negociación. Un servidor que ofrece un grupo híbrido no protege nada si ningún cliente lo selecciona.
- Denominadores silenciosos. Los activos que el escáner no ve deben aparecer como «desconocidos», no desaparecer.
- Observación dañina. Los escaneos activos y las pruebas de degradación en producción pueden causar interrupciones y debilitar la protección.
- La distribución del Lab 1 es arbitraria. Su valor es el método de análisis de sensibilidad, no las probabilidades.
- Convertir una tabla de sensibilidad en una única probabilidad de titular.

### Ejercicios — capítulo 1

Cada ejercicio se puntúa de 0 a 3: 0 = ausente o inseguro; 1 = parcialmente correcto con una laguna importante; 2 = correcto con lagunas menores; 3 = completo, acotado y justificado.

- **EX001 — Etiquetar la escalera.** Objetivo: separar los tipos de enunciado. Insumo: cinco frases del ejemplo resuelto. Restricción: usar solo las cinco etiquetas. Pasos: etiquetar cada una y después reescribir cualquier frase que se salte peldaños. Evidencia: una tabla etiquetada. Rúbrica: 3 = todas las etiquetas correctas y ambas reescrituras acotadas.
- **EX002 — Definir el objeto.** Objetivo: nombrar el objeto de una afirmación. Insumo: «Nuestro hospital está preparado para la PQC en un 80 %». Pasos: enumerar cuatro objetos que podría describir y la métrica que necesitaría cada uno. Evidencia: una tabla de cuatro filas. Rúbrica: 3 = objetos distintos y métricas auditables.
- **EX003 — Recorrer z.** Objetivo: análisis de sensibilidad. Insumo: el Lab 1. Pasos: cambiar la moda de *z* a 10 y a 25; informar de las cuatro clases de registros. Evidencia: una tabla y dos frases de interpretación. Rúbrica: 3 = ejecuciones correctas y una interpretación que no trata *z* como una previsión.
- **EX004 — Revisión de daños.** Objetivo: identificar los daños de la observación. Insumo: un plan para lanzar cada noche sondeos TLS activos contra todos los dispositivos médicos. Pasos: enumerar tres daños y un diseño más seguro para cada uno. Evidencia: tabla de daños. Rúbrica: 3 = daños realistas y alternativas que conservan la pregunta de investigación.
- **EX005 — Asignar niveles a los artefactos.** Objetivo: clasificación de datos. Insumo: captura de paquetes, CSV de saludos seudonimizado, inventario de certificados, cuaderno de análisis, una clave privada descubierta. Pasos: asignar los niveles 0–3 y el tratamiento de cada uno. Evidencia: una tabla. Rúbrica: 3 = la clave privada se borra y se comunica, no se almacena.
- **EX006 — Una métrica no manipulable.** Objetivo: diseño de métricas. Insumo: «% de sistemas migrados». Pasos: describir dos formas de manipularla y proponer una sustituta con un denominador auditable. Evidencia: la definición de la métrica. Rúbrica: 3 = la sustituta incluye la proporción desconocida.
- **EX007 — Protocolo acotado.** Objetivo: redactar un protocolo revisable. Pasos: una página que cubra la autorización, el modo de recogida, los niveles, la autoridad para detener, la divulgación y las métricas del Estudio Ciphertrail. Evidencia: el protocolo. Rúbrica: 3 = todos los elementos presentes y coherentes con 1.4–1.6.

### Síntesis del capítulo

La investigación en PQC mide una transición cuya magnitud más importante —cuándo existirá un CRQC— no puede observarse. Por eso el rigor procede de afirmaciones etiquetadas, de plazos tratados como supuestos que se recorren, de una observación que no puede dañar lo observado, de datos por niveles y de métricas cuyos denominadores puede auditar un lector adversarial.

### Siga estudiando — capítulo 01 de 08

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Seguridad cuántica y poscuántica: la frontera de la investigación

### Resultados de aprendizaje y conexión

Al terminar este capítulo usted podrá (1) describir las seis grandes familias de investigación en seguridad cuántica y poscuántica y el tipo de evidencia que produce cada una; (2) explicar qué dejó resuelto el proceso de normalización del NIST y qué dejó abierto; (3) evaluar un estudio de PQC en cuanto a validez de constructo, equidad de la línea base e independencia del corpus; (4) codificar un mapa de la literatura y localizar una celda vacía; y (5) formular una laguna falsable. Se apoya en la escalera de afirmaciones del capítulo 1 y aporta la pregunta que el capítulo 3 convierte en una contribución.

### 2.1 Por qué cuesta ver la frontera

El campo está repartido entre comunidades que rara vez se citan entre sí: investigadores de algoritmos cuánticos que publican en arXiv, criptógrafos en los foros de la IACR y en el [archivo ePrint de la IACR](https://eprint.iacr.org/), ingenieros de protocolos en el IETF y profesionales que escriben informes de fabricantes. El vocabulario varía —«quantum-safe», «quantum-resistant», «post-quantum» y «PQC-ready» se usan sin precisión—, de modo que una búsqueda por palabras clave pierde la mitad de la literatura. Construya una tabla de sinónimos antes de buscar y anote la fecha: en este campo, una revisión de hace dos años puede presentar como candidato destacado un esquema ya roto.

### 2.2 Familias de investigación

1. **Criptoanálisis cuántico y estimación de recursos.** El algoritmo de Shor rompe la factorización y los logaritmos discretos en tiempo polinómico en una máquina tolerante a fallos ([Shor 1997](https://doi.org/10.1137/S0097539795293172)); la búsqueda de Grover ofrece como mucho una aceleración cuadrática contra claves simétricas y funciones hash ([Grover 1996](https://doi.org/10.1145/237814.237866)), y por eso AES-256 y SHA-384/512 siguen siendo las opciones conservadoras en lugar de sustituirse. La investigación actual afina los recuentos de cúbits y de tiempo ([Gidney and Ekerå 2021](https://doi.org/10.22331/q-2021-04-15-433); [Gidney 2025](https://arxiv.org/abs/2505.15917)). Evidencia: análisis algorítmico bajo modelos de hardware explícitos.
2. **Problemas difíciles y esquemas.** *Retículos*: el aprendizaje con errores ([Regev 2009](https://doi.org/10.1145/1568318.1568324)) y sus variantes modulares sustentan ML-KEM y ML-DSA; Falcon (retículos NTRU) se está normalizando como FN-DSA. *Hash*: SLH-DSA (sin estado) y LMS/XMSS (con estado; [RFC 8554](https://www.rfc-editor.org/rfc/rfc8554.html), [RFC 8391](https://www.rfc-editor.org/rfc/rfc8391.html)) dependen solo de propiedades de las funciones hash. *Códigos*: Classic McEliece desciende de [McEliece (1978)](https://ipnpr.jpl.nasa.gov/progress_report2/42-44/44N.PDF); HQC fue seleccionado en marzo de 2025 para normalizarse como segundo KEM basado en un supuesto distinto ([NIST IR 8545](https://doi.org/10.6028/NIST.IR.8545)). *Multivariantes*: Rainbow, finalista de la tercera ronda, cayó ante un ataque de recuperación de clave ([Beullens 2022](https://eprint.iacr.org/2022/214)). *Isogenias*: SIKE cayó ante un ataque eficiente de recuperación de clave ([Castryck and Decru 2022](https://eprint.iacr.org/2022/975)). Evidencia: demostraciones, criptoanálisis, estimaciones de parámetros.
3. **Normas y políticas.** FIPS 203/204/205 (agosto de 2024), [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) sobre el uso de KEM (septiembre de 2025), el borrador del plan de transición [NIST IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) y la guía sobre agilidad de [NIST CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1). Evidencia: documentos con estado e historial.
4. **Protocolos híbridos.** Terminología en [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html); grupos híbridos de TLS 1.3 como X25519MLKEM768 en [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). Las preguntas de investigación atañen a la seguridad del combinador, el tamaño de los mensajes, la tolerancia de los equipos intermedios y la resistencia a la degradación. Evidencia: demostraciones, pruebas de interoperabilidad, medición en internet.
5. **Seguridad de la implementación.** Aritmética de tiempo constante, tratamiento de los fallos de descifrado, ataques por inyección de fallos y canales laterales en implementaciones de retículos; las fugas temporales por divisiones dependientes de secretos en varias implementaciones de Kyber se publicaron como «KyberSlash» ([Bernstein et al. 2024](https://eprint.iacr.org/2024/1049)). Evidencia: medición de laboratorio sobre versiones de código identificadas.
6. **Inventario y agilidad.** Cómo descubren las organizaciones dónde se usa la criptografía, cómo construyen una lista de materiales criptográficos (CBOM) y cómo hacen sustituibles los algoritmos. Evidencia: estudios de caso, bancos de pruebas, mediciones de campo; es la familia menos madura metodológicamente, como muestra el Lab 2.

### 2.3 Qué resolvió la normalización y qué no

El proceso del NIST resolvió una cartera: un KEM de propósito general (ML-KEM), una firma basada en retículos (ML-DSA) y una firma conservadora basada en hash (SLH-DSA), con Falcon y HQC por llegar ([NIST IR 8413](https://doi.org/10.6028/NIST.IR.8413) explica las selecciones de la tercera ronda). No resolvió el despliegue: cómo deben combinarse los secretos híbridos en cada protocolo, cómo deben transportar los certificados claves nuevas o compuestas, cómo deben arreglárselas los dispositivos limitados con firmas ML-DSA de 2.420 a 4.627 bytes (conjuntos de parámetros de FIPS 204) o cómo puede demostrar una organización que ha encontrado todos los usos vulnerables a la computación cuántica. Las roturas de Rainbow y SIKE en una fase tardía del proceso son el recordatorio permanente del campo de que la confianza en un problema difícil se gana a lo largo de años, y ese es el argumento científico a favor del despliegue híbrido y de la agilidad.

### 2.4 Evaluación: qué hace creíble un estudio de inventario o de migración a PQC

Hágase cinco preguntas. **Validez de constructo**: ¿«uso vulnerable» significa un algoritmo presente en el código, configurado, negociado o que protege datos de larga vida útil? **Verdad de referencia**: ¿quién la adjudicó, sin conocer el método evaluado? **Equidad de la línea base**: ¿configuró la herramienta rival alguien competente y con el mismo acceso? **Independencia del corpus**: ¿se ajustó el método sobre el mismo corpus en que se evaluó, o se validó en una segunda organización? **Incógnitas**: ¿se informa de los activos inalcanzables? Un estudio puede ser útil aunque falle en algunas, pero sus afirmaciones deben reducirse en consecuencia.

### 2.5 Ejemplo resuelto: evaluación de los estudios sintéticos Q1–Q8

Q1 y Q6 son estudios de caso de un solo hospital que informan de «se encontró el 94 % del uso de RSA» frente a una verdad de referencia producida por la misma herramienta: un razonamiento circular. Q2 y Q8 comparan escáneres sobre un corpus publicado por uno de los fabricantes: independencia «mismo fabricante». Q3 mide la negociación de grupos híbridos en un gran conjunto de sitios web públicos con un método documentado y es independiente. Q4 compara saludos híbridos en un laboratorio sin replicación externa. Q5 reproduce una fuga temporal en dos laboratorios independientes. Q7 es un artículo de posición sobre agilidad sin datos. Codificarlos (Lab 2) muestra que el inventario —la familia de la que más depende un programa de migración— no tiene ningún estudio validado sobre un corpus independiente. Esa celda vacía se convierte en la laguna del Estudio Ciphertrail.

### 2.6 Actividad práctica — Lab 2: codificar el mapa

```python
# Lab 2 (synthetic): code eight fictional studies Q1-Q8 and find empty cells.
studies = {  # id: (family, evidence type, corpus independence)
    "Q1": ("inventory", "single-org case", "none"),
    "Q2": ("inventory", "benchmark", "same-vendor"),
    "Q3": ("hybrid-protocol", "internet measurement", "independent"),
    "Q4": ("hybrid-protocol", "lab benchmark", "none"),
    "Q5": ("implementation", "side-channel lab", "independent"),
    "Q6": ("inventory", "single-org case", "none"),
    "Q7": ("agility", "position paper", "none"),
    "Q8": ("inventory", "benchmark", "same-vendor"),
}
families = sorted({f for f, _, _ in studies.values()})
indep = ["none", "same-vendor", "independent"]
print(f"{'family':16s}" + "".join(f"{i:>13s}" for i in indep))
for fam in families:
    row = [sum(1 for f, _, c in studies.values() if f == fam and c == i) for i in indep]
    print(f"{fam:16s}" + "".join(f"{n:13d}" for n in row))
gaps = [fam for fam in families
        if not any(f == fam and c == "independent" for f, _, c in studies.values())]
print("families with no independently validated study:", ", ".join(gaps))
```

Salida esperada:

```text
family                   none  same-vendor  independent
agility                     1            0            0
hybrid-protocol             1            0            1
implementation              0            0            1
inventory                   2            2            0
families with no independently validated study: agility, inventory
```

Amplíe el esquema de codificación con una cuarta columna para «verdad de referencia independiente de la herramienta» y vuelva a ejecutarlo; una laguna que sobrevive a dos codificaciones es más defendible que una que aparece con un único esquema.

La tabla hace visible la laguna de un vistazo: cuatro estudios de inventario, ninguno validado sobre un corpus independiente. La codificación vale lo que valen sus reglas, así que escriba qué cuenta como mismo fabricante o como independiente antes de codificar y pida a una segunda persona que codifique por separado los ocho estudios. Si el segundo codificador pasa un estudio a la columna de independientes, el enunciado de la laguna debe cambiar antes de entrar en la propuesta.

### 2.7 Una laguna falsable

Una laguna no es «nadie ha estudiado los inventarios de PQC». Es una ausencia concreta y comprobable: *ningún método de inventario publicado informa de la exhaustividad para los usos de establecimiento de claves y de firma vulnerables a la computación cuántica frente a una adjudicación ciega, sobre un corpus independiente de su corpus de desarrollo y con la proporción desconocida declarada.* El enunciado es falsable —un solo contraejemplo en la literatura lo cerraría— y nombra las mediciones que debe realizar una contribución.

Vuelva a contrastar la laguna con la literatura justo antes de la entrega, porque un contraejemplo publicado durante la tesis la cerraría. Anote la fecha y la búsqueda empleada en esa comprobación final. Si aparece un estudio que llena en parte la laguna, la contribución todavía puede sostenerse, pero debe reposicionarse como replicación o ampliación y no como primera medición.

### 2.8 Errores comunes y límites

- Citar como candidato un esquema roto porque la revisión es anterior a la rotura.
- Tratar a Grover como fatal para AES; en el modelo idealizado reduce a la mitad la longitud efectiva de la clave y es mucho más difícil de paralelizar.
- Confundir la distribución cuántica de claves (QKD) con la PQC. La QKD es una técnica de capa física con requisitos propios; varias agencias nacionales, entre ellas la [NSA](https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/), no la recomiendan para sistemas de seguridad nacional.
- Equivocarse sobre el estado de las normas: FN-DSA y HQC no eran normas definitivas el 12 de octubre de 2026.
- El corpus del Lab 2 es inventado; lo que se transfiere es el método, no los recuentos.

### Ejercicios — capítulo 2

Rúbrica de 0 a 3 como en el capítulo 1.

- **EX008 — Tabla de sinónimos.** Construya una tabla de doce términos con sinónimos y exclusiones para una búsqueda sobre inventario de PQC en arXiv, ePrint y el IETF. Evidencia: la tabla y dos cadenas de búsqueda. Rúbrica: 3 = cubre el vocabulario de fabricantes y de normas y excluye de forma deliberada los trabajos solo sobre QKD.
- **EX009 — Evidencia por familia.** Para cada una de las seis familias, nombre la forma de evidencia más sólida y una debilidad típica. Evidencia: tabla de seis filas. Rúbrica: 3 = debilidades específicas.
- **EX010 — Comprobación de estado.** Verifique en páginas primarias el estado actual de FIPS 206, de la norma HQC y de NIST IR 8547. Evidencia: tres citas con la fecha de comprobación. Rúbrica: 3 = solo fuentes primarias, fechas anotadas.
- **EX011 — Evaluar Q1.** Aplique a Q1 las cinco preguntas de evaluación. Evidencia: un párrafo por pregunta. Rúbrica: 3 = identifica la verdad de referencia circular y la afirmación que aún puede sostener.
- **EX012 — Recodificar el mapa.** Añada al Lab 2 la columna «verdad de referencia independiente» con sus propios juicios. Evidencia: diff del código y salida. Rúbrica: 3 = códigos justificados y laguna reexaminada.
- **EX013 — Lecciones de las roturas.** Explique en 250 palabras qué implican las roturas de Rainbow y SIKE para la arquitectura de la migración. Rúbrica: 3 = vincula las roturas con el despliegue híbrido y la agilidad sin exagerar.
- **EX014 — Formular la laguna.** Escriba en una frase una laguna falsable para una pregunta propia. Rúbrica: 3 = nombra la población, la medición y lo que la falsaría.

### Síntesis del capítulo

La frontera abarca seis familias con culturas de evidencia distintas. La normalización resolvió una cartera de algoritmos, no su despliegue. El inventario y la agilidad —las familias de las que más dependen las migraciones— tienen la evidencia más débil, y una laguna falsable en ese terreno es una contribución doctoral legítima.

### Siga estudiando — capítulo 02 de 08

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Propuesta de contribución original

### Resultados de aprendizaje y conexión

Al terminar este capítulo usted podrá (1) clasificar por tipo una contribución propuesta; (2) expresar un mecanismo que explique *por qué* debería funcionar un método; (3) redactar un modelo del observador, el equivalente en la investigación de inventarios de un modelo del atacante; (4) formular hipótesis con umbrales y condiciones de fracaso prerregistrados; y (5) seleccionar líneas base equitativas y nombrar explicaciones rivales. Convierte la laguna falsable del capítulo 2 en una propuesta que el capítulo 4 puede pilotar.

### 3.1 Tipos de contribución

Una contribución doctoral en este ámbito suele ser una de estas: un **método nuevo** (un procedimiento de inventario de doble fuente), una **medición nueva** (la primera estimación independiente de la exhaustividad de las herramientas de inventario), un **artefacto nuevo** (un corpus adjudicado abierto), un **resultado negativo** (mostrar que una métrica muy usada no es válida) o una **teoría** (un modelo de cómo la agilidad reduce el tiempo de sustitución). Declare un tipo principal; las contribuciones secundarias son bienvenidas, pero no deben diluir la afirmación que pondrá a prueba el tribunal. La contribución principal del Estudio Ciphertrail es una medición —la exhaustividad y la precisión independientes de un método de doble fuente—, con el corpus adjudicado como artefacto secundario.

### 3.2 El mecanismo: visibilidad complementaria

Un método merece estudiarse cuando hay una razón por la que debería funcionar. El análisis estático —escanear código fuente, manifiestos de dependencias, binarios y configuración— ve la criptografía que la organización construye y configura, pero no lo que hacen por dentro los equipos cerrados de los fabricantes. La telemetría pasiva —los metadatos de los saludos de TLS, SSH e IKE— ve lo que realmente se negocia en la red, también dentro de los equipos de los fabricantes, pero no ve nada de los datos en reposo ni de los dispositivos que nunca se comunican por un segmento supervisado. El mecanismo es la **visibilidad complementaria**: las dos fuentes fallan en clases de activos distintas, así que su unión debería elevar la exhaustividad donde una está ciega y la otra no, y no debería ayudar donde ambas están ciegas. Un mecanismo que predice dónde *fallará* el método vale más que uno que solo predice el éxito, porque hace falsable la afirmación.

### 3.3 Modelo del observador

Defina qué puede observar y qué no cada instrumento, igual que un modelo del atacante definiría capacidades:

| Observador | Ve | No ve |
|---|---|---|
| **S — estático** | Identificadores de algoritmos y llamadas a API en el código; versiones de bibliotecas; archivos de configuración; almacenes de certificados accesibles en disco | El interior de equipos cerrados; las elecciones de negociación en tiempo de ejecución; datos cifrados por terceros |
| **P — pasivo** | Grupos de TLS 1.3 y algoritmos de firma ofrecidos y seleccionados; cadenas de certificados en claro (TLS 1.2) o tal como las revelan los registros de los extremos; propuestas de SSH e IKE | Datos en reposo; tráfico en segmentos no supervisados; certificados cifrados de TLS 1.3 sin cooperación de los extremos |
| **G — verdad de referencia** | Adjudicación ciega por los ingenieros E01–E10 con la documentación de los dueños | Usos que ningún documento registra (se declaran como desconocidos) |

Fíjese en la sutileza de TLS 1.3: en TLS 1.3 los certificados viajan cifrados, de modo que un sensor puramente pasivo ve el grupo de intercambio de claves seleccionado, pero no el algoritmo de firma del servidor, salvo que se añada registro en los extremos. Una propuesta que ignorara esto exageraría la cobertura pasiva de las firmas.

### 3.4 Hipótesis y umbrales

Prerregistre, antes de ver el corpus principal:

- **H1** — La exhaustividad de doble fuente para los usos vulnerables a la computación cuántica supera a la exhaustividad solo estática en al menos 0,10 en el corpus HRHN (comparación pareada; el límite inferior del IC del 95 % de la diferencia es de al menos 0,10).
- **H2** — La precisión de doble fuente es de al menos 0,90 (los hallazgos pasivos pueden producir duplicados y atribuciones erróneas).
- **H3** — La ganancia de exhaustividad se concentra en los equipos de los fabricantes; en los usos de datos en reposo la ganancia es inferior a 0,02. *Esta hipótesis predice un fracaso.*
- **H4** — Los resultados se transfieren: en el corpus Marrow, intacto, con los umbrales y las reglas de fusión congelados, la ganancia de exhaustividad se mantiene en al menos 0,05.

Cada hipótesis tiene una condición declarada bajo la cual se rechaza. H3 se incluye porque, dado el mecanismo, sería sospechoso un método que «ayuda en todas partes».

### 3.5 Líneas base y explicaciones rivales

La línea base es el análisis solo estático configurado por un ingeniero competente con el mismo acceso, no un escáner deliberadamente débil. Una segunda línea base es la solo pasiva. Entre las explicaciones rivales de una ganancia observada están: hallazgos pasivos que duplican hallazgos estáticos con otros nombres (lo que infla los recuentos), adjudicadores influidos por qué herramienta encontró un elemento (lo que infla la precisión) y un corpus que sobrerrepresenta los equipos de los fabricantes (lo que infla la ganancia agregada). El diseño responde a cada una: identificadores canónicos por uso, adjudicación ciega e informes por clase.

Escriba cada explicación rival con el resultado que la respaldaría, para que el diseño pueda juzgarse antes de que lleguen los datos.

### 3.6 Ejemplo resuelto y Lab 3

La propuesta incluye un estudio de modelo para comprobar si H1 y H3 son siquiera plausibles antes de recoger ningún dato. Las probabilidades de detección son valores didácticos arbitrarios elegidos para encarnar el mecanismo.

```python
# Lab 3 - Ciphertrail Study (synthetic): static-only vs dual-source inventory recall.
# Each quantum-vulnerable "use" belongs to an asset class; each source detects it with a
# class-specific probability (ARBITRARY teaching values). Dual-source = union of detections.
import random
random.seed(2026)
classes = {  # class: (count, P(static detects), P(passive detects))
    "in-house code":       (420, 0.90, 0.55),
    "vendor appliance":    (260, 0.20, 0.80),
    "embedded/offline":    (180, 0.30, 0.10),
    "data at rest":        (140, 0.70, 0.00),
}
tot = {"static": 0, "dual": 0}; n_all = 0
print(f"{'class':18s}{'n':>5s}{'static':>8s}{'dual':>7s}")
for c, (n, ps, pp) in classes.items():
    s = d = 0
    for _ in range(n):
        hs, hp = random.random() < ps, random.random() < pp
        s += hs; d += (hs or hp)
    tot["static"] += s; tot["dual"] += d; n_all += n
    print(f"{c:18s}{n:5d}{s/n:8.2f}{d/n:7.2f}")
print(f"{'ALL':18s}{n_all:5d}{tot['static']/n_all:8.2f}{tot['dual']/n_all:7.2f}")
```

Salida esperada:

```text
class                 n  static   dual
in-house code       420    0.89   0.94
vendor appliance    260    0.18   0.84
embedded/offline    180    0.39   0.47
data at rest        140    0.69   0.69
ALL                1000    0.59   0.79
```

El modelo muestra el patrón previsto: una gran ganancia en los equipos de los fabricantes, casi ninguna en los datos en reposo y una ganancia agregada (0,20) que depende mucho de la mezcla de clases. Este último punto es una advertencia de diseño: una organización con menos equipos de fabricantes mostraría una ganancia agregada menor con el mismo método, así que la tesis debe informar de los resultados por clase y de la mezcla.

### 3.7 Errores comunes y límites

- Proponer un método sin mecanismo, de modo que cualquier resultado pueda racionalizarse.
- Hipótesis que no pueden fallar, como «la exhaustividad de doble fuente es al menos tan alta como la estática» (cierto por construcción para una unión).
- Líneas base débiles elegidas para que el método luzca.
- Ignorar que TLS 1.3 oculta los certificados a los observadores pasivos.
- Los estudios de modelo solo prueban coherencia interna; los números del Lab 3 son supuestos.

Cada error tiene un síntoma visible en una propuesta: un método descrito sin decir dónde debería fallar, una hipótesis que una unión garantiza, una línea base estática ejecutada con la configuración por defecto por alguien que no la conoce, o una afirmación de cobertura pasiva de las firmas con TLS 1.3. Busque esos síntomas en la propuesta antes de que lo haga el comité.

### Ejercicios — capítulo 3

- **EX015 — Tipo de contribución.** Clasifique la contribución de Ciphertrail y un planteamiento alternativo; argumente cuál encontraría más sólido un examinador. Rúbrica: 3 = justificado con referencia a la comprobabilidad.
- **EX016 — Mecanismo.** Escriba un párrafo de mecanismo para un método distinto (p. ej., inventario a partir de listas de materiales de software). Rúbrica: 3 = predice al menos una clase de fracaso.
- **EX017 — Modelo del observador.** Añada a la tabla de 3.3 un observador «E — registros de los extremos». Rúbrica: 3 = columnas de lo que ve y no ve exactas, incluido el coste para la privacidad.
- **EX018 — Hipótesis que puede fallar.** Reescriba «la doble fuente es mejor» como una hipótesis que pueda rechazarse. Rúbrica: 3 = umbral, comparación y condición de rechazo declarados.
- **EX019 — Mezcla de clases.** Modifique el Lab 3 para que haya 60 equipos de fabricantes en lugar de 260 (ajuste el código propio a 620). Informe de la ganancia agregada y explíquela. Rúbrica: 3 = ejecución correcta e interpretación vinculada a la mezcla de clases.
- **EX020 — Explicaciones rivales.** Nombre otras dos explicaciones rivales de una ganancia de exhaustividad y el rasgo del diseño que responde a cada una. Rúbrica: 3 = rivales plausibles, controles específicos.

### Síntesis del capítulo

Una contribución es defendible cuando su mecanismo predice tanto el éxito como el fracaso, su modelo del observador declara lo que cada instrumento no puede ver, sus hipótesis pueden rechazarse y sus líneas base son sólidas. El Estudio Ciphertrail propone la visibilidad complementaria y predice dónde no ayudará.

### Siga estudiando — capítulo 03 de 08

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Replicación de la línea base y piloto

### Resultados de aprendizaje y conexión

Al terminar este capítulo usted podrá (1) distinguir repetibilidad, reproducibilidad y replicabilidad; (2) diagnosticar por qué no se reproduce un resultado de inventario publicado; (3) verificar un instrumento con entradas conocidas antes de fiarse de su salida; (4) ajustar parámetros sin filtrar datos de prueba; y (5) ejecutar un piloto acotado que termine en una decisión explícita de seguir o no seguir. Aplica la propuesta del capítulo 3 antes del estudio principal del capítulo 5.

### 4.1 Términos

Según el vocabulario de [revisión y distintivos de artefactos](https://www.acm.org/publications/policies/artifact-review-and-badging-current) de la ACM: **repetibilidad**, el mismo equipo obtiene el mismo resultado con la misma configuración; **reproducibilidad**, un equipo distinto lo obtiene con los artefactos originales; **replicabilidad**, un equipo distinto lo obtiene con artefactos desarrollados de forma independiente. Una línea base doctoral debería al menos reproducirse, y el registro de la reproducción debería anotar cada desviación, incluidas las versiones de los escáneres, de los analizadores y del registro de grupos de TLS usado para clasificar los codepoints.

En el Estudio Ciphertrail, el trabajo sobre InvBench-22 es una reproducción, porque reutiliza el corpus publicado.

### 4.2 Diagnóstico de una reproducción fallida: InvBench-22

El artículo sintético InvBench-22 informa de que su escáner encontró «el 97 % de los activos vulnerables a la computación cuántica». El doctorando obtiene el corpus publicado y consigue un 61 %. Surgen tres causas, por orden de descubrimiento. Primera, **doble recuento**: el artículo contó hallazgos, no usos; el mismo servidor aparecía con un nombre corto, con un nombre completo y con dos direcciones IP, y cada uno se contaba como un acierto frente a un único elemento de la verdad de referencia. Segunda, **filtración de la verdad de referencia**: la verdad de referencia se construyó en parte a partir de la salida anterior del propio escáner, de modo que los elementos que el escáner no podía ver faltaban en el denominador. Tercera, **deriva del registro**: el clasificador del artículo era anterior a los codepoints definitivos de ML-KEM y etiquetaba como «desconocido» el codepoint híbrido obsoleto previo a la norma, que los autores después excluyeron. Nada de esto es fraude; cada causa es una decisión de medición que no se declaró. El registro de la reproducción enuncia cada causa, cuantifica su efecto e indica cuáles son inferencias y no hechos confirmados por los autores.

### 4.3 Verificar el instrumento

Antes de medir HRHN, verifique que el clasificador pasivo asigna correctamente cada codepoint de grupo admitido de TLS. El [registro de grupos admitidos de TLS](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-8) de la IANA enumera los codepoints; RFC 10024 define X25519MLKEM768, SecP256r1MLKEM768 y SecP384r1MLKEM1024. Las pruebas unitarias con entradas conocidas son la evidencia de validez más barata que puede tener una tesis. Importan dos reglas de diseño. Un codepoint desconocido debe clasificarse como *desconocido*, nunca como seguro. Y la identidad debe canonizarse antes de contar, de modo que un uso sea una fila.

### 4.4 Actividad práctica — Lab 4: verificar el clasificador y contar usos

```python
# Lab 4 (synthetic): verify the passive classifier and show how duplicate counting inflates recall.
# TLS supported-group codepoints (IANA registry): 0x001D x25519, 0x0017 secp256r1,
# 0x11EC X25519MLKEM768, 0x11EB SecP256r1MLKEM768, 0x11ED SecP384r1MLKEM1024,
# 0x6399 X25519Kyber768Draft00 (obsolete pre-standard codepoint).
GROUPS = {0x001D: "classical", 0x0017: "classical", 0x11EC: "hybrid", 0x11EB: "hybrid",
          0x11ED: "hybrid", 0x6399: "pre-standard hybrid"}
def classify(code):
    return GROUPS.get(code, "unknown")          # never default an unknown codepoint to "safe"
tests = [(0x001D, "classical"), (0x11EC, "hybrid"), (0x6399, "pre-standard hybrid"), (0xFFFF, "unknown")]
assert all(classify(c) == want for c, want in tests), "classifier unit test failed"
print("classifier unit tests: 4/4 pass")
# Synthetic handshake findings: (server pseudonym, port, selected group)
findings = [("srv-014", 443, 0x001D), ("srv-014", 443, 0x001D), ("SRV-014.halden.example", 443, 0x001D),
            ("srv-022", 8443, 0x11EC), ("srv-031", 443, 0x0017), ("srv-031", 443, 0x0017)]
truth_vulnerable = {("srv-014", 443), ("srv-031", 443), ("srv-040", 22)}   # adjudicated uses
def canon(host):
    return host.lower().split(".")[0]
raw_hits = sum(1 for h, p, g in findings if classify(g) == "classical")
uses = {(canon(h), p) for h, p, g in findings if classify(g) == "classical"}
print(f"raw classical findings: {raw_hits}  -> naive 'recall' {raw_hits}/{len(truth_vulnerable)} = {raw_hits/len(truth_vulnerable):.2f}")
print(f"canonical uses found:   {len(uses & truth_vulnerable)}  -> recall {len(uses & truth_vulnerable)/len(truth_vulnerable):.2f}")
```

Salida esperada:

```text
classifier unit tests: 4/4 pass
raw classical findings: 5  -> naive 'recall' 5/3 = 1.67
canonical uses found:   2  -> recall 0.67
```

Una «exhaustividad» superior a 1 es la señal más clara posible de un error de unidad, pero una inflación más sutil —por ejemplo, de 0,61 a 0,97— parece plausible y supera la revisión salvo que se declare la unidad de recuento. El uso SSH que falta en `srv-040` ilustra además el modelo del observador: el sensor de TLS no puede encontrarlo.

El laboratorio separa dos comprobaciones fáciles de confundir. Las pruebas unitarias muestran que el clasificador asigna correctamente los codepoints conocidos, incluido uno desconocido. El paso de recuento muestra cómo el mismo servidor, registrado repetidas veces y con dos nombres, puede inflar la exhaustividad. Mantenga ambas en el conjunto de pruebas del instrumento y ejecútelas antes de cada recogida, anotando junto a los resultados la fecha de recuperación del registro de la IANA.

### 4.5 Ajustar sin filtraciones

La regla de fusión tiene parámetros: cuánto tiempo sigue siendo válida una observación pasiva, cómo se emparejan los nombres de host con los repositorios de código y el umbral de confianza para atribuir un grupo negociado a un activo. Ajústelos sobre una **partición de desarrollo** (en el Estudio Ciphertrail, el hospital 1 de HRHN), congélelos y evalúe sobre los hospitales 2 y 3, reservados. Anote cada ejecución de ajuste, incluidas las abandonadas; un jardín de senderos que se bifurcan que se oculta es indistinguible del *p-hacking*.

Lleve un registro de ajuste con la fecha, los valores de los parámetros y el resultado en el hospital 1 de cada ejecución. Cuando las reglas queden congeladas, anote el hash de la configuración en ese mismo registro.

### 4.6 Un piloto acotado

El piloto dura dos semanas en un segmento de HRHN con 140 servicios. Criterios previos de seguir o no seguir: todas las pruebas unitarias del clasificador superadas; seudonimización verificada por una segunda persona en una muestra de 200 registros; ningún incidente operativo atribuible al estudio; concordancia entre adjudicadores (κ de Cohen) de al menos 0,70 en un conjunto de calibración de 60 elementos; y un protocolo que no requiera más de cuatro horas de ingeniero por cada 100 servicios. El piloto sintético cumple cuatro criterios, pero registra κ = 0,62, porque los adjudicadores discreparon sobre si un conjunto de cifrado con intercambio de claves RSA configurado pero nunca negociado es un «uso». La decisión es *seguir con enmienda*: el libro de códigos define ahora un uso como cualquier algoritmo que un par pueda alcanzar en la negociación, con una marca aparte para «configurado, no observado».

### 4.7 Errores comunes y límites

- Contar hallazgos en lugar de usos; declare siempre la unidad.
- Construir la verdad de referencia con la herramienta evaluada.
- Usar un registro de codepoints desactualizado; anote su fecha de recuperación.
- Ajustar sobre los datos de prueba, aunque sea de manera informal «mirando unos cuantos resultados».
- Un piloto sin criterios previos no puede fallar y, por tanto, enseña poco.

Cada error tiene una salvaguarda en este estudio: identificadores canónicos para los usos, adjudicación ciega respecto a la herramienta, un registro fechado, una partición por hospital con reglas congeladas y criterios previos para el piloto. La baja concordancia de 0,62 del piloto es un ejemplo de un criterio que cumple su función: obligó a enmendar el libro de códigos antes del estudio principal y no después.

### Ejercicios — capítulo 4

- **EX021 — Vocabulario.** Clasifique tres escenarios como repetibilidad, reproducibilidad o replicabilidad. Rúbrica: 3 = todos correctos, con una justificación de una línea cada uno.
- **EX022 — Registro de la reproducción.** Escriba la entrada del registro para la causa 2 de InvBench-22, separando la observación de la inferencia. Rúbrica: 3 = efecto cuantificado, inferencia etiquetada.
- **EX023 — Ampliar el clasificador.** Añada al Lab 4 pruebas unitarias para SecP384r1MLKEM1024 (0x11ED, ya presente en la tabla) y para un codepoint desconocido 0x0200. Rúbrica: 3 = las pruebas se superan y lo desconocido sigue siendo desconocido.
- **EX024 — Identidad canónica.** Proponga una regla de canonización de un uso que trate las direcciones IP, los alias y los balanceadores de carga. Rúbrica: 3 = aborda al menos un modo de fallo de la regla.
- **EX025 — Diseño de particiones.** Diseñe particiones de desarrollo y prueba para HRHN que eviten filtraciones cuando dos hospitales comparten una PKI. Rúbrica: 3 = identifica la filtración por PKI compartida y la mitiga.
- **EX026 — Seguir o no seguir.** Con κ = 0,62 y todos los demás criterios cumplidos, redacte el memorando de decisión. Rúbrica: 3 = decisión justificada, enmienda específica, criterio de nueva prueba declarado.

### Síntesis del capítulo

Las líneas base se reproducen antes de superarlas; los instrumentos se verifican con entradas conocidas; la unidad de recuento se declara; el ajuste se separa de la prueba; y un piloto existe para poder fallar. La exhaustividad inflada de InvBench-22 provenía de tres decisiones de medición no declaradas, no del escáner.

### Siga estudiando — capítulo 04 de 08

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](../../en/book/MANUSCRIPT.md#ch-05)

<a id="worked-results"></a>

## Resultados resueltos

Las respuestas son respuestas modelo para la autoevaluación; una respuesta distinta que cumpla la rúbrica puntúa igual. Los números sintéticos proceden de los laboratorios con semilla.

**EX001.** (1) observación: el recuento del sensor; (2) inferencia: la protección de las sesiones del segmento B con el supuesto de que basta cualquiera de los componentes; (3) afirmación: la exhaustividad con su IC; (4) decisión: la prioridad dada a la VPN; (5) exposición: las imágenes archivadas. Una frase que se salta peldaños, como «el segmento B es seguro frente a la computación cuántica», se reescribe así: «el 63 % de los saludos observados en el segmento B durante la ventana negoció un grupo híbrido PQ/T; no se midieron los demás segmentos, las firmas ni los datos almacenados».

**EX002.** Primitiva (¿los algoritmos desplegados son PQC normalizada? métrica: lista de algoritmos frente a FIPS 203/204/205), protocolo (¿las configuraciones de TLS/IKE ofrecen grupos híbridos? métrica: proporción de configuraciones), despliegue (¿se negocian? métrica: proporción negociada por sensibilidad), organización (¿se encuentran y sustituyen los usos vulnerables? métrica: exhaustividad, proporción desconocida, tiempo de sustitución). «Preparado en un 80 %» no significa nada hasta que se nombran un objeto y su denominador.

**EX003.** Con moda 10: resultados de laboratorio 0,415 y migración lenta 0,723; con moda 25: 0,097 y 0,325; los registros de citas se quedan en 0 y el archivo genómico en 1. Con moda 10, la última línea «[15,40]» (0,101) no es válida, porque una moda fuera del intervalo incumple la definición de la distribución triangular, lo que recuerda que hay que validar las entradas del modelo; con moda 25 es válida y sigue imprimiendo 0,000. Interpretación: la ordenación de las clases de registros es estable aunque las probabilidades varíen en un factor de cuatro, así que la priorización (primero la genómica, después los resultados de laboratorio) es más robusta que cualquier probabilidad aislada.

**EX004.** Daños: inestabilidad o reinicio del dispositivo durante la atención; avalanchas de alarmas que insensibilizan al equipo de seguridad; debilitamiento de la protección si los sondeos activan modos de reserva. Alternativas: captura pasiva en el perímetro de la red médica; documentación del fabricante y declaraciones de compra; una unidad de cada modelo de dispositivo en un banco de pruebas para las pruebas activas.

**EX005.** Captura de paquetes, nivel 2 (se guarda en las instalaciones del dueño); CSV seudonimizado, nivel 1; inventario de certificados, nivel 2 (revela la arquitectura); cuaderno, nivel 0 siempre que solo lea entradas de nivel 0/1; clave privada, nivel 3: no copiarla, avisar al dueño para que la rote y registrar solo el hecho del descubrimiento.

**EX006.** Manipulación: redefinir «sistema» para excluir los casos difíciles; contar grupos híbridos configurados que nunca se negocian. Sustituta: la exhaustividad de los usos vulnerables a la computación cuántica adjudicados, con la proporción desconocida comunicada por separado, y la proporción híbrida negociada ponderada por la vida útil de los datos.

**EX007.** Una respuesta completa nombra la autorización escrita de HRHN, la recogida con prioridad pasiva y sondeos activos limitados a 140 servicios de TI en ventanas programadas, los niveles 0–3 con el nivel 3 nunca recogido, la jefatura de ingeniería clínica como autoridad para detener el estudio, la divulgación primero al dueño y la exhaustividad, la precisión y la proporción desconocida frente a una adjudicación ciega.

**EX008.** Los términos incluyen *post-quantum*, *quantum-resistant*, *quantum-safe*, *PQC migration*, *cryptographic inventory*, *CBOM*, *crypto-agility*, *hybrid key exchange*, *ML-KEM/Kyber*, *ML-DSA/Dilithium*, *SLH-DSA/SPHINCS+*, *harvest now decrypt later*; exclusión: artículos solo sobre QKD y sobre la capa física de redes cuánticas, salvo que traten la migración. Las cadenas de búsqueda combinan un término de inventario AND un término de PQC, con fecha de recuperación.

**EX009.** Criptoanálisis: cotas algorítmicas / los supuestos de hardware envejecen. Esquemas: demostraciones y criptoanálisis / la confianza crece despacio y las roturas llegan tarde. Normas: estado autorizado / los documentos cambian. Protocolos híbridos: medición de interoperabilidad / los resultados de laboratorio no ven los equipos intermedios. Implementación: fugas reproducibles en laboratorio / ligadas a versiones de código. Inventario: datos de campo / verdad de referencia circular y denominadores ausentes.

**EX010.** A 12 de octubre de 2026: FIPS 206 (FN-DSA) en desarrollo; HQC seleccionado (NIST IR 8545, marzo de 2025) con una norma en desarrollo; NIST IR 8547 en borrador público inicial (noviembre de 2024). Consulte la [página del proyecto PQC del NIST](https://csrc.nist.gov/projects/post-quantum-cryptography) y anote la fecha de recuperación; un lector posterior debe contar con cambios.

**EX011.** Constructo: «uso de RSA» sin definir. Verdad de referencia: producida por la misma herramienta, circular. Línea base: ninguna. Independencia: un solo centro. Incógnitas: no se informa de ellas. Q1 todavía puede sostener «la herramienta encontró estas instancias», no ninguna cifra de exhaustividad.

**EX012.** Añadir la columna da «no» para Q1, Q2, Q6 y Q8 y «sí» o «no aplicable» para los demás; el inventario sigue sin un estudio que tenga a la vez corpus independiente y verdad de referencia independiente, así que la laguna sobrevive a dos codificaciones.

**EX013.** Dos finalistas o alternativas cayeron ante ataques clásicos descubiertos tarde en un proceso público, de modo que la confianza en un supuesto más reciente es provisional. Por eso las arquitecturas deben combinar supuestos (híbridos PQ/T durante la transición), mantener una segunda familia normalizada (firmas basadas en hash, HQC junto a ML-KEM) y convertir la sustitución de algoritmos en algo rutinario (agilidad). Las roturas no implican que ML-KEM sea débil.

**EX014.** Modelo: «Ningún estudio publicado mide el tiempo de sustitución de un algoritmo de firma en una PKI con más de 1.000 certificados bajo un mecanismo de agilidad documentado; una sola medición de ese tipo falsaría la laguna».

**EX015.** Principal: medición (exhaustividad y precisión independientes); alternativa: método nuevo. El planteamiento como medición es más sólido porque puede contrastarse con un umbral explícito sobre un corpus independiente; el planteamiento como «método» invita a la réplica «cualquier unión ayuda».

**EX016.** El inventario basado en SBOM ve las bibliotecas y versiones declaradas; predice una exhaustividad alta para el software propio con canalizaciones de compilación y fracaso para los equipos sin SBOM, para los algoritmos seleccionados en tiempo de ejecución por configuración y para los datos en reposo.

**EX017.** Los registros de los extremos ven los algoritmos de certificado y de firma del lado del servidor en TLS 1.3, las elecciones de cifrado y las identidades de los clientes; no ven los dispositivos sin registro ni los clientes no gestionados; el coste para la privacidad es mayor porque los registros pueden vincular usuarios con servicios, así que conviene seudonimizar en origen.

**EX018.** «En los elementos reservados de HRHN, la diferencia pareada de exhaustividad (doble − estática) es de al menos 0,10; se rechaza si el límite inferior del IC del 95 % es inferior a 0,10». Cualquier umbral que pueda rechazarse obtiene la puntuación.

**EX019.** Agregado estático 0,73 frente a doble 0,81: ganancia de 0,08 en lugar de 0,20, porque la clase que más se beneficia se ha reducido. El método no cambió; cambió la mezcla, así que deben informarse los resultados por clase.

**EX020.** Rival: sensores pasivos colocados después de incidentes anteriores, de modo que la ganancia observada refleja dónde ya se conocían problemas (control: ubicación de los sensores documentada y analizada). Rival: línea base estática ejecutada con un acceso desactualizado a los repositorios (control: misma fecha de instantánea de acceso para ambas).

**EX021.** El mismo laboratorio vuelve a ejecutar su canalización = repetibilidad; otro equipo usa el corpus y el código publicados = reproducibilidad; otro equipo construye su propio sensor y su propio corpus = replicabilidad.

**EX022.** «Observación: 214 de los 1.000 elementos de la verdad de referencia del corpus publicado llevan el identificador interno de hallazgo del escáner. Inferencia (no confirmada por los autores): la verdad de referencia se sembró a partir de la salida del escáner, excluyendo los elementos que el escáner no podía ver; por tanto, la exhaustividad está sobrestimada. Efecto: recalcular solo frente a los elementos documentados por los dueños reduce la exhaustividad de 0,97 a 0,71».

**EX023.** Añada las pruebas `(0x11ED, "hybrid")` y `(0x0200, "unknown")`; la tabla ya asigna 0x11ED, las seis pruebas se superan y los valores desconocidos nunca se asignan a seguro.

**EX024.** Uso canónico = (registro del dueño del servicio, nombre lógico del servicio, protocolo, puerto). Asigne las IP mediante el registro de activos, los alias mediante la resolución de CNAME del DNS registrada en el momento de la instantánea y trate una VIP de balanceador de carga como un uso por grupo de servidores solo si los servidores difieren en su criptografía. Modo de fallo: las VIP compartidas con servidores heterogéneos necesitan datos de los extremos.

**EX025.** Los hospitales que comparten una CA emisora filtran patrones de certificados entre particiones; particione por dominio de PKI, o mantenga los certificados de PKI compartida íntegramente en la partición de prueba y ajuste solo con rasgos ajenos a la PKI.

**EX026.** «Seguir con enmienda: κ 0,62 se atribuye a la definición de "uso". Libro de códigos enmendado (alcanzable en la negociación; marca configurado-no-observado). Nueva prueba con 60 elementos de calibración nuevos; continuar si κ ≥ 0,70».

<a id="references"></a>

## Referencias

Todos los enlaces se comprobaron el 12 de octubre de 2026. El estado de las normas cambia; vuelva a verificarlo. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Beullens, W. (2022). Breaking Rainbow takes a weekend on a laptop. IACR ePrint 2022/214. <https://eprint.iacr.org/2022/214>
- Bernstein, D. J., et al. (2024). KyberSlash: Exploiting secret-dependent division timings in Kyber implementations. IACR ePrint 2024/1049. <https://eprint.iacr.org/2024/1049>
- Castryck, W., and Decru, T. (2022). An efficient key recovery attack on SIDH. IACR ePrint 2022/975. <https://eprint.iacr.org/2022/975>
- Dittrich, D., and Kenneally, E. (2012). The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research. U.S. DHS.
- Driscoll, F., Parsons, M., and Hale, B. (2025). Terminology for Post-Quantum Traditional Hybrid Schemes. RFC 9794. <https://www.rfc-editor.org/rfc/rfc9794.html>
- Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits. arXiv:2505.15917. <https://arxiv.org/abs/2505.15917>
- Gidney, C., and Ekerå, M. (2021). How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits. *Quantum* 5, 433. <https://doi.org/10.22331/q-2021-04-15-433>
- Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *Proc. STOC '96*. <https://doi.org/10.1145/237814.237866>
- Hülsing, A., et al. (2018). XMSS: eXtended Merkle Signature Scheme. RFC 8391. <https://www.rfc-editor.org/rfc/rfc8391.html>
- McGrew, D., Curcio, M., and Fluhrer, S. (2019). Leighton-Micali Hash-Based Signatures. RFC 8554. <https://www.rfc-editor.org/rfc/rfc8554.html>
- McEliece, R. J. (1978). A public-key cryptosystem based on algebraic coding theory. JPL DSN Progress Report 42-44. <https://ipnpr.jpl.nasa.gov/progress_report2/42-44/44N.PDF>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST (2024). FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard. <https://doi.org/10.6028/NIST.FIPS.203>
- NIST (2024). FIPS 204, Module-Lattice-Based Digital Signature Standard. <https://doi.org/10.6028/NIST.FIPS.204>
- NIST (2024). FIPS 205, Stateless Hash-Based Digital Signature Standard. <https://doi.org/10.6028/NIST.FIPS.205>
- NIST (2020). SP 800-208, Recommendation for Stateful Hash-Based Signature Schemes. <https://doi.org/10.6028/NIST.SP.800-208>
- NIST (2025). SP 800-227, Recommendations for Key-Encapsulation Mechanisms. <https://doi.org/10.6028/NIST.SP.800-227>
- NIST (2022). IR 8413, Status Report on the Third Round of the NIST PQC Standardization Process. <https://doi.org/10.6028/NIST.IR.8413>
- NIST (2025). IR 8545, Status Report on the Fourth Round of the NIST PQC Standardization Process. <https://doi.org/10.6028/NIST.IR.8545>
- NIST (2024). IR 8547 (initial public draft), Transition to Post-Quantum Cryptography Standards. <https://doi.org/10.6028/NIST.IR.8547.ipd>
- NIST (2025, updated 2026). CSWP 39 upd1, Considerations for Achieving Crypto Agility. <https://doi.org/10.6028/NIST.CSWP.39-upd1>
- NSA (2022). Announcing the Commercial National Security Algorithm Suite 2.0. Cybersecurity advisory.
- Regev, O. (2009). On lattices, learning with errors, random linear codes, and cryptography. *Journal of the ACM* 56(6). <https://doi.org/10.1145/1568318.1568324>
- Shor, P. W. (1997). Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
- Kwiatkowski, K., Kampanakis, P., Westerbaan, B., and Stebila, D. (2026). Post-Quantum Traditional (PQ/T) Hybrid Key Agreement Mechanisms for TLS 1.3. RFC 10024. <https://www.rfc-editor.org/rfc/rfc10024.html>
- IANA. Transport Layer Security (TLS) Parameters — Supported Groups registry. <https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml>
- ACM. Artifact Review and Badging, current version. <https://www.acm.org/publications/policies/artifact-review-and-badging-current>
