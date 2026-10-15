# Resposta a incidentes e resiliência cibernética: curso guiado de um mês

- Idioma: português do Brasil (`pt`). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md), blob `cc7ca69e85e5bfeef91fa40038bcc5f87c56e403` (`git hash-object`).
- Este arquivo contém **somente o capítulo 1**. Os capítulos 2, 3 e 4 da referência inglesa ainda não estão traduzidos aqui. Não há, neste manuscrito, o ensino, os exercícios nem as resoluções desses capítulos.
- Nível: curso rápido, um mês. A carga deste arquivo é a do capítulo 1 da edição inglesa: cinco aulas diárias e os exercícios EX001–EX013, com resoluções. A edição inglesa planeja cerca de 80 horas para o livro inteiro; este arquivo não cobre esse total.
- Estado editorial: **texto de estudo publicado, com revisão independente aberta**. A revisão especializada do volume, a revisão de língua e a verificação em A4 continuam pendentes. Isto **não é uma qualificação concluída**, nem programa credenciado, nem livro editorialmente encerrado.
- Acesso: esta edição pública pode ser lida e estudada. Uma medição anterior da fonte chegou ao piso de extensão em A4, mas a fonte revista não tem nova renderização verificada. A medição de 343 páginas A4 do mantenedor vale apenas para o SHA-256 anterior `1353d6f595a18018b315126f7791aa0e32767c097bb78cf26ad41fc498b8af64`. O relatório anterior de 337 páginas não mede esta tradução nem a fonte alterada.
- Autoria e responsabilidade editorial: [hiagokinlevi](https://github.com/hiagokinlevi)
- Direitos: o texto original do mantenedor está dedicado sob [CC0 1.0](../../../../../LICENSE); as fontes citadas mantêm os próprios direitos.
- Caso: **Harbor Library**, organização fictícia copiada deste livro. Não se usam nomes de outros cursos. O ensino é defensivo: prontidão, papéis, escopo autorizado e registro de decisão. Não há exploit, carga útil nem procedimento de ataque.

As atualizações de 2026-10-13 da edição inglesa tratam de correções dos capítulos 2 e 4. Esses capítulos não estão neste arquivo, e o detalhe dessas correções não é reproduzido aqui. A revisão técnica, linguística, de direitos, de acessibilidade e de A4 do volume continua aberta segundo o [padrão do livro](../../../../../BOOK_STANDARD.md).

[Visão do curso](../README.md) · [Índice das aulas](../SUBJECTS.md) · [Skill do curso](../../skill/SKILL.md) · [Plano do livro](PLAN.md) · [Playbooks de prática](../../../../../playbooks/incident-response-resilience/README.md)

[Aula 01](#lesson-01) · [Aula 02](#lesson-02) · [Aula 03](#lesson-03) · [Aula 04](#lesson-04) · [Aula 05](#lesson-05) · [Resoluções do capítulo 1](#answers)

As aulas 06–20 existem na edição inglesa e **não** estão neste manuscrito. Não há elo para elas aqui.

## Como estudar esta edição pública

Leia a explicação e o exemplo resolvido de cada aula diária antes de olhar os exercícios. Registre à parte observações, premissas, decisões e informações ausentes. Use apenas os sistemas e registros fictícios fornecidos aqui, ou um ambiente que você possua e esteja autorizado a testar. As resoluções no fim deste arquivo ilustram um raciocínio aceitável; uma resposta que identifique outras premissas defensáveis também pode ser válida.

O currículo do livro inglês tem quatro módulos: (1) prontidão para incidentes, papéis e escopo autorizado; (2) triagem de alertas e preservação de evidência; (3) decisões de contenção, erradicação e recuperação; e (4) uma simulação guiada com revisão pós-ação. **Neste manuscrito só está o módulo 1, como capítulo 1.** Cada capítulo semanal da edição inglesa contém cinco aulas diárias. O livro inglês contém 50 exercícios. Este arquivo contém os 13 exercícios do capítulo 1, com resoluções. A contagem de exercícios, sozinha, não satisfaz o padrão completo de publicação.

| Capítulo semanal neste arquivo | Assunto | Aulas diárias | Exercícios escritos | Estado |
|---|---|---:|---:|---|
| 1 | Prontidão para incidentes, papéis e escopo autorizado | 01–05 | 13 | Publicado neste arquivo; revisão independente aberta |

Os capítulos 2, 3 e 4 da edição inglesa — triagem de alertas e preservação de evidência; decisões de contenção, erradicação e recuperação; simulação guiada e revisão pós-ação — **não estão traduzidos neste manuscrito**.

**Nota da edição em capítulos semanais:** o módulo 1 é o capítulo semanal deste arquivo; o ensino está nas aulas 01–05, e os 13 exercícios acompanham essas aulas. Uma aula pode ir além do mínimo nominal de quatro semanas quando o assunto exigir. Esta passagem estrutural não certifica, por si, exatidão técnica, extensão A4 medida nem conclusão do livro.

<a id="week-01"></a>
<a id="ch-01"></a>

## Capítulo 01 — Prontidão para incidentes, papéis e escopo autorizado

**Cinco aulas diárias · semana 1 de quatro na edição inglesa.** Este capítulo agrupa os identificadores originais de seção 1.x. Os números de aula identificam um dia de estudo; os identificadores de seção permanecem estáveis para que referências de fonte e instruções de laboratório continuem a funcionar. As semanas 2, 3 e 4 não estão neste arquivo.

#### Objetivos de aprendizagem do módulo

Ao longo destas cinco aulas diárias, quem estuda deve ser capaz de:

1. Explicar por que a resposta a incidentes começa antes de um alerta aparecer e continua depois da recuperação do serviço.
2. Distinguir uma observação de uma interpretação, de uma decisão de resposta e de um fato confirmado.
3. Identificar o responsável pelo serviço, o líder da resposta, o analista, o responsável pela recuperação e o contato de comunicação de um incidente pequeno.
4. Definir o escopo e a autorização de um exercício de resposta contido.
5. Abrir um registro de incidente com linha do tempo, ponteiros de evidência, incerteza e dono da decisão.
6. Descrever uma primeira ação segura quando um sinal suspeito ainda não foi verificado.
7. Transformar um mapa de dependências do serviço num plano limitado de prontidão de evidência, sem tratar uma fonte de log planejada como fato já coletado.

#### Pacote compartilhado da Rodada A

As oito linhas seguintes são entradas sintéticas de sala para as aulas 01–05 do capítulo 01. A seção 1.7 explica depois a proveniência e os limites; esta prévia torna o mesmo pacote disponível antes do primeiro exercício diário. Todos os horários são UTC em 2026-10-11. Uma linha relata o conteúdo da fonte, não uma causa provada nem uma identidade humana.

| ID | Hora | Fonte | Observação relatada |
|---|---|---|---|
| R1 | 08:40 | Log de identidade | `desk-a` entrou com sucesso |
| R2 | 08:42 | Log da aplicação | `desk-a` abriu o painel de reservas |
| R3 | 08:43 | Log da aplicação | A reserva B17 mudou da Room 2 para a Room 4 |
| R4 | 08:44 | Log da aplicação | A reserva B18 foi cancelada |
| R5 | 08:48 | Central de atendimento | Um frequentador relatou que B18 desapareceu |
| R6 | 08:50 | Calendário da equipe | O treinamento da recepção estava marcado para 08:30–09:00 |
| R7 | 08:52 | Monitor de cópia de segurança | A cópia da noite anterior terminou com sucesso |
| R8 | 08:55 | Resumo de rede | O detalhe de destino está ausente; não se segue nenhuma conclusão de rede relevante |

#### Regras dos exercícios do módulo 1

Trabalhe **somente com R1–R8** e com as regras fictícias de autoridade do módulo 1. O caso é sintético. Nos marcos de abertura às 09:00 e de decisão às 09:05, não cite registros ou entrevistas liberados em capítulos posteriores, não afirme que houve coleta de produção e não infira a identidade de uma pessoa a partir do rótulo de uma conta. Escreva qualquer sinal futuro imaginado como **hipotético**. Em cada resposta: (1) escreva `HL-IR-001` e o identificador do exercício; (2) copie os identificadores de registro relevantes e os horários UTC; (3) preencha os campos de saída nomeados; (4) marque cada conclusão como observada, inferida, desconhecida ou proposta; (5) nomeie um dono e uma aprovação para qualquer coleta nova ou mudança de serviço; e (6) compare o resultado com a resolução no fim deste arquivo. A tabela, a nota ou o cartão de decisão entregue é a evidência esperada de aprendizagem; um rótulo sem o registro que o sustenta é insuficiente.

**Rubrica comum de avaliação:** a fonte pontua um exercício com **0** se o artefato falta ou apresenta como fato uma atribuição ou ação sem suporte; com **1** se responde à pergunta, mas omite uma fonte, um limite, uma autoridade ou um teste exigido; com **2** se todos os campos nomeados estão presentes, o raciocínio segue a evidência fornecida e o passo seguinte é limitado e autorizado. Os requisitos locais abaixo especificam o que obtém 2 pontos. Uma alegação de comprometimento, de restauração bem-sucedida ou de ausência de transferência de dados baseada apenas em R1–R8 deve ser corrigida, qualquer que seja a nota numérica. Não é preciso site, conta ou dado real de frequentador.

*Rubrica:* 3 = reproduz a nota 2 da fonte: todos os campos nomeados presentes, raciocínio preso à evidência fornecida e passo seguinte limitado e autorizado;; 2 = os campos nomeados estão presentes, mas falta um limite, uma autoridade ou um teste exigido para a nota 2;; 1 = responde à pergunta, mas omite fonte, limite, autoridade ou teste exigido;; 0 = nenhum.

<a id="lesson-01"></a>

### Aula 01 — Prontidão de evidência e a primeira pergunta do caso

**Semana 1, dia 1.** Percorra o ensino e o marco resolvido antes de tentar o exercício indicado. Compare o seu artefato com a resolução final só depois.

#### 1.1 A resposta faz parte da gestão de risco

Uma equipe de resposta a incidentes faz mais do que reagir a um alarme. Ela prepara contatos e autoridade, reconhece atividade potencialmente danosa, preserva fatos, toma decisões proporcionais, restaura serviços e aprende com o resultado. O [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) distribui recomendações de resposta a incidentes ao longo da gestão de risco de cibersegurança descrita pelo [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework/faqs). As funções `Govern`, `Identify`, `Protect`, `Detect`, `Respond` e `Recover` do framework — governar, identificar, proteger, detectar, responder e recuperar — são atividades concorrentes e contínuas. Uma equipe não deve esperar por “responder” para pensar em donos, cópias de segurança, comunicações ou evidência.

Há uma distinção importante entre uma **função usada para preparar a resposta** e uma **ação tomada durante um caso particular**. O modelo do [NIST SP 800-61 Rev. 3, seção 2.1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) coloca `Govern`, `Identify` e `Protect` na preparação ampla e na gestão de risco; `Detect`, `Respond` e `Recover` descrevem as atividades de resposta voltadas ao caso. A categoria de melhoria liga as lições de volta a todas elas. Isto é um modelo para organizar resultados, não uma exigência de que todo caso atravesse seis passos isolados. Na Harbor Library, nomear um responsável autorizado pelo serviço pertence à prontidão; conferir a edição de reserva de hoje pertence à investigação; decidir se uma conta deve ser restringida pertence à resposta. Um tíquete de melhoria depois do exercício pode alterar a lista de contato do responsável antes do próximo caso.

Quem começa pode testar a prontidão com quatro perguntas: **Qual serviço pode ser prejudicado? Quais registros poderiam mostrar o que aconteceu? Quem pode aprovar uma ação disruptiva? Que resultado mostraria que o serviço normal pode ser retomado com segurança?** Uma equipe que não consegue respondê-las tem trabalho a fazer mesmo que o sistema de alerta seja excelente. Por outro lado, respondê-las não estabelece que um alerta particular seja malicioso. A distinção impede que um inventário de controles seja confundido com um achado de incidente.

Considere uma biblioteca pequena que oferece reserva de salas pela internet. Um alerta pode dizer que uma conta de administrador entrou numa hora incomum. Isso é um **sinal** que vale examinar. Por si, não prova comprometimento da conta. Uma mudança na base de reservas pode ser um **evento** com efeito de negócio. A equipe precisa avaliar contexto, evidência e impacto antes de rotular a situação como **incidente** confirmado. Estas são definições de trabalho para este caso de ensino; uma organização deve usar a própria política aprovada de classificação.

A primeira pergunta útil é: **Qual serviço e quais pessoas podem ser prejudicados, e o que se sabe agora?** Uma equipe que registra a incerteza pode agir depressa sem fingir que conhece a causa-raiz. Uma equipe que rotula todo alerta como “violação” arrisca interrupção desnecessária; uma equipe que descarta todo alerta arrisca contenção tardia.

#### 1.2 Um mapa fictício de serviço

O curso usa a **Harbor Library**, uma organização fictícia. Não há registros pessoais nem rede real. Moradores reservam salas de estudo por um site. A equipe da recepção pode editar reservas. Uma lista separada de boletim de eventos contém endereços de contato. O serviço de reserva depende de uma aplicação web, de um serviço de identidade, de uma base de dados, de uma cópia noturna e de uma central de atendimento da equipe.

| Dependência do serviço | Por que importa | Quem consultar | Evidência útil durante um incidente |
|---|---|---|---|
| Aplicação de reservas | Moradores e equipe criam ou alteram reservas | Responsável pelo serviço | Logs de pedido e histórico de mudança |
| Serviço de identidade da equipe | Controla quem pode editar reservas | Administrador de identidade | Registros de entrada e mudanças de conta |
| Base de reservas | Guarda a agenda atual | Responsável pelos dados | Log de auditoria e estado da cópia de segurança |
| Cópia noturna | Sustenta a restauração | Responsável pela recuperação | Última execução bem-sucedida e teste de restauração |
| Central de atendimento | Recebe relatos de usuários | Coordenação da resposta | Horários de tíquete e sintomas relatados |

Este mapa é incompleto de propósito. Não diz se a aplicação usa hospedagem de terceiros, como os relógios são sincronizados, nem quem pode aprovar uma interrupção de serviço. Uma equipe de resposta deve registrar isso como **lacunas de prontidão** antes de uma crise. Se uma dependência falhar, a equipe pode então pedir evidência e opções ao dono correto.

##### Do mapa de dependências ao contrato de prontidão de evidência

Um mapa de serviço nomeia componentes e donos; **não** mostra que um investigador conseguiria responder a uma pergunta específica a tempo. Um passo útil seguinte é um **contrato de prontidão de evidência**: um acordo curto e testável sobre qual fonte registraria um evento, o que os campos significam, quem pode recuperá-lo, por quanto tempo um registro útil pode permanecer disponível e como um segundo analista poderia reproduzir a seleção. Isto é um dispositivo de ensino da OpenCyber Academy, não um formulário exigido pelo [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). A orientação de resposta a incidentes do NIST coloca preparação, conhecimento do serviço e papéis de resposta dentro da gestão de risco mais ampla; o contrato abaixo transforma essa orientação geral num exercício pequeno de biblioteca fictícia.

Comece por uma **pergunta de decisão**, não pelo nome de um produto. Os registros de prática introduzidos na seção 1.7 incluirão uma reserva cancelada B18 e a conta `desk-a`; trate-os aqui como prévia. “Temos logs?” é amplo demais. “O cancelamento de B18 foi uma ação aprovada da equipe, e o estado atual da reserva o refletiu?” separa uma pergunta de atividade de uma pergunta de estado de negócio. Uma auditoria de reserva poderia registrar uma edição, mas uma comparação de estado autoritativo seria necessária para confirmar o que os usuários podem reservar agora. Do mesmo modo, um serviço de identidade poderia relatar que a conta `desk-a` entrou, enquanto nem o rótulo da conta nem um carimbo de tempo identificam a pessoa no teclado. O plano de evidência deve dizer o que uma fonte consegue *discriminar* e qual conclusão tentadora ela não pode carregar.

Para cada pergunta, escreva seis campos **antes** do incidente: (1) o produtor e o evento que ele deveria emitir; (2) identificadores que possam ligar registros sem fundir em silêncio pessoas ou ações diferentes; (3) hora do evento, hora da coleta e premissas de relógio ou fuso; (4) o custodiante, o caminho aprovado de coleta e o limite de acesso; (5) retenção esperada e indicadores de falha; e (6) um ensaio pequeno e autorizado que possa mostrar se a fonte de fato funciona. Campos em branco ou não testados permanecem **desconhecidos**. Um diagrama que mostra uma seta de log sem esses detalhes é uma hipótese de arquitetura, não prova de cobertura.

O que segue é um **cartão de desenho D1 proposto**, escrito para uma versão isolada de treinamento da Harbor Library. É um plano do que os donos testariam, **não** um registro novo da série R, nem uma descrição da configuração real de log da biblioteca, nem evidência disponível no marco das 09:05. Nomes de campo como `request_id` e `session_id` são campos candidatos de desenho; a existência e a semântica deles precisam ser conferidas antes de uma correlação real.

| Pergunta de decisão | Fonte proposta e campo de junção a verificar | Custodiante e verificação permitida | Alegação que continua bloqueada sem a verificação |
|---|---|---|---|
| Que valor de reserva mudou e qual é o valor aprovado atual? | Registro de mudança da aplicação chaveado por identificador de reserva e de pedido; cópia restrita do estado atual comparada com um alvo aprovado pelo responsável. | O custodiante da aplicação fornece uma seleção limitada de auditoria; o responsável pelo serviço aprova o alvo e a comparação de estado. | Um registro de edição, sozinho, não prova o estado presente nem se a mudança foi autorizada. |
| Uma sessão de equipe esteve associada a essa ação da aplicação? | Registro de sessão de identidade e registro da aplicação; testar se ambos usam o mesmo espaço de chave de sessão e a mesma base de tempo. | O administrador de identidade e o custodiante da aplicação fornecem só os campos permitidos depois da aprovação do líder do incidente. | Um rótulo de conta coincidente ou um horário próximo não identifica uma pessoa, uma intenção nem um nexo causal. |
| Que dano visível ao usuário tem suporte? | Relato da central de atendimento com a hora de recebimento, mais uma comparação autorizada entre a visão do frequentador e o estado aprovado da reserva. | A central recebe relatos; o responsável pelo serviço define uma verificação de impacto estreita e atenta à privacidade. | Um único relato não mede todos os frequentadores afetados; uma linha correta da base, sozinha, não prova que a exibição estava correta. |
| O serviço de reserva poderia ser restaurado com dados corretos? | Manifesto da cópia, cópia candidata, resultado de restauração isolada e comparação com a agenda aprovada. | O responsável pela recuperação testa uma cópia autorizada; o responsável pelo serviço aceita ou rejeita o resultado. | Um trabalho de cópia concluído não demonstra duração da restauração, correção das reservas nem aceitação do serviço. |

O cartão de quatro linhas é um **resumo**, não um contrato de seis campos concluído. Para a primeira linha, um *registro de teste proposto* plenamente especificado leria como segue. Os nomes de campo, os horários e as observações esperadas são inventados para um ensaio isolado futuro; nenhum é alegado como existente em R1–R8.

| Campo do contrato | Entrada proposta a conferir antes de confiar nela |
|---|---|
| Produtor e evento | Perguntar ao custodiante da aplicação se uma mudança de reserva, inclusive uma feita por uma rota alternativa de escrita, emite um evento de auditoria distinto. O nome do evento e a cobertura não estão verificados. |
| Identificadores de junção | Testar se o identificador da reserva e o do pedido estão presentes e são únicos para esta ação. Não juntar um registro de identidade só pelo nome de usuário ou por horário próximo; qualquer chave de sessão precisa de um espaço de nomes compartilhado demonstrado. |
| Base de tempo | Registrar à parte o carimbo original do evento e o fuso, a hora de recebimento do coletor e a hora da consulta do analista. A tolerância de relógio e o comportamento de chegada tardia permanecem desconhecidos até serem medidos. |
| Custódia e acesso | Obter aprovação do líder do incidente para uma seleção restrita, pelo custodiante da aplicação, da reserva sintética de teste no intervalo 09:59–10:03 UTC. Manter a lista do boletim, que não tem relação, fora do escopo. |
| Retenção e sinais de falha | Pedir ao custodiante que demonstre o evento de teste mais antigo recuperável, o atraso do coletor e um indicador visível de falha. Até essa verificação, não escreva uma garantia de retenção nem chame uma consulta vazia de completa. |
| Ensaio falseável | Se um teste isolado for aprovado, pré-declare uma edição sintética às 10:00 UTC e um controle fora do intervalo às 10:10 UTC. Espere só a primeira dentro da consulta limitada; guarde o filtro exato, a hora de execução e qualquer campo ausente ou falha de coleta. Isto é um procedimento proposto, não um resultado relatado. |

O cartão de decisão de quatro linhas é, de propósito, **de dois lados**. Nomeia uma fonte e, em seguida, nomeia o que ainda seria desconhecido depois de vê-la. Isso impede o salto familiar de “o log existe” para “a pergunta foi respondida”. A primeira linha também distingue um *registro de atividade* de um *registro do estado do mundo*. Se uma auditoria da aplicação diz que B18 foi cancelada, mas a cópia restrita do estado atual falta, o analista pode relatar o cancelamento registrado e pedir a comparação de estado. O analista não pode certificar a agenda ao vivo só pela auditoria. A segunda linha antecipa o exercício de correlação do módulo 2 da edição inglesa, que não está neste manuscrito: mesmo uma correspondência exata de chave de sessão, se fosse fornecida, estreitaria uma relação entre registros, não a identidade nem a autorização de uma pessoa.

**Trace onde uma observação pode se perder.** Um resultado de busca ausente tem várias causas diferentes. O produtor pode nunca emitir o evento; um evento emitido pode falhar na coleta; um registro coletado pode chegar depois da consulta; um registro disponível pode já ter expirado; controles de acesso podem negar a visão selecionada; a consulta pode usar o identificador de reserva, o fuso ou a janela de tempo errados; ou um revisor pode ler mal uma linha real. A resposta a essas falhas difere. Repetir a mesma consulta não repara a não emissão, e pedir uma exportação ampla não substitui corrigir um filtro errado. Uma revisão de prontidão registra, portanto, o *último ponto confirmado* no caminho do produtor até quem estuda, e um dono nomeado para a próxima verificação. Não reduza todo resultado vazio a “o sistema não teve atividade”.

**Torne um ensaio falseável.** Numa cópia isolada de treinamento, explicitamente aprovada, um dono poderia pré-declarar uma mudança sintética de reserva e um evento de controle deliberadamente fora do intervalo. O custodiante da aplicação registraria o identificador do pedido de teste e a hora UTC do evento; o coletor registraria a hora de recebimento e a fonte; o analista executaria uma consulta limitada e guardaria o filtro exato e a hora de execução. O resultado esperado é a mudança dentro do intervalo e os campos combinados, com o controle fora do intervalo excluído pelo intervalo declarado. Se a linha esperada falta, a equipe investiga emissão, transporte, retenção, acesso e escopo da consulta, nessa ordem. Se a linha fora do intervalo aparece, o filtro ou a interpretação do tempo precisa de correção. Passar neste ensaio pequeno mostra apenas que o caminho e o intervalo testados se comportaram como declarado. Não prova que todos os eventos futuros serão coletados, nem que o evento prova por que uma pessoa agiu.

A evidência do ensaio deve incluir os **casos negativos e de falha**, não só uma captura de painel bem-sucedida. Uma cópia de um resultado de busca sem fonte, filtros e limite de coleta pode ser impossível de reproduzir. O carimbo da fonte e a hora em que o analista descobriu o registro devem ocupar campos separados; caso contrário, um registro atrasado pode parecer ter ocorrido mais tarde do que ocorreu. O plano também deve dizer como um erro de fonte é notado: por exemplo, um evento de teste esperado ausente, um recebimento de coleta atrasado, uma mudança de esquema ou uma janela de retenção expirada. O módulo 2 da edição inglesa, ausente deste arquivo, exercita essas distinções com registros sintéticos. Elas pertencem à prontidão porque quem responde não pode reconstruir um registro que nunca foi retido.

**Escopo e privacidade seguem a pergunta.** A pergunta sobre reservas não autoriza abrir a lista separada do boletim. O cartão D1 nomeia os campos mínimos de reserva e de sessão a pedir, os custodiantes que poderiam fornecê-los e a aprovação a buscar. Se uma observação posterior e sustentada levantar uma preocupação de exposição de dados, o líder do incidente e o contato de privacidade podem definir um propósito e um limite novos. Coletar um histórico inteiro de identidade ou a base de frequentadores só porque isso é tecnicamente acessível ampliaria o caso e o número de pessoas expostas a esses registros. Um bom plano de evidência torna a menor seleção útil reproduzível e registra o que ela excluiu. As regras exatas de retenção, acesso e privacidade de uma organização real devem vir da própria política e das obrigações aplicáveis; este cartão fictício não as fornece.

Depois de ler o conjunto de dados na seção 1.7, aplique o contrato ao **instantâneo real do módulo 1** sem importar D1 como evidência. R1 relata uma entrada de `desk-a`, mas não há dispositivo, semântica de chave de sessão nem pessoa. R3 e R4 registram edições de reserva, mas a tabela fornecida não contém um alvo aprovado pelo responsável nem uma comparação fresca de estado autoritativo. R5 registra o relato de um frequentador, não uma contagem de todos os usuários afetados. R6 agenda treinamento, mas não lista as tarefas de reserva aprovadas. R7 relata um trabalho de cópia concluído, não uma restauração isolada. R8 carece explicitamente de detalhe de destino, portanto não pode estabelecer ausência de transferência de dados. Às 09:05 o analista pode abrir um caso limitado, preservar os ponteiros fornecidos e pedir aos donos nomeados os discriminadores que faltam. O analista não pode alegar que os campos de log ou os ensaios propostos em D1 já estavam implementados.

Um contrato de prontidão de evidência só é útil se alguém for dono da sua **manutenção**. Uma mudança de serviço pode renomear um campo de reserva, dividir um caminho de escrita, mover um produtor de log ou encurtar a retenção. O dono então repetiria o teste autorizado e atualizaria a fonte, o significado e a rota de coleta do contrato. O documento deve mostrar o último escopo testado e o próximo gatilho de revisão; um estado antigo “verde” sem esses detalhes é mais fraco do que um desconhecido atual e explícito. Isto liga o mapa de serviço do módulo 1 ao tratamento de evidência do módulo 2, às verificações de controle e recuperação do módulo 3 e às melhorias pós-ação do módulo 4, todos da edição inglesa e fora deste manuscrito. Continua a ser um artefato de preparação, não um substituto da evidência do caso nem de uma investigação concluída.

##### Testar se a prontidão é utilizável

Uma equipe de resposta pode possuir uma política, uma lista de contatos, software de monitoramento e cópias noturnas e ainda assim ser incapaz de tomar uma decisão segura sob pressão. A existência de um componente diz pouco sobre se a equipe consegue usá-lo corretamente quando um serviço particular está ameaçado.

Uma alegação prática de prontidão deve ter cinco partes: **capacidade**, **dono**, **permissão**, **teste** e **resposta à falha**. Por exemplo, “temos logs de reserva” é uma frase de inventário. Uma frase verificável de prontidão é: “o custodiante da aplicação pode, com a aprovação do líder do incidente, recuperar mudanças de reserva para um identificador e um intervalo de tempo especificados; outro revisor pode conferir a fonte, os filtros e a saída; se a linha de teste esperada estiver ausente, o custodiante investiga coleta e retenção em vez de alegar que não houve atividade.”

Esta distinção importa porque um sucesso técnico aparente pode esconder resultados de negócio fracassados. Um indicador verde de saúde da web pode representar uma página inicial que responde enquanto uma escrita de reserva falha. Um estado bem-sucedido de trabalho de cópia não demonstra que uma base restaurada contém a agenda correta. Um registro de entrada estabelece que o sistema produtor relatou um evento de conta; não estabelece uma identidade humana.

O [NIST Cybersecurity Framework 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) descreve resultados de cibersegurança em `Govern`, `Identify`, `Protect`, `Detect`, `Respond` e `Recover`. O [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integra recomendações de resposta a incidentes com a gestão de risco organizacional. Nenhuma das fontes autentica as observações fictícias da Harbor Library nem especifica os cartões deste exercício. A implicação de ensino é examinar se os resultados desejados pela organização podem de fato ser demonstrados.

Considere os resultados contrastantes de ensaio a seguir:

| Prontidão alegada | Evidência fraca | Demonstração mais forte, ainda limitada |
|---|---|---|
| Um dono pode autorizar interrupção | Um nome de dono aparece num documento | Um papel autorizado aceita ou rejeita um pedido fictício de escopo preciso, com motivo e hora de revisão |
| Mudanças de reserva podem ser reconstruídas | Existe um painel | Um custodiante devolve uma edição sintética pré-declarada, o identificador da fonte, a hora original e a seleção exata; um controle fora do intervalo é excluído |
| Cópias sustentam a recuperação | R7 relata a conclusão do trabalho | Uma restauração isolada, autorizada e separada, é comparada com um estado de reserva aprovado pelo responsável; **não realizada na Rodada A** |
| Um incidente pode ser passado adiante | Um tíquete diz “em investigação” | Um segundo revisor identifica de forma independente observações, desconhecidos, escopo, decisões propostas e donos |

Os testes de prontidão devem expor as próprias limitações. Passar num ensaio de recuperação valida o caminho e o intervalo testados, não todo coletor, conta ou dia futuro. Uma aprovação assinada para uma mudança simulada não estabelece autoridade para fazer qualquer outra mudança.

<a id="w1-review-01"></a>

#### Unidade de revisão da semana 1, número 1 — Conferir o contrato de entrada antes de interpretar o resultado

##### Objetivo e distinção

Estas cinco unidades suplementares de revisão estendem as aulas 01–05 já existentes; não criam aulas diárias novas nem substituem EX001–EX050. Todos os casos e programas usam peças fictícias ou em memória. Para cada extensão executável, rode primeiro o laboratório nomeado completo numa sessão nova de Python. Para AR1, rode também a listagem de aprovação presa ao pedido antes do portão de tipo. Não se conecte a sistemas de produção nem trate resultados de peça como autorização.

Depois desta unidade, explique por que um cálculo correto de um programa pode ainda ser irrelevante para a pergunta de incidente pretendida. Identifique três coisas separadas: **a versão de fonte selecionada**, **o quadro de entrada declarado** e **a proposição exata em teste**.

A aula 01 já ensina um contrato de prontidão de evidência: nomear uma pergunta útil, uma fonte, um custodiante, condições de coleta e um ensaio. O passo adicional aqui é testar a fronteira entre esse contrato e a entrada de fato entregue a um verificador. Uma tabela pode ser internamente bem formada e ainda pertencer a outra versão ou omitir um objeto exigido pela decisão.

Um **ponteiro de fonte** identifica onde o leitor deve olhar. Por si, não estabelece a verdade, a completude nem a aplicabilidade do que se encontra. Um **quadro de entrada declarado** afirma quais objetos a comparação atual deve cobrir. Não é evidência de que o quadro inclui todo objeto relevante de produção. Uma **proposição de teste** afirma a condição estreita que o programa pode avaliar depois que essas entradas são aceitas.

Por exemplo, o programa original BSL1 pode inspecionar intervalos de reserva fornecidos. Não pode determinar sozinho se um exportador omitiu uma reserva, se a política foi aprovada para o serviço relevante, ou se as linhas descrevem o incidente atual. Essas perguntas não se tornam verdadeiras porque a função de sobreposição executa corretamente.

##### Uma revisão em três estágios

~~~text
Aceitar o contrato de entrada declarado?
    não -> rejeitar ou pedir esclarecimento; sem aprovação de negócio
    sim
     |
     v
Avaliar o modelo declarado sobre essas entradas
     |
     v
Relatar o resultado dentro desse escopo
    + nomear o que a fonte e o modelo não podem estabelecer
~~~

**Explicação do texto:** o primeiro estágio confere se a entrada pode ser usada sob este contrato particular. O segundo aplica a regra declarada. O terceiro impede que um cálculo estreito se torne um achado de incidente sem suporte. Nenhuma das setas autentica um produtor, estabelece autorização ou fornece um registro ausente.

Comece por congelar o quadro esperado antes de olhar o resultado. Suponha que um revisor receba um quadro BSL1 declarado de seis objetos, S01–S06. Um segundo arquivo contém só S01 e relata ausência de conflito. Esse resultado pode estar correto **para S01 sozinho**. Não pode responder à pergunta de seis objetos, a menos que os cinco objetos ausentes sejam contabilizados. Redefinir em silêncio o quadro esperado para coincidir com o arquivo devolvido mudaria a pergunta depois de ver a resposta.

Em seguida, inspecione o significado do campo, não só a presença do campo. Um campo chamado `confirmed` pode conter um booleano, texto, um inteiro ou nenhum valor. Um valor que uma linguagem de programação trata como verdadeiro não é necessariamente uma afirmação afirmativa sob o esquema do exercício. A unidade 4 torna essa diferença executável.

Por fim, inspecione a frase que o analista escreve. Mesmo um ponteiro autêntico de R4 sustenta o fato de que um cancelamento foi registrado; não fornece aprovação, o ator humano nem uma comparação fresca de estado de reserva aprovada pelo responsável. Verificação de tipo não é prova semântica. Por outro lado, uma entrada malformada não é evidência de que ocorreu uma mudança maliciosa. É um motivo para interromper essa comparação e buscar uma fonte utilizável.

##### Exemplo resolvido

Uma nota de revisão proposta diz: “O verificador não devolveu achados, portanto as seis reservas estão seguras.” A entrada anexa contém só S01. O primeiro erro é um **descompasso de quadro**, antes de qualquer pergunta sobre se o cálculo de sobreposição está correto. O segundo erro é promover um resultado de peça a segurança do serviço. Uma substituição defensável é: “Não se encontrou sobreposição na comparação declarada de uma linha; esta entrada não responde à pergunta de ensaio de seis linhas nem estabelece um estado real de serviço.”

Para responder à pergunta original, o revisor deve reter a entrada de uma linha e o seu resultado, pedir o quadro ausente ou uma revisão explícita de escopo aprovada pelo responsável, e executar de novo a comparação relevante. Não invente as linhas ausentes, não infira que foram apagadas e não sobrescreva o primeiro resultado.

##### Prática suplementar W1-R1

**Objetivo:** separar a admissibilidade da entrada do significado de um resultado calculado. **Entradas:** os três relatórios abaixo, a limitação original de R4 e o quadro BSL1 de seis objetos descrito acima. **Artefato exigido:** três linhas contendo a decisão de admissibilidade, a afirmação estreita sustentada, a evidência ausente e o próximo pedido limitado. **Restrições:** nenhum fato novo da série R; nenhuma coleta de produção; reter tanto a entrada submetida quanto o escopo declarado.

| Relatório | Material fornecido |
|---|---|
| A | Quadro declarado S01–S06; só S01 fornecido; o verificador imprime ausência de achados. |
| B | Quadro declarado só S01; S01 fornecido; o verificador imprime ausência de achados. |
| C | R4 é citado corretamente, mas o autor conclui que uma pessoa identificada fez um cancelamento aprovado. |

**Avaliação:** um ponto por cada linha raciocinada corretamente, um por distinguir um quadro ausente de um achado negativo, e um por preservar a fronteira do caso canônico. Cinco pontos avaliam só esta tarefa suplementar. Uma alegação de aprovação real, de atribuição humana ou de estado seguro de produção exige correção, qualquer que seja o total. [Resolução](#w1-answer-01).

*Rubrica:* 3 = cinco pontos da fonte: três linhas corretas, distinção entre quadro ausente e achado negativo, e fronteira canônica preservada;; 2 = a maior parte desses pontos, com uma omissão de limite;; 1 = responde, mas omite fonte, limite ou a fronteira do caso;; 0 = nenhum.

##### Síntese da revisão

Uma entrada utilizável, um cálculo correto e uma conclusão operacional justificada são conquistas diferentes. Preserve a fronteira entre elas.

#### Marco resolvido

R1 registra uma entrada bem-sucedida de conta; R3 e R4 registram mudanças de reserva. Os registros estabelecem a sequência, enquanto a identidade da pessoa e a aprovação das mudanças permanecem desconhecidas. A primeira decisão é uma pergunta limitada ao responsável, não um veredito de comprometimento.

#### Prática — Aula 01

##### EX001 — Observação ou inferência

**Objetivo:** separar o conteúdo de um registro de uma explicação desse conteúdo. **Entradas:** R1, R3, R4, R5 e R7, todas dentro da liberação R1–R8 da Rodada A às 09:05. Estes são os ponteiros exatos de fonte para as quatro afirmações; não use R9 nem qualquer resultado posterior do caso. **Saída:** uma tabela de quatro linhas com afirmação, classificação, registro de suporte e uma frase que descreva o limite do registro. Classifique: (a) “R4 registra um cancelamento de B18”; (b) “`desk-a` foi comprometida”; (c) “R5 relata que B18 desapareceu”; (d) “R7 prova que o serviço pode ser restaurado em dez minutos.” Use as categorias observação direta, hipótese que exige confirmação e conclusão sem suporte. Uma nota 2 exige distinguir o *fato de um relato de frequentador* de uma prova independente da experiência completa do frequentador.

**Extensão:** Para cada afirmação original, reescreva qualquer conclusão sem suporte na formulação defensável mais estreita. Acrescente uma fonte que seria necessária para elevar a alegação.

**Para crédito completo:** Uma resposta de 2 pontos deve distinguir “R5 registra um relato de frequentador” de “a interface de reserva foi provada incorreta de forma independente”, e “R7 relata a conclusão da cópia” de “a recuperação foi testada”. Selecionar apenas um rótulo, sem uma frase de limite, obtém no máximo 1.

**Resolução:** [EX001 no apêndice final](#ex001--worked-result).

*Rubrica:* 3 = nota 2 da fonte: quatro linhas com classificação, registro e limite; distingue o relato de R5 de prova independente da experiência, e a conclusão da cópia em R7 de recuperação testada;; 2 = as quatro linhas existem, mas falta um limite exigido para a nota 2;; 1 = responde à pergunta, mas omite fonte, limite ou a frase que restringe a alegação;; 0 = nenhum.

<!-- open-cyber-academy:lesson-navigation:start lesson-01 -->
#### Continue estudando — aula 01 de pelo menos 20

[← Visão do curso](../../README.md) · [Índice de aulas do curso](../SUBJECTS.md) · [Aula 02 →](#lesson-02)

Siga para a próxima aula diária escrita neste manuscrito.
<!-- open-cyber-academy:lesson-navigation:end -->
<a id="lesson-02"></a>

### Aula 02 — Invariantes de reserva e linhas de base de comportamento

**Semana 1, dia 2.** Percorra o ensino e o marco resolvido antes de tentar os exercícios indicados. Compare o seu artefato com a resolução final só depois.

#### 1.2a Comportamento normal de reserva e invariantes de serviço

##### O que significa um serviço funcionar corretamente?

A prontidão para incidentes é mais fácil de discutir quando a organização consegue explicar o que o serviço promete a usuários legítimos. Uma página web pode responder enquanto a função por trás dela está errada. Num serviço de sala de estudo, um frequentador pode ver uma confirmação e não obter uma sala válida, ou ver um cancelamento enquanto a sala permanece indisponível para outra pessoa. Essas situações têm causas operacionais diferentes, mas ilustram um problema comum de preparação: saber que o software está alcançável não basta para especificar um resultado de negócio correto.

O capítulo 01 atual identifica a aplicação de reservas, o serviço de identidade da equipe, a base de dados, a cópia de segurança e a central de atendimento. Esse **mapa de serviço** nomeia componentes e donos. O contrato D1 de **prontidão de evidência** pergunta qual fonte poderia registrar um evento relevante, o que os campos significam e se a equipe conseguiria recuperá-lo com responsabilidade. A pergunta separada desenvolvida aqui é: **Que condição observável significaria que o serviço de reserva atendeu a um requisito de negócio definido?**

Uma **linha de base de comportamento** é uma descrição documentada de operação aceitável numa versão e num contexto especificados. Pode identificar quais estados de reserva são válidos, quando uma sala está ocupada, se um cancelamento libera um horário, como tempos sobrepostos são tratados e o que deve acontecer com um pedido inválido. O dono da regra precisa estar claro. Quem responde não deve inventar a política de reserva durante um incidente só para fazer uma teoria preferida caber nos dados.

Isto se relaciona a identificar serviços importantes e as consequências deles para o risco organizacional. O [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) organiza a gestão contínua de risco de cibersegurança, e o [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integra a preparação de resposta a incidentes com essas atividades de gestão de risco. Nenhuma das fontes prescreve as regras de reserva deste exemplo. As regras são deliberadamente fictícias, mas a disciplina de definir e testar um resultado de serviço é reutilizável.

No nível introdutório, quem estuda deve fazer três perguntas: Que tarefa legítima o usuário espera concluir? Que resultado seria inaceitável mesmo com a aplicação ainda alcançável? Quais condições precisam ser especificadas antes de julgarmos esse resultado? Uma resposta clara é mais útil do que um indicador verde de saúde sem explicação.

##### Trace a jornada do usuário legítimo antes de imaginar um atacante

Uma linha de base útil de comportamento começa com uma jornada normal de usuário. Num serviço hipotético da Harbor Library, um frequentador escolhe uma sala e um horário, envia um pedido, recebe uma resposta aceita ou rejeitada e mais tarde consulta a reserva resultante. Um membro autorizado da equipe pode mover ou cancelar essa reserva. A tabela canônica R1–R8 não especifica pontos de extremidade reais, regras de transação da base nem o fluxo completo de aprovação da organização, portanto esta jornada é um **modelo de ensino proposto**, não uma implementação verificada.

Divida a jornada proposta em resultados pequenos:

| Intenção do usuário | Resultado esperado sob uma política aprovada | Comportamento negativo que vale testar |
|---|---|---|
| Procurar um horário | Os horários disponíveis seguem as regras aceitas de ocupação da sala | Um horário ocupado e confirmado aparece como livre |
| Pedir uma reserva | Um pedido permitido e sem conflito recebe um resultado consistente | Uma reserva em conflito aparece como aceita |
| Alterar uma reserva | Só o objeto pedido e permitido muda | A reserva ou a sala errada muda |
| Cancelar uma reserva | O estado é registrado e a ocupação é atualizada sob a política | Uma sala cancelada permanece bloqueada sem justificativa |
| Revisar uma reserva | A visão reflete a reserva correta e as regras relevantes de atualização | Uma reserva obsoleta ou sem relação é exibida |

A tabela não estabelece que qualquer desses erros ocorreu no caso canônico. Descreve as **perguntas que um ensaio aprovado pelo responsável poderia testar** antes de um incidente. Os critérios de comportamento devem ser definidos em palavras que um trabalhador da recepção consiga entender. Se o requisito não pode ser explicado sem o nome de um framework de programação ou de um produto de base de dados, pode estar preso demais ao detalhe de implementação para expressar a promessa real ao usuário.

Note também que os resultados positivo e negativo são diferentes. Mostrar que uma reserva ordinária tem sucesso não mostra que uma sobreposição inválida será rejeitada. Mostrar que um cancelamento devolve uma resposta de sucesso não mostra que a sala correta ficou disponível. A prontidão exige um conjunto pequeno de perguntas independentes, não uma demonstração vagamente bem-sucedida.

A jornada deve incluir os seus *limites*: o tipo de sala pretendido, o período de tempo testado, os papéis permitidos e o que conta como reserva concluída. Uma biblioteca pode ter salas compartilhadas ou reservas provisórias, mas essas capacidades não estão especificadas no exercício. Quem estuda não deve assumi-las só para explicar um problema observado.

##### Converta expectativas vagas em invariantes testáveis

Um **invariante** é uma propriedade que deve permanecer verdadeira sempre que as condições declaradas se aplicam. Para uma sala de estudo simplificada de ocupação única, uma regra plausível é que duas reservas **confirmadas** não devem ocupar intervalos de tempo sobrepostos na mesma sala. Uma segunda regra pode ser que uma reserva cancelada não ocupa o horário antigo. Uma terceira pode exigir que todo intervalo aceito termine depois de começar.

Um invariante só é útil com um contrato completo:

1. **Escopo:** Quais salas, estados, representação de tempo e versão da aplicação a regra cobre?
2. **Pré-condições:** O que precisa ser verdadeiro antes de aplicar a regra?
3. **Comportamento esperado:** Quais valores são válidos e quais devem falhar?
4. **Verificação:** Que resultado demonstraria conformidade para as entradas selecionadas?
5. **Significado da falha:** O que se pode concluir quando a verificação falha, e o que permanece incerto?

Para a peça de ensino BSL1, o escopo é estreito de propósito: um dia fictício, salas de ocupação única, dois estados reconhecidos e seis objetos sintéticos de reserva. Outros significados de estado e regras de compartilhamento de sala não são inventados em silêncio. O invariante se aplica só a este modelo.

Uma regra testável é melhor do que “o sistema não deve cometer erros”. Por exemplo: “Sob a regra de ocupação única, nenhuma duas linhas confirmadas com a mesma sala podem ter intervalos de tempo semiabertos que se intersectem.” A regra especifica tanto os objetos quanto a condição. Também fornece um falseador: um par corretamente interpretado de intervalos confirmados, da mesma sala e sobrepostos, violaria a política declarada.

Esse achado ainda não identificaria a causa. Poderia resultar de um defeito de programação, de uma ação administrativa, de uma condição de corrida, de um erro de dados de teste ou de uso indevido. O invariante trata da **consistência do estado de negócio**. Um achado de incidente de segurança exige uma investigação separada de autorização, mecanismo e impacto.

Essa separação permite ao analista declarar um problema técnico útil sem alegar mais do que a evidência sustenta: “O modelo fornecido contém uma sobreposição que viola a regra declarada de ocupação” é defensável para a peça; “o atacante roubou uma conta da equipe e corrompeu as reservas” não é.

##### Os limites de tempo fazem parte da semântica do serviço

Reservas de sala são compromissos baseados em tempo. Se uma reserva usa a Room A das 09:00 às 10:00 e outra usa a sala das 10:00 às 11:00, os limites de tempo se encontram, mas não necessariamente conflitam. Se a primeira termina às 10:30, a segunda a sobrepõe. Uma política precisa especificar como trata inícios e fins.

O laboratório BSL1 usa **intervalos semiabertos**, em que o início está incluído e o fim está excluído. Em notação matemática isto é [início, fim). Sob esta convenção de ensino, uma reserva 09:00–10:00 não conflita com uma reserva 10:00–11:00. Uma reserva 09:00–10:30 conflita com uma reserva 10:00–11:00. Uma linha que começa e termina às 11:00 tem duração zero e é inválida.

A condição de sobreposição para dois intervalos válidos é: o primeiro começa antes de o segundo terminar **e** o segundo começa antes de o primeiro terminar. Comparar só se os horários de início são iguais perde intervalos sobrepostos com inícios diferentes. Tratar ambos os extremos como inclusivos cria relatos falsos de conflito para reservas adjacentes sob a convenção declarada.

Esses detalhes importam na operação. Um limite de tempo inválido pode criar um defeito de agenda visível ao usuário enquanto a aplicação está tecnicamente responsiva. Uma discrepância pode resultar de erros ordinários de implementação, de uma política incorreta ou de um fuso incompatível, e não de comportamento malicioso deliberado.

Uma aplicação real também precisaria definir horário de funcionamento, fusos, transições de horário de verão e reservas que cruzam a data. O laboratório inicial evita de propósito essas dimensões extras ao usar um dia fictício fixo com horários HH:MM. Isso evita implicar que um analisador curto de ensino seja uma implementação de agenda de produção.

Mantenha também o **horário da reserva** distinto do **horário da evidência do incidente**. R1 e R3 contêm carimbos de evento de fonte usados para entender o caso canônico. Os intervalos de sala do BSL1 descrevem horários em que um cliente poderia ocupar um espaço. Um tipo de tempo não substitui o outro. Um evento de fonte às 08:43 não significa que a reserva alterada estava marcada para 08:43.

##### O estado de uma reserva muda a interpretação do intervalo

Considere dois registros para a mesma sala e o mesmo horário. Se ambos estão confirmados, a política simplificada vê um conflito. Se um está cancelado, o registro cancelado já não ocupa o horário sob esta regra. Contar toda linha histórica como ativa produziria falsos positivos; tratar todo estado desconhecido como inofensivo poderia esconder conflitos reais.

BSL1 reconhece exatamente dois estados: **CONFIRMED** e **CANCELLED**. Reservas confirmadas participam das comparações de ocupação; reservas canceladas não participam. Outros valores não são mapeados automaticamente. Se uma mudança de sistema introduz um estado novo, o responsável pelo serviço deve explicar como ele afeta a ocupação, e o verificador deve ser atualizado sob um contrato versionado antes de se confiar num resultado.

Uma mudança de estado pode ser legítima ou não autorizada. O fato de o estado cancelado liberar uma sala **não** prova que o cancelamento foi aprovado. Também não estabelece que o usuário foi notificado ou que a auditoria histórica está completa. Isso exige testes e evidência separados. O R4 canônico original registra um cancelamento de B18, mas não contém um estado-alvo aprovado pelo responsável e não estabelece o comportamento atual de ocupação de B18.

A regra de estado é, portanto, um **auxílio de preparação**. Permite a uma equipe articular qual estado estaria correto *se* as condições aprovadas fossem conhecidas. Não pode transformar um evento impresso da aplicação num resultado de negócio verificado.

Uma pergunta útil de controle é: “Se a entrada de estado muda enquanto sala e horário permanecem constantes, qual resultado deve mudar?” A variante negativa posterior do BSL1 altera um item cancelado para confirmado e, com isso, introduz outra sobreposição. Isso mostra que o modelo é sensível ao campo de estado, em vez de gravar uma resposta preferida.

##### A aprovação de uma regra de negócio precisa ser versionada

O significado de uma reserva correta pode mudar. Uma biblioteca pode introduzir salas compartilhadas, alterar o horário de funcionamento, permitir retenções temporárias ou mudar o comportamento de cancelamento. Nessa situação, um teste que aplicou corretamente a regra do ano passado pode estar errado para o serviço aprovado de hoje.

Cada linha de base deve, portanto, carregar uma pequena **versão de livro de regras** e premissas aprovadas pelo responsável. Campos sugeridos incluem: versão, dono, data de vigência, funções afetadas, estados aceitos, categorias de sala, interpretação de tempo, amostras de entradas permitidas e proibidas, versão de implementação testada e um gatilho de revisão. Esses campos definem o comportamento correto de negócio; não substituem os campos de log de D1 nem a matriz de autorização da resposta a incidentes.

Imagine uma versão de linha de base que proíbe toda sobreposição na mesma sala. Uma versão futura pode distinguir salas de ocupação única de um espaço de estudo compartilhado. Uma colisão na sala compartilhada poderia então ser permitida segundo uma regra recém-aprovada. O processo responsável é reter ambas as versões, registrar por que a política mudou e retestar a regra nova de propósito.

Não reescreva a história aplicando uma política futura a uma decisão mais antiga sem dizê-lo. Um teste deve relatar qual versão conferiu e se essa versão se aplicava à operação examinada.

No registro canônico da Harbor Library, R6 mostra apenas que o treinamento da recepção estava agendado. Não fornece uma versão completa e aprovada de regra de reserva para B17 e B18. Quem estuda pode pedir a especificação de negócio relevante ao responsável pelo serviço, mas não pode afirmar que as regras do BSL1 já estavam ativas no ambiente fictício real da Harbor Library.

Quem começa deve entender a distinção entre “o programa está errado” e “a nossa expectativa documentada está errada”. Elas levam a passos seguintes diferentes. Corrigir o programa sem confirmar a política pode criar um erro novo; revisar uma política só para desculpar uma falha inexplicada pode ocultar um problema. Um contrato aprovado e um teste reproduzível ajudam um revisor a identificar qual premissa exige correção.

##### Violações de linha de base não provam comprometimento cibernético

Um alerta de segurança e um invariante de negócio falho podem aparecer juntos ou separados. Nenhum explica o outro automaticamente.

Suponha que um verificador isolado encontre duas reservas confirmadas sobrepostas na Room B. O resultado sustenta uma afirmação sobre essa peça sob a política escolhida. Não mostra que uma credencial da equipe foi roubada. Explicações possíveis incluem um defeito de lógica, uma importação malformada, um erro administrativo manual, um livro de regras desatualizado ou uma mudança intencional não autorizada. Cada explicação exigiria o próprio discriminador.

Por outro lado, uma sessão de conta não autorizada pode existir enquanto todo invariante de reserva ainda passa. Uma pessoa pode ver um registro não autorizado sem alterar uma reserva. Assim, a ausência de um problema de estado de negócio não prova a ausência de um problema de segurança.

Isto importa no primeiro marco de resposta. Um analista que observa uma entrada suspeita pode ser tentado a rotular qualquer erro posterior de reserva como obra do atacante. Mas proximidade temporal não é prova causal. R1 relata uma entrada bem-sucedida de desk-a, R3 e R4 relatam mudanças de reserva, e R5 registra uma preocupação de frequentador. Às 09:05, essas observações sustentam investigação; não fornecem uma explicação autenticada nem uma comparação de estado atual contra uma linha de base aprovada e completa.

Use um vocabulário de quatro níveis:

- **Requisito especificado:** o responsável pelo serviço definiu uma regra para um escopo declarado.
- **Peça avaliada:** um programa controlado aplicou essa regra a entradas de ensino selecionadas.
- **Discrepância operacional verificada:** uma comparação separada, autorizada e confiável, mostra que um serviço ao vivo não atendeu à regra aplicável.
- **Mecanismo de segurança estabelecido:** uma investigação independente liga a discrepância a uma causa não autorizada.

BSL1 alcança só o segundo nível. R1–R8 não provam o terceiro nem o quarto por associação com BSL1. Manter essas alegações separadas ajuda a equipe de resposta a investigar prontamente uma falha genuína de serviço sem acusar automaticamente um usuário nem minimizar uma preocupação possível de segurança.

##### Testes positivos, testes negativos e condições de controle

Um ensaio útil de prontidão não deve simplesmente buscar um resultado verde. Deve mostrar que entrada válida é aceita **e** que entrada inválida é rejeitada sob condições conhecidas.

O exemplo positivo do BSL1 consiste em reservas adjacentes. Uma reserva confirmada da Room A termina às 10:00, e outra reserva confirmada da Room A começa às 10:00. Sob a convenção semiaberta, o par não se sobrepõe.

O exemplo negativo primário contém reservas confirmadas da Room B para 09:00–10:00 e 09:30–10:30. Como os intervalos se intersectam, o verificador deve sinalizar um conflito.

Um segundo exemplo negativo é uma reserva confirmada com início e fim ambos às 11:00. A sala em si pode estar disponível, mas a reserva tem duração inválida. O teste de sobreposição não deve ser a única regra de aceitação.

O controle de cancelamento verifica uma premissa diferente. Um registro cancelado da Room A 09:00–10:00 é ignorado para ocupação ativa. Numa variante separada, mudar só esse estado para confirmado faz com que ele conflite com a reserva ativa existente. O teste revela por que o significado do estado é essencial.

Um terceiro teste de sensibilidade remove uma linha sobreposta de uma entrada de trabalho. O verificador agora relata menos problemas. Isso não significa que o sistema subjacente foi reparado; significa que o verificador já não vê todo objeto relevante. Num caso real, este é o risco de uma exportação filtrada ou incompleta do estado atual.

Cada um desses resultados precisa de uma limitação de escopo. Uma comparação bem-sucedida de intervalos adjacentes não diz nada sobre toda sala ou todo dia. Uma sobreposição sinalizada não é um impacto medido sobre frequentadores. Uma sobreposição ausente numa entrada incompleta não é prova de uma agenda segura.

##### Distinga falha de contrato, falha de entrada e ausência de fonte

Quando um verificador devolve um problema, quem estuda deve classificar que tipo de problema é.

Uma **falha de contrato** ocorre quando uma entrada interpretável viola a regra de negócio declarada — por exemplo, duas reservas válidas e confirmadas se sobrepõem na mesma sala de ocupação única.

Uma **falha de qualidade da entrada** ocorre quando os dados fornecidos não podem ser interpretados sob o contrato. Um intervalo de comprimento zero, um identificador de reserva duplicado ou um estado desconhecido não é necessariamente a mesma falha que uma reserva dupla. Pode refletir dados de teste malformados, um defeito do exportador ou um problema da aplicação a montante.

Uma **limitação de cobertura** ocorre quando registros relevantes estão ausentes do quadro de teste fornecido. Se uma linha sobreposta é omitida, o verificador pode relatar ausência de conflito apesar de a população maior permanecer inalterada. Isto não é uma demonstração de que a regra passou no escopo completo pretendido.

Essas categorias devem permanecer visíveis no resultado. Caso contrário, a equipe pode investigar o comportamento da aplicação quando na verdade precisa de uma verificação aprovada de qualidade da fonte, ou pode descartar um conflito genuíno como erro de exportador sem evidência.

O fato de uma asserção em Python ter sucesso não autentica a fonte da entrada. Para BSL1, isto é aceitável porque a peça é sintética de propósito. Uma comparação real aprovada pelo responsável exigiria, além disso, uma fonte declarada, seleção completa, carimbos de tempo, permissões de acesso e uma visão autoritativa do estado atual. Essas são perguntas separadas de evidência, cobertas por outros capítulos da edição inglesa e por D1; o laboratório de linha de base não as duplica.

Quem é novo deve conseguir explicar o resultado numa frase: “Nos dados BSL1 fornecidos, o verificador encontrou um conflito ativo de sala e uma duração inválida; as alegações mais amplas de correção limitam-se às seis linhas sintéticas e à política declarada.”

##### Uma interpretação errada e uma correta, em contraste

**Plausível, mas incorreta:**

> “R1 mostra que o atacante entrou. R3 e R4 mostram que o atacante mudou reservas. O nosso teste novo de reserva encontrou uma reserva dupla; portanto a Harbor Library sofreu um ataque confirmado que danificou a agenda.”

Isto funde conjuntos de dados sem relação e faz alegações causais sem suporte. R1 contém um rótulo de conta, não uma identidade humana verificada. R3/R4 registram operações sem estabelecer a autorização delas. O teste BSL1 usa objetos da série S sem relação com o caso da série R. Não pode ser tratado como evidência nova sobre B17 ou B18.

**Interpretação defensável de sala:**

> “No marco fictício das 09:05, R1–R8 justificam perguntar se as mudanças registradas de B17/B18 foram aprovadas e se o sintoma relatado pelo frequentador corresponde à agenda autoritativa. O operador, o escopo completo do treinamento e a correção atual do estado de negócio permanecem sem resolução. À parte, a peça BSL1 demonstra como definir e conferir dois invariantes de reserva em objetos inventados; essas verificações não fazem achado algum sobre o incidente da Harbor Library.”

A interpretação melhor identifica uma próxima pergunta válida e preserva a fronteira da fonte. Também evita dizer que uma ausência de achados BSL1 inocentaria a conta ou provaria que não houve exposição de dados. Um invariante de negócio é uma parte útil da prontidão, não um detector universal de segurança.

A edição atualizada oficial do [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) trata de avaliar sistemas e operações para requisitos e prioridades de contingência. Não define a política de reserva da Harbor Library nem confirma qualquer evento da série R. A aplicação de ensino aqui é que uma organização se beneficia de entender resultados críticos de serviço antes de uma interrupção, em vez de inventar um teste de correção só depois que algo parece suspeito.

##### Torne a linha de base portátil através de uma mudança de serviço

Uma regra deve permanecer compreensível quando o software ou a hospedagem muda. A frase “a consulta à base devolveu zero linhas” depende de uma implementação e de uma seleção particulares. A frase “duas reservas confirmadas de ocupação única não devem se sobrepor na mesma sala” expressa uma expectativa de negócio que pode ser avaliada por caminhos de teste autorizados diferentes.

Essa portabilidade sustenta a prontidão para incidentes. Se um serviço migra de um monólito para componentes separados, as fontes de log podem mudar. A promessa central de negócio pode permanecer estável. Uma linha de base de comportamento dá ao responsável pelo serviço um modo de reconhecer se a migração ainda produz resultados aceitáveis; D1 precisa ser atualizado à parte para identificar onde a evidência pode agora ser coletada.

Portabilidade não significa universalidade. Uma versão posterior do serviço pode alterar legitimamente a política. A regra precisa, portanto, de versão, escopo e histórico de mudança. Um bom teste pode relatar tanto o resultado esperado da política antiga quanto o resultado novo proposto, sem apagar o registro anterior de aceitação.

Considere uma atualização fictícia de software que muda a representação de reservas canceladas. Se uma linha de base passa de repente a sinalizar conflitos, a equipe deve primeiro conferir se entradas canceladas estão sendo contadas incorretamente como ativas ou se o significado efetivo do estado mudou. Essa é uma pergunta sobre alinhamento de contrato e de teste, ainda não um achado de comprometimento.

O responsável pelo serviço deve definir o resultado pretendido para o usuário e aprovar mudanças no significado. A equipe técnica pode expressar e ensaiar a regra em código. A equipe de resposta a incidentes pode mais tarde usar a regra aprovada como referência ao investigar uma falha relatada de serviço. Nenhum desses papéis ganha autoridade para inspecionar dados reais de frequentadores só porque existe um programa de demonstração.

##### Um modelo de relatório para quem estuda no primeiro mês

Depois de um ensaio de linha de base, quem estuda deve produzir um **relatório de contrato**, não um relatório de incidente. O documento deve identificar a versão da regra, os identificadores de entrada, a ocupação de sala assumida, a semântica de estado, a convenção de intervalo, os resultados esperados positivos e negativos, a saída executada ou raciocinada, e as alegações exatas que a verificação não pode estabelecer.

Um relatório claro pode afirmar:

> “BSL1-v1 aplica-se a seis linhas fictícias de reserva de um dia. O verificador testa a validade do intervalo e sobreposições na mesma sala entre reservas confirmadas, sob limites de tempo semiabertos. Encontra S03/S04 em conflito e S06 inválido. Uma variante independente de mudança de estado acrescenta um conflito S01/S05; omitir S04 de uma entrada copiada remove um conflito detectado sem provar reparo do serviço. Nenhum estado real de reserva, usuário, conta, fonte de log ou serviço de produção foi testado.”

Este é um artefato útil porque outra pessoa que estuda pode reproduzir toda classificação relevante a partir da entrada declarada. Também impede que a falha de um *requisito de brinquedo* se torne uma alegação sem suporte de incidente no mundo real.

Para quem começa, o resultado aceito não é matemática complicada nem uma avaliação abrangente de segurança da aplicação. É uma explicação que liga **expectativa de negócio → premissas declaradas → comparação reproduzível → conclusão restringida**. O estágio curricular seguinte pode então ensinar como um analista de resposta a incidentes obtém observações confiáveis e as separa de hipóteses.

Este relatório complementa, em vez de substituir, o contrato existente D1 de prontidão de evidência, o laboratório de revisão de alegações R1–R8 e a passagem do caso. As ferramentas respondem a perguntas diferentes, e um pacote maduro de prontidão mantém essas fronteiras explícitas.

##### Síntese da seção: a preparação começa com uma promessa explícita

O mapa de serviço diz quais sistemas podem importar. A linha de base de comportamento diz o que o serviço legítimo deve alcançar. O plano de prontidão de evidência diz quais fontes autorizadas poderiam mais tarde sustentar ou contestar uma alegação. O registro de decisão do caso afirma o que a equipe de fato sabe e qual próxima ação exige aprovação. São artefatos complementares com propósitos distintos.

Para a Harbor Library, um invariante sobre ocupação confirmada de sala oferece um exemplo prático de comportamento normal. Não estabelece que B17/B18 foram modificadas de forma incorreta, nem fornece um ator humano, uma lista autorizada de tarefas, um resultado de restauração ou uma conclusão de transferência de dados. O juízo canônico das 09:05 ainda se apoia só em R1–R8.

Um estudante sólido do primeiro mês deve terminar capaz de explicar por que uma reserva adjacente permitida passa, por que um par confirmado sobreposto falha, por que o cancelamento muda a ocupação, por que entradas incompletas podem esconder um conflito, e por que nenhum desses resultados de peça, sozinho, prova um incidente de segurança. Isso é conhecimento substantivo adicional de prontidão, não uma recontagem do caso do incidente.

<a id="ir-rapid-ch01-bsl1-lab"></a>

#### Laboratório offline BSL1 — invariantes de reserva

**Meta:** Reproduzir uma verificação determinística de invariante de negócio para um conjunto fictício pequeno de reservas e, em seguida, demonstrar como uma mudança de estado ou uma entrada ausente altera o que o verificador pode relatar.

**Ambiente:** biblioteca padrão do Python 3, só memória. Sem criação de arquivo, pedidos de rede, autenticação, registros pessoais ou mudanças de produção.

**Classificação da peça:** Os identificadores S01–S06 são objetos inventados de treinamento BSL1 e não têm relação com as reservas canônicas B17–B20 da Harbor Library nem com R1–R8.

**Regras:** Reservas confirmadas ocupam o intervalo da sala; reservas canceladas não ocupam. Os intervalos de reserva são semiabertos [início, fim), o fim precisa ser estritamente posterior ao início, e sobreposições confirmadas simultâneas na mesma sala são proibidas sob esta política de brinquedo de ocupação única.

| ID | Sala | Início | Fim | Estado |
|---|---|---|---|---|
| S01 | Room A | 09:00 | 10:00 | CONFIRMED |
| S02 | Room A | 10:00 | 11:00 | CONFIRMED |
| S03 | Room B | 09:00 | 10:00 | CONFIRMED |
| S04 | Room B | 09:30 | 10:30 | CONFIRMED |
| S05 | Room A | 09:00 | 10:00 | CANCELLED |
| S06 | Room C | 11:00 | 11:00 | CONFIRMED |

Antes de executar, preveja os achados de base. Explique por que S01 e S02 não se sobrepõem, e por que S05 não ocupa o horário da sala. Em seguida, preveja o resultado quando só S05 muda para confirmado e quando S04 é omitido de propósito de uma cópia de trabalho incompleta.

##### Programa reproduzível em Python 3

~~~python
from itertools import combinations

BOOKINGS = [
    ("S01", "Room A", "09:00", "10:00", "CONFIRMED"),
    ("S02", "Room A", "10:00", "11:00", "CONFIRMED"),
    ("S03", "Room B", "09:00", "10:00", "CONFIRMED"),
    ("S04", "Room B", "09:30", "10:30", "CONFIRMED"),
    ("S05", "Room A", "09:00", "10:00", "CANCELLED"),
    ("S06", "Room C", "11:00", "11:00", "CONFIRMED"),
]

def minute(text):
    hours, minutes = map(int, text.split(":"))
    if not (0 <= hours < 24 and 0 <= minutes < 60):
        raise ValueError("invalid clock field")
    return hours * 60 + minutes

def overlaps(a, b):
    return (
        minute(a[2]) < minute(b[3])
        and minute(b[2]) < minute(a[3])
    )

def inspect(rows):
    if len({r[0] for r in rows}) != len(rows):
        raise ValueError("duplicate booking ID")

    issues = []
    for row_id, room, start, end, status in rows:
        if status not in {"CONFIRMED", "CANCELLED"}:
            issues.append(f"UNKNOWN_STATUS {row_id}")
        if minute(start) >= minute(end):
            issues.append(f"INVALID_INTERVAL {row_id}")

    active = [
        row for row in rows
        if (
            row[4] == "CONFIRMED"
            and minute(row[2]) < minute(row[3])
        )
    ]

    for first, second in combinations(active, 2):
        if first[1] == second[1] and overlaps(first, second):
            issues.append(f"CONFLICT {first[0]}/{second[0]}")

    return sorted(issues)

baseline = inspect(BOOKINGS)
for issue in baseline:
    print("BASE", issue)
print("BASE_COUNT", len(baseline))

print(
    "BOUNDARY_S01_S02",
    "OVERLAP" if overlaps(BOOKINGS[0], BOOKINGS[1])
    else "NO_OVERLAP",
)

print(
    "CANCELLED_S05",
    "NOT_OCCUPYING"
    if BOOKINGS[4][4] == "CANCELLED"
    else "OCCUPYING",
)

# Controlled status-change variant: S05 only.
variant = [
    (*row[:4], "CONFIRMED") if row[0] == "S05" else row
    for row in BOOKINGS
]
changed = inspect(variant)
for issue in changed:
    print("VARIANT", issue)
print("VARIANT_COUNT", len(changed))

# Incomplete-input negative control: omit S04 only.
incomplete = [row for row in BOOKINGS if row[0] != "S04"]
missing = inspect(incomplete)
for issue in missing:
    print("INCOMPLETE", issue)
print("INCOMPLETE_COUNT", len(missing))

assert baseline == ["CONFLICT S03/S04", "INVALID_INTERVAL S06"]
assert len(changed) == 3
assert len(missing) == 1
~~~

Compare o resultado impresso e os limites com a [resolução BSL1](#ir-rapid-ch01-bsl1-result) no apêndice final. As seis entradas da série S são uma peça separada de preparação, nunca evidência do caso para R1–R8.

<a id="w1-review-02"></a>

#### Unidade de revisão da semana 1, número 2 — Não transformar uma entrada vazia numa agenda limpa

##### Objetivo e comportamento observado

Explique como rejeitar um quadro de ensaio incompleto ou ininterpretável, preservando os achados originais da regra de reserva. Esta unidade estende o [BSL1](#ir-rapid-ch01-bsl1-lab); não muda a convenção de intervalo semiaberto, os significados de estado confirmado/cancelado nem a peça S01–S06.

No programa original, `inspect([])` devolve `[]`. Isto é consistente com conferir pares numa sequência vazia: não há pares conflitantes fornecidos. Não é uma demonstração de um quadro saudável de seis reservas. Do mesmo modo, `minute("9:00")` devolve 540 porque o analisador converte as duas peças numéricas; não impõe uma representação de hora com dois dígitos. A linha de base original usa cadeias bem formadas, portanto os resultados existentes não são invalidados por essas sondas.

A guarda proposta torna explícito o contrato adicional do ensaio. Os identificadores esperados precisam ser um conjunto congelado não vazio; cada linha precisa conter cinco cadeias não vazias; os campos de relógio precisam usar exatamente dois dígitos ASCII, dois-pontos e dois dígitos ASCII, com intervalos válidos de hora e minuto; os estados precisam ter os dois significados definidos; os identificadores precisam ser únicos e coincidir exatamente com o quadro declarado.

São **convenções locais de ensino**, não requisitos universais para APIs reais de reserva. Um serviço real pode usar legitimamente listas JSON, outros modelos de estado ou uma representação diferente de carimbo de tempo. Precisa da própria interpretação documentada. A [documentação de expressões regulares do Python](https://docs.python.org/3/library/re.html#re.fullmatch) explica a correspondência da cadeia inteira; não prescreve o nosso contrato de tempo ou de reserva.

##### Por que o achado de duração precisa sobreviver

S06 tem horários de início e fim iguais. Ambos os campos são interpretáveis sob o contrato de relógio. O invariante original, portanto, ainda relata `INVALID_INTERVAL S06`; a guarda não repara em silêncio o horário de fim, não descarta a linha nem a reinterpreta como cancelamento. Admissão da entrada e achados da regra de negócio permanecem separados.

A mesma distinção se aplica a um quadro completo que contém um conflito genuíno modelado. Uma boa guarda precisa admitir as linhas interpretáveis e deixar a regra original relatar o conflito. Rejeitar toda entrada problemática impediria quem estuda de ver a condição de negócio que o laboratório foi desenhado para ensinar.

##### Extensão reproduzível do BSL1

Rode primeiro a listagem original completa do BSL1 numa sessão nova. Preveja cinco linhas novas antes de rodar a extensão seguinte. O resultado é condicional ao quadro esperado fornecido; nem a igualdade de identificadores nem a sintaxe estrita autenticam uma fonte.

~~~python
# Run after the complete BSL1 listing, in the same Python session.
import re

W1_BSL_EXPECTED = frozenset({"S01", "S02", "S03", "S04", "S05", "S06"})

def w1_inspect_scoped(rows, expected_ids=W1_BSL_EXPECTED):
    if type(expected_ids) is not frozenset or not expected_ids:
        raise ValueError("INVALID_EXPECTED_SCOPE")
    if any(type(item) is not str or not item.strip() for item in expected_ids):
        raise ValueError("INVALID_EXPECTED_SCOPE")
    if type(rows) not in (list, tuple) or not rows:
        raise ValueError("EMPTY_OR_INVALID_INPUT")
    ids = []
    for row in rows:
        if type(row) not in (list, tuple) or len(row) != 5:
            raise ValueError("INVALID_ROW_SHAPE")
        if any(type(item) is not str or not item.strip() for item in row):
            raise ValueError("INVALID_FIELD_TYPE")
        row_id, room, start, end, status = row
        ids.append(row_id)
        for text in (start, end):
            if re.fullmatch(r"[0-9]{2}:[0-9]{2}", text) is None:
                raise ValueError("CLOCK_FORMAT")
            minute(text)  # Reuse BSL1's hour/minute range check.
        if status not in {"CONFIRMED", "CANCELLED"}:
            raise ValueError("UNKNOWN_STATUS")
    if len(ids) != len(set(ids)):
        raise ValueError("DUPLICATE_ID")
    if frozenset(ids) != expected_ids:
        raise ValueError("COVERAGE_MISMATCH")
    return inspect(rows)  # Preserve BSL1's overlap/duration findings.

def w1_show_bsl(label, rows, expected_ids=W1_BSL_EXPECTED):
    try:
        issues = w1_inspect_scoped(rows, expected_ids)
    except ValueError as error:
        print(label, "INPUT_REJECTED", str(error))
    else:
        print(label, "EVALUATED", ";".join(issues) if issues else "NO_FINDINGS_IN_SCOPE")

w1_bad_clock = [
    (row[0], row[1], "9:00", row[3], row[4]) if row[0] == "S01" else row
    for row in BOOKINGS
]
w1_show_bsl("W1_BASE", BOOKINGS)
w1_show_bsl("W1_EMPTY", [])
w1_show_bsl("W1_MISSING_S04", [r for r in BOOKINGS if r[0] != "S04"])
w1_show_bsl("W1_BAD_CLOCK", w1_bad_clock)
w1_show_bsl("W1_NARROW_SCOPE", [BOOKINGS[0]], frozenset({"S01"}))
~~~

A última chamada declara de propósito um quadro diferente, de um objeto. Não é uma versão reparada do teste de seis objetos. Mantenha esses dois relatórios separados. Retenha também as demonstrações originais de sensibilidade do BSL1 à mudança de estado e à linha omitida: elas ensinam o que o modelo sem guarda vê, enquanto esta extensão ensina se um resultado responde a um quadro pré-declarado.

##### Prática suplementar W1-R2

**Objetivo:** diagnosticar entrada vazia, ausente e malformada sem suprimir achados válidos de invariante. **Entradas:** as seis linhas originais do BSL1 e as cinco chamadas acima. **Artefato exigido:** a saída de cinco linhas, uma explicação de cinco linhas sobre admissão versus resultado de invariante, e um pedido de fonte proposto para o caso de S04 ausente. **Restrições:** preserve S06 inalterado; não modifique o `BOOKINGS` original; não redefina o quadro de seis objetos para obter um resultado verde. Explique se conferir identificadores prova coleta autêntica ou completa no mundo real.

**Avaliação:** um ponto para cada um: achados de linha de base inalterados, rejeição de entrada vazia, rejeição de linha ausente, explicação do relógio estrito, e resultado de uma linha corretamente limitado. Alegações de autenticação da fonte ou de reparo do serviço precisam ser corrigidas. Os EX002, EX005 e EX010 originais mantêm os requisitos de duas linhas, quatro linhas e duas frases; este artefato suplementar não é inserido nesses campos exigidos. [Resolução](#w1-answer-02).

*Rubrica:* 3 = cinco pontos da fonte: linha de base inalterada, rejeição do vazio, rejeição da linha ausente, relógio estrito e resultado de uma linha limitado;; 2 = a maior parte desses pontos, com uma omissão de limite;; 1 = responde, mas omite fonte, limite ou a distinção entre admissão e invariante;; 0 = nenhum.

##### Síntese da revisão

“Nenhum achado nas linhas fornecidas” não é a mesma alegação que “a entrada pretendida estava completa”, e nenhuma das duas é um achado universal de segurança do serviço.

#### Marco resolvido

Uma chamada de edição bem-sucedida não é prova de que o estado da reserva atende à regra aprovada pelo responsável. Na peça BSL1, compare primeiro o estado final da reserva com o invariante declarado; depois teste à parte a variante controlada de mudança de estado. Nenhum dos resultados se torna um fato de incidente da série R.

#### Prática — Aula 02

##### EX002 — As duas primeiras perguntas

**Objetivo:** escolher verificações que poderiam mudar a decisão de restrição. **Entradas:** R1–R6 e as tabelas de serviço e de autoridade. **Saída:** duas linhas com uma pergunta precisa, o fato que a torna relevante, o custodiante ou a pessoa autorizada a quem perguntar, e como qualquer das respostas muda a decisão. Uma pergunta precisa testar a explicação do treinamento; a outra precisa testar quem usou a conta ou se as edições continuam. Registre pedidos em vez de dizer que a entrevista ou a revisão de log já ocorreu. Uma nota 2 exige discriminadores diferentes e um caminho nomeado de aprovação para qualquer coleta nova de identidade.

**Extensão de linha de base de comportamento:** Na pergunta de treinamento, especifique qual comportamento aprovado pelo responsável para B17/B18 precisa ser conferido além da entrada de calendário de R6. Na pergunta de conta, separe um discriminador de fonte da pergunta ainda aberta de contrato de negócio. Os resultados da série S do BSL1 não são evidência sobre B17/B18.

**Resolução:** [EX002 no apêndice final](#ex002--worked-result).

*Rubrica:* 3 = nota 2 da fonte: duas linhas com discriminadores diferentes, caminho nomeado de aprovação para coleta nova de identidade, e a série S fora da evidência de B17/B18;; 2 = as duas linhas existem, mas falta um discriminador ou o caminho de aprovação;; 1 = responde à pergunta, mas omite fonte, limite, autoridade ou teste exigido;; 0 = nenhum.

##### EX005 — Linha do tempo

**Objetivo:** preservar a ordem dos eventos sem transformar sequência em causação. **Entradas:** R1, R3, R4 e R5. **Saída:** uma tabela UTC de quatro linhas com identificador do registro, fonte, hora e evento observado, seguida de uma frase de ordenação e de uma frase separada de causalidade sem suporte. Mantenha a hora de abertura do caso, 09:00, fora da tabela de eventos. Uma nota 2 ordena os quatro eventos corretamente e explica por que a precedência, sozinha, não identifica o ator humano nem prova por que a visão do frequentador mudou.

**Extensão:** Acrescente uma nota separada de marco `case opened 09:00; decision 09:05; available R1–R8`. Explique por que os horários de abertura do caso e de decisão não devem ser inseridos na cronologia de quatro linhas de eventos de fonte como se fossem eventos de fonte.

**Para crédito completo:** Uma resposta de 2 pontos preserva a cronologia e rejeita atribuição humana e causalidade sem suporte.

**Resolução:** [EX005 no apêndice final](#ex005--worked-result).

*Rubrica:* 3 = nota 2 da fonte: quatro eventos na ordem correta, frase de ordenação, frase de causalidade sem suporte, e 09:00 fora da tabela de eventos de fonte;; 2 = a ordem está correta, mas falta o limite de causalidade ou de ator;; 1 = responde à pergunta, mas omite fonte, limite ou a separação entre ordem e causa;; 0 = nenhum.

##### EX010 — Rascunho de comunicação

**Objetivo:** comunicar uma ação útil sem atribuição prematura. **Entradas:** R1–R8 e o estado de abertura às 09:00, *antes* da decisão das 09:05. **Saída:** exatamente duas frases para um público interno de responsável pelo serviço: a primeira declara sinais observados de serviço e incerteza; a segunda nomeia uma próxima verificação **proposta**, o dono dela e o marco esperado de decisão às 09:05. Não diga que preservação, entrevista ou restrição já foi aprovada ou executada. Uma nota 2 fornece um ponteiro de fonte e uma distinção inequívoca entre trabalho planejado e trabalho concluído.

**Extensão de linha de base de comportamento:** Mantenha exatamente duas frases no marco de abertura das 09:00. Distinga os registros de edição R3/R4 e o relato de frequentador R5 de um estado de negócio incorreto verificado; nomeie uma verificação proposta, pelo responsável pelo serviço, do comportamento esperado, antes da decisão das 09:05.

**Resolução:** [EX010 no apêndice final](#ex010--worked-result).

*Rubrica:* 3 = nota 2 da fonte: exatamente duas frases, ponteiro de fonte, e distinção inequívoca entre trabalho planejado e concluído no marco das 09:00;; 2 = as duas frases existem, mas a distinção entre proposta e execução fica ambígua;; 1 = responde à pergunta, mas omite fonte, limite ou trata trabalho planejado como feito;; 0 = nenhum.

<!-- open-cyber-academy:lesson-navigation:start lesson-02 -->
#### Continue estudando — aula 02 de pelo menos 20

[← Aula 01](#lesson-01) · [Índice de aulas do curso](../SUBJECTS.md) · [Aula 03 →](#lesson-03)

Siga para a próxima aula diária escrita neste manuscrito.
<!-- open-cyber-academy:lesson-navigation:end -->
<a id="lesson-03"></a>

### Aula 03 — Caminhos de serviço, dependências e modos degradados

**Semana 1, dia 3.** Percorra o ensino e o marco resolvido antes de tentar os exercícios indicados. Compare o seu artefato com a resolução final só depois.

#### 1.2b Caminhos essenciais de serviço e modos degradados

##### Um componente em execução não é um serviço de negócio entregue

Um site de biblioteca pode responder enquanto o sistema de reserva subjacente não consegue exibir as salas atuais nem aceitar uma reserva. Um monitor de cópia pode relatar um trabalho concluído enquanto ninguém mostrou que a cópia resultante restaura uma agenda correta. Uma central de atendimento pode ainda receber o pedido de um frequentador enquanto a reserva feita por computador não pode ser aceita. As três situações ilustram o mesmo problema de preparação: a organização pode dizer com verdade que *alguma* tecnologia permanece operacional sem estabelecer que o resultado prometido ao usuário está disponível.

O capítulo 01 existente começa corretamente com um mapa de serviço e um contrato D1 de prontidão de evidência. Um mapa de serviço diz a quem responde quais componentes e donos importam. D1 pergunta se observações úteis poderiam ser obtidas sob autoridade, inclusive semântica da fonte e evidência ausente. É necessária uma terceira pergunta: **quais funções exatas, voltadas ao usuário, uma falha de componente afetaria?** Respondê-la exige um modelo de dependência específico da função, em vez de tratar todo componente como globalmente saudável ou globalmente fatal.

Uma **função de serviço** é uma operação específica com um resultado útil definido. Uma **dependência técnica** é algo exigido para realizar essa operação na arquitetura e no modo declarados. Um **modo degradado** é um estado operacional deliberadamente mais estreito, no qual algumas atividades continuam, mas outros compromissos de serviço não podem ser feitos com honestidade.

Essas distinções são consistentes com a ênfase em dependências de serviço e recuperação de função de negócio no [NIST SP 800-184, *Guide for Cybersecurity Event Recovery*](https://csrc.nist.gov/pubs/sp/800/184/final) e com a preparação de resposta atenta ao risco no [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Essas publicações do NIST não especificam as rotas internas da Harbor Library; PATH1 é material original de raciocínio de sala.

##### Comece pela promessa feita a um frequentador

Imagine cinco funções distinguíveis de um serviço hipotético de reserva: uma página informativa que responde, uma lista atual de salas sendo exibida, um membro autorizado da equipe editando uma reserva, um empregado da recepção registrando um pedido pendente, e um trabalho novo de cópia obtendo os dados de origem.

Os resultados não são intercambiáveis. Uma resposta bem-sucedida de página informativa diz pouco sobre a exatidão da reserva. Uma edição de equipe aceita é uma mudança de estado de negócio, que pode exigir autorização e armazenamento durável. Um recibo de pedido manual **não** é aceitação de uma reserva. O acesso de um trabalho de cópia a uma base de dados **não** é uma restauração testada nem um retorno aceito ao serviço.

Uma frase fraca de prontidão diz “a aplicação está disponível”. Uma frase mais útil diz “a função autorizada de edição pela equipe produziu a mudança esperada na reserva pretendida, e um revisor conferiu o estado autoritativo resultante num teste controlado”. A segunda frase tem um resultado testável e um escopo declarado.

Na profundidade do curso rápido, quem estuda deve identificar a **unidade de sucesso** antes de selecionar um teste. A pergunta é sobre alcançar uma página, ver uma sala atual, fazer uma reserva, recolher um pedido pendente ou produzir um objeto de cópia? Cada unidade precisa de uma resposta diferente e pode ter dependências técnicas diferentes.

Este enquadramento também melhora a comunicação do incidente. O responsável pelo serviço pode aprovar legitimamente um contorno limitado de recepção de pedidos, mas a equipe não deve anunciar que salas estão confirmadas enquanto as escritas estão indisponíveis. Um aviso honesto de serviço degradado deve explicar o que o usuário pode fazer, o que permanece pendente e o que precisa ocorrer antes de a confirmação ser possível.

##### Expresse premissas de caminho como uma tabela pequena de dependências

O modelo de ensino PATH1 usa componentes nomeados `web`, `identity`, `database`, `helpdesk` e `backup`. Essas categorias se parecem com o mapa de serviço, mas as **conexões específicas são inventadas**. Os registros canônicos R1–R8 não confirmam esta topologia.

| Função modelada fictícia | Componentes PATH1 exigidos | Significado estreito de negócio |
|---|---|---|
| `site_reachable` | `web` | Uma página informativa pode responder |
| `room_view` | `web`, `database` | Uma rota de visão de salas é estruturalmente possível |
| `staff_edit` | `web`, `identity`, `database` | Uma rota de edição pela equipe tem os pré-requisitos modelados |
| `manual_intake` | `helpdesk` | Um pedido pendente pode ser recebido, não confirmado |
| `new_backup_job` | `database`, `backup` | O processo modelado de cópia pode acessar dados de origem |

Um componente num caminho é **exigido sob este modelo**. Se um componente exigido está indisponível, o script prevê que a função está prejudicada. Se todo componente exigido está marcado como disponível, prevê apenas **possibilidade estrutural**, não correção verificada. O modelo não implementa autenticação, persistência de dados, validade de cache, integridade da cópia, notificação de frequentadores nem desempenho.

Essas limitações não são fraquezas a ocultar. Definem qual pergunta de engenharia o modelo responde. Um modelo pequeno e explícito pode ajudar a identificar o próximo dono ou teste, desde que ninguém promova as previsões dele a observações reais.

Em contraste, o contrato de fonte de D1 pergunta se uma auditoria da aplicação ou um registro de identidade poderia provar o que de fato aconteceu. O exercício de regra de negócio do BSL1 confere sobreposições e semântica de cancelamento usando registros inventados e separados de reserva. PATH1 não faz nenhuma das duas coisas. Pergunta quais *funções* poderiam perder os pré-requisitos modelados sob perda de componente.

##### Uma falha de um único componente pode prejudicar várias funções diferentes

Considere o caso hipotético independente em que a base de dados do PATH1 fica indisponível. Como `room_view`, `staff_edit` e `new_backup_job` a listam como exigida, o modelo prevê que essas três funções estão prejudicadas. A página informativa e a recepção manual da central não a listam, portanto permanecem estruturalmente possíveis neste desenho simplificado.

Essa previsão não equivale a “o site está saudável”. Um morador pode alcançar uma página e falhar em ver uma lista confiável de salas. Também não equivale a “a biblioteca inteira não pode ajudar ninguém”. Sob a premissa fictícia de alternativa, a central ainda pode receber um pedido não confirmado.

Uma falha do serviço de identidade tem outra forma. Prejudica o caminho modelado de edição pela equipe, mas não prejudica necessariamente a visão de salas. Isto **não** estabelece que a Harbor Library de fato permite leitura sem autenticação; reflete só a peça independente.

Uma falha da central pode remover a alternativa manual enquanto os caminhos mediados pelo site permanecem estruturalmente possíveis. Na operação ordinária isto pode ser inconveniente; durante uma interrupção mais ampla pode remover o único caminho permitido para receber pedidos novos. Assim, a importância de negócio de uma dependência depende do contexto operacional.

A pergunta correta de incidente não é simplesmente “qual componente está vermelho?”. É **qual função útil está afetada, que outro caminho permanece, e que promessa legítima ainda pode ser feita?** Contagens de componentes não substituem essa análise.

##### Pontos únicos de falha precisam nomear o resultado afetado

Chamar um componente de “ponto único de falha” é incompleto sem nomear a função que ele pode impedir. No PATH1, a falha só de `web` impede a página informativa, a visão de salas e a rota de edição pela equipe. Não impede, sob a peça declarada, a recepção de pedidos na central nem um trabalho novo de cópia.

Do mesmo modo, a base de dados é um elemento exigido único para a visão modelada de salas, mas não para a página informativa. Uma aplicação real pode ter dependências adicionais ou uma rota alternativa que funcione; a tabela PATH1 não fornece evidência sobre elas.

Para uma função com dependências todas exigidas, **a falha de qualquer componente listado** basta para prejudicar aquele caminho modelado particular. Um desenho resiliente real poderia, em vez disso, ter alternativas — como duas instâncias equivalentes de serviço ou uma leitura em cache controlada. Tais alternativas precisam ser documentadas e testadas de forma explícita antes de serem usadas em decisões operacionais.

Este modelo inicial evita de propósito estimativas de probabilidade. Uma lista de componentes não fornece taxas de falha, correlações, tempos de reparo nem evidência de que capacidade alternativa é utilizável. Atribuir uma probabilidade inventada de indisponibilidade acrescentaria precisão sem suporte.

O valor de preparação deste raciocínio é pedir a um responsável pelo serviço que identifique o que é de fato essencial e qual rota alternativa pode atender com segurança a um requisito mais estreito. Não autoriza mudar uma configuração de produção.

##### Disponível, degradado, indisponível e desconhecido são conclusões diferentes

Uma rota pode estar **modelada como disponível**, **modelada como prejudicada**, **observada a funcionar num teste limitado**, ou **ainda não testada**. Essas afirmações não devem ser colapsadas num único rótulo verde/vermelho.

Para PATH1, a peça Python fornecida usa disponibilidade booleana de componente e prevê estado estrutural. Componentes reais podem falhar em parte: uma base pode responder leituras e rejeitar escritas; um serviço de identidade pode validar sessões antigas e não sessões novas; um cache pode devolver conteúdo obsoleto. Nessas circunstâncias um booleano simples pode esconder incerteza importante.

Se um analista não consegue determinar o estado real de um componente, seria impróprio entrar `True` só para o modelo devolver um resultado verde. Registre a condição como desconhecida e pergunte qual observação poderia resolvê-la. O script de sala omite um terceiro estado por simplicidade; quem estuda precisa relatar isso como limitação do modelo.

Uma resposta bem-sucedida de um ponto de extremidade web também não prova que uma mudança de reserva foi autorizada e confirmada de forma durável. Um recibo da central não prova que existe uma atribuição de sala. São exemplos de **alegação excessiva a partir de sucesso parcial**.

Um relatório preciso pode dizer: “sob o modelo selecionado, o caminho da página informativa permanece estruturalmente possível, enquanto o caminho de escrita de reserva está previsto como indisponível”. Não deve alegar que frequentadores reais podem usar o serviço com segurança sem um teste correspondente e aceitação do responsável.

##### Desenhe um modo degradado com limites explícitos

Um modo degradado não é simplesmente “o que ainda funciona”. Deve ser definido de antemão pelo responsável pelo serviço, com condições de ativação, um fluxo aprovado, uma duração ou gatilho de revisão, uma mensagem que descreva com exatidão os limites do serviço, e um caminho de volta à operação normal.

Para um modo hipotético de central só de pedidos, o responsável precisaria responder:

1. A equipe pode receber pedidos enquanto o serviço autoritativo de reserva está indisponível?
2. Quais detalhes mínimos podem ser coletados com segurança e para qual propósito?
3. O pedido permanece **pendente** até uma verificação autorizada posterior?
4. Quem mantém a ordem dos recibos e impede duplicatas ou instruções conflitantes?
5. Quem comunica aos frequentadores a distinção entre recebimento e aceitação?
6. Qual é a rota de escalada se a mesa não consegue acompanhar ou se o pedido é urgente?
7. Quem autoriza a reconciliação eventual e confirma o estado de negócio resultante?
8. Que resultado observável encerra o modo degradado?

Isto é um **contrato de negócio proposto**, não uma alegação de que a central canônica da Harbor Library seguiu tal procedimento. O laboratório MQ3 do módulo 3 da edição inglesa, ausente deste arquivo, ensina reconciliação detalhada de pedidos, mas PATH1 faz uma pergunta anterior e diferente: *Aquele tipo de função alternativa permaneceria tecnicamente possível sob uma falha especificada de componente?*

A recepção manual pode estar indisponível por política mesmo quando a central está funcionando. A equipe pode não ter capacidade, procedimentos aprovados em papel ou salvaguardas de privacidade. A possibilidade técnica de um modelo nunca se sobrepõe às restrições operacionais do responsável pelo serviço.

Uma frase segura de modo degradado diz “o pedido pode ser registrado para revisão”. Uma frase perigosa diz “a sala está reservada” quando a reserva aceita não foi estabelecida.

##### A prontidão precisa de um plano de verificação para cada função

Antes de aceitar a tabela de funções, um responsável pelo serviço e um custodiante técnico devem identificar o teste que a contestaria. Um plano útil de teste inclui:

- A função e o resultado prometido.
- Os componentes exigidos propostos.
- A falha isolada específica ou o componente indisponível.
- A previsão de prejuízo ou o comportamento alternativo.
- A observação técnica positiva a procurar.
- Uma verificação negativa ou de segurança de negócio.
- O dono responsável e o ambiente permitido.
- Uma fonte e um carimbo de tempo para o resultado real.
- O limite da conclusão e a revisão exigida.

Para a visão modelada de salas, uma resposta técnica sozinha pode ser insuficiente se devolve dados obsoletos ou não autorizados. Para edição pela equipe, um pedido bem-sucedido não prova que o valor autoritativo pretendido foi confirmado. Para um trabalho de cópia, a criação não prova que o objeto é recuperável. Para a recepção na central, um recibo não prova que o pedido foi aceito.

Este plano deve ser comparado com os artefatos existentes D1 e BSL1 **sem copiar o conteúdo deles**. D1 especifica como um registro poderia ser obtido e interpretado; BSL1 define algum comportamento correto de estado de reserva; PATH1 especifica quais pré-requisitos de caminho estão sendo contestados. Um teste isolado real pode recorrer aos três, mas as conclusões permanecem separadas.

Se o teste negativo esperado falha, registre a falha em vez de enfraquecer em silêncio a regra de aceitação. Se os dados de entrada estão incompletos ou a falha suposta não foi de fato induzida, relate um **teste inconclusivo** em vez de uma aprovação limpa.

##### Contraste uma conclusão tentadora e errada com uma defensável

**Análise hipotética incorreta:**

> “A base está fora, mas a página inicial responde, portanto o serviço está saudável. A equipe pode receber pedidos na mesa, o que significa que as reservas ainda estão confirmadas. O componente de cópia permanece no ar, portanto a biblioteca já pode restaurar tudo.”

Isto assume que a página informativa representa todas as funções de reserva; que um pedido manual pendente é uma reserva concluída; e que um componente de cópia ou o resultado de um trabalho prova recuperação testada. Nenhuma das alegações segue do modelo PATH1, e nenhuma interrupção de base aparece em R1–R8 canônicos.

**Análise limitada correta:**

> “No modelo independente PATH1, a indisponibilidade da base prevê prejuízo dos caminhos de visão de salas, de edição pela equipe e de trabalho novo de cópia, enquanto a página informativa e a recepção de pedidos na central permanecem estruturalmente possíveis. A recepção manual não aceita reservas, e nenhum teste de recuperação é fornecido. São previsões de sensibilidade a partir de premissas declaradas, não observações do incidente da Harbor Library. O responsável pelo serviço precisaria aprovar qualquer promessa operacional degradada, e uma verificação autorizada separada seria necessária para estabelecer a função real e a correção de negócio.”

A melhoria não é simplesmente linguagem cautelosa. Identifica a **unidade de serviço**, a **fonte da alegação** e a **evidência de aceitação que falta**.

##### Compare cenários de falha sem transformá-los em eventos canônicos

Um ensaio offline útil muda uma condição modelada de cada vez e registra quais funções mudam de classificação. O estudante deve começar pela linha de base, simular uma falha da base, restaurar a linha de base e simular falha de identidade. O mesmo processo pode ser usado para falhas da central e da web.

Sem reiniciar o modelo, as conclusões podem se misturar: uma condição persistente de base indisponível pode fazer um teste de identidade parecer prejudicar mais funções do que realmente prejudica. O código abaixo evita isso ao avaliar conjuntos independentes de falha, em vez de alterar as definições compartilhadas de rota.

As comparações devem ser explicadas em termos de negócio. Se a falha de identidade afeta só o caminho de edição pela equipe, isso é diferente de uma falha da base afetar visão, edição e criação de cópia nova. Se a falha da central remove a recepção, o dano potencial depende em parte de os usuários terem outro meio aprovado de fazer pedidos.

Uma falha de dois componentes é útil como controle negativo. Com base e central indisponíveis sob PATH1, a página informativa restante não pode fornecer escritas de reserva aceitas nem receber pedidos pendentes. Seria enganoso rotular esse estado como “serviço de reserva parcialmente operacional” sem especificar a função limitada só de informação.

A peça **não** fornece frequência, probabilidade nem nota de severidade para esses cenários. Isso exige informação do responsável pelo serviço e evidência operacional medida fora da sala.

##### Relação com as decisões de incidente às 09:05

Volte ao conjunto real e fictício de fontes da Rodada A. R1 relata uma entrada de `desk-a`, R3 e R4 relatam mudanças de reserva, R5 é uma preocupação de frequentador, R6 descreve treinamento agendado, R7 relata a conclusão de um trabalho de cópia e R8 carece de detalhe suficiente de destino. Esses registros sustentam perguntas sobre aprovação, estado do serviço e contexto de identidade. **Não** estabelecem qualquer interrupção de componente PATH1.

Um estudante pode propor, com razão, que o responsável pelo serviço esclareça o que aconteceria se a base estivesse indisponível, ou se uma alternativa só de pedidos está aprovada. Essa é uma pergunta de prontidão, não um achado sobre o incidente.

Um cenário PATH1 nunca deve ser inserido como linha adicional da série R nem usado para justificar a decisão de restrição das 09:05. Do mesmo modo, os eventos posteriores B19/B20 ou os resultados dos ramos S/P, que pertencem a capítulos posteriores da edição inglesa, não podem ser importados para trás a fim de resolver a incerteza original.

Quem responde com qualidade pode manter dois livros: o **livro de evidência canônica**, limitado aos registros de caso liberados, e um **livro de modelo e teste**, contendo premissas declaradas e resultados hipotéticos. Essa separação permite planejamento tecnicamente útil sem ficcionalizar observações de produção.

##### Síntese da seção: resiliência é uma promessa limitada de serviço

Resiliência não é uma garantia de que todo componente permanece no ar. É a capacidade de definir resultados importantes para o usuário, identificar como a falha de um componente poderia afetá-los, preparar modos mais estreitos aceitáveis e testar o que esses modos de fato entregam.

Um site pode estar alcançável enquanto a visão atual de salas está prejudicada. Uma central pode conseguir receber um pedido sem confirmar uma reserva. Um trabalho de cópia pode ser possível sem demonstrar recuperação. Reconhecer essas distinções melhora a qualidade das perguntas de incidente e torna mais defensáveis as decisões posteriores do responsável pelo serviço.

O laboratório PATH1 é pequeno de propósito. Treina um hábito transferível: **prever consequências estruturais, identificar a promessa de negócio e exigir observação adequada antes de declarar impacto ou recuperação de serviço**.

<a id="ir-rapid-ch01-path1-lab"></a>

##### Laboratório offline PATH1 — dependências funcionais e serviço degradado

**Classificação:** Exercício independente de modelagem, inteiramente sintético. Não é R1–R24, não é a peça de estado de reserva BSL1, não é a arquitetura de nível técnico L6 e não é uma interrupção registrada da Harbor Library.

**Ambiente:** biblioteca padrão do Python 3, em memória. Sem arquivos, chamadas de rede, credenciais reais ou modificações de serviço.

**Tarefa de previsão:** Antes de executar, preveja quais funções permanecem em cada cenário e se o resultado significa disponibilidade modelada de edição pela equipe, só recepção de pedidos, ou nenhuma rota modelada de edição pela equipe nem de recepção.

O modo de resumo classifica só os caminhos de edição pela equipe e de recepção de pedidos. Leia a lista separada `available` antes de dizer se a visão de salas ou qualquer outra função permanece possível.

###### Programa Python completo

~~~python
ROUTES = {
    "site_reachable": {"web"},
    "room_view": {"web", "database"},
    "staff_edit": {"web", "identity", "database"},
    "manual_intake": {"helpdesk"},
    "new_backup_job": {"database", "backup"},
}

CASES = [
    ("BASE", set()),
    ("DATABASE_DOWN", {"database"}),
    ("IDENTITY_DOWN", {"identity"}),
    ("HELPDESK_DOWN", {"helpdesk"}),
    ("WEB_DOWN", {"web"}),
    ("DATABASE_AND_HELPDESK_DOWN", {"database", "helpdesk"}),
]

def assess_failed(failed):
    available = sorted(
        name for name, needs in ROUTES.items()
        if needs.isdisjoint(failed)
    )
    impaired = sorted(set(ROUTES) - set(available))

    if "staff_edit" in available:
        mode = "STAFF_EDIT_PATH_MODELED"
    elif "manual_intake" in available:
        mode = "NO_STAFF_EDIT_INTAKE_MODELED"
    else:
        mode = "NO_EDIT_OR_INTAKE_PATH"

    return available, impaired, mode

for name, failed in CASES:
    available, impaired, mode = assess_failed(failed)
    print(
        f"{name}: available={','.join(available)} "
        f"impaired={','.join(impaired)} mode={mode}"
    )

assert assess_failed({"database"})[2] == "NO_STAFF_EDIT_INTAKE_MODELED"
assert "room_view" not in assess_failed({"database"})[0]
~~~

Preveja as seis linhas de saída antes de rodar o programa e, em seguida, compare o resultado com a [resolução PATH1](#ir-rapid-ch01-path1-result) no apêndice final. Mantenha PATH1 separado da evidência de caso da série R.

<a id="w1-review-03"></a>

#### Unidade de revisão da semana 1, número 3 — Rejeitar nomes desconhecidos; modelar estados desconhecidos

##### Objetivo e contraexemplo

Distinga um **identificador inválido de componente** de um **componente válido com estado desconhecido**. Em seguida, explique por que um pré-requisito falho e conhecido pode estabelecer prejuízo modelado mesmo quando outro pré-requisito está sem resolução.

O [PATH1](#ir-rapid-ch01-path1-lab) original avalia um conjunto de componentes falhos. Se o conjunto fornecido é `{"databsae"}`, o nome com erro de grafia não intersecta nenhum dos cinco conjuntos de dependência de rota. A função original, em consequência, devolve toda função modelada como disponível. Esta é uma limitação reproduzível de fronteira de entrada, não um relatório de que uma base ou um serviço real estava saudável.

Uma guarda de identificador deve rejeitar essa grafia em vez de adivinhar que o autor pretendia `database`. Correção silenciosa poderia ocultar uma fonte errada, uma mudança de esquema ou um componente diferente. Peça uma entrada corrigida explícita e preserve a original.

Um problema diferente surge quando `database` está grafado corretamente, mas o estado não é conhecido. Rejeitar o nome seria errado; entrar `False` inventaria uma interrupção; entrar `True` inventaria disponibilidade. A extensão usa `None` para representar esta condição desconhecida definida de forma estreita, com todo componente explicitamente presente no dicionário de estado.

##### Raciocine por três estados

PATH1 define cada rota como um conjunto de **todos exigidos**. Sob esse modelo, uma função é:

| Classificação | Significado sob o modelo declarado de dependência |
|---|---|
| `IMPAIRED` | Pelo menos um componente exigido é explicitamente falso. |
| `UNRESOLVED` | Nenhum componente exigido é falso, mas pelo menos um é desconhecido. |
| `POSSIBLE` | Todo componente exigido é explicitamente verdadeiro. |

Considere a edição pela equipe, que exige web, identidade e base. Com web e identidade verdadeiras e base desconhecida, a rota está sem resolução. Com web verdadeira, identidade falsa e base desconhecida, a rota está prejudicada qualquer que seja a resolução posterior da incerteza da base. O pré-requisito falho e conhecido é suficiente **dentro deste modelo**. Essa conclusão não identifica a causa de uma interrupção real, não quantifica dano nem estabelece que uma arquitetura alternativa está ausente.

A recepção manual depende só de `helpdesk` no PATH1. Se `helpdesk` é verdadeiro, essa rota pode permanecer possível enquanto a edição pela equipe está prejudicada. “Possível” ainda significa uma rota modelada, não uma reserva de sala confirmada, um procedimento alternativo aprovado ou entrega observada de serviço.

##### Extensão reproduzível do PATH1

Rode primeiro a listagem original completa do PATH1 numa sessão nova. Preveja manualmente as quatro primeiras linhas novas. O laço final confere todas as `3^5 = 243` atribuições parciais entre os cinco componentes. Para cada atribuição, enumera toda atribuição booleana completa consistente com os desconhecidos declarados e compara os resultados possíveis de cada função com a classificação de três estados.

Esta comparação é um cálculo independente sobre um **modelo finito declarado**. Não verifica topologia real, medições, permissões, caminhos alternativos nem correção do serviço. Para sistemas reais, as próprias premissas exigem observação autorizada e revisão do responsável.

~~~python
# Run after the complete PATH1 listing, in the same Python session.
W1_COMPONENTS = frozenset().union(*ROUTES.values())

def w1_assess_failed(failed):
    if type(failed) not in (set, frozenset):
        raise ValueError("INVALID_FAILURE_SET")
    if not failed.issubset(W1_COMPONENTS):
        raise ValueError("UNKNOWN_COMPONENT")
    return assess_failed(failed)

def w1_assess_state(state):
    if type(state) is not dict or set(state) != set(W1_COMPONENTS):
        raise ValueError("COMPONENT_SET_MISMATCH")
    if any(value is not None and type(value) is not bool for value in state.values()):
        raise ValueError("INVALID_COMPONENT_STATE")
    result = {}
    for function, needs in sorted(ROUTES.items()):
        values = [state[component] for component in needs]
        if any(value is False for value in values):
            result[function] = "IMPAIRED"
        elif any(value is None for value in values):
            result[function] = "UNRESOLVED"
        else:
            result[function] = "POSSIBLE"
    return result

try:
    w1_assess_failed({"databsae"})
except ValueError as error:
    print("W1_TYPO", str(error))
w1_state = {component: True for component in W1_COMPONENTS}
w1_state["database"] = None
print("W1_UNKNOWN_DB", w1_assess_state(w1_state)["staff_edit"])
w1_state["identity"] = False
print("W1_UNKNOWN_DB_IDENTITY_DOWN", w1_assess_state(w1_state)["staff_edit"])
print("W1_MANUAL", w1_assess_state(w1_state)["manual_intake"])

# Independent finite check: compare each partial assignment with every
# complete Boolean assignment consistent with it. No real system is queried.
from itertools import product
w1_names = sorted(W1_COMPONENTS)
w1_checked = 0
for values in product((False, True, None), repeat=len(w1_names)):
    partial = dict(zip(w1_names, values))
    unknown = [name for name in w1_names if partial[name] is None]
    completions = []
    for fill in product((False, True), repeat=len(unknown)):
        complete = {**partial, **dict(zip(unknown, fill))}
        completions.append(complete)
    actual = w1_assess_state(partial)
    for function, needs in ROUTES.items():
        outcomes = {all(complete[name] is True for name in needs) for complete in completions}
        expected = ("POSSIBLE" if outcomes == {True} else
                    "IMPAIRED" if outcomes == {False} else "UNRESOLVED")
        if actual[function] != expected:
            raise AssertionError((partial, function, actual[function], expected))
    w1_checked += 1
print("W1_PARTIAL_STATES_CHECKED", w1_checked)
~~~

##### Prática suplementar W1-R3

**Objetivo:** justificar um resultado sob conhecimento incompleto de componentes. **Entradas:** as cinco funções PATH1, as dependências originais e a extensão acima. **Artefato exigido:** a transcrição de cinco linhas; uma tabela das cinco funções com a base desconhecida e todos os outros componentes verdadeiros; uma segunda tabela depois de só a identidade se tornar falsa; e uma mensagem de duas frases ao responsável pelo serviço, distinguindo recepção modelada de aceitação confirmada de reserva. **Restrições:** não transforme desconhecido em falso, não repare o erro de grafia em silêncio e não importe qualquer falha modelada para R1–R8.

**Avaliação:** um ponto para cada um: rejeição do erro de grafia, a primeira tabela completa de funções, a segunda tabela completa, a mensagem limitada ao responsável pelo serviço, e a explicação do que a enumeração finita não verifica. O EX003 original ainda exige os dois cartões de dependência; esta tabela é prática suplementar separada. [Resolução](#w1-answer-03).

*Rubrica:* 3 = cinco pontos da fonte: rejeição do erro de grafia, duas tabelas completas, mensagem limitada e o que a enumeração de 243 não verifica;; 2 = a maior parte desses pontos, com uma omissão de limite;; 1 = responde, mas omite fonte, limite ou trata estado desconhecido como falha;; 0 = nenhum.

##### Síntese da revisão

Um nome inválido é um defeito de entrada. Um estado desconhecido é uma premissa sem resolução. Um pré-requisito falho e conhecido pode resolver uma rota modelada sem resolver toda outra incerteza.

#### Marco resolvido

Se a aplicação de reservas responde, mas o estado autoritativo da reserva é desconhecido, disponibilidade não é correção de negócio. Um caminho de recepção manual pode preservar uma promessa limitada ao usuário, mas não pode ser chamado de aceitação confirmada de reserva sem reconciliação aprovada pelo responsável.

#### Prática — Aula 03

##### EX003 — Dependência de serviço

**Objetivo:** ligar um sinal de incidente a resultados de serviço e a donos de evidência. **Entradas:** o mapa de serviço da seção 1.2 e R1–R8. **Saída:** um cartão de dependência de duas linhas com dependência, dano possível ao usuário, ponteiro fornecido, evidência discriminante ausente e custodiante. Escolha duas dependências; para cada uma, explique o que uma verificação autorizada distinguiria. Não chame um dano potencial de interrupção confirmada. Uma nota 2 precisa de duas dependências diferentes e de um teste que possa separar um problema de estado de serviço de uso indevido de conta.

**Extensão:** Para cada uma das duas dependências de serviço escolhidas, distinga um *dano possível de negócio a jusante* de uma observação real. Nomeie um teste negativo que poderia enfraquecer a explicação proposta e identifique quem estaria autorizado a pedi-lo.

**Para crédito completo:** Uma resposta de 2 pontos liga explicitamente fontes técnicas diferentes a decisões diferentes. Os valores atuais de reserva da base não podem ser inferidos diretamente do histórico de edição de R3–R4.

**Tarefa suplementar PATH1 (depois do artefato exigido):**

**Requisito adicional:** Depois dos dois cartões de dependência existentes, escolha uma função modelada PATH1 e identifique uma falha de componente que a prejudicaria. Declare uma verificação autorizada *funcional* e uma verificação separada de *correção de negócio*. Não alegue que a falha PATH1 ocorreu em R1–R8 canônicos.

**Resolução:** [EX003 no apêndice final](#ex003--worked-result).

*Rubrica:* 3 = nota 2 da fonte: duas dependências diferentes, um teste que separa estado de serviço de uso indevido de conta, e a tarefa PATH1 sem importar a falha para R1–R8;; 2 = os dois cartões existem, mas falta o teste que separa as explicações;; 1 = responde à pergunta, mas omite fonte, limite, autoridade ou trata dano possível como interrupção confirmada;; 0 = nenhum.

##### EX008 — Qualidade da evidência

**Objetivo:** limitar alegações ao que três tipos diferentes de fonte de fato dizem. **Entradas:** R6–R8. **Saída:** uma tabela de limite de evidência com três linhas, com identificador e hora, conclusão estreita sustentada, conclusão tentadora sem suporte, e uma fonte ou teste de acompanhamento. Uma nota 2 trata uma atividade agendada como distinta de uma mudança de reserva aprovada, um trabalho de cópia concluído como distinto de uma restauração provada, e um resumo sem detalhe de destino como distinto de uma ausência verificada de transferência.

**Tarefa suplementar PATH1 (depois do artefato exigido):**

**Requisito adicional:** Na linha de estado de cópia de R7, explique por que a disponibilidade modelada de `new_backup_job` não verificaria restauração utilizável, recuperação decorrida aceitável nem correção de reserva aprovada pelo responsável. Preserve as limitações originais de fonte do treinamento em R6 e do resumo de rede em R8.

**Resolução:** [EX008 no apêndice final](#ex008--worked-result).

*Rubrica:* 3 = nota 2 da fonte: três linhas que separam agenda de aprovação, trabalho de cópia de restauração provada, e resumo sem destino de ausência de transferência;; 2 = as três linhas existem, mas uma conclusão sem suporte é tratada como sustentada;; 1 = responde à pergunta, mas omite fonte, limite ou o teste de acompanhamento;; 0 = nenhum.

##### EX011 — Gatilho de escalada

**Objetivo:** especificar quando a escolha inicial precisa ser reaberta. **Entradas:** o instantâneo R1–R8 e a seção 1.9. **Saída:** duas linhas **hipotéticas** de observação e resposta, com a fonte que verificaria o sinal, o dano ou a incerteza afetada, o dono da decisão e a próxima ação. Um gatilho deve tratar de mudança contínua de reserva; o outro deve tratar de amplitude ou impacto no serviço. Uma nota 2 afirma que nenhuma das observações está presente às 09:05 e evita uma ação automática de produção sem aprovação.

**Extensão de linha de base de comportamento:** Para o gatilho hipotético de impacto no serviço, especifique uma comparação futura, aprovada pelo responsável, do estado de reserva contra a versão aplicável da política, com o responsável pelo serviço confirmando regra e escopo. Mantenha o outro gatilho sobre uma edição nova, inexplicada e verificada à parte. Nenhum dos sinais está presente em R1–R8; um descompasso de regra não prova comprometimento cibernético.

**Resolução:** [EX011 no apêndice final](#ex011--worked-result).

*Rubrica:* 3 = nota 2 da fonte: dois gatilhos hipotéticos, nenhum presente às 09:05, sem ação automática de produção, e descompasso de regra distinto de comprometimento;; 2 = os dois gatilhos existem, mas um é tratado como observação já presente;; 1 = responde à pergunta, mas omite fonte, limite, autoridade ou aprovação;; 0 = nenhum.

<!-- open-cyber-academy:lesson-navigation:start lesson-03 -->
#### Continue estudando — aula 03 de pelo menos 20

[← Aula 02](#lesson-02) · [Índice de aulas do curso](../SUBJECTS.md) · [Aula 04 →](#lesson-04)

Siga para a próxima aula diária escrita neste manuscrito.
<!-- open-cyber-academy:lesson-navigation:end -->
<a id="lesson-04"></a>

### Aula 04 — Autoridade, delegação e ensaio antes do incidente

**Semana 1, dia 4.** Percorra o ensino e o marco resolvido antes de tentar os exercícios indicados. Compare o seu artefato com a resolução final só depois.

#### 1.3 Papéis e autoridade de decisão

Uma organização pequena pode atribuir vários papéis a uma pessoa, mas as decisões permanecem distintas:

| Papel | Responsabilidade principal neste curso | Decisão que precisa de um dono |
|---|---|---|
| Responsável pelo serviço | Explica o dano ao serviço e a interrupção aceitável | Se uma interrupção é tolerável |
| Líder do incidente | Mantém prioridades, escopo e registro de decisão | Se escalar a resposta |
| Analista | Confere sinais, reúne evidência autorizada e declara incerteza | Qual hipótese a evidência sustenta |
| Responsável pela recuperação | Testa opções de restauração e dependências | Se um passo proposto de recuperação está tecnicamente pronto |
| Contato de comunicação ou de privacidade | Coordena avisos exatos e revisão de tratamento de dados | O que pode ser dito, a quem e quando |

O analista não deve desligar um serviço só porque um painel parece incomum. O responsável pelo serviço não pode decidir que os logs são irrelevantes porque o serviço parece disponível. O líder do incidente reúne donos e evidência, registra a decisão e a revisita quando os fatos mudam.

Um **registro de decisão** útil contém um carimbo de tempo, a situação atual, as opções disponíveis, a ação escolhida, a pessoa que a aprovou, a evidência que a sustenta, os efeitos esperados e uma hora de revisão. Registre também opções rejeitadas quando elas explicam um compromisso importante. Um registro breve feito durante o incidente é mais confiável do que uma história reconstruída semanas depois.

##### Separe recomendação, aprovação, execução e verificação

Uma pessoa pode desempenhar mais de um papel numa equipe pequena, mas quatro verbos devem permanecer visíveis no registro do caso. O **analista recomenda** uma ação e cita observações. Uma pessoa responsável **aprova** o escopo e o compromisso. Um operador **executa** a mudança limitada. Um revisor **verifica** se a mudança alcançou o objetivo e registra qualquer dano. Nenhum desses verbos pode ser inferido com segurança só a partir de um cargo. O [NIST SP 800-61 Rev. 3, seções 2.2–2.3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) discute papéis distribuídos de resposta e a necessidade de autoridades e procedimentos documentados; o registro de quatro verbos abaixo é o dispositivo de ensino da OpenCyber Academy para tornar essas autoridades observáveis.

| Proposta fictícia | Recomenda | Aprova sob as regras do exercício | Executa | Verifica |
|---|---|---|---|---|
| Manter uma cópia autorizada dos registros de reserva | Analista | Líder do incidente | Analista | O líder do incidente confere escopo e ponteiros de registro |
| Restringir temporariamente `desk-a` | Analista com o administrador de identidade | Líder do incidente e responsável pelo serviço, quanto ao impacto no serviço | Administrador de identidade | O analista confere o resultado de acesso; o responsável pelo serviço confere o trabalho da recepção |
| Pausar escritas de reserva de sala | Responsável pelo serviço e líder da resposta | Responsável pelo serviço, sob a regra simulada de emergência | Operador da aplicação | O responsável pelo serviço confere reservas e pedidos em fila |

Essas atribuições são **regras fictícias de exercício**. Não são uma alegação sobre a autoridade legal de qualquer organização real nem uma instrução para desconectar um sistema de produção. Uma aprovação útil diz mais do que “pode seguir”: nomeia o alvo, a ação, a duração, a interrupção esperada, a evidência a preservar, o gatilho de reversão e a próxima revisão. Se uma ação urgente é necessária, mas o aprovador designado não pode ser alcançado, o líder da resposta segue a política aprovada de escalada da organização; quem estuda não deve inventar autoridade a partir do silêncio.

Considere uma recomendação de restringir `desk-a` depois de R1–R5. O analista pode declarar um benefício plausível: edições adicionais não autorizadas poderiam parar. O analista também precisa declarar um custo plausível: a equipe da recepção poderia perder o acesso num período movimentado. Nem o benefício nem o custo estão medidos ainda. Um registro de decisão que diz “conta comprometida; desabilitar imediatamente” esconde tanto a incerteza quanto a autoridade. Um registro provisório melhor é: “Às 09:05 UTC, preservar os registros fornecidos e buscar a confirmação do responsável pelo treinamento até 09:15; se aparecer uma edição nova e inexplicada de reserva, reconvocar o líder do incidente, o responsável pelo serviço e o administrador de identidade para uma restrição aprovada.” O horário e o limiar aqui pertencem a este caso sintético, não a uma política universal de resposta.

#### 1.3a Ensaiar a autoridade antes de um incidente

##### 1.3a.1 De conhecer um cargo a provar uma rota utilizável de decisão

Um plano de resposta pode dizer corretamente que o responsável pelo serviço aprova uma interrupção e o líder do incidente aprova uma coleta limitada. Essa afirmação é necessária, mas não basta para saber que uma decisão futura pode ser executada de forma lícita e segura. E se o responsável principal mudou de cargo no mês passado? E se o substituto listado pode autorizar uma pausa pequena de reserva de sala, mas não uma exportação de dados de frequentadores sem relação? E se a rota de aprovação funciona no horário de expediente, mas ninguém testou o canal de contato designado? E se a delegação foi revogada ou a data passou?

Uma equipe de resposta a incidentes deve descobrir tais lacunas **antes** de um evento real forçar uma escolha difícil. A pergunta de preparação não é “Uma pessoa aparece num organograma?”. É **“Um revisor consegue reconstruir um caminho exato e atualmente válido, de um pedido nomeado até o decisor e o custodiante responsáveis, com escopo explícito e um resultado seguro quando o caminho falha?”**

A seção 1.3 distingue recomendação, aprovação, execução e verificação. AR1 pede aos estudantes que **ensaiem se esses estágios são alcançáveis por meio dos registros atuais de autoridade**. Um ensaio bem-sucedido antes do incidente demonstra apenas que as regras simuladas de roteamento e verificação foram aplicadas corretamente para uma versão e um horário declarados. Não pré-aprova ações posteriores nem estabelece que uma pessoa real respondeu a uma mensagem real.

O [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) coloca o planejamento e a coordenação de resposta a incidentes dentro da gestão de risco do Cybersecurity Framework 2.0. O [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) trata do desenho, da condução e da avaliação de testes e exercícios de planos de TI. O registro versionado de autoridade e o procedimento de validação desenvolvidos aqui são **técnicas educacionais originais** para explorar essas preocupações documentadas, não formulários prescritos pelo NIST.

##### 1.3a.2 Um nome de papel não é prova de que uma pessoa particular detém autoridade

Um mapa de serviço pode nomear “responsável pelo serviço”, “administrador de identidade”, “custodiante da aplicação” e “líder do incidente”. Cada rótulo descreve responsabilidade, mas o rótulo sozinho não estabelece qual pessoa ocupa o papel agora, quais ações específicas ela pode aprovar, nem se um substituto listado pode assinar em nome do titular.

Um **papel** é uma categoria de responsabilidade. Uma **nomeação** associa esse papel a uma identidade organizacional verificada por um tempo declarado. Uma **delegação** dá um subconjunto definido de autoridade a outra pessoa ou papel, sob termos explícitos. Um **custodiante** administra um objeto ou uma fonte e pode executar um pedido autorizado, mas não é automaticamente dono da decisão de risco de negócio. Um **solicitante** pode explicar por que a evidência é necessária; ser o solicitante não é o mesmo que conceder o pedido.

Antes de um incidente, um revisor deve conseguir localizar o registro governado e autoritativo de cada nomeação e delegação, junto com o emissor, o estado de aprovação, a versão e o período de validade. Numa organização real, esse registro pode depender de situação empregatícia, grupos de gestão de identidade, delegações formais ou outros sistemas governados. O exercício da OpenCyber Academy não assume nenhuma implementação particular.

Um nome digitado numa planilha é evidência mais fraca do que uma nomeação atual, revista pelo responsável e sustentada pelo processo autoritativo da organização. Uma entrada de lista de contatos pode continuar útil depois que uma pessoa deixa um papel, mas deixa de ser fonte válida de decisão, a menos que o sistema de governança diga o contrário. Se o revisor não consegue estabelecer a nomeação, o resultado correto é **reter a ação e escalar**, não tratar a familiaridade com o nome da pessoa como prova de autoridade.

##### 1.3a.3 Estabeleça um registro versionado com perguntas explícitas de aceitação

Um **registro de prontidão de autoridade** útil precisa de mais do que colunas de nome e telefone. Precisa dizer a um revisor independente se a rota proposta de decisão é válida para a operação em consideração. No mínimo, deve identificar:

| Campo do registro | O que o revisor precisa estabelecer |
|---|---|
| Identificador e versão do registro | Qual edição foi conferida, e se ainda é atual |
| Papel que emite e mantém | Quem responde pelas nomeações e pelas correções do registro |
| Intervalo de vigência e de revisão | Quando esta edição começa e deixa de ser usada como base |
| Serviço e operação | Qual sistema de negócio e qual classe de decisão ela governa |
| Papel primário de decisão | Quem pode aprovar esta operação definida |
| Custodiante ou operador | Quem pode receber o pedido autorizado e executar a tarefa limitada |
| Substituto delegado | Quem pode substituir o titular, sob qual autoridade documentada |
| Restrições do delegado | Operação permitida, objetos, duração e qualquer aprovação adicional exigida |
| Caminho de confirmação | Rota independente aprovada para confirmar a identidade do respondente e o mandato atual |
| Campos exigidos do recibo | Como pedido, escopo da decisão, versão e aprovação são registrados |
| Verificações negativas | O que precisa ser rejeitado antes de se confiar na permissão |
| Escalada segura | Qual processo de governança ou de liderança do incidente recebe pedidos bloqueados sem conceder autoridade nova |

O próprio registro também precisa de **proveniência**. Um arquivo chamado `latest-authority.xlsx` não é evidência adequada de ser o mais recente. Um identificador de mudança, um emissor responsável, uma revisão registrada e uma transição de versão devem tornar possível determinar se uma cópia local está obsoleta. O leitor deve saber qual sistema é autoritativo e como resolver um conflito entre duas cópias.

Um registro pode ser uma tabela em papel para o exercício introdutório. A habilidade ensinada é validar um conjunto explícito de alegações, não escolher uma base de dados ou um fornecedor de tíquetes em particular. Os campos são escolhas fictícias de desenho instrucional; nenhuma fonte NIST é apresentada como exigindo este esquema exato.

##### 1.3a.4 O escopo pertence à delegação, não apenas ao pedido original

Suponha que o responsável pelo serviço pode autorizar uma pausa temporária de uma rota de escrita de reserva da equipe. Um substituto pode receber autoridade delegada para **aquela pausa específica**, por um período curto. Essa delegação não permite automaticamente ao substituto aprovar uma restauração de base de produção, desabilitar toda conta, recuperar registros do boletim de frequentadores ou estender a pausa indefinidamente.

O pedido precisa, portanto, ser comparado com a **operação permitida e o escopo de objetos** no registro. O mesmo substituto nomeado pode ter autoridade diferente para coleta de evidência e para um controle disruptivo de serviço. Um delegado aprovado para uma operação deve ser rejeitado para outra, a menos que um registro válido separado a cubra.

A peça AR1 usa duas atividades deliberadamente estreitas. Primeiro, um pedido para revisar uma seleção sintética de auditoria de treinamento contendo só `TR-01` ou `TR-02` exige a decisão do líder fictício do incidente e um custodiante designado de auditoria. Segundo, um pedido para *preparar* uma pausa de escrita da equipe exige os papéis fictícios de decisão do líder do incidente e do responsável pelo serviço; um substituto documentado pode preencher o papel de responsável pelo serviço só para essa classe estreita de pausa.

Isto é um ensaio de **validade da rota**, não a execução de qualquer das ações. A saída `REHEARSAL_PATH_VALID_NOT_EXECUTED` nunca significa “auditoria coletada” nem “pausa de escrita aplicada”. Num incidente real, a equipe ainda precisaria de uma decisão atual de negócio, de autorização de coleta ou de mudança, de recibo do operador, de verificação técnica e das salvaguardas aplicáveis de privacidade.

A verificação de escopo deve falhar fechada. Se o pedido inclui um objeto sem relação, o verificador não deve ignorar em silêncio esse objeto e aprovar o resto como se o pedido original estivesse inalterado. Deve devolver uma condição de retenção e exigir um pedido corrigido de forma explícita.

##### 1.3a.5 Períodos de validade e expiração são controles operacionais de segurança

A autoridade de um substituto pode ser válida só por um intervalo especificado. Um revisor precisa conhecer tanto o início efetivo quanto o último instante válido, e deve usar uma base de tempo consistente. No modelo de ensino AR1, a delegação vigora das 13:00 até **antes das 14:30 UTC** na data fictícia do ensaio. Uma verificação às 14:15 pode satisfazer a condição de tempo; uma verificação às 14:31 não pode.

A regra estrita importa: **uma delegação antes válida não é válida indefinidamente**. O fato de uma pessoa ter aprovado algo ontem não lhe concede o mesmo escopo hoje. Um registro também pode expirar como um todo. Um delegado não pode ser tratado como atual sob uma edição que o processo de governança já não aceita, só porque a data individual da delegação parece recente.

O exercício deve distinguir expiração de revogação. **Expiração** significa que o intervalo de validade delegada decorreu. **Revogação** significa que uma decisão governada retirou a delegação antes do fim nominal. Qualquer das duas deve bloquear a confiança no substituto para a operação afetada.

Se um carimbo de tempo falta ou não pode ser comparado, não selecione o valor que faz o teste passar. O estado apropriado é *tempo ou autoridade não verificados*, sujeito a revisão. O script AR1 assume carimbos com consciência de UTC e rejeita dois casos explícitos de expiração; não substitui autenticar relógios em registros organizacionais reais.

Uma expiração que se aproxima também pode ser um gatilho de manutenção de prontidão. A equipe deve revisar delegações críticas antes dos prazos, identificar o próximo responsável aprovado e ensaiar a rota atualizada. Isso impede que uma lista de contatos se torne um ponto único e silencioso de falha.

##### 1.3a.6 O dono, o aprovador e o custodiante podem ser pessoas diferentes

Um pedido pode ser válido no propósito de negócio e ainda ser encaminhado ao custodiante errado. Por exemplo, um responsável pelo serviço pode aprovar uma interrupção limitada enquanto um operador da aplicação é o único papel permitido a aplicá-la. Um líder do incidente pode aprovar um pedido estreito de evidência enquanto o custodiante da aplicação recupera os registros. Um coletor pode não estar autorizado a aprovar coleta ampliada só porque possui acesso técnico.

O registro deve modelar tanto **quem pode decidir** quanto **quem pode executar a tarefa aprovada**, como verificações separadas. Um aprovador válido com um executor inválido não é uma rota válida de execução. Por outro lado, um executor válido sem aprovação válida não deve executar a ação.

No AR1, o pedido imaginário de auditoria de treinamento nomeia um custodiante de auditoria; o pedido de pausa de escrita da equipe nomeia um operador da aplicação. Trocar os dois produz um resultado de **custodiante errado** mesmo quando o escopo pedido e os campos de aprovador estão corretos no resto.

Isto não pretende impor um requisito de toda a organização de que cada papel de equipe pequena seja ocupado por um humano distinto. O livro já explica que organizações pequenas podem combinar papéis. O requisito relevante é que as **decisões lógicas e a evidência de cada estágio permaneçam distinguíveis**. Uma única pessoa que ocupa vários papéis documentados ainda precisa exercer cada papel dentro da autoridade aplicável.

Quando o mesmo indivíduo proporia, aprovaria e executaria uma mudança de alto impacto, a organização pode exigir revisão independente adicional segundo a governança real. AR1 não cria tal requisito nem concede exceções. Ensina a registrar a pergunta de política sem resolução, em vez de inventar uma regra de separação de deveres.

##### 1.3a.7 Use uma rota registrada de confirmação, não uma resposta não verificada

Conhecer o papel correto não basta se o pedido chega por um canal não confiável ou não registrado. Uma mensagem de uma conta que exibe um nome familiar pode não autenticar a pessoa nem o papel atual. Um indicador de entrega bem-sucedida de e-mail não estabelece autoridade de decisão.

Um ensaio de prontidão de autoridade deve especificar **como o solicitante pode verificar uma resposta por uma rota obtida de forma independente do registro aprovado**. Um conceito comum é um retorno de chamada ou um canal organizacional confiável de confirmação. O método concreto numa implantação real depende dos controles de identidade, da política de comunicações e do modelo de ameaça da organização.

O script AR1 representa este requisito complexo pelo campo literal `registered-callback` e por um sinalizador booleano de confirmação. São **asserções de brinquedo** fornecidas pelo exercício. Não são prova de identidade, desafio secreto, assinatura criptográfica, telefonema real nem consentimento.

A pergunta anterior ao incidente é: o plano nomeia uma rota testada que permitiria a um revisor distinguir um aprovador válido de um impostor ou de um contato obsoleto? Um processo que diz “envie um e-mail ao responsável”, mas não tem procedimento para verificar uma instrução surpreendente ou de alto impacto, permanece incompleto.

Um ensaio negativo deve fornecer de propósito um canal de mensagem não registrado e confirmar que a ação proposta é retida. Outro deve reter a confirmação mesmo quando o nome e a rota coincidem. Em nenhum dos casos a equipe pode interpretar o silêncio como aprovação.

Este conceito difere do laboratório DEL4 do módulo 4 da edição inglesa, que não está neste manuscrito e testa entrega de mensagem, reconhecimento de versão e leitura de volta **durante coordenação simulada de incidente**. AR1 testa a **confiança anterior ao incidente no próprio caminho de autoridade**, antes de qualquer ação de incidente ser selecionada.

##### 1.3a.8 Um recibo de aprovação precisa identificar a decisão limitada

Um revisor fictício pode receber uma resposta que diz “aprovado”. Essa palavra, sozinha, é insuficiente se não identifica o pedido, o alvo e o escopo, o papel do respondente, a versão aplicável do registro e se a aprovação permanece atual. Uma aprovação pode ser genuína para uma tarefa e irrelevante para outra.

Um recibo planejado útil identifica o identificador do pedido, a decisão, a operação, os objetos, o papel e a identidade de quem aprova, a rota de confirmação, a hora, as restrições, a expiração ou a condição de revisão, e a versão do registro que governa. A organização real pode usar um processo estabelecido de tíquete ou de mudança; este capítulo não prescreve um sistema novo de produção.

AR1 usa um marcador pequeno `SIM-RECEIPT` para representar a presença de um recibo fictício de aprovação. Se o marcador está ausente, o validador de brinquedo devolve `HOLD_APPROVAL_MISSING`. A presença desse marcador **não autentica o aprovador nem autoriza uma ação real**; apenas permite a quem estuda praticar a verificação de que um recibo distinto faz parte da rota planejada.

Este é um limite epistêmico importante. Software pode conferir se campos existem e se valores cabem numa regra. Não pode estabelecer automaticamente que uma pessoa real autorizou de forma consciente uma interrupção de serviço, a menos que os processos organizacionais circundantes de identidade e de decisão forneçam essa evidência.

Durante um ensaio, rotule explicitamente o resultado como caminho simulado válido, não executado. Isso evita o modo de falha em que um “exercício bem-sucedido” é copiado para um tíquete real de incidente e confundido com uma aprovação real.

##### 1.3a.9 Dois exemplos contrastantes completos: uma delegação válida e um substituto inseguro

**Exemplo correto — rota limitada, atual e confirmada num ensaio anterior ao incidente.**

Na data inventada de ensaio 2026-09-15 às 14:15 UTC, a versão do registro é `AR-3` e está dentro do intervalo declarado de validade. Um pedido de prática concerne só a operação fictícia `pause_staff_writes` do recurso `staff-write-route`. O líder simulado do incidente `lead-sim` tem um recibo separado de decisão. O responsável nomeado pelo serviço `owner-sim` emitiu uma delegação documentada e não revogada, permitindo a `alternate-sim` preencher o papel de aprovação do responsável pelo serviço **só para esta operação e este objeto**, com vigência das 13:00 até antes das 14:30 UTC. O papel executor designado é `app-operator-sim`.

Ambas as aprovações fictícias têm recibos de treinamento com escopo e confirmações pela rota `registered-callback` declarada no registro. O validador devolve `REHEARSAL_PATH_VALID_NOT_EXECUTED`. A interpretação correta é: **as condições especificadas de roteamento passaram no exercício isolado**. Nenhuma pausa de produção foi aprovada, executada ou verificada; nenhuma identidade de pessoa real foi autenticada por este script.

Um pacote adequado a uma revisão anterior ao incidente, com duas pessoas, preservaria a versão do registro, o escopo e a expiração do delegado, os campos simulados de aprovação, o operador esperado, a hora da verificação, as condições de parada e o resultado. O revisor que recebe o pacote poderia reproduzir a decisão e identificar qual evidência uma implementação real precisaria.

**Exemplo incorreto — um substituto plausível, mas expirado e não verificado.**

Às 14:31 UTC, numa execução artificial diferente, o intervalo permitido do mesmo delegado terminou. Suponha que alguém copia o nome antigo do responsável de uma lista de contatos, acrescenta um pedido que afeta objetos sem relação de reserva ou de boletim, e o envia por uma conta de conversa não registrada dizendo que o assunto é urgente. O pedido não é válido só porque o substituto antes detinha uma delegação relevante ou porque o canal está disponível.

A primeira rejeição aplicável pode ser **delegação expirada** ou **escopo excedido**, conforme o que o validador confere primeiro. Um revisor real deve registrar **todos** os defeitos descobertos no trabalho de correção do caso, não interpretar uma saída de programa como aprovação de tudo o que ela não mencionou. A equipe não deve fabricar uma delegação nova nem permitir que o custodiante aja com base nesse pedido.

A **resposta correta** é reter a coleta ou a mudança de serviço, identificar a rota responsável de escalada de governança ou de liderança do incidente, obter um registro atual ou um aprovador designado por canais autorizados, e registrar a decisão sem resolução. Escalada é uma tentativa de obter autoridade, não uma forma alternativa de autoridade.

Estes dois exemplos não são eventos do incidente R1–R8 e não devem ser inseridos na linha do tempo das 09:05.

##### 1.3a.10 Um caminho seguro de escalada não concede permissão

Um caminho de contato de emergência pode ser necessário quando o aprovador ordinário ou o substituto não pode ser validado. Mas a palavra “escalar” é muitas vezes mal usada no sentido de “encontrar qualquer pessoa sênior o bastante para dizer sim”. Essa abordagem mina a razão de registrar delegações e autoridade limitada.

Um procedimento válido de escalada especifica **quem recebe a decisão bloqueada**, qual informação pode ser revelada, qual papel verifica a nomeação atual, como obter ou esclarecer autorização, e o que o operador técnico **não** deve fazer enquanto a decisão está sem resolução.

Para um pedido de coleta cuja aprovação falta, o analista pode continuar avaliando registros **já fornecidos e autorizados** sob o escopo permitido. Isso não autoriza acesso a um sistema novo. Para uma mudança potencialmente disruptiva sem rota verificada do responsável pelo serviço, o coordenador pode documentar riscos e pedir uma decisão válida; não autoriza execução com base só na urgência.

AR1 inclui `SAFE_ESCALATION`. A saída é `ESCALATE_HOLD_DELEGATION_EXPIRED`: uma escalada é pedida **enquanto a ação original permanece retida**. Isto é deliberadamente diferente de `REHEARSAL_PATH_VALID_NOT_EXECUTED`.

Um programa mais forte do mundo real poderia ter um mecanismo documentado à parte de autorização de emergência. Se assim for, o escopo, os pré-requisitos, o aprovador responsável e a verificação precisariam ser testados como outra regra de autoridade explicitamente versionada. AR1 nem assume nem inventa tal mecanismo.

Isto difere da repetição F1 do módulo 4 da edição inglesa, ausente deste arquivo, em que um aprovador fica indisponível **durante** uma resposta fictícia. O exercício atual testa, em vez disso, se o **registro anterior ao incidente e o processo de alternativa estão prontos e atuais**, bem antes de qualquer incidente da série R começar.

##### 1.3a.11 Um registro precisa ser testado contra controles negativos

Uma lista de contatos pode parecer correta no caminho mais fácil e falhar quando uma pessoa sai, uma delegação expira ou um pedido muda de escopo. Um teste significativo de prontidão precisa, portanto, de **controles positivos e negativos**.

O controle positivo pergunta se os aprovadores corretos, o escopo, a versão, o custodiante, os recibos e os sinalizadores de confirmação produzem uma aprovação limitada de prontidão. Outro controle positivo testa o delegado especificamente documentado dentro da janela válida de tempo. Essas verificações demonstram só a lógica do registro simulado.

Os controles negativos mudam de propósito **uma propriedade de cada vez**: substituir o aprovador pela pessoa errada, ampliar os objetos pedidos, omitir o recibo de aprovação, usar uma versão desatualizada do registro, mudar o custodiante, usar um canal de confirmação não aprovado, suprimir a confirmação, revogar um delegado, ou avançar a hora do teste além da expiração. Cada um deve produzir um motivo distinto de retenção.

Por que insistir nisto? Se o verificador aceita todo teste, pode não estar impondo nenhuma restrição real. Se rejeita até pedidos válidos, a organização poderia ser incapaz de agir com eficiência quando um incidente real exige uma decisão. A qualidade de um controle de prontidão depende dos dois tipos de comportamento.

O laboratório produz um código primário de rejeição, para reprodutibilidade. Numa revisão real, outros defeitos podem coexistir. Os revisores devem evitar declarar que todos os campos não relatados eram válidos só porque o verificador parou na primeira falha.

Um controle negativo não cria um incidente. Mudar a data de um recibo de treinamento para simular expiração não significa que a delegação real de alguém expirou.

##### 1.3a.12 Deriva de versão e cópias paralelas

Registros de autoridade mudam com frequência quando empregados rodam, serviços passam de equipe ou contatos de emergência são atualizados. Um ensaio anterior ao incidente deve incluir uma **verificação de consistência de versão**. O solicitante, o papel aprovador e o custodiante devem ter um modo confiável de determinar que estão usando a mesma edição atual do registro.

No AR1, a versão `AR-3` é a edição sintética atual. Um pedido copiado que ainda se refere a `AR-2` falha com `HOLD_STALE_REGISTER`. O programa não tenta inferir que a edição mais antiga ainda possa estar “perto o bastante”.

Há um intervalo separado de validade do registro inteiro. A edição de exemplo só é aceita de 1º de setembro até antes de 1º de outubro de 2026. Uma verificação em 2 de outubro devolve `HOLD_REGISTER_OUT_OF_DATE` mesmo quando o conteúdo, no resto, se parece com um pedido válido.

Essas verificações respondem a perguntas diferentes. Um **descompasso de versão** significa que o pedido não se apoia na edição atual designada; a **expiração do registro** significa que o período declarado de confiança da edição passou. Um delegado individual também pode expirar enquanto o próprio registro permanece válido. Um teste de qualidade distingue os três, em vez de chamar todos de “erro de contato”.

Se duas cópias remotas discordam, nenhum título de planilha nem valor em cache local deve vencer só porque é conveniente. O dono de governança da organização precisa de uma fonte autoritativa definida e de um caminho de correção. O líder da resposta deve reter qualquer ação cuja autoridade não possa ser resolvida com segurança.

##### 1.3a.13 Prova de identidade e prova de autoridade são independentes

Quem liga pode ser genuinamente a pessoa que afirma ser e ainda carecer de autoridade para uma coleta ou uma interrupção particulares. Por outro lado, uma entrada de diretório pode listar corretamente um papel que agora pertence a outra pessoa. O exercício deve, portanto, distinguir **confiança de identidade** de **confiança de escopo de decisão**.

Um método aprovado de retorno pode ajudar a validar quem está respondendo, assumindo que a organização real o implementa de forma adequada. Não estabelece que a delegação do respondente cobre todos os objetos. Uma delegação versionada pode estabelecer o escopo documentado, mas não prova que uma mensagem particular foi enviada pelo delegado listado. As duas verificações importam.

As cadeias literais do AR1 não são autenticação. O campo `confirmed=True` é fornecido pelo instrutor como premissa de entrada; nenhum desafio-resposta, token de acesso, assinatura ou telefonema real é executado. O script não pode verificar o quadro de empregados, números reais de telefone nem aprovações organizacionais atuais.

Um estudante introdutório deve ser capaz de dizer: “O campo sintético de identidade coincidiu com o delegado esperado e a rota sintética foi declarada confirmada; num ambiente real eu precisaria de confirmação autenticada e de um registro autoritativo e atual de delegação antes de confiar em qualquer dos dois.” Isso é mais defensável do que alegar que o código autenticou um humano.

O revisor também precisa evitar usar o registro como permissão para reunir registros de identidade sem relação. Autoridade para aprovar um pedido de auditoria de reserva não é um direito ilimitado de investigar toda pessoa associada ao serviço.

##### 1.3a.14 Artefatos de ensaio e evidência de encerramento

Um ensaio útil anterior ao incidente deixa para trás mais do que uma captura de tela de aprovação. O pacote de evidência deve identificar a versão testada do registro, a operação simulada, o escopo de objetos afetados, a hora da verificação, os papéis primário e alternativo de decisão, o custodiante designado, o requisito da rota de confirmação, a entrada da peça, o estado esperado e o estado real.

Deve registrar à parte que o exercício usou **identidades e recibos fictícios**, que nenhuma ação de produção ocorreu e que o programa não autenticou nenhuma fonte real. Um revisor independente deve conseguir executar de novo o mesmo script e entender por que cada caso negativo foi retido.

Um tíquete de correção pode ser aberto se um ensaio encontra um substituto desatualizado ou ausente, um escopo ambíguo, nenhum canal aprovado de confirmação, períodos de delegação sobrepostos, ou um responsável sem caminho definido de retorno. Um tíquete não se encerra só por atualizar uma página de contatos. O teste de encerramento deve repetir os casos positivos e negativos relevantes sob uma versão revista do registro e reter o resultado.

Por exemplo, uma correção de delegação obsoleta poderia exigir: um administrador nomeado do registro, um registro atual datado, um sucessor documentado, uma operação e uma expiração explicitamente limitadas, uma rota confirmada de retorno e um teste independente no qual o delegado antigo expirado é rejeitado enquanto a rota designada atual passa. Isso é uma melhoria mensurável de capacidade.

O avaliador do treinamento deve evitar atribuir uma porcentagem de “correção da autoridade organizacional” com base nos casos de brinquedo. Um teste sintético pequeno valida só as peças especificadas.

##### 1.3a.15 Como usar esta preparação sem contaminar a Rodada A

O incidente canônico da Harbor Library começa com R1–R8, não com o ensaio AR1. A tabela da série R relata uma entrada, acesso ao painel, mudanças de reserva, um relato de frequentador, treinamento agendado, conclusão de um trabalho de cópia e um resumo de rede com detalhe de destino ausente. Não contém o quadro do AR1, datas de emissão de delegação, recibos de aprovação nem rotas de confirmação.

Quem responde às 09:05 pode usar a **prática geral** aprendida com AR1: confirmar o responsável adequado, o escopo e a aprovação antes de ampliar a coleta ou restringir o serviço. Mas não pode afirmar “o responsável já aprovou porque o AR1 passou”, nem incluir o pessoal inventado do ensaio como atores reais da Harbor Library.

O próprio caso do capítulo 01 autoriza uma análise limitada de sala dos registros sintéticos fornecidos, e só isso. Toda coleta adicional de evidência e toda mudança de controle semelhante à de produção permanecem propostas, a menos que o caso fictício forneça explicitamente uma aprovação e um resultado posteriores. AR1 não acrescenta tal resultado.

Numa organização futura, a validação de autoridade antes do incidente reduz um tipo de incerteza; não elimina a necessidade de uma decisão contemporânea no momento da resposta. O sucesso de um ensaio anterior pode sustentar confiança no procedimento e ainda exigir verificações atuais de nomeação, escopo específico do caso, aprovação e recibos de execução.

Esta é a distinção-chave em relação a D1 (a fonte proposta de evidência existe e funciona?), BSL1 (o serviço atende a um invariante de negócio aprovado?), PATH1 (quais funções dependem de quais componentes?) e F1 (o que acontece quando um aprovador fica indisponível durante um incidente?). **AR1 avalia o caminho governado de permissão na preparação**, antes de qualquer dessas ações ser necessária. F1 pertence a material posterior da edição inglesa e não está neste manuscrito.

##### 1.3a.16 Síntese da seção

Um mapa de autoridade não está completo só porque os nomes dos papéis são sensatos. Uma equipe deve conseguir determinar se a versão atual do registro é válida, se a pessoa correta ou o delegado documentado pode aprovar uma operação e um escopo de objetos exatos, se o custodiante designado é apropriado, se a decisão foi confirmada por uma rota aprovada, e se uma condição ausente ou inválida interrompe o pedido.

Um caminho simulado válido não deve se tornar uma aprovação real. Um caminho inválido deve levar a uma retenção documentada e a uma escalada segura, não à substituição silenciosa por uma pessoa que soa sênior. O estudante que consegue fazer essas distinções está mais bem preparado para coordenar sob pressão sem tratar a urgência como autorização.

A peça Python a seguir fornece um conjunto reproduzível de verificações positivas e negativas de autoridade. Devolve de propósito **nenhuma ação executada de produção** em todo cenário.

<a id="ir-rapid-ch01-ar1-lab"></a>

#### 1.3b Laboratório offline AR1 — autoridade versionada e verificações de delegação

**Classificação:** Laboratório inteiramente fictício, anterior ao incidente, executado contra um registro inventado. **Não** é um incidente, um diretório real de empregados, uma aprovação organizacional, um retorno autenticado, evidência da série R nem a repetição F1 durante o incidente.

**Objetivo de aprendizagem:** Conferir operação pedida e escopo de objetos, versão atual do registro, aprovador nomeado ou delegado válido, custodiante, recibo, rota de confirmação e expiração antes de permitir até uma aprovação simulada de caminho de prontidão. Demonstrar que a escalada **retém** o pedido inseguro em vez de autorizá-lo.

**Ambiente:** só a biblioteca padrão do Python 3. Tudo corre em memória. Sem arquivos, rede, contas, telefonia, aplicações de conversa, credenciais, operações privilegiadas ou dados pessoais.

**Peça:** O registro artificial de autoridade é `AR-3`, declarado válido de 1º de setembro até antes de 1º de outubro de 2026. O delegado separado `alternate-sim` pode preencher o papel de responsável pelo serviço só para a operação de treinamento `pause_staff_writes` em `staff-write-route`, das 13:00 até antes das 14:30 UTC em 15 de setembro, salvo se revogado. O exemplo de auditoria de treinamento concerne só `TR-01` e `TR-02`. As identidades literais são apelidos de papel e não correspondem a humanos reais.

##### Programa reproduzível

~~~python
from datetime import datetime
from copy import deepcopy

def utc(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

REGISTRY = {
    "version": "AR-3",
    "valid_from": utc("2026-09-01T00:00Z"),
    "valid_until": utc("2026-10-01T00:00Z"),
    "approver": {
        "incident_lead": "lead-sim",
        "service_owner": "owner-sim",
    },
    "delegation": {
        "delegate": "alternate-sim",
        "role": "service_owner",
        "operations": {"pause_staff_writes"},
        "scope": {"staff-write-route"},
        "valid_from": utc("2026-09-15T13:00Z"),
        "valid_until": utc("2026-09-15T14:30Z"),
        "revoked": False,
    },
    "custodians": {
        "training-audit": "audit-custodian-sim",
        "staff-write-route": "app-operator-sim",
    },
}

RULES = {
    "collect_training_audit": {
        "resource": "training-audit",
        "allowed": {"TR-01", "TR-02"},
        "roles": ("incident_lead",),
    },
    "pause_staff_writes": {
        "resource": "staff-write-route",
        "allowed": {"staff-write-route"},
        "roles": ("incident_lead", "service_owner"),
    },
}

def approval(principal, receipt="SIM-RECEIPT",
             route="registered-callback", confirmed=True):
    return {
        "principal": principal,
        "receipt": receipt,
        "route": route,
        "confirmed": confirmed,
    }

BASE = {
    "version": "AR-3",
    "as_of": utc("2026-09-15T14:15Z"),
    "operation": "collect_training_audit",
    "resource": "training-audit",
    "objects": {"TR-01"},
    "executor": "audit-custodian-sim",
    "approvals": {"incident_lead": approval("lead-sim")},
    "escalate": False,
}

PAUSE = {
    **deepcopy(BASE),
    "operation": "pause_staff_writes",
    "resource": "staff-write-route",
    "objects": {"staff-write-route"},
    "executor": "app-operator-sim",
    "approvals": {
        "incident_lead": approval("lead-sim"),
        "service_owner": approval("alternate-sim"),
    },
}

def evaluate(c, registry=REGISTRY):
    reason = None
    if c["version"] != registry["version"]:
        reason = "STALE_REGISTER"
    elif not (registry["valid_from"] <= c["as_of"]
              < registry["valid_until"]):
        reason = "REGISTER_OUT_OF_DATE"
    elif c["operation"] not in RULES:
        reason = "UNKNOWN_OPERATION"
    else:
        rule = RULES[c["operation"]]
        if not c["objects"]:
            reason = "EMPTY_SCOPE"
        elif (c["resource"] != rule["resource"]
                or not c["objects"].issubset(rule["allowed"])):
            reason = "SCOPE_EXCEEDED"
        elif c["executor"] != registry["custodians"][c["resource"]]:
            reason = "WRONG_CUSTODIAN"
        else:
            for role in rule["roles"]:
                item = c["approvals"].get(role)
                if item is None or not item.get("receipt"):
                    reason = "APPROVAL_MISSING"
                    break

                if item["principal"] != registry["approver"][role]:
                    delegate = registry["delegation"]
                    if (item["principal"] != delegate["delegate"]
                            or role != delegate["role"]
                            or c["operation"] not in delegate["operations"]
                            or not c["objects"].issubset(delegate["scope"])):
                        reason = "WRONG_APPROVER"
                        break
                    if delegate["revoked"]:
                        reason = "DELEGATION_REVOKED"
                        break
                    if not (delegate["valid_from"] <= c["as_of"]
                            < delegate["valid_until"]):
                        reason = "DELEGATION_EXPIRED"
                        break

                if item["route"] != "registered-callback":
                    reason = "UNAPPROVED_CHANNEL"
                    break
                if not item["confirmed"]:
                    reason = "CONFIRMATION_MISSING"
                    break

    if reason is None:
        return "REHEARSAL_PATH_VALID_NOT_EXECUTED"
    if c["escalate"]:
        return "ESCALATE_HOLD_" + reason
    return "HOLD_" + reason

CASES = [
    ("VALID_AUDIT", BASE),
    ("VALID_DELEGATED_PAUSE", PAUSE),
    ("EXPIRED_DELEGATE",
     {**PAUSE, "as_of": utc("2026-09-15T14:31Z")}),
    ("WRONG_PERSON",
     {**PAUSE, "approvals": {
         **PAUSE["approvals"],
         "service_owner": approval("visitor-sim")}}),
    ("EXCESS_SCOPE",
     {**BASE, "objects": {"TR-01", "newsletter-sim"}}),
    ("EMPTY_OBJECTS",
     {**BASE, "objects": set()}),
    ("APPROVAL_ABSENT",
     {**PAUSE, "approvals": {
         "incident_lead": approval("lead-sim")}}),
    ("STALE_VERSION", {**BASE, "version": "AR-2"}),
    ("WRONG_CUSTODIAN",
     {**BASE, "executor": "app-operator-sim"}),
    ("BAD_CHANNEL",
     {**BASE, "approvals": {
         "incident_lead": approval(
             "lead-sim", route="unregistered-chat")}}),
    ("NO_CONFIRMATION",
     {**BASE, "approvals": {
         "incident_lead": approval(
             "lead-sim", confirmed=False)}}),
    ("REVOKED_DELEGATE", PAUSE, {
        **REGISTRY,
        "delegation": {**REGISTRY["delegation"], "revoked": True},
    }),
    ("EXPIRED_REGISTER",
     {**BASE, "as_of": utc("2026-10-02T14:15Z")}),
    ("MISSING_RECEIPT",
     {**BASE, "approvals": {
         "incident_lead": approval(
             "lead-sim", receipt="")}}),
    ("SAFE_ESCALATION",
     {**PAUSE,
      "as_of": utc("2026-09-15T14:31Z"),
      "escalate": True}),
]

for name, case, *overrides in CASES:
    registry = overrides[0] if overrides else REGISTRY
    print(name, evaluate(case, registry))

assert evaluate(BASE) == "REHEARSAL_PATH_VALID_NOT_EXECUTED"
assert evaluate({**BASE, "objects": set()}) == "HOLD_EMPTY_SCOPE"
assert evaluate(CASES[11][1], CASES[11][2]) == "HOLD_DELEGATION_REVOKED"
assert (evaluate(CASES[-1][1])
        == "ESCALATE_HOLD_DELEGATION_EXPIRED")
~~~

##### Verificação de aprovação presa ao pedido (ensaio suplementar AR1)

O programa AR1 existente modela corretamente o sinalizador de revogação do registro governado, o escopo não vazio de objetos, delegados válidos, o custodiante permitido e o canal aprovado de confirmação. Os quinze resultados publicados se reproduzem corretamente. Contudo, a função central `evaluate` testa se um item simulado de aprovação **existe**; não testa se o **registro da decisão emissora** prende esse item ao identificador *específico* do pedido, à operação, à fonte e ao conjunto de objetos.

Por exemplo, a proposta original `BASE` pede `TR-01` e inclui um recibo fictício genérico chamado `SIM-RECEIPT`. Se o pedido é mudado para outro objeto de resto permitido, `TR-02`, enquanto o mesmo recibo é reutilizado, a função original devolve `REHEARSAL_PATH_VALID_NOT_EXECUTED`. Esta é uma **limitação reproduzível do validador de brinquedo**. Não é evidência de que uma organização real aprovou o segundo objeto.

A lição de governança anterior ao incidente não deve chamar esse segundo pedido de aprovado. O registro simulado de aprovação precisa estar associado a um identificador estável de pedido **e** à operação, ao recurso, aos objetos e ao papel aprovados. A verificação suplementar seguinte introduz um *registro fictício do lado do emissor*, pequeno e independente, que o solicitante não pode redefinir em silêncio dentro do cartão avaliado. Não fornece autenticação real de identidade, assinatura digital nem permissão válida de produção.

##### Listagem suplementar AR1 em Python 3 — rode depois do programa AR1 completo já existente

~~~python
# These are invented issuer-side approval records for the classroom.
# The original AR1 program must have been executed first, so BASE,
# PAUSE, RULES, REGISTRY and evaluate are already defined.
SIMULATED_ISSUED_APPROVALS = {
    ("TRAIN-001", "incident_lead"): (
        "lead-sim", "SIM-RECEIPT",
        "collect_training_audit", "training-audit",
        frozenset({"TR-01"})
    ),
    ("PAUSE-001", "incident_lead"): (
        "lead-sim", "SIM-RECEIPT",
        "pause_staff_writes", "staff-write-route",
        frozenset({"staff-write-route"})
    ),
    ("PAUSE-001", "service_owner"): (
        "alternate-sim", "SIM-RECEIPT",
        "pause_staff_writes", "staff-write-route",
        frozenset({"staff-write-route"})
    ),
}

def evaluate_with_approval_binding(card):
    preliminary = evaluate(card)
    if preliminary != "REHEARSAL_PATH_VALID_NOT_EXECUTED":
        return preliminary

    for role in RULES[card["operation"]]["roles"]:
        item = card["approvals"][role]
        presented = (
            item["principal"], item["receipt"],
            card["operation"], card["resource"],
            frozenset(card["objects"])
        )
        issued = SIMULATED_ISSUED_APPROVALS.get(
            (card.get("request_id"), role)
        )
        if presented != issued:
            return "HOLD_RECEIPT_SCOPE_MISMATCH"
    return preliminary

valid_audit = {**BASE, "request_id": "TRAIN-001"}
valid_pause = {**PAUSE, "request_id": "PAUSE-001"}

reused_receipt = {
    **valid_audit, "objects": {"TR-02"}
}
wrong_reference = {
    **valid_audit, "request_id": "PAUSE-001"
}

for name, card in (
    ("REQUEST_SCOPED_TR01", valid_audit),
    ("REQUEST_SCOPED_PAUSE", valid_pause),
    ("REUSED_RECEIPT_TR02", reused_receipt),
    ("REUSED_REQUEST_ID", wrong_reference),
):
    print(name, evaluate_with_approval_binding(card))

assert (
    evaluate_with_approval_binding(valid_audit)
    == "REHEARSAL_PATH_VALID_NOT_EXECUTED"
)
assert (
    evaluate_with_approval_binding(valid_pause)
    == "REHEARSAL_PATH_VALID_NOT_EXECUTED"
)
assert (
    evaluate_with_approval_binding(reused_receipt)
    == "HOLD_RECEIPT_SCOPE_MISMATCH"
)
assert (
    evaluate_with_approval_binding(wrong_reference)
    == "HOLD_RECEIPT_SCOPE_MISMATCH"
)
~~~

Antes de rodar qualquer dos programas, preveja quais caminhos passam, quais são retidos e se a escalada muda a autoridade. Rode primeiro a listagem original e compare a transcrição de 15 linhas com a [resolução AR1](#ir-rapid-ch01-ar1-result). Em seguida, rode a listagem suplementar na **mesma sessão Python** e compare as quatro linhas adicionais com a resolução presa ao pedido. Explique por que `TR-02` passa na verificação original de roteamento, mas falha na verificação separada de vínculo da aprovação. Em particular, o **registro**, não o pedido, controla a revogação; um conjunto vazio de objetos não é um pedido limitado válido.
<a id="w1-review-04"></a>

#### Unidade de revisão da semana 1, número 4 — Uma cadeia não é uma confirmação

##### Objetivo e mecanismo

Explique por que uma verificação de tipo pertence antes da avaliação de autoridade, e por que não deve substituir a própria avaliação de autoridade.

O [AR1](#ir-rapid-ch01-ar1-lab) original lê `if not item["confirmed"]`. Sob as [regras documentadas de valor de verdade do Python](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), uma cadeia não vazia é verdadeira. Em consequência, os caracteres `"false"` não se comportam como o booleano `False`. Converter essa cadeia com `bool()` não corrige o significado. Do mesmo modo, testes de igualdade sozinhos podem borrar valores booleanos e inteiros; este portão de ensino exige de propósito o tipo booleano exato.

O defeito não é que o teste original `confirmed=False` do AR1 estivesse errado: essa linha de base ainda produz uma retenção. O contraexemplo adicional usa um tipo diferente. Na fonte revista, o pedido de resto válido com `confirmed="false"` passa tanto na função original de roteamento quanto na verificação posterior de recibo preso ao pedido. A verificação de recibo protege a associação do pedido, não a interpretação do campo booleano. Dois controles úteis podem, portanto, coexistir com uma fronteira de entrada não testada.

Esta demonstração concerne **só o validador de brinquedo**. O sinalizador original de confirmação já era uma premissa simulada, não um retorno real nem uma prova de identidade. O portão novo de tipo impede uma categoria de interpretação não pretendida; não pode tornar o sinalizador fornecido um fato autenticado.

##### Preserve verificações separadas

Mantenha estas perguntas em ordem: o campo é interpretável sob este contrato; a confirmação de fato diz verdadeiro; o papel atual e a delegação cobrem o pedido exato; o recibo está preso a esse pedido; e que prova do mundo real seria exigida antes de confiar em qualquer dessas premissas?

O invólucro proposto confere a forma do contêiner de aprovação e os tipos booleanos exatos de confirmação, escalada e do sinalizador de revogação do registro atual. Em seguida chama o avaliador **existente** preso ao recibo, retendo as verificações originais de papel, custodiante, escopo e tempo. Isto deliberadamente não é um validador completo de esquema: campos sem relação ausentes, carimbos malformados, objetos personalizados arbitrários e autenticidade permanecem fora da cobertura alegada.

Não mapeie todo texto inesperado para falso. Um descompasso de esquema e uma confirmação negativa explícita são achados diferentes. Não escale automaticamente uma entrada malformada porque uma cadeia acontece de ser verdadeira. O resultado seguro é uma retenção visível de entrada e um pedido de um registro corretamente tipado e sustentado pela fonte.

##### Extensão reproduzível do AR1

Rode o programa AR1 original **e** a listagem de aprovação presa ao pedido numa sessão nova. A extensão abaixo não edita `BASE`, `PAUSE` nem as aprovações aninhadas; os exemplos alterados usam cópias independentes. Preveja oito linhas novas de saída. Preste atenção particular ao extremo exato das 14:30: o fim do delegado é exclusivo no contrato original.

~~~python
# Run after AR1 AND its request-bound approval listing, in the same session.
# This adds a narrow type gate. It is not a full request-schema validator.
def w1_evaluate_typed(card):
    if type(card) is not dict or type(card.get("approvals")) is not dict:
        return "HOLD_INPUT_APPROVAL_SHAPE"
    if type(card.get("escalate")) is not bool:
        return "HOLD_INPUT_ESCALATE_TYPE"
    if type(REGISTRY["delegation"].get("revoked")) is not bool:
        return "HOLD_INPUT_REVOCATION_TYPE"
    for item in card["approvals"].values():
        if type(item) is not dict or type(item.get("confirmed")) is not bool:
            return "HOLD_INPUT_CONFIRMATION_TYPE"
    # Do not replace the role/scope/time/receipt checks with the type check.
    return evaluate_with_approval_binding(card)

w1_text_false = deepcopy(valid_audit)
w1_text_false["approvals"]["incident_lead"]["confirmed"] = "false"
w1_real_false = deepcopy(valid_audit)
w1_real_false["approvals"]["incident_lead"]["confirmed"] = False
print("W1_ORIGINAL_TEXT_FALSE", evaluate_with_approval_binding(w1_text_false))
print("W1_TYPED_TEXT_FALSE", w1_evaluate_typed(w1_text_false))
print("W1_TYPED_REAL_FALSE", w1_evaluate_typed(w1_real_false))
print("W1_TYPED_VALID", w1_evaluate_typed(valid_audit))
print("W1_TYPED_REUSED_RECEIPT", w1_evaluate_typed(reused_receipt))
for clock in ("13:00", "14:29", "14:30"):
    card = {**valid_pause, "as_of": utc("2026-09-15T" + clock + "Z")}
    print("W1_DELEGATE_" + clock, w1_evaluate_typed(card))
~~~

##### Prática suplementar W1-R4

**Objetivo:** distinguir rejeição de entrada, não confirmação explícita, rejeição de escopo do pedido e expiração de delegação. **Entradas:** as regras originais do AR1, os recibos sintéticos emitidos e as oito chamadas acima. **Artefato exigido:** oito linhas de saída; uma comparação de quatro linhas entre texto falso, booleano falso, verdadeiro válido e recibo reutilizado; mais uma verificação de delegação em três horários, 13:00, 14:29 e 14:30. Explique por que passar no portão novo de tipo não é uma aprovação nova.

**Restrições:** não acrescente credenciais reais nem detalhes de retorno; mantenha inalterado o vínculo do recibo emitido; use o intervalo semiaberto original do delegado; preserve as quatro linhas de responsabilidade do EX006 e o registro de três linhas de lacunas do EX013 mais o tíquete. **Avaliação:** um ponto para cada um: a distinção de tipo, a retenção explícita de falso, o vínculo preservado do recibo, o limite exato de expiração e a recusa de alegar autorização real. [Resolução](#w1-answer-04).

*Rubrica:* 3 = cinco pontos da fonte: distinção de tipo, retenção de falso explícito, vínculo do recibo, limite exato de expiração e recusa de autorização real;; 2 = a maior parte desses pontos, com uma omissão de limite;; 1 = responde, mas omite fonte, limite ou trata uma cadeia como confirmação;; 0 = nenhum.

##### Síntese da revisão

Um booleano corretamente tipado é um campo utilizável, não consentimento autenticado. Um recibo preso ao pedido e um portão de tipo tratam de modos diferentes de falha; nenhum substitui o outro.

#### 1.3c Ensaio de prontidão AR1 com dois papéis

**Objetivo:** Antes de um incidente simulado, verificar que uma segunda pessoa consegue reconstruir a rota correta de autoridade a partir do **registro atual e do pacote de pedido**, identificar uma delegação expirada ou fora de escopo, e escolher uma escalada segura sem pedir ao autor do pacote que invente uma aprovação ausente.

**Papéis:** **Administrador do registro / autor do pacote** e **revisor independente de prontidão**. Um facilitador pode observar, mas não muda os resultados declarados depois de ver a primeira resposta do revisor.

**Únicos dados permitidos:** O registro artificial AR1, o pedido sintético e os recibos simulados. Nenhum detalhe real de empregado, diretório de empresa, telefone, credencial ou serviço pode ser usado.

##### Fase 1 — O autor congela o pacote

O administrador prepara `AR1-packet-v1` e registra:

1. Identificador do registro, versão, papel emissor, intervalo de vigência e estado da fonte.
2. Operação de treinamento e conjunto permitido de objetos.
3. Papel primário de aprovação e delegado nomeado, inclusive emissor, escopo da operação, validade e estado de revogação.
4. Custodiante ou operador executor da tarefa selecionada.
5. Rota declarada e registrada de confirmação, e o que uma confirmação real teria de estabelecer.
6. Um identificador simulado de pedido, a hora selecionada, a operação pedida e os objetos nomeados.
7. A saída segura esperada se o caminho primário ou alternativo não puder ser verificado.
8. A afirmação explícita **“só revisão de treinamento; nenhum incidente atual nem autorização de produção.”**

O pacote precisa ser congelado antes de o revisor começar. Um campo ausente permanece ausente; o autor não pode reparar o registro em silêncio depois de conhecer a objeção do revisor.

##### Fase 2 — O revisor reconstrói de forma independente

Dê ao revisor um **cenário válido** claramente rotulado e um **cenário de delegado expirado**, nessa ordem. Sem ajuda do autor do pacote, o revisor precisa identificar: a edição atual do registro; os papéis corretos de aprovação; se o delegado nomeado ainda é válido para o pedido exato; o custodiante correto; a rota aprovada de confirmação; se todos os recibos simulados exigidos estão presentes; e a decisão de **reter** ou **escalar** se qualquer condição falha.

O revisor entrega `AR1-review-v1` com uma tabela pequena campo a campo e um parágrafo que explica o próximo passo seguro. Um revisor que diz “a pessoa é familiar, portanto aja imediatamente” falha mesmo que identifique corretamente o contato.

O revisor pode consultar o registro congelado e o pedido, mas não pode perguntar ao autor se uma delegação ausente “provavelmente existe”. Se um campo necessário à autorização está ausente, a resposta correta é **desconhecido/retenção**, com um pedido de fonte autoritativa.

##### Fase 3 — Preservar e julgar

Congele a primeira resposta. Compare a decisão com os campos da fonte e com a saída do código. Registre cada discrepância como **campo ausente do pacote**, **interpretação incorreta** ou **pergunta sem resolução de fonte ou de autoridade**. Não apague a primeira entrega quando evidência corrigida se torna disponível.

Um acompanhamento `AR1-packet-v2` pode substituir uma delegação expirada por um registro fictício recém-aprovado, mas essa versão nova precisa dos próprios testes de validade e de confirmação. A segunda tentativa não é prova de que o primeiro pacote era adequado.

##### Regras de aceitação e de falha

Uma **aprovação limitada** exige que o revisor identifique a versão correta, o serviço, a operação e o escopo, a delegação válida ou inválida, o custodiante, o requisito de confirmação e a condição segura de retenção ou escalada, sem alegar execução. Uma **falha crítica** ocorre se o revisor aceita um substituto expirado ou revogado, a pessoa errada, objetos não autorizados, um recibo de decisão ausente ou um canal não verificado como permissão para prosseguir. Uma **falha corrigível** inclui uma referência de versão ausente ou um ponteiro de pacote pouco claro que deixa o revisor incapaz de determinar a autoridade; o pedido atual permanece retido até a correção.

Isto é um **ensaio de preparação**. O desempenho não diz o que aconteceu no incidente R1–R8 da Harbor Library. Mede um procedimento pequeno e versionado de verificação de autoridade, não a confiabilidade real do quadro de emergência de uma organização real.

#### Marco resolvido

Um substituto nomeado numa lista antiga de contatos não pode aprovar uma coleta nova só pelo cargo. Compare a versão atual do registro, o escopo de objetos, a expiração e o caminho registrado de confirmação; se um falha, registre a aprovação como pendente e escale pela rota designada.

#### Prática — Aula 04

##### EX006 — Atribuição de papéis

**Objetivo:** tornar visíveis recomendação, aprovação, execução e verificação. **Entradas:** os papéis fictícios da seção 1.3, R7 e o escopo de sala. **Saída:** uma tabela de responsabilidade de quatro linhas para uma possível interrupção de reservas, a preservação de R1–R5, a coordenação da próxima revisão e um teste contido de restauração. Nomeie o dono da tarefa, quem a aprova sob as regras do exercício e o que verificaria a conclusão. Distinga **planejar** um teste de restauração de tê-lo executado. Uma nota 2 não delega uma decisão de interrupção ao analista nem trata R7 como restauração testada.

**Tarefa suplementar PATH1 (depois do artefato exigido):**

**Requisito adicional:** Mantenha a matriz original de papéis com quatro linhas. Para a possível interrupção de reservas, distinga um procedimento aprovado de recepção manual de pedidos da aceitação real de reserva; nomeie o responsável pelo serviço da decisão hipotética de modo degradado, o custodiante da central para os recibos e o revisor que autorizaria a reconciliação.

**Tarefa suplementar AR1 (depois do artefato exigido):**

**Verificação adicional:** Preserve a **tabela original de responsabilidade com quatro linhas**. Para as linhas de preservação de evidência e de possível interrupção de reservas, acrescente uma referência curta a onde uma **nomeação atual de responsável ou delegado e uma atribuição de custodiante** seriam conferidas antes de se confiar nelas. Declare qual aprovação permanece pendente se um substituto está expirado, e que evidência verificaria que um operador autorizado de fato executou uma ação posterior.

**Critério de crédito completo:** O analista, o líder do incidente, o responsável pelo serviço, o custodiante ou operador e o revisor retêm responsabilidades lógicas distintas. Uma listagem publicada de diretório não basta para provar um delegado válido, e um ensaio positivo não é uma coleta executada nem uma mudança de serviço.

**Resolução:** [EX006 no apêndice final](#ex006--worked-result).

*Rubrica:* 3 = nota 2 da fonte: quatro linhas com papéis distintos, interrupção não delegada ao analista, R7 distinto de restauração testada, e ensaio positivo distinto de execução;; 2 = as quatro linhas existem, mas um papel decide fora da autoridade do exercício;; 1 = responde à pergunta, mas omite fonte, limite, autoridade ou trata R7 como teste feito;; 0 = nenhum.

##### EX013 — Lacuna de prontidão

**Objetivo:** transformar uma fraqueza do exercício numa mudança mensurável de preparação. **Entradas:** o mapa de serviço, a tabela de autoridade, R7–R8 e o ateliê da seção 1.8. **Saída:** um registro de lacunas com três linhas, com capacidade ausente, consequência e dono; depois um tíquete de melhoria com justificativa de prioridade, mudança específica, prazo e um ensaio de aprovação ou falha. Uma nota 2 nomeia um teste que de fato demonstraria a mudança, como um ensaio de decisão do responsável e do substituto ou um ensaio contido de restauração, em vez de apenas publicar uma página de política.

**Extensão:** O tíquete de melhoria precisa incluir um ensaio falseável com critério de aprovação e de falha. Um ensaio de autoridade alternativa pode testar um aprovador primário indisponível; tíquetes defensáveis alternativos podem testar recuperação de log ou recuperação isolada.

**Para crédito completo:** Apenas escrever ou publicar uma política não satisfaz um exercício que pede a quem estuda que demonstre uma capacidade.

**Tarefa suplementar AR1 (depois do artefato exigido):**

**Verificação adicional:** Retenha o **registro de lacunas com três linhas mais um tíquete de melhoria**. Onde o registro de responsável ou substituto é identificado como lacuna, exija uma revisão versionada do registro de autoridade e um ensaio negativo de prontidão que confira delegado expirado, aprovador errado ou escopo excessivo. Defina o administrador responsável do registro, a evidência de conclusão e uma regra de falha ou reabertura. Não duplique a repetição F1 durante o incidente, que pertence a material posterior e não está neste manuscrito.

**Critério de crédito completo:** O tíquete não pode encerrar só porque uma lista de contatos foi editada. Precisa demonstrar, sob uma versão simulada congelada, que um caminho válido passa e que rotas inválidas permanecem bloqueadas, com as entradas originais e o resultado independente preservados.

**Resolução:** [EX013 no apêndice final](#ex013--worked-result).

*Rubrica:* 3 = nota 2 da fonte: três lacunas com dono, tíquete com teste que demonstra a mudança, e encerramento que não se reduz a editar uma lista de contatos;; 2 = o registro e o tíquete existem, mas o teste não é falseável;; 1 = responde à pergunta, mas omite fonte, limite, dono ou publica só uma página de política;; 0 = nenhum.

<!-- open-cyber-academy:lesson-navigation:start lesson-04 -->
#### Continue estudando — aula 04 de pelo menos 20

[← Aula 03](#lesson-03) · [Índice de aulas do curso](../SUBJECTS.md) · [Aula 05 →](#lesson-05)

Siga para a próxima aula diária escrita neste manuscrito.
<!-- open-cyber-academy:lesson-navigation:end -->
<a id="lesson-05"></a>

### Aula 05 — Escopo, registro do caso e primeira decisão limitada

**Semana 1, dia 5.** Percorra o ensino e o marco resolvido antes de tentar os exercícios indicados. Compare o seu artefato com a resolução final só depois.

#### 1.4 Escopo, autorização e segurança

Os laboratórios deste livro usam só registros sintéticos. No trabalho real, a autoridade de incidente vem de política organizacional, de um contrato, de deveres de emprego ou de aprovação escrita explícita. A autorização deve identificar os sistemas, as contas, os dados, a janela de tempo e as ações permitidas. Investigar o sistema de um parceiro, coletar dados pessoais, mudar direitos de acesso ou tirar um serviço de produção do ar pode exigir aprovação adicional.

Use a menor ação que responde à pergunta imediata. Ler uma cópia preparada de um log é diferente de alterar a fonte ao vivo. Exportar um conjunto de dados pode ampliar o número de pessoas com acesso. Uma captura de tela pode omitir o carimbo de tempo ou a consulta que a produziu. Quando a evidência puder importar mais tarde para decisões legais ou disciplinares, siga o procedimento da organização para tratamento de evidência e obtenha orientação especializada. Este curso introdutório ensina uma disciplina de registro; não certifica um processo forense.

Para o exercício da Harbor Library, o escopo permitido é uma tabela fictícia de oito registros neste capítulo. Quem estuda pode anotar, ordenar e raciocinar sobre a tabela. Não pode tentar contatar uma biblioteca real, sondar um domínio real nem testar uma conta real.

##### Escreva o escopo como uma fronteira executável

“Investigue o alerta” é vago demais para guiar uma prática segura. Um escopo útil de sala tem um **objeto** (R1–R8), uma **operação permitida** (ler, anotar e comparar), uma **operação excluída** (conectar-se a qualquer serviço ou conta reais), um **limite de tempo** (a sessão), um **dono** (o facilitador do curso ou quem estuda, para a cópia local) e uma **condição de parada** (os registros fornecidos não respondem à pergunta). Um plano real de resposta também precisa especificar a autoridade da organização e do sistema, o tratamento de dados e a rota de escalada. O escopo de sala é deliberadamente mais estreito.

Suponha que quem estuda queira investigar o dispositivo ou a origem da entrada associada à autenticação relatada de `desk-a` em **R1**. R1 identifica uma entrada bem-sucedida de conta, mas não fornece um dispositivo verificado, contexto de rede de origem nem identidade humana. O passo correto de sala é **propor** uma pergunta presa à autorização: “Administrador de identidade: se aprovado à parte, identifique a fonte estreita da entrada, o intervalo, os campos relevantes de dispositivo ou de sessão, o produtor e o fuso deles, e o método necessário para preservar e verificar esses detalhes.” Quem estuda não pode executar essa coleta a partir da tabela R1–R8 fornecida, e não pode acessar um sistema real de identidade com a força de um exercício de sala. R8 é uma **fonte diferente**: é um resumo de rede cujo **detalhe de destino** ausente impede uma afirmação sustentada sobre transferência de dados. O contexto de dispositivo ou sessão de R1 e a evidência de destino ausente em R8 não devem ser tratados como o mesmo campo nem como o mesmo pedido de custódia.

O escopo também afeta a força de uma conclusão. Se só R1–R8 estão no escopo, a frase “Não houve exfiltração” não tem suporte. R8 carece explicitamente de detalhe de destino, e quem estuda não tem registros adicionais de rede. Uma frase defensável é “O resumo de rede fornecido não permite uma conclusão sobre transferência de dados.” Isto não é escrita evasiva: diz ao próximo revisor exatamente que tipo de evidência falta.

#### 1.5 O primeiro registro de incidente

Abra um registro antes de investigar a fundo. Um mínimo prático é:

| Campo | Exemplo para o caso fictício |
|---|---|
| Identificador do caso | `HL-IR-001` |
| Aberto em | `2026-10-11 09:00 UTC` |
| Relator e canal | Tíquete `T-104` da central de atendimento |
| Serviço e responsável | Reserva de salas; responsável pelo serviço pendente de confirmação |
| Observação | R1 registra uma entrada de conta da equipe às 08:40 UTC; R3 e R4 registram mudanças de reserva às 08:43 e 08:44 UTC. O horário ordinário de funcionamento e a autorização dessas mudanças não são fornecidos. |
| Avaliação | Suspeito; comprometimento **não confirmado** |
| Escopo e autoridade | Só dados sintéticos de treinamento |
| Ponteiros de evidência | Registros `R1`–`R8` abaixo |
| Próxima pergunta | As edições foram autorizadas pelo membro da equipe? |
| Próxima revisão | `2026-10-11 09:15 UTC` |

Use **UTC de forma consistente** neste exercício. Se uma fonte usa outro fuso, retenha o carimbo original e registre a conversão, inclusive o deslocamento. Nunca reordene em silêncio eventos cujos relógios podem diferir. Dê a cada item de evidência um identificador, para que uma afirmação posterior possa citar a base.

<a id="w1-review-05"></a>

#### Unidade de revisão da semana 1, número 5 — Reparar uma observação sem suporte sem apagar a evidência

##### Objetivo e correção de fonte

Revise uma alegação que excede a fonte, preservando a cronologia útil, a incerteza e o formato exato do exercício original.

Uma versão anterior do registro de exemplo na seção 1.5 dizia que duas edições de reserva seguiram uma entrada **fora do horário ordinário**. R1 fornece a hora de entrada 08:40; R3 e R4 fornecem as horas de edição 08:43 e 08:44. R6 relata treinamento agendado das 08:30 às 09:00. Nenhum desses registros define horário ordinário de funcionamento nem uma agenda aprovada de entrada. A cronologia tem suporte; a comparação com horário ordinário não tem.

Não substitua a afirmação sem suporte pelo oposto. O pacote também não prova que a entrada foi ordinária ou aprovada. Uma boa correção remove o qualificador sem suporte e mantém a pergunta aberta.

**Observação corrigida da seção 1.5, como mostrada acima:**

> R1 registra uma entrada de conta da equipe às 08:40 UTC; R3 e R4 registram mudanças de reserva às 08:43 e 08:44 UTC. O horário ordinário de funcionamento e a autorização dessas mudanças não são fornecidos.

A prévia compartilhada da Rodada A agora identifica as **aulas 01–05 dentro do capítulo 01**. Essa correção não move os registros nem muda a fronteira de liberação. O exemplo introdutório hipotético da aula 01 ainda pode discutir o que um alerta de hora incomum poderia dizer; precisa permanecer visivelmente hipotético, e não um fato novo sobre R1.

##### Trace o suporte no nível da frase

Uma frase pode misturar uma observação válida com um qualificador sem suporte. Um revisor não deve classificar a frase inteira como perfeitamente sustentada ou inteiramente inútil. Divida-a em proposições: uma entrada foi relatada; duas edições posteriores foram relatadas; a hora era incomum; as edições foram aprovadas; uma identidade humana foi estabelecida. As duas primeiras têm ponteiros no pacote; as outras precisam de evidência não fornecida ali.

Este método também impede que uma edição de estilo se torne uma mudança factual. Substituir “cancelamento registrado” por “cancelamento não autorizado” não é apenas formulação mais forte. Acrescenta uma decisão sobre permissão. Substituir “o frequentador relatou um problema” por “o serviço falhou” acrescenta verificação independente. Um registro útil de correção guarda a formulação original, o acréscimo sem suporte, a substituição estreita e a evidência necessária para revisitá-la.

A [publicação NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) situa a resposta a incidentes dentro da gestão de risco de cibersegurança, e a [publicação CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) descreve resultados organizacionais de cibersegurança. Essas fontes fornecem contexto, não fatos da Harbor Library nem um modelo prescrito de redação. A correção de sete campos abaixo é raciocínio editorial original sobre o exercício fornecido.

##### Prática suplementar W1-R5

**Objetivo:** produzir um registro de abertura limitado pela evidência. **Entradas:** R1–R8, o contexto original da seção 1.5 `HL-IR-001` e `T-104`, o marco de abertura das 09:00, e os requisitos do EX007. **Artefato exigido:** exatamente sete campos rotulados na ordem original: identificador do caso e hora de abertura; serviço; relator e fonte; sinal observado com ponteiros; avaliação e incerteza; escopo e autoridade; próxima pergunta, dono e revisão. Acrescente uma nota separada de uma frase que explique o qualificador de horário ordinário removido.

**Restrições:** não alegue entrevista concluída, coleta, restrição, decisão das 09:05, comprometimento confirmado ou restauração testada na abertura das 09:00. Mantenha o relato do frequentador distinto de dano verificado ao estado da reserva. **Avaliação:** um ponto para cada um: hora e contexto de fonte corretos, observação limitada, autorização e estado sem resolução explícitos, escopo permitido, e uma rota proposta de dono e revisão. Um formulário de sete campos que contém fatos sem suporte ainda precisa ser corrigido. Isto suplementa o EX007; não cria EX051. [Resolução](#w1-answer-05).

*Rubrica:* 3 = cinco pontos da fonte: hora e fonte, observação limitada, autorização e estado sem resolução, escopo permitido, e rota proposta de dono e revisão;; 2 = os sete campos existem, mas um fato sem suporte permanece;; 1 = responde, mas omite fonte, limite ou trata a abertura das 09:00 como decisão das 09:05;; 0 = nenhum.

##### Síntese da revisão

Uma boa correção estreita a alegação até a evidência sem apagar a evidência. A ausência de uma regra de horário de funcionamento estabelece um desconhecido, não um evento ordinário nem extraordinário.

<a id="16-worked-example-the-unusual-sign-in"></a>

#### 1.6 Exemplo resolvido: uma entrada seguida de mudanças de reserva

Os registros sintéticos da seção 1.7 fornecem a única fonte de fatos do caso para este exemplo. R1 registra uma entrada de `desk-a` às 08:40 UTC, R3 uma mudança em B17 às 08:43, R4 um cancelamento de B18 às 08:44, e R5 um relato de frequentador às 08:48. A equipe pode dizer que a entrada precedeu ambas as edições e o relato. **Ainda não pode dizer** que a conta foi roubada, que qualquer das edições causou todo aspecto do relato, ou que dados foram exfiltrados. Um próximo passo seguro é preservar os identificadores relevantes de registro, perguntar ao responsável pelo serviço se as edições coincidem com trabalho agendado, e pedir contexto da conta da equipe por um canal autorizado. Conforme o procedimento organizacional e evidência nova, o líder do incidente pode então autorizar coleta adicional ou contenção.

A alternativa “desabilitar a conta imediatamente” tem um benefício possível se a conta está comprometida, mas pode interromper o trabalho da recepção e obscurecer se o membro da equipe está fazendo mudanças legítimas de forma ativa. A decisão correta depende de impacto, confiança, autoridade e alternativas disponíveis. Registre esse raciocínio em vez de apresentar um palpite como regra universal.

#### 1.7 Um conjunto de dados de prática contido

Use só estes registros sintéticos para os exercícios. Eles estendem o exemplo resolvido; não são evidência de um evento real.

| ID | Hora UTC | Fonte | Observação |
|---|---|---|---|
| R1 | 08:40 | Log de identidade | `desk-a` entrou com sucesso |
| R2 | 08:42 | Log da aplicação | `desk-a` abriu o painel de reservas |
| R3 | 08:43 | Log da aplicação | A reserva `B17` mudou da Room 2 para a Room 4 |
| R4 | 08:44 | Log da aplicação | A reserva `B18` foi cancelada |
| R5 | 08:48 | Central de atendimento | Um frequentador relatou que `B18` desapareceu |
| R6 | 08:50 | Calendário da equipe | O treinamento da recepção estava marcado para 08:30–09:00 |
| R7 | 08:52 | Monitor de cópia de segurança | A cópia da noite anterior terminou com sucesso |
| R8 | 08:55 | Resumo de rede | Nenhuma conclusão de rede relevante; o resumo carece de detalhe de destino |

R6 é um motivo para conferir se as edições faziam parte do treinamento; não é prova de que faziam. R7 pode sustentar o planejamento de recuperação, mas não prova que uma restauração funciona. R8 não pode provar ausência de transferência de dados. A lição é ligar uma alegação à evidência que de fato a sustenta.

##### Uma leitura de três hipóteses dos mesmos registros

Comece com três explicações que são diferentes de forma significativa. **H1: treinamento autorizado** causou as mudanças de reserva. R6 torna isto plausível porque o treinamento estava agendado; R6 não identifica quais reservas deviam mudar. **H2: alguém usou `desk-a` sem autorização.** R1–R4 são compatíveis com isto, mas não contêm prova sobre quem controlava a sessão. **H3: a visão do frequentador e o estado autoritativo da reserva diferem.** R5 sugere uma discrepância visível ao usuário, mas R4 registra um cancelamento na auditoria da aplicação, portanto H3 não pode, sozinha, explicar toda observação. As três são hipóteses, e mais de uma condição contribuinte pode estar presente.

A próxima verificação deve ser escolhida pela capacidade de **discriminar** entre essas explicações a baixo custo e dentro do escopo. Perguntar ao responsável pelo treinamento se B17 e B18 estavam especificadas no plano de treinamento pode fortalecer ou enfraquecer H1. Comparar o estado autoritativo da reserva com a visão do frequentador pode testar H3. Revisar um registro estreito e aprovado de detalhe de identidade poderia fortalecer ou enfraquecer H2. O fato de uma verificação ser útil não autoriza, por si, coletar esse registro. Se a permissão ou o dado não está disponível, registre o limite e revisite a decisão com o dono do caso.

| Alegação em revisão | Suporte fornecido | Discriminador ausente | Próximo passo seguro neste exercício |
|---|---|---|---|
| A mudança de B18 foi treinamento planejado | R6 mostra que o treinamento estava agendado; R4 mostra o cancelamento | A lista aprovada de tarefas de treinamento | Rascunhar um pedido ao responsável pelo treinamento |
| `desk-a` foi usada de forma indevida | R1–R4 estabelecem uma sessão e edições | O relato de atividade do usuário autorizado e detalhes aprovados de identidade | Registrar a pergunta e o custodiante responsável |
| O serviço pode ser restaurado | R7 mostra que um trabalho de cópia terminou | Uma restauração testada e a comparação com uma agenda autoritativa | Pedir ao responsável pela recuperação um plano contido de teste de restauração |

Isto é um exemplo de **disciplina de evidência**, não um veredito probabilístico. Com este conjunto pequeno de dados, nenhuma probabilidade numérica defensável de comprometimento pode ser calculada. Uma nota inventada a partir da intuição acrescentaria precisão aparente sem acrescentar evidência.

##### Deixe o resultado do serviço definir a pergunta de evidência

O título de um alerta diz a quem responde o que um detector notou. Não diz qual resultado de negócio está em risco. Para a Harbor Library, o resultado significativo é que moradores possam ver e reservar as salas de estudo pretendidas e que a equipe autorizada possa administrar reservas sem corromper a agenda em silêncio.

O mapa de serviço existente lista uma aplicação de reservas, um serviço de identidade da equipe, uma base de reservas, uma cópia noturna e uma central de atendimento. Cada um tem um propósito diferente de evidência. Um registro de identidade pode ajudar a investigar o contexto de autenticação de uma conta; uma auditoria da aplicação descreve uma operação relatada; uma verificação de estado autoritativo de reserva testa o que está armazenado agora; um tíquete da central registra uma experiência relatada de usuário; um monitor de cópia descreve um trabalho. Nenhum deve ser substituído por outro só porque o carimbo de tempo é conveniente.

Quem começa deve escrever uma **frase de propósito da decisão** antes de pedir evidência:

> “Preciso determinar se B17 e B18 foram mudanças autorizadas de treinamento antes de recomendar uma restrição de acesso que poderia interromper o trabalho da recepção.”

Essa frase fixa o objeto relevante, o dano suspeito, a explicação alternativa e a decisão pendente. Também impede uma expansão injustificada para a lista de contatos do boletim, sem relação, ou para todas as contas de frequentadores.

Uma pergunta útil de evidência tem dois resultados, não um. Pergunte: “O que eu concluiria se o registro pedido confirma a hipótese, e o que eu concluiria se a contradiz?” Se nenhum dos resultados mudaria a decisão, o pedido pode não ser o melhor primeiro uso de tempo limitado. Isto é um teste de valor da decisão, não uma nota matemática.

Por exemplo, o treinamento agendado em R6 torna plausível uma explicação de operação aprovada, mas R6 não lista B17 nem B18 como tarefas aprovadas. Um pedido limitado da lista datada de tarefas poderia fortalecer ou enfraquecer essa explicação. Uma busca ampla de rede, em contraste, não pode substituir a autorização de tarefa que falta só porque poderia produzir mais dados.

##### Mantenha um registro de alegações com falseadores

Um registro tem um **produtor**, um **evento relatado**, um **carimbo de tempo** e um **escopo**. O analista acrescenta uma interpretação. Manter esses elementos separados impede um atalho lógico comum: substituir “esta fonte relata X” por “X aconteceu exatamente como eu imagino”.

Use um registro de alegações com cinco colunas:

| Alegação | Ponteiro direto | Tipo | Limitação | O que poderia mudar a conclusão? |
|---|---|---|---|---|
| `desk-a` entrou | R1, 08:40, log de identidade | Observação do conteúdo do registro | Sem atribuição humana nem prova de dispositivo | Contexto estreito e autorizado de identidade e correlação validada |
| B18 foi cancelada | R4, 08:44, log da aplicação | Observação do conteúdo do registro | Sem aprovação nem confirmação do estado presente | Lista aprovada de tarefas e comparação limitada do estado atual |
| O treinamento explica as mudanças | R6 mais R3–R4 | Hipótese | Entrada de calendário não é autorização de tarefa | Lista datada e completa de tarefas de treinamento |
| O serviço pode ser restaurado depressa | R7 | Achado sem suporte | A conclusão do trabalho não dá duração nem correção da restauração | Teste isolado de restauração sob critérios de aceitação definidos pelo responsável |
| Nenhum dado foi transferido | R8 | Achado sem suporte | O detalhe de destino está ausente | Evidência de rede aprovada e adequada ao propósito, e verificação de cobertura |

A coluna “ponteiro direto” não transforma uma linha sintética em evidência autenticada de produção. Identifica a fonte exata *dentro do exercício* da qual uma afirmação foi extraída.

Uma conclusão crível também precisa de um **falseador**: uma observação que forçaria o autor a mudar a explicação atual. Se a única evidência aceitável é a que confirma a teoria favorecida, o analista não está realizando um teste significativo. Um plano aprovado de treinamento que exclui B18 enfraqueceria a explicação proposta de treinamento; um plano que inclui B18 a fortaleceria para essa edição, mas ainda não estabeleceria quem operou a sessão.

Quando a evidência está incompleta, “desconhecido” é um estado informativo. Identifica uma dependência inacabada entre pergunta e prova. Não deve ser mudado para “falso” só porque um campo ou registro falta. R8 ilustra isto diretamente: a ausência de detalhe de destino não é evidência de que não houve transferência.

##### Mantenha explícita a fronteira de informação das 09:05

Registros de incidente usam mais de um conceito de tempo. Um carimbo de evento descreve o que um produtor relatou. Uma hora de abertura do caso descreve quando o registro de resposta começou. Uma hora de decisão descreve quando informação e autoridade particulares foram usadas. Descoberta posterior não é acesso retroativo à evidência.

Neste exercício, os eventos de fonte R1–R8 têm carimbos entre 08:40 e 08:55 UTC, o caso abre às 09:00, e o primeiro marco de decisão é 09:05. Uma boa nota de decisão declara o **conjunto de evidência disponível** de forma tão explícita quanto o carimbo:

`case=HL-IR-001; checkpoint=09:05 UTC; available=R1–R8; later sources=not released`

Um revisor par pode agora perguntar se todo fato alegado estava disponível para quem decidiu. Um registro posterior com hora de evento anterior precisa permanecer excluído deste raciocínio das 09:05. Caso contrário, a revisão sofre de viés de retrospectiva: julgar uma ação anterior como se quem respondeu já conhecesse fatos recebidos depois.

Mantenha injeções hipotéticas em cartões separados. Se um treinador diz “imagine que outra edição acontece às 09:08”, quem estuda pode explicar como a decisão *mudaria*, mas não deve anexar em silêncio o evento imaginado a R1–R8. Restaurar a linha de base depois do contrafactual faz parte do exercício.

#### 1.8 Ateliê guiado de prontidão: preparar a primeira decisão

Este laboratório de papel e lápis transforma os oito registros fictícios num artefato reproduzível de caso. Não exige software, conexão de rede, conta, segredo nem pessoa real. Trabalhe a partir da tabela da seção 1.7 e das regras de papel e de escopo acima. As saídas são um cartão de serviço, um registro de evidência e um cartão de decisão. Mantenha os três artefatos juntos sob o identificador sintético de caso `HL-IR-001`.

**Passo 1 — Defina o serviço e a autoridade.** No cartão de serviço, nomeie o resultado de reserva de salas, as dependências de identidade e de base, o responsável pelo serviço a consultar e a pessoa que pode aprovar coleta de registro sob as regras do exercício. Marque o administrador de identidade como custodiante potencial de detalhes adicionais de entrada, não como fonte já consultada. Registre “só R1–R8 sintéticos” como a fronteira atual de evidência.

**Passo 2 — Construa o registro de evidência.** Copie os identificadores de registro e os horários UTC de R1, R3, R4, R5, R6, R7 e R8. Acrescente uma coluna rotulada “o que este item registra diretamente” e outra rotulada “o que ele não prova”. Por exemplo, R7 relata diretamente um trabalho de cópia concluído; não estabelece a agenda restaurada nem o tempo de recuperação. Não funda o relato do frequentador com a auditoria da aplicação num único fato sem qualificação.

**Passo 3 — Defina um marco de decisão.** No marco fictício das 09:05 UTC, proponha ou (A) preservar os registros fornecidos e verificar a explicação do treinamento antes de mudar o acesso, ou (B) pedir uma restrição temporária aprovada de `desk-a`. Para a opção escolhida, escreva o benefício esperado, o custo para o serviço, o papel aprovador, o resultado observável e a próxima hora de revisão. Registre também a opção rejeitada e a evidência que causaria reconsideração. Qualquer das escolhas pode ser defendida se premissas, urgência e autoridade estão declaradas; R1–R8 sozinhos não forçam uma resposta universal.

**Passo 4 — Execute um contrafactual.** Imagine que às 09:08 UTC um registro novo, fornecido e verificado, da aplicação mostra outra reserva editada depois da janela de treinamento agendada. Isto é uma **injeção fictícia**, não parte de R1–R8. Declare como mudaria a sua avaliação e qual aprovação você buscaria. Em seguida, remova a injeção e volte ao conjunto real de oito registros. Essa separação impede que um evento hipotético se torne em silêncio evidência do caso.

**Evidência esperada:** três artefatos rotulados com o identificador do caso, identificadores de fonte ao lado de toda afirmação factual, um estado explícito de causa não confirmada, um aprovador nomeado para qualquer ação disruptiva, e uma próxima hora de revisão. Um revisor deve conseguir reconstruir a ordem dos eventos e identificar quais afirmações foram observações, inferências ou propostas, sem perguntar ao autor.

**Rubrica de avaliação:** conceda um ponto para cada um: ponteiros exatos de evento e ordenação UTC, separação clara de fato e hipótese, autoridade e escopo atuais explícitos, comparação proporcional de opções, e um gatilho de revisão com dono. Uma nota de 5/5 mostra que o artefato está internamente completo para este exercício introdutório; **não** certifica competência de resposta a incidentes nem prova a causa do caso fictício. Um item omitido de escopo ou de aprovação precisa ser corrigido mesmo que os outros quatro pontos estejam presentes. Um exemplo resolvido aparece na seção final de respostas, depois de EX013.

*Rubrica:* 3 = 5/5 da fonte: ponteiros e ordem UTC, fato separado de hipótese, autoridade e escopo, comparação proporcional, e gatilho de revisão com dono;; 2 = quatro desses pontos, com escopo ou aprovação ainda a corrigir;; 1 = responde, mas omite fonte, limite ou autoridade;; 0 = nenhum.

#### 1.9 Construa um portão de decisão a partir de evidência incompleta

Uma resposta inicial é uma série de **decisões limitadas**, não uma busca de certeza antes de alguém agir. No marco das 09:05 UTC, o analista da Harbor Library tem oito registros fornecidos, um intervalo de treinamento agendado e duas mudanças de reserva. Os registros não dizem quem controlava `desk-a`, se B17 e B18 eram tarefas autorizadas de treinamento, nem se uma cópia poderia de fato restaurar uma agenda correta. Esses desconhecidos pedem perguntas discriminantes, não respostas inventadas. O portão de decisão abaixo é um modelo original de ensino para este caso fictício. Ilustra os papéis, a autoridade e as práticas de revisão documentados no [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final); não é uma escala de severidade prescrita pelo NIST.

| Campo do portão | Entrada sustentada às 09:05 UTC | O que a mudaria |
|---|---|---|
| Efeito observado no serviço | R3 registra que B17 foi movida; R4 registra que B18 foi cancelada; R5 registra um relato de frequentador sobre B18. O impacto completo sobre frequentadores é desconhecido. | Uma comparação, aprovada pelo responsável, de identificadores de reserva, agenda pretendida e estado atual. |
| Explicações concorrentes | R6 torna o treinamento plausível; R1–R4 também são compatíveis com uso de `desk-a` fora do propósito pretendido. | Lista aprovada de tarefas de treinamento e contexto de identidade autorizado de forma adequada. |
| Custo possível de esperar | Outra reserva incorreta pode ocorrer se edições não autorizadas continuam. Isto é um **risco**, não uma edição nova observada. | Uma linha posterior verificada de auditoria, ou um relato, ligada ao serviço de reserva. |
| Custo possível da restrição | O trabalho da recepção pode ser interrompido se `desk-a` for restringida temporariamente. O custo não foi medido. | O relato do responsável pelo serviço sobre equipe, alternativas e operações afetadas. |
| Autoridade atual | Análise de sala de R1–R8; uma restrição disruptiva exige aprovação separada sob a seção 1.3. | Uma decisão registrada do líder do incidente e do responsável pelo serviço, com alvo, duração e reversão. |
| Condição de revisão | Reavaliar às 09:15 UTC ou antes, diante de uma edição inexplicada e verificada. | Registrar o item novo e a hora de descoberta antes de mudar a decisão. |

Uma escolha defensável é preservar os registros fornecidos, perguntar ao responsável pelo treinamento sobre B17/B18 e reconvocar na hora de revisão. Isto evita uma interrupção imediata de serviço, mas aceita a possibilidade de uma edição adicional. Outra escolha defensável, se o responsável pelo serviço descreve um impacto alto de mudanças contínuas e os papéis aprovadores estão disponíveis, é buscar uma restrição temporária de conta com um fim definido e um modo de a equipe continuar o trabalho essencial. **A recomendação do analista não é permissão para executar qualquer das mudanças.** Um revisor deve perguntar que fato reverteria a escolha, quem pode autorizar a reversão, e com que rapidez o dano resultante pode ser observado.

Se o responsável pelo treinamento confirma que B17 e B18 estavam numa lista aprovada de tarefas, isso enfraquece a hipótese de que *aquelas duas* edições não eram autorizadas. Não prova a pessoa que controlava a sessão, nem resolve qualquer edição posterior B19 introduzida no módulo 2 da edição inglesa, ausente deste arquivo. Se a lista de tarefas exclui B18 e o responsável confirma que a lista está completa, a explicação de treinamento para B18 enfraquece. Se a lista não está disponível, a resposta é **desconhecida**, não “o treinamento foi descartado”. Esta distinção entre uma observação contraditória e uma observação ausente é fundamental para decisões responsáveis de incidente.

Para tornar o portão reproduzível, um segundo analista deve conseguir ler a mesma tabela R1–R8, recuperar a mesma ordem de eventos, localizar o registro de suporte de cada alegação e ver o caminho de aprovação. Se o segundo analista não consegue dizer se uma frase é um fato fornecido, uma hipótese ou uma ação proposta, reescreva-a. O módulo 2 da edição inglesa acrescenta preservação de evidência e disciplina de hora de descoberta a este mesmo caso; os registros posteriores não devem ser importados para trás na decisão das 09:05.

##### Torne a primeira decisão uma passagem reproduzível

Uma passagem deve permitir a um segundo estudante responder a seis perguntas sem pedir ao analista original contexto não documentado:

- Qual serviço e qual decisão estão no escopo?
- Quais identificadores exatos de registro sustentam as observações atuais?
- Quais hipóteses permanecem vivas, e o que poderia desconfirmá-las?
- O que foi apenas proposto, em contraste com aprovado ou executado?
- Quem é dono da próxima pergunta ou ação?
- Qual prazo ou gatilho observado exige revisão renovada?

Compare dois exemplos.

**Insuficiente:** “Atividade suspeita de administrador. Provável violação. Em investigação.”

**Revisável:** “No marco fictício das 09:05 UTC de HL-IR-001, R1 mostra uma entrada de `desk-a`, R3 e R4 relatam edições de reserva, e R5 relata uma queixa de frequentador. R6 documenta treinamento agendado, mas não a lista autorizada de tarefas. O analista não identificou um ator humano nem estabeleceu comprometimento. Pede-se ao líder do incidente que aprove uma verificação limitada junto ao responsável pelo treinamento e que revise o impacto no serviço com o responsável até 09:15 UTC; nenhuma restrição real de acesso foi executada.”

A mensagem mais longa não é melhor só porque tem mais palavras. Cada cláusula responde a uma pergunta essencial para a próxima decisão. Uma passagem que confunde um pedido proposto com uma coleta concluída pode ser mais perigosa do que uma passagem breve que marca com clareza a evidência ausente.

O [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) trata a resposta a incidentes como uma capacidade organizacional que envolve vários papéis e atividades. A passagem de seis perguntas acima é material instrucional original da OpenCyber Academy, não um formulário obrigatório do NIST.

<a id="ir-rapid-ch01-claim-lab"></a>

#### 1.10 Laboratório offline: revisão de alegações presa à evidência

**Meta:** Classificar alegações contra a liberação exata da Rodada A e demonstrar como uma fonte ausente muda uma afirmação sustentada de ensino sem mudar o incidente canônico.

**Entradas:** Os oito identificadores fictícios de registro, os carimbos e os tipos de fonte existentes, mais seis cartões de alegação de sala. Nenhuma observação nova de incidente é introduzida.

**Ambiente:** Python 3, só biblioteca padrão. A peça está em memória, não exige contas, não lê arquivos e não faz pedidos de rede.

**Antes de executar:** Preveja quais alegações podem relatar com exatidão o *conteúdo de registro* fornecido, quais permanecem hipóteses, quais excedem a semântica da fonte, e quais referenciam um registro não liberado. Em particular, não trate “conteúdo de registro disponível” como “evento real autenticado”.

~~~python
events = [
    ("R1", "08:40", "identity", "desk-a sign-in"),
    ("R2", "08:42", "application", "dashboard opened"),
    ("R3", "08:43", "application", "B17 moved"),
    ("R4", "08:44", "application", "B18 cancelled"),
    ("R5", "08:48", "helpdesk", "patron report"),
    ("R6", "08:50", "staff_calendar", "training scheduled"),
    ("R7", "08:52", "backup_monitor", "job completed"),
    ("R8", "08:55", "network_summary", "destination detail absent"),
]

assert len(events) == len({row[0] for row in events})
assert [row[1] for row in events] == sorted(row[1] for row in events)

available = {row[0] for row in events}

# Each card is an analytical claim, not another R-series event.
claims = [
    ("C01", {"R1"}, "record"),
    ("C02", {"R3", "R4", "R6"}, "hypothesis"),
    ("C03", {"R1", "R3"}, "actor"),
    ("C04", {"R7"}, "restore"),
    ("C05", {"R8"}, "no_transfer"),
    ("C06", {"R9"}, "record"),
]

def classify(refs, kind, released):
    if not refs <= released:
        return "NOT_IN_RELEASE"
    if kind == "record":
        return "RECORD_CONTENT_ONLY"
    if kind == "hypothesis":
        return "HYPOTHESIS_ONLY"
    return "NOT_ESTABLISHED"

for name, refs, kind in claims:
    print(name, classify(refs, kind, available))

# Negative test: make a temporary incomplete copy of Round A.
# This is not a deletion of canonical R6.
without_r6 = available - {"R6"}
print(
    "NEGATIVE_R6_MISSING",
    classify(claims[1][1], claims[1][2], without_r6),
)
print("EVENTS_IN_ROUND_A", len(events))
~~~

##### Saída exata esperada

~~~text
C01 RECORD_CONTENT_ONLY
C02 HYPOTHESIS_ONLY
C03 NOT_ESTABLISHED
C04 NOT_ESTABLISHED
C05 NOT_ESTABLISHED
C06 NOT_IN_RELEASE
NEGATIVE_R6_MISSING NOT_IN_RELEASE
EVENTS_IN_ROUND_A 8
~~~

##### Interpretação resolvida

**C01:** R1 está disponível. Quem estuda pode relatar que o *registro sintético de identidade* afirma uma entrada bem-sucedida de `desk-a`. A saída não é uma autenticação independente do registro nem uma atribuição humana.

**C02:** R3, R4 e R6 estão todos disponíveis. A explicação de treinamento pode ser formulada como hipótese, mas a entrada de calendário não autoriza as edições específicas. O código não avalia se a hipótese é verdadeira.

**C03:** Existem registros de conta e de aplicação, mas a identidade do ator não está estabelecida. Nenhum campo na liberação fornecida identifica o humano que opera a sessão.

**C04:** A conclusão relatada do trabalho de cópia não pode ser convertida num resultado provado de restauração. Nenhuma restauração foi executada nesta peça.

**C05:** R8 omite detalhe de destino. Uma alegação de que nenhuma transferência ocorreu excederia a fonte.

**C06:** A alegação referencia R9, fora da liberação da Rodada A. O código de propósito não fornece conteúdo para R9; o registro futuro não deve influenciar a avaliação das 09:05.

**Teste negativo:** Remover R6 de um conjunto temporário faz o cartão de hipótese de treinamento carecer de uma das fontes referenciadas. O resultado muda para `NOT_IN_RELEASE` *para a variante temporária*. Nenhum evento histórico nem o registro canônico R6 mudou.

##### Validação, modos de falha e limites

As duas primeiras asserções detectam identificadores duplicados ou carimbos impressos fora de ordem nesta peça literal. Não verificam a sincronização de sistemas reais independentes. O algoritmo confere de propósito a *disponibilidade* da fonte e uma classe simplificada de alegação; não faz análise semântica de narrativas de incidente, verificações de integridade criptográfica, verificações de autorização nem verificação independente de fonte.

Quem obtém a saída esperada reproduziu a lógica declarada de sala, não provou que a Harbor Library viveu um incidente. Quem edita a entrada Python precisa preservar a transcrição original e rotular a execução alterada como variante.

**Artefato exigido:** Entregue (a) a transcrição exata, (b) um registro de alegações de seis linhas com identificador de evidência, formulação sustentada e limitação, e (c) um relatório de diferença de duas frases para o teste negativo. Aprovação só quando todos os fatos originais da Rodada A permanecem inalterados, achados sem suporte permanecem bloqueados e a remoção hipotética de fonte não é representada como perda real de evidência.

*Rubrica:* 3 = transcrição exata, seis linhas com limite, e o teste negativo sem representar perda real de R6;; 2 = a transcrição coincide, mas uma alegação sem suporte passa;; 1 = responde, mas omite fonte, limite ou trata conteúdo de registro como evento autenticado;; 0 = nenhum.

#### 1.10a A prontidão depende de evidência autorizada, não de um inventário verde

**Objetivo de aprendizagem:** Para o marco inicial R1–R8 da Harbor Library, distinguir uma capacidade operacional, um dono de decisão, uma rota autorizada de evidência e um ensaio demonstrado. Cada item tem uma fonte diferente e uma falha possível diferente. Quem responde em início de estudo deve conseguir identificar o próximo pedido seguro sem inventar uma coleta concluída.

Uma afirmação de que o provedor de identidade retém logs detalhados de sessão descreve uma **capacidade possível de fonte**. O pedido do líder do incidente para examinar um intervalo limitado descreve **intenção**. A permissão do dono adequado de identidade ou de dados é **autorização**. Um recibo de exportação ligado à fonte e uma verificação repetível seriam **evidência de recuperação executada**. Nenhum cria automaticamente o seguinte. Um console disponível não é permissão para inspecionar frequentadores sem relação, e um tíquete que pede uma exportação não é o objeto exportado.

Desenhe um caminho de dependência de quatro arestas: **pergunta de negócio → autoridade → produtor e seleção → resultado verificado**. Para cada aresta, identifique a decisão que falharia se a aresta estivesse ausente. Na Rodada A, a pergunta relevante é se as edições de reserva R3/R4 pertencem a uma tarefa permitida de treinamento; R6 torna o treinamento plausível, mas não prova aprovação nem identifica o humano. Um analista que não estabeleceu o relógio e a semântica de retenção de uma fonte não pode afirmar um prazo particular e seguro de coleta. Quem responde e não verificou a delegação de emergência não pode atribuir autoridade a qualquer colega que tenha credenciais de acesso.

**Exemplo resolvido contrastivo A:** Um ambiente permitido de treinamento expõe um fluxo consultável de auditoria de reservas, mas o custodiante alternativo não foi nomeado. A fonte tecnicamente disponível **não está operacionalmente pronta** para coleta autorizada fora do expediente. Acompanhamento correto: pedir ao líder do incidente que localize e verifique uma rota delegada válida; registrar perguntas sem resposta de aprovação e de acesso à fonte. Acompanhamento errado: executar a consulta com as credenciais de outra pessoa porque o incidente parece urgente.

**Exemplo resolvido contrastivo B:** O responsável e a rota de acesso à fonte estão aprovados, mas um teste inofensivo e agendado de reserva não produz um identificador estável de pedido. Aqui a permissão está presente, mas a **cobertura de correlação falha**. A próxima ação é um teste estreito de produtor e de campo, e uma pergunta de correção ao responsável pela aplicação. Seria incorreto descrever todos os eventos como coletados, ou identificar o operador de uma reserva usando só carimbos próximos. Nenhum dos exemplos é um fato novo de caso da série R.

O [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) trata preparação e resposta a incidentes como atividades ligadas de gestão de risco. O [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) distingue exercícios de discussão de testes medidos de componente. O classificador original de aprendizagem a seguir é apenas uma **peça de sala em memória**, não um verificador de fonte ou de aprovação.

##### Ensaio offline R1X — o primeiro elo de prontidão sem suporte

Rode em Python 3 isolado. As entradas são inventadas e reiniciadas entre linhas. Não há arquivos, chamadas de rede, credenciais nem mudanças reais de sistema.

~~~python
def ready(owner, alternate, source_route, receipt):
    if owner is None:
        return "HOLD_OWNER_UNNAMED"
    if alternate is None:
        return "ESCALATION_ROUTE_UNVERIFIED"
    if source_route is None:
        return "COLLECTION_ROUTE_UNVERIFIED"
    if receipt is None:
        return "REHEARSAL_NOT_EXECUTED"
    return "FIXTURE_DECLARED_REHEARSAL_ONLY"

cases = [
    ("C01_SCOPE", "service_owner", None, "source", None),
    ("OWNER_UNKNOWN", None, "approved_alternate", "source", None),
    ("NO_SOURCE", "service_owner", "approved_alternate", None, None),
    ("NO_TEST", "service_owner", "approved_alternate", "source", None),
    ("TOY_PASS", "service_owner", "approved_alternate", "source", "synthetic"),
]
for name, *fields in cases:
    print(name, ready(*fields))
~~~

**Saída Python reproduzida de forma independente e exata:**

~~~text
C01_SCOPE ESCALATION_ROUTE_UNVERIFIED
OWNER_UNKNOWN HOLD_OWNER_UNNAMED
NO_SOURCE COLLECTION_ROUTE_UNVERIFIED
NO_TEST REHEARSAL_NOT_EXECUTED
TOY_PASS FIXTURE_DECLARED_REHEARSAL_ONLY
~~~

**Teste adversarial:** Substitua a cadeia final de `TOY_PASS` por `None`; a saída torna-se `REHEARSAL_NOT_EXECUTED`. Por outro lado, o literal arbitrário `"synthetic"` alcança um rótulo favorável de peça sem um recibo real de custódia. Assim, o código ensina distinções de estado, mas não pode autenticar um produtor real nem uma aprovação.

**Prática e critério:** Entregue as cinco linhas de saída, um mapa de dependência e de dono, e uma passagem de duas frases que explique um substituto autorizado ausente. O crédito completo exige a fronteira de liberação R1–R8, um teste observável de treinamento e a diferença entre evidência proposta, aprovada e de fato coletada. R9 não pode ser usado na Rodada A só porque a hora do evento de fonte é anterior à revisão das 09:05.

*Rubrica:* 3 = cinco linhas exatas, mapa de dono, fronteira R1–R8, teste observável, e diferença entre proposto, aprovado e coletado;; 2 = as cinco linhas coincidem, mas a passagem trata credencial de acesso como autoridade;; 1 = responde, mas omite fonte, limite ou usa R9 na Rodada A;; 0 = nenhum.

**Síntese:** A prontidão exige uma resposta governada pelo responsável a uma pergunta limitada, não um rótulo verde de painel. O módulo 2 da edição inglesa, ausente deste arquivo, testará as decisões de fonte, de relógio e de coleta. Este adendo não cria nenhum registro novo de incidente da Harbor Library.

#### 1.11 Erros comuns e síntese do capítulo

- **Confundir suspeita com confirmação.** Use uma hipótese e declare o que a confirmaria ou a enfraqueceria.
- **Pular o responsável pelo serviço.** Uma ação tecnicamente plausível pode causar dano evitável aos usuários.
- **Perder a linha do tempo.** Registre carimbos da fonte, fuso e hora de coleta.
- **Ampliar o escopo em silêncio.** Pergunte antes de coletar ou mudar sistemas fora da autoridade.
- **Tratar um estado de cópia como um teste de restauração.** Uma execução bem-sucedida de cópia é um fato, não uma garantia de recuperação.
- **Tratar uma ausência em logs incompletos como evidência de ausência.** Declare o limite da coleta.

Prontidão é a capacidade de responder, sob pressão, quem é dono do serviço, quem pode aprovar uma decisão, onde evidência confiável pode ser encontrada, e como uma decisão será revista. Este capítulo prepara o trabalho de triagem de alertas e de preservação de evidência do módulo 2 da edição inglesa. Esse módulo **não está neste manuscrito**.

#### Marco resolvido

Às 09:05 o caso contém só R1–R8. Um cartão de decisão pode recomendar uma verificação restrita com o dono, a alternativa e o gatilho de revisão das 09:15; não deve relatar uma entrevista, uma exportação ou uma mudança de serviço como executada até existir um registro separado de execução.

#### Prática — Aula 05

##### EX004 — Fronteira de escopo

**Objetivo:** aplicar uma fronteira de autorização a uma próxima ação tentadora. **Entradas:** a declaração de escopo da seção 1.4 e R1–R8. **Saída:** uma decisão curta de escopo com ação proposta, objetos e operações permitidos, motivo da rejeição, alternativa contida, e condição de parada ou de escalada. Quem estuda quer buscar num site público real de biblioteca um nome de conta correspondente. Explique o que os oito registros fornecidos permitem em vez disso, e escreva um pedido hipotético do detalhe adicional se ele importasse ao caso. Uma nota 2 exclui explicitamente acesso a site real e nomeia o aprovador responsável de qualquer escopo ampliado futuro.

**Tarefa suplementar AR1 (depois do artefato exigido):**

**Verificação adicional:** Na decisão curta existente de escopo que rejeita uma busca em biblioteca do mundo real, declare o que quem estuda precisaria ver numa aprovação **autoritativa, atual e presa ao escopo** antes de qualquer coleta nova futura poder sequer ser proposta ao custodiante designado. Use AR1 para nomear uma falha de registro obsoleto ou de escopo excessivo de objetos como um **exemplo separado de prontidão**, não como fato do incidente.

**Critério de crédito completo:** Mantenha os objetos permitidos originais, o motivo de rejeitar acesso a site real, a alternativa contida e a condição de parada ou escalada. Uma delegação expirada ou um caminho de confirmação não verificado precisa bloquear a coleta adicional proposta. Nenhum resultado AR1 simulado e válido concede permissão sobre um site real.

**Resolução:** [EX004 no apêndice final](#ex004--worked-result).

*Rubrica:* 3 = nota 2 da fonte: exclui acesso a site real, nomeia o aprovador de escopo ampliado, e uma delegação expirada bloqueia coleta adicional;; 2 = a rejeição existe, mas o aprovador ou a condição de parada falta;; 1 = responde à pergunta, mas omite fonte, limite ou trata um site alcançável como autoridade;; 0 = nenhum.

##### EX007 — Registro mínimo de incidente

**Objetivo:** abrir um caso que outro analista possa continuar. **Entradas:** R1–R8 e o marco de abertura das 09:00. **Saída:** exatamente sete campos rotulados: identificador do caso e hora de abertura; serviço; relator e fonte; sinal observado com identificadores de registro; avaliação atual e incerteza; escopo e autoridade permitidos; próxima pergunta, dono e hora de revisão. Detalhes relacionados podem compartilhar um campo. Uma nota 2 retém o contexto `T-104` da central, da seção 1.5, distingue o relato de um estado de reserva conferido de forma independente, e não alega que a decisão posterior das 09:05 já estava executada às 09:00.

**Extensão de linha de base de comportamento:** Mantenha exatamente sete campos de abertura. No campo existente de incerteza, note que uma edição registrada e um relato de frequentador não estabelecem o estado atual correto de reserva aprovado pelo responsável. Não importe a peça BSL1 separada nem uma decisão posterior.

**Resolução:** [EX007 no apêndice final](#ex007--worked-result).

*Rubrica:* 3 = nota 2 da fonte: sete campos, contexto `T-104`, relato distinto de estado conferido, e decisão das 09:05 ainda não executada às 09:00;; 2 = os sete campos existem, mas o relato é tratado como estado verificado;; 1 = responde à pergunta, mas omite fonte, limite, autoridade ou hora;; 0 = nenhum.

##### EX009 — Alternativas de decisão

**Objetivo:** justificar uma decisão proporcional das 09:05 sob incerteza. **Entradas:** R1–R8 e o portão da seção 1.9. **Saída:** uma matriz de opções com duas linhas para (A) buscar uma restrição temporária de `desk-a` e (B) preservar R1–R8, perguntar ao responsável pelo treinamento e revisar antes da restrição. Registre, para cada uma, benefício esperado, custo possível de serviço ou de atraso, aprovador, sucesso ou falha observável e um gatilho de revisão às 09:15. Escolha uma de forma provisória e explique que evidência nova a reverteria. Uma nota 2 identifica uma aprovação separada para a restrição e não descreve qualquer dos riscos como evento já observado.

**Extensão:** Acrescente um falseador e uma verificação negativa de negócio às duas opções originais. Declare qual observação faria quem estuda reconsiderar uma decisão de esperar, e qual observação indicaria que uma restrição de conta interrompeu trabalho legítimo.

**Para crédito completo:** Uma resposta de 2 pontos exige estados distintos de aprovação, execução e verificação, não apenas uma opção preferida.

**Tarefa suplementar PATH1 (depois do artefato exigido):**

**Requisito adicional:** Mantenha ambas as opções originais das 09:05 e as aprovações delas. Acrescente um **contrafactual** claramente marcado: se um teste futuro autorizado encontrasse edições da equipe prejudicadas, mas a recepção manual de pedidos possível, identifique a única promessa ao usuário que permanece permitida e uma que é proibida. Não substitua a decisão original de evidência nem invente um item novo da série R.

**Tarefa suplementar AR1 (depois do artefato exigido):**

**Verificação adicional:** Mantenha a **matriz original de duas opções das 09:05**, a evidência só de R1–R8 e os gatilhos de revisão. Para a opção de restrição, acrescente uma **pergunta de preparação anterior ao incidente**: se o responsável pelo serviço ou o substituto permitido não pudesse ser verificado pelo registro atual, o analista ainda teria autoridade para impor a restrição? Explique a resposta segura sem importar as pessoas fictícias do AR1 nem o ensaio de setembro como resultado do caso.

**Critério de crédito completo:** Recomendação e aprovação permanecem separadas; nenhuma resposta ausente é tratada como permissão. A opção provisória escolhida continua justificada pela evidência disponível do caso, não por um responsável expirado fabricado às 09:05.

**Resolução:** [EX009 no apêndice final](#ex009--worked-result).

*Rubrica:* 3 = nota 2 da fonte: duas opções, aprovação separada da restrição, riscos não tratados como eventos observados, e silêncio distinto de permissão;; 2 = a matriz existe, mas recomendação e aprovação se confundem;; 1 = responde à pergunta, mas omite fonte, limite, autoridade ou o gatilho das 09:15;; 0 = nenhum.

##### EX012 — Registro de prática

**Objetivo:** tornar auditável uma decisão limitada. **Entradas:** R1–R8, o marco fictício das 09:05 e a matriz de autoridade da seção 1.3. **Saída:** um registro de decisão com hora, ação, motivo com identificadores de fonte, papel aprovador, papel executor, escopo da cópia de evidência, alternativa rejeitada, próxima hora de revisão e gatilho de reversão. O cenário concede permissão de sala para a cópia limitada; não descreva uma exportação de produção. Uma nota 2 declara a pergunta ao responsável pelo serviço como **pendente** até ser respondida e preserva a incerteza sobre o controle da conta.

**Extensão:** Registre um estado explícito para cada atividade: `proposed`, `approved classroom analysis`, `performed classroom copy` se de fato feita, ou `not performed`. Deixe a resposta proposta do responsável pelo treinamento pendente até ser fornecida.

**Para crédito completo:** Uma resposta de 2 pontos nunca relata um pedido hipotético como entrevista concluída nem como coleta de evidência de produção.

**Resolução:** [EX012 no apêndice final](#ex012--worked-result).

*Rubrica:* 3 = nota 2 da fonte: registro com papéis, escopo de cópia de sala, pergunta ao responsável pendente, e incerteza sobre o controle da conta;; 2 = o registro existe, mas um pedido hipotético aparece como entrevista ou coleta feita;; 1 = responde à pergunta, mas omite fonte, limite, autoridade ou descreve exportação de produção;; 0 = nenhum.

<!-- open-cyber-academy:lesson-navigation:start lesson-05 -->
#### Continue estudando — aula 05 de pelo menos 20

[← Aula 04](#lesson-04) · [Índice de aulas do curso](../SUBJECTS.md)

A aula 06 pertence ao capítulo 2 da edição inglesa e **ainda não está neste manuscrito**. Não há elo para ela aqui.
<!-- open-cyber-academy:lesson-navigation:end -->

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando

[← Visão do curso](../../README.md) · [Índice de aulas do curso](../SUBJECTS.md)

O capítulo 2 da edição inglesa ainda não está neste manuscrito. Os capítulos 2, 3 e 4 não foram traduzidos aqui. As resoluções do capítulo 1 seguem neste arquivo.
<!-- open-cyber-academy:chapter-navigation:end -->
<a id="answers"></a>

## Resoluções e rubrica de avaliação do capítulo 1

Estas resoluções ficam depois do material do capítulo, como apêndice de respostas deste arquivo. Uma resposta diferente é aceitável quando cita o registro fornecido, declara premissas e explica autoridade e dano potencial. Só estão aqui as resoluções do capítulo 1. As resoluções dos capítulos 2, 3 e 4 da edição inglesa não estão neste manuscrito.

<!-- open-cyber-academy:bsl1-worked:start -->
<a id="ir-rapid-ch01-bsl1-result"></a>

### Laboratório offline BSL1 do módulo 1 — resolução

~~~text
BASE CONFLICT S03/S04
BASE INVALID_INTERVAL S06
BASE_COUNT 2
BOUNDARY_S01_S02 NO_OVERLAP
CANCELLED_S05 NOT_OCCUPYING
VARIANT CONFLICT S01/S05
VARIANT CONFLICT S03/S04
VARIANT INVALID_INTERVAL S06
VARIANT_COUNT 3
INCOMPLETE INVALID_INTERVAL S06
INCOMPLETE_COUNT 1
~~~

#### Resultado resolvido, interpretação e limitações

**Linha de base:** Os intervalos confirmados da Room B, S03/S04, se sobrepõem, e o intervalo de S06 tem duração zero. Sob as regras de brinquedo, são dois achados. S01/S02 se encontram às 10:00 sem se sobrepor; S05 está cancelada e, portanto, não é contada como ocupação ativa.

**Sensibilidade ao estado:** Mudar S05 de cancelada para confirmada causa uma sobreposição nova na mesma sala com S01, preservando todas as outras entradas de linha de base. O total sobe para três achados. Isto é uma *premissa de entrada* alterada, não um incidente canônico recém-observado.

**Controle negativo de entrada incompleta:** Remover S04 da cópia de trabalho esconde o conflito S03/S04. O verificador relata só o intervalo inválido de S06. Uma contagem menor de problemas **não** prova que o comportamento de reserva melhorou; a população de entrada ficou incompleta.

**Limites técnicos:** Isto é uma comparação sequencial de seis linhas artificiais. Não implementa transações, concorrência, autenticação de fonte, regras de autorização, mudanças históricas, políticas de compartilhamento de sala, notificação de frequentadores nem impactos reais de reserva. O programa assume uma data fictícia e usa um analisador HH:MM simplificado. O usuário não deve executá-lo nem adaptá-lo contra qualquer serviço real de reserva sem a autoridade explícita da organização relevante.

**Artefato exigido:** Entregue a saída exata, uma tabela de classificação da linha de base e das duas variantes, as premissas aplicáveis de regra de negócio, e duas frases que expliquem por que nem os erros simulados nem o resultado de S04 ausente provam qualquer coisa sobre R1–R8 canônicos. Mantenha uma previsão registrada antes da execução; uma transcrição esperada copiada sem execução real deve ser rotulada como tal.
<!-- open-cyber-academy:bsl1-worked:end -->

<a id="ir-rapid-ch01-path1-result"></a>

### PATH1 — Resolução

#### Saída exata esperada — reproduzida com Python 3

~~~text
BASE: available=manual_intake,new_backup_job,room_view,site_reachable,staff_edit impaired= mode=STAFF_EDIT_PATH_MODELED
DATABASE_DOWN: available=manual_intake,site_reachable impaired=new_backup_job,room_view,staff_edit mode=NO_STAFF_EDIT_INTAKE_MODELED
IDENTITY_DOWN: available=manual_intake,new_backup_job,room_view,site_reachable impaired=staff_edit mode=NO_STAFF_EDIT_INTAKE_MODELED
HELPDESK_DOWN: available=new_backup_job,room_view,site_reachable,staff_edit impaired=manual_intake mode=STAFF_EDIT_PATH_MODELED
WEB_DOWN: available=manual_intake,new_backup_job impaired=room_view,site_reachable,staff_edit mode=NO_STAFF_EDIT_INTAKE_MODELED
DATABASE_AND_HELPDESK_DOWN: available=site_reachable impaired=manual_intake,new_backup_job,room_view,staff_edit mode=NO_EDIT_OR_INTAKE_PATH
~~~

#### Interpretação, variante negativa e limitações

Com todo componente assumido disponível, o modelo prevê os cinco caminhos estruturalmente possíveis. O rótulo `STAFF_EDIT_PATH_MODELED` **não** é uma escrita bem-sucedida ou autorizada de reserva.

Quando a base está indisponível, a página informativa e a recepção manual permanecem estruturalmente possíveis; a visão de salas, a edição pela equipe e a criação de cópia nova estão prejudicadas no modelo de brinquedo. A recepção manual é só recibo de pedido, não serviço confirmado de reserva.

Quando a identidade está indisponível, só o caminho de edição pela equipe está prejudicado sob os requisitos declarados. Quando a central está indisponível, o caminho alternativo de recepção desaparece, mas as rotas relacionadas ao site permanecem. Quando o componente web está indisponível, a recepção de pedidos e o trabalho de cópia permanecem, mas as funções relacionadas à aplicação estão prejudicadas. Quando base e central estão indisponíveis, uma página informativa sozinha não pode satisfazer o requisito modelado de edição nem o de recepção.

**Variante negativa de sensibilidade:** Remova temporariamente a dependência `helpdesk` de `manual_intake` num modelo copiado. A entrada implicaria então, de forma incorreta, que a recepção de pedidos não exige nenhum componente. Explique como uma dependência omitida pode fazer um modelo parecer mais resiliente do que a implementação real. Restaure o dicionário original depois do experimento.

**Limites:** O script calcula só previsões estruturais baseadas em conjuntos. Não simula interrupções parciais, alternativas, cache, durabilidade de transação, correção de autenticação, aprovação do responsável pelo serviço, processamento real de pedidos nem verificação de estado de negócio. O usuário não deve interpretar qualquer linha impressa como um evento real da Harbor Library.

**Entrega:** Forneça seis linhas de resultado do modelo, dois impactos contrastados de função, a interpretação da variante negativa e um teste autorizado específico que discriminaria uma previsão modelada da correção observada do serviço. Uma resposta que alega que `manual_intake` prova uma reserva concluída falha o objetivo de aprendizagem.

<a id="ex001--worked-result"></a>

### EX001 — Resolução

| Afirmação | Classificação | Registro fornecido de suporte | Limite — uma frase |
|---|---|---|---|
| (a) “R4 registra um cancelamento de B18” | Observação direta **do conteúdo do registro** | R4, 08:44 UTC, log da aplicação | A linha relata cancelamento, mas não demonstra por que foi autorizado nem se uma visão posterior do frequentador estava correta. |
| (b) “`desk-a` foi comprometida” | Hipótese que exige confirmação; **sem suporte se afirmada como achado confirmado** | R1 relata uma entrada de conta, e R3–R4 relatam edições de reserva | Esses registros não estabelecem controle não autorizado, um ator humano, intenção nem uma investigação de comprometimento concluída. |
| (c) “R5 relata que B18 desapareceu” | Observação direta **de um relato de frequentador** | R5, 08:48 UTC, central de atendimento | O relato é evidência do que foi relatado, não uma comparação independente e autoritativa do estado da reserva. |
| (d) “R7 prova que o serviço pode ser restaurado em dez minutos” | Conclusão sem suporte | R7, 08:52 UTC, monitor de cópia de segurança | Um trabalho de cópia concluído não é uma restauração isolada, uma medição de recuperação decorrida nem correção aceita do serviço. |

Uma resposta forte distingue a *formulação observável* de (b) do estatuto epistêmico: o comprometimento alegado não tem suporte **como fato**, enquanto o uso não autorizado permanece uma hipótese viva. Reclassificá-lo como “confirmado” porque uma conta e edições aparecem perto uma da outra falha o exercício.

**Raciocínio adicional:** Uma resposta correta pode relatar que R4 contém um cancelamento de B18 e R5 contém um relato de frequentador. Nenhuma das fontes estabelece de forma independente o motivo do cancelamento nem o estado completo atual da exibição. “`desk-a` foi comprometida” não tem suporte como achado; “uso não autorizado é uma hipótese a investigar” é defensável. R7 relata a conclusão de um trabalho de cópia da noite anterior, não uma recuperação de dez minutos. A evidência de elevação que falta é uma comparação autorizada de contexto de conta para a pergunta do ator, e uma restauração isolada e cronometrada, com verificação correta do estado da reserva, para a alegação de recuperação. A evidência de acompanhamento ainda não existe dentro de R1–R8.

<a id="ex002--worked-result"></a>

### EX002 — Resolução

| Pergunta discriminante | Por que agora | Custodiante e permissão | Efeito na decisão |
|---|---|---|---|
| A mudança de B17 e o cancelamento de B18 foram especificamente tarefas aprovadas de treinamento? | R3–R4, 08:43–08:44, mostram edições; R6, 08:50, mostra só um intervalo de treinamento agendado. | O responsável pelo serviço ou pelo treinamento confere a lista datada e aprovada de tarefas; o líder do incidente registra o pedido. | Uma lista aprovada que nomeia ambas as edições enfraquece uma explicação de *edição* não autorizada para esses registros; uma lista completa confirmada que exclui B18 fortalece a preocupação. |
| `desk-a` foi usada pelo membro esperado da equipe, e uma edição ainda está ocorrendo? | R1, 08:40, nomeia uma conta, mas nenhum humano; a tabela fornecida para antes do marco das 09:05. | O líder do incidente busca uma verificação estreita de identidade ou de aplicação junto ao administrador autorizado; quem estuda não consulta um serviço real. | Uma sessão autorizada conferida de forma independente poderia reduzir a preocupação; uma edição nova, inexplicada e verificada elevaria a urgência e provocaria uma decisão nova. |

Nenhuma das respostas está em R1–R8. O líder registra um **pedido**, o dono e a hora da decisão. A lembrança de uma entrevista, sozinha, pode ser contexto útil, mas não é prova de identidade.

**Raciocínio de linha de base de comportamento:** R6 mostra um período de treinamento agendado, não uma lista completa e aprovada de tarefas para B17/B18. Pergunte ao responsável pelo treinamento se uma lista datada e aprovada incluía ambas as mudanças. Uma lista completa confirmada que exclui B18 enfraquece a explicação de treinamento para essa edição; uma lista aprovada que a inclui fortalece essa explicação sem identificar a pessoa que controla a conta. Uma verificação estreita e autorizada de identidade ou de aplicação pode discriminar atividade da conta, mas não pode, por si, estabelecer que o estado atual da reserva atende a uma regra de negócio aprovada pelo responsável. A peça da série S do BSL1 não fornece evidência sobre estes registros da série B.

<a id="ex003--worked-result"></a>

### EX003 — Resolução

| Dependência | Dano possível visível ao usuário | Ponteiro fornecido da Rodada A | Discriminador ausente e um resultado negativo que enfraqueceria a preocupação | Custodiante permitido / autoridade que pede |
|---|---|---|---|---|
| Serviço de identidade da equipe | Uso inesperado de uma conta da equipe poderia permitir mudanças inadequadas de reserva; o uso indevido contínuo não está verificado. | Entrada de conta em R1 e acesso ao painel em R2; R3–R4 são edições registradas, não prova de atribuição humana. | Uma verificação limitada e aprovada de contexto de identidade ou de sessão poderia mostrar circunstâncias esperadas da conta; isso enfraqueceria uma hipótese de acesso inesperado **sem identificar o operador humano nem validar a autorização de cada edição**. | O administrador de identidade fornece só o detalhe permitido depois da aprovação do líder do incidente; o analista pede, não coleta de forma unilateral. |
| Base de reservas e estado atual da reserva | Frequentadores poderiam ver disponibilidade incorreta de sala ou uma atribuição inadequada. | R3–R4 relatam edições e R5 relata uma preocupação de frequentador; nenhuma comparação de estado presente é fornecida. | Uma comparação aprovada pelo responsável que faça coincidir os valores autoritativos atuais de B17/B18 e a exibição ao frequentador com o alvo aprovado enfraqueceria uma **hipótese selecionada de discrepância de estado**, sem provar que todas as salas ou usuários estão não afetados. | O responsável pelo serviço aprova o alvo e a comparação; o custodiante da aplicação ou dos dados fornece uma visão limitada e autorizada. |

Ambos os efeitos são **possíveis**. O relato R5 sustenta investigar um problema visível, mas o exercício não mediu todos os usuários nem confirmou o estado atual da base. Outros pares válidos, como aplicação de reservas e central de atendimento, ainda precisam nomear uma verificação que distinga explicações.

**Raciocínio adicional:** Para a dependência de identidade, R1 identifica uma entrada relatada e R2 identifica acesso relatado ao painel. O dano hipotético é uso adicional incorreto de função autorizada da equipe, não um ataque contínuo medido. Uma verificação autorizada de sessão de identidade poderia enfraquecer uma premissa de contexto inesperado de sessão, mas não deve identificar um humano sem evidência independente adequada. Para a dependência da base, R3–R4 relatam mudanças e R5 um sintoma de frequentador. Uma comparação aprovada pelo responsável entre valores autoritativos de B17/B18 e uma agenda esperada poderia mostrar que o estado atual coincide ou difere do alvo do responsável. Essa comparação é **pedida**, não executada. Os dois caminhos têm donos diferentes e não resolvem um ao outro.

**Extensão resolvida PATH1:**

A fonte de identidade da equipe e a base de reservas são dependências diferentes, com perguntas diferentes de evidência. R1/R2 relatam uma entrada e uso do painel sem atribuição humana; R3/R4 relatam edições e R5 relata um sintoma de frequentador sem estabelecer o estado atual correto. No modelo PATH1 separado, `staff_edit` exige `web`, `identity` e `database`. Uma falha modelada de identidade prevê prejuízo deste caminho, mas não é uma interrupção observada da Rodada A. Um teste isolado futuro adequado conferiria tanto uma operação aprovada de edição pela equipe quanto o resultado autoritativo observado de forma independente. O responsável pelo serviço definiria a aceitação de negócio; os custodiantes de identidade e da aplicação forneceriam evidência técnica permitida. O modelo não pode substituir nenhum dos dois.

<a id="ex004--worked-result"></a>

### EX004 — Resolução

**Ação proposta:** buscar num site público real de biblioteca uma conta `desk-a` correspondente. **Fronteira:** este capítulo autoriza ler, ordenar e anotar R1–R8 sintéticos durante a sessão; não autoriza acesso a uma biblioteca real, a uma conta real ou a dados de terceiros. **Decisão:** rejeitar a busca proposta porque ampliaria tanto o objeto quanto a organização sob investigação. **Alternativa contida:** usar R1 e R2 para afirmar que a conta entrou e abriu o painel, marcando o operador humano como desconhecido. Rascunhar um pedido fictício ao líder do incidente para que o administrador de identidade forneça os campos mínimos relevantes de sessão e o intervalo *se* uma organização real aprovasse tal coleta. **Condição de parada:** se a resposta exige um campo ausente de R1–R8, pare na fronteira de evidência e registre a pergunta sem resolução. Uma página pública estar alcançável não confere autoridade de resposta a incidentes sobre ela.

**Extensão resolvida AR1:**

A busca proposta de conta num site real está fora da autorização de sala; só R1–R8 fornecidos podem ser analisados. Uma coleta organizacional real adicional exigiria uma pergunta documentada de negócio, objetos e fonte permitidos, papel aprovador atual, custodiante, nomeação ou delegação verificada, e uma decisão confirmada e presa ao escopo por um processo autorizado. Um registro antigo copiado ou um e-mail de uma pessoa não verificada não concede autoridade. Na peça AR1 separada, um pedido que inclui um objeto sem relação devolve `HOLD_SCOPE_EXCEEDED`, e uma edição obsoleta devolve `HOLD_STALE_REGISTER`. Nenhum dos resultados diz que essas condições ocorreram no caso das 09:05 da Harbor Library. A alternativa segura continua a ser documentar o detalhe ausente e pedir uma decisão limitada ao líder adequado do incidente e ao custodiante, sem acessar qualquer site real.

<a id="ex005--worked-result"></a>

### EX005 — Resolução

| Registro | Fonte | Hora UTC | Evento observado |
|---|---|---|---|
| R1 | Log de identidade | 08:40 | A entrada de `desk-a` teve sucesso. |
| R3 | Log da aplicação | 08:43 | B17 mudou da Room 2 para a Room 4. |
| R4 | Log da aplicação | 08:44 | B18 foi cancelada. |
| R5 | Central de atendimento | 08:48 | Um frequentador relatou que B18 havia desaparecido. |

**Fato de ordenação:** a entrada registrada precede as duas edições registradas, e o relato da central as segue. **Limite causal:** a ordem temporal não prova que a entrada não era autorizada, que uma pessoa nomeada fez as edições, nem que R4 explica toda parte da experiência do frequentador. A hora de abertura do caso, 09:00, pertence ao registro do incidente, não aos quatro eventos de fonte. Um revisor deve preservar os relógios da fonte e a informação de conversão para UTC se os sistemas subjacentes se tornarem disponíveis mais tarde.

**Raciocínio adicional:** As quatro linhas de evento são R1 08:40, R3 08:43, R4 08:44 e R5 08:48 UTC. A abertura do caso às 09:00 e a decisão às 09:05 são carimbos do fluxo do caso, não eventos adicionais de log. A sequência sustenta só uma afirmação de ordenação. Não prova que uma pessoa particular controlava `desk-a`, que as edições não eram autorizadas, nem que a mudança de R4 explica todo aspecto de R5. A passagem correta nomeia a fonte de cada carimbo e retém a falta de validação de relógio entre fontes numa investigação real futura.

<a id="ex006--worked-result"></a>

### EX006 — Resolução

| Tarefa | Papel responsável e autorização | Verificação |
|---|---|---|
| Possível interrupção de reservas | O analista e o líder podem recomendar; o **responsável pelo serviço** decide se a interrupção é tolerável sob a regra fictícia de emergência; o operador da aplicação executaria só depois da aprovação. | O responsável pelo serviço confere se as escritas de reserva de fato pararam e se o trabalho essencial tem alternativa. Nenhuma interrupção está aprovada em R1–R8. |
| Preservar R1–R5 para o caso de sala | O líder do incidente aprova a cópia limitada; o analista a prepara a partir da tabela sintética fornecida. | O líder do incidente confere identificadores, horários UTC, escopo e nota de armazenamento. Isto não é uma exportação de log de produção. |
| Coordenar a revisão | O líder do incidente nomeia 09:15 UTC ou um gatilho verificado mais cedo, e registra quem precisa comparecer. | O registro de decisão contém a hora, o dono e as perguntas sem resolução. |
| Testar uma restauração de cópia | O responsável pela recuperação desenha e, quando autorizado, executa uma restauração contida usando uma cópia; o responsável pelo serviço declara a agenda esperada. | Compare identificadores e valores restaurados de reserva com um alvo autoritativo e meça o tempo. R7 sozinho é um estado de trabalho de cópia, **não** esta verificação. |

A tabela atribui responsabilidades dentro do exercício fictício. Uma equipe pequena pode combinar papéis humanos e reter campos separados de aprovação e de resultado.

**Extensão resolvida PATH1:**

A tabela original de responsabilidade permanece válida: o analista e o líder do incidente coordenam a pergunta, o responsável pelo serviço controla a interrupção de negócio aceitável, os operadores adequados executam ações autorizadas à parte, e os responsáveis pela recuperação desenham verificação contida. Um modo degradado hipotético só de pedidos precisaria de aprovação do responsável pelo serviço, de um dono da central para recibos pendentes e de uma reconciliação autorizada posterior. A equipe poderia relatar que um pedido foi recebido para processamento, não que uma reserva foi confirmada. PATH1 fornece só um modelo de possibilidade de recepção; R1–R8 não fornece aprovação nem fila pendente real. O formato de quatro linhas permanece inalterado.

**Extensão resolvida AR1:**

A tabela existente de quatro linhas ainda atribui a tolerância à interrupção ao responsável pelo serviço, a aprovação da coleta ao líder do incidente, a execução limitada ao custodiante ou operador adequado, e a verificação a um revisor. Um registro de autoridade poderia, **antes de um incidente**, demonstrar como a nomeação do responsável e do substituto seria conferida e como o escopo ou a expiração de um papel seria verificado. Um substituto temporário cujo mandato expirou não pode aprovar uma pausa de escrita só porque a pessoa já esteve listada. O pedido precisa ser retido e escalado por uma rota aprovada. Um teste AR1 de sala concluído não significa que a cópia sintética de R1–R5 foi coletada nem que uma restrição ao vivo aconteceu. Qualquer execução real posterior precisaria de um recibo autorizado à parte e de uma verificação de resultado.

<a id="ex007--worked-result"></a>

### EX007 — Resolução

| Sete campos de abertura | Entrada modelo às 09:00 UTC |
|---|---|
| 1. Identificador do caso e hora de abertura | `HL-IR-001`; 2026-10-11 09:00 UTC. |
| 2. Serviço | Reserva de salas da Harbor Library; responsável pelo serviço a confirmar. |
| 3. Relator e fonte | Tíquete `T-104` da central; R5 é um **relato** de frequentador às 08:48 UTC. |
| 4. Sinal observado e ponteiros | Entrada R1 às 08:40, edição B17 em R3 às 08:43, cancelamento B18 em R4 às 08:44, relato R5 às 08:48. |
| 5. Avaliação e incerteza | Atividade suspeita de reserva; comprometimento da conta, estado de aprovação das edições e impacto completo sobre o usuário **não confirmados**. R6 nota treinamento, mas não resolve essas perguntas. |
| 6. Escopo e autoridade | Escopo atual de sala: inspecionar só R1–R8 sintéticos; nenhuma coleta de sistema real nem mudança de serviço aprovada. |
| 7. Próxima pergunta, dono e revisão | O líder do incidente pergunta ao responsável pelo serviço ou pelo treinamento se B17/B18 estavam planejadas; revisar a próxima ação proposta às 09:05 UTC. |

Isto é um registro de **abertura**. Uma decisão posterior das 09:05 pode ser anexada com a própria aprovação e hora de revisão. Retrodatar essa decisão na entrada das 09:00 distorceria a cronologia do caso.

**Raciocínio de linha de base de comportamento:** O registro de abertura de sete campos às 09:00 pode acrescentar “estado atual correto de reserva, aprovado pelo responsável, desconhecido” dentro do quinto campo. Os registros da aplicação e o relato do frequentador não provam violação de invariante. Nenhum resultado BSL1 nem decisão posterior pertence a este instantâneo de abertura.

<a id="ex008--worked-result"></a>

### EX008 — Resolução

| Registro e hora | Conclusão sustentada | Conclusão sem suporte | Acompanhamento dentro do modelo do exercício |
|---|---|---|---|
| R6, 08:50 UTC | O treinamento da recepção estava marcado para 08:30–09:00. | B17 e B18 eram necessariamente edições aprovadas de treinamento. | Pedir ao responsável pelo treinamento a lista datada de tarefas e os alvos aprovados. |
| R7, 08:52 UTC | O trabalho de cópia da noite anterior foi relatado como concluído. | O serviço de reserva pode ser restaurado corretamente dentro de um tempo dado. | O responsável pela recuperação planeja uma restauração contida e uma comparação de valores. |
| R8, 08:55 UTC | O resumo de rede fornecido não tem detalhe relevante de destino. | Nenhuma transferência de dados ocorreu. | Registrar os campos ausentes; qualquer consulta adicional precisa de propósito, fonte, intervalo e aprovação definidos. |

Cada linha preserva uma observação útil sem elevá-la a uma conclusão que a fonte não pode sustentar. Um campo ausente é um limite da alegação, não um achado negativo.

**Extensão resolvida PATH1:**

R6 documenta treinamento agendado, não permissão para edições especificadas de reserva. R8 carece de detalhes de destino e não pode estabelecer ausência de transferência. R7 registra um trabalho de cópia concluído, mas não uma cópia recuperável nomeada, tempo de restauração, valores aceitos de reserva nem serviço restaurado em funcionamento. O caminho hipotético `new_backup_job` do PATH1 é outra premissa estrutural, não evidência de recuperação. Um teste contido futuro identificaria a cópia, a hora da fonte, o ambiente isolado de teste, os valores esperados de reserva, o resultado medido e o responsável pelo serviço. Até tal resultado ser fornecido, a correção da recuperação permanece não verificada.

<a id="ex009--worked-result"></a>

### EX009 — Resolução

| Opção | Benefício esperado | Custo possível | Aprovação e execução | Revisão observável |
|---|---|---|---|---|
| A: buscar restrição temporária de `desk-a` | Pode interromper edições adicionais por essa conta, se ela estiver sendo usada de forma indevida. | Poderia interromper trabalho legítimo da recepção; outro caminho ainda pode existir. | O analista recomenda; o líder do incidente e o responsável pelo serviço aprovam escopo e impacto no serviço; o administrador de identidade executa. | Conferir se o acesso mudou e se o trabalho essencial de reserva continua; encerrar ou revisar a restrição na revisão registrada. |
| B: preservar R1–R8, verificar B17/B18 com o responsável pelo treinamento e então decidir | Retém a sequência observada e pode evitar interrupção desnecessária de serviço. | Um editor não autorizado poderia fazer outra mudança enquanto a equipe confere. | O líder do incidente aprova a análise limitada de sala; o responsável pelo serviço é dono da entrada sobre impacto no serviço. | Até 09:15 UTC, ou antes diante de uma edição nova inexplicada e verificada, comparar a resposta do responsável e qualquer fonte nova autorizada. |

**Escolha provisória:** B sob o instantâneo R1–R8 fornecido, porque a explicação de treinamento é testável e nenhuma mudança contínua foi fornecida ainda. Esta não é uma resposta universal. Uma edição fresca, inexplicada e verificada, ou um dano alto e confirmado ao serviço, poderia deslocar a recomendação para A, mas ainda exigiria uma aprovação explícita. R1–R8 não provam que esperar é inofensivo nem que a restrição imediata é necessária.

**Raciocínio adicional:** A opção provisória de preservar R1–R8 e perguntar ao responsável pelo treinamento sobre B17/B18 é defensável porque a lista aprovada de tarefas é um discriminador direto e nenhuma edição posterior é fornecida neste marco. O custo é uma possível edição adicional não autorizada, se houver uso indevido. Uma mudança nova, inexplicada e verificada provocaria reconsideração imediata; não é observada agora. O pedido alternativo de restringir `desk-a` poderia reduzir o uso indevido por essa conta, mas o dono da resposta precisaria de autoridade explícita e de um plano para testar tanto a rota suspeita quanto o trabalho legítimo da recepção. Mesmo depois da aprovação, uma proposta não está executada até um operador a realizar e um observador adequado verificar o resultado.

**Extensão resolvida PATH1:**

Às 09:05, preservar R1–R8 e buscar confirmação da autorização de treinamento de B17/B18 permanece uma opção provisória defensável; uma proposta de restrição permanece sujeita à parte a autoridade e a impacto operacional. Um modelo contrafactual **diferente** de falha de serviço pode sugerir que uma central poderia receber pedidos pendentes enquanto edições aceitas da equipe estão indisponíveis. Se uma organização real validasse e aprovasse à parte tal modo, a equipe poderia prometer só **recebimento para revisão posterior**, não uma reserva concluída. Uma alternativa modelada não prova que o serviço real está disponível nem que R1–R8 contém qualquer interrupção. O líder do incidente não deve preencher essa falha de volta no caso original nem mudar em silêncio o raciocínio das 09:05.

**Extensão resolvida AR1:**

A escolha original das 09:05 usa R1–R8 e pode favorecer de forma provisória preservar os registros fornecidos e testar a explicação de treinamento agendado, sujeita à hora de revisão e ao risco de mudança adicional. Buscar uma restrição temporária é uma proposta, não uma ordem; a aprovação do líder do incidente e do responsável pelo serviço, o escopo-alvo, o custo para o serviço legítimo e o plano de verificação permanecem necessários sob as regras do caso. Um **ensaio de autoridade anterior ao incidente**, como AR1, poderia ajudar a organização a identificar uma rota alternativa válida antes de uma interrupção futura. Se nenhuma rota atual e autorizada do responsável pelo serviço puder ser estabelecida, o analista não deve inventar aprovação nem tratar o silêncio como consentimento; em vez disso, registra a retenção, documenta o risco e busca a escalada designada de governança ou de liderança do incidente. O próprio cenário AR1 não é um evento novo da Rodada A nem prova de que o responsável da Harbor Library estava ausente.

<a id="ex010--worked-result"></a>

### EX010 — Resolução

“Às 09:00 UTC, os registros de aplicação R3–R4 mostram duas mudanças de reserva depois da entrada R1 de `desk-a`, e o registro R5 da central relata uma preocupação de frequentador; a causa e o impacto completo no serviço permanecem não confirmados. O líder do incidente **propõe** preservar os registros fornecidos e perguntar ao responsável pelo serviço se as edições coincidem com o treinamento agendado, com uma decisão de aprovação às 09:05 UTC.”

A primeira frase identifica a fonte e a incerteza. A segunda descreve uma proposta, não uma ação já autorizada ou concluída. O público é o responsável interno pelo serviço; uma notificação pública exigiria uma decisão separada e aprovada de comunicação.

**Rascunho interno alternativo de duas frases:** “Às 09:00 UTC, R3–R4 relatam mudanças em B17/B18 depois da entrada R1 de desk-a, enquanto R5 registra uma preocupação sobre B18; a causa, o comportamento aprovado e a correção atual da reserva permanecem não verificados. O líder do incidente propõe perguntar ao responsável pelo serviço e pelo treinamento se essas edições coincidem com tarefas aprovadas e qual resultado correto de reserva deve ser conferido antes da decisão das 09:05.” Isto é uma verificação proposta, não uma entrevista executada nem uma comparação de estado.

<a id="ex011--worked-result"></a>

### EX011 — Resolução

| Gatilho hipotético, **não presente em R1–R8** | Como seria verificado e por que importa | Dono e próxima decisão |
|---|---|---|
| Uma linha posterior de auditoria de reserva mostra uma edição nova fora de uma lista confirmada e aprovada de tarefas. | O custodiante da aplicação confere a fonte da linha, a hora do evento, o identificador da reserva e a comparação com a lista de tarefas; mudança contínua eleva o custo de esperar. | O líder do incidente reconvoca prontamente os responsáveis pelo serviço e pela identidade para considerar uma restrição temporária limitada. |
| Uma comparação do responsável pelo serviço encontra várias atribuições atuais de reserva diferentes de uma agenda aprovada. | O responsável pelo serviço e o analista comparam só os identificadores e valores necessários de reserva; um efeito mais amplo visível ao usuário eleva o dano potencial. | O responsável pelo serviço e o líder do incidente reavaliam a continuidade do serviço e a comunicação, registrando aprovação antes de qualquer interrupção. |

O exercício pede **gatilhos**, não fatos inventados do caso. Um sinal novo precisa ser coletado ou relatado dentro da autoridade e conferido antes de poder sustentar uma afirmação de urgência maior.

**Raciocínio de linha de base de comportamento:** Uma comparação futura autorizada e hipotética de duas reservas confirmadas de ocupação única contra a política aplicável aprovada pelo responsável, ou de uma reserva selecionada contra um alvo do responsável pelo serviço, poderia aumentar a urgência de dano de negócio se encontrasse um descompasso verificado. O custodiante da aplicação ou dos dados precisa estabelecer a fonte e o escopo da comparação, e o responsável pelo serviço precisa confirmar a versão da regra. À parte, uma edição nova, inexplicada e verificada, fora de uma lista completa, confirmada e aprovada de tarefas, reabriria a pergunta de atividade contínua. Nenhuma das observações está em R1–R8, e um descompasso de negócio, sozinho, não estabeleceria uma causa maliciosa.

<a id="ex012--worked-result"></a>

### EX012 — Resolução

| Campo do registro de decisão | Entrada modelo |
|---|---|
| Hora e ação | **09:05 UTC:** o líder fictício do incidente aprova uma cópia **só de sala** e limitada de R1–R5 sintéticos. **Execução real da cópia local: não evidenciada na resposta modelo.** Uma pergunta ao responsável pelo treinamento ou pelo serviço sobre a autorização de B17/B18 está **proposta; resposta pendente**. |
| Motivo e ponteiros | A entrada R1, a mudança B17 em R3, o cancelamento B18 em R4 e o relato de frequentador R5 estabelecem uma sequência; R6 torna o treinamento plausível, mas não aprova as edições. |
| Aprovador e executor | **Aprovador:** líder fictício do incidente, só para o escopo de sala declarado. **Executor prospectivo:** analista que estuda; marque `not performed` até quem estuda de fato criar uma cópia local e registrar a hora verdadeira de criação, o artefato e o escopo. O responsável pelo treinamento **ainda não** respondeu à pergunta. |
| Fronteira e opção rejeitada | O escopo autorizado de cópia de sala limita-se a R1–R5; o modelo não estabelece que a cópia ocorreu. R6–R8 permanecem disponíveis para interpretação. Não colete um log real nem restrinja uma conta real. A restrição imediata de `desk-a` é adiada porque o custo para o serviço e a aprovação não foram resolvidos. |
| Revisão e reversão | Reavaliar às 09:15 UTC ou antes, diante de uma edição nova e inexplicada de reserva que seja verificada; consultar o líder e o responsável pelo serviço antes de mudar o acesso. |

Esta entrada não alega que o responsável pelo serviço respondeu, que ocorreu uma exportação de produção, ou que `desk-a` está comprometida. Os titulares exatos dos papéis podem ser fictícios, mas a propriedade da decisão e o estado precisam permanecer explícitos.

**Raciocínio adicional:** Às 09:05 o líder do incidente pode autorizar uma cópia *de sala* do subconjunto sintético R1–R5 e uma pergunta proposta ao responsável pelo treinamento. Se quem estuda não fez de fato uma cópia local, o estado é “exercício aprovado; cópia não executada”, não “coletado”. Se executada, quem estuda registra a hora real de criação e o arquivo ou a planilha reais, sem inventar uma exportação de produção. A resposta do responsável pelo treinamento permanece pendente. O registro deve preservar o motivo de adiar qualquer restrição de conta, o responsável pelo serviço a consultar e a condição de revisão das 09:15.

<a id="ex013--worked-result"></a>

### EX013 — Resolução

| Lacuna de prontidão | Consequência neste caso | Dono da melhoria |
|---|---|---|
| O responsável pelo serviço e o substituto não estão confirmados no registro de abertura. | Uma interrupção de reservas ou uma restrição de conta poderia esperar por um aprovador indisponível. | Líder do incidente e gestor do serviço. |
| A sincronização de relógio entre fontes não está documentada. | A ordenação de R1–R8 poderia enganar se os relógios das fontes diferirem; o exercício assume os valores UTC fornecidos. | Custodiantes de identidade e da aplicação. |
| Nenhum resultado registrado de teste de restauração acompanha R7. | Um trabalho de cópia concluído pode não produzir uma agenda correta dentro de um tempo aceitável. | Responsável pela recuperação e responsável pelo serviço. |

**Tíquete de prioridade e ensaio de verificação — modelo resolvido:**

| Campo do tíquete | Entrada do modelo de treinamento |
|---|---|
| Lacuna | Os materiais de abertura do caso não confirmam a rota atual de autoridade do responsável pelo serviço ou do substituto para uma decisão disruptiva de reserva. |
| Justificativa de prioridade | Um aprovador não verificado ou um substituto expirado poderia atrasar uma decisão necessária ou induzir uma interrupção não autorizada; isto é uma **fraqueza de preparação**, não uma falha observada de incidente. |
| Dono responsável | O líder fictício do incidente coordena; o administrador designado do registro e o gestor do serviço são donos do registro governado de nomeação. |
| Mudança específica | Publicar e revisar um registro **governado e versionado** de papel e substituto, com escopo de operação e de objeto, emissor da delegação, validade, revogação, custodiante e rota aprovada de confirmação. |
| Prazo proposto de treinamento | **2026-10-25 UTC**, sujeito à aceitação explícita do gestor do serviço; o prazo de uma organização real precisa vir do próprio plano, não do NIST nem desta ficção. |
| Ensaio positivo | Uma rota atual, primária ou delegada, com escopo correto, produz só um resultado fictício de **caminho válido, não executado**. O revisor independente consegue reconstruir a decisão a partir do registro e do pedido congelados. |
| Ensaio negativo | Delegado expirado ou revogado, aprovador errado, recibo ausente ou escopo de objeto ampliado produz **retenção**, com um caminho nomeado e aprovado de escalada; nenhuma mudança de fonte nem controle de produção é executado. |
| Evidência de aceitação retida | Edição e emissor do registro, pedido congelado e resposta do revisor, transcrição de entrada e resultado, data da revisão, revisor nomeado e qualquer limitação observada. |
| Condição de falha e de reabertura | Se uma rota inválida passa, se uma rota válida não pode ser reconstruída, ou se a edição governante testada muda, deixe ou reabra o tíquete para correção do administrador e um reteste versionado à parte. |

**Aceitação:** Um documento de registro revisto, **sozinho**, não encerra o tíquete; o ensaio positivo e o negativo independentes precisam ser reproduzíveis, e o dono responsável precisa aceitar o resultado observado. A data proposta de vencimento é explicitamente um alvo sintético de tíquete, não um fato de R1–R8. Quem estuda pode escolher uma lacuna justificada diferente do registro original de três linhas, mas precisa fornecer a mesma lógica de mudança responsável, mensurável e testável.

**Extensão resolvida AR1:**

Um tíquete de prontidão de alto valor trata da certeza ausente sobre as nomeações do responsável pelo serviço e do substituto. O líder do incidente e o administrador designado do registro criam ou revisam um **registro de autoridade versionado e ligado à fonte**, mostrando papel primário, substituto restrito, escopo de operação e de objeto, intervalo de vigência, estado de revogação, custodiante nomeado e rota aprovada de confirmação. O ensaio executa pelo menos um caminho positivo válido e um caminho negativo expirado ou não autorizado, usando identidades inventadas. Passa quando o revisor independente reconstrói o roteamento esperado a partir do pacote congelado, o teste válido permanece explicitamente **não executado**, e os testes inválidos devolvem retenções ou um estado de reter e escalar. Falha se um delegado expirado, a pessoa errada, um escopo ampliado ou um recibo ausente é aceito; o administrador precisa corrigir a fonte governada, versionar o pacote e retestar. Publicar uma planilha de contatos sem detecção demonstrada de falha não encerra o tíquete. A repetição F1 de incidente, separada, permanece fora deste exercício anterior ao incidente e não está neste manuscrito.

### Ateliê de prontidão do módulo 1 — resolução

**Cartão de serviço:** caso `HL-IR-001`; resultado: moradores podem ver e reservar a sala correta; dependências: serviço de identidade da equipe e base de reservas; autoridade atual de coleta: o líder fictício do incidente permite análise só de R1–R8; o responsável pelo serviço precisa ser consultado antes de uma interrupção de reservas. O administrador de identidade está listado como custodiante de um pedido futuro *possível*, não como alguém já entrevistado.

**Trecho do registro de evidência:** R1 às 08:40 UTC registra diretamente uma entrada bem-sucedida de `desk-a`; não identifica o humano que controla a sessão. R4 às 08:44 registra o cancelamento de B18; não estabelece por que foi cancelada. R5 às 08:48 registra um relato de frequentador, não um relato verificado de forma independente de todo sintoma. R6 às 08:50 registra um intervalo de treinamento agendado, mas não a lista autorizada de tarefas. R7 às 08:52 relata um trabalho de cópia concluído, mas nenhum resultado de restauração. R8 às 08:55 tem detalhe de rede insuficiente para sustentar uma conclusão de exfiltração. Uma entrega completa também cita R3 e preserva a ordem UTC original.

**Cartão de decisão às 09:05 UTC:** preservar os registros fornecidos e perguntar ao responsável pelo treinamento se B17 e B18 estavam planejadas. Benefício esperado: evitar uma interrupção desnecessária de acesso enquanto se testa H1; custo possível: se a conta está sendo usada de forma indevida, outra edição poderia ocorrer antes da revisão. O líder fictício do incidente aprova a análise limitada do registro; o responsável pelo serviço revisa o impacto no serviço. Reavaliar às 09:15 UTC, ou antes se uma edição nova verificada for relatada. A opção rejeitada de restrição imediata poderia reduzir uso indevido adicional, mas interromperia o trabalho da recepção e exige aprovações explícitas de serviço e de identidade. Nenhuma das opções é rotulada como a resposta unicamente correta.

**Contrafactual mantido à parte:** se a edição hipotética das 09:08 fosse verificada e estivesse fora do treinamento, o líder elevaria a urgência, preservaria o registro novo sob um escopo atualizado e buscaria aprovação para uma restrição temporária de conta. Removida a injeção, o caso original volta a uma causa não confirmada. A amostra obtém cinco pontos de rubrica se o registro completo, a autoridade e o gatilho de revisão estão presentes; quem omite a fronteira de coleta precisa revisá-la, qualquer que seja a nota total.

**Raciocínio adicional:** Um mapa incompleto de aprovadores é resolvido por um contato alternativo bem-sucedido e por um ensaio de decisão, não só por acrescentar um nome a uma planilha. Um teste significativo apresenta um aprovador primário indisponível, registra quando o substituto recebe o caso fictício, e confere se uma decisão autorizada, com escopo e hora de revisão, é registrada dentro de um intervalo-alvo definido localmente. Uma lacuna de prontidão de log exige recuperar a linha sintética pré-declarada e excluir um controle fora do intervalo, com filtros guardados. Uma lacuna de prontidão de recuperação exige uma restauração contida separada e uma comparação de estado de reserva aprovada pelo responsável. Nenhuma das tarefas é provada pelo relatório de trabalho de cópia de R7. O tíquete de melhoria deve declarar que resultado constitui falha e qual dono precisa responder.

<a id="ir-rapid-ch01-ar1-result"></a>

### Laboratório offline AR1 do módulo 1 — resolução

#### Saída exata esperada — executada com Python 3

~~~text
VALID_AUDIT REHEARSAL_PATH_VALID_NOT_EXECUTED
VALID_DELEGATED_PAUSE REHEARSAL_PATH_VALID_NOT_EXECUTED
EXPIRED_DELEGATE HOLD_DELEGATION_EXPIRED
WRONG_PERSON HOLD_WRONG_APPROVER
EXCESS_SCOPE HOLD_SCOPE_EXCEEDED
EMPTY_OBJECTS HOLD_EMPTY_SCOPE
APPROVAL_ABSENT HOLD_APPROVAL_MISSING
STALE_VERSION HOLD_STALE_REGISTER
WRONG_CUSTODIAN HOLD_WRONG_CUSTODIAN
BAD_CHANNEL HOLD_UNAPPROVED_CHANNEL
NO_CONFIRMATION HOLD_CONFIRMATION_MISSING
REVOKED_DELEGATE HOLD_DELEGATION_REVOKED
EXPIRED_REGISTER HOLD_REGISTER_OUT_OF_DATE
MISSING_RECEIPT HOLD_APPROVAL_MISSING
SAFE_ESCALATION ESCALATE_HOLD_DELEGATION_EXPIRED
~~~

#### Interpretação resolvida e modos de falha

Os dois primeiros cenários são controles positivos. Afirmam apenas que o **roteamento simulado de autoridade** satisfaz os requisitos declarados do AR1 na hora selecionada. Ambos ainda terminam em `NOT_EXECUTED` porque nenhuma peça de treinamento representa uma coleta real ou uma mudança de serviço.

`EXPIRED_DELEGATE` move o ensaio para 14:31, depois do fim exclusivo do delegado às 14:30. `WRONG_PERSON` substitui o alternativo por um apelido arbitrário que não tem papel registrado. `EXCESS_SCOPE` pede um objeto sem relação de boletim além de um identificador autorizado de treinamento. Esses testes precisam ser retidos mesmo que outros campos permaneçam válidos. `EMPTY_OBJECTS` confirma que um conjunto vazio não pode passar de forma vazia como pedido limitado.

`APPROVAL_ABSENT` omite o recibo do papel de responsável pelo serviço exigido pela regra de pausa. `STALE_VERSION` usa AR-2 enquanto o registro atual declarado é AR-3. `WRONG_CUSTODIAN` nomeia um operador da aplicação para uma tarefa de custódia de auditoria. São lacunas diferentes e precisam de correções diferentes.

`BAD_CHANNEL` fornece uma rota não registrada; `NO_CONFIRMATION` retém uma confirmação mesmo na rota nominalmente registrada. Ambos demonstram que um nome plausível e um campo de aprovação não bastam. Em operações reais, identidade e autoridade organizacional exigiriam prova crível e independente, além destes booleanos.

`REVOKED_DELEGATE` rejeita um substituto cuja delegação foi expressamente retirada no **registro governado**. O solicitante não pode se sobrepor a esse estado. `EXPIRED_REGISTER` rejeita uma data fora da própria validade do registro, independentemente de qualquer delegado. `MISSING_RECEIPT` carece do recibo simulado de decisão.

`SAFE_ESCALATION` é o controle de segurança: **não passa**. O resultado pede ao processo responsável de escalada que obtenha uma decisão autorizada e atual, enquanto a operação proposta permanece retida. Quem descreve isto como aprovação de emergência não entendeu a lição.

A função devolve a **primeira** falha detectada. Numa revisão real pode haver várias deficiências simultâneas. O avaliador deve preservar quaisquer defeitos adicionais e não deve inferir que campos não testados são válidos a partir de um único código de erro.

**Limites técnicos:** O modelo se apoia em identificadores inventados de papel, num registro gravado, em recibos sintéticos, em sinalizadores declarados de confirmação e em carimbos Python com consciência de UTC. Não valida um sistema corporativo de identidade, não detecta uma aprovação forjada, não autentica uma pessoa, não prova que uma delegação foi emitida por um dono real de governança, não autoriza uma coleta real nem executa uma ação. Um programa real exigiria proveniência da fonte, identidades verificadas, informação de revogação, evidência adequada de aprovação e canais permitidos. Uma aprovação em Python **nunca** é permissão.

**Entrega de quem estuda:** Registre as 15 linhas de saída, classifique cada cenário como roteamento válido, pedido retido ou escalada com retenção, explique a causa distinta de pelo menos cinco controles negativos, e identifique quais registros e procedimentos de verificação do mundo real seriam exigidos antes de confiar num fluxo comparável.

#### Saída suplementar exata — executada com Python 3

~~~text
REQUEST_SCOPED_TR01 REHEARSAL_PATH_VALID_NOT_EXECUTED
REQUEST_SCOPED_PAUSE REHEARSAL_PATH_VALID_NOT_EXECUTED
REUSED_RECEIPT_TR02 HOLD_RECEIPT_SCOPE_MISMATCH
REUSED_REQUEST_ID HOLD_RECEIPT_SCOPE_MISMATCH
~~~

#### Explicação resolvida

`REQUEST_SCOPED_TR01` e `REQUEST_SCOPED_PAUSE` coincidem com os registros inventados e separados de emissão. `REUSED_RECEIPT_TR02` muda o objeto de TR-01 para TR-02, retendo o recibo de sala emitido antes; o pedido permanece dentro do conjunto *geral* de fontes permitidas, mas esta **aprovação específica não foi emitida para esse objeto**. `REUSED_REQUEST_ID` substitui um identificador de pedido que pertence a outra operação, portanto o registro alegado de aprovação não pode coincidir.

Esta é uma **verificação de segunda camada**: um resultado positivo completo de ensino deve exigir tanto a verificação original de rota de papel e de delegação quanto a verificação de emissão presa ao pedido. As quinze saídas originais permanecem corretas **para o que o programa original de fato confere**; não estabelecem esta propriedade adicional. Os registros do emissor são premissas fictícias gravadas; um desenho de produção precisaria de uma fonte autenticada e governada do emissor e de proteção contra falsificação, repetição e modificação não autorizada. Nenhuma ação é executada por qualquer dos programas.

**Condição de parada da revisão:** Se um papel, um recibo ou um vínculo de pedido não puder ser autenticado em trabalho real de resposta, retenha a execução e siga o procedimento atual de autorização ou escalada da organização. Uma rota válida só de ensino não se torna permissão para coletar dados ou mudar um serviço.

[Voltar ao laboratório AR1](#ir-rapid-ch01-ar1-lab).

<a id="w1-review-answers"></a>

### Prática de revisão da semana 1 — resultados suplementares resolvidos

W1-R1–W1-R5 suplementam as aulas 01–05 e EX001–EX050 já existentes. Não são aulas nativas novas nem um substituto dos exercícios numerados. As resoluções de EX014 em diante pertencem a capítulos posteriores e não estão neste manuscrito.

<a id="w1-answer-01"></a>

### W1-R1 — Resolução

| Relatório | Admissibilidade e conclusão sustentada | Evidência ausente e próximo passo limitado |
|---|---|---|
| A | A entrada não satisfaz o quadro declarado de seis objetos. O cálculo de uma linha pode estar correto, mas não pode responder à pergunta anunciada. | Pedir os objetos ausentes ou uma revisão de escopo justificada à parte. Reter a entrada parcial e não chamá-la de resultado limpo e completo. |
| B | O quadro de um objeto está satisfeito. Ausência de sobreposição nessa entrada declarada é um resultado estreito de modelo. | Uma pergunta de seis objetos, a completude real da fonte, a aplicabilidade da política aprovada e a correção de produção permanecem não testadas. Não inflacione a conclusão. |
| C | O ponteiro R4 sustenta um cancelamento registrado, não as alegações anexadas de identidade humana ou de aprovação. | Pedir o contexto aprovado de tarefa e a evidência autorizada e adequada de identidade, pelos donos; não relate essas verificações como executadas. |

O relatório A não equivale a um quadro completo sem achados. O relatório B não é intrinsecamente inválido só porque é pequeno: o escopo declarado é diferente. O relatório C ilustra uma alegação semântica excessiva que um validador de contagem de linhas não detectaria. Uma resposta correta preserva as três distinções e mantém as peças de modelo fora do livro canônico do incidente.

[Voltar à tarefa](#w1-review-01) · [Índice do curso](../SUBJECTS.md)

<a id="w1-answer-02"></a>

### W1-R2 — Resolução

A transcrição executada da extensão, de cinco linhas, é:

~~~text
W1_BASE EVALUATED CONFLICT S03/S04;INVALID_INTERVAL S06
W1_EMPTY INPUT_REJECTED EMPTY_OR_INVALID_INPUT
W1_MISSING_S04 INPUT_REJECTED COVERAGE_MISMATCH
W1_BAD_CLOCK INPUT_REJECTED CLOCK_FORMAT
W1_NARROW_SCOPE EVALUATED NO_FINDINGS_IN_SCOPE
~~~

O quadro de base é admitido porque os seis identificadores e os campos interpretáveis satisfazem o contrato novo. Ainda contém o conflito original S03/S04 e o achado de duração zero de S06. Um revisor que remove S06 para fazer o teste parecer mais limpo muda a evidência em vez de corrigir o modelo.

A entrada vazia é rejeitada antes da interpretação. Remover S04 falha a comparação com o quadro esperado; o invólucro, portanto, não apresenta a contagem reduzida de conflitos como resposta à pergunta original de seis objetos. O acompanhamento limitado é pedir ao custodiante do ensaio o objeto declarado ausente ou um escopo revisto explícito, não inventar o conteúdo.

A entrada `9:00` falha a regra de formato exato desta extensão, mesmo que o analisador original possa interpretá-la numericamente. Essa diferença é uma escolha documentada sobre o contrato de entrada de brinquedo, não prova de que todas as horas de um dígito são inválidas em sistemas reais.

A última chamada pede de propósito uma pergunta de um objeto. O resultado sem achados permanece restrito a esse quadro declarado. Coincidir identificadores esperados não demonstra autenticidade nem que o conjunto esperado representa todo objeto relevante num serviço real.

[Voltar à tarefa](#w1-review-02) · [Resultado original BSL1](#ir-rapid-ch01-bsl1-result)

<a id="w1-answer-03"></a>

### W1-R3 — Resolução

A transcrição executada de cinco linhas é:

~~~text
W1_TYPO UNKNOWN_COMPONENT
W1_UNKNOWN_DB UNRESOLVED
W1_UNKNOWN_DB_IDENTITY_DOWN IMPAIRED
W1_MANUAL POSSIBLE
W1_PARTIAL_STATES_CHECKED 243
~~~

| Função | Base desconhecida; todo outro componente verdadeiro | Base desconhecida; identidade falsa; outros componentes verdadeiros |
|---|---|---|
| `site_reachable` | `POSSIBLE` | `POSSIBLE` |
| `room_view` | `UNRESOLVED` | `UNRESOLVED` |
| `staff_edit` | `UNRESOLVED` | `IMPAIRED` |
| `manual_intake` | `POSSIBLE` | `POSSIBLE` |
| `new_backup_job` | `UNRESOLVED` | `UNRESOLVED` |

A falha de identidade muda a edição pela equipe porque a identidade é exigida para essa função. Não resolve o estado da base nem afeta funções que não dependem de identidade neste modelo. Com um pré-requisito falso e conhecido, toda conclusão dos desconhecidos restantes ainda deixa falsa a conjunção de edição pela equipe. Com só a base desconhecida, algumas conclusões permitem a rota e outras a prejudicam, portanto sem resolução é a classificação adequada.

Uma mensagem aceitável de duas frases é: “No modelo PATH1 independente, a edição pela equipe está prejudicada quando a identidade é falsa, enquanto a visão dependente da base permanece sem resolução. A recepção na central permanece estruturalmente possível, mas nenhum procedimento alternativo aprovado, reserva confirmada ou resultado real de serviço foi demonstrado.”

O laço final confere 243 atribuições parciais e cinco classificações de função por atribuição, ou 1.215 comparações de modelo. Não autentica estados de componente nem valida a tabela de dependência contra um sistema real. Os seis cenários originais PATH1, todos conhecidos, também foram conferidos pela guarda de identificador sem mudar as saídas.

[Voltar à tarefa](#w1-review-03) · [Resultado original PATH1](#ir-rapid-ch01-path1-result)

<a id="w1-answer-04"></a>

### W1-R4 — Resolução

A transcrição executada de oito linhas é:

~~~text
W1_ORIGINAL_TEXT_FALSE REHEARSAL_PATH_VALID_NOT_EXECUTED
W1_TYPED_TEXT_FALSE HOLD_INPUT_CONFIRMATION_TYPE
W1_TYPED_REAL_FALSE HOLD_CONFIRMATION_MISSING
W1_TYPED_VALID REHEARSAL_PATH_VALID_NOT_EXECUTED
W1_TYPED_REUSED_RECEIPT HOLD_RECEIPT_SCOPE_MISMATCH
W1_DELEGATE_13:00 REHEARSAL_PATH_VALID_NOT_EXECUTED
W1_DELEGATE_14:29 REHEARSAL_PATH_VALID_NOT_EXECUTED
W1_DELEGATE_14:30 HOLD_DELEGATION_EXPIRED
~~~

| Entrada | Interpretação |
|---|---|
| Texto `"false"` | Tipo inválido de confirmação sob o contrato booleano declarado; o invólucro novo para antes da avaliação de autoridade. |
| Booleano `False` | Não confirmação explícita e interpretável; a verificação existente de confirmação retém o pedido. |
| Booleano `True` com todas as premissas originais válidas | O portão de tipo passa; as verificações inalteradas de autoridade e de recibo produzem um caminho simulado válido, não execução. |
| Recibo reutilizado para TR-02 | Confirmação bem tipada não repara o descompasso do pedido; a verificação existente de vínculo ainda o retém. |

A delegação começa de forma inclusiva às 13:00 e termina de forma exclusiva às 14:30. Portanto 13:00 e 14:29 podem satisfazer a condição de tempo; 14:30 não pode. As outras premissas de papel, escopo e confirmação da peça de fonte ainda são exigidas em cada hora. O teste de fronteira não é permissão para executar depois que uma verificação anterior passou.

A verificação nova de tipo não verifica um retorno real, não prova consentimento, não autentica um emissor nem cria uma delegação. Também não valida por completo todo campo do pedido. Um tíquete correto de melhoria identifica esta classe específica de entrada, preserva os testes existentes válidos e inválidos de autoridade, e deixa garantia mais ampla de esquema e de identidade como trabalho separado.

[Voltar à tarefa](#w1-review-04) · [Resultado original AR1](#ir-rapid-ch01-ar1-result)

<a id="w1-answer-05"></a>

### W1-R5 — Resolução

| Formato original de sete campos | Entrada de abertura das 09:00 limitada pela evidência |
|---|---|
| 1. Identificador do caso e hora de abertura | `HL-IR-001`; 2026-10-11 09:00 UTC. |
| 2. Serviço | Reserva de salas da Harbor Library; responsável pelo serviço a confirmar. |
| 3. Relator e fonte | Tíquete `T-104` da central, do contexto de caso da seção 1.5; R5 registra o relato do frequentador às 08:48 de que B18 desapareceu. |
| 4. Sinal observado com ponteiros | R1 registra a entrada de `desk-a` às 08:40; R3 registra a mudança de B17 às 08:43; R4 registra o cancelamento de B18 às 08:44; R5 registra o relato posterior do frequentador. |
| 5. Avaliação e incerteza | Investigar as mudanças relatadas e o sintoma. Comprometimento, ator humano, aprovação da tarefa, horário ordinário de funcionamento e estado atual correto da reserva não estão estabelecidos. R6 fornece um intervalo de treinamento agendado, não aprovação destas mudanças. |
| 6. Escopo e autoridade permitidos | Ler, anotar e comparar o pacote sintético fornecido R1–R8. Nenhuma coleta nova, acesso a sistema real ou ação disruptiva é autorizada por este exercício. |
| 7. Próxima pergunta, dono e revisão | Propor que o líder do incidente coordene uma verificação, pelo responsável pelo serviço ou pelo treinamento, de se B17/B18 eram tarefas aprovadas, antes do marco de decisão das 09:05; reter a revisão das 09:15 da seção 1.5 como revisão planejada posterior, não como ação executada. |

**Nota de correção:** O qualificador de horário ordinário foi removido porque o pacote não fornece a política necessária para comparar a entrada das 08:40 com o horário normal de funcionamento.

A nota não estabelece a alegação oposta de que a entrada era ordinária. Preserva a ordenação válida da fonte e separa o relato do frequentador de uma comparação verificada de estado. O marco proposto das 09:05 e a revisão planejada das 09:15 não são carimbos de evento de fonte e não estão registrados como decisões concluídas às 09:00.

Formulação alternativa é aceitável quando os mesmos sete campos, os limites de evidência, o estado pendente do responsável e as ações propostas permanecem explícitos. Um registro mais curto que omite o limite da fonte não melhora só por ser conciso.

[Voltar à tarefa](#w1-review-05) · [Resposta original EX007](#ex007--worked-result)

A aula seguinte da edição inglesa não está neste manuscrito.

## Glossário do módulo 1

- **Função de serviço:** uma operação distinta voltada ao usuário, com um resultado útil definido.
- **Dependência técnica:** um componente exigido para uma operação sob um modelo declarado.
- **Modo degradado:** um estado operacional mais estreito, aprovado pelo responsável, com limites explícitos sobre o que pode ser prometido.
- **Possibilidade estrutural:** uma previsão do modelo de que os pré-requisitos estão disponíveis, não prova de comportamento de negócio bem-sucedido ou autorizado.

- **Linha de base de comportamento:** uma descrição versionada, aprovada pelo responsável, dos resultados de serviço esperados num escopo declarado.
- **Intervalo semiaberto:** um intervalo de tempo que inclui o início e exclui o fim; intervalos adjacentes não precisam se sobrepor.
- **Invariante de negócio:** uma propriedade que se espera permanecer verdadeira sempre que as condições declaradas da política se aplicam.
- **Limitação de cobertura:** um motivo pelo qual um resultado de teste pode omitir objetos ou intervalos relevantes; menos achados a partir de uma entrada incompleta não mostram reparo.

- **Alerta:** um sinal que uma regra ou uma pessoa marcou para avaliação.
- **Artefato:** um registro ou objeto produzido durante a investigação ou a resposta.
- **Autorização:** a permissão e o escopo sob os quais uma ação de resposta pode ser tomada.
- **Ponteiro de evidência:** um identificador estável que permite a um revisor localizar o registro subjacente.
- **Hipótese:** uma explicação a testar, não uma causa confirmada.
- **Registro de incidente:** o relato compartilhado de observações, decisões, donos e tempos.
- **Responsável pelo serviço:** a pessoa que responde pelo resultado de negócio do serviço e pelos compromissos.
- **Registro de autoridade:** um registro governado e versionado de quem pode aprovar uma operação e um escopo definidos, com a fonte atual e o período de validade.
- **Delegação:** uma transferência documentada e limitada de autoridade de decisão a um substituto, sujeita a escopo, expiração e possível revogação.
- **Revogação:** retirada de uma delegação antes da expiração declarada; o registro governado, e não o solicitante, fornece o estado dela no exercício AR1.
- **Custodiante:** o papel responsável por uma fonte ou por uma ação de serviço, distinto da pessoa que aprova a decisão.

Os glossários dos módulos 2, 3 e 4 da edição inglesa não estão neste manuscrito.

Todos os nomes, contas, reservas, logs e horários da **Harbor Library** são inventados para o ensino.

## Referências citadas no capítulo 1

As entradas abaixo são as da edição inglesa que este capítulo cita. Não foram traduzidas. Fontes citadas só por capítulos posteriores não são listadas aqui. Algumas notas de uso da edição inglesa mencionam o módulo 3, o módulo 4 ou a aula TRI2; esse ensino não está neste arquivo.

1. NIST, [SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*](https://csrc.nist.gov/pubs/sp/800/61/r3/final), April 2025. Used for the integration of response across risk-management activities.
2. NIST, [Cybersecurity Framework 2.0 FAQ](https://www.nist.gov/cyberframework/faqs), section “Framework Components.” Used for the six concurrent and continuous functions.
3. OpenCyber Academy, [incident-response practice playbook index](../../../../../playbooks/incident-response-resilience/README.md). This index points to revision-pinned source playbooks; it is supplementary to the book. Source repositories retain their own rights.
5. NIST, [SP 800-184, *Guide for Cybersecurity Event Recovery*](https://csrc.nist.gov/pubs/sp/800/184/final), December 2016. Used for the Module 3 emphasis on planned, verifiable recovery.
6. NIST, [SP 800-34 Rev. 1, *Contingency Planning Guide for Federal Information Systems*, updated edition](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), November 2010. Used for the distinction between a backup status and a tested recovery plan.
7. NIST, [SP 800-84, *Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities*](https://csrc.nist.gov/pubs/sp/800/84/final), September 2006. Used for the Module 4 design, conduct and evaluation of a tabletop exercise.
14. NIST, [Cybersecurity Framework 2.0 (CSWP 29)](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), February 2024. Provides flexible risk-management outcomes used as context for the TRI2 priority-review lesson; it does not prescribe TRI2 labels, decision thresholds or a universal incident-severity matrix.

O capítulo 1 também cita a seção 2.1 e as seções 2.2–2.3 do PDF [NIST.SP.800-61r3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf), a publicação [CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final), a página do framework em [nvlpubs NIST.CSWP.29](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), e a documentação do Python sobre [correspondência de cadeia inteira](https://docs.python.org/3/library/re.html#re.fullmatch) e [teste de valor de verdade](https://docs.python.org/3/library/stdtypes.html#truth-value-testing).

### Continue estudando

O capítulo 2 ainda não está neste manuscrito. Os capítulos 2, 3 e 4 da referência inglesa ficaram de fora desta tradução.
