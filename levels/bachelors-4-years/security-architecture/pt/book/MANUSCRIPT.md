# Arquitetura e Engenharia de Segurança: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 099, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–40 de 40 têm texto didático escrito à mão; os exercícios EX001–EX120 têm resoluções correspondentes com rubricas de 0 a 3; os dez laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: estudantes de graduação que aprendem a projetar, avaliar e operar a arquitetura de segurança de organizações reais.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios avaliam lógica, buscam caminhos de ataque, calculam intervalos amostrais, pseudonimizam, medem cobertura, contam dependências, verificam o menor privilégio, ajustam uma regra de detecção, estimam uma diferença em diferenças e ponderam opções, tudo sobre dados sintéticos; nada toca um sistema real. Projetos de produção usam produtos e padrões consagrados; nunca crie sua própria criptografia. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um estudante de graduação em estágio numa pequena cooperativa de varejo: fundamentos de matemática, computação, redes, dados, probabilidade e privacidade; conceitos de medição, arquitetura e criptografia; métodos de pesquisa; a sequência central de arquitetura e engenharia de segurança, com dois laboratórios; casos avançados e interdisciplinares; e o trabalho de conclusão, a prática de campo, a revisão de evidências e a tese. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Lucas Haddon** | Estudante de graduação | Inventado |
| **Dr. Marco Bellini** | Tutor | Inventado |
| **Hannah Osei** | Líder de segurança de TI da cooperativa | Inventada |
| **Ashgrove University** | Universidade fictícia | Inventada |
| **Fernway Outdoor Co-operative** | Varejista fictícia de artigos para atividades ao ar livre | Inventada |

### Fontes principais

Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Anderson, *Security Engineering* 3e (2020); Shostack, *Threat Modeling* (2014); Sherwood, Clark e Lynas, *Enterprise Security Architecture* (SABSA, 2005); NIST [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5) e [SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1); ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) e 27002:2022. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem

Você vai (1) expressar políticas de segurança como enunciados lógicos; (2) testar uma política com uma tabela-verdade; (3) identificar contradições e lacunas em regras escritas.

### 1.1 O caso e a lógica

Lucas Haddon é estudante do primeiro ano de um bacharelado de quatro anos na fictícia Ashgrove University, orientado pelo Dr. Marco Bellini. A partir do segundo ano, ele também trabalha meio período na fictícia Fernway Outdoor Co-operative, uma varejista de propriedade dos associados, com uma loja online, um armazém e duas lojas físicas, sob a líder de segurança de TI Hannah Osei. Todas as pessoas, organizações e números aqui são sintéticos. O Dr. Bellini começa pela lógica porque as políticas de segurança são enunciados lógicos. Uma regra como a equipe pode emitir reembolsos se for gerente de loja ou se o valor for inferior a vinte libras e houver recibo pode ser escrita com AND, OR e NOT, e então verificada com precisão.

### 1.2 Tabelas-verdade para políticas

Lucas escreve a regra de reembolso como uma fórmula com três condições: M para gerente, S para valor pequeno e R para recibo. A frase em inglês é ambígua: a exigência do recibo também se aplica aos gerentes? Ele escreve as duas leituras, M OR (S AND R) e (M OR S) AND R, e monta uma tabela-verdade para cada uma. O laboratório abaixo imprime as duas tabelas e as linhas em que elas divergem. Essas linhas são casos reais, como um gerente reembolsando sem recibo, em que funcionários que seguem leituras diferentes agiriam de modo diferente. A lógica expõe a ambiguidade antes que ela vire uma discussão no caixa.

### Laboratório — Duas leituras de uma regra de reembolso

```python
# Truth tables for two readings of a refund policy (M manager, S small amount, R receipt).
from itertools import product
a = lambda M, S, R: M or (S and R)
b = lambda M, S, R: (M or S) and R
diff = 0
print(" M S R | A B")
for M, S, R in product([0, 1], repeat=3):
    x, y = int(a(M, S, R)), int(b(M, S, R)); diff += x != y
    print(f" {M} {S} {R} | {x} {y}{'  <- differ' if x != y else ''}")
print("rows that differ:", diff)
```

Execute com `python3 lab_truth.py`. Saída verificada:

```text
 M S R | A B
 0 0 0 | 0 0
 0 0 1 | 0 0
 0 1 0 | 0 0
 0 1 1 | 1 1
 1 0 0 | 1 0  <- differ
 1 0 1 | 1 1
 1 1 0 | 1 0  <- differ
 1 1 1 | 1 1
rows that differ: 2
```

### 1.3 Lacunas e contradições

As políticas também contêm lacunas, em que nenhuma regra se aplica, e contradições, em que duas regras dão respostas opostas. O rascunho da política de acesso remoto da Fernway diz que os terceirizados devem usar a VPN e que os scanners do armazém nunca usam a VPN; ele não diz nada sobre terceirizados que fazem manutenção nos scanners. Lucas lista as combinações sistematicamente e encontra esse caso. A enumeração sistemática é um hábito matemático simples, mas capta as situações que a leitura informal deixa passar. Ele recomenda acrescentar uma regra explícita e um padrão: tudo o que não for explicitamente permitido é negado, o padrão fail-safe de Saltzer e Schroeder (1975).

### Exemplo resolvido

Lucas formaliza uma regra de reembolso de duas maneiras, encontra as linhas em que as leituras divergem e identifica, numa política de acesso remoto, um caso não coberto de terceirizados e scanners.

> **Caso sintético.** A Ashgrove University, a Fernway Outdoor Co-operative, Lucas, Hannah e o Dr. Bellini são inventados; Saltzer e Schroeder (1975) é real.

### Erros e limites

Políticas reais incluem contexto que as fórmulas omitem, como emergências. A enumeração cresce rapidamente com muitas condições.

### Exercícios

- **EX001 — Duas leituras.** Escreva em lógica as duas leituras da regra de reembolso. *Rubrica:* 3 = M OR (S AND R) e (M OR S) AND R;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.

- **EX002 — Linhas divergentes.** Segundo o laboratório, em quantas linhas as leituras divergem, e o que elas têm em comum? *Rubrica:* 3 = 2 linhas, ambas um gerente sem recibo;; 2 = contagem e padrão;; 1 = nenhuma;; 0 = nenhuma.

- **EX003 — Lacuna da política.** Que lacuna Lucas encontrou na política de acesso remoto? *Rubrica:* 3 = terceirizados fazendo manutenção nos scanners do armazém;; 2 = caso;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever as camadas de hardware, software e serviços de uma organização de varejo; (2) identificar onde ficam as responsabilidades de segurança em cada camada; (3) montar um primeiro inventário de ativos.

### 2.1 As camadas na Fernway

Lucas visita a Fernway com a turma do Dr. Bellini. Hannah lhes mostra as camadas: hardware, como caixas, scanners do armazém, notebooks e uma pequena sala de servidores; software, como a plataforma da loja, o banco de dados de estoque e o e-mail; e serviços contratados de fora, incluindo pagamentos com cartão, hospedagem em nuvem e o sistema de rastreamento de um parceiro de entregas. Cada camada depende da camada de baixo. Uma plataforma de loja segura rodando num servidor sem patches herda as fraquezas do servidor. Lucas aprende que a arquitetura começa por enxergar a pilha inteira, e não só a parte que uma equipe de projeto por acaso possui.

### 2.2 Responsabilidade por camada

Nos serviços contratados, a responsabilidade é compartilhada. O provedor de nuvem protege seus data centers e hipervisores; a Fernway protege suas máquinas virtuais, contas e dados. O provedor de pagamentos com cartão cuida dos números de cartão; a Fernway precisa proteger suas chaves de integração e a página de checkout. Lucas desenha uma tabela de responsabilidades com três colunas: Fernway, fornecedor e compartilhada. Ele descobre que ninguém na Fernway constava como responsável por revisar o acesso do parceiro de entregas aos endereços dos clientes, concedido anos antes. Responsabilidades sem dono estão entre as fraquezas de arquitetura mais comuns em pequenas organizações.

### 2.3 Um primeiro inventário

Hannah pede a Lucas que comece um inventário de ativos. Cada linha lista o ativo, seu responsável, sua localização ou provedor, os dados que guarda e sua criticidade. Ele encontra mais do que esperava: um notebook antigo usado para imprimir etiquetas ainda tinha dados de clientes armazenados, e uma cópia de teste do banco de dados da loja estava num bucket de armazenamento em nuvem. Os inventários são a base do trabalho de arquitetura, porque ninguém consegue proteger o que não sabe que existe. Ele registra as duas surpresas como achados para Hannah e anota que o inventário precisa ser atualizado sempre que os sistemas mudarem.

### Exemplo resolvido

Lucas mapeia as camadas de hardware, software e serviços da Fernway, desenha uma tabela de responsabilidades que encontra sem dono a revisão do acesso do parceiro de entregas e começa um inventário que revela duas cópias de dados esquecidas.

> **Caso sintético.** Os sistemas e os achados da Fernway são sintéticos.

### Erros e limites

Os inventários nunca ficam completos na primeira passada. As fronteiras da responsabilidade compartilhada variam entre provedores e contratos.

### Exercícios

- **EX004 — Fraqueza herdada.** Por que uma plataforma de loja segura ainda pode ser vulnerável? *Rubrica:* 3 = herda as fraquezas de um servidor sem patches abaixo dela;; 2 = camada inferior;; 1 = não pode;; 0 = nenhuma.

- **EX005 — Item sem dono.** Que responsabilidade não tinha dono na Fernway? *Rubrica:* 3 = revisar o acesso do parceiro de entregas aos endereços dos clientes;; 2 = nomeada;; 1 = nenhuma;; 0 = nenhuma.

- **EX006 — Surpresas do inventário.** Que duas surpresas o inventário revelou? *Rubrica:* 3 = notebook antigo de etiquetas com dados de clientes; cópia de teste do banco num bucket na nuvem;; 2 = as duas;; 1 = uma;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever programas simples em Python que processam registros com segurança; (2) validar entradas com allow-lists; (3) evitar segredos fixos no código.

### 3.1 Processar registros

Os primeiros programas de Lucas leem registros de pedidos de arquivos CSV sintéticos e calculam totais. O Dr. Bellini acrescenta uma lente de segurança desde o início: toda entrada é não confiável até ser verificada. Lucas escreve funções que verificam cada campo: os identificadores de pedido precisam corresponder a um padrão fixo, as quantidades precisam ser inteiros positivos abaixo de um limite e os códigos postais precisam corresponder a um formato permitido. Os registros que falham são separados com um motivo. Os hábitos de programação formados no primeiro ano duram, então o curso trata a validação como parte da programação correta, e não como um tema avançado de segurança acrescentado depois.

### 3.2 Allow-lists em vez de block-lists

Lucas primeiro tenta bloquear caracteres perigosos nos nomes de produtos. O Dr. Bellini lhe mostra que as block-lists são sempre incompletas: há muitas maneiras de codificar uma entrada perigosa. Uma allow-list, que descreve como é uma entrada válida, é mais segura: os nomes de produtos podem conter letras, dígitos, espaços e alguns sinais de pontuação, até sessenta caracteres. Qualquer outra coisa é rejeitada. Lucas reescreve suas verificações desse jeito e acha o código mais curto e mais claro. O princípio se aplica em qualquer escala, de um único campo até as regras de firewall, em que permitir os fluxos sabidamente bons é mais seguro do que bloquear os sabidamente ruins.

### 3.3 Segredos fora do código

O programa de Lucas precisa chamar um serviço de estoque sintético com uma API key. Sua primeira versão escreve a chave no arquivo-fonte. O Dr. Bellini explica que o código-fonte é copiado, compartilhado e muitas vezes publicado por engano, então chaves no código vazam. Lucas move a chave para uma variável de ambiente lida em tempo de execução e acrescenta o arquivo de configuração à lista de arquivos ignorados do seu sistema de controle de versão. Ele também aprende que, se uma chave chegar a ser commitada, removê-la do arquivo não basta; ela precisa ser revogada e substituída, porque podem existir cópias do histórico.

### Exemplo resolvido

Lucas escreve um verificador de registros de pedidos com validação por allow-list e move uma API key do código-fonte para uma variável de ambiente.

> **Caso sintético.** Os registros, os serviços e as chaves são sintéticos.

### Erros e limites

Allow-lists podem rejeitar entradas válidas incomuns, como nomes com acentos, se não forem projetadas com cuidado. Variáveis de ambiente não são uma solução completa de gestão de segredos.

### Exercícios

- **EX007 — Fraqueza da block-list.** Por que as block-lists são mais fracas do que as allow-lists? *Rubrica:* 3 = uma entrada perigosa tem muitas codificações, então as block-lists são sempre incompletas;; 2 = incompletas;; 1 = mais fortes;; 0 = nenhuma.

- **EX008 — Regra dos nomes de produtos.** Descreva a allow-list de Lucas para nomes de produtos. *Rubrica:* 3 = letras, dígitos, espaços e alguns sinais de pontuação, até sessenta caracteres;; 2 = regra;; 1 = block-list;; 0 = nenhuma.

- **EX009 — Chave commitada.** O que precisa acontecer se uma API key for commitada no controle de versão? *Rubrica:* 3 = revogá-la e substituí-la, não só apagá-la do arquivo;; 2 = revogar;; 1 = só apagar;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem

Você vai (1) estruturar um argumento num relatório de segurança; (2) citar fontes com exatidão; (3) distinguir, na escrita, evidência de opinião.

### 4.1 Estruturar um argumento

O Dr. Bellini pede a Lucas um ensaio de duas mil palavras sobre se pequenos varejistas devem adotar a arquitetura zero trust. Ele primeiro lista as afirmações e seu apoio e depois as ordena num argumento: o que zero trust significa segundo o NIST SP 800-207, que problemas ele trata, quanto custa a uma pequena organização e como poderia ser uma adoção proporcional. Cada parágrafo defende um ponto e se liga ao seguinte. Ele aprende que uma estrutura de argumento clara importa mais do que o vocabulário, porque os leitores precisam acompanhar o raciocínio para julgar se a conclusão se justifica.

### 4.2 Citar com exatidão

Lucas inicialmente cita um post de blog que resume o SP 800-207. O Dr. Bellini pede que ele leia a própria publicação e a cite diretamente, porque resumos muitas vezes distorcem. Ele aprende a citar trechos com moderação e exatidão, dar a referência completa com seu identificador e evitar citar fontes que não leu. Também aprende a verificar se uma referência existe: um identificador inventado ou digitado errado mina o ensaio inteiro. Na escrita sobre segurança, a citação exata é especialmente importante, porque os leitores podem tomar decisões que afetam sistemas reais com base nas afirmações.

### 4.3 Evidência versus opinião

O rascunho de Lucas diz que zero trust torna as redes seguras. O Dr. Bellini marca isso como uma opinião apresentada como fato. Lucas revisa: o SP 800-207 descreve zero trust como um conjunto de princípios voltados a reduzir a confiança implícita; se a adoção reduz incidentes em pequenos varejistas não é algo estabelecido pelas fontes revisadas. Ele separa o que as fontes afirmam, o que as evidências mostram e o que ele argumenta. Essa separação vira um hábito para o resto do curso e para os relatórios profissionais, em que misturar opinião com evidência pode enganar os tomadores de decisão.

### Exemplo resolvido

Lucas estrutura um ensaio sobre zero trust para pequenos varejistas, substitui a citação de um blog pelo próprio SP 800-207 e reescreve uma afirmação exagerada como um enunciado com fonte e com ressalvas.

> **Caso sintético.** O ensaio e o feedback são sintéticos; o SP 800-207 é real.

### Erros e limites

As fontes primárias podem ser longas e técnicas; os resumos ajudam na orientação, mas não devem substituí-las. As ressalvas cuidadosas podem ser levadas ao exagero até não restar nenhuma afirmação.

### Exercícios

- **EX010 — Um ponto por parágrafo.** Que estrutura Lucas usa nos parágrafos? *Rubrica:* 3 = cada um defende um ponto e se liga ao seguinte;; 2 = um ponto;; 1 = aleatória;; 0 = nenhuma.

- **EX011 — Fonte primária.** Por que Lucas precisa citar diretamente o SP 800-207, e não um blog? *Rubrica:* 3 = resumos podem distorcer; cite o que você leu;; 2 = distorção;; 1 = blog serve;; 0 = nenhuma.

- **EX012 — Reescrita do exagero.** Como Lucas reescreveu zero trust torna as redes seguras? *Rubrica:* 3 = princípios que reduzem a confiança implícita; efeito em pequenos varejistas não estabelecido;; 2 = com ressalvas;; 1 = inalterada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) explicar conceitos centrais de segurança em linguagem simples; (2) reconhecer padrões comuns de ataque contra varejistas; (3) relacionar os controles aos ataques que eles tratam.

### 5.1 Conceitos centrais

Lucas aprende a linguagem da segurança: confidencialidade, integridade e disponibilidade; ativos, ameaças, vulnerabilidades e risco; autenticação e autorização. Ele pratica explicar cada um a uma gerente de loja da Fernway, sem jargão. Confidencialidade significa que só as pessoas certas veem os dados dos clientes; integridade significa que preços e pedidos não podem ser alterados sem permissão; disponibilidade significa que a loja continua aberta online. Saber explicar os conceitos com simplicidade faz parte do letramento em segurança, porque os arquitetos precisam convencer não especialistas a financiar e seguir os controles. Se a gerente não consegue repetir a ideia com as próprias palavras, a explicação ainda não funcionou.

### 5.2 Ataques a varejistas

Hannah descreve os ataques que a Fernway enfrenta. E-mails de phishing que se passam por fornecedores pedem à equipe que altere dados bancários. O credential stuffing usa senhas vazadas de outros sites para entrar nas contas dos associados. Scripts de skimming injetados nas páginas de checkout roubam os dados dos cartões enquanto os clientes digitam. A fraude com vale-presente explora verificações fracas nas consultas de saldo. Lucas observa que a maioria não quebra criptografia nem explora falhas exóticas; elas abusam de processos comuns e de autenticação fraca. A arquitetura, portanto, precisa cobrir processos de negócio e pessoas, e não só servidores e redes.

### 5.3 Controles para os ataques

Lucas associa controles aos ataques. As alterações de dados bancários de fornecedores exigem uma ligação para um número conhecido e duas aprovações. O credential stuffing é reduzido com rate limiting, verificação das senhas contra listas de senhas vazadas e oferta de autenticação multifator. O skimming no checkout é reduzido limitando scripts de terceiros, usando content security policy e monitorando mudanças na página. A fraude com vale-presente é reduzida com rate limits e exigindo o número do cartão mais um PIN. Cada controle trata um caminho de ataque específico, e ele consegue explicar por que cada um existe, o que ajuda a equipe a aceitá-lo.

### Exemplo resolvido

Lucas explica cinco conceitos centrais a uma gerente de loja, lista quatro ataques ao varejo e associa cada um a controles.

> **Caso sintético.** Os ataques e os controles na Fernway são sintéticos.

### Erros e limites

Os padrões de ataque mudam; as listas precisam de atualização regular. Os controles podem deslocar os ataques para outro lugar, em vez de detê-los.

### Exercícios

- **EX013 — Integridade no varejo.** Dê um exemplo de integridade no varejo. *Rubrica:* 3 = preços e pedidos não podem ser alterados sem permissão;; 2 = exemplo;; 1 = confidencialidade;; 0 = nenhuma.

- **EX014 — Credential stuffing.** O que é credential stuffing, e um controle contra ele? *Rubrica:* 3 = entrar com senhas vazadas em outros sites; rate limiting, verificação de senhas vazadas ou MFA;; 2 = os dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX015 — Controle dos dados bancários.** Como as alterações de dados bancários de fornecedores devem ser verificadas? *Rubrica:* 3 = ligação para um número conhecido mais duas aprovações;; 2 = os dois;; 1 = resposta por e-mail;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem

Você vai (1) modelar sistemas e acessos como grafos; (2) encontrar caminhos de ataque com busca em grafos; (3) usar medidas de grafos para priorizar controles.

### 6.1 Grafos de acesso

