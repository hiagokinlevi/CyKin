# Privacidade e Proteção de Dados: Trilha de Pesquisa de Doutorado

- Idioma: português do Brasil (`pt`); curso 188, trilha de pesquisa de doutorado (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–8 de 8 têm texto didático escrito à mão; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; os cinco laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: doutorandos que comparam registros k-anonimizados com contagens diferencialmente privadas em uma publicação de dados do setor público.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios medem a unicidade, generalizam registros até k = 5, acrescentam ruído de Laplace a contagens, executam um ataque de vinculação e conferem um arquivo em busca de identificadores, sempre sobre uma população sintética com semente fixa. A análise jurídica é didática e não constitui aconselhamento jurídico; a LGPD e os atos da ANPD são citados pelo texto oficial e parafraseados. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma doutoranda que compara métodos de publicação de dados de transporte: integridade e uma linha de base de unicidade, a fronteira da pesquisa, o projeto, o piloto de privacidade diferencial, o estudo principal de vinculação e sua validação, a crítica dos pares, a síntese e o arquivo, e a defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Ines Carvalho** | Doutoranda | Inventada |
| **Prof. Henrik Aaltonen** | Orientador | Inventado |
| **Thornbury University** | Universidade fictícia | Inventada |
| **Valemont Regional Transit Authority** | Autoridade de transporte fictícia que publica dados de viagens com cartão eletrônico | Inventada |

### Fontes principais

Regulamento (UE) 2016/679 (GDPR); Lei nº 13.709/2018 (LGPD); Resolução CD/ANPD nº 18/2024; Sweeney (2002), [doi:10.1142/S0218488502001648](https://doi.org/10.1142/S0218488502001648); Dwork et al. (2006) e Dwork e Roth (2014), [doi:10.1561/0400000042](https://doi.org/10.1561/0400000042); Narayanan e Shmatikov (2008); Solove (2006); Nissenbaum (2004, 2009); NISTIR 8053 e NIST SP 800-188; Diretrizes 4/2019 do EDPB. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Integridade e métodos avançados de pesquisa

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta falseável sobre publicação de dados com preservação de privacidade; (2) definir regras de integridade para pesquisas que envolvem dados pessoais; (3) medir com que rapidez atributos comuns tornam as pessoas únicas.

### 1.1 Uma pergunta falseável

Ines Carvalho é doutoranda na fictícia Thornbury University, sob orientação do Prof. Henrik Aaltonen. Sua parceira é a fictícia Valemont Regional Transit Authority, que coleta as viagens feitas com cartão eletrônico e quer publicar dados de deslocamento para os planejadores urbanos. Ines pergunta se publicar contagens de origem e destino com privacidade diferencial protege os passageiros melhor do que publicar registros de viagens k-anonimizados, com uma utilidade que os planejadores ainda aceitem. Antes de coletar qualquer coisa, ela escreve quais resultados provariam que está errada: nenhuma redução mensurável no risco de vinculação, ou um erro tão grande que os planejadores rejeitem as contagens nas decisões rotineiras de quadro de horários.

### 1.2 Por que a pergunta importa

A pergunta importa porque dados de transporte parecem inofensivos, mas revelam onde as pessoas moram, trabalham e rezam. Pelo Regulamento (UE) 2016/679, o GDPR, dados que permitem singularizar uma pessoa continuam sendo dados pessoais, enquanto o Considerando 26 deixa a informação verdadeiramente anônima fora do regulamento. A LGPD brasileira, Lei nº 13.709/2018, traça uma linha semelhante: dado anonimizado é o dado relativo a titular que não possa ser identificado, considerando os meios técnicos razoáveis e disponíveis na ocasião do tratamento (art. 5º, III), e esse dado não é considerado pessoal, salvo quando a anonimização puder ser revertida com esforços razoáveis (art. 12). Saber se uma publicação é anônima é, portanto, uma questão jurídica e também técnica. Ines a trata como uma afirmação empírica a ser testada, e não como um rótulo que a autoridade possa simplesmente aplicar a uma planilha antes de publicá-la.

### 1.3 Regras de integridade

A pesquisa com dados pessoais não pode criar o dano que estuda. O protocolo de Ines, aprovado pelo comitê de ética da Thornbury e revisado pelo encarregado de proteção de dados da Valemont, fixa cinco regras. Ela trabalha apenas com uma população sintética gerada para reproduzir estatísticas agregadas já publicadas; nenhum número real de cartão sai da autoridade; todo experimento de ataque mira a população sintética, nunca passageiros reais; o plano de análise é pré-registrado antes que os resultados sejam vistos; e todo arquivo que deixa o ambiente seguro é conferido em busca de identificadores diretos. Ela também declara que não tem interesse comercial em nenhum produto ou consultoria de anonimização.

### 1.4 A unicidade como linha de base

Antes de comparar métodos de publicação, Ines mede quão identificadores são atributos comuns. Sweeney (2002) mostrou que poucos quase-identificadores, como código postal, data de nascimento e sexo, bastam para singularizar a maioria das pessoas, o que motivou o modelo de k-anonimato. O laboratório cria 20.000 passageiros sintéticos com uma zona de residência, uma zona de trabalho, um ano de nascimento e um sexo, e depois conta a parcela que é única em combinações crescentes. A zona de residência sozinha não singulariza ninguém, e residência mais trabalho também não, mas acrescentar o ano de nascimento torna 83,4% únicos, e acrescentar o sexo eleva a proporção para 91,5% da população sintética.

### Laboratório — Unicidade de passageiros sintéticos em quase-identificadores

```python
# Share of synthetic transit riders who are unique on combinations of quasi-identifiers.
import random
from collections import Counter
r = random.Random(7)
riders = [(r.randrange(40), r.randrange(40), r.randrange(1940, 2008), r.choice("FM")) for _ in range(20000)]
def unique(cols):
    keys = [tuple(x[c] for c in cols) for x in riders]
    c = Counter(keys)
    return sum(1 for k in keys if c[k] == 1) / len(keys)
for name, cols in [("home zone", (0,)), ("home + work zone", (0, 1)),
                   ("home + work + birth year", (0, 1, 2)), ("home + work + birth year + sex", (0, 1, 2, 3))]:
    print(f"{name:32s} unique {unique(cols):6.1%}")
```

Execute com `python3 lab_unique.py`. Saída verificada:

```text
home zone                        unique   0.0%
home + work zone                 unique   0.0%
home + work + birth year         unique  83.4%
home + work + birth year + sex   unique  91.5%
```

### Exemplo resolvido

Ines formula uma comparação falseável entre registros k-anonimizados e contagens diferencialmente privadas, define regras de integridade para a pesquisa com dados de transporte e registra uma linha de base: 83,4% dos passageiros sintéticos são únicos na combinação de zona de residência, zona de trabalho e ano de nascimento.

> **Caso sintético.** A Thornbury, a Valemont e todos os passageiros são sintéticos; o GDPR, a LGPD e Sweeney (2002) são reais.

### Erros e limites

A unicidade em uma população sintética apenas se aproxima da unicidade na população real. Ser único não é o mesmo que ser reidentificado; o atacante também precisa de conhecimento externo.

### Exercícios

- **EX001 — Plano falseável.** O que torna falseável a pergunta de pesquisa de Ines? *Rubrica:* 3 = ela lista de antemão os resultados que a refutariam: nenhuma queda no risco de vinculação ou um erro inaceitável;; 2 = menciona vagamente resultados definidos antes;; 1 = diz que é uma boa pergunta;; 0 = nenhuma.
- **EX002 — Anônimo na lei.** Por que "anônimo" é, para a autoridade, uma questão jurídica e também técnica? *Rubrica:* 3 = o Considerando 26 do GDPR e a LGPD deixam os dados anônimos fora da lei, então o rótulo muda os deveres legais;; 2 = cita uma só lei;; 1 = diz que é técnica;; 0 = nenhuma.
- **EX003 — População sintética.** Por que Ines trabalha com uma população sintética em vez de cartões reais? *Rubrica:* 3 = isso permite executar ataques e publicar resultados sem expor nem reidentificar passageiros reais;; 2 = diz que é mais fácil;; 1 = diz que os dados reais não estão disponíveis;; 0 = nenhuma.
- **EX004 — Salto de unicidade.** Que atributo causa o maior salto de unicidade no laboratório, e por quê? *Rubrica:* 3 = o ano de nascimento: de 0% para 83,4%, porque divide cada par de zonas em muitos grupos pequenos;; 2 = cita o ano de nascimento sem números;; 1 = cita a zona;; 0 = nenhuma.
- **EX005 — Único versus identificado.** Por que a unicidade ainda não é reidentificação? *Rubrica:* 3 = o atacante também precisa de conhecimento externo que ligue a combinação única a uma pessoa nomeada;; 2 = diz que são diferentes;; 1 = trata as duas como iguais;; 0 = nenhuma.
- **EX006 — Declaração de interesses.** Por que Ines declara não ter interesse comercial? *Rubrica:* 3 = os leitores podem avaliar o viés; um interesse em produto poderia inclinar a comparação de métodos;; 2 = diz que é obrigatório;; 1 = omite as razões;; 0 = nenhuma.
- **EX007 — Valor do pré-registro.** Contra o que o pré-registro do plano de análise protege? *Rubrica:* 3 = contra escolher métricas ou limiares depois de ver resultados que favorecem um método;; 2 = menciona viés em geral;; 1 = diz que é burocracia;; 0 = nenhuma.

### Síntese

O capítulo 1 define uma pergunta falseável, regras de integridade e uma linha de base de unicidade. O capítulo 2 mapeia a fronteira da pesquisa, de Warren e Brandeis à privacidade diferencial.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 08)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Privacidade e proteção de dados: fronteira da pesquisa

### Objetivos de aprendizagem

Você vai (1) traçar o desenvolvimento da teoria da privacidade; (2) contrastar os modelos sintáticos de anonimato com a privacidade diferencial; (3) localizar a lacuna que o estudo de Ines aborda.

### 2.1 Do direito de ser deixado em paz

Ines começa sua revisão por Warren e Brandeis (1890), que defenderam na Harvard Law Review um direito à privacidade contra a fotografia invasiva e a fofoca. Mais tarde, Solove (2006) argumentou que a privacidade não é uma coisa só e ofereceu uma taxonomia de atividades danosas, agrupadas em coleta de informações, processamento de informações, disseminação de informações e invasão. Nissenbaum (2004, 2009) propôs a integridade contextual: um fluxo de informação é apropriado quando respeita as normas do contexto em que a informação foi compartilhada. Para dados de transporte, a integridade contextual pergunta se os passageiros esperam que suas viagens cheguem, de alguma forma, aos planejadores urbanos.

### 2.2 Modelos sintáticos de anonimato

A primeira família técnica protege os registros fazendo com que se pareçam uns com os outros. Sweeney (2002) definiu o k-anonimato: cada combinação de quase-identificadores deve ser compartilhada por pelo menos k registros. Machanavajjhala e colegas (2007) mostraram que um grupo k-anônimo ainda pode revelar um valor sensível se todos nele tiverem esse mesmo valor, e propuseram a l-diversidade. Li, Li e Venkatasubramanian (2007) propuseram a t-proximidade (t-closeness), que exige que a distribuição sensível de cada grupo fique próxima da distribuição geral. Ines observa que cada modelo foi proposto depois de um ataque ao anterior, o que sugere que as garantias sintáticas dependem de hipóteses sobre o atacante.

### 2.3 Vinculação e desanonimização

Narayanan e Shmatikov (2008) mostraram que um conjunto supostamente anônimo de avaliações de filmes podia ser vinculado a resenhas públicas usando apenas algumas avaliações conhecidas, porque registros esparsos são muito distintivos. O resultado se generaliza para as viagens de transporte, que também são esparsas e distintivas. O relatório de Garfinkel para o NIST sobre desidentificação (NISTIR 8053, 2015) e a NIST SP 800-188 (2023) descrevem a posição prática que resulta disso: remover nomes não basta, o risco de reidentificação precisa ser estimado, e a escolha do método deve depender do modelo de publicação, seja público, restrito ou em ambiente controlado (enclave), bem como dos usuários pretendidos dos dados.

### 2.4 Privacidade diferencial

A segunda família protege o resultado de uma análise, e não os registros. Dwork, McSherry, Nissim e Smith (2006) introduziram a calibração do ruído pela sensibilidade da consulta: se acrescentar ou retirar uma pessoa muda uma contagem em no máximo um, o ruído de Laplace com escala de um sobre épsilon torna a contagem publicada quase igualmente provável com ou sem aquela pessoa. Dwork e Roth (2014) apresentam os fundamentos formais. A garantia vale seja qual for o conhecimento prévio do atacante, o que responde à fraqueza dos modelos sintáticos, mas custa precisão, e o custo é maior nas contagens pequenas, como estações pouco movimentadas e viagens raras.

### 2.5 A lacuna

Ines encontra muitas comparações teóricas e muitos estudos de caso com um único método, mas poucos estudos que comparem as duas famílias sobre a mesma publicação, meçam o risco com o mesmo ataque e perguntem a usuários reais se o resultado continua útil. Essa é a sua lacuna. Sua contribuição será empírica e prática: uma comparação controlada sobre uma única população sintética de transporte, com a aceitação dos planejadores como critério explícito de utilidade. Ela escreve a lacuna em uma única frase para sua banca e a confronta com a pergunta falseável do Capítulo 1, para que a revisão e o desenho do estudo apontem exatamente para a mesma incerteza.

### Exemplo resolvido

Ines agrupa a literatura em teoria (Warren e Brandeis, Solove, Nissenbaum), modelos sintáticos (Sweeney, l-diversidade, t-proximidade), ataques (Narayanan e Shmatikov) e privacidade diferencial (Dwork e colegas), e identifica uma lacuna: a comparação na mesma publicação com um teste de utilidade feito pelos usuários.

> **Caso sintético.** Todas as obras citadas são reais e constam das referências; a síntese de Ines é uma ilustração didática.

### Erros e limites

Um mapa da literatura simplifica; a privacidade diferencial também tem variantes e sofre ataques às suas implementações. A integridade contextual é uma teoria normativa, não uma métrica.

### Exercícios

- **EX008 — Integridade contextual.** Como a integridade contextual julgaria o envio de dados de viagem aos planejadores? *Rubrica:* 3 = pergunta se o fluxo respeita as normas que os passageiros esperavam ao passar o cartão;; 2 = menciona normas;; 1 = diz que é legal;; 0 = nenhuma.
- **EX009 — Grupos de Solove.** Cite os quatro grupos de problemas de privacidade de Solove. *Rubrica:* 3 = coleta, processamento, disseminação, invasão;; 2 = cita três;; 1 = cita um;; 0 = nenhuma.
- **EX010 — Motivo da l-diversidade.** Que fraqueza do k-anonimato levou à l-diversidade? *Rubrica:* 3 = um grupo k-anônimo pode compartilhar um único valor sensível, revelando-o para todos os membros;; 2 = menciona valores sensíveis;; 1 = repete a definição de k-anonimato;; 0 = nenhuma.
- **EX011 — Registros esparsos.** Por que o resultado de Narayanan e Shmatikov importa para dados de transporte? *Rubrica:* 3 = as viagens são esparsas e distintivas como as avaliações, então poucas viagens conhecidas podem vincular um registro;; 2 = diz que a vinculação é possível;; 1 = cita apenas o caso dos filmes;; 0 = nenhuma.
- **EX012 — Sentido da sensibilidade.** O que é a sensibilidade de uma consulta de contagem, e por que ela importa? *Rubrica:* 3 = o máximo que uma pessoa pode alterá-la, um; a escala do ruído é a sensibilidade sobre épsilon;; 2 = define sensibilidade de modo vago;; 1 = cita apenas o épsilon;; 0 = nenhuma.
- **EX013 — Conhecimento prévio.** Que vantagem a privacidade diferencial tem sobre os modelos sintáticos? *Rubrica:* 3 = sua garantia vale independentemente do conhecimento prévio do atacante;; 2 = menciona atacantes;; 1 = diz que é mais nova;; 0 = nenhuma.
- **EX014 — Enunciado da lacuna.** Enuncie em uma frase a lacuna de pesquisa de Ines. *Rubrica:* 3 = poucos estudos comparam as duas famílias em uma publicação, com um ataque e um teste de utilidade com usuários;; 2 = menciona comparação;; 1 = diz que é preciso mais pesquisa;; 0 = nenhuma.

### Síntese

O capítulo 2 mapeia teoria, modelos, ataques e privacidade diferencial até chegar a uma lacuna precisa. O capítulo 3 transforma a lacuna em uma proposta com uma linha de base de generalização.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 08)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Proposta de contribuição original

