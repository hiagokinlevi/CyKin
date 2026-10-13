# Privacidade e Proteção de Dados: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 073, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–5 de 30 já estão escritos em português, com os exercícios EX001–EX015 e suas resoluções com rubricas de 0 a 3; os capítulos 6–30 (EX016–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de tecnólogo que aprendem a verificar como sistemas reais tratam dados pessoais.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios inspecionam os fluxos de SDKs de um aplicativo sintético, testam a completude da exportação de um pedido de acesso, varrem arquivos sintéticos em busca de padrões de dados pessoais, conferem a retenção de imagens de CFTV e automatizam a exclusão de contas inativas, sempre sobre dados sintéticos. A análise jurídica é didática e não constitui aconselhamento jurídico; a LGPD e os atos da ANPD são citados pelo texto oficial e parafraseados. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de tecnólogo pelos fundamentos de computação e depois pela orientação em privacidade, ativos, fluxos, riscos, métodos, ferramentas, controles, monitoramento, solução de problemas, integração, automação, avaliação, pesquisa, trabalho em equipe, transição para a operação, implantação, prática de campo e um projeto final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Aisha Bello** | Estudante de tecnólogo | Inventada |
| **Sr. Tom Reilly** | Supervisor | Inventado |
| **Lindon Technical Institute** | Instituto fictício | Inventado |
| **Quayside Fitness** | Rede fictícia de academias, 40 unidades, cerca de 60.000 alunos, aplicativo e vestíveis | Inventada |

### Fontes principais

Regulamento (UE) 2016/679 (GDPR), artigos 5, 9, 15, 28, 30, 32, 33 e 35; Lei nº 13.709/2018 (LGPD); Resolução CD/ANPD nº 15/2024; Diretrizes 3/2019 (dispositivos de vídeo), 05/2020 (consentimento) e 01/2022 (acesso) do EDPB; WP248 rev.01; NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10); ISO/IEC 27701:2025; Nissenbaum (2004). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) |

Capítulos 6–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-06), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever os sistemas que tratam os dados dos alunos numa academia; (2) distinguir servidores, serviços em nuvem, aplicativos e dispositivos; (3) começar um inventário de sistemas.

### 1.1 O curso e o caso

Aisha Bello começa um curso de tecnólogo de três anos no fictício Lindon Technical Institute, supervisionada pelo Sr. Tom Reilly. Seu estágio é na fictícia Quayside Fitness, uma rede de quarenta academias com cerca de 60.000 alunos, um aplicativo e cintas cardíacas vestíveis usadas nas aulas. A Quayside guarda nomes, contatos, dados de pagamento, históricos de treino, leituras de frequência cardíaca e imagens de CFTV. O Sr. Reilly explica que privacidade e proteção de dados serão a especialidade de Aisha e que cada disciplina técnica do curso será aplicada aos sistemas da Quayside.

### 1.2 Tipos de sistemas

Aisha lista os sistemas da Quayside. Um sistema de matrículas na nuvem guarda contratos e pagamentos. O aplicativo guarda perfis e históricos de treino. Os computadores das unidades controlam a catraca e a reserva de aulas. As cintas cardíacas enviam a frequência cardíaca para as telas das aulas e para o aplicativo. Gravadores de CFTV ficam em cada unidade. Ela observa que alguns sistemas são operados pela Quayside e outros por fornecedores, e que os dados dos alunos circulam entre eles. Entender os tipos de sistemas a ajuda a ver onde os dados ficam e quem os controla.

### 1.3 Começar um inventário

O Sr. Reilly pede que Aisha comece um inventário. Para cada sistema, ela registra a finalidade, os dados que ele guarda, onde roda, quem é o responsável e qual fornecedor dá suporte. O inventário revela que ninguém responde pelos gravadores de CFTV de forma centralizada; cada gerente de unidade cuida do seu. Ela anota isso como uma lacuna de governança. Aprende que o artigo 30 do GDPR exige um registro das atividades de tratamento, como o art. 37 da LGPD exige o registro das operações, e que seu inventário técnico vai alimentar esse registro; por isso suas colunas usam os mesmos títulos: finalidades, categorias de dados e destinatários.

