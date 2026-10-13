# Segurança de IA e Aprendizado de Máquina: Livro do Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos; aproximadamente 4.000 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 50 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3; os capítulos 11–50 (EX031–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: futuros projetistas de sistemas de segurança que vão especificar, construir, verificar e operar sistemas com IA que resistam a ataques e falhem de forma segura.
- Relação com os livros vizinhos: o [livro de bacharelado](../../../../bachelors-4-years/ai-security/en/book/MANUSCRIPT.md) é mais amplo e menos voltado ao projeto; o [livro de pós-graduação](../../../../postgraduate-2-years/ai-security/en/book/MANUSCRIPT.md) pressupõe experiência profissional. **Este livro ensina a segurança de IA como uma disciplina de engenharia**: fundamentos de matemática e computação, requisitos, arquitetura, controles, medição, confiabilidade, safety, operações e um projeto final com dossiê de evidências e defesa.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação e não concede autorização para testar sistemas reais. Todas as organizações, pessoas, conjuntos de dados e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Cinquenta capítulos acompanham o curso: fundamentos de matemática, física, programação e comunicação (1–10); sistemas computacionais e fundamentos de segurança (11–19); engenharia de segurança de IA, do contexto à otimização (20–42); e prática, projeto final, dossiê, tese e defesa (43–50). Cada capítulo tem objetivos de aprendizagem, texto didático, um exemplo resolvido, erros e limites, três exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios são determinísticos, rodam offline com `python3 arquivo.py` e imprimem os resultados mostrados em *Saída esperada*. São modelos de brinquedo que tornam um conceito mensurável, não defesas de produção.

### O exemplo contínuo (sintético): Northgate Rail Systems

> **Caso sintético — ficção.** A **Northgate Rail Systems (NRS)** é uma empresa inventada de engenharia de manutenção ferroviária. Ela opera (1) o **TrackEye**, um modelo baseado em câmeras, instalado em trens de inspeção, que sinaliza defeitos nos trilhos; (2) o **Wrench**, um assistente de manutenção baseado em modelo de linguagem que lê manuais, notas dos técnicos e boletins de fornecedores e pode redigir ordens de serviço por meio de uma interface de ferramentas; e (3) o **Pulse**, um modelo de anomalias sobre sensores de temperatura de rolamentos de eixo. O estudante de engenharia *Sam Ito* faz estágios na NRS ao longo do curso. Todo número sobre a NRS é inventado; todos os testes descritos acontecem em cópias isoladas, com autorização por escrito.

### Política de fontes

As fontes foram verificadas em 12 de outubro de 2026: NIST [AI 100-1](https://doi.org/10.6028/NIST.AI.100-1) (AI RMF 1.0), [AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) (Generative AI Profile) e [AI 100-2 E2025](https://doi.org/10.6028/NIST.AI.100-2e2025) (taxonomia de ML adversarial); o [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); o [MITRE ATLAS](https://atlas.mitre.org/); o [Regulamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) (AI Act); e a [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html). Os artigos são citados pelo identificador arXiv, e cada um foi aberto e teve o título conferido.

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) calcular derivadas das funções usadas em aprendizado de máquina (polinômios, exponenciais, logaritmos, a função logística); (2) interpretar uma derivada como sensibilidade; (3) conferir derivadas numericamente; e (4) explicar por que a mesma derivada que treina um modelo também orienta um atacante.

### 1.1 Derivadas como sensibilidade

A derivada f′(x) mede quanto f muda quando x muda um pouco: f(x + h) ≈ f(x) + h f′(x). Engenheiros usam isso como uma *sensibilidade*: se o modelo de temperatura de um rolamento tem uma derivada grande em relação a uma entrada, pequenos erros do sensor causam grandes mudanças na saída. Modelos de aprendizado de máquina são funções de entradas e parâmetros, então as derivadas nos dizem como as saídas respondem a ambos. A aproximação vale apenas para h pequeno, de modo que uma derivada descreve a vizinhança de um ponto, não a função inteira. Por isso Sam sempre informa onde uma sensibilidade foi medida, por exemplo numa imagem diurna típica, e a confere de novo em outros pontos de operação antes de tirar conclusões sobre o modelo como um todo.

### 1.2 Regras que você usará o tempo todo

Regra da potência (xⁿ)′ = n xⁿ⁻¹; exponencial (eˣ)′ = eˣ; logaritmo (ln x)′ = 1/x; regras do produto, do quociente e da cadeia. A função logística σ(z) = 1/(1 + e⁻ᶻ) leva qualquer número real a (0, 1) e satisfaz σ′(z) = σ(z)(1 − σ(z)). A perda logística para um rótulo y ∈ {−1, +1} e pontuação z = w·x é L = ln(1 + e^(−y z)); pela regra da cadeia, ∂L/∂w = −y x / (1 + e^(y w x)). Vale a pena lembrar a derivada logística porque ela é máxima em z = 0, onde σ′ = 0.25, e encolhe em direção a zero à medida que a pontuação fica confiante em qualquer das direções. Entradas perto da fronteira de decisão são, portanto, onde pequenas mudanças mais movem a saída, e é exatamente aí que um atacante começa.

### 1.3 Conferindo derivadas numericamente

Uma diferença finita central (f(x + h) − f(x − h)) / 2h aproxima f′(x) com erro proporcional a h². Compará-la com sua fórmula analítica é o teste padrão para código de gradiente; uma divergência significa um bug. O laboratório faz exatamente isso e depois dá seis passos de descida do gradiente que reduzem a perda. Na tabela impressa, as duas colunas concordam até a sexta casa decimal nos quatro pontos de teste, inclusive em w = 2, onde o gradiente é pequeno. Os passos de descida mostram a perda caindo de 2.1269 para 0.0928, e os passos cada vez menores decorrem do achatamento do gradiente à medida que w cresce e o exemplo é classificado com mais confiança.

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

Saída esperada:

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

### 1.4 Por que engenheiros de segurança se importam

O treinamento move os *parâmetros* contra o gradiente da perda. Um atacante de evasão move a *entrada* ao longo do gradiente da perda em relação à entrada, para aumentar a perda — a ideia por trás do fast gradient sign method (Goodfellow et al., arXiv:1412.6572). Assim, as derivadas são ao mesmo tempo o motor do aprendizado e um mapa para o atacante. Defesas que escondem ou quebram gradientes sem mudar o comportamento do modelo dão uma falsa sensação de segurança (Athalye et al., arXiv:1802.00420). Para quem revisa segurança, um gradiente é tanto uma ferramenta do atacante quanto de quem treina.

### 1.5 Exemplo resolvido (caso sintético da NRS)

Sam calcula a derivada da pontuação logística final do TrackEye em relação a um atributo de intensidade de pixel e encontra 0.8 por unidade, enquanto a maioria dos atributos fica abaixo de 0.05. Uma lente suja que desloca esse atributo em 0.5 muda a pontuação em cerca de 0.4 — o suficiente para inverter uma decisão limítrofe. Sam registra o atributo como uma *entrada de alta sensibilidade* para testes de robustez posteriores. A aritmética é a aproximação de primeira ordem em ação: 0.8 × 0.5 = 0.4. Ela vale apenas perto do ponto onde a derivada foi medida, então Sam depois confere a mudança real da pontuação em imagens com sujeira simulada, o que mostra se a estimativa linear subestima ou superestima o efeito. O atributo entra no plano de testes de robustez com essa ressalva registrada.

### 1.6 Erros e limites

Três erros são comuns: esquecer a derivada interna da regra da cadeia; usar um h pequeno demais nas diferenças finitas (erro de arredondamento) ou grande demais (erro de truncamento); e tratar um gradiente pequeno como prova de que nenhuma pequena mudança pode inverter a saída (funções podem ser não lineares). Cada erro tem uma proteção simples. Escrever explicitamente a função interna antes de derivar revela um fator da regra da cadeia que falta. Testar vários tamanhos de passo, como 1e-3, 1e-5 e 1e-7, mostra onde as diferenças finitas são estáveis, já que o erro primeiro cai e depois volta a subir. Quanto ao terceiro erro, um gradiente pequeno é tratado como motivo para testar diretamente mudanças maiores, nunca como garantia de que a saída não pode se inverter.

### Exercícios

- **EX001 — Derivada logística.** Mostre que σ′(z) = σ(z)(1 − σ(z)) e calcule-a em z = 0. Rubrica: 3 = dedução e 0.25; 2 = valor sem dedução; 1 = parcial; 0 = nenhuma.
- **EX002 — Leitura do laboratório.** No Lab G, quais são a perda e o gradiente em w = 0, e por que a perda cai ao longo dos seis passos? Rubrica: 3 = 0.6931, −1.0; mover-se contra o gradiente reduz a perda; 2 = só os números; 1 = vago; 0 = errado.
- **EX003 — O ponto de vista do atacante.** Explique em duas frases como um atacante usa a mesma derivada de modo diferente do treinamento. Rubrica: 3 = derivada em relação à entrada, passo para aumentar a perda; 2 = parcial; 1 = vago; 0 = errado.

### Síntese

Derivadas quantificam a sensibilidade. Elas treinam modelos e também mostram aos atacantes quais pequenas mudanças na entrada mais importam — o primeiro elo entre a matemática e a segurança de IA.

