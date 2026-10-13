# Seguridad de la IA y del aprendizaje automático: libro del curso de grado

- Idioma: español neutro (`es`); curso de grado, cuatro años; aproximadamente 3.200 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–40 de 40 tienen texto didáctico de autor; los ejercicios EX001–EX120 (tres por capítulo) tienen sus resultados resueltos correspondientes con rúbricas de 0 a 3; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas impresas proceden de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no equivale a un libro terminado.
- Público: estudiantes de seguridad y computación en sentido amplio que necesitan una base rigurosa y práctica sobre cómo se atacan, se defienden, se gobiernan y se evalúan los sistemas de IA.
- Relación con los libros vecinos: el [libro de tecnólogo](../../../../technologist-3-years/ai-security/en/book/MANUSCRIPT.md) se centra más en la implementación; el [libro de ingeniería](../../../../engineering-5-years/ai-security/es/book/MANUSCRIPT.md) pone más peso en el diseño. **Este libro equilibra teoría, casos, métodos y habilidades de investigación**, y termina con un proyecto final y un trabajo de fin de grado.
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado y no concede autorización para probar sistemas reales. Todas las organizaciones, personas, conjuntos de datos y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Cuarenta capítulos siguen el grado: fundamentos (1–18); teoría, casos, métodos y laboratorios de seguridad de la IA (19–32); e investigación, proyecto final y trabajo de fin de grado (33–40). Cada capítulo tiene resultados de aprendizaje, texto didáctico, un ejemplo resuelto, errores y límites, tres ejercicios puntuados de 0 a 3 (0 ausente o inseguro; 1 laguna importante; 2 lagunas menores; 3 completo y justificado), una síntesis y un bloque **Siga estudiando**. Los laboratorios son deterministas, se ejecutan sin conexión con `python3 file.py` e imprimen los resultados que aparecen bajo *Salida esperada*. Son modelos de juguete, no defensas de producción.

### El ejemplo conductor (sintético): Lumen Community Health

> **Caso sintético — ficción.** **Lumen Community Health (LCH)** es una red inventada de cinco clínicas. Opera **Ask Lumen**, un chatbot basado en un modelo de lenguaje que responde a preguntas de pacientes sobre citas y servicios de las clínicas a partir de documentos recuperados de las clínicas y que puede reservar o cancelar citas mediante una herramienta; **NoShow**, un modelo que predice las citas a las que el paciente no acudirá; y **DocSort**, un modelo que lee cartas de derivación escaneadas y las encamina. La estudiante *Rina Costa* sigue a LCH a lo largo del grado en trabajos de curso, un laboratorio y un proyecto final. Todos los números sobre LCH son inventados; todas las pruebas se hacen en copias aisladas con historiales de pacientes sintéticos y autorización por escrito.

### Política de fuentes

