# Seguridad de la IA y del aprendizaje automático: guía de investigación de maestría

- Idioma: español neutro (`es`); programa de maestría, dos años; aproximadamente 1.600 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–8 de 8 tienen texto didáctico de autor; los ejercicios EX001–EX050 tienen sus resultados resueltos correspondientes con rúbricas de 0 a 3; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas impresas proceden de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4. Que los capítulos estén en borrador no significa que el libro esté terminado.
- Público: investigadores principiantes que diseñarán, realizarán y defenderán un trabajo de fin de máster supervisado en seguridad de la IA y del aprendizaje automático.
- Relación con los libros vecinos: el [libro de posgrado](../../../../postgraduate-2-years/ai-security/en/book/MANUSCRIPT.md) se centra en la práctica; el [libro de doctorado](../../../../doctorate-2-years/ai-security/es/book/MANUSCRIPT.md) exige una contribución original puesta a prueba de forma independiente. **Este libro enseña el ciclo completo de investigación una vez, bajo supervisión**: pregunta, literatura, diseño, explicaciones alternativas, piloto, análisis, redacción y defensa.
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título y no concede autorización para probar sistemas reales. Todas las organizaciones, personas, conjuntos de datos y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Cada capítulo tiene resultados de aprendizaje, texto didáctico, un ejemplo resuelto, actividades de práctica, errores y límites, ejercicios puntuados de 0 a 3 (0 = ausente o inseguro; 1 = laguna importante; 2 = lagunas menores; 3 = completo y justificado), una síntesis y un bloque **Siga estudiando**. Los laboratorios son deterministas, se ejecutan sin conexión con `python3 file.py` e imprimen los resultados que se muestran bajo *Salida esperada*. Son modelos de juguete elegidos para hacer medible un concepto, no evidencia sobre sistemas en producción.

### El ejemplo de referencia (sintético): un trabajo de fin de máster sobre privacidad en Harbourline

> **Caso sintético — ficción.** *Leo Brandt* es un estudiante de maestría en prácticas en **Harbourline Mutual**, una aseguradora inventada que ajusta finamente un clasificador de texto para clasificar las notas de siniestros. El trabajo de fin de máster de Leo pregunta si *eliminar los registros de entrenamiento duplicados* reduce la fuga por inferencia de pertenencia del modelo ajustado con un coste de exactitud aceptable. Todos los registros son sintéticos; no se usa ningún dato real de reclamantes; los experimentos se ejecutan sobre una copia aislada. Todos los números sobre Harbourline son inventados.

### Política de fuentes

