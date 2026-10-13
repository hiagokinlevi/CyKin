# Privacidade e Proteção de Dados: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 073, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 30 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3; os capítulos 11–30 (EX031–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

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

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operacionais e virtualização

### Objetivos de aprendizagem

Você vai (1) proteger os computadores das unidades; (2) entender as máquinas virtuais e o isolamento; (3) gerir os dados guardados localmente.

### 6.1 Computadores das unidades

Os computadores da recepção rodam o software de reservas e da catraca. Aisha encontra contas de administrador compartilhadas e exportações de alunos salvas nas pastas de downloads. Recomenda contas individuais, a retirada dos direitos de administrador da equipe da recepção e a limpeza automática dos downloads. Descobre ainda que o software de reservas grava toda noite uma exportação completa dos alunos numa pasta temporária que ninguém esvazia. O fornecedor confirma que a pasta pode ser limpa automaticamente, e Aisha pede que isso seja o padrão em todas as unidades, em vez de depender da memória de cada gerente.

### 6.2 Máquinas virtuais

A sede da Quayside roda vários serviços em máquinas virtuais na nuvem. Aisha aprende que as máquinas virtuais isolam as cargas de trabalho, mas compartilham os hosts. Ela confere que o banco de matrículas roda em máquina virtual própria, com acesso de rede restrito, o que limita a propagação de um comprometimento. Ao revisar as regras do firewall da nuvem, encontra uma que permite a qualquer endereço da rede da sede alcançar a porta do banco, e a restringe aos dois servidores de aplicação que precisam dela. Ela explica que o isolamento só funciona se as regras de rede corresponderem ao desenho, e que as regras tendem a se alargar com o tempo.

### 6.3 Dados locais

Aisha procura cópias locais de dados de alunos nos computadores das unidades e encontra planilhas antigas em três delas. Trabalha com os gerentes para excluí-las e usar o sistema central. Observa que as cópias locais escapam das regras de retenção e dos controles de acesso. Para entender por que as cópias existiam, ela pergunta aos gerentes, que explicam que o sistema central ficava lento nas noites de segunda-feira e eles guardavam listas para consultas rápidas. Aisha relata o problema de desempenho à TI, porque excluir as cópias sem corrigir a causa só faria surgir cópias novas em poucas semanas.

### 6.4 Atualizações

Aisha confere a situação das atualizações e encontra dois computadores de unidade meses atrasados. Ela configura as atualizações automáticas. O Sr. Reilly observa que máquinas sem correções são uma rota frequente de ataque e que aplicar as correções é uma medida básica pelo artigo 32. Ela lista o software de cada computador e encontra um visualizador de documentos antigo, com vulnerabilidades conhecidas, que é removido porque ninguém o usa. Ela registra a situação das atualizações no inventário, para comparação futura, e pede à TI um relatório mensal de qualquer computador com mais de trinta dias de atraso.

### Exemplo resolvido

Aisha remove as contas de administrador compartilhadas, isola a máquina virtual do banco de matrículas, exclui as planilhas locais antigas e ativa as atualizações automáticas.

> **Caso sintético.** Os computadores são sintéticos; o artigo 32 do GDPR é real.

### Erros e limites

Atualizações automáticas podem quebrar o software das unidades; teste antes.

### Exercícios

- **EX016 — Limpeza dos downloads.** Por que limpar as pastas de downloads dos computadores da recepção? *Rubrica:* 3 = as exportações salvas contêm dados de alunos;; 2 = menciona exportações;; 1 = nada;; 0 = nenhuma.
- **EX017 — Isolamento da máquina virtual.** Por que dar ao banco de matrículas uma máquina virtual própria? *Rubrica:* 3 = o isolamento limita a propagação de um comprometimento;; 2 = menciona isolamento;; 1 = nada;; 0 = nenhuma.
- **EX018 — Risco das cópias locais.** Por que as planilhas locais são arriscadas? *Rubrica:* 3 = escapam da retenção e dos controles de acesso;; 2 = menciona controle;; 1 = nada;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Fundamentos de identidade e acesso

