# Fatores Humanos e Política Cibernética: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 098, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 40 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 5 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 11–40 (EX031–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de bacharelado que aprendem a estudar, projetar e avaliar o comportamento de segurança e os reportes numa pequena organização pública.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios contam reportes, calculam taxas, intervalos de Wilson, funis e medianas e consultam SQLite sobre dados sintéticos; nenhum funcionário, usuário, e-mail ou conta real está envolvido. Toda simulação de phishing descrita é anunciada, acordada com os representantes dos funcionários, evita iscas que explorem sofrimento pessoal e é relatada apenas de forma agregada; os testes de usabilidade usam uma caixa postal de teste com voluntários que sabem que estão testando a ferramenta, e não sendo testados. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos 1–18 constroem os fundamentos (raciocínio, computação, programação, escrita, letramento, dados, ética, estatística, identidade, privacidade, medição, arquitetura, criptografia e métodos de pesquisa) por meio de um único caso de bibliotecas; os capítulos 19–32 desenvolvem a teoria de fatores humanos, modelos, métodos, controles, verificação, análise de falhas e operações, com dois laboratórios; os capítulos 33–40 cobrem o projeto comparativo, o trabalho de conclusão com voluntários e a tese. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Nadia Farouk** | Estudante de bacharelado | Inventada |
| **Dr. Owen Prescott** | Orientador | Inventado |
| **Fenmoor University** | Universidade fictícia | Inventada |
| **Ashcombe Community Library Network** | Rede de bibliotecas fictícia, 120 funcionários, nove unidades | Inventada |
| **Dunmore Libraries** | Rede fictícia de comparação, 150 funcionários | Inventada |

### Fontes principais

