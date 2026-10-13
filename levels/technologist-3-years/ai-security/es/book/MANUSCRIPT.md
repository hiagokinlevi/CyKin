# Seguridad de la IA y del aprendizaje automático: libro del tecnólogo

- Idioma: español neutro (`es`); programa de tecnólogo, tres años; aproximadamente 2400 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–30 de 30 tienen texto didáctico de autor; los ejercicios EX001–EX090 (tres por capítulo) tienen sus resultados resueltos correspondientes con rúbricas de 0 a 3; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas impresas proceden de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no equivale a un libro terminado.
- Público: futuros tecnólogos de seguridad que construyen, configuran, supervisan y diagnostican los sistemas que rodean a los modelos de IA.
- Relación con los libros vecinos: el [libro de grado](../../../../bachelors-4-years/ai-security/es/book/MANUSCRIPT.md) es más amplio y más teórico; el [libro técnico](../../../../technical-18-months/ai-security/en/book/MANUSCRIPT.md) (en inglés) es más breve y más procedimental. **Este libro está centrado en la implementación**: herramientas, controles, supervisión, automatización y traspaso.
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado y no concede autorización para probar sistemas reales. Todas las organizaciones, personas, conjuntos de datos y cifras de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Treinta capítulos siguen el programa: fundamentos de computación y de seguridad (1–9); métodos, herramientas y operaciones de seguridad de la IA y del aprendizaje automático (10–23 y 26); e investigación, proyecto, despliegue y proyecto final (24–30). Cada capítulo tiene resultados de aprendizaje, texto didáctico, un ejemplo resuelto, errores y límites, tres ejercicios puntuados de 0 a 3 (0 ausente o inseguro; 1 laguna importante; 2 lagunas menores; 3 completo y justificado), una síntesis y un bloque **Siga estudiando**. Los laboratorios son deterministas, se ejecutan sin conexión con `python3 file.py` e imprimen los resultados que se muestran bajo *Salida esperada*. Son modelos de juguete, no defensas de producción.

### El ejemplo conductor (sintético): Brightwell Home

> **Caso sintético — ficción.** **Brightwell Home** es un minorista en línea de muebles inventado. Opera **Ask Brightwell**, un asistente de tienda basado en un modelo de lenguaje que responde preguntas a partir de documentos de productos y de políticas mediante recuperación y que, mediante herramientas, puede consultar pedidos e iniciar devoluciones; **ReturnGuard**, un modelo que puntúa las solicitudes de devolución según el riesgo de fraude; y **CodePilot**, un asistente interno de programación que usan sus desarrolladores. El tecnólogo en formación *Jonas Weber* se incorpora al equipo de plataforma y sigue estos sistemas a lo largo del programa. Todas las cifras sobre Brightwell son inventadas; todas las pruebas se realizan sobre copias aisladas con datos sintéticos y autorización por escrito.

### Política de fuentes

