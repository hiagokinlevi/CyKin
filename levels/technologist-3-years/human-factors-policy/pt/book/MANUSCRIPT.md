# Fatores Humanos e Política Cibernética: Curso de Tecnólogo

- Idioma: português do Brasil (`pt`); curso 075, curso de tecnólogo (3 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–20 de 30 já estão escritos em português, com os exercícios EX001–EX060 e suas resoluções com rubricas de 0 a 3 e 9 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 21–30 (EX061–EX090) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

Capítulos 21–30: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-21), até a chegada dos próximos lotes.

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

<a id="ch-11"></a>

## Capítulo 11 — Ativos e contexto

### Objetivos de aprendizagem

Você vai (1) identificar os ativos que os controles centrados nas pessoas protegem; (2) descrever o contexto em que os funcionários tomam decisões de segurança; (3) priorizar os ativos pelo dano.

### 11.1 Ativos

Lucas lista os ativos da Brightwell com a gerente da clínica: prontuários dos pacientes, contas de pagamento, o sistema de agendamento, dados de imagem e contas dos funcionários. Ele também lista ativos menos óbvios: a confiança dos pacientes, a reputação de cada clínica e a disposição dos funcionários para reportar problemas. Esse último ativo importa porque um programa que prejudica a confiança pode tornar a organização menos segura no conjunto. Nomear a confiança como ativo lembra aos gestores que o modo como a segurança é feita importa tanto quanto o que é feito. A gerente concorda em incluir a confiança no registro de riscos.

### 11.2 Contexto de decisão

Lucas descreve o contexto em que os funcionários tomam decisões de segurança. As recepcionistas decidem rápido, muitas vezes enquanto falam com pacientes. Os clínicos estão concentrados no tratamento e veem o e-mail entre um atendimento e outro. Os gestores lidam com fornecedores e pagamentos, muitas vezes perto dos prazos de fechamento do mês. Cada grupo enfrenta pressões diferentes e ataques diferentes. Ele escreve um perfil de um parágrafo para cada grupo, descrevendo os momentos típicos em que uma mensagem ou ligação enganosa pode chegar e o que mais estão fazendo nessa hora, o que depois orienta o desenho dos controles. Os funcionários revisam os perfis.

### 11.3 Priorização pelo dano

Lucas ordena os ativos pelo dano que se seguiria a um comprometimento. Os prontuários dos pacientes vêm primeiro, por causa dos deveres de privacidade e da angústia que um vazamento causaria. As contas de pagamento vêm em segundo, porque a fraude pode custar milhares rapidamente. As contas dos funcionários vêm em terceiro, porque dão caminho até os dois primeiros. Ele observa que o risco de pagamento depende quase inteiramente de uma única decisão humana, aceitar a alteração de um dado bancário, o que o torna prioridade para um procedimento de verificação e não para conscientização geral. Os gestores concordam.

### Exemplo resolvido

Lucas lista ativos que incluem a confiança, traça o perfil dos contextos de decisão de três grupos e ordena os ativos pelo dano.

> **Caso sintético.** O contexto é sintético.

### Erros e limites

As ordenações mudam conforme os serviços mudam. Os perfis generalizam.

### Exercícios

- **EX031 — Ativo oculto.** Que ativo menos óbvio Lucas nomeia? *Rubrica:* 3 = a disposição dos funcionários para reportar;; 2 = confiança;; 1 = nada;; 0 = nenhuma.

- **EX032 — Pressão dos gestores.** Quando os gestores enfrentam pressão de pagamentos? *Rubrica:* 3 = perto dos prazos de fechamento do mês;; 2 = fechamento do mês;; 1 = nada;; 0 = nenhuma.

- **EX033 — Decisão de pagamento.** Que decisão única determina o risco de pagamento? *Rubrica:* 3 = aceitar a alteração de um dado bancário;; 2 = dado bancário;; 1 = nada;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Fluxos de dados

### Objetivos de aprendizagem

Você vai (1) mapear como os dados de pacientes e de pagamento fluem entre pessoas e sistemas; (2) encontrar os pontos em que as pessoas lidam com dados sob pressão; (3) propor fluxos mais seguros.

### 12.1 Mapeamento dos fluxos

Lucas mapeia os fluxos de dados na Brightwell. Os dados dos pacientes vão dos formulários de agendamento para o sistema da clínica, depois para os clínicos e para as seguradoras nos pedidos de reembolso. Os dados de pagamento vão dos pacientes para as maquininhas de cartão e das faturas para o banco. Lucas desenha cada fluxo com as pessoas envolvidas em cada etapa. Ele descobre que algumas cartas de pacientes são enviadas a especialistas externos a partir de contas de e-mail pessoais quando o sistema da clínica está lento, o que contorna as proteções e deixa cópias fora do controle da Brightwell. Ele compartilha o mapa com a gerente da clínica.

