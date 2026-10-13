# Seguridad de la IA y del aprendizaje automático: libro del curso de ingeniería

- Idioma: español neutro (`es`); curso de ingeniería, cinco años; aproximadamente 4.000 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–50 de 50 tienen texto didáctico de autor; los ejercicios EX001–EX150 (tres por capítulo) tienen sus resultados resueltos correspondientes con rúbricas de 0 a 3; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas impresas proceden de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no equivale a un libro terminado.
- Público: futuros diseñadores de sistemas de seguridad que especificarán, construirán, verificarán y operarán sistemas con IA que resistan ataques y fallen de forma segura.
- Relación con los libros vecinos: el [libro de grado](../../../../bachelors-4-years/ai-security/en/book/MANUSCRIPT.md) es más amplio y menos centrado en el diseño; el [libro de posgrado](../../../../postgraduate-2-years/ai-security/en/book/MANUSCRIPT.md) presupone experiencia profesional. **Este libro enseña la seguridad de la IA como disciplina de ingeniería**: fundamentos de matemáticas y computación, requisitos, arquitectura, controles, medición, confiabilidad, seguridad funcional, operaciones y un proyecto final con expediente de evidencia y defensa.
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado y no concede autorización para probar sistemas reales. Todas las organizaciones, personas, conjuntos de datos y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Cincuenta capítulos siguen la carrera: fundamentos de matemáticas, física, programación y comunicación (1–10); sistemas de computación y fundamentos de seguridad (11–19); ingeniería de seguridad de la IA, desde el contexto hasta la optimización (20–42); y práctica, proyecto final, expediente, trabajo de fin de grado y defensa (43–50). Cada capítulo tiene resultados de aprendizaje, texto didáctico, un ejemplo resuelto, errores y límites, tres ejercicios puntuados de 0 a 3 (0 ausente o inseguro; 1 laguna importante; 2 lagunas menores; 3 completo y justificado), una síntesis y un bloque **Siga estudiando**. Los laboratorios son deterministas, se ejecutan sin conexión con `python3 file.py` e imprimen los resultados que aparecen en *Salida esperada*. Son modelos de juguete que hacen medible un concepto, no defensas de producción.

### El ejemplo conductor (sintético): Northgate Rail Systems

> **Caso sintético — ficción.** **Northgate Rail Systems (NRS)** es una empresa inventada de ingeniería de mantenimiento ferroviario. Opera (1) **TrackEye**, un modelo basado en cámaras instalado en trenes de inspección que señala defectos en los carriles; (2) **Wrench**, un asistente de mantenimiento basado en un modelo de lenguaje que lee manuales, notas de los técnicos y boletines de proveedores y puede redactar órdenes de trabajo mediante una interfaz de herramientas; y (3) **Pulse**, un modelo de anomalías sobre sensores de temperatura de los rodamientos de los ejes. El estudiante de ingeniería *Sam Ito* hace prácticas en NRS a lo largo de la carrera. Todos los números sobre NRS son inventados; todas las pruebas descritas se realizan sobre copias aisladas y con autorización escrita.

### Política de fuentes