### Continue estudando — capítulo 01 de 50

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) usar conjuntos, relações, funções e lógica para descrever com precisão o comportamento de sistemas; (2) expressar políticas de acesso e de uso de ferramentas como predicados; (3) contar possibilidades para estimar espaços de busca; e (4) raciocinar sobre grafos de fluxo de dados e de controle em sistemas de IA.

### 2.1 Conjuntos, funções e lógica

Um modelo é uma função f: X → Y de um conjunto de entradas para um conjunto de saídas. Uma política é um predicado P(usuário, ação, recurso) que é verdadeiro quando a ação é permitida. Conectivos lógicos (∧, ∨, ¬, →) e quantificadores (∀, ∃) nos permitem escrever propriedades de segurança com exatidão: "∀ chamada de ferramenta c emitida pelo Wrench, Authorised(requesting_user(c), c)". Escrever propriedades dessa forma revela ambiguidades — quem é o "usuário solicitante" quando a chamada foi disparada por um texto num boletim de fornecedor? Sam resolve isso definindo o usuário solicitante como a pessoa cuja sessão iniciou a conversa.

### 2.2 Relações e grafos

Um grafo direcionado de componentes (câmera → pré-processamento → modelo → fila de alertas → técnico) mostra por onde os dados fluem e onde a confiança muda. Caminhos de uma *fonte não confiável* até um *destino privilegiado* são as rotas que um atacante pode usar; em aplicações de modelos de linguagem, o caminho "boletim do fornecedor → prompt do Wrench → ferramenta de ordens de serviço" é exatamente um caminho de injeção indireta de prompt (Greshake et al., arXiv:2302.12173). A alcançabilidade em grafos é calculada por busca em largura ou em profundidade. Desenhar o grafo primeiro torna a busca mecânica: marque cada nó cujo conteúdo um agente externo pode influenciar, marque cada nó que pode mudar algo no mundo e liste os caminhos entre eles. Cada caminho encontrado assim precisa de um controle em algum ponto do percurso, e o grafo mostra onde.

### 2.3 Contagem

A combinatória estima espaços de busca. Se um atacante pode mudar quaisquer 3 de 100 atributos para um de 4 valores, há C(100,3) × 4³ = 161,700 × 64 ≈ 10.3 milhões de variantes — viável de percorrer por computador. A contagem mostra por que "ninguém vai encontrar a entrada ruim" não é uma defesa. Dez milhões de variantes podem ser avaliadas em minutos num computador comum se cada consulta ao modelo for rápida, então o atacante não precisa de engenhosidade, só de paciência e de acesso ao modelo ou a uma cópia próxima dele. A mesma contagem diz aos defensores onde limitar consultas: se cada variante tivesse de passar por uma interface com limite de mil requisições por dia, a busca exaustiva levaria décadas, e o atacante precisaria buscar de forma muito mais engenhosa.

### 2.4 Indução e invariantes

Um *invariante* é uma propriedade que vale antes e depois de cada passo. "A ferramenta de ordens de serviço só pode ser chamada com o token de sessão de um técnico" é um invariante; provar que ele vale em todos os caminhos do código (por indução sobre os passos) é mais forte do que testar alguns casos. A indução tem duas partes. O caso base confere que nenhuma chamada de ferramenta é possível antes de existir uma sessão. O passo mostra que, se toda chamada anterior levava um token válido, o caminho do código que emite a próxima chamada também anexa um e, caso contrário, recusa. Um teste com algumas chamadas não consegue mostrar que nenhum caminho pula a verificação; um argumento sobre todos os caminhos consegue, desde que os caminhos do código estejam listados por completo.

### 2.5 Exemplo resolvido (caso sintético da NRS)

Sam desenha o grafo de fluxo de dados do Wrench com nós para o chat do usuário, manuais, notas dos técnicos, boletins de fornecedores (externos), o modelo e duas ferramentas (search, create_work_order). Existem dois caminhos de não confiável para privilegiado: boletim → modelo → create_work_order e notas dos técnicos (editáveis por terceirizados) → modelo → create_work_order. Sam escreve a propriedade "∀ chamada de create_work_order, um técnico humano a confirmou" e marca os dois caminhos para receber controles. O segundo caminho é fácil de deixar passar porque as notas dos técnicos parecem internas, mas terceirizados podem editá-las, então elas pertencem às entradas não confiáveis. A propriedade de confirmação coloca um único controle no destino, que cobre os dois caminhos de uma vez, em vez de tentar filtrar cada fonte não confiável separadamente.

### 2.6 Erros e limites

Três erros são comuns: políticas informais com exceções ocultas; esquecer caminhos indiretos através de repositórios de dados; e subestimar espaços de busca que computadores enumeram com facilidade. Exceções ocultas aparecem quando uma política escrita como 'técnicos podem criar ordens de serviço' acaba significando 'exceto terceirizados nos turnos de fim de semana', algo que ninguém escreveu. Caminhos indiretos são esquecidos quando um grafo mostra apenas conexões ativas e omite repositórios, como notas salvas hoje e lidas pelo modelo amanhã. Espaços de busca são subestimados por quem imagina um humano testando entradas à mão, e não um programa testando milhões.

### Exercícios

- **EX004 — Predicado.** Escreva um predicado afirmando que o Wrench só pode criar ordens de serviço para ativos do depósito do técnico solicitante. Rubrica: 3 = predicado quantificado correto; 2 = erro menor; 1 = informal; 0 = nenhuma.
- **EX005 — Caminhos.** Liste os caminhos de não confiável para privilegiado no grafo de Sam e um controle para cada um. Rubrica: 3 = os dois caminhos, controles sensatos; 2 = um; 1 = vago; 0 = nenhuma.
- **EX006 — Contagem.** Conte as variantes se um atacante muda quaisquer 2 de 50 atributos para um de 3 valores. Rubrica: 3 = C(50,2)×3² = 1,225×9 = 11,025; 2 = deslize aritmético; 1 = só o método; 0 = nenhuma.

### Síntese

A matemática discreta dá uma linguagem precisa para políticas, fluxos de dados e espaços de busca — a base para enunciar e verificar propriedades de segurança de IA em vez de torcer por elas.

### Continue estudando — capítulo 02 de 50

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) relacionar sinais, ruído e amostragem às entradas de sensores e câmeras; (2) explicar como condições físicas (luz, vibração, temperatura) deslocam as entradas de um modelo; (3) descrever, em nível conceitual, ataques adversariais no mundo físico e falsificação de sensores; e (4) especificar condições físicas de teste para um componente de IA.

### 3.1 Sinais, ruído e amostragem

Sensores convertem grandezas físicas em números. Toda medição contém ruído; a amostragem transforma sinais contínuos em discretos, e amostrar abaixo do dobro da maior frequência (a taxa de Nyquist) causa aliasing. Câmeras integram a luz ao longo do tempo de exposição; borrão de movimento, ofuscamento e pouca luz alteram os valores dos pixels. Um modelo de visão treinado com imagens diurnas nítidas pode encontrar entradas muito diferentes à noite ou na chuva. No TrackEye, a amostragem também se aplica ao tempo: uma câmera que captura quadros devagar demais para a velocidade do trem pode perder um defeito curto inteiro entre dois quadros. Engenheiros conferem se a taxa de quadros e o tempo de exposição servem para a maior velocidade de operação, não só para uma viagem média.

### 3.2 Deslocamentos físicos versus ataques

O deslocamento de distribuição *natural* vem da física: poeira nas lentes, deriva de temperatura em termistores, vibração. Ataques físicos *adversariais* criam deliberadamente objetos ou sinais: padrões impressos que causam classificação errada ou sinais injetados que falsificam sensores. Pesquisas mostraram que perturbações podem sobreviver à impressão e à captura por câmera sob condições de visão variadas quando otimizadas sobre muitas transformações. Os dois tipos de deslocamento precisam ser testados; a diferença de engenharia é que adversários buscam o pior caso, enquanto a natureza amostra casos típicos. O plano de testes os trata de forma diferente: deslocamentos naturais são medidos como desempenho médio nas condições esperadas, e os adversariais como o pior resultado que um atacante conseguiria encontrar dentro de limites declarados.

### 3.3 Energia, calor e canais laterais

A computação consome energia e emite calor e sinais eletromagnéticos que podem vazar informação (canais laterais). Em aceleradores de IA, medições de tempo e de consumo de energia foram estudadas como formas de inferir propriedades do modelo. O acesso físico, portanto, pertence ao modelo de ameaças de dispositivos de IA de borda, como o computador de um trem de inspeção. Esse computador percorre a rede e pode receber manutenção de terceirizados nos depósitos, então alguém poderia acoplar equipamento de medição sem muita dificuldade. Engenheiros normalmente não se defendem de todos os canais laterais, mas registram quais são plausíveis dado quem tem acesso físico e protegem os ativos mais valiosos, como os pesos do modelo e as chaves de assinatura, com invólucros que evidenciam violação e armazenamento cifrado.

### 3.4 Especificando condições físicas de teste

