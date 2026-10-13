# Fatores Humanos e Política Cibernética: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 098, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–40 de 40 têm texto didático escrito à mão; os exercícios EX001–EX120 têm resoluções correspondentes com rubricas de 0 a 3; os quinze laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

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

### Síntese

Razões, taxas de base e aritmética conferida são as primeiras ferramentas para raciocinar sobre o comportamento de segurança.

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

- **EX004 — Interação mais fraca.** Por que uma política forte de senhas pouco importa em um caso? *Rubrica:* 3 = se os computadores do balcão ficam logados;; 2 = logados;; 1 = vago;; 0 = nenhuma.
- **EX005 — Adams e Sasse.** O que Adams e Sasse (1999) mostraram sobre os usuários? *Rubrica:* 3 = não são o inimigo e têm dificuldade com mecanismos que não se encaixam;; 2 = encaixe;; 1 = descuidados;; 0 = nenhuma.
- **EX006 — Correção sugerida.** Que correção Nadia sugeriu para as telas desbloqueadas? *Rubrica:* 3 = bloqueio automático curto com desbloqueio por cartão de aproximação;; 2 = cartão de aproximação;; 1 = senhas mais longas;; 0 = nenhuma.

### Síntese

A segurança vive nos pontos em que as pessoas interagem com os sistemas, e o encaixe com o trabalho é o que mais importa.

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
- **EX008 — Unidade no topo.** Que unidade mais reportou no laboratório? *Rubrica:* 3 = Central, com 14;; 2 = Central;; 1 = vago;; 0 = nenhuma.
- **EX009 — Linhas quebradas.** Como o script trata uma linha com um campo faltando? *Rubrica:* 3 = pula a linha com um aviso;; 2 = pula;; 1 = trava;; 0 = nenhuma.

### Síntese

Scripts simples e testados transformam registros em contagens que levantam perguntas úteis.

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

- **EX010 — Contra-argumento.** Que contra-argumento Nadia precisa enfrentar? *Rubrica:* 3 = muitas violações envolvem ações humanas;; 2 = elemento humano;; 1 = vago;; 0 = nenhuma.
- **EX011 — Sasse et al.** O que Sasse, Brostoff e Weirich (2001) argumentaram? *Rubrica:* 3 = a segurança deve ser projetada em torno das capacidades humanas;; 2 = design;; 1 = os usuários são descuidados;; 0 = nenhuma.
- **EX012 — Cautela com o DBIR.** Por que o número do DBIR não mostra que os funcionários são descuidados? *Rubrica:* 3 = combina erros, uso indevido e engenharia social;; 2 = combinado;; 1 = vago;; 0 = nenhuma.

### Síntese

A escrita acadêmica estrutura afirmações, cita com precisão e mantém a evidência separada da opinião.

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

- **EX013 — Três níveis.** Que três níveis a SP 800-16 distinguiu? *Rubrica:* 3 = conscientização, treinamento e educação;; 2 = três;; 1 = vago;; 0 = nenhuma.
- **EX014 — Pretexting.** O que é pretexting? *Rubrica:* 3 = inventar uma história crível para enganar;; 2 = história;; 1 = phishing;; 0 = nenhuma.
- **EX015 — Falha das campanhas.** Por que as campanhas muitas vezes falham, segundo Bada et al. (2019)? *Rubrica:* 3 = supõem que o conhecimento leva ao comportamento;; 2 = suposição;; 1 = vago;; 0 = nenhuma.

### Síntese

O letramento em segurança abrange conscientização, táticas e a distância entre saber e fazer.

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
- **EX017 — Funcionários inalcançáveis.** Quantos funcionários não alcançavam a TI no laboratório? *Rubrica:* 3 = 11, em Quay e Elm;; 2 = 11;; 1 = vago;; 0 = nenhuma.
- **EX018 — Lacuna da sessão.** Que lacuna o teste lógico revelou? *Rubrica:* 3 = um novo visitante herda uma sessão aberta;; 2 = herdar;; 1 = vago;; 0 = nenhuma.

### Síntese

Conjuntos, grafos e lógica expõem as diferenças entre as regras e rotas pretendidas e as reais.

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

- **EX019 — Remetente forjado.** Por que o remetente exibido pode ser forjado? *Rubrica:* 3 = o e-mail básico foi projetado para a cooperação, e não para a segurança;; 2 = projeto;; 1 = vago;; 0 = nenhuma.
- **EX020 — Limites das verificações.** O que as verificações de autenticação não conseguem impedir? *Rubrica:* 3 = domínios parecidos e contas comprometidas;; 2 = domínios parecidos;; 1 = vago;; 0 = nenhuma.
- **EX021 — Whitten e Tygar.** O que Whitten e Tygar (1999) mostraram? *Rubrica:* 3 = software de segurança pode ser difícil demais para usuários comuns;; 2 = usabilidade;; 1 = vago;; 0 = nenhuma.

### Síntese

Os limites dos protocolos deixam o julgamento para as pessoas; por isso, as interfaces precisam apoiá-lo.

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

- **EX022 — Proteção contra zero.** Por que se proteger contra divisão por zero? *Rubrica:* 3 = uma unidade pode não ter registros de funcionários;; 2 = unidade nova;; 1 = vago;; 0 = nenhuma.
- **EX023 — Maior taxa.** Que unidade teve a maior taxa de reporte no laboratório? *Rubrica:* 3 = Quay, com 60 por cem;; 2 = Quay;; 1 = Central;; 0 = nenhuma.
- **EX024 — Linhas puladas.** Por que informar o número de linhas puladas? *Rubrica:* 3 = para que nada fique escondido;; 2 = transparência;; 1 = vago;; 0 = nenhuma.

### Síntese

Funções, leitura correta de CSV e premissas documentadas tornam as medidas confiáveis.

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

- **EX025 — Nome excluído.** Por que a tabela exclui os nomes de quem reporta? *Rubrica:* 3 = a análise precisa apenas de contagens por unidade e os nomes criam risco;; 2 = minimização;; 1 = vago;; 0 = nenhuma.
- **EX026 — Categoria no topo.** Que categoria maliciosa foi a mais comum no laboratório? *Rubrica:* 3 = fatura;; 2 = faturas;; 1 = encomenda;; 0 = nenhuma.
- **EX027 — Efeito do reporte.** O que Nadia deve verificar quando a contagem de uma unidade é alta? *Rubrica:* 3 = se reflete mais ataques ou mais reportes;; 2 = reportes;; 1 = vago;; 0 = nenhuma.

### Síntese

Tabelas bem desenhadas, consultas simples e dados minimizados sustentam uma análise segura.

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

- **EX028 — Direitos dos participantes.** O que os participantes devem poder fazer? *Rubrica:* 3 = saber, concordar livremente e desistir;; 2 = consentimento;; 1 = vago;; 0 = nenhuma.
- **EX029 — A confiança como ativo.** Por que o engano deve ser usado com parcimônia? *Rubrica:* 3 = pode prejudicar a confiança, que é um ativo de segurança;; 2 = confiança;; 1 = vago;; 0 = nenhuma.
- **EX030 — Tipo de isca proibido.** Que iscas as regras proíbem? *Rubrica:* 3 = as que exploram sofrimento pessoal, como salário ou saúde;; 2 = sofrimento;; 1 = vago;; 0 = nenhuma.

### Síntese

A prática ética exige consentimento, salvaguardas para o uso de engano e regras de simulação respeitosas.

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) explicar contas, permissões e atualizações num sistema operacional; (2) descrever como os avisos de atualização afetam os usuários; (3) propor configurações que reduzam o ônus para o usuário.

### 11.1 Contas e permissões

Um sistema operacional gerencia contas e controla o que cada conta pode fazer. Na Ashcombe, os computadores do balcão usam contas compartilhadas, o que torna impossível saber quem fez o quê. Os notebooks dos escritórios dão aos funcionários direitos de administrador para que possam instalar drivers de impressora, o que também permite que um malware se instale. Nadia aprende que separar contas comuns e de administrador limita os danos de erros e ataques. Ela recomenda contas nominais com login por cartão de aproximação nos balcões e a remoção dos direitos de administrador de rotina, com a TI instalando os drivers de forma centralizada, em vez de depender de cada pessoa.

### 11.2 Avisos de atualização

Os sistemas operacionais pedem aos usuários que reiniciem para aplicar atualizações. Os funcionários da Ashcombe adiam as reinicializações porque elas chegam em horários movimentados e levam vários minutos. Nadia constata que alguns notebooks adiam atualizações há mais de um mês, deixando sem correção fraquezas conhecidas. Ela liga isso à ideia de orçamento de compliance de Beautement, Sasse e Wonham (2008): as pessoas têm disposição limitada para gastar esforço com segurança, e quando os avisos chegam em maus momentos, são adiados. Culpar os funcionários pelo adiamento ignoraria o problema de horário embutido no próprio sistema.

### 11.3 Reduzir o ônus

Nadia propõe que as atualizações sejam instaladas automaticamente durante a noite, quando as bibliotecas estão fechadas, com os notebooks deixados carregando nos escritórios. As reinicializações durante o horário de funcionamento passam a ser raras. Ela também sugere que a TI monitore a situação das atualizações de forma centralizada, para que ninguém precise se lembrar. A mudança transfere o esforço dos indivíduos para o sistema, que é mais confiável. O Dr. Prescott observa que esse é um tema recorrente em fatores humanos: quando um comportamento seguro depende de muitas pessoas se lembrarem, projete o sistema para fazê-lo por elas sempre que possível.

### Exemplo resolvido

Nadia recomenda contas nominais e a remoção dos direitos de administrador de rotina, liga os adiamentos de atualização ao orçamento de compliance e propõe atualizações noturnas.

> **Caso sintético.** As configurações são sintéticas; Beautement et al. (2008) é real.

### Erros e limites

Atualizações noturnas falham se os dispositivos estiverem desligados. Remover direitos de administrador aumenta a carga da TI.

### Exercícios

- **EX031 — Problema da conta compartilhada.** Qual é o problema das contas compartilhadas do balcão? *Rubrica:* 3 = ninguém consegue saber quem fez o quê;; 2 = responsabilização;; 1 = vago;; 0 = nenhuma.
- **EX032 — Orçamento de compliance.** O que o orçamento de compliance descreve? *Rubrica:* 3 = disposição limitada para gastar esforço com segurança;; 2 = esforço;; 1 = vago;; 0 = nenhuma.
- **EX033 — Transferência do ônus.** Para onde Nadia transfere o esforço das atualizações? *Rubrica:* 3 = dos indivíduos para o sistema;; 2 = sistema;; 1 = usuários;; 0 = nenhuma.

### Síntese

As configurações do sistema operacional podem transferir o esforço de segurança das pessoas para os sistemas.

<a id="ch-12"></a>

## Capítulo 12 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) estimar uma proporção com um intervalo de confiança; (2) comparar duas proporções com cautela; (3) explicar por que amostras pequenas enganam.

### 12.1 Proporções e intervalos

A Ashcombe conduziu uma simulação anunciada e acordada com os funcionários, na qual 120 funcionários receberam um e-mail de prática. Destes, 18 o reportaram em até uma hora. A proporção que reportou é de 15%. Nadia aprende que um número isolado esconde a incerteza, por isso calcula um intervalo de confiança de 95% pelo método de Wilson, que se comporta bem com contagens pequenas. O intervalo mostra a faixa de taxas compatíveis com os dados. Ela relata a taxa junto com seu intervalo, para que os gestores não tratem uma estimativa isolada como exata. O intervalo vai de 9,7% a 22,5%.

### Laboratório — Intervalo de Wilson para uma proporção de reportes

```python
# Wilson 95% interval for reporting proportions (synthetic).
from math import sqrt
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h
for name, k, n in (("all staff", 18, 120), ("Central", 6, 30), ("Riverside", 3, 24)):
    lo, hi = wilson(k, n); print(f"{name}: {k}/{n} = {k / n:.1%}, 95% CI {lo:.1%} to {hi:.1%}")
```

Execute com `python3 lab_ci.py`. Saída verificada:

```text
all staff: 18/120 = 15.0%, 95% CI 9.7% to 22.5%
Central: 6/30 = 20.0%, 95% CI 9.5% to 37.3%
Riverside: 3/24 = 12.5%, 95% CI 4.3% to 31.0%
```

### 12.2 Comparar proporções

Duas unidades mostram taxas de reporte diferentes: Central, 6 de 30 (20%, intervalo de 9,5% a 37,3%), e Riverside, 3 de 24 (12,5%, intervalo de 4,3% a 31,0%). Nadia as compara e descobre que os intervalos se sobrepõem bastante. A diferença aparente poderia facilmente surgir por acaso. Ela resiste à tentação de elogiar uma unidade e criticar a outra. Comparar grupos de forma justa exige atenção ao tamanho da amostra e, no trabalho de fatores humanos, também exige cuidado, porque comparações públicas entre equipes podem criar pressão e ressentimento que prejudicam a cultura de reporte que o programa busca construir.

### 12.3 Amostras pequenas

Em unidades pequenas, a ação de uma única pessoa muda muito a taxa. Em Quay, com cinco funcionários, um reporte a mais move a taxa em vinte pontos. Nadia explica isso aos gestores usando a saída do laboratório e sugere relatar os resultados por unidade apenas quando incluírem pelo menos vinte funcionários, ou combinar unidades pequenas. Essa regra protege tanto a precisão dos números quanto a privacidade dos funcionários de equipes pequenas, em que as ações individuais poderiam, de outro modo, ser deduzidas de uma taxa do grupo. Os gestores aceitam a regra.

### Exemplo resolvido

Nadia calcula um intervalo de Wilson para 18 de 120, compara duas unidades com cautela e define um tamanho mínimo de grupo de vinte.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Os intervalos supõem respostas independentes. Uma simulação é um retrato único.

### Exercícios

- **EX034 — Intervalo geral.** Qual foi o intervalo de 95% para 18 de 120? *Rubrica:* 3 = cerca de 9,7% a 22,5%;; 2 = faixa;; 1 = exatamente 15%;; 0 = nenhuma.
- **EX035 — Comparação entre unidades.** Por que não elogiar Central em detrimento de Riverside? *Rubrica:* 3 = os intervalos se sobrepõem bastante;; 2 = acaso;; 1 = vago;; 0 = nenhuma.
- **EX036 — Grupo mínimo.** Que tamanho mínimo de grupo Nadia sugeriu? *Rubrica:* 3 = vinte funcionários;; 2 = 20;; 1 = cinco;; 0 = nenhuma.

### Síntese

As proporções precisam de intervalos, as comparações precisam de cuidado e os grupos pequenos precisam de proteção.

<a id="ch-13"></a>

## Capítulo 13 — Identidade e acesso

### Objetivos de aprendizagem

Você vai (1) explicar os fatores de autenticação; (2) avaliar políticas de senha com evidências de fatores humanos; (3) recomendar uma autenticação usável.

### 13.1 Fatores de autenticação