Las fuentes se comprobaron el 12 de octubre de 2026: NIST [AI 100-1](https://doi.org/10.6028/NIST.AI.100-1) (AI RMF 1.0), [AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) (perfil de IA generativa) y [AI 100-2 E2025](https://doi.org/10.6028/NIST.AI.100-2e2025) (taxonomía del aprendizaje automático adversarial); el [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [MITRE ATLAS](https://atlas.mitre.org/); el [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) (Reglamento de IA); y la [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html). Los artículos se citan por su identificador de arXiv; cada uno se abrió y se comprobó su título.

## Contenido

| Parte | Capítulos |
|---|---|
| Fundamentos | [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| Sistemas y seguridad | [11](#ch-11) · [12](#ch-12) · [13](../../en/book/MANUSCRIPT.md#ch-13) · [14](../../en/book/MANUSCRIPT.md#ch-14) · [15](../../en/book/MANUSCRIPT.md#ch-15) · [16](../../en/book/MANUSCRIPT.md#ch-16) · [17](../../en/book/MANUSCRIPT.md#ch-17) · [18](../../en/book/MANUSCRIPT.md#ch-18) · [19](../../en/book/MANUSCRIPT.md#ch-19) |
| Ingeniería de seguridad de la IA | [20](../../en/book/MANUSCRIPT.md#ch-20) · [21](../../en/book/MANUSCRIPT.md#ch-21) · [22](../../en/book/MANUSCRIPT.md#ch-22) · [23](../../en/book/MANUSCRIPT.md#ch-23) · [24](../../en/book/MANUSCRIPT.md#ch-24) · [25](../../en/book/MANUSCRIPT.md#ch-25) · [26](../../en/book/MANUSCRIPT.md#ch-26) · [27](../../en/book/MANUSCRIPT.md#ch-27) · [28](../../en/book/MANUSCRIPT.md#ch-28) · [29](../../en/book/MANUSCRIPT.md#ch-29) · [30](../../en/book/MANUSCRIPT.md#ch-30) · [31](../../en/book/MANUSCRIPT.md#ch-31) · [32](../../en/book/MANUSCRIPT.md#ch-32) · [33](../../en/book/MANUSCRIPT.md#ch-33) · [34](../../en/book/MANUSCRIPT.md#ch-34) · [35](../../en/book/MANUSCRIPT.md#ch-35) · [36](../../en/book/MANUSCRIPT.md#ch-36) · [37](../../en/book/MANUSCRIPT.md#ch-37) · [38](../../en/book/MANUSCRIPT.md#ch-38) · [39](../../en/book/MANUSCRIPT.md#ch-39) · [40](../../en/book/MANUSCRIPT.md#ch-40) · [41](../../en/book/MANUSCRIPT.md#ch-41) · [42](../../en/book/MANUSCRIPT.md#ch-42) |
| Práctica y proyecto final | [43](../../en/book/MANUSCRIPT.md#ch-43) · [44](../../en/book/MANUSCRIPT.md#ch-44) · [45](../../en/book/MANUSCRIPT.md#ch-45) · [46](../../en/book/MANUSCRIPT.md#ch-46) · [47](../../en/book/MANUSCRIPT.md#ch-47) · [48](../../en/book/MANUSCRIPT.md#ch-48) · [49](../../en/book/MANUSCRIPT.md#ch-49) · [50](../../en/book/MANUSCRIPT.md#ch-50) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Resultados de aprendizaje

Usted será capaz de (1) calcular derivadas de las funciones que se usan en el aprendizaje automático (polinomios, exponenciales, logaritmos, la función logística); (2) interpretar una derivada como sensibilidad; (3) comprobar derivadas numéricamente; y (4) explicar por qué la misma derivada que entrena un modelo también guía a un atacante.

### 1.1 Derivadas como sensibilidad

La derivada f′(x) mide cuánto cambia f cuando x cambia un poco: f(x + h) ≈ f(x) + h f′(x). Los ingenieros la usan como *sensibilidad*: si el modelo de temperatura de un rodamiento tiene una derivada grande respecto de una entrada, pequeños errores del sensor provocan grandes cambios en la salida. Los modelos de aprendizaje automático son funciones de entradas y parámetros, así que las derivadas nos dicen cómo responden las salidas a ambos. La aproximación solo vale para h pequeño, de modo que una derivada describe el entorno de un punto, no la función entera. Por eso Sam siempre indica dónde se midió una sensibilidad, por ejemplo en una imagen diurna típica, y la vuelve a comprobar en otros puntos de operación antes de sacar conclusiones sobre el modelo en su conjunto.

### 1.2 Reglas que usará constantemente

Regla de la potencia (xⁿ)′ = n xⁿ⁻¹; exponencial (eˣ)′ = eˣ; logaritmo (ln x)′ = 1/x; reglas del producto, del cociente y de la cadena. La función logística σ(z) = 1/(1 + e⁻ᶻ) transforma cualquier número real en un valor de (0, 1) y cumple σ′(z) = σ(z)(1 − σ(z)). La pérdida logística para una etiqueta y ∈ {−1, +1} y una puntuación z = w·x es L = ln(1 + e^(−y z)); por la regla de la cadena, ∂L/∂w = −y x / (1 + e^(y w x)). Conviene recordar la derivada logística porque es máxima en z = 0, donde σ′ = 0,25, y se reduce hacia cero a medida que la puntuación se vuelve segura en cualquiera de las dos direcciones. Por tanto, las entradas cercanas a la frontera de decisión son aquellas en las que pequeños cambios mueven más la salida, y es justamente ahí donde empieza un atacante.

### 1.3 Comprobación numérica de derivadas

Una diferencia finita centrada (f(x + h) − f(x − h)) / 2h aproxima f′(x) con un error proporcional a h². Compararla con la fórmula analítica es la prueba estándar del código de gradientes; una discrepancia indica un fallo. El laboratorio hace exactamente eso y después da seis pasos de descenso de gradiente que reducen la pérdida.

```python
"""Lab G: gradients by calculus and by finite differences (stdlib only).
For logistic loss L(w) = log(1 + exp(-y * w * x)) the derivative is
dL/dw = -y * x / (1 + exp(y * w * x)). The same gradient drives both
training (descend) and evasion attacks (ascend with respect to the input)."""
import math
x, y = 2.0, 1.0
L = lambda w: math.log(1 + math.exp(-y * w * x))
dL = lambda w: -y * x / (1 + math.exp(y * w * x))
for w in (-1.0, 0.0, 0.5, 2.0):
    h = 1e-5
    fd = (L(w + h) - L(w - h)) / (2 * h)
    print(f"w={w:5.2f} loss={L(w):.4f} analytic={dL(w):.6f} finite_diff={fd:.6f}")
w = -1.0
for step in range(6):
    w -= 0.5 * dL(w)
    print(f"step {step+1}: w={w:.4f} loss={L(w):.4f}")
```

Salida esperada:

```text
w=-1.00 loss=2.1269 analytic=-1.761594 finite_diff=-1.761594
w= 0.00 loss=0.6931 analytic=-1.000000 finite_diff=-1.000000
w= 0.50 loss=0.3133 analytic=-0.537883 finite_diff=-0.537883
w= 2.00 loss=0.0181 analytic=-0.035972 finite_diff=-0.035972
step 1: w=-0.1192 loss=0.8194
step 2: w=0.4401 loss=0.3469
step 3: w=0.7332 loss=0.2076
step 4: w=0.9207 loss=0.1472
step 5: w=1.0576 loss=0.1139
step 6: w=1.1652 loss=0.0928
```

En la tabla impresa, las dos columnas coinciden hasta el sexto decimal en los cuatro puntos de prueba, incluido w = 2, donde el gradiente es pequeño. Los pasos de descenso muestran que la pérdida baja de 2,1269 a 0,0928, y los pasos cada vez más cortos se deben a que el gradiente se aplana a medida que w crece y el ejemplo se clasifica con más confianza.

### 1.4 Por qué les importa a los ingenieros de seguridad

El entrenamiento mueve los *parámetros* en contra del gradiente de la pérdida. Un atacante de evasión mueve la *entrada* a lo largo del gradiente de la pérdida respecto de la entrada, para hacer la pérdida mayor: es la idea del método del signo del gradiente rápido (FGSM; Goodfellow et al., arXiv:1412.6572). Así, las derivadas son a la vez el motor del aprendizaje y un mapa para el atacante. Las defensas que ocultan o rompen los gradientes sin cambiar el comportamiento del modelo dan una falsa sensación de seguridad (Athalye et al., arXiv:1802.00420).

Para un revisor de seguridad, un gradiente es tanto una herramienta del atacante como del entrenador.

### 1.5 Ejemplo resuelto (caso sintético de NRS)

Sam calcula la derivada de la puntuación logística final de TrackEye respecto de una característica de intensidad de píxel y obtiene 0,8 por unidad, mientras que la mayoría de las características están por debajo de 0,05. Una lente sucia que desplace esa característica en 0,5 cambia la puntuación en aproximadamente 0,4, suficiente para invertir una decisión dudosa. Sam registra la característica como *entrada de alta sensibilidad* para las pruebas de robustez posteriores. La aritmética es la aproximación de primer orden en acción: 0,8 × 0,5 = 0,4. Solo vale cerca del punto donde se midió la derivada, así que Sam comprueba después el cambio real de la puntuación con imágenes con suciedad simulada, lo que muestra si la estimación lineal subestima o sobrestima el efecto. La característica entra en el plan de pruebas de robustez con esa salvedad registrada.

### 1.6 Errores y límites

- Olvidar la derivada interna de la regla de la cadena.
- Usar un h demasiado pequeño en las diferencias finitas (error de redondeo) o demasiado grande (error de truncamiento).
- Tratar un gradiente pequeño como prueba de que ningún cambio pequeño puede invertir la salida (las funciones pueden ser no lineales).

Cada error tiene una salvaguarda sencilla. Escribir explícitamente la función interna antes de derivar detecta un factor de la regla de la cadena que falta. Probar varios tamaños de paso, como 1e-3, 1e-5 y 1e-7, muestra dónde son estables las diferencias finitas, ya que el error primero baja y luego vuelve a subir. Para el tercer error, un gradiente pequeño se trata como un motivo para probar directamente cambios más grandes, nunca como una garantía de que la salida no puede invertirse.

### Ejercicios — capítulo 1

- **EX001 — Derivada logística.** Demuestre que σ′(z) = σ(z)(1 − σ(z)) y evalúela en z = 0. Rúbrica: 3 = derivación y 0,25; 2 = valor sin derivación; 1 = parcial; 0 = nada.
- **EX002 — Lectura del laboratorio.** En el laboratorio G, ¿cuáles son la pérdida y el gradiente en w = 0, y por qué baja la pérdida a lo largo de los seis pasos? Rúbrica: 3 = 0,6931, −1,0; moverse en contra del gradiente reduce la pérdida; 2 = solo los números; 1 = vago; 0 = incorrecto.
- **EX003 — La mirada del atacante.** Explique en dos frases cómo usa un atacante la misma derivada de forma distinta al entrenamiento. Rúbrica: 3 = derivada respecto de la entrada, paso para aumentar la pérdida; 2 = parcial; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

Las derivadas cuantifican la sensibilidad. Entrenan modelos y también muestran a los atacantes qué pequeños cambios de la entrada importan más: el primer vínculo entre las matemáticas y la seguridad de la IA.

### Siga estudiando — capítulo 01 de 50

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Matemáticas discretas

### Resultados de aprendizaje

Usted será capaz de (1) usar conjuntos, relaciones, funciones y lógica para describir con precisión el comportamiento de un sistema; (2) expresar políticas de acceso y de uso de herramientas como predicados; (3) contar posibilidades para estimar espacios de búsqueda; y (4) razonar sobre grafos de flujo de datos y de control en sistemas de IA.

### 2.1 Conjuntos, funciones y lógica

Un modelo es una función f: X → Y de un conjunto de entradas en un conjunto de salidas. Una política es un predicado P(usuario, acción, recurso) que es verdadero cuando la acción está permitida. Los conectivos lógicos (∧, ∨, ¬, →) y los cuantificadores (∀, ∃) permiten escribir propiedades de seguridad con exactitud: "∀ tool call c issued by Wrench, Authorised(requesting_user(c), c)". Escribir las propiedades así revela ambigüedades: ¿quién es el «usuario solicitante» cuando la llamada la desencadenó un texto de un boletín de un proveedor?

Sam lo resuelve definiendo al usuario solicitante como la persona cuya sesión inició la conversación.

### 2.2 Relaciones y grafos

Un grafo dirigido de componentes (cámara → preprocesamiento → modelo → cola de alertas → técnico) muestra por dónde fluyen los datos y dónde cambia la confianza. Los caminos desde una *fuente no confiable* hasta un *sumidero privilegiado* son las rutas que puede usar un atacante; en las aplicaciones con modelos de lenguaje, el camino «boletín del proveedor → prompt de Wrench → herramienta de órdenes de trabajo» es exactamente un camino de inyección indirecta de prompts (Greshake et al., arXiv:2302.12173). La alcanzabilidad en grafos se calcula mediante búsqueda en anchura o en profundidad.

Dibujar primero el grafo hace que la búsqueda sea mecánica: marque cada nodo cuyo contenido pueda influir un externo, marque cada nodo que pueda cambiar algo en el mundo y enumere los caminos entre ellos. Cada camino encontrado así necesita un control en algún punto de su recorrido, y el grafo muestra dónde.

### 2.3 Conteo

La combinatoria estima espacios de búsqueda. Si un atacante puede cambiar 3 cualesquiera de 100 características a uno de 4 valores, hay C(100,3) × 4³ = 161.700 × 64 ≈ 10,3 millones de variantes, algo que un ordenador puede recorrer sin problema. El conteo muestra por qué «nadie encontrará la entrada mala» no es una defensa. Diez millones de variantes pueden evaluarse en minutos en un ordenador corriente si cada consulta al modelo es rápida, de modo que un atacante no necesita ingenio, solo paciencia y acceso al modelo o a una copia parecida. El mismo conteo indica a los defensores dónde limitar las consultas: si cada variante tuviera que pasar por una interfaz con límite de mil solicitudes al día, la búsqueda exhaustiva llevaría décadas, y el atacante tendría que buscar con mucho más ingenio.

### 2.4 Inducción e invariantes

Un *invariante* es una propiedad que se cumple antes y después de cada paso. «La herramienta de órdenes de trabajo solo puede llamarse con el token de sesión de un técnico» es un invariante; demostrar que se cumple en todos los caminos del código (por inducción sobre los pasos) es más sólido que probar unos pocos casos. La inducción tiene dos partes. El caso base comprueba que no es posible ninguna llamada a herramientas antes de que exista una sesión. El paso muestra que, si todas las llamadas anteriores llevaban un token válido, el camino de código que emite la siguiente llamada también adjunta uno y, en caso contrario, la rechaza. Una prueba con unas pocas llamadas no puede mostrar que ningún camino se salta la comprobación; un argumento sobre todos los caminos sí puede, siempre que los caminos de código se enumeren por completo.

### 2.5 Ejemplo resuelto (caso sintético de NRS)

Sam dibuja el grafo de flujo de datos de Wrench con nodos para el chat del usuario, los manuales, las notas de los técnicos, los boletines de proveedores (externos), el modelo y dos herramientas (search, create_work_order). Existen dos caminos de lo no confiable a lo privilegiado: boletín → modelo → create_work_order y notas de los técnicos (editables por contratistas) → modelo → create_work_order. Sam escribe la propiedad «∀ llamadas a create_work_order, un técnico humano la confirmó» y marca ambos caminos para aplicarles controles.

El segundo camino es fácil de pasar por alto porque las notas de los técnicos parecen internas, pero los contratistas pueden editarlas, así que pertenecen a las entradas no confiables. La propiedad de confirmación coloca un único control en el sumidero, que cubre ambos caminos a la vez, en lugar de intentar filtrar cada fuente no confiable por separado.

### 2.6 Errores y límites

- Políticas informales con excepciones ocultas.
- Olvidar los caminos indirectos a través de almacenes de datos.
- Subestimar espacios de búsqueda que los ordenadores enumeran con facilidad.

Las excepciones ocultas aparecen cuando una política escrita como «los técnicos pueden crear órdenes de trabajo» resulta significar «salvo los contratistas en turnos de fin de semana», algo que nadie dejó por escrito. Los caminos indirectos se pasan por alto cuando un grafo muestra solo las conexiones activas y omite los almacenes, como notas guardadas hoy y leídas por el modelo mañana. Subestiman los espacios de búsqueda quienes imaginan a una persona probando entradas a mano, en lugar de un programa probando millones.

### Ejercicios — capítulo 2

- **EX004 — Predicado.** Escriba un predicado que establezca que Wrench solo puede crear órdenes de trabajo para activos del depósito del técnico solicitante. Rúbrica: 3 = predicado cuantificado correcto; 2 = error menor; 1 = informal; 0 = nada.
- **EX005 — Caminos.** Enumere los caminos de lo no confiable a lo privilegiado en el grafo de Sam y un control para cada uno. Rúbrica: 3 = ambos caminos, controles sensatos; 2 = uno; 1 = vago; 0 = nada.
- **EX006 — Conteo.** Cuente las variantes si un atacante cambia 2 cualesquiera de 50 características a uno de 3 valores. Rúbrica: 3 = C(50,2)×3² = 1.225×9 = 11.025; 2 = desliz aritmético; 1 = solo el método; 0 = nada.

### Síntesis del capítulo

Las matemáticas discretas ofrecen un lenguaje preciso para políticas, flujos de datos y espacios de búsqueda: la base para enunciar y comprobar propiedades de seguridad de la IA en lugar de confiar en que se cumplan.

### Siga estudiando — capítulo 02 de 50

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Física para la computación

### Resultados de aprendizaje

Usted será capaz de (1) relacionar señales, ruido y muestreo con las entradas de sensores y cámaras; (2) explicar cómo las condiciones físicas (luz, vibración, temperatura) desplazan las entradas de un modelo; (3) describir a nivel conceptual los ataques adversariales en el mundo físico y la suplantación de sensores; y (4) especificar condiciones de prueba físicas para un componente de IA.

### 3.1 Señales, ruido y muestreo

Los sensores convierten magnitudes físicas en números. Toda medición contiene ruido; el muestreo convierte señales continuas en discretas, y muestrear por debajo del doble de la frecuencia más alta (la tasa de Nyquist) provoca aliasing. Las cámaras integran la luz durante el tiempo de exposición; el desenfoque por movimiento, los deslumbramientos y la poca luz cambian los valores de los píxeles. Un modelo de visión entrenado con imágenes diurnas nítidas puede encontrarse con entradas muy distintas de noche o con lluvia. En TrackEye, el muestreo también se aplica al tiempo: una cámara que captura fotogramas demasiado despacio para la velocidad del tren puede perder por completo un defecto corto entre dos fotogramas. Los ingenieros comprueban que la frecuencia de fotogramas y el tiempo de exposición sean adecuados para la velocidad de operación más alta, no solo para un recorrido medio.

### 3.2 Desplazamientos físicos frente a ataques

El desplazamiento de distribución *natural* procede de la física: polvo en las lentes, deriva térmica de los termistores, vibración. Los ataques físicos *adversariales* fabrican deliberadamente objetos o señales: patrones impresos que provocan una clasificación errónea o señales inyectadas que suplantan a los sensores. La investigación ha mostrado que las perturbaciones pueden sobrevivir a la impresión y a la captura con cámara en condiciones de observación variadas cuando se optimizan sobre muchas transformaciones. Hay que probar ambos tipos de desplazamiento; la diferencia de ingeniería es que los adversarios buscan el peor caso, mientras que la naturaleza muestrea casos típicos.

El plan de pruebas los trata de forma distinta: los desplazamientos naturales se miden como rendimiento medio en las condiciones esperadas, mientras que los adversariales se miden como el peor resultado que un atacante podría encontrar dentro de unos límites establecidos.

### 3.3 Energía, calor y canales laterales

La computación consume energía y emite calor y señales electromagnéticas que pueden filtrar información (canales laterales). En los aceleradores de IA se han estudiado las mediciones de tiempo y de consumo como formas de inferir propiedades del modelo. Por eso el acceso físico forma parte del modelo de amenazas de los dispositivos de IA en el borde, como el ordenador de un tren de inspección. Un ordenador de tren de inspección recorre la red y puede recibir mantenimiento de contratistas en los depósitos, así que alguien podría conectarle equipos de medida sin mucha dificultad. Los ingenieros no suelen defenderse de todos los canales laterales, pero registran cuáles son verosímiles según quién tenga acceso físico y protegen los activos más valiosos, como los pesos del modelo y las claves de firma, con envolventes con evidencia de manipulación y almacenamiento cifrado.

### 3.4 Especificación de condiciones de prueba físicas

Una especificación de ingeniería enumera condiciones: rango de iluminación (lux), rango de temperatura, espectro de vibración, niveles de contaminación de la lente y velocidad del tren. Cada una se convierte en un eje de prueba. Para la seguridad, añada condiciones adversariales dentro del modelo de amenazas; por ejemplo, «un atacante puede colocar marcas en las traviesas, pero no puede acceder al tren». Cada eje necesita un rango declarado y la forma en que se producirá en las pruebas: recorridos grabados, montajes de iluminación controlada o simulación. Los rangos proceden de datos de operación, como la luz más baja medida en los recorridos al amanecer y la velocidad de línea más alta. Una frase del modelo de amenazas que diga lo que el atacante no puede hacer es tan importante como la que dice lo que puede, porque define cuándo un fallo cuenta como hallazgo de seguridad y no como limitación.

### 3.5 Ejemplo resuelto (caso sintético de NRS)

La tasa de falsos negativos de TrackEye subió del 2 % al 9 % en los recorridos al amanecer. Sam lo atribuyó al ángulo bajo del sol, que causaba deslumbramientos a 60–80 km/h. La corrección combinó un filtro polarizador, un cambio de exposición y 4.000 imágenes adicionales tomadas al amanecer. Sam añadió además un eje de prueba para marcas deliberadas cerca de los carriles, ya que cualquiera que camine por la vía podría colocarlas. La subida del 2 % al 9 % solo apareció al desglosar los resultados por hora del día; la media global la ocultaba. La corrección combina medidas físicas y de datos, y solo una nueva prueba con recorridos recientes al amanecer puede mostrar si funcionó.

### 3.6 Errores y límites

- Probar solo con la iluminación del laboratorio.
- Confundir el desplazamiento natural con un ataque (o ignorar cualquiera de los dos).
- Omitir el acceso físico en los modelos de amenazas de los dispositivos en el borde.

La iluminación del laboratorio es uniforme y estable, así que un modelo que pasa allí no se ha enfrentado a deslumbramientos, lluvia ni lentes sucias. Tratar cada fallo como un ataque malgasta esfuerzo en la búsqueda de amenazas, mientras que tratar cada fallo como natural puede ocultar una manipulación deliberada. Los dispositivos en el borde suelen estar al alcance de personas con acceso legítimo al depósito, de modo que el acceso físico es una vía realista, no exótica, y omitirlo hace que el modelo de amenazas parezca más seguro que el sistema.

### Ejercicios — capítulo 3

- **EX007 — Nyquist.** Un sensor de vibración debe capturar componentes de hasta 400 Hz. ¿Qué frecuencia de muestreo mínima evita el aliasing? Rúbrica: 3 = > 800 Hz con justificación; 2 = 800 sin justificación; 1 = incorrecto pero razonado; 0 = nada.
- **EX008 — Desplazamiento o ataque.** Clasifique: polvo en la lente; patrón pintado en una traviesa; deriva del termistor. Rúbrica: 3 = natural, adversarial, natural, con razones; 2 = solo las etiquetas; 1 = uno correcto; 0 = nada.
- **EX009 — Ejes de prueba.** Escriba cinco ejes de prueba físicos para TrackEye. Rúbrica: 3 = cinco ejes medibles con rangos; 2 = cinco sin rangos; 1 = dos o tres; 0 = nada.

### Síntesis del capítulo

La física determina qué entradas recibe realmente un componente de IA. Los ingenieros especifican las condiciones físicas, prueban los desplazamientos naturales e incluyen a los adversarios físicos en el modelo de amenazas.

### Siga estudiando — capítulo 03 de 50

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Programación I

### Resultados de aprendizaje

Usted será capaz de (1) escribir programas pequeños y correctos en Python con funciones, bucles y estructuras de datos; (2) manejar entradas no confiables de forma segura; (3) probar código con aserciones; y (4) leer los laboratorios del libro y modificarlos.

### 4.1 Los programas como instrucciones precisas

Un programa dice exactamente lo que hace el ordenador. Las variables guardan valores; las funciones empaquetan pasos; los bucles repiten; los condicionales eligen. El código legible usa nombres claros y funciones pequeñas. Los laboratorios de este libro usan solo la biblioteca estándar de Python, de modo que se ejecutan en cualquier lugar. La precisión tiene dos caras: el ordenador hace lo que dice el código, no lo que quería decir su autor. Un bucle que se detiene un elemento antes o una condición escrita con 'or' en lugar de 'and' producen resultados erróneos sin ningún aviso. Sam lee cada laboratorio línea por línea antes de ejecutarlo y predice la salida, de modo que una sorpresa en el resultado impreso señala una laguna en su comprensión.

### 4.2 Estructuras de datos

Las listas guardan secuencias; los diccionarios asocian claves con valores; los conjuntos guardan elementos únicos. Un inventario de modelos es, de forma natural, una lista de diccionarios; una lista de permitidos de una política es, de forma natural, un conjunto. Elegir la estructura adecuada hace el código más corto y más seguro: la pertenencia a un conjunto es una prueba clara y rápida para «¿está permitida esta herramienta?». Una lista también serviría como lista de permitidos, pero comprobar la pertenencia en ella obliga a recorrer todos los elementos, y pueden colarse duplicados sin que nadie lo note. La estructura equivocada también puede ocultar un fallo de seguridad: si las herramientas permitidas se guardan como una sola cadena separada por comas, una comprobación como 'search' in allowed aceptaría también una herramienta llamada 'research'.

### 4.3 Entradas no confiables

Todo dato que venga de fuera del programa (archivos, mensajes de red, salidas de modelos) es no confiable. Nunca lo pase a `eval`, a comandos de shell ni a consultas de bases de datos sin una validación estricta. Esto se aplica a la IA: OWASP LLM 2025 incluye el *manejo inadecuado de la salida* (LLM05) porque las aplicaciones suelen ejecutar o representar directamente la salida del modelo. Analice con analizadores estrictos (p. ej., `json.loads`), valide tipos y rangos, y rechace los campos desconocidos.

Rechazar los campos desconocidos importa porque los sistemas posteriores pueden actuar sobre campos que el validador nunca miró. Un analizador estricto los rechaza de plano.

### 4.4 Los errores como información

Cuando el código falla, debe fallar *de forma cerrada* y explicarse. Un analizador que descarta en silencio un campo desconocido podría dejar pasar un campo que el sistema posterior sí respeta; un analizador que rechaza el objeto entero con un mensaje claro es más seguro y más fácil de depurar. Registre el rechazo con contexto suficiente para investigarlo (hora, origen, motivo), pero sin copiar contenido sensible en los registros. Las excepciones son el mecanismo normal de Python: lance `ValueError` con un mensaje y deje que quien llama decida si reintentar, consultar a una persona o detenerse.

### 4.5 Pruebas

Un `assert` enuncia lo que debe ser verdadero. Las pruebas unitarias llaman a funciones con entradas elegidas y comprueban las salidas, incluidos los casos límite (listas vacías, valores muy grandes, texto mal formado). Las pruebas hacen que los cambios posteriores sean seguros. En el código de seguridad, las pruebas más valiosas son las que deberían fallar: una orden de trabajo con un campo de más, una prioridad escrita de otra forma, un identificador de activo que contiene signos de puntuación. Cada rechazo esperado se escribe como una prueba, de modo que un cambio posterior que relaje la validación rompa la compilación en lugar de llegar a producción. Sam conserva como caso de prueba permanente cada entrada mal formada que alguna vez causó un problema.

### 4.6 Ejemplo resuelto (caso sintético de NRS)

Sam escribe una función que analiza la orden de trabajo propuesta por Wrench (JSON) antes de que llegue al sistema de órdenes de trabajo:

```python
import json
ALLOWED = {"asset_id", "priority", "summary"}
def parse_order(text):
    d = json.loads(text)
    assert isinstance(d, dict) and set(d) <= ALLOWED, "unexpected fields"
    assert d.get("priority") in {"low", "medium", "high"}, "bad priority"
    assert isinstance(d.get("asset_id"), str) and d["asset_id"].isalnum(), "bad asset id"
    return d
print(parse_order('{"asset_id": "AX12", "priority": "high", "summary": "bearing hot"}'))
try:
    parse_order('{"asset_id": "AX12; rm", "priority": "high"}')
except AssertionError as e:
    print("rejected:", e)
```

El programa imprime la orden válida y después `rejected: bad asset id`. La salida del modelo se trata como datos que hay que validar, nunca como código.

El identificador de activo se rechaza porque el punto y coma y el espacio no superan la comprobación alfanumérica, de modo que un texto que parece un comando de shell nunca llega al sistema de órdenes de trabajo. La función nunca exige un resumen, así que una orden sin él pasaría; Sam añade esa comprobación a continuación. En producción, Sam sustituye las aserciones por excepciones explícitas, por la razón que se da entre los errores siguientes.

### 4.7 Errores y límites

- Ejecutar la salida del modelo como código o como comandos de shell.
- Validación que solo comprueba los caminos felices.
- Usar aserciones como única comprobación en código de producción (pueden desactivarse con `python -O`; use allí excepciones explícitas).

Cada error tiene una señal reconocible en la revisión de código. Las llamadas a eval, exec o subprocess con una cadena construida a partir de la salida del modelo son lo primero que hay que buscar. Los validadores sin pruebas para entradas rechazadas probablemente nunca se han probado con datos malos. Las aserciones que protegen condiciones de seguridad deberían convertirse en sentencias if que lancen una excepción con nombre, porque, de lo contrario, una ejecución optimizada en producción se saltaría la comprobación por completo sin ningún mensaje.

### Ejercicios — capítulo 4

- **EX010 — Lista de permitidos.** Escriba una función `allowed(tool)` que use un conjunto de herramientas permitidas. Rúbrica: 3 = pertenencia a conjunto correcta con prueba; 2 = funciona sin prueba; 1 = usa una lista con errores; 0 = nada.
- **EX011 — Manejo de la salida.** ¿Por qué es peligroso pasar la salida del modelo a `eval`? Nombre la entrada de OWASP. Rúbrica: 3 = ejecución de código arbitrario a partir de texto influido por el atacante; LLM05; 2 = una parte; 1 = vago; 0 = incorrecto.
- **EX012 — Casos límite.** Enumere cuatro pruebas de casos límite para `parse_order`. Rúbrica: 3 = cuatro pertinentes (vacío, campo de más, tipo incorrecto, JSON no válido, resumen largo); 2 = tres; 1 = una o dos; 0 = nada.

### Síntesis del capítulo

Programar para la seguridad de la IA empieza por un hábito: tratar todo lo que viene de fuera, incluida la salida del modelo, como datos no confiables, validarlo estrictamente y probar los extremos.

### Siga estudiando — capítulo 04 de 50

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Comunicación en ingeniería

### Resultados de aprendizaje

Usted será capaz de (1) redactar documentos técnicos claros (requisitos, notas de diseño, informes de pruebas, resúmenes de incidentes); (2) comunicar la incertidumbre y el riesgo con honestidad; (3) adaptar los mensajes a ingenieros, directivos y reguladores; y (4) documentar componentes de IA con fichas de modelo y fichas técnicas de conjuntos de datos.

### 5.1 Los documentos del ingeniero

Los requisitos dicen lo que un sistema debe hacer y lo que no debe hacer. Las notas de diseño explican las decisiones y sus alternativas. Los informes de pruebas indican qué se probó, cómo, los resultados y los límites. Los resúmenes de incidentes indican qué ocurrió, el impacto, la causa y las acciones. Cada uno tiene un lector que debe tomar una decisión; escriba para esa decisión. Escribir para una decisión cambia lo que va primero. Un directivo que decide si desplegar TrackEye necesita el riesgo y las opciones en la primera página; un probador que repite la evaluación necesita el método completo. Sam abre cada documento con una frase que nombra a su lector y la decisión que respalda, lo que también le muestra qué puede omitir.

### 5.2 Comunicar la incertidumbre

Nunca escriba «el modelo es seguro». Escriba «en las condiciones probadas (enumeradas), la tasa de falsos negativos fue del 2,1 % (intervalo del 95 %: 1,6–2,7 %); entre las condiciones no probadas están la nieve intensa y las marcas deliberadas». Los números con intervalos y condiciones explícitas permiten a los lectores juzgar por sí mismos. Separe los *hechos* (medidos), las *valoraciones* (su juicio) y las *recomendaciones*. El intervalo indica al lector cuánto podría variar la cifra si la prueba se repitiera con datos nuevos. Enumerar las condiciones no probadas es igual de importante, porque, si no, los lectores suponen que el resultado las cubre. Mantener hechos, valoraciones y recomendaciones en párrafos separados permite que un lector que discrepa de una valoración siga confiando en las mediciones en que se apoya.

### 5.3 Documentar componentes de IA

Las fichas de modelo (*model cards*; Mitchell et al., arXiv:1810.03993) describen el uso previsto de un modelo, los usos fuera de alcance, los datos de evaluación, las métricas desglosadas por factores pertinentes y las consideraciones éticas. Las fichas técnicas de conjuntos de datos (*datasheets for datasets*; Gebru et al., arXiv:1803.09010) describen la motivación, la composición, la recogida, el preprocesamiento, los usos, la distribución y el mantenimiento. Ambas hacen visibles los supuestos ocultos para los ingenieros posteriores y los auditores. En el caso de TrackEye, la ficha técnica registra que la mayoría de las imágenes de entrenamiento procedían de recorridos diurnos sobre vía de ancho estándar, lo que explica las debilidades posteriores al amanecer y en tipos de carril poco habituales. Un equipo posterior que planee reutilizar el modelo puede ver esa limitación antes de desplegarlo, en lugar de descubrirla en servicio.

### 5.4 Públicos

Los ingenieros necesitan interfaces y modos de fallo precisos. Los directivos necesitan el riesgo, el coste y las opciones. Los reguladores y auditores necesitan evidencia trazable vinculada a los requisitos. El mismo hecho puede aparecer en tres formas. El problema de los falsos negativos al amanecer muestra las tres formas. Para los ingenieros: los falsos negativos suben al 9 % entre las 05:00 y las 07:00 a 60–80 km/h, con el conjunto de prueba identificado. Para los directivos: las inspecciones al amanecer pasan por alto más defectos, hay una corrección en marcha y existe una comprobación manual provisional. Para los auditores: el hallazgo, el requisito al que afecta, el registro de la prueba y la acción correctiva, cada uno con un identificador.

### 5.5 Estructura y trazabilidad

Numere los requisitos (REQ-SEC-012) y remita a ellos desde las notas de diseño y los informes de pruebas, de modo que cualquiera pueda seguir un requisito hasta su evidencia. Use tablas para las condiciones y los resultados, figuras para las tendencias y párrafos breves para el razonamiento. Ponga primero la conclusión y después el método para los lectores que deciden; invierta el orden para los revisores que deben comprobar el método. Versione cada documento y mantenga un registro de cambios: una evaluación que era cierta para el modelo v1.3 puede ser falsa para la v1.4. Cada entrada del registro de cambios anota qué cambió, por qué y qué resultados deja sin validez.

### 5.6 Ejemplo resuelto (caso sintético de NRS)

El primer informe de pruebas de TrackEye de Sam decía «funciona bien en la mayoría de las condiciones». El supervisor se lo devolvió. La versión revisada tenía un resumen de un párrafo para los directivos («los falsos negativos al amanecer son 4,5 veces los diurnos; corrección en curso; provisionalmente, segunda comprobación visual al amanecer»), una tabla por condición con intervalos para los ingenieros y una sección de ficha de modelo que indicaba los usos fuera de alcance (no validado para carriles de tranvía ni con nieve).

La cifra de 4,5 veces es la tasa de falsos negativos al amanecer, del 9 %, dividida entre la diurna, del 2 %. La frase original no era falsa, pero no daba a los lectores nada sobre lo que actuar. La revisión permite que cada lector encuentre lo que necesita sin leer el resto.

### 5.7 Errores y límites

- Afirmaciones absolutas («seguro», «a salvo») sin condiciones.
- Mezclar medición y opinión.
- Fichas de modelo escritas una vez y nunca actualizadas.

Las afirmaciones absolutas tientan porque suenan seguras, pero un solo contraejemplo las desmonta y, con ellas, la confianza del lector. Mezclar medición y opinión impide cuestionar una sin cuestionar la otra. Una ficha de modelo que describe la versión 1.3 adjunta a la versión 1.5 es peor que no tener ninguna, porque los lectores confían en ella; Sam vincula cada ficha a una versión del modelo y la actualiza en el mismo cambio que publica el modelo.

### Ejercicios — capítulo 5

- **EX013 — Reescritura.** Reescriba «Wrench está a salvo de la inyección de prompts» como una afirmación honesta. Rúbrica: 3 = condiciones, métrica con intervalo, áreas no probadas; 2 = dos; 1 = una; 0 = sin cambios.
- **EX014 — Ficha de modelo.** Enumere cinco secciones de una ficha de modelo para TrackEye. Rúbrica: 3 = cinco pertinentes; 2 = cuatro; 1 = dos; 0 = nada.
- **EX015 — Públicos.** Redacte el mismo hallazgo del amanecer para un directivo y para un auditor. Rúbrica: 3 = directivo: riesgo/acción; auditor: evidencia y vínculo con el requisito; 2 = uno bien; 1 = vago; 0 = nada.

### Síntesis del capítulo

Una comunicación clara y honesta (condiciones, intervalos, hechos separados de las recomendaciones, y modelos y conjuntos de datos documentados) es la forma en que la evidencia de ingeniería llega a quienes deciden.

### Siga estudiando — capítulo 05 de 50

[← Capítulo 04 (borrador)](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 (borrador) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Resultados de aprendizaje

Usted será capaz de (1) calcular derivadas parciales y gradientes de funciones de varias variables; (2) aplicar la regla de la cadena a composiciones (la base de la retropropagación); (3) aplicar aproximaciones de Taylor para estimar cambios en la salida; y (4) relacionar las normas del gradiente y las constantes de Lipschitz con la robustez.

### 6.1 Derivadas parciales y gradientes

Para f(x₁, …, xₙ), la derivada parcial ∂f/∂xᵢ mantiene fijas las demás variables. El gradiente ∇f las reúne en un vector que apunta en la dirección de máximo crecimiento. Para una puntuación lineal s = w·x + b, ∇ₓ s = w: los pesos *son* el gradiente respecto de la entrada, y por eso los modelos lineales son fáciles de atacar en la dirección de sign(w). En un modelo lineal, la dirección de ataque es por tanto visible en los propios pesos. Quien los obtenga, por ejemplo de un archivo de modelo filtrado, sabe exactamente qué características empujar y en qué sentido. En los modelos no lineales el gradiente cambia de una entrada a otra, pero el mismo razonamiento se aplica localmente alrededor de cada una.

### 6.2 La regla de la cadena multivariable

Las redes neuronales son composiciones f = f_L ∘ … ∘ f₁. La regla de la cadena multiplica matrices jacobianas capa a capa; la retropropagación calcula este producto de forma eficiente desde la salida hacia atrás. El mismo algoritmo da los gradientes respecto de las entradas, que usan los ataques de caja blanca. La retropropagación ahorra trabajo al reutilizar productos intermedios, de modo que calcular el gradiente para todas las entradas cuesta aproximadamente lo mismo que una pasada hacia delante. Esa eficiencia es la razón por la que los ataques de caja blanca son baratos: un atacante con el archivo del modelo puede calcular en milisegundos la dirección más dañina para cualquier entrada. Proteger los pesos del modelo forma parte, por tanto, de la defensa contra la evasión, no solo de la protección de la propiedad intelectual.

### 6.3 Aproximación de Taylor y cambio en el peor caso

Taylor de primer orden: f(x + δ) ≈ f(x) + ∇f(x)·δ. Si un atacante puede cambiar cada característica como máximo en ε (un presupuesto L∞), el mayor cambio de primer orden es ε·‖∇f(x)‖₁, que se alcanza con δ = ε·sign(∇f(x)), exactamente el paso de FGSM (Goodfellow et al., arXiv:1412.6572). Con un presupuesto L2, el peor cambio es ε·‖∇f(x)‖₂. Las normas importan: un gradiente con muchas componentes pequeñas puede tener, aun así, una norma L1 grande en dimensiones altas, lo que es una de las explicaciones de la vulnerabilidad adversarial de los modelos de alta dimensión. La aproximación solo es precisa para ε pequeño, así que los ingenieros la usan como estimación rápida y después prueban el modelo real con perturbaciones reales.

### 6.4 Constantes de Lipschitz

Una función es L-lipschitziana si |f(x) − f(y)| ≤ L‖x − y‖. Si el margen de un clasificador en x es m y su puntuación es L-lipschitziana, ninguna perturbación menor que m/L puede invertir la decisión: es un *certificado*. Calcular una L ajustada para redes profundas es difícil, y por eso los métodos certificados como el suavizado aleatorio (Cohen et al., arXiv:1902.02918) usan en su lugar argumentos probabilísticos. Un certificado es más fuerte que un resultado de prueba: garantiza que ningún ataque dentro del radio puede tener éxito, por ingenioso que sea. Las cotas holgadas siguen dando certificados válidos, pero el radio garantizado puede volverse demasiado pequeño para ser útil.

### 6.5 Ejemplo resuelto (caso sintético de NRS)

La puntuación de anomalía de rodamientos de Pulse es s = 0.9·t + 0.4·v − 0.2·h + c (temperatura, vibración y humedad, normalizadas). Con ε = 0,1 por característica, el peor cambio de primer orden es 0,1 × (0,9 + 0,4 + 0,2) = 0,15. Sam lo compara con el margen típico (0,3) y concluye que un atacante que suplante sensores con un límite de ±0,1 no puede ocultar un rodamiento claramente caliente, pero sí los que están en el límite. Los pesos dan directamente la peor dirección: subir la humedad y bajar la temperatura y la vibración, cada una en 0,1. Un margen de 0,3 es el doble del peor cambio, así que los rodamientos claramente calientes siguen señalados, pero cualquier rodamiento cuya puntuación esté a menos de 0,15 del umbral podría ocultarse. Sam registra esa franja como riesgo residual y propone contrastar las lecturas dudosas con un segundo sensor.

### 6.6 Errores y límites

- Usar estimaciones de primer orden lejos del punto donde son precisas.
- Confundir los presupuestos L1, L2 y L∞.
- Tratar un gradiente local como una cota global.

Las estimaciones de primer orden funcionan cerca del punto medido y dejan de ser fiables con cambios mayores, donde domina la curvatura. Mezclar normas produce cotas erróneas en un factor que crece con el número de características. Un gradiente local no dice nada sobre entradas lejanas, así que Sam siempre acompaña las estimaciones con pruebas con perturbaciones reales e indica la norma del presupuesto en cada resultado que comunica.

### Ejercicios — capítulo 6

- **EX016 — Gradiente.** Calcule ∇f para f(x, y) = x²y + 3y. Rúbrica: 3 = (2xy, x² + 3); 2 = una componente; 1 = intento; 0 = nada.
- **EX017 — Peor caso.** Para s = 2x₁ − x₂ + 0.5x₃ y ε = 0,2 (L∞), dé el mayor aumento de primer orden y δ. Rúbrica: 3 = 0,7, δ = (0,2, −0,2, 0,2); 2 = uno; 1 = método; 0 = nada.
- **EX018 — Certificado.** Una puntuación tiene margen 0,6 y constante de Lipschitz 3 (L2). ¿Qué tamaño de perturbación queda certificado como seguro? Rúbrica: 3 = < 0,2 en L2, con razonamiento; 2 = solo el número; 1 = norma equivocada; 0 = nada.

### Síntesis del capítulo

Los gradientes y las normas convierten «un cambio pequeño» en un número. Explican por qué funcionan los ataques, cómo se acotan los peores casos y por qué los certificados son posibles pero difíciles para los modelos profundos.

### Siga estudiando — capítulo 06 de 50

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Probabilidad y estadística

### Resultados de aprendizaje

Usted será capaz de (1) aplicar la regla de Bayes a problemas de detección; (2) explicar las tasas base y por qué los sucesos raros dominan la precisión de las alertas; (3) estimar tasas con intervalos de confianza; y (4) diseñar evaluaciones con suficientes muestras.

### 7.1 Probabilidad condicionada y Bayes

P(A | B) = P(B | A) P(A) / P(B). Para un detector de prompts maliciosos, la tasa de verdaderos positivos es P(alerta | malicioso) y la tasa de falsos positivos es P(alerta | benigno). Lo que interesa a los operadores es la *precisión*, P(malicioso | alerta), que depende mucho de la tasa base P(malicioso). Las dos tasas describen el detector y se mantienen más o menos fijas; la precisión describe el detector en un flujo de tráfico concreto y cambia siempre que cambia la mezcla. Sam escribe los tres números en cada informe sobre un detector, porque los operadores que solo leen la tasa de verdaderos positivos tienden a tratar cada alerta como un ataque.

### 7.2 El efecto de la tasa base

El laboratorio calcula la precisión de tres detectores para tres prevalencias. Un detector con un 95 % de TPR y un 5 % de FPR parece bueno, pero si solo 1 de cada 1.000 prompts es malicioso, menos del 2 % de sus alertas son reales. Arp et al. (arXiv:2010.09470) incluyen la falacia de la tasa base entre los errores habituales del aprendizaje automático en seguridad.

```python
"""Lab B: base rates and alarm precision (Bayes' rule).
A detector for malicious prompts with given true- and false-positive rates
is applied to traffic with different shares of malicious prompts."""
for tpr, fpr in ((0.95, 0.05), (0.95, 0.01), (0.80, 0.001)):
    for prev in (0.10, 0.01, 0.001):
        tp = tpr * prev; fp = fpr * (1 - prev)
        prec = tp / (tp + fp)
        per_10k = round(10000 * (tp + fp))
        print(f"tpr={tpr:.2f} fpr={fpr:.3f} prevalence={prev:.3f} precision={prec:.3f} alerts_per_10k={per_10k}")
```

Salida esperada:

```text
tpr=0.95 fpr=0.050 prevalence=0.100 precision=0.679 alerts_per_10k=1400
tpr=0.95 fpr=0.050 prevalence=0.010 precision=0.161 alerts_per_10k=590
tpr=0.95 fpr=0.050 prevalence=0.001 precision=0.019 alerts_per_10k=509
tpr=0.95 fpr=0.010 prevalence=0.100 precision=0.913 alerts_per_10k=1040
tpr=0.95 fpr=0.010 prevalence=0.010 precision=0.490 alerts_per_10k=194
tpr=0.95 fpr=0.010 prevalence=0.001 precision=0.087 alerts_per_10k=109
tpr=0.80 fpr=0.001 prevalence=0.100 precision=0.989 alerts_per_10k=809
tpr=0.80 fpr=0.001 prevalence=0.010 precision=0.890 alerts_per_10k=90
tpr=0.80 fpr=0.001 prevalence=0.001 precision=0.445 alerts_per_10k=18
```

Leer la tabla fila por fila muestra que reducir los falsos positivos rinde más que aumentar la detección. Con una prevalencia de 0,001, el tercer detector detecta menos ataques que el primero, pero casi la mitad de sus alertas son reales, frente a menos del 2 %, y genera 18 alertas por cada 10.000 prompts en lugar de 509.

### 7.3 Estimación de tasas

Una tasa observada k/n tiene incertidumbre. El intervalo de puntuación de Wilson es fiable incluso con n pequeño o con tasas cercanas a 0 o a 1. Comunique intervalos y dimensione los estudios para que los intervalos sean lo bastante estrechos para la decisión: n ≈ z² p(1 − p)/h² para una semiamplitud h. El intervalo de Wilson se mantiene entre 0 y 1 y se aproxima al correcto incluso cuando se observan pocos fallos, lo que importa porque los buenos sistemas producen pocos. Para una tasa en torno al 5 % y una semiamplitud de 1 punto porcentual con un 95 % de confianza, la fórmula da aproximadamente 1,96² × 0,05 × 0,95 / 0,01², unos 1.800 elementos de prueba. Sam hace esta cuenta antes de recoger datos, ya que un estudio demasiado pequeño para zanjar la cuestión hace perder el tiempo a todos.

### 7.4 Distribuciones e independencia

Los modelos binomiales cuentan éxitos en ensayos independientes. Muchas evaluaciones de seguridad violan la independencia: los prompts generados a partir de una plantilla están correlacionados, de modo que el tamaño muestral efectivo es menor. Agrupe por plantilla y remuestree los grupos (un *bootstrap por conglomerados*) al estimar intervalos. Suponga que 1.000 prompts de prueba proceden de 20 plantillas con 50 redacciones cada una. Si un filtro falla con una plantilla, probablemente falle con la mayoría de sus redacciones, de modo que la evaluación tiene más bien 20 unidades independientes que 1.000. Tratarlas como 1.000 hace el intervalo demasiado estrecho. Remuestrear plantillas enteras da una amplitud honesta y muestra además qué plantillas provocan los fallos.

### 7.5 Comparación de dos sistemas

Para decidir si un filtro nuevo es mejor que el antiguo, ejecute ambos sobre los *mismos* elementos y analice las diferencias emparejadas; así se cancela la dificultad de cada elemento. Un bootstrap emparejado (remuestrear elementos, recalcular la diferencia, tomar percentiles) da un intervalo para la mejora. Si el intervalo incluye el cero, los datos no muestran una mejora, por atractiva que sea la estimación puntual. Emparejar elimina el ruido de la dificultad de los elementos: un prompt inusualmente difícil cuenta en contra de ambos filtros, de modo que deja de ocultar la diferencia entre ellos.

### 7.6 Ejemplo resuelto (caso sintético de NRS)

El detector de inyecciones de Wrench tuvo un 95 % de TPR y un 1 % de FPR en las pruebas. Sam estimó que quizá 1 de cada 1.000 boletines de proveedores llegaría a contener un intento de inyección. Según el laboratorio, la precisión sería de aproximadamente el 8,7 %, con 109 alertas por cada 10.000 boletines, en su mayoría falsas alarmas. Sam recomendó enviar las alertas a una cola de revisión ligera en lugar de bloquear, y combinar la detección con límites de privilegios para que los ataques no detectados tengan un impacto acotado.

La cifra de 1 de cada 1.000 es en sí misma una estimación, así que Sam lee también la fila de 1 de cada 100 del laboratorio, donde la precisión sube a 0,490. En cualquier caso, bloquear cada boletín señalado bloquearía sobre todo boletines legítimos. Una cola de revisión mantiene informados a los técnicos, y los límites de privilegios hacen que la decisión no dependa de que el detector acierte.

### 7.7 Errores y límites

- Citar la exactitud en lugar de la precisión con tasas base realistas.
- Tratar muestras correlacionadas como independientes.
- Estimaciones puntuales sin intervalos.

La exactitud engaña con tasas base bajas: un detector que nunca alerta tiene un 99,9 % de exactitud cuando uno de cada mil prompts es malicioso. Las muestras correlacionadas inflan la confianza, como cuando muchos prompts comparten plantilla. Las estimaciones puntuales sin intervalos ocultan lo poco que puede mostrar una prueba pequeña. La lista de revisión de Sam hace tres preguntas a cualquier métrica: con qué tasa base, contada sobre qué unidades y con qué intervalo.

### Ejercicios — capítulo 7

- **EX019 — Precisión.** Con TPR 0,90, FPR 0,02 y prevalencia 0,005, calcule la precisión. Rúbrica: 3 = 0,0045/(0,0045 + 0,0199) ≈ 0,184; 2 = desliz; 1 = método; 0 = nada.
- **EX020 — Lectura del laboratorio.** ¿Qué detector del laboratorio da una precisión superior a 0,4 con prevalencia 0,001, y a qué coste? Rúbrica: 3 = TPR 0,80/FPR 0,001: 0,445, menor TPR; 2 = solo la fila; 1 = vago; 0 = incorrecto.
- **EX021 — Conglomerados.** ¿Por qué generar 500 prompts a partir de 5 plantillas exagera el tamaño muestral? Rúbrica: 3 = correlación dentro de cada plantilla; n efectivo más cercano a 5 grupos; usar bootstrap por conglomerados; 2 = parcial; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

La probabilidad dice a los ingenieros lo que significa realmente una alerta. Las tasas base, los intervalos honestos y las unidades de muestreo correctas deciden si un detector es útil en operación.

### Siga estudiando — capítulo 07 de 50

[← Capítulo 06 (borrador)](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 (borrador) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Arquitectura de computadores

### Resultados de aprendizaje

Usted será capaz de (1) describir las CPU, las jerarquías de memoria, las GPU y los aceleradores que se usan para el aprendizaje automático; (2) explicar los formatos numéricos y su efecto sobre el comportamiento del modelo; (3) identificar superficies de ataque arquitectónicas (aislamiento de memoria, canales laterales, firmware); y (4) razonar sobre la ejecución confiable para cargas de trabajo de IA.

### 8.1 Procesadores y aceleradores

Las CPU ejecutan instrucciones generales con cachés profundas. Las GPU y los aceleradores de IA ejecutan miles de operaciones sencillas en paralelo, lo ideal para la multiplicación de matrices. Los modelos se trasladan entre la memoria del anfitrión y la del dispositivo; en entornos de nube, los datos en la memoria del dispositivo pueden compartirse entre procesos o clientes, así que el aislamiento importa. Las copias son el problema de seguridad: los pesos cargados en una GPU, las entradas guardadas en un búfer compartido y los resultados a la espera de devolverse existen brevemente en lugares que otro cliente o un controlador descuidado podrían leer. Los proveedores de nube aíslan a sus clientes, pero los ingenieros siguen preguntando si la memoria del dispositivo se borra entre trabajos y quién puede verla, y registran las respuestas en el modelo de amenazas del despliegue.

### 8.2 Formatos numéricos

El entrenamiento suele usar coma flotante de 32 o 16 bits; la inferencia puede usar enteros de 8 bits (cuantización). Una precisión menor cambia ligeramente las salidas y puede cambiar decisiones cerca de las fronteras. Las evaluaciones de seguridad deben usar la precisión *desplegada*: un ataque o una defensa medidos en 32 bits pueden comportarse de otro modo en 8 bits, y viceversa. La cuantización asigna cada valor al más cercano de un pequeño conjunto de niveles, de modo que las entradas próximas al umbral de decisión pueden pasar al otro lado. Los gradientes calculados sobre una copia de 32 bits pueden no coincidir con el comportamiento del modelo de 8 bits, lo que puede hacer que los ataques parezcan más fuertes o más débiles de lo que son en servicio.

### 8.3 Superficies de ataque arquitectónicas

Los fallos de seguridad de memoria en el código que sirve el modelo pueden exponer pesos o entradas. Las cachés compartidas y los tiempos pueden filtrar información entre procesos (canales laterales). Los fallos de hardware, incluidos los inducidos deliberadamente, como las inversiones de bits al estilo rowhammer, pueden corromper los pesos; la investigación ha mostrado que unos pocos bits invertidos en los parámetros de una red pueden degradarla o desviarla de forma drástica. El firmware y los controladores forman parte de la base de cómputo confiable.

Para un ingeniero, cada elemento sugiere un control: lenguajes con seguridad de memoria o una revisión cuidadosa del código de servicio, aislamiento entre clientes, memoria con corrección de errores y comprobaciones de integridad de los pesos cargados. Calcular el hash del archivo de pesos antes de cargarlo detecta cambios en disco, pero no bits invertidos después en memoria, así que los despliegues críticos también comparan periódicamente las salidas sobre un conjunto de comprobación fijo.

### 8.4 Ejecución confiable y atestación

Los entornos de ejecución confiable (TEE) y las GPU de computación confidencial pretenden proteger el código y los datos en uso frente al operador del anfitrión, y la *atestación remota* permite a un cliente verificar qué código se está ejecutando. Reducen algunos riesgos (un operador de nube curioso), pero no otros (un servidor de modelos vulnerable dentro del enclave, la inyección de prompts). La atestación responde a una pregunta limitada: ¿es este el código esperado sobre hardware genuino? No dice nada sobre si ese código es seguro. Por eso los ingenieros tratan un TEE como una capa que protege frente a un operador curioso, y mantienen la validación de entradas, los límites de privilegios y la monitorización para los ataques que llegan por la interfaz normal del modelo.

### 8.5 Ejemplo resuelto (caso sintético de NRS)

TrackEye se ejecuta en un ordenador en el borde del tren de inspección con un modelo cuantizado a 8 bits. Sam descubrió que las pruebas de robustez se habían hecho con el modelo de 32 bits en el laboratorio; repetirlas con la compilación desplegada de 8 bits cambió los falsos negativos al amanecer del 9,0 % al 9,6 %. Sam añadió como requisito «evaluar sobre el artefacto y el hardware desplegados» y anotó que el puerto de mantenimiento del ordenador en el borde da acceso físico al firmware, un elemento del modelo de amenazas.

Una subida de 0,6 puntos porcentuales es pequeña, pero muestra que el resultado del laboratorio no describía el sistema que realmente funciona en el tren. El nuevo requisito hace que cada cifra de robustez futura indique el hash del artefacto y el hardware sobre los que se midió.

### 8.6 Errores y límites

- Evaluar con una precisión numérica distinta de la desplegada.
- Suponer que los TEE resuelven los ataques a nivel de aplicación.
- Ignorar el firmware y los puertos físicos de mantenimiento.

Estos errores tienen una causa común: evaluar un sistema idealizado en lugar del desplegado. La precisión usada en las pruebas es fácil de contrastar con la compilación. Las afirmaciones sobre los TEE deben leerse fijándose en lo que excluyen. Los puertos de mantenimiento suelen quedar habilitados por comodidad; la lista de comprobación de Sam pregunta, para cada puerto, si es necesario en servicio, quién puede llegar a él y si su uso queda registrado.

### Ejercicios — capítulo 8

- **EX022 — Precisión numérica.** ¿Por qué debe probarse la robustez sobre el modelo cuantizado desplegado? Rúbrica: 3 = la cuantización cambia las salidas cerca de las fronteras; los resultados pueden diferir; 2 = parcial; 1 = vago; 0 = incorrecto.
- **EX023 — Límites de los TEE.** Nombre una amenaza que un TEE mitiga y otra que no mitiga en un servicio de LLM. Rúbrica: 3 = el operador del anfitrión leyendo datos frente a la inyección de prompts/fallos del servidor; 2 = una; 1 = vago; 0 = incorrecto.
- **EX024 — Inversiones de bits.** Explique por qué las comprobaciones de integridad de los pesos en el momento de la carga no resuelven del todo los ataques por fallos. Rúbrica: 3 = los fallos pueden producirse en memoria después de la carga; hacen falta comprobaciones en tiempo de ejecución/ECC/redundancia; 2 = parcial; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

La IA se ejecuta sobre hardware real con precisión finita, recursos compartidos y firmware. Los ingenieros prueban el artefacto desplegado en la plataforma desplegada e incluyen las amenazas a nivel de arquitectura en el modelo.

### Siga estudiando — capítulo 08 de 50

[← Capítulo 07 (borrador)](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 (borrador) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Programación II

### Resultados de aprendizaje

Usted será capaz de (1) estructurar programas más grandes en módulos con interfaces claras; (2) gestionar las dependencias y sus riesgos de cadena de suministro; (3) escribir pruebas, incluidas las basadas en propiedades y las de regresión; y (4) construir un pequeño entorno de evaluación para un componente de IA.

### 9.1 Módulos e interfaces

Los programas grandes se dividen en módulos con interfaces estrechas. En los sistemas de IA, separe la *carga de datos*, la *inferencia del modelo*, la *aplicación de la política* y la *ejecución de herramientas*. El módulo de política debe ser pequeño, revisable e independiente del modelo: decide lo que está permitido con independencia de lo que diga el modelo. Es la forma en software del mínimo privilegio. Si la política depende del propio juicio del modelo, una inyección de prompts que tenga éxito también burla la política. Mantenerla en código separado hace que aplique las mismas reglas sea cual sea la forma en que se persuadió al modelo. Las interfaces estrechas también hacen posibles las revisiones: un revisor puede leer con atención un módulo de 80 líneas, pero no un sistema cuyas comprobaciones están repartidas entre prompts y scripts.

### 9.2 Dependencias y cadena de suministro

Los proyectos de IA incorporan muchas bibliotecas y archivos de modelos. Fije las versiones, verifique los hashes y prefiera la serialización segura: cargar archivos *pickle* no confiables en Python puede ejecutar código arbitrario, y por eso se prefieren, para los pesos de los modelos, formatos diseñados para contener solo tensores. OWASP LLM 2025 incluye la *cadena de suministro* (LLM03) y el *envenenamiento de datos y modelos* (LLM04). Gu et al. (arXiv:1708.06733) mostraron que un modelo con puerta trasera obtenido de un tercero puede comportarse con normalidad ante entradas limpias.

Fijar las versiones impide que una actualización cambie el comportamiento en silencio, y la comprobación de hashes impide cargar un archivo sustituido. Un modelo con puerta trasera es más difícil: puede superar todas las pruebas ordinarias, porque su comportamiento dañino solo aparece con un disparador concreto. Los ingenieros reducen este riesgo prefiriendo fuentes con procedencia publicada, registrando de dónde procede cada modelo y probando si hay comportamientos inesperados con entradas ajenas a la distribución habitual.

### 9.3 Pruebas más allá de los ejemplos

Las pruebas de regresión congelan el comportamiento conocido como correcto para que los cambios no puedan romperlo en silencio. Las pruebas basadas en propiedades generan muchas entradas y comprueban invariantes («la política nunca permite `create_work_order` sin un indicador de confirmación»). Para los componentes de IA, un *conjunto dorado* de entradas con salidas esperadas detecta la deriva de comportamiento cuando cambia un modelo o un prompt. Cada tipo detecta algo distinto. Las pruebas de regresión impiden que vuelvan fallos antiguos, las pruebas de propiedades encuentran entradas en las que nadie había pensado, y los conjuntos dorados muestran cuándo la edición de un prompt o la actualización de un modelo cambia respuestas que antes eran correctas. Los conjuntos dorados requieren cuidado, porque las salidas de los modelos varían; Sam comprueba propiedades de las respuestas, como qué herramienta se propuso, en lugar de la redacción exacta.

### 9.4 Un entorno de evaluación

Un entorno de evaluación carga un conjunto de prueba, ejecuta el componente, registra las salidas y calcula métricas con intervalos. Debe ser determinista dada una semilla, registrar las versiones (hash del modelo, versión del prompt, commit del código) y mantener los datos de prueba separados de los de desarrollo. Sin versiones registradas, un resultado no puede vincularse al sistema que describe, y una regresión posterior no puede rastrearse. El determinismo hace comparables las nuevas ejecuciones, de modo que un cambio en las métricas refleja un cambio en el sistema y no en el muestreo aleatorio. Mantener separados los datos de prueba y de desarrollo impide ajustar el sistema con los mismos ejemplos que se usan para juzgarlo, lo que haría que los resultados parecieran mejores de lo que son.

### 9.5 Ejemplo resuelto (caso sintético de NRS)

Sam reestructuró Wrench en cuatro módulos. El módulo `policy` (80 líneas) comprueba cada llamada a herramienta propuesta frente al rol del usuario y exige un token de confirmación para las órdenes de trabajo. Una prueba basada en propiedades generó 10.000 solicitudes aleatorias de llamadas a herramientas y confirmó que ninguna pasaba sin token. La revisión de dependencias encontró un script de conversión de modelos que cargaba archivos pickle desde una carpeta compartida; Sam lo sustituyó por un cargador de un formato solo de tensores y añadió la verificación de hashes. La prueba de propiedades muestrea el espacio de llamadas a herramientas de forma mucho más amplia de lo que permitirían los casos escritos a mano, aunque no demuestra que no exista ninguna llamada insegura.

### 9.6 Errores y límites

- Lógica de política incrustada en los prompts en lugar de en el código.
- Dependencias sin fijar y archivos de modelos sin verificar.
- Conjuntos dorados reutilizados para el ajuste (dejan de detectar la deriva).

Una política escrita en un prompt puede sortearse mediante la entrada del modelo; una política en código, no. Las dependencias sin fijar hacen que los resultados de las pruebas de ayer no signifiquen nada hoy. Un conjunto dorado usado durante el ajuste deja poco a poco de ser una comprobación independiente, porque el sistema se ha adaptado a él. Sam conserva un segundo conjunto, intacto, para las decisiones de publicación y lo renueva cuando cambia el uso del sistema.

### Ejercicios — capítulo 9

- **EX025 — División en módulos.** Proponga una estructura de módulos para un asistente basado en LLM con herramientas y diga qué módulo aplica la seguridad. Rúbrica: 3 = datos, inferencia, política, herramientas; política fuera del modelo; 2 = parcial; 1 = vago; 0 = nada.
- **EX026 — Pickle.** ¿Por qué es peligroso cargar un modelo no confiable en formato pickle, y cuál es la alternativa? Rúbrica: 3 = ejecución de código arbitrario al cargar; formato solo de tensores más verificación de hash; 2 = una parte; 1 = vago; 0 = incorrecto.
- **EX027 — Prueba de propiedades.** Escriba en una frase el invariante que probó Sam y otro invariante más. Rúbrica: 3 = ambos precisos; 2 = uno; 1 = vago; 0 = nada.

### Síntesis del capítulo

Una buena estructura sitúa las decisiones de seguridad en código pequeño y comprobable fuera del modelo; la disciplina con las dependencias y las pruebas mantiene esa estructura digna de confianza a medida que el sistema crece.

### Siga estudiando — capítulo 09 de 50

[← Capítulo 08 (borrador)](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 (borrador) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Ética y seguridad en la ingeniería

### Resultados de aprendizaje

Usted será capaz de (1) aplicar la ética profesional de la ingeniería a los sistemas de IA; (2) distinguir la seguridad funcional (daño accidental) de la ciberseguridad (daño intencionado) y mostrar cómo interactúan; (3) aplicar las reglas de las pruebas autorizadas y la divulgación responsable; y (4) reconocer obligaciones legales como las del Reglamento de IA de la UE para los sistemas de alto riesgo.

### 10.1 Deberes profesionales

Los códigos de ética de la ingeniería anteponen la seguridad, la salud y el bienestar públicos, exigen honestidad sobre las capacidades y los límites, y exigen competencia. En la IA, esto significa no exagerar lo que puede hacer un modelo, documentar los modos de fallo conocidos y negarse a desplegar cuando el riesgo es inaceptable. Estos deberes se aplican en los momentos corrientes, no solo en los dramáticos: una diapositiva que redondea a la baja una tasa de fallos al amanecer del 9 % hasta «alrededor del 2 %», una demostración que oculta las condiciones en que el modelo falla o un plazo que tienta a un equipo a saltarse la revisión de seguridad. La competencia incluye conocer los límites de la propia pericia y pedir ayuda, por ejemplo a un ingeniero de seguridad ferroviaria, cuando una decisión queda fuera de ellos.

### 10.2 Seguridad funcional y ciberseguridad

La ingeniería de seguridad funcional se ocupa de los fallos accidentales; la ciberseguridad, de los ataques deliberados. En la IA interactúan: una entrada adversarial puede causar un fallo de seguridad funcional (un defecto del carril no detectado), y un mecanismo de seguridad funcional (el paso a la inspección manual) puede usarse de forma abusiva para causar una denegación de servicio. El AI RMF del NIST (AI 100-1) incluye *seguro* (*safe*) y *protegido y resiliente* (*secure and resilient*) entre las características de una IA confiable y subraya que deben gestionarse conjuntamente.

Gestionarlas conjuntamente significa un único análisis de peligros que pregunte tanto qué podría fallar como qué podría hacer fallar alguien. El paso a la inspección manual es seguro frente a los accidentes, pero un atacante capaz de provocarlo repetidamente podría agotar a los inspectores y retrasar el trabajo real.

### 10.3 Pruebas autorizadas y divulgación

Pruebe solo sistemas que sean suyos o para los que tenga permiso escrito, dentro de un alcance y un plazo definidos. Nunca lance ataques contra servicios públicos de IA sin autorización; las condiciones de servicio suelen prohibirlo. Cuando encuentre una vulnerabilidad en el producto de otra persona, comuníquela en privado al fabricante y acuerden un calendario antes de publicarla (divulgación coordinada). Mantenga los datos de prueba sintéticos o debidamente gobernados; nunca extraiga ni publique datos personales. El permiso escrito indica quién puede probar, qué, cuándo y con qué métodos.

### 10.4 Legislación y regulación

El Reglamento (UE) 2024/1689 (el Reglamento de IA) clasifica algunos sistemas de IA como de alto riesgo, entre ellos los componentes de seguridad de infraestructuras críticas, y exige gestión de riesgos, gobernanza de datos, documentación técnica, registro de eventos, supervisión humana, y precisión, solidez y ciberseguridad (artículo 15). Las obligaciones se aplican por etapas de 2025 a 2027. Los ingenieros deben saber si su sistema puede entrar en una categoría regulada y recurrir a expertos jurídicos; este libro ofrece orientación, no asesoramiento jurídico. Incluso antes del asesoramiento jurídico, un ingeniero puede preparar la evidencia que necesitaría un sistema regulado: un registro de riesgos, la documentación de los conjuntos de datos, registros de las decisiones y constancia de la revisión humana. Esos registros son una buena práctica de todos modos, y reunirlos pronto evita tener que reconstruir más tarde la historia de un sistema con prisas.

### 10.5 Ejemplo resuelto (caso sintético de NRS)

Un directivo pidió a Sam que subiera el umbral de alerta de TrackEye para reducir las falsas alarmas antes de una demostración. Sam calculó que los falsos negativos subirían del 2 % al 5 % con datos diurnos. Sam documentó el compromiso, se negó a cambiar el umbral de producción sin una revisión de seguridad y propuso una configuración solo para la demostración, claramente etiquetada como tal. Sam señaló además que TrackEye, como componente de seguridad de una infraestructura ferroviaria, puede ser de alto riesgo según el Reglamento de IA, y lo remitió a revisión jurídica. La configuración de demostración cumplió el objetivo del directivo sin tocar el sistema que inspecciona la vía real.

### 10.6 Errores y límites

- Tratar la ética como algo separado de las decisiones técnicas.
- Probar servicios de IA de terceros sin permiso.
- Ocultar compromisos de seguridad en cambios de configuración.

La ética separada del trabajo técnico tiende a aparecer solo en documentos de políticas, mientras que las decisiones reales se toman en los umbrales y en los planes de prueba. Probar un servicio público de IA sin permiso puede infringir la ley incluso con buenas intenciones. Un cambio de umbral que cambia en silencio defectos no detectados por menos alarmas es una decisión de seguridad tomada sin las personas responsables de la seguridad; la regla de Sam es que cualquier cambio que afecte a las tasas de fallos de detección pase por revisión con sus números a la vista.

### Ejercicios — capítulo 10

- **EX028 — Seguridad funcional y ciberseguridad.** Dé un ejemplo en NRS en que un ataque cause un fallo de seguridad funcional y otro en que se abuse de un mecanismo de seguridad funcional. Rúbrica: 3 = ambos verosímiles; 2 = uno; 1 = confuso; 0 = nada.
- **EX029 — Divulgación.** Descubre que el modelo alojado de un proveedor filtra los prompts de otros clientes. Enumere los pasos que da. Rúbrica: 3 = detenerse, conservar la evidencia mínima, informe privado, calendario acordado, no publicar datos; 2 = parcial; 1 = vago; 0 = publicar o explotar.
- **EX030 — Reglamento de IA.** Nombre cuatro obligaciones de los sistemas de IA de alto riesgo. Rúbrica: 3 = cuatro entre gestión de riesgos, gobernanza de datos, documentación, registro de eventos, transparencia, supervisión humana, precisión/solidez/ciberseguridad; 2 = tres; 1 = una o dos; 0 = nada.

### Síntesis del capítulo

La ética en la ingeniería de IA es concreta: límites honestos, seguridad funcional y ciberseguridad gestionadas conjuntamente, pruebas autorizadas, divulgación coordinada y conciencia de las obligaciones legales de los sistemas de alto riesgo.

### Siga estudiando — capítulo 10 de 50

[← Capítulo 09 (borrador)](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 (borrador) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Redes y protocolos

### Resultados de aprendizaje

Usted será capaz de (1) explicar el recorrido de red de una solicitud a un servicio de modelos (DNS, TCP, TLS, HTTP); (2) identificar amenazas de nivel de red para los servicios de IA (interceptación, denegación de servicio, abuso de las API); (3) diseñar la segmentación de red para el entrenamiento, el servicio y los sistemas de las herramientas; y (4) interpretar los límites de tasa y las cuotas de las API como controles de seguridad.

### 11.1 El recorrido de la solicitud

Un cliente resuelve el nombre del servicio con DNS, abre una conexión TCP, negocia TLS (que autentica al servidor y cifra el tráfico) y envía una solicitud HTTP, normalmente un JSON que contiene un prompt o unas características. El servidor devuelve una respuesta, quizá transmitida token a token. Cada capa tiene sus propios modos de fallo: suplantación de DNS, configuración errónea de TLS, contrabando de solicitudes HTTP, cuerpos de tamaño excesivo. Los ingenieros revisan cada capa por separado. Los registros DNS se protegen y se monitorizan, la configuración de TLS se contrasta con las recomendaciones vigentes y la capa HTTP impone un tamaño máximo del cuerpo y un tiempo máximo de solicitud antes de que el modelo vea nada. Una solicitud rechazada en el perímetro casi no cuesta nada; la misma solicitud, si llega al modelo, puede costar segundos de tiempo de acelerador.

### 11.2 Amenazas propias de las API de IA

Además de los ataques de red clásicos, las API de IA se enfrentan a la *extracción de modelos* mediante consultas sistemáticas (Tramèr et al., arXiv:1609.02943), a la *inferencia de pertenencia* a través de las salidas de confianza y al *consumo ilimitado* (OWASP LLM10): prompts y salidas largos que agotan la capacidad de cómputo o el presupuesto. Como cada solicitud es cara, los límites ordinarios de solicitudes por segundo no bastan; las cuotas deben tener en cuenta los tokens y el cómputo.

```python
"""Lab R: token-bucket limits against unbounded consumption (synthetic).
Simulates 60 seconds of requests from a normal client and a flooding client
against a model endpoint with a per-client token bucket."""
import random
rng = random.Random(4)
def simulate(rate_per_s, burst, reqs):
    tokens, last, ok = burst, 0.0, 0
    for t in reqs:
        tokens = min(burst, tokens + (t - last) * rate_per_s); last = t
        if tokens >= 1: tokens -= 1; ok += 1
    return ok
normal = sorted(rng.uniform(0, 60) for _ in range(90))
flood = sorted(rng.uniform(0, 60) for _ in range(3000))
for rate, burst in ((5, 20), (2, 10), (1, 5)):
    print(f"limit={rate}/s burst={burst:2d} normal_served={simulate(rate, burst, normal):3d}/90 "
          f"flood_served={simulate(rate, burst, flood):4d}/3000")
```

Salida esperada:

```text
limit=5/s burst=20 normal_served= 90/90 flood_served= 319/3000
limit=2/s burst=10 normal_served= 90/90 flood_served= 129/3000
limit=1/s burst= 5 normal_served= 62/90 flood_served=  64/3000
```

El laboratorio muestra un cubo de testigos que atiende por completo a un cliente normal mientras limita a un cliente que inunda el servicio. Un límite demasiado estricto (1/s, ráfaga de 5) empieza a rechazar tráfico legítimo: los límites son un compromiso que hay que ajustar con datos de uso reales.

### 11.3 Segmentación

Sitúe los clústeres de entrenamiento, los registros de modelos, los puntos de servicio y los sistemas de las herramientas en zonas de red separadas. El servicio no debe llegar a los almacenes de datos de entrenamiento; el sistema de las herramientas de un agente basado en LLM (por ejemplo, un sistema de órdenes de trabajo) debe aceptar llamadas solo del servicio de política, no directamente del anfitrión del modelo. El filtrado de salida impide que un componente comprometido o manipulado envíe datos a destinos arbitrarios, una mitigación directa de la exfiltración mediante llamadas a herramientas inyectadas.

Las zonas se imponen con reglas de cortafuegos y se comprueban con pruebas: desde el anfitrión del modelo, una conexión al sistema de órdenes de trabajo o a una dirección externa debe fallar. Registrar estas pruebas hace que la segmentación siga verificada tras los cambios de red, en lugar de darse por supuesta.

### 11.4 Ejemplo resuelto (caso sintético de NRS)

El anfitrión del modelo de Wrench podía conectarse a internet para obtener los boletines de proveedores y también podía llamar directamente a la API de órdenes de trabajo. Sam trasladó la obtención de boletines a un servicio de ingesta separado que guarda copias depuradas, eliminó la salida a internet del anfitrión del modelo e hizo que la API de órdenes de trabajo aceptara solicitudes solo del servicio de política, con TLS mutuo. Los cambios cortaron a nivel de red ambos caminos de lo no confiable a lo privilegiado. Aunque un boletín manipule el modelo, el anfitrión del modelo no puede enviar datos al exterior ni llegar al sistema de órdenes de trabajo sin pasar por el servicio de política. Sam verifica cada cambio intentando las conexiones bloqueadas desde el anfitrión del modelo y registrando los rechazos como evidencia.

### 11.5 Errores y límites

- Límites de tasa sobre las solicitudes, pero no sobre los tokens ni el cómputo.
- Redes planas en las que el anfitrión del modelo llega a todo.
- Salida sin restricciones desde componentes que procesan texto no confiable.

Contar solo las solicitudes permite que un cliente envíe unos pocos prompts enormes que cuestan tanto como miles de prompts pequeños. Las redes planas hacen que un único componente manipulado pueda llegar a todos los sistemas. La salida sin restricciones da a las instrucciones inyectadas una vía para enviar datos al exterior. La tercera configuración del laboratorio añade otra lección: los límites ajustados sin datos de uso pueden rechazar un tercio de las solicitudes legítimas, así que las cuotas necesitan medición además de razonamiento de seguridad.

### Ejercicios — capítulo 11

- **EX031 — Lectura del laboratorio.** Con 2/s y ráfaga de 10, ¿cuántas solicitudes normales y de inundación se atienden, y por qué 1/s perjudica a los usuarios normales? Rúbrica: 3 = 90/90 y 129/3000; las ráfagas normales superan el cubo más pequeño; 2 = solo los números; 1 = vago; 0 = incorrecto.
- **EX032 — Segmentación.** Describa (con palabras) cuatro zonas para Wrench y los flujos permitidos. Rúbrica: 3 = ingesta, modelo, política, herramientas, con flujos direccionales y sin camino directo modelo→herramientas; 2 = laguna menor; 1 = vago; 0 = nada.
- **EX033 — Filtrado de salida.** Explique cómo el filtrado de salida limita el impacto de la inyección de prompts. Rúbrica: 3 = el componente manipulado no puede enviar datos a destinos del atacante; 2 = parcial; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

Los servicios de IA son servicios de red con solicitudes caras. TLS, la segmentación, el control de salida y las cuotas que tienen en cuenta el cómputo reducen la interceptación, el abuso y el impacto de los componentes manipulados.

### Siga estudiando — capítulo 11 de 50

[← Capítulo 10 (borrador)](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 (borrador) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operativos

### Resultados de aprendizaje

Usted será capaz de (1) explicar los procesos, los usuarios, los permisos y el aislamiento; (2) aislar en entornos restringidos (*sandbox*) los componentes que ejecutan acciones generadas por modelos; (3) configurar el mínimo privilegio para los procesos que sirven modelos; y (4) recoger registros del sistema operativo útiles para investigar incidentes de IA.

### 12.1 Procesos y privilegios

El sistema operativo ejecuta los programas como procesos con una identidad (usuario, grupos) e impone permisos sobre archivos, dispositivos y sockets de red. Un servidor de modelos debe ejecutarse como un usuario dedicado sin privilegios, con acceso de solo lectura a sus pesos y sin acceso de escritura a los directorios de código. Con esa configuración, un fallo o una instrucción inyectada que tome el control del proceso del servidor puede leer los pesos que ya sirve, pero no puede sustituirlos, cambiar el código del servidor ni leer archivos de otros usuarios. Ejecutarlo como root elimina todas esas barreras de golpe, y por eso los revisores comprueban primero la identidad del proceso.

### 12.2 Mecanismos de aislamiento

Los contenedores (espacios de nombres y grupos de control en Linux), las máquinas virtuales y los filtros de llamadas al sistema (seccomp) aíslan procesos. Cuando un agente de IA puede ejecutar código (una herramienta de tipo «intérprete de código»), ese código debe ejecutarse en un entorno aislado sin red, con un sistema de archivos temporal, límites de CPU y memoria y un límite de tiempo. Trate como no confiable cada cadena de código producida por un modelo, porque la inyección de prompts puede controlarla.

Los contenedores comparten el núcleo del anfitrión, de modo que un fallo del núcleo puede permitir que el código escape; las máquinas virtuales añaden una frontera más fuerte a un coste mayor. Para el código generado por un modelo, que puede ser cualquier cosa, Sam prefiere una máquina virtual dedicada o un entorno aislado reforzado con filtrado de llamadas al sistema, y desecha el entorno después de cada ejecución.

### 12.3 Límites de recursos

Los grupos de control limitan la CPU, la memoria y la cuota de GPU; sin ellos, una solicitud desmesurada puede dejar sin recursos a las demás. Es la parte, a nivel del sistema operativo, de la defensa frente al consumo ilimitado. Los límites deben fijarse a partir de mediciones. Sam perfila las solicitudes normales para conocer sus necesidades de memoria y tiempo y después fija los límites con cierto margen. Una solicitud que alcanza un límite se detiene y se registra, de modo que un patrón de solicitudes desmesuradas se hace visible. Los límites también protegen al anfitrión: un trabajador de inferencia que se queda sin memoria sin un límite puede arrastrar consigo a otros servicios de la misma máquina y convertir una solicitud mala en una caída más amplia.

### 12.4 Secretos y permisos de archivos

Los servidores de modelos necesitan a menudo credenciales: para una base de datos vectorial, la API de una herramienta o un registro. Guárdelas en el gestor de secretos de la plataforma o en archivos que solo pueda leer el usuario del servicio, nunca en prompts, volcados del entorno ni imágenes compartidas entre equipos. Se puede inducir a un modelo a revelar cualquier cosa que esté en su ventana de contexto; OWASP LLM 2025 incluye la *filtración del prompt del sistema* (LLM07) en parte porque los desarrolladores colocan secretos ahí. Mantenga las credenciales fuera del alcance del modelo y dé a cada herramienta su propia credencial de alcance estrecho.

### 12.5 Registros

Los registros del sistema (autenticación, inicios de procesos, auditorías de acceso a archivos) complementan los registros de la aplicación. En los incidentes de IA, correlacione el identificador de solicitud del modelo con los eventos del sistema operativo: ¿provocó una llamada a herramienta el inicio de un proceso o el cambio de un archivo? Un identificador de solicitud compartido es el vínculo. El servicio del modelo lo escribe con cada prompt y cada llamada a herramienta, los servicios de las herramientas lo incluyen en sus propios registros y el entorno aislado lo registra con cada proceso que inicia. Durante una investigación, una sola búsqueda muestra entonces la cadena completa, desde el boletín que llevaba una instrucción hasta el proceso que intentó ejecutarla. Los relojes deben estar sincronizados; si no, los eventos de distintos anfitriones no pueden ordenarse.

### 12.6 Ejemplo resuelto (caso sintético de NRS)

Wrench incorporó una herramienta «calculate» que ejecuta fragmentos breves de Python para cálculos de par y desgaste. Sam la ejecutó en un contenedor sin red, con raíz de solo lectura, un límite de memoria de 64 MB, un límite de CPU de 2 segundos y un perfil seccomp. Un boletín de prueba sintético con la instrucción de «calcular» algo que abría un socket de red falló de forma segura y quedó registrado. Había varias capas en el camino: no había red a la que conectarse, el perfil seccomp puede rechazar de plano las llamadas de socket y el registro anotó el identificador de solicitud, de modo que pudo rastrearse el boletín de origen. Sam conserva el boletín como prueba de regresión, para que los cambios posteriores del entorno aislado se comprueben frente a él.

### 12.7 Errores y límites

- Servidores de modelos que se ejecutan como root.
- Herramientas de código con acceso a la red.
- Trabajadores de inferencia sin límites de recursos.

Los servidores de modelos como root convierten cualquier fallo del servidor en el control total del anfitrión. Las herramientas de código con acceso a la red permiten que las instrucciones inyectadas envíen datos a cualquier parte. Los trabajadores de inferencia sin límites permiten que una solicitud deje sin recursos al resto. Cada error es fácil de detectar con una comprobación sencilla: el usuario del proceso, un intento de conexión desde dentro del entorno aislado y una solicitud deliberadamente desmesurada en preproducción, así que Sam ejecuta las tres antes de cada publicación.

### Ejercicios — capítulo 12

- **EX034 — Especificación del entorno aislado.** Escriba seis restricciones para una herramienta de ejecución de código. Rúbrica: 3 = seis entre sin red, sistema de archivos de solo lectura, directorio temporal, límites de CPU/memoria/tiempo, filtro de llamadas al sistema, usuario sin privilegios; 2 = cuatro; 1 = dos; 0 = nada.
- **EX035 — Mínimo privilegio.** Enumere tres permisos que no debería tener el proceso del servidor de modelos. Rúbrica: 3 = escritura en código/pesos, root, acceso a datos de entrenamiento/secretos, red sin restricciones; 2 = dos; 1 = uno; 0 = nada.
- **EX036 — Correlación.** ¿Por qué correlacionar los identificadores de solicitud del modelo con los registros del sistema operativo? Rúbrica: 3 = vincular las decisiones del modelo con sus efectos para la investigación; 2 = parcial; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

El aislamiento del sistema operativo convierte «el modelo podría ser manipulado» en «un modelo manipulado puede hacer poco». El mínimo privilegio, los entornos aislados, los límites de recursos y los registros correlacionados son las herramientas.

### Siga estudiando — capítulo 12 de 50

[← Capítulo 11 (borrador)](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 (borrador) →](../../en/book/MANUSCRIPT.md#ch-13)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo; cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación. Northgate Rail Systems y todos sus números son sintéticos.

**EX001.** σ(z) = (1 + e⁻ᶻ)⁻¹, de modo que σ′(z) = e⁻ᶻ/(1 + e⁻ᶻ)² = σ(z)·(1 − σ(z)), porque 1 − σ(z) = e⁻ᶻ/(1 + e⁻ᶻ). En z = 0, σ = 0,5, así que σ′ = 0,25.

**EX002.** Pérdida 0,6931 (= ln 2) y gradiente −1,000000. Cada paso mueve w en sentido opuesto al gradiente (w ← w − 0,5·dL/dw), de modo que w aumenta y la pérdida baja de 2,1269 a 0,0928.

**EX003.** El entrenamiento toma la derivada de la pérdida respecto de los parámetros y avanza para reducirla. Un atacante toma la derivada respecto de la entrada y avanza para aumentar la pérdida (o para acercarse a una clase objetivo).

**EX004.** ∀ c ∈ Calls(create_work_order): Depot(Asset(c)) = Depot(RequestingTechnician(c)).

**EX005.** Boletín del proveedor → modelo → create_work_order: tratar el texto del boletín solo como datos y exigir la confirmación del técnico. Notas editables por contratistas → modelo → create_work_order: restringir quién puede editar las notas, etiquetar su procedencia y exigir confirmación.

**EX006.** C(50,2) × 3² = 1.225 × 9 = 11.025 variantes.

**EX007.** Por encima de 800 Hz (el doble de 400 Hz); en la práctica, elija un margen, p. ej., 1–2 kHz, con un filtro antialiasing.

**EX008.** Polvo en la lente: desplazamiento natural. Patrón pintado en una traviesa: posible ataque físico adversarial (deliberado). Deriva del termistor: desplazamiento natural (envejecimiento).

**EX009.** Iluminación de 1 a 100.000 lux; velocidad del tren de 0 a 120 km/h; contaminación de la lente del 0 al 30 % de oclusión; temperatura de −20 a +45 °C; intensidad de lluvia de 0 a 50 mm/h (además: marcas a menos de 1 m del carril).

**EX010.** `TOOLS = {"search", "summarise"}; def allowed(tool): return tool in TOOLS` con `assert allowed("search") and not allowed("email")`.

**EX011.** `eval` ejecuta el texto como Python, de modo que un texto influido por un atacante (p. ej., mediante inyección de prompts) se convierte en ejecución de código arbitrario. OWASP LLM05 Improper Output Handling (manejo inadecuado de la salida).

**EX012.** JSON no válido; objeto vacío; campo de más; asset_id con signos de puntuación o que no es una cadena; prioridad fuera del conjunto; resumen extremadamente largo.

**EX013.** «En nuestra prueba en entorno aislado (200 boletines sintéticos con instrucciones inyectadas, modelo v1.3, plantilla de prompt v2), Wrench emitió una orden de trabajo no autorizada en 3 de 200 tareas (intervalo de Wilson del 95 %: 0,5–4,3 %); no se probaron las inyecciones multilingües ni las basadas en imágenes».

**EX014.** Detalles del modelo (versión, responsable); uso previsto y usos fuera de alcance; datos de evaluación; métricas desglosadas por condición (luz, velocidad, tipo de carril); consideraciones éticas y salvedades.

**EX015.** Directivo: «Al amanecer, TrackEye pasa por alto unas 4,5 veces más defectos que de día; hasta que se publique la corrección, añadimos una segunda comprobación visual en los recorridos al amanecer». Auditor: «El informe de pruebas TR-031 (v1.3) muestra una tasa de falsos negativos al amanecer del 9 % frente al 2 % diurno, contra REQ-SAF-004 (≤3 %); se abrió la no conformidad NC-07; control provisional documentado».

**EX016.** ∂f/∂x = 2xy; ∂f/∂y = x² + 3; ∇f = (2xy, x² + 3).

**EX017.** Aumento = ε·‖w‖₁ = 0,2 × (2 + 1 + 0,5) = 0,7, con δ = ε·sign(w) = (0,2, −0,2, 0,2).

**EX018.** Ninguna perturbación L2 menor que margen/L = 0,6/3 = 0,2 puede cambiar el signo de la puntuación.

**EX019.** VP = 0,90 × 0,005 = 0,0045; FP = 0,02 × 0,995 = 0,0199; precisión = 0,0045/0,0244 ≈ 0,184.

**EX020.** TPR 0,80 y FPR 0,001 dan una precisión de 0,445 con prevalencia 0,001 (18 alertas por cada 10.000), a costa de no detectar el 20 % de los ataques.

**EX021.** Los prompts de una misma plantilla comparten estructura, de modo que sus resultados están correlacionados; la información se parece más a 5 grupos independientes que a 500 ensayos. Remuestree plantillas (bootstrap por conglomerados) y comunique los resultados por plantilla.

**EX022.** La cuantización desplaza ligeramente las puntuaciones, de modo que las entradas cercanas a la frontera de decisión pueden invertirse; las tasas de éxito de los ataques y de error medidas en el modelo de 32 bits pueden no mantenerse en el despliegue de 8 bits.

**EX023.** Mitiga: que un operador del anfitrión en la nube lea prompts o pesos en memoria. No mitiga: la inyección de prompts ni los fallos del servidor de modelos que se ejecuta dentro del enclave.

**EX024.** Un fallo puede invertir bits después de la comprobación del hash en la carga, durante la inferencia. Entre las mitigaciones están la memoria ECC, el recálculo periódico del hash, la computación redundante y las comprobaciones de verosimilitud de las salidas.

**EX025.** `ingest` (carga los datos y los etiqueta con su procedencia), `inference` (llamadas al modelo), `policy` (comprueba cada acción propuesta frente al rol, el alcance y la confirmación), `tools` (ejecuta las acciones aprobadas). El módulo de política aplica la seguridad, fuera del modelo.

**EX026.** Deserializar con pickle ejecuta el código incrustado en el archivo, de modo que un archivo de modelo malicioso compromete la máquina al cargarse. Use un formato solo de tensores (sin código) y verifique un hash fijado procedente de una fuente confiable.

**EX027.** «No se ejecuta ninguna llamada a `create_work_order` a menos que lleve un token de confirmación válido del técnico solicitante». Otro: «Ninguna llamada a herramienta se dirige a un activo fuera del depósito del usuario solicitante».

**EX028.** Ataque → seguridad funcional: unas marcas colocadas cerca de los carriles hacen que TrackEye no detecte un defecto real. Abuso de un mecanismo de seguridad funcional: provocar deliberadamente muchas alertas de baja confianza para que el sistema pase a la lenta inspección manual y retrase el servicio (denegación de servicio).

**EX029.** Dejar de probar; registrar la evidencia mínima sin conservar datos de otros; informar en privado al contacto de seguridad del proveedor; acordar un calendario de corrección y divulgación; publicar solo después de la corrección y sin datos personales.

**EX030.** Sistema de gestión de riesgos; gobernanza de datos; documentación técnica; conservación de registros/registro de eventos; transparencia hacia los responsables del despliegue; supervisión humana; precisión, solidez y ciberseguridad.

**EX031.** 90/90 normales y 129/3000 de inundación. Con 1/s y ráfaga de 5, las ráfagas naturales del cliente normal superan el cubo, de modo que solo se atienden 62 de 90: el límite es demasiado estricto.

**EX032.** Zona de ingesta (obtiene y depura los boletines; puede conectarse a internet) → zona del modelo (sin internet; lee el almacén depurado) → zona de política (recibe las acciones propuestas por el modelo; comprueba el rol y la confirmación) → zona de herramientas (la API de órdenes de trabajo solo acepta al servicio de política mediante TLS mutuo). Sin camino directo modelo→herramientas.

**EX033.** Aunque un texto inyectado haga que un componente intente enviar datos al exterior, las reglas de salida bloquean las conexiones a destinos que no están en una lista de permitidos, así que la exfiltración fracasa.

**EX034.** Sin red; sistema de archivos raíz de solo lectura; directorio temporal con escritura; límites de CPU, memoria y tiempo real; filtro de llamadas al sistema; usuario sin privilegios (sin capacidades).

**EX035.** Derechos de root o de administración; acceso de escritura al código o a los pesos; acceso a datos de entrenamiento, secretos o credenciales que no necesita; salida de red sin restricciones.

**EX036.** Vincula una decisión del modelo (y el prompt que la causó) con efectos concretos, como inicios de procesos o cambios de archivos, que es como los investigadores establecen lo que realmente hizo una instrucción inyectada.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; los marcos cambian, así que vuelva a verificarlos. Los identificadores de arXiv se abrieron y se comprobaron sus títulos. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Abadi, M. et al. (2016). Deep Learning with Differential Privacy. arXiv:1607.00133.
- Arp, D. et al. (2020). Dos and Don'ts of Machine Learning in Computer Security. arXiv:2010.09470.
- Athalye, A., Carlini, N., Wagner, D. (2018). Obfuscated Gradients Give a False Sense of Security. arXiv:1802.00420.
- Carlini, N. et al. (2019). On Evaluating Adversarial Robustness. arXiv:1902.06705.
- Carlini, N. et al. (2023). Poisoning Web-Scale Training Datasets is Practical. arXiv:2302.10149.
- Chen, S. et al. (2024). StruQ: Defending Against Prompt Injection with Structured Queries. arXiv:2402.06363.
- Cohen, J., Rosenfeld, E., Kolter, J. Z. (2019). Certified Adversarial Robustness via Randomized Smoothing. arXiv:1902.02918.
- European Union. Regulation (EU) 2024/1689 (Artificial Intelligence Act). <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
- Gebru, T. et al. (2018). Datasheets for Datasets. arXiv:1803.09010.
- Goodfellow, I., Shlens, J., Szegedy, C. (2014). Explaining and Harnessing Adversarial Examples. arXiv:1412.6572.
- Greshake, K. et al. (2023). Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. arXiv:2302.12173.
- Gu, T., Dolan-Gavitt, B., Garg, S. (2017). BadNets. arXiv:1708.06733.
- ISO/IEC 42001:2023 Artificial intelligence — Management system. <https://www.iso.org/standard/81230.html>
- Liu, Y. et al. (2023). Prompt Injection attack against LLM-integrated Applications. arXiv:2306.05499.
- Madry, A. et al. (2017). Towards Deep Learning Models Resistant to Adversarial Attacks. arXiv:1706.06083.
- MITRE ATLAS. <https://atlas.mitre.org/>
- Mitchell, M. et al. (2018). Model Cards for Model Reporting. arXiv:1810.03993.
- NIST AI 100-1 (2023), AI RMF 1.0. <https://doi.org/10.6028/NIST.AI.100-1>
- NIST AI 100-2 E2025 (2025), Adversarial Machine Learning taxonomy. <https://doi.org/10.6028/NIST.AI.100-2e2025>
- NIST AI 600-1 (2024), Generative AI Profile. <https://doi.org/10.6028/NIST.AI.600-1>
- OWASP Top 10 for LLM Applications 2025. <https://genai.owasp.org/llm-top-10/>
- Shokri, R. et al. (2016). Membership Inference Attacks against Machine Learning Models. arXiv:1610.05820.
- Tramèr, F. et al. (2016). Stealing Machine Learning Models via Prediction APIs. arXiv:1609.02943.
