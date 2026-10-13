# Segurança da Informação: Curso Profissional

- Idioma: português do Brasil (`pt`); curso 025, curso profissional (6 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 12 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 7–12 (EX031–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: profissionais em atividade que assumem a segurança da informação junto com outra função numa firma pequena ou média.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios medem a cobertura da entrada com múltiplos fatores por tipo de conta num diretório sintético e classificam um registro sintético de riscos por probabilidade vezes impacto. As normas são citadas pela edição e parafraseadas; os pontos jurídicos são gerais e exigem orientação profissional. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um gerente administrativo desde a compreensão da firma e de seus riscos, passando pelas contas, pelos dispositivos, pela fraude de pagamentos, pelos fornecedores e pelas pessoas, até os incidentes, a continuidade, a política e os relatórios à liderança. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Daniel Reyes** | Gerente administrativo e aluno | Inventado |
| **Sra. Helen Ashby** | Tutora | Inventada |
| **Kingsmere Professional Institute** | Instituto fictício | Inventado |
| **Corbridge Accountancy Partners** | Firma fictícia, com oito sócios, cerca de sessenta funcionários e dois mil clientes | Inventada |

### Fontes principais

ISO/IEC 27000:2026; ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022); ISO/IEC 27002:2022; NIST SP 800-30 Rev. 1. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Um profissional em atividade volta a estudar

### Objetivos de aprendizagem

Você vai (1) descrever o que cobre o curso profissional de seis meses; (2) conhecer o caso que acompanha o livro; (3) combinar as regras básicas para trabalhar com um empregador real.

### 1.1 O aluno

Daniel Reyes é um gerente administrativo a quem pediram que assumisse a segurança da informação em seu empregador junto com o trabalho que já faz. Ele se matricula num curso profissional de seis meses no fictício Kingsmere Professional Institute, estudando duas noites por semana. Sua tutora, a Sra. Helen Ashby, passou quinze anos comandando a segurança de firmas médias antes de lecionar. Ela diz à turma que a maioria deles será a única pessoa da organização com segurança no título do cargo, por isso o curso se concentra no julgamento, nas prioridades e na comunicação clara, e não em habilidades técnicas profundas.

### 1.2 O empregador

Daniel trabalha na fictícia Corbridge Accountancy Partners, uma firma de oito sócios e cerca de sessenta funcionários em dois escritórios. A firma guarda declarações de impostos, arquivos de folha de pagamento, extratos bancários e documentos de identidade de cerca de dois mil clientes. O e-mail, os arquivos e o software de contabilidade rodam todos em serviços em nuvem, com um pequeno servidor de arquivos mantido no escritório principal para os registros mais antigos. Uma empresa de suporte externa cuida dos dispositivos. Daniel se reporta à sócia-gerente, a Sra. Joanna Pike, que quer uma resposta simples a uma pergunta: estamos fazendo as coisas certas, e o que devemos fazer em seguida?

### 1.3 Como o curso funciona

Os doze capítulos vão da compreensão da firma e de seus riscos, passando pelas contas, pelos dispositivos, pelo e-mail, pelos fornecedores e pelas pessoas, até os incidentes, a continuidade, a política, a medição e os relatórios à liderança. Cada capítulo termina com uma tarefa que Daniel aplica na Corbridge, e a Sra. Ashby revisa os resultados numa breve ligação semanal. Dois laboratórios usam pequenos scripts em Python sobre dados sintéticos: um mede a cobertura da entrada com múltiplos fatores e outro classifica um registro de riscos. Daniel nunca escreveu código, por isso a Sra. Ashby explica que ele só precisa ler e executar os scripts, não escrevê-los do zero.

### 1.4 Regras básicas

A Sra. Ashby define três regras. Primeiro, obter a concordância por escrito da Sra. Pike antes de verificar qualquer sistema, mesmo um que Daniel já use diariamente. Segundo, nunca copiar dados reais de clientes nos trabalhos do curso; descrevê-los ou usar exemplos sintéticos. Terceiro, registrar cada achado com a data, a evidência e a pessoa informada, para que um colega possa seguir a trilha depois. Daniel escreve uma nota de escopo de uma página listando o que pode examinar, e a Sra. Pike a assina. A Sra. Ashby explica que a nota protege Daniel se alguém perguntar depois por que ele estava examinando configurações fora de seu trabalho habitual.

### Exemplo resolvido

Daniel entra no curso profissional, conhece os sessenta funcionários e os dois mil clientes da Corbridge e obtém uma nota de escopo assinada antes de verificar qualquer coisa.

> **Caso sintético.** O Kingsmere, a Corbridge e todas as pessoas são sintéticos.

### Erros e limites

Verificar sistemas sem concordância por escrito pode abalar a confiança mesmo quando a intenção é boa.

### Exercícios

- **EX001 — Duração do curso.** Quanto dura o curso de Daniel? *Rubrica:* 3 = seis meses;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX002 — Registros de clientes.** Aproximadamente de quantos clientes a Corbridge guarda registros? *Rubrica:* 3 = cerca de dois mil;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX003 — Pergunta da liderança.** O que a Sra. Pike quer ver respondido? *Rubrica:* 3 = estamos fazendo as coisas certas, e o que vem a seguir;; 2 = as duas partes;; 1 = uma parte;; 0 = nenhuma.

- **EX004 — Nota de escopo.** Por que Daniel obtém uma nota de escopo assinada? *Rubrica:* 3 = concordância por escrito antes de verificar;; 2 = correto;; 1 = vaga;; 0 = nenhuma.

- **EX005 — Programação necessária.** Daniel precisa escrever os scripts dos laboratórios? *Rubrica:* 3 = não, só lê-los e executá-los;; 2 = correto;; 1 = errado;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Entendendo a firma

### Objetivos de aprendizagem

Você vai (1) mapear as informações que uma firma de serviços profissionais guarda; (2) identificar quem depende delas; (3) declarar o que a firma não pode se dar ao luxo de perder.

### 2.1 Inventário de informações

Daniel passa a primeira semana listando o que a Corbridge guarda. Os documentos de identidade e os extratos bancários dos clientes chegam por e-mail e por um portal de envio. As declarações de impostos e os cálculos da folha de pagamento ficam no software de contabilidade. As cartas de contratação e os papéis de trabalho ficam em pastas compartilhadas na nuvem. Os registros dos funcionários ficam num serviço de folha de pagamento. Os arquivos de clientes mais antigos, alguns com mais de dez anos, continuam no servidor de arquivos do escritório. Ele registra cada tipo com a localização, o responsável e o volume aproximado numa planilha e anota onde a mesma informação é copiada em mais de um lugar, porque cada cópia precisa de proteção.

### 2.2 Quem depende delas

Daniel pergunta a cada sócio sem quais informações eles não conseguiriam trabalhar por uma semana. As respostas se concentram em três coisas: o software de contabilidade durante a temporada de impostos, o sistema de e-mail para a comunicação com os clientes e o portal dos clientes para a coleta de documentos. Ele também pergunta à recepção e à equipe da folha de pagamento, que acrescentam o sistema telefônico e o serviço de folha de pagamento. A Sra. Ashby explica que a dependência é tão importante quanto a sensibilidade. Um sistema que guarda poucos dados pessoais ainda pode parar a empresa se falhar, e esse tipo de risco muitas vezes escapa a quem pensa apenas em sigilo.

### 2.3 Objetivos de segurança

A Sra. Ashby apresenta os três objetivos que a ISO/IEC 27000:2026 usa para descrever a segurança da informação: confidencialidade, integridade e disponibilidade. Para a Corbridge, a confidencialidade importa mais para os documentos de identidade e os extratos bancários. A integridade importa mais para os cálculos de impostos e para os dados bancários dos clientes usados nas restituições, porque um número ou uma conta alterados causam dano financeiro direto. A disponibilidade importa mais nas semanas que antecedem os prazos de entrega das declarações, quando uma indisponibilidade de um único dia já causa entregas perdidas. Daniel acrescenta ao inventário uma coluna que marca o objetivo mais importante para cada tipo de informação, com uma frase explicando por quê.

### 2.4 O que não pode ser perdido

Daniel redige uma breve declaração para a Sra. Pike: a firma não pode se dar ao luxo de um vazamento dos documentos de identidade dos clientes, de uma alteração nos dados bancários de restituição dos clientes nem da perda do software de contabilidade em janeiro. Ela concorda e acrescenta um quarto item tirado da própria experiência: a reputação de discrição da firma, que traz a maior parte dos novos clientes por indicação. A Sra. Ashby diz a Daniel que essa declaração vai orientar todas as decisões de prioridade no resto do curso e que uma lista curta acordada com a liderança vale mais do que uma lista longa escrita sozinho.

### Exemplo resolvido

Daniel inventaria as informações da Corbridge, descobre de que os sócios dependem, liga cada tipo a um objetivo de segurança e acorda quatro coisas que a firma não pode perder.

> **Caso sintético.** Os tipos e os volumes de informação são sintéticos.

### Erros e limites

Listar apenas os dados sensíveis deixa de fora os sistemas de que a empresa depende para operar.

### Exercícios

- **EX006 — Três objetivos.** Quais três objetivos a ISO/IEC 27000:2026 usa? *Rubrica:* 3 = confidencialidade, integridade, disponibilidade;; 2 = os três;; 1 = dois;; 0 = nenhuma.

- **EX007 — Exemplo de integridade.** Dê um exemplo de integridade na Corbridge. *Rubrica:* 3 = os dados bancários de restituição dos clientes;; 2 = correto;; 1 = vago;; 0 = nenhuma.

- **EX008 — Pico de disponibilidade.** Quando a disponibilidade importa mais? *Rubrica:* 3 = nas semanas antes dos prazos de entrega;; 2 = correto;; 1 = vago;; 0 = nenhuma.

- **EX009 — Quarto item.** O que a Sra. Pike acrescentou à lista? *Rubrica:* 3 = a reputação de discrição da firma;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX010 — Lição da dependência.** Por que perguntar sobre a dependência além da sensibilidade? *Rubrica:* 3 = sistemas pouco sensíveis ainda podem parar a empresa;; 2 = correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — O risco em termos simples

### Objetivos de aprendizagem

Você vai (1) descrever o risco como probabilidade e impacto; (2) montar um pequeno registro de riscos; (3) classificar os riscos com um script simples.

### 3.1 O que significa risco

A Sra. Ashby define um risco como algo que pode dar errado, descrito pela probabilidade de acontecer e pelo dano que causaria. A NIST SP 800-30 Revision 1, o guia para a condução de avaliações de risco, usa as mesmas duas ideias, embora com mais detalhes. Ela pede à turma que escreva cada risco como uma frase curta que nomeie a causa e o resultado, como phishing leva à tomada da caixa postal. Entradas vagas como ataque cibernético não permitem ação, porque ninguém sabe qual controle ajudaria nem quem deveria ser responsável pelo trabalho.

### 3.2 Montagem do registro

Daniel lista oito riscos para a Corbridge depois de conversar com os sócios e com a empresa de suporte. Ele dá a cada um uma nota de um a cinco para a probabilidade e para o impacto, usando descrições simples: uma probabilidade quatro significa que aconteceu várias vezes recentemente com firmas semelhantes; um impacto cinco significa dano aos clientes, notificação a reguladores e perda de clientes. A Sra. Ashby lembra que as notas são julgamentos, não medições, e que seu valor está em forçar uma conversa sobre quais riscos importam mais. Ele registra quem deu cada nota e por quê.

### Laboratório — Classificando um registro sintético de riscos por probabilidade vezes impacto

```python
"""Score a synthetic risk register by likelihood x impact and rank it (stdlib only)."""
risks = [
    ("R1 phishing leads to mailbox takeover", 4, 4),
    ("R2 laptop lost with client files", 3, 4),
    ("R3 ransomware on file server", 2, 5),
    ("R4 payment diversion by fake invoice", 3, 5),
    ("R5 leaver keeps cloud access", 3, 3),
    ("R6 backup fails silently", 2, 4),
    ("R7 website defaced", 2, 2),
    ("R8 tax software vendor breach", 1, 4),
]
scored = sorted(((l * i, name, l, i) for name, l, i in risks), reverse=True)
for s, name, l, i in scored:
    band = "high" if s >= 15 else "medium" if s >= 8 else "low"
    print(f"{s:>2} {band:<6} {name} (L{l} x I{i})")
print("high:", sum(1 for s, *_ in scored if s >= 15), "medium:", sum(1 for s, *_ in scored if 8 <= s < 15), "low:", sum(1 for s, *_ in scored if s < 8))
```

Execute com `python3 lab_risk.py`. Saída verificada:

```text
16 high   R1 phishing leads to mailbox takeover (L4 x I4)
15 high   R4 payment diversion by fake invoice (L3 x I5)
12 medium R2 laptop lost with client files (L3 x I4)
10 medium R3 ransomware on file server (L2 x I5)
 9 medium R5 leaver keeps cloud access (L3 x I3)
 8 medium R6 backup fails silently (L2 x I4)
 4 low    R8 tax software vendor breach (L1 x I4)
 4 low    R7 website defaced (L2 x I2)
high: 2 medium: 4 low: 2
```

### 3.3 Leitura da classificação

O script multiplica a probabilidade pelo impacto e ordena o registro. Dois riscos somam quinze ou mais e são marcados como altos: o phishing que leva à tomada da caixa postal, com dezesseis, e o desvio de pagamento por fatura falsa, com quinze. Quatro são médios, dos notebooks perdidos, com doze, até a falha silenciosa do backup, com oito. Dois são baixos, com quatro cada: uma violação no fornecedor do software de impostos e a desfiguração do site. Daniel percebe que os dois riscos altos começam com um e-mail, o que lhe diz por onde começar e lhe dá uma mensagem simples para os sócios.

### 3.4 Limites das notas

A Sra. Ashby adverte contra tratar os números como precisos. Uma violação no fornecedor recebeu nota baixa porque Daniel a julgou improvável, mas seu impacto poderia atingir todos os clientes de uma vez. Ela sugere manter uma breve nota ao lado de qualquer risco de nota baixa com um pior caso grave, para que a liderança o veja em vez de deixá-lo escondido no fim de uma lista. Daniel acrescenta essa nota ao risco do fornecedor e planeja perguntar ao fornecedor sobre sua própria segurança no capítulo dos fornecedores. Ele também marca uma data para revisar todas as notas em três meses.

### Exemplo resolvido

Daniel dá notas a oito riscos sintéticos; o script classifica como altos a tomada por phishing (16) e a fraude de faturas (15), quatro como médios e dois como baixos, e ele destaca o pior caso grave do risco do fornecedor.

> **Caso sintético.** Os riscos e as notas são sintéticos.

### Erros e limites

Tratar notas baseadas em julgamento como medições precisas esconde a incerteza de quem decide.

### Exercícios

- **EX011 — Principal risco.** Qual risco fica em primeiro lugar e com que nota? *Rubrica:* 3 = tomada da caixa postal por phishing, 16;; 2 = os dois;; 1 = um;; 0 = nenhuma.

- **EX012 — Número de riscos altos.** Quantos riscos são altos? *Rubrica:* 3 = dois;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX013 — Causa comum.** Com o que começam os dois riscos altos? *Rubrica:* 3 = um e-mail;; 2 = correto;; 1 = vago;; 0 = nenhuma.

- **EX014 — Nota do fornecedor.** Por que acrescentar uma nota ao risco do fornecedor? *Rubrica:* 3 = nota baixa, mas pior caso grave;; 2 = correto;; 1 = vaga;; 0 = nenhuma.

- **EX015 — Boa frase de risco.** Como um risco deve ser escrito? *Rubrica:* 3 = causa e resultado numa frase curta;; 2 = os dois;; 1 = um;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Contas e entrada com múltiplos fatores

### Objetivos de aprendizagem

Você vai (1) explicar por que a entrada com múltiplos fatores importa; (2) medir a cobertura por tipo de conta; (3) planejar correções para as lacunas.

### 4.1 Por que importa

O principal risco de Daniel é a tomada da caixa postal depois de um phishing. A Sra. Ashby explica que uma senha roubada basta para tomar uma conta protegida apenas por senha, mas um segundo fator, como uma notificação num aplicativo ou uma chave de segurança, impede a maioria dessas tentativas. Ela observa que os atacantes tentam cada vez mais induzir os usuários a aprovar as notificações, por isso o método também importa. Daniel decide medir quantas contas da Corbridge já usam um segundo fator antes de propor qualquer coisa, porque uma recomendação baseada em números é mais fácil de ser aceita pelos sócios.

### 4.2 Tipos de conta

Daniel exporta uma lista de contas do serviço de e-mail e de identidade, com permissão da Sra. Pike, e as agrupa em quatro tipos: sócios, funcionários, administradores e contas de serviço. As contas de serviço são usadas por software, e não por pessoas, como o scanner que envia documentos por e-mail para as pastas. Ele substitui os nomes por códigos antes de usar a lista nos trabalhos do curso. A Sra. Ashby observa que os administradores merecem atenção separada, porque uma única conta de administrador comprometida pode mudar as configurações de todos, de modo que a cobertura deles importa mais do que o total geral.

### Laboratório — Cobertura da entrada com múltiplos fatores por tipo de conta num diretório sintético

```python
"""Measure multi-factor sign-in coverage by account type in a synthetic directory (stdlib only)."""
import random
from collections import Counter
random.seed(25)
accounts = []
for kind, n, p in [("partner", 8, 0.75), ("staff", 52, 0.6), ("admin", 4, 0.5), ("service", 6, 0.0)]:
    for i in range(n):
        accounts.append((kind, random.random() < p))
total = Counter(k for k, _ in accounts)
on = Counter(k for k, m in accounts if m)
for k in total:
    print(f"{k}: {on[k]} of {total[k]} with MFA ({on[k]/total[k]:.1%})")
print(f"all accounts: {sum(on.values())} of {len(accounts)} ({sum(on.values())/len(accounts):.1%})")
```

Execute com `python3 lab_mfa.py`. Saída verificada:

```text
partner: 4 of 8 with MFA (50.0%)
staff: 39 of 52 with MFA (75.0%)
admin: 1 of 4 with MFA (25.0%)
service: 0 of 6 with MFA (0.0%)
all accounts: 44 of 70 (62.9%)
```

### 4.3 Leitura dos resultados

O script encontra 44 de 70 contas sintéticas usando um segundo fator, 62,9 por cento no total. Os funcionários estão no topo, com 39 de 52, ou 75 por cento. Os sócios estão em 4 de 8, ou 50 por cento. Os administradores são os mais baixos entre as pessoas, com 1 de 4, ou 25 por cento. Nenhuma das seis contas de serviço usa um segundo fator. Daniel vê que o número geral esconde as lacunas mais importantes: as contas com mais poder e os sócios que aprovam pagamentos são os menos protegidos, o que corresponde ao risco de fraude de faturas. Ele compartilha a tabela com a empresa de suporte antes que os sócios a vejam.

### 4.4 Fechando as lacunas

Daniel propõe ativar um segundo fator para todos os administradores em uma semana e para todos os sócios em um mês, com a empresa de suporte presente para ajudar. Para as contas de serviço, que muitas vezes não conseguem usar um segundo fator, ele pede à empresa de suporte que restrinja de onde cada uma pode entrar e que remova as que não forem mais necessárias. A Sra. Ashby o aconselha a explicar a mudança aos sócios em termos do risco de fraude de faturas que já os preocupa, e não como uma regra técnica. A Sra. Pike concorda em ser a primeira, para dar o exemplo.

### Exemplo resolvido

Daniel mede a cobertura sintética: 44 de 70 contas (62,9 por cento), administradores 1 de 4, sócios 4 de 8, contas de serviço 0 de 6, e planeja as correções começando pelos administradores.

> **Caso sintético.** As contas são sintéticas e anonimizadas.

### Erros e limites

Um número geral de cobertura pode esconder lacunas nas contas mais poderosas.

### Exercícios

- **EX016 — Cobertura geral.** Qual é a cobertura geral de MFA? *Rubrica:* 3 = 44 de 70, 62,9 por cento;; 2 = os dois;; 1 = um;; 0 = nenhuma.

- **EX017 — Administradores.** Quantos administradores usam MFA? *Rubrica:* 3 = 1 de 4;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX018 — Contas de serviço.** O que Daniel faz em relação às contas de serviço? *Rubrica:* 3 = restringe os locais de entrada, remove as sem uso;; 2 = os dois;; 1 = um;; 0 = nenhuma.

- **EX019 — Argumento aos sócios.** Como a mudança deve ser explicada aos sócios? *Rubrica:* 3 = em termos do risco de fraude de faturas;; 2 = correto;; 1 = vago;; 0 = nenhuma.

- **EX020 — Quem vai primeiro.** Quem concorda em ativar a MFA primeiro? *Rubrica:* 3 = a Sra. Pike;; 2 = correto;; 1 = outra pessoa;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Dispositivos e dados no escritório

### Objetivos de aprendizagem

Você vai (1) definir uma linha de base para os notebooks; (2) lidar com o antigo servidor de arquivos; (3) reduzir os riscos do papel e das mídias removíveis.

### 5.1 Linha de base dos notebooks

A empresa de suporte administra os notebooks da Corbridge, mas ninguém escreveu como é um notebook configurado corretamente. Daniel redige com ela uma breve linha de base: criptografia de disco ligada, atualizações automáticas ligadas, bloqueio de tela após cinco minutos, uso de contas padrão pela equipe e possibilidade de apagar o dispositivo remotamente se for perdido. Ele pede um relatório mensal mostrando quantos notebooks cumprem cada item. A Sra. Ashby explica que uma linha de base escrita transforma uma confiança vaga num fornecedor em algo que pode ser verificado e que o relatório mensal dá a Daniel evidências para a liderança.

### 5.2 O antigo servidor de arquivos

O servidor de arquivos do escritório guarda arquivos de clientes com mais de dez anos. Daniel descobre que as regras de retenção da firma dizem que a maioria dos registros de clientes precisa ser guardada por um número definido de anos, depois do qual deve ser destruída. Ele pede a um sócio que revise uma amostra e encontra muitos arquivos bem além desse período. Mantê-los acrescenta risco sem benefício. Com a aprovação da Sra. Pike, ele planeja uma limpeza supervisionada, começando por uma lista das pastas por idade, e pede à empresa de suporte que confirme que os backups dos arquivos apagados também expiram no prazo.

### 5.3 Papel e mídias

A Corbridge ainda recebe documentos em papel de alguns clientes mais antigos. Daniel encontra uma bandeja de originais digitalizados aguardando devolução, guardada numa prateleira aberta perto da recepção. Ele os leva para um armário trancado e define uma regra: os originais são devolvidos ou triturados com segurança em até duas semanas depois da digitalização. Ele também encontra dois pen drives sem criptografia usados para levar arquivos entre os escritórios. Ele os substitui pelas pastas na nuvem que já estão disponíveis e pede à empresa de suporte que bloqueie o armazenamento removível sem criptografia nos notebooks, com exceções apenas mediante pedido.

### 5.4 Acompanhamento do progresso

Depois de um mês, o relatório da empresa de suporte mostra 55 de 60 notebooks cumprindo a linha de base completa. As cinco exceções incluem dois notebooks que perderam atualizações enquanto os funcionários estavam de licença e três em que a criptografia nunca foi ligada. Daniel acompanha cada um e registra a correção. A limpeza do servidor de arquivos remove uma grande parte das pastas vencidas, depois da aprovação de um sócio para cada lote. Ele registra o que foi apagado e por quê, para que a firma possa responder a perguntas depois. A Sra. Ashby elogia o registro tanto quanto a própria limpeza.

### Exemplo resolvido

Daniel escreve uma linha de base de cinco itens para os notebooks, encontra 55 de 60 notebooks em conformidade depois de um mês, limpa os arquivos vencidos do servidor com aprovação dos sócios e tranca os originais em papel.

> **Caso sintético.** As contagens de dispositivos e os achados são sintéticos.

### Erros e limites

Apagar registros antigos sem aprovação e sem log pode violar os deveres de retenção ou deixar a firma sem condições de explicar o que aconteceu.

### Exercícios

- **EX021 — Itens da linha de base.** Cite três itens da linha de base dos notebooks. *Rubrica:* 3 = criptografia, atualizações, bloqueio de tela, contas padrão, apagamento remoto;; 2 = três;; 1 = dois;; 0 = nenhuma.

- **EX022 — Conformidade.** Quantos notebooks cumpriam a linha de base depois de um mês? *Rubrica:* 3 = 55 de 60;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX023 — Arquivos antigos.** Por que remover os arquivos vencidos do servidor? *Rubrica:* 3 = risco sem benefício;; 2 = correto;; 1 = vago;; 0 = nenhuma.

- **EX024 — Regra do papel.** Que regra Daniel definiu para os originais em papel? *Rubrica:* 3 = devolvidos ou triturados em até duas semanas;; 2 = correto;; 1 = vaga;; 0 = nenhuma.

- **EX025 — Pen drives.** O que substituiu os pen drives? *Rubrica:* 3 = as pastas na nuvem já existentes;; 2 = correto;; 1 = outra coisa;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — E-mail e fraude de pagamentos

### Objetivos de aprendizagem

Você vai (1) explicar como funciona a fraude de faturas e de pagamentos; (2) projetar verificações que a impeçam; (3) preparar a equipe para ela.

### 6.1 Como a fraude funciona

O segundo risco alto de Daniel é o desvio de pagamentos. A Sra. Ashby explica o padrão habitual: um criminoso obtém acesso à caixa postal de um fornecedor ou de um cliente, ou registra um endereço parecido, e envia uma mensagem convincente dizendo que os dados bancários mudaram. A equipe atualiza os dados, e o pagamento seguinte vai para o criminoso. Numa firma de contabilidade, o mesmo truque pode mirar as restituições de impostos dos clientes. As mensagens muitas vezes chegam em períodos de muito trabalho e mencionam faturas reais, e é por isso que pessoas cuidadosas ainda caem. Daniel percebe que os controles técnicos sozinhos não conseguem barrar esse padrão.

### 6.2 Verificações

Daniel propõe uma regra simples: nenhuma mudança de dados bancários, de fornecedores ou de restituições de clientes, é feita apenas com base num e-mail. A pessoa que recebe o pedido liga para o fornecedor ou o cliente num número já cadastrado, não num informado no e-mail, e registra a ligação. Uma segunda pessoa aprova a mudança antes do pagamento seguinte. A Sra. Pike aceita a regra, mas pede uma forma de tratar os pedidos urgentes. Daniel sugere que a própria urgência seja tratada como um sinal de alerta e que a sócia-gerente seja a única pessoa que possa aprovar uma mudança no mesmo dia.

### 6.3 Proteções do e-mail

Daniel pede à empresa de suporte que marque os e-mails vindos de fora da firma com uma faixa visível e que verifique se o domínio da própria firma está configurado de modo a dificultar que criminosos enviem e-mails fingindo ser a Corbridge. Ele também pede que sinalizem as mensagens de domínios recém-registrados parecidos com nomes de clientes ou fornecedores. A Sra. Ashby observa que essas medidas reduzem o número de mensagens fraudulentas que chegam à equipe, mas nunca as eliminam, por isso a regra de verificação continua sendo a principal defesa. Daniel registra cada medida no registro, ligada ao risco de pagamento.

### 6.4 Preparação da equipe

Daniel conduz uma sessão curta para as equipes do financeiro e da folha de pagamento. Ele mostra dois exemplos sintéticos de pedidos de mudança fraudulentos e pede às equipes que encontrem os sinais de alerta. Depois, percorre passo a passo a regra da ligação de volta. As equipes perguntam o que fazer se um cliente se irritar por receber a ligação; Daniel sugere explicar que a ligação protege o dinheiro do cliente. Um mês depois, uma assistente da folha de pagamento liga para um fornecedor depois de um e-mail que pedia novos dados bancários. O fornecedor não sabe de nada, e a tentativa é barrada e comunicada.

### Exemplo resolvido

Daniel introduz uma regra de ligação de volta e de segunda aprovação para as mudanças de dados bancários, acrescenta proteções ao e-mail, treina a equipe do financeiro, e a regra barra uma tentativa sintética de fraude em um mês.

> **Caso sintético.** Os exemplos de fraude são sintéticos.

### Erros e limites

Ligar para um número informado no e-mail suspeito só leva ao criminoso.

### Exercícios

- **EX026 — Padrão da fraude.** Como o desvio de pagamentos costuma funcionar? *Rubrica:* 3 = mensagem diz que os dados bancários mudaram;; 2 = correto;; 1 = vago;; 0 = nenhuma.

- **EX027 — Número da ligação de volta.** Para qual número a equipe deve ligar? *Rubrica:* 3 = um já cadastrado;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX028 — Mudanças urgentes.** Quem pode aprovar uma mudança no mesmo dia? *Rubrica:* 3 = apenas a sócia-gerente;; 2 = correto;; 1 = outra pessoa;; 0 = nenhuma.

- **EX029 — Principal defesa.** O que continua sendo a principal defesa contra essa fraude? *Rubrica:* 3 = a regra de verificação;; 2 = correto;; 1 = outra coisa;; 0 = nenhuma.

- **EX030 — Tentativa barrada.** Quem barrou a tentativa de fraude? *Rubrica:* 3 = uma assistente da folha de pagamento;; 2 = correto;; 1 = outra pessoa;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). Daniel Reyes, a Sra. Helen Ashby, o Kingsmere Professional Institute, a Corbridge Accountancy Partners e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Seis meses, duas noites por semana.