A autenticação verifica se alguém é quem diz ser, usando algo que a pessoa sabe, como uma senha; algo que ela tem, como um cartão ou uma chave de segurança; ou algo que ela é, como uma impressão digital. Combinar fatores torna as senhas roubadas menos úteis. Nadia observa que a Ashcombe usa apenas senhas no sistema de gestão da biblioteca, que guarda os endereços dos usuários. Um e-mail de phishing que capturasse uma senha daria acesso total, de modo que acrescentar um segundo fator reduziria o dano que uma única pessoa enganada poderia causar.

### 13.2 Políticas de senha

A Ashcombe exige que os funcionários troquem as senhas a cada sessenta dias, com regras complexas. Adams e Sasse (1999) constataram que regras assim levam as pessoas a anotar as senhas ou a usar padrões previsíveis, porque memorizar muitas senhas que mudam é difícil. Nadia aplica um questionário anônimo a um pequeno grupo de colegas e descobre que a maioria acrescenta um número à senha antiga a cada troca. Ela recomenda acabar com as trocas periódicas forçadas, a menos que haja evidência de comprometimento, e permitir frases-senha mais longas, que são mais fáceis de lembrar e mais difíceis de adivinhar.

### 13.3 Autenticação usável

Nadia compara opções de segundo fator: códigos por SMS, um aplicativo autenticador em celulares pessoais e chaves de segurança. Nem todos os atendentes de balcão têm celular do trabalho, e alguns preferem não usar o celular pessoal para o trabalho. As chaves de segurança funcionam sem celular e resistem ao phishing porque verificam o site. Ela recomenda chaves para os funcionários que acessam dados de usuários, com um processo simples de contingência. Sua recomendação equilibra segurança, custo e a situação prática dos funcionários, algo que ela aprendeu a ponderar nos capítulos anteriores.

### Exemplo resolvido

Nadia explica os fatores, liga as trocas forçadas a senhas fracas e recomenda frases-senha e chaves de segurança.

> **Caso sintético.** O questionário é sintético; Adams e Sasse (1999) é real.

### Erros e limites

Chaves podem ser perdidas. Acabar com as trocas forçadas exige detecção de comprometimento.

### Exercícios

- **EX037 — Três tipos de fator.** Quais são os três tipos de fator? *Rubrica:* 3 = saber, ter, ser;; 2 = três;; 1 = vago;; 0 = nenhuma.
- **EX038 — Efeito da troca forçada.** O que Nadia descobriu que os funcionários fazem nas trocas forçadas? *Rubrica:* 3 = acrescentam um número à senha antiga;; 2 = padrão;; 1 = vago;; 0 = nenhuma.
- **EX039 — Vantagem da chave.** Por que as chaves de segurança resistem ao phishing? *Rubrica:* 3 = verificam o site;; 2 = verificação do site;; 1 = são longas;; 0 = nenhuma.

### Síntese

A autenticação utilizável combina fatores de formas que convêm à equipe e resistem ao engano.

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos de privacidade

### Objetivos de aprendizagem

Você vai (1) explicar os princípios centrais de privacidade; (2) aplicá-los aos dados dos usuários de uma biblioteca; (3) ligar a privacidade à confiança dos funcionários nos programas de segurança.

### 14.1 Princípios de privacidade

Os princípios de privacidade incluem a limitação da finalidade, ou seja, coletar dados apenas para finalidades declaradas; a minimização de dados; a exatidão; a limitação do armazenamento; e a segurança do tratamento. As bibliotecas guardam informações sensíveis sobre o que as pessoas leem, por isso têm uma forte tradição de proteger a privacidade dos usuários. Nadia aprende que privacidade e segurança se sobrepõem, mas diferem: a segurança protege os dados contra acesso não autorizado, enquanto a privacidade também limita o que as pessoas autorizadas fazem com eles. Um sistema pode ser seguro e ainda assim usar mal os dados, se coletar ou compartilhar mais do que o necessário. Nadia lê a política de privacidade da biblioteca.

### 14.2 Dados dos usuários

Nadia revisa como a Ashcombe trata os pedidos de dados de usuários. Às vezes, quem liga pergunta se uma pessoa é usuária ou o que ela tomou emprestado. Os funcionários são treinados para recusar, mas quem diz ser da polícia ou parente pode ser persuasivo, usando a autoridade e a urgência descritas por Cialdini. Nadia propõe um procedimento escrito: nunca revelar informações de usuários por telefone; encaminhar os pedidos formais ao encarregado de privacidade, por escrito. Isso elimina a necessidade de os atendentes julgarem a credibilidade sob pressão, o que protege tanto os usuários quanto os funcionários.

### 14.3 Privacidade e confiança dos funcionários

Os programas de segurança também coletam dados sobre os funcionários, como quem reportou ou clicou. Se os funcionários acreditarem que esses dados serão usados contra eles, podem parar de reportar. Nadia argumenta que os mesmos princípios de privacidade devem valer para os dados dos funcionários: coletar apenas o necessário, relatar agregados e não usar os resultados das simulações para punição. Respeitar a privacidade dos funcionários constrói a confiança que faz as pessoas admitirem erros rapidamente, o que muitas vezes é o comportamento de segurança mais valioso depois de um incidente. Os gestores discutem a proposta.

### Exemplo resolvido

Nadia explica os princípios de privacidade, escreve um procedimento de não revelação por telefone e aplica a privacidade aos dados de segurança dos funcionários.

> **Caso sintético.** O procedimento é sintético; Cialdini (2021) é real.

### Erros e limites

Os procedimentos podem atrasar pedidos urgentes legítimos. Agregados ainda podem revelar indivíduos em grupos pequenos.

### Exercícios

- **EX040 — Privacidade versus segurança.** Em que a privacidade difere da segurança? *Rubrica:* 3 = a privacidade também limita o que as pessoas autorizadas fazem com os dados;; 2 = limites de uso;; 1 = vago;; 0 = nenhuma.
- **EX041 — Procedimento telefônico.** O que o novo procedimento exige? *Rubrica:* 3 = nenhuma revelação por telefone e pedidos por escrito ao encarregado de privacidade;; 2 = por escrito;; 1 = vago;; 0 = nenhuma.
- **EX042 — Dados dos funcionários.** Por que aplicar princípios de privacidade aos dados dos funcionários? *Rubrica:* 3 = para manter a confiança que sustenta os reportes;; 2 = confiança;; 1 = vago;; 0 = nenhuma.

### Síntese

A privacidade protege associados e equipe, e os procedimentos tiram a pressão de quem atende no balcão.

<a id="ch-15"></a>

## Capítulo 15 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) escolher medidas válidas de comportamento de segurança; (2) distinguir produtos de resultados; (3) medir sem prejudicar a confiança.

### 15.1 Medidas válidas

Uma medida é válida se captura o que diz capturar. As taxas de conclusão de cursos mostram que as pessoas clicaram até o fim de um módulo, e não que se comportam com segurança. As taxas de clique em simulações dependem muito da dificuldade do e-mail, que a NIST Phish Scale (Dawkins e Jacobs, 2023) ajuda a classificar. Nadia lista medidas candidatas para a Ashcombe e julga a validade de cada uma. As taxas de reporte de e-mails suspeitos reais e o tempo até o primeiro reporte estão mais perto do que importa: a rapidez com que a organização fica sabendo de um ataque.

### 15.2 Produtos e resultados

Produtos são o que o programa entrega, como vídeos exibidos ou e-mails enviados. Resultados são mudanças no mundo, como menos fraudes bem-sucedidas ou reportes mais rápidos. Nadia classifica os números atuais da Ashcombe e descobre que todos são produtos. Ela propõe duas medidas de resultado: a mediana do tempo entre a chegada de um e-mail malicioso e o primeiro reporte, e o número de pedidos de pagamento fraudulentos barrados. O laboratório calcula a mediana do tempo a partir de um mês sintético de dados, mostrando como um resultado pode ser calculado a partir de registros já existentes.

### Laboratório — Mediana do tempo até o primeiro reporte

```python
# Median minutes from arrival to first report for a month of malicious emails (synthetic).
times = [4, 7, 9, 11, 12, 14, 15, 22, 30, 41, 65]
s = sorted(times); print("emails:", len(s), "median:", s[len(s) // 2], "min")
```

Execute com `python3 lab_median.py`. Saída verificada:

```text
emails: 11 median: 14 min
```

### 15.3 Medir com respeito

A medição pode prejudicar a confiança se os funcionários se sentirem vigiados. Nadia propõe que os resultados sejam relatados por grupos de unidades com vinte ou mais pessoas, que os dados individuais não sejam mostrados aos gestores e que os funcionários vejam o mesmo resumo que o conselho. Ela também propõe perguntar aos funcionários, a cada poucos meses, quanto esforço a segurança exige. Medir o ônus junto com os resultados lembra aos líderes que o esforço de segurança tem um custo, e que um programa que melhora os resultados à custa de esgotar os funcionários dificilmente vai durar. Os representantes dos funcionários revisam a proposta.

### Exemplo resolvido

Nadia julga a validade das medidas, separa produtos de resultados, calcula uma mediana do tempo de reporte e propõe uma medição respeitosa.

> **Caso sintético.** Os dados são sintéticos; Dawkins e Jacobs (2023) é real.

### Erros e limites

As medidas de resultado podem ser ruidosas. Ataques não reportados são invisíveis.

### Exercícios

- **EX043 — Validade da conclusão.** Por que as taxas de conclusão são medidas fracas? *Rubrica:* 3 = mostram que se clicou até o fim, e não o comportamento;; 2 = validade;; 1 = vago;; 0 = nenhuma.
- **EX044 — Resultado da mediana.** Qual foi a mediana do tempo até o primeiro reporte no laboratório? *Rubrica:* 3 = 14 minutos;; 2 = 14;; 1 = vago;; 0 = nenhuma.
- **EX045 — Medida de ônus.** Por que medir também o esforço dos funcionários? *Rubrica:* 3 = o esforço é um custo real que afeta a sustentabilidade;; 2 = custo;; 1 = vago;; 0 = nenhuma.

### Síntese

Medidas de resultado válidas, coletadas com respeito, mostram se um programa ajuda.

<a id="ch-16"></a>

## Capítulo 16 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) descrever defesas em camadas; (2) situar os papéis humanos dentro de uma arquitetura; (3) projetar para que um único erro humano não seja catastrófico.

### 16.1 Defesas em camadas

A arquitetura de segurança organiza os controles de modo que várias camadas protejam cada ativo. No banco de dados de usuários da Ashcombe, as camadas incluem filtragem de e-mail, autenticação com segundo fator, direitos de acesso limitados, monitoramento e backups. Nenhuma camada é perfeita, mas juntas reduzem a chance de que uma única falha leve a um dano. Saltzer e Schroeder (1975) descreveram princípios como o menor privilégio e a aceitabilidade psicológica, que significa que a proteção deve ser fácil de usar corretamente. Nadia percebe que esses princípios ligam a arquitetura diretamente aos fatores humanos.

### 16.2 Papéis humanos

Nadia marca onde as pessoas atuam dentro da arquitetura: os funcionários decidem se abrem e-mails, os gestores aprovam acessos, o pessoal de TI revisa alertas e os usuários escolhem senhas para as contas online. Cada papel humano é ao mesmo tempo uma fraqueza potencial e uma força potencial. Funcionários que reportam e-mails suspeitos atuam como sensores que detectam ataques que os filtros deixam passar. Ela rotula cada papel com o apoio de que precisa, como ferramentas claras, treinamento ou tempo. Uma arquitetura que ignora os papéis humanos supõe que as pessoas se comportarão de forma perfeita, o que nunca acontece na prática.

### 16.3 Tolerar o erro

Nadia projeta a arquitetura da Ashcombe para que um único erro não leve ao desastre. Se um funcionário digitar a senha num site falso, o segundo fator bloqueia o atacante. Se alguém abrir um malware, os direitos limitados impedem que ele se espalhe e os backups permitem a recuperação. Se alguém enviar dados de usuários ao endereço errado, os alertas sobre exportações em massa ajudam a detectar o problema. Ela chama isso de tolerar o erro, o que reflete a visão de que as pessoas às vezes vão errar, de modo que os sistemas devem absorver os erros, em vez de depender da perfeição.

### Exemplo resolvido

Nadia organiza defesas em camadas, mapeia os papéis humanos e projeta a arquitetura para tolerar erros individuais.

> **Caso sintético.** A arquitetura é sintética; Saltzer e Schroeder (1975) é real.

### Erros e limites

As camadas acrescentam custo e complexidade. Os alertas precisam de pessoas para responder a eles.

### Exercícios

- **EX046 — Princípio da aceitabilidade.** O que significa aceitabilidade psicológica? *Rubrica:* 3 = a proteção deve ser fácil de usar corretamente;; 2 = usabilidade;; 1 = vago;; 0 = nenhuma.
- **EX047 — Funcionários como sensores.** Como os funcionários podem fortalecer a arquitetura? *Rubrica:* 3 = reportando ataques que os filtros deixam passar;; 2 = sensores;; 1 = vago;; 0 = nenhuma.
- **EX048 — Defesa contra site falso.** O que bloqueia um atacante depois que uma senha é digitada num site falso? *Rubrica:* 3 = o segundo fator;; 2 = fator;; 1 = backups;; 0 = nenhuma.

### Síntese

A arquitetura em camadas posiciona as pessoas de forma deliberada e absorve os seus erros inevitáveis.

<a id="ch-17"></a>

## Capítulo 17 — Conceitos de criptografia

### Objetivos de aprendizagem

Você vai (1) explicar criptografia e assinaturas em termos simples; (2) descrever os problemas de usabilidade das ferramentas criptográficas; (3) recomendar onde a criptografia deve ser invisível.

### 17.1 Criptografia e assinaturas

A criptografia embaralha os dados para que só quem tem a chave certa consiga lê-los. As assinaturas digitais permitem ao destinatário verificar quem enviou uma mensagem e que ela não foi alterada. Nadia aprende essas ideias em termos simples, o suficiente para entender seus papéis. As conexões web com o catálogo da biblioteca são criptografadas automaticamente, de modo que os usuários não precisam fazer nada. Assinaturas de e-mail poderiam ajudar os funcionários a confiar nas mensagens internas, mas apenas se verificá-las fosse simples. O valor da criptografia depende muito de quanto ela exige das pessoas.

### 17.2 Problemas de usabilidade

Whitten e Tygar (1999) estudaram um programa de criptografia de e-mail e constataram que a maioria dos participantes não conseguiu usá-lo corretamente em noventa minutos, e alguns expuseram segredos que pretendiam proteger. Os problemas estavam em conceitos confusos, como chaves públicas e privadas, e numa interface que não orientava os usuários. Nadia observa que, duas décadas depois, a criptografia mais bem-sucedida, como a dos navegadores e dos aplicativos de mensagens, é aquela que os usuários mal percebem, porque funciona automaticamente, sem decisões. Essa lição molda seus conselhos.

### 17.3 Criptografia invisível