O Dr. Bellini mostra como os grafos modelam a segurança. Os nós podem ser usuários, máquinas e repositórios de dados; as arestas podem ser logins, conexões de rede ou permissões. Um atacante que controla um nó pode seguir as arestas até outros. Lucas constrói um pequeno grafo sintético da Fernway: um notebook de funcionário vítima de phishing, um servidor de arquivos compartilhado, o sistema de gestão do armazém, uma estação de trabalho de administração e o banco de dados da loja. As arestas representam permissões e alcançabilidade de rede. Desenhar o grafo torna visíveis caminhos difíceis de ver em listas de regras espalhadas por sistemas e equipes diferentes.

### 6.2 Caminhos de ataque mais curtos

Usando busca em largura, Lucas encontra o caminho mais curto do notebook vítima de phishing até o banco de dados da loja. O laboratório abaixo mostra um caminho de três saltos: do notebook ao servidor de arquivos, do servidor de arquivos à estação de administração por meio de uma credencial de administrador salva, e da estação de administração ao banco de dados. Os caminhos mais curtos importam porque os atacantes preferem rotas fáceis. Remover a credencial salva corta esse caminho; a busca então encontra um caminho mais longo pelo sistema do armazém. Cada mudança pode ser verificada rodando a busca de novo, o que oferece uma maneira precisa de avaliar se um controle realmente bloqueia a rota que pretende bloquear.

### Laboratório — Caminhos de ataque por busca em largura

```python
# BFS attack paths on a synthetic Fernway graph.
from collections import deque
def bfs(E, s, t):
    prev, q = {s: None}, deque([s])
    while q:
        u = q.popleft()
        if u == t:
            p = [];
            while u: p.append(u); u = prev[u]
            return p[::-1]
        for v in E.get(u, []):
            if v not in prev: prev[v] = u; q.append(v)
E = {"staff-laptop": ["file-server", "warehouse-wms"], "file-server": ["admin-ws"],
     "warehouse-wms": ["integration-svc"], "integration-svc": ["stock-api"], "stock-api": ["shop-db"], "admin-ws": ["shop-db"]}
p = bfs(E, "staff-laptop", "shop-db"); print(f"{len(p)-1} hops:", " -> ".join(p))
E["file-server"] = []          # saved admin credential removed
p = bfs(E, "staff-laptop", "shop-db"); print(f"{len(p)-1} hops:", " -> ".join(p))
```

Execute com `python3 lab_paths.py`. Saída verificada:

```text
3 hops: staff-laptop -> file-server -> admin-ws -> shop-db
4 hops: staff-laptop -> warehouse-wms -> integration-svc -> stock-api -> shop-db
```

### 6.3 Priorizar com grafos

Alguns nós aparecem em muitos caminhos; protegê-los traz mais benefício. Lucas conta quantos caminhos mais curtos dos notebooks da equipe até os dados sensíveis passam por cada nó. A estação de administração e o servidor de arquivos se destacam. Ele recomenda fazer primeiro o hardening da estação de administração e remover as credenciais armazenadas do servidor de arquivos. O raciocínio com grafos dá uma base objetiva para as prioridades, mas Lucas observa que o grafo só é tão bom quanto suas arestas: conexões desconhecidas, como ferramentas de acesso remoto esquecidas, mudariam a resposta, e é por isso que os inventários importam.

### Exemplo resolvido

Lucas modela a Fernway como um grafo, encontra um caminho de três saltos até o banco de dados da loja, mostra que a remoção de uma credencial salva alonga o caminho e prioriza dois nós que são pontos de estrangulamento.

> **Caso sintético.** O grafo e as credenciais são sintéticos.

### Erros e limites

Os grafos omitem arestas que ninguém conhece. O comprimento do caminho é um indicador grosseiro do esforço do atacante.

### Exercícios

- **EX016 — Significado das arestas.** O que as arestas podem representar num grafo de segurança? *Rubrica:* 3 = logins, conexões de rede ou permissões;; 2 = dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX017 — Mudança de caminho no laboratório.** O que aconteceu com o caminho mais curto depois da remoção da credencial salva? *Rubrica:* 3 = passou de 3 para 4 saltos, pelo sistema do armazém;; 2 = mais longo;; 1 = inalterado;; 0 = nenhuma.

- **EX018 — Pontos de estrangulamento.** Que nós Lucas priorizou, e por quê? *Rubrica:* 3 = a estação de administração e o servidor de arquivos, que estão em muitos caminhos mais curtos;; 2 = os dois;; 1 = aleatórios;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) descrever como a loja, as lojas físicas e o armazém da Fernway se conectam; (2) explicar os papéis de DNS, HTTP e TLS numa loja online; (3) identificar fraquezas de projeto de rede numa pequena organização.

### 7.1 Como a Fernway se conecta

Lucas mapeia a rede da Fernway. Os clientes chegam à loja pela internet; a loja roda num provedor de nuvem. As lojas físicas se conectam à sede por enlaces de banda larga com uma VPN site-to-site. O armazém tem sua própria rede sem fio para os scanners. A equipe usa e-mail e um serviço de arquivos na nuvem. Ele rotula cada conexão com seu protocolo e sua criptografia e anota qual tráfego atravessa a internet pública. O mapa mostra que a rede sem fio do armazém e a rede do escritório estão interligadas em bridge, de modo que um scanner e um notebook do financeiro ficam no mesmo segmento.

### 7.2 DNS, HTTP e TLS numa loja

Quando um cliente visita a loja, o DNS traduz o nome num endereço, o navegador abre uma conexão TLS especificada na RFC 8446 e então envia requisições HTTP. Lucas aprende que o comprometimento da conta de DNS da Fernway permitiria a um atacante redirecionar os clientes para uma loja falsa, que poderia obter seu próprio certificado para um nome parecido, mas não para o nome da Fernway, a menos que também controlasse o DNS usado na validação do certificado. Por isso, ele recomenda autenticação forte na conta do registrador do domínio, um ativo muitas vezes esquecido nas revisões de arquitetura porque fica fora do parque técnico.

### 7.3 Fraquezas de pequenas organizações

Lucas lista fraquezas de rede típicas de pequenas organizações, todas presentes na Fernway: as redes do armazém e do escritório interligadas, uma senha de Wi-Fi compartilhada sem troca há anos, área de trabalho remota exposta à internet para um fornecedor e nenhum registro dos responsáveis pelas regras de firewall. Ele propõe correções simples: redes separadas para scanners, visitantes e equipe; substituir a área de trabalho remota exposta por um serviço gerenciado de acesso remoto com autenticação multifator; e anotar nas regras de firewall os responsáveis e as datas de revisão. Cada correção é barata em comparação com o impacto da fraqueza que elimina.

### Exemplo resolvido

Lucas mapeia as conexões da Fernway, recomenda proteger a conta do registrador e propõe três correções de rede, incluindo separar os segmentos interligados do armazém e do escritório.

> **Caso sintético.** A rede da Fernway é sintética; a RFC 8446 é real.

### Erros e limites

Separar redes pode quebrar dependências não documentadas; teste antes. Os serviços em nuvem podem contornar completamente a rede do escritório.

### Exercícios

- **EX019 — Redes interligadas.** Que risco a interligação das redes do armazém e do escritório cria? *Rubrica:* 3 = um scanner comprometido consegue alcançar diretamente os notebooks do financeiro;; 2 = alcance;; 1 = nenhuma;; 0 = nenhuma.

- **EX020 — Conta do registrador.** Por que proteger fortemente a conta do registrador do domínio? *Rubrica:* 3 = seu comprometimento permite redirecionar os clientes e possivelmente obter certificados;; 2 = redirecionar;; 1 = não é importante;; 0 = nenhuma.

- **EX021 — Correção da área de trabalho remota.** O que deve substituir a área de trabalho remota exposta à internet para o fornecedor? *Rubrica:* 3 = um serviço gerenciado de acesso remoto com autenticação multifator;; 2 = gerenciado com MFA;; 1 = deixar como está;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem

Você vai (1) construir um pequeno serviço web com autenticação e autorização; (2) escrever testes para regras de controle de acesso; (3) registrar de forma útil os eventos relevantes para a segurança.

### 8.1 Um pequeno serviço

Em Programação II, Lucas constrói um serviço sintético de consulta de estoque para a equipe das lojas, usando o servidor HTTP da biblioteca padrão do Python para fins de aprendizado. A equipe faz login e depois consulta os níveis de estoque; os gerentes também podem ajustar o estoque. Ele separa a autenticação, que estabelece quem é o usuário, da autorização, que decide o que esse usuário pode fazer. Cada requisição verifica as duas. Ele aprende que misturá-las causa bugs, como verificar apenas que um usuário está logado e esquecer de verificar se ele é gerente antes de permitir um ajuste.

### 8.2 Testar as regras de acesso

Lucas escreve testes para cada combinação de papel e ação: a equipe pode consultar, a equipe não pode ajustar, os gerentes podem fazer as duas coisas, usuários anônimos não podem fazer nenhuma. Ele também testa casos-limite, como um gerente de uma loja ajustando o estoque de outra loja, o que as regras proíbem. Um teste falha: o serviço verifica o papel de gerente, mas não a loja. Ele corrige a verificação e o teste passa. Testar as regras de acesso como uma matriz torna visíveis as verificações ausentes, e esses testes depois protegem a regra quando alguém modifica o código.

### 8.3 Registrar de forma útil

O serviço registra logins, logins com falha, ajustes de estoque e falhas de autorização, com usuário, horário, ação e resultado, mas nunca senhas ou tokens de sessão. Lucas aprende que os logs servem às investigações, então cada entrada precisa responder quem fez o quê, quando e com que resultado. Ele também aprende a evitar registrar dados pessoais em excesso. Hannah revisa seu desenho de logs e pede um identificador de correlação para cada requisição, para que os eventos de diferentes serviços possam ser ligados durante um incidente. Um logging útil é projetado pensando em quem vai lê-lo no futuro.

### Exemplo resolvido

Lucas constrói um serviço de estoque que separa a autenticação da autorização, encontra uma verificação de loja ausente por meio de uma matriz de testes de papel e ação e projeta logs com identificadores de correlação.

> **Caso sintético.** O serviço, os papéis e as lojas são sintéticos.

### Erros e limites

Servidores da biblioteca padrão servem para aprender; a produção usa frameworks mantidos. As matrizes de testes crescem rapidamente com os papéis e os recursos.

### Exercícios

- **EX022 — AuthN versus AuthZ.** Qual é a diferença entre autenticação e autorização? *Rubrica:* 3 = a autenticação estabelece a identidade; a autorização decide as ações permitidas;; 2 = as duas;; 1 = iguais;; 0 = nenhuma.

- **EX023 — Teste que falhou.** Que teste falhou, e por quê? *Rubrica:* 3 = gerente ajustando o estoque de outra loja; a loja não era verificada;; 2 = nomeado;; 1 = nenhuma;; 0 = nenhuma.

- **EX024 — Nunca registrado.** O que nunca pode aparecer nos logs? *Rubrica:* 3 = senhas ou tokens de sessão;; 2 = os dois;; 1 = nomes de usuário;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Dados e bancos de dados

### Objetivos de aprendizagem

Você vai (1) projetar o acesso ao banco de dados segundo o menor privilégio; (2) prevenir injeção por meio de consultas parametrizadas; (3) proteger backups e cópias de teste.

### 9.1 Acesso ao banco com menor privilégio

O banco de dados da loja da Fernway guarda associados, pedidos e estoque. Lucas revisa como as aplicações se conectam. A loja usa uma única conta de banco de dados com todos os direitos sobre tudo, inclusive apagar tabelas. Ele propõe contas separadas: a loja pode ler produtos e gravar pedidos; os relatórios podem ler visões agregadas; só uma conta de administrador, usada raramente e com registro, pode mudar o esquema. Cada conta recebe apenas os direitos de que sua função precisa. Se a loja for comprometida, o atacante herda só os direitos da loja, e não o poder de apagar ou exportar todas as tabelas.

### 9.2 Injeção e parâmetros

Lucas revisa o código de busca da loja e encontra uma consulta montada concatenando strings com a entrada do cliente. Ele demonstra, num banco sintético com o sqlite3 do Python, como um termo de busca forjado devolve todos os registros de associados. A correção é passar a entrada como parâmetros, que o banco trata estritamente como dados. Ele também verifica as demais consultas e encontra mais duas montadas do mesmo jeito. As consultas parametrizadas são um controle simples e consagrado, e mesmo assim a injeção continua comum porque desenvolvedores sob pressão de prazo copiam padrões antigos. Os checklists de revisão de código devem incluí-la explicitamente.

### 9.3 Backups e cópias de teste

O inventário do capítulo 2 encontrou uma cópia de teste do banco de dados no armazenamento em nuvem. Lucas investiga: ela continha dados reais de associados e podia ser lida por qualquer pessoa com o link. Ele recomenda que os ambientes de teste usem dados sintéticos ou mascarados, que os backups sejam criptografados com chaves guardadas separadamente e que as permissões de armazenamento sejam revisadas automaticamente. A ISO/IEC 27002:2022 inclui controles sobre informações de teste e mascaramento de dados. As cópias de dados multiplicam o risco, e a arquitetura precisa tratar cada cópia com o mesmo cuidado que o original, ou evitar criá-la.

### Exemplo resolvido

Lucas divide uma conta de banco de dados todo-poderosa em três contas de menor privilégio, encontra três consultas injetáveis e recomenda dados de teste sintéticos e backups criptografados.

> **Caso sintético.** O conteúdo do banco e as consultas são sintéticos; a ISO/IEC 27002:2022 é real.

### Erros e limites

Dividir as contas exige mudanças e testes na aplicação. Dados mascarados ainda podem ser reidentificáveis se o mascaramento for malfeito.

### Exercícios

- **EX025 — Impacto do comprometimento.** Como contas de banco separadas limitam um comprometimento da loja? *Rubrica:* 3 = o atacante obtém apenas os direitos limitados da conta da loja;; 2 = limitado;; 1 = nenhuma;; 0 = nenhuma.

- **EX026 — Contagem de injeções.** Quantas consultas injetáveis Lucas encontrou no total? *Rubrica:* 3 = três;; 2 = três;; 1 = uma;; 0 = nenhuma.

- **EX027 — Regra dos dados de teste.** Que dados os ambientes de teste devem usar? *Rubrica:* 3 = dados sintéticos ou mascarados;; 2 = sintéticos;; 1 = reais;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e prática autorizada

### Objetivos de aprendizagem

Você vai (1) explicar por que a autorização é exigida antes de testes de segurança; (2) tratar com ética os dados pessoais encontrados durante o trabalho; (3) aplicar códigos profissionais a dilemas.

### 10.1 A autorização primeiro

Lucas quer testar se o login dos associados da Fernway é vulnerável a credential stuffing. Hannah explica que, mesmo com boas intenções, testar sem autorização por escrito pode violar leis sobre uso indevido de computadores e prejudicar os clientes. A autorização declara o que pode ser testado, como, quando e por quem, e indica um contato para emergências. Ela precisa vir de alguém com autoridade sobre o sistema. No caso da loja, isso inclui as regras do provedor de nuvem, que restringem certos testes. Lucas escreve uma solicitação de teste, Hannah aprova uma versão limitada num ambiente de staging e o teste segue com segurança.

### 10.2 Dados pessoais na prática

Ao revisar logs, Lucas vê nomes, endereços e históricos de pedidos de associados. Ele aprende a acessar só o que a tarefa exige, nunca navegar por curiosidade e nunca copiar dados pessoais para anotações pessoais ou trabalhos do curso. Quando precisa de exemplos para seu trabalho na universidade, ele cria registros sintéticos. A legislação de privacidade de muitos países exige esse cuidado, mas a questão ética é mais simples: os associados confiaram seus dados à Fernway para fazer compras, e não para a conveniência de um estudante. Respeitar essa confiança faz parte da prática profissional.

### 10.3 Dilemas e códigos

Lucas enfrenta um dilema: um amigo que trabalha em outro varejista comenta que a página de checkout deles carrega scripts de um domínio desconhecido. Ele deveria investigar? Os códigos profissionais, como os das sociedades de computação, enfatizam a honestidade, evitar danos e respeitar a autorização. Ele não sonda o outro site. Em vez disso, sugere que o amigo relate o caso internamente à equipe de segurança deles. Ele discute o caso com o Dr. Bellini, que elogia a contenção: ajudar é certo, mas agir sobre sistemas que não se está autorizado a testar causa danos, mesmo quando motivado pela preocupação.

### Exemplo resolvido

Lucas obtém uma autorização por escrito limitada para um teste em staging, usa dados sintéticos nos trabalhos do curso e se recusa a sondar o site de outro varejista.

> **Caso sintético.** A solicitação de teste, os logs e o caso do amigo são sintéticos.

### Erros e limites

As leis variam conforme a jurisdição; busque orientação em caso de dúvida. Os ambientes de staging podem não reproduzir o comportamento da produção.

### Exercícios

- **EX028 — Conteúdo da autorização.** O que uma autorização de teste deve especificar? *Rubrica:* 3 = o quê, como, quando, por quem e um contato de emergência;; 2 = quatro;; 1 = nenhuma;; 0 = nenhuma.

- **EX029 — Dados dos trabalhos.** O que Lucas usa como exemplos nos trabalhos do curso? *Rubrica:* 3 = registros sintéticos, não dados de associados;; 2 = sintéticos;; 1 = reais;; 0 = nenhuma.

- **EX030 — Relato do amigo.** O que Lucas aconselhou o amigo a fazer sobre o script suspeito? *Rubrica:* 3 = relatá-lo internamente à equipe de segurança da própria organização;; 2 = relatar;; 1 = sondá-lo;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) comparar os modelos de contas e permissões do Windows e do Linux; (2) fazer o hardening de notebooks e servidores com baselines; (3) gerenciar atualizações numa pequena organização.

### 11.1 Contas e permissões

Lucas estuda como o Windows e o Linux controlam o acesso. Ambos têm usuários e grupos; ambos distinguem administradores de usuários comuns. Na Fernway, todo usuário de notebook das lojas é administrador local, uma conveniência que permite a qualquer malware rodar com direitos totais. Hannah concorda em remover os direitos de administrador local e oferecer um processo de solicitação para a instalação de software. Lucas também revisa um servidor Linux em que vários funcionários compartilham a senha de root. Ele recomenda contas individuais com direitos elevados por meio de comandos registrados, para que as ações possam ser atribuídas a pessoas.

### 11.2 Baselines

Uma baseline é um conjunto documentado de configurações seguras. Para os notebooks, Lucas propõe criptografia de disco completo, bloqueio automático de tela, firewall de host, remoção de software não usado e contas de usuário padrão. Para os servidores, propõe desativar serviços não usados, login de administrador baseado em chaves com autenticação multifator e logging centralizado. Ele relaciona a baseline a famílias de controles do SP 800-53 Rev. 5, como gestão de configuração e controle de acesso, para que a Fernway possa mostrar aos auditores o que faz. Aplicar uma baseline de forma consistente elimina muitas das brechas fáceis das quais os atacantes dependem.

### 11.3 Atualizações

Software sem patches é uma porta de entrada frequente. Os notebooks da Fernway se atualizam automaticamente, mas os caixas rodam uma versão antiga do sistema operacional que o fornecedor ainda suporta apenas com atualizações pagas, e os scanners do armazém nunca foram atualizados. Lucas propõe uma política de atualizações: atualizações automáticas onde possível, uma janela mensal para os servidores, contratos com o fornecedor cobrindo os caixas e um plano de substituição para os scanners. Cada exceção é registrada com um responsável e uma data de revisão. Ele observa que as atualizações mais difíceis são as dos dispositivos que ninguém considera computadores.

### Exemplo resolvido

Lucas remove os direitos de administrador local, substitui uma senha de root compartilhada por contas individuais, propõe baselines para notebooks e servidores e escreve uma política de atualizações com exceções.

> **Caso sintético.** Os dispositivos, as versões e as políticas são sintéticos; o SP 800-53 Rev. 5 é real.

### Erros e limites

Remover os direitos de administrador aumenta os pedidos de suporte no início. Alguns dispositivos de fornecedores não podem ser atualizados sem perder a garantia.

