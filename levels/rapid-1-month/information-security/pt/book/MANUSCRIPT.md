# Segurança da Informação: Curso Rápido

- Idioma: português do Brasil (`pt`); curso 002, curso rápido (1 mês). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–4 de 4 têm texto didático escrito à mão; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; o laboratório offline usa apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e sua saída foi incorporada de uma execução real, idêntica à da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: gestores e funcionários de organizações muito pequenas que precisam corrigir em um mês as fraquezas de segurança mais comuns.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: o laboratório conta, por pasta, os arquivos compartilhados sintéticos abertos a qualquer pessoa com o link. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os quatro capítulos acompanham uma gerente de clínica desde o que a clínica guarda, passando pelas contas, pelos dispositivos e pelo compartilhamento e pela fraude por e-mail e pelas pessoas, até os backups, os incidentes e uma rotina mensal. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Sofia Lindqvist** | Gerente da clínica e aluna | Inventada |
| **Sr. Tomasz Nowak** | Instrutor | Inventado |
| **Eastgate Training Centre** | Centro de treinamento fictício | Inventado |
| **Hollybank Veterinary Practice** | Clínica fictícia, com uma unidade e dezoito funcionários | Inventada |

### Fontes principais

ISO/IEC 27000:2026. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Um mês para acertar o básico

### Objetivos de aprendizagem

Você vai (1) descrever o que cobre o curso rápido de um mês; (2) conhecer o caso que acompanha o livro; (3) listar o que uma pequena clínica guarda e o que ela não pode perder.

### 1.1 A aluna

Sofia Lindqvist é a gerente de uma pequena clínica veterinária. Depois que uma empresa vizinha perdeu uma semana de trabalho por causa de um ransomware, a dona pede a ela que garanta que a clínica não seja a próxima. Sofia se matricula num curso rápido de um mês em segurança da informação no fictício Eastgate Training Centre, com quatro sessões semanais e tarefas curtas entre elas. Seu instrutor, o Sr. Tomasz Nowak, passou anos ajudando pequenas empresas a se recuperar de incidentes. Ele diz à turma que um mês basta para corrigir as fraquezas mais comuns, embora não para se tornar especialista.

### 1.2 A clínica

Sofia trabalha na fictícia Hollybank Veterinary Practice, uma unidade única com dois veterinários, quatro enfermeiros, três recepcionistas e uma pequena equipe de escritório, dezoito funcionários ao todo. A clínica usa um sistema de gestão clínica em nuvem para as consultas, os prontuários dos animais e os pagamentos, um serviço de e-mail e arquivos em nuvem e nove computadores, além de dois tablets. Os registros dos clientes guardam nomes, endereços, telefones e o histórico de pagamentos. Um técnico externo vem quando algo quebra. A dona, a Dra. Rachel Moss, quer a clínica protegida sem atrasar o balcão da recepção nas manhãs movimentadas, quando já se formam filas.

### 1.3 O que a clínica guarda

Na primeira tarefa, Sofia lista as informações que a clínica guarda e onde elas ficam. Os prontuários dos animais e dos clientes, as consultas e os pagamentos estão no sistema de gestão clínica. Os contratos e as escalas dos funcionários ficam em pastas compartilhadas. As faturas e os dados bancários dos fornecedores chegam por e-mail. Os resultados de exames chegam por e-mail de um laboratório externo. As fotos de marketing para as redes sociais da clínica também ficam em pastas compartilhadas. O Sr. Nowak pede que ela marque cada item pelo dano que um vazamento, uma alteração errada ou uma perda causaria, usando alto, médio ou baixo.

### 1.4 O que não pode ser perdido

Sofia combina três prioridades com a Dra. Moss. A clínica não pode perder o acesso ao sistema de gestão clínica durante o horário de funcionamento, porque as consultas e as anotações de tratamento dependem dele. Ela não pode deixar vazar os contatos e os dados de pagamento dos clientes, porque os clientes os confiam à clínica e a lei exige que sejam protegidos. E ela não pode pagar uma fatura fraudulenta de fornecedor, porque as margens são apertadas. O Sr. Nowak explica que a ISO/IEC 27000:2026 descreve a segurança da informação como a proteção da confidencialidade, da integridade e da disponibilidade e que as três prioridades de Sofia correspondem perfeitamente a esses três objetivos.

### 1.5 Regras básicas