### Objetivos de aprendizagem

Você vai (1) escrever um projeto de doutorado com hipóteses e critérios; (2) generalizar registros até alcançar o k-anonimato; (3) explicar o custo de utilidade da generalização.

### 3.1 Hipóteses

Ines enuncia duas hipóteses. H1: uma publicação diferencialmente privada de contagens de origem e destino com épsilon igual a um produz um risco de vinculação medido menor do que um arquivo de viagens k-anonimizado com k igual a cinco. H2: os planejadores aceitarão as contagens diferencialmente privadas para decisões de quadro de horários com esse épsilon, o que se define como pelo menos dois de três planejadores avaliando-as como utilizáveis. Cada hipótese tem um critério mensurável e um limiar declarado antes que os dados existam. O Prof. Aaltonen pede que ela justifique os dois limiares por escrito, e ela o faz citando a prática atual de planejamento da autoridade e a tolerância de erro que os planejadores já aceitam nas pesquisas manuais.

### 3.2 A generalização como linha de base

Para construir uma linha de base justa, Ines precisa produzir um arquivo k-anônimo que um curador de dados competente de fato publicaria. Ela generaliza as zonas em blocos e os anos de nascimento em faixas, e todo passageiro que ainda fique em um grupo menor que cinco é suprimido. O laboratório testa quatro configurações sobre 20.000 passageiros sintéticos. Os valores exatos suprimiriam todos os registros; blocos de duas zonas com faixas de cinco anos ainda suprimem 51,4%; blocos de quatro zonas com faixas de cinco anos suprimem apenas 0,1%; e blocos de oito zonas com faixas de dez anos não suprimem nenhum. Cada passo que elimina a supressão também borra os lugares por onde as pessoas de fato se deslocam.

