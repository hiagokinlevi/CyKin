# Fatores Humanos e Política Cibernética: Curso Técnico

- Idioma: português do Brasil (`pt`); curso 052, curso técnico (18 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–9 de 18 já estão escritos em português, com os exercícios EX001–EX036 e suas resoluções com rubricas de 0 a 3 e 4 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 10–18 (EX037–EX072) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: estudantes de curso técnico que configuram, verificam, corrigem e documentam os controles de reporte e de verificação numa organização pequena.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios contam minutos com a tela desbloqueada, resumem um CSV, modelam perdas no reporte, contam barreiras de um questionário, apuram resultados de verificação, comparam tempos de reporte e efeitos do retorno e resumem reportes de motoristas, sempre sobre dados sintéticos; nenhum funcionário, cliente, e-mail ou conta real está envolvido. Os laboratórios isolados usam contas de teste e voluntários que conhecem o propósito. Nenhum phishing simulado é enviado; as regras documentadas exigem aprovação dos gestores e dos representantes dos funcionários, proíbem iscas sobre salário, saúde ou estabilidade no emprego e mantêm os resultados agregados e fora dos processos de RH. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos 1–5 tratam de sistemas, redes, identidades, scripts e escopo ao longo de um estágio numa empresa de logística; os capítulos 6–15 configuram, verificam, corrigem, automatizam e integram o reporte e a verificação, com um laboratório isolado; os capítulos 16–18 tratam de documentação e segurança, de um segundo laboratório isolado e do projeto supervisionado. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Priya Raman** | Estudante de curso técnico | Inventada |
| **Tom Hallett** | Instrutor | Inventado |
| **Eastvale Technical College** | Escola fictícia | Inventada |
| **Kestrel Logistics** | Empresa de logística fictícia, 300 funcionários, três centros de distribuição | Inventada |

### Fontes principais

Whitten e Tygar (1999), USENIX Security; Reason (1990), [doi:10.1017/CBO9781139062367](https://doi.org/10.1017/CBO9781139062367); Hansche et al. (2024), NIST SP 800-50r1; Adams e Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) |

Capítulos 10–18: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-10), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Computação e arquitetura de serviços

### Objetivos de aprendizagem

Você vai (1) descrever os sistemas usados num centro de distribuição; (2) identificar onde os funcionários interagem com a segurança durante os turnos; (3) registrar uma linha de base das tarefas de segurança.

### 1.1 Sistemas do centro de distribuição

Priya Raman, estudante de curso técnico no fictício Eastvale Technical College, entra para a equipe de suporte de TI da fictícia Kestrel Logistics, uma empresa com 300 funcionários em três centros de distribuição. Seu instrutor, Tom Hallett, pede que ela liste os sistemas que os funcionários usam. Os trabalhadores do armazém usam coletores portáteis e terminais compartilhados para registrar as entregas. O pessoal do escritório usa notebooks, e-mail e um sistema de despacho que guarda os endereços dos clientes. Os motoristas usam um aplicativo de rotas no celular. Priya desenha um diagrama simples mostrando que grupo usa que sistema e como os sistemas se conectam aos serviços em nuvem que rodam o despacho.

### 1.2 A segurança nos turnos

Priya acompanha um turno do armazém e um turno do escritório para ver onde a segurança aparece. Os trabalhadores do armazém entram nos terminais compartilhados com uma única senha da equipe escrita na parede, porque cada login toma tempo e os turnos são corridos. O pessoal do escritório recebe muitos e-mails de clientes e transportadoras, alguns com anexos e links. Os motoristas às vezes recebem mensagens de texto que dizem vir da empresa sobre mudanças de rota. Priya anota cada ponto e a pressão que os funcionários enfrentam ali, como prazos de carregamento ou clientes irritados ao telefone.

### 1.3 Registro da linha de base

Priya registra uma linha de base: número de sistemas, logins por turno, senhas compartilhadas em uso e como os funcionários hoje reportam qualquer coisa suspeita. Ela descobre que não existe um caminho claro de reporte; a maioria avisa o supervisor, que pode avisar a TI ou não. Ela escreve a linha de base como um resumo de uma página para Tom e para o líder de TI. Uma linha de base permite que a equipe meça depois se as mudanças melhoraram as coisas e mostra onde o esforço é mais necessário antes de mudar qualquer ferramenta ou política.

### Exemplo resolvido

Priya mapeia os sistemas do centro de distribuição, observa os pontos de segurança durante os turnos e registra uma linha de base que inclui uma senha compartilhada na parede e a falta de um caminho de reporte.

> **Caso sintético.** A Kestrel Logistics é sintética.

### Erros e limites

Dois turnos podem não ser típicos. As observações não devem registrar nomes.

### Exercícios

- **EX001 — Senha na parede.** Por que a senha da equipe está escrita na parede? *Rubrica:* 3 = logins individuais tomam tempo em turnos corridos;; 2 = tempo;; 1 = descuido;; 0 = nenhuma.

- **EX002 — Mensagens aos motoristas.** O que os motoristas às vezes recebem? *Rubrica:* 3 = mensagens de texto que dizem vir da empresa sobre mudanças de rota;; 2 = mensagens falsas;; 1 = nada;; 0 = nenhuma.

- **EX003 — Reporte atual.** Como os funcionários reportam hoje as mensagens suspeitas? *Rubrica:* 3 = avisam o supervisor, que pode avisar a TI;; 2 = supervisor;; 1 = um botão;; 0 = nenhuma.

- **EX004 — Propósito da linha de base.** Por que registrar uma linha de base? *Rubrica:* 3 = para medir depois se as mudanças ajudaram;; 2 = comparação;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) explicar como e-mails e mensagens de texto chegam aos funcionários; (2) descrever por que os dados do remetente podem ser falsificados; (3) configurar avisos simples.

