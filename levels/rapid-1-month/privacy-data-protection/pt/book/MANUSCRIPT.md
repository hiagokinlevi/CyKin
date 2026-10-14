# Privacidade e Proteção de Dados: Curso Rápido

- Idioma: português do Brasil (`pt`); curso 004, curso rápido (1 mês). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–4 de 4 têm texto didático escrito à mão; os exercícios EX001–EX058 têm resoluções correspondentes com rubricas de 0 a 3; o laboratório offline usa apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e sua saída foi incorporada de uma execução real, idêntica à da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: iniciantes que precisam de um começo rápido e prático em privacidade e proteção de dados para um pequeno negócio.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: o laboratório compara os campos que o aplicativo de fidelidade sintético de uma farmácia coleta com os campos de que suas finalidades declaradas precisam. A análise jurídica é didática e não constitui aconselhamento jurídico; a LGPD e os atos da ANPD são citados pelo texto oficial e parafraseados. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os quatro capítulos acompanham uma atendente de farmácia ao longo de um curso de um mês: fundamentos e primeiras decisões, escopo e prática segura, sistemas, dados e fornecedores, e um laboratório guiado que vira um plano de ação curto. Execute o laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas. Cada capítulo agora separa a definição do teste que a aplica: se o item identifica uma pessoa, se é dado de saúde, se a cópia cabe no escopo assinado, se a base pertence àquela finalidade, e se o nome de um campo do laboratório esconde um valor que o script não lê. EX051–EX058 usam esses testes num fato novo da loja.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Sofia Mendes** | Estudante do curso rápido, atendente de farmácia | Inventada |
| **Sr. Raj Patel** | Mentor, encarregado de proteção de dados | Inventado |
| **Brightwater Community Learning Centre** | Centro de ensino fictício | Inventado |
| **Juniper Pharmacy** | Farmácia fictícia, 3 lojas, cerca de 9.000 clientes regulares, aplicativo de fidelidade | Inventada |

### Fontes principais

Regulamento (UE) 2016/679 (GDPR), artigos 4(1), 5, 9 e 28; Lei nº 13.709/2018 (LGPD), arts. 5º e 6º; Resolução CD/ANPD nº 15/2024; NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10); ISO/IEC 29100:2011. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Privacidade e proteção de dados: fundamentos e decisões

<!-- open-cyber-academy:lesson-figures:start ch-01 -->
### Mapa da aula

Aula 01 publicada. Mapa, exemplo, EX051.

```mermaid
flowchart TD
  N0["1.1 O curso e o caso"]
  N1["1.2 O que conta como dado pessoal"]
  N2["1.3 Categorias especiais"]
  N3["1.4 Os princípios"]
  N4["1.5 Uma primeira decisão"]
  N5["Conceitos — três testes diferentes"]
  N6["Dados — um papel, duas camadas"]
  N7["Fluxo de decisão — classificar antes de decidir o us"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> N6 --> N7
  N7 --> EX["Exemplo resolvido"]
  EX --> Q["Exercício EX051"]
```

### Desenho lógico

```mermaid
flowchart LR
  N0["1.1 O curso e o caso"]
  N1["1.2 O que conta como dado pessoal"]
  N2["1.3 Categorias especiais"]
  N3["1.4 Os princípios"]
  N4["1.5 Uma primeira decisão"]
  N5["Conceitos — três testes diferentes"]
  N6["Dados — um papel, duas camadas"]
  N7["Fluxo de decisão — classificar antes de decidir o us"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> N6 --> N7 --> Q["EX051"]
```

```text
[1.1 O curso e o caso]
    |
    v
[1.2 O que conta como dado pessoal]
    |
    v
[1.3 Categorias especiais]
    |
    v
[1.4 Os princípios]
    |
    v
[1.5 Uma primeira decisão]
    |
    v
[Conceitos — três testes diferentes]
    |
    v
[Dados — um papel, duas camadas]
    |
    v
[Fluxo de decisão — classificar antes de decidir o us]
    |
    v
[Exemplo resolvido] --> [Exercício EX051]
```
<!-- open-cyber-academy:lesson-figures:end ch-01 -->


### Objetivos de aprendizagem

Você vai (1) definir dado pessoal e dado de categoria especial; (2) nomear os princípios do GDPR e da LGPD; (3) tomar uma primeira decisão de privacidade fundamentada num pequeno negócio.

### 1.1 O curso e o caso

Sofia Mendes, atendente de farmácia, entra num curso rápido de um mês no fictício Brightwater Community Learning Centre. Seu mentor, o Sr. Raj Patel, atua como encarregado de proteção de dados de várias pequenas empresas. O local de trabalho de Sofia é a fictícia Juniper Pharmacy, um negócio familiar com três lojas, cerca de 9.000 clientes regulares, um serviço de receitas e um novo aplicativo de fidelidade. As farmácias lidam com informações sobre medicamentos, que podem revelar doenças, então até um pequeno negócio tem responsabilidades sérias de privacidade desde o primeiro atendimento. Sofia começa pela própria loja.

### 1.2 O que conta como dado pessoal

O Sr. Patel explica que dado pessoal é qualquer informação relativa a uma pessoa viva identificada ou identificável, pelo artigo 4(1) do GDPR; no Brasil, a LGPD usa uma definição semelhante no art. 5º, I. O nome e o telefone de um cliente são dados pessoais, mas o número de fidelidade também é, porque a Juniper consegue ligá-lo a uma pessoa. Sofia lista exemplos da loja: receitas, pontos de fidelidade, imagens do CFTV no balcão, endereços de entrega e anotações sobre o farmacêutico preferido de um cliente. O teste é a possibilidade de identificar, e não a presença de nomes.

### 1.3 Categorias especiais

Alguns dados recebem proteção extra. O artigo 9 do GDPR lista as categorias especiais, entre elas os dados relativos à saúde, e a LGPD as chama de dados pessoais sensíveis, no art. 5º, II. Uma receita de insulina revela diabetes; a compra de testes de gravidez pode sugerir uma gravidez. Sofia percebe que o histórico de compras do aplicativo de fidelidade pode, portanto, conter informações de saúde, embora tenha sido criado para pontos e vales, e não para cuidados. Tratar esses dados exige uma condição específica, e não só uma base legal comum. As farmácias lidam com eles todos os dias.

### 1.4 Os princípios

O Sr. Patel entrega a Sofia um resumo de uma página dos princípios do artigo 5 do GDPR: licitude, lealdade e transparência; limitação da finalidade; minimização; exatidão; limitação da conservação; integridade e confidencialidade; e responsabilização. A LGPD lista princípios comparáveis no art. 6º, entre eles a necessidade e a não discriminação. Para cada princípio, Sofia escreve uma frase sobre a Juniper, citando um sistema, como o aplicativo de fidelidade ou o CFTV. Para a minimização, escreve: o aplicativo de fidelidade deve coletar só o que os pontos e os vales exigem. Essas frases viram sua lista de verificação para as decisões seguintes.

### 1.5 Uma primeira decisão

O dono pergunta a Sofia se a equipe pode publicar nas redes sociais uma foto da loja cheia, com clientes visíveis no balcão. Sofia aplica sua lista. A finalidade é promocional, os clientes não esperavam aparecer na internet e um balcão de farmácia sugere necessidades de saúde. Ela recomenda tirar fotos só quando não houver clientes ou com permissão clara. O dono concorda. O Sr. Patel elogia o raciocínio: ela identificou a finalidade, considerou as expectativas e escolheu uma alternativa simples que ainda atende ao objetivo do negócio, sem expor ninguém que só foi comprar um remédio.

