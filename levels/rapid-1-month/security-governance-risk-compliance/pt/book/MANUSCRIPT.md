# Governança, Riscos e Compliance de Segurança: Curso Prático de Um Mês

- Idioma: português do Brasil (`pt`); curso 005, curso rápido (1 mês). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–4 de 4 estão escritos; os exercícios EX001–EX050 têm resoluções correspondentes. O capítulo 1 e os exercícios EX001–EX005 são texto do autor original, traduzido com fidelidade e sem alterações de conteúdo; os capítulos 2–4 e os exercícios EX006–EX050 continuam o mesmo caso Northstar, com rubricas de 0 a 3. Os laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. A contagem de páginas A4 não foi verificada.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); [escopo e exceções](../../../../../RIGHTS.md); as obras citadas mantêm seus direitos.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este livro

Este curso ensina uma pequena equipe de segurança a transformar prioridades de negócio em uma estratégia de segurança curta e testável. Os leitores trabalham com uma organização fictícia, para que todos os exercícios possam ser feitos sem acesso a uma empresa real ou a seus registros confidenciais. O produto final será uma estratégia de uma página, um plano de ação priorizado e uma planilha compacta de medição. Os leitores só podem aplicar o método a uma organização real se tiverem permissão para acessar suas informações.

Este é o livro principal do curso rápido de Governança, riscos e compliance de segurança. Ele incorpora como primeiro capítulo o rascunho anterior sobre estratégia de segurança. O [índice de disciplinas](../SUBJECTS.md) e o [plano do livro](PLAN.md) definem quatro capítulos, um por disciplina. Cada capítulo traz seus próprios exemplos e exercícios; todas as resoluções ficam no apêndice final deste mesmo livro. O capítulo 1 define a estratégia; os capítulos 2–4 a estendem para escopo e permissão, dependências e dados, e um exercício guiado de restauração com uma decisão registrada.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Northstar Community Services** | Organização fictícia com portal público de agendamento, gestão de casos e escala de voluntários | Inventada |
| **Diretor de operações** | Dono do serviço de agendamento e das decisões de tradeoff | Inventado |
| **Engenheiro de segurança** | Único profissional de segurança da Northstar | Inventado |
| **Responsável pela proteção de dados** | Segundo aprovador quando há dados pessoais de clientes | Inventado |

### Fontes principais

