# Privacidade e Proteção de Dados: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 073, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–30 de 30 têm texto didático escrito à mão; os exercícios EX001–EX090 têm resoluções correspondentes com rubricas de 0 a 3; os cinco laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

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
- **EX002 — Lacuna do CFTV.** Que lacuna de governança o inventário mostrou? *Rubrica:* 3 = nenhum responsável central pelos gravadores de CFTV;; 2 = menciona CFTV;; 1 = vago;; 0 = nenhuma.
- **EX003 — Prática versus política.** Por que os tecnólogos importam para a privacidade? *Rubrica:* 3 = veem como os sistemas se comportam e podem conferir a prática diante da política;; 2 = menciona sistemas;; 1 = vago;; 0 = nenhuma.

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
- **EX014 — Rapidez da comunicação.** Por que a equipe precisa comunicar depressa? *Rubrica:* 3 = o prazo de 72 horas começa quando a Quayside toma conhecimento;; 2 = menciona prazo;; 1 = vago;; 0 = nenhuma.
- **EX015 — Fotografar listas.** Que hábito arriscado o guia proíbe? *Rubrica:* 3 = fotografar listas de alunos com celulares pessoais;; 2 = menciona celulares;; 1 = vago;; 0 = nenhuma.

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

- **EX016 — Limpeza dos downloads.** Por que limpar as pastas de downloads dos computadores da recepção? *Rubrica:* 3 = as exportações salvas contêm dados de alunos;; 2 = menciona exportações;; 1 = vago;; 0 = nenhuma.
- **EX017 — Isolamento da máquina virtual.** Por que dar ao banco de matrículas uma máquina virtual própria? *Rubrica:* 3 = o isolamento limita a propagação de um comprometimento;; 2 = menciona isolamento;; 1 = vago;; 0 = nenhuma.
- **EX018 — Risco das cópias locais.** Por que as planilhas locais são arriscadas? *Rubrica:* 3 = escapam da retenção e dos controles de acesso;; 2 = menciona controle;; 1 = vago;; 0 = nenhuma.

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
- **EX020 — Ex-funcionários.** Quantas contas de ex-funcionários estavam ativas? *Rubrica:* 3 = quarenta;; 2 = aproximadamente;; 1 = vago;; 0 = nenhuma.
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

- **EX022 — Segmento restrito.** Que repositórios ficam no segmento restrito? *Rubrica:* 3 = o banco de matrículas e o repositório de frequência cardíaca;; 2 = um;; 1 = vago;; 0 = nenhuma.
- **EX023 — Camadas de controles.** Por que usar várias camadas de controles? *Rubrica:* 3 = reduz a dependência de uma medida isolada;; 2 = menciona camadas;; 1 = uma basta;; 0 = nenhuma.
- **EX024 — Mapeamento dos fornecedores.** O que Aisha marca para cada fornecedor? *Rubrica:* 3 = se recebe dados pessoais e se há contrato;; 2 = um;; 1 = vago;; 0 = nenhuma.

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
- **EX027 — Valor da linha de base.** Por que registrar uma linha de base? *Rubrica:* 3 = para mostrar o progresso mais tarde;; 2 = menciona comparação;; 1 = vago;; 0 = nenhuma.

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
- **EX029 — Base do marketing.** Que base legal os e-mails de marketing usam? *Rubrica:* 3 = consentimento;; 2 = parcialmente correta;; 1 = contrato;; 0 = nenhuma.
- **EX030 — Condição para a frequência cardíaca.** Que condição os dados de saúde de frequência cardíaca podem exigir? *Rubrica:* 3 = consentimento explícito pelo artigo 9;; 2 = menciona consentimento;; 1 = vago;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Privacidade e proteção de dados: ativos e contexto

### Objetivos de aprendizagem

Você vai (1) classificar os ativos de dados pessoais; (2) entender as expectativas dos alunos; (3) relacionar o contexto ao uso adequado.

### 11.1 Classes de ativos

Aisha classifica os ativos: identidade, pagamento, treino, frequência cardíaca, CFTV e marketing, e avalia a sensibilidade e o volume de cada um. Os dados de identidade incluem nomes, e-mails, telefones e as fotos das carteirinhas. Os de pagamento incluem dados bancários e tokens de cartão. Os de treino incluem aulas e exercícios. A frequência cardíaca vem das cintas. O CFTV cobre entradas e salas de musculação. O marketing inclui preferências e respostas a campanhas. Ela classifica a frequência cardíaca e o CFTV como os mais sensíveis, e identidade e treino como os maiores em volume; pagamento fica em terceiro, porque os tokens ficam com o processador.

### 11.2 Expectativas

Aisha pergunta a vinte voluntários sobre suas expectativas. São alunos que responderam a um aviso em duas unidades, e as perguntas curtas tratam de para onde os dados vão, quem pode vê-los e por quanto tempo são guardados. A maioria espera que os dados de treino fiquem no aplicativo e sejam excluídos quando saírem da academia. Vários se surpreendem ao saber que as telas das aulas mostram zonas cardíacas com o primeiro nome, e dois dizem que deixaram de usar as cintas por isso. Ela registra as opiniões de forma anônima e as leva para o trabalho de análise de riscos do capítulo seguinte.

### 11.3 Contexto

A integridade contextual pergunta se um fluxo de informação respeita as normas do contexto em que os dados foram compartilhados. Os alunos compartilham a frequência cardíaca com os trainers para treinar melhor. Um fluxo para anunciantes serve a outra finalidade e rompe essas normas, mesmo que um aviso o mencione, e as expectativas dos alunos confirmam isso. Aisha usa esse referencial para explicar à equipe do aplicativo por que alguns fluxos lícitos ainda parecem errados aos alunos, e por que a confiança depende de respeitar o contexto, e não apenas de cumprir as exigências formais de transparência.

### 11.4 Prioridades

Aisha ordena os ativos combinando a sensibilidade com a amplitude da exposição. A frequência cardíaca é sensível e chega a fornecedores e telas. As imagens de CFTV são sensíveis e acessadas pelos gerentes locais sem registro. Os dados de pagamento são sensíveis, mas já protegidos pelo processador de pagamentos. A frequência cardíaca e o CFTV ficam, portanto, em primeiro lugar. Essa ordem orienta quais fluxos de dados ela examina primeiro no capítulo seguinte e quais controles proporá depois. O Sr. Reilly observa que o contexto ajuda a decidir onde a proteção importa mais.

### Exemplo resolvido

Aisha classifica seis tipos de ativos, levanta as expectativas dos alunos, aplica a integridade contextual aos dados de frequência cardíaca e coloca a frequência cardíaca e o CFTV no topo.

> **Caso sintético.** A pesquisa é sintética; Nissenbaum (2004) é real.

### Erros e limites

Vinte voluntários não são representativos.

### Exercícios

- **EX031 — Classes de ativos.** Cite quatro classes de ativos. *Rubrica:* 3 = identidade, pagamento, treino, frequência cardíaca, CFTV, marketing;; 2 = três;; 1 = vago;; 0 = nenhuma.
- **EX032 — Expectativa dos alunos.** O que a maioria dos voluntários esperava sobre os dados de treino? *Rubrica:* 3 = ficam no aplicativo e são excluídos na saída;; 2 = uma parte;; 1 = vago;; 0 = nenhuma.
- **EX033 — Prioridades.** Que ativos ficam no topo? *Rubrica:* 3 = frequência cardíaca e CFTV;; 2 = um;; 1 = errado;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Privacidade e proteção de dados: fluxos de dados

### Objetivos de aprendizagem

Você vai (1) inspecionar os SDKs embutidos num aplicativo; (2) conferir a cobertura pelo aviso e pelos contratos; (3) recomendar mudanças.

### 12.1 SDKs

O aplicativo da Quayside embute cinco kits de desenvolvimento de software (SDKs). Um SDK é uma biblioteca fornecida por outra empresa e incluída no aplicativo para oferecer uma funcionalidade, como relatórios de falhas ou chat, e pode coletar dados sem que a equipe do aplicativo perceba. Aisha gera uma versão de teste, entra com alunos sintéticos e registra o tráfego de rede enquanto usa treinos, aulas e chat. Depois lista cada SDK, os campos que ele recebe e se o aviso de privacidade e os contratos o cobrem, para comparar o que o aplicativo diz com o que de fato envia.

### 12.2 Resultados

O laboratório mostra que os SDKs de relatório de falhas, análise de uso e chat de atendimento estão cobertos pelo aviso e pelos contratos. A rede de anúncios recebe o identificador de publicidade, a zona cardíaca e a localização, e não está no aviso nem tem contrato. O login social não tem contrato. A zona cardíaca deriva de dados de saúde, e enviá-la com identificador de publicidade e localização permite montar um perfil do condicionamento e dos deslocamentos do aluno; é o achado mais grave. Os desenvolvedores contam que o SDK veio com uma funcionalidade de promoções dois anos antes e ninguém revisou sua coleta.

### 12.3 Recomendações

Aisha recomenda remover o SDK da rede de anúncios, assinar um contrato com o provedor de login social e atualizar o aviso de privacidade. Recomenda também uma regra: nenhum SDK entra sem revisão de privacidade. Cada recomendação tem responsável e data: a equipe do aplicativo remove o SDK, compras cuida do contrato do login social e o encarregado atualiza o aviso. Ela pede ainda à equipe do aplicativo que mantenha no repositório uma lista de todos os SDKs, com versão e finalidade, para que as revisões futuras partam de um registro exato, e não da memória de alguém.

### 12.4 Acompanhamento

A equipe do aplicativo remove o SDK de anúncios na versão seguinte. Aisha testa de novo, com as mesmas contas sintéticas e os mesmos passos, para que os resultados possam ser comparados diretamente, e confirma que nenhum dado de frequência cardíaca sai para anunciantes. O tráfego para a rede de anúncios desapareceu, e o contrato do login social é assinado em um mês. Aisha acrescenta à lista de verificação de cada versão uma pergunta simples aos desenvolvedores: esta versão acrescenta ou atualiza alguma biblioteca de terceiros que envia dados para fora do aparelho? O Sr. Reilly observa que a revisão deve se repetir a cada versão.

### Laboratório — Fluxos de dados dos SDKs e sua cobertura