### 12.2 Pontos de pressão

Lucas marca as etapas em que as pessoas lidam com dados sob pressão. As recepcionistas copiam dados entre sistemas nos períodos de movimento. Os gestores processam faturas de fornecedores no fechamento do mês. Os clínicos enviam encaminhamentos ao fim dos turnos. Em cada ponto, um erro ou um engano é mais provável porque a atenção está dividida. Ele observa que o atalho do e-mail pessoal acontece porque o método oficial leva vários minutos, enquanto o e-mail pessoal leva segundos, o que mostra mais uma vez que a conveniência guia o comportamento quando a segurança acrescenta esforço demais. Ele marca cada ponto em vermelho no mapa.

### 12.3 Fluxos mais seguros

Lucas propõe fluxos mais seguros. Um modelo seguro de encaminhamento dentro do sistema da clínica, que envia a especialistas cadastrados com um clique, substitui o e-mail pessoal. Faturas com dados bancários alterados ficam retidas automaticamente para confirmação por retorno de ligação. A cópia entre sistemas diminui com a integração dos sistemas de agendamento e da clínica. Cada mudança faz do caminho seguro também o caminho mais rápido. Ele apresenta as propostas com estimativas de economia de tempo, o que convence a gerente da clínica mais do que argumentos de segurança sozinhos. A gerente pede ao fornecedor um orçamento para a integração e a agenda para o próximo trimestre.

### Exemplo resolvido

Lucas mapeia os fluxos de pacientes e de pagamento, identifica os pontos de pressão e o atalho do e-mail pessoal e propõe caminhos seguros mais rápidos.

> **Caso sintético.** Os fluxos são sintéticos.

### Erros e limites

A integração de sistemas pode ser cara. Os especialistas precisam estar cadastrados.

### Exercícios

- **EX034 — Causa do atalho.** Por que os funcionários usam e-mail pessoal para as cartas? *Rubrica:* 3 = o método oficial leva minutos e o e-mail pessoal, segundos;; 2 = rapidez;; 1 = nada;; 0 = nenhuma.

- **EX035 — Correção do encaminhamento.** O que substitui o atalho do e-mail pessoal? *Rubrica:* 3 = um modelo seguro de encaminhamento com um clique;; 2 = modelo;; 1 = nada;; 0 = nenhuma.

- **EX036 — Argumento persuasivo.** O que mais convenceu a gerente da clínica? *Rubrica:* 3 = as estimativas de economia de tempo;; 2 = tempo;; 1 = segurança;; 0 = nenhuma.

<a id="ch-13"></a>

## Capítulo 13 — Cenários de risco

### Objetivos de aprendizagem

Você vai (1) escrever cenários de risco realistas que envolvam pessoas; (2) estimar probabilidade e impacto de forma simples; (3) ligar os cenários aos controles.

### 13.1 Escrita de cenários

Lucas escreve cenários que descrevem como um ataque poderia se desenrolar na Brightwell, cada um com um atacante, um método, um alvo e um resultado. Num deles, alguém que se passa pelo fornecedor do sistema da clínica convence uma recepcionista por telefone a instalar um software de acesso remoto e depois copia os prontuários dos pacientes. Noutro, um e-mail falso de fornecedor altera os dados bancários e um gestor paga uma fatura alta ao atacante. Num terceiro, uma página falsa de login do sistema de agendamento captura a senha de uma recepcionista. Cada cenário usa detalhes sintéticos.

### 13.2 Estimativa do risco

Lucas estima probabilidade e impacto em escalas simples de três níveis, com a gerente da clínica. A ligação do falso fornecedor tem probabilidade média e impacto alto; a alteração falsa de fornecedor tem probabilidade alta e impacto alto; o login falso tem probabilidade alta, mas impacto médio depois que as chaves de segurança estão em uso. O laboratório multiplica as notas e ordena os cenários. Ele observa que as notas são julgamentos e que seu principal valor está em provocar a discussão sobre quais riscos tratar primeiro. A gerente revisa cada nota.

### Laboratório — Ordenação dos cenários de risco

```python
# Rank risk scenarios by likelihood x impact on 1-3 scales (synthetic).
s = [("fake vendor call", 2, 3), ("fake supplier bank change", 3, 3), ("fake booking login", 3, 2)]
for n, l, i in sorted(s, key=lambda x: -x[1] * x[2]): print(f"{n}: {l}x{i} = {l * i}")
```

Execute com `python3 lab_scenarios.py`. Saída verificada:

```text
fake supplier bank change: 3x3 = 9
fake vendor call: 2x3 = 6
fake booking login: 3x2 = 6
```

### 13.3 Ligação com os controles

