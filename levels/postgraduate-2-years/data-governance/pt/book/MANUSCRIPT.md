# Governança de Dados: Curso de Pós-Graduação

- Idioma: português do Brasil (`pt`); curso 141, pós-graduação (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–12 de 12 têm texto didático escrito à mão; os exercícios EX001–EX060 têm resoluções correspondentes com rubricas de 0 a 3; dois laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: profissionais em atividade que cursam uma pós-graduação em tempo parcial e precisam liderar a governança de dados em sua própria organização.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios medem a parcela de eventos sintéticos de rastreamento das transportadoras que chegam em até quinze minutos e revisam contas inativas e não aprovadas em um conjunto sintético de dados de remessas. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma profissional desde o modelo operacional, a titularidade e a gestão da qualidade, passando por pontualidade, metadados, acessos, privacidade, contratos com parceiros e relatórios ao conselho, até um projeto final baseado no trabalho e sua apresentação. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Lucía Herrera** | Estudante profissional, analista de dados | Inventada |
| **Dr. Samuel Achebe** | Orientador | Inventado |
| **Westbridge Business School** | Escola fictícia | Inventada |
| **Corran Freight** | Empresa de logística fictícia, com cerca de 12.000 remessas por dia | Inventada |

### Fontes principais

DAMA-DMBOK2 (2017); ISO/IEC 38505-1:2017; ISO 8000-8:2015; Wang e Strong (1996); NIST Privacy Framework 1.0; GDPR; LGPD. Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — A profissional e a Corran Freight

### Objetivos de aprendizagem

Você vai (1) descrever o percurso da pós-graduação e seu caso; (2) enunciar os problemas de governança da Corran Freight; (3) planejar uma abordagem de aprendizagem baseada no trabalho.

### 1.1 A estudante

Lucía Herrera é analista de dados e trabalha há seis anos na Corran Freight, uma empresa de logística fictícia que transporta mercadorias para varejistas por uma rede rodoviária nacional. Ela se matricula em uma pós-graduação de dois anos em tempo parcial em governança de dados na fictícia Westbridge Business School, estudando junto com o trabalho. Seu orientador, o Dr. Samuel Achebe, explica que o curso foi desenhado para profissionais: cada módulo pede aos estudantes que apliquem as ideias diretamente à própria organização, usando dados sintéticos em todos os laboratórios e exercícios avaliados.

### 1.2 A Corran Freight

A Corran Freight opera trezentos caminhões, trabalha com três transportadoras subcontratadas e movimenta cerca de doze mil remessas por dia. Seus dados incluem pedidos de remessa, eventos de rastreamento enviados pelos veículos e pelas transportadoras, cadastros de motoristas, contratos com clientes e faturas. Os clientes exigem cada vez mais estimativas de chegada precisas e comprovantes de entrega. A gerente de Lucía lhe pediu que liderasse melhorias na governança de dados, porque as disputas sobre entregas atrasadas estão custando dinheiro e ninguém sabe dizer quais dados de rastreamento são confiáveis o bastante para resolvê-las. Lucía já viu essas disputas de perto.

### 1.3 Os problemas

Lucía lista os problemas que vê: os eventos de rastreamento das transportadoras chegam atrasados ou nem chegam, os endereços dos clientes são inconsistentes entre o sistema de pedidos e o de faturamento, o acesso aos dados dos motoristas é concedido informalmente e o relatório semanal de desempenho para o conselho usa definições diferentes das que constam nos contratos com os clientes. O Dr. Achebe lhe pede que descreva cada problema pelo efeito no negócio, como as faturas contestadas, e não pelo sintoma técnico, para que as propostas seguintes se liguem a resultados que importam para os gestores.

### 1.4 Aprendizagem baseada no trabalho

O curso usa a aprendizagem baseada no trabalho: Lucía vai investigar sua organização, aplicar modelos, propor mudanças e refletir sobre os resultados. O Dr. Achebe adverte que quem está dentro pode não ver o que quem está de fora vê, e pode hesitar em questionar os colegas. Ele lhe pede que mantenha um diário reflexivo e que busque a opinião de pessoas de fora de sua equipe. Ela concorda em compartilhar seus planos com a gerente a cada semestre, para que a organização entenda o que ela está estudando e possa se beneficiar de suas propostas. A gerente acolhe o arranjo e oferece apoio.

### Exemplo resolvido

Lucía, analista da Corran Freight, começa uma pós-graduação para profissionais, lista os eventos atrasados das transportadoras, os endereços inconsistentes, o acesso informal aos dados dos motoristas e as definições divergentes do relatório e planeja uma aprendizagem reflexiva baseada no trabalho.

> **Caso sintético.** A Corran Freight, a Westbridge e todas as pessoas são sintéticas.

### Erros e limites

Descrever os problemas em termos técnicos, e não pelo efeito no negócio, faz perder a atenção dos gestores.

### Exercícios

- **EX001 — Formato do curso.** Que tipo de curso Lucía está fazendo? *Rubrica:* 3 = uma pós-graduação para profissionais em tempo parcial;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.
- **EX002 — Volume de remessas.** Quantas remessas a Corran movimenta por dia, aproximadamente? *Rubrica:* 3 = cerca de doze mil;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX003 — Divergência do relatório.** O que há de errado com as definições do relatório ao conselho? *Rubrica:* 3 = diferem das definições dos contratos com os clientes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX004 — Risco de quem está dentro.** Que risco corre quem pesquisa a própria organização? *Rubrica:* 3 = não ver o que quem está de fora vê e hesitar em questionar;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.
- **EX005 — Formulação dos problemas.** Como os problemas devem ser descritos? *Rubrica:* 3 = pelo efeito no negócio;; 2 = parcialmente correto;; 1 = em termos técnicos;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 12)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Modelo operacional de governança

### Objetivos de aprendizagem

Você vai (1) comparar modelos operacionais de governança; (2) escolher um para uma empresa de porte médio; (3) definir o mandato de um grupo de governança.

### 2.1 Modelos

O Dr. Achebe apresenta os modelos operacionais. Um modelo centralizado concentra as decisões de governança em uma única equipe. Um modelo federado divide as decisões entre um escritório central, que define os padrões, e as unidades de negócio, que os aplicam. Um modelo descentralizado deixa as decisões com as unidades, com uma coordenação leve. O DAMA-DMBOK2 discute essas opções e observa que a certa depende da cultura, do porte e de como os dados são compartilhados. Lucía observa que os dados da Corran atravessam os departamentos o tempo todo, dos pedidos de vendas à operação e ao financeiro, o que pesa contra deixar as decisões inteiramente com cada departamento.

### 2.2 Escolhendo para a Corran

Lucía compara os modelos com a situação da Corran: uma sede, três centros de distribuição regionais, sistemas compartilhados e uma equipe de dados pequena. Um modelo totalmente centralizado sobrecarregaria a equipe de dados e ignoraria o conhecimento dos centros. Um modelo descentralizado perpetuaria as definições inconsistentes. Ela propõe um modelo federado: um escritório central de governança com duas pessoas define os padrões e cuida dos relatórios, enquanto os donos na operação, em vendas e no financeiro tomam as decisões de seus domínios dentro desses padrões. Lucía mostra a comparação em uma tabela curta, com uma linha por modelo e uma coluna por fator.