```python
# Fitness app: what does each embedded SDK receive, and is it covered by the privacy notice and a contract?
sdks = [("crash reporter", ["device model", "app version"], True, True),
        ("analytics", ["member id", "screen views", "workout type"], True, True),
        ("ad network", ["advertising id", "heart rate zone", "location"], False, False),
        ("chat support", ["member id", "name", "messages"], True, True),
        ("social login", ["email", "name"], True, False)]
for name, data, notice, contract in sdks:
    issues = ([] if notice else ["not in notice"]) + ([] if contract else ["no contract"])
    health = any(d in ("heart rate zone",) for d in data)
    print(f"{name:15s} {', '.join(data):40s} {'OK' if not issues else '; '.join(issues)}{' [HEALTH DATA]' if health else ''}")
```

Execute com `python3 lab_flows.py`. Saída verificada:

```text
crash reporter  device model, app version                OK
analytics       member id, screen views, workout type    OK
ad network      advertising id, heart rate zone, location not in notice; no contract [HEALTH DATA]
chat support    member id, name, messages                OK
social login    email, name                              no contract
```

### Exemplo resolvido

Aisha descobre que a rede de anúncios recebe a zona cardíaca e a localização sem aviso nem contrato e que o login social não tem contrato, e o SDK de anúncios é removido.

> **Caso sintético.** Os SDKs são sintéticos.

### Erros e limites

A inspeção de rede pode deixar escapar dados enviados mais tarde ou em lotes.

### Exercícios

- **EX034 — Pior SDK.** Que SDK é o achado mais grave? *Rubrica:* 3 = a rede de anúncios, que recebe zona cardíaca e localização sem aviso nem contrato;; 2 = cita-o;; 1 = outro;; 0 = nenhuma.
- **EX035 — Lacuna do login social.** Que lacuna o login social tem? *Rubrica:* 3 = não tem contrato;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX036 — Regra para SDKs.** Que regra Aisha recomendou? *Rubrica:* 3 = nenhum SDK entra sem revisão de privacidade;; 2 = menciona revisão;; 1 = vago;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Privacidade e proteção de dados: cenários de risco

### Objetivos de aprendizagem

Você vai (1) escrever cenários de risco para os dados dos alunos; (2) classificar probabilidade e impacto; (3) escolher tratamentos.

### 13.1 Cenários

Aisha escreve quatro cenários: dados de frequência cardíaca vazados para anunciantes; imagens de CFTV dos corredores dos vestiários acessadas pela equipe; listas de alunos fotografadas e compartilhadas; e conta do aplicativo sequestrada. Cada cenário diz quem age, o que faz, que dados são afetados e que dano se segue. Por exemplo, uma recepcionista curiosa sobre uma vizinha vê os vídeos das chegadas dela e os compartilha, causando constrangimento e sofrimento. Escrever os cenários assim ajuda os gerentes a reconhecer os riscos nas próprias unidades, em vez de tratar a privacidade como um assunto jurídico abstrato.

### 13.2 Classificações

Aisha classifica cada cenário de um a três em probabilidade e em impacto. A probabilidade considera a frequência de eventos parecidos e a facilidade de provocá-los. O impacto considera o dano aos alunos, como sofrimento, discriminação ou perda financeira, e não só o dano à Quayside. O vazamento da frequência cardíaca tem impacto alto, porque dados de saúde podem afetar seguros ou empregos. O sequestro de conta tem probabilidade alta, porque os alunos costumam reaproveitar senhas de outros serviços. Os dois ficam, portanto, em três por três, no topo da lista, enquanto os demais cenários ficam abaixo.

### 13.3 Tratamentos

Os tratamentos incluem a revisão de SDKs, o registro de acessos ao CFTV, a orientação à equipe e o login multifator opcional no aplicativo. Aisha escolhe tratamentos que reduzam a probabilidade ou o impacto. A revisão de SDKs reduz a chance de novos vazamentos. O registro de acessos ao CFTV dissuade o uso indevido e o torna detectável. A orientação reduz as listas fotografadas. O login multifator protege as contas. Ela registra o risco residual depois de cada tratamento e aceita que algum risco permanece, como alunos que escolhem senhas fracas; o do vazamento da frequência cardíaca cai de alto para médio.

### 13.4 Responsáveis

Cada tratamento recebe um responsável e uma data. Os responsáveis são pessoas com autoridade para agir, e não comitês: o líder do aplicativo cuida da revisão de SDKs e das mudanças de login; o diretor de operações, do registro de acessos ao CFTV; o gerente de treinamento, da orientação à equipe. As datas são realistas e combinadas com os responsáveis. Aisha revisa a lista todo mês e informa os itens atrasados ao encarregado, que pode escalá-los à liderança. O Sr. Reilly observa que os cenários ajudam quem não é especialista a entender os riscos e a agir.

### Exemplo resolvido

Aisha escreve quatro cenários, classifica o vazamento da frequência cardíaca e o sequestro de conta como os mais altos e atribui tratamentos com responsáveis.

> **Caso sintético.** Os cenários são sintéticos.

### Erros e limites

As classificações são subjetivas; discuta-as com os colegas.

### Exercícios

- **EX037 — Cenários mais altos.** Que cenários ficam no topo? *Rubrica:* 3 = vazamento da frequência cardíaca e sequestro de conta;; 2 = um;; 1 = vago;; 0 = nenhuma.
- **EX038 — Tratamento do CFTV.** Que tratamento enfrenta o uso indevido do CFTV? *Rubrica:* 3 = registro de acessos;; 2 = menciona registro;; 1 = vago;; 0 = nenhuma.
- **EX039 — Valor dos cenários.** Por que usar cenários? *Rubrica:* 3 = ajudam quem não é especialista a entender os riscos;; 2 = menciona compreensão;; 1 = vago;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Privacidade e proteção de dados: métodos I

### Objetivos de aprendizagem

Você vai (1) testar a completude da resposta a um pedido de acesso; (2) encontrar os sistemas esquecidos; (3) melhorar o processo.

### 14.1 O teste

Aisha testa o processo de pedidos de acesso da Quayside com um aluno sintético. Ela cria um aluno que usa o aplicativo, reserva aulas, conversa com o atendimento, aparece numa entrada do índice do CFTV e recebe marketing. Depois envia um pedido de acesso pelo canal normal e espera a resposta que um aluno real receberia, para ver o processo como os alunos o vivem, e não como a equipe o descreve. A primeira exportação busca no sistema de matrículas, no perfil do aplicativo e nos pagamentos; Aisha a compara com todos os sistemas que guardam dados desse aluno.

### 14.2 Resultados

O laboratório mostra que a exportação cobriu 47 de 287 registros, 16%, em três de sete sistemas. Ficaram de fora o histórico de treinos, o índice do CFTV, o chat de atendimento e o marketing. O artigo 15 do GDPR, como o art. 18, II, da LGPD, garante acesso a todos os dados pessoais tratados. A equipe buscou nos sistemas que conhecia melhor e esqueceu os outros, porque nenhuma lista dizia onde ficavam os dados dos alunos. O histórico de treinos, o maior conjunto, faltou porque fica num banco separado do aplicativo; o índice do CFTV e as transcrições do chat estavam com fornecedores, a quem ninguém tinha pedido nada.

### 14.3 Melhoria

Aisha cria, a partir do inventário, uma lista de verificação de sistemas e atribui um responsável a cada busca. As Diretrizes 01/2022 do EDPB ajudam a definir o que precisa ser incluído. A lista traz cada sistema, o método de busca, o responsável, o tempo esperado e as necessidades de ocultação: as imagens de CFTV precisam ter outras pessoas desfocadas, e as transcrições do chat podem citar funcionários. A equipe agora registra quais sistemas foram pesquisados em cada pedido. Esse registro, guardado por dois anos, também mostra à autoridade, se ela perguntar, como a Quayside cumpre sua obrigação.

### 14.4 Novo teste

Depois das mudanças, um segundo aluno sintético recebe uma resposta que cobre os sete sistemas e chega dentro do prazo de um mês do GDPR; na LGPD, o art. 19, II, fixa quinze dias para a declaração completa. A equipe percebe que as buscas nos fornecedores são as mais demoradas e passa a iniciá-las no primeiro dia. Aisha recomenda repetir o teste duas vezes por ano e sempre que um sistema novo entrar, porque os sistemas novos são o lugar mais provável para as lacunas reaparecerem. O Sr. Reilly observa que testes de ponta a ponta revelam lacunas que os documentos de procedimento escondem.

### Laboratório — Completude da exportação de um pedido de acesso

```python
# Access request completeness: which systems hold data for a synthetic member, and which did the first export search?
holding = {"membership": 14, "app profile": 9, "workout history": 220, "CCTV index": 3, "chat support": 6, "marketing": 11, "payments": 24}
searched = {"membership", "app profile", "payments"}
found = sum(v for k, v in holding.items() if k in searched); total = sum(holding.values())
for k, v in holding.items(): print(f"{k:16s} records {v:4d} {'searched' if k in searched else 'MISSED'}")
print(f"first export covered {found} of {total} records ({found/total:.0%}) in {len(searched)} of {len(holding)} systems")
```

Execute com `python3 lab_sar.py`. Saída verificada:

```text
membership       records   14 searched
app profile      records    9 searched
workout history  records  220 MISSED
CCTV index       records    3 MISSED
chat support     records    6 MISSED
marketing        records   11 MISSED
payments         records   24 searched
first export covered 47 of 287 records (16%) in 3 of 7 systems
```

### Exemplo resolvido

Aisha descobre que a primeira exportação cobriu 47 de 287 registros (16%) em três de sete sistemas, acrescenta uma lista de verificação baseada no inventário e confirma a cobertura completa no novo teste.

> **Caso sintético.** O aluno é sintético; o artigo 15 do GDPR, os arts. 18 e 19 da LGPD e as Diretrizes 01/2022 do EDPB são reais.

### Erros e limites

As imagens de CFTV exigem a ocultação de outras pessoas antes da entrega.

### Exercícios

- **EX040 — Cobertura.** Que parcela dos registros a primeira exportação cobriu? *Rubrica:* 3 = 47 de 287, 16%;; 2 = aproximadamente;; 1 = errada;; 0 = nenhuma.
- **EX041 — Sistemas esquecidos.** Cite dois sistemas esquecidos. *Rubrica:* 3 = histórico de treinos, índice do CFTV, chat de atendimento, marketing;; 2 = um;; 1 = vago;; 0 = nenhuma.
- **EX042 — Correção.** O que fechou a lacuna? *Rubrica:* 3 = lista de verificação baseada no inventário, com responsáveis pelas buscas;; 2 = menciona lista;; 1 = vago;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Privacidade e proteção de dados: laboratório guiado

### Objetivos de aprendizagem