### 3.3 Escolhendo a configuração de base

Ines escolhe como linha de base os blocos de quatro zonas com faixas de cinco anos, porque essa configuração suprime apenas 24 de 20.000 passageiros e mantém 1.400 classes. A configuração mais grosseira, de oito zonas, não suprime nada, mas funde bairros distintos que os planejadores precisam distinguir. Ela registra a escolha e o motivo no protocolo, porque uma linha de base fraca faria a privacidade diferencial parecer melhor do que é. Isso segue a recomendação da NIST SP 800-188 de que as escolhas de desidentificação sejam documentadas e justificadas para a publicação pretendida, de modo que os revisores possam verificar se a comparação foi justa.

### 3.4 Os planejadores como juízes da utilidade

A utilidade costuma ser medida apenas como erro numérico, mas a hipótese H2 de Ines consulta as pessoas que usam os dados. Três planejadores da Valemont receberão o mesmo conjunto de tabelas de viagens, produzidas pelos dois métodos, sem identificação, e avaliarão se poderiam usar cada uma em uma decisão de quadro de horários. Ines também informará o erro absoluto médio, para que os leitores possam comparar seu resultado com outros estudos. Ela explica no projeto que combinar um julgamento humano com uma métrica numérica torna o estudo mais relevante para a decisão real da autoridade sobre que tipo de dado publicar.

### Laboratório — Generalização e supressão para k = 5

```python
# Generalise synthetic rider records until every class has k >= 5; report suppression and information loss.
import random
from collections import Counter
r = random.Random(7)
riders = [(r.randrange(40), r.randrange(40), r.randrange(1940, 2008)) for _ in range(20000)]
def gen(x, zw, yw):
    return (x[0] // zw, x[1] // zw, x[2] // yw)
for zw, yw in [(1, 1), (2, 5), (4, 5), (8, 10)]:
    keys = [gen(x, zw, yw) for x in riders]; c = Counter(keys)
    small = sum(1 for k in keys if c[k] < 5)
    print(f"zones/{zw:<2d} years/{yw:<2d} classes {len(c):6d}  suppressed for k=5 {small:6d} ({small/len(keys):5.1%})")
```

Execute com `python3 lab_kanon.py`. Saída verificada:

```text
zones/1  years/1  classes  18228  suppressed for k=5  20000 (100.0%)
zones/2  years/5  classes   5430  suppressed for k=5  10282 (51.4%)
zones/4  years/5  classes   1400  suppressed for k=5     24 ( 0.1%)
zones/8  years/10 classes    175  suppressed for k=5      0 ( 0.0%)
```

### Exemplo resolvido

Ines enuncia H1 e H2 com limiares, generaliza registros sintéticos e escolhe blocos de quatro zonas com faixas de cinco anos como linha de base para k = 5: 1.400 classes e 24 passageiros suprimidos.

> **Caso sintético.** Todos os números vêm da população sintética; a NIST SP 800-188 e Sweeney (2002) são reais.

### Erros e limites

Três planejadores formam um painel pequeno; a aceitação é uma medida grosseira. A linha de base é uma escolha razoável entre várias.

### Exercícios

- **EX015 — Critérios da hipótese.** O que torna H2 testável? *Rubrica:* 3 = um painel definido, uma avaliação definida e um limiar de dois em três fixado de antemão;; 2 = menciona um limiar;; 1 = repete a hipótese;; 0 = nenhuma.
- **EX016 — Valores exatos.** Por que publicar zonas e anos de nascimento exatos falha totalmente para k = 5? *Rubrica:* 3 = quase toda combinação é única, então todo registro fica em um grupo menor que cinco;; 2 = diz que muitos são únicos;; 1 = diz que é detalhado demais;; 0 = nenhuma.
- **EX017 — Escolha da linha de base.** Por que Ines prefere blocos de quatro zonas com faixas de cinco anos a blocos de oito zonas? *Rubrica:* 3 = suprime apenas 24 passageiros e mantém a geografia mais fina de que os planejadores precisam;; 2 = menciona apenas a supressão;; 1 = escolhe oito zonas;; 0 = nenhuma.
- **EX018 — Perigo da linha de base fraca.** O que acontece se a linha de base de k-anonimato for mal escolhida? *Rubrica:* 3 = a comparação favorece a privacidade diferencial e o resultado engana;; 2 = diz que os resultados mudam;; 1 = ignora a justiça da comparação;; 0 = nenhuma.
- **EX019 — Avaliação às cegas.** Por que as tabelas dos planejadores não têm identificação? *Rubrica:* 3 = para impedir que expectativas sobre qualquer dos métodos influenciem as avaliações;; 2 = diz que é mais justo;; 1 = omite o motivo;; 0 = nenhuma.
- **EX020 — Duas medidas de utilidade.** Por que informar tanto a aceitação dos planejadores quanto o erro absoluto médio? *Rubrica:* 3 = a aceitação mostra a utilidade real; o erro permite comparar com outros estudos;; 2 = cita uma;; 1 = diz que mais dados é melhor;; 0 = nenhuma.

### Síntese

O capítulo 3 fixa hipóteses, uma linha de base justa de k-anonimato e um teste de utilidade em duas partes. O capítulo 4 pilota a publicação com privacidade diferencial.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 08)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Replicação da linha de base e piloto

### Objetivos de aprendizagem

Você vai (1) replicar um resultado conhecido antes de estendê-lo; (2) implementar o mecanismo de Laplace sobre contagens; (3) interpretar o custo de precisão do épsilon nas células pequenas.

### 4.1 Replicar primeiro

Antes de confiar no próprio código, Ines replica uma propriedade de manual descrita por Dwork e Roth (2014): para o ruído de Laplace com escala de um sobre épsilon, o erro absoluto esperado é igual a um sobre épsilon. Se sua implementação produzisse uma média diferente, todos os resultados posteriores ficariam sob suspeita. Ela sorteia muitas amostras de ruído para cada épsilon e compara o erro absoluto médio com a teoria. A replicação é um passo pequeno, mas o Prof. Aaltonen insiste que ela apareça na tese, porque os examinadores precisam de evidência de que o instrumento funciona antes de considerar o que ele mede no contexto do transporte.

### 4.2 A publicação piloto