Adams e Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806); Sasse, Brostoff e Weirich (2001), [doi:10.1023/A:1011902718709](https://doi.org/10.1023/A:1011902718709); Wilson et al. (1998), NIST SP 800-16; Hansche et al. (2024), NIST SP 800-50r1; Herley (2009), [doi:10.1145/1719030.1719050](https://doi.org/10.1145/1719030.1719050); Lain, Kostiainen e Čapkun (2022), [doi:10.1109/SP46214.2022.9833766](https://doi.org/10.1109/SP46214.2022.9833766). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem

Você vai (1) usar razões e porcentagens para descrever o comportamento de segurança; (2) raciocinar sobre taxas-base ao julgar alertas; (3) conferir afirmações com aritmética simples.

### 1.1 Razões e taxas

Nadia Farouk, estudante do primeiro ano da fictícia Fenmoor University, começa o curso estudando uma rede de bibliotecas. A fictícia Ashcombe Community Library Network tem 120 funcionários distribuídos em nove unidades. No ano passado, os funcionários reportaram 48 e-mails suspeitos, e 12 deles eram de fato maliciosos. Uma razão compara duas contagens, e uma taxa expressa uma contagem por unidade, como reportes por cem funcionários. Nadia calcula 48 reportes para 120 funcionários, ou 40 por cem funcionários, e 12 de 48, ou um quarto, como a proporção de reportes que eram ameaças reais.

### 1.2 Taxas-base

Seu orientador, o Dr. Owen Prescott, pede a Nadia que pense nas taxas-base. Se um e-mail em mil é malicioso e um banner de alerta sinaliza 5% de todos os e-mails, a maioria dos e-mails sinalizados será inofensiva, porque os e-mails inofensivos superam em muito os maliciosos. Pessoas que veem muitos alertas falsos aprendem a ignorá-los, um padrão que Herley (2009) descreveu ao argumentar que os usuários ignoram racionalmente conselhos cujos custos superam os benefícios. Entender as taxas-base ajuda Nadia a ver por que um comportamento que parece descuidado pode ser uma resposta sensata a sinais ruidosos.

### 1.3 Conferir afirmações

Nadia lê o folheto de um fornecedor que afirma que o treinamento reduz o risco de phishing em 70%. Ela pergunta: 70% de quê, medido como e comparado com quê? Uma queda nos cliques em e-mails simulados fáceis não significa uma queda nas perdas reais. Ela confere a aritmética de outra afirmação, a de que os reportes subiram de 20 para 48, e descobre que se trata de um aumento de 140%, e não dos 240% declarados. Aritmética simples e perguntas cuidadosas protegem contra números enganosos, comuns no marketing de segurança e até em relatórios internos. Ela mantém uma lista de verificação com essas perguntas.

### Laboratório — Taxas-base e alertas falsos

```python
# Base rates and false warnings (synthetic): 100,000 emails, 1 in 1,000 malicious.
n = 100_000; mal = n // 1000; ben = n - mal
flag_mal = int(mal * 0.90)          # banner catches 90% of malicious
flag_ben = int(ben * 0.05)          # and flags 5% of harmless
flagged = flag_mal + flag_ben
print(f"flagged {flagged}: malicious {flag_mal}, harmless {flag_ben} ({flag_ben / flagged:.0%} harmless)")
```

Execute com `python3 lab_base.py`. Saída verificada:

```text
flagged 5085: malicious 90, harmless 4995 (98% harmless)
```

### Exemplo resolvido

Nadia calcula taxas de reporte, usa as taxas-base para explicar alertas ignorados e confere porcentagens declaradas.

> **Caso sintético.** A rede de bibliotecas é sintética; Herley (2009) é real.

### Erros e limites

Porcentagens escondem contagens pequenas. As taxas-base mudam com o tempo.

### Exercícios

- **EX001 — Reportes por cem.** Quantos reportes por cem funcionários a Ashcombe recebeu? *Rubrica:* 3 = 40;; 2 = 48 por 120;; 1 = 48;; 0 = nenhuma.
- **EX002 — Proporção inofensiva sinalizada.** No laboratório, que proporção dos e-mails sinalizados era inofensiva? *Rubrica:* 3 = cerca de 98%;; 2 = a maioria;; 1 = 5%;; 0 = nenhuma.
- **EX003 — Conferir o aumento.** Qual é o aumento real de 20 para 48 reportes? *Rubrica:* 3 = 140%;; 2 = 28 a mais;; 1 = 240%;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever as partes de um sistema computacional que os funcionários usam no dia a dia; (2) identificar onde as pessoas interagem com a segurança; (3) mapear uma jornada simples do usuário.

### 2.1 Partes de um sistema

Um sistema computacional inclui hardware, software, dados, redes e as pessoas que os usam. Na Ashcombe, os funcionários usam computadores de mesa compartilhados nos balcões, notebooks nos escritórios e um sistema de gestão da biblioteca que guarda os cadastros dos usuários. Os computadores públicos são usados pelos visitantes. Nadia aprende que a segurança depende de todas essas partes funcionarem juntas. Uma política forte de senhas no sistema de gestão pouco significa se os funcionários deixam os computadores do balcão logados enquanto atendem os usuários, porque muitas vezes é a interação mais fraca que decide o resultado, e não o controle técnico mais forte.

### 2.2 Pontos de interação

Nadia lista os pontos em que os funcionários interagem com a segurança: fazer login no início dos turnos, bloquear a tela ao se afastar, tratar pedidos de dados de usuários, abrir e-mails e aprovar atualizações de software. Cada ponto exige atenção e tempo. Adams e Sasse (1999) mostraram que os usuários têm dificuldade com mecanismos de segurança que não se encaixam em seu trabalho, e que eles não são o inimigo, mas pessoas tentando fazer seu trabalho. Mapear esses pontos ajuda Nadia a ver onde o sistema exige demais das pessoas e onde o design poderia ajudá-las.

### 2.3 Uma jornada do usuário

Nadia mapeia a jornada de um atendente de balcão durante uma manhã movimentada: fazer login, atender os usuários, afastar-se para buscar um livro, voltar, responder a uma consulta por telefone e verificar o e-mail entre um atendimento e outro. Ela observa que bloquear a tela a cada vez leva vários segundos e exige digitar a senha de novo. Os atendentes muitas vezes deixam as telas desbloqueadas porque as filas se formam rapidamente. Ela sugere um bloqueio automático curto com desbloqueio por cartão de aproximação. O mapa mostra que o problema está no encaixe entre a tarefa e o controle, e não na atitude dos funcionários.

### Exemplo resolvido

Nadia lista as partes do sistema, identifica os pontos de interação e mapeia a jornada de um atendente de balcão para sugerir o desbloqueio por cartão de aproximação.

> **Caso sintético.** A jornada é sintética; Adams e Sasse (1999) é real.

### Erros e limites

Mapas de jornada simplificam o trabalho real. Leitores de cartão custam dinheiro.

### Exercícios

- **EX004 — Interação mais fraca.** Por que uma política forte de senhas pouco importa em um caso? *Rubrica:* 3 = se os computadores do balcão ficam logados;; 2 = logados;; 1 = nada;; 0 = nenhuma.
- **EX005 — Adams e Sasse.** O que Adams e Sasse (1999) mostraram sobre os usuários? *Rubrica:* 3 = não são o inimigo e têm dificuldade com mecanismos que não se encaixam;; 2 = encaixe;; 1 = descuidados;; 0 = nenhuma.
- **EX006 — Correção sugerida.** Que correção Nadia sugeriu para as telas desbloqueadas? *Rubrica:* 3 = bloqueio automático curto com desbloqueio por cartão de aproximação;; 2 = cartão de aproximação;; 1 = senhas mais longas;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever Python simples para contar e resumir registros; (2) usar listas e dicionários para dados de comportamento; (3) testar um script com entradas conhecidas.

### 3.1 Contar registros

Nadia escreve seu primeiro script em Python para contar os reportes de e-mails suspeitos por unidade. Cada registro é uma linha com data, unidade e veredito. O script lê as linhas, divide cada uma em campos e soma um ao contador da unidade. O dicionário do Python é ideal para isso, porque associa o nome de cada unidade à sua contagem. Ela imprime os totais em ordem. Até uma contagem simples é útil: mostra que duas unidades com computadores públicos reportam muito mais e-mails do que as outras, o que levanta uma pergunta que vale a pena investigar.

### 3.2 Listas e dicionários

Uma lista guarda itens em ordem, como todas as datas de reporte, enquanto um dicionário guarda pares, como unidade e contagem. Nadia usa uma lista de dicionários, um por reporte, para que cada reporte mantenha seus campos juntos. Em seguida, filtra a lista para encontrar os reportes maliciosos e os agrupa por unidade. Ela aprende a manter os dados sintéticos e sem nomes de pessoas, já que até código de prática deve respeitar a privacidade. Bons hábitos aprendidos em scripts pequenos se levam para projetos maiores mais adiante no curso.

### Laboratório — Contagem de reportes por unidade

```python
# Count synthetic suspicious-email reports by branch.
rows = ["2026-01-03,Central,malicious", "2026-01-04,Riverside,harmless"] + \
       [f"2026-{2 + d // 28:02d}-{1 + d % 28:02d},{b},{v}" for d, (b, v) in enumerate(
           [("Central", "harmless")] * 13 + [("Riverside", "malicious")] * 9 + [("Hill", "harmless")] * 6 +
           [("Market", "harmless")] * 5 + [("Oakfield", "malicious")] * 4 + [("Mill", "harmless")] * 3 +
           [("Quay", "harmless")] * 3 + [("Elm", "harmless")] * 2 + [("Abbey", "malicious")] * 1, start=1) if True]
counts = {}
for r in rows:
    parts = r.split(",")
    if len(parts) != 3: print("skip", r); continue
    counts[parts[1]] = counts.get(parts[1], 0) + 1
for b, c in sorted(counts.items(), key=lambda x: -x[1]): print(b, c)
print("total", sum(counts.values()))
```

Execute com `python3 lab_count.py`. Saída verificada:

```text
Central 14
Riverside 10
Hill 6
Market 5
Oakfield 4
Mill 3
Quay 3
Elm 2
Abbey 1
total 48
```

### 3.3 Testar com entradas conhecidas

Nadia testa o script criando um arquivo minúsculo com cinco reportes cujos totais ela conhece. Se a saída do script coincide com sua contagem manual, ela ganha confiança. Ela também testa um arquivo vazio e uma linha com um campo faltando, e acrescenta uma verificação que pula linhas quebradas com um aviso. Testar com entradas conhecidas é uma disciplina básica da programação, e importa no trabalho de segurança porque contagens erradas podem levar a decisões erradas sobre onde investir esforço ou treinamento.

### Exemplo resolvido

Nadia conta reportes sintéticos por unidade com um dicionário, agrupa os reportes maliciosos e testa o script com entradas conhecidas.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Linhas quebradas podem esconder problemas reais. Testes pequenos não provam a correção.

### Exercícios

- **EX007 — Uso do dicionário.** Por que um dicionário é adequado para contar por unidade? *Rubrica:* 3 = associa cada unidade à sua contagem;; 2 = associação;; 1 = ordem da lista;; 0 = nenhuma.
- **EX008 — Unidade no topo.** Que unidade mais reportou no laboratório? *Rubrica:* 3 = Central, com 14;; 2 = Central;; 1 = nada;; 0 = nenhuma.
- **EX009 — Linhas quebradas.** Como o script trata uma linha com um campo faltando? *Rubrica:* 3 = pula a linha com um aviso;; 2 = pula;; 1 = trava;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem

Você vai (1) estruturar um argumento acadêmico curto; (2) citar fontes com precisão; (3) distinguir evidência de opinião.

### 4.1 Estruturar um argumento

O primeiro ensaio de Nadia pergunta se os funcionários são o elo mais fraco da segurança. Ela o estrutura com uma tese, razões, evidências e uma conclusão. Sua tese é que chamar os funcionários de elo mais fraco direciona mal o esforço. Suas razões são que os sistemas muitas vezes exigem demais das pessoas e que culpar os funcionários desestimula os reportes. Cada parágrafo defende um ponto e leva ao seguinte. O Dr. Prescott lembra que um bom argumento também enfrenta o contra-argumento mais forte, que neste caso é o de que muitas violações de fato envolvem ações humanas.

### 4.2 Citar com precisão

Nadia cita Sasse, Brostoff e Weirich (2001), cujo artigo sobre transformar o elo mais fraco argumentou que a segurança deve ser projetada em torno das capacidades humanas. Ela também cita o Verizon Data Breach Investigations Report, que relata que uma grande parcela das violações envolve um elemento humano. Ela confere cada fonte diretamente, em vez de copiar citações de outros ensaios, registra os dados completos e nunca inventa um número de página ou um DOI. A citação precisa permite aos leitores conferir suas evidências e a protege de repetir os erros de outros sobre o que uma fonte de fato disse.

### 4.3 Evidência e opinião

Nadia aprende a separar evidências, como os achados de um estudo, de opiniões, como a visão de um blogueiro. Ela marca cada frase do rascunho como tese, evidência ou interpretação. Encontra duas frases em que apresentou uma opinião como fato e as reescreve com ressalvas. Também observa que o número do elemento humano do DBIR conta juntos erros, uso indevido e engenharia social, de modo que não mostra que os funcionários são descuidados. Ler o que uma estatística de fato mede faz parte da escrita acadêmica honesta.

### Exemplo resolvido

Nadia escreve um ensaio estruturado sobre a ideia do elo mais fraco, cita Sasse et al. e o DBIR com precisão e separa evidência de opinião.

> **Caso sintético.** O ensaio é sintético; Sasse et al. (2001) e o Verizon DBIR são reais.

### Erros e limites

Ressalvas podem virar imprecisão. Os relatórios atualizam seus números todo ano.

### Exercícios

- **EX010 — Contra-argumento.** Que contra-argumento Nadia precisa enfrentar? *Rubrica:* 3 = muitas violações envolvem ações humanas;; 2 = elemento humano;; 1 = nada;; 0 = nenhuma.
- **EX011 — Sasse et al.** O que Sasse, Brostoff e Weirich (2001) argumentaram? *Rubrica:* 3 = a segurança deve ser projetada em torno das capacidades humanas;; 2 = design;; 1 = os usuários são descuidados;; 0 = nenhuma.
- **EX012 — Cautela com o DBIR.** Por que o número do DBIR não mostra que os funcionários são descuidados? *Rubrica:* 3 = combina erros, uso indevido e engenharia social;; 2 = combinado;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) definir conscientização, treinamento e educação em segurança; (2) reconhecer táticas comuns de engenharia social; (3) explicar por que o conhecimento não garante o comportamento.

