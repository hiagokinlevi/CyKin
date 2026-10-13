# Arquitetura e Engenharia de Segurança: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 122, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–42 de 50 já estão escritos em português, com os exercícios EX001–EX126 e suas resoluções com rubricas de 0 a 3 e 13 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 43–50 (EX127–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de engenharia que vão projetar, verificar e operar sistemas seguros.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios calculam crescimento, fecho transitivo, probabilidades, disponibilidade, árvores de falhas, limites de taxa, diferenças entre regras, métricas e digests sobre dados sintéticos, e usam sqlite3 em memória para mostrar a injeção e sua correção; nada toca um sistema real. Projetos de produção usam produtos e padrões consagrados; nunca crie sua própria criptografia. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de engenharia dos fundamentos de matemática, física e programação, passando por redes, engenharia de sistemas e arquitetura de segurança, até o projeto completo de um back-office, dois ateliês, dois laboratórios de verificação, um ensaio de recuperação, um dossiê, uma tese e uma defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Sofia Mbeki** | Estudante de engenharia | Inventada |
| **Daniel Ferreira** | Arquiteto de segurança e mentor | Inventado |
| **Kestrel Polytechnic University** | Universidade fictícia | Inventada |
| **Corvia Regional Transit** | Operadora de transporte fictícia | Inventada |

### Fontes principais

Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); NIST [SP 800-160 Vol. 1 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v1r1), [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5), [SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1) e [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); Shostack (2014); Anderson (2020); SABSA; TOGAF G152. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) |

Capítulos 43–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-43), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) usar taxas de variação para raciocinar sobre cargas de segurança em crescimento; (2) modelar o crescimento exponencial do volume de logs; (3) reconhecer quando uma estimativa linear falha.

### 1.1 O caso e por que cálculo

Sofia Mbeki é estudante do primeiro ano do curso de engenharia de cinco anos da fictícia Kestrel Polytechnic University. Sua parceira na indústria ao longo de todo o curso é a fictícia Corvia Regional Transit, que opera ônibus e bondes, um sistema de bilhetagem por aproximação, um aplicativo para passageiros e as redes das garagens. Seu mentor lá é o arquiteto de segurança Daniel Ferreira. Todas as pessoas, organizações e números aqui são sintéticos. Sofia se pergunta por que um curso de arquitetura começa com cálculo. A resposta de Daniel é prática: arquitetos dimensionam sistemas que crescem, e derivadas descrevem a rapidez com que as coisas mudam. Um pipeline de logs, uma frota de certificados ou uma base de regras que cresce mais rápido do que o esperado vira um problema de segurança muito antes que alguém perceba.

### 1.2 Crescimento exponencial dos logs

Os logs do sistema de bilhetagem da Corvia crescem cerca de quatro por cento ao mês à medida que novos dispositivos são instalados. Sofia modela o volume como V(t) = V0 e^(kt), em que k é a taxa de crescimento mensal na forma contínua. A derivada dV/dt = kV mostra que o aumento de cada mês é proporcional ao volume atual, de modo que o crescimento absoluto se acelera. O laboratório abaixo calcula o volume depois de dois anos a partir de um ponto de partida sintético e o tempo até que o orçamento atual de armazenamento seja ultrapassado. O resultado mostra que o orçamento se esgota mais de um ano antes do que prevê uma estimativa em linha reta, o que importa porque logs descartados deixam cega a equipe de monitoramento de segurança.

### Laboratório — Crescimento dos logs e orçamento de armazenamento

```python
# Synthetic log volume: V(t) = V0 * e^(k t), k from 4%/month; compare with tangent-line forecast.
import math
V0, budget = 8.0, 20.0            # TB at month 0, storage budget in TB
k = math.log(1.04)
exp_v = lambda t: V0 * math.exp(k * t)
lin_v = lambda t: V0 + k * V0 * t  # tangent line at t=0
m = next(t for t in range(200) if exp_v(t) > budget)
ml = next(t for t in range(200) if lin_v(t) > budget)
print(f"month 24: exponential {exp_v(24):.1f} TB, linear {lin_v(24):.1f} TB")
print(f"budget {budget} TB exceeded: exponential month {m}, linear month {ml}")
```

Execute com `python3 lab_growth.py`. Saída verificada:

```text
month 24: exponential 20.5 TB, linear 15.5 TB
budget 20.0 TB exceeded: exponential month 24, linear month 39
```

### 1.3 Quando estimativas lineares falham

Uma estimativa linear supõe um aumento constante por mês e só é precisa em períodos curtos. Sofia compara a reta tangente no mês zero, a previsão linear baseada na derivada, com o modelo exponencial. Nos primeiros meses as duas concordam de perto; no mês vinte e quatro, divergem por uma grande margem. Arquitetos costumam planejar a capacidade a partir do aumento do ano anterior, o que é uma visão linear de um processo exponencial. A lição é geral: sempre que uma grandeza cresce em proporção a si mesma, como dispositivos conectados ou eventos armazenados, use um modelo de crescimento e revise-o à medida que chegam dados reais.

### Exemplo resolvido

Sofia ajusta um modelo de crescimento de quatro por cento ao mês a volumes sintéticos de logs, calcula quando o armazenamento é ultrapassado e mostra a Daniel a diferença entre as previsões linear e exponencial.

> **Caso sintético.** A Kestrel Polytechnic, a Corvia Regional Transit, Sofia, Daniel e todos os números são inventados.

### Erros e limites

O crescimento real raramente é suave; a implantação de novos dispositivos causa saltos. Os modelos precisam ser reajustados aos dados medidos.

### Exercícios

- **EX001 — Crescimento proporcional.** O que dV/dt = kV diz a Sofia sobre o crescimento dos logs? *Rubrica:* 3 = o aumento de cada mês é proporcional ao volume atual, então o crescimento absoluto se acelera;; 2 = proporcional;; 1 = crescimento constante;; 0 = nenhuma.

- **EX002 — Mês do orçamento.** No laboratório, em que mês o orçamento de armazenamento é ultrapassado pela primeira vez no modelo exponencial? *Rubrica:* 3 = mês 24, contra o mês 39 da previsão linear;; 2 = mês 24;; 1 = nenhuma;; 0 = nenhuma.

- **EX003 — Planejamento linear.** Por que é arriscado planejar o armazenamento de logs a partir do aumento do ano anterior? *Rubrica:* 3 = aplica uma visão linear a um processo exponencial e subestima o crescimento;; 2 = subestima;; 1 = é preciso;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) representar direitos de acesso como relações e grafos; (2) calcular o fecho transitivo para encontrar acessos indiretos; (3) usar operações de conjuntos para verificar a segregação de funções.

### 2.1 Acesso como relação

Daniel mostra a Sofia que uma lista de controle de acesso é uma relação: um conjunto de pares (sujeito, objeto). A participação em grupos é outra relação: (usuário, grupo). Grupos podem conter grupos. Escrever isso como conjuntos permite que Sofia raciocine com precisão. Se a usuária ana está no grupo fare-ops, e fare-ops está no grupo fare-admins, e fare-admins pode modificar as tabelas de tarifas, então ana pode modificar tarifas, embora nenhuma entrada isolada diga isso. A matemática discreta fornece a ferramenta para isso: a composição de relações e o fecho transitivo, que tornam visíveis os direitos indiretos em vez de deixá-los enterrados em grupos aninhados que ninguém lê.

### 2.2 Fecho transitivo

O fecho transitivo de uma relação acrescenta todo par alcançável por meio de uma cadeia. Sofia escreve um pequeno programa em Python que recebe as participações aninhadas e sintéticas em grupos da Corvia e calcula, para cada usuário, todos os grupos aos quais ele pertence direta ou indiretamente, e depois os objetos que esses grupos podem acessar. O laboratório abaixo roda sobre um diretório sintético e mostra uma conta de terceirizado herdando direitos de modificação de tarifas por três níveis de aninhamento. A auditoria não havia percebido isso porque os revisores olharam apenas as participações diretas. Cálculos de fecho desse tipo estão por trás de muitas ferramentas comerciais de revisão de acessos, mas entendê-los permite que um engenheiro confira as ferramentas.

### Laboratório — Direitos indiretos via fecho transitivo

```python
# Transitive closure of synthetic nested groups; find indirect tariff rights and SoD conflicts.
member = {"ana": {"fare-ops"}, "ben": {"tariff-approvers"}, "contractor-07": {"vendor-support"},
          "vendor-support": {"field-tech"}, "field-tech": {"fare-ops"}, "fare-ops": {"fare-admins"},
          "dina": {"tariff-approvers", "fare-ops"}}
rights = {"fare-admins": {"tariff:create"}, "tariff-approvers": {"tariff:approve"}}
def closure(x, seen=None):
    seen = seen or set()
    for g in member.get(x, ()):
        if g not in seen: seen.add(g); closure(g, seen)
    return seen
users = ["ana", "ben", "contractor-07", "dina"]
eff = {u: set().union(*(rights.get(g, set()) for g in closure(u))) for u in users}
for u in users: print(f"{u:14} groups={len(closure(u))} rights={sorted(eff[u])}")
create = {u for u in users if "tariff:create" in eff[u]}; approve = {u for u in users if "tariff:approve" in eff[u]}
print("create & approve conflict:", sorted(create & approve))
```

Execute com `python3 lab_closure.py`. Saída verificada:

```text
ana            groups=2 rights=['tariff:create']
ben            groups=1 rights=['tariff:approve']
contractor-07  groups=4 rights=['tariff:create']
dina           groups=3 rights=['tariff:approve', 'tariff:create']
create & approve conflict: ['dina']
```

### 2.3 Segregação de funções como conjuntos

A Corvia exige que ninguém possa ao mesmo tempo criar uma alteração de tarifa e aprová-la. Em termos de conjuntos, o conjunto de usuários capazes de criar e o conjunto capaz de aprovar precisam ser disjuntos. Sofia calcula os dois conjuntos a partir do fecho e sua interseção. Uma interseção não vazia é uma violação. Esse é o princípio da separação de privilégios de Saltzer e Schroeder (1975), expresso como um simples teste de conjuntos. Ela observa que o raciocínio com conjuntos capta violações estruturais, mas não o conluio entre duas pessoas, que exige controles de processo como registro em log e revisão.

### Exemplo resolvido

Sofia calcula o fecho de grupos aninhados sintéticos, encontra um terceirizado com direitos indiretos sobre tarifas e testa os conjuntos de criação e aprovação, encontrando dina nos dois.

> **Caso sintético.** Os usuários, grupos e direitos são sintéticos; Saltzer e Schroeder (1975) é real.

### Erros e limites

O fecho supõe que as participações estão atualizadas; dados desatualizados escondem ou inventam direitos. Conjuntos disjuntos não impedem o conluio.

### Exercícios

- **EX004 — Direito oculto.** Que conta ganhou direitos sobre tarifas indiretamente no laboratório, e por quantos níveis? *Rubrica:* 3 = contractor-07, por uma cadeia de quatro grupos que termina em fare-admins;; 2 = a conta;; 1 = nenhuma;; 0 = nenhuma.

- **EX005 — Teste de SoD.** Como a segregação de funções é expressa com conjuntos? *Rubrica:* 3 = os conjuntos de criadores e de aprovadores devem ser disjuntos; interseção vazia;; 2 = disjuntos;; 1 = união;; 0 = nenhuma.

- **EX006 — Lacuna do conluio.** O que uma verificação de conjuntos disjuntos não consegue impedir? *Rubrica:* 3 = o conluio entre duas pessoas diferentes;; 2 = conluio;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) relacionar fenômenos físicos a riscos de segurança do hardware; (2) explicar por que emanações e consumo de energia podem vazar informação; (3) ligar limites físicos a escolhas de arquitetura.

### 3.1 Informação é física

O módulo de física de Sofia cobre eletricidade, sinais e calor. Daniel o liga à segurança: computadores são dispositivos físicos, então a computação produz efeitos mensuráveis, como variação de consumo de energia, emissão eletromagnética, diferenças de tempo e calor. Anderson (2020) descreve como esses side channels já vazaram chaves e dados. Para um arquiteto, a lição não é construir bancadas de medição, e sim reconhecer onde o acesso físico ou a proximidade criam risco, como em leitores de cartões de passagem montados em ônibus públicos, onde um atacante pode tocar, abrir ou acoplar instrumentos ao dispositivo por horas sem ser notado pela equipe.

### 3.2 Energia, tempo e emissões

O consumo de energia varia conforme as operações que um chip executa. Se o consumo de um dispositivo depende de dados secretos, um atacante que o mede às vezes consegue recuperar o segredo; isso se chama análise de consumo de energia (power analysis). O tempo funciona de forma parecida no software, e é por isso que comparações em tempo constante são usadas para segredos. Emissões eletromagnéticas de cabos e telas também podem carregar sinais. Sofia aprende que se defender disso é principalmente tarefa dos projetistas de hardware e de secure elements certificados, e que a responsabilidade do arquiteto é escolher componentes avaliados contra esses ataques para os lugares onde os atacantes têm acesso físico.

### 3.3 Limites físicos na arquitetura

A física também impõe limites que os arquitetos precisam respeitar. A propagação de sinais e a latência de rede fazem com que o validador de passagens de um bonde nem sempre consiga alcançar o servidor central a tempo, então ele precisa tomar algumas decisões offline com chaves e listas de bloqueio armazenadas localmente. Baterias e calor limitam quanto trabalho criptográfico um dispositivo portátil de fiscalização consegue fazer. A resistência física a adulteração custa dinheiro e espaço. Sofia escreve uma nota curta para Daniel explicando que os validadores de passagens devem usar secure elements para as chaves e devem ser projetados para funcionar offline com segurança, porque é a física, e não a preferência, que impõe esse projeto.

### Exemplo resolvido

Sofia lista três side channels físicos, mapeia-os para os leitores de passagens embarcados da Corvia e defende secure elements e uma operação offline segura.

> **Caso sintético.** Os locais dos dispositivos e as notas de projeto são sintéticos; Anderson (2020) é real.

### Erros e limites

O risco de side channel depende do acesso e da habilidade do atacante; nem todo dispositivo precisa da mesma proteção. Os limites físicos mudam à medida que o hardware evolui.

### Exercícios

- **EX007 — Risco de acesso físico.** Por que os leitores de passagens nos ônibus estão mais expostos a side channels do que os servidores de data center? *Rubrica:* 3 = atacantes podem tocá-los e instrumentá-los por longos períodos em público;; 2 = acesso;; 1 = mesmo risco;; 0 = nenhuma.

- **EX008 — Papel do arquiteto.** Qual é a responsabilidade do arquiteto quanto à análise de consumo de energia? *Rubrica:* 3 = escolher componentes avaliados contra ela onde houver acesso físico;; 2 = escolher componentes;; 1 = construir bancadas;; 0 = nenhuma.

- **EX009 — Offline pela física.** Por que os validadores de passagens precisam tomar algumas decisões offline? *Rubrica:* 3 = limites de latência e conectividade fazem com que o servidor possa não ser alcançado a tempo;; 2 = latência;; 1 = preferência;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever programas pequenos e legíveis que validam a entrada; (2) tratar erros sem vazar detalhes sensíveis; (3) usar a biblioteca padrão em vez de reinventar funções de segurança.

### 4.1 Programas que verificam a entrada

O primeiro curso de programação de Sofia usa Python. Daniel pede que ela escreva um parser para registros sintéticos de validação de passagens: identificador do cartão, identificador do validador, timestamp e valor. Sua primeira versão confia em todos os campos. Ele lhe dá linhas malformadas, como um valor negativo, um timestamp no futuro e um identificador de cartão com caracteres inesperados, e o programa ou trava ou aceita absurdos. Ela o reescreve para validar cada campo contra um padrão de allow-list e uma faixa, rejeitando a linha com um motivo. A validação de entrada nas fronteiras é um dos hábitos mais básicos de projeto seguro, e começa nos primeiros programas que um estudante escreve.

### 4.2 Erros sem vazamentos

Quando a validação falha, o programa precisa relatar o suficiente para que um operador corrija o problema, mas sem expor segredos ou detalhes internos a quem forneceu a entrada. Sofia separa duas mensagens: um erro público curto, como registro inválido, e uma entrada detalhada de log interno com o número da linha e o motivo, gravada num arquivo com permissões restritas. Ela evita mostrar stack traces aos usuários. Daniel explica que erros verbosos em serviços web já revelaram nomes de bancos de dados, caminhos de arquivos e versões a atacantes, entregando-lhes um mapa. O tratamento de erros faz parte da interface e merece o mesmo cuidado de projeto.

### 4.3 A biblioteca padrão primeiro

Sofia precisa de identificadores aleatórios para cartões de teste. Primeiro ela usa o módulo random e depois aprende que, para qualquer coisa relevante para a segurança, o módulo secrets do Python é obrigatório, porque ele obtém os valores da fonte segura do sistema operacional. Ela também precisa comparar uma tag de autenticação e aprende a usar hmac.compare_digest. A regra de Daniel é simples: use a biblioteca padrão ou um pacote bem mantido para funções de segurança, leia sua documentação e nunca escreva você mesmo uma cifra, um hash ou um gerador aleatório. A habilidade em programação se mostra ao compor corretamente partes confiáveis, e não ao recriá-las.

### Exemplo resolvido

Sofia reescreve um parser de registros de passagem com validação por allow-list, mensagens de erro públicas e internas separadas e identificadores de teste gerados com secrets.

> **Caso sintético.** Os registros, formatos e identificadores são sintéticos.

### Erros e limites

As allow-lists precisam de manutenção quando os formatos mudam. Os logs internos ainda podem vazar se suas permissões ou sua retenção estiverem erradas.

### Exercícios

- **EX010 — Três campos malformados.** Cite três entradas malformadas que Daniel usou para quebrar o primeiro parser de Sofia. *Rubrica:* 3 = valor negativo, timestamp no futuro, identificador de cartão com caracteres inesperados;; 2 = duas;; 1 = uma;; 0 = nenhuma.

- **EX011 — Duas mensagens.** Que dois tipos de mensagem de erro Sofia produz? *Rubrica:* 3 = mensagem pública curta e log interno detalhado com acesso restrito;; 2 = as duas;; 1 = stack trace;; 0 = nenhuma.

- **EX012 — Módulo secrets.** Por que os identificadores de cartões de teste devem usar secrets em vez de random? *Rubrica:* 3 = secrets usa a fonte segura do sistema operacional; random é previsível;; 2 = fonte segura;; 1 = nenhuma diferença;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever registros de decisão de arquitetura; (2) desenhar diagramas que outras pessoas possam revisar; (3) explicar tradeoffs de segurança a não especialistas.

### 5.1 Registros de decisão

Daniel apresenta o registro de decisão de arquitetura (ADR), um documento curto que declara o contexto, a decisão, as opções consideradas, as consequências e a data. Sofia escreve um para uma escolha simples: se os validadores de passagens devem armazenar uma lista de bloqueio completa dos cartões bloqueados ou consultar o servidor a cada vez. O registro explica as opções, escolhe listas de bloqueio locais com atualizações a cada hora, pela resiliência offline, e declara a consequência de que um cartão recém-bloqueado pode funcionar por até uma hora. Os registros de decisão permitem que futuros engenheiros entendam por que um projeto tem a forma que tem, em vez de adivinhar ou repetir debates antigos.

### 5.2 Diagramas revisáveis

Sofia aprende que um diagrama serve para revisão, não para decoração. Um bom diagrama de fluxo de dados mostra processos, repositórios de dados, entidades externas, fluxos de dados e fronteiras de confiança, a notação que Shostack (2014) usa para a modelagem de ameaças. Cada seta é rotulada com o que flui e por qual protocolo. Cada fronteira é desenhada onde a confiança muda, como entre um ônibus e a rede da garagem. Ela redesenha um diagrama poluído de um fornecedor numa versão limpa, com legenda e número de versão. Os revisores então conseguem apontar exatamente o elemento que questionam, o que torna as revisões mais rápidas e precisas.

### 5.3 Explicar tradeoffs

A diretora financeira da Corvia pergunta por que o sistema de bilhetagem não consegue bloquear instantaneamente cartões roubados. Sofia escreve uma explicação de meia página sem jargão: os validadores funcionam offline nos veículos, atualizam suas listas a cada hora, e o bloqueio instantâneo exigiria uma conectividade constante que os ônibus não têm. Ela declara o risco, um cartão roubado usado por no máximo uma hora, e o custo de reduzi-lo. Daniel elogia a explicação porque ela declara o tradeoff com clareza e deixa a diretora decidir se atualizações mais frequentes valem os custos extras de dados, em vez de esconder a decisão dentro de linguagem técnica.

### Exemplo resolvido

Sofia escreve um registro de decisão sobre as listas de bloqueio, redesenha um diagrama de fornecedor com fluxos e fronteiras rotulados e explica à diretora financeira a janela de bloqueio de uma hora.

> **Caso sintético.** As decisões, os diagramas e a diretora são sintéticos; Shostack (2014) é real.

### Erros e limites

Os registros de decisão ficam desatualizados se não forem revistos quando as decisões mudam. Explicações simples podem omitir casos-limite que importam.

### Exercícios

- **EX013 — Campos do ADR.** Liste os campos de um registro de decisão de arquitetura. *Rubrica:* 3 = contexto, decisão, opções, consequências, data;; 2 = quatro;; 1 = dois;; 0 = nenhuma.

- **EX014 — Posição da fronteira.** Onde uma fronteira de confiança deve ser desenhada num diagrama de fluxo de dados? *Rubrica:* 3 = onde a confiança muda, como entre um ônibus e a rede da garagem;; 2 = mudança de confiança;; 1 = em qualquer lugar;; 0 = nenhuma.

- **EX015 — Janela de bloqueio.** Que risco Sofia declarou à diretora financeira? *Rubrica:* 3 = um cartão roubado pode ser usado por até uma hora;; 2 = uma hora;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) usar integrais para acumular taxas ao longo do tempo; (2) estimar janelas de exposição a partir de taxas variáveis; (3) aplicar aproximações por séries para raciocinar sobre pequenos riscos repetidos.

### 6.1 Acumular taxas

O Cálculo II introduz a integração: somar uma taxa ao longo do tempo para obter um total. Daniel dá a Sofia uma curva sintética de tentativas de validação fraudulentas por hora ao longo de um dia, que sobe no horário de pico e cai à noite. O número total de tentativas é a área sob a curva. Ela aproxima a integral com a regra do trapézio usando amostras de hora em hora. A integração aparece sempre que uma grandeza de segurança é uma taxa: bytes por segundo de exfiltração, logins com falha por minuto ou exposição por dia. São os totais, e não só os picos, que muitas vezes determinam o impacto no negócio que os arquitetos precisam explicar.

### 6.2 Janelas de exposição