O piloto usa 100 contagens sintéticas de origem e destino, entre zero e 400 viagens por dia. Para cada épsilon da grade 0,1, 0,5, 1,0 e 2,0, o laboratório acrescenta ruído de Laplace vinte vezes a cada contagem. O erro absoluto médio é 9,91 com épsilon 0,1, 1,98 com 0,5, 0,98 com 1,0 e 0,51 com 2,0, muito próximo de um sobre épsilon. A replicação é aprovada. Ines observa que esses erros absolutos parecem minúsculos ao lado de contagens de várias centenas de viagens, e é exatamente por isso que o passo seguinte examina as células pequenas em separado, em vez de confiar em uma média. As células pequenas recebem verificações próprias.

### 4.3 Células pequenas

Os planejadores se preocupam sobretudo com as linhas pouco movimentadas, em que poucas viagens decidem se um ônibus continua a circular. O piloto contém cinco células com menos de vinte viagens por dia. Nelas, o erro relativo médio é de 94,1% com épsilon 0,1, 22,0% com 0,5, 9,3% com 1,0 e 5,0% com 2,0. Com épsilon 0,1, o número publicado é quase só ruído. Ines espera, portanto, que os planejadores rejeitem valores baixos de épsilon para as linhas pequenas, e acrescenta uma análise secundária pré-registrada que informa os erros separadamente para células pequenas e grandes, para que uma média não possa esconder o problema.

### 4.4 Contabilidade do orçamento

Cada tabela publicada gasta parte de um orçamento de privacidade, porque responder a várias consultas sobre os mesmos passageiros tem efeito cumulativo. Dwork e Roth descrevem como os valores de épsilon se combinam pela composição. A Valemont quer tabelas diárias durante um ano, então Ines precisa decidir se o épsilon igual a um vale por tabela, por dia ou por ano. Ela registra essa decisão no protocolo como uma pergunta explícita ao encarregado de proteção de dados da autoridade, porque ela muda a força da garantia em ordens de grandeza, e adverte que um épsilon por tabela repetido diariamente não pode ser descrito honestamente como uma proteção anual forte.

### Laboratório — Ruído de Laplace em contagens de origem e destino

```python
# Laplace mechanism on 100 synthetic origin-destination counts (sensitivity 1); error by epsilon.
import random, math
r = random.Random(3)
true = [r.randint(0, 400) for _ in range(100)]
def lap(b):
    u = r.random() - 0.5
    return -b * math.copysign(1, u) * math.log(1 - 2 * abs(u))
for eps in [0.1, 0.5, 1.0, 2.0]:
    errs = [abs(lap(1 / eps)) for _ in true for _ in range(20)]
    small = [t for t in true if t < 20]
    rel = sum(abs(lap(1 / eps)) / max(t, 1) for t in small for _ in range(20)) / (20 * len(small))
    print(f"epsilon {eps:3.1f}  mean abs error {sum(errs)/len(errs):5.2f}  mean relative error on {len(small)} small cells {rel:6.1%}")
```

Execute com `python3 lab_laplace.py`. Saída verificada:

```text
epsilon 0.1  mean abs error  9.91  mean relative error on 5 small cells  94.1%
epsilon 0.5  mean abs error  1.98  mean relative error on 5 small cells  22.0%
epsilon 1.0  mean abs error  0.98  mean relative error on 5 small cells   9.3%
epsilon 2.0  mean abs error  0.51  mean relative error on 5 small cells   5.0%
```

### Exemplo resolvido

Ines replica o erro de um sobre épsilon do mecanismo de Laplace (0,98 com épsilon 1,0), depois encontra um erro relativo de 94,1% nas células pequenas com épsilon 0,1 e leva a contabilidade do orçamento ao protocolo como uma decisão a tomar.

> **Caso sintético.** As contagens são sintéticas e geradas com semente fixa; Dwork, McSherry, Nissim e Smith (2006) e Dwork e Roth (2014) são reais.

### Erros e limites

Cinco células pequenas são poucas para estimativas precisas. Publicações reais também exigem pós-processamento, como o arredondamento de contagens negativas, que o piloto omite.

### Exercícios

- **EX021 — Propósito da replicação.** Por que replicar o erro de um sobre épsilon antes de estudar os dados de transporte? *Rubrica:* 3 = confirma que o instrumento funciona, para que os resultados posteriores sejam confiáveis;; 2 = diz que é boa prática;; 1 = omite;; 0 = nenhuma.
- **EX022 — Erro com épsilon um.** Que erro absoluto médio o piloto encontrou com épsilon 1,0, e o que a teoria previa? *Rubrica:* 3 = 0,98 contra 1,0 previsto;; 2 = dá um número;; 1 = não dá nenhum;; 0 = nenhuma.
- **EX023 — A média esconde o dano.** Por que o erro absoluto médio pode esconder danos ao planejamento? *Rubrica:* 3 = ele faz a média sobre contagens grandes, enquanto as linhas pequenas sofrem grande erro relativo;; 2 = menciona as células pequenas;; 1 = confia na média;; 0 = nenhuma.
- **EX024 — Erro nas células pequenas.** Que erro relativo as células pequenas mostram com épsilon 0,5? *Rubrica:* 3 = 22,0%;; 2 = cerca de um quinto;; 1 = número errado;; 0 = nenhuma.
- **EX025 — Pergunta de composição.** Por que a Valemont precisa decidir se o épsilon vale por tabela, por dia ou por ano? *Rubrica:* 3 = publicações repetidas se compõem, então a garantia total depende da unidade de contabilização;; 2 = menciona tabelas repetidas;; 1 = ignora a composição;; 0 = nenhuma.
- **EX026 — Contagens negativas.** Que questão de pós-processamento o piloto omite? *Rubrica:* 3 = contagens com ruído podem ser negativas ou fracionárias e precisam ser tratadas sem quebrar a garantia;; 2 = menciona arredondamento;; 1 = diz que nenhuma;; 0 = nenhuma.

### Síntese

O capítulo 4 replica o mecanismo e expõe o erro em células pequenas e a contabilidade do orçamento. O capítulo 5 conduz o estudo principal com um ataque independente.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 08)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Estudo principal e validação independente

### Objetivos de aprendizagem

Você vai (1) executar um ataque de vinculação sobre publicações sintéticas; (2) comparar o risco entre métodos de publicação; (3) validar os resultados com uma equipe independente.

### 5.1 O modelo de ataque

Ines define um atacante que conhece a zona de residência, a zona de trabalho e o ano de nascimento de 500 passageiros-alvo, obtidos talvez de uma rede social ou de um diretório de funcionários de uma empresa. Contra os microdados pseudonimizados, em que os nomes são substituídos mas os valores exatos permanecem, o atacante procura uma linha que corresponda exatamente a cada alvo. Contra o arquivo k-anonimizado, o atacante encontra a classe correspondente e escolhe uma linha ao acaso. Contra as contagens diferencialmente privadas, não há linhas a vincular. Definir o atacante com precisão importa porque o NISTIR 8053 adverte que as estimativas de reidentificação dependem do conhecimento presumido, que deve ser declarado abertamente.

### 5.2 Resultados

O laboratório mostra que a pseudonimização, sozinha, permite ao atacante reidentificar com certeza 415 dos 500 alvos, 83,0%. O arquivo k-anonimizado impede qualquer correspondência certa; o palpite aleatório dentro das classes rende cerca de 4,4 acertos esperados, 0,9% dos alvos. As contagens diferencialmente privadas não dão ao atacante nenhum registro a vincular, e o risco passa a ser limitado pelo épsilon. H1 é sustentada quanto à direção, mas a comparação não é entre iguais: o arquivo k-anônimo vaza pouco sob este ataque, e seu risco restante vem de ataques que Ines ainda não testou, como a combinação de viagens.

### 5.3 Pseudonimização não é anonimização

O número de 83,0% torna concreto um ponto jurídico. O GDPR define a pseudonimização no artigo 4(5) como o tratamento que faz com que os dados não possam mais ser atribuídos a uma pessoa sem informações adicionais mantidas separadamente, e trata os dados pseudonimizados como dados pessoais. A LGPD usa uma definição muito próxima no art. 13, § 4º: o dado perde a possibilidade de associação a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro. O plano original da Valemont era trocar os números dos cartões por tokens aleatórios e chamar o arquivo de anônimo. O resultado de Ines mostra por que isso estaria errado: os tokens escondem os nomes, mas os atributos restantes identificam a maioria dos passageiros. Ela redige essa constatação como uma recomendação que a autoridade pode adotar de imediato, independentemente do restante da tese.