### Exercícios

- **EX031 — Risco do administrador local.** Por que ter todo usuário como administrador local é arriscado? *Rubrica:* 3 = o malware roda com direitos totais;; 2 = direitos totais;; 1 = nenhuma;; 0 = nenhuma.

- **EX032 — Correção do root compartilhado.** O que substitui a senha de root compartilhada? *Rubrica:* 3 = contas individuais com elevação registrada;; 2 = individuais;; 1 = nova senha compartilhada;; 0 = nenhuma.

- **EX033 — Atualizações mais difíceis.** Que atualizações Lucas considera as mais difíceis? *Rubrica:* 3 = as de dispositivos que ninguém considera computadores, como scanners e caixas;; 2 = dispositivos;; 1 = notebooks;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) estimar uma proporção a partir de uma amostra de auditoria; (2) calcular e interpretar um intervalo de confiança; (3) evitar erros estatísticos comuns em relatórios de segurança.

### 12.1 Amostragem para auditoria

A Fernway tem cerca de quatro mil contas de usuários e de serviço distribuídas pelos sistemas. Hannah não consegue revisar todas as contas, então Lucas sorteia uma amostra aleatória de duzentas e verifica em cada uma problemas como falta de responsável ou acessos desatualizados. Ele encontra vinte e seis com problemas. A proporção amostral é de treze por cento. A amostragem aleatória importa: se ele tivesse verificado apenas as contas de que já suspeitava, a estimativa seria enviesada para cima. Ele registra como a amostra foi sorteada, com a semente aleatória, para que a auditoria possa ser repetida e conferida por outra pessoa.

### 12.2 Intervalos de confiança

Uma proporção isolada esconde a incerteza. Lucas calcula um intervalo de confiança de noventa e cinco por cento usando o método de Wilson, que se comporta bem com proporções. O laboratório abaixo mostra a estimativa e o intervalo, e a faixa implícita de contas afetadas na população. Ele relata que entre cerca de nove e dezoito por cento das contas provavelmente têm problemas, algo como 360 a 740 contas. Essa faixa é mais honesta e mais útil do que os treze por cento sozinhos, porque diz a Hannah quanto esforço de limpeza planejar.

### Laboratório — Amostra de auditoria e intervalo de confiança

```python
# Wilson 95% interval for an account-audit sample (synthetic).
import math
N, n, x, z = 4000, 200, 26, 1.96
p = x / n
den = 1 + z*z/n; centre = (p + z*z/(2*n)) / den
half = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den
lo, hi = centre - half, centre + half
print(f"sample {x}/{n} = {p:.1%}; Wilson 95% CI {lo:.1%} to {hi:.1%}")
print(f"implied affected accounts: {lo*N:.0f} to {hi*N:.0f} of {N}")
```

Execute com `python3 lab_sample.py`. Saída verificada:

```text
sample 26/200 = 13.0%; Wilson 95% CI 9.0% to 18.4%
implied affected accounts: 361 to 735 of 4000
```

### 12.3 Erros comuns

Lucas lista erros que já viu em relatórios de segurança: porcentagens sem contagens, comparações de números pequenos apresentadas como mudanças dramáticas, médias de dados assimétricos e confusão entre correlação e causa. Um relatório que afirma que os cliques em phishing caíram pela metade depois de um treinamento, com base em quatro cliques que caíram para dois, diz pouco. Ele decide sempre relatar as contagens junto com as proporções, os intervalos quando houver amostragem e o método usado. A estatística não torna um relatório mais científico a menos que seja usada com cuidado; mal usada, empresta uma falsa autoridade a afirmações fracas.

### Exemplo resolvido

Lucas amostra 200 de 4.000 contas, encontra 26 com problemas, calcula um intervalo de Wilson e relata uma faixa de contas afetadas.

> **Caso sintético.** As contas e os achados são sintéticos.

### Erros e limites

Os intervalos supõem amostragem aleatória; amostras por conveniência os invalidam. Os problemas encontrados dependem da consistência de quem revisa.

### Exercícios

- **EX034 — Por que aleatória.** Por que a amostra da auditoria precisa ser aleatória? *Rubrica:* 3 = amostras dirigidas enviesam a estimativa;; 2 = viés;; 1 = mais rápido;; 0 = nenhuma.

- **EX035 — Intervalo do laboratório.** Que intervalo o laboratório relatou? *Rubrica:* 3 = cerca de 9,0 a 18,4 por cento, aproximadamente 361 a 735 contas;; 2 = intervalo;; 1 = nenhuma;; 0 = nenhuma.

- **EX036 — De quatro para dois.** Por que os cliques em phishing caíram pela metade, de quatro para dois, é uma evidência fraca? *Rubrica:* 3 = contagens minúsculas tornam a mudança sem significado, explicável pelo acaso;; 2 = números pequenos;; 1 = forte;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Identidade e acesso

### Objetivos de aprendizagem

Você vai (1) projetar processos de ciclo de vida da identidade para admissões, movimentações e desligamentos; (2) aplicar o acesso baseado em papéis com segregação de funções; (3) fortalecer a autenticação com métodos resistentes a phishing.

### 13.1 Admissões, movimentações e desligamentos

A maioria dos problemas de acesso encontrados no capítulo 12 veio do ciclo de vida da identidade. Os novos funcionários recebiam acesso copiando a conta de um colega, os funcionários que mudavam de função mantinham os direitos antigos e as contas dos desligados ficavam ativas por semanas. Lucas projeta processos: os admitidos recebem acesso a partir de definições de papéis aprovadas pelos gestores; quem muda de função perde os papéis antigos ao ganhar os novos; os desligados são desativados no último dia, por um gatilho do sistema de RH. Cada etapa é registrada. Os processos de ciclo de vida impedem que o acesso cresça em silêncio, um padrão chamado privilege creep que mina o menor privilégio ao longo do tempo.

### 13.2 Papéis e funções

Lucas define papéis para a Fernway: equipe de loja, gerente de loja, operador de armazém, comprador, auxiliar financeiro e administrador. Cada papel tem um conjunto documentado de permissões. Ele procura combinações tóxicas: um comprador que também pode aprovar pagamentos a fornecedores poderia criar um fornecedor falso e pagá-lo. Ele marca esses pares como conflitos que não podem ser mantidos juntos, implementando a segregação de funções. Os papéis simplificam as revisões de acesso, porque os gestores revisam atribuições de papéis em vez de centenas de permissões individuais. Mas os papéis precisam de manutenção, ou as exceções se acumulam até que os papéis signifiquem pouco.

### 13.3 Autenticação mais forte

A equipe da Fernway usa senhas mais códigos por mensagem de texto. Lucas explica que os códigos por SMS podem ser capturados por phishing em páginas de login falsas que os repassam em tempo real. Métodos resistentes a phishing, como passkeys ou chaves de segurança em hardware que usam criptografia de chave pública vinculada ao site verdadeiro, impedem isso, porque a credencial não funciona num domínio falso. Ele propõe passkeys primeiro para os administradores e o financeiro, e depois para os demais. Também recomenda que a loja dos associados ofereça passkeys como opção. A força da autenticação deve acompanhar o valor do que uma conta pode fazer.

### Exemplo resolvido

Lucas projeta os processos de admissão, movimentação e desligamento, define seis papéis com uma combinação tóxica bloqueada e propõe autenticação resistente a phishing primeiro para a equipe privilegiada.

> **Caso sintético.** Os papéis e os processos são sintéticos.

### Erros e limites

Os modelos de papéis derivam sem revisão regular. Os processos de recuperação de passkeys podem virar um ponto fraco.

### Exercícios

- **EX037 — Privilege creep.** O que é privilege creep, e que processo o impede? *Rubrica:* 3 = acesso que se acumula nas mudanças de função; o processo de movimentação remove os papéis antigos;; 2 = os dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX038 — Combinação tóxica.** Que combinação tóxica Lucas bloqueou? *Rubrica:* 3 = comprador que também pode aprovar pagamentos a fornecedores;; 2 = nomeada;; 1 = nenhuma;; 0 = nenhuma.

- **EX039 — Fraqueza dos códigos por SMS.** Por que os códigos por SMS são mais fracos do que as passkeys? *Rubrica:* 3 = podem ser capturados por phishing e repassados em tempo real; as passkeys se vinculam ao site verdadeiro;; 2 = repasse;; 1 = mais fortes;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos de privacidade

### Objetivos de aprendizagem

Você vai (1) aplicar os princípios de privacidade aos dados dos associados da Fernway; (2) projetar a pseudonimização para as análises; (3) atender às solicitações dos titulares por meio da arquitetura.

### 14.1 Princípios de privacidade

Lucas estuda os princípios de privacidade comuns às leis de proteção de dados: finalidade legítima, minimização dos dados, exatidão, limitação do armazenamento, segurança e responsabilização. Ele os aplica ao programa de associados da Fernway. Os associados informam o endereço para as entregas e o histórico de compras para as recompensas. A equipe de marketing quer analisar as compras por região. A minimização sugere que eles precisam dos distritos postais e das categorias de produtos, e não de nomes e endereços completos. Lucas aprende que a privacidade molda a arquitetura: o sistema de análise deve receber menos dados do que a loja guarda, por projeto, e não só por política.

### 14.2 Pseudonimização

Para as análises, Lucas projeta a pseudonimização: os identificadores dos associados são substituídos por hashes com chave calculados com HMAC e uma chave secreta guardada pela equipe de dados, e não pelos analistas. O mesmo associado sempre corresponde ao mesmo pseudônimo, de modo que as compras podem ser ligadas, mas os analistas não conseguem revertê-lo sem a chave. O laboratório abaixo mostra isso com associados sintéticos e por que um hash sem chave é mais fraco: qualquer pessoa pode calcular o hash de números de associado candidatos e compará-los. Dados pseudonimizados continuam sendo dados pessoais segundo muitas leis, então ainda precisam de proteção, mas o risco é menor.

### Laboratório — Pseudônimos com chave versus sem chave

```python
# Keyed (HMAC) vs unkeyed pseudonyms for synthetic member numbers. Teaching only.
import hmac, hashlib
KEY = b"synthetic-data-team-key"
members = ["M100231", "M100232", "M100233"]
keyed = {m: hmac.new(KEY, m.encode(), hashlib.sha256).hexdigest()[:12] for m in members}
plain = {m: hashlib.sha256(m.encode()).hexdigest()[:12] for m in members}
target_plain, target_keyed = plain["M100232"], keyed["M100232"]
guesses = [f"M1002{i:02d}" for i in range(100)]
hit_plain = [g for g in guesses if hashlib.sha256(g.encode()).hexdigest()[:12] == target_plain]
hit_keyed = [g for g in guesses if hashlib.sha256(g.encode()).hexdigest()[:12] == target_keyed]
print("stable keyed pseudonym:", keyed["M100232"] == hmac.new(KEY, b"M100232", hashlib.sha256).hexdigest()[:12])
print("guessing unkeyed pseudonym recovers:", hit_plain)
print("guessing keyed pseudonym (no key) recovers:", hit_keyed)
```

Execute com `python3 lab_pseudo.py`. Saída verificada:

```text
stable keyed pseudonym: True
guessing unkeyed pseudonym recovers: ['M100232']
guessing keyed pseudonym (no key) recovers: []
```

### 14.3 Solicitações dos titulares

Os associados podem pedir para ver ou excluir seus dados. Lucas mapeia onde ficam os dados dos associados: o banco de dados da loja, o e-mail marketing, as análises, os backups e o parceiro de entregas. Sem o mapa, a Fernway não conseguiria atender às solicitações por completo. Ele propõe que cada sistema ofereça uma forma de localizar e excluir os registros de um associado, e que os backups expirem num calendário em vez de serem editados. O atendimento às solicitações se torna um teste da arquitetura: se os dados estão espalhados em lugares desconhecidos, a organização não consegue cumprir suas promessas aos associados.

### Exemplo resolvido

Lucas aplica seis princípios de privacidade ao programa de associados, projeta pseudônimos baseados em HMAC para as análises e mapeia cinco locais de dados para as solicitações dos titulares.

> **Caso sintético.** Os associados, os sistemas e as chaves são sintéticos.

### Erros e limites

Dados pseudonimizados podem ser reidentificados pela combinação de campos. Os requisitos legais variam conforme a jurisdição.

### Exercícios

- **EX040 — Minimização nas análises.** De que dados o marketing realmente precisa para a análise por região? *Rubrica:* 3 = distritos postais e categorias de produtos, não nomes ou endereços completos;; 2 = mínimos;; 1 = tudo;; 0 = nenhuma.

- **EX041 — Fraqueza sem chave.** O que o laboratório mostrou sobre os hashes sem chave? *Rubrica:* 3 = qualquer pessoa pode calcular o hash de números de associado candidatos e compará-los; os hashes com chave resistem a isso;; 2 = comparação;; 1 = iguais;; 0 = nenhuma.

- **EX042 — Exclusão nos backups.** Como Lucas trata a exclusão de associados nos backups? *Rubrica:* 3 = os backups expiram num calendário em vez de serem editados;; 2 = expiração;; 1 = editar os backups;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) escolher medições que mostrem se os controles funcionam; (2) calcular métricas de cobertura a partir de dados sintéticos; (3) apresentar as evidências com contexto.

### 15.1 O que medir

Hannah pergunta a Lucas como a Fernway pode saber se seus controles funcionam. Contar controles diz pouco. Ele propõe medir resultados e cobertura: a fração de contas da equipe com autenticação resistente a phishing, a fração de notebooks que atendem à baseline, o tempo entre o desligamento e a desativação da conta e o número de serviços expostos encontrados nas varreduras mensais. Cada medida se liga a um risco dos capítulos anteriores. Ele escreve as definições com precisão, por exemplo o que conta como atender à baseline, para que os números signifiquem a mesma coisa todo mês e não possam ser inflados mudando as regras.

### 15.2 Calcular a cobertura

Lucas escreve um script que lê exportações sintéticas do sistema de identidade e da ferramenta de gestão de dispositivos e calcula a cobertura de cada medida, desdobrada por departamento. O laboratório abaixo mostra os números gerais e o departamento com a cobertura mais fraca: a equipe do armazém tem a menor fração de autenticação resistente a phishing, porque muitos compartilham scanners e não têm dispositivos individuais. O desdobramento por departamento transforma uma média única numa ação: o armazém precisa de um projeto de autenticação diferente, talvez login por crachá nos dispositivos compartilhados, e não de um lembrete geral para se cadastrar.

### Laboratório — Cobertura dos controles por departamento

```python
# Coverage of phishing-resistant auth and laptop baseline by department (synthetic export).
staff = {"finance": (12, 11), "buying": (9, 7), "stores": (40, 22), "warehouse": (15, 2), "it": (5, 5)}
laptops = {"finance": (12, 12), "buying": (9, 8), "stores": (14, 11), "warehouse": (3, 2), "it": (6, 6)}
tot = sum(n for n, _ in staff.values()); ok = sum(k for _, k in staff.values())
print(f"phishing-resistant auth: {ok}/{tot} = {ok/tot:.0%}")
for d, (n, k) in sorted(staff.items(), key=lambda x: x[1][1] / x[1][0]): print(f"  {d:9} {k}/{n} = {k/n:.0%}")
tl = sum(n for n, _ in laptops.values()); bl = sum(k for _, k in laptops.values())
print(f"laptops meeting baseline: {bl}/{tl} = {bl/tl:.0%}")
```

Execute com `python3 lab_coverage.py`. Saída verificada:

```text
phishing-resistant auth: 47/81 = 58%
  warehouse 2/15 = 13%
  stores    22/40 = 55%
  buying    7/9 = 78%
  finance   11/12 = 92%
  it        5/5 = 100%
laptops meeting baseline: 39/44 = 89%
```

### 15.3 Evidências em contexto

Lucas apresenta os resultados à direção da Fernway com contagens, porcentagens e tendências, e explica o que cada número mostra e o que não mostra. Uma alta cobertura da baseline não prova que os notebooks estão seguros, só que atendem à baseline; a própria baseline pode deixar passar riscos. Os tempos de desativação dos desligados mostram o desempenho do processo, e não se ex-funcionários usaram indevidamente o acesso. Ele também lista problemas de qualidade dos dados, como dispositivos ausentes da ferramenta de gestão. A medição constrói confiança quando seus limites são declarados ao lado dos seus resultados.

### Exemplo resolvido

Lucas define quatro medidas de cobertura e de tempestividade, calcula-as por departamento e apresenta os resultados com seus limites e notas sobre a qualidade dos dados.

> **Caso sintético.** As exportações e os números são sintéticos.

### Erros e limites

As métricas de cobertura medem a presença dos controles, não sua eficácia. Dispositivos ausentes inflam a cobertura aparente.

### Exercícios

- **EX043 — Definição precisa.** Por que definir com precisão o que é atender à baseline? *Rubrica:* 3 = para que os números signifiquem o mesmo todo mês e não possam ser inflados por redefinição;; 2 = consistência;; 1 = nenhuma;; 0 = nenhuma.

- **EX044 — Departamento mais fraco.** Que departamento teve a cobertura resistente a phishing mais fraca no laboratório, e por quê? *Rubrica:* 3 = o armazém, 2 de 15, scanners compartilhados sem dispositivos individuais;; 2 = armazém;; 1 = financeiro;; 0 = nenhuma.

- **EX045 — Cautela com a cobertura.** O que uma alta cobertura da baseline não prova? *Rubrica:* 3 = que os notebooks estão seguros; só que atendem à baseline;; 2 = limite;; 1 = prova a segurança;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) descrever o que uma arquitetura de segurança contém; (2) aplicar à Fernway o raciocínio por atributos ao estilo do SABSA; (3) produzir uma visão geral de arquitetura para uma pequena organização.

### 16.1 O que uma arquitetura contém

Lucas aprende que uma arquitetura de segurança é uma descrição estruturada de como a segurança é alcançada em toda a organização: princípios, os atributos de negócio que a segurança precisa sustentar, os principais componentes e serviços, como eles se conectam e quem são seus responsáveis. Não é uma lista de produtos. O Dr. Bellini apresenta o SABSA, descrito por Sherwood, Clark e Lynas (2005), que parte dos atributos de negócio, e o guia do The Open Group sobre a integração de risco e segurança no TOGAF. Ambos enfatizam que a arquitetura liga aquilo que o negócio valoriza àquilo que é construído e operado.

### 16.2 Atributos para a Fernway

Lucas trabalha com Hannah para definir os atributos principais da Fernway: disponível, para que a loja venda nas temporadas de pico; confiável, para que os associados confiem seus dados à Fernway; exata, para que estoque e preços estejam corretos; e em conformidade, para que as obrigações de cartões e de privacidade sejam cumpridas. Para cada atributo, ele lista os serviços que o sustentam. A disponibilidade depende da hospedagem em nuvem e da resposta a incidentes; a confiabilidade depende de identidade, privacidade e proteção do checkout. Quando alguém propõe cortar um serviço, o mapa de atributos mostra qual valor de negócio seria enfraquecido, transformando debates técnicos em debates de negócio.

### 16.3 Um documento de visão geral

Lucas escreve uma visão geral de arquitetura de dez páginas: princípios como negar por padrão e menor privilégio; atributos; um diagrama de zonas e serviços; os principais serviços de segurança, incluindo identidade, logging, backup e integração de pagamentos; responsáveis; e lacunas conhecidas, com planos. Ele a mantém curta para que seja lida. Hannah a apresenta ao conselho da Fernway, que pela primeira vez vê a segurança como um projeto coerente, e não como uma série de compras. A visão geral se torna a referência para as futuras revisões de projetos. Ela é revista toda primavera.

### Exemplo resolvido

Lucas define quatro atributos de negócio para a Fernway, mapeia os serviços que os sustentam e escreve uma visão geral de arquitetura de dez páginas apresentada ao conselho.

> **Caso sintético.** Os atributos e a visão geral são sintéticos; o SABSA e o TOGAF G152 são reais.

### Erros e limites

As visões gerais simplificam; os detalhes ficam em documentos de apoio. Os atributos precisam ser revistos quando o negócio muda.

### Exercícios