As listas de bloqueio da Corvia são atualizadas a cada hora, então um cartão roubado continua utilizável até a próxima atualização. Se os furtos acontecem a uma taxa que varia ao longo do dia, o uso indevido esperado depende da taxa integrada sobre cada janela de exposição. Sofia calcula o uso indevido esperado para atualizações a cada hora e a cada quinze minutos, integrando a taxa sintética de uso após furto multiplicada pela janela média restante. O laboratório abaixo compara os dois intervalos de atualização. As atualizações a cada quinze minutos reduzem bastante o uso indevido esperado, e o resultado dá à diretora financeira um número para pesar contra o custo de dados discutido no capítulo 5.

### Laboratório — Exposição sob dois intervalos de atualização

```python
# Expected misuse of stolen cards before deny-list update; synthetic hourly theft-use rate.
rate = [0.2]*6 + [1.5, 3.0, 2.5, 1.0, 0.8, 0.9, 1.2, 0.9, 0.8, 1.0, 2.0, 3.2, 2.6, 1.1, 0.6, 0.4] + [0.2]*2
assert len(rate) == 24
def misuse(update_h):          # each use happens on average update_h/2 hours before the list catches up
    return sum(r * update_h / 2 for r in rate) * 1.0
print(f"daily theft-use events: {sum(rate):.1f}")
for h in (1.0, 0.25):
    print(f"update every {h*60:.0f} min -> expected misuse {misuse(h):.1f} uses/day")
import math
p, n = 0.001, 800
print(f"P(at least one error) exact {1 - (1 - p)**n:.2f}, n*p approx {n*p:.2f}")
```

Execute com `python3 lab_exposure.py`. Saída verificada:

```text
daily theft-use events: 25.1
update every 60 min -> expected misuse 12.6 uses/day
update every 15 min -> expected misuse 3.1 uses/day
P(at least one error) exact 0.55, n*p approx 0.80
```

### 6.3 Séries e pequenos riscos repetidos

Pequenos riscos repetidos muitas vezes se somam. Se cada um de muitos validadores de passagens independentes tem uma pequena probabilidade p de erro de configuração num mês, a probabilidade de que pelo menos um tenha erro é 1 menos (1 menos p) elevado a n. Para p pequeno, uma aproximação por série dá aproximadamente n vezes p, fácil de calcular de cabeça. Sofia usa isso para mostrar que uma taxa de erro de um em mil em oitocentos validadores significa uma alta chance de pelo menos um erro por mês, um argumento a favor da verificação automatizada de configuração, em vez de torcer para que cada dispositivo esteja certo.

### Exemplo resolvido

Sofia integra uma curva sintética de taxa de fraude, compara o uso indevido esperado com atualizações a cada hora e a cada quinze minutos e usa uma aproximação por série para defender verificações automatizadas dos validadores.

> **Caso sintético.** As taxas, as contagens de validadores e os custos são sintéticos.

### Erros e limites

Integrais de taxas estimadas herdam os erros das estimativas. A aproximação n vezes p deixa de valer quando n vezes p não é pequeno.

### Exercícios

- **EX016 — Significado da área.** O que representa a área sob a curva de tentativas de fraude? *Rubrica:* 3 = o número total de tentativas ao longo do dia;; 2 = total;; 1 = pico;; 0 = nenhuma.

- **EX017 — Comparação das atualizações.** Segundo o laboratório, como muda o uso indevido esperado ao passar de atualizações a cada hora para a cada quinze minutos? *Rubrica:* 3 = cai para cerca de um quarto, de 12,6 para 3,1 usos;; 2 = cai;; 1 = sobe;; 0 = nenhuma.

- **EX018 — Pelo menos um erro.** Com p = 0,001 e n = 800, qual é a chance aproximada de pelo menos um erro? *Rubrica:* 3 = cerca de 0,55 (exata) ou 0,8 por n p, que aqui superestima;; 2 = aproximação;; 1 = 0,001;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) aplicar a probabilidade condicional a alertas de segurança; (2) explicar o problema da taxa-base na detecção; (3) resumir dados de segurança com estatísticas adequadas.

### 7.1 Probabilidade condicional

O detector de fraudes da Corvia sinaliza validações suspeitas. Seu fornecedor afirma que ele detecta noventa e cinco por cento das validações fraudulentas e sinaliza por engano apenas um por cento das legítimas. Sofia aprende a fazer uma pergunta diferente: dado que uma validação foi sinalizada, qual a probabilidade de ser fraude? Isso é uma probabilidade condicional, e o teorema de Bayes a liga às taxas do detector e à taxa-base, a fração de todas as validações que são fraudulentas. Os arquitetos precisam desse raciocínio porque decidem como os alertas chegam aos analistas e se o bloqueio automático é seguro.

### 7.2 O problema da taxa-base

A fraude é rara: nos dados sintéticos da Corvia, cerca de uma validação em duas mil. Sofia calcula a probabilidade de que uma validação sinalizada seja fraude. O laboratório abaixo mostra que ela fica abaixo de cinco por cento: a maioria dos sinais é alarme falso, apesar das taxas impressionantes do detector. Bloquear automaticamente todo cartão sinalizado, portanto, incomodaria muitos passageiros honestos. Esse é o problema da taxa-base, e ele afeta a detecção de intrusões em toda parte. Sofia recomenda que os sinais alimentem uma fila de revisão e que só combinações de sinais disparem o bloqueio, uma decisão de projeto que decorre diretamente da aritmética.

### Laboratório — Taxas-base e precisão dos alertas

```python
# P(fraud | flag) via Bayes with synthetic rates.
base, tpr, fpr = 1/2000, 0.95, 0.01
taps = 1_000_000
fraud = taps * base; legit = taps - fraud
tp, fp = fraud * tpr, legit * fpr
print(f"taps {taps:,}: fraud {fraud:.0f}, flagged true {tp:.0f}, flagged false {fp:.0f}")
print(f"P(fraud | flag) = {tp / (tp + fp):.3f}")
```

Execute com `python3 lab_bayes.py`. Saída verificada:

```text
taps 1,000,000: fraud 500, flagged true 475, flagged false 9995
P(fraud | flag) = 0.045
```

### 7.3 Resumir bem os dados

Sofia também aprende a resumir. Os tempos de resposta das revisões de fraude são assimétricos: a maioria é rápida, algumas levam dias. A média é puxada para cima pelos casos lentos, então ela relata a mediana e o percentil noventa junto com ela. Ao comparar dois meses, relata as contagens com seus denominadores, e não só porcentagens, para que os leitores vejam quantos dados estão por trás de cada número. Daniel avisa que muitos dashboards de segurança mostram médias de dados assimétricos e variações percentuais sobre números minúsculos, e as duas coisas enganam os tomadores de decisão sobre o que de fato está acontecendo.

### Exemplo resolvido

Sofia aplica o teorema de Bayes às taxas do fornecedor, mostra que a maioria dos sinais é alarme falso com uma taxa-base de um em dois mil e redesenha o fluxo de alertas com uma fila de revisão.

> **Caso sintético.** As taxas do detector e os dados de fraude são sintéticos.

### Erros e limites

Taxas do fornecedor medidas em outros dados podem não valer na Corvia. As premissas de independência entre sinais costumam ser falsas.

### Exercícios

- **EX019 — Inversão da pergunta.** Que probabilidade importa para um analista diante de uma validação sinalizada? *Rubrica:* 3 = a probabilidade de fraude dado um sinal;; 2 = condicional;; 1 = taxa de detecção;; 0 = nenhuma.

- **EX020 — Precisão no laboratório.** Que fração das validações sinalizadas era fraude no laboratório? *Rubrica:* 3 = cerca de 4,5 por cento;; 2 = abaixo de cinco por cento;; 1 = 95 por cento;; 0 = nenhuma.

- **EX021 — Resumo de dados assimétricos.** Por que relatar a mediana e o percentil 90 dos tempos de revisão? *Rubrica:* 3 = os dados são assimétricos e a média é puxada pelos casos lentos;; 2 = assimetria;; 1 = só a média;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) descrever as camadas de CPU, memória e armazenamento relevantes para a segurança; (2) explicar anéis de privilégio e proteção de memória; (3) explicar raízes de confiança em hardware e o secure boot.

### 8.1 Camadas de um computador

Sofia estuda como processadores, caches, memória principal e armazenamento funcionam juntos. Daniel liga cada camada à segurança. Os caches aceleram o acesso à memória, mas diferenças de tempo entre dados em cache e fora dele já permitiram ataques de side channel como os que Anderson (2020) discute. A memória principal guarda chaves e segredos enquanto os programas rodam, então o acesso físico ou bugs podem expô-los. O armazenamento guarda os dados em repouso, e é por isso que os servidores do sistema de bilhetagem criptografam os discos. Entender as camadas ajuda um arquiteto a perguntar onde um segredo vive a cada momento e que componente precisa ser confiável para protegê-lo ali.

### 8.2 Privilégio e proteção de memória

Os processadores oferecem níveis de privilégio: o kernel do sistema operacional roda com privilégio alto, e as aplicações com privilégio mais baixo. A unidade de gerenciamento de memória dá a cada processo seu próprio espaço de endereçamento, de modo que um programa não consegue ler a memória de outro sem permissão. Esses mecanismos de hardware implementam a mediação completa e o menor privilégio no nível mais baixo. Quando um bug permite que um programa atravesse essas fronteiras, as garantias de todo o sistema falham. Sofia vê por que máquinas virtuais e contêineres dependem de recursos do hardware, e por que vulnerabilidades de kernel são tratadas como críticas: elas minam as fronteiras das quais todos os outros controles dependem.

### 8.3 Raízes de confiança e secure boot

Um dispositivo precisa partir de algo em que confia. Uma raiz de confiança em hardware, como uma ROM de boot e uma chave gravada no chip, verifica a assinatura do primeiro software carregado, que verifica o estágio seguinte, e assim por diante: isso é o secure boot. Os validadores de passagens da Corvia o usam para que firmware adulterado não rode. O NIST SP 800-160 Vol. 1 Rev. 1 trata esses mecanismos como parte da engenharia de confiabilidade ao longo de todo o ciclo de vida. Sofia observa o lado operacional: as chaves de assinatura do firmware precisam ser protegidas, porque quem as possui pode tornar confiável qualquer firmware.

### Exemplo resolvido

Sofia rastreia onde a chave de um validador de passagens vive no armazenamento, na memória e no cache, e explica o secure boot da ROM de boot até a aplicação.

> **Caso sintético.** Os detalhes dos dispositivos são sintéticos; Anderson (2020) e o SP 800-160 Vol. 1 Rev. 1 são reais.

### Erros e limites

As proteções de hardware já tiveram falhas que exigiram correções de microcódigo e de projeto. O secure boot não protege contra bugs em software corretamente assinado.

### Exercícios

- **EX022 — Tempo de cache.** Por que os caches podem criar problemas de segurança? *Rubrica:* 3 = diferenças de tempo entre acessos em cache e fora dele podem vazar informação;; 2 = tempo;; 1 = nenhuma;; 0 = nenhuma.

- **EX023 — Gravidade de bugs de kernel.** Por que vulnerabilidades de kernel são tratadas como críticas? *Rubrica:* 3 = quebram as fronteiras de privilégio e memória das quais os outros controles dependem;; 2 = fronteiras;; 1 = menores;; 0 = nenhuma.

- **EX024 — Risco da chave de assinatura.** Por que as chaves de assinatura de firmware precisam ser protegidas? *Rubrica:* 3 = quem as possui pode tornar qualquer firmware confiável para o secure boot;; 2 = firmware confiável;; 1 = não é importante;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar programas em módulos com interfaces claras; (2) escrever testes, inclusive testes negativos do comportamento de segurança; (3) gerenciar dependências com segurança.

### 9.1 Módulos e interfaces

Em Programação II, Sofia constrói um pequeno motor de regras tarifárias como vários módulos: parsing, consulta de tarifas, regras de desconto e saída. Cada módulo expõe uma interface estreita e esconde seus detalhes internos. Daniel explica por que isso importa para a segurança: interfaces estreitas são mais fáceis de revisar, e um módulo que recebe do parser apenas dados validados não precisa repetir todas as verificações. Isso é economia de mecanismo no nível do código. Quando o módulo de descontos mais tarde precisa de uma mudança, Sofia pode revisar só sua interface e seus testes, e não o programa inteiro, o que reduz a chance de introduzir uma falha em outro lugar.

### 9.2 Testes negativos

Sofia escreve testes unitários para tarifas normais, e então Daniel pede testes negativos: entradas que precisam ser rejeitadas. Um desconto infantil não pode valer para um cartão de adulto; uma zona tarifária fora da rede deve gerar um erro; um valor com mais de duas casas decimais deve ser recusado. Bugs de segurança muitas vezes moram naquilo que um programa aceita por engano, então os testes devem mostrar que entradas ruins falham. Ela roda os testes automaticamente a cada mudança. Os testes negativos também documentam a intenção: um desenvolvedor posterior consegue ver que rejeitar essas entradas foi deliberado, e não um acidente a ser removido.

### 9.3 Dependências

O programa de Sofia usa um pacote de terceiros para ler arquivos de configuração. Daniel lhe mostra como fixar a versão, registrar de onde ele veio e verificar avisos de segurança publicados. O NIST SP 800-218, o Secure Software Development Framework, recomenda práticas como rastrear os componentes e responder às vulnerabilidades encontradas neles. Uma dependência é código que outra pessoa escreveu e que roda com os privilégios do seu programa. Sofia aprende a preferir a biblioteca padrão quando ela basta, escolher pacotes bem mantidos nos demais casos e avaliar quanto código cada nova dependência traz, já que cada linha faz parte da superfície de ataque do sistema.

### Exemplo resolvido

Sofia modulariza um motor de regras tarifárias, acrescenta três testes negativos que precisam falhar com segurança e fixa e registra uma dependência segundo as práticas do SP 800-218.

> **Caso sintético.** O motor e o pacote são sintéticos; o SP 800-218 é real.

### Erros e limites

Os testes mostram a presença de verificações, não a ausência de todos os bugs. Dependências fixadas ainda precisam de atualização quando surgem avisos de segurança.

### Exercícios

- **EX025 — Benefício da interface estreita.** Como interfaces de módulo estreitas ajudam a revisão de segurança? *Rubrica:* 3 = menos para revisar, e dados validados não precisam ser verificados de novo em toda parte;; 2 = revisão;; 1 = nenhuma;; 0 = nenhuma.

- **EX026 — Exemplo de teste negativo.** Dê um teste negativo do motor de Sofia. *Rubrica:* 3 = desconto infantil em cartão de adulto rejeitado, erro para zona fora da rede ou valor com três casas recusado;; 2 = um;; 1 = teste positivo;; 0 = nenhuma.

- **EX027 — Prática com dependências.** O que o SP 800-218 recomenda sobre componentes de terceiros? *Rubrica:* 3 = rastreá-los e responder às vulnerabilidades encontradas neles;; 2 = rastrear;; 1 = ignorar;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar códigos de ética da engenharia a decisões de segurança; (2) reconhecer as dimensões de segurança pública dos sistemas de transporte; (3) lidar com conflitos entre prazos e segurança.

### 10.1 Deveres de um engenheiro

Os códigos profissionais de engenharia em geral colocam a segurança, a saúde e o bem-estar públicos acima dos interesses do empregador ou do cliente, e exigem honestidade sobre os limites da própria competência. Daniel pede que Sofia leia o código do órgão de engenharia do seu país e o aplique ao trabalho de segurança. Esconder uma fraqueza conhecida para cumprir uma data de lançamento conflita com o dever de honestidade. Alegar especialidade numa área que ela não estudou conflita com os limites de competência. Engenheiros de segurança enfrentam esses dilemas com frequência, e a ética oferece um referencial para decidir antes que a pressão chegue, em vez de improvisar quando um gestor pede silêncio.

### 10.2 Segurança física em sistemas de transporte

Sistemas de transporte carregam pessoas, então falhas de segurança da informação podem virar falhas de segurança física. Se um atacante interrompe as telas de informação aos passageiros durante uma emergência, as pessoas podem ir para a plataforma errada. Se as catracas falham fechadas durante uma evacuação, podem prender passageiros. Sofia aprende que os padrões fail-safe de Saltzer e Schroeder (1975) precisam ser interpretados com cuidado: para o acesso a dados, negar por padrão; para catracas físicas durante alarmes de incêndio, abrir por padrão. A arquitetura de segurança no transporte precisa ser coordenada com os engenheiros de segurança física, que muitas vezes têm deveres regulatórios e seus próprios métodos de análise.

### 10.3 Prazo versus segurança

Durante o estágio de Sofia, um terceirizado quer ativar uma nova funcionalidade do aplicativo de passageiros antes que sua revisão de segurança esteja concluída, por causa de um lançamento para a imprensa. Sofia, como estudante, não pode aprová-la nem bloqueá-la, mas pode registrar sua preocupação por escrito a Daniel com o risco específico: na build de teste, a funcionalidade expõe históricos de viagem por uma interface sem autenticação. Daniel escala o caso, e a funcionalidade é lançada uma semana depois, após uma correção. A lição é que a ética muitas vezes significa tornar um risco visível, por escrito, à pessoa certa, de forma clara e rápida.

### Exemplo resolvido

Sofia relaciona o código de engenharia a três dilemas de segurança, distingue os padrões fail-safe para dados e para o mundo físico e escreve uma nota de risco concisa que adia um lançamento inseguro.

> **Caso sintético.** O lançamento, o terceirizado e a funcionalidade do aplicativo são sintéticos; Saltzer e Schroeder (1975) é real.

### Erros e limites

Os códigos de ética variam por país e por órgão. Levantar uma preocupação não garante ação; é preciso haver caminhos de escalonamento.

### Exercícios

- **EX028 — Dever primordial.** O que os códigos de engenharia colocam acima dos interesses do empregador? *Rubrica:* 3 = a segurança, a saúde e o bem-estar públicos;; 2 = segurança;; 1 = lucro;; 0 = nenhuma.

- **EX029 — Padrão das catracas.** Durante um alarme de incêndio, as catracas devem falhar abertas ou fechadas, e por quê? *Rubrica:* 3 = abertas, para que os passageiros possam evacuar; a segurança física prevalece sobre a proteção da tarifa;; 2 = abertas;; 1 = fechadas;; 0 = nenhuma.

- **EX030 — Ação da estudante.** O que Sofia podia fazer quanto ao lançamento prematuro? *Rubrica:* 3 = registrar o risco específico por escrito a Daniel para escalonamento;; 2 = preocupação por escrito;; 1 = nada;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) mapear as zonas de rede e os protocolos da Corvia; (2) explicar o que TLS, VPNs e segmentação protegem; (3) identificar fraquezas de arquitetura numa rede plana.

### 11.1 Mapear zonas

Sofia desenha a rede da Corvia: ônibus e bondes se conectam por enlaces celulares a um gateway na garagem; as garagens se conectam ao data center central; o aplicativo de passageiros e o site ficam num ambiente de nuvem; os escritórios corporativos têm rede própria. Cada zona tem usuários, dispositivos e ameaças diferentes. Ela lista os protocolos que atravessam cada fronteira, como HTTPS para o aplicativo, uma VPN dos veículos até as garagens e um protocolo proprietário do fornecedor para os validadores de passagens. Um mapa assim é o ponto de partida de toda revisão de arquitetura, porque as proteções precisam ser colocadas onde o tráfego atravessa fronteiras de confiança.

### 11.2 O que os protocolos protegem

O TLS, especificado na RFC 8446, protege os dados em trânsito entre dois endpoints com criptografia, integridade e autenticação do servidor. Uma VPN cria um túnel criptografado entre redes, de modo que o tráfego dos veículos que atravessa redes celulares públicas fica protegido. Nenhum dos dois controla o que acontece dentro de um endpoint nem quais sistemas internos um dispositivo conectado pode alcançar. A segmentação faz isso, limitando quais zonas podem falar com quais. Sofia observa que uma VPN que joga cada ônibus direto na rede central sem filtragem protegeria a confidencialidade no enlace celular, mas daria a um ônibus comprometido um caminho para tudo.

### 11.3 Fraquezas das redes planas

Na garagem mais antiga da Corvia, notebooks da equipe, servidores de bilhetagem e impressoras compartilham um único segmento de rede. Sofia explica o risco a Daniel: um notebook infectado consegue alcançar diretamente os servidores de bilhetagem, e o monitoramento não consegue distinguir com facilidade o tráfego normal do anormal quando tudo fala com tudo. Anderson (2020) descreve incidentes em que redes internas planas deixaram atacantes se moverem livremente. Ela propõe separar as zonas com firewalls e permitir apenas os fluxos necessários, a abordagem depois formalizada em orientações de zero trust como o SP 800-207, e lista os fluxos de que cada zona legitimamente precisa como base para as regras.

### Exemplo resolvido

Sofia mapeia seis zonas da Corvia e seus protocolos de fronteira, explica os limites dos túneis VPN e propõe segmentar a rede plana da garagem pelos fluxos necessários.

> **Caso sintético.** As zonas e os fluxos são sintéticos; a RFC 8446, o SP 800-207 e Anderson (2020) são reais.

### Erros e limites

Mapas de rede ficam desatualizados rapidamente. As regras de segmentação precisam ser mantidas, ou derivam de volta para uma rede plana.

### Exercícios

- **EX031 — Limite da VPN.** O que uma VPN de veículo não controla? *Rubrica:* 3 = quais sistemas internos o dispositivo conectado pode alcançar;; 2 = alcance;; 1 = confidencialidade;; 0 = nenhuma.

- **EX032 — Risco da garagem plana.** Cite dois problemas da rede plana da garagem. *Rubrica:* 3 = notebook infectado alcança os servidores de bilhetagem; o monitoramento não separa o normal do anormal;; 2 = dois;; 1 = um;; 0 = nenhuma.

- **EX033 — Base das regras.** Em que as regras de segmentação devem se basear? *Rubrica:* 3 = nos fluxos de que cada zona legitimamente precisa;; 2 = fluxos necessários;; 1 = todos os fluxos;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) explicar o isolamento de processos, usuários e permissões; (2) fazer o hardening de uma baseline de servidor; (3) relacionar o logging do sistema operacional à detecção no nível da arquitetura.

### 12.1 Isolamento e permissões

Os sistemas operacionais isolam processos e controlam o acesso a arquivos por meio de usuários, grupos e permissões. Sofia estuda um servidor Linux de bilhetagem: o serviço de bilhetagem roda com sua própria conta, que pode ler sua configuração e gravar seus logs, mas não pode modificar arquivos do sistema. Os administradores usam contas separadas com direitos elevados só quando necessário. Isso é o menor privilégio aplicado ao sistema operacional. Ela encontra um script legado rodando como root por conveniência, e Daniel explica que um único processo root comprometido mina todas as outras permissões, então o script é reescrito para rodar sob uma conta restrita.

