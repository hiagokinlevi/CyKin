# Inteligência de ameaças e OSINT: um livro de engenharia

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–36 de 50 já estão escritos em português, com os exercícios EX001–EX108 e suas resoluções com rubricas de 0 a 3 e 8 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 37–50 (EX109–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) |

Capítulos 37–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-37), até a chegada dos próximos lotes.

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

<a id="ch-07"></a>

## Capítulo 7 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) calcular a precisão a partir da sensibilidade, da taxa de falsos positivos e da prevalência; (2) explicar o efeito da taxa-base sobre os alertas; (3) expressar julgamentos com palavras de probabilidade calibradas; (4) escolher resumos adequados a dados assimétricos.

### 7.1 O efeito da taxa-base

Uma regra que detecta 95% das conexões maliciosas e detecta por engano 2% das benignas parece excelente. Mas, se apenas 1 em cada 100 conexões é maliciosa, a maioria dos alertas é falsa. Se apenas 1 em cada 1.000 é maliciosa, quase todos são. O laboratório demonstra isso com números. Na prevalência mais baixa, quase duas mil conexões benignas são sinalizadas para menos de cem maliciosas. Os analistas aprendem depressa a ignorar esses alertas, e então perdem os verdadeiros. A regra em si não mudou entre as duas linhas; só mudou o tráfego sobre o qual ela roda. É por isso que Kofi sempre pergunta onde uma regra vai rodar antes de julgar o quanto ela é boa.

### Laboratório 3 — taxa-base

```python
"""Lab 3 (ch 07): base-rate effect on alert precision for a synthetic indicator match rule."""
for prevalence in (0.01, 0.001):
    sens, fpr, n = 0.95, 0.02, 100000
    bad = n * prevalence; good = n - bad
    tp, fp = bad * sens, good * fpr
    print(f"prevalence {prevalence:.3f}: TP={tp:.0f} FP={fp:.0f} precision={tp/(tp+fp):.3f}")
```

Execute com `python3 lab_bayes.py`. Saída verificada:

```text
prevalence 0.010: TP=950 FP=1980 precision=0.324
prevalence 0.001: TP=95 FP=1998 precision=0.045
```

### 7.2 Lendo o laboratório

Na prevalência 0.010, 950 verdadeiros e 1.980 falsos positivos dão precisão 0.324. Em 0.001, a precisão cai para 0.045: cerca de 21 alertas falsos para cada verdadeiro. A resposta de engenharia: reduzir a taxa de falsos positivos, elevar a prevalência aplicando a regra apenas onde o tráfego malicioso é mais provável, ou encaminhar as detecções ao enriquecimento antes dos analistas. A terceira opção é a que o exemplo resolvido recomenda. Uma detecção passa então a somar peso a outras evidências, em vez de acionar um analista sozinha. Kofi também confere a aritmética à mão uma vez, porque um laboratório que discorda de um cálculo simples geralmente tem um bug.

### 7.3 Palavras calibradas

Os analistas traduzem probabilidades em palavras. O ensaio de Kent sobre palavras de probabilidade estimativa mostrou que os leitores interpretam "provável" de modo inconsistente; as equipes devem publicar um mapeamento. A ICD 203 também pede que a incerteza seja expressa de forma adequada. O guia de relatórios do Lantern dá a cada palavra uma faixa: por exemplo, provável significa uma probabilidade entre cerca de 0,55 e 0,80. Os analistas escolhem uma palavra da tabela, e não por instinto, e o leitor pode consultar o que ela significa. Kofi procura nos rascunhos palavras fora da tabela, como possivelmente, que os leitores interpretam como qualquer coisa entre rara e meio a meio. A tabela é revista todo ano com as pessoas que leem os relatórios, para que as palavras mantenham o sentido que os leitores esperam.

### 7.4 Dados assimétricos

O tempo até o bloqueio e a latência do enriquecimento são assimétricos à direita. Medianas e percentis (p90, p99) os descrevem melhor do que médias. A maioria dos indicadores é bloqueada em minutos, mas alguns esperam horas porque um parceiro os reteve ou uma aprovação demorou. Esses poucos puxam a média muito acima do que um indicador típico vive. A mediana mostra o caso habitual e o nonagésimo percentil mostra o quanto os casos lentos pioram. Kofi relata os dois, com a contagem de itens, para que os leitores vejam a cauda longa sem que ela distorça o número típico. Uma única média não descreveria nenhum indicador real.

### Nota de prática — Revocação e cobertura

A precisão responde quantos alertas são verdadeiros; a revocação (*recall*) responde quantos eventos maliciosos foram detectados. Um feed muito preciso, mas que cobre uma pequena parte do cenário de ameaças, ainda pode deixar a BEN exposta. Por isso o Lantern relata as duas, e estima a revocação a partir de revisões de incidentes em que o conjunto completo de eventos maliciosos foi estabelecido depois. Kofi também mantém uma pequena tabela da prevalência suposta para cada segmento de tráfego, porque a mesma regra se comporta de modo muito diferente no Wi-Fi de visitantes e na rede de gerência das subestações.

### Exemplo resolvido

Kofi avalia uma regra proposta que detecta qualquer conexão aos IPs de um feed. Ele estima a prevalência perto de 0.001 no tráfego da BEN, calcula a precisão de 0.045 e recomenda usar a regra como entrada do enriquecimento, e não como acionamento direto dos analistas.

> **Caso sintético.** As taxas são ilustrativas.

### Erros e limites

A prevalência é difícil de conhecer; declare as suposições. Precisão sem revocação esconde ameaças não detectadas.

### Exercícios

- **EX019 — Precisão citada.** Que precisão o laboratório dá na prevalência 0.001? *Rubrica:* 3 = 0.045; 2 = aproximada; 1 = 0.95; 0 = nenhuma.
- **EX020 — Correção de engenharia.** Cite duas formas de melhorar a precisão desta regra. *Rubrica:* 3 = duas entre reduzir a FPR / restringir a segmentos de maior prevalência / portão de enriquecimento; 2 = uma; 1 = só aumentar a sensibilidade; 0 = nenhuma.
- **EX021 — Escolha do percentil.** Por que relatar a latência p90 do enriquecimento em vez da média? *Rubrica:* 3 = a cauda assimétrica importa para a experiência do usuário/SLA; a média a esconde; 2 = vago; 1 = a média é melhor; 0 = nenhuma.

### Síntese

As taxas-base dominam a qualidade dos alertas, as palavras precisam de números por trás, e métricas assimétricas precisam de percentis.

### Continue estudando — capítulo 07 de 50

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Arquitetura de computadores

### Objetivos de aprendizagem

Você vai (1) relacionar a hierarquia de CPU, memória e armazenamento ao processamento de inteligência; (2) estimar se uma carga de trabalho é limitada por CPU, por memória ou por E/S; (3) explicar o cache para consultas de enriquecimento; (4) reconhecer âncoras de confiança em hardware nos sistemas de coleta.

### 8.1 A hierarquia

Registradores e caches são rápidos e pequenos; a memória principal é maior e mais lenta; o armazenamento em estado sólido é mais lento ainda; o armazenamento em rede é o mais lento. O conjunto quente do Lantern — os indicadores comparados com o tráfego ao vivo — precisa caber na memória, ou cada comparação espera pelo disco. Kofi verificou isso com um teste simples. Comparar um lote com um conjunto em memória levou alguns milissegundos; as mesmas consultas a um índice em disco levaram dezenas de milissegundos, a maior parte esperando leituras. O arquivo frio pode ficar em armazenamento mais lento, porque os analistas o consultam de vez em quando e podem esperar um segundo por uma resposta.

### 8.2 Limitado por quê

Interpretar objetos STIX em JSON consome muita CPU. Juntar indicadores com avistamentos consome muita memória. Carregar arquivos consome muita E/S. O profiling identifica o recurso limitante; comprar o hardware errado é comum e caro. Kofi aprendeu isso quando chegou um pedido de discos mais rápidos para resolver um parsing lento. O profiling mostrou que o parser usava um núcleo de processador inteiro enquanto os discos ficavam ociosos. Discos mais rápidos não teriam mudado nada. Um segundo processo worker, que não custou nada além de configuração, praticamente dobrou a vazão. Cada perfil é salvo junto com o hardware em que rodou, para que as comparações posteriores sejam justas.

### 8.3 Cache de enriquecimento

O enriquecimento — acrescentar dados de registro no estilo WHOIS, DNS passivo ou contexto interno de ativos — muitas vezes repete consultas. Um cache indexado pelo indicador, com tempo de vida (TTL), evita consultas repetidas e respeita os limites de taxa e os termos de terceiros. Dados em cache precisam expirar, tanto pela exatidão quanto porque os termos de alguns provedores limitam a retenção. Kofi define o tempo de vida por provedor, usando o menor entre o que a exatidão exige e o que os termos do provedor permitem. O cache registra quando cada entrada foi obtida, para que um analista saiba se os dados estão frescos.

### 8.4 Raízes de confiança em hardware

Servidores de coleta que assinam os dados exportados dependem de chaves. Um módulo de segurança de hardware (HSM) ou um TPM mantém as chaves de assinatura fora da memória comum, melhorando a integridade do que o Lantern compartilha. Sem esse módulo, a chave fica em um arquivo que qualquer pessoa com acesso de administrador ao servidor poderia copiar, e uma chave copiada permite a um atacante assinar indicadores falsos em que os parceiros confiariam. Com ele, a assinatura continua funcionando, mas a chave não pode ser exportada. O desenho de Kofi lista quais servidores guardam chaves de assinatura e quem pode usá-las, e os logs do módulo mostram cada operação de assinatura para revisão posterior.

### 8.5 Dimensionamento de memória

Um milhão de indicadores com média de 200 bytes em um conjunto em memória precisam de cerca de 200 MB mais a sobrecarga; objetos Python podem triplicar isso. Meça. Kofi montou um conjunto de um milhão de strings de teste e o mediu, em vez de confiar na aritmética. O resultado foi várias vezes o tamanho dos dados brutos, porque cada objeto string carrega sua própria sobrecarga. Ele então dimensionou a memória do comparador com espaço para um ano de crescimento e uma margem, e registrou o método de medição para que possa ser repetido quando os volumes mudarem. Uma representação compacta, como armazenar hashes dos valores, poderia reduzir o consumo se a memória ficasse apertada.

### Nota de prática — Disciplina de profiling

Kofi faz profiling antes e depois de toda mudança de desempenho e guarda os relatórios. Mudanças que não movem o gargalo medido são revertidas, mesmo que "devessem" ajudar. Esse hábito impede a equipe de acumular otimizações engenhosas que acrescentam complexidade, mas não velocidade.

### Exemplo resolvido

O profiling mostra que o comparador do Lantern passa 70% do tempo esperando pelo disco. Kofi move o conjunto ativo de indicadores (cerca de 400.000 entradas) para a memória, reduzindo a latência de comparação de 40 ms para 3 ms por lote, e acrescenta um cache com TTL de 24 horas para as consultas de enriquecimento, a fim de ficar dentro da cota diária de consultas de um provedor.

> **Caso sintético.** Os perfis e os tempos são inventados.

### Erros e limites

Caches podem servir dados obsoletos; o TTL é uma escolha de correção, e não apenas de desempenho. Respeite os termos dos provedores sobre retenção.

### Exercícios

- **EX022 — Recurso limitante.** A CPU de um job fica em 15% enquanto a espera por disco é alta. O que o limita? *Rubrica:* 3 = E/S; mover os dados quentes para a memória ou para armazenamento mais rápido; 2 = só E/S; 1 = CPU; 0 = nenhuma.
- **EX023 — Motivos do TTL.** Dê dois motivos pelos quais um cache de enriquecimento precisa de TTL. *Rubrica:* 3 = frescor + termos de retenção/limites de taxa do provedor; 2 = um; 1 = não precisa; 0 = nenhuma.
- **EX024 — Estimativa de memória.** Estime a memória bruta para 400.000 indicadores × 200 bytes. *Rubrica:* 3 = 80 MB (com a sobrecarga mencionada); 2 = só o número; 1 = erro de fator 1000; 0 = nenhuma.

### Síntese

Saiba qual recurso limita, mantenha o conjunto quente na memória, use cache com expiração e ancore as chaves de assinatura em hardware.

### Continue estudando — capítulo 08 de 50

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 (rascunho) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar um parser como um pipeline de etapas; (2) tratar erros sem perder registros em silêncio; (3) interpretar JSON com segurança usando a biblioteca padrão; (4) escrever testes de propriedades para a normalização.

### 9.1 Pipelines

A ingestão do Lantern é uma cadeia: obter → decodificar → validar → normalizar → deduplicar → armazenar. Cada etapa recebe registros e produz registros mais rejeições. Os geradores do Python permitem que feeds grandes fluam sem carregar tudo na memória. Cada etapa pode ser testada isoladamente com uma lista curta de registros, e uma falha em uma etapa não esconde o que as outras fizeram. Os logs de Kofi mostram quantos registros entraram e saíram de cada etapa, então uma queda repentina aponta a etapa que a causou. Quando um parceiro envia um arquivo muito grande, o fluxo contínuo faz o uso de memória ficar estável, em vez de crescer com o arquivo.

### 9.2 Erros como dados

Um objeto malformado não é uma exceção a engolir; é um registro de rejeição com um motivo, a fonte e o hash dos bytes originais. As contagens de rejeições por fonte viram uma métrica de qualidade de dados sobre a qual os parceiros podem agir. Os registros de rejeição de Kofi guardam o hash, e não o conteúdo, para que dados restritos de um parceiro não sejam copiados para logs que uma equipe mais ampla pode ler. Se o mesmo motivo aparece em muitos registros de uma fonte, o parceiro provavelmente mudou algo do lado dele. O relatório enviado a ele traz contagens e exemplos, o que geralmente basta para que encontre e corrija o problema.

### 9.3 JSON seguro

`json.loads` interpreta dados sem executar código, ao contrário de avaliar texto. Limite o tamanho das entradas para evitar o esgotamento da memória e valide os tipos depois do parsing; números, strings e nulos JSON chegam em lugares inesperados. Kofi define um tamanho máximo para cada objeto antes do parsing, para que uma entrada enorme seja rejeitada em vez de encher a memória. Depois do parsing, ele verifica se cada campo tem o tipo esperado: um campo de carimbo de tempo contendo um número, ou uma lista onde se esperava uma string, é uma rejeição com motivo claro. Um código antigo que avaliava texto como programa para poupar esforço foi removido em seu primeiro mês.

### 9.4 Propriedades

Em vez de apenas testes de exemplo, declare propriedades: normalizar duas vezes é igual a normalizar uma vez (idempotência); a saída está sempre em minúsculas; nenhuma saída tem espaço em branco em nenhuma das pontas. Gere muitas entradas aleatórias e verifique se as propriedades se mantêm. As entradas aleatórias de Kofi incluem maiúsculas e minúsculas misturadas, espaços no início e no fim, strings vazias e caracteres de outros alfabetos. Um teste de propriedade descobriu que seu normalizador de domínios mantinha um ponto final, o que fazia duas formas do mesmo nome contarem como indicadores diferentes. A correção removeu algumas centenas de duplicatas do repositório.

### 9.5 Versionamento de parsers

Quando um parceiro muda seu formato de exportação, uma nova versão do parser é implantada ao lado da antiga até que a troca seja verificada. Cada objeto armazenado registra a versão do parser que o produziu. Rodar as duas versões sobre a mesma entrada por alguns dias mostra se a nova produz os mesmos registros, mais rejeições ou valores diferentes. Só quando as diferenças são compreendidas o parser antigo é desligado. Registrar a versão em cada objeto significa que, se um bug for encontrado depois, os registros afetados podem ser identificados e reprocessados, em vez de adivinhados.

### Nota de prática — Contrapressão

Quando uma etapa a jusante fica lenta, as etapas a montante não podem continuar empurrando até a memória acabar. Filas limitadas entre as etapas dão contrapressão (*backpressure*): os produtores esperam quando uma fila está cheia. O coletor do Lantern pausa as consultas quando a fila de validação está na capacidade máxima e registra a pausa, para que os operadores a vejam, em vez de descobrirem dados ausentes depois.

### Exemplo resolvido

Um parceiro envia 5.000 objetos com 37 carimbos de tempo malformados. O pipeline de Kofi armazena 4.963, grava 37 rejeições com o motivo "created not RFC 3339" e envia ao contato de qualidade de dados do parceiro um e-mail com a contagem e dois hashes de exemplo — não os objetos brutos, que são TLP:AMBER.

> **Caso sintético.** As contagens e o parceiro são inventados.

### Erros e limites

Descartar registros ruins em silêncio esconde problemas dos parceiros; corrigi-los em silêncio inventa dados. Não avalie texto não confiável como código.

### Exercícios

- **EX025 — Registro de rejeição.** Liste quatro campos que um registro de rejeição deve trazer. *Rubrica:* 3 = quatro entre motivo, fonte, hash, carimbo de tempo, versão do parser; 2 = dois; 1 = um; 0 = nenhuma.
- **EX026 — Idempotência.** Enuncie a propriedade de idempotência de um normalizador e por que ela importa. *Rubrica:* 3 = norm(norm(x)) == norm(x); reprocessar é estável; 2 = só o enunciado; 1 = errado; 0 = nenhuma.
- **EX027 — Relatório ao parceiro.** Por que enviar hashes e contagens, e não os próprios objetos malformados? *Rubrica:* 3 = TLP/minimização; o parceiro localiza pelo hash; 2 = parcial; 1 = enviar tudo; 0 = nenhuma.

### Síntese

Faça os dados fluírem por etapas, trate erros como dados, interprete com segurança, teste propriedades e registre as versões dos parsers.

### Continue estudando — capítulo 09 de 50