Nadia recomenda que a Ashcombe confie numa criptografia que funcione sem decisões dos funcionários: conexões criptografadas, discos de notebook criptografados ativados centralmente e chaves de segurança que usam criptografia por trás de um simples toque. Ela desaconselha pedir aos funcionários que criptografem manualmente anexos de e-mail, o que seria propenso a erros. Onde os funcionários precisam fazer uma escolha, como ao enviar dados de usuários para fora, o sistema deve oferecer uma única opção segura óbvia. Tornar a criptografia invisível aplica as lições da segurança usável a algumas de suas ferramentas mais difíceis. A TI concorda com o plano.

### Exemplo resolvido

Nadia explica criptografia e assinaturas, recupera os achados de Whitten e Tygar e recomenda a criptografia invisível.

> **Caso sintético.** As recomendações são sintéticas; Whitten e Tygar (1999) é real.

### Erros e limites

Ferramentas invisíveis podem esconder falhas. A criptografia central exige recuperação de chaves.

### Exercícios

- **EX049 — Finalidade da assinatura.** O que uma assinatura digital mostra? *Rubrica:* 3 = quem enviou a mensagem e que ela não foi alterada;; 2 = origem;; 1 = sigilo;; 0 = nenhuma.
- **EX050 — Achado do estudo.** O que Whitten e Tygar constataram? *Rubrica:* 3 = a maioria não conseguiu usar a criptografia corretamente em noventa minutos;; 2 = usabilidade;; 1 = vago;; 0 = nenhuma.
- **EX051 — Criptografia manual.** Por que evitar a criptografia manual de anexos? *Rubrica:* 3 = é propensa a erros dos funcionários;; 2 = erros;; 1 = vago;; 0 = nenhuma.

### Síntese

A criptografia protege melhor quando pede poucas decisões às pessoas.

<a id="ch-18"></a>

## Capítulo 18 — Métodos de pesquisa I

### Objetivos de aprendizagem

Você vai (1) escrever uma pergunta de pesquisa clara; (2) escolher entre questionários, entrevistas e observação; (3) planejar a amostragem e a ética de um estudo pequeno.

### 18.1 Perguntas de pesquisa

Uma boa pergunta de pesquisa é específica, respondível e vale a pena ser feita. A primeira tentativa de Nadia, como melhorar a segurança na Ashcombe, é ampla demais. Ela a estreita para: o que impede os atendentes de balcão de reportar e-mails suspeitos em até uma hora? Essa pergunta nomeia um grupo, um comportamento e um prazo, e pode ser respondida com evidências. O Dr. Prescott sugere que ela também pergunte o que ajuda os funcionários a reportar, para que o estudo identifique forças a desenvolver, além de barreiras a remover. Ela anota as duas perguntas.

### 18.2 Escolher os métodos

Questionários alcançam muitas pessoas rapidamente e servem para contar quão comuns são as opiniões. Entrevistas exploram razões em profundidade com menos pessoas. A observação mostra o que as pessoas de fato fazem, e não o que dizem. Nadia planeja usar um questionário curto e anônimo com todos os funcionários e entrevistas com oito atendentes de balcão. Ela evita a observação encoberta porque levantaria preocupações éticas sem consentimento. Combinar métodos permite que o questionário mostre quão comum é cada barreira, enquanto as entrevistas explicam por que ela importa para as pessoas. O questionário leva cinco minutos.

### 18.3 Amostragem e ética

Nadia seleciona entrevistados de unidades, turnos e níveis de experiência diferentes, para que as opiniões não sejam dominadas por um único grupo. Ela busca aprovação ética, escreve uma folha de informações e um termo de consentimento e planeja guardar as anotações sem nomes. Informa aos participantes que podem parar a qualquer momento e que os gestores verão apenas temas anonimizados. Ela testa o questionário num piloto com três colegas para verificar se as perguntas estão claras. Um planejamento cuidadoso nesta fase evita dados fracos depois. A aprovação chega em três semanas.

### Exemplo resolvido

Nadia estreita sua pergunta, combina um questionário com entrevistas e planeja a amostragem e a ética.

> **Caso sintético.** O plano de estudo é sintético.

### Erros e limites

Voluntários podem diferir dos demais. Questionários dependem de autorrelato honesto.

### Exercícios

- **EX052 — Pergunta estreitada.** Qual foi a pergunta estreitada de Nadia? *Rubrica:* 3 = o que impede os atendentes de reportar em até uma hora;; 2 = barreiras;; 1 = como melhorar a segurança;; 0 = nenhuma.
- **EX053 — Escolha da observação.** Por que Nadia evitou a observação encoberta? *Rubrica:* 3 = levanta preocupações éticas sem consentimento;; 2 = consentimento;; 1 = vago;; 0 = nenhuma.
- **EX054 — Finalidade do piloto.** Por que testar o questionário num piloto? *Rubrica:* 3 = para verificar se as perguntas estão claras;; 2 = clareza;; 1 = vago;; 0 = nenhuma.

### Síntese

Perguntas claras, métodos adequados e ética cuidadosa fazem pequenos estudos valerem a pena.

<a id="ch-19"></a>

## Capítulo 19 — Fatores humanos e política cibernética: escopo e teoria

### Objetivos de aprendizagem

Você vai (1) definir o escopo dos fatores humanos em cibersegurança; (2) explicar as principais teorias do comportamento de segurança; (3) aplicar a teoria à Ashcombe.

### 19.1 Escopo

Os fatores humanos em cibersegurança estudam como as pessoas interagem com a segurança: usuários, defensores, gestores e atacantes. O campo cobre usabilidade, tomada de decisão, cultura, política, treinamento e engenharia social. Nadia aprende que o campo passou de culpar os usuários a projetar para eles, uma mudança expressa nos títulos de Adams e Sasse (1999), "Users are not the enemy", e de Sasse, Brostoff e Weirich (2001), "Transforming the weakest link". O escopo também inclui a política, porque regras e leis moldam o que as organizações pedem às pessoas. Nadia lê os dois artigos na íntegra.

### 19.2 Teorias do comportamento

Várias teorias ajudam a explicar o comportamento de segurança. A teoria do comportamento planejado, de Ajzen (1991), diz que as intenções dependem das atitudes, das normas sociais e do controle percebido. O orçamento de compliance (Beautement, Sasse e Wonham, 2008) diz que as pessoas pesam o esforço de segurança contra suas tarefas principais. Herley (2009) argumentou que rejeitar alguns conselhos é racional quando seus custos superam os benefícios. Nadia compara essas teorias e observa que elas concordam num ponto: o comportamento depende de quão fácil e quão valiosa a ação segura parece, e não apenas do conhecimento. Ela resume cada uma numa tabela.

### 19.3 Aplicar a teoria

Nadia aplica essas teorias ao problema de reporte da Ashcombe. O comportamento planejado sugere verificar se os funcionários acreditam que os colegas reportam e se reportar parece fácil. O orçamento de compliance sugere verificar se reportar compete com o atendimento aos usuários. A visão de Herley sugere verificar se os funcionários veem algum benefício em reportar. Ela transforma cada ponto num item do questionário. Assim, a teoria orienta o que medir, em vez de deixar o estudo à mercê das perguntas que lhe ocorrerem, e ajuda a explicar os resultados quando os dados chegam. Cada item está ligado a uma teoria em seu plano.

### Exemplo resolvido

Nadia define o campo, compara três teorias e as transforma em itens de questionário para a Ashcombe.

> **Caso sintético.** A aplicação é sintética; Ajzen (1991), Beautement et al. (2008) e Herley (2009) são reais.

### Erros e limites

As teorias se sobrepõem. Os itens do questionário podem não capturar plenamente os construtos.

### Exercícios

- **EX055 — Mudança do campo.** Que mudança o campo mostra? *Rubrica:* 3 = de culpar os usuários a projetar para eles;; 2 = design;; 1 = vago;; 0 = nenhuma.
- **EX056 — Partes do comportamento planejado.** Que três fatores moldam as intenções na teoria de Ajzen? *Rubrica:* 3 = atitudes, normas e controle percebido;; 2 = três;; 1 = vago;; 0 = nenhuma.
- **EX057 — Ponto comum.** Em que as teorias concordam? *Rubrica:* 3 = o comportamento depende de quão fácil e valiosa a ação segura parece;; 2 = facilidade;; 1 = conhecimento;; 0 = nenhuma.

### Síntese

A teoria define o que procurar no comportamento de segurança e orienta a medição.

<a id="ch-20"></a>

## Capítulo 20 — Fatores humanos e política cibernética: casos fundamentais

### Objetivos de aprendizagem

Você vai (1) analisar relatos publicados de engenharia social; (2) identificar fatores humanos comuns em incidentes; (3) tirar lições para organizações pequenas.

### 20.1 Estudar casos

Nadia estuda como a engenharia social é descrita em Hadnagy (2018) e no Verizon DBIR. Padrões comuns incluem fingir ser uma autoridade confiável, criar urgência, explorar a prestatividade e usar informações coletadas em fontes públicas. Ela constrói um caso sintético para a Ashcombe com base nesses padrões: alguém que liga fingindo ser auditor da prefeitura pede a uma atendente de unidade que envie por e-mail uma lista de usuários com multas em atraso, alegando um prazo naquela mesma tarde. O caso lhe permite analisar os fatores sem usar nenhum incidente real. O Dr. Prescott aprova o caso.

### 20.2 Fatores comuns

Nadia lista os fatores humanos do caso sintético: a pressão de autoridade de um suposto cargo na prefeitura; a urgência do prazo; a prestatividade, já que os atendentes querem ajudar as autoridades; e a falta de um procedimento para pedidos de dados. Ela observa que a atendente não é tola; a situação foi desenhada para explorar intenções normais e boas. Também identifica fatores organizacionais: nenhum responsável claro pelos pedidos de dados e nenhuma forma fácil de verificar se o auditor existe. A maioria dos fatores está no sistema, e não na pessoa.

### 20.3 Lições para organizações pequenas

Organizações pequenas como a Ashcombe não têm equipes de segurança, por isso as lições precisam ser simples. Nadia propõe três: uma regra de que dados de usuários nunca são enviados em resposta a uma ligação; um único contato nomeado que verifica qualquer pedido oficial; e uma cultura em que os funcionários possam dizer não à pressão sem medo. Ela observa que as diretrizes de cultura de cibersegurança da ENISA enfatizam a cultura organizacional e o apoio da liderança. Essas lições custam pouco, o que importa para uma biblioteca pública com orçamento apertado. Os gestores as discutem numa reunião de equipe.

### Exemplo resolvido

Nadia constrói um caso sintético de falsificação de identidade, identifica fatores pessoais e organizacionais e propõe três lições simples.

> **Caso sintético.** O caso é sintético; Hadnagy (2018), o DBIR e as diretrizes da ENISA são reais.

### Erros e limites

Casos sintéticos podem deixar de fora detalhes reais. Regras simples têm exceções.

### Exercícios

- **EX058 — Tipos de pressão.** Que pressões quem ligou usou? *Rubrica:* 3 = autoridade e urgência;; 2 = duas;; 1 = vago;; 0 = nenhuma.
- **EX059 — Onde estão os fatores.** Onde está a maioria dos fatores no caso? *Rubrica:* 3 = no sistema, e não na pessoa;; 2 = sistema;; 1 = a atendente;; 0 = nenhuma.
- **EX060 — Contato nomeado.** O que faz o contato nomeado? *Rubrica:* 3 = verifica qualquer pedido oficial;; 2 = verificar;; 1 = vago;; 0 = nenhuma.

### Síntese

Os casos mostram que a engenharia social explora boas intenções e procedimentos ausentes.

<a id="ch-21"></a>

## Capítulo 21 — Fatores humanos e política cibernética: modelos de sistema

### Objetivos de aprendizagem

Você vai (1) modelar o processo de reporte como um sistema com entradas, etapas e retorno; (2) identificar atrasos e pontos de perda; (3) usar o modelo para priorizar melhorias.

### 21.1 Um modelo de processo

Nadia modela o processo de reporte da Ashcombe como um sistema. A entrada é um e-mail suspeito que chega à caixa de entrada de um funcionário. Seguem-se as etapas: a pessoa nota algo estranho, decide se vai reportar, descobre como reportar, envia o reporte, a TI o analisa e a TI responde. O retorno da TI influencia se a pessoa vai reportar da próxima vez. Desenhar o processo com caixas e setas a ajuda a ver que reportar não é um ato único, mas uma cadeia, e que qualquer elo fraco dessa cadeia pode impedir que um alerta chegue à TI.

### 21.2 Atrasos e perdas

Em cada etapa, alguns reportes se perdem ou atrasam. Alguns funcionários não notam os sinais; outros notam, mas decidem não se dar ao trabalho; alguns não encontram o endereço de reporte; e a TI, com duas pessoas, pode levar um dia para responder. Nadia estima, a partir do questionário e dos registros da TI, quantos reportes potenciais sobrevivem a cada etapa. O laboratório multiplica as taxas das etapas para estimar quantos de cada cem e-mails suspeitos se tornam reportes com resposta. O resultado mostra que a etapa de decisão é a que mais perde.

### Laboratório — Funil de reporte, de notar a receber resposta

```python
# Reporting funnel for 100 suspicious emails (synthetic step rates).
steps = [("notice", 0.70), ("decide to report", 0.45), ("find how to report", 0.85), ("receive reply", 0.90)]
n = 100.0
for s, r in steps:
    n2 = n * r; print(f"{s}: {n:.0f} -> {n2:.0f} (lose {n - n2:.0f})"); n = n2
print(f"replied reports per 100: {n:.0f}")
```

Execute com `python3 lab_funnel.py`. Saída verificada:

```text
notice: 100 -> 70 (lose 30)
decide to report: 70 -> 32 (lose 38)
find how to report: 32 -> 27 (lose 5)
receive reply: 27 -> 24 (lose 3)
replied reports per 100: 24
```

### 21.3 Priorizar

O modelo ajuda Nadia a priorizar. Melhorar a etapa de decisão, dando aos funcionários a confiança de que reportar é bem-vindo mesmo na dúvida, aumentaria os reportes mais do que melhorar a percepção por meio de treinamento. Acrescentar um botão de reporte ajudaria na etapa de descobrir como reportar. Respostas mais rápidas da TI fortaleceriam o retorno para reportes futuros. Ela ordena as melhorias pelo número de reportes extras que cada uma produziria por unidade de esforço. Um modelo de sistema desloca a atenção de apelos vagos por conscientização para etapas específicas em que as pessoas precisam de apoio. Os gestores aprovam a ordenação.

### Exemplo resolvido

Nadia modela o reporte como uma cadeia, estima as perdas em cada etapa e prioriza a etapa de decisão.

> **Caso sintético.** As taxas são sintéticas.

### Erros e limites

As taxas das etapas são estimativas grosseiras. As etapas interagem.

### Exercícios

