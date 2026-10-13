# Privacidade e Proteção de Dados: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 096, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–5 de 40 já estão escritos em português, com os exercícios EX001–EX015 e suas resoluções com rubricas de 0 a 3; os capítulos 6–40 (EX016–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de bacharelado que aprendem a proteger os dados de crianças e famílias em uma rede de escolas.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios consultam um registro de aplicativos em SQLite, calculam intervalos de Wilson para uma pesquisa com as famílias, resumem os tempos de resposta a pedidos de acesso, pontuam aplicativos de sala de aula, suprimem células pequenas e cruzam fotografias com registros de consentimento, sempre sobre dados sintéticos. A análise jurídica é didática e não constitui aconselhamento jurídico; a LGPD e os atos da ANPD são citados pelo texto oficial e parafraseados. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma estudante de bacharelado ao longo de quatro anos centrados em uma rede de escolas: fundamentos, sistemas e programação, escrita e letramento em segurança, dados e ética, identidade e fundamentos da privacidade, medição, arquitetura e pesquisa, escopo e casos, modelos e dependências, controle de divulgação e controles, laboratórios, consentimento, verificação, análise de falhas e operações, casos difíceis, trabalho interdisciplinar, pesquisa, comparação, prática comunitária e um portal para as famílias como projeto final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Elena Rossi** | Estudante de bacharelado | Inventada |
| **Dr. Kwame Asante** | Tutor | Inventado |
| **Fairhaven College** | Faculdade fictícia | Inventada |
| **Brindle Valley Schools Trust** | Rede fictícia de 12 escolas de ensino fundamental, com cerca de 6.000 alunos | Inventada |
| **Harrow Lane Academy** | Escola fictícia usada para comparação | Inventada |

### Fontes principais

Regulamento (UE) 2016/679 (GDPR), incluindo o considerando 38 e os artigos 7, 8, 28, 30 e 33; Lei nº 13.709/2018 (LGPD), incluindo o art. 14; Diretrizes 05/2020, 07/2020, 01/2022 e 9/2022 do EDPB; WP248 rev.01; NIST SP 800-188; Sweeney (2002); Narayanan e Shmatikov (2008); Solove (2006); Nissenbaum (2004); Acquisti et al. (2015); Warren e Brandeis (1890). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) |

Capítulos 6–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-06), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem

Você vai (1) usar a lógica para enunciar regras de privacidade com precisão; (2) identificar premissas ocultas em argumentos sobre dados; (3) raciocinar sobre proporções e taxas de base.

### 1.1 Um curso construído em torno das escolas

Elena Rossi começa um bacharelado de quatro anos no fictício Fairhaven College, com a tutoria do Dr. Kwame Asante. A parceira de seu estágio é a fictícia Brindle Valley Schools Trust, uma rede que mantém doze escolas de ensino fundamental com cerca de 6.000 alunos. As escolas guardam nomes, endereços, anotações de saúde, registros de necessidades educacionais especiais e fotografias de crianças. O Dr. Asante explica que a privacidade e a proteção de dados serão a principal matéria de Elena e que cada disciplina de fundamentos será lida pela ótica do trabalho da rede, a começar pelo raciocínio matemático. Sua primeira tarefa é contar os alunos de cada escola.

### 1.2 Regras como lógica

As regras de privacidade costumam ser escritas de forma frouxa. A política da rede diz que os funcionários podem compartilhar dados de alunos com aplicativos se for necessário e se os pais concordarem. Elena reescreve a regra como um enunciado lógico: o compartilhamento só é permitido se houver necessidade e existir uma base legal. Ela percebe que a concordância dos pais não é a única base possível; uma escola pode se apoiar no cumprimento de uma missão de interesse público para ensinar. Escrever a regra com precisão expõe a confusão. Ela aprende que a lógica é uma ferramenta para tornar as políticas testáveis antes que sejam aplicadas a crianças reais.

### 1.3 Premissas ocultas

Elena examina o argumento de uma professora: o aplicativo de leitura é seguro porque é popular entre as escolas. A premissa oculta é que a popularidade implica um tratamento cuidadoso dos dados. Ela lista outras premissas ocultas que encontra: que a página de privacidade de um fornecedor reflete sua prática, que dados anonimizados não conseguem identificar crianças e que os pais leem os formulários de consentimento. Cada premissa pode ser conferida. O Dr. Asante pede à turma que sublinhe as premissas em todo argumento que ler, um hábito que vai ajudá-los a avaliar fornecedores e políticas ao longo de todo o curso.