### 2.1 Como as mensagens chegam

Os e-mails chegam à Kestrel pelo serviço de e-mail em nuvem, que os passa por um filtro antes de entregá-los. As mensagens de texto chegam aos celulares dos motoristas pelas redes móveis. Priya aprende que o remetente exibido num e-mail ou numa mensagem de texto é fácil de falsificar, porque os protocolos básicos foram projetados para entregar mensagens, não para provar quem as enviou. As verificações de autenticação de e-mail conseguem detectar algumas falsificações do próprio domínio da Kestrel, mas não conseguem barrar atacantes que registram domínios parecidos ou que enviam mensagens de texto usando o nome de uma empresa como rótulo de remetente.

### 2.2 Por que as falsificações funcionam

Priya estuda um exemplo sintético: um e-mail de um domínio que difere do da Kestrel por uma letra, pedindo ao pessoal do escritório que atualize o endereço de entrega de um cliente e envie uma cópia da fatura. Ele passa na autenticação porque o atacante é dono desse domínio parecido. Funcionários sob pressão de tempo leem o nome familiar e agem. Whitten e Tygar (1999) mostraram que as ferramentas de segurança deixam os usuários confusos quando a interface não os orienta, e Priya percebe que os funcionários precisam de sinais claros, e não de conhecimento técnico, para decidir.

### 2.3 Configuração de avisos

Com o líder de TI, Priya configura uma etiqueta de externo nos e-mails vindos de fora da Kestrel e um aviso para quando o nome de exibição de um remetente coincide com o de um funcionário, mas o endereço é externo. Ela testa os dois com mensagens sintéticas numa caixa postal de teste antes de ativá-los. Também redige uma mensagem curta para os motoristas dizendo que as mudanças de rota sempre chegam pelo aplicativo de rotas, nunca por mensagem de texto. Cada sinal dá aos funcionários uma indicação simples no momento da decisão, sem exigir que entendam os protocolos.

### Exemplo resolvido

Priya explica a entrega e a falsificação de mensagens, analisa um exemplo de domínio parecido e configura etiquetas de externo, avisos de nome e uma mensagem aos motoristas.

> **Caso sintético.** Os exemplos são sintéticos; Whitten e Tygar (1999) é real.

### Erros e limites

As etiquetas perdem efeito se usadas em excesso. Os motoristas podem não ler as mensagens.

### Exercícios

- **EX005 — Domínio parecido aprovado.** Por que o e-mail do domínio parecido passa na autenticação? *Rubrica:* 3 = o atacante é dono do domínio parecido;; 2 = propriedade;; 1 = nada;; 0 = nenhuma.

- **EX006 — Whitten e Tygar.** O que Whitten e Tygar (1999) mostraram? *Rubrica:* 3 = interfaces de segurança sem orientação confundem os usuários;; 2 = usabilidade;; 1 = nada;; 0 = nenhuma.

- **EX007 — Teste dos avisos.** Onde os avisos foram testados primeiro? *Rubrica:* 3 = numa caixa postal de teste com mensagens sintéticas;; 2 = caixa postal de teste;; 1 = caixas postais reais;; 0 = nenhuma.

- **EX008 — Regra para os motoristas.** Que regra Priya redigiu para os motoristas? *Rubrica:* 3 = as mudanças de rota só chegam pelo aplicativo de rotas;; 2 = só pelo aplicativo;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Sistemas operacionais e identidades

### Objetivos de aprendizagem

Você vai (1) substituir a senha compartilhada de um terminal por logins individuais utilizáveis; (2) configurar bloqueios de tela para o trabalho no armazém; (3) gerenciar contas de funcionários temporários.

### 3.1 Logins individuais

