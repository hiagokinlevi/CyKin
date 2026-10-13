# Arquitetura e Engenharia de Segurança: Curso de Engenharia

- Idioma: português do Brasil (`pt`); curso 122, curso de engenharia (5 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 50 já estão escritos em português, com os exercícios EX001–EX012 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 5–50 (EX013–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

Capítulos 5–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX012 (as de EX013–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). Sofia Mbeki, Daniel Ferreira, a Kestrel Polytechnic University, a Corvia Regional Transit e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