### 1.4 Taxas de base

Elena estuda as taxas de base. Se um aplicativo em cem trata mal os dados e uma verificação de triagem pega nove em cada dez aplicativos ruins, mas marca por engano cinco em cada cem aplicativos bons, a maioria dos aplicativos marcados é, na verdade, adequada. Ela faz as contas: de 1.000 aplicativos, dez são ruins e nove são marcados; dos 990 bons, cerca de cinquenta são marcados. Assim, só cerca de um em cada seis aplicativos marcados é ruim. A lição é que as verificações precisam ser projetadas levando em conta as taxas de base, ou os funcionários perderão a confiança nelas.

### Exemplo resolvido

Elena reescreve uma regra de compartilhamento como lógica, expõe premissas ocultas sobre aplicativos populares e mostra que uma verificação de triagem marca sobretudo aplicativos bons quando os ruins são raros.

> **Caso sintético.** O Fairhaven, a Brindle Valley e todos os números são sintéticos.

### Erros e limites

As taxas de base aqui são ilustrativas; as taxas reais precisam ser estimadas.

### Exercícios

- **EX001 — Necessidade e base.** Como Elena reescreve a regra de compartilhamento? *Rubrica:* 3 = compartilhamento permitido só se for necessário e existir base legal;; 2 = menciona necessidade;; 1 = mantém a original;; 0 = nenhuma.
- **EX002 — Premissa do aplicativo popular.** Que premissa oculta há em "o aplicativo é popular, então é seguro"? *Rubrica:* 3 = a popularidade implica tratamento cuidadoso dos dados;; 2 = cita uma premissa;; 1 = nenhuma;; 0 = nenhuma.
- **EX003 — Aplicativos marcados.** Aproximadamente que parcela dos aplicativos marcados é de fato ruim no exemplo de Elena? *Rubrica:* 3 = cerca de um em seis;; 2 = uma minoria;; 1 = a maioria;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) mapear onde ficam os dados dos alunos nos sistemas escolares; (2) distinguir o armazenamento local, em nuvem e com fornecedores; (3) relacionar o projeto dos sistemas aos deveres de proteção de dados.

### 2.1 Onde ficam os dados

Elena mapeia os sistemas da rede. O sistema de gestão escolar guarda os registros dos alunos; uma suíte de escritório em nuvem guarda documentos e e-mails; os aplicativos de sala de aula guardam dados de aprendizagem; um sistema de pagamentos guarda as contas da merenda; e as pastas compartilhadas guardam fotografias. Alguns dados ficam em servidores nas escolas, alguns na nuvem e alguns com fornecedores. Ela desenha um diagrama simples e descobre que ninguém na rede tem uma visão completa. Seu mapa vira a primeira versão do inventário que o artigo 30 do GDPR exige, e que no Brasil corresponde ao registro das operações do art. 37 da LGPD.

### 2.2 Local e nuvem

Os servidores locais dão à rede controle direto, mas exigem manutenção, que as escolas pequenas têm dificuldade de garantir. Os serviços em nuvem são mantidos pelos provedores, mas levam os dados para outra organização, que passa a ser operadora pelo GDPR. Elena lista as responsabilidades em cada modelo. Ela observa que a nuvem não é automaticamente menos privada: um serviço em nuvem bem configurado pode ser mais seguro que um servidor escolar sem atualizações. A decisão deve seguir os riscos e os contratos existentes, e não uma preferência geral por um modelo. Os contratos decidem muita coisa.

### 2.3 Dispositivos

Os alunos usam tablets compartilhados e os professores usam notebooks. Elena verifica que dados ficam nos dispositivos: documentos em cache, senhas salvas e fotografias. Um notebook de professor perdido e sem criptografia poderia expor os registros de muitas crianças. Ela recomenda criptografia de disco completo nos notebooks dos funcionários e saída automática da conta nos tablets compartilhados. Ela aprende que os dispositivos fazem parte do sistema computacional e muitas vezes são seu ponto mais fraco, porque saem da escola e são usados por muitas pessoas, com graus diferentes de cuidado. Os notebooks dos alunos vão para casa toda noite, muitas vezes divididos com irmãos.

### 2.4 Os deveres seguem o projeto