Uma especificação de engenharia lista condições: faixa de iluminação (lux), faixa de temperatura, espectro de vibração, níveis de contaminação da lente e velocidade do trem. Cada uma vira um eixo de teste. Para a segurança, acrescente condições adversariais dentro do modelo de ameaças — por exemplo, "um atacante pode colocar marcações nos dormentes, mas não pode acessar o trem". Cada eixo precisa de uma faixa declarada e de como ela será produzida nos testes: viagens gravadas, bancadas de iluminação controlada ou simulação. As faixas vêm de dados de operação, como a menor luminosidade medida nas viagens de madrugada e a maior velocidade da linha. Uma frase do modelo de ameaças que diz o que o atacante não pode fazer é tão importante quanto o que ele pode, porque define quando uma falha conta como achado de segurança e não como limitação.

### 3.5 Exemplo resolvido (caso sintético da NRS)

A taxa de falsos negativos do TrackEye subiu de 2% para 9% nas viagens de madrugada. Sam rastreou a causa até o sol baixo, que provoca ofuscamento a 60–80 km/h. A correção combinou um filtro polarizador, uma mudança de exposição e 4,000 imagens adicionais de madrugada. Sam também acrescentou um eixo de teste para marcações deliberadas perto dos trilhos, já que qualquer pessoa caminhando pela linha poderia colocá-las. A alta de 2% para 9% só apareceu quando os resultados foram separados por hora do dia; a média geral a escondia. A correção combina medidas físicas e de dados, e só um novo teste em viagens de madrugada recentes pode mostrar se ela funcionou.

### 3.6 Erros e limites

Três erros são comuns: testar apenas com a iluminação do laboratório; confundir deslocamento natural com ataque (ou ignorar qualquer um dos dois); e omitir o acesso físico dos modelos de ameaças de dispositivos de borda. A iluminação de laboratório é uniforme e estável, então um modelo aprovado ali ainda não encontrou ofuscamento, chuva ou lentes sujas. Tratar toda falha como ataque desperdiça esforço em caça a ameaças, enquanto tratar toda falha como natural pode esconder adulteração deliberada. Dispositivos de borda costumam estar ao alcance de pessoas com acesso legítimo ao depósito, então o acesso físico é um caminho realista, não exótico, e deixá-lo de fora faz o modelo de ameaças parecer mais seguro do que o sistema é.

### Exercícios

- **EX007 — Nyquist.** Um sensor de vibração precisa captar componentes de até 400 Hz. Que taxa mínima de amostragem evita aliasing? Rubrica: 3 = > 800 Hz com justificativa; 2 = 800 sem justificativa; 1 = errado, mas fundamentado; 0 = nenhuma.
- **EX008 — Deslocamento vs. ataque.** Classifique: poeira na lente; padrão pintado num dormente; deriva do termistor. Rubrica: 3 = natural, adversarial, natural, com justificativas; 2 = só os rótulos; 1 = um certo; 0 = nenhuma.
- **EX009 — Eixos de teste.** Escreva cinco eixos físicos de teste para o TrackEye. Rubrica: 3 = cinco eixos mensuráveis com faixas; 2 = cinco sem faixas; 1 = dois ou três; 0 = nenhuma.

### Síntese

A física determina quais entradas um componente de IA de fato recebe. Engenheiros especificam condições físicas, testam deslocamentos naturais e incluem adversários físicos no modelo de ameaças.

### Continue estudando — capítulo 03 de 50

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever programas Python pequenos e corretos com funções, laços e estruturas de dados; (2) tratar entradas não confiáveis com segurança; (3) testar código com asserções; e (4) ler os laboratórios do livro e modificá-los.

### 4.1 Programas como instruções precisas

Um programa diz exatamente o que o computador faz. Variáveis guardam valores; funções empacotam passos; laços repetem; condicionais escolhem. Código legível usa nomes claros e funções pequenas. Os laboratórios deste livro usam apenas a biblioteca padrão do Python, para rodarem em qualquer lugar. A precisão corta dos dois lados: o computador faz o que o código diz, não o que o autor quis dizer. Um laço que para um item antes ou uma condição escrita com 'or' em vez de 'and' produz resultados errados sem nenhum aviso. Sam lê cada laboratório linha por linha antes de executá-lo e prevê a saída, de modo que uma surpresa no resultado impresso aponta uma lacuna no seu entendimento.

### 4.2 Estruturas de dados

Listas guardam sequências; dicionários associam chaves a valores; conjuntos guardam itens únicos. Um inventário de modelos é naturalmente uma lista de dicionários; uma lista de permissões de uma política é naturalmente um conjunto. Escolher a estrutura certa deixa o código mais curto e mais seguro: a pertinência a um conjunto é um teste claro e rápido para "esta ferramenta é permitida?". Uma lista também funcionaria como lista de permissões, mas verificar a pertinência nela significa percorrer todos os itens, e duplicatas podem entrar sem que ninguém perceba. A estrutura errada também pode esconder um bug de segurança: se as ferramentas permitidas forem guardadas como uma única string separada por vírgulas, uma verificação como 'search' in allowed aceitaria também uma ferramenta chamada 'research'.

### 4.3 Entrada não confiável

Quaisquer dados de fora do seu programa — arquivos, mensagens de rede, saídas de modelos — são não confiáveis. Nunca os passe para `eval`, comandos de shell ou consultas a bancos de dados sem validação estrita. Isso se aplica à IA: o OWASP LLM 2025 lista o *tratamento inadequado de saídas* (LLM05) porque aplicações frequentemente executam ou renderizam diretamente a saída do modelo. Faça o parsing com parsers estritos (por exemplo, `json.loads`), valide tipos e faixas e rejeite campos desconhecidos. Rejeitar campos desconhecidos importa porque sistemas a jusante podem agir sobre campos que o validador nunca examinou. Um parser estrito os recusa de imediato.

### 4.4 Erros como informação

Quando o código falha, ele deve falhar *fechado* e explicar o motivo. Um parser que descarta silenciosamente um campo desconhecido pode deixar passar um campo que o sistema a jusante respeita; um parser que rejeita o objeto inteiro com uma mensagem clara é mais seguro e mais fácil de depurar. Registre a rejeição com contexto suficiente para investigar (hora, origem, motivo), mas sem copiar conteúdo sensível para os logs. Exceções são o mecanismo normal do Python: lance `ValueError` com uma mensagem e deixe quem chamou decidir se tenta de novo, consulta um humano ou para.

### 4.5 Testes

Um `assert` declara o que precisa ser verdade. Testes unitários chamam funções com entradas escolhidas e conferem as saídas, inclusive casos-limite (listas vazias, valores muito grandes, texto malformado). Testes tornam seguras as mudanças futuras. Para código de segurança, os testes mais valiosos são os que deveriam falhar: uma ordem de serviço com um campo extra, uma prioridade escrita de outro jeito, um identificador de ativo contendo pontuação. Cada rejeição esperada é escrita como teste, de modo que uma mudança futura que afrouxe a validação quebre o build em vez de chegar à produção. Sam guarda como caso de teste permanente toda entrada malformada que já causou um problema.

### 4.6 Exemplo resolvido (caso sintético da NRS)

Sam escreve uma função que faz o parsing da ordem de serviço proposta pelo Wrench (JSON) antes que ela chegue ao sistema de ordens de serviço. O programa abaixo imprime a ordem válida e depois `rejected: bad asset id`. A saída do modelo é tratada como dado a validar, nunca como código. O identificador do ativo é rejeitado porque o ponto e vírgula e o espaço falham na verificação alfanumérica, então um texto que parece um comando de shell nunca chega ao sistema de ordens de serviço. A função nunca exige um resumo, então uma ordem sem resumo passaria; Sam acrescenta essa verificação em seguida. Na produção, Sam substitui os asserts por exceções explícitas, pelo motivo dado entre os erros abaixo.

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

### 4.7 Erros e limites

Três erros são comuns: executar a saída do modelo como código ou comandos de shell; uma validação que só confere os caminhos felizes; e usar asserts como única verificação em código de produção (eles podem ser desativados com `python -O`; ali, use exceções explícitas). Cada erro tem um sinal reconhecível na revisão de código. Chamadas a eval, exec ou subprocess com uma string montada a partir da saída do modelo são a primeira coisa a procurar. Validadores sem testes para entradas rejeitadas provavelmente nunca foram experimentados com dados ruins. Asserts que protegem condições de segurança devem virar if-statements que lançam uma exceção nomeada, porque uma execução otimizada na produção pularia a verificação por completo, sem nenhuma mensagem.

### Exercícios

- **EX010 — Lista de permissões.** Escreva uma função `allowed(tool)` usando um conjunto de ferramentas permitidas. Rubrica: 3 = pertinência a conjunto correta, com teste; 2 = funciona sem teste; 1 = usa lista, com erros; 0 = nenhuma.
- **EX011 — Tratamento de saídas.** Por que passar a saída do modelo para `eval` é perigoso? Cite a entrada do OWASP. Rubrica: 3 = execução arbitrária de código a partir de texto influenciado pelo atacante; LLM05; 2 = uma parte; 1 = vago; 0 = errado.
- **EX012 — Casos-limite.** Liste quatro testes de casos-limite para `parse_order`. Rubrica: 3 = quatro pertinentes (vazio, campo extra, tipo errado, JSON inválido, resumo longo); 2 = três; 1 = um ou dois; 0 = nenhuma.

