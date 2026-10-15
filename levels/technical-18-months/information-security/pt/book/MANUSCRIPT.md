# Segurança da Informação: Curso Técnico

- Idioma: português do Brasil (`pt`); curso 048, curso técnico (18 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–18 de 18 têm texto didático escrito à mão; os exercícios EX001–EX072 têm resoluções correspondentes com rubricas de 0 a 3; os dois laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: estudantes de curso técnico que aprendem a apoiar a segurança da informação do dia a dia num pequeno varejista com várias unidades.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios contam, por tipo, os dispositivos sintéticos sem atualização há mais de trinta dias e pontuam e-mails sintéticos com quatro sinais de phishing, comparando com rótulos conhecidos. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de curso técnico desde a empresa, os dispositivos, as contas, as senhas, os scripts e as noções básicas de segurança, passando pelas atualizações, pelo phishing, pelos dados pessoais, pela segurança dos dados, pelas redes e pelos backups, até a comunicação de problemas, a documentação, o trabalho em equipe, um estágio, uma avaliação prática e uma revisão. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Chloe Martin** | Estudante de curso técnico | Inventada |
| **Sr. Kwesi Appiah** | Tutor | Inventado |
| **Harborview Technical College** | Escola técnica fictícia | Inventada |
| **Westfield Garden Centres** | Varejista fictício, com cinco centros, cerca de 120 funcionários e 64 dispositivos | Inventada |

### Fontes principais

ISO/IEC 27000:2026; Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Começando no Harborview

### Objetivos de aprendizagem

Você vai (1) descrever o que cobre um curso técnico em segurança da informação; (2) conhecer o caso que acompanha o livro; (3) adotar hábitos de estudo seguros.

### 1.1 A estudante

Chloe Martin começa um curso técnico de dezoito meses em segurança da informação no fictício Harborview Technical College. Seu tutor é o Sr. Kwesi Appiah, que passou anos dando suporte a computadores em lojas e escritórios antes de lecionar. Ele explica que o curso prepara os estudantes para funções de suporte em que ajudam a manter dispositivos, contas e informações seguros todos os dias. O trabalho é prático: configurar dispositivos, ajudar os usuários, identificar problemas e comunicá-los com clareza à pessoa certa. Chloe escolheu o curso porque gosta de consertar os computadores da família.

### 1.2 O local de trabalho

A parceira de estágio de Chloe é a fictícia Westfield Garden Centres, uma empresa familiar com cinco centros de jardinagem e cerca de 120 funcionários. Ela usa 22 computadores de caixa, 18 notebooks e 24 tablets para a conferência de estoque, além de uma loja on-line e de um programa de fidelidade que guarda nomes, e-mails e históricos de compra dos clientes. A Westfield tem um único responsável de TI, o Sr. Sam Doyle, que cuida de tudo com a ajuda de uma empresa de suporte. O Sr. Appiah observa que muitas pequenas empresas são assim, por isso as habilidades se aplicam amplamente. A empresa de suporte faz visitas mensais e atende chamados.

### 1.3 Como o curso funciona

Os seis primeiros capítulos cobrem a empresa, os dispositivos, as contas, as senhas, verificações simples em Python e as noções básicas de segurança. Os seis seguintes cobrem as atualizações, o phishing, os dados pessoais, a segurança dos dados, as redes sem fio e os backups. Os seis últimos cobrem a comunicação de problemas, a documentação, o trabalho com o responsável de TI, um estágio no local de trabalho, uma avaliação prática e uma revisão. Cada capítulo liga o que Chloe aprende a uma tarefa que ela pode fazer na Westfield, para que ela veja a finalidade de cada habilidade. Ela copia a lista de capítulos no caderno e marca cada um com uma tarefa da Westfield.

### 1.4 Hábitos seguros

O Sr. Appiah define três regras para o curso. Praticar apenas em equipamentos da escola ou com permissão por escrito. Usar dados sintéticos nos exercícios, nunca dados reais de clientes. Anotar o que se faz, para que você ou outra pessoa possa conferir depois. Chloe começa um caderno com a data, a tarefa e o resultado de cada sessão prática. Ela observa que esses hábitos protegem tanto a ela quanto as organizações em que vai trabalhar, porque ações descuidadas podem causar dano mesmo quando bem-intencionadas. O Sr. Appiah confere os cadernos todo mês.

### Exemplo resolvido

Chloe começa o curso, conhece os cinco centros da Westfield e seu único responsável de TI, mapeia os dezoito meses e adota três hábitos seguros.

> **Caso sintético.** O Harborview, a Westfield e todas as pessoas são sintéticos.

### Erros e limites

Praticar em sistemas reais sem permissão pode causar dano e pode ser ilegal.

### Exercícios

- **EX001 — Duração do curso.** Quanto dura o curso de Chloe? *Rubrica:* 3 = dezoito meses;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX002 — Número de dispositivos.** Quantos tablets a Westfield usa? *Rubrica:* 3 = 24;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX003 — Responsável de TI.** Quem é o responsável de TI da Westfield? *Rubrica:* 3 = o Sr. Sam Doyle;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX004 — Hábito seguro.** Cite uma das três regras do Sr. Appiah. *Rubrica:* 3 = praticar apenas com permissão;; 2 = uma;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 18)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — A informação numa rede de centros de jardinagem

### Objetivos de aprendizagem

Você vai (1) listar as informações que um pequeno varejista guarda; (2) dizer por que cada tipo precisa de proteção; (3) anotar onde cada uma fica guardada.

### 2.1 O que a Westfield guarda

Chloe lista as informações da Westfield: nomes, e-mails e históricos de compra dos membros do programa de fidelidade; pedidos da loja on-line com endereços de entrega; pagamentos com cartão nos caixas; registros e escalas dos funcionários; faturas e dados bancários dos fornecedores; e registros de estoque. O Sr. Appiah pede que ela pense em qual delas causaria mais dano se fosse perdida, alterada ou vista pela pessoa errada. Ela acha que os dados dos clientes e os dados bancários vêm primeiro, porque o uso indevido poderia causar fraude ou constrangimento a clientes e funcionários. Ela registra cada tipo de informação numa tabela simples com seus usuários.

### 2.2 Por que isso importa

Chloe aprende os três objetivos da segurança da informação: manter a informação privada, mantê-la exata e mantê-la disponível quando necessário. A ISO/IEC 27000:2026, a norma de visão geral da gestão da segurança da informação, descreve a segurança nesses termos. Na Westfield, os dados de fidelidade precisam continuar privados, os dados bancários dos fornecedores precisam continuar exatos para que os pagamentos cheguem ao lugar certo e os caixas precisam continuar disponíveis nos fins de semana movimentados. Ela escreve no caderno um exemplo da Westfield para cada objetivo. O Sr. Appiah pede que ela acrescente, para cada objetivo, um exemplo do que poderia dar errado.

### 2.3 Onde fica guardada

Chloe rastreia onde as informações ficam. Os dados de fidelidade e da loja on-line estão num serviço em nuvem. Os pagamentos com cartão passam pelos terminais de pagamento até a empresa de cartões. Os registros dos funcionários ficam num serviço de folha de pagamento. As faturas dos fornecedores chegam por e-mail e são salvas numa pasta compartilhada. As escalas são impressas e afixadas nas salas da equipe. Ela encontra uma lista impressa de entregas de clientes deixada num balcão de um centro. Ela avisa o gerente do centro, que a leva para o escritório. Ela acrescenta à tabela uma coluna de localização.

### 2.4 Quem a usa

Chloe anota quem precisa de cada tipo de informação. A equipe dos caixas precisa dos preços e das consultas de fidelidade, mas não dos registros dos funcionários. Os motoristas de entrega precisam apenas dos endereços das próprias entregas. A gerente do escritório precisa dos dados bancários dos fornecedores. O Sr. Appiah explica que saber quem precisa de quê é o ponto de partida para decidir quem deve ter acesso. Chloe vê que a pasta compartilhada da Westfield pode ser aberta por todas as contas da equipe, o que dá a muitas pessoas acesso a faturas de que elas não precisam. O Sr. Doyle concorda em restringir a pasta à equipe do escritório.

### Exemplo resolvido

Chloe lista as informações da Westfield, liga cada tipo à privacidade, à exatidão ou à disponibilidade, rastreia onde ficam guardadas e encontra uma pasta compartilhada em excesso.

> **Caso sintético.** Os tipos de informação são sintéticos.

### Erros e limites

Listas impressas de clientes deixadas nos balcões podem ser lidas por qualquer pessoa que passe.

### Exercícios

- **EX005 — Três objetivos.** Quais são os três objetivos da segurança da informação? *Rubrica:* 3 = privada, exata, disponível;; 2 = todos;; 1 = alguns;; 0 = nenhuma.

- **EX006 — Objetivo dos dados bancários.** Qual objetivo importa mais para os dados bancários dos fornecedores? *Rubrica:* 3 = exatidão;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX007 — Lista no balcão.** O que Chloe encontrou num balcão? *Rubrica:* 3 = uma lista impressa de entregas de clientes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX008 — Problema da pasta.** O que há de errado com a pasta compartilhada? *Rubrica:* 3 = todas as contas da equipe podem abri-la;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 18)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Dispositivos e contas

### Objetivos de aprendizagem

Você vai (1) criar contas de usuário com o acesso certo; (2) explicar as contas padrão e as de administrador; (3) remover o acesso quando as pessoas saem.

### 3.1 Contas de usuário

Chloe aprende que cada pessoa deve ter a própria conta, para que as ações possam ser rastreadas e o acesso corresponda ao seu trabalho. Na Westfield, os caixas usam um login compartilhado por centro. O Sr. Doyle explica que isso foi feito pela rapidez. Chloe descobre que o software dos caixas aceita, em vez disso, códigos pessoais rápidos. Ela pratica a criação de contas no laboratório da escola, dando a cada usuário apenas o acesso de que sua função precisa, e mantém uma lista das contas com seus donos. O Sr. Doyle planeja testar os códigos pessoais nos caixas de um centro no mês seguinte.

