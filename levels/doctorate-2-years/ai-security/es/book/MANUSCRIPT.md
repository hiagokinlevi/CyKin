# Seguridad de la IA y del aprendizaje automático: guía de investigación doctoral

- Idioma: español neutro (`es`); programa de investigación doctoral, dos años; aproximadamente 1.600 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–8 de 8 tienen texto didáctico de autor; los ejercicios EX001–EX052 tienen sus resultados resueltos correspondientes con rúbricas de 0 a 3; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas impresas proceden de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4. Que los capítulos estén en borrador no significa que el libro esté terminado.
- Público: investigadores avanzados, con experiencia en investigación y una pregunta original defendible, que pondrán a prueba de forma independiente una contribución original, y sus límites, en la seguridad de la IA y del aprendizaje automático.
- Relación con los libros vecinos: el [libro de maestría](../../../../masters-2-years/ai-security/en/book/MANUSCRIPT.md) enseña una primera tesis supervisada; el [libro de posgrado](../../../../postgraduate-2-years/ai-security/en/book/MANUSCRIPT.md) enseña la práctica especializada y el aseguramiento. **Este libro trata de producir y defender conocimiento nuevo**: integridad, cartografía de la frontera, una propuesta falsable, replicación de la línea de base, un estudio principal con validación independiente, crítica, un archivo y una defensa.
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título y no concede autorización para probar sistemas reales. Todas las organizaciones, personas, conjuntos de datos y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Ocho capítulos siguen el arco de un doctorado: integridad y métodos (1), la frontera de la investigación (2), una propuesta (3), replicación de la línea de base y piloto (4), el estudio principal y la validación independiente (5), crítica de pares y revisión (6), síntesis y un archivo de reproducibilidad (7), y defensa y publicación (8). Cada capítulo tiene resultados de aprendizaje, texto didáctico, un ejemplo resuelto, actividades de práctica, errores y límites, ejercicios puntuados de 0 a 3 (0 = ausente o inseguro; 1 = laguna importante; 2 = lagunas menores; 3 = completo y justificado), una síntesis y un bloque **Siga estudiando**. Los laboratorios son deterministas, se ejecutan sin conexión con `python3 file.py` e imprimen los resultados que se muestran bajo *Salida esperada*.

### El ejemplo de referencia (sintético): Meridian Applied AI Lab

> **Caso sintético — ficción.** El **Meridian Applied AI Lab (MAAL)** es un grupo universitario inventado. La doctoranda *Ana Okafor* estudia si la *separación estructural entre las instrucciones y los datos recuperados* reduce la inyección indirecta de instrucciones (*prompt injection*) en agentes de modelos de lenguaje que usan herramientas de forma más fiable que el filtrado de contenidos. El MAAL solo usa bancos de pruebas locales y aislados, documentos sintéticos y cargas útiles canario inofensivas dirigidas a dominios reservados `.invalid`. Todos los números sobre el MAAL son inventados.

### Política de fuentes

