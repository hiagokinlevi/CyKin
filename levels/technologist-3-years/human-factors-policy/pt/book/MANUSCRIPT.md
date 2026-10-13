# Fatores Humanos e Política Cibernética: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 075, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–10 de 30 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 3 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 11–30 (EX031–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de tecnólogo que constroem, configuram e operam controles de segurança centrados nas pessoas e serviços de reporte em organizações pequenas.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios totalizam reportes, contam avisos, calculam medianas, ordenam cenários, comparam tempos de tarefa e proporções por clínica, conferem logs de automação e sinalizam cadastros de fornecedores, sempre sobre dados sintéticos; nenhum funcionário, paciente, e-mail ou conta real está envolvido. Os testes de usabilidade usam caixas postais de teste com voluntários que sabem que estão testando ferramentas; os procedimentos de verificação são praticados em dramatizações anunciadas, nunca por engano secreto. Toda simulação de phishing mencionada é anunciada, acordada com os funcionários e relatada apenas de forma agregada. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos 1–9 constroem os fundamentos técnicos por meio de um único estágio num grupo odontológico; os capítulos 10–23 desenvolvem o trabalho de fatores humanos, da orientação à avaliação, com um laboratório guiado; os capítulos 24–30 cobrem pesquisa aplicada, o ateliê em equipe, a passagem operacional, a implantação, a prática de campo e o projeto final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Lucas Ferreira** | Estudante de tecnólogo | Inventado |
| **Marta Kowalczyk** | Professora | Inventada |
| **Northgate Institute of Technology** | Instituto fictício | Inventado |
| **Brightwell Dental Group** | Grupo odontológico fictício, 14 clínicas, 210 funcionários | Inventado |

### Fontes principais

Adams e Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806); Sasse, Brostoff e Weirich (2001), [doi:10.1023/A:1011902718709](https://doi.org/10.1023/A:1011902718709); Hansche et al. (2024), NIST SP 800-50r1; Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Herley (2009), [doi:10.1145/1719030.1719050](https://doi.org/10.1145/1719030.1719050). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |

Capítulos 11–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-11), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever os sistemas computacionais usados num pequeno negócio de saúde; (2) identificar onde os funcionários interagem com a segurança; (3) observar como a carga de trabalho molda o comportamento.

### 1.1 Sistemas das clínicas

Lucas Ferreira, estudante de tecnólogo do fictício Northgate Institute of Technology, começa um estágio no fictício Brightwell Dental Group, com catorze clínicas e 210 funcionários. Cada clínica tem computadores na recepção, um sistema de gestão do consultório que guarda os prontuários dos pacientes, computadores de imagem e uma impressora compartilhada. Sua professora, Marta Kowalczyk, pede a ele que liste cada sistema e quem o usa. Lucas descobre que as recepcionistas usam quatro sistemas durante um único agendamento, alternando rapidamente entre telas enquanto falam com os pacientes ao telefone ou no balcão.

### 1.2 Pontos de contato com a segurança

Lucas marca cada ponto em que os funcionários encontram a segurança: fazer login no início do turno, bloquear a tela, digitar senhas no sistema de imagem, abrir e-mails de fornecedores e pacientes e lidar com dados de pagamento. As recepcionistas fazem login e logout muitas vezes por dia. Adams e Sasse (1999) mostraram que, quando os mecanismos de segurança conflitam com o trabalho, os usuários encontram atalhos. Lucas vê post-its com senhas em duas clínicas e os entende não como descuido, mas como resposta a senhas demais e a pouco tempo entre um paciente e outro.

### 1.3 Carga de trabalho e comportamento

Numa manhã movimentada, uma recepcionista atende ligações, faz check-ins e recebe pagamentos com uma fila de pacientes esperando. Lucas observa que as tarefas de segurança competem com o atendimento aos pacientes pela atenção. Um bloqueio de tela que exige uma senha longa a cada dois minutos é inviável ali. Ele registra suas observações num relatório curto: o número de sistemas, os logins por turno e os principais pontos de pressão. Essa linha de base orientará as escolhas de design posteriores, porque qualquer controle precisa se ajustar à realidade de uma recepção de clínica para ser usado de forma consistente.

### Exemplo resolvido

Lucas lista os sistemas das clínicas, mapeia os pontos de contato com a segurança, explica as senhas em post-its como um atalho e registra os pontos de pressão da carga de trabalho.

> **Caso sintético.** O Brightwell Dental Group é sintético; Adams e Sasse (1999) é real.

### Erros e limites

Uma manhã pode não ser típica. As observações devem respeitar a privacidade dos pacientes.

### Exercícios

