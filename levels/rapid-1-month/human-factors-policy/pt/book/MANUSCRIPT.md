# Fatores Humanos e Política Cibernética: Curso Rápido

- Idioma: português do Brasil (`pt`); curso 006, curso rápido (1 mês). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado, com vinte aulas em português e revisão de equivalência pendente**. Os capítulos 1–20 e EX001–EX066 com respostas estão disponíveis. Os quatro capítulos iniciais, seus cinquenta pares e os dois programas foram preservados. A revisão integral técnica, linguística, de fontes, direitos e acessibilidade continua aberta; presença de texto não significa livro concluído. Nenhuma renderização A4 desta fonte é declarada; uma medição anterior não verifica o texto alterado.
- Público: funcionários e voluntários de pequenas organizações beneficentes e comunitárias que precisam de um começo rápido e prático em segurança centrada nas pessoas.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios contam os sistemas que cada função alcança e resumem os tempos de reporte num teste guiado, ambos sobre dados sintéticos; nenhum funcionário, voluntário, doador, e-mail ou conta real está envolvido. O teste guiado usa uma conta de e-mail de teste e voluntários que conhecem o propósito. O curso não recomenda phishing simulado; se algum dia for usado, deve ser anunciado, acordado com os representantes dos funcionários e dos voluntários, evitar iscas sobre dinheiro, comida ou dificuldades, dar um retorno gentil e relatar apenas totais. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este livro

Leia na ordem. Os quatro capítulos iniciais acompanham uma coordenadora de operações num pequeno banco de alimentos: fundamentos e primeiras decisões; escopo, permissão e prática segura; sistemas, dados e dependências; e um laboratório guiado com um plano de um mês. Os capítulos 5–20 examinam decisões posteriores sem transformar propostas em resultados realizados. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

<a id="pt-translation-ch05-10"></a>

### Continuação traduzida — capítulos 05–10

Este lote incorpora seis capítulos, EX051–EX056 e suas respostas no mesmo livro. Fonte: `levels/rapid-1-month/human-factors-policy/en/book/MANUSCRIPT.md`, revisão `bb01c9fa8768320fdc5e2fdaee91c4ecc26d83a1`, blob `51818a05bf99ecb52b4603ff970cb679640bca73`; alvo português anterior: `3cad3561072a3cf8667099e773cd1f673b621fe6`. Responsabilidade editorial: hiagokinlevi. A disponibilidade passa de **4/20 para 10/20 posições de capítulo (50%)**, e de **50/66 para 56/66 IDs com respostas (84,85%)**. São medidas de presença, não equivalência integral aprovada.

A sequência 05–10 preserva ensino, objetivos, tabelas, rubricas 0–3 e gabaritos da fonte. Tente cada exercício antes de seguir o link para sua resposta. Os capítulos seguintes estão [neste manuscrito](#ch-11). O [registro do lote](PLAN.md#translation-review) delimita a comparação e os testes; as [notas técnicas separadas](#pt-human-limits-05-10) distinguem o que os programas calculam do que não observam. Esta publicação não declara a coleção inglesa ou portuguesa concluída.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Ruth Adeyemi** | Coordenadora de operações e participante do curso rápido | Inventada |
| **Callum Shaw** | Facilitador | Inventado |
| **Oakmere Adult Learning Centre** | Instituição de formação fictícia | Inventada |
| **Riverbend Food Bank** | Organização beneficente fictícia, 12 funcionários e 60 voluntários | Inventada |

### Fontes principais

Adams e Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806); Sasse, Brostoff e Weirich (2001), [doi:10.1023/A:1011902718709](https://doi.org/10.1023/A:1011902718709); Hadnagy (2018); Cialdini (2021); Bada, Sasse e Nurse (2019), arXiv:1901.02672; Merritt et al. (2024), NIST SP 800-50r1. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Fatores humanos e política cibernética: fundamentos e decisões

### Objetivos de aprendizagem

Você vai (1) explicar por que as pessoas, e não só a tecnologia, decidem os resultados de segurança; (2) reconhecer táticas comuns de engano; (3) tomar três decisões iniciais para uma pequena organização beneficente.

### 1.1 Pessoas e segurança

Ruth Adeyemi coordena as operações do fictício Riverbend Food Bank, um banco de alimentos beneficente com doze funcionários e sessenta voluntários. Ela entra num curso rápido de um mês no fictício Oakmere Adult Learning Centre, orientada pelo facilitador Callum Shaw. Callum começa com uma ideia simples: a maioria dos ataques contra pequenas organizações beneficentes chega às pessoas antes de chegar aos sistemas. Uma fatura falsa de fornecedor, uma ligação de alguém fingindo ser do banco ou um e-mail que pede a um voluntário que faça login em algum lugar dependem todos de uma pessoa agir. A segurança, portanto, depende de ajudar as pessoas a agir com segurança sob as pressões do dia a dia.

### 1.2 Não são o inimigo

Callum apresenta dois artigos clássicos. Adams e Sasse (1999), Users are not the enemy, mostraram que as pessoas descumprem as regras de segurança sobretudo porque as regras não se encaixam no seu trabalho, e não por descuido. Sasse, Brostoff e Weirich (2001) defenderam transformar o chamado elo mais fraco por meio de um design melhor. Ruth reconhece isso no Riverbend: os voluntários compartilham um único login da planilha de doações porque nunca se providenciou a criação de contas individuais. O problema é a configuração, não a atitude dos voluntários, e culpá-los só os faria esconder os erros.

### 1.3 Táticas de engano

Ruth aprende as táticas comuns descritas por Hadnagy (2018) e explicadas pelos princípios de influência de Cialdini. Os atacantes alegam autoridade, como quando se passam pelo banco ou por um grande doador; criam urgência, como um prazo que vence hoje; e usam a simpatia ou a familiaridade, como quando copiam o estilo de um fornecedor conhecido. No Riverbend, um ataque típico poderia ser um e-mail de um endereço parecido com o do atacadista de alimentos pedindo pagamento para novos dados bancários. Conhecer esses padrões ajuda Ruth a desenhar verificações simples que não dependem de perceber cada pista.

### 1.4 Conhecimento não basta

Callum avisa que falar às pessoas sobre as táticas raramente muda o comportamento por si só. Bada, Sasse e Nurse (2019) constataram que as campanhas de conscientização muitas vezes falham quando se apoiam no medo ou supõem que o conhecimento leva à ação. O NIST SP 800-50r1 (Merritt et al., 2024) descreve programas de aprendizagem que combinam conscientização, treinamento por função e avaliação. Para uma pequena organização beneficente, conclui Ruth, a abordagem prática é ter alguns hábitos fáceis, procedimentos claros para as tarefas arriscadas e um jeito amigável de pedir ajuda, em vez de palestras longas que as pessoas esquecem.

### 1.5 Três decisões iniciais

Ruth toma três decisões iniciais para o Riverbend. Primeiro, qualquer alteração dos dados bancários de um fornecedor será conferida ligando para o fornecedor no número que já consta do cadastro. Segundo, funcionários e voluntários serão informados com clareza de que reportar qualquer coisa estranha é bem-vindo e nunca leva à culpa. Terceiro, o login compartilhado da planilha de doações será substituído por contas individuais. Ela escreve as decisões numa nota de uma página para a gerente da organização, explicando em linguagem simples o motivo de cada uma. Callum observa que essas decisões atacam os maiores riscos a baixo custo.

### Exemplo resolvido

Ruth aprende por que as pessoas decidem os resultados, reconhece as táticas de autoridade e urgência e toma três decisões: retorno de ligação para alterações bancárias, uma mensagem de reporte sem culpa e contas individuais.

> **Caso sintético.** O Riverbend é sintético; Adams e Sasse (1999), Sasse et al. (2001), Hadnagy (2018), Cialdini (2021), Bada et al. (2019) e o SP 800-50r1 são reais.

### Erros e limites

As decisões precisam de continuidade. As equipes pequenas mudam com frequência.

### Exercícios

- **EX001 — Tamanho da organização.** Quantos funcionários e voluntários o Riverbend tem? *Rubrica:* 3 = doze funcionários e sessenta voluntários;; 2 = 72;; 1 = vago;; 0 = nenhuma.

- **EX002 — Onde os ataques chegam.** Segundo Callum, ao que a maioria dos ataques contra pequenas organizações beneficentes chega primeiro? *Rubrica:* 3 = às pessoas, antes de chegarem aos sistemas;; 2 = às pessoas, sem o contraste com os sistemas;; 1 = aos sistemas;; 0 = nenhuma.

- **EX003 — Causa do descumprimento.** Por que as pessoas descumprem as regras de segurança, segundo Adams e Sasse (1999)? *Rubrica:* 3 = as regras não se encaixam no seu trabalho;; 2 = encaixe;; 1 = descuido;; 0 = nenhuma.

- **EX004 — Causa do login compartilhado.** Por que os voluntários compartilham um único login de doações? *Rubrica:* 3 = nunca se providenciaram contas individuais;; 2 = configuração;; 1 = preguiça;; 0 = nenhuma.

- **EX005 — Exemplo de autoridade.** Dê um exemplo de tática de autoridade. *Rubrica:* 3 = passar-se pelo banco ou por um grande doador;; 2 = autoridade;; 1 = vago;; 0 = nenhuma.

- **EX006 — Exemplo de urgência.** Dê um exemplo de tática de urgência. *Rubrica:* 3 = um prazo que vence hoje;; 2 = prazo;; 1 = vago;; 0 = nenhuma.

- **EX007 — Ataque típico.** Que ataque típico o Riverbend poderia enfrentar? *Rubrica:* 3 = um e-mail de endereço parecido com o do atacadista com novos dados bancários;; 2 = fraude de fatura;; 1 = vago;; 0 = nenhuma.

- **EX008 — Fraqueza das campanhas.** Por que as campanhas de conscientização muitas vezes falham, segundo Bada et al. (2019)? *Rubrica:* 3 = o medo e a suposição de que o conhecimento leva à ação;; 2 = medo;; 1 = vago;; 0 = nenhuma.

- **EX009 — Conteúdo do SP 800-50r1.** O que o SP 800-50r1 combina nos programas de aprendizagem? *Rubrica:* 3 = conscientização, treinamento por função e avaliação;; 2 = três;; 1 = palestras;; 0 = nenhuma.

- **EX010 — Abordagem prática.** Que abordagem prática convém a uma pequena organização beneficente? *Rubrica:* 3 = hábitos fáceis, procedimentos claros e ajuda amigável;; 2 = hábitos;; 1 = palestras longas;; 0 = nenhuma.

- **EX011 — Primeira decisão.** Qual é a primeira decisão de Ruth? *Rubrica:* 3 = ligar para os fornecedores no número do cadastro antes de alterações bancárias;; 2 = retorno de ligação;; 1 = vago;; 0 = nenhuma.

- **EX012 — Segunda decisão.** Qual é a segunda decisão de Ruth? *Rubrica:* 3 = dizer a todos que reportar é bem-vindo, sem culpa;; 2 = sem culpa;; 1 = vago;; 0 = nenhuma.

- **EX013 — Terceira decisão.** Qual é a terceira decisão de Ruth? *Rubrica:* 3 = substituir o login compartilhado por contas individuais;; 2 = contas;; 1 = vago;; 0 = nenhuma.

### Síntese

A segurança em organizações pequenas começa pelas pessoas, por procedimentos simples e por uma cultura de reporte acolhedora.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 20 na referência; 10 disponíveis em português)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Escopo, permissão e prática segura

