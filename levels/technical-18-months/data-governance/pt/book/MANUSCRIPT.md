# Governança de Dados: Curso Técnico

- Idioma: português do Brasil (`pt`); curso 049, curso técnico (18 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 18 já estão escritos em português, com os exercícios EX001–EX024 e suas resoluções com rubricas de 0 a 3; os capítulos 7–18 (EX025–EX072) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de curso técnico que se preparam para trabalhar como técnicos de dados, registrando, conferindo, corrigindo e protegendo dados segundo regras acordadas.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios comparam uma tabela de horários sintética com os registros de contagem de passageiros para encontrar, por linha, as viagens sem contagem, e normalizam nomes sintéticos de pontos de ônibus para descobrir quantos pontos reais existem por trás das variações. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de curso técnico desde formulários, planilhas e verificações simples em Python, passando por qualidade, completude, nomes e códigos, dados pessoais, segurança, compartilhamento e retenção, até registros de problemas, documentação, curadoria, um estágio e uma avaliação prática. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Marta Kowalski** | Estudante do curso técnico | Inventada |
| **Sr. Daniel Osei** | Instrutor | Inventado |
| **Southport Technical College** | Escola técnica fictícia | Inventada |
| **Linkway Buses** | Empresa de ônibus fictícia, com sessenta ônibus em doze linhas | Inventada |

### Fontes principais

Wang e Strong (1996); GDPR; LGPD. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–18: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Começando na Southport

### Objetivos de aprendizagem

Você vai (1) descrever o curso técnico e seu caso; (2) explicar o que a governança de dados significa para um técnico; (3) preparar-se para aprender pela prática.

### 1.1 A estudante

Marta Kowalski começa um curso técnico de dezoito meses em administração de dados na fictícia Southport Technical College. Seu instrutor, o Sr. Daniel Osei, explica que os técnicos lidam com dados todos os dias: registram, conferem, corrigem e mantêm os dados seguros. O curso acompanha uma empresa parceira fictícia, a Linkway Buses, que opera sessenta ônibus em doze linhas em uma cidade de porte médio e registra passagens, contagens de passageiros, tabelas de horários e horas de trabalho da equipe. Todos os dados dos exercícios e laboratórios são sintéticos, criados apenas para o ensino. Marta está pronta para começar.

### 1.2 Governança para técnicos

O Sr. Osei explica a governança de dados de forma simples: combinar quem é responsável por cada tipo de dado, que regras ele deve seguir e como é mantido em segurança. Os técnicos normalmente não tomam essas decisões, mas aplicam as regras e percebem quando algo dá errado. Marta aprende que seu papel é seguir os procedimentos com cuidado, conferir os dados, relatar problemas à pessoa certa e sugerir melhorias com base no que vê no trabalho diário. Ela escreve essa descrição de seu papel na primeira página do caderno de atividades, para consultá-la ao longo do curso.

### 1.3 Aprendendo na prática

A maior parte das aulas envolve tarefas práticas: conferir uma planilha, escrever um script curto em Python, preencher um formulário de problema ou ler um procedimento. O Sr. Osei pede a Marta que mantenha um caderno de atividades registrando cada tarefa, o que deu certo e o que foi difícil. Ele explica que os empregadores valorizam técnicos capazes de mostrar evidências de seu trabalho, e que o caderno vai ajudá-la a se preparar para a avaliação prática no fim do curso. Marta começa o caderno no primeiro dia, registrando a primeira tarefa e uma dúvida sobre ela.

### 1.4 As necessidades da Linkway

O responsável pelos dados da Linkway, uma figura fictícia chamada Sr. Hughes, visita a turma. Ele explica que a empresa informa o número de passageiros à autoridade local de transporte, que financia parte de algumas linhas. Contagens ausentes ou erradas podem reduzir esse financiamento. Ele também menciona reclamações sobre nomes de pontos errados no site e a preocupação em proteger os dados pessoais dos funcionários e dos passageiros. Pede aos estudantes ajuda com verificações práticas durante o curso. Marta anota cada necessidade no caderno, e a turma decide começar pelas contagens de passageiros, porque o financiamento depende delas.

### Exemplo resolvido

Marta começa o curso técnico, aprende que os técnicos aplicam as regras e relatam problemas, mantém um caderno de tarefas práticas e ouve as necessidades da Linkway sobre contagens de passageiros, nomes de pontos e dados pessoais.

> **Caso sintético.** A Southport, a Linkway e todas as pessoas são sintéticas.

### Erros e limites

Supor que a governança cabe só aos gestores ignora o papel diário do técnico.

### Exercícios

- **EX001 — Frota da Linkway.** Quantos ônibus a Linkway opera? *Rubrica:* 3 = sessenta;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX002 — Tarefas do técnico.** O que os técnicos fazem na governança? *Rubrica:* 3 = aplicam regras, conferem dados e relatam problemas;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX003 — Finalidade do caderno.** Por que manter um caderno de atividades? *Rubrica:* 3 = evidência do trabalho para empregadores e para a avaliação;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX004 — Risco ao financiamento.** Por que as contagens de passageiros importam para o financiamento? *Rubrica:* 3 = a autoridade financia parte das linhas com base nelas;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Dados em uma empresa de ônibus

### Objetivos de aprendizagem

Você vai (1) listar os principais dados de uma empresa de ônibus; (2) acompanhar como as contagens de passageiros são coletadas; (3) identificar quem as usa.

### 2.1 Principais dados

Marta lista os dados da Linkway: tabelas de horários com linhas, pontos e horários de partida; vendas de passagens nas máquinas de cada ônibus; contagens de passageiros feitas por sensores nas portas; escalas e horas dos motoristas; registros de manutenção dos veículos; e reclamações de clientes. Cada um fica em um sistema ou planilha diferente. Ela observa que as tabelas de horários ligam muitos conjuntos, porque passagens, contagens e escalas se referem a uma viagem programada, identificada pela linha e pelo horário de partida. Marta desenha um diagrama simples com cada conjunto em uma caixa, ligada à tabela de horários no centro.

### 2.2 Como as contagens são coletadas

Sensores acima de cada porta contam as pessoas que sobem e descem. No fim de cada viagem, o computador de bordo guarda os totais com o identificador da viagem. Quando o ônibus volta à garagem à noite, os dados são enviados pela rede sem fio da garagem. Marta observa que, se um ônibus não se conecta na garagem, suas contagens esperam até a noite seguinte, e que, se o sensor falha, nenhuma contagem é registrada para aquela viagem. O Sr. Hughes confirma que os dois problemas acontecem todo mês e que ninguém acompanha hoje quantas viagens ficam sem contagem.

### 2.3 Quem usa as contagens

As contagens são usadas pelos planejadores que decidem os horários, pelos gestores que prestam contas à autoridade de transporte e pelo financeiro, que estima a receita das linhas financiadas. A autoridade de transporte as usa para decidir o financiamento. Marta percebe que uma contagem ausente pode levar os planejadores a cortar uma viagem cheia ou a autoridade a reduzir o financiamento de uma linha da qual as pessoas dependem. Ela escreve no caderno que erros nos dados podem afetar o serviço de ônibus dos passageiros e acrescenta cada usuário ao diagrama, com uma nota sobre o que ele decide usando as contagens.

### 2.4 Onde os erros entram

Marta marca os pontos por onde os erros podem entrar: sensores com defeito, envios que falham, mudanças de horário não carregadas nos computadores de bordo e correções manuais em planilhas. O Sr. Osei pede que ela os ordene pela frequência com que acha que acontecem e pelo dano que causam. Ela coloca no topo os sensores com defeito e os envios que falham. Ele explica que esse tipo de ordenação simples ajuda a decidir onde as verificações são mais necessárias antes de investir tempo. Marta anota que sua ordenação é um primeiro palpite, que ela vai testar com verificações reais mais adiante no curso.

### Exemplo resolvido

Marta lista os dados da Linkway, com as tabelas de horários como elo, acompanha as contagens desde os sensores das portas até o envio na garagem, identifica planejadores, gestores, financeiro e autoridade como usuários e ordena os pontos de entrada de erros.

> **Caso sintético.** Os sistemas são sintéticos.

### Erros e limites

Ignorar como os dados são coletados esconde onde os erros começam.

### Exercícios

- **EX005 — Dados de ligação.** Que conjunto de dados liga muitos outros? *Rubrica:* 3 = as tabelas de horários;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX006 — Momento do envio.** Quando as contagens são enviadas? *Rubrica:* 3 = à noite, na garagem;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX007 — Dano de uma contagem ausente.** Que dano uma contagem ausente pode causar? *Rubrica:* 3 = o corte de uma viagem cheia ou a redução do financiamento;; 2 = correto;; 1 = parcial;; 0 = nenhuma.
- **EX008 — Principais pontos de erro.** Que pontos de erro Marta colocou no topo? *Rubrica:* 3 = sensores com defeito e envios que falham;; 2 = ambos;; 1 = um;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Registros e formulários

### Objetivos de aprendizagem

Você vai (1) desenhar formulários que coletem bons dados; (2) usar campos obrigatórios e listas; (3) testar formulários com os usuários.

### 3.1 Formulários em papel e em tela

A Linkway coleta alguns dados por formulários: reclamações de passageiros, relatos de ocorrências dos motoristas e registros de achados e perdidos. Marta revisa o formulário de reclamação e encontra texto livre para a linha, a data e o ponto, de modo que as pessoas escrevem as linhas de muitos jeitos, como linha 7, número 7 e o ônibus do hospital. Ela observa que o texto livre dificulta a análise posterior, porque a mesma linha aparece com nomes diferentes. Ela conta onze maneiras diferentes de escrever os números das linhas em um único mês de reclamações sintéticas, o que mostra o tamanho do problema para quem as analisa.

### 3.2 Um desenho melhor

Marta redesenha o formulário de reclamação do site: a linha é escolhida em uma lista, a data em um calendário, o ponto em uma lista filtrada pela linha, e há uma caixa de texto livre para a descrição. Os campos obrigatórios ficam claramente marcados. Ela mantém o formulário curto, pedindo só as informações necessárias para tratar a reclamação. Explica que bons formulários previnem erros logo no início, o que é mais fácil do que corrigi-los depois em planilhas. O Sr. Hughes aprova o desenho para testes antes de ele ir para o site, e pede que Marta registre cada decisão no caderno.

### 3.3 Dados de contato

O formulário antigo pedia o endereço completo, a data de nascimento e o telefone do passageiro. Marta pergunta ao Sr. Hughes por quê. Ele responde que basta um e-mail ou um telefone para dar a resposta. Ela remove o endereço e a data de nascimento. O Sr. Osei explica que coletar apenas o necessário é um princípio de proteção de dados, o princípio da necessidade no art. 6º, III, da LGPD, e também torna os formulários mais rápidos de preencher, de modo que mais passageiros os concluem. O Sr. Hughes concorda, e a versão seguinte pede apenas um e-mail ou um telefone, à escolha do passageiro.

### 3.4 Testando com os usuários

Marta pede a três colegas de turma e a dois funcionários da Linkway que preencham o novo formulário. Um funcionário aponta que alguns pontos têm o mesmo nome em linhas diferentes, por isso a lista de pontos precisa mostrar a linha. Outro acha o calendário difícil de usar no celular. Marta ajusta as duas coisas. Ela aprende que testar formulários com usuários reais revela problemas que os desenhistas não veem e registra as mudanças no caderno, com os motivos. O formulário final entra no site, e o Sr. Hughes relata que as reclamações agora chegam com a linha e o ponto corretos em quase todos os casos.

### Exemplo resolvido

Marta encontra linhas escritas em texto livre no formulário de reclamação, redesenha-o com listas e um calendário, remove os campos desnecessários de endereço e data de nascimento e corrige os problemas encontrados no teste com usuários.

> **Caso sintético.** Os formulários são sintéticos.

### Erros e limites

Texto livre para informações estruturadas torna a análise pouco confiável.

### Exercícios

- **EX009 — Variações da linha.** Dê uma forma como as pessoas escreviam a linha 7. *Rubrica:* 3 = número 7 ou o ônibus do hospital;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX010 — Campos de contato removidos.** Que campos Marta removeu? *Rubrica:* 3 = o endereço completo e a data de nascimento;; 2 = ambos;; 1 = um;; 0 = nenhuma.
- **EX011 — Problema da lista de pontos.** Que problema os funcionários encontraram na lista de pontos? *Rubrica:* 3 = pontos com o mesmo nome em linhas diferentes;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX012 — Problema do calendário.** O que era difícil no calendário? *Rubrica:* 3 = usá-lo no celular;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Planilhas feitas com segurança

### Objetivos de aprendizagem

Você vai (1) organizar planilhas com clareza; (2) proteger fórmulas e acrescentar verificações; (3) manter as versões sob controle.

### 4.1 Uma planilha bagunçada

O relatório mensal de passageiros da Linkway é montado em uma planilha. Marta a abre e encontra dados colados do sistema de contagem, fórmulas misturadas com números digitados, cores sem explicação e três abas ocultas. Ela não consegue saber quais números são calculados e quais foram digitados. O Sr. Osei explica que planilhas assim são comuns e arriscadas, porque ninguém consegue conferi-las com facilidade e um único erro pode mudar todos os totais. Quem a montou já saiu da empresa, e a pessoa que a prepara hoje copia os passos sem saber por que alguns deles existem.

### 4.2 Organizando

Marta reorganiza uma cópia: uma aba para os dados brutos colados sem alteração, uma para os cálculos, uma para o relatório e uma explicando as fontes e os passos. As células calculadas recebem um sombreado padronizado, com legenda. Os ajustes digitados ficam em uma coluna separada, com o motivo. Ela remove as abas ocultas depois de confirmar com o dono do relatório que não são necessárias. O novo leiaute permite a qualquer pessoa ver de onde vem cada número. O dono do relatório revisa a cópia e concorda em usar o novo leiaute a partir do mês seguinte.

### 4.3 Verificações

Marta acrescenta células de verificação: o total de passageiros no relatório deve ser igual ao total dos dados brutos, e o número de viagens deve bater com a tabela de horários do mês. Se uma verificação falha, a célula fica vermelha. Ela também protege as células de fórmula, para que não sejam sobrescritas por engano. O Sr. Osei observa que verificações simples pegam a maior parte dos erros de planilha e que a proteção evita o erro mais comum, que é digitar por cima de uma fórmula. As verificações do primeiro mês passam, o que dá ao dono confiança no novo leiaute.

### 4.4 Versões

O relatório antigo era salvo como relatorio passageiros final, final2 e final mais recente. Marta cria uma convenção de nomes com o ano e o mês, salva o relatório de cada mês em uma pasta datada e mantém o modelo separado. Ela escreve a convenção na aba de explicação. Observa que versões claras permitem enviar à autoridade exatamente a versão aprovada e encontrar as versões anteriores se surgirem dúvidas. O dono do relatório adota a convenção e pede às outras equipes que também a usem, o que reduz a confusão entre os arquivos compartilhados da empresa.

### Exemplo resolvido

Marta reorganiza um relatório de passageiros bagunçado em abas de dados brutos, cálculos, relatório e explicação, acrescenta células de verificação que ficam vermelhas e proteção de fórmulas e troca os nomes do tipo final-final por versões datadas.

> **Caso sintético.** As planilhas são sintéticas.

### Erros e limites

Misturar números digitados com fórmulas esconde as alterações manuais.

### Exercícios

- **EX013 — Abas ocultas.** Quantas abas ocultas Marta encontrou? *Rubrica:* 3 = três;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX014 — Coluna de ajustes.** Onde ficam os ajustes digitados? *Rubrica:* 3 = em uma coluna separada, com o motivo;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX015 — Verificação das viagens.** Com o que o número de viagens deve bater? *Rubrica:* 3 = com a tabela de horários do mês;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX016 — Benefício das versões.** O que versões claras permitem? *Rubrica:* 3 = enviar exatamente a versão aprovada;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Conferindo dados com Python

### Objetivos de aprendizagem

Você vai (1) ler um arquivo CSV em Python; (2) escrever verificações simples; (3) imprimir um resumo claro.

### 5.1 Lendo um arquivo

O Sr. Osei apresenta o Python para as verificações repetitivas. Marta escreve um script curto com o módulo csv para ler uma exportação sintética das contagens de passageiros. Cada linha traz a data, a linha de ônibus, o horário da viagem, os embarques e os desembarques. Ela imprime o número de linhas e as primeiras linhas do arquivo para confirmar que ele foi lido corretamente. Aprende que verificar se o arquivo foi bem lido é o primeiro passo antes de confiar em qualquer resultado. Também confere se o número de linhas impresso bate com o número mostrado na tela de exportação do sistema.

### 5.2 Verificações simples

Marta escreve as verificações: embarques e desembarques devem ser números inteiros, não negativos e não maiores que cento e vinte, a capacidade do ônibus. A linha deve ser uma das doze linhas da Linkway. Ela conta as linhas do arquivo que falham em cada verificação. Observa que cada verificação é uma única regra clara, fácil de explicar ao Sr. Hughes e de mudar se a Linkway comprar ônibus maiores. Ela coloca o valor da capacidade no topo do script, como uma configuração com nome, para que possa ser alterado em um só lugar se um dia a frota mudar.

### 5.3 Resumos

Marta imprime um resumo: linhas lidas, linhas que falham em cada verificação e a parcela de falhas. Ela encontra algumas linhas com desembarques negativos, que o Sr. Hughes diz virem de um defeito de sensor em um ônibus. Ela acrescenta o número do ônibus à saída para que o defeito possa ser rastreado. Aprende que um bom resumo ajuda alguém a agir, e não apenas a saber que algo está errado. O Sr. Hughes passa o número do ônibus à equipe de manutenção, que troca o sensor defeituoso naquela semana, e os valores negativos deixam de aparecer nos arquivos seguintes.

### 5.4 Salvando e compartilhando

Marta salva o script com comentários que explicam cada passo e com a data. O Sr. Osei mostra como guardar os scripts em uma pasta compartilhada com um pequeno arquivo leia-me. Quando uma colega roda o script no arquivo de um novo mês, ele funciona sem alterações. Marta anota no caderno que um script que ela consegue executar de novo poupa horas em comparação com conferir uma planilha a olho todo mês. O Sr. Hughes pede uma cópia do script para a equipe de dados da Linkway, e Marta acrescenta uma nota curta explicando como executá-lo e o que cada linha do resumo significa.

### Exemplo resolvido

Marta lê um arquivo de contagens com o módulo csv, confere os embarques contra a capacidade e as linhas válidas, acrescenta o número do ônibus para rastrear um defeito de sensor e salva um script comentado que outras pessoas podem executar de novo.

> **Caso sintético.** As exportações são sintéticas.

### Erros e limites

Confiar em resultados antes de confirmar que o arquivo foi bem lido arrisca conclusões erradas.

### Exercícios

- **EX017 — Limite de capacidade.** Que limite superior a verificação usou? *Rubrica:* 3 = cento e vinte;; 2 = correto;; 1 = errado;; 0 = nenhuma.
- **EX018 — Causa dos negativos.** O que causou os desembarques negativos? *Rubrica:* 3 = um defeito de sensor em um ônibus;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX019 — Acréscimo para rastrear.** O que Marta acrescentou para rastrear defeitos? *Rubrica:* 3 = o número do ônibus;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX020 — Compartilhamento de scripts.** Como os scripts são compartilhados? *Rubrica:* 3 = em uma pasta compartilhada com um leia-me;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Fundamentos de qualidade de dados

### Objetivos de aprendizagem

Você vai (1) nomear dimensões comuns de qualidade de dados; (2) aplicá-las aos dados de passageiros; (3) escolher a verificação certa para cada uma.

### 6.1 Dimensões

O Sr. Osei apresenta as dimensões de qualidade em palavras simples, com base na pesquisa de Wang e Strong com usuários de dados. A completude pergunta se todos os dados esperados estão presentes. A validade pergunta se os valores seguem as regras. A exatidão pergunta se os dados correspondem à realidade. A pontualidade pergunta se os dados chegam quando são necessários. A consistência pergunta se sistemas diferentes concordam. Marta escreve no caderno um exemplo da Linkway para cada dimensão. O Sr. Osei confere os exemplos e sugere uma mudança no de pontualidade, para que corresponda ao modo como a Linkway de fato usa as contagens.

### 6.2 Aplicando às contagens

Para as contagens de passageiros, completude significa que toda viagem programada tem uma contagem. Validade significa contagens inteiras, não negativas e abaixo da capacidade. Exatidão significa que as contagens correspondem ao número real de passageiros, o que pode ser conferido por uma pessoa contando em uma amostra de viagens. Pontualidade significa que as contagens são enviadas até a manhã seguinte. Consistência significa que os totais das contagens concordam, aproximadamente, com as vendas de passagens nas mesmas viagens. Marta escreve essas definições em uma tabela no caderno, uma linha por dimensão, com uma coluna para a verificação correspondente.

### 6.3 Escolhendo as verificações

Marta associa as verificações às dimensões. Seu script em Python cobre a validade. Uma comparação com a tabela de horários cobre a completude. Uma conferência matinal dos horários de envio cobre a pontualidade. Uma comparação mensal com as vendas de passagens cobre a consistência. A exatidão exige contagens manuais, que o Sr. Hughes organiza em dez viagens por mês. Ela observa que nenhuma verificação sozinha cobre tudo, por isso várias verificações simples juntas dão um quadro mais completo. O Sr. Hughes concorda em executá-las em uma agenda regular e compartilhar os resultados todo mês com o gerente de operações e os planejadores.

### 6.4 Qualidade para uma finalidade

O Sr. Hughes explica que a autoridade se importa sobretudo com a completude e a exatidão, porque o financiamento depende do total de passageiros. Os planejadores se importam mais com a pontualidade, porque revisam as viagens cheias toda semana. Marta aprende que a qualidade depende do uso que se faz dos dados, de modo que as verificações devem se concentrar no que mais importa para cada usuário. Ela acrescenta à tabela uma coluna mostrando quais usuários se importam com cada dimensão. O Sr. Hughes usa a tabela para explicar ao gerente de operações por que as contagens manuais compensam o tempo que tomam.

### Exemplo resolvido

Marta aprende cinco dimensões de qualidade, aplica-as às contagens de passageiros, associa uma verificação a cada uma, incluindo contagens manuais mensais para a exatidão, e anota quais usuários se importam mais com cada dimensão.

> **Caso sintético.** Os exemplos são sintéticos; Wang e Strong (1996) é real.

### Erros e limites

Conferir só a validade deixa passar dados ausentes ou atrasados.

### Exercícios

- **EX021 — Verificação da exatidão.** Como a exatidão das contagens é conferida? *Rubrica:* 3 = contagens manuais em uma amostra de viagens;; 2 = correto;; 1 = nenhuma;; 0 = nenhuma.
- **EX022 — Comparação de consistência.** Com o que as contagens são comparadas para a consistência? *Rubrica:* 3 = com as vendas de passagens;; 2 = correto;; 1 = outro;; 0 = nenhuma.
- **EX023 — Prioridade da autoridade.** Que dimensões mais importam para a autoridade? *Rubrica:* 3 = completude e exatidão;; 2 = ambas;; 1 = uma;; 0 = nenhuma.
- **EX024 — Prioridade dos planejadores.** Que dimensão mais importa para os planejadores? *Rubrica:* 3 = a pontualidade;; 2 = correto;; 1 = outra;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX024 (as de EX025–EX072 estão na edição em inglês até a tradução dos capítulos correspondentes). Marta Kowalski, o Sr. Daniel Osei, a Southport Technical College, a Linkway Buses e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Sessenta ônibus.

**EX002.** Aplicam as regras, conferem os dados e relatam problemas.

**EX003.** Ele fornece evidências do trabalho para os empregadores e para a avaliação final.

**EX004.** A autoridade de transporte financia parte das linhas com base nelas.

**EX005.** As tabelas de horários, por meio da viagem programada.

**EX006.** À noite, pela rede sem fio da garagem.

**EX007.** Os planejadores poderiam cortar uma viagem cheia ou o financiamento poderia cair.

**EX008.** Sensores com defeito e envios que falham.

**EX009.** O ônibus do hospital.

**EX010.** O endereço completo e a data de nascimento.

**EX011.** Alguns pontos têm o mesmo nome em linhas diferentes.

**EX012.** Era difícil de usar no celular.

**EX013.** Três.

**EX014.** Em uma coluna separada, com o motivo.

**EX015.** A tabela de horários do mês.

**EX016.** Enviar à autoridade exatamente a versão aprovada.

**EX017.** Cento e vinte, a capacidade do ônibus.

**EX018.** Um defeito de sensor em um ônibus.

**EX019.** O número do ônibus.

**EX020.** Em uma pasta compartilhada com um pequeno leia-me.

**EX021.** Por uma pessoa contando os passageiros em uma amostra de viagens.

**EX022.** As vendas de passagens nas mesmas viagens.

**EX023.** Completude e exatidão.

**EX024.** Pontualidade.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da LGPD, citada nesta edição como referência brasileira; nenhuma das normas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