Elena conclui que o projeto dos sistemas molda os deveres de proteção de dados. Se os dados estiverem espalhados por muitos fornecedores, a rede precisa de muitos contratos e tem de atender aos pedidos de direitos em todos eles. Se estiverem centralizados, um único sistema guarda tudo e precisa ser bem protegido. O Dr. Asante observa que o artigo 25 do GDPR pede aos controladores que considerem a proteção de dados ao escolher os meios de tratamento, o que inclui escolher e configurar sistemas, e não só escrever políticas depois que os sistemas já foram instalados. É o artigo 25 na prática.

### Exemplo resolvido

Elena mapeia cinco sistemas que guardam dados de alunos, compara as responsabilidades no modelo local e na nuvem, recomenda criptografia e saída automática nos dispositivos e liga a escolha dos sistemas ao artigo 25.

> **Caso sintético.** Os sistemas da rede são sintéticos; os artigos 25 e 30 do GDPR e o art. 37 da LGPD são reais.

### Erros e limites

Um primeiro mapa deixa escapar sistemas paralelos, como planilhas pessoais; revise-o.

### Exercícios

- **EX004 — Visão ausente.** O que o mapa de sistemas de Elena revelou? *Rubrica:* 3 = ninguém tinha uma visão completa de onde ficam os dados dos alunos;; 2 = menciona lacunas;; 1 = nada;; 0 = nenhuma.
- **EX005 — A nuvem não é automática.** Por que o armazenamento em nuvem não é automaticamente menos privado? *Rubrica:* 3 = uma nuvem bem configurada pode ser mais segura que um servidor escolar sem atualizações;; 2 = menciona configuração;; 1 = diz que a nuvem é pior;; 0 = nenhuma.
- **EX006 — Controles nos dispositivos.** Que controles nos dispositivos Elena recomenda? *Rubrica:* 3 = criptografia de disco completo nos notebooks e saída automática nos tablets compartilhados;; 2 = um;; 1 = nenhum;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem

Você vai (1) escrever pequenos programas que tratem dados de alunos com segurança; (2) evitar expor dados nas saídas; (3) usar dados sintéticos para praticar.

### 3.1 Primeiro, dados sintéticos

Os primeiros programas de Elena calculam percentuais de frequência. O Dr. Asante insiste que toda a prática use alunos sintéticos gerados por um script, nunca exportações reais da rede. Elena escreve um gerador que produz nomes, turmas e registros de frequência com padrões realistas. Ela aprende que os dados sintéticos permitem errar com segurança, compartilhar código com os colegas e publicar exemplos. A regra protege as crianças e também ensina um hábito que os desenvolvedores profissionais deveriam manter, porque dados reais em ambientes de prática são uma fonte frequente de vazamentos.

### 3.2 Saídas e exposição

O programa de frequência imprime uma lista dos alunos com frequência abaixo de noventa por cento. Elena percebe que, se a lista fosse impressa e esquecida numa mesa da sala dos professores, revelaria informações sensíveis sobre as famílias. Ela muda o programa para imprimir contagens por turma para o uso geral e gerar a lista nominal apenas para o responsável pela frequência, salva em uma pasta protegida. Decidir quem vê qual saída é uma decisão de programação tanto quanto de política, e o código pode impor essa decisão.

### 3.3 Verificação das entradas

O programa lê uma planilha. Elena acrescenta verificações que rejeitam colunas inesperadas, como uma coluna de anotações de saúde incluída por engano em uma exportação. Se a coluna aparecer, o programa para e explica por quê. Isso impede o programa de tratar dados de que não precisa. Ela explica que a verificação das entradas implementa a minimização de dados no ponto em que os dados entram no programa, e que falhar de forma ruidosa é melhor do que tratar em silêncio dados sensíveis que nunca deveriam estar ali. Seu script rejeita as colunas inesperadas.

### 3.4 Comentários que explicam o porquê

Elena escreve comentários que explicam as decisões de privacidade, como o motivo de a lista nominal ser salva apenas em uma pasta protegida. Um colega que revisa o código entende o motivo e não o altera. O Dr. Asante observa que os comentários que explicam o porquê valem mais que os que explicam o quê, porque o próprio código já mostra o que faz. O raciocínio de privacidade se perde com facilidade quando o código muda de mãos, e explicações curtas o mantêm junto do código que o impõe. Seus comentários nomeiam a finalidade de cada decisão.

### Exemplo resolvido

Elena pratica com alunos gerados, imprime contagens por turma para o uso geral e listas nominais só para o responsável pela frequência, rejeita colunas de saúde inesperadas e documenta seus motivos em comentários.

