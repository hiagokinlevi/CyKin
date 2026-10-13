# Arquitetura e Engenharia de Segurança: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 099, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–14 de 40 já estão escritos em português, com os exercícios EX001–EX042 e suas resoluções com rubricas de 0 a 3 e 4 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 15–40 (EX043–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) |

Capítulos 15–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-15), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX042 (as de EX043–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Lucas Haddon, o Dr. Marco Bellini, Hannah Osei, a Ashgrove University, a Fernway Outdoor Co-operative e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