### Objetivos de aprendizagem

Você vai (1) definir o escopo do trabalho de segurança numa pequena organização beneficente; (2) obter permissão e respeitar limites; (3) praticar com segurança e ética, inclusive quanto às simulações.

### 2.1 Definição do escopo

Callum pede a Ruth que escreva o que seu trabalho de segurança vai abranger. Estão no escopo o reporte de mensagens suspeitas, o procedimento de alteração bancária, as contas individuais e um guia curto de boas-vindas para os voluntários. Ficam fora do escopo ler o e-mail de qualquer pessoa, monitorar o que os voluntários fazem e qualquer teste que engane as pessoas sem acordo. Pôr o escopo por escrito ajuda Ruth a explicar sua função aos colegas e a protege de pedidos que prejudicariam a confiança, como vigiar determinados voluntários. A gerente o lê.

### 2.2 Permissão

Ruth pede à gerente da organização e à presidente do conselho de curadores que aprovem seu escopo de uma página. Elas o assinam. Ruth conta aos funcionários e aos coordenadores de voluntários o que vai fazer e por quê. Callum explica que a permissão importa mesmo para mudanças pequenas e amigáveis, porque o trabalho de segurança mexe com as contas das pessoas, com seus dados e com a sensação de que confiam nelas. Pedir antes também traz ideias úteis: a coordenadora de voluntários sugere incluir o guia no kit de integração que todo voluntário novo já recebe, o que poupa Ruth de criar um processo separado.

### 2.3 Manuseio seguro dos reportes

Ruth aprende hábitos seguros para lidar com as mensagens reportadas. Ela nunca clica em links nem abre anexos dos e-mails reportados; encaminha-os ao voluntário de TI da organização pelo método combinado; e registra apenas a data, o tipo e o desfecho, não quem reportou. Se um reporte sugere algo grave, como dados de doadores enviados ao endereço errado, ela segue as etapas de incidente da organização e pede ajuda ao voluntário de TI, em vez de investigar sozinha. O manuseio seguro protege tanto a organização quanto a pessoa que reportou.

### 2.4 Simulações e ética

A gerente da organização pergunta se o Riverbend deveria enviar e-mails falsos de phishing para testar os voluntários. Callum explica que o engano pode prejudicar a confiança, da qual depende uma organização baseada em voluntários. Lain, Kostiainen e Čapkun (2022) constataram que algumas práticas comuns de simulação não ajudavam. Ruth recomenda nenhuma simulação por enquanto. Se algum dia forem usadas, as regras devem ser acordadas com os representantes dos funcionários e dos voluntários: anunciar o programa, evitar iscas sobre dinheiro, comida ou dificuldades pessoais, dar retorno gentil na hora, relatar só totais e nunca usar os resultados contra ninguém.

### 2.5 Resumo da prática segura

Ruth escreve para si mesma um resumo curto da prática segura: trabalhar dentro do escopo assinado; pedir antes de alterar o acesso de qualquer pessoa; lidar com os reportes sem clicar; manter os registros sem nomes; usar exemplos sintéticos nos treinamentos; e praticar os procedimentos com encenação anunciada, e não com testes secretos. Ela o prende acima da sua mesa. Callum observa que esses hábitos são o que separa um trabalho de segurança confiável de uma interferência bem-intencionada, e que importam ainda mais em organizações beneficentes, onde as pessoas doam seu tempo livremente e podem simplesmente ir embora se sentirem desconfiança.

### Exemplo resolvido

Ruth escreve um escopo e obtém sua aprovação, adota um manuseio seguro dos reportes, recomenda nenhuma simulação, com regras rígidas para o futuro, e escreve um resumo da prática segura.

> **Caso sintético.** O escopo e as regras são sintéticos; Lain et al. (2022) é real.

### Erros e limites

O escopo pode precisar de atualização. Os voluntários podem não ler os guias.

### Exercícios

- **EX014 — Item fora do escopo.** Cite um item fora do escopo de Ruth. *Rubrica:* 3 = ler o e-mail de qualquer pessoa;; 2 = monitoramento;; 1 = reporte;; 0 = nenhuma.

- **EX015 — Signatárias do escopo.** Quem assinou o escopo de Ruth? *Rubrica:* 3 = a gerente da organização e a presidente do conselho de curadores;; 2 = duas;; 1 = vago;; 0 = nenhuma.

- **EX016 — Ideia da coordenadora.** O que a coordenadora de voluntários sugeriu? *Rubrica:* 3 = incluir o guia no kit de integração;; 2 = integração;; 1 = vago;; 0 = nenhuma.

- **EX017 — Regra dos links reportados.** O que Ruth nunca deve fazer com os links dos e-mails reportados? *Rubrica:* 3 = clicar neles;; 2 = não clicar;; 1 = vago;; 0 = nenhuma.

- **EX018 — Campos registrados.** O que Ruth registra sobre os reportes? *Rubrica:* 3 = apenas data, tipo e desfecho;; 2 = mínimo;; 1 = nomes;; 0 = nenhuma.

- **EX019 — Reporte grave.** O que Ruth faz com um reporte grave? *Rubrica:* 3 = segue as etapas de incidente com o voluntário de TI;; 2 = escala;; 1 = investiga sozinha;; 0 = nenhuma.

- **EX020 — Risco das simulações.** Por que as simulações são arriscadas para uma organização de voluntários? *Rubrica:* 3 = o engano pode prejudicar a confiança;; 2 = confiança;; 1 = custo;; 0 = nenhuma.

- **EX021 — Recomendação sobre simulações.** O que Ruth recomenda agora sobre as simulações? *Rubrica:* 3 = nenhuma simulação por enquanto;; 2 = nenhuma simulação, sem o "por enquanto";; 1 = mensais;; 0 = sem resposta.

- **EX022 — Temas de isca proibidos.** Que temas de isca são proibidos se algum dia houver simulações? *Rubrica:* 3 = dinheiro, comida ou dificuldades pessoais;; 2 = dificuldades;; 1 = vago;; 0 = nenhuma.

- **EX023 — Uso dos resultados.** Como os resultados de simulação podem ser usados? *Rubrica:* 3 = só como totais, nunca contra ninguém;; 2 = agregados;; 1 = vago;; 0 = nenhuma.

- **EX024 — Prática dos procedimentos.** Como os procedimentos devem ser praticados? *Rubrica:* 3 = encenação anunciada;; 2 = encenação;; 1 = testes secretos;; 0 = nenhuma.

- **EX025 — Por que os hábitos importam mais.** Por que os hábitos seguros importam ainda mais nas organizações beneficentes? *Rubrica:* 3 = os voluntários podem ir embora se sentirem desconfiança;; 2 = voluntários;; 1 = vago;; 0 = nenhuma.

- **EX026 — Resumo afixado.** Onde Ruth guarda seu resumo da prática segura? *Rubrica:* 3 = preso acima da sua mesa;; 2 = mesa;; 1 = vago;; 0 = nenhuma.

### Síntese

Escopo claro, permissão e hábitos éticos tornam o trabalho de segurança confiável.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 20 na referência; 10 disponíveis em português)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Fatores humanos e política cibernética: sistemas, dados e dependências

### Objetivos de aprendizagem

Você vai (1) mapear os sistemas, os dados e as pessoas dos quais uma pequena organização beneficente depende; (2) encontrar os pontos em que uma pessoa ou um erro podem causar dano; (3) escolher correções simples.

### 3.1 Mapeamento dos sistemas

Ruth mapeia os sistemas do Riverbend numa página: contas de e-mail compartilhadas, a planilha de doações, uma conta bancária on-line, um aplicativo de escala de voluntários e as páginas da organização nas redes sociais. Ao lado de cada um, escreve quem o usa e que dados ele guarda. A planilha de doações guarda nomes e endereços de doadores; o aplicativo de escala guarda os telefones dos voluntários; a conta bancária pode fazer pagamentos. O mapeamento ajuda Ruth a ver onde ficam os dados pessoais e o dinheiro, que são as coisas que os atacantes mais querem e cuja perda mais prejudicaria a organização.

### 3.2 Dados e pessoas

Ruth anota como os dados circulam entre as pessoas. Os voluntários copiam os dados dos doadores dos formulários em papel para a planilha. A tesoureira aprova os pagamentos depois que a coordenadora encaminha as faturas por e-mail. Os funcionários publicam atualizações nas redes sociais usando uma única senha compartilhada. Em cada passagem, uma mensagem enganosa ou um erro simples pode causar dano. Ela conta quantos sistemas cada pessoa consegue acessar e descobre que a tesoureira, uma voluntária aposentada, alcança quase tudo, enquanto alguns funcionários que precisam acessar a escala não têm esse acesso.

### Laboratório — Contagem dos sistemas que cada função alcança

```python
# Systems each role can reach (synthetic): email, spreadsheet, bank, rota, social media.
access = {"treasurer": {"email", "spreadsheet", "bank", "rota", "social"}, "coordinator": {"email", "spreadsheet", "rota"},
          "warehouse volunteer": {"spreadsheet"}, "staff (rota needed)": {"email"}}
for r, s in access.items(): print(f"{r}: {len(s)} of 5")
```

Execute com `python3 lab_access.py`. Saída verificada:

```text
treasurer: 5 of 5
coordinator: 3 of 5
warehouse volunteer: 1 of 5
staff (rota needed): 1 of 5
```

### 3.3 Pontos únicos de falha

Ruth encontra dois pontos únicos de falha. Só a tesoureira pode aprovar pagamentos, então, se ela está fora, as faturas esperam e a pressão aumenta, algo que os atacantes podem explorar com faturas falsas urgentes. Só um voluntário sabe a senha das redes sociais, então, se essa conta for tomada, ninguém mais consegue recuperá-la rapidamente. Ela também observa que a conta bancária envia alertas apenas para o e-mail pessoal da tesoureira. Cada ponto único significa que uma ausência, um erro ou um engano poderia causar um dano duradouro.

### 3.4 Correções simples

Ruth escolhe correções simples. Um segundo curador é autorizado a aprovar pagamentos, sempre depois de um retorno de ligação em caso de alteração bancária. As contas das redes sociais recebem logins individuais com verificação em duas etapas, e os dados de recuperação ficam com a gerente da organização. Os alertas bancários passam a ir para uma caixa postal compartilhada da organização, além da tesoureira. Os dados de doadores na planilha se limitam ao necessário para as cartas de agradecimento. Cada correção custa pouco e elimina um ponto em que uma pessoa ou um erro poderiam causar um dano grave.

### 3.5 Conferência das correções

Ruth confere se cada correção funciona. Ela pede ao segundo curador que aprove um pequeno pagamento de teste com retorno de ligação, confirma que um alerta bancário de teste chega à caixa postal compartilhada e entra nas redes sociais com sua própria conta para confirmar que a verificação em duas etapas funciona. Ela registra cada conferência com a data. Callum lembra que conferir as correções faz parte do trabalho, porque muitas mudanças de segurança são feitas com boas intenções, mas nunca confirmadas, e falham em silêncio justamente quando mais são necessárias.

### Exemplo resolvido

Ruth mapeia sistemas e dados, conta os acessos por função, encontra os pontos únicos de falha nos pagamentos e nas redes sociais e confere as correções simples.

> **Caso sintético.** Os sistemas e os dados são sintéticos.

### Erros e limites

Os mapas se desatualizam. Os segundos aprovadores precisam de treinamento.

### Exercícios

- **EX027 — Localização dos dados.** Onde ficam os nomes e endereços dos doadores? *Rubrica:* 3 = na planilha de doações;; 2 = planilha;; 1 = aplicativo de escala;; 0 = nenhuma.