> **Caso sintético.** Os programas e os alunos são sintéticos.

### Erros e limites

Os dados sintéticos podem não ter os casos extremos reais; acrescente-os de propósito.

### Exercícios

- **EX007 — Prática sintética.** Por que a prática precisa usar alunos sintéticos? *Rubrica:* 3 = os erros e o compartilhamento são seguros, e os dados reais continuam protegidos;; 2 = menciona segurança;; 1 = dados reais servem;; 0 = nenhuma.
- **EX008 — Duas saídas.** Como Elena muda a saída de frequência? *Rubrica:* 3 = contagens por turma para o uso geral; lista nominal só para o responsável pela frequência;; 2 = uma parte;; 1 = imprime nomes;; 0 = nenhuma.
- **EX009 — Coluna inesperada.** O que o programa faz com uma coluna de saúde inesperada? *Rubrica:* 3 = para e explica;; 2 = avisa;; 1 = trata a coluna;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem

Você vai (1) escrever um ensaio argumentativo sobre uma questão de privacidade; (2) citar corretamente fontes jurídicas e acadêmicas; (3) distinguir descrição de argumentação.

### 4.1 A questão do ensaio

O primeiro ensaio de Elena pergunta: as escolas devem publicar fotografias de alunos em sites públicos? Ela precisa tomar uma posição e sustentá-la. Pesquisa as disposições do GDPR sobre base legal e consentimento, incluindo o artigo 8, sobre o consentimento de crianças para serviços online, e o art. 14 da LGPD, que trata dos dados de crianças e adolescentes, e lê trabalhos acadêmicos sobre a privacidade infantil. Decide argumentar que as escolas só podem publicar fotografias com consentimento claro e específico dos pais e, à medida que as crianças crescem, delas próprias, e somente quando a finalidade for relevante. Sua tese enuncia isso em uma frase.

### 4.2 Citar corretamente

O Dr. Asante ensina a citar. As leis são citadas pelo número e pelo artigo, como Regulamento (UE) 2016/679, artigo 6, ou Lei nº 13.709/2018, art. 7º. As obras acadêmicas são citadas com autor, ano e título, e uma lista de referências traz os detalhes completos. Elena confere cada citação no texto original, em vez de copiar de resumos secundários. Ela descobre que um blog cita errado o GDPR, dizendo que o consentimento é sempre exigido para fotografias. Citar o texto original permite que ela não repita o erro e fortalece seu argumento. A fonte era o blog de uma escola.

### 4.3 Descrição e argumentação

O primeiro rascunho de Elena descreve a lei longamente, mas argumenta pouco. O Dr. Asante marca os parágrafos que apenas descrevem. Ela revisa o texto para que cada parágrafo faça uma afirmação, apresente evidências e explique como as evidências sustentam a afirmação. Por exemplo, ela argumenta que o consentimento para fotografias só tem sentido se a recusa não trouxer consequências, porque as diretrizes do EDPB sobre consentimento dizem que ele precisa ser livre. O ensaio revisado é mais curto, porém mais persuasivo. O primeiro rascunho listava regras; o segundo explica por que cada uma protege os alunos.

### 4.4 Contra-argumentos

Um ensaio forte enfrenta as objeções. Elena considera o argumento de que as fotografias celebram conquistas e fortalecem a comunidade. Ela reconhece o valor, mas argumenta que boletins internos e páginas protegidas por senha podem atingir a mesma finalidade com menos exposição. Também considera que alunos mais velhos podem querer suas conquistas exibidas. Conclui que as opiniões das próprias crianças devem ganhar peso com a idade. Enfrentar os contra-argumentos, ela aprende, mostra ao leitor que a posição resiste ao escrutínio, em vez de ignorá-lo. Um dos contra-argumentos diz respeito às tradições da escola. Sua resposta cita a lei.

### Exemplo resolvido

Elena argumenta que as fotografias escolares exigem consentimento claro e específico, com peso crescente para a opinião das crianças, cita diretamente o GDPR, a LGPD e as orientações do EDPB e responde às objeções sobre o fortalecimento da comunidade.

> **Caso sintético.** O ensaio é sintético; os artigos 6 e 8 do GDPR, os arts. 7º e 14 da LGPD e as Diretrizes 05/2020 do EDPB são reais.

### Erros e limites

O consentimento é uma base legal entre várias; as escolas podem se apoiar em outras para parte do tratamento.

### Exercícios

