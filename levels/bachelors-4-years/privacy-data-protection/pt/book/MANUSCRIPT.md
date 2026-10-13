# Privacidade e Proteção de Dados: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 096, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–20 de 40 já estão escritos em português, com os exercícios EX001–EX060 e suas resoluções com rubricas de 0 a 3 e 3 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 21–40 (EX061–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

Capítulos 21–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-21), até a chegada dos próximos lotes.

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

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem

Você vai (1) usar conjuntos e relações para modelar o compartilhamento de dados; (2) contar as combinações que identificam alunos; (3) usar grafos para rastrear fluxos de dados.

### 6.1 Conjuntos de dados

Elena modela os dados da rede como conjuntos: todos os dados pessoais, os dados de categorias especiais, como saúde e religião, e os dados de crianças com necessidades educacionais especiais. Ela observa que alguns dados pertencem a vários conjuntos. Uma lista de alunos com restrições alimentares pode revelar religião ou condição de saúde. Pensar em conjuntos a ajuda a ver que dados de aparência comum podem cair em categorias sensíveis, que o artigo 9 do GDPR protege com condições mais estritas e que a LGPD chama de dados pessoais sensíveis (art. 5º, II). Ela usa diagramas de Venn no relatório para a rede. Os dados de saúde são um exemplo.

### 6.2 Contagem de identidades

Elena conta quantos alunos compartilham combinações de atributos em uma escola pequena: ano escolar, sexo e primeira língua. Em uma escola de duzentos alunos, algumas combinações contêm uma única criança. Publicar uma tabela de resultados por esses atributos poderia identificar essa criança. Ela liga isso ao trabalho de Sweeney (2002) sobre como combinações de atributos comuns identificam pessoas. O exercício de contagem mostra por que as estatísticas de escolas pequenas exigem cuidado especial antes de serem publicadas. Numa escola com um único aluno de determinada idade e etnia, as contagens identificam essa criança.

### 6.3 Relações

Uma relação forma pares de elementos de dois conjuntos. Elena modela como relação quais funções da equipe podem acessar quais categorias de dados. Os professores acessam os registros de aprendizagem; a secretaria acessa os dados de contato; a coordenadora de necessidades especiais acessa os planos de apoio. Ela confere a relação com o princípio do privilégio mínimo e descobre que a secretaria também consegue acessar os planos de apoio, de que não precisa. O modelo torna o problema visível de um jeito que uma lista de permissões num menu de software não tornava. Remover esse par restringe o acesso.

### 6.4 Grafos de fluxos

Elena desenha os fluxos de dados da rede como um grafo dirigido: das famílias para as escolas, das escolas para os aplicativos, dos aplicativos para os suboperadores dos fornecedores. Ela encontra caminhos que saem da rede em várias etapas, como um aplicativo de leitura que repassa dados a um provedor de análise. Um caminho, observa, é tão protegido quanto seu elo mais fraco. O grafo a prepara para os capítulos seguintes, em que ela vai verificar se cada aresta tem base legal e contrato. Cada aresta é um fluxo de dados que precisa de justificativa.

### Exemplo resolvido

Elena modela as categorias de dados como conjuntos, conta as combinações que identificam alunos em escolas pequenas, modela o acesso por função como uma relação (descobrindo o acesso da secretaria aos planos de apoio) e rastreia fluxos de várias etapas como um grafo.

> **Caso sintético.** Os modelos são sintéticos; o artigo 9 do GDPR, o art. 5º da LGPD e Sweeney (2002) são reais.

### Erros e limites

Os modelos simplificam; o acesso real costuma ter exceções que as tabelas de funções não capturam.

### Exercícios

- **EX016 — Comum, mas sensível.** Dê um exemplo de dado de aparência comum que pode ser de categoria especial. *Rubrica:* 3 = restrições alimentares que revelam religião ou saúde;; 2 = dá um exemplo;; 1 = nenhum;; 0 = nenhuma.
- **EX017 — Achado na relação de acesso.** O que a relação de acesso revelou? *Rubrica:* 3 = a secretaria podia acessar planos de apoio de que não precisa;; 2 = menciona a secretaria;; 1 = nada;; 0 = nenhuma.
- **EX018 — O elo mais fraco.** Por que um caminho de dados com várias etapas é tão protegido quanto seu elo mais fraco? *Rubrica:* 3 = os dados podem vazar em qualquer etapa, como um suboperador;; 2 = menciona etapas;; 1 = o mais forte;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) identificar o que o tráfego da rede escolar revela; (2) entender a filtragem e o monitoramento; (3) equilibrar a proteção das crianças com a privacidade.

### 7.1 Redes escolares

Elena estuda a rede de computadores da rede de escolas. Os dispositivos dos alunos se conectam pelo Wi-Fi da escola, que passa por um filtro web. O filtro registra cada site visitado por um dispositivo. A criptografia protege o conteúdo, mas o filtro vê os nomes de domínio. Elena percebe que os logs revelam informações sensíveis, como buscas sobre problemas de saúde ou de família, e que se referem a crianças identificáveis quando os dispositivos são atribuídos aos alunos. O projeto da rede cria, portanto, um volume significativo de dados pessoais cuja existência muitos funcionários nem conhecem. Os logs são dados pessoais.

### 7.2 Filtragem e monitoramento

As escolas costumam ter deveres de proteção que as obrigam a resguardar as crianças de conteúdos nocivos. Elena aprende que a filtragem e o monitoramento podem apoiar esses deveres, mas precisam ser proporcionais. Ela revisa as configurações do filtro e descobre logs guardados por três anos e acessíveis a toda a equipe de TI. Recomenda uma retenção mais curta, acesso limitado aos responsáveis designados pela proteção das crianças e informação clara a alunos e famílias sobre o que é monitorado. Ela observa que a transparência faz parte da lealdade, mesmo quando o monitoramento se justifica. Os alunos veem um aviso ao entrar.

### 7.3 Criptografia em trânsito

Elena verifica se o sistema de gestão escolar e os aplicativos usam conexões cifradas. Um aplicativo legado usado por uma escola envia nomes de alunos sem criptografia na rede local. Ela leva o caso à equipe de TI, que o substitui. Explica aos professores que as conexões cifradas impedem que outras pessoas na mesma rede leiam os dados, o que importa nas escolas, onde muitos dispositivos compartilham as redes. Ela confere o sistema de gestão escolar e o portal das famílias e encontra os dois cifrados, mas um serviço de impressão legado envia listas de turma em texto claro pela rede, e a TI o substitui nas férias seguintes.

### 7.4 Equilíbrio de deveres

Elena discute com o Dr. Asante como equilibrar a proteção das crianças e a privacidade. As duas querem proteger as crianças. O monitoramento excessivo pode desencorajar os alunos de buscar ajuda online sobre assuntos sensíveis, enquanto o monitoramento insuficiente pode deixar passar riscos graves. Ela escreve que a rede deve declarar com clareza a finalidade do monitoramento, limitá-lo a essa finalidade e revisá-lo com regularidade. A discussão lhe mostra que a privacidade não se opõe à segurança, mas precisa ser ponderada com ela de forma cuidadosa e aberta. Os logs de monitoramento passam a ser guardados por um período letivo.

### Exemplo resolvido

Elena encontra logs do filtro web que revelam buscas sensíveis guardados por três anos, recomenda retenção mais curta e acesso restrito aos responsáveis pela proteção das crianças, substitui um aplicativo sem criptografia e trata o monitoramento como um equilíbrio de deveres.

> **Caso sintético.** A rede e o filtro são sintéticos.

### Erros e limites

As exigências de proteção das crianças variam de país para país; consulte as orientações locais.

### Exercícios

- **EX019 — Logs do filtro.** Por que os logs do filtro web são sensíveis? *Rubrica:* 3 = revelam buscas das crianças sobre saúde ou questões familiares;; 2 = menciona buscas;; 1 = não são pessoais;; 0 = nenhuma.
- **EX020 — Retenção do filtro.** O que Elena recomendou para os logs do filtro? *Rubrica:* 3 = retenção mais curta, acesso só para os responsáveis pela proteção e transparência;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX021 — Dano do monitoramento excessivo.** Como o monitoramento excessivo pode prejudicar as crianças? *Rubrica:* 3 = pode desencorajá-las de buscar ajuda online sobre assuntos sensíveis;; 2 = menciona efeito inibidor;; 1 = nenhum;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem

Você vai (1) implementar verificações de acesso; (2) pseudonimizar dados para análise; (3) testar o comportamento de privacidade.