- **EX028 — Acesso da tesoureira.** Quantos dos cinco sistemas a tesoureira alcança no laboratório? *Rubrica:* 3 = 5;; 2 = todos;; 1 = 2;; 0 = nenhuma.

- **EX029 — Ponto único nos pagamentos.** Por que a tesoureira é um ponto único de falha? *Rubrica:* 3 = só ela pode aprovar pagamentos;; 2 = aprovação;; 1 = vago;; 0 = nenhuma.

- **EX030 — Ligação com a pressão.** Como uma fatura à espera ajuda os atacantes? *Rubrica:* 3 = aumenta a pressão que as falsificações urgentes exploram;; 2 = urgência;; 1 = vago;; 0 = nenhuma.

- **EX031 — Risco das redes sociais.** Qual é o ponto único nas redes sociais? *Rubrica:* 3 = só um voluntário sabe a senha;; 2 = uma pessoa;; 1 = vago;; 0 = nenhuma.

- **EX032 — Alertas bancários.** Para onde iam originalmente os alertas bancários? *Rubrica:* 3 = só para o e-mail pessoal da tesoureira;; 2 = pessoal;; 1 = vago;; 0 = nenhuma.

- **EX033 — Correção dos pagamentos.** O que corrige o ponto único nos pagamentos? *Rubrica:* 3 = um segundo curador autorizado, com retorno de ligação;; 2 = segundo aprovador;; 1 = vago;; 0 = nenhuma.

- **EX034 — Correção das redes sociais.** Como as contas das redes sociais são protegidas? *Rubrica:* 3 = logins individuais com verificação em duas etapas;; 2 = duas etapas;; 1 = senha compartilhada;; 0 = nenhuma.

- **EX035 — Limite dos dados de doadores.** Que limite vale para os dados dos doadores? *Rubrica:* 3 = só o necessário para as cartas de agradecimento;; 2 = mínimo;; 1 = vago;; 0 = nenhuma.

- **EX036 — Conferência das correções.** Como Ruth conferiu a correção dos alertas bancários? *Rubrica:* 3 = um alerta de teste chegou à caixa postal compartilhada;; 2 = teste;; 1 = vago;; 0 = nenhuma.

- **EX037 — Correções não conferidas.** Por que conferir as correções, segundo Callum? *Rubrica:* 3 = mudanças bem-intencionadas muitas vezes falham em silêncio;; 2 = falha silenciosa;; 1 = vago;; 0 = nenhuma.

- **EX038 — Lacuna de acesso à escala.** Que lacuna Ruth encontrou no acesso à escala? *Rubrica:* 3 = alguns funcionários que precisam dele não o têm;; 2 = acesso faltando;; 1 = vago;; 0 = nenhuma.

### Síntese

Mapear sistemas, dados e pessoas revela pontos únicos de falha que correções simples podem eliminar.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 20 na referência; 10 disponíveis em português)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Fatores humanos e política cibernética: laboratório guiado e síntese aplicada

### Objetivos de aprendizagem

Você vai (1) testar um caminho de reporte com voluntários num ambiente seguro; (2) medir se ele é rápido e claro; (3) escrever um plano de ação de um mês.

### 4.1 Caminho de reporte

O Riverbend não tinha um jeito claro de reportar mensagens suspeitas; as pessoas as mencionavam a quem estivesse por perto, quando mencionavam. Ruth monta um caminho simples: encaminhar qualquer coisa estranha para um endereço compartilhado de reporte ou avisar a coordenadora de plantão, que a encaminha. O voluntário de TI confere o endereço todo dia e responde a cada reporte com um veredito curto e um agradecimento. Ela escreve uma instrução de duas linhas e a acrescenta ao guia dos voluntários e a um cartaz no armazém. O caminho precisa ser rápido, porque os voluntários têm pouco tempo no turno.

### 4.2 Laboratório guiado

No laboratório guiado, Ruth testa o caminho com oito voluntários usando uma conta de e-mail de teste e mensagens sintéticas. Todos sabem que estão testando o caminho, não sendo testados. Cada voluntário recebe três mensagens, uma delas suspeita, e é convidado a reportar qualquer coisa estranha. Ruth cronometra quanto tempo leva o reporte e anota as confusões. O laboratório resume os tempos e os acertos. Sete dos oito reportam corretamente a mensagem suspeita; um encaminha uma mensagem genuína, sem saber qual era a estranha, o que Ruth trata como um reporte útil, e não como um erro.

### Laboratório — Tempos e acertos de reporte no laboratório guiado

```python
# Reporting times (seconds) and success for eight volunteers in the guided lab (synthetic).
times = [25, 31, 34, 38, 42, 47, 95, 110]; correct = [1, 1, 1, 1, 1, 1, 1, 0]
s = sorted(times)
print(f"correct {sum(correct)}/8; median time {(s[3] + s[4]) / 2:.0f} s; over 60 s: {sum(t > 60 for t in times)}")
```

Execute com `python3 lab_route.py`. Saída verificada:

```text
correct 7/8; median time 40 s; over 60 s: 2
```

### 4.3 Aprendizados do teste

O teste mostra que encaminhar leva menos de um minuto para a maioria dos voluntários, mas dois tiveram dificuldade para encontrar o endereço de reporte no celular. Ruth acrescenta o endereço como contato nos celulares compartilhados dos voluntários e pede ao voluntário de TI que crie um modelo de resposta rápida. Os voluntários dizem que gostam de ter retorno, o que bate com as evidências de que o retorno incentiva reportes futuros. Ruth também nota que uma voluntária ficou nervosa por ter reportado uma mensagem genuína, então acrescenta uma linha ao guia: na dúvida, reporte.

### 4.4 Plano de um mês

Ruth escreve um plano de ação de um mês. Semana um: confirmar o procedimento de retorno de ligação com a tesoureira e o segundo curador e enviar a mensagem sem culpa. Semana dois: substituir o login compartilhado de doações por contas individuais. Semana três: lançar o caminho de reporte com o guia e o cartaz. Semana quatro: revisar os reportes, as respostas e eventuais problemas com a gerente da organização. Cada etapa tem um responsável e uma verificação. Callum observa que um plano curto e concreto tem mais chance de ser cumprido do que uma estratégia ambiciosa.

### 4.5 Síntese

No fim do curso, Ruth resume o que aprendeu. A segurança no Riverbend depende das pessoas: voluntários, funcionários e curadores agindo sob pressões reais. As medidas mais úteis são simples: retorno de ligação nas alterações bancárias, contas individuais, um caminho de reporte fácil com respostas amigáveis e nenhuma culpa por erros honestos. Testes enganosos são desnecessários e poderiam prejudicar a confiança. Ela compartilha o resumo com os curadores, que adotam o plano. Callum a lembra de revisá-lo depois de três meses, porque os bons hábitos precisam de atenção regular para durar.

### Exemplo resolvido

Ruth monta um caminho de reporte, testa-o com oito voluntários, corrige o contato no celular e a questão dos reportes na dúvida e escreve um plano de quatro semanas adotado pelos curadores.

> **Caso sintético.** O laboratório e o plano são sintéticos.

### Erros e limites

Teste pequeno. Os planos atrasam sem revisão.

### Exercícios

- **EX039 — Reporte antigo.** Como as mensagens suspeitas eram reportadas antes? *Rubrica:* 3 = mencionadas a quem estivesse por perto;; 2 = informal;; 1 = botão;; 0 = nenhuma.

- **EX040 — Promessa de resposta.** O que o voluntário de TI faz para cada reporte? *Rubrica:* 3 = responde com um veredito curto e um agradecimento;; 2 = retorno;; 1 = vago;; 0 = nenhuma.

- **EX041 — Acertos no laboratório.** Quantos voluntários reportaram corretamente a mensagem suspeita no laboratório? *Rubrica:* 3 = 7 de 8;; 2 = sete;; 1 = 8 de 8;; 0 = nenhuma.

- **EX042 — Mediana do tempo no laboratório.** Qual foi a mediana do tempo de reporte no laboratório? *Rubrica:* 3 = 40 segundos;; 2 = menos de um minuto;; 1 = vago;; 0 = nenhuma.

- **EX043 — Encaminhamento genuíno.** Como Ruth tratou o voluntário que encaminhou uma mensagem genuína? *Rubrica:* 3 = como um reporte útil;; 2 = útil;; 1 = erro;; 0 = nenhuma.

- **EX044 — Correção no celular.** O que corrigiu o problema do celular? *Rubrica:* 3 = acrescentar o endereço de reporte como contato;; 2 = contato;; 1 = vago;; 0 = nenhuma.

- **EX045 — Linha da dúvida.** Que linha Ruth acrescentou ao guia? *Rubrica:* 3 = na dúvida, reporte;; 2 = dúvida;; 1 = vago;; 0 = nenhuma.

- **EX046 — Semana dois.** O que acontece na semana dois do plano? *Rubrica:* 3 = contas individuais substituem o login compartilhado;; 2 = contas;; 1 = vago;; 0 = nenhuma.

- **EX047 — Semana quatro.** O que acontece na semana quatro? *Rubrica:* 3 = revisão dos reportes e dos problemas com a gerente;; 2 = revisão;; 1 = vago;; 0 = nenhuma.

- **EX048 — Estilo do plano.** Por que preferir um plano curto e concreto? *Rubrica:* 3 = tem mais chance de ser cumprido;; 2 = cumprimento;; 1 = vago;; 0 = nenhuma.

- **EX049 — Visão sobre testes enganosos.** Qual é a visão de Ruth sobre os testes enganosos? *Rubrica:* 3 = desnecessários e podem prejudicar a confiança;; 2 = desnecessários;; 1 = vago;; 0 = nenhuma.

- **EX050 — Momento da revisão.** Quando Ruth deve revisar o plano? *Rubrica:* 3 = depois de três meses;; 2 = três meses;; 1 = nunca;; 0 = nenhuma.

### Síntese