- **EX046 — Não é uma lista de produtos.** Por que uma arquitetura de segurança não é uma lista de produtos? *Rubrica:* 3 = descreve princípios, atributos, serviços, conexões e responsáveis;; 2 = estrutura;; 1 = é sim;; 0 = nenhuma.

- **EX047 — Uso dos atributos.** Como o mapa de atributos ajuda quando alguém propõe cortar um serviço? *Rubrica:* 3 = mostra qual valor de negócio seria enfraquecido;; 2 = valor;; 1 = nenhuma;; 0 = nenhuma.

- **EX048 — Efeito no conselho.** O que a visão geral mudou para o conselho da Fernway? *Rubrica:* 3 = passaram a ver a segurança como um projeto coerente, e não como compras;; 2 = coerente;; 1 = nada;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Conceitos de criptografia

### Objetivos de aprendizagem

Você vai (1) explicar os principais blocos criptográficos e seus usos; (2) posicionar a criptografia na arquitetura da Fernway; (3) identificar as responsabilidades de gestão de chaves.

### 17.1 Blocos de construção

Lucas estuda criptografia simétrica, hashing, códigos de autenticação de mensagem, assinaturas digitais e troca de chaves, usando o livro de Katz e Lindell como base. Ele se concentra no que cada um oferece. A criptografia oferece confidencialidade; a criptografia autenticada, como o AES-GCM, também oferece integridade. Os hashes oferecem impressões digitais; os códigos de autenticação de mensagem oferecem integridade e autenticidade entre partes que compartilham uma chave; as assinaturas permitem que qualquer pessoa verifique a origem com uma chave pública. A troca de chaves permite que duas partes acordem uma chave por uma rede aberta. Os arquitetos escolhem entre eles conforme a necessidade e nunca projetam novos.

### 17.2 Criptografia na Fernway

Lucas mapeia onde a criptografia é usada: TLS para a loja e o e-mail; a tokenização do provedor de pagamentos, para que a Fernway nunca armazene números de cartão; webhooks do parceiro de entregas assinados com HMAC; criptografia de disco nos notebooks; backups criptografados; e a pseudonimização do capítulo 14. Para cada um, ele anota o objetivo e quem guarda a chave. Ele descobre que o segredo do webhook do parceiro de entregas é o mesmo em teste e em produção, o que significa que um vazamento de um sistema de teste permitiria forjar atualizações de entrega em produção. Ele recomenda segredos separados por ambiente.

### 17.3 Responsabilidades de gestão de chaves

Cada uso de criptografia cria deveres de gestão de chaves: geração, armazenamento seguro, rotação, revogação e destruição, como descreve o NIST SP 800-57 Part 1 Rev. 5. Lucas lista as chaves e os segredos da Fernway com responsáveis e períodos de rotação. Vários não tinham responsável ou nunca haviam sido rotacionados. Ele recomenda um gerenciador de segredos para os segredos das aplicações e um calendário para as renovações de certificados. Ele observa que a maioria das falhas criptográficas em pequenas organizações vem do manuseio das chaves, e não de algoritmos fracos, então a responsabilidade e a rotação merecem tanta atenção quanto a escolha do algoritmo.

### Exemplo resolvido

Lucas resume cinco blocos de construção, mapeia seis usos na Fernway, encontra um segredo de webhook compartilhado entre teste e produção e monta um inventário de chaves com responsáveis.

> **Caso sintético.** As chaves e os segredos da Fernway são sintéticos; Katz e Lindell e o SP 800-57 Part 1 Rev. 5 são reais.

### Erros e limites

Chaves gerenciadas pelo provedor reduzem o ônus, mas acrescentam dependência. A rotação pode quebrar integrações se não for coordenada.

### Exercícios

- **EX049 — Assinatura versus MAC.** O que uma assinatura oferece que um MAC não oferece? *Rubrica:* 3 = verificação pública sem a capacidade de assinar;; 2 = verificação pública;; 1 = o mesmo;; 0 = nenhuma.

- **EX050 — Segredo de webhook compartilhado.** Por que um único segredo de webhook para teste e produção é um problema? *Rubrica:* 3 = um vazamento em teste permitiria forjar atualizações em produção;; 2 = forjar;; 1 = nenhuma;; 0 = nenhuma.

- **EX051 — Principal fonte de falhas.** De onde vem a maioria das falhas criptográficas em pequenas organizações? *Rubrica:* 3 = do manuseio das chaves, e não de algoritmos fracos;; 2 = chaves;; 1 = algoritmos;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Métodos de pesquisa I

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta pesquisável sobre a segurança da Fernway; (2) escolher entre levantamento, estudo de caso e experimento; (3) planejar uma coleta de dados ética.

### 18.1 Formular uma pergunta

O Dr. Bellini pede a Lucas que transforme seu estágio num projeto de pesquisa. Lucas parte de um interesse vago em saber se a equipe segue a política de segurança e o estreita até uma pergunta que consegue responder: os funcionários das lojas da Fernway que receberam breves orientações presenciais na loja reportam e-mails suspeitos com mais frequência do que os que receberam apenas o módulo online? A pergunta nomeia uma população, uma intervenção, uma comparação e um desfecho. Ela pode ser respondida com dados que a Fernway já coleta por meio do seu botão de reportar phishing, e importa para Hannah porque orienta como o orçamento de treinamento é gasto.

### 18.2 Escolher um método

Lucas considera três métodos. Um levantamento perguntaria aos funcionários o que eles fazem, mas os autorrelatos exageram o bom comportamento. Um estudo de caso descreveria uma loja em profundidade, mas não permitiria a comparação. Um quase-experimento que compare lojas que receberam as orientações com lojas semelhantes que não receberam, usando as taxas reais de reporte, dá a resposta mais forte disponível. Wohlin e colegas (2012) descrevem como desenhar estudos assim em contextos de software e sistemas, incluindo as ameaças à validade. Lucas escolhe o quase-experimento e observa que as lojas não foram atribuídas aleatoriamente, o que limita as afirmações causais.

### 18.3 Ética e dados

Lucas submete o projeto ao comitê de ética da Ashgrove. Ele usará apenas contagens agregadas de reportes por loja e por mês, sem nomes individuais, e a direção da Fernway concorda por escrito. Os funcionários são informados por meio de um aviso de que os dados por loja serão usados num estudo de estudante. Ele guarda os dados nos sistemas da universidade, exclui-os depois do projeto e compartilhará apenas resultados agregados. O comitê aprova com a condição de que as lojas com menos de cinco funcionários sejam agrupadas, para que o comportamento de nenhum indivíduo possa ser inferido a partir do número de uma loja.

### Exemplo resolvido

Lucas estreita um interesse vago até uma pergunta comparativa, escolhe um quase-experimento em vez de levantamento e estudo de caso e obtém aprovação ética com uma condição de agrupamento das células pequenas.

> **Caso sintético.** O estudo e as lojas são sintéticos; Wohlin et al. (2012) é real.

### Erros e limites

A atribuição não aleatória limita as afirmações causais. O uso do botão de reporte é apenas um indicador de vigilância.

### Exercícios

- **EX052 — Partes da pergunta.** Que quatro partes a pergunta de Lucas nomeia? *Rubrica:* 3 = população, intervenção, comparação e desfecho;; 2 = três das quatro;; 1 = nenhuma;; 0 = nenhuma.

- **EX053 — Por que não um levantamento.** Por que Lucas rejeitou um levantamento como método principal? *Rubrica:* 3 = os autorrelatos exageram o bom comportamento;; 2 = viés;; 1 = custo;; 0 = nenhuma.

- **EX054 — Condição das células pequenas.** Por que o comitê exigiu agrupar as lojas pequenas? *Rubrica:* 3 = para que o comportamento individual não possa ser inferido a partir do número de uma loja;; 2 = privacidade;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Arquitetura e engenharia de segurança: escopo e teoria

### Objetivos de aprendizagem

Você vai (1) declarar o que a arquitetura e a engenharia de segurança cobrem; (2) aplicar à Fernway os princípios de Saltzer e Schroeder; (3) relacionar a teoria às revisões práticas de projeto.

### 19.1 Escopo

Lucas escreve um ensaio curto sobre o escopo da área. A arquitetura de segurança descreve como a proteção é organizada em toda a organização; a engenharia de segurança é a disciplina de construir sistemas que continuam confiáveis sob ataque, como diz Anderson (2020). Ambas cobrem pessoas, processos e tecnologia, e ambas atuam ao longo do ciclo de vida, dos requisitos à desativação. O NIST SP 800-160 Vol. 1 Rev. 1 enquadra isso como engenharia de segurança de sistemas, integrada à engenharia normal, e não acrescentada no fim. Lucas observa que, numa cooperativa do tamanho da Fernway, uma pessoa muitas vezes faz as duas coisas.

### 19.2 Princípios clássicos

Lucas aplica à Fernway os princípios de projeto de Saltzer e Schroeder (1975). A economia de mecanismo sugere um único provedor de identidade, em vez de logins separados para cada sistema. Os padrões fail-safe significam que as contas de novos funcionários começam sem acesso. A mediação completa significa que toda requisição ao sistema de estoque é verificada, e não só a primeira. O menor privilégio significa que as contas do armazém não podem mudar preços. A aceitabilidade psicológica significa que os controles precisam se encaixar nas rotinas atarefadas das lojas, ou a equipe vai contorná-los. Ele descobre que princípios de quase cinquenta anos ainda explicam a maior parte das fraquezas da Fernway.

### 19.3 A teoria nas revisões

Hannah pergunta como a teoria ajuda no dia a dia. Lucas transforma os princípios em perguntas de revisão para novos projetos: qual é o acesso padrão, toda requisição é verificada, quem tem o menor privilégio necessário e a equipe vai achar o controle aceitável. Ele as usa num aplicativo proposto de escalas de trabalho e descobre que ele daria a todo gerente acesso às escalas de todas as lojas, violando o menor privilégio. O fornecedor acrescenta um escopo por loja. A teoria dá aos revisores um vocabulário compartilhado e um checklist fundamentado em décadas de experiência.

### Exemplo resolvido

Lucas define a área, aplica à Fernway cinco princípios de Saltzer e Schroeder e os usa para corrigir o escopo de acesso de um aplicativo de escalas.

> **Caso sintético.** A Fernway e o aplicativo de escalas são sintéticos; Anderson (2020), o SP 800-160v1r1 e Saltzer e Schroeder (1975) são reais.

### Erros e limites

Os princípios podem entrar em conflito, como o menor privilégio versus a aceitabilidade. O julgamento continua necessário.

### Exercícios

- **EX055 — Padrão fail-safe.** Como a Fernway aplica os padrões fail-safe? *Rubrica:* 3 = as contas de novos funcionários começam sem acesso;; 2 = sem acesso;; 1 = acesso aberto;; 0 = nenhuma.

- **EX056 — Aceitabilidade.** Por que a aceitabilidade psicológica importa nas lojas? *Rubrica:* 3 = controles que não se encaixam nas rotinas são contornados;; 2 = contorno;; 1 = nenhuma;; 0 = nenhuma.

- **EX057 — Achado do aplicativo de escalas.** O que os princípios revelaram sobre o aplicativo de escalas? *Rubrica:* 3 = todo gerente podia ver todas as lojas, violando o menor privilégio;; 2 = menor privilégio;; 1 = nada;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Arquitetura e engenharia de segurança: casos fundamentais

### Objetivos de aprendizagem

Você vai (1) analisar incidentes publicados em busca de lições de arquitetura; (2) relacionar as lições à Fernway; (3) escrever uma análise de caso curta.

### 20.1 Aprender com os casos

O Dr. Bellini passa três padrões de incidentes públicos bem documentados, em vez de histórias de empresas específicas: comprometimento por meio de um fornecedor com acesso à rede, roubo de dados de um bucket de armazenamento em nuvem exposto e um ransomware que se espalhou porque os backups eram alcançáveis a partir da mesma rede. Lucas analisa cada um em busca de causas de arquitetura, e não de culpa individual. O caso do fornecedor mostra confiança excessiva; o do armazenamento mostra padrões fracos e falta de monitoramento; o do ransomware mostra um único domínio de falha. Cada um aponta para um princípio de projeto que poderia ter limitado o dano.

### 20.2 Relacionar à Fernway

Lucas confere a Fernway contra cada padrão. O terceirizado de montagem de lojas tem uma conta de VPN permanente com acesso amplo, o que corresponde ao padrão do fornecedor; ele recomenda acesso com prazo limitado, aprovado a cada trabalho. As imagens de produtos da Fernway ficam num bucket na nuvem, corretamente público, mas uma pasta de exportação no mesmo bucket guarda um arquivo de estoque; ele recomenda um bucket privado separado. Os backups já estão offline desde o capítulo 11. O mapeamento transforma casos abstratos em três ações concretas, ordenadas pelo tamanho da lacuna e pela facilidade da correção.

### 20.3 Escrever uma análise de caso

Lucas escreve cada análise numa estrutura fixa: o que aconteceu, as causas de arquitetura, o que teria limitado o impacto e a relevância para a Fernway. Ele deixa a culpa de fora e cita orientações publicadas onde se aplicam, como o SP 800-207 para limitar a confiança em fornecedores. Cada análise tem menos de uma página. Hannah as compartilha com os gestores da Fernway, que acham casos curtos e estruturados mais persuasivos do que avisos genéricos. Lucas aprende que o valor de um caso está na lição de projeto transferível, e não no drama do incidente.

### Exemplo resolvido

Lucas analisa três padrões de incidentes em busca de causas de arquitetura, relaciona-os à Fernway e produz três ações ordenadas em análises de uma página.

> **Caso sintético.** Os padrões de incidentes são genéricos e sintéticos; o SP 800-207 é real.

### Erros e limites

Os padrões genéricos podem deixar passar detalhes locais. As lições dos casos precisam ser conferidas com as configurações atuais.

### Exercícios

- **EX058 — Padrão do fornecedor.** Que arranjo da Fernway correspondia ao padrão do fornecedor? *Rubrica:* 3 = a conta de VPN permanente e ampla do terceirizado de montagem de lojas;; 2 = terceirizado;; 1 = nenhuma;; 0 = nenhuma.

- **EX059 — Correção do bucket.** O que Lucas recomendou para o bucket na nuvem? *Rubrica:* 3 = mover a pasta de exportação para um bucket privado separado;; 2 = separar;; 1 = apagar as imagens;; 0 = nenhuma.

- **EX060 — Valor de um caso.** Onde está o valor de um caso? *Rubrica:* 3 = na lição de projeto transferível;; 2 = lição;; 1 = drama;; 0 = nenhuma.

<a id="ch-21"></a>

## Capítulo 21 — Arquitetura e engenharia de segurança: modelos de sistema

### Objetivos de aprendizagem

Você vai (1) construir um modelo do sistema de pedidos da Fernway; (2) identificar as fronteiras de confiança e os ativos; (3) usar o modelo numa revisão STRIDE.

### 21.1 Construir o modelo

Lucas desenha um diagrama de fluxo de dados do sistema de pedidos da Fernway: o navegador do cliente, a loja web, o provedor de pagamentos, o banco de dados de estoque, o aplicativo de separação do armazém e o parceiro de entregas. Ele marca os processos, os repositórios de dados, as entidades externas e os fluxos, e rotula o que cada fluxo carrega. Ele valida o diagrama com o desenvolvedor e com o gerente do armazém, que corrigem dois fluxos que ele havia deixado passar: uma importação noturna de preços de um fornecedor e um upload manual de planilha. Os modelos só são úteis se as pessoas que operam o sistema concordarem que estão corretos.

### 21.2 Fronteiras e ativos

Lucas marca as fronteiras de confiança onde os dados passam entre partes ou níveis de privilégio: entre o navegador e a loja, a loja e o provedor de pagamentos, a Fernway e o parceiro de entregas, e entre a rede do escritório e a nuvem. Ele lista os ativos: dados dos clientes, histórico de pedidos, preços e níveis de estoque. O upload manual de planilha atravessa uma fronteira sem nenhuma validação, o que significa que um arquivo equivocado ou malicioso poderia mudar preços em toda a loja. Marcar as fronteiras torna visíveis lacunas assim, porque toda travessia deveria ter uma verificação definida.

### 21.3 Revisão STRIDE

Usando as categorias STRIDE de Shostack (2014), Lucas examina cada elemento. Spoofing: os webhooks do parceiro de entregas são assinados. Tampering: o upload de planilha não tem validação. Repudiation: as mudanças de preço não são registradas com o usuário que as fez. Information disclosure: o histórico de pedidos é acessível a todas as contas da equipe. Denial of service: a loja depende de uma única região de hospedagem. Elevation of privilege: o aplicativo de separação roda com direitos de dono do banco de dados. Ele registra sete ameaças com mitigações propostas e responsáveis, e a Fernway agenda as três principais para o próximo trimestre.

### Exemplo resolvido

Lucas constrói e valida um modelo de fluxo de dados, marca quatro fronteiras de confiança e conduz uma revisão STRIDE que produz sete ameaças com responsáveis.

> **Caso sintético.** O sistema de pedidos é sintético; Shostack (2014) é real.

### Erros e limites

Os modelos envelhecem à medida que os sistemas mudam. O STRIDE encontra categorias de ameaças, não todos os ataques.

### Exercícios

- **EX061 — Validar o modelo.** O que o desenvolvedor e o gerente do armazém acrescentaram? *Rubrica:* 3 = uma importação noturna de preços de um fornecedor e um upload manual de planilha;; 2 = um fluxo;; 1 = nenhuma;; 0 = nenhuma.

- **EX062 — Travessia sem validação.** Por que o upload de planilha é uma preocupação? *Rubrica:* 3 = atravessa uma fronteira sem validação e poderia mudar preços;; 2 = validação;; 1 = nenhuma;; 0 = nenhuma.

- **EX063 — Achado de repúdio.** Que lacuna de repúdio o STRIDE encontrou? *Rubrica:* 3 = as mudanças de preço não são registradas com o usuário;; 2 = logging;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-22"></a>

## Capítulo 22 — Arquitetura e engenharia de segurança: dados e dependências

### Objetivos de aprendizagem

Você vai (1) classificar os dados da Fernway; (2) mapear as dependências de fornecedores e serviços; (3) identificar pontos únicos de falha.

### 22.1 Classificar os dados

Lucas propõe três classes de dados para a Fernway: públicos, como as descrições de produtos; internos, como os níveis de estoque e as escalas; e confidenciais, como os dados dos associados, os registros dos funcionários e os contratos com fornecedores. Cada classe tem regras de manuseio para armazenamento, compartilhamento e descarte. Ele mantém o esquema pequeno porque a equipe precisa aplicá-lo sem manuais de treinamento. Ele rotula os principais repositórios de dados com sua classe e descobre que uma pasta do drive compartilhado chamada "misc" guarda registros confidenciais de funcionários ao lado de imagens públicas de marketing, o que significa que qualquer pessoa com acesso de marketing pode ler os dados da folha de pagamento.

### 22.2 Mapear as dependências

Lucas lista todos os serviços externos dos quais a Fernway depende: hospedagem, pagamentos, e-mail, entregas, identidade, contabilidade e o feed de preços do fornecedor. Para cada um, registra os dados compartilhados, o responsável pelo contrato, se o fornecedor tem compromissos de segurança e o que acontece se o serviço falhar. O laboratório abaixo modela as dependências como um grafo e conta quantas funções de negócio cada serviço sustenta. A identidade e a hospedagem sustentam, cada uma, todas as funções online, então sua falha pararia quase tudo de uma vez, enquanto o feed de preços afeta só as atualizações de preços.

### Laboratório — Contagem das funções afetadas por cada dependência

```python
# Count business functions depending on each service (synthetic map).
deps = {"online sales": ["hosting", "identity", "payment", "email"],
        "click-and-collect": ["hosting", "identity", "email"],
        "delivery tracking": ["hosting", "identity", "delivery"],
        "member accounts": ["hosting", "identity", "email"],
        "pricing updates": ["hosting", "identity", "price feed"],
        "month-end accounts": ["accounting"]}
count = {}
for f, svcs in deps.items():
    for s in svcs: count[s] = count.get(s, 0) + 1
for s, n in sorted(count.items(), key=lambda x: (-x[1], x[0])): print(f"{s:11} supports {n} function(s)")
```