Para cada cenário, Lucas lista os controles que o impediriam ou o limitariam. A ligação do falso fornecedor é combatida por uma regra: o acesso remoto só é concedido depois de ligar de volta para o fornecedor num número conhecido e obter a aprovação de um gestor. A alteração de fornecedor é combatida pela retenção automática e pelo retorno de ligação. O login falso é combatido pelas chaves de segurança e pelo reporte. Mapear os controles nos cenários mostra aos gestores por que cada controle existe e que risco cresceria se ele fosse retirado. Os gestores guardam a tabela.

### Exemplo resolvido

Lucas escreve três cenários centrados nas pessoas, ordena-os com notas simples e mapeia os controles de cada um.

> **Caso sintético.** Os cenários são sintéticos.

### Erros e limites

As notas são subjetivas. Os cenários podem não prever métodos novos.

### Exercícios

- **EX037 — Cenário do fornecedor.** O que quer quem liga se passando pelo fornecedor? *Rubrica:* 3 = a instalação de um software de acesso remoto;; 2 = acesso remoto;; 1 = senhas;; 0 = nenhuma.

- **EX038 — Cenário principal.** Que cenário ficou em primeiro no laboratório? *Rubrica:* 3 = a alteração falsa de fornecedor, com nota 9;; 2 = fornecedor;; 1 = nada;; 0 = nenhuma.

- **EX039 — Regra de acesso remoto.** Que regra combate a ligação do falso fornecedor? *Rubrica:* 3 = retorno de ligação num número conhecido mais aprovação de um gestor;; 2 = retorno de ligação;; 1 = nada;; 0 = nenhuma.

<a id="ch-14"></a>

## Capítulo 14 — Métodos I

### Objetivos de aprendizagem

Você vai (1) aplicar um questionário anônimo curto; (2) conduzir entrevistas breves; (3) resumir os achados para a ação.

### 14.1 Questionário

Lucas desenha um questionário anônimo de cinco perguntas para todos os funcionários sobre o reporte de e-mails suspeitos: se sabem como reportar, se já reportaram, o que os impede, se receberam resposta e quão confiantes se sentem. Ele o mantém curto para que funcionários ocupados o respondam em dois minutos. A gerente da clínica o aprova e representantes dos funcionários revisam a redação. Ele recebe 150 respostas de 210 funcionários. O laboratório conta as respostas à pergunta sobre barreiras. Os funcionários são informados de que o questionário é anônimo e de que os resultados serão compartilhados com todos num resumo curto na próxima reunião mensal.

### Laboratório — Barreiras no questionário entre 150 respostas

```python
# Survey barriers among 150 responses (multiple choice, synthetic).
b = {"unsure IT wants it": 64, "don't know how": 41, "too busy": 33, "never heard back": 29, "fear of blame": 18}
for k, v in sorted(b.items(), key=lambda x: -x[1]): print(f"{k}: {v}/150 = {v / 150:.0%}")
```

Execute com `python3 lab_barrier.py`. Saída verificada:

```text
unsure IT wants it: 64/150 = 43%
don't know how: 41/150 = 27%
too busy: 33/150 = 22%
never heard back: 29/150 = 19%
fear of blame: 18/150 = 12%
```

### 14.2 Entrevistas

Lucas entrevista seis funcionários de funções diferentes, por quinze minutos cada, com consentimento e sem registrar nomes. Ele pede que descrevam a última mensagem suspeita que receberam e o que fizeram. As recepcionistas dizem que muitas vezes apagam os e-mails suspeitos porque não têm certeza se a TI os quer. Uma clínica conta que reportou uma vez, nunca teve retorno e por isso parou. As entrevistas dão as razões por trás dos números do questionário e sugerem correções específicas que o questionário sozinho não revelaria. Cada anotação de entrevista é conferida com a pessoa.

### 14.3 Resumo para a ação

Lucas resume seus achados em três pontos de ação: dizer claramente aos funcionários que reportes na dúvida são bem-vindos; acrescentar um botão de reporte para que reportar leve segundos; e responder a cada reporte no mesmo dia. Ele liga cada ponto a números do questionário e a falas das entrevistas, retirando tudo o que pudesse identificar alguém. A gerente da clínica aprova os três. Transformar os achados numa lista curta de ações ajuda gestores ocupados a decidir rápido e mantém o estudo concentrado em melhorar o serviço. Os funcionários veem o mesmo resumo.

### Exemplo resolvido

Lucas aplica o questionário a 150 funcionários e entrevista seis, encontra a incerteza e a falta de retorno como barreiras principais e propõe três ações.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

As respostas do questionário são autodeclaradas. Seis entrevistas são poucas.

### Exercícios

- **EX040 — Taxa de resposta.** Qual foi a taxa de resposta do questionário? *Rubrica:* 3 = cerca de 71%;; 2 = 150 de 210;; 1 = 150%;; 0 = nenhuma.