### 8.1 Verificações de acesso

Elena escreve um pequeno aplicativo para consultar informações dos alunos. Antes de mostrar qualquer registro, ele verifica a função do usuário e a finalidade. Um professor pode ver os registros de aprendizagem dos alunos de suas turmas; a coordenadora de necessidades especiais pode ver os planos de apoio. Os pedidos sem uma função válida são recusados e registrados. Ela aprende que escrever as verificações no código garante que as regras sejam aplicadas de forma consistente, em vez de depender de os funcionários lembrarem quais dados devem consultar. Cada pedido confere a lista da turma.

### 8.2 Análise pseudonimizada

A rede quer analisar o progresso da leitura entre as escolas. Elena escreve um código que substitui os identificadores dos alunos por pseudônimos usando um hash com chave antes que os dados cheguem ao analista. A chave fica com o responsável pela proteção de dados. Ela explica que o analista pode estudar o progresso sem saber quem é cada criança, mas que os dados continuam sendo pessoais pelo GDPR, porque a chave poderia reidentificar os alunos. A pseudonimização reduz o risco, mas não elimina os deveres legais. A chave fica guardada separadamente dos dados, como pede o art. 13, § 4º, da LGPD.

### 8.3 Testes

Elena escreve testes que verificam o comportamento de privacidade: um professor não consegue ver um aluno de outra turma, a exportação para análise não contém nomes e os logs registram cada acesso. Um teste falha porque um professor que deixou uma turma ainda tem acesso a ela. Ela acrescenta uma regra para remover o acesso quando as atribuições de turma mudam. Testar automaticamente as propriedades de privacidade encontra problemas que a revisão manual deixaria passar e continua funcionando à medida que o código muda. Um teste reprovado impede a implantação da mudança. Os testes rodam a cada mudança, apenas com turmas sintéticas.

### 8.4 Revisão de código

O código de Elena é revisado por um colega, que pergunta por que a exportação inclui a data de nascimento. Elena percebe que ela não é necessária para o progresso da leitura e a remove. O Dr. Asante observa que os revisores devem perguntar que dados são necessários, além de verificar se o código funciona. A revisão de código vira uma verificação de minimização, além de uma verificação de qualidade, e pequenas remoções como essa se somam ao longo de muitos programas. Em uma revisão, ela tira um campo de data de nascimento de uma exportação. Os revisores perguntam por que cada campo existe.

### Exemplo resolvido

Elena implementa verificações de acesso baseadas na função e na turma, pseudonimiza os dados de leitura com um hash com chave, encontra por meio de testes acessos remanescentes a turmas antigas e remove a data de nascimento depois da revisão.

> **Caso sintético.** O código e os alunos são sintéticos.

### Erros e limites

Os pseudônimos com chave podem ser revertidos por quem tiver a chave; proteja-a.

### Exercícios

- **EX022 — Acesso por turma.** Como o aplicativo de Elena decide se um professor vê um registro? *Rubrica:* 3 = verificações de função e finalidade, mais a participação na turma;; 2 = menciona a função;; 1 = mostra tudo;; 0 = nenhuma.
- **EX023 — Pseudonimizado, ainda pessoal.** Por que o conjunto de leitura pseudonimizado continua sendo de dados pessoais? *Rubrica:* 3 = a chave pode reidentificar os alunos;; 2 = menciona a chave;; 1 = anônimo;; 0 = nenhuma.
- **EX024 — Acesso remanescente.** Que teste reprovado Elena corrigiu? *Rubrica:* 3 = professores que mantinham o acesso depois de deixar uma turma;; 2 = menciona acesso;; 1 = nenhum;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Dados e bancos de dados

### Objetivos de aprendizagem

Você vai (1) consultar um banco de dados para encontrar riscos de compartilhamento; (2) relacionar os contratos aos fluxos de dados; (3) recomendar ações a partir dos resultados das consultas.

### 9.1 Um banco de dados de compartilhamento

Elena monta um pequeno banco de dados SQLite dos aplicativos de sala de aula e dos dados de alunos que cada um recebe, a partir de uma versão sintética dos registros da rede. Cada aplicativo tem um fornecedor, uma região e uma marcação que indica se há um contrato de tratamento de dados assinado. O artigo 28 do GDPR exige um contrato com os operadores. O banco permite fazer perguntas que uma planilha torna difíceis, como quais aplicativos recebem dados sem contrato e quantos alunos eles afetam. Ele usa apenas o sqlite3 da biblioteca padrão.

### 9.2 A consulta

O laboratório junta os aplicativos com os campos compartilhados e filtra os aplicativos sem contrato. Aparecem três. O ClassChat, sediado no EEE, recebe nomes e endereços de e-mail de 3.100 alunos. O ReadAlong, sediado nos Estados Unidos, recebe nomes, níveis de leitura e uma marcação de necessidades educacionais especiais de até 1.800 alunos. O QuizBlitz, nos Estados Unidos, recebe nomes de 900 alunos. No total, há 5.800 compartilhamentos aluno-aplicativo sem contrato, contando cada aluno uma vez por aplicativo. A consulta junta a tabela de aplicativos com a de contratos e conta os alunos por aplicativo.

### 9.3 Leitura do resultado

Elena observa que o ReadAlong é o caso mais grave. Ele recebe uma marcação de necessidades educacionais especiais, que pode ser dado de saúde, envia dados para fora do EEE e não tem contrato. O ClassChat afeta mais alunos, mas guarda dados menos sensíveis. Ela ordena os aplicativos pela sensibilidade, pela transferência e pela escala, e não só pela escala. Explica que uma consulta ao banco dá fatos, mas é preciso julgamento para decidir quais fatos importam mais para as crianças. O QuizBlitz, apesar dos números menores, também exige atenção, porque seus dados saem da Europa.

### 9.4 Recomendações

Elena recomenda suspender o ReadAlong até que haja contrato e mecanismo de transferência e que a marcação de necessidades especiais seja removida; obter um contrato para o ClassChat; e avaliar se o QuizBlitz é mesmo necessário. Também recomenda que a rede mantenha o banco atualizado à medida que os aplicativos mudam, transformando-o em um registro vivo. O Dr. Asante observa que um registro consultado com regularidade é mais útil que uma planilha de auditoria pontual. Cada novo aplicativo é incluído antes que os professores comecem a usá-lo. Os próprios professores podem consultá-lo.

### Laboratório — Aplicativos de sala de aula que recebem dados de alunos sem contrato

```python
# SQLite: which classroom apps receive pupil data without a signed data processing agreement?
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE app(name TEXT, vendor TEXT, dpa INTEGER, region TEXT);
CREATE TABLE share(app TEXT, field TEXT, pupils INTEGER);
INSERT INTO app VALUES ('MathsQuest','Qbit Ltd',1,'EEA'),('ReadAlong','Fable Inc',0,'US'),('ClassChat','Talko',0,'EEA'),
 ('Timetabler','Sched AB',1,'EEA'),('QuizBlitz','Blitz LLC',0,'US'),('LunchPay','Payfair',1,'EEA');
INSERT INTO share VALUES ('MathsQuest','name',2400),('MathsQuest','year_group',2400),('ReadAlong','name',1800),('ReadAlong','reading_level',1800),
 ('ReadAlong','sen_flag',140),('ClassChat','name',3100),('ClassChat','email',3100),('Timetabler','name',6000),('QuizBlitz','name',900),
 ('LunchPay','name',6000),('LunchPay','free_meals',1150);
""")
q = """SELECT a.name, a.region, GROUP_CONCAT(s.field), MAX(s.pupils) FROM app a JOIN share s ON s.app=a.name
       WHERE a.dpa=0 GROUP BY a.name ORDER BY MAX(s.pupils) DESC"""
for n, reg, f, p in db.execute(q): print(f"{n:10s} {reg:4s} fields={f:28s} pupils={p}")
print("pupil-app shares without a DPA (a pupil may count in several apps):", db.execute("SELECT SUM(m) FROM (SELECT MAX(s.pupils) m FROM app a JOIN share s ON s.app=a.name WHERE a.dpa=0 GROUP BY a.name)").fetchone()[0])
```

Execute com `python3 lab_sqlite.py`. Saída verificada:

```text
ClassChat  EEA  fields=email,name                   pupils=3100
ReadAlong  US   fields=name,reading_level,sen_flag  pupils=1800
QuizBlitz  US   fields=name                         pupils=900
pupil-app shares without a DPA (a pupil may count in several apps): 5800
```