### 1.4 Por que os sistemas importam para a privacidade

Aisha reflete que a privacidade depende de os sistemas se comportarem corretamente. Uma política pode dizer que os dados de frequência cardíaca são excluídos depois de um ano, mas, se o aplicativo os guarda para sempre, a política é falsa. Ela conclui que os tecnólogos têm um papel central: sabem como os sistemas de fato se comportam e podem conferir se a prática corresponde à política. O Sr. Reilly concorda e acrescenta que eles costumam descobrir os problemas primeiro. O primeiro exemplo de Aisha é o botão de exportação do aplicativo, que a política nunca menciona, mas que deixa qualquer gerente baixar todos os alunos em segundos.

### Exemplo resolvido

Aisha lista os sistemas de matrículas, aplicativo, unidades, vestíveis e CFTV da Quayside, começa um inventário que revela a falta de um responsável central pelo CFTV e o liga ao artigo 30.

> **Caso sintético.** O Lindon, a Quayside e todas as pessoas são sintéticos; o artigo 30 do GDPR e o art. 37 da LGPD são reais.

### Erros e limites

Um primeiro inventário é incompleto; planeje revisitá-lo.

### Exercícios

- **EX001 — Lista de sistemas.** Cite quatro sistemas que guardam dados de alunos da Quayside. *Rubrica:* 3 = matrículas, aplicativo, catraca/reservas das unidades, vestíveis, CFTV;; 2 = três;; 1 = um;; 0 = nenhuma.
- **EX002 — Lacuna do CFTV.** Que lacuna de governança o inventário mostrou? *Rubrica:* 3 = nenhum responsável central pelos gravadores de CFTV;; 2 = menciona CFTV;; 1 = nenhuma;; 0 = nenhuma.
- **EX003 — Prática versus política.** Por que os tecnólogos importam para a privacidade? *Rubrica:* 3 = veem como os sistemas se comportam e podem conferir a prática diante da política;; 2 = menciona sistemas;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Redes e serviços de internet

### Objetivos de aprendizagem

Você vai (1) rastrear os dados dos alunos pelas redes; (2) identificar serviços de terceiros em aplicativos e sites; (3) proteger os dados em trânsito.

### 2.1 Redes das unidades

Cada unidade tem uma rede para os computadores da equipe, a catraca, o CFTV e o Wi-Fi de visitantes. Aisha descobre que, em duas unidades, os gravadores de CFTV e o Wi-Fi de visitantes compartilham a mesma rede, então um visitante poderia alcançar os gravadores. Ela recomenda separá-los. Explica que a segmentação de rede protege dados pessoais, como as imagens, de quem não deveria acessá-los, e reduz a chance de um dispositivo comprometido se espalhar para outros sistemas. Na Quayside, a correção é uma rede virtual separada para as câmeras, em que só o servidor de gestão dos gravadores pode se conectar a elas.

### 2.2 Serviços de internet

O site e o aplicativo da Quayside usam muitos serviços de internet: hospedagem, pagamentos, análise de uso, mapas e login social. Aisha usa as ferramentas de desenvolvedor do navegador no site, com uma conta de teste, para ver quais domínios recebem requisições, e lista onze domínios de terceiros. Alguns recebem só dados técnicos; outros recebem identificadores de alunos, como um serviço de mapas que recebe buscas por unidade com o número do aluno. Ela aprende que cada terceiro pode ser um operador que precisa de contrato pelo artigo 28 do GDPR, ou um controlador separado, e que muitos serviços são acrescentados sem revisão de privacidade.

### 2.3 Criptografia em trânsito

Aisha confere se o site e o aplicativo usam conexões criptografadas. Todos os endpoints públicos usam, mas as telas de reserva das unidades enviam os nomes dos alunos a um servidor local sem criptografia; qualquer pessoa ligada ao switch da unidade poderia ler nomes e horários de aula em texto claro. Ela leva o caso à equipe de TI, que ativa a criptografia. Explica que a criptografia em trânsito é uma medida de segurança básica pelo artigo 32 e que as redes internas não são seguras por si. Depois da mudança, ela repete a captura com uma reserva de teste, vê só tráfego cifrado e registra isso como evidência no chamado.