- **EX001 — Sistemas por agendamento.** Quantos sistemas as recepcionistas usam num agendamento? *Rubrica:* 3 = quatro;; 2 = 4;; 1 = um;; 0 = nenhuma.
- **EX002 — Post-its.** Como Lucas interpreta as senhas em post-its? *Rubrica:* 3 = um atalho diante de senhas demais e pouco tempo;; 2 = atalho;; 1 = descuido;; 0 = nenhuma.
- **EX003 — Demanda concorrente.** Com o que as tarefas de segurança competem na recepção? *Rubrica:* 3 = o atendimento aos pacientes;; 2 = pacientes;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Redes e serviços de internet

### Objetivos de aprendizagem

Você vai (1) explicar como as clínicas se conectam ao e-mail, ao agendamento e aos serviços em nuvem; (2) descrever como os atacantes exploram os serviços de internet para enganar os funcionários; (3) identificar pistas técnicas simples que ajudam os funcionários.

### 2.1 Conexões das clínicas

Cada clínica da Brightwell se conecta à internet por um roteador e usa e-mail em nuvem, um serviço de agendamento online e o sistema de gestão do consultório hospedado por um fornecedor. Lucas desenha um diagrama de rede simples. Ele aprende que os funcionários veem esses serviços principalmente pelo navegador e pelo e-mail. Os pacientes agendam online e recebem lembretes por SMS e e-mail. Como grande parte da comunicação é online, mensagens que imitam esses serviços, como falsas notificações de agendamento ou e-mails de suporte do fornecedor, chegam facilmente a funcionários e pacientes.

### 2.2 Explorar os serviços

Os atacantes enviam e-mails que parecem mensagens do serviço de agendamento pedindo aos funcionários que façam login para resolver um problema, levando a uma página de login falsa. Também registram domínios parecidos com o da Brightwell para enviar mensagens que parecem internas. Lucas aprende que a autenticação de e-mail ajuda a rejeitar mensagens forjadas do próprio domínio da Brightwell, mas que domínios parecidos passam nessas verificações. Ele observa que, por isso, os funcionários não podem confiar apenas na tecnologia, e que são necessárias pistas visuais e um reporte fácil para pegar o que passa.

### 2.3 Pistas úteis

Lucas sugere três pistas. Primeiro, uma etiqueta de e-mail externo nas mensagens de fora da Brightwell. Segundo, um alerta quando um remetente externo usa um nome de exibição igual ao de um funcionário. Terceiro, favoritos para as páginas oficiais de login dos serviços, para que os funcionários nunca precisem seguir links de e-mail para fazer login. Ele testa a ideia dos favoritos com duas recepcionistas, que a acham mais rápida do que procurar nos e-mails. Pistas que economizam tempo têm mais chance de ser adotadas do que pistas que acrescentam etapas. A gerente do consultório aprova as três pistas para um teste.

### Exemplo resolvido

Lucas mapeia as conexões das clínicas, explica domínios parecidos e páginas de login falsas e sugere etiquetas externas, alertas de nome e favoritos.

> **Caso sintético.** A rede é sintética.

### Erros e limites

As etiquetas perdem efeito se usadas em excesso. Os favoritos precisam de manutenção.

### Exercícios

- **EX004 — Limite dos domínios parecidos.** Por que domínios parecidos passam nas verificações de autenticação? *Rubrica:* 3 = são domínios legítimos de propriedade dos atacantes;; 2 = domínio próprio;; 1 = nada;; 0 = nenhuma.
- **EX005 — Benefício dos favoritos.** Por que os favoritos ajudam? *Rubrica:* 3 = os funcionários nunca seguem links de e-mail para fazer login;; 2 = evitar links;; 1 = nada;; 0 = nenhuma.
- **EX006 — Fator de adoção.** Que pistas têm mais chance de ser adotadas? *Rubrica:* 3 = as que economizam tempo;; 2 = tempo;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Fundamentos de programação

### Objetivos de aprendizagem

Você vai (1) escrever um script em Python para resumir e-mails reportados; (2) usar funções e laços; (3) tratar os dados com segurança.

### 3.1 Um resumo dos reportes

O prestador de TI da Brightwell encaminha os e-mails reportados para uma caixa postal compartilhada e exporta uma lista semanal com data, clínica e categoria do assunto. Lucas escreve um script em Python que lê a lista e conta os reportes por clínica e por categoria. Ele usa um laço para percorrer cada linha e um dicionário para guardar as contagens. O script imprime um resumo curto para a reunião semanal de TI, substituindo uma contagem manual que levava meia hora e muitas vezes tinha erros. O prestador o lê toda segunda-feira.

### Laboratório — Reportes semanais por clínica e categoria

