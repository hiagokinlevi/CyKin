# Privacidade e Proteção de Dados: Curso de Bacharelado

- Idioma: português do Brasil (`pt`); curso 096, curso de bacharelado (4 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 40 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 11–40 (EX031–EX120) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–40: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

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

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX120 estão na edição em inglês até a tradução dos capítulos correspondentes). Elena Rossi, o Dr. Kwame Asante, o Fairhaven College, a Brindle Valley Schools Trust e todos os números são sintéticos. As respostas dos laboratórios citam as saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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
