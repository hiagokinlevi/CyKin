# Arquitetura e Engenharia de Segurança: Curso de Mestrado

- Idioma: português do Brasil (`pt`); curso 168, curso de mestrado (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 8 já estão escritos em português, com os exercícios EX001–EX026 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 5–8 (EX027–EX050) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: pesquisadores iniciantes em arquitetura e engenharia de segurança.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios contam registros de triagem, calculam a alcançabilidade em grafos sob três políticas sintéticas de segmentação e fazem bootstrap de resultados pareados; nunca varrem nem tocam uma rede real. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um mestrando que compara a microssegmentação baseada em identidade com a segmentação por zonas em redes corporativas simuladas: pergunta e método de revisão da literatura, um seminário avançado, desenho do estudo e ética, explicações concorrentes, proposta e piloto, análise, redação e limitações, e revisão independente e defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Kenji Albrecht** | Mestrando, em meio período na Vantor | Inventado |
| **Dra. Selin Aydın** | Orientadora | Inventada |
| **Northmoor University** | Universidade fictícia | Inventada |
| **Vantor Logistics** | Empregadora fictícia cuja estrutura molda o modelo | Inventada |

### Fontes principais

NIST [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-160 Vol. 1 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v1r1) e [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5); Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Shostack (2014); Anderson (2020); Wohlin et al. (2012). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

Capítulos 5–8: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Pergunta de pesquisa e método de revisão da literatura

### Objetivos de aprendizagem

Você vai (1) transformar um interesse em arquitetura numa pergunta focada e respondível; (2) desenhar uma busca documentada na literatura; (3) fazer a triagem das fontes com critérios explícitos; (4) registrar a busca para que outros possam repeti-la.

### 1.1 Do interesse à pergunta

Kenji Albrecht é mestrando na fictícia Northmoor University, sob orientação da Dra. Selin Aydın. Ele trabalha em meio período na fictícia Vantor Logistics, cuja rede interna plana permite que quase qualquer estação de trabalho alcance quase qualquer servidor. Seu interesse é a arquitetura zero trust, descrita no NIST SP 800-207, mas um interesse não é uma pergunta. A Dra. Aydın o pressiona a estreitá-lo. Depois de vários rascunhos, ele chega a esta: em redes corporativas simuladas com a forma da Vantor, quanto a microssegmentação baseada em identidade reduz o número de servidores que um atacante consegue alcançar a partir de uma estação comprometida, em comparação com a segmentação por zonas? Todas as pessoas, organizações e redes aqui são sintéticas.

### 1.2 Por que esta pergunta funciona

A pergunta nomeia uma população, redes simuladas com a forma de um tipo real de empresa; uma intervenção, a microssegmentação baseada em identidade; uma comparação, a segmentação por zonas; e um desfecho, os servidores alcançáveis a partir de um ponto de apoio. Ela pode ser respondida dentro do prazo de um mestrado porque usa simulação em vez de alterar uma rede de produção, e evita os riscos éticos e operacionais de testar em sistemas reais. Ela também é limitada: a alcançabilidade é uma aproximação do avanço do atacante, não uma medida de incidentes reais. Kenji escreve essa limitação no documento da pergunta desde já, para que ela molde todos os capítulos seguintes, em vez de aparecer só no fim.

### 1.3 Desenho da busca

Kenji desenha a busca antes de executá-la. Escolhe as bases, as bibliotecas digitais do IEEE e da ACM mais as publicações do NIST, e escreve strings de busca que combinam termos de segmentação, zero trust e movimento lateral. Define os critérios de inclusão: estudos revisados por pares ou padrões oficiais de 2010 em diante que discutam os efeitos da segmentação de rede sobre o movimento do atacante. Exclui material de marketing de fornecedores e textos de opinião, mas mantém uma lista separada de literatura cinzenta para contexto. Escrever os critérios primeiro o impede de incluir, sem perceber, só os estudos que concordam com o que ele espera encontrar, um viés bem conhecido nas revisões de literatura.

### 1.4 Triagem e registro

A busca retorna 312 registros. A triagem por título e resumo remove os que estão fora do escopo, e a leitura do texto completo remove mais. Ele registra o número em cada etapa, os motivos de exclusão e a data de cada busca, numa tabela de fluxo semelhante às usadas em revisões sistemáticas. O laboratório abaixo reproduz as contagens do seu log de triagem. O conjunto final de 27 estudos é pequeno, e ele observa que a maioria relata designs ou simulações, e não medições de campo. Registrar a busca a torna repetível e permite aos examinadores julgar se algum trabalho importante pode ter ficado de fora.

### Laboratório — Contagens do fluxo de triagem

```python
# Screening flow from a synthetic search log.
log = {"ieee": 141, "acm": 118, "nist": 53}
dupes = 46; title_abstract_out = 197; fulltext_out = 42
total = sum(log.values()); after_d = total - dupes
after_ta = after_d - title_abstract_out; included = after_ta - fulltext_out
for k, v in log.items(): print(f"source {k:5} {v}")
print(f"records {total} -> after duplicates {after_d} -> after title/abstract {after_ta} -> included {included}")
```

Execute com `python3 lab_screen.py`. Saída verificada:

```text
source ieee  141
source acm   118
source nist  53
records 312 -> after duplicates 266 -> after title/abstract 69 -> included 27
```

### 1.5 O que diz a literatura

Kenji resume os temas. Os princípios fundamentais, incluindo o menor privilégio e a mediação completa de Saltzer e Schroeder (1975), sustentam a segmentação. O NIST SP 800-207 descreve pontos de aplicação de política que tomam decisões de acesso a cada requisição. Anderson (2020) traz estudos de caso em que redes planas permitiram aos atacantes se mover amplamente depois de um único comprometimento. Existem estudos de simulação com grafos de ataque, mas poucos comparam estratégias de segmentação nas mesmas redes e com as mesmas premissas. Essa lacuna molda sua contribuição: uma comparação controlada sob premissas declaradas, e não uma afirmação sobre como atacantes reais vão se comportar em qualquer empresa.

### Exemplo resolvido

Kenji estreita seu interesse numa pergunta sobre alcançabilidade, escreve de antemão as strings e os critérios de busca, faz a triagem de 312 registros até chegar a 27 estudos com uma tabela de fluxo e identifica a lacuna de comparação.

> **Caso sintético.** A Northmoor University, a Vantor Logistics, Kenji, a Dra. Aydın e os números da triagem são inventados; o SP 800-207, Saltzer e Schroeder (1975) e Anderson (2020) são reais.

### Erros e limites

A escolha das bases limita a cobertura; o conhecimento dos praticantes pode estar fora da literatura indexada. A alcançabilidade ignora a detecção e a resposta.

### Exercícios

- **EX001 — Partes da pergunta.** Nomeie a população, a intervenção, a comparação e o desfecho da pergunta de Kenji. *Rubrica:* 3 = redes simuladas como a da Vantor; microssegmentação por identidade; segmentação por zonas; servidores alcançáveis a partir de um ponto de apoio;; 2 = três;; 1 = nada;; 0 = nenhuma.

- **EX002 — Escolha da simulação.** Por que usar simulação em vez de alterar a rede da Vantor? *Rubrica:* 3 = cabe no prazo e evita riscos éticos e operacionais aos sistemas reais;; 2 = um motivo;; 1 = sem motivo;; 0 = nenhuma.

- **EX003 — Limite da aproximação.** Que limitação Kenji escreve no documento da pergunta? *Rubrica:* 3 = a alcançabilidade é uma aproximação do avanço do atacante, não de incidentes reais;; 2 = aproximação;; 1 = nada;; 0 = nenhuma.

- **EX004 — Critérios primeiro.** Por que escrever os critérios de inclusão antes de buscar? *Rubrica:* 3 = para evitar incluir seletivamente os estudos que concordam;; 2 = viés;; 1 = sem motivo;; 0 = nenhuma.

- **EX005 — Laboratório da triagem.** Quantos registros entraram na triagem e quantos estudos foram incluídos? *Rubrica:* 3 = 312 registros, 27 incluídos;; 2 = um número;; 1 = errado;; 0 = nenhuma.

- **EX006 — Evidência das redes planas.** O que Anderson (2020) contribui para a revisão de Kenji? *Rubrica:* 3 = estudos de caso em que redes planas permitiram movimento amplo depois de um comprometimento;; 2 = casos;; 1 = nada;; 0 = nenhuma.

- **EX007 — Lacuna de comparação.** Que lacuna Kenji identificou? *Rubrica:* 3 = poucos estudos comparam estratégias de segmentação nas mesmas redes sob as mesmas premissas;; 2 = lacuna;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Arquitetura e engenharia de segurança: seminário avançado

### Objetivos de aprendizagem

Você vai (1) comparar as visões corporativa, de engenharia de sistemas e orientada a ameaças da arquitetura de segurança; (2) relacionar os princípios de design à segmentação; (3) criticar uma afirmação de um framework; (4) apresentar um argumento de seminário com evidências.

### 2.1 Três visões da arquitetura

No seminário da Dra. Aydın, Kenji conhece três formas de ver a arquitetura de segurança. A visão corporativa, representada pelo SABSA e pelo guia do TOGAF, do The Open Group, sobre a integração de risco e segurança, parte dos atributos de negócio e os desdobra até os controles. A visão de engenharia de sistemas, representada pelo NIST SP 800-160 Vol. 1 Rev. 1, trata a segurança como uma propriedade emergente construída ao longo do ciclo de vida, com casos de garantia explícitos. A visão orientada a ameaças, representada por Shostack (2014), parte do que pode dar errado num design específico. Cada visão faz uma primeira pergunta diferente, e os bons arquitetos transitam entre elas de forma deliberada.

### 2.2 Os princípios por trás da segmentação

A segmentação aplica princípios mais antigos. O menor privilégio diz que cada estação deve alcançar apenas os serviços de que precisa. A mediação completa diz que todo acesso deve ser verificado, o que o SP 800-207 implementa por meio de pontos de aplicação de política. A separação de privilégios sugere que o acesso sensível exija mais de uma condição, como a integridade do dispositivo e a identidade do usuário. A economia de mecanismo alerta contra políticas tão complexas que ninguém consegue verificá-las. Kenji percebe que esse último princípio puxa contra os outros: uma segmentação mais fina aplica melhor o menor privilégio, mas cria mais regras, e cada regra não gerenciada é uma lacuna potencial.

### 2.3 Crítica a uma afirmação de framework

Uma leitura do seminário afirma que adotar zero trust elimina o movimento lateral. Kenji a critica. O próprio SP 800-207 descreve o zero trust como um conjunto de princípios e uma jornada, e não como um produto único, e reconhece ameaças às implantações de zero trust, como o comprometimento do ponto de decisão de política e as credenciais roubadas. O movimento lateral pode continuar com uma identidade válida por um caminho permitido. A afirmação justa é mais estreita: o zero trust pode reduzir os caminhos alcançáveis e tornar o movimento mais fácil de observar. Ele apresenta essa distinção com citação direta da seção de ameaças da publicação, e não com paráfrases de fontes secundárias.

### 2.4 Evidências no argumento do seminário

A Dra. Aydın pede a cada apresentador que marque as afirmações como princípio, orientação de framework, evidência de caso ou resultado medido. Os slides de Kenji trazem pequenas etiquetas. Quando um colega afirma que a microssegmentação sempre reduz os incidentes, Kenji pergunta que etiqueta se aplica, e a resposta é princípio mais estudos de caso de fornecedores, não medição. O exercício é desconfortável, mas útil: mostra à turma quanto da prática de arquitetura se apoia em raciocínio e experiência, e não em resultados medidos, o que é aceitável desde que seja dito com clareza e não seja apresentado como prova.

### 2.5 Produto do seminário

O artigo de seminário de Kenji argumenta que as estratégias de segmentação devem ser comparadas ao mesmo tempo pela alcançabilidade e pela complexidade das regras, porque uma estratégia que reduz o alcance mas exige milhares de regras impossíveis de gerenciar pode falhar na operação. Ele propõe medir as duas na dissertação. A turma o desafia a definir complexidade; ele escolhe o número de regras de permissão distintas como uma medida simples e imperfeita, e lista suas fraquezas. O artigo vira o capítulo conceitual da dissertação, e o desafio dos colegas vira uma das explicações concorrentes que ele vai testar depois.

### Exemplo resolvido

Kenji contrasta três visões de arquitetura, associa quatro princípios de Saltzer e Schroeder à segmentação, critica a afirmação de que o zero trust elimina o movimento lateral e propõe medir o alcance junto com o número de regras.

> **Caso sintético.** Os participantes do seminário e as afirmações são sintéticos; o SABSA, o TOGAF G152, o SP 800-160v1r1, o SP 800-207 e Shostack (2014) são reais.

### Erros e limites

O número de regras é uma aproximação grosseira da complexidade operacional. A marcação no seminário pode simplificar demais evidências mistas.

### Exercícios

- **EX008 — Primeiras perguntas.** Que primeira pergunta cada visão de arquitetura faz? *Rubrica:* 3 = corporativa: atributos de negócio; engenharia de sistemas: garantia ao longo do ciclo de vida; orientada a ameaças: o que pode dar errado;; 2 = duas;; 1 = uma;; 0 = nenhuma.

- **EX009 — Tensão entre princípios.** Que princípio puxa contra a segmentação fina, e por quê? *Rubrica:* 3 = economia de mecanismo, porque a segmentação mais fina cria mais regras a verificar;; 2 = nomeado;; 1 = nada;; 0 = nenhuma.

- **EX010 — Ameaças ao zero trust.** Cite uma ameaça às implantações de zero trust reconhecida no SP 800-207. *Rubrica:* 3 = comprometimento do ponto de decisão de política ou credenciais roubadas;; 2 = uma;; 1 = nada;; 0 = nenhuma.

- **EX011 — Afirmação justa sobre zero trust.** Qual é a versão justa de o zero trust elimina o movimento lateral? *Rubrica:* 3 = ele pode reduzir os caminhos alcançáveis e tornar o movimento mais fácil de observar;; 2 = reduz;; 1 = elimina;; 0 = nenhuma.

- **EX012 — Etiquetas de evidência.** Que quatro etiquetas a Dra. Aydın exige nas afirmações? *Rubrica:* 3 = princípio, orientação de framework, evidência de caso, resultado medido;; 2 = três;; 1 = uma;; 0 = nenhuma.

- **EX013 — Medida de complexidade.** Como Kenji mede a complexidade das regras, e qual é a fraqueza disso? *Rubrica:* 3 = número de regras de permissão distintas; aproximação grosseira;; 2 = medida;; 1 = nada;; 0 = nenhuma.

- **EX014 — Motivo do duplo desfecho.** Por que comparar as estratégias pelo alcance e pelo número de regras juntos? *Rubrica:* 3 = uma estratégia pode reduzir o alcance mas ser impossível de gerenciar na operação;; 2 = ambos;; 1 = só alcance;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Desenho do estudo, ética e reprodutibilidade

### Objetivos de aprendizagem

Você vai (1) desenhar um estudo de simulação com comparações controladas; (2) construir um modelo de alcançabilidade sobre redes sintéticas; (3) tratar a ética quando uma organização real molda o modelo; (4) planejar a reprodutibilidade desde o início.

### 3.1 Desenho da simulação

Kenji desenha seu estudo como uma simulação controlada. Ele gera muitas redes sintéticas cuja estrutura se parece com a da Vantor: departamentos de estações de trabalho, servidores compartilhados, alguns jump hosts administrativos e um controlador de domínio. A cada rede ele aplica três políticas: plana, por zonas com zonas departamentais e microssegmentação baseada em identidade. O desfecho é o número de servidores alcançáveis a partir de uma estação comprometida escolhida ao acaso. Gerar muitas redes em vez de uma protege contra conclusões que dependam de um único layout arbitrário, e comparar as três políticas na mesma rede elimina a variação que nada tem a ver com a política.

### 3.2 O modelo de alcançabilidade

Uma rede é modelada como um grafo direcionado: uma aresta do host A para o host B significa que a política permite que A se conecte a B. Um atacante numa estação consegue alcançar qualquer coisa ligada por um caminho, supondo que cada salto seja explorável. Essa premissa é deliberadamente pessimista e dá um limite superior para o alcance. O laboratório abaixo constrói uma pequena rede sintética sob as três políticas e conta os servidores alcançáveis com uma busca em largura. Os resultados mostram o padrão que Kenji espera: o acesso plano alcança todos os servidores, as zonas alcançam menos, as regras baseadas em identidade menos ainda, mas os jump hosts reabrem caminhos se suas regras forem amplas.

### Laboratório — Alcançabilidade sob três políticas

```python
# Count servers reachable from one compromised workstation under three synthetic policies (BFS).
from collections import deque
ws = ["ws-fin1", "ws-fin2", "ws-ops1", "ws-ops2"]
srv = {"erp": "fin", "payroll": "fin", "wms": "ops", "fleet": "ops", "files": "all", "dc": "all"}
dept = lambda h: h[3:6]
def edges(policy, broad_jump=False):
    E = {h: set() for h in ws + list(srv) + ["jump"]}
    for w in ws:
        for s, d in srv.items():
            if policy == "flat" or (policy == "zone" and d in (dept(w), "all")) \
               or (policy == "identity" and s == {"fin": "erp", "ops": "wms"}[dept(w)]):
                E[w].add(s)
        if policy == "identity": E[w].add("jump")
    if broad_jump: E["jump"] |= set(srv)
    return E
def reach(E, start):
    seen, q = {start}, deque([start])
    while q:
        for n in E[q.popleft()]:
            if n not in seen: seen.add(n); q.append(n)
    return len([n for n in seen if n in srv])
for p in ["flat", "zone", "identity"]:
    print(f"{p:9} servers reachable from ws-fin1: {reach(edges(p), 'ws-fin1')}")
print(f"identity + broad jump-host rule: {reach(edges('identity', True), 'ws-fin1')}")
```

Execute com `python3 lab_reach.py`. Saída verificada:

```text
flat      servers reachable from ws-fin1: 6
zone      servers reachable from ws-fin1: 4
identity  servers reachable from ws-fin1: 1
identity + broad jump-host rule: 6
```

### 3.3 Ética com uma parceira real

Embora as redes sejam sintéticas, elas são moldadas pela estrutura real da Vantor, que é uma informação sensível. Kenji obtém a permissão por escrito do empregador, combina que nenhum nome de host, endereço ou regra real aparecerá na dissertação e abstrai a estrutura em parâmetros como o número de departamentos e a proporção de servidores. Seu pedido ao comitê de ética declara que não há participantes humanos e que nenhum teste toca os sistemas da Vantor. Ele também considera o uso dual: um mapa detalhado de onde a Vantor é mais fraca ajudaria atacantes, então a dissertação relata apenas padrões agregados entre as redes geradas.

### 3.4 Plano de reprodutibilidade

Desde o primeiro dia, Kenji mantém o código em controle de versão, fixa as sementes aleatórias de cada experimento e registra os parâmetros de cada execução num arquivo de configuração guardado junto com os resultados. Ele escreve um script curto que roda de novo todos os experimentos do zero e confere se os números resumidos batem com os guardados. Registra as versões do software. A Dra. Aydın pede que ele tente rodar o pipeline inteiro numa máquina limpa na metade do projeto, o que revela uma dependência faltando. Planejar a reprodutibilidade cedo é muito mais barato do que reconstruí-la antes da entrega, quando a memória das decisões passadas já se apagou.

### 3.5 Pré-especificação da análise

Antes de rodar os experimentos principais, Kenji escreve seu plano de análise: a comparação principal é o alcance médio da segmentação por identidade contra o da segmentação por zonas, com um intervalo de confiança por bootstrap; as medidas secundárias são o número de regras e o efeito da amplitude das regras dos jump hosts. Ele faz commit do plano no repositório com carimbo de tempo. Análises exploratórias são permitidas depois, mas precisam ser rotuladas. Essa disciplina importa mesmo em simulação, porque com muitos parâmetros é fácil procurar até que alguma configuração mostre uma diferença marcante e depois apresentá-la como se tivesse sido o plano desde o começo.

### Exemplo resolvido

Kenji desenha uma simulação de três políticas sobre redes geradas, roda o laboratório de alcançabilidade, escreve um plano ético que abstrai a estrutura da Vantor e faz commit de um plano de análise com sementes e configurações.

> **Caso sintético.** Os parâmetros de estrutura da Vantor e a rede do laboratório são sintéticos.

### Erros e limites

Supor que todo salto é explorável superestima o alcance; atacantes reais enfrentam patches e detecção. As redes geradas podem não reproduzir topologias reais incomuns.

### Exercícios

- **EX015 — Comparação na mesma rede.** Por que aplicar as três políticas à mesma rede gerada? *Rubrica:* 3 = elimina a variação não relacionada à política;; 2 = controle;; 1 = sem motivo;; 0 = nenhuma.

- **EX016 — Significado da aresta.** O que significa uma aresta de A para B no modelo? *Rubrica:* 3 = a política permite que A se conecte a B;; 2 = conexão permitida;; 1 = cabo físico;; 0 = nenhuma.

- **EX017 — Limite pessimista.** Por que supor que todo salto é explorável é chamado de pessimista? *Rubrica:* 3 = dá um limite superior para o alcance do atacante;; 2 = limite superior;; 1 = otimista;; 0 = nenhuma.

- **EX018 — Contagens do laboratório.** Que contagens de servidores alcançáveis o laboratório imprimiu para as políticas plana, por zonas e por identidade? *Rubrica:* 3 = plana 6, zonas 4, identidade 1;; 2 = duas corretas;; 1 = erradas;; 0 = nenhuma.

- **EX019 — Efeito do jump host.** O que o laboratório mostrou quando as regras do jump host eram amplas? *Rubrica:* 3 = o alcance voltou a 6, reabrindo caminhos;; 2 = subiu;; 1 = sem mudança;; 0 = nenhuma.

- **EX020 — Preocupação com o uso dual.** Como Kenji lida com o risco de uso dual dos achados? *Rubrica:* 3 = relata só padrões agregados, sem pontos fracos específicos da Vantor;; 2 = agregado;; 1 = publica o mapa;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Arquitetura e engenharia de segurança: explicações concorrentes

### Objetivos de aprendizagem

Você vai (1) listar as explicações rivais para um resultado esperado; (2) desenhar verificações que as distingam; (3) reconhecer os artefatos das escolhas de modelagem; (4) decidir de antemão o que mudaria sua conclusão.

### 4.1 Rivais da hipótese principal

Kenji espera que a microssegmentação baseada em identidade reduza o alcance. Antes de testar, ele lista as rivais que poderiam produzir o mesmo padrão. Primeiro, a diferença poderia vir só do número de arestas permitidas, e não da identidade: qualquer política com menos arestas pareceria melhor. Segundo, ela poderia depender do tamanho da rede e aparecer só em redes pequenas. Terceiro, poderia ser um artefato do modo como ele gerou as regras de identidade, dando a cada estação exatamente um servidor. Quarto, os resultados poderiam depender dos jump hosts, que o laboratório do capítulo 3 mostrou serem capazes de apagar o benefício. Cada rival prevê algo diferente que ele pode verificar.

### 4.2 Verificações que separam as rivais

Para a rival do número de arestas, Kenji acrescenta uma política de controle: arestas aleatórias removidas da rede plana até ela ter o mesmo número de arestas da política por identidade. Se a identidade ainda vencer esse controle aleatório, a estrutura importa, e não só o número de arestas. Para a rival do tamanho, ele gera redes de três tamanhos. Para o artefato de geração, varia quantos servidores cada identidade pode alcançar, de um a quatro. Para os jump hosts, varia a amplitude das suas regras. Cada verificação é um pequeno experimento escrito no plano antes das execuções principais, para que a dissertação possa relatar quais rivais sobreviveram.

### 4.3 Artefatos de modelagem

Os resultados de simulação podem refletir as escolhas de modelagem, e não a realidade. O modelo de Kenji trata todos os hosts como igualmente exploráveis, ignora o tempo e supõe que as políticas são aplicadas com perfeição. Se os pontos de aplicação reais estiverem mal configurados uma parte do tempo, as políticas por identidade, com muitas regras finas, podem vazar mais do que as políticas por zonas, com poucas regras amplas. Ele acrescenta um parâmetro de configuração incorreta que adiciona ao acaso uma pequena parcela de arestas não intencionais. Isso retoma a preocupação com a economia de mecanismo do seminário: conjuntos complexos de regras oferecem mais chances de erro, e o modelo deve conseguir mostrar esse tradeoff, em vez de eliminá-lo por premissa.

### 4.4 O que mudaria a conclusão

Kenji escreve, antes de ver os resultados, o que o faria concluir que a segmentação baseada em identidade não oferece uma vantagem relevante: se seu alcance médio ficar a menos de um servidor do controle de arestas aleatórias, ou se uma taxa de configuração incorreta de dois por cento apagar a maior parte da diferença. Escrever esses limiares de antemão o protege de mudar as regras do jogo depois de ver os dados. A Dra. Aydın observa que a maioria das dissertações de mestrado nunca declara essas condições, e que fazê-lo é um dos sinais mais claros de maturidade de pesquisa que um examinador pode ver.

### 4.5 Discussão das rivais com praticantes

Kenji apresenta sua lista de rivais a dois engenheiros de rede da Vantor. Eles acrescentam uma rival que ele não tinha visto: na prática, as regras baseadas em identidade costumam ser escritas copiando modelos, de modo que muitas estações acabam com o mesmo acesso amplo, o que reduz o benefício. Ele acrescenta um parâmetro de modelo que faz uma parcela das estações herdar um conjunto amplo de regras. Os praticantes conhecem modos de falha que a literatura raramente registra, e consultá-los cedo melhora o realismo do modelo. Ele reconhece a contribuição deles na dissertação sem nomeá-los, como combinado.

### Exemplo resolvido

Kenji lista cinco rivais, acrescenta um controle de arestas aleatórias, variações de tamanho e de geração, uma taxa de configuração incorreta e um parâmetro de cópia de modelos, e escreve os limiares que derrubariam sua expectativa.

> **Caso sintético.** As rivais, os limiares e a contribuição dos engenheiros são sintéticos.

### Erros e limites

Nenhuma lista de rivais é completa. Os parâmetros acrescentados para modelar a realidade podem multiplicar as execuções e tentar a um relato seletivo.

### Exercícios

- **EX021 — Rival do número de arestas.** O que o controle de arestas aleatórias testa? *Rubrica:* 3 = se a vantagem da identidade vem da estrutura ou só de ter menos arestas;; 2 = estrutura;; 1 = nada;; 0 = nenhuma.

- **EX022 — Artefato de geração.** Como Kenji testa o artefato de geração das regras de identidade? *Rubrica:* 3 = varia de um a quatro quantos servidores cada identidade pode alcançar;; 2 = varia;; 1 = ignora;; 0 = nenhuma.

- **EX023 — Parâmetro de configuração incorreta.** Por que acrescentar ao modelo uma taxa de configuração incorreta? *Rubrica:* 3 = a aplicação real erra, e conjuntos complexos de regras oferecem mais chances de erro;; 2 = erros;; 1 = não é necessário;; 0 = nenhuma.

- **EX024 — Limiares de reversão.** Enuncie uma condição pré-definida que derrubaria a expectativa de Kenji. *Rubrica:* 3 = identidade a menos de um servidor do controle aleatório, ou dois por cento de configuração incorreta apagando a maior parte do ganho;; 2 = uma;; 1 = nada;; 0 = nenhuma.

- **EX025 — Rival dos praticantes.** Que rival os engenheiros acrescentaram? *Rubrica:* 3 = a cópia de modelos dá a muitas estações o mesmo acesso amplo;; 2 = modelo;; 1 = nada;; 0 = nenhuma.

- **EX026 — Sinal de maturidade.** O que a Dra. Aydın chama de sinal claro de maturidade de pesquisa? *Rubrica:* 3 = declarar de antemão o que mudaria a conclusão;; 2 = condições prévias;; 1 = tese longa;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX026 (as de EX027–EX050 estão na edição em inglês até a tradução dos capítulos correspondentes). Kenji Albrecht, a Dra. Selin Aydın, a Northmoor University, a Vantor Logistics e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** População: redes simuladas como a da Vantor; intervenção: microssegmentação baseada em identidade; comparação: segmentação por zonas; desfecho: servidores alcançáveis a partir de uma estação comprometida.

**EX002.** Cabe no prazo de um mestrado e evita os riscos de experimentar numa rede de produção.

**EX003.** Que a alcançabilidade só aproxima o avanço do atacante e não mede incidentes reais.

**EX004.** Para evitar escolher, sem perceber, só os estudos que apoiam a resposta esperada.

**EX005.** 312 registros passaram pela triagem e 27 estudos foram incluídos.

**EX006.** Estudos de caso que mostram atacantes se movendo amplamente por redes planas depois de um único comprometimento.

**EX007.** Poucos estudos comparam estratégias de segmentação em redes idênticas com premissas idênticas.

**EX008.** A corporativa pergunta que atributos de negócio importam; a de engenharia de sistemas pergunta como a segurança é construída e garantida ao longo do ciclo de vida; a orientada a ameaças pergunta o que pode dar errado neste design.

**EX009.** A economia de mecanismo, já que a segmentação mais fina multiplica as regras que precisam ser entendidas e verificadas.

**EX010.** O comprometimento dos componentes de decisão ou de aplicação de política, ou o uso indevido de credenciais válidas roubadas.

**EX011.** Que o zero trust pode reduzir os caminhos disponíveis e tornar o movimento lateral mais fácil de detectar, e não eliminá-lo.

**EX012.** Princípio, orientação de framework, evidência de caso e resultado medido.

**EX013.** Pelo número de regras de permissão distintas, uma aproximação grosseira que ignora a interação entre as regras e a frequência de mudança.

**EX014.** Porque uma estratégia que corta o alcance mas exige regras impossíveis de gerenciar pode falhar na prática.

**EX015.** Para garantir que as diferenças de alcance venham da política, e não de layouts de rede diferentes.

**EX016.** Que a política permite que o host A abra uma conexão com o host B.

**EX017.** Porque supõe que o atacante sempre tem sucesso em cada salto, de modo que o resultado é um limite superior para o alcance.

**EX018.** A plana alcançou 6 servidores, a por zonas alcançou 4 e a baseada em identidade alcançou 1.

**EX019.** Com uma regra ampla no jump host, o alcance da baseada em identidade voltou a 6 servidores, mostrando que os jump hosts podem reabrir caminhos.

**EX020.** Ele relata apenas padrões agregados entre as redes geradas, nunca um mapa das fraquezas específicas da Vantor.

**EX021.** Se a segmentação por identidade ajuda por causa da sua estrutura, e não simplesmente porque permite menos arestas.

**EX022.** Variando de um a quatro o número de servidores que a identidade de cada estação pode alcançar.

**EX023.** Porque as políticas reais às vezes são configuradas incorretamente, e conjuntos de regras finos dão mais oportunidades para esses erros.

**EX024.** Se o alcance médio da identidade ficar a menos de um servidor do controle de arestas aleatórias.

**EX025.** Que as regras de identidade costumam ser copiadas de modelos, dando a muitas estações o mesmo acesso amplo.

**EX026.** Escrever, antes de ver os resultados, as observações que mudariam a conclusão.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Herley, C., & van Oorschot, P. C. (2017). SoK: Science, security and the elusive goal of security as a scientific pursuit. *2017 IEEE Symposium on Security and Privacy*, 99–120. <https://doi.org/10.1109/SP.2017.38>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sherwood, J., Clark, A., & Lynas, D. (2005). *Enterprise security architecture: A business-driven approach* (SABSA). CMP Books.
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
- The Open Group. (2016, revised 2022). *Integrating risk and security within a TOGAF enterprise architecture* (TOGAF Series Guide G152). The Open Group.
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in software engineering*. Springer. <https://doi.org/10.1007/978-3-642-29044-2>