### Objetivos de aprendizagem

Você vai (1) desenhar perfis de acesso para a equipe das unidades e da sede; (2) gerir os desligamentos; (3) aplicar a autenticação multifator.

### 7.1 Perfis

Aisha desenha os perfis: recepção, personal trainer, gerente de unidade, suporte da sede, marketing e TI. Os personal trainers veem as reservas e os dados de treino dos seus alunos; a recepção vê reservas e situação da matrícula; o marketing vê preferências, mas não dados de treino. Ela documenta por que cada perfil precisa do seu acesso e testa o rascunho com cada grupo. Os trainers lembram que às vezes substituem colegas e precisam de acesso temporário a esses alunos. Aisha acrescenta uma permissão de substituição que expira depois da aula, em vez de abrir todos os alunos aos trainers.

### 7.2 Desligamentos

As academias têm alta rotatividade de pessoal. Aisha encontra quarenta contas ativas de ex-funcionários. Ela rastreia como surgiram: os gerentes criavam as contas diretamente, mas ninguém avisava a TI quando alguém saía, e o RH usava um sistema separado. Ela liga a remoção das contas ao processo de desligamento do RH, de modo que a data de saída registrada no RH agora desativa a conta automaticamente, e roda uma verificação mensal que compara as contas ativas com a lista do RH e informa qualquer diferença ao gerente da unidade. Ela observa que contas esquecidas são uma rota comum de uso indevido.

### 7.3 Autenticação multifator

Aisha recomenda a autenticação multifator para as contas da sede e dos gerentes, que podem exportar listas de alunos. As contas da recepção, em telas compartilhadas, usam sessões curtas e login por crachá. Os gerentes temem que os passos extras atrasem os turnos movimentados. Aisha faz um teste de duas semanas numa unidade com um aplicativo autenticador e descobre que os gerentes entram só algumas vezes por dia, então o atraso é pequeno. O direito de exportar é a principal razão do controle, porque uma exportação pode copiar milhares de alunos em segundos, e é esse o risco que se quer reduzir.

### 7.4 Revisões

Aisha implanta revisões trimestrais de acesso para os gerentes das unidades. Cada gerente recebe a lista das contas da sua unidade, com perfis e datas do último acesso, e precisa confirmar ou corrigir cada uma. A primeira revisão corrige vinte e três contas, entre elas trainers com direitos de recepção, um funcionário da limpeza com conta de reservas e dois gerentes que tinham sido transferidos para outras unidades. Aisha guarda as listas assinadas e datadas como evidência de que a revisão foi feita, o que sustenta a responsabilização pelo artigo 5(2) do GDPR e pelo art. 6º, X, da LGPD.

### Exemplo resolvido

Aisha define seis perfis, remove quarenta contas de ex-funcionários ligando-as ao RH, acrescenta a autenticação multifator para quem exporta listas e conduz revisões trimestrais.

> **Caso sintético.** As contas são sintéticas; o artigo 5(2) do GDPR e o art. 6º, X, da LGPD são reais.

### Erros e limites

Revisões feitas por gerentes ocupados podem virar carimbo; confira as respostas por amostragem.

### Exercícios

- **EX019 — Acesso dos trainers.** O que os personal trainers podem ver? *Rubrica:* 3 = reservas e dados de treino dos seus alunos;; 2 = menciona alunos;; 1 = todos os alunos;; 0 = nenhuma.
- **EX020 — Ex-funcionários.** Quantas contas de ex-funcionários estavam ativas? *Rubrica:* 3 = quarenta;; 2 = aproximadamente;; 1 = nenhuma;; 0 = nenhuma.
- **EX021 — Alcance da autenticação multifator.** Que contas recebem a autenticação multifator? *Rubrica:* 3 = sede e gerentes que podem exportar listas;; 2 = menciona gerentes;; 1 = todas;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Fundamentos de arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) aplicar a segmentação e o menor privilégio; (2) posicionar controles em volta dos dados sensíveis; (3) documentar uma arquitetura.