### 12.2 Hardening da baseline

A Corvia usa uma baseline de hardening para servidores: desativar serviços não usados, remover contas padrão, aplicar atualizações num calendário, exigir autenticação forte dos administradores e ativar firewalls de host. Famílias de controles do SP 800-53 Rev. 5, como gestão de configuração e integridade de sistemas e informações, descrevem essas expectativas. Sofia aplica a baseline a um servidor de laboratório e registra cada mudança. Ela aprende que o hardening reduz a superfície de ataque, mas que uma baseline só é útil se os desvios forem detectados, então também agenda uma verificação de configuração que relata a cada semana a deriva em relação à baseline.

### 12.3 Logging para detecção

Os sistemas operacionais registram logins, mudanças de privilégio, inícios de processos e falhas de serviços. Um arquiteto decide quais desses logs são coletados centralmente, por quanto tempo são guardados e quem pode alterá-los. Sofia configura seu servidor de laboratório para enviar os logs de autenticação e de privilégio a um coletor central que os administradores do servidor não podem modificar, de modo que um intruso com acesso ao servidor não consiga apagar as evidências. Ela documenta quais eventos são coletados e por quê. O desenho do logging é uma decisão de arquitetura, porque determina se os ataques podem sequer ser percebidos e investigados.

### Exemplo resolvido

Sofia remove um script que rodava como root, aplica e registra uma baseline de hardening com verificações semanais de deriva e envia logs resistentes a adulteração a um coletor central.

> **Caso sintético.** Os servidores, os scripts e as configurações da baseline são sintéticos; o SP 800-53 Rev. 5 é real.

### Erros e limites

Baselines podem quebrar software legado; teste antes de implantar. Logs centrais podem ficar sobrecarregados sem filtragem.

### Exercícios

- **EX034 — Perigo do script root.** Por que o script que rodava como root foi reescrito? *Rubrica:* 3 = um processo root comprometido mina todas as outras permissões;; 2 = risco do root;; 1 = estilo;; 0 = nenhuma.

- **EX035 — Verificações de deriva.** Por que agendar verificações semanais de configuração depois do hardening? *Rubrica:* 3 = para detectar desvios da baseline ao longo do tempo;; 2 = deriva;; 1 = não são necessárias;; 0 = nenhuma.

- **EX036 — Imutabilidade dos logs.** Por que enviar os logs a um coletor que os administradores do servidor não podem modificar? *Rubrica:* 3 = um intruso no servidor não consegue apagar as evidências;; 2 = evidências;; 1 = velocidade;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem

Você vai (1) classificar os dados de uma organização de transporte; (2) prevenir injeção com consultas parametrizadas; (3) projetar a retenção e a minimização de dados.

### 13.1 Classificar dados

A Corvia guarda vários tipos de dados: identificadores de cartões e históricos de viagem, tokens de pagamento, registros de funcionários, dados de horários e telemetria dos veículos. Sofia ajuda a classificá-los. Os históricos de viagem são dados pessoais que revelam onde as pessoas moram e trabalham; os tokens de pagamento são dados financeiros sensíveis; os horários são públicos. A classificação orienta a arquitetura: dados pessoais e de pagamento precisam de criptografia, controles de acesso e logging, enquanto dados públicos precisam de integridade, mas não de confidencialidade. Daniel ressalta que a classificação precisa ser feita antes do projeto, porque adaptar a proteção a um banco cheio de dados misturados é caro e muitas vezes incompleto.

### 13.2 Consultas parametrizadas

Sofia escreve uma consulta para buscar viagens pelo identificador do cartão. Sua primeira versão monta a string SQL concatenando a entrada do usuário. Daniel lhe mostra que uma entrada como uma aspa seguida de OR 1=1 muda o sentido da consulta e devolve todas as viagens, um ataque de injeção. A correção é uma consulta parametrizada, em que o driver do banco passa a entrada como dado, nunca como código. O laboratório abaixo demonstra as duas com o módulo sqlite3 embutido no Python, sobre uma tabela sintética. A consulta concatenada vaza todas as linhas; a parametrizada não devolve nenhuma para a entrada maliciosa.

### Laboratório — Consulta concatenada versus parametrizada

```python
# Injection vs parameterised query with stdlib sqlite3 on a synthetic table.
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE journeys (card TEXT, stop TEXT)")
db.executemany("INSERT INTO journeys VALUES (?, ?)", [("C100", "Harbour"), ("C100", "Market"), ("C200", "Depot"), ("C300", "Airport")])
evil = "X' OR '1'='1"
rows_bad = db.execute(f"SELECT * FROM journeys WHERE card = '{evil}'").fetchall()   # never do this
rows_ok = db.execute("SELECT * FROM journeys WHERE card = ?", (evil,)).fetchall()
print("concatenated query rows:", len(rows_bad))
print("parameterised query rows:", len(rows_ok))
print("legit lookup C100:", len(db.execute("SELECT * FROM journeys WHERE card = ?", ("C100",)).fetchall()))
```

Execute com `python3 lab_sqli.py`. Saída verificada:

```text
concatenated query rows: 4
parameterised query rows: 0
legit lookup C100: 2
```

### 13.3 Retenção e minimização

Guardar dados para sempre aumenta o dano de qualquer vazamento. Sofia propõe um desenho de retenção: históricos de viagem detalhados mantidos por noventa dias para atendimento ao cliente e investigação de fraudes, e depois agregados em contagens anônimas para o planejamento. Os tokens de pagamento são mantidos só pelo tempo que o provedor de pagamentos exige. A ISO/IEC 27002:2022 inclui controles sobre exclusão de informações e mascaramento de dados. Ela documenta cada prazo de retenção com sua finalidade. A minimização é um controle de arquitetura: dados que não são armazenados não podem ser roubados, e um conjunto de dados menor é mais fácil de proteger bem.

### Exemplo resolvido

Sofia classifica cinco tipos de dados da Corvia, demonstra a injeção e sua correção no sqlite3 e propõe um desenho de retenção de noventa dias para os históricos de viagem.

> **Caso sintético.** Os dados, as tabelas e os prazos de retenção são sintéticos; a ISO/IEC 27002:2022 é real.

### Erros e limites

A agregação ainda pode permitir a reidentificação em grupos pequenos. As regras de retenção dependem da lei e precisam ser conferidas com o jurídico.

### Exercícios

- **EX037 — Sensibilidade das viagens.** Por que os históricos de viagem são dados pessoais que precisam de proteção? *Rubrica:* 3 = revelam onde as pessoas moram, trabalham e circulam;; 2 = localização;; 1 = públicos;; 0 = nenhuma.

- **EX038 — Resultado da injeção no laboratório.** O que o laboratório devolveu para a entrada maliciosa em cada estilo de consulta? *Rubrica:* 3 = a concatenada devolveu as 4 linhas; a parametrizada devolveu 0;; 2 = as duas;; 1 = iguais;; 0 = nenhuma.

- **EX039 — Lógica da minimização.** Por que a minimização de dados é um controle de segurança? *Rubrica:* 3 = dados não armazenados não podem ser roubados, e conjuntos menores são mais fáceis de proteger;; 2 = não roubados;; 1 = não é um controle;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem

Você vai (1) integrar atividades de segurança a um ciclo de vida de desenvolvimento; (2) conduzir uma revisão de projeto leve; (3) usar com eficácia a revisão de código e as verificações automatizadas.

### 14.1 Segurança no ciclo de vida

Sofia entra por um semestre numa equipe da Corvia que constrói um novo serviço de reembolso de passagens. O ciclo de vida da equipe tem requisitos, projeto, implementação, testes, release e manutenção. Daniel lhe mostra onde a segurança se encaixa: casos de abuso junto com os requisitos, modelagem de ameaças no projeto, codificação segura e revisão durante a implementação, testes de segurança antes do release e resposta a vulnerabilidades depois dele. O NIST SP 800-218 organiza essas práticas em grupos: preparar a organização, proteger o software, produzir software bem protegido e responder a vulnerabilidades. Integrar a segurança a cada fase custa menos do que tentar acrescentá-la no fim.

### 14.2 Revisão de projeto leve

Antes de começar a codificação, a equipe faz uma revisão de projeto de uma hora. Eles desenham um diagrama de fluxo de dados do serviço de reembolso, marcam as fronteiras de confiança e passam cada elemento pelas categorias STRIDE, como Shostack (2014) descreve. Descobrem que as solicitações de reembolso poderiam ser repetidas (replay) para obter reembolsos em dobro, e que a equipe de suporte poderia aprovar as próprias solicitações de reembolso. As mitigações são registradas: identificadores únicos de solicitação verificados no servidor e uma regra de que o aprovador deve ser diferente do solicitante. Sofia observa que uma hora encontrou dois problemas sérios que teriam sido caros de corrigir depois do release.

### 14.3 Revisões e automação

Durante a implementação, toda mudança é revisada por outro engenheiro usando um checklist curto: validação de entrada, verificações de autorização, tratamento de erros e logging. Verificações automatizadas rodam análise estática e varredura de dependências a cada commit. Sofia aprende que as ferramentas captam padrões comuns, mas deixam passar falhas de projeto como o problema da autoaprovação, enquanto as pessoas se cansam de verificações repetitivas que as ferramentas fazem bem. Combinar as duas coisas é eficiente. A equipe acompanha os achados até o fechamento e examina todo achado que as ferramentas deixaram passar para melhorar o checklist, um ciclo de feedback que melhora o próprio processo.

### Exemplo resolvido

Sofia relaciona os grupos de práticas do SP 800-218 ao projeto de reembolso, participa de uma revisão STRIDE que encontra problemas de replay e de autoaprovação e ajuda a refinar o checklist de revisão.

> **Caso sintético.** O serviço de reembolso e os achados são sintéticos; o SP 800-218 e Shostack (2014) são reais.

### Erros e limites

Revisões leves deixam passar problemas fora do diagrama. As ferramentas produzem falsos positivos que as equipes aprendem a ignorar se não forem ajustadas.

### Exercícios

- **EX040 — Grupos do SP 800-218.** Cite os quatro grupos de práticas do SP 800-218. *Rubrica:* 3 = preparar a organização, proteger o software, produzir software bem protegido, responder a vulnerabilidades;; 2 = três;; 1 = um;; 0 = nenhuma.

- **EX041 — Achados do reembolso.** Que dois problemas a revisão de projeto encontrou? *Rubrica:* 3 = replay de solicitações de reembolso e autoaprovação pela equipe de suporte;; 2 = os dois;; 1 = um;; 0 = nenhuma.

- **EX042 — Ferramentas versus pessoas.** Que tipo de falha as ferramentas costumam deixar passar? *Rubrica:* 3 = falhas de projeto, como a lógica de autoaprovação;; 2 = falhas de projeto;; 1 = sintaxe;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem

Você vai (1) definir ativos, ameaças, vulnerabilidades e risco; (2) aplicar os princípios de Saltzer e Schroeder a um projeto; (3) distinguir controles preventivos, detectivos e corretivos.

### 15.1 Vocabulário essencial

O curso de fundamentos de segurança de Sofia oferece palavras precisas. Um ativo é algo de valor, como o banco de dados de bilhetagem. Uma ameaça é uma causa potencial de dano, como um grupo de fraudadores. Uma vulnerabilidade é uma fraqueza que uma ameaça poderia explorar, como uma interface sem autenticação. O risco combina a probabilidade de que uma ameaça explore uma vulnerabilidade com o impacto sobre o ativo; o NIST SP 800-30 Rev. 1 descreve como avaliá-lo. Usar essas palavras com cuidado evita debates confusos em que uma pessoa fala de atacantes e outra de bugs, cada uma achando que as duas querem dizer a mesma coisa.

### 15.2 Princípios de projeto na prática

Sofia aplica os princípios de Saltzer e Schroeder ao serviço de reembolso do capítulo 14. Menor privilégio: a equipe de suporte pode ver os reembolsos, mas só supervisores podem aprovar os grandes. Padrões fail-safe: se o serviço de autorização estiver inacessível, os reembolsos são recusados, não aprovados. Mediação completa: toda solicitação de reembolso é verificada, não só a primeira de uma sessão. Projeto aberto: a segurança não depende de esconder como o serviço funciona. Aceitabilidade psicológica: as telas de aprovação são simples o bastante para que os supervisores não busquem atalhos. Escrever cada princípio ao lado de uma escolha de projeto concreta torna ideias abstratas úteis na revisão.

### 15.3 Tipos de controles

Os controles podem prevenir, detectar ou corrigir. A autenticação e a autorização previnem reembolsos não autorizados. O logging e o monitoramento detectam padrões suspeitos, como um cartão recebendo muitos reembolsos. Os controles corretivos restauram a operação normal, como estornar reembolsos fraudulentos e revogar contas comprometidas. Sofia aprende que nenhum controle preventivo é perfeito, então todo ativo importante também precisa de detecção e correção. A ISO/IEC 27002:2022 agrupa os controles nos temas organizacional, de pessoas, físico e tecnológico, uma visão diferente que ajuda a verificar se controles não técnicos, como treinamento e procedimentos, foram considerados.

### Exemplo resolvido

Sofia define ativo, ameaça, vulnerabilidade e risco para o serviço de reembolso, relaciona cinco princípios de projeto a escolhas concretas e lista controles preventivos, detectivos e corretivos.

> **Caso sintético.** O serviço de reembolso e os controles são sintéticos; o SP 800-30 Rev. 1, Saltzer e Schroeder (1975) e a ISO/IEC 27002:2022 são reais.

### Erros e limites

O vocabulário varia entre as normas; defina os termos em cada documento. Os princípios podem entrar em conflito e exigem julgamento.

### Exercícios

- **EX043 — Vulnerabilidade versus ameaça.** Dê um exemplo da Corvia de uma ameaça e de uma vulnerabilidade. *Rubrica:* 3 = ameaça: grupo de fraudadores; vulnerabilidade: interface sem autenticação;; 2 = as duas;; 1 = trocadas;; 0 = nenhuma.

- **EX044 — Reembolso fail-safe.** Como o padrão fail-safe se aplica quando o serviço de autorização está fora do ar? *Rubrica:* 3 = os reembolsos são recusados, não aprovados;; 2 = recusar;; 1 = aprovar;; 0 = nenhuma.

- **EX045 — Temas da ISO.** Que quatro temas a ISO/IEC 27002:2022 usa para agrupar os controles? *Rubrica:* 3 = organizacional, de pessoas, físico, tecnológico;; 2 = três;; 1 = um;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem

Você vai (1) descrever o ciclo de vida da engenharia de sistemas; (2) aplicar conceitos do NIST SP 800-160 Vol. 1 Rev. 1 a um sistema de transporte; (3) construir a rastreabilidade das necessidades até a verificação.

### 16.1 O ciclo de vida

A engenharia de sistemas gerencia sistemas complexos do conceito à desativação. Daniel explica que um sistema de bilhetagem envolve hardware nos veículos, software nos data centers, serviços de nuvem, pessoas e contratos, então precisa ser projetado como um todo. As etapas do ciclo de vida incluem conceito, desenvolvimento, produção, utilização, suporte e desativação. Preocupações de segurança surgem em cada uma: requisitos no conceito, revisões de projeto no desenvolvimento, fabricação segura na produção, monitoramento na utilização, aplicação de patches no suporte e destruição de dados na desativação. Sofia percebe que muitas das falhas de segurança sobre as quais leu aconteceram no suporte ou na desativação, etapas que os projetos costumam negligenciar.

### 16.2 Engenharia de confiabilidade

O NIST SP 800-160 Vol. 1 Rev. 1 trata a segurança como parte da confiabilidade (trustworthiness) do sistema e a integra aos processos de engenharia de sistemas. Ele enfatiza as necessidades de proteção das partes interessadas, os requisitos de segurança derivados delas, a arquitetura e o projeto que satisfazem esses requisitos e a garantia (assurance) de que o sistema de fato o faz. Também lista princípios de projeto, ampliando Saltzer e Schroeder com ideias como persistência mínima e proteção contínua. Sofia usa a publicação para estruturar um artigo curto sobre o validador de passagens, ligando as necessidades de proteção dos passageiros a requisitos como evidência de adulteração e chaves protegidas.

### 16.3 Rastreabilidade

A rastreabilidade liga cada necessidade das partes interessadas a requisitos, elementos de projeto e evidências de verificação. Sofia monta uma pequena tabela de rastreabilidade: a necessidade de que os dados de viagem dos passageiros permaneçam privados se liga a requisitos de criptografia em trânsito e em repouso, que se ligam a elementos de projeto como TLS e criptografia de disco, que se ligam a testes e verificações de configuração. Quando um teste falha ou um requisito muda, a rastreabilidade mostra o que mais é afetado. Sem ela, as equipes não conseguem dizer se toda necessidade foi atendida nem qual elemento de projeto existe por qual motivo.

### Exemplo resolvido

Sofia relaciona preocupações de segurança a seis etapas do ciclo de vida, estrutura um artigo sobre o validador com conceitos do SP 800-160 Vol. 1 Rev. 1 e monta uma tabela de rastreabilidade das necessidades aos testes.

> **Caso sintético.** O artigo sobre o validador e a tabela são sintéticos; o SP 800-160 Vol. 1 Rev. 1 é real.

### Erros e limites

Tabelas de rastreabilidade ficam onerosas se forem detalhadas demais. Os modelos de ciclo de vida simplificam projetos reais, que são iterativos.

### Exercícios

- **EX046 — Etapas negligenciadas.** Que etapas do ciclo de vida costumam ser negligenciadas na segurança? *Rubrica:* 3 = suporte e desativação;; 2 = as duas;; 1 = desenvolvimento;; 0 = nenhuma.

- **EX047 — Fluxo do SP 800-160.** Que cadeia o SP 800-160 Vol. 1 Rev. 1 enfatiza? *Rubrica:* 3 = necessidades de proteção para requisitos, para projeto, para garantia;; 2 = cadeia;; 1 = nenhuma;; 0 = nenhuma.

- **EX048 — Valor da rastreabilidade.** O que a rastreabilidade mostra quando um requisito muda? *Rubrica:* 3 = quais elementos de projeto e testes são afetados;; 2 = itens afetados;; 1 = nada;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem

Você vai (1) descrever ciclos de realimentação nas operações de segurança; (2) simular um rate limiter adaptativo; (3) reconhecer oscilação e atraso em sistemas de controle.

### 17.1 Realimentação na segurança

Um ciclo de realimentação mede uma saída, compara-a com uma meta e ajusta uma entrada. Sofia encontra realimentação por toda parte nas operações de segurança: um rate limiter que aperta quando os logins com falha aumentam, um autoscaler que acrescenta capacidade durante uma inundação de tráfego e uma organização que ajusta seus controles depois de incidentes. A teoria de controle, que ela estuda na engenharia, oferece ferramentas para raciocinar se esses ciclos se estabilizam suavemente, reagem devagar demais ou reagem em excesso. Daniel observa que uma automação de segurança mal ajustada pode causar indisponibilidades, que atacantes podem explorar de propósito ao dispará-la.

### 17.2 Simular um rate limiter

O serviço de login do aplicativo de passageiros usa um rate limiter adaptativo: se os logins com falha num minuto excedem uma meta, a taxa de requisições permitida é reduzida; se ficam abaixo, ela é relaxada. Sofia simula isso com tráfego de ataque sintético que chega no minuto cinco e para no minuto quinze. Com um ganho proporcional alto demais, a taxa permitida oscila para cima e para baixo, ora bloqueando usuários legítimos, ora deixando os ataques passarem. Com um ganho moderado, ela se estabiliza. O laboratório abaixo imprime as duas execuções para que ela veja a diferença, em vez de só ler sobre ela.

### Laboratório — Ganhos do rate limiter adaptativo

```python
# Adaptive rate limiter (proportional control) on synthetic failed-login traffic.
def run(gain, minutes=24, target=50):
    allowed, out = 200.0, []
    for t in range(minutes):
        attack = 400 if 5 <= t < 15 else 0
        failures = min(allowed, 40 + attack) * (0.9 if attack else 0.3)
        allowed = max(20.0, min(400.0, allowed - gain * (failures - target)))
        out.append(round(allowed))
    return out
for g in (2.5, 0.6):
    r = run(g)
    swings = sum(1 for a, b, c in zip(r, r[1:], r[2:]) if (b - a) * (c - b) < 0)
    print(f"gain {g}: allowed/min = {r}")
    print(f"  direction changes: {swings}")
```

Execute com `python3 lab_feedback.py`. Saída verificada:

```text
gain 2.5: allowed/min = [295, 390, 400, 400, 400, 20, 100, 20, 100, 20, 100, 20, 100, 20, 100, 195, 290, 385, 400, 400, 400, 400, 400, 400]
  direction changes: 9
gain 0.6: allowed/min = [223, 246, 268, 291, 314, 174, 110, 81, 67, 61, 58, 57, 56, 56, 56, 78, 101, 124, 147, 170, 192, 215, 238, 261]
  direction changes: 1
```

### 17.3 Atraso e oscilação

Dois problemas se repetem em sistemas com realimentação: o atraso, em que a resposta chega tarde demais, e a oscilação, em que a resposta passa do ponto repetidamente. Um rate limiter que mede em janelas longas fica atrás de ataques súbitos; um que reage a cada segundo pode oscilar. Sofia relaciona isso à resposta a incidentes: uma organização que só muda a política uma vez por ano se atrasa, enquanto uma que reverte decisões toda semana oscila e confunde a equipe. Ela propõe que os controles automatizados tenham tamanhos de ajuste limitados, limites mínimo e máximo e revisão humana quando os limites forem atingidos, para manter a realimentação estável.

### Exemplo resolvido

Sofia simula um rate limiter adaptativo com dois ganhos, mostra a oscilação com o ganho alto e propõe ajustes automáticos limitados e revisados.

> **Caso sintético.** O tráfego e os parâmetros do limiter são sintéticos.

### Erros e limites

Modelos proporcionais simples ignoram a adaptação do atacante. Os resultados da simulação dependem das formas de tráfego supostas.

### Exercícios

- **EX049 — Exploração da automação.** Como atacantes poderiam explorar uma automação de segurança mal ajustada? *Rubrica:* 3 = dispará-la de propósito para causar indisponibilidade aos usuários legítimos;; 2 = disparar;; 1 = nenhuma;; 0 = nenhuma.

- **EX050 — Resultado do ganho alto.** O que aconteceu no laboratório com o ganho alto? *Rubrica:* 3 = a taxa permitida oscilou, alternando entre bloquear usuários e deixar ataques entrarem;; 2 = oscilou;; 1 = estabilizou;; 0 = nenhuma.