Execute com `python3 lab_deps.py`. Saída verificada:

```text
hosting     supports 5 function(s)
identity    supports 5 function(s)
email       supports 3 function(s)
accounting  supports 1 function(s)
delivery    supports 1 function(s)
payment     supports 1 function(s)
price feed  supports 1 function(s)
```

### 22.3 Pontos únicos de falha

A contagem de dependências mostra onde a resiliência mais importa. Lucas recomenda um procedimento manual de contingência documentado para a identidade, como uma conta break-glass lacrada, e a confirmação de que o plano do provedor de hospedagem inclui a recuperação numa segunda região. Para o provedor de pagamentos, ele indica um compromisso contratual em vez de redundância técnica, já que um segundo provedor de pagamentos custaria mais do que o risco justifica. Ele explica que nem todo ponto único de falha precisa ser eliminado; alguns são aceitos conscientemente, com um plano de recuperação e um responsável que acompanha o fornecedor.

### Exemplo resolvido

Lucas define três classes de dados, encontra registros confidenciais numa pasta misturada, mapeia sete dependências e as ordena pelas funções afetadas.

> **Caso sintético.** Os dados, os serviços e as contagens são sintéticos.

### Erros e limites

Os mapas de dependências deixam de fora as quartas partes, os fornecedores dos fornecedores. As classificações derivam sem revisão periódica.

### Exercícios

- **EX064 — Pasta misturada.** O que havia de errado com a pasta misc? *Rubrica:* 3 = registros confidenciais de funcionários ao lado de imagens públicas, legíveis pelo marketing;; 2 = classes misturadas;; 1 = nada;; 0 = nenhuma.

- **EX065 — Dependência mais ampla.** Que serviços sustentaram mais funções no laboratório? *Rubrica:* 3 = identidade e hospedagem, 5 funções cada;; 2 = identidade;; 1 = feed de preços;; 0 = nenhuma.

- **EX066 — Aceitar uma dependência.** Por que manter um único provedor de pagamentos? *Rubrica:* 3 = um segundo custaria mais do que o risco; coberto por contrato e um plano;; 2 = custo;; 1 = precisa eliminar;; 0 = nenhuma.

<a id="ch-23"></a>

## Capítulo 23 — Arquitetura e engenharia de segurança: métodos I

### Objetivos de aprendizagem

Você vai (1) aplicar um método de avaliação de risco a um projeto da Fernway; (2) estimar probabilidade e impacto de forma consistente; (3) documentar as decisões para revisão.

### 23.1 Um método de avaliação de risco

A Fernway planeja um serviço de click-and-collect (compra online com retirada na loja). Lucas conduz uma avaliação de risco usando a estrutura do NIST SP 800-30 Rev. 1: identificar fontes e eventos de ameaça, vulnerabilidades, probabilidade, impacto e o risco resultante. Ele a reduz para uma cooperativa, usando um modelo de uma página por risco. Os eventos de ameaça incluem alguém retirar o pedido de outro cliente e funcionários usarem indevidamente os números de telefone dos clientes. Ele envolve uma gerente de loja, porque as pessoas que operam o processo sabem onde ele pode dar errado de maneiras que um diagrama nunca mostra. O modelo cabe numa única página para que seja usado.

### 23.2 Estimativas consistentes

Lucas define escalas de probabilidade e de impacto com exemplos, para que pessoas diferentes classifiquem de forma consistente: probabilidade alta significa esperado várias vezes por ano na Fernway; impacto alto significa perda acima de um valor definido ou dano a muitos associados. Ele pede que Hannah e a gerente da loja classifiquem os mesmos cinco riscos de forma independente e depois compara as classificações. Elas divergem em dois, e a discussão revela que a gerente sabe de erros passados na retirada de que Hannah nunca tinha ouvido falar. Escalas consistentes ajudam, mas é na discussão das diferenças que surge a maior parte das informações.

### 23.3 Documentar as decisões

Para cada risco, Lucas registra a classificação, o tratamento proposto e quem decide. A retirada pela pessoa errada é tratada com um código de retirada enviado por SMS e conferido no balcão. O uso indevido dos números de telefone é tratado mascarando os números no aplicativo da loja depois da retirada. Um risco baixo, um e-mail de notificação atrasado, é aceito. Cada decisão tem uma data de revisão. O registro permite que auditores e futuros funcionários vejam por que as escolhas foram feitas, o que importa quando as pessoas saem e o raciocínio, de outro modo, se perderia.

### Exemplo resolvido

Lucas aplica ao click-and-collect uma avaliação no estilo do SP 800-30 com escalas definidas, compara classificações independentes e registra as decisões de tratamento.

> **Caso sintético.** O projeto e as classificações são sintéticos; o SP 800-30 Rev. 1 é real.

### Erros e limites

As escalas qualitativas escondem a incerteza. Equipes pequenas podem compartilhar pontos cegos apesar da classificação independente.

### Exercícios

- **EX067 — Por que uma gerente de loja.** Por que Lucas envolveu uma gerente de loja? *Rubrica:* 3 = as pessoas que operam o processo sabem onde ele falha;; 2 = conhecimento local;; 1 = nenhuma;; 0 = nenhuma.

- **EX068 — Diferenças de classificação.** O que a comparação das classificações independentes revelou? *Rubrica:* 3 = erros passados na retirada conhecidos só pela gerente da loja;; 2 = informação nova;; 1 = nada;; 0 = nenhuma.

- **EX069 — Tratamento da retirada pela pessoa errada.** Como a retirada pela pessoa errada foi tratada? *Rubrica:* 3 = um código de retirada por SMS conferido no balcão;; 2 = código;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-24"></a>

## Capítulo 24 — Arquitetura e engenharia de segurança: controles

### Objetivos de aprendizagem

Você vai (1) selecionar controles de um catálogo para a Fernway; (2) adaptar os controles a uma pequena organização; (3) ligar os controles a riscos e responsáveis.

### 24.1 Usar um catálogo

Lucas usa o NIST SP 800-53 Rev. 5 e a ISO/IEC 27002:2022 como catálogos, e não como checklists. Ele procura controles que tratem os riscos já registrados: controle de acesso, registro de auditoria, gestão de configuração, relacionamento com fornecedores e resposta a incidentes. Os catálogos o ajudam a não esquecer áreas inteiras, como o descarte de mídias, que a Fernway nunca havia considerado para os discos rígidos dos caixas antigos. Ele mantém uma lista curta de cerca de trinta controles que importam para a Fernway, em vez de tentar implementar centenas escritos para organizações muito maiores. A lista curta é revista todo ano.

### 24.2 Adaptação

Cada controle selecionado é adaptado ao tamanho da Fernway. O controle de revisão de auditoria do SP 800-53 vira uma revisão mensal de trinta minutos dos alertas de identidade feita por Hannah, e não um centro de operações de segurança. A gestão de configuração vira uma única baseline para os notebooks, gerenciada pela ferramenta de dispositivos. Os controles de fornecedores viram um questionário de uma página e uma cláusula contratual. Lucas registra os motivos da adaptação, para que um auditor veja que o controle foi considerado e adaptado deliberadamente. A adaptação é o modo como os frameworks se tornam utilizáveis por organizações sem grandes equipes de segurança.

### 24.3 Ligar controles a riscos

Lucas monta uma tabela que liga cada controle aos riscos que reduz, a seu responsável e à sua evidência, como um registro de revisão ou um relatório de configuração. Os controles sem risco ligado são questionados; dois se revelam resquícios das exigências de uma antiga seguradora e são aposentados. Os riscos sem controle ligado são sinalizados como lacunas. A tabela se torna a declaração da Fernway sobre como a segurança é alcançada e dá ao conselho uma forma de acompanhar o progresso sem ler detalhes técnicos. Ela também torna as auditorias posteriores mais rápidas.

### Exemplo resolvido

Lucas seleciona cerca de trinta controles do SP 800-53 e da ISO/IEC 27002, adapta-os ao tamanho da Fernway e liga cada um a riscos, responsáveis e evidências.

> **Caso sintético.** A lista de controles da Fernway é sintética; o SP 800-53 Rev. 5 e a ISO/IEC 27002:2022 são reais.

### Erros e limites

A adaptação pode descambar para o enfraquecimento dos controles. A evidência precisa ser real, e não uma promessa.

### Exercícios

- **EX070 — Área esquecida.** Que área a Fernway nunca havia considerado? *Rubrica:* 3 = o descarte de mídias dos discos rígidos dos caixas antigos;; 2 = descarte;; 1 = nenhuma;; 0 = nenhuma.

- **EX071 — Revisão de auditoria adaptada.** Como a revisão de auditoria foi adaptada? *Rubrica:* 3 = uma revisão mensal de trinta minutos dos alertas de identidade;; 2 = revisão mensal;; 1 = um centro de operações de segurança;; 0 = nenhuma.

- **EX072 — Controles sem ligação.** O que aconteceu com os controles sem risco ligado? *Rubrica:* 3 = foram questionados; dois resquícios foram aposentados;; 2 = aposentados;; 1 = mantidos;; 0 = nenhuma.

<a id="ch-25"></a>

## Capítulo 25 — Laboratório I

### Objetivos de aprendizagem

Você vai (1) construir um pequeno verificador de controle de acesso; (2) testar o menor privilégio sobre dados sintéticos de papéis; (3) relatar os resultados com suas limitações.

### 25.1 A tarefa

O Dr. Bellini propõe um exercício de laboratório: escrever um programa em Python que leia as definições sintéticas de papéis e as atribuições de usuários da Fernway e encontre os usuários cujas permissões excedem as necessidades da sua função. Lucas define do que cada função deve precisar, como a equipe de caixa precisar de vendas, mas não de mudanças de preço, e compara isso com o que cada usuário de fato tem. O programa roda offline sobre dados sintéticos, para que possa ser compartilhado com os colegas sem expor contas reais. O objetivo é praticar a transformação de um princípio, o menor privilégio, numa verificação repetível.

### Laboratório — Encontrar permissões além das necessidades da função

```python
# Find permissions beyond job needs (synthetic roles and users).
need = {"till": {"sales"}, "store-manager": {"sales", "rota", "refunds"},
        "warehouse": {"picking", "stock-read"}, "buyer": {"stock-read", "price-change"}}
users = {"u01": ("till", {"sales"}), "u02": ("till", {"sales", "price-change"}),
         "u03": ("till", {"sales", "price-change"}), "u04": ("store-manager", {"sales", "rota", "refunds"}),
         "u05": ("warehouse", {"picking", "stock-read", "db-owner"}), "u06": ("buyer", {"stock-read", "price-change"}),
         "u07": ("warehouse", {"picking", "stock-read"})}
found = 0
for u, (job, has) in sorted(users.items()):
    extra = has - need[job]
    if extra: found += 1; print(f"{u} ({job}) excess: {', '.join(sorted(extra))}")
print(f"{found} of {len(users)} users exceed job needs")
```

Execute com `python3 lab_excess.py`. Saída verificada:

```text
u02 (till) excess: price-change
u03 (till) excess: price-change
u05 (warehouse) excess: db-owner
3 of 7 users exceed job needs
```

### 25.2 Resultados

O laboratório encontra três usuários com permissões em excesso. Dois funcionários de loja têm direitos de mudança de preço que sobraram de um projeto temporário de promoção, e um usuário do armazém tem direitos de dono do banco de dados concedidos durante uma correção urgente. Lucas confirma com Hannah que as definições das funções estão certas antes de chamar isso de achados, porque uma definição incorreta produziria alarmes falsos. Hannah remove os direitos da promoção na mesma semana e abre um ticket de mudança para substituir o direito de dono do banco por um papel mais restrito, depois que o desenvolvedor confirmar do que a tarefa do armazém precisa.

### 25.3 Limitações

Lucas lista os limites do seu verificador. Ele só conhece as permissões registradas na exportação, e não as que existem dentro de aplicações com listas de usuários próprias. As definições das funções são simplificadas e podem deixar de fora exceções legítimas. Ele encontra excessos, e não uso indevido. Ele sugere rodá-lo todo mês e acrescentar um campo para exceções aprovadas com datas de expiração, para que os direitos temporários fiquem visíveis em vez de esquecidos. O Dr. Bellini elogia a seção honesta de limitações, observando que os revisores confiam mais nas ferramentas quando seus autores dizem com clareza o que elas não conseguem fazer.

### Exemplo resolvido

Lucas escreve um verificador offline de menor privilégio, encontra três permissões em excesso, confirma as definições com Hannah e lista os limites do verificador.

> **Caso sintético.** Os papéis e os usuários são sintéticos.

### Erros e limites

As permissões internas das aplicações são invisíveis para o verificador. As exceções precisam de expiração para continuarem honestas.

### Exercícios

- **EX073 — Excesso encontrado.** Quantos usuários tinham permissões em excesso, e por quê? *Rubrica:* 3 = três: dois resquícios da promoção e um direito de dono do banco de uma correção urgente;; 2 = três;; 1 = nenhuma;; 0 = nenhuma.

- **EX074 — Conferir as definições.** Por que confirmar as definições das funções antes de relatar? *Rubrica:* 3 = definições erradas causam alarmes falsos;; 2 = exatidão;; 1 = nenhuma;; 0 = nenhuma.

- **EX075 — Campo de exceções.** Que melhoria Lucas sugeriu para as exceções? *Rubrica:* 3 = um campo de exceção aprovada com datas de expiração;; 2 = expiração;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-26"></a>

## Capítulo 26 — Arquitetura e engenharia de segurança: métodos II

### Objetivos de aprendizagem

Você vai (1) usar árvores de ataque para analisar um objetivo; (2) comparar projetos pelo custo para o atacante; (3) combinar métodos para uma decisão de projeto.

### 26.1 Árvores de ataque

Lucas analisa o objetivo "obter o histórico de pedidos de um associado" com uma árvore de ataque, um método que Shostack (2014) descreve junto com o STRIDE. A raiz é o objetivo; os ramos são as maneiras de alcançá-lo: adivinhar ou roubar a senha do associado, abusar de uma conta da equipe, explorar a página de pedidos ou obter uma exportação antiga. Cada ramo se divide em etapas. Escrever a árvore o obriga a pensar como um atacante sobre caminhos, em vez de listar controles. Ele descobre que o ramo da exportação antiga, uma planilha velha enviada por e-mail a uma agência de marketing, não exige nenhuma habilidade técnica.

### 26.2 Comparar projetos

Lucas atribui níveis aproximados de esforço às etapas-folha e compara dois projetos para as contas dos associados: senhas com redefinição por e-mail, e passkeys com contingência por e-mail. Para cada projeto, o caminho mais barato até o objetivo mostra a rota provável do atacante. Com senhas, o credential stuffing é o mais barato. Com passkeys, a contingência por e-mail se torna a mais barata, então a força do projeto depende de proteger a redefinição por e-mail. A comparação mostra que acrescentar um método forte não ajuda muito se continuar existindo uma contingência fraca, uma lição que vale muito além da Fernway.

### 26.3 Combinar métodos

Lucas combina seus resultados do STRIDE, a árvore de ataque e as classificações de risco numa única recomendação: adotar passkeys, exigir um segundo fator para a contingência por e-mail e recolher a exportação antiga da agência, com um acordo de compartilhamento de dados para o futuro. Cada método contribuiu com algo diferente: o STRIDE deu amplitude, a árvore deu os caminhos do atacante e as classificações de risco deram a prioridade. O Dr. Bellini observa que arquitetos experientes combinam métodos rotineiramente, porque cada um tem pontos cegos que os outros cobrem em parte. Lucas registra qual método encontrou cada problema.

### Exemplo resolvido

Lucas constrói uma árvore de ataque para o roubo do histórico de pedidos, compara os projetos com senhas e com passkeys pelo caminho mais barato e combina métodos numa recomendação.

> **Caso sintético.** A árvore e os projetos são sintéticos; Shostack (2014) é real.

### Erros e limites

As estimativas de esforço são julgamentos grosseiros. As árvores podem deixar de fora ramos que ninguém imaginou.

### Exercícios

- **EX076 — Ramo de baixa habilidade.** Que ramo não exigia nenhuma habilidade técnica? *Rubrica:* 3 = a exportação antiga enviada por e-mail a uma agência de marketing;; 2 = exportação antiga;; 1 = senha;; 0 = nenhuma.

- **EX077 — Ponto fraco das passkeys.** O que se tornou o caminho mais barato com as passkeys? *Rubrica:* 3 = a contingência por e-mail;; 2 = contingência;; 1 = passkeys;; 0 = nenhuma.

- **EX078 — Contribuições dos métodos.** Com o que contribuíram o STRIDE, a árvore e as classificações? *Rubrica:* 3 = amplitude, caminhos do atacante e prioridade;; 2 = dois dos três;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-27"></a>

## Capítulo 27 — Arquitetura e engenharia de segurança: verificação

### Objetivos de aprendizagem

Você vai (1) planejar a verificação dos requisitos de segurança; (2) usar testes, revisões e varreduras de forma adequada; (3) registrar as evidências de verificação.

### 27.1 Planejar a verificação

Para o serviço de click-and-collect, Lucas escreve os requisitos de segurança como enunciados testáveis: deve ser exigido um código de retirada para liberar um pedido; os códigos devem expirar depois de catorze dias; as telas do aplicativo da equipe devem mascarar os números de telefone depois da retirada; e o serviço deve registrar cada liberação com a identidade do funcionário. Para cada requisito, ele nomeia um método de verificação e quem o executa. Requisitos escritos como objetivos vagos, como "o serviço deve ser seguro", não podem ser verificados e dão um falso conforto a todos que os leem.

### 27.2 Escolher os métodos

Lucas associa métodos aos requisitos. A expiração dos códigos é verificada por um teste automatizado com o relógio adiantado. O mascaramento é verificado por um revisor usando o aplicativo da equipe numa conta de teste. O logging é verificado fazendo uma liberação e lendo o log. Uma varredura de dependências procura bibliotecas com vulnerabilidades conhecidas, como recomenda o SP 800-218. Ele observa que as varreduras encontram problemas conhecidos, mas não falhas de lógica, como liberar um pedido sem código, que só um teste projetado para isso consegue captar. Cada método cobre o que pode.

### 27.3 Registrar as evidências

Toda verificação produz um registro: data, método, resultado e quem a executou. Um teste falha: os códigos não expiram porque a tarefa de expiração não foi agendada em produção. O desenvolvedor corrige, e Lucas roda o teste de novo. O registro mostra tanto a falha quanto a correção, o que convence mais um auditor do que uma folha impecável. Lucas acrescenta os testes ao checklist de release, para que as mudanças futuras sejam verificadas de novo, em vez de se supor que preservaram o comportamento.

### Exemplo resolvido

Lucas escreve quatro requisitos testáveis, associa cada um a um método de verificação, encontra uma tarefa de expiração não agendada e registra a falha e a correção.

> **Caso sintético.** O serviço e os resultados são sintéticos; o SP 800-218 é real.

### Erros e limites

Os testes verificam apenas o que foram projetados para verificar. As evidências envelhecem a cada mudança.

### Exercícios

- **EX079 — Requisito não testável.** Por que "o serviço deve ser seguro" é um requisito ruim? *Rubrica:* 3 = não pode ser verificado;; 2 = não testável;; 1 = está bom;; 0 = nenhuma.

- **EX080 — Limite da varredura.** O que uma varredura de dependências não consegue encontrar? *Rubrica:* 3 = falhas de lógica, como liberação sem código;; 2 = falhas de lógica;; 1 = tudo;; 0 = nenhuma.

- **EX081 — Teste que falhou.** Que teste falhou, e por quê? *Rubrica:* 3 = expiração dos códigos; a tarefa não estava agendada em produção;; 2 = expiração;; 1 = mascaramento;; 0 = nenhuma.

<a id="ch-28"></a>

## Capítulo 28 — Arquitetura e engenharia de segurança: análise de falhas

### Objetivos de aprendizagem

Você vai (1) conduzir uma revisão sem culpados de um incidente da Fernway; (2) separar as causas em fatores de projeto, de processo e humanos; (3) produzir melhorias duradouras.