### 8.1 Segmentos

Aisha desenha a arquitetura da Quayside em segmentos: aplicativo e site públicos, serviços da sede, redes das unidades e CFTV. Ela coloca o banco de matrículas e o repositório de frequência cardíaca num segmento restrito e explica à TI a razão de cada fronteira. Os serviços públicos ficam expostos à internet e são os mais atacados, então não devem alcançar diretamente os repositórios de alunos. As redes das unidades ficam fisicamente expostas em prédios abertos ao público. O CFTV produz grandes volumes de imagens de pessoas identificáveis. Cada segmento tem regras que descrevem exatamente que tráfego pode passar para outro.

### 8.2 Controles em volta dos dados

O acesso ao repositório de frequência cardíaca passa por uma API que confere o perfil e a finalidade. As exportações exigem aprovação, e as de listas grandes vão para o encarregado. A criptografia protege os dados em repouso, com chaves geridas pelo serviço de chaves da nuvem e acesso restrito a dois administradores. A API registra cada requisição com o perfil e a finalidade declarada, para que padrões incomuns possam ser encontrados depois, como um trainer lendo centenas de perfis numa noite. Aisha explica que as camadas de controles reduzem a dependência de qualquer medida isolada.

### 8.3 Fornecedores no diagrama

Aisha inclui os fornecedores: o processador de pagamentos, o chat de atendimento, a ferramenta de análise e o fornecedor das cintas cardíacas. Ela marca quais recebem dados pessoais e se há contrato. O mapeamento mostra que o fornecedor das cintas recebe as leituras brutas de frequência cardíaca, e não só as zonas, e que seu contrato não fala de retenção; Aisha leva a lacuna à equipe de compras. Ela também descobre que o fornecedor do chat guarda as transcrições por cinco anos por padrão, muito mais do que a Quayside precisa para o atendimento, e pede noventa dias.

### 8.4 Documentação

Aisha escreve um documento curto de arquitetura com o diagrama, os fluxos de dados e os controles, em linguagem simples e com um glossário para termos como segmento, API e criptografia em repouso. Ela inclui uma seção com as fraquezas conhecidas e as correções planejadas, para que os leitores não suponham que o desenho é perfeito. O documento tem número de versão e um responsável na TI, que vai atualizá-lo depois de cada mudança importante. O Sr. Reilly observa que a documentação ajuda os novos funcionários e os auditores a entender como os dados dos alunos são protegidos.

### Exemplo resolvido

Aisha segmenta a arquitetura da Quayside, coloca o repositório de frequência cardíaca atrás de uma API que confere perfis, mapeia os fornecedores e documenta o desenho.

> **Caso sintético.** A arquitetura é sintética.

### Erros e limites

Os diagramas se afastam da realidade; revise-os depois de mudanças.

### Exercícios

- **EX022 — Segmento restrito.** Que repositórios ficam no segmento restrito? *Rubrica:* 3 = o banco de matrículas e o repositório de frequência cardíaca;; 2 = um;; 1 = nenhum;; 0 = nenhuma.
- **EX023 — Camadas de controles.** Por que usar várias camadas de controles? *Rubrica:* 3 = reduz a dependência de uma medida isolada;; 2 = menciona camadas;; 1 = uma basta;; 0 = nenhuma.
- **EX024 — Mapeamento dos fornecedores.** O que Aisha marca para cada fornecedor? *Rubrica:* 3 = se recebe dados pessoais e se há contrato;; 2 = um;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) escolher métricas de privacidade; (2) coletar evidências de forma confiável; (3) relatar os resultados.

### 9.1 Métricas

Aisha propõe quatro métricas: contas de ex-funcionários, cópias locais encontradas, pedidos de titulares respondidos no prazo e imagens de CFTV além do prazo de retenção. Cada uma tem uma definição e uma fonte de dados. Ela evita métricas fáceis de contar, mas que dizem pouco, como o número de políticas publicadas. Para cada métrica, escreve como é calculada, quem fornece os dados, com que frequência é medida e que valor seria preocupante. Por exemplo, qualquer conta de ex-funcionário ativa por mais de dois dias já é motivo de preocupação e gera uma ação imediata.