Las fuentes se comprobaron el 12 de octubre de 2026: NIST [AI 100-1](https://doi.org/10.6028/NIST.AI.100-1) (AI RMF 1.0), [AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) (perfil de IA generativa) y [AI 100-2 E2025](https://doi.org/10.6028/NIST.AI.100-2e2025) (taxonomía de aprendizaje automático adversario); el [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [MITRE ATLAS](https://atlas.mitre.org/); el [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) (Reglamento de IA); y la [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html). Los artículos se citan por su identificador de arXiv; cada uno se abrió y se comprobó su título.

## Contenido

| Parte | Capítulos |
|---|---|
| Fundamentos | [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](../../en/book/MANUSCRIPT.md#ch-07) · [8](../../en/book/MANUSCRIPT.md#ch-08) · [9](../../en/book/MANUSCRIPT.md#ch-09) · [10](../../en/book/MANUSCRIPT.md#ch-10) · [11](../../en/book/MANUSCRIPT.md#ch-11) · [12](../../en/book/MANUSCRIPT.md#ch-12) · [13](../../en/book/MANUSCRIPT.md#ch-13) · [14](../../en/book/MANUSCRIPT.md#ch-14) · [15](../../en/book/MANUSCRIPT.md#ch-15) · [16](../../en/book/MANUSCRIPT.md#ch-16) · [17](../../en/book/MANUSCRIPT.md#ch-17) · [18](../../en/book/MANUSCRIPT.md#ch-18) |
| Seguridad de la IA y del aprendizaje automático | [19](../../en/book/MANUSCRIPT.md#ch-19) · [20](../../en/book/MANUSCRIPT.md#ch-20) · [21](../../en/book/MANUSCRIPT.md#ch-21) · [22](../../en/book/MANUSCRIPT.md#ch-22) · [23](../../en/book/MANUSCRIPT.md#ch-23) · [24](../../en/book/MANUSCRIPT.md#ch-24) · [25](../../en/book/MANUSCRIPT.md#ch-25) · [26](../../en/book/MANUSCRIPT.md#ch-26) · [27](../../en/book/MANUSCRIPT.md#ch-27) · [28](../../en/book/MANUSCRIPT.md#ch-28) · [29](../../en/book/MANUSCRIPT.md#ch-29) · [30](../../en/book/MANUSCRIPT.md#ch-30) · [31](../../en/book/MANUSCRIPT.md#ch-31) · [32](../../en/book/MANUSCRIPT.md#ch-32) |
| Investigación y proyecto final | [33](../../en/book/MANUSCRIPT.md#ch-33) · [34](../../en/book/MANUSCRIPT.md#ch-34) · [35](../../en/book/MANUSCRIPT.md#ch-35) · [36](../../en/book/MANUSCRIPT.md#ch-36) · [37](../../en/book/MANUSCRIPT.md#ch-37) · [38](../../en/book/MANUSCRIPT.md#ch-38) · [39](../../en/book/MANUSCRIPT.md#ch-39) · [40](../../en/book/MANUSCRIPT.md#ch-40) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Razonamiento matemático

### Resultados de aprendizaje

Usted podrá (1) leer y escribir enunciados matemáticos precisos; (2) usar técnicas de demostración (directa, por contradicción, por contraejemplo) para razonar sobre afirmaciones de seguridad; (3) trabajar con funciones, vectores y optimización sencilla; y (4) ver por qué un único contraejemplo derriba una afirmación universal de seguridad.

### 1.1 Enunciados y cuantificadores

Las afirmaciones de seguridad son enunciados matemáticos disfrazados. «Ask Lumen nunca revela la cita de otro paciente» significa: *para todas* las entradas y *para todos* los usuarios, la salida no contiene datos de otro paciente. Un enunciado universal («para todo») se refuta con un contraejemplo; un enunciado existencial («existe un ataque») se demuestra exhibiendo uno. Esta asimetría explica por qué los atacantes tienen ventaja: necesitan una entrada que funcione, mientras que los defensores deben cubrirlas todas. Escribir la afirmación por extenso deja a la vista lo que hay que comprobar: cada usuario, cada entrada, cada vía por la que los datos llegan a la salida, incluidos los documentos recuperados y los resultados de las herramientas.

### 1.2 Técnicas de demostración

La *demostración directa* deriva la conclusión de los supuestos. La *demostración por contradicción* supone lo contrario y deriva una imposibilidad. La *demostración por contraejemplo* refuta una afirmación universal. En seguridad de la IA, las demostraciones son raras para sistemas completos pero comunes para componentes: «si el servicio de políticas deniega toda llamada a herramientas sin un token válido, no se produce ninguna reserva no autenticada» es una demostración directa a partir de una propiedad de diseño. La demostración basada en la propiedad de diseño solo vale lo que vale su supuesto: si alguna vía llega al sistema de reservas sin pasar por el servicio de políticas, la conclusión falla. Comprobar ese supuesto es una tarea de arquitectura, que capítulos posteriores automatizan con búsqueda en grafos.

### 1.3 Funciones y vectores

Un modelo es una función de entradas a salidas. Entradas como imágenes o registros de atributos son vectores; la distancia entre vectores (por ejemplo, la distancia euclidiana o la máxima diferencia absoluta) formaliza la idea de «cambio pequeño». Muchos ataques buscan un vector cercano que produzca una salida distinta (Szegedy et al., arXiv:1312.6199). La elección de la distancia importa. Con la máxima diferencia absoluta, todos los atributos pueden cambiar a la vez hasta una cantidad fija; con la distancia euclidiana, un cambio grande en un solo atributo agota todo el presupuesto. El laboratorio de evasión usa más adelante el primer tipo, de modo que su tamaño de perturbación eps acota por separado el cambio en cada coordenada. Una afirmación de robustez no significa nada hasta que se declaran la distancia y su tamaño.

### 1.4 Optimización

El entrenamiento minimiza una función de pérdida; los ataques la maximizan (o minimizan la distancia con la condición de que la salida cambie). Ambos son problemas de optimización, por eso las mismas herramientas matemáticas —gradientes, restricciones, búsqueda— aparecen en los dos lados. El laboratorio de evasión muestra ambos lados en pocas líneas. El entrenamiento ajusta los pesos en contra del gradiente de la pérdida para reducir el error; el ataque mueve cada punto de prueba según el signo de ese mismo gradiente respecto a la entrada para aumentar el error. Con eps de 0,5, la exactitud del modelo de juguete cae de 0,985 a 0,840, lo que muestra el poco esfuerzo que necesita una búsqueda guiada por el gradiente cuando el modelo es sencillo.

### 1.5 Ejemplo resuelto (caso sintético de LCH)

El proveedor de LCH afirmaba: «NoShow no puede ser manipulado por los pacientes». Rina lo reescribió como enunciado universal: para todos los pacientes y todos los valores de los campos que controlan los pacientes (preferencias de contacto, motivo declarado de la visita), la predicción no cambia en un sentido que el paciente prefiera. Después encontró un contraejemplo en un registro sintético: cambiar el «motivo» de «seguimiento» a «urgente» bajó el riesgo previsto de inasistencia de 0,42 a 0,18, lo que podría hacer subir a un paciente en una lista de recordatorios. La afirmación era falsa tal como estaba formulada; el proveedor la revisó.

### 1.6 Errores y límites

- Aceptar afirmaciones universales probadas con unos pocos ejemplos.
- Confundir «no se encontró ningún ataque» con «no existe ningún ataque».
- Nociones vagas de «cambio pequeño» sin medida de distancia.

El ejemplo de NoShow muestra los tres. La afirmación del proveedor se había probado solo con registros ordinarios; nadie había buscado un cambio en un campo que controlan los pacientes; y «manipulado» no tenía una medida declarada. El contraejemplo de Rina, un cambio de 0,42 a 0,18 causado por un solo campo, zanjó la cuestión de inmediato. Una afirmación revisada nombraría los campos, el tamaño de cambio que se considera aceptable y cómo se probó.

### Ejercicios

- **EX001 — Cuantificadores.** Escriba «el filtro bloquea todos los intentos de inyección» con cuantificadores explícitos y diga qué la refuta. Rúbrica: 3 = ∀ entradas de la clase, bloqueadas; una instancia no bloqueada la refuta; 2 = parcial; 1 = vago; 0 = nada.
- **EX002 — Contraejemplo.** ¿Por qué un solo registro refutó la afirmación del proveedor? Rúbrica: 3 = afirmación universal falsada por una instancia; 2 = parcial; 1 = vago; 0 = incorrecto.
- **EX003 — Distancia.** Para x = (1; 2; 3) e y = (1,5; 2; 2), calcule las distancias euclidiana y de máxima diferencia absoluta. Rúbrica: 3 = √(0,25 + 0 + 1) ≈ 1,118 y 1; 2 = una; 1 = método; 0 = nada.

### Síntesis

El razonamiento matemático hace precisas las afirmaciones de seguridad. Las afirmaciones universales necesitan evidencia sólida; un contraejemplo basta para refutarlas; «pequeño» necesita una distancia.

### Siga estudiando — capítulo 01 de 40

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Sistemas de computación

### Resultados de aprendizaje

Usted podrá (1) describir cómo encajan los ordenadores, los sistemas operativos, las redes y los servicios en la nube; (2) identificar dónde se ejecuta una aplicación de IA y dónde almacena datos; (3) explicar el modelo de responsabilidad compartida para la nube y la IA alojada; y (4) mapear un servicio de IA a sus componentes de computación.

### 2.1 Capas de un sistema de computación

El hardware ejecuta un sistema operativo, que ejecuta aplicaciones; las aplicaciones se comunican por redes con otros servicios, a menudo en la nube. Una aplicación de IA añade archivos de modelo, servidores de inferencia, bases de datos vectoriales y conexiones con API de modelos externas. Cada capa tiene sus propios responsables y modos de fallo. En Ask Lumen, las piezas adicionales son el modelo alojado, la base de datos vectorial de documentos de las clínicas y la herramienta de reservas. Cada una añade responsables: el proveedor del modelo, el equipo de datos de LCH y los administradores del sistema de citas. Un problema de seguridad en cualquiera de ellas, como una base de datos mal configurada, afecta al chatbot aunque el modelo funcione correctamente. Conocer las capas le dice a Rina a quién preguntar por cada riesgo.

### 2.2 Dónde se ejecuta la IA

Un modelo puede ejecutarse en el dispositivo del usuario, en los servidores de la organización o en un proveedor mediante una API. Cada opción cambia quién puede ver los datos, quién puede cambiar el modelo y quién puede probarlo. Las API de IA alojadas procesan las instrucciones en la infraestructura del proveedor; la organización controla solo su propio código, su configuración y los datos que envía. Ask Lumen usa una API alojada, así que LCH no puede inspeccionar los pesos del modelo ni parchearlo; solo puede elegir qué envía y cómo trata lo que recibe. Eso convierte el propio código de LCH, la parte que construye las instrucciones y comprueba las salidas, en el lugar principal donde se pueden añadir controles.

### 2.3 Responsabilidad compartida

En la computación en la nube, el proveedor protege la infraestructura y el cliente protege lo que pone sobre ella. En la IA alojada, el proveedor suele responder del alojamiento del modelo y de la seguridad de la plataforma; el cliente responde de qué datos envía, cómo se usan las salidas, qué herramientas puede activar el modelo y quién puede acceder a la aplicación. Entender mal este reparto es una causa habitual de incidentes. En el mapa de Rina, la cuenta de servicio de reservas es el ejemplo más claro: el proveedor del modelo no tiene ningún control sobre lo que esa cuenta puede hacer en el sistema de citas de LCH.

### 2.4 Mapear un servicio de IA

Enumere: interfaz de usuario; servidor de aplicaciones; modelo (dónde y qué versión); almacén de recuperación; herramientas y los sistemas que tocan; registros; identidades usadas en cada paso. Este mapa es el punto de partida de todos los capítulos posteriores. Cada elemento responde a una pregunta que haría un atacante o un investigador: dónde entra la entrada, dónde reposan los datos, qué puede cambiar el sistema y bajo qué identidad. Un mapa que solo enumera el modelo pierde la mayor parte de la superficie de ataque, porque en Ask Lumen las acciones de riesgo ocurren a través de la herramienta de reservas y del almacén de recuperación. Rina mantiene su mapa en un documento compartido y lo actualiza cada vez que LCH cambia un componente.

### 2.5 Ejemplo resuelto (caso sintético de LCH)

Rina mapeó Ask Lumen: widget de chat web → servidor de aplicaciones de LCH (máquina virtual en la nube) → API de modelo de lenguaje alojada (proveedor) → recuperación desde una base de datos vectorial de documentos de las clínicas (gestionada por LCH) → herramienta de reservas que llama al sistema de citas (local) con una cuenta de servicio. Los registros iban al servicio de registros del proveedor de nube. Rina anotó que la cuenta de servicio de reservas podía reservar para cualquier paciente: una responsabilidad que debe corregir LCH, no el proveedor del modelo. El mapa también muestra quién debe actuar sobre cada hallazgo: la cuenta de servicio pertenece al equipo de citas de LCH, y la corrección consiste en restringirla al paciente cuya sesión hizo la petición.

### 2.6 Errores y límites

- Suponer que el proveedor del modelo protege toda la aplicación.
- Olvidar las herramientas y los registros en el mapa.
- No saber qué versión del modelo está en uso.

Cada error oculta parte del riesgo. Suponer que el proveedor lo protege todo deja sin examinar la cuenta de servicio de LCH. Omitir las herramientas y los registros oculta las vías por las que el chatbot puede actuar sobre datos de pacientes o registrarlos. No saber la versión del modelo impide distinguir si un cambio de comportamiento vino de que el proveedor actualizó el modelo o del propio código de LCH.

### Ejercicios

- **EX004 — Responsabilidad.** Para Ask Lumen, enumere dos responsabilidades del proveedor y tres de LCH. Rúbrica: 3 = reparto correcto; 2 = error menor; 1 = confuso; 0 = nada.
- **EX005 — Mapa.** Mapee un asistente de IA para deberes escolares en los siete componentes de 2.4. Rúbrica: 3 = los siete plausibles; 2 = cinco; 1 = tres; 0 = nada.
- **EX006 — Elección de despliegue.** Dé una ventaja de seguridad de los modelos en el dispositivo y una de las API alojadas. Rúbrica: 3 = los datos quedan en local frente a parcheo/escala gestionados por el proveedor; 2 = una; 1 = vago; 0 = incorrecto.

### Síntesis

Las aplicaciones de IA son sistemas de computación con piezas adicionales. Mapear dónde se ejecuta cada pieza y quién responde de ella es el primer paso de seguridad.

### Siga estudiando — capítulo 02 de 40

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Programación I

### Resultados de aprendizaje

Usted podrá (1) escribir programas sencillos en Python con variables, condiciones, bucles, funciones y listas; (2) leer los laboratorios de este libro; (3) tratar la entrada de forma segura; y (4) probar funciones pequeñas.

### 3.1 Por qué la programación importa en seguridad de la IA

El trabajo de seguridad necesita evidencia, y la evidencia sale de ejecutar cosas: evaluar un modelo con un conjunto de prueba, analizar registros, comprobar archivos. Incluso los programas cortos le hacen más rápido y más preciso. Los laboratorios de este libro usan solo la biblioteca estándar de Python, así que funcionan en cualquier ordenador. El primer script útil de Rina midió con qué frecuencia las respuestas de prueba de Ask Lumen citaban un documento de la clínica, una comprobación que a mano habría llevado horas. Escribirlo también la obligó a definir qué contaba como cita, una pregunta más precisa que aquella con la que había empezado. Los laboratorios con la biblioteca estándar evitan problemas de dependencias, así que un compañero puede volver a ejecutar su trabajo y obtener los mismos números.

### 3.2 Construcciones básicas

Las variables guardan valores; `if` elige; `for` repite; las funciones empaquetan pasos; las listas y los diccionarios guardan colecciones. Lea el laboratorio de evasión que sigue: crea datos sintéticos, entrena con un bucle un modelo diminuto de regresión logística y después mide la exactitud a medida que crece una perturbación. Todavía no necesita entender cada línea; céntrese en la estructura: datos, entrenamiento, evaluación, impresión.

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

La salida muestra el patrón con claridad: la exactitud es 0,985 sin perturbación y cae a 0,505 cuando eps llega a uno, cerca de adivinar al azar. La semilla aleatoria fija hace que cada ejecución imprima los mismos números.

### 3.3 Tratar la entrada de forma segura

Los programas que leen archivos, datos de red o salidas de IA deben tratarlos como no confiables. Convierta el texto en números con cuidado, compruebe los rangos y nunca ejecute texto como código. Un error habitual en las aplicaciones con LLM es pasar la salida del modelo a un comando o a una página web sin comprobaciones; el OWASP LLM 2025 lo llama *improper output handling* (manejo inadecuado de la salida, LLM05). En Ask Lumen, la reserva que sugiere el modelo es una entrada como cualquier otra: debe analizarse como datos, comprobarse contra reglas y solo entonces pasarse al sistema de citas. El ejemplo resuelto de este capítulo hace exactamente eso con tres comprobaciones del código de clínica, la fecha y el identificador del paciente.

### 3.4 Pruebas

Escriba pruebas pequeñas con `assert`: `assert classify(0.9) == "high"`. Pruebe los casos límite: entrada vacía, valores extremos, tipos incorrectos. Las pruebas hacen que sea seguro cambiar el código más adelante. En la comprobación de reservas de Rina, los casos límite incluyen una fecha exactamente a 90 días, una fecha pasada, un código de clínica desconocido, un identificador de paciente ausente y una petición con el identificador de otro paciente. Cada caso recibe una prueba con el resultado esperado escrito al lado. Cuando más tarde cambia la regla de fechas, las pruebas existentes muestran de inmediato si algo más se ha roto.

### 3.5 Ejemplo resuelto (caso sintético de LCH)

Rina escribió una función que comprueba una petición de reserva producida por Ask Lumen antes de que llegue al sistema de citas: el código de clínica debe ser uno de cinco códigos conocidos, la fecha debe estar dentro de 90 días y el identificador del paciente debe coincidir con el usuario que ha iniciado sesión. Sus pruebas incluían una petición con el identificador de otro paciente, que la función rechazó. Comprobar en código, fuera del modelo, significa que la regla se cumple aunque una instrucción persuada al modelo de pedir la reserva de otro paciente.

### 3.6 Errores y límites

- Copiar código sin entender lo que hace.
- Confiar en la salida de la IA como si fuera código propio.
- Probar solo el caso normal.

El código copiado puede incluir comportamientos que quien lo copió nunca advirtió, como una llamada insegura que ejecuta texto como comando. Confiar en la salida de la IA como si fuera código propio repite ese error con un autor menos cuidadoso. Probar solo el caso normal deja sin probar justamente las vías que usa un atacante; la prueba de Rina con el identificador de otro paciente es del tipo que detecta problemas reales.

### Ejercicios

- **EX007 — Estructura del laboratorio.** Identifique las partes de datos, entrenamiento, evaluación y salida del laboratorio de evasión. Rúbrica: 3 = las cuatro localizadas correctamente; 2 = tres; 1 = una o dos; 0 = nada.
- **EX008 — Lectura del laboratorio.** ¿Qué exactitud informa el laboratorio con eps 0.00 y 0.50? Rúbrica: 3 = 0,985 y 0,840; 2 = una; 1 = aproximada; 0 = incorrecta.
- **EX009 — Validación.** Enumere las tres comprobaciones de la función de reservas de Rina y una más que podría añadir. Rúbrica: 3 = código de clínica, ventana de fechas, coincidencia del paciente + extra razonable (formato de franja horaria, límite de frecuencia); 2 = solo las tres; 1 = una o dos; 0 = nada.

### Síntesis

La programación convierte las ideas de seguridad en evidencia. Lea los laboratorios buscando la estructura, trate toda entrada externa —incluida la salida de la IA— como no confiable y pruebe los límites.

### Siga estudiando — capítulo 03 de 40

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Escritura académica

### Resultados de aprendizaje

Usted podrá (1) escribir prosa académica clara con afirmaciones respaldadas por evidencia; (2) citar fuentes correctamente y verificar cada cita; (3) distinguir entre investigación revisada por pares, preprints, normas y literatura gris; y (4) evitar el plagio, incluido el mal uso de herramientas de escritura con IA.

### 4.1 Afirmaciones y evidencia

Toda afirmación sustantiva necesita respaldo: datos que usted produjo, una fuente citada o un argumento claro. En seguridad de la IA, las afirmaciones sobre ataques y defensas deben declarar sus condiciones: qué modelo, qué ataque, qué métrica. «El entrenamiento adversario hace robustos los modelos» es demasiado amplio; «el entrenamiento adversario con descenso de gradiente proyectado mejoró la robustez frente a perturbaciones acotadas en los bancos de pruebas de imágenes evaluados (Madry et al., arXiv:1706.06083)» se puede sostener. La versión sostenible nombra el método, el modelo de amenaza y el alcance de la evaluación, de modo que el lector puede saber si se aplica a su sistema. Una afirmación sobre bancos de pruebas de imágenes dice poco de un chatbot de texto como Ask Lumen.

### 4.2 Citación y verificación

Cite lo que realmente leyó y compruebe que cada referencia existe: abra el DOI, la página de arXiv o la URL oficial. No invente identificadores. Los asistentes de escritura con IA pueden producir referencias verosímiles pero inexistentes; cada cita que entrega es responsabilidad suya. Use un estilo coherente e incluya información suficiente para que el lector encuentre la fuente. El ejemplo resuelto de Rina muestra que el riesgo es real: una de seis referencias producidas con un asistente no existía. Comprobarlas lleva minutos por referencia y protege la credibilidad del ensayo. Ella anota dónde verificó cada una, por ejemplo la página del DOI, para que quien corrija pueda seguir el mismo camino.

### 4.3 Tipos de fuentes

Los artículos revisados por pares han sido comprobados por expertos; los preprints (por ejemplo, en arXiv) suelen ser importantes en seguridad de la IA, pero no están revisados; las normas y los marcos (NIST AI 100-1, ISO/IEC 42001) definen términos y prácticas; los blogs de proveedores y las noticias son pistas útiles, pero evidencia débil. El tipo de fuente determina cómo se redacta una afirmación. Un resultado revisado por pares puede citarse como hallazgo bajo sus condiciones declaradas; un preprint, como resultado comunicado y aún no revisado; un blog de proveedor, como una afirmación. En los ensayos de Rina, una afirmación respaldada solo por un blog de proveedor se escribe como «el proveedor afirma», lo que indica al lector cuánto peso darle.

### 4.4 Integridad y herramientas de IA

Siga la política de su institución sobre herramientas de IA. Normalmente debe declarar su uso, comprobar su salida y no presentar nunca como trabajo propio texto o análisis generados sin permiso. Parafrasear sin citar es plagio. La declaración permite a quienes corrigen juzgar el trabajo con justicia y a los lectores saber qué partes comprobar con más cuidado. La declaración de Rina indica la herramienta, la tarea en la que ayudó y cómo comprobó ella la salida. La referencia inventada de su borrador muestra por qué importa comprobar: la herramienta la produjo con seguridad, y solo la verificación la puso al descubierto.

### 4.5 Ejemplo resuelto (caso sintético de LCH)

El primer borrador de ensayo de Rina, producido en parte con un asistente de IA, contenía seis referencias. Las comprobó: cuatro existían, una tenía el año equivocado y otra no existía en absoluto. Eliminó la referencia inventada, corrigió el año, declaró el uso de la herramienta y reescribió el párrafo que dependía de la fuente falsa usando una real que había leído. Una tasa de una referencia fabricada de cada seis es lo bastante alta como para que ahora compruebe cada referencia antes de redactar en torno a ella.

### 4.6 Errores y límites

- Referencias sin verificar.
- Afirmaciones sin condiciones.
- Tratar un blog de proveedor como un hecho establecido.

Las referencias sin verificar pueden estar equivocadas o ser inventadas, como mostró el borrador de Rina, y una sola falsa hace que los lectores duden del resto. Las afirmaciones sin condiciones, como «el entrenamiento adversario hace robustos los modelos», son fáciles de refutar con un contraejemplo de otro contexto. Tratar los blogs de proveedores como hechos establecidos hace pasar el marketing por evidencia. Cada error es barato de evitar y caro una vez que lo encuentra quien corrige o revisa.

### Ejercicios

- **EX010 — Reescritura.** Reescriba «la inyección de instrucciones se resuelve con filtros» como una afirmación sostenible o como una refutación con una cita. Rúbrica: 3 = afirmación condicional que cita trabajo real (p. ej., Greshake et al. arXiv:2302.12173) que muestra que los filtros son insuficientes; 2 = parcial; 1 = sin cita; 0 = sin cambios.
- **EX011 — Verificación.** Describa cómo verificar una referencia de arXiv. Rúbrica: 3 = abrir arxiv.org/abs/ID y comprobar que título/autores/año coinciden; 2 = parcial; 1 = vago; 0 = nada.
- **EX012 — Tipo de fuente.** Clasifique: NIST AI 600-1; un artículo de arXiv; un blog de empresa. Rúbrica: 3 = norma/marco, preprint, literatura gris; 2 = dos; 1 = una; 0 = nada.

### Síntesis

La escritura académica en seguridad de la IA significa afirmaciones condicionales, citas verificadas y un uso honesto de las herramientas: habilidades que también hacen fiables los informes profesionales.

### Siga estudiando — capítulo 04 de 40

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Alfabetización en seguridad

### Resultados de aprendizaje

Usted podrá (1) explicar la confidencialidad, la integridad y la disponibilidad; (2) definir amenaza, vulnerabilidad, riesgo y control; (3) describir ataques comunes (*phishing*, malware, robo de credenciales) y sus variantes en la era de la IA; y (4) aplicar prácticas básicas de seguridad personales y organizativas.

### 5.1 La tríada CIA

La *confidencialidad* mantiene la información fuera del alcance de personas no autorizadas; la *integridad* la mantiene exacta y sin alterar; la *disponibilidad* mantiene los sistemas utilizables cuando se necesitan. Para un chatbot de IA: confidencialidad de los datos de pacientes en las conversaciones; integridad de las respuestas y las reservas; disponibilidad del servicio. En Ask Lumen, un fallo de confidencialidad sería mostrar a un paciente la cita de otro; un fallo de integridad sería una respuesta errónea sobre el horario de una clínica o una reserva hecha para la persona equivocada; un fallo de disponibilidad sería que el chatbot no pudiera usarse durante una mañana de mucha actividad. Cada uno necesita controles distintos, así que nombrar la propiedad en riesgo ayuda a elegir el adecuado.

### 5.2 Vocabulario del riesgo

Una *amenaza* es algo que podría causar daño (un atacante, un accidente). Una *vulnerabilidad* es una debilidad. El *riesgo* combina probabilidad e impacto. Un *control* reduce el riesgo. Un vocabulario preciso ayuda a los equipos a ponerse de acuerdo sobre las prioridades. Aplicado a Ask Lumen: una amenaza es un paciente que intenta ver las citas de otro; la vulnerabilidad es la cuenta de servicio de reservas, que puede actuar en nombre de cualquier paciente; el riesgo es la probabilidad de esa combinación multiplicada por el daño de exponer datos de salud; el control es una comprobación de políticas que vincula cada reserva al paciente que ha iniciado sesión. Usar las palabras de forma coherente evita que las discusiones mezclen problemas con soluciones.

### 5.3 Ataques clásicos y variantes con IA

El *phishing* engaña a las personas para que revelen credenciales; la IA puede generar *phishing* más convincente y personalizado, y clonar voces. El malware compromete dispositivos; el código generado por IA puede contener vulnerabilidades si se acepta sin crítica. El robo de credenciales da acceso a los atacantes; las credenciales pegadas en chatbots pueden filtrarse. Y los sistemas de IA introducen nuevos tipos de ataque: inyección de instrucciones, envenenamiento de datos, extracción de modelos y evasión. Los nuevos tipos de ataque afectan a las mismas tres propiedades: la inyección de instrucciones amenaza la integridad de las acciones, la extracción amenaza la confidencialidad del modelo y el envenenamiento amenaza la integridad de los datos de entrenamiento.

### 5.4 Prácticas básicas

Use autenticación multifactor, mantenga el software actualizado, aplique el mínimo privilegio, haga copias de seguridad de los datos importantes y comunique los eventos sospechosos. Con herramientas de IA: no pegue secretos ni datos personales en servicios no aprobados, compruebe las salidas antes de actuar y siga la política de la organización sobre herramientas aprobadas. Estas prácticas se aplican al trabajo con IA tanto como a cualquier otro: una clave de API del proveedor del modelo es una credencial que necesita el mismo cuidado que una contraseña. En LCH se indica al personal qué herramientas de IA están aprobadas para el trabajo relacionado con pacientes y que nunca deben pegarse datos de pacientes en otras. Comprobar la salida de la IA antes de actuar es el hábito que habría detectado la referencia inventada de Rina.

### 5.5 Ejemplo resuelto (caso sintético de LCH)

Una recepcionista de LCH recibió un mensaje de voz que parecía de una directora de clínica y que pedía cambiar con urgencia los datos bancarios de un proveedor. La sesión de formación en alfabetización en seguridad de Rina usó este caso sintético para hablar de la clonación de voz y del control que la detiene: verificar los cambios de pago mediante un número de teléfono conocido y un segundo aprobador, por convincente que suene la petición. El control funciona tanto si la voz es real como si es clonada, por eso aquí el proceso gana a la detección. LCH también indicó al personal que la urgencia en una petición de pago es en sí misma un motivo para ir más despacio y verificar.

### 5.6 Errores y límites

- Tratar los riesgos específicos de la IA como ajenos a la seguridad clásica.
- Confiar en detectar falsificaciones en lugar de en controles de proceso.
- Pegar datos sensibles en herramientas públicas de IA.

Los riesgos específicos de la IA suelen reutilizar vías clásicas: una voz clonada es *phishing* por otro medio, y una clave de API filtrada es robo de credenciales. Confiar en detectar falsificaciones falla a medida que mejora la generación, mientras que la verificación por devolución de llamada sigue funcionando. Pegar datos sensibles en herramientas públicas puede exponerlos a la retención del proveedor y a cualquiera que obtenga después esos datos, por eso la política de LCH nombra explícitamente las herramientas aprobadas.

### Ejercicios

- **EX013 — CIA.** Dé un ejemplo de confidencialidad, uno de integridad y uno de disponibilidad para DocSort. Rúbrica: 3 = un ejemplo de cada, exactos; 2 = dos; 1 = uno; 0 = nada.
- **EX014 — Vocabulario.** Para el caso de la voz clonada, indique amenaza, vulnerabilidad, impacto y control. Rúbrica: 3 = los cuatro coherentes; 2 = tres; 1 = uno o dos; 0 = nada.
- **EX015 — Prácticas.** Enumere tres prácticas seguras para usar asistentes de IA en el trabajo. Rúbrica: 3 = sin secretos/datos personales, verificar las salidas, solo herramientas aprobadas; 2 = dos; 1 = una; 0 = nada.

### Síntesis

La alfabetización en seguridad —CIA, vocabulario del riesgo, ataques comunes y prácticas básicas— es la base sobre la que se construye la seguridad específica de la IA.

### Siga estudiando — capítulo 05 de 40

[← Capítulo 04 (borrador)](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 (borrador) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Estructuras discretas

### Resultados de aprendizaje

Usted podrá (1) usar conjuntos, relaciones y grafos para modelar sistemas; (2) expresar reglas de acceso como relaciones y comprobarlas; (3) encontrar en un grafo caminos desde entradas no confiables hasta acciones sensibles; y (4) contar posibilidades para juzgar si la fuerza bruta es viable.

### 6.1 Conjuntos y relaciones

Una regla de control de acceso es una relación entre sujetos, acciones y objetos: (paciente P, reservar, cita propia) está permitido; (paciente P, ver, historial de otro paciente) no lo está. Escribir las reglas como conjuntos de triples permitidos las hace comprobables por programa y deja a la vista los casos que faltan. Una vez que las reglas son un conjunto, un programa puede comprobar cada petición contra él y enumerar cualquier acción que no tenga ninguna regla. El primer intento de Rina descubrió que «cancelar» no tenía regla para pacientes que cancelan la cita de otra persona, algo que la política en prosa simplemente no mencionaba. Añadir una denegación explícita cerró la laguna, y el conjunto se convirtió en la referencia de sus comprobaciones de reservas.

### 6.2 Grafos

Un grafo tiene nodos y aristas. Dibuje un sistema de IA como un grafo dirigido: usuario → chatbot → modelo → herramienta de reservas → sistema de citas, más almacén de documentos → modelo. Un camino desde un nodo no confiable (una página web pública, un documento subido) hasta un nodo sensible (la herramienta de reservas) es una posible ruta de ataque. La inyección indirecta de instrucciones sigue exactamente esos caminos (Greshake et al., arXiv:2302.12173). Dibujar el grafo hizo visible una arista que el documento de arquitectura había pasado por alto: las organizaciones asociadas suben documentos al almacén que lee el modelo.

### 6.3 Búsqueda en grafos

La búsqueda en anchura encuentra todos los nodos alcanzables desde un nodo de partida. Ejecutarla desde cada nodo no confiable y comprobar si se alcanzan nodos sensibles es una comprobación de arquitectura sencilla y automatizable. El coste crece con el número de nodos y aristas, así que incluso los sistemas grandes pueden comprobarse en segundos. El valor está en mantener el grafo exacto: una nueva fuente de subidas o una nueva herramienta deben añadirse en cuanto existen, o la búsqueda dará un resultado limpio para un sistema que ya no se corresponde con él. Rina vuelve a ejecutar la comprobación cada vez que cambia el mapa de arquitectura y guarda la salida junto al mapa.

### 6.4 Contar

Si un código de reserva tiene 6 dígitos, hay 10⁶ posibilidades; a 10 intentos por segundo, un atacante necesita unas 28 horas para probarlas todas, así que los límites de frecuencia y los bloqueos importan. Contar convierte la intuición en números. Con un bloqueo tras cinco intentos fallidos, un atacante tiene cinco intentos por cuenta en lugar de un millón: una probabilidad de éxito de cinco entre un millón. La misma aritmética se aplica a adivinar identificadores de pacientes a través del chatbot: si los identificadores son cortos y secuenciales, enumerarlos es barato. Rina incluye estos cálculos en sus revisiones para que los ajustes de los límites de frecuencia se apoyen en números y no en impresiones.

### 6.5 Ejemplo resuelto (caso sintético de LCH)

Rina enumeró los nodos y las aristas de Ask Lumen e hizo a mano una comprobación de alcanzabilidad. Dos fuentes no confiables llegaban a la herramienta de reservas: el chat de pacientes (esperado, controlado por la autenticación) y las subidas de documentos de clínica por organizaciones asociadas (inesperado). Las subidas de los asociados podían contener texto con forma de instrucción que el modelo podría seguir. LCH añadió una revisión de los documentos de los asociados y mantuvo la herramienta de reservas detrás de una comprobación de políticas vinculada al paciente que ha iniciado sesión. El segundo camino explica por qué se mantuvieron ambos controles y no uno: la revisión reduce la probabilidad de texto hostil, y la comprobación de políticas limita su efecto.

### 6.6 Errores y límites

- Reglas de acceso escritas solo en prosa.
- Grafos que omiten almacenes de datos y subidas.
- Ignorar lo rápido que los ordenadores enumeran posibilidades.

Las reglas en prosa dejan casos sin definir, como mostró la regla de cancelación que faltaba. Los grafos que omiten las subidas y los almacenes de datos pierden justamente la ruta por la que la inyección indirecta de instrucciones llega a una herramienta. Subestimar la velocidad de enumeración lleva a límites débiles sobre códigos e identificadores; un código de seis dígitos sin límites de frecuencia cae en aproximadamente un día a solo diez intentos por segundo, y mucho más rápido con más.

### Ejercicios

- **EX016 — Relación.** Escriba tres triples permitidos y dos prohibidos para Ask Lumen. Rúbrica: 3 = cinco triples razonables; 2 = cuatro; 1 = dos; 0 = nada.
- **EX017 — Caminos.** Nombre el camino inesperado que encontró Rina y un control. Rúbrica: 3 = subidas de asociados → modelo → reservas; revisión más política vinculada al paciente; 2 = solo el camino; 1 = vago; 0 = nada.
- **EX018 — Contar.** Un código de 4 dígitos a 5 intentos por segundo: ¿tiempo en el peor caso? Rúbrica: 3 = 10.000/5 = 2.000 s ≈ 33 min; 2 = desliz; 1 = método; 0 = nada.

### Síntesis

Las estructuras discretas dan herramientas exactas —relaciones para las reglas, grafos para el flujo de datos, conteo para la viabilidad— que hacen visibles las debilidades de los sistemas de IA.

### Siga estudiando — capítulo 06 de 40

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](../../en/book/MANUSCRIPT.md#ch-07)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo; cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación. Lumen Community Health, Rina y todos sus números son sintéticos.

**EX001.** «Para toda entrada x del conjunto de intentos de inyección, Filter(x) = bloqueada». Un solo intento de inyección que no se bloquee la refuta.

**EX002.** La afirmación era universal (para todos los pacientes y todos los valores controlables); un registro sintético cuya predicción se movió a favor del paciente es un contraejemplo, así que la afirmación es falsa.

**EX003.** Euclidiana: √(0,5² + 0² + 1²) = √1,25 ≈ 1,118. Máxima diferencia absoluta: max(0,5; 0; 1) = 1.

**EX004.** Proveedor: proteger la plataforma de alojamiento del modelo; mantener disponible y parcheado el servicio del modelo alojado. LCH: qué datos de pacientes se envían en las instrucciones; restringir los permisos de la herramienta de reservas; controlar quién puede usar el chatbot y cómo se muestran las salidas.

**EX005.** Interfaz: portal web del centro escolar; servidor de aplicaciones: la aplicación del centro; modelo: API alojada, versión X; recuperación: índice de materiales del curso; herramientas: ninguna o «entregar borrador»; registros: registros de la aplicación y del proveedor; identidades: cuenta SSO del estudiante, clave de servicio de la aplicación.

**EX006.** En el dispositivo: los datos no salen del dispositivo. API alojada: el proveedor se encarga del parcheo, el escalado y la supervisión del servicio del modelo.

**EX007.** Datos: la función `point` y las listas `train`/`test`. Entrenamiento: el bucle de gradiente de 200 épocas que actualiza `w` y `b`. Evaluación: la función `acc`, que aplica la perturbación. Salida: las líneas `print` de los pesos y de la exactitud para cada eps.

**EX008.** 0,985 con eps 0.00 y 0,840 con eps 0.50.

**EX009.** Código de clínica dentro del conjunto conocido; fecha dentro de 90 días; identificador del paciente igual al usuario que ha iniciado sesión. Extra: comprobación del formato de la franja horaria, o un límite de reservas por usuario y día.

**EX010.** «Los filtros de contenido reducen, pero no eliminan, la inyección de instrucciones; la inyección indirecta a través de contenido recuperado ha comprometido aplicaciones reales integradas con LLM (Greshake et al., arXiv:2302.12173), así que las acciones con consecuencias necesitan controles fuera del modelo».

**EX011.** Abra https://arxiv.org/abs/ seguido del identificador y compruebe que el título, los autores y el año coinciden con la referencia; anote la versión si importa.

**EX012.** NIST AI 600-1: norma/marco (guía gubernamental). Artículo de arXiv: preprint. Blog de empresa: literatura gris.

**EX013.** Confidencialidad: las cartas de derivación contienen datos de salud. Integridad: encaminar mal una carta retrasa la atención. Disponibilidad: si DocSort no funciona, las cartas se acumulan sin procesar.

**EX014.** Amenaza: un estafador con una voz clonada. Vulnerabilidad: se aceptan cambios de pago por teléfono. Impacto: el dinero se envía al estafador. Control: verificar mediante un número conocido y un segundo aprobador.

**EX015.** No pegar nunca secretos ni datos personales en herramientas no aprobadas; comprobar las salidas antes de actuar en consecuencia; usar solo servicios de IA aprobados por la organización.

**EX016.** Permitidos: (paciente P, reservar, cita de P); (paciente P, cancelar, cita de P); (paciente P, leer, información pública de la clínica). Prohibidos: (paciente P, leer, cita de Q); (paciente P, reservar, cita para Q).

**EX017.** Subidas de documentos de asociados → modelo → herramienta de reservas. Control: revisar los documentos de los asociados antes de indexarlos y aplicar mediante una comprobación de políticas que solo se reserve para el paciente que ha iniciado sesión.

**EX018.** 10.000 / 5 = 2.000 segundos ≈ 33 minutos.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; los marcos cambian, así que vuelva a verificarlos. Los identificadores de arXiv se abrieron y se comprobaron sus títulos. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Abadi, M. et al. (2016). Deep Learning with Differential Privacy. arXiv:1607.00133.
- Arp, D. et al. (2020). Dos and Don'ts of Machine Learning in Computer Security. arXiv:2010.09470.
- Athalye, A., Carlini, N., Wagner, D. (2018). Obfuscated Gradients Give a False Sense of Security. arXiv:1802.00420.
- Carlini, N. et al. (2019). On Evaluating Adversarial Robustness. arXiv:1902.06705.
- Carlini, N. et al. (2020). Extracting Training Data from Large Language Models. arXiv:2012.07805.
- Carlini, N. et al. (2023). Poisoning Web-Scale Training Datasets is Practical. arXiv:2302.10149.
- Chen, S. et al. (2024). StruQ: Defending Against Prompt Injection with Structured Queries. arXiv:2402.06363.
- Cohen, J., Rosenfeld, E., Kolter, J. Z. (2019). Certified Adversarial Robustness via Randomized Smoothing. arXiv:1902.02918.
- Hubinger, E. et al. (2024). Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training. arXiv:2401.05566.
- Kapoor, S., Narayanan, A. (2022). Leakage and the Reproducibility Crisis in ML-based Science. arXiv:2207.07048.
- Lipton, Z. C., Steinhardt, J. (2018). Troubling Trends in Machine Learning Scholarship. arXiv:1807.03341.
- Szegedy, C. et al. (2013). Intriguing properties of neural networks. arXiv:1312.6199.
- Unión Europea. Reglamento (UE) 2024/1689 (Reglamento de Inteligencia Artificial). <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
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
- Wei, A., Haghtalab, N., Steinhardt, J. (2023). Jailbroken: How Does LLM Safety Training Fail? arXiv:2307.02483.
- Zou, A. et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models. arXiv:2307.15043.