### Síntese

Programar para a segurança de IA começa com um hábito: tratar tudo o que vem de fora — inclusive a saída do modelo — como dado não confiável, validá-lo estritamente e testar os limites.

### Continue estudando — capítulo 04 de 50

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever documentos técnicos claros (requisitos, notas de projeto, relatórios de teste, resumos de incidentes); (2) comunicar incerteza e risco com honestidade; (3) adaptar mensagens a engenheiros, gestores e reguladores; e (4) documentar componentes de IA com model cards e datasheets.

### 5.1 Os documentos do engenheiro

Requisitos dizem o que um sistema deve fazer e o que não deve fazer. Notas de projeto explicam escolhas e alternativas. Relatórios de teste dizem o que foi testado, como, os resultados e os limites. Resumos de incidentes dizem o que aconteceu, o impacto, a causa e as ações. Cada um tem um leitor com uma decisão a tomar; escreva para essa decisão. Escrever para uma decisão muda o que vem primeiro. Um gestor que decide se implanta o TrackEye precisa do risco e das opções na primeira página; um testador que vai repetir a avaliação precisa do método completo. Sam abre cada documento com uma frase que nomeia o leitor e a decisão que o documento apoia, o que também lhe mostra o que pode ficar de fora.

### 5.2 Comunicando incerteza

Nunca escreva "o modelo é seguro". Escreva "nas condições testadas (lista), a taxa de falsos negativos foi de 2.1% (intervalo de 95% 1.6–2.7%); entre as condições não testadas estão neve intensa e marcações deliberadas". Números com intervalos e condições explícitas deixam os leitores julgarem por si mesmos. Separe *fatos* (medidos), *avaliações* (seu julgamento) e *recomendações*. O intervalo diz ao leitor quanto o número poderia variar se o teste fosse repetido com dados novos. Listar as condições não testadas é igualmente importante, porque, do contrário, os leitores supõem que o resultado as cobre. Manter fatos, avaliações e recomendações em parágrafos separados permite que um leitor que discorda de um julgamento continue confiando nas medições em que ele se apoia.

### 5.3 Documentando componentes de IA

Model cards (Mitchell et al., arXiv:1810.03993) descrevem o uso pretendido de um modelo, os usos fora de escopo, os dados de avaliação, as métricas desagregadas por fatores relevantes e as considerações éticas. Datasheets para conjuntos de dados (Gebru et al., arXiv:1803.09010) descrevem motivação, composição, coleta, pré-processamento, usos, distribuição e manutenção. Ambos tornam visíveis suposições ocultas para engenheiros e auditores a jusante. No TrackEye, o datasheet registra que a maioria das imagens de treinamento veio de viagens diurnas em via de bitola padrão, o que explica as fraquezas posteriores na madrugada e em tipos de trilho desconhecidos. Uma equipe que planeje reutilizar o modelo pode ver essa limitação antes de implantá-lo, em vez de descobri-la em serviço.

### 5.4 Públicos

Engenheiros precisam de interfaces precisas e modos de falha. Gestores precisam de risco, custo e opções. Reguladores e auditores precisam de evidências rastreáveis ligadas aos requisitos. O mesmo fato pode aparecer em três formas. O problema dos falsos negativos na madrugada mostra as três. Para engenheiros: os falsos negativos sobem para 9% entre 05:00 e 07:00 a 60–80 km/h, com o conjunto de teste nomeado. Para gestores: as inspeções de madrugada deixam passar mais defeitos, uma correção está em andamento e uma verificação manual provisória está em vigor. Para auditores: o achado, o requisito que ele afeta, o registro do teste e a ação corretiva, cada um com um identificador.

### 5.5 Estrutura e rastreabilidade

Numere os requisitos (REQ-SEC-012) e faça referência a eles nas notas de projeto e nos relatórios de teste, para que qualquer pessoa possa rastrear um requisito até sua evidência. Use tabelas para condições e resultados, figuras para tendências e parágrafos curtos para o raciocínio. Ponha a conclusão primeiro e o método depois para leitores que decidem; inverta a ordem para revisores que precisam conferir o método. Versione cada documento e mantenha um registro de mudanças: uma avaliação que era verdadeira para o modelo v1.3 pode ser falsa para o v1.4. Uma entrada do registro de mudanças diz o que mudou, por quê e quais resultados ela invalida.

### 5.6 Exemplo resolvido (caso sintético da NRS)

O primeiro relatório de teste do TrackEye escrito por Sam dizia "funciona bem na maioria das condições". O supervisor o devolveu. A versão revisada tinha um resumo de um parágrafo para gestores ("os falsos negativos de madrugada são 4.5× os diurnos; correção em andamento; provisoriamente: segunda verificação visual de madrugada"), uma tabela por condição com intervalos para engenheiros e uma seção de model card declarando os usos fora de escopo (não validado para trilhos de bonde nem para neve). O valor de 4.5× é a taxa de falsos negativos de madrugada, 9%, dividida pela diurna, 2%. A frase original não era falsa, mas não dava aos leitores nada sobre o que agir. A revisão permite que cada leitor encontre o que precisa sem ler o resto.

### 5.7 Erros e limites

Três erros são comuns: afirmações absolutas ("seguro", "safe") sem condições; misturar medição e opinião; e model cards escritos uma vez e nunca atualizados. Afirmações absolutas são tentadoras porque soam confiantes, mas um único contraexemplo as desfaz e, com elas, a confiança do leitor. Misturar medição e opinião torna impossível contestar uma sem a outra. Um model card que descreve a versão 1.3 anexado à versão 1.5 é pior do que nenhum, porque os leitores confiam nele; Sam vincula cada card a uma versão do modelo e o atualiza na mesma mudança que libera o modelo.

### Exercícios

- **EX013 — Reescrita.** Reescreva "o Wrench está a salvo de injeção de prompt" como uma afirmação honesta. Rubrica: 3 = condições, métrica com intervalo, áreas não testadas; 2 = duas; 1 = uma; 0 = sem mudança.
- **EX014 — Model card.** Liste cinco seções de um model card para o TrackEye. Rubrica: 3 = cinco pertinentes; 2 = quatro; 1 = duas; 0 = nenhuma.
- **EX015 — Públicos.** Escreva o mesmo achado da madrugada para um gestor e para um auditor. Rubrica: 3 = gestor: risco/ação; auditor: evidência e vínculo com o requisito; 2 = um bom; 1 = vago; 0 = nenhuma.

### Síntese

Uma comunicação clara e honesta — condições, intervalos, fatos separados das recomendações e modelos e conjuntos de dados documentados — é o modo como a evidência de engenharia chega a quem decide.

### Continue estudando — capítulo 05 de 50

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) calcular derivadas parciais e gradientes de funções de várias variáveis; (2) usar a regra da cadeia em composições (a base da retropropagação); (3) aplicar aproximações de Taylor para estimar mudanças na saída; e (4) relacionar normas de gradiente e constantes de Lipschitz à robustez.

### 6.1 Derivadas parciais e gradientes

Para f(x₁, …, xₙ), a derivada parcial ∂f/∂xᵢ mantém as outras variáveis fixas. O gradiente ∇f as reúne num vetor que aponta na direção de maior crescimento. Para uma pontuação linear s = w·x + b, ∇ₓ s = w: os pesos *são* o gradiente em relação à entrada, e é por isso que modelos lineares são fáceis de atacar ao longo de sign(w). Num modelo linear, a direção de ataque fica, portanto, visível nos próprios pesos. Quem os obtiver, por exemplo a partir de um arquivo de modelo vazado, sabe exatamente quais atributos empurrar e em que direção. Em modelos não lineares o gradiente muda de entrada para entrada, mas o mesmo raciocínio vale localmente em torno de cada uma.

### 6.2 A regra da cadeia multivariada

Redes neurais são composições f = f_L ∘ … ∘ f₁. A regra da cadeia multiplica matrizes jacobianas camada por camada; a retropropagação calcula esse produto de forma eficiente, da saída para trás. O mesmo algoritmo dá gradientes em relação às entradas, que os ataques de caixa-branca usam. A retropropagação economiza trabalho ao reutilizar produtos intermediários, de modo que calcular o gradiente para todas as entradas custa mais ou menos o mesmo que uma passada direta. Essa eficiência é o motivo de os ataques de caixa-branca serem baratos: um atacante com o arquivo do modelo consegue calcular em milissegundos a direção mais danosa para qualquer entrada. Proteger os pesos do modelo é, portanto, parte da defesa contra evasão, e não apenas uma questão de propriedade intelectual.

### 6.3 Aproximação de Taylor e mudança no pior caso

Taylor de primeira ordem: f(x + δ) ≈ f(x) + ∇f(x)·δ. Se um atacante pode mudar cada atributo em no máximo ε (um orçamento L∞), a maior mudança de primeira ordem é ε·‖∇f(x)‖₁, atingida com δ = ε·sign(∇f(x)) — exatamente o passo do FGSM (Goodfellow et al., arXiv:1412.6572). Sob um orçamento L2, a pior mudança é ε·‖∇f(x)‖₂. As normas importam: um gradiente com muitas componentes pequenas ainda pode ter uma norma L1 grande em altas dimensões, o que é uma das explicações para a vulnerabilidade adversarial de modelos de alta dimensão. A aproximação só é precisa para ε pequeno, então engenheiros a usam como estimativa rápida e depois testam o modelo real com perturbações efetivas.