- **EX010 — Fontes originais.** Por que conferir as citações no texto legal original? *Rubrica:* 3 = fontes secundárias podem citar errado, como um blog fez sobre o consentimento para fotos;; 2 = menciona exatidão;; 1 = confia em blogs;; 0 = nenhuma.
- **EX011 — Estrutura do parágrafo.** O que cada parágrafo argumentativo deve conter? *Rubrica:* 3 = uma afirmação, evidências e uma explicação que as ligue;; 2 = dois;; 1 = descrição;; 0 = nenhuma.
- **EX012 — Resposta às objeções.** Como Elena responde à objeção do fortalecimento da comunidade? *Rubrica:* 3 = canais internos ou protegidos atingem a finalidade com menos exposição;; 2 = menciona alternativas;; 1 = ignora;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) reconhecer as ameaças comuns aos dados escolares; (2) explicar as proteções básicas aos funcionários; (3) relacionar incidentes de segurança à proteção de dados.

### 5.1 Ameaças às escolas

Elena estuda as ameaças que as escolas enfrentam: e-mails de phishing que se passam por pais ou fornecedores, ransomware que cifra os registros, dispositivos perdidos e e-mails enviados ao destinatário errado. Ela lê que as escolas são alvos atraentes porque guardam dados valiosos e muitas vezes têm pouca equipe de segurança. Ela lista os incidentes mais prováveis da rede e descobre que os e-mails enviados ao destinatário errado, como mandar o boletim de uma família para outra, são os mais frequentes, embora o ransomware receba mais atenção do noticiário. A revisão do registro de incidentes sustenta claramente essa ordenação.

### 5.2 Explicar as proteções

Elena prepara uma sessão curta para os professores. Explica senhas fortes com um gerenciador de senhas, autenticação multifator no e-mail, conferência dos destinatários antes do envio e bloqueio de tela. Usa exemplos de escolas, e não de bancos. Evita culpar os funcionários pelos erros, explicando que os sistemas devem tornar fácil a escolha segura, por exemplo avisando quando um e-mail vai para um endereço externo. Os professores respondem melhor a conselhos práticos do que a alertas sobre hackers. Um exemplo: confirmar os anexos antes de enviar para fora da rede. Os professores adotam as orientações depressa.

### 5.3 Incidentes são eventos de proteção de dados

Elena aprende que um incidente de segurança que envolva dados pessoais pode ser uma violação de dados pessoais pelo GDPR. Enviar o boletim de um aluno ao pai errado é uma violação, mesmo que acidental. A rede precisa avaliar o risco e, a menos que a violação não seja suscetível de gerar risco para as pessoas, notificar a autoridade de controle em até 72 horas, pelo artigo 33. No Brasil, o art. 48 da LGPD e a Resolução CD/ANPD nº 15/2024 tratam do mesmo dever com um relógio próprio: três dias úteis para comunicar a ANPD. Ela observa que muitos funcionários acham que as violações só envolvem hackers, então o treinamento precisa cobrir os erros do dia a dia.

### 5.4 Cultura

Elena reflete sobre a cultura de segurança. Funcionários que temem punição escondem os erros, o que atrasa a resposta. Ela recomenda um processo de comunicação que agradeça a quem relata depressa e se concentre em corrigir os problemas. O Dr. Asante concorda, observando que relatar rápido é essencial quando corre o relógio de 72 horas. Elena escreve um guia de uma página intitulado O que fazer se você enviar algo para a pessoa errada, que orienta os funcionários a comunicar imediatamente o responsável pela proteção de dados e a não tentar resolver sozinhos. A rapidez é o que mais importa.

### Exemplo resolvido

Elena identifica os e-mails enviados ao destinatário errado como a ameaça mais frequente, treina os professores com exemplos escolares, explica que as divulgações acidentais são violações pelo artigo 33 e promove uma cultura de comunicação sem culpa.

> **Caso sintético.** Os incidentes são sintéticos; o artigo 33 do GDPR, o art. 48 da LGPD e a Resolução CD/ANPD nº 15/2024 são reais.

### Erros e limites

Sem culpa não significa sem responsabilização; comportamentos descuidados repetidos ainda exigem gestão.

### Exercícios