```python
# Weekly reports by clinic and category (synthetic export).
rows = [("Harbour", "fake invoice")] * 4 + [("Harbour", "fake login")] * 2 + [("Elm Road", "fake invoice")] * 3 + \
       [("Elm Road", "other")] * 2 + [("Station", "fake login")] * 3 + [("Station", "fake invoice")] * 2 + [("Mill", "other")] * 1
def count(rows, i):
    c = {}
    for r in rows: c[r[i]] = c.get(r[i], 0) + 1
    return dict(sorted(c.items(), key=lambda x: -x[1]))
print("by clinic:", count(rows, 0)); print("by category:", count(rows, 1))
```

Execute com `python3 lab_tally.py`. Saída verificada:

```text
by clinic: {'Harbour': 6, 'Elm Road': 5, 'Station': 5, 'Mill': 1}
by category: {'fake invoice': 9, 'fake login': 5, 'other': 3}
```

### 3.2 Funções e laços

Lucas organiza o script em funções: uma lê os dados, uma conta por um campo escolhido e uma imprime uma tabela. Usar uma única função de contagem para clínicas e categorias evita repetir código. Ele testa cada função numa pequena amostra que consegue conferir à mão. Aprende que nomes de função claros ajudam os outros a entender seu código, o que importa porque o prestador de TI vai executá-lo quando Lucas não estiver lá. Ele também acrescenta comentários curtos no início de cada função, descrevendo a entrada, a saída e as premissas que ela faz sobre os dados.

### 3.3 Tratamento seguro dos dados

A exportação contém os assuntos dos e-mails, que às vezes incluem nomes de pacientes. Lucas muda a exportação para incluir apenas uma categoria escolhida por quem revisa, e não o assunto completo, de modo que o script nunca lida com informações de pacientes. Ele guarda o arquivo numa pasta restrita e apaga as exportações antigas depois que o resumo é feito. Tratar os dados com segurança faz parte de programar com responsabilidade, sobretudo na saúde, onde a confidencialidade dos pacientes é um dever legal e ético. A gerente do consultório confirma a mudança com o encarregado de proteção de dados antes da próxima exportação.

### Exemplo resolvido

Lucas escreve uma contagem testada em Python com funções, remove os nomes de pacientes da exportação e restringe o armazenamento.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

As categorias dependem de quem revisa. Scripts precisam de manutenção.

### Exercícios

- **EX007 — Problema da contagem manual.** Que problema o script substituiu? *Rubrica:* 3 = uma contagem manual lenta e sujeita a erros;; 2 = manual;; 1 = nada;; 0 = nenhuma.
- **EX008 — Categoria principal.** Que categoria foi a mais comum no laboratório? *Rubrica:* 3 = fake invoice (fatura falsa), com 9;; 2 = faturas;; 1 = nada;; 0 = nenhuma.
- **EX009 — Remoção do assunto.** Por que remover os assuntos dos e-mails da exportação? *Rubrica:* 3 = podem conter nomes de pacientes;; 2 = privacidade;; 1 = nada;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Modelos de dados

### Objetivos de aprendizagem

Você vai (1) desenhar um modelo de dados simples para reportes e vereditos; (2) definir campos e valores permitidos; (3) evitar guardar dados pessoais desnecessários.

### 4.1 Modelar os reportes

Lucas desenha um modelo de dados para os reportes da Brightwell. Cada reporte tem um identificador, a data e a hora de recebimento, a clínica, uma categoria, um veredito e a hora em que o veredito foi enviado. Ele liga os reportes sobre o mesmo e-mail usando um identificador de agrupamento, de modo que vinte reportes de um mesmo e-mail de phishing contam como um incidente com vinte pessoas que reportaram. Esse modelo permite à TI responder a perguntas úteis, como quão rápido chegou o primeiro reporte e quão rápido foi enviado um veredito. O prestador revisa o modelo e o aprova.

### 4.2 Campos e valores

Para cada campo, Lucas define os valores permitidos. O veredito pode ser malicioso, inofensivo, spam ou desconhecido. A categoria tem uma lista curta, como fatura falsa, login falso e outros. Os horários usam um único formato, com fuso horário. Valores fixos evitam variações de grafia que dividiriam as contagens. Ele escreve as definições numa tabela e a compartilha com o prestador de TI, para que todos registrem os dados da mesma forma e as análises possam ser comparadas entre meses. Também acrescenta um campo de observações para qualquer coisa incomum, limitado a uma frase curta.

### 4.3 Minimizar os dados pessoais

Lucas decide não guardar o nome de quem reporta. Um código aleatório de quem reporta permite contar quem reporta repetidamente sem identificar ninguém, e a ligação entre código e pessoa não é guardada. Ele explica à gerente do consultório que nomear quem reporta poderia fazer os funcionários se sentirem vigiados e desestimular os reportes. O modelo guarda o necessário para melhorar o serviço e deixa de fora o que poderia causar dano, aplicando a minimização de dados de forma prática. A gerente concorda, e o encarregado de proteção de dados registra a decisão e suas razões no registro das operações de tratamento mantido para auditorias.