- **EX051 — Proposta de estabilização.** Cite duas salvaguardas que Sofia propõe para controles automatizados. *Rubrica:* 3 = ajustes limitados, limites mínimo e máximo, revisão humana nos limites (duas);; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) descrever frameworks de arquitetura de segurança corporativa; (2) construir uma visão de arquitetura em camadas para a Corvia; (3) ligar atributos de negócio a controles técnicos.

### 18.1 Frameworks de arquitetura

A arquitetura de segurança organiza os controles num projeto coerente, e não numa coleção de produtos. O SABSA, descrito por Sherwood, Clark e Lynas (2005), parte de requisitos de negócio expressos como atributos, como disponível, privado ou auditável, e os rastreia por camadas até os componentes físicos e as operações. O guia do The Open Group sobre a integração de risco e segurança no TOGAF mostra como levar a segurança a cada fase do desenvolvimento da arquitetura corporativa. Sofia aprende que os frameworks fornecem vocabulário e estrutura; seu valor está em tornar visíveis, entre as equipes, as premissas e as dependências.

### 18.2 Visão em camadas da Corvia

Sofia constrói uma visão simples em camadas do sistema de bilhetagem. Na camada de negócio: cobrar as tarifas com exatidão, proteger a privacidade dos passageiros, manter os serviços funcionando. Na camada lógica: serviços de identidade, tokenização de pagamentos, logging e gestão de chaves. Na camada física: secure elements nos validadores, módulos de segurança de hardware (HSMs) para as chaves, redes segmentadas. Na camada operacional: monitoramento, resposta a incidentes e gestão de patches. Cada controle aparece numa camada e se liga ao atributo que sustenta. A visão expõe lacunas, como a falta de um responsável operacional pelo serviço de gestão de chaves.

### 18.3 Dos atributos aos controles

Daniel pede que Sofia rastreie para baixo o atributo privacidade dos passageiros. Na camada lógica, ele exige dados minimizados e controle de acesso; na camada física, armazenamento criptografado e redes segmentadas; na camada operacional, revisões de acesso e resposta a vazamentos. Cada ligação é uma afirmação de projeto que pode ser verificada. Quando uma mudança proposta remove um controle, o rastreamento mostra qual atributo de negócio é enfraquecido. Essa ligação de cima para baixo é a contribuição central do SABSA: ela mantém os gastos com segurança atrelados ao que a organização valoriza, e não a tecnologias da moda.

### Exemplo resolvido

Sofia constrói uma visão de arquitetura em quatro camadas do sistema de bilhetagem da Corvia, rastreia a privacidade dos passageiros do atributo à operação e encontra a falta de um responsável pela gestão de chaves.

> **Caso sintético.** A visão de arquitetura e a lacuna são sintéticas; o SABSA e o TOGAF G152 são reais.

### Erros e limites

As visões em camadas simplificam preocupações transversais. Os rastreamentos de atributos podem virar burocracia se não forem mantidos atualizados.

### Exercícios

- **EX052 — Ponto de partida do SABSA.** Por onde o SABSA começa uma arquitetura? *Rubrica:* 3 = por requisitos de negócio expressos como atributos;; 2 = atributos;; 1 = tecnologia;; 0 = nenhuma.

- **EX053 — Lacuna encontrada.** Que lacuna a visão em camadas de Sofia expôs? *Rubrica:* 3 = nenhum responsável operacional pela gestão de chaves;; 2 = responsável;; 1 = nenhuma;; 0 = nenhuma.

- **EX054 — Remoção de um controle.** O que o rastreamento de atributos mostra quando uma mudança remove um controle? *Rubrica:* 3 = qual atributo de negócio é enfraquecido;; 2 = atributo;; 1 = nada;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem

Você vai (1) projetar fluxos de identidade para funcionários, passageiros e dispositivos; (2) posicionar mecanismos criptográficos na arquitetura; (3) planejar a gestão de chaves como um serviço de arquitetura.

### 19.1 Três tipos de identidade

A Corvia tem identidades de funcionários num diretório corporativo, identidades de passageiros no sistema de contas do aplicativo e identidades de dispositivos para validadores e veículos. Cada uma precisa de um projeto diferente. Os funcionários usam single sign-on com autenticação multifator. Os passageiros usam contas no aplicativo com passkeys opcionais, e muitos viajam anonimamente com cartões. Os dispositivos se autenticam com certificados emitidos pela autoridade interna da Corvia e armazenados em secure elements. Sofia desenha os três fluxos num único diagrama e descobre que uma conta de suporte compartilhada de um fornecedor contorna o single sign-on dos funcionários, uma lacuna de identidade que mina o projeto forte nas demais partes.

### 19.2 Posicionar a criptografia

Sofia lista onde a criptografia protege o sistema. O TLS da RFC 8446 protege o tráfego do aplicativo e da web. Uma VPN protege os enlaces dos veículos. Os validadores assinam os registros de validação para que o back-office consiga detectar adulterações. Os dados de pagamento são tokenizados pelo provedor de pagamentos, de modo que a Corvia nunca armazena números de cartão. Os bancos de dados são criptografados em repouso. Cada mecanismo atende a um objetivo específico da classificação do capítulo 13. Ela aprende que o trabalho de um arquiteto é escolher e posicionar mecanismos padronizados, não projetar novos, e que todo mecanismo traz obrigações de gestão de chaves que a arquitetura precisa cumprir.

### 19.3 Gestão de chaves como serviço

As chaves precisam de geração, armazenamento, distribuição, rotação, revogação e destruição. O NIST SP 800-57 Part 1 Rev. 5 dá orientações sobre essas fases e sobre os criptoperíodos. Sofia propõe tratar a gestão de chaves como um serviço de arquitetura com responsável próprio, HSMs para as chaves raiz e de assinatura e procedimentos documentados para cada fase. Isso se liga de volta à lacuna encontrada no capítulo 18. Daniel concorda e acrescenta que o serviço precisa ser testado em exercícios de rotação e de recuperação, porque uma gestão de chaves que nunca foi exercitada costuma falhar na primeira vez em que é necessária.

### Exemplo resolvido

Sofia diagrama as identidades de funcionários, passageiros e dispositivos, encontra uma conta compartilhada de fornecedor que contorna o single sign-on, lista cinco mecanismos criptográficos posicionados e propõe a gestão de chaves como um serviço com responsável.

> **Caso sintético.** As identidades e os mecanismos são sintéticos; a RFC 8446 e o SP 800-57 Part 1 Rev. 5 são reais.

### Erros e limites

Passkeys e certificados ainda dependem de processos de recuperação que podem ser abusados. Os HSMs acrescentam custo e complexidade operacional.

### Exercícios

- **EX055 — Lacuna de identidade.** Que lacuna de identidade Sofia encontrou? *Rubrica:* 3 = uma conta de suporte compartilhada de fornecedor contornando o single sign-on dos funcionários;; 2 = conta compartilhada;; 1 = nenhuma;; 0 = nenhuma.

- **EX056 — Benefício da tokenização.** Por que a tokenização ajuda a Corvia? *Rubrica:* 3 = ela nunca armazena números de cartão, o que reduz a exposição;; 2 = sem números de cartão;; 1 = nenhuma;; 0 = nenhuma.

- **EX057 — Ciclo de vida das chaves.** Liste quatro fases da gestão de chaves. *Rubrica:* 3 = quatro entre geração, armazenamento, distribuição, rotação, revogação, destruição;; 2 = três;; 1 = uma;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Arquitetura e engenharia de segurança: contexto de engenharia

### Objetivos de aprendizagem

Você vai (1) descrever o contexto regulatório, contratual e organizacional da arquitetura da Corvia; (2) identificar partes interessadas e restrições; (3) escrever uma declaração de contexto para um projeto.

### 20.1 Contexto regulatório e contratual

A partir do terceiro ano, Sofia trabalha num projeto em escala real: redesenhar o back-office de bilhetagem da Corvia. Daniel primeiro lhe pede que entenda o contexto. Os pagamentos com cartão trazem obrigações do setor de pagamentos; os dados pessoais trazem a legislação de privacidade; o financiamento público traz exigências de auditoria; e os contratos com fornecedores limitam o que a Corvia pode mudar nos validadores. Ela lista cada obrigação, sua origem e o que ela exige da arquitetura, como a segmentação dos sistemas de pagamento ou a exclusão de dados pessoais a pedido. O contexto restringe o projeto antes de qualquer escolha técnica, então ignorá-lo leva a projetos que não podem ser aprovados.

### 20.2 Partes interessadas e restrições

Sofia identifica as partes interessadas: passageiros, equipe de arrecadação, financeiro, o encarregado de proteção de dados, o centro de operações, os fornecedores de validadores e de pagamentos, os auditores e o conselho da autoridade de transporte. Cada uma tem necessidades e restrições. O financeiro precisa de uma conciliação exata; as operações precisam de sistemas que funcionem durante indisponibilidades; o encarregado de proteção de dados precisa de minimização e de logs de acesso; os fornecedores precisam de interfaces estáveis. As restrições incluem um orçamento fixo, um cronograma de três anos e validadores legados que só podem ser substituídos no quinto ano. Ela registra cada restrição, porque arquitetura é a arte de atender às necessidades dentro das restrições, e não de projetar um sistema ideal.

### 20.3 A declaração de contexto

Sofia escreve uma declaração de contexto de duas páginas para o projeto: propósito, escopo, partes interessadas, obrigações, restrições, premissas e itens fora do escopo. Daniel a revisa com o comitê do projeto, que corrige duas premissas: a tokenização de pagamentos já está contratada, e o aplicativo de passageiros está fora do escopo. Corrigir premissas nesta etapa custa uma reunião; corrigi-las depois do projeto custa meses. A declaração de contexto se torna o primeiro documento do registro de arquitetura e é referenciada por toda decisão posterior, para que os revisores possam verificar se um projeto ainda se ajusta ao seu contexto.

### Exemplo resolvido

Sofia lista quatro fontes de obrigações, mapeia oito partes interessadas e restrições e escreve uma declaração de contexto corrigida pelo comitê do projeto.

> **Caso sintético.** As obrigações, as partes interessadas e as decisões do comitê são sintéticas.

### Erros e limites

A interpretação jurídica exige aconselhamento qualificado. O contexto muda ao longo de projetos longos e precisa ser revisitado.

### Exercícios

- **EX058 — Exemplo de obrigação.** Dê uma obrigação e seu efeito na arquitetura. *Rubrica:* 3 = obrigações de pagamento exigem segmentar os sistemas de pagamento; a privacidade exige suporte à exclusão;; 2 = um par;; 1 = nenhuma;; 0 = nenhuma.

- **EX059 — Restrição legada.** Que restrição limita as mudanças nos validadores? *Rubrica:* 3 = os validadores legados só podem ser substituídos no quinto ano;; 2 = legado;; 1 = orçamento;; 0 = nenhuma.

- **EX060 — Premissas corrigidas.** Que duas premissas o comitê corrigiu? *Rubrica:* 3 = a tokenização já está contratada; o aplicativo de passageiros está fora do escopo;; 2 = as duas;; 1 = uma;; 0 = nenhuma.

<a id="ch-21"></a>

## Capítulo 21 — Arquitetura e engenharia de segurança: requisitos

### Objetivos de aprendizagem

Você vai (1) escrever requisitos de segurança verificáveis; (2) derivar requisitos de necessidades de proteção e de casos de abuso; (3) selecionar controles de catálogos com justificativa.

### 21.1 Requisitos verificáveis

Um requisito como o sistema deve ser seguro não pode ser verificado. Sofia aprende a escrever requisitos que podem ser testados: aprovações de reembolso acima de cinquenta euros devem exigir um segundo aprovador distinto do solicitante; os registros de validação devem ser assinados pelo validador e rejeitados pelo back-office se a assinatura falhar; o acesso administrativo deve exigir autenticação multifator. Cada requisito nomeia quem ou o quê, a condição e o comportamento esperado. Ela acrescenta a cada um um método de verificação, como teste, inspeção ou análise, para que a equipe saiba desde o início como a conformidade será demonstrada.

### 21.2 Casos de abuso

Os casos de uso descrevem o que os usuários legítimos fazem; os casos de abuso descrevem o que atacantes ou insiders descuidados poderiam fazer. Sofia escreve casos de abuso para o back-office: um fraudador repete registros de validação assinados para criar viagens falsas e pedir reembolsos; um insider exporta históricos de viagem para vendê-los; uma conta de fornecedor comprometida envia uma tabela de tarifas maliciosa. Cada caso de abuso leva a requisitos, como detecção de replay com identificadores únicos de registro, registro e aprovação das exportações e tabelas de tarifas assinadas e verificadas antes do uso. Os casos de abuso tornam os requisitos concretos e ajudam as partes interessadas a entender por que cada um existe.

### 21.3 Selecionar controles

O NIST SP 800-53 Rev. 5 oferece um catálogo de controles; a ISO/IEC 27002:2022 oferece outro. Sofia os usa para procurar lacunas nos seus requisitos, e não para copiá-los por inteiro. Por exemplo, a família de auditoria e responsabilização do catálogo a lembra de exigir a proteção e a revisão dos logs, que ela havia esquecido. Para cada controle selecionado, ela registra o requisito que ele sustenta e o motivo. Selecionar controles com justificativa evita tanto lacunas quanto projetos inchados, que implementam controles de que ninguém precisa e consomem um orçamento que poderia tratar riscos reais.

### Exemplo resolvido

Sofia escreve doze requisitos verificáveis com métodos de verificação e três casos de abuso com requisitos derivados, e usa o SP 800-53 Rev. 5 para encontrar um requisito de revisão de logs que faltava.

> **Caso sintético.** Os requisitos e os casos de abuso são sintéticos; o SP 800-53 Rev. 5 e a ISO/IEC 27002:2022 são reais.

### Erros e limites

Os requisitos podem entrar em conflito, como logging versus privacidade. Os catálogos são amplos; adaptá-los exige julgamento.

### Exercícios

- **EX061 — Reescrita verificável.** Reescreva o sistema deve ser seguro como um requisito verificável para reembolsos. *Rubrica:* 3 = reembolsos acima de 50 euros exigem um segundo aprovador distinto do solicitante, verificado por teste;; 2 = verificável;; 1 = vago;; 0 = nenhuma.

- **EX062 — Derivação do caso de abuso.** Que requisito decorre do caso de abuso dos registros de validação repetidos? *Rubrica:* 3 = identificadores únicos de registro com detecção de replay;; 2 = detecção de replay;; 1 = nenhuma;; 0 = nenhuma.

- **EX063 — Uso do catálogo.** Como Sofia usou o SP 800-53 Rev. 5? *Rubrica:* 3 = para procurar lacunas, encontrando um requisito de proteção e revisão de logs que faltava;; 2 = verificação de lacunas;; 1 = copiou tudo;; 0 = nenhuma.

<a id="ch-22"></a>

## Capítulo 22 — Arquitetura e engenharia de segurança: modelos de sistema e de dados

### Objetivos de aprendizagem

Você vai (1) modelar o back-office com componentes, interfaces e fluxos de dados; (2) marcar no modelo as fronteiras de confiança e as classificações dos dados; (3) manter os modelos coerentes com o sistema.

### 22.1 Modelo de componentes e interfaces

Sofia modela o back-office de bilhetagem como componentes: ingestão das validações, construção das viagens, cálculo das tarifas, reembolsos, relatórios e uma camada de integração com o provedor de pagamentos. Cada componente tem interfaces definidas, com formatos de mensagem e requisitos de autenticação. Modelar as interfaces explicitamente ajuda a encontrar lugares onde os dados entram sem validação ou onde um componente confia em outro mais do que deveria. Ela percebe que os relatórios leem diretamente do banco de viagens, em vez de passar por uma interface, contornando os controles de acesso, e registra isso como um problema de projeto para revisão.

### 22.2 Fronteiras e classificações

Na versão de fluxo de dados do modelo, Sofia marca as fronteiras de confiança: entre os validadores e a ingestão, entre o back-office e o provedor de pagamentos e entre o back-office e as estações de trabalho da equipe. Ela rotula cada fluxo de dados com sua classificação do capítulo 13. Os fluxos que levam dados pessoais através de fronteiras precisam de criptografia e autenticação; os que levam dados públicos precisam de integridade. O modelo rotulado se torna a base da modelagem de ameaças do próximo capítulo. Ele também facilita responder à pergunta de um auditor sobre por onde os dados pessoais trafegam.

### 22.3 Manter os modelos fiéis

Os modelos se afastam da realidade à medida que os sistemas mudam. Sofia propõe três práticas: guardar o modelo no controle de versão ao lado do código, revisá-lo em toda revisão de projeto e compará-lo a cada trimestre com os fluxos de rede observados e os logs de acesso. Quando a comparação encontra um fluxo que não está no modelo, ou o modelo ou o sistema está errado, e vale a pena saber qualquer das duas coisas. Daniel observa que diagramas desatualizados são piores do que nenhum, porque dão uma falsa confiança, então o modelo precisa ter um responsável por mantê-lo exato.

### Exemplo resolvido

Sofia modela seis componentes do back-office, encontra os relatórios contornando os controles de acesso, rotula os fluxos pela classificação e estabelece verificações trimestrais entre o modelo e a realidade.

> **Caso sintético.** Os componentes e os fluxos são sintéticos.

### Erros e limites

Os modelos abstraem detalhes onde falhas podem se esconder. Os fluxos observados podem não incluir caminhos raros usados só durante incidentes.

### Exercícios

- **EX064 — Problema de contorno.** Que problema de projeto o modelo de componentes revelou? *Rubrica:* 3 = relatórios lendo diretamente o banco de viagens, contornando os controles de acesso;; 2 = contorno;; 1 = nenhuma;; 0 = nenhuma.

- **EX065 — Fluxos de dados pessoais.** De que precisam os fluxos que levam dados pessoais através de fronteiras? *Rubrica:* 3 = criptografia e autenticação;; 2 = as duas;; 1 = nenhuma;; 0 = nenhuma.

- **EX066 — Resposta à deriva.** O que significa quando os fluxos observados incluem um que não está no modelo? *Rubrica:* 3 = ou o modelo ou o sistema está errado; investigar os dois;; 2 = investigar;; 1 = ignorar;; 0 = nenhuma.

<a id="ch-23"></a>

## Capítulo 23 — Arquitetura e engenharia de segurança: análise de ameaças e falhas

### Objetivos de aprendizagem

Você vai (1) modelar as ameaças do back-office com STRIDE; (2) construir uma árvore de falhas para uma falha crítica; (3) combinar as visões de ameaças e de falhas em riscos priorizados.

### 23.1 STRIDE sobre o modelo

Usando o modelo de fluxo de dados do capítulo 22, Sofia e dois engenheiros passam cada elemento pelo STRIDE: spoofing, tampering, repudiation, information disclosure, denial of service e elevation of privilege, seguindo Shostack (2014). Descobrem que a interface de ingestão aceita registros de qualquer dispositivo que apresente um certificado da autoridade interna, inclusive validadores desativados; que as decisões de reembolso não são registradas com a identidade do aprovador, o que permite o repúdio; e que uma rajada de registros malformados poderia esgotar a fila de construção das viagens. Cada ameaça recebe um responsável, uma mitigação proposta e uma ligação com o requisito que afeta.

### 23.2 Árvore de falhas para a perda de receita

A modelagem de ameaças pergunta o que os atacantes podem fazer; a análise de falhas pergunta como o sistema pode falhar, qualquer que seja a causa. Sofia constrói uma árvore de falhas para o evento de topo em que a receita tarifária de um dia não pode ser conciliada. Ele ocorre se registros de validação forem perdidos ou se o cálculo da tarifa estiver errado. Os registros são perdidos se o buffer do validador transbordar e, ao mesmo tempo, o enlace de upload ficar fora do ar por tempo suficiente. Ela atribui probabilidades sintéticas e calcula a probabilidade do evento de topo com portas AND e OR, supondo independência. O laboratório abaixo mostra o cálculo e qual ramo domina.

### Laboratório — Árvore de falhas para a receita não conciliada

```python
# Fault tree for "day's revenue cannot be reconciled" with synthetic daily probabilities (independence assumed).
p_buffer_overflow = 0.02
p_link_down_long = 0.05
p_records_lost = p_buffer_overflow * p_link_down_long          # AND gate
p_tariff_change_day = 0.10
p_calc_error_given_change = 0.08
p_calc_error = p_tariff_change_day * p_calc_error_given_change  # AND gate
p_top = 1 - (1 - p_records_lost) * (1 - p_calc_error)            # OR gate
print(f"records lost      {p_records_lost:.4f}")
print(f"calculation error {p_calc_error:.4f}")
print(f"top event         {p_top:.4f}  (~{p_top*365:.1f} days/year)")
```

Execute com `python3 lab_fta.py`. Saída verificada:

```text
records lost      0.0010
calculation error 0.0080
top event         0.0090  (~3.3 days/year)
```

### 23.3 Combinar as visões

A árvore de falhas mostra que os erros de cálculo depois de mudanças de tarifa dominam o risco, mais do que os registros perdidos. O modelo de ameaças mostra que uma tabela de tarifas maliciosa enviada por uma conta de fornecedor comprometida poderia causar exatamente essa falha. Combinando as duas visões, Sofia classifica as tabelas de tarifas assinadas e verificadas como a principal mitigação, porque ela trata tanto as causas acidentais quanto as maliciosas da falha mais provável. Ela observa que as premissas de independência nas árvores de falhas podem subestimar o risco quando uma única causa, como uma queda de energia, dispara vários ramos ao mesmo tempo.

### Exemplo resolvido

Sofia conduz uma sessão STRIDE que encontra três ameaças, constrói uma árvore de falhas para a receita não conciliada e prioriza as tabelas de tarifas assinadas, porque as duas análises apontam para erros de tarifa.

> **Caso sintético.** As ameaças, as probabilidades e a árvore de falhas são sintéticas; Shostack (2014) é real.

### Erros e limites

As probabilidades das árvores de falhas muitas vezes são palpites; sua ordenação é mais útil do que os valores absolutos. O STRIDE pode deixar passar ameaças fora do modelo.

### Exercícios

- **EX067 — Validadores desativados.** Que ameaça de spoofing a sessão STRIDE encontrou? *Rubrica:* 3 = validadores desativados com certificados internos ainda podiam enviar registros;; 2 = dispositivos desativados;; 1 = nenhuma;; 0 = nenhuma.

- **EX068 — Ramo dominante.** Que ramo dominou a árvore de falhas no laboratório? *Rubrica:* 3 = erro de cálculo da tarifa depois de mudança de tarifa;; 2 = cálculo;; 1 = registros perdidos;; 0 = nenhuma.