Um teste seguro, um plano curto e medidas simples e gentis dão a uma pequena organização beneficente um começo sólido.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 20 na referência; 10 disponíveis em português)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 05 em português →](#ch-05)

Continue para os capítulos 05–10 traduzidos; o quarto módulo anterior não encerra a referência atual.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Um plano adotado não significa que a segunda semana já foi cumprida

### Diagrama — Adoção do plano e evidência de execução

```mermaid
flowchart TD
  A["Os curadores adotam o plano de quatro semanas"] --> B["A segunda semana prevê contas individuais"]
  B --> C{"Há uma nova listagem de acessos nos documentos?"}
  C -->|Não| D["Mantenha as quatro linhas de funções publicadas"]
  C -->|Sim| E["Essa listagem seria uma execução própria"]
```

A adoção define o trabalho. Não executa a segunda semana.

### Dados e limites em texto

```text
saída publicada de acessos
    treasurer: 5 of 5
    coordinator: 3 of 5
    warehouse volunteer: 1 of 5
    staff (rota needed): 1 of 5
plano, segunda semana
    substituir o login compartilhado de doações
        |
        +-- a adoção pelos curadores não é essa substituição
        +-- lab_access.py não é alterado
        +-- nenhuma nova função é acrescentada ao dicionário
```

### Objetivos de aprendizagem

Depois deste capítulo, você deverá conseguir:

1. Manter as linhas de acesso publicadas como a contagem já executada.
2. Distinguir uma etapa da segunda semana adotada no plano de contas já criadas e disponibilizadas.
3. Manter o achado sobre o login compartilhado até que exista uma listagem posterior.

### 5.1 A assinatura inicia o mês. Não conclui a tarefa de terça-feira.

O Capítulo 4 registra que os curadores adotam o plano de quatro semanas de Ruth. A segunda semana desse plano prevê substituir o login compartilhado de doações por contas individuais. Um colega trata a adoção como prova de que a substituição aconteceu e quer reescrever a nota de acessos para que cada função apresente um login individual. A única listagem nos documentos é a saída de quatro linhas de `lab_access.py`. Essa saída ainda descreve a tesoureira, a coordenadora, o voluntário do armazém e os funcionários que precisam da escala. Ela não descreve a criação e a disponibilização concluídas de contas. Ruth mantém o script inalterado. A segunda semana continua sendo uma etapa do plano adotado, não um resultado que ela já possa citar.

### 5.2 Exemplo resolvido

| O que alguém cita | O que os documentos contêm | Decisão |
|---|---|---|
| Os curadores adotam o plano | Uma decisão de seguir as quatro semanas | Mantenha a adoção |
| "Portanto, a segunda semana está concluída." | Nenhuma listagem posterior de acessos | Recuse |
| As quatro linhas de funções publicadas | A primeira execução | Mantenha-as |
| "Acrescente uma linha para cada conta nova." | O dicionário original | Recuse a alteração |

> **Caso sintético.** Nenhum login novo é disponibilizado nesta aula. As quatro linhas continuam sendo a execução verificada.

### Erros e limites

Manter a segunda semana em aberto não cancela a decisão de substituir o login compartilhado. Recusa um resultado que os documentos não contêm.

### Aplicar

- **EX051 — Qual semana foi concluída?** Os curadores adotam o plano. A segunda semana prevê substituir o login compartilhado de doações por contas individuais. A saída de acessos continua sendo as quatro linhas publicadas. A segunda semana foi executada? O que acontece com o script? *Rubrica:* 3 = adoção não é conclusão; as quatro linhas permanecem; não alterar o script; não acrescentar linhas de contas; 2 = o plano foi adotado e a saída permanece; 1 = um desses elementos; 0 = nenhum.

[Resolução de EX051 no apêndice](#answer-ex051).

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — aula 05 (capítulo 05 de 20 na referência inglesa)

[← Capítulo 04](#ch-04) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Sete de oito não são oito acertos perfeitos

### Diagrama — Encaminhamento útil versus contagem de acertos

```mermaid
flowchart TD
  P["Saída publicada: correct 7/8"] --> G["Uma mensagem genuína foi encaminhada"]
  G --> U["Ruth trata esse encaminhamento como útil"]
  U --> R{"Alguém troca o 0 por 1?"}
  R -->|Sim| N["Recuse. Isso seria outra lista"]
  R -->|Não| K["7/8 permanece, e o encaminhamento continua útil"]
```

Uma interpretação acolhedora não reescreve a contagem de acertos.

### Dados e limites em texto

```text
lab_route.py
    correct 7/8
    median time 40 s
    over 60 s: 2
o oitavo indicador
    uma mensagem genuína, encaminhada
    registrada como 0 na lista correct
        |
        +-- útil não é a mesma afirmação que correto
        +-- o 0 não é invertido
        +-- ninguém é identificado pelo nome
```

### Objetivos de aprendizagem

Depois deste capítulo, você deverá conseguir:

1. Manter `correct 7/8` como a linha publicada de acertos.
2. Manter o encaminhamento da mensagem genuína como um reporte útil.
3. Recusar uma lista reescrita que produziria oito de oito.

### 6.1 Útil e correto respondem a perguntas diferentes

O laboratório guiado pediu a oito voluntários que reportassem qualquer coisa estranha. Sete reportaram a mensagem suspeita. Uma pessoa encaminhou uma mensagem genuína, e Ruth trata esse encaminhamento como um reporte útil, em vez de repreendê-la. Um colega diz que esse acolhimento significa que a saída deveria mostrar oito de oito. O programa conta apenas a mensagem suspeita. O encaminhamento genuíno corresponde ao 0 final na lista de acertos, e por isso a linha mostra 7/8. Chamá-lo de útil não altera esse 0. Ruth não modifica `lab_route.py` nem identifica a pessoa pelo nome.

### 6.2 Exemplo resolvido

| Afirmação | A qual pergunta responde | Decisão |
|---|---|---|
| Sete reportaram a mensagem suspeita | A lista de acertos | Mantenha 7/8 |
| O outro encaminhamento foi um reporte útil | A interpretação de Ruth sobre a pessoa | Mantenha essa interpretação |
| "Então o laboratório foi 8/8." | Outra contagem | Recuse |
| "Troque o último 0 por 1." | A lista publicada | Recuse |

> **Caso sintético.** A oitava pessoa permanece sem nome. O 0 pertence à lista já executada.

### Erros e limites

Proteger a pessoa de culpa não exige uma fração mais bonita. A fração e o acolhimento podem permanecer juntos.

### Aplicar

- **EX052 — Qual número muda?** Sete de oito reportaram a mensagem suspeita. A outra pessoa encaminhou uma mensagem genuína, e Ruth considera isso útil. A saída pode passar a 8/8? O que acontece com o script? *Rubrica:* 3 = 7/8 permanece; o encaminhamento genuíno continua sendo um reporte útil e não é reclassificado como reporte correto de mensagem suspeita; não alterar o script; não identificar voluntário pelo nome; 2 = 7/8 permanece e a pessoa não é culpabilizada; 1 = um desses elementos; 0 = nenhum.

[Resolução de EX052 no apêndice](#answer-ex052).

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — aula 06 (capítulo 06 de 20 na referência inglesa)

[← Capítulo 05](#ch-05) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Um alerta de teste não é cada alerta posterior

### Diagrama — Teste de entrega versus próximo alerta real

```mermaid
flowchart TD
  O["Os alertas iam apenas ao e-mail pessoal da tesoureira"] --> F["Uma caixa postal compartilhada também é acrescentada"]
  F --> T["Um alerta de teste chegou a essa caixa postal"]
  T --> L{"O teste dispensa a conferência do próximo alerta real?"}
  L -->|Não| K["O próximo alerta ainda precisa ser observado"]
```

A conferência do caminho usa uma mensagem. Não é uma promessa sobre a mensagem seguinte.

### Dados e limites em texto

```text
destino original
    somente o e-mail pessoal da tesoureira
correção
    caixa postal compartilhada da organização, além da tesoureira
conferência já realizada
    um alerta de teste chegou à caixa postal compartilhada
        |
        +-- a cópia pessoal não é removida
        +-- o teste não é o próximo alerta de fatura
        +-- nenhuma chegada posterior é inventada
```

### Objetivos de aprendizagem

Depois deste capítulo, você deverá conseguir:

1. Manter o alerta de teste como uma chegada confirmada.
2. Manter a cópia pessoal da tesoureira.
3. Recusar o uso do teste como prova de cada alerta posterior.

### 7.1 A caixa postal foi acrescentada ao lado do endereço antigo e testada uma vez

Os alertas bancários iam apenas ao e-mail pessoal da tesoureira. A correção também os envia a uma caixa postal compartilhada da organização. Ruth confirmou que um alerta de teste chegou a essa caixa postal e registrou a conferência. Um colega risca o endereço pessoal da página e escreve que os alertas futuros estão resolvidos. Os documentos dizem "além de", não "em vez de". Uma chegada não descreve o próximo alerta real do banco. Ruth não remove a cópia da tesoureira, e esta aula não inventa um segundo teste.

### 7.2 Exemplo resolvido

| Frase | Sustentação nos documentos | Decisão |
|---|---|---|
| Um alerta de teste chegou à caixa postal compartilhada | A conferência registrada por Ruth | Pode permanecer |
| A tesoureira também continua recebendo alertas | "Além de" | Pode permanecer |
| "Todos os alertas posteriores chegarão." | Nenhum teste posterior | Recuse |
| "Exclua o endereço pessoal." | A correção não determinou isso | Recuse |

> **Caso sintético.** Nenhum segundo alerta é redigido. A tesoureira continua sem nome.

### Erros e limites

Manter a cópia pessoal não significa que a caixa postal compartilhada fosse desnecessária. Significa que os documentos não substituíram um destino pelo outro.

### Aplicar

- **EX053 — O que o teste abrangeu?** Um alerta bancário de teste chegou à caixa postal compartilhada. Os alertas também continuam indo à tesoureira. Um integrante da equipe exclui o endereço pessoal e diz que os alertas posteriores estão garantidos. O que permanece? O que não está garantido? *Rubrica:* 3 = o teste realizado permanece; a cópia pessoal permanece; um alerta posterior não está garantido; não inventar segundo teste; 2 = um teste não é cada alerta, e a cópia pessoal permanece; 1 = um desses elementos; 0 = nenhum.

[Resolução de EX053 no apêndice](#answer-ex053).

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — aula 07 (capítulo 07 de 20 na referência inglesa)

[← Capítulo 06](#ch-06) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Um pagamento de teste não valida os novos dados do atacadista

### Diagrama — Pagamento de teste versus autorização de um novo pedido

```mermaid
flowchart TD
  T["Um pequeno pagamento de teste usou o retorno de ligação"] --> P["Essa conferência testou o caminho do segundo curador"]
  W["Um remetente parecido com o atacadista pede novos dados bancários"] --> C["Ligue para o número já cadastrado"]
  P --> R{"O teste aprova o pedido do atacadista?"}
  R -->|Não| K["O pedido ainda precisa de sua própria ligação"]
```

O ensaio de ontem não responde à fatura de hoje.

### Dados e limites em texto

```text
conferência já realizada
    segundo curador
    pequeno pagamento de teste
    retorno de ligação utilizado
ainda necessário para uma alteração real
    ligar para o fornecedor no número cadastrado
isca típica
    endereço parecido com o do atacadista
    novos dados bancários
        |
        +-- o pagamento de teste não identifica fornecedor
        +-- nenhum valor é registrado aqui
        +-- a isca não é paga
```

### Objetivos de aprendizagem

Depois deste capítulo, você deverá conseguir:

1. Manter o pequeno pagamento de teste como uma conferência do caminho do segundo curador.
2. Submeter um pedido posterior de alteração bancária à ligação para o número cadastrado.
3. Recusar o uso do ensaio como aprovação de uma fatura enviada por um remetente semelhante ao legítimo.

### 8.1 O retorno de ligação foi praticado. Não foi usado para aprovar um fornecedor.

Ruth pediu ao segundo curador que aprovasse um pequeno pagamento de teste, e essa aprovação usou um retorno de ligação. Separadamente, a decisão inicial exige conferir qualquer alteração dos dados bancários de um fornecedor ligando para o número já cadastrado. Um colega recebe uma mensagem de um endereço parecido com o do atacadista de alimentos, pedindo pagamento para novos dados bancários, e diz que o teste torna o caminho confiável o suficiente para pagar. O teste não tinha fornecedor nem conta nova. A mensagem semelhante à legítima é a situação para a qual a ligação foi prevista. Ruth não faz o pagamento, não inventa um valor nem o nome verdadeiro do atacadista.

### 8.2 Exemplo resolvido

| Item | O que é | Decisão |
|---|---|---|
| Pequeno pagamento de teste com retorno de ligação | Uma conferência do segundo curador | Pode permanecer como essa conferência |
| Remetente parecido com o atacadista, dados novos | A isca típica | Não pague |
| "O ensaio abrangeu esta fatura." | Um salto de conclusão | Recuse |
| Ligar para o número cadastrado | A regra para uma alteração real | Continua necessário |

> **Caso sintético.** Nenhum nome de fornecedor, número de conta ou valor é acrescentado.

### Erros e limites

Recusar a isca não desfaz o pagamento de teste. O ensaio e a fatura são objetos diferentes.

### Aplicar

- **EX054 — Qual pagamento era o teste?** O segundo curador aprovou um pequeno pagamento de teste com retorno de ligação. Depois, um remetente parecido com o atacadista pede novos dados bancários. O teste aprova esse pedido? Qual ligação continua necessária? *Rubrica:* 3 = o teste não aprova a isca; ligar para o número já cadastrado; não pagar; não inventar valor nem nome de fornecedor; 2 = a isca não é o pagamento de teste; 1 = um desses elementos; 0 = nenhum.

[Resolução de EX054 no apêndice](#answer-ex054).

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — aula 08 (capítulo 08 de 20 na referência inglesa)

[← Capítulo 07](#ch-07) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — A lacuna da escala não se resolve copiando a linha da tesoureira

### Diagrama — Acesso à escala sem ampliar outros privilégios

```mermaid
flowchart TD
  S["staff (rota needed): 1 of 5"] --> G["Têm e-mail e não têm a escala"]
  G --> C{"Alguém lhes concede os cinco sistemas da tesoureira?"}
  C -->|Sim| R["Recuse. A lacuna é a escala, não o banco"]
  C -->|Não| K["A linha publicada permanece em 1 of 5"]
```

O sistema que falta é indicado pela função. Isso não é um convite para copiar outra função.

### Dados e limites em texto

```text
funcionários que precisam da escala
    somente e-mail
    1 of 5
tesoureira
    email, spreadsheet, bank, rota, social
    5 of 5
lacuna registrada por Ruth
    alguns funcionários que precisam da escala não têm esse acesso
        |
        +-- a correção seria a escala, não o conjunto inteiro
        +-- esta aula também não concede a escala
        +-- a saída não é reescrita
```

### Objetivos de aprendizagem

Depois deste capítulo, você deverá conseguir:

1. Interpretar `staff (rota needed): 1 of 5` como e-mail sem acesso à escala.
2. Recusar a cópia dos cinco sistemas da tesoureira para essa função.
3. Manter a lacuna em aberto nesta aula.

### 9.1 O nome da função indica qual sistema está faltando

A listagem de acessos imprime `staff (rota needed): 1 of 5`. O dicionário dá a essa função apenas e-mail. A nota de Ruth diz que alguns funcionários que precisam da escala não têm esse acesso. Um colega "corrige" a linha concedendo a esses funcionários os cinco sistemas da tesoureira, inclusive banco e redes sociais. A lacuna é a escala. Não é motivo para entregar pagamentos ou páginas públicas. Esta aula também não concede a escala, porque nenhuma nova listagem foi executada. A linha publicada permanece em 1 of 5. Ruth não altera `lab_access.py`.

### 9.2 Exemplo resolvido

| Proposta | O que altera | Decisão |
|---|---|---|
| Manter a linha dos funcionários em 1 of 5 | Nada | Aceite para estes documentos |
| Dar a esses funcionários a escala quando uma alteração real for feita | O sistema que falta | Não foi feito nesta aula |
| Copiar os cinco sistemas da tesoureira | Também banco e redes sociais | Recuse |
| Excluir a função para fazer a lacuna desaparecer | A evidência | Recuse |

> **Caso sintético.** Nenhum funcionário é identificado pelo nome. A escala não é habilitada aqui.

### Erros e limites

Manter a lacuna visível não é decidir negar a escala para sempre. Impede que uma concessão mais ampla se faça passar pela correção menor.

### Aplicar

- **EX055 — Qual sistema estava faltando?** A saída mostra `staff (rota needed): 1 of 5`, e essa função tem apenas e-mail. Um integrante da equipe atribui os cinco sistemas da tesoureira. Qual era a lacuna? O que a saída continua mostrando? *Rubrica:* 3 = a lacuna é a escala, não o banco nem as redes sociais; a linha permanece em 1 of 5; não copiar o conjunto da tesoureira; não alterar o script; esta aula não concede a escala; 2 = a lacuna é a escala e a saída permanece; 1 = um desses elementos; 0 = nenhum.

[Resolução de EX055 no apêndice](#answer-ex055).

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue estudando — aula 09 (capítulo 09 de 20 na referência inglesa)

[← Capítulo 08](#ch-08) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Um login verificado não é uma senha compartilhada destruída

### Diagrama — Login individual verificado e lacunas restantes

```mermaid
flowchart TD
  O["Um voluntário não identificado sabia a senha compartilhada"] --> D["Logins individuais e verificação em duas etapas"]
  D --> R["O login próprio de Ruth passou por uma conferência"]
  R --> Q{"Há comprovação de que a senha antiga foi destruída?"}
  Q -->|Não| K["Não escreva a senha nem identifique o voluntário"]
```

Uma autenticação bem-sucedida em uma conta não comprova todas as outras contas.

### Dados e limites em texto

```text
ponto único anterior
    um voluntário sabe a senha compartilhada das redes sociais
    essa pessoa não é identificada pelo nome
desenho da correção
    logins individuais
    verificação em duas etapas
    dados de recuperação guardados pela gerente da organização
conferência
    Ruth entra com sua própria conta
    a verificação em duas etapas funciona nessa autenticação
        |
        +-- uma conta não é cada conta
        +-- a destruição da senha compartilhada não consta dos documentos
        +-- a senha não é escrita
```

### Objetivos de aprendizagem

Depois deste capítulo, você deverá conseguir:

1. Manter a conferência em duas etapas de Ruth como uma conferência do login dela.
2. Deixar sem afirmação a destruição da senha compartilhada antiga.
3. Não identificar a senha nem o voluntário que a conhecia.

### 10.1 A conferência tinha um único objeto: a autenticação da própria Ruth

Só um voluntário sabia a senha das redes sociais, e o livro nunca identifica essa pessoa pelo nome. A correção são logins individuais, verificação em duas etapas e dados de recuperação guardados pela gerente da organização. Ruth então entra com sua própria conta e vê a verificação em duas etapas funcionar. Um colega escreve "senha compartilhada destruída" e pede que Ruth guarde a senha antiga na nota para permitir comparação. Os documentos mostram uma conferência bem-sucedida. Não mostram uma destruição nem todas as outras contas. Ruth não escreve senha nem inventa nome. A linha da tesoureira na listagem de acessos é outro fato e não é usada para identificar quem conhecia a senha.

### 10.2 Exemplo resolvido

| Frase | Evidência | Decisão |
|---|---|---|
| O login próprio de Ruth passou pela verificação em duas etapas | A conferência | Pode permanecer |
| Os dados de recuperação ficam com a gerente | O desenho da correção | Pode permanecer como desenho |
| "A senha compartilhada foi destruída." | Não consta dos documentos | Recuse |
| "Escreva a senha antiga na margem." | Um segredo que a nota não deve guardar | Recuse |
| Identificar pelo nome o voluntário que a sabia | Nenhum nome foi fornecido | Não invente |

> **Caso sintético.** Nenhuma senha ou conta adicional é criada.

### Erros e limites

Impedir que a nota guarde uma senha não prova que a senha antiga seja inofensiva. Mantém a nota dentro do que foi conferido.

### Aplicar

- **EX056 — O que a autenticação de Ruth comprovou?** A verificação em duas etapas funcionou no login próprio de Ruth nas redes sociais. Um integrante da equipe escreve que a senha compartilhada foi destruída e pede que ela seja copiada para a nota. O que permanece válido? O que você não escreve? *Rubrica:* 3 = a conferência é de uma conta; a destruição não consta dos documentos; não escrever a senha; não identificar o voluntário pelo nome; 2 = um login não é uma senha destruída; 1 = um desses elementos; 0 = nenhum.

[Resolução de EX056 no apêndice](#answer-ex056).

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue estudando — aula 10 (capítulo 10 de 20 na referência inglesa)

[← Capítulo 09](#ch-09) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continue para a próxima aula publicada.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="pt-translation-ch11-20"></a>

### Continuação traduzida — capítulos 11–20

Dez capítulos e EX057–EX066, já escritos numa cópia de trabalho local, foram integrados seletivamente neste livro. Conferiram-se a estrutura, os IDs, os números centrais e uma amostra de sentido contra a fonte inglesa publicada (blob anterior `63c6951d427a84acb4293c5da4cf351751247136`); a comparação semântica integral permanece pendente. As respostas foram vinculadas aos enunciados. Os diagramas automáticos que apenas repetiam a ordem das seções foram omitidos. Esta integração amplia a presença de aulas em português para 20/20 e de pares enunciado–resposta para 66/66; **não** certifica equivalência editorial ou livro concluído. O histórico Git identifica a publicação; a revisão humana independente permanece pendente.

<a id="ch-11"></a>

## Capítulo 11 — "Nenhuma simulação por enquanto" não é uma surpresa amigável

### Objetivos de aprendizagem

Depois deste capítulo, você deverá ser capaz de:

1. Manter a recomendação de nenhuma simulação por enquanto.
2. Reconhecer um e-mail surpresa como uma simulação.
3. Deixar a prática na dramatização anunciada.

### 11.1 A pergunta da gerente já tinha resposta

A gerente da organização perguntou se o Riverbend deveria enviar mensagens falsas para testar os voluntários. A recomendação de Ruth é nenhuma simulação por enquanto, porque o engano pode prejudicar uma confiança da qual os voluntários podem se afastar. Depois que os curadores adotam o plano, um colega propõe uma "surpresa amigável" sobre um turno perdido e diz que não é realmente uma simulação. Uma mensagem que as pessoas não sabem ser um teste é aquilo que o escopo excluiu: um teste que engana as pessoas sem acordo. Turnos perdidos ficam ao lado dos temas de dificuldade que estariam barrados mesmo se um programa algum dia fosse acordado. Ruth não a envia. A dramatização anunciada continua sendo o modo de praticar um procedimento.

### 11.2 Exemplo resolvido

| Proposta | O que ela é de fato | Decisão |
|---|---|---|
| Nenhuma simulação por enquanto | A recomendação | Mantê-la |
| Dramatização anunciada do retorno de ligação | A prática permitida | Pode seguir como prática |
| Um e-mail surpresa sobre um turno perdido | Um truque não anunciado | Recusar |
| "Vamos guardar só os totais, então está bem." | Uma regra para um programa que não foi acordado | Não é motivo para começar |

> **Caso sintético.** Nenhuma isca é enviada. Nenhum voluntário é pontuado.

### Erros e limites

Recusar a surpresa não proíbe falar de táticas numa aula em que as pessoas sabem que estão presentes. A diferença é se a pessoa concordou em ser testada.

### Aplicar

- **EX057 — O que é a surpresa?** Ruth recomendou nenhuma simulação por enquanto. Um colega quer um e-mail de surpresa amigável sobre um turno perdido, guardando apenas os totais. O que você recusa, e que prática continua permitida? *Rubrica:* 3 = recuse a surpresa; é um truque sem acordo; nenhuma simulação por enquanto continua valendo; a dramatização anunciada continua sendo a prática; não envie a mensagem;; 2 = a surpresa é recusada;; 1 = um desses;; 0 = nenhum.

[Resolução de EX057 no apêndice](#answer-ex057).

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue estudando — aula 11 (capítulo 11 de 20 na referência)

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Um nome na linha do reporte quebra o registro

### Objetivos de aprendizagem

Depois deste capítulo, você deverá ser capaz de:

1. Manter o registro de um reporte em data, tipo e desfecho.
2. Recusar um nome nessa linha.
3. Deixar a investigação de um reporte grave com as etapas de incidente e o voluntário de TI.

### 12.1 A acolhida não coleta uma identidade

Ruth registra apenas a data, o tipo e o desfecho de um reporte, não quem o enviou. Esse limite protege a pessoa que falou. Um colega de turma acrescenta um nome "para o agradecimento poder ser pessoal" e também abre o link para ver se a mensagem é real. O agradecimento pode ser feito sem guardar o nome no registro. Abrir o link é o ato que a regra de manuseio proíbe. Se o reporte parece grave, Ruth segue as etapas de incidente e pede ajuda ao voluntário de TI. Ela não investiga sozinha e não inventa um nome só para recusar um.

### 12.2 Exemplo resolvido

| Acréscimo | Permitido? | Decisão |
|---|---|---|
| Data, tipo, desfecho | Sim | Manter esses três |
| O nome de quem reportou | Não | Deixá-lo de fora |
| Clicar no link para conferir | Não | Não clicar |
| Um caso grave investigado por Ruth sozinha | Não | Etapas de incidente, com o voluntário de TI |

> **Caso sintético.** Ninguém que reportou é nomeado e nenhum corpo de mensagem é citado.

### Erros e limites

Omitir o nome não significa que o reporte seja ignorado. O desfecho ainda é registrado, e um caso grave ainda segue adiante.

### Aplicar

- **EX058 — O que entra na linha?** Um reporte chega. Um colega de equipe escreve o nome do voluntário ao lado da data, do tipo e do desfecho, e clica no link. O que você registra, e o que não faz? *Rubrica:* 3 = registre apenas data, tipo e desfecho; não registre o nome; não clique; não invente um nome; um reporte grave segue as etapas de incidente com o voluntário de TI;; 2 = sem nome e sem clique;; 1 = um desses;; 0 = nenhum.

[Resolução de EX058 no apêndice](#answer-ex058).

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue estudando — aula 12 (capítulo 12 de 20 na referência)

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Uma sugestão para o kit de integração não é o kit

### Objetivos de aprendizagem

Depois deste capítulo, você deverá ser capaz de:

1. Manter a ideia da coordenadora como uma sugestão.
2. Manter a semana três como um lançamento que a adoção não concluiu.
3. Recusar a afirmação de que todo voluntário novo já recebeu o guia.

### 13.1 O kit era a prateleira certa. Ninguém mostrou o guia nela.

A coordenadora de voluntários sugere pôr o guia no kit de integração, para Ruth não construir um segundo processo. Essa frase é uma ideia de uma colega. A semana três do plano adotado é o lançamento do caminho de reporte com o guia e o cartaz. Um colega de turma marca "todos os voluntários novos orientados" porque a sugestão era sensata e os curadores adotaram o plano. O arquivo não diz que o kit foi reimpresso e não diz que a semana três foi executada. Ruth não inventa uma contagem de pessoas que leram a página.

### 13.2 Exemplo resolvido

| Afirmação | Situação | Decisão |
|---|---|---|
| A coordenadora sugeriu o kit de integração | Uma ideia | Pode permanecer como ideia |
| Ruth escreveu uma instrução curta | Redação | Pode permanecer |
| A semana três lança o caminho | Uma etapa do plano | Não aparece como concluída |
| "Todo voluntário novo tem o guia." | Nenhuma contagem | Recusar |

> **Caso sintético.** Nenhum voluntário novo é nomeado. Nenhum kit é descrito como reimpresso.

### Erros e limites

Deixar a inclusão inacabada não desperdiça a sugestão. Mantém o lançamento na semana que foi escrita para ele.

### Aplicar

- **EX059 — Quem tem o guia?** A coordenadora sugeriu o kit de integração. A semana três é o lançamento, e os curadores adotaram o plano. Um colega de equipe diz que todo voluntário novo já tem o guia. O que ainda é apenas uma sugestão ou uma etapa, e que contagem falta? *Rubrica:* 3 = a ideia do kit não é uma inclusão concluída; a semana três não aparece como concluída; não afirme que todo voluntário novo tem o guia; não invente contagem;; 2 = a sugestão não é o lançamento;; 1 = um desses;; 0 = nenhum.

[Resolução de EX059 no apêndice](#answer-ex059).

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue estudando — aula 13 (capítulo 13 de 20 na referência)

[← Capítulo 12](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Doze e sessenta não são um censo de setenta e dois

### Objetivos de aprendizagem

Depois deste capítulo, você deverá ser capaz de:

1. Manter doze funcionários e sessenta voluntários como o tamanho publicado.
2. Recusar 72 como censo substituto.
3. Manter a saída de acesso como quatro funções, não como uma contagem de pessoas.

### 14.1 O tamanho da organização e a largura de uma função são contagens diferentes

O Riverbend tem doze funcionários e sessenta voluntários. O programa de acesso não conta essas pessoas. Conta sistemas alcançáveis por quatro funções, cada uma sobre cinco. Um colega de turma soma doze e sessenta, escreve 72 e substitui as linhas de função por "72 of 5". A soma aritmética é 72, mas o caso não estabelece se os grupos se sobrepõem; portanto, não é uma contagem verificada de pessoas distintas. Somar não executa o programa de acesso: pessoas não são o numerador de sua contagem de sistemas por função. O número de funcionários e o número de voluntários permanecem separados. Ruth não edita `lab_access.py`.

### 14.2 Exemplo resolvido

| Número | O que conta | Decisão |
|---|---|---|
| Doze funcionários | Funcionários | Manter |
| Sessenta voluntários | Voluntários | Manter |
| 72 | Soma aritmética; contagem de pessoas distintas não verificada | Recusar como censo ou saída do programa |
| Quatro linhas de função, cada uma de 5 | Sistemas que uma função alcança | Manter essas linhas |

> **Caso sintético.** A soma 72 é a aritmética do colega de turma. Não é uma execução nova.

### Erros e limites

A soma é aritmeticamente correta. Recusar seu uso como censo medido ou como saída de sistemas por função preserva as unidades e deixa visível a possível sobreposição.

### Aplicar

- **EX060 — O que é 72?** O Riverbend tem doze funcionários e sessenta voluntários. A saída de acesso tem quatro linhas de função. Um colega de equipe escreve "72 of 5". Quais números permanecem, e o que você não imprime? *Rubrica:* 3 = doze e sessenta permanecem separados; 72 não é o censo; as quatro linhas de função permanecem; não edite o script;; 2 = 72 é recusado e as linhas de função permanecem;; 1 = um desses;; 0 = nenhum.

[Resolução de EX060 no apêndice](#answer-ex060).

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue estudando — aula 14 (capítulo 14 de 20 na referência)

[← Capítulo 13](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Dois tempos lentos permanecem na lista publicada

### Objetivos de aprendizagem

Depois deste capítulo, você deverá ser capaz de:

1. Manter 95 e 110 dentro da lista de tempos publicada.
2. Manter a mediana em 40 segundos para essa lista completa.
3. Situar a correção do contato no celular depois do teste, não dentro dele.

### 15.1 O par lento é o motivo de os celulares terem sido alterados. Não é um par para apagar.

Dois dos oito tempos passam de um minuto: 95 segundos e 110 segundos. A saída diz `over 60 s: 2`, e a mediana da lista completa ordenada é 40 segundos. Ruth então acrescenta o endereço de reporte como contato nos celulares compartilhados dos voluntários, porque as pessoas tiveram dificuldade para encontrá-lo. Um colega de turma apaga 95 e 110, dizendo que os celulares estão corrigidos e portanto esses tempos já não contam, e pede uma mediana nova. O contato foi acrescentado depois das oito tentativas. Remover o par seria uma lista diferente, e esta aula não executa essa lista. A mediana publicada permanece 40 segundos.

### 15.2 Exemplo resolvido

| Ação | Momento | Decisão |
|---|---|---|
| Manter 95 e 110 | Estão na lista publicada | Aceitar |
| Mediana de 40 segundos | A lista completa | Manter |
| Acrescentar o endereço aos celulares | Depois do teste | Pode permanecer como correção posterior |
| Descartar os dois tempos lentos e recalcular | Uma lista nova | Recusar |

> **Caso sintético.** Nenhuma mediana nova é calculada. Os oito tempos continuam sendo os do programa.

### Erros e limites

Manter os tempos lentos não significa que o contato no celular tenha sido inútil. Significa que o contato não reescreve a tarde que o motivou.

### Aplicar

- **EX061 — Quais tempos permanecem?** A lista publicada inclui 95 e 110, a mediana é 40 segundos e dois tempos estão acima de 60 segundos. Ruth acrescenta o endereço de reporte aos celulares depois. Um colega de equipe descarta os dois tempos lentos. O que permanece, e o que você não recalcula? *Rubrica:* 3 = 95 e 110 permanecem; a mediana permanece 40 segundos para a lista completa; o contato no celular é posterior ao teste; não recalcule; não edite o script;; 2 = os tempos lentos permanecem e a mediana não é refeita;; 1 = um desses;; 0 = nenhum.

[Resolução de EX061 no apêndice](#answer-ex061).

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue estudando — aula 15 (capítulo 15 de 20 na referência)

[← Capítulo 14](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — A adoção não é a revisão de três meses

### Objetivos de aprendizagem

Depois deste capítulo, você deverá ser capaz de:

1. Manter a revisão de três meses como um olhar futuro.
2. Distingui-la da adoção pelos curadores.
3. Recusar achados que o olhar posterior nunca produziu.

### 16.1 O lembrete aponta para a frente. A adoção aponta para o plano.

Callum diz a Ruth que revise o plano depois de três meses, porque os hábitos precisam de atenção para durar. Os curadores adotam o plano no fim do curso. Um colega de turma escreve "revisão de três meses: feita" com base nessa adoção e acrescenta dois achados que a reunião nunca registrou. A adoção é a decisão de começar. O olhar de três meses não tem data no arquivo e não tem notas. A semana quatro, uma conversa com a gerente da organização sobre reportes e problemas, é uma etapa dentro do primeiro mês. Não é a revisão posterior. Ruth não inventa achado algum e não marca os três meses como decorridos.

### 16.2 Exemplo resolvido

| Evento | O que é | Decisão |
|---|---|---|
| Os curadores adotam o plano | O começo | Pode permanecer |
| Revisar depois de três meses | Um lembrete | Mantê-lo no futuro |
| Semana quatro com a gerente | Uma etapa dentro do plano | Não é a revisão de três meses |
| Dois achados dessa revisão posterior | Nada foi escrito | Não os inventar |

> **Caso sintético.** Nenhuma data de calendário é fornecida para a revisão posterior.

### Erros e limites

Deixar a revisão no futuro não enfraquece o lembrete de Callum. Recusa fingir que o lembrete já foi cumprido.

### Aplicar

- **EX062 — Qual reunião foi a revisão?** Os curadores adotam o plano. Callum diz para revisá-lo depois de três meses. Um colega de equipe marca essa revisão como feita e escreve dois achados. O que aconteceu, e o que falta? *Rubrica:* 3 = a adoção não é a revisão de três meses; os três meses não estão datados como decorridos; não invente achados; a semana quatro não é essa revisão posterior;; 2 = a adoção não é a revisão posterior;; 1 = um desses;; 0 = nenhum.

[Resolução de EX062 no apêndice](#answer-ex062).

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue estudando — aula 16 (capítulo 16 de 20 na referência)

[← Capítulo 15](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — A ausência de culpa não é motivo para investigar sozinha

### Objetivos de aprendizagem

Depois deste capítulo, você deverá ser capaz de:

1. Manter a acolhida sem culpa.
2. Encaminhar um reporte grave pelas etapas de incidente com o voluntário de TI.
3. Recusar uma investigação solitária disfarçada de gentileza.

### 17.1 A acolhida e o escalonamento continuam ambos em vigor

A segunda decisão de Ruth diz a funcionários e voluntários que reportar qualquer coisa estranha é bem-vindo e não leva à culpa. Um colega de turma ouve falar de dados de doadores enviados ao lugar errado e diz que Ruth deveria "resolver em silêncio" para ninguém se sentir acusado. Resolver em silêncio, por uma só pessoa, é a investigação que a regra de manuseio já recusou. Um reporte grave segue as etapas de incidente da organização, e Ruth pede ajuda ao voluntário de TI. A ausência de culpa ainda permite um registro de data, tipo e desfecho. Não exige um nome, e esta aula não inventa um doador nem um voluntário.

### 17.2 Exemplo resolvido

| Resposta | Cabe na acolhida? | Decisão |
|---|---|---|
| Agradecer o reporte e registrar data, tipo e desfecho | Sim | Fazer isso |
| Culpar a pessoa | Não | Não fazer |
| Ruth investiga sozinha o caso do endereço errado | Não | Etapas de incidente, com o voluntário de TI |
| Esconder o caso para a acolhida continuar confortável | Não | A acolhida não é ocultação |

> **Caso sintético.** O caso do endereço errado continua sendo o tipo já usado no livro. Ninguém é nomeado.

### Erros e limites

Escalar não transforma quem reportou em suspeito. Leva um caso grave às pessoas que as etapas já nomearam.

### Aplicar

- **EX063 — Quem segue um reporte grave?** Reportar é bem-vindo e ninguém é culpado por um erro honesto. Dados de doadores foram para o endereço errado. Um colega de equipe diz a Ruth para resolver em silêncio, sozinha. O que ainda acontece, e o que a ausência de culpa não permite? *Rubrica:* 3 = a ausência de culpa permanece; ela não investiga sozinha; ela segue as etapas de incidente com o voluntário de TI; o registro ainda pode conter data, tipo e desfecho; não nomeie ninguém;; 2 = nenhuma investigação solitária;; 1 = um desses;; 0 = nenhum.

[Resolução de EX063 no apêndice](#answer-ex063).

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue estudando — aula 17 (capítulo 17 de 20 na referência)

[← Capítulo 16](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — A linha do armazém não herda o banco

### Objetivos de aprendizagem

Depois deste capítulo, você deverá ser capaz de:

1. Ler a linha do armazém como somente a planilha.
2. Manter o segundo curador como a correção dos pagamentos.
3. Recusar pôr o banco na função do armazém.

### 18.1 Um segundo aprovador é uma pessoa com um trabalho, não um conjunto novo para o armazém

O voluntário do armazém alcança um sistema dos cinco: a planilha, que é onde os dados dos doadores, vindos de formulários em papel, são digitados. O ponto único dos pagamentos é corrigido autorizando um segundo curador, que aprova somente depois de um retorno de ligação quando os dados bancários mudam. Um colega de turma vê que a tesoureira alcança o banco e diz que a função do armazém também deveria alcançá-lo, para a organização nunca ficar parada. Espalhar o banco para as pessoas que digitam formulários de doadores é uma concessão mais ampla do que a correção. O segundo curador não é um novo nome da linha do armazém. A linha publicada permanece `warehouse volunteer: 1 of 5`. Ruth não edita o script.

### 18.2 Exemplo resolvido

| Proposta | Efeito | Decisão |
|---|---|---|
| Deixar a linha do armazém em `1 of 5` | Somente a planilha | Aceitar |
| O segundo curador aprova depois de um retorno de ligação | A correção dos pagamentos | Já é a correção escolhida |
| Dar o banco à função do armazém | Uma concessão nova | Recusar |
| "Aí eles podem pagar se a tesoureira estiver fora." | O problema da pressão, resolvido pela função errada | Recusar |

> **Caso sintético.** O segundo curador continua sem nome. A linha do armazém não é reescrita.

### Erros e limites

Manter o banco fora da função do armazém não deixa os pagamentos com uma só pessoa. O segundo curador já é a outra pessoa no desenho.

### Aplicar

- **EX064 — Quem ganha o banco?** A saída do armazém é `1 of 5`, a planilha. Um segundo curador é a correção dos pagamentos. Um colega de equipe dá o banco à função do armazém para as faturas não precisarem esperar. O que permanece `1 of 5`, e quem já era o segundo aprovador? *Rubrica:* 3 = a linha do armazém permanece `1 of 5` e não ganha o banco; o segundo curador continua sendo a correção dos pagamentos; não edite o script;; 2 = a função do armazém não ganha o banco;; 1 = um desses;; 0 = nenhum.

[Resolução de EX064 no apêndice](#answer-ex064).

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue estudando — aula 18 (capítulo 18 de 20 na referência)

[← Capítulo 17](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Um modelo de resposta pedido não é uma resposta já enviada

### Objetivos de aprendizagem

Depois deste capítulo, você deverá ser capaz de:

1. Manter a promessa de resposta como uma promessa.
2. Situar o pedido do modelo depois do laboratório guiado.
3. Recusar a afirmação de que oito respostas foram enviadas com esse modelo.

### 19.1 O pedido veio depois de o relógio já ter parado

O desenho do caminho diz que o voluntário de TI confere o endereço de reporte todo dia e responde a cada reporte com um veredito curto e um agradecimento. Depois que os oito voluntários foram cronometrados, Ruth pede um modelo de resposta rápida, porque as pessoas disseram que gostam de receber retorno. Um colega de turma escreve que o modelo foi usado nas oito mensagens e redige um veredito para colar na nota. O modelo foi pedido depois desses tempos. O arquivo não contém oito respostas enviadas e não contém as palavras de um veredito. Ruth não as inventa. A promessa continua valendo para reportes que vierem depois. Não é evidência sobre os oito.

### 19.2 Exemplo resolvido

| Item | Quando se situa | Decisão |
|---|---|---|
| Um veredito curto e um agradecimento para cada reporte | A promessa | Pode permanecer como promessa |
| Um pedido de modelo rápido | Depois do laboratório | Pode permanecer como pedido |
| "O modelo tratou dos oito." | Antes de o pedido existir | Recusar |
| Um veredito de exemplo escrito agora | Não está no arquivo | Não inventar as palavras |

> **Caso sintético.** Nenhum texto de resposta é redigido. Os oito tempos continuam sendo um exercício de cronometragem.

### Erros e limites

Separar a promessa das oito tentativas não cancela a promessa. Impede que o relógio do laboratório seja enfeitado com uma ferramenta pedida depois.

### Aplicar

- **EX065 — Quando o modelo foi pedido?** O voluntário de TI deve responder a cada reporte com um veredito curto e um agradecimento. Ruth pede um modelo de resposta rápida depois que os oito voluntários são cronometrados. Um colega de equipe diz que o modelo produziu oito respostas. O que é uma promessa, o que é um pedido posterior, e o que você não inventa? *Rubrica:* 3 = a regra de resposta é uma promessa; o modelo foi pedido depois do laboratório; oito respostas enviadas não estão no arquivo; não invente texto de veredito;; 2 = o modelo não é evidência sobre os oito;; 1 = um desses;; 0 = nenhum.

[Resolução de EX065 no apêndice](#answer-ex065).

<!-- open-cyber-academy:chapter-navigation:start ch-19 -->
### Continue estudando — aula 19 (capítulo 19 de 20 na referência)

[← Capítulo 18](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Continue para a próxima aula traduzida.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — O que a nota da organização pode dizer

### Objetivos de aprendizagem

Depois deste capítulo, você deverá ser capaz de:

1. Repetir as linhas de laboratório e as decisões que o arquivo já contém.
2. Rejeitar uma nota que encerra etapas em aberto.
3. Apontar o próximo curso sem chamar esta edição de concluída.

### 20.1 Uma nota pode citar o arquivo. Ela não pode melhorá-lo.

Uma nota de passagem pode dizer o que já estava escrito. O Riverbend ainda tem doze funcionários e sessenta voluntários. A saída de acesso ainda mostra a tesoureira em 5 de 5, a coordenadora em 3 de 5, o voluntário do armazém em 1 de 5 e os funcionários que precisam da escala em 1 de 5. A saída de reporte ainda diz `correct 7/8`, uma mediana de 40 segundos e dois tempos acima de 60 segundos. Os curadores adotaram o plano de quatro semanas. A semana dois, as contas individuais, não aparece como concluída. As simulações continuam desligadas por enquanto. A revisão de três meses não foi realizada. O próprio login social de Ruth passou por uma conferência de verificação em duas etapas, o que não é uma nota de que a senha compartilhada foi destruída.

### 20.2 Exemplo resolvido

| Frase da nota de passagem | Por que falha ou permanece | Decisão |
|---|---|---|
| "A saída de acesso são as quatro linhas de função publicadas." | A primeira execução | Pode permanecer |
| "Os reportes corretos foram 7 de 8, mediana de 40 segundos." | A execução de reporte | Pode permanecer |
| "A saída agora é 8/8 e a mediana foi recalculada." | Nenhuma execução nova | Rejeitar |
| "A semana dois terminou porque o plano foi adotado." | A adoção não é essa etapa | Rejeitar |
| "A revisão de três meses foi realizada." | Não existe essa nota | Rejeitar |

> **Caso sintético.** A nota é uma página de sala de aula sobre o Riverbend. Não é um aviso aos doadores.

### Erros e limites

Atingir o mínimo de planejamento de 20 aulas deixa a revisão independente em aberto. Uma pergunta nova do Riverbend ainda pode merecer uma aula posterior própria. Esta edição portuguesa não conclui a coleção ou a revisão editorial. Fatores humanos continua sendo este curso. Arquitetura de segurança é a disciplina seguinte de quem estuda. As etapas em aberto no Riverbend continuam em aberto nessa passagem. Estes capítulos não certificam a organização beneficente e não entregam uma qualificação a ninguém.

### Aplicar

- **EX066 — Quatro afirmações.** A nota de passagem de um colega de turma diz que a saída de reporte agora é 8/8 com uma mediana nova, que a semana dois está concluída porque os curadores adotaram o plano, que a senha social compartilhada foi destruída e que a revisão de três meses já foi realizada. Quais afirmações você rejeita, e a que as vinte aulas atendem? *Rubrica:* 3 = rejeitar as quatro; a saída de reporte permanece 7/8 com mediana de 40 segundos e dois tempos acima de 60 segundos; a semana dois não aparece como concluída; a destruição da senha compartilhada não está no arquivo; a revisão de três meses não foi realizada; vinte aulas atendem ao mínimo de planejamento e deixam a revisão em aberto;; 2 = rejeitar as quatro afirmações e manter as saídas publicadas;; 1 = uma afirmação;; 0 = nenhum.

[Resolução de EX066 no apêndice](#answer-ex066).

<!-- open-cyber-academy:chapter-navigation:start ch-20 -->
### Continue estudando — aula 20 (capítulo 20 de 20 na referência)

[← Capítulo 19](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Próximo curso →](../../../security-architecture/pt/SUBJECTS.md)

A trilha continua no curso 007; as revisões deste livro permanecem abertas.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX066. Ruth Adeyemi, Callum Shaw, o Oakmere Adult Learning Centre, o Riverbend Food Bank e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Doze funcionários e sessenta voluntários.

**EX002.** Às pessoas, antes de chegarem aos sistemas.

**EX003.** Sobretudo porque as regras não se encaixam no seu trabalho.

**EX004.** Porque nunca se providenciaram contas individuais.

**EX005.** Passar-se pelo banco ou por um grande doador.

**EX006.** Alegar um prazo que vence hoje.

**EX007.** Um e-mail de um endereço parecido com o do atacadista pedindo pagamento para novos dados bancários.

**EX008.** Porque se apoiam no medo ou supõem que o conhecimento leva à ação.

**EX009.** Conscientização, treinamento por função e avaliação.

**EX010.** Alguns hábitos fáceis, procedimentos claros e um jeito amigável de pedir ajuda.

**EX011.** Conferir as alterações de dados bancários ligando para o fornecedor no número do cadastro.

**EX012.** Dizer a funcionários e voluntários que reportar qualquer coisa estranha é bem-vindo e nunca leva à culpa.

**EX013.** Substituir o login compartilhado de doações por contas individuais.

**EX014.** Ler o e-mail de qualquer pessoa, monitorar voluntários ou enganar pessoas sem acordo.

**EX015.** A gerente da organização e a presidente do conselho de curadores.

**EX016.** Incluir o guia no kit de integração já existente.

**EX017.** Clicar neles ou abrir anexos.

**EX018.** Apenas a data, o tipo e o desfecho.

**EX019.** Segue as etapas de incidente e pede ajuda ao voluntário de TI.

**EX020.** Porque o engano pode prejudicar a confiança da qual a organização depende.

**EX021.** Nenhuma simulação por enquanto.

**EX022.** Dinheiro, comida ou dificuldades pessoais.

**EX023.** Só como totais, nunca contra nenhuma pessoa.

**EX024.** Com encenação anunciada, e não com testes secretos.

**EX025.** Porque os voluntários doam seu tempo livremente e podem ir embora se sentirem desconfiança.

**EX026.** Preso acima da sua mesa.

**EX027.** Na planilha de doações.

**EX028.** Todos os cinco sistemas.

**EX029.** Porque só ela pode aprovar pagamentos.

**EX030.** A pressão aumenta, e os atacantes podem explorá-la com faturas falsas urgentes.

**EX031.** Só um voluntário sabe a senha compartilhada.

**EX032.** Só para o e-mail pessoal da tesoureira.

**EX033.** Autorizar um segundo curador, com retorno de ligação nas alterações bancárias.

**EX034.** Com logins individuais, verificação em duas etapas e dados de recuperação guardados pela gerente.

**EX035.** Só o necessário para as cartas de agradecimento.

**EX036.** Confirmando que um alerta bancário de teste chegou à caixa postal compartilhada.

**EX037.** Porque mudanças bem-intencionadas muitas vezes falham em silêncio quando nunca são confirmadas.

**EX038.** Alguns funcionários que precisam de acesso à escala não o têm.

**EX039.** As pessoas as mencionavam a quem estivesse por perto, quando mencionavam.

**EX040.** Responde com um veredito curto e um agradecimento.

**EX041.** Sete de oito.

**EX042.** 40 segundos.

**EX043.** Como um reporte útil, e não como um erro.

**EX044.** Acrescentar o endereço de reporte como contato nos celulares compartilhados dos voluntários.

**EX045.** Na dúvida, reporte.

**EX046.** O login compartilhado de doações é substituído por contas individuais.

**EX047.** Uma revisão dos reportes, das respostas e dos problemas com a gerente da organização.

**EX048.** Porque tem mais chance de ser cumprido do que uma estratégia ambiciosa.

**EX049.** Que são desnecessários e poderiam prejudicar a confiança.

**EX050.** Depois de três meses.

<a id="answer-ex051"></a>

**EX051.** Adoção não é conclusão. As quatro linhas permanecem. Não altere o script. Não acrescente linhas de contas.

[Voltar ao exercício EX051](#ch-05).

<a id="answer-ex052"></a>

**EX052.** 7/8 permanece. O encaminhamento genuíno continua sendo um reporte útil e não é reclassificado como reporte correto de mensagem suspeita. Não altere o script. Não identifique voluntário pelo nome.

[Voltar ao exercício EX052](#ch-06).

<a id="answer-ex053"></a>

**EX053.** O teste realizado permanece. A cópia pessoal permanece. Um alerta posterior não está garantido. Não invente segundo teste.

[Voltar ao exercício EX053](#ch-07).

<a id="answer-ex054"></a>

**EX054.** O teste não aprova a isca. Ligue para o número já cadastrado. Não pague. Não invente valor nem nome de fornecedor.

[Voltar ao exercício EX054](#ch-08).

<a id="answer-ex055"></a>

**EX055.** A lacuna é a escala, não o banco nem as redes sociais. A linha permanece em 1 of 5. Não copie o conjunto da tesoureira. Não altere o script. Esta aula não concede a escala.

[Voltar ao exercício EX055](#ch-09).

<a id="answer-ex056"></a>

**EX056.** A conferência é de uma conta. A destruição não consta dos documentos. Não escreva a senha. Não identifique o voluntário pelo nome.

[Voltar ao exercício EX056](#ch-10).

<a id="answer-ex057"></a>

**EX057.** Recuse a surpresa. É um truque sem acordo. Nenhuma simulação por enquanto continua valendo. A dramatização anunciada continua sendo a prática. Não envie a mensagem.

[Voltar ao exercício EX057](#ch-11).

<a id="answer-ex058"></a>

**EX058.** Registre apenas data, tipo e desfecho. Não registre o nome. Não clique. Não invente um nome. Um reporte grave segue as etapas de incidente com o voluntário de TI.

[Voltar ao exercício EX058](#ch-12).

<a id="answer-ex059"></a>

**EX059.** A ideia do kit não é uma inclusão concluída. A semana três não aparece como concluída. Não afirme que todo voluntário novo tem o guia. Não invente contagem.

[Voltar ao exercício EX059](#ch-13).

<a id="answer-ex060"></a>

**EX060.** Doze e sessenta permanecem separados. 72 não é o censo. As quatro linhas de função permanecem. Não edite o script.

[Voltar ao exercício EX060](#ch-14).

<a id="answer-ex061"></a>

**EX061.** 95 e 110 permanecem. A mediana permanece 40 segundos para a lista completa. O contato no celular é posterior ao teste. Não recalcule. Não edite o script.

[Voltar ao exercício EX061](#ch-15).

<a id="answer-ex062"></a>

**EX062.** A adoção não é a revisão de três meses. Os três meses não estão datados como decorridos. Não invente achados. A semana quatro não é essa revisão posterior.

[Voltar ao exercício EX062](#ch-16).

<a id="answer-ex063"></a>

**EX063.** A ausência de culpa permanece. Ela não investiga sozinha. Ela segue as etapas de incidente com o voluntário de TI. O registro ainda pode conter data, tipo e desfecho. Não nomeie ninguém.

[Voltar ao exercício EX063](#ch-17).

<a id="answer-ex064"></a>

**EX064.** A linha do armazém permanece `1 of 5` e não ganha o banco. O segundo curador continua sendo a correção dos pagamentos. Não edite o script.

[Voltar ao exercício EX064](#ch-18).

<a id="answer-ex065"></a>

**EX065.** A regra de resposta é uma promessa. O modelo foi pedido depois do laboratório. Oito respostas enviadas não estão no arquivo. Não invente texto de veredito.

[Voltar ao exercício EX065](#ch-19).

<a id="answer-ex066"></a>

**EX066.** Rejeite as quatro. A saída de reporte permanece 7/8, com mediana de 40 segundos e dois tempos acima de 60 segundos. A semana dois não aparece como concluída. A destruição da senha compartilhada não está no arquivo. A revisão de três meses não foi realizada. Vinte aulas atendem ao mínimo de planejamento e deixam a revisão em aberto.

[Voltar ao exercício EX066](#ch-20).

<a id="pt-human-limits-05-10"></a>

### Notas editoriais do lote 05–10 — separadas do texto traduzido

**O que os programas observam:** nenhum deles inspeciona uma conta, lê uma mensagem, cria um login ou realiza pagamento. `lab_access.py` conta elementos dos conjuntos fornecidos; o divisor apresentado como cinco é literal. `lab_route.py` soma os rótulos fornecidos em `correct`, ordena os tempos e utiliza as posições 3 e 4 com divisor oito fixo. A frase do Capítulo 6 sobre contar a mensagem suspeita deve ser lida como contagem dos indicadores do caso, não como detecção automática de phishing. Uma nova listagem também não concede autorização nem comprova, por si só, a criação de contas. Os exemplos preservam decisões e pendências da narrativa; ausência de evidência nos documentos não é uma prova universal de ausência de acontecimentos.

**Saídas reproduzidas e limites de generalização:** as listagens completas, transcritas das leituras fixadas, foram executadas em Python 3.13.5. O acesso reproduziu quatro linhas; o reporte reproduziu `correct 7/8; median time 40 s; over 60 s: 2`. Dez entradas alternativas mostraram, entre outros limites, que um sexto sistema pode imprimir `6 of 5`; sete tempos produzem 40 onde a mediana desse conjunto é 38; nove tempos produzem 40 onde a mediana é 42; tempos vazios geram `IndexError`; um indicador 2 pode produzir `9/8`. O limiar é estritamente maior que sessenta, e conjuntos eliminam elementos repetidos. Esses testes são separados da execução canônica; não alteram as listas, os gabaritos ou os acontecimentos do Riverbend. O código anterior não foi modificado silenciosamente.

**Fontes e proveniência:** foi consultada a [página oficial de NIST SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final), que descreve programas de aprendizagem adaptáveis e avaliação. Os quatro papéis, oito participantes, tempos, decisões de contas e prazos do caso são sintéticos, não exigências numéricas do NIST. A página oficial lista **Marian Merritt** antes dos demais autores; a autoria desta referência foi corrigida nas duas edições. A [página dos autores no arXiv](https://arxiv.org/abs/1901.02672) confirma o trabalho de Bada, Sasse e Nurse e seu resumo; esta consulta não substitui nova revisão integral dos artigos, dos livros comerciais ou da referência ABNT.

A comparação deste lote preservou dezoito objetivos, seis tabelas com 25 linhas de exemplos, seis mapas com 25 conexões, seis desenhos textuais, seis enunciados, seus quatro níveis de rubrica e seis respostas. Sete controles estruturais inválidos foram rejeitados. A igualdade da estrutura não certifica a tradução. A reconciliação integral dos quatro capítulos anteriores, a revisão humana independente, a renderização Mermaid/A4 e a leitura ao vivo do site/MCP continuam pendentes. Os rótulos truncados em diagramas antigos não foram corrigidos nesta passagem. Nenhuma ação sobre pessoas, contas, mensagens ou dinheiro reais ocorreu.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Cialdini, R. B. (2021). *Influence, new and expanded: The psychology of persuasion*. Harper Business.
- Hadnagy, C. (2018). *Social engineering: The science of human hacking* (2nd ed.). Wiley.
- Merritt, M., Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Lain, D., Kostiainen, K., & Čapkun, S. (2022). Phishing in organizations: Findings from a large-scale and long-term study. *2022 IEEE Symposium on Security and Privacy*, 842–859. <https://doi.org/10.1109/SP46214.2022.9833766>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