### Exemplo resolvido

Lucas modela os reportes com agrupamentos, define valores permitidos e substitui os nomes por códigos aleatórios.

> **Caso sintético.** O modelo é sintético.

### Erros e limites

Códigos aleatórios ainda podem ser ligados por meio de outros dados. As categorias precisam de revisão.

### Exercícios

- **EX010 — Finalidade do agrupamento.** O que faz o identificador de agrupamento? *Rubrica:* 3 = agrupa os reportes do mesmo e-mail;; 2 = agrupamento;; 1 = nada;; 0 = nenhuma.
- **EX011 — Valores fixos.** Por que usar valores permitidos fixos? *Rubrica:* 3 = para evitar que variações de grafia dividam as contagens;; 2 = consistência;; 1 = nada;; 0 = nenhuma.
- **EX012 — Código de quem reporta.** Por que usar um código aleatório de quem reporta? *Rubrica:* 3 = contar quem reporta repetidamente sem identificar;; 2 = anonimato;; 1 = nomes;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) explicar técnicas comuns de engenharia social; (2) descrever por que as pessoas caem nelas; (3) explicar o papel das orientações de conscientização.

### 5.1 Técnicas comuns

Lucas estuda as técnicas descritas por Hadnagy (2018): e-mails de phishing, pretexting por telefone e falsificação de identidade. Na Brightwell, os ataques mais prováveis são faturas falsas de fornecedores, páginas de login falsas do sistema de agendamento e ligações de quem finge ser do fornecedor do sistema de gestão pedindo acesso remoto. Ele escreve descrições curtas de cada um, com exemplos sintéticos, para que os colegas reconheçam os padrões sem serem expostos a conteúdo malicioso real. Compartilha as descrições numa reunião de equipe, em que as recepcionistas acrescentam dois exemplos de ligações que receberam, que ele reescreve sem nenhum detalhe identificador.

### 5.2 Por que as pessoas caem

Cialdini (2021) descreve princípios de influência como autoridade, urgência, escassez e afinidade. Uma ligação do suposto fornecedor afirmando que um sistema vai parar de funcionar em uma hora, a menos que uma recepcionista conceda acesso remoto, usa autoridade e urgência. Lucas observa que as recepcionistas são treinadas para ser prestativas e rápidas, o que os atacantes exploram. Cair numa ligação assim reflete hábitos normais e úteis usados contra as pessoas, e não estupidez. Esse entendimento molda seu trabalho posterior em procedimentos de verificação que dispensam os funcionários de fazer esses julgamentos sozinhos. Marta concorda.

### 5.3 Papel da conscientização

A NIST SP 800-50r1 (Hansche et al., 2024) descreve a conscientização como uma parte de um programa de aprendizagem, ao lado do treinamento por função. Lucas vê que a conscientização pode ajudar os funcionários a reconhecer padrões, mas Bada, Sasse e Nurse (2019) alertam que a conscientização sozinha raramente muda o comportamento. Ele conclui que a Brightwell precisa tanto de uma conscientização breve quanto de procedimentos práticos, como ligar de volta para os fornecedores em números conhecidos, para que os funcionários saibam o que fazer, e não apenas o que temer. Ele registra essa conclusão no relatório de estágio e a discute com a gerente do consultório, que concorda em testar as duas abordagens juntas.

### Exemplo resolvido

Lucas descreve os ataques prováveis na Brightwell, explica-os com os princípios de Cialdini e posiciona a conscientização ao lado dos procedimentos.

> **Caso sintético.** Os exemplos são sintéticos; Hadnagy (2018), Cialdini (2021), a SP 800-50r1 e Bada et al. (2019) são reais.

### Erros e limites

Os tipos de ataque mudam. A conscientização se desgasta.

### Exercícios

- **EX013 — Princípios da ligação do fornecedor.** Que princípios de influência a falsa ligação do fornecedor usa? *Rubrica:* 3 = autoridade e urgência;; 2 = dois;; 1 = afinidade;; 0 = nenhuma.
- **EX014 — Hábitos explorados.** Que hábitos dos funcionários os atacantes exploram? *Rubrica:* 3 = ser prestativo e rápido;; 2 = prestatividade;; 1 = nada;; 0 = nenhuma.
- **EX015 — Conscientização e algo mais.** O que deve acompanhar a conscientização? *Rubrica:* 3 = procedimentos práticos, como ligar de volta;; 2 = procedimentos;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Sistemas operacionais e virtualização

### Objetivos de aprendizagem

Você vai (1) configurar contas e bloqueios de tela adequados ao trabalho nas clínicas; (2) usar máquinas virtuais para testes seguros; (3) reduzir os avisos de segurança que interrompem o atendimento aos pacientes.

### 6.1 Contas e bloqueios