Las fuentes se comprobaron el 12 de octubre de 2026: NIST [AI 100-1](https://doi.org/10.6028/NIST.AI.100-1) (AI RMF 1.0, 2023), [AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) (perfil de IA generativa, 2024) y [AI 100-2 E2025](https://doi.org/10.6028/NIST.AI.100-2e2025) (taxonomía del aprendizaje automático adversarial); el [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [MITRE ATLAS](https://atlas.mitre.org/); el [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) (Reglamento de Inteligencia Artificial); y [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html). Los artículos de investigación se citan por su identificador de arXiv, y cada uno se abrió y se comprobó su título. Los marcos tienen versiones y cambian; vuelva a comprobarlos antes de basarse en ellos.

## Contenido

| Etapa | Capítulo |
|---|---|
| 1 | [1 Integridad y métodos avanzados de investigación](#ch-01) |
| 1 | [2 Seguridad de la IA y del aprendizaje automático: frontera de la investigación](../../en/book/MANUSCRIPT.md#ch-02) |
| 2 | [3 Propuesta de contribución original](../../en/book/MANUSCRIPT.md#ch-03) |
| 2 | [4 Replicación de la línea de base y piloto](../../en/book/MANUSCRIPT.md#ch-04) |
| 3 | [5 Estudio principal y validación independiente](../../en/book/MANUSCRIPT.md#ch-05) |
| 3 | [6 Crítica de pares y revisión](../../en/book/MANUSCRIPT.md#ch-06) |
| 4 | [7 Síntesis de la tesis y archivo de reproducibilidad](../../en/book/MANUSCRIPT.md#ch-07) |
| 4 | [8 Defensa y plan de publicación](../../en/book/MANUSCRIPT.md#ch-08) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Integridad y métodos avanzados de investigación

### Resultados de aprendizaje

Usted podrá (1) explicar por qué la investigación en seguridad de la IA está especialmente expuesta al error de medición, a la fuga de datos y al daño de doble uso; (2) separar las *afirmaciones de seguridad* de las *afirmaciones de capacidad* y formular cada una de modo que pueda refutarse; (3) diseñar una evaluación con un modelo de amenazas declarado, métricas especificadas de antemano y un adversario adaptativo; (4) aplicar las normas sobre autorización, protección de datos y divulgación responsable que obligan a la investigación de seguridad sobre modelos y servicios de IA; y (5) comunicar la incertidumbre con intervalos en lugar de con números aislados.

### 1.1 Por qué la integridad es un método y no una cortesía

La integridad de la investigación en seguridad de la IA no es una lista de hábitos corteses; es el conjunto de procedimientos que hacen que un resultado sea cierto fuera del laboratorio donde se obtuvo. El campo tiene un historial documentado de resultados que no sobrevivieron al contacto con un adversario más fuerte. Athalye, Carlini y Wagner (arXiv:1802.00420) mostraron que siete de nueve defensas aceptadas en un congreso de primer nivel se basaban en *gradientes ofuscados*: la defensa no hacía robusto el modelo, solo rompía la optimización del atacante. Una vez adaptado el ataque, la mayoría de las defensas cayeron. Carlini y sus colegas escribieron después *On Evaluating Adversarial Robustness* (arXiv:1902.06705), una lista de comprobación que convierte esa lección en método: declarar el modelo de amenazas, usar ataques adaptativos, comunicar el presupuesto del ataque, verificar que los ataques más fuertes nunca rinden peor que los más débiles y publicar el código. Arp et al. (arXiv:2010.09470) catalogaron diez escollos del aprendizaje automático en la seguridad informática (sesgo de muestreo, etiquetas inexactas, fisgoneo de datos, correlaciones espurias, selección sesgada de parámetros, líneas de base inadecuadas, falacia de la tasa base, evaluación solo en laboratorio, modelo de amenazas inadecuado y medidas de rendimiento inadecuadas) y los encontraron extendidos en artículos de los congresos más importantes. Kapoor y Narayanan (arXiv:2207.07048) mostraron que la *fuga* entre los datos de entrenamiento y de evaluación había inflado los resultados en muchos campos científicos que usaban el aprendizaje automático. Lipton y Steinhardt (arXiv:1807.03341) describieron «tendencias preocupantes» más amplias: no distinguir la explicación de la especulación, fuentes poco claras de las mejoras y mal uso de las matemáticas.

Un investigador doctoral debe tratar estos artículos como la descripción del modo de fallo por defecto. Si no hace nada especial, su resultado probablemente será optimista.

### 1.2 Afirmaciones de seguridad y afirmaciones de capacidad

Una *afirmación de capacidad* dice lo que un sistema puede hacer («el detector señala el 94 % de los documentos con inyección»). Una *afirmación de seguridad* dice lo que un adversario no puede hacer en condiciones declaradas («ningún atacante adaptativo con acceso de caja negra y 1.000 consultas consigue más de un 5 % de secuestro de herramientas»). Las afirmaciones de seguridad están cuantificadas universalmente sobre los adversarios, y por eso son frágiles: un solo contraejemplo las refuta. Escriba cada afirmación en tres partes: el **adversario** (objetivos, conocimiento, capacidades, presupuesto), el **sistema** (modelo, versión, configuración, herramientas, datos) y la **propiedad**, con su métrica y su umbral. NIST AI 100-2 E2025 organiza los ataques contra la IA predictiva y generativa según el objetivo del atacante (disponibilidad, integridad, privacidad y, para los sistemas generativos, facilitación del uso indebido), su conocimiento (caja blanca, gris o negra), su capacidad (control de los datos de entrenamiento, control del modelo, acceso por consultas, control de recursos) y la etapa del ciclo de vida; use su vocabulario para que los revisores puedan situar su afirmación.

### 1.3 Métodos que sobreviven a la revisión

Cinco hábitos soportan la mayor parte del peso. **Especificación previa**: escriba las hipótesis, las métricas, los conjuntos de datos y las reglas de parada antes de mirar los resultados de prueba, y registre después cada cambio. **Separación**: mantenga un conjunto de prueba sellado que ningún ajuste toque nunca; elimine los elementos casi idénticos entre particiones, algo muy importante en los datos de lenguaje extraídos de la web. **Adversarios adaptativos**: para cada defensa, pregúntese cómo respondería un atacante que la conoce, y construya ese ataque. **Líneas de base fuertes**: compare con el mejor método sencillo, no con un hombre de paja. **Incertidumbre**: comunique intervalos de confianza, el número de semillas y la varianza. Una tasa de éxito de ataque de 3 sobre 20 (15 %) tiene un intervalo de Wilson al 95 % de aproximadamente el 5 % al 36 %, demasiado amplio para ordenar dos defensas.

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

El laboratorio muestra la misma tasa del 15 % con tres tamaños de muestra. Solo la muestra mayor respalda una afirmación con dos decimales. A lo largo de cinco semillas la tasa oscila entre el 10,5 % y el 14,5 %, así que un resultado con una sola semilla podría inducir a error. El *bootstrap* emparejado estima la reducción que logra una defensa sobre las *mismas* instrucciones, que es la comparación que realmente importa, y su intervalo excluye el cero.

### 1.4 Autorización, datos y divulgación

La investigación de seguridad sobre la IA afecta a sistemas, datos y seguridad de otras personas. Pruebe solo sistemas que sean suyos o que tenga autorización por escrito para probar, con un alcance que nombre los modelos, los puntos de acceso, las cuentas, los límites de frecuencia y las fechas. Las condiciones de servicio de las API de modelos alojados suelen restringir algunas formas de prueba; léalas y pregunte al proveedor en caso de duda. Los datos personales presentes en instrucciones, conjuntos de entrenamiento o registros están sujetos a la legislación de protección de datos (por ejemplo, el RGPD en la UE); minimícelos, seudonimícelos y obtenga la aprobación del comité de ética cuando intervengan participantes humanos o sus datos. *Nota para el lector hispanohablante:* en España, el RGPD se complementa con la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales; en América Latina rige la ley de cada país, por ejemplo la Ley 25.326 en Argentina o la Ley 1581 de 2012 en Colombia. Cuando encuentre una debilidad en un producto desplegado, use la divulgación coordinada: notifique al fabricante en privado, acuerde un calendario y publique sin detalles operativos que ayudarían sobre todo a los atacantes. La revisión del doble uso debe ser explícita: para cada artefacto (código, instrucciones, conjuntos de datos, pesos del modelo), pregúntese quién se beneficia más de su publicación, los defensores o los atacantes, y si una publicación escalonada o con acceso controlado cambia la respuesta.

### 1.5 Ejemplo resuelto (caso sintético del MAAL)

El primer borrador de afirmación de Ana era «nuestra defensa por separación detiene la inyección de instrucciones». Su directora de tesis la reescribió así. *Adversario*: un tercero que controla el texto de hasta un documento recuperado por tarea, conoce el diseño de la defensa (al estilo de Kerckhoffs), no tiene los pesos del modelo y puede probar 200 variantes de carga útil por familia de tareas. *Sistema*: un modelo local de pesos abiertos en un entorno aislado con tres herramientas (búsqueda, resumen, correo a direcciones de la lista de permitidos), con la plantilla de instrucciones fija v1.3. *Propiedad*: tasa de llamadas no autorizadas a herramientas (cualquier llamada que el usuario no haya pedido) sobre 600 tareas reservadas, con un límite superior del intervalo al 95 % por debajo del 2 %. La reescritura es falsable, nombra un presupuesto y vincula la afirmación a una versión. También deja a la vista la parte difícil: «conoce el diseño de la defensa» significa que Ana debe construir ataques adaptativos contra su propio método.

### 1.6 Actividades de práctica

1. Tome un artículo reciente de seguridad de la IA que admire y reescriba su afirmación principal en la forma adversario–sistema–propiedad. 2. Aplique la lista de escollos de Arp et al. a su último experimento. 3. Redacte un plan de autorización y de datos de una página para su banco de pruebas doctoral. Para la primera actividad, use como modelo la reescritura del MAAL: nombre el conocimiento y el presupuesto del adversario, vincule el sistema a una versión y dé a la propiedad una métrica y un umbral. Si el artículo no dice lo suficiente para completar una parte, anótelo como una laguna del artículo. Para la segunda, marque cada uno de los diez escollos como presente, ausente o desconocido, con una frase de evidencia. Para la tercera, nombre los modelos, los puntos de acceso, los datos y las fechas, e indique quién aprueba.

### 1.7 Errores y límites

Cada uno de estos errores hace que un resultado parezca más fuerte de lo que es:

- Comunicar la mejor de muchas ejecuciones como «el» resultado, lo que oculta la dispersión entre semillas que muestra el Lab S.
- Ajustar instrucciones o umbrales sobre el conjunto de prueba, lo que lo convierte en datos de entrenamiento.
- Evaluar una defensa solo contra ataques diseñados antes de que existiera; esa defensa no se ha enfrentado al adversario adaptativo del modelo de amenazas de Ana.
- Tratar «no se encontró ningún ataque» como prueba de seguridad, cuando puede significar solo que la búsqueda fue débil.
- Publicar cadenas de explotación funcionales contra un producto en servicio antes de que el fabricante pueda responder, lo que perjudica a los usuarios antes de que exista una corrección.

### Ejercicios — capítulo 1

- **EX001 — Reescribir una afirmación.** Reescriba «nuestro filtro protege a los chatbots de los *jailbreaks*» como una afirmación de seguridad falsable. Rúbrica: 3 = adversario con conocimiento y presupuesto, sistema con versión, propiedad con métrica y umbral; 2 = una parte vaga; 1 = faltan dos partes; 0 = sin cambios o insegura.
- **EX002 — Gradientes ofuscados.** Explique en dos frases por qué una defensa que rompe el cálculo del gradiente del atacante no es evidencia de robustez. Rúbrica: 3 = distingue el fallo del ataque de la robustez del modelo y nombra el remedio (ataque adaptativo de tipo BPDA o sin gradientes); 2 = la idea sin el remedio; 1 = vago; 0 = incorrecto.
- **EX003 — Intervalo.** A partir del laboratorio, indique qué puede y qué no puede afirmar con 3 éxitos de 20. Rúbrica: 3 = intervalo ≈0,05–0,36, no se pueden ordenar defensas que difieren en pocos puntos, se necesita una n mayor; 2 = solo el intervalo; 1 = solo la estimación puntual; 0 = incorrecto.
- **EX004 — Escollos.** Nombre tres de los diez escollos de Arp et al. y dé una salvaguarda para cada uno. Rúbrica: 3 = tres correctos con salvaguardas; 2 = tres sin salvaguardas; 1 = uno o dos; 0 = ninguno.
- **EX005 — Fuga.** Describa cómo las instrucciones casi duplicadas entre las particiones de entrenamiento y de prueba inflan la puntuación de un detector de *jailbreaks*, y una prueba para detectarlo. Rúbrica: 3 = mecanismo más prueba de deduplicación por *hash* o de solapamiento de n-gramas; 2 = solo el mecanismo; 1 = vago; 0 = incorrecto.
- **EX006 — Alcance.** Enumere cinco campos que debe contener una autorización para probar un modelo alojado. Rúbrica: 3 = sistemas o puntos de acceso, métodos, fechas, límites de frecuencia o de datos, contactos y condiciones de parada; 2 = cuatro; 1 = dos o tres; 0 = ninguno o inseguro.
- **EX007 — Doble uso.** Para un conjunto de datos de 5.000 cargas útiles de inyección que tuvieron éxito, proponga una decisión de publicación y justifíquela. Rúbrica: 3 = sopesa el beneficio para defensores y atacantes, propone una publicación con acceso controlado, escalonada o censurada, y menciona la divulgación al fabricante; 2 = decisión con razones parciales; 1 = solo la decisión; 0 = publicación incondicional de explotaciones activas sin razonamiento.

### Síntesis del capítulo

La integridad en la seguridad de la IA es operativa: afirmaciones falsables, datos de prueba sellados, adversarios adaptativos, incertidumbre honesta y trabajo autorizado y divulgado. Son las herramientas que hacen fiable el resto del doctorado.

### Siga estudiando — capítulo 01 de 08

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](../../en/book/MANUSCRIPT.md#ch-02)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo; cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación. El Meridian Applied AI Lab y todos sus números son sintéticos.

**EX001.** «Frente a un adversario que controla las instrucciones del usuario, conoce el diseño del filtro y puede enviar 500 intentos por categoría de la política, el modelo *M* v2.1 con el filtro *F* v1.0 produce una salida que infringe la política en menos del 3 % de 1.000 peticiones dañinas reservadas (límite superior al 95 %), con una tasa de falsos rechazos inferior al 5 % en 1.000 peticiones benignas.»

**EX002.** Una defensa que rompe el cálculo del gradiente hace que falle el ataque basado en gradientes, no que el modelo acierte; las mismas entradas pueden seguir clasificándose mal. El remedio es un ataque adaptativo: aproximar el componente roto (BPDA), usar la esperanza sobre transformaciones o pasar a una búsqueda sin gradientes.

**EX003.** 3/20 = 15 %, con un intervalo de Wilson al 95 % de aproximadamente el 5,2 % al 36,0 %. Puede decir que la tasa probablemente no es cero y probablemente está por debajo del 40 %; no puede ordenarla frente a otra defensa que esté a pocos puntos. Aumente n (2.000 ensayos dan aproximadamente del 13,5 % al 16,6 %).

**EX004.** Tres cualesquiera, por ejemplo: fisgoneo de datos → sellar los datos de prueba y prerregistrar; falacia de la tasa base → comunicar la precisión y la FPR con tasas base realistas; evaluación solo en laboratorio → validar en un despliegue realista o declarar el límite; línea de base inadecuada → incluir líneas de base sencillas y fuertes; sesgo de muestreo → documentar y diversificar las fuentes de datos.

**EX005.** Si hay paráfrasis o copias casi exactas de una instrucción de prueba en el entrenamiento, el detector reconoce texto memorizado, no el concepto del ataque, y las puntuaciones suben. Prueba: calcular el *hash* del texto normalizado y la similitud de n-gramas (por ejemplo, de 8-gramas) o de *embeddings* entre particiones; eliminar o agrupar los duplicados antes de particionar.

**EX006.** Sistemas y puntos de acceso incluidos en el alcance (versiones del modelo, cuentas); métodos permitidos; fechas y horas; límites de frecuencia, de datos y de contenido (sin datos personales, sin terceros reales); contactos, condiciones de parada y vía de notificación. Firmada por alguien con autoridad para ello.

**EX007.** Controlar el acceso. Los defensores obtienen datos de evaluación, pero las cargas útiles funcionales abaratan los ataques contra sistemas reales. Publique una versión censurada o con canarios sintéticos, entregue el corpus completo a investigadores verificados bajo condiciones y divulgue primero a los fabricantes los hallazgos específicos de cada producto.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; los marcos cambian, así que vuelva a verificarlos. Los identificadores de arXiv se abrieron y se comprobaron sus títulos. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Abadi, M. et al. (2016). Deep Learning with Differential Privacy. arXiv:1607.00133.
- Arp, D. et al. (2020/2022). Dos and Don'ts of Machine Learning in Computer Security. arXiv:2010.09470.
- Athalye, A., Carlini, N., Wagner, D. (2018). Obfuscated Gradients Give a False Sense of Security. arXiv:1802.00420.
- Biggio, B., Nelson, B., Laskov, P. (2012). Poisoning Attacks against Support Vector Machines. arXiv:1206.6389.
- Carlini, N. et al. (2019). On Evaluating Adversarial Robustness. arXiv:1902.06705.
- Carlini, N. et al. (2020). Extracting Training Data from Large Language Models. arXiv:2012.07805.
- Carlini, N. et al. (2023). Poisoning Web-Scale Training Datasets is Practical. arXiv:2302.10149.
- Carlini, N., Wagner, D. (2016). Towards Evaluating the Robustness of Neural Networks. arXiv:1608.04644.
- Chen, S. et al. (2024). StruQ: Defending Against Prompt Injection with Structured Queries. arXiv:2402.06363.
- Chen, X. et al. (2017). Targeted Backdoor Attacks on Deep Learning Systems Using Data Poisoning. arXiv:1712.05526.
- Cohen, J., Rosenfeld, E., Kolter, J. Z. (2019). Certified Adversarial Robustness via Randomized Smoothing. arXiv:1902.02918.
- European Union. Regulation (EU) 2024/1689 (Artificial Intelligence Act). <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
- Gebru, T. et al. (2018). Datasheets for Datasets. arXiv:1803.09010.
- Goodfellow, I., Shlens, J., Szegedy, C. (2014). Explaining and Harnessing Adversarial Examples. arXiv:1412.6572.
- Greshake, K. et al. (2023). Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. arXiv:2302.12173.
- Gu, T., Dolan-Gavitt, B., Garg, S. (2017). BadNets. arXiv:1708.06733.
- Henderson, P. et al. (2017). Deep Reinforcement Learning that Matters. arXiv:1709.06560.
- Hubinger, E. et al. (2024). Sleeper Agents. arXiv:2401.05566.
- ISO/IEC 42001:2023 Artificial intelligence — Management system. <https://www.iso.org/standard/81230.html>
- Kapoor, S., Narayanan, A. (2022). Leakage and the Reproducibility Crisis in ML-based Science. arXiv:2207.07048.
- Lipton, Z. C., Steinhardt, J. (2018). Troubling Trends in Machine Learning Scholarship. arXiv:1807.03341.
- Liu, Y. et al. (2023). Prompt Injection attack against LLM-integrated Applications. arXiv:2306.05499.
- Madry, A. et al. (2017). Towards Deep Learning Models Resistant to Adversarial Attacks. arXiv:1706.06083.
- MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems). <https://atlas.mitre.org/>
- Mitchell, M. et al. (2018). Model Cards for Model Reporting. arXiv:1810.03993.
- NIST AI 100-1 (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). <https://doi.org/10.6028/NIST.AI.100-1>
- NIST AI 100-2 E2025 (2025). Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations. <https://doi.org/10.6028/NIST.AI.100-2e2025>
- NIST AI 600-1 (2024). AI RMF: Generative Artificial Intelligence Profile. <https://doi.org/10.6028/NIST.AI.600-1>
- OWASP Top 10 for LLM Applications 2025. <https://genai.owasp.org/llm-top-10/>
- Perez, F., Ribeiro, I. (2022). Ignore Previous Prompt: Attack Techniques For Language Models. arXiv:2211.09527.
- Pineau, J. et al. (2020). Improving Reproducibility in Machine Learning Research. arXiv:2003.12206.
- Shokri, R. et al. (2016). Membership Inference Attacks against Machine Learning Models. arXiv:1610.05820.
- Szegedy, C. et al. (2013). Intriguing properties of neural networks. arXiv:1312.6199.
- Tramèr, F. et al. (2016). Stealing Machine Learning Models via Prediction APIs. arXiv:1609.02943.
- Wei, A., Haghtalab, N., Steinhardt, J. (2023). Jailbroken: How Does LLM Safety Training Fail? arXiv:2307.02483.
- Zou, A. et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models. arXiv:2307.15043.