Priya propõe substituir a senha da parede por logins com crachá nos terminais do armazém. Cada trabalhador encosta o crachá para entrar e encosta de novo para sair, o que leva cerca de dois segundos. Os logins individuais permitem à TI ver quem fez cada alteração, o que ajuda a investigar erros e uso indevido. Ela testa os leitores de crachá num terminal durante uma semana. Os trabalhadores acham o toque mais rápido do que digitar a senha compartilhada. Tornar a opção segura mais rápida do que a insegura é a chave para a adoção. Os supervisores apoiam o teste.

### 3.2 Bloqueios de tela

Os terminais compartilhados ficavam conectados o turno inteiro. Com os logins por crachá, Priya configura os terminais para bloquear depois de dois minutos de inatividade, já que desbloquear agora custa um toque. Os notebooks do escritório bloqueiam depois de cinco minutos e desbloqueiam com digital ou PIN. Ela conta quantas vezes os terminais ficaram desbloqueados antes e depois, ao longo de uma semana de teste. O tempo curto de bloqueio é aceito porque o custo de desbloquear é pequeno, o que mostra como usabilidade e segurança podem se reforçar. Os supervisores concordam com as configurações.

### Laboratório — Minutos de terminais desbloqueados antes e depois dos crachás

```python
# Unlocked terminal minutes per test week before and after badge logins (synthetic, 4 terminals).
before = [480, 500, 460, 480]; after = [20, 25, 18, 22]
print("before:", sum(before), "after:", sum(after))
```

Execute com `python3 lab_unlocked.py`. Saída verificada:

```text
before: 1920 after: 85
```

### 3.3 Funcionários temporários

A Kestrel contrata cinquenta trabalhadores temporários a cada inverno. Antes, eles compartilhavam contas. Priya monta um processo: o RH envia uma lista antes de cada temporada, a TI cria as contas com data de término, os crachás são entregues na integração e as contas expiram automaticamente na data de término. Ela escreve um checklist para o RH e a TI. Os temporários recebem uma integração de dois minutos sobre reporte e crachás. A expiração automática elimina o risco de contas antigas continuarem ativas, que de outro modo ninguém se lembraria de remover. O RH concorda com o checklist.

### Exemplo resolvido

Priya substitui uma senha compartilhada por logins com crachá, encurta os bloqueios de tela e monta contas com expiração para os trabalhadores temporários.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Crachás podem ser perdidos ou compartilhados. As datas de término podem precisar de prorrogação.

### Exercícios

- **EX009 — Tempo do crachá.** Quanto tempo leva um login com crachá? *Rubrica:* 3 = cerca de dois segundos;; 2 = 2 segundos;; 1 = nada;; 0 = nenhuma.

- **EX010 — Minutos desbloqueados no laboratório.** Como mudaram os minutos desbloqueados no laboratório? *Rubrica:* 3 = de 1.920 para 85 por semana;; 2 = queda;; 1 = nada;; 0 = nenhuma.

- **EX011 — Aceitação do bloqueio.** Por que um bloqueio de dois minutos é aceito? *Rubrica:* 3 = desbloquear só exige um toque;; 2 = custo baixo;; 1 = nada;; 0 = nenhuma.

- **EX012 — Expiração dos temporários.** Como terminam as contas dos temporários? *Rubrica:* 3 = expiram automaticamente numa data de término;; 2 = expiração;; 1 = remoção manual;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Scripts e formatos de dados

### Objetivos de aprendizagem

Você vai (1) escrever um script para resumir reportes a partir de um arquivo CSV; (2) usar JSON para configuração; (3) evitar guardar dados pessoais sem necessidade.

### 4.1 Resumo dos reportes

Assim que existe uma caixa postal de reporte, Priya escreve um script em Python que lê uma exportação semanal em CSV com data, centro de distribuição, categoria e veredito, e imprime as contagens por centro e por categoria. Ela usa o módulo csv do Python para que as vírgulas dentro dos campos sejam tratadas corretamente. Testa o script num arquivo pequeno cujos totais ela conhece. O resumo substitui uma contagem manual que tomava uma hora por semana do líder de TI e muitas vezes tinha erros, liberando tempo para responder a quem reporta. O líder de TI confere a primeira saída.

### Laboratório — Resumo semanal dos reportes a partir do CSV

```python
# Weekly report summary from CSV (synthetic).
import csv, io, json
cfg = json.loads('{"depots": ["North", "South", "East"]}')
data = "date,depot,category,verdict\n" + "".join(f"2026-10-0{1 + i % 5},{d},{c},{v}\n" for i, (d, c, v) in enumerate(
    [("North", "fake carrier", "malicious")] * 7 + [("North", "newsletter", "harmless")] * 5 +
    [("South", "fake invoice", "malicious")] * 4 + [("South", "other", "harmless")] * 3 + [("East", "fake carrier", "malicious")] * 5))
counts = {d: 0 for d in cfg["depots"]}
for row in csv.DictReader(io.StringIO(data)): counts[row["depot"]] += 1
print(counts, "total", sum(counts.values()))
```

