# Segurança de IA e Aprendizado de Máquina: Livro de Pesquisa de Mestrado

- Idioma: português do Brasil (`pt`); programa de mestrado, dois anos; aproximadamente 1.600 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–8 de 8 têm texto didático escrito; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; os laboratórios offline usam a biblioteca padrão do Python 3, e as saídas impressas foram produzidas por execuções reais. A revisão independente e a verificação de 300 páginas A4 continuam em aberto. Cobertura de capítulos em rascunho não é um livro concluído.
- Público: pesquisadores iniciantes que vão desenhar, executar e defender uma dissertação orientada em segurança de IA e aprendizado de máquina.
- Relação com os livros vizinhos: o [livro de pós-graduação](../../../../postgraduate-2-years/ai-security/en/book/MANUSCRIPT.md) é orientado à prática; o [livro de doutorado](../../../../doctorate-2-years/ai-security/en/book/MANUSCRIPT.md) pede uma contribuição original testada de forma independente. **Este livro ensina o ciclo completo de pesquisa uma vez, sob orientação**: pergunta, literatura, desenho, explicações concorrentes, piloto, análise, escrita e defesa.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação e não concede autorização para testar sistemas reais. Todas as organizações, pessoas, conjuntos de dados e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Cada capítulo tem objetivos de aprendizagem, texto didático, um exemplo resolvido, atividades práticas, erros e limites, exercícios pontuados de 0 a 3 (0 ausente ou inseguro; 1 lacuna grave; 2 lacunas menores; 3 completo e justificado), uma síntese e um bloco **Continue estudando**. Os laboratórios são determinísticos, rodam offline com `python3 arquivo.py` e imprimem os resultados mostrados em *Saída esperada*. São modelos de brinquedo escolhidos para tornar um conceito mensurável, não evidência sobre sistemas em produção.

### O exemplo contínuo (sintético): uma dissertação sobre privacidade na Harbourline

> **Caso sintético — ficção.** *Leo Brandt* é um mestrando alocado na **Harbourline Mutual**, uma seguradora inventada que faz o ajuste fino (fine-tuning) de um classificador de texto para triar notas de sinistro. A dissertação de Leo pergunta se *deduplicar os registros de treino* reduz o vazamento por inferência de pertencimento (membership inference) do modelo ajustado a um custo de acurácia aceitável. Todos os registros são sintéticos; nenhum dado real de segurado é usado; os experimentos rodam numa cópia isolada. Todo número sobre a Harbourline é inventado.

### Política de fontes