### Exemplo resolvido

Sofia define dado pessoal e dado de categoria especial com exemplos da farmácia, escreve uma frase por princípio para a Juniper e desaconselha publicar fotos do balcão com clientes.

> **Caso sintético.** O Brightwater, a Juniper e todas as pessoas são sintéticos; os artigos 4(1), 5 e 9 do GDPR e os arts. 5º e 6º da LGPD são reais.

### Erros e limites

As definições são amplas; na dúvida sobre se um dado é pessoal, trate-o como pessoal.

### Conceitos — três testes diferentes

O artigo 4(1) pergunta se a Juniper está diante de uma pessoa viva. O artigo 9 faz uma segunda pergunta, sobre saúde. A decisão da foto do balcão, neste capítulo, fez uma terceira: a pessoa esperaria esse uso? Passar num teste não faz passar nos outros.

| Teste | Pergunta da Sofia | Exemplo da Juniper | Resultado |
|---|---|---|---|
| Nomeado | Este item nomeia uma pessoa viva? | Um nome numa receita | Dado pessoal na hora |
| Ligável | Se não, a Juniper consegue ligá-lo a uma pessoa? | O número de fidelidade 44021 num papel sem nome | Continua sendo dado pessoal |
| Saúde | O conteúdo declara uma condição, ou a revela? | Uma linha grampeada, "insulina 10 ml" | Também dado de saúde, categoria especial |
| A loja, não uma pessoa | Dá para não apontar cliente nenhum? | O total de terça, sem cupom ligado | Não é dado pessoal |
| Expectativa | Mesmo sendo dado pessoal comum, a pessoa esperava esse uso? | Uma foto do balcão publicada para promoção | Recusar ainda, como na primeira decisão |

Se Sofia não consegue saber se o item é ligável, ela o trata como pessoal. Esse limite continua. Ele não serve para chamar o total do dia de registro de cliente.

### Dados — um papel, duas camadas

| O que ela tem na mão | Dado pessoal? | Dado de saúde? | Por que as respostas diferem |
|---|---|---|---|
| Só o número de fidelidade 44021 | Sim | Não | O sistema de dispensação liga 44021 a um cliente; pontos não declaram doença |
| O mesmo papel mais "insulina 10 ml" | Sim | Sim | A linha do medicamento revela uma condição; o número já identificava quem |
| Um fotograma do CFTV do balcão, sem legenda | Sim | Não por si | Um rosto identifica a pessoa; o fotograma não declara um diagnóstico |
| O total de terça | Não | Não | O número não é sobre uma pessoa viva |

### Fluxo de decisão — classificar antes de decidir o uso

```mermaid
flowchart TD
  A["Um item da loja"] --> B{"Ele nomeia uma pessoa viva, ou a Juniper consegue ligá-lo a uma?"}
  B -->|Não| C["Não é dado pessoal, salvo se Sofia estiver em dúvida"]
  C --> D["Na dúvida, tratar como pessoal e parar o palpite"]
  B -->|Sim| E["Dado pessoal. A lista do artigo 5 se aplica"]
  E --> F{"O conteúdo declara uma condição, ou a revela, como a insulina?"}
  F -->|Sim| G["Dado de saúde. A finalidade vai precisar de uma condição do artigo 9"]
  F -->|Não| H["Dado pessoal comum"]
  G --> I{"O uso proposto é um que a pessoa esperaria?"}
  H --> I
  I -->|Não| J["Recusar esse uso, mesmo com o item já classificado"]
  I -->|Sim| K["Registrar a classe e seguir para finalidade e minimização"]
```

### Exemplo resolvido — um papel sem nome, depois uma linha grampeada

Um cupom mostra o número de fidelidade 44021 e nenhum nome. Sofia o marca como dado pessoal porque o sistema de dispensação liga 44021 a um cliente. Ela não o marca como dado de saúde: o papel lista pontos, não um medicamento. O farmacêutico grampeia "insulina 10 ml". Só a resposta sobre saúde muda. O número já era pessoal; o medicamento torna o papel também dado de saúde. Ela ainda não publicaria uma foto desse cliente no balcão. Classificação e a decisão da promoção são testes separados, e a foto falha na expectativa mesmo quando não há diagnóstico escrito.

> **Caso sintético.** O número 44021 e a linha dos mililitros grampeada são inventados. Os artigos 4(1) e 9 são reais. Isto não é aconselhamento jurídico.

### Aplicar

- **EX051 — Número sem nome.** Por que o número de fidelidade 44021 é dado pessoal se o papel não tem nome, e por que ainda não é dado de saúde? *Rúbrica:* 3 = a Juniper consegue ligar o número a um cliente, então é pessoal; pontos não declaram nem revelam uma doença;; 2 = é pessoal por causa do vínculo;; 1 = vago;; 0 = nenhuma.
- **EX052 — Linha grampeada.** O que muda quando se acrescenta "insulina 10 ml", e o que não muda? *Rúbrica:* 3 = o papel passa a ser dado de saúde porque a linha revela uma condição; ele já era dado pessoal; a recusa da foto do balcão continua;; 2 = passa a ser dado de saúde;; 1 = vago;; 0 = nenhuma.

### Exercícios

- **EX001 — Número de fidelidade.** O número de fidelidade é dado pessoal? *Rubrica:* 3 = sim, pode ser ligado a uma pessoa;; 2 = sim;; 1 = não;; 0 = nenhuma.
- **EX002 — Insulina.** O que uma receita de insulina pode revelar? *Rubrica:* 3 = uma condição de saúde, como diabetes;; 2 = menciona saúde;; 1 = vago;; 0 = nenhuma.
- **EX003 — Termo da LGPD.** Como a LGPD chama os dados de categoria especial? *Rubrica:* 3 = dados pessoais sensíveis;; 2 = parcialmente correta;; 1 = outro;; 0 = nenhuma.
- **EX004 — Histórico de compras.** Por que o histórico de compras da fidelidade pode ser dado de saúde? *Rubrica:* 3 = as compras podem revelar doenças ou condições;; 2 = menciona saúde;; 1 = vago;; 0 = nenhuma.
- **EX005 — Contar os princípios.** Quantos princípios há no artigo 5 do GDPR? *Rubrica:* 3 = sete;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX006 — Necessidade.** Que princípio da LGPD se parece com a minimização? *Rubrica:* 3 = necessidade;; 2 = parcialmente correta;; 1 = outro;; 0 = nenhuma.
- **EX007 — Frase da minimização.** O que Sofia escreveu sobre a minimização? *Rubrica:* 3 = o aplicativo deve coletar só o que os pontos e os vales exigem;; 2 = menciona necessidade;; 1 = vago;; 0 = nenhuma.
- **EX008 — Foto do balcão.** O que Sofia recomendou para as fotos da loja? *Rubrica:* 3 = nenhum cliente visível ou permissão clara;; 2 = menciona permissão;; 1 = permitir;; 0 = nenhuma.
- **EX009 — Finalidade da foto.** Que finalidade a foto do balcão atendia? *Rubrica:* 3 = promoção;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX010 — Expectativa.** Os clientes esperavam aparecer na internet? *Rubrica:* 3 = não;; 2 = parcialmente correta;; 1 = sim;; 0 = nenhuma.
- **EX011 — Pessoas vivas.** A definição do GDPR cobre pessoas falecidas? *Rubrica:* 3 = não, pessoas vivas;; 2 = parcialmente correta;; 1 = sim;; 0 = nenhuma.
- **EX012 — Condição extra.** De que o tratamento de dados de saúde precisa além de uma base legal? *Rubrica:* 3 = uma condição específica do artigo 9;; 2 = menciona condição;; 1 = vago;; 0 = nenhuma.
- **EX013 — Uso da lista.** Como Sofia vai usar as frases dos princípios? *Rubrica:* 3 = como lista de verificação para as decisões seguintes;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 04)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Escopo, permissão e prática segura