### 5.4 Validação independente

Ines pede a uma equipe de outra universidade que execute o ataque sobre os arquivos que ela publicou, sem ver o seu código. A equipe recebe a população sintética, as publicações e a descrição do ataque, e informa suas próprias taxas de reidentificação. Os resultados diferem dos dela em menos de um ponto percentual. Ela também pede que tentem um ataque que ela não desenhou, combinando dois dias de viagens; a equipe descobre que o arquivo k-anônimo vaza mais sob esse ataque. Ines informa os dois resultados, porque a validação independente só tem valor se puder encontrar problemas no estudo principal.

### Laboratório — Ataque de vinculação a três tipos de publicação

```python
# Linkage attack: an adversary knows home zone, work zone and birth year of 500 targets.
import random
from collections import Counter
r = random.Random(7)
riders = [(r.randrange(40), r.randrange(40), r.randrange(1940, 2008)) for _ in range(20000)]
targets = r.sample(range(20000), 500)
raw = Counter(riders)
hit_raw = sum(1 for t in targets if raw[riders[t]] == 1)
g = lambda x: (x[0] // 8, x[1] // 8, x[2] // 10)
gen = Counter(g(x) for x in riders)
kept = [t for t in targets if gen[g(riders[t])] >= 5]
exp = sum(1 / gen[g(riders[t])] for t in kept)
print(f"pseudonymised microdata: {hit_raw} of 500 targets re-identified with certainty ({hit_raw/5:.1f}%)")
print(f"k-anonymised (k>=5): 0 certain; expected correct guesses {exp:.1f} ({exp/5:.1f}%)")
print("differentially private counts: no record-level rows to link; risk bounded by epsilon instead")
```

Execute com `python3 lab_link.py`. Saída verificada:

```text
pseudonymised microdata: 415 of 500 targets re-identified with certainty (83.0%)
k-anonymised (k>=5): 0 certain; expected correct guesses 4.4 (0.9%)
differentially private counts: no record-level rows to link; risk bounded by epsilon instead
```

### Exemplo resolvido

Ines encontra 83,0% de reidentificação certa nos dados pseudonimizados, 0,9% de acertos esperados para k = 5 e nenhuma linha vinculável nas contagens diferencialmente privadas; uma equipe independente confirma os números e encontra uma fraqueza adicional com vários dias de viagens.

> **Caso sintético.** O atacante, os alvos e as publicações são sintéticos; o artigo 4(5) do GDPR, o art. 13, § 4º, da LGPD e o NISTIR 8053 são reais.

### Erros e limites

Um único modelo de atacante não representa todos os atacantes. A privacidade diferencial elimina a vinculação, mas sua proteção real depende da contabilidade de épsilon escolhida.

### Exercícios

- **EX027 — Conhecimento do atacante.** O que o atacante de Ines conhece, e por que declarar isso? *Rubrica:* 3 = zona de residência, zona de trabalho e ano de nascimento dos alvos; as estimativas de risco dependem do conhecimento presumido;; 2 = lista só o conhecimento;; 1 = omite;; 0 = nenhuma.
- **EX028 — Resultado pseudonimizado.** Quantos alvos foram reidentificados no arquivo pseudonimizado? *Rubrica:* 3 = 415 de 500, 83,0%;; 2 = cerca de quatro em cinco;; 1 = errado;; 0 = nenhuma.
- **EX029 — Artigo 4(5).** Por que dados pseudonimizados continuam sendo dados pessoais pelo GDPR? *Rubrica:* 3 = pelo artigo 4(5), os dados podem ser reatribuídos com informações adicionais, então continuam no escopo;; 2 = menciona a reatribuição;; 1 = diz que são anônimos;; 0 = nenhuma.
- **EX030 — Comparação entre iguais.** Por que a comparação de H1 "não é entre iguais"? *Rubrica:* 3 = tipos diferentes de publicação enfrentam ataques diferentes; o risco residual do k-anonimato está em ataques ainda não testados;; 2 = menciona saídas diferentes;; 1 = aceita H1 sem ressalvas;; 0 = nenhuma.
- **EX031 — Validação às cegas.** Por que a equipe de validação trabalha sem o código de Ines? *Rubrica:* 3 = para que erros do código dela não sejam copiados e a verificação seja independente;; 2 = menciona independência;; 1 = diz que é mais rápido;; 0 = nenhuma.
- **EX032 — Ataque não planejado.** Por que informar o ataque adicional de vários dias que enfraqueceu o k-anonimato? *Rubrica:* 3 = a validação precisa poder encontrar problemas; escondê-lo enviesaria a tese;; 2 = menciona honestidade;; 1 = omite;; 0 = nenhuma.

### Síntese

O capítulo 5 mede o risco sob um ataque declarado e o valida de forma independente. O capítulo 6 enfrenta a crítica dos pares e revisa as afirmações.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — aula 05 (capítulo 05 de 08)