Lucas revisa as configurações dos computadores da recepção. A recepção usa contas compartilhadas, e as telas bloqueiam depois de quinze minutos, com uma senha longa. Ele propõe contas nominais com desbloqueio rápido por crachá, para que os funcionários possam bloquear a tela sempre que se afastarem e voltar em segundos. O tempo de bloqueio cai para três minutos, porque desbloquear se torna rápido. Tornar a ação segura rápida permite que uma configuração mais rígida seja aceita, o que mostra como usabilidade e segurança podem se apoiar mutuamente. A gerente do consultório concorda com um teste.

### 6.2 Testes seguros

Antes de mudar os computadores das clínicas, Lucas testa as configurações em máquinas virtuais num computador de laboratório. Uma máquina virtual é um computador em software que pode ser restaurado a um estado limpo. Ele testa o software de desbloqueio por crachá, os tempos de bloqueio de tela e os horários de atualização sem arriscar os sistemas reais dos pacientes. As máquinas virtuais também lhe permitem examinar com segurança anexos suspeitos encaminhados para análise, sem abri-los nos computadores dos funcionários, sob a supervisão do prestador de TI. Ele registra cada resultado de teste num log simples, incluindo as configurações que falharam, para que o prestador possa repetir os testes depois em outras máquinas.

### 6.3 Menos avisos

Os computadores da recepção mostram avisos de atualização durante o horário de atendimento. Lucas configura as atualizações para serem instaladas à noite, quando as clínicas estão fechadas, e suprime os avisos não urgentes durante o horário de funcionamento. Ele conta os avisos antes e depois numa máquina de teste, ao longo de uma semana simulada. Menos interrupções reduzem a chance de os funcionários clicarem nos avisos sem lê-los, o que Herley (2009) apontou como uma resposta racional a alertas frequentes e de pouco valor. Atualizações de segurança urgentes ainda podem gerar avisos durante o dia se o prestador decidir que não podem esperar, mas espera-se que esses casos sejam raros, e eles são registrados quando ocorrem.

### Laboratório — Avisos durante o horário de funcionamento, antes e depois

```python
# Prompts during opening hours on a test machine over a simulated week (synthetic).
before = {"update restart": 12, "update available": 8, "other": 3}
after = {"update restart": 0, "update available": 0, "other": 3}
print("before:", sum(before.values()), "after:", sum(after.values()))
```

Execute com `python3 lab_prompts.py`. Saída verificada:

```text
before: 23 after: 3
```

### Exemplo resolvido

Lucas propõe contas nominais com desbloqueio por crachá e um tempo de bloqueio menor, testa em máquinas virtuais e passa as atualizações para a noite.

> **Caso sintético.** As configurações são sintéticas; Herley (2009) é real.

### Erros e limites

Leitores de crachá custam dinheiro. Atualizações noturnas exigem computadores ligados.

### Exercícios

- **EX016 — Mudança no tempo de bloqueio.** Como mudou o tempo de bloqueio de tela? *Rubrica:* 3 = de quinze para três minutos;; 2 = menor;; 1 = nada;; 0 = nenhuma.
- **EX017 — Uso de máquinas virtuais.** Por que testar em máquinas virtuais? *Rubrica:* 3 = podem ser restauradas sem arriscar os sistemas dos pacientes;; 2 = seguro;; 1 = nada;; 0 = nenhuma.
- **EX018 — Redução de avisos.** Quantos avisos diurnos por semana o laboratório mostrou antes e depois? *Rubrica:* 3 = 23 e 3;; 2 = menos;; 1 = nada;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Fundamentos de identidade e acesso

### Objetivos de aprendizagem

Você vai (1) aplicar o menor privilégio às funções das clínicas; (2) introduzir a autenticação multifator de forma usável; (3) gerir entradas, mudanças de função e saídas.

### 7.1 Menor privilégio

Lucas revisa os acessos ao sistema de gestão do consultório. Toda recepcionista pode exportar todos os prontuários, embora só precise visualizar e atualizar agendamentos. Ele propõe funções: as recepcionistas podem gerir agendamentos; os clínicos podem ver as anotações clínicas de seus pacientes; os gestores podem gerar relatórios. As exportações exigem aprovação de um gestor. O menor privilégio limita o que um atacante pode fazer com a senha roubada de uma recepcionista e reduz o dano de erros honestos, como enviar uma exportação completa ao endereço errado. Os gestores aprovam as funções numa única reunião.

### 7.2 Autenticação multifator

A Brightwell decide acrescentar um segundo fator ao e-mail e ao sistema de gestão do consultório. Lucas compara opções para recepcionistas que dividem mesas e podem não ter celular do trabalho. Ele recomenda chaves de segurança presas ao porta-crachá para os funcionários que acessam dados de pacientes, e um aplicativo para os gestores. Planeja um piloto numa clínica, medindo o tempo de login e as ligações de suporte, e prepara instruções simples com imagens, porque uma implantação confusa geraria atalhos que anulariam o benefício. A clínica piloto é escolhida pela gerente.