### 5.1 Conscientização, treinamento, educação

A NIST SP 800-16 (Wilson et al., 1998) distinguiu a conscientização, que chama a atenção para a segurança, do treinamento, que desenvolve habilidades, e da educação, que desenvolve compreensão. A NIST SP 800-50r1 (Hansche et al., 2024) atualiza a orientação para construir um programa de aprendizagem em cibersegurança e privacidade. Nadia usa essas distinções para analisar os esforços atuais da Ashcombe: um vídeo anual conta como conscientização, mas ninguém foi treinado para verificar pedidos incomuns. Ela percebe que funcionários diferentes precisam de combinações diferentes, e que a conscientização sozinha não desenvolve as habilidades necessárias para tratar com segurança os pedidos de dados de usuários.

### 5.2 Táticas de engenharia social

Nadia estuda táticas comuns descritas por Hadnagy (2018): o pretexting, em que o atacante inventa uma história crível; o phishing, com e-mails enganosos; e a falsificação de identidade por telefone. Os princípios de influência de Cialdini, como autoridade, urgência e afinidade, explicam por que essas táticas funcionam. Numa biblioteca, alguém pode ligar fingindo ser um servidor da prefeitura que exige com urgência dados de usuários. Nadia aprende a reconhecer esses padrões para poder desenhar procedimentos que ajudem os funcionários a fazer uma pausa, mas os estuda apenas para defender, nunca para enganar pessoas reais sem autorização.