<!-- open-cyber-academy:lesson-figures:start ch-02 -->
### Mapa da aula

Aula 02 publicada. Mapa, exemplo, EX053.

```mermaid
flowchart TD
  N0["2.1 Combinar o escopo"]
  N1["2.2 Tratamento seguro durante a revisão"]
  N2["2.3 Quando pedem para ir além"]
  N3["2.4 Comunicar problemas"]
  N4["2.5 Respeitar a equipe"]
  N5["Conceitos — a página assinada decide, e uma cópia co"]
  N6["Dados — cinco pedidos contra a página assinada"]
  N7["Fluxo de decisão — olhar, copiar ou guardar"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> N6 --> N7
  N7 --> EX["Exemplo resolvido"]
  EX --> Q["Exercício EX053"]
```

### Desenho lógico

```mermaid
flowchart LR
  N0["2.1 Combinar o escopo"]
  N1["2.2 Tratamento seguro durante a revisão"]
  N2["2.3 Quando pedem para ir além"]
  N3["2.4 Comunicar problemas"]
  N4["2.5 Respeitar a equipe"]
  N5["Conceitos — a página assinada decide, e uma cópia co"]
  N6["Dados — cinco pedidos contra a página assinada"]
  N7["Fluxo de decisão — olhar, copiar ou guardar"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> N6 --> N7 --> Q["EX053"]
```

```text
[2.1 Combinar o escopo]
    |
    v
[2.2 Tratamento seguro durante a revisão]
    |
    v
[2.3 Quando pedem para ir além]
    |
    v
[2.4 Comunicar problemas]
    |
    v
[2.5 Respeitar a equipe]
    |
    v
[Conceitos — a página assinada decide, e uma cópia co]
    |
    v
[Dados — cinco pedidos contra a página assinada]
    |
    v
[Fluxo de decisão — olhar, copiar ou guardar]
    |
    v
[Exemplo resolvido] --> [Exercício EX053]
```
<!-- open-cyber-academy:lesson-figures:end ch-02 -->


### Objetivos de aprendizagem

Você vai (1) trabalhar dentro da permissão combinada ao revisar a privacidade; (2) tratar os dados dos clientes com segurança durante a revisão; (3) comunicar problemas pelo canal certo.

### 2.1 Combinar o escopo

Antes de Sofia revisar qualquer coisa na Juniper, o Sr. Patel pede que ela combine um escopo por escrito com o dono. Ele lista o que ela pode examinar: as configurações do aplicativo de fidelidade, o aviso de privacidade, o arquivo de receitas em papel, o acesso da equipe ao sistema de dispensação e as placas de CFTV da loja. Ficam de fora a leitura de registros individuais de clientes, o contato com clientes e a mudança de configurações. O dono assina. O Sr. Patel explica que o escopo protege os clientes, o negócio e a própria Sofia, porque fixa limites antes que a curiosidade ou a pressão os empurrem.

### 2.2 Tratamento seguro durante a revisão

Sofia usa capturas de tela das configurações, e não das telas com clientes. Quando precisa de exemplos de registros, pede ao farmacêutico que crie no sistema de dispensação um cliente de teste com nome inventado. Ela guarda suas anotações numa gaveta trancada e numa pasta criptografada no computador da loja, e não no celular pessoal; ao fim, as anotações são destruídas. O Sr. Patel lembra que a própria revisão pode criar um risco de privacidade se anotações e capturas se espalharem, então ela precisa seguir o mesmo cuidado que recomenda aos outros.

### 2.3 Quando pedem para ir além

Uma colega pede a Sofia que veja se uma vizinha já retirou uma receita. Sofia recusa, explica que consultar uma pessoa sem motivo de trabalho é uso indevido do acesso e registra o pedido no diário da revisão. Mais tarde, o dono pede que ela olhe o celular do entregador para ver se endereços de clientes ficam guardados ali. Como isso está fora do escopo, ela pede ao dono que o acrescente por escrito primeiro, e ele concorda depois de conversar com o entregador. Assim, o novo item entra na revisão com a mesma clareza dos outros e com o conhecimento de quem é afetado.

### 2.4 Comunicar problemas

Durante a revisão, Sofia encontra uma caixa de cópias antigas de receitas num depósito destrancado. Ela não as move nem as lê. Comunica o achado ao dono e ao Sr. Patel no mesmo dia, com o local, a hora e o que viu. O dono tranca o depósito e providencia a trituração segura das cópias que passaram do prazo de retenção, e o Sr. Patel registra o evento. Ele explica que uma comunicação rápida e factual permite ao negócio julgar se houve violação e se é preciso notificar: pelo GDPR, em até 72 horas; no Brasil, pela Resolução CD/ANPD nº 15/2024, em três dias úteis.

### 2.5 Respeitar a equipe

A revisão de Sofia também envolve a equipe, como o acesso ao sistema de dispensação e as imagens do CFTV no balcão. Ela explica aos colegas o que está conferindo e por quê, e evita registrar opiniões sobre pessoas. Os funcionários também são titulares, com direitos pelo GDPR e pela LGPD. O Sr. Patel observa que as revisões funcionam melhor quando a equipe entende que o objetivo é melhorar os processos e proteger os clientes, e não flagrar ninguém, e que essa abertura incentiva as pessoas a mencionar os problemas que conhecem, muitas vezes os mais úteis da revisão.

### Exemplo resolvido

Sofia combina um escopo assinado, usa um cliente de teste e anotações criptografadas, recusa a consulta sobre a vizinha, faz o celular do entregador entrar no escopo por escrito, comunica as cópias de receitas destrancadas e explica a revisão à equipe.

> **Caso sintético.** O escopo e os eventos são sintéticos; a Resolução CD/ANPD nº 15/2024 é real.

### Erros e limites

A permissão verbal é fácil de contestar; registre as mudanças de escopo por escrito.

### Conceitos — a página assinada decide, e uma cópia conta como consulta

O escopo é uma lista, não um humor. Fotografar uma tela viva de dispensação copia o registro que está nela. A cópia é a mesma exclusão que ler aquele cliente.

| Pergunta | Permitido nesta semana | Não permitido |
|---|---|---|
| O que ela pode abrir? | Configurações da fidelidade, o aviso de privacidade, o modo de arquivar receitas em papel, a lista de acessos da equipe, as placas de CFTV | O registro de um cliente nomeado |
| O que ela pode guardar? | Capturas das configurações; anotações na gaveta trancada e na pasta criptografada do computador da loja | Uma tela de cliente no celular pessoal |
| O pedido cresce | O dono acrescenta o item por escrito antes de ela olhar | Um "só desta vez" falado |
| Ela acha registros expostos | Comunicar o local, a hora e o que viu, no mesmo dia | Mover as cópias, ou lê-las |

### Dados — cinco pedidos contra a página assinada

| Pedido | Está na página que o dono assinou? | O que Sofia faz |
|---|---|---|
| Capturar as configurações da fidelidade | Sim | Só configurações, não um cliente |
| Ver como as receitas em papel são arquivadas | Sim, o método | Ela não abre o arquivo de uma pessoa nomeada |
| A vizinha já retirou a receita? | Não | Recusar, e escrever o pedido no diário da revisão |
| Olhar o celular do entregador | Não, até o dono acrescentar por escrito | Esperar |
| Uma caixa de cópias antigas de receitas, destrancada | O achado é uma comunicação, não permissão para manuseá-las | Não mover nem ler; avisar o dono e o Sr. Patel |

