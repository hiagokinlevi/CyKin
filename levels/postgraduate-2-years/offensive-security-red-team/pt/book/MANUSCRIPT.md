# Segurança Ofensiva Autorizada e Red Team: Um Livro para o Especialista de Pós-Graduação

- Idioma: português do Brasil (`pt`); curso de pós-graduação, dois anos; aproximadamente 600 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 12 já estão escritos em português, com os exercícios EX001–EX020 e suas resoluções com rubricas de 0 a 3; os capítulos 5–12 (EX021–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: especialistas experientes que conduzem escolhas de testes autorizados em escala organizacional.
- Relação com os livros vizinhos: o [livro do bacharelado](../../../../bachelors-4-years/offensive-security-red-team/pt/book/MANUSCRIPT.md) constrói os fundamentos e um projeto final; o [livro do mestrado](../../../../masters-2-years/offensive-security-red-team/pt/book/MANUSCRIPT.md) enfatiza o desenho de pesquisa. **Este livro enfatiza o julgamento do especialista, a leitura de testes guiados por ameaças e a liderança em garantia.**
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação acreditada. **Não concede autorização para testar infraestruturas de mercado reais.** Todas as organizações, pessoas e números são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os capítulos 1–6 cobrem decisões, prática, evidências, ética, desenho de programas e avaliação; os capítulos 7–12 cobrem integração, casos difíceis, liderança, crítica, projeto aplicado e transferência. Cada capítulo traz objetivos, ensino, um exemplo resolvido, um caso sintético rotulado, erros e limites, cinco exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**. Os laboratórios dos capítulos 6, 9 e 10 leem apenas dados locais.

### Caso contínuo sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Meridian Clearing House (MCH)** — serviços de compensação, testes web comuns, exercícios bienais no estilo guiado por ameaças, exclusões adjacentes ao SWIFT | Organização estudada ao longo do livro | Inventada |
| **Amira Hassan** | Especialista que conduz o julgamento sobre testes autorizados na MCH | Inventada |

### Fontes principais

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); MITRE [ATT&CK](https://attack.mitre.org/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

Capítulos 5–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Tomada de decisão avançada em segurança

### Objetivos de aprendizagem

Você vai (1) estruturar decisões sob incerteza para programas de testes autorizados; (2) separar a aceitação de risco do pensamento desejoso; (3) usar registros de decisão que examinadores consigam acompanhar; (4) recusar decisões que não têm responsável.

### 1.1 Objetos de decisão

Na Meridian Clearing House, Amira Hassan trata cada escolha importante de testes como um objeto com cinco campos: opções, evidências, incertezas, recomendação e responsável. "Deveríamos fazer mais red team" não é um objeto de decisão enquanto esses campos não forem escritos, porque os examinadores não conseguem ver o que foi sacrificado. A DEC-14 rejeita trabalho anual guiado por ameaças porque a capacidade do white team não cobre dois ciclos completos sem tomar emprestados analistas do SOC da operação do dia a dia. O CISO aceita esse limite de capacidade por escrito, e Amira arquiva a aceitação ao lado da tabela de opções, para que um examinador futuro veja que a troca foi assumida, e não subentendida.

### 1.2 Tipos de incerteza

Ela distingue a incerteza aleatória (taxas de detecção ruidosas) da incerteza epistêmica (não se sabe se existe um canal de conexão). Intervalos no estilo de Wilson ajudam na primeira; oficinas de arquitetura ajudam na segunda. Misturá-las produz falsa precisão, e é assim que os materiais do conselho ganham uma única porcentagem que finge certeza. Na DEC-14, ela marca o ruído da taxa de detecção como aleatório e o canal desconhecido adjacente ao SWIFT como epistêmico; a oficina de arquitetura seguinte tem data e um líder nomeado. Seus registros de decisão indicam qual incerteza é qual, para que um leitor futuro saiba o que mais dados poderiam resolver e o que só o trabalho de desenho pode resolver.

### 1.3 Aceitação versus adiamento

Aceitar risco residual exige um aceitante nomeado, uma data de expiração e um controle compensatório. Adiar um teste porque "o ano que vem é melhor", sem data, não é aceitação nem gestão — é deriva. A exclusão adjacente ao SWIFT nomeia o CISO como aceitante, expira na próxima revisão do catálogo e lista o isolamento de rede e o MFA no jump host como controles compensatórios. Amira não arquiva uma aceitação se qualquer um desses três campos estiver em branco, e não trata um adiamento sem prazo como substituto deles. Um examinador que lê o registro deve ver uma escolha deliberada, e não uma conversa adiada disfarçada de gestão.

### 1.4 Legibilidade para o examinador

Os registros de decisão respondem: o que foi escolhido, o que foi rejeitado, quais evidências contaram e o que continua desconhecido. Amira rejeita registros que soam como slogans; frases como "levamos a segurança a sério" são apagadas dos rascunhos antes de saírem da mesa dela. Um registro legível da DEC-14 declara que foram escolhidos testes web trimestrais no estilo do WSTG mais um exercício bienal guiado por ameaças, que o exercício anual guiado por ameaças foi rejeitado por capacidade e que os sistemas adjacentes ao SWIFT continuam excluídos. Um diretor que perdeu a reunião consegue reconstruir a troca sem ligar para Amira, e um sucessor consegue continuar o programa sem pedir a ela o folclore.

### 1.5 Autoridade

Somente os papéis listados no estatuto de governança podem aceitar risco residual adjacente a pagamentos: o CISO, para exclusões comuns, e o comitê de riscos do conselho, para escolhas que afetam todo o programa. Amira escala em vez de inventar autoridade, porque a autoridade inventada desmorona diante do questionamento do examinador. Quando um responsável de produto pede que ela aceite o que só o CISO pode aceitar, ele recebe um escalonamento com o trecho do estatuto anexado, e não um aceno discreto. Ela mantém o mesmo trecho ao lado de cada registro de aceitação, para que qualquer pessoa que leia o arquivo depois possa verificar que quem assinou tinha direito de assinar.

### 1.6 Prática

A clínica semanal de decisões pega uma escolha real (sintética), como adiar o exercício guiado por ameaças em um trimestre, e dedica vinte minutos a ela. A sessão termina com opções, evidências e responsável escritos antes de alguém sair da sala. Os juniores apresentam primeiro; Amira edita para dar clareza, e não para suavizar conclusões. Ela lança o registro no log de decisões no mesmo dia, para que a clínica não vire uma conversa de corredor sem documentação. Vinte minutos bastam quando a escolha é concreta, e o hábito de terminar com um registro escrito é o que a clínica realmente treina.

### 1.7 Narrativa

Amira guarda os registros DEC em uma pasta que a auditoria interna amostrou no ano passado sem encontrar adiamentos sem data; a carta da amostragem está fixada acima do monitor dela. Quando um VP pede um sim rápido para ampliar o escopo às redes dos participantes, ela abre um objeto de decisão em branco no projetor e preenche as opções em voz alta até que o VP assuma a responsabilidade ou retire o pedido. O ritual parece lento e evita a inflação silenciosa de escopo entre os participantes da compensação. Três adjuntos já escreveram registros DEC que a auditoria aceitou sem alterações.

### Exemplo resolvido (MCH sintética)

O registro DEC-14 de Amira escolhe testes web trimestrais no estilo do WSTG mais um exercício bienal guiado por ameaças; rejeita o exercício anual guiado por ameaças por razões de capacidade; e lista os sistemas adjacentes ao SWIFT como fora do escopo comum, com o CISO como aceitante dessa exclusão.

> **Caso sintético — Meridian Clearing House (MCH).** A organização de compensação, Amira Hassan e todos os números foram inventados para fins didáticos.

### Erros e limites

Testes guiados por ameaças e de sistemas de compensação exigem autorização jurídica especializada. Este livro só usa casos sintéticos e não traz código de exploração nem roteiro de ataque ao mercado.

### Exercícios

- **EX001 — Campos do objeto de decisão.** Liste cinco campos de um objeto de decisão. *Rubrica:* 3 = cinco entre opções, evidências, incertezas, recomendação, responsável e opções rejeitadas; 2 = três; 1 = um; 0 = nada.
- **EX002 — Aleatória versus epistêmica.** Dê um exemplo de cada uma na MCH. *Rubrica:* 3 = os dois tipos corretos; 2 = um; 1 = trocados; 0 = nada.
- **EX003 — Adiamento ruim.** Por que "testar no ano que vem", sem data, é um problema? *Rubrica:* 3 = deriva / nem aceita nem gerencia; 2 = parcial; 1 = está tudo bem; 0 = nada.
- **EX004 — Autoridade.** Quem pode aceitar risco residual adjacente a pagamentos? *Rubrica:* 3 = papéis do estatuto de governança / nível de CISO; 2 = parcial; 1 = qualquer engenheiro; 0 = nada.
- **EX005 — O que a DEC-14 rejeita.** O que a DEC-14 rejeita e por quê? *Rubrica:* 3 = o exercício anual guiado por ameaças, por capacidade; 2 = parcial; 1 = todos os testes; 0 = nada.

### Síntese

Decisões são objetos com responsável e com as incertezas nomeadas; slogans e adiamentos sem data não contam.

### Continue estudando — capítulo 01 de 12

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Prática atual em segurança ofensiva autorizada

### Objetivos de aprendizagem

Você vai (1) mapear os referenciais da prática atual; (2) situar o TIBER-EU e o CBEST entre testes mais leves; (3) criticar as promessas de fornecedores; (4) manter honesto o catálogo da MCH.

### 2.1 Panorama da prática

As organizações combinam gestão de vulnerabilidades, testes periódicos de aplicações web que seguem os temas do OWASP WSTG, exercícios de purple team e exercícios ocasionais guiados por ameaças sob regras do TIBER-EU ou semelhantes às do CBEST. Os nomes não são intercambiáveis, e nomes errados geram expectativas erradas sobre o aprendizado de detecção e a cobertura dos sistemas adjacentes ao SWIFT. O catálogo de Amira lista essas quatro atividades como linhas separadas, com alegações separadas. Chamar todas de red team é a forma pela qual os conselhos ouvem uma garantia sobre o SWIFT que nunca foi comprada, por isso ela corrige o vocabulário em cada reunião de planejamento até que os nomes fiquem separados em todas as notas de planejamento.

### 2.2 Especificidades dos testes guiados por ameaças

O TIBER-EU e o CBEST enfatizam cenários guiados por inteligência, controle pelo white team e aprendizado para detecção e resposta — e não a maximização do número de achados. Quando os executivos dizem "é só fazer pentest em tudo", Amira abre os guias públicos e mostra essas três expectativas; segundo eles, uma semana de varredura não é um programa guiado por ameaças. A linguagem das RFPs dela pede inteligência, desenho do white team e aprendizado de detecção, e não uma meta de número de achados, que é pontuada como teatro. Fornecedores que não conseguem descrever o desenho do white team saem da lista curta, e assim a Meridian Clearing House não compra uma varredura fantasiada de trabalho guiado por ameaças.

### 2.3 SP 800-115 e PTES

O NIST SP 800-115 e o PTES continuam sendo a espinha dorsal para planejar os tipos de avaliação e as etapas do engajamento. Os programas guiados por ameaças ficam por cima dessa disciplina de escopo, e não no lugar dela: autorização escrita, inclusões, exclusões e condições de parada continuam obrigatórias mesmo quando o cenário é guiado por inteligência e bienal. Pular o escopo porque o exercício é especial é como acontecem sondagens fora do escopo. Apoiar-se nessa espinha dorsal é o que permite a Amira manter os sistemas adjacentes ao SWIFT fora dos testes comuns e, ainda assim, conduzir um cenário bienal sob controle do white team. Por isso, as próprias ROE do cenário bienal nomeiam explicitamente a exclusão adjacente ao SWIFT.

### 2.4 Crítica a fornecedores

Fornecedores que prometem "red team completo em uma semana" sem inteligência, sem white team e sem metas de detecção estão vendendo uma varredura com teatro. A pontuação das RFPs de Amira pergunta quem atua como white team, quais metas de detecção serão medidas e como a inteligência molda os cenários; essas três respostas separam uma oferta real de um slogan. Ela já rejeitou uma proposta de red team completo em uma semana sem fase de inteligência e registrou o motivo no catálogo. Cada motivo de rejeição fica ali, para que o próximo comprador da Meridian Clearing House consiga ver o padrão das propostas de varredura com teatro.

### 2.5 Catálogo da MCH

Um catálogo vivo associa cada atividade ao que ela pode e não pode alegar. Os testes web trimestrais comuns não podem alegar a segurança do SWIFT; um exercício bienal guiado por ameaças não pode alegar cobertura contínua de cada mudança na web. A honestidade aqui impede que questionários de seguro e slides do conselho exagerem a garantia da Meridian Clearing House. Uma linha do catálogo sem a frase do que não pode alegar está incompleta, e Amira não deixa uma linha assim entrar em um material do conselho. Ela também bloqueia, nos materiais do conselho, linguagem que invente alegações proibidas por uma linha completa, mesmo quando o texto vem de um patrocinador sênior.

### 2.6 Atualidade

Amira revisa o catálogo duas vezes por ano diante das novas edições dos referenciais. As revisões detectam novas edições do ATT&CK, do WSTG, do TIBER-EU e do CBEST e riscam slogans aposentados de fornecedores que ainda estão em materiais antigos do conselho. Um catálogo que nunca é atualizado vira um museu da bravata do ano anterior. Ela data cada revisão e arquiva o índice de riscos, para que slogans aposentados não sejam colados de materiais antigos em materiais novos. A atualidade é um controle agendado, com data no calendário, e não a esperança de que alguém perceba uma alegação vencida antes que um comitê a perceba.

### 2.7 Narrativa

As revisões do catálogo recebem uma vez por ano um fornecedor de red team como crítico convidado. Amira pede que ele ataque as frases do que não pode ser alegado: se ele puder dizer honestamente que um teste web trimestral prova a segurança do SWIFT, a frase é fraca demais. O convidado do ano passado não conseguiu quebrar as frases; ainda assim, ela tornou um adjetivo mais preciso. Ela convida um fornecedor diferente a cada ano, para que a crítica não fique capturada. As revisões de atualidade também caçam slogans aposentados de fornecedores que persistem em materiais antigos do conselho e os riscam no índice do arquivo.

### 2.8 Riscos do arquivo

Os riscos feitos em materiais antigos ficam ligados ao registro de alterações do catálogo, para que os revisores vejam qual alegação foi suavizada e por quê; esquecer a história é como a bravata volta à linguagem do conselho. A reescrita de "estamos em conformidade com o CBEST" para um exercício inspirado no CBEST, com prazo definido e exclusões adjacentes ao SWIFT, é o exemplo resolvido, e as duas versões ficam no arquivo. Quando um diretor perguntou por que "em conformidade" sumiu do slide de 2025, o link do registro de alterações respondeu à pergunta sem reunião. Cada entrada do registro de alterações anota a data, a redação antiga e o revisor que aprovou a nova redação.

### Exemplo resolvido (MCH sintética)

Amira reescreve um slide do conselho de "estamos em conformidade com o CBEST" para "concluímos um exercício inspirado no CBEST em 2025; os testes trimestrais comuns excluem os sistemas adjacentes ao SWIFT, conforme o catálogo".

> **Caso sintético — Meridian Clearing House (MCH).** A organização de compensação, Amira Hassan e todos os números foram inventados para fins didáticos.

### Erros e limites

Testes guiados por ameaças e de sistemas de compensação exigem autorização jurídica especializada. Este livro só usa casos sintéticos e não traz código de exploração nem roteiro de ataque ao mercado.

### Exercícios

- **EX006 — Não intercambiáveis.** Por que não chamar todo teste de red team? *Rubrica:* 3 = profundidade, inteligência e metas de detecção diferentes; 2 = parcial; 1 = são iguais; 0 = nada.
- **EX007 — Ênfase dos testes guiados por ameaças.** Cite duas ênfases dos testes no estilo do TIBER-EU/CBEST. *Rubrica:* 3 = cenários guiados por inteligência e aprendizado de detecção e resposta (white team); 2 = uma; 1 = volume de achados; 0 = nada.
- **EX008 — Pergunta da RFP.** Dê uma pergunta de RFP que elimine o teatro. *Rubrica:* 3 = pergunta pelo white team, pelos objetivos de aprendizado ou pela inteligência; 2 = parcial; 1 = apenas o menor preço; 0 = nada.
- **EX009 — O que não pode alegar.** O que um catálogo precisa declarar além do que os testes fazem? *Rubrica:* 3 = o que eles não podem alegar; 2 = parcial; 1 = logotipos; 0 = nada.
- **EX010 — Reescrita do slide.** O que estava errado em "estamos em conformidade com o CBEST"? *Rubrica:* 3 = alegação exagerada / imprecisa; 2 = parcial; 1 = diz que nada estava errado; 0 = sem resposta.

### Síntese

A prática atual é um catálogo de atividades nomeadas com honestidade, e não um único jargão da moda.

### Continue estudando — capítulo 02 de 12

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Evidências de especialista

### Objetivos de aprendizagem

Você vai (1) definir evidências de nível de especialista; (2) tratar dados privilegiados de compensação; (3) desenhar evidências que resistam a questionamentos; (4) recusar capturas de tela teatrais.

### 3.1 Nível de especialista

A evidência precisa ser reproduzível sob as ROE, minimizada, com hash, com fuso horário e vinculada a uma decisão. "Parece ruim na ferramenta" não é nível de especialista: a reprodutibilidade é o critério, o drama não. Uma evidência de nível de especialista pode ser reproduzida sob as ROE por outro testador, usando os hashes, os carimbos de tempo e o contexto de escopo guardados no cofre. O FindingsDesk bloqueia a entrada nos materiais do conselho até que hash e responsável estejam presentes, então o drama sem esses campos nunca chega a um slide de comitê. Uma observação que falha nesse teste é reescrita até que outro especialista consiga repeti-la.

### 3.2 Dados privilegiados

As mensagens de compensação e os identificadores dos participantes são altamente sensíveis. A sensibilidade não é motivo para dispensar a evidência; é motivo para desenhar uma evidência mais segura. Amira mantém mensagens e identificadores reais fora das evidências comuns sempre que modelos sintéticos de mensagem conseguem mostrar a mesma classe de problema, e prefere esses modelos até na homologação. Tudo o que ainda parecer real demais é ocultado antes de entrar no cofre. O resultado é um cofre em que as entradas comuns provam o problema sem carregar dados de participantes que um vazamento ou uma exportação descuidada poderiam expor.

### 3.3 Resistência ao questionamento

O questionamento jurídico ou do white team pergunta: outro especialista conseguiria reproduzir esta observação sem o folclore do seu notebook? Se não, reescreva. Nos exercícios de questionamento, um segundo especialista tem dez minutos para encontrar um hash, um fuso horário ou uma cláusula das ROE que estejam faltando, e é pontuado por encontrar lacunas reais. Se a observação não resiste, Amira a reescreve antes da entrada no cofre; o reparo calmo depois de uma falha apontada pontua bem, a postura defensiva não. O exercício existe para que o questionamento jurídico ou do white team nunca encontre pela primeira vez, numa disputa real, uma alegação impossível de reproduzir.

### 3.4 Capturas de tela teatrais

Painéis de tema escuro sem hashes, carimbos de tempo ou contexto de escopo impressionam e não provam nada, e o cofre de evidências os rejeita de imediato. Eles desperdiçam o tempo do examinador e ensinam os juniores a confundir acabamento com evidência. Amira pede primeiro os artefatos sem graça — saída de comandos, trechos de configuração e hashes — e não discute temas de cores enquanto não existirem hashes e carimbos de tempo. Uma captura teatral rejeitada vira exemplo didático no exercício de questionamento seguinte, para que o mesmo erro de acabamento não volte nas evidências do trimestre seguinte.

### 3.5 Cadeia de custódia

Nos exercícios guiados por ameaças, os registros de custódia são tão importantes quanto os artefatos técnicos. Eles mostram quem guardou cada artefato, quando ele foi movido e quem autorizou a movimentação, e uma linha de custódia ausente é tratada com a mesma seriedade que um hash ausente. Os questionamentos do white team e da área jurídica costumam começar por perguntas sobre a cadeia de custódia, por isso o registro é construído durante o exercício, enquanto a memória está fresca, e não reconstruído depois. Um registro escrito de memória uma semana depois convida justamente à dúvida que os registros de custódia existem para eliminar.

### 3.6 Plataforma

Os campos do FindingsDesk exigem hash e responsável antes que um achado possa entrar nos materiais do conselho. Essa trava da plataforma é como a Meridian Clearing House mantém os padrões de especialista quando a pressão do calendário aumenta antes de uma reunião de comitê. Amira recusa exceções manuais para slides atrasados, mesmo quando a reunião é amanhã e a cor e a severidade parecem prontas. Os campos de cor e de severidade vêm depois do hash e do responsável, nunca no lugar deles. Um achado que fica fora do material porque falta o hash entra completo no material seguinte, o que custa um ciclo em vez de custar credibilidade.

### 3.7 Narrativa

Os exercícios de questionamento formam duplas de especialistas: um apresenta a evidência, o outro tem dez minutos para encontrar um hash, um fuso horário ou uma cláusula das ROE ausente. Amira pontua quem questiona por encontrar lacunas reais e quem apresenta pelo reparo calmo. As taxas de rejeição no cofre caíram depois disso, porque os apresentadores passaram a chegar com os hashes preenchidos. Os exercícios de custódia incluem uma apreensão simulada de notebook que pergunta se os hashes ainda se comprovam; a recuperação parcial de um hash conta como reprovação, e uma reprovação anterior financiou o trabalho com HSM para as chaves do cofre. O cenário de apreensão é refeito depois de cada mudança na forma de guardar as chaves do cofre.

### 3.8 Controles financiados por exercícios

O memorando de orçamento do HSM usou a reprovação no exercício de apreensão como prova principal: exercícios sem graça compram controles reais. O memorando pôs o fragmento recuperado ao lado do inventário de chaves do cofre, mostrando qual chave o notebook apreendido teria exposto. A área financeira aceitou a linha do HSM porque o registro do exercício tinha um plano datado, uma regra escrita e um resultado de reprovação que ninguém havia suavizado. Tratar o resultado parcial como reprovação foi o que tornou o exercício uma evidência crível naquele memorando; uma nota suavizada teria parecido uma quase aprovação e não teria financiado nada.

### 3.9 Regra de pontuação do exercício

As notas do exercício de apreensão são aprovado/reprovado, e a recuperação parcial de um hash é reprovação: um fragmento recuperado ainda prova que material de chave saiu do dispositivo, por isso a regra não tem nota intermediária. Amira escreve essa frase de aprovação ou reprovação no roteiro do exercício antes de ele começar e a mantém ao lado do plano do exercício para as turmas seguintes. O roteiro também nomeia antecipadamente quem vai pontuar, para que ninguém que conduziu o cenário de apreensão o avalie depois. Os operadores que querem uma nota intermediária depois que um fragmento é recuperado aprendem que a regra não se dobra por conforto; suavizá-la os ensinaria a negociar notas.

### Exemplo resolvido (MCH sintética)

Amira rejeita o slide de um fornecedor com um painel vermelho; aceita um pacote com identificadores de requisição, hashes, deslocamentos em relação ao UTC e a cláusula das ROE que permitiu a verificação.

> **Caso sintético — Meridian Clearing House (MCH).** A organização de compensação, Amira Hassan e todos os números foram inventados para fins didáticos.

### Erros e limites

Testes guiados por ameaças e de sistemas de compensação exigem autorização jurídica especializada. Este livro só usa casos sintéticos e não traz código de exploração nem roteiro de ataque ao mercado.

### Exercícios

- **EX011 — Quatro características.** Liste quatro características de uma evidência de nível de especialista. *Rubrica:* 3 = quatro entre reproduzível, minimizada, com hash, com fuso horário e vinculada a uma decisão; 2 = três; 1 = uma; 0 = nada.
- **EX012 — Preferência pelo sintético.** Por que preferir modelos sintéticos de compensação? *Rubrica:* 3 = a sensibilidade dos dados reais de compensação; 2 = parcial; 1 = preguiça; 0 = nada.
- **EX013 — Pergunta do questionamento.** Qual pergunta testa a resistência ao questionamento? *Rubrica:* 3 = outro especialista conseguiria reproduzir sem folclore?; 2 = parcial; 1 = está vermelho?; 0 = nada.
- **EX014 — Rejeição do teatro.** Por que rejeitar uma captura de tela de painel escuro sozinha? *Rubrica:* 3 = sem hash, horário ou contexto de escopo; 2 = parcial; 1 = estética; 0 = nada.
- **EX015 — Trava do cofre.** O que o FindingsDesk exige antes dos materiais do conselho? *Rubrica:* 3 = hash e responsável (e campos relacionados); 2 = um; 1 = cor; 0 = nada.

### Síntese

A evidência de especialista resiste ao questionamento; o teatro não entra no cofre.

### Continue estudando — capítulo 03 de 12

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Risco avançado e ética

### Objetivos de aprendizagem

Você vai (1) pesar o risco sistêmico para a compensação; (2) lidar com conflitos de interesse; (3) resistir à pressão pelas aparências; (4) desenhar condições éticas de parada para o trabalho guiado por ameaças.

### 4.1 Risco sistêmico

A lente de risco de Amira é sistêmica, e não apenas local da MCH. Um teste descuidado que atrase a liquidação pode prejudicar muitos participantes além da Meridian Clearing House, por isso uma janela de teste é combinada com as operações antes que qualquer cenário toque o caminho da liquidação. Antes de aprovar o desenho, ela pergunta quem mais faz compensação por esse caminho e o que uma pausa de quinze minutos causaria. Cenários que precisam de impacto real sobre participantes são rejeitados na fase de desenho e nunca saem da revisão de desenho. O dano sistêmico também é a razão de existirem, no programa, a autoridade de parada e os bloqueios de calendário.

### 4.2 Conflitos

Investimentos pessoais, empregadores anteriores e amizades com fornecedores entram no registro de conflitos antes de começarem as reuniões de pontuação. Declarar-se impedido é normal na Meridian Clearing House, e não prejudica a carreira, e Amira se declara impedida sempre que uma decisão toca uma das entradas dela. Os juniores já a viram sair de uma reunião de pontuação de fornecedores quando um antigo empregador apresentou proposta, o que ensina o hábito melhor do que uma página de política sozinha. O registro é lido em voz alta no início de cada reunião de pontuação, para que um conflito seja declarado antes de existirem notas, e não descoberto depois que um contrato foi assinado.

### 4.3 Pressão pelas aparências

Datas de divulgação de resultados e demonstrações em conferências nunca justificam enterrar achados. Respostas da gestão podem ficar ao lado dos achados; a exclusão, não. Quando um líder de produto pediu para segurar um achado até depois de uma demonstração em conferência, Amira acrescentou a resposta dele ao lado do achado e registrou a recusa sob o estatuto de ética. Cada entrada de recusa nomeia o papel de quem pediu, o identificador do achado e a data, para que o comitê de riscos do conselho veja os padrões de pressão. A pressão pelas aparências é previsível, por isso o estatuto de ética a responde antes de o e-mail chegar.

### 4.4 Paradas em testes guiados por ameaças

Amira recusa exercícios em que ninguém consegue parar o red team em minutos. A autoridade de parada do white team é escrita antes de os cenários começarem, com nomes e números de telefone que funcionam sob estresse, e nenhum cenário começa antes que esses contatos nomeados confirmem que podem ser acionados. Antes de cada ano de exercícios guiados por ameaças, o líder do white team liga para a linha de parada durante o ensaio e registra quanto tempo a resposta levou. Um atraso simulado de quinze minutos na liquidação é motivo suficiente para parar no meio do jogo; os estudantes que continuam por mais um objetivo são reprovados no exercício de mesa de ética.

### 4.5 Uso dual

Publicar caminhos de exploração específicos da compensação está fora do escopo deste currículo e das palestras públicas da MCH. As palestras de Amira descrevem o método de decisão, o catálogo e as frases do que não pode ser alegado, nunca um caminho através da conexão de um participante, e o último slide dela lista essa recusa ao lado de "nenhuma demonstração ao vivo contra participantes". Quando um organizador de conferência pediu um passo a passo sobre a compensação, ela ofereceu em vez disso uma palestra sobre o objeto de decisão DEC-14 e explicou o motivo em termos simples. A disciplina do uso dual faz parte da identidade do especialista, e não é um apêndice opcional para uma vaga em conferência.

### 4.6 Cuidado

A ética inclui sono, limites de horas e nenhum heroísmo perto das janelas de liquidação. Os limites de horas valem para a equipe do white team e também para os operadores, porque um responsável pela parada cansado é uma parada que falha. Amira os aplica para que pessoas cansadas não se tornem o risco que o programa deveria reduzir. Os bloqueios de calendário impedem reservas de cenários nos picos de liquidação e mostram o estatuto de ética como motivo da rejeição, o que torna a política visível no momento da reserva, e não numa repreensão posterior. Nem a própria Amira consegue agendar um horário de cenário passando por cima de um bloqueio.

### 4.7 Narrativa

O exercício de mesa sobre risco sistêmico usa um atraso simulado de quinze minutos na liquidação. Os estudantes do white team precisam parar um cenário no meio do jogo quando o atraso aparece, e Amira reprova qualquer estudante que continue por apenas mais um objetivo. Ela conduz o exercício de mesa antes de cada ano de exercícios guiados por ameaças, para que o reflexo de parar seja ensaiado, e não inventado sob estresse. Os limites de horas perto da liquidação são garantidos por bloqueios de calendário nos horários de cenário, de modo que o heroísmo não possa ser agendado, nem mesmo por ela. O debriefing registra quanto tempo cada estudante levou para acionar a parada, e os tempos mais lentos são discutidos sem nomes.

### 4.8 Bloqueios de calendário

Quando alguém tenta reservar um cenário no pico de liquidação, o bloqueio de calendário rejeita o pedido e cita como motivo a cláusula pertinente do estatuto de ética. Mostrar o estatuto diz a quem pediu que o bloqueio é uma decisão de política, e não um acidente de agenda, e permite ler a regra exata antes de discutir com alguém. Com o tempo, isso também ensina os solicitantes a ler o estatuto antes de pedir. Uma rejeição que dissesse apenas "horário indisponível" convidaria a uma nova reserva uma hora depois; uma rejeição que nomeia a cláusula encerra a tentativa na origem.

### 4.9 Cópias das rejeições

Os e-mails de rejeição dos bloqueios de calendário vão automaticamente com cópia para a caixa compartilhada dos mantenedores do estatuto, de modo que tentativas repetidas de reservar no pico de liquidação ficam visíveis para quem é dono do estatuto e nenhum revisor isolado pode absorvê-las em silêncio. Amira revisa essas cópias a cada trimestre como sinal de pressão cultural, e não como caça a indivíduos. Uma equipe que vive esbarrando no bloqueio costuma estar com falta de capacidade, o que é um problema de desenho do programa, e não de disciplina, por isso ela abre uma clínica de decisões sobre capacidade e calendário em vez de conceder exceções.

### Exemplo resolvido (MCH sintética)

Amira cancela, dois dias antes de um pico de liquidação, um cenário proposto que não tinha um botão de parada do white team, citando o risco sistêmico e o estatuto de ética.

> **Caso sintético — Meridian Clearing House (MCH).** A organização de compensação, Amira Hassan e todos os números foram inventados para fins didáticos.

### Erros e limites

Testes guiados por ameaças e de sistemas de compensação exigem autorização jurídica especializada. Este livro só usa casos sintéticos e não traz código de exploração nem roteiro de ataque ao mercado.

### Exercícios

- **EX016 — Lente sistêmica.** Por que o risco da compensação é diferente do risco do site de um único banco? *Rubrica:* 3 = muitos participantes / impacto na liquidação; 2 = parcial; 1 = é igual; 0 = nada.
- **EX017 — Impedimento.** Dê um motivo válido para se declarar impedido. *Rubrica:* 3 = investimento, antigo empregador ou amizade com fornecedor; 2 = parcial; 1 = antipatia; 0 = nada.
- **EX018 — Enterrar versus responder.** O que pode ficar ao lado de um achado sob pressão? *Rubrica:* 3 = a resposta da gestão, e não a exclusão; 2 = parcial; 1 = a exclusão; 0 = nada.
- **EX019 — Botão de parada.** O que precisa existir antes de os cenários guiados por ameaças começarem? *Rubrica:* 3 = autoridade de parada do white team; 2 = parcial; 1 = diz que nada é necessário; 0 = sem resposta.
- **EX020 — Pico de liquidação.** Por que cancelar perto do pico de liquidação quando não há botão de parada? *Rubrica:* 3 = risco sistêmico + ética; 2 = parcial; 1 = medo; 0 = nada.

### Síntese

A ética na escala da compensação inclui o dano sistêmico, o impedimento, a recusa a enterrar achados e uma autoridade de parada real.

### Continue estudando — capítulo 04 de 12

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX020 (as de EX021–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). A Meridian Clearing House, Amira Hassan e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Opções, evidências, incertezas, recomendação e responsável (as opções rejeitadas também contam).

**EX002.** Aleatória: taxas de detecção que variam entre tentativas; epistêmica: não se sabe se existe um canal de conexão até o núcleo da compensação.

**EX003.** Ele nem aceita o risco residual nem agenda sua gestão; é deriva sem gestão.

**EX004.** Somente os papéis listados no estatuto de governança (tipicamente no nível de CISO), sem inventar autoridade.

**EX005.** Os exercícios anuais guiados por ameaças, por razões de capacidade.

**EX006.** Porque os tipos de avaliação diferem em profundidade, uso de inteligência e metas de aprendizado de detecção.

**EX007.** Cenários guiados por inteligência e aprendizado para detecção e resposta (com controle pelo white team).

**EX008.** Descreva o desenho do seu white team e os objetivos de aprendizado de detecção do engajamento.

**EX009.** O que cada atividade não pode alegar.

**EX010.** Exagera a alegação e confunde um exercício inspirado, feito uma vez, com as exclusões permanentes dos testes comuns.

**EX011.** Reproduzível, minimizada, com hash e com fuso horário (vinculada a uma decisão também conta).

**EX012.** As mensagens reais de compensação e os identificadores dos participantes são altamente sensíveis.

**EX013.** Outro especialista conseguiria reproduzir esta observação sem o folclore do notebook?

**EX014.** Falta hash, carimbo de tempo e contexto de escopo — é teatro, não evidência.

**EX015.** No mínimo, o hash da evidência e o responsável.

**EX016.** A interrupção pode afetar muitos participantes e a liquidação, e não apenas o site de uma instituição.

**EX017.** Um investimento pessoal, uma relação com um antigo empregador ou uma amizade próxima com um fornecedor que afete a imparcialidade.

**EX018.** Uma resposta da gestão pode ficar ao lado dele; o achado não pode ser excluído.

**EX019.** Autoridade escrita do white team para parar o exercício em minutos.

**EX020.** O risco sistêmico para a liquidação mais o estatuto de ética, que exige um botão de parada.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide. <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- FIRST. CVSS v3.1 Specification Document. <https://www.first.org/cvss/v3.1/specification-document>
- MITRE ATT&CK, including T1078 Valid Accounts. <https://attack.mitre.org/>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