### 5.3 Conhecimento e comportamento

Os funcionários da Ashcombe sabem descrever o phishing quando perguntados, mas alguns ainda clicam. Nadia aprende que saber não é fazer. Bada, Sasse e Nurse (2019) argumentaram que as campanhas de conscientização muitas vezes falham porque supõem que o conhecimento leva ao comportamento, ignorando a carga de trabalho, os hábitos e o esforço que as ações seguras exigem. As pessoas agem sob pressão de tempo, com informação incompleta e objetivos concorrentes. O letramento em segurança inclui, portanto, entender por que o comportamento se afasta do conhecimento, o que aponta para desenhar opções seguras mais fáceis, em vez de repetir as mesmas mensagens mais alto. O Dr. Prescott concorda.

### Exemplo resolvido

Nadia distingue conscientização, treinamento e educação, reconhece pretexting e táticas de influência e explica por que o conhecimento não garante o comportamento.

> **Caso sintético.** Os exemplos são sintéticos; SP 800-16, SP 800-50r1, Hadnagy (2018), Cialdini (2021) e Bada et al. (2019) são reais.

### Erros e limites

As táticas evoluem. Na prática, as categorias se sobrepõem.

### Exercícios

- **EX013 — Três níveis.** Que três níveis a SP 800-16 distinguiu? *Rubrica:* 3 = conscientização, treinamento e educação;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX014 — Pretexting.** O que é pretexting? *Rubrica:* 3 = inventar uma história crível para enganar;; 2 = história;; 1 = phishing;; 0 = nenhuma.
- **EX015 — Falha das campanhas.** Por que as campanhas muitas vezes falham, segundo Bada et al. (2019)? *Rubrica:* 3 = supõem que o conhecimento leva ao comportamento;; 2 = suposição;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem

Você vai (1) usar conjuntos e lógica para descrever regras de política; (2) modelar relações de reporte como grafos; (3) encontrar lacunas nas regras com lógica simples.

### 6.1 Conjuntos e política

Um conjunto é uma coleção de itens distintos. Nadia descreve os funcionários da Ashcombe como conjuntos: atendentes de balcão, gestores, pessoal de TI e voluntários. Uma regra de política pode dizer que apenas gestores e pessoal de TI podem exportar listas de usuários. Em termos de conjuntos, os exportadores permitidos são a união de gestores e pessoal de TI. Ela confere a lista de acesso real e descobre que dois voluntários pertencem ao conjunto de exportadores. Expressar regras como conjuntos facilita comparar o que a política pretende com o que o sistema de fato permite.

### 6.2 Grafos de reporte

Um grafo tem nós ligados por arestas. Nadia desenha um grafo em que os funcionários são nós e uma aresta mostra a quem cada pessoa contaria sobre um e-mail suspeito. A maioria dos atendentes contaria ao gestor da unidade, que poderia ou não contar à TI. Algumas unidades não têm nenhum caminho até a TI. O laboratório encontra quais nós não alcançam o nó da TI. Um grafo torna visíveis as rotas por onde os alertas viajam e mostra onde a ausência de um único gestor poderia impedir que um reporte importante chegasse a quem pode agir.

### Laboratório — Quais funcionários não alcançam a TI

```python
# Reporting graph: who can reach IT? (synthetic)
edges = {"IT": [], "Central-mgr": ["IT"], "Riverside-mgr": ["IT"], "Hill-mgr": ["Central-mgr"], "Quay-mgr": [], "Elm-mgr": []}
staff = {"Central": 20, "Riverside": 18, "Hill": 12, "Quay": 5, "Elm": 6}
for b in staff: edges[f"{b}-staff"] = [f"{b}-mgr"]
def reach(n, seen=None):
    seen = seen or set()
    if n == "IT": return True
    seen.add(n)
    return any(reach(m, seen) for m in edges[n] if m not in seen)
blocked = [b for b in staff if not reach(f"{b}-staff")]
print("branches without a route to IT:", blocked, "staff:", sum(staff[b] for b in blocked))
```