- **EX041 — Barreira principal.** Qual foi a principal barreira no laboratório? *Rubrica:* 3 = não ter certeza se a TI quer o reporte, 64 de 150 ou 43%;; 2 = incerteza;; 1 = nada;; 0 = nenhuma.

- **EX042 — Relato da clínica.** Por que a clínica parou de reportar? *Rubrica:* 3 = nunca teve retorno;; 2 = falta de retorno;; 1 = nada;; 0 = nenhuma.

<a id="ch-15"></a>

## Capítulo 15 — Laboratório guiado

### Objetivos de aprendizagem

Você vai (1) testar um botão de reporte com voluntários num ambiente de teste; (2) medir tempo e sucesso; (3) registrar problemas de usabilidade.

### 15.1 Montagem do teste

Num laboratório guiado, Lucas monta uma caixa postal de teste com e-mails sintéticos e o botão de reporte instalado. Oito funcionários voluntários participam, sabendo que estão testando o botão e não sendo testados. Cada voluntário reporta dois e-mails suspeitos sintéticos pelo método antigo, encaminhando para um endereço, e dois usando o botão. A ordem é alternada para que o aprendizado não favoreça um dos métodos. Lucas registra tempo e sucesso e anota qualquer hesitação ou confusão enquanto os voluntários trabalham. Cada sessão dura vinte minutos.

### 15.2 Resultados

O laboratório compara os tempos. Encaminhar leva cerca de quarenta e cinco segundos em média, em parte porque os voluntários procuram o endereço; o botão leva cerca de sete segundos. Dois voluntários encaminharam para o endereço errado. Todos têm sucesso com o botão. Os voluntários avaliam o botão como muito mais fácil. Lucas observa que o ambiente de teste é mais calmo que uma recepção movimentada, de modo que os tempos reais podem ser maiores, mas a diferença é tão grande que o botão claramente vale a adoção. Ele registra o resultado numa nota curta para a gerente da clínica.

### Laboratório — Tempos de tarefa: encaminhamento versus botão

```python
# Mean task times (seconds) for eight volunteers (synthetic).
fwd = [41, 52, 38, 47, 44, 50, 39, 49]; btn = [6, 8, 7, 7, 6, 9, 7, 6]
print(f"forwarding {sum(fwd) / 8:.0f} s; button {sum(btn) / 8:.0f} s")
```

Execute com `python3 lab_button.py`. Saída verificada:

```text
forwarding 45 s; button 7 s
```

### 15.3 Problemas de usabilidade

Lucas registra três problemas: nas telas menores da recepção, o botão aparece só num menu de excedentes; os voluntários não têm certeza se o reporte foi enviado porque nenhuma confirmação aparece; e o botão não existe no aplicativo de e-mail no celular que os clínicos usam. Ele os reporta ao prestador de TI, que ajusta o layout da barra de ferramentas e ativa uma mensagem de confirmação. O problema do celular exige outro add-in, que fica agendado. Registrar os problemas com precisão os torna mais fáceis de corrigir. Cada correção é testada de novo.

### Exemplo resolvido

Lucas testa o botão com oito voluntários numa caixa postal de teste, encontra grande economia de tempo e registra três problemas de usabilidade.

> **Caso sintético.** O teste é sintético.

### Erros e limites

Condições calmas de laboratório. Amostra pequena.

### Exercícios

- **EX043 — Alternância da ordem.** Por que alternar a ordem dos métodos? *Rubrica:* 3 = para que o aprendizado não favoreça um método;; 2 = equidade;; 1 = nada;; 0 = nenhuma.

- **EX044 — Tempos do laboratório.** Que tempos médios o laboratório mostrou? *Rubrica:* 3 = 45 segundos encaminhando e 7 segundos com o botão;; 2 = 38 economizados;; 1 = nada;; 0 = nenhuma.

- **EX045 — Falta de confirmação.** Que problema a falta de confirmação causou? *Rubrica:* 3 = os voluntários não tinham certeza se o reporte foi enviado;; 2 = incerteza;; 1 = nada;; 0 = nenhuma.

<a id="ch-16"></a>

## Capítulo 16 — Métodos II

### Objetivos de aprendizagem

Você vai (1) comparar o reporte antes e depois de uma mudança; (2) considerar outras explicações; (3) usar uma implantação escalonada como comparação.

### 16.1 Antes e depois

Depois da introdução do botão e das respostas no mesmo dia, Lucas compara o reporte em dois meses antes e dois meses depois. Os reportes de e-mails maliciosos reais subiram e a mediana do tempo até o primeiro reporte caiu. Ele é cuidadoso: outros fatores podem ter mudado, como o número de ataques ou a cobertura na imprensa de um vazamento numa clínica odontológica. Ele confere os logs de filtragem do prestador de TI e descobre que o volume de ataques foi parecido nos dois períodos, o que torna a mudança mais convincente. Ele registra as duas verificações no relatório.