O Sr. Nowak define três regras para o mês. Obter a concordância por escrito da Dra. Moss antes de mudar qualquer configuração. Nunca colocar dados reais de clientes nos trabalhos do curso nem em exemplos compartilhados. Anotar cada mudança com a data e o motivo, para que o técnico e a Dra. Moss possam ver o que foi feito. Sofia cria um log de mudanças simples num documento compartilhado que só ela e a Dra. Moss podem abrir. O Sr. Nowak acrescenta que as pequenas empresas muitas vezes são prejudicadas por mudanças bem-intencionadas que ninguém registrou, porque os problemas posteriores não podem ser rastreados até sua causa.

### Exemplo resolvido

Sofia entra no curso rápido, lista o que guarda a clínica de dezoito pessoas da Hollybank, combina três prioridades ligadas à confidencialidade, à integridade e à disponibilidade e inicia um log de mudanças.

> **Caso sintético.** O Eastgate, a Hollybank e todas as pessoas são sintéticos.

### Erros e limites

As mudanças não registradas tornam os problemas posteriores difíceis de rastrear.

### Exercícios

- **EX001 — Duração do curso.** Quanto dura o curso de Sofia? *Rubrica:* 3 = um mês, quatro sessões;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.

- **EX002 — Gatilho.** O que levou a dona a agir? *Rubrica:* 3 = o ransomware de um vizinho;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX003 — Número de funcionários.** Quantos funcionários a Hollybank tem? *Rubrica:* 3 = dezoito;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX004 — Sistema central.** Onde ficam os prontuários dos animais e as consultas? *Rubrica:* 3 = sistema de gestão clínica em nuvem;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX005 — Número de dispositivos.** Quantos computadores e tablets a clínica usa? *Rubrica:* 3 = nove computadores, dois tablets;; 2 = os dois;; 1 = um;; 0 = nenhuma.

- **EX006 — Condição da dona.** O que a Dra. Moss pediu? *Rubrica:* 3 = proteção sem atrasar a recepção;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX007 — Resultados de exames.** Como chegam os resultados dos exames de laboratório? *Rubrica:* 3 = por e-mail;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX008 — Marcação do dano.** Como Sofia marca cada item de informação? *Rubrica:* 3 = dano alto, médio ou baixo;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX009 — Prioridade de disponibilidade.** Qual prioridade trata da disponibilidade? *Rubrica:* 3 = o sistema da clínica no horário de funcionamento;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

- **EX010 — Prioridade de integridade.** Qual prioridade trata da integridade? *Rubrica:* 3 = não pagar uma fatura fraudulenta;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

- **EX011 — Norma citada.** Qual norma descreve os três objetivos? *Rubrica:* 3 = ISO/IEC 27000:2026;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

- **EX012 — Acesso ao log de mudanças.** Quem pode abrir o log de mudanças? *Rubrica:* 3 = Sofia e a Dra. Moss;; 2 = parcialmente correto;; 1 = outra pessoa;; 0 = nenhuma.

- **EX013 — Motivo do log.** Por que registrar cada mudança? *Rubrica:* 3 = para que os problemas possam ser rastreados;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Contas, dispositivos e compartilhamento

### Objetivos de aprendizagem

Você vai (1) dar a cada pessoa a própria conta com um segundo fator; (2) proteger os dispositivos da clínica; (3) encontrar e fechar arquivos compartilhados em excesso com um script curto.

### 2.1 Contas próprias

Sofia descobre que a equipe da recepção compartilha um único login do sistema de gestão clínica, escrito num bilhete embaixo do teclado. O Sr. Nowak explica que os logins compartilhados escondem quem fez o quê e que o bilhete significa que qualquer pessoa no balcão poderia entrar. O sistema aceita contas pessoais com troca rápida entre usuários, por isso Sofia cria uma conta por pessoa e remove o bilhete. A equipe da recepção se preocupa com atrasos, então ela cronometra a troca durante uma manhã movimentada e mostra que leva alguns segundos. A Dra. Moss aprova a mudança depois de ver o tempo medido.

### 2.2 Segundo fator

O Sr. Nowak explica que a maioria das tomadas de conta começa com uma senha roubada ou adivinhada e que um segundo fator, como um aplicativo no celular, impede a maioria delas. Sofia ativa um segundo fator no e-mail e no sistema da clínica, começando pela Dra. Moss e pela equipe do escritório, que cuida dos pagamentos, e depois todos os demais ao longo de duas semanas. Dois enfermeiros não querem aplicativos de trabalho nos próprios celulares, por isso a clínica compra duas pequenas chaves de segurança para eles. Sofia registra o método de cada pessoa no log de mudanças, para que os dispositivos perdidos possam ser tratados depressa.