### 7.3 Entradas, mudanças e saídas

Lucas encontra contas de funcionários que saíram há meses. Ele organiza um processo simples: o RH avisa a TI no último dia, a TI desativa a conta no mesmo dia, e os gestores revisam os acessos dos funcionários que mudam de função. Ele cria um relatório mensal listando as contas não usadas há sessenta dias. A gestão de contas depende da comunicação rotineira entre pessoas, por isso ele desenha o processo em torno de uma lista de verificação que o RH já usa. O primeiro relatório encontra nove contas sem uso, que são desativadas depois que os gestores confirmam que nenhuma é necessária.

### Exemplo resolvido

Lucas define as funções das clínicas, planeja um piloto de chaves de segurança e incorpora um processo de saída à lista de verificação que o RH já usa.

> **Caso sintético.** As funções são sintéticas.

### Erros e limites

Mudanças de função exigem atualizações. Chaves podem ser perdidas.

### Exercícios

- **EX019 — Exportação pela recepcionista.** Que mudança se aplica às exportações? *Rubrica:* 3 = exigem aprovação de um gestor;; 2 = aprovação;; 1 = nada;; 0 = nenhuma.
- **EX020 — Escolha da chave.** Por que recomendar chaves para as recepcionistas? *Rubrica:* 3 = dividem mesas e podem não ter celular do trabalho;; 2 = sem celular;; 1 = nada;; 0 = nenhuma.
- **EX021 — Etapa de saída.** Quando a conta de quem sai é desativada? *Rubrica:* 3 = no mesmo dia em que o RH avisa a TI;; 2 = mesmo dia;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Fundamentos de arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) descrever defesas em camadas para um grupo de clínicas; (2) situar os papéis humanos na arquitetura; (3) projetar para que um único erro seja contido.

### 8.1 Camadas

Lucas esboça as camadas de segurança da Brightwell: filtragem de e-mail, etiquetas externas, autenticação multifator, menor privilégio, backups e monitoramento pelo prestador de TI. Saltzer e Schroeder (1975) descreveram princípios como o menor privilégio e a aceitabilidade psicológica, que significa que a proteção deve ser fácil de usar corretamente. Lucas confere cada camada segundo os dois princípios. Descobre que os backups existem, mas nunca foram testados, e que os alertas de monitoramento vão para uma caixa postal que ninguém lê fora do expediente. Ele lista os dois problemas para o prestador de TI, que concorda em fazer um teste de restauração e encaminhar os alertas urgentes para um celular de plantão.

### 8.2 Papéis humanos

Lucas acrescenta os papéis humanos à arquitetura: recepcionistas que reportam e-mails suspeitos, gestores que aprovam exportações, a gerente do consultório que aprova pagamentos e o prestador de TI que analisa os reportes. Cada papel precisa de ferramentas e de tempo. Ele observa que o reporte é uma camada de detecção: funcionários que reportam rapidamente permitem que a TI bloqueie um ataque antes que outros caiam nele. Tratar os funcionários como parte da defesa estimula designs que os apoiam, e não designs que os contornam. Ele escreve as necessidades ao lado de cada papel.

### 8.3 Conter os erros

Lucas projeta para que um único erro não vire um desastre. Uma recepcionista que digita a senha numa página falsa é protegida pela chave de segurança. Um gestor que abre um malware é limitado pelos direitos reduzidos e recuperado por backups testados. Um pedido de mudança de pagamento fica bloqueado até a verificação por retorno de ligação. Ele apresenta um diagrama de uma página que mostra cada erro e a camada que o contém. Isso torna a arquitetura compreensível para gestores sem formação técnica. Os gestores acham o diagrama fácil de seguir.

### Exemplo resolvido

Lucas mapeia as camadas da Brightwell, acrescenta os papéis humanos, incluindo o reporte como detecção, e mostra que camada contém cada erro.

> **Caso sintético.** A arquitetura é sintética; Saltzer e Schroeder (1975) é real.

### Erros e limites

Camadas não testadas dão falsa confiança. Diagramas simplificam.

### Exercícios

- **EX022 — Achado nos backups.** Que problema Lucas encontrou nos backups? *Rubrica:* 3 = nunca tinham sido testados;; 2 = não testados;; 1 = nada;; 0 = nenhuma.
- **EX023 — Camada do reporte.** Que camada o reporte dos funcionários fornece? *Rubrica:* 3 = detecção;; 2 = detecção;; 1 = prevenção;; 0 = nenhuma.
- **EX024 — Contenção de pagamentos.** O que contém uma falsa mudança de pagamento? *Rubrica:* 3 = um bloqueio com verificação por retorno de ligação;; 2 = retorno de ligação;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) escolher medidas para um serviço de reportes; (2) calcular o tempo até o primeiro reporte e o tempo até o veredito; (3) apresentar as medidas de forma justa.

