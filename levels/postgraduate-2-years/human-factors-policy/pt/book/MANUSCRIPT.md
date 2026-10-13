# Fatores Humanos e Política Cibernética: Curso de Pós-Graduação

- Idioma: português do Brasil (`pt`); curso 144, curso de pós-graduação (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–12 de 12 têm texto didático escrito à mão; os exercícios EX001–EX060 têm resoluções correspondentes com rubricas de 0 a 3; os seis laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: profissionais de segurança em atividade que lideram um programa de segurança centrado nas pessoas numa organização de porte médio.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios comparam perda esperada, calculam diferenças de risco, testam a sensibilidade de pesos, analisam uma implantação escalonada com um teste de permutação e resumem dados de garantia e de service desk, todos sintéticos; nenhum funcionário, e-mail ou conta real está envolvido. Toda simulação de phishing descrita é anunciada, aprovada por uma banca que inclui representantes dos funcionários e o RH, evita iscas que explorem sofrimento pessoal, como salário, bônus ou saúde, é relatada apenas de forma agregada e nunca é usada em avaliações de desempenho. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um profissional-estudante que redesenha o programa de uma seguradora: enquadramento da decisão, prática atual, evidências especializadas, risco e ética, alternativas de desenho, avaliação controlada, integração, casos difíceis, liderança e garantia, crítica de pesquisas, um projeto aplicado e a revisão final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Daniel Osei** | Gestor de segurança e estudante de pós-graduação | Inventado |
| **Dra. Ingrid Holm** | Coordenadora do curso | Inventada |
| **Westbrook School of Professional Studies** | Escola fictícia | Inventada |
| **Calloway Insurance** | Seguradora fictícia, 900 funcionários | Inventada |

### Fontes principais

Hansche et al. (2024), NIST SP 800-50r1; Beautement, Sasse e Wonham (2008), [doi:10.1145/1595676.1595684](https://doi.org/10.1145/1595676.1595684); Lain, Kostiainen e Čapkun (2022), [doi:10.1109/SP46214.2022.9833766](https://doi.org/10.1109/SP46214.2022.9833766); Bada, Sasse e Nurse (2019), arXiv:1901.02672; Herley (2009), [doi:10.1145/1719030.1719050](https://doi.org/10.1145/1719030.1719050). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Tomada de decisão avançada em segurança

### Objetivos de aprendizagem

Você vai (1) enquadrar decisões de segurança centradas nas pessoas sob incerteza; (2) usar a perda esperada junto com o ônus para os funcionários; (3) documentar a justificativa das decisões para os líderes.

### 1.1 Enquadrar a decisão

Daniel Osei, gestor de segurança que estuda em meio período na fictícia Westbrook School of Professional Studies, enfrenta uma decisão na fictícia Calloway Insurance, uma empresa de 900 funcionários. O conselho quer saber se deve comprar um serviço ampliado de simulações ou investir em controles mais rápidos de reporte e verificação. A coordenadora do curso, a Dra. Ingrid Holm, pede a ele que enquadre a decisão de forma explícita: as opções, os resultados que importam, as incertezas e as pessoas afetadas. Um enquadramento claro impede que a escolha seja feita apenas pelo entusiasmo de fornecedores ou pelo hábito.

### 1.2 Perda esperada e ônus

Daniel estima a perda anual esperada com fraude de pagamento e roubo de credenciais em cada opção, usando faixas em vez de números únicos, porque as evidências são incertas. Ele acrescenta o ônus para os funcionários, estimado em horas por ano, porque Herley (2009) mostrou que os conselhos de segurança impõem aos usuários custos reais que as organizações muitas vezes ignoram. O laboratório compara as opções pela redução da perda esperada e pelas horas dos funcionários, mostrando que a opção de verificação reduz mais perdas e custa menos horas aos funcionários, embora as faixas se sobreponham o bastante para exigir julgamento.

### Laboratório — Redução da perda esperada e horas dos funcionários em duas opções

```python
# Expected loss reduction (thousands) and staff hours for two options (synthetic, triangular estimates).
opts = {"verification and reporting": ((180, 300, 450), 1800), "expanded simulations": ((60, 130, 230), 4500)}
for name, ((lo, mode, hi), hrs) in opts.items():
    mean = (lo + mode + hi) / 3
    print(f"{name}: expected loss reduction {mean:.0f}k (range {lo}-{hi}k), staff hours {hrs}")
```

Execute com `python3 lab_decide.py`. Saída verificada:

```text
verification and reporting: expected loss reduction 310k (range 180-450k), staff hours 1800
expanded simulations: expected loss reduction 140k (range 60-230k), staff hours 4500
```

### 1.3 Documentar a justificativa

Daniel escreve para o conselho uma nota de decisão de duas páginas que declara as opções, as estimativas, as premissas e sua recomendação pela opção de verificação e reporte. Ele registra o que o faria mudar de ideia, como evidências de que os resultados das simulações predizem perdas reais com fraude. A nota usa linguagem simples e mostra as faixas. Documentar a justificativa permite ao conselho questionar o raciocínio e cria um registro que revisores futuros podem comparar com os resultados reais, o que sustenta o aprendizado entre decisões, e não apenas dentro de uma. O conselho a lê antes da reunião.

### Exemplo resolvido

Daniel enquadra uma escolha de programa na Calloway Insurance, compara perda esperada e horas dos funcionários e documenta uma recomendação com as condições que a mudariam.

> **Caso sintético.** A Calloway e todos os números são sintéticos; Herley (2009) é real.

### Erros e limites

As estimativas de perda são incertas. As estimativas de horas podem omitir esforço oculto.

### Exercícios

- **EX001 — Enquadramento da decisão.** Que elementos compõem o enquadramento da decisão de Daniel? *Rubrica:* 3 = opções, resultados, incertezas e pessoas afetadas;; 2 = enquadramento;; 1 = vago;; 0 = nenhuma.
- **EX002 — O custo de Herley.** Por que incluir as horas dos funcionários, seguindo Herley (2009)? *Rubrica:* 3 = os conselhos de segurança impõem custos reais aos usuários;; 2 = ônus;; 1 = vago;; 0 = nenhuma.
- **EX003 — Comparação no laboratório.** Como as duas opções se compararam em redução de perdas e horas? *Rubrica:* 3 = verificação 310k e 1.800 h; simulações 140k e 4.500 h;; 2 = verificação melhor;; 1 = vago;; 0 = nenhuma.
- **EX004 — O que mudaria a decisão.** Que evidência faria Daniel mudar de ideia? *Rubrica:* 3 = resultados de simulação que predizem perdas reais com fraude;; 2 = predição;; 1 = vago;; 0 = nenhuma.
- **EX005 — Finalidade da nota.** Por que documentar a justificativa? *Rubrica:* 3 = para que possa ser questionada e comparada depois com os resultados;; 2 = registro;; 1 = vago;; 0 = nenhuma.

### Síntese

Decisões avançadas enquadram opções, pesam perda e ônus e registram a justificativa abertamente.

<a id="ch-02"></a>

## Capítulo 2 — Fatores humanos e política cibernética: prática atual

### Objetivos de aprendizagem

Você vai (1) descrever a prática atual dos programas de conscientização em segurança; (2) relacionar a prática a orientações como a NIST SP 800-50r1; (3) identificar lacunas entre a prática e as evidências.

### 2.1 Prática atual

Daniel levanta a prática atual por meio de relatórios do setor e de conversas com colegas de outras organizações. Muitas organizações oferecem cursos online anuais, phishing simulado mensal e painéis de taxas de clique por departamento. Menos organizações medem a rapidez dos reportes ou investem em procedimentos de verificação para tarefas de alto risco. O Verizon DBIR continua relatando um grande elemento humano nas violações, que as organizações muitas vezes citam para justificar o treinamento. Daniel observa que a prática é moldada tanto pelo que é fácil de comprar e relatar quanto pelo que as evidências mostram que funciona. Ele registra cada fonte.

### 2.2 Orientações

A NIST SP 800-50r1 (Hansche et al., 2024) descreve como construir um programa de aprendizagem em cibersegurança e privacidade, incluindo avaliar necessidades, desenhar conteúdo por função, implementar e avaliar. A SP 800-16, mais antiga (Wilson et al., 1998), estabeleceu a distinção entre conscientização, treinamento e educação. As diretrizes de cultura de cibersegurança da ENISA enfatizam entender e moldar a cultura, e não apenas transmitir mensagens. Daniel mapeia o programa da Calloway em relação a esses documentos e descobre que a avaliação de necessidades e a avaliação de resultados são os pontos mais fracos, enquanto a entrega de conteúdo é o mais forte. Ele compartilha o mapeamento com o comitê de riscos, para que os membros vejam onde o esforço se concentra e onde o programa precisa crescer.

### 2.3 Lacunas

Comparando a prática com as evidências, Daniel encontra lacunas. Lain, Kostiainen e Čapkun (2022) constataram que o treinamento embutido após cliques simulados não reduzia os cliques posteriores, e a Calloway usa exatamente isso. Bada, Sasse e Nurse (2019) constataram que mensagens baseadas no medo muitas vezes saem pela culatra, e os cartazes da Calloway usam imagens alarmantes. O reporte, que Lain e colegas consideraram valioso em larga escala, é difícil na Calloway porque o endereço de reporte está escondido. Identificar essas lacunas dá a Daniel uma agenda inicial fundamentada em evidências publicadas, e não em preferência pessoal. Ele lista cada lacuna com sua fonte.

### Exemplo resolvido

Daniel revisa a prática comum, mapeia a Calloway em relação à SP 800-50r1, à SP 800-16 e às orientações da ENISA e identifica três lacunas em relação às evidências.

> **Caso sintético.** A Calloway é sintética; as orientações e os estudos citados são reais.

### Erros e limites

Conversas com colegas são anedóticas. Orientação não é evidência de efeito.

### Exercícios

- **EX006 — Prática comum.** Que medida domina a prática comum? *Rubrica:* 3 = taxas de clique por departamento;; 2 = cliques;; 1 = rapidez dos reportes;; 0 = nenhuma.
- **EX007 — Etapas mais fracas.** Que etapas do programa eram as mais fracas na Calloway? *Rubrica:* 3 = avaliação de necessidades e avaliação de resultados;; 2 = duas;; 1 = entrega;; 0 = nenhuma.
- **EX008 — Lacuna do treinamento embutido.** Que evidência conflita com o treinamento embutido da Calloway? *Rubrica:* 3 = Lain et al. constataram que ele não reduzia os cliques;; 2 = Lain;; 1 = vago;; 0 = nenhuma.
- **EX009 — Lacuna dos cartazes.** Que prática conflita com Bada et al. (2019)? *Rubrica:* 3 = cartazes alarmantes baseados no medo;; 2 = medo;; 1 = vago;; 0 = nenhuma.
- **EX010 — Lacuna do reporte.** Por que o reporte é fraco na Calloway? *Rubrica:* 3 = o endereço de reporte está escondido;; 2 = acesso;; 1 = vago;; 0 = nenhuma.

### Síntese

A prática atual muitas vezes fica atrás das evidências, e as orientações ajudam a mapear as lacunas.

<a id="ch-03"></a>

## Capítulo 3 — Fatores humanos e política cibernética: evidências especializadas

### Objetivos de aprendizagem

Você vai (1) avaliar criticamente estudos especializados sobre comportamento de segurança; (2) interpretar tamanhos de efeito e incerteza; (3) julgar a transferibilidade para uma organização.

### 3.1 Avaliar estudos

Daniel avalia em detalhe os estudos-chave. Para cada um, pergunta o que foi estudado, com quem, como os resultados foram medidos, se havia comparação e que limites os autores declaram. Lain e colegas estudaram milhares de funcionários de uma empresa ao longo de quinze meses, com condições randomizadas, o que dá ao estudo forte validade interna. Adams e Sasse (1999) usaram questionários e entrevistas para explicar o comportamento em relação às senhas, oferecendo profundidade, e não medição de efeitos. A avaliação crítica o ajuda a usar cada estudo para aquilo que ele pode sustentar. Ele mantém anotações sobre cada um.

### 3.2 Tamanhos de efeito

Daniel aprende a ler tamanhos de efeito, e não apenas a significância. Uma diferença pode ser estatisticamente significativa e, ainda assim, pequena na prática, ou grande, mas incerta. O laboratório calcula uma diferença de risco e seu intervalo de confiança para uma comparação sintética das taxas de reporte entre dois formatos de treinamento. O intervalo é largo, de modo que, embora um formato pareça melhor, os dados são compatíveis com um benefício pequeno ou até nulo. Ele observa que as decisões devem considerar a faixa plausível, e não apenas a estimativa pontual. Ele relata os dois números.

### Laboratório — Diferença de risco e intervalo para dois formatos

```python
# Risk difference with Wald 95% interval for two training formats (synthetic).
from math import sqrt
a, n1, b, n2 = 37, 100, 31, 100
p1, p2 = a / n1, b / n2; d = p1 - p2; se = sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
print(f"format A {p1:.0%}, format B {p2:.0%}, difference {100 * d:.1f} points, 95% CI {100 * (d - 1.96 * se):.1f} to {100 * (d + 1.96 * se):.1f}")
```

Execute com `python3 lab_effect.py`. Saída verificada:

```text
format A 37%, format B 31%, difference 6.0 points, 95% CI -7.1 to 19.1
```

### 3.3 Transferibilidade

Um achado de uma organização pode não valer em outra. Daniel compara a Calloway com as organizações dos estudos-chave: tamanho, setor, cultura e exposição a ataques. A Calloway se parece com a grande empresa do estudo de Lain no trabalho intensivo em e-mail, de modo que o achado sobre os reportes provavelmente se transfere; ela difere dos ambientes universitários de alguns estudos sobre senhas. Ele registra explicitamente seus julgamentos de transferibilidade, para que outros possam ver por que ele confia mais em alguns estudos do que em outros ao desenhar o programa da Calloway. A Dra. Holm revisa esses julgamentos.

### Exemplo resolvido

Daniel avalia os estudos pelo desenho, lê um tamanho de efeito com seu intervalo e julga a transferibilidade para a Calloway.

> **Caso sintético.** Os dados do laboratório são sintéticos; os estudos citados são reais.

### Erros e limites

A transferibilidade é um julgamento. Os estudos publicados favorecem resultados positivos.

### Exercícios

- **EX011 — Força do desenho de Lain.** O que dá a Lain et al. forte validade interna? *Rubrica:* 3 = condições randomizadas ao longo de quinze meses;; 2 = randomização;; 1 = vago;; 0 = nenhuma.
- **EX012 — Método de Adams e Sasse.** O que Adams e Sasse (1999) ofereceram? *Rubrica:* 3 = profundidade a partir de questionários e entrevistas;; 2 = profundidade;; 1 = tamanho de efeito;; 0 = nenhuma.
- **EX013 — Diferença no laboratório.** Que diferença de risco o laboratório calculou? *Rubrica:* 3 = 6,0 pontos, intervalo de -7,1 a 19,1;; 2 = largo;; 1 = vago;; 0 = nenhuma.
- **EX014 — Significado do intervalo.** O que significa o intervalo largo? *Rubrica:* 3 = o benefício pode ser pequeno ou nulo;; 2 = incerto;; 1 = vago;; 0 = nenhuma.
- **EX015 — Julgamento de transferência.** Por que o achado de Lain sobre reportes provavelmente se transfere? *Rubrica:* 3 = a Calloway se parece com a grande empresa intensiva em e-mail;; 2 = semelhança;; 1 = vago;; 0 = nenhuma.

### Síntese

As evidências especializadas são avaliadas pelo desenho, lidas com incerteza e transferidas com julgamento explícito.

<a id="ch-04"></a>

## Capítulo 4 — Risco avançado e ética

### Objetivos de aprendizagem

Você vai (1) avaliar riscos centrados nas pessoas usando os conceitos da SP 800-30r1; (2) analisar questões éticas em programas de segurança no ambiente de trabalho; (3) definir uma governança para a prática ética.

### 4.1 Risco centrado nas pessoas

Daniel avalia riscos em que o comportamento humano tem um papel, seguindo os conceitos da NIST SP 800-30r1: fontes de ameaça, eventos, vulnerabilidades, probabilidade e impacto. Na fraude de pagamento, a fonte de ameaça são grupos criminosos, o evento é um falso pedido de mudança de dados de fornecedor, a vulnerabilidade é a ausência de verificação independente e o impacto é a perda financeira direta. Ele observa que a vulnerabilidade está no processo, e não no caráter dos funcionários. Enquadrar o risco dessa forma aponta para controles de processo, e não para mais alertas aos funcionários. O dono do risco concorda.

### 4.2 Questões éticas

Daniel analisa as questões éticas do programa da Calloway. As simulações usam engano sem consentimento específico. Os rankings de cliques por departamento expõem publicamente as equipes. Funcionários que clicam repetidamente são enviados a um treinamento obrigatório descrito como corretivo. Alguns modelos imitam anúncios de bônus. Ele julga cada ponto com base nos princípios de respeito, proporcionalidade e dano. O modelo de bônus explora esperanças financeiras, e os rankings minam a confiança; ambos podem desestimular os reportes. Ele também observa que dados de monitoramento sobre indivíduos poderiam ser mal usados em avaliações de desempenho se não forem controlados. Ele discute cada ponto com o RH.

### 4.3 Governança

Daniel propõe uma governança para a prática ética: um estatuto que declare a finalidade do programa; uma banca de revisão, com representantes dos funcionários e o RH, para aprovar os modelos de simulação; a proibição de iscas que explorem sofrimento pessoal, como salário, bônus ou saúde; relatórios apenas agregados; nenhum uso dos resultados das simulações em avaliações de desempenho; e uma revisão ética anual. A governança transforma boas intenções em regras que persistem quando as pessoas mudam, e dá aos funcionários voz num programa que os afeta diretamente. O conselho a adota.

### Exemplo resolvido

Daniel enquadra o risco de fraude de pagamento nos termos da SP 800-30r1, identifica problemas éticos nos rankings e nas iscas de bônus e propõe uma governança com uma banca de revisão.

> **Caso sintético.** O programa da Calloway é sintético; a SP 800-30r1 é real.

### Erros e limites

As bancas podem aprovar conteúdo limítrofe. As revisões éticas podem virar rotina.

### Exercícios

- **EX016 — Vulnerabilidade da fraude.** Onde está a vulnerabilidade da fraude de pagamento? *Rubrica:* 3 = na ausência de verificação independente;; 2 = processo;; 1 = caráter dos funcionários;; 0 = nenhuma.
- **EX017 — Modelo de bônus.** Por que o modelo de bônus é antiético? *Rubrica:* 3 = explora esperanças financeiras;; 2 = sofrimento;; 1 = vago;; 0 = nenhuma.
- **EX018 — Dano dos rankings.** Que dano os rankings por departamento causam? *Rubrica:* 3 = exposição pública que mina a confiança;; 2 = confiança;; 1 = vago;; 0 = nenhuma.
- **EX019 — Membros da banca.** Quem integra a banca de revisão dos modelos? *Rubrica:* 3 = representantes dos funcionários e o RH;; 2 = representantes;; 1 = vago;; 0 = nenhuma.
- **EX020 — Regra de desempenho.** Que regra se aplica aos resultados das simulações e às avaliações de desempenho? *Rubrica:* 3 = nunca são usados;; 2 = proibição;; 1 = vago;; 0 = nenhuma.

### Síntese

O risco centrado nas pessoas aponta para controles de processo, e a governança torna a prática ética duradoura.

<a id="ch-05"></a>

## Capítulo 5 — Fatores humanos e política cibernética: alternativas de desenho

### Objetivos de aprendizagem

Você vai (1) gerar desenhos alternativos de programa; (2) avaliá-los segundo múltiplos critérios; (3) selecionar e justificar um desenho.

### 5.1 Alternativas

Daniel gera três desenhos para a Calloway. O desenho A refina o modelo atual com simulações melhores e treinamentos mais curtos. O desenho B se centra no reporte: um botão em destaque, retorno rápido, uma política de não atribuição de culpa e simulações reduzidas a trimestrais sob a nova governança. O desenho C se centra na engenharia: autenticação resistente a phishing para todos os funcionários, controles de verificação de pagamentos e filtragem forte, com treinamento mínimo. Ele descreve cada um em uma página, incluindo o que os funcionários vivenciariam no dia a dia, para que as partes interessadas possam visualizar a mudança. As partes interessadas leem os três.

### 5.2 Avaliar

Daniel pontua os desenhos com as partes interessadas quanto a redução de risco, ônus para os funcionários, custo, confiança e evidências para o regulador. Os pesos são acordados antes da pontuação. O laboratório calcula as pontuações ponderadas e testa se a ordenação muda quando cada peso varia pela metade para mais ou para menos. O desenho C tem a maior pontuação em redução de risco, mas a menor em evidências para o regulador; o desenho B se equilibra bem. Uma combinação de B e C surge como a opção mais forte na maioria das configurações de pesos, o que dá ao conselho confiança de que o resultado não é frágil.

### Laboratório — Pontuações ponderadas e sensibilidade para três desenhos

```python
# Weighted scores and sensitivity for three designs plus a combination (synthetic 1-5 scores).
crit = ["risk", "burden", "cost", "trust", "evidence"]
w0 = dict(risk=0.30, burden=0.20, cost=0.15, trust=0.20, evidence=0.15)
S = {"A": [2, 2, 4, 2, 5], "B": [4, 4, 4, 5, 3], "C": [5, 4, 2, 3, 2], "B+C": [5, 4, 3, 5, 4]}
def score(w): return {k: sum(w[c] * v for c, v in zip(crit, vals)) / sum(w.values()) for k, vals in S.items()}
print("base:", {k: round(v, 2) for k, v in score(w0).items()})
wins = 0
for c in crit:
    for f in (0.5, 1.5):
        s = score(dict(w0, **{c: w0[c] * f})); wins += max(s, key=s.get) == "B+C"
print("B+C ranked first in", wins, "of 10 variations")
```

Execute com `python3 lab_weights.py`. Saída verificada:

```text
base: {'A': 2.75, 'B': 4.05, 'C': 3.5, 'B+C': 4.35}
B+C ranked first in 10 of 10 variations
```

### 5.3 Selecionar

Daniel recomenda um desenho combinado: os controles de engenharia de C com a cultura de reporte de B, mantendo um treinamento breve por função para atender aos reguladores. Ele explica o trade-off: custo maior no primeiro ano em troca de reduções duradouras de risco e de ônus. Aponta riscos da combinação, como a sobrecarga de projetos, e propõe implantá-la em fases ao longo de dezoito meses. O conselho aceita e pede uma revisão do andamento aos seis meses. Uma seleção baseada em critérios explícitos torna a decisão mais fácil de defender e de revisitar. O plano de fases é aprovado.

### Exemplo resolvido

Daniel desenha três alternativas, pontua-as com os pesos das partes interessadas, testa a sensibilidade e recomenda uma combinação implantada em fases.

> **Caso sintético.** Os desenhos e as pontuações são sintéticos.

### Erros e limites

As pontuações são subjetivas. Desenhos combinados podem sobrecarregar as equipes.

### Exercícios

- **EX021 — Fraqueza do desenho C.** Em que o desenho C tem a menor pontuação? *Rubrica:* 3 = evidências para o regulador;; 2 = evidências;; 1 = risco;; 0 = nenhuma.
- **EX022 — Momento dos pesos.** Quando os pesos foram acordados? *Rubrica:* 3 = antes da pontuação;; 2 = antes;; 1 = depois;; 0 = nenhuma.
- **EX023 — Sensibilidade no laboratório.** Quão robusto foi o desenho combinado no laboratório? *Rubrica:* 3 = primeiro em 10 de 10 variações de peso;; 2 = robusto;; 1 = vago;; 0 = nenhuma.
- **EX024 — Fases.** Em que período o desenho combinado é implantado? *Rubrica:* 3 = dezoito meses;; 2 = 18;; 1 = vago;; 0 = nenhuma.
- **EX025 — Risco da combinação.** Que risco a combinação traz? *Rubrica:* 3 = sobrecarga de projetos;; 2 = sobrecarga;; 1 = vago;; 0 = nenhuma.

### Síntese

Alternativas avaliadas com pesos acordados, com testes de sensibilidade, sustentam uma seleção robusta.

<a id="ch-06"></a>

## Capítulo 6 — Fatores humanos e política cibernética: avaliação controlada

### Objetivos de aprendizagem

Você vai (1) desenhar uma avaliação controlada de uma mudança no programa; (2) analisar os resultados com testes adequados; (3) tratar as restrições éticas da avaliação.

### 6.1 Desenhar a avaliação

Daniel planeja avaliar as novas mensagens de retorno que informam a quem reportou, em até uma hora, se o reporte era malicioso. Ele usa uma implantação escalonada: seis escritórios começam no primeiro mês, seis no segundo e seis no terceiro, com a ordem sorteada. Todos os escritórios acabam recebendo a mudança, o que responde às preocupações com justiça. O resultado é a proporção de e-mails maliciosos reais reportados por pelo menos uma pessoa em cada escritório por mês, usando dados que o sistema de reportes já coleta, sem ônus adicional.

### 6.2 Análise dentro de cada mês

O laboratório compara escritórios-mês com e sem retorno, ajustando pelo mês ao comparar dentro de cada mês. Os escritórios com retorno mostram uma proporção maior de e-mails maliciosos reportados. Daniel calcula a diferença média dentro dos meses e a confere com um teste de permutação que embaralha quais escritórios tiveram retorno. A diferença observada é maior do que quase todas as diferenças embaralhadas. Ele relata a estimativa, o resultado da permutação e os limites, incluindo que os escritórios têm tamanhos diferentes e que o período é curto. A diferença é de cerca de 14 pontos.

### Laboratório — Análise da implantação escalonada com teste de permutação

```python
# Stepped rollout: 18 offices, start months 1-3 (6 each), 4 months of data (synthetic).
import random
r = random.Random(3)
start = [1] * 6 + [2] * 6 + [3] * 6; r.shuffle(start)
base = [r.uniform(0.45, 0.65) for _ in range(18)]
y = {(o, m): min(1, base[o] + 0.03 * m + (0.16 if m >= start[o] else 0) + r.gauss(0, 0.05)) for o in range(18) for m in range(4)}
def effect(st):
    diffs = []
    for m in range(1, 4):
        t = [y[o, m] for o in range(18) if m >= st[o]]; c = [y[o, m] for o in range(18) if m < st[o]]
        if t and c: diffs.append(sum(t) / len(t) - sum(c) / len(c))
    return sum(diffs) / len(diffs)
obs = effect(start)
cnt = 0; N = 2000
for _ in range(N):
    s = start[:]; r.shuffle(s); cnt += effect(s) >= obs
print(f"within-month difference {100 * obs:.1f} points; permutation share {cnt / N:.3f}")
```

Execute com `python3 lab_stepped.py`. Saída verificada:

```text
within-month difference 14.4 points; permutation share 0.001
```

### 6.3 Restrições éticas

A avaliação usa dados existentes de forma agregada, por isso não é preciso consentimento individual de cada funcionário, mas Daniel informa os funcionários, pelo estatuto e pelos boletins internos, de que a mudança no retorno está sendo avaliada por escritório. A banca de governança aprova o plano. Nenhuma simulação faz parte da avaliação. Ele observa que uma avaliação que negasse indefinidamente a alguns escritórios um retorno útil seria injusta; o desenho escalonado limita o atraso a dois meses, o que a banca considera aceitável diante do conhecimento obtido.

### Exemplo resolvido

Daniel avalia as mensagens de retorno com uma implantação escalonada e randomizada em dezoito escritórios, encontra uma diferença positiva dentro dos meses e documenta a aprovação ética.

> **Caso sintético.** Os escritórios e os dados são sintéticos.

### Erros e limites

Avaliações curtas não captam efeitos de longo prazo. Os escritórios diferem em exposição.

### Exercícios

- **EX026 — Ordem da implantação.** Como foi escolhida a ordem da implantação? *Rubrica:* 3 = por sorteio;; 2 = aleatória;; 1 = por tamanho;; 0 = nenhuma.
- **EX027 — Medida de resultado.** Que resultado foi usado? *Rubrica:* 3 = proporção de e-mails maliciosos reportados por escritório por mês;; 2 = proporção reportada;; 1 = cliques;; 0 = nenhuma.
- **EX028 — Estimativa no laboratório.** Que diferença dentro dos meses o laboratório encontrou? *Rubrica:* 3 = cerca de 14,4 pontos, proporção da permutação 0,001;; 2 = positiva;; 1 = vago;; 0 = nenhuma.
- **EX029 — Sem simulações.** As simulações fizeram parte da avaliação? *Rubrica:* 3 = não;; 2 = nenhuma;; 1 = sim;; 0 = sem resposta.
- **EX030 — Atraso máximo.** Qual foi o atraso máximo para qualquer escritório? *Rubrica:* 3 = dois meses;; 2 = 2;; 1 = vago;; 0 = nenhuma.

### Síntese

Avaliações controladas podem ser justas, éticas e informativas quando a implantação é escalonada e randomizada.

<a id="ch-07"></a>

## Capítulo 7 — Fatores humanos e política cibernética: integração organizacional

### Objetivos de aprendizagem

Você vai (1) integrar o programa ao RH, ao financeiro e à resposta a incidentes; (2) alinhá-lo a frameworks de governança; (3) gerir a mudança entre departamentos.

### 7.1 Ligações entre departamentos

Daniel integra o programa a outras funções da Calloway. O RH acrescenta expectativas de segurança à integração de novos funcionários e concorda que os dados das simulações fiquem fora dos processos de desempenho. O financeiro adota o controle de verificação de pagamentos, com bloqueio das mudanças de dados bancários e retorno de ligação por números conhecidos. A resposta a incidentes recebe os reportes automaticamente e dá crédito, em seus resumos, a quem reportou primeiro. Cada ligação transforma o programa de um projeto da equipe de segurança em parte do modo como a Calloway funciona, o que o torna mais duradouro e menos dependente de alguns entusiastas.

### 7.2 Alinhamento a frameworks

Daniel mapeia o programa para a função Govern do NIST CSF 2.0, que cobre papéis, responsabilidades, política e supervisão, e para os requisitos de conscientização e competência da ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022). Ele mostra ao comitê de riscos como cada elemento fornece evidências para auditorias. Tem o cuidado de não deixar que os frameworks definam o sucesso: eles descrevem estruturas, enquanto resultados como reportes mais rápidos e menos fraudes mostram se o programa funciona. O alinhamento reduz o esforço duplicado quando auditores e reguladores pedem evidências. Os auditores recebem bem o mapeamento. O comitê concorda.

### 7.3 Gerir a mudança

Daniel usa um plano de mudança simples para cada departamento: explicar o porquê, envolver campeões locais, fazer um piloto com uma equipe, ajustar e depois ampliar. O financeiro resiste de início ao controle de verificação, porque ele atrasa os pagamentos no fim do mês. Ele trabalha com a equipe para escalar um segundo analista no fim do mês e pré-verificar os fornecedores habituais. A resistência muitas vezes sinaliza um custo real, e tratar esse custo conquista apoio com mais eficácia do que insistir na conformidade. No nono mês, os três departamentos já adotaram suas partes do programa.

### Exemplo resolvido

Daniel liga o programa ao RH, ao financeiro e à resposta a incidentes, mapeia-o para a função Govern do CSF 2.0 e para a ISO/IEC 27001 e lida com a resistência do financeiro tratando os custos do fim do mês.

> **Caso sintético.** A integração é sintética; o NIST CSF 2.0 e a ISO/IEC 27001:2022 são reais.

### Erros e limites

A integração leva tempo. O mapeamento de frameworks pode virar papelada.

### Exercícios

- **EX031 — Acordo com o RH.** O que o RH acordou sobre os dados das simulações? *Rubrica:* 3 = ficam fora dos processos de desempenho;; 2 = separação;; 1 = vago;; 0 = nenhuma.
- **EX032 — Escopo da função Govern.** O que a função Govern do CSF 2.0 cobre? *Rubrica:* 3 = papéis, responsabilidades, política e supervisão;; 2 = governança;; 1 = detecção;; 0 = nenhuma.
- **EX033 — Papel dos frameworks.** Que papel os frameworks devem ter? *Rubrica:* 3 = descrever estruturas, e não definir o sucesso;; 2 = estrutura;; 1 = resultados;; 0 = nenhuma.
- **EX034 — Resistência do financeiro.** Por que o financeiro resistiu ao controle de verificação? *Rubrica:* 3 = atrasava os pagamentos do fim do mês;; 2 = fim do mês;; 1 = vago;; 0 = nenhuma.
- **EX035 — Lição da resistência.** O que a resistência muitas vezes sinaliza? *Rubrica:* 3 = um custo real;; 2 = custo;; 1 = teimosia;; 0 = nenhuma.

### Síntese

A integração incorpora o programa a outras funções e trata a resistência como informação.

<a id="ch-08"></a>

## Capítulo 8 — Fatores humanos e política cibernética: casos difíceis

### Objetivos de aprendizagem

Você vai (1) tratar casos que envolvem quem clica repetidamente, executivos e denúncias; (2) equilibrar responsabilização e apoio; (3) aplicar princípios consistentes.

### 8.1 Quem clica repetidamente

Um pequeno número de funcionários da Calloway clica repetidamente nos e-mails simulados. O programa antigo os enviava a um treinamento corretivo. Daniel revisa os casos com o RH e descobre que a maioria trabalha em funções que recebem volumes muito altos de e-mail externo, como a regulação de sinistros. Ele propõe apoio em vez de sanção: revisão da carga de trabalho, filtragem extra para as caixas de entrada dessas pessoas e autenticação resistente a phishing, para que um clique cause menos dano. Ele observa que rotular pessoas como reincidentes tende a reduzir sua disposição de reportar erros.

### 8.2 Executivos

Os executivos seniores são alvos frequentes, mas muitas vezes se isentam do programa. Daniel propõe que os executivos sigam as mesmas regras de verificação, que seus assistentes sejam treinados nos procedimentos de retorno de ligação e que recebam breves orientações pessoais sobre a falsificação da própria identidade. Ele explica que os atacantes se passam por executivos justamente porque os funcionários hesitam em questioná-los. Um executivo que acolhe publicamente as ligações de verificação dá aos funcionários permissão para checar, o que fortalece toda a organização. O CEO concorda em gravar uma mensagem curta dizendo isso. Os assistentes também recebem a orientação.

### 8.3 Denúncias e reportes

Uma funcionária reporta que um gestor tem pedido aos colegas que compartilhem senhas para cobrir ausências. Isso é uma violação de política, mas também um sintoma de falta de pessoal. Daniel garante que o reporte seja tratado com confidencialidade pelo canal de denúncias, que quem reportou seja protegida e que o problema de carga de trabalho subjacente seja levantado. Ele aplica princípios consistentes entre os casos: proteger quem reporta, procurar causas sistêmicas, aplicar sanções apenas a atos deliberadamente danosos e manter as decisões documentadas e justas. O gestor também recebe apoio.

### Exemplo resolvido

Daniel reenquadra os cliques repetidos como questão de carga de trabalho e de design, coloca os executivos sob as mesmas regras e trata um reporte de compartilhamento de senhas pelo canal de denúncias, com correções sistêmicas.

> **Caso sintético.** Os casos são sintéticos.

### Erros e limites

O apoio pode ser visto como leniência. O engajamento dos executivos pode se dissipar.

### Exercícios

- **EX036 — Funções de quem clica.** Onde trabalhava a maioria de quem clicava repetidamente? *Rubrica:* 3 = funções com alto volume de e-mail externo, como sinistros;; 2 = sinistros;; 1 = vago;; 0 = nenhuma.
- **EX037 — Apoio a quem clica.** Que apoio Daniel propôs a quem clica repetidamente? *Rubrica:* 3 = revisão da carga de trabalho, filtragem extra e autenticação resistente a phishing;; 2 = apoio;; 1 = treinamento corretivo;; 0 = nenhuma.
- **EX038 — Mensagem do executivo.** O que o CEO concordou em fazer? *Rubrica:* 3 = gravar uma mensagem acolhendo as ligações de verificação;; 2 = permissão;; 1 = vago;; 0 = nenhuma.
- **EX039 — Causa do compartilhamento de senhas.** Que problema subjacente o reporte de compartilhamento de senhas revelou? *Rubrica:* 3 = falta de pessoal;; 2 = carga de trabalho;; 1 = malícia;; 0 = nenhuma.
- **EX040 — Regra de sanção.** Quando se aplicam sanções pelos princípios de Daniel? *Rubrica:* 3 = apenas a atos deliberadamente danosos;; 2 = deliberados;; 1 = qualquer erro;; 0 = nenhuma.

### Síntese

Casos difíceis exigem princípios consistentes que protejam quem reporta e corrijam as causas sistêmicas.

<a id="ch-09"></a>

## Capítulo 9 — Fatores humanos e política cibernética: liderança e garantia

### Objetivos de aprendizagem

Você vai (1) liderar um programa de segurança centrado nas pessoas; (2) fornecer garantia a conselhos e reguladores; (3) comunicar a incerteza com honestidade.

### 9.1 Liderar o programa

Daniel lidera uma pequena equipe e uma rede de trinta campeões espalhados pelos departamentos. Ele define uma finalidade clara: ajudar as pessoas a fazer escolhas seguras com facilidade e a reportar rapidamente. Realiza reuniões mensais com os campeões para compartilhar exemplos e problemas. Dá o exemplo do comportamento que pede, reportando abertamente seus próprios quase incidentes. Liderar nessa área tem menos a ver com comandar a conformidade e mais com criar condições em que as pessoas se sintam capazes de agir com segurança e de se manifestar quando algo parece errado. Os campeões fazem rodízio anual.

### 9.2 Garantia

O conselho e o regulador de seguros pedem garantia de que os riscos humanos são geridos. Daniel fornece um relatório trimestral com medidas de resultado: mediana do tempo até o primeiro reporte, proporção de e-mails maliciosos reportados, mudanças de pagamento bloqueadas e verificadas e ônus para os funcionários. Ele inclui os resultados de verificação dos controles e as decisões da banca de governança. O laboratório produz um resumo trimestre a trimestre a partir de dados sintéticos. Garantia significa mostrar evidências de que os controles funcionam e os resultados melhoram, e não apenas listar atividades concluídas. Cada medida tem uma definição escrita.

### Laboratório — Medidas trimestrais de garantia

```python
# Quarterly assurance measures (synthetic).
q = [("Q1", 52, 0.48, 3, 3.1), ("Q2", 31, 0.61, 5, 3.0), ("Q3", 19, 0.72, 4, 2.8), ("Q4", 14, 0.79, 6, 2.7)]
for name, med, share, held, burden in q:
    print(f"{name}: median first report {med} min, reported share {share:.0%}, fake changes held {held}, burden {burden}/5")
```

Execute com `python3 lab_assure.py`. Saída verificada:

```text
Q1: median first report 52 min, reported share 48%, fake changes held 3, burden 3.1/5
Q2: median first report 31 min, reported share 61%, fake changes held 5, burden 3.0/5
Q3: median first report 19 min, reported share 72%, fake changes held 4, burden 2.8/5
Q4: median first report 14 min, reported share 79%, fake changes held 6, burden 2.7/5
```

### 9.3 Comunicar a incerteza

Daniel relata a incerteza com honestidade. Mostra intervalos para as taxas, observa quando as mudanças estão dentro da variação normal e explica quando os volumes de ataque mudaram. Quando o conselho pergunta se o programa tornou a Calloway segura, ele responde que reduziu riscos específicos de forma mensurável, mas que nenhum programa elimina o engano. O conselho valoriza essa franqueza. Ele observa que exagerar minaria a confiança quando ocorresse o próximo incidente, enquanto um relato honesto define expectativas realistas. Ele inclui um glossário curto para que os conselheiros possam ler intervalos e variações sem precisar de formação estatística.

### Exemplo resolvido

Daniel lidera por meio de uma finalidade e de campeões, apresenta trimestralmente uma garantia baseada em resultados e comunica a incerteza com honestidade.

> **Caso sintético.** As medidas são sintéticas.

### Erros e limites

O comprometimento dos campeões varia. Dados trimestrais são ruidosos.

### Exercícios

- **EX041 — Finalidade do programa.** Que finalidade Daniel definiu? *Rubrica:* 3 = ajudar as pessoas a fazer escolhas seguras com facilidade e a reportar rapidamente;; 2 = finalidade;; 1 = conformidade;; 0 = nenhuma.
- **EX042 — Dar o exemplo.** Como Daniel dá o exemplo do comportamento desejado? *Rubrica:* 3 = reportando abertamente seus próprios quase incidentes;; 2 = abertura;; 1 = vago;; 0 = nenhuma.
- **EX043 — Tendência no laboratório.** Como a mediana do tempo de reporte evoluiu ao longo dos trimestres? *Rubrica:* 3 = 52, 31, 19 e 14 minutos;; 2 = queda;; 1 = vago;; 0 = nenhuma.
- **EX044 — Significado de garantia.** O que garantia significa aqui? *Rubrica:* 3 = evidências de que os controles funcionam e os resultados melhoram;; 2 = evidências;; 1 = listas de atividades;; 0 = nenhuma.
- **EX045 — Resposta ao conselho.** Como Daniel respondeu se a Calloway está segura? *Rubrica:* 3 = riscos específicos reduzidos, mas o engano não foi eliminado;; 2 = franqueza;; 1 = sim;; 0 = nenhuma.

### Síntese

A liderança cria condições seguras, e a garantia relata as evidências com incerteza honesta.

<a id="ch-10"></a>

## Capítulo 10 — Leitura e crítica de pesquisas

### Objetivos de aprendizagem

Você vai (1) ler artigos de pesquisa com senso crítico; (2) escrever uma crítica estruturada; (3) identificar implicações para a prática.

### 10.1 Leitura crítica

Daniel lê com atenção três artigos: Sasse, Brostoff e Weirich (2001), sobre transformar o elo mais fraco; Beautement, Sasse e Wonham (2008), sobre o orçamento de compliance; e Lain, Kostiainen e Čapkun (2022), sobre phishing nas organizações. Para cada um, anota a pergunta, os métodos, os achados e os limites, e pergunta se as conclusões decorrem das evidências. Ele lê as seções de métodos com cuidado, porque os resumos em outras fontes muitas vezes exageram os achados ou omitem limites que os próprios autores declararam com clareza. Ele mantém um diário de leitura, com uma página de notas sobre cada artigo e seus limites.

### 10.2 Crítica estruturada

Daniel escreve uma crítica do artigo sobre o orçamento de compliance. Resume seu argumento de que os funcionários pesam o esforço de segurança contra os objetivos do negócio e têm capacidade limitada de conformidade. Aponta pontos fortes: o conceito se baseia em entrevistas em várias organizações e explica muitos comportamentos observados. Aponta limites: o orçamento é difícil de medir diretamente, e o artigo oferece um framework, e não previsões testadas. Conclui que o conceito é útil para decisões de design, desde que os gestores o tratem como uma lente, e não como uma quantidade precisa.

### 10.3 Implicações

A partir das leituras, Daniel tira implicações para a Calloway: projetar para reduzir o esforço; medir o ônus junto com os resultados; favorecer o reporte coletivo em vez da perfeição individual; e tratar as simulações com cautela, já que as evidências sugerem que algumas práticas comuns acrescentam pouco. Ele as registra no estatuto do programa, com citações. A crítica é valiosa não para encontrar defeitos, mas para entender até onde cada estudo pode sustentar decisões, o que protege a prática tanto da fé cega quanto da rejeição da pesquisa. A banca de governança revisa as mudanças no estatuto e as aprova depois de uma breve discussão com o RH.

### Exemplo resolvido

Daniel lê três artigos com senso crítico, critica o artigo sobre o orçamento de compliance e registra quatro implicações no estatuto da Calloway.

> **Caso sintético.** As obras citadas são reais; a Calloway é sintética.

### Erros e limites

A crítica pode descambar para a busca de defeitos. As implicações podem esticar as evidências.

### Exercícios

- **EX046 — Foco nos métodos.** Por que Daniel lê as seções de métodos com cuidado? *Rubrica:* 3 = resumos em outras fontes muitas vezes exageram ou omitem limites;; 2 = precisão;; 1 = vago;; 0 = nenhuma.
- **EX047 — Ponto forte do orçamento.** Cite um ponto forte do artigo sobre o orçamento de compliance. *Rubrica:* 3 = baseia-se em entrevistas em várias organizações;; 2 = fundamentação;; 1 = vago;; 0 = nenhuma.
- **EX048 — Limite do orçamento.** Cite um limite do artigo sobre o orçamento de compliance. *Rubrica:* 3 = o orçamento é difícil de medir diretamente;; 2 = medição;; 1 = vago;; 0 = nenhuma.
- **EX049 — Uso como lente.** Como os gestores devem tratar o orçamento de compliance? *Rubrica:* 3 = como uma lente, e não uma quantidade precisa;; 2 = lente;; 1 = número;; 0 = nenhuma.
- **EX050 — Implicações no estatuto.** Onde Daniel registrou suas implicações? *Rubrica:* 3 = no estatuto do programa, com citações;; 2 = estatuto;; 1 = vago;; 0 = nenhuma.

### Síntese

A leitura crítica pesa o que os estudos conseguem sustentar e os traduz com cuidado para a prática.

<a id="ch-11"></a>

## Capítulo 11 — Projeto aplicado

### Objetivos de aprendizagem

Você vai (1) conduzir um projeto aplicado sobre um controle centrado nas pessoas; (2) avaliar resultados e ônus; (3) relatar às partes interessadas.

### 11.1 O projeto

O projeto aplicado de Daniel introduz chaves de segurança resistentes a phishing para o pessoal de sinistros e do financeiro da Calloway, 240 pessoas que lidam com pagamentos e dados sensíveis. Ele planeja a implantação com a TI, o RH e os líderes de equipe: as chaves são entregues em sessões curtas, cada pessoa registra duas chaves e um processo de recuperação simples é criado. Ele aplica as lições dos capítulos anteriores: envolver os usuários cedo, testar com uma equipe piloto e medir o ônus. O projeto busca tornar ineficaz o phishing de credenciais nas funções mais visadas. A equipe piloto dá retorno.

### 11.2 Resultados e ônus

Depois de quatro meses, Daniel compara os resultados de phishing de credenciais e as ligações ao service desk. Antes das chaves, essas equipes tinham vários comprometimentos de conta por phishing por ano; depois, nenhum durante o período, embora o período seja curto. As ligações ao service desk subiram no primeiro mês, enquanto as pessoas aprendiam a usar as chaves, e depois caíram abaixo do nível anterior, porque as redefinições de senha diminuíram. O laboratório resume as ligações mensais ao service desk. Um questionário curto mostra que a maioria dos funcionários acha as chaves mais fáceis do que os códigos, embora alguns se preocupem em perdê-las.

### Laboratório — Ligações ao service desk antes e depois das chaves

```python
# Monthly help desk calls for 240 staff before and after security keys (synthetic).
base = 45; after = [62, 44, 36, 31]
print("baseline per month:", base)
for m, c in enumerate(after, 1): print(f"month {m}: {c} ({c - base:+d})")
```

Execute com `python3 lab_keys.py`. Saída verificada:

```text
baseline per month: 45
month 1: 62 (+17)
month 2: 44 (-1)
month 3: 36 (-9)
month 4: 31 (-14)
```

### 11.3 Relatar

Daniel relata ao conselho e aos funcionários. Declara que as chaves eliminaram a principal via de roubo de credenciais nas equipes visadas e reduziram as ligações de suporte sobre senhas depois de um período de aprendizado. Aponta os limites: quatro meses é pouco tempo, e os atacantes podem migrar para outros métodos, como a fraude por telefone, que os controles de verificação tratam. Ele recomenda estender as chaves a todos os funcionários ao longo do próximo ano. Os funcionários ouvem os resultados primeiro, o que reforça que o programa é feito com eles, e não para eles.

### Exemplo resolvido

Daniel implanta chaves de segurança para 240 funcionários, não encontra comprometimentos por phishing em quatro meses e observa menor carga no service desk após um mês de aprendizado, e relata com honestidade.

> **Caso sintético.** O projeto é sintético.

### Erros e limites

Períodos curtos enganam. A perda de chaves exige uma boa recuperação.

### Exercícios

- **EX051 — Grupo-alvo.** Que funcionários receberam as chaves primeiro? *Rubrica:* 3 = pessoal de sinistros e do financeiro, 240 pessoas;; 2 = funções visadas;; 1 = vago;; 0 = nenhuma.
- **EX052 — Duas chaves.** Por que cada pessoa registra duas chaves? *Rubrica:* 3 = como reserva, caso uma se perca;; 2 = reserva;; 1 = vago;; 0 = nenhuma.
- **EX053 — Padrão do service desk.** O que o laboratório mostrou sobre as ligações ao service desk? *Rubrica:* 3 = subiram para 62 no primeiro mês e caíram para 31 no quarto, a partir de uma base de 45;; 2 = oscilação;; 1 = vago;; 0 = nenhuma.
- **EX054 — Migração dos atacantes.** Para onde os atacantes podem migrar? *Rubrica:* 3 = fraude por telefone;; 2 = telefone;; 1 = vago;; 0 = nenhuma.
- **EX055 — Ordem dos públicos.** Quem ouviu os resultados primeiro? *Rubrica:* 3 = os funcionários;; 2 = funcionários;; 1 = o conselho;; 0 = nenhuma.

### Síntese

Projetos aplicados entregam controles com os usuários, medem o ônus e relatam os limites.

<a id="ch-12"></a>

## Capítulo 12 — Revisão final e transferência

### Objetivos de aprendizagem

Você vai (1) revisar o desenvolvimento do programa como um todo; (2) transferir as lições para outros contextos; (3) planejar o desenvolvimento profissional contínuo.

### 12.1 Revisar o todo

Daniel revisa os dois anos na Calloway. O programa passou das simulações e dos rankings de cliques para o reporte, o retorno rápido, os controles de verificação e as chaves de segurança, sob um estatuto e uma banca que inclui representantes dos funcionários. As medidas de resultado melhoraram: reportes mais rápidos, mais e-mails maliciosos reportados e falsas mudanças de pagamento barradas. O ônus caiu ligeiramente. Ele também lista o que não funcionou, como um esquema inicial de campeões que desmoronou porque os campeões não tinham tempo reservado para a função. Uma revisão do todo mostra como as partes interagiram ao longo do tempo.

### 12.2 Transferência

Daniel considera como as lições se transferem. Uma pequena instituição beneficente não teria equipe de segurança, de modo que as ideias centrais, reporte fácil, retorno gentil, verificação de pagamentos e autenticação forte, precisariam de formas mais simples. Um hospital enfrentaria a pressão de tempo clínica, o que tornaria o ônus ainda mais importante. Ele escreve um guia de transferência curto que separa os princípios dos detalhes específicos da Calloway. Transferir exige distinguir por que algo funcionou de como foi feito, já que o como muitas vezes depende dos recursos e da cultura locais. Ele testa o guia com um colega de uma instituição beneficente.

### 12.3 Desenvolvimento contínuo

Daniel planeja seu desenvolvimento contínuo: ler novas evidências a cada trimestre, incluindo o DBIR anual e novos estudos; participar de um grupo de gestores de segurança; e orientar um colega júnior em métodos centrados nas pessoas. A Dra. Holm sugere que ele escreva um artigo curto para profissionais sobre a avaliação escalonada, já que avaliações baseadas na prática são raras na literatura. Ele observa que o campo muda rapidamente à medida que os atacantes se adaptam, por isso seu aprendizado precisa continuar muito além do curso. Ele também reserva duas horas por mês na agenda para leitura e reflexão.

### Exemplo resolvido

Daniel revisa o programa como um todo, escreve um guia de transferência que separa princípios de detalhes locais e planeja seu desenvolvimento contínuo.

> **Caso sintético.** A revisão é sintética; o DBIR é real.

### Erros e limites

As revisões podem ser autocomplacentes. Os guias de transferência simplificam demais.

### Exercícios

- **EX056 — Mudança do programa.** De onde e para onde o programa mudou? *Rubrica:* 3 = de simulações e rankings para reporte, retorno, verificação e chaves;; 2 = mudança;; 1 = vago;; 0 = nenhuma.
- **EX057 — Esquema que falhou.** Que esquema inicial falhou, e por quê? *Rubrica:* 3 = campeões sem tempo reservado;; 2 = tempo;; 1 = vago;; 0 = nenhuma.
- **EX058 — Diferença no hospital.** O que importaria mais num hospital? *Rubrica:* 3 = o ônus, por causa da pressão de tempo clínica;; 2 = ônus;; 1 = vago;; 0 = nenhuma.
- **EX059 — Distinção na transferência.** O que a transferência precisa distinguir? *Rubrica:* 3 = por que algo funcionou de como foi feito;; 2 = princípio;; 1 = vago;; 0 = nenhuma.
- **EX060 — Artigo sugerido.** Que artigo a Dra. Holm sugeriu? *Rubrica:* 3 = sobre a avaliação escalonada;; 2 = avaliação;; 1 = vago;; 0 = nenhuma.

### Síntese

A revisão final conecta as partes, separa princípios de detalhes e se compromete com o aprendizado contínuo.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. Daniel Osei, a Dra. Ingrid Holm, a Westbrook School of Professional Studies, a Calloway Insurance e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** As opções, os resultados que importam, as incertezas e as pessoas afetadas.

**EX002.** Porque os conselhos de segurança impõem aos usuários custos reais que muitas vezes são ignorados.

**EX003.** A verificação reduziu a perda esperada em cerca de 310 mil com 1.800 horas dos funcionários; as simulações, em cerca de 140 mil com 4.500 horas.

**EX004.** Evidências de que os resultados das simulações predizem perdas reais com fraude.

**EX005.** Para que o conselho possa questioná-la e revisores futuros possam compará-la com os resultados.

**EX006.** As taxas de clique por departamento nas simulações.

**EX007.** A avaliação de necessidades e a avaliação de resultados.

**EX008.** Lain, Kostiainen e Čapkun (2022) constataram que o treinamento embutido não reduzia os cliques posteriores.

**EX009.** Os cartazes da Calloway baseados no medo.

**EX010.** Porque o endereço de reporte é difícil de encontrar.

**EX011.** Condições randomizadas com milhares de funcionários ao longo de quinze meses.

**EX012.** Profundidade de explicação a partir de questionários e entrevistas.

**EX013.** Uma diferença de 6,0 pontos, com intervalo de 95% de cerca de -7,1 a 19,1 pontos.

**EX014.** Que o benefício real pode ser pequeno ou até nulo.

**EX015.** Porque a Calloway se parece com a grande empresa intensiva em e-mail que foi estudada.

**EX016.** No processo, que não tem verificação independente.

**EX017.** Porque explora as esperanças e ansiedades financeiras dos funcionários.

**EX018.** Expõem publicamente as equipes e minam a confiança, desestimulando os reportes.

**EX019.** Representantes dos funcionários e o RH, ao lado da segurança.

**EX020.** Os resultados das simulações nunca são usados em avaliações de desempenho.

**EX021.** Em evidências para o regulador.

**EX022.** Antes de qualquer pontuação.

**EX023.** Ficou em primeiro lugar nas dez variações de peso.

**EX024.** Dezoito meses.

**EX025.** O risco de sobrecarregar as equipes de projeto.

**EX026.** Por sorteio.

**EX027.** A proporção de e-mails maliciosos reais reportados por pelo menos uma pessoa, por escritório e por mês.

**EX028.** Cerca de 14,4 pontos percentuais, com apenas 0,1% dos embaralhamentos tão grandes quanto isso.

**EX029.** Não; usou apenas e-mails reais reportados.

**EX030.** Dois meses.

**EX031.** Que eles ficam fora dos processos de desempenho.

**EX032.** Papéis, responsabilidades, política e supervisão.

**EX033.** Descrever estruturas, e não definir o sucesso, que é mostrado pelos resultados.

**EX034.** Porque atrasava os pagamentos no fim do mês.

**EX035.** Um custo real que precisa ser tratado.

**EX036.** Em funções com alto volume de e-mail externo, como a regulação de sinistros.

**EX037.** Revisão da carga de trabalho, filtragem extra e autenticação resistente a phishing.

**EX038.** Gravar uma mensagem acolhendo as ligações de verificação.

**EX039.** Falta de pessoal, que levava a pedidos para cobrir ausências.

**EX040.** Apenas a atos deliberadamente danosos.

**EX041.** Ajudar as pessoas a fazer escolhas seguras com facilidade e a reportar rapidamente.

**EX042.** Reportando abertamente seus próprios quase incidentes.

**EX043.** Caiu de 52 para 31, 19 e 14 minutos.

**EX044.** Mostrar evidências de que os controles funcionam e os resultados melhoram.

**EX045.** Que riscos específicos foram reduzidos de forma mensurável, mas que nenhum programa elimina o engano.

**EX046.** Porque os resumos em outras fontes muitas vezes exageram os achados ou omitem limites.

**EX047.** Baseia-se em entrevistas em várias organizações e explica muitos comportamentos.

**EX048.** O orçamento é difícil de medir diretamente, e o artigo oferece um framework, e não previsões testadas.

**EX049.** Como uma lente para o design, e não como uma quantidade precisa.

**EX050.** No estatuto do programa, com citações.

**EX051.** O pessoal de sinistros e do financeiro, 240 pessoas.

**EX052.** Para ter uma reserva caso uma chave se perca.

**EX053.** As ligações subiram para 62 no primeiro mês e depois caíram para 31 no quarto mês, abaixo da base de 45.

**EX054.** Fraude por telefone, tratada pelos controles de verificação.

**EX055.** Os funcionários, o que reforça que o programa é feito com eles.

**EX056.** De simulações e rankings de cliques para reporte, retorno rápido, controles de verificação e chaves de segurança.

**EX057.** Um esquema de campeões que fracassou porque os campeões não tinham tempo reservado.

**EX058.** O ônus, por causa da pressão de tempo clínica.

**EX059.** Por que algo funcionou de como foi feito localmente.

**EX060.** Um artigo para profissionais sobre a avaliação escalonada.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Beautement, A., Sasse, M. A., & Wonham, M. (2008). The compliance budget: Managing security behaviour in organisations. *Proceedings of the 2008 New Security Paradigms Workshop*, 47–58. <https://doi.org/10.1145/1595676.1595684>
- European Union Agency for Cybersecurity. (2019). *Cybersecurity culture guidelines: Behavioural aspects of cybersecurity*. ENISA. <https://www.enisa.europa.eu/publications/cybersecurity-culture-guidelines-behavioural-aspects-of-cybersecurity>
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Lain, D., Kostiainen, K., & Čapkun, S. (2022). Phishing in organizations: Findings from a large-scale and long-term study. *2022 IEEE Symposium on Security and Privacy*, 842–859. <https://doi.org/10.1109/SP46214.2022.9833766>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
- Verizon Business. (2024). *2024 Data breach investigations report*. Verizon. <https://www.verizon.com/business/resources/reports/dbir/>
- Wilson, M., de Zafra, D. E., Pitcher, S. I., Tressler, J. D., & Ippolito, J. B. (1998). *Information technology security training requirements: A role- and performance-based model* (NIST SP 800-16). NIST. <https://doi.org/10.6028/NIST.SP.800-16>