Você vai (1) conduzir com segurança um laboratório guiado de privacidade; (2) verificar a retenção do CFTV; (3) registrar os resultados.

### 15.1 Plano do laboratório

Aisha planeja um laboratório guiado sobre a retenção do CFTV numa unidade, usando um índice sintético de vídeos. A política da Quayside guarda as imagens por trinta dias, salvo se marcadas por um incidente. As Diretrizes 3/2019 do EDPB sobre dispositivos de vídeo tratam da retenção e da transparência. O índice lista a câmera, a data e a marcação de incidente de cada vídeo, mas nenhuma imagem, então o laboratório não exige assistir às gravações de pessoas reais. Aisha combina o plano com o gerente e o encarregado e escreve que resultado indicaria um problema: qualquer vídeo sem marcação com mais de trinta dias.

### 15.2 Resultados

O laboratório confere 500 vídeos. Desses, 304 têm mais de trinta dias; doze estão guardados por incidentes; 292 deveriam ter sido excluídos. O vídeo sem marcação mais antigo tem 75 dias, então a exclusão automática não está funcionando. O resultado surpreende o gerente, que acreditava que a exclusão era automática. Os vídeos marcados são esperados, já que as imagens ligadas a incidentes ficam guardadas até a resolução. A idade do vídeo mais antigo sugere que a exclusão parou cerca de seis semanas antes da verificação, e o log do firmware confirma a data exata da interrupção.

### 15.3 Correção

O gravador da unidade teve a exclusão automática desligada depois de uma atualização de firmware, que voltou várias configurações aos padrões de fábrica. Aisha religa a exclusão e acrescenta uma verificação mensal. Ela pergunta ao fornecedor se as atualizações nas outras unidades fizeram o mesmo, e ele confirma o problema num modelo de gravador. Ela confere as outras unidades com esse modelo e encontra mais duas com a exclusão desligada, corrigidas na mesma semana. Depois, pede ao fornecedor que envie as notas de atualização com antecedência, para que as configurações de privacidade sejam conferidas antes de cada atualização.

### 15.4 Registro

Aisha registra os achados e a correção: a data, o método, o resultado, a causa raiz, a correção e as verificações de acompanhamento. Ela sugere ainda que o fornecedor mude seu processo de atualização para que as configurações de privacidade sobrevivam às atualizações. A verificação mensal entra na rotina do gerente, e os resultados vão alimentar o monitoramento que ela construirá mais adiante no curso para as quarenta unidades, com esta unidade servindo de modelo para as demais. O Sr. Reilly observa que os laboratórios guiados mostram como uma verificação simples revela uma falha silenciosa.

### Laboratório — Imagens de CFTV além do prazo de retenção

```python
# CCTV footage retention: clips older than 30 days must be deleted unless flagged for an incident.
import random
r = random.Random(8)
clips = [(r.randint(0, 75), r.random() < 0.04) for _ in range(500)]
over = [a for a, f in clips if a > 30 and not f]; held = [a for a, f in clips if a > 30 and f]
print(f"clips {len(clips)}; older than 30 days {len(over)+len(held)}; held for incidents {len(held)}; to delete {len(over)}")
print(f"oldest unflagged clip {max(over)} days")
```

Execute com `python3 lab_cctv.py`. Saída verificada:

```text
clips 500; older than 30 days 304; held for incidents 12; to delete 292
oldest unflagged clip 75 days
```

### Exemplo resolvido

Aisha encontra 292 de 500 vídeos com mais de trinta dias (o mais antigo com 75 dias), liga isso à exclusão desligada por uma atualização de firmware, religa a exclusão e acrescenta uma verificação mensal.

> **Caso sintético.** Os vídeos são sintéticos; as Diretrizes 3/2019 do EDPB são reais.

### Erros e limites

O resultado de uma unidade pode não representar as quarenta.

### Exercícios

- **EX043 — Vídeos a excluir.** Quantos vídeos deveriam ser excluídos? *Rubrica:* 3 = 292;; 2 = aproximado;; 1 = errado;; 0 = nenhuma.
- **EX044 — Causa raiz.** Por que as imagens não eram excluídas? *Rubrica:* 3 = uma atualização de firmware desligou a exclusão automática;; 2 = menciona firmware;; 1 = vago;; 0 = nenhuma.
- **EX045 — Verificação contínua.** Que controle contínuo Aisha acrescentou? *Rubrica:* 3 = uma verificação mensal da retenção;; 2 = menciona mensal;; 1 = vago;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Privacidade e proteção de dados: métodos II

### Objetivos de aprendizagem

Você vai (1) realizar uma avaliação de impacto sobre a proteção de dados para uma nova funcionalidade; (2) consultar as partes interessadas; (3) registrar as decisões.

### 16.1 A funcionalidade

A Quayside planeja uma funcionalidade que usa as tendências da frequência cardíaca para sugerir dias de descanso. Aisha reconhece que o tratamento sistemático de dados de saúde pode exigir uma DPIA pelo artigo 35 do GDPR; na LGPD, o equivalente é o relatório de impacto à proteção de dados pessoais do art. 38. O guia WP248 lista critérios como dados sensíveis e tratamento em grande escala. A equipe de produto vê a funcionalidade como mera conveniência, mas Aisha mostra que ela analisa dados de saúde de milhares de alunos por longos períodos e faz sugestões que podem influenciar comportamentos. Dois critérios se aplicam claramente, o que em geral exige a avaliação antes do desenvolvimento.

### 16.2 Avaliação

Aisha descreve o tratamento, avalia a necessidade e a proporcionalidade e lista os riscos: sugestões inexatas, inferência de doenças e compartilhamento com seguradoras. A necessidade pergunta se a funcionalidade precisa de históricos completos ou só de tendências recentes; Aisha descobre que catorze dias de dados bastam. A proporcionalidade pergunta se o benefício justifica a intrusão. O risco de inferir doenças é real, porque leituras irregulares podem sugerir uma condição cardíaca. As mitigações incluem tratamento no aparelho, nenhum compartilhamento e explicações claras; tratar no celular do aluno evita que os históricos saiam do aparelho e elimina vários riscos de uma vez.

### 16.3 Consulta

Aisha consulta os trainers, cinco alunos voluntários e o encarregado. Os alunos querem um jeito fácil de desligar a funcionalidade, que é acrescentado. Os trainers temem que os alunos faltem às sessões por conselho do aplicativo sem entender por quê. O encarregado pergunta como os alunos vão saber o que a funcionalidade faz e como desligá-la. Os voluntários querem uma redação clara, nenhuma notificação surpresa e a garantia de que a seguradora nunca verá os dados. Aisha registra cada preocupação e a resposta de design correspondente no documento da avaliação, para que a ligação entre consulta e desenho fique visível.

### 16.4 Decisão

O encarregado aprova com condições: a funcionalidade vem desligada por padrão, é explicada em palavras simples, roda no aparelho e será revista depois de três meses de uso. A avaliação fica guardada com a documentação do produto, para que mudanças futuras acionem uma revisão. O Sr. Reilly observa que a avaliação moldou o desenho, em vez de só documentá-lo, e que uma boa avaliação registra as alternativas consideradas e rejeitadas, e não só a escolha final. Aqui, a alternativa rejeitada foi o tratamento na nuvem, que exigiria enviar os históricos completos aos servidores da Quayside.

### Exemplo resolvido

Aisha conduz uma avaliação de impacto das sugestões de dias de descanso, escolhe o tratamento no aparelho, acrescenta um botão para desligar depois da consulta e registra a aprovação.

> **Caso sintético.** A funcionalidade é sintética; o artigo 35 do GDPR, o art. 38 da LGPD e o WP248 são reais.

### Erros e limites

As avaliações precisam ser atualizadas se a funcionalidade mudar.

### Exercícios

- **EX046 — Gatilho da DPIA.** Por que a funcionalidade precisa de uma avaliação? *Rubrica:* 3 = tratamento sistemático de dados de saúde em escala;; 2 = menciona saúde;; 1 = vago;; 0 = nenhuma.
- **EX047 — Mitigação principal.** Cite uma mitigação. *Rubrica:* 3 = tratamento no aparelho, nenhum compartilhamento, explicações claras;; 2 = uma;; 1 = vago;; 0 = nenhuma.
- **EX048 — Resultado da consulta.** O que os alunos pediram? *Rubrica:* 3 = um jeito fácil de desligar;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Privacidade e proteção de dados: ferramentas

### Objetivos de aprendizagem

Você vai (1) usar um varredor simples para encontrar dados pessoais em arquivos; (2) interpretar seus limites; (3) agir sobre os resultados.

### 17.1 O varredor

Aisha escreve um varredor em Python, só com a biblioteca padrão, que usa expressões regulares para e-mails, telefones e números de cartão. Ela o roda em cinco arquivos sintéticos de um drive compartilhado, cópias modeladas nos tipos reais encontrados ali. O varredor lê cada arquivo linha a linha, aplica três padrões e conta as ocorrências sem imprimir os valores encontrados, para que o próprio relatório não espalhe dados pessoais. Os números de cartão são conferidos com um padrão simples de dígitos; ela observa que uma ferramenta de produção acrescentaria um teste de dígito verificador para reduzir os falsos positivos.

### 17.2 Resultados

O laboratório encontra padrões em três de cinco arquivos: uma exportação antiga de alunos com dois e-mails e dois telefones, anotações de um trainer com um telefone e um arquivo de reembolsos com um número de cartão. As anotações também mencionam uma lesão no joelho, que a expressão regular não detecta. A exportação foi criada para uma promoção três anos antes e esquecida; o arquivo de reembolsos foi salvo por um assistente financeiro para trabalhar offline; as anotações foram compartilhadas para cobrir aulas. Cada arquivo tem uma história plausível, o que mostra que os dados pessoais se espalham pelo trabalho comum, e não por descuido.

### 17.3 Limites

Aisha explica que os varredores de padrões deixam passar informações de saúde em texto livre e podem gerar falsos positivos. As expressões regulares encontram padrões estruturados, como e-mails, mas a saúde aparece em palavras comuns: lesão no joelho, asma, grávida. Uma lista de palavras-chave poderia ajudar, mas geraria muitos alarmes falsos numa academia, onde palavras como coração e lesão aparecem nas descrições das aulas. Por isso, é preciso revisão humana dos arquivos sinalizados e das anotações em geral. Aisha recomenda usar o varredor para priorizar essa revisão, e não para declarar que um arquivo está limpo.

### 17.4 Ações