- **EX061 — Visão de cadeia.** Por que modelar o reporte como uma cadeia? *Rubrica:* 3 = qualquer etapa fraca pode barrar um alerta;; 2 = elo fraco;; 1 = ato único;; 0 = nenhuma.
- **EX062 — Sobreviventes do funil.** Quantos de 100 e-mails suspeitos se tornam reportes com resposta no laboratório? *Rubrica:* 3 = cerca de 24;; 2 = 24;; 1 = vago;; 0 = nenhuma.
- **EX063 — Maior perda.** Que etapa mais perde? *Rubrica:* 3 = a decisão de reportar;; 2 = decisão;; 1 = notar;; 0 = nenhuma.

### Síntese

Um modelo do sistema mostra onde os reportes se perdem e qual etapa melhorar primeiro.

<a id="ch-22"></a>

## Capítulo 22 — Fatores humanos e política cibernética: dados e dependências

### Objetivos de aprendizagem

Você vai (1) identificar os dados e as pessoas de que o processo de reporte depende; (2) analisar pontos únicos de falha; (3) reduzir a dependência de indivíduos.

### 22.1 Dependências

Nadia lista aquilo de que o processo de reporte depende: o sistema de e-mail, o endereço de reporte, as duas pessoas da TI, os gestores de unidade que repassam reportes verbais e uma planilha compartilhada em que a TI registra os reportes. Ela também lista os fluxos de dados: os reportes trazem cabeçalhos de e-mail e às vezes conteúdo pessoal, e a planilha contém nomes de funcionários. Mapear as dependências mostra o que precisa funcionar para que o reporte dê certo e quais dados precisam de proteção, já que um log de reportes vazado poderia revelar quem reportou o quê e desestimular futuros reportes dos colegas.

### 22.2 Pontos únicos de falha

Um ponto único de falha é uma parte cuja perda interrompe todo o processo. Nadia encontra dois: uma única analista de TI trata quase todos os reportes, e o endereço de reporte encaminha para a caixa de entrada pessoal dela. Quando ela está de férias, os reportes ficam sem resposta por dias. Em duas unidades, os gestores são a única rota para os funcionários que não usam e-mail no trabalho. Essas dependências de indivíduos tornam o processo frágil, sobretudo numa organização pequena, em que a rotatividade ou uma doença pode facilmente afastar uma pessoa-chave.

### 22.3 Reduzir a dependência

Nadia propõe uma caixa postal de reporte compartilhada, monitorada pelas duas pessoas da TI, com uma confirmação automática para que quem reporta saiba que a mensagem chegou. Ela sugere um formulário impresso simples nas unidades para os funcionários sem e-mail, recolhido diariamente. Recomenda remover os nomes dos funcionários do log e registrar apenas a unidade e o veredito, em linha com a minimização de dados. Essas mudanças custam pouco, mas tornam o processo robusto a ausências. Reduzir a dependência de indivíduos é um tema ao qual ela voltará nas operações e no trabalho de conclusão.

### Exemplo resolvido

Nadia mapeia dependências e dados, encontra pontos únicos de falha na TI e nos gestores e propõe uma caixa postal compartilhada, formulários impressos e um log minimizado.

> **Caso sintético.** O processo é sintético.

### Erros e limites

Caixas postais compartilhadas precisam de responsáveis claros. Formulários em papel podem se perder.

### Exercícios

- **EX064 — Risco do log.** Por que um log de reportes vazado é prejudicial? *Rubrica:* 3 = poderia revelar quem reportou o quê;; 2 = nomes;; 1 = vago;; 0 = nenhuma.
- **EX065 — Dependência da TI.** Que ponto único de falha envolve a TI? *Rubrica:* 3 = uma única analista cuja caixa de entrada recebe os reportes;; 2 = uma pessoa;; 1 = vago;; 0 = nenhuma.
- **EX066 — Confirmação.** O que a confirmação automática faz? *Rubrica:* 3 = avisa a quem reportou que a mensagem chegou;; 2 = confirmação;; 1 = vago;; 0 = nenhuma.

### Síntese

Processos robustos evitam depender de pessoas únicas e minimizam os dados sensíveis.

<a id="ch-23"></a>

## Capítulo 23 — Fatores humanos e política cibernética: métodos I

### Objetivos de aprendizagem

Você vai (1) analisar dados de questionário sobre barreiras ao reporte; (2) codificar respostas de entrevistas em temas; (3) combinar ambos em achados.

### 23.1 Análise do questionário

O questionário anônimo de Nadia recebeu 84 respostas de 120 funcionários. Ela perguntou quais barreiras tornavam o reporte menos provável, permitindo várias respostas. O laboratório conta quantas vezes cada barreira foi escolhida. A barreira mais comum é a dúvida sobre se um e-mail é suspeito o suficiente, seguida de não saber como reportar e do receio de parecer tolo. Ela relata contagens e porcentagens e observa que quem respondeu pode diferir de quem não respondeu, talvez por ser mais engajado, de modo que os resultados descrevem quem respondeu, e não todos os funcionários. Ela compartilha as contagens com os funcionários.

### Laboratório — Contagem das barreiras relatadas

```python
# Barrier counts from 84 synthetic survey responses (multiple choice).
b = {"unsure if suspicious enough": 45, "don't know how to report": 28, "worry about looking foolish": 19, "too busy": 17, "never hear back": 12}
for k, v in sorted(b.items(), key=lambda x: -x[1]): print(f"{k}: {v}/84 = {v / 84:.0%}")
```

Execute com `python3 lab_barriers.py`. Saída verificada:

```text
unsure if suspicious enough: 45/84 = 54%
don't know how to report: 28/84 = 33%
worry about looking foolish: 19/84 = 23%
too busy: 17/84 = 20%
never hear back: 12/84 = 14%
```

### 23.2 Codificar entrevistas

Nadia entrevista oito atendentes de balcão por cerca de vinte minutos cada, fazendo anotações sem nomes. Lê as anotações várias vezes e rotula trechos com códigos como dúvida, pressa, sem resposta e constrangimento. Agrupa os códigos em temas: incerteza, pressão de tempo, falta de retorno e risco social. Uma segunda estudante codifica duas entrevistas de forma independente, e as duas comparam os resultados, discutindo as divergências para refinar as definições dos códigos. Essa verificação simples melhora a consistência e torna a codificação menos dependente da interpretação de uma única pessoa. Elas concordam na maioria dos códigos.

### 23.3 Combinar os achados

Nadia combina o questionário e as entrevistas. O questionário mostra que a incerteza é a barreira mais comum; as entrevistas a explicam: os funcionários temem desperdiçar o tempo da TI e nunca ouviram que reportes na dúvida são bem-vindos. A falta de retorno aparece nas entrevistas, embora não esteja entre as principais escolhas do questionário, o que sugere que ela importa mais do que o questionário captou. Seus achados são que a Ashcombe deve dizer explicitamente aos funcionários que reportem na dúvida, tornar o reporte mais rápido e responder a todos os reportes. Cada achado está ligado à sua evidência.

### Exemplo resolvido

Nadia conta as barreiras de 84 respostas ao questionário, codifica as entrevistas em temas com uma segunda codificadora e combina os métodos em achados.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Viés de resposta no questionário. A codificação continua sendo interpretativa.

### Exercícios

- **EX067 — Taxa de resposta.** Qual foi a taxa de resposta do questionário? *Rubrica:* 3 = 70%;; 2 = 84 de 120;; 1 = 84%;; 0 = nenhuma.
- **EX068 — Barreira principal.** Qual foi a barreira principal e sua proporção? *Rubrica:* 3 = dúvida sobre se é suspeito o suficiente, 45 de 84 ou 54%;; 2 = incerteza;; 1 = vago;; 0 = nenhuma.
- **EX069 — Segunda codificadora.** Por que uma segunda estudante codificou entrevistas? *Rubrica:* 3 = para verificar a consistência dos códigos;; 2 = consistência;; 1 = vago;; 0 = nenhuma.

### Síntese

Os questionários mostram quão comuns são as barreiras, e as entrevistas explicam por que elas importam.

<a id="ch-24"></a>

## Capítulo 24 — Fatores humanos e política cibernética: controles

### Objetivos de aprendizagem

Você vai (1) desenhar controles que tratem as barreiras identificadas; (2) aplicar nudges éticos; (3) avaliar o ônus dos controles.

### 24.1 Controles a partir dos achados

Nadia desenha controles ligados a seus achados. Para tratar a incerteza, a Ashcombe declarará com clareza que reportes na dúvida são bem-vindos e agradecerá a cada pessoa que reportar. Para tratar a dificuldade, um botão de reporte será acrescentado ao cliente de e-mail. Para tratar a falta de retorno, a TI responderá em até um dia útil com um veredito curto. Para tratar o risco de falsificação de identidade por telefone, serão introduzidos a regra de não revelação e o contato nomeado. Cada controle remonta a uma evidência, o que ajuda os gestores a ver por que ele é necessário e o que deve mudar.

### 24.2 Nudges éticos

Um nudge é uma pequena mudança de design que facilita uma escolha sem impô-la. Nadia propõe posicionar o botão de reporte em destaque e mostrar um lembrete curto quando e-mails externos pedirem pagamento ou senhas. Ela define limites: os nudges devem ser transparentes, os funcionários devem poder ignorá-los e eles nunca devem manipular as pessoas pelo medo. Ela observa que Bada, Sasse e Nurse (2019) alertaram que mensagens baseadas no medo podem sair pela culatra. Os nudges respeitam a autonomia e, ao mesmo tempo, reduzem o esforço de fazer a coisa segura.

### 24.3 Avaliar o ônus

Todo controle acrescenta algum esforço. Nadia estima quanto tempo por semana cada controle custa aos funcionários: o botão de reporte economiza tempo em comparação com o encaminhamento; os lembretes acrescentam alguns segundos; a regra de não revelação reduz conversas telefônicas difíceis. Ela apresenta uma estimativa geral que mostra uma economia líquida de tempo dos funcionários. Também observa que os controles devem ser revistos depois de três meses quanto a ônus inesperados, como lembretes que aparecem com frequência excessiva. Avaliar o ônus antes da implantação reflete a ideia do orçamento de compliance e ajuda a manter os controles sustentáveis.

### Exemplo resolvido

Nadia desenha quatro controles a partir dos achados, define limites éticos para os nudges e estima o ônus para os funcionários.

> **Caso sintético.** Os controles são sintéticos; Bada et al. (2019) é real.

### Erros e limites

As estimativas de ônus podem ser otimistas. Os nudges perdem força com a familiaridade.

### Exercícios

- **EX070 — Controle de retorno.** Que controle trata a falta de retorno? *Rubrica:* 3 = a TI responde em até um dia útil;; 2 = resposta;; 1 = vago;; 0 = nenhuma.
- **EX071 — Limites dos nudges.** Que limites se aplicam aos nudges? *Rubrica:* 3 = transparentes, ignoráveis e não baseados no medo;; 2 = limites;; 1 = vago;; 0 = nenhuma.
- **EX072 — Momento da revisão.** Quando os controles devem ser revistos quanto ao ônus? *Rubrica:* 3 = depois de três meses;; 2 = três meses;; 1 = vago;; 0 = nenhuma.

### Síntese

Controles rastreados até as evidências, incentivados de forma ética e verificados quanto ao ônus têm mais chance de perdurar.

<a id="ch-25"></a>

## Capítulo 25 — Laboratório I

### Objetivos de aprendizagem

Você vai (1) conduzir um teste controlado do botão de reporte com voluntários; (2) medir o tempo e o sucesso da tarefa; (3) relatar os resultados com seus limites.

### 25.1 Planejar o teste

No primeiro laboratório, Nadia testa o botão de reporte com dez funcionários voluntários, usando uma caixa postal de teste cheia de e-mails sintéticos. Nenhuma caixa de entrada real é usada, e os voluntários sabem que se trata de um teste do botão, e não deles. Pede-se a cada voluntário que reporte dois e-mails suspeitos, uma vez encaminhando-o para o endereço e outra com o botão. Ela registra o tempo da tarefa e se o reporte deu certo. O plano tem aprovação ética, e os voluntários podem parar a qualquer momento. Cada sessão leva dez minutos.

### 25.2 Medir

O laboratório compara os tempos da tarefa. O encaminhamento leva cerca de quarenta segundos em média, porque as pessoas precisam encontrar o endereço e acrescentar uma nota. O botão leva cerca de seis segundos. Os dez voluntários conseguem com o botão; dois não conseguem encaminhar corretamente porque digitam o endereço errado. Nadia também pede aos voluntários que avaliem a facilidade numa escala de cinco pontos. As avaliações favorecem fortemente o botão. O teste mostra que uma pequena mudança de design elimina boa parte do esforço que desestimulava o reporte. Ela registra cada tempo numa tabela.

### Laboratório — Tempo da tarefa: encaminhamento versus botão

```python
# Task times in seconds for ten volunteers (synthetic).
fwd = [35, 42, 38, 51, 33, 44, 39, 36, 47, 35]
btn = [5, 7, 6, 6, 5, 8, 6, 5, 7, 5]
print(f"forwarding mean {sum(fwd) / 10:.0f} s; button mean {sum(btn) / 10:.0f} s; saving {sum(fwd) / 10 - sum(btn) / 10:.0f} s")
```

Execute com `python3 lab_button.py`. Saída verificada:

```text
forwarding mean 40 s; button mean 6 s; saving 34 s
```

### 25.3 Relatar os resultados

Nadia relata os resultados numa nota curta, com uma tabela de tempos e taxas de sucesso. Acrescenta os limites: os voluntários podem ser mais confiantes do que os funcionários típicos; o teste usou um computador de mesa, e não celulares; e dez pessoas são uma amostra pequena. Ela recomenda implantar o botão e depois conferir os tempos reais de reporte. Declarar os limites com honestidade torna os gestores mais propensos a confiar no resultado, porque eles conseguem ver o que ele mostra e o que não mostra. Os gestores aceitam a nota.

### Exemplo resolvido

Nadia testa um botão de reporte com dez voluntários numa caixa postal de teste, encontra uma grande economia de tempo e relata os limites.

> **Caso sintético.** O teste é sintético.

### Erros e limites

Os voluntários não são típicos. As condições do laboratório diferem das de um balcão movimentado.

### Exercícios

- **EX073 — Caixa postal de teste.** Por que usar uma caixa postal de teste? *Rubrica:* 3 = para que nenhuma caixa de entrada real seja envolvida;; 2 = controlado;; 1 = vago;; 0 = nenhuma.
- **EX074 — Tempos médios.** Quais foram os tempos médios do encaminhamento e do botão? *Rubrica:* 3 = 40 e 6 segundos;; 2 = 34 segundos economizados;; 1 = vago;; 0 = nenhuma.
- **EX075 — Falhas de encaminhamento.** Quantos voluntários não conseguiram encaminhar corretamente? *Rubrica:* 3 = dois;; 2 = 2;; 1 = vago;; 0 = nenhuma.

### Síntese

Testes de usabilidade contidos mostram o efeito de pequenas mudanças de desenho e os seus limites.

<a id="ch-26"></a>