Las fuentes se comprobaron el 12 de octubre de 2026: NIST [AI 100-1](https://doi.org/10.6028/NIST.AI.100-1), [AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) y [AI 100-2 E2025](https://doi.org/10.6028/NIST.AI.100-2e2025); el [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [MITRE ATLAS](https://atlas.mitre.org/); el [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj); e [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html). Los artículos se citan por su identificador de arXiv, y cada uno se abrió y se comprobó su título.

## Contenido

| Etapa | Capítulo |
|---|---|
| 1 | [1 Pregunta de investigación y método de revisión de la literatura](#ch-01) |
| 1 | [2 Seguridad de la IA y del aprendizaje automático: seminario avanzado](#ch-02) |
| 2 | [3 Diseño del estudio, ética y reproducibilidad](../../en/book/MANUSCRIPT.md#ch-03) |
| 2 | [4 Seguridad de la IA y del aprendizaje automático: explicaciones alternativas](../../en/book/MANUSCRIPT.md#ch-04) |
| 3 | [5 Propuesta y piloto](../../en/book/MANUSCRIPT.md#ch-05) |
| 3 | [6 Recogida y análisis de datos](../../en/book/MANUSCRIPT.md#ch-06) |
| 4 | [7 Redacción del trabajo de fin de máster y limitaciones](../../en/book/MANUSCRIPT.md#ch-07) |
| 4 | [8 Revisión independiente y defensa](../../en/book/MANUSCRIPT.md#ch-08) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Pregunta de investigación y método de revisión de la literatura

### Resultados de aprendizaje

Usted será capaz de (1) pasar de un tema a una pregunta investigable con una unidad de análisis clara; (2) realizar una búsqueda bibliográfica sistemática y documentada en foros de seguridad y de aprendizaje automático y en servidores de preprints; (3) extraer la evidencia a una matriz de comparación; (4) juzgar la calidad de las fuentes, incluidos los preprints y el material de proveedores; y (5) escribir una sección breve y honesta sobre el estado de la cuestión.

### 1.1 Del tema a la pregunta

«La privacidad de la IA» es un tema. «¿Reduce la eliminación de registros de entrenamiento duplicados la ventaja de la inferencia de pertenencia contra un clasificador de texto ajustado finamente, y con qué coste de exactitud?» es una pregunta. Una pregunta investigable nombra un *sistema* (clasificador ajustado finamente), una *intervención o factor* (deduplicación), un *resultado* (ventaja de la inferencia de pertenencia; exactitud) e implícitamente una *comparación* (con frente a sin). El acrónimo PICO de la medicina basada en la evidencia (población, intervención, comparación y resultado, por sus siglas en inglés) es una plantilla útil. Compruebe pronto la viabilidad: ¿puede obtener o sintetizar datos, dispone de capacidad de cómputo, puede hacerse el trabajo en el plazo, y es ético y está autorizado?

### 1.2 Una búsqueda documentada

La literatura sobre seguridad de la IA está repartida entre congresos de seguridad (IEEE S&P, USENIX Security, ACM CCS, NDSS), congresos de aprendizaje automático (NeurIPS, ICML, ICLR) y preprints de arXiv, además de los marcos de NIST, OWASP y MITRE. Redacte un protocolo de búsqueda: bases de datos (por ejemplo, DBLP, Google Scholar, arXiv, ACM Digital Library), cadenas de búsqueda, intervalo de fechas, criterios de inclusión y exclusión, y la fecha en que buscó. Siga las citas hacia delante y hacia atrás a partir de artículos semilla; para la inferencia de pertenencia, Shokri et al. (arXiv:1610.05820) es la semilla evidente. Registre los recuentos en cada etapa (encontrados, cribados, incluidos) para que un lector pueda repetir la búsqueda. Es una versión ligera de la práctica de la revisión sistemática; le protege de citar solo lo que ya conocía.

### 1.3 Extracción de la evidencia

Construya una matriz con una fila por artículo y columnas para: modelo de amenaza (conocimiento y acceso del atacante), tipo y tamaño del modelo, datos, métrica, resultado principal, defensa probada, evaluación adaptativa, disponibilidad del código y limitaciones. En trabajos sobre privacidad, anote si el artículo informa la tasa de verdaderos positivos con una tasa de falsos positivos baja o solo la exactitud media o el AUC; lo primero importa porque un ataque que identifica con confianza a unas pocas personas es un daño real aunque su rendimiento medio parezca modesto. La matriz revelará desacuerdos y lagunas que se convertirán en su contribución.

### 1.4 Juzgar las fuentes

Ordene la evidencia según lo comprobable que sea. Los artículos revisados por pares con código publicado son los más sólidos; los preprints pueden ser excelentes, pero no están revisados; los blogs de proveedores y el marketing son afirmaciones que hay que verificar, no evidencia. Las normas y los marcos (NIST AI 100-1, AI 100-2 E2025, ISO/IEC 42001) definen vocabulario y expectativas; no son resultados experimentales. Cuando un preprint aparece después en un foro, cite la versión final si difiere. Nunca cite un artículo que no haya abierto y nunca invente un DOI: si no encuentra un identificador, cite el título, los autores, el año y la URL que realmente utilizó.

### 1.5 Ejemplo resuelto (caso sintético de Harbourline)

El protocolo de Leo buscó en DBLP, arXiv y Google Scholar el 2 de febrero con cadenas que combinaban "membership inference", "fine-tuning", "deduplication" y "memorization", entre 2016 y 2026, incluyendo estudios empíricos sobre clasificadores o modelos de lenguaje y excluyendo los artículos sin un modelo de amenaza declarado. De 212 resultados, 61 superaron el cribado por título, 24 el cribado por resumen y 17 la lectura del texto completo. La matriz mostró que la mayoría de los estudios informaban el AUC, pocos informaban la TPR con una FPR del 0,1 %, y solo tres probaban directamente la deduplicación, todos sobre modelos de lenguaje generativos y ninguno sobre clasificadores ajustados finamente. El párrafo de Leo sobre el estado de la cuestión lo dijo con claridad y citó a Carlini et al. (arXiv:2012.07805) sobre la extracción literal como el daño que motiva el estudio.

El laboratorio de inferencia de pertenencia muestra la idea central que Leo estudiará: cuando un modelo memoriza en la práctica sus registros de entrenamiento (k = 1), la pertenencia es detectable; cuando generaliza (k mayor), la señal se desvanece.

```python
"""Lab M: membership inference against an overfit 1-nearest-neighbour 'model'
that returns a confidence score. Synthetic records only; teaching model."""
import random, math
rng = random.Random(5)
def rec(): 
    y = rng.random() < 0.5
    return [rng.gauss(0.6 if y else -0.6, 1.0) for _ in range(4)], int(y)
members = [rec() for _ in range(150)]; nonmembers = [rec() for _ in range(150)]
def confidence(x, y, k):
    # k-NN vote share for the true label, computed over the training set
    d = sorted((sum((a-b)**2 for a, b in zip(x, m)), my) for m, my in members)
    return sum(1 for _, my in d[:k] if my == y)/k
def auc(pos, neg):
    s = sum((p > n) + 0.5*(p == n) for p in pos for n in neg)
    return s/(len(pos)*len(neg))
for k in (1, 5, 25):
    pos = [confidence(x, y, k) for x, y in members]
    neg = [confidence(x, y, k) for x, y in nonmembers]
    best = max(sum(p >= t for p in pos)/len(pos) - sum(n >= t for n in neg)/len(neg)
               for t in sorted(set(pos + neg)))
    print(f"k={k:2d} attack_auc={auc(pos, neg):.3f} best_advantage={best:.3f}")
```

Salida esperada:

```text
k= 1 attack_auc=0.600 best_advantage=0.200
k= 5 attack_auc=0.521 best_advantage=0.073
k=25 attack_auc=0.520 best_advantage=0.060
```

### 1.6 Actividades de práctica

1. Escriba su tema y luego tres preguntas candidatas en forma PICO; elija una y justifique su viabilidad. 2. Redacte un protocolo de búsqueda y aplíquelo, registrando los recuentos. 3. Construya una matriz de evidencia de diez filas. Para las preguntas, nombre el sistema, la intervención o factor, la comparación y el resultado, como hace la pregunta de Leo. Juzgue la viabilidad según los datos, el cómputo, el tiempo y la ética, y descarte cualquier pregunta que no supere alguno de ellos. Para la búsqueda, registre las bases de datos, las cadenas, las fechas y los recuentos en cada etapa, para que otra persona pueda repetirla. En la matriz, incluya si cada artículo informa la TPR con una FPR baja.

### 1.7 Errores y límites

Cinco errores se repiten, y cada uno debilita el trabajo de fin de máster desde el principio:

- Preguntas demasiado amplias para responderlas en un trabajo de fin de máster; una pregunta amplia no puede responderse en el plazo.
- Búsquedas que se detienen en la primera página de un buscador; una búsqueda que se detiene pronto pierde trabajos como los tres estudios sobre deduplicación que encontró Leo.
- Tratar el blog de un proveedor como evidencia; el blog de un proveedor es una afirmación que hay que verificar.
- Citar artículos que no ha leído, o fabricar identificadores; los identificadores no citados o inventados dañan la confianza en todas las demás citas.
- Informar solo de promedios en los ataques contra la privacidad; los promedios ocultan a las pocas personas que un ataque identifica con confianza, que es el daño que estudia Leo.

### Ejercicios — capítulo 1

- **EX001 — PICO.** Escriba una pregunta PICO sobre las defensas contra la inyección de instrucciones (*prompt injection*). Rúbrica: 3 = los cuatro elementos son concretos y viables; 2 = uno es vago; 1 = faltan dos; 0 = solo el tema.
- **EX002 — Protocolo de búsqueda.** Enumere seis elementos de un protocolo de búsqueda documentado. Rúbrica: 3 = fuentes, cadenas, fechas, criterios, fecha de búsqueda, recuentos; 2 = cuatro; 1 = dos; 0 = ninguno.
- **EX003 — Columnas de la matriz.** Nombre seis columnas de la matriz para una revisión de la literatura sobre seguridad de la IA y explique por qué importa una de ellas. Rúbrica: 3 = seis pertinentes más la justificación; 2 = seis; 1 = tres; 0 = ninguna.
- **EX004 — FPR baja.** ¿Por qué informar la TPR con una FPR baja en la inferencia de pertenencia? Rúbrica: 3 = el daño procede de la identificación confiada de algunas personas; los promedios lo ocultan; 2 = parcial; 1 = vago; 0 = incorrecto.
- **EX005 — Orden de las fuentes.** Ordene: blog de un proveedor, preprint de arXiv con código, artículo revisado por pares sin código, marco del NIST, y explique el papel del marco. Rúbrica: 3 = orden razonable más el marco como vocabulario y no como resultados; 2 = solo el orden; 1 = vago; 0 = nada.
- **EX006 — Lectura del laboratorio.** ¿Qué AUC informa el laboratorio de inferencia de pertenencia con k = 1 y con k = 5? Rúbrica: 3 = 0.600 y 0.521 con interpretación; 2 = solo los números; 1 = un número; 0 = incorrecto.
- **EX007 — Identificador ausente.** No encuentra un DOI para un artículo de un taller. ¿Cómo lo cita? Rúbrica: 3 = autores, título, foro/año, URL realmente utilizada, sin DOI inventado; 2 = parcial; 1 = vago; 0 = inventa uno.

### Síntesis del capítulo

Un buen trabajo de fin de máster empieza con una pregunta acotada y viable y con una búsqueda que otra persona podría repetir. La matriz de evidencia convierte la lectura en un mapa de lagunas, y unas fuentes honestas hacen que el mapa sea fiable.

### Siga estudiando — capítulo 01 de 08

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Seguridad de la IA y del aprendizaje automático: seminario avanzado

### Resultados de aprendizaje

Usted será capaz de (1) explicar las principales clases de ataque (evasión, envenenamiento y puertas traseras, privacidad —inferencia de pertenencia y extracción de datos—, extracción de modelos e inyección de instrucciones) con sus modelos de amenaza; (2) explicar las defensas y sus límites conocidos; (3) leer y presentar críticamente un artículo en un seminario; (4) relacionar los resultados con NIST AI 100-2 E2025, OWASP LLM 2025 y MITRE ATLAS; y (5) identificar cómo aparece cada clase de ataque en un despliegue real como el de Harbourline.

### 2.1 El formato del seminario

Cada semana un estudiante presenta un artículo en quince minutos: afirmación, modelo de amenaza, método, resultados y tres preguntas críticas. El grupo discute si la evidencia respalda la afirmación. El objetivo no es admirar los artículos, sino entender exactamente lo que muestran. La presentación de Leo sobre Shokri et al. en el ejemplo resuelto de más abajo sigue este formato, y su tercera pregunta pasó a formar parte de su propio diseño. Prepare preguntas que un lector pueda responder a partir del artículo y anote las que el artículo no puede responder, porque ahí suelen estar las lagunas de investigación.

### 2.2 Evasión

Los ejemplos adversariales (Szegedy et al., arXiv:1312.6199) son entradas ligeramente modificadas para provocar errores. FGSM (Goodfellow et al., arXiv:1412.6572) da un paso en la dirección del signo del gradiente de la pérdida; PGD (Madry et al., arXiv:1706.06083) itera y proyecta de nuevo sobre el conjunto de perturbaciones permitidas; el entrenamiento adversarial usa esos ejemplos durante el entrenamiento. En texto, los cambios «pequeños» son más difíciles de definir: sustituir sinónimos o editar caracteres puede cambiar el sentido. En Harbourline, la evasión consistiría en redactar una nota de siniestro de modo que el clasificador la encamine mal. El laboratorio de juguete muestra cómo se desploma la exactitud a medida que crece el presupuesto.

```python
"""Lab E: evasion of a toy linear classifier (synthetic data, stdlib only).
Trains logistic regression on two synthetic clusters, then applies a
fast-gradient-sign (FGSM-style) perturbation of size eps to every test point
and reports clean vs adversarial accuracy. Teaching model only."""
import math, random
rng = random.Random(7)
def point(label):
    cx = 1.0 if label else -1.0
    return [rng.gauss(cx, 0.7), rng.gauss(cx, 0.7)], label
train = [point(i % 2) for i in range(400)]
test = [point(i % 2) for i in range(200)]
w, b = [0.0, 0.0], 0.0
sig = lambda z: 1 / (1 + math.exp(-z))
for epoch in range(200):
    gw, gb = [0.0, 0.0], 0.0
    for x, y in train:
        p = sig(w[0]*x[0] + w[1]*x[1] + b)
        gw[0] += (p - y)*x[0]; gw[1] += (p - y)*x[1]; gb += p - y
    w = [w[i] - 0.1*gw[i]/len(train) for i in range(2)]; b -= 0.1*gb/len(train)
def acc(data, eps):
    ok = 0
    for x, y in data:
        # gradient of the loss w.r.t. x is (p - y) * w; FGSM steps along its sign
        p = sig(w[0]*x[0] + w[1]*x[1] + b)
        xa = [x[i] + eps*math.copysign(1, (p - y)*w[i]) for i in range(2)]
        ok += (sig(w[0]*xa[0] + w[1]*xa[1] + b) >= 0.5) == bool(y)
    return ok / len(data)
print(f"weights w=({w[0]:.3f}, {w[1]:.3f}) b={b:.3f}")
for eps in (0.0, 0.25, 0.5, 0.75, 1.0):
    print(f"eps={eps:.2f} accuracy={acc(test, eps):.3f}")
```

Salida esperada:

```text
weights w=(1.795, 1.756) b=-0.080
eps=0.00 accuracy=0.985
eps=0.25 accuracy=0.950
eps=0.50 accuracy=0.840
eps=0.75 accuracy=0.660
eps=1.00 accuracy=0.505
```

### 2.3 Envenenamiento y puertas traseras

Los ataques de envenenamiento controlan parte de los datos de entrenamiento. El envenenamiento de disponibilidad degrada la exactitud de forma general; el envenenamiento dirigido y el de puerta trasera (Gu et al., arXiv:1708.06733) mantienen la exactitud con datos limpios mientras un disparador provoca el comportamiento elegido. En Harbourline, un tramitador de siniestros malintencionado que pueda insertar notas en el conjunto de entrenamiento podría enseñar al clasificador que una frase encamina los siniestros a la aprobación por vía rápida. Las defensas incluyen la procedencia de los datos, el filtrado de valores atípicos y la limitación de quién puede aportar datos de entrenamiento; ninguna es completa. Pregunte, para cualquier conjunto de datos, quién puede añadir registros y si eso queda registrado.

### 2.4 Ataques contra la privacidad

La inferencia de pertenencia (Shokri et al., arXiv:1610.05820) decide si un registro estuvo en el entrenamiento, usando diferencias en la confianza o en la pérdida del modelo. La extracción de datos de entrenamiento (Carlini et al., arXiv:2012.07805) recupera secuencias literales de los modelos generativos. La privacidad diferencial (Abadi et al., arXiv:1607.00133) acota cuánto puede influir un único registro en el modelo, lo que reduce ambos riesgos a costa de utilidad. Para una aseguradora, la propia pertenencia puede ser sensible («esta persona presentó un siniestro»). El trabajo de fin de máster de Leo estudia el primero de estos riesgos: si la deduplicación reduce la fuga de pertenencia. Según este razonamiento, un reclamante cuya nota aparece muchas veces está más expuesto.

### 2.5 Extracción de modelos

La extracción de modelos (Tramèr et al., arXiv:1609.02943) construye una copia de un modelo a partir de las salidas de su API. Las salidas ricas (vectores de probabilidad completos) la facilitan; redondear y devolver solo etiquetas la dificultan, pero no la hacen imposible. La extracción importa por la propiedad intelectual y porque una copia robada permite ataques de caja blanca. El laboratorio siguiente muestra el efecto de la precisión de la salida: con la puntuación de precisión completa la copia es exacta, con dos decimales es casi exacta y con redondeo a enteros la copia coincide en el 88 % de las etiquetas. En Harbourline, devolver solo la etiqueta de clasificación dificultaría la extracción, no la impediría.

```python
"""Lab X: model extraction of a toy linear scoring API by querying it.
The 'API' returns a real-valued score; d+1 well-chosen queries recover the
weights exactly, and rounding the output limits fidelity. Synthetic model."""
import random
rng = random.Random(9)
d = 5
secret_w = [round(rng.uniform(-2, 2), 3) for _ in range(d)]; secret_b = 0.42
def api(x, decimals=None):
    s = sum(a*b for a, b in zip(secret_w, x)) + secret_b
    return round(s, decimals) if decimals is not None else s
for dec in (None, 2, 0):
    b = api([0]*d, dec)
    w = [api([1 if j == i else 0 for j in range(d)], dec) - b for i in range(d)]
    err = max(abs(a-c) for a, c in zip(w, secret_w))
    test = [[rng.uniform(-1, 1) for _ in range(d)] for _ in range(500)]
    agree = sum((sum(a*c for a, c in zip(w, x))+b > 0) == (api(x) > 0) for x in test)/500
    print(f"output_rounding={str(dec):4s} queries={d+1} max_weight_error={err:.3f} label_agreement={agree:.3f}")
```

Salida esperada:

```text
output_rounding=None queries=6 max_weight_error=0.000 label_agreement=1.000
output_rounding=2    queries=6 max_weight_error=0.004 label_agreement=0.998
output_rounding=0    queries=6 max_weight_error=0.534 label_agreement=0.882
```

### 2.6 Inyección de instrucciones y aplicaciones de LLM

Cuando un LLM procesa texto no fiable, ese texto puede contener instrucciones (Greshake et al., arXiv:2302.12173). OWASP LLM 2025 sitúa la inyección de instrucciones en primer lugar y enumera riesgos relacionados como la divulgación de información sensible, la agencia excesiva y la filtración de la instrucción del sistema. El plan futuro de Harbourline, un asistente que lee los correos de siniestros y redacta respuestas, heredaría estos riesgos. Para un asistente así, el correo de un reclamante es texto no fiable que podría dirigir los borradores o filtrar datos de otros reclamantes. Ese plan queda fuera del trabajo de fin de máster de Leo, pero el seminario debería relacionarlo con las entradas de OWASP para que Harbourline vea qué riesgos añadiría.

### 2.7 Ejemplo resuelto (caso sintético de Harbourline)

Leo presentó a Shokri et al. Sus tres preguntas críticas: (1) el enfoque de modelos sombra supone que el atacante puede muestrear de una distribución de datos similar; ¿es eso realista para notas de seguros? (2) los resultados se informaron sobre todo como precisión/exactitud; ¿cuál es la TPR con una FPR baja? (3) ¿qué parte de la fuga se explica por el sobreajuste? El grupo concluyó que la pregunta (3) era directamente pertinente para su trabajo de fin de máster: si la deduplicación ayuda sobre todo porque reduce el sobreajuste, la «explicación» es la generalización y no la deduplicación en sí, una explicación alternativa para el capítulo 4.

### 2.8 Actividades de práctica

1. Presente un artículo con el formato del seminario. 2. Para cada clase de ataque, escriba un modelo de amenaza de una línea para un sistema que conozca. 3. Relacione el asistente de correo previsto por Harbourline con tres entradas de OWASP LLM 2025. Para la presentación, prepare la afirmación, el modelo de amenaza, el método, los resultados y tres preguntas críticas, como hizo Leo. Para los modelos de amenaza, nombre el conocimiento, el acceso y el objetivo del atacante para cada clase. Para la correspondencia, considere la inyección de instrucciones, la divulgación de información sensible y la agencia excesiva, e indique para cada una qué podría hacer mal el asistente y qué control lo limitaría.

### 2.9 Errores y límites

Cuatro errores se repiten, y cada uno lleva a un resumen engañoso; revise sus notas del seminario en busca de los cuatro:

- Describir ataques sin su modelo de amenaza; un ataque sin su modelo de amenaza no puede compararse con una defensa.
- Suponer que los resultados del dominio de las imágenes se trasladan directamente al texto; puede que no, porque pequeñas ediciones del texto pueden cambiar el sentido.
- Tratar el redondeo o la salida de solo etiquetas como una defensa completa contra la extracción; el redondeo dificultó la extracción en el laboratorio, pero no la detuvo.
- Ignorar que la propia pertenencia puede ser sensible; en Harbourline, el mero hecho de que una persona presentara un siniestro puede ser sensible, de modo que la inferencia de pertenencia es un daño real.

### Ejercicios — capítulo 2

- **EX008 — Modelos de amenaza.** Dé un modelo de amenaza de una línea para la evasión, el envenenamiento con puerta trasera y la inferencia de pertenencia. Rúbrica: 3 = tres con conocimiento, capacidad y objetivo; 2 = dos; 1 = uno; 0 = ninguno.
- **EX009 — FGSM frente a PGD.** Explique la diferencia. Rúbrica: 3 = un único paso frente a pasos iterados y proyectados; PGD es más fuerte; 2 = parcial; 1 = vago; 0 = incorrecto.
- **EX010 — Laboratorio de extracción.** ¿Qué ocurre con el error de los pesos y la coincidencia de etiquetas cuando las salidas se redondean a enteros, y qué implica? Rúbrica: 3 = error 0.534, coincidencia 0.882; la precisión de la salida limita la fidelidad, pero queda una copia útil; 2 = solo los números; 1 = vago; 0 = incorrecto.
- **EX011 — Daño para la aseguradora.** ¿Por qué puede ser sensible la pertenencia en Harbourline? Rúbrica: 3 = revela que una persona presentó un siniestro, posiblemente con detalles de salud o de pérdidas; 2 = parcial; 1 = vago; 0 = nada.
- **EX012 — Escenario de puerta trasera.** Describa (a nivel de diseño) un riesgo de puerta trasera para el clasificador de siniestros y dos controles. Rúbrica: 3 = notas con disparador insertadas por alguien de dentro; control de procedencia/acceso y pruebas de disparadores/valores atípicos; 2 = un control; 1 = vago; 0 = detalle dañino.
- **EX013 — Correspondencia con OWASP.** Relacione el asistente de correo con tres entradas de OWASP LLM 2025. Rúbrica: 3 = p. ej., LLM01, LLM02, LLM06 con sus razones; 2 = solo los identificadores; 1 = una; 0 = ninguna.
- **EX014 — Preguntas para el seminario.** Escriba tres preguntas críticas para un artículo sobre una defensa de su elección. Rúbrica: 3 = tres sobre el modelo de amenaza, el ataque adaptativo y las métricas/costes; 2 = dos; 1 = una; 0 = ninguna.

### Síntesis del capítulo

El seminario aporta soltura en las clases de ataque y en la lectura crítica. Cada clase tiene un modelo de amenaza, un daño típico y defensas con límites conocidos, y las explicaciones alternativas que descubra en la discusión se convierten en preguntas de investigación.

### Siga estudiando — capítulo 02 de 08

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](../../en/book/MANUSCRIPT.md#ch-03)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo; cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación. Harbourline Mutual y todos sus números son sintéticos.

**EX001.** «En agentes de LLM que usan herramientas y leen correo electrónico no fiable (P), ¿exigir confirmación humana para las acciones salientes (I), frente a no exigir confirmación (C), reduce la exfiltración lograda en un banco de pruebas aislado de 500 tareas sintéticas (O)?»

**EX002.** Fuentes/bases de datos; cadenas de búsqueda; intervalo de fechas; criterios de inclusión y exclusión; fecha de la búsqueda; recuentos en cada etapa de cribado (además: seguimiento de citas).

**EX003.** Modelo de amenaza; tipo/tamaño del modelo; datos; métrica; resultado principal; defensa; evaluación adaptativa; disponibilidad del código; limitaciones. La *evaluación adaptativa* importa porque las defensas probadas solo contra ataques fijos a menudo se rompen después.

**EX004.** El daño a la privacidad procede de identificar con confianza a personas concretas; un ataque con un AUC modesto puede aun así identificar algunos registros casi con certeza, y solo la TPR con una FPR baja lo revela.

**EX005.** El artículo revisado por pares (comprobado por la revisión) y el preprint de arXiv con código (comprobable) arriba, en cualquier orden defendible; el blog del proveedor, el último. El marco del NIST no es una fuente experimental: aporta vocabulario y expectativas que se citan para las definiciones.

**EX006.** k = 1: AUC 0.600; k = 5: AUC 0.521. Memorizar (k = 1) filtra la pertenencia; promediar sobre los vecinos elimina la mayor parte de la señal.

**EX007.** Cite los autores, el título, el nombre del taller y el año, y la URL que utilizó (con la fecha de acceso). Nunca invente un DOI.

**EX008.** Evasión: un atacante con acceso de consulta (o de caja blanca) perturba las entradas de prueba para provocar una clasificación errónea. Puerta trasera: un atacante que controla parte de los datos de entrenamiento inserta ejemplos con disparador para provocar las salidas que elige. Inferencia de pertenencia: un atacante con acceso de consulta a las salidas decide si un registro estuvo en el entrenamiento.

**EX009.** FGSM da un único paso de tamaño eps en la dirección del signo del gradiente; PGD da muchos pasos más pequeños, proyectando de nuevo sobre el conjunto permitido cada vez, y es un ataque más fuerte.

**EX010.** Con salidas enteras, el error máximo de los pesos es 0.534 y la coincidencia de etiquetas 0.882 (frente a 0.000/1.000 con precisión completa). Las salidas gruesas reducen la fidelidad, pero siguen dejando una copia aproximada útil.

**EX011.** La pertenencia revela que una persona presentó un siniestro, lo que puede implicar problemas de salud, accidentes o pérdidas: algo sensible en sí mismo.

**EX012.** Alguien de dentro con acceso de escritura a las notas de entrenamiento podría insertar notas que contengan una frase poco común etiquetadas como "fast-track". Controles: acceso de escritura restringido y registrado, con procedencia de los datos de entrenamiento; auditorías previas al entrenamiento de correlaciones entre tokens poco comunes y etiquetas, y pruebas de disparadores después del entrenamiento.

**EX013.** LLM01 Prompt Injection (instrucciones en los correos); LLM02 Sensitive Information Disclosure (detalles de siniestros en las respuestas); LLM06 Excessive Agency (enviar respuestas sin revisión).

**EX014.** Por ejemplo: ¿qué conocimiento del adversario se supone, y se evalúa la defensa frente a un atacante que la conoce? ¿Se informan los resultados con tasas de falsos positivos bajas y con intervalos entre semillas? ¿Cuál es el coste en utilidad o en latencia en las mismas tareas?

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; los marcos cambian, así que vuelva a verificarlos. Los identificadores de arXiv se abrieron y se comprobaron sus títulos. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Abadi, M. et al. (2016). Deep Learning with Differential Privacy. arXiv:1607.00133.
- Athalye, A., Carlini, N., Wagner, D. (2018). Obfuscated Gradients Give a False Sense of Security. arXiv:1802.00420.
- Carlini, N. et al. (2020). Extracting Training Data from Large Language Models. arXiv:2012.07805.
- European Union. Regulation (EU) 2024/1689 (Artificial Intelligence Act). <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
- Gebru, T. et al. (2018). Datasheets for Datasets. arXiv:1803.09010.
- Goodfellow, I., Shlens, J., Szegedy, C. (2014). Explaining and Harnessing Adversarial Examples. arXiv:1412.6572.
- Greshake, K. et al. (2023). Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. arXiv:2302.12173.
- Gu, T., Dolan-Gavitt, B., Garg, S. (2017). BadNets. arXiv:1708.06733.
- ISO/IEC 42001:2023 Artificial intelligence — Management system. <https://www.iso.org/standard/81230.html>
- Kapoor, S., Narayanan, A. (2022). Leakage and the Reproducibility Crisis in ML-based Science. arXiv:2207.07048.
- Madry, A. et al. (2017). Towards Deep Learning Models Resistant to Adversarial Attacks. arXiv:1706.06083.
- MITRE ATLAS. <https://atlas.mitre.org/>
- Mitchell, M. et al. (2018). Model Cards for Model Reporting. arXiv:1810.03993.
- NIST AI 100-1 (2023), AI RMF 1.0. <https://doi.org/10.6028/NIST.AI.100-1>
- NIST AI 100-2 E2025 (2025), Adversarial Machine Learning taxonomy. <https://doi.org/10.6028/NIST.AI.100-2e2025>
- NIST AI 600-1 (2024), Generative AI Profile. <https://doi.org/10.6028/NIST.AI.600-1>
- OWASP Top 10 for LLM Applications 2025. <https://genai.owasp.org/llm-top-10/>
- Pineau, J. et al. (2020). Improving Reproducibility in Machine Learning Research. arXiv:2003.12206.
- Shokri, R. et al. (2016). Membership Inference Attacks against Machine Learning Models. arXiv:1610.05820.
- Szegedy, C. et al. (2013). Intriguing properties of neural networks. arXiv:1312.6199.
- Tramèr, F. et al. (2016). Stealing Machine Learning Models via Prediction APIs. arXiv:1609.02943.