Las fuentes se comprobaron el 12 de octubre de 2026: NIST [AI 100-1](https://doi.org/10.6028/NIST.AI.100-1) (AI RMF 1.0), [AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) (perfil de IA generativa) y [AI 100-2 E2025](https://doi.org/10.6028/NIST.AI.100-2e2025) (taxonomía de aprendizaje automático adversario); el [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [MITRE ATLAS](https://atlas.mitre.org/); el [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) (Reglamento de IA); y la norma [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html). Los artículos se citan por su identificador de arXiv; cada uno se abrió y se comprobó su título.

## Contenido

| Parte | Capítulos |
|---|---|
| Fundamentos | [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](../../en/book/MANUSCRIPT.md#ch-07) · [8](../../en/book/MANUSCRIPT.md#ch-08) · [9](../../en/book/MANUSCRIPT.md#ch-09) |
| Seguridad de la IA y del aprendizaje automático | [10](../../en/book/MANUSCRIPT.md#ch-10) · [11](../../en/book/MANUSCRIPT.md#ch-11) · [12](../../en/book/MANUSCRIPT.md#ch-12) · [13](../../en/book/MANUSCRIPT.md#ch-13) · [14](../../en/book/MANUSCRIPT.md#ch-14) · [15](../../en/book/MANUSCRIPT.md#ch-15) · [16](../../en/book/MANUSCRIPT.md#ch-16) · [17](../../en/book/MANUSCRIPT.md#ch-17) · [18](../../en/book/MANUSCRIPT.md#ch-18) · [19](../../en/book/MANUSCRIPT.md#ch-19) · [20](../../en/book/MANUSCRIPT.md#ch-20) · [21](../../en/book/MANUSCRIPT.md#ch-21) · [22](../../en/book/MANUSCRIPT.md#ch-22) · [23](../../en/book/MANUSCRIPT.md#ch-23) |
| Proyecto, despliegue y proyecto final | [24](../../en/book/MANUSCRIPT.md#ch-24) · [25](../../en/book/MANUSCRIPT.md#ch-25) · [26](../../en/book/MANUSCRIPT.md#ch-26) · [27](../../en/book/MANUSCRIPT.md#ch-27) · [28](../../en/book/MANUSCRIPT.md#ch-28) · [29](../../en/book/MANUSCRIPT.md#ch-29) · [30](../../en/book/MANUSCRIPT.md#ch-30) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Sistemas informáticos

### Resultados de aprendizaje

Usted podrá (1) describir las capas de hardware y software sobre las que funciona un servicio de IA; (2) explicar dónde residen los modelos, los pesos y los datos en tiempo de ejecución; (3) identificar los recursos informáticos que un atacante puede agotar; y (4) relacionar las capas del sistema con los controles de seguridad de la IA.

### 1.1 Capas

Un asistente de tienda como Ask Brightwell no es «solo un modelo». Una petición atraviesa un navegador, un balanceador de carga, una aplicación web, un servicio de orquestación que construye el *prompt*, un servicio de recuperación, un servidor de modelos (a menudo la API de un proveedor) y servicios de herramientas como la base de datos de pedidos. Cada capa funciona sobre un sistema operativo, en hardware físico o virtual, y cada una tiene sus propias cuentas, registros y modos de fallo. El trabajo de seguridad empieza por dibujar estas capas. El primer dibujo que Jonas hizo de Ask Brightwell encontró un problema en una capa que nadie consideraba de IA: los registros del orquestador.

### 1.2 Dónde residen los modelos

Un modelo es un archivo de números (pesos) más el código que lo ejecuta. Cuando está autoalojado, los pesos están en disco, se cargan en memoria y suelen ejecutarse en GPU. Cuando se accede a él mediante una API, el proveedor los guarda y usted envía texto. En ambos casos, el *prompt*, los documentos recuperados y las salidas pasan por la memoria y los registros de sistemas que usted opera, lugares por donde pueden filtrarse datos sensibles. En Ask Brightwell los pesos permanecen en el proveedor, pero los *prompts* que construía el orquestador, incluidas las direcciones de clientes obtenidas por la herramienta de pedidos, estaban en un contenedor de registros compartido. Los archivos del modelo autoalojado de CodePilot, en cambio, residen en los discos de la propia Brightwell, donde las comprobaciones de integridad son tarea de Brightwell.

### 1.3 Recursos

La inferencia de los modelos de lenguaje es cara: cada petición consume tiempo y memoria de GPU en proporción a la longitud de la entrada y de la salida. Los atacantes que envían peticiones muy largas o muy numerosas pueden elevar los costes o denegar el servicio; OWASP lo recoge como LLM10 Unbounded Consumption (consumo ilimitado). Saber qué recurso es escaso —GPU, *tokens*, dinero— indica qué hay que limitar. En Ask Brightwell, el recurso escaso es el dinero: cada *token* enviado a la API del proveedor se factura, de modo que un punto de acceso sin límites permite que cualquiera dispare la factura. Por eso la primera propuesta de Jonas combinaba un límite de tasa de peticiones con un presupuesto diario de *tokens* por cuenta.

### 1.4 Capas y controles

Asigne los controles a las capas: autenticación en el perímetro, límites de tasa en la pasarela, construcción del *prompt* y tratamiento de las salidas en el orquestador, control de acceso en la recuperación y en las herramientas, comprobaciones de integridad de los archivos del modelo en disco y registros en todas partes. Para Ask Brightwell, el diagrama de Jonas muestra dónde está hoy cada control y dónde falta alguno. No había límite de tasa en la pasarela y los registros de *prompts* del orquestador podían leerlos 40 ingenieros, así que a dos capas les faltaban controles que el mapa hace evidentes. El servicio de políticas añadido más tarde pertenece a esa misma capa del orquestador, entre el modelo y las herramientas.

### 1.5 Ejemplo resuelto (caso sintético de Brightwell)

Jonas dibuja Ask Brightwell: navegador → CDN → aplicación web → orquestador → (índice de recuperación de 3000 páginas de políticas y productos; API del modelo del proveedor; herramientas de consulta de pedidos y de devoluciones) → bases de datos. Anota que el orquestador registra los *prompts* completos, incluidas las direcciones de clientes obtenidas por la herramienta de pedidos, en un contenedor de registros compartido que pueden leer 40 ingenieros. Lo añade a la lista de incidencias del equipo. El hallazgo no tiene nada que ver con el modelo: es un problema corriente de control de acceso en la capa de registro. Como los registros contienen direcciones que obtuvo la herramienta de pedidos, el contenedor se convirtió en uno de los mayores almacenes de datos de clientes del sistema sin que nadie lo decidiera.

### 1.6 Errores y límites

- Tratar el modelo como si fuera todo el sistema.
- Olvidar que los registros y las cachés son almacenes de datos.
- Ignorar el coste como objetivo de ataque.

El dibujo de Jonas protege contra los tres. Muestra el modelo como una caja entre muchas, incluye el contenedor de registros compartido como almacén de datos con direcciones de clientes y marca la API del proveedor como un coste que hay que proteger. Cada error, si no se hubiera corregido, habría dejado fuera de la lista de incidencias una debilidad real de Ask Brightwell. Los capítulos posteriores vuelven a cada capa con pruebas y controles.

### Ejercicios

- **EX001 — Diagrama de capas.** Dibuje las capas de un *chatbot* de IA que use y etiquete un control por capa. Rúbrica: 3 = al menos seis capas con controles adecuados; 2 = cuatro o cinco; 1 = dos o tres; 0 = ninguna.
- **EX002 — Dónde residen los datos.** Enumere cuatro lugares donde podría almacenarse una dirección de cliente durante una petición a Ask Brightwell. Rúbrica: 3 = cuatro lugares plausibles; 2 = tres; 1 = uno o dos; 0 = ninguno.
- **EX003 — Recurso escaso.** En un modelo autoalojado, ¿qué recurso limitaría primero y cómo? Rúbrica: 3 = tiempo de GPU o *tokens*, límites por usuario y longitudes máximas; 2 = parcial; 1 = vago; 0 = ninguno.

### Síntesis

Los servicios de IA son sistemas por capas. La seguridad empieza por cartografiar por dónde viajan las peticiones, los modelos y los datos, y qué recursos pueden agotar los atacantes.

### Siga estudiando — capítulo 01 de 30

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Redes y servicios de internet

### Resultados de aprendizaje

Usted podrá (1) seguir una petición de IA a través de redes y protocolos; (2) explicar el papel de TLS, DNS y HTTP en los servicios de IA; (3) configurar controles de pasarela como la limitación de tasa; y (4) reconocer el abuso de los puntos de acceso de IA a nivel de red.

### 2.1 El recorrido de la petición

El navegador de un cliente resuelve el dominio de la tienda mediante DNS, abre una conexión TLS y envía una petición HTTP. La aplicación web llama a servicios internos por la red privada y llama a la API del proveedor del modelo por internet, de nuevo con TLS y una clave de API. Cada salto es un lugar donde autenticar, cifrar y registrar. En Ask Brightwell, el salto interno del orquestador a la herramienta de pedidos y el salto externo a la API del proveedor transportan datos de clientes, así que ambos necesitan TLS y registro. La clave del proveedor en esa llamada externa es una credencial como cualquier otra y debe permanecer en el servidor.

### 2.2 El papel de los protocolos

DNS asigna nombres a direcciones; si se secuestra, los usuarios pueden acabar en un asistente falso. TLS protege la confidencialidad y la integridad en tránsito y autentica a los servidores mediante certificados. HTTP transporta peticiones y respuestas; las respuestas en flujo continuo (*server-sent events* o WebSockets) son habituales en el chat y necesitan tiempos de espera para que las conexiones inactivas no se acumulen. Ask Brightwell transmite las respuestas al navegador en flujo continuo, de modo que un atacante que abre muchos flujos y nunca los lee puede acaparar las conexiones del servidor. Los tiempos de espera sobre los flujos inactivos los cierran, y la pasarela cuenta los flujos abiertos por sesión como uno de sus límites. Las comprobaciones de certificado en la llamada al proveedor también importan, porque la clave de API viaja en ella.

### 2.3 Controles de pasarela

Una pasarela de API o un *proxy* inverso se sitúa delante de los puntos de acceso de IA. Autentica a quienes llaman, impone un tamaño máximo de petición y aplica límites de tasa. Un cubo de *tokens* permite una tasa constante con ráfagas cortas: se atiende a los usuarios que se comportan bien mientras se recortan las avalanchas.

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

El laboratorio de Jonas prueba exactamente este diseño, con una tasa de 2 peticiones por segundo y una ráfaga de 10, frente a una avalancha y a un conjunto de usuarios normales. La pasarela también rechaza los mensajes que superan una longitud fijada antes de que lleguen al orquestador, de modo que una sola petición enorme no puede consumir todo el presupuesto de *tokens* de una sesión.

### 2.4 Abuso de red

Los patrones de abuso incluyen avalanchas para elevar el coste, la extracción masiva de respuestas para copiar el comportamiento de un modelo (extracción del modelo) y claves de API robadas usadas desde redes inesperadas. Señales: tasas de peticiones por clave, geografías inusuales, muchas consultas distintas desde un mismo cliente. En Ask Brightwell, las señales útiles son las tasas de peticiones por sesión, el uso de *tokens* por cuenta y cuántas preguntas distintas hace un mismo cliente. Una clave de socio que de repente envía miles de llamadas de puntuación variadas a ReturnGuard es el patrón que más tarde resultó ser una extracción.

### 2.5 Ejemplo resuelto (caso sintético de Brightwell)

El punto de acceso de Ask Brightwell no tenía límite de tasa. Jonas ejecuta el laboratorio sobre una copia: a 2 peticiones por segundo con ráfaga 10, se atienden las 90 peticiones normales mientras solo pasan 129 de las 3000 peticiones de la avalancha. A 1 por segundo, los usuarios normales empiezan a fallar (62/90). Propone 2/s con ráfaga 10 por sesión, más un presupuesto diario de *tokens* por cuenta. Las cifras del laboratorio hacen concreto el compromiso. Un límite lo bastante holgado para atender todas las peticiones normales sigue reduciendo la avalancha a una pequeña fracción, mientras que reducir la tasa a la mitad empieza a hacer fallar a usuarios reales. Limitar por sesión y no por dirección evita también bloquear a clientes que comparten una red.

### 2.6 Errores y límites

- Limitar la tasa solo por IP (redes compartidas, *botnets*).
- Límites tan estrictos que bloquean a usuarios reales.
- Claves de API del proveedor en el código del *front-end*.

La propuesta de Jonas responde a cada uno. Limita por sesión y por cuenta y no por dirección, se eligió a partir de las mediciones del laboratorio de modo que las 90 peticiones normales siguieran atendiéndose, y mantiene la clave del proveedor en el servidor. Un límite que bloquea a usuarios reales empujaría al negocio a eliminarlo, así que medir ambos lados importa más que elegir una cifra estricta.

### Ejercicios

- **EX004 — Recorrido.** Enumere cada salto de protocolo de una petición a Ask Brightwell y un control por salto. Rúbrica: 3 = DNS, TLS, HTTP, interno, API del proveedor, con controles; 2 = tres o cuatro; 1 = uno o dos; 0 = ninguno.
- **EX005 — Laboratorio.** Justifique con el laboratorio el límite elegido. Rúbrica: 3 = los normales se atienden por completo, la avalancha se reduce, un límite más estricto perjudica a los usuarios; 2 = dos; 1 = uno; 0 = erróneo.
- **EX006 — Fuga de la clave.** Una clave de API del proveedor aparece en el JavaScript del navegador. ¿Qué ocurre y cuál es la solución? Rúbrica: 3 = cualquiera puede usarla, coste y abuso; rotarla, llevarla al servidor, acotar su alcance; 2 = parcial; 1 = vago; 0 = ninguno.

### Síntesis

Los puntos de acceso de IA son servicios de internet: proteja DNS, TLS y HTTP, ponga una pasarela delante y ajuste los límites de tasa para atender a los usuarios mientras se frena el abuso.

### Siga estudiando — capítulo 02 de 30

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programación

### Resultados de aprendizaje

Usted podrá (1) escribir Python sencillo para llamar a servicios de IA y probarlos de forma segura; (2) validar la entrada no confiable y la salida del modelo; (3) tratar correctamente los errores y los secretos; y (4) explicar por qué la salida del modelo debe tratarse como datos no confiables.

### 3.1 Programas alrededor de los modelos

La mayor parte del trabajo de seguridad de la IA es programación corriente: construir *prompts*, analizar respuestas, llamar a herramientas, escribir pruebas. La biblioteca estándar de Python basta para muchas tareas: `json` para analizar salidas estructuradas, `re` para patrones, `hashlib` para comprobaciones de integridad, `unittest` para pruebas. El trabajo de Jonas en Ask Brightwell es sobre todo de este tipo: escapar la salida en la consola del personal, validar el JSON de la herramienta de devoluciones y escribir pruebas que fallan cuando una consulta entre usuarios distintos tiene éxito. Nada de ello exige cambiar el modelo. Cada cosa es Python sencillo que un revisor puede leer en minutos y contrastar con la amenaza que aborda.

### 3.2 La salida del modelo no es confiable

La respuesta de un modelo puede contener texto que un atacante plantó mediante un documento. Si el código inserta ese texto en HTML, SQL o un comando de *shell* sin escaparlo, el atacante obtiene una inyección en esos sistemas: OWASP LLM05 Improper Output Handling (tratamiento inadecuado de las salidas). Trate la salida exactamente como la entrada del usuario: escápela para HTML, use consultas parametrizadas y nunca la pase a un *shell*. La reseña plantada por Jonas en la consola del personal lo mostró directamente: el asistente citó una etiqueta de imagen de una reseña y la consola la representó, con lo que el *script* se ejecutó en el navegador de un empleado. La solución fue escapar, no un modelo mejor.

### 3.3 Validar la salida estructurada

Cuando un modelo debe devolver una acción, pida JSON y valídelo de forma estricta: analícelo, compruebe que solo existen las claves esperadas, compruebe los tipos, compruebe los valores permitidos (por ejemplo, `action` en {"lookup", "return"}) y rechace todo lo demás. Nunca «arregle» una salida no válida adivinando. En Ask Brightwell, el orquestador solo acepta `lookup` y `return` como acciones y comprueba que el número de pedido sea una cadena de dígitos. Cualquier otra cosa, incluidas las claves adicionales que invente el modelo, hace que la petición se rechace y se registre, de modo que una propuesta mal formada nunca llega a la herramienta de devoluciones. Después, el servicio de políticas hace su propia comprobación sobre la acción validada.

### 3.4 Errores y secretos

Falle de forma cerrada: si la validación falla o una herramienta da error, no ejecute la acción. Guarde las claves de API en variables de entorno o en un gestor de secretos, nunca en el código ni en los registros.

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

En Ask Brightwell, si la herramienta de pedidos agota el tiempo de espera, el asistente le dice al cliente que ahora no puede consultar el pedido, en lugar de adivinar. La clave de API del proveedor reside en el gestor de secretos, y el filtro de registros del orquestador la elimina de cualquier mensaje de error antes de escribirlo. Jonas añadió una prueba que falla si aparece en una línea de registro una cadena con forma de clave, de modo que la regla se comprueba en cada compilación.

### 3.5 Lectura del laboratorio

El laboratorio entrena un pequeño clasificador lineal y muestra cómo cae su exactitud a medida que las entradas se desplazan eps en la peor dirección: 0,985 sin perturbación y 0,505 con eps 1,0. Recuerda que la decisión de un modelo puede dirigirse con cambios pequeños y deliberados en la entrada; el código que rodea a los modelos no debe suponer que sus salidas son correctas. Para Brightwell, el laboratorio respalda una decisión de diseño, no un hecho sobre ReturnGuard: las decisiones que importan no deben descansar en una sola puntuación sin comprobaciones. En el laboratorio, las perturbaciones las elige el atacante; los atacantes reales tienen límites sobre lo que pueden cambiar, y por eso el laboratorio es un recordatorio, no una medición.

### 3.6 Ejemplo resuelto (caso sintético de Brightwell)

La consola del personal de Ask Brightwell mostraba las respuestas del modelo como HTML sin procesar. Jonas planta en una copia de prueba una reseña de producto que contiene `<img src=x onerror=...>`; el asistente la cita y el *script* se ejecuta en el navegador del personal. Cambia la consola para que escape la salida y añade una prueba unitaria. La corrección está donde los datos salen del sistema, en la consola, así que se mantiene diga lo que diga el modelo. La prueba unitaria planta la misma etiqueta de imagen y falla si la consola vuelve a representarla como HTML, lo que protege frente a un cambio posterior que reintroduzca el fallo.

### 3.7 Errores y límites

- Insertar texto del modelo en HTML, SQL o un *shell*.
- Reparar JSON no válido a base de conjeturas.
- Secretos en el código fuente.

Cada uno convierte el texto de un modelo en una acción en otro sistema. La consola de Ask Brightwell mostró el primero; la validación estricta del JSON de la herramienta de devoluciones evita el segundo; y guardar la clave del proveedor en el gestor de secretos evita el tercero. Tener pruebas para cada uno significa que un cambio posterior no puede reintroducir sin ruido la debilidad, que es precisamente la razón de escribirlas como código.

### Ejercicios

- **EX007 — Validador.** Escriba pseudocódigo para validar `{"action":..., "order_id":...}`. Rúbrica: 3 = análisis, claves exactas, tipos, valores permitidos, fallo cerrado; 2 = cuatro; 1 = dos; 0 = ninguno.
- **EX008 — Tratamiento de las salidas.** Nombre tres destinos donde la salida del modelo necesita codificación y la técnica adecuada para cada uno. Rúbrica: 3 = escape de HTML, SQL parametrizado, sin *shell*/lista de argumentos; 2 = dos; 1 = uno; 0 = ninguno.
- **EX009 — Laboratorio.** ¿Qué significa la caída a 0,505 con eps 1,0? Rúbrica: 3 = cerca del azar, pequeños cambios elaborados invierten decisiones, advertencia de modelo de juguete; 2 = parcial; 1 = vago; 0 = erróneo.

### Síntesis

Programar alrededor de los modelos significa validar y codificar todo lo que pasa a otros sistemas —en especial la salida del modelo— y fallar de forma cerrada.

### Siga estudiando — capítulo 03 de 30

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Modelos de datos

### Resultados de aprendizaje

Usted podrá (1) describir las estructuras de datos que usan los sistemas de IA: tablas, documentos, *embeddings*; (2) explicar los índices vectoriales y sus propiedades de seguridad; (3) aplicar control de acceso a los datos usados para la recuperación; y (4) clasificar la sensibilidad de los datos.

### 4.1 Tipos de datos

Los sistemas de IA usan tablas relacionales (pedidos, clientes), documentos (políticas, páginas de productos, correos electrónicos), conjuntos de entrenamiento (ejemplos etiquetados) y *embeddings*: listas de números que representan el significado y que se almacenan en índices vectoriales para la recuperación. Ask Brightwell usa tres de ellos: las tablas de pedidos y de clientes mediante la herramienta de pedidos, las páginas de políticas y de productos mediante la recuperación, y sus *embeddings* en el índice vectorial. ReturnGuard añade un conjunto de entrenamiento de devoluciones pasadas, etiquetado por el personal. Cada uno tiene responsables y una sensibilidad distintos, que el inventario registra más adelante.

### 4.2 Índices vectoriales

La generación aumentada por recuperación (RAG) convierte los documentos en *embeddings*, almacena los vectores y, en el momento de la consulta, encuentra los más cercanos para incluirlos en el *prompt*. Problemas de seguridad: el índice puede mezclar documentos con permisos distintos; los *embeddings* pueden filtrar información sobre el texto que codifican; y cualquiera que pueda añadir documentos puede influir en las respuestas. OWASP los recoge como LLM08 Vector and Embedding Weaknesses (debilidades de vectores y *embeddings*). El índice de Ask Brightwell mostró el primer problema: una hoja de cálculo de márgenes de proveedores, subida por alguien, estaba en el mismo índice que las páginas públicas de productos, de modo que una pregunta de un cliente sobre descuentos la recuperó.

### 4.3 Control de acceso en la recuperación

Almacene cada fragmento con metadatos: responsable, público destinatario, sensibilidad. En el momento de la consulta, filtre según los permisos de quien llama antes de pasar los fragmentos al modelo; mejor aún, mantenga índices separados para públicos distintos. Nunca confíe en decirle al modelo «no reveles documentos internos». Tras la filtración de márgenes, Brightwell eligió la opción más sólida: un índice de clientes que solo contiene documentos públicos y un índice separado solo para el personal. Los metadatos de público destinatario siguen registrándose en cada fragmento, de modo que puede encontrarse un documento mal archivado y el filtro actúa como segunda capa si alguna vez se indexa un documento del personal en el lugar equivocado.

### 4.4 Clases de sensibilidad

Clasifique: público, interno, confidencial, personal. Los datos personales necesitan una base jurídica y minimización. Los conjuntos de entrenamiento necesitan la misma clasificación que sus fuentes. En Ask Brightwell, las páginas de productos y la política de devoluciones publicada son públicas, la hoja de cálculo de márgenes de proveedores es confidencial y los detalles de los pedidos son personales. El conjunto de entrenamiento de ReturnGuard hereda la clase personal porque se construye a partir de devoluciones de clientes, así que su almacenamiento y su acceso siguen las mismas reglas que la tabla de pedidos. Clasificar las fuentes antes de indexarlas habría dejado la hoja de márgenes fuera del índice de clientes.

### 4.4b Envenenamiento de datos mediante documentos

Cualquiera que pueda añadir o editar documentos indexados puede plantar texto que el modelo leerá: precios falsos, políticas inventadas o instrucciones ocultas. Restrinja quién puede publicar en el índice, registre la fuente y el historial de cambios de cada documento y revise las fuentes nuevas antes de indexarlas. Las reseñas de productos escritas por clientes no son confiables y deben indexarse por separado o no indexarse. La página de vacaciones de 60 días que más tarde confundió a Ask Brightwell fue un ejemplo involuntario de la misma debilidad. Esa página no era maliciosa, pero llegó a los clientes por el mismo camino.

### 4.5 Ejemplo resuelto (caso sintético de Brightwell)

El índice de Brightwell contenía páginas públicas de productos y una hoja de cálculo interna de «márgenes de proveedores» que alguien había subido. Jonas pregunta a Ask Brightwell «¿qué descuento puedes hacerme en el sofá Oslo?» y obtiene el margen. Añade metadatos de público destinatario, reconstruye el índice de clientes solo con documentos públicos y traslada los documentos internos a un índice solo para el personal. La corrección cambió dónde residen los documentos, no cómo se comporta el modelo. Una pregunta sobre descuentos ahora solo llega a páginas públicas, la formule como la formule el cliente, porque la hoja de márgenes ni siquiera está en el índice de clientes. Decirle al modelo que no la revelara habría dejado los datos a una pregunta ingeniosa de distancia.

### 4.6 Errores y límites

- Un solo índice para todos los públicos.
- Permisos impuestos mediante instrucciones en el *prompt*.
- Conjuntos de entrenamiento sin clasificar.

La filtración de márgenes de Brightwell vino del primer error y no se habría corregido con el segundo: una instrucción en el *prompt* no puede impedir que el modelo repita un texto que se le ha dado. El conjunto de entrenamiento de ReturnGuard, construido a partir de devoluciones de clientes, debe clasificarse como datos personales igual que su fuente, de modo que su almacenamiento y su acceso sigan las reglas de la tabla de pedidos. Cada error convierte una equivocación en el tratamiento de datos en una divulgación a través del asistente.

### Ejercicios

- **EX010 — Metadatos.** Proponga campos de metadatos para los fragmentos de recuperación y cómo se usa cada uno. Rúbrica: 3 = responsable, público destinatario, sensibilidad, fuente, fecha, con sus usos; 2 = tres; 1 = uno o dos; 0 = ninguno.
- **EX011 — Filtración.** Explique la filtración de márgenes y dos correcciones. Rúbrica: 3 = índice mixto; índice separado, filtrado antes del *prompt*; 2 = una corrección; 1 = vago; 0 = ninguna.
- **EX012 — Clasificación.** Clasifique cinco conjuntos de datos de Brightwell por sensibilidad. Rúbrica: 3 = cinco correctos; 2 = cuatro; 1 = dos o tres; 0 = menos.

### Síntesis

Los modelos de datos de la IA incluyen documentos y *embeddings*; la seguridad depende de etiquetar los datos, filtrar por permisos antes de la recuperación y no dejar nunca que los *prompts* sustituyan al control de acceso.

### Siga estudiando — capítulo 04 de 30

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Alfabetización en seguridad

### Resultados de aprendizaje

Usted podrá (1) usar la confidencialidad, la integridad y la disponibilidad para describir los riesgos de la IA; (2) interpretar correctamente amenaza, vulnerabilidad y riesgo; (3) conocer los principales marcos de seguridad de la IA; y (4) explicar la práctica autorizada.

### 5.1 La tríada CIA aplicada a la IA

Confidencialidad: los datos de entrenamiento, los *prompts*, los *prompts* de sistema y los registros de clientes no deben filtrarse. Integridad: las salidas y las acciones del modelo no deben poder manipularse, ya sea mediante inyección, envenenamiento o entradas adversarias. Disponibilidad: los servicios no deben poder agotarse ni inutilizarse. NIST AI 100-2 E2025 usa objetivos similares (disponibilidad, integridad, privacidad) para clasificar los ataques. En Ask Brightwell, los tres objetivos se corresponden con tres pruebas: si un cliente puede ver el pedido de otro, si un texto plantado puede hacer que el asistente inicie una devolución y si una avalancha de peticiones puede agotar el presupuesto de *tokens*. Cada capítulo posterior añade un control para uno de ellos.

### 5.2 Vocabulario

Una amenaza es una causa posible de daño (un estafador). Una vulnerabilidad es una debilidad (se le puede ordenar al asistente que inicie devoluciones para otras personas). El riesgo combina probabilidad e impacto. Un control reduce el riesgo. Ser precisos ayuda a los equipos a ponerse de acuerdo sobre qué corregir. En el caso de Brightwell, la consulta de pedidos entre clientes distintos era una vulnerabilidad; un estafador que busca reembolsos es la amenaza; el servicio de políticas es el control. Mantener separadas estas palabras evita que un equipo llame vulnerabilidad al estafador o amenaza al modelo, lo que confunde sobre quién debe actuar. También ayuda al redactar un informe de hallazgo, porque cada parte tiene un lector distinto.

### 5.3 Marcos

El NIST AI RMF (AI 100-1) organiza el trabajo sobre el riesgo en Govern, Map, Measure y Manage (gobernar, cartografiar, medir y gestionar). El OWASP Top 10 for LLM Applications 2025 enumera los riesgos habituales de las aplicaciones, desde LLM01 Prompt Injection hasta LLM10 Unbounded Consumption. MITRE ATLAS cataloga las técnicas de los atacantes contra la IA. ISO/IEC 42001 define un sistema de gestión de la IA. Jonas los usa juntos para Brightwell: la lista de OWASP para nombrar los riesgos de aplicación de Ask Brightwell, ATLAS para los ataques contra ReturnGuard, como la extracción, y las funciones del AI RMF para organizar el trabajo. ISO/IEC 42001 pasa a ser pertinente si Brightwell busca la certificación de su gestión de la IA.

### 5.4 Práctica autorizada

Pruebe solo los sistemas que esté autorizado a probar, por escrito y dentro del alcance. Use copias aisladas y datos sintéticos. Comunique los hallazgos por los canales acordados. La curiosidad no es una autorización. La autorización de Jonas cubre la copia de preproducción de Ask Brightwell, no la producción. Cuando quiso comprobar si la consulta entre clientes también funcionaba en vivo, se lo preguntó a su responsable en lugar de intentarlo, y la prueba se ejecutó en preproducción con cuentas de prueba. Todas las pruebas posteriores de este libro se mantienen dentro del mismo alcance escrito. El alcance escrito también protege a Jonas si una prueba en preproducción rompe algo, porque la prueba se acordó de antemano.

### 5.4b Comunicar un hallazgo

Un buen informe de hallazgo indica el sistema y la versión, los pasos para reproducirlo en la copia autorizada, el efecto observado, el impacto en términos de la tríada CIA, una gravedad y una corrección sugerida. Manténgalo factual y evite los detalles de explotación que vayan más allá de lo que necesita el equipo que corrige. El informe de Jonas sobre la consulta entre clientes siguió esta forma: versión de preproducción, la petición «muestra el pedido 100245» desde otro cliente de prueba, la dirección mostrada, un impacto en la confidencialidad y la corrección en el servicio de la herramienta. Su informe omitió cualquier redacción que ayudara a abusar del fallo.

### 5.5 Ejemplo resuelto (caso sintético de Brightwell)

Jonas enumera los riesgos de Ask Brightwell en términos de la tríada CIA: confidencialidad, los detalles de los pedidos de otros clientes; integridad, una reseña plantada ordena al asistente aprobar devoluciones; disponibilidad, avalanchas de *tokens*. Asigna el segundo a OWASP LLM01 y LLM06 (agencia excesiva) y comprueba que su autorización de pruebas cubre solo la copia de preproducción. Escribir los riesgos así dio a cada uno una prueba que podía ejecutar en preproducción y un control que proponer. Confirmar el alcance de su autorización antes de probar mantuvo el trabajo en la copia de preproducción, donde las reseñas plantadas y los clientes de prueba no pueden hacer daño.

### 5.6 Errores y límites

- Llamar «vulnerabilidad» a cualquier problema.
- Probar en producción «solo para comprobar».
- Usar marcos sin relacionarlos con el sistema.

La lista de Jonas para Ask Brightwell evitó estos errores. El riesgo de avalancha de *tokens* se describe como una laguna de diseño y no como una vulnerabilidad del modelo, todas las pruebas se mantuvieron en preproducción y cada entrada de un marco está vinculada a una parte del dibujo. Una etiqueta que no puede vincularse a un componente no le dice a nadie qué corregir. Estos hábitos hacen que los desarrolladores puedan actuar con facilidad sobre sus informes posteriores.

### Ejercicios

- **EX013 — Tríada CIA.** Dé un riesgo de confidencialidad, uno de integridad y uno de disponibilidad para ReturnGuard. Rúbrica: 3 = tres adecuados; 2 = dos; 1 = uno; 0 = ninguno.
- **EX014 — Vocabulario.** Etiquete la amenaza, la vulnerabilidad, el riesgo y el control en un escenario breve. Rúbrica: 3 = los cuatro correctos; 2 = tres; 1 = uno o dos; 0 = ninguno.
- **EX015 — Autorización.** Un amigo le pide que pruebe el *chatbot* de su empresa. ¿Qué debe existir primero? Rúbrica: 3 = autorización escrita del propietario, alcance, reglas, canal de comunicación; 2 = tres; 1 = uno; 0 = hacerlo sin más.

### Síntesis

La alfabetización en seguridad aporta palabras compartidas —tríada CIA, amenaza, vulnerabilidad, riesgo, control—, marcos compartidos y la disciplina de la práctica autorizada.

### Siga estudiando — capítulo 05 de 30

[← Capítulo 04 (borrador)](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 (borrador) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operativos y virtualización

### Resultados de aprendizaje

Usted podrá (1) explicar los procesos, los usuarios, los permisos de archivos y el aislamiento; (2) usar contenedores y máquinas virtuales para aislar los componentes de IA; (3) confinar en un entorno aislado el código generado o ejecutado por herramientas de IA; y (4) proteger los archivos de modelos en reposo.

### 6.1 Procesos y permisos

Todo servicio se ejecuta como un proceso bajo una cuenta de usuario. Si el orquestador se ejecuta como *root*, un fallo se convierte en un compromiso total del sistema. Ejecute cada componente con su propio usuario de bajo privilegio y con acceso de lectura solo a los archivos que necesita. En Ask Brightwell, el orquestador, el servicio de recuperación y los servicios de herramientas se ejecutan cada uno con su propia cuenta, de modo que un fallo en el orquestador no puede leer directamente la base de datos de pedidos. La cuenta de la herramienta de pedidos puede leer los pedidos pero no modificarlos, y la cuenta de la herramienta de devoluciones puede crear devoluciones pero no leer otras tablas. Jonas lo confirma en preproducción enviando una consulta a la tabla de pedidos con la cuenta del orquestador y comprobando que la base de datos la rechaza.

### 6.2 Contenedores y máquinas virtuales

Los contenedores empaquetan un servicio con sus dependencias y lo aíslan mediante funciones del núcleo; las máquinas virtuales aíslan con más fuerza, con un núcleo separado. Ejecute los servidores de modelos, la recuperación y los servicios de herramientas en contenedores separados con imágenes mínimas, sistemas de archivos de solo lectura cuando sea posible y sin acceso de red innecesario. En CodePilot, el servidor del modelo autoalojado se ejecuta en su propio contenedor con un sistema de archivos de solo lectura, de modo que un servidor comprometido no puede reescribir sus archivos de modelo. Los servicios de herramientas de Ask Brightwell están en contenedores separados con reglas de red que solo permiten que los llame el orquestador. Las imágenes separadas también dejan claro qué componente necesita qué secreto.

### 6.3 Aislamiento del código generado

Los asistentes de programación y los agentes con una herramienta de «ejecutar código» ejecutan texto producido por un modelo, un texto en el que un atacante puede influir. Ejecute ese código en un entorno aislado desechable: sin red por defecto, sin acceso a secretos, con límites de CPU y de memoria, con un límite de tiempo y destruido tras su uso. El botón original «ejecutar pruebas» de CodePilot incumplía todas estas reglas: ejecutaba el código generado en un servidor de compilación compartido que tenía claves de despliegue. El nuevo diseño arranca un contenedor nuevo para cada ejecución, sin red, sin secretos y con un límite de tiempo, y lo destruye después. Un comentario plantado todavía puede moldear el código, pero el código ya no puede llegar a nada valioso.

### 6.4 Archivos de modelos en reposo

Los archivos de pesos de un modelo pueden sustituirse o manipularse. Algunos formatos (por ejemplo, los archivos basados en *pickle* de Python) pueden ejecutar código al cargarse. Prefiera formatos que solo almacenan tensores, verifique los *hashes* antes de cargar y restrinja quién puede escribir en los directorios de modelos.

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

Para el modelo autoalojado de CodePilot, Brightwell guarda el *hash* esperado de cada archivo en el control de versiones y el cargador se niega a arrancar si un archivo difiere. Solo la cuenta de la cadena de despliegue puede escribir en el directorio de modelos, y registra cada escritura, de modo que un archivo sustituido quedaría a la vez bloqueado y visible.

### 6.5 Ejemplo resuelto (caso sintético de Brightwell)

CodePilot ofrece un botón «ejecutar pruebas» que ejecuta el código generado en un servidor de compilación compartido con acceso a claves de despliegue. Jonas muestra en una copia que un comentario en un archivo de código abierto descargado puede llevar al asistente a escribir código que imprime las variables de entorno. Traslada la ejecución a un contenedor desechable sin red ni secretos y añade comprobaciones de *hash* para los archivos del modelo autoalojado; el laboratorio muestra cómo se detecta un archivo modificado. El comentario plantado no necesitó explotar nada: solo tuvo que persuadir al asistente, y el acceso del servidor de compilación hizo el resto.

### 6.6 Errores y límites

- Servicios que se ejecutan como *root*.
- Ejecutar código generado por el modelo en máquinas compartidas.
- Cargar archivos de modelos sin comprobaciones de integridad.

El diseño original de CodePilot tenía el segundo error y el orquestador anterior de Ask Brightwell se arriesgaba al primero. Los cambios de este capítulo dan a cada servicio su propia cuenta, trasladan el código generado a un contenedor desechable y comprueban los *hashes* de los archivos de modelos antes de cargarlos. Cada error es barato de evitar cuando se construye un servicio y caro de corregir cuando otros sistemas ya dependen de él. La cadena de despliegue ejecuta ahora una comprobación para cada error en cada despliegue.

### Ejercicios

- **EX016 — Mínimo privilegio.** Enumere los permisos que necesita y los que no necesita el servicio de recuperación. Rúbrica: 3 = leer el índice, red solo hacia el orquestador; sin escritura, sin secretos; 2 = parcial; 1 = vago; 0 = ninguno.
- **EX017 — Entorno aislado.** Especifique cinco ajustes del entorno aislado para la herramienta de código de un agente. Rúbrica: 3 = sin red, sin secretos, CPU/memoria, límite de tiempo, desechable; 2 = cuatro; 1 = dos; 0 = ninguno.
- **EX018 — Laboratorio de *hashes*.** ¿Qué debe ocurrir cuando el laboratorio informa MISMATCH para model.bin? Rúbrica: 3 = negarse a cargarlo, alertar, investigar el origen; 2 = dos; 1 = uno; 0 = cargarlo de todos modos.

### Síntesis

El aislamiento del sistema operativo limita lo que puede hacer un componente de IA comprometido: cuentas de mínimo privilegio, contenedores, entornos aislados desechables y archivos de modelos verificados.

### Siga estudiando — capítulo 06 de 30

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](../../en/book/MANUSCRIPT.md#ch-07)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo; cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación. Brightwell Home, Jonas y todas sus cifras son sintéticos.

**EX001.** Navegador (política de seguridad de contenidos); CDN/perímetro (TLS, protección contra DDoS); aplicación web (autenticación); orquestador (construcción del *prompt*, codificación de las salidas); recuperación (filtrado por permisos); API del modelo (clave en un gestor de secretos, cuotas); herramientas (comprobaciones de titularidad); bases de datos (cuentas de mínimo privilegio, cifrado).

**EX002.** En la base de datos de pedidos; en la respuesta de la herramienta guardada en la memoria del orquestador; en el *prompt* enviado a la API del proveedor y, posiblemente, en los registros del proveedor; en los registros de *prompts* del orquestador; en una caché de respuestas.

**EX003.** El tiempo de GPU, que en la práctica significa *tokens*. Limite el máximo de *tokens* de entrada y de salida por petición y fije presupuestos de peticiones y de *tokens* por usuario con colas, para que ningún usuario pueda monopolizar la GPU.

**EX004.** DNS (DNSSEC o bloqueo en el registrador y supervisión); TLS hasta el perímetro (versiones actuales, HSTS); HTTP hasta la aplicación web (autenticación, límites de tamaño); llamadas internas (TLS mutuo, política de red); API del proveedor (TLS, clave en el servidor, cuotas).

**EX005.** A 2/s con ráfaga 10, se atienden las 90 peticiones normales mientras la avalancha cae a 129/3000. A 1/s, los usuarios normales fallan (62/90). Por tanto, 2/s equilibra el servicio frente al abuso.

**EX006.** Cualquiera puede copiar la clave y lanzar peticiones a costa de Brightwell, o abusar de las condiciones del proveedor en nombre de Brightwell. Rote la clave de inmediato, lleve las llamadas al servidor tras una autenticación y fije en el proveedor límites de gasto y alcances.

**EX007.**

```
parse JSON → fail → reject
keys == {"action","order_id"} → else reject
type(action) is str and action in {"lookup","return"} → else reject
order_id matches ^[0-9]{6}$ → else reject
pass to tool service (which rechecks ownership)
```

**EX008.** HTML: escape según el contexto. SQL: consultas parametrizadas. *Shell*: evite por completo el *shell* y pase los argumentos como una lista a un programa fijo, con una lista de permitidos de valores.

**EX009.** Con eps 1,0, la exactitud (0,505) está cerca del azar: cambios pequeños y elegidos deliberadamente invierten aproximadamente la mitad de las decisiones. Es un modelo lineal de juguete, pero muestra que no se puede confiar en las salidas ante una entrada adversaria.

**EX010.**
- responsable (*owner*): a quién preguntar por el contenido;
- público destinatario (público/personal): filtra la recuperación;
- sensibilidad: bloquea los fragmentos restringidos;
- fuente: procedencia para auditorías y comprobaciones de envenenamiento;
- fecha de actualización: elimina el contenido obsoleto.

**EX011.** Las consultas de los clientes buscaban en un índice mixto que incluía la hoja interna de márgenes, y el modelo la citó. Correcciones: un índice de clientes separado y solo público, y filtrar por público destinatario antes de que los fragmentos entren en el *prompt*.

**EX012.**
- Páginas de productos: públicas.
- Política de devoluciones: pública.
- Márgenes de proveedores: confidenciales.
- Pedidos y direcciones de clientes: personales.
- Datos de entrenamiento de ReturnGuard, derivados de los pedidos de clientes: personales y confidenciales.

**EX013.** Confidencialidad: filtración del historial de devoluciones de los clientes a través de las explicaciones. Integridad: estafadores que moldean las devoluciones para evitar las alertas, o que envenenan las etiquetas. Disponibilidad: caída del servicio de puntuación, de modo que las devoluciones se atascan.

**EX014.** Escenario: «Un estafador (amenaza) puede ordenar al asistente que inicie devoluciones de pedidos de otros clientes porque la herramienta carece de comprobaciones de titularidad (vulnerabilidad). Esto podría causar pérdidas de unos pocos miles de euros al mes (riesgo). Una comprobación de titularidad en el servicio de la herramienta (control) lo elimina».

**EX015.** Una autorización escrita de alguien que sea propietario del sistema, un alcance definido y reglas de enfrentamiento (copias, datos, horarios) y un canal de comunicación acordado. Si no, rechace el encargo.

**EX016.** Necesita acceso de lectura a los archivos del índice y acceso de red solo hacia el orquestador. No necesita acceso de escritura al índice, credenciales de la base de datos, salida a internet ni secretos de otros servicios.

**EX017.**
- Sin red.
- Sin secretos ni credenciales montados.
- Topes de CPU y de memoria.
- Un límite de tiempo de 60 segundos o menos.
- Un contenedor nuevo por ejecución, destruido después, con una imagen base de solo lectura.

**EX018.** Negarse a cargar el archivo, alertar al responsable y a seguridad, compararlo con la fuente de confianza, revisar los registros de acceso a model.bin y volver a desplegar a partir de un artefacto verificado.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; los marcos cambian, así que vuelva a verificarlos. Los identificadores de arXiv se abrieron y se comprobaron sus títulos. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Abadi, M. et al. (2016). Deep Learning with Differential Privacy. arXiv:1607.00133.
- Arp, D. et al. (2020). Dos and Don'ts of Machine Learning in Computer Security. arXiv:2010.09470.
- Athalye, A., Carlini, N., Wagner, D. (2018). Obfuscated Gradients Give a False Sense of Security. arXiv:1802.00420.
- Carlini, N. et al. (2019). On Evaluating Adversarial Robustness. arXiv:1902.06705.
- Chen, S. et al. (2024). StruQ: Defending Against Prompt Injection with Structured Queries. arXiv:2402.06363.
- European Union. Regulation (EU) 2024/1689 (Artificial Intelligence Act). <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
- Goodfellow, I., Shlens, J., Szegedy, C. (2014). Explaining and Harnessing Adversarial Examples. arXiv:1412.6572.
- Greshake, K. et al. (2023). Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. arXiv:2302.12173.
- Gu, T., Dolan-Gavitt, B., Garg, S. (2017). BadNets. arXiv:1708.06733.
- ISO/IEC 42001:2023 Artificial intelligence — Management system. <https://www.iso.org/standard/81230.html>
- MITRE ATLAS. <https://atlas.mitre.org/>
- NIST AI 100-1 (2023), AI RMF 1.0. <https://doi.org/10.6028/NIST.AI.100-1>
- NIST AI 100-2 E2025 (2025), Adversarial Machine Learning taxonomy. <https://doi.org/10.6028/NIST.AI.100-2e2025>
- NIST AI 600-1 (2024), Generative AI Profile. <https://doi.org/10.6028/NIST.AI.600-1>
- OWASP Top 10 for LLM Applications 2025. <https://genai.owasp.org/llm-top-10/>
- Shokri, R. et al. (2016). Membership Inference Attacks against Machine Learning Models. arXiv:1610.05820.
- Szegedy, C. et al. (2013). Intriguing properties of neural networks. arXiv:1312.6199.
- Tramèr, F. et al. (2016). Stealing Machine Learning Models via Prediction APIs. arXiv:1609.02943.