A exportação antiga é excluída, o arquivo de reembolsos vai para o sistema de pagamentos e as anotações dos trainers passam para o aplicativo, com controles de acesso. Antes de excluir a exportação, Aisha confirma com o encarregado que não há retenção judicial. Ela pergunta ao financeiro por que precisava de uma cópia offline e descobre que o sistema de pagamentos não tinha um relatório de reembolsos, que a TI acrescenta. Os trainers ganham no aplicativo um campo de anotações que só os trainers do próprio aluno leem. O Sr. Reilly observa que as ferramentas ajudam, mas não substituem o julgamento.

### Laboratório — Varredura de padrões em arquivos compartilhados

```python
# Scan synthetic shared-drive files for personal data patterns (email, phone, card-like numbers).
import re
files = {"class_timetable.csv": "Mon,Spin,Studio 2\nTue,Yoga,Studio 1",
         "member_export_old.csv": "name,email,phone\nAna Lima,ana@example.org,+44 7700 900123\nRui Sousa,rui@example.org,+44 7700 900456",
         "trainer_notes.txt": "Client J. knee injury, avoid squats. Call 07700 900789.",
         "refunds_march.txt": "Refund to card 4111 1111 1111 1111 approved",
         "poster.txt": "Summer challenge! Join at the front desk."}
pat = {"email": r"[\w.]+@[\w.]+", "phone": r"(?:\+44 ?|0)7700 ?\d{6}", "card": r"\b(?:\d{4} ?){3}\d{4}\b"}
hits = 0
for f, t in files.items():
    found = {k: len(re.findall(p, t)) for k, p in pat.items() if re.findall(p, t)}
    hits += bool(found); print(f"{f:22s} {found if found else '-'}")
print(f"files with personal data patterns: {hits} of {len(files)}")
```

Execute com `python3 lab_scan.py`. Saída verificada:

```text
class_timetable.csv    -
member_export_old.csv  {'email': 2, 'phone': 2}
trainer_notes.txt      {'phone': 1}
refunds_march.txt      {'card': 1}
poster.txt             -
files with personal data patterns: 3 of 5
```

### Exemplo resolvido

O varredor de Aisha sinaliza três de cinco arquivos e deixa passar a anotação sobre a lesão no joelho, e ela exclui, move e protege os arquivos.

> **Caso sintético.** Os arquivos são sintéticos.

### Erros e limites

Varredores por expressões regulares não captam o contexto nem formatos incomuns.

### Exercícios

- **EX049 — Arquivos sinalizados.** Quantos arquivos continham padrões? *Rubrica:* 3 = 3 de 5;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX050 — Dado não detectado.** O que o varredor deixou passar? *Rubrica:* 3 = a anotação de saúde sobre a lesão no joelho;; 2 = menciona saúde;; 1 = vago;; 0 = nenhuma.
- **EX051 — Destino do arquivo de cartão.** O que aconteceu com o arquivo de reembolsos? *Rubrica:* 3 = foi movido para o sistema de pagamentos;; 2 = menciona a mudança;; 1 = foi mantido;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Privacidade e proteção de dados: controles

### Objetivos de aprendizagem

Você vai (1) selecionar controles para os riscos da Quayside; (2) mapear os controles para os princípios; (3) acompanhar a implementação.

### 18.1 Selecionar controles

Aisha lista seis controles: revisão de SDKs, lista de verificação dos pedidos de acesso, verificação da exclusão do CFTV, varredura de arquivos, autenticação multifator e exclusão de contas inativas. Ela escolhe controles que respondem aos achados dos capítulos anteriores, em vez de copiar uma lista genérica. Cada controle enfrenta uma falha real: o SDK de anúncios, a resposta de acesso incompleta, o firmware do CFTV, os arquivos esquecidos, os logins fracos dos gerentes e as contas guardadas para sempre. Isso torna o conjunto fácil de explicar, porque cada item tem uma história de que a equipe se lembra; controles genéricos sem história ficam para depois.

### 18.2 Mapeamento

Aisha mapeia cada controle para os princípios. A revisão de SDKs apoia a licitude, a transparência e a limitação da finalidade, porque impede fluxos para novas finalidades. A verificação da exclusão do CFTV apoia a limitação da conservação. A autenticação multifator apoia a integridade e a confidencialidade. A lista dos pedidos de acesso apoia a transparência e o direito de acesso. A varredura de arquivos apoia a limitação da conservação e a confidencialidade. A exclusão de contas inativas apoia a limitação da conservação e a minimização. O mapa mostra que a exatidão não tem controle próprio, então ela acrescenta um lembrete anual para os alunos conferirem seus dados.

### 18.3 Normas

Aisha observa que a ISO/IEC 27701 oferece controles de privacidade que estendem um sistema de gestão da segurança da informação, e que o NIST Privacy Framework organiza resultados de privacidade. A Quayside os usa como referência. Ela não tenta a certificação; usa os documentos como listas de verificação para encontrar áreas faltantes. As funções do NIST Privacy Framework, como Identify-P e Control-P, ajudam a agrupar as atividades, e as listas de controles da ISO/IEC 27701 lembram o treinamento e a gestão de fornecedores. Ela registra quais itens a Quayside já atende e quais estão planejados, para mostrar o progresso à liderança.

### 18.4 Acompanhamento

Cada controle tem responsável, situação e evidência, numa tabela simples compartilhada com os responsáveis. As situações possíveis são planejado, em andamento, operando e testado. Um controle só conta como testado quando uma evidência mostra que funcionou, como um log de vídeos excluídos ou um teste de pedido de acesso concluído. Aisha revisa a tabela todo mês e pede aos responsáveis que atualizem os links das evidências, e não só as palavras de situação; quem não tem evidência continua em andamento, porque a situação sozinha não prova nada. O Sr. Reilly observa que o mapeamento revela as lacunas de cobertura.

### Exemplo resolvido

Aisha lista seis controles, mapeia-os para os princípios do GDPR, usa como referência a ISO/IEC 27701 e o NIST Privacy Framework e acompanha responsáveis e evidências.

> **Caso sintético.** Os controles são sintéticos; a ISO/IEC 27701 e o NIST Privacy Framework são reais.

### Erros e limites

Um controle mapeado não é necessariamente eficaz.

### Exercícios

- **EX052 — Princípio do CFTV.** Que princípio a exclusão do CFTV apoia? *Rubrica:* 3 = limitação da conservação;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.
- **EX053 — Norma de referência.** Cite uma norma usada como referência. *Rubrica:* 3 = ISO/IEC 27701 ou NIST Privacy Framework;; 2 = uma;; 1 = vago;; 0 = nenhuma.
- **EX054 — Benefício do mapeamento.** Por que mapear os controles para os princípios? *Rubrica:* 3 = revela lacunas de cobertura;; 2 = menciona lacunas;; 1 = vago;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Privacidade e proteção de dados: monitoramento

### Objetivos de aprendizagem

Você vai (1) monitorar os controles de privacidade; (2) definir alertas; (3) analisar tendências.

### 19.1 O que monitorar

Aisha monitora a retenção do CFTV em todas as unidades, as mudanças de SDKs em cada versão do aplicativo, os prazos dos pedidos de acesso e as contas de ex-funcionários. Escolhe esses quatro sinais porque cada um já falhou uma vez ou tende a se desviar: a exclusão do CFTV falhou depois de uma atualização de firmware, os SDKs chegam com as versões, os prazos dos pedidos são obrigações legais e a rotatividade da equipe é alta. Ela evita monitorar tudo, porque um pequeno conjunto de sinais significativos, que cabe numa página, é mais fácil de usar do que um grande painel que ninguém lê.

### 19.2 Alertas

Aisha define os alertas: imagens com mais de trinta e cinco dias, qualquer SDK novo, pedidos a cinco dias do prazo e contas não removidas dois dias depois da saída. Os limites têm uma pequena margem, para que variações normais não disparem alertas. Os alertas do CFTV vão para o gerente da unidade e para a TI; os de SDK, para o líder do aplicativo e o encarregado; os de prazo, para a equipe de atendimento aos titulares; os de contas, para o RH e a TI. Cada mensagem de alerta diz o que fazer, e não só o que aconteceu, para que quem a recebe aja sem precisar perguntar.

### 19.3 Tendências

Depois de três meses, as contas de ex-funcionários caem de quarenta para duas, e todas as unidades cumprem a retenção do CFTV. Todos os pedidos de acesso são respondidos no prazo, embora as buscas nos fornecedores continuem sendo a etapa mais lenta. O alerta do CFTV de uma unidade dispara uma vez depois de outra atualização de firmware, e a correção leva um dia, em vez de seis semanas. As reclamações dos alunos sobre e-mails de marketing também caem a zero no período. Aisha observa que os dados de tendência mostram os controles funcionando, uma evidência mais forte do que a simples existência de uma política.

### 19.4 Revisão

Aisha revisa os alertas todo mês para eliminar o ruído. No primeiro mês, o alerta de SDK dispara a cada pequena atualização de biblioteca, então ela o muda para disparar só quando uma biblioteca envia dados a um domínio novo, e ele cai de quarenta por mês para dois. Ela registra cada mudança nas regras de alerta com uma justificativa, para que os revisores vejam se o monitoramento foi enfraquecido por conveniência ou melhorado em precisão. O Sr. Reilly observa que o monitoramento impede que as correções falhem em silêncio, como mostrou o problema do firmware do CFTV.

### Exemplo resolvido

Aisha monitora quatro controles com alertas, vê as contas esquecidas caírem de quarenta para duas e todas as unidades cumprirem a retenção do CFTV.

> **Caso sintético.** Os resultados são sintéticos.

### Erros e limites

Alertas demais fazem as pessoas ignorá-los.

### Exercícios

- **EX055 — Alerta do CFTV.** O que dispara o alerta do CFTV? *Rubrica:* 3 = imagens com mais de trinta e cinco dias;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.
- **EX056 — Tendência das contas.** Como mudaram as contas de ex-funcionários? *Rubrica:* 3 = de quarenta para duas;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX057 — Finalidade do monitoramento.** Por que monitorar controles já corrigidos? *Rubrica:* 3 = as correções podem falhar em silêncio;; 2 = menciona falha;; 1 = vago;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Privacidade e proteção de dados: solução de problemas

### Objetivos de aprendizagem

Você vai (1) diagnosticar falhas de privacidade; (2) encontrar as causas raiz; (3) evitar a recorrência.

### 20.1 Uma falha