## Capítulo 26 — Fatores humanos e política cibernética: métodos II

### Objetivos de aprendizagem

Você vai (1) analisar a mudança ao longo do tempo com dados de antes e depois; (2) reconhecer fatores de confusão; (3) usar um grupo de comparação quando possível.

### 26.1 Antes e depois

Depois que a Ashcombe acrescenta o botão de reporte, declara que reportes na dúvida são bem-vindos e promete respostas, Nadia compara os reportes de antes e de depois. Nos três meses anteriores, os funcionários reportaram em média 12 e-mails suspeitos por mês; nos três meses seguintes, 31. Ela calcula a mudança e observa que é grande. Ainda assim, uma simples comparação antes e depois não consegue dizer se as mudanças causaram o aumento, porque outras coisas podem ter mudado no mesmo período, como o número de ataques. Ela plota os dois períodos.

### 26.2 Confusão

Um fator de confusão é algo que afeta tanto o momento de uma mudança quanto o resultado. Nadia considera vários: uma campanha nacional de phishing contra bibliotecas durante o período posterior, a cobertura jornalística de uma violação numa biblioteca e a chegada de novos funcionários. Qualquer um deles poderia ter aumentado os reportes. Ela consulta os registros da TI e descobre que os e-mails maliciosos também subiram, de 3 para 5 por mês, o que poderia explicar parte do aumento. Considerar abertamente os fatores de confusão é essencial para não afirmar mais do que as evidências sustentam.

### 26.3 Grupos de comparação

Nadia aprende que um grupo de comparação ajuda a separar os efeitos. Duas unidades receberam o botão um mês depois das demais por causa de um atraso técnico. Nesse mês, os reportes nas unidades que o receberam antes subiram fortemente, enquanto nas que o receberam depois pouco mudaram. O laboratório calcula os reportes por cem funcionários de cada grupo naquele mês. A diferença sustenta a ideia de que as mudanças, e não apenas eventos externos, aumentaram os reportes. Ela observa que os grupos não foram escolhidos ao acaso, de modo que podem diferir também em outros aspectos.

### Laboratório — Unidades adiantadas e atrasadas no mês da implantação

```python
# Rollout month: reports per hundred staff for early and late branches (synthetic).
early = (25, 96); late = (2, 24)
for name, (r, s) in (("early", early), ("late", late)): print(f"{name}: {r} reports / {s} staff = {100 * r / s:.0f} per 100")
```

Execute com `python3 lab_compare.py`. Saída verificada:

```text
early: 25 reports / 96 staff = 26 per 100
late: 2 reports / 24 staff = 8 per 100
```

### Exemplo resolvido

Nadia compara os reportes de antes e depois, considera os fatores de confusão e usa uma implantação atrasada como grupo de comparação.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Grupos não aleatórios podem diferir. Um mês é pouco tempo.

### Exercícios

- **EX076 — Mudança mensal.** Como mudou a média mensal de reportes? *Rubrica:* 3 = de 12 para 31;; 2 = aumento de 19;; 1 = vago;; 0 = nenhuma.
- **EX077 — Fator de confusão encontrado.** Que fator de confusão os registros da TI revelaram? *Rubrica:* 3 = os e-mails maliciosos subiram de 3 para 5 por mês;; 2 = mais ataques;; 1 = vago;; 0 = nenhuma.
- **EX078 — Taxas dos grupos.** Que taxas as unidades adiantadas e atrasadas mostraram no mês da implantação? *Rubrica:* 3 = 26 contra 8 por cem funcionários;; 2 = adiantadas mais altas;; 1 = vago;; 0 = nenhuma.

### Síntese

Dados de antes e depois exigem considerar os fatores de confusão e, sempre que possível, grupos de comparação.

<a id="ch-27"></a>

## Capítulo 27 — Fatores humanos e política cibernética: verificação

### Objetivos de aprendizagem

Você vai (1) verificar se os controles funcionam conforme especificado; (2) conferir os controles do lado do usuário; (3) registrar as evidências da verificação.

### 27.1 Comportamento especificado

A verificação confere se cada controle faz o que deveria. Nadia lista as especificações: o botão aparece em todas as caixas postais dos funcionários; os reportes chegam à caixa postal compartilhada; uma confirmação é enviada em até um minuto; as respostas são enviadas em até um dia útil; e o cartão do procedimento telefônico está em todos os balcões. Ela testa cada uma com e-mails sintéticos e uma lista de verificação para visitas às unidades. A verificação difere da avaliação: não pergunta se o reporte melhorou, apenas se os controles estão implantados e funcionando corretamente. A TI aprova a lista antes.

### 27.2 Verificações do lado do usuário

Nadia confere os controles do lado do usuário, e não apenas pelo console da TI. Ela faz login com uma conta de funcionário de teste num computador de balcão e num notebook e reporta um e-mail sintético. No computador de balcão, o botão fica escondido atrás de um menu por causa de uma configuração de tela menor. A TI ajusta o layout. Ela também pede a três funcionários que encontrem o cartão do procedimento telefônico; uma unidade o havia guardado numa gaveta. As verificações do lado do usuário revelam problemas que as verificações técnicas não pegam, porque testam o que as pessoas de fato veem.

### 27.3 Registrar as evidências

Nadia registra cada verificação com data, método, resultado e correção. Das oito verificações, seis passaram na primeira vez e duas foram corrigidas e testadas de novo. Ela guarda o registro com os documentos do programa, para que possa ser repetido depois de mudanças. Registrar falhas e correções demonstra que a verificação foi genuína, e não uma formalidade. O Dr. Prescott observa que organizações pequenas muitas vezes pulam essa etapa, mas o registro se torna valioso quando os funcionários mudam ou quando auditores perguntam como os controles foram conferidos. O registro tem duas páginas.

### Exemplo resolvido

Nadia verifica cinco especificações, encontra um botão escondido e um cartão fora do lugar por meio de verificações do lado do usuário e registra oito verificações.

> **Caso sintético.** As verificações são sintéticas.

### Erros e limites

As verificações mostram um momento no tempo. Mudanças de layout podem reintroduzir problemas.

### Exercícios

- **EX079 — Verificação versus avaliação.** O que a verificação não pergunta? *Rubrica:* 3 = se o reporte melhorou;; 2 = resultados;; 1 = vago;; 0 = nenhuma.
- **EX080 — Problema no balcão.** Que problema apareceu nos computadores de balcão? *Rubrica:* 3 = o botão estava escondido atrás de um menu;; 2 = escondido;; 1 = vago;; 0 = nenhuma.
- **EX081 — Registro das verificações.** Quantas das oito verificações passaram na primeira vez? *Rubrica:* 3 = seis;; 2 = 6;; 1 = vago;; 0 = nenhuma.

### Síntese

A verificação confere os controles tanto do lado técnico quanto do lado do usuário e registra as evidências.

<a id="ch-28"></a>

## Capítulo 28 — Fatores humanos e política cibernética: análise de falhas

### Objetivos de aprendizagem

Você vai (1) analisar um quase incidente sem atribuir culpa; (2) classificar os fatores contribuintes; (3) transformar a análise em melhorias.

### 28.1 Um quase incidente

Durante o ano, uma atendente de unidade quase pagou uma fatura falsa de fornecimento de livros. O e-mail veio de um domínio parecido com o de um fornecedor real e pedia pagamento em novos dados bancários. A atendente o encaminhou ao analista financeiro, que notou a mudança nos dados e ligou para o fornecedor usando o número do cadastro. Nadia analisa esse quase incidente. Quase incidentes são valiosos porque revelam fraquezas sem causar danos, mas as pessoas só os compartilham se confiarem que não serão culpadas.

### 28.2 Fatores contribuintes

Nadia classifica os fatores em individuais, da tarefa, técnicos e organizacionais. No plano individual, a atendente era nova e não conhecia os fornecedores. A tarefa era rotineira, por isso não despertou suspeita. No plano técnico, o domínio parecido passou nas verificações de e-mail e não tinha alerta de mensagem externa. No plano organizacional, não havia regra exigindo verificação de mudanças de dados bancários, embora o analista financeiro tenha verificado por hábito. O laboratório totaliza os fatores deste e de outros quatro quase incidentes registrados naquele ano, mostrando que os fatores organizacionais aparecem com mais frequência. Cada fator é anotado numa tabela.

### Laboratório — Fatores contribuintes em cinco quase incidentes

```python
# Contributing factors across five near misses (synthetic).
nm = [{"individual", "technical", "organisational"}, {"task", "organisational"}, {"technical", "organisational"},
      {"individual", "organisational"}, {"task", "technical", "organisational"}]
for f in ("organisational", "technical", "individual", "task"): print(f, sum(f in s for s in nm), "of", len(nm))
```

Execute com `python3 lab_factors.py`. Saída verificada:

```text
organisational 5 of 5
technical 3 of 5
individual 2 of 5
task 2 of 5
```

### 28.3 Melhorias

Nadia propõe melhorias associadas aos fatores: uma regra escrita de que qualquer mudança de dados bancários deve ser verificada por telefone, usando um número conhecido; uma etiqueta de e-mail externo; e uma familiarização com os fornecedores para os novos funcionários. Ela elogia o hábito do analista financeiro e recomenda transformá-lo em regra, em vez de depender de uma pessoa. Compartilha a análise com os funcionários, sem nomes, para mostrar que reportar quase incidentes leva a mudanças úteis. A análise sem culpados estimula futuros reportes de quase incidentes e erros. Os gestores aprovam as três medidas.

### Exemplo resolvido

Nadia analisa sem culpa o quase incidente da fatura falsa, classifica os fatores e propõe uma regra de verificação e etiquetas de e-mail externo.

> **Caso sintético.** O quase incidente é sintético.

### Erros e limites

As classes de fatores se sobrepõem. Cinco quase incidentes são um conjunto pequeno.

### Exercícios

- **EX082 — Valor do quase incidente.** Por que os quase incidentes são valiosos? *Rubrica:* 3 = revelam fraquezas sem causar danos;; 2 = aprendizado;; 1 = vago;; 0 = nenhuma.
- **EX083 — Classe mais comum.** Que classe de fator mais apareceu no laboratório? *Rubrica:* 3 = organizacional, em 5 de 5;; 2 = organizacional;; 1 = individual;; 0 = nenhuma.
- **EX084 — Do hábito à regra.** O que Nadia fez com o hábito do analista financeiro? *Rubrica:* 3 = transformou-o numa regra escrita;; 2 = regra;; 1 = vago;; 0 = nenhuma.

### Síntese

A análise de quase-incidentes sem culpados encontra fatores do sistema e transforma hábitos em regras.

<a id="ch-29"></a>

## Capítulo 29 — Fatores humanos e política cibernética: operações

### Objetivos de aprendizagem

Você vai (1) definir as tarefas de rotina que sustentam o programa; (2) planejar reciclagens e simulações éticas; (3) tratar o retorno dos funcionários.

### 29.1 Tarefas de rotina

Um programa se apaga sem cuidados de rotina. Nadia rascunha um calendário para a Ashcombe: a TI confere a caixa postal compartilhada diariamente e responde em até um dia; todo mês, a TI compartilha uma nota curta sobre e-mails suspeitos recentes; todo trimestre, os gestores revisam os números de reporte por grupo de unidades; todo ano, o programa é revisto. Cada tarefa tem um responsável e um substituto. O calendário é pequeno o bastante para uma equipe de TI de duas pessoas, o que importa porque um plano ambicioso que não pode ser sustentado desmoronaria rapidamente. Os gestores aprovam o calendário.

### 29.2 Reciclagens e simulações

Nadia propõe reciclagens de cinco minutos nas reuniões de equipe, usando exemplos reais recentes sem dados pessoais. Ela pondera se deve haver phishing simulado e recomenda apenas um pequeno número, no máximo duas vezes por ano, sob as regras do capítulo 10: programa anunciado, modelos acordados com os representantes dos funcionários, nenhuma isca sobre salário ou saúde, retorno imediato e gentil e apenas resultados agregados. Ela classifica os modelos com a NIST Phish Scale, para que os resultados possam ser comparados de um ano para outro. Também pede aos representantes dos funcionários que revisem os temas das reciclagens a cada trimestre.

### 29.3 Retorno dos funcionários

Os funcionários podem comentar o programa por meio de um formulário de retorno e nas reuniões de equipe. Nadia espera algumas reclamações, sobretudo sobre as simulações, e propõe que cada uma seja respondida pessoalmente e registrada por tema. Se um modelo incomodar os funcionários, ele é retirado. Responder bem ao retorno mostra aos funcionários que o programa os respeita, o que sustenta a confiança da qual os reportes dependem. O retorno também revela problemas práticos, como lembretes que aparecem com frequência excessiva, que os gestores de outro modo talvez não percebessem. Os temas são relatados aos gestores a cada trimestre.

### Exemplo resolvido

Nadia rascunha um calendário sustentável, planeja reciclagens breves e simulações éticas limitadas e organiza o tratamento do retorno.

> **Caso sintético.** Os planos são sintéticos; a Phish Scale é real.

### Erros e limites

Os calendários escorregam sob pressão. Poucas simulações geram dados limitados.

### Exercícios

- **EX085 — Frequência das simulações.** Com que frequência Nadia recomenda simulações? *Rubrica:* 3 = no máximo duas vezes por ano;; 2 = duas vezes;; 1 = mensalmente;; 0 = nenhuma.
- **EX086 — Classificação dos modelos.** Por que classificar os modelos com a Phish Scale? *Rubrica:* 3 = para que os resultados possam ser comparados entre anos;; 2 = comparação;; 1 = vago;; 0 = nenhuma.
- **EX087 — Modelo que incomoda.** O que acontece com um modelo que incomoda os funcionários? *Rubrica:* 3 = é retirado;; 2 = retirar;; 1 = vago;; 0 = nenhuma.

### Síntese

Operações sustentáveis usam pequenas rotinas, simulações éticas limitadas e um tratamento ágil do retorno recebido.

<a id="ch-30"></a>

## Capítulo 30 — Laboratório II

### Objetivos de aprendizagem

Você vai (1) analisar o efeito da rapidez da resposta sobre os reportes posteriores; (2) apresentar resultados com sua incerteza; (3) recomendar mudanças a partir das evidências.

### 30.1 A pergunta sobre a rapidez da resposta

As entrevistas sugeriram que o retorno importa. No segundo laboratório, Nadia analisa os registros da TI para ver se os funcionários que receberam resposta em até um dia tinham mais probabilidade de reportar de novo em três meses do que os que receberam resposta tardia ou nenhuma. Os dados são registros sintéticos que refletem o padrão do ano, com os funcionários identificados apenas por códigos aleatórios. Ela sabe que a comparação é observacional: quem recebeu respostas rápidas pode diferir dos demais, por exemplo por trabalhar em unidades próximas da TI.

### 30.2 Análise