Execute com `python3 lab_weekly.py`. Saída verificada:

```text
{'North': 12, 'South': 7, 'East': 5} total 24
```

### 4.2 Configuração em JSON

Priya guarda as configurações, como os nomes dos centros de distribuição e os rótulos das categorias, num arquivo JSON, e não dentro do script. JSON é um formato de texto simples, de nomes e valores, que tanto pessoas quanto programas conseguem ler. Quando um novo centro abre, o líder de TI atualiza o arquivo JSON sem mexer no código. Separar a configuração do código torna os scripts mais fáceis de manter e reduz a chance de erros quando alguém com menos familiaridade com programação precisa fazer uma alteração. Ela acrescenta um arquivo curto de exemplo.

### 4.3 Evitar dados pessoais

A primeira exportação que Priya recebe inclui os endereços de e-mail de quem reportou. Ela pede que sejam removidos, porque o resumo só precisa das contagens por centro, e os nomes poderiam fazer os funcionários se sentirem monitorados. A exportação passa a trazer um código aleatório no lugar. Ela guarda os arquivos numa pasta restrita e os apaga depois de quatro semanas. A boa prática em scripts inclui pensar em que dados o script manipula e se ele precisa deles. O líder de TI concorda com a mudança e a registra nas notas de tratamento de dados, e Tom a elogia por levantar a questão cedo.

### Exemplo resolvido

Priya escreve um script de resumo do CSV, leva as configurações para JSON e remove da exportação os endereços de quem reporta.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

As exportações podem mudar de formato. Às vezes é possível vincular os códigos aleatórios.

### Exercícios

- **EX013 — Motivo do módulo csv.** Por que usar o módulo csv do Python? *Rubrica:* 3 = trata as vírgulas dentro dos campos;; 2 = parsing;; 1 = split;; 0 = nenhuma.

- **EX014 — Centro principal no laboratório.** Que centro de distribuição teve mais reportes no laboratório? *Rubrica:* 3 = North, com 12;; 2 = North;; 1 = nada;; 0 = nenhuma.

- **EX015 — Vantagem do JSON.** Por que guardar as configurações em JSON? *Rubrica:* 3 = as mudanças não exigem editar o código;; 2 = manutenibilidade;; 1 = nada;; 0 = nenhuma.

- **EX016 — Campo removido.** Que campo foi removido da exportação? *Rubrica:* 3 = os endereços de e-mail de quem reporta;; 2 = endereços;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Escopo e evidências de segurança

### Objetivos de aprendizagem

Você vai (1) definir o escopo de uma tarefa técnica de fatores humanos; (2) acordar permissões e limites; (3) coletar evidências que apoiem as decisões.

### 5.1 Definição do escopo

Tom pede a Priya que defina o escopo do trabalho dela: melhorar o modo como os funcionários da Kestrel reportam mensagens suspeitas e verificam pedidos incomuns. Estão no escopo a caixa postal de reporte, as configurações de aviso, os procedimentos de verificação e orientações curtas. Ficam fora do escopo as questões disciplinares, o monitoramento de funcionários individuais e qualquer teste que engane os funcionários sem acordo. Pôr o escopo por escrito protege os funcionários, a empresa e a própria Priya, porque todos sabem o que ela vai e o que não vai fazer durante o estágio. Tom e o líder de TI assinam o documento de escopo.

### 5.2 Permissões e limites

Priya obtém permissão por escrito do líder de TI e do gerente de operações para cada atividade, como instalar leitores de crachá ou fazer testes de usabilidade com voluntários. Os representantes dos funcionários são informados. Ela acorda os limites: os testes usam caixas postais de teste e mensagens sintéticas; nenhum phishing simulado é enviado durante o estágio; e todos os dados são reportados de forma agregada. O NIST SP 800-50r1 (Hansche et al., 2024) enfatiza o planejamento e a governança nos programas de aprendizagem, e a permissão é o primeiro passo dessa governança. Cada permissão é arquivada.

### 5.3 Coleta de evidências

Priya coleta evidências para apoiar as decisões: contagens da exportação de reportes, testes de tempo dos procedimentos, questionários curtos e notas de observação sem nomes. Ela registra a fonte e a data de cada item. Quando recomenda uma mudança, aponta a evidência por trás dela. Recomendações baseadas em evidências são mais fáceis de os gestores aceitarem e de revisarem depois. Ela também registra as evidências que contrariam suas expectativas, como a preferência dos funcionários por lembretes por e-mail, porque escondê-las induziria a erro. Ela guarda todos os itens numa única pasta datada.

### Exemplo resolvido