### 6.4 Constantes de Lipschitz

Uma função é L-Lipschitz se |f(x) − f(y)| ≤ L‖x − y‖. Se a margem de um classificador em x é m e sua pontuação é L-Lipschitz, nenhuma perturbação menor que m/L consegue inverter a decisão — um *certificado*. Calcular um L justo para redes profundas é difícil, e é por isso que métodos certificados como o randomized smoothing (Cohen et al., arXiv:1902.02918) usam argumentos probabilísticos. Um certificado é mais forte do que um resultado de teste: garante que nenhum ataque dentro do raio pode ter sucesso, por mais engenhoso que seja. Limites folgados ainda dão certificados válidos, mas o raio garantido pode ficar pequeno demais para importar.

### 6.5 Exemplo resolvido (caso sintético da NRS)

A pontuação de anomalia de rolamentos do Pulse é s = 0.9·t + 0.4·v − 0.2·h + c (temperatura, vibração, umidade, normalizadas). Com ε = 0.1 por atributo, a pior mudança de primeira ordem é 0.1 × (0.9 + 0.4 + 0.2) = 0.15. Sam compara isso com a margem típica (0.3) e conclui que um atacante que falsifica sensores, limitado a ±0.1, não consegue esconder um rolamento claramente quente, mas consegue esconder os limítrofes. Os pesos dão diretamente a pior direção: aumentar a umidade e reduzir a temperatura e a vibração, cada uma em 0.1. Uma margem de 0.3 é o dobro da pior mudança, então rolamentos claramente quentes continuam sinalizados, mas qualquer rolamento cuja pontuação esteja a menos de 0.15 do limiar poderia ser escondido. Sam registra essa faixa como risco residual e sugere cruzar as leituras limítrofes com um segundo sensor.

### 6.6 Erros e limites

Três erros são comuns: usar estimativas de primeira ordem longe do ponto em que elas são precisas; confundir orçamentos L1, L2 e L∞; e tratar um gradiente local como limite global. Estimativas de primeira ordem funcionam perto do ponto medido e ficam pouco confiáveis para mudanças maiores, em que a curvatura domina. Misturar normas produz limites errados por um fator que cresce com o número de atributos. Um gradiente local nada diz sobre entradas distantes, por isso Sam sempre combina as estimativas com testes usando perturbações reais e declara a norma do orçamento em todo resultado que relata.

### Exercícios

- **EX016 — Gradiente.** Calcule ∇f para f(x, y) = x²y + 3y. Rubrica: 3 = (2xy, x² + 3); 2 = uma componente; 1 = tentativa; 0 = nenhuma.
- **EX017 — Pior caso.** Para s = 2x₁ − x₂ + 0.5x₃ e ε = 0.2 (L∞), dê o aumento de primeira ordem no pior caso e δ. Rubrica: 3 = 0.7, δ = (0.2, −0.2, 0.2); 2 = um; 1 = método; 0 = nenhuma.
- **EX018 — Certificado.** Uma pontuação tem margem 0.6 e constante de Lipschitz 3 (L2). Que tamanho de perturbação é certificado como seguro? Rubrica: 3 = < 0.2 em L2, com raciocínio; 2 = só o número; 1 = norma errada; 0 = nenhuma.

### Síntese

Gradientes e normas transformam "mudança pequena" num número. Eles explicam por que os ataques funcionam, como os piores casos são limitados e por que certificados são possíveis, mas difíceis, para modelos profundos.

### Continue estudando — capítulo 06 de 50

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) aplicar a regra de Bayes a problemas de detecção; (2) explicar as taxas de base e por que eventos raros dominam a precisão dos alertas; (3) estimar taxas com intervalos de confiança; e (4) desenhar avaliações com amostras suficientes.

### 7.1 Probabilidade condicional e Bayes

P(A | B) = P(B | A) P(A) / P(B). Para um detector de prompts maliciosos, a taxa de verdadeiros positivos é P(alerta | malicioso) e a taxa de falsos positivos é P(alerta | benigno). O que importa para os operadores é a *precisão*, P(malicioso | alerta), que depende fortemente da taxa de base P(malicioso). As duas taxas descrevem o detector e ficam mais ou menos fixas; a precisão descreve o detector num fluxo de tráfego específico e muda sempre que a composição muda. Sam escreve os três números em todo relatório de detector, porque operadores que leem só a taxa de verdadeiros positivos tendem a tratar todo alerta como ataque.

### 7.2 O efeito da taxa de base

O laboratório calcula a precisão de três detectores em três prevalências. Um detector com TPR de 95% e FPR de 5% parece bom, mas, se só 1 em 1,000 prompts for malicioso, menos de 2% dos seus alertas são reais. Arp et al. (arXiv:2010.09470) listam a falácia da taxa de base entre as armadilhas comuns do aprendizado de máquina em segurança. Ler a tabela linha por linha mostra que cortar falsos positivos faz mais do que aumentar a detecção. Com prevalência de 0.001, o terceiro detector pega menos ataques que o primeiro, mas quase metade dos seus alertas é real, contra menos de 2%, e ele gera 18 alertas por 10,000 prompts em vez de 509.

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

Saída esperada:

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

### 7.3 Estimando taxas

Uma taxa observada k/n tem incerteza. O intervalo de escore de Wilson é confiável mesmo para n pequeno ou taxas perto de 0 ou de 1. Relate intervalos e dimensione os estudos para que os intervalos sejam estreitos o bastante para a decisão: n ≈ z² p(1 − p)/h² para uma semiamplitude h. O intervalo de Wilson fica dentro de 0 e 1 e é quase correto mesmo quando se observam poucas falhas, o que importa porque bons sistemas produzem poucas. Para uma taxa em torno de 5% e semiamplitude de 1 ponto percentual com 95% de confiança, a fórmula dá cerca de 1.96² × 0.05 × 0.95 / 0.01², aproximadamente 1,800 itens de teste. Sam faz essa conta antes de coletar dados, já que um estudo pequeno demais para resolver a questão desperdiça o tempo de todos.

### 7.4 Distribuições e independência

Modelos binomiais contam sucessos em tentativas independentes. Muitas avaliações de segurança violam a independência: prompts gerados a partir de um mesmo modelo de texto são correlacionados, então o tamanho efetivo da amostra é menor. Agrupe por modelo de texto e reamostre os grupos (um *cluster bootstrap*) ao estimar intervalos. Suponha que 1,000 prompts de teste venham de 20 modelos de texto com 50 redações cada. Se um filtro falha num modelo, provavelmente falha na maioria das suas redações, então a avaliação tem mais perto de 20 unidades independentes do que de 1,000. Tratá-las como 1,000 deixa o intervalo estreito demais. Reamostrar modelos inteiros dá uma largura honesta e também mostra quais modelos provocam as falhas.

### 7.5 Comparando dois sistemas

Para decidir se um filtro novo é melhor que o antigo, execute os dois sobre os *mesmos* itens e analise as diferenças pareadas; a dificuldade dos itens então se cancela. Um bootstrap pareado — reamostrar itens, recalcular a diferença, tomar percentis — dá um intervalo para a melhoria. Se o intervalo inclui zero, os dados não mostram melhoria, por mais atraente que seja a estimativa pontual. O pareamento remove o ruído da dificuldade dos itens: um prompt excepcionalmente difícil conta contra os dois filtros, então deixa de obscurecer a diferença entre eles.

### 7.6 Exemplo resolvido (caso sintético da NRS)

O detector de injeção do Wrench teve TPR de 95% e FPR de 1% nos testes. Sam estimou que talvez 1 em 1,000 boletins de fornecedores chegaria a conter uma tentativa de injeção. Pelo laboratório, a precisão seria de cerca de 8.7%, com 109 alertas por 10,000 boletins — em sua maioria alarmes falsos. Sam recomendou encaminhar os alertas para uma fila de revisão leve em vez de bloquear, e combinar a detecção com limites de privilégio, para que ataques não detectados tenham impacto limitado. O valor de 1 em 1,000 é ele próprio uma estimativa, então Sam também lê a linha de 1 em 100 do laboratório, onde a precisão sobe para 0.490. De qualquer forma, bloquear todo boletim sinalizado bloquearia sobretudo boletins legítimos. Uma fila de revisão mantém os técnicos informados, e os limites de privilégio fazem com que a decisão não dependa de o detector acertar.

### 7.7 Erros e limites

Três erros são comuns: citar a acurácia em vez da precisão em taxas de base realistas; tratar amostras correlacionadas como independentes; e estimativas pontuais sem intervalos. A acurácia engana em taxas de base baixas: um detector que nunca alerta tem 99.9% de acurácia quando um prompt em mil é malicioso. Amostras correlacionadas inflam a confiança, como quando muitos prompts compartilham um modelo de texto. Estimativas pontuais sem intervalos escondem quão pouco um teste pequeno consegue mostrar. A lista de revisão de Sam faz três perguntas a qualquer métrica: em que taxa de base, contada sobre quais unidades e com que intervalo.