### 2.3 Dispositivos

Sofia confere os nove computadores e os dois tablets com o técnico. Três computadores estão com as atualizações desligadas porque uma impressora de etiquetas antiga parou de funcionar depois de uma atualização no ano passado. O técnico instala um driver de impressora mais novo e religa as atualizações. Todos os dispositivos agora bloqueiam após cinco minutos, e as contas da equipe não conseguem mais instalar software. Os tablets usados nos consultórios recebem uma senha de acesso e apagamento remoto. O Sr. Nowak observa que desligar as atualizações para resolver um problema é comum e que a correção é resolver o problema de fundo em vez de deixar os dispositivos expostos.

### Laboratório — Arquivos compartilhados abertos a qualquer pessoa com o link, por pasta, num repositório sintético de arquivos

```python
"""Find synthetic shared files open to anyone with the link, by folder (stdlib only)."""
import random
from collections import Counter
random.seed(2)
files = []
for folder, n, p in [("clients", 140, 0.04), ("finance", 60, 0.05), ("marketing", 80, 0.30), ("rotas", 20, 0.5)]:
    for i in range(n):
        files.append((folder, random.random() < p))
total = Counter(f for f, _ in files)
open_ = Counter(f for f, o in files if o)
for f in total:
    print(f"{f}: {open_[f]} of {total[f]} open to anyone with the link")
print(f"all files: {sum(open_.values())} of {len(files)}")
```

Execute com `python3 lab_sharing.py`. Saída verificada:

```text
clients: 8 of 140 open to anyone with the link
finance: 4 of 60 open to anyone with the link
marketing: 25 of 80 open to anyone with the link
rotas: 10 of 20 open to anyone with the link
all files: 47 of 300
```

### 2.4 Arquivos compartilhados em excesso

Com a permissão da Dra. Moss, o técnico exporta uma lista dos arquivos compartilhados e indica se cada um está aberto a qualquer pessoa com o link. Sofia executa o script numa cópia sintética com a mesma estrutura de pastas. Ele encontra 47 de 300 arquivos abertos a qualquer pessoa com o link. A maioria são fotos de marketing, 25 de 80, e escalas da equipe, 10 de 20. Mas 8 de 140 arquivos da pasta de clientes e 4 de 60 da pasta do financeiro também estão abertos. Esses doze são os que mais importam, porque qualquer pessoa que obtenha um link poderia ler informações de clientes ou bancárias.

### 2.5 Fechando as lacunas

Sofia muda primeiro os doze arquivos de clientes e do financeiro para compartilhamento restrito à clínica. Depois, pergunta à equipe por que as escalas eram compartilhadas abertamente e descobre que os funcionários de meio período as consultam de casa nos celulares pessoais. Ela leva a escala para o sistema da clínica, onde a equipe pode vê-la depois de entrar com login. As fotos de marketing podem continuar públicas porque já estão publicadas na internet. Sofia pede ao técnico que defina como padrão para os novos compartilhamentos o acesso restrito à clínica e acrescenta um lembrete mensal para repetir a verificação. O Sr. Nowak a elogia por corrigir o motivo por trás do compartilhamento das escalas, e não só a configuração.

### Exemplo resolvido

Sofia substitui um login compartilhado da recepção, ativa segundos fatores com chaves de segurança para dois enfermeiros, religa as atualizações em três computadores e encontra 47 de 300 arquivos sintéticos abertos a qualquer pessoa, incluindo 12 arquivos de clientes e do financeiro.

> **Caso sintético.** As contas, os dispositivos e os arquivos são sintéticos.

### Erros e limites

Desligar as atualizações para consertar uma impressora deixa os dispositivos expostos muito depois de a impressora ser esquecida.

### Exercícios

- **EX014 — Login compartilhado.** O que a recepção usava para entrar? *Rubrica:* 3 = um login compartilhado num bilhete;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.

- **EX015 — Tempo da troca.** Quanto tempo leva a troca de usuários? *Rubrica:* 3 = alguns segundos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX016 — Primeiro grupo com MFA.** Quem recebeu um segundo fator primeiro? *Rubrica:* 3 = a Dra. Moss e a equipe do escritório;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.