### Exemplo resolvido

A consulta de Elena encontra três aplicativos sem contrato (5.800 compartilhamentos aluno-aplicativo), põe o ReadAlong em primeiro lugar por causa da marcação de necessidades especiais e da transferência para os Estados Unidos e recomenda suspensão, contratos e um registro vivo.

> **Caso sintético.** Os aplicativos e as contagens são sintéticos; o artigo 28 do GDPR é real.

### Erros e limites

Contar alunos por aplicativo conta duas vezes as crianças que usam vários aplicativos.

### Exercícios

- **EX025 — Aplicativos sem contrato.** Quais aplicativos não têm contrato de tratamento de dados? *Rubrica:* 3 = ClassChat, ReadAlong, QuizBlitz;; 2 = dois;; 1 = um;; 0 = nenhuma.
- **EX026 — O mais grave.** Por que o ReadAlong é o caso mais grave? *Rubrica:* 3 = marcação de necessidades especiais, transferência para os EUA e ausência de contrato;; 2 = dois motivos;; 1 = escala;; 0 = nenhuma.
- **EX027 — Registro vivo.** Por que manter o banco como um registro vivo? *Rubrica:* 3 = os aplicativos mudam, então consultas regulares encontram novas lacunas;; 2 = menciona atualizações;; 1 = auditoria pontual;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Ética e prática autorizada

### Objetivos de aprendizagem

Você vai (1) aplicar princípios éticos ao trabalho com dados de crianças; (2) definir os limites da prática autorizada; (3) lidar com pedidos fora da própria autoridade.

### 10.1 O interesse das crianças

Elena estuda a ética do trabalho com dados de crianças. As crianças podem ter menos consciência dos riscos e menos capacidade de exercer seus direitos. O considerando 38 do GDPR diz que as crianças merecem proteção específica, e o art. 14 da LGPD exige que o tratamento de dados de crianças e adolescentes seja realizado em seu melhor interesse. Ela escreve que seu trabalho na rede deve sempre perguntar o que é melhor para as crianças, e não só o que é lícito ou conveniente para os adultos. Essa vira sua regra de trabalho para cada decisão. Ser lícito não basta.

### 10.2 Prática autorizada

Durante o estágio, Elena tem acesso a dados sintéticos e às configurações reais dos sistemas, mas não aos registros reais dos alunos. O Dr. Asante explica que prática autorizada significa fazer apenas o que o termo de estágio permite. Quando uma professora se oferece para lhe mostrar uma planilha real para ajudá-la a entender um problema, ela recusa com educação e pede um exemplo sintético. Ela registra a oferta e sua resposta no diário do estágio. O supervisor aprova a resposta e fornece os dados sintéticos de que ela precisava para continuar o trabalho.

### 10.3 Pedidos fora da autoridade

Uma diretora pede a Elena que verifique, olhando os logs de e-mail, se a reclamação de um pai sobre uma violação de dados procede. Elena explica que investigar uma reclamação exige autorização do responsável pela proteção de dados e um acesso que ela não tem. Ela encaminha o pedido ao responsável. Aprende que boas intenções não criam autoridade, e que sair de seu papel poderia prejudicar as pessoas que ela quer ajudar e minar a confiança na investigação. Ela repassa o pedido a quem tem competência para tratá-lo, e registra o encaminhamento no diário.

### 10.4 Valores profissionais

Elena reflete sobre valores: respeito pelas crianças e pelas famílias, honestidade sobre os riscos e humildade quanto aos próprios limites. Ela escreve um código pessoal curto para o estágio. O Dr. Asante a incentiva a revisitá-lo todo ano. Ele explica que os códigos profissionais da computação e da proteção de dados compartilham esses valores, e que o hábito de refletir sobre eles prepara os estudantes para decisões difíceis que as regras sozinhas não resolvem. Seu diário reflexivo registra um dilema por semana, com o que ela decidiu e por quê.

### Exemplo resolvido

Elena põe no centro o melhor interesse das crianças, recusa uma planilha real, encaminha a investigação de uma reclamação ao responsável pela proteção de dados e escreve um código pessoal de valores.

> **Caso sintético.** Os acontecimentos do estágio são sintéticos; o considerando 38 do GDPR e o art. 14 da LGPD são reais.

### Erros e limites

Os códigos pessoais podem ser vagos; ligue cada valor a um comportamento concreto.

### Exercícios

- **EX028 — Proteção das crianças.** Que dispositivos enfatizam a proteção especial dos dados de crianças? *Rubrica:* 3 = o considerando 38 do GDPR e o art. 14 da LGPD;; 2 = um;; 1 = nenhum;; 0 = nenhuma.
- **EX029 — Recusar dados reais.** Por que Elena recusa a planilha real? *Rubrica:* 3 = seu estágio só autoriza dados sintéticos;; 2 = menciona autoridade;; 1 = aceita;; 0 = nenhuma.
- **EX030 — Encaminhar a reclamação.** Por que encaminhar a investigação da reclamação ao responsável pela proteção de dados? *Rubrica:* 3 = exige autoridade e acesso que ela não tem;; 2 = menciona o papel;; 1 = investiga;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) configurar contas e permissões nos dispositivos escolares; (2) gerir logs e arquivos temporários; (3) planejar o descarte seguro de dispositivos.

### 11.1 Contas em dispositivos compartilhados

Elena estuda como os sistemas operacionais gerenciam contas. Nos computadores compartilhados das salas de aula, os alunos entram com contas individuais, para que os trabalhos e a navegação fiquem separados. Ela descobre que uma escola usa uma única conta compartilhada para todos os alunos, o que deixa arquivos e históricos de navegação visíveis para todos. Recomenda contas individuais com limpeza automática dos arquivos temporários ao sair. Explica ao técnico da escola que as configurações do sistema operacional são a primeira linha de privacidade nos dispositivos compartilhados, antes que qualquer aplicativo seja aberto.

### 11.2 Permissões e pastas compartilhadas

Os professores salvam documentos em pastas de rede. Elena confere as permissões e encontra uma pasta de anotações de proteção das crianças que todos os funcionários conseguem ler. Ela trabalha com o técnico para restringi-la aos responsáveis pela proteção. Também ativa a auditoria da pasta, para que os acessos possam ser revisados. O episódio mostra que informações sensíveis muitas vezes ficam em pastas comuns, e não em sistemas protegidos, e que as permissões se desviam ao longo dos anos à medida que os funcionários mudam de função sem que ninguém revise quem ainda abre quais pastas. As revisões corrigem isso.

### 11.3 Logs

Os sistemas operacionais registram os logins e os acessos a arquivos. Elena explica que os logs ajudam a investigar incidentes, mas também contêm dados pessoais de funcionários e alunos. Ela recomenda guardar os logs pelo tempo necessário às investigações, como seis meses, restringir o acesso à equipe de segurança de TI e informar os funcionários, na política de uso aceitável, de que a atividade é registrada. A transparência, observa, é exigida pelos artigos 13 e 14 do GDPR tanto para os funcionários quanto para os alunos, e os funcionários têm o direito de saber o que é registrado sobre eles. Eles podem pedir acesso a esses registros.

### 11.4 Descarte

Notebooks e tablets antigos são vendidos ou reciclados. Elena descobre que os dispositivos são apagados com a exclusão das contas de usuário, o que pode deixar dados recuperáveis. Ela recomenda usar as funções nativas de apagamento seguro ou a criptografia de disco completo com destruição da chave, e manter um registro de descarte para cada dispositivo. Aprende que o descarte faz parte do ciclo de vida dos dados e que muitas violações no setor envolveram dispositivos vendidos sem o apagamento adequado, uma forma evitável e constrangedora de perder dados de crianças. Os certificados comprovam o apagamento.

### Exemplo resolvido

Elena substitui uma conta compartilhada de alunos por contas individuais, restringe e audita uma pasta de proteção das crianças, define a retenção dos logs com transparência para os funcionários e introduz o apagamento seguro e os registros de descarte.

> **Caso sintético.** Os dispositivos e as pastas são sintéticos; os artigos 13 e 14 do GDPR são reais.

### Erros e limites

Os métodos de apagamento seguro variam de dispositivo para dispositivo; verifique se o método funciona em cada modelo.

### Exercícios