### 3.2 Contas padrão e de administrador

As contas de administrador podem instalar software e mudar configurações. As contas padrão não podem. Chloe descobre que os notebooks do escritório da Westfield usam contas de administrador no trabalho diário. Se alguém abrir um anexo nocivo, ele ganha controle total do notebook. Ela sugere contas padrão para o trabalho diário e uma conta de administrador separada, usada apenas pelo Sr. Doyle quando necessário. O Sr. Appiah explica que isso segue a ideia do menor privilégio: apenas o acesso necessário para a tarefa. O Sr. Doyle concorda e muda os notebooks um de cada vez, conferindo que cada um continua funcionando.

### 3.3 Desligamentos

Quando os funcionários saem, suas contas devem ser desativadas no último dia. A Westfield contrata funcionários extras para a primavera e o Natal. Chloe confere uma lista sintética e encontra vários temporários do ano passado com contas ainda ativas. O Sr. Doyle as desativa. Chloe sugere uma regra simples: os gerentes dos centros mandam e-mail ao Sr. Doyle no último dia de cada pessoa que sai, e ele confere a lista todo mês com os registros da folha de pagamento. As contas esquecidas são uma porta de entrada fácil para quem descobrir uma senha antiga. Chloe registra a regra.

### 3.4 Cuidados com os dispositivos

Chloe aprende os cuidados básicos com os dispositivos: bloquear a tela ao se afastar, não deixar os clientes usarem os tablets da equipe, comunicar imediatamente os dispositivos perdidos ou quebrados e não instalar aplicativos não aprovados. Ela faz uma lista de verificação curta para os novos funcionários. O Sr. Appiah observa que regras simples e claras são seguidas com mais frequência do que documentos longos e que a equipe de suporte deve explicar o motivo de cada regra, para que as pessoas entendam em vez de apenas obedecer. Ela testa a lista com dois novos funcionários de primavera, que a acham fácil de seguir, e o Sr. Doyle a acrescenta ao kit de boas-vindas.

### Exemplo resolvido

Chloe aprende o uso de contas individuais, sugere contas padrão para o uso diário dos notebooks, encontra contas de temporários esquecidas e escreve uma lista de cuidados com os dispositivos.

> **Caso sintético.** As contas são sintéticas.

### Erros e limites

Os logins compartilhados tornam impossível saber quem fez o quê.

### Exercícios

- **EX009 — Login dos caixas.** O que os caixas usam atualmente? *Rubrica:* 3 = um login compartilhado por centro;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX010 — Risco dos notebooks.** Por que as contas de administrador são arriscadas no trabalho diário? *Rubrica:* 3 = anexos nocivos ganham controle total;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX011 — Contas dos temporários.** O que Chloe encontrou sobre os temporários? *Rubrica:* 3 = contas ainda ativas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX012 — Menor privilégio.** O que significa o menor privilégio? *Rubrica:* 3 = apenas o acesso necessário para a tarefa;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 18)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Senhas e entrada nos sistemas

### Objetivos de aprendizagem

Você vai (1) explicar o que torna uma senha forte; (2) configurar a entrada com múltiplos fatores; (3) ajudar os usuários com segurança em problemas de senha.

### 4.1 Senhas fortes

Chloe aprende que senhas longas, formadas por várias palavras aleatórias, são mais fáceis de lembrar e mais difíceis de adivinhar do que senhas curtas e complexas. As senhas devem ser diferentes para cada serviço, porque os criminosos testam em muitos outros sites as senhas vazadas de um deles. Um gerenciador de senhas ajuda as pessoas a manter muitas senhas diferentes. Ela também aprende que senhas comuns, como o nome da loja seguido de um ano, estão entre as primeiras que os atacantes testam. Ela mostra aos colegas como uma frase-senha de palavras aleatórias pode ser longa e ainda fácil de digitar no teclado de um caixa.

### 4.2 Entrada com múltiplos fatores

A entrada com múltiplos fatores pede algo a mais depois da senha, como um código de um aplicativo. Mesmo que uma senha seja roubada, o atacante não consegue entrar sem o código. Chloe ajuda o Sr. Doyle a ativá-la no e-mail e na página de administração da loja on-line, começando pela equipe do escritório. Ela escreve um guia de uma página com imagens. Alguns funcionários não querem aplicativos nos celulares pessoais, por isso o Sr. Doyle fornece pequenos chaveiros geradores de código. Ela registra quem recebeu os chaveiros para que possam ser recolhidos quando os funcionários saírem.

### 4.3 Redefinição de senhas

Os funcionários às vezes esquecem as senhas. Chloe aprende que redefinir a senha para a pessoa errada é um modo comum de os atacantes entrarem. Antes de redefinir, ela precisa confirmar a identidade da pessoa, por exemplo ligando de volta para o número que consta nos registros dos funcionários, e não para um número informado na ligação. Ela pratica isso numa encenação em que um colega finge ser um gerente com pressa. Ela aprende que a pressão e a urgência são truques comuns. Ela inclui o passo da ligação de volta num breve guia de redefinição.

### 4.4 Senhas compartilhadas

Chloe descobre que a senha de administração da loja on-line está escrita num bilhete adesivo no escritório. Ela avisa o Sr. Doyle, que a troca e dá a cada pessoa que precisa de acesso o próprio login. O Sr. Appiah explica que as senhas compartilhadas se espalham com o tempo para pessoas que não deveriam tê-las, incluindo ex-funcionários, e que ninguém consegue saber quem usou um login compartilhado. Ela também confere os escritórios dos outros centros e não encontra mais bilhetes. O Sr. Doyle agradece e pede à equipe, na reunião seguinte, que não anote senhas, explicando o motivo.

### Exemplo resolvido

Chloe aprende as frases-senha e as senhas únicas, ajuda a ativar a entrada com múltiplos fatores com chaveiros como opção, pratica redefinições seguras e elimina uma senha escrita num bilhete adesivo.

> **Caso sintético.** Os exemplos são sintéticos.

### Erros e limites

Redefinir uma senha sem confirmar a identidade pode deixar um atacante entrar.

### Exercícios

- **EX013 — Perigo da reutilização.** Por que usar senhas diferentes para cada serviço? *Rubrica:* 3 = senhas vazadas são testadas em outros lugares;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX014 — Motivo dos chaveiros.** Por que são fornecidos chaveiros? *Rubrica:* 3 = alguns funcionários recusam aplicativos nos celulares pessoais;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX015 — Verificação na redefinição.** Como a identidade é confirmada antes de uma redefinição? *Rubrica:* 3 = ligação de volta para o número dos registros dos funcionários;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX016 — Bilhete adesivo.** Onde foi encontrada a senha de administração da loja? *Rubrica:* 3 = num bilhete adesivo no escritório;; 2 = parcialmente correto;; 1 = outro lugar;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 18)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Verificando configurações com Python

### Objetivos de aprendizagem

Você vai (1) escrever um script curto em Python; (2) ler um arquivo CSV com informações de dispositivos; (3) imprimir uma lista clara de problemas.

### 5.1 Por que os scripts ajudam

Conferir sessenta e quatro dispositivos à mão leva horas, e é fácil errar. Chloe aprende a escrever scripts curtos em Python usando apenas a biblioteca padrão. Seu primeiro script lê um arquivo CSV que lista cada dispositivo com seu tipo, seu centro e a data da última atualização e imprime quantos dispositivos há de cada tipo. O Sr. Appiah explica que mesmo poucas linhas de código podem poupar tempo e tornar as verificações repetíveis, de modo que a mesma verificação dê a mesma resposta toda semana. Ela executa o script todas as semanas.

### 5.2 Leitura dos dados

Chloe usa o módulo csv para ler o arquivo uma linha por vez. Ela aprende a tratar as linhas com valores ausentes imprimindo um aviso em vez de deixar o script parar. Ela testa o script com um arquivo que contém um erro deliberado. O Sr. Appiah lembra que os dados reais sempre contêm erros, por isso um bom script avisa sobre as linhas ruins em vez de pulá-las em silêncio. Seu arquivo de teste tem três erros deliberados, e o script avisa sobre os três com o número da linha, para que ela saiba exatamente onde olhar.

### 5.3 Resultados claros

O script de Chloe imprime um título, a data, o número de dispositivos conferidos e uma lista dos dispositivos que precisam de atenção, agrupados por centro. Ela salva a lista num novo arquivo CSV para que o Sr. Doyle possa abri-lo numa planilha. O Sr. Appiah pede que ela explique cada linha da saída a um colega. Se o colega entender, a saída está clara o bastante para um responsável de TI ocupado. O Sr. Doyle abre o arquivo salvo e diz que é exatamente o que ele precisa para planejar as visitas a cada centro.

### 5.4 Scripts seguros

Chloe guarda seus scripts numa pasta do sistema da escola, acrescenta comentários explicando o que cada parte faz e nunca coloca senhas num script. Os arquivos de saída que listam dispositivos ficam numa pasta restrita, porque uma lista de dispositivos fracos poderia ajudar um atacante. Ela aprende que as próprias ferramentas de verificação de segurança precisam ser tratadas com cuidado. Ela também escreve uma breve nota no topo de cada script explicando o que ele verifica e de que arquivo precisa. O Sr. Appiah diz que essas notas vão ajudar qualquer pessoa que use os scripts depois, inclusive a própria Chloe daqui a alguns meses.

### Exemplo resolvido

Chloe escreve um script com a biblioteca padrão que lê dados de dispositivos, avisa sobre linhas ruins, imprime uma lista clara por centro e mantém seguros os scripts e as saídas.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Scripts que pulam em silêncio as linhas ruins podem esconder problemas.

### Exercícios