**EX002.** Cerca de dois mil clientes.

**EX003.** Se a firma está fazendo as coisas certas e o que fazer em seguida.

**EX004.** Ela registra a concordância por escrito antes de ele verificar qualquer sistema.

**EX005.** Não; ele só precisa lê-los e executá-los.

**EX006.** Confidencialidade, integridade e disponibilidade.

**EX007.** Os dados bancários dos clientes usados nas restituições de impostos.

**EX008.** Nas semanas que antecedem os prazos de entrega das declarações de impostos.

**EX009.** A reputação de discrição da firma.

**EX010.** Um sistema com poucos dados pessoais ainda pode interromper o trabalho se falhar.

**EX011.** O phishing que leva à tomada da caixa postal, com nota 16.

**EX012.** Dois: a tomada da caixa postal e a fraude de faturas.

**EX013.** Os dois começam com um e-mail.

**EX014.** Sua nota é baixa, mas seu pior caso poderia atingir todos os clientes.

**EX015.** Como uma frase curta que nomeia a causa e o resultado.

**EX016.** 44 de 70 contas, 62,9 por cento.

**EX017.** Um de quatro administradores, 25 por cento.

**EX018.** Restringir de onde cada uma pode entrar e remover as sem uso.

**EX019.** Em termos do risco de fraude de faturas que já os preocupa.

**EX020.** A Sra. Pike, a sócia-gerente.

**EX021.** Criptografia de disco, atualizações automáticas e bloqueio de tela após cinco minutos.

**EX022.** 55 de 60 notebooks.

**EX023.** Mantê-los acrescenta risco sem benefício depois que a retenção termina.

**EX024.** Devolvê-los ou triturá-los com segurança em até duas semanas depois da digitalização.

**EX025.** As pastas na nuvem que a firma já tinha.

**EX026.** Uma mensagem convincente diz que os dados bancários mudaram, desviando o pagamento seguinte.

**EX027.** Um número já cadastrado, nunca um informado no e-mail.

**EX028.** Apenas a sócia-gerente.

**EX029.** A regra da ligação de volta e da segunda aprovação.

**EX030.** Uma assistente da folha de pagamento que ligou para o fornecedor.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (with Amd 1:2024). <https://www.iso.org/standard/27001>
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1