Priya escreve o escopo, obtém permissões com limites e coleta evidências datadas, incluindo achados que a contrariam.

> **Caso sintético.** O escopo é sintético; o SP 800-50r1 é real.

### Erros e limites

Expansão do escopo. A coleta de evidências toma tempo.

### Exercícios

- **EX017 — Fora do escopo.** Cite um item fora do escopo. *Rubrica:* 3 = o monitoramento de funcionários individuais;; 2 = monitoramento;; 1 = caixa postal de reporte;; 0 = nenhuma.

- **EX018 — Limite das simulações.** Que limite vale para o phishing simulado? *Rubrica:* 3 = nenhum é enviado durante o estágio;; 2 = nenhum;; 1 = mensal;; 0 = nenhuma.

- **EX019 — Registro das evidências.** O que Priya registra com cada item de evidência? *Rubrica:* 3 = a fonte e a data;; 2 = procedência;; 1 = nada;; 0 = nenhuma.

- **EX020 — Evidências contrárias.** Por que registrar as evidências contrárias? *Rubrica:* 3 = escondê-las induziria a erro;; 2 = honestidade;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Fatores humanos e política cibernética: modelo do sistema

### Objetivos de aprendizagem

Você vai (1) modelar o processo de reporte, da chegada da mensagem ao retorno; (2) identificar as etapas em que os reportes se perdem; (3) escolher melhorias por etapa.

### 6.1 O processo

Priya modela o reporte na Kestrel como uma série de etapas: uma mensagem suspeita chega; a pessoa percebe; decide reportar; descobre como reportar; envia; a TI revisa; a TI responde. Se qualquer etapa falha, o alerta nunca chega à TI ou quem reportou nunca fica sabendo se estava certo. Ela desenha o processo com setas e acrescenta onde cada etapa acontece, como num terminal do armazém, num notebook do escritório ou no celular de um motorista. Tom revisa o desenho. Ele sugere rótulos.

### 6.2 Onde os reportes se perdem

Usando as respostas do questionário e a exportação de reportes, Priya estima quantos reportes potenciais sobrevivem a cada etapa. Muitos funcionários percebem as mensagens suspeitas, mas menos decidem reportar, porque não têm certeza se a TI as quer. Alguns não conseguem descobrir como reportar pelo celular. O laboratório multiplica as taxas das etapas para estimar quantas de cada cem mensagens suspeitas viram reportes com resposta. A maior perda está na etapa de decisão, o que lhe diz onde a melhoria mais importa. Ela compartilha o resultado com o líder de TI.

### Laboratório — Perdas no processo de reporte por etapa

```python
# Reporting process losses by step for 100 suspicious messages (synthetic).
steps = [("notice", 0.75), ("decide", 0.40), ("find how", 0.80), ("send", 0.98), ("IT review", 0.95), ("reply", 0.95)]
n = 100.0
for s, r in steps: n2 = n * r; print(f"{s}: {n:.0f} -> {n2:.0f}"); n = n2
print(f"replied reports: {n:.0f}")
```

Execute com `python3 lab_steps.py`. Saída verificada:

```text
notice: 100 -> 75
decide: 75 -> 30
find how: 30 -> 24
send: 24 -> 24
IT review: 24 -> 22
reply: 22 -> 21
replied reports: 21
```

### 6.3 Melhorias por etapa

Priya escolhe melhorias por etapa. Para a etapa de decisão, uma mensagem clara dos gestores de que reportes na dúvida são bem-vindos. Para descobrir como reportar, um botão de reporte no e-mail e um número curto para os motoristas. Para o retorno, respostas em até um dia útil. Ela estima que corrigir a etapa de decisão acrescentaria mais reportes do que as outras duas juntas. Modelar o processo transforma uma preocupação vaga com a conscientização dos funcionários em mudanças específicas e direcionadas. O gerente de operações aprova as três mudanças. O trabalho começa na semana seguinte.

### Exemplo resolvido

Priya modela o reporte em sete etapas, descobre que a etapa de decisão é a que mais perde e direciona as melhorias por etapa.

> **Caso sintético.** As taxas são sintéticas.

### Erros e limites

As taxas das etapas são estimativas. As etapas interagem.

### Exercícios

- **EX021 — Número de etapas.** Quantas etapas tem o modelo de Priya? *Rubrica:* 3 = sete;; 2 = 7;; 1 = três;; 0 = nenhuma.

- **EX022 — Sobreviventes no laboratório.** Quantas de 100 mensagens suspeitas viram reportes com resposta no laboratório? *Rubrica:* 3 = 21;; 2 = 21;; 1 = nada;; 0 = nenhuma.

- **EX023 — Maior perda.** Que etapa perde mais? *Rubrica:* 3 = a decisão de reportar;; 2 = decisão;; 1 = perceber;; 0 = nenhuma.