### 28.1 O incidente

Durante uma liquidação de fim de semana, a loja da Fernway mostrou alguns itens com preço zero por quarenta minutos, e vinte e três pedidos foram feitos. Hannah pede a Lucas que ajude a conduzir uma revisão sem culpados (blameless). Eles montam uma linha do tempo a partir dos logs e de entrevistas: um comprador enviou uma planilha de preços com uma coluna em branco, a importação tratou os campos em branco como zero, e nenhum alerta disparou porque o monitoramento observava a disponibilidade, e não os preços. Montar a linha do tempo antes de discutir as causas mantém a revisão ancorada no que de fato aconteceu, e não em suposições iniciais.

### 28.2 Camadas de causas

Lucas separa as causas contribuintes em camadas. Projeto: a importação aceitava campos em branco como zero, e o upload de planilha atravessava uma fronteira de confiança sem validação, como observado no capítulo 21. Processo: nenhuma segunda pessoa conferia grandes mudanças de preço antes das liquidações de fim de semana. Humana: o comprador estava com pressa para cumprir um prazo definido pelo marketing. Ele evita apontar o comprador como a causa, já que qualquer pessoa sob a mesma pressão e com as mesmas ferramentas poderia ter cometido o erro. O enquadramento sem culpados incentiva as pessoas a relatarem problemas cedo.

### 28.3 Melhorias duradouras

A revisão produz quatro melhorias: a importação rejeita campos em branco e qualquer mudança de preço acima de cinquenta por cento sem aprovação; um alerta no dashboard dispara quando muitos preços mudam de uma vez; é acrescentada uma conferência por uma segunda pessoa na preparação das liquidações; e os prazos para os preços das liquidações são antecipados em um dia. Cada uma tem um responsável e uma data. A Fernway honra os pedidos como gesto de boa vontade. Três meses depois, Lucas confere se as melhorias estão em vigor e descobre que o alerta já captou uma conversão de moeda equivocada antes que os clientes a vissem.

### Exemplo resolvido

Lucas ajuda a conduzir uma revisão sem culpados de um incidente de preço zero, separa as causas de projeto, de processo e humanas e confere depois quatro melhorias.

> **Caso sintético.** O incidente e os números são sintéticos.

### Erros e limites

Sem culpados não significa sem responsáveis; os responsáveis pelas correções continuam sendo nomeados. Linhas do tempo feitas de memória precisam de confirmação nos logs.

### Exercícios

- **EX082 — Por que nenhum alerta.** Por que nenhum alerta disparou? *Rubrica:* 3 = o monitoramento observava a disponibilidade, e não os preços;; 2 = lacuna de monitoramento;; 1 = nenhuma;; 0 = nenhuma.

- **EX083 — Não culpar o comprador.** Por que evitar apontar o comprador como a causa? *Rubrica:* 3 = qualquer pessoa sob a mesma pressão e com as mesmas ferramentas poderia errar;; 2 = sistema;; 1 = culpa;; 0 = nenhuma.

- **EX084 — Prova posterior.** O que mostrou que as melhorias funcionaram? *Rubrica:* 3 = o alerta captou um erro de conversão de moeda;; 2 = alerta;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-29"></a>

## Capítulo 29 — Arquitetura e engenharia de segurança: operações

### Objetivos de aprendizagem

Você vai (1) descrever as atividades operacionais que mantêm uma arquitetura eficaz; (2) projetar um ritmo de operação leve para a Fernway; (3) lidar com mudanças sem perder a segurança.

### 29.1 A arquitetura em operação

Lucas aprende que uma arquitetura se deteriora sem operação. As contas acumulam direitos, os certificados expiram, os fornecedores mudam e surgem novas ferramentas. O NIST SP 800-37 Rev. 2 chama a parte contínua de monitoramento contínuo: verificar se os controles ainda funcionam e se o risco continua aceitável. Para a Fernway, isso não pode significar uma equipe grande. Lucas lista as atividades que mais importam: revisões de acesso, aplicação de patches, testes de backup, revisão de logs, verificações de fornecedores e simulados de incidente. Cada uma tem uma frequência e um responsável, e cada uma produz uma pequena evidência.

### 29.2 Um ritmo de operação

Lucas projeta um calendário. Semanal: Hannah confere os alertas de identidade e o status dos patches. Mensal: o verificador de menor privilégio do capítulo 25 é executado e os resultados são revisados; testa-se a restauração de um backup. Trimestral: revisão da lista de fornecedores, exercício de mesa (tabletop) e um relatório ao conselho com as métricas do capítulo 15. Anual: atualização da visão geral da arquitetura e revisão de riscos. Ele estima o total em cerca de quatro horas por semana. Registrar o ritmo por escrito faz com que as tarefas sobrevivam a férias e trocas de pessoal, porque é o calendário, e não a memória, que as carrega.

### 29.3 Mudar com segurança

A Fernway muda com frequência: novas lojas, funcionários temporários e novos fornecedores. Lucas acrescenta perguntas de segurança ao formulário de mudança existente: esta mudança acrescenta um fornecedor, dados novos, um novo cruzamento de fronteira ou um novo acesso privilegiado? Um sim dispara uma breve revisão com Hannah. A maioria das mudanças responde não e passa rapidamente. Durante o estágio dele, as perguntas pegam um novo aplicativo de fidelidade que teria recebido a lista completa de associados. A integração é reprojetada para enviar apenas os números dos associados e os saldos de pontos, que é tudo de que o aplicativo precisa.

### Exemplo resolvido

Lucas lista as atividades operacionais, projeta um ritmo de quatro horas por semana e acrescenta quatro perguntas de segurança ao formulário de mudança, pegando um aplicativo de fidelidade que compartilhava dados demais.

> **Caso sintético.** O ritmo e o aplicativo são sintéticos; o SP 800-37 Rev. 2 é real.

### Erros e limites

Os ritmos escorregam sob pressão de trabalho. As perguntas de mudança dependem de respostas honestas.

### Exercícios

- **EX085 — Por que um calendário.** Por que registrar o ritmo de operação por escrito? *Rubrica:* 3 = as tarefas sobrevivem a férias e trocas de pessoal;; 2 = continuidade;; 1 = nenhuma;; 0 = nenhuma.

- **EX086 — Gatilho de mudança.** O que dispara uma revisão de segurança de uma mudança? *Rubrica:* 3 = acrescentar um fornecedor, dados novos, um cruzamento de fronteira ou acesso privilegiado;; 2 = gatilho;; 1 = todas as mudanças;; 0 = nenhuma.

- **EX087 — Correção do aplicativo de fidelidade.** Como o aplicativo de fidelidade foi reprojetado? *Rubrica:* 3 = para receber apenas números de associados e saldos de pontos;; 2 = minimizar;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-30"></a>

## Capítulo 30 — Laboratório II

### Objetivos de aprendizagem

Você vai (1) simular a revisão de logs em busca de logins suspeitos; (2) ajustar uma regra de detecção simples; (3) medir falsos positivos e falhas de detecção em dados sintéticos.

### 30.1 A tarefa

O segundo laboratório pede que Lucas escreva uma regra de detecção para logins suspeitos usando logs sintéticos do sistema de identidade da Fernway. Cada registro tem um usuário, um horário, um país e um resultado. Ele começa com uma regra que sinaliza logins vindos de um país diferente do habitual do usuário. Os dados sintéticos incluem eventos rotulados, alguns deles ataques genuínos plantados pelo Dr. Bellini, para que Lucas possa medir o quão bem sua regra funciona. Todos os dados são gerados, então nenhuma atividade real de funcionários é examinada.

### Laboratório — Ajuste de uma regra de impossible travel

```python
# Tune a sign-in rule on labelled synthetic logs: (user, hour, country, attack?)
logs = [("ana", 9, "UK", 0), ("ana", 10.5, "BR", 1), ("ben", 8, "UK", 0), ("ben", 20, "FR", 0),
        ("cai", 7, "UK", 0), ("cai", 8.5, "RU", 1), ("dee", 9, "UK", 0), ("dee", 15, "ES", 0),
        ("eli", 12, "UK", 0), ("eli", 13.5, "CN", 1), ("fay", 9, "DE", 0), ("fay", 18, "DE", 0),
        ("gus", 9, "UK", 0), ("gus", 30, "IT", 0), ("hal", 9, "UK", 0), ("hal", 9.8, "US", 1)]
home = "UK"
def evaluate(name, flags):
    tp = sum(1 for i in flags if logs[i][3]); fp = len(flags) - tp
    miss = sum(r[3] for r in logs) - tp
    print(f"{name}: flagged {len(flags)}, attacks caught {tp}, false positives {fp}, missed {miss}")
evaluate("any foreign", [i for i, r in enumerate(logs) if r[2] != home])
def travel(window):
    out = []
    for i, r in enumerate(logs):
        for j, p in enumerate(logs[:i]):
            if p[0] == r[0] and p[2] != r[2] and r[1] - p[1] <= window: out.append(i)
    return out
evaluate("2-hour travel", travel(2)); evaluate("1-hour travel", travel(1))
```

Execute com `python3 lab_detect.py`. Saída verificada:

```text
any foreign: flagged 9, attacks caught 4, false positives 5, missed 0
2-hour travel: flagged 4, attacks caught 4, false positives 0, missed 0
1-hour travel: flagged 1, attacks caught 1, false positives 0, missed 3
```

### 30.2 Ajuste

A primeira regra sinaliza todo login do exterior, inclusive de compradores em viagens a fornecedores, produzindo muitos alarmes falsos. Lucas acrescenta uma condição: sinalizar apenas quando dois logins bem-sucedidos do mesmo usuário vêm de países diferentes em até duas horas, o que é rápido demais para viajar. O laboratório mostra a mudança: os falsos positivos caem drasticamente, enquanto os ataques plantados continuam sendo detectados. Ele também testa uma janela mais estreita, de uma hora, e descobre que ela deixa passar três dos quatro ataques, então mantém duas horas. O ajuste é uma troca entre ruído e falhas de detecção, medida em dados rotulados.

### 30.3 Relato

Lucas relata o desempenho da regra em dados sintéticos e avisa que os dados reais serão diferentes. Ele recomenda um teste de duas semanas na ferramenta de identidade da Fernway em modo apenas de alerta, com Hannah registrando quais alertas eram reais. Ele observa que a regra não detecta atacantes que fazem login do mesmo país do usuário, então ela complementa, e não substitui, a autenticação resistente a phishing. O Dr. Bellini observa que declarar o que uma regra não consegue detectar é tão importante quanto sua taxa de detecção, porque, do contrário, os defensores confiam demais nela.

### Exemplo resolvido

Lucas escreve e ajusta uma regra de impossible travel em logs sintéticos rotulados, compara janelas por falsos positivos e falhas de detecção e planeja um teste.

> **Caso sintético.** Os logs e os ataques são sintéticos.

### Erros e limites

Os dados sintéticos raramente reproduzem o ruído real. VPNs e aplicativos de viagem podem confundir regras de localização.

### Exercícios

- **EX088 — Problema da primeira regra.** O que havia de errado em sinalizar todos os logins do exterior? *Rubrica:* 3 = compradores em viagem causaram muitos alarmes falsos;; 2 = falsos positivos;; 1 = nenhuma;; 0 = nenhuma.

- **EX089 — Escolha da janela.** Por que manter duas horas em vez de uma? *Rubrica:* 3 = uma hora deixou passar três dos quatro ataques;; 2 = falha de detecção;; 1 = mais rápido;; 0 = nenhuma.

- **EX090 — Ponto cego da regra.** O que a regra não detecta? *Rubrica:* 3 = atacantes fazendo login do próprio país do usuário;; 2 = mesmo país;; 1 = nada;; 0 = nenhuma.

<a id="ch-31"></a>

## Capítulo 31 — Arquitetura e engenharia de segurança: casos avançados

### Objetivos de aprendizagem

Você vai (1) analisar uma migração para zero trust na Fernway; (2) ponderar o projeto de resiliência para as altas temporadas; (3) avaliar trade-offs em projetos avançados.

### 31.1 Zero trust para uma cooperativa

Hannah se pergunta se o zero trust se aplica à Fernway. Lucas lê o NIST SP 800-207 e explica sua ideia central: nenhuma confiança implícita baseada na localização na rede; cada solicitação de acesso é avaliada usando a identidade, o estado do dispositivo e o contexto. Para a Fernway, isso significa aposentar a VPN do escritório para a maioria dos usos e colocar o sistema de estoque e os aplicativos da equipe atrás de um proxy de acesso ciente de identidade. Ele planeja uma migração em fases, começando pelo aplicativo financeiro, que tem poucos usuários e alto valor, para que as lições sejam aprendidas antes de incluir as lojas movimentadas.

### 31.2 Resiliência para a alta temporada

A Fernway obtém um terço de sua receita online nas seis semanas antes do inverno. Lucas usa ideias do NIST SP 800-160 Vol. 2 Rev. 1 sobre ciber-resiliência: antecipar, resistir, recuperar e adaptar. Ele propõe um congelamento pré-temporada das mudanças não essenciais, um failover testado da loja para uma segunda região de hospedagem, um processo manual de pedidos ensaiado caso o pagamento falhe e monitoramento extra durante o pico. Cada medida é dimensionada ao risco: o failover custa dinheiro o ano inteiro, então ele o compara com a receita perdida numa indisponibilidade num dia de pico antes de recomendá-lo.

### 31.3 Ponderar os trade-offs

Projetos avançados trazem custos. O proxy de acesso acrescenta uma dependência do provedor de identidade, que já é um ponto único de falha desde o capítulo 22. O congelamento de mudanças atrasa funcionalidades que o marketing quer. Lucas apresenta cada trade-off abertamente: o que se ganha, o que se perde e quem arca com o custo. O conselho aprova o proxy para o financeiro e o congelamento, mas adia a segunda região de hospedagem para o orçamento do próximo ano, aceitando o risco por uma temporada com o processo manual de pedidos como contingência. Lucas registra a decisão e sua data de revisão.

### Exemplo resolvido

Lucas planeja uma migração para zero trust em fases, começando pelo financeiro, aplica os objetivos de resiliência à alta temporada e apresenta os trade-offs que levam a uma decisão registrada do conselho.

> **Caso sintético.** Os planos e os custos são sintéticos; o SP 800-207 e o SP 800-160 Vol. 2 Rev. 1 são reais.

### Erros e limites

Zero trust é uma direção, e não um produto. A resiliência adiada deixa a temporada exposta.

### Exercícios

- **EX091 — Por que o financeiro primeiro.** Por que começar o zero trust pelo aplicativo financeiro? *Rubrica:* 3 = poucos usuários e alto valor, então as lições são aprendidas com segurança;; 2 = piloto;; 1 = lojas primeiro;; 0 = nenhuma.

- **EX092 — Quatro objetivos de resiliência.** Que quatro objetivos de resiliência Lucas usou? *Rubrica:* 3 = antecipar, resistir, recuperar e adaptar;; 2 = três;; 1 = nenhuma;; 0 = nenhuma.

- **EX093 — Item adiado.** O que o conselho adiou, e com qual contingência? *Rubrica:* 3 = a segunda região de hospedagem; processo manual de pedidos;; 2 = adiado;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-32"></a>

## Capítulo 32 — Arquitetura e engenharia de segurança: interfaces interdisciplinares

### Objetivos de aprendizagem

Você vai (1) trabalhar com colegas do jurídico, do financeiro e de operações em decisões de segurança; (2) traduzir a segurança para a linguagem de cada disciplina; (3) resolver prioridades conflitantes.

### 32.1 Linguagens diferentes

Lucas percebe que cada departamento da Fernway ouve a segurança de um jeito diferente. O gerente financeiro pensa em custos e perdas; o gerente de operações pensa em vazão e tempo da equipe; a assessora jurídica da cooperativa pensa em obrigações e responsabilidade. Quando Lucas apresentou o proxy de acesso em termos técnicos, ninguém se engajou. Quando o descreveu ao financeiro como redução da chance de fraude em pagamentos, a operações como a eliminação da etapa de VPN que atrasa a equipe das lojas e ao jurídico como apoio aos deveres de proteção de dados, cada pessoa viu um motivo para apoiá-lo.

### 32.2 Trabalhar com o jurídico e a privacidade

A assessora jurídica pergunta se a regra de detecção de logins do capítulo 30 é lícita perante as normas de proteção de dados, já que trata dados de localização dos funcionários. Lucas e a assessora documentam a finalidade, os dados minimizados ao nível de país, o prazo de retenção e o aviso aos funcionários, e registram uma avaliação de interesse legítimo. A ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) espera que tais obrigações sejam identificadas e cumpridas. O trabalho atrasa o teste em duas semanas, mas o torna defensável. Lucas aprende que envolver o jurídico cedo sai mais barato do que reprojetar depois de uma objeção.

### 32.3 Resolver conflitos

Operações quer que os funcionários temporários comecem a trabalhar em até uma hora após a chegada; a segurança quer as contas aprovadas e o treinamento feito antes. Lucas negocia um meio-termo: as contas temporárias são pré-criadas com direitos limitados de caixa, ativadas na chegada por um gerente de loja e expiram no fim da temporada. O treinamento é um vídeo de cinco minutos no caixa. Os dois lados obtêm a maior parte do que precisam. Ele registra o meio-termo como uma decisão de projeto, para que não seja reaberto a cada temporada. O trabalho interdisciplinar consiste sobretudo em encontrar projetos que sirvam a vários objetivos ao mesmo tempo.

### Exemplo resolvido

Lucas traduz o proxy de acesso para os termos do financeiro, de operações e do jurídico, documenta uma base legal para a detecção e negocia um meio-termo para as contas temporárias.

> **Caso sintético.** Os departamentos e as decisões são sintéticos; a ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) é real.

### Erros e limites

A tradução pode exagerar os benefícios. Os meios-termos precisam de revisão se as condições mudarem.

### Exercícios

- **EX094 — Enquadramento para o financeiro.** Como Lucas enquadrou o proxy para o financeiro? *Rubrica:* 3 = redução da chance de fraude em pagamentos;; 2 = fraude;; 1 = termos técnicos;; 0 = nenhuma.

- **EX095 — Detecção e lei.** O que Lucas e a assessora documentaram para a regra de detecção? *Rubrica:* 3 = finalidade, minimização ao nível de país, retenção, aviso e uma avaliação de interesse legítimo;; 2 = três itens;; 1 = nenhuma;; 0 = nenhuma.

- **EX096 — Meio-termo temporário.** Qual foi o meio-termo para as contas temporárias? *Rubrica:* 3 = contas limitadas pré-criadas, ativadas na chegada e que expiram no fim da temporada;; 2 = limitadas;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-33"></a>

## Capítulo 33 — Métodos de pesquisa II

### Objetivos de aprendizagem

Você vai (1) analisar os dados do quase-experimento do capítulo 18; (2) tratar as ameaças à validade; (3) relatar os achados com a cautela adequada.

### 33.1 Analisar os dados

Lucas coleta seis meses de contagens agregadas do botão de denúncia. As lojas que receberam as orientações mostram uma taxa mensal de denúncias por funcionário antes e depois das orientações; as lojas de comparação mostram o mesmo nos mesmos meses. Ele calcula a variação em cada grupo e a diferença entre essas variações, um difference-in-differences simples. O laboratório abaixo executa o cálculo sobre as contagens sintéticas. As lojas orientadas subiram mais do que as de comparação, o que sugere que as orientações ajudaram, embora a estimativa dependa da suposição de que os dois grupos, de outro modo, teriam seguido tendências semelhantes.

### Laboratório — Difference-in-differences nas taxas de denúncia

```python
# Difference-in-differences on report rates (reports per staff per month), synthetic.
briefed = {"before": [0.20, 0.25, 0.22], "after": [0.55, 0.58, 0.51]}
compare = {"before": [0.21, 0.19, 0.24], "after": [0.27, 0.25, 0.22]}
m = lambda xs: sum(xs) / len(xs)
db = m(briefed["after"]) - m(briefed["before"]); dc = m(compare["after"]) - m(compare["before"])
print(f"briefed change {db:+.2f}, comparison change {dc:+.2f}, difference-in-differences {db - dc:+.2f}")
```