### Exercícios

- **EX019 — Precisão.** Com TPR 0.90, FPR 0.02 e prevalência 0.005, calcule a precisão. Rubrica: 3 = 0.0045/(0.0045 + 0.0199) ≈ 0.184; 2 = deslize; 1 = método; 0 = nenhuma.
- **EX020 — Leitura do laboratório.** Qual detector do laboratório dá precisão acima de 0.4 com prevalência 0.001, e a que custo? Rubrica: 3 = TPR 0.80/FPR 0.001: 0.445, TPR menor; 2 = só a linha; 1 = vago; 0 = errado.
- **EX021 — Agrupamento.** Por que gerar 500 prompts a partir de 5 modelos de texto superestima o tamanho da amostra? Rubrica: 3 = correlação dentro do modelo; n efetivo mais perto de 5 grupos; usar cluster bootstrap; 2 = parcial; 1 = vago; 0 = errado.

### Síntese

A probabilidade diz aos engenheiros o que um alerta realmente significa. Taxas de base, intervalos honestos e as unidades amostrais corretas decidem se um detector é útil na operação.

### Continue estudando — capítulo 07 de 50

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) descrever CPUs, hierarquias de memória, GPUs e aceleradores usados em aprendizado de máquina; (2) explicar os formatos numéricos e seu efeito sobre o comportamento do modelo; (3) identificar superfícies de ataque arquiteturais (isolamento de memória, canais laterais, firmware); e (4) raciocinar sobre execução confiável para cargas de trabalho de IA.

### 8.1 Processadores e aceleradores

CPUs executam instruções gerais com caches profundos. GPUs e aceleradores de IA executam milhares de operações simples em paralelo, o ideal para multiplicação de matrizes. Os modelos transitam entre a memória do host e a memória do dispositivo; na nuvem, os dados na memória do dispositivo podem ser compartilhados entre processos ou clientes, então o isolamento importa. As cópias são a preocupação de segurança: pesos carregados numa GPU, entradas mantidas num buffer compartilhado e resultados aguardando retorno existem por um instante em lugares que outro cliente ou um driver descuidado poderia ler. Provedores de nuvem isolam os clientes, mas engenheiros ainda perguntam se a memória do dispositivo é limpa entre tarefas e quem pode vê-la, e registram as respostas no modelo de ameaças da implantação.

### 8.2 Formatos numéricos

O treinamento costuma usar ponto flutuante de 32 ou 16 bits; a inferência pode usar inteiros de 8 bits (quantização). Uma precisão menor muda levemente as saídas e pode mudar decisões perto das fronteiras. Avaliações de segurança devem usar a precisão *implantada*: um ataque ou uma defesa medidos em 32 bits podem se comportar de outro modo em 8 bits, e vice-versa. A quantização leva cada valor ao mais próximo de um pequeno conjunto de níveis, então entradas próximas do limiar de decisão podem passar para o outro lado. Gradientes calculados numa cópia de 32 bits podem não corresponder ao comportamento do modelo de 8 bits, o que pode fazer os ataques parecerem mais fortes ou mais fracos do que são em serviço.

### 8.3 Superfícies de ataque arquiteturais

Bugs de segurança de memória no código que serve o modelo podem expor pesos ou entradas. Caches compartilhados e o tempo de execução podem vazar informação entre processos (canais laterais). Falhas de hardware — inclusive as induzidas deliberadamente, como inversões de bits ao estilo rowhammer — podem corromper pesos; pesquisas mostraram que um pequeno número de bits invertidos nos parâmetros de uma rede pode degradá-la ou redirecioná-la fortemente. Firmware e drivers fazem parte da base de computação confiável. Para um engenheiro, cada item sugere um controle: linguagens com segurança de memória ou revisão cuidadosa do código de serviço, isolamento entre clientes, memória com correção de erros e verificações de integridade dos pesos carregados. Calcular o hash do arquivo de pesos antes de carregá-lo detecta mudanças em disco, mas não bits invertidos na memória depois disso, então implantações críticas também comparam, em intervalos, as saídas sobre um conjunto fixo de verificação.

### 8.4 Execução confiável e atestação

Ambientes de execução confiável (TEEs) e GPUs de computação confidencial buscam proteger código e dados em uso contra o operador do host, e a *atestação remota* permite a um cliente verificar que código está sendo executado. Eles reduzem alguns riscos (um operador de nuvem curioso), mas não outros (um servidor de modelo vulnerável dentro do enclave, injeção de prompt). A atestação responde a uma pergunta estreita: este é o código esperado, em hardware genuíno? Ela nada diz sobre se esse código é seguro. Engenheiros tratam, portanto, um TEE como uma camada que protege contra um operador curioso e mantêm validação de entradas, limites de privilégio e monitoramento para ataques que chegam pela interface normal do modelo.

### 8.5 Exemplo resolvido (caso sintético da NRS)

O TrackEye roda num computador de borda no trem de inspeção, com um modelo quantizado de 8 bits. Sam descobriu que os testes de robustez tinham sido feitos no laboratório com o modelo de 32 bits; repeti-los na build implantada de 8 bits mudou os falsos negativos de madrugada de 9.0% para 9.6%. Sam acrescentou "avaliar no artefato e no hardware implantados" como requisito e anotou que a porta de manutenção do computador de borda dá acesso físico ao firmware — um item do modelo de ameaças. Uma alta de 0.6 ponto percentual é pequena, mas mostra que o resultado do laboratório não descrevia o sistema que de fato roda no trem. O novo requisito faz com que todo número de robustez futuro informe o hash do artefato e o hardware em que foi medido.

### 8.6 Erros e limites

Três erros são comuns: avaliar uma precisão numérica diferente da implantada; supor que TEEs resolvem ataques no nível da aplicação; e ignorar o firmware e as portas físicas de manutenção. Esses erros têm uma causa comum: avaliar um sistema idealizado em vez do implantado. A precisão usada nos testes é fácil de conferir contra a build. As alegações sobre TEEs devem ser lidas pelo que excluem. Portas de manutenção costumam ficar habilitadas por conveniência; a lista de verificação de Sam pergunta, para cada porta, se ela é necessária em serviço, quem pode alcançá-la e se seu uso é registrado.

### Exercícios

- **EX022 — Precisão.** Por que a robustez precisa ser testada no modelo quantizado implantado? Rubrica: 3 = a quantização muda as saídas perto das fronteiras; os resultados podem diferir; 2 = parcial; 1 = vago; 0 = errado.
- **EX023 — Limites do TEE.** Cite uma ameaça que um TEE mitiga e uma que ele não mitiga num serviço de LLM. Rubrica: 3 = operador do host lendo dados vs. injeção de prompt/bugs do servidor; 2 = uma; 1 = vago; 0 = errado.
- **EX024 — Inversões de bits.** Explique por que verificações de integridade dos pesos no carregamento não resolvem por completo os ataques por falhas. Rubrica: 3 = as falhas podem ocorrer na memória depois do carregamento; são precisos verificações em tempo de execução/ECC/redundância; 2 = parcial; 1 = vago; 0 = errado.

### Síntese

A IA roda em hardware real, com precisão finita, recursos compartilhados e firmware. Engenheiros testam o artefato implantado na plataforma implantada e incluem ameaças no nível da arquitetura no modelo.

### Continue estudando — capítulo 08 de 50

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 (rascunho) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar programas maiores em módulos com interfaces claras; (2) gerenciar dependências e seus riscos de cadeia de suprimentos; (3) escrever testes, inclusive testes baseados em propriedades e de regressão; e (4) construir um pequeno harness de avaliação para um componente de IA.

### 9.1 Módulos e interfaces

Programas grandes são divididos em módulos com interfaces estreitas. Em sistemas de IA, separe *carregamento de dados*, *inferência do modelo*, *aplicação de políticas* e *execução de ferramentas*. O módulo de políticas deve ser pequeno, revisável e independente do modelo: ele decide o que é permitido independentemente do que o modelo diga. Essa é a forma em software do menor privilégio. Se a política depender do julgamento do próprio modelo, uma injeção de prompt bem-sucedida também derrota a política. Mantê-la em código separado significa que ela aplica as mesmas regras, seja qual for a forma como o modelo foi persuadido. Interfaces estreitas também tornam as revisões possíveis: um revisor consegue ler com cuidado um módulo de 80 linhas, mas não um sistema em que as verificações estão espalhadas por prompts e scripts.

### 9.2 Dependências e cadeia de suprimentos

Projetos de IA puxam muitas bibliotecas e arquivos de modelo. Fixe versões, verifique hashes e prefira serialização segura: carregar arquivos *pickle* não confiáveis em Python pode executar código arbitrário, e é por isso que formatos feitos para guardar apenas tensores são preferidos para os pesos dos modelos. O OWASP LLM 2025 lista *cadeia de suprimentos* (LLM03) e *envenenamento de dados e de modelos* (LLM04). Gu et al. (arXiv:1708.06733) mostraram que um modelo com backdoor obtido de terceiros pode se comportar normalmente em entradas limpas. Fixar versões impede que uma atualização mude o comportamento em silêncio, e as verificações de hash impedem que um arquivo trocado seja carregado. Um modelo com backdoor é mais difícil: pode passar em todos os testes comuns, porque seu comportamento nocivo só aparece com um gatilho específico. Engenheiros reduzem esse risco preferindo fontes com proveniência publicada, registrando de onde veio cada modelo e testando comportamentos inesperados em entradas fora da distribuição habitual.