- **EX024 — Correção da decisão.** O que corrige a etapa de decisão? *Rubrica:* 3 = os gestores dizerem que reportes na dúvida são bem-vindos;; 2 = mensagem;; 1 = nada;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Fatores humanos e política cibernética: dados e telemetria

### Objetivos de aprendizagem

Você vai (1) identificar as fontes de dados para o reporte e a verificação; (2) definir que telemetria coletar; (3) respeitar a privacidade na telemetria.

### 7.1 Fontes de dados

Priya lista as fontes de dados para monitorar o lado humano da segurança na Kestrel: a exportação da caixa postal de reporte, os logs do filtro de e-mail com as mensagens maliciosas bloqueadas e entregues, o log do sistema contábil com as alterações de pagamento retidas, os chamados do help desk e questionários trimestrais curtos. Cada fonte responde a perguntas diferentes. Juntas, mostram quantos ataques chegam aos funcionários, quantos são reportados, com que rapidez a TI responde e se os controles de verificação estão sendo usados como previsto. Ela lista cada fonte numa tabela curta. Nenhuma exige software novo.

### 7.2 Escolha da telemetria

Telemetria são dados coletados automaticamente dos sistemas. Priya define um conjunto pequeno: a hora em que cada mensagem maliciosa foi entregue; a hora do primeiro reporte; a hora do veredito; o número de alterações de pagamento retidas e seu desfecho; e a contagem de logins com crachá por terminal por turno. Ela evita coletar qualquer coisa que não esteja ligada a uma decisão. Coletar dados demais acrescenta armazenamento, custo e risco à privacidade sem melhorar as decisões, e pode fazer os funcionários se sentirem vigiados. O líder de TI concorda com a lista. Cada item tem um propósito declarado.

### 7.3 Privacidade na telemetria

Os dados de login com crachá poderiam mostrar quando cada pessoa trabalhou, o que poderia ser usado indevidamente para monitorar a produtividade. Priya propõe que os dados de crachá sejam usados apenas em investigações de segurança e em contagens agregadas, com acesso restrito à TI e uma declaração clara no aviso de privacidade aos funcionários. Os dados de reporte não têm nomes. O gerente de operações concorda por escrito. Respeitar a privacidade na telemetria preserva a confiança da qual o programa de reporte depende e impede que os dados de segurança derivem para usos com os quais os funcionários nunca concordaram. Os funcionários são informados.

### Exemplo resolvido

Priya lista as fontes de dados, define uma telemetria mínima e limita o uso dos dados de crachá com um acordo por escrito.

> **Caso sintético.** Os usos dos dados são sintéticos.

### Erros e limites

Acordos podem ser esquecidos. Os logs podem estar incompletos.

### Exercícios

- **EX025 — Definição de telemetria.** O que é telemetria? *Rubrica:* 3 = dados coletados automaticamente dos sistemas;; 2 = automáticos;; 1 = questionários;; 0 = nenhuma.

- **EX026 — Regra de coleta.** Que regra orienta a coleta de telemetria? *Rubrica:* 3 = coletar só o que está ligado a uma decisão;; 2 = mínimo;; 1 = tudo;; 0 = nenhuma.

- **EX027 — Risco dos dados de crachá.** Que uso indevido os dados de crachá permitiriam? *Rubrica:* 3 = monitorar a produtividade;; 2 = vigilância;; 1 = nada;; 0 = nenhuma.

- **EX028 — Limite dos dados de crachá.** A que se limitam os dados de crachá? *Rubrica:* 3 = investigações de segurança e contagens agregadas;; 2 = uso limitado;; 1 = nada;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Fatores humanos e política cibernética: modos de falha

### Objetivos de aprendizagem

Você vai (1) identificar modos de falha ligados às pessoas; (2) distinguir deslizes, lapsos e enganos; (3) associar defesas aos tipos de falha.

### 8.1 Modos de falha

Priya lista as maneiras pelas quais o lado humano da segurança pode falhar na Kestrel: um despachante clica num link de um e-mail falso de transportadora; um motorista segue uma mensagem de texto falsa até uma página falsa de login; um auxiliar de contas altera os dados bancários de um cliente depois de um e-mail convincente; um supervisor esquece de avisar a TI sobre uma ligação suspeita. Cada falha tem causas diferentes. Listar as falhas antes que aconteçam permite à equipe desenhar as defesas com antecedência, em vez de reagir depois do dano. Os supervisores acrescentam mais duas.

### 8.2 Deslizes, lapsos, enganos