### 9.1 Escolher as medidas

Lucas e a gerente do consultório escolhem as medidas para os reportes da Brightwell: a proporção de e-mails maliciosos reportados por pelo menos uma pessoa, o tempo da chegada até o primeiro reporte, o tempo do reporte até o veredito e o ônus para os funcionários, medido por uma pergunta trimestral curta. Eles evitam ordenar as clínicas por taxas de clique em simulações, porque os rankings constrangem os funcionários e as taxas de clique dependem muito da dificuldade do e-mail simulado. As medidas devem ajudar a melhorar o serviço, e não julgar indivíduos. Cada medida tem uma definição escrita curta.

### 9.2 Calcular os tempos

Lucas usa o modelo de dados do capítulo 4 para calcular os tempos de um mês de e-mails maliciosos sintéticos. Para cada agrupamento, encontra o primeiro reporte e o horário do veredito. O laboratório imprime a mediana do tempo até o primeiro reporte e a mediana do tempo até o veredito. Ele descobre que os reportes costumam chegar rapidamente, mas os vereditos são lentos, porque o prestador de TI confere a caixa postal só duas vezes por dia. Isso aponta para uma correção prática: notificações de novos reportes. Ele compartilha o resultado com o prestador.

### Laboratório — Mediana do tempo até o primeiro reporte e até o veredito

```python
# Median minutes: arrival to first report, and report to verdict (synthetic month).
first = [3, 5, 6, 8, 9, 11, 14, 18, 25, 40, 55]
verdict = [60, 95, 120, 150, 170, 190, 210, 260, 300, 340, 420]
m = lambda x: sorted(x)[len(x) // 2]
print(f"emails {len(first)}; median to first report {m(first)} min; median report to verdict {m(verdict)} min")
```

Execute com `python3 lab_times.py`. Saída verificada:

```text
emails 11; median to first report 11 min; median report to verdict 190 min
```

### 9.3 Apresentação justa

Lucas apresenta as medidas por grupos de clínicas com pelo menos vinte funcionários, e não por indivíduo ou por clínica pequena. Mostra as medianas com o número de e-mails por trás delas. Explica aos gestores que um mês de dados é ruidoso e que as tendências importam mais do que valores isolados. Uma apresentação justa protege a privacidade dos funcionários e ajuda os gestores a tirar conclusões sensatas, em vez de reagir a variações aleatórias. Ele também mostra o mesmo resumo aos funcionários na reunião mensal, para que todos vejam os mesmos números que os gestores e possam fazer perguntas sobre eles.

### Exemplo resolvido

Lucas seleciona medidas de reporte, calcula medianas que mostram vereditos lentos e apresenta resultados agrupados e atentos ao ruído.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

E-mails não reportados ficam de fora. As amostras mensais são pequenas.

### Exercícios

- **EX025 — Ranking evitado.** Por que evitar rankings de clínicas por taxa de clique? *Rubrica:* 3 = constrangem os funcionários e dependem da dificuldade;; 2 = justiça;; 1 = nada;; 0 = nenhuma.
- **EX026 — Medianas no laboratório.** Que medianas o laboratório calculou? *Rubrica:* 3 = 11 minutos até o reporte e 190 minutos até o veredito;; 2 = veredito lento;; 1 = nada;; 0 = nenhuma.
- **EX027 — Correção do veredito.** Que correção o veredito lento sugere? *Rubrica:* 3 = notificações de novos reportes;; 2 = alertas;; 1 = nada;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Fatores humanos e política cibernética: orientação

### Objetivos de aprendizagem

Você vai (1) descrever o escopo dos fatores humanos e da política cibernética; (2) explicar como a política molda o comportamento; (3) apresentar em linhas gerais as políticas atuais da Brightwell.

### 10.1 Escopo

Fatores humanos e política cibernética tratam de como as pessoas interagem com os sistemas de segurança e de como regras, cultura e design moldam essa interação. Sasse, Brostoff e Weirich (2001) defenderam transformar o elo mais fraco projetando a segurança em torno das capacidades humanas. Lucas aprende que o campo inclui usabilidade, treinamento, cultura, ética e política organizacional. Na Brightwell, isso significa olhar como recepcionistas, clínicos e gestores vivenciam a segurança e o que as políticas lhes pedem. Ele lê o artigo e resume seu argumento principal para a gerente do consultório em palavras simples.

### 10.2 A política molda o comportamento