### 2.4 Wi-Fi de visitantes

O Wi-Fi de visitantes pede que os alunos entrem com o número de matrícula. Aisha descobre que os registros de login, com identificadores dos dispositivos, são guardados indefinidamente. Ela recomenda guardá-los só pelo tempo necessário para segurança e tratamento de abusos, por exemplo trinta dias, e informar isso aos alunos no aviso de privacidade. Os identificadores de dispositivo podem seguir um aluno entre visitas, e trinta dias limitam o histórico de deslocamentos que se acumula. Ela observa que as redes criam dados pessoais como efeito colateral, e que eles exigem o mesmo cuidado que os dados coletados de propósito.

### Exemplo resolvido

Aisha separa o CFTV do Wi-Fi de visitantes, lista onze domínios de terceiros no site, faz as telas de reserva passarem a usar criptografia e limita os registros do Wi-Fi de visitantes a trinta dias.

> **Caso sintético.** As redes são sintéticas; os artigos 28 e 32 do GDPR são reais.

### Erros e limites

As ferramentas do navegador mostram só as requisições web; os aplicativos precisam de testes separados.

### Exercícios

- **EX004 — Risco da rede compartilhada.** Por que separar o CFTV do Wi-Fi de visitantes? *Rubrica:* 3 = visitantes poderiam alcançar os gravadores com as imagens;; 2 = menciona acesso;; 1 = está bem assim;; 0 = nenhuma.
- **EX005 — Terceiros.** Como Aisha encontrou os serviços de terceiros? *Rubrica:* 3 = ferramentas de desenvolvedor do navegador com uma conta de teste;; 2 = menciona ferramentas;; 1 = adivinhou;; 0 = nenhuma.
- **EX006 — Registros do Wi-Fi.** Que retenção Aisha recomendou para os registros de login do Wi-Fi? *Rubrica:* 3 = cerca de trinta dias, com transparência;; 2 = menciona limite;; 1 = indefinida;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programação

### Objetivos de aprendizagem

Você vai (1) escrever scripts que tratem os dados dos alunos com segurança; (2) evitar imprimir ou registrar em log dados pessoais; (3) usar dados de teste.

### 3.1 Scripts seguros

Aisha escreve scripts em Python para contar a presença nas aulas. O Sr. Reilly exige dados sintéticos de alunos em todos os exercícios. O script lê um arquivo de reservas, conta a presença por aula e imprime os totais. Ela evita imprimir os nomes dos alunos, que não são necessários para os totais. Aprende que os scripts costumam ser copiados e reaproveitados, então os hábitos formados em scripts simples se espalham para os sistemas de produção. Por isso o script agrupa as reservas por código de aula e data, e a única saída é uma tabela como Spinning terça 18h com vinte e dois participantes.

### 3.2 Logs

Aisha acrescenta logs ao script para ajudar na depuração. A primeira versão registra cada reserva com o nome do aluno. Ela a altera para registrar apenas as referências das reservas e as contagens. Explica que os logs costumam ser guardados por mais tempo e acessados por mais pessoas do que os dados que descrevem, de modo que dados pessoais em logs criam exposição desnecessária. No script dela, uma linha de log agora diz que a reserva B-10422 foi contada para a aula SPN-18, o que ainda permite rastrear um erro até o arquivo de origem sem revelar quem frequentou a aula.

### 3.3 Validação da entrada

O script de Aisha lê arquivos exportados do sistema de reservas. Ela acrescenta verificações de que o arquivo só tem as colunas esperadas, e o script para se encontrar colunas inesperadas, como observações de saúde. Ela explica que a validação apoia a minimização, já que um script não deve tratar dados de que não precisa, e que parar de forma ruidosa é melhor do que tratar em silêncio informações sensíveis. A verificação compara a linha de cabeçalho com uma lista permitida de cinco colunas e encerra com uma mensagem que nomeia a coluna extra, como medical_notes, para que o responsável corrija a exportação.

