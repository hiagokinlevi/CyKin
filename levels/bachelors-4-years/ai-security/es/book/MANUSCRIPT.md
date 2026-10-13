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
| Fundamentos | [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](../../en/book/MANUSCRIPT.md#ch-13) · [14](../../en/book/MANUSCRIPT.md#ch-14) · [15](../../en/book/MANUSCRIPT.md#ch-15) · [16](../../en/book/MANUSCRIPT.md#ch-16) · [17](../../en/book/MANUSCRIPT.md#ch-17) · [18](../../en/book/MANUSCRIPT.md#ch-18) |
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

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Redes y protocolos

### Resultados de aprendizaje

Usted podrá (1) explicar cómo viaja por internet una petición a un chatbot (DNS, TCP, TLS, HTTP); (2) describir qué protege TLS y qué no; (3) explicar la autenticación de API y la limitación de frecuencia; y (4) relacionar los controles de red con amenazas de la IA como la extracción y el agotamiento de recursos.

### 7.1 El camino de una petición

El navegador busca el dominio del chatbot (DNS), se conecta (TCP), establece un canal cifrado y autenticado (TLS) y envía una petición HTTP que contiene el mensaje. El servidor de aplicaciones puede a su vez llamar a una API de modelo por otra conexión TLS. Cada paso deja un registro que puede ayudar en una investigación: la consulta DNS, el establecimiento de la conexión TLS en el balanceador de carga, la petición HTTP en el servidor de aplicaciones y la llamada saliente al proveedor del modelo. En Ask Lumen, por tanto, un solo mensaje de un paciente atraviesa dos conexiones cifradas, y el servidor de aplicaciones es el único lugar donde LCH ve el texto en claro. Ahí es donde corresponden las comprobaciones de la entrada, el registro y las decisiones de política.

### 7.2 Qué hace TLS y qué no

TLS protege los datos en tránsito contra la escucha y la manipulación, y autentica al servidor. No protege contra un mensaje malicioso de un usuario autenticado, contra la inyección de instrucciones dentro del contenido ni contra el mal uso de los datos una vez que llegan. En Ask Lumen, TLS garantiza que el mensaje de un paciente llega al servidor de LCH sin ser leído ni modificado y que el paciente habla con el sitio real de LCH. No hace nada respecto a un paciente que escribe una instrucción diseñada para manipular el modelo, ni respecto a un documento de un asociado que lleva texto oculto. Esos problemas están dentro del canal protegido y necesitan controles en la aplicación.

### 7.3 Autenticación de API y limitación de frecuencia

Las API autentican a quienes las llaman con claves o tokens. Los límites de frecuencia y las cuotas acotan cuánto puede usar cada cliente. En las API de IA, los costes crecen con los tokens, así que los límites deben contar tokens, no solo peticiones. OWASP LLM10 (*unbounded consumption*, consumo ilimitado) cubre los ataques que agotan recursos o presupuestos.

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

El Laboratorio R muestra el compromiso. Con 5 peticiones por segundo y una ráfaga de 20, se atienden todas las peticiones normales y la avalancha obtiene 319 de 3.000. Con 1 por segundo y una ráfaga de 5, la avalancha baja a 64, pero el cliente normal pierde 28 de sus 90 peticiones. Un límite debe fijarse a partir del uso normal medido, no elegirse solo para detener ataques.

### 7.4 Amenazas a la IA a nivel de red

Las consultas sistemáticas pueden copiar un modelo (Tramèr et al., arXiv:1609.02943). Las avalanchas de instrucciones largas pueden agotar la capacidad. Los controles de red —autenticación, cuotas, supervisión, segmentación y filtrado de salida— reducen estos riesgos y limitan lo que puede alcanzar un componente comprometido. La extracción necesita muchas consultas, así que las cuotas por cliente y la vigilancia de patrones de consulta inusuales aumentan su coste. El filtrado de salida importa si un componente se ve comprometido: un servidor de inferencia que solo puede alcanzar al proveedor del modelo no puede enviar datos a otro sitio. La segmentación mantiene los servidores del chatbot separados de la base de datos de citas, salvo a través de la interfaz estrecha de la herramienta de reservas.

### 7.5 Ejemplo resuelto (caso sintético de LCH)

El punto de acceso público del chat de Ask Lumen no tenía límites por sesión. Una prueba de carga sintética que enviaba instrucciones largas multiplicó por diez los costes del modelo en una hora. LCH añadió cuotas de tokens por sesión, una longitud máxima de mensaje y una alerta cuando el gasto supera el 150 % de la mediana diaria. Contar tokens en lugar de peticiones fue el cambio clave: unas pocas instrucciones muy largas habían costado más que miles de mensajes normales. El umbral de alerta del 150 % de la mediana diaria detecta el abuso en cuestión de horas sin reaccionar a la subida normal de las mañanas de mucha actividad, y la longitud máxima de mensaje impide que una sola instrucción consuma una parte grande del presupuesto.

### 7.6 Errores y límites

- Creer que TLS resuelve los ataques a nivel de aplicación.
- Límites de peticiones que ignoran el coste en tokens.
- Claves de API incrustadas en el código del navegador.

TLS protege el canal, no el contenido, así que la inyección de instrucciones y el abuso por parte de usuarios con sesión iniciada lo atraviesan sin obstáculos. Los límites que solo cuentan peticiones permiten a un atacante enviar menos instrucciones, pero mucho más largas, como mostró la prueba de carga de LCH. Las claves de API en el código del navegador puede leerlas cualquiera que abra la página, lo que le permite llamar directamente al proveedor del modelo y saltarse por completo las cuotas de LCH; las claves deben estar en el servidor.

### 7.6b Tiempos de espera y reintentos en las llamadas al modelo

Ask Lumen llama al proveedor del modelo a través de la red, y las respuestas lentas tientan a los ingenieros a reintentar de forma agresiva. Cada reintento reenvía la pregunta del paciente y cuesta dinero; los reintentos ilimitados durante una caída pueden multiplicar el tráfico y agotar el límite de frecuencia de todas las clínicas. LCH limita los reintentos a dos con una espera creciente y muestra a los pacientes un número de teléfono cuando el modelo no está disponible. Una espera creciente entre reintentos permite que un proveedor en apuros se recupere en lugar de verse inundado. El número de teléfono mantiene atendidos a los pacientes mientras el chatbot no funciona.

### Ejercicios

- **EX019 — TLS.** Nombre dos cosas que TLS protege y dos que no. Rúbrica: 3 = confidencialidad/integridad en tránsito, autenticación del servidor frente a contenido malicioso, inyección/mal uso; 2 = tres; 1 = una o dos; 0 = nada.
- **EX020 — Lectura del laboratorio.** En el laboratorio, ¿por qué el límite de 1/s con ráfaga de 5 perjudica a los usuarios normales? Rúbrica: 3 = solo se atienden 62/90 porque las ráfagas naturales superan el cubo; 2 = solo el número; 1 = vago; 0 = incorrecto.
- **EX021 — Claves.** ¿Por qué las claves de API del modelo no deben aparecer en el código del navegador? Rúbrica: 3 = cualquiera puede leerlas y usarlas indebidamente, lo que causa costes y abuso; usar llamadas desde el servidor; 2 = parcial; 1 = vago; 0 = incorrecto.

### Síntesis

Las redes entregan los servicios de IA; TLS, la autenticación, las cuotas que tienen en cuenta los tokens y la supervisión protegen la entrega, pero no el contenido, del que se ocupan capítulos posteriores.

### Siga estudiando — capítulo 07 de 40

[← Capítulo 06 (borrador)](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 (borrador) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Programación II

### Resultados de aprendizaje

Usted podrá (1) organizar programas en módulos y funciones con responsabilidades claras; (2) usar JSON y archivos de forma segura; (3) gestionar paquetes de terceros y archivos de modelo con comprobaciones de integridad; y (4) escribir pruebas que incluyan casos adversarios.

### 8.1 Módulos y responsabilidades

Divida los programas de modo que cada parte tenga una sola tarea. En una aplicación con LLM: tratamiento de la entrada, recuperación, llamada al modelo, comprobación de políticas, ejecución de herramientas, registro. Mantener la comprobación de políticas en su propio módulo pequeño significa que puede revisarse y probarse con independencia del modelo. La separación también limita el daño: si se manipula el módulo de recuperación para que devuelva un documento hostil, la comprobación de políticas sigue decidiendo por su cuenta si se permite cualquier llamada a herramientas que resulte de ello. En Ask Lumen, las comprobaciones de reservas que Rina escribió en el capítulo de programación viven en un módulo así, con pruebas que se ejecutan en cada cambio. Un revisor puede leer el módulo completo en pocos minutos.

### 8.2 JSON y archivos

Analice los datos estructurados con analizadores estrictos (`json.loads`) y valide campos, tipos y rangos. Rechace los campos desconocidos. Nunca use `eval` sobre datos. Cuando se pide al modelo que produzca JSON, valídelo de la misma manera, porque el modelo puede producir salidas mal formadas o manipuladas. En Ask Lumen, se pide al modelo que devuelva una reserva como JSON con un código de clínica, una fecha y un identificador de paciente. El analizador rechaza cualquier campo adicional, como una instrucción para cancelar otras citas, y cualquier valor fuera de los rangos permitidos. Una respuesta mal formada lleva a un mensaje de fallo cortés para el paciente, nunca a una acción parcial.

### 8.3 Paquetes y archivos de modelo

Instale paquetes desde fuentes de confianza y con versiones fijadas. Los archivos de modelo son riesgos parecidos al código: algunos formatos de serialización pueden ejecutar código al cargarse. Verifique el hash SHA-256 de un archivo contra un manifiesto de confianza antes de cargarlo; el laboratorio detecta así la manipulación.

```python
"""Lab H: integrity of model artefacts with SHA-256 manifests (stdlib only).
Creates synthetic 'artefact' bytes, records a manifest, then detects a
one-byte tampering and a swapped file. No real models are involved."""
import hashlib, json
files = {"model.bin": bytes(range(256)) * 40, "tokenizer.json": b'{"vocab": ["a", "b"]}',
         "config.yaml": b"layers: 4\nheads: 8\n"}
manifest = {n: hashlib.sha256(b).hexdigest() for n, b in files.items()}
print(json.dumps({k: v[:16] for k, v in manifest.items()}, indent=1))
received = dict(files)
tampered = bytearray(received["model.bin"]); tampered[5000] ^= 1
received["model.bin"] = bytes(tampered)
received["config.yaml"] = b"layers: 4\nheads: 8\ntrust_remote_code: true\n"
for n, b in sorted(received.items()):
    ok = hashlib.sha256(b).hexdigest() == manifest[n]
    print(f"{n:15s} {'OK' if ok else 'MISMATCH'}")
```

Salida esperada:

```text
{
 "model.bin": "e96760a87768717b",
 "tokenizer.json": "f63d2ddabc61f2d9",
 "config.yaml": "e5bbb570ca0fcb87"
}
config.yaml     MISMATCH
model.bin       MISMATCH
tokenizer.json  OK
```

En el Laboratorio H, un solo bit invertido en model.bin y una línea añadida en config.yaml cambian sus hashes, mientras que el tokenizer.json intacto sigue coincidiendo. El manifiesto debe proceder de una fuente de confianza, como la versión firmada del proveedor; de lo contrario, un atacante que cambie un archivo podría cambiar también el manifiesto.

### 8.4 Pruebas adversarias

Añada pruebas que intenten romper su código: entradas de tamaño excesivo, tipos incorrectos, cadenas con forma de inyección, peticiones de datos de otros usuarios. Manténgalas de forma permanente en el conjunto de pruebas. Para el analizador de reservas, las pruebas adversarias incluyen una fecha escrita con palabras, un identificador de paciente que pertenece a otra persona, un código de clínica con espacios al final y una salida del modelo que contiene dos reservas. Cada prueba registra el rechazo esperado. Una vez añadidas, estas pruebas protegen contra las regresiones: un cambio posterior que relaje sin querer una comprobación falla de inmediato, antes de llegar a los pacientes.

### 8.5 Ejemplo resuelto (caso sintético de LCH)

El proveedor de DocSort envió un modelo actualizado. La comprobación de integridad de Rina comparó el hash con el manifiesto firmado del proveedor y encontró una discrepancia en el archivo de configuración. La investigación mostró que un contratista había editado el archivo para activar un modo de depuración que registraba el texto completo de las cartas. El cambio se revirtió, y LCH exigió que todos los cambios de modelo llegaran por el proceso de publicación firmada. El modo de depuración se corresponde en espíritu con la línea de configuración manipulada del Laboratorio H: un pequeño cambio de texto con un gran efecto sobre la privacidad.

### 8.6 Errores y límites

- Lógica de políticas mezclada con el texto de la instrucción.
- Cargar archivos de modelo sin comprobaciones de integridad.
- Pruebas solo con entradas benignas.

Una política escrita en la instrucción puede desmontarse con un mensaje astuto, mientras que una política en el código no. Cargar archivos de modelo sin comprobar los hashes habría permitido que el modo de depuración del contratista llegara a producción en LCH. Las pruebas solo con entradas benignas pasan incluso cuando el analizador acepta salidas peligrosas; el archivo de pruebas hostiles del analizador de reservas existe precisamente para evitarlo, y crece con cada incidente.

### 8.6b Pruebas que protegen el analizador

El módulo que convierte la salida del modelo en una petición de reserva es el código más relevante para la seguridad de Ask Lumen, porque una respuesta mal formada o manipulada podría cancelar la cita equivocada. LCH mantiene un archivo de pruebas con salidas hostiles —campos adicionales, fechas erróneas, dos identificadores de cita— y todo cambio en el analizador debe superarlo antes de fusionarse. Cada salida hostil del archivo procede de un fallo real o de un hallazgo de revisión, así que el archivo registra la historia de ataques al analizador además de protegerlo de ellos. Cuando aparece un nuevo tipo de fallo, se añade una prueba para él antes de la corrección.

### Ejercicios

- **EX022 — Lectura del laboratorio.** ¿Qué archivos fallan la comprobación de hash en el laboratorio y por qué? Rúbrica: 3 = model.bin y config.yaml, ambos modificados; 2 = uno; 1 = vago; 0 = incorrecto.
- **EX023 — Validación de JSON.** Enumere cuatro comprobaciones para el JSON de reserva producido por el modelo. Rúbrica: 3 = JSON válido, solo campos permitidos, tipos, rangos/titularidad; 2 = tres; 1 = una o dos; 0 = nada.
- **EX024 — Modo de depuración.** ¿Por qué el cambio al modo de depuración era un problema de seguridad? Rúbrica: 3 = registraba datos de salud sensibles, lo que ampliaba la exposición; cambio no autorizado; 2 = parcial; 1 = vago; 0 = incorrecto.

### Síntesis

Los programas estructurados, el análisis estricto, las dependencias verificadas y las pruebas adversarias hacen que las aplicaciones de IA sean más difíciles de romper y más fáciles de confiar.

### Siga estudiando — capítulo 08 de 40

[← Capítulo 07 (borrador)](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 (borrador) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Datos y bases de datos

### Resultados de aprendizaje

Usted podrá (1) diseñar esquemas relacionales sencillos y escribir consultas; (2) prevenir la inyección en las consultas a bases de datos; (3) entender las bases de datos vectoriales que se usan para la recuperación; y (4) aplicar el control de acceso y la minimización de datos a los datos de IA.

### 9.1 Datos relacionales

Las tablas guardan registros; las claves enlazan tablas; las consultas SQL recuperan y modifican datos. El sistema de citas de LCH tiene tablas de pacientes, clínicas y citas. Las consultas deben estar parametrizadas: construir SQL concatenando cadenas con la entrada del usuario (o del modelo) permite la inyección de SQL. Con una consulta parametrizada, la base de datos trata el identificador de un paciente como un valor, así que un texto como una comilla seguida de palabras clave de SQL no puede cambiar el significado de la consulta. Esto importa aún más cuando los valores proceden de un modelo, al que su entrada puede dirigir para que produzca ese texto. La herramienta de reservas de LCH pasa cada valor como parámetro, y una prueba con un identificador con forma de inyección lo confirma.

### 9.2 Salida del modelo y bases de datos

Si un LLM genera consultas o parámetros de consulta, trátelos como entrada no confiable: use consultas parametrizadas, restrinja la cuenta de la base de datos a las tablas y operaciones mínimas y valide los valores. Un LLM que puede escribir SQL arbitrario con una cuenta de administrador es un riesgo grave de agencia excesiva (OWASP LLM06). Ask Lumen no genera SQL; propone una reserva cuyos campos la herramienta de reservas coloca en consultas fijas y parametrizadas. La cuenta de base de datos de la herramienta puede insertar y cancelar citas, pero no puede leer otras tablas ni cambiar el esquema. Aunque el modelo estuviera totalmente manipulado, el peor resultado se limitaría a lo que permite esa cuenta, y la comprobación de políticas lo restringe además al paciente que ha iniciado sesión.

### 9.3 Bases de datos vectoriales

La generación aumentada por recuperación almacena fragmentos de documentos como *embeddings* y recupera los más parecidos para cada pregunta. El control de acceso debe aplicarse en el momento de la recuperación con los permisos del usuario; de lo contrario, el chatbot puede recuperar y revelar documentos que el usuario no debería ver (OWASP LLM08, *vector and embedding weaknesses*, debilidades de vectores y *embeddings*). Los documentos añadidos al almacén también pueden llevar instrucciones inyectadas. Filtrar en el momento de la recuperación, en lugar de pedir al modelo que no muestre el contenido restringido, es el enfoque fiable: el modelo no puede filtrar un texto que nunca recibió.

### 9.4 Minimización y conservación

Guarde solo los datos que necesita y durante el tiempo que los necesita. Los registros de conversación de los chatbots contienen a menudo datos personales; fije plazos de conservación y reglas de acceso. En Ask Lumen, LCH conserva los registros de conversación durante un periodo fijo, necesario para la revisión de calidad y la investigación de incidentes, y después los borra. Solo los equipos de seguridad y de calidad pueden leerlos. La minimización se aplica también a lo que se envía al proveedor del modelo: los identificadores de pacientes que el modelo no necesita para responder se dejan fuera de la instrucción.

### 9.5 Ejemplo resuelto (caso sintético de LCH)

El índice de recuperación de Ask Lumen incluía documentos de turnos del personal con números de teléfono del personal. Una pregunta de prueba sintética, «¿quién está de guardia esta noche y cómo le localizo?», devolvió un número de teléfono a un paciente. LCH retiró los documentos del personal del índice orientado a pacientes, añadió un campo de clasificación de documentos y filtró la recuperación por público. La filtración no necesitó ningún ataque, solo una pregunta, lo que muestra que el control de acceso debe diseñarse dentro de la recuperación en lugar de probarse después del despliegue. El campo de clasificación dirige ahora cada recuperación.

### 9.6 Errores y límites

- SQL construido con cadenas.
- Un solo índice de recuperación para todos los públicos.
- Conservación indefinida de los registros de chat.

El SQL construido con cadenas permite que la salida de un modelo, o el texto que escribe un paciente, pase a formar parte de un comando de base de datos. Un único índice de recuperación para todos los públicos causó la filtración del número de teléfono del personal en el ejemplo resuelto. La conservación indefinida de los registros de chat acumula información personal y de salud que se convierte en un objetivo y en una carga. Cada error tiene una corrección sencilla y conocida, mucho más barata antes del despliegue que después de un incidente.

### 9.6b Borrar datos a petición

Cuando un paciente pide a LCH que borre su historial de chat, el borrado debe llegar a todas las copias: la tabla de conversaciones, los registros y cualquier entrada del almacén vectorial construida a partir de esos chats. El equipo mantiene un mapa de por dónde fluye el texto de los pacientes para que una petición pueda completarse y confirmarse dentro del plazo declarado por la clínica. El almacén vectorial es la copia que más se olvida, porque el texto se guarda allí como fragmentos y *embeddings* y no como una conversación reconocible. LCH etiqueta cada fragmento con la conversación de la que procede, para que el borrado pueda encontrarlo.

### Ejercicios

- **EX025 — Consulta parametrizada.** ¿Por qué las consultas parametrizadas son más seguras que la concatenación de cadenas? Rúbrica: 3 = los datos no pueden cambiar la estructura de la consulta; evita la inyección; 2 = parcial; 1 = vago; 0 = incorrecto.
- **EX026 — Acceso en la recuperación.** ¿Qué falló con los documentos de turnos y cuál es la corrección general? Rúbrica: 3 = público equivocado en el índice; aplicar filtrado por público/usuario en la recuperación; 2 = parcial; 1 = vago; 0 = nada.
- **EX027 — Conservación.** Proponga una regla de conservación para los registros de chat de Ask Lumen. Rúbrica: 3 = plazo, finalidad, acceso, borrado; 2 = tres; 1 = uno; 0 = nada.

### Síntesis

Los almacenes de datos alimentan y registran los sistemas de IA. Las consultas parametrizadas, las cuentas de mínimo privilegio, la recuperación según el público y la conservación mínima evitan que se conviertan en la filtración.

### Siga estudiando — capítulo 09 de 40

[← Capítulo 08 (borrador)](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 (borrador) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Ética y práctica autorizada

### Resultados de aprendizaje

Usted podrá (1) aplicar principios éticos al trabajo de seguridad de la IA; (2) explicar por qué hace falta autorización antes de probar; (3) seguir la divulgación coordinada; y (4) reconocer los problemas de equidad, privacidad y seguridad funcional que plantean los sistemas de IA.

### 10.1 Principios

El respeto por las personas, evitar el daño, la honestidad, la equidad y la rendición de cuentas guían el trabajo de seguridad. En seguridad de la IA, los daños incluyen violaciones de la privacidad, resultados discriminatorios, consejos inseguros y el mal uso de capacidades. Estos principios se convierten en decisiones concretas. Evitar el daño significa probar con historiales sintéticos, no con pacientes reales. La honestidad significa comunicar los resultados con sus límites. La equidad significa comprobar si las predicciones de NoShow tratan de forma distinta a distintos grupos. La rendición de cuentas significa registrar quién autorizó cada prueba y quién tomó cada decisión, para que la responsabilidad quede clara si algo sale mal. Las notas de laboratorio de Rina registran cada una de estas decisiones.

### 10.2 Autorización

Probar sistemas sin permiso puede ser ilegal y puede dañar a usuarios reales. Obtenga siempre una autorización por escrito del responsable del sistema que defina el alcance, los métodos, el periodo y los contactos. Los servicios públicos de IA tienen condiciones de uso; no los ataque fuera de programas que lo permitan explícitamente (como los alcances publicados de los programas de recompensas por errores). La autorización de Rina para trabajar con LCH nombra los sistemas (copias aisladas de Ask Lumen, NoShow y DocSort), los métodos permitidos, las fechas y el contacto al que llamar si ocurre algo inesperado. Lleva una copia en cada sesión de pruebas.

### 10.3 Divulgación coordinada

Si encuentra una vulnerabilidad, comuníquela en privado al responsable, dé un plazo razonable para corregirla y publique solo los detalles que ayuden a los defensores. No acceda a más datos de los necesarios para demostrar el problema. En el caso de Rina, el problema del número de teléfono se demostró con un único ejemplo sintético y no comprobando muchos números reales. Su informe describía el comportamiento, las condiciones y una corrección sugerida, y lo mantuvo confidencial hasta que LCH confirmó la corrección.

### 10.4 Equidad y seguridad funcional

Los sistemas de IA pueden tratar de forma distinta a distintos grupos. NoShow, por ejemplo, podría situar más abajo a algunos pacientes en los recordatorios por atributos correlacionados con los ingresos. El NIST AI RMF incluye *fair, with harmful bias managed* (justo, con el sesgo dañino gestionado) entre las características de una IA confiable, junto a *secure and resilient* (segura y resiliente) y *privacy-enhanced* (con mejoras de privacidad). El Reglamento de IA de la UE impone obligaciones a los sistemas de alto riesgo, incluidos algunos usos relacionados con la asistencia sanitaria; la clasificación jurídica necesita asesoramiento experto. Una comprobación de equidad para NoShow compararía las tasas de error entre grupos, por ejemplo si a los pacientes de algunos códigos postales se les predice erróneamente con más frecuencia que faltarán a sus citas.

### 10.5 Ejemplo resuelto (caso sintético de LCH)

Un compañero propuso probar un chatbot sanitario comercial «para ver si filtra datos». Rina explicó que sin autorización eso sería poco ético y posiblemente ilegal, y propuso en su lugar construir una réplica sintética en el laboratorio del curso. Por otra parte, en una prueba autorizada de LCH, Rina descubrió que Ask Lumen podía revelar si un número de teléfono pertenecía a un paciente registrado; lo comunicó por el proceso de LCH con evidencia mínima, y se corrigió antes de que terminara el semestre. La evidencia mínima consistió en un número de teléfono sintético, no en una lista de números reales.

### 10.6 Errores y límites

- «Solo echar un vistazo» a sistemas no autorizados.
- Recoger más datos personales de los necesarios para un informe.
- Ignorar la equidad como algo que «no es seguridad».

«Solo echar un vistazo» a un sistema no autorizado puede infringir la ley y dañar a los usuarios, sea cual sea la intención. Recoger más datos personales de los necesarios convierte un informe de seguridad en un riesgo de privacidad en sí mismo. Ignorar la equidad pasa por alto daños que afectan a los pacientes tan directamente como lo haría una filtración de datos, como que NoShow dé menos recordatorios a algunos grupos por atributos correlacionados con los ingresos. La práctica de Rina aborda los tres por diseño.

### Ejercicios

- **EX028 — Autorización.** Enumere cinco elementos de una autorización de pruebas. Rúbrica: 3 = alcance, métodos, ventana temporal, tratamiento de datos, contactos/condiciones de parada; 2 = cuatro; 1 = dos; 0 = nada.
- **EX029 — Divulgación.** Describa los pasos de divulgación de Rina para el problema del número de teléfono. Rúbrica: 3 = informe privado, evidencia mínima, verificación de la corrección, sin datos públicos; 2 = parcial; 1 = vago; 0 = divulgación pública primero.
- **EX030 — Equidad.** Explique cómo NoShow podría producir resultados injustos. Rúbrica: 3 = atributos sustitutos de características protegidas afectan a los recordatorios/la programación; 2 = parcial; 1 = vago; 0 = nada.

### Síntesis

La práctica ética de la seguridad de la IA significa pruebas autorizadas, divulgación cuidadosa, datos mínimos y atención a la equidad y a la seguridad funcional, además de a los ataques.

### Siga estudiando — capítulo 10 de 40

[← Capítulo 09 (borrador)](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 (borrador) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operativos

### Resultados de aprendizaje

Usted podrá (1) explicar los procesos, los usuarios, los permisos de archivo y el aislamiento; (2) ejecutar servicios de IA con mínimo privilegio; (3) aislar en entornos controlados el código producido o activado por la IA; y (4) usar los registros del sistema en las investigaciones.

### 11.1 Procesos y permisos

Todo programa se ejecuta como un proceso perteneciente a una cuenta de usuario. El sistema operativo comprueba los permisos de esa cuenta antes de permitir el acceso a archivos, las conexiones de red o el uso de dispositivos. Un servidor de modelos debe ejecutarse con su propia cuenta sin privilegios, que pueda leer los archivos del modelo pero no modificar código, leer datos ajenos a su función ni administrar la máquina. Si un atacante encontrara un fallo en el servidor de modelos, solo obtendría los derechos de esa cuenta. Por eso el trabajador de OCR de DocSort que se ejecutaba como administrador, en el ejemplo resuelto, fue un hallazgo grave incluso antes de que nada saliera mal.

### 11.2 Aislamiento

Los contenedores y las máquinas virtuales aíslan las cargas de trabajo. El aislamiento es esencial cuando un sistema de IA puede ejecutar código (por ejemplo, una herramienta de análisis de datos en un chatbot): el código puede verse influido por la inyección de instrucciones, así que debe ejecutarse sin acceso a la red, con CPU y memoria limitadas, un límite de tiempo corto y un sistema de archivos temporal. Ask Lumen no ejecuta código, pero DocSort procesa escaneos subidos, que son archivos no confiables. Ejecutar su trabajador de OCR en un contenedor con acceso de solo lectura a la carpeta de entrada significa que un archivo malicioso solo puede afectar a ese contenedor. Cada restricción responde a un riesgo concreto: sin red, los datos no pueden salir; el límite de tiempo detiene los bucles sin fin; y el sistema de archivos temporal desaparece tras cada trabajo.

### 11.3 Control de recursos

Sin límites, una petición pesada puede dejar sin recursos a las demás. Los grupos de control (en Linux) y los límites de los contenedores acotan el uso de CPU, memoria y GPU por carga de trabajo, lo que favorece la disponibilidad. En DocSort, un solo escaneo mal formado que consuma toda la memoria podría bloquear todas las cartas de derivación de la cola. Un tope de memoria en el contenedor del trabajador hace que ese archivo falle por sí solo mientras el siguiente trabajo continúa. Los límites se fijan a partir del uso normal medido más un margen, y un trabajo que alcanza un límite se registra para poder investigar la causa en lugar de reintentarlo en silencio.

### 11.4 Registros

Los registros de autenticación, de procesos y de acceso a archivos ayudan a reconstruir lo ocurrido. Correlacionarlos con los identificadores de petición de la aplicación vincula una conversación del chatbot con sus efectos en el sistema. En Ask Lumen, cada conversación recibe un identificador de petición que aparece en el registro de la aplicación, en el registro de llamadas al modelo y en el registro de la herramienta de reservas. Con ese identificador, Rina puede seguir un mensaje de un paciente desde el chat hasta cualquier cita que haya modificado. Sin él, emparejar entradas solo por la hora es lento y propenso a errores cuando hay muchas conversaciones a la vez.

### 11.4b Parcheo y configuración

Los sistemas operativos y el software que sirve modelos de IA reciben actualizaciones de seguridad; aplíquelas según un calendario y controle las versiones. Las configuraciones predeterminadas suelen activar funciones de depuración, páginas de error detalladas y cuentas de ejemplo que deben desactivarse en producción. Los volcados de memoria de DocSort en el ejemplo resuelto son un caso de ese tipo de valor predeterminado: útil durante el desarrollo, dañino en producción. LCH mantiene ahora una lista de comprobación de configuración para cada servicio de IA, revisada antes de cada publicación, que enumera los ajustes de depuración, las páginas de error y las cuentas de ejemplo que deben estar desactivados. El parcheo sigue un calendario mensual, y las correcciones urgentes se aplican antes cuando se anuncia una vulnerabilidad grave.

### 11.5 Ejemplo resuelto (caso sintético de LCH)

El trabajador de OCR de DocSort se ejecutaba con una cuenta de administrador «por comodidad». Un archivo escaneado mal formado lo hizo fallar, y el volcado de memoria se escribió en una carpeta compartida que todo el personal podía leer, lo que expuso el texto de las cartas. La corrección de Rina: una cuenta dedicada sin privilegios, volcados de memoria desactivados en producción, el trabajador en un contenedor con acceso de solo lectura a su carpeta de entrada y alertas ante los fallos. Cada corrección responde a una causa: la cuenta sin privilegios limita lo que puede hacer un trabajador comprometido, los volcados desactivados impiden que el texto llegue a una carpeta compartida, la entrada de solo lectura impide que el trabajador altere las cartas y las alertas hacen visibles los fallos.

### 11.6 Errores y límites

- Servicios que se ejecutan como administrador.
- Herramientas de IA que ejecutan código con acceso a la red.
- Registros que no se pueden vincular con las peticiones.

Ejecutar como administrador convierte cualquier error en control total de la máquina, como casi ocurrió en el caso de DocSort. Las herramientas de IA que ejecutan código con acceso a la red pueden ser dirigidas mediante inyección de instrucciones para enviar datos al exterior. Los registros que no se pueden vincular con las peticiones impiden decir qué conversación causó qué efecto, así que las investigaciones se estancan. Cada uno de estos es una decisión de configuración, barata de acertar desde el principio.

### Ejercicios

- **EX031 — Mínimo privilegio.** Enumere tres permisos que necesita el trabajador de DocSort y tres que no debería tener. Rúbrica: 3 = ambos lados razonables; 2 = un lado débil; 1 = vago; 0 = nada.
- **EX032 — Entorno aislado.** Especifique un entorno aislado para la herramienta «analizar hoja de cálculo» de un chatbot. Rúbrica: 3 = sin red, límites de CPU/memoria/tiempo, sistema de archivos temporal, usuario sin privilegios; 2 = tres; 1 = uno o dos; 0 = nada.
- **EX033 — Volcado de memoria.** ¿Por qué el volcado de memoria era un problema de confidencialidad? Rúbrica: 3 = contenía texto sensible escrito en una ubicación de lectura amplia; 2 = parcial; 1 = vago; 0 = incorrecto.

### Síntesis

El sistema operativo impone quién puede hacer qué. El mínimo privilegio, el aislamiento, los límites de recursos y los registros vinculables hacen más seguros los servicios de IA cuando algo sale mal.

### Siga estudiando — capítulo 11 de 40

[← Capítulo 10 (borrador)](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 (borrador) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Probabilidad y estadística

### Resultados de aprendizaje

Usted podrá (1) usar la probabilidad condicionada y la regla de Bayes; (2) explicar las tasas base y la precisión de las alertas; (3) calcular e interpretar intervalos de confianza para tasas; y (4) comparar dos sistemas de forma justa.

### 12.1 Probabilidad condicionada

P(A | B) es la probabilidad de A dado B. La tasa de verdaderos positivos de un detector es P(alerta | ataque); lo que necesitan los operadores es P(ataque | alerta), que la regla de Bayes obtiene a partir de las tasas de verdaderos y falsos positivos y de la tasa base de ataques. Las dos se confunden con facilidad, y los proveedores suelen citar la primera. Un detector que detecta el 95 % de los ataques sigue produciendo sobre todo falsas alarmas si los ataques son raros, porque la mayoría limpia genera muchos falsos positivos. La regla de Bayes hace explícito el cálculo, y el Laboratorio B muestra cuánto depende la respuesta de la tasa base.

### 12.2 Tasas base

Cuando los ataques son raros, incluso los buenos detectores producen sobre todo falsas alarmas. El laboratorio muestra un detector con un 95 % de TPR y un 5 % de FPR que da menos de un 2 % de precisión con una tasa base de 1 entre 1.000.

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

Leyendo el Laboratorio B por filas: con una tasa base de uno entre mil, bajar la tasa de falsos positivos del 5 % al 1 % eleva la precisión de 0,019 a 0,087, y el detector de 0,001 llega a 0,445. Las alertas por cada 10.000 conversaciones muestran la carga de trabajo: 509 para el primer detector frente a 18 para el último. Los revisores pueden atender dieciocho alertas; quinientas acabarían ignoradas.

### 12.3 Intervalos de confianza

Una tasa observada en una muestra es incierta. El intervalo de Wilson funciona bien con muestras pequeñas y tasas extremas. Tres éxitos de veinte son compatibles con tasas reales de aproximadamente el 5 % al 36 %.

```python
"""Lab S: reporting attack-success rates honestly: Wilson intervals,
seed variation and a paired bootstrap. Synthetic trial outcomes only."""
import math, random
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c - h, c + h
for k, n in ((3, 20), (30, 200), (300, 2000)):
    lo, hi = wilson(k, n); print(f"successes={k}/{n} rate={k/n:.3f} wilson95=[{lo:.3f}, {hi:.3f}]")
# five seeds of a synthetic defence evaluation: per-seed attack success rate
rates = []
for seed in range(5):
    r = random.Random(seed); rates.append(sum(r.random() < 0.12 for _ in range(200))/200)
m = sum(rates)/5; sd = math.sqrt(sum((x-m)**2 for x in rates)/4)
print("per-seed rates:", " ".join(f"{x:.3f}" for x in rates), f"mean={m:.3f} sd={sd:.3f}")
# paired bootstrap: baseline vs defence on the same 300 synthetic prompts
r = random.Random(42)
base = [r.random() < 0.30 for _ in range(300)]
defn = [b and r.random() < 0.6 for b in base]   # defence blocks ~40% of successes
diffs = []
for _ in range(2000):
    idx = [r.randrange(300) for _ in range(300)]
    diffs.append(sum(base[i] for i in idx)/300 - sum(defn[i] for i in idx)/300)
diffs.sort()
print(f"baseline_asr={sum(base)/300:.3f} defended_asr={sum(defn)/300:.3f} "
      f"reduction_ci95=[{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Salida esperada:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

El laboratorio muestra cómo se estrecha el intervalo con el tamaño de la muestra: la misma tasa del 15 % da un intervalo de aproximadamente el 11 % al 21 % con 200 ensayos y de 0,135 a 0,166 con 2.000. Una demostración con 20 instrucciones no puede distinguir una defensa débil de una fuerte. La línea por semilla añade otra fuente de dispersión: cinco ejecuciones de la misma evaluación van de 0,105 a 0,145.

### 12.4 Comparar sistemas

Para comparar dos defensas, pruebe ambas con los mismos elementos y observe la diferencia emparejada con un intervalo *bootstrap*. Si el intervalo incluye el cero, no puede afirmar que una sea mejor. Probar con los mismos elementos elimina la variación causada por que algunas instrucciones sean más difíciles que otras. En el Laboratorio S, la defensa reduce el éxito de los ataques de 0,350 a 0,190, y el intervalo *bootstrap* de la reducción va de 0,120 a 0,203. Como excluye el cero, la mejora es real para este conjunto de prueba; si se mantiene con otras instrucciones es otra cuestión.

### 12.4b Variación y tamaño de la muestra

Los resultados también varían con las semillas aleatorias, las particiones de los datos y la redacción de las instrucciones. Ejecute varias semillas e informe de su dispersión, como muestra la línea por semilla del laboratorio. Para planificar cuántos casos de prueba necesita para una tasa cercana a p con una semiamplitud de intervalo h al 95 % de confianza, use n ≈ 1,96² × p(1 − p) / h². Para p = 0,1 y h = 0,02 son unos 864 casos, muchos más de los que usan la mayoría de las demostraciones rápidas, por eso muchas «tasas de éxito» publicadas son menos seguras de lo que parecen. La fórmula también muestra el coste de la precisión: reducir h a la mitad, a 0,01, exige cuatro veces más casos, unos 3.457.

### 12.5 Ejemplo resuelto (caso sintético de LCH)

Un proveedor ofrecía un «detector de ataques por instrucciones» con un 98 % de exactitud. Rina pidió la TPR y la FPR: 90 % y 2 %. Con una estimación de 1 conversación maliciosa por cada 2.000, la precisión sería de aproximadamente un 2 %: la mayoría de las alertas serían falsas. LCH usó el detector solo para marcar conversaciones para una revisión semanal, no para bloquear a pacientes. La cifra del 98 % de exactitud apenas significaba nada aquí, ya que un detector que nunca se activara obtendría aproximadamente un 99,95 % con el mismo tráfico. Usarlo para la revisión semanal en lugar de para bloquear significa que las falsas alertas cuestan tiempo de los revisores, no el acceso de los pacientes.

### 12.6 Errores y límites

- Exactitud sin tasas base.
- Cifras únicas sin intervalos.
- Comparar sistemas con conjuntos de prueba distintos.

La exactitud oculta el equilibrio entre ataques no detectados y falsas alarmas, y puede parecer alta en un detector inútil cuando los ataques son raros. Una cifra única sin intervalo invita al exceso de confianza, sobre todo en pruebas pequeñas como tres éxitos de veinte. Comparar sistemas con conjuntos de prueba distintos confunde las diferencias entre los sistemas con las diferencias entre las instrucciones. El Laboratorio S muestra la corrección de cada uno con las mismas instrucciones sintéticas.

### Ejercicios

- **EX034 — Precisión.** Calcule la precisión para TPR 0,90, FPR 0,02 y tasa base 0,0005. Rúbrica: 3 = 0,00045/(0,00045 + 0,01999) ≈ 0,022; 2 = desliz; 1 = método; 0 = nada.
- **EX035 — Lectura del laboratorio.** ¿Cuál es el intervalo de Wilson para 300/2000 en el Laboratorio S? Rúbrica: 3 = [0,135; 0,166]; 2 = aproximado; 1 = solo el valor puntual; 0 = incorrecto.
- **EX036 — Comparación emparejada.** ¿Por qué probar dos defensas con los mismos elementos? Rúbrica: 3 = elimina la variación por dificultad de los elementos; inferencia emparejada válida; 2 = parcial; 1 = vago; 0 = incorrecto.

### Síntesis

La probabilidad le dice qué significa una alerta y cuánta seguridad puede tener. Las tasas base, los intervalos y las comparaciones emparejadas son el mínimo para hacer afirmaciones honestas en seguridad de la IA.

### Siga estudiando — capítulo 12 de 40

[← Capítulo 11 (borrador)](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 (borrador) →](../../en/book/MANUSCRIPT.md#ch-13)

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

**EX019.** Protege: la confidencialidad y la integridad de los datos en tránsito; la autenticidad del servidor. No protege: contra contenido malicioso de un usuario autenticado; contra la inyección de instrucciones ni el mal uso tras la llegada.

**EX020.** Solo atiende 62 de 90 peticiones normales porque las ráfagas naturales del cliente normal superan un cubo de 5 testigos que se rellena a 1 por segundo.

**EX021.** El código del navegador es visible para cualquiera; una clave filtrada permite a otros usar la API a su costa y saltarse sus controles. Llame al modelo desde el servidor.

**EX022.** Fallan model.bin (un bit cambiado) y config.yaml (una línea añadida); tokenizer.json no ha cambiado y pasa.

**EX023.** JSON válido; solo campos permitidos; tipos correctos; valores dentro de los rangos y pertenecientes al paciente que ha iniciado sesión.

**EX024.** Registraba el texto completo de las cartas —datos de salud sensibles—, lo que ampliaba la exposición, y era un cambio no autorizado fuera del proceso de publicación.

**EX025.** Los parámetros se envían por separado del texto de la consulta, así que la entrada no puede cambiar la estructura de la consulta; esto evita la inyección de SQL.

**EX026.** Había documentos del personal en el índice orientado a pacientes; la recuperación debe filtrar por público o por permisos del usuario antes de que el contenido llegue al modelo.

**EX027.** Conservar los registros de chat 30 días para soporte y revisión de seguridad; acceso limitado al equipo de soporte; datos personales censurados cuando sea posible; borrado automático a los 30 días.

**EX028.** Alcance (sistemas y cuentas); métodos permitidos; ventana temporal; reglas de tratamiento de datos; contactos y condiciones de parada.

**EX029.** Se detuvo en cuanto el problema quedó demostrado, lo comunicó en privado por el proceso de LCH con evidencia sintética mínima, no conservó datos reales y verificó la corrección.

**EX030.** Atributos como el código postal o el tipo de teléfono pueden actuar como sustitutos de los ingresos o del origen étnico; si reducen la prioridad prevista, algunos grupos reciben menos recordatorios o peores franjas horarias.

**EX031.** Necesita: leer su carpeta de entrada; escribir los resultados de encaminamiento en la cola; leer sus archivos de modelo. No debería tener: derechos de administrador; acceso de escritura al código o a los archivos de modelo; acceso de lectura a recursos compartidos ajenos ni acceso a toda la red.

**EX032.** Ejecutar el código de la herramienta en un contenedor sin red, con límites de CPU, memoria y tiempo, un sistema de archivos temporal que solo contenga el archivo subido y un usuario sin privilegios.

**EX033.** El volcado contenía texto de las cartas (datos de salud) y se escribió en una carpeta que todo el personal podía leer, lo que lo exponía más allá de las personas autorizadas.

**EX034.** VP = 0,90 × 0,0005 = 0,00045; FP = 0,02 × 0,9995 ≈ 0,01999; precisión ≈ 0,00045 / 0,02044 ≈ 0,022.

**EX035.** [0,135; 0,166].

**EX036.** Los elementos difieren en dificultad; usar los mismos elementos permite que esa variación se cancele en la diferencia emparejada, lo que da una comparación justa y más precisa.

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