Um aluno recebe um e-mail de marketing depois de revogar o consentimento. Ele reclama na recepção, a reclamação chega ao encarregado, e este pede a Aisha que descubra o que deu errado. O aluno tinha revogado o consentimento pelo aplicativo nove dias antes. Uma reclamação assim pode abalar a confiança e, se se repetir, levar a uma reclamação à autoridade de proteção de dados, então merece uma investigação cuidadosa. Aisha começa reunindo o registro do aplicativo, o log da plataforma de e-mail e o histórico das rotinas automáticas desses nove dias, para reconstruir a sequência dos fatos.

### 20.2 Diagnóstico

Aisha segue a revogação do banco do aplicativo até a plataforma de marketing. O aplicativo registrou a mudança corretamente, com data e hora. Mas a rotina noturna que copia as mudanças de preferência para a plataforma de e-mail tinha registrado erros por sete noites seguidas, e a revogação nunca foi sincronizada. Ao reproduzir o problema numa cópia de teste, ela conta 214 revogações equivalentes que não foram transferidas naquela semana, então o problema afetou muitos alunos, e não apenas um. Isso transforma uma reclamação isolada num incidente a tratar de forma ampla, com todos os afetados identificados.

### 20.3 Causa raiz

A rotina falhou depois de uma troca de senha e não tinha alerta de falha. A TI tinha trocado uma senha de serviço, como manda a boa prática de segurança, mas não atualizou a credencial guardada pela rotina. A rotina falhou em silêncio, porque suas mensagens de erro iam para uma caixa de correio que ninguém lia. A causa real, portanto, foi a falta de alerta e de responsável, e não a troca de senha, que era a coisa certa a fazer. Culpar a TI não teria corrigido nada. Aisha acrescenta um alerta de falha e uma reconciliação semanal, que atacam a causa, e não o sintoma.

### 20.4 Prevenção

Aisha lista todas as rotinas que transportam escolhas de privacidade: preferências de marketing, configurações de compartilhamento da frequência cardíaca, exclusões de contas e exclusões de dados nos fornecedores. Cada uma agora tem um responsável e um alerta de falha. A reconciliação semanal compara as revogações no aplicativo com as supressões na plataforma de e-mail e informa qualquer diferença. Os alunos afetados recebem um pedido de desculpas e a confirmação da sua escolha. O Sr. Reilly lembra que revogar deve ser tão fácil quanto consentir, pelo artigo 7(3) do GDPR e pelo art. 8º, §5º, da LGPD, e precisa de fato funcionar.

### Exemplo resolvido

Aisha liga um e-mail indesejado a uma rotina de sincronização que falhou, acrescenta alertas e reconciliação e confere rotinas semelhantes.

> **Caso sintético.** A falha é sintética; o artigo 7(3) do GDPR e o art. 8º, §5º, da LGPD são reais.

### Erros e limites

Corrigir só o sintoma convida a recorrência.

### Exercícios

- **EX058 — Causa.** Por que o aluno recebeu o e-mail? *Rubrica:* 3 = a rotina de sincronização falhou depois de uma troca de senha;; 2 = menciona a rotina;; 1 = vago;; 0 = nenhuma.
- **EX059 — Correção.** Que correções Aisha acrescentou? *Rubrica:* 3 = um alerta e uma reconciliação semanal;; 2 = uma;; 1 = vago;; 0 = nenhuma.
- **EX060 — Princípio.** O que exige o artigo 7(3)? *Rubrica:* 3 = revogar tão facilmente quanto consentir;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<a id="ch-21"></a>

## Capítulo 21 — Privacidade e proteção de dados: integração de serviços

### Objetivos de aprendizagem

Você vai (1) integrar um novo fornecedor com segurança; (2) conferir contratos e transferências; (3) limitar os dados compartilhados.

### 21.1 O fornecedor

A Quayside quer um novo fornecedor de reservas de aulas, que oferece uma tela de reserva melhor e uma lista de espera. Aisha revisa sua segurança, seu contrato e a localização dos dados. Envia um questionário curto sobre certificação de segurança, localização dos dados, suboperadores, retenção, notificação de incidentes e apoio aos pedidos de exclusão e de acesso. Também lê o aviso de privacidade público do fornecedor e o compara com as respostas, porque o material comercial e o contrato às vezes dizem coisas diferentes. Aqui, o aviso cita um parceiro de análise de uso que o questionário tinha omitido.

### 21.2 Contrato

O contrato precisa atender ao artigo 28 do GDPR. Ele deve prever o tratamento apenas sob as instruções da Quayside, a confidencialidade, a segurança, o uso de suboperadores, o apoio aos pedidos dos titulares, a exclusão ao fim do serviço e o direito de auditoria. O fornecedor guarda os dados fora da UE, então são necessárias salvaguardas de transferência, como as cláusulas contratuais-padrão; no Brasil, a transferência internacional segue os arts. 33 a 36 da LGPD. Aisha aponta esses pontos ao jurídico, que negocia o contrato final; a assinatura espera essas cláusulas, e o direito de auditoria é mantido.

### 21.3 Minimização

Aisha limita os dados compartilhados a nome, número de matrícula e reservas, sem dados de saúde. A integração padrão do fornecedor pede data de nascimento, gênero, endereço e zonas cardíacas para personalizar as sugestões de aulas. Aisha retira esses campos, porque as reservas funcionam sem eles, e a lista de espera funciona só com os números de matrícula. O fornecedor concorda, e a especificação da integração lista os campos exatos permitidos. Qualquer pedido para acrescentar um campo depois precisa passar pelo encarregado e atualizar o registro das operações de tratamento. Menos campos significam menos riscos a gerir.

### 21.4 Testes

Aisha testa a integração com alunos sintéticos, de modo que nenhum dado real fica exposto enquanto os problemas aparecem. Os testes conferem que só os campos listados saem da Quayside, que os cancelamentos e as exclusões chegam ao fornecedor e que um pedido de acesso consegue recuperar os registros do fornecedor. Um teste descobre que o fornecedor guarda as reservas canceladas indefinidamente, então o contrato ganha um limite de retenção de doze meses. Cada teste que falha vira uma cláusula. O Sr. Reilly observa que a integração é onde aparecem os fluxos de dados não planejados.

### Exemplo resolvido

Aisha confere o contrato e as transferências do fornecedor, limita os campos compartilhados e testa com alunos sintéticos.

> **Caso sintético.** O fornecedor é sintético; o artigo 28 do GDPR e os arts. 33 a 36 da LGPD são reais.

### Erros e limites

Os fornecedores mudam de suboperadores; acompanhe os avisos.

### Exercícios

- **EX061 — Artigo do contrato.** Que artigo rege os contratos com operadores? *Rubrica:* 3 = artigo 28;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.
- **EX062 — Campos compartilhados.** Que dados são compartilhados? *Rubrica:* 3 = nome, número de matrícula, reservas;; 2 = a maioria;; 1 = saúde;; 0 = nenhuma.
- **EX063 — Dados de teste.** Que dados foram usados nos testes? *Rubrica:* 3 = alunos sintéticos;; 2 = parcialmente correta;; 1 = reais;; 0 = nenhuma.

<a id="ch-22"></a>

## Capítulo 22 — Privacidade e proteção de dados: automação

### Objetivos de aprendizagem

Você vai (1) automatizar a exclusão de contas inativas; (2) tratar as exceções; (3) verificar os resultados.

### 22.1 A regra

A Quayside exclui as contas inativas há mais de dois anos, depois de um e-mail de aviso enviado trinta dias antes. Os dois anos seguem a tabela de retenção documentada da Quayside, que equilibra os alunos que voltam depois de longas pausas com a limitação da conservação. O aviso dá ao aluno a chance de manter a conta simplesmente entrando nela. As contas com dívida em aberto ficam retidas, porque a Quayside precisa dos registros para cobrar ou quitar a dívida; essa é uma exceção documentada, com prazo de retenção próprio, e não uma decisão tomada caso a caso.

### 22.2 Resultados

O laboratório processa 3.000 contas: 73 e-mails de aviso neste mês, 1.116 contas a excluir e 37 retidas por dívida em aberto. O script lê uma lista sintética de 3.000 contas com a data da última atividade e a marcação de dívida, e calcula quais chegam ao ponto de aviso neste mês, quais passaram do ponto de exclusão e quais ficam retidas. Ele imprime apenas contagens, e não identidades, e grava a lista dos números de conta afetados num arquivo protegido para a equipe de operações. Nenhum nome aparece na saída do console nem nos logs.

### 22.3 Exceções

As contas com dívida ficam retidas, com base documentada, até a resolução. Aisha registra cada decisão. Cada conta retida é revista todo mês, e, quando a dívida é quitada ou baixada, a conta entra na exclusão na rodada seguinte. Aisha considera outras exceções possíveis, como ações judiciais, e acrescenta uma marcação de retenção manual que só o encarregado pode definir. Cada retenção registra quem a definiu, quando e por quê, e as retenções sem justificativa são removidas na revisão mensal. Na primeira rodada, todas as trinta e sete retenções têm uma referência de dívida registrada.

### 22.4 Verificação

Aisha examina uma amostra das contas excluídas para confirmar a remoção em todos os sistemas. Para vinte contas, ela confere o sistema de matrículas, o banco do aplicativo, a plataforma de e-mail e o fornecedor de reservas. Na primeira rodada, o fornecedor ainda guarda três contas, porque sua interface de exclusão tinha falhado; a correção acrescenta uma etapa de confirmação pelo fornecedor. A exclusão agora é verificada, e não presumida, o que apoia a responsabilização do artigo 5(2). Vinte amostras por mês bastam para detectar uma ligação quebrada com um fornecedor. O Sr. Reilly observa que a automação aplica a limitação da conservação com confiabilidade.

### Laboratório — Exclusão automática de contas inativas

```python
# Automated deletion of inactive app accounts: inactive > 24 months, warn at 23 months, skip accounts with debt.
import random
r = random.Random(13)
acc = [(r.randint(0, 40), r.random() < 0.03) for _ in range(3000)]  # months inactive, outstanding debt
warn = sum(1 for m, d in acc if m == 23); dele = sum(1 for m, d in acc if m > 24 and not d); hold = sum(1 for m, d in acc if m > 24 and d)
print(f"accounts {len(acc)}; warning emails this month {warn}; delete {dele}; held for outstanding debt {hold}")
```

Execute com `python3 lab_inactive.py`. Saída verificada:

```text
accounts 3000; warning emails this month 73; delete 1116; held for outstanding debt 37
```

### Exemplo resolvido

A rotina de Aisha envia 73 avisos, exclui 1.116 contas e retém 37 com dívida, e as exclusões são verificadas por amostragem.

> **Caso sintético.** As contas são sintéticas.