Execute com `python3 lab_graph.py`. Saída verificada:

```text
branches without a route to IT: ['Quay', 'Elm'] staff: 11
```

### 6.3 Lógica e lacunas

Nadia escreve em lógica a regra dos computadores dos visitantes: uma sessão deve terminar se o visitante sair ou se passarem trinta minutos. Ela testa casos e encontra uma lacuna: se um visitante sai sem encerrar a sessão e outro se senta em menos de trinta minutos, a sessão continua com o e-mail do primeiro visitante aberto. Ela propõe acrescentar uma regra para que as sessões terminem quando a tela ficar ociosa por três minutos. A lógica simples expõe casos que a linguagem comum esconde, e testar regras contra casos é um hábito que ela usará ao longo do curso.

### Exemplo resolvido

Nadia usa conjuntos para comparar a política com as listas de acesso, um grafo para encontrar funcionários sem rota até a TI e lógica para encontrar uma lacuna nas sessões dos visitantes.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

As rotas reais de reporte são informais. Tempos de ociosidade podem incomodar os visitantes.

### Exercícios

- **EX016 — União de conjuntos.** Que união de conjuntos descreve os exportadores permitidos? *Rubrica:* 3 = gestores e pessoal de TI;; 2 = união;; 1 = voluntários;; 0 = nenhuma.
- **EX017 — Funcionários inalcançáveis.** Quantos funcionários não alcançavam a TI no laboratório? *Rubrica:* 3 = 11, em Quay e Elm;; 2 = 11;; 1 = nada;; 0 = nenhuma.
- **EX018 — Lacuna da sessão.** Que lacuna o teste lógico revelou? *Rubrica:* 3 = um novo visitante herda uma sessão aberta;; 2 = herdar;; 1 = nada;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) explicar como o e-mail trafega e como a identidade do remetente pode ser forjada; (2) descrever a autenticação de e-mail em alto nível; (3) relacionar os limites dos protocolos ao julgamento humano.

### 7.1 Como o e-mail trafega

Quando alguém envia um e-mail, seu servidor de correio o repassa pela internet ao servidor do destinatário, que o armazena até que o destinatário o leia. O protocolo básico de e-mail foi projetado para a cooperação, e não para a segurança, por isso o endereço do remetente exibido ao leitor pode ser definido como quase qualquer coisa. Nadia aprende que é por isso que funcionários da Ashcombe receberam mensagens que pareciam vir da bibliotecária-chefe, mas que na verdade foram enviadas de outro lugar. Entender essa história do projeto explica por que as pessoas não podem confiar no nome do remetente exibido.

### 7.2 Verificações de autenticação

Os sistemas de e-mail hoje acrescentam verificações que permitem aos servidores de destino testar se uma mensagem veio de um servidor autorizado pelo domínio do remetente. Quando as verificações falham, o sistema de destino pode rejeitar a mensagem ou marcá-la. Nadia aprende esses mecanismos apenas em linhas gerais, o suficiente para entender que eles reduzem as mensagens com domínio forjado, mas não impedem domínios parecidos (lookalike) nem contas legítimas comprometidas. Ela observa que as verificações técnicas deslocam o problema em vez de eliminá-lo, deixando parte do julgamento para as pessoas no caso de mensagens que passam por todas as verificações e ainda assim são enganosas.

### 7.3 Protocolos e julgamento

Whitten e Tygar (1999) mostraram, em seu estudo sobre criptografia de e-mail, que até um software de segurança bem projetado pode ser difícil demais para usuários comuns. Nadia tira uma lição: quando os protocolos deixam decisões para as pessoas, a interface precisa tornar fácil a decisão certa. Ela sugere que o sistema de e-mail da Ashcombe mostre uma etiqueta clara nas mensagens externas e um alerta quando um nome de exibição coincidir com o de um funcionário, mas o endereço for externo. Essas pistas apoiam o julgamento sem exigir que os funcionários entendam os protocolos por trás.

### Exemplo resolvido

Nadia explica os endereços de remetente forjados, descreve em linhas gerais as verificações de autenticação e sugere etiquetas de mensagem externa e alertas de nome coincidente.

> **Caso sintético.** Os exemplos são sintéticos; Whitten e Tygar (1999) é real.

### Erros e limites

As etiquetas passam a ser ignoradas se tudo for externo. As verificações dependem de configuração correta.

### Exercícios

- **EX019 — Remetente forjado.** Por que o remetente exibido pode ser forjado? *Rubrica:* 3 = o e-mail básico foi projetado para a cooperação, e não para a segurança;; 2 = projeto;; 1 = nada;; 0 = nenhuma.
- **EX020 — Limites das verificações.** O que as verificações de autenticação não conseguem impedir? *Rubrica:* 3 = domínios parecidos e contas comprometidas;; 2 = domínios parecidos;; 1 = nada;; 0 = nenhuma.
- **EX021 — Whitten e Tygar.** O que Whitten e Tygar (1999) mostraram? *Rubrica:* 3 = software de segurança pode ser difícil demais para usuários comuns;; 2 = usabilidade;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem

Você vai (1) escrever funções para calcular medidas de comportamento; (2) ler dados de arquivos CSV; (3) tratar erros e documentar o código.

### 8.1 Funções para medidas

Nadia reorganiza o código em funções. Uma função calcula a taxa de reporte de uma unidade; outra, a proporção de reportes genuínos. Funções tornam o código reutilizável e testável, já que cada uma pode ser conferida isoladamente. Ela lhes dá nomes claros e descrições curtas do que recebem e devolvem. Aprende que calcular uma taxa exige proteção contra divisão por zero, porque uma unidade nova pode ainda não ter registros de funcionários. Pequenas decisões como essa evitam erros que poderiam enganar os gestores que leem os resultados.

### 8.2 Ler arquivos CSV

A equipe de TI da Ashcombe fornece uma exportação sintética dos reportes como um arquivo de valores separados por vírgula. Nadia usa o módulo csv do Python, que trata corretamente campos entre aspas e vírgulas dentro do texto, ao contrário da simples divisão da linha. Ela lê cada linha num dicionário indexado pelo nome da coluna, para que o código continue correto mesmo que as colunas sejam reordenadas. Calcula as taxas de reporte por unidade e a proporção geral de ameaças genuínas. O laboratório imprime as taxas de cada unidade, e ela nota que as taxas variam muito entre unidades semelhantes.

### Laboratório — Taxas de reporte por unidade a partir de um arquivo CSV

```python
# Reporting rates per branch from a CSV (synthetic).
import csv, io
data = "branch,staff,reports,genuine\nCentral,30,14,3\nRiverside,24,10,4\nHill,15,6,1\nMarket,14,5,1\nOakfield,10,4,2\nMill,8,3,0\nQuay,5,3,1\nElm,6,2,0\nAbbey,8,1,0\nNew,,0,0\n"
def rate(r, s): return 100 * r / s if s else None
skipped = 0; rows = []
for row in csv.DictReader(io.StringIO(data)):
    if not row["staff"]: skipped += 1; continue
    rows.append((row["branch"], rate(int(row["reports"]), int(row["staff"]))))
for b, r in sorted(rows, key=lambda x: -x[1]): print(f"{b}: {r:.0f} per 100 staff")
print("skipped rows:", skipped)
```

Execute com `python3 lab_csv.py`. Saída verificada:

```text
Quay: 60 per 100 staff
Central: 47 per 100 staff
Riverside: 42 per 100 staff
Hill: 40 per 100 staff
Oakfield: 40 per 100 staff
Mill: 38 per 100 staff
Market: 36 per 100 staff
Elm: 33 per 100 staff
Abbey: 12 per 100 staff
skipped rows: 1
```

### 8.3 Erros e documentação

Nadia acrescenta tratamento de erros: linhas sem a contagem de funcionários são registradas e puladas, e o script informa quantas linhas pulou, para que nada fique escondido. Ela escreve um readme curto explicando o formato de entrada, as medidas e seus limites. A documentação importa porque outras pessoas podem reutilizar o script, e uma medida sem definição pode ser mal interpretada. O Dr. Prescott lembra que um bom código diz aos leitores o que pressupõe, o que faz parte da análise honesta tanto quanto da boa engenharia. Ela o mantém curto.

### Exemplo resolvido

Nadia escreve funções de medida com proteção contra zero, lê um CSV com o módulo csv e documenta as premissas e as linhas puladas.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Linhas puladas podem enviesar os resultados. As taxas de unidades pequenas são instáveis.

### Exercícios

- **EX022 — Proteção contra zero.** Por que se proteger contra divisão por zero? *Rubrica:* 3 = uma unidade pode não ter registros de funcionários;; 2 = unidade nova;; 1 = nada;; 0 = nenhuma.
- **EX023 — Maior taxa.** Que unidade teve a maior taxa de reporte no laboratório? *Rubrica:* 3 = Quay, com 60 por cem;; 2 = Quay;; 1 = Central;; 0 = nenhuma.
- **EX024 — Linhas puladas.** Por que informar o número de linhas puladas? *Rubrica:* 3 = para que nada fique escondido;; 2 = transparência;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Dados e bancos de dados

### Objetivos de aprendizagem

Você vai (1) desenhar uma tabela simples para reportes de segurança; (2) consultar dados com SQL; (3) aplicar a minimização de dados.

### 9.1 Desenhar uma tabela

Nadia desenha uma tabela de reportes com colunas para identificador do reporte, data, unidade, categoria e veredito. Deixa de fora, de propósito, o nome de quem reportou, porque a análise precisa apenas de contagens por unidade e dados pessoais criariam risco à privacidade. Cada coluna tem um tipo e regras, como o veredito ser malicioso, inofensivo ou desconhecido. Uma tabela bem desenhada dificulta os erros: um veredito digitado errado é rejeitado, em vez de ser contado silenciosamente como uma nova categoria que distorce os resultados. O responsável pela TI revisa o desenho e aprova as regras antes que qualquer dado seja carregado.

### 9.2 Consultar com SQL

Usando o módulo sqlite3, que já vem com o Python, Nadia carrega reportes sintéticos e escreve consultas. Uma conta os reportes por unidade, outra conta os reportes maliciosos por mês e uma terceira encontra as categorias mais comuns. O SQL expressa essas perguntas de forma compacta e deixa o banco de dados fazer o trabalho. O laboratório mostra que os e-mails com tema de fatura foram a categoria maliciosa mais comum. Ela aprende a ler os resultados das consultas com senso crítico, verificando se uma contagem alta reflete mais ataques ou simplesmente mais reportes numa unidade específica. Ela salva cada consulta com um comentário.