O laboratório conta os reportes repetidos em dois grupos. Dos 40 funcionários cujo primeiro reporte recebeu resposta em até um dia, 26 reportaram de novo; dos 30 que receberam resposta tardia ou nenhuma, 9 reportaram de novo. Nadia calcula as proporções e um intervalo de Wilson para cada uma. Os intervalos não se sobrepõem, o que sugere uma diferença real, embora não necessariamente causal. Ela observa que o resultado é compatível com as entrevistas, o que reforça sua confiança de que o retorno importa. Os intervalos vão de 50% a 78% e de 17% a 48%. Ela confere as contagens duas vezes.

### Laboratório — Reportes repetidos após respostas rápidas e lentas

```python
# Repeat reporting after fast vs slow replies, with Wilson intervals (synthetic).
from math import sqrt
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h
for name, k, n in (("fast reply", 26, 40), ("slow or none", 9, 30)):
    lo, hi = wilson(k, n); print(f"{name}: {k}/{n} = {k / n:.0%} (95% CI {lo:.0%} to {hi:.0%})")
```

Execute com `python3 lab_reply.py`. Saída verificada:

```text
fast reply: 26/40 = 65% (95% CI 50% to 78%)
slow or none: 9/30 = 30% (95% CI 17% to 48%)
```

### 30.3 Recomendações

Nadia recomenda que a TI responda a todos os reportes em até um dia útil, usando modelos curtos para ganhar tempo, e que a caixa postal compartilhada seja monitorada pelas duas pessoas da TI, para evitar atrasos durante as férias. Ela sugere conferir a medida de novo depois de seis meses. Apresenta o resultado aos gestores como evidência a favor de uma mudança barata, com limites honestos quanto à causalidade. Os gestores aprovam os modelos, e a TI concorda em acompanhar os tempos de resposta como parte da revisão trimestral. Os modelos ficam prontos em uma semana.

### Exemplo resolvido

Nadia compara os reportes repetidos após respostas rápidas e lentas, encontra 65% contra 30% com intervalos que não se sobrepõem e recomenda respostas rápidas.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Dados observacionais não provam causalidade. Os grupos podem diferir.

### Exercícios

- **EX088 — Taxas dos grupos.** Que taxas de repetição os dois grupos mostraram? *Rubrica:* 3 = 65% após respostas rápidas e 30% após lentas ou nenhuma;; 2 = 26/40 e 9/30;; 1 = vago;; 0 = nenhuma.
- **EX089 — Resultado dos intervalos.** O que os intervalos mostraram? *Rubrica:* 3 = não se sobrepuseram;; 2 = separados;; 1 = sobreposição;; 0 = nenhuma.
- **EX090 — Cautela quanto à causalidade.** Por que o resultado não pode provar causalidade? *Rubrica:* 3 = os dados são observacionais e os grupos podem diferir;; 2 = observacionais;; 1 = vago;; 0 = nenhuma.

### Síntese

A análise observacional, lida com cautela, pode sustentar mudanças baratas baseadas em evidências.

<a id="ch-31"></a>

## Capítulo 31 — Fatores humanos e política cibernética: casos avançados

### Objetivos de aprendizagem

Você vai (1) analisar casos que envolvem pessoas internas, voluntários e o público; (2) pesar a segurança contra os valores do serviço; (3) desenhar respostas proporcionais.

### 31.1 Voluntários e pessoas internas

A Ashcombe conta com quarenta voluntários que ajudam em eventos e em grupos de apoio às tarefas escolares. Alguns precisam de acesso aos sistemas de reserva. Nadia analisa um caso sintético em que um voluntário compartilha o login de um funcionário para que um amigo possa reservar salas. A intenção é ajudar, e não prejudicar, mas isso contorna a responsabilização. Ela aprende que a maioria dos problemas com pessoas internas envolve conveniência e boa vontade, e não malícia. Tratar os voluntários como suspeitos prejudicaria relações das quais a biblioteca depende, por isso a resposta deve tratar a lacuna de conveniência sem presumir má intenção.

### 31.2 Segurança e valores do serviço

As bibliotecas valorizam a abertura, a privacidade e o acesso para todos. Os computadores públicos precisam ser fáceis de usar por pessoas com poucas habilidades digitais. Nadia examina uma proposta de exigir identificação para o uso dos computadores públicos, a fim de dissuadir o mau uso. Ela a pesa contra os valores da biblioteca: a identificação excluiria alguns usuários vulneráveis e criaria registros do que as pessoas fazem. Conclui que limites de tempo, limpeza automática das sessões e filtragem de malware na rede alcançam a maior parte dos objetivos de segurança sem prejudicar o acesso. As escolhas de segurança devem se ajustar à missão da organização que protegem.

### 31.3 Respostas proporcionais

Nadia desenvolve um princípio de proporcionalidade: as respostas devem corresponder ao risco e respeitar os papéis das pessoas. Para o caso do login compartilhado, ela propõe uma conta simples de voluntário, apenas com direitos de reserva, criada em até um dia após o pedido. Para os computadores públicos, mantém o modelo aberto com salvaguardas técnicas. Para os funcionários, aposta no apoio, e não na vigilância. A proporcionalidade evita reações exageradas depois de incidentes, que podem impor ônus pesados a todos por causa de um único evento, e mantém o programa alinhado aos valores da organização.

### Exemplo resolvido

Nadia analisa um caso de compartilhamento de login por um voluntário, pesa a identificação contra os valores da biblioteca e define respostas proporcionais.

> **Caso sintético.** Os casos são sintéticos.

### Erros e limites

A proporcionalidade exige julgamento. Modelos abertos carregam risco residual.

### Exercícios

- **EX091 — Motivação interna.** O que costuma motivar os problemas com pessoas internas, segundo o capítulo? *Rubrica:* 3 = conveniência e boa vontade, e não malícia;; 2 = conveniência;; 1 = malícia;; 0 = nenhuma.
- **EX092 — Identificação rejeitada.** Por que Nadia rejeitou a identificação nos computadores públicos? *Rubrica:* 3 = excluiria usuários vulneráveis e criaria registros;; 2 = acesso;; 1 = vago;; 0 = nenhuma.
- **EX093 — Correção para voluntários.** Que correção trata o login compartilhado? *Rubrica:* 3 = uma conta de voluntário apenas com direitos de reserva;; 2 = conta por função;; 1 = proibição;; 0 = nenhuma.

### Síntese

Respostas proporcionais ajustam o risco aos papéis e protegem a missão da organização.

<a id="ch-32"></a>

## Capítulo 32 — Fatores humanos e política cibernética: interfaces interdisciplinares

### Objetivos de aprendizagem

Você vai (1) trabalhar com as perspectivas do direito, da psicologia e da gestão; (2) traduzir entre disciplinas; (3) construir entendimento comum para as decisões.

### 32.1 Várias perspectivas

As decisões de segurança na Ashcombe envolvem várias disciplinas. A legislação de proteção de dados define deveres para os dados dos usuários. A psicologia explica por que os funcionários reagem à pressão como reagem. A gestão decide orçamentos e prioridades. A TI implementa os controles. Nadia aprende que cada disciplina usa sua própria linguagem: os juristas falam de bases legais e deveres, os psicólogos de normas e carga cognitiva, os gestores de custos e resultados. Um bom trabalho em fatores humanos envolve traduzir entre essas linguagens, para que as decisões se apoiem em todo o conhecimento relevante, e não numa única visão.

### 32.2 Traduzir

Nadia prepara um resumo de uma página sobre o risco de falsificação de identidade por telefone para cada público. Para o encarregado de privacidade, apresenta a regra de não revelação como proteção dos dados dos usuários e cumprimento dos deveres legais. Para os gestores, como redução de risco a quase nenhum custo. Para os funcionários, como proteção contra a pressão: eles nunca precisam julgar se quem liga é legítimo. A mesma regra, explicada nos termos de cada disciplina, ganha apoio com mais facilidade do que uma explicação única ganharia. Cada resumo cabe em uma página.

### 32.3 Entendimento comum

Nadia organiza uma reunião curta em que o encarregado de privacidade, um gestor, uma analista de TI e um representante dos funcionários discutem juntos o programa de reportes. Cada um explica suas preocupações. O encarregado de privacidade se preocupa com os logs; o gestor, com o custo; a TI, com a carga de trabalho; o representante, com a culpa. Ouvindo uns aos outros, eles concordam com um log minimizado, um orçamento modesto, respostas com modelos e uma declaração de não atribuição de culpa. Nadia aprende que o trabalho interdisciplinar muitas vezes tem menos a ver com especialização e mais com criar espaços em que as pessoas possam se entender.

### Exemplo resolvido

Nadia traduz a regra de não revelação para os públicos jurídico, gerencial e dos funcionários e convoca uma reunião que chega a acordos comuns.

> **Caso sintético.** A reunião é sintética.

### Erros e limites

A tradução pode simplificar demais. As reuniões podem ser dominadas pelas vozes mais seniores.

### Exercícios

- **EX094 — Enquadramento para os funcionários.** Como a regra foi apresentada aos funcionários? *Rubrica:* 3 = proteção contra a pressão de julgar quem liga;; 2 = alívio;; 1 = vago;; 0 = nenhuma.
- **EX095 — Preocupação do representante.** Com o que o representante dos funcionários se preocupava? *Rubrica:* 3 = a culpa;; 2 = culpa;; 1 = custo;; 0 = nenhuma.
- **EX096 — Resultado da reunião.** Com o que a reunião concordou? *Rubrica:* 3 = log minimizado, orçamento modesto, modelos e declaração de não atribuição de culpa;; 2 = quatro;; 1 = vago;; 0 = nenhuma.

### Síntese

O trabalho com fatores humanos traduz entre disciplinas e cria entendimento compartilhado.

<a id="ch-33"></a>

## Capítulo 33 — Métodos de pesquisa II

### Objetivos de aprendizagem

Você vai (1) desenhar um pequeno estudo comparativo; (2) considerar confiabilidade e validade; (3) planejar a análise antes de coletar os dados.

### 33.1 Desenho comparativo

Para o último ano, Nadia planeja comparar a Ashcombe com outra rede de bibliotecas fictícia, a Dunmore Libraries, que tem um programa guiado pela conformidade, com treinamento anual e simulações mensais. Sua pergunta é se a abordagem centrada em reportes da Ashcombe está associada a reportes mais rápidos de e-mails suspeitos reais do que a abordagem da Dunmore. Ela planeja coletar dados anonimizados de reporte e aplicar o mesmo questionário curto nas duas redes. Um desenho comparativo não pode provar causalidade, mas pode mostrar se as diferenças são grandes o bastante para merecer mais atenção.

### 33.2 Confiabilidade e validade

Confiabilidade significa que uma medida dá resultados consistentes; validade significa que ela mede o que deveria. Nadia confere se as duas redes definem os reportes da mesma forma e se suas equipes de TI registram os tempos de modo semelhante. Ela usa a mesma redação no questionário. Observa as ameaças à validade: as redes diferem em tamanho, localização e nos ataques que recebem. Planeja descrever essas diferenças abertamente, em vez de ignorá-las, e tratar qualquer achado como um indício, e não como uma conclusão sobre qual programa é melhor.

### 33.3 Planejar a análise

Antes de coletar os dados, Nadia escreve seu plano de análise: comparar a mediana do tempo até o primeiro reporte, comparar a proporção de e-mails maliciosos reais que foram reportados e comparar as pontuações do questionário em confiança e medo de culpa. Ela especifica quais testes usará e declara que diferença consideraria relevante. Escrever o plano primeiro a impede de vasculhar os dados atrás de qualquer resultado que pareça interessante. O Dr. Prescott aprova o plano, e as duas redes concordam em compartilhar dados anonimizados sob um acordo de compartilhamento de dados. O plano tem duas páginas.

### Exemplo resolvido

Nadia desenha uma comparação entre a Ashcombe e a Dunmore, trata a confiabilidade e a validade e escreve um plano de análise de antemão.

> **Caso sintético.** As duas redes são sintéticas.

### Erros e limites

Comparações entre organizações sofrem com fatores de confusão. As práticas de registro diferem.

### Exercícios

- **EX097 — Abordagem da Dunmore.** Que abordagem a Dunmore usa? *Rubrica:* 3 = treinamento anual e simulações mensais;; 2 = guiada pela conformidade;; 1 = guiada pelo reporte;; 0 = nenhuma.
- **EX098 — Definição de confiabilidade.** O que significa confiabilidade? *Rubrica:* 3 = resultados consistentes de uma medida;; 2 = consistência;; 1 = validade;; 0 = nenhuma.
- **EX099 — O plano primeiro.** Por que escrever o plano de análise antes dos dados? *Rubrica:* 3 = para evitar vasculhar os dados atrás de resultados interessantes;; 2 = planejamento prévio;; 1 = vago;; 0 = nenhuma.

### Síntese

Estudos comparativos precisam de medidas consistentes, ameaças declaradas abertamente e análise planejada de antemão.

<a id="ch-34"></a>

## Capítulo 34 — Projeto comparativo

### Objetivos de aprendizagem

Você vai (1) conduzir uma comparação com as medidas planejadas; (2) interpretar as diferenças com cuidado; (3) apresentar conclusões equilibradas.

### 34.1 Coletar os dados

Nadia coleta seis meses de dados anonimizados das duas redes. Na Ashcombe, 22 e-mails maliciosos chegaram aos funcionários; na Dunmore, com 150 funcionários, 27. Para cada um, ela registra o tempo até o primeiro reporte ou anota que nunca foi reportado. Também aplica o questionário nas duas redes, recebendo 82 respostas na Ashcombe e 95 na Dunmore. Ela guarda os dados numa pasta protegida, confere se há erros comparando os totais com os resumos da TI e registra cada decisão sobre itens excluídos ou pouco claros. Ela anota cada exclusão num caderno.

### 34.2 Comparar os resultados

O laboratório calcula a mediana do tempo até o primeiro reporte e a proporção de e-mails maliciosos reportados em cada rede. A Ashcombe mostra uma mediana de tempo menor e uma proporção reportada maior. As pontuações do questionário mostram mais confiança e menos medo de culpa na Ashcombe. Nadia observa que as taxas de clique da Dunmore nas simulações são baixas, o que seus gestores citam como sucesso, mas seus funcionários reportam ataques reais lentamente. Isso sugere que taxas de clique baixas e reportes rápidos são coisas diferentes, um ponto que ela discute com cuidado.

### Laboratório — Resultados de reporte em duas redes de bibliotecas

```python
# Reporting outcomes at two synthetic library networks over six months.
ash = [3, 5, 6, 8, 9, 10, 11, 12, 12, 14, 15, 18, 21, 25, 30, 38, 44, 52, 66] + [None] * 3
dun = [9, 15, 22, 30, 41, 47, 55, 70, 88, 120, 150, 180, 240, 300] + [None] * 13
for name, d in (("Ashcombe", ash), ("Dunmore", dun)):
    t = sorted(x for x in d if x is not None)
    print(f"{name}: {len(d)} malicious, reported {len(t)} ({len(t) / len(d):.0%}), median first report {t[len(t) // 2]} min")
```