NIST [Cybersecurity Framework 2.0](https://doi.org/10.6028/NIST.CSWP.29); NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10); relatório público do U.S. GAO sobre a Colonial Pipeline ([GAO-21-105263](https://www.gao.gov/products/gao-21-105263)). As fontes de cada parte aparecem no fim do capítulo 1 e do capítulo 4, como na edição em inglês.

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Resoluções](#worked-results)

<a id="ch-01"></a>

## Capítulo 1 — Governança, riscos e compliance de segurança: fundamentos e decisões

### Objetivos de aprendizagem

Ao final deste capítulo, o leitor deve ser capaz de distinguir um objetivo de negócio de uma atividade de segurança, explicar como um cenário de risco afeta um serviço, identificar quem deve ser dono de uma decisão, escrever um resultado de segurança mensurável e testar se uma ação proposta pertence a uma estratégia.

### 1.1 O problema de decisão

Uma estratégia de segurança é um conjunto de escolhas sobre o que a organização vai proteger, por que isso importa, que nível de interrupção ou perda ela consegue tolerar, quem pode decidir e como o progresso será verificado. Ela tem um horizonte de tempo e um limite de recursos. Uma lista de controles, ferramentas ou normas é uma evidência útil para uma estratégia, mas a lista sozinha não explica qual resultado importa primeiro.

Considere duas propostas: “Comprar uma nova plataforma de segurança” e “Restaurar o serviço de agendamento de clientes em até quatro horas após um evento destrutivo”. A primeira é uma atividade possível. A segunda é um resultado de serviço. Para cumprir o resultado, a organização pode acabar precisando de uma plataforma, de backups, de runbooks, de treinamento ou de uma arquitetura diferente. O resultado oferece um motivo para comparar essas opções. Ele também cria um teste: um exercício cronometrado de restauração pode mostrar se a promessa é crível.

O [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) oferece uma linguagem útil para esse trabalho. Suas seis funções são Govern, Identify, Protect, Detect, Respond e Recover. Uma estratégia usa as seis, mas é em Govern que a organização define expectativas, responsabilidades e a direção de risco. Os [recursos de início rápido para pequenas empresas](https://www.nist.gov/itl/smallbusinesscyber/nist-cybersecurity-framework-0) do NIST ilustram que uma organização modesta pode começar pelo próprio contexto e pelas próprias prioridades, em vez de copiar um programa grande de outra empresa.

### 1.2 Comece por um serviço, não por um produto

O trabalho de segurança tem valor porque protege um serviço, um dever, uma pessoa ou um ativo que importa para a missão. Comece nomeando os serviços em linguagem simples. Um processador de pagamentos pode depender de autorização de cartões, liquidação, acesso de lojistas e suporte. Uma clínica pode depender de agendamento de consultas, acesso a prontuários e resultados de laboratório. A mesma tecnologia pode sustentar vários serviços, e um único serviço pode atravessar vários fornecedores e sistemas.

Para cada serviço, registre cinco fatos: o dono, as pessoas afetadas, os sistemas e dados de suporte, a interrupção máxima tolerável e as consequências da falha. O dono é a pessoa responsável por escolher os tradeoffs aceitáveis; a equipe de segurança fornece evidências e opções. Um dono crível consegue dizer se uma indisponibilidade de quatro horas importa mais do que um lançamento atrasado e pode aprovar um exercício de recuperação que ocupe temporariamente o tempo da equipe.

Não tente tornar o primeiro inventário perfeito. Uma primeira passada que nomeie os serviços mais importantes e as dependências desconhecidas é mais útil do que uma planilha abrangente cujas linhas não têm dono. Registre a incerteza como incerteza. Se o tempo de recuperação for um palpite, marque-o como uma premissa a validar com o dono do serviço.

### 1.3 Traduza uma ameaça em um cenário de negócio

“Ransomware” é um rótulo de ameaça. “O serviço de agendamento fica indisponível por dois dias porque os administradores não conseguem restaurar seu banco de dados” é um cenário de risco. O cenário pode ser testado contra evidências: idade do backup, tempo de restauração, separação das contas de administrador e existência de um processo manual de agendamento. Ele também tem uma consequência de negócio: atraso no serviço, sobrecarga da equipe ou impacto contratual.

Um cenário compacto tem quatro partes:

1. **Condição:** o evento ou a fraqueza que pode ocorrer.
2. **Serviço:** o processo de negócio que seria afetado.
3. **Consequência:** o tipo de dano que se seguiria.
4. **Lacuna de evidência:** o que ainda não se sabe bem o bastante para decidir.

Por exemplo: “Se uma conta de administrador comprometida puder apagar tanto o banco de dados de agendamento em produção quanto seus backups, os agendamentos podem parar além da meta de quatro horas; a equipe não executou um teste completo de restauração neste trimestre.” A afirmação não diz que houve comprometimento. Ela liga uma condição plausível a um resultado de serviço mensurável e a uma lacuna testável.

Incidentes reais mostram por que essas distinções importam. Em seu relatório público sobre o evento de ransomware da Colonial Pipeline em 2021, o [U.S. Government Accountability Office](https://www.gao.gov/products/gao-21-105263) afirma que o ransomware foi implantado contra os sistemas de negócio da operadora e discute a resposta posterior em segurança de dutos. A lição estratégica aqui é uma **inferência**: dependências de sistemas de negócio podem afetar decisões operacionais, por isso o mapeamento de serviços e o planejamento de continuidade não devem parar no sistema técnico mais visível. Este livro não infere dessa fonte a causa raiz detalhada do incidente.

### 1.4 Escolha resultados que possam ser verificados

Um resultado de segurança descreve um estado que a organização quer alcançar. Ele deve ter um dono, uma data, uma fronteira e evidências. “Melhorar o monitoramento” não tem fronteira nem teste de sucesso. “Até o fim do trimestre, todo provedor de identidade de produção e toda aplicação exposta externamente enviam eventos de segurança ao repositório de logs monitorado, e um relatório semanal de cobertura identifica as fontes ausentes” pode ser verificado.

Um resultado não precisa garantir que nenhum incidente ocorrerá. Equipes de segurança não podem prometer zero ataques ou zero perdas. Elas podem estabelecer expectativas claras sobre capacidade: detectar uma classe de evento dentro de um tempo definido, restaurar um serviço dentro de uma janela testada, revisar acessos privilegiados em uma cadência definida ou resolver exposições críticas segundo uma regra de risco acordada. A medição deve usar evidências coletadas no trabalho cotidiano, e não números inventados para uma apresentação.

Medidas úteis combinam **cobertura**, **qualidade** e **efeito**. Cobertura pergunta se a população-alvo está incluída. Qualidade pergunta se um controle funciona sob teste. Efeito pergunta se o resultado do serviço melhorou. Para backups, essas medidas podem ser: percentual de serviços críticos com cópias protegidas; percentual de restaurações amostradas que dão certo; e tempo medido para restaurar um serviço. Um número alto de cobertura de backup não substitui um teste de restauração.

### 1.5 Defina prioridades sob um limite real

A maioria das equipes não consegue fazer tudo ao mesmo tempo. Por isso uma estratégia precisa de uma regra explícita de priorização. Comece pela criticidade e pela exposição do serviço e depois considere as evidências que sustentam o cenário, o tempo necessário para reduzir o risco, as dependências e o custo. Use rótulos consistentes como “agir neste mês”, “planejar neste trimestre” e “aceitar por ora, com um dono e uma data de revisão”. Evite a falsa precisão: uma nota 8,7 não é útil se ninguém consegue explicar como ela foi calculada ou que decisão muda em 8,7.

Uma ação pode ser valiosa mesmo quando é pequena. Testar se os backups podem ser restaurados pode custar menos do que comprar uma ferramenta nova e revelar a lacuna de maior consequência. Inversamente, um dashboard de segurança vistoso pode ser um mau investimento inicial se ninguém for dono dos alertas por trás dele. Priorizar é decidir sobre a **redução esperada de danos relevantes**, não uma competição para implantar o maior número de controles.

A estratégia deve nomear o que fica adiado e por quê. Um adiamento aprovado não é evidência de que o risco desapareceu. Ele registra o tradeoff, o dono, as medidas compensatórias e a data em que a decisão será revista. O [NIST Privacy Framework](https://www.nist.gov/privacy-framework), separado, pode ajudar quando o cenário envolve danos decorrentes do tratamento de dados pessoais; o risco de privacidade é mais amplo do que a prevenção de vazamentos.

### 1.6 Um exemplo curto de trabalho

A fictícia **Northstar Community Services** opera um portal público de agendamento, um serviço interno de gestão de casos e uma escala de voluntários. Sua equipe executiva tem um engenheiro de segurança e orçamento limitado para os próximos três meses. A organização não tem um inventário confirmado de integrações com terceiros. Seu resultado de serviço mais importante é que os agendamentos possam continuar durante uma indisponibilidade de sistema, mesmo que o portal fique temporariamente fora do ar.

Uma primeira conversa sobre estratégia pode produzir o seguinte registro:

| Item de decisão | Primeiro rascunho | Evidência a solicitar |
|---|---|---|
| Serviço prioritário | Agendamento de consultas | Confirmação do dono do serviço e mapa de dependências |
| Interrupção tolerável | Quatro horas | Dimensionamento da recepção e teste do processo manual |
| Cenário principal | Portal ou banco de dados indisponível após comprometimento de conta | Revisão de acessos de identidade e teste de restauração |
| Primeiro resultado | Executar uma restauração cronometrada de ponta a ponta e documentar o resultado em até 30 dias | Log do exercício, carimbos de tempo, aprovação formal do dono do serviço |
| Medida provisória | Revisão diária de falhas de backup e de mudanças privilegiadas | Log de revisão e roteamento de alertas |
| Dono da decisão | Diretor de operações | Aceitação por escrito da meta de serviço e do uso de recursos |

Isto é deliberadamente incompleto. A meta de quatro horas é uma premissa de trabalho até que o diretor de operações a valide. O mapa de dependências pode mudar a prioridade. O exercício pode revelar que o processo manual é mais importante do que a restauração técnica. Uma estratégia pode mudar quando as evidências melhoram; a mudança deve ser registrada para que as pessoas entendam por que a decisão mudou.

### 1.7 O teste da estratégia em uma página

Antes de comprar ou construir qualquer coisa, tente escrever seis frases:

1. Precisamos manter **este serviço** disponível ou recuperável para **estas pessoas**.
2. O dono do serviço aceita **este limite de impacto**.
3. Nossos principais cenários sustentados por evidências são **estes**.
4. Neste trimestre entregaremos **estes resultados mensuráveis**.
5. **Estes donos** tomarão as decisões de tradeoff e executarão o trabalho.
6. Revisaremos **estes sinais** **nesta cadência** e revisaremos o plano quando as evidências mudarem.

Se alguma frase for impossível de completar, o fato que falta é a próxima tarefa de pesquisa. O objetivo do teste de uma página não é esconder a complexidade. Ele obriga a equipe a mostrar a relação entre missão, risco, ação e evidência antes de se expandir em um plano longo.

### Exercícios do capítulo 1

Estes cinco exercícios são os primeiros do mínimo exigido de cinquenta. Suas resoluções aparecem no fim deste rascunho. Use apenas o caso fictício da Northstar Community Services apresentado acima.

### EX001 — Atividade ou resultado

Classifique cada afirmação como atividade ou como resultado de serviço mensurável e depois reescreva uma atividade como resultado: (a) comprar uma ferramenta de segurança de endpoint; (b) restaurar o agendamento de consultas a partir do backup em até quatro horas em um exercício cronometrado; (c) escrever uma política sobre phishing; (d) enviar um alerta a um revisor designado em até quinze minutos após uma mudança em conta privilegiada.

### EX002 — Construção de cenário

Escreva um cenário de risco em quatro partes para a escala de voluntários, usando condição, serviço, consequência e lacuna de evidência. Declare uma premissa que precise de confirmação. Não afirme que tenha ocorrido qualquer violação.

### EX003 — Seleção de evidências

A Northstar informa que “todos os serviços críticos têm backups”. Cite três evidências que testariam se isso sustenta seu objetivo de continuidade dos agendamentos. Explique por que uma captura de tela da configuração, sozinha, é insuficiente.

### EX004 — Decisão de prioridade

A equipe tem uma semana. Ela pode (a) comprar um dashboard sem dono designado para os alertas ou (b) executar um exercício cronometrado de restauração com o diretor de operações. Escolha a primeira ação e dê dois motivos. Indique uma condição sob a qual a outra ação poderia se tornar adequada mais tarde.

### EX005 — Estratégia em uma página

Complete o teste da estratégia em seis frases para a Northstar. Marque pelo menos duas afirmações como premissas ou como pendentes de aprovação do dono. Inclua um resultado com dono, data e evidência.

## Fontes deste capítulo

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — funções do framework e finalidade de gestão de riscos.
- [NIST CSF 2.0 Small Business Quick Start](https://www.nist.gov/itl/smallbusinesscyber/nist-cybersecurity-framework-0) — como iniciar um programa modesto no contexto da organização.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — risco de privacidade além dos eventos de segurança.
- [U.S. GAO, Critical Infrastructure Protection: TSA Is Taking Steps to Address Some Pipeline Security Program Weaknesses](https://www.gao.gov/products/gao-21-105263) — fatos públicos sobre o incidente da Colonial Pipeline em 2021.

> **Caso sintético.** Todos os detalhes do caso da Northstar Community Services são fictícios. A lição estratégica extraída do relatório do GAO está explicitamente identificada como inferência.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 04)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Escopo, permissão e prática segura

### Objetivos de aprendizagem

Você vai (1) definir por escrito o escopo de uma revisão de governança; (2) obter e registrar permissão antes de tocar em sistemas ou dados; (3) planejar a coleta de evidências e exercícios que não possam prejudicar serviços nem pessoas.

### 2.1 Por que o escopo vem primeiro

O capítulo 1 terminou com a Northstar Community Services rascunhando uma estratégia em torno do portal de agendamento e de um exercício cronometrado de restauração. Antes que alguém execute esse exercício ou colete evidências, o trabalho precisa de um escopo escrito. Um escopo declara quais serviços, sistemas, dados, locais e pessoas estão incluídos, quais estão excluídos e por quanto tempo o trabalho vai durar. Na Northstar, o primeiro escopo cobre o portal de agendamento, seu banco de dados de agendamento, o provedor de identidade e o serviço de backup. A gestão de casos e a escala de voluntários ficam de fora por enquanto, com uma nota de que serão revisadas no próximo trimestre. Um escopo claro evita duas falhas comuns: um trabalho que se expande silenciosamente para sistemas que ninguém aprovou e conclusões que afirmam mais do que as evidências cobrem.

### 2.2 Permissão e autoridade

Escopo não é o mesmo que permissão. O engenheiro de segurança pode saber ler logs de backup ou exportar contas, mas saber fazer não é autoridade para fazer. A permissão precisa vir da pessoa responsável por cada sistema ou conjunto de dados, e deve ser dada por escrito. Na Northstar, o diretor de operações é dono do serviço de agendamento e aprova a revisão; o responsável pela proteção de dados também precisa concordar, porque o banco de dados de agendamento guarda dados pessoais de clientes. A aprovação declara o que pode ser lido, o que pode ser alterado, quem pode fazê-lo e quando. Se mais tarde o engenheiro encontrar algo fora do escopo, como uma conta suspeita no sistema de gestão de casos, a conduta correta é comunicar o fato ao dono desse sistema, e não investigá-lo sozinho.

### 2.3 Tratar dados pessoais com segurança

O trabalho de governança muitas vezes toca dados pessoais mesmo quando sua finalidade não diz respeito a pessoas. Exportações de contas listam nomes de funcionários; testes de restauração copiam registros de consultas de clientes. A Northstar aplica os mesmos princípios que espera de todas as equipes: usar o mínimo de dados necessário, proteger o que for coletado e não guardar nada por mais tempo do que o preciso. O engenheiro pede exportações de contas apenas com os campos necessários à revisão, guarda as evidências em uma pasta restrita, mascara nomes de clientes nas capturas de tela e apaga as cópias temporárias depois do exercício. O NIST Privacy Framework trata o risco de privacidade como mais amplo do que os incidentes de segurança, o que lembra à equipe que um trabalho de revisão descuidado pode, ele próprio, causar dano à privacidade, mesmo sem nenhum atacante envolvido.

### 2.4 Desenhar um exercício seguro

O exercício de restauração do capítulo 1 não pode pôr em risco o portal em produção. A equipe escreve um plano curto: restaurar em um ambiente de teste isolado, nunca por cima da produção; usar o backup real mais recente, mas bloquear todo e-mail de saída para que os agendamentos de teste não cheguem aos clientes; marcar o exercício fora do horário de atendimento; nomear uma pessoa que possa interrompê-lo a qualquer momento; e definir antes de começar o que significa sucesso. O plano também lista o que pode dar errado, como restaurar por acidente por cima do banco de dados em produção, e o controle para cada risco, como credenciais separadas para o ambiente de teste. Pôr essas salvaguardas por escrito transforma um teste bem-intencionado em uma atividade governada, que o diretor de operações pode aprovar com confiança.

### 2.5 Registrar o que foi feito

A prática segura termina com um registro. Para cada atividade dentro do escopo, a Northstar registra a data, a pessoa, a referência da aprovação, o que foi acessado ou alterado e quais evidências foram guardadas. O registro tem três finalidades. Permite que outras pessoas repitam ou confiram o trabalho. Mostra que a equipe permaneceu dentro da permissão recebida. E dá ao diretor de operações uma base para decidir, porque as conclusões podem ser rastreadas até as evidências, e não até a memória de alguém. O registro não exige software especial; um log datado em uma pasta compartilhada restrita, revisado pelo diretor de operações no fim de cada mês, basta para uma organização do porte da Northstar.

### Exemplo resolvido

A Northstar escreve um escopo que cobre o portal de agendamento e suas dependências, obtém aprovação por escrito do diretor de operações e do responsável pela proteção de dados, planeja um exercício de restauração isolado com regra de interrupção e registra todas as atividades.

> **Caso sintético.** A Northstar Community Services e todos os seus detalhes continuam fictícios, dando sequência ao caso do capítulo 1.

### Erros e limites

Escopos podem ser estreitos demais para mostrar as dependências reais. Uma permissão por escrito não torna seguro um teste inseguro. O mascaramento pode falhar se as capturas de tela incluírem campos inesperados.

### Exercícios

- **EX006 — Conteúdo do escopo.** Liste os elementos que um escopo escrito deve declarar. *Rubrica:* 3 = serviços, sistemas, dados, locais, pessoas, exclusões e duração;; 2 = a maioria dos elementos;; 1 = vago;; 0 = nenhuma.
- **EX007 — Serviços excluídos.** Quais serviços da Northstar ficam fora do primeiro escopo? *Rubrica:* 3 = gestão de casos e escala de voluntários;; 2 = os dois;; 1 = vago;; 0 = nenhuma.
- **EX008 — Falhas de escopo.** Cite as duas falhas que um escopo claro evita. *Rubrica:* 3 = expansão não aprovada e conclusões exageradas;; 2 = as duas;; 1 = vago;; 0 = nenhuma.
- **EX009 — Escopo versus permissão.** Explique por que saber ler logs de backup não basta. *Rubrica:* 3 = a permissão precisa vir do dono responsável;; 2 = menciona autoridade;; 1 = vago;; 0 = nenhuma.
- **EX010 — Segundo aprovador.** Além do diretor de operações, quem precisa aprovar e por quê? *Rubrica:* 3 = o responsável pela proteção de dados, porque o banco guarda dados pessoais de clientes;; 2 = menciona privacidade;; 1 = vago;; 0 = nenhuma.
- **EX011 — Achado fora do escopo.** Nota-se uma conta suspeita na gestão de casos. O que o engenheiro deve fazer? *Rubrica:* 3 = comunicar ao dono, sem investigar sozinho;; 2 = comunicar;; 1 = investigar;; 0 = nenhuma.
- **EX012 — Exportações mínimas.** Como devem ser pedidas as exportações de contas? *Rubrica:* 3 = só com os campos necessários à revisão;; 2 = campos mínimos;; 1 = exportação completa;; 0 = nenhuma.
- **EX013 — Cuidado com capturas de tela.** Que precaução vale para capturas de tela de registros de clientes? *Rubrica:* 3 = mascarar nomes de clientes;; 2 = mascaramento;; 1 = vago;; 0 = nenhuma.
- **EX014 — Privacidade além de vazamentos.** O que o NIST Privacy Framework lembra à equipe sobre o trabalho de revisão? *Rubrica:* 3 = uma revisão descuidada pode, ela própria, causar dano à privacidade;; 2 = risco mais amplo;; 1 = vago;; 0 = nenhuma.
- **EX015 — Restauração isolada.** Onde o exercício de restauração deve ser executado? *Rubrica:* 3 = em ambiente de teste isolado, nunca por cima da produção;; 2 = ambiente de teste;; 1 = produção;; 0 = nenhuma.
- **EX016 — Bloqueio de e-mail.** Por que bloquear o e-mail de saída durante o exercício? *Rubrica:* 3 = para que agendamentos de teste não cheguem aos clientes;; 2 = proteção dos clientes;; 1 = vago;; 0 = nenhuma.
- **EX017 — Regra de interrupção.** Que papel o plano do exercício nomeia além do operador? *Rubrica:* 3 = uma pessoa que pode interrompê-lo a qualquer momento;; 2 = autoridade para interromper;; 1 = vago;; 0 = nenhuma.
- **EX018 — Separação de credenciais.** Que controle evita restaurar por engano por cima do banco em produção? *Rubrica:* 3 = credenciais separadas para o ambiente de teste;; 2 = credenciais separadas;; 1 = vago;; 0 = nenhuma.
- **EX019 — Finalidades do registro.** Declare as três finalidades do registro de atividades. *Rubrica:* 3 = repetibilidade, prova de permanência no escopo, base para decisões;; 2 = as três;; 1 = vago;; 0 = nenhuma.
- **EX020 — Revisão do registro.** Quem revisa o log de atividades e com que frequência? *Rubrica:* 3 = o diretor de operações, mensalmente;; 2 = mensalmente;; 1 = vago;; 0 = nenhuma.

### Síntese

Escopo por escrito, permissão explícita, manuseio cuidadoso dos dados, desenho seguro dos exercícios e um registro datado tornam o trabalho de governança confiável antes que qualquer achado seja feito.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 04)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Governança, riscos e compliance de segurança: sistemas, dados e dependências

### Objetivos de aprendizagem

Você vai (1) mapear os sistemas e os dados por trás de cada serviço prioritário; (2) encontrar dependências compartilhadas e componentes sem dono; (3) transformar o mapa em cenários de risco e pedidos de evidência.

### 3.1 De serviços a componentes

O capítulo 1 pediu à Northstar que nomeasse seus serviços antes de escolher produtos. O passo seguinte é listar do que cada serviço depende. O portal de agendamento precisa de um web host, do banco de dados de agendamento, do provedor de identidade que autentica a equipe e de um relay de e-mail que envia as confirmações. A gestão de casos precisa de seu próprio banco de dados, do provedor de identidade e de um armazenamento de arquivos para documentos. A escala de voluntários é uma planilha compartilhada que também usa o provedor de identidade e o relay de e-mail para lembretes. Escrever essas listas com os donos dos serviços é rápido e costuma surpreendê-los, porque poucas pessoas enxergam a cadeia inteira por trás de um serviço que usam todos os dias.

### 3.2 Como ler o mapa de dependências

O laboratório transforma as listas em um pequeno mapa. O provedor de identidade sustenta os três serviços, de modo que uma falha ou um comprometimento ali afetaria tudo de uma só vez. O relay de e-mail sustenta dois serviços, mas não tem dono. A planilha da escala também não tem dono. Todos os demais componentes têm. Esses dois fatos mudam as prioridades do capítulo 1. Um teste de restauração do banco de dados de agendamento continua valioso, mas, se a equipe não conseguir se autenticar, uma restauração perfeita não reabrirá o portal. Por isso o mapa acrescenta o provedor de identidade ao escopo do exercício de restauração e acrescenta a definição de donos para o relay de e-mail e para a escala à lista de decisões do diretor de operações.

### Laboratório — Mapa de dependências e donos da Northstar

```python
"""Northstar dependency map: which services each component supports, and unowned components."""
deps = {"appointment portal": ["web host", "scheduling database", "identity provider", "email relay"],
        "case management": ["case database", "identity provider", "file storage"],
        "volunteer roster": ["roster spreadsheet", "identity provider", "email relay"]}
owners = {"web host": "IT", "scheduling database": "IT", "identity provider": "IT", "case database": "Casework",
          "file storage": "IT", "email relay": None, "roster spreadsheet": None}
use = {}
for s, cs in deps.items():
    for c in cs: use.setdefault(c, []).append(s)
for c, ss in sorted(use.items(), key=lambda x: -len(x[1])):
    print(f"{c}: supports {len(ss)} service(s); owner {owners[c] or 'NONE'}")
print("shared by all three:", [c for c, ss in use.items() if len(ss) == 3])
```

Execute com `python3 lab_deps.py`. Saída verificada:

```text
identity provider: supports 3 service(s); owner IT
email relay: supports 2 service(s); owner NONE
web host: supports 1 service(s); owner IT
scheduling database: supports 1 service(s); owner IT
case database: supports 1 service(s); owner Casework
file storage: supports 1 service(s); owner IT
roster spreadsheet: supports 1 service(s); owner NONE
shared by all three: ['identity provider']
```

### 3.3 Os dados e para onde eles vão

Sistemas guardam dados, e dados criam obrigações. O banco de dados de agendamento da Northstar guarda nomes de clientes, dados de contato e motivos das consultas, alguns dos quais podem revelar problemas de saúde ou dificuldades financeiras. A gestão de casos guarda anotações detalhadas dos casos. A escala guarda os dados de contato dos voluntários. Para cada um, a equipe registra que dados existem, por que são mantidos, quem pode vê-los, para onde vão as cópias e por quanto tempo são retidos. Ela descobre que as confirmações de consulta enviadas pelo relay de e-mail incluem o motivo da consulta, o que é mais do que os clientes precisam receber por e-mail. Reduzir esse conteúdo é uma mudança barata que diminui o risco de privacidade sem afetar o serviço.

### 3.4 Dependências fora da organização

Vários componentes são operados por fornecedores: o web host, o provedor de identidade e o relay de e-mail. A Northstar não pode inspecionar o funcionamento interno deles, mas pode perguntar que garantias oferecem, ler seus termos sobre indisponibilidades e tratamento de dados e verificar se consegue exportar seus dados caso precise sair. O NIST CSF 2.0 situa a gestão de riscos da cadeia de suprimentos dentro da função Govern, o que corresponde à situação da Northstar: o conselho não precisa de detalhes técnicos, mas precisa saber quais serviços dependem de fornecedores e se alguém os verificou. A equipe registra cada fornecedor, o serviço que ele sustenta, as evidências disponíveis e a data da última revisão.

### 3.5 Do mapa aos cenários e às evidências

O mapa produz cenários mais precisos no formato do capítulo 1. Se o provedor de identidade ficar indisponível, a equipe não consegue acessar nenhum serviço, e a Northstar não testou uma forma alternativa de autenticação. Se o relay de e-mail sem dono estiver mal configurado, confirmações de consulta podem chegar às pessoas erradas, e ninguém revisa suas configurações. Se a planilha da escala estiver compartilhada de forma ampla demais, os dados de contato dos voluntários podem ficar expostos, e o acesso nunca foi revisado. Cada cenário nomeia um pedido de evidência: o histórico de status e as opções de contingência do provedor de identidade, a configuração do relay e a lista de compartilhamento da escala. Pedidos de evidência mantêm a estratégia honesta, porque mostram quais crenças foram verificadas e quais ainda são premissas.

### Exemplo resolvido

A Northstar lista os componentes por trás de três serviços, descobre que o provedor de identidade é compartilhado pelos três e que há dois componentes sem dono, retira os motivos das consultas dos e-mails e escreve três cenários sustentados por evidências.

> **Caso sintético.** Todos os sistemas, fornecedores e dados da Northstar são fictícios; o NIST CSF 2.0 e o NIST Privacy Framework são reais.

### Erros e limites

Mapas omitem ferramentas informais usadas pela equipe. As garantias dos fornecedores variam de escopo. Um componente compartilhado pode ter redundância oculta que o mapa não mostra.

### Exercícios

- **EX021 — Cadeia do portal.** Liste os quatro componentes por trás do portal de agendamento. *Rubrica:* 3 = web host, banco de dados de agendamento, provedor de identidade, relay de e-mail;; 2 = os quatro;; 1 = vago;; 0 = nenhuma.
- **EX022 — Dependência universal.** Que componente sustenta os três serviços? *Rubrica:* 3 = o provedor de identidade;; 2 = identidade;; 1 = relay de e-mail;; 0 = nenhuma.
- **EX023 — Componentes sem dono.** Quais dois componentes não têm dono no laboratório? *Rubrica:* 3 = o relay de e-mail e a planilha da escala;; 2 = os dois;; 1 = vago;; 0 = nenhuma.
- **EX024 — Mudança no escopo da restauração.** Por que o mapa acrescenta o provedor de identidade ao exercício de restauração? *Rubrica:* 3 = sem autenticação, um portal restaurado continua sem reabrir;; 2 = autenticação;; 1 = vago;; 0 = nenhuma.
- **EX025 — Lista de decisões.** O que o mapa acrescentou à lista de decisões do diretor de operações? *Rubrica:* 3 = donos para o relay de e-mail e para a escala;; 2 = responsabilidade;; 1 = vago;; 0 = nenhuma.
- **EX026 — Dado sensível da consulta.** Por que o motivo da consulta é sensível? *Rubrica:* 3 = pode revelar problemas de saúde ou dificuldade financeira;; 2 = sensibilidade;; 1 = vago;; 0 = nenhuma.
- **EX027 — Ajuste no conteúdo do e-mail.** Que mudança barata reduz o risco de privacidade nas confirmações? *Rubrica:* 3 = retirar o motivo da consulta dos e-mails;; 2 = minimizar;; 1 = vago;; 0 = nenhuma.
- **EX028 — Campos do registro de dados.** Que fatos são registrados para cada conjunto de dados? *Rubrica:* 3 = o quê, por quê, quem vê, para onde vão as cópias, retenção;; 2 = os cinco;; 1 = vago;; 0 = nenhuma.
- **EX029 — Perguntas a fornecedores.** O que a Northstar pode verificar sobre fornecedores sem inspecionar seu funcionamento interno? *Rubrica:* 3 = garantias oferecidas, termos de indisponibilidade e de dados, capacidade de exportação;; 2 = os três;; 1 = vago;; 0 = nenhuma.
- **EX030 — Posição no CSF.** Onde o NIST CSF 2.0 situa a gestão de riscos da cadeia de suprimentos? *Rubrica:* 3 = na função Govern;; 2 = Govern;; 1 = Protect;; 0 = nenhuma.
- **EX031 — Registro de fornecedores.** O que a equipe registra para cada fornecedor? *Rubrica:* 3 = serviço sustentado, evidências disponíveis, data da última revisão;; 2 = registro;; 1 = vago;; 0 = nenhuma.
- **EX032 — Cenário de identidade.** Escreva a lacuna de evidência do cenário do provedor de identidade. *Rubrica:* 3 = nenhuma autenticação alternativa testada;; 2 = contingência não testada;; 1 = vago;; 0 = nenhuma.
- **EX033 — Cenário do relay.** Que consequência decorre de um relay de e-mail mal configurado? *Rubrica:* 3 = confirmações podem chegar às pessoas erradas;; 2 = desvio;; 1 = vago;; 0 = nenhuma.
- **EX034 — Evidência da escala.** Que evidência é pedida para o cenário da escala? *Rubrica:* 3 = sua lista de compartilhamento;; 2 = lista de compartilhamento;; 1 = vago;; 0 = nenhuma.
- **EX035 — Estratégia honesta.** Como os pedidos de evidência mantêm a estratégia honesta? *Rubrica:* 3 = mostram quais crenças foram verificadas e quais são premissas;; 2 = evidência;; 1 = vago;; 0 = nenhuma.

### Síntese

Um mapa de dependências transforma serviços nomeados em componentes compartilhados, donos, obrigações sobre dados, verificações de fornecedores e cenários apoiados em evidências.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 04)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Governança, riscos e compliance de segurança: laboratório guiado e síntese aplicada

### Objetivos de aprendizagem

Você vai (1) executar e cronometrar um exercício de restauração com segurança; (2) comparar o resultado com a meta do serviço e encontrar o atraso crítico; (3) escrever um registro de decisão curto e uma estratégia de uma página atualizada.

### 4.1 Executar o exercício

Com o escopo, a permissão e o mapa de dependências estabelecidos, a Northstar executa o exercício cronometrado de restauração prometido no capítulo 1. Segue-se o plano do capítulo 2: um ambiente de teste isolado, o e-mail de saída bloqueado, uma pessoa nomeada capaz de interromper o exercício e o sucesso definido de antemão como a equipe da recepção conseguindo fazer agendamentos de teste no portal restaurado. O engenheiro de segurança registra cada etapa com horário de início e de término. O diretor de operações acompanha o início e o fim, porque o resultado vai testar o limite de interrupção de quatro horas, que ainda era uma premissa de trabalho. Ninguém toca no portal em produção durante o exercício.

### 4.2 Como ler os tempos

O laboratório soma as etapas registradas. Declarar o exercício e isolar a cópia de teste levou quinze minutos. Localizar o backup e as credenciais levou cinquenta e cinco. Restaurar o banco de dados de agendamento levou setenta. Reconstruir a configuração do web host levou sessenta. Reconectar o provedor de identidade levou vinte e cinco, e os agendamentos de teste da recepção levaram vinte. O total foi de duzentos e quarenta e cinco minutos, cinco minutos acima da meta de duzentos e quarenta. A restauração do banco de dados foi a etapa mais longa, mas a mais surpreendente foram os cinquenta e cinco minutos gastos para encontrar o backup e as credenciais, o que é uma lacuna de governança, e não um limite técnico.

### Laboratório — Cronometrando o exercício de restauração da Northstar

```python
"""Timed restore exercise for the Northstar appointment portal against a four-hour target."""
steps = [("declare exercise and isolate test copy", 15), ("locate backup and credentials", 55),
         ("restore scheduling database", 70), ("rebuild web host configuration", 60),
         ("reconnect identity provider", 25), ("front-desk test bookings", 20)]
t = 0
for s, m in steps:
    t += m; print(f"{s}: {m} min (cumulative {t} min)")
print(f"total {t} min = {t/60:.2f} h; target 240 min; {'MET' if t <= 240 else 'MISSED by ' + str(t-240) + ' min'}")
slow = max(steps, key=lambda x: x[1]); print(f"longest step: {slow[0]} ({slow[1]} min)")
```

Execute com `python3 lab_restore.py`. Saída verificada:

```text
declare exercise and isolate test copy: 15 min (cumulative 15 min)
locate backup and credentials: 55 min (cumulative 70 min)
restore scheduling database: 70 min (cumulative 140 min)
rebuild web host configuration: 60 min (cumulative 200 min)
reconnect identity provider: 25 min (cumulative 225 min)
front-desk test bookings: 20 min (cumulative 245 min)
total 245 min = 4.08 h; target 240 min; MISSED by 5 min
longest step: restore scheduling database (70 min)
```

### 4.3 O que o resultado significa

Perder a meta por cinco minutos não significa que a estratégia falhou; significa que agora uma evidência substitui uma premissa. Três melhorias ficam claras. Manter as instruções de restauração e o acesso às credenciais do backup em um local conhecido e protegido poderia poupar a maior parte dos cinquenta e cinco minutos. Documentar a configuração do web host como um script poderia encurtar a reconstrução. Incluir a reconexão do provedor de identidade no procedimento escrito elimina adivinhações. A equipe também anota os limites: um único exercício, em condições tranquilas, com pessoas que sabiam que ele ia acontecer. Um evento real à noite, possivelmente com atacantes ainda presentes, seria mais lento. Por isso o limite de quatro horas só deve ser confirmado depois de um segundo exercício.

### 4.4 Registrar a decisão

A Northstar escreve um registro de decisão curto para o diretor de operações. Ele declara a decisão necessária, as evidências, as opções e a recomendação. A decisão é se o portal de agendamento terá um limite de interrupção aceito de quatro horas. A evidência é o log do exercício. As opções são aceitar o limite agora, aceitá-lo depois das melhorias e de um segundo teste, ou elevar o limite para seis horas e manter pessoal para um processo manual de agendamento. A recomendação é a segunda opção, com as melhorias previstas para dentro de trinta dias e um segundo exercício já marcado. O diretor de operações a aprova, e o registro é arquivado junto com as evidências, para que o raciocínio possa ser conferido depois.

### 4.5 Atualizar a estratégia de uma página

O capítulo termina atualizando o teste da estratégia em seis frases do capítulo 1. O serviço prioritário continua sendo o agendamento de consultas para clientes e para a equipe da recepção. O limite de impacto agora é uma proposta baseada em evidências, e não um palpite. Os cenários principais incluem a falha do provedor de identidade, revelada pelo mapa de dependências. Os resultados do trimestre são as três melhorias da restauração, um segundo exercício cronometrado, donos para o relay de e-mail e para a escala e a retirada dos motivos das consultas dos e-mails. O diretor de operações é dono dos tradeoffs. Os sinais a revisar mensalmente são tempo de restauração, falhas de backup, mudanças privilegiadas e ações atrasadas dos donos. A estratégia é mais curta do que muitos planos de segurança, mas agora cada linha está ligada a uma evidência ou a uma premissa aprovada.

### Exemplo resolvido

A Northstar executa uma restauração cronometrada e segura que leva 245 minutos diante de uma meta de 240, identifica um atraso de governança de 55 minutos, registra uma decisão aprovada de melhorar e testar de novo e atualiza sua estratégia de uma página.

> **Caso sintético.** O exercício e os tempos são fictícios e usam dados sintéticos em um ambiente isolado.

### Erros e limites

Um único exercício tranquilo e anunciado superestima a prontidão real. Os tempos dependem de quem está disponível. Perder a meta por poucos minutos pode tentar as equipes a ajustar a meta em vez do processo.

### Exercícios

- **EX036 — Definição de sucesso.** Como o sucesso foi definido antes do exercício? *Rubrica:* 3 = equipe da recepção fazendo agendamentos de teste no portal restaurado;; 2 = agendamentos;; 1 = vago;; 0 = nenhuma.
- **EX037 — Presença do diretor.** Por que o diretor de operações acompanhou o início e o fim? *Rubrica:* 3 = o resultado testa a premissa de quatro horas de que o diretor é dono;; 2 = responsabilidade;; 1 = vago;; 0 = nenhuma.
- **EX038 — Tempo total.** Quanto tempo o exercício levou no total? *Rubrica:* 3 = 245 minutos;; 2 = 4,08 horas;; 1 = 240;; 0 = nenhuma.
- **EX039 — Diferença em relação à meta.** Por quanto o exercício perdeu a meta? *Rubrica:* 3 = cinco minutos;; 2 = 5;; 1 = vago;; 0 = nenhuma.
- **EX040 — Etapa mais longa.** Qual etapa levou mais tempo? *Rubrica:* 3 = restaurar o banco de dados de agendamento, 70 minutos;; 2 = banco de dados;; 1 = vago;; 0 = nenhuma.
- **EX041 — Atraso de governança.** Que atraso foi uma lacuna de governança, e não um limite técnico? *Rubrica:* 3 = 55 minutos para localizar backup e credenciais;; 2 = localização;; 1 = vago;; 0 = nenhuma.
- **EX042 — Três melhorias.** Cite as três melhorias identificadas. *Rubrica:* 3 = local conhecido e protegido para instruções e credenciais, configuração do web host em script, etapa de identidade no procedimento;; 2 = as três;; 1 = vago;; 0 = nenhuma.
- **EX043 — Condições tranquilas.** Por que um evento real poderia ser mais lento que o exercício? *Rubrica:* 3 = pode ocorrer à noite, sem aviso e com atacantes presentes;; 2 = condições;; 1 = vago;; 0 = nenhuma.
- **EX044 — Segundo exercício.** Quando o limite de quatro horas deve ser confirmado? *Rubrica:* 3 = depois de um segundo exercício, após as melhorias;; 2 = novo teste;; 1 = agora;; 0 = nenhuma.
- **EX045 — Opções da decisão.** Que três opções o registro de decisão ofereceu? *Rubrica:* 3 = aceitar agora, aceitar após melhorias e novo teste, elevar para seis horas com agendamento manual;; 2 = as três;; 1 = vago;; 0 = nenhuma.
- **EX046 — Opção recomendada.** Que opção foi recomendada e aprovada? *Rubrica:* 3 = aceitar após melhorias em trinta dias e um segundo teste;; 2 = segunda opção;; 1 = vago;; 0 = nenhuma.
- **EX047 — Arquivamento do registro.** Por que o registro de decisão é arquivado junto com as evidências? *Rubrica:* 3 = para que o raciocínio possa ser conferido depois;; 2 = rastreabilidade;; 1 = vago;; 0 = nenhuma.
- **EX048 — Novo cenário.** Que cenário entrou na estratégia a partir do mapa de dependências? *Rubrica:* 3 = falha do provedor de identidade;; 2 = identidade;; 1 = vago;; 0 = nenhuma.
- **EX049 — Sinais mensais.** Liste os sinais revisados mensalmente. *Rubrica:* 3 = tempo de restauração, falhas de backup, mudanças privilegiadas, ações atrasadas dos donos;; 2 = os quatro;; 1 = vago;; 0 = nenhuma.
- **EX050 — Ajustar metas.** Que tentação a equipe deve evitar depois de perder a meta por minutos? *Rubrica:* 3 = mudar a meta em vez do processo;; 2 = resistir;; 1 = vago;; 0 = nenhuma.

### Síntese

Um exercício seguro e cronometrado transforma um limite de serviço presumido em evidência, em uma decisão registrada e em uma estratégia de uma página mais precisa para o próximo trimestre.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 04)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- cyberabc:chapter-navigation:end -->

## Fontes dos capítulos 2–4

- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29> — gestão de riscos da cadeia de suprimentos dentro de Govern (capítulo 3).
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10> — risco de privacidade no trabalho de revisão e nos fluxos de dados (capítulos 2–3).

Todos os detalhes da Northstar nos capítulos 2–4 continuam fictícios; os laboratórios usam apenas a biblioteca padrão do Python sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais.

<a id="worked-results"></a>

## Apêndice final — resoluções e notas de avaliação

As resoluções de todos os capítulos estão reunidas aqui: EX001–EX005 (capítulo 1), como escritas originalmente, seguidas de EX006–EX050 (capítulos 2–4). A Northstar Community Services, seus sistemas, fornecedores, dados e tempos são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

### EX001 — Resolução

**EX001.** (a) e (c) são atividades. (b) e (d) são resultados mensuráveis ou metas operacionais, desde que seu escopo e seus donos estejam definidos. Uma reescrita mais forte de (a) é: “Até o fim do primeiro mês, todos os notebooks gerenciados da equipe produzem eventos de saúde do endpoint e de ameaças visíveis para o responsável designado pela resposta, e um alerta de amostra chega a esse responsável em até quinze minutos.” Essa versão declara uma população, um prazo, uma evidência e um revisor. Uma ferramenta específica pode ser escolhida depois.

### EX002 — Resolução

**EX002.** “Se uma conta desatualizada de voluntário puder acessar a escala depois que o voluntário sair, dados pessoais de contato podem ser expostos, e a Northstar não concluiu uma revisão de acessos neste trimestre.” A condição é o acesso remanescente; o serviço é a escala de voluntários; a consequência é a exposição de dados de contato; a lacuna de evidência é a revisão que falta. A premissa é que voluntários desligados ainda mantêm acesso, o que precisa ser testado em vez de afirmado como fato.

### EX003 — Resolução

**EX003.** Solicite um inventário recente de backups do banco de dados de agendamento, um log de teste de restauração com carimbos de tempo e critérios de sucesso, e um mapa de dependências mostrando se identidade, rede e configuração da aplicação também podem ser restauradas. Uma captura de tela pode mostrar que um job de backup está configurado. Ela não pode mostrar que existe uma cópia utilizável, que todas as dependências estão incluídas ou que o serviço volta em até quatro horas.

### EX004 — Resolução

**EX004.** Execute primeiro o exercício cronometrado de restauração. Ele testa diretamente o resultado do serviço prioritário e produz evidências sobre a maior incógnita. Também identifica dependências que podem orientar gastos futuros. Um dashboard passa a ser adequado quando as fontes de monitoramento, as definições de alerta, a responsabilidade pela revisão e os caminhos de ação estão definidos; aí a compra pode sustentar uma meta de detecção mensurável.

### EX005 — Resolução

**EX005.** Um rascunho aceitável é: “Precisamos manter o agendamento de consultas recuperável para clientes e para a equipe da recepção. Pede-se ao diretor de operações que confirme um limite de interrupção de quatro horas; por ora, é uma premissa. Nosso cenário principal é a perda do portal e do banco de dados após o comprometimento de uma conta, pendente de revisão de acessos e de dependências. Em até trinta dias, o engenheiro de segurança e o diretor de operações executarão um teste de restauração de ponta a ponta e guardarão os carimbos de tempo e um resultado assinado. O diretor de operações é dono do tradeoff do serviço, e o engenheiro é dono do exercício. Eles revisarão as falhas de backup diariamente e a estratégia mensalmente, atualizando-a após o teste de restauração.” A resposta recebe crédito pela aprovação explícita do dono, pela evidência mensurável e pela incerteza declarada com honestidade, não por usar exatamente estas palavras.

### EX006–EX050 — Resoluções

**EX006.** Os serviços, sistemas, dados, locais e pessoas incluídos, o que fica excluído e quanto tempo o trabalho dura.

**EX007.** A gestão de casos e a escala de voluntários, que serão revisadas no próximo trimestre.

**EX008.** Um trabalho que se expande silenciosamente para sistemas não aprovados e conclusões que afirmam mais do que as evidências cobrem.

**EX009.** Porque habilidade não é autoridade; a permissão precisa vir por escrito da pessoa responsável pelo sistema ou pelos dados.

**EX010.** O responsável pela proteção de dados, porque o banco de dados de agendamento guarda dados pessoais de clientes.

**EX011.** Comunicar o fato ao dono do sistema de gestão de casos, em vez de investigar fora do escopo.

**EX012.** Apenas com os campos necessários à revisão.

**EX013.** Os nomes de clientes são mascarados nas capturas de tela guardadas como evidência.

**EX014.** Que o risco de privacidade é mais amplo do que os incidentes de segurança, de modo que um trabalho de revisão descuidado pode, ele próprio, causar dano.

**EX015.** Em um ambiente de teste isolado, nunca por cima do banco de dados em produção.

**EX016.** Para que os agendamentos de teste não enviem mensagens a clientes reais.

**EX017.** Uma pessoa com autoridade para interromper o exercício a qualquer momento.

**EX018.** O uso de credenciais separadas para o ambiente de teste.

**EX019.** Permite que outras pessoas repitam ou confiram o trabalho, mostra que a equipe ficou dentro da permissão e dá ao dono da decisão evidências rastreáveis.

**EX020.** O diretor de operações o revisa no fim de cada mês.

**EX021.** O web host, o banco de dados de agendamento, o provedor de identidade e o relay de e-mail.

**EX022.** O provedor de identidade.

**EX023.** O relay de e-mail e a planilha da escala.

**EX024.** Porque, se a equipe não conseguir se autenticar, restaurar apenas o banco de dados não reabrirá o portal.

**EX025.** A designação de donos para o relay de e-mail e para a planilha da escala.

**EX026.** Porque pode revelar problemas de saúde ou dificuldades financeiras.

**EX027.** Retirar o motivo da consulta dos e-mails de confirmação.

**EX028.** Que dados existem, por que são mantidos, quem pode vê-los, para onde vão as cópias e por quanto tempo são mantidos.

**EX029.** Que garantias oferecem, seus termos sobre indisponibilidades e tratamento de dados e se os dados podem ser exportados.

**EX030.** Dentro da função Govern.

**EX031.** O fornecedor, o serviço que ele sustenta, as evidências disponíveis e a data da última revisão.

**EX032.** A Northstar não testou uma autenticação alternativa para o caso de o provedor de identidade ficar indisponível.

**EX033.** Confirmações de consulta poderiam chegar às pessoas erradas.

**EX034.** A lista de compartilhamento atual da planilha da escala.

**EX035.** Mostram quais crenças foram verificadas e quais continuam sendo premissas.

**EX036.** A equipe da recepção fazendo agendamentos de teste no portal restaurado.

**EX037.** Porque o resultado testaria o limite de interrupção de quatro horas de que o diretor de operações é dono.

**EX038.** 245 minutos, cerca de 4,08 horas.

**EX039.** Por cinco minutos.

**EX040.** Restaurar o banco de dados de agendamento, com 70 minutos.

**EX041.** Os 55 minutos gastos para localizar o backup e as credenciais.

**EX042.** Um local conhecido e protegido para as instruções de restauração e as credenciais, a configuração do web host em script e a inclusão da reconexão de identidade no procedimento.

**EX043.** Porque um evento real pode acontecer à noite, sem aviso e com atacantes possivelmente ainda presentes.

**EX044.** Somente depois das melhorias e de um segundo exercício.

**EX045.** Aceitar agora; aceitar depois das melhorias e de um segundo teste; ou elevar o limite para seis horas com um processo manual de agendamento.

**EX046.** Aceitar o limite depois das melhorias previstas para dentro de trinta dias e de um segundo exercício.

**EX047.** Para que o raciocínio possa ser conferido depois, à luz das evidências.

**EX048.** A falha do provedor de identidade.

**EX049.** Tempo de restauração, falhas de backup, mudanças privilegiadas e ações atrasadas dos donos.

**EX050.** Ajustar a meta em vez de melhorar o processo.