### Fluxo de decisão — olhar, copiar ou guardar

```mermaid
flowchart TD
  A["Alguém pede a Sofia que olhe, copie ou guarde algo"] --> B{"Essa ação está na página que o dono assinou?"}
  B -->|Não| C["Parar. O acréscimo por escrito vem antes de qualquer olhada"]
  B -->|Sim| D{"Isso mostraria ou copiaria o registro de um cliente real?"}
  D -->|Sim| E["Recusar. Usar o cliente de teste inventado"]
  D -->|Não| F{"As anotações sairiam da gaveta trancada e da pasta criptografada da loja?"}
  F -->|Sim| G["Recusar essa cópia. O celular pessoal fica fora da revisão"]
  F -->|Não| H["Seguir. Registros expostos são comunicados pelo local, pela hora e pelo que ela viu"]
```

### Exemplo resolvido — uma foto da tela viva

Uma colega pede a Sofia que fotografe uma tela viva de dispensação "para a revisão mostrar o leiaute". A tela nomeia um cliente real e um medicamento. O acesso da equipe está na página assinada; um registro individual, não. A fotografia ainda poria esse registro num celular. Sofia recusa. O farmacêutico cria o cliente de teste inventado, e Sofia faz a captura dessa tela para a pasta criptografada do computador da loja. O pedido da colega entra no diário da revisão no mesmo dia.

> **Caso sintético.** A fotografia do leiaute e a tela viva são inventadas.

### Aplicar

- **EX053 — Tela viva.** Por que a fotografia é recusada, e o que a substitui? *Rúbrica:* 3 = uma tela viva é o registro de um cliente real, o que o escopo exclui, e o celular o copiaria; usar o cliente de teste inventado e a pasta criptografada da loja;; 2 = o escopo exclui registros reais;; 1 = vago;; 0 = nenhuma.
- **EX054 — A caixa.** Que três fatos a comunicação do mesmo dia contém, e que duas ações Sofia não faz? *Rúbrica:* 3 = local, hora e o que viu; ela não move as cópias e não as lê;; 2 = ela comunica e não as lê;; 1 = vago;; 0 = nenhuma.

### Exercícios

- **EX014 — Exclusões do escopo.** Cite duas coisas excluídas do escopo de Sofia. *Rubrica:* 3 = ler registros de clientes, contatar clientes, mudar configurações;; 2 = duas;; 1 = uma;; 0 = nenhuma.
- **EX015 — Cliente de teste.** Por que Sofia usou um cliente de teste? *Rubrica:* 3 = para não ver registros reais de clientes;; 2 = menciona dados reais;; 1 = vago;; 0 = nenhuma.
- **EX016 — Guarda das anotações.** Onde Sofia guarda suas anotações? *Rubrica:* 3 = gaveta trancada e pasta criptografada;; 2 = as duas;; 1 = celular;; 0 = nenhuma.
- **EX017 — Consulta sobre a vizinha.** Por que Sofia recusou a consulta sobre a vizinha? *Rubrica:* 3 = sem motivo de trabalho; uso indevido do acesso;; 2 = menciona uso indevido;; 1 = vago;; 0 = nenhuma.
- **EX018 — Celular do entregador.** Como o celular do entregador entrou na revisão? *Rubrica:* 3 = o dono o acrescentou por escrito depois de falar com o entregador;; 2 = menciona por escrito;; 1 = vago;; 0 = nenhuma.
- **EX019 — Achado no depósito.** O que Sofia encontrou no depósito? *Rubrica:* 3 = cópias antigas de receitas sem tranca;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX020 — Não mexer.** Por que Sofia não moveu nem leu as cópias? *Rubrica:* 3 = para evitar mais exposição e ficar dentro do escopo;; 2 = menciona escopo;; 1 = vago;; 0 = nenhuma.
- **EX021 — Conteúdo da comunicação.** O que a comunicação dela incluía? *Rubrica:* 3 = local, hora e o que viu;; 2 = a maioria;; 1 = um;; 0 = nenhuma.
- **EX022 — Resposta do dono.** O que o dono fez com o depósito? *Rubrica:* 3 = trancou-o e providenciou a trituração das cópias vencidas;; 2 = os dois;; 1 = um;; 0 = nenhuma.
- **EX023 — Comunicação rápida.** Por que a comunicação rápida importa? *Rubrica:* 3 = para julgar se houve violação e se é preciso notificar;; 2 = menciona notificação;; 1 = vago;; 0 = nenhuma.
- **EX024 — Equipe como titular.** Os funcionários também são titulares? *Rubrica:* 3 = sim;; 2 = parcialmente correta;; 1 = não;; 0 = nenhuma.
- **EX025 — Risco da revisão.** Como a própria revisão pode criar risco? *Rubrica:* 3 = anotações e capturas de tela podem se espalhar;; 2 = menciona anotações;; 1 = vago;; 0 = nenhuma.
- **EX026 — Abertura.** O que incentiva a equipe a mencionar problemas? *Rubrica:* 3 = entender que o objetivo é melhorar, não culpar;; 2 = menciona objetivo;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 04)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Privacidade e proteção de dados: sistemas, dados e dependências

<!-- open-cyber-academy:lesson-figures:start ch-03 -->
### Mapa da aula

Aula 03 publicada. Mapa, exemplo, EX055.

```mermaid
flowchart TD
  N0["3.1 Mapear os sistemas"]
  N1["3.2 Seguir os fluxos"]
  N2["3.3 Fornecedores e dependências"]
  N3["3.4 Bases legais"]
  N4["3.5 Retenção"]
  N5["Conceitos — a base não viaja para a finalidade segui"]
  N6["Dados — quatro fluxos que saem da loja"]
  N7["Fluxo de decisão — o dono propõe um uso novo"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> N6 --> N7
  N7 --> EX["Exemplo resolvido"]
  EX --> Q["Exercício EX055"]
```

### Desenho lógico

```mermaid
flowchart LR
  N0["3.1 Mapear os sistemas"]
  N1["3.2 Seguir os fluxos"]
  N2["3.3 Fornecedores e dependências"]
  N3["3.4 Bases legais"]
  N4["3.5 Retenção"]
  N5["Conceitos — a base não viaja para a finalidade segui"]
  N6["Dados — quatro fluxos que saem da loja"]
  N7["Fluxo de decisão — o dono propõe um uso novo"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> N6 --> N7 --> Q["EX055"]
```

```text
[3.1 Mapear os sistemas]
    |
    v
[3.2 Seguir os fluxos]
    |
    v
[3.3 Fornecedores e dependências]
    |
    v
[3.4 Bases legais]
    |
    v
[3.5 Retenção]
    |
    v
[Conceitos — a base não viaja para a finalidade segui]
    |
    v
[Dados — quatro fluxos que saem da loja]
    |
    v
[Fluxo de decisão — o dono propõe um uso novo]
    |
    v
[Exemplo resolvido] --> [Exercício EX055]
```
<!-- open-cyber-academy:lesson-figures:end ch-03 -->


### Objetivos de aprendizagem

Você vai (1) mapear os sistemas e os fluxos de dados da Juniper; (2) identificar fornecedores e dependências; (3) anotar as bases legais e a retenção.

### 3.1 Mapear os sistemas