### 3.4 Geração de dados de teste

Aisha escreve um gerador de alunos sintéticos com nomes, idades, tipos de plano e reservas. Inclui casos extremos, como alunos com nomes longos ou sem nenhuma reserva, e compartilha o gerador com os colegas. Ele usa uma semente aleatória fixa, então os colegas que o executam obtêm os mesmos alunos e podem comparar os resultados linha a linha. O Sr. Reilly observa que bons dados de teste tornam o desenvolvimento mais seguro e mais rápido, e que usar dados reais de alunos em testes é uma causa comum de incidentes, porque os ambientes de teste são menos protegidos.

### Exemplo resolvido

Aisha escreve um script de presença que imprime totais sem nomes, registra só referências em log, rejeita colunas inesperadas e gera alunos sintéticos com casos extremos.

> **Caso sintético.** Os scripts e os alunos são sintéticos.

### Erros e limites

Dados sintéticos podem deixar de fora peculiaridades reais; acrescente-as de propósito.

### Exercícios

- **EX007 — Sem nomes nos totais.** Por que o script de Aisha não imprime nomes? *Rubrica:* 3 = os totais não precisam deles;; 2 = menciona minimização;; 1 = imprime;; 0 = nenhuma.
- **EX008 — Conteúdo do log.** O que Aisha registra em log no lugar dos nomes? *Rubrica:* 3 = referências das reservas e contagens;; 2 = menciona referências;; 1 = nomes;; 0 = nenhuma.
- **EX009 — Dados reais em teste.** Por que evitar dados reais de alunos nos testes? *Rubrica:* 3 = é uma causa comum de incidentes;; 2 = menciona risco;; 1 = não há problema;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Modelos de dados

### Objetivos de aprendizagem

Você vai (1) desenhar modelos de dados que separem os dados sensíveis; (2) definir a retenção no próprio modelo; (3) modelar o consentimento.

### 4.1 Separar os dados sensíveis

Aisha desenha um modelo de dados para o aplicativo da Quayside. A identidade do aluno (nome, e-mail, telefone) fica numa tabela; os dados de treino e de frequência cardíaca ficam em outra, ligada por um identificador interno; as preferências de marketing ficam numa terceira. A separação permite que cada serviço acesse só o que precisa: a tela das aulas lê zonas cardíacas e primeiros nomes, mas não consulta e-mails nem a situação de pagamento. A frequência cardíaca pode ser dado relativo à saúde pelo artigo 4(15) do GDPR, e dado pessoal sensível pelo art. 5º, II, da LGPD, quando usada para avaliar condicionamento ou saúde, o que exige cuidado extra pelo artigo 9.

### 4.2 Campos de retenção

Aisha acrescenta a cada registro uma data de criação e uma categoria, para que as regras de retenção possam ser aplicadas. As leituras de frequência cardíaca são guardadas por doze meses, salvo se o aluno escolher guardá-las por mais tempo; os resumos de treino são guardados enquanto a conta estiver ativa. A rotina de retenção lê a categoria, compara a data de criação com a regra e exclui as linhas vencidas. Ela observa que desenhar a retenção no modelo desde o início é muito mais fácil do que acrescentá-la depois, quando os dados já se acumularam sem datas nem categorias.

### 4.3 Modelar o consentimento

A Quayside usa o consentimento para os e-mails de marketing e para compartilhar a frequência cardíaca com as telas das aulas. Aisha modela o consentimento como uma tabela com aluno, finalidade, versão do texto, data e situação; a revogação muda a situação e a data. Ela explica que as Diretrizes 05/2020 do EDPB exigem um consentimento específico e demonstrável, e o modelo apoia isso ao registrar o que foi aceito e quando. A versão do texto importa porque a Quayside vai mudar sua redação; sem ela, ninguém consegue provar que texto um aluno viu em 2025, comparado com 2027.

### 4.4 Revisar o modelo