- **EX017 — Primeira contagem.** O que o primeiro script conta? *Rubrica:* 3 = os dispositivos de cada tipo;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX018 — Valores ausentes.** Como o script trata os valores ausentes? *Rubrica:* 3 = imprime um aviso;; 2 = parcialmente correto;; 1 = parar;; 0 = nenhuma.

- **EX019 — Teste da saída.** Como Chloe testa a clareza da saída? *Rubrica:* 3 = explica-a a um colega;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX020 — Saída restrita.** Por que manter restritas as listas de dispositivos? *Rubrica:* 3 = poderiam ajudar um atacante;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — aula 05 (capítulo 05 de 18)

[← Capítulo 04](#ch-04) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Noções básicas de segurança

### Objetivos de aprendizagem

Você vai (1) explicar ameaças, fraquezas e riscos; (2) dar exemplos de controles; (3) explicar a proteção em camadas.

### 6.1 Ameaças e fraquezas

Uma ameaça é algo que poderia causar dano, como um criminoso que envia e-mails falsos. Uma fraqueza é uma brecha que uma ameaça poderia usar, como uma senha num bilhete adesivo. O risco é a chance de o dano acontecer e o quanto ele seria grave. Chloe lista as ameaças à Westfield: e-mails falsos, tablets furtados, fraude com cartões nos caixas e erros como enviar listas de clientes à pessoa errada. Ela acrescenta no caderno uma fraqueza e um possível dano ao lado de cada ameaça, para que a lista se torne uma tabela de riscos simples.

### 6.2 Controles

Os controles reduzem o risco. Alguns evitam problemas, como a entrada com múltiplos fatores. Alguns detectam problemas, como os alertas de logins incomuns. Alguns ajudam na recuperação, como os backups. Chloe associa um controle a cada ameaça da lista. Para os tablets furtados, ela sugere o bloqueio de tela e a possibilidade de apagá-los remotamente. O Sr. Appiah explica que os controles devem corresponder aos riscos reais, e não apenas seguir uma lista. Ela mostra a lista ao Sr. Doyle, que acrescenta uma ameaça que ela deixou passar: a conta de suporte de um fornecedor com acesso aos caixas. Chloe acrescenta um controle também para ela.

### 6.3 Camadas

Nenhum controle é perfeito. Chloe aprende a pensar em camadas. Para a loja on-line, as camadas incluem senhas fortes, a entrada com múltiplos fatores, a limitação de quem tem acesso de administração, a atualização do software e a observação de pedidos incomuns. Se uma camada falhar, as outras continuam protegendo. O Sr. Appiah observa que essa abordagem em camadas é usada em toda a segurança, das pequenas lojas às grandes empresas. Chloe desenha as camadas num diagrama simples, com a loja on-line no meio e cada controle como um anel em volta dela. O Sr. Appiah pergunta qual anel seria esquecido primeiro se o Sr. Doyle ficasse duas semanas fora.

### 6.4 Pessoas e processos

A segurança não é só tecnologia. Chloe vê que os maiores riscos da Westfield envolvem pessoas: funcionários que clicam em links falsos, gerentes que enviam dados ao endereço errado e fornecedores que mudam dados bancários por e-mail. Ela aprende que processos claros, como conferir por telefone as mudanças de dados bancários, protegem contra esses riscos. O artigo de Saltzer e Schroeder de 1975 sobre a proteção da informação descreveu a aceitabilidade psicológica: a segurança precisa ser fácil o bastante para que as pessoas a usem corretamente. Chloe anota três processos da Westfield que protegem contra os riscos ligados a pessoas e os mostra ao Sr. Doyle, que confirma que já são usados.

### Exemplo resolvido

Chloe define ameaças, fraquezas e risco, associa controles às ameaças da Westfield, monta camadas para a loja on-line e reconhece os riscos ligados a pessoas e processos.

> **Caso sintético.** Os exemplos são sintéticos.

### Erros e limites

Depender de um único controle não deixa proteção alguma quando ele falha.

### Exercícios

- **EX021 — Exemplo de fraqueza.** Dê um exemplo de fraqueza. *Rubrica:* 3 = uma senha num bilhete adesivo;; 2 = um;; 1 = vago;; 0 = nenhuma.

- **EX022 — Controles para tablets.** Quais controles servem para tablets furtados? *Rubrica:* 3 = bloqueio de tela e apagamento remoto;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX023 — Camada da loja.** Cite uma camada da loja on-line. *Rubrica:* 3 = entrada com múltiplos fatores;; 2 = uma;; 1 = vago;; 0 = nenhuma.

- **EX024 — Princípio da usabilidade.** Que princípio diz que a segurança precisa ser fácil de usar? *Rubrica:* 3 = aceitabilidade psicológica;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — aula 06 (capítulo 06 de 18)

[← Capítulo 05](#ch-05) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Atualizações na loja

### Objetivos de aprendizagem

Você vai (1) explicar por que as atualizações importam; (2) encontrar os dispositivos que perderam atualizações; (3) ajudar a corrigir problemas de atualização.

### 7.1 Por que as atualizações importam

Os fabricantes de software lançam atualizações para corrigir fraquezas de segurança. Os criminosos estudam essas correções e miram os dispositivos que não as instalaram. Chloe aprende que manter os dispositivos atualizados é uma das proteções mais simples e eficazes. Na Westfield, os caixas são atualizados pelo fornecedor dos caixas, os notebooks por atualizações automáticas e os tablets por seus usuários quando recebem o aviso. O Sr. Doyle suspeita que os tablets estejam atrasados, porque a equipe muitas vezes dispensa as mensagens de atualização durante a conferência do estoque. O Sr. Doyle pede a Chloe que confira as datas de atualização de todos os dispositivos.

### 7.2 O laboratório das atualizações

O laboratório lê dados sintéticos dos 64 dispositivos da Westfield e conta os que não são atualizados há mais de trinta dias. Nenhum dos 22 caixas está atrasado, 2 dos 18 notebooks estão atrasados, 11,1 por cento, e 4 dos 24 tablets estão atrasados, 16,7 por cento. No total, 6 de 64 dispositivos precisam de atenção. Chloe observa que a suspeita do Sr. Doyle se confirma: os tablets têm a maior parcela de atualizações atrasadas, embora alguns notebooks também estejam para trás. Ela mostra os resultados ao Sr. Doyle numa tabela curta, com cada dispositivo atrasado listado por centro, para que ele possa planejar quais centros visitar primeiro. Ele concorda que os tablets precisam de atenção.

### Laboratório — Dispositivos sem atualização há mais de trinta dias, por tipo de dispositivo

```python
"""Find synthetic devices with no update for more than 30 days, by device type (stdlib only)."""
import random
from collections import Counter
random.seed(18)
devices = []
for kind, n, mean in [("till", 22, 9), ("laptop", 18, 14), ("tablet", 24, 26)]:
    for i in range(n):
        devices.append((kind, int(random.expovariate(1 / mean))))
total = Counter(k for k, _ in devices)
late = Counter(k for k, d in devices if d > 30)
for k in total:
    print(f"{k}: {late[k]} of {total[k]} not updated for over 30 days ({late[k]/total[k]:.1%})")
print(f"all devices: {sum(late.values())} of {len(devices)}")
```

Execute com `python3 lab_updates.py`. Saída verificada:

```text
till: 0 of 22 not updated for over 30 days (0.0%)
laptop: 2 of 18 not updated for over 30 days (11.1%)
tablet: 4 of 24 not updated for over 30 days (16.7%)
all devices: 6 of 64
```

### 7.3 Encontrar as causas

Chloe visita dois centros e confere os tablets atrasados. Dois ficaram semanas numa gaveta como reserva, por isso nunca se conectaram para instalar as atualizações. Um tem pouco espaço livre para a atualização. Um pertence a um gerente que vive adiando as reinicializações. Os dois notebooks atrasados são usados apenas de vez em quando. Ela aprende que causas diferentes exigem correções diferentes e que encontrar a causa é mais rápido do que adivinhar. Ela registra cada causa ao lado do dispositivo no caderno, junto com a data em que o conferiu e a pessoa com quem falou.

### 7.4 Correção

Chloe carrega e atualiza os tablets de reserva e depois cria um lembrete mensal para que os gerentes dos centros liguem os aparelhos de reserva. Ela libera espaço no tablet cheio removendo fotos antigas depois de conferir com o usuário. O Sr. Doyle configura os tablets para instalar as atualizações automaticamente durante a noite, enquanto carregam. Os notebooks de uso ocasional são agendados para atualização no início de cada mês. Ela repete a verificação uma semana depois e encontra os seis dispositivos atualizados. O Sr. Doyle agradece a ela por conferir que a correção funcionou.

### Exemplo resolvido

Chloe encontra 6 de 64 dispositivos sintéticos sem atualização há mais de trinta dias (tablets 16,7 por cento, notebooks 11,1 por cento, caixas nenhum), descobre as causas e corrige cada uma.

> **Caso sintético.** Os dispositivos são sintéticos; as saídas vêm de lab_updates.py.

### Erros e limites

Os dispositivos de reserva mantidos desligados perdem as atualizações sem que ninguém perceba.

### Exercícios

- **EX025 — Tablets atrasados.** Quantos tablets estão atrasados? *Rubrica:* 3 = 4 de 24, 16,7 por cento;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX026 — Caixas atrasados.** Quantos caixas estão atrasados? *Rubrica:* 3 = nenhum dos 22 caixas;; 2 = nenhum, sem conferir os 22;; 1 = errado;; 0 = sem resposta.

- **EX027 — Tablets de reserva.** Por que dois tablets estavam atrasados? *Rubrica:* 3 = ficavam numa gaveta como reserva;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX028 — Configuração noturna.** Que configuração o Sr. Doyle muda nos tablets? *Rubrica:* 3 = atualizações automáticas à noite durante a carga;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — aula 07 (capítulo 07 de 18)

[← Capítulo 06](#ch-06) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Identificando o phishing

### Objetivos de aprendizagem

Você vai (1) reconhecer os sinais comuns de phishing; (2) testar uma regra simples de pontuação; (3) explicar por que as regras deixam passar algumas mensagens.

### 8.1 Sinais de phishing

Os e-mails de phishing tentam induzir as pessoas a clicar num link nocivo, abrir um anexo ou entregar informações. Chloe aprende quatro sinais comuns: o endereço do remetente não corresponde à organização que ele alega ser, a mensagem usa palavras urgentes, como imediatamente ou conta suspensa, o endereço real de um link difere do texto mostrado e há um anexo inesperado. O Sr. Appiah avisa que os atacantes cuidadosos evitam alguns desses sinais, por isso nenhum deles é garantia. Ela escreve os quatro sinais num cartão.

### 8.2 O laboratório do phishing

O laboratório pontua 40 e-mails sintéticos, 12 sabidamente de phishing e 28 genuínos, contando quantos dos quatro sinais cada um mostra. As mensagens com dois ou mais sinais são sinalizadas. A regra pega 11 dos 12 e-mails de phishing e deixa passar um. Ela também sinaliza 3 e-mails genuínos como alarmes falsos. Chloe examina a mensagem que passou e descobre que ela mostrava apenas um sinal, um endereço de remetente que não correspondia, sem palavras urgentes, link estranho ou anexo. Ela mostra o resultado ao Sr. Appiah, que observa que uma regra que olha apenas quatro sinais sempre vai deixar passar algumas mensagens, porque os atacantes podem mudar seus métodos para evitá-los.

### Laboratório — Pontuando e-mails sintéticos com quatro sinais de phishing e comparando com rótulos conhecidos

```python
"""Score synthetic emails with four simple phishing indicators and compare with known labels (stdlib only)."""
import random
random.seed(3)
msgs = []
for i in range(40):
    phish = i < 12
    f = {
        "sender_mismatch": random.random() < (0.75 if phish else 0.05),
        "urgent_words": random.random() < (0.8 if phish else 0.15),
        "link_mismatch": random.random() < (0.7 if phish else 0.03),
        "unexpected_attachment": random.random() < (0.4 if phish else 0.1),
    }
    msgs.append((phish, sum(f.values()), [k for k, v in f.items() if v]))
tp = sum(p and s >= 2 for p, s, _ in msgs); fn = sum(p and s < 2 for p, s, _ in msgs)
fp = sum((not p) and s >= 2 for p, s, _ in msgs); tn = sum((not p) and s < 2 for p, s, _ in msgs)
print(f"messages {len(msgs)}; phishing {tp+fn}; genuine {fp+tn}")
print(f"flagged (score >= 2): caught {tp}, missed {fn}, false alarms {fp}")
print("signs on missed phishing:", [k for p, s, k in msgs if p and s < 2])
```

Execute com `python3 lab_phish.py`. Saída verificada:

```text
messages 40; phishing 12; genuine 28
flagged (score >= 2): caught 11, missed 1, false alarms 3
signs on missed phishing: [['sender_mismatch']]
```

### 8.3 Por que as regras falham

Chloe aprende que qualquer regra simples comete dois tipos de erro. Ela deixa passar parte do phishing e sinaliza algumas mensagens genuínas. Baixar o limiar para um sinal pegaria mais phishing, mas criaria muito mais alarmes falsos, como e-mails genuínos de fornecedores marcados como urgentes. Subi-lo deixaria passar mais phishing. O Sr. Appiah explica que as regras ajudam as pessoas a concentrar a atenção, mas o julgamento da equipe e um meio de comunicar as dúvidas continuam necessários. Ela testa no papel o limiar de um sinal com as mesmas mensagens e vê os alarmes falsos subirem, o que a ajuda a entender esse equilíbrio.

### 8.4 O que a equipe deve fazer

Chloe escreve uma orientação simples para a equipe da Westfield: se um e-mail mostrar qualquer um dos quatro sinais, não clique; confirme entrando em contato com o remetente por outro meio; e comunique-o ao Sr. Doyle pelo botão de comunicação do programa de e-mail. Ela também explica que comunicar um e-mail genuíno por engano não tem problema. O Sr. Doyle prefere dez comunicações desnecessárias a um e-mail de phishing que passe. A equipe reage bem à mensagem clara e sem culpa. Ela imprime a orientação num pequeno cartão para cada caixa e cada mesa de escritório. O Sr. Doyle recebe mais comunicações no mês seguinte.

### Exemplo resolvido

Chloe aprende quatro sinais de phishing, descobre que uma regra de dois sinais pega 11 de 12 e-mails sintéticos de phishing com 3 alarmes falsos e escreve uma orientação sem culpa para a equipe.

> **Caso sintético.** Os e-mails são sintéticos; as saídas vêm de lab_phish.py.

### Erros e limites

Tratar uma regra simples como perfeita leva as pessoas a confiar nas mensagens que ela deixa passar.

### Exercícios

- **EX029 — Número pego.** Quantos e-mails de phishing a regra pega? *Rubrica:* 3 = 11 de 12;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX030 — Alarmes falsos.** Quantos e-mails genuínos são sinalizados? *Rubrica:* 3 = três;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX031 — Mensagem que passou.** Por que um e-mail de phishing passou? *Rubrica:* 3 = mostrava apenas um sinal;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX032 — Limiar mais baixo.** O que acontece se o limiar cair para um sinal? *Rubrica:* 3 = mais alarmes falsos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — aula 08 (capítulo 08 de 18)

[← Capítulo 07](#ch-07) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Dados pessoais no trabalho

### Objetivos de aprendizagem

Você vai (1) reconhecer os dados pessoais; (2) tratar com cuidado os dados dos clientes; (3) responder às perguntas dos clientes sobre seus dados.

### 9.1 O que são dados pessoais

Dados pessoais são qualquer informação sobre uma pessoa identificável: nomes, e-mails, endereços, números de telefone, históricos de compra e fotos. Chloe aprende que as leis de proteção de dados de muitos países exigem que as organizações usem os dados pessoais de forma justa, os mantenham seguros e os guardem apenas pelo tempo necessário. A Westfield guarda dados pessoais dos membros do programa de fidelidade, dos clientes on-line e dos funcionários. O Sr. Appiah explica que as regras exatas dependem do país, por isso a equipe deve seguir a política de sua organização. Ela lista na tabela do caderno os dados pessoais que a Westfield guarda.

### 9.2 Tratamento cuidadoso

Chloe vê exemplos de tratamento descuidado na Westfield: uma lista de entregas enviada por e-mail a um endereço pessoal para que um motorista pudesse lê-la no celular, e os detalhes do pedido de um cliente lidos em voz alta num caixa movimentado. Ela sugere um aplicativo de entregas que mostre a cada motorista apenas as próprias entregas e pedir aos clientes que confiram os dados na tela do caixa. Ela aprende que pequenos hábitos protegem os clientes tanto quanto os controles técnicos. Os gerentes dos centros concordam em testar as duas ideias, e o Sr. Doyle verifica se o aplicativo de entregas pode limitar o que cada motorista vê.

### 9.3 Perguntas dos clientes

Os clientes às vezes perguntam que dados a Westfield guarda sobre eles ou pedem para sair do programa de fidelidade. Chloe aprende que a equipe não deve responder a essas perguntas na hora, mas encaminhá-las à gerente do escritório, que segue o processo adequado. Isso evita erros e confirma que a pessoa que pergunta é de fato o cliente. Ela escreve uma breve nota para a equipe dos caixas explicando o que dizer e a quem recorrer. O Sr. Doyle e a gerente do escritório aprovam a nota, que é afixada ao lado de cada caixa. A equipe diz que ela ajuda a se sentir segura quando os clientes perguntam.

### 9.4 Erros

Erros acontecem. Se um e-mail com dados de clientes for para a pessoa errada, a equipe deve comunicá-lo imediatamente, e não escondê-lo. Chloe aprende que a comunicação rápida permite à Westfield pedir ao destinatário que o apague e decidir se alguém precisa ser informado. O Sr. Appiah insiste que culpar as pessoas por erros honestos as leva a esconder os próximos, o que é pior para todos. Chloe pratica os passos da comunicação numa encenação com um colega que enviou uma lista de clientes ao fornecedor errado. Ela observa como o problema pode ser contido muito mais depressa quando quem enviou o comunica na hora, em vez de esperar para ver se alguém percebe.

### Exemplo resolvido

Chloe identifica os dados pessoais, sugere listas de entrega e conferências nos caixas mais seguras, encaminha os pedidos dos clientes à gerente do escritório e incentiva a comunicação rápida dos erros.

> **Caso sintético.** Os exemplos são sintéticos; as leis variam de país para país.

### Erros e limites

Esconder um erro com dados impede a organização de limitar o dano.

### Exercícios

- **EX033 — Exemplo de dado pessoal.** Dê um exemplo de dado pessoal. *Rubrica:* 3 = o endereço de e-mail de um cliente;; 2 = um;; 1 = vago;; 0 = nenhuma.

- **EX034 — Solução para os motoristas.** O que Chloe sugere para os motoristas? *Rubrica:* 3 = um aplicativo que mostre apenas as próprias entregas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX035 — Tratamento dos pedidos.** Quem trata os pedidos dos clientes sobre seus dados? *Rubrica:* 3 = a gerente do escritório;; 2 = parcialmente correto;; 1 = o caixa;; 0 = nenhuma.

- **EX036 — Resposta ao erro.** O que a equipe deve fazer depois de um e-mail enviado ao destinatário errado? *Rubrica:* 3 = comunicá-lo imediatamente;; 2 = parcialmente correto;; 1 = escondê-lo;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue estudando — aula 09 (capítulo 09 de 18)

[← Capítulo 08](#ch-08) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Mantendo os dados seguros

### Objetivos de aprendizagem

Você vai (1) proteger os dados nos dispositivos e nas pastas; (2) usar a criptografia onde for necessária; (3) compartilhar arquivos com segurança.

### 10.1 Pastas e permissões

Chloe ajuda o Sr. Doyle a organizar as pastas compartilhadas da Westfield. Ela lista cada pasta com quem precisa de acesso. As faturas dos fornecedores vão apenas para a equipe do escritório; as escalas, para os gerentes; as imagens de marketing, para todos. O Sr. Doyle ajusta as permissões de acordo. Chloe confere depois, entrando com uma conta de teste de caixa e confirmando que ela não consegue abrir a pasta das faturas. Ela aprende a conferir que uma mudança funcionou em vez de presumir que funcionou. Ela registra cada pasta, suas novas permissões e a data do teste, para que o Sr. Doyle tenha um registro claro caso alguém pergunte.

### 10.2 Criptografia

A criptografia embaralha os dados para que apenas quem tem a chave consiga lê-los. Chloe verifica que os notebooks da Westfield usam criptografia de disco completo, para que um notebook furtado não exponha dados. Dois notebooks mais antigos não estão criptografados. O Sr. Doyle ativa a criptografia e guarda as chaves de recuperação com segurança. Chloe também verifica que a loja on-line usa uma conexão criptografada, indicada pelo cadeado no navegador. Ela aprende que a criptografia protege os dados se um dispositivo for perdido. Ela registra na lista de dispositivos quais notebooks estão criptografados.

### 10.3 Compartilhamento de arquivos

Os funcionários às vezes precisam enviar arquivos a fornecedores ou contadores. Chloe descobre que alguns usam e-mail pessoal ou sites gratuitos de compartilhamento de arquivos. Ela recomenda usar o serviço de compartilhamento aprovado da Westfield, com links que expiram e exigem que o destinatário entre com login. Ela escreve um guia curto. O Sr. Appiah explica que as ferramentas aprovadas mantêm as cópias sob o controle da organização e permitem remover o acesso depois. O Sr. Doyle envia o guia a toda a equipe do escritório com uma breve explicação e pede que parem de usar o e-mail pessoal para arquivos de trabalho. Chloe se oferece para ajudar quem achar o serviço difícil.

### 10.4 Mesas e telas limpas

Chloe percebe papéis com dados de clientes deixados nas mesas do escritório e telas deixadas desbloqueadas. Ela sugere uma rotina simples: bloquear a tela ao sair da mesa e guardar os papéis numa gaveta trancada no fim do dia. Ela ajuda a configurar as telas para bloquearem automaticamente depois de alguns minutos. Pequenas rotinas como essas reduzem a chance de as informações serem vistas por visitantes ou clientes. Ela confere o escritório de novo duas semanas depois e encontra as mesas limpas e as telas bloqueadas. A gerente do escritório diz que a rotina leva só um minuto no fim de cada dia.

### Exemplo resolvido

Chloe ajusta o acesso às pastas conforme a necessidade e o testa, encontra dois notebooks sem criptografia, recomenda um serviço de compartilhamento aprovado e promove mesas e telas limpas.

> **Caso sintético.** Os exemplos são sintéticos.

### Erros e limites

Presumir que uma mudança de permissão funcionou sem testá-la pode deixar dados expostos.

### Exercícios

- **EX037 — Conta de teste.** Como Chloe confirma a mudança na pasta? *Rubrica:* 3 = entrando com uma conta de teste de caixa;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX038 — Notebooks sem criptografia.** Quantos notebooks não estavam criptografados? *Rubrica:* 3 = dois;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX039 — Serviço de compartilhamento.** O que Chloe recomenda para enviar arquivos? *Rubrica:* 3 = o serviço aprovado com links que expiram;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX040 — Configuração da tela.** Que configuração ajuda com as telas desbloqueadas? *Rubrica:* 3 = bloqueio automático depois de alguns minutos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue estudando — aula 10 (capítulo 10 de 18)

[← Capítulo 09](#ch-09) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Noções básicas de redes sem fio e de rede

### Objetivos de aprendizagem

Você vai (1) descrever a rede de uma pequena empresa; (2) separar as redes sem fio de visitantes e da equipe; (3) identificar dispositivos desconhecidos.

### 11.1 A rede

Chloe desenha a rede de um centro da Westfield: um roteador de internet, um switch, os caixas, o notebook do escritório, os tablets da equipe, uma rede sem fio de visitantes para os clientes do café e as câmeras. O Sr. Appiah pede que ela identifique quais dispositivos lidam com pagamentos com cartão, porque esses precisam de mais proteção. Ela marca os caixas e os terminais de pagamento. Ela também marca a rede sem fio de visitantes e as câmeras e lista cada dispositivo com sua localização. O Sr. Doyle confere o diagrama com a lista de dispositivos conectados do roteador e o considera completo, exceto por uma impressora, que ela acrescenta. Ele guarda uma cópia do diagrama para a empresa de suporte.

### 11.2 Redes sem fio de visitantes e da equipe

Os clientes usam a rede sem fio gratuita de visitantes no café. Chloe verifica que a rede de visitantes está separada da rede da equipe, para que o dispositivo de um cliente não alcance os caixas nem os tablets. Num centro, a rede de visitantes usa a mesma senha da rede sem fio da equipe, e as duas se conectam à mesma rede. O Sr. Doyle as separa e troca as senhas. Chloe testa a separação a partir de um notebook da escola conectado à rede de visitantes. O teste confirma que a rede de visitantes não alcança mais nenhum dispositivo da equipe.

### 11.3 Dispositivos desconhecidos

Chloe examina a lista de dispositivos conectados ao roteador de um centro, com a permissão do Sr. Doyle. Ela encontra um dispositivo que não consegue identificar. O Sr. Doyle descobre que é uma caixa de som inteligente que um funcionário trouxe para ouvir música. Ela estava conectada à rede da equipe. Ele a passa para a rede de visitantes. Chloe aprende que dispositivos desconhecidos nas redes da equipe devem sempre ser verificados. Ela sugere uma verificação mensal dos dispositivos conectados em cada centro, e o Sr. Doyle concorda em fazê-la durante as visitas regulares. Ele também lembra a equipe de perguntar antes de conectar dispositivos pessoais.

### 11.4 Configurações do roteador

Chloe confere as configurações do roteador com o Sr. Doyle: a senha de administrador foi trocada em relação à padrão, a administração remota pela internet está desligada e o software do roteador está atualizado. O roteador de um centro ainda tem a senha padrão. O Sr. Doyle a troca. O Sr. Appiah explica que as senhas padrão são publicadas na internet e estão entre as primeiras coisas que os atacantes testam. Chloe registra as configurações de cada roteador nas notas de rede, e o Sr. Doyle confere os outros centros e confirma que seus roteadores estão seguros. Ele planeja conferir as configurações de novo depois de qualquer atualização de software.

### Exemplo resolvido

Chloe desenha a rede de um centro, encontra as redes sem fio de visitantes e da equipe compartilhando rede e senha, identifica a caixa de som inteligente de um funcionário e encontra um roteador com senha padrão.

> **Caso sintético.** As redes são sintéticas.

### Erros e limites

Dispositivos de visitantes na rede da equipe podem alcançar os caixas e os tablets.

### Exercícios

- **EX041 — Dispositivos de pagamento.** Quais dispositivos lidam com pagamentos com cartão? *Rubrica:* 3 = caixas e terminais de pagamento;; 2 = parcialmente correto;; 1 = outros;; 0 = nenhuma.

- **EX042 — Problema da rede sem fio.** O que estava errado num centro? *Rubrica:* 3 = visitantes e equipe compartilhavam rede e senha;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX043 — Dispositivo desconhecido.** Qual era o dispositivo desconhecido? *Rubrica:* 3 = a caixa de som inteligente de um funcionário;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX044 — Senha padrão do roteador.** Por que trocar as senhas padrão dos roteadores? *Rubrica:* 3 = são publicadas na internet;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue estudando — aula 11 (capítulo 11 de 18)

[← Capítulo 10](#ch-10) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Backups e recuperação

### Objetivos de aprendizagem

Você vai (1) explicar por que os backups importam; (2) verificar que os backups funcionam; (3) saber o que fazer quando dados são perdidos.

### 12.1 Por que os backups importam

Os backups são cópias dos dados guardadas para que possam ser restauradas depois de um erro, de uma falha de dispositivo ou de um ataque como o ransomware, que bloqueia os arquivos e exige pagamento. Chloe aprende que um bom backup é guardado separado do original, para que um único problema não destrua os dois. Os dados da loja on-line e do programa de fidelidade da Westfield têm backup feito pelo provedor de nuvem. Os arquivos do escritório têm backup toda noite num serviço em nuvem. O Sr. Doyle confirma que os backups rodam todas as noites e guardam cópias por trinta dias.

### 12.2 Teste dos backups

Um backup só é útil se puder ser restaurado. Chloe pergunta ao Sr. Doyle quando uma restauração foi testada pela última vez. Ele não tem certeza. Juntos, eles restauram uma pasta de amostra do backup em nuvem num notebook de teste e comparam os arquivos com os originais. Todos os arquivos abrem corretamente. Chloe registra o teste com a data, a pasta e o resultado e sugere repeti-lo a cada três meses. O Sr. Doyle acrescenta o teste trimestral ao calendário. Chloe observa que foi a primeira vez que alguém conferiu que o backup realmente funcionava.

### 12.3 Lacunas

Chloe confere o que não tem backup. A gerente do escritório guarda algumas planilhas na área de trabalho do notebook, fora das pastas com backup. Os tablets guardam fotos da conferência de estoque que não têm backup, mas não são necessárias depois que o estoque é atualizado. Chloe ajuda a gerente do escritório a mover as planilhas para a pasta com backup. Ela aprende que as pessoas muitas vezes salvam arquivos em lugares convenientes fora dos backups. A gerente do escritório concorda em salvar os novos arquivos na pasta com backup daqui em diante. Chloe confere os outros notebooks do escritório e não encontra outros arquivos fora dos backups.

### 12.4 Quando dados são perdidos

Chloe escreve passos simples para os funcionários que perdem um arquivo ou suspeitam de ransomware: parar de usar o dispositivo, não tentar consertá-lo por conta própria, ligar para o Sr. Doyle e anotar o que aconteceu. Ela aprende que comunicar rápido e não fazer alterações ajuda na recuperação. O Sr. Appiah explica que tentativas bem-intencionadas de consertar as coisas às vezes espalham o problema ou destroem as evidências do que aconteceu. Ela imprime os passos num cartão para cada escritório e cada caixa. O Sr. Doyle acrescenta seu telefone e o da empresa de suporte, para que a equipe consiga falar com alguém mesmo quando ele estiver fora.

### Exemplo resolvido

Chloe aprende por que os backups separados importam, testa uma restauração com o Sr. Doyle, move planilhas para pastas com backup e escreve passos para a perda de dados ou o ransomware.

> **Caso sintético.** Os backups são sintéticos.

### Erros e limites

Os arquivos salvos fora das pastas com backup se perdem se o dispositivo falhar.

### Exercícios

- **EX045 — Significado de ransomware.** O que o ransomware faz? *Rubrica:* 3 = bloqueia os arquivos e exige pagamento;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX046 — Frequência dos testes.** Com que frequência as restaurações devem ser testadas? *Rubrica:* 3 = a cada três meses;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX047 — Lacuna no backup.** Quais arquivos estavam fora dos backups? *Rubrica:* 3 = planilhas na área de trabalho da gerente do escritório;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX048 — Primeiro passo.** Qual é o primeiro passo se houver suspeita de ransomware? *Rubrica:* 3 = parar de usar o dispositivo;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue estudando — aula 12 (capítulo 12 de 18)

[← Capítulo 11](#ch-11) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Comunicando problemas

### Objetivos de aprendizagem

Você vai (1) reconhecer os problemas de segurança que precisam ser comunicados; (2) escrever uma comunicação de problema clara; (3) acompanhar até o problema ser encerrado.

### 13.1 O que comunicar

Chloe aprende que a equipe de suporte muitas vezes percebe os problemas primeiro: um e-mail suspeito, um dispositivo com comportamento estranho, uma porta deixada destrancada ou uma lista de clientes no lugar errado. O Sr. Appiah explica que comunicar cedo permite que a pessoa certa aja antes que o dano cresça. Na Westfield, os problemas vão para o Sr. Doyle por e-mail ou telefone, ou para a empresa de suporte se ele estiver fora. Chloe anota os contatos na contracapa do caderno para tê-los sempre à mão. Ela também salva os dois números no celular.

### 13.2 Uma comunicação clara

Uma boa comunicação diz o que foi visto, onde, quando, quem é afetado e o que já foi feito. Chloe pratica escrever comunicações a partir de cenários. Seu primeiro rascunho diz que um notebook está estranho. O Sr. Appiah pergunta o que exatamente aconteceu. Ela o reescreve: às 10h15 de terça-feira, o notebook do escritório do centro norte mostrou uma mensagem exigindo pagamento, e a usuária o desligou e ligou para ela. O detalhe ajuda quem recebe a comunicação a agir depressa. O Sr. Appiah avalia a comunicação reescrita como clara e útil.

### 13.3 Uma comunicação real

Durante o estágio, uma funcionária do caixa conta a Chloe que um cliente pediu para ligar o celular num caixa para carregá-lo. A funcionária recusou, mas o cliente insistiu. Chloe comunica o fato ao Sr. Doyle com o horário, o centro e uma descrição. O Sr. Doyle confere as portas do caixa e coloca tampas nas que não são usadas. Ele agradece à funcionária do caixa e a Chloe. Ela aprende que as comunicações sobre tentativas que falharam continuam valiosas. Chloe acrescenta o evento à sua lista de comunicações, com a data e o desfecho.

### 13.4 Acompanhamento

As comunicações não devem ser esquecidas depois de enviadas. Chloe mantém uma lista simples das comunicações que fez, com a data e a situação atual. Ela confere com o Sr. Doyle toda semana até que cada uma seja encerrada. Uma comunicação sobre uma câmera quebrada fica parada por duas semanas, até que ela o lembre. O Sr. Appiah observa que acompanhar com educação faz parte do trabalho, porque pessoas ocupadas às vezes perdem de vista os problemas menores. A câmera é consertada na semana seguinte, e Chloe marca a comunicação como encerrada, com a data. Sua lista agora mostra cada comunicação e seu desfecho.

### Exemplo resolvido

Chloe aprende o que comunicar, reescreve uma comunicação vaga com horário, local e detalhes, comunica um pedido suspeito de carregar um celular num caixa e acompanha as comunicações até o encerramento.

> **Caso sintético.** As comunicações são sintéticas.

### Erros e limites

Comunicações vagas atrasam as pessoas que precisam agir com base nelas.

### Exercícios

- **EX049 — Conteúdo da comunicação.** O que uma boa comunicação deve incluir? *Rubrica:* 3 = o quê, onde, quando, quem é afetado, ações tomadas;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.

- **EX050 — Comunicação reescrita.** Que detalhes Chloe acrescentou? *Rubrica:* 3 = horário, centro e mensagem de pagamento;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX051 — Pedido no caixa.** O que um cliente pediu para fazer? *Rubrica:* 3 = ligar um celular num caixa;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX052 — Acompanhamento.** Com que frequência Chloe confere as comunicações abertas? *Rubrica:* 3 = toda semana;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue estudando — aula 13 (capítulo 13 de 18)

[← Capítulo 12](#ch-12) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Documentação simples

### Objetivos de aprendizagem

Você vai (1) escrever instruções simples que outras pessoas consigam seguir; (2) manter registros das mudanças; (3) guardar os documentos onde possam ser encontrados.

### 14.1 Por que documentar

O Sr. Doyle é a única pessoa de TI da Westfield. Quando ele está de férias, a empresa de suporte e os gerentes dos centros precisam saber como as coisas estão configuradas. Chloe aprende que uma documentação simples, escrita com clareza, permite que outras pessoas ajudem quando o responsável habitual está fora. O Sr. Appiah explica que a documentação é um controle de segurança, porque os erros acontecem quando as pessoas adivinham como os sistemas funcionam e mudam a configuração errada. Chloe pergunta ao Sr. Doyle sobre quais tarefas a empresa de suporte mais liga para ele quando está fora. Ele cita três, e ela decide documentá-las primeiro, porque ajudariam mais gente.

### 14.2 Redação das instruções

Chloe escreve instruções passo a passo para três tarefas: configurar um tablet novo, redefinir o código de um funcionário do caixa e verificar que o backup noturno rodou. Cada uma tem um título, a finalidade, passos numerados com capturas de tela e o que fazer se algo der errado. Ela pede a uma gerente de centro que siga as instruções do tablet. A gerente trava num passo, por isso Chloe acrescenta uma captura de tela que faltava. Ela aprende que o melhor teste das instruções é outra pessoa usá-las. Depois disso, a gerente conclui a tarefa sem ajuda.

### 14.3 Registros de mudanças

Chloe inicia um log de mudanças simples para a Westfield: data, o que mudou, por quê, quem fez a mudança e como desfazê-la. Ela registra a troca da senha do roteador, as mudanças de permissão das pastas e a separação da rede sem fio de visitantes. O Sr. Doyle acha o log útil quando uma gerente de centro pergunta por que não consegue mais ver a pasta das faturas. O log responde à pergunta em segundos. Ela acrescenta uma coluna que mostra se cada mudança foi testada depois e a preenche para as mudanças feitas até então. O Sr. Doyle decide continuar usando o log depois do estágio e pede à empresa de suporte que registre nele também as mudanças dela.

### 14.4 Guarda dos documentos

Chloe guarda as instruções e o log de mudanças numa pasta compartilhada que os gerentes e a empresa de suporte podem abrir, mas não os clientes nem as contas dos caixas. Ela evita escrever senhas nos documentos e remete ao gerenciador de senhas. Ela acrescenta uma data e um responsável a cada documento. O Sr. Appiah observa que os documentos sem data deixam os leitores sem saber se ainda estão corretos. Ela cria um documento de índice que lista cada instrução, sua finalidade, seu responsável e sua data, para que o leitor encontre depressa a instrução certa. O Sr. Doyle confere as permissões da pasta e confirma que apenas os gerentes e a empresa de suporte conseguem abri-la.

### Exemplo resolvido

Chloe escreve e testa três conjuntos de instruções, inicia um log de mudanças que responde à pergunta de uma gerente e guarda documentos datados e sem senhas.

> **Caso sintético.** Os documentos são sintéticos.

### Erros e limites

Escrever senhas nos documentos as expõe a todos os leitores.

### Exercícios

- **EX053 — Tarefas documentadas.** Cite uma tarefa que Chloe documenta. *Rubrica:* 3 = redefinir o código de um funcionário do caixa;; 2 = uma;; 1 = vago;; 0 = nenhuma.

- **EX054 — Teste das instruções.** Quem testa as instruções do tablet? *Rubrica:* 3 = uma gerente de centro;; 2 = parcialmente correto;; 1 = outra pessoa;; 0 = nenhuma.

- **EX055 — Uso do log de mudanças.** Que pergunta o log de mudanças responde? *Rubrica:* 3 = por que uma gerente perdeu o acesso às faturas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX056 — Datas nos documentos.** Por que acrescentar datas aos documentos? *Rubrica:* 3 = os leitores sabem se estão atualizados;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue estudando — aula 14 (capítulo 14 de 18)

[← Capítulo 13](#ch-13) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Trabalhando com o responsável de TI

### Objetivos de aprendizagem

Você vai (1) receber orientações de um colega mais experiente; (2) pedir ajuda de forma adequada; (3) trabalhar dentro de sua autoridade.

### 15.1 Receber orientações

Durante o estágio, Chloe trabalha sob a orientação do Sr. Doyle. Toda segunda-feira, ele lhe dá uma lista de tarefas para a semana: verificações de contas, atualizações de dispositivos, documentação e visitas aos centros. Ela confirma que entende cada tarefa e pergunta sobre as prioridades. O Sr. Appiah explica que um acordo claro no início evita esforço desperdiçado e mal-entendidos, sobretudo quando o colega mais experiente está ocupado. Ela escreve a lista no caderno, com a prioridade ao lado de cada tarefa, e marca cada uma quando termina. No fim da semana, ela envia ao Sr. Doyle um breve resumo do que foi concluído e do que fica para a semana seguinte, o que, segundo ele, lhe poupa tempo.

### 15.2 Pedir ajuda

Chloe às vezes encontra problemas que não consegue resolver, como um caixa que se recusa a conectar depois de uma atualização. Ela tenta primeiro os passos documentados e depois liga para o Sr. Doyle com um resumo claro do que tentou. Ele a orienta na correção. O Sr. Appiah observa que pedir ajuda cedo, com um resumo claro, é uma habilidade profissional, enquanto lutar em silêncio por horas desperdiça tempo e pode piorar as coisas. Ela acrescenta a correção à pasta de instruções, para que a próxima pessoa consiga resolver o mesmo problema sem ligar.

### 15.3 Trabalhar dentro da autoridade

Chloe aprende que algumas ações precisam da aprovação do Sr. Doyle: mudar configurações do firewall, dar acesso de administrador a alguém ou apagar contas. Quando uma gerente de centro pede que ela dê a uma nova supervisora acesso à pasta das faturas, ela explica que precisa conferir primeiro com o Sr. Doyle. Ele confirma que a supervisora não precisa desse acesso. Chloe aprende que dizer ainda não, com educação, protege tanto a ela quanto a empresa. A gerente do centro aceita a resposta, e o Sr. Doyle explica que a supervisora pode pedir à gerente do escritório qualquer fatura específica de que precise. Chloe registra o pedido e a decisão no log de mudanças.

### 15.4 Retorno

O Sr. Doyle dá retorno a Chloe a cada duas semanas. Ele elogia suas comunicações claras e a documentação e sugere que ela se manifeste mais cedo quando uma tarefa for demorar mais do que o previsto. Chloe registra o retorno no caderno e define a meta de avisá-lo em até um dia se uma tarefa estiver atrasando. O Sr. Appiah observa que o retorno regular ajuda os estudantes a melhorar mais depressa do que esperar até o fim. Na reunião de retorno seguinte, o Sr. Doyle observa que ela o avisou cedo sobre uma tarefa atrasada e que o atraso não causou problemas.

### Exemplo resolvido

Chloe confirma as tarefas semanais, pede ajuda com um resumo claro, recusa com educação um pedido de acesso não aprovado e age com base no retorno.

> **Caso sintético.** O estágio é sintético.

### Erros e limites

Conceder acesso sem aprovação pode dar às pessoas dados que elas não deveriam ver.

### Exercícios

- **EX057 — Lista semanal.** Quando o Sr. Doyle passa as tarefas? *Rubrica:* 3 = toda segunda-feira;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX058 — Como pedir ajuda.** O que Chloe faz antes de ligar pedindo ajuda? *Rubrica:* 3 = tenta os passos documentados;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX059 — Aprovação necessária.** Cite uma ação que precisa de aprovação. *Rubrica:* 3 = dar acesso de administrador;; 2 = uma;; 1 = vago;; 0 = nenhuma.

- **EX060 — Meta do retorno.** Que meta Chloe define? *Rubrica:* 3 = avisá-lo em até um dia se uma tarefa atrasar;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue estudando — aula 15 (capítulo 15 de 18)

[← Capítulo 14](#ch-14) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Prática no local de trabalho

### Objetivos de aprendizagem

Você vai (1) aplicar as habilidades ao longo de um estágio completo; (2) lidar com situações de contato com os clientes; (3) refletir sobre o que aprendeu.

### 16.1 O estágio

Chloe passa dez semanas na Westfield, dois dias por semana, circulando entre os centros. Ela confere dispositivos, ajuda a equipe com problemas de entrada nos sistemas, atualiza a documentação e apoia o Sr. Doyle em projetos. Ela vê que a movimentada temporada de primavera deixa a equipe impaciente com qualquer coisa que atrase os caixas. Ela aprende a agendar o trabalho para horários mais tranquilos, como o início da manhã, e a explicar brevemente o que está fazendo e por quê. Ela mantém um breve log diário das tarefas, dos centros visitados e dos problemas encontrados, o que a ajuda a escrever o relatório de estágio e a lembra de lições que de outro modo poderia esquecer.

### 16.2 Momentos com os clientes

Às vezes Chloe trabalha perto dos clientes. Um cliente pergunta por que a rede sem fio do café pede um endereço de e-mail. Chloe explica que é opcional e oferece a opção de acesso direto. Outro cliente pede que ela consulte seus pontos de fidelidade. Ela o encaminha com educação à equipe do caixa, porque não está autorizada a acessar as contas dos clientes. O Sr. Appiah observa que a equipe de suporte representa a empresa e precisa ficar dentro de sua função. Os dois clientes saem satisfeitos, e Chloe registra as perguntas no caderno como exemplos de como permanecer dentro da própria função.

### 16.3 Um momento de segurança

Durante uma visita, Chloe percebe um desconhecido numa área da equipe que diz ser do fornecedor dos caixas. Ele não tem crachá e não era esperado. Ela pede com educação que ele espere na recepção e liga para o Sr. Doyle, que confirma que nenhuma visita estava planejada. O homem vai embora. O Sr. Doyle lembra a todos os centros que as visitas de fornecedores são sempre combinadas com antecedência. Chloe aprende que a segurança física depende de funcionários dispostos a fazer perguntas. Chloe escreve uma breve comunicação do ocorrido, com o horário e uma descrição do homem.

### 16.4 Reflexão

Chloe escreve uma reflexão no fim do estágio. Ela observa que as tarefas técnicas muitas vezes eram simples, mas trabalhar com pessoas ocupadas exigia paciência e explicações claras. Ela se orgulha da verificação das atualizações dos dispositivos e da documentação. Ela quer melhorar seu entendimento de redes. O Sr. Appiah lê a reflexão e observa o quanto a confiança dela cresceu. Ela também anota uma coisa que faria diferente: fazer mais perguntas no início de cada tarefa, em vez de descobrir no meio do caminho que tinha entendido mal o que era necessário. O Sr. Appiah diz que esse tipo de reflexão honesta mostra maturidade.

### Exemplo resolvido

Chloe trabalha dez semanas entre os centros, agenda o trabalho em torno dos períodos de movimento, fica dentro de sua função com os clientes, detém um visitante inesperado e reflete sobre seu crescimento.

> **Caso sintético.** O estágio é sintético.

### Erros e limites

Deixar visitantes inesperados entrarem nas áreas da equipe sem verificação traz risco de furto ou adulteração.

### Exercícios

- **EX061 — Formato do estágio.** Quanto dura o estágio? *Rubrica:* 3 = dez semanas, dois dias por semana;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX062 — Pedido de fidelidade.** Como Chloe trata um pedido de pontos de fidelidade? *Rubrica:* 3 = encaminha o cliente à equipe do caixa;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX063 — Resposta ao visitante.** O que Chloe faz com o visitante inesperado? *Rubrica:* 3 = pede que espere e liga para o Sr. Doyle;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX064 — Ponto a melhorar.** O que Chloe quer melhorar? *Rubrica:* 3 = o entendimento de redes;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue estudando — aula 16 (capítulo 16 de 18)

[← Capítulo 15](#ch-15) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Avaliação prática

### Objetivos de aprendizagem

Você vai (1) concluir tarefas práticas de segurança sob avaliação; (2) explicar suas ações; (3) demonstrar um trabalho seguro.

### 17.1 A avaliação

No fim do curso, Chloe faz uma avaliação prática no laboratório da escola. Ela tem três horas para cumprir tarefas num conjunto de máquinas virtuais que representam uma pequena empresa: criar contas com o acesso certo, encontrar dispositivos sem atualizações, identificar e-mails de phishing numa caixa postal de amostra, verificar que um backup pode ser restaurado e escrever uma comunicação de problema. Um avaliador observa e faz perguntas. O Sr. Appiah explica que a avaliação verifica tanto a habilidade técnica quanto os hábitos de trabalho seguro, por isso os estudantes devem explicar suas escolhas enquanto trabalham.

### 17.2 Cumprindo as tarefas

Chloe começa lendo todas as tarefas e planejando o tempo. Ela cria as contas com o acesso correto e as confere entrando com elas. Ela executa seu script de atualizações nos dados do laboratório e lista os dispositivos atrasados. Ela classifica os e-mails de amostra usando os quatro sinais de phishing e anota uma mensagem sobre a qual não tem certeza, explicando por quê. Ela restaura uma pasta de teste e compara os arquivos. Ela termina com dez minutos de sobra. Ela usa o tempo restante para conferir se falta algum detalhe na comunicação de problema.

### 17.3 Explicando as ações

O avaliador pergunta por que ela conferiu as contas entrando com elas. Chloe explica que conferir se uma mudança funcionou é um hábito que aprendeu no estágio. Ele pergunta o que ela faria se uma restauração falhasse. Ela explica que registraria o que aconteceu, comunicaria o fato e não apagaria o backup original. O avaliador observa que ela explica seu raciocínio com clareza e calma. Ele também pergunta como ela decidiu quais e-mails eram phishing. Ela descreve os quatro sinais e explica que marcou uma mensagem como incerta em vez de adivinhar, porque uma decisão errada, em qualquer direção, poderia causar problemas.

### 17.4 Trabalho seguro

A avaliação inclui um teste oculto: uma tarefa pede que ela desative uma configuração de segurança para fazer um programa rodar. Chloe para e pergunta ao avaliador se isso está aprovado, explicando o risco. Ele confirma que era um teste de julgamento. O Sr. Appiah explica depois que saber quando parar e perguntar é tão importante quanto a habilidade técnica, porque muitos incidentes começam com atalhos bem-intencionados. Chloe é aprovada nas cinco tarefas e no teste de julgamento. O retorno escrito do avaliador destaca seu hábito de conferir o próprio trabalho e de perguntar antes de tomar ações arriscadas.

### Exemplo resolvido

Chloe planeja e conclui cinco tarefas práticas, explica seu raciocínio e passa num teste de julgamento ao parar antes de desativar uma configuração de segurança.

> **Caso sintético.** A avaliação é sintética.

### Erros e limites

Desativar uma configuração de segurança sem aprovação para fazer algo funcionar pode abrir riscos graves.

### Exercícios

- **EX065 — Tempo da avaliação.** Quanto dura a avaliação? *Rubrica:* 3 = três horas;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX066 — Mensagem incerta.** O que Chloe faz com um e-mail incerto? *Rubrica:* 3 = anota-o e explica por quê;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX067 — Restauração com falha.** O que ela faria se uma restauração falhasse? *Rubrica:* 3 = registrar, comunicar, manter o backup original;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX068 — Teste oculto.** Qual era o teste oculto? *Rubrica:* 3 = desativar uma configuração de segurança;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue estudando — aula 17 (capítulo 17 de 18)

[← Capítulo 16](#ch-16) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continue para a próxima aula já escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Revisão e próximos passos

### Objetivos de aprendizagem

Você vai (1) revisar o que aprendeu; (2) planejar a continuação do aprendizado; (3) entender como este curso se liga a outros.

### 18.1 Olhando para trás

Chloe revisa seu caderno desde o início do curso. As primeiras anotações descrevem o cumprimento de instruções; as últimas mostram que ela encontra causas, escreve documentação e faz julgamentos. Ela lista as habilidades que adquiriu: gerenciar contas, verificar atualizações com scripts, identificar phishing, proteger dados pessoais, verificar redes e backups, comunicar problemas e trabalhar com um colega mais experiente. O Sr. Appiah observa que o caderno é uma boa evidência de seu progresso. Ela compara lado a lado a primeira e a última comunicação e vê o quanto sua escrita ficou mais clara e mais específica.

### 18.2 Resultados

Chloe é aprovada no curso com mérito. O Sr. Doyle escreve uma carta de referência elogiando seu trabalho cuidadoso e suas comunicações claras, e a Westfield lhe oferece uma função de suporte em meio período enquanto ela continua estudando. Chloe fica contente porque seu trabalho, como a verificação das atualizações e a documentação, continua sendo usado na Westfield depois do fim do estágio. Ela também recebe um certificado que lista as habilidades práticas avaliadas. O Sr. Appiah a parabeniza e pergunta se ela visitaria os estudantes do ano seguinte para falar do estágio. Ela concorda e planeja levar exemplos de sua documentação e de seu script de atualizações, sem nenhum dado real.

### 18.3 Continuação do aprendizado

Chloe planeja estudar para uma certificação profissional de nível inicial e aprender mais sobre redes, que ela anotou como um ponto fraco. O Sr. Appiah sugere que ela mantenha o hábito do caderno e confira se as fontes estão atualizadas, já que as normas mudam; a ISO/IEC 27000, por exemplo, foi revisada em 2026. Ele também recomenda participar de um grupo local em que profissionais de segurança compartilham experiências. Chloe escreve um plano de aprendizado com três metas para o próximo ano: ser aprovada na certificação, concluir um curso curto de redes e conduzir um pequeno projeto de melhoria na Westfield com o apoio do Sr. Doyle.

### 18.4 O próximo curso

O Sr. Appiah explica que o próximo curso nesta área, governança de dados, examina quem decide como as informações são coletadas, conferidas, usadas e guardadas. Chloe observa que muitas de suas tarefas de segurança, como restringir pastas e tratar os pedidos dos clientes, dependiam de decisões sobre os dados que alguém precisou tomar antes. Ela planeja fazer o curso para entender melhor essas decisões. O Sr. Appiah acrescenta que a segurança e a governança de dados trabalham muito juntas nas pequenas empresas, em que as mesmas poucas pessoas muitas vezes tomam decisões sobre as duas. Chloe concorda que entender as duas a tornará mais útil na Westfield.

### Exemplo resolvido

Chloe revisa seu crescimento, é aprovada com mérito, assume uma função em meio período na Westfield e planeja a certificação, o estudo de redes e o curso de governança de dados.

> **Caso sintético.** Os resultados são sintéticos.

### Erros e limites

Depender de fontes antigas sem conferir as edições pode espalhar orientações desatualizadas.

### Exercícios

- **EX069 — Resultado do curso.** Que resultado Chloe obtém? *Rubrica:* 3 = aprovação com mérito;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX070 — Oferta da Westfield.** O que a Westfield oferece a Chloe? *Rubrica:* 3 = uma função de suporte em meio período;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX071 — Ponto fraco.** Que área Chloe planeja fortalecer? *Rubrica:* 3 = redes;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

- **EX072 — Tema do próximo curso.** O que cobre o curso de governança de dados? *Rubrica:* 3 = quem decide como as informações são coletadas e usadas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue estudando — aula 18 (capítulo 18 de 18)

[← Capítulo 17](#ch-17) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX072. Chloe Martin, o Sr. Kwesi Appiah, o Harborview Technical College, a Westfield Garden Centres e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Dezoito meses.

**EX002.** 24 tablets para a conferência de estoque.

**EX003.** O Sr. Sam Doyle.

**EX004.** Praticar apenas em equipamentos da escola ou com permissão por escrito.

**EX005.** Manter a informação privada, exata e disponível.

**EX006.** Mantê-los exatos para que os pagamentos cheguem ao lugar certo.

**EX007.** Uma lista impressa de entregas de clientes.

**EX008.** Todas as contas da equipe podem abri-la.

**EX009.** Um login compartilhado por centro.

**EX010.** Um anexo nocivo ganharia controle total.

**EX011.** Os temporários do ano passado ainda tinham contas ativas.

**EX012.** Apenas o acesso necessário para a tarefa.

**EX013.** Os criminosos testam em outros sites as senhas vazadas de um deles.

**EX014.** Alguns funcionários não querem aplicativos nos celulares pessoais.

**EX015.** Ligando de volta para o número que consta nos registros dos funcionários.

**EX016.** Num bilhete adesivo no escritório.

**EX017.** Quantos dispositivos há de cada tipo.

**EX018.** Imprime um aviso em vez de parar.

**EX019.** Explicando-a a um colega.

**EX020.** Uma lista de dispositivos fracos poderia ajudar um atacante.

**EX021.** Uma senha num bilhete adesivo.

**EX022.** O bloqueio de tela e o apagamento remoto.

**EX023.** A entrada com múltiplos fatores.

**EX024.** A aceitabilidade psicológica.

**EX025.** 4 de 24 tablets, 16,7 por cento.

**EX026.** Nenhum dos 22 caixas.

**EX027.** Ficavam desligados numa gaveta como reserva.

**EX028.** Atualizações automáticas durante a noite, enquanto carregam.

**EX029.** 11 dos 12 e-mails de phishing.

**EX030.** Três e-mails genuínos.

**EX031.** Mostrava apenas um sinal, um endereço de remetente que não correspondia.

**EX032.** Mais phishing é pego, mas os alarmes falsos sobem muito.

**EX033.** O endereço de e-mail de um cliente.

**EX034.** Um aplicativo de entregas que mostre apenas as próprias entregas.

**EX035.** A gerente do escritório.

**EX036.** Comunicá-lo imediatamente.

**EX037.** Entrando com uma conta de teste de caixa.

**EX038.** Dois notebooks mais antigos.

**EX039.** O serviço de compartilhamento aprovado, com links que expiram.

**EX040.** O bloqueio automático da tela depois de alguns minutos.

**EX041.** Os caixas e os terminais de pagamento.

**EX042.** As redes sem fio de visitantes e da equipe compartilhavam a mesma rede e a mesma senha.

**EX043.** A caixa de som inteligente de um funcionário.

**EX044.** As senhas padrão são publicadas na internet.

**EX045.** Bloqueia os arquivos e exige pagamento.

**EX046.** A cada três meses.

**EX047.** Planilhas na área de trabalho do notebook da gerente do escritório.

**EX048.** Parar de usar o dispositivo.

**EX049.** O que foi visto, onde, quando, quem é afetado e o que já foi feito.

**EX050.** O horário, o centro e a mensagem que exigia pagamento.

**EX051.** Ligar um celular num caixa para carregá-lo.

**EX052.** Toda semana, até que cada uma seja encerrada.

**EX053.** Redefinir o código de um funcionário do caixa.

**EX054.** Uma gerente de centro.

**EX055.** Por que uma gerente de centro não conseguia mais ver as faturas.

**EX056.** Para que os leitores saibam se eles ainda estão corretos.

**EX057.** Toda segunda-feira.

**EX058.** Ela tenta primeiro os passos documentados.

**EX059.** Dar acesso de administrador a alguém.

**EX060.** Avisar o Sr. Doyle em até um dia se uma tarefa estiver atrasando.

**EX061.** Dez semanas, dois dias por semana.

**EX062.** Ela encaminha o cliente à equipe do caixa.

**EX063.** Pede que ele espere na recepção e liga para o Sr. Doyle.

**EX064.** Seu entendimento de redes.

**EX065.** Três horas.

**EX066.** Ela o anota e explica por que não tem certeza.

**EX067.** Registrar o ocorrido, comunicá-lo e não apagar o backup original.

**EX068.** Uma tarefa que pedia que ela desativasse uma configuração de segurança.

**EX069.** Aprovação com mérito.

**EX070.** Uma função de suporte em meio período.

**EX071.** Redes.

**EX072.** Quem decide como as informações são coletadas, conferidas, usadas e guardadas.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939