- **EX069 — Ressalva da independência.** Por que as premissas de independência podem subestimar o risco? *Rubrica:* 3 = uma causa comum, como uma queda de energia, pode disparar vários ramos juntos;; 2 = causa comum;; 1 = superestimam;; 0 = nenhuma.

<a id="ch-24"></a>

## Capítulo 24 — Arquitetura e engenharia de segurança: métodos I

### Objetivos de aprendizagem

Você vai (1) comparar métodos de risco qualitativos e quantitativos; (2) conduzir uma avaliação de risco segundo o SP 800-30 Rev. 1; (3) documentar as decisões de risco com responsáveis.

### 24.1 Qualitativo e quantitativo

O risco pode ser classificado qualitativamente, com escalas como baixo, médio e alto, ou quantitativamente, com frequências e perdas estimadas. Os métodos qualitativos são rápidos e ajudam a discussão, mas escondem grandes diferenças dentro de uma mesma categoria. Os métodos quantitativos obrigam a explicitar as premissas, mas podem criar uma falsa precisão quando os dados de entrada são palpites. Sofia usa os dois: uma passada qualitativa para ordenar muitos riscos e, depois, estimativas quantitativas com faixas para os poucos do topo, em que as decisões envolvem dinheiro de verdade. Ela registra as premissas por trás de cada número para que os leitores possam contestá-las, em vez de aceitar um valor pelo que aparenta.

### 24.2 Conduzir uma avaliação

O NIST SP 800-30 Rev. 1 descreve preparar a avaliação, conduzi-la identificando fontes de ameaça, eventos, vulnerabilidades, probabilidade e impacto, comunicar os resultados e manter a avaliação. Sofia segue essas etapas para o back-office. Ela define o escopo e as premissas, identifica as fontes de ameaça a partir da sessão STRIDE e da declaração de contexto, classifica a probabilidade e o impacto em escalas acordadas e registra cada risco. O valor do método está na consistência: outro avaliador que use as mesmas escalas e informações deve chegar a classificações parecidas, o que torna os resultados comparáveis ao longo do tempo e entre sistemas.

### 24.3 Decisões de risco e responsáveis

Cada risco precisa de uma decisão: mitigar, transferir, evitar ou aceitar. Sofia prepara um registro de riscos em que cada entrada tem um responsável com autoridade para decidir. A diretora financeira aceita um risco residual de até uma hora de uso de cartão roubado, documentado no capítulo 5. O chefe de operações é o responsável pelo risco de uso indevido de certificados de validadores e aprova um projeto de revogação. Daniel ressalta que os engenheiros recomendam, mas os responsáveis do negócio decidem, e que os riscos aceitos precisam ser revistos regularmente, porque uma aceitação feita num contexto pode estar errada depois que o contexto muda.

### Exemplo resolvido

Sofia ordena qualitativamente vinte riscos do back-office, estima faixas para os três do topo, segue as etapas do SP 800-30 Rev. 1 e atribui responsáveis e decisões num registro.

> **Caso sintético.** Os riscos, as classificações e os responsáveis são sintéticos; o SP 800-30 Rev. 1 é real.

### Erros e limites

As escalas de risco significam coisas diferentes para pessoas diferentes, a menos que sejam ancoradas com exemplos. As faixas quantitativas continuam incertas.

### Exercícios

- **EX070 — Fraqueza qualitativa.** Qual é uma fraqueza das escalas de risco qualitativas? *Rubrica:* 3 = escondem grandes diferenças dentro de uma mesma categoria;; 2 = esconde diferenças;; 1 = nenhuma;; 0 = nenhuma.

- **EX071 — Etapas do SP 800-30.** Cite as quatro etapas principais do SP 800-30 Rev. 1. *Rubrica:* 3 = preparar, conduzir, comunicar, manter;; 2 = três;; 1 = uma;; 0 = nenhuma.

- **EX072 — Quem decide.** Quem decide se um risco é aceito? *Rubrica:* 3 = o responsável do negócio com autoridade, não o engenheiro;; 2 = responsável;; 1 = engenheiro;; 0 = nenhuma.

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto I

### Objetivos de aprendizagem

Você vai (1) desenvolver um projeto de arquitetura num formato de ateliê; (2) apresentar e defender escolhas de projeto; (3) incorporar críticas nas revisões.

### 25.1 O briefing do ateliê

No Ateliê de Projeto I, a equipe de quatro pessoas de Sofia recebe um briefing: projetar a arquitetura segura do novo sistema de gestão de recarga das garagens da Corvia, que programa a recarga dos ônibus elétricos e se conecta ao portal do fornecedor de energia. Eles têm quatro semanas. Começam pelo contexto, pelas partes interessadas e pelas necessidades de proteção, e depois desenham um modelo de componentes e os fluxos de dados. O formato de ateliê espelha a prática profissional: os projetos são desenvolvidos de forma iterativa, revisados por colegas e praticantes e revisados de novo. Daniel faz o papel de cliente, respondendo a perguntas sobre as restrições e recusando-se a tomar decisões de projeto por eles.

### 25.2 Apresentar as escolhas

Na revisão intermediária, a equipe apresenta três opções: controle da recarga na nuvem, com comandos remotos para as garagens; controle em cada garagem, com a nuvem apenas para relatórios; e um modelo híbrido. Eles defendem o controle local na garagem porque os ônibus precisam recarregar mesmo quando o enlace de internet falha, com programações assinadas vindas da nuvem e regras locais de contingência. Um revisor questiona como eles vão impedir que um controlador de garagem comprometido danifique os carregadores. Eles ainda não têm resposta e dizem isso com honestidade, registrando a pergunta como uma questão em aberto, em vez de inventar uma resposta sob pressão.

### 25.3 Revisar a partir da crítica

Na semana seguinte, a equipe pesquisa a questão em aberto na documentação do fornecedor dos carregadores e com os engenheiros de segurança física. Acrescentam limites de hardware nos carregadores que o controlador não consegue sobrepor, separam a rede do controlador dos sistemas corporativos e exigem aprovação de duas pessoas para mudanças nas regras de contingência. Na revisão final, mostram como cada mudança responde à crítica e que risco permanece. Sofia aprende que um ateliê de projeto recompensa a incerteza honesta seguida de pesquisa, e que a crítica é mais útil quando registrada e respondida explicitamente na versão seguinte.

### Exemplo resolvido

A equipe de Sofia compara três opções de controle da recarga, escolhe o controle local na garagem com programações assinadas, registra uma questão em aberto sobre controladores comprometidos e a responde com limites de hardware e segmentação.

> **Caso sintético.** O sistema de recarga, o fornecedor e as revisões são sintéticos.

### Erros e limites

Os projetos de ateliê não têm o detalhamento de produção; restrições reais podem mudar as escolhas. Os limites de hardware dependem da qualidade da implementação do fornecedor.

### Exercícios

- **EX073 — Motivo do controle local.** Por que a equipe escolheu o controle de recarga local na garagem? *Rubrica:* 3 = os ônibus precisam recarregar mesmo quando os enlaces de internet falham;; 2 = resiliência;; 1 = custo;; 0 = nenhuma.

- **EX074 — Questionamento sem resposta.** Como a equipe lidou com o questionamento que não sabia responder? *Rubrica:* 3 = disse isso com honestidade e o registrou como questão em aberto;; 2 = questão em aberto;; 1 = inventou uma resposta;; 0 = nenhuma.

- **EX075 — Mitigações finais.** Cite duas mitigações acrescentadas depois da crítica. *Rubrica:* 3 = limites de hardware não sobreponíveis nos carregadores, separação de rede, aprovação de duas pessoas para as regras de contingência (duas);; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-26"></a>

## Capítulo 26 — Arquitetura e engenharia de segurança: alternativas de arquitetura

### Objetivos de aprendizagem

Você vai (1) gerar alternativas de arquitetura para o back-office; (2) avaliá-las contra critérios ponderados; (3) documentar por que a opção escolhida venceu.

### 26.1 Gerar alternativas

Para o back-office de bilhetagem, Sofia gera três alternativas. A alternativa A mantém um único cluster on-premises com segmentação melhorada. A alternativa B leva o processamento para um provedor de nuvem com serviços gerenciados de chaves. A alternativa C divide o sistema: a ingestão das validações e o cálculo das tarifas ficam on-premises, enquanto os relatórios e as análises vão para a nuvem apenas com dados pseudonimizados. Daniel insiste em pelo menos três opções, porque comparar só duas muitas vezes esconde um caminho intermediário melhor, e uma opção de mudança mínima fornece uma base contra a qual o valor da mudança pode ser julgado.

### 26.2 Avaliação ponderada

Sofia e as partes interessadas acordam os critérios e os pesos: segurança dos dados pessoais, resiliência durante indisponibilidades, custo em cinco anos, risco de migração e compatibilidade com os validadores legados. Cada alternativa é pontuada por três pessoas de forma independente, e as pontuações são discutidas onde divergem. A alternativa C tem a maior pontuação geral, principalmente porque mantém os dados pessoais on-premises e ao mesmo tempo ganha a escalabilidade da nuvem para as análises. Sofia registra o quanto o resultado é sensível: se o peso do custo dobrar, A vence. A sensibilidade mostra às partes interessadas quais premissas orientam a decisão, convidando ao debate sobre elas, e não sobre o número final.

### 26.3 Documentar a escolha

Sofia escreve um registro de decisão de arquitetura para a alternativa C, listando as opções, os critérios, os pesos, as pontuações, os resultados da sensibilidade e as consequências, inclusive novos riscos, como o processo de pseudonimização se tornar um ponto único de falha para a privacidade. O registro também declara as condições em que a decisão deve ser revista, como uma mudança nos preços da nuvem ou nas orientações regulatórias. Daniel explica que decisões documentadas assim podem ser auditadas e revistas com calma, enquanto decisões não documentadas são reabertas repetidamente sempre que chega um novo gestor com outra preferência.

### Exemplo resolvido

Sofia gera três alternativas para o back-office, pontua-as em cinco critérios ponderados com análise de sensibilidade e registra a alternativa C com seus novos riscos e condições de revisão.

> **Caso sintético.** As alternativas, os pesos e as pontuações são sintéticos.

### Erros e limites

A pontuação ponderada pode esconder divergências por trás das médias. Dados pseudonimizados podem ser reidentificáveis quando combinados com outros dados.

### Exercícios

- **EX076 — Três opções.** Por que Daniel insiste em pelo menos três alternativas? *Rubrica:* 3 = duas opções escondem caminhos intermediários; uma opção mínima dá uma base;; 2 = caminho intermediário;; 1 = sem motivo;; 0 = nenhuma.

- **EX077 — Resultado da sensibilidade.** O que acontece com a decisão se o peso do custo dobrar? *Rubrica:* 3 = a alternativa A vence no lugar da C;; 2 = A vence;; 1 = C continua;; 0 = nenhuma.

- **EX078 — Novo risco.** Que novo risco a alternativa C introduz? *Rubrica:* 3 = o processo de pseudonimização vira um ponto único de falha para a privacidade;; 2 = pseudonimização;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-27"></a>

## Capítulo 27 — Arquitetura e engenharia de segurança: projeto de controles

### Objetivos de aprendizagem

Você vai (1) projetar controles que atendam a requisitos específicos; (2) combinar em camadas controles preventivos, detectivos e corretivos; (3) especificar os controles com precisão suficiente para implementá-los e testá-los.

### 27.1 Projetar a partir dos requisitos

Sofia projeta controles para o requisito de que as tabelas de tarifas sejam autênticas antes do uso. O controle preventivo é uma assinatura digital: as tabelas de tarifas são assinadas no escritório de tarifas com uma chave guardada num HSM, e todo consumidor verifica a assinatura com uma chave pública fixada (pinned) antes de carregá-las. O controle detectivo registra cada carga com a versão e o hash da tabela e gera um alerta se aparecer uma versão que o escritório de tarifas não publicou. O controle corretivo permite que as operações voltem à última tabela verificada em minutos. Cada controle se liga ao requisito e ao caso de abuso que atende.

### 27.2 Defesa em profundidade com propósito

Combinar controles em camadas só é útil se as camadas falharem de forma independente. Sofia verifica seu projeto das tabelas de tarifas: se a chave de assinatura fosse roubada, as assinaturas seriam verificadas, então o controle detectivo compara as versões carregadas com uma lista de publicações independente mantida pelo financeiro. Se o código de verificação tivesse um bug, o controle detectivo ainda perceberia versões inesperadas. Se os dois falhassem, o rollback limitaria o dano. Ela observa que dois controles que dependem da mesma chave ou do mesmo banco de dados não oferecem profundidade real. Defesa em profundidade significa perguntar, para cada camada, o que acontece se a anterior falhar.

### 27.3 Especificações precisas

A especificação de um controle precisa dizer o suficiente para que ele seja implementado e testado. Sofia escreve: o algoritmo de assinatura é o Ed25519, conforme especificado na RFC 8032; a chave pública é fixada na configuração e só é rotacionada por meio da gestão de mudanças; uma falha na verificação interrompe a carga e gera um alerta de alta prioridade; os logs incluem o identificador da tabela, a versão, o hash e o componente que fez a verificação. Ela anexa casos de teste: uma tabela corretamente assinada é carregada; uma tabela modificada é rejeitada; uma tabela assinada com uma chave desconhecida é rejeitada. Especificações precisas impedem que cada implementador faça premissas diferentes que deixam lacunas entre os componentes.

### Exemplo resolvido

Sofia projeta tabelas de tarifas assinadas com uma chave guardada em HSM, verificações independentes de versão e rollback, testa a independência das camadas e escreve uma especificação com três casos de teste.

> **Caso sintético.** O projeto das tarifas é sintético; a RFC 8032 é real.

### Erros e limites

Chaves fixadas complicam a rotação de emergência. Os controles detectivos dependem de alguém responder aos alertas.

### Exercícios

- **EX079 — Três tipos de controle.** Cite os controles preventivo, detectivo e corretivo das tabelas de tarifas. *Rubrica:* 3 = verificação de assinatura; registro de versões e alertas; rollback;; 2 = três;; 1 = um;; 0 = nenhuma.

- **EX080 — Verificação de independência.** Por que comparar as versões carregadas com a lista independente do financeiro? *Rubrica:* 3 = ainda detecta o uso indevido se a chave de assinatura for roubada;; 2 = independente;; 1 = redundante;; 0 = nenhuma.

- **EX081 — Teste da especificação.** Dê um caso de teste da especificação. *Rubrica:* 3 = tabela corretamente assinada carrega, tabela modificada é rejeitada ou chave desconhecida é rejeitada;; 2 = um;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-28"></a>

## Capítulo 28 — Arquitetura e engenharia de segurança: implementação I

### Objetivos de aprendizagem

Você vai (1) traduzir a arquitetura em tarefas de implementação; (2) aplicar configuração segura e tratamento de segredos; (3) manter a implementação alinhada à arquitetura.

### 28.1 Da arquitetura às tarefas

A equipe de Sofia começa a implementar o componente de ingestão do back-office. Ela divide a arquitetura em tarefas: autenticação de dispositivos baseada em certificados, validação do esquema dos registros, detecção de replay com um repositório dos identificadores de registros recentes, verificação dos registros assinados e logging estruturado. Cada tarefa referencia o requisito e a especificação de controle que implementa e inclui testes de aceitação. Isso evita a deriva comum em que os desenvolvedores implementam o que é fácil e os controles mais difíceis da arquitetura são adiados em silêncio. As referências das tarefas também permitem que os revisores verifiquem a cobertura: todo requisito deve corresponder a pelo menos uma tarefa concluída.

### 28.2 Configuração e segredos

O serviço de ingestão precisa de uma chave privada para seu certificado de servidor TLS e de credenciais para seu banco de dados. Sofia garante que nenhum dos dois seja armazenado no código-fonte ou em imagens de contêiner. Os segredos vêm de um repositório gerenciado de segredos em tempo de execução, legível apenas pela identidade do serviço, e são rotacionados num calendário. A configuração fica sob controle de versão e é revisada, com as configurações relevantes para a segurança, como as versões de TLS e os emissores de certificado permitidos, verificadas automaticamente contra a especificação. Ela encontra uma credencial de teste commitada num branch antigo, remove-a do histórico e providencia sua rotação, registrando o incidente.

### 28.3 Manter o alinhamento

Durante a implementação, a equipe descobre que a detecção de replay precisa de mais memória do que o esperado no pico de carga. Um desenvolvedor propõe pulá-la durante os picos. Sofia leva isso como uma mudança de arquitetura, e não como uma decisão de codificação, porque enfraquece um requisito. Em vez disso, a equipe usa um repositório com limite de tempo, indexado pelo identificador do registro e pelo validador, que cabe nos limites de memória. Ela atualiza o registro de arquitetura e a especificação. Daniel ressalta que a implementação sempre ensina alguma coisa; a disciplina está em levar esse aprendizado de volta à arquitetura, em vez de deixar o sistema construído divergir em silêncio.

### Exemplo resolvido

Sofia relaciona os requisitos da ingestão a cinco tarefas de implementação, leva os segredos para um repositório gerenciado, trata uma credencial de teste commitada e encaminha uma mudança na detecção de replay pela revisão de arquitetura.

> **Caso sintético.** O componente de ingestão e o incidente são sintéticos.

### Erros e limites

Os repositórios de segredos se tornam dependências críticas que precisam de alta disponibilidade. Remover segredos do histórico não desfaz a exposição; a rotação continua necessária.

### Exercícios

- **EX082 — Referências das tarefas.** Por que cada tarefa referencia um requisito? *Rubrica:* 3 = evita adiar os controles difíceis e permite que os revisores verifiquem a cobertura;; 2 = cobertura;; 1 = nenhuma;; 0 = nenhuma.

- **EX083 — Credencial commitada.** Que passos se seguiram à descoberta de uma credencial de teste commitada? *Rubrica:* 3 = removida do histórico e rotacionada, com o incidente registrado;; 2 = as duas;; 1 = só removida;; 0 = nenhuma.

- **EX084 — Encaminhamento da mudança de replay.** Por que pular a detecção de replay foi tratado como uma mudança de arquitetura? *Rubrica:* 3 = enfraquece um requisito, então precisa de revisão de arquitetura;; 2 = requisito;; 1 = escolha de codificação;; 0 = nenhuma.

<a id="ch-29"></a>

## Capítulo 29 — Arquitetura e engenharia de segurança: medição

### Objetivos de aprendizagem

Você vai (1) definir métricas de segurança ligadas aos objetivos da arquitetura; (2) calcular métricas de cobertura e de tempestividade a partir de dados sintéticos; (3) evitar métricas que recompensem o comportamento errado.

### 29.1 Métricas ligadas a objetivos

Daniel pede que Sofia proponha métricas para a arquitetura do back-office. Ela parte dos objetivos: tabelas de tarifas autênticas, revogação tempestiva dos dispositivos desativados, dados pessoais protegidos e recuperação rápida. Para cada um, define uma ou duas métricas: porcentagem de cargas de tarifas com assinatura verificada; mediana de dias entre a desativação do dispositivo e a revogação do certificado; porcentagem de repositórios de dados pessoais com criptografia e registro de acesso ativados; e tempo para restaurar a ingestão nos testes de recuperação. Cada métrica tem definição, fonte de dados, meta e responsável. Métricas sem objetivos tendem a medir o que é fácil, e não o que importa.

### 29.2 Calcular as métricas

Sofia escreve um script que lê registros sintéticos de desativações e revogações de dispositivos e de configurações dos repositórios de dados, e calcula as métricas. O laboratório abaixo mostra que a tempestividade da revogação é ruim, com uma cauda longa de dispositivos revogados semanas depois da desativação e alguns nunca revogados, enquanto a cobertura de criptografia é alta. Ela apresenta as contagens e os denominadores junto com as porcentagens. Os números priorizam o trabalho imediatamente: é o processo de revogação, e não a criptografia, que precisa de atenção. A medição transforma a ameaça encontrada no capítulo 23 numa melhoria acompanhada, com uma linha de base.

### Laboratório — Tempestividade da revogação e cobertura

```python
# Synthetic device retirement/revocation records and data-store configs.
import statistics
delays = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 12, 15, 21, 28, 35, 44, None, None, None]   # None = never revoked
done = [d for d in delays if d is not None]
print(f"retired devices: {len(delays)}, revoked: {len(done)}, never revoked: {delays.count(None)}")
print(f"median days to revoke (revoked only): {statistics.median(done)}")
print(f"revoked within 7 days: {sum(d <= 7 for d in done)}/{len(delays)}")
stores = {"journeys": (True, True), "refunds": (True, True), "staff": (True, False), "reports": (True, True), "archive": (True, True)}
cov = sum(e and l for e, l in stores.values())
print(f"personal-data stores encrypted+logged: {cov}/{len(stores)}")
```

Execute com `python3 lab_metrics.py`. Saída verificada:

```text
retired devices: 20, revoked: 17, never revoked: 3
median days to revoke (revoked only): 8
revoked within 7 days: 8/20
personal-data stores encrypted+logged: 4/5
```

### 29.3 Métricas que enganam

As métricas moldam o comportamento. Se a equipe é recompensada por fechar rapidamente os tickets de vulnerabilidade, pode fechá-los sem verificação. Se a métrica é o número de controles implementados, pode implementar controles fáceis em vez de importantes. Sofia propõe métricas em pares: velocidade de fechamento com taxa de reabertura; contagem de controles com cobertura dos riscos de alta prioridade. Ela também alerta contra relatar uma métrica sem seu denominador ou sua tendência. Anderson (2020) discute como as métricas de segurança podem ser manipuladas. Boas métricas são poucas, ligadas aos objetivos e revistas para ver se ainda induzem o comportamento pretendido.

### Exemplo resolvido

Sofia define cinco métricas ligadas a objetivos, calcula a tempestividade da revogação e a cobertura de criptografia a partir de dados sintéticos e combina métricas em pares para resistir à manipulação.

> **Caso sintético.** Os dados das métricas são sintéticos; Anderson (2020) é real.

### Erros e limites

As métricas medem indicadores indiretos, não a segurança em si. Denominadores pequenos tornam as porcentagens instáveis.

### Exercícios

- **EX085 — Métrica ligada a objetivo.** Dê uma métrica para o objetivo de revogação tempestiva dos dispositivos desativados. *Rubrica:* 3 = mediana de dias entre a desativação e a revogação;; 2 = métrica;; 1 = contagem de dispositivos;; 0 = nenhuma.

- **EX086 — Resultado da revogação no laboratório.** O que o laboratório mostrou sobre a tempestividade da revogação? *Rubrica:* 3 = mediana de 8 dias entre os revogados, 3 de 20 nunca revogados, só 8 de 20 em até uma semana;; 2 = os dois;; 1 = boa;; 0 = nenhuma.