Execute com `python3 lab_did.py`. Saída verificada:

```text
briefed change +0.32, comparison change +0.03, difference-in-differences +0.29
```

### 33.2 Ameaças à validade

Lucas usa as categorias de Wohlin e colegas (2012). Validade interna: as lojas orientadas foram escolhidas pelos gerentes regionais, talvez porque já fossem engajadas. Validade de construto: o uso do botão de denúncia mede a disposição de denunciar, e não a capacidade de detectar. Validade externa: as lojas da Fernway podem diferir das de outros varejistas. Validade de conclusão: com poucas lojas, o resultado pode surgir por acaso. Ele trata algumas ameaças verificando que as tendências anteriores às orientações eram semelhantes e declara as demais abertamente, em vez de escondê-las num apêndice. Cada ameaça é listada com a provável direção do viés.

### 33.3 Relatar com cautela

Lucas escreve que as lojas orientadas mostraram uma alta maior nas denúncias do que as lojas de comparação, o que é consistente com um benefício das orientações, mas que o desenho não consegue descartar outras explicações. Ele recomenda uma implantação aleatorizada na próxima rodada, com as lojas designadas por sorteio, que a Fernway concorda em experimentar. Hannah usa o resultado cauteloso para manter as orientações enquanto o estudo mais forte acontece. O Dr. Bellini dá nota alta ao relatório por ajustar a força das afirmações à força das evidências.

### Exemplo resolvido

Lucas executa um difference-in-differences sobre taxas sintéticas de denúncia, lista quatro ameaças à validade e relata um achado cauteloso com um acompanhamento aleatorizado.

> **Caso sintético.** As contagens são sintéticas; Wohlin et al. (2012) é real.

### Erros e limites

Poucas unidades tornam as estimativas instáveis. As tendências paralelas não podem ser provadas, apenas verificadas.

### Exercícios

- **EX097 — Resultado do DiD.** Qual foi o difference-in-differences no laboratório? *Rubrica:* 3 = 0,29 denúncia por funcionário por mês;; 2 = positivo;; 1 = nenhuma;; 0 = nenhuma.

- **EX098 — Ameaça de construto.** Que ameaça à validade de construto Lucas apontou? *Rubrica:* 3 = o uso do botão mede a disposição, e não a capacidade de detecção;; 2 = construto;; 1 = nenhuma;; 0 = nenhuma.

- **EX099 — Desenho mais forte.** O que Lucas recomendou em seguida? *Rubrica:* 3 = implantação aleatorizada por sorteio;; 2 = aleatorizar;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-34"></a>

## Capítulo 34 — Projeto comparativo

### Objetivos de aprendizagem

Você vai (1) comparar duas opções de arquitetura para o acesso da equipe da Fernway; (2) usar critérios ponderados; (3) testar a sensibilidade da escolha.

### 34.1 As opções

A Fernway precisa escolher como a equipe das lojas faz login no aplicativo de estoque em tablets compartilhados. A opção A são senhas individuais com tempo curto de expiração da sessão. A opção B é aproximar o crachá mais um PIN curto, com os crachás vinculados ao provedor de identidade. Lucas as compara como seu projeto comparativo. Ele define os critérios com Hannah e os gerentes de loja: segurança contra o uso indevido de credenciais compartilhadas, rapidez no caixa, custo, facilidade de remover quem sai e acessibilidade para funcionários com deficiência. Definir os critérios antes da pontuação impede que a opção favorita molde os critérios.

### Laboratório — Comparação ponderada com verificação de sensibilidade

```python
# Weighted comparison of two sign-in options with a sensitivity check (synthetic).
crit = ["security", "speed", "cost", "leavers", "access"]
w = {"security": 0.30, "speed": 0.25, "cost": 0.15, "leavers": 0.15, "access": 0.15}
score = {"A": {"security": 3, "speed": 2, "cost": 5, "leavers": 3, "access": 3},
         "B": {"security": 4, "speed": 5, "cost": 2, "leavers": 5, "access": 4}}
def totals(wt):
    s = sum(wt.values()); return {o: sum(wt[c] * score[o][c] for c in crit) / s for o in score}
print("base:", {o: f"{v:.2f}" for o, v in totals(w).items()})
w2 = dict(w, cost=0.30); print("cost weight doubled:", {o: f"{v:.2f}" for o, v in totals(w2).items()})
```

Execute com `python3 lab_weighted.py`. Saída verificada:

```text
base: {'A': '3.05', 'B': '4.10'}
cost weight doubled: {'A': '3.30', 'B': '3.83'}
```

### 34.2 Pontuação ponderada

Cada critério recebe um peso acordado pelo grupo, e cada opção recebe uma nota de um a cinco em cada critério. O laboratório calcula os totais ponderados: a opção B pontua mais, principalmente em rapidez e na remoção de quem sai, enquanto a opção A é mais barata. Lucas registra quem deu cada nota e por quê, para que as notas possam ser contestadas. Ele observa que a pontuação esconde incerteza, então uma diferença pequena não justificaria uma recomendação forte sem mais evidências, como um piloto numa loja.

### 34.3 Sensibilidade

Lucas verifica se a escolha muda quando os pesos se deslocam. O laboratório dobra o peso do custo e descobre que a opção B continua vencendo, embora por menos. A opção A só vence se o custo pesar mais do que a segurança e a rapidez juntas. Como ninguém na Fernway acredita que o custo importe tanto aqui, a recomendação é robusta. Ele apresenta o resultado com a verificação de sensibilidade, que convence o gerente financeiro mais do que os totais sozinhos. Um piloto numa loja confirma que o login por crachá leva cerca de quatro segundos.

### Exemplo resolvido

Lucas compara duas opções de login em tablets compartilhados com cinco critérios ponderados, verifica a sensibilidade ao peso do custo e confirma com um piloto.

> **Caso sintético.** As opções, os pesos e as notas são sintéticos.

### Erros e limites

Os pesos refletem opiniões. As notas de um grupo pequeno podem compartilhar vieses.

### Exercícios

- **EX100 — Critérios primeiro.** Por que definir os critérios antes da pontuação? *Rubrica:* 3 = para que a opção favorita não possa moldá-los;; 2 = viés;; 1 = nenhuma;; 0 = nenhuma.

- **EX101 — Totais.** Quais foram os totais ponderados no laboratório? *Rubrica:* 3 = A 3,05, B 4,10;; 2 = B maior;; 1 = A maior;; 0 = nenhuma.

- **EX102 — Resultado da sensibilidade.** O que aconteceu quando o peso do custo dobrou? *Rubrica:* 3 = B continuou vencendo, 3,83 a 3,30;; 2 = B vence;; 1 = A vence;; 0 = nenhuma.

<a id="ch-35"></a>

## Capítulo 35 — Proposta de trabalho de conclusão

### Objetivos de aprendizagem

Você vai (1) escrever uma proposta de projeto final (capstone) para um projeto de arquitetura de segurança; (2) definir escopo, entregáveis e avaliação; (3) obter a concordância dos patrocinadores.

### 35.1 Escolher o projeto final

Lucas propõe seu projeto final: uma arquitetura de segurança para o segundo armazém planejado pela Fernway, que usará robôs de separação automatizados e um novo sistema de gestão de armazém. O projeto é real o bastante para importar para a Fernway, delimitado o bastante para um único estudante ao longo de dois semestres e rico em questões de arquitetura: novos fornecedores, tecnologia operacional na rede, novos papéis na equipe e integração com o sistema de estoque existente. O Dr. Bellini aprova o tema com a condição de que o escopo exclua os sistemas internos de segurança física dos robôs, que exigem engenheiros especializados.

### 35.2 Escopo e entregáveis

A proposta define os entregáveis: uma visão geral da arquitetura do armazém, um modelo de fluxo de dados com fronteiras de confiança, uma análise STRIDE e de árvore de ataque, um conjunto de controles ligado aos riscos, testes de verificação para cinco requisitos-chave e uma avaliação. Ela lista o que está fora do escopo, inclusive a segurança física dos robôs e as práticas internas de desenvolvimento do fornecedor. Ela define marcos a cada mês. Registrar as exclusões por escrito protege o estudante do aumento descontrolado do escopo (scope creep) e diz claramente ao patrocinador o que não será entregue, para que as expectativas continuem realistas.

### 35.3 Avaliação e concordância

Lucas define como o projeto final será julgado: se a Fernway adota o projeto, se os testes de verificação passam e se um revisor independente, uma arquiteta de segurança de uma cooperativa parceira, encontra lacunas graves. Ele escreve esses critérios na proposta para que o sucesso não seja definido depois do fato. Hannah assina como patrocinadora, o Dr. Bellini como orientador, e o gerente do projeto do armazém concorda em compartilhar documentos. A proposta ocupa quatro páginas e se torna o contrato para os dois semestres seguintes. Os três signatários guardam cópias.

### Exemplo resolvido

Lucas propõe um projeto final de arquitetura de segurança para o armazém, define entregáveis e exclusões, fixa os critérios de avaliação de antemão e obtém três assinaturas.

> **Caso sintético.** O armazém e as pessoas são sintéticos.

### Erros e limites

Projetos reais atrasam, afetando os cronogramas dos estudantes. Os patrocinadores podem mudar de prioridades.

### Exercícios

- **EX103 — Área excluída.** O que o Dr. Bellini exigiu que fosse excluído? *Rubrica:* 3 = os sistemas internos de segurança física dos robôs;; 2 = segurança dos robôs;; 1 = nenhuma;; 0 = nenhuma.

- **EX104 — Por que listar exclusões.** Por que escrever as exclusões na proposta? *Rubrica:* 3 = para evitar o scope creep e alinhar as expectativas do patrocinador;; 2 = escopo;; 1 = nenhuma;; 0 = nenhuma.

- **EX105 — Critérios de antemão.** Por que definir os critérios de avaliação na proposta? *Rubrica:* 3 = para que o sucesso não seja definido depois do fato;; 2 = de antemão;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-36"></a>

## Capítulo 36 — Prática de campo ou comunitária

### Objetivos de aprendizagem

Você vai (1) aplicar habilidades de arquitetura de segurança num ambiente comunitário; (2) adaptar as recomendações para organizações sem equipe de TI; (3) refletir sobre o que se transfere.

### 36.1 Um estágio comunitário

Como parte da prática de campo, Lucas trabalha como voluntário por quatro semanas num banco de alimentos local que usa notebooks doados, um serviço de e-mail gratuito e uma planilha das famílias atendidas. Não há equipe de TI, e os voluntários mudam toda semana. Ele aplica o mesmo raciocínio usado na Fernway, mas as restrições são mais duras: nenhum orçamento, pouco tempo e usuários com graus variados de confiança digital. Ele começa ouvindo como os voluntários trabalham, já que qualquer recomendação que acrescente etapas a um turno de distribuição movimentado será ignorada.

### 36.2 Adaptar as recomendações

Lucas identifica três prioridades: a planilha das famílias é compartilhada por link com qualquer pessoa, a conta compartilhada dos voluntários não tem segundo fator e os notebooks não são criptografados. Ele restringe o compartilhamento a contas nominais, ativa o segundo fator gratuito do provedor de e-mail para a coordenadora e passa os voluntários para contas gratuitas individuais, e habilita a criptografia de disco nativa. Ele escreve um guia de uma página com imagens. Ele abandona a implantação planejada de um gerenciador de senhas porque os voluntários não a sustentariam. As recomendações para pequenos grupos comunitários precisam ser mínimas, gratuitas e fáceis de manter.

### 36.3 Reflexão

Em seu diário reflexivo, Lucas registra o que se transferiu da Fernway: a classificação de dados, o menor privilégio e a pergunta sobre quem perceberia um problema. O que não se transferiu: formulários de mudança, dashboards de métricas e questionários de fornecedores, que pressupõem tempo da equipe. Ele percebe que arquitetura é ajustar a proteção à organização, e que um projeto simples que os voluntários seguem é melhor do que um projeto completo que eles abandonam. A coordenadora do banco de alimentos relata depois que o guia está afixado junto ao balcão de distribuição e que os novos voluntários o leem no primeiro dia.

### Exemplo resolvido

Lucas adapta recomendações de arquitetura para um banco de alimentos, corrige três prioridades com ferramentas gratuitas e reflete sobre o que se transfere de um varejista.

> **Caso sintético.** O banco de alimentos é sintético.

### Erros e limites

A rotatividade dos voluntários corrói as mudanças. Os serviços gratuitos podem mudar seus termos.

### Exercícios

- **EX106 — Primeiro passo.** Por que Lucas começou ouvindo os voluntários? *Rubrica:* 3 = recomendações que acrescentam etapas a turnos movimentados são ignoradas;; 2 = adequação;; 1 = nenhuma;; 0 = nenhuma.

- **EX107 — Plano abandonado.** O que Lucas abandonou, e por quê? *Rubrica:* 3 = a implantação de um gerenciador de senhas que os voluntários não sustentariam;; 2 = sustentar;; 1 = custo;; 0 = nenhuma.

- **EX108 — O que se transferiu.** Cite duas coisas que se transferiram da Fernway. *Rubrica:* 3 = classificação, menor privilégio, perguntar quem perceberia;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-37"></a>

## Capítulo 37 — Seminário de revisão de evidências

### Objetivos de aprendizagem

Você vai (1) avaliar criticamente as fontes publicadas; (2) distinguir normas, pesquisa e opinião; (3) apresentar aos colegas uma síntese justa das evidências.

### 37.1 Avaliar as fontes

No seminário, cada estudante revisa as evidências sobre uma pergunta. Lucas fica com a pergunta: a segmentação de rede reduz a propagação de ransomware em pequenas organizações? Ele reúne normas, relatórios de fornecedores, artigos acadêmicos e posts de blog. Para cada um, pergunta quem o escreveu, que método foi usado, que dados o sustentam e que interesses o autor tem. Herley e van Oorschot (2017) alertam que boa parte do conhecimento em segurança se apoia em afirmações, e não em alegações testadas, então Lucas procura evidências que resistiriam a um exame rigoroso.

### 37.2 Tipos de fonte

Lucas classifica suas fontes. Normas como o SP 800-53 Rev. 5 e a ISO/IEC 27002:2022 registram o consenso de especialistas sobre boas práticas, mas não medem resultados. Os relatórios de fornecedores oferecem grandes conjuntos de dados, mas têm interesses comerciais e métodos pouco claros. Os estudos acadêmicos têm métodos mais claros, mas muitas vezes estudam redes simuladas. Os posts de blog dão exemplos vívidos, mas não podem ser generalizados. Ele pondera cada tipo pelo que ele consegue mostrar. O resultado é um quadro em que a segmentação é amplamente recomendada e plausível, mas as evidências de resultado para pequenas organizações são escassas.

### 37.3 Apresentar com justiça

Lucas apresenta sua síntese ao seminário com uma tabela que mostra cada fonte, seu tipo, seu achado e seus limites. Ele enuncia a conclusão com cuidado: a segmentação é uma prática razoável apoiada no consenso de especialistas e em estudos de simulação, mas as medições no mundo real para pequenas organizações são escassas. Um colega o contesta com uma estatística de fornecedor; ele explica por que o método dela não é claro. O Dr. Bellini elogia a imparcialidade, observando que uma síntese honesta de evidências fracas é mais útil para os profissionais do que uma síntese confiante construída sobre marketing.

### Exemplo resolvido

Lucas avalia fontes sobre segmentação e ransomware, classifica-as por tipo e apresenta uma síntese justa, apontando que as evidências de resultado são escassas.

> **Caso sintético.** A coleção de fontes é sintética nos detalhes; Herley e van Oorschot (2017), o SP 800-53 Rev. 5 e a ISO/IEC 27002:2022 são reais.

### Erros e limites

Ausência de evidência não é evidência de ausência. Os revisores podem carregar seus próprios vieses.

### Exercícios

- **EX109 — Quatro perguntas.** Que quatro perguntas Lucas fez a cada fonte? *Rubrica:* 3 = autor, método, dados e interesses;; 2 = três;; 1 = nenhuma;; 0 = nenhuma.

- **EX110 — Limite das normas.** O que as normas não fazem? *Rubrica:* 3 = medir resultados;; 2 = resultados;; 1 = tudo;; 0 = nenhuma.

- **EX111 — Conclusão.** Qual foi a conclusão de Lucas sobre a segmentação? *Rubrica:* 3 = prática razoável apoiada em consenso e simulações, mas com poucas evidências reais para pequenas organizações;; 2 = equilibrada;; 1 = comprovada;; 0 = nenhuma.

<a id="ch-38"></a>

## Capítulo 38 — Implementação do trabalho de conclusão

### Objetivos de aprendizagem

Você vai (1) executar o trabalho de arquitetura do projeto final; (2) gerenciar mudanças num projeto em andamento; (3) manter a rastreabilidade dos riscos aos controles.

### 38.1 Fazer o trabalho

Lucas avança pelos entregáveis do projeto final para o novo armazém. Ele modela o sistema de gestão de armazém, os controladores dos robôs, a integração com o sistema de estoque e o link de suporte remoto do fornecedor. Ele marca uma fronteira entre a rede dos robôs e a rede do escritório, com apenas o sistema de gestão de armazém autorizado a falar com as duas. Ele executa o STRIDE e uma árvore de ataque para o objetivo "parar a separação durante a alta temporada", o que revela que o link de suporte remoto do fornecedor é o caminho mais fácil, porque usa uma senha compartilhada.

### 38.2 Gerenciar a mudança

No meio do caminho, a Fernway troca de fornecedor de gestão de armazém depois de uma disputa de preços. Os modelos de Lucas ficam parcialmente obsoletos. Ele revisa quais entregáveis são afetados, informa Hannah e o Dr. Bellini e acerta um marco revisado. O sistema do novo fornecedor usa um serviço em nuvem em vez de um servidor local, então a fronteira se desloca. Ele reaproveita seu método e a maior parte da sua lista de riscos, atualizando apenas o que mudou. A experiência lhe ensina que os documentos de arquitetura precisam ser projetados para mudar, com premissas claras, para que os leitores saibam o que revisitar.

### 38.3 Rastreabilidade

Lucas mantém uma tabela que liga cada risco a seus controles, requisitos e testes de verificação, como no capítulo 24. Quando o fornecedor muda, a tabela mostra quais controles dependem do sistema antigo e precisam ser substituídos. O link de suporte remoto do fornecedor passa a ter como requisito contas nominais com autenticação multifator e gravação de sessão, verificado por um login de teste. Ao final, todo risco alto se liga a pelo menos um controle verificado. A rastreabilidade torna o projeto final auditável e permite que a Fernway mantenha o projeto depois que Lucas sair.

### Exemplo resolvido

Lucas modela o armazém, encontra um link de suporte com senha compartilhada, adapta-se a uma troca de fornecedor e mantém a rastreabilidade do risco ao teste.

> **Caso sintético.** O armazém e os fornecedores são sintéticos.

### Erros e limites

As trocas de fornecedor podem invalidar testes anteriores. As tabelas de rastreabilidade precisam de um responsável para se manterem atualizadas.

### Exercícios

- **EX112 — Caminho mais fácil.** Qual era o caminho mais fácil para parar a separação? *Rubrica:* 3 = o link de suporte remoto do fornecedor com senha compartilhada;; 2 = link de suporte;; 1 = nenhuma;; 0 = nenhuma.

- **EX113 — Troca de fornecedor.** Como Lucas lidou com a troca de fornecedor? *Rubrica:* 3 = revisou os entregáveis afetados, acertou novos marcos, reaproveitou o método e atualizou o que mudou;; 2 = adaptou-se;; 1 = recomeçou;; 0 = nenhuma.

- **EX114 — Controle do link de suporte.** Que requisito substituiu a senha compartilhada de suporte? *Rubrica:* 3 = contas nominais com autenticação multifator e gravação de sessão;; 2 = nominais;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-39"></a>

## Capítulo 39 — Avaliação do trabalho de conclusão

### Objetivos de aprendizagem

Você vai (1) avaliar o projeto final segundo os critérios acordados; (2) usar um revisor independente; (3) separar o que foi alcançado das lacunas remanescentes.