O Sr. Reilly revisa o modelo de Aisha e pergunta por que a data de nascimento é guardada quando faixas etárias bastariam. Aisha a substitui por uma faixa etária para as aulas e mantém a data completa apenas no sistema de matrículas, onde ela é necessária para os contratos. Depois da revisão, ela também retira o gênero do aplicativo, já que nenhuma funcionalidade o usa. O Sr. Reilly observa que cada campo de um modelo de dados deve ter uma razão de existir, e que revisar os modelos em busca de campos desnecessários é uma prática de privacidade eficaz e barata.

### Exemplo resolvido

Aisha separa os dados de identidade, de treino e de marketing, acrescenta campos de retenção, modela o consentimento com versões do texto e substitui a data de nascimento por faixas etárias no aplicativo.

> **Caso sintético.** O modelo é sintético; os artigos 4(15) e 9 do GDPR, o art. 5º, II, da LGPD e as Diretrizes 05/2020 do EDPB são reais.

### Erros e limites

Faixas etárias ainda podem identificar pessoas em turmas pequenas; combine-as com outras proteções.

### Exercícios

- **EX010 — Natureza da frequência cardíaca.** Quando os dados de frequência cardíaca podem ser dados de saúde? *Rubrica:* 3 = quando usados para avaliar condicionamento ou saúde, pelo artigo 4(15);; 2 = menciona saúde;; 1 = nunca;; 0 = nenhuma.
- **EX011 — Campos do consentimento.** Que campos a tabela de consentimento guarda? *Rubrica:* 3 = aluno, finalidade, versão do texto, data e situação;; 2 = a maioria;; 1 = poucos;; 0 = nenhuma.
- **EX012 — Data de nascimento.** Por que substituir a data de nascimento por uma faixa etária no aplicativo? *Rubrica:* 3 = o aplicativo não precisa da data completa;; 2 = menciona necessidade;; 1 = manter;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) reconhecer as ameaças aos dados dos alunos; (2) explicar as proteções básicas à equipe das unidades; (3) reconhecer violações de dados pessoais.

### 5.1 Ameaças

Aisha lista as ameaças à Quayside: e-mails de phishing para os gerentes das unidades, senhas fracas nas telas de reserva, tablets da recepção perdidos e funcionários compartilhando listas de alunos em celulares pessoais. Ela observa que a maioria dos incidentes em negócios parecidos envolve erros comuns, e não ataques sofisticados. Agrupa as ameaças por onde começam: o phishing no e-mail, as senhas fracas na tela, os tablets perdidos na recepção e as fotos compartilhadas nos hábitos da equipe. Para cada grupo, escreve um exemplo realista, como um gerente que clica num falso link de fatura numa segunda-feira movimentada.

### 5.2 Orientação para a equipe

Aisha escreve um guia de uma página para a equipe das unidades: usar o gerenciador de senhas, bloquear as telas da recepção, nunca fotografar listas de alunos, comunicar imediatamente a perda de dispositivos e conferir os destinatários dos e-mails. Ela o testa com dois gerentes e simplifica a redação. O primeiro rascunho usava um vocabulário de segurança que os confundiu: perguntaram o que era um gerenciador de senhas e por que bloquear a tela se estavam ao lado dela. Aisha reescreve cada regra como uma ação curta com uma razão, por exemplo: bloqueie a tela sempre que se afastar, porque os alunos fazem fila bem ao lado.

### 5.3 Reconhecer violações

Aisha explica que uma violação de dados pessoais inclui perdas ou divulgações acidentais, e não só ataques. Um tablet perdido com reservas ou um e-mail enviado ao aluno errado podem ser violações. A Quayside precisa avaliar cada uma e, pelo artigo 33 do GDPR, notificar a autoridade de controle em até 72 horas, salvo se a violação não for suscetível de gerar risco; no Brasil, a Resolução CD/ANPD nº 15/2024 fixa um relógio próprio de três dias úteis para comunicar a ANPD. Ela prepara três exemplos para o treinamento: um tablet esquecido num ônibus, uma lista de turma enviada ao instrutor errado e um log da catraca exposto por um link mal configurado.

### 5.4 Comunicação de incidentes

