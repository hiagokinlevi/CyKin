# Inteligência de ameaças e OSINT: um livro de engenharia

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 50 já estão escritos em português, com os exercícios EX001–EX018 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 7–50 (EX019–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de engenharia que vão projetar, construir, verificar e operar plataformas de inteligência de ameaças e fluxos de OSINT como sistemas confiáveis.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite ético: nenhuma coleta sobre pessoas privadas reais, nenhuma evasão de termos de uso, nenhuma desanonimização e nenhuma interação com infraestrutura de adversários. Toda organização, pessoa, indicador e número é **sintético**, salvo quando uma frase cita uma fonte pública; os endereços usam as faixas da RFC 5737 e os domínios usam `.example`.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os capítulos 1–19 aplicam fundamentos de matemática, computação e segurança a problemas de inteligência. Os capítulos 20–41 constroem uma plataforma de CTI, dos requisitos aos modelos, controles, implementação, medição, confiabilidade, integração, escala, operações, validação e otimização, com ateliês de projeto e laboratórios de verificação. Os capítulos 42–50 tratam de pesquisa, prática, projeto final, revisão, ensaios de falha, dossiê de evidências, trabalho de conclusão e defesa. Cada capítulo tem objetivos, texto didático, um exemplo resolvido, um caso sintético rotulado, erros e limites, três exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**.

### Caso contínuo sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Brightwater Energy Networks (BEN)** — distribuidora regional de energia elétrica com um SOC de 14 pessoas | Organização que precisa de CTI | Inventada |
| **Lantern** — plataforma interna de CTI da BEN (ingestão TAXII 2.1, repositório STIX 2.1, enriquecimento, disseminação) | Sistema construído ao longo do livro | Inventado |
| **Kofi Mensah** | Estudante de engenharia em estágio na equipe de engenharia de segurança da BEN | Inventado |

### Fontes principais

MITRE [ATT&CK](https://attack.mitre.org/); OASIS [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) e [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html); [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf); a [kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf) de Hutchins et al.; NIST [SP 800-150](https://doi.org/10.6028/NIST.SP.800-150); FIRST [TLP 2.0](https://www.first.org/tlp/); [ICD 203](https://www.odni.gov/files/documents/ICD/ICD-203.pdf). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Objetivos de aprendizagem

Você vai (1) ler taxas de variação em cargas de trabalho de inteligência; (2) interpretar uma derivada como "com que rapidez isto está crescendo agora"; (3) aproximar a área sob uma curva para totalizar uma carga de trabalho; (4) evitar extrapolar uma inclinação local longe demais.

### 1.1 Taxas em um SOC

Os indicadores chegam ao Lantern a uma taxa que muda ao longo do dia: baixa durante a madrugada, crescente quando comunidades parceiras em outros fusos horários publicam. Se N(t) é a contagem acumulada de indicadores recebidos até a hora t, sua derivada N′(t) é a taxa de chegada. Os engenheiros dimensionam os parsers e os workers de enriquecimento para o pico de N′, e não para a média diária, porque as filas se formam quando a chegada instantânea supera o atendimento. Um feed que entrega a maior parte do volume diário em duas horas da manhã precisa de workers dimensionados para essas horas, mesmo que a média pareça tranquila. Kofi traça a taxa, e não o total acumulado, quando verifica isso, porque uma curva acumulada esconde as rajadas dentro de sua subida constante.

### 1.2 Inclinações a partir de dados

Dados reais são discretos. Um quociente de diferenças — (N(t+1) − N(t)) / 1 hora — estima a taxa. Suavizar ao longo de várias horas reduz o ruído, mas esconde rajadas curtas; a escolha depende de você estar planejando capacidade (use picos) ou relatando tendências (suavize). Por isso Kofi mantém duas visões das mesmas contagens. As diferenças horárias brutas vão para a revisão de capacidade, onde uma única hora movimentada importa. Uma média móvel de seis horas vai para o relatório mensal, cujos leitores querem saber se o volume dos parceiros está crescendo. Cada gráfico diz qual das duas visões mostra. As horas ausentes ficam como lacunas, em vez de preenchidas, porque um valor inventado distorceria tanto o pico quanto a tendência.

### 1.3 Áreas como totais

Se r(t) é a taxa de horas de analista necessárias para triar alertas, a integral de r ao longo de um turno é o esforço total. Uma soma de trapézios sobre amostras horárias é precisa o bastante para dimensionar a equipe. Com amostras a cada hora, a regra dos trapézios faz a média de cada par de taxas vizinhas e a multiplica por uma hora. Somar essas fatias ao longo de um turno de oito horas dá as horas de analista que o turno precisa cobrir. Se o resultado for onze horas de trabalho e houver três analistas no turno, o plano tem folga; se for trinta, a equipe precisa de ajuda ou de um escopo de triagem mais estreito. A estimativa só é tão boa quanto as amostras, por isso uma hora ausente é marcada, e não adivinhada.

### 1.4 Limites das inclinações locais

Uma rajada durante uma grande campanha pode mostrar uma inclinação acentuada. Projetar essa inclinação um mês à frente prevê volumes absurdos. Derivadas descrevem o agora; previsões exigem modelos de causa. Kofi viu isso quando um parceiro publicou, em uma única tarde, um grande acúmulo de indicadores antigos. A taxa horária saltou dez vezes e voltou ao normal no dia seguinte. Se ele tivesse dimensionado o Lantern pela inclinação daquela tarde, a BEN teria comprado hardware para uma carga que nunca voltou. Uma previsão precisa de uma explicação de por que o volume muda, como a entrada de um novo parceiro, e a inclinação só lhe diz que algo mudou.

### Nota de prática — Unidades e painéis

O painel do Lantern certa vez traçou o total acumulado onde os operadores esperavam uma taxa, e o turno da noite leu uma linha plana e calma como um pico repentino quando o eixo mudou de escala. Hoje Kofi rotula cada gráfico como 'por hora' ou 'acumulado desde 00:00 UTC', e a revisão de capacidade usa apenas gráficos de taxa.

### Exemplo resolvido

Kofi amostra a contagem acumulada de indicadores do Lantern às 08:00 (12.400), às 09:00 (12.700) e às 10:00 (13.300). A taxa subiu de 300 para 600 por hora. Ele dimensiona o parser para pelo menos 600 por hora mais uma margem, e anota que o salto coincidiu com o boletim matinal de um parceiro — um aumento programado, não estrutural.

> **Caso sintético.** As contagens do Lantern foram inventadas para este capítulo.

### Erros e limites

Confundir a contagem acumulada com a taxa leva a planos de capacidade absurdos. Aqui o cálculo mede cargas de trabalho; ele não prevê adversários.

### Exercícios

- **EX001 — Taxa horária.** Usando as amostras de Kofi, calcule a taxa de chegada entre 09:00 e 10:00. *Rubrica:* 3 = 600 por hora, com o método; 2 = só o número; 1 = usa o acumulado; 0 = nenhuma.
- **EX002 — Pico ou média.** Explique por que a capacidade do parser é dimensionada pela taxa de pico, e não pela média diária. *Rubrica:* 3 = as filas se formam quando a chegada supera o atendimento; a média esconde rajadas; 2 = parcial; 1 = a média basta; 0 = nenhuma.
- **EX003 — Total por trapézios.** As horas de analista necessárias são 2, 4 e 6 por hora em três amostras horárias consecutivas. Estime o esforço total nessas duas horas. *Rubrica:* 3 = 8 horas de analista por trapézios; 2 = método certo; 1 = soma 12; 0 = nenhuma.

### Síntese

Taxas dimensionam sistemas, áreas totalizam esforço, e inclinações locais não devem ser esticadas até virar previsões.

### Continue estudando — capítulo 01 de 50

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Objetivos de aprendizagem

Você vai (1) representar relações de inteligência como um grafo; (2) calcular a alcançabilidade com busca em largura; (3) relacionar os pivôs no grafo ao Diamond Model; (4) explicar por que componentes desconexos importam para alegações de atribuição.

### 2.1 Conjuntos e relações

Um conjunto de indicadores é um conjunto; "o evento usa a infraestrutura" é uma relação. União, interseção e diferença permitem aos engenheiros comparar feeds; as relações permitem ligar eventos. O STIX 2.1 expressa relações explicitamente por meio de objetos de relacionamento como "indicates" ou "uses". Kofi compara dois feeds de parceiros pela interseção de seus conjuntos de domínios. A sobreposição lhe diz quanto o segundo feed acrescenta; a diferença mostra o que apenas um parceiro viu. A união é o que o Lantern precisa armazenar. As relações carregam mais do que pertinência: um par como um indicador e o malware que ele indica diz como duas coisas estão ligadas, e o tipo dessa ligação importa quando um analista decide depois até que ponto confiar nela.

### 2.2 Grafos e pivôs

Trate eventos, infraestrutura, capacidades e vítimas como nós, e suas ligações como arestas. O Diamond Model de Caltagirone, Pendergast e Betz descreve o pivô analítico exatamente ao longo dessas arestas: de um evento para sua infraestrutura, da infraestrutura para outros eventos. A busca em largura conta saltos, o que é um limite natural para o quanto um analista deve confiar em uma cadeia de inferências. Por isso a contagem de saltos do laboratório funciona também como medida de confiança. A um salto de um evento está algo que a evidência mostra diretamente; três saltos são uma cadeia de inferências, cada uma das quais pode estar errada.

### Laboratório 1 — grafo de pivôs

```python
"""Lab 1 (ch 02): breadth-first pivot over a synthetic Diamond-style relationship graph."""
from collections import deque
edges = [("event-1", "c2.example"), ("c2.example", "event-4"), ("event-4", "victim-B"),
         ("event-1", "victim-A"), ("event-7", "loader-x"), ("loader-x", "event-9")]
g = {}
for a, b in edges:
    g.setdefault(a, set()).add(b); g.setdefault(b, set()).add(a)
def reach(start, max_hops):
    seen, q = {start: 0}, deque([start])
    while q:
        n = q.popleft()
        if seen[n] == max_hops:
            continue
        for m in sorted(g[n]):
            if m not in seen:
                seen[m] = seen[n] + 1; q.append(m)
    return seen
for node, hops in sorted(reach("event-1", 3).items(), key=lambda x: (x[1], x[0])):
    print(hops, node)
print("event-7 reachable:", "event-7" in reach("event-1", 10))
```

Execute com `python3 lab_graph.py`. Saída verificada:

```text
0 event-1
1 c2.example
1 victim-A
2 event-4
3 victim-B
event-7 reachable: False
```

### 2.3 Componentes

O event-7 e seu loader não são alcançáveis a partir do event-1. Dois componentes significam que nenhuma evidência neste grafo liga as atividades. Alegações de que ambas pertencem a uma mesma campanha precisam de novas evidências, e não de arestas desejadas. A saída do laboratório mostra essa separação com clareza: a busca a partir do event-1 nunca alcança o event-7, por mais saltos que permita. Um analista ainda pode suspeitar de uma ligação, talvez porque os dois loaders se comportam de modo parecido, mas essa suspeita pertence às anotações, como hipótese a testar. Desenhar uma aresta sem evidência faria o grafo concordar com o analista e não ensinaria nada a ninguém. Se chegar uma nova evidência, como um certificado compartilhado, a aresta é acrescentada com sua fonte, e os componentes se fundem de forma registrada.

### 2.4 Limites de saltos

Cada salto acrescenta incerteza. O Lantern limita os pivôs automáticos a três saltos e rotula qualquer coisa além disso como hipótese do analista. O limite decorre de uma aritmética simples. Se cada ligação está certa nove vezes em dez, uma cadeia de três saltos está certa apenas cerca de sete vezes em dez, e uma cadeia de cinco saltos, pouco mais da metade das vezes. Pivôs automáticos além de três saltos encheriam os relatórios de ligações com a mesma chance de estarem erradas ou certas. Um analista ainda pode seguir uma cadeia mais longa à mão, mas o resultado é rotulado como hipótese, e o raciocínio de cada salto extra fica registrado para que um revisor possa conferi-lo.

### Nota de prática — Pesos das arestas

Nem toda aresta merece a mesma confiança. O Lantern pondera uma aresta pela especificidade: um certificado autoassinado único compartilhado por dois servidores é uma ligação forte; um resolvedor público popular quase não é ligação. A alcançabilidade ponderada permite ao analista perguntar quais nós são alcançáveis apenas por arestas fortes, o que costuma encolher um grafo de campanha dramático até algo defensável.

### Exemplo resolvido

Kofi executa o pivô a partir do event-1. Em até três saltos, ele alcança c2.example, victim-A, event-4 e victim-B. Ele relata que victim-B está ligada ao event-1 apenas por infraestrutura compartilhada, uma cadeia de três saltos, e recomenda notificar o contato setorial de victim-B com essa ressalva.

> **Caso sintético.** Todos os nós são inventados.

### Erros e limites

Infraestrutura compartilhada, como um grande provedor de hospedagem, cria ligações falsas; pondere as arestas pela especificidade. Alcançabilidade no grafo não é atribuição.

### Exercícios

- **EX004 — Contagem de saltos.** Em quantos saltos o laboratório alcança victim-B? *Rubrica:* 3 = 3; 2 = correto, sem explicar o caminho; 1 = errado; 0 = nenhuma.
- **EX005 — Componente separado.** O que "event-7 reachable: False" implica para uma alegação de campanha? *Rubrica:* 3 = nenhuma evidência de ligação no grafo; a alegação precisa de novas evidências; 2 = parcial; 1 = mesma campanha; 0 = nenhuma.
- **EX006 — Armadilha da hospedagem compartilhada.** Por que uma aresta por um IP de uma grande hospedagem compartilhada pode criar uma ligação falsa? *Rubrica:* 3 = muitos clientes sem relação entre si o compartilham; baixa especificidade; 2 = vago; 1 = sem problema; 0 = nenhuma.

### Síntese

Conjuntos comparam, grafos ligam, saltos custam confiança, e componentes desconexos são um silêncio honesto.

### Continue estudando — capítulo 02 de 50

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Física para computação

### Objetivos de aprendizagem

Você vai (1) relacionar a propagação de sinais e a largura de banda à latência da coleta; (2) estimar o crescimento do armazenamento da inteligência retida; (3) entender energia e refrigeração como restrições de plataformas sempre ligadas; (4) ligar a temporização física à precisão dos carimbos de tempo.

### 3.1 A latência tem um piso

A luz na fibra viaja a cerca de 200.000 km por segundo, então uma ida e volta entre continentes custa dezenas de milissegundos antes de qualquer processamento. Uma consulta TAXII 2.1 através de um oceano nunca será instantânea; os engenheiros definem intervalos de consulta e timeouts com esse piso em mente. Kofi mediu uma consulta do Lantern a um servidor parceiro em outro continente e viu cerca de cem milissegundos antes da chegada do primeiro byte. Esse custo é fixado pela distância. Um timeout menor que o piso faz toda requisição falhar, enquanto um muito mais longo esconde quedas reais. Ele define o timeout em vários segundos e registra a duração de cada consulta, para que um parceiro lento apareça nos logs, e não como dados ausentes.

### 3.2 Largura de banda e feeds em lote

Um feed em lote de 2 GB por noite em um enlace de 100 Mbit/s leva cerca de 160 segundos à taxa plena, ignorando sobrecargas. Se o enlace é compartilhado com o tráfego operacional das subestações, programar as transferências longe dos horários de pico é uma decisão física, e não meramente administrativa. É por isso que o exemplo resolvido acrescenta a sobrecarga e programa a transferência para as 02:00. Um download grande durante o dia poderia competir com a telemetria das subestações, que a BEN não pode se dar ao luxo de atrasar. Limitar a taxa da transferência é outra opção, trocando um download mais longo por uma fatia menor do enlace.

### 3.3 Crescimento do armazenamento

Armazenar 50.000 objetos STIX por dia, com cerca de 2 KB cada, dá aproximadamente 100 MB por dia, cerca de 36 GB por ano antes dos índices. Índices e enriquecimento podem triplicar isso. Políticas de retenção são, portanto, entradas de engenharia. Kofi transforma esses números em uma pergunta de retenção para o líder de CTI: por quanto tempo os indicadores expirados precisam continuar pesquisáveis? Manter dois anos de objetos brutos mais os índices poderia passar de duzentos gigabytes, enquanto resumir os itens expirados após noventa dias mantém o repositório bem menor. A resposta depende de as investigações precisarem de indicadores antigos, e isso é um requisito a combinar com os analistas, e não uma escolha da equipe de armazenamento.

### 3.4 Relógios

Os relógios dos servidores derivam. Se o coletor do Lantern e o firewall da BEN discordam em dois minutos, as medições de tempo até o bloqueio ficam erradas em dois minutos. Sincronização de tempo pela rede e fontes de relógio registradas importam para a evidência. Kofi verifica se todos os servidores do Lantern e o firewall obtêm a hora da mesma fonte sincronizada, e se cada log registra a fonte que usou. Quando se descobriu, durante um teste, que o relógio do firewall estava adiantado, ele corrigiu as medições anteriores pelo desvio conhecido e anotou a correção ao lado dos resultados. Uma métrica construída sobre relógios não sincronizados pode mostrar tempos até o bloqueio negativos, o sinal mais rápido de que algo está errado.

### 3.5 Energia e calor

Um cluster local do Lantern consome energia e precisa de refrigeração. Em uma empresa de energia isso parece trivial, mas salas de SOC não são data centers; o planejamento de capacidade inclui a sala. Kofi estimou o consumo de três servidores e descobriu que ficava perto do que a refrigeração da sala conseguia remover em uma tarde quente. Acrescentar um quarto servidor exigiria nova refrigeração, um custo que o plano original não previa. Instalar o cluster no data center da BEN eliminou o problema, ao preço de um caminho de rede mais longo até o SOC.

### Nota de prática — Orçamentos de latência

A latência de ponta a ponta é uma soma: idas e voltas na rede, esperas em fila, parsing, enriquecimento e o envio ao firewall. Kofi escreve uma tabela de orçamento com uma meta para cada parcela, de modo que um nível de serviço de 30 minutos possa ser conferido componente a componente. Quando uma parcela cresce, a tabela mostra qual etapa roubou o tempo.

### Exemplo resolvido

Kofi estima o tempo de transferência noturna de um arquivo de 2 GB de um parceiro: 2 GB × 8 = 16 Gbit, / 0,1 Gbit/s = 160 s. Com 30% de sobrecarga de protocolo, ele planeja cerca de 210 s e programa a transferência para as 02:00, longe dos picos de telemetria das subestações.

> **Caso sintético.** Os tamanhos dos feeds e as velocidades dos enlaces são inventados.

### Erros e limites

Contas de guardanapo orientam o projeto; meça antes de comprometer hardware. Bits e bytes são um erro frequente de fator oito.

### Exercícios

- **EX007 — Tempo de transferência.** Estime o tempo de transferência de 500 MB a 50 Mbit/s, ignorando a sobrecarga. *Rubrica:* 3 = 80 s, com o método; 2 = método certo, com deslize; 1 = erro de byte/bit; 0 = nenhuma.
- **EX008 — Armazenamento anual.** Estime o armazenamento bruto de um ano a 20.000 objetos/dia × 2 KB. *Rubrica:* 3 ≈ 14,6 GB (40 MB/dia); 2 = ordem de grandeza certa; 1 = erro de fator 1000; 0 = nenhuma.
- **EX009 — Desvio de relógio.** Como um desvio de relógio de 2 minutos afeta uma métrica de tempo até o bloqueio? *Rubrica:* 3 = enviesa cada medição em até 2 minutos; é preciso NTP e fonte registrada; 2 = "impreciso"; 1 = nenhum efeito; 0 = nenhuma.

### Síntese

A física impõe pisos à latência, orçamentos à largura de banda e ao armazenamento, e a precisão de cada carimbo de tempo em que um analista confia.

### Continue estudando — capítulo 03 de 50

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever funções pequenas e puras que transformam registros de inteligência; (2) usar os tipos da biblioteca padrão para strings, conjuntos e dicionários; (3) testar funções contra entradas conhecidas; (4) recusar-se a escrever código de coleta que viole termos de uso ou a privacidade.

### 4.1 Registros como dicionários

Um indicador já interpretado é naturalmente um dicionário: `{"type": "domain", "value": "c2.example", "source": "partner-A", "tlp": "TLP:GREEN"}`. Funções que recebem um registro e devolvem um novo são fáceis de testar e de compor. O dicionário mantém cada campo nomeado, então o código fica legível e campos ausentes podem ser verificados. As funções de Kofi nunca alteram o registro que recebem; elas devolvem um novo, o que significa que uma versão anterior continua disponível se uma etapa posterior der errado. Um registro sem fonte ou sem rótulo TLP é rejeitado nesta etapa, em vez de armazenado sem eles.

### 4.2 Funções puras primeiro

Uma função pura não tem efeitos colaterais: dada a mesma entrada, devolve a mesma saída e não escreve nada. Normalizar um domínio para minúsculas é puro. Gravar no banco de dados não é. Mantenha as partes puras separadas, para que a maior parte do código possa ser testada sem infraestrutura. O parser de Kofi segue essa divisão. As funções que limpam e validam um registro são puras e têm dezenas de testes rápidos. Uma camada externa fina lê do feed e grava no repositório, e essa camada é testada com menos frequência, contra um banco de dados de teste. Quando aparece um bug, os testes puros costumam localizá-lo em segundos.

### 4.3 Texto desarmado

Relatórios muitas vezes "desarmam" (*defang*) indicadores — `hxxp`, `[.]` — para que ninguém clique neles. Um parser deve rearmá-los apenas dentro da plataforma, nunca em saídas que pessoas vão colar em navegadores. O Lantern armazena a forma normal e exibe a forma desarmada nos relatórios. As duas formas nunca podem ser confundidas. Se um relatório mostra um link ativo e um analista clica nele, o clique pode chegar à infraestrutura do atacante, o que o limite ético do livro proíbe. A função de exibição de Kofi desarma todo domínio e endereço, e um teste falha se qualquer saída de relatório contiver um esquema funcional.

### 4.4 Testes

Para cada função, escreva três casos de resposta conhecida: um valor normal, um caso-limite e uma entrada malformada. A entrada malformada deve produzir um erro explícito ou uma marca de rejeição, nunca um valor adivinhado. Para uma função que normaliza um domínio, o caso normal pode ser um nome com maiúsculas e minúsculas misturadas que deve voltar em minúsculas. O caso-limite pode ser um nome com um ponto final, e o caso malformado, uma string com um espaço no meio. Escrever esses três testes antes da própria função muitas vezes revela o que ela deve fazer quando a entrada é estranha, que é onde os feeds reais causam problemas.

### 4.5 O que não programar

Às vezes os estudantes perguntam como raspar uma plataforma social em busca de dados pessoais de agentes de ameaça. O código do Lantern coleta apenas de fontes cujos termos o permitem, e apenas os campos necessários. Coleta automatizada que burla limites de taxa, logins ou termos está fora do escopo. A regra protege as pessoas tanto quanto a BEN. Os dados pessoais de um suposto agente podem pertencer a alguém sem envolvimento, e reuni-los pode violar a legislação de privacidade e os termos das plataformas. As fontes do Lantern são listadas com os termos que permitem seu uso, e acrescentar uma nova fonte exige a aprovação do líder de CTI antes que qualquer código seja escrito. As revisões de código de Kofi conferem essa lista.

### Exemplo resolvido

Kofi escreve `refang(s)`, que substitui `hxxp` e `[.]`. Seus testes: `"hxxp://a[.]example"` → `"http://a.example"`; `"a.example"` inalterado; `""` → rejeitado. A versão de um colega devolvia uma string vazia para entrada vazia; a de Kofi a rejeita, para que valores vazios nunca virem indicadores armazenados.

> **Caso sintético.** A função e os testes de Kofi são inventados.

### Erros e limites

Trechos de parsing copiados e colados podem conter chamadas de rede; leia-os. Strings rearmadas em relatórios convidam a cliques acidentais.

### Exercícios

- **EX010 — Teste de pureza.** Uma função que normaliza maiúsculas e minúsculas e também grava em um arquivo de log é pura? Por quê? *Rubrica:* 3 = não; gravar em arquivo é efeito colateral; 2 = não; 1 = sim; 0 = nenhuma.
- **EX011 — Regra do rearme.** Onde indicadores rearmados podem aparecer, e onde devem permanecer desarmados? *Rubrica:* 3 = rearmados no processamento/armazenamento da plataforma; desarmados nos relatórios para pessoas; 2 = uma metade; 1 = rearmados em toda parte; 0 = nenhuma.
- **EX012 — Entrada vazia.** O que `refang("")` deve devolver no desenho de Kofi, e por quê? *Rubrica:* 3 = rejeição/erro, para que valores vazios nunca sejam armazenados; 2 = só o erro; 1 = string vazia; 0 = nenhuma.

### Síntese

Funções pequenas e puras, rejeição explícita, saídas desarmadas e código de coleta que respeita os termos de uso.

### Continue estudando — capítulo 04 de 50

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Comunicação em engenharia

### Objetivos de aprendizagem

Você vai (1) escrever requisitos, notas de projeto e resumos de incidentes em linguagem simples; (2) separar fatos, suposições e julgamentos, como recomenda a ICD 203; (3) aplicar rótulos TLP a documentos de engenharia; (4) escolher figuras que reduzam a confusão, em vez de aumentá-la.

### 5.1 Escrever para a decisão do leitor

Todo documento responde a uma pergunta do leitor. Um requisito responde "o que o sistema deve fazer?". Uma nota de projeto responde "por que deste jeito?". Um resumo de inteligência responde "o que devo fazer agora?". Comece pela resposta e depois a sustente. Um analista que lê um resumo no início do turno quer saber se deve bloquear, observar ou ignorar. Se essa resposta estiver enterrada no quarto parágrafo, o leitor pode agir com base na errada. Kofi põe a ação recomendada na primeira frase e a evidência abaixo dela, para que um leitor que pare cedo ainda aja corretamente e um que continue lendo possa conferir o raciocínio.

### 5.2 Fato, suposição, julgamento

"O feed do Parceiro A entregou 12.000 indicadores ontem" é um fato. "O feed do Parceiro A é, em sua maioria, atual" é uma suposição, a menos que seja medida. "Devemos priorizar o Parceiro A para bloqueio automatizado" é um julgamento. Os padrões de ofício analítico da ICD 203 pedem que quem escreve distinga informação de suposições e julgamentos; os engenheiros se beneficiam da mesma disciplina. Kofi marca cada tipo em seus rascunhos. Um fato traz sua fonte e data, uma suposição diz o que a confirmaria, e um julgamento declara quem o fez. Assim os leitores podem contestar a coisa certa.

### 5.3 TLP em documentos

Uma nota de projeto que contém nomes de parceiros sob um acordo de compartilhamento AMBER herda essa restrição. Coloque o rótulo TLP 2.0 no cabeçalho e no rodapé. Documentos sem rótulo tendem a se espalhar. O modelo de Kofi põe o rótulo nos dois lugares, para que uma página impressa ainda o mostre. Um documento que mistura materiais deve levar o rótulo mais restritivo entre suas partes, ou ser dividido para que a parte mais ampla possa circular mais longe. Os nomes dos parceiros costumam ser o elemento restrito, e substituí-los por um identificador neutro pode permitir que o resto seja compartilhado.

### 5.4 Figuras

Um único gráfico de tempo até o bloqueio por fonte é mais claro que um painel de vinte medidores. Rotule os eixos com unidades; informe o período e a fonte dos dados na legenda. Kofi testou com o turno da noite um painel de muitos medidores e descobriu que ninguém conseguia dizer qual fonte era a mais lenta. Um único gráfico de barras ordenado pela mediana do tempo até o bloqueio respondeu isso em segundos. Cada gráfico que ele publica agora tem uma legenda com o período, a fonte dos dados e a unidade, para que o leitor possa julgar se uma mudança é real ou resultado de uma medição diferente.

### 5.5 Revisão

Peça a um revisor que repita seu ponto principal em uma frase. Se ele não conseguir, reescreva. Kofi faz isso com um colega antes de enviar qualquer nota de projeto. Quando o colega descreveu sua nota sobre enriquecimento como sendo sobre logs, ele percebeu que a conclusão estava no último parágrafo. Movê-la para o topo resolveu o problema. Uma segunda verificação é perguntar que ação o leitor deve tomar; se o revisor não souber dizer, a nota não tem um pedido claro. As duas verificações levam poucos minutos e poupam os leitores de um documento confuso.

### Nota de prática — Formas curtas

Executivos leem o primeiro parágrafo e a figura. Analistas leem a tabela de indicadores. Engenheiros leem o registro de decisão. Kofi escreve cada documento com um resumo de três linhas no topo — decisão, motivo, prazo —, para que todo leitor possa parar cedo sem perder a ação que lhe cabe.

### Exemplo resolvido

Kofi redige uma nota recomendando um segundo worker de enriquecimento. O primeiro rascunho abre com três parágrafos de histórico. Ele reescreve: "Acrescentar um worker de enriquecimento antes de 1º de março; o atraso da fila passou de 10 minutos em 9 de 30 dias (fato). Supomos que o volume cresça 20% este ano (suposição)." O gestor aprova em uma única leitura.

> **Caso sintético.** A nota e os números são inventados.

### Erros e limites

Rotular tudo como RED impede o compartilhamento necessário; rotular de menos vaza informação. Linguagem simples não é o mesmo que linguagem vaga.

### Exercícios

- **EX013 — Classifique as frases.** Classifique "a fila passou de 10 minutos em 9 de 30 dias" e "o volume vai crescer 20%". *Rubrica:* 3 = fato; suposição (ou julgamento de previsão); 2 = uma certa; 1 = ambas fatos; 0 = nenhuma.
- **EX014 — Rótulo herdado.** Uma nota de projeto cita nomes de parceiros cobertos por um acordo AMBER. Que rótulo TLP a nota deve levar? *Rubrica:* 3 = pelo menos TLP:AMBER (herdado); 2 = algum rótulo; 1 = CLEAR; 0 = nenhuma.
- **EX015 — Conteúdo da legenda.** Liste três coisas que a legenda de um gráfico deve informar. *Rubrica:* 3 = unidades/métrica, período, fonte dos dados; 2 = duas; 1 = só o título; 0 = nenhuma.

### Síntese

Responda primeiro, separe fato de suposição e julgamento, rotule a sensibilidade e faça cada figura trazer suas unidades e sua fonte.

### Continue estudando — capítulo 05 de 50

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Objetivos de aprendizagem

Você vai (1) modelar o decaimento da confiança de indicadores com uma função exponencial; (2) resolver para o instante em que um valor cruza um limiar; (3) escolher meias-vidas por tipo de indicador; (4) reconhecer quando os modelos de decaimento enganam.

### 6.1 Por que decaimento

Os indicadores perdem valor: os adversários trocam endereços IP depressa e domínios mais devagar, enquanto comportamentos descritos por técnicas do ATT&CK persistem por meses ou anos. A Pyramid of Pain de Bianco captura essa ordem. O Lantern a codifica como uma pontuação de confiança que decai com o tempo, a menos que o indicador seja observado de novo. A pontuação não mede o quanto um indicador é perigoso. Ela estima a probabilidade de que o indicador ainda aponte para atividade hostil. Um endereço que era malicioso na semana passada pode agora pertencer a um cliente sem relação da mesma empresa de hospedagem, e bloqueá-lo cortaria tráfego legítimo. O decaimento embute esse risco no Lantern sem que alguém precise se lembrar de remover entradas antigas à mão.

### 6.2 O modelo

c(t) = c₀ · e^(−t·ln2/h), em que h é a meia-vida em dias. Depois de uma meia-vida, a confiança cai pela metade; depois de duas, para um quarto. Resolver c(t) = piso dá t = h · ln(c₀/piso) / ln 2. Em palavras, a pontuação cai pela mesma fração a cada dia, então a queda é grande enquanto a confiança é alta e pequena perto do piso. A segunda fórmula responde à pergunta prática: em quantos dias este indicador precisa de revisão? Kofi a usa para agendar a revalidação, em vez de deixar as entradas se arrastarem. Mudar a meia-vida muda a inclinação, mas a forma continua a mesma.

### Laboratório 2 — decaimento

```python
"""Lab 2 (ch 06): exponential confidence decay for a synthetic indicator, c(t) = c0 * exp(-t * ln2 / h)."""
import math
c0, half_life_days, floor = 90.0, 14.0, 30.0
for t in (0, 7, 14, 21, 28):
    print(f"day {t:2d}: confidence {c0 * math.exp(-t * math.log(2) / half_life_days):5.1f}")
t_floor = half_life_days * math.log(c0 / floor) / math.log(2)
print(f"falls below {floor:.0f} after {t_floor:.1f} days -> retire or re-validate")
```

Execute com `python3 lab_decay.py`. Saída verificada:

```text
day  0: confidence  90.0
day  7: confidence  63.6
day 14: confidence  45.0
day 21: confidence  31.8
day 28: confidence  22.5
falls below 30 after 22.2 days -> retire or re-validate
```

### 6.3 Escolhendo meias-vidas

Meias-vidas são parâmetros de engenharia ajustados a partir de dados de reobservação: com que frequência um indicador de IP ainda parece malicioso depois de uma semana? O Lantern começa com 14 dias para IPs, 45 para domínios e nenhuma para hashes de arquivos (que não mudam, mas podem se tornar irrelevantes), e depois ajusta a partir das evidências. Kofi registra cada valor inicial com o raciocínio por trás dele. Os catorze dias para endereços refletem a rapidez com que os clientes de hospedagem mudam; o período mais longo para domínios reflete os custos de registro. Hashes não decaem porque um arquivo nunca muda, mas são revistos quando a família de malware deixa de aparecer.

### 6.4 Reobservação

Um avistamento redefine c para um novo valor. O modelo, portanto, descreve obsolescência, e não verdade. Quando um parceiro relata o mesmo endereço outra vez, ou os próprios sensores da BEN o veem em tráfego hostil, o Lantern eleva a pontuação ao valor definido para esse tipo de avistamento e o relógio recomeça. Um indicador que continua sendo visto permanece ativo enquanto for visto. Um que nunca mais é visto se apaga no prazo, qualquer que seja sua confiança inicial. O registro guarda cada avistamento com sua fonte, para que um analista possa ver por que a pontuação é o que é.

### 6.5 Quando o modelo engana

Uma infraestrutura adormecida reutilizada depois de meses terá decaído para perto de zero. Indicadores aposentados devem ser arquivados, e não apagados, para que os analistas ainda possam correlacionar eventos históricos. Kofi viu isso com um domínio que ficara quieto por seis meses e depois reapareceu em uma campanha de phishing. Sua pontuação tinha caído muito abaixo do piso de bloqueio, então o Lantern não o bloqueou automaticamente. Como o arquivo ainda o guardava, o analista que viu o novo avistamento encontrou na hora a campanha anterior e elevou a pontuação à mão. Apagar as entradas aposentadas teria perdido esse histórico.

### Nota de prática — Reajustando meias-vidas

A cada trimestre, Kofi amostra indicadores aposentados e verifica quantos reapareceram em avistamentos posteriores. Se indicadores de IP ainda são avistados depois de 30 dias a uma taxa relevante, a meia-vida de 14 dias é curta demais. O reajuste é registrado com o tamanho da amostra, para que revisores posteriores possam julgar se a mudança se justificava.

### Exemplo resolvido

Com c₀ = 90, h = 14 dias e um piso de 30, o laboratório mostra confiança 45.0 no dia 14 e o cruzamento do piso depois de 22.2 dias. O Lantern agenda a revalidação para o dia 22 e retira o indicador do bloqueio automatizado, a menos que ele seja observado de novo.

> **Caso sintético.** Os parâmetros são ilustrativos, não medidos.

### Erros e limites

Uma curva elegante pode esconder dados ruins; ajuste as meias-vidas a partir das evidências. O decaimento serve para indicadores, não para julgamentos sobre a intenção do adversário.

### Exercícios

- **EX016 — Valor no dia 14.** Que confiança o laboratório imprime no dia 14, e por que esse número? *Rubrica:* 3 = 45.0; uma meia-vida reduz 90 à metade; 2 = só o número; 1 = errado; 0 = nenhuma.
- **EX017 — Tempo até o piso.** Usando a fórmula, depois de quantos dias a confiança cruza 30? *Rubrica:* 3 = 22,2 dias, com a fórmula; 2 = só o número; 1 = 28; 0 = nenhuma.
- **EX018 — Arquivar, não apagar.** Por que arquivar indicadores decaídos em vez de apagá-los? *Rubrica:* 3 = correlação histórica/reuso de infraestrutura; análise retrospectiva; 2 = vago; 1 = apagar não tem problema; 0 = nenhuma.

### Síntese

O decaimento exponencial codifica a obsolescência, as meias-vidas vêm das evidências, e os indicadores aposentados continuam pesquisáveis.

### Continue estudando — capítulo 06 de 50

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX018 (as de EX019–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). A Brightwater Energy Networks, o Lantern, Kofi Mensah e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** (13.300 − 12.700) / 1 h = 600 indicadores por hora.

**EX002.** As filas de trabalho crescem sempre que as chegadas superam o atendimento; uma média diária dilui justamente as rajadas que sobrecarregam o parser.

**EX003.** Trapézios: (2+4)/2 + (4+6)/2 = 3 + 5 = 8 horas de analista.

**EX004.** Três saltos: event-1 → c2.example → event-4 → victim-B.

**EX005.** Nada no grafo liga o event-7 ao event-1, então uma alegação de campanha comum precisa de evidências adicionais.

**EX006.** Milhares de clientes sem relação entre si podem compartilhar um único endereço de hospedagem, então a coocorrência ali diz pouco sobre um adversário comum.

**EX007.** 500 MB × 8 = 4.000 Mbit; / 50 Mbit/s = 80 s.

**EX008.** 20.000 × 2 KB = 40 MB por dia; × 365 ≈ 14,6 GB brutos por ano.

**EX009.** Cada intervalo medido pode ficar errado em até dois minutos, sempre na mesma direção; sincronize os relógios com NTP e registre a fonte de tempo.

**EX010.** Não. Gravar em um arquivo de log é um efeito colateral, então a função não é pura; separe a normalização do log.

**EX011.** Os valores rearmados são usados dentro do parsing e do armazenamento do Lantern; relatórios e mensagens mostrados a pessoas mantêm a forma desarmada.

**EX012.** Uma rejeição (erro ou marca), porque uma string vazia nunca pode ser armazenada como indicador.

**EX013.** A frase sobre a fila é um fato medido; o crescimento de 20% é uma suposição sobre o futuro.

**EX014.** Pelo menos TLP:AMBER, herdado do acordo que cobre os nomes de parceiros citados.

**EX015.** A métrica e suas unidades, o período coberto e a fonte dos dados.

**EX016.** 45.0 — o dia 14 é exatamente uma meia-vida, então 90 cai pela metade, para 45.

**EX017.** t = 14 × ln(90/30) / ln 2 = 14 × 1,585 ≈ 22,2 dias.

**EX018.** Os adversários às vezes reutilizam infraestrutura antiga, e os analistas precisam correlacionar eventos passados; indicadores arquivados continuam pesquisáveis sem acionar bloqueios automatizados.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Bianco, D. (2013). The Pyramid of Pain. <https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>
- Caltagirone, S., Pendergast, A. and Betz, C. (2013). The Diamond Model of Intrusion Analysis. Technical Report ADA586960, Center for Cyber Intelligence Analysis and Threat Research. <https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf>
- European Union. Regulation (EU) 2016/679 (General Data Protection Regulation). <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- FIRST. Traffic Light Protocol (TLP) version 2.0. <https://www.first.org/tlp/>
- Heuer, R. J. (1999). Psychology of Intelligence Analysis. CIA Center for the Study of Intelligence. <https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/>
- Hutchins, E. M., Cloppert, M. J. and Amin, R. M. (2011). Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains. Lockheed Martin. <https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf>
- Kent, S. (1964). Words of Estimative Probability. CIA Studies in Intelligence. <https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf>
- MITRE ATT&CK Enterprise matrix, groups, software and technique pages. <https://attack.mitre.org/>
- NIST SP 800-150 (2016). Guide to Cyber Threat Information Sharing. <https://doi.org/10.6028/NIST.SP.800-150>
- NIST SP 800-61 Rev. 3 (2025). Incident Response Recommendations and Considerations for Cybersecurity Risk Management. <https://doi.org/10.6028/NIST.SP.800-61r3>
- OASIS. STIX Version 2.1 (Committee Specification / OASIS Standard). <https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html>
- OASIS. TAXII Version 2.1. <https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html>
- ODNI. Intelligence Community Directive 203: Analytic Standards (2015, amended 2022). <https://www.odni.gov/files/documents/ICD/ICD-203.pdf>