### 9.2 Evidências

Sempre que possível, Aisha coleta evidências por relatórios dos sistemas, e não por questionários, porque os relatórios são mais confiáveis. Um questionário pergunta aos gerentes se removeram os desligados, mas eles podem lembrar errado ou responder com otimismo; um relatório do sistema lista as contas diretamente. Quando só um questionário é possível, como na conscientização da equipe, ela o combina com um pequeno teste, como pedir a um funcionário que mostre onde fica o formulário de comunicação. Ela guarda as evidências com datas e registra como cada uma foi produzida, o que evita conclusões exageradas.

### 9.3 Linha de base

Aisha registra uma linha de base: quarenta contas esquecidas, três unidades com planilhas locais e uma situação desconhecida da retenção do CFTV, que ela trata como lacuna a medir, começando por uma unidade. Anota a data e o método de cada valor, porque uma mudança posterior de método poderia parecer uma melhoria. Registra também dois valores que espera ver subir no início, as comunicações de incidentes e os pedidos de acesso, explicando que uma conscientização maior pode fazer os números crescerem antes de os riscos caírem. Sem essa ressalva, a direção poderia ler a alta como piora.

### 9.4 Relatórios

Aisha reporta todo mês ao encarregado da Quayside. Cada relatório cabe numa página: uma tabela com o valor atual, o anterior e a linha de base de cada métrica, um comentário curto sobre cada mudança, uma lista de ações com responsáveis e as fontes dos dados. O encarregado o encaminha ao diretor de operações. Aisha guarda os relatórios numa pasta datada, para que as tendências possam ser revistas depois. O Sr. Reilly observa que medir desde o início é o que permite mostrar o progresso mais tarde, porque sem linha de base qualquer melhoria vira apenas uma afirmação sem prova.

### Exemplo resolvido

Aisha define quatro métricas, prefere as evidências dos sistemas, registra uma linha de base que inclui os desconhecidos e reporta todo mês.

> **Caso sintético.** As métricas são sintéticas.

### Erros e limites

As métricas podem deixar escapar o que não é medido.

### Exercícios

- **EX025 — Fonte das evidências.** Por que preferir relatórios dos sistemas a questionários? *Rubrica:* 3 = são mais confiáveis;; 2 = menciona confiabilidade;; 1 = questionários;; 0 = nenhuma.
- **EX026 — CFTV desconhecido.** Como Aisha trata a situação desconhecida do CFTV? *Rubrica:* 3 = como uma lacuna a medir;; 2 = menciona lacuna;; 1 = ignora;; 0 = nenhuma.
- **EX027 — Valor da linha de base.** Por que registrar uma linha de base? *Rubrica:* 3 = para mostrar o progresso mais tarde;; 2 = menciona comparação;; 1 = nada;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Privacidade e proteção de dados: orientação

### Objetivos de aprendizagem

Você vai (1) explicar os princípios centrais da proteção de dados; (2) identificar as bases legais numa academia; (3) reconhecer os dados de categorias especiais.

### 10.1 Princípios

Aisha estuda os princípios do artigo 5 do GDPR e do art. 6º da LGPD e aplica cada um à Quayside. A limitação da finalidade significa que as imagens de CFTV gravadas para segurança não servem para vigiar a produtividade da equipe. A minimização significa que o aplicativo pede só os dados necessários aos treinos. A exatidão significa que os alunos podem corrigir seus dados no aplicativo. A limitação da conservação significa que as imagens e as contas inativas são excluídas no prazo. A responsabilização significa que a Quayside precisa conseguir demonstrar a conformidade, e é por isso que Aisha guarda evidências de cada verificação.

### 10.2 Bases legais