- **EX031 — Risco da conta compartilhada.** O que há de errado com uma única conta compartilhada de alunos? *Rubrica:* 3 = arquivos e históricos ficam visíveis para todos os alunos;; 2 = menciona compartilhamento;; 1 = está tudo bem;; 0 = nenhuma.
- **EX032 — Pasta de proteção.** Como a pasta de proteção das crianças foi corrigida? *Rubrica:* 3 = acesso restrito aos responsáveis pela proteção, com auditoria;; 2 = uma parte;; 1 = nada;; 0 = nenhuma.
- **EX033 — Descarte de dispositivos.** Por que excluir as contas de usuário não basta antes de vender um notebook? *Rubrica:* 3 = os dados podem continuar recuperáveis no disco;; 2 = menciona recuperação;; 1 = basta;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) estimar uma proporção a partir de uma pesquisa, com sua incerteza; (2) comparar grupos com cuidado; (3) relatar resultados de pesquisa sem identificar os respondentes.

### 12.1 A pesquisa com as famílias

A rede faz uma pesquisa com as famílias sobre a consciência de privacidade. Uma pergunta indaga se os pais sabem quais aplicativos recebem os dados de seu filho. Elena analisa os resultados sintéticos. Nas doze escolas, 131 de 520 respondentes dizem que sim, 25%. Ela calcula um intervalo de Wilson de 95%, que se comporta bem com proporções próximas de zero ou de um e com amostras pequenas, e obtém de 22% a 29%. Ela relata o intervalo porque um único percentual esconde o quanto a estimativa é incerta, sobretudo para cada escola isolada. O intervalo de Wilson funciona bem com proporções perto de zero ou amostras pequenas.

### 12.2 Comparação entre escolas

Elena compara duas escolas. Na Ashby Primary, 9 de 40 pais dizem que sim, 22%, com intervalo de 12% a 38%. Na Kelso Primary, 22 de 48 dizem que sim, 46%, com intervalo de 33% a 60%. Os intervalos quase não se sobrepõem, o que sugere uma diferença real. Ela investiga e descobre que a Kelso envia às famílias uma carta anual listando os aplicativos. Ela adverte que a pesquisa não consegue provar que a carta causou a diferença, mas o padrão justifica testar a carta em outras escolas. Outras diferenças entre as escolas também poderiam explicar a distância. Só um experimento mostraria a causalidade.

### 12.3 Viés de resposta

Nem todos os pais respondem. Elena observa que os pais interessados em privacidade podem ter mais propensão a responder, o que faria a consciência parecer maior do que é. Ela relata a taxa de resposta de cada escola e recomenda cautela na interpretação das escolas com poucas respostas. Explica que as estatísticas sobre pessoas dependem de quem é contado, e que um analista cuidadoso sempre pergunta quem está faltando nos dados antes de tirar conclusões sobre todos. Os pais que respondem às pesquisas podem ser diferentes dos que não respondem, e isso precisa constar do relatório.

### 12.4 Proteção dos respondentes

A pesquisa inclui um campo de comentário livre. Alguns comentários mencionam nomes e condições de crianças. Elena remove os detalhes identificadores antes de compartilhar os comentários com a direção da rede e só relata números por escola quando pelo menos vinte pais responderam. Ela explica que uma pesquisa sobre privacidade precisa, ela própria, proteger a privacidade, e que os grupos pequenos e o texto livre são as formas mais comuns de os relatórios de pesquisa identificarem pessoas por acidente. Ela suprime resultados de grupos com menos de dez pessoas e retira respostas livres que citam nomes ou turmas de crianças.

### Laboratório — Consciência das famílias com intervalos de Wilson

```python
# Wilson 95% intervals for a synthetic parent survey: "I know which apps receive my child's data".
import math
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h
for school, k, n in [("Ashby Primary", 9, 40), ("Kelso Primary", 22, 48), ("all 12 schools", 131, 520)]:
    lo, hi = wilson(k, n); print(f"{school:15s} {k}/{n} = {k/n:.0%}  95% CI {lo:.0%}-{hi:.0%}")
```

Execute com `python3 lab_wilson.py`. Saída verificada:

```text
Ashby Primary   9/40 = 22%  95% CI 12%-38%
Kelso Primary   22/48 = 46%  95% CI 33%-60%
all 12 schools  131/520 = 25%  95% CI 22%-29%
```

### Exemplo resolvido

Elena estima a consciência em toda a rede em 25% (intervalo de 95% de 22% a 29%), encontra 22% na Ashby contra 46% na Kelso, com intervalos que quase não se sobrepõem, aponta o viés de resposta e remove os detalhes identificadores dos comentários.

> **Caso sintético.** Os dados da pesquisa são sintéticos.

### Erros e limites

Intervalos que quase não se sobrepõem são sugestivos, não um teste formal; um teste de diferença seria mais preciso.

### Exercícios

- **EX034 — Intervalo da rede.** Qual é o intervalo de 95% para a consciência em toda a rede? *Rubrica:* 3 = de 22% a 29%;; 2 = aproximadamente certo;; 1 = errado;; 0 = nenhuma.
- **EX035 — Diferença da Kelso.** O que pode explicar a consciência maior na Kelso? *Rubrica:* 3 = uma carta anual listando os aplicativos, embora a causalidade não esteja provada;; 2 = menciona a carta;; 1 = nada;; 0 = nenhuma.
- **EX036 — Proteção dos respondentes.** Como Elena protege os respondentes da pesquisa? *Rubrica:* 3 = remove identificadores do texto livre e só relata escolas com pelo menos vinte respostas;; 2 = uma parte;; 1 = nada;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Identidade e acesso

### Objetivos de aprendizagem

Você vai (1) projetar o acesso baseado em funções nos sistemas escolares; (2) gerir entradas, mudanças e saídas de pessoas; (3) revisar os acessos com regularidade.

### 13.1 Funções

Elena projeta funções para o sistema de gestão escolar da rede: professor de turma, coordenador de ano, coordenadora de necessidades especiais, auxiliar administrativo, responsável pela proteção das crianças e diretor. Cada função tem um acesso definido. Ela documenta a finalidade de cada permissão. Por exemplo, os auxiliares administrativos precisam dos dados de contato para enviar cartas, mas não dos resultados das avaliações. O desenho das funções transforma o princípio do privilégio mínimo em algo que funcionários e auditores conseguem entender e conferir. A função administrativa, por exemplo, pode atualizar contatos, mas não vê os níveis de leitura.

### 13.2 Entradas, mudanças e saídas

Os funcionários mudam de função com frequência. Elena descobre que uma antiga coordenadora de necessidades especiais, agora professora de turma, ainda tem acesso a todos os planos de apoio. Outro professor, que deixou a rede seis meses antes, ainda tem uma conta ativa. Ela propõe um processo ligado ao sistema de recursos humanos: quando alguém entra, muda de função ou sai, seu acesso muda automaticamente, com um gestor confirmando a nova função. Ela observa que o acesso remanescente é uma das falhas de controle de acesso mais comuns em organizações de todos os tamanhos.

### 13.3 Revisões de acesso

Elena institui revisões de acesso a cada período letivo. Cada diretor recebe uma lista dos funcionários e de suas funções e a confirma ou corrige. Na primeira revisão, onze das 340 contas precisam de mudanças. Ela registra os resultados e repete a revisão no período seguinte, quando só três mudanças são necessárias. As revisões regulares, explica, pegam erros que os processos automáticos deixam passar e fornecem evidências de responsabilização pelo artigo 5(2) do GDPR. Cada diretor confirma a lista de sua escola a cada período. As correções são registradas com datas e motivos.

### 13.4 Autenticação

Elena recomenda autenticação multifator para os funcionários que acessam registros de alunos de fora da escola. Também recomenda que os alunos usem logins simples, mas individuais, adequados à idade. Os alunos muito pequenos podem usar senhas com figuras nos dispositivos da sala, enquanto os mais velhos usam senhas. Ela explica que a autenticação precisa servir às pessoas que a usam, e que uma segurança que as crianças pequenas não conseguem manejar será contornada por professores bem-intencionados que compartilham os próprios logins. Os alunos menores usam senhas com figuras nos tablets compartilhados, e os professores não precisam mais compartilhar seus logins.

### Exemplo resolvido

Elena define seis funções com finalidades documentadas, liga as mudanças de acesso ao RH, faz revisões a cada período (de onze mudanças para três) e adapta a autenticação aos funcionários e à idade dos alunos.

> **Caso sintético.** As contas e as funções são sintéticas; o artigo 5(2) do GDPR é real.

### Erros e limites

A integração com o RH falha se os registros do RH atrasarem; as revisões continuam necessárias.

### Exercícios