- **EX013 — Incidente mais frequente.** Qual é o incidente mais frequente na rede? *Rubrica:* 3 = e-mails enviados ao destinatário errado;; 2 = menciona e-mail;; 1 = ransomware;; 0 = nenhuma.
- **EX014 — Violação acidental.** Enviar um boletim ao pai errado é uma violação? *Rubrica:* 3 = sim; a divulgação acidental conta;; 2 = sim;; 1 = não;; 0 = nenhuma.
- **EX015 — Cultura de comunicação.** Por que agradecer aos funcionários que relatam erros depressa? *Rubrica:* 3 = o medo atrasa a comunicação, e o relógio de 72 horas exige rapidez;; 2 = menciona rapidez;; 1 = punir;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX015 (as de EX016–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Elena Rossi, o Dr. Kwame Asante, o Fairhaven College, a Brindle Valley Schools Trust e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** O compartilhamento só é permitido quando há necessidade e existe uma base legal, que não precisa ser o consentimento dos pais.

**EX002.** Que o uso amplo significa que o fornecedor trata adequadamente os dados das crianças.

**EX003.** Cerca de um em seis: 9 de aproximadamente 59 aplicativos marcados.

**EX004.** Que ninguém na rede tinha um quadro completo de onde os dados dos alunos estavam guardados.

**EX005.** A segurança depende da configuração e da manutenção, então um serviço em nuvem bem gerido pode ser mais seguro que um servidor local negligenciado.

**EX006.** Criptografia de disco completo nos notebooks dos funcionários e saída automática nos tablets compartilhados.

**EX007.** Os dados sintéticos permitem errar e compartilhar com segurança, sem expor as crianças.

**EX008.** Os usuários em geral recebem contagens por turma; só o responsável pela frequência recebe a lista nominal protegida.

**EX009.** Ele se recusa a rodar e explica que a coluna não é necessária.

**EX010.** Porque os resumos podem estar errados, como um blog que descreveu mal as regras de consentimento para fotografias.

**EX011.** Uma afirmação, evidências que a sustentem e uma explicação de como as evidências a sustentam.

**EX012.** Boletins e páginas protegidos podem celebrar os alunos com menos exposição.

**EX013.** E-mails enviados ao destinatário errado, como o boletim de uma família mandado para outra.

**EX014.** Sim, é uma violação de dados pessoais, mesmo sendo acidental.

**EX015.** O medo faz as pessoas esconderem erros; a comunicação rápida é necessária para avaliar e notificar a tempo.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da Resolução CD/ANPD nº 15, de 24 de abril de 2024, citada nesta edição como referência brasileira e conferida em sua fonte oficial; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Acquisti, A., Brandimarte, L., & Loewenstein, G. (2015). Privacy and human behavior in the age of information. *Science, 347*(6221), 509–514. <https://doi.org/10.1126/science.aaa1465>
- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Brasil. Agência Nacional de Proteção de Dados. (2024). *Resolução CD/ANPD nº 15, de 24 de abril de 2024 — Aprova o Regulamento de Comunicação de Incidente de Segurança*. Diário Oficial da União. <https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
- European Data Protection Board. (2021). *Guidelines 07/2020 on the concepts of controller and processor in the GDPR* (Version 2.0 adopted 7 July 2021; Version 2.1, 20 September 2022). <https://www.edpb.europa.eu/documents/guideline/guidelines-072020-on-the-concepts-of-controller-and-processor-in-the-gdpr_en>
- European Data Protection Board. (2023). *Guidelines 01/2022 on data subject rights — Right of access* (Version 2.0 adopted 28 March 2023; Version 2.1 with minor corrections, 30 May 2024). <https://www.edpb.europa.eu/documents/guideline/guidelines-012022-on-data-subject-rights-right-of-access_en>
- European Data Protection Board. (2023). *Guidelines 9/2022 on personal data breach notification under GDPR* (Version 2.0, adopted 28 March 2023). <https://www.edpb.europa.eu/documents/guideline/guidelines-92022-on-personal-data-breach-notification-under-gdpr_en>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). NIST. <https://doi.org/10.6028/NIST.SP.800-188>
- Narayanan, A., & Shmatikov, V. (2008). Robust de-anonymization of large sparse datasets. *IEEE Symposium on Security and Privacy*, 111–125. <https://doi.org/10.1109/SP.2008.33>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
- Solove, D. J. (2006). A taxonomy of privacy. *University of Pennsylvania Law Review, 154*(3), 477–564. <https://doi.org/10.2307/40041279>
- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570. <https://doi.org/10.1142/S0218488502001648>
- Warren, S. D., & Brandeis, L. D. (1890). The right to privacy. *Harvard Law Review, 4*(5), 193–220. <https://doi.org/10.2307/1321160>