- **EX087 — Métrica em par.** Que métrica deve acompanhar a velocidade de fechamento de tickets? *Rubrica:* 3 = a taxa de reabertura;; 2 = reabertura;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-30"></a>

## Capítulo 30 — Laboratório de verificação I

### Objetivos de aprendizagem

Você vai (1) verificar se os controles implementados atendem às suas especificações; (2) rodar casos de teste positivos e negativos de autenticidade dos registros e de replay; (3) registrar as evidências de verificação.

### 30.1 Propósito da verificação

A verificação pergunta se o sistema foi construído conforme especificado. No Laboratório de Verificação I, Sofia testa os controles de autenticidade e de replay do componente de ingestão num laboratório isolado, com validadores sintéticos. Seu plano de testes vem diretamente das especificações dos controles: cada requisito tem testes positivos, que mostram o comportamento correto, e testes negativos, que mostram que entradas ruins são rejeitadas. O ambiente do laboratório usa apenas chaves e dados sintéticos. As evidências de verificação sustentarão o assurance case mais adiante, então cada teste registra as entradas, os resultados esperados, os resultados obtidos, a versão do ambiente e a data, num formato consistente.

### 30.2 Testes de autenticidade e de replay

No laboratório, os validadores autenticam os registros de validação com um código de autenticação de mensagem (MAC), usando uma chave compartilhada com a ingestão, um substituto simplificado das assinaturas de produção, implementado com o módulo hmac do Python. O script de Sofia envia quatro registros sintéticos: um registro novo e autêntico, uma duplicata dele, um registro com o valor alterado e um registro de um validador desativado cuja chave foi removida. O laboratório abaixo mostra a ingestão aceitando apenas o primeiro. Ela compara os resultados com os desfechos esperados e constata que os quatro coincidem. Uma divergência seria um defeito a ser relatado, e não um teste a ser ajustado.

### Laboratório — Verificação de autenticidade e de replay

```python
# Lab ingestion check: HMAC stand-in for validator signatures + replay store. Synthetic keys only.
import hmac, hashlib
keys = {"V-101": b"lab-key-101", "V-102": b"lab-key-102"}       # V-099 retired: key removed
seen = set()
def tag(k, rec): return hmac.new(k, rec, hashlib.sha256).hexdigest()
def ingest(vid, rec, t):
    k = keys.get(vid)
    if k is None: return "reject: unknown or retired validator"
    if not hmac.compare_digest(tag(k, rec), t): return "reject: bad tag"
    rid = rec.split(b",")[0]
    if (vid, rid) in seen: return "reject: replay"
    seen.add((vid, rid)); return "accept"
r = b"R-5521,C100,2.40"
t = tag(keys["V-101"], r)
print("authentic:", ingest("V-101", r, t))
print("duplicate:", ingest("V-101", r, t))
print("altered amount:", ingest("V-101", b"R-5522,C100,0.10", tag(keys["V-101"], b"R-5522,C100,2.40")))
print("retired validator:", ingest("V-099", b"R-7,C200,2.40", tag(b"old-099", b"R-7,C200,2.40")))
```

Execute com `python3 lab_ingest.py`. Saída verificada:

```text
authentic: accept
duplicate: reject: replay
altered amount: reject: bad tag
retired validator: reject: unknown or retired validator
```

### 30.3 Registrar as evidências

Sofia escreve um relatório de verificação com uma tabela de testes, resultados e links para as evidências, e anota o que não foi verificado: o desempenho sob a carga de pico, o comportamento durante o failover do banco de dados e o caminho das assinaturas de produção, que usa outro mecanismo. Ela assina e data o relatório e o guarda com um hash no repositório de evidências do projeto. Daniel lembra que a verificação mostra a conformidade com a especificação; se a própria especificação é adequada é uma questão separada, tratada pela validação, que vem mais adiante no curso.

### Exemplo resolvido

Sofia roda quatro testes de autenticidade e de replay num laboratório isolado, constata que todos coincidem com o esperado e registra um relatório que lista três áreas ainda não verificadas.

> **Caso sintético.** O laboratório, as chaves e os registros são sintéticos; o HMAC substitui as assinaturas de produção.

### Erros e limites

Os ambientes de laboratório diferem da produção em escala e em tempo. Testes aprovados dependem da qualidade dos casos de teste.

### Exercícios

- **EX088 — Pergunta da verificação.** Que pergunta a verificação responde? *Rubrica:* 3 = o sistema foi construído conforme especificado;; 2 = conforme especificado;; 1 = é útil;; 0 = nenhuma.

- **EX089 — Resultados do laboratório.** Quais dos quatro registros do laboratório foram aceitos? *Rubrica:* 3 = só o registro novo e autêntico; duplicado, alterado e desativado rejeitados;; 2 = só o primeiro;; 1 = vários;; 0 = nenhuma.

- **EX090 — Não verificado.** Cite uma área que o relatório de Sofia lista como não verificada. *Rubrica:* 3 = carga de pico, failover do banco de dados ou caminho das assinaturas de produção;; 2 = uma;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-31"></a>

## Capítulo 31 — Arquitetura e engenharia de segurança: implementação II

### Objetivos de aprendizagem

Você vai (1) implementar a automação do ciclo de vida dos certificados de dispositivos; (2) integrar a revogação à gestão de ativos; (3) lidar com componentes legados que não conseguem atender ao projeto-alvo.

### 31.1 Automatizar os certificados de dispositivos

As métricas do capítulo 29 mostraram uma revogação lenta dos validadores desativados. Em Implementação II, a equipe de Sofia automatiza o ciclo de vida dos certificados de dispositivos. Os novos validadores recebem certificados por meio de um processo de enrolment que exige um registro de ativo e um ticket de instalação aprovado. Os certificados têm validade curta e são renovados automaticamente enquanto o dispositivo está em serviço. O projeto segue as fases de gestão de chaves do SP 800-57 Part 1 Rev. 5. A automação reduz tanto o trabalho manual que causava atrasos quanto a chance de erro humano, mas também concentra a confiança no serviço de enrolment, que precisa ele próprio ser protegido e monitorado.

### 31.2 Ligação com a gestão de ativos

Agora a revogação é disparada pelo sistema de gestão de ativos: quando um validador é marcado como desativado, perdido ou roubado, um evento chama a autoridade interna para revogar seu certificado e o acrescenta à lista de bloqueio da ingestão. Sofia escreve testes de integração para cada mudança de status. Ela também acrescenta uma conciliação diária que compara os certificados ativos com os ativos em serviço e gera alertas sobre divergências. A integração entre sistemas é onde muitos processos de segurança falham, porque cada equipe supõe que outra cuida da etapa, então a conciliação funciona como uma rede de segurança para eventos perdidos.

### 31.3 Exceções legadas

Cerca de cem validadores mais antigos não suportam a renovação automática. Sofia não finge que eles atendem ao projeto. Ela os documenta como exceções com controles compensatórios: certificados de vida mais longa guardados nos seus secure elements, regras de ingestão que limitam suas taxas de registros aceitos, verificações manuais trimestrais e uma data de substituição no quinto ano. Cada exceção tem um responsável e uma data de expiração. Daniel explica que uma gestão honesta de exceções é sinal de uma arquitetura madura; projetos que alegam conformidade total enquanto escondem lacunas legadas deixam a organização exposta a riscos que ninguém está acompanhando.

### Exemplo resolvido

A equipe de Sofia automatiza o enrolment e a renovação dos validadores, dispara a revogação a partir das mudanças de status dos ativos com conciliação diária e documenta cem validadores legados como exceções com responsável e expiração.

> **Caso sintético.** Os dispositivos, os sistemas e as contagens são sintéticos; o SP 800-57 Part 1 Rev. 5 é real.

### Erros e limites

O enrolment automatizado se torna um alvo de alto valor. A conciliação depende de os registros de ativos estarem corretos.

### Exercícios

- **EX091 — Condição de enrolment.** O que precisa existir antes que um validador receba um certificado? *Rubrica:* 3 = um registro de ativo e um ticket de instalação aprovado;; 2 = os dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX092 — Propósito da conciliação.** O que a conciliação diária capta? *Rubrica:* 3 = divergências entre certificados ativos e ativos em serviço causadas por eventos perdidos;; 2 = divergências;; 1 = nada;; 0 = nenhuma.

- **EX093 — Conteúdo da exceção.** O que cada exceção legada inclui? *Rubrica:* 3 = controles compensatórios, responsável e data de expiração ou substituição;; 2 = três;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-32"></a>

## Capítulo 32 — Arquitetura e engenharia de segurança: confiabilidade

### Objetivos de aprendizagem

Você vai (1) calcular a disponibilidade de componentes em série e em paralelo; (2) projetar redundância para serviços de segurança; (3) reconhecer quando controles de segurança reduzem a confiabilidade.

### 32.1 Série e paralelo

A engenharia de confiabilidade oferece regras simples. Componentes em série, todos necessários para o serviço, multiplicam suas disponibilidades, de modo que o todo é menos disponível do que qualquer parte. Componentes em paralelo, em que qualquer um basta, se combinam de modo que o todo é mais disponível do que cada um. Sofia aplica isso à ingestão, que precisa em série do balanceador de carga, do serviço de ingestão, do repositório de segredos e do banco de dados. O laboratório abaixo calcula a disponibilidade geral com números sintéticos e mostra como acrescentar uma segunda instância do repositório de segredos em paralelo muda o resultado. Serviços de segurança como os repositórios de segredos costumam ser esquecidos quando a disponibilidade é planejada.

### Laboratório — Disponibilidade em série e em paralelo

```python
# Series/parallel availability with synthetic component figures.
comp = {"load balancer": 0.9995, "ingestion": 0.999, "secret store": 0.998, "database": 0.9995}
def series(xs):
    p = 1.0
    for x in xs: p *= x
    return p
def parallel(a, n): return 1 - (1 - a) ** n
base = series(comp.values())
red = series([comp["load balancer"], comp["ingestion"], parallel(comp["secret store"], 2), comp["database"]])
print(f"single secret store: {base:.4f}  (~{(1-base)*8760:.0f} h/yr down)")
print(f"two secret stores:   {red:.4f}  (~{(1-red)*8760:.0f} h/yr down)")
```

Execute com `python3 lab_avail.py`. Saída verificada:

```text
single secret store: 0.9960  (~35 h/yr down)
two secret stores:   0.9980  (~18 h/yr down)
```

### 32.2 Redundância para serviços de segurança

Autenticação, gestão de chaves e logging são dependências de quase tudo. Se o provedor de identidade falha, a equipe não consegue fazer login; se o repositório de segredos falha, os serviços não conseguem iniciar; se o logging falha, os ataques passam despercebidos. Sofia propõe redundância para cada um: provedores de identidade em cluster em dois sites, repositórios de segredos replicados e buffer local de logs quando o coletor central estiver inacessível. Ela também documenta o que acontece no modo degradado, como os validadores seguirem com listas de bloqueio em cache. Projetar deliberadamente o comportamento degradado é mais seguro do que descobri-lo durante uma indisponibilidade.

### 32.3 Quando a segurança prejudica a confiabilidade

Alguns controles reduzem a disponibilidade. Uma validação estrita de certificados falha fechada se o serviço de revogação estiver inacessível; um rate limiting agressivo pode bloquear picos legítimos; a autenticação multifator obrigatória falha se o serviço do segundo fator estiver fora do ar. Sofia lista esses casos e decide cada um deliberadamente: a ingestão das validações faz soft-fail nas verificações de revogação por um curto período, usando listas em cache, enquanto o acesso administrativo faz hard-fail. A decisão decorre do ativo e da ameaça: a arrecadação precisa continuar, enquanto o acesso administrativo pode esperar. Confiabilidade e segurança são propriedades do mesmo sistema e precisam ser negociadas explicitamente.

### Exemplo resolvido

Sofia calcula a disponibilidade da ingestão com e sem um repositório de segredos redundante, projeta redundância para três serviços de segurança e registra as decisões de falhar aberto e falhar fechado.

> **Caso sintético.** Os números de disponibilidade são sintéticos.

### Erros e limites

As premissas de independência superestimam os benefícios do paralelo quando as réplicas compartilham uma causa de falha. As janelas de soft-fail podem ser abusadas.

### Exercícios

- **EX094 — Regra da série.** Como as disponibilidades se combinam em série? *Rubrica:* 3 = multiplicam-se; o todo é menos disponível do que qualquer parte;; 2 = multiplicar;; 1 = somar;; 0 = nenhuma.

- **EX095 — Efeito da redundância no laboratório.** O que o laboratório mostrou quando o repositório de segredos foi duplicado? *Rubrica:* 3 = a disponibilidade subiu de 0.9960 para 0.9980, reduzindo à metade a indisponibilidade, de cerca de 35 para 18 horas por ano;; 2 = subiu;; 1 = caiu;; 0 = nenhuma.

- **EX096 — Decisão de falha.** Que caminho faz soft-fail nas verificações de revogação, e qual faz hard-fail? *Rubrica:* 3 = a ingestão das validações faz soft-fail por pouco tempo; o acesso administrativo faz hard-fail;; 2 = os dois;; 1 = invertido;; 0 = nenhuma.

<a id="ch-33"></a>

## Capítulo 33 — Arquitetura e engenharia de segurança: segurança e resiliência

### Objetivos de aprendizagem

Você vai (1) distinguir os objetivos de segurança da informação, segurança física e resiliência; (2) aplicar técnicas de resiliência das orientações de engenharia de sistemas; (3) projetar a degradação controlada sob ataque.

### 33.1 Três objetivos relacionados

A segurança da informação protege contra danos intencionais, a segurança física (safety) protege as pessoas de danos físicos, qualquer que seja a causa, e a resiliência é a capacidade de antecipar, resistir, recuperar-se e adaptar-se a condições adversas. Nos sistemas de transporte, elas se sobrepõem. Um ataque de ransomware ao centro de operações é um evento de segurança da informação que pode virar uma questão de segurança física se a informação aos passageiros falhar durante interrupções. Sofia aprende que as três comunidades usam métodos e vocabulários diferentes, e que os arquitetos precisam aproximá-las, por exemplo convidando engenheiros de segurança física para as sessões de modelagem de ameaças de sistemas que afetam passageiros ou veículos.

### 33.2 Técnicas de resiliência

O NIST SP 800-160 Vol. 1 Rev. 1 liga a resiliência à engenharia de sistemas confiáveis, e o SP 800-160 Vol. 2 Rev. 1 descreve técnicas de ciber-resiliência como redundância, diversidade, segmentação, resposta adaptativa e não persistência, cada uma com orientações sobre quando ajuda. Sofia aplica várias delas ao centro de operações da Corvia: segmentação para conter a propagação, backups offline para a recuperação, um canal de comunicação de reserva diverso para os motoristas e procedimentos operacionais manuais planejados de antemão. Ela escreve cada técnica ao lado da condição adversa que ela trata. O planejamento de resiliência supõe que a prevenção às vezes vai falhar e pergunta como a missão continua mesmo assim, e quais pessoas precisam agir quando isso acontecer.

### 33.3 Degradação controlada

Sofia projeta níveis de degradação para o sistema de bilhetagem. Nível um: back-office central indisponível, os validadores continuam offline com tarifas e listas de bloqueio em cache. Nível dois: validadores indisponíveis, os fiscais aceitam comprovação visual e a cobrança é suspensa. Nível três: centro de operações comprometido, os serviços rodam com horários manuais e comunicação por rádio. Cada nível tem um gatilho, um tomador de decisão e um procedimento de retorno. Ensaiar esses níveis mostra à equipe que um incidente cibernético não precisa parar os bondes, o que reduz a pressão para pagar resgates ou apressar restaurações inseguras.

### Exemplo resolvido

Sofia separa os objetivos de segurança da informação, segurança física e resiliência, relaciona quatro técnicas de resiliência a condições adversas e define três níveis de degradação com gatilhos e responsáveis.

> **Caso sintético.** Os níveis de degradação e os procedimentos são sintéticos; o SP 800-160 Vol. 1 Rev. 1 e o Vol. 2 Rev. 1 são reais.

### Erros e limites

Procedimentos manuais se deterioram sem prática. A própria degradação pode criar oportunidades de fraude que precisam ser monitoradas.

### Exercícios

- **EX097 — Definição de resiliência.** Defina resiliência nos termos deste capítulo. *Rubrica:* 3 = capacidade de antecipar, resistir, recuperar-se e adaptar-se a condições adversas;; 2 = três partes;; 1 = só segurança;; 0 = nenhuma.

- **EX098 — Canal diverso.** Que técnica de resiliência um canal de comunicação de reserva para os motoristas representa? *Rubrica:* 3 = diversidade ou redundância da comunicação;; 2 = diversidade;; 1 = segmentação;; 0 = nenhuma.

- **EX099 — Pressão do resgate.** Como níveis de degradação ensaiados reduzem a pressão para pagar resgates? *Rubrica:* 3 = a equipe sabe que os serviços podem continuar manualmente, então há menos urgência para pagar;; 2 = continuidade;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-34"></a>

## Capítulo 34 — Arquitetura e engenharia de segurança: integração

### Objetivos de aprendizagem

Você vai (1) proteger integrações com parceiros externos; (2) projetar a autenticação e a autorização de APIs para o acesso de parceiros; (3) gerenciar a responsabilidade compartilhada nas fronteiras de integração.

### 34.1 Integrações com parceiros

A Corvia se integra a um provedor de pagamentos, a um aplicativo regional de mobilidade que vende passagens da Corvia, ao fornecedor de energia e a uma consultoria de análise de dados. Cada integração atravessa uma fronteira de confiança e traz obrigações contratuais e técnicas. Sofia lista para cada uma os dados trocados, a direção, o método de autenticação e a parte responsável por cada controle. Ela descobre que o aplicativo de mobilidade usa uma única API key de longa duração compartilhada por todos os seus servidores, enquanto a consultoria recebe exportações mensais de dados por e-mail. As duas são fraquezas de integração que a arquitetura deve tratar.

### 34.2 Projeto de APIs para parceiros

Sofia propõe um API gateway para parceiros. Os parceiros se autenticam com tokens de curta duração obtidos com client credentials vinculadas a certificados, em vez de chaves estáticas. Cada token carrega escopos que limitam o que o parceiro pode fazer: o aplicativo de mobilidade pode vender passagens e consultar tarifas, mas não ler históricos de viagem. O gateway aplica rate limits, valida os esquemas e registra cada requisição com a identidade do parceiro. As exportações de dados para a consultoria passam para um serviço de transferência segura, com dados pseudonimizados e expiração do acesso. Essas escolhas aplicam o menor privilégio e a mediação completa na fronteira.

### 34.3 Responsabilidade compartilhada

Em toda integração, alguns controles pertencem à Corvia e outros ao parceiro. Sofia escreve uma matriz de responsabilidades: a Corvia protege o gateway e valida as requisições; o parceiro protege suas credenciais e seus próprios usuários; ambos devem comunicar incidentes dentro de prazos acordados. A matriz é anexada aos contratos. Quando o aplicativo de mobilidade mais tarde sofre um vazamento das contas dos seus próprios clientes, a matriz deixa claro qual parte notifica quais passageiros e quais tokens a Corvia revoga. A clareza sobre as responsabilidades evita lacunas em que cada parte supõe que a outra cuida de um controle.

### Exemplo resolvido

Sofia inventaria quatro integrações com parceiros, substitui uma API key estática compartilhada por tokens de curta duração, com escopo e vinculados a certificados, e escreve uma matriz de responsabilidades usada durante um vazamento de um parceiro.

> **Caso sintético.** Os parceiros, as integrações e o vazamento são sintéticos.

### Erros e limites

Os gateways se tornam pontos únicos de falha e precisam ser resilientes. Os contratos não conseguem obrigar os parceiros a proteger os próprios sistemas.

### Exercícios

- **EX100 — Duas fraquezas.** Que duas fraquezas de integração Sofia encontrou? *Rubrica:* 3 = API key compartilhada e de longa duração do aplicativo de mobilidade; exportações da consultoria por e-mail;; 2 = as duas;; 1 = uma;; 0 = nenhuma.

- **EX101 — Exemplo de escopo.** O que os tokens do aplicativo de mobilidade podem permitir, e o que não? *Rubrica:* 3 = vender passagens e consultar tarifas, não ler históricos de viagem;; 2 = as duas partes;; 1 = acesso total;; 0 = nenhuma.

- **EX102 — Matriz no vazamento.** Como a matriz de responsabilidades ajudou durante o vazamento do parceiro? *Rubrica:* 3 = esclareceu quem notifica os passageiros e quais tokens a Corvia revoga;; 2 = clareza;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-35"></a>

## Capítulo 35 — Ateliê de projeto II

### Objetivos de aprendizagem

Você vai (1) liderar um projeto multidisciplinar de um sistema maior; (2) conciliar requisitos conflitantes das partes interessadas; (3) produzir um pacote de projeto adequado para revisão independente.

### 35.1 O briefing

O Ateliê de Projeto II é maior: Sofia lidera uma equipe de seis pessoas, incluindo dois estudantes de outras engenharias, para projetar a arquitetura de segurança da futura bilhetagem baseada em conta (account-based ticketing) da Corvia, em que os passageiros aproximam cartões bancários ou celulares e as tarifas são calculadas no back-office, em vez de armazenadas nos cartões. O briefing inclui requisitos de privacidade, pagamento, acessibilidade e operação. O papel de Sofia é coordenar, não decidir tudo. Ela cria um registro de decisões compartilhado, atribui uma área a cada membro da equipe e faz breves reuniões diárias para que os conflitos apareçam cedo.

### 35.2 Conciliar conflitos

Os requisitos colidem. Os analistas de fraude querem históricos de viagem detalhados guardados por dois anos; a responsável pela privacidade quer noventa dias; o atendimento ao cliente quer os históricos visíveis aos atendentes para as contestações; a responsável pela acessibilidade quer uma recuperação de conta simples para passageiros que perdem o celular, o que os analistas de fraude temem que permita o sequestro de contas. Sofia conduz uma sessão em que cada lado declara a necessidade subjacente. O resultado: dados detalhados por noventa dias, atributos agregados de fraude por dois anos, telas dos atendentes mostrando só as viagens contestadas e recuperação por meio de aproximações verificadas do cartão bancário, em vez de perguntas de segurança. Cada acordo é registrado com sua justificativa.

### 35.3 O pacote de projeto

O pacote final contém a declaração de contexto, os requisitos com métodos de verificação, os modelos de componentes e de fluxo de dados, o modelo de ameaças, a análise de alternativas, as especificações dos controles, os níveis de degradação, as questões em aberto e o registro de decisões. Sofia verifica que todo requisito se liga a controles e testes. O pacote vai para um revisor independente de outra universidade, que identifica duas lacunas: nenhum plano para o comprometimento de chaves no serviço de tokenização e um responsável pouco claro pelas solicitações de exclusão de dados dos passageiros. A equipe de Sofia acrescenta as duas coisas. Produzir um pacote que outras pessoas possam revisar é a entrega, mais do que qualquer diagrama isolado.