### 2.3 O grupo de governança

Ela redige o mandato de um grupo de governança presidido pelo diretor de operações (COO). O grupo aprova políticas e padrões, resolve disputas entre domínios, define prioridades para o trabalho de qualidade e revisa o desempenho a cada trimestre. Seus membros são os donos dos domínios e o chefe de TI. A ISO/IEC 38505-1 descreve o papel do órgão de governança como avaliar, dirigir e monitorar o uso dos dados, e Lucía associa cada item do mandato a uma dessas três atividades para mostrar que ele está completo. O diretor de operações revisa o rascunho do mandato e o aceita.

### 2.4 Começando pequeno

O Dr. Achebe adverte contra lançar um programa grande. Lucía propõe começar por um único conjunto de dados crítico, o rastreamento das remessas, em que as disputas geram custos claros. O sucesso ali daria credibilidade para estender o trabalho aos dados de clientes e de motoristas. Ela esboça um plano de seis meses e o apresenta à gerente, que concorda em levá-lo ao diretor de operações. Ela anota no diário que um começo estreito torna os resultados visíveis depressa, o que importa em uma empresa voltada à operação diária. O diretor o aprova.

### Exemplo resolvido

Lucía compara os modelos centralizado, federado e descentralizado, propõe um modelo federado com um escritório de duas pessoas, redige o mandato de um grupo de governança associado a avaliar, dirigir e monitorar e começa pelo rastreamento das remessas.

> **Caso sintético.** A Corran Freight é sintética; o DAMA-DMBOK2 e a ISO/IEC 38505-1:2017 são reais.

### Erros e limites

Lançar a governança sobre todos os dados de uma vez espalha o esforço demais.

### Exercícios

- **EX006 — Modelo escolhido.** Que modelo Lucía propôs? *Rubrica:* 3 = o federado;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.
- **EX007 — Tamanho do escritório.** Quantas pessoas compõem o escritório central? *Rubrica:* 3 = duas;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX008 — Presidência do grupo.** Quem preside o grupo de governança? *Rubrica:* 3 = o diretor de operações;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.
- **EX009 — Associação do mandato.** A que três atividades Lucía associou o mandato? *Rubrica:* 3 = avaliar, dirigir, monitorar;; 2 = todas;; 1 = algumas;; 0 = nenhuma.
- **EX010 — Primeiro conjunto de dados.** Que conjunto de dados vem primeiro? *Rubrica:* 3 = o rastreamento das remessas;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 12)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Titularidade de dados em uma rede logística

### Objetivos de aprendizagem

Você vai (1) atribuir a titularidade de dados internos e externos; (2) tratar os dados criados por parceiros; (3) escrever declarações de titularidade.

### 3.1 Domínios internos

Lucía mapeia os domínios de dados da Corran: clientes e contratos, de propriedade do diretor de vendas; remessas e rastreamento, do diretor de operações; motoristas e veículos, do gerente de frota; e faturas, do diretor financeiro. Cada dono designa um curador. Ela descobre que os eventos de rastreamento são território disputado: a operação os usa para planejar, vendas os cita aos clientes e o financeiro os usa para sustentar as faturas. Ela propõe a operação como dona, já que controla os processos que criam os eventos. Os demais concordam.

### 3.2 Dados de parceiros

As transportadoras enviam eventos de rastreamento das remessas que movimentam. A Corran não controla como as transportadoras capturam os eventos, mas decide como esses eventos são usados. Lucía distingue a titularidade da fonte, que fica com a transportadora, da responsabilização pelo uso que a Corran faz dos dados, que cabe ao diretor de operações. Ela observa que a governança de dados de parceiros funciona por meio de acordos e monitoramento, e não de controle direto, o que os capítulos seguintes sobre dados de terceiros desenvolvem. Lucía registra essa distinção na declaração de cada dono, para maior clareza.

### 3.3 Declarações de titularidade

Para cada domínio, Lucía escreve uma declaração de titularidade de uma página: os dados cobertos, as decisões que o dono toma, o curador, as principais expectativas de qualidade e os caminhos de escalonamento. A declaração do diretor de operações inclui aprovar as regras de qualidade do rastreamento e decidir quando os dados das transportadoras são confiáveis o bastante para sustentar reclamações de clientes. Os donos revisam e assinam suas declarações. Ela observa que escrever as decisões explicitamente revela lacunas, como ninguém ter autoridade para aprovar novos usos de dados. O grupo de governança atribui essa autoridade ao dono do domínio correspondente, com assessoria jurídica quando necessário.

### 3.4 Testando a titularidade

Para testar se a titularidade funciona, Lucía leva a cada dono um tipo real de pergunta: vendas pode compartilhar históricos de rastreamento com a seguradora de um cliente? O diretor de operações decide com a contribuição do jurídico, e a decisão é registrada. Ela observa que a titularidade só se torna real quando os donos de fato tomam decisões, e que perguntas de teste no início ajudam os donos a praticar seu papel antes que casos mais difíceis cheguem sob pressão. Lucía faz uma pergunta de teste desse tipo a cada dono no primeiro trimestre e registra cada decisão em um registro compartilhado, para consulta posterior.

### Exemplo resolvido

Lucía mapeia quatro domínios, atribui à operação os disputados eventos de rastreamento, separa a titularidade da fonte, do parceiro, da responsabilização pelo uso, escreve declarações de titularidade assinadas e as testa com uma pergunta sobre compartilhamento com uma seguradora.

> **Caso sintético.** As atribuições de titularidade são sintéticas.

### Erros e limites

Atribuir a titularidade a quem mais usa os dados ignora quem controla sua criação.

### Exercícios

- **EX011 — Dono do rastreamento.** Quem é dono dos eventos de rastreamento? *Rubrica:* 3 = o diretor de operações;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.
- **EX012 — Distinção dos parceiros.** O que fica com as transportadoras? *Rubrica:* 3 = a titularidade dos dados de origem;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX013 — Lacuna nas declarações.** Que lacuna as declarações revelaram? *Rubrica:* 3 = ninguém tinha autoridade para aprovar novos usos de dados;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX014 — Pergunta de teste.** Que pergunta de teste Lucía usou? *Rubrica:* 3 = se vendas pode compartilhar históricos de rastreamento com uma seguradora;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX015 — Assinatura.** Quem assina as declarações de titularidade? *Rubrica:* 3 = os donos;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 12)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Gestão da qualidade dos dados de remessas

### Objetivos de aprendizagem

Você vai (1) definir as expectativas de qualidade dos dados de remessas; (2) montar um ciclo de gestão da qualidade; (3) priorizar os problemas pelo custo.

### 4.1 Expectativas

Lucía trabalha com o curador da operação para definir as expectativas de qualidade dos dados de remessas. Cada remessa precisa ter cliente, origem, destino, janela de entrega prometida e situação válidos. O rastreamento precisa mostrar os eventos de coleta, chegada ao centro de distribuição, saída e entrega. O comprovante de entrega precisa incluir o horário e uma assinatura ou fotografia. Ela baseia as dimensões em Wang e Strong e a forma de medição na ISO 8000-8, registrando para cada expectativa como ela será medida e que limiar se aplica. O curador revisa cada limiar com os supervisores dos centros de distribuição antes da adoção.