O tratamento das matrículas se apoia no contrato; os registros de pagamento, na obrigação legal; os e-mails de marketing, no consentimento; o CFTV, no legítimo interesse. Aisha aprende que cada finalidade precisa da sua base. Ela observa que o consentimento não serve para as matrículas, porque o aluno não pode recusar o tratamento e continuar matriculado; o contrato se encaixa melhor. Para o CFTV, o legítimo interesse exige um teste de ponderação que mostre que as necessidades de segurança superam a intrusão sobre alunos e equipe. Ela redige esse teste com o encarregado e registra o raciocínio.

### 10.3 Categorias especiais

Os dados de frequência cardíaca usados para avaliar a saúde podem ser dados de saúde e exigir uma condição do artigo 9 do GDPR, como o consentimento explícito; na LGPD, são dados pessoais sensíveis, sujeitos ao art. 11. Aisha observa que a Quayside precisa decidir e documentar isso com cuidado. Ela discute a diferença entre as leituras mostradas durante uma aula e um histórico longo usado para sugerir dias de descanso ou detectar ritmos irregulares; o segundo revela claramente informações de saúde. A Quayside decide tratar todos os dados de frequência cardíaca armazenados como dados de saúde, a escolha mais protetiva e mais simples de explicar.

### 10.4 Direitos

Os alunos têm direitos de acesso, retificação, eliminação, limitação, portabilidade e oposição. Aisha lista como cada um seria atendido nos sistemas da Quayside, porque os direitos precisam ser práticos, e não só declarados. Para o acesso, uma lista de verificação cobre todos os sistemas. Para a retificação, os alunos editam os dados no aplicativo. Para a eliminação, um processo de exclusão da conta alcança todos os sistemas, com exceções documentadas, como dívidas. Para a oposição, o aluno interrompe o marketing com um toque. Ela observa que o art. 18 da LGPD daria direitos semelhantes aos alunos se a Quayside operasse no Brasil.

### Exemplo resolvido

Aisha aplica os princípios à Quayside, atribui bases legais por finalidade, sinaliza os dados de frequência cardíaca como possíveis dados de saúde e lista o atendimento aos direitos.

> **Caso sintético.** As escolhas da Quayside são sintéticas; os artigos 5 e 9 do GDPR e os arts. 6º, 11 e 18 da LGPD são reais.

### Erros e limites

A escolha da base legal depende dos fatos; revise-a com o jurídico.

### Exercícios

- **EX028 — Finalidade do CFTV.** Por que as imagens de CFTV não podem ser usadas para a produtividade da equipe? *Rubrica:* 3 = limitação da finalidade;; 2 = menciona finalidade;; 1 = é permitido;; 0 = nenhuma.
- **EX029 — Base do marketing.** Que base legal os e-mails de marketing usam? *Rubrica:* 3 = consentimento;; 2 = correta;; 1 = contrato;; 0 = nenhuma.
- **EX030 — Condição para a frequência cardíaca.** Que condição os dados de saúde de frequência cardíaca podem exigir? *Rubrica:* 3 = consentimento explícito pelo artigo 9;; 2 = menciona consentimento;; 1 = nenhuma;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). Aisha Bello, o Sr. Tom Reilly, o Lindon Technical Institute, a Quayside Fitness e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX016.** Guardavam exportações de alunos fora dos controles centrais.

**EX017.** Para isolá-lo de serviços menos críticos.

**EX018.** Escapam das regras centrais de retenção e dos controles de acesso.

**EX019.** Reservas e dados de treino dos seus próprios alunos.

**EX020.** Quarenta.

**EX021.** Contas da sede e dos gerentes com direito de exportação.

**EX022.** O banco de matrículas e o repositório de frequência cardíaca.

**EX023.** Para que uma única falha não exponha os dados.

**EX024.** Se recebe dados pessoais e se existe contrato.

**EX025.** Os relatórios dos sistemas são mais confiáveis que as respostas declaradas.

**EX026.** Como uma lacuna de medição a fechar.

**EX027.** Para que as melhorias posteriores possam ser demonstradas.

**EX028.** As imagens coletadas para segurança não podem ser reaproveitadas para uma finalidade incompatível.

**EX029.** Consentimento.

**EX030.** Uma condição do artigo 9, como o consentimento explícito.

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