Reason (1990) distinguiu os deslizes (slips), em que uma ação dá errado apesar de um plano correto, como clicar no botão errado; os lapsos (lapses), em que algo é esquecido, como não repassar um reporte; e os enganos (mistakes), em que o próprio plano está errado, como acreditar que um e-mail falso é genuíno. Priya classifica cada modo de falha. O reporte esquecido pelo supervisor é um lapso; a alteração dos dados bancários é um engano causado por fraude. A classificação orienta a escolha da defesa. Ela explica os termos aos supervisores.

### 8.3 Associação das defesas

Os deslizes são reduzidos pelo design, como etapas de confirmação para ações arriscadas. Os lapsos são reduzidos eliminando as exigências de memória, como um botão de reporte que envia direto à TI em vez de passar pelos supervisores. Os enganos causados por fraude são reduzidos por procedimentos de verificação que não dependem de julgar a aparência, como ligar para o cliente num número conhecido. Priya apresenta uma tabela que associa cada falha a um tipo de defesa, o que mostra aos gestores que mais treinamento não é a resposta para todas as falhas.

### Exemplo resolvido

Priya lista quatro modos de falha, classifica-os com os deslizes, lapsos e enganos de Reason e associa cada um a um tipo de defesa.

> **Caso sintético.** As falhas são sintéticas; Reason (1990) é real.

### Erros e limites

As classificações se sobrepõem. As defesas têm efeitos colaterais.

### Exercícios

- **EX029 — Exemplo de lapso.** Que falha é um lapso? *Rubrica:* 3 = o supervisor esquecer de avisar a TI;; 2 = esquecimento;; 1 = a alteração bancária;; 0 = nenhuma.

- **EX030 — Definição de engano.** O que é um engano nos termos de Reason? *Rubrica:* 3 = o próprio plano está errado;; 2 = plano errado;; 1 = ação errada;; 0 = nenhuma.

- **EX031 — Defesa contra lapsos.** Como os lapsos são reduzidos? *Rubrica:* 3 = eliminando as exigências de memória;; 2 = memória;; 1 = treinamento;; 0 = nenhuma.

- **EX032 — Defesa contra a fraude.** O que reduz os enganos causados por fraude? *Rubrica:* 3 = verificação que não se baseia na aparência;; 2 = retornos de ligação;; 1 = nada;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Fatores humanos e política cibernética: ferramentas e métodos

### Objetivos de aprendizagem

Você vai (1) usar um questionário curto e a observação para estudar o reporte; (2) fazer um teste de usabilidade simples; (3) combinar os métodos em achados.

### 9.1 Questionário e observação

Priya aplica um questionário anônimo de cinco perguntas a todos os funcionários e observa como o reporte acontece em cada centro de distribuição, com permissão e sem registrar nomes. Ela recebe 210 respostas de 300 funcionários. A barreira mais comum é não saber como reportar a partir de um terminal ou do celular. A observação mostra que os terminais do armazém não têm cliente de e-mail, de modo que os trabalhadores não têm como reportar uma mensagem suspeita que veem numa tela compartilhada, como um pop-up que diz vir da TI. Ela redige suas notas no mesmo dia.

### Laboratório — Barreiras no questionário entre 210 respostas

```python
# Barriers among 210 synthetic survey responses (multiple choice).
b = {"don't know how from terminal or phone": 88, "unsure IT wants it": 71, "too busy": 52, "never heard back": 30}
for k, v in sorted(b.items(), key=lambda x: -x[1]): print(f"{k}: {v}/210 = {v / 210:.0%}")
```

Execute com `python3 lab_survey.py`. Saída verificada:

```text
don't know how from terminal or phone: 88/210 = 42%
unsure IT wants it: 71/210 = 34%
too busy: 52/210 = 25%
never heard back: 30/210 = 14%
```

### 9.2 Teste de usabilidade

Priya testa um método de reporte proposto para os terminais do armazém: um atalho na área de trabalho que abre um formulário curto. Seis trabalhadores voluntários o experimentam com pop-ups sintéticos num terminal de teste, sabendo que estão testando o formulário. Cinco concluem o reporte em menos de vinte segundos; um se confunde com a palavra incidente. Ela muda o rótulo para Reportar algo estranho. Testes de usabilidade pequenos captam problemas de redação que os projetistas não percebem, porque já sabem o que quiseram dizer. Depois disso, os seis têm sucesso. O teste leva uma hora.

### 9.3 Combinação dos métodos

Priya combina o questionário, a observação e o teste em achados: os funcionários querem reportar, mas não têm um caminho nos terminais e nos celulares; a palavra incidente afasta as pessoas; e muitos não têm certeza se a TI quer os reportes. Ela propõe o formulário no terminal, um número de texto para os motoristas e uma mensagem clara de boas-vindas dos gestores. Cada achado cita sua evidência. Combinar métodos dá um retrato mais completo do que qualquer método sozinho, porque os questionários contam, a observação revela o contexto e os testes conferem as soluções. O gerente de operações aprova as propostas. O trabalho começa logo.