Numa tarde, Sofia desenha os sistemas da Juniper numa página: o sistema de dispensação, que guarda receitas e históricos de medicação; o caixa, que registra as vendas; o aplicativo de fidelidade, operado por um fornecedor; a ferramenta de newsletter por e-mail; o gravador de CFTV; o serviço de entregas; e os arquivos de receitas em papel. Em cada caixa, ela escreve os principais dados que o sistema guarda. O desenho mostra que o aplicativo de fidelidade recebe toda noite os dados de compras do caixa, um fluxo que o dono não sabia que incluía as compras de medicamentos.

### 3.2 Seguir os fluxos

Sofia rastreia para onde os dados vão depois. As receitas chegam eletronicamente dos consultórios médicos e também em papel. O sistema de dispensação envia as cobranças ao serviço de saúde para pagamento. O serviço de entregas recebe nomes, endereços e a descrição de um pacote lacrado. A ferramenta de newsletter recebe os e-mails dos clientes que entraram na lista. O fornecedor da fidelidade recebe cada item do caixa, incluindo analgésicos e testes de gravidez. Ela marca cada fluxo com uma seta, seu conteúdo e se os clientes o esperariam. Dois fluxos surpreendem o dono.

### 3.3 Fornecedores e dependências

A Juniper depende de quatro fornecedores: o do sistema de dispensação, a empresa do aplicativo de fidelidade, a ferramenta de newsletter e a empresa de entregas. Cada um trata dados de clientes para a Juniper e precisa de um contrato que atenda ao artigo 28 do GDPR, com instruções, confidencialidade, segurança e exclusão; na LGPD, o operador age segundo as instruções do controlador, pelo art. 39. Sofia encontra contratos com o fornecedor da dispensação e com a ferramenta de newsletter, mas os da fidelidade e das entregas são termos padrão que não falam de proteção de dados. O Sr. Patel redige as cláusulas que faltam.

### 3.4 Bases legais

Com o Sr. Patel, Sofia anota a base legal de cada finalidade numa tabela. A dispensação se apoia na prestação de cuidados de saúde, com o artigo 9(2)(h) do GDPR como condição para os dados de saúde; na LGPD, a tutela da saúde do art. 11, II, "f". Guardar os registros de receitas se apoia em obrigações legais das farmácias. A newsletter se apoia no consentimento. O programa de fidelidade se apoia no contrato com os membros, mas usar as compras de medicamentos para ofertas personalizadas exigiria consentimento explícito, porque envolve dados de saúde. Cada finalidade precisa da sua base, escolhida antes de o tratamento começar.

### 3.5 Retenção

Sofia pergunta por quanto tempo cada tipo de dado é guardado. Os registros de receitas seguem regras profissionais definidas para as farmácias. O CFTV é sobrescrito depois de trinta dias. Os dados de fidelidade não têm limite, e os registros de entrega ficam no celular do entregador indefinidamente. Ela recomenda que o dono defina prazos de retenção para os dados de fidelidade, os registros de entrega e os assinantes da newsletter que nunca abrem os e-mails, e os registre numa tabela simples. O dono aprova. A limitação da conservação, ela observa, reduz tanto o risco jurídico quanto o dano de uma eventual violação.

### Exemplo resolvido

Sofia mapeia sete sistemas, rastreia os fluxos, incluindo as compras de medicamentos enviadas ao fornecedor da fidelidade, encontra dois contratos com fornecedores sem cláusulas de proteção de dados, anota as bases legais e recomenda prazos de retenção.

> **Caso sintético.** Os sistemas são sintéticos; os artigos 9(2)(h) e 28 do GDPR e os arts. 11 e 39 da LGPD são reais.

### Erros e limites

Um mapa desenhado uma vez fica desatualizado; atualize-o quando os sistemas mudarem.

### Conceitos — a base não viaja para a finalidade seguinte

Sofia já anota uma base para cada finalidade, antes de o tratamento começar. Uma base escolhida para pontos não cobre uma finalidade nova. Dado de saúde mantém essa regra e acrescenta uma condição do artigo 9 para a finalidade que de fato usa o dado de saúde. Na LGPD, a tutela da saúde do art. 11, II, "f", continua sendo a condição que a edição já registrou para a dispensação, e o operador segue as instruções do controlador, pelo art. 39.

| Finalidade já na tabela dela | Base que ela registrou | Condição de saúde também? | O que não bastaria |
|---|---|---|---|
| Dispensar uma receita | Prestação de cuidados de saúde | Sim, artigo 9(2)(h); na LGPD, art. 11, II, "f" | O consentimento colhido para a newsletter |
| Guardar o registro da receita | Uma obrigação legal das farmácias | O registro é dado de saúde; a obrigação é o motivo de guardá-lo | Um prazo mais curto que Sofia invente |
| Newsletter | Consentimento | Não, enquanto a mensagem não for sobre uma condição | A adesão à fidelidade |
| Pontos para os membros | Contrato com esses membros | Não, enquanto o registro for pontos e gasto que não é medicamento | Usar esse contrato para uma oferta com o nome do medicamento |
| Uma mensagem ligada a um medicamento nomeado | Não está na tabela | A mensagem usaria dado de saúde | O contrato da fidelidade, ou o consentimento comum da newsletter |

### Dados — quatro fluxos que saem da loja

| Fluxo | Quem recebe | O contrato tem os termos do artigo 28? | Retenção que ela encontrou |
|---|---|---|---|
| Receitas e cobranças | Fornecedor da dispensação | Sim | Regras profissionais das farmácias; ela não as reescreve |
| Endereços da lista | Ferramenta de newsletter | Sim | Ainda sem prazo para quem nunca abre a mensagem |
| Cada item do caixa, inclusive medicamentos | Fornecedor da fidelidade, toda noite | Não | Os dados de fidelidade não têm data de fim |
| Nome, endereço, descrição do pacote lacrado | Empresa de entregas | Não | Ficam no celular do entregador sem data de fim |

### Fluxo de decisão — o dono propõe um uso novo

```mermaid
flowchart TD
  A["Um uso novo de dados que a Juniper já tem"] --> B{"Essa finalidade já está na tabela de bases da Sofia?"}
  B -->|Não| C["Não começar. Registrar uma base para esta finalidade primeiro"]
  B -->|Sim| D{"Este uso contém o nome de um medicamento ou outro dado de saúde?"}
  D -->|Sim| E{"Já há uma condição do artigo 9 registrada para esta mesma finalidade?"}
  E -->|Não| F["Parar. O contrato da fidelidade não é essa condição"]
  E -->|Sim| G["Seguir para quem recebe"]
  D -->|Não| G
  G --> H{"Um fornecedor receberia isso sob um contrato sem os termos do artigo 28?"}
  H -->|Sim| I["Marcar o contrato. Não acrescentar um fluxo novo nesses termos"]
  H -->|Não| J{"Há um prazo de retenção escrito para este dado?"}
  J -->|Não| K["Definir um prazo antes de guardar mais. Não inventar a regra da farmácia"]
  J -->|Sim| L["Escrever o uso na tabela"]
```

### Exemplo resolvido — uma mensagem quando se vende insulina

O dono quer que o aplicativo de fidelidade envie uma mensagem com um vale sempre que um membro comprar insulina. Sofia não liga isso. O contrato dos membros cobre pontos. Não cobre uma mensagem disparada por um medicamento nomeado, e essa mensagem é uma finalidade nova que usa dado de saúde. A loja não colheu o consentimento explícito de que essa finalidade precisa. O contrato da fidelidade também ainda não tem os termos do artigo 28, e o operador continuaria sem instrução clara do controlador. Um vale só pelo total de pontos, sem nomear medicamento, seria outra proposta e percorreria este fluxo desde o início. Esta proposta nomeia a insulina, então fica desligada.