### 4.2 O ciclo da qualidade

Ela monta um ciclo: definir as regras, medir os resultados todo dia, analisar as falhas toda semana, corrigir as causas e revisar as regras a cada trimestre. Isso espelha os ciclos de melhoria usados na operação, o que ajuda a equipe de operação a aceitá-lo. Os resultados alimentam um painel para o curador e um resumo semanal para o dono. Lucía observa que o valor do ciclo está na etapa de correção; medir sem corrigir as causas apenas documenta o declínio com mais detalhe. Lucía escreve o ciclo como um procedimento de uma página, e o curador o segue desde a primeira semana, com uma reunião curta toda sexta-feira para analisar as falhas.

### 4.3 O custo da má qualidade

Para priorizar, Lucía estima o custo das falhas de qualidade. A falta de comprovante de entrega leva a faturas contestadas que o financeiro acaba baixando como perda. Códigos de destino errados levam a remessas mal encaminhadas e a custos de reentrega. Eventos de rastreamento atrasados levam a ligações ao atendimento ao cliente. Usando números sintéticos baseados em volumes típicos, ela mostra que a falta de comprovante de entrega é a que mais custa. O grupo de governança concorda em atacá-la primeiro, já que seu efeito sobre a receita é direto e mensurável. Lucía mostra ao grupo o custo anual estimado de cada tipo de falha em um gráfico simples.

### 4.4 Corrigindo o comprovante de entrega

Lucía investiga os comprovantes ausentes. A maioria vem de uma transportadora cujos motoristas usam anotações em papel digitalizadas dias depois, e alguns vêm de motoristas da Corran cujos dispositivos portáteis perdem o sinal nas áreas rurais. A transportadora concorda em adotar o aplicativo móvel da Corran. Os dispositivos da Corran são atualizados para guardar os comprovantes sem conexão e enviá-los quando o sinal volta. Depois de dois meses, os comprovantes ausentes caem bastante, e as faturas contestadas diminuem. O Dr. Achebe observa que custear as falhas de qualidade tornou a priorização simples. Lucía registra os números de antes e depois no registro de qualidade.

### Exemplo resolvido

Lucía define as expectativas para remessas e rastreamento com suas medições, monta um ciclo de definir, medir, analisar, corrigir e revisar, classifica a falta de comprovante de entrega como a falha mais cara e corrige as anotações em papel da transportadora e o armazenamento sem conexão dos dispositivos.

> **Caso sintético.** Os números são sintéticos; Wang e Strong (1996) e a ISO 8000-8:2015 são reais.

### Erros e limites

Medir a qualidade sem corrigir as causas apenas documenta o declínio.

### Exercícios

- **EX016 — Conteúdo do comprovante.** O que o comprovante de entrega precisa incluir? *Rubrica:* 3 = o horário e uma assinatura ou fotografia;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.
- **EX017 — Falha mais cara.** Que falha custava mais? *Rubrica:* 3 = a falta de comprovante de entrega;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.
- **EX018 — Causa na transportadora.** Por que faltavam os comprovantes de uma transportadora? *Rubrica:* 3 = anotações em papel digitalizadas dias depois;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX019 — Correção dos dispositivos.** Como os dispositivos da Corran foram corrigidos? *Rubrica:* 3 = guardando os comprovantes sem conexão e enviando-os depois;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX020 — Valor do ciclo.** Onde está o valor do ciclo da qualidade? *Rubrica:* 3 = na etapa de correção;; 2 = parcialmente correto;; 1 = na medição;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 12)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Pontualidade dos eventos das transportadoras

### Objetivos de aprendizagem

Você vai (1) medir a pontualidade dos eventos por fonte; (2) comparar os parceiros com justiça; (3) usar os resultados na gestão dos parceiros.

### 5.1 Por que a pontualidade importa

Os clientes veem as atualizações de rastreamento no site da Corran e esperam que reflitam a realidade. Se um evento chega com uma hora de atraso, o cliente pode ligar perguntando onde está a remessa, ou um planejador pode despachar um veículo substituto sem necessidade. Lucía define a pontualidade como o atraso entre o momento em que o evento aconteceu e o momento em que a Corran o recebeu, e fixa a meta de que os eventos cheguem em até quinze minutos. Ela a mede separadamente para cada transportadora, já que cada uma usa sistemas diferentes. Os clientes percebem os atrasos depressa.

### Laboratório — Parcela de eventos sintéticos das transportadoras que chegam em até quinze minutos

```python
"""Share of synthetic shipment status events arriving within 15 minutes, by carrier (stdlib only)."""
import random
random.seed(9)
mean = {"Carrier A": 6, "Carrier B": 9, "Carrier C": 21}
for c, m in mean.items():
    d = [random.expovariate(1/m) for _ in range(3000)]
    print(f"{c}: within 15 min {100*sum(x <= 15 for x in d)/len(d):.1f}%")
```

Execute com `python3 lab_timeliness.py`. Saída verificada:

```text
Carrier A: within 15 min 91.9%
Carrier B: within 15 min 81.7%
Carrier C: within 15 min 51.0%
```

### 5.2 Resultados

O laboratório simula três mil eventos por transportadora. A Transportadora A entrega 91,9 por cento dos eventos em até quinze minutos, a Transportadora B, 81,7 por cento, e a Transportadora C, apenas 51,0 por cento. Lucía observa que a diferença é grande o bastante para importar aos clientes: as remessas movimentadas pela Transportadora C vão mostrar uma situação desatualizada cerca de metade do tempo. Ela verifica que a composição sintética dos eventos é semelhante entre as transportadoras, para que a comparação não seja distorcida por tipos de remessa ou rotas diferentes. Ela apresenta as parcelas em uma tabela, com o número de eventos por trás de cada número.

### 5.3 Comparação justa

Antes de apresentar os resultados, Lucía pensa na justiça da comparação. Na realidade, a Transportadora C opera mais rotas rurais, onde o sinal é mais fraco, de modo que parte do atraso pode estar fora de seu controle. Ela planeja comparar as transportadoras em rotas semelhantes em um estudo de acompanhamento e discutir os resultados com cada transportadora antes de tirar conclusões. O Dr. Achebe observa que a governança de dados de parceiros depende de cooperação, e que apresentar os resultados como problemas compartilhados costuma funcionar melhor do que apresentá-los como acusações. Ela registra esse plano no diário e o compartilha com o Dr. Achebe para comentários.

### 5.4 Usando os resultados

Lucía compartilha os resultados com cada transportadora. A Transportadora C explica que seu sistema envia os eventos em lotes a cada meia hora para economizar no custo dos dados móveis. A Corran se oferece para cobrir a diferença de custo do envio em tempo real em suas remessas, avaliando que menos ligações de clientes vão compensá-la. A Transportadora C concorda. Lucía acrescenta metas de pontualidade aos acordos com as transportadoras que estão para ser renovados e agenda relatórios mensais dos resultados de cada uma. Os resultados do mês seguinte mostram os eventos da Transportadora C chegando muito mais rápido, e as ligações de clientes sobre suas remessas começam a cair.