Execute com `python3 lab_networks.py`. Saída verificada:

```text
Ashcombe: 22 malicious, reported 19 (86%), median first report 14 min
Dunmore: 27 malicious, reported 14 (52%), median first report 70 min
```

### 34.3 Conclusões equilibradas

Nadia conclui que a abordagem da Ashcombe está associada a reportes mais rápidos e a mais confiança dos funcionários, mas não afirma que ela causou essas diferenças. Os funcionários da Dunmore podem enfrentar ataques diferentes, e seu programa tem pontos fortes, como a prática regular. Ela sugere que a Dunmore poderia ganhar acrescentando retorno rápido e uma mensagem de não atribuição de culpa, e que a Ashcombe poderia aprender com as reciclagens regulares da Dunmore. Conclusões equilibradas respeitam as duas organizações e têm mais chance de ser postas em prática do que afirmações de que uma abordagem é simplesmente a certa.

### Exemplo resolvido

Nadia compara duas redes, encontra reportes mais rápidos e mais confiança na Ashcombe e tira conclusões equilibradas.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Seis meses é pouco tempo. As redes enfrentam ataques diferentes.

### Exercícios

- **EX100 — Medianas no laboratório.** Que medianas de tempo até o primeiro reporte o laboratório mostrou? *Rubrica:* 3 = Ashcombe 14 e Dunmore 70 minutos;; 2 = mais rápido;; 1 = vago;; 0 = nenhuma.
- **EX101 — Proporção reportada.** Que proporções dos e-mails maliciosos foram reportadas? *Rubrica:* 3 = Ashcombe 86% e Dunmore 52%;; 2 = maior;; 1 = vago;; 0 = nenhuma.
- **EX102 — Clique versus reporte.** O que os resultados da Dunmore sugerem? *Rubrica:* 3 = cliques baixos e reportes rápidos são diferentes;; 2 = diferentes;; 1 = iguais;; 0 = nenhuma.

### Síntese

As comparações devem ser interpretadas com cautela e concluídas com equilíbrio.

<a id="ch-35"></a>

## Capítulo 35 — Proposta de trabalho de conclusão

### Objetivos de aprendizagem

Você vai (1) escolher um problema para o trabalho de conclusão a partir de achados anteriores; (2) escrever objetivos e critérios de sucesso; (3) planejar recursos e ética.

### 35.1 Escolher o problema

Para o trabalho de conclusão, Nadia escolhe uma lacuna encontrada antes: voluntários e funcionários de meio período, que trabalham em horários irregulares, muitas vezes ficam de fora das reciclagens dadas nas reuniões de equipe e raramente reportam. Seu problema é como incluí-los no programa de reportes de um jeito que combine com seus padrões de trabalho e com sua relação com a biblioteca. Ela escolhe esse tema porque ele se apoia em seus achados anteriores, importa para a Ashcombe e é viável em um ano letivo com recursos modestos. O Dr. Prescott concorda com a escolha.

### 35.2 Objetivos e critérios

Nadia define três objetivos: desenhar um guia de boas-vindas curto para voluntários e funcionários de meio período; oferecer uma via de reporte simples que funcione sem conta de e-mail de funcionário; e avaliar se os reportes e a confiança melhoram. Os critérios de sucesso são que pelo menos dois terços dos voluntários recebam o guia, que os reportes dos voluntários aumentem e que as pontuações de confiança subam num questionário curto. Ela define de antemão que, se menos da metade receber o guia, revisará a distribuição antes de avaliar. Cada critério tem uma data.

### 35.3 Recursos e ética

Nadia lista os recursos: seu tempo, o apoio da coordenadora de voluntários, impressão e algumas horas da TI para um formulário web. Ela busca aprovação ética para questionários e entrevistas breves com voluntários, observando que eles podem se sentir obrigados a participar; ela enfatiza que a participação é voluntária e não tem ligação com suas funções. Planeja guardar os dados sem nomes. Planejar recursos e ética cedo evita os atrasos que costumam afetar os trabalhos de conclusão no fim do ano. A coordenadora concorda em ajudar na distribuição.

### Exemplo resolvido

Nadia escolhe um trabalho de conclusão sobre a inclusão de voluntários, define objetivos e critérios com uma regra de revisão predefinida e planeja recursos e ética.

> **Caso sintético.** O trabalho de conclusão é sintético.

### Erros e limites

O número de voluntários oscila. Amostras pequenas limitam a avaliação.

### Exercícios

- **EX103 — Grupo do trabalho.** Que grupo o trabalho de conclusão trata? *Rubrica:* 3 = voluntários e funcionários de meio período;; 2 = voluntários;; 1 = vago;; 0 = nenhuma.
- **EX104 — Critério do guia.** Que proporção dos voluntários deve receber o guia? *Rubrica:* 3 = pelo menos dois terços;; 2 = dois terços;; 1 = metade;; 0 = nenhuma.
- **EX105 — Preocupação com obrigação.** Que preocupação ética se aplica aos voluntários? *Rubrica:* 3 = podem se sentir obrigados a participar;; 2 = pressão;; 1 = vago;; 0 = nenhuma.

### Síntese

Uma proposta de projeto final parte das descobertas, define objetivos mensuráveis e planeja a ética desde cedo.

<a id="ch-36"></a>

## Capítulo 36 — Prática de campo ou comunitária

### Objetivos de aprendizagem

Você vai (1) trabalhar com voluntários e com o público num contexto comunitário; (2) oferecer orientações de segurança com respeito; (3) aprender com o retorno da comunidade.

### 36.1 Contexto comunitário

Nadia passa seis semanas trabalhando ao lado da coordenadora de voluntários da Ashcombe. Ela participa dos grupos de apoio às tarefas escolares e das sessões de ajuda digital, em que os voluntários apoiam os usuários em tarefas como criar um e-mail ou solicitar serviços online. Ela vê que os voluntários muitas vezes recebem perguntas de segurança dos usuários, como se uma mensagem de um banco é legítima. Trabalhar na comunidade lhe mostra que o comportamento de segurança vai além dos funcionários e alcança as pessoas que a biblioteca atende, e que os voluntários atuam como conselheiros informais de segurança online.

### 36.2 Orientação respeitosa

Nadia elabora com os voluntários um guia de uma página para ajudar os usuários: nunca lidar com as senhas de um usuário, incentivar os usuários a contatar as organizações pelos números oficiais e sugerir que golpes sejam denunciados pelos canais nacionais. Ela evita linguagem técnica e exemplos assustadores, concentrando-se em passos práticos e tranquilos. Os voluntários testam o guia nas sessões e sugerem uma redação mais simples. Ela observa que as diretrizes de cultura de cibersegurança da ENISA enfatizam entender o público, e que uma orientação respeitosa constrói a confiança dos usuários, em vez de fazê-los se sentir tolos por não saber. Os voluntários gostam do guia.

### 36.3 Retorno da comunidade

Usuários e voluntários dão retorno por meio de conversas curtas e de uma caixa de comentários. Vários usuários dizem que o guia os ajudou a sentir menos ansiedade com os serviços online. Os voluntários pedem uma sessão curta sobre como reconhecer SMS de golpe, que Nadia organiza com a TI. Uma usuária mais velha comenta que os alertas sobre golpes a deixaram com medo de usar o banco pela internet. Nadia registra isso como um lembrete de que o medo pode reduzir o uso seguro e útil da tecnologia, e revisa o guia para incluir passos positivos, e não apenas alertas.

### Exemplo resolvido

Nadia trabalha em sessões comunitárias, elabora com os voluntários um guia respeitoso e o revisa depois de um retorno sobre o medo.

> **Caso sintético.** A prática é sintética; as diretrizes da ENISA são reais.

### Erros e limites

O retorno informal não é representativo. Os voluntários variam em confiança.

### Exercícios

- **EX106 — Papel dos voluntários.** Que papel informal os voluntários desempenham? *Rubrica:* 3 = conselheiros de segurança online para os usuários;; 2 = conselheiros;; 1 = vago;; 0 = nenhuma.
- **EX107 — Regra das senhas.** O que os voluntários nunca devem fazer? *Rubrica:* 3 = lidar com as senhas de um usuário;; 2 = senhas;; 1 = vago;; 0 = nenhuma.
- **EX108 — Lição sobre o medo.** O que o comentário da usuária mais velha mostrou? *Rubrica:* 3 = o medo pode reduzir o uso seguro e útil da tecnologia;; 2 = medo;; 1 = vago;; 0 = nenhuma.

### Síntese

A prática comunitária estende as orientações de segurança ao público com respeito e atenção ao medo.

<a id="ch-37"></a>

## Capítulo 37 — Seminário de revisão de evidências

### Objetivos de aprendizagem

Você vai (1) revisar as evidências sobre a eficácia do treinamento de conscientização; (2) avaliar a qualidade dos estudos; (3) resumir o que se sabe e o que não se sabe.

### 37.1 Revisar as evidências

Num seminário, Nadia e os colegas revisam as evidências publicadas sobre se o treinamento de conscientização e as simulações funcionam. Eles leem Bada, Sasse e Nurse (2019) sobre por que as campanhas falham, Lain, Kostiainen e Čapkun (2022) sobre um grande estudo organizacional de phishing e a NIST SP 800-50r1 sobre o desenho de programas. Observam que muitas afirmações de fornecedores não têm evidência independente. Revisar as evidências os ajuda a não repetir crenças populares e, em vez disso, basear as recomendações em estudos cujos métodos podem examinar e julgar. Cada estudante apresenta um artigo ao grupo e conduz dez minutos de discussão.

### 37.2 Avaliar a qualidade

O grupo avalia a qualidade dos estudos com perguntas simples: quantos participantes, havia grupo de comparação, como os resultados foram medidos e quem financiou o estudo. Lain e colegas estudaram milhares de funcionários por mais de um ano, o que dá peso a seus achados; eles constataram que o treinamento embutido após os cliques não melhorou os resultados, enquanto os funcionários, coletivamente, reportaram muitos e-mails de phishing. Estudos pequenos, sem grupo de comparação ou financiados por fornecedores, recebem menos peso. A avaliação de qualidade os ajuda a pesar afirmações conflitantes de forma sensata.

### 37.3 O que se sabe

O grupo resume: as evidências sugerem que campanhas baseadas no medo e longos treinamentos após o clique são fracos; que o reporte por muitos funcionários pode detectar ataques rapidamente; e que o design usável reduz o ônus. Sabe-se menos sobre os efeitos de longo prazo do retorno ou sobre organizações pequenas como as bibliotecas. Nadia observa que seu próprio trabalho na Ashcombe acrescenta um pequeno caso a essa lacuna. Uma declaração clara do que se sabe e do que não se sabe orienta tanto a prática quanto a pesquisa futura, e protege contra afirmações excessivamente confiantes. O resumo cabe em uma página.

### Exemplo resolvido

O seminário de Nadia revisa estudos-chave, avalia sua qualidade e resume os pontos conhecidos e desconhecidos.

> **Caso sintético.** O seminário é sintético; Bada et al. (2019), Lain et al. (2022) e a SP 800-50r1 são reais.

### Erros e limites

As revisões podem deixar estudos de fora. As perguntas de qualidade são simples.

### Exercícios

- **EX109 — Achado de Lain.** O que Lain et al. constataram sobre o treinamento embutido? *Rubrica:* 3 = não melhorou os resultados;; 2 = ineficaz;; 1 = ajudou;; 0 = nenhuma.
- **EX110 — Perguntas de qualidade.** Cite duas perguntas de qualidade usadas. *Rubrica:* 3 = número de participantes e grupo de comparação;; 2 = duas;; 1 = vago;; 0 = nenhuma.
- **EX111 — Lacuna conhecida.** O que se sabe menos? *Rubrica:* 3 = efeitos de longo prazo do retorno e organizações pequenas;; 2 = lacuna;; 1 = vago;; 0 = nenhuma.

### Síntese

A revisão de evidências pesa a qualidade dos estudos e declara o que se sabe e o que não se sabe.

<a id="ch-38"></a>

## Capítulo 38 — Implementação do trabalho de conclusão

### Objetivos de aprendizagem

Você vai (1) implementar o guia para voluntários e a via de reporte; (2) gerir a distribuição; (3) adaptar-se durante a implementação.

### 38.1 Construir as peças

Nadia escreve o guia de boas-vindas para voluntários e funcionários de meio período: como são as mensagens suspeitas, as três perguntas a fazer, como reportar e a promessa de que os reportes são bem-vindos e nunca levam a culpa. A TI constrói um formulário web simples que qualquer pessoa com um código de voluntário pode usar a partir de qualquer dispositivo, enviando os reportes para a caixa postal compartilhada. Ela testa o formulário com cinco voluntários, que o acham fácil, e corrige um rótulo confuso antes do lançamento. O guia tem duas páginas.

### 38.2 Distribuição

O guia é entregue pela coordenadora de voluntários na integração e enviado por um link via SMS aos voluntários já existentes. Os funcionários de meio período o recebem junto com o contracheque. Nadia acompanha a distribuição com uma contagem simples dos guias entregues por unidade, e não por nomes. Depois de quatro semanas, 31 de 40 voluntários e 18 de 22 funcionários de meio período receberam o guia, o que atende a seu critério de dois terços. Acompanhar por contagens respeita a privacidade e, ao mesmo tempo, mostra se o guia chegou às pessoas. A coordenadora mantém a planilha de contagem atualizada.

### 38.3 Adaptar

Durante a implementação, os voluntários de uma unidade dizem que raramente olham o celular durante as sessões, por isso o link por SMS é ignorado. Nadia providencia guias impressos para ficarem naquela unidade. A TI percebe que alguns reportes do formulário contêm dados pessoais de usuários, que os voluntários incluíram para explicar o contexto; o formulário é atualizado com uma nota pedindo que as pessoas não incluam dados pessoais. Adaptar-se durante a implementação é normal e fica registrado, para que a avaliação final reflita o que de fato foi feito. As duas mudanças são registradas.

### Exemplo resolvido

Nadia constrói um guia e um formulário web, os distribui a 49 de 62 pessoas e se adapta a uma unidade e aos dados pessoais nos reportes.

> **Caso sintético.** A implementação é sintética.

### Erros e limites

Contagens não mostram a leitura. Formulários podem ser mal utilizados.

### Exercícios

- **EX112 — Acesso ao formulário.** Como os voluntários acessam o formulário? *Rubrica:* 3 = com um código de voluntário, a partir de qualquer dispositivo;; 2 = código;; 1 = e-mail de funcionário;; 0 = nenhuma.
- **EX113 — Proporção da distribuição.** Que proporção dos voluntários recebeu o guia? *Rubrica:* 3 = 31 de 40, cerca de 78%;; 2 = 78%;; 1 = vago;; 0 = nenhuma.
- **EX114 — Mudança no formulário.** Por que o formulário foi atualizado? *Rubrica:* 3 = os reportes incluíam dados pessoais de usuários;; 2 = privacidade;; 1 = vago;; 0 = nenhuma.