### 16.2 Implantação escalonada

Por causa de um atraso, quatro clínicas receberam o botão duas semanas depois das outras. Lucas usa essas duas semanas como comparação. Nesse período, as clínicas com o botão reportaram uma proporção maior de e-mails maliciosos do que as clínicas sem ele. O laboratório calcula as duas proporções. Ele observa que as clínicas não foram escolhidas ao acaso, já que o atraso se deveu a computadores mais antigos, de modo que os grupos podem ser diferentes. Ainda assim, a comparação dá mais peso ao resultado de antes e depois. Ele registra o motivo do atraso.

### Laboratório — Clínicas adiantadas e atrasadas durante a quinzena escalonada

```python
# Staggered fortnight: share of malicious emails reported (synthetic).
early = (8, 10); late = (4, 9)
for n, (r, t) in (("early clinics", early), ("late clinics", late)): print(f"{n}: {r}/{t} = {r / t:.0%}")
```

Execute com `python3 lab_stagger.py`. Saída verificada:

```text
early clinics: 8/10 = 80%
late clinics: 4/9 = 44%
```

### 16.3 Interpretação cuidadosa

Lucas escreve que as evidências são compatíveis com a melhora do reporte graças ao botão e às respostas, apoiadas pelo volume estável de ataques e pela comparação escalonada, mas não a provam. Ele recomenda continuar o monitoramento. Marta elogia o hábito de buscar uma comparação sempre que possível, observando que muitas mudanças no trabalho podem ser avaliadas de forma mais convincente quase sem custo se alguém percebe uma comparação natural e a registra com cuidado. Ele também lista que dados adicionais fortaleceriam a conclusão, como um período mais longo de monitoramento e números das clínicas que entraram depois.

### Exemplo resolvido

Lucas compara antes e depois com volume de ataques estável e usa uma implantação atrasada como comparação.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Grupos não aleatórios. Períodos curtos.

### Exercícios

- **EX046 — Verificação do volume.** Como Lucas verificou se o volume de ataques mudou? *Rubrica:* 3 = os logs de filtragem mostraram volume parecido;; 2 = logs;; 1 = nada;; 0 = nenhuma.

- **EX047 — Proporções do laboratório.** Que proporções as clínicas adiantadas e atrasadas reportaram no laboratório? *Rubrica:* 3 = 80% contra 44%;; 2 = as adiantadas, mais;; 1 = nada;; 0 = nenhuma.

- **EX048 — Causa do atraso.** Por que algumas clínicas atrasaram? *Rubrica:* 3 = computadores mais antigos;; 2 = hardware;; 1 = acaso;; 0 = nenhuma.

<a id="ch-17"></a>

## Capítulo 17 — Ferramentas

### Objetivos de aprendizagem

Você vai (1) selecionar ferramentas para reporte e triagem; (2) configurar as ferramentas pensando na privacidade; (3) automatizar etapas simples da triagem.

### 17.1 Seleção de ferramentas

Lucas ajuda a Brightwell a escolher uma ferramenta de reporte e triagem. As opções incluem o recurso de reporte embutido na plataforma de e-mail, um produto de triagem separado e uma simples caixa postal compartilhada com regras. Ele as compara em custo, facilidade para os funcionários, esforço para o prestador de TI e privacidade. O recurso embutido, com uma caixa postal compartilhada e automação simples, atende à maior parte das necessidades a baixo custo. Ele evita ferramentas que dão nota a funcionários individualmente, porque o programa existe para apoiar as pessoas, não para ranqueá-las. O prestador concorda com a escolha.

### 17.2 Configuração de privacidade

Lucas configura a ferramenta para que a identidade de quem reporta fique visível apenas para a pessoa da triagem, com a finalidade de enviar respostas, e não seja exportada. Os reportes com mais de noventa dias são apagados automaticamente. Os painéis mostram totais por grupos de pelo menos vinte funcionários. Ele documenta essas configurações com o responsável pela proteção de dados. Privacidade pela configuração significa que as boas intenções são garantidas pelo sistema, em vez de depender de que as pessoas se lembrem de regras sobre o que não devem olhar. O responsável aprova as configurações.

### 17.3 Automação da triagem

Lucas monta uma automação simples: os reportes do mesmo e-mail são agrupados; uma mensagem de agradecimento é enviada na hora; e, se o e-mail coincide com uma amostra maliciosa conhecida, um veredito padrão é enviado e o e-mail é removido de todas as caixas postais. O prestador de TI revisa só os e-mails novos. O laboratório conta quantos reportes precisaram de revisão humana numa semana sintética. A automação reduz a carga de triagem e acelera o retorno, que as entrevistas mostraram ser muito valorizado pelos funcionários. As amostras conhecidas são revisadas toda semana para manter a lista correta.