- **EX017 — Chaves de segurança.** Por que foram compradas chaves de segurança? *Rubrica:* 3 = dois enfermeiros recusaram aplicativos nos celulares pessoais;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX018 — Atualizações desligadas.** Por que as atualizações estavam desligadas em três computadores? *Rubrica:* 3 = uma impressora de etiquetas antiga quebrou após uma atualização;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX019 — Correção da atualização.** Como o problema da impressora foi corrigido? *Rubrica:* 3 = um driver de impressora mais novo;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX020 — Controles dos tablets.** O que os tablets dos consultórios receberam? *Rubrica:* 3 = senha de acesso e apagamento remoto;; 2 = os dois;; 1 = um;; 0 = nenhuma.

- **EX021 — Total de abertos.** Quantos arquivos estavam abertos a qualquer pessoa com o link? *Rubrica:* 3 = 47 de 300;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX022 — Arquivos de marketing.** Quantos arquivos de marketing estavam abertos? *Rubrica:* 3 = 25 de 80;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX023 — Sensíveis abertos.** Quantos arquivos de clientes e do financeiro estavam abertos? *Rubrica:* 3 = 12 (8 de clientes, 4 do financeiro);; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.

- **EX024 — Causa das escalas.** Por que as escalas eram compartilhadas abertamente? *Rubrica:* 3 = funcionários de meio período as consultavam de casa;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX025 — Correção das escalas.** Para onde foi a escala? *Rubrica:* 3 = para o sistema da clínica;; 2 = parcialmente correto;; 1 = outro lugar;; 0 = nenhuma.

- **EX026 — Configuração padrão.** Que padrão o técnico definiu? *Rubrica:* 3 = compartilhamento restrito à clínica para os novos compartilhamentos;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — E-mail, fraude e pessoas

### Objetivos de aprendizagem

Você vai (1) reconhecer o phishing e a fraude de faturas; (2) definir uma regra de verificação de pagamentos; (3) criar um hábito curto e sem culpa de comunicação.

### 3.1 Sinais de phishing

O Sr. Nowak mostra à turma os sinais comuns de phishing: um endereço de remetente que não corresponde ao nome mostrado, uma urgência inesperada, um link cujo destino real difere do texto e pedidos de senhas ou pagamentos. Sofia escolhe três e-mails recentes da caixa de entrada da clínica sobre os quais a equipe tinha perguntado e os examina com a equipe da recepção. Um alegava vir de uma transportadora e levava a um endereço parecido. O Sr. Nowak insiste que nenhuma lista pega tudo, por isso o hábito de parar e conferir importa mais do que decorar os sinais.

### 3.2 Fraude de faturas

As pequenas empresas são alvos frequentes de mensagens que alegam que um fornecedor mudou os dados bancários. A Hollybank paga um distribuidor de medicamentos, um laboratório e vários fornecedores de equipamentos. Sofia combina uma regra com a Dra. Moss: qualquer pedido de mudança de dados bancários é conferido ligando para o fornecedor num número já cadastrado, nunca num informado na mensagem, e uma segunda pessoa aprova a mudança. O Sr. Nowak explica que essa única regra impede a maior parte das fraudes de faturas, seja qual for a aparência do e-mail, porque o criminoso não consegue atender o telefone no escritório do fornecedor verdadeiro.

### 3.3 A regra em ação

Duas semanas depois, o escritório recebe um e-mail aparentemente do fornecedor de equipamentos, com um número de fatura correto e o pedido de pagar numa conta nova antes do fim do dia. A assistente do escritório segue a regra e liga para o fornecedor no número que consta nos registros da clínica. O fornecedor não enviou mensagem alguma e diz que sua própria caixa postal pode ter sido comprometida. A clínica não paga nada à conta nova. Sofia registra a tentativa, encaminha o e-mail ao fornecedor e agradece à assistente na frente da equipe.

### 3.4 Treinamento curto

Sofia conduz uma sessão de dez minutos na reunião semanal da equipe, usando dois exemplos sintéticos parecidos com os e-mails da clínica, um sobre uma encomenda e outro sobre um pedido de reembolso de seguro para animais. A equipe encontra os sinais em conjunto e combina o que fazer. O Sr. Nowak desaconselha treinamentos anuais longos para uma clínica desse tamanho; sessões curtas, regulares e relevantes são mais lembradas. Sofia planeja um tema curto por mês, escolhido entre as perguntas que a equipe fez, e mantém uma lista dos temas tratados para que os novos funcionários possam se atualizar na primeira semana.