[← Capítulo 04](#ch-04) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Crítica dos pares e revisão

### Objetivos de aprendizagem

Você vai (1) responder a críticas substantivas dos pares; (2) restringir as afirmações ao que a evidência sustenta; (3) distinguir objeções jurídicas, técnicas e éticas.

### 6.1 As críticas

Ines apresenta seu rascunho em um seminário de doutorado. Três críticas se destacam. Um estatístico argumenta que populações sintéticas podem ser menos diversas que as reais, de modo que a unicidade e a vinculação podem estar subestimadas. Uma advogada argumenta que a tese trata o épsilon como se ele resolvesse a questão jurídica do anonimato prevista no Considerando 26 do GDPR, o que ele não pode fazer sozinho. Uma planejadora argumenta que avaliar tabelas no papel não é o mesmo que usá-las em uma reunião real de quadro de horários. Ines anota cada crítica por inteiro antes de responder, para responder ao que foi de fato dito, e não a uma versão mais fraca.

### 6.2 Respondendo ao estatístico

Ines aceita o argumento e o testa. Ela gera de novo a população sintética com uma distribuição assimétrica, em que a maioria dos passageiros mora em poucas zonas densas, o que se aproxima mais das cidades reais. A unicidade cai um pouco nas zonas densas e sobe nas esparsas, mas as conclusões gerais não mudam. Ela acrescenta essa análise de sensibilidade à tese e restringe sua afirmação: os resultados valem para populações de estrutura semelhante, e uma replicação com dados reais dentro do ambiente seguro da autoridade, sob a base legal da própria autoridade e com uma avaliação de impacto sobre a proteção de dados, fica recomendada como trabalho futuro, em vez de presumida.

### 6.3 Respondendo à advogada

Ines concorda que o status jurídico de uma publicação depende de todos os meios razoavelmente suscetíveis de serem usados para identificar pessoas, como diz o Considerando 26, incluindo custo, tempo e tecnologia disponível. A LGPD adota um critério parecido: o que é razoável deve considerar fatores objetivos, como o custo e o tempo necessários para reverter a anonimização, de acordo com as tecnologias disponíveis (art. 12, § 1º). O épsilon é evidência para essa avaliação, não um substituto dela. Ela reescreve a conclusão para dizer que contagens diferencialmente privadas com orçamento documentado oferecem forte evidência técnica que a autoridade pode usar em sua avaliação de anonimização, a qual o encarregado e, quando necessário, a autoridade de controle ainda precisam julgar. Ela também cita as diretrizes do EDPB sobre proteção de dados desde a concepção como contexto para documentar essas escolhas.

### 6.4 Respondendo à planejadora

Ines não pode conduzir reuniões reais de quadro de horários durante a tese, então restringe H2 a "os planejadores julgam as tabelas utilizáveis em uma revisão estruturada" e acrescenta uma limitação. Ela também propõe um estudo complementar em que a revisão de uma linha use as contagens publicadas e os planejadores registrem qualquer decisão que difira da que tomariam com os dados exatos. A planejadora concorda que esse é um teste mais justo. Ines anota em seu registro de revisões que duas das três críticas mudaram suas afirmações, e que esse é um resultado normal e saudável da revisão por pares, e não um sinal de que a tese era fraca.

### Exemplo resolvido

Ines transforma três críticas em uma análise de sensibilidade, uma conclusão jurídica mais estreita e uma afirmação de utilidade mais estreita, registrando cada mudança em um registro de revisões.

> **Caso sintético.** Os participantes do seminário são sintéticos; o Considerando 26 do GDPR, o art. 12 da LGPD e as Diretrizes 4/2019 do EDPB são reais.

### Erros e limites

Restringir as afirmações pode ir longe demais e não deixar nada útil; Ines mantém o resultado central e limita apenas o seu alcance.

### Exercícios

- **EX033 — Crítica da diversidade.** Como Ines testa a crítica do estatístico? *Rubrica:* 3 = gera uma população assimétrica e repete as análises como verificação de sensibilidade;; 2 = menciona repetir;; 1 = descarta a crítica;; 0 = nenhuma.
- **EX034 — Meios razoavelmente suscetíveis.** Por que o épsilon não pode, sozinho, resolver o anonimato segundo o Considerando 26? *Rubrica:* 3 = o Considerando 26 pergunta por todos os meios razoavelmente suscetíveis de identificar, um julgamento jurídico que usa evidência técnica;; 2 = menciona a lei;; 1 = diz que o épsilon basta;; 0 = nenhuma.
- **EX035 — H2 restringida.** Como Ines restringe H2 depois da crítica da planejadora? *Rubrica:* 3 = à utilidade julgada em uma revisão estruturada, com uma limitação e um teste complementar em uma linha;; 2 = menciona a restrição;; 1 = mantém H2 igual;; 0 = nenhuma.
- **EX036 — Registrar as críticas.** Por que anotar as críticas por inteiro antes de responder? *Rubrica:* 3 = para responder ao argumento real, não a uma versão mais fraca;; 2 = menciona precisão;; 1 = omite;; 0 = nenhuma.
- **EX037 — Revisão saudável.** É uma fraqueza que duas críticas tenham mudado as afirmações dela? *Rubrica:* 3 = não; ajustar as afirmações à evidência é o propósito da revisão;; 2 = diz que está tudo bem;; 1 = diz que é um fracasso;; 0 = nenhuma.
- **EX038 — Replicação com dados reais.** Que condições Ines impõe a uma futura replicação com dados reais? *Rubrica:* 3 = dentro do ambiente seguro, com base legal e uma avaliação de impacto (DPIA);; 2 = cita uma;; 1 = omite;; 0 = nenhuma.

### Síntese

O capítulo 6 mostra a crítica aprimorando as afirmações. O capítulo 7 monta a tese e um arquivo de reprodutibilidade sem vazar dados pessoais.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — aula 06 (capítulo 06 de 08)

[← Capítulo 05](#ch-05) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Síntese da tese e arquivo de reprodutibilidade

### Objetivos de aprendizagem

Você vai (1) sintetizar os achados em afirmações defensáveis; (2) montar um arquivo de reprodutibilidade; (3) conferir que nenhum identificador sai nos arquivos suplementares.

### 7.1 A síntese

Ines redige sua afirmação central com cuidado. A pseudonimização sozinha deixa a maioria dos passageiros sintéticos reidentificável. Um arquivo k-anonimizado bem escolhido resiste à vinculação simples, mas vaza sob ataques com vários dias de viagens. As contagens diferencialmente privadas eliminam a vinculação de registros, com um erro desprezível nas linhas movimentadas e grave nas linhas pouco movimentadas quando o épsilon é baixo. Os planejadores, em uma revisão estruturada, aceitaram as contagens com épsilon igual a um. A afirmação é limitada pela população sintética, pelos três planejadores e pelos ataques testados. Ela confere cada frase da afirmação com uma tabela, uma figura ou uma saída de laboratório, para que nada na conclusão fique solto da evidência.

### 7.2 O que entra no arquivo

A Thornbury exige um arquivo de reprodutibilidade. Ines inclui o protocolo pré-registrado, o código de análise com suas sementes aleatórias, as tabelas de resultados e um breve arquivo de instruções que explica como executar tudo de novo. Cada arquivo é listado em um manifesto com seu resumo SHA-256, para que qualquer alteração posterior possa ser detectada. Ela não inclui a população sintética em si, apenas o gerador e sua semente, porque a população pode ser reconstruída exatamente. Isso deixa o arquivo pequeno o bastante para ser depositado no repositório da universidade, mantendo cada número da tese reproduzível por um examinador com ferramentas comuns.

### 7.3 Um vazamento detectado

Quando Ines executa a verificação do arquivo, ela bloqueia um item. Um arquivo de linhas de exemplo, que ela acrescentara para ilustrar o formato dos dados, contém uma coluna chamada identificador do passageiro, com um token copiado de um teste inicial que usava formatos reais de cartão. Embora o token seja fictício, a verificação foi desenhada justamente para barrar esse tipo de deslize. Ela retira o arquivo e o substitui por uma descrição do formato. O episódio mostra por que a proteção de dados desde a concepção, descrita no artigo 25 do GDPR e nas diretrizes do EDPB, e refletida na LGPD na exigência de que as medidas de segurança sejam observadas desde a fase de concepção (art. 46, § 2º), alcança também os produtos da pesquisa, e não só o sistema principal estudado.

### 7.4 Licenciamento e acesso

Ines publica o código sob uma licença aberta e declara que o gerador é sintético e não contém dados pessoais. Ela acrescenta uma declaração de dados que explica o que o arquivo contém, o que não contém e com quem falar na autoridade sobre o acesso a dados reais pelos procedimentos próprios dela. O Prof. Aaltonen lembra que ciência aberta e proteção de dados são compatíveis quando o arquivo é desenhado para as duas desde o início. Ela registra a declaração tanto nas páginas iniciais da tese quanto no arquivo, para que leitores que nunca abram o repositório também entendam os seus limites.

### Laboratório — Manifesto e verificação de identificadores do arquivo da tese

```python
# SHA-256 manifest for a synthetic thesis archive; the release check flags any file containing a raw rider id.
import hashlib
files = {"protocol.md": b"pre-registered protocol v3", "analysis.py": b"seed=7; epsilon grid", "results.csv": b"eps,mae\n0.1,10.1\n", "README.md": b"rerun: python3 analysis.py", "sample_rows.csv": b"rider_id,zone\nR-104233,12\n"}
for n, b in files.items():
    flag = "BLOCK (contains rider_id)" if b"rider_id" in b else "ok"
    print(f"{hashlib.sha256(b).hexdigest()[:16]}  {n:16s} {flag}")
```

Execute com `python3 lab_archive.py`. Saída verificada:

```text
a52eebd60ecdcdf6  protocol.md      ok
fec505cc4b189e5f  analysis.py      ok
56ae8db2fd66c425  results.csv      ok
0859d3705f295926  README.md        ok
59ddbf48bee52954  sample_rows.csv  BLOCK (contains rider_id)
```

### Exemplo resolvido

Ines redige uma afirmação central delimitada, monta um manifesto de cinco arquivos com resumos SHA-256 e detecta um arquivo de exemplo com uma coluna de identificador de passageiro, que ela substitui antes do depósito.

> **Caso sintético.** Os arquivos e o token são sintéticos; o artigo 25 do GDPR, o art. 46, § 2º, da LGPD e as Diretrizes 4/2019 do EDPB são reais.

### Erros e limites

Uma verificação por palavra-chave só encontra os identificadores que foi instruída a procurar; textos livres ainda podem vazar. Resumos criptográficos provam integridade, não correção.

### Exercícios

- **EX039 — Afirmação delimitada.** Liste os três limites da afirmação central de Ines. *Rubrica:* 3 = população sintética, três planejadores, ataques testados;; 2 = lista dois;; 1 = não lista nenhum;; 0 = nenhuma.
- **EX040 — Gerador, não dados.** Por que arquivar o gerador e a semente em vez da população? *Rubrica:* 3 = reconstrói exatamente a mesma população e mantém o arquivo pequeno;; 2 = menciona o tamanho;; 1 = arquiva tudo;; 0 = nenhuma.
- **EX041 — Arquivo bloqueado.** Que arquivo a verificação bloqueou, e por quê? *Rubrica:* 3 = sample_rows.csv, porque contém uma coluna rider_id;; 2 = cita o arquivo;; 1 = diz que nenhum;; 0 = nenhuma.
- **EX042 — Papel dos resumos.** O que um manifesto SHA-256 prova, e o que não prova? *Rubrica:* 3 = que os arquivos não mudaram desde a listagem; não que as análises estejam corretas;; 2 = cita um;; 1 = confunde os dois;; 0 = nenhuma.
- **EX043 — Alcance da concepção.** Por que a proteção de dados desde a concepção alcança o arquivo da pesquisa? *Rubrica:* 3 = os produtos podem vazar dados pessoais tanto quanto os sistemas;; 2 = menciona os produtos;; 1 = limita-a aos sistemas;; 0 = nenhuma.
- **EX044 — Declaração de dados.** O que a declaração de dados de Ines deve explicar? *Rubrica:* 3 = conteúdo, exclusões e como pedir acesso a dados reais;; 2 = cita um;; 1 = omite;; 0 = nenhuma.

### Síntese

O capítulo 7 produz uma afirmação delimitada e um arquivo limpo. O capítulo 8 prepara a defesa e a publicação.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — aula 07 (capítulo 07 de 08)

[← Capítulo 06](#ch-06) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Defesa e plano de publicação

### Objetivos de aprendizagem

Você vai (1) preparar uma defesa de doutorado em torno da evidência e dos limites; (2) planejar publicações para públicos distintos; (3) traduzir os achados em uma decisão da organização.

### 8.1 Preparando a defesa

Ines se prepara listando as perguntas mais difíceis que espera. Por que confiar em uma população sintética? Um épsilon igual a um por ano é realista para publicações diárias? Um atacante mais forte quebraria ainda mais o arquivo k-anônimo? Para cada uma, ela prepara uma resposta curta que aponta para a evidência e para um limite. O Prof. Aaltonen conduz uma defesa simulada em que faz o papel de um examinador hostil, e ela aprende a responder "não sei, mas é assim que eu descobriria" quando a evidência acaba, em vez de defender diante da banca afirmações que seus dados não sustentam.

### 8.2 A defesa

Na defesa, o examinador externo, um engenheiro de privacidade, insiste na contabilidade do orçamento. Ines explica que seu estudo usou épsilon igual a um por tabela, e que um ano de tabelas diárias, pela composição simples, resultaria em um total muito maior; assim, a autoridade precisa escolher um orçamento anual e aceitar um erro diário maior, ou publicar com menos frequência. O examinador aceita a resposta e pede que a tese declare esse compromisso no resumo. A banca aprova a tese com correções menores, uma das quais acrescenta ao resumo uma frase sobre composição e outra esclarece o ataque com vários dias de viagens.

### 8.3 Plano de publicação

Ines planeja três produtos para três públicos. Um artigo em periódico apresenta aos pesquisadores a comparação controlada e a validação independente. Um guia prático curto explica, sem equações, por que pseudonimização não é anonimização e como escolher entre métodos de publicação. Um informe para o conselho da Valemont recomenda interromper a publicação apenas com tokens e testar em piloto as contagens diferencialmente privadas nas linhas movimentadas, mantendo acesso restrito para as linhas pouco movimentadas. Cada produto cita o mesmo arquivo, para que leitores de todos os públicos possam rastrear as afirmações até a mesma evidência e examinar o código que produziu cada número.

### 8.4 A decisão da organização

O conselho da Valemont adota a recomendação. Seu encarregado de proteção de dados registra o raciocínio nos registros da autoridade, com uma avaliação de impacto sobre a proteção de dados para o novo processo de publicação, como exige o artigo 35 do GDPR quando o tratamento é suscetível de resultar em alto risco. No Brasil, o documento equivalente é o relatório de impacto à proteção de dados pessoais (LGPD, art. 5º, XVII), que a ANPD pode exigir do controlador (art. 38), e as atribuições do encarregado estão regulamentadas pela Resolução CD/ANPD nº 18/2024. O conselho também pede a Ines que apresente o resultado a outras autoridades de transporte. Ela concorda, mas apenas com a afirmação delimitada e seus limites, e lembra que as populações e os atacantes delas podem ser diferentes. Sua reflexão final é que a tese mudou uma decisão real porque cada afirmação era falseável e documentada.

### Exemplo resolvido

Ines prepara as perguntas difíceis, defende um compromisso de contabilidade do orçamento, planeja um artigo em periódico, um guia prático e um informe ao conselho, e vê a Valemont substituir as publicações só com tokens por um piloto documentado com privacidade diferencial.

> **Caso sintético.** A defesa, o conselho e o examinador são sintéticos; os artigos 25 e 35 do GDPR, os arts. 5º e 38 da LGPD e a Resolução CD/ANPD nº 18/2024 são reais.

### Erros e limites

Uma defesa bem-sucedida não prova uma verdade universal; outras autoridades precisam validar o resultado em seu próprio contexto.

### Exercícios

- **EX045 — Respostas desconhecidas.** Como Ines deve responder quando a evidência acaba durante a defesa? *Rubrica:* 3 = admitir o limite e explicar como descobriria;; 2 = admite a incerteza;; 1 = defende mesmo assim;; 0 = nenhuma.
- **EX046 — Orçamento anual.** Que compromisso o examinador quis ver declarado no resumo? *Rubrica:* 3 = um orçamento anual obriga a um erro diário maior ou a publicações menos frequentes;; 2 = menciona a composição;; 1 = omite;; 0 = nenhuma.
- **EX047 — Três públicos.** Cite os três produtos de Ines e seus públicos. *Rubrica:* 3 = artigo em periódico para pesquisadores, guia para profissionais, informe para o conselho;; 2 = cita dois;; 1 = cita um;; 0 = nenhuma.
- **EX048 — Recomendação ao conselho.** O que o informe ao conselho recomendou? *Rubrica:* 3 = interromper a publicação só com tokens, piloto de contagens com DP nas linhas movimentadas, acesso restrito nas pouco movimentadas;; 2 = duas partes;; 1 = uma parte;; 0 = nenhuma.
- **EX049 — Papel do artigo 35.** Por que o novo processo de publicação precisa de uma DPIA? *Rubrica:* 3 = o artigo 35 a exige quando o tratamento é suscetível de resultar em alto risco;; 2 = menciona risco;; 1 = diz que é opcional;; 0 = nenhuma.
- **EX050 — Cautela na transferência.** Que cautela Ines transmite a outras autoridades? *Rubrica:* 3 = suas populações e atacantes podem ser diferentes, então precisam validar localmente;; 2 = menciona a diferença;; 1 = diz que os resultados se transferem;; 0 = nenhuma.

### Síntese

O capítulo 8 encerra o percurso de doutorado com um resultado defendido e delimitado e uma decisão alterada. Seguem-se as resoluções e, depois, as referências.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — aula 08 (capítulo 08 de 08)

[← Capítulo 07](#ch-07) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX050. Ines Carvalho, o Prof. Henrik Aaltonen, a Thornbury University, a Valemont Regional Transit Authority e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Ines declara de antemão que nenhuma redução do risco de vinculação, ou um erro que os planejadores rejeitem, refutaria sua afirmação, de modo que os dados podem provar que ela está errada.

**EX002.** Como o GDPR e a LGPD (arts. 5º, III, e 12) excluem de seu escopo os dados verdadeiramente anônimos, chamar uma publicação de anônima elimina deveres legais; a afirmação precisa, portanto, ser justificada tecnicamente.

**EX003.** Uma população sintética permite testar ataques e publicar sem expor passageiros reais, evitando que a pesquisa cause o dano que mede.

**EX004.** Acrescentar o ano de nascimento leva a unicidade de 0,0% para 83,4%; ele divide cada par residência-trabalho em dezenas de grupos minúsculos.

**EX005.** Uma linha única só se torna uma pessoa nomeada quando o atacante tem dados externos que correspondem àquela combinação; a unicidade é uma precondição, não uma prova.

**EX006.** Declarar que não tem interesse em produtos de anonimização permite aos examinadores e à autoridade confiar que a comparação não pende para um produto que ela vende.

**EX007.** Impede que ela escolha a métrica de erro ou a grade de épsilon depois de ver qual escolha favorece o método preferido.

**EX008.** Pergunta se esse fluxo corresponde às normas do contexto em que os passageiros compartilharam as viagens; se o uso pelos planejadores romper essas normas, o fluxo é inadequado.

**EX009.** Coleta de informações, processamento de informações, disseminação de informações e invasão.

**EX010.** Se todos os membros de um grupo k-anônimo têm o mesmo valor sensível, o atacante o descobre sem singularizar ninguém; a l-diversidade exige variedade.

**EX011.** Históricos de transporte, como avaliações de filmes, são esparsos e distintivos; conhecer algumas viagens pode vincular um histórico pseudônimo a uma pessoa.

**EX012.** Em uma contagem, uma pessoa muda a resposta em no máximo um; o ruído de Laplace com escala 1/épsilon é calibrado para esse limite.

**EX013.** Sua garantia não depende do que o atacante já sabe, enquanto o k-anonimato presume um conjunto específico de quase-identificadores.

**EX014.** Poucos estudos comparam registros k-anonimizados e contagens diferencialmente privadas na mesma publicação, sob o mesmo ataque, com a aceitação dos usuários como teste de utilidade.

**EX015.** H2 define quem julga, como avalia e o limiar de aprovação de dois em três, tudo fixado antes que os dados existam.

**EX016.** Com valores exatos quase todo passageiro é único, então todo registro cai em uma classe menor que cinco e todos os 20.000 seriam suprimidos.

**EX017.** Suprime apenas 24 de 20.000 e mantém 1.400 classes; os blocos de oito zonas fundem bairros que os planejadores precisam distinguir.

**EX018.** Uma linha de base fraca exagera a vantagem da privacidade diferencial, e o estudo enganaria a autoridade.

**EX019.** Tabelas sem identificação impedem que os planejadores favoreçam o método que esperam ser melhor.

**EX020.** A aceitação mostra se os dados servem a decisões reais, enquanto o erro absoluto médio torna o resultado comparável com a literatura.

**EX021.** Reproduzir o erro teórico mostra que a implementação está correta, de modo que diferenças posteriores refletem o método, e não um defeito.

**EX022.** O laboratório informa 0,98, próximo do 1/épsilon = 1,0 previsto.

**EX023.** As contagens grandes dominam a média, enquanto as linhas pouco movimentadas, que orientam as decisões de serviço, têm erros relativos de 22% a 94% com épsilon baixo.

**EX024.** 22,0% de erro relativo médio nas cinco células pequenas.

**EX025.** A perda de privacidade se acumula entre publicações; épsilon igual a um por tabela diária significa uma garantia anual muito mais fraca do que épsilon igual a um por ano.

**EX026.** Contagens com ruído podem ser negativas; um pós-processamento como o arredondamento é seguro para a privacidade, mas altera o erro, e o piloto o ignora.

**EX027.** O atacante conhece três quase-identificadores de 500 alvos; declarar isso importa porque o risco depende do que o atacante sabe.

**EX028.** 415 de 500 alvos (83,0%) foram reidentificados com certeza.

**EX029.** O artigo 4(5) define dados pseudonimizados como reatribuíveis com informações mantidas separadamente; por isso continuam sendo dados pessoais. A LGPD adota definição equivalente no art. 13, § 4º.

**EX030.** Registros e contagens são atacados de formas diferentes; o risco restante do arquivo k-anônimo aparece em outros ataques, como a vinculação de vários dias.

**EX031.** Sem o código dela, a equipe não pode repetir seus erros, e a concordância é evidência real.

**EX032.** Informar a fraqueza de vários dias mostra que a validação foi genuína e dá à autoridade um quadro completo do risco.

**EX033.** Ela constrói uma população assimétrica, mais próxima das cidades reais, e repete a unicidade e a vinculação; as conclusões se mantêm e ela restringe a afirmação.

**EX034.** O Considerando 26 considera todos os meios razoavelmente suscetíveis de serem usados, incluindo custo e tecnologia; o épsilon informa, mas não substitui esse julgamento. A LGPD exige a mesma ponderação no art. 12, § 1º.

**EX035.** H2 agora afirma apenas a utilidade em uma revisão estruturada, com uma limitação declarada e a proposta de uma revisão real em uma linha.

**EX036.** Registrar cada crítica exatamente evita responder a um espantalho.

**EX037.** Não; restringir as afirmações em resposta a críticas válidas é para isso que serve a revisão por pares.

**EX038.** Deve ocorrer dentro do ambiente seguro da autoridade, sob a base legal dela e depois de uma avaliação de impacto sobre a proteção de dados.

**EX039.** A afirmação é limitada pela população sintética, pelo painel de três planejadores e pelos ataques específicos testados.

**EX040.** O gerador com semente recria exatamente a população, então o arquivo fica pequeno e reproduzível.

**EX041.** sample_rows.csv foi bloqueado porque continha uma coluna rider_id com um token em formato de cartão.

**EX042.** Prova a integridade desde que o manifesto foi feito, não que o código ou as conclusões estejam corretos.

**EX043.** Arquivos suplementares também são produtos do tratamento; desenhá-los para excluir identificadores aplica à pesquisa o raciocínio do artigo 25.

**EX044.** Explica o que o arquivo contém, o que ele exclui e com quem falar sobre o acesso a dados reais.

**EX045.** Ela diz que não sabe e explica o estudo que responderia à pergunta.

**EX046.** Publicações diárias gastam orçamento; um épsilon anual fixo significa erro diário maior ou menos publicações.

**EX047.** Um artigo em periódico para pesquisadores, um guia prático para profissionais e um informe ao conselho da Valemont.

**EX048.** Interromper as publicações com tokens pseudonimizados, testar em piloto as contagens diferencialmente privadas nas linhas movimentadas e manter acesso restrito para as pouco movimentadas.

**EX049.** Publicar dados de viagem derivados é provavelmente de alto risco, então o artigo 35 exige uma avaliação de impacto sobre a proteção de dados; no Brasil, o instrumento correspondente é o relatório de impacto da LGPD (art. 5º, XVII; art. 38).

**EX050.** Os resultados são delimitados; outras autoridades precisam testar suas próprias populações e atacantes.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da Resolução CD/ANPD nº 18, de 16 de julho de 2024, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Brasil. Agência Nacional de Proteção de Dados. (2024). *Resolução CD/ANPD nº 18, de 16 de julho de 2024 — Aprova o Regulamento sobre a atuação do encarregado pelo tratamento de dados pessoais*. Diário Oficial da União. <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd>
- Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in Theoretical Computer Science, 9*(3–4), 211–407. <https://doi.org/10.1561/0400000042>
- Dwork, C., McSherry, F., Nissim, K., & Smith, A. (2006). Calibrating noise to sensitivity in private data analysis. *Theory of Cryptography (TCC 2006)*, 265–284. <https://doi.org/10.1007/11681878_14>
- European Data Protection Board. (2020). *Guidelines 4/2019 on Article 25 Data Protection by Design and by Default* (Version 2.0, adopted 20 October 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-42019-on-article-25-data-protection-by-design-and-by-default_en>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Garfinkel, S. L. (2015). *De-identification of personal information* (NISTIR 8053). NIST. <https://doi.org/10.6028/NIST.IR.8053>
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). NIST. <https://doi.org/10.6028/NIST.SP.800-188>
- Li, N., Li, T., & Venkatasubramanian, S. (2007). t-Closeness: Privacy beyond k-anonymity and l-diversity. *IEEE 23rd ICDE*, 106–115. <https://doi.org/10.1109/ICDE.2007.367856>
- Machanavajjhala, A., Kifer, D., Gehrke, J., & Venkitasubramaniam, M. (2007). l-Diversity: Privacy beyond k-anonymity. *ACM TKDD, 1*(1), 3. <https://doi.org/10.1145/1217299.1217302>
- Narayanan, A., & Shmatikov, V. (2008). Robust de-anonymization of large sparse datasets. *IEEE Symposium on Security and Privacy*, 111–125. <https://doi.org/10.1109/SP.2008.33>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
- Nissenbaum, H. (2009). *Privacy in context: Technology, policy, and the integrity of social life*. Stanford University Press. <https://doi.org/10.1515/9780804772891>
- Solove, D. J. (2006). A taxonomy of privacy. *University of Pennsylvania Law Review, 154*(3), 477–564. <https://doi.org/10.2307/40041279>
- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570. <https://doi.org/10.1142/S0218488502001648>
- Warren, S. D., & Brandeis, L. D. (1890). The right to privacy. *Harvard Law Review, 4*(5), 193–220. <https://doi.org/10.2307/1321160>