### Laboratório — Reportes que precisam de revisão humana após a automação

```python
# Reports needing human review after automation in a synthetic week.
reports = 60; duplicates = 38; known = 13
print(f"reports {reports}; grouped duplicates {duplicates}; known-malicious auto verdicts {known}; human review {reports - duplicates - known}")
```

Execute com `python3 lab_auto.py`. Saída verificada:

```text
reports 60; grouped duplicates 38; known-malicious auto verdicts 13; human review 9
```

### Exemplo resolvido

Lucas escolhe uma ferramenta embutida de baixo custo, configura limites de privacidade e automatiza o agrupamento, o agradecimento e os vereditos conhecidos.

> **Caso sintético.** As ferramentas são genéricas e os dados, sintéticos.

### Erros e limites

Vereditos automáticos podem errar. Limites de retenção perdem o histórico.

### Exercícios

- **EX049 — Recurso evitado.** Que recurso de ferramenta Lucas evitou? *Rubrica:* 3 = dar nota a funcionários individualmente;; 2 = notas;; 1 = nada;; 0 = nenhuma.

- **EX050 — Retenção.** Por quanto tempo os reportes são guardados? *Rubrica:* 3 = noventa dias;; 2 = 90;; 1 = para sempre;; 0 = nenhuma.

- **EX051 — Carga de revisão no laboratório.** Quantos dos 60 reportes precisaram de revisão humana no laboratório? *Rubrica:* 3 = 9;; 2 = 15%;; 1 = 60;; 0 = nenhuma.

<a id="ch-18"></a>

## Capítulo 18 — Controles

### Objetivos de aprendizagem

Você vai (1) implementar procedimentos de verificação para pagamentos e acesso remoto; (2) escrever procedimentos que os funcionários consigam seguir sob pressão; (3) testar os procedimentos com encenação.

### 18.1 Verificação de pagamentos

Lucas trabalha com a gerente da clínica para implementar a verificação de pagamentos. Qualquer pedido de alteração dos dados bancários de um fornecedor fica retido automaticamente no sistema contábil. Uma segunda pessoa liga para o fornecedor no número que já consta do cadastro, nunca no número do pedido. A alteração só é liberada depois da confirmação, e a ligação é registrada. Esse controle elimina a necessidade de um gestor julgar se um e-mail parece genuíno, um julgamento que atacantes habilidosos conseguem derrotar. A equipe financeira o testa primeiro com pedidos de exemplo.

### 18.2 Procedimentos claros

Lucas escreve os procedimentos para alterações de pagamento e para acesso remoto de fornecedores em cartões únicos, com etapas numeradas, frases curtas e os telefones a usar. Ele coloca os cartões ao lado dos telefones da recepção e no escritório financeiro. Evita a linguagem longa de política. Segue a ideia de aceitabilidade psicológica de Saltzer e Schroeder: se um procedimento é fácil de seguir, as pessoas o seguem. Ele também acrescenta uma linha dizendo que os funcionários sempre terão apoio por tomar tempo para verificar, mesmo que quem ligou esteja irritado.

### 18.3 Teste com encenação

Lucas testa os procedimentos com encenação. Um colega faz o papel de alguém que liga dizendo ser o fornecedor, e as recepcionistas praticam dizer que vão retornar a ligação no número oficial. Todos sabem que é treino; ninguém é enganado. As recepcionistas acham a frase roteirizada útil porque ela permite recusar com educação. Uma sugere acrescentar ao cartão o horário de suporte do fornecedor. A encenação dá confiança para as ligações reais sem os problemas éticos e o dano à confiança dos testes secretos. A sugestão é acrescentada. O treino acontece todo mês.

### Exemplo resolvido

Lucas implementa retenções de pagamento com retorno de ligação, escreve cartões de procedimento e os testa com encenação anunciada.

> **Caso sintético.** Os procedimentos são sintéticos; Saltzer e Schroeder (1975) é real.

### Erros e limites

Os cartões podem sumir. Quem liga pode ficar agressivo.

### Exercícios

- **EX052 — Número para retorno.** Para que número a segunda pessoa liga? *Rubrica:* 3 = o número que já consta do cadastro;; 2 = cadastro;; 1 = o do pedido;; 0 = nenhuma.

- **EX053 — Linha de apoio.** Que linha foi acrescentada aos cartões? *Rubrica:* 3 = os funcionários terão apoio por tomar tempo para verificar;; 2 = apoio;; 1 = nada;; 0 = nenhuma.

- **EX054 — Ética da encenação.** Por que usar encenação em vez de testes secretos? *Rubrica:* 3 = dá confiança sem engano nem dano à confiança;; 2 = ética;; 1 = nada;; 0 = nenhuma.