### Exemplo resolvido

Priya aplica o questionário a 210 funcionários, observa os centros de distribuição, testa um formulário de terminal com seis voluntários e combina os métodos em achados.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

Viés de autodeclaração. Testes pequenos.

### Exercícios

- **EX033 — Taxa de resposta.** Qual foi a taxa de resposta do questionário? *Rubrica:* 3 = 70%;; 2 = 210 de 300;; 1 = 210%;; 0 = nenhuma.

- **EX034 — Barreira principal no laboratório.** Qual foi a principal barreira no laboratório? *Rubrica:* 3 = não saber como reportar pelos terminais ou celulares, 88 de 210;; 2 = como;; 1 = nada;; 0 = nenhuma.

- **EX035 — Lacuna dos terminais.** Por que os trabalhadores do armazém não conseguiam reportar? *Rubrica:* 3 = os terminais não têm cliente de e-mail;; 2 = sem caminho;; 1 = nada;; 0 = nenhuma.

- **EX036 — Mudança de rótulo.** Que rótulo substituiu incidente? *Rubrica:* 3 = Reportar algo estranho;; 2 = palavras simples;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX036 (as de EX037–EX072 estão na edição em inglês até a tradução dos capítulos correspondentes). Priya Raman, Tom Hallett, o Eastvale Technical College, a Kestrel Logistics e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Porque cada login toma tempo e os turnos são corridos.

**EX002.** Mensagens de texto que dizem vir da empresa sobre mudanças de rota.

**EX003.** Avisam o supervisor, que pode avisar a TI ou não.

**EX004.** Para que a equipe possa medir depois se as mudanças melhoraram as coisas.

**EX005.** Porque o atacante é dono do domínio parecido, de modo que suas mensagens se autenticam.

**EX006.** Que as ferramentas de segurança confundem os usuários quando as interfaces não os orientam.

**EX007.** Numa caixa postal de teste, com mensagens sintéticas.

**EX008.** Que as mudanças de rota sempre chegam pelo aplicativo de rotas, nunca por mensagem de texto.

**EX009.** Cerca de dois segundos.

**EX010.** De 1.920 para 85 minutos desbloqueados por semana.

**EX011.** Porque desbloquear só exige um toque do crachá.

**EX012.** Expiram automaticamente numa data de término definida.

**EX013.** Porque trata corretamente os campos entre aspas e as vírgulas dentro deles.

**EX014.** O centro North, com 12 reportes.

**EX015.** Para que as configurações possam ser atualizadas sem mexer no código.

**EX016.** Os endereços de e-mail de quem reporta.

**EX017.** Questões disciplinares, monitoramento de funcionários individuais ou testes enganosos sem acordo.

**EX018.** Nenhum phishing simulado é enviado durante o estágio.

**EX019.** A fonte e a data.

**EX020.** Porque escondê-las induziria a erro quem decide.

**EX021.** Sete, da chegada à resposta.

**EX022.** Cerca de 21 de cada 100.

**EX023.** A etapa de decisão.

**EX024.** Uma mensagem clara dos gestores de que reportes na dúvida são bem-vindos.

**EX025.** Dados coletados automaticamente dos sistemas.

**EX026.** Coletar apenas dados ligados a uma decisão.

**EX027.** Monitorar quando cada pessoa trabalhou, para fins de produtividade.

**EX028.** Investigações de segurança e contagens agregadas, com acesso apenas da TI.

**EX029.** O supervisor esquecer de repassar uma ligação suspeita.

**EX030.** Uma falha em que o próprio plano está errado, como confiar num e-mail falso.

**EX031.** Eliminando as exigências de memória, como no reporte direto.

**EX032.** Procedimentos de verificação que não dependem de julgar a aparência.

**EX033.** 70%, já que 210 de 300 funcionários responderam.

**EX034.** Não saber como reportar a partir de um terminal ou do celular, escolhida por 88 de 210 (42%).

**EX035.** Porque os terminais do armazém não têm cliente de e-mail.

**EX036.** Reportar algo estranho.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- European Union Agency for Cybersecurity. (2019). *Cybersecurity culture guidelines: Behavioural aspects of cybersecurity*. ENISA. <https://www.enisa.europa.eu/publications/cybersecurity-culture-guidelines-behavioural-aspects-of-cybersecurity>
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Reason, J. (1990). *Human error*. Cambridge University Press. <https://doi.org/10.1017/CBO9781139062367>
- Whitten, A., & Tygar, J. D. (1999). Why Johnny can't encrypt: A usability evaluation of PGP 5.0. *Proceedings of the 8th USENIX Security Symposium*. USENIX. <https://www.usenix.org/conference/8th-usenix-security-symposium/why-johnny-cant-encrypt-usability-evaluation-pgp-50>