> **Caso sintético.** A mensagem do vale de insulina é inventada. Os artigos 9 e 28 são reais, como os arts. 11 e 39 da LGPD já citados neste capítulo. Isto não é aconselhamento jurídico.

### Aplicar

- **EX055 — Mensagem da insulina.** Que base registrada falha, e o que precisa existir antes de qualquer mensagem dessas? *Rúbrica:* 3 = o contrato da fidelidade não cobre uma oferta com o nome do medicamento; a loja precisa de consentimento explícito para essa finalidade, e o contrato da fidelidade ainda não tem os termos do artigo 28;; 2 = consentimento explícito;; 1 = vago;; 0 = nenhuma.
- **EX056 — Sem data de fim.** Que princípio falha nos registros de entrega no celular do entregador, e o que Sofia não inventa? *Rúbrica:* 3 = a limitação da conservação, porque não há data de fim; o dono define um prazo de entrega; ela não inventa o prazo profissional das receitas;; 2 = definir um prazo de entrega;; 1 = vago;; 0 = nenhuma.

### Exercícios

- **EX027 — Fluxo oculto.** Que fluxo o dono não conhecia? *Rubrica:* 3 = o caixa envia as compras de medicamentos ao aplicativo de fidelidade;; 2 = menciona fidelidade;; 1 = vago;; 0 = nenhuma.
- **EX028 — Dados da entrega.** O que o serviço de entregas recebe? *Rubrica:* 3 = nomes, endereços e descrição do pacote;; 2 = a maioria;; 1 = um;; 0 = nenhuma.
- **EX029 — Número de fornecedores.** De quantos fornecedores a Juniper depende? *Rubrica:* 3 = quatro;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX030 — Lacunas contratuais.** Que contratos não tinham cláusulas de proteção de dados? *Rubrica:* 3 = fidelidade e entregas;; 2 = os dois;; 1 = um;; 0 = nenhuma.
- **EX031 — Artigo 28.** O que os contratos com operadores precisam cobrir? *Rubrica:* 3 = instruções, confidencialidade, segurança, exclusão;; 2 = a maioria;; 1 = um;; 0 = nenhuma.
- **EX032 — Condição da dispensação.** Que condição cobre os dados de saúde da dispensação? *Rubrica:* 3 = artigo 9(2)(h);; 2 = parcialmente correta;; 1 = consentimento;; 0 = nenhuma.
- **EX033 — Ofertas personalizadas.** De que precisariam as ofertas personalizadas baseadas em compras de medicamentos? *Rubrica:* 3 = consentimento explícito;; 2 = parcialmente correta;; 1 = contrato;; 0 = nenhuma.
- **EX034 — Retenção do CFTV.** Por quanto tempo o CFTV é guardado? *Rubrica:* 3 = trinta dias;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX035 — Dados sem limite.** Que dados não tinham limite de retenção? *Rubrica:* 3 = dados de fidelidade e registros de entrega;; 2 = os dois;; 1 = um;; 0 = nenhuma.
- **EX036 — Benefício da retenção.** Por que a limitação da conservação reduz o dano de uma violação? *Rubrica:* 3 = menos dados guardados, menos dados expostos;; 2 = menciona menos dados;; 1 = vago;; 0 = nenhuma.
- **EX037 — Momento da base.** Quando a base legal deve ser escolhida? *Rubrica:* 3 = antes de o tratamento começar;; 2 = parcialmente correta;; 1 = depois;; 0 = nenhuma.
- **EX038 — Marcação da expectativa.** O que Sofia marcou em cada fluxo além do conteúdo? *Rubrica:* 3 = se os clientes o esperariam;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 04)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Privacidade e proteção de dados: laboratório guiado e síntese aplicada

<!-- open-cyber-academy:lesson-figures:start ch-04 -->
### Mapa da aula

Aula 04 publicada. Mapa, exemplo, EX057.

```mermaid
flowchart TD
  N0["4.1 O laboratório guiado"]
  N1["4.2 Interpretar o laboratório"]
  N2["4.3 Um plano curto"]
  N3["4.4 Apresentar ao dono"]
  N4["4.5 Conferir e próximos passos"]
  N5["Laboratório — Campos do aplicativo de fidelidade ver"]
  N6["Conceitos — o script testa nomes, não valores"]
  N7["Dados — pertinência aos três conjuntos"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> N6 --> N7
  N7 --> EX["Exemplo resolvido"]
  EX --> Q["Exercício EX057"]
```

### Desenho lógico

```mermaid
flowchart LR
  N0["4.1 O laboratório guiado"]
  N1["4.2 Interpretar o laboratório"]
  N2["4.3 Um plano curto"]
  N3["4.4 Apresentar ao dono"]
  N4["4.5 Conferir e próximos passos"]
  N5["Laboratório — Campos do aplicativo de fidelidade ver"]
  N6["Conceitos — o script testa nomes, não valores"]
  N7["Dados — pertinência aos três conjuntos"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> N6 --> N7 --> Q["EX057"]
```

```text
[4.1 O laboratório guiado]
    |
    v
[4.2 Interpretar o laboratório]
    |
    v
[4.3 Um plano curto]
    |
    v
[4.4 Apresentar ao dono]
    |
    v
[4.5 Conferir e próximos passos]
    |
    v
[Laboratório — Campos do aplicativo de fidelidade ver]
    |
    v
[Conceitos — o script testa nomes, não valores]
    |
    v
[Dados — pertinência aos três conjuntos]
    |
    v
[Exemplo resolvido] --> [Exercício EX057]
```
<!-- open-cyber-academy:lesson-figures:end ch-04 -->


### Objetivos de aprendizagem

Você vai (1) conduzir um laboratório guiado de minimização; (2) reunir os achados num plano curto; (3) apresentar recomendações ao dono de um negócio.

### 4.1 O laboratório guiado

O Sr. Patel guia Sofia num laboratório que usa o formulário de cadastro sintético do aplicativo de fidelidade e as finalidades que a Juniper declara no aviso: ganhar e gastar pontos, um vale de aniversário e e-mails de marketing para quem aceitar. O laboratório compara cada campo coletado com os campos de que cada finalidade precisa. Ele mostra que o aplicativo coleta dez campos e que cinco deles, 50%, não são necessários para nenhuma finalidade declarada: telefone, CEP, itens de receita, gênero e um rastro de localização registrado pelo aplicativo em segundo plano.

### 4.2 Interpretar o laboratório

Sofia examina cada campo desnecessário. Os itens de receita são dados de saúde sem nenhuma finalidade declarada no programa. O rastro de localização acompanha os deslocamentos dos clientes, o que é invasivo e inesperado. Gênero, CEP e telefone podem ter vindo do modelo padrão do fornecedor. Nenhum dos cinco campos serve a uma finalidade declarada. O Sr. Patel lembra que coletar dados sem finalidade declarada viola os princípios da minimização e da limitação da finalidade, e que dados de saúde num programa de fidelidade também carecem da condição do artigo 9 de que precisariam.

### 4.3 Um plano curto

Sofia reúne os achados do mês num plano de uma página com cinco ações: retirar os cinco campos desnecessários e parar de enviar os itens de medicamentos do caixa ao fornecedor da fidelidade; assinar contratos de proteção de dados com as empresas de fidelidade e de entregas; definir prazos de retenção para os dados de fidelidade, entregas e newsletter; trocar as fotos do balcão por imagens sem clientes; e manter o depósito trancado, com uma rotina de trituração. Cada ação tem um responsável, uma estimativa de custo e uma data-alvo dentro de três meses, e o plano inteiro cabe numa página.