Aisha cria um formulário simples para a equipe comunicar incidentes. Explica que a rapidez importa porque o prazo começa a contar quando a Quayside toma conhecimento. O Sr. Reilly acrescenta que funcionários com medo de serem culpados atrasam as comunicações, por isso o guia agradece a quem comunica depressa. O formulário pergunta só o que aconteceu, quando foi percebido, em que unidade e que dados podem estar envolvidos. Ele não pede à equipe que julgue a gravidade, porque essa decisão cabe ao encarregado. No primeiro mês, o formulário recebe seis comunicações, quatro delas de e-mails enviados ao destinatário errado.

### Exemplo resolvido

Aisha lista as ameaças do dia a dia, escreve um guia de uma página para a equipe, explica que perdas acidentais são violações e cria um formulário rápido de comunicação.

> **Caso sintético.** As ameaças e as orientações são sintéticas; o artigo 33 do GDPR e a Resolução CD/ANPD nº 15/2024 são reais.

### Erros e limites

Os guias precisam ser atualizados à medida que as ameaças mudam.

### Exercícios

- **EX013 — Tablet perdido.** Um tablet da recepção perdido com reservas é uma possível violação? *Rubrica:* 3 = sim; perda acidental de dados pessoais;; 2 = sim;; 1 = não;; 0 = nenhuma.
- **EX014 — Rapidez da comunicação.** Por que a equipe precisa comunicar depressa? *Rubrica:* 3 = o prazo de 72 horas começa quando a Quayside toma conhecimento;; 2 = menciona prazo;; 1 = nada;; 0 = nenhuma.
- **EX015 — Fotografar listas.** Que hábito arriscado o guia proíbe? *Rubrica:* 3 = fotografar listas de alunos com celulares pessoais;; 2 = menciona celulares;; 1 = nenhum;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX015 (as de EX016–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). Aisha Bello, o Sr. Tom Reilly, o Lindon Technical Institute, a Quayside Fitness e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Sistema de matrículas, aplicativo, vestíveis e CFTV (também a catraca e as reservas das unidades).

**EX002.** Cada unidade cuida do próprio CFTV, sem responsável central.

**EX003.** Eles sabem se os sistemas realmente seguem as políticas escritas sobre eles.

**EX004.** Visitantes na mesma rede poderiam acessar os gravadores de CFTV.

**EX005.** Observou as requisições com as ferramentas de desenvolvedor do navegador, usando uma conta de teste.

**EX006.** Cerca de trinta dias, informados no aviso de privacidade.

**EX007.** Os nomes são desnecessários para os totais de presença.

**EX008.** Referências das reservas e contagens.

**EX009.** Os ambientes de teste são menos protegidos, então os dados reais neles costumam vazar.

**EX010.** Quando revelam informações sobre a saúde, como ao serem usados para avaliar o condicionamento.

**EX011.** Aluno, finalidade, versão do texto, data e situação.

**EX012.** As aulas precisam só de uma faixa etária; a data completa fica onde os contratos precisam dela.

**EX013.** Sim, a perda acidental de dados pessoais pode ser uma violação.

**EX014.** Os prazos de notificação contam a partir de quando a empresa toma conhecimento.

**EX015.** Tirar fotos de listas de alunos com celulares pessoais.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da Resolução CD/ANPD nº 15, de 24 de abril de 2024, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Brasil. Agência Nacional de Proteção de Dados. (2024). *Resolução CD/ANPD nº 15, de 24 de abril de 2024 — Aprova o Regulamento de Comunicação de Incidente de Segurança*. Diário Oficial da União. <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
- European Data Protection Board. (2020). *Guidelines 3/2019 on processing of personal data through video devices* (Version 2.0, adopted 29 January 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-32019-on-processing-of-personal-data-through-video-devices_en>
- European Data Protection Board. (2023). *Guidelines 01/2022 on data subject rights — Right of access* (Version 2.0 adopted 28 March 2023; Version 2.1 with minor corrections, 30 May 2024). <https://www.edpb.europa.eu/documents/guideline/guidelines-012022-on-data-subject-rights-right-of-access_en>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO/IEC. (2025). *ISO/IEC 27701:2025 Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance* (2nd ed., replaces the 2019 edition). <https://www.iso.org/standard/27701>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