### Laboratório — Contagem de reportes com SQLite

```python
# Counting synthetic reports with SQLite.
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("create table reports(id integer primary key, month text, branch text, category text, verdict text check (verdict in ('malicious','harmless','unknown')))")
rows = [("2026-01", "Central", "invoice", "malicious")] * 5 + [("2026-02", "Riverside", "parcel", "malicious")] * 3 + \
       [("2026-02", "Hill", "account", "malicious")] * 2 + [("2026-03", "Central", "invoice", "malicious")] * 2 + [("2026-03", "Market", "newsletter", "harmless")] * 36
db.executemany("insert into reports(month,branch,category,verdict) values (?,?,?,?)", rows)
for r in db.execute("select category, count(*) from reports where verdict='malicious' group by category order by 2 desc"): print(r)
```

Execute com `python3 lab_sql.py`. Saída verificada:

```text
('invoice', 7)
('parcel', 3)
('account', 2)
```

### 9.3 Minimização de dados

Minimização de dados significa coletar apenas os dados necessários para uma finalidade. Nadia explica ao responsável pela TI da Ashcombe por que os nomes de quem reporta não devem ser guardados na tabela de análise: os nomes poderiam ser usados para julgar indivíduos, o que desestimularia os reportes, e acrescentam pouco às decisões do programa. Os reportes originais permanecem no sistema de e-mail, sob suas regras normais de retenção. O princípio liga a legislação de privacidade ao objetivo, próprio dos fatores humanos, de fazer as pessoas se sentirem seguras para reportar qualquer coisa que pareça estranha. O responsável pela TI concorda.

### Exemplo resolvido

Nadia desenha uma tabela de reportes sem nomes, a consulta com SQLite e defende a minimização de dados.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Remover os nomes impede alguns acompanhamentos. Os rótulos de categoria podem ser inconsistentes.

### Exercícios

- **EX025 — Nome excluído.** Por que a tabela exclui os nomes de quem reporta? *Rubrica:* 3 = a análise precisa apenas de contagens por unidade e os nomes criam risco;; 2 = minimização;; 1 = nada;; 0 = nenhuma.
- **EX026 — Categoria no topo.** Que categoria maliciosa foi a mais comum no laboratório? *Rubrica:* 3 = fatura;; 2 = faturas;; 1 = encomenda;; 0 = nenhuma.
- **EX027 — Efeito do reporte.** O que Nadia deve verificar quando a contagem de uma unidade é alta? *Rubrica:* 3 = se reflete mais ataques ou mais reportes;; 2 = reportes;; 1 = nada;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e prática autorizada

### Objetivos de aprendizagem

Você vai (1) aplicar princípios éticos à pesquisa em fatores humanos; (2) explicar por que o engano exige salvaguardas especiais; (3) descrever regras éticas para simulações de phishing.

### 10.1 Princípios éticos

A pesquisa com pessoas deve respeitar a autonomia, evitar danos e tratar as pessoas com justiça. Nadia aprende que sua universidade exige aprovação ética para qualquer estudo que envolva funcionários, incluindo questionários e entrevistas. Os participantes devem saber o que o estudo envolve, concordar livremente e poder desistir. Os dados devem ser protegidos e os resultados relatados sem identificar indivíduos. Esses princípios valem até para pequenos projetos de estudantes, porque uma pergunta descuidada ou um comentário vazado pode prejudicar o emprego de alguém ou suas relações com os colegas. Ela conclui o módulo de ética antes de começar qualquer trabalho de campo.

### 10.2 Salvaguardas contra o engano

Alguns exercícios de segurança envolvem engano, como e-mails de phishing simulados. O engano conflita com o consentimento informado, por isso precisa de forte justificativa e de salvaguardas. Nadia aprende que os comitês de ética costumam exigir que o engano seja necessário, que o dano seja mínimo, que os participantes sejam informados depois e que possam retirar seus dados. Nas organizações, os representantes dos funcionários devem concordar com o programa. Ela observa que o engano pode prejudicar a confiança, que é em si um ativo de segurança, por isso deve ser usado com parcimônia e cuidado. Ela registra essa visão.

### 10.3 Regras para simulações

Nadia rascunha regras para qualquer simulação futura na Ashcombe: anunciar que existe um programa; acordar os modelos com os representantes dos funcionários; evitar iscas que explorem sofrimento pessoal, como salário ou saúde; dar retorno imediato e gentil; relatar apenas resultados agregados; e nunca usar os resultados para punição. Lain, Kostiainen e Čapkun (2022) constataram que algumas práticas comuns, como longas páginas de treinamento depois de um clique, não ajudavam. As regras buscam fazer das simulações uma ferramenta de aprendizagem que respeita os funcionários, e não uma armadilha que mina a confiança deles.

### Exemplo resolvido

Nadia aplica a ética de pesquisa, explica as salvaguardas contra o engano e rascunha seis regras para simulações éticas.

> **Caso sintético.** As regras são orientações sintéticas; Lain et al. (2022) é real.

### Erros e limites

As regras podem ser ignoradas sob pressão. Organizações pequenas podem não ter representantes dos funcionários.

### Exercícios