Uma política declara o que as pessoas devem fazer. A política da Brightwell exige a troca de senha todo mês e proíbe anotar senhas. Lucas descobre que as trocas mensais levam os funcionários a anotar as senhas em post-its, violando a segunda regra. Uma política que ignora a memória humana cria o comportamento que proíbe. Ele também descobre que a política diz que os funcionários devem reportar incidentes, mas não diz como, o que deixa as pessoas na dúvida. Uma boa política é específica, prática e coerente com o modo como as pessoas trabalham. Ele anota os dois problemas no relatório.

### 10.3 As políticas da Brightwell

Lucas revisa as políticas da Brightwell: uso aceitável, senhas, proteção de dados e reporte de incidentes. Lista os problemas: regras de senha desatualizadas, nenhuma instrução sobre como reportar, nenhum procedimento para verificar ligações de fornecedores e nenhuma declaração de que reportar erros é bem-vindo. Ele rascunha para a gerente do consultório uma lista curta de mudanças propostas, em linguagem simples. Essa orientação define a agenda dos capítulos de fatores humanos que se seguem, que vão desenhar e testar cada melhoria. A gerente concorda em revisar a lista com os responsáveis pelas clínicas na próxima reunião.

### Exemplo resolvido

Lucas define o campo, mostra como as trocas mensais de senha levam a senhas anotadas e lista as lacunas das políticas da Brightwell.

> **Caso sintético.** As políticas são sintéticas; Sasse et al. (2001) é real.

### Erros e limites

Mudanças de política precisam de aprovação. A linguagem simples pode perder precisão.

### Exercícios

- **EX028 — Conflito de política.** Que duas regras de política conflitam? *Rubrica:* 3 = trocas mensais e proibição de anotar;; 2 = conflito;; 1 = nada;; 0 = nenhuma.
- **EX029 — Lacuna do reporte.** O que falta na política de reporte? *Rubrica:* 3 = como reportar;; 2 = método;; 1 = nada;; 0 = nenhuma.
- **EX030 — Declaração ausente.** Que declaração de acolhimento está ausente? *Rubrica:* 3 = que reportar erros é bem-vindo;; 2 = não atribuição de culpa;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). Lucas Ferreira, a professora Marta Kowalczyk, o Northgate Institute of Technology, o Brightwell Dental Group e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Quatro sistemas.

**EX002.** Como um atalho causado por senhas demais e pouco tempo.

**EX003.** A atenção ao atendimento aos pacientes.

**EX004.** Porque são domínios reais controlados pelos atacantes, de modo que suas mensagens se autenticam corretamente.

**EX005.** Permitem aos funcionários chegar às páginas oficiais de login sem seguir links de e-mail.

**EX006.** Pistas que economizam tempo, em vez de acrescentar etapas.

**EX007.** Uma contagem manual de meia hora que muitas vezes tinha erros.

**EX008.** Faturas falsas, com 9 reportes.

**EX009.** Porque os assuntos às vezes contêm nomes de pacientes.

**EX010.** Agrupa os reportes do mesmo e-mail num único incidente.

**EX011.** Para evitar que variações de grafia dividam as contagens.

**EX012.** Para contar quem reporta repetidamente sem identificar ninguém.

**EX013.** Autoridade e urgência.

**EX014.** Ser prestativo e rápido.

**EX015.** Procedimentos práticos, como ligar de volta para os fornecedores em números conhecidos.

**EX016.** De quinze minutos para três, porque desbloquear se tornou rápido.

**EX017.** Porque podem ser restauradas a um estado limpo sem arriscar os sistemas reais.

**EX018.** 23 antes e 3 depois.

**EX019.** As exportações exigem aprovação de um gestor.

**EX020.** Porque dividem mesas e podem não ter celular do trabalho.

**EX021.** No mesmo dia em que o RH avisa a TI.

**EX022.** Nunca tinham sido testados.

**EX023.** Detecção, que permite à TI bloquear ataques cedo.

**EX024.** Um bloqueio com verificação por retorno de ligação.

**EX025.** Porque os rankings constrangem os funcionários e as taxas de clique dependem da dificuldade da simulação.

**EX026.** 11 minutos até o primeiro reporte e 190 minutos até o veredito.

**EX027.** Notificações de novos reportes, em vez de conferências duas vezes por dia.

**EX028.** As trocas mensais de senha e a proibição de anotar senhas.

**EX029.** Não diz como reportar.

**EX030.** Uma declaração de que reportar erros é bem-vindo.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Cialdini, R. B. (2021). *Influence, new and expanded: The psychology of persuasion*. Harper Business.
- European Union Agency for Cybersecurity. (2019). *Cybersecurity culture guidelines: Behavioural aspects of cybersecurity*. ENISA. <https://www.enisa.europa.eu/publications/cybersecurity-culture-guidelines-behavioural-aspects-of-cybersecurity>
- Hadnagy, C. (2018). *Social engineering: The science of human hacking* (2nd ed.). Wiley.
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