### 39.1 Segundo os critérios

Lucas volta aos critérios da sua proposta. Adoção: a Fernway adotou a visão geral da arquitetura e os controles para o novo armazém. Verificação: quatro dos cinco testes-chave passaram; o quinto, o isolamento da rede dos robôs, não pôde ser executado porque os robôs ainda não haviam chegado. Revisão independente: uma arquiteta de segurança de uma cooperativa parceira revisou o projeto. Ele relata cada critério com evidências e não força o teste incompleto a virar uma aprovação. Critérios acordados de antemão tornam a avaliação simples e honesta. O teste incompleto é marcado como pendente, e não como aprovado.

### 39.2 Revisão independente

A revisora não encontra lacunas graves, mas duas moderadas: nenhum plano para aplicar patches nos controladores dos robôs, que muitas vezes não podem ser atualizados durante a operação, e nenhum processo para revogar o acesso do fornecedor caso o contrato termine. Lucas aceita as duas, acrescenta um plano de janelas de manutenção acordado com o fornecedor e um checklist de saída do contrato. Ele observa que a revisora viu lacunas que ele havia deixado passar porque já tinha trabalhado com tecnologia operacional. A revisão independente é valiosa justamente porque o revisor traz uma experiência diferente.

### 39.3 O alcançado e as lacunas

A avaliação de Lucas lista o que foi alcançado, os dois achados da revisão já corrigidos e as lacunas remanescentes: o teste de isolamento aguarda os robôs, e o provedor de identidade continua sendo um ponto único de falha nos dois armazéns. Ele dá a cada lacuna remanescente um responsável na Fernway. O Dr. Bellini observa que uma boa avaliação deixa o patrocinador sabendo exatamente o que está feito e o que não está. Hannah agenda o teste de isolamento para a semana de instalação dos robôs e acrescenta a questão da resiliência da identidade ao orçamento do próximo ano. A nota de passagem lista cada item em aberto com uma data.

### Exemplo resolvido

Lucas avalia seu projeto final segundo três critérios acordados de antemão, incorpora dois achados da revisora e entrega as lacunas remanescentes a responsáveis nomeados.

> **Caso sintético.** A avaliação e as pessoas são sintéticas.

### Erros e limites

A disponibilidade do revisor limita a profundidade. Testes adiados para a instalação podem ser esquecidos sem responsáveis.

### Exercícios

- **EX115 — Teste não executado.** Que teste não pôde ser executado, e por quê? *Rubrica:* 3 = isolamento da rede dos robôs; os robôs não haviam chegado;; 2 = isolamento;; 1 = nenhuma;; 0 = nenhuma.

- **EX116 — Achados da revisora.** Que duas lacunas a revisora encontrou? *Rubrica:* 3 = nenhum plano de patches para os controladores dos robôs e nenhum processo de revogação do acesso do fornecedor;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.

- **EX117 — Responsáveis pelas lacunas.** O que aconteceu com as lacunas remanescentes? *Rubrica:* 3 = cada uma recebeu um responsável na Fernway;; 2 = responsáveis;; 1 = ignoradas;; 0 = nenhuma.

<a id="ch-40"></a>

## Capítulo 40 — Tese e apresentação

### Objetivos de aprendizagem

Você vai (1) estruturar um trabalho de conclusão de bacharelado em arquitetura de segurança; (2) apresentar os achados a públicos acadêmicos e profissionais; (3) planejar os próximos passos nos estudos ou no trabalho.

### 40.1 Estruturar o trabalho de conclusão

Lucas escreve seu trabalho de conclusão na estrutura padrão: introdução com o problema e as perguntas, fundamentação sobre princípios e normas, método, a arquitetura da Fernway e o projeto final, resultados incluindo a verificação e a revisão, discussão dos limites e conclusão. Ele cita apenas fontes que leu, entre elas Saltzer e Schroeder (1975), Shostack (2014), o SP 800-207 e Anderson (2020). Ele mantém os rótulos de sintético em todo conjunto de dados e detalhe de caso. O trabalho tem quarenta páginas, com os modelos e os registros de teste em apêndices. Cada capítulo abre com um breve resumo, e um glossário explica termos como fronteira de confiança para leitores não especialistas.

### 40.2 Dois públicos

Lucas apresenta duas vezes. À banca, explica os métodos, a validade e como seu trabalho se relaciona com as orientações publicadas. Ao conselho da Fernway, explica o que mudou, quanto custou, que riscos permanecem e que decisões eles precisam tomar em seguida. Ele usa as mesmas evidências, mas com ênfase e linguagem diferentes, como praticado no capítulo 32. O conselho pergunta sobre o risco do provedor de identidade, e a banca pergunta sobre a validade do quase-experimento. Ele responde às duas diretamente, admitindo a incerteza onde ela existe. Cada apresentação dura vinte minutos, mais as perguntas.

### 40.3 Próximos passos

Lucas reflete sobre seu curso. Ele aprendeu a modelar sistemas, avaliar riscos, escolher e verificar controles, medir resultados, revisar evidências e trabalhar entre disciplinas. A Fernway lhe oferece uma vaga de segurança júnior, e o Dr. Bellini sugere, mais adiante, um certificado de pós-graduação em arquitetura de segurança. Ele escolhe o emprego, com planos de estudar em tempo parcial. Seu conselho final aos futuros estudantes é tratar todo projeto como uma hipótese a ser testada e registrar o que não se sabe com o mesmo cuidado que o que se sabe.

### Exemplo resolvido

Lucas estrutura um trabalho de conclusão de quarenta páginas, apresenta à banca e ao conselho com ênfases diferentes e planeja entrar na Fernway enquanto estuda em tempo parcial.

> **Caso sintético.** Os detalhes do trabalho e as pessoas são sintéticos; as obras citadas são reais.

### Erros e limites

As apresentações simplificam; o trabalho escrito guarda os detalhes. Os planos de carreira mudam.

### Exercícios

- **EX118 — Fontes do trabalho.** Que regra Lucas seguiu nas citações? *Rubrica:* 3 = citar apenas as fontes que de fato leu;; 2 = lidas;; 1 = quaisquer;; 0 = nenhuma.

- **EX119 — Perguntas do conselho.** Sobre o que o conselho perguntou? *Rubrica:* 3 = o risco do provedor de identidade;; 2 = identidade;; 1 = validade;; 0 = nenhuma.

- **EX120 — Conselho final.** Qual foi o conselho de Lucas aos futuros estudantes? *Rubrica:* 3 = tratar todo projeto como hipótese e registrar as incógnitas com cuidado;; 2 = hipótese;; 1 = nenhuma;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX120. Lucas Haddon, o Dr. Marco Bellini, Hannah Osei, a Ashgrove University, a Fernway Outdoor Co-operative e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** M OR (S AND R), e (M OR S) AND R.

**EX002.** Em 2 das 8 linhas, ambas em que um gerente emite um reembolso sem recibo.

**EX003.** O caso dos terceirizados que fazem manutenção nos scanners do armazém, que nenhuma das regras cobria.

**EX004.** Porque roda sobre camadas inferiores, como um servidor sem patches, cujas fraquezas ela herda.

**EX005.** Revisar o acesso antigo do parceiro de entregas aos endereços dos clientes.

**EX006.** Um notebook antigo de impressão de etiquetas com dados de clientes e uma cópia de teste do banco de dados da loja no armazenamento em nuvem.

**EX007.** Porque há infinitas maneiras de codificar uma entrada nociva, então uma lista de padrões ruins nunca fica completa.

**EX008.** Letras, dígitos, espaços e um pequeno conjunto de sinais de pontuação, com comprimento máximo de sessenta caracteres.

**EX009.** Ela precisa ser revogada e substituída, porque cópias do histórico podem já existir.

**EX010.** Cada parágrafo defende um ponto e leva logicamente ao seguinte.

**EX011.** Porque resumos secundários podem distorcer o original, e ele deve citar apenas o que leu.

**EX012.** Que o SP 800-207 descreve princípios para reduzir a confiança implícita, e que os efeitos sobre os incidentes de pequenos varejistas não são estabelecidos pelas fontes.

**EX013.** Preços e pedidos não podem ser alterados por ninguém sem autorização.

**EX014.** Usar senhas vazadas de outros sites para entrar; rate limiting e autenticação multifator ajudam.

**EX015.** Ligando para o fornecedor num número conhecido e exigindo duas aprovações.

**EX016.** Logins, conexões de rede ou permissões entre os nós.

**EX017.** Passou de 3 para 4 saltos, agora atravessando o sistema de gestão do armazém.

**EX018.** A estação de administração e o servidor de arquivos, porque muitos caminhos mais curtos até os dados sensíveis passam por eles.

**EX019.** Um scanner comprometido fica no mesmo segmento que os notebooks do financeiro e consegue alcançá-los diretamente.

**EX020.** Porque um atacante que a controle pode redirecionar os clientes e pode passar na validação de certificados para o nome da Fernway.

**EX021.** Um serviço gerenciado de acesso remoto que exija autenticação multifator.

**EX022.** A autenticação estabelece quem é o usuário; a autorização decide o que esse usuário pode fazer.

**EX023.** Um gerente podia ajustar o estoque de outra loja, porque só o papel, e não a loja, era verificado.

**EX024.** Senhas e tokens de sessão.

**EX025.** O atacante herda apenas os direitos de leitura e de gravação de pedidos da loja, e não os poderes sobre o esquema ou de exportação.

**EX026.** Três: a consulta de busca e outras duas montadas do mesmo jeito.

**EX027.** Dados sintéticos ou adequadamente mascarados, nunca registros brutos de associados.

**EX028.** O que pode ser testado, como, quando, por quem, e um contato de emergência.

**EX029.** Registros sintéticos que ele cria, nunca dados reais de associados.

**EX030.** Relatá-lo à equipe de segurança da própria organização, em vez de Lucas investigar.

**EX031.** Porque qualquer malware que um usuário rode ganha controle total do notebook.

**EX032.** Contas individuais que elevam privilégios por meio de comandos registrados.

**EX033.** As atualizações de dispositivos como caixas e scanners, que as pessoas não consideram computadores.

**EX034.** Porque verificar apenas as contas suspeitas enviesaria a estimativa para cima.

**EX035.** Cerca de 9,0% a 18,4%, o que implica aproximadamente 361 a 735 contas afetadas.

**EX036.** Porque, com contagens tão pequenas, a mudança poderia facilmente ser obra do acaso.

**EX037.** O acesso que se acumula conforme as pessoas mudam de função; o processo de movimentação remove os papéis antigos quando novos são concedidos.

**EX038.** Um comprador que também podia aprovar pagamentos a fornecedores, o que permitiria uma fraude com fornecedor falso.

**EX039.** Porque páginas falsas podem capturar e repassar os códigos por SMS, enquanto as passkeys só funcionam no site genuíno.

**EX040.** Distritos postais e categorias de produtos, sem nomes ou endereços completos.

**EX041.** Que um atacante que calcula o hash de números de associado adivinhados consegue identificar pseudônimos sem chave, mas não os com chave sem conhecer a chave.

**EX042.** Os backups expiram num calendário definido, em vez de serem editados registro por registro.

**EX043.** Para que os resultados sejam comparáveis ao longo do tempo e não possam ser melhorados simplesmente mudando o que conta.

**EX044.** O armazém, com 2 de 15 funcionários, porque a equipe compartilha scanners e não tem dispositivos individuais.

**EX045.** Não prova que os notebooks estão seguros, só que estão em conformidade com uma baseline que pode ter lacunas.

**EX046.** Porque explica como a segurança é alcançada por meio de princípios, serviços, conexões e responsáveis, e não o que foi comprado.

**EX047.** Mostra qual atributo de negócio, como a confiabilidade, seria enfraquecido.

**EX048.** Pela primeira vez, viram a segurança como um projeto coerente, e não como um conjunto de compras.

**EX049.** Qualquer pessoa com a chave pública pode verificar, sem ser capaz de criar assinaturas.

**EX050.** Porque um vazamento do ambiente de teste, menos protegido, permitiria que atacantes forjassem atualizações de entrega em produção.

**EX051.** Do manuseio das chaves, como falta de responsáveis e de rotação, e não de algoritmos fracos.

**EX052.** Funcionários das lojas, orientações presenciais na loja, a comparação com o módulo apenas online e as taxas de reporte.

**EX053.** Porque os funcionários tendem a exagerar seu bom comportamento quando perguntados.

**EX054.** Para que o comportamento de nenhum indivíduo pudesse ser inferido a partir do número de uma loja muito pequena.

**EX055.** As novas contas começam sem acesso até que um papel seja concedido.

**EX056.** Porque funcionários sob pressão de tempo contornam controles que não se encaixam nas suas rotinas.

**EX057.** Ele dava a todo gerente acesso às escalas de todas as lojas, então o fornecedor acrescentou um escopo por loja.

**EX058.** A conta de VPN permanente e com acesso amplo do terceirizado de montagem de lojas.

**EX059.** Mover a exportação de estoque para um bucket privado separado, deixando públicas as imagens de produtos.

**EX060.** Na lição de projeto transferível, e não nos detalhes do incidente.

**EX061.** Uma importação noturna de preços de um fornecedor e um upload manual de planilha.

**EX062.** Porque atravessa uma fronteira de confiança sem validação, de modo que um arquivo ruim poderia mudar preços em toda a loja.

**EX063.** As mudanças de preço não são registradas com a identidade do usuário que as fez.

**EX064.** Ela guardava registros confidenciais de funcionários ao lado de imagens públicas, de modo que os usuários de marketing podiam ler os dados da folha de pagamento.

**EX065.** Identidade e hospedagem, cada uma sustentando todas as 5 funções online.

**EX066.** Porque a redundância custaria mais do que o risco justifica, então ela é aceita com um contrato, um plano e um responsável.

**EX067.** Porque as pessoas que operam o processo conhecem modos de falha que os diagramas não mostram.

**EX068.** Que a gerente da loja sabia de erros passados na retirada de que Hannah não tinha ouvido falar.

**EX069.** Com um código de retirada enviado por SMS e conferido no balcão.

**EX070.** O descarte de mídias, especificamente dos discos rígidos dos caixas antigos.

**EX071.** Como uma revisão mensal de trinta minutos dos alertas de identidade feita por Hannah.

**EX072.** Foram questionados, e dois resquícios de uma antiga exigência de seguradora foram aposentados.

**EX073.** Três: dois funcionários de loja com direitos que sobraram da promoção e um usuário do armazém com direitos de dono do banco de dados de uma correção urgente.

**EX074.** Porque definições incorretas fariam o verificador relatar alarmes falsos.

**EX075.** Acrescentar exceções aprovadas com datas de expiração, para que os direitos temporários continuem visíveis.

**EX076.** A exportação antiga de planilha mantida por uma agência de marketing.

**EX077.** A contingência por e-mail, que por isso precisava de um segundo fator.

**EX078.** O STRIDE deu amplitude, a árvore de ataque deu os caminhos do atacante e as classificações de risco deram a prioridade.

**EX079.** Porque não pode ser verificado, então dá um falso conforto.

**EX080.** Falhas de lógica, como liberar um pedido sem código.

**EX081.** A expiração dos códigos falhou porque a tarefa de expiração não estava agendada em produção.

**EX082.** Porque o monitoramento observava a disponibilidade da loja, e não as mudanças de preço.

**EX083.** Porque qualquer pessoa com a mesma pressão e as mesmas ferramentas poderia ter cometido o mesmo erro.

**EX084.** O novo alerta captou uma conversão de moeda equivocada antes que os clientes a vissem.

**EX085.** Para que as tarefas sejam carregadas pelo calendário e sobrevivam a férias e trocas de pessoal.

**EX086.** Um sim a qualquer pergunta sobre novos fornecedores, dados, cruzamentos de fronteira ou acesso privilegiado.

**EX087.** Para receber apenas os números dos associados e os saldos de pontos, em vez da lista completa de associados.

**EX088.** Compradores viajando a fornecedores causaram muitos alarmes falsos.

**EX089.** Porque a janela de uma hora deixou passar três dos quatro ataques plantados.

**EX090.** Atacantes que fazem login do mesmo país do usuário.

**EX091.** Porque tem poucos usuários e alto valor, o que permite aprender lições antes da migração das lojas movimentadas.

**EX092.** Antecipar, resistir, recuperar e adaptar.

**EX093.** A segunda região de hospedagem, com o processo manual de pedidos ensaiado como contingência por uma temporada.

**EX094.** Como redução da chance de fraude em pagamentos.

**EX095.** A finalidade, os dados ao nível de país, a retenção, o aviso aos funcionários e uma avaliação de interesse legítimo.

**EX096.** Contas de caixa limitadas pré-criadas, ativadas por um gerente na chegada e que expiram no fim da temporada.

**EX097.** As lojas orientadas subiram 0,29 denúncia a mais por funcionário por mês do que as lojas de comparação.

**EX098.** Que o uso do botão de denúncia mede a disposição de denunciar, e não a capacidade de detectar.

**EX099.** Uma implantação aleatorizada em que as lojas são designadas por sorteio.

**EX100.** Para que a opção preferida não influencie o que é medido.

**EX101.** A opção A obteve 3,05 e a opção B, 4,10.

**EX102.** A opção B continuou vencendo, 3,83 a 3,30.

**EX103.** Os sistemas internos de segurança física dos robôs, que exigem engenheiros especializados.

**EX104.** Para proteger contra o scope creep e deixar claro o que não será entregue.

**EX105.** Para que o sucesso seja julgado por critérios acordados de antemão, e não depois dos resultados.

**EX106.** Porque recomendações que atrasam um turno de distribuição movimentado serão ignoradas.

**EX107.** A implantação do gerenciador de senhas, porque os voluntários não continuariam a usá-lo.

**EX108.** A classificação de dados e o menor privilégio, além da pergunta sobre quem perceberia um problema.

**EX109.** Quem o escreveu, que método, que dados e que interesses o autor tem.

**EX110.** Elas registram o consenso sobre boas práticas, mas não medem resultados.

**EX111.** É uma prática razoável apoiada em consenso e simulação, com poucas evidências de resultado no mundo real para pequenas organizações.

**EX112.** O link de suporte remoto do fornecedor, porque usava uma senha compartilhada.

**EX113.** Ele identificou os entregáveis afetados, acertou marcos revisados e atualizou apenas o que mudou.

**EX114.** Contas nominais com autenticação multifator e sessões gravadas, verificado por um login de teste.

**EX115.** O teste de isolamento da rede dos robôs, porque os robôs não haviam chegado.

**EX116.** Nenhum plano de patches para os controladores dos robôs e nenhum processo para revogar o acesso do fornecedor ao fim do contrato.

**EX117.** Cada uma foi atribuída a um responsável na Fernway, com uma ação agendada.

**EX118.** Ele citou apenas fontes que havia lido.

**EX119.** O ponto único de falha do provedor de identidade.

**EX120.** Tratar os projetos como hipóteses a testar e registrar o que é desconhecido com o mesmo cuidado que o que é conhecido.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Herley, C., & van Oorschot, P. C. (2017). SoK: Science, security and the elusive goal of security as a scientific pursuit. *2017 IEEE Symposium on Security and Privacy*, 99–120. <https://doi.org/10.1109/SP.2017.38>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Joint Task Force. (2018). *Risk management framework for information systems and organizations* (NIST SP 800-37 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-37r2>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Katz, J., & Lindell, Y. (2020). *Introduction to modern cryptography* (3rd ed.). CRC Press.
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., & McQuaid, R. (2021). *Developing cyber-resilient systems: A systems security engineering approach* (NIST SP 800-160 Vol. 2 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v2r1>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sherwood, J., Clark, A., & Lynas, D. (2005). *Enterprise security architecture: A business-driven approach* (SABSA). CMP Books.
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
- Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure software development framework (SSDF) version 1.1* (NIST SP 800-218). NIST. <https://doi.org/10.6028/NIST.SP.800-218>
- The Open Group. (2016, revised 2022). *Integrating risk and security within a TOGAF enterprise architecture* (TOGAF Series Guide G152). The Open Group.
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in software engineering*. Springer. <https://doi.org/10.1007/978-3-642-29044-2>