- **EX028 — Direitos dos participantes.** O que os participantes devem poder fazer? *Rubrica:* 3 = saber, concordar livremente e desistir;; 2 = consentimento;; 1 = nada;; 0 = nenhuma.
- **EX029 — A confiança como ativo.** Por que o engano deve ser usado com parcimônia? *Rubrica:* 3 = pode prejudicar a confiança, que é um ativo de segurança;; 2 = confiança;; 1 = nada;; 0 = nenhuma.
- **EX030 — Tipo de isca proibido.** Que iscas as regras proíbem? *Rubrica:* 3 = as que exploram sofrimento pessoal, como salário ou saúde;; 2 = sofrimento;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Nadia Farouk, o Dr. Owen Prescott, a Fenmoor University, a Ashcombe Community Library Network, a Dunmore Libraries e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** 40 reportes por cem funcionários, já que 48 dividido por 120 dá 0,4.

**EX002.** Cerca de 98% dos e-mails sinalizados eram inofensivos.

**EX003.** 140%, porque o aumento de 28 equivale a 1,4 vez os 20 iniciais.

**EX004.** Porque os funcionários podem deixar os computadores do balcão logados enquanto atendem, o que contorna a política.

**EX005.** Que os usuários não são o inimigo, mas têm dificuldade com mecanismos que não se encaixam em seu trabalho.

**EX006.** Um bloqueio automático curto com desbloqueio por cartão de aproximação.

**EX007.** Ele associa o nome de cada unidade à sua contagem.

**EX008.** Central, com 14 reportes.

**EX009.** Pula a linha e imprime um aviso.

**EX010.** Que muitas violações de fato envolvem ações humanas.

**EX011.** Que a segurança deve ser projetada em torno das capacidades humanas.

**EX012.** Porque o número do elemento humano combina erros, uso indevido e engenharia social.

**EX013.** Conscientização, treinamento e educação.

**EX014.** Usar uma história inventada e crível para convencer alguém a agir.

**EX015.** Porque supõem que saber leva a fazer, ignorando a carga de trabalho e o esforço.

**EX016.** A união de gestores e pessoal de TI.

**EX017.** Onze funcionários, todos nas unidades Quay e Elm.

**EX018.** Um segundo visitante poderia se sentar e herdar a sessão aberta do primeiro.

**EX019.** Porque o protocolo básico de e-mail foi projetado para a cooperação e não verifica o remetente exibido.

**EX020.** Domínios parecidos e mensagens de contas legítimas comprometidas.

**EX021.** Que até um software de segurança bem projetado, como a criptografia de e-mail, pode ser difícil demais para usuários comuns.

**EX022.** Porque uma unidade nova pode ainda não ter registros de funcionários.

**EX023.** Quay, com 60 reportes por cem funcionários.

**EX024.** Para que os leitores saibam que dados foram excluídos e nada fique escondido.

**EX025.** Porque a análise precisa apenas de contagens por unidade, e os nomes criariam risco à privacidade.

**EX026.** E-mails com tema de fatura.

**EX027.** Se ela reflete mais ataques ou simplesmente mais reportes.

**EX028.** Saber o que o estudo envolve, concordar livremente e desistir.

**EX029.** Porque pode prejudicar a confiança, que por si só sustenta a segurança.

**EX030.** Iscas que exploram sofrimento pessoal, como salário ou saúde.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Ajzen, I. (1991). The theory of planned behavior. *Organizational Behavior and Human Decision Processes*, 50(2), 179–211. <https://doi.org/10.1016/0749-5978(91)90020-T>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Beautement, A., Sasse, M. A., & Wonham, M. (2008). The compliance budget: Managing security behaviour in organisations. *Proceedings of the 2008 New Security Paradigms Workshop*, 47–58. <https://doi.org/10.1145/1595676.1595684>
- Cialdini, R. B. (2021). *Influence, new and expanded: The psychology of persuasion*. Harper Business.
- Dawkins, S., & Jacobs, J. (2023). *NIST Phish Scale user guide* (NIST TN 2276). NIST. <https://doi.org/10.6028/NIST.TN.2276>
- European Union Agency for Cybersecurity. (2019). *Cybersecurity culture guidelines: Behavioural aspects of cybersecurity*. ENISA. <https://www.enisa.europa.eu/publications/cybersecurity-culture-guidelines-behavioural-aspects-of-cybersecurity>
- Hadnagy, C. (2018). *Social engineering: The science of human hacking* (2nd ed.). Wiley.
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- Lain, D., Kostiainen, K., & Čapkun, S. (2022). Phishing in organizations: Findings from a large-scale and long-term study. *2022 IEEE Symposium on Security and Privacy*, 842–859. <https://doi.org/10.1109/SP46214.2022.9833766>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
- Verizon Business. (2024). *2024 Data breach investigations report*. Verizon. <https://www.verizon.com/business/resources/reports/dbir/>
- Whitten, A., & Tygar, J. D. (1999). Why Johnny can't encrypt: A usability evaluation of PGP 5.0. *Proceedings of the 8th USENIX Security Symposium*. USENIX. <https://www.usenix.org/conference/8th-usenix-security-symposium/why-johnny-cant-encrypt-usability-evaluation-pgp-50>
- Wilson, M., de Zafra, D. E., Pitcher, S. I., Tressler, J. D., & Ippolito, J. B. (1998). *Information technology security training requirements: A role- and performance-based model* (NIST SP 800-16). NIST. <https://doi.org/10.6028/NIST.SP.800-16>