### 4.4 Apresentar ao dono

Sofia apresenta o plano ao dono da Juniper em quinze minutos. Começa pelo problema mais grave, as compras de medicamentos chegando ao fornecedor da fidelidade, e o explica em palavras simples: as compras de saúde dos clientes estão sendo compartilhadas com uma empresa de aplicativo sem motivo e sem o conhecimento deles. O dono pergunta se retirar os campos vai reduzir o valor do aplicativo. Sofia responde com calma e mostra que os pontos e os vales funcionam com os campos que restam. O dono aprova as cinco ações e pede ao fornecedor que faça as mudanças.

### 4.5 Conferir e próximos passos

Duas semanas depois, Sofia e o Sr. Patel conferem o aplicativo com um novo cadastro sintético. O formulário agora pede cinco campos, e a exportação do caixa não contém itens de medicamentos, apenas o gasto total e as categorias que não são medicamentos. Os contratos estão em negociação. O Sr. Patel explica que conferir depois de uma mudança confirma que o plano funcionou, em vez de supor que funcionou. Sofia planeja o próximo passo, um curso de governança, riscos e compliance, para aprender como as empresas mantêm essas melhorias ao longo do tempo. O curso termina.

### Laboratório — Campos do aplicativo de fidelidade versus finalidades declaradas

```python
"""Compare fields collected by a synthetic pharmacy loyalty app with fields its purposes need (stdlib only)."""
collected = ["name", "email", "phone", "date_of_birth", "postcode", "purchase_history",
             "prescription_items", "gender", "location_trail", "marketing_choice"]
needs = {
    "earn and spend points": {"name", "email", "purchase_history"},
    "birthday voucher": {"email", "date_of_birth"},
    "marketing emails": {"email", "marketing_choice"},
}
used = set().union(*needs.values())
unneeded = [f for f in collected if f not in used]
for f in collected:
    print(f"{f:20s} {'needed' if f in used else 'NOT NEEDED'}")
print(f"fields collected {len(collected)}; not needed for any stated purpose {len(unneeded)} ({100*len(unneeded)/len(collected):.0f}%)")
```

Execute com `python3 lab_loyalty.py`. Saída verificada:

```text
name                 needed
email                needed
phone                NOT NEEDED
date_of_birth        needed
postcode             NOT NEEDED
purchase_history     needed
prescription_items   NOT NEEDED
gender               NOT NEEDED
location_trail       NOT NEEDED
marketing_choice     needed
fields collected 10; not needed for any stated purpose 5 (50%)
```

### Exemplo resolvido

Sofia descobre que cinco de dez campos da fidelidade (50%) são desnecessários, incluindo itens de receita e um rastro de localização, reúne os achados do mês num plano de cinco ações, obtém a aprovação do dono e confirma as mudanças no aplicativo.

> **Caso sintético.** O aplicativo é sintético; os artigos 5 e 9 do GDPR são reais.

### Erros e limites

As finalidades listadas num aviso podem estar incompletas; pergunte ao negócio se existe outra finalidade antes de excluir campos.

### Conceitos — o script testa nomes, não valores

`lab_loyalty.py` monta `used` como a união dos três conjuntos de finalidade e pergunta se cada nome coletado está nessa união. Um campo imprime `needed` quando o nome é membro. O script não abre o campo para ler o que foi guardado dentro dele.

| Passo | O que o script usa | O que ele não vê |
|---|---|---|
| Montar `used` | A união de pontos, vale de aniversário e e-mails de marketing | Se essa finalidade é lícita |
| Marcar cada nome coletado | Se o nome pertence a `used` | Os valores guardados sob o nome |
| Contar | Nomes em `collected` que estão fora de `used` | Um medicamento escondido dentro de `purchase_history` |

`purchase_history` está no conjunto dos pontos, então o script imprime `needed`. `prescription_items` não está em conjunto nenhum, então imprime `NOT NEEDED`. A conferência posterior do caixa é um segundo teste: o gasto total e as categorias que não são medicamentos podem ficar; o nome de um medicamento, não. Passar na lista de campos não faz passar na conferência do conteúdo.

### Dados — pertinência aos três conjuntos

| Nome coletado | Conjunto de finalidade que o contém | Marca do script | Regra de conteúdo da conferência de duas semanas |
|---|---|---|---|
| `name`, `email` | Pontos | `needed` | Ficam |
| `date_of_birth` | Vale de aniversário | `needed` | Fica |
| `marketing_choice` | E-mails de marketing | `needed` | Fica |
| `purchase_history` | Pontos | `needed` | Não pode carregar o nome de um medicamento |
| `phone`, `postcode`, `gender`, `location_trail`, `prescription_items` | Nenhum | `NOT NEEDED` | Sair |

A contagem continua a verificada: 10 nomes coletados, 5 fora da união.

### Fluxo de decisão — alguém diz que o formulário foi corrigido

```mermaid
flowchart TD
  A["Alguém afirma que a mudança da fidelidade está pronta"] --> B["Rodar lab_loyalty.py no formulário novo"]
  B --> C{"phone, postcode, prescription_items, gender e location_trail saíram?"}
  C -->|Não| D["A conferência dos campos falhou"]
  C -->|Sim| E{"A exportação do caixa ainda nomeia um medicamento?"}
  E -->|Sim| F["A lista de campos passou e a conferência do conteúdo falhou"]
  E -->|Não| G["As duas passaram: cinco campos, totais e categorias que não são medicamentos"]
  D --> H["Escrever qual conferência falhou, e a data. Deixar a ação aberta"]
  F --> H
  G --> I["Registrar os dois resultados. A ação pode fechar"]
```

### Exemplo resolvido — cinco nomes limpos, uma linha de insulina

O formulário novo pede nome, e-mail, data de nascimento, histórico de compras e a escolha de marketing. Sofia roda o script. Os cinco nomes estão na união, e nenhum dos cinco nomes rejeitados permanece. Ela abre então a exportação de uma noite do caixa e encontra uma linha que diz insulina. A conferência dos campos passou. A conferência do conteúdo falhou, porque `purchase_history` é permitido como nome e o script nunca lê o interior. Ela deixa a ação aberta e diz ao dono que a exportação ainda carrega um medicamento. Pontos e o vale de aniversário não precisam desse nome.

> **Caso sintético.** O frasco 44021 no arquivo de terça à noite é inventado. A regra de pertinência é a de lab_loyalty.py. Isto não é aconselhamento jurídico.

### Aplicar

- **EX057 — Dentro do campo.** Por que `purchase_history` pode imprimir `needed` enquanto uma linha de insulina guardada nele ainda é uma falha? *Rúbrica:* 3 = o script testa o nome do campo contra a união, não os valores dentro do campo; o nome de um medicamento tem de ficar fora da exportação;; 2 = o script não lê o interior do campo;; 1 = vago;; 0 = nenhuma.
- **EX058 — Duas conferências.** O formulário tem os cinco campos permitidos e a exportação ainda lista insulina. Qual conferência passou, qual falhou, e Sofia fecha a ação? *Rúbrica:* 3 = a conferência dos campos passou; a do conteúdo falhou; ela não fecha a ação;; 2 = ela não fecha;; 1 = ela fecha;; 0 = nenhuma.

### Exercícios

