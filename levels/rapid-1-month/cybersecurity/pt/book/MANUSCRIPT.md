# Cibersegurança: um curso guiado de um mês

- Edição: texto público em português, 14 de outubro de 2026
- Idioma: português do Brasil (`pt`)
- Curso: rápido, um mês; cerca de 80 horas de estudo planejado
- Estado: Vinte capítulos publicados, com os exercícios EX001–EX036 e as resoluções. O mínimo de planejamento do curso rápido é 20 aulas e não há máximo. A revisão técnica, linguística, de fontes e de acessibilidade **não está completa**. Isto não é uma qualificação concluída.
- Mantenedor: [hiagokinlevi](https://github.com/hiagokinlevi)
- Texto original: [CC0 1.0](../../../../../LICENSE), dentro do [aviso de direitos](../../../../../RIGHTS.md). As fontes externas ligadas abaixo conservam os próprios direitos.

Esta edição em português acompanha o livro em inglês, cujo conteúdo didático corresponde ao blob `c62a23de520c86a258daf888daa7a3098f377c4a`; a versão inglesa atual removeu apenas os vinte mapas automáticos de aula e recebeu a correção do número de rótulos descrita no capítulo 4. Traduzir o texto não encerra a revisão e não transforma o curso numa qualificação pronta.

## Como estudar este livro

Leia a explicação antes de tentar um exercício. Trabalhe só com a biblioteca fictícia descrita aqui. Mantenha um caderno curto com os fatos que você observa, as premissas que você adota e a pergunta que faria em seguida. Compare as suas respostas com as resoluções no final. Uma alternativa plausível pode estar correta quando identifica as próprias premissas e sustenta a decisão com evidência.

Este é o **livro principal único** do curso rápido de Cibersegurança em português. Ele incorpora o texto anterior de letramento em segurança. Cada capítulo publicado ensina uma ideia, com um exemplo e exercícios. As resoluções estão no apêndice final. O mínimo de planejamento deste livro rápido é 20 aulas, e não há máximo. Estes vinte capítulos publicados atingem esse mínimo e não são uma qualificação concluída.

| Capítulo do assunto | Exercícios escritos | Publicação |
|---|---:|---|
| [1. Fundamentos e decisões](#ch-01) | EX001–EX005 | Publicado |
| [2. Escopo, permissão e prática segura](#ch-02) | EX006–EX010 | Publicado |
| [3. Sistemas, dados e dependências](#ch-03) | EX011–EX015 | Publicado |
| [4. Laboratório guiado e síntese aplicada](#ch-04) | EX016–EX020 | Publicado |
| [5. O que se pode dizer sobre uma reserva](#ch-05) | EX021 | Publicado |
| [6. Uma alteração manuscrita não é uma correção](#ch-06) | EX022 | Publicado |
| [7. Uma fila pendente durante uma interrupção](#ch-07) | EX023 | Publicado |
| [8. Um procedimento fraco ainda não é uma vulnerabilidade](#ch-08) | EX024 | Publicado |
| [9. Uma contagem de vereditos não é uma severidade](#ch-09) | EX025 | Publicado |
| [10. Um horário falado não é uma impressão](#ch-10) | EX026 | Publicado |
| [11. Uma folha nomeada não libera a sala](#ch-11) | EX027 | Publicado |
| [12. Uma linha ausente não é uma sala livre](#ch-12) | EX028 | Publicado |
| [13. A nomeação de ontem não vincula o dia de hoje](#ch-13) | EX029 | Publicado |
| [14. Uma página nova responde só às próprias linhas](#ch-14) | EX030 | Publicado |
| [15. Duas páginas não são uma agenda](#ch-15) | EX031 | Publicado |
| [16. Um horário de criação não apaga uma linha impressa](#ch-16) | EX032 | Publicado |
| [17. Linhas coincidentes não são uma causa](#ch-17) | EX033 | Publicado |
| [18. As páginas anteriores permanecem no arquivo](#ch-18) | EX034 | Publicado |
| [19. Uma página de reservas não abre a lista de contatos](#ch-19) | EX035 | Publicado |
| [20. A nota que pode sair da sala](#ch-20) | EX036 | Publicado |

<a id="ch-01"></a>

## Capítulo 1 — Cibersegurança: fundamentos e decisões

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Descrever um ativo, uma ameaça, uma vulnerabilidade, um controle, um cenário de risco e uma evidência em linguagem comum.
2. Explicar confidencialidade, integridade e disponibilidade com um exemplo concreto de serviço.
3. Separar uma observação de uma premissa e de uma recomendação.
4. Descrever as seis funções do NIST Cybersecurity Framework (CSF) 2.0 sem tratá-las como uma sequência obrigatória ou uma lista de produtos.
5. Produzir uma nota de segurança pequena e revisável sem sondar um sistema real.

### 1.1 Comece pelo serviço e pelas pessoas

A segurança começa com uma pergunta: **O que precisa continuar funcionando, para quem, e que dano viria se não funcionasse?** A resposta dá sentido aos detalhes técnicos. Um servidor não é valioso apenas por ser um servidor. Ele importa porque sustenta um serviço, guarda informação ou ajuda pessoas a concluir uma tarefa. Uma página de acesso importa porque controla o acesso ao que está atrás dela. Uma cópia de segurança importa se de fato puder restaurar o serviço no tempo de que as pessoas precisam.

O caso de ensino é a **Harbor Library**, uma biblioteca pública inteiramente fictícia. Moradores reservam salas de estudo por um site. A equipe pode ver as reservas, resolver conflitos e imprimir a agenda do dia. A biblioteca também guarda uma lista de frequentadores que pediram para receber anúncios de eventos. São detalhes inventados; nenhuma biblioteca real e nenhum registro pessoal são usados nesta aula.

Antes de propor uma ferramenta de segurança, liste os resultados do serviço:

| Resultado do serviço | Pessoas afetadas | Exemplo de dano se falhar | Pergunta para verificar |
|---|---|---|---|
| Moradores conseguem reservar salas disponíveis | Moradores e equipe do balcão | Um morador se desloca até uma sala que foi reservada em duplicidade | Como reservas em conflito são impedidas? |
| A equipe consegue ver uma agenda diária correta | Equipe e moradores | A equipe entrega uma sala ao grupo errado | Qual é a agenda de referência? |
| Contatos de eventos são usados só para anúncios | Assinantes | Divulgação indesejada ou uso indevido dos dados de contato | Quem pode exportar a lista de contatos, e por quê? |

Esta tabela é um primeiro modelo, não um inventário verificado. Numa organização real, um responsável pelo serviço confirmaria os resultados e a interrupção aceitável. Nos exercícios daqui, o caso fictício é o escopo inteiro; não teste um site real.

### 1.2 Nomeie ativos e dependências

Um **ativo** é algo de valor que ajuda a prestar ou a proteger um serviço. Pode ser informação, software, um dispositivo, uma conta, um processo ou o tempo e a confiança de uma pessoa. Os registros de reserva da Harbor Library são ativos de informação. A aplicação de reservas, as contas da equipe, as cópias de segurança e a agenda impressa também são ativos. O valor e o tratamento diferem: uma agenda impressa pode ser essencial durante uma interrupção, enquanto uma conta da equipe pode alterar reservas e, por isso, precisa de controles de acesso fortes.

Uma **dependência** é algo de que um serviço precisa para funcionar. A página de reservas pode precisar de um serviço de identidade, de um banco de dados, de uma conexão de rede e de procedimentos da equipe. Uma dependência não se torna automaticamente um ponto único de falha; essa afirmação exige evidência sobre alternativas e recuperação. Desenhe uma cadeia simples antes de atribuir um controle:

```text
Morador -> página de reserva -> depósito de reservas -> agenda da equipe
                            \-> mensagem de confirmação
Membro da equipe -> acesso da equipe -> depósito de reservas
```

As setas significam que informação ou um pedido se move entre partes do serviço. Elas não provam que a implementação foi construída assim. Essa distinção importa: um diagrama é uma hipótese até que um responsável ou uma observação a confirme.

### 1.3 Três propriedades da informação

O modelo conhecido de **confidencialidade, integridade e disponibilidade** descreve três modos diferentes de um serviço ou da sua informação sofrer dano. É uma lente de ensino, não uma lista exaustiva de todos os danos.

- **Confidencialidade** pergunta quem pode ver a informação. Se a lista de contatos de eventos é enviada a um destinatário não autorizado, a confidencialidade é afetada mesmo que o site de reservas continue no ar.
- **Integridade** pergunta se a informação está correta e se só muda do modo pretendido. Se uma reserva é alterada em silêncio, a agenda pode estar disponível e mesmo assim errada.
- **Disponibilidade** pergunta se as pessoas autorizadas conseguem usar o serviço quando precisam. Uma interrupção pode impedir um morador de reservar e a equipe de consultar a agenda, mesmo que nenhuma informação seja divulgada.

Um evento pode afetar várias propriedades. Por exemplo, uma conta com privilégios excessivos poderia exportar a lista de contatos e mudar reservas de sala. Evite reduzir a análise a um único rótulo. Declare a consequência real, as pessoas afetadas e o que se sabe.

Outras preocupações também podem importar: se os dados de uma pessoa foram coletados para uma finalidade legítima, se os registros podem ser ligados a uma ação autorizada e se a biblioteca consegue restaurar o serviço depois de uma interrupção. Capítulos posteriores tratarão disso com mais profundidade.

### 1.4 Distinga ameaça, vulnerabilidade, evento e risco

Uma **ameaça** é uma circunstância ou um evento com potencial de dano. A [entrada de ameaça no glossário do NIST](https://csrc.nist.gov/glossary/term/threat) inclui, entre os impactos possíveis, acesso não autorizado, divulgação, modificação e negação de serviço. Uma ameaça não é prova de que um ataque ocorreu.

Uma **vulnerabilidade** é uma fraqueza que uma fonte de ameaça poderia explorar ou disparar. A [entrada de vulnerabilidade no glossário do NIST](https://csrc.nist.gov/glossary/term/vulnerability) inclui fraquezas em sistemas, procedimentos, controles e implementações. Uma senha de equipe reutilizada é uma fraqueza possível. Se essa fraqueza existe na Harbor Library é algo desconhecido; o caso não afirma que exista.

Um **evento** é algo observado: por exemplo, a agenda fictícia ficou indisponível das 10:00 às 10:20. Um evento, sozinho, não estabelece a causa. Pode resultar de manutenção, de um erro de software, de uma falha de rede ou de atividade maliciosa. Um **incidente** é um evento, ou uma série de eventos, julgado como algo que exige resposta de segurança segundo critérios definidos. O curso usará os critérios de resposta da organização, em vez de rotular todo erro como ataque.

Um **cenário de risco** liga uma condição plausível a um resultado: “Se uma pessoa não autorizada alterar reservas de sala, moradores podem receber confirmações incorretas e a equipe pode alocar salas de modo incorreto.” Essa frase não atribui probabilidade. Também não afirma que qualquer alteração não autorizada tenha ocorrido. Para priorizar a ação, acrescente contexto: quão crítico é o serviço, que controles existem, que evidência sustenta o cenário e que incerteza permanece? Um número sem essas entradas criaria uma confiança falsa.

As seis funções do CSF 2.0 — **Governar (Govern), Identificar (Identify), Proteger (Protect), Detectar (Detect), Responder (Respond) e Recuperar (Recover)** — oferecem uma linguagem comum para discutir essas responsabilidades. O NIST as descreve como resultados concorrentes e contínuos, não como um procedimento rígido de seis passos. Na Harbor Library, designar um responsável pelos dados de reserva é governança; entender a dependência da reserva é identificação; restrições de acesso são proteção; notar mudanças inesperadas é detecção; conter o uso indevido de uma conta é resposta; restaurar uma agenda confiável é recuperação. Uma decisão prática pode envolver mais de uma função. Veja as [perguntas frequentes do NIST CSF 2.0](https://www.nist.gov/cyberframework/faqs) para a descrição do próprio framework.

### 1.5 Controles respondem a uma preocupação específica

Um **controle** é uma medida destinada a reduzir risco ou melhorar um resultado. Pode ser técnico, procedimental ou organizacional. “Usar software de segurança” é vago demais para avaliar. “Exigir que a equipe use um segundo fator aprovado ao entrar na página de administração das reservas” descreve uma população, uma ação e um limite. Ainda precisa de verificação: todas as contas da equipe seguem a regra, uma pessoa aprovada consegue recuperar o acesso, e existe um processo seguro de exceção?

Para a segurança digital pessoal, a [orientação Secure Our World da CISA](https://www.cisa.gov/secure-our-world) recomenda reconhecer e reportar phishing, usar senhas fortes e um gerenciador de senhas, ativar a autenticação multifator e atualizar o software. São ações iniciais úteis. Elas não substituem uma análise específica do serviço. Uma biblioteca poderia implementar as quatro e ainda ter um processo de restauração não testado ou um responsável pouco claro pela lista de contatos de eventos.

Pense em **prevenir, notar, agir e recuperar**. Um controle que reduz a chance de uso indevido pode falhar ou ser contornado. A biblioteca, portanto, também precisa de um modo de reconhecer mudanças anormais, de uma pessoa que possa agir e de um procedimento para restaurar a informação correta. A combinação certa depende da importância do serviço e de fatos verificados. Mais controles não são automaticamente melhores: um procedimento sem dono dificilmente funciona sob pressão.

### 1.6 Use evidência sem exagerar a conclusão

O letramento em segurança inclui saber em que uma frase se baseia. Uma nota de trabalho útil separa quatro tipos de frase:

1. **Fato observado:** “O registro fictício do exercício anota uma falha de acesso da equipe às 09:14.” A evidência é nomeada e o alcance é claro.
2. **Fato relatado:** “O responsável pelo serviço diz que a agenda impressa é atualizada toda manhã.” Quem fala e o momento são nomeados; a frase ainda não foi conferida de modo independente.
3. **Inferência:** “Se a impressão ocorre só de manhã, a equipe pode não ver reservas posteriores durante uma interrupção.” Isso decorre do relato, mas ainda precisa de teste.
4. **Recomendação:** “Teste uma interrupção ao meio-dia e compare a agenda impressa com a lista de reservas de referência.” Isso propõe uma verificação, não uma afirmação sobre o sistema atual.

A distinção evita um erro comum: transformar uma explicação plausível num achado. Se uma página fica indisponível uma vez, é inexato escrever “A biblioteca foi atacada.” Em vez disso, registre o horário, o que falhou, quem observou e que registros ou testemunho do responsável poderiam ajudar a determinar a causa. Não colete nem publique informação pessoal de frequentadores para fazer um ponto de ensino.

A evidência tem limites. Uma captura de tela de um trabalho de cópia de segurança pode mostrar que o trabalho foi configurado. Não prova que uma cópia utilizável foi produzida, nem que uma restauração completa do serviço atenderá às necessidades da biblioteca. Um único teste ao meio-dia não prova que o serviço está sempre disponível. Boas notas identificam tanto o que a evidência sustenta quanto o que ela não pode estabelecer.

### 1.7 Uma análise guiada pequena

Leia este registro **sintético**. Foi inventado para este livro, não é um incidente real:

```text
09:00  A equipe imprime a agenda diária das salas.
10:05  Um morador recebe a confirmação de reserva da Sala 2 às 14:00.
11:30  A página de reservas fica indisponível para o balcão por 20 minutos.
11:42  A equipe usa a agenda impressa às 09:00 para responder a uma pergunta sobre a sala.
12:10  Um membro da equipe nota que a reserva das 10:05 está ausente da impressão.
```

O que fica estabelecido? A impressão é anterior à reserva, e a reserva posterior está ausente dela. O registro também diz que a página ficou indisponível para o balcão por vinte minutos. Ele **não** estabelece por que a página falhou, se os moradores conseguiriam usá-la ou se alguém acessou a lista de contatos. A primeira preocupação é que a equipe pode decidir com informação desatualizada durante uma interrupção. Uma próxima ação proporcional é perguntar ao responsável pelo serviço como a equipe deve confirmar reservas atuais quando a agenda ao vivo está indisponível e, então, testar essa alternativa com reservas sintéticas.

Uma nota de análise compacta poderia dizer:

> Num exercício fictício de interrupção, a equipe usou uma impressão das 09:00 depois de uma reserva das 10:05. A impressão não incluía essa reserva. O exercício, portanto, demonstra um risco de agenda desatualizada para decisões do balcão; não estabelece a causa da interrupção da página de reservas. Confirme o procedimento alternativo com o responsável pelo serviço e teste-o com uma reserva posterior.

Este é o padrão do resto do curso: nomeie o serviço, descreva a evidência, limite a conclusão e proponha uma verificação segura. O capítulo 2 acrescenta autorização, escopo e condições de parada para que este método possa ser praticado com responsabilidade.

### Resumo do capítulo 1

O vocabulário de segurança só é útil quando melhora uma decisão. Nomeie primeiro o serviço e as pessoas, mapeie ativos valiosos e dependências, descreva o tipo de dano e, então, ligue uma condição plausível a evidência e a um controle proporcional. Mantenha distintas as observações, as premissas, as inferências e as recomendações. O capítulo seguinte mostra como praticar esse trabalho dentro de um limite autorizado.

### Exercícios do capítulo 1

Use só o caso fictício. Compare o seu trabalho com o apêndice final de resoluções.

### EX001 — Mapa de ativos e dependências

- **Objetivo:** Distinguir um serviço, um ativo e uma dependência.
- **Entrada:** A descrição da Harbor Library nas seções 1.1–1.2.
- **Condição segura:** Trabalhe só com este texto; não navegue nem teste uma biblioteca real.
- **Tarefa:** Nomeie o serviço de reservas, três ativos diferentes e duas dependências. Explique por que um ativo importa para os moradores.
- **Evidência esperada:** Um mapa anotado de cinco itens ou uma tabela curta.
- *Rubrica:* 3 = resultado de serviço claro, três ativos plausíveis de pelo menos dois tipos, duas dependências e uma consequência para o morador;; 2 = faltam um tipo de ativo ou uma dependência, sem tratar um site real como o serviço;; 1 = o serviço fica vago e não há consequência para o morador;; 0 = nenhuma.

### EX002 — Três tipos de dano

- **Objetivo:** Aplicar confidencialidade, integridade e disponibilidade sem confundi-las.
- **Entrada:** Os serviços fictícios da seção 1.1.
- **Condição segura:** Invente eventos; não use informação pessoal real.
- **Tarefa:** Escreva um cenário distinto para cada uma das três propriedades. Em cada um, nomeie as pessoas afetadas e um fato que você precisaria conferir antes de afirmar que o evento ocorreu.
- **Evidência esperada:** Três cenários rotulados e três perguntas de verificação.
- *Rubrica:* 3 = o dano corresponde à propriedade, as pessoas são identificadas e um evento não observado não é afirmado como fato;; 2 = as três propriedades aparecem, mas uma verificação fica vaga;; 1 = as propriedades se misturam ou um evento não observado vira fato;; 0 = nenhuma.

### EX003 — Observação ou inferência

- **Objetivo:** Calibrar uma conclusão à evidência disponível.
- **Entrada:** O registro sintético de cinco linhas na seção 1.7.
- **Condição segura:** Analise só o texto fornecido.
- **Tarefa:** Classifique estas afirmações como sustentadas, não sustentadas ou inferência razoável: (a) uma reserva das 10:05 estava ausente da impressão das 09:00; (b) um atacante causou a interrupção; (c) uma impressão desatualizada poderia enganar a equipe; (d) a lista de contatos de eventos foi exportada. Explique cada classificação.
- **Evidência esperada:** Quatro classificações e uma frase de raciocínio para cada uma.
- *Rubrica:* 3 = (a) sustentada, (b) não sustentada, (c) inferência razoável, (d) não sustentada, cada uma com limite ligado ao registro;; 2 = três classificações corretas, sem transformar (b) ou (d) em fato;; 1 = o ataque ou a exportação é tratado como fato;; 0 = nenhuma.

### EX004 — Controle e verificação

- **Objetivo:** Propor uma medida proporcional com evidência de efetividade.
- **Entrada:** A questão da agenda desatualizada na seção 1.7.
- **Condição segura:** Desenhe um exercício em papel; não altere um sistema ao vivo.
- **Tarefa:** Proponha um procedimento alternativo para a equipe durante uma interrupção da página de reservas. Defina o responsável, o gatilho, o passo de verificação e um modo de falha.
- **Evidência esperada:** Um procedimento em quatro partes mais um teste de exemplo com uma reserva sintética.
- *Rubrica:* 3 = responsável e gatilho explícitos, um teste capaz de detectar dado desatualizado e uma limitação honesta;; 2 = há procedimento, mas falta uma das quatro partes;; 1 = altera um sistema ao vivo ou não há teste;; 0 = nenhuma.

### EX005 — Visão das seis funções

- **Objetivo:** Usar as funções do CSF 2.0 como vocabulário para decisões de serviço.
- **Entrada:** A Harbor Library e as [perguntas frequentes do NIST](https://www.nist.gov/cyberframework/faqs).
- **Condição segura:** Trabalhe só com o caso fictício.
- **Tarefa:** Dê um exemplo da Harbor Library para cada uma das funções Governar, Identificar, Proteger, Detectar, Responder e Recuperar. Explique por que concluir uma função não termina o trabalho de segurança.
- **Evidência esperada:** Seis exemplos curtos e uma explicação de duas frases.
- *Rubrica:* 3 = exemplos que correspondem a cada função, reconhecem responsabilidade compartilhada e não tratam as funções como sequência única;; 2 = as seis funções aparecem, sem a explicação de continuidade;; 1 = as funções viram sequência de uma vez só ou lista de produtos;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 20

[← Início do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Escopo, permissão e prática segura

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de definir uma atividade de estudo permitida, identificar quem pode autorizá-la, escrever condições de parada, escolher um conjunto de dados sintéticos e relatar uma observação sem coletar informação pessoal desnecessária.

### 2.1 A curiosidade precisa de um limite

O primeiro capítulo usou uma agenda inventada para que qualquer leitor pudesse praticar o método. Um site público é diferente. Conseguir abrir uma página não significa que você tem permissão para sondar o sistema por trás dela, testar contas, coletar registros ou perturbar a operação. Um exercício de treino precisa de um ambiente nomeado, de um responsável, de ações permitidas e de um modo de parar. Ler um documento público e testar um serviço ao vivo são atividades diferentes, mesmo quando a intenção de quem estuda é educacional.

Este curso usa registros **sintéticos** e exercícios em papel por padrão. Quem estuda só pode trabalhar com um sistema real depois que o responsável autorizou a atividade específica e a pessoa entendeu as regras da organização. Esta é uma regra de prática do curso, não aconselhamento jurídico sobre qualquer jurisdição. Se a autorização não estiver clara, o passo seguinte é perguntar ao responsável; não é testar primeiro e explicar depois.

O [guia de testes NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) descreve o planejamento e a condução de avaliações técnicas. A [definição de regras de engajamento](https://csrc.nist.gov/glossary/term/Rules_of_Engagement) enfatiza diretrizes e restrições fixadas antes de um teste. Este curso rápido permanece no nível de definir um escopo seguro e revisar evidência. Ele não exige teste ativo dos sistemas de outra pessoa.

### 2.2 Escreva um briefing de autorização

Imagine que o responsável pelo serviço da Harbor Library quer que a equipe ensaie o que fazer se a página de reserva de salas ficar indisponível. O exercício aprovado pode ser inteiramente offline. Um briefing de uma página deve responder a sete perguntas:

| Pergunta | Resposta do exercício da Harbor Library |
|---|---|
| Quem é o responsável pelo exercício? | O responsável fictício pelo serviço designa uma liderança do balcão. |
| O que está no escopo? | Uma agenda em papel, reservas inventadas e uma dramatização de uma interrupção de 20 minutos. |
| O que está fora do escopo? | Contas ao vivo, moradores reais, a página real de reservas e dados de produção. |
| O que as pessoas participantes podem fazer? | Comparar reservas impressas e sintéticas posteriores; registrar decisões. |
| Quando ocorre? | Durante uma sessão de treino agendada de 30 minutos. |
| O que o encerra? | O limite de tempo, uma interação inesperada com um sistema real ou uma preocupação de uma pessoa participante com a própria segurança. |
| Quem recebe o resultado? | O responsável pelo serviço recebe uma nota curta com evidência e limitações. |

O briefing é específico o bastante para um iniciante seguir. Também impede que o exercício se expanda para um teste não aprovado de conta ou de rede. Uma frase como “testar a biblioteca” não é um escopo adequado, porque não identifica sistemas, ações, pessoas ou tempo.

### 2.3 Decida que informação é necessária

Boa evidência não exige copiar tudo o que está disponível. O exercício precisa de um horário de reserva, de um identificador de sala, de um horário de impressão e de uma decisão tomada pela equipe. Não precisa do nome de um morador, de dados de contato nem de credenciais de conta. Substitua nomes por rótulos inventados, como `Resident A`, e use identificadores artificiais de reserva. Isso reduz o dano possível e torna o exercício reproduzível para outras pessoas.

Num relatório real de incidente, preserve a evidência exigida segundo o processo aprovado da organização; não apague nem transforme por conta própria registros que você tem o dever de reter. Num exercício de sala de aula, comece com entradas sintéticas para que a pergunta de privacidade seja simples. Quem estuda deve conseguir explicar por que cada campo do exercício está presente. Se um campo não sustenta um objetivo, remova-o.

A amostra seguinte tem informação suficiente para uma comparação de agenda. O valor do campo `room` é `Room 2`; neste livro, Sala 2 nomeia esse valor, e Sala 4 nomeará `Room 4`. Não é outra sala.

```csv
booking_id,room,start_time,created_time,status
SYN-001,Room 2,14:00,08:20,confirmed
SYN-002,Room 2,15:00,10:05,confirmed
```

`SYN-` identifica registros inventados. A amostra não contém dados reais de identidade. Um leitor pode perguntar se uma impressão das 09:00 incluiria os dois registros sem acessar um sistema de reservas. Incluiria só o primeiro se a impressão for um instantâneo às 09:00; essa é uma premissa do exercício que deve ser declarada de modo explícito.

### 2.4 Defina condições de parada antes do exercício

Uma **condição de parada** é uma razão observável para pausar o trabalho e pedir orientação. Deve ser escrita antes de a atividade começar, quando todos ainda conseguem pensar com clareza. Exemplos para este exercício em papel: uma pessoa participante abre uma página real de reservas para “conferir” o cenário; uma folha contém o nome real de um frequentador; o exercício começa a interferir no atendimento do balcão; ou um resultado sugere um problema urgente real que precisa do processo de resposta da organização. Em cada caso, pause o treino, proteja o material já coletado e pergunte ao responsável designado o que fazer em seguida.

Parar não é fracasso. É evidência de que a equipe respeitou o próprio limite. Um bom relatório pode dizer: “O exercício parou depois que a equipe notou o nome real de um frequentador na folha de amostra. A folha não foi circulada; o responsável a substituiu por dados sintéticos.” Essa frase documenta o problema e a ação segura sem publicar o nome.

### 2.5 Relate um achado com linguagem calibrada

O objetivo de um relatório de exercício é ajudar o responsável a decidir o que conferir ou mudar. Uma estrutura compacta é:

1. **Objetivo e escopo:** o que o exercício pretendia testar, e o que foi excluído?
2. **Método:** quais entradas sintéticas e quais passos foram usados?
3. **Observação:** o que as pessoas participantes de fato viram ou fizeram?
4. **Interpretação:** que risco ou lacuna de controle pode seguir, e que explicação alternativa permanece?
5. **Recomendação:** o que o responsável pode verificar ou melhorar em seguida?
6. **Limitações:** o que o exercício não estabeleceu?

Para o teste inventado da biblioteca, uma frase justa é: “Num exercício em papel, a equipe que usava um instantâneo das 09:00 não viu uma reserva sintética criada às 10:05. O exercício sugere que uma impressão estática é insuficiente como única fonte para reservas posteriores durante uma interrupção. O exercício não testou o serviço real de reservas nem estabeleceu como um balcão real opera hoje.” A frase é útil porque a observação e o limite estão ambos visíveis.

Evite rótulos dramáticos como “violação crítica” quando nenhuma violação foi observada. Evite uma recomendação vaga como “melhorar a segurança”. Proponha uma decisão que o responsável possa avaliar: definir uma fonte alternativa para reservas posteriores, marcar o horário da impressão e ensaiar o procedimento com uma reserva sintética posterior.

### 2.6 Laboratório: um exercício de mesa limitado

Este laboratório precisa só de um editor de texto ou de papel. Use as duas linhas sintéticas do CSV acima e desenhe uma impressão das 09:00 contendo apenas `SYN-001`. Uma pessoa faz o papel de quem atende no balcão, outra o de morador que pergunta sobre a Sala 2 às 15:00, e outra o de observador. Se estiver sozinho, escreva três linhas curtas para cada papel. O observador pergunta se quem atende conhece o horário da impressão, nota a reserva posterior ausente e evita prometer uma sala sem uma fonte atual.

Faça duas rodadas. Na primeira, não dê a quem atende nenhuma instrução alternativa e registre o que acontece. Na segunda, dê esta regra: “Quando a página de reservas estiver indisponível, marque a idade da impressão e coloque pedidos posteriores não verificados numa fila de pendências até que uma fonte aprovada ou o responsável pelo serviço os confirme.” Registre se a regra mudou a decisão. Não infira que a regra funcionará em todo cenário. O resultado demonstra apenas como este cenário pequeno se comportou sob as premissas declaradas.

Um registro aceitável de laboratório tem a data do exercício fictício, os rótulos dos papéis, os dois identificadores sintéticos de reserva, a decisão em cada rodada e uma frase de limitação. Não há necessidade de criar uma conta ao vivo, enviar uma mensagem ou acessar um sistema externo.

### Resumo do capítulo 2

Um limite autorizado torna um exercício de segurança útil e seguro. Declare, antes de começar, o responsável, os dados e as ações permitidos, os sistemas excluídos, o tempo, as condições de parada e o caminho do relatório. Use registros sintéticos quando eles puderem responder à pergunta de aprendizagem. Relate exatamente o que foi observado e o que permanece desconhecido. O capítulo 3 acrescentará um modelo mais completo de sistemas, fluxos de dados e dependências dentro desse limite.

### Exercícios do capítulo 2

Mantenha toda atividade dentro do limite do exercício sintético em papel. As resoluções aparecem no fim deste livro.

### EX006 — Escreva o escopo

- **Objetivo:** Transformar uma atividade vaga num limite de exercício autorizado.
- **Entrada:** O exercício de mesa da Harbor Library na seção 2.6.
- **Condição segura:** Use só papel ou um editor de texto e registros inventados.
- **Tarefa:** Escreva um briefing de seis linhas nomeando o responsável, os materiais no escopo, os sistemas excluídos, as ações permitidas, a janela de tempo e quem recebe os resultados.
- **Evidência esperada:** Um briefing que outra pessoa possa seguir sem adivinhar o limite.
- *Rubrica:* 3 = os seis elementos e uma exclusão clara de sistemas de produção e de moradores reais;; 2 = cinco elementos, com a exclusão de produção presente;; 1 = o escopo é “testar a biblioteca” ou inclui um sistema real;; 0 = nenhuma.

### EX007 — Minimize os dados

- **Objetivo:** Selecionar só a informação necessária para testar um objetivo de aprendizagem.
- **Entrada:** Uma folha fictícia de rascunho com identificador de reserva, sala, horário de início, horário de criação, nome do morador, número de telefone pessoal e status.
- **Condição segura:** Não use nem invente dados realistas de contato pessoal.
- **Tarefa:** Escolha os campos para o exercício da impressão desatualizada, explique cada escolha e remova os campos desnecessários.
- **Evidência esperada:** Uma lista sintética revista de campos e uma frase por campo mantido.
- *Rubrica:* 3 = mantém a evidência de horário e de sala e exclui nome e telefone;; 2 = exclui o telefone, mas ainda discute o nome sem removê-lo;; 1 = mantém nome ou telefone;; 0 = nenhuma.

### EX008 — Parar ou continuar

- **Objetivo:** Aplicar uma condição de parada escrita de antemão.
- **Entrada:** Na metade do exercício em papel, uma pessoa participante propõe abrir o site real da biblioteca para conferir uma resposta.
- **Condição segura:** Não abra nem teste nenhum serviço real.
- **Tarefa:** Declare se continua, o que registrar, quem decide o passo seguinte e como concluir o objetivo de aprendizagem em segurança.
- **Evidência esperada:** Uma resposta em quatro partes com uma alternativa offline.
- *Rubrica:* 3 = pausa a ação ao vivo proposta, avisa o responsável, preserva o limite do exercício e continua com dados sintéticos se isso for aprovado;; 2 = pausa a ação ao vivo, mas falta a alternativa offline;; 1 = abre ou testa um serviço real;; 0 = nenhuma.

### EX009 — Calibre o relatório

- **Objetivo:** Distinguir uma observação de uma afirmação exagerada.
- **Entrada:** “A impressão antiga não mostrava `SYN-002`; portanto a biblioteca real tem uma violação crítica de segurança.”
- **Condição segura:** Use só o caso fictício fornecido.
- **Tarefa:** Reescreva a frase como observação, interpretação, limitação e próxima verificação.
- **Evidência esperada:** Quatro frases rotuladas.
- *Rubrica:* 3 = conserva a lacuna observada na impressão, remove a alegação de violação não sustentada e propõe uma verificação aprovada pelo responsável;; 2 = a observação está correta e a limitação fica incompleta;; 1 = mantém a alegação de violação crítica;; 0 = nenhuma.

### EX010 — Compare duas rodadas de mesa

- **Objetivo:** Avaliar se um procedimento muda uma decisão num exercício controlado.
- **Entrada:** As duas rodadas da seção 2.6, incluindo a regra da fila de pendências na segunda rodada.
- **Condição segura:** Dramatize sem dados ou comunicação de um serviço real.
- **Tarefa:** Defina uma decisão observável em cada rodada, um critério de melhora e dois limites para generalizar o resultado.
- **Evidência esperada:** Uma tabela curta de comparação e as limitações.
- *Rubrica:* 3 = uma medida observável, uma diferença plausível de decisão e limites sobre dados sintéticos e o escopo de uma sessão;; 2 = compara as rodadas sem um dos limites;; 1 = generaliza o resultado para a operação real;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 20

[← Capítulo 01](#ch-01) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Cibersegurança: sistemas, dados e dependências

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Fixar um limite útil para um modelo pequeno de serviço e nomear as pessoas, os processos, os depósitos e os serviços externos.
2. Rastrear um tipo de informação da criação ao uso, à cópia e ao descarte, sem presumir que toda cópia está atual.
3. Distinguir um fluxo de dados de uma dependência e marcar onde uma mudança de autoridade ou de confiança merece uma pergunta.
4. Declarar quais partes de um diagrama são fatos fornecidos, premissas do exercício ou perguntas sem resposta.
5. Produzir um modelo pequeno e uma lista de lacunas de evidência só a partir de registros sintéticos.

### 3.1 Um modelo responde a uma pergunta; não é o serviço

O primeiro capítulo nomeou o serviço de reserva de salas da Harbor Library. O segundo limitou a prática a registros inventados. Agora podemos fazer uma pergunta mais precisa: **Uma pessoa do balcão conseguiria tomar uma decisão correta sobre a sala enquanto a visão ao vivo das reservas está indisponível?** Um modelo útil contém as partes necessárias para responder a essa pergunta. Não precisa retratar cada dispositivo que a biblioteca possui.

Uma **fronteira de serviço** diz o que o modelo cobre. Nesta aula, inclui o pedido de reserva de um morador, a visão de reserva, um depósito de reservas, uma visão da equipe e a impressão alternativa da equipe. A lista de anúncios de eventos é um conjunto de dados separado; cabe num inventário mais amplo da biblioteca, mas está fora do caminho da decisão de reserva que vamos rastrear. Essa exclusão é deliberada, não uma afirmação de que a lista de contatos não tem necessidades de segurança.

O [CSF 2.0 do NIST](https://doi.org/10.6028/NIST.CSWP.29) coloca, na categoria de gestão de ativos (`ID.AM`), inventários de hardware, software e serviços, representações de fluxos de rede autorizados, serviços de fornecedores, priorização de ativos e tipos de dados designados. O framework descreve resultados; não prescreve o diagrama deste curso nem prova que a Harbor Library tenha qualquer implementação particular. Uma organização confirmaria o modelo com responsáveis e registros aprovados. O exercício de iniciante usa premissas declaradas para que o raciocínio possa ser conferido sem descoberta ao vivo.

A [folha de consulta de modelagem de ameaças da OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) recomenda mostrar entidades externas, processos, depósitos de dados, fluxos e fronteiras de confiança ao modelar um sistema. Tomamos esses rótulos simples emprestados para entender o serviço. A ordenação de ameaças e o teste de aplicação ficam mais adiante no percurso de aprendizagem. Por agora, o trabalho é entender que informação se move, quem depende dela e onde o nosso conhecimento termina.

### 3.2 Nomeie as partes e os responsáveis

Uma **entidade externa** é uma pessoa ou um sistema fora do processo modelado que interage com ele. Um **processo** aceita informação e executa uma tarefa. Um **depósito de dados** retém informação. Um **fluxo de dados** é o movimento entre eles. Esses rótulos descrevem papéis num modelo, não uma arquitetura de produto verificada. Uma aplicação real poderia combinar vários papéis; um papel poderia estar espalhado por vários serviços.

| Parte modelada | Papel na aula | Quem confirmaria isso numa revisão real? | Evidência atual |
|---|---|---|---|
| Morador | Pede uma sala e recebe uma decisão | Responsável pelo serviço e responsável pelo processo voltado ao usuário | Descrição do caso fictício |
| Visão de reserva | Recebe um pedido e mostra informação de reserva | Responsável pela aplicação | Premissa de ensino; nenhum software foi examinado |
| Depósito de reservas | Guarda o estado atual da reserva para o exercício | Responsável pela aplicação ou pelos dados | Só linhas sintéticas de reserva |
| Visão da equipe | Permite que a equipe autorizada consulte a agenda | Responsável pelo serviço e liderança da equipe | Premissa de ensino |
| Agenda impressa | Instantâneo usado durante a interrupção do exercício de mesa | Liderança do balcão | Impressão inventada das 09:00 no capítulo 2 |
| Contatos de eventos | Informação separada, usada para anúncios | Responsável pelos dados | Descrição fictícia do serviço; fora deste fluxo |

A coluna “responsável” é um caminho de verificação, não uma afirmação de que uma única pessoa nomeada detém toda responsabilidade. Se a visão da equipe na verdade lê de outro depósito, o modelo tem de mudar. Se a impressão em papel é produzida a cada hora, e não uma vez por manhã, o risco de desatualização também muda. Um diagrama deve ser revisto quando a evidência discorda dele.

### 3.3 Siga a informação, inclusive as cópias

Comece pelos dados necessários para a decisão. No nosso exercício sintético, uma reserva tem um identificador inventado, sala, horário de início, horário de criação e status. Uma reserva confirmada está representada no depósito de reservas. Uma visão da equipe pode exibir esse estado. Uma impressão contém um **instantâneo** feito num horário determinado; não recebe automaticamente mudanças posteriores. Esta é uma propriedade temporal da cópia em papel, não uma vulnerabilidade de software.

Rastreie cada representação de modo explícito:

| Representação | Por que existe | Quando está atual para este exercício | Pergunta antes de confiar nela |
|---|---|---|---|
| Linha sintética de reserva | Descreve uma reserva para a aula | No `created_time` declarado | O status está confirmado ou apenas pedido? |
| Visão da agenda da equipe | Apoiaria uma decisão de sala ao vivo | Desconhecido enquanto o exercício diz que a visão está indisponível | Que fonte a alimenta, e quando essa fonte foi atualizada? |
| Agenda impressa das 09:00 | Fornece uma referência offline | Contém as reservas conhecidas às 09:00 sob a premissa declarada de instantâneo | Reservas posteriores foram acrescentadas, alteradas ou canceladas? |
| Fila de pedidos pendentes | Registra uma decisão não verificada durante o exercício | Tão atual quanto as anotações de quem trabalha, mas **não** é confirmação autoritativa de reserva | Quem a reconcilia depois que o serviço volta? |

A lista de contatos de eventos tem um propósito diferente da lista de reservas. Não presuma que uma pessoa que pode ver uma reserva de sala também pode exportar contatos de eventos. Do mesmo modo, uma cópia de segurança é um recurso potencial de recuperação, não automaticamente uma visão atual de reservas. Num inventário real, um responsável deveria identificar tipos de dados, locais, finalidade, acesso e regras de retenção e descarte segundo as políticas da organização. Neste exercício, registramos só os campos necessários para a pergunta de ensino e não inventamos identificadores pessoais.

A distinção entre **fonte de verdade** e **cópia** ajuda a evitar um erro fácil. Um registro autoritativo atual é aquele que o responsável pelo serviço designa para uma decisão particular, sujeito à integridade e à disponibilidade reais. Uma cópia impressa ainda pode ser útil durante uma interrupção, mas o carimbo de tempo limita o que ela pode estabelecer. “A impressão existe” não implica “a impressão reflete todas as reservas.” “Um trabalho de cópia de segurança terminou” não implica “a equipe pode usar a cópia de segurança com segurança como agenda ao vivo.” Cada afirmação precisa de evidência separada.

### 3.4 Desenhe um fluxo e marque as fronteiras

O que segue é uma **alternativa em texto** a um diagrama. É pequeno de propósito. As setas indicam movimento proposto de informação, e os colchetes nomeiam papéis. Elas não afirmam que uma aplicação real da Harbor Library tenha esta arquitetura.

```text
[Morador] --pedido de reserva--> [Visão de reserva] --escrita proposta--> [Depósito de reservas]
     ^                              |                                      |
     |                         resultado da reserva                  leitura proposta
     +------------------------------+                                      |
                                                                           v
[Membro da equipe] --acesso e consulta--> [Visão da equipe] <--------------+
                                                |
                                           instantâneo das 09:00
                                                v
                                       [Agenda impressa]
```

A primeira seta cruza uma fronteira entre um morador e um serviço que decide se um pedido é válido. O acesso e a consulta da equipe cruzam uma fronteira diferente, porque quem trabalha pode ter autoridade para ver ou alterar informação que um morador não pode. A agenda impressa sai de um processo digital e vira uma cópia física; o manuseio e a atualidade precisam de procedimentos humanos. Uma **fronteira de confiança** marca uma mudança de premissas ou de autoridade que deve ser examinada. Não é, por si, evidência de que autenticação, autorização, cifragem ou registro de eventos está presente ou ausente.

Para cada seta, faça três perguntas de iniciante: **O que se move? Quem pode causar ou ler esse movimento? Que evidência mostraria que a regra pretendida é seguida?** Para o pedido do morador, as respostas poderiam ser “sala e horário”, “um morador pode pedir uma sala disponível” e “um teste aprovado pelo responsável com reservas sintéticas, mais uma especificação de aplicação revisada”. São verificações possíveis, não fatos estabelecidos pelo nosso exercício em papel. Não use este diagrama como permissão para enviar pedidos de teste a um site público.

Se um serviço de mensagens de terceiro envia confirmações, acrescente-o como serviço externo só depois de confirmar que ele é de fato usado. Então pergunte que dados ele recebe, pelo que o fornecedor é responsável e se o serviço ainda consegue decidir uma reserva se a mensagem atrasar. Este é um exemplo de **dependência condicional**: a resposta pode diferir entre “uma reserva pode ser gravada” e “um morador recebe a confirmação”. Manter esses resultados separados evita tratar toda interrupção de fornecedor como uma interrupção completa das reservas.

### 3.5 Dependências mudam com o resultado

Uma dependência é necessária para um resultado particular sob condições particulares. No caminho ao vivo proposto, a visão de reserva pode depender de um depósito de reservas. Durante a interrupção do exercício de mesa, a equipe pode, em vez disso, depender da última fonte alternativa aprovada e de uma regra para pedidos pendentes. Um componente pode ser importante sem ser o único modo de continuar funcionando. Não chame o depósito de reservas de “ponto único de falha” a menos que o responsável tenha confirmado que não há alternativa adequada e tenha definido o que falha significa.

Para revisar uma dependência, escreva uma frase condicional: “Se **X** está indisponível, **Y** não pode ser concluído dentro do tempo **Z** usando a alternativa aprovada.” O caso fictício não fornece uma meta de recuperação `Z`, então deixe isso como pergunta para o responsável pelo serviço. Separe os efeitos sobre moradores, equipe e assinantes de eventos. Uma interrupção da visão do balcão não prova que a página de um morador está fora do ar; o registro do capítulo 1 limitou de modo específico a interrupção observada ao balcão.

O modelo de serviço também precisa de uma regra de atualização. Uma mudança no fluxo de reserva, na agenda de impressão ou na fonte aprovada pode invalidar esta página. Uma entrada pequena de inventário deve, portanto, registrar a data do modelo, o autor ou o responsável, o escopo, a evidência, as perguntas abertas e o gatilho de revisão. Um diagrama arrumado sem data de revisão pode enganar um leitor mais do que um diagrama tosco com rótulos claros de incerteza.

### 3.6 Laboratório guiado: uma decisão a partir de um instantâneo desatualizado

Use as linhas **sintéticas** introduzidas no capítulo 2:

```csv
booking_id,room,start_time,created_time,status
SYN-001,Room 2,14:00,08:20,confirmed
SYN-002,Room 2,15:00,10:05,confirmed
```

Só neste laboratório, presuma que uma impressão das 09:00 é um instantâneo fixo, inclui `SYN-001` e não pode incluir `SYN-002`, porque essa reserva foi criada às 10:05. A visão do balcão está indisponível das 11:30 às 11:50. Às 11:42 alguém pergunta se a Sala 2 está livre às 15:00. Nenhuma rede e nenhum dado real são usados.

1. Copie as seis partes modeladas da seção 3.2 para o papel ou para uma tabela Markdown. Circule a agenda impressa como uma cópia.
2. Rastreie `SYN-002` da criação às 10:05 até o depósito de reservas no modelo *hipotético*. Desenhe um ponto de interrogação em qualquer passo não verificado, inclusive se a visão da equipe normalmente o mostraria.
3. Compare o horário da consulta, o horário da impressão e o horário da reserva. A impressão não pode responder à pergunta de disponibilidade das 15:00 sob a premissa declarada de instantâneo. Não transforme essa conclusão numa afirmação sobre um serviço real.
4. Use a regra alternativa do capítulo 2: marque o pedido como **pendente**, registre o motivo e busque uma fonte atual aprovada ou o responsável. Não prometa a sala só com o papel antigo.
5. Escreva um relatório de três linhas: fato observado no exercício, decisão e limitação. Uma resposta modelo é: “A impressão sintética das 09:00 omitiu uma reserva criada às 10:05. No exercício de mesa, quem atendia marcou o pedido das 15:00 como pendente em vez de confirmá-lo. O exercício não inspecionou um depósito real de reservas nem estabeleceu como a biblioteca real trata interrupções.”

O artefato esperado é um modelo pequeno mais este relatório. O resultado não é “descobrimos uma violação”. O resultado é uma decisão defensável diante de informação limitada. Se o responsável mais tarde fornecer uma agenda de papel horária verificada ou uma réplica offline aprovada, repita a análise com essa evidência; não preserve a conclusão original só porque ela apareceu num diagrama.

### 3.7 Um registro de modelo revisável

Use este modelo Markdown para um modelo de serviço. Ele é curto de propósito, para que outra pessoa possa contestá-lo:

```text
Decisão que o modelo apoia:
Serviço e pessoas afetadas:
Dentro do escopo / fora do escopo:
Entidades, processos e depósitos:
Tipos de dados e seus propósitos:
Fluxos e fronteiras:
Dependências e premissas da alternativa:
Fatos fornecidos:
Premissas do exercício:
Perguntas abertas e a quem perguntar:
Última revisão / gatilho de atualização:
```

Na Harbor Library, “reserva criada às 10:05” é um fato sintético fornecido; “a agenda impressa é um instantâneo fixo das 09:00” é uma premissa do exercício; “que fonte a equipe pode usar durante uma interrupção real” é uma pergunta aberta. Essas categorias devem permanecer visíveis no artefato final. Quem escreve “o sistema não tem recuperação” porque este capítulo não mencionou uma confundiu **evidência ausente** com **evidência de ausência**.

Erros comuns incluem desenhar uma arquitetura detalhada a partir de uma narrativa curta, tratar cada linha como uma conexão de rede verificada, omitir cópias físicas, confundir uma dependência com uma falha e deixar um modelo inalterado depois que informação nova chega. O remédio é modesto: mantenha o modelo ligado a uma decisão, rotule a incerteza, pergunte ao responsável e revise o registro quando um fato muda. O capítulo 4 usará este modelo limitado para discutir ameaças plausíveis e modos comuns de falha sem afirmar que qualquer um deles ocorreu.

### Resumo do capítulo 3

Modele as pessoas, os processos, os depósitos e a informação necessários para uma decisão definida de serviço. Trate as cópias de dados e os seus carimbos de tempo de modo explícito. Um fluxo mostra movimento proposto; uma fronteira de confiança provoca uma pergunta sobre autoridade; uma dependência só importa em relação a um resultado declarado. Marque fatos fornecidos, premissas e perguntas sem resposta para que o modelo continue útil quando a evidência mudar.

### Exercícios do capítulo 3

Use o modelo e os registros inventados acima; não teste um serviço ao vivo. As resoluções aparecem no apêndice final.

### EX011 — Fronteira e componentes

- **Objetivo:** Definir um modelo de serviço que responda a uma pergunta específica sem inventar detalhes de implementação.
- **Entrada:** A pergunta de decisão na seção 3.1 e as seis partes modeladas na seção 3.2.
- **Condição segura:** Use só o caso fictício; não inspecione um serviço real de biblioteca.
- **Passos:** (1) Escreva a pergunta de decisão. (2) Nomeie quatro partes necessárias para respondê-la e classifique cada uma como entidade, processo, depósito ou cópia. (3) Nomeie um conjunto de dados relacionado que esteja fora deste caminho de decisão e explique por quê. (4) Marque uma premissa arquitetural não verificada.
- **Evidência esperada:** Uma declaração de escopo e uma tabela de componentes com quatro linhas e uma pergunta aberta.
- *Rubrica:* 3 = pergunta limitada à decisão de reserva, papéis adequados, exclusão fundamentada dos contatos de eventos e um rótulo visível de incerteza;; 2 = a pergunta e os papéis estão certos, mas a exclusão ou a incerteza fica implícita;; 1 = um diagrama de rede muito detalhado e sem sustentação não atende ao objetivo;; 0 = nenhuma.

### EX012 — Rastreie o instantâneo

- **Objetivo:** Distinguir o horário de uma cópia de dados do horário de uma mudança posterior.
- **Entrada:** As duas linhas CSV da seção 3.6, uma impressão fixa das 09:00 e a pergunta sobre a sala às 11:42.
- **Condição segura:** Trabalhe só com estes horários e identificadores inventados.
- **Passos:** (1) Ponha os quatro horários relevantes em ordem. (2) Liste quais identificadores de reserva a impressão pode incluir sob a premissa de instantâneo. (3) Declare o que a impressão não pode estabelecer às 11:42. (4) Registre a próxima ação defensável de quem atende.
- **Evidência esperada:** Uma linha do tempo curta e uma nota de decisão com a premissa.
- *Rubrica:* 3 = `SYN-001` na impressão, `SYN-002` ausente, premissa explícita de instantâneo e decisão pendente ou confirmada pelo responsável, em vez de uma promessa sem apoio;; 2 = os identificadores estão certos, mas a premissa de instantâneo fica implícita;; 1 = promete a sala a partir da impressão das 09:00;; 0 = nenhuma.

### EX013 — Fluxo versus dependência

- **Objetivo:** Separar o movimento de informação de uma condição exigida para um resultado.
- **Entrada:** O diagrama em texto da seção 3.4 e os dois resultados “gravar uma reserva” e “enviar uma confirmação”.
- **Condição segura:** Trate o fornecedor opcional de mensagens como hipotético; não contate um fornecedor nem envie mensagens.
- **Passos:** (1) Nomeie dois fluxos mostrados no diagrama. (2) Escreva uma dependência condicional para cada resultado. (3) Explique se um atraso de mensagem prova, necessariamente, que a reserva não foi gravada. (4) Nomeie o fato que um responsável precisa confirmar.
- **Evidência esperada:** Dois fluxos rotulados, duas frases condicionais e uma pergunta de verificação.
- *Rubrica:* 3 = distingue um caminho de dados proposto de uma condição exigida pelo serviço e não afirma o fornecedor ou a implementação não confirmados;; 2 = os fluxos estão certos, mas a frase condicional falta;; 1 = afirma uma implementação ou um fornecedor não observado;; 0 = nenhuma.

### EX014 — Perguntas de fronteira

- **Objetivo:** Usar uma fronteira de confiança como convite à verificação, e não como prova de um controle.
- **Entrada:** As setas de morador para visão de reserva e de equipe para visão da equipe na seção 3.4.
- **Condição segura:** Isto é uma revisão em papel; não teste contas nem envie pedidos a um serviço ao vivo.
- **Passos:** Para cada seta, escreva (1) que informação ou ação a cruza, (2) quem deveria ter permissão para iniciá-la no cenário fictício, (3) uma pergunta de controle para o responsável e (4) um tipo de evidência autorizada que poderia responder a essa pergunta.
- **Evidência esperada:** Uma tabela de duas linhas que separa a permissão esperada da prova observada.
- *Rubrica:* 3 = autoridade distinta de morador e de equipe, perguntas específicas ao responsável e a afirmação de que o diagrama sozinho não verifica implementação alguma;; 2 = as duas fronteiras aparecem, mas a pergunta ao responsável fica genérica;; 1 = trata a seta como prova de que um controle existe;; 0 = nenhuma.

### EX015 — Revise quando um fato muda

- **Objetivo:** Atualizar um modelo sem se agarrar a uma conclusão anterior.
- **Entrada:** Um *novo relato fictício do responsável* diz que o balcão recebe uma agenda offline aprovada, atualizada às 11:40 e contendo `SYN-002`. A exatidão ainda não foi testada.
- **Condição segura:** Não busque nem copie reservas reais; raciocine a partir deste relato inventado adicional.
- **Passos:** (1) Identifique qual conclusão anterior fica enfraquecida. (2) Acrescente a agenda offline relatada como uma representação separada. (3) Especifique uma verificação sintética segura do carimbo de tempo e do conteúdo. (4) Declare a decisão se a verificação passar e se falhar, e anote uma limitação que permanece.
- **Evidência esperada:** Uma nota de modelo revista, com relato, teste, decisões de cada ramo e limitação.
- *Rubrica:* 3 = trata a informação nova como relato, não como fato observado de modo independente; muda de modo condicional a conclusão de que só existe o papel das 09:00; mantém a decisão de quem atende dentro da regra alternativa aprovada;; 2 = separa o relato do fato, mas a decisão condicional fica incompleta;; 1 = trata o relato das 11:40 como fato já verificado ou defende o diagrama antigo;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 20

[← Capítulo 02](#ch-02) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Cibersegurança: laboratório guiado e síntese aplicada

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Aplicar uma regra escrita a uma ação sintética da equipe e nomear o veredito que a regra produz.
2. Separar a classificação de uma proposta registrada de uma decisão de que o serviço real é seguro.
3. Explicar por que ALLOW, REFUSE, OUT OF SCOPE e STOP respondem a perguntas diferentes.
4. Declarar um fato que o programa offline não pode saber.
5. Escrever um dossiê curto que mantenha a observação, a decisão e o limite em frases separadas.

### 4.1 Cinco rótulos, quatro ações registradas

Os capítulos 1–3 deixaram uma pessoa do balcão com uma agenda de papel das 09:00, duas reservas inventadas e uma regra: não confirmar uma sala posterior a partir desse papel, não abrir um site ao vivo e não puxar a lista de contatos de eventos para dentro do exercício de reserva. O capítulo 4 transforma essa regra numa verificação que uma segunda pessoa pode executar de novo.

A verificação tem cinco rótulos possíveis. Quatro aparecem no registro das quatro ações; `UNKNOWN` permanece com contagem zero. São rótulos deste exercício, não uma escala de severidade.

| Veredito | Pergunta que responde | O que não responde |
|---|---|---|
| STOP | Esta ação saiu do exercício em papel? | Se um site real está sob ataque |
| OUT OF SCOPE | Este conjunto de dados está fora da decisão de reserva? | Se a lista de contatos está bem protegida |
| REFUSE | O instantâneo das 09:00 omite uma reserva posterior para essa sala e esse início? | Por que a página de reservas estava indisponível |
| ALLOW | A regra escrita permite esta ação registrada? | Se a Sala 2 está de fato livre |
| UNKNOWN | A ação está ausente do conjunto de regras? | O que o responsável decidiria depois de ser perguntado |

Um número como 7.4 esconderia qual destas perguntas mudou. Este capítulo não atribui nota à biblioteca.

### 4.2 O programa lê a premissa do exercício

O laboratório abaixo é Python da biblioteca padrão. Ele codifica três premissas já fixadas neste livro: o horário da impressão é 09:00, `SYN-002` foi criada às 10:05 para a Sala 2 às 15:00, e os contatos de eventos estão fora do caminho da reserva. Ele não lê o *relato* do responsável, no capítulo 3, de uma folha offline das 11:40. Esse relato continua não verificado, então o programa não deve tratá-lo como uma impressão mais nova.

`REFUSE` só dispara quando uma ação de confirmar pela impressão nomeia uma sala e um início cuja reserva foi criada depois das 09:00. `ALLOW` em marcar pendente significa que a regra aceita uma fila de pendências. `ALLOW` numa confirmação significa apenas que nenhuma reserva posterior nesta tabela minúscula corresponde àquela sala e àquele início. Uma sala diferente pode, portanto, imprimir ALLOW e continuar desconhecida no prédio real.

### 4.3 Exemplo resolvido: quatro ações

Use as mesmas linhas que o programa usa.

| Horário | Ação | Por que a regra fala | Veredito |
|---|---|---|---|
| 11:42 | Confirmar a Sala 2 às 15:00 pelo papel | `SYN-002` foi criada às 10:05, depois da impressão | REFUSE |
| 11:43 | Exportar contatos de eventos | Contatos de anúncio não são a decisão de reserva | OUT OF SCOPE |
| 11:44 | Abrir o site ao vivo de reservas | O briefing proíbe sistemas de produção | STOP |
| 11:45 | Marcar o pedido das 15:00 como pendente | A regra alternativa permite uma fila de pendências | ALLOW |

A linha das 11:44 classifica uma *proposta registrada*. Por si, ela não interrompe uma sala de aula. Num ensaio ao vivo, o responsável ainda pausa as pessoas, como o capítulo 2 exigiu. O programa segue para que as outras três linhas continuem visíveis. Essa diferença é um limite do programa, não uma condição de parada mais branda.

### 4.4 Laboratório: classifique o registro sintético

Salve este programa como `lab_dossier.py` e execute-o com `python3 lab_dossier.py`. Não o aponte para uma rede, para o site de uma biblioteca ou para um arquivo de frequentadores reais. A saída esperada é fixa para estas linhas. Se a sua saída diferir, a regra que você executou não é a regra deste capítulo.

```python
"""Harbor Library tabletop dossier. Synthetic records only."""

PRINTOUT = "09:00"

BOOKINGS = [
    {"id": "SYN-001", "room": "Room 2", "start": "14:00", "created": "08:20", "status": "confirmed"},
    {"id": "SYN-002", "room": "Room 2", "start": "15:00", "created": "10:05", "status": "confirmed"},
]

ACTIONS = [
    {"time": "11:42", "action": "confirm-from-printout", "room": "Room 2", "start": "15:00"},
    {"time": "11:43", "action": "export-contacts"},
    {"time": "11:44", "action": "open-live-site"},
    {"time": "11:45", "action": "mark-pending", "room": "Room 2", "start": "15:00"},
]


def minutes(clock):
    hour, minute = clock.split(":")
    return int(hour) * 60 + int(minute)


def decide(action):
    kind = action["action"]
    if kind == "open-live-site":
        return "STOP", "live site is outside the paper exercise"
    if kind == "export-contacts":
        return "OUT OF SCOPE", "event contacts are outside the booking decision"
    if kind == "confirm-from-printout":
        later = [
            booking["id"]
            for booking in BOOKINGS
            if booking["room"] == action["room"]
            and booking["start"] == action["start"]
            and minutes(booking["created"]) > minutes(PRINTOUT)
        ]
        if later:
            return "REFUSE", "printout 09:00 omits " + ",".join(later)
        return "ALLOW", "no later booking is recorded for that room and start"
    if kind == "mark-pending":
        return "ALLOW", "pending until an approved current source"
    return "UNKNOWN", "the written rule set does not name this action"


def main():
    print("printout: 09:00; bookings: 2")
    omitted = [booking["id"] for booking in BOOKINGS if minutes(booking["created"]) > minutes(PRINTOUT)]
    print("omitted by printout: " + ",".join(omitted))
    counts = {"STOP": 0, "OUT OF SCOPE": 0, "REFUSE": 0, "ALLOW": 0, "UNKNOWN": 0}
    for action in ACTIONS:
        verdict, reason = decide(action)
        counts[verdict] += 1
        print(f"{action['time']} {action['action']}: {verdict}; {reason}")
    print(
        "STOP {STOP}; OUT OF SCOPE {OUT OF SCOPE}; REFUSE {REFUSE}; ALLOW {ALLOW}; UNKNOWN {UNKNOWN}".format(
            **counts
        )
    )


if __name__ == "__main__":
    main()
```

Saída exata, conferida com Python 3:

```text
printout: 09:00; bookings: 2
omitted by printout: SYN-002
11:42 confirm-from-printout: REFUSE; printout 09:00 omits SYN-002
11:43 export-contacts: OUT OF SCOPE; event contacts are outside the booking decision
11:44 open-live-site: STOP; live site is outside the paper exercise
11:45 mark-pending: ALLOW; pending until an approved current source
STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0
```

A linha de contagem é uma contagem destas quatro linhas. Não é uma classificação de risco. Mudar a sala das 11:42 para a Sala 4, que não aparece em `BOOKINGS`, faz essa linha imprimir ALLOW. O novo ALLOW significa que a tabela não tem reserva posterior para a Sala 4 às 15:00. Não significa que um morador pode ficar com a sala.

### 4.5 Um dossiê usa só o que a execução mostrou

Escreva seis frases curtas e pare. A frase 1 nomeia o exercício e a premissa das 09:00. A frase 2 cita uma linha da saída. A frase 3 declara a decisão que essa linha sustenta. A frase 4 nomeia um veredito que não deve ser fundido com ela: exportar contatos é OUT OF SCOPE, não REFUSE, porque a lista de contatos nunca foi uma comparação de horário de reserva. A frase 5 diz que o programa não inspecionou um depósito de reservas e não aceitou o relato não verificado das 11:40. A frase 6 nomeia a pergunta ao responsável que continua aberta: qual fonte aprovada, se alguma, pode substituir o papel das 09:00.

Se a frase 5 estiver em branco, a nota não está pronta para orientar uma mudança de procedimento. Um limite em branco permite que um leitor trate uma contagem de sala de aula como um achado sobre os sistemas reais da Harbor Library, que este livro não tem.

### Resumo do capítulo 4

Uma regra escrita pode classificar uma ação sintética do mesmo modo duas vezes. STOP, OUT OF SCOPE, REFUSE, ALLOW e UNKNOWN respondem a perguntas diferentes. O ALLOW do programa é permissão sob as linhas que lhe foram dadas, não evidência de que uma sala está livre ou de que uma folha relatada das 11:40 existe. O dossiê mantém separados a saída, a decisão e o limite.

### Exercícios do capítulo 4

Use o programa e a saída da seção 4.4. Não contate uma biblioteca real. As resoluções estão no apêndice.

### EX016 — Leia a contagem

- **Objetivo:** Ligar um veredito à linha que o produziu.
- **Entrada:** A saída exata do laboratório na seção 4.4.
- **Condição segura:** Não acrescente reservas nem abra um site.
- **Tarefa:** Nomeie a ação que recebeu REFUSE, o identificador de reserva que o motivo cita e a premissa que torna esse identificador ausente do papel.
- **Evidência esperada:** Três itens, cada um tirado da saída ou do instantâneo declarado das 09:00.
- *Rubrica:* 3 = a ação é a confirmação das 11:42, o identificador é `SYN-002` e a premissa é a impressão das 09:00, não um ataque inferido;; 2 = dois dos três itens, sem inferir ataque;; 1 = atribui a lacuna a um ataque;; 0 = nenhuma.

### EX017 — ALLOW não é disponibilidade

- **Objetivo:** Limitar o que uma regra de correspondência pode significar.
- **Entrada:** Mude só a ação das 11:42 para que a sala seja a Sala 4 e o início continue 15:00. Deixe todas as outras linhas como impressas.
- **Condição segura:** Edite a tabela sintética no papel ou numa cópia local. Não consulte um sistema ao vivo.
- **Tarefa:** Declare o novo veredito das 11:42 e escreva a frase que um membro da equipe não deve dizer a um morador.
- **Evidência esperada:** O veredito mais uma afirmação proibida.
- *Rubrica:* 3 = ALLOW junto com a recusa de prometer a Sala 4;; 2 = ALLOW, mas a frase proibida fica incompleta;; 1 = chama a sala de livre e, com isso, falha;; 0 = nenhuma.

### EX018 — Não funda os vereditos

- **Objetivo:** Manter um limite de conjunto de dados distinto de uma comparação com papel desatualizado.
- **Entrada:** A linha de saída das 11:43.
- **Condição segura:** Raciocine só a partir dessa linha.
- **Tarefa:** Explique por que a exportação é OUT OF SCOPE e não REFUSE, e nomeie um fato sobre a proteção da lista de contatos que esta execução não fornece.
- **Evidência esperada:** Uma distinção e uma incógnita explícita.
- *Rubrica:* 3 = REFUSE permanece ligado à comparação com a impressão e a lista de contatos continua não medida;; 2 = a distinção está certa, mas a incógnita fica vaga;; 1 = redescreve a exportação como REFUSE;; 0 = nenhuma.

### EX019 — Parada do programa versus parada humana

- **Objetivo:** Notar que uma linha classificada não é o mesmo ato que pausar pessoas.
- **Entrada:** A linha STOP das 11:44 e a regra do capítulo 2 de que uma proposta de site ao vivo pausa o exercício.
- **Condição segura:** Não abra um site para ilustrar o ponto.
- **Tarefa:** Diga o que o programa fez depois de imprimir STOP, o que um facilitador deve fazer com as pessoas participantes e por que essas duas ações diferem.
- **Evidência esperada:** Três frases.
- *Rubrica:* 3 = o programa continua até as 11:45, o facilitador pausa as pessoas e pergunta ao responsável;; 2 = separa programa e pessoas, mas omite a pergunta ao responsável;; 1 = trata o STOP impresso como se já tivesse pausado as pessoas, ou abre um site;; 0 = nenhuma.

### EX020 — Dossiê de seis frases

- **Objetivo:** Relatar a execução sem ampliá-la.
- **Entrada:** A seção 4.5 e a saída do laboratório.
- **Condição segura:** Não invente causa da interrupção, frequentador nem segundo sistema.
- **Tarefa:** Escreva as seis frases. Deixe a frase 5 concreta. Não atribua uma nota numérica.
- **Evidência esperada:** Seis frases que um colega possa conferir contra a saída.
- *Rubrica:* 3 = cada frase permanece dentro da execução, a linha das 11:43 não é redescrita como REFUSE e o relato das 11:40 continua não verificado;; 2 = cinco frases dentro da execução, sem nota numérica;; 1 = atribui nota numérica, causa da interrupção ou trata as 11:43 como REFUSE;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 20

[← Capítulo 03](#ch-03) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — O que se pode dizer sobre uma reserva

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Separar um fato de reserva de que quem pergunta precisa de um fato sobre outra pessoa.
2. Explicar por que uma frase verdadeira ainda pode ser a coisa errada a dizer.
3. Escolher uma resposta que atenda à pergunta operacional sem nomear um morador.

### 5.1 Confidencialidade é sobre divulgação, não sobre segredo da sala

Confidencialidade, no sentido comum de segurança usado no capítulo 1, significa que a informação não é divulgada a alguém que não deveria recebê-la. O número da sala na porta da biblioteca não é confidencial. O nome da pessoa que a reservou pode ser, porque a reserva liga uma pessoa a um lugar e a um horário. O exercício da Harbor Library não tem um estatuto de privacidade para aplicar e não tem frequentadores reais. O limite ainda importa: uma prática que trata todo fato verdadeiro como dizível treinará o hábito errado.

Um morador no balcão pergunta: “Quem está com a Sala 2 às 14:00?” Quem atende pode ver, na tabela sintética, que `SYN-001` é uma reserva confirmada da Sala 2 às 14:00. A tabela deste livro nem sequer contém o nome de um morador. Inventar um para ser prestativo criaria dado pessoal que o exercício removeu de propósito no capítulo 2.

### 5.2 Exemplo resolvido

A pergunta operacional escondida dentro da pergunta falada costuma ser “Posso usar a Sala 2 às 14:00?” Essa pergunta pode ser respondida a partir do estado da reserva.

| Palavras de quem pergunta | Fato que quem atende tem | Resposta que permanece no exercício | Resposta que sai dele |
|---|---|---|---|
| Quem está com a Sala 2 às 14:00? | `SYN-001` confirmada, nenhum nome armazenado | “Esse horário já está reservado. Não posso usar esta folha para dizer quem.” | Um nome inventado, ou um palpite a partir da lista de eventos |
| A Sala 2 está livre às 15:00? | `SYN-002` confirmada depois das 09:00 | “O registro atual do exercício mostra 15:00 como reservado. Não vou confirmar uma mudança a partir do papel das 09:00.” | “Está livre”, porque o papel omitiu `SYN-002` |

A segunda linha reutiliza a regra do papel desatualizado do capítulo 4. O ponto novo é a primeira linha: mesmo um registro atual não autoriza nomear uma pessoa que não está no registro.

### 5.3 O que este capítulo não decide

Ele não decide que toda biblioteca deve esconder nomes de reserva, nem que um nome é sempre sensível. Uma biblioteca poderia ter um programa público afixado que lista o nome de quem fala porque essa pessoa concordou em ser listada. O exercício de reserva da Harbor Library não tem esse acordo e não tem campo de nome. Quem da equipe precisa de um nome por uma razão de segurança pergunta ao responsável e registra o porquê. Não empresta um nome dos contatos de anúncio, que o capítulo 3 deixou fora do caminho da reserva.

### Resumo do capítulo 5

Um estado verdadeiro de reserva pode ser compartilhado quando responde à pergunta da própria pessoa. A identidade de uma pessoa é uma divulgação diferente. Este exercício não tem nomes para dar, e inventar um não é atendimento.

### Exercícios do capítulo 5

### EX021 — Responda à pessoa à sua frente

- **Objetivo:** Recusar uma divulgação desnecessária sem esconder o estado da sala.
- **Entrada:** Um morador pergunta quem reservou a Sala 2 às 14:00. A linha sintética é `SYN-001`, confirmada, sem nome.
- **Condição segura:** Não invente um morador e não abra um site ao vivo.
- **Tarefa:** Escreva a resposta que você diria e nomeie o fato que você deixa de fora de propósito.
- **Evidência esperada:** Uma resposta falada e um item retido.
- *Rubrica:* 3 = o horário é descrito como reservado e nenhuma pessoa é nomeada ou inventada;; 2 = diz que está reservado, mas não nomeia o item retido;; 1 = nomeia ou inventa uma pessoa;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 20

[← Capítulo 04](#ch-04) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Uma alteração manuscrita não é uma correção

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Distinguir uma atualização autorizada de uma agenda de um acréscimo manuscrito.
2. Explicar por que fazer o papel coincidir com a resposta desejada danifica o registro.
3. Declarar que evidência seria exigida antes que uma cópia posterior pudesse substituir o papel das 09:00.

### 6.1 Integridade é sobre o registro, não sobre o desejo

Integridade significa que a informação permanece correta e só é alterada de um modo autorizado. O capítulo 3 já avisou que uma segunda cópia pode estar desatualizada. Este capítulo olha para uma falha diferente: alguém que quer ajudar escreve `SYN-002` na folha das 09:00 para que uma confirmação deixe de parecer recusada. A reserva pode existir de verdade na tabela sintética. A escrita ainda muda o artefato que deveria ser o instantâneo das 09:00.

Depois dessa marca de caneta, um colega já não consegue ver o que o papel dizia às 09:00. O laboratório do capítulo 4 também mudaria se alguém editasse `PRINTOUT` ou o horário da reserva para o programa imprimir ALLOW. Os dois movimentos ajustam o registro ao veredito preferido. Nenhum dos dois é uma verificação.

### 6.2 Exemplo resolvido

| Ação | O que é preservado | Veredito para este exercício |
|---|---|---|
| Deixar a folha das 09:00 sem marcas e marcar o pedido das 15:00 como pendente | O instantâneo e a reserva posterior permanecem distintos | Coerente com o capítulo 4 |
| Pedir ao responsável a folha relatada das 11:40 e conferir o horário e a presença de `SYN-002` | A cópia nova continua apenas relatada até a verificação passar | A condição do capítulo 3 |
| Escrever `SYN-002` na folha das 09:00 a lápis | O instantâneo original desapareceu | Não é uma correção |

A terceira linha é a aula. A boa intenção não restaura a integridade. Se o responsável mais tarde produzir uma cópia real das 11:40, a folha a lápis não pode servir como essa cópia, porque o horário e o autor já não são confiáveis.

### 6.3 Um limite

Este capítulo não afirma que a Harbor Library proíbe todas as agendas manuscritas. Um formulário offline desenhado, com horário, autor e uma verificação, pode ser uma cópia autorizada. Uma marca anônima a lápis na impressão de ontem não é esse formulário. O exercício também não mostra que alguém na Harbor Library fez isso. É um erro contra o qual praticar, usando só a folha sintética.

### Resumo do capítulo 6

Alterar um instantâneo para que uma regra tivesse permitido a ação destrói a evidência de que a regra precisava. Pendente, ou uma cópia posterior conferida, preserva o histórico. Uma marca a lápis não faz isso.

### Exercícios do capítulo 6

### EX022 — Reconheça a alteração

- **Objetivo:** Recusar uma edição que fabrica concordância.
- **Entrada:** A folha das 09:00 lista só `SYN-001`. Durante a interrupção, uma pessoa voluntária escreve a lápis `SYN-002`, Sala 2, 15:00, e diz: “Agora o papel coincide com a tabela, então podemos confirmar.”
- **Condição segura:** Não confirme uma sala e não altere a sua própria cópia até virar a resposta que você prefere.
- **Tarefa:** Diga o que a marca a lápis fez ao registro das 09:00, se a confirmação agora é permitida e o que você manteria no lugar.
- **Evidência esperada:** Três julgamentos.
- *Rubrica:* 3 = a marca é chamada de alteração, a confirmação continua recusada nessa folha e a alternativa é um pedido pendente ou uma cópia posterior conferida pelo responsável;; 2 = chama a marca de alteração, mas a alternativa fica incompleta;; 1 = trata o lápis como correção ou confirma a sala;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 20

[← Capítulo 05](#ch-05) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Uma fila pendente durante uma interrupção

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Separar “a página de reservas está fora do ar” de “não existe procedimento de decisão”.
2. Usar uma fila de pendências como método de continuidade sem fingir que a sala foi confirmada.
3. Aplicar o mesmo método a uma segunda interrupção sem inventar uma causa nova.

### 7.1 Disponibilidade de quê

O capítulo 1 nomeou a disponibilidade como a propriedade de que a informação e o serviço estão lá quando são necessários. Às 11:30 a visão de reserva não está lá. O balcão ainda pode estar lá. São ativos diferentes. Chamar a biblioteca inteira de “indisponível” apagaria o procedimento que ainda pode ser usado: escrever o pedido, marcá-lo como pendente e esperar uma fonte atual aprovada.

Uma entrada pendente precisa de quatro campos e de nada pessoal: o horário em que o pedido foi ouvido, a sala, o início pedido e as palavras “não confirmado”. Acrescentar o nome de um morador repetiria o erro do capítulo 5. Acrescentar “provavelmente tudo bem” seria uma confirmação vestida com roupa mais macia.

### 7.2 Exemplo resolvido: a manhã seguinte

Na manhã seguinte a visão falha de novo, das 09:10 às 09:25. Uma pessoa visitante pede para ficar com a Sala 2 às 15:00 nesse dia. Nada neste livro diz que as duas interrupções têm a mesma causa. Quem atende não precisa da causa. A fonte atual aprovada continua ausente, e o papel das 09:00 do exercício anterior é o instantâneo de outro dia, então não pode confirmar as 15:00 de hoje.

| Campo | Entrada |
|---|---|
| Ouvido | 09:12 |
| Sala | Sala 2 (`Room 2`) |
| Início | 15:00 |
| Estado | não confirmado |

Quando a visão volta, quem atende compara a linha pendente com o registro atual antes que alguém diga à pessoa visitante que a sala é dela. Se o registro atual já tem uma reserva, diz-se à pessoa que o horário está reservado, ainda sem um nome. Se estiver livre, uma reserva nova ainda exige a aprovação que o responsável definiu. Esta aula não inventa esse passo de aprovação.

### 7.3 Limite

Um comprovante pendente e calmo não mede por quanto tempo a biblioteca pode operar assim, quantos pedidos chegam ou se a visão voltará. Também não explica a interrupção. O trabalho de disponibilidade neste nível é a próxima ação segura durante a lacuna, não um estudo de capacidade.

### Resumo do capítulo 7

Uma página fora do ar remove um modo de ver reservas. Não autoriza a memória, o papel de ontem nem um sim verbal. Uma linha pendente com sala, horário e “não confirmado” mantém o serviço honesto até existir uma fonte atual.

### Exercícios do capítulo 7

### EX023 — Escreva a linha pendente

- **Objetivo:** Continuar o serviço sem confirmar uma sala.
- **Entrada:** Às 09:12 a visão de reserva está fora do ar. Uma pessoa visitante quer a Sala 2 às 15:00 hoje. O papel de ontem, das 09:00, está na gaveta.
- **Condição segura:** Não diagnostique a interrupção e não use o papel de ontem como fonte de hoje.
- **Tarefa:** Preencha os quatro campos pendentes e declare por que o papel de ontem é a fonte errada.
- **Evidência esperada:** Os quatro campos e uma exclusão.
- *Rubrica:* 3 = o estado é “não confirmado”, nenhum nome é armazenado e a folha de ontem é excluída porque é outro instantâneo;; 2 = o estado está certo, mas a exclusão da folha de ontem fica implícita;; 1 = confirma a sala ou usa a folha de ontem como fonte de hoje;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 20

[← Capítulo 06](#ch-06) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Um procedimento fraco ainda não é uma vulnerabilidade

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Usar “fraqueza” para o hábito do papel desatualizado sem promovê-lo a ataque.
2. Declarar a evidência extra que uma alegação de vulnerabilidade exigiria.
3. Recusar uma aula que trate uma limitação de sala de aula como um relatório de incidente.

### 8.1 As palavras não são intercambiáveis

O [glossário do NIST Computer Security Resource Center](https://csrc.nist.gov/glossary/term/vulnerability) descreve uma vulnerabilidade como uma fraqueza que poderia ser explorada ou disparada por uma fonte de ameaça. Uma ameaça, no mesmo glossário, é uma circunstância ou um evento que poderia prejudicar operações ou ativos. Um incidente não é o mesmo substantivo que nenhum dos dois. O capítulo 1 já separou ameaça, vulnerabilidade, evento e risco. Este capítulo aplica essa separação à única falha que o livro de fato construiu: pessoas podem tratar uma impressão das 09:00 como se fosse a agenda ao vivo.

Esse hábito é uma fraqueza no procedimento. O livro não exibiu um defeito num programa de reservas, um payload, uma conta roubada ou um morador prejudicado. Chamá-lo de vulnerabilidade só é justo se também dissermos “poderia ser disparado” como hipótese e, então, mostrarmos o disparo. Não podemos mostrá-lo. A biblioteca é fictícia, e a interrupção não tem causa medida.

### 8.2 Exemplo resolvido

| Afirmação | Classe neste livro | Por quê |
|---|---|---|
| O papel das 09:00 omite uma reserva criada às 10:05 | Observação | Está na tabela sintética |
| A equipe poderia confirmar a partir desse papel | Procedimento fraco | O exercício foi construído para que esse erro seja possível |
| Um atacante derrubou a página de reservas | Não sustentado | Não há evidência, e o capítulo 4 proíbe o site ao vivo |
| O software de reservas tem uma falha que um atacante poderia usar | Não estabelecido | Nenhum comportamento de programa foi testado |
| A interrupção é um incidente de segurança | Não declarado | Nenhum responsável a definiu como tal, e a causa é desconhecida |

A decisão útil é procedimental. Mantenha a regra de pendência, pare as edições a lápis e não nomeie pessoas que não estão no registro. Essas ações reduzem a fraqueza que o exercício pode demonstrar. Elas não encerram um incidente que nunca foi aberto.

### 8.3 O que uma aula posterior precisaria

Um curso posterior, mais técnico, pode examinar uma falha de software quando tem um programa autorizado, uma entrada controlada e um resultado observado. Esta aula rápida para antes disso. Se um colega escreve “vulnerabilidade crítica, nota 9.1” no dossiê do capítulo 4, o número é a precisão falsa que o capítulo 4 já recusou, e o substantivo é a classe errada. O dossiê permanece um registro de quatro ações com rótulos sintéticos.

### Resumo do capítulo 8

O exercício da Harbor Library mostra um procedimento desatualizado e o dano que esse procedimento pode causar dentro da história: uma confirmação errada, uma divulgação ou um instantâneo arruinado. Não mostra uma falha explorável de produto nem um ataque. Use a palavra menor até a evidência crescer.

### Exercícios do capítulo 8

### EX024 — Escolha a palavra menor

- **Objetivo:** Classificar o problema do papel desatualizado sem inflá-lo.
- **Entrada:** A nota de um colega diz: “A interrupção das 11:30 foi um incidente causado por uma vulnerabilidade crítica no site de reservas.”
- **Condição segura:** Use só fatos dos capítulos 1–7. Não investigue um site real.
- **Tarefa:** Substitua a nota por três frases: o que foi observado, que classe de problema o exercício sustenta e qual afirmação mais forte permanece não provada.
- **Evidência esperada:** Três frases que um leitor possa conferir contra o livro.
- *Rubrica:* 3 = a interrupção permanece sem explicação, a classe sustentada é um procedimento fraco e nem vulnerabilidade nem incidente são afirmados como fato;; 2 = nomeia o procedimento fraco e não afirma a causa, mas omite uma das negações;; 1 = afirma vulnerabilidade ou incidente como fato;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 20

[← Capítulo 07](#ch-07) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Uma contagem de vereditos não é uma severidade

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Ler `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0` como quatro rótulos contados e um resto vazio.
2. Manter esse censo separado do impacto adverso e da probabilidade.
3. Recusar uma nota, uma porcentagem ou um grau construído só a partir desses cinco números.

### 9.1 O programa conta rótulos

O programa do capítulo 4 percorre o registro sintético uma vez. Cada ação recebe um rótulo, e o contador desse rótulo aumenta em um. A linha impressa é um censo deste registro:

`STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`

Quatro ações entraram. Quatro rótulos decididos saíram, um de cada classe, e o resto permaneceu em zero. Essas contagens iguais pertencem ao desenho do exercício. O registro foi escrito com uma ação por classe para que todo ramo aparecesse. Uma semana posterior num balcão real poderia mostrar quarenta linhas ALLOW e uma linha REFUSE. Esse único REFUSE poderia ser a única linha em que um morador teria ouvido que uma sala ocupada estava livre. Contagens iguais de sala de aula não fazem as classes pesarem o mesmo.

`UNKNOWN 0` significa que toda ação neste registro correspondeu a um ramo da regra escrita. A interrupção ainda não tem causa testada. A folha relatada das 11:40 continua sem conferência. A biblioteca ainda tem perguntas abertas. Nenhum desses fatos era uma ação no registro, então nenhum deles pode mover um contador.

### 9.2 Exemplo resolvido

A [NIST SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1), como transportada na [entrada de risco do glossário do CSRC](https://csrc.nist.gov/glossary/term/risk), trata o risco como uma medida da extensão em que uma circunstância potencial ameaça uma entidade, em geral uma função do impacto adverso e da probabilidade. Acesso em 13 de outubro de 2026. A contagem da Harbor Library não fornece nenhuma das duas entradas. Não estima com que frequência a equipe confiaria numa impressão desatualizada, e não mede o dano de uma confirmação errada. Este capítulo usa só essa distinção. Não realiza uma avaliação de risco e não atribui um nível à biblioteca.

| Frase que um colega propôs | O que a linha impressa pode sustentar | Decisão |
|---|---|---|
| “A execução rotulou uma ação de cada classe, e nenhuma ação foi UNKNOWN.” | Os cinco contadores | Manter, como contagem |
| “Metade dos vereditos foi adversa, então o número é 50 por cento.” | Nenhum impacto e nenhuma probabilidade | Recusar a porcentagem |
| “ALLOW 1 mostra que uma sala foi confirmada como livre.” | A regra não encontrou reserva posterior para esse horário | Recusar a alegação de disponibilidade |
| “UNKNOWN 0 mostra que a interrupção das 11:30 está compreendida.” | O registro não tinha ação sem correspondência | Recusar a alegação causal |
| “Dê 2.5 à biblioteca e encerre o exercício.” | Nenhuma escala, e nenhum responsável aceitou uma fonte atual | Recusar a nota e o encerramento |

O relatório que sobrevive são as quatro decisões do capítulo 4, nomeadas uma a uma, mais a declaração de que impacto e probabilidade não foram medidos. O capítulo 8 manteve o problema demonstrado na classe “procedimento fraco”. Este capítulo deixa essa classe onde está.

### 9.3 O que os contadores deixam aberto

Um facilitador ainda pode perguntar qual fonte aprovada, se alguma, pode substituir o papel das 09:00. Essa pergunta fica fora da contagem. Tratar os contadores como equilibrados esconderia o pedido pendente da Sala 2 às 15:00 do capítulo 7. A aritmética deste registro está terminada. A decisão de reserva continua aberta.

### Resumo do capítulo 9

A contagem é um censo de rótulos num registro sintético. Contagens iguais vêm do modo como esse registro foi construído. Elas não declaram uma severidade, uma probabilidade nem permissão para parar de perguntar qual fonte está atual.

### Exercícios do capítulo 9

### EX025 — Tire a nota do painel

- **Objetivo:** Manter a contagem do capítulo 4 como contagem.
- **Entrada:** O painel de um colega diz: “Nota de risco da Harbor 25. Dois vereditos adversos em quatro são 50 por cento, então a biblioteca é Medium e o exercício pode encerrar.”
- **Condição segura:** Use a contagem impressa do capítulo 4. Não invente uma segunda execução nem abra um site ao vivo.
- **Tarefa:** Substitua o painel por quatro frases: o que foi contado, por que 50 por cento não se segue, por que Medium não se segue e qual decisão permanece aberta.
- **Evidência esperada:** Quatro frases que um leitor possa conferir contra a linha impressa e os capítulos 4, 7 e 8.
- *Rubrica:* 3 = a contagem permanece uma contagem de quatro rótulos, a porcentagem e o grau são ambos recusados e a confirmação pendente continua sem resolução;; 2 = recusa a porcentagem e o grau, mas não diz qual decisão continua aberta;; 1 = um número substituto, 50 por cento ou o grau Medium não recebe crédito;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 20

[← Capítulo 08](#ch-08) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Um horário falado não é uma impressão

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Classificar um horário de relógio repetido como relato, e não como impressão.
2. Nomear as duas conferências que teriam de passar antes que uma folha das 11:40 pudesse substituir o papel das 09:00.
3. Deixar a execução do capítulo 4 inalterada quando o único item novo é esse relato.

### 10.1 A regra lê um artefato, não uma lembrança

O capítulo 4 compara um relógio fixo de impressão com o horário em que uma reserva foi criada. A execução publicada usa 09:00. `SYN-002` foi criada às 10:05, então o papel a omite, e a confirmação das 11:42 é REFUSE. Uma frase como “o responsável mencionou uma atualização das 11:40” contém as palavras de um relógio posterior. Não contém a folha, as linhas nem uma assinatura de que este objeto é a fonte aprovada.

São entradas diferentes. O programa não consegue ver uma conversa. Se quem estuda digita 11:40 porque um facilitador falou isso, inventou a entrada. O capítulo 6 já recusou uma marca a lápis na folha das 09:00. Este capítulo recusa uma substituição diferente: trocar a folha por conversa sobre uma folha.

O capítulo 3 registrou a menção do responsável a uma cópia das 11:40 como **relatada, não verificada**. Esse rótulo continua valendo. Repetir a menção na sala de aula não a verifica. A contagem do capítulo 9 também permanece como impressa. Esta conversa não é uma das quatro ações registradas, então não pode limpar REFUSE nem mover UNKNOWN.

### 10.2 Exemplo resolvido

Dois portões têm de passar antes que alguém trate uma folha posterior como a fonte atual. O responsável pelo exercício nomeia **esta** folha como a fonte atual aprovada. Quem estuda, então, olha para essa folha e escreve duas observações: o horário na folha é 11:40, e `SYN-002` está impressa nela. Ouvir que os dois portões “provavelmente foram feitos” é um terceiro relato. Não completa nenhum dos portões.

| O que está à frente de quem estuda | Classe | A Sala 2 às 15:00 pode ser confirmada a partir disso? |
|---|---|---|
| Facilitador: “Ouvi o responsável dizer que 11:40 inclui SYN-002.” | Relato de segunda mão | Não |
| Uma folha com horário 11:40 e `SYN-002` visível, e nenhuma declaração do responsável de que esta folha é a fonte aprovada | Artefato conferido, autoridade em aberto | Não |
| A mesma folha, depois que o responsável a nomeia e as duas observações são escritas | Fonte conferida e aprovada | Só pelo procedimento que o responsável declarou |
| Um plano de redigitar 11:40 no programa do capítulo 4 | Entrada inventada | Não. Não comece essa execução |

O registro útil é curto. O resultado das 09:00 permanece. O pedido das 15:00 continua não confirmado. O horário falado é arquivado como relato ao lado do papel, não por cima dele.

### 10.3 O que este capítulo não abre

Passar os dois portões num exercício posterior ainda seria uma conferência sintética. Não mostraria com que frequência um balcão real atualiza a folha alternativa, e não explicaria a interrupção. Esta aula para no relato. Não entrega a quem estuda uma folha das 11:40, e não pede uma nova execução do programa.

### Resumo do capítulo 10

Um horário de relógio que chega numa frase é testemunho sobre uma fonte. A regra de confirmação precisa da fonte. Até o responsável nomear a folha e quem estuda registrar o horário dela e `SYN-002`, a Sala 2 às 15:00 permanece pendente e a contagem publicada permanece como estava.

### Exercícios do capítulo 10

### EX026 — Arquive a frase ao lado do papel

- **Objetivo:** Impedir que um horário de atualização ouvido vire a impressão.
- **Entrada:** A nota de um colega diz: “O facilitador ouviu o responsável mencionar 11:40, então confirme a Sala 2 às 15:00 e limpe o REFUSE.”
- **Condição segura:** Permaneça dentro do exercício sintético. Não digite um horário novo de impressão no programa do capítulo 4 e não abra um site ao vivo.
- **Tarefa:** Escreva três partes: a classe da nota, as duas conferências que ainda faltam e o estado de reserva que você deixa no lugar.
- **Evidência esperada:** Três partes que um leitor possa conferir contra os capítulos 3, 4 e 7.
- *Rubrica:* 3 = a nota permanece um relato, a nomeação pelo responsável e as observações da folha continuam ausentes, o pedido das 15:00 permanece não confirmado e a contagem publicada não muda;; 2 = mantém o relato e o pedido não confirmado, mas não nomeia os dois portões;; 1 = confirma a sala, trata o horário falado como impressão ou apaga o REFUSE;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 20

[← Capítulo 09](#ch-09) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Uma folha nomeada não libera a sala

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Ler uma página sintética nomeada das 11:40 que inclui `SYN-002` como evidência de que a Sala 2 às 15:00 já está reservada.
2. Manter essa leitura dentro deste exercício: deixar a contagem do capítulo 4 intocada e não transformar a página numa regra para interrupções posteriores.
3. Recusar o nome de uma pessoa e recusar uma conferência em site ao vivo quando a própria página já respondeu ao horário.

### 11.1 O que a página nomeada pode decidir

O capítulo 10 parou enquanto a página das 11:40 era só conversa. Esta aula muda a mesa. O responsável pelo exercício coloca uma página sintética à sua frente e diz que **esta página** é a fonte atual aprovada **para este exercício**. O cabeçalho da página é 11:40. As linhas são:

| Reserva | Sala | Início | Criada | Status |
|---|---|---|---|---|
| `SYN-001` | Room 2 | 14:00 | 08:20 | confirmed |
| `SYN-002` | Room 2 | 15:00 | 10:05 | confirmed |

Você registra duas observações a partir da página, não da memória. O relógio do cabeçalho é 11:40. `SYN-002` é uma linha impressa, com Sala 2, início 15:00, criada às 10:05 e status `confirmed`. As duas observações passam. A frase do responsável e essas duas observações são toda a autoridade desta sessão.

A decisão que esses fatos sustentam é estreita. Um morador que pede a Sala 2 às 15:00 está pedindo um horário que esta página já lista como reserva confirmada. A equipe diz que o horário está ocupado. A página tem identificadores de reserva e nenhum nome pessoal, então a resposta falada não acrescenta um. `SYN-002` identifica a linha sintética. Não é uma pessoa, e anunciar o identificador é desnecessário para a pergunta do morador.

`SYN-001` é outro horário de início. Um horário das 14:00 reservado não decide, por si, as 15:00. A resposta das 15:00 vem da linha `SYN-002`. Misturar as duas linhas inventaria um conflito, ou uma hora livre, que a página não declara.

### 11.2 Exemplo resolvido

A impressão das 09:00 e esta página são artefatos diferentes, então os rótulos não se cancelam. O capítulo 4 recusou uma confirmação que usava a impressão das 09:00, porque essa impressão não tem a linha `SYN-002`. Esta página tem a linha. A fala correta a partir desta página ainda não é “a sala está livre”. É “o horário está ocupado”. Apagar REFUSE fingiria que o programa anterior tinha lido esta página. Não tinha. Ninguém executa esse programa de novo, e ninguém digita 11:40 nele. O censo publicado permanece o censo daquele registro mais antigo.

| Próximo passo do colega | O que esta página de fato resolve | Decisão |
|---|---|---|
| “As duas conferências passaram, então chame a Sala 2 às 15:00 de livre.” | `SYN-002` é uma reserva confirmada das 15:00 | Recuse. Diga que o horário está ocupado |
| “Limpe o REFUSE na contagem do capítulo 4.” | A contagem rotula a execução das 09:00 | Deixe a linha impressa inalterada |
| “Trate 11:40 como a alternativa para toda interrupção deste mês.” | O responsável nomeou uma página, uma vez | Recuse a regra permanente |
| “Abra o site ao vivo e veja se a produção coincide.” | O exercício forneceu uma página de papel | Pare. O site permanece fechado |
| “Diga ao morador quem ocupa as 15:00.” | Nenhum nome está impresso | Recuse o nome |

A linha de caderno que coincide com a página é: a Sala 2 às 15:00 já está reservada na página nomeada das 11:40; nenhum nome é dado; o censo do capítulo 4 permanece como impresso; a página expira com este exercício.

### 11.3 O que uma página não pode resolver

Uma única página sintética não pode mostrar com que frequência um balcão real reimprime uma agenda alternativa. Não pode explicar por que a visão de reserva estava indisponível. Não pode autorizar uma busca num sistema ao vivo. A frase do responsável deve ser copiada para o caderno com o limite anexado: nomeada para este exercício, não adotada como o procedimento de interrupção da biblioteca. Quando a sessão termina, a próxima interrupção volta a ficar pendente até que a própria fonte seja nomeada e conferida.

A linha ALLOW do capítulo 4 também é a ferramenta errada aqui. Esse rótulo pertencia à Sala 4 às 15:00, um horário sem linha posterior na impressão das 09:00. A Sala 2 às 15:00 agora tem uma linha numa página diferente. Reutilizar a redação de ALLOW relataria uma sala livre que esta página contradiz.

### Resumo do capítulo 11

Quando o responsável nomeia esta página das 11:40 e as duas observações passam, a Sala 2 às 15:00 está ocupada. Essa resposta não limpa a contagem mais antiga, não identifica uma pessoa e não vira a regra da próxima interrupção.

### Exercícios do capítulo 11

### EX027 — Tire o salto da página

- **Objetivo:** Usar uma página nomeada das 11:40 sem transformar um horário reservado numa sala livre ou numa regra mensal.
- **Entrada:** Um colega escreve: “Os dois portões passaram, então a sala está livre, limpe o REFUSE e use 11:40 para toda interrupção deste mês.”
- **Condição segura:** Só papel. Deixe o programa do capítulo 4 fechado e deixe qualquer site ao vivo de reservas fechado.
- **Tarefa:** Escreva quatro frases: o que `SYN-002` mostra sobre a Sala 2 às 15:00, por que “livre” inverte essa linha, por que a linha do capítulo 4 permanece e por que 11:40 não governa a próxima interrupção.
- **Evidência esperada:** Quatro frases que um leitor possa conferir contra a página da seção 11.1 e contra a contagem publicada do capítulo 4.
- *Rubrica:* 3 = o horário permanece reservado, a contagem fica como impressa, a regra mensal é recusada e não aparecem nome de pessoa nem site ao vivo;; 2 = diz que o horário está ocupado, mas não trata da contagem ou da regra mensal;; 1 = chama a sala de livre, adota a regra mensal, limpa o REFUSE, executa o programa de novo, nomeia uma pessoa ou abre um site, e isso não recebe crédito;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 20

[← Capítulo 10](#ch-10) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Uma linha ausente não é uma sala livre

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Fazer corresponder uma pergunta de sala e início a uma linha na página nomeada das 11:40.
2. Tratar uma pergunta sem linha correspondente como silêncio, não como sala livre.
3. Deixar o rótulo ALLOW do capítulo 4 e o censo impresso no registro das 09:00.

### 12.1 Autoridade não é a mesma afirmação que completude

O capítulo 11 usou a página nomeada para uma pergunta que a página pode responder. `SYN-002` imprime a Sala 2 às 15:00, então esse horário está ocupado. Uma pergunta nova de um morador agora pede a Sala 4 às 15:00. A mesma página continua na mesa. As duas linhas continuam sendo a página inteira. Nenhuma linha diz Sala 4.

A nomeação deu permissão para ler este objeto neste exercício. Não disse que duas linhas são todas as reservas do prédio. São afirmações separadas. A primeira é sobre autoridade. A segunda seria sobre completude, e o responsável não a fez.

Busque na página pelo par que o morador pediu. Sala e início têm de corresponder ambos. `SYN-001` corresponde à Sala 2 às 14:00, então esse horário está ocupado para a própria pergunta. Não responde à Sala 4. `SYN-002` corresponde à Sala 2 às 15:00. Também não responde à Sala 4. Depois que as duas linhas são conferidas, a contagem de correspondências para a Sala 4 às 15:00 é zero. Zero correspondências é silêncio. O silêncio não sustenta nem “ocupada” nem “livre”.

A resposta falada é, portanto, limitada: “Esta página não lista a Sala 4 às 15:00, então não posso responder a partir dela.” A equipe registra o pedido como pendente. Não oferece a sala.

### 12.2 Exemplo resolvido

Um colega trata o rótulo ALLOW antigo como se fosse a linha que falta. No capítulo 4, ALLOW foi o rótulo de uma ação registrada: uma pergunta sobre a Sala 4 comparada com a impressão das 09:00. O motivo nessa execução foi que a tabela da impressão não tinha reserva posterior para o horário. A equipe já tinha sido instruída a não anunciar que a Sala 4 estava livre. A página das 11:40 é um segundo objeto. Não contém o rótulo ALLOW e não contém uma linha da Sala 4. Mover ALLOW para esta página forjaria uma linha que a impressora nunca produziu.

| Proposta | O que as duas linhas sustentam | Decisão |
|---|---|---|
| “A Sala 4 às 15:00 está ausente, então ofereça-a como livre.” | Zero linhas correspondentes | Recuse. Ausência é silêncio |
| “O capítulo 4 imprimiu ALLOW, então a página das 11:40 confirma a Sala 4.” | ALLOW pertence ao registro das 09:00 | Deixe esse rótulo onde foi impresso |
| “Acrescente a Sala 4 à mão para a página ficar completa.” | A página deixaria de ser o objeto impresso | Recuse. Essa marca é uma alteração |
| “A Sala 2 às 15:00 também tem de ser reaberta, porque a Sala 4 não está clara.” | `SYN-002` ainda corresponde à Sala 2 às 15:00 | Mantenha a leitura de ocupada para esse par |
| “Procure a lacuna no site ao vivo de reservas.” | O exercício forneceu só esta página | Pare. O site permanece fora do exercício |

A nota a guardar é uma contagem. Linhas na página: 2. Linhas que correspondem à Sala 4 às 15:00: 0. Resultado para essa pergunta: pendente. Resultado para a Sala 2 às 15:00: ainda ocupada, por `SYN-002`. Censo do registro antigo: inalterado.

### 12.3 O que o silêncio ainda deixa aberto

Um pedido pendente da Sala 4 não é uma reserva escondida. A página não mostrou um conflito e também não mostrou uma vaga. Outra fonte, nomeada depois e conferida quanto a uma linha da Sala 4, seria um exercício novo. Esta aula não fornece essa fonte. Também não explica a interrupção e não mede com que frequência um balcão real imprime uma alternativa parcial.

O programa do capítulo 4 permanece fechado. O censo dele continua uma descrição das quatro ações registradas contra a impressão das 09:00. Uma pergunta feita à página das 11:40 não é uma quinta ação nesse registro, então não pode mudar ALLOW, REFUSE ou UNKNOWN.

### Resumo do capítulo 12

Nesta página nomeada, uma pergunta só é decidida quando uma linha impressa corresponde à sala e ao início. A Sala 4 às 15:00 não tem essa linha. A página está em silêncio, o pedido permanece pendente, e o rótulo ALLOW mais antigo não é uma linha substituta.

### Exercícios do capítulo 12

### EX028 — Não ofereça a sala que a página omite

- **Objetivo:** Impedir que uma linha ausente vire oferta de uma sala livre.
- **Entrada:** Um colega diz: “A Sala 4 não está na página aprovada das 11:40, então diga ao morador que está livre às 15:00 e transforme ALLOW nessa confirmação.”
- **Condição segura:** Permaneça com as duas linhas impressas. Não escreva uma linha nova na página e não lance o programa de reservas de novo.
- **Tarefa:** Escreva quatro frases: quantas linhas correspondem à Sala 4 às 15:00, o que você diz ao morador, o que você faz com o rótulo ALLOW e o que permanece verdadeiro sobre a Sala 2 às 15:00.
- **Evidência esperada:** Quatro frases que um leitor possa conferir contra a página de duas linhas e contra o censo do capítulo 4.
- *Rubrica:* 3 = o pedido da Sala 4 permanece pendente, ALLOW permanece no registro antigo, o censo não é reescrito e `SYN-002` ainda torna a Sala 2 às 15:00 ocupada;; 2 = deixa a Sala 4 pendente e não oferece a sala, mas omite o destino de ALLOW;; 1 = oferece a sala livre ou reescreve ALLOW como confirmação, e isso não recebe crédito;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 20

[← Capítulo 11](#ch-11) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — A nomeação de ontem não vincula o dia de hoje

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Separar a página nomeada de um exercício encerrado de uma interrupção posterior.
2. Deixar o pedido de sala de hoje pendente quando o responsável de hoje não nomeou uma fonte.
3. Manter a conclusão de ontem na nota de ontem.

### 13.1 Uma nomeação tem uma sessão anexada

A página das 11:40 permanece na pasta do exercício. As linhas não foram editadas. O que terminou foi a frase que a tornava a fonte. Essa frase estava limitada à sessão em que foi dita. Uma manhã nova, com a visão de reserva descrita como indisponível às 09:12, é uma decisão nova. O colega que diz “os portões já passaram” está citando um exercício encerrado.

Até o responsável pelo exercício de hoje nomear uma fonte para hoje, a equipe não tem uma página que lhe seja permitido ler como atual. Não toma emprestada a fala de ontem. Não diz a um morador que a Sala 2 às 15:00 está ocupada, e não diz ao morador que está livre. O pedido está pendente. O censo do capítulo 4 não é participante desta manhã, então permanece impresso como estava.

### 13.2 Exemplo resolvido

| Em que o colega se apoia | O que de fato está datado | Decisão |
|---|---|---|
| “As duas conferências passaram ontem.” | Essas conferências pertencem à sessão anterior | Não as reutilize |
| “A página das 11:40 ainda está na pasta.” | Posse não é a nomeação de hoje | Deixe-a arquivada |
| “Diga que a Sala 2 às 15:00 está ocupada, como antes.” | Nenhuma fonte foi nomeada hoje | Pendente |
| “A contagem das 09:00 pode ser limpa porque uma página posterior um dia existiu.” | A contagem descreve o registro antigo | Deixe a linha |

A nota da manhã registra 09:12, Sala 2, início 15:00, estado pendente e o motivo “nenhuma fonte nomeada para hoje”. Não copia o nome de um morador e não explica a interrupção.

### 13.3 O que este limite não nega

A página anterior ainda é uma folha real do exercício anterior. Arquivá-la é permitido. Lê-la como autoridade de hoje não é. Uma frase posterior, dita pelo responsável de hoje sobre um objeto nomeado, abriria uma aula diferente. Este capítulo não fornece essa frase.

### Resumo do capítulo 13

Uma página que foi nomeada ontem responde a ontem. A interrupção de hoje espera a nomeação de hoje. Até essa frase existir, o pedido de sala está pendente e o censo antigo permanece no lugar.

### Exercícios do capítulo 13

### EX029 — Deixe ontem na nota de ontem

- **Objetivo:** Impedir que uma nomeação encerrada governe uma manhã nova.
- **Entrada:** Um colega diz: “A página das 11:40 passou nas duas conferências ontem, então confirme a Sala 2 às 15:00 de hoje a partir dela e retire o comprovante pendente.”
- **Condição segura:** Use só a pasta do exercício. Não abra um site de reservas e não alimente a página antiga no programa do capítulo 4.
- **Tarefa:** Escreva três frases: a que sessão a nomeação pertencia, o que o responsável de hoje ainda não fez e o estado do pedido de hoje.
- **Evidência esperada:** Três frases que um leitor possa conferir contra as duas datas.
- *Rubrica:* 3 = a página de ontem permanece um artefato anterior, o pedido de hoje permanece pendente e o censo não é tocado;; 2 = deixa o pedido pendente, mas não diz a qual sessão a nomeação pertencia;; 1 = confirma a sala pela página antiga ou reexecuta o censo, e isso não recebe crédito;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue estudando — capítulo 13 de 20

[← Capítulo 12](#ch-12) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Uma página nova responde só às próprias linhas

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Aplicar a nomeação de hoje à página das 11:55 e a nenhum outro objeto.
2. Ler `SYN-003` como uma Sala 4 às 15:00 ocupada, sem oferecer o nome de uma pessoa.
3. Deixar a conclusão pendente de ontem e o censo do capítulo 4 nos próprios registros.

### 14.1 A fonte de hoje é um objeto diferente

O responsável de hoje agora nomeia uma página sintética, com cabeçalho 11:55, só para este exercício. Você confere o cabeçalho no papel e encontra três linhas impressas. `SYN-003` é a linha nova: Sala 4, início 15:00, criada às 11:20, status `confirmed`. Esse par corresponde a um morador que pede a Sala 4 às 15:00. A equipe diz que o horário está ocupado. O identificador não é uma pessoa, e nenhum nome pessoal está impresso, então nenhum é falado.

`SYN-002` também está nesta página, então a Sala 2 às 15:00 também está ocupada aqui. O silêncio do capítulo 12 se aplicava a uma página que não tinha linha da Sala 4. Esta página tem a linha. O silêncio anterior não é um veto sobre um objeto posterior e nomeado. Também não é apagado da nota anterior. Duas sessões podem guardar dois fatos diferentes sobre o que as próprias páginas mostraram.

O programa das 09:00 não recebe `SYN-003`. ALLOW permanece um rótulo naquele registro antigo. Esta sessão não o reescreve como confirmação nem como recusa.

### 14.2 Exemplo resolvido

| Pergunta nesta sessão | Linha na página das 11:55 | Fala |
|---|---|---|
| Sala 4 às 15:00 | `SYN-003`, confirmed | Ocupada. Nenhum nome |
| Sala 2 às 15:00 | `SYN-002`, confirmed | Ocupada. Nenhum nome |
| Sala 4 às 16:00 | Nenhuma linha | Pendente. A página está em silêncio |
| “Limpe ALLOW porque a Sala 4 agora está listada.” | ALLOW não é uma linha nesta página | Recuse a edição |

A página das 11:40 permanece na pasta como artefato de ontem. Não é consultada para estas respostas, porque o responsável de hoje não a nomeou.

### 14.3 Limites da terceira linha

`SYN-003` é uma reserva inventada para esta aula. Não mostra que uma biblioteca real criou uma reserva às 11:20, e não mostra por que a visão de reserva estava indisponível. A nomeação expira quando este exercício termina. Uma regra de um mês do tipo “confie em 11:55” não está na página.

### Resumo do capítulo 14

Quando o responsável de hoje nomeia a página das 11:55, a Sala 4 às 15:00 está ocupada porque `SYN-003` está impressa ali. Essa leitura não reescreve a nota de ontem nem o censo das 09:00.

### Exercícios do capítulo 14

### EX030 — Leia a linha que esta página de fato tem

- **Objetivo:** Aceitar uma página nomeada nova sem arrastar para ela um silêncio antigo ou um rótulo antigo.
- **Entrada:** Um colega diz: “O capítulo 12 deixou a Sala 4 pendente, então `SYN-003` não pode contar. Mantenha a sala livre e limpe ALLOW.”
- **Condição segura:** Leia a página das 11:55 nomeada para este exercício. Não altere a página das 11:40 e não inicie o programa do capítulo 4.
- **Tarefa:** Escreva três frases: qual página está nomeada hoje, o que `SYN-003` mostra e quais dois registros você recusa editar.
- **Evidência esperada:** Três frases que um leitor possa conferir contra a página de três linhas.
- *Rubrica:* 3 = a Sala 4 às 15:00 está ocupada por `SYN-003`, nenhum nome é acrescentado, a nota de ontem fica como nota de ontem e ALLOW permanece no registro antigo;; 2 = lê `SYN-003` como ocupada e sem nome, mas não nomeia os dois registros que ficam intocados;; 1 = mantém a sala livre, apaga ALLOW ou edita a nota de ontem;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue estudando — capítulo 14 de 20

[← Capítulo 13](#ch-13) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Duas páginas não são uma agenda

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Escolher a página nomeada em vez de uma mistura de páginas.
2. Recusar uma cópia a lápis de `SYN-003` na página das 11:40.
3. Manter toda linha da página nomeada, inclusive linhas que uma página mais antiga também mostrou.

### 15.1 Uma agenda é a página à sua frente

A equipe às vezes quer a “melhor” linha de cada folha. Esse desejo constrói uma terceira agenda. Nenhuma impressora a produziu, e o responsável não a nomeou. Neste exercício o responsável nomeou a página das 11:55. As três linhas ficam juntas. Descartar `SYN-002` porque a página mais antiga foi manuseada primeiro esconderia uma linha que a página nomeada imprime. Copiar `SYN-003` para a página das 11:40 mudaria um artefato cujo trabalho é mostrar o que a folha de ontem continha.

A comparação entre as páginas pode ser escrita ao lado delas: a página posterior acrescenta `SYN-003`; as duas imprimem `SYN-002`. A comparação é uma nota. Não é uma folha-mestra nova.

### 15.2 Exemplo resolvido

| Mistura proposta | Objeto que resultaria | Decisão |
|---|---|---|
| Colar `SYN-003` na página das 11:40 | Uma página anterior alterada | Recuse |
| Descartar `SYN-002` e ficar só com a linha nova | Uma página nomeada parcial | Recuse |
| Responder a partir da página das 11:55 como impressa | O objeto nomeado | Aceite |
| Jogar fora a página das 11:40 para sobrar uma folha só | Um registro anterior ausente | Recuse. Arquive-a |

A Sala 4 às 15:00 está ocupada porque a página nomeada diz isso. A Sala 2 às 15:00 está ocupada pelo mesmo motivo. O censo do registro das 09:00 não é uma linha em nenhuma das misturas, então não é atualizado para coincidir com a mistura que alguém desejou.

### 15.3 O que uma comparação ainda pode dizer

Um facilitador pode escrever que as páginas diferem por uma linha. Essa frase não escolhe uma sala, não nomeia uma pessoa e não declara uma causa. O capítulo seguinte olha para outra tentação: apagar uma linha impressa por causa do relógio dentro dela.

### Resumo do capítulo 15

Use a página que este exercício nomeou, com todas as linhas. Não fabrique uma agenda movendo linhas entre folhas.

### Exercícios do capítulo 15

### EX031 — Pare a agenda misturada

- **Objetivo:** Impedir que dois artefatos sejam fundidos num terceiro.
- **Entrada:** Um colega diz: “Copie `SYN-003` para a página das 11:40, risque `SYN-002` na página das 11:55 e responda a partir do resultado.”
- **Condição segura:** Manuseie papel que já está no exercício. Não acrescente uma linha a nenhuma das páginas.
- **Tarefa:** Nomeie a página que você vai ler, as duas edições que você não fará e as duas respostas das 15:00 que a folha nomeada dessas páginas já sustenta.
- **Evidência esperada:** Uma nota curta que um leitor possa conferir contra as duas páginas.
- *Rubrica:* 3 = a página das 11:55 é lida inteira, as folhas mais antiga e mais nova permanecem sem marcas e os dois horários de 15:00 que a página nomeada lista são tratados como ocupados;; 2 = lê a página nomeada inteira, mas não declara os dois horários;; 1 = copia, risca ou marca uma linha;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue estudando — capítulo 15 de 20

[← Capítulo 14](#ch-14) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Um horário de criação não apaga uma linha impressa

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Ler um horário de criação como o horário da reserva e um cabeçalho como o horário da página.
2. Manter uma linha impressa quando o horário de criação é anterior ao cabeçalho da página.
3. Recusar empurrar esse horário de criação para dentro da execução já terminada das 09:00.

### 16.1 Dois relógios, uma linha

`SYN-003` traz o horário de criação 11:20. O cabeçalho da página é 11:55. Um colega argumenta que uma reserva feita às 11:20 já está “velha” às 11:55 e deve ser ignorada, e também que a mesma reserva é “depois das 09:00” e deve ser inserida no registro do capítulo 4 para ALLOW virar REFUSE. Os dois movimentos usam mal um relógio.

O cabeçalho diz quando esta folha se apresenta. Uma linha criada antes ainda pode estar numa folha posterior. Isso é ordinário. Ignorar a linha fingiria que a impressora a deixou de fora. Inserir 11:20 no programa das 09:00 fingiria que esse programa tinha visto `SYN-003`. A execução publicada não viu. O censo permanece `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`.

Na página nomeada das 11:55, a Sala 4 às 15:00 permanece ocupada.

### 16.2 Exemplo resolvido

| Afirmação sobre 11:20 | Relógio que confunde | Decisão |
|---|---|---|
| “11:20 é antes de 11:55, então descarte `SYN-003`.” | Horário de criação com cabeçalho da página | Mantenha a linha |
| “11:20 é depois das 09:00, então reexecute o registro.” | Horário de criação com um programa mais antigo | Não reexecute |
| “O cabeçalho é posterior, então a página inteira está desatualizada.” | Um cabeçalho não é, por si, um veredito | O responsável ainda nomeou esta página |
| “Mude ALLOW para REFUSE no papel.” | Um rótulo de outro artefato | Deixe o rótulo |

A linha útil é: criada às 11:20, página 11:55, linha presente, horário ocupado, registro antigo inalterado.

### 16.3 O que os relógios ainda não mostram

Nada nos dois horários explica a visão de reserva indisponível. Nada neles mede com que frequência um balcão imprime. O capítulo seguinte pergunta o que uma linha repetida pode provar, o que é uma afirmação menor do que uma causa.

### Resumo do capítulo 16

Um horário de criação localiza uma reserva. Um cabeçalho localiza uma página. Uma linha impressa permanece impressa. O censo terminado das 09:00 não é reescrito para coincidir com um relógio de uma folha posterior.

### Exercícios do capítulo 16

### EX032 — Mantenha a linha que o relógio foi usado para atacar

- **Objetivo:** Impedir que um horário de criação apague `SYN-003` ou reabra o programa antigo.
- **Entrada:** Um colega diz: “`SYN-003` às 11:20 é ao mesmo tempo velha demais para a página das 11:55 e tardia o bastante para virar ALLOW em REFUSE.”
- **Condição segura:** Compare os relógios no papel. Não digite um horário no programa de reservas.
- **Tarefa:** Declare o que cada relógio significa, se a linha permanece e o que acontece com ALLOW.
- **Evidência esperada:** Três declarações que um leitor possa conferir contra `SYN-003` e o censo publicado.
- *Rubrica:* 3 = a linha permanece, a Sala 4 às 15:00 permanece ocupada na página nomeada e ALLOW não é reescrito;; 2 = mantém a linha, mas discute reexecutar o programa;; 1 = apaga `SYN-003` ou troca ALLOW por REFUSE;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue estudando — capítulo 16 de 20

[← Capítulo 15](#ch-15) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Linhas coincidentes não são uma causa

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Declarar o fato limitado quando a mesma linha sintética está em duas páginas.
2. Recusar promover esse fato a ataque, vulnerabilidade ou incidente.
3. Deixar a classe do capítulo 8, um procedimento fraco de confirmação, onde estava.

### 17.1 O que a repetição pode carregar

Ponha a página das 11:40 ao lado da página das 11:55. `SYN-002` está nas duas, com a mesma sala, o mesmo início, o mesmo horário de criação e o mesmo status confirmado. A frase cuidadosa é que este exercício imprimiu essa linha em duas folhas posteriores. A página das 11:55 também tem `SYN-003`, que a folha anterior não tem. Semelhança e diferença podem ambas ser listadas. Nenhuma das listas contém uma causa para a visão indisponível.

O capítulo 8 já recusou chamar o hábito do papel desatualizado de fraqueza de software provada ou de incidente. Uma segunda cópia de `SYN-002` não acrescenta a demonstração que faltava. Não acrescenta uma declaração de incidente do responsável. A palavra “ataque” de um colega é uma afirmação nova sem evidência nova. A palavra “segura”, tirada da coincidência, é o exagero oposto. Linhas coincidentes não medem dano nem probabilidade, então também não revivem a nota recusada no capítulo 9.

### 17.2 Exemplo resolvido

| Frase oferecida para o par de páginas | Evidência de que precisaria | Decisão |
|---|---|---|
| “As duas páginas posteriores mostram `SYN-002` para a Sala 2 às 15:00.” | As duas folhas | Mantenha |
| “A coincidência mostra que a interrupção foi um ataque.” | Uma ação hostil demonstrada | Rejeite |
| “A coincidência mostra uma vulnerabilidade no site de reservas.” | Uma fraqueza demonstrada | Rejeite |
| “A coincidência mostra que a biblioteca está segura.” | Uma avaliação que este exercício não realizou | Rejeite |
| “Aumente o UNKNOWN da contagem, porque a causa é desconhecida.” | UNKNOWN conta ações do registro sem correspondência | Rejeite. A causa nunca foi uma das quatro ações |

A classe do problema do exercício permanece um procedimento fraco de confirmação. O censo permanece o censo do registro das 09:00.

### 17.3 A causa em aberto

A equipe ainda pode escrever “causa não estabelecida” sob a comparação. Essa frase bloqueia um final falso. Não atribui culpa e não autoriza uma investigação ao vivo. O capítulo seguinte trata de se as folhas mais antigas podem ser destruídas quando uma folha mais nova existe.

### Resumo do capítulo 17

Duas páginas que compartilham `SYN-002` sustentam essa linha compartilhada e nada causal. A interrupção permanece sem explicação. Os rótulos mais antigos de procedimento, contagem e nota permanecem nas aulas anteriores.

### Exercícios do capítulo 17

### EX033 — Tire o diagnóstico da linha coincidente

- **Objetivo:** Impedir que uma linha sintética repetida vire uma história de ataque ou uma alegação de segurança.
- **Entrada:** Um colega escreve: “As páginas concordam em `SYN-002`, portanto a interrupção foi um ataque e o exercício pode encerrar como seguro.”
- **Condição segura:** Compare as duas páginas sintéticas. Não investigue um site real.
- **Tarefa:** Substitua a nota pelo fato que as páginas sustentam, pelas duas afirmações que você rejeita e pela classe que o capítulo 8 já permitiu.
- **Evidência esperada:** Quatro frases que um leitor possa conferir contra as páginas e os capítulos 8 e 9.
- *Rubrica:* 3 = a linha compartilhada é declarada, ataque e segurança são ambos recusados, a classe de procedimento não muda e o censo não muda;; 2 = declara a linha e recusa ataque e segurança, mas não nomeia a classe de procedimento;; 1 = aceita ataque ou encerramento como seguro;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue estudando — capítulo 17 de 20

[← Capítulo 16](#ch-16) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — As páginas anteriores permanecem no arquivo

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Arquivar a impressão das 09:00, a página das 11:40 e a página das 11:55 como cópias separadas.
2. Explicar qual comparação se perde se uma cópia anterior for destruída.
3. Continuar respondendo ao exercício atual a partir da página nomeada para ele.

### 18.1 Mais nova não significa solitária

Uma página posterior pode ser a que este exercício nomeou. Esse papel não transforma as páginas anteriores em lixo. A impressão das 09:00 é o artefato que o programa publicado leu. Se ela desaparece, um leitor já não consegue ver por que a confirmação das 11:42 foi recusada. A página das 11:40 é o artefato que não tinha `SYN-003`. Se ela desaparece, o silêncio de ontem vira uma história em vez de uma folha. A página das 11:55 permanece a fonte nomeada para as respostas atuais de sala.

Arquivar significa três rótulos: horário, o que o responsável disse ou não disse sobre cada uma, e um ponteiro como “não fundir”. Sobrescrever a impressão das 09:00 com as linhas das 11:55 seria o mesmo tipo de dano que a marca a lápis do capítulo 6, feito com uma página inteira em vez de uma linha.

### 18.2 Exemplo resolvido

| Limpeza proposta | Comparação que desapareceria | Decisão |
|---|---|---|
| Destruir a impressão das 09:00 | A entrada da execução registrada | Mantenha e rotule |
| Destruir a página das 11:40 | A linha ausente da Sala 4 de ontem | Mantenha e rotule |
| Substituir as duas pela página das 11:55 | O histórico do que cada folha mostrou | Recuse |
| Responder à Sala 4 a partir da página nomeada das 11:55 enquanto as outras permanecem arquivadas | Nenhuma | Aceite |

Nenhum passo de limpeza reexecuta o programa. O censo permanece o censo do registro que já foi executado.

### 18.3 Não é uma política de retenção para uma biblioteca real

Este capítulo não fixa por quanto tempo a Harbor Library, ou qualquer biblioteca real, deve guardar papel. Não cita um estatuto. A regra é local ao exercício: não destrua as folhas de que o raciocínio depende. Um cronograma real seria uma decisão do responsável, com a própria autoridade. Essa decisão não está na pasta.

### Resumo do capítulo 18

Mantenha as três folhas, rotuladas e separadas. Use a que foi nomeada para este exercício quando responder a uma sala. Não destrua nem sobrescreva as outras para a pasta parecer simples.

### Exercícios do capítulo 18

### EX034 — Pare a limpeza

- **Objetivo:** Preservar as folhas que tornam as decisões anteriores conferíveis.
- **Entrada:** Um colega diz: “A página das 11:55 é a mais nova. Destrua a impressão das 09:00 e a página das 11:40 para o arquivo ter uma verdade só.”
- **Condição segura:** Permaneça dentro da pasta sintética. Não destrua nem marque nenhuma folha.
- **Tarefa:** Para cada folha, dê o papel dela e diga se ela permanece. Depois nomeie a folha que você de fato leria para a Sala 4 às 15:00 neste exercício.
- **Evidência esperada:** Quatro linhas curtas que um leitor possa casar com os três horários.
- *Rubrica:* 3 = as três folhas permanecem, os papéis diferem, a página das 11:55 é a lida para a pergunta atual da Sala 4 e o censo não é reexecutado;; 2 = mantém as três folhas, mas não distingue os papéis;; 1 = destrói uma folha ou reexecuta o censo;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue estudando — capítulo 18 de 20

[← Capítulo 17](#ch-17) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Uma página de reservas não abre a lista de contatos

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Manter uma página nomeada de reservas dentro das perguntas de reserva.
2. Deixar os contatos de eventos fora da autoridade dessa página.
3. Recusar acrescentar nomes para que uma mensagem fora de escopo possa ser enviada.

### 19.1 A fronteira não segue a folha mais nova

A ação das 11:43 pediu contatos de eventos e recebeu OUT OF SCOPE, porque esses contatos não fazem parte da decisão de sala. Um colega agora diz que a página das 11:55 está atual, então a exportação passou a ser permitida, e a equipe deveria dizer à lista de contatos que as salas mudaram. A página contém linhas de reserva. Não contém a lista de contatos, uma permissão para exportá-la nem uma razão para anexar nomes pessoais.

A nomeação de hoje seleciona qual folha de reservas pode ser lida. Não redesenha a fronteira do exercício dos capítulos 2 e 4. Os contatos permanecem fora. A equipe não abre uma exportação, ao vivo ou inventada, e não escreve nomes em `SYN-003` para ter alguém a quem avisar.

As respostas de sala já feitas a partir da página nomeada permanecem: Sala 2 às 15:00 ocupada, Sala 4 às 15:00 ocupada, nenhum nome falado.

### 19.2 Exemplo resolvido

| Pedido depois da nomeação das 11:55 | Relação com a página nomeada | Decisão |
|---|---|---|
| “A Sala 4 às 15:00 está ocupada?” | Corresponde a `SYN-003` | Ocupada. Nenhum nome |
| “Exporte os contatos de eventos.” | Coleção diferente | Fora de escopo |
| “Acrescente um nome a `SYN-003` para podermos ligar.” | A página não tem campo de nome | Recuse o acréscimo |
| “A página nova cancela o rótulo das 11:43.” | O rótulo descreveu outra pergunta | Mantenha OUT OF SCOPE nessa ação |

A contagem ainda é o censo das quatro ações. Este pedido não é uma quinta linha registrada, então UNKNOWN não se move.

### 19.3 Um aviso pode ser um trabalho real, sob outra autoridade

Uma biblioteca poderia um dia ter um modo lícito de avisar um frequentador sobre uma sala. Este exercício não fornece esse modo. Querer ser prestativo não move contatos para dentro da folha de reservas. O responsável teria de nomear uma atividade diferente, com o próprio limite. Até lá, o caminho dos contatos permanece fechado.

### Resumo do capítulo 19

Nomear a página das 11:55 autoriza ler as linhas de reserva dela. Não autoriza uma exportação de contatos de eventos nem um nome escrito numa linha.

### Exercícios do capítulo 19

### EX035 — Mantenha os contatos do lado de fora

- **Objetivo:** Impedir que uma página nova de reservas seja tratada como permissão para exportar contatos.
- **Entrada:** Um colega diz: “A página das 11:55 é a fonte aprovada, então exporte os contatos de eventos e acrescente os nomes correspondentes a `SYN-002` e `SYN-003`.”
- **Condição segura:** Permaneça com as linhas sintéticas de reserva. Não crie uma lista de contatos nem abra um site.
- **Tarefa:** Separe as respostas de sala que você pode dar da exportação que você não pode fazer, e diga o que acontece com o rótulo das 11:43.
- **Evidência esperada:** Uma nota curta de separação.
- *Rubrica:* 3 = os dois horários de 15:00 permanecem ocupados sem nomes, a exportação permanece fora de escopo, nenhum nome é escrito numa linha e o censo permanece como impresso;; 2 = recusa a exportação e não escreve nome, mas omite um dos horários;; 1 = exporta contatos ou escreve um nome numa linha;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-19 -->
### Continue estudando — capítulo 19 de 20

[← Capítulo 18](#ch-18) · [Índice de capítulos](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Continue para a próxima aula escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — A nota que pode sair da sala

### Objetivos de aprendizagem

Ao final deste capítulo, você deve ser capaz de:

1. Montar uma nota conferível a partir das folhas e do censo inalterado.
2. Incluir as perguntas abertas em vez de encerrar o exercício.
3. Rejeitar a alegação de segurança, a alegação de estar segura, a culpa e uma regra permanente de relógio como frases que esta pasta não pode sustentar.

### 20.1 O que cabe na nota

Um facilitador deve conseguir testar a nota sem confiar no tom de quem escreve. A nota nomeia as três folhas e diz qual delas o responsável de hoje nomeou. Responde à Sala 2 às 15:00 e à Sala 4 às 15:00 a partir dessa página nomeada, com os identificadores de reserva e sem nomes pessoais. Cita o censo do capítulo 4 como inalterado. Lista o que permanece desconhecido: a causa da visão indisponível, se algum balcão real reimprime uma alternativa num relógio determinado, e o fato de que outra interrupção precisará da própria nomeação.

Frases que não cabem: “a biblioteca está segura”, “a sala está livre”, “o morador está nomeado”, “11:55 é a regra deste mês”, “ALLOW foi limpo”, “a interrupção foi um ataque”. Cada uma falha contra uma folha ou contra o registro.

Atingir a contagem de planejamento de 20 aulas do curso rápido não encerra essas perguntas e não confere uma qualificação. A revisão de fontes, de língua e de exatidão técnica permanece aberta.

### 20.2 Exemplo resolvido

| Linha proposta para a nota que sai | Conferência | Manter? |
|---|---|---|
| “Página das 11:55 nomeada para este exercício; três linhas.” | A nomeação e a página | Sim |
| “Sala 4 às 15:00 ocupada, `SYN-003`, nenhum nome.” | Essa linha | Sim |
| “Censo inalterado.” | A linha impressa | Sim |
| “Causa não estabelecida.” | Nenhuma causa está em folha alguma | Sim |
| “O risco da Harbor é baixo e o exercício está encerrado.” | Nenhuma escala e nenhuma condição de encerramento | Não |
| “Use 11:55 sempre que o site falhar.” | A nomeação foi para este exercício | Não |

A nota pode sair da sala. O caso não pode ser declarado terminado.

### 20.3 O que a vigésima aula não termina

Outra interrupção, uma regra real de retenção ou um procedimento de contato seriam ensino adicional se um responsável os definisse. Não estão implícitos por se chegar à aula 20. As outras línguas deste curso não ficam publicadas por esta nota. Segurança da informação é um livro separado. Leia-o quando a intenção for estudar aquele livro, e não como substituto de uma pergunta da Harbor Library que ficou sem resposta.

### Resumo do capítulo 20

A nota que sai lista a folha nomeada, os horários ocupados, o censo intocado e as perguntas abertas. Não encerra o caso, não nomeia uma pessoa, não libera uma sala e não converte este exercício numa regra permanente.

### Exercícios do capítulo 20

### EX036 — Corte a frase de encerramento

- **Objetivo:** Produzir uma nota que um facilitador possa conferir, inclusive o que continua aberto.
- **Entrada:** As linhas de encerramento de um colega dizem: “As vinte aulas estão feitas, então a Harbor está segura, a Sala 4 está livre afinal, e 11:55 será a alternativa toda manhã deste mês.”
- **Condição segura:** Use a pasta sintética e o censo impresso. Não acrescente uma folha nova nem abra um site.
- **Tarefa:** Substitua esse final pela folha em que você se apoia, pelas duas respostas das 15:00, pelo censo e por uma pergunta que a pasta ainda não consegue responder.
- **Evidência esperada:** Cinco linhas conferíveis.
- *Rubrica:* 3 = os dois horários da página nomeada permanecem ocupados, o censo é citado sem mudança, ao menos uma pergunta realmente aberta permanece e somem a alegação de segurança, a sala livre e a regra mensal;; 2 = mantém os horários ocupados, o censo e a recusa da sala livre, mas a pergunta aberta não é uma pergunta que a pasta deixe sem resposta;; 1 = declara o livro concluído, libera a sala, mantém a alegação de segurança ou a regra mensal, e isso não recebe crédito;; 0 = nenhuma.

<!-- open-cyber-academy:chapter-navigation:start ch-20 -->
### Continue estudando — capítulo 20 de 20

[← Capítulo 19](#ch-19) · [Índice de capítulos](../SUBJECTS.md) · [Próximo curso pelo índice de capítulos →](../SUBJECTS.md)

O índice de capítulos leva ao próximo curso do percurso de estudo.
<!-- open-cyber-academy:chapter-navigation:end -->

## Referências e notas de fonte

- [NIST, Cybersecurity Framework 2.0 FAQ](https://www.nist.gov/cyberframework/faqs) — seis funções e o uso contínuo, orientado a resultados. Acesso em 11 de outubro de 2026.
- [NIST CSRC glossary, “threat”](https://csrc.nist.gov/glossary/term/threat) — fonte de terminologia. Acesso em 11 de outubro de 2026.
- [NIST CSRC glossary, “vulnerability”](https://csrc.nist.gov/glossary/term/vulnerability) — fonte de terminologia. Acesso em 11 de outubro de 2026.
- [CISA, Secure Our World](https://www.cisa.gov/secure-our-world) — ações práticas iniciais de segurança pessoal. Acesso em 11 de outubro de 2026.
- [NIST SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final) — contexto de planejamento e avaliação. Acesso em 11 de outubro de 2026.
- [NIST CSRC glossary, “Rules of Engagement”](https://csrc.nist.gov/glossary/term/Rules_of_Engagement) — limites de teste combinados de antemão. Acesso em 11 de outubro de 2026.
- [NIST, The Cybersecurity Framework 2.0 (NIST CSWP 29)](https://doi.org/10.6028/NIST.CSWP.29) — resultados de gestão de ativos `ID.AM-01`, `ID.AM-02`, `ID.AM-03`, `ID.AM-04`, `ID.AM-05` e `ID.AM-07`. Acesso em 11 de outubro de 2026.
- [OWASP, Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — elementos do modelo de sistema, fluxos de dados e fronteiras de confiança. Acesso em 11 de outubro de 2026.
- [NIST CSRC glossary, “vulnerability”](https://csrc.nist.gov/glossary/term/vulnerability) — fraqueza que poderia ser explorada ou disparada por uma fonte de ameaça. Acesso em 13 de outubro de 2026.
- [NIST CSRC glossary, “threat”](https://csrc.nist.gov/glossary/term/threat) — circunstância ou evento com potencial de prejudicar operações ou ativos. Acesso em 13 de outubro de 2026.
- [NIST SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1), por meio da [entrada de “risk” no glossário do CSRC](https://csrc.nist.gov/glossary/term/risk) — risco como impacto junto com probabilidade. Acesso em 13 de outubro de 2026. A contagem da Harbor Library não é uma aplicação desse método.

A Harbor Library, os serviços, o registro de eventos e as decisões trabalhadas são material original e fictício de ensino. Nenhum texto ou figura das fontes ligadas é reproduzido aqui. As definições e as descrições do framework são parafraseadas e ligadas a essas referências primárias.

<a id="worked-results"></a>

## Apêndice final — resoluções e notas de avaliação

Estas resoluções correspondem a EX001–EX036. Respostas equivalentes recebem crédito quando mantêm os mesmos limites de evidência. Atingir o mínimo de 20 aulas é separado deste gabarito.

### EX001 — Resolução

O serviço é a reserva de salas e o acesso à agenda. Os ativos incluem os registros de reserva (informação), a aplicação de reservas (software) e as contas de acesso da equipe (recursos de identidade). O depósito de reservas e o processo de acesso da equipe são dependências da agenda da equipe mostrada no diagrama de amostra; o desenho exato exigiria verificação num cenário real. Os registros de reserva importam para os moradores porque uma reserva incorreta ou indisponível pode desperdiçar uma visita ou criar uma reserva em duplicidade. Uma resposta que rotula “a internet” como o serviço, sem explicar o resultado para o morador, está incompleta.

### EX002 — Resolução

Confidencialidade: um destinatário não autorizado recebe a lista de contatos de eventos; os assinantes são afetados; confira um registro aprovado de exportação ou de entrega antes de afirmar a divulgação. Integridade: uma reserva é alterada sem o pedido do morador; moradores e equipe são afetados; compare o registro de referência e um histórico de mudanças. Disponibilidade: a página de reservas fica indisponível durante uma janela de reserva; moradores e equipe podem ser afetados; confira o horário, o alcance e o monitoramento do serviço. São cenários inventados. Uma resposta pode usar exemplos diferentes se cada propriedade e cada pergunta de verificação estiverem claras.

### EX003 — Resolução

(a) é sustentada pelo registro sintético. (b) não é sustentada: nenhuma causa da interrupção está registrada. (c) é uma inferência razoável porque a impressão é mais antiga que a reserva, mas uma alocação errada de fato não é observada. (d) não é sustentada: a lista de contatos não aparece no registro do evento. A habilidade central é preservar a fronteira entre uma consequência plausível e um evento documentado.

### EX004 — Resolução

Uma alternativa aceitável: a liderança do balcão é responsável por um procedimento de interrupção. Quando a agenda ao vivo está indisponível há cinco minutos, a equipe marca o horário da última impressão e evita confirmar reservas posteriores só a partir dessa impressão. Usa uma fonte secundária atual e aprovada, se existir uma, ou registra o pedido e diz ao morador que a confirmação está pendente. Num teste em papel, acrescente uma reserva sintética às 10:05, dispare uma interrupção às 11:30 e confira se a equipe nota que uma impressão das 09:00 está desatualizada. Um modo de falha é que a fonte secundária também esteja desatualizada; o responsável deve verificar o horário de atualização antes de confiar nela. O gatilho preciso de cinco minutos é um parâmetro proposto do exercício, não uma política real.

### EX005 — Resolução

Governar: designe um responsável pelas decisões de reserva e da lista de contatos. Identificar: mapeie o serviço de reservas e as dependências. Proteger: restrinja mudanças da equipe a contas autorizadas. Detectar: alerte um revisor sobre mudanças inesperadas de reserva. Responder: suspenda uma conta de uso indevido confirmado e comunique o responsável pelo serviço. Recuperar: restaure uma agenda confiável e verifique-a com o responsável. O NIST descreve as funções como contínuas e concorrentes. Mapear um exemplo para cada função ajuda a revelar responsabilidades; não prova que todo controle funciona ou que o risco desapareceu.

### EX006 — Resolução

Responsável: o responsável fictício pelo serviço da biblioteca, representado por quem instrui. No escopo: as duas reservas sintéticas e uma impressão inventada das 09:00. Excluídos: sistemas de produção, contas e informação de moradores reais. Ações permitidas: comparar registros e dramatizar decisões do balcão. Tempo: uma sessão agendada de 30 minutos. Quem recebe o resultado: o responsável pelo serviço. Uma resposta que nomeia um site real sem autorização específica falha a exigência de limite.

### EX007 — Resolução

Mantenha o identificador de reserva para rastrear o registro inventado, a sala para comparar usos concorrentes, o horário de início para determinar qual pedido importa, o horário de criação para testar a desatualização da impressão e o status para saber se o pedido está confirmado. Remova o nome do morador e o número de telefone pessoal: nenhum dos dois é necessário para a pergunta de horário. Quem estuda pode omitir o status se o cenário disser com clareza que as duas reservas estão confirmadas, mas deve declarar essa premissa.

### EX008 — Resolução

Pause a conferência ao vivo proposta. Registre que ela foi proposta, sem abrir o site e sem atribuir culpa. Pergunte ao responsável designado do exercício se uma atividade aprovada diferente é necessária. Continue o objetivo de aprendizagem offline usando a folha sintética de reservas e a impressão, se o responsável confirmar que o exercício original permanece no escopo. A curiosidade de uma pessoa não substitui o limite aprovado.

### EX009 — Resolução

Observação: a impressão sintética das 09:00 não incluía `SYN-002`, que a amostra diz ter sido criada às 10:05. Interpretação: uma impressão estática poderia enganar a equipe sobre reservas posteriores durante uma interrupção. Limitação: o exercício em papel não testou a biblioteca real nem mostrou uma violação. Próxima verificação: peça ao responsável pelo serviço o procedimento alternativo aprovado e teste-o com uma reserva sintética posterior. A redação mantém a evidência e a conclusão em proporção.

### EX010 — Resolução

Na primeira rodada, quem atende pode prometer a Sala 2 às 15:00 a partir de uma impressão antiga; registre isso como a decisão observada na dramatização. Na segunda rodada, quem atende marca a impressão como desatualizada e coloca o pedido numa fila de pendências. Um critério de melhora é “quem atende não confirma uma reserva posterior à impressão sem uma fonte atual aprovada”. O resultado é limitado por dados inventados e por uma única sessão com um número pequeno de participantes. Não estabelece confiabilidade no mundo real; testes repetidos e revisão do responsável seriam necessários.

### EX011 — Resolução

A pergunta de decisão é se uma pessoa do balcão pode tomar uma decisão correta sobre a sala enquanto a visão ao vivo está indisponível. O morador é uma entidade externa; a visão de reserva e a visão da equipe são processos; o depósito de reservas é um depósito; a agenda impressa é uma cópia física. Quaisquer quatro desses papéis, explicados de modo correto, satisfazem a tabela. A lista de contatos de eventos está fora do caminho de reserva rastreado porque a finalidade são os anúncios, embora continue relevante para um inventário de informação mais amplo. Uma pergunta aberta é se a visão da equipe lê o mesmo depósito mostrado no diagrama. Um bom modelo diz “leitura proposta” até o responsável confirmar.

### EX012 — Resolução

Às 08:20, `SYN-001` é criada; às 09:00, a impressão fixa é feita; às 10:05, `SYN-002` é criada; às 11:42, chega a pergunta sobre a sala. Sob a premissa declarada de instantâneo, a impressão pode mostrar `SYN-001`, mas não `SYN-002`. Não pode estabelecer que a Sala 2 está livre às 15:00. Quem atende marca o pedido como pendente e pede uma fonte atual aprovada ou o responsável. Se alguém diz que a impressão poderia se atualizar sozinha, precisa contestar de modo explícito a premissa do exercício; não pode usar em silêncio um cenário diferente.

### EX013 — Resolução

Dois fluxos no modelo proposto são o pedido de reserva de um morador até a visão de reserva e uma escrita proposta da visão de reserva até o depósito de reservas. Para gravar uma reserva neste caminho hipotético, o processo de reserva precisaria de um modo de persistir uma decisão válida; se o depósito retratado é o mecanismo real permanece não verificado. Para enviar uma confirmação por um fornecedor hipotético, esse fornecedor precisaria receber os dados exigidos de aviso e aceitar a tarefa de entrega. Uma mensagem atrasada não prova, por si, uma reserva que falhou. Pergunte ao responsável se as confirmações são enviadas por um serviço externo e se gravar e enviar mensagem estão acoplados. Outras respostas são aceitáveis quando declaram um resultado, uma dependência e uma incerteza, em vez de afirmar uma implementação não observada.

### EX014 — Resolução

Fronteira do morador: um pedido de sala e horário entra na visão de reserva; um morador pode pedir uma sala disponível, mas não deve ganhar poderes da equipe. Pergunte ao responsável como os pedidos são validados e o que um teste sintético aprovado ou uma revisão de desenho mostra. Fronteira da equipe: uma pessoa autenticada consulta uma visão da equipe e pode ver ou alterar informação segundo um papel definido. Pergunte quais papéis podem fazer mudanças e se uma matriz de papéis aprovada e um teste revisado sustentam essa regra. As setas localizam perguntas; não mostram que verificações de acesso existem ou funcionam. Uma afirmação de que cifragem ou autenticação multifator está presente só a partir deste desenho falha a exigência de evidência.

### EX015 — Resolução

A conclusão anterior, de que só uma agenda de papel desatualizada das 09:00 está disponível, fica enfraquecida pelo relato novo do responsável. Acrescente “agenda offline aprovada e relatada, atualizada às 11:40” como uma cópia separada; marque a autoridade e a atualidade como **relatadas, não verificadas**. Num ensaio em papel, dê a quem atende uma folha sintética das 11:40 e confira que o carimbo de tempo é 11:40 e que ela inclui `SYN-002`. Se o responsável confirma isto como fonte atual aprovada e a conferência passa, quem atende pode usá-la segundo o procedimento aprovado; se a conferência falha, mantenha o pedido pendente. Uma limitação que permanece é que uma única conferência sintética não estabelece com que confiabilidade a agenda offline real se atualiza. O modelo correto muda de modo condicional, em vez de defender o diagrama antigo.

### EX016 — Resolução

A linha REFUSE é `11:42 confirm-from-printout`. O motivo nomeia `SYN-002`. Esse identificador está ausente do papel porque a impressão do exercício é fixa às 09:00 e a reserva foi criada às 10:05. A saída não diz que um atacante causou a lacuna.

### EX017 — Resolução

A Sala 4 às 15:00 não tem linha criada depois das 09:00, então a regra imprime ALLOW e o motivo diz que nenhuma reserva posterior está registrada para essa sala e esse início. O membro da equipe não deve dizer a um morador que a Sala 4 está livre. ALLOW aqui significa que a tabela sintética não continha uma reserva posterior em conflito.

### EX018 — Resolução

REFUSE compara um horário de impressão com uma reserva criada depois. A exportação das 11:43 nunca faz essa comparação, então a regra devolve OUT OF SCOPE. Esta execução não mostra quem pode baixar a lista de contatos, por quanto tempo ela é guardada ou se um controle sobre ela funciona.

### EX019 — Resolução

Depois de STOP, o programa ainda imprime a linha de marcar pendente das 11:45 e a contagem final. Um facilitador pausa as pessoas participantes, não deixa ninguém abrir um site e pergunta ao responsável pelo exercício o que acontece em seguida. O programa está reproduzindo um registro; o facilitador é responsável pelas pessoas na sala.

### EX020 — Resolução

Uma nota aceitável: O exercício classificou quatro ações sintéticas contra uma impressão das 09:00. Às 11:42 o programa recusou a confirmação da Sala 2 às 15:00 porque o papel omite `SYN-002`. A decisão é deixar esse pedido pendente em vez de confirmá-lo a partir do papel. A exportação das 11:43 está fora de escopo, não é uma reserva recusada. O programa não abriu um depósito de reservas e não tratou a folha relatada das 11:40 como verificada. A pergunta aberta para o responsável é qual fonte aprovada, se alguma, pode substituir o papel das 09:00. Nenhuma nota numérica cabe na nota.

### EX021 — Resolução

Diga: “A Sala 2 às 14:00 já está reservada. Esta folha não diz quem, e eu não vou adivinhar.” Deixe de fora o nome de qualquer pessoa. `SYN-001` identifica uma reserva sintética, não um morador, então ler o identificador em voz alta também é desnecessário para a pergunta de quem pergunta.

### EX022 — Resolução

A marca a lápis substitui o instantâneo das 09:00 por uma linha nova e não autorizada, então a folha já não pode mostrar o que foi impresso. A confirmação nessa folha alterada continua não permitida. Mantenha o pedido pendente, ou espere uma cópia posterior cujo horário e cujo autor o responsável possa conferir. Não trate o lápis como essa cópia.

### EX023 — Resolução

Ouvido às 09:12; sala Sala 2 (`Room 2`); início 15:00; estado não confirmado. O papel de ontem, das 09:00, é outro instantâneo, então não pode mostrar se as 15:00 de hoje estão livres. Nenhum nome de morador cabe no comprovante, e a causa da interrupção não faz parte da entrada.

### EX024 — Resolução

O exercício observou um papel das 09:00 que omitiu uma reserva sintética posterior, e uma visão de reserva descrita como indisponível, sem causa testada. A classe sustentada é um procedimento fraco de confirmação. Uma vulnerabilidade de software, um ataque e um incidente não estão provados: nenhuma falha de programa foi demonstrada, e nenhum responsável declarou um incidente.

### EX025 — Resolução

O programa contou um STOP, um OUT OF SCOPE, um REFUSE e um ALLOW no registro de quatro ações, e deixou UNKNOWN em zero. Cinquenta por cento transformaria dois desses rótulos numa taxa de dano. A linha impressa não mede dano e não mede com que frequência a equipe confiaria no papel desatualizado. Medium nomeia um grau que este exercício nunca definiu. O pedido da Sala 2 às 15:00 permanece pendente até existir uma fonte atual aprovada. O procedimento fraco de confirmação do capítulo 8 permanece inalterado.

### EX026 — Resolução

A nota do colega é um relato de segunda mão de um horário de relógio. Não é a folha das 11:40. O responsável não nomeou uma folha como fonte atual aprovada, e ninguém registrou que o próprio horário da folha é 11:40 e que `SYN-002` está impressa nela. A Sala 2 às 15:00 permanece não confirmada. A contagem do capítulo 4 permanece `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`.

### EX027 — Resolução

`SYN-002` na página nomeada é uma reserva confirmada da Sala 2 às 15:00, então diz-se ao morador que o horário está ocupado. A palavra livre contradiz essa linha. O programa mais antigo ainda descreve a impressão das 09:00, e a linha permanece `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`. Um cabeçalho 11:40 numa página de sala de aula não fixa a alternativa para interrupções posteriores. Nenhum nome pessoal é falado, e o site ao vivo não é aberto.

### EX028 — Resolução

A página nomeada imprime duas linhas, e as duas nomeiam a Sala 2. A Sala 4 às 15:00 não corresponde a nenhuma, então a página não diz nada sobre esse pedido. A equipe diz ao morador que não pode responder a partir desta página e deixa o pedido pendente. Não oferece a sala. ALLOW permanece o rótulo que o capítulo 4 imprimiu para o registro das 09:00. Não é reescrito como confirmação na página das 11:40. O censo desse registro ainda é `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`. `SYN-002` ainda está na página, então a Sala 2 às 15:00 permanece reservada.

### EX029 — Resolução

A nomeação que o colega cita pertencia à sessão anterior. O responsável de hoje não nomeou uma fonte para a interrupção das 09:12. O pedido de hoje da Sala 2 às 15:00 permanece pendente. A página das 11:40 permanece arquivada como folha anterior. O censo do capítulo 4 não é reexecutado.

### EX030 — Resolução

O responsável de hoje nomeou a página das 11:55. `SYN-003` imprime a Sala 4 às 15:00 como confirmada, então o horário está ocupado e nenhum nome pessoal é acrescentado. O silêncio do capítulo 12 permanece na nota daquele capítulo sobre a página das 11:40. ALLOW permanece no registro das 09:00.

### EX031 — Resolução

Leia a página das 11:55 inteira. Não copie `SYN-003` para a página das 11:40 e não risque `SYN-002` da página nomeada. Os dois horários de 15:00 impressos na página nomeada estão ocupados. As folhas permanecem sem marcas.

### EX032 — Resolução

11:20 é quando `SYN-003` foi criada. 11:55 é o cabeçalho da página. A linha está na página nomeada, então a Sala 4 às 15:00 permanece ocupada. ALLOW não é invertido. O programa não é iniciado de novo.

### EX033 — Resolução

As duas páginas posteriores mostram `SYN-002` para a Sala 2 às 15:00. Esse é o fato sustentado. Um ataque não é mostrado. Segurança não é mostrada. A classe sustentada permanece um procedimento fraco de confirmação. O censo permanece a linha de quatro rótulos do registro das 09:00.

### EX034 — Resolução

Mantenha a impressão das 09:00 porque é a entrada da execução registrada. Mantenha a página das 11:40 porque mostra a linha ausente da Sala 4 de ontem. Mantenha a página das 11:55 e use-a para a pergunta atual da Sala 4. Não destrua nem sobrescreva. Não reexecute o censo.

### EX035 — Resolução

A Sala 2 às 15:00 e a Sala 4 às 15:00 permanecem ocupadas a partir da página nomeada, sem nomes falados ou escritos. A exportação de contatos de eventos permanece fora de escopo, e o rótulo das 11:43 permanece OUT OF SCOPE. O censo não ganha uma quinta ação.

### EX036 — Resolução

A nota nomeia a página das 11:55 para este exercício. A Sala 2 às 15:00 está ocupada a partir de `SYN-002`. A Sala 4 às 15:00 está ocupada a partir de `SYN-003`. O censo permanece `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`. A causa da interrupção ainda não está estabelecida. A alegação de segurança, a sala livre e a regra mensal das 11:55 são removidas. Chegar à aula 20 não termina o livro.