### Erros e limites

A exclusão precisa chegar, com o tempo, aos backups e aos fornecedores.

### Exercícios

- **EX064 — Exclusões.** Quantas contas são excluídas? *Rubrica:* 3 = 1.116;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX065 — Retidas.** Por que 37 contas ficam retidas? *Rubrica:* 3 = dívida em aberto;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX066 — Verificação.** Como a exclusão é verificada? *Rubrica:* 3 = por amostragem em todos os sistemas;; 2 = menciona amostragem;; 1 = vago;; 0 = nenhuma.

<a id="ch-23"></a>

## Capítulo 23 — Privacidade e proteção de dados: avaliação

### Objetivos de aprendizagem

Você vai (1) avaliar o programa de privacidade; (2) comparar os resultados com a linha de base; (3) recomendar prioridades.

### 23.1 Comparação

Aisha compara as métricas atuais com a linha de base: as contas esquecidas caíram de quarenta para duas, a retenção do CFTV é cumprida e a cobertura dos pedidos de acesso é completa. Ela apresenta cada métrica com a data e o método da linha de base, para que a comparação seja justa. Algumas melhorias são grandes e claras. Outras precisam de explicação, como as comunicações de incidentes, que subiram de quase nenhuma para seis por mês: mais comunicações indicam mais conscientização, e não mais incidentes. Ela evita afirmar, sem evidências, que o programa causou cada mudança, e cita a fonte de cada comparação.

### 23.2 Lacunas restantes

As anotações de saúde em texto livre continuam difíceis de detectar, porque o varredor não as encontra de forma confiável. O monitoramento dos fornecedores é manual e depende de alguém ler os e-mails sobre mudanças de suboperadores, o que é fácil de perder. O registro de acessos ao CFTV existe em apenas trinta unidades, porque dez gravadores antigos não têm o recurso. Aisha lista essas lacunas abertamente, para que os líderes entendam o que o programa ainda não cobre, e dá a cada uma um responsável nomeado. Nenhuma fica escondida em notas de rodapé ou anexos.

### 23.3 Prioridades

Aisha recomenda treinar os trainers sobre as anotações e automatizar as verificações dos fornecedores. Ensinar os trainers a guardar as anotações de saúde no campo protegido do aplicativo resolve a primeira lacuna a baixo custo, com uma tarde por região, e reduz depressa a maior exposição restante. As verificações automáticas poderiam comparar todo mês as listas de suboperadores dos fornecedores. Trocar os dez gravadores antigos exige orçamento, então ela estima o custo e a redução de risco. Ela ordena as prioridades pela redução de risco por unidade de esforço, o que ajuda os líderes a escolher.

### 23.4 Relatório

Aisha apresenta os resultados ao encarregado. O relatório é curto, com duas páginas no total: o que foi encontrado, o que mudou, o que falta e o que ela recomenda, com a evidência de cada afirmação. O encarregado aceita as duas primeiras prioridades e consulta o diretor financeiro sobre a troca dos gravadores. Os líderes leem o relatório inteiro. O Sr. Reilly observa que a avaliação transforma atividade em evidência, e diz a Aisha que uma avaliação equilibrada tem mais credibilidade do que uma que proclama sucesso total, porque os leitores confiam mais em quem também mostra o que não funcionou.

### Exemplo resolvido

Aisha mostra a melhoria em relação à linha de base, nomeia as lacunas restantes e recomenda prioridades.

> **Caso sintético.** Os resultados são sintéticos.

### Erros e limites

As melhorias podem refletir mudanças na forma de medir.

### Exercícios

- **EX067 — Melhoria.** Cite uma melhoria. *Rubrica:* 3 = contas esquecidas de quarenta para duas; retenção do CFTV cumprida; cobertura completa dos pedidos de acesso;; 2 = uma;; 1 = vago;; 0 = nenhuma.
- **EX068 — Lacuna restante.** Cite uma lacuna restante. *Rubrica:* 3 = anotações de saúde em texto livre; monitoramento manual dos fornecedores;; 2 = uma;; 1 = vago;; 0 = nenhuma.
- **EX069 — Prioridade.** O que Aisha recomendou? *Rubrica:* 3 = treinamento dos trainers e verificações automáticas dos fornecedores;; 2 = uma;; 1 = vago;; 0 = nenhuma.

<a id="ch-24"></a>

## Capítulo 24 — Métodos de pesquisa aplicada

### Objetivos de aprendizagem

Você vai (1) enquadrar um pequeno estudo; (2) coletar dados de forma ética; (3) relatar os limites.

### 24.1 Pergunta

Aisha pergunta se os alunos entendem as configurações de compartilhamento da frequência cardíaca. Antes, os voluntários tinham se surpreendido com as telas das aulas mostrando zonas cardíacas, e ela quer saber se a página de configurações permite aos alunos controlar isso. Uma pergunta de pesquisa clara mantém o estudo pequeno e focado, a ponto de ser respondida em quatro semanas com um pequeno grupo de voluntários. Ela escreve a pergunta, o método, os participantes e a análise planejada antes de coletar os dados, para que os resultados não moldem a pergunta depois, e limita o estudo a alunos adultos.

### 24.2 Método

Aisha aplica um questionário curto, com consentimento e sem identificadores, e conduz cinco sessões de usabilidade. O questionário pede aos alunos que encontrem e expliquem cada configuração e registra se a explicação está correta. As sessões pedem a cinco alunos que realizem tarefas pensando em voz alta. Os participantes recebem uma folha de informações, dão consentimento e podem parar a qualquer momento. Nenhum nome é registrado, e as anotações das sessões usam números de participante que não se ligam às contas. Os arquivos brutos do questionário são excluídos depois da análise, e os termos de consentimento ficam guardados à parte.

### 24.3 Resultados

A maioria dos participantes do questionário encontrou a configuração de frequência cardíaca, mas menos da metade explicou corretamente que ela controlava o compartilhamento com as telas das aulas, e vários acharam que ela desligava a cinta por completo. Nas sessões, dois participantes procuraram a configuração na página de reservas de aulas. Esses resultados sugerem um problema de redação e de posição, e não alunos desinteressados pela privacidade. Menos da metade explicar a configuração corretamente é um sinal forte de que o rótulo, e não os alunos, precisa mudar, o que dá ao projeto seguinte um objetivo claro.

### 24.4 Limites

A amostra é pequena e autosselecionada: os participantes se ofereceram e podem se importar mais com a privacidade do que os outros alunos. O estudo aconteceu em apenas duas unidades. A amostra de usabilidade é pequena, embora amostras pequenas ainda revelem os problemas maiores. Os participantes também sabiam que estavam num estudo. Aisha relata esses limites ao lado dos resultados e recomenda um acompanhamento depois do redesenho, com as mesmas perguntas, para ver se a compreensão melhora. O Sr. Reilly observa que limites honestos tornam os resultados úteis e orientam o acompanhamento.

### Exemplo resolvido

Aisha estuda a compreensão das configurações com um questionário anônimo e cinco sessões e relata os limites.

> **Caso sintético.** O estudo é sintético.

### Erros e limites

Amostras pequenas não permitem generalizar.

### Exercícios

- **EX070 — Pergunta.** O que o estudo perguntou? *Rubrica:* 3 = se os alunos entendem as configurações de frequência cardíaca;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX071 — Ética.** Como os dados foram coletados de forma ética? *Rubrica:* 3 = com consentimento e sem identificadores;; 2 = um;; 1 = vago;; 0 = nenhuma.
- **EX072 — Limite.** Cite um limite. *Rubrica:* 3 = amostra pequena e autosselecionada;; 2 = um;; 1 = vago;; 0 = nenhuma.

<a id="ch-25"></a>

## Capítulo 25 — Ateliê de projeto em equipe

### Objetivos de aprendizagem

Você vai (1) trabalhar em equipe num projeto de privacidade; (2) dividir os papéis; (3) revisar o trabalho dos colegas.

### 25.1 Projeto

A equipe de Aisha redesenha a página de configurações de privacidade do aplicativo. A pesquisa do capítulo anterior mostrou que os alunos entendiam mal a configuração de compartilhamento da frequência cardíaca, e o projeto transforma esse achado num redesenho. Aisha trabalha com três colegas de outras especialidades: design de interface, desenvolvimento de software e testes. A equipe combina um briefing, um cronograma de seis semanas e uma definição de sucesso baseada na compreensão: a maioria dos testadores precisa explicar a configuração corretamente, sem ajuda, medida com as mesmas perguntas do estudo anterior.

### 25.2 Papéis

Os papéis incluem pesquisa, design, desenvolvimento e testes. Aisha lidera a pesquisa e a revisão de privacidade, uma colega lidera o design de interface, outro constrói o protótipo e um terceiro planeja os testes. Os papéis são claros, mas não rígidos; todos participam de duas sessões com alunos. A equipe se reúne duas vezes por semana e mantém um registro compartilhado das decisões, que depois ajuda a explicar por que certas redações e disposições foram escolhidas. Quando o designer e o desenvolvedor discordam sobre onde colocar a configuração, o registro guarda a evidência dos alunos que resolveu a questão.

### 25.3 Revisão

Os colegas revisam o trabalho uns dos outros quanto à clareza e à exatidão, seguindo uma lista simples: a configuração é fácil de encontrar, a redação é exata, o padrão protege os alunos e o design funciona com leitores de tela? A redação de Aisha é criticada por ser longa demais, e ela a encurta. A revisão também pega um erro no protótipo: desligar o compartilhamento também parava o registro dos treinos. Esse defeito teria apagado em silêncio o histórico de treinos dos alunos, então a equipe acrescenta um teste que confere que compartilhamento e registro são configurações independentes.

### 25.4 Resultado

A nova página explica com clareza o compartilhamento com as telas das aulas. Ela separa esse compartilhamento da conexão da cinta e usa palavras simples: mostrar minha zona cardíaca nas telas das aulas. O compartilhamento passa a vir desligado por padrão para os novos alunos, e os atuais são consultados uma única vez, de modo que aparecer na tela exige uma escolha deliberada. Num novo teste com outros voluntários, a maioria dos participantes já explica a configuração corretamente. A equipe entrega o design à equipe do aplicativo da Quayside com as evidências da pesquisa. O Sr. Reilly observa que o trabalho em equipe traz visões variadas.

### Exemplo resolvido

A equipe redesenha a página de configurações com papéis claros e revisão entre colegas.

> **Caso sintético.** O projeto é sintético.

### Erros e limites

As equipes podem deixar de lado a visão dos alunos; teste com alunos.