- **EX037 — Casos de acesso remanescente.** Cite os dois casos de acesso remanescente que Elena encontrou. *Rubrica:* 3 = a antiga coordenadora de necessidades especiais com os planos de apoio; o professor que saiu com conta ativa;; 2 = um;; 1 = nenhum;; 0 = nenhuma.
- **EX038 — Resultado das revisões.** Quantas contas precisaram de mudanças na primeira e na segunda revisão? *Rubrica:* 3 = onze, depois três;; 2 = um número;; 1 = errado;; 0 = nenhuma.
- **EX039 — Login adequado à idade.** Por que usar senhas com figuras para os alunos muito pequenos? *Rubrica:* 3 = uma segurança que eles não conseguem manejar será contornada;; 2 = menciona usabilidade;; 1 = nenhum;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos da privacidade

### Objetivos de aprendizagem

Você vai (1) explicar teorias da privacidade; (2) aplicar os princípios de proteção de dados; (3) identificar as bases legais do tratamento escolar.

### 14.1 Teorias

Elena estuda a teoria da privacidade. Warren e Brandeis (1890) defenderam o direito de ser deixado em paz. Solove (2006) descreve a privacidade como uma família de problemas, como a vigilância, a agregação e a divulgação. A integridade contextual de Nissenbaum sustenta que os fluxos de informação devem respeitar as normas do contexto em que surgem. Elena aplica a integridade contextual às escolas: a informação que os pais compartilham com uma professora sobre uma situação familiar não deve fluir para outros pais nem para fornecedores de aplicativos, mesmo que isso seja tecnicamente possível. As normas acompanham a informação.

### 14.2 Princípios

Ela estuda os princípios do artigo 5 do GDPR e encontra equivalentes no art. 6º da LGPD, que lista princípios como finalidade, adequação, necessidade, transparência, segurança e prevenção. Ela relaciona cada princípio a um exemplo escolar: a limitação da finalidade significa que os dados de frequência coletados para a proteção das crianças não devem ser usados para ranquear professores; a minimização significa que um aplicativo de merenda não precisa dos níveis de leitura. Os exemplos tornam concretos, para o treinamento da equipe, princípios que pareciam abstratos. Cada exemplo vem da prática da rede.

### 14.3 Bases legais

Elena aprende que o tratamento precisa de uma base legal pelo artigo 6 do GDPR; na LGPD, as hipóteses estão no art. 7º. As escolas costumam se apoiar na obrigação legal para os registros exigidos pela legislação educacional, na missão de interesse público para o ensino e no consentimento para atividades opcionais, como fotografias em boletins. Ela explica que o consentimento nem sempre é a base certa: se a escola precisa dos dados para ensinar, pedir consentimento sugere que os pais poderiam recusar sem consequências, o que pode não ser verdade. Escolher a base correta torna o tratamento mais honesto. A missão de interesse público cobre a maior parte dos dados dos alunos.

### 14.4 Categorias especiais

Dados de saúde, convicções religiosas e origem étnica são categorias especiais pelo artigo 9; a LGPD os chama de dados sensíveis e trata deles no art. 11. As escolas os tratam para cuidados médicos, necessidades alimentares e monitoramento da igualdade. Cada tratamento precisa de uma condição do artigo 9, além de uma base do artigo 6. Elena monta uma tabela do tratamento de categorias especiais da rede com as duas bases. Descobre que os dados de monitoramento da igualdade são guardados com os nomes, quando uma análise agregada bastaria, e recomenda separá-los. A separação reduz a exposição sem reduzir a utilidade dos relatórios. O responsável concorda.

### Exemplo resolvido

Elena aplica a integridade contextual às informações familiares, relaciona os princípios do GDPR e da LGPD a exemplos escolares, explica por que o consentimento nem sempre é a base certa e descobre dados de igualdade guardados com os nomes.

> **Caso sintético.** O tratamento da rede é sintético; Warren e Brandeis (1890), Solove (2006), Nissenbaum (2004), os artigos 5, 6 e 9 do GDPR e os arts. 6º, 7º e 11 da LGPD são reais.

### Erros e limites

A escolha da base legal depende da legislação educacional de cada país; confira localmente.

### Exercícios

- **EX040 — Fluxo contextual.** Como a integridade contextual se aplica às informações familiares compartilhadas com uma professora? *Rubrica:* 3 = não devem fluir para outros pais nem para fornecedores;; 2 = menciona normas;; 1 = podem circular livremente;; 0 = nenhuma.
- **EX041 — Uso indevido do consentimento.** Por que o consentimento é a base errada para dados necessários ao ensino? *Rubrica:* 3 = os pais não podem de fato recusar sem consequências;; 2 = menciona escolha;; 1 = sempre consentimento;; 0 = nenhuma.
- **EX042 — Dados de igualdade.** O que Elena descobriu sobre os dados de monitoramento da igualdade? *Rubrica:* 3 = eram guardados com os nomes quando uma análise agregada bastaria;; 2 = menciona nomes;; 1 = nada;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) medir o desempenho no atendimento aos pedidos de direitos; (2) identificar as causas dos atrasos; (3) definir metas e monitoramento.

### 15.1 Pedidos de acesso das famílias

Os pais podem pedir acesso aos dados do filho, e as próprias crianças podem fazer pedidos quando tiverem maturidade suficiente. Elena reúne dados sintéticos de vinte pedidos do último ano. O tempo mediano de resposta é de 26 dias e a média, de 26,8. Seis dos vinte, 30%, levaram mais de trinta dias, o limite aproximado de um mês do artigo 12(3) do GDPR; no Brasil, o art. 19, II, da LGPD fixa quinze dias para a declaração completa. O mais longo levou 61 dias. Os números dão à rede seu primeiro retrato factual de como trata os pedidos. A maioria foi respondida no prazo, mas os atrasos se concentraram perto das férias.

### 15.2 Causas

Elena examina os pedidos atrasados. Todos os quatro pedidos recebidos logo antes das férias escolares atrasaram, porque a equipe estava ausente. Ela também descobre que os pedidos iam para cada escola, e não para um ponto central, então o tratamento variava. Explica que o prazo do GDPR continua correndo nas férias, embora o artigo 12(3) permita prorrogá-lo por dois meses em caso de pedidos complexos ou numerosos, desde que o solicitante seja informado no primeiro mês. As férias, sozinhas, não justificam a prorrogação. A maioria dos atrasos veio das férias escolares, e o planejamento resolve isso.

### 15.3 Metas e processo

Elena propõe uma caixa central de pedidos gerida pelo responsável pela proteção de dados, uma escala de cobertura nas férias e a meta de responder a todos os pedidos em até vinte e cinco dias, para deixar margem. Também propõe um modelo de carta para as prorrogações realmente necessárias. As Diretrizes 01/2022 do EDPB sobre o direito de acesso a ajudam a desenhar a verificação de identidade e o conteúdo das respostas. Ela apresenta o plano à direção da rede com a linha de base medida. O plano fixa uma meta interna de vinte dias. Cada pedido é registrado centralmente desde o primeiro dia.

### 15.4 Monitoramento

Elena monta um relatório mensal simples: pedidos recebidos, pedidos em aberto, tempo mediano e pedidos atrasados. Explica que medir com regularidade transforma uma revisão pontual em um ciclo de retorno. O Dr. Asante observa que números pequenos deixam os percentuais instáveis, então ela relata as contagens junto com os percentuais. Seis meses depois, com o novo processo em funcionamento, nenhum pedido atrasa. Ela relata a melhoria com a ressalva de que a amostra é pequena. Com tão poucos pedidos, um único atraso muda bastante o percentual. Por isso as contagens também aparecem no relatório.

### Laboratório — Tempos de resposta aos pedidos de acesso das famílias

```python
# Subject access requests from parents over one year: days to respond, one-month (30-day) target.
import statistics
days = [12, 25, 31, 8, 44, 19, 27, 30, 52, 15, 22, 35, 9, 28, 61, 17, 24, 29, 33, 14]
print(f"requests {len(days)}; median {statistics.median(days)} days; mean {statistics.mean(days):.1f}")
late = [d for d in days if d > 30]
print(f"late (>30 days): {len(late)} of {len(days)} ({len(late)/len(days):.0%}); longest {max(days)} days")
print("holiday-period requests late:", sum(1 for d in [44, 52, 61, 35] if d > 30), "of 4")
```

Execute com `python3 lab_sar.py`. Saída verificada:

```text
requests 20; median 26.0 days; mean 26.8
late (>30 days): 6 of 20 (30%); longest 61 days
holiday-period requests late: 4 of 4
```

### Exemplo resolvido

Elena mede uma mediana de 26 dias, com 6 de 20 pedidos atrasados (todos os quatro do período de férias), centraliza o atendimento com cobertura nas férias e passa a monitorar mensalmente.

> **Caso sintético.** Os pedidos são sintéticos; o artigo 12(3) do GDPR, o art. 19 da LGPD e as Diretrizes 01/2022 do EDPB são reais.

### Erros e limites

Vinte pedidos são poucos; um único atraso muda muito o percentual.

### Exercícios

- **EX043 — Parcela atrasada.** Que parcela dos pedidos atrasou? *Rubrica:* 3 = 6 de 20, 30%;; 2 = cerca de um terço;; 1 = errado;; 0 = nenhuma.
- **EX044 — Prorrogação nas férias.** As férias escolares justificam prorrogar o prazo? *Rubrica:* 3 = não; a prorrogação é para complexidade ou volume, com aviso;; 2 = não;; 1 = sim;; 0 = nenhuma.
- **EX045 — Contagens com percentuais.** Por que relatar contagens junto com os percentuais? *Rubrica:* 3 = números pequenos deixam os percentuais instáveis;; 2 = menciona tamanho;; 1 = desnecessário;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) projetar uma arquitetura segura para uma rede de várias escolas; (2) separar os dados sensíveis; (3) planejar backup e recuperação.

### 16.1 A arquitetura da rede

Elena projeta uma arquitetura para a rede. Um sistema central de gestão escolar atende às doze escolas. Os funcionários de cada escola veem apenas os próprios alunos. Os registros de proteção das crianças ficam em um sistema separado e mais restrito. Os aplicativos de sala de aula se conectam por login único (single sign-on), o que permite à rede controlar o acesso de forma central e removê-lo rapidamente. Ela desenha o projeto com zonas e explica por que os registros sensíveis ficam separados dos sistemas do dia a dia usados por muitos funcionários. Os registros de proteção ficam em uma zona própria, com acesso separado. As zonas são documentadas.

### 16.2 Separação

A separação limita o dano. Se a conta de um professor for comprometida, o atacante alcança os registros de aprendizagem, mas não as anotações de proteção das crianças. Elena também separa os dados dos alunos dos dados dos funcionários, já que funções diferentes precisam de cada um. Ela explica que o GDPR exige, no artigo 32, segurança adequada ao risco, e que a LGPD traz dever semelhante no art. 46; a separação é uma medida de bom custo-benefício para uma rede com pouca equipe de segurança, porque reduz o quanto qualquer falha isolada consegue expor. Um notebook de sala comprometido não alcança diretamente os registros de proteção.

### 16.3 Backup e recuperação

Escolas já sofreram ataques de ransomware. Elena projeta backups cifrados, guardados separadamente e testados. Ela define objetivos de recuperação: o sistema de gestão restabelecido em até um dia e os registros de proteção das crianças em até quatro horas, já que os responsáveis pela proteção podem precisar deles com urgência. Planeja um teste de restauração a cada período letivo. Observa que os backups também guardam dados pessoais e precisam seguir as regras de retenção, então os backups antigos expiram. No primeiro teste, os registros de frequência de um período são recuperados em menos de uma hora, e a cópia restaurada é apagada em seguida, para que não sobre duplicata.

### 16.4 Arquitetura dos fornecedores

Muitas funções são fornecidas por terceiros. Elena inclui os fornecedores no diagrama de arquitetura, com seus fluxos de dados e contratos. Ela observa que o login único permite à rede desativar rapidamente o acesso a todos os aplicativos quando um aluno sai. Também estabelece a regra de que novos aplicativos precisam se conectar pelo login único e passar pela triagem. A arquitetura, explica, inclui regras sobre como novos componentes entram, e não só os componentes atuais. Cada aplicativo só entra depois da triagem e aparece no diagrama de arquitetura, com seu responsável e seu contrato.

### Exemplo resolvido

Elena projeta um sistema central com acesso por escola, um sistema separado para a proteção das crianças, login único para os aplicativos, backups cifrados e testados e uma regra de entrada para novos aplicativos.

> **Caso sintético.** A arquitetura é sintética; o artigo 32 do GDPR e o art. 46 da LGPD são reais.

### Erros e limites

Sistemas centrais concentram o risco; proteja-os e monitore-os de perto.

### Exercícios

- **EX046 — Separação da proteção.** Por que manter os registros de proteção das crianças em um sistema separado? *Rubrica:* 3 = uma conta de professor comprometida não os alcança;; 2 = menciona sensibilidade;; 1 = mesmo sistema;; 0 = nenhuma.
- **EX047 — Benefício do login único.** O que o login único dá à rede? *Rubrica:* 3 = controle central e remoção rápida do acesso a todos os aplicativos;; 2 = menciona controle;; 1 = nada;; 0 = nenhuma.
- **EX048 — Retenção dos backups.** Por que os backups precisam seguir as regras de retenção? *Rubrica:* 3 = os backups também guardam dados pessoais;; 2 = menciona dados;; 1 = estão isentos;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Conceitos de criptografia

### Objetivos de aprendizagem

Você vai (1) explicar a criptografia em repouso e em trânsito; (2) entender o hash e a pseudonimização; (3) gerir as chaves de forma adequada.

### 17.1 Criptografia

Elena aprende a diferença entre a criptografia em trânsito, que protege os dados que circulam pelas redes, e a criptografia em repouso, que protege os dados armazenados. As duas protegem os registros das crianças contra ameaças diferentes. Ela verifica se os sistemas da rede usam as duas e descobre que os relatórios exportados e salvos em pen drives não são cifrados. Recomenda pen drives cifrados ou, melhor ainda, acabar com as exportações para mídias removíveis e usar um compartilhamento seguro. A auditoria mostra que esses pen drives servem sobretudo para levar relatórios para casa e corrigir.

### 17.2 Hash e pseudônimos

O hash transforma dados em um valor de tamanho fixo que não pode ser revertido com facilidade. Elena explica que aplicar o hash apenas ao identificador de um aluno é fraco, porque o conjunto de identificadores é pequeno e um atacante pode calcular o hash de todos. Um hash com chave secreta é mais forte. Ela usa hashes com chave na análise de leitura do Capítulo 8. Ela ressalta que a pseudonimização reduz o risco, mas os dados continuam pessoais pelo artigo 4(5) do GDPR. As chaves ficam com o responsável pela proteção de dados, que as troca uma vez por ano.

### 17.3 Chaves

A criptografia depende das chaves. Elena pergunta quem guarda as chaves dos backups da rede. A resposta é um único técnico de TI. Se ele sair ou perder a chave, os backups ficam inutilizáveis. Ela recomenda guardar as chaves em um serviço gerenciado de chaves, com dois custodiantes autorizados e recuperação documentada. Explica que a gestão de chaves costuma ser a parte mais difícil da criptografia na prática, e que as organizações pequenas precisam de arranjos simples e bem documentados. A rede mantém um registro de chaves de duas páginas, com os detentores e os locais de cada chave.

### 17.4 Limites

Elena observa que a criptografia não protege contra usuários autorizados que fazem mau uso dos dados nem contra a coleta desnecessária. Um professor com acesso legítimo ainda pode compartilhar um relatório de forma indevida. A criptografia é uma medida entre muitas. Ela escreve em suas anotações que a criptografia protege a confidencialidade contra pessoas de fora, enquanto o controle de acesso, o treinamento e a minimização tratam das pessoas de dentro e da coleta excessiva. Um professor com acesso legítimo ainda pode usar mal relatórios decifrados, então só a criptografia não teria evitado o e-mail enviado ao destinatário errado que ela estudou no início do curso.

### Exemplo resolvido

Elena acaba com as exportações sem criptografia em pen drives, usa hashes com chave para os pseudônimos, leva as chaves dos backups para um serviço gerenciado com dois custodiantes e enuncia os limites da criptografia.

> **Caso sintético.** Os sistemas são sintéticos; o artigo 4(5) do GDPR é real.

### Erros e limites

Dados cifrados continuam sendo dados pessoais; a criptografia reduz o risco, não as obrigações.

### Exercícios