- **EX039 — Parcela desnecessária.** Que parcela dos campos da fidelidade era desnecessária? *Rubrica:* 3 = 5 de 10, 50%;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX040 — Rastro de localização.** Por que o rastro de localização preocupa? *Rubrica:* 3 = rastreamento invasivo e inesperado;; 2 = menciona rastreamento;; 1 = vago;; 0 = nenhuma.
- **EX041 — Padrões do fornecedor.** De onde podem ter vindo gênero, CEP e telefone? *Rubrica:* 3 = do modelo padrão de cadastro do fornecedor;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX042 — Princípios violados.** Que dois princípios a coleta desnecessária viola? *Rubrica:* 3 = minimização e limitação da finalidade;; 2 = os dois;; 1 = um;; 0 = nenhuma.
- **EX043 — Ações do plano.** Quantas ações o plano de Sofia contém? *Rubrica:* 3 = cinco;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX044 — Detalhes do plano.** O que cada ação tem? *Rubrica:* 3 = responsável, estimativa de custo, data-alvo;; 2 = a maioria;; 1 = um;; 0 = nenhuma.
- **EX045 — Problema principal.** Que problema Sofia apresentou primeiro? *Rubrica:* 3 = as compras de medicamentos chegando ao fornecedor da fidelidade;; 2 = parcialmente correta;; 1 = outro;; 0 = nenhuma.
- **EX046 — Preocupação do dono.** Com o que o dono se preocupou? *Rubrica:* 3 = retirar campos reduzir o valor do aplicativo;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX047 — Campos restantes.** Quantos campos o formulário pede depois da mudança? *Rubrica:* 3 = cinco;; 2 = parcialmente correta;; 1 = dez;; 0 = nenhuma.
- **EX048 — Exportação do caixa.** O que a exportação do caixa contém agora? *Rubrica:* 3 = gasto total e categorias que não são medicamentos;; 2 = parcialmente correta;; 1 = medicamentos;; 0 = nenhuma.
- **EX049 — Conferência posterior.** Por que conferir depois de uma mudança? *Rubrica:* 3 = para confirmar que o plano funcionou;; 2 = menciona confirmação;; 1 = vago;; 0 = nenhuma.
- **EX050 — Próximo estudo.** O que Sofia planeja estudar a seguir? *Rubrica:* 3 = governança, riscos e compliance;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 04)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX058. Sofia Mendes, o Sr. Raj Patel, o Brightwater Community Learning Centre, a Juniper Pharmacy e todos os números são sintéticos. As respostas do laboratório citam a saída verificada. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Sim, porque a Juniper consegue ligá-lo a um cliente identificável.

**EX002.** Que o cliente provavelmente tem diabetes, uma condição de saúde.

**EX003.** Dados pessoais sensíveis.

**EX004.** Compras como testes ou medicamentos podem revelar condições de saúde.

**EX005.** Sete.

**EX006.** Necessidade.

**EX007.** O aplicativo de fidelidade deve coletar só o que os pontos e os vales exigem.

**EX008.** Tirar fotos sem clientes presentes ou com permissão clara.

**EX009.** Promoção nas redes sociais.

**EX010.** Não, eles não esperavam isso.

**EX011.** Não, cobre pessoas vivas.

**EX012.** Uma condição específica do artigo 9.

**EX013.** Como lista de verificação para todas as decisões seguintes.

**EX014.** Ler registros individuais de clientes e mudar configurações.

**EX015.** Para ver como os registros funcionam sem ver clientes reais.

**EX016.** Numa gaveta trancada e numa pasta criptografada no computador da loja.

**EX017.** Consultar alguém sem motivo de trabalho é uso indevido do acesso.

**EX018.** O dono o acrescentou ao escopo por escrito depois de falar com o entregador.

**EX019.** Cópias antigas de receitas num depósito destrancado.

**EX020.** Mexer nelas estava fora do escopo e poderia causar mais exposição.

**EX021.** O local, a hora e o que ela viu.

**EX022.** Trancou o depósito e providenciou a trituração segura das cópias vencidas.

**EX023.** Para que o negócio decida se houve violação e se precisa notificar.

**EX024.** Sim, os funcionários têm direitos pelo GDPR e pela LGPD.

**EX025.** Suas anotações e capturas de tela podem espalhar dados pessoais.

**EX026.** Saber que a revisão quer melhorar os processos, e não flagrar pessoas.

**EX027.** O caixa enviando toda noite as compras de medicamentos ao aplicativo de fidelidade.

**EX028.** Nomes, endereços e a descrição de um pacote lacrado.

**EX029.** Quatro.

**EX030.** Os do aplicativo de fidelidade e das entregas.

**EX031.** Instruções, confidencialidade, segurança e exclusão.

**EX032.** O artigo 9(2)(h), a prestação de cuidados de saúde.

**EX033.** Consentimento explícito, porque usam dados de saúde.

**EX034.** Trinta dias, depois é sobrescrito.

**EX035.** Os dados de fidelidade e os registros de entrega no celular do entregador.

**EX036.** Menos dados guardados significa menos dados que podem ser expostos.

**EX037.** Antes de o tratamento começar.

**EX038.** Se os clientes esperariam aquele fluxo.

**EX039.** Cinco de dez (50%).

**EX040.** Rastreia os deslocamentos dos clientes de forma invasiva e inesperada.

**EX041.** Do modelo padrão de cadastro do fornecedor.

**EX042.** Minimização e limitação da finalidade.

**EX043.** Cinco.

**EX044.** Um responsável, uma estimativa de custo e uma data-alvo.

**EX045.** As compras de medicamentos sendo enviadas ao fornecedor da fidelidade.

**EX046.** Que retirar campos reduziria o valor do aplicativo.

**EX047.** Cinco campos.

**EX048.** Só o gasto total e as categorias que não são medicamentos.

**EX049.** Para confirmar que o plano funcionou, em vez de supor.

**EX050.** Governança, riscos e compliance.


**EX051.** A Juniper consegue ligar 44021 a um cliente, então o número é dado pessoal mesmo sem nome. Pontos não declaram nem revelam uma doença, então ainda não é dado de saúde.

**EX052.** A linha grampeada torna o papel dado de saúde porque revela uma condição. O papel já era dado pessoal. A recusa da foto do balcão não muda.

**EX053.** Uma tela viva de dispensação é o registro de um cliente real, o que o escopo assinado exclui, e o celular o copiaria. Ela usa o cliente de teste inventado e guarda a captura na pasta criptografada da loja.

**EX054.** A comunicação contém o local, a hora e o que ela viu. Ela não move as cópias e não as lê.

**EX055.** O contrato da fidelidade não cobre uma oferta com o nome do medicamento. Antes de qualquer mensagem dessas, a loja precisa de consentimento explícito para essa finalidade, e o contrato da fidelidade ainda precisa dos termos do artigo 28.

**EX056.** A limitação da conservação falha porque os registros de entrega não têm data de fim. O dono define um prazo de entrega. Sofia não inventa o prazo profissional de retenção das receitas.

**EX057.** O script testa se o nome do campo está na união das finalidades. Ele não lê os valores dentro de `purchase_history`. O nome de um medicamento na exportação continua sendo falha da conferência de conteúdo.

**EX058.** A conferência dos campos passou e a do conteúdo falhou. Sofia não fecha a ação.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da Resolução CD/ANPD nº 15, de 24 de abril de 2024, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Brasil. Agência Nacional de Proteção de Dados. (2024). *Resolução CD/ANPD nº 15, de 24 de abril de 2024 — Aprova o Regulamento de Comunicação de Incidente de Segurança*. Diário Oficial da União. <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO/IEC. (2011). *ISO/IEC 29100:2011 Information technology — Security techniques — Privacy framework*. <https://www.iso.org/standard/45123.html>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
