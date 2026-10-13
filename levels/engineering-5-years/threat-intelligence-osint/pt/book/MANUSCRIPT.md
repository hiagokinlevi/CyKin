# Inteligência de ameaças e OSINT: um livro de engenharia

- Idioma: português do Brasil (`pt`); curso de engenharia, cinco anos. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–15 de 50 já estão escritos em português, com os exercícios EX001–EX045 e suas resoluções com rubricas de 0 a 3 e 4 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 16–50 (EX046–EX150) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) |

Capítulos 16–50: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-16), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX045 (as de EX046–EX150 estão na edição em inglês até a tradução dos capítulos correspondentes). A Brightwater Energy Networks, o Lantern, Kofi Mensah e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