### 9.3 Testes além de exemplos

Testes de regressão congelam um comportamento sabidamente bom, para que mudanças não possam quebrá-lo em silêncio. Testes baseados em propriedades geram muitas entradas e conferem invariantes ("a política nunca permite `create_work_order` sem um indicador de confirmação"). Em componentes de IA, um *conjunto de referência* (golden set) de entradas com saídas esperadas detecta deriva de comportamento quando um modelo ou um prompt muda. Cada tipo pega algo diferente. Testes de regressão impedem que bugs antigos voltem, testes de propriedades encontram entradas em que ninguém pensou e conjuntos de referência mostram quando uma edição de prompt ou uma atualização do modelo muda respostas que antes estavam certas. Conjuntos de referência exigem cuidado, porque as saídas dos modelos variam; Sam confere propriedades das respostas, como qual ferramenta foi proposta, e não a redação exata.

### 9.4 Um harness de avaliação

Um harness carrega um conjunto de teste, executa o componente, registra as saídas e calcula métricas com intervalos. Ele deve ser determinístico dada uma semente, registrar versões (hash do modelo, versão do prompt, commit do código) e manter os dados de teste separados dos dados de desenvolvimento. Sem versões registradas, um resultado não pode ser vinculado ao sistema que descreve, e uma regressão posterior não pode ser rastreada. O determinismo torna as reexecuções comparáveis, de modo que uma mudança nas métricas reflita uma mudança no sistema e não na amostragem aleatória. Manter teste e desenvolvimento separados impede que o sistema seja ajustado com os próprios exemplos usados para julgá-lo, o que faria os resultados parecerem melhores do que são.

### 9.5 Exemplo resolvido (caso sintético da NRS)

Sam reestruturou o Wrench em quatro módulos. O módulo `policy` (80 linhas) confere cada chamada de ferramenta proposta contra o papel do usuário e exige um token de confirmação para ordens de serviço. Um teste baseado em propriedades gerou 10,000 requisições aleatórias de chamada de ferramenta e confirmou que nenhuma passou sem token. A revisão de dependências encontrou um script de conversão de modelos que carregava arquivos pickle de uma pasta compartilhada; Sam o substituiu por um carregador de formato só de tensores e acrescentou verificação de hash. O teste de propriedades amostra o espaço de chamadas de ferramenta de forma muito mais ampla do que casos escritos à mão conseguiriam, embora não prove que não existe nenhuma chamada insegura.

### 9.6 Erros e limites

Três erros são comuns: lógica de política embutida em prompts em vez de código; dependências sem versão fixada e arquivos de modelo não verificados; e conjuntos de referência reutilizados para ajuste (eles deixam de detectar deriva). Uma política escrita num prompt pode ser contornada pela entrada do modelo, enquanto uma política em código não pode. Dependências sem versão fixada tornam sem sentido hoje os resultados dos testes de ontem. Um conjunto de referência usado durante o ajuste deixa aos poucos de ser uma verificação independente, porque o sistema foi adaptado a ele. Sam mantém um segundo conjunto, intocado, para as decisões de liberação e o renova quando o uso do sistema muda.

### Exercícios

- **EX025 — Divisão em módulos.** Proponha uma estrutura de módulos para um assistente de LLM com ferramentas e diga qual módulo aplica a segurança. Rubrica: 3 = dados, inferência, política, ferramentas; política fora do modelo; 2 = parcial; 1 = vago; 0 = nenhuma.
- **EX026 — Pickle.** Por que carregar um modelo não confiável em formato pickle é perigoso, e qual é a alternativa? Rubrica: 3 = execução arbitrária de código no carregamento; formato só de tensores mais verificação de hash; 2 = uma parte; 1 = vago; 0 = errado.
- **EX027 — Teste de propriedades.** Escreva em uma frase o invariante que Sam testou e mais um invariante. Rubrica: 3 = ambos precisos; 2 = um; 1 = vago; 0 = nenhuma.

### Síntese

Uma boa estrutura coloca as decisões de segurança em código pequeno e testável fora do modelo; dependências e testes disciplinados mantêm essa estrutura confiável à medida que o sistema cresce.

### Continue estudando — capítulo 09 de 50