### Exemplo resolvido

Sofia lidera um ateliê de seis pessoas sobre a bilhetagem baseada em conta, concilia quatro requisitos conflitantes por meio das necessidades declaradas e monta um pacote revisável que fecha duas lacunas encontradas por um revisor externo.

> **Caso sintético.** O ateliê, a equipe e o revisor são sintéticos.

### Erros e limites

Os acordos do ateliê podem não sobreviver a negociações reais. A completude do pacote não garante a qualidade do projeto.

### Exercícios

- **EX103 — Papel da líder.** Qual é o principal papel de Sofia como líder do ateliê? *Rubrica:* 3 = coordenar, fazer os conflitos aparecerem e manter um registro de decisões, não decidir tudo;; 2 = coordenar;; 1 = decidir tudo;; 0 = nenhuma.

- **EX104 — Acordo de retenção.** A que acordo de retenção a equipe chegou? *Rubrica:* 3 = dados detalhados por 90 dias, atributos agregados de fraude por dois anos;; 2 = os dois;; 1 = um;; 0 = nenhuma.

- **EX105 — Lacunas do revisor.** Que duas lacunas o revisor independente encontrou? *Rubrica:* 3 = nenhum plano de comprometimento de chaves para a tokenização; responsável pouco claro pelas solicitações de exclusão;; 2 = as duas;; 1 = uma;; 0 = nenhuma.

<a id="ch-36"></a>

## Capítulo 36 — Arquitetura e engenharia de segurança: desempenho e escala

### Objetivos de aprendizagem

Você vai (1) analisar o custo de desempenho dos controles de segurança; (2) dimensionar o rate limiting com um token bucket; (3) projetar controles que escalem com a demanda.

### 36.1 O custo dos controles

Todo controle consome recursos. Os handshakes de TLS custam CPU; a verificação de assinaturas acrescenta latência a cada registro; o logging consome armazenamento e banda de rede; a inspeção profunda deixa o tráfego mais lento. Em pequena escala, esses custos são invisíveis, mas a bilhetagem baseada em conta vai processar milhões de validações por dia. Sofia mede o custo de cada controle num laboratório e estima os totais no pico. Ela descobre que a verificação de assinaturas é barata por registro, mas se acumula, enquanto um logging de debug verboso excederia os orçamentos de armazenamento em semanas. Medir os custos cedo evita pressões futuras para desligar controles quando o desempenho sofre.

### 36.2 Dimensionar o token bucket

O gateway de parceiros do capítulo 34 precisa limitar as taxas de requisição sem bloquear picos legítimos, como muitas compras de passagens antes de um show. Sofia modela um token bucket: os tokens são repostos a uma taxa constante, cada requisição consome um, e a capacidade do bucket permite rajadas curtas. O laboratório abaixo simula uma rajada sintética de requisições contra dois tamanhos de bucket com a mesma taxa de reposição. O bucket pequeno rejeita muitas requisições legítimas durante a rajada; o maior absorve quase toda ela e ainda limita o abuso prolongado. O dimensionamento vem do tráfego observado, e não de palpites.

### Laboratório — Tratamento de rajadas com token bucket

```python
# Token bucket vs synthetic burst: 20 req/s refill, burst of 300 requests over 5 s.
def run(capacity, refill=20.0, seconds=20):
    tokens, rejected = capacity, 0
    for t in range(seconds):
        tokens = min(capacity, tokens + refill)
        demand = 60 if 5 <= t < 10 else 10
        ok = min(demand, int(tokens)); tokens -= ok; rejected += demand - ok
    return rejected
for cap in (20, 200):
    print(f"capacity {cap:3d}: rejected {run(cap)} of {5*60 + 15*10} requests")
```

Execute com `python3 lab_bucket.py`. Saída verificada:

```text
capacity  20: rejected 200 of 450 requests
capacity 200: rejected 20 of 450 requests
```

### 36.3 Projetar para escala

Controles que funcionam para um servidor podem não escalar. Um serviço central de autorização chamado a cada validação vira um gargalo e um ponto único de falha. Sofia propõe guardar em cache as decisões de autorização com vida curta, distribuir a verificação aos nós de ingestão com chaves públicas compartilhadas e particionar os logs por tempo e região. Cada mudança mantém a propriedade de segurança e melhora a escala, e cada uma introduz uma nova consideração, como a rapidez com que as decisões em cache refletem as revogações. Ela documenta esses tradeoffs para que a equipe de operações entenda por que, por exemplo, um token de parceiro revogado pode funcionar por até um minuto.

### Exemplo resolvido

Sofia mede os custos dos controles, dimensiona um token bucket para as rajadas de shows e redesenha a autorização e o logging para escalar, documentando os atrasos de revogação ligados ao cache.

> **Caso sintético.** O tráfego, os custos e os parâmetros do bucket são sintéticos.

### Erros e limites

As medições de laboratório podem não refletir o hardware de produção. Os caches criam janelas em que direitos revogados ainda funcionam.

### Exercícios

- **EX106 — Custo oculto.** Que controle excederia os orçamentos de armazenamento em semanas? *Rubrica:* 3 = logging de debug verboso;; 2 = logging;; 1 = TLS;; 0 = nenhuma.

- **EX107 — Comparação dos buckets.** Como os dois tamanhos de bucket lidaram com a rajada sintética? *Rubrica:* 3 = capacidade 20 rejeitou 200 de 450; capacidade 200 rejeitou 20;; 2 = os dois;; 1 = iguais;; 0 = nenhuma.

- **EX108 — Tradeoff do cache.** Que tradeoff o cache das decisões de autorização introduz? *Rubrica:* 3 = direitos revogados podem continuar funcionando até o cache expirar;; 2 = atraso na revogação;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-37"></a>

## Capítulo 37 — Arquitetura e engenharia de segurança: operações

### Objetivos de aprendizagem

Você vai (1) projetar as operações de segurança para a nova arquitetura; (2) definir casos de uso de detecção a partir do modelo de ameaças; (3) planejar a aplicação de patches e a gestão de mudanças preservando as propriedades de segurança.

### 37.1 Operações desde o projeto

Uma arquitetura só é tão boa quanto sua operação. Sofia trabalha com o centro de operações da Corvia para planejar como o novo back-office será operado com segurança: quem monitora quais alertas, quem pode mudar configurações, como os incidentes são escalados e como os acessos são revisados. Ela usa o NIST CSF 2.0, cujas funções são govern, identify, protect, detect, respond e recover, para verificar se cada função tem responsáveis e procedimentos para o novo sistema. Planejar as operações durante o projeto evita construir sistemas que ninguém consegue monitorar ou manter adequadamente depois que a equipe do projeto sai.

### 37.2 Detecção a partir das ameaças

Sofia transforma as ameaças do capítulo 23 em casos de uso de detecção. Para registros de validação repetidos: alertar quando as rejeições por replay de um validador excederem um limiar. Para tabelas de tarifas maliciosas: alertar sobre qualquer versão não publicada. Para a exportação de dados de viagem por insiders: alertar quando as exportações excederem o volume normal ou ocorrerem fora do horário de trabalho. Cada caso de uso lista a fonte de dados, a lógica, os falsos positivos esperados e o playbook de resposta. Derivar a detecção do modelo de ameaças garante que o monitoramento se concentre no que importa para este sistema, e não em alertas genéricos copiados de modelos de fornecedores.

### 37.3 Patches e mudanças

As mudanças podem quebrar propriedades de segurança. Sofia define um processo de mudanças em que qualquer mudança que toque autenticação, criptografia, regras de rede ou logging precisa de revisão de segurança e de uma nova execução dos testes de verificação relevantes dos capítulos 30 e 40. Os patches de rotina seguem um calendário, com caminhos de emergência para vulnerabilidades críticas. Ela também exige que o modelo de arquitetura seja atualizado quando uma mudança alterar fluxos ou componentes. Daniel observa que a maioria das organizações não tem dificuldade em projetar sistemas seguros, e sim em mantê-los seguros ao longo de anos de pequenas mudanças bem-intencionadas.

### Exemplo resolvido

Sofia relaciona o back-office às funções do CSF 2.0, deriva três casos de uso de detecção do modelo de ameaças e define um processo de mudanças com nova verificação de segurança.

> **Caso sintético.** Os casos de uso e os processos são sintéticos; o NIST CSF 2.0 é real.

### Erros e limites

Os limiares de detecção precisam de ajuste depois do lançamento. Os processos de mudança podem virar gargalos se toda mudança exigir revisão completa.

### Exercícios

- **EX109 — Funções do CSF.** Liste as seis funções do CSF 2.0. *Rubrica:* 3 = govern, identify, protect, detect, respond, recover;; 2 = cinco;; 1 = três;; 0 = nenhuma.

- **EX110 — Detecção de exportação por insider.** Como a exportação de dados de viagem por um insider é detectada? *Rubrica:* 3 = alerta sobre volume de exportação incomum ou exportações fora do horário;; 2 = volume ou horário;; 1 = nenhuma;; 0 = nenhuma.

- **EX111 — Gatilho de revisão.** Que mudanças precisam de revisão de segurança e nova verificação? *Rubrica:* 3 = as que tocam autenticação, criptografia, regras de rede ou logging;; 2 = três;; 1 = todas as triviais;; 0 = nenhuma.

<a id="ch-38"></a>

## Capítulo 38 — Arquitetura e engenharia de segurança: validação

### Objetivos de aprendizagem

Você vai (1) distinguir validação de verificação; (2) validar a arquitetura contra as necessidades das partes interessadas e o uso real; (3) usar exercícios de red team e estudos com usuários como evidência de validação.

### 38.1 Construir o sistema certo

A verificação perguntou se o sistema foi construído conforme especificado; a validação pergunta se a especificação atende às necessidades reais. Um sistema perfeitamente verificado ainda pode falhar com seus usuários ou deixar passar ameaças reais. Sofia planeja a validação do back-office: revisar com as partes interessadas se as necessidades de privacidade são de fato atendidas na prática diária, observar os atendentes usando as telas de contestação e contratar um exercício de red team autorizado para testar se atacantes realistas conseguem atingir seus objetivos apesar dos controles. A validação muitas vezes encontra problemas nos próprios requisitos, que nenhuma quantidade de verificação revelaria.

### 38.2 Achados do red team

Um red team autorizado de uma empresa especializada, trabalhando sob regras de engajamento escritas que excluem dados reais de passageiros e veículos, tenta obter históricos de viagem. Eles não quebram nenhuma criptografia; em vez disso, aplicam phishing a um atendente e usam o acesso legítimo dele para consultar as viagens de pessoas escolhidas. Todos os controles funcionaram conforme especificado. O achado mostra uma lacuna de requisito: os atendentes podiam consultar qualquer cartão sem uma contestação vinculada. Sofia acrescenta um requisito de que as consultas exigem um caso aberto e são revisadas, algo que a verificação nunca teria encontrado.

### 38.3 Estudos com usuários

Sofia também observa seis atendentes lidando com contestações sintéticas. Eles acham as novas telas confusas e compartilham anotações numa ferramenta de chat, copiando detalhes das viagens para fora do sistema protegido. Isso é uma falha de validação da aceitabilidade psicológica. A equipe redesenha as telas para mostrar as anotações do caso dentro do sistema e elimina a necessidade de copiar dados. Sofia observa que controles de segurança que ignoram os padrões reais de trabalho empurram as pessoas para contornos que minam a arquitetura, então os estudos com usuários são uma atividade de segurança, e não só de usabilidade.

### Exemplo resolvido

Sofia planeja a validação; um red team obtém dados de viagem por meio do acesso legítimo de um atendente vítima de phishing, revelando uma lacuna de requisito, e um estudo com usuários encontra dados copiados para o chat, o que leva ao redesenho das telas.

> **Caso sintético.** O red team, os atendentes e os achados são sintéticos.

### Erros e limites

Os exercícios de red team cobrem apenas os caminhos tentados. Usuários observados podem se comportar de outro modo quando sabem que estão sendo observados.

### Exercícios

- **EX112 — Validação versus verificação.** Como a validação difere da verificação? *Rubrica:* 3 = a validação verifica se a especificação atende às necessidades reais; a verificação, se a construção corresponde à especificação;; 2 = as duas;; 1 = iguais;; 0 = nenhuma.

- **EX113 — Caminho do red team.** Como o red team obteve os históricos de viagem? *Rubrica:* 3 = aplicou phishing a um atendente e usou o acesso legítimo para consultar cartões escolhidos;; 2 = phishing;; 1 = quebrou a criptografia;; 0 = nenhuma.

- **EX114 — Causa do contorno.** Por que os atendentes copiavam dados para o chat? *Rubrica:* 3 = as telas eram confusas e não tinham anotações de caso;; 2 = usabilidade;; 1 = má-fé;; 0 = nenhuma.

<a id="ch-39"></a>

## Capítulo 39 — Arquitetura e engenharia de segurança: manutenibilidade

### Objetivos de aprendizagem

Você vai (1) projetar uma segurança manutenível ao longo de uma vida longa; (2) planejar a agilidade criptográfica e a substituição de componentes; (3) gerenciar a dívida técnica nos controles de segurança.

### 39.1 Sistemas de vida longa

Os sistemas de transporte funcionam por décadas. Validadores comprados hoje podem ainda estar operando daqui a quinze anos, muito depois de suas bibliotecas de software deixarem de receber atualizações. Sofia estuda a manutenibilidade: a facilidade de mudar um sistema com segurança. Para a segurança, isso significa a capacidade de aplicar patches a componentes, rotacionar chaves, substituir algoritmos e atualizar regras sem redesenho. Ela revisa o projeto do back-office quanto à manutenibilidade e descobre que o componente de verificação das tarifas tem um único algoritmo de assinatura e uma única chave fixos no código, o que tornaria as mudanças futuras arriscadas e lentas. Ela propõe a seleção de chaves e algoritmos orientada por configuração, com formatos versionados.

### 39.2 Agilidade criptográfica

Os algoritmos envelhecem. O NIST publicou em 2024 os padrões pós-quânticos FIPS 203, 204 e 205, e as organizações vão precisar migrar dos algoritmos de chave pública atuais nos próximos anos. Sofia projeta o formato de assinatura das tarifas com um campo de versão e um identificador de algoritmo, para que o back-office possa aceitar tanto os tipos de assinatura atuais quanto os futuros durante uma transição. Ela inventaria cada lugar em que a criptografia de chave pública é usada, um pré-requisito para planejar a migração. Agilidade não significa suportar todos os algoritmos; significa ser capaz de mudar deliberadamente, com procedimentos testados, quando a mudança se tornar necessária.

### 39.3 Dívida técnica de segurança

Os atalhos se acumulam: uma exceção concedida para uma demonstração que nunca foi removida, uma regra de firewall acrescentada durante um incidente e esquecida, um protocolo obsoleto mantido por causa de um parceiro antigo. Sofia cria um registro de dívida de segurança que lista cada item, seu risco, seu responsável e o plano para removê-lo. Os itens são revistos a cada trimestre, e as novas exceções precisam ter datas de expiração. Ela apresenta o registro ao comitê de arquitetura como parte normal da manutenção, e não como uma confissão. Tornar a dívida visível permite que a organização a pague deliberadamente, em vez de descobri-la durante um incidente.

### Exemplo resolvido

Sofia substitui um algoritmo de assinatura fixo no código por uma seleção versionada e orientada por configuração, inventaria o uso de chave pública para o planejamento pós-quântico e inicia um registro de dívida de segurança.

> **Caso sintético.** Os componentes e os itens de dívida são sintéticos; os FIPS 203, 204 e 205 são reais.

### Erros e limites

A agilidade acrescenta complexidade e riscos de downgrade se algoritmos antigos continuarem aceitos por tempo demais. Os registros de dívida precisam da atenção da alta direção para serem eficazes.

### Exercícios

- **EX115 — Problema do código fixo.** Que problema de manutenibilidade Sofia encontrou na verificação das tarifas? *Rubrica:* 3 = algoritmo de assinatura e chave fixos no código;; 2 = fixo no código;; 1 = nenhuma;; 0 = nenhuma.

- **EX116 — Viabilizador da agilidade.** Que características do formato viabilizam a agilidade criptográfica das assinaturas de tarifas? *Rubrica:* 3 = um campo de versão e um identificador de algoritmo;; 2 = os dois;; 1 = nenhuma;; 0 = nenhuma.

- **EX117 — Registro de dívida.** O que cada entrada do registro de dívida de segurança inclui? *Rubrica:* 3 = risco, responsável e plano de remoção;; 2 = três;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-40"></a>

## Capítulo 40 — Laboratório de verificação II

### Objetivos de aprendizagem

Você vai (1) verificar a segmentação da rede contra uma matriz de fluxos aprovada; (2) automatizar a verificação de configuração; (3) relatar desvios com evidências.

### 40.1 A matriz de fluxos como especificação

O projeto de rede do back-office define uma matriz de fluxos aprovada: quais zonas podem se conectar a quais, em quais portas. No Laboratório de Verificação II, Sofia verifica se as regras de firewall implementadas correspondem à matriz. Uma regra que permite um fluxo fora da matriz é acesso em excesso; um fluxo da matriz sem regra é uma função quebrada. Ela exporta regras de firewall sintéticas do ambiente de laboratório e as compara programaticamente com a matriz, em vez de ler centenas de regras a olho, o que é lento e sujeito a erros. O próprio script é revisado como qualquer outro controle.

### 40.2 Comparação automatizada

O script de Sofia lê a matriz aprovada e as regras exportadas, normaliza-as e calcula as diferenças. O laboratório abaixo roda sobre dados sintéticos e relata duas regras em excesso, uma que permite que as estações de trabalho da equipe alcancem diretamente o banco de viagens e uma regra any-to-any que sobrou dos testes, e um fluxo ausente da ingestão para o coletor de logs. A comparação roda automaticamente depois de cada mudança, transformando uma auditoria pontual numa verificação contínua. Ela guarda as saídas como evidências ligadas aos tickets de mudança, para que os auditores vejam quando cada desvio apareceu e quando foi fechado.

### Laboratório — Regras de firewall contra a matriz de fluxos

```python
# Compare synthetic firewall rules with an approved zone flow matrix.
approved = {("validators", "ingestion", 443), ("ingestion", "journey-db", 5432), ("ingestion", "logging", 6514),
            ("reporting", "journey-db", 5432), ("admin-jump", "ingestion", 22)}
rules = ["validators ingestion 443", "ingestion journey-db 5432", "reporting journey-db 5432",
         "admin-jump ingestion 22", "staff-ws journey-db 5432", "any any any"]
impl = {(a, b, int(p) if p != "any" else p) for a, b, p in (r.split() for r in rules)}
for x in sorted(impl - approved, key=str): print("EXCESS ", *x)
for x in sorted(approved - impl, key=str): print("MISSING", *x)
```

Execute com `python3 lab_flows.py`. Saída verificada:

```text
EXCESS  any any any
EXCESS  staff-ws journey-db 5432
MISSING ingestion logging 6514
```

### 40.3 Relatar desvios

Cada desvio vira um achado com a regra, a entrada da matriz que ela viola, o risco e uma correção proposta. A regra any-to-any é crítica porque anula completamente a segmentação; a regra da estação de trabalho para o banco de dados é alta, porque recria o contorno encontrado no capítulo 22; o fluxo de logging ausente é médio, porque enfraquece a detecção em silêncio. O relatório de Sofia também declara o que a verificação cobre: a configuração das regras, não o comportamento em tempo de execução, então um teste complementar envia tráfego sintético para confirmar a aplicação. As evidências de verificação são mais fortes quando as verificações de configuração e os testes de comportamento concordam.

### Exemplo resolvido

Sofia compara regras de firewall sintéticas com a matriz de fluxos aprovada, encontra duas regras em excesso e um fluxo ausente, classifica-os e acrescenta testes de comportamento.

> **Caso sintético.** As zonas, as regras e a matriz são sintéticas.

### Erros e limites

As exportações de configuração podem não refletir as regras em vigor. As matrizes precisam ser mantidas atualizadas, ou a verificação confere o alvo errado.

### Exercícios

- **EX118 — Excesso versus ausência.** Qual é a diferença entre uma regra em excesso e um fluxo ausente? *Rubrica:* 3 = o excesso permite acesso não aprovado; a ausência quebra uma função aprovada;; 2 = os dois;; 1 = iguais;; 0 = nenhuma.

- **EX119 — Desvios do laboratório.** Que desvios o laboratório relatou? *Rubrica:* 3 = excesso estação-da-equipe-para-banco-de-viagens e any-to-any; ausência ingestão-para-logging;; 2 = três;; 1 = um;; 0 = nenhuma.

- **EX120 — Declaração de cobertura.** O que a verificação de configuração não cobre? *Rubrica:* 3 = o comportamento de aplicação em tempo de execução;; 2 = tempo de execução;; 1 = tudo coberto;; 0 = nenhuma.

<a id="ch-41"></a>

## Capítulo 41 — Arquitetura e engenharia de segurança: otimização do sistema

### Objetivos de aprendizagem

Você vai (1) formular a seleção de controles como uma otimização sob orçamento; (2) comparar a seleção gulosa e a exaustiva sobre dados sintéticos; (3) reconhecer os limites da otimização numérica na segurança.

### 41.1 Escolher sob restrições

O orçamento de segurança da Corvia para o próximo ano não consegue financiar todos os controles propostos. Sofia formula a escolha como uma otimização: cada controle candidato tem um custo e uma redução de risco estimada a partir da avaliação de risco do capítulo 24, e o objetivo é maximizar a redução total dentro do orçamento. Essa é uma versão do problema da mochila da matemática discreta. Formular a decisão assim torna as premissas explícitas e permite que as partes interessadas vejam por que um controle foi preferido a outro, em vez de depender de quem argumenta mais alto numa reunião de orçamento.

### 41.2 Guloso versus exaustivo

Sofia compara dois métodos sobre oito controles candidatos sintéticos. Um método guloso escolhe os controles em ordem de redução por unidade de custo até esgotar o orçamento. Uma busca exaustiva testa todas as combinações, o que é viável aqui porque oito itens dão só 256 subconjuntos. O laboratório abaixo mostra que a seleção gulosa chega perto, mas perde a melhor combinação, porque enche o orçamento com itens pequenos e eficientes e não deixa espaço para um controle grande e valioso. Em problemas maiores, a busca exaustiva se torna impossível, e os engenheiros usam algoritmos melhores ou aceitam aproximações conscientemente.

### Laboratório — Seleção de controles gulosa e exaustiva