<a id="ch-19"></a>

## Capítulo 19 — Monitoramento

### Objetivos de aprendizagem

Você vai (1) monitorar ao longo do tempo as medidas de reporte e de verificação; (2) definir limiares simples de alerta; (3) revisar as tendências com os gestores.

### 19.1 Monitoramento contínuo

Lucas monta um monitoramento mensal das medidas escolhidas no capítulo 9: proporção de e-mails maliciosos reportados, tempo até o primeiro reporte, tempo até o veredito e alterações de pagamento retidas e verificadas. Os dados vêm da ferramenta de triagem e do log do sistema contábil, de modo que os funcionários não têm trabalho extra. Ele monta um gráfico simples para cada medida. O monitoramento mostra se as melhoras duram ou se apagam, o que importa porque muitos esforços de conscientização mostram ganhos iniciais que desaparecem em poucos meses. Ele compartilha os gráficos com todos os funcionários a cada trimestre.

### 19.2 Limiares

Lucas define limiares que disparam ação: se a mediana do tempo até o veredito passar de duas horas em qualquer mês, o prestador revisa a equipe; se a proporção reportada cair abaixo de sessenta por cento por dois meses, a equipe procura problemas como um botão quebrado. O laboratório confere seis meses de dados sintéticos contra os limiares e sinaliza um mês em que o tempo até o veredito subiu porque o prestador estava de férias. Os limiares transformam o monitoramento em ação, e não apenas em gráficos. Os dois limiares ficam escritos no procedimento.

### Laboratório — Medidas mensais contra os limiares

```python
# Monthly measures against thresholds (synthetic).
months = [(1, 0.72, 95), (2, 0.75, 80), (3, 0.78, 70), (4, 0.74, 165), (5, 0.79, 75), (6, 0.81, 65)]
for m, share, verdict in months:
    flags = (["verdict > 120"] if verdict > 120 else []) + (["share < 60%"] if share < 0.6 else [])
    print(f"month {m}: reported {share:.0%}, median verdict {verdict} min {'FLAG ' + ', '.join(flags) if flags else ''}")
```

Execute com `python3 lab_monitor.py`. Saída verificada:

```text
month 1: reported 72%, median verdict 95 min 
month 2: reported 75%, median verdict 80 min 
month 3: reported 78%, median verdict 70 min 
month 4: reported 74%, median verdict 165 min FLAG verdict > 120
month 5: reported 79%, median verdict 75 min 
month 6: reported 81%, median verdict 65 min
```

### 19.3 Revisão das tendências

Lucas revisa os gráficos com a gerente da clínica a cada trimestre. Eles discutem o mês sinalizado e combinam que uma pessoa reserva deve cuidar da triagem durante as férias. Também percebem que os reportes sobem cada vez que uma mensagem de reforço é enviada e depois se estabilizam. Esse padrão sugere que lembretes breves ajudam. Revisar as tendências juntos mantém os gestores informados e envolvidos e ajuda o programa a se ajustar antes que os problemas cresçam. Eles decidem enviar um lembrete curto todo mês, com exemplos reais recentes sem dados pessoais, e verificar depois de três meses se os reportes continuam mais altos.

### Exemplo resolvido

Lucas monitora quatro medidas por mês, define limiares de ação, sinaliza um atraso ligado às férias e combina uma reserva para a triagem.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Os limiares podem ser arbitrários. As tendências precisam de períodos mais longos.

### Exercícios

- **EX055 — Fontes de dados.** De onde vêm os dados do monitoramento? *Rubrica:* 3 = da ferramenta de triagem e do log contábil;; 2 = sistemas existentes;; 1 = questionários aos funcionários;; 0 = nenhuma.

- **EX056 — Sinalização do laboratório.** Que mês o laboratório sinalizou e por quê? *Rubrica:* 3 = o mês 4, tempo até o veredito de 165 minutos durante as férias;; 2 = mês 4;; 1 = nada;; 0 = nenhuma.

- **EX057 — Padrão dos lembretes.** Que padrão se seguiu às mensagens de reforço? *Rubrica:* 3 = os reportes subiram e depois se estabilizaram;; 2 = alta;; 1 = nada;; 0 = nenhuma.

<a id="ch-20"></a>

## Capítulo 20 — Solução de problemas

### Objetivos de aprendizagem

Você vai (1) investigar problemas no serviço de reporte; (2) separar causas técnicas de causas humanas; (3) corrigir as causas-raiz, e não os sintomas.

### 20.1 Uma queda repentina