### Exemplo resolvido

Lucía mede o atraso dos eventos por transportadora, encontra 91,9, 81,7 e 51,0 por cento em até quinze minutos, considera as diferenças de rota, descobre que a Transportadora C envia os eventos em lotes a cada meia hora e acorda o envio em tempo real, com metas.

> **Caso sintético.** Os eventos são sintéticos; as saídas vêm de lab_timeliness.py.

### Erros e limites

Comparar parceiros sem considerar suas condições pode ser injusto.

### Exercícios

- **EX021 — Definição de pontualidade.** Como Lucía definiu a pontualidade? *Rubrica:* 3 = o atraso entre o evento e seu recebimento pela Corran;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX022 — Parcela da Transportadora C.** Que parcela dos eventos da Transportadora C chegou em até quinze minutos? *Rubrica:* 3 = 51,0%;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX023 — Fator de justiça.** O que pode explicar em parte os atrasos da Transportadora C? *Rubrica:* 3 = mais rotas rurais, com sinal mais fraco;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX024 — Causa real.** Que causa a Transportadora C revelou? *Rubrica:* 3 = o envio dos eventos em lotes a cada meia hora;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX025 — Mudança nos acordos.** O que foi acrescentado aos acordos em renovação? *Rubrica:* 3 = metas de pontualidade;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — aula 05 (capítulo 05 de 12)