[← Capítulo 08 (rascunho)](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 (rascunho) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar a ética profissional da engenharia a sistemas de IA; (2) distinguir safety (dano acidental) de security (dano intencional) e mostrar como elas interagem; (3) aplicar regras para testes autorizados e divulgação responsável; e (4) reconhecer deveres legais, como os previstos no AI Act da UE para sistemas de alto risco.

### 10.1 Deveres profissionais

Os códigos de ética da engenharia colocam em primeiro lugar a segurança, a saúde e o bem-estar do público, exigem honestidade sobre capacidades e limites e exigem competência. Para a IA, isso significa não exagerar o que um modelo consegue fazer, documentar os modos de falha conhecidos e recusar a implantação quando o risco é inaceitável. Esses deveres valem nos momentos comuns, não só nos dramáticos: um slide que arredonda uma taxa de 9% de defeitos perdidos na madrugada para 'cerca de 2%', uma demonstração que esconde as condições em que o modelo falha, ou um prazo que tenta a equipe a pular a revisão de segurança. A competência inclui conhecer os limites da própria especialidade e pedir ajuda, por exemplo a um engenheiro de segurança ferroviária, quando uma decisão fica fora deles.

### 10.2 Safety e security

A engenharia de safety trata de falhas acidentais; a security trata de ataques deliberados. Na IA elas interagem: uma entrada adversarial pode causar uma falha de safety (um defeito no trilho que passa despercebido), e um mecanismo de safety (um recurso à inspeção manual) pode ser abusado para causar negação de serviço. O NIST AI RMF (AI 100-1) lista *safe* e *secure and resilient* entre as características de uma IA confiável e enfatiza geri-las em conjunto. Geri-las em conjunto significa uma única análise de perigos que pergunta tanto o que pode falhar quanto o que alguém pode fazer falhar. Recorrer à inspeção manual é seguro contra acidentes, mas um atacante que consiga acioná-lo repetidamente poderia esgotar os inspetores e atrasar o trabalho real.

### 10.3 Testes autorizados e divulgação

Teste apenas sistemas que sejam seus ou que você tenha permissão por escrito para testar, dentro de um escopo e de um prazo definidos. Nunca execute ataques contra serviços públicos de IA sem autorização; os termos de serviço frequentemente os proíbem. Quando encontrar uma vulnerabilidade no produto de outra pessoa, relate-a em particular ao fornecedor e combine um prazo antes de publicar (divulgação coordenada). Mantenha os dados de teste sintéticos ou devidamente governados; nunca extraia nem publique dados pessoais. A permissão por escrito nomeia quem pode testar, o quê, quando e por quais métodos.

### 10.4 Lei e regulação

O Regulamento (UE) 2024/1689 (o AI Act) classifica alguns sistemas de IA como de alto risco — inclusive componentes de segurança de infraestrutura crítica — e exige gestão de riscos, governança de dados, documentação técnica, registro em logs, supervisão humana e exatidão, robustez e cibersegurança (Artigo 15). As obrigações se aplicam em etapas de 2025 a 2027. Engenheiros devem saber se seu sistema pode cair numa categoria regulada e envolver especialistas jurídicos; este livro dá orientação, não aconselhamento jurídico. Mesmo antes do parecer jurídico, um engenheiro pode preparar a evidência de que um sistema regulado precisaria: um registro de riscos, a documentação dos conjuntos de dados, logs de decisões e registros de revisão humana. Esses registros são boa prática de qualquer forma, e reuni-los cedo evita reconstruir depois, sob prazo, a história de um sistema.

### 10.5 Exemplo resolvido (caso sintético da NRS)

Um gestor pediu a Sam que elevasse o limiar de alerta do TrackEye para reduzir alarmes falsos antes de uma demonstração. Sam calculou que os falsos negativos subiriam de 2% para 5% nos dados diurnos. Sam documentou o compromisso, recusou-se a mudar o limiar de produção sem uma revisão de safety e propôs uma configuração apenas para a demonstração, claramente identificada como tal. Sam também observou que o TrackEye, por ser um componente de segurança da infraestrutura ferroviária, pode ser de alto risco segundo o AI Act, e sinalizou isso para revisão jurídica. A configuração de demonstração atendeu ao objetivo do gestor sem tocar no sistema que inspeciona a via real.

### 10.6 Erros e limites

Três erros são comuns: tratar a ética como separada das decisões técnicas; testar serviços de IA de terceiros sem permissão; e esconder compromissos de safety em mudanças de configuração. Uma ética separada do trabalho técnico tende a aparecer só em documentos de política, enquanto as decisões reais são tomadas em limiares e planos de teste. Testar um serviço público de IA sem permissão pode violar a lei mesmo com boas intenções. Uma mudança de limiar que troca em silêncio defeitos não detectados por menos alarmes é uma decisão de safety tomada sem as pessoas responsáveis pela safety; a regra de Sam é que qualquer mudança que afete as taxas de defeitos perdidos passe por revisão, com seus números declarados.

### Exercícios

- **EX028 — Safety vs. security.** Dê um exemplo em que um ataque de security causa uma falha de safety na NRS e um em que um mecanismo de safety é abusado. Rubrica: 3 = ambos plausíveis; 2 = um; 1 = confuso; 0 = nenhuma.
- **EX029 — Divulgação.** Você descobre que o modelo hospedado de um fornecedor vaza prompts de outros clientes. Liste os passos que você segue. Rubrica: 3 = parar, preservar evidência mínima, relato privado, prazo combinado, nenhuma publicação de dados; 2 = parcial; 1 = vago; 0 = publicar ou explorar.
- **EX030 — AI Act.** Cite quatro obrigações para sistemas de IA de alto risco. Rubrica: 3 = quatro entre gestão de riscos, governança de dados, documentação, registro em logs, transparência, supervisão humana, exatidão/robustez/cibersegurança; 2 = três; 1 = uma ou duas; 0 = nenhuma.

### Síntese

A ética na engenharia de IA é concreta: limites honestos, safety e security geridas em conjunto, testes autorizados, divulgação coordenada e consciência dos deveres legais para sistemas de alto risco.

### Continue estudando — capítulo 10 de 50

[← Capítulo 09 (rascunho)](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (rascunho) →](#ch-11)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Sam Ito, a Northgate Rail Systems e todos os seus números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** σ(z) = (1 + e⁻ᶻ)⁻¹, então σ′(z) = e⁻ᶻ/(1 + e⁻ᶻ)² = σ(z)·(1 − σ(z)), porque 1 − σ(z) = e⁻ᶻ/(1 + e⁻ᶻ). Em z = 0, σ = 0.5, então σ′ = 0.25.

**EX002.** Perda 0.6931 (= ln 2) e gradiente −1.000000. Cada passo move w no sentido oposto ao gradiente (w ← w − 0.5·dL/dw), então w aumenta e a perda cai de 2.1269 para 0.0928.

**EX003.** O treinamento toma a derivada da perda em relação aos parâmetros e dá passos para reduzi-la. Um atacante toma a derivada em relação à entrada e dá passos para aumentar a perda (ou para se aproximar de uma classe-alvo).

**EX004.** ∀ c ∈ Calls(create_work_order): Depot(Asset(c)) = Depot(RequestingTechnician(c)).

**EX005.** Boletim do fornecedor → modelo → create_work_order: tratar o texto do boletim apenas como dado e exigir confirmação do técnico. Notas editáveis por terceirizados → modelo → create_work_order: restringir quem pode editar as notas, rotular a proveniência e exigir confirmação.

**EX006.** C(50,2) × 3² = 1,225 × 9 = 11,025 variantes.

**EX007.** Acima de 800 Hz (o dobro de 400 Hz); na prática, escolha uma margem, por exemplo 1–2 kHz, com um filtro anti-aliasing.

**EX008.** Poeira na lente: deslocamento natural. Padrão pintado num dormente: possível ataque físico adversarial (deliberado). Deriva do termistor: deslocamento natural (envelhecimento).

**EX009.** Iluminação de 1–100,000 lux; velocidade do trem de 0–120 km/h; contaminação da lente de 0–30% de oclusão; temperatura de −20 a +45 °C; intensidade de chuva de 0–50 mm/h (também: marcações a até 1 m do trilho).

**EX010.** `TOOLS = {"search", "summarise"}; def allowed(tool): return tool in TOOLS` com `assert allowed("search") and not allowed("email")`.

**EX011.** `eval` executa o texto como Python, então um texto influenciado por um atacante (por exemplo, via injeção de prompt) vira execução arbitrária de código. OWASP LLM05 Improper Output Handling.

**EX012.** JSON inválido; objeto vazio; campo extra; asset_id com pontuação ou que não seja string; prioridade fora do conjunto; resumo extremamente longo.

**EX013.** "No nosso teste em sandbox (200 boletins sintéticos com instruções injetadas, modelo v1.3, template de prompt v2), o Wrench emitiu uma ordem de serviço não autorizada em 3 de 200 tarefas (intervalo de Wilson de 95% 0.5–4.3%); injeções multilíngues e baseadas em imagens não foram testadas."

**EX014.** Detalhes do modelo (versão, responsável); uso pretendido e usos fora de escopo; dados de avaliação; métricas desagregadas por condição (luz, velocidade, tipo de trilho); considerações éticas e ressalvas.

**EX015.** Gestor: "De madrugada, o TrackEye deixa passar cerca de 4.5 vezes mais defeitos do que de dia; até a correção ser liberada, acrescentamos uma segunda verificação visual nas viagens de madrugada." Auditor: "O relatório de teste TR-031 (v1.3) mostra taxa de falsos negativos de madrugada de 9% contra 2% de dia, frente ao REQ-SAF-004 (≤3%); não conformidade NC-07 aberta; controle provisório documentado."

**EX016.** ∂f/∂x = 2xy; ∂f/∂y = x² + 3; ∇f = (2xy, x² + 3).

**EX017.** Aumento = ε·‖w‖₁ = 0.2 × (2 + 1 + 0.5) = 0.7, com δ = ε·sign(w) = (0.2, −0.2, 0.2).

**EX018.** Qualquer perturbação L2 menor que margem/L = 0.6/3 = 0.2 não consegue mudar o sinal da pontuação.

**EX019.** VP = 0.90 × 0.005 = 0.0045; FP = 0.02 × 0.995 = 0.0199; precisão = 0.0045/0.0244 ≈ 0.184.

**EX020.** TPR 0.80, FPR 0.001 dá precisão de 0.445 com prevalência 0.001 (18 alertas por 10,000) — ao custo de deixar passar 20% dos ataques.

**EX021.** Prompts de um mesmo modelo de texto compartilham estrutura, então seus resultados são correlacionados; a informação está mais perto de 5 grupos independentes do que de 500 tentativas. Reamostre os modelos de texto (cluster bootstrap) e relate os resultados por modelo.

**EX022.** A quantização desloca levemente as pontuações, então entradas perto da fronteira de decisão podem se inverter; taxas de sucesso de ataques e de erro medidas no modelo de 32 bits podem não valer na implantação de 8 bits.

**EX023.** Mitiga: um operador do host na nuvem lendo prompts ou pesos na memória. Não mitiga: injeção de prompt, nem bugs no servidor de modelo que roda dentro do enclave.

**EX024.** Uma falha pode inverter bits depois da verificação de hash no carregamento, durante a inferência. As mitigações incluem memória ECC, novo cálculo periódico do hash, computação redundante e verificações de plausibilidade das saídas.

**EX025.** `ingest` (carrega os dados e os rotula com a proveniência), `inference` (chamadas ao modelo), `policy` (confere cada ação proposta contra papel, escopo e confirmação), `tools` (executa as ações aprovadas). O módulo de políticas aplica a segurança, fora do modelo.

**EX026.** Desserializar um pickle executa o código embutido no arquivo, então um arquivo de modelo malicioso compromete a máquina no carregamento. Use um formato só de tensores (sem código) e verifique um hash fixado, vindo de uma fonte confiável.

**EX027.** "Nenhuma chamada a `create_work_order` é executada sem que leve um token de confirmação válido do técnico solicitante." Outro: "Nenhuma chamada de ferramenta tem como alvo um ativo fora do depósito do usuário solicitante."

**EX028.** Ataque → safety: marcações colocadas perto dos trilhos fazem o TrackEye deixar passar um defeito real. Mecanismo de safety abusado: disparar deliberadamente muitos alertas de baixa confiança para que o sistema recorra à lenta inspeção manual, atrasando o serviço (negação de serviço).

**EX029.** Parar os testes; registrar evidência mínima sem reter dados de terceiros; relatar em particular ao contato de segurança do fornecedor; combinar um prazo de correção e de divulgação; publicar só depois da correção, sem dados pessoais.

**EX030.** Sistema de gestão de riscos; governança de dados; documentação técnica; manutenção de registros/logs; transparência para quem implanta; supervisão humana; exatidão, robustez e cibersegurança.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

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
- Mitchell, M. et al. (2018). Model Cards for Model Reporting. arXiv:1810.03993.
- MITRE ATLAS. <https://atlas.mitre.org/>
- NIST AI 100-1 (2023), AI RMF 1.0. <https://doi.org/10.6028/NIST.AI.100-1>
- NIST AI 100-2 E2025 (2025), Adversarial Machine Learning taxonomy. <https://doi.org/10.6028/NIST.AI.100-2e2025>
- NIST AI 600-1 (2024), Generative AI Profile. <https://doi.org/10.6028/NIST.AI.600-1>
- OWASP Top 10 for LLM Applications 2025. <https://genai.owasp.org/llm-top-10/>
- Shokri, R. et al. (2016). Membership Inference Attacks against Machine Learning Models. arXiv:1610.05820.
- Tramèr, F. et al. (2016). Stealing Machine Learning Models via Prediction APIs. arXiv:1609.02943.
