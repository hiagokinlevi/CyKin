# Arquitetura e Engenharia de Segurança: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 122, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 50 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 4 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 11–50 (EX031–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Sofia Mbeki, Daniel Ferreira, a Kestrel Polytechnic University, a Corvia Regional Transit e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