### 3.5 Comunicação sem culpa

Sofia cria um único meio de comunicar qualquer coisa suspeita: encaminhar para ela ou avisá-la no balcão. A Dra. Moss diz à equipe que ninguém será criticado por clicar num link ou cometer um erro, desde que comunique depressa, porque as comunicações precoces tornam os problemas menores. Em uma semana, uma recepcionista comunica que digitou a senha numa página que parecia estranha. Sofia redefine a senha na mesma manhã e confere a conta, sem encontrar uso indevido. O Sr. Nowak observa que o segundo fator também teria bloqueado uma entrada com aquela senha.

### Exemplo resolvido

Sofia ensina os sinais de phishing, define uma regra de ligação de volta que barra uma tentativa sintética de fraude de faturas, conduz sessões mensais de dez minutos e recebe uma comunicação rápida e sem culpa de uma senha digitada.

> **Caso sintético.** Os e-mails e os fornecedores são sintéticos.

### Erros e limites

Ligar para o número de uma mensagem suspeita leva ao criminoso, e não ao fornecedor.

### Exercícios

- **EX027 — Quatro sinais.** Cite dois sinais de phishing. *Rubrica:* 3 = remetente que não corresponde, urgência, link estranho, pedido de senha ou pagamento;; 2 = dois;; 1 = um;; 0 = nenhuma.

- **EX028 — E-mail da transportadora.** Para onde levava o link do e-mail da transportadora? *Rubrica:* 3 = um endereço parecido;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX029 — Hábito principal.** O que importa mais do que decorar os sinais? *Rubrica:* 3 = parar e conferir;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX030 — Regra bancária.** Qual é a regra para mudanças de dados bancários? *Rubrica:* 3 = ligar para um número conhecido, segunda aprovação;; 2 = as duas;; 1 = uma;; 0 = nenhuma.

- **EX031 — Por que funciona.** Por que a regra da ligação de volta impede a fraude? *Rubrica:* 3 = o criminoso não atende o telefone do fornecedor verdadeiro;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX032 — Fatura falsa.** De qual fornecedor o e-mail falso se fazia passar? *Rubrica:* 3 = o fornecedor de equipamentos;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX033 — Desfecho.** Quanto a clínica pagou à conta nova? *Rubrica:* 3 = nada; o pedido foi recusado depois da ligação;; 2 = nada, sem dizer por quê;; 1 = errado;; 0 = sem resposta.

- **EX034 — Duração do treinamento.** Quanto dura cada sessão com a equipe? *Rubrica:* 3 = dez minutos;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX035 — Origem dos temas.** Como são escolhidos os temas mensais? *Rubrica:* 3 = pelas perguntas da equipe;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX036 — Via de comunicação.** Como a equipe comunica algo suspeito? *Rubrica:* 3 = encaminha a Sofia ou a avisa;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.

- **EX037 — Promessa da dona.** O que a Dra. Moss prometeu à equipe? *Rubrica:* 3 = nenhuma crítica para comunicações rápidas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX038 — Senha digitada.** O que Sofia fez sobre a senha digitada? *Rubrica:* 3 = redefiniu-a e conferiu a conta;; 2 = os dois;; 1 = um;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Backups, incidentes e o plano adiante

### Objetivos de aprendizagem

Você vai (1) confirmar que a clínica consegue restaurar seus dados; (2) escrever um cartão de incidentes de uma página; (3) definir um plano simples para os meses depois do curso.

### 4.1 Backups

Sofia pergunta ao provedor do sistema da clínica como os dados têm backup e com que rapidez poderiam ser restaurados. O provedor guarda backups diários por trinta dias e consegue restaurar em até um dia. O e-mail e os arquivos compartilhados da clínica não têm backup separado, de modo que uma exclusão percebida tarde seria perdida. A Dra. Moss aprova um serviço de backup de baixo custo para o e-mail e os arquivos. O Sr. Nowak explica que um provedor manter seu serviço funcionando não significa que os seus arquivos apagados ou cifrados possam ser recuperados, o que surpreende várias pessoas da turma.

### 4.2 Teste de uma restauração

