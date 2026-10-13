# Fatores Humanos e Política Cibernética: Curso Técnico

- Idioma: português do Brasil (`pt`); curso 052, curso técnico (18 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–18 de 18 têm texto didático escrito à mão na edição em inglês; os exercícios EX001–EX072 têm resoluções correspondentes com rubricas de 0 a 3; os nove laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

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

- **EX002 — Mensagens aos motoristas.** O que os motoristas às vezes recebem? *Rubrica:* 3 = mensagens de texto que dizem vir da empresa sobre mudanças de rota;; 2 = mensagens falsas;; 1 = vago;; 0 = nenhuma.

- **EX003 — Reporte atual.** Como os funcionários reportam hoje as mensagens suspeitas? *Rubrica:* 3 = avisam o supervisor, que pode avisar a TI;; 2 = supervisor;; 1 = um botão;; 0 = nenhuma.

- **EX004 — Propósito da linha de base.** Por que registrar uma linha de base? *Rubrica:* 3 = para medir depois se as mudanças ajudaram;; 2 = comparação;; 1 = vago;; 0 = nenhuma.

### Síntese

Uma linha de base dos sistemas e das pressões dos turnos mostra onde a segurança centrada nas pessoas é necessária.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — aula 01 (capítulo 01 de 18)

[← Início do curso](../../README.md) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

- **EX005 — Domínio parecido aprovado.** Por que o e-mail do domínio parecido passa na autenticação? *Rubrica:* 3 = o atacante é dono do domínio parecido;; 2 = propriedade;; 1 = vago;; 0 = nenhuma.

- **EX006 — Whitten e Tygar.** O que Whitten e Tygar (1999) mostraram? *Rubrica:* 3 = interfaces de segurança sem orientação confundem os usuários;; 2 = usabilidade;; 1 = vago;; 0 = nenhuma.

- **EX007 — Teste dos avisos.** Onde os avisos foram testados primeiro? *Rubrica:* 3 = numa caixa postal de teste com mensagens sintéticas;; 2 = caixa postal de teste;; 1 = caixas postais reais;; 0 = nenhuma.

- **EX008 — Regra para os motoristas.** Que regra Priya redigiu para os motoristas? *Rubrica:* 3 = as mudanças de rota só chegam pelo aplicativo de rotas;; 2 = só pelo aplicativo;; 1 = vago;; 0 = nenhuma.

### Síntese

Os limites dos protocolos deixam a equipe julgando as mensagens; por isso, sinais simples precisam orientá-la.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — aula 02 (capítulo 02 de 18)

[← Capítulo 01](#ch-01) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

- **EX009 — Tempo do crachá.** Quanto tempo leva um login com crachá? *Rubrica:* 3 = cerca de dois segundos;; 2 = 2 segundos;; 1 = vago;; 0 = nenhuma.

- **EX010 — Minutos desbloqueados no laboratório.** Como mudaram os minutos desbloqueados no laboratório? *Rubrica:* 3 = de 1.920 para 85 por semana;; 2 = queda;; 1 = vago;; 0 = nenhuma.

- **EX011 — Aceitação do bloqueio.** Por que um bloqueio de dois minutos é aceito? *Rubrica:* 3 = desbloquear só exige um toque;; 2 = custo baixo;; 1 = vago;; 0 = nenhuma.

- **EX012 — Expiração dos temporários.** Como terminam as contas dos temporários? *Rubrica:* 3 = expiram automaticamente numa data de término;; 2 = expiração;; 1 = remoção manual;; 0 = nenhuma.

### Síntese

Identidades utilizáveis tornam a opção segura a mais rápida.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — aula 03 (capítulo 03 de 18)

[← Capítulo 02](#ch-02) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

- **EX014 — Centro principal no laboratório.** Que centro de distribuição teve mais reportes no laboratório? *Rubrica:* 3 = North, com 12;; 2 = North;; 1 = vago;; 0 = nenhuma.

- **EX015 — Vantagem do JSON.** Por que guardar as configurações em JSON? *Rubrica:* 3 = as mudanças não exigem editar o código;; 2 = manutenibilidade;; 1 = vago;; 0 = nenhuma.

- **EX016 — Campo removido.** Que campo foi removido da exportação? *Rubrica:* 3 = os endereços de e-mail de quem reporta;; 2 = endereços;; 1 = vago;; 0 = nenhuma.

### Síntese

Os scripts devem ser testados, configuráveis e cuidadosos com os dados pessoais.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — aula 04 (capítulo 04 de 18)

[← Capítulo 03](#ch-03) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

- **EX018 — Limite das simulações.** Que limite vale para o phishing simulado? *Rubrica:* 3 = nenhum phishing simulado durante o estágio;; 2 = nenhum phishing simulado, sem o limite do estágio;; 1 = mensal;; 0 = sem resposta.

- **EX019 — Registro das evidências.** O que Priya registra com cada item de evidência? *Rubrica:* 3 = a fonte e a data;; 2 = procedência;; 1 = vago;; 0 = nenhuma.

- **EX020 — Evidências contrárias.** Por que registrar as evidências contrárias? *Rubrica:* 3 = escondê-las induziria a erro;; 2 = honestidade;; 1 = vago;; 0 = nenhuma.

### Síntese

Escopo claro, permissão e evidências protegem as pessoas e sustentam decisões sólidas.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — aula 05 (capítulo 05 de 18)

[← Capítulo 04](#ch-04) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

- **EX022 — Sobreviventes no laboratório.** Quantas de 100 mensagens suspeitas viram reportes com resposta no laboratório? *Rubrica:* 3 = cerca de 21;; 2 = um número próximo de 21 (15 a 25);; 1 = vago;; 0 = nenhuma.

- **EX023 — Maior perda.** Que etapa perde mais? *Rubrica:* 3 = a decisão de reportar;; 2 = decisão;; 1 = perceber;; 0 = nenhuma.

- **EX024 — Correção da decisão.** O que corrige a etapa de decisão? *Rubrica:* 3 = os gestores dizerem que reportes na dúvida são bem-vindos;; 2 = mensagem;; 1 = vago;; 0 = nenhuma.

### Síntese

Um modelo por etapas mostra onde os reportes se perdem e qual correção importa mais.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — aula 06 (capítulo 06 de 18)

[← Capítulo 05](#ch-05) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

- **EX027 — Risco dos dados de crachá.** Que uso indevido os dados de crachá permitiriam? *Rubrica:* 3 = monitorar a produtividade;; 2 = vigilância;; 1 = vago;; 0 = nenhuma.

- **EX028 — Limite dos dados de crachá.** A que se limitam os dados de crachá? *Rubrica:* 3 = investigações de segurança e contagens agregadas;; 2 = uso limitado;; 1 = vago;; 0 = nenhuma.

### Síntese

Uma telemetria mínima, usada apenas para fins acordados, sustenta o monitoramento sem corroer a confiança.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — aula 07 (capítulo 07 de 18)

[← Capítulo 06](#ch-06) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

- **EX032 — Defesa contra a fraude.** O que reduz os enganos causados por fraude? *Rubrica:* 3 = verificação que não se baseia na aparência;; 2 = retornos de ligação;; 1 = vago;; 0 = nenhuma.

### Síntese

Classificar as falhas humanas aponta defesas adequadas, que vão além de mais treinamento.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — aula 08 (capítulo 08 de 18)

[← Capítulo 07](#ch-07) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

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

- **EX034 — Barreira principal no laboratório.** Qual foi a principal barreira no laboratório? *Rubrica:* 3 = não saber como reportar pelos terminais ou celulares, 88 de 210;; 2 = como;; 1 = vago;; 0 = nenhuma.

- **EX035 — Lacuna dos terminais.** Por que os trabalhadores do armazém não conseguiam reportar? *Rubrica:* 3 = os terminais não têm cliente de e-mail;; 2 = sem caminho;; 1 = vago;; 0 = nenhuma.

- **EX036 — Mudança de rótulo.** Que rótulo substituiu incidente? *Rubrica:* 3 = Reportar algo estranho;; 2 = palavras simples;; 1 = vago;; 0 = nenhuma.

### Síntese

Métodos combinados revelam barreiras e testam correções antes da implantação.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — aula 09 (capítulo 09 de 18)

[← Capítulo 08](#ch-08) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Fatores humanos e política cibernética: configuração de controles

### Objetivos de aprendizagem

Você vai (1) configurar caminhos de reporte para e-mail, terminais e celulares; (2) montar controles de verificação para alterações de pagamento e de endereço; (3) documentar as configurações com clareza.

### 10.1 Caminhos de reporte

Priya configura três caminhos de reporte. No e-mail, um botão de reporte envia a mensagem para a caixa postal compartilhada da TI e mostra na hora uma nota de agradecimento. Nos terminais do armazém, o atalho na área de trabalho abre o formulário com o rótulo Reportar algo estranho, que pede uma descrição curta e o número do terminal, sem exigir nome. Para os motoristas, um número curto da empresa recebe as mensagens de texto encaminhadas. Ela testa cada caminho de ponta a ponta com mensagens sintéticas e confirma que os três chegam à mesma fila de triagem da equipe de TI.

### 10.2 Controles de verificação

Pedidos falsos para alterar os endereços de entrega ou os dados bancários dos clientes são um risco importante na Kestrel. Priya trabalha com a equipe de contas para configurar o sistema contábil de modo que qualquer alteração de dados bancários fique retida até que uma segunda pessoa a confirme ligando para o cliente no número que já consta do cadastro. No sistema de despacho, as alterações de endereço pedidas por e-mail são sinalizadas para uma ligação rápida antes da próxima entrega. Esses controles tiram a decisão do julgamento da aparência de um e-mail e a levam para uma verificação simples.

### 10.3 Documentação

Priya documenta cada configuração numa página: o que faz, por que existe, como testá-la e quem é o responsável. Ela inclui capturas de tela e a data do último teste. O líder de TI guarda as páginas na pasta compartilhada de suporte. Uma documentação clara permite que qualquer pessoa da equipe confira ou repare um controle, e registra os motivos de cada configuração, o que impede alguém de remover um controle mais tarde por não entender para que ele servia. Tom revisa as páginas.

### Exemplo resolvido

Priya configura caminhos de reporte por e-mail, terminal e celular, monta retenções de verificação para pagamentos e endereços e documenta cada um numa página.

> **Caso sintético.** As configurações são sintéticas.

### Erros e limites

As retenções podem atrasar alterações genuínas. Os telefones do cadastro podem estar desatualizados.

### Exercícios

- **EX037 — Formulário do terminal.** O que o formulário do terminal pede? *Rubrica:* 3 = uma descrição curta e o número do terminal, sem nome;; 2 = mínimo;; 1 = nome;; 0 = nenhuma.

- **EX038 — Caminho dos motoristas.** Como os motoristas reportam mensagens de texto suspeitas? *Rubrica:* 3 = encaminham-nas para um número curto da empresa;; 2 = encaminhar;; 1 = vago;; 0 = nenhuma.

- **EX039 — Controle de alteração bancária.** Como uma alteração de dados bancários é confirmada? *Rubrica:* 3 = uma segunda pessoa liga para o número do cadastro;; 2 = retorno de ligação;; 1 = resposta por e-mail;; 0 = nenhuma.

- **EX040 — Valor da documentação.** Por que registrar o motivo de cada configuração? *Rubrica:* 3 = para que ninguém a remova sem entender;; 2 = justificativa;; 1 = vago;; 0 = nenhuma.

### Síntese

Rotas e retenções configuradas tornam o reporte fácil e a verificação rotineira.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — aula 10 (capítulo 10 de 18)

[← Capítulo 09](#ch-09) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Fatores humanos e política cibernética: verificação

### Objetivos de aprendizagem

Você vai (1) verificar se os controles funcionam como configurados; (2) conferir os controles do ponto de vista do usuário; (3) registrar os resultados da verificação.

### 11.1 Verificações técnicas

Priya verifica cada controle. Ela reporta mensagens sintéticas por cada caminho e confirma que chegam à fila de triagem em menos de um minuto. Envia uma alteração sintética de dados bancários e confirma que ela fica retida. Confere se as etiquetas de externo aparecem e se os avisos de nome coincidente disparam. Confere, com uma conta de teste, se as contas temporárias expiram na data de término. Cada verificação tem um resultado esperado escrito antes do teste, para que ela possa dizer com clareza se o controle passou ou falhou. Cada verificação é cronometrada.

### 11.2 Verificações do lado do usuário

As verificações técnicas não mostram o que os funcionários vivenciam. Priya pede a três voluntários de funções diferentes que usem cada controle enquanto ela observa. Um motorista descobre que o aplicativo de mensagens do celular dele torna incômodo encaminhar uma mensagem de texto, exigindo cinco toques. Uma auxiliar de contas não sabe o que fazer quando aparece uma alteração retida. Priya escreve uma instrução de uma linha para a auxiliar e um guia curto com figuras para os motoristas. As verificações do lado do usuário encontram problemas que importam na prática, mas que não apareceriam em nenhum log.

### Laboratório — Resultados da verificação de sete controles

```python
# Verification results for seven controls (synthetic).
r = [("email button", True), ("terminal form", True), ("driver number", False), ("bank change hold", True),
     ("address flag", False), ("external tag", True), ("seasonal expiry", True)]
print("first pass:", sum(ok for _, ok in r), "of", len(r)); print("needed fixes:", [n for n, ok in r if not ok])
```

Execute com `python3 lab_verify.py`. Saída verificada:

```text
first pass: 5 of 7
needed fixes: ['driver number', 'address flag']
```

### 11.3 Registro dos resultados

Priya registra cada verificação numa tabela com data, método, resultado esperado, resultado real e eventual correção. Dos sete controles, cinco passam de primeira e dois precisam de correções antes de passar. Ela compartilha a tabela com o líder de TI e com Tom. A tabela vira a linha de base para nova verificação depois de atualizações futuras. Registrar as falhas, além das aprovações, mostra que a verificação foi genuína e ajuda a equipe a perceber se o mesmo controle falha repetidamente ao longo do tempo. Os dois controles corrigidos são o número dos motoristas e a sinalização de endereço.

### Exemplo resolvido

Priya faz verificações técnicas e do lado do usuário em sete controles, corrige dois e registra os resultados.

> **Caso sintético.** As verificações são sintéticas.

### Erros e limites

As verificações refletem um momento. Os voluntários podem não representar todos.

### Exercícios

- **EX041 — Resultado esperado.** Por que escrever os resultados esperados antes do teste? *Rubrica:* 3 = para que fique claro se passou ou falhou;; 2 = clareza;; 1 = vago;; 0 = nenhuma.

- **EX042 — Problema do motorista.** Que problema o motorista encontrou? *Rubrica:* 3 = encaminhar uma mensagem de texto exigia cinco toques;; 2 = incômodo;; 1 = vago;; 0 = nenhuma.

- **EX043 — Taxa de aprovação no laboratório.** Quantos controles passaram de primeira no laboratório? *Rubrica:* 3 = 5 de 7;; 2 = cinco;; 1 = 7 de 7;; 0 = nenhuma.

- **EX044 — Uso da tabela.** Em que a tabela se transforma? *Rubrica:* 3 = na linha de base para nova verificação;; 2 = linha de base;; 1 = vago;; 0 = nenhuma.

### Síntese

A verificação pelos lados técnico e do usuário, com resultados registrados, comprova que os controles funcionam.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — aula 11 (capítulo 11 de 18)

[← Capítulo 10](#ch-10) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Laboratório isolado I

### Objetivos de aprendizagem

Você vai (1) testar métodos de reporte num ambiente isolado; (2) medir o tempo e o sucesso das tarefas; (3) relatar os limites com honestidade.

### 12.1 Montagem isolada

No primeiro laboratório isolado, Priya monta um terminal de teste, uma conta de e-mail de teste e um celular reserva, todos desconectados dos sistemas reais da Kestrel. Ela prepara mensagens suspeitas sintéticas para cada um. Nove voluntários, três de cada grupo de funcionários, participam. Eles sabem que estão testando os métodos de reporte, não sendo avaliados pelo seu julgamento. Cada voluntário reporta uma mensagem pelo método antigo, avisando um supervisor que depois manda um e-mail à TI, e outra pelo novo caminho do seu grupo. Cada sessão leva quinze minutos.

### 12.2 Medições

Priya mede o tempo entre ver a mensagem e o reporte chegar à fila de triagem. Com o método antigo, os reportes levam vários minutos porque os supervisores estão ocupados; com os novos caminhos, levam menos de meio minuto. Dois reportes do método antigo nunca chegam, porque quem fazia o papel de supervisor esqueceu, reproduzindo o lapso identificado no capítulo 8. O laboratório calcula os tempos médios por método. Os voluntários dizem que os novos caminhos parecem mais fáceis, embora os motoristas ainda achem o encaminhamento trabalhoso. Ela anota cada hesitação num log curto e o compartilha com o fornecedor do aplicativo.

### Laboratório — Tempos de reporte antigo e novo no laboratório isolado

```python
# Old vs new reporting times in seconds (synthetic, 9 volunteers; None = never arrived).
old = [210, 300, None, 250, 280, None, 240, 270, 270]; new = [18, 25, 20, 22, 30, 19, 21, 24, 19]
o = [x for x in old if x is not None]
print(f"old: mean {sum(o) / len(o):.0f} s, {old.count(None)} never arrived; new: mean {sum(new) / len(new):.0f} s")
```

Execute com `python3 lab_contained.py`. Saída verificada:

```text
old: mean 260 s, 2 never arrived; new: mean 22 s
```

### 12.3 Limites honestos

Priya relata os resultados com limites: nove voluntários são um grupo pequeno; o laboratório era mais calmo do que um turno real; e os tempos do método antigo dependem de quão ocupado estava quem fazia o papel de supervisor. Ela recomenda adotar os novos caminhos e medir os tempos reais de reporte depois do lançamento. Também observa que o caminho dos motoristas precisa de uma opção de encaminhamento mais simples. Limites honestos ajudam os gestores a confiar nos achados e a planejar um acompanhamento sensato, em vez de tratar um teste pequeno como prova final. Os gestores aceitam a recomendação. Tom concorda.

### Exemplo resolvido

Priya testa o reporte antigo e o novo num laboratório isolado com nove voluntários e relata grande economia de tempo, com limites honestos.

> **Caso sintético.** O laboratório é sintético.

### Erros e limites

Amostra pequena. Condições calmas.

### Exercícios

- **EX045 — Isolamento.** Por que o laboratório fica desconectado dos sistemas reais? *Rubrica:* 3 = para manter os testes isolados e seguros;; 2 = isolamento;; 1 = vago;; 0 = nenhuma.

- **EX046 — Reportes perdidos.** O que aconteceu com dois reportes do método antigo? *Rubrica:* 3 = nunca chegaram porque o supervisor esqueceu;; 2 = lapso;; 1 = vago;; 0 = nenhuma.

- **EX047 — Tempos do laboratório.** Que tempos médios o laboratório mostrou? *Rubrica:* 3 = antigo 260 segundos, novo 22 segundos;; 2 = mais rápido;; 1 = vago;; 0 = nenhuma.

- **EX048 — Acompanhamento dos motoristas.** Que acompanhamento é necessário para os motoristas? *Rubrica:* 3 = uma opção de encaminhamento mais simples;; 2 = mais simples;; 1 = vago;; 0 = nenhuma.

### Síntese

Testes contidos mostram o valor das rotas diretas de reporte e precisam de limites honestos.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — aula 12 (capítulo 12 de 18)

[← Capítulo 11](#ch-11) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Fatores humanos e política cibernética: solução de problemas

### Objetivos de aprendizagem

Você vai (1) diagnosticar problemas no serviço de reporte; (2) separar causas técnicas de causas humanas; (3) corrigir as causas e evitar a recorrência.

### 13.1 O problema

Dois meses depois do lançamento, os reportes dos terminais do centro South param. Priya investiga. O formulário do terminal ainda existe, mas os envios falham em silêncio porque uma mudança de rede bloqueou o servidor do formulário. Os trabalhadores que tentaram reportar não viram nenhum erro e supuseram que tinha funcionado, de modo que ninguém levantou o problema. Enquanto isso, o líder de TI tinha notado a queda, mas supôs que o South simplesmente recebia menos mensagens suspeitas. Priya confere os logs do filtro de e-mail e confirma que o South recebeu um número normal de mensagens maliciosas no período.

### 13.2 Separação das causas

Priya separa as causas. A causa técnica foi a mudança de rede, feita sem testar os serviços dependentes. A causa de design foi o formulário não mostrar confirmação, o que deixou as falhas invisíveis para os usuários. A causa humana foi interpretar a queda nos reportes como boa notícia sem conferir. Cada causa precisa de sua própria correção. Tratar só a causa técnica deixaria o serviço vulnerável à próxima falha silenciosa, qualquer que fosse a origem, e perderia a lição sobre a interpretação dos dados.

### 13.3 Correções e prevenção

Priya e o líder de TI corrigem as três causas. A mudança de rede é corrigida e acrescentada a um checklist de serviços a testar depois de mudanças. O formulário agora mostra um número de confirmação quando o reporte é recebido e uma mensagem de erro se ele falha. Uma verificação semanal compara os reportes com as mensagens maliciosas entregues em cada centro e sinaliza qualquer centro em que os reportes caiam muito. Ela registra o incidente no log de solução de problemas. A verificação semanal teria detectado o problema do South em poucos dias.

### Exemplo resolvido

Priya atribui uma queda nos reportes do centro South a uma mudança de rede, à falta de confirmação e a uma métrica mal interpretada, e corrige as três.

> **Caso sintético.** O incidente é sintético.

### Erros e limites

As verificações semanais exigem atenção. Os checklists podem ser pulados.

### Exercícios

- **EX049 — Falha silenciosa.** Por que os trabalhadores não perceberam a falha? *Rubrica:* 3 = o formulário não mostrava erro nem confirmação;; 2 = silenciosa;; 1 = vago;; 0 = nenhuma.

- **EX050 — Queda mal interpretada.** Como o líder de TI interpretou mal a queda? *Rubrica:* 3 = como menos mensagens suspeitas;; 2 = boa notícia;; 1 = vago;; 0 = nenhuma.

- **EX051 — Correção do formulário.** O que o formulário mostra agora? *Rubrica:* 3 = um número de confirmação ou um erro;; 2 = retorno;; 1 = vago;; 0 = nenhuma.

- **EX052 — Verificação semanal.** O que a verificação semanal compara? *Rubrica:* 3 = os reportes com as mensagens maliciosas entregues por centro;; 2 = razão;; 1 = vago;; 0 = nenhuma.

### Síntese

A resolução de problemas encontra causas técnicas, de desenho e humanas, e a prevenção exige corrigir as três.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue estudando — aula 13 (capítulo 13 de 18)

[← Capítulo 12](#ch-12) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Fatores humanos e política cibernética: automação

### Objetivos de aprendizagem

Você vai (1) automatizar etapas da triagem dos reportes; (2) manter a revisão humana onde ela é necessária; (3) monitorar as etapas automatizadas.

### 14.1 Automação da triagem

Priya automatiza a triagem rotineira. Os reportes sobre a mesma mensagem são agrupados. Uma nota de agradecimento é enviada na hora. Se uma mensagem reportada coincide com uma já confirmada como maliciosa, quem reportou recebe o veredito padrão e a mensagem é removida automaticamente das outras caixas postais. O líder de TI revisa só as mensagens novas. O laboratório conta quantos reportes de uma semana movimentada sintética precisaram de revisão humana depois da automação, mostrando quanto tempo se economiza para respostas e investigação. As regras são simples de ler e de alterar.

### Laboratório — Reportes que precisam de revisão humana após a automação

```python
# Reports needing human review after automation in a synthetic busy week.
total, dup, known = 80, 51, 17
print(f"total {total}; duplicates {dup}; known verdicts {known}; human review {total - dup - known} ({(total - dup - known) / total:.0%})")
```

Execute com `python3 lab_triage.py`. Saída verificada:

```text
total 80; duplicates 51; known verdicts 17; human review 12 (15%)
```

### 14.2 Revisão humana

Priya cogita deixar um serviço de pontuação decidir os vereditos de todas as mensagens. Decide contra, porque rotular por engano como maliciosa uma mensagem real de cliente poderia causar uma entrega perdida ou a perda de um cliente, e rotular por engano uma falsificação como segura poderia causar fraude. A revisão humana continua para as mensagens novas. Ela observa que a automação deve cuidar do que é certo e repetitivo, enquanto as pessoas cuidam do que é incerto ou tem consequências sérias. O líder de TI concorda com essa divisão do trabalho e a registra no runbook de triagem.

### 14.3 Monitoramento da automação

As etapas automatizadas podem falhar sem que ninguém perceba, como mostrou o incidente do centro South. Priya acrescenta uma linha diária de log para cada etapa automatizada e um resumo semanal que lista as falhas. Também sorteia dez vereditos automáticos por mês para o líder de TI conferir à mão. No primeiro mês, os dez estão corretos. O monitoramento dá à equipe confiança na automação e detecta os erros antes que prejudiquem a confiança no serviço de reporte. O resumo chega por e-mail toda segunda-feira de manhã. Os resultados são registrados.

### Exemplo resolvido

Priya automatiza o agrupamento, o agradecimento e os vereditos conhecidos, mantém a revisão humana para as mensagens novas e monitora a automação com logs e amostras.

> **Caso sintético.** Os dados são sintéticos.

### Erros e limites

As listas de conhecidos precisam de atualização. As amostras podem deixar passar erros raros.

### Exercícios

- **EX053 — Proporção de revisão no laboratório.** Quantos dos 80 reportes precisaram de revisão humana no laboratório? *Rubrica:* 3 = 12;; 2 = 15%;; 1 = 80;; 0 = nenhuma.

- **EX054 — Serviço de pontuação.** Por que não deixar um serviço de pontuação decidir todos os vereditos? *Rubrica:* 3 = rótulos errados causam perda de clientes ou fraude;; 2 = consequências;; 1 = custo;; 0 = nenhuma.

- **EX055 — Regra da automação.** Do que a automação deve cuidar? *Rubrica:* 3 = do que é certo e repetitivo;; 2 = rotina;; 1 = julgamento;; 0 = nenhuma.

- **EX056 — Amostra mensal.** Que verificação mensal Priya acrescentou? *Rubrica:* 3 = conferir à mão dez vereditos automáticos;; 2 = amostra;; 1 = vago;; 0 = nenhuma.

### Síntese

A automação acelera o retorno quando lida com o que é certo e deixa o julgamento para as pessoas.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue estudando — aula 14 (capítulo 14 de 18)

[← Capítulo 13](#ch-13) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Fatores humanos e política cibernética: integração e dependências

### Objetivos de aprendizagem

Você vai (1) conectar o reporte à resposta a incidentes e ao atendimento ao cliente; (2) identificar as dependências de pessoas e de fornecedores; (3) reduzir os pontos únicos de falha.

### 15.1 Integração

Priya liga o reporte à resposta a incidentes: quando uma mensagem maliciosa chegou a muitos funcionários, o líder de TI a remove, bloqueia o remetente e verifica se alguém digitou dados. Ela também o liga ao atendimento ao cliente. Quando os clientes reportam mensagens de texto falsas de entrega que usam o nome da Kestrel, o atendimento as encaminha para a mesma fila de triagem, e um aviso é publicado no site. Integração significa que uma única fila vê todos os reportes, de modo que padrões que afetam tanto os funcionários quanto os clientes são percebidos rapidamente. A equipe de atendimento recebe uma orientação curta.

### 15.2 Dependências

Priya lista as dependências: o líder de TI faz a maior parte da triagem; o provedor de e-mail opera o botão de reporte; um prestador mantém o formulário do terminal; e o recurso de retenção do sistema contábil depende do calendário de atualizações de um fornecedor. Ela marca o líder de TI como ponto único de falha, já que a triagem para quando ele está ausente. Também observa que o número dos motoristas depende de um único contrato de telefonia móvel. Mapear as dependências mostra do que o serviço de reporte depende e onde ele pode quebrar. Ela compartilha a lista com Tom.

### 15.3 Redução dos pontos únicos

Para reduzir a dependência do líder de TI, Priya treina um segundo integrante da equipe na triagem com um runbook curto e organiza um rodízio. Pede ao prestador um contato de suporte para o formulário do terminal. Registra no calendário da equipe a data de renovação do contrato de telefonia móvel. Reduzir os pontos únicos de falha custa pouco, mas torna o serviço confiável durante férias, doenças e trocas de pessoal, que são inevitáveis em qualquer equipe pequena. O rodízio começa no mês seguinte. As duas mudanças são registradas no runbook.

### Exemplo resolvido

Priya integra o reporte à resposta e ao atendimento ao cliente, mapeia as dependências e acrescenta uma reserva para a triagem e contatos dos fornecedores.

> **Caso sintético.** A integração é sintética.

### Erros e limites

Reservas perdem a prática se não forem usadas. Os contratos mudam.

### Exercícios

- **EX057 — Reportes dos clientes.** O que acontece com os reportes de clientes sobre mensagens de texto falsas? *Rubrica:* 3 = são encaminhados à triagem e um aviso é publicado no site;; 2 = integração;; 1 = vago;; 0 = nenhuma.

- **EX058 — Ponto único.** Quem é o principal ponto único de falha? *Rubrica:* 3 = o líder de TI;; 2 = uma pessoa;; 1 = o prestador;; 0 = nenhuma.

- **EX059 — Reserva da triagem.** Como se reduz a dependência do líder de TI? *Rubrica:* 3 = treinando uma segunda pessoa com um runbook e um rodízio;; 2 = reserva;; 1 = vago;; 0 = nenhuma.

- **EX060 — Risco contratual.** Que risco de fornecedor é acompanhado no calendário? *Rubrica:* 3 = a renovação do contrato de telefonia móvel;; 2 = renovação;; 1 = vago;; 0 = nenhuma.

### Síntese

A integração amplia o que o reporte enxerga, e os backups o mantêm funcionando.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue estudando — aula 15 (capítulo 15 de 18)

[← Capítulo 14](#ch-14) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Documentação técnica e segurança

### Objetivos de aprendizagem

Você vai (1) escrever runbooks para o serviço de reporte; (2) incluir regras de segurança e de ética; (3) manter a documentação atualizada.

### 16.1 Runbooks

Priya escreve runbooks para a triagem, as retenções de verificação, a verificação semanal por centro e a criação das contas temporárias. Cada runbook declara o propósito, as etapas, as ferramentas, os resultados esperados e o que fazer se algo der errado. Ela usa etapas numeradas e capturas de tela. Testa cada runbook observando o segundo integrante da equipe segui-lo sem ajuda e depois corrige as etapas que causaram hesitação. Os runbooks permitem que o serviço continue quando quem o construiu está ausente ou já saiu. Cada runbook tem um número de versão.

### 16.2 Regras de segurança e de ética

Priya inclui regras na documentação: nunca enviar phishing simulado sem aprovação do gerente de operações e dos representantes dos funcionários; nunca usar iscas sobre salário, saúde ou estabilidade no emprego; relatar os resultados apenas de forma agregada; nunca usar dados de reporte ou de cliques em processos disciplinares ou de desempenho; e usar contas de teste e mensagens sintéticas em qualquer teste. Ela cita o NIST SP 800-50r1 e as diretrizes de cultura da ENISA como base. Pôr essas regras por escrito protege os funcionários de experimentos bem-intencionados, mas prejudiciais. O gerente de operações as assina.

### 16.3 Manter atualizado

A documentação se deteriora à medida que os sistemas mudam. Priya acrescenta uma data de revisão a cada página e, no topo, uma linha dizendo quem é o responsável. Ela cria um lembrete no calendário para a revisão trimestral. Quando aconteceu o incidente da mudança de rede, ela atualizou três páginas em um dia. Ela explica a Tom que uma documentação desatualizada pode ser pior do que nenhuma, porque as pessoas confiam nela, e que os responsáveis e as datas de revisão são o que mantém os documentos úteis com o tempo. O líder de TI adota essa prática. Os responsáveis confirmam as revisões.

### Exemplo resolvido

Priya escreve runbooks testados, registra regras de ética para qualquer simulação ou teste e define responsáveis e datas de revisão.

> **Caso sintético.** A documentação é sintética; o SP 800-50r1 e as diretrizes da ENISA são reais.

### Erros e limites

As revisões são puladas. As regras precisam ser aplicadas.

### Exercícios

- **EX061 — Teste dos runbooks.** Como os runbooks foram testados? *Rubrica:* 3 = um colega os seguiu sem ajuda;; 2 = simulação guiada;; 1 = vago;; 0 = nenhuma.

- **EX062 — Iscas proibidas.** Que iscas são proibidas? *Rubrica:* 3 = salário, saúde ou estabilidade no emprego;; 2 = angústia;; 1 = vago;; 0 = nenhuma.

- **EX063 — Regra dos dados.** Onde os dados de reporte e de cliques nunca podem ser usados? *Rubrica:* 3 = em processos disciplinares ou de desempenho;; 2 = RH;; 1 = vago;; 0 = nenhuma.

- **EX064 — Perigo da desatualização.** Por que uma documentação desatualizada pode ser pior do que nenhuma? *Rubrica:* 3 = as pessoas confiam nela;; 2 = confiança equivocada;; 1 = vago;; 0 = nenhuma.

### Síntese

A documentação inclui etapas, regras de ética e responsabilidades para que o serviço continue seguro e atualizado.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue estudando — aula 16 (capítulo 16 de 18)

[← Capítulo 15](#ch-15) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Laboratório isolado II

### Objetivos de aprendizagem

Você vai (1) testar num exercício isolado o efeito do retorno rápido sobre o reporte posterior; (2) analisar os resultados de forma simples; (3) recomendar uma prática.

### 17.1 Desenho do exercício

No segundo laboratório isolado, Priya testa se o retorno rápido incentiva as pessoas a reportar de novo. Doze voluntários, que conhecem o propósito, usam contas de teste em duas sessões com uma semana de intervalo. Na primeira sessão, cada um reporta mensagens sintéticas; metade recebe um veredito curto em minutos e metade não recebe nada. Na segunda sessão, todos recebem um novo lote e Priya conta quantas mensagens reportam. O desenho é aprovado por Tom e pelo gerente de operações, e os voluntários podem desistir a qualquer momento. Os horários das sessões se ajustam aos turnos.

### 17.2 Resultados

O laboratório compara o reporte da segunda sessão entre os dois grupos. Os voluntários que receberam retorno rápido reportam mais das novas mensagens do que os que não receberam. Priya observa que doze pessoas são um grupo pequeno e que os voluntários conheciam o propósito, o que pode afetar o comportamento. Ainda assim, o resultado é compatível com as entrevistas e com achados anteriores de que o retorno importa. Ela apresenta as contagens e a diferença sem afirmar mais do que o pequeno teste mostra. O grupo com retorno chegou a 87%, contra 57%. Ela compartilha as contagens com os voluntários.

### Laboratório — Reporte na segunda sessão com e sem retorno

```python
# Session two: messages reported out of 30 per group (6 volunteers x 5 messages), synthetic.
fb, nofb = 26, 17
print(f"feedback group {fb}/30 = {fb / 30:.0%}; no-feedback group {nofb}/30 = {nofb / 30:.0%}")
```

Execute com `python3 lab_feedback.py`. Saída verificada:

```text
feedback group 26/30 = 87%; no-feedback group 17/30 = 57%
```

### 17.3 Recomendação

Priya recomenda que todo reporte real receba resposta em até um dia útil e que os vereditos automáticos sejam usados sempre que possível para acelerar isso. Ela sugere que o líder de TI acompanhe os tempos de resposta toda semana. Também recomenda que cada veredito traga uma breve explicação do que tornava a mensagem suspeita, para que os funcionários aprendam com cada caso. Sua recomendação é barata e se apoia em várias fontes de evidência, o que deixa os gestores dispostos a adotá-la. O líder de TI a adota imediatamente.

### Exemplo resolvido

Priya conduz um exercício isolado de retorno com doze voluntários, encontra mais reporte posterior depois do retorno rápido e recomenda respostas em até um dia.

> **Caso sintético.** O exercício é sintético.

### Erros e limites

Os voluntários conheciam o propósito. Grupo pequeno.

### Exercícios

- **EX065 — Grupos do exercício.** Como os dois grupos foram tratados na primeira sessão? *Rubrica:* 3 = metade recebeu vereditos rápidos, metade nada;; 2 = retorno;; 1 = vago;; 0 = nenhuma.

- **EX066 — Resultado do laboratório.** O que o laboratório mostrou para o reporte da segunda sessão? *Rubrica:* 3 = 26 de 30 com retorno contra 17 de 30 sem;; 2 = maior;; 1 = vago;; 0 = nenhuma.

- **EX067 — Conteúdo do veredito.** O que cada veredito deve incluir brevemente? *Rubrica:* 3 = o que tornava a mensagem suspeita;; 2 = explicação;; 1 = vago;; 0 = nenhuma.

- **EX068 — Meta de resposta.** Que meta de resposta Priya recomendou? *Rubrica:* 3 = em até um dia útil;; 2 = um dia;; 1 = vago;; 0 = nenhuma.

### Síntese

Exercícios contidos podem sustentar melhorias simples e baratas, como o retorno rápido.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue estudando — aula 17 (capítulo 17 de 18)

[← Capítulo 16](#ch-16) · [Índice das aulas](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continue para a próxima aula já escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Projeto técnico supervisionado

### Objetivos de aprendizagem

Você vai (1) entregar uma melhoria completa sob supervisão; (2) avaliá-la depois do lançamento; (3) passá-la adiante com documentação.

### 18.1 O projeto

No projeto supervisionado, Priya entrega um caminho de reporte mais simples para os motoristas. Em vez de encaminhar mensagens de texto, os motoristas tocam num botão Reportar no aplicativo de rotas, que captura o remetente e o conteúdo da mensagem suspeita depois que o motorista a cola, e a envia à triagem. Ela trabalha com o fornecedor do aplicativo, testa o recurso com cinco motoristas num ambiente de teste e o lança depois da aprovação de Tom e do gerente de operações. Os motoristas recebem um vídeo de um minuto mostrando como usá-lo. Os motoristas gostam do vídeo.

### 18.2 Avaliação

Depois de seis semanas, Priya compara os reportes dos motoristas antes e depois da mudança. Os reportes de mensagens de texto falsas subiram, e a mediana do tempo entre o recebimento e o reporte caiu. Num questionário curto, os motoristas dizem que o botão é mais fácil do que encaminhar. O laboratório resume os números. Ela também confere que o tempo de triagem não cresceu demais e descobre que o agrupamento automático o manteve administrável. Ela observa que seis semanas é pouco e que uma campanha de ataque na quarta semana pode ter aumentado os reportes.

### Laboratório — Reportes dos motoristas antes e depois do botão no aplicativo

```python
# Driver reports of fake texts, six weeks before vs after the app button (synthetic).
before = [120, 95, 60, 150, 80, 40]; after = [5, 8, 12, 15, 20, 9, 10, 14, 12, 18, 11, 25, 7, 13, 16, 30, 6, 12, 22]
m = lambda x: sorted(x)[len(x) // 2]
print(f"before: {len(before)} reports, median {m(before)} min; after: {len(after)} reports, median {m(after)} min")
```

Execute com `python3 lab_drivers.py`. Saída verificada:

```text
before: 6 reports, median 95 min; after: 19 reports, median 12 min
```

### 18.3 Passagem

Priya escreve um runbook para o caminho do aplicativo, acrescenta-o à tabela de verificação e treina a segunda pessoa da triagem. Ela apresenta o projeto a Tom, ao líder de TI e ao gerente de operações, cobrindo o problema, o design, o teste, os resultados e os limites. O gerente de operações pede que o botão seja estendido aos coletores portáteis do armazém. Tom observa que o projeto de Priya mostra a função técnica no seu melhor: prático, testado, respeitoso com os usuários e documentado para que outros possam mantê-lo. Tom aprova o projeto.

### Exemplo resolvido

Priya entrega um botão de reporte no aplicativo para os motoristas, avalia seis semanas de resultados e faz a passagem com runbook e treinamento.

> **Caso sintético.** O projeto é sintético.

### Erros e limites

Seis semanas é pouco. Campanhas podem inflar os reportes.

### Exercícios

- **EX069 — Caminho dos motoristas.** O que substituiu o encaminhamento para os motoristas? *Rubrica:* 3 = um botão Reportar no aplicativo de rotas;; 2 = botão no aplicativo;; 1 = vago;; 0 = nenhuma.

- **EX070 — Mudança no laboratório.** O que o laboratório mostrou para os reportes dos motoristas? *Rubrica:* 3 = de 6 para 19 reportes e mediana de 95 para 12 minutos;; 2 = alta;; 1 = vago;; 0 = nenhuma.

- **EX071 — Fator de confusão.** O que, além do botão, pode ter aumentado os reportes? *Rubrica:* 3 = uma campanha de ataque na quarta semana;; 2 = campanha;; 1 = vago;; 0 = nenhuma.

- **EX072 — Próximo pedido.** O que o gerente de operações pediu em seguida? *Rubrica:* 3 = estender o botão aos coletores portáteis;; 2 = coletores;; 1 = vago;; 0 = nenhuma.

### Síntese

Um projeto supervisionado entrega, avalia e repassa uma melhoria prática.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue estudando — aula 18 (capítulo 18 de 18)

[← Capítulo 17](#ch-17) · [Índice das aulas](../SUBJECTS.md) · [Próximo curso pelo índice →](../SUBJECTS.md)

O índice aponta para o próximo curso do percurso de estudos.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX072. Priya Raman, Tom Hallett, o Eastvale Technical College, a Kestrel Logistics e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX037.** Uma descrição curta e o número do terminal, sem nome.

**EX038.** Encaminhando-as para um número curto da empresa.

**EX039.** Uma segunda pessoa liga para o cliente no número que já consta do cadastro.

**EX040.** Para que ninguém remova o controle mais tarde sem entender seu propósito.

**EX041.** Para poder dizer com clareza se cada controle passou ou falhou.

**EX042.** Encaminhar uma mensagem de texto exigia cinco toques no aplicativo de mensagens dele.

**EX043.** Cinco de sete passaram de primeira; dois passaram depois de correções.

**EX044.** A linha de base para nova verificação depois de atualizações futuras.

**EX045.** Para que os testes não possam afetar sistemas reais nem funcionários reais.

**EX046.** Nunca chegaram, porque quem fazia o papel de supervisor se esqueceu de repassá-los.

**EX047.** Cerca de 260 segundos com o método antigo e 22 segundos com os novos caminhos.

**EX048.** Uma forma mais simples de encaminhar as mensagens de texto suspeitas.

**EX049.** Porque o formulário não mostrava confirmação nem erro.

**EX050.** Como sinal de que o South recebia menos mensagens suspeitas.

**EX051.** Um número de confirmação em caso de sucesso ou um erro em caso de falha.

**EX052.** Os reportes com as mensagens maliciosas entregues, em cada centro.

**EX053.** 12 de 80, ou 15%.

**EX054.** Porque rótulos errados poderiam causar perda de clientes ou fraude.

**EX055.** Do que é certo e repetitivo.

**EX056.** O líder de TI confere à mão dez vereditos automáticos por mês.

**EX057.** O atendimento ao cliente os encaminha à triagem e um aviso é publicado no site.

**EX058.** O líder de TI, que faz a maior parte da triagem.

**EX059.** Treinando um segundo integrante da equipe com um runbook e organizando um rodízio.

**EX060.** A data de renovação do contrato de telefonia móvel do número dos motoristas.

**EX061.** Observando um colega segui-los sem ajuda.

**EX062.** Iscas sobre salário, saúde ou estabilidade no emprego.

**EX063.** Em processos disciplinares ou de desempenho.

**EX064.** Porque as pessoas confiam nela e seguem etapas erradas.

**EX065.** Metade recebeu vereditos rápidos e metade não recebeu retorno.

**EX066.** 26 de 30 mensagens reportadas com retorno contra 17 de 30 sem retorno.

**EX067.** Uma breve explicação do que tornava a mensagem suspeita.

**EX068.** Uma resposta a cada reporte em até um dia útil.

**EX069.** Um botão Reportar no aplicativo de rotas.

**EX070.** Os reportes subiram de 6 para 19 e a mediana do tempo até o reporte caiu de 95 para 12 minutos.

**EX071.** Uma campanha de ataque na quarta semana.

**EX072.** Estender o botão aos coletores portáteis do armazém.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- European Union Agency for Cybersecurity. (2019). *Cybersecurity culture guidelines: Behavioural aspects of cybersecurity*. ENISA. <https://www.enisa.europa.eu/publications/cybersecurity-culture-guidelines-behavioural-aspects-of-cybersecurity>
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Reason, J. (1990). *Human error*. Cambridge University Press. <https://doi.org/10.1017/CBO9781139062367>
- Whitten, A., & Tygar, J. D. (1999). Why Johnny can't encrypt: A usability evaluation of PGP 5.0. *Proceedings of the 8th USENIX Security Symposium*. USENIX. <https://www.usenix.org/conference/8th-usenix-security-symposium/why-johnny-cant-encrypt-usability-evaluation-pgp-50>