No sétimo mês, os reportes de três clínicas caem quase a zero. Lucas investiga. Confere se os ataques diminuíram, mas os logs de filtragem mostram volume normal. Ele visita uma clínica e descobre que o botão de reporte sumiu depois que uma atualização de software reiniciou a barra de ferramentas. Os funcionários supuseram que ele tinha sido retirado de propósito e não perguntaram. A causa técnica foi a atualização; a causa humana foi a incerteza sobre se o reporte ainda era desejado. Ele confere as outras duas clínicas e encontra o mesmo problema em todos os computadores da recepção.

### 20.2 Separação das causas

Lucas lista as duas causas. Do lado técnico, o processo de atualização não confere os add-ins. Do lado humano, os funcionários não tinham um jeito fácil de avisar a TI de que algo parecia errado com a ferramenta. Ele também confere outra clínica em que os reportes caíram pouco e encontra uma causa diferente: uma recepcionista nova não tinha sido informada sobre o reporte. Separar as causas evita aplicar uma única correção a problemas de origens diferentes, o que deixaria alguns deles sem solução. Ele registra as duas causas no log, para que cada uma tenha sua correção e seu responsável.

### 20.3 Causas-raiz

Lucas corrige as causas-raiz. O prestador de TI acrescenta, depois de cada atualização, uma verificação de que o botão existe em todos os computadores. A mensagem de agradecimento agora traz uma linha convidando os funcionários a avisar a TI se o botão sumir. A integração dos novos funcionários passa a incluir o reporte. Ele registra o incidente e as correções no log de solução de problemas. Marta observa que corrigir só o botão deixaria a próxima atualização causar o mesmo problema e que convidar o retorno cria um sistema de alerta precoce. O log é revisado a cada trimestre.

### Exemplo resolvido

Lucas atribui uma queda nos reportes a uma reinicialização da barra de ferramentas e à incerteza dos funcionários, separa as causas em duas clínicas e corrige as causas-raiz.

> **Caso sintético.** O incidente é sintético.

### Erros e limites

As visitas tomam tempo. As verificações podem deixar passar outros add-ins.

### Exercícios

- **EX058 — Causa da queda.** O que causou a queda nos reportes em três clínicas? *Rubrica:* 3 = uma atualização reiniciou a barra de ferramentas e removeu o botão;; 2 = atualização;; 1 = menos ataques;; 0 = nenhuma.

- **EX059 — Causa na outra clínica.** O que causou a queda menor em outra clínica? *Rubrica:* 3 = uma recepcionista nova não foi informada sobre o reporte;; 2 = integração;; 1 = nada;; 0 = nenhuma.

- **EX060 — Verificação pós-atualização.** O que o prestador faz agora depois das atualizações? *Rubrica:* 3 = verifica se o botão existe em todos os computadores;; 2 = verificação;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060 (as de EX061–EX090 estão na edição em inglês até a tradução dos capítulos correspondentes). Lucas Ferreira, a professora Marta Kowalczyk, o Northgate Institute of Technology, o Brightwell Dental Group e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX031.** A disposição dos funcionários para reportar problemas.

**EX032.** Perto dos prazos de fechamento do mês.

**EX033.** Aceitar a alteração de um dado bancário.

**EX034.** Porque o método oficial leva minutos e o e-mail pessoal, segundos.

**EX035.** Um modelo seguro de encaminhamento com um clique.

**EX036.** As estimativas de economia de tempo.

**EX037.** A instalação de um software de acesso remoto.

**EX038.** A alteração falsa de dados bancários de fornecedor, com nota 9.

**EX039.** Retorno de ligação num número conhecido mais aprovação de um gestor.

**EX040.** Cerca de 71%.

**EX041.** Não ter certeza se a TI quer o reporte, 64 de 150 ou 43%.

**EX042.** Porque nunca teve retorno.

**EX043.** Para que o aprendizado não favoreça um dos métodos.

**EX044.** 45 segundos encaminhando e 7 segundos com o botão.

**EX045.** Os voluntários não tinham certeza se o reporte foi enviado.

**EX046.** Os logs de filtragem mostraram volume parecido.

**EX047.** 80% contra 44%.

**EX048.** Computadores mais antigos.

**EX049.** Dar nota a funcionários individualmente.

**EX050.** Noventa dias.

**EX051.** 9.

**EX052.** O número que já consta do cadastro.

**EX053.** Que os funcionários terão apoio por tomar tempo para verificar.

**EX054.** Dá confiança sem engano nem dano à confiança.

**EX055.** Da ferramenta de triagem e do log contábil.

**EX056.** O mês 4, com tempo até o veredito de 165 minutos durante as férias.

**EX057.** Os reportes subiram e depois se estabilizaram.

**EX058.** Uma atualização reiniciou a barra de ferramentas e removeu o botão.

**EX059.** Uma recepcionista nova não foi informada sobre o reporte.

**EX060.** Verifica se o botão existe em todos os computadores.

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