[← Capítulo 08 (rascunho)](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 (rascunho) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Ética e segurança na engenharia

### Objetivos de aprendizagem

Você vai (1) aplicar os deveres da ética de engenharia a sistemas de inteligência; (2) identificar os limites de privacidade e legais da OSINT; (3) projetar para falhar com segurança em um contexto de infraestrutura crítica; (4) saber quando escalar uma preocupação.

### 10.1 Deveres

Os engenheiros têm deveres para com o público, o empregador e a profissão. Em CTI, isso significa proteger as pessoas cujos dados passam pela plataforma, honrar os acordos de compartilhamento e recusar trabalho que facilite danos. Para Kofi, esses deveres são concretos. Dados pessoais que chegam em um feed ficam limitados ao que a análise precisa e são apagados no prazo. O material de parceiros marcado AMBER permanece dentro do público combinado. Se a BEN pedisse uma capacidade que pudesse ferir pessoas, como monitorar funcionários fora do trabalho, o dever para com o público prevaleceria sobre a instrução.

### 10.2 Limites da OSINT

Público não significa irrestrito. Os termos de uso das plataformas podem proibir a coleta automatizada; leis de proteção de dados como o GDPR da União Europeia se aplicam a pessoas identificáveis mesmo em publicações públicas; agregar fatos inofensivos pode criar um perfil que coloca alguém em perigo. No Brasil, a Lei Geral de Proteção de Dados Pessoais (LGPD, Lei nº 13.709/2018) cumpre esse papel e também alcança dados pessoais de acesso público (art. 7º, §§ 3º e 4º), sob fiscalização da Autoridade Nacional de Proteção de Dados (ANPD). Por isso o módulo de OSINT do Lantern coleta dados organizacionais — domínios, certificados, alertas publicados —, e não perfis sociais pessoais. Kofi confere cada nova fonte de OSINT com seus termos antes de escrever qualquer código e registra o resultado no cadastro de fontes. Uma fonte que proíbe o acesso automatizado é lida à mão, se tanto, e nada dela é armazenado em massa.

### 10.3 Falhar com segurança em uma empresa de energia

Se o Lantern enviar uma lista de bloqueio ruim aos firewalls que protegem a telemetria das subestações, poderá cortar a visibilidade operacional. O desenho de segurança: os segmentos de tecnologia operacional recebem bloqueios apenas após aprovação humana, e uma lista malformada faz o envio parar, e não limpar o firewall. O serviço de envio de Kofi verifica a lista antes de enviá-la: ela precisa ser interpretável, não pode estar vazia e não pode ter encolhido mais do que um valor definido desde o último envio. Uma verificação que falha interrompe o envio e alerta o engenheiro de plantão, enquanto o firewall mantém suas regras atuais. Para os segmentos das subestações, um operador aprova cada mudança, porque um bloqueio errado ali pode cegar a sala de controle.

### 10.4 Escalonamento

Se um gestor pede a Kofi que raspe as contas sociais dos funcionários "para encontrar pessoas de dentro", ele recusa, documenta o pedido e o escala ao encarregado de privacidade. A recusa ética faz parte da competência de engenharia. Registrar por escrito o pedido, quem o fez e o que ele fez protege tanto Kofi quanto a BEN. O encarregado de privacidade pode então decidir se há alguma preocupação legítima por trás do pedido e como tratá-la legalmente, por exemplo pelo processo de risco interno que a BEN já tem. Kofi não precisa vencer a discussão sozinho. Precisa garantir que a pessoa certa a ouça.

### 10.5 Duplo uso

Ferramentas que mapeiam a infraestrutura de um adversário também poderiam mapear a de um jornalista. Controles de acesso, limites de finalidade e logs de auditoria reduzem o mau uso. O desenho de Kofi entrega as ferramentas de mapeamento de infraestrutura a um grupo pequeno, exige uma finalidade registrada para cada consulta e registra quem buscou o quê. Uma revisão mensal amostra os logs em busca de pesquisas que não combinam com a finalidade, como nomes de pessoas em vez de domínios. Os controles não tornam o mau uso impossível, mas o tornam visível, o que dissuade a maior parte dele e permite encontrar o resto.

### Nota de prática — Códigos profissionais

As instituições de engenharia publicam códigos de conduta que põem o bem-estar público em primeiro lugar. Em um contexto de segurança, esses códigos amparam a recusa: um pedido que prejudica pessoas ou viola a lei está fora da prática profissional, mesmo que um empregador insista. Kofi mantém uma cópia do código de sua instituição ao lado da política de privacidade que ele cita nas revisões de projeto.

### Exemplo resolvido

Chega um pedido para enriquecer todo alerta interno com o endereço residencial do funcionário, "para dar contexto". Kofi pergunta que decisão precisa disso; nenhuma precisa. O campo é retirado do desenho, e a decisão é registrada com a concordância do encarregado de privacidade.

> **Caso sintético.** O pedido e a decisão são inventados.

### Erros e limites

A ética não é uma caixa a marcar no fim do projeto. Este capítulo não é aconselhamento jurídico.

### Exercícios

- **EX028 — Risco de perfil.** Por que agregar fatos públicos sobre um funcionário pode ser prejudicial, mesmo que cada um seja público? *Rubrica:* 3 = cria um perfil que possibilita perseguição/dano; deveres de proteção de dados; 2 = privacidade, de forma vaga; 1 = inofensivo; 0 = nenhuma.
- **EX029 — Envio à prova de falhas.** O que o Lantern deve fazer se a lista de bloqueio gerada para segmentos de TO falhar na validação? *Rubrica:* 3 = interromper o envio, manter a última lista boa, alertar uma pessoa; 2 = interromper o envio; 1 = enviar lista vazia; 0 = nenhuma.
- **EX030 — Raspagem interna.** Descreva a resposta correta de Kofi ao pedido de raspagem. *Rubrica:* 3 = recusar, documentar, escalar à privacidade/jurídico; 2 = só recusar; 1 = cumprir; 0 = nenhuma.

### Síntese

Proteja as pessoas, honre os termos e a lei, falhe com segurança em ambientes críticos e escale pedidos que cruzam limites.

### Continue estudando — capítulo 10 de 50

[← Capítulo 09 (rascunho)](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 (rascunho) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) explicar o HTTPS como transporte do TAXII 2.1; (2) ler os registros DNS relevantes para indicadores; (3) entender como a tradução de endereços de rede (NAT) e a hospedagem compartilhada afetam a atribuição; (4) configurar a coleta para respeitar limites de taxa.

### 11.1 TAXII sobre HTTPS

O TAXII 2.1 é uma API RESTful sobre HTTPS. Os clientes descobrem as raízes de API, listam as coleções e obtêm ou acrescentam objetos com paginação. A autenticação mútua e o TLS protegem o canal; a especificação TAXII define os endpoints e os tipos de mídia, não as relações de confiança, que vêm dos acordos. Para o Lantern, isso significa que o servidor de um parceiro apresenta um certificado que o coletor de Kofi verifica, e o coletor apresenta o próprio certificado para que o parceiro saiba quem está pedindo. Quais coleções a BEN pode ler é definido pelo acordo de compartilhamento e imposto pelo parceiro. Uma conexão válida não torna o conteúdo confiável; apenas mostra de onde ele veio.

### 11.2 DNS na inteligência

Um indicador de domínio é resolvido pelo DNS em endereços que podem mudar a cada hora. Registros A, CNAMEs e servidores de nomes contam, cada um, uma história diferente. O DNS passivo — dados históricos de resolução de provedores licenciados — mostra como a infraestrutura se moveu. Kofi registra o horário de cada resolução que o Lantern faz, porque uma resposta sem horário não pode ser comparada com nada. Um domínio que apontava para um endereço hostil no mês passado pode apontar hoje para uma página estacionada. O DNS passivo permite ao analista perguntar para onde o domínio resolvia no dia de um avistamento, que é a pergunta que uma investigação geralmente precisa responder. A licença do provedor limita por quanto tempo esse histórico pode ser guardado, e o Lantern a segue.

### 11.3 NAT e hospedagem compartilhada

Muitos dispositivos podem estar atrás de um único endereço público; muitos sites podem compartilhar um único endereço de hospedagem. Bloquear um endereço assim pode causar danos colaterais, e associar tudo o que está por trás dele a um adversário é um erro analítico clássico. A BEN enfrentou isso quando um parceiro listou um endereço usado pelo gateway compartilhado de um provedor de nuvem. Bloqueá-lo teria cortado vários serviços de que a BEN depende. O exemplo resolvido mostra o caminho mais seguro: bloquear o domínio específico na camada de DNS, onde isso não afeta outros clientes, e registrar por que o endereço não foi bloqueado. Os analistas devem dizer que um endereço hospedou conteúdo hostil, e não que ele pertence ao adversário.

### 11.4 Limites de taxa e cortesia

A coleta em servidores TAXII de parceiros segue os limites que eles publicam. Recue diante de respostas HTTP 429; nunca troque de identidade para burlar limites. Uma resposta com esse status pede ao cliente que desacelere, e muitos servidores dizem quanto tempo esperar. O coletor do Lantern respeita esse valor, dobra a espera a cada nova recusa e para depois de um número definido de tentativas, emitindo um alerta para um engenheiro. Usar muitas contas ou endereços para contornar um limite violaria o acordo e prejudicaria a reputação da BEN com o parceiro. Um coletor que respeita os limites mantém seu acesso; um que não respeita o perde.

### 11.5 Portas e protocolos no ATT&CK

A técnica T1071 Application Layer Protocol do ATT&CK descreve adversários que se comunicam por protocolos comuns para se misturar ao tráfego. Por isso, indicadores de rede sozinhos deixam escapar boa parte do comando e controle; analíticas comportamentais os complementam. Um atacante que envia comandos por tráfego web comum a um domínio recém-criado não deixa nenhum indicador que o Lantern já conheça. O que ainda pode chamar atenção é o padrão: contatos regulares em intervalos fixos, volumes incomuns de dados ou conexões de um host que nunca navega. Kofi repassa essas analíticas à equipe de detecção como complemento dos feeds de indicadores, e não como substituto.

### Nota de prática — Paginação e completude

As respostas do TAXII 2.1 podem ser paginadas. Um coletor que lê apenas a primeira página relata sucesso enquanto perde a maioria dos objetos. O Lantern segue os indicadores `more` e `next` até que o servidor informe a conclusão, e registra a contagem recebida em cada consulta, para que quedas repentinas fiquem visíveis.

### Exemplo resolvido

Kofi vê que o indicador de um parceiro resolve para um endereço compartilhado por 3.000 sites em um provedor de hospedagem. Ele o marca como "não bloquear no perímetro", encaminha-o para bloqueio do domínio específico na camada de DNS e documenta o motivo.

> **Caso sintético.** O indicador e a contagem de sites hospedados são inventados.

### Erros e limites

As respostas do DNS variam conforme o resolvedor e o momento. Nunca teste os endpoints de parceiros além do uso combinado.

### Exercícios

- **EX031 — Transporte do TAXII.** O que o TAXII 2.1 especifica, e o que precisa vir dos acordos? *Rubrica:* 3 = API/endpoints/tipos de mídia sobre HTTPS; confiança/permissões/termos de compartilhamento vêm dos acordos; 2 = uma metade; 1 = o TAXII define a confiança; 0 = nenhuma.
- **EX032 — Endereço compartilhado.** Por que bloquear o domínio, e não o endereço, no exemplo de Kofi? *Rubrica:* 3 = endereço compartilhado por muitos sites; dano colateral; o domínio é específico; 2 = parcial; 1 = bloquear o endereço; 0 = nenhuma.
- **EX033 — HTTP 429.** Qual é o comportamento correto do cliente diante de um HTTP 429 do servidor de um parceiro? *Rubrica:* 3 = recuar/respeitar o Retry-After; nunca burlar; 2 = desacelerar; 1 = trocar de IPs; 0 = nenhuma.

### Síntese

O TAXII trafega sobre HTTPS, o DNS conta histórias que dependem do tempo, endereços compartilhados enganam, e clientes corteses recuam.

### Continue estudando — capítulo 11 de 50

[← Capítulo 10 (rascunho)](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 (rascunho) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) executar serviços de inteligência sob contas de privilégio mínimo; (2) usar os logs do sistema operacional como evidência do comportamento da plataforma; (3) isolar parsers que lidam com entradas não confiáveis; (4) aplicar patches e configurar hosts para uma plataforma sempre ligada.

### 12.1 Contas de serviço

O coletor do Lantern roda com uma conta dedicada, com permissão apenas para seu diretório de trabalho e para HTTPS de saída aos servidores dos parceiros. Ele não consegue ler a configuração do firewall que acaba influenciando; um serviço separado e auditado faz isso. Se o coletor fosse comprometido por um arquivo malicioso de um parceiro, o atacante teria uma conta que só lê a própria pasta e só conversa com servidores de parceiros. Ele não poderia alterar regras do firewall nem alcançar os relatórios dos analistas. Kofi lista cada conta de serviço com suas permissões e revisa a lista depois de cada versão, removendo qualquer direito que tenha entrado para um teste e nunca tenha sido retirado.

### 12.2 Logs como evidência da plataforma

Logs de autenticação, inícios de processos e modificações de arquivos mostram o que a própria plataforma fez. Quando um parceiro pergunta se um relatório TLP:RED foi acessado, os logs do sistema operacional e da aplicação respondem. Essa pergunta exige logs que tenham sido guardados, protegidos contra alteração e sincronizados no tempo. O Lantern envia os logs dos hosts a um repositório separado, em que os administradores da plataforma podem ler, mas não apagar. Kofi testou a resposta uma vez abrindo um relatório de teste e verificando se o acesso aparecia em até um minuto, com o usuário, o horário e o objeto. Um parceiro que confia material restrito à BEN pode pedir uma verificação assim, e a BEN deve ser capaz de respondê-la com segurança.

### 12.3 Isolando parsers

Os arquivos dos parceiros são entradas não confiáveis. Os parsers rodam em um contêiner ou sandbox sem acesso à rede além do necessário, com sistemas de arquivos somente leitura sempre que possível e com limites de memória. Assim, um bug em um parser não pode virar um ponto de apoio dentro do SOC. Kofi testa o sandbox entregando ao parser um arquivo que tenta abrir uma conexão de rede e outro que tenta gravar fora de sua pasta. As duas tentativas falham e são registradas. Um teste que falhasse bloquearia a versão até que o sandbox fosse corrigido.

### 12.4 Patches

Plataformas expostas à internet precisam de patches rápidos. Uma janela de manutenção, uma imagem testada e um snapshot de reversão permitem à BEN aplicar patches toda semana sem longas interrupções. A rotina de Kofi aplica os patches primeiro em um host de teste que reproduz um dia de tráfego sintético de feeds. Se a saída do pipeline corresponde ao snapshot esperado, a mesma imagem vai para produção na janela semanal. Um snapshot tirado logo antes permite à equipe voltar ao estado anterior em minutos se algo quebrar. Correções urgentes para falhas exploradas ativamente podem pular a espera semanal, com as mesmas etapas de teste e reversão comprimidas em horas.

### 12.5 Tempo e agendamento

Timers do cron ou do systemd agendam as consultas e os recálculos de decaimento. Registre os timers no gerenciamento de configuração, para que as mudanças sejam revisadas. Um timer não revisado passa despercebido com facilidade. Kofi encontrou certa vez um job de decaimento configurado para rodar a cada minuto depois de um teste, o que carregava o banco de dados sem motivo. Como os timers agora ficam no gerenciamento de configuração, uma mudança assim aparece na revisão e na linha de base do host. Cada timer registra sua finalidade e seu responsável, para que ninguém precise adivinhar se pode ser removido. Os horários são definidos em UTC, para evitar surpresas quando os relógios mudam.

### Nota de prática — Linhas de base dos hosts

Uma linha de base lista os processos, as portas abertas e as tarefas agendadas esperados para cada host do Lantern. Uma comparação noturna sinaliza desvios: um serviço escutando inesperadamente ou um novo timer. As linhas de base ficam no gerenciamento de configuração e são revistas depois de cada mudança aprovada, para que os alertas signifiquem algo.

### Exemplo resolvido

Um pacote de arquivos de um parceiro contém um arquivo deliberadamente malformado (teste sintético). O parser trava dentro de seu sandbox; o contêiner reinicia; um registro de rejeição é gravado. Nada mais no host é afetado, e a falha aparece nos logs com o hash do arquivo, para o parceiro.

> **Caso sintético.** O arquivo malformado e o comportamento do sandbox são inventados.

### Erros e limites

Rodar tudo como root é rápido de implantar e lento de recuperar. Sandboxes reduzem o risco, mas não o eliminam.

### Exercícios

- **EX034 — Direitos do coletor.** A conta do coletor deve poder gravar regras de firewall? Explique. *Rubrica:* 3 = não; privilégio mínimo/separação; serviço separado e auditado; 2 = não; 1 = sim; 0 = nenhuma.
- **EX035 — Pergunta de acesso.** Que evidência responde "quem abriu o relatório TLP:RED?" *Rubrica:* 3 = logs de acesso da aplicação + logs de autenticação do sistema operacional; 2 = um; 1 = perguntar à equipe; 0 = nenhuma.
- **EX036 — Configurações do sandbox.** Cite três configurações de sandbox para um parser de arquivos não confiáveis. *Rubrica:* 3 = três entre rede inexistente/limitada, sistema de arquivos somente leitura, limites de memória/CPU, usuário sem privilégios; 2 = duas; 1 = uma; 0 = nenhuma.

### Síntese

Privilégio mínimo, logs como evidência, parsers em sandbox e patches disciplinados mantêm a plataforma confiável.

### Continue estudando — capítulo 12 de 50

[← Capítulo 11 (rascunho)](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 (rascunho) →](#ch-13)

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de dados

### Objetivos de aprendizagem

Você vai (1) normalizar e deduplicar indicadores antes do armazenamento; (2) escolher chaves e índices para consultas de inteligência; (3) modelar a proveniência de cada objeto armazenado; (4) projetar a retenção e a exclusão.

### 13.1 Normalização

O mesmo domínio pode chegar como `C2.Example.`, `c2.example` ou em texto desarmado. Sem normalização, o repositório se enche de duplicatas e as contagens de correspondências mentem. O laboratório mostra o efeito: sete entradas, quatro valores reais. Uma contagem baseada nas strings brutas alegaria que a BEN viu sete indicadores distintos quando viu quatro. O normalizador de Kofi passa para minúsculas onde a caixa não importa, remove o ponto final dos domínios, retira os espaços e rearma o texto, com cada etapa testada isoladamente. A ordem das etapas é fixa e documentada.

### Laboratório 4 — normalizar e deduplicar

```python
"""Lab 4 (ch 13): normalise and de-duplicate synthetic indicators before storage."""
raw = ["C2.Example.", "c2.example", "hxxp://drop[.]example/a", "http://drop.example/a",
       "203.0.113.9", " 203.0.113.9 ", "198.51.100.44"]
def norm(s):
    s = s.strip().lower().replace("hxxp", "http").replace("[.]", ".")
    return s[:-1] if s.endswith(".") else s
seen, out = set(), []
for r in raw:
    n = norm(r)
    if n not in seen:
        seen.add(n); out.append(n)
print(f"raw={len(raw)} unique={len(out)}")
for o in out:
    print(" ", o)
```

Execute com `python3 lab_dedupe.py`. Saída verificada:

```text
raw=7 unique=4
  c2.example
  http://drop.example/a
  203.0.113.9
  198.51.100.44
```

### 13.2 Lendo o resultado

Sete strings brutas se reduzem a quatro valores únicos. O ponto final, as maiúsculas, o desarme e os espaços em volta eram todos ruído. As regras de normalização precisam ser documentadas, versionadas e idempotentes. Kofi trata as regras como parte do modelo de dados. Cada regra tem um motivo escrito, um teste e um número de versão armazenado com cada registro que produziu. Rodar o normalizador sobre a própria saída deve dar o mesmo resultado, o que os testes de propriedades do capítulo de programação verificam. Se uma regra muda, os registros mais antigos podem ser encontrados pela versão e reprocessados, em vez de deixar duas formas normais diferentes no repositório ao mesmo tempo.

### 13.3 Chaves e índices

Os objetos STIX 2.1 trazem um `id` da forma `type--UUID`. O Lantern usa esse id como chave dos objetos e indexa os valores normalizados dos indicadores para comparações rápidas. Os avistamentos têm como chave o id do indicador e o horário. O identificador nunca muda, mesmo que a descrição ou a confiança do indicador mudem, então as referências feitas por relacionamentos e avistamentos continuam válidas. Os índices são escolhidos a partir das perguntas que os analistas mais fazem. Kofi mediu a velocidade de comparação com e sem o índice de valores e achou a diferença grande o bastante para justificar seu custo de armazenamento. Consultas raras podem rodar mais devagar, em vez de ganhar índices próprios.

### 13.4 Proveniência

Cada objeto registra sua fonte, o rótulo TLP, o horário da coleta e a versão do parser. Indicadores duplicados vindos de duas fontes são armazenados uma vez, com as duas entradas de proveniência, para que os analistas vejam a corroboração. A corroboração só conta se as fontes forem independentes. Se o parceiro B simplesmente copia o feed do parceiro A, duas entradas não acrescentam nada. O modelo de Kofi registra onde cada parceiro diz ter obtido um indicador, quando o parceiro informa isso, para que os analistas percebam relatos repetidos, e não independentes. O rótulo mais restritivo entre as fontes acompanha o registro compartilhado, de modo que a fusão nunca afrouxa um limite de compartilhamento.

### 13.5 Retenção

A retenção segue os acordos e a lei. A exclusão precisa chegar aos backups dentro de um prazo declarado; "apagado da interface" não é exclusão. O desenho de Kofi dá a cada fonte um período de retenção tirado de seu acordo. Um job agendado remove os registros expirados do repositório ativo, e os backups são destruídos em um ciclo fixo, de modo que um registro expirado sobrevive nas cópias de backup por, no máximo, o prazo declarado. O job grava um log das contagens removidas por fonte, que o encarregado de privacidade revisa. Se um parceiro pedir a exclusão, o mesmo log mostra quando ela foi feita.

### Nota de prática — Padrões de consulta

Os analistas fazem três tipos de pergunta: este valor existe, o que está relacionado a ele e o que mudou recentemente. Consultas de correspondência exata precisam de índices hash sobre os valores normalizados; consultas de relacionamento precisam de índices sobre os ids de origem e de destino; consultas de recência precisam de índices de tempo. Projetar os índices a partir de perguntas reais evita tanto consultas lentas quanto armazenamento desperdiçado. As exclusões em massa são ensaiadas primeiro em uma cópia, porque uma regra de normalização equivocada aplicada durante a exclusão pode remover muito mais do que o pretendido.

### Exemplo resolvido

Kofi funde os feeds de dois parceiros. A normalização revela que 18% dos indicadores do parceiro B já existem a partir do parceiro A. Em vez de descartá-los, o Lantern acrescenta a proveniência do parceiro B aos registros existentes, aumentando sua contagem de corroboração.

> **Caso sintético.** Os feeds e as porcentagens são inventados.

### Erros e limites

Uma normalização agressiva demais pode fundir valores distintos (por exemplo, caminhos de URL sensíveis a maiúsculas e minúsculas). Teste as regras com formatos reais.

### Exercícios

- **EX037 — Contagem de únicos.** Quantos valores únicos o laboratório produz a partir de sete entradas? *Rubrica:* 3 = 4; 2 = correto, com um valor listado errado; 1 = 7; 0 = nenhuma.
- **EX038 — Corroboração.** Por que manter as duas entradas de proveniência de um indicador duplicado? *Rubrica:* 3 = mostra a corroboração por fontes independentes; auditoria; 2 = só auditoria; 1 = descartar duplicatas; 0 = nenhuma.
- **EX039 — Caixa do caminho.** Dê um exemplo em que passar uma URL inteira para minúsculas poderia estar errado. *Rubrica:* 3 = caminho/consulta sensível a maiúsculas no servidor; 2 = vago; 1 = nunca está errado; 0 = nenhuma.

### Síntese

Normalize com cuidado, use ids estáveis como chave, mantenha a proveniência e torne a exclusão real.

### Continue estudando — capítulo 13 de 50

[← Capítulo 12 (rascunho)](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 (rascunho) →](#ch-14)

<a id="ch-14"></a>

## Capítulo 14 — Engenharia de software

### Objetivos de aprendizagem

Você vai (1) aplicar controle de versão, revisão de código e integração contínua a uma plataforma de CTI; (2) gerenciar dependências com cuidado de cadeia de suprimentos; (3) escrever registros de mudança ligados aos requisitos; (4) separar a configuração do código.

### 14.1 Controle de versão e revisão

Toda mudança no Lantern passa por um branch, uma execução automática de testes e a revisão de um segundo engenheiro. Mudanças em parsers precisam de um revisor que entenda o formato do parceiro. Revisar é mais do que ler código. O revisor roda os testes, verifica se a mudança corresponde ao que foi pedido e pergunta o que acontece com entradas ruins. Nas mudanças de parser, uma amostra de registros reais de parceiros, coberta pelo acordo, passa pelas duas versões. Kofi já viu revisões detectarem um campo lido da posição errada, que os testes com dados sintéticos limpos tinham deixado passar.

### 14.2 Integração contínua

A CI roda testes unitários, testes de propriedades e uma reprodução de um feed sintético pelo pipeline inteiro, comparando as saídas com um snapshot sabidamente bom. Uma diferença faz o build falhar até ser explicada. Foi a reprodução que tornou visível a mudança do exemplo resolvido: o snapshot mostrou exatamente quantos indicadores continuariam no bloqueio. Uma reprodução que falha nem sempre é um bug. Às vezes a mudança é intencional, e o engenheiro atualiza o snapshot com uma nota explicando o porquê.

### 14.3 Dependências

Bibliotecas de terceiros podem trazer vulnerabilidades ou estar comprometidas. Fixe as versões, revise as atualizações e prefira a biblioteca padrão para tarefas pequenas. A técnica T1195 Supply Chain Compromise do ATT&CK lembra aos defensores que suas próprias ferramentas são um alvo. A regra de Kofi é que cada nova biblioteca precisa de um motivo que a biblioteca padrão não atenda, de um responsável nomeado e de uma verificação de seus mantenedores e de seu histórico recente. As atualizações chegam em um lote semanal, lido antes do merge, e o build falha se uma dependência for obtida sem versão e hash fixos. O Lantern guarda dados de parceiros e influencia firewalls, o que faz de uma biblioteca comprometida em seu build uma rota atraente para um atacante.

### 14.4 Rastreabilidade

Cada mudança cita o requisito ou o defeito que trata. Quando um auditor pergunta por que o portão de TLP permite AMBER para "org", o histórico leva ao requisito e à definição do TLP 2.0. Kofi liga cada commit a um ticket, e cada ticket a um número de requisito no documento de requisitos. Um auditor consegue seguir a cadeia do código até o motivo dele em poucos cliques. Mudanças sem um motivo vinculado não entram no merge. Isso também ajuda na remoção de código: se o requisito foi retirado, o vínculo mostra quais partes podem sair.

### 14.5 Configuração

Os endpoints dos parceiros, as referências a credenciais e os limiares ficam na configuração, e não no código. Os segredos ficam em um cofre; a configuração guarda apenas referências. Separá-los significa que o mesmo código testado pode rodar em teste e em produção com configurações diferentes, e que mudar um limiar não exige um novo build. As mudanças de configuração também passam por revisão, porque um limiar errado pode causar tanto dano quanto um bug. Kofi mantém, ao lado de cada configuração, uma descrição curta do que ela controla e de quem pode alterá-la. Uma credencial nunca é colada na configuração, nem temporariamente; a referência ao cofre é a única coisa armazenada.

### Nota de prática — Notas de versão

Cada versão do Lantern sai com notas escritas para os analistas: que comportamento mudou, quais limiares se moveram e como relatar problemas. Analistas que entendem uma mudança têm menos chance de confundir o novo comportamento com um incidente, e relatam regressões mais depressa.

### Exemplo resolvido

Um pull request baixa o piso de decaimento de 30 para 20. A reprodução da CI mostra que mais 1.240 indicadores permaneceriam no bloqueio automatizado. O revisor pede o requisito; não existe nenhum. A mudança é rejeitada até que o líder do SOC concorde e um requisito seja escrito.

> **Caso sintético.** O pull request e as contagens são inventados.

### Erros e limites

Testes com dados sintéticos não provam o comportamento sobre todos os dados dos parceiros; continue amostrando formatos reais sob o acordo. A pressa é a inimiga habitual da revisão.

### Exercícios

- **EX040 — Valor da reprodução.** O que a reprodução de feed sintético na CI detecta que os testes unitários podem deixar passar? *Rubrica:* 3 = mudanças de comportamento de ponta a ponta entre as etapas; 2 = bugs de integração, de forma vaga; 1 = vago; 0 = nenhuma.
- **EX041 — Mudança rejeitada.** Por que a mudança do piso de decaimento foi rejeitada? *Rubrica:* 3 = sem requisito/acordo do responsável; grande impacto no comportamento; 2 = um; 1 = os testes falharam; 0 = nenhuma.
- **EX042 — Local dos segredos.** Onde ficam as credenciais dos parceiros, e o que a configuração guarda? *Rubrica:* 3 = cofre; a configuração guarda referências; 2 = só o cofre; 1 = no código; 0 = nenhuma.

### Síntese

Revise, reproduza, fixe versões, rastreie e mantenha os segredos fora do código.

### Continue estudando — capítulo 14 de 50

[← Capítulo 13 (rascunho)](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 (rascunho) →](#ch-15)

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de segurança

### Objetivos de aprendizagem

Você vai (1) aplicar confidencialidade, integridade e disponibilidade aos dados de inteligência; (2) definir ameaça, vulnerabilidade e risco; (3) situar a CTI nas funções do NIST CSF 2.0; (4) explicar por que a própria plataforma de CTI é um alvo.

### 15.1 CID para a inteligência

Confidencialidade: relatórios TLP:RED só podem chegar aos destinatários nomeados. Integridade: um indicador adulterado poderia bloquear um fornecedor legítimo ou, pior, o servidor de atualizações de um sistema de segurança. Disponibilidade: quando uma campanha começa, é quando os analistas mais precisam da plataforma. Kofi escreve uma nota curta para cada tipo de dado do Lantern dizendo qual das três propriedades importa mais. Os relatórios de parceiros tratam principalmente de confidencialidade, as listas de bloqueio de integridade e o serviço de comparação de disponibilidade. Os controles são escolhidos a partir dessa nota, em vez de aplicados igualmente em toda parte.

### 15.2 Ameaça, vulnerabilidade, risco

Uma ameaça é uma causa potencial de dano (um adversário ou um acidente). Uma vulnerabilidade é uma fraqueza que poderia ser usada. O risco combina probabilidade e impacto. A CTI informa o lado da ameaça: quais adversários, quais técnicas, quais alvos. Kofi mantém os termos separados em seus relatórios. Um boletim de um parceiro sobre um agente que mira empresas de energia é informação de ameaça. Um servidor de acesso remoto sem patch na BEN é uma vulnerabilidade. O risco é esse agente usar esse servidor, julgado pela probabilidade e pelo dano que isso causaria. A inteligência muda a estimativa de probabilidade; ela não corrige o servidor.

### 15.3 A CTI no CSF 2.0

O NIST CSF 2.0 organiza os resultados em Govern, Identify, Protect, Detect, Respond e Recover (governar, identificar, proteger, detectar, responder e recuperar). A inteligência de ameaças alimenta Identify (avaliação de riscos), Detect (regras) e Respond (contexto), e os acordos de compartilhamento são assunto de Govern. Situar o trabalho de inteligência nessas funções ajuda a BEN a explicar seu valor. Uma nova regra de detecção escrita a partir do relatório de um parceiro é um resultado de Detect; um briefing que muda o registro de riscos é Identify. Os acordos sobre o que a BEN pode compartilhar, com quem e sob que rótulo ficam em Govern, porque criam obrigações para a organização inteira, e não para uma equipe. Kofi marca cada saída do Lantern com a função a que ela serve.

### 15.4 A plataforma como alvo

Um adversário que envenenasse o Lantern poderia fazer a BEN bloquear os próprios fornecedores ou ignorar ameaças reais. Controles de integridade — feeds assinados quando disponíveis, reputação das fontes, verificações de anomalia no volume — protegem contra o envenenamento. As verificações de anomalia de Kofi comparam cada entrega com o histórico daquela fonte. Um salto repentino de volume, muitos indicadores para serviços conhecidos ou entradas que correspondem à lista de permissões da BEN retêm a entrega para revisão. A reputação de uma fonte cai quando entradas de um parceiro se revelam erradas depois, o que reduz a confiança de suas entregas futuras até que o histórico melhore.

### 15.5 A kill chain como mapa defensivo

Hutchins et al. argumentaram que os defensores podem agir em cada fase. As saídas do Lantern se mapeiam às fases: bloqueios de domínio para entrega e comando e controle, analíticas comportamentais para instalação e ações sobre os objetivos. O mapeamento mostra onde as defesas da BEN estão finas. Quando Kofi contou as saídas do Lantern por fase, a maioria caía em entrega e comando e controle, porque indicadores dessas fases são fáceis de compartilhar. Poucas tratavam do que um intruso faz depois de ganhar um ponto de apoio. Essa lacuna virou um pedido à equipe de detecção por analíticas comportamentais nos hosts internos.

### Nota de prática — Responsabilização

Todo bloqueio automatizado precisa ser explicável: qual indicador, qual fonte, qual confiança, qual regra. O Lantern armazena essa cadeia junto com o bloqueio, para que, quando um fornecedor reclamar, o SOC possa responder em minutos e corrigir a fonte, em vez de adivinhar.

### Exemplo resolvido

O feed de um parceiro passa de repente a incluir o domínio do próprio provedor de folha de pagamento da BEN. A verificação de anomalia de Kofi o sinaliza porque o domínio aparece na lista de permissões de fornecedores críticos da BEN. Os analistas confirmam que a entrada foi um erro do parceiro; o bloqueio teria interrompido o pagamento dos salários.

> **Caso sintético.** O erro do feed e o fornecedor são inventados.

### Erros e limites

As próprias listas de permissões podem ser abusadas; revise-as. A tríade CID é um vocabulário inicial, e não um método completo de risco.

### Exercícios

- **EX043 — Dano à integridade.** Descreva uma falha de integridade no Lantern e sua consequência operacional. *Rubrica:* 3 = indicador adulterado/envenenado → bloqueio de serviço legítimo ou ameaça não detectada; 2 = adulteração vaga; 1 = exemplo de confidencialidade; 0 = nenhuma.
- **EX044 — Lugar no CSF.** Cite duas funções do CSF 2.0 que a CTI apoia, com um exemplo de cada. *Rubrica:* 3 = duas funções com exemplos correspondentes; 2 = dois nomes; 1 = uma; 0 = nenhuma.
- **EX045 — Verificação de envenenamento.** Por que comparar o conteúdo do feed com uma lista de permissões de fornecedores críticos? *Rubrica:* 3 = detecta envenenamentos/erros que bloqueariam serviços críticos; 2 = parcial; 1 = rapidez; 0 = nenhuma.

### Síntese

Aplique a tríade CID à própria inteligência, situe a CTI no CSF e proteja a plataforma contra o envenenamento.

### Continue estudando — capítulo 15 de 50

[← Capítulo 14 (rascunho)](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 (rascunho) →](#ch-16)

<a id="ch-16"></a>

## Capítulo 16 — Engenharia de sistemas

### Objetivos de aprendizagem

Você vai (1) definir a fronteira de um sistema e suas partes interessadas; (2) escrever um conceito de operações para uma plataforma de CTI; (3) gerenciar interfaces com um documento de controle de interface; (4) planejar o ciclo de vida, do conceito à desativação.

### 16.1 Fronteira e partes interessadas

A fronteira do Lantern inclui coletores, armazenamento, enriquecimento, interface do analista e disseminação. Fora dela: servidores dos parceiros, firewalls e SIEM da BEN, o ISAC do setor. As partes interessadas incluem analistas do SOC, engenheiros de OT, o encarregado de privacidade, parceiros e executivos. Traçar a linha mostra à equipe o que ela controla e o que só pode influenciar. Um firewall fora da fronteira pode rejeitar uma regra enviada pelo Lantern, e o Lantern precisa lidar com isso em vez de presumir sucesso. Kofi encontrou uma parte interessada ausente no primeiro rascunho: a equipe de operações de rede, dona dos firewalls, que precisa concordar com toda mudança na forma como as regras chegam.

### 16.2 Conceito de operações

Um ConOps descreve, com as palavras dos operadores, como o sistema é usado: "Às 07:00 o analista de plantão revisa os indicadores de alta confiança da noite; bloqueios automáticos se aplicam apenas aos segmentos de TI; bloqueios de OT aguardam aprovação." Ele é a referência para os requisitos. Kofi escreveu o primeiro rascunho passando uma manhã ao lado da analista de plantão e anotando o que ela fazia, e depois perguntando o que ela gostaria que o sistema fizesse. Os operadores corrigiram várias etapas ao lê-lo, incluindo a ordem em que verificam os alertas da noite. Cada requisito escrito depois pode ser rastreado até uma frase dessa descrição, o que mostra por que ele existe.

### 16.3 Controle de interfaces

Cada interface — TAXII 2.1 com os parceiros, a API do SIEM, o envio aos firewalls — tem um documento de controle de interface: formatos de dados, taxas, autenticação, tratamento de erros e responsáveis dos dois lados. Sem esse documento, cada lado presume que o outro trata os erros. Kofi descobriu que a equipe do SIEM esperava que o Lantern repetisse as entregas que falhavam, enquanto o Lantern esperava que o SIEM pedisse os dados ausentes. Escrever a interface expôs a lacuna antes que uma interrupção o fizesse. Cada documento indica um contato de cada lado e é revisado sempre que um dos sistemas muda seu formato ou seus limites.

### 16.4 Ciclo de vida

Conceito, requisitos, projeto, construção, verificação, validação, operação e desativação. A desativação importa em CTI: descomissionar um feed significa avisar o parceiro, apagar os dados restritos retidos e remover as credenciais. O plano de Kofi para cada feed inclui seu fim: quem avisa o parceiro, quais registros armazenados precisam sair segundo o acordo, quais credenciais são revogadas e quais regras de firewall derivadas do feed são revisadas. Quando a BEN mais tarde abandonou um feed comercial de pouco valor, o plano transformou o que poderia ter sido uma semana confusa em uma lista de verificação concluída em dois dias.

### 16.5 Estudos de compromisso

Construir ou comprar, local ou em nuvem, plataformas de inteligência de ameaças de código aberto ou comerciais: os estudos de compromisso ponderam custo, controle, integração e risco com critérios explícitos. O estudo de Kofi para a plataforma listou primeiro os critérios e os ponderou com o líder de CTI antes de pontuar qualquer opção, para que a resposta preferida não moldasse os pesos. A integração com o SIEM existente da BEN e a capacidade de manter os dados restritos dos parceiros nos próprios servidores da BEN tiveram o maior peso. As pontuações e o raciocínio foram guardados, de modo que a decisão possa ser revista quando as circunstâncias mudarem, em vez de discutida de memória.

### Nota de prática — Mapa de partes interessadas

Kofi desenha um mapa das partes interessadas com seu interesse e sua influência. O encarregado de privacidade tem alta influência e interesse restrito; os parceiros têm influência moderada e forte interesse em reciprocidade. O mapa orienta quem revisa quais documentos e evita surpresas tardias. Kofi mantém o ConOps em quatro páginas para que os operadores realmente o leiam e corrijam.

### Exemplo resolvido

Kofi escreve o ICD do envio aos firewalls: indicadores STIX convertidos para o formato de regra do fornecedor; no máximo 5.000 regras por envio; TLS mútuo; uma falha retorna erro e mantém o conjunto de regras anterior; responsáveis — equipe do Lantern e operações de rede.

> **Caso sintético.** Os valores do ICD são inventados.

### Erros e limites

Papelada de engenharia de sistemas que ninguém lê é desperdício; mantenha os documentos curtos e em uso. Partes interessadas esquecidas aparecem tarde e saem caro.

### Exercícios

- **EX046 — Decisão de fronteira.** O servidor TAXII do ISAC do setor está dentro da fronteira do Lantern? Explique. *Rubrica:* 3 = não; interface externa de propriedade do ISAC; 2 = não; 1 = sim; 0 = nenhuma.
- **EX047 — Campos do ICD.** Liste cinco campos de um documento de controle de interface. *Rubrica:* 3 = cinco entre formato, taxa, autenticação, tratamento de erros, responsáveis, versionamento; 2 = três; 1 = um; 0 = nenhuma.
- **EX048 — Etapas de desativação.** Quais três ações desativam o feed de um parceiro? *Rubrica:* 3 = avisar o parceiro, apagar os dados restritos retidos, revogar as credenciais; 2 = duas; 1 = desligar o coletor; 0 = nenhuma.

### Síntese

Trace a fronteira, fale a língua dos operadores, controle as interfaces e planeje a desativação desde o primeiro dia.

### Continue estudando — capítulo 16 de 50

[← Capítulo 15 (rascunho)](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 (rascunho) →](#ch-17)

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de controle e realimentação

### Objetivos de aprendizagem

Você vai (1) modelar o ciclo de inteligência como um laço de realimentação; (2) identificar sensores, controladores e atuadores em um fluxo de trabalho de CTI; (3) reconhecer oscilação e atraso; (4) projetar a realimentação dos consumidores para os produtores.

### 17.1 Laços

Um termostato mede a temperatura, compara-a com um valor de referência e age. O Lantern mede as taxas de falsos positivos dos bloqueios, compara-as com uma meta e ajusta os limiares de confiança. Sem medição o laço fica aberto e deriva. A grandeza medida precisa ser uma que o laço consiga de fato mudar. O Lantern não pode alterar diretamente a qualidade do feed de um parceiro, mas pode mudar quanto peso os indicadores desse feed carregam. Kofi escolheu o limiar como valor ajustável porque movê-lo tem um efeito previsível sobre quantos bloqueios chegam aos firewalls.

### 17.2 Partes do laço

Sensor: os chamados do SOC que marcam bloqueios como falsos positivos. Controlador: a regra que sobe ou desce o limiar. Atuador: a lista de bloqueio enviada aos firewalls. Perturbação: um parceiro que de repente publica indicadores de baixa qualidade. Nomear as partes mostra por onde os erros entram. Se os analistas param de marcar falsos positivos porque o formulário do chamado é lento, o sensor silencia e o controlador vê um sistema falsamente saudável. Por isso Kofi transformou a marcação em um único clique dentro da tela do alerta. A perturbação não pode ser eliminada, mas o laço pode ser projetado para se recuperar dela em poucos dias.

### 17.3 Atraso e oscilação

Se o limiar muda todo dia com base nas reclamações de ontem, ele pode passar do ponto: rígido demais em um dia, frouxo demais no seguinte. O amortecimento — passos pequenos, média ao longo de uma semana — estabiliza o laço. Kofi simulou as duas versões com um mês de chamados antigos. Ajustes diários de tamanho cheio fizeram o limiar subir e descer quase todo dia, enquanto médias semanais com passos limitados a um valor pequeno se estabilizaram em duas semanas. O laço mais lento reage mais tarde a uma mudança real, e esse é o preço da estabilidade. Um problema grande e repentino é tratado à parte, por um analista que pausa a fonte.

### 17.4 Realimentação aos produtores

O NIST SP 800-150 incentiva relações de compartilhamento nos dois sentidos. Dizer aos parceiros quais de seus indicadores causaram falsos positivos melhora o laço de toda a comunidade, desde que respeite o TLP e os acordos. A realimentação de Kofi a um parceiro lista os identificadores dos indicadores que deram problema e o tipo de problema, como o bloqueio de um fornecedor legítimo, sem enviar o texto interno dos chamados da BEN. Parceiros que recebem esse retorno corrigiram erros recorrentes em poucas semanas. Como os indicadores vieram do próprio parceiro, devolver seus identificadores não amplia seu público.

### 17.5 Humano no laço

O controle automatizado serve para bloqueios de baixo impacto no perímetro de TI; nos segmentos de OT, uma pessoa aprova cada mudança, o que desacelera deliberadamente o laço onde os erros custam caro. Kofi mediu o custo dessa escolha. Mudanças aprovadas nos firewalls das subestações levaram uma mediana de várias horas, contra minutos nos segmentos corporativos. O gerente de operações aceitou o atraso porque um bloqueio errado em uma subestação poderia esconder a telemetria de que a sala de controle precisa. Existem caminhos rápidos para emergências, mas cada um exige um aprovador nomeado que registra o motivo.

### Nota de prática — Valores de referência vindos da política

A taxa-alvo de falsos positivos não é uma escolha só de engenharia. Os gerentes de operações decidem quanta interrupção é tolerável, e o controlador do Lantern usa esse valor de referência. Escrever o valor de referência na política faz de ajustes posteriores uma decisão governada, e não uma mudança silenciosa no código.

### Exemplo resolvido

Os chamados de falso positivo saltam de 3 para 25 depois que um parceiro acrescenta uma grande lista não verificada. O controlador de Kofi reduz o peso do parceiro em 10% por dia, com teto de 30% no total, em vez de desativá-lo de uma vez, e envia ao parceiro um resumo dos indicadores afetados.

> **Caso sintético.** As contagens de chamados e os pesos são inventados.

### Erros e limites

Os sinais de realimentação podem ser enviesados: os analistas relatam falsos positivos mais do que detecções perdidas. Meça os dois.

### Exercícios

- **EX049 — Nomeie as partes.** Identifique sensor, controlador e atuador no laço de limiar do Lantern. *Rubrica:* 3 = chamados de FP; regra do limiar; lista de bloqueio enviada; 2 = dois; 1 = um; 0 = nenhuma.
- **EX050 — Escolha de amortecimento.** Por que limitar a mudança de peso a 10% por dia? *Rubrica:* 3 = evita oscilação/reação exagerada a um sinal ruidoso; 2 = cautela, de forma vaga; 1 = mais rápido é melhor; 0 = nenhuma.
- **EX051 — Sinal enviesado.** Por que depender só de chamados de falso positivo pode enviesar o laço? *Rubrica:* 3 = ignora falsos negativos; empurra para a permissividade; 2 = parcial; 1 = não há viés; 0 = nenhuma.

### Síntese

Feche o laço com medição, amorteça-o para evitar oscilação, compartilhe a realimentação com quem produz e mantenha pessoas onde os erros custam caro.

### Continue estudando — capítulo 17 de 50

[← Capítulo 16 (rascunho)](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 (rascunho) →](#ch-18)

<a id="ch-18"></a>

## Capítulo 18 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) situar o Lantern nas zonas e conduítes da BEN; (2) projetar fronteiras de confiança entre as redes de TI, de OT e dos parceiros; (3) aplicar defesa em profundidade a uma plataforma de inteligência; (4) escolher onde os indicadores são aplicados.

### 18.1 Zonas

A BEN separa a TI corporativa, a zona do SOC, uma DMZ para trocas externas e as zonas de OT das subestações. Os coletores do Lantern ficam na DMZ; seu armazenamento e a interface do analista, na zona do SOC; nada do Lantern roda em OT. Manter o Lantern fora das zonas de OT significa que o comprometimento da plataforma não coloca um atacante ao lado dos equipamentos das subestações. Sua influência sobre a OT só chega por meio de listas de bloqueio que passam por aprovação. Os coletores ficam na DMZ porque conversam com servidores externos, o que os torna os componentes mais expostos a entradas hostis.

### 18.2 Conduítes

Os dados fluem dos coletores da DMZ para o armazenamento do SOC por um único conduíte inspecionado. As listas de bloqueio fluem do SOC para os firewalls de TI automaticamente e para os firewalls de OT por meio de um serviço de aprovação. Cada conduíte tem um responsável e um conjunto de regras. Um único conduíte é mais fácil de inspecionar e registrar do que muitas conexões espalhadas. As verificações de fluxo de Kofi comparam o tráfego observado com essa lista, de modo que qualquer caminho novo entre zonas aparece como achado. O serviço de aprovação para a OT é ele mesmo um conduíte, com seu próprio responsável em operações de rede.

### 18.3 Profundidade

Segmentação de rede, TLS mútuo entre componentes, mensagens internas assinadas, acesso baseado em papéis para os analistas e registro de auditoria formam camadas independentes. O comprometimento de um coletor não deve entregar o armazenamento. Kofi verificou isso perguntando o que um atacante em um coletor poderia fazer. Ele poderia ler a configuração do próprio coletor e enviar mensagens ao armazenamento, mas essas mensagens precisam ser assinadas com uma chave que o coletor só mantém em um serviço restrito. Uma mensagem forjada falharia nas verificações e seria registrada.

### 18.4 Pontos de aplicação

Os indicadores podem ser aplicados em resolvedores DNS, proxies web, firewalls e agentes de endpoint. Cada um tem um risco colateral diferente: o DNS bloqueia um nome com precisão; um bloqueio de firewall em um endereço compartilhado afeta muitos sites. A regra de roteamento de Kofi envia cada indicador ao ponto mais preciso capaz de agir sobre ele. Domínios vão para os resolvedores DNS, endereços web completos vão para o proxy e só endereços sem uso compartilhado conhecido vão para os firewalls. Hashes de arquivo vão para os agentes de endpoint. A escolha é registrada com o bloqueio, o que ajuda quando alguém pergunta por que um site ficou inacessível.

### 18.5 Estações de trabalho dos analistas

Os analistas abrem relatórios e amostras suspeitos. Suas estações de trabalho precisam de isolamento dos sistemas de produção e de um ambiente de navegação separado para a pesquisa OSINT, para não expor a identidade da BEN. Quando um analista visita um site suspeito a partir da rede da BEN, o operador do site pode ver um endereço registrado em nome de uma empresa de energia e descobrir que está sendo observado. O projeto de Kofi dá aos analistas um ambiente de pesquisa separado, com conexão não atribuída e sem acesso à zona do SOC. Arquivos baixados ali vão para a sandbox de análise por uma transferência controlada e nunca são abertos na estação principal.

### Nota de prática — Verificação da arquitetura

Kofi confronta o diagrama com a realidade usando registros de fluxo: toda conexão observada entre zonas precisa corresponder a um conduíte aprovado. Fluxos inesperados viram achados. Isso pega os atalhos que surgem durante incidentes e nunca são removidos. Os achados são acompanhados até que o fluxo desviante seja aprovado pelo controle de mudanças ou removido.

### Exemplo resolvido

Uma revisão de arquitetura descobre que o serviço de enriquecimento na zona do SOC chama APIs externas de consulta diretamente. Kofi move as chamadas de enriquecimento de saída para um proxy na DMZ, para que a zona do SOC não tenha acesso direto à internet.

> **Caso sintético.** O achado da revisão é inventado.

### Erros e limites

Os diagramas se afastam da realidade; verifique os fluxos com evidências da rede. O projeto de OT precisa envolver engenheiros de OT.

### Exercícios

- **EX052 — Posição em OT.** Por que nenhum componente do Lantern roda dentro das zonas de OT? *Rubrica:* 3 = manter a OT mínima/isolada; reduzir a superfície de ataque e o risco à segurança operacional; 2 = parcial; 1 = deveria rodar em OT; 0 = nenhuma.
- **EX053 — Escolha do ponto de aplicação.** Para um domínio malicioso em hospedagem compartilhada, qual ponto de aplicação é preferível e por quê? *Rubrica:* 3 = bloqueio do domínio no DNS/proxy; preciso, evita dano colateral; 2 = só o ponto; 1 = bloqueio de IP no firewall; 0 = nenhuma.
- **EX054 — Saída do enriquecimento.** Que risco foi reduzido ao mover as chamadas de enriquecimento para um proxy na DMZ? *Rubrica:* 3 = exposição direta da zona do SOC à internet/caminho de exfiltração; 2 = vago; 1 = desempenho; 0 = nenhuma.

### Síntese

Divida a plataforma em zonas, controle os conduítes, empilhe as defesas, aplique com precisão e mantenha a pesquisa dos analistas separada.

### Continue estudando — capítulo 18 de 50

[← Capítulo 17 (rascunho)](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 (rascunho) →](#ch-19)

<a id="ch-19"></a>

## Capítulo 19 — Identidade e criptografia

### Objetivos de aprendizagem

Você vai (1) autenticar parceiros e analistas com a força adequada; (2) usar assinaturas digitais para proteger a integridade dos feeds; (3) gerenciar chaves e certificados ao longo de seu ciclo de vida; (4) aplicar acesso baseado em papéis a conteúdo rotulado com TLP.

### 19.1 Identidade dos parceiros

Servidores TAXII 2.1 autenticam os clientes, em geral com autenticação HTTP sobre TLS ou com certificados de cliente. O TLS mútuo permite que os dois lados provem sua identidade. As credenciais são por parceiro, para que uma possa ser revogada sem afetar as outras. Kofi mantém um registro das credenciais dos parceiros com suas datas de expiração e responsáveis. Quando um funcionário de um parceiro sai, o parceiro pode pedir a troca da credencial sem interromper os outros feeds. Credenciais compartilhadas entre parceiros tornariam isso impossível e esconderiam qual parceiro fez determinada requisição.

### 19.2 Assinaturas

Uma assinatura sobre um pacote exportado permite ao destinatário verificar que ele veio do Lantern e não foi alterado. Calcule primeiro o hash (SHA-256), assine o hash com uma chave privada mantida em hardware e publique a chave pública por um canal confiável. Se a verificação falhar, o pacote é posto de lado e os dois lados são avisados, porque ou o conteúdo mudou no caminho ou a chave errada está em uso. A tarefa de exportação de Kofi assina automaticamente, e a impressão digital da chave pública é lida em voz alta em uma chamada com cada novo parceiro.

### 19.3 Ciclo de vida das chaves

Gerar, distribuir, usar, rotacionar, revogar, destruir. Certificados expiram; certificados expirados em um cliente TAXII interrompem a coleta no pior momento. Coloque-os na agenda e monitore-os. O exemplo resolvido mostra o custo de pular essa etapa. O registro de Kofi lista cada certificado e cada chave com sua expiração, seu responsável e as etapas de substituição, e os alertas chegam com semanas de antecedência. A revogação é testada uma vez por ano com um certificado de teste, para que a equipe saiba que as etapas funcionam antes de precisar delas. Chaves destruídas são registradas com data e método, o que um auditor pode pedir para ver.

### 19.4 Acesso dos analistas

Os papéis seguem o TLP: todos os analistas leem CLEAR e GREEN; a equipe do SOC lê AMBER; o conteúdo AMBER+STRICT fica limitado à BEN; relatórios RED vão para as pessoas nomeadas em cada relatório. As decisões de acesso são registradas. O mapeamento fica no sistema de identidade, e não no código do Lantern, de modo que mudar quem pode ler conteúdo AMBER é uma mudança de acesso com aprovação própria. Kofi revisa mensalmente a composição dos grupos com o líder do SOC. Para relatórios RED, o Lantern verifica a lista de destinatários de cada relatório em vez de um grupo, o que corresponde ao significado do rótulo: apenas pessoas nomeadas.

### 19.5 Múltiplos fatores

O acesso dos analistas ao Lantern exige MFA. A técnica T1078 Valid Accounts do ATT&CK descreve adversários que usam credenciais legítimas; o MFA aumenta o custo. Uma senha roubada, sozinha, então não abre a plataforma. Kofi escolheu chaves de hardware para os analistas com acesso a material AMBER e RED, porque códigos enviados por mensagem de texto podem ser interceptados ou desviados. Contas de serviço não podem usar um segundo fator da mesma forma, então dependem de certificados e restrições de rede. Logins a partir de dispositivos novos são registrados e revisados toda semana.

### Nota de prática — Acesso de emergência

Se o provedor de identidade falhar durante um incidente, os analistas ainda precisam do Lantern. Uma conta de emergência lacrada, com uma senha aleatória longa, guardada offline e registrada a cada uso, dá esse acesso. Seu uso dispara um alerta e uma revisão posterior, para que o acesso de emergência nunca vire rotina. Cada uso da conta de emergência é revisado em até um dia útil por alguém que não seja quem a usou.

### Exemplo resolvido

O certificado de cliente de um parceiro expira em um domingo e interrompe seu feed. Kofi acrescenta monitoramento de expiração de certificados com alertas a 30, 14 e 3 dias e documenta com o parceiro um roteiro de rotação.

> **Caso sintético.** O incidente de expiração é inventado.

### Erros e limites

Assinaturas provam origem e integridade, não a veracidade do conteúdo. Contas compartilhadas pela equipe anulam os registros de acesso.

### Exercícios

- **EX055 — Limite da assinatura.** O que uma assinatura válida em um feed prova, e o que ela não prova? *Rubrica:* 3 = origem/integridade; não a exatidão dos indicadores; 2 = uma das metades; 1 = prova a verdade; 0 = nenhuma.
- **EX056 — Acesso a RED.** Quem pode ler um relatório TLP:RED no Lantern? *Rubrica:* 3 = apenas os destinatários nomeados no relatório; 2 = uma equipe pequena; 1 = todo o SOC; 0 = nenhuma.
- **EX057 — Alertas de expiração.** Proponha um calendário de alertas para a expiração de certificados. *Rubrica:* 3 = várias antecedências (p. ex., 30/14/3 dias) + responsável; 2 = um alerta; 1 = vago; 0 = nenhuma.

### Síntese

Autentique por parceiro, assine as exportações, gerencie o ciclo de vida das chaves e associe os papéis ao TLP com acesso registrado.

### Continue estudando — capítulo 19 de 50

[← Capítulo 18 (rascunho)](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 (rascunho) →](#ch-20)

<a id="ch-20"></a>

## Capítulo 20 — Inteligência de ameaças e OSINT: contexto de engenharia

### Objetivos de aprendizagem

Você vai (1) descrever o ciclo de vida da CTI como um serviço projetado; (2) distinguir dados, informação e inteligência; (3) identificar os consumidores e suas decisões; (4) formular a missão do Lantern em uma frase.

### 20.1 Dados, informação, inteligência

Dados são observações brutas: um domínio em um feed. Informação são dados organizados: o domínio foi visto em phishing contra concessionárias. Inteligência é informação analisada e relevante para uma decisão: a BEN deve bloquear o domínio no DNS e procurar contatos passados porque a campanha mira operadores de distribuição. A diferença está na análise e na decisão. Um feed cheio de domínios continua sendo dados, por maior que seja. Kofi pergunta, de cada produto do Lantern, qual decisão ele apoia; se nenhuma, ainda não é inteligência.

### 20.2 Consumidores e decisões

Os consumidores incluem analistas do SOC (bloquear, caçar, escalar), engenheiros de OT (aprovar mudanças), gestores de risco (priorizar investimentos), executivos (aceitar riscos) e parceiros (suas próprias decisões). Cada um precisa de formatos e prazos diferentes. Kofi lista cada consumidor com a decisão que ele toma, com que rapidez precisa do insumo e em que forma. O SOC quer indicadores legíveis por máquina em minutos; os executivos querem uma página trimestral em linguagem simples. Um único produto não atende bem aos dois. A lista também mostra consumidores que ninguém atendia, como compras, que precisava de alertas sobre fornecedores.

### 20.3 A visão de serviço

O Lantern é um serviço com entradas (feeds, OSINT, telemetria interna), processamento (validação, enriquecimento, análise) e saídas (bloqueios, relatórios, objetos compartilhados). Níveis de serviço se aplicam: por exemplo, indicadores de alta confiança chegam à aplicação em TI em até 30 minutos. Pensar no Lantern como serviço lhe dá promessas mensuráveis. Uma promessa como a meta de trinta minutos pode ser verificada nos registros toda semana, e uma meta perdida vira um problema a investigar. Kofi relata mensalmente o desempenho em cada nível de serviço, o que mostra aos consumidores com o que podem contar e aos engenheiros onde trabalhar.

### 20.4 Declaração de missão

"O Lantern transforma informação de ameaças compartilhada e de fontes abertas em inteligência oportuna, confiável e coletada legalmente, que ajuda a BEN a prevenir e detectar ataques a seus ambientes de TI e OT." Todo requisito posterior deve ser rastreável até ela. Kofi testa cada funcionalidade proposta contra a declaração. Uma proposta de coletar perfis sociais pessoais de supostos agentes falha em "coletada legalmente". Uma funcionalidade que acrescenta dados que os analistas nunca usam falha em "ajuda a BEN a prevenir ou detectar". A declaração é curta o bastante para ser lembrada, e é por isso que funciona em reuniões de projeto.

### 20.5 Frameworks como contexto

O Diamond Model, a kill chain, o ATT&CK, STIX/TAXII e o TLP dão uma linguagem comum com os parceiros. A engenharia os adota onde ajudam a interoperabilidade e a análise, não como decoração. Kofi adotou os frameworks por etapas. STIX e TAXII vieram primeiro, porque os parceiros já os usavam. As marcações do ATT&CK foram acrescentadas quando os analistas foram treinados para atribuí-las de forma consistente; antes disso, as marcações eram aplicadas de modo desigual e as comparações entre relatórios enganavam. Cada framework é listado com o problema que resolve para a BEN, para que seu uso possa ser revisto.

### Nota de prática — Retorno dos consumidores

Kofi acrescenta a cada relatório do Lantern um controle de um clique, "útil / não útil". As contagens são grosseiras, mas fecham um laço que o ciclo de inteligência costuma deixar aberto e revelam quais produtos merecem investimento.

### Exemplo resolvido

Kofi entrevista cinco consumidores. O engenheiro de OT diz: "Não quero indicadores; quero saber se uma campanha mira o fornecedor dos nossos relés." Essa é uma necessidade estratégico-operacional, então o Lantern acrescenta um relatório de vigilância de fornecedores em vez de mais feeds.

> **Caso sintético.** As entrevistas são inventadas.

### Erros e limites

Mais feeds não significam mais inteligência. Missões que prometem "visibilidade completa" não podem ser verificadas.

### Exercícios

- **EX058 — Escada DII.** Classifique "domínio visto em phishing contra concessionárias". *Rubrica:* 3 = informação (contexto organizado, ainda não específico de uma decisão); 2 = certo com razão fraca; 1 = inteligência; 0 = nenhuma.
- **EX059 — Necessidade do consumidor.** Que saída atende melhor à necessidade declarada pelo engenheiro de OT? *Rubrica:* 3 = relatório/vigilância de campanhas focado no fornecedor; 2 = relatório vago; 1 = mais indicadores; 0 = nenhuma.
- **EX060 — Teste da missão.** Qual expressão da declaração de missão do Lantern compromete com a OSINT legal? *Rubrica:* 3 = "coletada legalmente" identificada; 2 = aponta para a coleta; 1 = errada; 0 = nenhuma.

### Síntese

Suba de dados para inteligência, atenda a decisões nomeadas e ancore tudo em uma missão testável.

### Continue estudando — capítulo 20 de 50

[← Capítulo 19 (rascunho)](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 (rascunho) →](#ch-21)

<a id="ch-21"></a>

## Capítulo 21 — Inteligência de ameaças e OSINT: requisitos

### Objetivos de aprendizagem

Você vai (1) coletar requisitos prioritários de inteligência (PIRs) junto às partes interessadas; (2) transformar PIRs em requisitos de sistema; (3) escrever requisitos verificáveis; (4) manter a rastreabilidade.

### 21.1 PIRs

Requisitos prioritários de inteligência são perguntas que os tomadores de decisão precisam ver respondidas: "Quais adversários miram distribuidoras de eletricidade na nossa região?" "Nossos fornecedores de OT estão sendo visados?" Eles orientam a coleta e a análise e devem ser revistos a cada trimestre. Kofi reuniu as perguntas da BEN perguntando ao CISO, ao líder do SOC e ao chefe de operações de rede o que eles gostariam de saber antes de sua próxima grande decisão. Muitas respostas se sobrepunham, e cinco perguntas cobriam quase tudo o que foi pedido. Uma pergunta sobre a qual ninguém pode agir é descartada, por mais interessante que pareça aos analistas.

### 21.2 Do PIR ao requisito de sistema

Um PIR sobre fornecedores de OT implica requisitos: ingerir os avisos dos fornecedores; marcar os objetos com o nome dos fornecedores; alertar quando uma campanha mencionar um fornecedor marcado. Cada um é uma declaração com "deve" e um método de verificação. Kofi escreve o método de verificação ao lado de cada declaração no momento em que a escreve: um teste com dados sintéticos, uma inspeção de configuração ou uma medição nos registros de produção. Se ele não consegue dizer como uma declaração seria verificada, a redação ainda não está precisa o bastante. Cada requisito também indica a pergunta a que serve, para que seu propósito continue visível depois que quem perguntou tiver seguido adiante.

### 21.3 Redação verificável

"O sistema deve ser rápido" não pode ser verificado. "O Lantern deve entregar indicadores com confiança ≥ 70 à aplicação por DNS em TI em até 30 minutos após a ingestão, para 95% dos indicadores em cada mês" pode. A segunda versão nomeia a população, o limiar, o destino, o prazo, a fração que precisa cumpri-lo e o período em que é julgada. Os registros do Lantern guardam os horários de ingestão e de entrega, então o número pode ser calculado todo mês sem esforço extra. Kofi reescreveu uma dúzia de declarações vagas nessa forma; três se mostraram impossíveis de medir com o registro atual, o que virou itens de trabalho próprios.

### 21.4 Requisitos não funcionais

Confidencialidade (aplicação do TLP), integridade (verificação de assinatura onde oferecida), disponibilidade (99,5% ao mês), privacidade (nenhuma coleta em redes sociais pessoais), retenção e auditabilidade também são requisitos, não reflexões tardias. Cada um deles é escrito e testado como qualquer declaração funcional. O requisito de privacidade, por exemplo, é verificado inspecionando o registro de fontes e o código dos coletores em busca de qualquer conector de rede social. A disponibilidade é medida por verificações de saúde a cada minuto. Deixar essas necessidades sem registro costuma significar descobri-las durante um incidente ou uma auditoria, quando mudar o projeto custa muito mais.

### 21.5 Matriz de rastreabilidade

Uma tabela liga PIRs → requisitos → elementos de projeto → testes. Quando um PIR é aposentado, seus requisitos podem ser revistos para remoção. Kofi mantém a tabela em uma planilha gerada a partir de marcações no documento de requisitos e dos nomes dos testes, de modo que ela se atualiza sozinha em vez de depender de alguém para editá-la. As lacunas saltam aos olhos: um requisito sem teste, ou um elemento de projeto que não serve a nenhum requisito. Quando a revisão trimestral aposentou uma pergunta sobre um agente regional, a tabela mostrou duas fontes de enriquecimento que existiam só para ela, e ambas foram abandonadas depois.

### Nota de prática — Revisões de requisitos

Os requisitos são revistos com as partes interessadas que são donas deles. O líder do SOC aprova os prazos, o encarregado de privacidade a minimização, o engenheiro de OT as etapas de aprovação. Um requisito sem dono é candidato à exclusão.

### Exemplo resolvido

Kofi converte o PIR sobre fornecedores de OT em quatro requisitos e escreve um teste para cada um, como "Dado um aviso sintético que nomeia o fornecedor V, o Lantern emite um alerta ao canal de OT em até 15 minutos."

> **Caso sintético.** O fornecedor V, seu aviso e o prazo de 15 minutos são inventados.

### Erros e limites

Requisitos que copiam as funcionalidades do produto de um fornecedor não são necessidades das partes interessadas. PIRs demais significam que nenhum é prioridade.

### Exercícios

- **EX061 — Reescrita verificável.** Reescreva "O Lantern deve compartilhar rapidamente com os parceiros" como requisito verificável. *Rubrica:* 3 = métrica, limiar, escopo, percentual/prazo; 2 = só a métrica; 1 = inalterado; 0 = nenhuma.
- **EX062 — Derivação de PIR.** Derive um requisito de sistema de "Quais adversários miram distribuidoras regionais?" *Rubrica:* 3 = declaração específica com "deve" (p. ex., marcar/relatar agente que mira o setor) com verificação; 2 = vago; 1 = sem relação; 0 = nenhuma.
- **EX063 — Requisito de privacidade.** Escreva um requisito de privacidade para o módulo de OSINT do Lantern. *Rubrica:* 3 = proibição/limite verificável (nenhum perfil social pessoal; só fontes organizacionais) + teste; 2 = declaração sem teste; 1 = vago; 0 = nenhuma.

### Síntese

Pergunte aos tomadores de decisão, derive "deves" verificáveis, inclua as necessidades não funcionais e rastreie tudo.

### Continue estudando — capítulo 21 de 50

[← Capítulo 20 (rascunho)](#ch-20) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 22 (rascunho) →](#ch-22)

<a id="ch-22"></a>

## Capítulo 22 — Inteligência de ameaças e OSINT: modelos de sistema e de dados

### Objetivos de aprendizagem

Você vai (1) modelar os dados do Lantern com objetos e relacionamentos STIX 2.1; (2) escolher quais objetos STIX suportar; (3) modelar procedência e confiança; (4) validar objetos contra as propriedades obrigatórias.

### 22.1 Núcleo do STIX 2.1

O STIX 2.1 define objetos de domínio (indicator, malware, threat-actor, campaign, attack-pattern, report e outros), objetos observáveis cibernéticos (domain-name, ipv4-addr, file) e objetos de relacionamento e de avistamento. Todo objeto de domínio precisa de `type`, `spec_version`, `id`, `created` e `modified`; os indicadores também precisam de `pattern`, `pattern_type` e `valid_from`. O validador do Lantern verifica essas propriedades obrigatórias em cada objeto antes de qualquer outra coisa. Indicadores são o tipo que a maioria dos parceiros envia, e seu campo de padrão contém a condição a casar, como o valor de um domínio. Kofi mantém um guia interno curto com exemplos de objetos válidos para cada tipo suportado, que os parceiros acharam útil ao depurar as próprias exportações.

### 22.2 Escolhendo um subconjunto

O Lantern suporta indicator, attack-pattern (ligado a IDs do ATT&CK por referências externas), campaign, threat-actor, malware, report, relationship e sighting. Tipos não suportados são armazenados de forma opaca e sinalizados para revisão, em vez de descartados. Kofi escolheu o subconjunto contando o que os parceiros de fato enviaram em três meses e o que os analistas de fato consultaram. Tipos que apareciam raramente e que ninguém pesquisava ficaram de fora, o que poupou a construção de telas e regras de validação para eles. Armazenar os objetos não suportados como registros opacos significa que nada se perde se surgir uma necessidade depois, e a sinalização para revisão mostra com que frequência chega cada tipo não suportado.

### 22.3 Confiança e marcações

O STIX oferece uma propriedade `confidence` (0–100) e definições de marcação, incluindo marcações TLP. O Lantern converte sua confiança interna com decaimento para essa propriedade na exportação e anexa marcações TLP 2.0 a todo objeto compartilhado. Como cada produtor define a confiança à sua maneira, o Lantern registra o valor enviado pelo parceiro ao lado de sua própria pontuação. Assim os analistas veem quando a visão da BEN difere da visão da fonte. Na exportação, a marcação TLP é escolhida pelo rótulo mais restritivo entre as fontes, e um objeto sem rótulo de sua fonte não é compartilhado até que um analista lhe atribua um.

### 22.4 Validação

Antes de armazenar, o validador verifica as propriedades obrigatórias e o formato do identificador. O laboratório de mestrado desta família de cursos verifica as mesmas regras; o Lantern as aplica no pipeline e conta as falhas por fonte. As contagens de falhas por fonte alimentam os relatórios de qualidade de dados dos parceiros. Kofi descobriu que a maioria das falhas vinha de dois parceiros, ambos enviando carimbos de tempo sem fuso horário. Uma nota curta a cada parceiro, com exemplos, resolveu o problema em um mês. O validador rejeita em vez de consertar, porque um carimbo de tempo consertado dependeria de um palpite sobre o fuso que o parceiro pretendia.

### 22.5 Modelo do sistema

Além dos dados: os componentes (coletor, validador, armazenamento, enriquecedor, interface do analista, publicador), suas interfaces e seus estados. Uma máquina de estados para um indicador — novo, ativo, decaído, aposentado — torna o comportamento explícito. A máquina de estados impede combinações estranhas, como um indicador aposentado ainda sendo enviado aos firewalls. Kofi listou cada transição permitida com seu gatilho: um objeto novo fica ativo após a validação, decai com o passar do tempo sem avistamentos e é aposentado quando cruza o piso. Um avistamento pode levar um indicador decaído de volta a ativo. Qualquer transição fora da lista é um erro e é registrada.

### Nota de prática — Mapeando referências externas

Objetos attack-pattern carregam referências externas às páginas de técnicas do ATT&CK, por exemplo T1566 Phishing. O Lantern valida que essas referências usem IDs de técnica reais, porque IDs digitados errado quebram silenciosamente os relatórios de cobertura de detecção que agrupam os achados por técnica.

### Exemplo resolvido

Um parceiro envia um objeto threat-actor sem `spec_version`. O Lantern o rejeita com um motivo, armazena o hash e avisa o contato de dados do parceiro. A exportação seguinte do parceiro inclui a propriedade.

> **Caso sintético.** O objeto e o parceiro são inventados.

### Erros e limites

O STIX é expressivo; suportar tudo acrescenta complexidade sem valor. Números de confiança de produtores diferentes não são diretamente comparáveis.

### Exercícios

- **EX064 — Extras do indicador.** Quais três propriedades um indicador precisa ter além das comuns? *Rubrica:* 3 = pattern, pattern_type, valid_from; 2 = duas; 1 = uma; 0 = nenhuma.
- **EX065 — Tipo não suportado.** Como o Lantern deve tratar um tipo STIX que não suporta? *Rubrica:* 3 = armazenar de forma opaca + sinalizar para revisão, não descartar; 2 = sinalizar; 1 = descartar; 0 = nenhuma.
- **EX066 — Máquina de estados.** Liste os estados do indicador e um gatilho de transição. *Rubrica:* 3 = novo/ativo/decaído/aposentado + gatilho válido (sem avistamentos com o tempo, aposentadoria abaixo do piso, novo avistamento); 2 = só os estados; 1 = parcial; 0 = nenhuma.

### Síntese

Use um subconjunto deliberado do STIX, valide as propriedades obrigatórias, carregue confiança e marcações TLP e torne os estados explícitos.

### Continue estudando — capítulo 22 de 50

[← Capítulo 21 (rascunho)](#ch-21) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 23 (rascunho) →](#ch-23)

<a id="ch-23"></a>

## Capítulo 23 — Inteligência de ameaças e OSINT: análise de ameaças e falhas

### Objetivos de aprendizagem

Você vai (1) modelar as ameaças à própria plataforma de CTI; (2) realizar uma análise de modos de falha e efeitos (FMEA); (3) classificar riscos por severidade, ocorrência e detecção; (4) mapear técnicas de adversários contra o Lantern usando IDs do ATT&CK.

### 23.1 Ameaças ao Lantern

Envenenamento de feeds, roubo de credenciais (T1078 Valid Accounts), comprometimento da cadeia de suprimentos de uma dependência (T1195), exfiltração de relatórios restritos e negação de serviço por feeds superdimensionados. Cada ameaça corresponde a um controle. Kofi escreveu cada ameaça como um cenário curto, com o objetivo do atacante e o caminho que ele seguiria. O envenenamento, por exemplo, poderia vir de um parceiro comprometido ou de uma entrega forjada. Escrever o caminho mostra qual controle o interrompe: verificações de assinatura barram a falsificação, mas não um parceiro comprometido, que exige verificações de anomalia. Os cenários ficam junto ao registro de riscos e são revistos quando um componente muda.

### 23.2 FMEA

Para cada componente, liste modos de falha, efeitos e causas. Pontue severidade (S), ocorrência (O) e dificuldade de detecção (D) de 1 a 10; o número de prioridade de risco RPN = S × O × D ordena a atenção. As três pontuações vêm do julgamento da equipe, informado pelo histórico de incidentes onde ele existe. Kofi conduz a pontuação com um operador, um engenheiro e um analista na sala, porque cada um enxerga falhas diferentes. O número resultante é útil para ordenar; a discussão que o produz muitas vezes importa mais, pois revela modos de falha que nenhuma pessoa sozinha havia considerado.

### 23.3 Linhas de exemplo

Coletor para em silêncio: S6, O4, D7 → RPN 168. Bloqueio errado enviado à TI: S8, O3, D4 → 96. Relatório TLP:RED compartilhado indevidamente: S9, O2, D6 → 108. A parada silenciosa do coletor fica em primeiro porque ninguém perceberia por dias. A classificação surpreendeu a equipe, que esperava ver em primeiro o relatório RED compartilhado indevidamente, porque seu dano é o maior. Sua probabilidade é baixa, e o registro de acesso o revelaria com relativa rapidez. A falha do coletor é menos grave, mas nada alerta ninguém, então o dano se acumula em silêncio enquanto os indicadores envelhecem. É esse o caso que o exemplo resolvido trata.

### 23.4 Agindo a partir da classificação

Pontuações altas de detecção pedem monitoramento: um alerta de pulsação se nenhum objeto chegar de um parceiro por seis horas. Severidade alta pede prevenção e etapas de aprovação. O alerta de pulsação de Kofi compara o histórico de chegadas de cada parceiro com o intervalo atual. Um parceiro que normalmente envia a cada hora dispara o alerta após seis horas de silêncio; um que publica uma vez por dia tem uma janela mais longa. Depois da mudança, a equipe pontuou de novo a linha e registrou o número menor com o motivo, para que o efeito do controle fique visível no registro.

### 23.5 Acidentes

Nem toda falha é maliciosa. O envio maciço por engano de um parceiro ou um erro de relógio podem causar dano. A análise de falhas cobre os dois. O registro de Kofi dá aos acidentes suas próprias linhas. Certa vez um parceiro enviou por engano um conjunto inteiro de dados de teste, cheio de domínios inofensivos. A verificação de volume reteve a entrega, e o parceiro a retirou no mesmo dia. Um relógio ajustado para o ano errado em um servidor de teste produziu indicadores que pareciam já expirados. Nenhum dos eventos envolveu um adversário, mas ambos poderiam ter perturbado a BEN.

### Nota de prática — Casos de abuso

Ao lado dos casos de uso, Kofi escreve casos de abuso: "Uma conta de parceiro envia dez milhões de objetos", "Um analista exporta um relatório RED para o e-mail pessoal". Cada caso de abuso corresponde a um controle e a um teste, o que transforma o modelo de ameaças em trabalho verificável. Os casos de abuso são revistos sempre que um novo parceiro ou uma nova interface entra na plataforma.

### Exemplo resolvido

A FMEA de Kofi mostra a parada silenciosa do coletor com RPN 168. Ele acrescenta monitoramento de pulsação por parceiro, reduzindo D para 2 e o RPN para 48, e registra a mudança no registro de riscos.

> **Caso sintético.** As pontuações são inventadas.

### Erros e limites

O RPN multiplica escalas ordinais; trate-o como auxílio de ordenação, não como medida precisa. Modelos de ameaças envelhecem; revise-os após mudanças grandes.

### Exercícios

- **EX067 — Cálculo do RPN.** Calcule o RPN para S7, O3, D5. *Rubrica:* 3 = 105; 2 = método certo; 1 = soma; 0 = nenhuma.
- **EX068 — Depois da pulsação.** Com D reduzido de 7 para 2, qual é o RPN do coletor? *Rubrica:* 3 = 48; 2 = método; 1 = errado; 0 = nenhuma.
- **EX069 — Ligação com técnica.** Qual ID de técnica do ATT&CK cobre um atacante que usa o login roubado de um analista? *Rubrica:* 3 = T1078 Valid Accounts; 2 = só o nome; 1 = errado; 0 = nenhuma.

### Síntese

Modele as ameaças à plataforma, ordene as falhas com FMEA, acrescente detecção onde as falhas são silenciosas e cubra acidentes além de adversários.

### Continue estudando — capítulo 23 de 50

[← Capítulo 22 (rascunho)](#ch-22) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 24 (rascunho) →](#ch-24)

<a id="ch-24"></a>

## Capítulo 24 — Inteligência de ameaças e OSINT: métodos I

### Objetivos de aprendizagem

Você vai (1) aplicar o Diamond Model para estruturar a inteligência de um incidente; (2) mapear o comportamento observado para técnicas do ATT&CK; (3) posicionar controles ao longo da kill chain; (4) registrar a confiança analítica e as fontes.

### 24.1 Estruturação em diamante

Para cada evento, registre o adversário (se conhecido), a capacidade (malware, técnica), a infraestrutura (domínios, endereços) e a vítima (ativo, organização). Vértices desconhecidos ficam como "desconhecido"; preenchê-los por palpite é o erro clássico. Os analistas de Kofi registram cada vértice com sua evidência. O nome da estação de trabalho da vítima vem dos registros do endpoint, a infraestrutura vem do proxy e a capacidade, do relatório da sandbox. O vértice do adversário costuma ficar vazio, e dizer isso é exato. Um nome de grupo dado por palpite se espalha depressa depois de escrito, e leitores posteriores podem tratá-lo como fato estabelecido.

### 24.2 Mapeamento no ATT&CK

Os comportamentos correspondem a IDs de técnica: e-mail de phishing → T1566; scripts no host → T1059 Command and Scripting Interpreter; C2 por protocolo web → T1071. O mapeamento apoia a engenharia de detecção e a comparação com perfis de grupos. Kofi pede aos analistas que citem a evidência de cada marcação de técnica, como a linha de registro que mostra um interpretador de scripts iniciado a partir de um anexo de e-mail. Marcações sem evidência são removidas na revisão. Uma marcação consistente permite à equipe de detecção ver quais técnicas se repetem entre incidentes e quais não têm detecção alguma, o que orienta seu trabalho no trimestre seguinte.

### 24.3 Controles na kill chain

Hutchins et al. propuseram uma matriz de cursos de ação: detectar, negar, interromper, degradar, enganar e destruir, ao longo das fases. O Lantern produz insumos para várias células — negar na entrega por filtragem de e-mail, detectar no C2 por analíticas de DNS. Kofi desenhou a matriz para os incidentes de phishing da BEN e encontrou a maioria das células vazia além de negar e detectar. Interromper o tráfego de comando, por exemplo com um sinkhole do domínio no resolvedor, era possível, mas nunca havia sido planejado. Preencher uma célula significa nomear a ação, quem é seu dono e como seu efeito seria medido. Células vazias são uma lacuna de planejamento, não necessariamente uma falha.

### 24.4 Fontes e confiança

Cada afirmação analítica cita suas fontes e sua confiança. Uma graduação de fontes no estilo Admiralty ou uma escala simples (confirmado, provável, possível) ajuda os leitores. Os relatórios de Kofi trazem uma linha curta de fonte sob cada julgamento, nomeando a evidência e sua confiabilidade, e uma palavra de confiança da tabela da equipe. O leitor consegue então distinguir uma afirmação apoiada nos próprios registros da BEN de outra apoiada em um único boletim de parceiro. Quando as fontes discordam, o relatório diz isso em vez de escolher uma em silêncio. Os revisores devolvem todo julgamento sem linha de fonte.

### 24.5 OSINT dentro dos limites

Os métodos incluem consultas de transparência de certificados em busca de domínios relacionados e a leitura de avisos públicos. Neste curso, os pesquisadores não interagem com a infraestrutura de adversários nem criam contas em fóruns criminosos. Os registros de transparência de certificados são públicos e feitos para esse tipo de busca, então procurar certificados emitidos para nomes parecidos com um domínio de phishing conhecido está dentro dos limites. Visitar os sites suspeitos não faz parte desses métodos. Kofi registra cada consulta de OSINT com seu propósito, o que mostra que a pesquisa ficou dentro dos limites acordados, caso alguém pergunte depois.

### Nota de prática — Notas analíticas

O registro em diamante de cada incidente traz uma nota analítica: o que foi observado, o que foi inferido e o que continua desconhecido. Separar essas três linhas impede que leitores posteriores confundam uma inferência com uma observação quando o registro for reutilizado meses depois. Os revisores verificam se cada linha de inferência nomeia a evidência em que se apoia.

### Exemplo resolvido

Um incidente sintético de phishing na BEN: capacidade T1566 mais um instalador por script (T1059), infraestrutura drop.example, vítima a estação de trabalho de uma atendente de faturamento, adversário desconhecido. Cursos de ação: negar a entrega com uma regra de e-mail; detectar o C2 por DNS para drop.example; caçar T1059 nas outras estações de trabalho.

> **Caso sintético.** O incidente é inventado.

### Erros e limites

O mapeamento no ATT&CK é interpretativo; dois analistas podem divergir. Mantenha a evidência ligada.

### Exercícios

- **EX070 — Vértice desconhecido.** Como o vértice do adversário deve ser registrado no incidente de Kofi, e por quê? *Rubrica:* 3 = desconhecido; evita atribuição por palpite; 2 = desconhecido; 1 = nomeia um grupo; 0 = nenhuma.
- **EX071 — IDs de técnica.** Dê os IDs de técnica do e-mail de phishing e da execução do script. *Rubrica:* 3 = T1566 e T1059; 2 = um; 1 = errado; 0 = nenhuma.
- **EX072 — Curso de ação.** Dê uma ação de negar e uma de detectar, com a fase da kill chain. *Rubrica:* 3 = negar na entrega (regra de e-mail) + detectar no C2 (DNS); 2 = uma; 1 = vago; 0 = nenhuma.

### Síntese

Estruture com o diamante, mapeie com o ATT&CK, aja ao longo da kill chain e mantenha fontes e confiança ligadas.

### Continue estudando — capítulo 24 de 50

[← Capítulo 23 (rascunho)](#ch-23) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 25 (rascunho) →](#ch-25)

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto I

### Objetivos de aprendizagem

Você vai (1) produzir um primeiro projeto de ponta a ponta para o caminho de ingestão do Lantern; (2) apresentá-lo a uma banca de revisão; (3) registrar as decisões em registros de decisão de arquitetura (ADRs); (4) responder às críticas com mudanças no projeto.

### 25.1 Enunciado do ateliê

Projete o caminho das coleções TAXII 2.1 dos parceiros até um armazenamento pronto para os analistas: consulta periódica, validação, normalização, eliminação de duplicatas, procedência, aplicação do TLP e monitoramento. Restrições: protótipos só com a biblioteca padrão, dados sintéticos, modelo de zonas da BEN. A equipe de Kofi começou desenhando as zonas e colocando cada componente em uma delas antes de escrever qualquer código. A restrição de usar só a biblioteca padrão forçou projetos simples, que a banca conseguia ler por inteiro. Os dados sintéticos permitiram que cada teste fosse compartilhado com a banca e repetido exatamente, o que dados reais de parceiros, sob limites de compartilhamento, não permitiriam.

### 25.2 ADRs

Um registro de decisão de arquitetura expõe contexto, decisão, alternativas e consequências em uma página. "Consultar a cada 15 minutos em vez de assinar envio ativo" — contexto: o TAXII 2.1 é baseado em consulta para coleções; consequências: até 15 minutos de latência. A equipe de Kofi escreveu um registro para cada escolha que alguém poderia questionar depois. O intervalo de consulta foi uma delas; a escolha de rejeitar, e não consertar, carimbos de tempo malformados foi outra. Cada registro lista as opções consideradas e por que perderam. Quando a banca contestava uma escolha, a equipe podia apontar o registro em vez de reconstruir o raciocínio de memória.

### 25.3 Revisão da banca

A banca inclui um analista, um engenheiro de OT e um encarregado de privacidade. Cada um pergunta a partir de seu papel: É oportuno? A OT está protegida? Os dados pessoais estão minimizados? Cada revisor lê o projeto a partir de suas próprias preocupações, e suas perguntas raramente se sobrepõem. O analista perguntou quanto tempo um indicador de alta confiança levaria para chegar ao DNS. O engenheiro de OT perguntou se algo no projeto poderia enviar regras aos firewalls das subestações sem aprovação. A pergunta do encarregado de privacidade levou à mudança descrita no exemplo resolvido. Kofi registrou cada pergunta com a resposta dada.

### 25.4 Iterando

A crítica vira itens de backlog. Os projetos melhoram quando os estudantes os mudam em resposta, não quando defendem cada escolha. A equipe de Kofi registrou cada comentário da banca como item de backlog com responsável e decisão. A maioria dos comentários levou a mudanças pequenas; dois levaram a novos registros de decisão; um foi recusado com um motivo escrito que a banca aceitou. A equipe descobriu que aceitar depressa uma crítica justa rendia mais confiança do que uma defesa engenhosa. A segunda revisão da banca foi mais curta porque os comentários anteriores tinham sido visivelmente atendidos.

### 25.5 Entregáveis

Um diagrama, cinco ADRs, uma lista de interfaces, um plano de monitoramento e uma demonstração do pipeline com dados sintéticos. Cada item tem um propósito. O diagrama mostra a estrutura, os registros mostram o raciocínio, a lista de interfaces mostra o que precisa ser acordado com outros e o plano de monitoramento mostra como as falhas serão percebidas. A demonstração prova que o pipeline roda de ponta a ponta com o feed sintético. A equipe de Kofi entregou os cinco juntos, para que a banca pudesse verificar se a demonstração correspondia ao diagrama e aos registros.

### Nota de prática — Disciplina na demonstração

A demonstração do ateliê roda com dados sintéticos a partir de um ambiente limpo, com os comandos roteirizados de antemão. Improvisar ao vivo diante de uma banca esconde defeitos e desperdiça tempo; uma execução roteirizada mostra o que o projeto realmente faz. Os estudantes ensaiam a execução roteirizada duas vezes antes da banca, uma delas em uma máquina nova, para que as surpresas de ambiente apareçam no ensaio e não diante dos revisores. Depois, os comentários da banca e as respostas da equipe são arquivados com os ADRs como registro do ateliê.

### Exemplo resolvido

O encarregado de privacidade pergunta por que o projeto armazena os cabeçalhos completos dos e-mails dos relatos de phishing. O ADR de Kofi não tinha motivo. Ele muda o projeto para armazenar apenas o domínio do remetente, um hash do assunto e os campos de indicador, e escreve um novo ADR registrando a mudança.

> **Caso sintético.** A banca do ateliê é inventada.

### Erros e limites

Ateliês recompensam a clareza, não o volume. Um projeto sem monitoramento está incompleto.

### Exercícios

- **EX073 — Partes do ADR.** Liste as quatro seções de um ADR. *Rubrica:* 3 = contexto, decisão, alternativas, consequências; 2 = três; 1 = uma; 0 = nenhuma.
- **EX074 — Consequência da consulta.** Indique uma consequência da consulta a cada 15 minutos. *Rubrica:* 3 = até 15 min de latência (mais a troca com a carga); 2 = latência, de forma vaga; 1 = vago; 0 = nenhuma.
- **EX075 — Minimização dos cabeçalhos.** Quais campos substituem os cabeçalhos completos de e-mail no projeto revisado? *Rubrica:* 3 = domínio do remetente, hash do assunto, campos de indicador; 2 = dois; 1 = manter os cabeçalhos completos; 0 = nenhuma.

### Síntese

Projete de ponta a ponta, registre as decisões, convide críticas baseadas em papéis e mude o projeto quando a crítica estiver certa.

### Continue estudando — capítulo 25 de 50

[← Capítulo 24 (rascunho)](#ch-24) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 26 (rascunho) →](#ch-26)

<a id="ch-26"></a>

## Capítulo 26 — Inteligência de ameaças e OSINT: alternativas de arquitetura

### Objetivos de aprendizagem

Você vai (1) comparar as opções de construir, comprar ou adotar uma plataforma comunitária de CTI; (2) conduzir um estudo de compromisso ponderado; (3) avaliar o aprisionamento e a portabilidade dos dados por meio do suporte a STIX/TAXII; (4) registrar a decisão e sua data de revisão.

### 26.1 Três opções

Opção A: estender o Lantern internamente. Opção B: comprar uma plataforma comercial de inteligência de ameaças. Opção C: adotar uma plataforma comunitária de código aberto, como o MISP, e integrá-la aos controles da BEN. Todas podem ingerir feeds e compartilhar com os parceiros; diferem em custo, controle, equipe e suporte. Kofi descreve cada opção pelo que a BEN teria de fazer por conta própria. Internamente, a BEN escreve e mantém tudo. Um produto comercial transfere a manutenção para um fornecedor, mas limita o quanto a BEN pode alterá-lo. Uma plataforma comunitária traz uma grande base de usuários e software livre, enquanto a BEN continua operando e protegendo os servidores.

### 26.2 Critérios e pesos

Kofi acorda os critérios com as partes interessadas antes de pontuar: interoperabilidade (STIX/TAXII 2.1), aplicação do TLP, fluxo de aprovação de OT, custo total em cinco anos, carga sobre a equipe, residência dos dados e custo de saída. Os pesos somam 100. Acordar os pesos primeiro impede que a opção favorita molde os critérios. Kofi conduziu a sessão de ponderação com o líder de CTI, o gerente de operações de rede e o encarregado de privacidade, e cada um defendeu os critérios mais próximos de seu trabalho. Os pesos finais foram registrados com uma frase explicando cada um, para que leitores posteriores vejam por que o fluxo de OT contou mais do que o acabamento da interface.

### 26.3 Portabilidade

Se uma plataforma não consegue exportar tudo como pacotes STIX 2.1 padrão, deixá-la depois significa perder o histórico. O custo de saída é um critério real, não uma nota de rodapé. Kofi testou a portabilidade de cada opção com o conjunto de dados sintético: carregar alguns milhares de objetos, exportá-los e comparar a exportação com o original. Uma opção perdeu os objetos de relacionamento na exportação, o que teria quebrado os vínculos de que os analistas dependem. Esse resultado baixou sua pontuação mais do que qualquer lista de funcionalidades poderia tê-la elevado. O teste leva uma tarde e deve ser repetido antes da assinatura de qualquer contrato.

### 26.4 Respostas híbridas

Estudos de compromisso costumam terminar em híbridos: uma plataforma comunitária para o compartilhamento com parceiros mais um serviço interno enxuto para aprovações de OT e envios aos firewalls. Híbridos acrescentam trabalho de integração, que também precisa ser pontuado. No exemplo resolvido o híbrido vence, mas a integração de que ele precisa é trabalho real: a plataforma comunitária precisa entregar os bloqueios aprovados ao serviço interno, e os dois precisam concordar nos identificadores. Kofi estimou esse esforço em semanas de engenheiro e o somou ao critério de custo. Sem essa etapa, um híbrido parece o melhor das duas opções sem preço extra, o que raramente é verdade.

### 26.5 Datas de revisão

Mercados e equipes mudam. O registro de decisão fixa uma data de revisão — por exemplo, em dois anos — e os gatilhos que forçariam uma revisão antecipada, como a saída do único engenheiro que conhece o código interno. Kofi também lista as evidências de que a revisão precisaria: custos efetivamente incorridos, retorno dos parceiros sobre o compartilhamento e tempo gasto em manutenção. Reunir esses números desde o início faz da revisão uma comparação, e não um debate. Uma decisão que nunca é revista tende a ser defendida muito depois de deixar de servir.

### Exemplo resolvido

Pontuações (de 100): A 68, B 71, C 74. A opção C vence por pouco em interoperabilidade e custo, mas pontua menos no fluxo de OT. Kofi recomenda C mais um pequeno serviço interno de aprovação de OT, observa que a margem está dentro da incerteza da pontuação e pede à banca que julgue explicitamente o risco de OT.

> **Caso sintético.** As pontuações e as opções são ilustrativas; nenhum fornecedor é avaliado.

### Erros e limites

Pontuações próximas são empates na prática; diga isso. Demonstrações de fornecedores com dados do próprio fornecedor provam pouco; teste com dados sintéticos parecidos com os da BEN.

### Exercícios

- **EX076 — Pesos primeiro.** Por que os pesos dos critérios precisam ser acordados antes de pontuar as opções? *Rubrica:* 3 = impede enviesar os critérios a favor de uma favorita; 2 = justiça, de forma vaga; 1 = a ordem é irrelevante; 0 = nenhuma.
- **EX077 — Custo de saída.** Como a capacidade de exportar STIX 2.1 afeta o custo de saída? *Rubrica:* 3 = exportação padrão completa reduz o custo/preserva o histórico; sua ausência o aumenta; 2 = parcial; 1 = sem relação; 0 = nenhuma.
- **EX078 — Margem estreita.** Pontuações de 71 e 74 diferem em três pontos. Como Kofi deve apresentar isso? *Rubrica:* 3 = dentro da incerteza; tratar como quase empate; expor o risco qualitativo decisivo; 2 = menciona a proximidade; 1 = vencedor claro; 0 = nenhuma.

### Síntese

Acorde os pesos primeiro, pontue a portabilidade, aceite híbridos com seu custo de integração e fixe uma data de revisão.

### Continue estudando — capítulo 26 de 50

[← Capítulo 25 (rascunho)](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 (rascunho) →](#ch-27)

<a id="ch-27"></a>

## Capítulo 27 — Inteligência de ameaças e OSINT: projeto de controles

### Objetivos de aprendizagem

Você vai (1) implementar o TLP 2.0 como controle de disseminação aplicável; (2) falhar fechado diante de rótulos desconhecidos; (3) projetar etapas de aprovação para ações de alto impacto; (4) registrar as decisões dos controles para auditoria.

### 27.1 O TLP como controle

O TLP 2.0 do FIRST define quem pode receber a informação: CLEAR sem restrição; GREEN dentro da comunidade; AMBER dentro da organização destinatária e de seus clientes, conforme a necessidade de saber; AMBER+STRICT apenas dentro da organização; RED apenas para destinatários nomeados. O Lantern transforma essas definições em uma barreira em cada exportação e em cada tela do analista. A barreira de Kofi lê o rótulo do objeto e o público da requisição e confere o par contra uma tabela derivada das definições. Manter a tabela separada do código permite a um revisor compará-la linha a linha com o padrão publicado.

### Laboratório 5 — barreira de disseminação

```python
"""Lab 5 (ch 27): TLP 2.0 dissemination gate for synthetic reports and audiences."""
ALLOWED = {
    "TLP:CLEAR": {"public", "community", "org", "team"},
    "TLP:GREEN": {"community", "org", "team"},
    "TLP:AMBER": {"org", "team"},
    "TLP:AMBER+STRICT": {"team", "org-only"},
    "TLP:RED": {"named-recipients"},
}
requests = [("R-1", "TLP:GREEN", "public"), ("R-2", "TLP:AMBER", "org"),
            ("R-3", "TLP:RED", "team"), ("R-4", "TLP:CLEAR", "public"), ("R-5", "TLP:PURPLE", "team")]
for rid, label, aud in requests:
    if label not in ALLOWED:
        verdict = "BLOCK unknown label"
    else:
        verdict = "ALLOW" if aud in ALLOWED[label] else "BLOCK"
    print(rid, label, "->", aud, verdict)
```

Execute com `python3 lab_tlp.py`. Saída verificada:

```text
R-1 TLP:GREEN -> public BLOCK
R-2 TLP:AMBER -> org ALLOW
R-3 TLP:RED -> team BLOCK
R-4 TLP:CLEAR -> public ALLOW
R-5 TLP:PURPLE -> team BLOCK unknown label
```

### 27.2 Lendo a barreira

GREEN para o público é bloqueado; AMBER para a organização é permitido; RED para uma equipe é bloqueado, porque só destinatários nomeados se qualificam; CLEAR para o público é permitido; um rótulo desconhecido, TLP:PURPLE, é bloqueado. O laboratório simplifica os públicos em categorias; as regras de produção também verificam a identidade do destinatário. Essas verificações importam sobretudo para o RED. Uma categoria como equipe deixaria passar qualquer pessoa da equipe, enquanto o rótulo permite apenas as pessoas nomeadas. A barreira de produção de Kofi consulta a lista de destinatários armazenada com cada relatório RED e a compara com a pessoa que pede acesso.

### 27.3 Falhar fechado

Rótulos desconhecidos ou ausentes precisam bloquear, não permitir. Um erro de digitação em um rótulo nunca deveria publicar conteúdo restrito. O laboratório mostra isso com o rótulo inventado, que a barreira bloqueia em vez de tratá-lo como permissivo. A barreira de Kofi também bloqueia objetos sem rótulo algum, objetos cujo rótulo tem espaços extras e objetos com dois rótulos conflitantes. Cada bloqueio registra um motivo, para que o analista que o encontrou possa pedir à fonte que corrija o rótulo. Permitir diante de um erro transformaria todo problema de qualidade de dados em um possível vazamento, que é a pior forma de a barreira falhar.

### 27.4 Etapas de aprovação

Envios aos firewalls de OT, compartilhamento além da comunidade e exclusão de indicadores são ações de alto impacto. Cada uma exige um aprovador nomeado, e a aprovação é registrada com a versão do objeto. O serviço de aprovação de Kofi mostra ao aprovador exatamente o que vai mudar: as regras a acrescentar ou remover, a fonte de cada uma e os segmentos afetados. Os aprovadores não podem aprovar os próprios pedidos. Se o objeto mudar depois da aprovação, a aprovação deixa de valer e precisa ser dada de novo, o que fecha a brecha entre o que foi revisado e o que foi enviado.

### 27.5 Auditoria

Cada decisão de permitir ou bloquear é registrada com solicitante, rótulo, público e horário. Auditores e parceiros podem então verificar se os acordos foram cumpridos. Kofi testou o registro pedindo a um colega que escolhesse dez decisões passadas ao acaso e rastreasse cada uma até a requisição e o rótulo. Todas as dez puderam ser rastreadas. O registro fica em um armazenamento que os analistas não podem editar, e sua retenção segue o acordo de compartilhamento mais longo, de modo que a pergunta de um parceiro sobre como seu material foi tratado pode ser respondida enquanto o material for mantido.

### Treinando as pessoas

Kofi conduz uma sessão curta para os analistas mostrando as decisões da barreira em exemplos sintéticos com aparência real. Quando as pessoas entendem por que o GREEN não pode chegar ao blog público, pedem aos parceiros resumos publicáveis em vez de procurar atalhos.

### Exemplo resolvido

Um analista tenta publicar no blog público da BEN um boletim GREEN de um parceiro. A barreira o bloqueia; o analista pede ao parceiro permissão para publicar em seu lugar um resumo CLEAR, que o parceiro fornece por escrito.

> **Caso sintético.** O boletim e o pedido são inventados.

### Erros e limites

Os rótulos descrevem limites de compartilhamento, não níveis de classificação no sentido governamental. Barreiras não impedem alguém de redigitar o conteúdo; treinamento e cultura continuam importando.

### Exercícios

- **EX079 — Veredictos da barreira.** Cite os veredictos do laboratório para R-1 e R-3. *Rubrica:* 3 = R-1 BLOCK (GREEN para o público), R-3 BLOCK (RED para a equipe); 2 = um; 1 = permitir; 0 = nenhuma.
- **EX080 — Rótulo desconhecido.** Por que R-5 bloqueia em vez de permitir? *Rubrica:* 3 = rótulo desconhecido → falhar fechado; 2 = desconhecido; 1 = deveria permitir; 0 = nenhuma.
- **EX081 — Registro da aprovação.** O que precisa ser armazenado com um envio aprovado a um firewall de OT? *Rubrica:* 3 = aprovador, horário, versão da regra/do objeto, motivo; 2 = dois; 1 = vago; 0 = nenhuma.

### Síntese

Codifique o TLP como barreira, falhe fechado, exija aprovação para ações de alto impacto e registre cada decisão.

### Continue estudando — capítulo 27 de 50

[← Capítulo 26 (rascunho)](#ch-26) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 28 (rascunho) →](#ch-28)

<a id="ch-28"></a>

## Capítulo 28 — Inteligência de ameaças e OSINT: implementação I

### Objetivos de aprendizagem

Você vai (1) implementar uma etapa de cliente TAXII 2.1 contra um servidor substituto sintético; (2) implementar as etapas de validação e normalização; (3) ligar as etapas com filas limitadas; (4) produzir métricas visíveis ao operador desde a primeira versão.

### 28.1 Etapa do cliente

O cliente descobre a raiz da API, lista as coleções permitidas e pede os objetos acrescentados depois do último ponto de controle salvo. Ele segue a paginação até o fim e só armazena o novo ponto de controle depois que o lote foi gravado com segurança, de modo que uma queda causa uma nova busca, e não uma lacuna. A ordem importa, como mostra o exemplo resolvido. Um ponto de controle salvo antes da gravação marca como recebidos objetos que não foram. Salvar depois da gravação significa que uma queda entre as duas etapas busca alguns objetos duas vezes, o que o armazenamento suporta porque as gravações são indexadas pelo identificador e gravações repetidas não mudam nada.

### 28.2 Validação e normalização

A validação impõe as propriedades obrigatórias do STIX e o formato do identificador. A normalização aplica as regras documentadas no Capítulo 13. As duas etapas emitem rejeições com motivos. Rodar a validação antes da normalização significa que as regras de formato são verificadas sobre o que o parceiro de fato enviou. Normalizar primeiro poderia esconder um valor malformado, transformando-o em algo que parece válido. Os registros da etapa de Kofi mostram contagens por fonte e por motivo, que viram os relatórios de qualidade dos parceiros. Um registro rejeitado aqui nunca chega ao armazenamento, então nenhum analista vê um valor limpo pela metade.

### 28.3 Filas

Filas limitadas ligam as etapas. Se o enriquecimento fica lento, a validação enche sua fila de saída e espera; o cliente pausa. Isso protege a memória e torna a lentidão visível. Kofi escolheu os tamanhos das filas a partir do uso de memória medido por objeto e de um limite que deixa espaço para o resto do host. Quando uma fila fica cheia por mais de alguns minutos, um alerta diz ao operador qual etapa está lenta. Filas ilimitadas esconderiam a lentidão até a memória acabar e o coletor inteiro parar de uma vez.

### 28.4 Métricas desde o primeiro dia

Objetos recebidos, aceitos e rejeitados por fonte; profundidade das filas; idade do ponto de controle; duração da consulta. Métricas são baratas de acrescentar cedo e caras de adaptar depois. Kofi acrescentou esses contadores na primeira semana, antes de qualquer trabalho de desempenho. Em poucos dias eles mostraram que as consultas a um parceiro demoravam muito mais que as demais, o que se revelou um servidor lento do lado do parceiro, e não um problema do Lantern. Sem a métrica de duração da consulta, a equipe poderia ter passado dias analisando o código errado. Cada métrica tem uma descrição curta e um responsável no painel.

### 28.5 Servidor substituto sintético

O desenvolvimento usa um substituto local que serve pacotes STIX sintéticos no formato TAXII 2.1. Nenhum tráfego de desenvolvimento toca os servidores dos parceiros, o que protege os parceiros e mantém os testes reproduzíveis. O substituto serve pacotes fixos a partir de arquivos, incluindo malformados para testes de erro, e pode ser instruído a responder devagar ou a recusar requisições. Isso permite à equipe testar tempos limite e recuos sem pedir a um parceiro um servidor quebrado. Como os pacotes são fixos, um teste que passa hoje passará amanhã, a menos que o código tenha mudado.

### Configuração dos parceiros

Cada entrada de parceiro na configuração indica a raiz da API, as coleções, o intervalo de consulta, a referência da credencial e o contato de dados. Acrescentar um parceiro é uma mudança de configuração revisada, não uma mudança de código, o que mantém genérica a etapa do cliente e torna auditável a própria lista de parceiros. Remover um parceiro segue as etapas de desativação do Capítulo 16.

### Exemplo resolvido

Na primeira execução de teste, o cliente salvou o ponto de controle antes de gravar o lote; uma queda forçada então perdeu 200 objetos. Kofi inverte as etapas — gravar, depois salvar o ponto de controle — e acrescenta um teste que provoca uma queda entre elas e verifica que nada se perde.

> **Caso sintético.** O defeito e as contagens são inventados.

### Erros e limites

Entrega exatamente uma vez é difícil; projete para pelo menos uma vez com gravações idempotentes. Testar contra servidores reais de parceiros não é aceitável no desenvolvimento.

### Exercícios

- **EX082 — Ordem do ponto de controle.** Por que o ponto de controle precisa ser salvo depois que o lote é gravado? *Rubrica:* 3 = senão uma queda perde objetos; buscar de novo é seguro com gravações idempotentes; 2 = parcial; 1 = a ordem é irrelevante; 0 = nenhuma.
- **EX083 — Razão do substituto.** Dê duas razões para desenvolver contra um substituto TAXII sintético. *Rubrica:* 3 = nenhuma carga/risco para os parceiros + testes reproduzíveis; 2 = uma; 1 = só mais rápido; 0 = nenhuma.
- **EX084 — Métrica precoce.** Qual métrica revela um coletor parado, e por quê? *Rubrica:* 3 = idade do ponto de controle / objetos recebidos por fonte; sobe ou cai a zero quando parado; 2 = só a métrica; 1 = CPU; 0 = nenhuma.

### Síntese

Salve o ponto de controle depois de gravar, valide e normalize com rejeições, limite as filas e entregue métricas com a primeira versão.

### Continue estudando — capítulo 28 de 50

[← Capítulo 27 (rascunho)](#ch-27) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 29 (rascunho) →](#ch-29)

<a id="ch-29"></a>

## Capítulo 29 — Inteligência de ameaças e OSINT: medição

### Objetivos de aprendizagem

Você vai (1) medir a qualidade de um feed com precisão, revocação e F1 contra um conjunto rotulado; (2) construir um conjunto rotulado de avaliação de forma ética; (3) medir oportunidade e exclusividade; (4) relatar as métricas com seus limites.

### 29.1 Conjuntos rotulados

Para medir um feed, compare-o com a verdade de referência: indicadores confirmados como maliciosos em incidentes da BEN ou em investigações de parceiros confiáveis, mais valores confirmados como benignos. Os rótulos vêm de investigações concluídas, e não do próprio feed, para evitar circularidade. Usar as próprias entradas do feed como verdade faria qualquer feed parecer perfeito. O conjunto rotulado de Kofi se apoia em investigações encerradas nas quais um analista confirmou se um valor era hostil. Os rótulos benignos vêm da lista de permissões de fornecedores conhecidos da BEN e de valores investigados e liberados. Cada rótulo registra quem o atribuiu e quando.

### Laboratório 6 — avaliação de feed

```python
"""Lab 6 (ch 29): precision and recall of a synthetic feed against a labelled ground-truth set."""
truth_bad = {"a.example", "b.example", "c.example", "d.example", "e.example"}
feed = {"a.example", "b.example", "c.example", "x.example", "y.example", "z.example"}
tp = len(feed & truth_bad); fp = len(feed - truth_bad); fn = len(truth_bad - feed)
p, r = tp / (tp + fp), tp / (tp + fn)
print(f"TP={tp} FP={fp} FN={fn}")
print(f"precision={p:.2f} recall={r:.2f} F1={2*p*r/(p+r):.2f}")
```

Execute com `python3 lab_feedeval.py`. Saída verificada:

```text
TP=3 FP=3 FN=2
precision=0.50 recall=0.60 F1=0.55
```

### 29.2 Lendo as pontuações

Três das seis entradas do feed são confirmadas como maliciosas (precisão 0,50); ele encontrou três de cinco valores maliciosos conhecidos (revocação 0,60); o F1 é 0,55. Metade do feed seria ruído se fosse bloqueada diretamente. As pontuações respondem a perguntas diferentes. A precisão diz à BEN quantos bloqueios vindos desse feed seriam equivocados. A revocação diz quanto da atividade hostil conhecida o feed teria pego. Um feed com revocação alta e precisão baixa ainda pode ajudar como fonte de enriquecimento, que é como o exemplo resolvido acaba usando-o.

### 29.3 Oportunidade e exclusividade

Um feed que lista indicadores uma semana depois que a BEN os viu tem pouco valor operacional. Meça a antecedência mediana em relação ao primeiro avistamento interno. A exclusividade — indicadores que nenhuma outra fonte fornece — mostra o valor marginal. Kofi mede a antecedência como a diferença entre o horário de publicação do feed e o primeiro avistamento do mesmo valor pela BEN. Uma antecedência positiva significa que o feed avisou a BEN com antecedência; uma negativa significa que chegou depois do fato. A exclusividade é medida contra todas as outras fontes do Lantern no mesmo período, já que um feed que duplica os outros acrescenta pouco, mesmo com qualidade alta.

### 29.4 Limites

A verdade de referência é incompleta: valores maliciosos desconhecidos contam como falsos positivos quando apenas não foram confirmados. Relate o período de avaliação, o tamanho do conjunto e o método de rotulagem com cada número. Por isso Kofi relata a precisão como limite inferior quando entradas não confirmadas são contadas como falsas. Ele também anota quantas entradas do feed não puderam ser rotuladas. Com um conjunto pequeno, um único valor rerrotulado pode mover as pontuações de forma perceptível, então o relatório traz as contagens por trás de cada razão. Os leitores podem então julgar quanto peso os números merecem.

### 29.5 Usando os resultados

As métricas alimentam os pesos das fontes no modelo de confiança do Lantern e informam as decisões de renovação de feeds pagos. Elas são compartilhadas com os parceiros de forma agregada quando os acordos permitem, apoiando a reciprocidade descrita no NIST SP 800-150. Kofi muda os pesos das fontes em passos pequenos e registra a avaliação que justificou cada mudança. A renovação de um feed pago depende das pontuações ao longo de um período contratual completo, e não de um trimestre. Quando a BEN compartilha resultados agregados com um parceiro, o parceiro descobre como seu feed se comporta no ambiente da BEN, o que o ajuda a melhorar sem expor detalhes dos incidentes da BEN.

### Amostragem para rótulos

Rotular todos os indicadores é impossível. Kofi sorteia uma amostra aleatória estratificada por tipo de indicador, rotula-a a partir dos registros de investigação e relata intervalos de confiança. Uma amostra de algumas centenas, sorteada honestamente, vale mais que uma enorme amostra de conveniência com o que por acaso foi investigado.

### Exemplo resolvido

Kofi avalia um feed pago ao longo de um trimestre: precisão 0,50, revocação 0,60, antecedência mediana de −2 dias (ele chega depois dos avistamentos internos). Ele recomenda mantê-lo apenas como fonte de enriquecimento e não renovar o nível premium.

> **Caso sintético.** Os valores do feed são inventados.

### Erros e limites

Conjuntos rotulados pequenos dão estimativas instáveis. Não publique pontuações de fornecedores nomeados a partir de dados licenciados.

### Exercícios

- **EX085 — Citação das pontuações.** Cite a precisão, a revocação e o F1 do laboratório. *Rubrica:* 3 = 0,50, 0,60, 0,55; 2 = dois; 1 = um; 0 = nenhuma.
- **EX086 — Rótulo circular.** Por que os rótulos não podem vir do feed avaliado? *Rubrica:* 3 = a circularidade infla a precisão; 2 = viés, de forma vaga; 1 = tudo bem; 0 = nenhuma.
- **EX087 — Antecedência negativa.** O que uma antecedência mediana de −2 dias significa operacionalmente? *Rubrica:* 3 = o feed chega depois da detecção interna; pouco valor preventivo; 2 = atrasado; 1 = adiantado; 0 = nenhuma.

### Síntese

Meça contra rótulos independentes, acrescente oportunidade e exclusividade e relate cada métrica com seus limites.

### Continue estudando — capítulo 29 de 50

[← Capítulo 28 (rascunho)](#ch-28) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 30 (rascunho) →](#ch-30)

<a id="ch-30"></a>

## Capítulo 30 — Laboratório de verificação I

### Objetivos de aprendizagem

Você vai (1) escrever procedimentos de verificação rastreáveis até os requisitos; (2) executá-los com dados sintéticos; (3) registrar resultados de aprovação, falha e desvio; (4) distinguir verificação ("construído certo") de validação ("a coisa certa").

### 30.1 Verificação versus validação

A verificação confere se o Lantern atende aos requisitos escritos. A validação, no Capítulo 38, confere se ele atende às necessidades reais das partes interessadas. Uma plataforma pode passar na verificação e ainda falhar na validação se os requisitos estiverem errados. Kofi mantém as duas atividades em planos separados, com responsáveis separados. A verificação é conduzida pela equipe de engenharia contra o documento de requisitos. A validação envolve as pessoas que usam o Lantern e pergunta se ele ajuda no trabalho delas. Um requisito que passa na verificação, mas falha na validação, é evidência de que o próprio requisito precisa mudar.

### 30.2 Procedimentos

Cada procedimento indica o requisito, as pré-condições, os passos, o resultado esperado e os critérios de aprovação. "Carregar o pacote S-07 com 1.000 indicadores, dos quais 12 sem valid_from válido; esperar 988 armazenados e 12 rejeitados com motivo; aprovar se as contagens baterem exatamente." O exemplo mostra o nível de detalhe necessário: um pacote nomeado, contagens exatas e uma regra de aprovação clara. Duas pessoas que o sigam devem obter o mesmo resultado. Kofi escreve o procedimento antes de executá-lo, para que o resultado esperado não possa ser moldado pelo que o sistema por acaso produzir no dia.

### 30.3 Cobertura

A matriz de rastreabilidade mostra quais requisitos têm procedimentos. Requisitos descobertos são listados explicitamente; um requisito não testado é um risco aberto, não uma aprovação silenciosa. O relatório de cobertura de Kofi lista cada requisito com seus procedimentos e seu último resultado. Na primeira execução, vários requisitos não tinham procedimento, a maioria não funcionais, como a retenção. Cada lacuna foi preenchida com um procedimento ou registrada como risco aceito, com responsável e data de revisão. Ninguém podia marcar como atendido um requisito não testado.

### 30.4 Desvios

Quando um resultado difere, registre um desvio com severidade e responsável. Não edite o resultado esperado para casar com a saída sem uma mudança de requisito. Cada desvio registra o procedimento, o que era esperado, o que aconteceu e a evidência. A severidade segue o efeito sobre os usuários: uma falha na barreira de TLP é alta porque poderia vazar dados restritos; uma métrica ausente é menor. Kofi revisa semanalmente com a equipe os desvios abertos e só fecha cada um depois que o procedimento foi executado de novo e aprovado.

### 30.5 Evidências

Registros, instantâneos de métricas e hashes das saídas são armazenados com a execução do procedimento. Um revisor pode executar o mesmo procedimento com os mesmos dados sintéticos e comparar os hashes. Os hashes tornam a comparação rápida: se o arquivo de saída tem o mesmo hash da execução armazenada, o resultado é idêntico. Kofi guarda os dados sintéticos, a versão do código e a configuração com cada execução, para que um revisor meses depois possa reproduzi-la exatamente. Evidências que não podem ser reproduzidas pesam muito menos em uma auditoria.

### Suíte de regressão

Procedimentos aprovados viram testes de regressão automatizados executados a cada mudança. A suíte cresce com cada defeito corrigido, de modo que o mesmo erro não pode voltar em silêncio. Kofi marca cada teste com o ID de seu requisito, o que mantém a matriz de rastreabilidade atualizada sem esforço manual e mostra num relance quais requisitos perderam cobertura quando um teste foi removido.

### Exemplo resolvido

Kofi executa 42 procedimentos. 38 passam, 3 falham (a barreira de TLP permitiu um rótulo com espaço no final; faltou o motivo de rejeição para um tipo de erro; a métrica do ponto de controle não foi exportada) e 1 fica bloqueado pela falta de um dado de teste. Cada falha vira um defeito com responsável; o bloqueado é agendado.

> **Caso sintético.** As contagens e os defeitos são inventados.

### Erros e limites

Uma execução de testes toda verde com dados sintéticos não prova robustez diante de todos os formatos de parceiros; amplie os dados de teste à medida que surgem formatos. Não conte procedimentos bloqueados como aprovados.

### Exercícios

- **EX088 — V e V.** Em uma frase cada, defina verificação e validação. *Rubrica:* 3 = construído conforme os requisitos; atende às necessidades reais; 2 = uma; 1 = trocadas; 0 = nenhuma.
- **EX089 — Espaço no final.** Por que uma barreira de TLP que aceita "TLP:AMBER " (com um espaço) é um defeito? *Rubrica:* 3 = tratamento inconsistente do rótulo; deveria normalizar ou falhar fechado conforme o requisito; 2 = parcial; 1 = inofensivo; 0 = nenhuma.
- **EX090 — Contagem do bloqueado.** Como o procedimento bloqueado deve ser relatado? *Rubrica:* 3 = à parte, como bloqueado/não executado, com plano; não é aprovação; 2 = não aprovado; 1 = aprovado; 0 = nenhuma.

### Síntese

Verifique contra os requisitos escritos com procedimentos rastreáveis, registre os desvios com honestidade e mantenha as evidências reexecutáveis.

### Continue estudando — capítulo 30 de 50

[← Capítulo 29 (rascunho)](#ch-29) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 31 (rascunho) →](#ch-31)

<a id="ch-31"></a>

## Capítulo 31 — Inteligência de ameaças e OSINT: implementação II

### Objetivos de aprendizagem

Você vai (1) implementar o enriquecimento com cache e respeito aos termos dos provedores; (2) implementar a ingestão de avistamentos a partir da telemetria interna; (3) calcular a confiança com decaimento na leitura; (4) publicar de volta aos parceiros os objetos aprovados por analistas.

### 31.1 Enriquecimento

O enriquecimento acrescenta contexto: o dono interno do ativo de um endereço, o histórico de DNS passivo de um domínio, ligações a técnicas do ATT&CK para uma família de malware. Provedores externos de enriquecimento têm termos sobre volume de consultas, retenção e redistribuição. O enriquecedor do Lantern registra qual provedor forneceu cada campo, para que as regras de redistribuição possam ser aplicadas na exportação. O enriquecimento interno costuma ser o mais útil. Saber que um endereço contatado pertence ao notebook de um engenheiro de subestação muda na hora a prioridade de um avistamento. O enriquecedor de Kofi consulta primeiro as fontes internas.

### 31.2 Avistamentos

Quando o resolvedor DNS ou o proxy da BEN vê um indicador, o Lantern registra um objeto sighting do STIX 2.1 que referencia o indicador, com os horários da primeira e da última observação e uma contagem. Os avistamentos aumentam a confiança e dão aos parceiros um retorno valioso quando compartilhados conforme o acordo. O gravador de avistamentos de Kofi agrupa ocorrências repetidas dentro de uma hora em um só objeto com contagem, para que um indicador muito ativo não produza milhares de registros. O objeto registra qual sensor da BEN o viu, usando um identificador interno em vez de um nome de host. Isso mantém a topologia da rede interna fora de tudo o que possa ser compartilhado depois.

### 31.3 Confiança na leitura

Em vez de reescrever todos os registros toda noite, o Lantern armazena c₀ e o horário do último avistamento e calcula a confiança com decaimento quando consultado. Isso evita atualizações em massa e mantém a mudança de modelo em uma única função. Calcular na leitura também significa que mudar uma meia-vida vale imediatamente para todos os indicadores, sem migração. O custo é um pouco de processamento na hora da consulta, que Kofi mediu como desprezível perto da própria busca. As exportações e o envio aos firewalls chamam a mesma função, então todo consumidor vê a mesma pontuação para o mesmo indicador no mesmo momento. Um teste compara os resultados da função com os valores impressos pelo laboratório de decaimento.

### 31.4 Publicação

Os analistas aprovam objetos para compartilhamento com uma marcação TLP. O publicador remove os campos de enriquecimento cujo provedor proíbe a redistribuição, assina o pacote e o acrescenta à coleção TAXII da comunidade. A etapa de aprovação é onde um analista confere se o objeto diz o que deveria e se seu rótulo está certo. O publicador então aplica as regras mecânicas sem exceções. Os testes de Kofi incluem um objeto com um campo de DNS passivo licenciado e falham se esse campo aparecer no pacote assinado. Os analistas veem na interface quais campos serão removidos antes de aprovar.

### 31.5 Dados pessoais na telemetria

Os avistamentos vêm de sistemas que sabem de qual funcionário era a máquina que fez uma requisição. O Lantern armazena o identificador do ativo, não a pessoa, e compartilha para fora apenas contagens agregadas. Um analista que investiga um avistamento ainda pode chegar à pessoa pelo registro de ativos da BEN, mas essa consulta acontece nas ferramentas do próprio SOC, sob suas regras de acesso, e não no Lantern. Kofi fez essa escolha de projeto depois que o encarregado de privacidade observou que os dados do Lantern são compartilhados mais amplamente que os arquivos de casos do SOC. Os relatórios para fora trazem contagens por tipo de ativo, como estações de trabalho ou servidores, e nunca uma lista de máquinas.

### Nota de prática — implantação gradual

Novas etapas entram em produção atrás de uma chave de funcionalidade, primeiro para uma fração do tráfego. Kofi compara as métricas entre os caminhos com e sem a chave durante uma semana antes da implantação completa.

### Exemplo resolvido

Um parceiro pede os avistamentos de seus indicadores. O Lantern exporta objetos sighting com contagens e intervalos de tempo, mas sem nomes de host internos nem nomes de usuário, marcados como TLP:AMBER conforme o acordo com o parceiro. O parceiro informa que dois de seus indicadores não tiveram avistamentos em toda a comunidade e os aposenta.

> **Caso sintético.** A troca é inventada.

### Erros e limites

Redistribuir enriquecimento licenciado pode violar contratos. Avistamentos podem revelar a exposição de um membro; compartilhe apenas conforme acordado.

### Exercícios

- **EX091 — Campo do provedor.** Por que registrar o provedor de cada campo de enriquecimento? *Rubrica:* 3 = aplicar os termos de redistribuição/retenção na exportação; 2 = auditoria; 1 = sem motivo; 0 = nenhuma.
- **EX092 — Conteúdo do avistamento.** O que o Lantern compartilha nos objetos sighting, e o que remove? *Rubrica:* 3 = contagens/intervalos de tempo/referência ao indicador; remove nomes de host/usuários; 2 = uma das metades; 1 = tudo; 0 = nenhuma.
- **EX093 — Cálculo na leitura.** Dê uma vantagem de calcular a confiança com decaimento na leitura. *Rubrica:* 3 = sem reescritas noturnas em massa/função única do modelo; 2 = eficiência, de forma vaga; 1 = tentativa mínima; 0 = nenhuma.

### Síntese

Enriqueça dentro dos termos dos provedores, registre avistamentos sem pessoas, calcule o decaimento na leitura e publique apenas o que pode ser compartilhado.

### Continue estudando — capítulo 31 de 50

[← Capítulo 30 (rascunho)](#ch-30) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 32 (rascunho) →](#ch-32)

<a id="ch-32"></a>

## Capítulo 32 — Inteligência de ameaças e OSINT: confiabilidade

### Objetivos de aprendizagem

Você vai (1) calcular a disponibilidade de pipelines em série; (2) quantificar o efeito da redundância; (3) definir objetivos de nível de serviço com orçamentos de erro; (4) decidir onde o investimento em confiabilidade compensa.

### 32.1 Disponibilidade em série

Uma requisição que precisa passar por todas as etapas só tem sucesso se todas estiverem no ar, então as disponibilidades se multiplicam. Quatro etapas que parecem boas uma a uma podem resultar em algo medíocre. Uma etapa que fica no ar a maior parte do tempo ainda falha de vez em quando, e o pipeline falha sempre que qualquer etapa falha. O laboratório põe números nesse efeito com quatro valores plausíveis. Kofi usa o cálculo cedo no projeto para ver qual etapa limita o todo, antes de gastar dinheiro em etapas que já são confiáveis.

### Laboratório 7 — disponibilidade

```python
"""Lab 7 (ch 32): availability of a synthetic CTI pipeline - serial stages and a redundant pair."""
stages = {"taxii-poll": 0.995, "parser": 0.999, "enrich": 0.98, "store": 0.999}
serial = 1.0
for a in stages.values():
    serial *= a
print(f"serial availability={serial:.4f} (~{(1-serial)*8760:.0f} h/yr down)")
enrich_pair = 1 - (1 - stages["enrich"]) ** 2
improved = serial / stages["enrich"] * enrich_pair
print(f"with redundant enrich: {improved:.4f} (~{(1-improved)*8760:.0f} h/yr down)")
```

Execute com `python3 lab_avail.py`. Saída verificada:

```text
serial availability=0.9732 (~235 h/yr down)
with redundant enrich: 0.9926 (~65 h/yr down)
```

### 32.2 Lendo o laboratório

O pipeline em série chega a 0,9732, cerca de 235 horas de indisponibilidade por ano — dominadas pelo enriquecimento, com 0,98. Duplicar o enriquecimento (duas instâncias independentes, qualquer uma pode atender) eleva o pipeline a 0,9926, cerca de 65 horas por ano. Investir na etapa mais fraca dá o maior ganho. Kofi apresentou o resultado em horas, e não em razões, porque os gestores achavam mais fácil julgar duzentas horas por ano do que quatro casas decimais. O mesmo raciocínio orienta os gastos seguintes: antes de comprar um armazenamento mais confiável, que já está perto da perfeição, a equipe pergunta qual etapa ainda responde pela maior parte das horas perdidas.

### 32.3 Hipótese de independência

A fórmula da redundância supõe que as falhas são independentes. Dois trabalhadores de enriquecimento no mesmo host, ou chamando o mesmo provedor externo, falham juntos. Redundância real exige hosts diversos e, quando possível, provedores alternativos. Kofi conferiu o primeiro projeto de redundância e descobriu que as duas instâncias de enriquecimento chamavam o mesmo provedor externo. Se esse provedor caísse, as duas falhariam juntas e a melhoria do laboratório desapareceria. O projeto revisado acrescenta um modo de contingência que marca os indicadores como não enriquecidos em vez de esperar, o que tira a dependência comum do caminho crítico. Ele declara a hipótese de independência ao lado de cada número de disponibilidade que relata.

### 32.4 SLOs e orçamentos de erro

Um SLO como "99,5% das consultas têm sucesso a cada mês" define um orçamento de erro de 0,5%. Quando o orçamento se esgota, o trabalho em funcionalidades pausa e o trabalho de confiabilidade ganha prioridade. A equipe de Kofi acompanha o orçamento toda semana no mesmo painel das outras métricas. Quando uma interrupção de um parceiro consumiu a maior parte do orçamento de um mês, a equipe passou a sprint seguinte acrescentando novas tentativas e alertas em vez da funcionalidade de relatórios planejada. A regra foi acordada de antemão com o líder de CTI, então a pausa não precisou de uma nova discussão a cada vez.

### 32.5 Degradação controlada

Se o enriquecimento falha, o Lantern ainda deve armazenar e casar os indicadores, marcando-os como "não enriquecidos", em vez de parar a ingestão. Num SOC, serviço degradado é melhor que nenhum serviço. O modo de contingência de Kofi foi testado parando o serviço de enriquecimento durante uma reprodução de tráfego sintético. A ingestão continuou, a correspondência continuou e os indicadores levaram a marcação de não enriquecidos. Quando o enriquecimento voltou, uma tarefa em segundo plano preencheu o contexto ausente. Os analistas relataram que a marcação era útil, porque lhes dizia para buscar o contexto à mão nos casos urgentes durante a interrupção.

### Medindo o que os usuários sentem

O tempo no ar de cada processo não é o que os analistas experimentam. Kofi acrescenta uma sonda sintética que injeta um indicador de teste a cada quinze minutos e confere se ele chega à política de DNS. A taxa de sucesso da sonda é a disponibilidade que os usuários de fato sentem, e ela pega falhas entre componentes que as verificações de saúde por processo deixam passar.

### Exemplo resolvido

Kofi propõe uma segunda instância de enriquecimento em outro host e um modo de contingência que pula o enriquecimento externo quando o provedor está fora. A disponibilidade mensal medida sobe de 97,4% para 99,2% no trimestre seguinte; são números medidos, por isso diferem um pouco dos 0,9732 e 0,9926 previstos pelo Laboratório 7.

> **Caso sintético.** Os números são ilustrativos.

### Erros e limites

Números de disponibilidade escondem falhas parciais, como respostas lentas. Meça também SLOs de latência.

### Exercícios

- **EX094 — Resultado em série.** Cite a disponibilidade em série do laboratório e a indisponibilidade anual aproximada. *Rubrica:* 3 = 0,9732, ~235 h; 2 = um; 1 = errado; 0 = nenhuma.
- **EX095 — Dependência oculta.** Por que dois trabalhadores de enriquecimento podem não ser independentes? *Rubrica:* 3 = host/provedor/rede compartilhados → falha de modo comum; 2 = vago; 1 = sempre independentes; 0 = nenhuma.
- **EX096 — Modo degradado.** O que o Lantern deve fazer quando o enriquecimento externo está indisponível? *Rubrica:* 3 = continuar a ingestão/correspondência; marcar como não enriquecido; tentar de novo depois; 2 = continuar; 1 = parar o pipeline; 0 = nenhuma.

### Síntese

Multiplique as disponibilidades em série, corrija a etapa mais fraca com redundância de fato independente, administre os orçamentos de erro e degrade de forma controlada.

### Continue estudando — capítulo 32 de 50

[← Capítulo 31 (rascunho)](#ch-31) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 33 (rascunho) →](#ch-33)

<a id="ch-33"></a>

## Capítulo 33 — Inteligência de ameaças e OSINT: segurança operacional e resiliência

### Objetivos de aprendizagem

Você vai (1) analisar como as saídas de CTI poderiam prejudicar a tecnologia operacional; (2) projetar intertravamentos de segurança para ações automatizadas; (3) planejar a resiliência contra a perda de feeds ou parceiros; (4) ensaiar um retorno seguro à configuração anterior.

### 33.1 Como a inteligência pode ferir a operação

Um bloqueio amplo demais em um firewall de OT poderia separar um mestre SCADA de suas unidades terminais remotas, eliminando a visibilidade da rede elétrica. Uma marcação "maliciosa" equivocada no servidor de atualizações de um fornecedor poderia bloquear um patch relevante para a segurança operacional. Em infraestrutura crítica, falsos positivos têm consequências físicas. As revisões de projeto de Kofi perguntam, para cada ação automatizada, que efeito físico uma decisão errada poderia ter. Na TI corporativa a resposta costuma ser um site bloqueado e um chamado. Na OT pode ser uma sala de controle perdendo de vista parte da rede durante uma tempestade, justamente quando os operadores mais precisam dela. Essa diferença justifica regras diferentes para os dois ambientes.

### 33.2 Intertravamentos

O Lantern aplica intertravamentos: nenhuma ação automática em segmentos de OT; uma lista de endereços operacionais protegidos que nenhum bloqueio pode incluir; um tamanho máximo de mudança por envio; e aprovação por duas pessoas para qualquer regra de OT. Eles espelham a ideia da engenharia de segurança de que uma única falha não deve causar dano. Kofi testa cada intertravamento com um envio sintético feito para dispará-lo: uma lista com um endereço protegido, uma lista muito maior que o limite, uma aprovação por uma só pessoa. Cada teste precisa ser recusado e registrado.

### 33.3 Resiliência à perda de fontes

Se um parceiro importante parar de compartilhar, a detecção deve degradar de forma controlada. Fontes diversas, analíticas sobre a telemetria interna e detecções comportamentais mapeadas no ATT&CK reduzem a dependência de qualquer feed isolado. Kofi testou isso reproduzindo um mês de tráfego sintético sem o maior parceiro. As detecções caíram, mas as regras comportamentais ainda pegaram a maioria das intrusões simuladas que os indicadores haviam pegado, embora muitas vezes mais tarde. O resultado mostrou à BEN quão exposta ela ficaria se esse parceiro parasse de compartilhar e apoiou o investimento em analíticas internas.

### 33.4 Retorno à configuração anterior

Cada envio registra o conjunto de regras anterior. Um retorno testado, com um único comando, o restaura em minutos. Exercícios de retorno são feitos a cada trimestre no ambiente de teste. O exercício de Kofi mede quanto tempo o retorno leva e confere se as regras restauradas correspondem exatamente à cópia armazenada. O primeiro exercício levou vinte minutos porque o comando precisava de uma credencial que ninguém tinha à mão; agora o roteiro indica onde ela fica guardada. Um retorno que nunca é praticado tende a falhar na primeira vez em que é realmente necessário.

### 33.5 Coordenação com a operação

Os engenheiros de OT são donos das decisões operacionais. O Lantern fornece recomendações e evidências; ele não passa por cima da operação. Na prática, isso significa que as saídas do Lantern para a OT são recomendações com evidências anexadas. Um engenheiro de OT pode recusar um bloqueio porque ele interromperia uma janela de manutenção planejada, e essa decisão prevalece. Kofi registra o motivo, para que os analistas vejam por que o bloqueio não aconteceu. Se a ameaça crescer, os analistas a levantam de novo com novas evidências, em vez de contornar a equipe de operação. As duas equipes revisam juntas, todo mês, as recomendações recusadas.

### Nota de prática — casos de segurança

Um argumento de segurança curto declara o perigo, os intertravamentos que o previnem e a evidência de que cada intertravamento funciona. Os revisores podem então contestar um elo específico em vez do projeto inteiro.

### Depois de uma anulação

Sempre que um engenheiro anula um intertravamento, o dia útil seguinte inclui uma revisão curta do porquê, de se o intertravamento estava errado e de se a regra deve mudar.

### Exemplo resolvido

Um parceiro marca como malicioso o endereço do servidor de atualizações do fornecedor de relés da BEN depois de um comprometimento em outro lugar. O intertravamento de endereços protegidos bloqueia o envio automático; os engenheiros de OT revisam, confirmam que o servidor do fornecedor está limpo para a região da BEN e registram a decisão.

> **Caso sintético.** O fornecedor e a marcação são inventados.

### Erros e limites

Intertravamentos podem ser contornados sob pressão; audite cada anulação. A análise de segurança operacional precisa envolver engenheiros de OT.

### Exercícios

- **EX097 — Dano físico.** Dê uma forma pela qual um bloqueio no estilo de TI poderia causar dano operacional em uma rede elétrica. *Rubrica:* 3 = mecanismo específico (cortar a visibilidade do SCADA, bloquear patch de segurança); 2 = vago; 1 = tentativa mínima; 0 = nenhuma.
- **EX098 — Lista de intertravamentos.** Cite três intertravamentos que o Lantern aplica às ações de OT. *Rubrica:* 3 = três entre nenhuma ação automática em OT/lista de endereços protegidos/tamanho máximo de mudança/aprovação por duas pessoas; 2 = dois; 1 = um; 0 = nenhuma.
- **EX099 — Perda de fonte.** Como a detecção comportamental mapeada no ATT&CK ajuda quando um feed desaparece? *Rubrica:* 3 = detecta técnicas independentemente dos indicadores do feed; 2 = parcial; 1 = não ajuda; 0 = nenhuma.

### Síntese

Trate falsos positivos como riscos físicos, intertrave as ações automatizadas, diversifique as fontes e ensaie o retorno à configuração anterior.

### Continue estudando — capítulo 33 de 50

[← Capítulo 32 (rascunho)](#ch-32) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 34 (rascunho) →](#ch-34)

<a id="ch-34"></a>

## Capítulo 34 — Inteligência de ameaças e OSINT: integração

### Objetivos de aprendizagem

Você vai (1) integrar o Lantern a sistemas de SIEM, DNS, proxy e chamados; (2) projetar integrações idempotentes; (3) mapear os objetos do Lantern para os formatos dos sistemas de destino; (4) testar as integrações de ponta a ponta.

### 34.1 Alvos de integração

SIEM: os indicadores viram tabelas de consulta de correlação; os avistamentos fluem de volta. Resolvedor DNS: bloqueios de domínio e zonas de política de resposta. Proxy web: categorias de URL. Chamados: correspondências de alta confiança abrem chamados com contexto do diamante e do ATT&CK. Cada alvo tem seu próprio formato, seus limites e seu responsável, e é por isso que cada um tem seu próprio documento de interface. Kofi começou pelo resolvedor DNS porque ali os bloqueios de domínio são precisos e fáceis de desfazer. O SIEM veio em seguida, depois o proxy, depois os chamados. Acrescentar os alvos um de cada vez fez com que os problemas de um não se misturassem com os de outro.

### 34.2 Idempotência

Reenviar a mesma lista de bloqueio não pode duplicar regras. As integrações comparam o estado desejado com o estado atual e aplicam apenas as diferenças. Isso também faz do retorno à configuração anterior uma questão de reaplicar o estado desejado anterior. O exemplo resolvido mostra o que acontece sem isso: uma nova tentativa criou milhares de regras duplicadas. Comparar o estado desejado com o atual transforma uma nova tentativa em uma verificação inofensiva. A integração de Kofi registra o número de regras acrescentadas e removidas em cada execução, e uma execução que relata nenhuma mudança é o resultado normal e saudável.

### 34.3 Mapeando formatos

Padrões STIX como `[domain-name:value = 'c2.example']` são traduzidos para a sintaxe de regras de cada produto. Recursos de padrão não suportados são rejeitados com motivo, em vez de aproximados. Kofi mantém a tabela de tradução de cada produto na configuração, com testes. Um padrão que combina duas condições com uma janela de tempo, por exemplo, não pode ser expresso no formato do resolvedor, então vai para o SIEM. Aproximá-lo com uma só condição bloquearia muito mais ou muito menos do que o pretendido. Cada rejeição é registrada com o padrão.

### 34.4 Contexto nos chamados

Um chamado que diz "correspondência em drop.example" é fraco. Um chamado que acrescenta fonte, confiança, TLP, técnicas do ATT&CK relacionadas e ações recomendadas permite aos analistas agir depressa. Kofi mediu o efeito em uma amostra de chamados. Os analistas encerraram mais rápido os chamados ricos em contexto e escalaram menos deles por engano, porque a ação recomendada e a confiança estavam diante deles. Um link de volta para o objeto no Lantern permite ao analista ver o histórico completo sem procurar. Os chamados são gerados a partir do mesmo objeto.

### 34.5 Testes de ponta a ponta

Um indicador sintético é injetado no coletor; o teste confere se ele aparece na política de DNS, dispara uma consulta no SIEM a partir de uma requisição sintética e abre um chamado — depois o remove e confere a limpeza. Kofi executa esse teste após cada versão e cada mudança nos sistemas de destino. Quando a equipe de DNS atualizou seu resolvedor, o teste pegou uma mudança na forma como o arquivo de política era carregado, e a correção foi feita em homologação antes da produção. O indicador sintético usa um domínio de exemplo reservado, então nem uma limpeza que falhe pode afetar tráfego real.

### Nota de prática — responsáveis

Cada integração tem um responsável nomeado na equipe do sistema de destino. Quando a equipe de DNS atualiza seu resolvedor, ela sabe que precisa executar o teste de integração do Lantern.

### Deriva de versões

Os produtos de destino mudam suas APIs. O Lantern fixa a versão da API que usa em cada integração e executa o teste de ponta a ponta no ambiente de homologação da equipe de destino antes que ela faça a atualização, para que as mudanças apareçam antes da produção.

### Exemplo resolvido

A integração com o proxy duplicou 3.000 regras após uma nova tentativa. Kofi a muda para uma comparação de estados; envios repetidos agora relatam "0 changes", e a equipe do proxy confirma que as contagens de regras batem com o estado desejado do Lantern.

> **Caso sintético.** O incidente de duplicação é inventado.

### Erros e limites

Os produtos de destino têm limites de quantidade de regras; priorize pela confiança. Aproximar padrões não suportados cria lacunas silenciosas.

### Exercícios

- **EX100 — Envio idempotente.** Descreva como funciona uma integração idempotente de lista de bloqueio. *Rubrica:* 3 = compara o desejado com o atual e aplica só a diferença; repetir não muda nada; 2 = parcial; 1 = reenviar tudo; 0 = nenhuma.
- **EX101 — Contexto do chamado.** Liste quatro campos de contexto para um chamado de correspondência. *Rubrica:* 3 = quatro entre fonte, confiança, TLP, ATT&CK, ação recomendada, campos do diamante; 2 = dois; 1 = só o indicador; 0 = nenhuma.
- **EX102 — Padrão não suportado.** O que deve acontecer com um padrão STIX que o proxy não consegue expressar? *Rubrica:* 3 = rejeitar com motivo/encaminhar a outro destino; nunca aproximar em silêncio; 2 = rejeitar; 1 = aproximar; 0 = nenhuma.

### Síntese

Integre pelo estado desejado, traduza os padrões com exatidão, enriqueça os chamados com contexto e teste o caminho inteiro.

### Continue estudando — capítulo 34 de 50

[← Capítulo 33 (rascunho)](#ch-33) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 35 (rascunho) →](#ch-35)

<a id="ch-35"></a>

## Capítulo 35 — Ateliê de projeto II

### Objetivos de aprendizagem

Você vai (1) projetar a camada de análise e disseminação do Lantern; (2) produzir modelos de produtos para consumidores diferentes; (3) defender as escolhas de projeto diante de um revisor adversarial; (4) estimar esforço e riscos da construção.

### 35.1 Enunciado

Projete como os analistas transformam objetos armazenados em produtos: um resumo tático diário, um sumário operacional semanal e um briefing estratégico trimestral para executivos, cada um com controles de TLP, linguagem de julgamento no estilo da ICD 203 e captura de retorno. Os três produtos atendem a leitores diferentes, em calendários diferentes. Os analistas precisam do resumo toda manhã; os gestores querem o sumário semanal antes da reunião de planejamento; os executivos leem o briefing uma vez por trimestre. A equipe de Kofi projetou cada um de trás para a frente a partir da decisão do leitor, começando pelo que o leitor deveria ser capaz de fazer depois da leitura.

### 35.2 Modelos

Resumo tático: principais indicadores por confiança, ações tomadas, avistamentos. Sumário operacional: campanhas ativas com estrutura de diamante e técnicas do ATT&CK. Briefing estratégico: tendências de adversários relevantes para a distribuição de eletricidade, julgamentos-chave com palavras estimativas e uma escala de probabilidade publicada. Cada modelo tem uma ordem fixa, para que os leitores saibam onde procurar. Kofi manteve o resumo em uma única tela e o briefing estratégico em duas páginas. Os modelos também obrigam o analista a preencher fonte e confiança para cada item, o que torna as lacunas evidentes antes da publicação.

### 35.3 Revisão adversarial

Um revisor faz o papel de um executivo cético: "Por que eu deveria confiar nisto?" O projeto responde com descrições das fontes, confiança e um histórico de julgamentos anteriores. As respostas vêm de registros que o Lantern já mantém. As descrições das fontes explicam quem relatou algo e como sabia. Os julgamentos anteriores são pontuados quando os desfechos se tornam conhecidos, para que o leitor veja com que frequência o "provável" da equipe quis dizer o que dizia. O revisor cético do ateliê de Kofi se convenceu por esse histórico, e não pela segurança do texto.

### 35.4 Esforço e risco

A equipe estima o esforço por componente e lista os riscos: o tempo dos analistas para escrever briefings estratégicos, o consentimento dos parceiros para citação, a atenção dos executivos. Os briefings estratégicos tomaram muito mais tempo dos analistas do que a equipe imaginou de início; a estimativa de Kofi dobrou depois que ele cronometrou um briefing de teste. O consentimento dos parceiros para citar material pode levar semanas, o que afeta o cronograma. A atenção dos executivos é o recurso mais escasso de todos, então o briefing se limita ao que eles podem fazer algo a respeito. Cada risco tem um responsável e um plano.

### 35.5 Acessibilidade

Os produtos são legíveis no celular, evitam codificação apenas por cor (os rótulos TLP são escritos em texto, como o TLP 2.0 recomenda) e incluem texto alternativo para as figuras. Kofi testou os modelos em um telefone e com um leitor de tela. Um gráfico que usava só a cor para indicar a severidade ficou ilegível para um revisor, então agora a severidade também é escrita como palavra. Escrever o rótulo em texto também faz com que ele sobreviva à impressão em preto e branco. Produtos acessíveis alcançam mais leitores, o que importa quando o leitor é um engenheiro em uma subestação lendo em um tablet.

### Nota de prática — menos produtos, melhores

As equipes do ateliê costumam propor uma dúzia de tipos de produto. A banca resiste: três produtos que são lidos valem mais que doze que são ignorados.

### Medindo a leitura

Cada produto registra aberturas e cliques de retorno. Depois de um trimestre, a equipe aposenta qualquer produto que ninguém lê e pergunta ao público pretendido do que ele precisa em seu lugar.

### Exemplo resolvido

O modelo de briefing estratégico de Kofi abre com três julgamentos-chave, cada um com uma expressão estimativa associada a uma faixa, a base do julgamento e o que o mudaria. O revisor cético aceita o modelo depois de ver que a exatidão dos julgamentos anteriores é acompanhada.

> **Caso sintético.** A revisão do modelo é inventada.

### Erros e limites

Modelos podem virar texto de praxe; os revisores devem conferir se cada produto diz algo novo. Produtos estratégicos precisam de tempo de analista, não só de automação.

### Exercícios

- **EX103 — Três produtos.** Associe os produtos tático, operacional e estratégico a seu público principal. *Rubrica:* 3 = analistas do SOC; líderes de resposta a incidentes/caça; executivos; 2 = dois; 1 = um; 0 = nenhuma.
- **EX104 — Resposta sobre confiança.** Dê duas características de projeto que respondam a "por que eu deveria confiar nisto?". *Rubrica:* 3 = duas entre descrição da fonte, confiança/escala estimativa, histórico, gatilhos de mudança; 2 = uma; 1 = identidade visual; 0 = nenhuma.
- **EX105 — Só cor.** Por que os rótulos TLP devem ser escritos em texto, e não mostrados apenas por cor? *Rubrica:* 3 = acessibilidade/daltonismo/impressão; orientação do TLP 2.0; 2 = acessibilidade; 1 = sem motivo; 0 = nenhuma.

### Síntese

Projete poucos produtos para públicos nomeados, torne a confiança visível, planeje o esforço com honestidade e mantenha os produtos acessíveis.

### Continue estudando — capítulo 35 de 50

[← Capítulo 34 (rascunho)](#ch-34) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 36 (rascunho) →](#ch-36)

<a id="ch-36"></a>

## Capítulo 36 — Inteligência de ameaças e OSINT: desempenho e escala

### Objetivos de aprendizagem

Você vai (1) detectar filas instáveis, em que a chegada supera o atendimento; (2) aplicar a lei de Little para estimar o tempo de espera; (3) escolher entre escalar verticalmente, escalar horizontalmente e descartar carga; (4) proteger os parceiros quando o Lantern escala.

### 36.1 Filas instáveis

Se 120 objetos por minuto chegam ao enriquecimento e só 100 por minuto são atendidos, o acúmulo cresce 20 a cada minuto, sem limite. Nenhuma espera resolve isso; a capacidade ou a demanda precisa mudar. O laboratório imprime exatamente esse padrão, e depois de cinco minutos o acúmulo é de cem itens e continua subindo. Kofi observa a tendência, e não o tamanho: uma fila longa que está encolhendo está se recuperando, enquanto uma curta que cresce a cada minuto é um problema. Seu alerta dispara quando o acúmulo cresce por dez minutos seguidos, antes que fique grande o bastante para os analistas notarem.

### Laboratório 8 — crescimento da fila

```python
"""Lab 8 (ch 36): Little's law and backlog growth for a synthetic enrichment queue."""
arrival_per_min, service_per_min = 120, 100
backlog = 0
for minute in range(1, 6):
    backlog += arrival_per_min - service_per_min
    print(f"minute {minute}: backlog={backlog}")
L, lam = 400, 100 / 60  # items in system, throughput items/s after scaling fixes
print(f"Little's law wait W=L/lambda={L/lam:.0f} s at L={L}, lambda={lam:.2f}/s")
```

Execute com `python3 lab_queue.py`. Saída verificada:

```text
minute 1: backlog=20
minute 2: backlog=40
minute 3: backlog=60
minute 4: backlog=80
minute 5: backlog=100
Little's law wait W=L/lambda=240 s at L=400, lambda=1.67/s
```

### 36.2 Lei de Little

Em um sistema estável, o número médio no sistema L é igual à vazão λ vezes o tempo médio no sistema W. Com 400 itens na fila e 1,67 item atendido por segundo, a espera média é de cerca de 240 segundos. A lei não exige suposições sobre o padrão das chegadas, o que a torna uma verificação robusta nos painéis. Kofi a usa para conferir se os números do painel concordam entre si. Se o tamanho da fila, a vazão e a espera relatada não se encaixam na lei, uma das medições está errada.

### 36.3 Opções

Escalar verticalmente (hardware mais rápido), escalar horizontalmente (mais trabalhadores) ou descartar carga (pular enriquecimentos de pouco valor, amostrar indicadores de baixa confiança). Descartar pelo valor costuma ser o mais barato: enriqueça primeiro os indicadores de alta confiança. Kofi compara o custo de cada opção com o ganho. Uma máquina mais rápida só ajuda se o trabalho for limitado pelo processamento. Mais trabalhadores só ajudam se o trabalho puder ser dividido e o provedor permitir mais consultas. Descartar trabalho de pouco valor exige uma regra clara sobre o que conta como pouco valor, acordada com os analistas, e um registro do que foi pulado, para que possa ser feito depois se necessário.

### 36.4 Protegendo os parceiros

Escalar os coletores horizontalmente não pode multiplicar a carga sobre os servidores TAXII dos parceiros. O Lantern mantém uma única identidade de consulta por parceiro e compartilha os resultados internamente, respeitando os limites de taxa dos parceiros. O projeto de Kofi separa a coleta do processamento por esse motivo. Não importa quantos trabalhadores internos o Lantern execute, um único coletor por parceiro consulta na taxa acordada e coloca os objetos em uma fila interna. Os parceiros veem o mesmo tráfego, esteja a BEN tranquila ou no meio de uma campanha. Se um parceiro aumenta seus limites, a configuração muda depois do acordo, e não antes.

### 36.5 Testando em escala

Os testes de carga usam pacotes sintéticos gerados em tamanhos realistas, executados apenas contra o substituto TAXII e os componentes internos. O gerador de Kofi cria pacotes com a mesma mistura de tipos e tamanhos de objeto que os parceiros enviam, incluindo uma parcela de objetos malformados, para que o teste exercite também o caminho de rejeição. Executar contra servidores reais dos parceiros testaria a capacidade deles, e não a da BEN, e violaria os acordos. Os resultados registram o hardware, a versão do código e os volumes gerados, para que um teste posterior possa ser comparado de forma justa. Cada execução termina conferindo se as filas se esvaziaram por completo.

### Nota de prática — filas com prioridade

Duas filas — alta e baixa confiança — com trabalhadores atendendo primeiro a alta mantêm rápido o enriquecimento importante durante os picos, enquanto o trabalho de pouco valor espera ou é pulado.

### Revisões de capacidade

A cada trimestre, Kofi compara as taxas de chegada de pico com a capacidade de atendimento e registra a folga em percentual, para que o crescimento seja planejado antes que as filas fiquem instáveis.

### Exemplo resolvido

Durante uma grande campanha, as chegadas saltam para 120 por minuto. Kofi acrescenta dois trabalhadores (atendimento de 150 por minuto) e passa os indicadores de baixa confiança para uma fila adiada. O acúmulo se esvazia em menos de dez minutos, e a consulta aos parceiros continua inalterada.

> **Caso sintético.** As taxas são inventadas.

### Erros e limites

A lei de Little descreve médias; a latência de cauda exige percentis. Escalar o consumidor de um provedor externo com limite de taxa só produz mais respostas 429.

### Exercícios

- **EX106 — Acúmulo após cinco.** Que acúmulo o laboratório mostra depois de cinco minutos, e por que ele continua crescendo? *Rubrica:* 3 = 100; a chegada supera o atendimento em 20/min; 2 = só o número; 1 = estável; 0 = nenhuma.
- **EX107 — Lei de Little.** Calcule W para L = 300 itens com λ = 2 itens por segundo. *Rubrica:* 3 = 150 s; 2 = método; 1 = 600; 0 = nenhuma.
- **EX108 — Carga nos parceiros.** Por que escalar os coletores horizontalmente não pode acrescentar identidades de consulta por parceiro? *Rubrica:* 3 = multiplicaria a carga do parceiro/violaria os limites de taxa; 2 = parcial; 1 = tudo bem; 0 = nenhuma.

### Síntese

Identifique a instabilidade, use a lei de Little para as esperas, escale ou descarte pelo valor e mantenha constante a carga sobre os parceiros.

### Continue estudando — capítulo 36 de 50

[← Capítulo 35 (rascunho)](#ch-35) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 37 (rascunho) →](#ch-37)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX108 (as de EX109–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). A Brightwater Energy Networks, o Lantern, Kofi Mensah e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX019.** 0.045 — cerca de um alerta verdadeiro em cada vinte e dois.

**EX020.** Reduzir a taxa de falsos positivos (por exemplo, combinando com um segundo sinal) e aplicar a regra apenas aos segmentos de tráfego em que a atividade maliciosa é mais prevalente; um portão de enriquecimento antes do acionamento também funciona.

**EX021.** A latência é assimétrica à direita; a cauda lenta é o que os usuários percebem e o que os SLAs regem, e a média a esconde.

**EX022.** Entrada/saída — o processo está esperando pelo disco; mantenha o conjunto quente na memória ou em armazenamento mais rápido.

**EX023.** Os dados de enriquecimento ficam obsoletos, e os termos dos provedores podem limitar por quanto tempo os resultados são retidos ou com que frequência são consultados.

**EX024.** 400.000 × 200 B = 80 MB brutos; o uso real será maior por causa da sobrecarga dos objetos.

**EX025.** Quatro quaisquer entre: motivo da rejeição, fonte, hash dos bytes originais, carimbo de tempo, versão do parser.

**EX026.** norm(norm(x)) == norm(x): reexecutar a ingestão ou renormalizar os dados armazenados nunca muda os valores, então não surgem duplicatas nem deriva.

**EX027.** Os objetos são TLP:AMBER e o parceiro já os tem; hashes e contagens permitem que ele encontre os registros ruins sem que o Lantern recompartilhe conteúdo restrito.

**EX028.** Fatos combinados podem revelar onde alguém mora ou como encontrá-lo, possibilitando assédio; tratar dados identificáveis também gera obrigações de proteção de dados.

**EX029.** Abortar o envio, manter ativa nos firewalls a última lista sabidamente boa e alertar uma pessoa para revisão.

**EX030.** Recusar, registrar o pedido por escrito e escalá-lo ao encarregado de privacidade ou à equipe jurídica.

**EX031.** O TAXII 2.1 especifica a API HTTPS — descoberta, raízes de API, coleções, endpoints de objetos, tipos de mídia; quem pode ler ou gravar e o que pode ser compartilhado vêm dos acordos.

**EX032.** O endereço hospeda milhares de sites sem relação entre si, então bloqueá-lo causaria danos colaterais; o domínio identifica especificamente o recurso malicioso.

**EX033.** Recuar e tentar de novo depois do intervalo indicado pelo servidor (por exemplo, Retry-After); nunca trocar de identidade ou de endereço para burlar o limite.

**EX034.** Não. O privilégio mínimo e a segregação de funções mantêm as mudanças no firewall em um serviço separado e auditado; um coletor comprometido não deve poder alterar controles.

**EX035.** Os logs de acesso da aplicação do Lantern, corroborados pelos logs de autenticação do sistema operacional das contas envolvidas.

**EX036.** Três quaisquer entre: nenhum acesso à rede ou acesso muito limitado, sistema de arquivos somente leitura, limites de memória e CPU, usuário sem privilégios.

**EX037.** Quatro: c2.example, http://drop.example/a, 203.0.113.9 e 198.51.100.44.

**EX038.** Duas fontes independentes relatando o mesmo indicador são uma corroboração que os analistas precisam ver, e a proveniência sustenta a auditoria de quem compartilhou o quê.

**EX039.** Os caminhos de URL costumam ser sensíveis a maiúsculas e minúsculas nos servidores, então `/Payload` e `/payload` podem ser recursos diferentes; passe para minúsculas apenas o esquema e o host.

**EX040.** Mudanças no comportamento de ponta a ponta — quantos indicadores sobrevivem a todas as etapas e chegam ao bloqueio —, que os testes unitários isolados não revelam.

**EX041.** Nenhum requisito nem acordo do SOC a justificava, e a reprodução mostrou um grande efeito no comportamento (1.240 indicadores a mais no bloqueio automatizado).

**EX042.** Em um cofre de segredos; a configuração guarda apenas referências às entradas do cofre.

**EX043.** Um indicador envenenado que liste o domínio de um fornecedor poderia levar a BEN a bloqueá-lo, interrompendo pagamentos ou atualizações; inversamente, indicadores removidos poderiam deixar passar uma ameaça real.

**EX044.** Exemplo: Detect — indicadores e técnicas viram regras de detecção; Identify — perfis de ameaça alimentam a avaliação de riscos. Respond (contexto durante incidentes) e Govern (acordos de compartilhamento) também pontuam.

**EX045.** Detecta entradas envenenadas ou equivocadas que bloqueariam serviços de que a BEN depende, antes que cheguem aos controles.

**EX046.** Não. É um sistema externo de propriedade do ISAC; o Lantern interage com ele por meio de uma interface TAXII controlada.

**EX047.** Formato dos dados, limites de taxa, autenticação, tratamento de erros, responsáveis de cada lado (versionamento também conta).

**EX048.** Avisar o parceiro, apagar os dados retidos que o acordo exige apagar e revogar as credenciais usadas pelo feed.

**EX049.** Sensor: chamados de falso positivo do SOC. Controlador: a regra de ajuste do limiar. Atuador: a lista de bloqueio enviada aos firewalls.

**EX050.** Passos pequenos evitam reagir demais a um dia ruidoso e impedem que o limiar oscile entre rígido demais e frouxo demais.

**EX051.** Detecções perdidas raramente geram chamados, então um laço guiado só por reclamações deriva para menos bloqueios e mais ameaças perdidas.

**EX052.** As zonas de OT devem conter só o que a operação precisa; acrescentar uma plataforma de CTI aumenta a superfície de ataque e o risco à segurança operacional, então a OT recebe apenas saídas aprovadas.

**EX053.** Um bloqueio do domínio no resolvedor DNS ou no proxy web, porque mira o nome malicioso sem bloquear milhares de sites sem relação no endereço compartilhado.

**EX054.** Removeu o acesso direto da zona do SOC à internet, reduzindo a exposição e um possível caminho de exfiltração a partir do armazenamento.

**EX055.** Prova que o pacote veio de quem detém a chave e não foi alterado; não prova que os indicadores estão corretos.

**EX056.** Apenas as pessoas nomeadas como destinatárias naquele relatório.

**EX057.** Alertas 30, 14 e 3 dias antes da expiração para o engenheiro responsável e o contato do parceiro, com um link para o roteiro de rotação.

**EX058.** Informação — organizada e contextualizada, mas ainda não analisada para dizer o que a BEN deve fazer.

**EX059.** Um relatório de vigilância de fornecedores que diga ao engenheiro de OT se campanhas miram o fornecedor de relés da BEN, com ações recomendadas.

**EX060.** "Coletada legalmente" — compromete a OSINT e os feeds do Lantern com uma coleta legal, que respeita os termos de uso.

**EX061.** Exemplo: "O Lantern deve publicar indicadores TLP:GREEN aprovados por analista na coleção TAXII do ISAC em até 60 minutos após a aprovação, para 95% dos indicadores em cada mês."

**EX062.** Exemplo: "O Lantern deve marcar objetos threat-actor cujos relatórios citem ataques à distribuição de eletricidade e produzir um resumo mensal de agentes; verificado por um teste com relatório sintético."

**EX063.** Exemplo: "O módulo de OSINT deve coletar apenas de fontes organizacionais (domínios, certificados, avisos) e não deve armazenar perfis pessoais de redes sociais; verificado por revisão de código e por um teste que rejeita essas fontes."

**EX064.** `pattern`, `pattern_type` e `valid_from`.

**EX065.** Armazená-lo de forma opaca, com a procedência, e sinalizá-lo para revisão, para que nada se perca silenciosamente.

**EX066.** novo → ativo → decaído → aposentado. Exemplos de gatilho: ativo → decaído com o passar do tempo sem avistamentos; decaído → aposentado quando a confiança cai abaixo do piso; decaído → ativo com um novo avistamento.

**EX067.** 7 × 3 × 5 = 105.

**EX068.** 6 × 4 × 2 = 48.

**EX069.** T1078 Valid Accounts.

**EX070.** Como "desconhecido": nada na evidência identifica o adversário, e um palpite contaminaria a análise posterior.

**EX071.** E-mail de phishing: T1566. Execução do script: T1059.

**EX072.** Negar na entrega: uma regra no gateway de e-mail que bloqueia o padrão do phishing. Detectar no comando e controle: analíticas de DNS que alertam sobre consultas a drop.example.

**EX073.** Contexto, decisão, alternativas consideradas, consequências.

**EX074.** Os indicadores podem esperar até 15 minutos antes da ingestão; intervalos menores aumentariam a carga nos servidores dos parceiros.

**EX075.** O domínio do remetente, um hash da linha de assunto e os campos de indicador extraídos.

**EX076.** Se os pesos forem definidos depois da pontuação, podem ser ajustados para que a opção preferida vença; acordá-los primeiro mantém o estudo honesto.

**EX077.** Uma plataforma que exporta tudo como STIX 2.1 padrão permite à BEN migrar o histórico a baixo custo; uma que não exporta aprisiona os dados e eleva o custo de saída.

**EX078.** Como um quase empate dentro da incerteza da pontuação, com a questão qualitativa decisiva — o risco do fluxo de OT — posta explicitamente à banca.

**EX079.** R-1: `TLP:GREEN -> public BLOCK`. R-3: `TLP:RED -> team BLOCK`.

**EX080.** TLP:PURPLE não é um rótulo do TLP 2.0, então a barreira falha fechada e o bloqueia.

**EX081.** O aprovador nomeado, o horário da aprovação, a versão exata da regra ou do objeto enviado e o motivo.

**EX082.** Se o ponto de controle avança primeiro e o processo cai antes da gravação, esses objetos nunca são buscados de novo; gravar primeiro significa que uma queda só causa uma nova busca inofensiva, tornada segura pelas gravações idempotentes.

**EX083.** O tráfego de desenvolvimento nunca carrega nem põe em risco os servidores dos parceiros, e os testes rodam sobre pacotes sintéticos fixos, então os resultados são reproduzíveis.

**EX084.** A idade do ponto de controle (ou os objetos recebidos por fonte): se ela não para de crescer ou os recebimentos caem a zero, o coletor parou.

**EX085.** precisão 0,50, revocação 0,60, F1 0,55.

**EX086.** Usar as próprias afirmações do feed como verdade contaria toda entrada como correta, inflando a precisão; os rótulos precisam vir de investigações independentes.

**EX087.** O feed costuma listar indicadores dois dias depois que a BEN já os viu, então acrescenta pouco valor preventivo.

**EX088.** Verificação: confirmar que o Lantern atende aos requisitos escritos. Validação: confirmar que ele atende às necessidades reais das partes interessadas em uso.

**EX089.** O tratamento dos rótulos precisa ser exato e especificado — normalizado por uma regra documentada ou rejeitado; aceitar em silêncio uma variante mostra que a barreira não se comporta como exigido.

**EX090.** Como "bloqueado — não executado", listado à parte com o dado de teste ausente e uma data agendada; não é uma aprovação.

**EX091.** Para que a exportação possa remover os campos cujo provedor proíbe a redistribuição e para que os limites de retenção sejam respeitados por fonte.

**EX092.** Compartilha a referência ao indicador, as contagens de avistamentos e os horários da primeira e da última observação; remove nomes de host internos e nomes de usuário.

**EX093.** Evita reescrever todos os registros toda noite e mantém o modelo de decaimento em uma única função, de modo que mudar o modelo muda todos os resultados de uma vez.

**EX094.** Disponibilidade em série de 0,9732, cerca de 235 horas de indisponibilidade por ano.

**EX095.** Se os dois rodam no mesmo host, dependem do mesmo provedor externo ou compartilham um caminho de rede, uma única falha derruba os dois — uma falha de modo comum.

**EX096.** Continuar ingerindo e casando, marcar os indicadores afetados como "não enriquecidos" e enriquecê-los quando o provedor voltar.

**EX097.** Bloquear o tráfego entre um mestre SCADA e as unidades terminais remotas eliminaria a visibilidade e o controle das subestações.

**EX098.** Nenhuma ação automática em OT; uma lista de endereços protegidos que os bloqueios não podem incluir; um tamanho máximo de mudança por envio; aprovação por duas pessoas (quaisquer três).

**EX099.** As detecções comportamentais procuram técnicas como T1059 ou T1071 na própria telemetria da BEN, então continuam funcionando sem os indicadores do feed perdido.

**EX100.** A integração lê as regras atuais do destino, compara-as com o conjunto desejado do Lantern e aplica apenas as diferenças, de modo que repetir um envio não muda nada.

**EX101.** Fonte, confiança, marcação TLP, técnicas do ATT&CK relacionadas (também a ação recomendada e os campos do diamante).

**EX102.** Rejeitá-lo para aquele destino com um motivo registrado e encaminhá-lo a uma integração que consiga expressá-lo; nunca aproximar em silêncio.

**EX103.** Resumo tático → analistas do SOC; sumário operacional → líderes de resposta a incidentes e de caça; briefing estratégico → executivos.

**EX104.** Descrições das fontes com a confiança em uma escala estimativa publicada e um histórico acompanhado da exatidão dos julgamentos anteriores (gatilhos de mudança também contam).

**EX105.** Só a cor falha para leitores daltônicos e na impressão monocromática; o TLP 2.0 espera que o texto do rótulo seja mostrado.

**EX106.** Um acúmulo de 100 depois de cinco minutos; ele cresce 20 a cada minuto porque chegam 120 e só 100 são atendidos.

**EX107.** W = L / λ = 300 / 2 = 150 segundos.

**EX108.** Cada nova identidade consultaria o parceiro separadamente, multiplicando sua carga e possivelmente violando os limites de taxa acordados.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da LGPD, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Bianco, D. (2013). The Pyramid of Pain. <https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
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