### Exercícios

- **EX073 — Projeto.** O que a equipe redesenhou? *Rubrica:* 3 = a página de configurações de privacidade;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX074 — Papéis.** Cite dois papéis. *Rubrica:* 3 = pesquisa, design, desenvolvimento, testes;; 2 = dois;; 1 = um;; 0 = nenhuma.
- **EX075 — Resultado.** O que melhorou? *Rubrica:* 3 = a explicação do compartilhamento com as telas das aulas;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<a id="ch-26"></a>

## Capítulo 26 — Privacidade e proteção de dados: transição para a operação

### Objetivos de aprendizagem

Você vai (1) entregar os controles à equipe de operações; (2) escrever runbooks; (3) confirmar os responsáveis.

### 26.1 Runbooks

Aisha escreve runbooks para as verificações do CFTV, as revisões de SDKs, os pedidos de acesso e as exclusões. Cada runbook descreve a finalidade da tarefa, quando executá-la, os passos, os resultados esperados, o que fazer se os resultados forem inesperados e quem procurar. Ela os escreve para a equipe de operações, e não para especialistas, então evita jargão e usa capturas de tela do ambiente de teste sintético, e não dos sistemas reais. O runbook do CFTV, por exemplo, traz o caminho no menu do gravador, a idade esperada do vídeo mais antigo e o telefone a ligar quando ela passar de trinta e cinco dias.

### 26.2 Responsáveis

Cada runbook nomeia um responsável em operações: o do CFTV pertence ao gerente de operações; a revisão de SDKs, ao líder do aplicativo; os pedidos de acesso, à líder do atendimento; a exclusão de contas, ao gerente de serviços de TI. Cada responsável tem um substituto nomeado para as férias. Sempre que possível, a responsabilidade é escrita na descrição do cargo, para sobreviver às mudanças de função. Sem responsáveis nomeados, a verificação da exclusão do CFTV dependeria de quem se lembrasse dela, que foi exatamente como a falha do firmware passou despercebida por seis semanas.

### 26.3 Treinamento

Aisha treina os responsáveis e os observa executando cada tarefa. Enquanto o responsável executa o runbook, ela anota onde ele hesita ou lê um passo errado. A líder do atendimento tem dificuldade com a busca das transcrições do chat no fornecedor, então Aisha acrescenta passos mais claros e o nome de um contato no fornecedor. No runbook de exclusão, o gerente de serviços de TI entende mal qual confirmação do fornecedor esperar, e o passo passa a mostrar um exemplo da mensagem de confirmação. A observação revela lacunas que a simples revisão do documento deixaria passar.

### 26.4 Confirmação

Os responsáveis assinam a aceitação, o que significa que concordam que o runbook está correto e que conseguem executá-lo. O encarregado guarda as aceitações assinadas. Aisha marca um acompanhamento três meses depois para conferir se as tarefas estão rodando e deixa seus contatos para dúvidas. A transição só termina quando as tarefas rodam sem a ajuda dela. Três meses depois, as quatro tarefas rodaram no prazo sem a participação de Aisha, e seu papel se encerra. O Sr. Reilly observa que a transição para a operação é o que mantém os controles vivos depois do fim de um projeto.

### Exemplo resolvido

Aisha escreve quatro runbooks, nomeia os responsáveis, treina-os e obtém sua aceitação.

> **Caso sintético.** Os runbooks são sintéticos.

### Erros e limites

Runbooks envelhecem; revise-os todo ano.

### Exercícios

- **EX076 — Runbooks.** Cite dois runbooks. *Rubrica:* 3 = verificações do CFTV, revisões de SDKs, pedidos de acesso, exclusões;; 2 = dois;; 1 = um;; 0 = nenhuma.
- **EX077 — Treinamento.** Como Aisha confirmou que os responsáveis conseguiam executar as tarefas? *Rubrica:* 3 = observou-os executando cada tarefa;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX078 — Finalidade.** Por que fazer a transição? *Rubrica:* 3 = mantém os controles vivos depois do projeto;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<a id="ch-27"></a>

## Capítulo 27 — Implantação e validação

### Objetivos de aprendizagem

Você vai (1) implantar mudanças de privacidade; (2) validá-las; (3) reverter com segurança.

### 27.1 Implantação

A nova página de configurações e a versão do aplicativo sem o SDK de anúncios são implantadas em etapas: primeiro para cinco por cento dos alunos, depois para metade e, por fim, para todos, ao longo de duas semanas. A implantação em etapas limita o impacto dos erros. A equipe do aplicativo acompanha os relatórios de falhas e os contatos com o suporte em cada etapa, e Aisha monitora o tráfego de rede de aparelhos de teste em busca de fluxos de dados inesperados. Na etapa de cinco por cento, ela não vê tráfego para a rede de anúncios em nenhum aparelho de teste.

### 27.2 Validação

Aisha valida a versão com contas sintéticas e inspeção de rede. A validação repete os testes de fluxo anteriores na nova versão, com as mesmas contas e os mesmos passos, para que os resultados possam ser comparados com os achados anteriores. Ela confere cada domínio contatado pelo aplicativo e os campos enviados. Também confere que o novo padrão do compartilhamento da frequência cardíaca é desligado para as contas novas: uma conta de teste criada no dia do lançamento confirma que a chave começa na posição desligada. Todos os resultados correspondem ao plano, e ela os registra para a decisão de ampliar a implantação.

### 27.3 Reversão

Um plano de reversão está pronto caso apareçam erros graves e seja preciso voltar à versão anterior. Aisha aponta um problema de privacidade na reversão: a versão anterior continha o SDK de anúncios, então voltar a ela reativaria o fluxo prejudicial. A equipe prepara uma versão anterior corrigida, sem o SDK, para usar em qualquer reversão. Essa versão é testada com antecedência, para que uma reversão feita sob pressão não reintroduza o fluxo para a rede de anúncios. Ela observa que os planos de reversão costumam ser escritos pensando só na estabilidade, e raramente na privacidade.

### 27.4 Resultado

A versão chega a todos os alunos sem erros graves. Os testes de rede não mostram tráfego para a rede de anúncios nem campos de frequência cardíaca saindo para terceiros além do fornecedor contratado das cintas. A validação confirma que nenhum dado de frequência cardíaca vai para anunciantes. Aisha registra os resultados com datas, versão do aplicativo e aparelhos de teste, para que o encarregado possa mostrar evidências se um aluno ou o regulador perguntar; nada fica sem documentação. O Sr. Reilly observa que a validação comprova a mudança, e não apenas a intenção de mudar.

### Exemplo resolvido

Aisha implanta em etapas, valida com contas sintéticas e confirma que não há fluxos para anunciantes.

> **Caso sintético.** A implantação é sintética.

### Erros e limites

As implantações em etapas podem misturar versões.

### Exercícios

- **EX079 — Validação.** Como a validação é feita? *Rubrica:* 3 = contas sintéticas e inspeção de rede;; 2 = um;; 1 = vago;; 0 = nenhuma.
- **EX080 — Reversão.** Por que ter um plano de reversão? *Rubrica:* 3 = para se recuperar de erros;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX081 — Resultado.** O que a validação confirmou? *Rubrica:* 3 = nenhum dado de frequência cardíaca vai para anunciantes;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<a id="ch-28"></a>

## Capítulo 28 — Prática de campo

### Objetivos de aprendizagem

Você vai (1) aplicar as habilidades nas unidades; (2) conversar com a equipe; (3) registrar as observações.

### 28.1 Visitas

Aisha visita cinco unidades para conferir telas, placas de CFTV e registros. Cada visita segue uma lista: telas da recepção bloqueadas quando ninguém está por perto, nenhuma lista de alunos à vista, placas de CFTV presentes e legíveis, gravadores em salas trancadas, Wi-Fi de visitantes separado e formulário de comunicação conhecido pela equipe. Ela escolhe unidades de tamanhos e idades diferentes, incluindo duas com gravadores antigos, para cobrir condições variadas. Cada visita leva cerca de noventa minutos, e ela fotografa apenas placas e portas de salas, nunca telas ou pessoas.

### 28.2 Equipe

Aisha conversa com a equipe sobre o guia e a comunicação de incidentes. Os funcionários são simpáticos e falam abertamente das dificuldades. Vários dizem que o formulário é fácil, mas uma unidade nunca tinha ouvido falar dele, porque o gerente era novo. Os trainers gostam do novo campo de anotações. A recepção pede um jeito rápido de responder aos alunos que perguntam que dados a Quayside guarda, então Aisha redige um roteiro curto. O roteiro orienta a equipe a indicar o formulário de pedido de acesso no aplicativo, em vez de ler os dados em voz alta no balcão.

### 28.3 Observações

Duas unidades não tinham placas de CFTV, que as Diretrizes 3/2019 do EDPB esperam como primeira camada de informação. As diretrizes descrevem a placa de aviso como a primeira camada de transparência, que informa sobre o monitoramento antes de a pessoa entrar na área, com informações mais completas em outro lugar. Sem as placas, os alunos entram em áreas monitoradas sem aviso. As duas unidades tinham retirado as placas antigas durante uma pintura e nunca as recolocaram. Outras observações incluem uma tela da recepção desbloqueada num horário de pico e uma sala de gravador usada como depósito, com a porta aberta.

### 28.4 Acompanhamento

As placas são instaladas em duas semanas, o depósito é esvaziado e trancado, e o gerente novo recebe uma apresentação do formulário de comunicação. Aisha acrescenta a lista às visitas de rotina dos gerentes regionais, para que as verificações de campo continuem depois do estágio. Ela compartilha os achados comuns com todas as unidades, sem nomear funcionários. Os gerentes regionais reportam os resultados a cada trimestre, e achados repetidos na mesma unidade levam a uma conversa com o gerente. O Sr. Reilly observa que as visitas de campo encontram o que as verificações remotas deixam passar.

### Exemplo resolvido

Aisha visita cinco unidades, descobre a falta de placas de CFTV em duas e faz com que sejam instaladas.

> **Caso sintético.** As visitas são sintéticas; as Diretrizes 3/2019 do EDPB são reais.

### Erros e limites

As visitas são retratos de um momento.

### Exercícios

- **EX082 — Unidades visitadas.** Quantas unidades Aisha visitou? *Rubrica:* 3 = cinco;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX083 — Placas.** O que faltava em duas unidades? *Rubrica:* 3 = placas de CFTV;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX084 — Valor.** Por que as visitas de campo importam? *Rubrica:* 3 = encontram o que as verificações remotas deixam passar;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<a id="ch-29"></a>