Sofia pede ao técnico que restaure uma pasta e uma caixa postal do novo backup numa área de teste. A pasta é restaurada em minutos. A restauração da caixa postal falha na primeira tentativa porque o backup ainda não tinha concluído sua primeira cópia completa. Na segunda tentativa, uma semana depois, ela funciona. Sofia registra os dois resultados no log de mudanças. O Sr. Nowak a elogia por testar, porque muitas empresas só descobrem os problemas de backup quando precisam do backup, no pior momento possível e com clientes esperando no balcão.

### 4.3 Um cartão de incidentes

Sofia escreve um cartão de incidentes de uma página e o afixa no escritório. Ele lista o que conta como incidente, como um tablet perdido, um alerta de entrada suspeita, uma mensagem de resgate ou dados de clientes enviados à pessoa errada; para quem ligar primeiro, que é Sofia, depois a Dra. Moss e depois o técnico; os primeiros passos, como desconectar da rede um computador afetado; e os telefones do provedor do sistema da clínica e do consultor de proteção de dados. Ela também mantém uma folha de consultas em papel para o dia, caso o sistema fique indisponível.

### 4.4 Um exercício prático

Sofia conduz um exercício de vinte minutos com a Dra. Moss e duas recepcionistas. O cenário: numa segunda-feira de manhã, o sistema da clínica fica indisponível por quatro horas. A equipe usa a folha em papel, liga para os clientes com consultas urgentes a partir de uma lista impressa e registra os tratamentos em papel para lançá-los depois. Eles descobrem que a lista impressa tem três semanas e não inclui os clientes novos. Sofia cria um lembrete semanal para imprimir uma lista nova e trancá-la no escritório. O Sr. Nowak observa que os exercícios encontram pequenas lacunas que são fáceis de corrigir antes e dolorosas de descobrir durante uma indisponibilidade real.

### 4.5 O plano adiante

Na última sessão, Sofia lista o que mudou no mês: contas pessoais e segundos fatores para todos, atualizações religadas, doze arquivos sensíveis que não estão mais abertos a qualquer pessoa, uma regra de ligação de volta que barrou uma tentativa de fraude, um backup testado e um cartão de incidentes. Ela define uma breve rotina mensal: repetir a verificação de compartilhamento, revisar as contas de quem saiu, dar uma sessão de dez minutos e testar uma restauração. O Sr. Nowak recomenda em seguida o curso rápido de governança de dados, já que a retenção dos registros antigos de clientes da clínica é a próxima pergunta que a Dra. Moss quer ver respondida.

### Exemplo resolvido

Sofia acrescenta um backup para o e-mail e os arquivos, testa uma restauração que falha uma vez e depois funciona, afixa um cartão de incidentes de uma página, encontra numa simulação uma lista de clientes desatualizada e define uma rotina mensal de quatro itens.

> **Caso sintético.** Os provedores, os tempos e os exercícios são sintéticos.

### Erros e limites

Presumir que um provedor de nuvem recuperará seus arquivos apagados ou cifrados pode deixar a empresa sem cópia alguma.

### Exercícios

- **EX039 — Backups do provedor.** Por quanto tempo o provedor do sistema da clínica guarda os backups? *Rubrica:* 3 = trinta dias;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX040 — Backup ausente.** O que não tinha backup separado? *Rubrica:* 3 = o e-mail e os arquivos compartilhados;; 2 = os dois;; 1 = um;; 0 = nenhuma.

- **EX041 — Primeira falha.** Por que a primeira restauração da caixa postal falhou? *Rubrica:* 3 = a primeira cópia completa não tinha terminado;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX042 — Primeira ligação.** Para quem se liga primeiro num incidente? *Rubrica:* 3 = Sofia;; 2 = parcialmente correto;; 1 = outra pessoa;; 0 = nenhuma.

- **EX043 — Primeiro passo.** Qual é um primeiro passo para um computador afetado? *Rubrica:* 3 = desconectá-lo da rede;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX044 — Alternativa em papel.** Que alternativa em papel Sofia mantém? *Rubrica:* 3 = a folha de consultas do dia;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

- **EX045 — Duração do exercício.** Quanto durou o exercício prático? *Rubrica:* 3 = vinte minutos;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX046 — Lacuna do exercício.** Que lacuna o exercício encontrou? *Rubrica:* 3 = a lista impressa de clientes tinha três semanas;; 2 = parcialmente correto;; 1 = vaga;; 0 = nenhuma.