- **EX049 — Exportações em pen drive.** O que Elena recomendou para as exportações em pen drives? *Rubrica:* 3 = pen drives cifrados ou substituição por compartilhamento seguro;; 2 = uma opção;; 1 = nada;; 0 = nenhuma.
- **EX050 — Um único detentor da chave.** Qual era o risco de um só técnico guardar as chaves dos backups? *Rubrica:* 3 = os backups ficariam inutilizáveis se ele saísse ou perdesse a chave;; 2 = menciona perda;; 1 = nenhum;; 0 = nenhuma.
- **EX051 — Limites da criptografia.** Contra o que a criptografia não protege? *Rubrica:* 3 = mau uso por usuários autorizados e coleta excessiva;; 2 = um;; 1 = protege contra tudo;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Métodos de pesquisa I

### Objetivos de aprendizagem

Você vai (1) formular uma questão de pesquisa sobre a prática de privacidade; (2) escolher métodos adequados às escolas; (3) planejar uma pesquisa ética que envolva dados de crianças.

### 18.1 A questão

A disciplina de métodos de pesquisa pede que Elena planeje um estudo pequeno. Ela pergunta: por que os professores adotam aplicativos de sala de aula sem verificar suas práticas de dados? A questão importa porque os aplicativos não verificados criam a maior parte dos riscos de compartilhamento da rede encontrados no Capítulo 9. Ela a formula como questão exploratória, adequada a entrevistas, e não como hipótese a testar, porque pouco se sabe sobre o raciocínio dos professores nesse contexto. Ela espera motivos variados e quer ouvi-los nas palavras dos próprios professores.

### 18.2 Métodos

Elena planeja entrevistas semiestruturadas com dez professores de quatro escolas. Escreve um roteiro de entrevista com perguntas abertas sobre como eles encontram os aplicativos, o que verificam e do que precisariam para verificar mais. Planeja analisar as transcrições de forma temática, codificando os motivos recorrentes. Também planeja comparar os temas das entrevistas com o registro de aplicativos, para ver se as práticas declaradas correspondem ao compartilhamento real. As entrevistas duram cerca de trinta minutos e usam as mesmas perguntas centrais para todos. As respostas são comparadas com o registro.

### 18.3 Ética

O estudo de Elena envolve adultos, não crianças, mas as conversas podem mencionar alunos. Ela planeja pedir aos participantes que não citem crianças pelo nome, apagar qualquer nome que apareça nas transcrições e guardar as gravações com segurança, apagando-as depois da transcrição. Obtém a aprovação ética do Fairhaven e a autorização da rede. Os participantes dão consentimento informado e podem desistir. Ela observa que uma pesquisa sobre privacidade precisa ser um modelo de boa prática de privacidade. As gravações são apagadas depois da transcrição, e os nomes citados são retirados dos textos.

### 18.4 Limites

Elena registra os limites: dez professores não representam todos os professores; os participantes podem se apresentar de forma favorável; e seu papel no estágio pode influenciar o que eles dizem. Ela planeja declarar esses limites no relatório e pedir a uma colega que não participa do estágio que conduza duas entrevistas, como verificação. O Dr. Asante lembra que reconhecer os limites faz parte da boa pesquisa, e não é uma fraqueza. Seu papel no estágio poderia deixar os professores menos francos. A colega conduz duas entrevistas para verificar esse efeito.

### Exemplo resolvido

Elena formula uma questão exploratória sobre a adoção de aplicativos pelos professores, planeja dez entrevistas com análise temática, define salvaguardas éticas contra a identificação de crianças e lista os limites.

> **Caso sintético.** O plano de estudo é sintético.

### Erros e limites

As entrevistas captam o comportamento relatado; compare-o com os registros sempre que possível.

### Exercícios

- **EX052 — Formulação exploratória.** Por que formular a questão como exploratória? *Rubrica:* 3 = pouco se sabe sobre o raciocínio dos professores, então as entrevistas são adequadas;; 2 = menciona novidade;; 1 = hipótese;; 0 = nenhuma.
- **EX053 — Crianças nas transcrições.** Como Elena trata as menções a crianças nas entrevistas? *Rubrica:* 3 = pede que não as citem pelo nome e apaga os nomes das transcrições;; 2 = uma parte;; 1 = mantém;; 0 = nenhuma.
- **EX054 — Influência do estágio.** Por que o papel de Elena no estágio pode afetar as respostas? *Rubrica:* 3 = os professores podem dizer o que acham que a rede quer ouvir;; 2 = menciona viés;; 1 = nenhum efeito;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Privacidade e proteção de dados: escopo e teoria

### Objetivos de aprendizagem

Você vai (1) definir o alcance da legislação de proteção de dados; (2) relacionar a teoria aos conceitos jurídicos; (3) entender onde a lei termina e a ética continua.

### 19.1 Alcance da lei

Elena estuda o alcance do GDPR. Ele se aplica ao tratamento de dados pessoais por meios automatizados ou em sistemas de arquivo, com exceções como as atividades puramente domésticas. Dado pessoal significa qualquer informação relativa a uma pessoa natural identificada ou identificável. A LGPD tem uma definição semelhante, no art. 5º, I, e também exclui o tratamento para fins exclusivamente particulares (art. 4º, I). Elena observa que os dados dos alunos claramente entram no alcance da lei, assim como as fotografias e as gravações de voz em que as crianças podem ser reconhecidas. O artigo 4(1) define dados pessoais de forma ampla, incluindo os identificadores indiretos.

### 19.2 Identificabilidade

O considerando 26 explica que a identificabilidade depende dos meios razoavelmente suscetíveis de serem usados. Elena aplica isso a uma tabela publicada de resultados de exames de uma escola pequena. Se a tabela mostrar que um aluno com merenda gratuita obteve determinada nota, os leitores podem identificar a criança. Os dados são, portanto, pessoais, mesmo sem nenhum nome. Ela liga isso ao exercício de contagem do Capítulo 6 e à pesquisa de Sweeney. O considerando 26 define o teste: pergunta que meios são razoavelmente suscetíveis de serem usados para identificar alguém.

### 19.3 Teoria e lei

Elena compara os conceitos jurídicos com a teoria da privacidade. A limitação da finalidade da lei se parece com a preocupação da integridade contextual com fluxos que correspondam aos contextos. Os danos de Solove, como a exclusão e o uso secundário, correspondem aos direitos de acesso e à limitação da finalidade. Ela observa que a teoria muitas vezes explica por que uma regra jurídica existe, o que ajuda os funcionários a entendê-la e segui-la, em vez de vê-la como arbitrária. A integridade contextual, por exemplo, explica por que dados compartilhados com uma professora não devem chegar a anunciantes de aplicativos.

### 19.4 Além da lei

Algumas práticas podem ser lícitas e, ainda assim, prejudiciais. Uma escola pode compartilhar licitamente fotografias da turma com os pais, mas uma foto que mostre uma criança num momento de angústia pode causar dano. Elena escreve que a rede deve considerar a dignidade e os sentimentos das crianças, e não só as permissões legais. O Dr. Asante concorda e observa que a ética continua onde a lei silencia, especialmente para crianças que não conseguem falar por si com facilidade. Ela acrescenta uma pergunta ética à triagem: isto é justo com a criança? Ela a faz todas as vezes.

### Exemplo resolvido

Elena define o alcance do GDPR, mostra como a tabela de resultados de uma escola pequena pode identificar um aluno, relaciona a teoria às regras jurídicas e acrescenta a dignidade como consideração além da lei.

> **Caso sintético.** Os exemplos são sintéticos; o considerando 26 do GDPR, a LGPD, Solove (2006), Nissenbaum (2004) e Sweeney (2002) são reais.

### Erros e limites

A identificabilidade depende do contexto; a mesma tabela pode ser segura para uma escola grande.

### Exercícios

- **EX055 — Definição de dado pessoal.** O que significa dado pessoal pelo GDPR? *Rubrica:* 3 = informação relativa a uma pessoa natural identificada ou identificável;; 2 = aproximada;; 1 = errada;; 0 = nenhuma.
- **EX056 — Tabela sem nomes.** Como uma tabela de resultados sem nomes pode conter dados pessoais? *Rubrica:* 3 = células pequenas permitem identificar uma criança;; 2 = menciona números pequenos;; 1 = nunca;; 0 = nenhuma.
- **EX057 — Lícito, mas prejudicial.** Dê um exemplo, tirado do capítulo, de tratamento lícito, mas prejudicial. *Rubrica:* 3 = compartilhar uma foto que mostra uma criança em angústia;; 2 = um exemplo;; 1 = nenhum;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Privacidade e proteção de dados: casos fundamentais

### Objetivos de aprendizagem