### Síntese

A implementação constrói, distribui e adapta, com cada mudança registrada.

<a id="ch-39"></a>

## Capítulo 39 — Avaliação do trabalho de conclusão

### Objetivos de aprendizagem

Você vai (1) avaliar o trabalho de conclusão em relação aos critérios; (2) analisar pequenas amostras de antes e depois; (3) relatar com honestidade.

### 39.1 Dados de avaliação

Nadia compara os três meses anteriores e os três meses posteriores ao guia. Antes, voluntários e funcionários de meio período fizeram 4 reportes; depois, 15. Ela também aplica um questionário, recebendo 34 respostas antes e 37 depois, perguntando se saberiam como reportar uma mensagem suspeita e se teriam receio de ser culpados. Ela observa que pessoas diferentes responderam a cada questionário, já que os voluntários mudam, de modo que a comparação é entre grupos, e não entre indivíduos. O questionário leva três minutos, é anônimo e não faz perguntas sobre dados pessoais, para que os voluntários possam responder rapidamente no fim de uma sessão.

### 39.2 Analisar as amostras

O laboratório calcula a proporção que respondeu sim à pergunta sobre saber como reportar, antes e depois, com intervalos de Wilson. O conhecimento subiu claramente. O receio de culpa caiu, embora os intervalos tenham se sobreposto. Os reportes subiram de 4 para 15, mas, com contagens pequenas e possíveis efeitos sazonais, como mais sessões no outono, ela trata o aumento como encorajador, e não conclusivo. Os três critérios de sucesso são atendidos, de modo que a regra de revisão predefinida não é acionada e o programa continua. O conhecimento subiu de 41% para 81%. O receio caiu de 35% para 19%.

### Laboratório — Saber como reportar, antes e depois

```python
# Knowing how to report: before and after the guide, Wilson intervals (synthetic).
from math import sqrt
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h
for name, k, n in (("know before", 14, 34), ("know after", 30, 37), ("worry before", 12, 34), ("worry after", 7, 37)):
    lo, hi = wilson(k, n); print(f"{name}: {k}/{n} = {k / n:.0%} (95% CI {lo:.0%} to {hi:.0%})")
```

Execute com `python3 lab_capstone.py`. Saída verificada:

```text
know before: 14/34 = 41% (95% CI 26% to 58%)
know after: 30/37 = 81% (95% CI 66% to 91%)
worry before: 12/34 = 35% (95% CI 21% to 52%)
worry after: 7/37 = 19% (95% CI 9% to 34%)
```

### 39.3 Relato honesto

Nadia escreve seu relatório de avaliação com resultados, limites e recomendações. Ela observa que os grupos do questionário diferem, que efeitos sazonais podem explicar parte da mudança e que saber como reportar não é o mesmo que reportar. Recomenda manter o guia e o formulário, acrescentar um lembrete anual curto e conferir de novo em um ano. O Dr. Prescott elogia o relatório por não exagerar nem descartar os resultados, que é o equilíbrio que uma boa avaliação exige. Os gestores aceitam todas as recomendações. O relatório é compartilhado com os funcionários.

### Exemplo resolvido

Nadia avalia seu trabalho de conclusão, constata que o conhecimento subiu de 41% para 81% e os reportes aumentaram de 4 para 15, e relata os limites com honestidade.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Respondentes diferentes antes e depois. Efeitos sazonais.

### Exercícios

- **EX115 — Contagem de reportes.** Como mudaram os reportes de voluntários e funcionários de meio período? *Rubrica:* 3 = de 4 para 15;; 2 = aumento;; 1 = vago;; 0 = nenhuma.
- **EX116 — Proporções de conhecimento.** Que proporções sabiam como reportar antes e depois, no laboratório? *Rubrica:* 3 = 41% e 81%;; 2 = aumento;; 1 = vago;; 0 = nenhuma.
- **EX117 — Cautela com os grupos.** Por que a comparação do questionário é entre grupos? *Rubrica:* 3 = os voluntários mudaram entre os questionários;; 2 = rotatividade;; 1 = vago;; 0 = nenhuma.

### Síntese

As avaliações comparam com critérios, analisam amostras pequenas com cuidado e relatam os limites.

<a id="ch-40"></a>

## Capítulo 40 — Tese e apresentação

### Objetivos de aprendizagem

Você vai (1) estruturar uma monografia de bacharelado; (2) apresentar os achados a um público acadêmico e profissional; (3) refletir sobre a aprendizagem.

### 40.1 Estrutura da tese

A tese de Nadia, "Fazendo o reporte funcionar numa rede pública de bibliotecas", tem capítulos sobre contexto e literatura, métodos, o estudo de reportes, o projeto comparativo, o trabalho de conclusão com voluntários e as conclusões. Cada capítulo declara sua pergunta, métodos, achados e limites. Ela cita fontes que conferiu, como Adams e Sasse (1999), Sasse, Brostoff e Weirich (2001), Herley (2009) e Lain, Kostiainen e Čapkun (2022), e mantém todos os dados do caso sintéticos ou anonimizados. Os apêndices trazem seu código, o questionário e as aprovações éticas. A tese tem sessenta páginas. Cada apêndice é indexado.

### 40.2 Apresentação

Nadia apresenta aos examinadores e aos gestores da Ashcombe em quinze minutos. Começa pelo problema dos reportes lentos, mostra o modelo de funil, o efeito do retorno, a comparação com a Dunmore e os resultados do trabalho de conclusão. Um gestor pergunta se as simulações deveriam aumentar; ela responde que as evidências favorecem o retorno rápido e o reporte fácil, com simulações usadas com parcimônia sob regras acordadas. Um examinador pergunta sobre generalização; ela reconhece que seu trabalho trata de uma única rede e sugere estudos semelhantes em outros lugares. Os gestores pedem uma cópia.

### 40.3 Reflexão

Nadia reflete sobre o que aprendeu: que os problemas de segurança muitas vezes estão nos sistemas, e não nas pessoas; que pequenas mudanças de design e um retorno gentil podem importar mais do que palestras; e que limites declarados com honestidade tornam os achados mais confiáveis. Ela observa como sua visão mudou desde o primeiro ensaio, quando ainda acreditava pela metade que os funcionários eram o elo mais fraco. Planeja seguir numa função de segurança, levando o hábito de perguntar o que o sistema exige das pessoas antes de julgar como elas reagem. Ela escreve a reflexão em uma página.

### Exemplo resolvido

Nadia estrutura sua tese, apresenta aos examinadores e gestores, responde perguntas sobre simulações e generalização e reflete sobre sua aprendizagem.

> **Caso sintético.** A tese é sintética; as obras citadas são reais.

### Erros e limites

Um único caso limita a generalização. A reflexão pode ser seletiva.

### Exercícios

- **EX118 — Resposta sobre simulações.** Como Nadia respondeu à pergunta sobre simulações? *Rubrica:* 3 = favorecer o retorno e o reporte fácil, simulações com parcimônia;; 2 = parcimônia;; 1 = mais simulações;; 0 = nenhuma.
- **EX119 — Resposta sobre generalização.** Como Nadia respondeu sobre generalização? *Rubrica:* 3 = uma única rede, sugere estudos em outros lugares;; 2 = limites;; 1 = vago;; 0 = nenhuma.
- **EX120 — Visão que mudou.** Como a visão de Nadia mudou desde o primeiro ensaio? *Rubrica:* 3 = de acreditar pela metade que os funcionários são o elo mais fraco a olhar para os sistemas;; 2 = sistemas;; 1 = vago;; 0 = nenhuma.

### Síntese

Uma tese conecta perguntas, métodos e descobertas honestas, e a reflexão mostra o crescimento.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX120. Nadia Farouk, o Dr. Owen Prescott, a Fenmoor University, a Ashcombe Community Library Network, a Dunmore Libraries e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX031.** É impossível saber quem fez o quê.

**EX032.** A disposição limitada das pessoas para gastar esforço com tarefas de segurança.

**EX033.** Dos funcionários, individualmente, para um processo automático noturno.

**EX034.** Cerca de 9,7% a 22,5%.

**EX035.** Porque os intervalos se sobrepõem bastante, de modo que a diferença pode ser acaso.

**EX036.** Vinte funcionários, ou a combinação de unidades pequenas.

**EX037.** Algo que você sabe, algo que você tem e algo que você é.

**EX038.** A maioria acrescenta um número à senha antiga.

**EX039.** Porque verificam se o site é legítimo antes de responder.

**EX040.** A privacidade também limita o que as pessoas autorizadas podem fazer com os dados.

**EX041.** Nunca revelar informações de usuários por telefone e encaminhar os pedidos por escrito ao encarregado de privacidade.

**EX042.** Porque funcionários que temem o mau uso param de reportar, de modo que a privacidade constrói confiança.

**EX043.** Porque mostram que as pessoas terminaram um módulo, e não que se comportam com segurança.

**EX044.** 14 minutos.

**EX045.** Porque o esforço de segurança é um custo real, e esgotar os funcionários não é sustentável.

**EX046.** Que os mecanismos de proteção devem ser fáceis de usar corretamente.

**EX047.** Reportando e-mails suspeitos que os filtros deixam passar, atuando como sensores.

**EX048.** O segundo fator de autenticação.

**EX049.** Quem enviou a mensagem e que ela não foi alterada.

**EX050.** A maioria dos participantes não conseguiu usar o programa corretamente em noventa minutos.

**EX051.** Porque pedir aos funcionários que criptografem anexos manualmente é propenso a erros.

**EX052.** O que impede os atendentes de balcão de reportar e-mails suspeitos em até uma hora?

**EX053.** Porque levantaria preocupações éticas sem consentimento.

**EX054.** Para verificar se as perguntas estão claras antes do questionário principal.

**EX055.** De culpar os usuários a projetar a segurança em torno deles.

**EX056.** Atitudes, normas sociais e controle comportamental percebido.

**EX057.** Que o comportamento depende de quão fácil e valiosa a ação segura parece.

**EX058.** Autoridade, por um suposto cargo na prefeitura, e urgência, por um prazo.

**EX059.** No sistema, como a falta de procedimentos, e não na pessoa.

**EX060.** Verifica qualquer pedido oficial antes que dados sejam compartilhados.

**EX061.** Porque qualquer etapa fraca pode impedir que um alerta chegue à TI.

**EX062.** Cerca de 24 de cada 100.

**EX063.** A etapa de decisão, em que os funcionários escolhem se vão se dar ao trabalho.

**EX064.** Poderia revelar quem reportou o quê e desestimular os reportes.

**EX065.** Uma única analista de TI trata a maioria dos reportes pela caixa de entrada pessoal dela.

**EX066.** Avisa a quem reportou que o reporte chegou.

**EX067.** 70%, já que 84 de 120 funcionários responderam.

**EX068.** A dúvida sobre se um e-mail era suspeito o suficiente, escolhida por 45 de 84 (54%).

**EX069.** Para verificar e melhorar a consistência da codificação.

**EX070.** A TI responde a todos os reportes em até um dia útil, com um veredito.

**EX071.** Devem ser transparentes, fáceis de ignorar e nunca manipular pelo medo.

**EX072.** Depois de três meses.

**EX073.** Para que nenhuma caixa de entrada ou e-mail real seja envolvido.

**EX074.** Cerca de 40 segundos para o encaminhamento e 6 segundos para o botão.

**EX075.** Dois, porque digitaram o endereço errado.

**EX076.** De 12 para 31 por mês.

**EX077.** Os e-mails maliciosos subiram de 3 para 5 por mês.

**EX078.** Unidades adiantadas, 26, e atrasadas, 8 reportes por cem funcionários.

**EX079.** Se o reporte melhorou; ela confere apenas se os controles funcionam.

**EX080.** O botão estava escondido atrás de um menu por causa de uma configuração de tela.

**EX081.** Seis; duas foram corrigidas e testadas de novo.

**EX082.** Revelam fraquezas sem causar danos.

**EX083.** Fatores organizacionais, presentes em todos os cinco quase incidentes.

**EX084.** Recomendou transformar o hábito de verificar por telefone numa regra escrita.

**EX085.** No máximo duas vezes por ano, sob regras acordadas.

**EX086.** Para que os resultados possam ser comparados entre anos.

**EX087.** É retirado.

**EX088.** 65% (26 de 40) após respostas rápidas e 30% (9 de 30) após respostas lentas ou nenhuma.

**EX089.** Não se sobrepuseram, o que sugere uma diferença real.

**EX090.** Porque os dados são observacionais e os grupos podem diferir em outros aspectos.

**EX091.** Conveniência e boa vontade, e não malícia.

**EX092.** Porque excluiria usuários vulneráveis e criaria registros de suas atividades.

**EX093.** Uma conta de voluntário apenas com direitos de reserva, criada rapidamente.

**EX094.** Como proteção contra ter de julgar se quem liga é legítimo.

**EX095.** Ser culpado por erros.

**EX096.** Um log minimizado, um orçamento modesto, respostas com modelos e uma declaração de não atribuição de culpa.

**EX097.** Um programa guiado pela conformidade, com treinamento anual e simulações mensais.

**EX098.** Que uma medida dá resultados consistentes.

**EX099.** Para evitar vasculhar os dados atrás de qualquer resultado que pareça interessante.

**EX100.** 14 minutos na Ashcombe e 70 minutos na Dunmore.

**EX101.** 86% na Ashcombe e 52% na Dunmore.

**EX102.** Que taxas de clique baixas em simulações e reportes rápidos de ataques reais são coisas diferentes.

**EX103.** Voluntários e funcionários de meio período.

**EX104.** Pelo menos dois terços.

**EX105.** Que podem se sentir obrigados a participar.

**EX106.** Conselheiros informais dos usuários sobre segurança online.

**EX107.** Lidar com as senhas de um usuário.

**EX108.** Que alertas baseados no medo podem fazer as pessoas deixarem de usar serviços úteis.

**EX109.** Que o treinamento embutido após os cliques não melhorou os resultados.

**EX110.** Exemplos incluem o número de participantes, grupos de comparação, medidas de resultado e financiamento.

**EX111.** Os efeitos de longo prazo do retorno e os resultados em organizações pequenas.

**EX112.** Com um código de voluntário, a partir de qualquer dispositivo.

**EX113.** 31 de 40 voluntários, cerca de 78%.

**EX114.** Porque alguns reportes incluíam dados pessoais de usuários.

**EX115.** De 4, nos três meses anteriores, para 15 depois.

**EX116.** 41% (14 de 34) antes e 81% (30 de 37) depois.

**EX117.** Porque pessoas diferentes responderam a cada questionário, à medida que os voluntários mudaram.

**EX118.** Que as evidências favorecem o retorno rápido e o reporte fácil, com simulações usadas com parcimônia sob regras acordadas.

**EX119.** Ela reconheceu que o trabalho trata de uma única rede e sugeriu estudos em outros lugares.

**EX120.** Ela passou de acreditar pela metade que os funcionários eram o elo mais fraco a examinar o que os sistemas exigem das pessoas.

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