```python
# Greedy vs exhaustive control selection under budget (synthetic costs and risk reductions).
from itertools import combinations
C = {"mfa-admins": (8, 10), "egress-filter": (15, 13), "log-review": (20, 14), "hsm-keys": (50, 34),
     "edr-depots": (35, 20), "phish-training": (12, 9), "backup-offline": (25, 17), "waf": (30, 15)}
B = 100
g, cost, val = [], 0, 0
for k, (c, v) in sorted(C.items(), key=lambda kv: kv[1][1] / kv[1][0], reverse=True):
    if cost + c <= B: g.append(k); cost += c; val += v
best = max((s for r in range(len(C) + 1) for s in combinations(C, r) if sum(C[k][0] for k in s) <= B),
           key=lambda s: sum(C[k][1] for k in s))
print(f"greedy:     value {val}, cost {cost}, {sorted(g)}")
print(f"exhaustive: value {sum(C[k][1] for k in best)}, cost {sum(C[k][0] for k in best)}, {sorted(best)}")
```

Execute com `python3 lab_knapsack.py`. Saída verificada:

```text
greedy:     value 63, cost 80, ['backup-offline', 'egress-filter', 'log-review', 'mfa-admins', 'phish-training']
exhaustive: value 74, cost 98, ['backup-offline', 'egress-filter', 'hsm-keys', 'mfa-admins']
```

### 41.3 Limites dos números

A otimização só é tão boa quanto seus dados de entrada. As estimativas de redução de risco são incertas, os controles interagem, de modo que dois controles podem se sobrepor em vez de se somar, e alguns controles são obrigatórios para a conformidade, qualquer que seja a pontuação. Sofia roda a seleção com estimativas baixas e altas e mostra quais controles são escolhidos em todos os cenários; essas são as escolhas robustas. Ela apresenta o resultado como apoio à decisão, e não como uma decisão. Daniel acrescenta que o principal valor do exercício é a conversa que ele força sobre as estimativas, que muitas vezes revela que ninguém sabe quanto um controle popular de fato reduz o risco.

### Exemplo resolvido

Sofia formula os controles do próximo ano como um problema da mochila com orçamento, mostra a seleção gulosa perdendo o ótimo em dados sintéticos e identifica as escolhas robustas nas faixas de estimativa.

> **Caso sintético.** Os controles, os custos e as reduções são sintéticos.

### Erros e limites

A redução de risco aditiva é irrealista quando os controles se sobrepõem. Os controles obrigatórios precisam ser fixados antes da otimização.

### Exercícios

- **EX121 — Tipo de problema.** A que problema clássico a seleção de controles com orçamento se assemelha? *Rubrica:* 3 = o problema da mochila;; 2 = mochila;; 1 = ordenação;; 0 = nenhuma.

- **EX122 — Deficiência do guloso.** No laboratório, como a seleção gulosa se comparou ao ótimo exaustivo? *Rubrica:* 3 = o guloso chegou a 63 com custo 80; o ótimo foi 74 com custo 98 e incluiu hsm-keys;; 2 = os dois valores;; 1 = iguais;; 0 = nenhuma.

- **EX123 — Escolha robusta.** O que torna um controle uma escolha robusta? *Rubrica:* 3 = ele é selecionado tanto com as estimativas baixas quanto com as altas;; 2 = os dois cenários;; 1 = maior pontuação;; 0 = nenhuma.

<a id="ch-42"></a>

## Capítulo 42 — Arquitetura e engenharia de segurança: pesquisa aplicada

### Objetivos de aprendizagem

Você vai (1) formular uma pergunta de pesquisa aplicada a partir da prática de engenharia; (2) desenhar um pequeno estudo usando dados da Corvia com responsabilidade; (3) relatar os achados com seus limites.

### 42.1 Uma pergunta vinda da prática

O projeto de pesquisa aplicada de Sofia pergunta se os certificados de dispositivo de curta duração, introduzidos no capítulo 31, reduziram a janela em que validadores desativados ainda conseguiam se autenticar. A pergunta vem da prática e importa para a Corvia. Ela define o desfecho como os dias entre a desativação e a última autenticação bem-sucedida, compara os dispositivos desativados antes e depois da mudança e lista rivais, como uma melhoria simultânea nos registros de ativos. Herley e van Oorschot (2017) alertam contra afirmações de segurança que não podem ser testadas; a pergunta dela nomeia exatamente o que mostraria ausência de efeito.

### 42.2 Uso responsável dos dados

O estudo usa os logs operacionais da Corvia, que contêm identificadores de dispositivos, mas nenhum dado de passageiros. Sofia combina com Daniel e com o encarregado de proteção de dados quais campos pode usar, guarda os extratos numa área de projeto com controle de acesso e os exclui depois do estudo. Ela pseudonimiza os identificadores de dispositivos em todas as saídas. Até dados técnicos podem ser sensíveis: uma lista de dispositivos que continuaram se autenticando depois da desativação poderia guiar um atacante até os pontos fracos. Seu relatório, portanto, apresenta agregados e distribuições, não listas de dispositivos, e ela compartilha a lista detalhada apenas com o responsável pelas operações.

### 42.3 Achados com limites

Os dispositivos desativados depois da mudança deixaram de se autenticar numa mediana de dois dias, contra onze dias antes. A melhoria dos registros de ativos aconteceu ao mesmo tempo, então Sofia não consegue separar totalmente as duas causas; ela observa que os dispositivos cujos registros de ativos já eram exatos antes da mudança também melhoraram, o que sustenta fracamente o efeito dos certificados. Ela relata o achado com essa limitação e recomenda o monitoramento contínuo. O projeto lhe ensina que até perguntas modestas de engenharia precisam de um desenho cuidadoso para produzir respostas confiáveis.

### Exemplo resolvido

Sofia estuda a autenticação depois da desativação antes e depois dos certificados de curta duração, usa os logs dentro de limites acordados e relata uma queda de onze para dois dias, registrando um fator de confusão.

> **Caso sintético.** Os logs, os dispositivos e os resultados são sintéticos; Herley e van Oorschot (2017) é real.

### Erros e limites

Desenhos antes e depois não conseguem excluir mudanças simultâneas. Contagens pequenas de dispositivos tornam as medianas instáveis.

### Exercícios

- **EX124 — Definição do desfecho.** Que desfecho Sofia mediu? *Rubrica:* 3 = dias entre a desativação e a última autenticação bem-sucedida;; 2 = definido;; 1 = vago;; 0 = nenhuma.

- **EX125 — Cuidado com a lista de dispositivos.** Por que o relatório evita listar dispositivos individuais? *Rubrica:* 3 = uma lista assim poderia guiar atacantes até os pontos fracos;; 2 = mapa para atacantes;; 1 = sem motivo;; 0 = nenhuma.

- **EX126 — Fator de confusão.** Que fator de confusão limita a conclusão? *Rubrica:* 3 = as melhorias nos registros de ativos aconteceram ao mesmo tempo;; 2 = registros de ativos;; 1 = nenhuma;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX126 (as de EX127–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Sofia Mbeki, Daniel Ferreira, a Kestrel Polytechnic University, a Corvia Regional Transit e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Que o aumento de cada mês é proporcional ao volume atual, de modo que o crescimento absoluto continua se acelerando.

**EX002.** Mês 24 (20,5 TB contra um orçamento de 20 TB), quinze meses antes do que prevê a previsão linear.

**EX003.** Porque trata um processo exponencial como linear e subestima o volume futuro.

**EX004.** contractor-07, via vendor-support, field-tech e fare-ops até fare-admins: quatro grupos de profundidade.

**EX005.** O conjunto de usuários que podem criar e o conjunto dos que podem aprovar devem ter interseção vazia.

**EX006.** Duas pessoas diferentes em conluio, uma criando e outra aprovando, o que exige controles de processo.

**EX007.** Porque os atacantes podem alcançá-los fisicamente, abri-los e instrumentá-los por longos períodos num veículo público.

**EX008.** Selecionar componentes seguros avaliados, como secure elements, onde quer que os atacantes possam obter acesso físico.

**EX009.** Porque a latência da rede e as falhas de conectividade fazem com que o servidor central nem sempre consiga responder a tempo.

**EX010.** Um valor negativo, um timestamp no futuro e um identificador de cartão com caracteres inesperados.

**EX011.** Uma mensagem pública curta de registro inválido e uma entrada de log detalhada, com a linha e o motivo, num arquivo restrito.

**EX012.** Porque secrets obtém os valores da fonte criptograficamente segura do sistema operacional, enquanto random pode ser previsto.

**EX013.** Contexto, decisão, opções consideradas, consequências e data.

**EX014.** Onde quer que o nível de confiança mude, por exemplo entre os dispositivos embarcados e a rede da garagem.

**EX015.** Que um cartão roubado ainda poderia ser usado por até uma hora, até a próxima atualização da lista de bloqueio.

**EX016.** O número total de tentativas fraudulentas ao longo do dia.

**EX017.** O uso indevido esperado cai de 12,6 para 3,1 usos por dia, um quarto do valor com atualização a cada hora.

**EX018.** Cerca de 0,55 exatamente; o atalho n vezes p dá 0,8, que superestima porque n p não é pequeno.

**EX019.** A probabilidade de a validação ser fraude, dado que foi sinalizada.

**EX020.** Cerca de 4,5 por cento; mais de 95 por cento dos sinais eram alarmes falsos.

**EX021.** Porque os tempos de revisão são assimétricos, de modo que a média representa mal o caso típico e a cauda.

**EX022.** Porque as diferenças no tempo de acesso revelam quais dados foram usados recentemente, permitindo side channels.

**EX023.** Porque permitem que o código atravesse as fronteiras impostas pelo hardware das quais todos os outros controles dependem.

**EX024.** Porque qualquer pessoa com a chave de assinatura pode produzir um firmware que o secure boot aceitará.

**EX025.** Reduzem o que precisa ser revisado e permitem que os módulos confiem em entradas validadas em vez de repetir verificações.

**EX026.** Aplicar um desconto infantil a um cartão de adulto deve ser rejeitado.

**EX027.** Rastrear os componentes usados e responder às vulnerabilidades encontradas neles.

**EX028.** A segurança, a saúde e o bem-estar públicos.

**EX029.** Abertas, porque a evacuação dos passageiros tem prioridade sobre a cobrança da tarifa.

**EX030.** Escrever uma nota clara do risco específico ao seu mentor para que ele possa ser escalado.

**EX031.** Não limita quais sistemas internos um veículo comprometido pode alcançar depois de conectado.

**EX032.** Um notebook infectado consegue alcançar diretamente os servidores de bilhetagem, e o monitoramento não consegue distinguir os fluxos normais.

**EX033.** Numa lista dos fluxos de que cada zona realmente precisa, permitindo apenas esses.

**EX034.** Porque, se fosse comprometido, os privilégios de root minariam todas as outras permissões do servidor.

**EX035.** Porque os sistemas derivam da baseline, e a baseline só é útil se os desvios forem percebidos.

**EX036.** Para que um atacante que obtenha acesso ao servidor não consiga apagar o registro de suas ações.

**EX037.** Porque revelam os padrões de moradia, trabalho e deslocamento das pessoas.

**EX038.** A consulta concatenada devolveu as 4 linhas, enquanto a consulta parametrizada devolveu 0.

**EX039.** Porque dados que nunca são guardados não podem vazar, e menos dados são mais fáceis de proteger adequadamente.

**EX040.** Preparar a organização, proteger o software, produzir software bem protegido e responder a vulnerabilidades.

**EX041.** O replay de solicitações de reembolso para obter reembolsos em dobro e funcionários aprovando os próprios reembolsos.

**EX042.** Falhas no nível do projeto, como o problema da autoaprovação, que exigem revisão humana.

**EX043.** Um grupo de fraudadores é uma ameaça; uma interface sem autenticação é uma vulnerabilidade que ele poderia explorar.

**EX044.** As solicitações de reembolso são recusadas até que a autorização possa ser verificada.

**EX045.** Organizacional, de pessoas, físico e tecnológico.

**EX046.** O suporte, incluindo a aplicação de patches, e a desativação, incluindo a destruição de dados.

**EX047.** Das necessidades de proteção das partes interessadas aos requisitos de segurança, à arquitetura e ao projeto, e à garantia de que são atendidos.

**EX048.** Mostra quais elementos de projeto e evidências de verificação dependem daquele requisito.

**EX049.** Disparando-a de propósito para que bloqueie usuários legítimos, transformando o controle numa negação de serviço.

**EX050.** Durante o ataque, ela alternou entre 20 e 100 requisições por minuto a cada minuto (9 mudanças de direção), enquanto o ganho 0.6 se estabilizou perto de 56 com 1 mudança.

**EX051.** Tamanhos de ajuste limitados e limites mínimo e máximo, com revisão humana quando os limites forem atingidos.

**EX052.** Por requisitos de negócio expressos como atributos, como privado ou disponível.

**EX053.** O serviço de gestão de chaves não tinha responsável operacional.

**EX054.** Mostra qual atributo de negócio aquele controle sustentava e que agora fica enfraquecido.

**EX055.** Uma conta de suporte compartilhada de fornecedor que contorna o single sign-on e a autenticação multifator.

**EX056.** A Corvia nunca armazena os números reais dos cartões, então um vazamento dos seus sistemas não pode expô-los.

**EX057.** Geração, armazenamento, rotação e revogação, além de distribuição e destruição.

**EX058.** As obrigações do setor de pagamentos exigem segmentar os sistemas de pagamento das demais redes.

**EX059.** Os validadores legados só podem ser substituídos no quinto ano.

**EX060.** Que a tokenização de pagamentos já estava contratada e que o aplicativo de passageiros estava fora do escopo.

**EX061.** Reembolsos acima de cinquenta euros devem exigir a aprovação de uma segunda pessoa distinta do solicitante, verificada por teste.

**EX062.** Cada registro de validação deve ter um identificador único, e os duplicados devem ser detectados e rejeitados.

**EX063.** Para procurar lacunas nos seus requisitos; ele revelou que faltava um requisito de proteção e revisão de logs.

**EX064.** Os relatórios liam diretamente do banco de viagens, em vez de passar por uma interface, contornando os controles de acesso.

**EX065.** Criptografia e autenticação do fluxo.

**EX066.** Ou o modelo está desatualizado ou o sistema tem um fluxo inesperado; as duas possibilidades precisam ser investigadas.

**EX067.** Validadores desativados que ainda tinham certificados internos podiam enviar registros, porque os certificados não haviam sido revogados.

**EX068.** Os erros de cálculo da tarifa depois de mudanças de tarifa: 0.0080 por dia contra 0.0010 dos registros perdidos, com o evento de topo em 0.0090 (cerca de 3,3 dias por ano).

**EX069.** Porque uma causa comum, como uma queda de energia, pode fazer vários ramos falharem juntos.

**EX070.** Agrupam riscos muito diferentes sob rótulos como alto.

**EX071.** Preparar a avaliação, conduzi-la, comunicar os resultados e mantê-la.

**EX072.** Um responsável do negócio com autoridade; os engenheiros recomendam.

**EX073.** Porque os ônibus ainda precisam recarregar quando a conexão de internet da garagem falha.

**EX074.** Admitiram que ainda não tinham resposta e a registraram como uma questão em aberto.

**EX075.** Limites de hardware nos carregadores que o controlador não consegue sobrepor e a separação da rede do controlador em relação aos sistemas corporativos.

**EX076.** Porque comparar só duas pode esconder uma opção intermediária melhor, e uma opção mínima fornece uma base.

**EX077.** A alternativa A, a opção on-premises, venceria.

**EX078.** O processo de pseudonimização se torna um ponto único de falha para a privacidade dos passageiros.

**EX079.** A verificação da assinatura antes da carga, o registro e o alerta sobre versões não publicadas e o rollback para a última tabela verificada.

**EX080.** Porque, se a chave de assinatura fosse roubada, as assinaturas ainda seriam verificadas, mas a lista independente revelaria versões não publicadas.

**EX081.** Uma tabela de tarifas modificada depois de assinada deve ser rejeitada.

**EX082.** Para que os controles difíceis não sejam abandonados em silêncio e os revisores possam verificar que todo requisito foi implementado.

**EX083.** Ela foi removida do histórico do repositório, rotacionada e registrada como incidente.

**EX084.** Porque enfraqueceria um requisito de segurança, que só uma decisão de arquitetura pode mudar.

**EX085.** A mediana do número de dias entre a desativação do dispositivo e a revogação do certificado.

**EX086.** Uma mediana de 8 dias entre os dispositivos revogados, só 8 de 20 revogados em até uma semana e 3 nunca revogados; criptografia e registro cobriam 4 de 5 repositórios.

**EX087.** A taxa de reabertura, para mostrar se tickets foram fechados sem correções reais.

**EX088.** Se o sistema foi construído de acordo com suas especificações.

**EX089.** Só o primeiro registro autêntico; os registros duplicado, alterado e do validador desativado foram rejeitados.

**EX090.** O comportamento durante o failover do banco de dados.

**EX091.** Um registro de ativo e um ticket de instalação aprovado.

**EX092.** Certificados ainda ativos para dispositivos fora de serviço, causados por eventos de integração perdidos.

**EX093.** Controles compensatórios, um responsável e uma expiração atrelada à data de substituição.

**EX094.** Multiplicam-se, de modo que o serviço é menos disponível do que seu componente mais fraco.

**EX095.** A disponibilidade geral subiu de 0.9960 para 0.9980, de cerca de 35 para 18 horas de indisponibilidade por ano, porque o repositório de segredos era o elo mais fraco.

**EX096.** A ingestão das validações faz soft-fail usando listas em cache por pouco tempo; o acesso administrativo faz hard-fail.

**EX097.** A capacidade de antecipar, resistir, recuperar-se e adaptar-se a condições adversas.

**EX098.** Diversidade, ao oferecer um canal alternativo que não compartilha os modos de falha do sistema principal.

**EX099.** Porque a equipe sabe que os serviços podem continuar funcionando em níveis reduzidos, então há menos pressão para pagar ou restaurar de forma insegura.

**EX100.** A única API key compartilhada e de longa duração do aplicativo de mobilidade e as exportações mensais de dados para a consultoria por e-mail.

**EX101.** Vender passagens e consultar tarifas, mas não ler históricos de viagem.

**EX102.** Deixou claro qual parte notificava os passageiros afetados e quais tokens a Corvia deveria revogar.

**EX103.** Coordenar a equipe, manter um registro de decisões compartilhado e fazer os conflitos aparecerem cedo.

**EX104.** Dados de viagem detalhados por noventa dias, com atributos agregados de fraude guardados por dois anos.

**EX105.** Nenhum plano para o comprometimento das chaves do serviço de tokenização e nenhum responsável claro pelas solicitações de exclusão dos passageiros.

**EX106.** O logging de debug verboso nos volumes da bilhetagem baseada em conta.

**EX107.** Com a mesma reposição de 20 por segundo, a capacidade 20 rejeitou 200 de 450 requisições, enquanto a capacidade 200 rejeitou só 20.

**EX108.** Um token ou direito revogado pode continuar funcionando até a decisão em cache expirar, por até um minuto.

**EX109.** Govern, identify, protect, detect, respond e recover.

**EX110.** Alertando quando as exportações excedem o volume normal ou ocorrem fora do horário de trabalho.

**EX111.** Mudanças que afetam autenticação, criptografia, regras de rede ou logging.

**EX112.** A verificação checa se o sistema corresponde à sua especificação; a validação checa se a especificação atende às necessidades reais.

**EX113.** Aplicando phishing a um atendente e usando o acesso legítimo de consulta desse atendente.

**EX114.** Porque as telas eram confusas e não ofereciam lugar para as anotações do caso, então eles usavam o chat.

**EX115.** O componente tinha um único algoritmo de assinatura e uma única chave fixos no código.

**EX116.** Um campo de versão e um identificador de algoritmo no formato assinado.

**EX117.** O risco do item, um responsável e um plano para removê-lo.

**EX118.** Uma regra em excesso permite um acesso que não está na matriz; um fluxo ausente bloqueia algo que a matriz exige.

**EX119.** Regras em excesso das estações de trabalho da equipe para o banco de viagens e uma regra de teste any-to-any, além de um fluxo ausente da ingestão para o logging.

**EX120.** Se as regras são de fato aplicadas em tempo de execução, o que exige testes de tráfego de comportamento.

**EX121.** O problema da mochila: maximizar o valor dentro de um limite de peso, aqui o custo.

**EX122.** O guloso chegou a uma redução de 63 usando 80 do orçamento, enquanto o ótimo exaustivo chegou a 74 com custo 98 ao incluir o grande controle hsm-keys.

**EX123.** Ele é escolhido em todos os cenários de estimativa, do baixo ao alto.

**EX124.** O número de dias entre a desativação de um dispositivo e sua última autenticação bem-sucedida.

**EX125.** Porque uma lista de dispositivos que ainda se autenticavam depois da desativação poderia ajudar um atacante a encontrar pontos fracos.

**EX126.** As melhorias nos registros de ativos ocorreram ao mesmo tempo que a mudança dos certificados.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Herley, C., & van Oorschot, P. C. (2017). SoK: Science, security and the elusive goal of security as a scientific pursuit. *2017 IEEE Symposium on Security and Privacy*, 99–120. <https://doi.org/10.1109/SP.2017.38>
- International Organization for Standardization. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Joint Task Force. (2018). *Risk management framework for information systems and organizations* (NIST SP 800-37 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-37r2>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Josefsson, S., & Liusvaara, I. (2017). *Edwards-curve digital signature algorithm (EdDSA)* (RFC 8032). IETF. <https://www.rfc-editor.org/rfc/rfc8032>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- National Institute of Standards and Technology. (2024). *Module-lattice-based digital signature standard* (FIPS 204). <https://doi.org/10.6028/NIST.FIPS.204>
- National Institute of Standards and Technology. (2024). *Module-lattice-based key-encapsulation mechanism standard* (FIPS 203). <https://doi.org/10.6028/NIST.FIPS.203>
- National Institute of Standards and Technology. (2024). *Stateless hash-based digital signature standard* (FIPS 205). <https://doi.org/10.6028/NIST.FIPS.205>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., & McQuaid, R. (2021). *Developing cyber-resilient systems: A systems security engineering approach* (NIST SP 800-160 Vol. 2 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v2r1>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sherwood, J., Clark, A., & Lynas, D. (2005). *Enterprise security architecture: A business-driven approach* (SABSA). CMP Books.
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
- Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure software development framework (SSDF) version 1.1* (NIST SP 800-218). NIST. <https://doi.org/10.6028/NIST.SP.800-218>
- The Open Group. (2016, revised 2022). *Integrating risk and security within a TOGAF enterprise architecture* (TOGAF Series Guide G152). The Open Group.
