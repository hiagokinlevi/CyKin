# Governança de Dados: Trilha de Pesquisa de Doutorado

- Idioma: português do Brasil (`pt`); curso 187, trilha de pesquisa de doutorado (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–8 de 8 têm texto didático escrito à mão; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; três laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: doutorandos que estudam como os direitos de decisão sobre regras de qualidade de dados e sobre o pareamento de registros (*record linkage*) moldam as estatísticas oficiais.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios medem dimensões de qualidade em um cadastro empresarial sintético, calculam pesos de pareamento de Fellegi-Sunter em pares de registros sintéticos e avaliam metadados sintéticos de conjuntos de dados com uma lista de verificação FAIR. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública. O código dos laboratórios e suas saídas são mantidos exatamente como na edição em inglês.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma doutoranda desde as regras de integridade e a fronteira da pesquisa, passando por um projeto, a replicação de uma linha de base de pareamento, uma simulação principal com validação independente, a crítica dos pares e um arquivo de reprodutibilidade, até a defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Nadia Rahman** | Doutoranda | Inventada |
| **Prof. Lars Eriksen** | Orientador | Inventado |
| **Universidade Halvorsen** | Universidade fictícia | Inventada |
| **Instituto de Estatística de Westmark** | Instituto de estatística fictício que vincula um cadastro empresarial a registros de emprego | Inventado |

### Fontes principais

DAMA-DMBOK2 (2017); ISO/IEC 38505-1:2017; ISO 8000-8:2015; Khatri e Brown (2010), [doi:10.1145/1629175.1629210](https://doi.org/10.1145/1629175.1629210); Wang e Strong (1996); Batini et al. (2009); Fellegi e Sunter (1969); NIST SP 800-188; Wilkinson et al. (2016), [doi:10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Integridade e métodos avançados de pesquisa

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta de doutorado sobre governança de dados; (2) definir regras de integridade para trabalhar com dados administrativos vinculados; (3) planejar métodos que outras pessoas possam reproduzir.

### 1.1 A doutoranda e a pergunta

Nadia Rahman inicia uma trilha de pesquisa de doutorado de dois anos na fictícia Universidade Halvorsen, sob orientação do Prof. Lars Eriksen. A organização parceira é o fictício Instituto de Estatística de Westmark, que vincula um cadastro empresarial a registros de emprego para publicar estatísticas sobre empregos regionais. Sua pergunta é como as decisões de governança — por exemplo, quem define as regras de qualidade de dados e quem escolhe os limiares de pareamento de registros — alteram as estatísticas que ministros e o público leem. Khatri e Brown descrevem a governança como a decisão sobre quem detém os direitos de decisão sobre os dados, e Nadia quer medir as consequências desses direitos.

### 1.2 Regras de integridade

O Prof. Eriksen pede a Nadia que escreva regras de integridade antes de tocar em qualquer dado. Toda a análise usa uma réplica sintética do cadastro de Westmark, construída a partir de distribuições publicadas, nunca de registros confidenciais. Cada resultado é produzido por um script mantido sob controle de versão, e cada número da tese precisa ser rastreável até uma execução de script. Ela registrará as decisões que alteram resultados, como descartar um campo, em um diário de decisões com datas e justificativas. Nadia observa que a integridade importa em dobro na pesquisa sobre governança, porque a própria pesquisa faz afirmações sobre a integridade dos dados de outras pessoas.

### 1.3 Métodos que outros possam repetir

Nadia opta por métodos mistos. A parte quantitativa mede dimensões de qualidade de dados e o erro de pareamento na réplica sintética. A parte qualitativa usa entrevistas com a equipe de Westmark sobre quem decide as regras de qualidade e os limiares, realizadas com consentimento livre e esclarecido e com transcrições anonimizadas. Ela pré-registra as hipóteses principais com o orientador: direitos de decisão pouco claros levam a limiares inconsistentes entre divulgações, e limiares inconsistentes produzem deslocamentos mensuráveis nas contagens regionais de emprego. O pré-registro a protege contra a tentação de remodelar hipóteses depois de ver os resultados. Os roteiros de entrevista são testados com dois servidores aposentados.

### 1.4 Fontes e normas

Nadia monta sua lista de leitura em torno de fontes consolidadas. O DAMA-DMBOK2 descreve a governança de dados como o exercício de autoridade e controle sobre ativos de dados e explica sua relação com as demais funções de gestão de dados. A ISO/IEC 38505-1 aplica o modelo de governança da ISO/IEC 38500 aos dados, atribuindo a responsabilização (*accountability*) ao órgão de governança. Wang e Strong oferecem um arcabouço de dimensões de qualidade de dados orientado ao consumidor. Ela registra quais afirmações cada fonte sustenta, para que a tese cite fontes como base de definições e evidências, e não apenas como argumento de autoridade. As definições vêm primeiro.

### Exemplo resolvido

Nadia formula uma pergunta sobre direitos de decisão e estatísticas publicadas, escreve regras de integridade para uma réplica sintética, pré-registra hipóteses e associa cada fonte às afirmações que ela sustenta.

> **Caso sintético.** Halvorsen, Westmark e todas as pessoas são sintéticos; DAMA-DMBOK2, ISO/IEC 38505-1, Khatri e Brown (2010) e Wang e Strong (1996) são reais.

### Erros e limites

Uma réplica sintética não reproduz todas as peculiaridades de registros reais; declare esse limite desde o início.

### Exercícios

- **EX001 — Pergunta de pesquisa.** Qual é a pergunta de doutorado de Nadia? *Rubrica:* 3 = como decisões de governança alteram estatísticas publicadas;; 2 = menciona decisões;; 1 = nenhuma;; 0 = nenhuma.
- **EX002 — Direitos de decisão.** Como Khatri e Brown enquadram a governança? *Rubrica:* 3 = decidir quem detém direitos de decisão sobre os dados;; 2 = menciona direitos;; 1 = nenhuma;; 0 = nenhuma.
- **EX003 — Regra da réplica.** Que dados Nadia pode analisar? *Rubrica:* 3 = uma réplica sintética a partir de distribuições publicadas;; 2 = correto;; 1 = dados reais;; 0 = nenhuma.
- **EX004 — Rastreabilidade.** Como cada número deve ser rastreável? *Rubrica:* 3 = até uma execução de script sob controle de versão;; 2 = menciona scripts;; 1 = nenhuma;; 0 = nenhuma.
- **EX005 — Pré-registro.** Por que pré-registrar hipóteses? *Rubrica:* 3 = para não remodelá-las depois dos resultados;; 2 = menciona viés;; 1 = nenhuma;; 0 = nenhuma.
- **EX006 — Duas hipóteses.** Enuncie uma hipótese pré-registrada. *Rubrica:* 3 = direitos pouco claros causam limiares inconsistentes; limiares deslocam contagens;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.
- **EX007 — Modelo ISO.** Onde a ISO/IEC 38505-1 coloca a responsabilização? *Rubrica:* 3 = no órgão de governança;; 2 = correto;; 1 = gestores;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Governança de dados: a fronteira da pesquisa

### Objetivos de aprendizagem

Você vai (1) revisar os debates atuais na pesquisa em governança de dados; (2) medir dimensões de qualidade de dados em um cadastro sintético; (3) identificar uma lacuna para um trabalho original.

### 2.1 O estado da área

Nadia revisa a literatura. Os primeiros trabalhos tratavam a qualidade de dados apenas como acurácia; Wang e Strong mostraram que os consumidores de dados também se importam com atualidade, relevância, acessibilidade e interpretabilidade. Batini e colegas compararam metodologias de avaliação e constataram que a maioria define dimensões, mede essas dimensões e propõe melhorias, mas diverge na escolha das dimensões e no peso atribuído a cada uma. A ISO 8000-8 estabelece conceitos e pré-requisitos para medir a qualidade da informação e dos dados. Nadia observa que os métodos de medição estão bem desenvolvidos, enquanto a pesquisa sobre quem decide as regras de qualidade é mais escassa.

### 2.2 Medindo um cadastro

Para ancorar a revisão, Nadia mede três dimensões em um cadastro sintético de 5.000 empresas. O laboratório informa completude de 0,798, validade de 0,937 e unicidade de 0,966. A completude é a mais baixa porque muitos registros não têm código de setor ou código postal. As falhas de validade vêm de códigos postais com letras e de um código de setor desconhecido. A unicidade fica abaixo de um porque alguns números de registro aparecem duas vezes. Cada número depende de uma regra escolhida por alguém, por exemplo se um setor em branco conta como ausente ou como valor legítimo. As regras pesam tanto quanto os dados.

### 2.3 Regras são decisões

Nadia mostra ao Prof. Eriksen como o índice de completude muda se setores em branco forem permitidos para empresas recém-registradas. O número sobe, embora nenhum registro tenha mudado. Ela argumenta que os índices de qualidade são, em parte, produtos da governança: refletem decisões sobre regras, limiares e exceções. É por isso que o DAMA-DMBOK2 situa a gestão da qualidade de dados dentro de um arcabouço de governança. O mapa de literatura de Nadia mostra poucos estudos empíricos que acompanham como essas decisões sobre regras são tomadas e como deslocam os números publicados — e essa é a lacuna que ela vai abordar.

### 2.4 Posicionando a contribuição

Nadia redige uma declaração de posicionamento: a pesquisa existente mede a qualidade e propõe estruturas de governança, mas raramente liga as duas coisas de forma quantitativa no contexto das estatísticas oficiais. Sua contribuição será um método que registra os direitos de decisão, aplica regras alternativas a uma réplica sintética e mede o efeito sobre os produtos publicados. O Prof. Eriksen a desafia a mostrar por que isso importa para além de Westmark. Ela responde que qualquer organização que publica indicadores a partir de dados administrativos enfrenta a mesma pergunta: quem decide o que conta como dado bom o suficiente. Westmark é o caso de teste.

### Laboratório — Dimensões de qualidade de um cadastro empresarial sintético

```python
"""Score completeness, validity and uniqueness of a synthetic business register (stdlib only)."""
import random, re
random.seed(3)
rows = []
for i in range(5000):
    reg = f"BR{i:06d}"
    if random.random() < 0.03: reg = f"BR{random.randint(0, i):06d}"      # duplicate ids
    post = f"{random.randint(1000, 9999)}" if random.random() > 0.08 else ""
    if random.random() < 0.04: post = "ABCD"                                # invalid
    sector = random.choice(["A", "C", "F", "G", "J", "M", ""]) if random.random() > 0.02 else "Z9"
    rows.append((reg, post, sector))
n = len(rows)
complete = sum(1 for r in rows if r[1] and r[2]) / n
valid = sum(1 for r in rows if re.fullmatch(r"\d{4}", r[1] or "0000") and r[2] in {"A","C","F","G","J","M",""}) / n
unique = len({r[0] for r in rows}) / n
print(f"records {n}")
print(f"completeness {complete:.3f}  validity {valid:.3f}  uniqueness {unique:.3f}")
```

Execute com `python3 lab_quality.py`. Saída verificada:

```text
records 5000
completeness 0.798  validity 0.937  uniqueness 0.966
```

### Exemplo resolvido

Nadia revisa a literatura sobre qualidade, mede completude de 0,798, validade de 0,937 e unicidade de 0,966 em 5.000 registros sintéticos, mostra que a escolha de regras move os índices e posiciona sua contribuição.

> **Caso sintético.** O cadastro é sintético; Wang e Strong (1996), Batini et al. (2009), ISO 8000-8:2015 e DAMA-DMBOK2 são reais.

### Erros e limites

Os índices das dimensões dependem das definições das regras; publique as regras junto com os índices.

### Exercícios

- **EX008 — Além da acurácia.** O que Wang e Strong acrescentaram à acurácia? *Rubrica:* 3 = atualidade, relevância, acessibilidade, interpretabilidade;; 2 = duas;; 1 = uma;; 0 = nenhuma.
- **EX009 — Completude.** Que índice de completude o laboratório informou? *Rubrica:* 3 = 0,798;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX010 — Causa do menor índice.** Por que a completude é a mais baixa? *Rubrica:* 3 = faltam códigos de setor ou códigos postais;; 2 = menciona ausência;; 1 = nenhuma;; 0 = nenhuma.
- **EX011 — Causa da unicidade.** Por que a unicidade fica abaixo de um? *Rubrica:* 3 = números de registro duplicados;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX012 — Mudança de índice.** Por que a completude subiu sem que nenhum registro mudasse? *Rubrica:* 3 = mudou a regra para setores em branco;; 2 = menciona regra;; 1 = nenhuma;; 0 = nenhuma.
- **EX013 — Papel da ISO 8000.** O que a ISO 8000-8 oferece? *Rubrica:* 3 = conceitos e pré-requisitos para medir a qualidade de dados;; 2 = menciona medição;; 1 = nenhuma;; 0 = nenhuma.
- **EX014 — Lacuna de pesquisa.** Que lacuna Nadia aborda? *Rubrica:* 3 = como decisões sobre regras são tomadas e deslocam números publicados;; 2 = menciona decisões;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Projeto de contribuição original

### Objetivos de aprendizagem

Você vai (1) escrever um projeto de doutorado com afirmações testáveis; (2) definir medidas e variáveis de direitos de decisão; (3) planejar ética e acesso.

### 3.1 O projeto

O projeto de Nadia tem três afirmações. Primeira: os direitos de decisão de Westmark sobre regras de qualidade e limiares de pareamento podem ser descritos com uma matriz de papéis e decisões, seguindo os domínios de Khatri e Brown. Segunda: decisões alternativas dentro de faixas plausíveis mudam as contagens regionais de emprego em magnitudes relevantes para os usuários. Terceira: um processo decisório documentado reduz a variação não explicada entre divulgações. Cada afirmação indica sua evidência: a matriz, a partir de entrevistas e documentos; os tamanhos de efeito, a partir de simulação na réplica sintética; e a variação, a partir da comparação entre divulgações antes e depois da documentação.

### 3.2 Medidas

Para os produtos, Nadia mede as contagens regionais de emprego e sua variação entre divulgações. Para o pareamento, mede precisão e revocação (*precision* e *recall*), definidas como a proporção de pares vinculados que são correspondências verdadeiras e a proporção de correspondências verdadeiras que foram vinculadas. Para a qualidade, usa as dimensões do Capítulo 2. Para a governança, codifica cada decisão por quem a tomou, se foi documentada e se foi revisada. O Prof. Eriksen pede que ela defina cada medida antes de rodar qualquer coisa, para que as medidas não derivem em direção a resultados convenientes.

### 3.3 Ética e acesso

As entrevistas envolvem servidores de Westmark, que podem temer críticas às suas decisões. O protocolo submetido ao comitê de ética promete anonimato, direito de desistência, revisão das citações pelos entrevistados e armazenamento das gravações em sistemas criptografados da universidade, com exclusão após a transcrição. O acesso aos documentos de Westmark é regido por um acordo escrito que exclui microdados confidenciais e permite a publicação de resultados agregados após uma revisão de exatidão, não de conteúdo. Ela observa que uma revisão de conteúdo comprometeria a independência, por isso o acordo limita a revisão de Westmark a erros factuais. Westmark assina o acordo.

### 3.4 Viabilidade

Nadia distribui o trabalho ao longo de dois anos: seis meses para a réplica, a matriz de decisões e a linha de base; seis meses para a simulação principal e as entrevistas; seis meses para a validação e a comparação entre divulgações; e seis meses para a redação e a defesa. Ela identifica riscos, como atrasos nas entrevistas, e planeja análises alternativas que dependem apenas de documentos. O Prof. Eriksen aprova o projeto depois de pedir que ela restrinja a comparação entre divulgações a dois indicadores, o que torna a etapa de validação viável dentro do prazo disponível.

### Exemplo resolvido

Nadia propõe três afirmações testáveis, define medidas de produto, pareamento, qualidade e governança, obtém aprovação ética com anonimato e uma cláusula de revisão apenas factual, e planeja um cronograma viável de dois anos.

> **Caso sintético.** O projeto é sintético; Khatri e Brown (2010) são reais.

### Erros e limites

Projetos que prometem demais fracassam na validação; restrinja o escopo cedo.

### Exercícios

- **EX015 — Três afirmações.** Enuncie uma das afirmações de Nadia. *Rubrica:* 3 = matriz de direitos de decisão; decisões mudam contagens; documentação reduz variação;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.
- **EX016 — Precisão.** Defina precisão no pareamento. *Rubrica:* 3 = proporção de pares vinculados que são correspondências verdadeiras;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX017 — Revocação.** Defina revocação no pareamento. *Rubrica:* 3 = proporção de correspondências verdadeiras que foram vinculadas;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX018 — Codificação de decisões.** Como cada decisão de governança é codificada? *Rubrica:* 3 = quem tomou, se documentada, se revisada;; 2 = a maioria;; 1 = um item;; 0 = nenhuma.
- **EX019 — Cláusula de revisão.** O que Westmark pode revisar antes da publicação? *Rubrica:* 3 = somente a exatidão factual;; 2 = correto;; 1 = conteúdo;; 0 = nenhuma.
- **EX020 — Restrição.** Como o Prof. Eriksen restringiu o plano? *Rubrica:* 3 = comparação entre divulgações limitada a dois indicadores;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Replicação da linha de base e estudo piloto

### Objetivos de aprendizagem

Você vai (1) replicar uma linha de base de pareamento de registros; (2) calcular pesos de correspondência e limiares; (3) relatar o compromisso entre precisão e revocação.

### 4.1 Por que replicar primeiro

Antes de testar as próprias ideias, Nadia replica na réplica sintética o método de pareamento publicado por Westmark. Westmark usa a abordagem de Fellegi e Sunter: cada campo contribui com um peso baseado em m, a probabilidade de que uma correspondência verdadeira concorde naquele campo, e em u, a probabilidade de que uma não correspondência concorde por acaso. A concordância soma o logaritmo de m sobre u; a discordância soma o logaritmo de um menos m sobre um menos u. Replicar a linha de base prova que suas ferramentas reproduzem o método antes que ela varie as decisões contidas nele.

### 4.2 O laboratório piloto

O piloto usa 4.000 pares de registros sintéticos, dos quais 400 são correspondências verdadeiras, com os campos nome, código postal e setor. Com limiar 0, ele vincula 505 pares, com precisão de 0,776 e revocação de 0,980. Com limiar 4, vincula 386 pares, com precisão de 0,953 e revocação de 0,920. Com limiar 8, vincula 338 pares, com precisão de 0,991 e revocação de 0,838. Elevar o limiar elimina falsas correspondências, mas perde verdadeiras, de modo que nenhum limiar é livre de erro. Entre os limiares 0 e 4, a precisão ganha muito mais do que a revocação perde, o que sugere que o limiar mais baixo vincula pares falsos demais. Acima de 4, cada ganho de precisão custa visivelmente mais revocação.

### 4.3 Quem escolhe o limiar

Nadia pergunta à equipe de Westmark quem escolheu o limiar atual. A resposta não é clara: um metodologista o definiu anos atrás, e as divulgações seguintes o reutilizaram sem revisão. As entrevistas sugerem que a equipe de produção acredita que o limiar pertence à equipe de métodos, enquanto a equipe de métodos acredita que a produção pode ajustá-lo. É exatamente a lacuna de direitos de decisão que o projeto previa. Ela registra o achado na matriz de decisões e anota que o limiar afeta todas as contagens regionais de emprego que Westmark publica. Nenhuma das equipes tinha um mandato escrito cobrindo essa decisão.

### 4.4 Lições do piloto

O piloto mostra que a réplica e os scripts funcionam, que o compromisso entre precisão e revocação é substancial e que a titularidade do limiar não está clara. Também revela que os valores de m e u foram estimados uma única vez e nunca atualizados, embora o cadastro tenha mudado. O Prof. Eriksen pede a Nadia que trate as estimativas de m e u como mais uma decisão de governança no estudo principal. Ela atualiza o diário de pré-registro para anotar o acréscimo antes de rodar o estudo principal, mantendo a mudança transparente. A transparência vem primeiro.

### Laboratório — Pesos de correspondência, limiares, precisão e revocação

```python
"""Fellegi-Sunter style match weights on synthetic record pairs; precision and recall by threshold (stdlib only)."""
import random, math
random.seed(9)
fields = {"name": (0.95, 0.01), "postcode": (0.90, 0.05), "sector": (0.85, 0.20)}  # (m, u)
pairs = []
for i in range(4000):
    match = i < 400
    agree = {f: (random.random() < (m if match else u)) for f, (m, u) in fields.items()}
    w = sum(math.log2(m / u) if agree[f] else math.log2((1 - m) / (1 - u)) for f, (m, u) in fields.items())
    pairs.append((w, match))
for t in (0, 4, 8):
    pred = [p for p in pairs if p[0] >= t]; tp = sum(1 for p in pred if p[1])
    print(f"threshold {t:2d}: linked {len(pred):4d}  precision {tp/len(pred):.3f}  recall {tp/400:.3f}")
```

Execute com `python3 lab_linkage.py`. Saída verificada:

```text
threshold  0: linked  505  precision 0.776  recall 0.980
threshold  4: linked  386  precision 0.953  recall 0.920
threshold  8: linked  338  precision 0.991  recall 0.838
```

### Exemplo resolvido

Nadia replica os pesos de Fellegi-Sunter em 4.000 pares sintéticos, relata precisão de 0,776 a 0,991 e revocação de 0,980 a 0,838 entre os limiares e constata que a titularidade do limiar não está clara.

> **Caso sintético.** Os pares são sintéticos; Fellegi e Sunter (1969) é real.

### Erros e limites

Supor independência entre os campos, como faz este piloto, pode distorcer os pesos; teste essa suposição mais tarde.

### Exercícios

- **EX021 — Fórmula do peso.** O que a concordância em um campo soma ao peso? *Rubrica:* 3 = log de m sobre u;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX022 — Limiar 4.** Que precisão e revocação ocorrem no limiar 4? *Rubrica:* 3 = 0,953 e 0,920;; 2 = ambas;; 1 = uma;; 0 = nenhuma.
- **EX023 — Limiar mais alto.** O que acontece quando o limiar sobe para 8? *Rubrica:* 3 = menos falsas correspondências, mais verdadeiras perdidas;; 2 = menciona o compromisso;; 1 = nenhuma;; 0 = nenhuma.
- **EX024 — Titular indefinido.** Quem é o titular do limiar em Westmark? *Rubrica:* 3 = não está claro; as equipes apontam uma para a outra;; 2 = menciona indefinição;; 1 = nomeia uma equipe;; 0 = nenhuma.
- **EX025 — Estimativas defasadas.** O que mais nunca havia sido atualizado? *Rubrica:* 3 = as estimativas de m e u;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX026 — Atualização do diário.** O que Nadia fez antes de acrescentar a nova variável? *Rubrica:* 3 = atualizou o diário de pré-registro;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Estudo principal e validação independente

### Objetivos de aprendizagem

Você vai (1) executar a simulação principal das decisões de governança; (2) medir os efeitos sobre as contagens publicadas; (3) validar os resultados de forma independente.

### 5.1 Desenho do estudo principal

O estudo principal varia três decisões dentro de faixas que a equipe de Westmark considerou plausíveis: o limiar de pareamento, de 0 a 8; a reestimação ou não de m e u a cada ano; e a imputação ou não dos códigos de setor em branco. Cada combinação produz um conjunto sintético de contagens regionais de emprego. Nadia roda todas as combinações com sementes aleatórias fixas e armazena as saídas junto com a versão do script. Ela compara cada resultado com uma referência produzida a partir dos vínculos sintéticos verdadeiros, que são conhecidos porque ela mesma gerou os dados.

### 5.2 Efeitos sobre as contagens

Os resultados mostram que o limiar tem o maior efeito. Com limiares baixos, vínculos falsos inflam o emprego em regiões com muitas empresas de nomes parecidos. Com limiares altos, vínculos perdidos reduzem as contagens em regiões onde os códigos postais mudam com frequência. Reestimar m e u reduz os dois tipos de erro. Imputar códigos de setor desloca emprego entre setores, mas quase não altera os totais regionais. Nadia expressa cada efeito como a diferença em relação à referência, para que os leitores vejam quais decisões mais importam e em quais regiões. As regiões pequenas apresentam os maiores erros relativos.

### 5.3 Validação independente

Para validar, o Prof. Eriksen providencia que um pesquisador de outra universidade, que não viu o código de Nadia, implemente o método a partir da descrição escrita dela e o execute em uma nova réplica sintética, gerada com outra semente. Os resultados independentes concordam em direção e magnitude aproximada para as três decisões. Surge uma discrepância porque a descrição de Nadia omitia como os empates no limiar eram tratados. Ela corrige a descrição, mostrando como a validação melhora a documentação, além da confiança nos resultados. As duas execuções são arquivadas.

### 5.4 Interpretando os achados

Nadia relaciona os achados à governança. A decisão de maior efeito, o limiar, é também a de titularidade menos clara. A decisão de menor efeito sobre os totais regionais, a imputação de setor, é a mais documentada, porque consta de um manual publicado. Ela argumenta que, em Westmark, a atenção da governança seguiu a visibilidade, e não o impacto. O Prof. Eriksen a adverte para não generalizar a partir de uma única organização, e ela formula a afirmação como uma hipótese a ser testada por outros institutos de estatística.

### Exemplo resolvido

Nadia varia limiar, reestimação e imputação, constata que o limiar tem o maior efeito sobre as contagens regionais, obtém de um pesquisador independente a reprodução da direção e da magnitude dos efeitos e relaciona o impacto à titularidade pouco clara.

> **Caso sintético.** Os resultados são sintéticos.

### Erros e limites

As faixas plausíveis vêm de entrevistas; outras organizações podem usar faixas mais amplas.

### Exercícios

- **EX027 — Três decisões.** Cite as três decisões variadas. *Rubrica:* 3 = limiar, reestimação de m e u, imputação de setor;; 2 = todas;; 1 = uma;; 0 = nenhuma.
- **EX028 — Maior efeito.** Qual decisão teve o maior efeito? *Rubrica:* 3 = o limiar de pareamento;; 2 = correto;; 1 = outra;; 0 = nenhuma.
- **EX029 — Limiar baixo.** O que acontece com as contagens em limiares baixos? *Rubrica:* 3 = vínculos falsos inflam as contagens;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX030 — Método de validação.** Por que a validação foi independente? *Rubrica:* 3 = outro pesquisador reimplementou a partir da descrição com nova semente;; 2 = menciona reimplementação;; 1 = nenhuma;; 0 = nenhuma.
- **EX031 — Discrepância.** O que causou a discrepância na validação? *Rubrica:* 3 = tratamento não documentado de empates no limiar;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX032 — Atenção.** O que a atenção da governança seguiu em Westmark? *Rubrica:* 3 = a visibilidade, e não o impacto;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Crítica dos pares e revisão

### Objetivos de aprendizagem

Você vai (1) responder à crítica dos pares sobre pesquisa em governança; (2) revisar análises de forma transparente; (3) fortalecer a seção de limitações.

### 6.1 A crítica

Nadia apresenta seus resultados em um seminário de doutorado. Os colegas levantam três críticas. Primeira: a réplica sintética pode subestimar a variação de nomes do mundo real, o que alteraria o erro de pareamento. Segunda: as entrevistas com a equipe de Westmark podem refletir a esquiva de culpa, já que ninguém quer admitir ser o titular de um limiar mal escolhido. Terceira: a afirmação de que a documentação reduz a variação se apoia em apenas duas divulgações. O Prof. Eriksen lhe diz que uma boa crítica é um presente, porque aponta fraquezas antes que examinadores ou usuários as encontrem. Ela anota cada crítica literalmente.

### 6.2 Respondendo à variação de nomes

Nadia acrescenta uma análise de sensibilidade em que a concordância de nomes é menos confiável, reduzindo o m dos nomes de 0,95 para 0,85. O erro de pareamento aumenta em todos os limiares, mas a ordenação das decisões por efeito permanece a mesma. Ela relata as duas versões e explica que a magnitude dos efeitos é incerta, enquanto a ordenação é robusta. Também observa que a NIST SP 800-188 discute como dados sintéticos podem preservar algumas propriedades e não outras, de modo que os analistas precisam declarar em quais propriedades se apoiaram. As duas análises são arquivadas juntas.

### 6.3 Respondendo ao viés das entrevistas

Para tratar a possível esquiva de culpa, Nadia compara as respostas das entrevistas com documentos como notas de divulgação, atas de reunião e solicitações de mudança. Os documentos confirmam que não há registro de revisão do limiar desde a escolha original. Mostram também que a equipe de métodos propôs uma revisão dois anos atrás, que nunca foi agendada. A triangulação reforça o achado de que a titularidade não estava clara e, ao mesmo tempo, atenua qualquer insinuação de que indivíduos ignoraram o problema. Ela reescreve o texto para descrever uma lacuna estrutural, e não uma falha pessoal. Os documentos encerram a questão.

### 6.4 Limitando a afirmação sobre documentação

Com apenas duas divulgações, Nadia não consegue mostrar que a documentação causa a redução da variação. Ela reescreve a terceira afirmação como uma observação compatível com a hipótese e propõe um desenho de continuidade em que Westmark documenta as decisões de quatro divulgações enquanto uma série de comparação segue sem documentação. O Prof. Eriksen aprova a revisão. Nadia registra cada mudança no diário de decisões, incluindo a redação original, para que os examinadores vejam como a tese respondeu à crítica em vez de deslocar suas afirmações em silêncio. Examinadores valorizam muito essa honestidade.

### Exemplo resolvido

Nadia responde às críticas com uma análise de sensibilidade sobre a concordância de nomes, triangula as entrevistas com documentos e reformula a afirmação sobre documentação como compatível, mas não causal.

> **Caso sintético.** O seminário é sintético; a NIST SP 800-188 é real.

### Erros e limites

Análises de sensibilidade testam apenas as alternativas escolhidas; outras podem importar.

### Exercícios

- **EX033 — Crítica sobre nomes.** Que crítica dizia respeito aos nomes? *Rubrica:* 3 = a réplica pode subestimar a variação de nomes;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX034 — Mudança na sensibilidade.** Como Nadia testou a variação de nomes? *Rubrica:* 3 = reduziu o m dos nomes de 0,95 para 0,85;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX035 — Resultado robusto.** O que permaneceu igual na análise de sensibilidade? *Rubrica:* 3 = a ordenação das decisões por efeito;; 2 = correto;; 1 = as magnitudes;; 0 = nenhuma.
- **EX036 — Triangulação.** O que os documentos mostraram sobre revisões do limiar? *Rubrica:* 3 = nenhuma desde a escolha original; uma proposta nunca agendada;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX037 — Redação estrutural.** Como Nadia reescreveu o texto sobre titularidade? *Rubrica:* 3 = uma lacuna estrutural, não falha pessoal;; 2 = correto;; 1 = culpa;; 0 = nenhuma.
- **EX038 — Desenho de continuidade.** Que continuidade Nadia propôs? *Rubrica:* 3 = quatro divulgações documentadas contra uma série de comparação;; 2 = menciona comparação;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Síntese da tese e arquivo de reprodutibilidade

### Objetivos de aprendizagem

Você vai (1) sintetizar os achados em uma tese coerente; (2) montar um arquivo de reprodutibilidade; (3) avaliar o arquivo à luz dos princípios FAIR.

### 7.1 O argumento da tese

A tese de Nadia sustenta que, no contexto estudado, as decisões de governança sobre pareamento e regras de qualidade moldam as estatísticas oficiais tanto quanto a coleta de dados, e que as decisões mais influentes receberam a menor atenção da governança. Cada capítulo sustenta uma etapa: a matriz de decisões, a replicação da linha de base, a simulação principal, a validação e a resposta à crítica. Ela escreve o argumento em uma página antes de revisar os capítulos, para que cada seção contribua para a afirmação e nada entre apenas porque foi um trabalho que ela fez.

### 7.2 O arquivo de reprodutibilidade

Nadia monta um arquivo com o gerador da réplica, os scripts de análise, as sementes fixas, as saídas esperadas, o diário de decisões, o protocolo de entrevistas e o quadro de codificação anonimizado. O material confidencial, incluindo quaisquer documentos internos de Westmark, fica de fora e é apenas descrito. Os princípios FAIR de Wilkinson e colegas estabelecem que dados e metadados devem ser localizáveis, acessíveis, interoperáveis e reutilizáveis (*findable, accessible, interoperable, reusable*), com identificadores persistentes, metadados ricos, vocabulários padronizados, licenças claras e proveniência. Ela trata os princípios como metas de projeto para o arquivo, e não como um certificado que ele tem ou não tem.

### 7.3 Verificando as propriedades FAIR

Para testar o arquivo diante dessas metas, Nadia avalia quatro registros sintéticos de conjuntos de dados com uma lista de verificação de oito itens. O laboratório informa que o registro do cadastro empresarial atende 8 de 8 itens, o registro de emprego vinculado 4 de 8, a pesquisa de comércio 4 de 8 e o extrato piloto 1 de 8, uma média de 0,53. Ao registro de emprego vinculado faltam identificador persistente, entrada em índice de busca, vocabulário padronizado e licença, o que dificultaria o reúso até para colegas dentro de Westmark. O extrato piloto atende apenas ao item de protocolo aberto, algo típico de arquivos produzidos às pressas para um teste e nunca descritos depois. Esses arquivos são os primeiros a se tornar inutilizáveis.

### 7.4 Melhorando o arquivo

Nadia aplica as lições ao próprio arquivo. Obtém um identificador persistente pelo repositório da universidade, escreve metadados que descrevem as variáveis com códigos padronizados, escolhe uma licença aberta para o código e os dados sintéticos e documenta a proveniência desde o gerador até cada figura. As condições de acesso informam que microdados confidenciais não estão incluídos e explicam como pesquisadores podem solicitá-los separadamente a Westmark. O Prof. Eriksen testa o arquivo pedindo a um aluno novo que regenere duas figuras; o aluno consegue, sem ajuda, em uma tarde. Nenhuma etapa exigiu a ajuda de Nadia.

### Laboratório — Pontuação FAIR de registros de conjuntos de dados

```python
"""Score synthetic dataset metadata records against a simple FAIR checklist (stdlib only)."""
checks = ["persistent_id", "rich_metadata", "searchable_index", "open_protocol", "access_conditions",
          "standard_vocabulary", "licence", "provenance"]
sets = {
    "business_register_2025": {"persistent_id", "rich_metadata", "searchable_index", "open_protocol", "licence", "provenance", "standard_vocabulary", "access_conditions"},
    "linked_employment_2024": {"rich_metadata", "open_protocol", "access_conditions", "provenance"},
    "trade_survey_2023":      {"persistent_id", "searchable_index", "open_protocol", "licence"},
    "pilot_linkage_extract":  {"open_protocol"},
}
for name, have in sets.items():
    miss = [c for c in checks if c not in have]
    print(f"{name:24s} {len(have)}/{len(checks)}  missing: {', '.join(miss) if miss else '-'}")
avg = sum(len(h) for h in sets.values()) / (len(sets) * len(checks))
print(f"mean checklist score {avg:.2f}")
```

Execute com `python3 lab_fair.py`. Saída verificada:

```text
business_register_2025   8/8  missing: -
linked_employment_2024   4/8  missing: persistent_id, searchable_index, standard_vocabulary, licence
trade_survey_2023        4/8  missing: rich_metadata, access_conditions, standard_vocabulary, provenance
pilot_linkage_extract    1/8  missing: persistent_id, rich_metadata, searchable_index, access_conditions, standard_vocabulary, licence, provenance
mean checklist score 0.53
```

### Exemplo resolvido

Nadia escreve o argumento da tese em uma página, monta um arquivo que exclui material confidencial, avalia quatro registros sintéticos de 8 de 8 a 1 de 8 (média de 0,53) e melhora o próprio arquivo até que um aluno novo regenere figuras sem ajuda.

> **Caso sintético.** Os registros de conjuntos de dados são sintéticos; Wilkinson et al. (2016) é real.

### Erros e limites

Uma lista de verificação simplifica os princípios FAIR; alguns itens exigem julgamento, não apenas marcações.

### Exercícios

- **EX039 — Afirmação da tese.** Qual é a afirmação central da tese? *Rubrica:* 3 = decisões de governança moldam estatísticas; as mais influentes recebem menos atenção;; 2 = menciona atenção;; 1 = nenhuma;; 0 = nenhuma.
- **EX040 — Letras FAIR.** O que significam as letras de FAIR? *Rubrica:* 3 = localizável, acessível, interoperável, reutilizável;; 2 = todas;; 1 = duas;; 0 = nenhuma.
- **EX041 — Registro vinculado.** Que pontuação obteve o registro de emprego vinculado? *Rubrica:* 3 = 4 de 8;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX042 — Média.** Qual foi a pontuação média da lista? *Rubrica:* 3 = 0,53;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX043 — Conteúdo excluído.** O que Nadia exclui do arquivo? *Rubrica:* 3 = material confidencial de Westmark;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX044 — Teste do arquivo.** Como o Prof. Eriksen testou o arquivo? *Rubrica:* 3 = um aluno novo regenerou duas figuras;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Defesa e plano de publicação

### Objetivos de aprendizagem

Você vai (1) defender uma pesquisa em governança diante de uma banca; (2) planejar a publicação de forma responsável; (3) transferir os achados para a prática.

### 8.1 Preparando a defesa

Nadia se prepara listando as perguntas mais difíceis que espera: por que uma réplica sintética é crível, se uma única organização sustenta afirmações gerais, como o viés das entrevistas foi tratado e o que Westmark deveria fazer de outro modo. Para cada uma, escreve uma resposta curta que cita sua evidência e um limite que ela aceita. O Prof. Eriksen conduz uma defesa simulada em que faz o papel de examinador cético e a pressiona sobre o compromisso entre precisão e revocação até que ela consiga explicá-lo sem slides. Cada resposta cabe em uma ficha.

### 8.2 A defesa

Na defesa, o examinador externo pergunta por que Westmark não deveria simplesmente escolher o limiar que maximiza a precisão. Nadia explica que maximizar a precisão reduz a revocação e subcontabiliza as regiões com códigos postais instáveis; portanto, a escolha depende de qual erro os usuários podem tolerar, o que é uma decisão de governança, e não um fato técnico. O examinador também pergunta sobre o arquivo de reprodutibilidade e regenera uma figura durante a sessão. A banca aprova a tese com correções menores no capítulo de limitações. As correções levam duas semanas.

### 8.3 Plano de publicação

Nadia planeja três artigos: um artigo metodológico sobre a simulação de decisões de governança, um artigo empírico sobre direitos de decisão em um instituto de estatística e uma nota técnica curta para estatísticos oficiais. Cada artigo aponta para o arquivo. Westmark revisa os rascunhos quanto à exatidão factual, como combinado, e não pede mudanças de conteúdo. Ela escolhe periódicos de acesso aberto sempre que possível, porque os achados dizem respeito a estatísticas públicas e devem poder ser lidos pelas pessoas que dependem delas, e não apenas por assinantes. A nota técnica vem primeiro, porque o próximo ciclo de divulgação de Westmark começa em poucos meses.

### 8.4 Transferência para a prática

Nadia apresenta um resumo ao conselho diretor de Westmark. Recomenda nomear um titular para o limiar de pareamento, revisar as estimativas de m e u todo ano, documentar as decisões de cada divulgação e publicar estimativas de precisão e revocação junto com as contagens regionais. O conselho aceita as três primeiras e pede um piloto da quarta. O Prof. Eriksen observa que o sinal mais forte de uma tese útil é que suas recomendações podem ser verificadas: a divulgação do ano seguinte mostrará se foram adotadas. Nadia se oferece para revisar o piloto.

### Exemplo resolvido

Nadia ensaia perguntas difíceis, defende a escolha do limiar como decisão de governança, planeja três artigos com um arquivo aberto e recomenda titularidade do limiar, reestimação anual, documentação e publicação das estimativas de erro.

> **Caso sintético.** A defesa e o conselho são sintéticos.

### Erros e limites

Cronogramas de publicação atrasam; priorize o artigo que mais afeta a prática.

### Exercícios

- **EX045 — Pergunta sobre precisão.** Por que não simplesmente maximizar a precisão? *Rubrica:* 3 = a revocação cai e algumas regiões são subcontabilizadas;; 2 = menciona revocação;; 1 = nenhuma;; 0 = nenhuma.
- **EX046 — Escolha de governança.** Que tipo de decisão é escolher o erro tolerável? *Rubrica:* 3 = uma decisão de governança;; 2 = correto;; 1 = técnica;; 0 = nenhuma.
- **EX047 — Resultado da defesa.** Qual foi o resultado da defesa? *Rubrica:* 3 = aprovação com correções menores;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX048 — Artigos.** Quantos artigos Nadia planeja? *Rubrica:* 3 = três;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX049 — Decisões do conselho.** Qual recomendação o conselho levou a piloto em vez de adotar? *Rubrica:* 3 = publicar estimativas de precisão e revocação;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX050 — Recomendações verificáveis.** Por que recomendações verificáveis são valiosas? *Rubrica:* 3 = a próxima divulgação mostra a adoção;; 2 = menciona verificação;; 1 = nenhuma;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX050. Nadia Rahman, o Prof. Lars Eriksen, a Universidade Halvorsen, o Instituto de Estatística de Westmark e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Como as decisões sobre regras de qualidade e limiares de pareamento alteram as estatísticas que as pessoas leem.

**EX002.** Como a decisão sobre quem detém os direitos de decisão sobre os dados.

**EX003.** Apenas uma réplica sintética construída a partir de distribuições publicadas.

**EX004.** Cada número deve remeter a uma execução de script sob controle de versão.

**EX005.** Para que as hipóteses não possam ser remodeladas depois de ver os resultados.

**EX006.** Direitos de decisão pouco claros levam a limiares de pareamento inconsistentes entre divulgações.

**EX007.** No órgão de governança da organização.

**EX008.** Dimensões como atualidade e relevância, valorizadas pelos consumidores.

**EX009.** 0,798.

**EX010.** Muitos registros não têm código de setor ou código postal.

**EX011.** Alguns números de registro aparecem duas vezes.

**EX012.** Permitir setores em branco para empresas novas mudou a regra, não os dados.

**EX013.** Conceitos e pré-requisitos para medir a qualidade da informação e dos dados.

**EX014.** Vínculos empíricos entre decisões sobre regras de qualidade e os produtos publicados.

**EX015.** Decisões alternativas de pareamento mudam de forma relevante as contagens regionais de emprego.

**EX016.** A proporção de pares vinculados que são correspondências verdadeiras.

**EX017.** A proporção de correspondências verdadeiras que foram vinculadas.

**EX018.** Por quem a tomou, se foi documentada e se foi revisada.

**EX019.** Apenas a exatidão factual, não o conteúdo.

**EX020.** Limitou a comparação entre divulgações a dois indicadores.

**EX021.** O logaritmo de m dividido por u.

**EX022.** Precisão de 0,953 e revocação de 0,920.

**EX023.** A precisão sobe para 0,991, mas a revocação cai para 0,838.

**EX024.** Ninguém, de forma clara; cada equipe acredita que o titular é a outra.

**EX025.** As estimativas das probabilidades m e u.

**EX026.** Primeiro atualizou o diário de pré-registro.

**EX027.** Limiar de pareamento, reestimação de m e u e imputação de setor.

**EX028.** O limiar de pareamento.

**EX029.** Vínculos falsos inflam o emprego em algumas regiões.

**EX030.** Um pesquisador reimplementou o método a partir da descrição dela em uma nova réplica.

**EX031.** A descrição omitia como os empates no limiar eram tratados.

**EX032.** A visibilidade, não o impacto.

**EX033.** A réplica pode subestimar a variação real de nomes.

**EX034.** Reduziu o valor de m dos nomes de 0,95 para 0,85.

**EX035.** A ordenação das decisões por efeito.

**EX036.** Nenhuma revisão desde a escolha original, e uma revisão proposta nunca foi agendada.

**EX037.** Como uma lacuna estrutural, e não uma falha pessoal.

**EX038.** Documentar quatro divulgações enquanto uma série de comparação segue sem documentação.

**EX039.** Decisões de governança influentes moldam as estatísticas, mas recebem a menor atenção.

**EX040.** Localizável, acessível, interoperável e reutilizável.

**EX041.** Quatro de oito.

**EX042.** 0,53.

**EX043.** Material confidencial, como documentos internos.

**EX044.** Um aluno novo regenerou duas figuras sem ajuda.

**EX045.** Mais precisão reduz a revocação e subcontabiliza regiões com códigos postais instáveis.

**EX046.** Uma decisão de governança sobre qual erro os usuários podem aceitar.

**EX047.** Aprovação com correções menores no capítulo de limitações.

**EX048.** Três.

**EX049.** Publicar estimativas de precisão e revocação junto com as contagens.

**EX050.** A próxima divulgação mostrará se foram adotadas.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. As referências são mantidas idênticas às da edição em inglês; nenhuma das normas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Batini, C., Cappiello, C., Francalanci, C., & Maurino, A. (2009). Methodologies for data quality assessment and improvement. *ACM Computing Surveys, 41*(3), 1–52. https://doi.org/10.1145/1541880.1541883
- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- Fellegi, I. P., & Sunter, A. B. (1969). A theory for record linkage. *Journal of the American Statistical Association, 64*(328), 1183–1210. https://doi.org/10.1080/01621459.1969.10501049
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-188
- ISO. (2015). *ISO 8000-8:2015 Data quality — Part 8: Information and data quality: Concepts and measuring*. International Organization for Standardization. <https://www.iso.org/standard/60805.html>
- ISO/IEC. (2017). *ISO/IEC 38505-1:2017 Information technology — Governance of IT — Governance of data — Part 1: Application of ISO/IEC 38500 to the governance of data*. <https://www.iso.org/standard/56639.html>
- Khatri, V., & Brown, C. V. (2010). Designing data governance. *Communications of the ACM, 53*(1), 148–152. https://doi.org/10.1145/1629175.1629210
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., et al. (2016). The FAIR guiding principles for scientific data management and stewardship. *Scientific Data, 3*, 160018. https://doi.org/10.1038/sdata.2016.18