[← Capítulo 04](#ch-04) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Metadados, linhagem e catálogo

### Objetivos de aprendizagem

Você vai (1) documentar as definições por trás das medidas principais; (2) rastrear a linhagem de uma medida do conselho; (3) montar um catálogo leve.

### 6.1 Definições

A medida de entregas no prazo do conselho conta as remessas entregues até o fim do dia prometido. Os contratos com os clientes definem no prazo como dentro da janela de entrega prometida, muitas vezes de duas horas. O conselho vê mais de noventa por cento no prazo, enquanto os clientes reclamam. Lucía documenta as duas definições em um glossário e propõe que a medida do conselho siga as janelas dos contratos, com a medida antiga renomeada como entrega no mesmo dia. O grupo de governança concorda, aceitando que o número relatado vai cair. Lucía escreve as duas definições no glossário, com suas fontes.

### 6.2 Linhagem

Lucía rastreia a medida de entregas no prazo do relatório do conselho de volta, pelo banco de dados de relatórios e pelo sistema de remessas, até os eventos de rastreamento dos dispositivos da Corran e das transportadoras. Ela descobre que as remessas sem evento de entrega são simplesmente excluídas da medida, em vez de contadas como atrasadas ou desconhecidas. Isso infla o número. Ela registra a linhagem no catálogo e recomenda que os eventos de entrega ausentes sejam contados como desconhecidos e informados separadamente. O diretor de operações aprova a mudança, e o relatório do conselho ganha uma linha separada para a situação de entrega desconhecida.

### 6.3 Um catálogo leve

A Corran não tem ferramenta de catálogo. Lucía cria entradas na wiki que a empresa já usa para os doze conjuntos de dados e medidas mais usados, cada uma com descrição, dono, curador, fonte, horário de atualização, links para as definições e problemas conhecidos. Ela pede aos curadores que atualizem as entradas quando houver mudanças. Em poucas semanas, os planejadores começam a citar links das entradas nos e-mails. Ela observa que um catálogo modesto que as pessoas usam é melhor do que um ambicioso que espera orçamento. Os curadores atualizam as entradas na reunião semanal de qualidade.

### 6.4 Comunicando a mudança

Quando a medida do conselho muda, o número relatado cai bruscamente. Lucía prepara uma nota curta explicando a nova definição, por que ela corresponde aos contratos e como o número antigo superestimava o desempenho. Ela inclui os dois números por três meses, para que o conselho veja a transição. O Dr. Achebe observa que mudar definições sem explicação destrói a confiança, enquanto explicar abertamente gera confiança de que o novo número é mais honesto. O conselho aceita a nova medida, e o presidente pede que as futuras mudanças de definição sejam sempre explicadas da mesma forma, com os dois números lado a lado.

### Exemplo resolvido

Lucía documenta definições conflitantes de no prazo e alinha a medida do conselho às janelas dos contratos, encontra remessas sem evento de entrega excluídas, monta entradas de catálogo na wiki e explica ao conselho a queda do número.

> **Caso sintético.** As medidas são sintéticas.

### Erros e limites

Excluir registros com eventos ausentes infla os números de desempenho.

### Exercícios

- **EX026 — Definição dos contratos.** Como os contratos definem no prazo? *Rubrica:* 3 = dentro da janela de entrega prometida;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX027 — Constatação da exclusão.** O que a linhagem revelou? *Rubrica:* 3 = remessas sem evento de entrega eram excluídas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX028 — Plataforma do catálogo.** Onde Lucía montou as entradas de catálogo? *Rubrica:* 3 = na wiki da empresa;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.
- **EX029 — Período de transição.** Por quanto tempo os dois números foram mostrados? *Rubrica:* 3 = três meses;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX030 — Nome da medida antiga.** Como a medida antiga foi renomeada? *Rubrica:* 3 = entrega no mesmo dia;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — aula 06 (capítulo 06 de 12)

[← Capítulo 05](#ch-05) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Governança de acessos

### Objetivos de aprendizagem

Você vai (1) revisar o acesso a um conjunto de dados governado; (2) encontrar contas inativas e não aprovadas; (3) instituir revisões periódicas pelos donos.

### 7.1 Por que revisar os acessos

O acesso ao conjunto de dados de remessas cresceu ao longo dos anos, à medida que pessoas entraram, mudaram de função e saíram. A TI concede acesso a pedido, muitas vezes sem consultar o dono. Lucía explica que cada conta desnecessária aumenta a chance de mau uso ou de que uma senha comprometida exponha dados de clientes e motoristas. Ela propõe uma revisão, a ser aprovada pelo diretor de operações como dono, que compara o último uso e o registro de aprovação de cada conta com as regras acordadas sobre quem deve ter acesso. O dono aprova o plano de revisão em uma semana.

### Laboratório — Contas inativas e não aprovadas em um conjunto sintético de dados de remessas

```python
"""Review access to a synthetic shipment data set: stale and unapproved accounts (stdlib only)."""
import random, datetime as dt
random.seed(5)
today = dt.date(2026, 3, 31)
acc = []
for i in range(240):
    last = today - dt.timedelta(days=min(400, int(random.expovariate(1/45))))
    approved = random.random() > 0.07
    acc.append((f"u{i:03d}", last, approved))
stale = [a for a in acc if (today - a[1]).days > 90]
unapp = [a for a in acc if not a[2]]
both = [a for a in stale if not a[2]]
print(f"accounts {len(acc)}; unused over 90 days {len(stale)} ({100*len(stale)/len(acc):.1f}%)")
print(f"no owner approval {len(unapp)}; stale and unapproved {len(both)}")
```

Execute com `python3 lab_access.py`. Saída verificada:

```text
accounts 240; unused over 90 days 30 (12.5%)
no owner approval 17; stale and unapproved 2
```

### 7.2 Resultados

O laboratório revisa 240 contas sintéticas com a data de referência de 31 de março de 2026. Trinta contas, 12,5 por cento, não são usadas há mais de noventa dias. Dezessete não têm registro de aprovação do dono. Duas contas são, ao mesmo tempo, inativas e não aprovadas, o que as torna a maior prioridade de remoção, já que ninguém as aprovou e ninguém parece usá-las. Lucía observa que contas inativas e contas não aprovadas são problemas diferentes, com correções diferentes, e por isso os relata separadamente. Lucía compartilha as listas com o diretor de operações no mesmo dia, para as decisões.

### 7.3 Agindo sobre os resultados

O diretor de operações revisa a lista. As contas inativas são desativadas depois que os gestores de seus titulares confirmam que não há necessidade; três são mantidas para pessoas em licença longa, com uma anotação e uma data de expiração. As contas não aprovadas são revistas uma a uma: a maioria é legítima e recebe aprovação retroativa, enquanto algumas pertencem a terceirizados cujo trabalho terminou, e essas são removidas. As duas contas presentes nos dois grupos são removidas imediatamente. Cada decisão é registrada com sua razão. A revisão leva três semanas para ser concluída por inteiro.

### 7.4 Tornando-a periódica

Lucía propõe revisões trimestrais de acesso para o conjunto de dados de remessas e semestrais para os conjuntos menos sensíveis. A TI muda o processo de solicitação para que novos acessos exijam a aprovação do dono, registrada automaticamente. As contas de quem sai da empresa são desativadas pelo processo de desligamento do RH. O Dr. Achebe observa que limpezas pontuais se degradam depressa, e que uma governança de acessos sustentável depende de mudar os processos que criaram o problema, além de corrigir sua situação atual. A primeira revisão trimestral depois dessas mudanças encontra muito menos contas inativas, o que sugere que as mudanças de processo estão funcionando.

### Exemplo resolvido

Lucía revisa 240 contas, encontra 30 sem uso há mais de noventa dias (12,5 por cento), 17 não aprovadas e 2 nos dois grupos, faz o dono decidir sobre cada uma com razões registradas e torna periódicas as revisões e as aprovações.

> **Caso sintético.** As contas são sintéticas; as saídas vêm de lab_access.py.

### Erros e limites

Limpezas sem mudança de processo se degradam depressa.

### Exercícios

- **EX031 — Parcela inativa.** Que parcela das contas estava sem uso há mais de noventa dias? *Rubrica:* 3 = 12,5% (30 de 240);; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.
- **EX032 — Maior prioridade.** Que contas tinham a maior prioridade? *Rubrica:* 3 = as duas inativas e não aprovadas ao mesmo tempo;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX033 — Tratamento das licenças longas.** Como as contas de pessoas em licença longa foram tratadas? *Rubrica:* 3 = mantidas com uma anotação e uma data de expiração;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX034 — Mudança na solicitação.** Como a TI mudou o processo de solicitação? *Rubrica:* 3 = novos acessos exigem aprovação registrada do dono;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX035 — Controle dos desligamentos.** Como são tratadas as contas de quem sai? *Rubrica:* 3 = desativadas pelo processo de desligamento do RH;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — aula 07 (capítulo 07 de 12)

[← Capítulo 06](#ch-06) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Privacidade e dados de motoristas

### Objetivos de aprendizagem

Você vai (1) avaliar os riscos de privacidade da telemetria veicular; (2) aplicar a limitação da finalidade e a minimização; (3) envolver as pessoas afetadas.

### 8.1 Telemetria

Os caminhões da Corran registram localização, velocidade, frenagem e dados do motor a cada poucos segundos. Esses dados sustentam o planejamento de rotas, a eficiência de combustível e a segurança. Como cada caminhão é atribuído a um motorista, os dados são dados pessoais dos motoristas segundo o GDPR, e também o seriam segundo a LGPD. Lucía descobre que os gestores passaram a usar a telemetria para monitorar os horários de descanso dos motoristas, finalidade que não consta do aviso de privacidade dos motoristas. Ela leva o caso ao encarregado de proteção de dados como um possível problema de limitação da finalidade. O encarregado concorda e abre uma avaliação.

### 8.2 Avaliação

Lucía ajuda o encarregado de proteção de dados a realizar uma avaliação de impacto sobre a proteção de dados da telemetria; no Brasil, o instrumento correspondente é o relatório de impacto à proteção de dados pessoais previsto na LGPD (art. 5º, XVII, e art. 38). A avaliação descreve o tratamento, avalia a necessidade e a proporcionalidade, identifica os riscos para os motoristas, como punições injustas baseadas em dados mal interpretados, e propõe salvaguardas. As funções governar e controlar do NIST Privacy Framework ajudam a estruturar as salvaguardas: políticas sobre os usos permitidos, acesso limitado por papel e retenção dos dados detalhados de localização por noventa dias, com os agregados guardados por mais tempo. A avaliação é assinada pelo encarregado e pelo gerente de frota, como dono.

### 8.3 Envolvendo os motoristas

A avaliação recomenda consultar os motoristas. Lucía ajuda a organizar sessões com representantes dos motoristas. Os motoristas aceitam os usos para segurança e rotas, mas se opõem ao monitoramento minuto a minuto dos descansos, lembrando que as regras legais de descanso já são registradas pelos tacógrafos. A Corran concorda que a telemetria não será usada para monitorar os descansos e que qualquer uso disciplinar exigirá a revisão de um segundo gestor, com a presença do representante do motorista. O aviso de privacidade é atualizado para descrever com clareza os usos permitidos. Os representantes dos motoristas revisam o novo aviso antes que ele seja enviado a todos os motoristas.

### 8.4 Minimização

Lucía examina se todos os dados coletados são necessários. Os dados do motor com detalhe segundo a segundo servem à manutenção, mas não ao planejamento; ela propõe que os planejadores recebam os dados agregados por viagem. A localização fora do horário de trabalho, quando em alguns centros os motoristas levam os caminhões para casa, é desligada. O Dr. Achebe observa que essas mudanças reduziram o risco sem perder o benefício operacional, e que envolver os motoristas produziu salvaguardas melhores do que os gestores teriam desenhado sozinhos. O gerente de frota aprova as duas mudanças, e a avaliação é atualizada para registrá-las, com a data de cada decisão.

### Exemplo resolvido

Lucía encontra a telemetria usada para monitorar descansos sem aviso, apoia uma avaliação de impacto com acesso por papel e retenção de noventa dias, consulta os motoristas, que rejeitam o monitoramento dos descansos, e minimiza os dados do motor e a localização fora do expediente.

> **Caso sintético.** As práticas são sintéticas; o GDPR, a LGPD e o NIST Privacy Framework 1.0 são reais. Isto não é aconselhamento jurídico.

### Erros e limites

Novos usos de dados de empregados sem aviso violam a limitação da finalidade.

### Exercícios

- **EX036 — Uso sem aviso.** Que uso sem aviso Lucía encontrou? *Rubrica:* 3 = o monitoramento dos horários de descanso dos motoristas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX037 — Retenção da localização.** Por quanto tempo os dados detalhados de localização são guardados? *Rubrica:* 3 = noventa dias;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX038 — Objeção dos motoristas.** A que os motoristas se opuseram? *Rubrica:* 3 = ao monitoramento minuto a minuto dos descansos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX039 — Salvaguarda disciplinar.** Que salvaguarda se aplica ao uso disciplinar? *Rubrica:* 3 = revisão de um segundo gestor, com a presença do representante;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.
- **EX040 — Dados fora do expediente.** O que acontece com a localização fora do horário de trabalho? *Rubrica:* 3 = é desligada;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — aula 08 (capítulo 08 de 12)

[← Capítulo 07](#ch-07) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Dados de terceiros e contratos

### Objetivos de aprendizagem

Você vai (1) governar os dados trocados com parceiros; (2) incluir cláusulas de dados nos contratos; (3) monitorar o cumprimento pelos parceiros.

### 9.1 Fluxos de dados com parceiros

A Corran troca dados com transportadoras, clientes, um fornecedor de cartões de combustível, uma seguradora e um fornecedor de software que hospeda a plataforma de rastreamento. Lucía lista cada fluxo: os dados enviados e recebidos, a finalidade, a base legal e as cláusulas contratuais atuais. Ela descobre que o fornecedor da plataforma de rastreamento trata dados de clientes e motoristas em nome da Corran, mas o contrato não tem as cláusulas de operador exigidas pelo artigo 28 do GDPR; a LGPD trata das obrigações do operador nos arts. 37 a 39. A equipe jurídica prioriza a atualização desse contrato. Lucía encontra também dois fluxos sem nenhum acordo escrito, que o jurídico acrescenta à sua lista.

### 9.2 Cláusulas de dados

Lucía redige com o jurídico cláusulas-padrão de dados: finalidade, obrigações de qualidade dos dados, como metas de pontualidade, segurança, compartilhamento posterior, retenção, notificação de incidentes em prazo definido, direito de auditoria e devolução ou eliminação ao final. Para as transportadoras, as cláusulas de qualidade são as mais importantes; para o fornecedor da plataforma, as de segurança e de operador. Ela observa que cláusulas-padrão aceleram as negociações e garantem que as obrigações sobre dados não sejam esquecidas quando os termos comerciais dominam a discussão. O jurídico aprova as cláusulas, que são usadas nas três renovações de contrato seguintes.

### 9.3 Monitorando os parceiros

As cláusulas precisam de monitoramento. Lucía desenha um painel de indicadores dos parceiros, com pontualidade, completude e notificação de incidentes para cada transportadora, revisado todo mês com ela. Do fornecedor da plataforma, ela pede todo ano o relatório independente de garantia de segurança e verifica se os controles acordados aparecem nele. Quando uma transportadora não cumpre as metas de pontualidade por três meses seguidos, a cláusula de escalonamento do acordo aciona um plano conjunto de melhoria, em vez de penalidades imediatas. O plano define ações dos dois lados, como a Corran corrigir os erros de sua própria interface e a transportadora atualizar seus dispositivos, com uma data para revisarem juntas o progresso.

### 9.4 Encerrando as relações

Quando a Corran troca de fornecedor de cartões de combustível, Lucía verifica se o fornecedor antigo devolve ou elimina os dados da Corran, como o contrato exige. O fornecedor confirma a eliminação por escrito, e Lucía registra a confirmação. Ela verifica também se os sistemas da própria Corran deixam de enviar dados ao fornecedor antigo. O Dr. Achebe observa que a saída é a etapa mais negligenciada da governança de parceiros, e que confirmar a eliminação protege tanto a empresa quanto as pessoas cujos dados foram compartilhados. Ela acrescenta uma lista de verificação de saída ao procedimento.

### Exemplo resolvido

Lucía lista os fluxos com parceiros, encontra a falta de cláusulas de operador no contrato do fornecedor da plataforma, redige cláusulas-padrão de dados, monitora as transportadoras com painéis e o fornecedor com relatórios de garantia e confirma a eliminação ao trocar de fornecedor.

> **Caso sintético.** Os parceiros são sintéticos; o artigo 28 do GDPR e a LGPD são reais.

### Erros e limites

Contratos negociados apenas em termos comerciais muitas vezes omitem as obrigações sobre dados.

### Exercícios

- **EX041 — Cláusulas ausentes.** O que faltava no contrato do fornecedor da plataforma? *Rubrica:* 3 = as cláusulas de operador do artigo 28 do GDPR;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX042 — Foco das cláusulas para transportadoras.** Que cláusulas importam mais para as transportadoras? *Rubrica:* 3 = as obrigações de qualidade;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.
- **EX043 — Garantia do fornecedor.** O que Lucía pede todo ano ao fornecedor? *Rubrica:* 3 = seu relatório independente de garantia de segurança;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX044 — Três meses de descumprimento.** O que acontece depois de três meses de metas não cumpridas? *Rubrica:* 3 = um plano conjunto de melhoria;; 2 = parcialmente correto;; 1 = penalidades;; 0 = nenhuma.
- **EX045 — Verificação de saída.** O que Lucía confirmou ao trocar de fornecedor de cartões de combustível? *Rubrica:* 3 = a confirmação escrita da eliminação;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue estudando — aula 09 (capítulo 09 de 12)

[← Capítulo 08](#ch-08) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Métricas, relatórios e o conselho

### Objetivos de aprendizagem

Você vai (1) desenhar métricas de governança para executivos; (2) ligar as métricas aos resultados do negócio; (3) relatar o progresso com honestidade.

### 10.1 Escolhendo as métricas

Lucía escolhe um conjunto pequeno de métricas de governança para o conselho: completude dos comprovantes de entrega, pontualidade dos eventos das transportadoras, entregas no prazo segundo as definições dos contratos, valor das faturas contestadas, conclusão das revisões de acesso e problemas de dados de alta prioridade em aberto. Cada uma se liga a um resultado que importa ao conselho, como a receita perdida em disputas. Ela evita métricas que medem apenas atividade, como o número de reuniões realizadas, que dizem pouco sobre se a governança melhora o negócio. O grupo de governança revisa a lista e acorda cada meta com o dono correspondente antes do primeiro relatório.

### 10.2 Montando o relatório

O relatório trimestral cabe em duas páginas: uma tabela de métricas com metas e tendências, três destaques, três preocupações e as decisões necessárias. Lucía escreve em linguagem simples e explica qualquer mudança de definição. Ela inclui um gráfico do valor das faturas contestadas antes e depois da correção dos comprovantes de entrega. Ela observa que os conselhos têm pouco tempo, então os relatórios devem facilitar ver o que está funcionando, o que não está e o que o conselho precisa decidir. O presidente do conselho acolhe o formato.

### 10.3 Atribuição

O conselho pergunta se a governança causou a queda nas faturas contestadas. Lucía explica que as correções dos comprovantes de entrega são a causa mais provável, já que as disputas caíram sobretudo nas remessas da transportadora que trocou de aplicativo, mas que outros fatores, como um novo modelo de contrato com os clientes, também podem ter contribuído. Ela apresenta as evidências e seus limites. O Dr. Achebe observa que uma atribuição honesta protege a credibilidade quando os resultados futuros forem menos favoráveis. Ela inclui uma nota curta sobre esses limites logo abaixo do gráfico.

### 10.4 Decisões

O relatório pede ao conselho duas decisões: financiamento para estender a governança aos dados mestres de clientes e aprovação de uma política segundo a qual todo novo compartilhamento de dados exige a aprovação de um dono. O conselho aprova as duas. Lucía registra as decisões e seus responsáveis. Ela reflete que ligar a governança a resultados financeiros visíveis tornou o conselho receptivo, e que pedir decisões específicas transformou o relatório de informação em ação. As duas decisões aparecem no relatório seguinte com seu andamento, para que o conselho veja que suas aprovações levaram a ações.

### Exemplo resolvido

Lucía escolhe métricas ligadas a resultados, escreve um relatório de duas páginas para o conselho com destaques, preocupações e decisões, atribui com cautela a queda das disputas e obtém financiamento e uma política de compartilhamento.

> **Caso sintético.** As métricas são sintéticas.

### Erros e limites

Reivindicar todo o crédito por melhorias com várias causas prejudica a credibilidade.

### Exercícios

- **EX046 — Métrica de atividade.** Que tipo de métrica Lucía evitou? *Rubrica:* 3 = métricas apenas de atividade, como reuniões realizadas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX047 — Tamanho do relatório.** Qual é o tamanho do relatório trimestral? *Rubrica:* 3 = duas páginas;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.
- **EX048 — Outra causa.** Que outro fator pode reduzir as disputas? *Rubrica:* 3 = um novo modelo de contrato com os clientes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX049 — Aprovações do conselho.** O que o conselho aprovou? *Rubrica:* 3 = financiamento para os dados mestres de clientes e uma política de aprovação de compartilhamentos;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX050 — Propósito do relatório.** O que transformou o relatório em ação? *Rubrica:* 3 = pedir decisões específicas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue estudando — aula 10 (capítulo 10 de 12)

[← Capítulo 09](#ch-09) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Projeto final

### Objetivos de aprendizagem

Você vai (1) desenhar uma intervenção de governança como projeto final; (2) implementá-la com as partes interessadas; (3) avaliar os resultados em relação a uma linha de base.

### 11.1 Escolhendo a intervenção

Para seu projeto final, Lucía escolhe governar os dados de endereço dos clientes, que o conselho financiou. Os endereços diferem entre o sistema de pedidos e o de faturamento, causando faturas mal entregues e entregas que falham. Ela define o problema com uma linha de base: a parcela de clientes cujos endereços diferem entre os sistemas, as entregas falhas atribuídas a erros de endereço e as faturas devolvidas sem entrega. Ela acorda os critérios de sucesso com o diretor de vendas, como dono, e com o Dr. Achebe, como orientador, antes de começar. Ela registra os números da linha de base no diário do projeto antes de qualquer mudança nos sistemas.

### 11.2 Desenho

Lucía desenha a intervenção: o sistema de pedidos passa a ser a fonte oficial dos endereços de entrega, e o de faturamento, a dos endereços de cobrança, com regras claras sobre que mudanças fluem para onde. Um curador em vendas revisa as divergências toda semana. A validação de endereços é acrescentada na entrada do pedido, com uma consulta de CEP. Os clientes podem atualizar seus endereços por um portal que grava no sistema oficial. Ela registra cada escolha de desenho em um registro de decisão, com as alternativas consideradas. O diretor de vendas aprova o desenho depois de uma revisão com a TI e com a equipe de faturamento.

### 11.3 Implementação

A implementação leva quatro meses. A TI constrói os fluxos de endereço e a validação; vendas treina as pessoas no portal. Lucía faz verificações semanais e encontra um problema inesperado: alguns clientes têm vários locais de entrega válidos, que o desenho original tratava como divergências. Ela revê as regras para permitir vários locais de entrega por cliente, com um único endereço de cobrança. Ela observa que a implementação revela premissas que as discussões de desenho deixaram escapar, e por isso o monitoramento durante a implantação importa. As regras revistas são testadas em casos sintéticos antes de entrar em produção.

### 11.4 Avaliação

Depois da implementação, Lucía compara os resultados com a linha de base usando números sintéticos que espelham suas observações. As divergências de endereço, as entregas falhas por erro de endereço e as faturas devolvidas caem. Ela verifica se outras mudanças coincidiram e encontra uma queda sazonal de volume que poderia explicar em parte as falhas a menos, e ajusta suas afirmações. Ela documenta os limites e recomenda manter o monitoramento. O Dr. Achebe aprova a avaliação como equilibrada e bem fundamentada. Ela apresenta os números de antes e depois em uma tabela curta, com uma nota ao lado de cada número explicando como foi medido.

### Exemplo resolvido

Lucía governa os endereços dos clientes com uma linha de base e critérios acordados, desenha fontes oficiais, revisão por um curador, validação e um portal, ajusta as regras para vários locais de entrega e avalia com cautela em relação à linha de base.

> **Caso sintético.** O projeto e os números são sintéticos.

### Erros e limites

Avaliar sem uma linha de base torna impossível mostrar melhora.

### Exercícios

- **EX051 — Problema dos endereços.** Que problemas as diferenças de endereço causavam? *Rubrica:* 3 = faturas mal entregues e entregas falhas;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX052 — Fonte dos endereços de entrega.** Que sistema é a fonte oficial dos endereços de entrega? *Rubrica:* 3 = o sistema de pedidos;; 2 = parcialmente correto;; 1 = o de faturamento;; 0 = nenhuma.
- **EX053 — Surpresa.** Que problema inesperado apareceu? *Rubrica:* 3 = clientes com vários locais de entrega válidos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX054 — Mudança coincidente.** Que mudança coincidente Lucía encontrou? *Rubrica:* 3 = uma queda sazonal de volume;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX055 — Método de validação.** Como os endereços são validados na entrada? *Rubrica:* 3 = com uma consulta de CEP;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue estudando — aula 11 (capítulo 11 de 12)

[← Capítulo 10](#ch-10) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Apresentação do projeto final e próximos passos

### Objetivos de aprendizagem

Você vai (1) apresentar um projeto final a avaliadores acadêmicos e do setor; (2) refletir sobre seu desenvolvimento profissional; (3) planejar a governança para além do curso.

### 12.1 A apresentação

Lucía apresenta seu projeto final ao Dr. Achebe, a um segundo acadêmico e ao diretor de operações da Corran. Em vinte minutos, ela cobre o problema, a linha de base, o desenho, a implementação, a avaliação e os limites. O diretor de operações pergunta como as regras de endereço serão mantidas depois que o curso de Lucía terminar. Ela explica que o curador de vendas é responsável pela revisão semanal, que as regras estão documentadas no catálogo e que o grupo de governança revisa as métricas de endereço a cada trimestre. O diretor fica satisfeito com a resposta e confirma os arranjos.

### 12.2 Perguntas dos avaliadores

O segundo acadêmico pergunta como Lucía separou o efeito de sua intervenção das mudanças sazonais. Ela explica a comparação com o mesmo período do ano anterior e reconhece que ela é imperfeita. Ele pergunta também o que ela faria diferente. Ela diz que teria verificado a estrutura de locais dos clientes antes de desenhar as regras. Os avaliadores elogiam sua franqueza e a ligação clara entre as ações de governança e os resultados do negócio ao longo de todo o projeto. Lucía anota a devolutiva no diário reflexivo, para uso posterior.

### 12.3 Reflexão profissional

Em seu ensaio reflexivo final, Lucía observa como seu papel mudou: de analista que produz relatórios a profissional que lidera a governança entre departamentos. Ela aprendeu a formular os problemas pelo efeito no negócio, a envolver as pessoas afetadas, como os motoristas, a negociar com parceiros e a se apresentar com honestidade ao conselho. Ela registra também as dificuldades, como questionar colegas mais seniores, e como as evidências e a titularidade acordada facilitaram essas conversas ao longo do tempo. Ela observa ainda que o diário reflexivo a ajudou a perceber padrões em seu próprio progresso que, de outro modo, teria deixado escapar.

### 12.4 Próximos passos

Lucía propõe próximos passos para a Corran: estender a governança aos dados de faturas, automatizar os painéis dos parceiros e fazer uma avaliação de maturidade anual. Ela é promovida a líder de governança de dados. O Dr. Achebe lembra-lhe que a governança nunca termina, porque os negócios e as regulações mudam. O próximo curso desta área trata de privacidade e proteção de dados, onde os dados governados encontram os direitos das pessoas que eles descrevem. Lucía agradece ao Dr. Achebe e aos colegas da Corran e planeja ser mentora do próximo analista da empresa que entrar no curso.

### Exemplo resolvido

Lucía apresenta o projeto final, explica como a governança dos endereços será sustentada, responde a perguntas sobre sazonalidade e sobre o que faria diferente, reflete sobre seu desenvolvimento e é promovida a líder de governança.

> **Caso sintético.** A apresentação é sintética.

### Erros e limites

Projetos finais que terminam sem um responsável por sustentar as mudanças se apagam.

### Exercícios

- **EX056 — Sustentando as regras.** Quem fica responsável pela revisão semanal dos endereços depois? *Rubrica:* 3 = o curador de vendas;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.
- **EX057 — Método para a sazonalidade.** Como Lucía tratou a sazonalidade? *Rubrica:* 3 = comparando com o mesmo período do ano anterior;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX058 — Olhar retrospectivo.** O que Lucía faria diferente? *Rubrica:* 3 = verificar a estrutura de locais dos clientes antes de desenhar as regras;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX059 — Nova função.** Que função Lucía assume em seguida? *Rubrica:* 3 = líder de governança de dados;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.
- **EX060 — Extensão proposta.** Que dados serão governados em seguida? *Rubrica:* 3 = os dados de faturas;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue estudando — aula 12 (capítulo 12 de 12)

[← Capítulo 11](#ch-11) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. Lucía Herrera, o Dr. Samuel Achebe, a Westbridge Business School, a Corran Freight e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Uma pós-graduação de dois anos em tempo parcial para profissionais.

**EX002.** Cerca de doze mil.

**EX003.** Elas diferem das definições dos contratos com os clientes.

**EX004.** Não ver o que quem está de fora veria e hesitar em questionar os colegas.

**EX005.** Pelo efeito no negócio, como as faturas contestadas.

**EX006.** Um modelo federado.

**EX007.** Duas.

**EX008.** O diretor de operações.

**EX009.** Avaliar, dirigir e monitorar.

**EX010.** O rastreamento das remessas.

**EX011.** O diretor de operações.

**EX012.** A titularidade sobre como os dados de origem são capturados.

**EX013.** Ninguém tinha autoridade para aprovar novos usos de dados.

**EX014.** Se vendas pode compartilhar históricos de rastreamento com a seguradora de um cliente.

**EX015.** Os próprios donos.

**EX016.** O horário mais uma assinatura ou fotografia.

**EX017.** A falta de comprovante de entrega.

**EX018.** Seus motoristas usavam anotações em papel digitalizadas dias depois.

**EX019.** Agora guardam os comprovantes sem conexão e os enviam quando o sinal volta.

**EX020.** Na etapa de correção.

**EX021.** O atraso entre o momento em que o evento aconteceu e o momento em que a Corran o recebeu.

**EX022.** 51,0 por cento.

**EX023.** Mais rotas rurais, com sinal mais fraco.

**EX024.** Seu sistema enviava os eventos em lotes a cada meia hora.

**EX025.** Metas de pontualidade com relatórios mensais.

**EX026.** Dentro da janela de entrega prometida.

**EX027.** Remessas sem eventos de entrega eram excluídas da medida.

**EX028.** Na wiki que a empresa já usava.

**EX029.** Três meses.

**EX030.** Entrega no mesmo dia.

**EX031.** 12,5 por cento, 30 de 240.

**EX032.** As duas contas que eram, ao mesmo tempo, inativas e não aprovadas.

**EX033.** Mantidas com uma anotação e uma data de expiração.

**EX034.** Novos acessos agora exigem a aprovação do dono, registrada automaticamente.

**EX035.** Desativadas pelo processo de desligamento do RH.

**EX036.** Gestores monitorando os horários de descanso dos motoristas.

**EX037.** Noventa dias, com os agregados guardados por mais tempo.

**EX038.** O monitoramento minuto a minuto dos descansos.

**EX039.** Revisão por um segundo gestor, com a presença do representante do motorista.

**EX040.** A coleta é desligada.

**EX041.** As cláusulas de operador exigidas pelo artigo 28 do GDPR.

**EX042.** Obrigações de qualidade dos dados, como a pontualidade.

**EX043.** Seu relatório independente de garantia de segurança.

**EX044.** Um plano conjunto de melhoria.

**EX045.** A confirmação escrita de que o fornecedor antigo eliminou os dados da Corran.

**EX046.** Métricas apenas de atividade, como as reuniões realizadas.

**EX047.** Duas páginas.

**EX048.** Um novo modelo de contrato com os clientes.

**EX049.** Financiamento para os dados mestres de clientes e uma política de compartilhamento com aprovação do dono.

**EX050.** Pedir ao conselho decisões específicas.

**EX051.** Faturas mal entregues e entregas falhas.

**EX052.** O sistema de pedidos.

**EX053.** Clientes com vários locais de entrega válidos.

**EX054.** Uma queda sazonal no volume de remessas.

**EX055.** Com uma consulta de CEP.

**EX056.** O curador de vendas.

**EX057.** Comparando com o mesmo período do ano anterior.

**EX058.** Verificar a estrutura de locais dos clientes antes de desenhar as regras.

**EX059.** Líder de governança de dados.

**EX060.** Os dados de faturas.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da LGPD, citada nesta edição como referência brasileira; nenhuma das normas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO. (2015). *ISO 8000-8:2015 Data quality — Part 8: Information and data quality: Concepts and measuring*. International Organization for Standardization. <https://www.iso.org/standard/60805.html>
- ISO/IEC. (2017). *ISO/IEC 38505-1:2017 Information technology — Governance of IT — Governance of data — Part 1: Application of ISO/IEC 38500 to the governance of data*. <https://www.iso.org/standard/56639.html>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0*. https://doi.org/10.6028/NIST.CSWP.10
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