As fontes foram verificadas em 12 de outubro de 2026: NIST [AI 100-1](https://doi.org/10.6028/NIST.AI.100-1), [AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) e [AI 100-2 E2025](https://doi.org/10.6028/NIST.AI.100-2e2025); o [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); o [MITRE ATLAS](https://atlas.mitre.org/); o [Regulamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj); e a [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html). Os artigos são citados pelo identificador arXiv, e cada um foi aberto e teve o título conferido.

## Sumário

| Etapa | Capítulo |
|---|---|
| 1 | [1 Pergunta de pesquisa e método de revisão da literatura](#ch-01) |
| 1 | [2 Segurança de IA e aprendizado de máquina: seminário avançado](#ch-02) |
| 2 | [3 Desenho do estudo, ética e reprodutibilidade](#ch-03) |
| 2 | [4 Segurança de IA e aprendizado de máquina: explicações concorrentes](#ch-04) |
| 3 | [5 Proposta e piloto](#ch-05) |
| 3 | [6 Coleta e análise de dados](#ch-06) |
| 4 | [7 Escrita da dissertação e limitações](#ch-07) |
| 4 | [8 Revisão independente e defesa](#ch-08) |

[Resoluções](#worked-results) · [Referências](#referências)

<a id="ch-01"></a>

## Capítulo 1 — Pergunta de pesquisa e método de revisão da literatura

### Objetivos de aprendizagem

Você vai (1) passar de um tema a uma pergunta pesquisável com uma unidade de análise clara; (2) conduzir uma busca bibliográfica sistemática e documentada em veículos de segurança e de aprendizado de máquina e em servidores de preprints; (3) extrair evidências para uma matriz de comparação; (4) julgar a qualidade das fontes, inclusive preprints e material de fornecedores; e (5) escrever uma seção curta e honesta de estado da arte.

### 1.1 Do tema à pergunta

"Privacidade da IA" é um tema. "Deduplicar os registros de treino reduz a vantagem da inferência de pertencimento contra um classificador de texto ajustado, e a que custo de acurácia?" é uma pergunta. Uma pergunta pesquisável nomeia um *sistema* (classificador ajustado), uma *intervenção ou fator* (deduplicação), um *desfecho* (vantagem da inferência de pertencimento; acurácia) e, implicitamente, uma *comparação* (com versus sem). O acrônimo PICO, da medicina baseada em evidências (população, intervenção, comparação, desfecho — *outcome*), é um modelo útil. Verifique a viabilidade cedo: você consegue obter ou sintetizar os dados, tem capacidade computacional, o trabalho cabe no prazo, e ele é ético e autorizado?

### 1.2 Uma busca documentada

A literatura de segurança de IA está espalhada por conferências de segurança (IEEE S&P, USENIX Security, ACM CCS, NDSS), conferências de aprendizado de máquina (NeurIPS, ICML, ICLR) e preprints do arXiv, além de frameworks do NIST, da OWASP e do MITRE. Escreva um protocolo de busca: bases (por exemplo, DBLP, Google Scholar, arXiv, ACM Digital Library), expressões de busca, intervalo de datas, critérios de inclusão e exclusão, e a data em que você buscou. Siga as citações para frente e para trás a partir de artigos-semente — para inferência de pertencimento, Shokri et al. (arXiv:1610.05820) é a semente óbvia. Registre as contagens em cada etapa (encontrados, triados, incluídos) para que um leitor possa repetir a busca. Esta é uma versão leve da prática de revisão sistemática; ela protege você de citar apenas o que já conhecia.

### 1.3 Extração de evidências

Monte uma matriz com uma linha por artigo e colunas para: modelo de ameaça (conhecimento e acesso do atacante), tipo e tamanho do modelo, dados, métrica, resultado principal, defesa testada, avaliação adaptativa, disponibilidade de código e limitações. Em trabalhos de privacidade, registre se o artigo relata a taxa de verdadeiros positivos com baixa taxa de falsos positivos (TPR com FPR baixa) ou apenas acurácia/AUC médias; a primeira importa porque um ataque que identifica com confiança alguns indivíduos é um dano real, mesmo que o seu desempenho médio pareça modesto. A matriz vai revelar divergências e lacunas que se tornam a sua contribuição.

### 1.4 Julgamento das fontes

Ordene as evidências pelo quanto podem ser verificadas. Artigos revisados por pares com código publicado são os mais fortes; preprints podem ser excelentes, mas não foram revisados; blogs e marketing de fornecedores são alegações a verificar, não evidência. Normas e frameworks (NIST AI 100-1, AI 100-2 E2025, ISO/IEC 42001) definem vocabulário e expectativas; não são resultados experimentais. Quando um preprint sai depois num veículo, cite a versão final se ela for diferente. Nunca cite um artigo que você não abriu, e nunca invente um DOI: se não encontrar um identificador, cite o título, os autores, o ano e a URL que você de fato usou.

### 1.5 Exemplo resolvido (caso sintético da Harbourline)

O protocolo de Leo buscou no DBLP, no arXiv e no Google Scholar em 2 de fevereiro, com expressões que combinavam "membership inference", "fine-tuning", "deduplication" e "memorization", no período 2016–2026, incluindo estudos empíricos sobre classificadores ou modelos de linguagem e excluindo artigos sem modelo de ameaça declarado. Dos 212 resultados, 61 passaram na triagem por título, 24 na triagem por resumo e 17 na leitura do texto completo. A matriz mostrou que a maioria dos estudos relatava AUC, poucos relatavam TPR com FPR de 0,1% e só três testavam a deduplicação diretamente — todos em modelos de linguagem generativos, nenhum em classificadores ajustados. O parágrafo de estado da arte de Leo disse isso com clareza e citou Carlini et al. (arXiv:2012.07805) para a extração literal como o dano motivador.

O laboratório de inferência de pertencimento mostra a ideia central que Leo vai estudar: quando um modelo efetivamente memoriza os seus registros de treino (k = 1), o pertencimento é detectável; quando ele generaliza (k maior), o sinal se dissipa.

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

Saída esperada:

```text
k= 1 attack_auc=0.600 best_advantage=0.200
k= 5 attack_auc=0.521 best_advantage=0.073
k=25 attack_auc=0.520 best_advantage=0.060
```

### 1.6 Atividades práticas

1. Escreva o seu tema e, depois, três perguntas candidatas na forma PICO; escolha uma e justifique a viabilidade. 2. Escreva um protocolo de busca e execute-o, registrando as contagens. 3. Monte uma matriz de evidências com dez linhas. Nas perguntas, nomeie o sistema, a intervenção ou fator, a comparação e o desfecho, como faz a pergunta de Leo. Julgue a viabilidade por dados, computação, prazo e ética, e descarte qualquer pergunta que falhe em um deles. Na busca, registre as bases, as expressões, as datas e as contagens em cada etapa, para que outra pessoa possa repeti-la. Na matriz, inclua se cada artigo relata TPR com FPR baixa.

### 1.7 Erros e limites

Cinco erros se repetem, e cada um enfraquece a dissertação desde o início:

- Perguntas amplas demais para serem respondidas numa dissertação; uma pergunta ampla não pode ser respondida no prazo.
- Buscas que param na primeira página de um buscador; uma busca que para cedo perde trabalhos como os três estudos de deduplicação que Leo encontrou.
- Tratar um blog de fornecedor como evidência; um blog de fornecedor é uma alegação a verificar.
- Citar artigos que você não leu, ou fabricar identificadores; identificadores não citados ou inventados abalam a confiança em todas as outras citações.
- Relatar apenas médias para ataques de privacidade; as médias escondem os poucos indivíduos que um ataque identifica com confiança, que é justamente o dano que Leo estuda.

### Exercícios

- **EX001 — PICO.** Escreva uma pergunta PICO sobre defesas contra injeção de prompt. Rubrica: 3 = os quatro elementos específicos e viáveis; 2 = um vago; 1 = dois ausentes; 0 = só o tema.
- **EX002 — Protocolo de busca.** Liste seis elementos de um protocolo de busca documentado. Rubrica: 3 = fontes, expressões, datas, critérios, data da busca, contagens; 2 = quatro; 1 = dois; 0 = nenhum.
- **EX003 — Colunas da matriz.** Nomeie seis colunas de matriz para uma revisão da literatura de segurança de IA e diga por que uma delas importa. Rubrica: 3 = seis pertinentes mais justificativa; 2 = seis; 1 = três; 0 = nenhuma.
- **EX004 — FPR baixa.** Por que relatar a TPR com FPR baixa na inferência de pertencimento? Rubrica: 3 = o dano vem da identificação confiante de alguns indivíduos; as médias o escondem; 2 = parcial; 1 = vago; 0 = errado.
- **EX005 — Ordenação de fontes.** Ordene: blog de fornecedor, preprint do arXiv com código, artigo revisado por pares sem código, framework do NIST — e explique o papel do framework. Rubrica: 3 = ordenação sensata mais o framework como vocabulário, não resultados; 2 = só a ordenação; 1 = vago; 0 = nenhuma.
- **EX006 — Leitura do laboratório.** Que AUC o laboratório de MIA relata com k = 1 e com k = 5? Rubrica: 3 = 0.600 e 0.521 com interpretação; 2 = só os números; 1 = um número; 0 = errado.
- **EX007 — Identificador ausente.** Você não encontra um DOI para um artigo de workshop. Como o cita? Rubrica: 3 = autores, título, veículo/ano, URL de fato usada, sem DOI inventado; 2 = parcial; 1 = vago; 0 = inventa um.

### Síntese

Uma boa dissertação começa com uma pergunta estreita e viável e uma busca que outra pessoa possa repetir. A matriz de evidências transforma a leitura num mapa de lacunas, e a honestidade nas fontes mantém o mapa confiável.

### Continue estudando — capítulo 01 de 08

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Segurança de IA e aprendizado de máquina: seminário avançado

### Objetivos de aprendizagem

Você vai (1) explicar as principais classes de ataque — evasão, envenenamento e backdoors, privacidade (inferência de pertencimento, extração de dados), extração de modelo e injeção de prompt — com os seus modelos de ameaça; (2) explicar as defesas e os seus limites conhecidos; (3) ler e apresentar um artigo de forma crítica num seminário; (4) relacionar resultados ao NIST AI 100-2 E2025, ao OWASP LLM 2025 e ao MITRE ATLAS; e (5) identificar como cada classe de ataque aparece numa implantação real como a da Harbourline.

### 2.1 O formato do seminário

A cada semana, um estudante apresenta um artigo em quinze minutos: alegação, modelo de ameaça, método, resultados e três perguntas críticas. O grupo discute se a evidência sustenta a alegação. O objetivo não é admirar artigos, mas entender exatamente o que eles mostram. A apresentação de Leo sobre Shokri et al., no exemplo resolvido abaixo, segue esse formato, e a sua terceira pergunta passou a fazer parte do seu próprio desenho. Prepare perguntas que um leitor consiga responder a partir do artigo e anote as que ele não responde, pois muitas vezes é ali que estão as lacunas de pesquisa.

### 2.2 Evasão

Exemplos adversariais (Szegedy et al., arXiv:1312.6199) são entradas ligeiramente alteradas para causar erros. O FGSM (Goodfellow et al., arXiv:1412.6572) dá um passo na direção do sinal do gradiente da perda; o PGD (Madry et al., arXiv:1706.06083) itera e projeta de volta no conjunto de perturbações permitido; o treinamento adversarial usa esses exemplos durante o treino. Em texto, mudanças "pequenas" são mais difíceis de definir: trocas por sinônimos ou edições de caracteres podem mudar o sentido. Para a Harbourline, evasão significaria redigir uma nota de sinistro de modo que o classificador a encaminhe errado. O laboratório de brinquedo mostra como a acurácia desaba à medida que o orçamento cresce.

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

Saída esperada:

```text
weights w=(1.795, 1.756) b=-0.080
eps=0.00 accuracy=0.985
eps=0.25 accuracy=0.950
eps=0.50 accuracy=0.840
eps=0.75 accuracy=0.660
eps=1.00 accuracy=0.505
```

### 2.3 Envenenamento e backdoors

Os ataques de envenenamento controlam parte dos dados de treino. O envenenamento de disponibilidade degrada a acurácia de forma ampla; o envenenamento direcionado e o de backdoor (Gu et al., arXiv:1708.06733) mantêm a acurácia limpa enquanto um gatilho provoca o comportamento escolhido. Na Harbourline, um analista de sinistros mal-intencionado que consiga inserir notas no conjunto de treino poderia ensinar ao classificador que uma certa frase encaminha sinistros para aprovação acelerada. As defesas incluem a proveniência dos dados, a filtragem de valores atípicos e a limitação de quem pode contribuir com dados de treino; nenhuma é completa. Pergunte, para qualquer conjunto de dados, quem pode adicionar registros e se isso fica registrado.

### 2.4 Ataques de privacidade

A inferência de pertencimento (Shokri et al., arXiv:1610.05820) decide se um registro estava no treino, usando diferenças na confiança ou na perda do modelo. A extração de dados de treino (Carlini et al., arXiv:2012.07805) recupera sequências literais de modelos generativos. A privacidade diferencial (Abadi et al., arXiv:1607.00133) limita o quanto um único registro pode influenciar o modelo, reduzindo os dois riscos a um custo de utilidade. Para uma seguradora, o próprio pertencimento pode ser sensível ("esta pessoa abriu um sinistro"). A dissertação de Leo estuda o primeiro desses ataques: se a deduplicação reduz o vazamento de pertencimento. Por esse raciocínio, um segurado cuja nota aparece muitas vezes fica mais exposto.

### 2.5 Extração de modelo

A extração de modelo (Tramèr et al., arXiv:1609.02943) constrói uma cópia de um modelo a partir das saídas da sua API. Saídas ricas (vetores completos de probabilidades) a facilitam; arredondar e devolver apenas rótulos a dificultam, mas não a impossibilitam. A extração importa para a propriedade intelectual e porque uma cópia roubada permite ataques de caixa-branca. O laboratório abaixo mostra o efeito da precisão da saída: com a pontuação em precisão total a cópia é exata, com duas casas decimais é quase exata, e com arredondamento para inteiros a cópia concorda em 88% dos rótulos. Na Harbourline, devolver apenas o rótulo de triagem tornaria a extração mais difícil, não impossível.

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

Saída esperada:

```text
output_rounding=None queries=6 max_weight_error=0.000 label_agreement=1.000
output_rounding=2    queries=6 max_weight_error=0.004 label_agreement=0.998
output_rounding=0    queries=6 max_weight_error=0.534 label_agreement=0.882
```

### 2.6 Injeção de prompt e aplicações com LLM

Quando um LLM processa texto não confiável, esse texto pode conter instruções (Greshake et al., arXiv:2302.12173). O OWASP LLM 2025 coloca a injeção de prompt em primeiro lugar e lista riscos relacionados, como divulgação de informações sensíveis, agência excessiva e vazamento do prompt de sistema. O plano futuro da Harbourline — um assistente que lê e-mails de sinistro e redige respostas — herdaria esses riscos. Para um assistente assim, o e-mail de um segurado é texto não confiável que poderia direcionar as minutas ou vazar dados de outros segurados. Esse plano está fora da dissertação de Leo, mas o seminário deve mapeá-lo às entradas da OWASP para que a Harbourline veja quais riscos ele acrescentaria.

### 2.7 Exemplo resolvido (caso sintético da Harbourline)

Leo apresentou Shokri et al. As suas três perguntas críticas: (1) a abordagem de modelos-sombra supõe que o atacante consegue amostrar de uma distribuição de dados semelhante — isso é realista para notas de seguro? (2) os resultados foram relatados sobretudo como precisão/acurácia; qual é a TPR com FPR baixa? (3) quanto do vazamento é explicado pelo sobreajuste? O grupo concluiu que a pergunta (3) era diretamente relevante para a sua dissertação: se a deduplicação ajuda principalmente por reduzir o sobreajuste, a "explicação" é a generalização, não a deduplicação em si — uma explicação concorrente para o Capítulo 4.

### 2.8 Atividades práticas

1. Apresente um artigo usando o formato do seminário. 2. Para cada classe de ataque, escreva um modelo de ameaça de uma linha para um sistema que você conhece. 3. Mapeie o assistente de e-mail planejado pela Harbourline a três entradas do OWASP LLM 2025. Para a apresentação, prepare alegação, modelo de ameaça, método, resultados e três perguntas críticas, como Leo fez. Para os modelos de ameaça, nomeie o conhecimento, o acesso e o objetivo do atacante em cada classe. Para o mapeamento, considere injeção de prompt, divulgação de informações sensíveis e agência excessiva, e diga, para cada uma, o que o assistente poderia fazer de errado e que controle o limitaria.

### 2.9 Erros e limites

Quatro erros se repetem, e cada um leva a um resumo enganoso; confira as suas notas do seminário quanto aos quatro:

- Descrever ataques sem o seu modelo de ameaça; um ataque sem o seu modelo de ameaça não pode ser comparado com uma defesa.
- Supor que resultados do domínio de imagens se transferem diretamente para texto; podem não se transferir, pois pequenas edições de texto podem mudar o sentido.
- Tratar o arredondamento ou a saída só com rótulos como defesa completa contra a extração; o arredondamento dificultou a extração no laboratório, mas não a impediu.
- Ignorar que o próprio pertencimento pode ser sensível; na Harbourline, o simples fato de uma pessoa ter aberto um sinistro pode ser sensível, de modo que a inferência de pertencimento é um dano real.

### Exercícios

- **EX008 — Modelos de ameaça.** Dê um modelo de ameaça de uma linha para evasão, envenenamento por backdoor e inferência de pertencimento. Rubrica: 3 = três com conhecimento, capacidade e objetivo; 2 = dois; 1 = um; 0 = nenhum.
- **EX009 — FGSM vs PGD.** Explique a diferença. Rubrica: 3 = passo único vs passos iterados com projeção; PGD mais forte; 2 = parcial; 1 = vago; 0 = errado.
- **EX010 — Laboratório de extração.** O que acontece com o erro dos pesos e a concordância de rótulos quando as saídas são arredondadas para inteiros, e o que isso implica? Rubrica: 3 = erro 0.534, concordância 0.882; a precisão da saída limita a fidelidade, mas resta uma cópia útil; 2 = só os números; 1 = vago; 0 = errado.
- **EX011 — Dano à seguradora.** Por que o pertencimento pode ser sensível para a Harbourline? Rubrica: 3 = revela que uma pessoa abriu um sinistro, possivelmente com detalhes de saúde ou de perdas; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX012 — Cenário de backdoor.** Descreva (em nível de desenho) um risco de backdoor para o classificador de sinistros e dois controles. Rubrica: 3 = notas-gatilho inseridas por alguém de dentro; proveniência/controle de acesso e testes de gatilho/valores atípicos; 2 = um controle; 1 = vago; 0 = detalhe danoso.
- **EX013 — Mapeamento OWASP.** Mapeie o assistente de e-mail a três entradas do OWASP LLM 2025. Rubrica: 3 = por exemplo, LLM01, LLM02, LLM06 com razões; 2 = só os IDs; 1 = uma; 0 = nenhuma.
- **EX014 — Perguntas de seminário.** Escreva três perguntas críticas para um artigo de defesa à sua escolha. Rubrica: 3 = três sobre modelo de ameaça, ataque adaptativo, métricas/custos; 2 = duas; 1 = uma; 0 = nenhuma.

### Síntese

O seminário cria fluência nas classes de ataque e na leitura crítica. Cada classe tem um modelo de ameaça, um dano típico e defesas com limites conhecidos — e as explicações concorrentes que você descobre na discussão se tornam perguntas de pesquisa.

### Continue estudando — capítulo 02 de 08

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Desenho do estudo, ética e reprodutibilidade

### Objetivos de aprendizagem

Você vai (1) escolher um desenho (experimento controlado, estudo observacional, estudo de caso) adequado à pergunta; (2) definir variáveis, controles, aleatorização e tamanho da amostra; (3) planejar o tratamento dos dados e a ética para dados pessoais ou sensíveis; (4) tornar o estudo reprodutível desde o início; e (5) documentar o plano para que um orientador possa aprová-lo.

### 3.1 Escolha de um desenho

A maioria dos projetos de mestrado em segurança de IA são **experimentos controlados**: você muda um fator (deduplicação ligada/desligada), mantém os outros fixos e mede os desfechos. Estudos **observacionais** analisam dados existentes sem intervir (por exemplo, registros de tentativas de injeção de prompt contra um assistente implantado) e precisam se preocupar com confusão (confounding). **Estudos de caso** examinam um sistema em profundidade e são úteis quando experimentos são impossíveis, mas sustentam uma generalização mais fraca. Escolha o desenho mais forte que você consiga executar de forma ética e dentro do prazo. A pergunta de Leo compara condições que ele pode controlar, então um experimento controlado é adequado.

### 3.2 Variáveis e controles

Para Leo: a *variável independente* é o tratamento do conjunto de treino (original, deduplicado exato, deduplicado aproximado). As *variáveis dependentes* são a TPR da inferência de pertencimento com FPR de 1%, a AUC e o macro-F1 do classificador. As *variáveis controladas* incluem a arquitetura do modelo, as épocas, a taxa de aprendizado, as sementes aleatórias e a partição de avaliação. Aleatorize quais registros vão para o treino e quais ficam reservados, para que membros e não membros venham da mesma distribuição — caso contrário, um ataque pode detectar a mudança de distribuição em vez do pertencimento, uma armadilha conhecida. Use várias sementes e relate a variabilidade. Estime o tamanho da amostra a partir de um piloto (Capítulo 5).

### 3.3 Ética e proteção de dados

Quando os dados dizem respeito a pessoas, aplique os princípios de proteção de dados: base legal, limitação da finalidade, minimização, limitação da conservação e segurança. O GDPR (o regulamento geral de proteção de dados) se aplica na UE; outras jurisdições têm leis semelhantes. Prefira dados sintéticos que preservem as propriedades de que você precisa; se dados reais forem essenciais, obtenha a aprovação do comitê de ética da sua instituição e do controlador dos dados, pseudonimize, restrinja o acesso e defina datas de exclusão. Ataques de privacidade sobre dados reais criam exatamente o dano que você estuda; execute-os apenas em cópias sob acordo e nunca publique registros recuperados. Se o seu projeto envolver pessoas (anotadores, participantes de questionários), você precisa de consentimento informado.

> **Nota para o leitor brasileiro.** No Brasil, o tratamento de dados pessoais em pesquisa é regido pela Lei Geral de Proteção de Dados Pessoais (LGPD, Lei nº 13.709/2018), fiscalizada pela Autoridade Nacional de Proteção de Dados (ANPD); a lei tem disposições específicas para órgãos de pesquisa, mas elas não dispensam a minimização, a pseudonimização e a aprovação ética descritas acima.

### 3.4 Reprodutível por desenho

Prepare desde o primeiro dia: um repositório com controle de versão; um ambiente fixado; arquivos de configuração em vez de parâmetros embutidos no código; sementes fixas; um único comando para executar cada experimento; registros gravados em formato legível por máquina; e um cartão de dados (data card) que descreva a proveniência e o processamento (Gebru et al., arXiv:1803.09010). O programa de reprodutibilidade da NeurIPS (Pineau et al., arXiv:2003.12206) oferece uma lista de verificação que vale adotar. Embutir a reprodutibilidade desde o início sai muito mais barato do que acrescentá-la depois. O desenho de Leo lista desde o início o repositório, um arquivo de travamento (lock file) e uma interface `run.py --config`, o que tornou simples as suas reexecuções posteriores.

### 3.5 Exemplo resolvido (caso sintético da Harbourline)

O documento de desenho de Leo especifica um experimento controlado com três condições × cinco sementes. Dados: 20.000 notas de sinistro sintéticas geradas a partir de modelos (templates) com duplicação controlada (8% de duplicatas exatas, 6% de quase-duplicatas), de modo que a verdade de referência sobre a duplicação é conhecida. Membros e não membros são sorteados por partição aleatória do mesmo conjunto. A seção de ética registra que nenhum dado real de segurado é usado, que o encarregado de proteção de dados da Harbourline revisou o plano e que o gerador sintético será publicado. A seção de reprodutibilidade lista o repositório, o arquivo de travamento do ambiente e uma interface `run.py --config`.

O laboratório de estatística mostra por que estão previstas cinco sementes: os resultados por semente variam mesmo quando nada muda além da semente.

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

Saída esperada:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

### 3.6 Atividades práticas

1. Escreva o seu desenho com variáveis, controles e aleatorização. 2. Redija uma seção de ética e proteção de dados. 3. Crie o esqueleto do repositório com arquivos de configuração e uma política de sementes. Use o desenho de Leo como modelo: nomeie as variáveis independentes, dependentes e controladas, e diga como membros e não membros são sorteados do mesmo conjunto. No texto de ética, diga que dados são usados, quem revisou o plano e o que será publicado. No repositório, inclua arquivos de configuração, um arquivo de travamento, uma política de sementes e um único comando por experimento. Peça ao seu orientador que revise os três.

### 3.7 Erros e limites

Quatro erros se repetem, e cada um compromete o resultado; confira o seu desenho quanto aos quatro:

- Membros e não membros sorteados de distribuições diferentes; isso deixa o ataque detectar a mudança em vez do pertencimento.
- Uma semente por condição; uma única semente não mostra a variabilidade que o Laboratório S torna visível.
- Usar dados pessoais reais quando dados sintéticos bastariam; dados pessoais reais criam o dano estudado quando dados sintéticos serviriam, como servem as notas sintéticas de Leo.
- Caminhos e parâmetros embutidos no código que tornam as reexecuções impossíveis; eles fazem as reexecuções falharem para qualquer outra pessoa, inclusive os examinadores.

### Exercícios

- **EX015 — Escolha do desenho.** Para "assistentes implantados recebem tentativas de injeção, e de que tipos?", escolha um desenho e justifique. Rubrica: 3 = estudo observacional de registros autorizados, com notas sobre confusão/consentimento; 2 = só o desenho; 1 = pouco adequado; 0 = nenhum.
- **EX016 — Variáveis.** Liste a variável independente, a dependente e três variáveis controladas para um experimento sobre uma defesa contra evasão. Rubrica: 3 = todas corretas; 2 = lacuna menor; 1 = lacuna grave; 0 = nenhuma.
- **EX017 — Armadilha da distribuição.** Explique por que membros e não membros devem vir da mesma distribuição. Rubrica: 3 = caso contrário o ataque detecta a mudança, inflando os resultados; 2 = parcial; 1 = vago; 0 = errado.
- **EX018 — Proteção de dados.** Nomeie quatro princípios de proteção de dados que se aplicam a um estudo de ataque de privacidade. Rubrica: 3 = quatro corretos; 2 = três; 1 = um ou dois; 0 = nenhum.
- **EX019 — Leitura do laboratório.** No laboratório de estatística, qual é a amplitude das taxas por semente e a média? Rubrica: 3 = 0.105–0.145, média 0.125, dp 0.017; 2 = dois dos três; 1 = um; 0 = errado.
- **EX020 — Preparação para a reprodutibilidade.** Liste cinco coisas a preparar antes do primeiro experimento. Rubrica: 3 = cinco entre repositório, ambiente fixado, configurações, sementes, comando único, registros, cartão de dados; 2 = quatro; 1 = duas; 0 = nenhuma.

### Síntese

O desenho determina o que você pode concluir. Variáveis controladas, amostragem pareada de membros e não membros, várias sementes, tratamento ético dos dados e reprodutibilidade embutida desde o início são o que permite a um projeto curto produzir uma resposta crível.

### Continue estudando — capítulo 03 de 08

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Segurança de IA e aprendizado de máquina: explicações concorrentes

### Objetivos de aprendizagem

Você vai (1) listar explicações alternativas para um efeito de segurança observado; (2) desenhar ablações e controles que as separem; (3) reconhecer fatores de confusão típicos dos experimentos de segurança de IA (sobreajuste, vazamento de dados, mudança de distribuição, artefatos de avaliação, ataques fracos); (4) usar os laboratórios de envenenamento e de evasão para raciocinar sobre mecanismos; e (5) enunciar conclusões no nível que a evidência sustenta.

### 4.1 Por que as explicações concorrentes importam

Um efeito observado — "a deduplicação reduziu a vantagem da inferência de pertencimento" — pode ter várias causas. A deduplicação poderia reduzir especificamente a memorização de registros repetidos; poderia simplesmente reduzir o tamanho efetivo do conjunto de treino e, com isso, alterar o sobreajuste; poderia mudar o equilíbrio entre classes; ou o ataque poderia ser mais fraco contra o novo modelo por razões que nada têm a ver com privacidade. Uma dissertação que nomeia e testa essas alternativas é muito mais forte do que uma que apenas relata o efeito. A discussão no seminário de Leo levantou a explicação do sobreajuste antes que ele tivesse qualquer dado.

### 4.2 Um catálogo de alternativas em segurança de IA

Seis alternativas se repetem. *Generalização vs. mecanismo específico*: o vazamento de privacidade se correlaciona com a diferença entre treino e teste, então compare os tratamentos com diferenças de generalização equiparadas, ou inclua um controle que mude o tamanho dos dados sem deduplicar. *Vazamento*: duplicatas entre as partições de treino e de teste inflam a acurácia e confundem as métricas de privacidade (Kapoor e Narayanan, arXiv:2207.07048). *Mudança de distribuição*: se membros e não membros diferem na distribuição, os ataques detectam a mudança, não o pertencimento. *Ataque fraco ou mal ajustado*: uma defesa "funciona" porque o ataque não foi adaptado (Athalye et al., arXiv:1802.00420); use um ataque mais forte ou calibrado como controle. *Artefatos de avaliação*: escolha de métrica ou limiares ajustados no conjunto de teste. *Aleatoriedade*: uma única semente pode produzir um efeito aparente.

### 4.3 Ablações e controles

Uma *ablação* remove ou varia um componente para ver a sua contribuição. O plano de Leo acrescenta uma quarta condição: a *remoção aleatória* do mesmo número de registros que a deduplicação removeria. Se a remoção aleatória der o mesmo ganho de privacidade, a explicação é o tamanho do conjunto de dados; se a deduplicação der mais, as duplicatas importam. Ele também acrescenta um ataque de controle calibrado com modelos de referência, sabidamente mais forte com FPR baixa do que um simples limiar de confiança. Escreva o resultado esperado de cada condição antes de executar.

### 4.4 Raciocinar sobre mecanismos com os laboratórios

O laboratório de envenenamento oferece um contraste nítido. Inverter os rótulos de até 40% de uma classe quase não altera um modelo de centroide mais próximo (0.965 → 0.945), porque os centroides fazem a média de muitos pontos; um backdoor que usa uma característica-gatilho separada atinge 98% de sucesso do ataque com 80 pontos, enquanto a acurácia limpa fica em 0.968. O *mecanismo* — uma direção de característica nova, sem outro uso — explica por que as métricas limpas não o percebem. Uma explicação concorrente ("o modelo é simplesmente impreciso") é descartada pela acurácia limpa inalterada. Para Leo, a analogia é que registros duplicados podem dar ao modelo uma via específica para memorizá-los.

```python
"""Lab P: label-flip poisoning and a backdoor trigger on a toy nearest-centroid
classifier (synthetic data, stdlib only). Teaching model only."""
import random
rng = random.Random(11)
def point(label, trigger=False):
    cx = 1.0 if label else -1.0
    x = [rng.gauss(cx, 0.8), rng.gauss(cx, 0.8), 0.0]
    if trigger: x[2] = 5.0          # third feature is the 'trigger'
    return x, label
clean = [point(i % 2) for i in range(400)]
test = [point(i % 2) for i in range(400)]
def fit(data):
    c = {}
    for lab in (0, 1):
        pts = [x for x, y in data if y == lab]
        c[lab] = [sum(p[i] for p in pts)/len(pts) for i in range(3)]
    return c
def pred(c, x):
    d = {k: sum((x[i]-v[i])**2 for i in range(3)) for k, v in c.items()}
    return min(d, key=d.get)
def accuracy(c, data): return sum(pred(c, x) == y for x, y in data)/len(data)
print("label-flip poisoning (flip a fraction of class-1 labels to 0):")
for frac in (0.0, 0.1, 0.2, 0.3, 0.4):
    data = [(x, y) for x, y in clean]; ones = [i for i, (x, y) in enumerate(data) if y == 1]
    for i in ones[:int(frac*len(ones))]: data[i] = (data[i][0], 0)
    print(f"  flipped={frac:.1f} clean_test_accuracy={accuracy(fit(data), test):.3f}")
print("backdoor: add n triggered class-1 points labelled 0")
trig_test = [point(1, trigger=True) for _ in range(200)]
for n in (0, 10, 40, 80):
    data = clean + [(point(1, trigger=True)[0], 0) for _ in range(n)]
    c = fit(data)
    asr = sum(pred(c, x) == 0 for x, _ in trig_test)/len(trig_test)
    print(f"  poison_points={n:3d} clean_accuracy={accuracy(c, test):.3f} attack_success={asr:.3f}")
```

Saída esperada:

```text
label-flip poisoning (flip a fraction of class-1 labels to 0):
  flipped=0.0 clean_test_accuracy=0.965
  flipped=0.1 clean_test_accuracy=0.965
  flipped=0.2 clean_test_accuracy=0.953
  flipped=0.3 clean_test_accuracy=0.950
  flipped=0.4 clean_test_accuracy=0.945
backdoor: add n triggered class-1 points labelled 0
  poison_points=  0 clean_accuracy=0.965 attack_success=0.075
  poison_points= 10 clean_accuracy=0.963 attack_success=0.145
  poison_points= 40 clean_accuracy=0.963 attack_success=0.685
  poison_points= 80 clean_accuracy=0.968 attack_success=0.980
```

### 4.5 Exemplo resolvido (caso sintético da Harbourline)

Nos dados do piloto, sob o ataque calibrado, a deduplicação reduziu a TPR com FPR de 1% de 6,1% para 3,4%. A remoção aleatória do mesmo número de registros a reduziu para 5,6%. A diferença entre a deduplicação e a remoção aleatória (2,2 pontos) é a parte plausivelmente atribuível à remoção das duplicatas; os 0,5 ponto restantes são explicados pelo tamanho. O ataque simples por limiar de confiança ficou perto do seu piso em todas as condições (o piloto do Capítulo 5 descreve isso), de modo que só o ataque calibrado conseguiu separá-las. A frase de conclusão de Leo mudou de "a deduplicação protege a privacidade" para "a maior parte da redução observada no vazamento de pertencimento é atribuível à remoção de registros duplicados, e não ao conjunto de treino menor, sob o ataque avaliado".

### 4.6 Atividades práticas

1. Liste cinco explicações concorrentes para o seu resultado esperado. 2. Desenhe uma ablação e um controle para cada uma das duas mais plausíveis. 3. Reescreva a sua conclusão esperada no nível de evidência que você terá. Para a lista, use o catálogo acima e acrescente qualquer explicação específica do seu sistema. Para as ablações, mude uma coisa de cada vez e diga que resultado sustentaria cada explicação. Para a conclusão, escreva a frase que você conseguiria defender se o efeito principal aparecesse e compare-a com a frase revisada de Leo, que nomeia o ataque e o que foi descartado.

### 4.7 Erros e limites

Quatro erros se repetem, e cada um deixa uma explicação concorrente sobreviver; confira o seu plano quanto aos quatro:

- Relatar um efeito sem testar alternativas; um efeito sem alternativas testadas pode ser tamanho, mudança de distribuição ou acaso.
- Ablações que mudam várias coisas de uma vez; uma ablação assim não consegue atribuir o efeito.
- Usar apenas um ataque fraco para avaliar uma defesa de privacidade; um ataque fraco pode fazer qualquer defesa parecer boa, e é por isso que Leo acrescentou o ataque calibrado.
- Afirmar um mecanismo só a partir de correlação; uma correlação, como o vazamento acompanhar a duplicação, não mostra por si só um mecanismo sem controles como a remoção aleatória.

### Exercícios

- **EX021 — Alternativas.** Liste quatro explicações concorrentes para "um guardrail reduziu o sucesso de jailbreaks". Rubrica: 3 = quatro plausíveis (conjunto de ataques mais fraco, recusas disparadas em excesso, mudança de distribuição, artefato de semente/juiz); 2 = três; 1 = uma ou duas; 0 = nenhuma.
- **EX022 — Ablação.** Desenhe o controle de remoção aleatória e explique o que cada resultado significaria. Rubrica: 3 = mesma contagem removida ao acaso; ganho igual → tamanho, ganho maior → duplicatas; 2 = só o desenho; 1 = vago; 0 = nenhum.
- **EX023 — Mecanismo no laboratório.** Por que a inversão de rótulos quase não muda o modelo de centroide, enquanto o backdoor tem sucesso? Rubrica: 3 = os centroides fazem a média de muitos pontos vs o gatilho usa uma direção de característica nova, não afetada pelos dados limpos; 2 = parcial; 1 = vago; 0 = errado.
- **EX024 — Números do laboratório.** Relate a acurácia limpa e o sucesso do ataque com 80 pontos envenenados. Rubrica: 3 = 0.968 e 0.980; 2 = um; 1 = aproximado; 0 = errado.
- **EX025 — Ataque mais forte.** Por que incluir um ataque calibrado como controle? Rubrica: 3 = garante que o efeito da defesa não é artefato de um ataque fraco, sobretudo com FPR baixa; 2 = parcial; 1 = vago; 0 = errado.
- **EX026 — Nível da conclusão.** Reescreva "a dedup resolve a privacidade" no nível de evidência de 4.5. Rubrica: 3 = atribui uma parcela, nomeia o ataque e as condições; 2 = parcial; 1 = ainda exagera; 0 = inalterada.

### Síntese

Efeitos precisam de explicações, e explicações precisam de testes. Ablações, controles e ataques mais fortes separam mecanismos de artefatos, e as conclusões resultantes são mais estreitas, porém defensáveis.

### Continue estudando — capítulo 04 de 08

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Proposta e piloto

### Objetivos de aprendizagem

Você vai (1) escrever uma proposta de dissertação com pergunta, contexto, desenho, plano de análise, ética, riscos e cronograma; (2) executar um piloto para testar a viabilidade e estimar a variabilidade; (3) calcular tamanhos de amostra; (4) revisar o plano a partir da evidência do piloto; e (5) obter aprovação com um registro claro das decisões.

### 5.1 A proposta

Uma proposta de mestrado tem tipicamente de 3.000 a 6.000 palavras. Seções: **pergunta e motivação** (um parágrafo cada); **contexto**, a partir da sua matriz de evidências; **desenho** (Capítulo 3), incluindo explicações concorrentes e ablações (Capítulo 4); **plano de análise**, com desfechos primários e secundários e a estatística que você vai usar; **ética e proteção de dados**; **riscos** (técnicos, de dados, de cronograma) com mitigações; **cronograma** com marcos; e **contribuição esperada**, enunciada com modéstia. O plano de análise é a parte mais negligenciada — escreva-o agora, antes dos dados, para que escolhas posteriores não possam ser guiadas pelos resultados. A proposta de Leo seguiu esse roteiro.

### 5.2 O piloto

Um piloto executa o pipeline completo em pequena escala. Objetivos: confirmar que o código funciona de ponta a ponta, medir o tempo de execução, medir a variabilidade do desfecho primário, verificar que o ataque e as métricas se comportam de forma sensata (por exemplo, que o modelo sem defesa é atacável) e encontrar surpresas. Resultados de piloto não são testes de hipótese; não os relate como achados e mantenha os dados finais de teste fora do piloto. O piloto de Leo encontrou um efeito piso e uma falha no gerador. Registre os dois no registro de decisões.

### 5.3 Tamanho da amostra e poder

Para taxas, a aproximação normal n ≈ z² p(1−p)/h² dá o número de tentativas necessário para uma semiamplitude h do intervalo de confiança. Para comparações entre condições, a análise de poder pergunta quantas repetições são necessárias para detectar uma diferença d com probabilidade (poder) 0,8 a um nível de significância de 0,05; em desenhos pareados, o que importa é a variância das *diferenças*. Com poucas sementes (o típico em aprendizado de máquina), relate intervalos sobre as sementes e sobre os itens de avaliação, em vez de depender de um único teste de significância. O piloto de Leo mostrou cerca de 0,8 ponto de variação entre sementes, o que, junto com o bootstrap sobre os registros, tornou cinco sementes adequadas. Use a variação que você de fato observa, não um palpite.

### 5.4 Revisão do plano

Pilotos costumam mudar alguma coisa: um ataque fraco demais para separar as condições, uma avaliação que demora demais, uma métrica com efeito piso (todas as condições perto de zero). Registre cada mudança num registro de decisões, com a razão. Orientadores e examinadores reagem bem a uma proposta que mostra ter aprendido com o seu piloto. O registro de Leo anota duas mudanças vindas do piloto: a substituição do ataque limitado pelo piso por um ataque calibrado e a correção dos modelos que produziam notas quase idênticas entre classes. Cada uma tem data e razão. Mantenha o registro junto com a proposta para que os examinadores possam acompanhar a evolução do plano.

### 5.5 Exemplo resolvido (caso sintético da Harbourline)

O piloto de Leo usou 2.000 registros e duas sementes. Levou 40 minutos por execução, então o plano completo (20.000 registros, quatro condições, cinco sementes) exige cerca de 130 horas de computação — viável no cluster do laboratório. O ataque simples por limiar de confiança produziu TPR com FPR de 1% entre 1% e 2% em todas as condições: um efeito piso. Ele o substituiu por um ataque calibrado com modelos de referência, que separou as condições. A variabilidade entre sementes foi de cerca de 0,8 ponto, então cinco sementes mais bootstrap sobre os registros foram consideradas adequadas. Ele também descobriu que dois modelos geravam notas quase idênticas entre classes, introduzindo ruído de rótulo; corrigiu o gerador e registrou a mudança.

O laboratório de evasão oferece um exemplo de varredura em piloto: antes de escolher um orçamento de perturbação para o estudo principal, varra vários para descobrir onde o efeito é mensurável, em vez de estar no piso ou no teto.

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

Saída esperada:

```text
weights w=(1.795, 1.756) b=-0.080
eps=0.00 accuracy=0.985
eps=0.25 accuracy=0.950
eps=0.50 accuracy=0.840
eps=0.75 accuracy=0.660
eps=1.00 accuracy=0.505
```

### 5.6 Atividades práticas

1. Escreva o seu plano de análise com desfechos primários e secundários. 2. Execute um piloto e preencha um registro de decisões. 3. Calcule o tamanho da amostra para o seu desfecho primário. No plano de análise, nomeie o desfecho primário, como a TPR com FPR de 1%, e os secundários, com a estatística de cada um. No piloto, execute o pipeline inteiro em pequena escala e registre cada mudança com a sua razão, como Leo fez. No tamanho da amostra, use a fórmula acima com a variação que o seu piloto observou e diga se o seu orçamento de computação o permite.

### 5.7 Erros e limites

Quatro erros se repetem, e cada um enfraquece o estudo; confira a sua proposta quanto aos quatro:

- Propostas sem plano de análise; sem ele, escolhas posteriores podem ser guiadas pelos resultados.
- Relatar resultados de piloto como achados; não são achados, porque o piloto não foi desenhado nem dimensionado para testar hipóteses.
- Usar dados de teste no piloto; dados de teste usados num piloto deixam de ser inéditos.
- Ignorar efeitos piso ou teto; um efeito piso, como o do ataque simples de Leo, entre 1% e 2% em todas as condições, esconde diferenças reais.

### Exercícios

- **EX027 — Seções da proposta.** Liste oito seções da proposta. Rubrica: 3 = oito corretas; 2 = seis; 1 = três; 0 = nenhuma.
- **EX028 — Objetivos do piloto.** Dê quatro objetivos de um piloto. Rubrica: 3 = pipeline funciona, tempo, variabilidade, sanidade das métricas/surpresas; 2 = três; 1 = um ou dois; 0 = nenhum.
- **EX029 — Tamanho da amostra.** Calcule o número de tentativas para uma taxa perto de 5% com semiamplitude de 1 ponto a 95%. Rubrica: 3 = ≈1.825 com a fórmula; 2 = deslize aritmético; 1 = só a fórmula; 0 = nenhum.
- **EX030 — Efeito piso.** O que é um efeito piso e como Leo o corrigiu? Rubrica: 3 = todas as condições perto do mínimo, de modo que as diferenças ficam invisíveis; ataque calibrado mais forte; 2 = só a definição; 1 = vago; 0 = errado.
- **EX031 — Varredura no laboratório.** No laboratório de evasão, que valores de eps evitam o piso e o teto para comparar defesas? Rubrica: 3 = em torno de 0.5–0.75 (0.840, 0.660), com razões; 2 = só os valores; 1 = vago; 0 = errado.
- **EX032 — Registro de decisões.** Escreva duas entradas do registro de decisões do piloto de Leo. Rubrica: 3 = data, mudança, razão e efeito nas duas; 2 = uma; 1 = vago; 0 = nenhuma.

### Síntese

A proposta fixa o que você vai fazer e como vai analisar; o piloto mostra se você consegue. Revisões registradas com as suas razões transformam surpresas em evidência de um processo cuidadoso.

### Continue estudando — capítulo 05 de 08

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Coleta e análise de dados

### Objetivos de aprendizagem

Você vai (1) executar os experimentos principais exatamente como planejado e registrar os desvios; (2) verificar a qualidade dos dados antes da análise; (3) calcular os desfechos primários com incerteza (intervalos de Wilson, bootstrap, variação entre sementes); (4) analisar comparações pareadas e desfechos secundários; e (5) apresentar os resultados em tabelas e figuras que respondam à pergunta de pesquisa.

### 6.1 Execução do estudo principal

Congele o código num commit marcado com tag, trave os arquivos de configuração e execute as condições em ordem intercalada ou aleatorizada, para que problemas dependentes do tempo (um nó ficando lento, uma atualização de biblioteca) não coincidam com uma única condição. Cada execução grava um registro: condição, semente, hash da configuração, horários de início e fim, métricas e caminhos para as saídas brutas. Mantenha um registro de desvios, como no piloto. As execuções de Leo foram intercaladas por condição e semente, e o seu registro de desvios anotou a execução ausente da semente 4 e a sua reexecução. Confira o registro antes da análise, não depois.

### 6.2 Verificações de qualidade dos dados

Antes de calcular qualquer coisa, verifique: todas as execuções esperadas estão presentes? As verificações-canário passam (o modelo sem defesa precisa ser atacável; um modelo treinado com rótulos embaralhados deve ter desempenho de acaso)? Há duplicatas entre as partições? Os valores das métricas estão em faixas plausíveis? Essas verificações pegam defeitos que, de outro modo, virariam "achados". As verificações de Leo encontraram uma execução ausente da semente 4, que foi reexecutada e registrada antes da análise. Escreva as verificações como um script, para que rodem sempre da mesma forma, e guarde a saída delas junto com os resultados.

### 6.3 Análise primária

Calcule o desfecho primário por condição, com intervalos. Para taxas, use intervalos de Wilson; para métricas calculadas como média sobre itens, faça bootstrap sobre os itens; relate a variação entre sementes separadamente. Para comparações pareadas (os mesmos registros ou prompts em todas as condições), faça bootstrap da *diferença*. Siga o plano de análise; rotule qualquer análise extra como exploratória. Quando fizer várias comparações, corrija para a multiplicidade ou apresente-as como exploratórias. O laboratório abaixo demonstra as três ferramentas. Com 3 sucessos em 20, o intervalo de Wilson vai de 5% a 36%: uma amostra tão pequena não sustenta uma alegação precisa. As taxas por semente mostram a dispersão de uma semente para outra. O bootstrap pareado estima a redução proporcionada por uma defesa sobre os mesmos prompts, com um intervalo que exclui o zero.

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

Saída esperada:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

### 6.4 Desfechos secundários e custos

Toda melhoria de segurança tem custos: acurácia, latência, recusas de pedidos legítimos, computação, manutenibilidade. Relate-os sobre os mesmos itens. Uma defesa de privacidade que reduz o vazamento pela metade, mas derruba o macro-F1 em 10 pontos, é uma proposta diferente de uma que custa 1 ponto. Faça o gráfico do compromisso (por exemplo, TPR com FPR de 1% versus macro-F1) para todas as condições. O resultado de Leo é do segundo tipo: a dedup aproximada reduziu a TPR com FPR de 1% a menos da metade, para 4,2%, enquanto o macro-F1 caiu menos de um ponto. Relate os dois números juntos, com intervalos, para que os leitores possam pesar o compromisso por si mesmos.

### 6.5 Exemplo resolvido (caso sintético da Harbourline)

Os resultados principais de Leo (sintéticos, cinco sementes, 20.000 registros): a TPR com FPR de 1% sob o ataque calibrado foi de 9,8% (original), 7,9% (remoção aleatória), 5,1% (dedup exata) e 4,2% (dedup aproximada). A diferença pareada entre a dedup aproximada e a remoção aleatória foi de 3,7 pontos (IC de 95% por bootstrap: 2,6–4,9). O macro-F1 caiu de 0,912 para 0,905 com a dedup aproximada. As verificações de qualidade dos dados encontraram uma execução ausente da semente 4, reexecutada e registrada. Uma análise exploratória, rotulada como tal, mostrou o vazamento concentrado em registros que tinham aparecido três ou mais vezes. O achado exploratório sobre registros vistos três ou mais vezes é uma hipótese para trabalhos futuros, não um resultado confirmado.

### 6.6 Atividades práticas

1. Escreva uma lista de verificação de qualidade dos dados para o seu estudo e execute-a. 2. Produza a tabela primária com intervalos. 3. Faça o gráfico do compromisso entre segurança e utilidade. Na lista de verificação, inclua todas as execuções esperadas, verificações-canário, duplicatas entre partições e faixas plausíveis, e execute-a antes de qualquer análise. Na tabela primária, dê o desfecho de cada condição com um intervalo e o número de sementes. No gráfico, coloque a métrica de privacidade contra o macro-F1 para cada condição, para que um leitor veja o compromisso de relance, como faz a figura de Leo.

### 6.7 Erros e limites

Quatro erros se repetem: executar todas as sementes de uma condição antes de outra; analisar antes das verificações de qualidade; misturar resultados exploratórios e confirmatórios; e relatar ganhos de segurança sem os custos. Cada erro enviesa os resultados ou esconde custos. Executar primeiro as sementes de uma condição deixa problemas dependentes do tempo coincidirem com ela. Analisar antes das verificações de qualidade transforma defeitos em achados, como uma semente ausente. Misturar resultados exploratórios e confirmatórios exagera a certeza. Relatar ganhos sem custos esconde compromissos, como a queda no macro-F1 que Leo relatou. Confira a sua análise quanto aos quatro.

### Exercícios

- **EX033 — Intercalação.** Por que intercalar as condições durante as execuções? Rubrica: 3 = impede que problemas dependentes do tempo se confundam com as condições; 2 = parcial; 1 = vago; 0 = errado.
- **EX034 — Verificações de qualidade.** Liste quatro verificações de qualidade dos dados. Rubrica: 3 = completude, canários, duplicatas entre partições, faixas plausíveis; 2 = três; 1 = uma ou duas; 0 = nenhuma.
- **EX035 — Leitura do laboratório.** Quais são a ASR de base, a ASR com defesa e o intervalo da redução no laboratório de estatística? Rubrica: 3 = 0.350, 0.190, [0.120, 0.203]; 2 = dois; 1 = um; 0 = errado.
- **EX036 — Pareado vs não pareado.** Por que fazer bootstrap da diferença sobre itens compartilhados, em vez de comparar dois intervalos separados? Rubrica: 3 = a dificuldade dos itens se cancela; inferência mais estreita e correta; 2 = parcial; 1 = vago; 0 = errado.
- **EX037 — Custos.** Nomeie quatro custos a relatar para uma defesa de segurança. Rubrica: 3 = acurácia/utilidade, latência, recusas indevidas, computação/manutenção; 2 = três; 1 = um ou dois; 0 = nenhum.
- **EX038 — Exploratório.** Como Leo deve relatar o achado das "três ou mais aparições"? Rubrica: 3 = rotulado como exploratório, hipótese para trabalhos futuros, não confirmatório; 2 = parcial; 1 = relatado como resultado principal; 0 = omitido sem razão.

### Síntese

A análise é onde o desenho cuidadoso compensa: execuções intercaladas, verificações de qualidade, intervalos e comparações pareadas transformam registros brutos numa resposta defensável, e os custos tornam a resposta útil.

### Continue estudando — capítulo 06 de 08

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Escrita da dissertação e limitações

### Objetivos de aprendizagem

Você vai (1) estruturar uma dissertação de modo que cada capítulo sirva à pergunta de pesquisa; (2) escrever resultados e discussão que separem achados de interpretação; (3) escrever uma seção de limitações organizada por tipo de validade; (4) tratar com responsabilidade, na escrita, os detalhes sensíveis para a segurança; e (5) produzir um apêndice de artefatos que sustente a reprodução.

### 7.1 Estrutura

Uma estrutura comum: introdução (problema, pergunta, resumo da contribuição); contexto e trabalhos relacionados (a partir da sua matriz); método (desenho, dados, ataques, métricas, plano de análise); resultados (primários, secundários e exploratórios claramente rotulados); discussão (interpretação, explicações concorrentes, implicações); limitações; conclusão; referências; apêndices (artefatos, tabelas extras). Escreva o método de modo que um colega possa repeti-lo; escreva os resultados de modo que um leitor encontre a resposta à pergunta de pesquisa numa única tabela. A dissertação de Leo responde à sua pergunta numa tabela de TPR com FPR de 1% e macro-F1 para as quatro condições.

### 7.2 Achados versus interpretação

Os resultados dizem o que foi medido: "a deduplicação aproximada reduziu a TPR com FPR de 1% de 9,8% para 4,2%". A discussão interpreta: "isso sugere que os registros duplicados respondem por boa parte do vazamento, em linha com trabalhos sobre memorização em modelos de linguagem". Mantenha-os separados. Na discussão, volte às explicações concorrentes e diga quais as suas ablações descartaram. Leo moveu dos resultados para a discussão uma recomendação de que as seguradoras deveriam deduplicar, e a atenuou. Leia cada frase dos resultados e pergunte se ela relata uma medição; se ela explica ou recomenda, mova-a.

### 7.3 Limitações por tipo de validade

Organize as limitações pelos quatro tipos de validade. *Interna*: algo além do tratamento poderia explicar o efeito? (por exemplo, artefatos do gerador sintético.) *De construto*: as métricas medem a propriedade? (por exemplo, a TPR com FPR de 1% sob uma única família de ataques captura apenas parte do risco de privacidade.) *Externa*: o resultado se transfere? (por exemplo, uma única arquitetura de modelo, notas sintéticas, só em inglês.) *De conclusão*: a estatística é adequada? (por exemplo, cinco sementes.) Para cada uma, diga o que você fez e o que resta. Limitações escritas assim são um ponto forte; os examinadores desconfiam de dissertações que não declaram nenhuma.

### 7.4 Escrever sobre ataques com responsabilidade

Descreva os ataques no nível necessário para a compreensão e a reprodução em ambientes de pesquisa, cite os artigos originais e evite publicar detalhes operacionais dirigidos a sistemas em produção identificados pelo nome. Nunca inclua dados pessoais recuperados. Se você encontrou uma vulnerabilidade num produto real, siga a divulgação coordenada antes de a dissertação ser publicada. Rotule dados e organizações sintéticos como ficção em todo o texto. A dissertação de Leo descreve o ataque calibrado citando a sua fonte e a configuração usada, sem nenhum registro recuperado. Peça ao seu orientador que leia a descrição dos ataques em busca de detalhes operacionais antes da entrega.

### 7.5 Apêndice de artefatos

Inclua a URL do repositório e o commit, o ambiente, os comandos para reproduzir cada tabela, o cartão de dados do gerador sintético, o cartão de modelo (model card) de qualquer modelo publicado (Mitchell et al., arXiv:1810.03993) e os hashes dos arquivos principais. Diga o que não é publicado e por quê. O apêndice de Leo inclui o cartão de dados do gerador sintético, o commit do repositório, os comandos de cada tabela e os hashes dos arquivos. Ele declara que nenhum modelo é publicado e por quê. Peça a um colega que reproduza uma tabela apenas a partir do apêndice antes da entrega. Mantenha-o atualizado.

### 7.6 Exemplo resolvido (caso sintético da Harbourline)

A seção de limitações de Leo tem quatro subseções curtas. Validade externa: "Estudamos um único classificador transformer ajustado com notas sintéticas em inglês; os resultados podem diferir para modelos generativos, outros idiomas e dados reais de sinistros." Validade de construto: "Medimos a inferência de pertencimento com dois ataques; a inferência de atributos e a extração não foram estudadas." Ele moveu dos resultados para a discussão uma frase sobre "as seguradoras devem deduplicar" e a atenuou para "a deduplicação é um controle candidato de baixo custo que as seguradoras poderiam avaliar". O laboratório de extração é citado no seu capítulo de contexto como uma ilustração simples de por que a precisão da saída da API importa ao descrever modelos de ameaça.

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

Saída esperada:

```text
output_rounding=None queries=6 max_weight_error=0.000 label_agreement=1.000
output_rounding=2    queries=6 max_weight_error=0.004 label_agreement=0.998
output_rounding=0    queries=6 max_weight_error=0.534 label_agreement=0.882
```

### 7.7 Atividades práticas

1. Escreva a sua seção de limitações por tipo de validade. 2. Marque cada frase do seu capítulo de resultados como achado ou interpretação e mova as que estiverem fora do lugar. 3. Redija o apêndice de artefatos. Nas limitações, use os quatro tipos de validade e diga, para cada um, o que você fez e o que resta, como Leo fez para um classificador e notas sintéticas. No capítulo de resultados, marque cada frase e mova as interpretações para a discussão. No apêndice, liste repositório, commit, ambiente, comandos, cartões e hashes, e diga o que não é publicado.

### 7.8 Erros e limites

Quatro erros se repetem: resultados e discussão misturados; limitações genéricas ("são necessários mais dados"); detalhes operacionais de ataque contra sistemas identificados pelo nome; e recomendações enunciadas como achados. Cada erro torna as alegações menos confiáveis. Resultados e discussão misturados borram o que foi medido. Limitações genéricas não dizem nada aos examinadores sobre este estudo. Detalhes operacionais contra sistemas identificados ajudam atacantes sem ajudar os leitores. Uma recomendação enunciada como achado alega mais do que os dados mostram, e é por isso que Leo moveu e atenuou a sua recomendação às seguradoras. Confira o seu rascunho quanto aos quatro.

### Exercícios

- **EX039 — Achado ou interpretação.** Classifique: (a) "a ASR caiu de 31% para 6%"; (b) "a defesa funciona porque remove o canal do atacante". Rubrica: 3 = (a) achado, (b) interpretação, com razão; 2 = só os rótulos; 1 = um; 0 = errado.
- **EX040 — Validade.** Escreva uma limitação para cada tipo de validade no seu projeto. Rubrica: 3 = quatro específicas; 2 = três; 1 = uma ou duas; 0 = nenhuma.
- **EX041 — Detalhe responsável.** Reescreva de forma responsável uma frase que dá uma carga exata e funcional contra um chatbot identificado pelo nome. Rubrica: 3 = descrição em nível de desenho, citação, sem alvo real nem string; 2 = parcial; 1 = ainda operacional; 0 = inalterada.
- **EX042 — Apêndice de artefatos.** Liste seis itens. Rubrica: 3 = seis pertinentes; 2 = quatro; 1 = dois; 0 = nenhum.
- **EX043 — Citação do laboratório.** O que o laboratório de extração mostra sobre a precisão da saída, com números? Rubrica: 3 = recuperação exata com precisão total (erro 0.000), 0.004 com 2 casas decimais, 0.534 com inteiros; a concordância cai para 0.882; 2 = números parciais; 1 = vago; 0 = errado.
- **EX044 — Recomendação.** Reescreva "As seguradoras devem deduplicar" no nível da evidência. Rubrica: 3 = controle candidato a avaliar, com condições; 2 = parcial; 1 = ainda prescritiva; 0 = inalterada.

### Síntese

Uma dissertação é julgada pela clareza com que as suas alegações correspondem à sua evidência. Separar achados de interpretação, escrever limitações específicas e tratar com responsabilidade os detalhes dos ataques tornam o trabalho crível e seguro.

### Continue estudando — capítulo 07 de 08

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Revisão independente e defesa

### Objetivos de aprendizagem

Você vai (1) encomendar e usar uma revisão independente do código e do texto antes da entrega; (2) preparar uma apresentação de defesa; (3) responder às perguntas dos examinadores com evidência e limites; (4) atender às correções exigidas; e (5) planejar a divulgação, incluindo um resumo curto para profissionais.

### 8.1 Revisão independente antes da entrega

Peça a um colega que não trabalhou no projeto que (a) reproduza uma tabela principal a partir do seu apêndice de artefatos, (b) leia o método e diga o que não conseguiria repetir e (c) leia o resumo e diga o que ele acha que você alega. Cada uma revela um problema diferente: dependências ocultas, detalhes de método ausentes e alegações exageradas. Uma revisão de código curta, focada no cálculo das métricas e nas partições dos dados, vale o tempo; defeitos ali mudam conclusões. Foi assim que o colega de Leo encontrou um descarte silencioso de registros longos.

### 8.2 A apresentação da defesa

De vinte a trinta minutos: problema e pergunta; desenho e por quê; resultados com intervalos e custos; explicações concorrentes e o que as descartou; limitações; contribuição e próximos passos. Um slide deve responder à pergunta de pesquisa numa frase, com um número e um intervalo. O slide de resposta de Leo trouxe a diferença pareada com o seu intervalo. Coloque as explicações concorrentes antes das limitações, pois os examinadores vão perguntar sobre elas. Ensaie com um cronômetro e um colega que faça perguntas difíceis, e prepare slides de reserva para a ablação e as verificações de qualidade, para poder mostrar a evidência quando ela for pedida.

### 8.3 Respostas aos examinadores

Espere perguntas sobre escolhas de desenho ("por que dados sintéticos?"), ameaças à validade ("isso valeria para notas reais?"), estatística ("cinco sementes bastam?"), explicações alternativas ("isso não é só sobreajuste?") e prática ("o que a Harbourline deveria fazer?"). Responda em três partes: resposta direta, evidência, limite. Quando não souber, diga isso e diga como descobriria. As respostas de Leo no exemplo resolvido abaixo seguem essa forma: a ablação como evidência, o ataque como limite. Prepare respostas escritas para cada pergunta esperada e ensaie-as com um colega que faça o papel de examinador crítico.

### 8.4 Correções e divulgação

Os examinadores costumam exigir correções. Faça cada mudança, liste-a numa tabela de correções com referências de página e devolva-a sem demora. As opções de divulgação incluem um artigo de workshop, um repositório público com o gerador sintético e um resumo de duas páginas para profissionais que enuncie o achado, as condições e o próximo passo recomendado — mapeado, quando pertinente, aos frameworks que a organização usa, como as funções *Measure* (Medir) e *Manage* (Gerenciar) do NIST AI RMF ou o seu processo de tratamento de riscos da ISO/IEC 42001. O resumo para profissionais de Leo apresenta a deduplicação como um controle candidato de baixo custo sob o ataque avaliado.

### 8.5 Exemplo resolvido (caso sintético da Harbourline)

Um colega, ao reproduzir a tabela principal de Leo, descobriu que o script de avaliação descartava silenciosamente registros com mais de 512 tokens, cerca de 3% dos não membros. Leo corrigiu o problema; a TPR com FPR de 1% mudou 0,2 ponto e as conclusões se mantiveram, e ele registrou a correção. Na defesa, um examinador perguntou: "Isso não é só sobreajuste?" Leo mostrou a ablação de remoção aleatória e a análise com diferenças de generalização equiparadas: "Parte do efeito está ligada ao tamanho — 1,9 ponto —, mas os 3,7 pontos restantes são específicos das duplicatas, sob este ataque." Outro perguntou se a Harbourline não deveria adotar a privacidade diferencial no lugar. Leo respondeu que a DP dá garantias formais (Abadi et al., arXiv:1607.00133) a um custo de utilidade que ele não mediu; a deduplicação é complementar e barata, e uma comparação com a DP é trabalho futuro.

O laboratório de inferência de pertencimento pode ser usado na defesa para mostrar o conceito central em trinta segundos.

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

Saída esperada:

```text
k= 1 attack_auc=0.600 best_advantage=0.200
k= 5 attack_auc=0.521 best_advantage=0.073
k=25 attack_auc=0.520 best_advantage=0.060
```

### 8.6 Atividades práticas

1. Organize uma revisão com reprodução e leitura do resumo. 2. Monte uma apresentação de defesa com um slide de resposta. 3. Escreva o resumo para profissionais. Na revisão, peça a um colega que reproduza uma tabela e leia o resumo, e registre o que ele encontrou. Na apresentação, inclua um slide que responda à pergunta com um número e um intervalo, como o de Leo fez com a diferença de 3,7 pontos. No resumo, enuncie o achado, as condições e o próximo passo, e limite-o a duas páginas. Anote o que mudou.

### 8.7 Erros e limites

Quatro erros se repetem: entregar sem que ninguém tenha reproduzido um resultado; responder às perguntas na defensiva, sem evidência; resumos para profissionais que omitem as condições; e ignorar as referências de página das correções exigidas. Cada erro enfraquece a etapa final. Sem uma reprodução, problemas como os registros longos descartados no trabalho de Leo chegam aos examinadores. Respostas defensivas sem evidência fazem perder a confiança dos examinadores. Um resumo que omite as condições transforma um resultado sob um único ataque numa regra geral. Correções sem referências de página são difíceis de conferir e atrasam a aprovação. Confira a sua entrega quanto aos quatro.

### Exercícios

- **EX045 — Revisões.** Nomeie três revisões independentes a pedir e o que cada uma encontra. Rubrica: 3 = reprodução/dependências ocultas, leitura do método/detalhes ausentes, leitura do resumo/alegações exageradas; 2 = duas; 1 = uma; 0 = nenhuma.
- **EX046 — Slide de resposta.** Escreva o slide de resposta de uma frase de Leo. Rubrica: 3 = achado com número, intervalo e condições; 2 = falta o intervalo ou as condições; 1 = vago; 0 = nenhum.
- **EX047 — Pergunta sobre sobreajuste.** Responda a "isso não é só sobreajuste?" para o seu próprio projeto. Rubrica: 3 = resposta direta, evidência (ablação/controle), limite; 2 = duas partes; 1 = uma; 0 = nenhuma.
- **EX048 — Impacto do defeito.** Como Leo deve relatar o defeito dos 512 tokens? Rubrica: 3 = descrever, corrigir, quantificar a mudança, registrar que as conclusões se mantiveram, no registro de desvios/correções; 2 = parcial; 1 = esconder; 0 = nenhum.
- **EX049 — DP vs dedup.** Contraste a privacidade diferencial e a deduplicação em duas frases. Rubrica: 3 = DP é um limite formal com custo de utilidade; dedup é heurística, barata, mira a repetição; complementares; 2 = parcial; 1 = vago; 0 = errado.
- **EX050 — Resumo para profissionais.** Escreva as três primeiras frases do resumo para profissionais. Rubrica: 3 = achado, condições, próximo passo, sem exagero; 2 = duas; 1 = uma; 0 = nenhuma.

### Síntese

A revisão independente pega os erros que você não consegue ver; a defesa testa se você consegue ligar cada alegação à evidência e aos seus limites. Um resumo cuidadoso para profissionais leva o resultado à prática sem perder as suas condições.

### Continue estudando — capítulo 08 de 08

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções ↓](#worked-results) · [Próximo curso pelo índice de capítulos →](../SUBJECTS.md)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo; qualquer resposta que atenda à rubrica recebe a mesma pontuação. A Harbourline Mutual e todos os seus números são sintéticos.

**EX001.** "Em agentes de LLM que usam ferramentas e leem e-mails não confiáveis (P), exigir confirmação humana para ações de saída (I), em comparação com nenhuma confirmação (C), reduz a exfiltração bem-sucedida num benchmark em sandbox de 500 tarefas sintéticas (O)?"

**EX002.** Fontes/bases; expressões de busca; intervalo de datas; critérios de inclusão e exclusão; data da busca; contagens em cada etapa de triagem (também: rastreamento de citações).

**EX003.** Modelo de ameaça; tipo/tamanho do modelo; dados; métrica; resultado principal; defesa; avaliação adaptativa; disponibilidade de código; limitações. A *avaliação adaptativa* importa porque defesas testadas apenas contra ataques fixos costumam ser quebradas depois.

**EX004.** O dano à privacidade vem de identificar com confiança indivíduos específicos; um ataque com AUC modesta ainda pode identificar alguns registros com quase certeza, o que só a TPR com FPR baixa revela.

**EX005.** O artigo revisado por pares (conferido pela revisão) e o preprint do arXiv com código (verificável) perto do topo — qualquer das duas ordens pode ser defendida; o blog de fornecedor por último. O framework do NIST não é uma fonte experimental: ele fornece vocabulário e expectativas a citar para definições.

**EX006.** k = 1: AUC 0.600; k = 5: AUC 0.521. Memorizar (k = 1) vaza o pertencimento; fazer a média sobre os vizinhos remove a maior parte do sinal.

**EX007.** Cite os autores, o título, o nome do workshop e o ano, e a URL que você usou (com data de acesso). Nunca invente um DOI.

**EX008.** Evasão: um atacante com acesso por consulta (ou de caixa-branca) perturba entradas de teste para causar erro de classificação. Backdoor: um atacante que controla parte dos dados de treino insere exemplos com gatilho para provocar saídas escolhidas. Inferência de pertencimento: um atacante com acesso por consulta às saídas decide se um registro estava no treino.

**EX009.** O FGSM dá um passo de tamanho eps na direção do sinal do gradiente; o PGD dá muitos passos menores, projetando de volta no conjunto permitido a cada vez, e é um ataque mais forte.

**EX010.** Com saídas inteiras, o erro máximo dos pesos é 0.534 e a concordância de rótulos é 0.882 (contra 0.000/1.000 com precisão total). Saídas grosseiras reduzem a fidelidade, mas ainda deixam uma cópia aproximada útil.

**EX011.** O pertencimento revela que uma pessoa abriu um sinistro, o que pode implicar problemas de saúde, acidentes ou perdas — algo sensível em si.

**EX012.** Alguém de dentro com acesso de escrita às notas de treino poderia inserir notas com uma frase rara rotulada como "aprovação acelerada". Controles: acesso de escrita restrito e registrado, com proveniência dos dados de treino; auditorias antes do treino em busca de correlações raras entre tokens e rótulos e testes de gatilho depois do treino.

**EX013.** LLM01 Prompt Injection (instruções nos e-mails); LLM02 Sensitive Information Disclosure (detalhes do sinistro nas respostas); LLM06 Excessive Agency (envio de respostas sem revisão).

**EX014.** Por exemplo: que conhecimento do adversário se supõe, e a defesa é avaliada contra um atacante que a conhece? Os resultados são relatados com taxas baixas de falsos positivos e com intervalos entre sementes? Qual é o custo de utilidade ou de latência nas mesmas tarefas?

**EX015.** Estudo observacional dos registros de um assistente que o pesquisador está autorizado a estudar, com salvaguardas de consentimento/privacidade; os fatores de confusão (população de usuários, mudanças de funcionalidades) precisam ser discutidos. Um experimento é impossível porque não se pode controlar atacantes reais.

**EX016.** Independente: defesa (nenhuma vs treinamento adversarial). Dependentes: acurácia sob PGD com eps fixo; acurácia limpa. Controladas: arquitetura, épocas de treino, partição dos dados, passos/eps do ataque, sementes.

**EX017.** Se os não membros diferem na distribuição (por exemplo, registros mais novos), o ataque consegue distingui-los pela mudança de distribuição, não pelo pertencimento, e o vazamento medido fica inflado.

**EX018.** Licitude; limitação da finalidade; minimização dos dados; limitação da conservação; integridade e confidencialidade (segurança); responsabilização.

**EX019.** Taxas por semente 0.110, 0.130, 0.135, 0.105, 0.145 — uma amplitude de 0.105–0.145 — com média 0.125 e dp 0.017.

**EX020.** Repositório com controle de versão; ambiente fixado; arquivos de configuração; política de sementes; um comando por experimento; registros estruturados; cartão de dados.

**EX021.** A avaliação usou prompts de jailbreak mais fracos ou diferentes; o guardrail recusa em excesso (inclusive prompts benignos); a distribuição dos prompts difere entre as condições; artefatos do juiz ou da semente.

**EX022.** Remova o mesmo número de registros ao acaso (vários sorteios). Se o ganho de privacidade for igual ao da deduplicação, o tamanho do conjunto o explica; se a deduplicação ganhar mais, remover as duplicatas importa.

**EX023.** Os centroides fazem a média de centenas de pontos, então uma minoria de rótulos invertidos os desloca pouco; o backdoor usa uma terceira característica que é zero nos dados limpos, criando uma direção nova que os dados limpos não conseguem contrabalançar.

**EX024.** Acurácia limpa 0.968; sucesso do ataque 0.980.

**EX025.** Um ataque fraco pode fazer qualquer defesa parecer eficaz; um ataque calibrado e mais forte (sobretudo com FPR baixa) mostra se a redução sobrevive.

**EX026.** "Sob um ataque calibrado de inferência de pertencimento, a maior parte da redução observada no vazamento foi atribuível à remoção de registros duplicados, e não ao conjunto de treino menor."

**EX027.** Pergunta/motivação; contexto; desenho; explicações concorrentes/ablações; plano de análise; ética e proteção de dados; riscos e mitigações; cronograma; contribuição esperada.

**EX028.** Confirmar que o pipeline funciona de ponta a ponta; medir o tempo de execução; estimar a variabilidade; verificar que métricas e ataques se comportam de forma sensata; descobrir surpresas.

**EX029.** n ≈ 1,96² × 0,05 × 0,95 / 0,01² ≈ 1.825.

**EX030.** Todas as condições ficam perto do mínimo da métrica, de modo que as diferenças não aparecem. Leo substituiu o ataque por limiar de confiança por um ataque calibrado com modelos de referência.

**EX031.** eps 0.50 (0.840) e 0.75 (0.660): a acurácia não está perto do teto limpo (0.985) nem no nível do acaso (0.505 em 1.00), então as defesas podem ser distinguidas.

**EX032.** "Piloto, dia 3: ataque por limiar substituído por ataque calibrado; razão: efeito piso (TPR de 1–2% em todas as condições); efeito: condições separáveis." "Piloto, dia 4: corrigidos os modelos 12 e 19 do gerador; razão: notas quase idênticas entre classes; efeito: elimina o ruído de rótulo."

**EX033.** Se as condições rodam em blocos, uma mudança dependente do tempo (hardware, biblioteca, carga) pode se disfarçar de efeito do tratamento; a intercalação espalha esses problemas por todas as condições.

**EX034.** Todas as execuções presentes; canários passam (modelo sem defesa atacável, modelo com rótulos embaralhados no nível do acaso); nenhuma duplicata entre partições; valores de métricas plausíveis.

**EX035.** ASR de base 0.350; com defesa 0.190; IC de 95% da redução [0.120, 0.203].

**EX036.** Os itens variam em dificuldade; o pareamento cancela essa variação compartilhada, dando um intervalo mais estreito e correto para a diferença. Comparar intervalos separados que se sobrepõem é conservador e pode enganar.

**EX037.** Utilidade/acurácia; latência; recusas indevidas ou falsos positivos; custo de computação e de manutenção.

**EX038.** Como resultado exploratório, numa subseção rotulada, apresentado como hipótese para trabalho confirmatório futuro.

**EX039.** (a) Achado — uma quantidade medida. (b) Interpretação — uma explicação causal que precisa de evidência de ablação.

**EX040.** Interna: artefatos do gerador; de construto: uma única família de ataques; externa: uma única arquitetura, notas sintéticas em inglês; de conclusão: cinco sementes. (Cada uma com a ação tomada.)

**EX041.** "Seguindo Greshake et al. (arXiv:2302.12173), construímos injeções indiretas embutidas em documentos recuperados na nossa sandbox; as strings das cargas não são publicadas e ficam disponíveis a pesquisadores mediante pedido."

**EX042.** Repositório e commit; ambiente; comandos de reprodução por tabela; cartão de dados; cartão de modelo; hashes dos arquivos principais; declaração do que é retido e por quê.

**EX043.** A precisão total recupera os pesos exatamente (erro 0.000, concordância 1.000); duas casas decimais dão erro 0.004 (concordância 0.998); inteiros dão erro 0.534 (concordância 0.882). A precisão da saída faz parte do modelo de ameaça.

**EX044.** "A deduplicação é um controle de baixo custo que seguradoras que ajustam classificadores poderiam avaliar para reduzir o vazamento de pertencimento."

**EX045.** A reprodução de uma tabela encontra dependências ocultas e defeitos; a leitura do método encontra detalhes ausentes; a leitura do resumo encontra alegações exageradas.

**EX046.** "A deduplicação aproximada reduziu a TPR da inferência de pertencimento com FPR de 1% de 9,8% para 4,2%, 3,7 pontos (IC de 95%: 2,6–4,9) a mais do que a remoção aleatória, a um custo de 0,007 no macro-F1 — em notas sintéticas, uma única arquitetura, ataque calibrado."

**EX047.** As respostas variam; uma resposta completa dá uma resposta direta, a evidência da ablação ou do controle e um limite.

**EX048.** Descrever o defeito, a correção, a mudança de 0,2 ponto, que as conclusões se mantiveram, e registrá-lo no registro de desvios e nos métodos.

**EX049.** A privacidade diferencial limita formalmente a influência de cada registro, a um custo de utilidade mensurável. A deduplicação é uma heurística barata que mira registros repetidos; as duas são complementares.

**EX050.** "Remover as notas de sinistro duplicadas antes do ajuste fino reduziu aproximadamente à metade uma medida de vazamento de pertencimento no nosso estudo sintético, quase sem custo de acurácia. Isso valeu para um único tipo de modelo e dados sintéticos. Sugerimos um piloto numa cópia governada de dados reais antes de adotar a prática."

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; os frameworks mudam, então verifique de novo. Os identificadores arXiv foram abertos e os títulos conferidos.

- Abadi, M. et al. (2016). Deep Learning with Differential Privacy. arXiv:1607.00133.
- Athalye, A., Carlini, N., Wagner, D. (2018). Obfuscated Gradients Give a False Sense of Security. arXiv:1802.00420.
- Carlini, N. et al. (2020). Extracting Training Data from Large Language Models. arXiv:2012.07805.
- União Europeia. Regulamento (UE) 2024/1689 (Regulamento de Inteligência Artificial — AI Act). <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
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