- **EX047 — Correção da lacuna.** Como a lacuna do exercício foi corrigida? *Rubrica:* 3 = impressão nova toda semana, trancada;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.

- **EX048 — Arquivos sensíveis.** Quantos arquivos sensíveis foram fechados? *Rubrica:* 3 = doze;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX049 — Rotina mensal.** Cite dois itens da rotina mensal. *Rubrica:* 3 = verificação de compartilhamento, desligamentos, sessão, teste de restauração;; 2 = dois;; 1 = um;; 0 = nenhuma.

- **EX050 — Próximo passo.** Que curso vem a seguir e por quê? *Rubrica:* 3 = governança de dados rápido, retenção de registros antigos;; 2 = os dois;; 1 = um;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX050. Sofia Lindqvist, o Sr. Tomasz Nowak, o Eastgate Training Centre, a Hollybank Veterinary Practice e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Um mês, com quatro sessões semanais.

**EX002.** Uma empresa vizinha perdeu uma semana de trabalho por causa de um ransomware.

**EX003.** Dezoito funcionários.

**EX004.** No sistema de gestão clínica em nuvem.

**EX005.** Nove computadores e dois tablets.

**EX006.** Proteção que não atrase o balcão da recepção.

**EX007.** Por e-mail, de um laboratório externo.

**EX008.** Pelo dano que um vazamento, uma alteração ou uma perda causaria: alto, médio ou baixo.

**EX009.** Manter o sistema de gestão clínica disponível durante o horário de funcionamento.

**EX010.** Não pagar uma fatura fraudulenta de fornecedor.

**EX011.** A ISO/IEC 27000:2026.

**EX012.** Apenas Sofia e a Dra. Moss.

**EX013.** Para que os problemas posteriores possam ser rastreados até sua causa.

**EX014.** Um único login compartilhado escrito num bilhete embaixo do teclado.

**EX015.** Alguns segundos, cronometrados durante uma manhã movimentada.

**EX016.** A Dra. Moss e a equipe do escritório, que cuida dos pagamentos.

**EX017.** Dois enfermeiros não queriam aplicativos de trabalho nos celulares pessoais.

**EX018.** Uma atualização tinha quebrado uma impressora de etiquetas antiga.

**EX019.** O técnico instalou um driver de impressora mais novo.

**EX020.** Uma senha de acesso e apagamento remoto.

**EX021.** 47 de 300 arquivos sintéticos.

**EX022.** 25 de 80 arquivos de marketing.

**EX023.** Doze: 8 arquivos de clientes e 4 do financeiro.

**EX024.** Os funcionários de meio período as consultavam de casa nos celulares pessoais.

**EX025.** Para o sistema da clínica, atrás do login.

**EX026.** Os novos compartilhamentos passam a ser restritos à clínica por padrão.

**EX027.** Um endereço de remetente que não corresponde e uma urgência inesperada.

**EX028.** Um endereço parecido.

**EX029.** O hábito de parar e conferir.

**EX030.** Ligar para o fornecedor num número cadastrado e obter uma segunda aprovação.

**EX031.** O criminoso não consegue atender o telefone do fornecedor verdadeiro.

**EX032.** O fornecedor de equipamentos.

**EX033.** Nada; o pedido foi recusado depois da ligação.

**EX034.** Dez minutos, na reunião semanal da equipe.

**EX035.** Pelas perguntas que a equipe fez.

**EX036.** Encaminhá-lo a Sofia ou avisá-la no balcão.

**EX037.** Ninguém será criticado por um erro comunicado depressa.

**EX038.** Redefiniu a senha naquela manhã e conferiu a conta em busca de uso indevido.

**EX039.** Backups diários guardados por trinta dias.

**EX040.** O e-mail e os arquivos compartilhados da clínica.

**EX041.** O backup ainda não tinha concluído sua primeira cópia completa.

**EX042.** Sofia, depois a Dra. Moss e depois o técnico.

**EX043.** Desconectá-lo da rede.

**EX044.** Uma folha de consultas em papel para o dia.

**EX045.** Vinte minutos.

**EX046.** A lista impressa de clientes tinha três semanas.

**EX047.** Um lembrete semanal para imprimir uma lista nova e trancá-la.

**EX048.** Doze arquivos de clientes e do financeiro.

**EX049.** Repetir a verificação de compartilhamento e testar uma restauração.

**EX050.** O curso rápido de governança de dados, para tratar da retenção dos registros antigos de clientes.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
