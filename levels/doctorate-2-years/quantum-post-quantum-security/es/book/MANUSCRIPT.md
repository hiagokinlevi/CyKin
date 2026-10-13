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
2. [Seguridad cuántica y poscuántica: frontera de la investigación](../../en/book/MANUSCRIPT.md#ch-02)
3. [Propuesta de contribución original](../../en/book/MANUSCRIPT.md#ch-03)
4. [Replicación de las líneas base y piloto](../../en/book/MANUSCRIPT.md#ch-04)
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

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](../../en/book/MANUSCRIPT.md#ch-02)

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