Você vai (1) aprender com casos de pesquisa em privacidade publicados; (2) identificar a lição de cada caso; (3) aplicar as lições às escolas.

### 20.1 Reidentificação

Elena estuda a demonstração de Sweeney (2002) de que alguns poucos atributos, como código postal, data de nascimento e sexo, podiam reidentificar pessoas em registros de saúde supostamente anônimos. A lição é que remover os nomes não torna os dados anônimos. Para a rede, isso significa que entregar a pesquisadores dados por aluno sem nomes, mas com data de nascimento e escola, ainda poderia identificar crianças, e esses dados precisam ser tratados como pessoais, com as salvaguardas adequadas. Em escolas pequenas, a data de nascimento e a escola podem bastar para identificar uma criança.

### 20.2 Dados esparsos

Narayanan e Shmatikov (2008) mostraram que um conjunto de avaliações de filmes podia ser ligado a resenhas públicas a partir de umas poucas avaliações conhecidas. A lição é que dados comportamentais detalhados identificam muito. Elena a aplica aos aplicativos de aprendizagem, que registram atividades detalhadas, como respostas e tempos. Esses dados poderiam revelar crianças individuais mesmo sem nomes, o que reforça sua preocupação com aplicativos que compartilham logs de atividade com terceiros. Os logs dos aplicativos registram cada clique e seu horário, e alguns poucos horários bastam para destacar uma criança.

### 20.3 Comportamento e escolhas

Acquisti, Brandimarte e Loewenstein (2015) revisam evidências de que as escolhas de privacidade das pessoas são incertas, dependentes do contexto e maleáveis. A lição para a rede é que o consentimento dos pais depende muito de como as escolhas são apresentadas. Elena recomenda formulários de consentimento neutros, sem opções pré-marcadas nem pressão, em linha com as diretrizes do EDPB sobre consentimento. Ela observa que a pesquisa sobre comportamento ajuda a desenhar escolhas mais justas. Como as escolhas são moldadas com facilidade pelo desenho e pelo contexto, os formulários da rede passam a apresentá-las de forma neutra.

### 20.4 Aplicação das lições

Elena escreve um guia curto para a rede: nunca tratar dados sem nomes como anônimos sem análise; tratar os dados de atividade de aprendizagem como identificadores; e desenhar as escolhas de consentimento de forma neutra. Cada lição está ligada a um caso publicado. O Dr. Asante observa que fundamentar as orientações em evidências as torna mais persuasivas para diretores ocupados do que alertas genéricos, porque as evidências mostram que os riscos são reais, e não teóricos. Cada slide combina um estudo com um exemplo escolar, para que os diretores vejam por que a pesquisa importa localmente.

### Exemplo resolvido

Elena tira três lições de Sweeney (2002), de Narayanan e Shmatikov (2008) e de Acquisti et al. (2015) e as transforma em um guia para a rede.

> **Caso sintético.** O guia é sintético; as obras citadas e as Diretrizes 05/2020 do EDPB são reais.

### Erros e limites

Lições de outros domínios exigem cuidado quando transferidas para os dados de crianças.

### Exercícios

- **EX058 — Lição de Sweeney.** Que lição o trabalho de Sweeney ensina? *Rubrica:* 3 = remover os nomes não torna os dados anônimos;; 2 = aproximada;; 1 = os nomes bastam;; 0 = nenhuma.
- **EX059 — Logs de atividade.** Por que os logs de atividade dos aplicativos de aprendizagem identificam? *Rubrica:* 3 = dados comportamentais detalhados podem ser ligados a pessoas, como as avaliações esparsas;; 2 = menciona detalhe;; 1 = não identificam;; 0 = nenhuma.
- **EX060 — Consentimento neutro.** Que desenho de consentimento decorre da pesquisa comportamental? *Rubrica:* 3 = formulários neutros, sem caixas pré-marcadas nem pressão;; 2 = menciona desenho;; 1 = pré-marcar;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060 (as de EX061–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Elena Rossi, o Dr. Kwame Asante, o Fairhaven College, a Brindle Valley Schools Trust e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX016.** Uma lista de restrições alimentares pode revelar religião ou condições de saúde.

**EX017.** A secretaria tinha acesso aos planos de apoio de necessidades especiais sem necessidade.

**EX018.** A exposição em qualquer aresta, como um suboperador de análise, expõe os dados daquele caminho.

**EX019.** Registram os sites visitados por alunos identificáveis, incluindo buscas sensíveis.

**EX020.** Retenção mais curta, acesso só para os responsáveis designados pela proteção das crianças e informação clara às famílias.

**EX021.** Os alunos podem deixar de buscar ajuda para problemas sensíveis se se sentirem vigiados.

**EX022.** Ele verifica a função do professor e se o aluno está em suas turmas.

**EX023.** A chave do responsável pela proteção de dados poderia ligar os pseudônimos de volta aos alunos.

**EX024.** Os professores mantinham acesso aos alunos depois das mudanças de turma; agora o acesso é atualizado automaticamente.

**EX025.** ClassChat, ReadAlong e QuizBlitz.

**EX026.** Recebe uma marcação de necessidades educacionais especiais, envia dados para fora do EEE e não tem contrato.

**EX027.** Os aplicativos e o compartilhamento mudam, e um registro consultado com regularidade encontra novas lacunas.

**EX028.** O considerando 38 do GDPR e o art. 14 da LGPD.

**EX029.** O termo de estágio só permite dados sintéticos, então ver registros reais excederia sua autoridade.

**EX030.** A investigação exige autoridade e acesso que só o responsável pode conceder.

**EX031.** Todo aluno consegue ver os arquivos e o histórico de navegação dos outros.

**EX032.** O acesso foi limitado aos responsáveis pela proteção das crianças e a auditoria foi ativada.

**EX033.** Contas excluídas podem deixar dados recuperáveis; é preciso apagamento seguro ou destruição da chave.

**EX034.** De 22% a 29%.

**EX035.** A Kelso envia uma carta anual listando os aplicativos; isso pode explicar a diferença, mas não está provado.

**EX036.** Ela remove os detalhes identificadores dos comentários e só relata números por escola quando vinte ou mais pais responderam.

**EX037.** Uma antiga coordenadora de necessidades especiais com acesso aos planos de apoio e um professor que saiu com a conta ativa.

**EX038.** Onze de 340 na primeira revisão, três na segunda.

**EX039.** Crianças pequenas não conseguem manejar senhas complexas, o que leva ao compartilhamento de logins.

**EX040.** A informação compartilhada em confiança com uma professora deve permanecer naquele contexto.

**EX041.** Porque a recusa não é realmente livre quando os dados são necessários para o ensino.

**EX042.** Eram guardados com os nomes, embora uma análise agregada atendesse à finalidade.

**EX043.** 6 de 20 (30%).

**EX044.** Não. As prorrogações são permitidas para pedidos complexos ou numerosos, com aviso, e não por causa das férias.

**EX045.** Com poucos pedidos, os percentuais oscilam muito, então as contagens dão contexto.

**EX046.** A separação faz com que o comprometimento de contas comuns não exponha as anotações de proteção das crianças.

**EX047.** Controle central do acesso e a capacidade de remover de uma vez o acesso a todos os aplicativos.

**EX048.** Os backups contêm dados pessoais, então precisam expirar como os originais.

**EX049.** Usar pen drives cifrados ou, melhor, acabar com as exportações para mídias removíveis.

**EX050.** Se ele sair ou perdê-la, os backups não poderão ser restaurados.

**EX051.** O mau uso por usuários autorizados e a coleta de mais dados do que o necessário.

**EX052.** Há pouco conhecimento prévio, então a exploração aberta se ajusta melhor do que testar uma hipótese.

**EX053.** Pede-se aos participantes que não citem alunos pelo nome, e qualquer nome é apagado.

**EX054.** Os professores podem se apresentar de forma favorável a alguém ligado à rede.

**EX055.** Qualquer informação relativa a uma pessoa natural identificada ou identificável.

**EX056.** Em escolas pequenas, uma célula que descreve um único aluno pode identificar essa criança.

**EX057.** Compartilhar uma foto lícita da turma que mostra uma criança num momento de angústia.

**EX058.** Remover os nomes deixa os dados identificáveis por meio de outros atributos.

**EX059.** Padrões detalhados de atividade são distintivos, como as avaliações de filmes no estudo de Narayanan e Shmatikov.

**EX060.** Formulários neutros, sem opções pré-marcadas nem pressão.

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