## Capítulo 29 — Construção do projeto final

### Objetivos de aprendizagem

Você vai (1) construir um kit de ferramentas de privacidade; (2) combinar os laboratórios; (3) documentá-lo.

### 29.1 Kit de ferramentas

Aisha combina num kit os scripts dos laboratórios anteriores: a revisão dos fluxos de SDKs, a verificação da cobertura dos pedidos de acesso, o varredor de arquivos, a verificação da retenção do CFTV e a rotina das contas inativas. Ela lhes dá uma estrutura comum, formatos de saída consistentes e um arquivo de configuração compartilhado para os limites, para que a equipe de privacidade os execute sempre do mesmo jeito. Limites como trinta dias para as imagens e dois anos para as contas inativas ficam no arquivo de configuração, e não no código, para que possam mudar sem reescrever nada.

### 29.2 Documentação

Cada script tem finalidade, entradas, saídas e limites documentados. No varredor, a seção de limites diz claramente que informações de saúde em texto livre não são detectadas; na verificação do CFTV, que o script lê um índice, e não as imagens. A documentação explica também como mudar os limites e onde as saídas ficam guardadas. Aisha a escreve para pessoas que não fizeram seu curso. Cada seção de limites é um aviso direto, por exemplo: uma varredura limpa não significa que o arquivo não contenha informações de saúde. Um exemplo resolvido com arquivos sintéticos mostra a saída esperada de cada script.

### 29.3 Testes

Aisha testa todos os scripts com dados sintéticos. Cada script tem um conjunto de arquivos de entrada sintéticos com resultados corretos conhecidos, para que qualquer pessoa confirme que ele continua funcionando depois de mudanças. Os testes incluem casos extremos, como arquivos vazios, datas ausentes e contas ao mesmo tempo inativas e com dívida; neste último caso, o teste confirma que a retenção prevalece sobre a exclusão. Todos os testes passam antes da entrega, e os resultados ficam guardados com o kit, para que a próxima pessoa saiba exatamente o que era esperado.

### 29.4 Entrega

O kit é entregue à equipe de privacidade da Quayside, que nomeia um responsável e combina uma revisão anual. Aisha explica que scripts escritos para uma versão de um sistema podem quebrar quando os sistemas mudam. Lembra também que o kit usa apenas as bibliotecas padrão do Python, o que simplifica a manutenção e evita dependências extras. A equipe de privacidade executa cada script uma vez com Aisha observando, e a data da primeira revisão anual é marcada. O Sr. Reilly observa que as ferramentas precisam de manutenção, e que uma ferramenta sem responsável logo deixa de ser confiável.

### Exemplo resolvido

Aisha constrói e documenta um kit de cinco scripts testado com dados sintéticos.

> **Caso sintético.** O kit é sintético.

### Erros e limites

Ferramentas precisam de responsáveis.

### Exercícios

- **EX085 — Scripts.** Quantos scripts são combinados? *Rubrica:* 3 = cinco;; 2 = parcialmente correta;; 1 = errada;; 0 = nenhuma.
- **EX086 — Documentação.** O que a documentação de cada script inclui? *Rubrica:* 3 = finalidade, entradas, saídas, limites;; 2 = a maioria;; 1 = um;; 0 = nenhuma.
- **EX087 — Dados.** Que dados são usados nos testes? *Rubrica:* 3 = sintéticos;; 2 = parcialmente correta;; 1 = reais;; 0 = nenhuma.

<a id="ch-30"></a>

## Capítulo 30 — Avaliação do projeto final

### Objetivos de aprendizagem

Você vai (1) apresentar seu projeto final; (2) responder a perguntas; (3) refletir.

### 30.1 Apresentação

Aisha apresenta seu trabalho na Quayside ao Sr. Reilly e ao encarregado. A apresentação segue o curso: inventário, fluxos, direitos, retenção, monitoramento e transição para a operação. Para cada área, ela mostra um achado, a correção e a evidência. Os slides são simples e usam números dos laboratórios, como os 47 de 287 registros da primeira resposta de acesso e os 292 vídeos além da retenção numa unidade. Ela termina com as lacunas restantes: as anotações de saúde em texto livre, os dez gravadores antigos e o monitoramento manual dos fornecedores. Os avaliadores destacam a honestidade.

### 30.2 Perguntas

Os avaliadores perguntam sobre os limites, como as anotações de saúde em texto livre. O encarregado pergunta como a Quayside detectaria um novo risco desse tipo, e Aisha explica a abordagem de treinamento e amostragem. O Sr. Reilly pergunta o que ela faria diferente. Ela responde que teria começado o monitoramento mais cedo, porque vários problemas existiam havia meses antes de alguém olhar para eles. Acrescenta que teria testado o processo de pedidos de acesso já no primeiro mês, porque o resultado de 16% de cobertura mudou a forma como a equipe enxergava todos os outros controles.

### 30.3 Reflexão

Aisha reflete que muitos problemas vieram do trabalho comum: sistemas lentos, atualizações de firmware, arquivos esquecidos e SDKs que vinham embutidos. As verificações técnicas os encontraram porque compararam o que os sistemas faziam de fato com o que as políticas diziam. Ela também aprendeu que as correções precisam de responsáveis e de monitoramento, senão voltam a falhar em silêncio, como a exclusão do CFTV mostrou duas vezes. Sua lição mais forte é que um aluno sintético que percorre um processo inteiro, do cadastro à exclusão, revela mais do que qualquer lista de verificação.

### 30.4 Próximos passos

Depois do curso, a Quayside oferece a Aisha um cargo de tecnóloga de privacidade júnior. Ela planeja estudar governança, riscos e compliance, para entender como suas verificações técnicas se encaixam em sistemas de gestão mais amplos. Sua primeira tarefa no novo cargo é repetir o teste dos pedidos de acesso. O Sr. Reilly encerra observando que o trabalho de privacidade continua depois do curso e que as perguntas que ela aprendeu a fazer continuarão úteis quaisquer que sejam as tecnologias que a Quayside adotar nos próximos anos, porque elas tratam de comportamento, e não de ferramentas.

### Exemplo resolvido

Aisha apresenta o trabalho, responde a perguntas sobre os limites e reflete sobre as verificações técnicas.

> **Caso sintético.** A avaliação é sintética.

### Erros e limites

A reflexão deve ser honesta sobre as falhas.

### Exercícios

- **EX088 — Banca.** Quem avaliou? *Rubrica:* 3 = o Sr. Reilly e o encarregado;; 2 = os dois;; 1 = um;; 0 = nenhuma.
- **EX089 — Limite perguntado.** Sobre que limite perguntaram? *Rubrica:* 3 = as anotações de saúde em texto livre;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.
- **EX090 — Próximo passo.** O que Aisha planeja a seguir? *Rubrica:* 3 = estudar governança;; 2 = parcialmente correta;; 1 = vago;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX090. Aisha Bello, o Sr. Tom Reilly, o Lindon Technical Institute, a Quayside Fitness e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX031.** Identidade, pagamento, frequência cardíaca e CFTV (também treino e marketing).

**EX032.** Que fiquem no aplicativo e sejam excluídos quando saírem da academia.

**EX033.** Os dados de frequência cardíaca e as imagens de CFTV.

**EX034.** A rede de anúncios.

**EX035.** Não tem contrato.

**EX036.** Todo SDK novo exige revisão de privacidade.

**EX037.** O vazamento dos dados de frequência cardíaca e o sequestro de conta do aplicativo.

**EX038.** Registrar e revisar os acessos às imagens.

**EX039.** Tornam os riscos concretos para quem não é especialista.

**EX040.** 47 de 287 (16%).

**EX041.** Histórico de treinos e chat de atendimento (também índice do CFTV e marketing).

**EX042.** Uma lista de verificação baseada no inventário, com um responsável por sistema.

**EX043.** 292.

**EX044.** A exclusão automática foi desligada por uma atualização de firmware.

**EX045.** Uma verificação mensal da retenção do CFTV.

**EX046.** Trata dados de saúde de forma sistemática e em escala.

**EX047.** O tratamento no aparelho.

**EX048.** Um jeito fácil de desligar a funcionalidade.

**EX049.** Três de cinco.

**EX050.** Informação de saúde em texto livre sobre uma lesão no joelho.

**EX051.** Foi movido para o sistema de pagamentos.

**EX052.** Limitação da conservação.

**EX053.** ISO/IEC 27701.

**EX054.** Revela princípios sem controles.

**EX055.** Imagens com mais de trinta e cinco dias.

**EX056.** De quarenta para duas.

**EX057.** As correções podem falhar em silêncio, como a exclusão do CFTV.

**EX058.** A rotina noturna de sincronização falhou depois de uma troca de senha.

**EX059.** Um alerta de falha e uma reconciliação semanal.

**EX060.** Revogar o consentimento deve ser tão fácil quanto dá-lo.

**EX061.** Artigo 28.

**EX062.** Nome, número de matrícula e reservas.

**EX063.** Alunos sintéticos.

**EX064.** 1.116.

**EX065.** Têm dívida em aberto.

**EX066.** Por amostragem das contas excluídas em todos os sistemas.

**EX067.** As contas esquecidas caíram de quarenta para duas.

**EX068.** As anotações de saúde em texto livre.

**EX069.** Treinar os trainers sobre as anotações.

**EX070.** Se os alunos entendem as configurações de compartilhamento da frequência cardíaca.

**EX071.** Com consentimento e sem identificadores.

**EX072.** Amostra pequena.

**EX073.** A página de configurações de privacidade.

**EX074.** Pesquisa e design.

**EX075.** O compartilhamento com as telas das aulas passou a ser explicado com clareza.

**EX076.** Verificações do CFTV e revisões de SDKs.

**EX077.** Observou-os executando cada tarefa.

**EX078.** Para que os controles continuem depois do projeto.

**EX079.** Com contas sintéticas e inspeção de rede.

**EX080.** Para se recuperar rapidamente de erros.

**EX081.** Nenhum dado de frequência cardíaca chega aos anunciantes.

**EX082.** Visitou cinco unidades.

**EX083.** Placas de CFTV.

**EX084.** Revelam problemas que as verificações remotas deixam passar.

**EX085.** Cinco scripts foram combinados.

**EX086.** Finalidade, entradas, saídas e limites.

**EX087.** Dados sintéticos.

**EX088.** O Sr. Reilly e o encarregado.

**EX089.** Detectar as anotações de saúde em texto livre que o varredor deixa passar.

**EX090.** Estudar governança.

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
