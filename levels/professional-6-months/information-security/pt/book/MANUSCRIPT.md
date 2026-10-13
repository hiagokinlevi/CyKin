# Segurança da Informação: Curso Profissional

- Idioma: português do Brasil (`pt`); curso 025, curso profissional (6 meses). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–12 de 12 têm texto didático escrito à mão; os exercícios EX001–EX060 têm resoluções correspondentes com rubricas de 0 a 3; os dois laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

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

- **EX001 — Duração do curso.** Quanto dura o curso de Daniel? *Rubrica:* 3 = seis meses;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX002 — Registros de clientes.** Aproximadamente de quantos clientes a Corbridge guarda registros? *Rubrica:* 3 = cerca de dois mil;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX003 — Pergunta da liderança.** O que a Sra. Pike quer ver respondido? *Rubrica:* 3 = estamos fazendo as coisas certas, e o que vem a seguir;; 2 = as duas partes;; 1 = uma parte;; 0 = nenhuma.

- **EX004 — Nota de escopo.** Por que Daniel obtém uma nota de escopo assinada? *Rubrica:* 3 = concordância por escrito antes de verificar;; 2 = parcialmente correto;; 1 = vaga;; 0 = nenhuma.

- **EX005 — Programação necessária.** Daniel precisa escrever os scripts dos laboratórios? *Rubrica:* 3 = não, só lê-los e executá-los;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

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

- **EX007 — Exemplo de integridade.** Dê um exemplo de integridade na Corbridge. *Rubrica:* 3 = os dados bancários de restituição dos clientes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX008 — Pico de disponibilidade.** Quando a disponibilidade importa mais? *Rubrica:* 3 = nas semanas antes dos prazos de entrega;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX009 — Quarto item.** O que a Sra. Pike acrescentou à lista? *Rubrica:* 3 = a reputação de discrição da firma;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX010 — Lição da dependência.** Por que perguntar sobre a dependência além da sensibilidade? *Rubrica:* 3 = sistemas pouco sensíveis ainda podem parar a empresa;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

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

- **EX012 — Número de riscos altos.** Quantos riscos são altos? *Rubrica:* 3 = dois;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX013 — Causa comum.** Com o que começam os dois riscos altos? *Rubrica:* 3 = um e-mail;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX014 — Nota do fornecedor.** Por que acrescentar uma nota ao risco do fornecedor? *Rubrica:* 3 = nota baixa, mas pior caso grave;; 2 = parcialmente correto;; 1 = vaga;; 0 = nenhuma.

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

- **EX017 — Administradores.** Quantos administradores usam MFA? *Rubrica:* 3 = 1 de 4;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX018 — Contas de serviço.** O que Daniel faz em relação às contas de serviço? *Rubrica:* 3 = restringe os locais de entrada, remove as sem uso;; 2 = os dois;; 1 = um;; 0 = nenhuma.

- **EX019 — Argumento aos sócios.** Como a mudança deve ser explicada aos sócios? *Rubrica:* 3 = em termos do risco de fraude de faturas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX020 — Quem vai primeiro.** Quem concorda em ativar a MFA primeiro? *Rubrica:* 3 = a Sra. Pike;; 2 = parcialmente correto;; 1 = outra pessoa;; 0 = nenhuma.

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

- **EX022 — Conformidade.** Quantos notebooks cumpriam a linha de base depois de um mês? *Rubrica:* 3 = 55 de 60;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX023 — Arquivos antigos.** Por que remover os arquivos vencidos do servidor? *Rubrica:* 3 = risco sem benefício;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX024 — Regra do papel.** Que regra Daniel definiu para os originais em papel? *Rubrica:* 3 = devolvidos ou triturados em até duas semanas;; 2 = parcialmente correto;; 1 = vaga;; 0 = nenhuma.

- **EX025 — Pen drives.** O que substituiu os pen drives? *Rubrica:* 3 = as pastas na nuvem já existentes;; 2 = parcialmente correto;; 1 = outra coisa;; 0 = nenhuma.

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

- **EX026 — Padrão da fraude.** Como o desvio de pagamentos costuma funcionar? *Rubrica:* 3 = mensagem diz que os dados bancários mudaram;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX027 — Número da ligação de volta.** Para qual número a equipe deve ligar? *Rubrica:* 3 = um já cadastrado;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX028 — Mudanças urgentes.** Quem pode aprovar uma mudança no mesmo dia? *Rubrica:* 3 = apenas a sócia-gerente;; 2 = parcialmente correto;; 1 = outra pessoa;; 0 = nenhuma.

- **EX029 — Principal defesa.** O que continua sendo a principal defesa contra essa fraude? *Rubrica:* 3 = a regra de verificação;; 2 = parcialmente correto;; 1 = outra coisa;; 0 = nenhuma.

- **EX030 — Tentativa barrada.** Quem barrou a tentativa de fraude? *Rubrica:* 3 = uma assistente da folha de pagamento;; 2 = parcialmente correto;; 1 = outra pessoa;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Fornecedores e serviços em nuvem

### Objetivos de aprendizagem

Você vai (1) listar os fornecedores que lidam com as informações da firma; (2) fazer perguntas de segurança proporcionais; (3) registrar o que cada fornecedor consegue alcançar.

### 7.1 Lista de fornecedores

Daniel lista todas as organizações externas que armazenam ou conseguem alcançar informações da Corbridge: o serviço de e-mail e arquivos, o fornecedor do software de contabilidade, o provedor do portal dos clientes, o serviço de folha de pagamento, a empresa de suporte e uma empresa de trituração de documentos. Ele anota o que cada uma guarda e como se conecta. A empresa de suporte se destaca porque tem acesso de administrador a todos os notebooks e ao sistema de e-mail. A Sra. Ashby explica que um fornecedor com acesso amplo faz parte da segurança da firma, quer alguém pense nele assim ou não, por isso ele pertence ao registro de riscos.

### 7.2 Perguntas proporcionais

A Sra. Ashby desaconselha o envio de questionários longos que os pequenos fornecedores não conseguem responder. Em vez disso, Daniel faz a cada um poucas perguntas adequadas ao que eles guardam: o acesso da equipe exige um segundo fator, com que rapidez vocês nos avisarão de uma violação, onde nossos dados ficam armazenados e o que acontece com eles quando o contrato termina. A ISO/IEC 27002:2022, a orientação sobre os controles de segurança da informação, inclui as relações com fornecedores entre seus temas de controle, e Daniel a usa como lista de verificação para suas perguntas, e não como um livro de regras, escolhendo apenas os itens que importam para cada fornecedor.

### 7.3 A empresa de suporte

As respostas da empresa de suporte mostram que seus técnicos compartilham uma única conta de administrador para os sistemas da Corbridge. Daniel explica que isso torna impossível saber quem mudou o quê. Ele pede contas nominais, cada uma com um segundo fator, e uma lista mensal das mudanças feitas. A empresa concorda, depois de alguma discussão sobre o custo. Daniel também confirma que o contrato de suporte inclui o dever de comunicar incidentes em até um dia útil. A Sra. Ashby observa que cláusulas contratuais claras dão a uma firma pequena um poder de negociação que de outro modo ela não teria diante de um provedor maior.

### 7.4 O risco do fornecedor

Daniel volta ao risco de violação no fornecedor, que recebeu nota baixa no capítulo três. O fornecedor do software de contabilidade publica um resumo de segurança e tem uma certificação reconhecida, o que Daniel registra. Ele também verifica como a firma ficaria sabendo de uma violação e o que precisaria fazer: avisar os clientes afetados e possivelmente o regulador. Ele redige um breve plano para esse caso e o arquiva com os procedimentos de incidentes. A Sra. Ashby observa que planejar para um risco fora de seu controle continua sendo útil, porque a resposta está sob seu controle.

### Exemplo resolvido

Daniel lista seis fornecedores, faz quatro perguntas proporcionais a cada um, consegue que a empresa de suporte substitua uma conta de administrador compartilhada por contas nominais e planeja a resposta a uma violação no fornecedor.

> **Caso sintético.** Os fornecedores e as respostas são sintéticos.

### Erros e limites

Questionários genéricos e longos muitas vezes ficam sem resposta e deixam as lacunas reais desconhecidas.

### Exercícios

- **EX031 — Acesso mais amplo.** Qual fornecedor tem o acesso mais amplo? *Rubrica:* 3 = a empresa de suporte;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX032 — Quatro perguntas.** Cite duas das perguntas de Daniel aos fornecedores. *Rubrica:* 3 = MFA, aviso de violação, local dos dados, fim do contrato;; 2 = duas;; 1 = uma;; 0 = nenhuma.

- **EX033 — Conta compartilhada.** Que problema a empresa de suporte tinha? *Rubrica:* 3 = uma única conta de administrador compartilhada;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX034 — Dever de comunicação.** Em quanto tempo a empresa de suporte precisa comunicar incidentes? *Rubrica:* 3 = em até um dia útil;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX035 — Plano para o fornecedor.** Por que planejar para uma violação no fornecedor, fora do controle da firma? *Rubrica:* 3 = a resposta está sob seu controle;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Pessoas e conscientização

### Objetivos de aprendizagem

Você vai (1) criar atividades de conscientização curtas e relevantes; (2) tratar de forma confiável as admissões e os desligamentos; (3) construir uma cultura em que as comunicações sejam bem-vindas.

### 8.1 Conscientização relevante

A Corbridge usava um vídeo anual genérico que a equipe assistia sem som. Daniel o substitui por sessões curtas ligadas aos riscos da própria firma: phishing, fraude de pagamentos, tratamento dos documentos dos clientes e o que fazer com um notebook perdido. Cada sessão dura quinze minutos durante uma reunião de equipe e usa exemplos sintéticos parecidos com o trabalho real da firma. A Sra. Ashby explica que as pessoas se lembram muito melhor de exemplos do próprio trabalho do que de conselhos gerais e que sessões curtas e regulares superam uma única sessão longa por ano para manter os hábitos vivos.

### 8.2 Admissões e desligamentos

Daniel verifica como as contas são criadas e removidas. Os novos funcionários recebem as contas prontamente, mas as contas de quem sai às vezes são desativadas dias depois da saída, porque os recursos humanos avisam a empresa de suporte por e-mail quando alguém se lembra. Ele cria um formulário simples que os recursos humanos preenchem no último dia de quem sai, que vai direto para a empresa de suporte com cópia para Daniel. Depois, ele compara todo mês a lista de contas com a lista da folha de pagamento. A primeira comparação encontra dois ex-funcionários temporários com contas ativas, que são removidas no mesmo dia.

### 8.3 Uma cultura de comunicação

A Sra. Ashby insiste que os funcionários que temem ser culpados escondem os erros, e os erros escondidos se tornam incidentes. Daniel trabalha com a Sra. Pike para enviar uma breve mensagem dela: comunicar um e-mail suspeito ou um erro é sempre a coisa certa, e ninguém será criticado por comunicar. Ele cria um único endereço de e-mail e um único número de telefone para as comunicações. No mês seguinte, a equipe comunica nove mensagens suspeitas e um e-mail enviado ao cliente errado. Daniel agradece pessoalmente a cada pessoa que comunicou, porque o agradecimento incentiva a próxima comunicação tanto quanto qualquer treinamento.

### 8.4 Medição do comportamento

Daniel quer saber se as sessões mudam alguma coisa. Ele acompanha três números simples todo mês: e-mails suspeitos comunicados, erros comunicados pelos próprios autores e dias levados para desativar as contas de quem sai. A Sra. Ashby desaconselha julgar o sucesso pelo número de pessoas que clicam num e-mail de phishing de teste, porque os resultados variam com a dificuldade do teste e podem deixar a equipe ressentida. Daniel concorda e decide que o aumento das comunicações e a queda dos atrasos nos desligamentos são sinais melhores de que os hábitos estão mudando, e planeja mostrá-los à liderança trimestralmente junto com outras medidas.

### Exemplo resolvido

Daniel substitui um vídeo genérico por sessões curtas específicas da firma, corrige os atrasos nos desligamentos com um formulário e uma verificação mensal e obtém nove comunicações em um mês depois de uma mensagem sem culpa.

> **Caso sintético.** Os funcionários e os números são sintéticos.

### Erros e limites

Julgar a conscientização apenas pelas taxas de clique nos testes pode enganar e desestimular a equipe.

### Exercícios

- **EX036 — Duração da sessão.** Quanto dura cada sessão de conscientização? *Rubrica:* 3 = quinze minutos;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX037 — Lacuna nos desligamentos.** Por que as contas de quem saía eram desativadas com atraso? *Rubrica:* 3 = o RH mandava e-mail à empresa de suporte quando se lembrava;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX038 — Verificação mensal.** O que Daniel compara todo mês? *Rubrica:* 3 = a lista de contas com a da folha de pagamento;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX039 — Comunicações obtidas.** Quantas mensagens suspeitas foram comunicadas no mês seguinte? *Rubrica:* 3 = nove;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX040 — Medida melhor.** Por que evitar julgar pelas taxas de clique nos testes? *Rubrica:* 3 = variam com a dificuldade, causam ressentimento;; 2 = os dois;; 1 = um;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Tratamento de incidentes

### Objetivos de aprendizagem

Você vai (1) escrever um procedimento de incidentes curto; (2) segui-lo durante um incidente sintético; (3) decidir quando notificar clientes ou reguladores.

### 9.1 Um procedimento curto

Daniel escreve um procedimento de duas páginas que cobre as primeiras horas de um incidente: para quem ligar, como conter o problema, o que registrar e quem decide sobre as notificações. Ele indica Daniel como coordenador, a empresa de suporte como responsável pela resposta técnica e a Sra. Pike como quem decide sobre tudo o que envolver clientes ou reguladores. A Sra. Ashby lembra que um procedimento que ninguém encontra é inútil, por isso ele imprime cópias para cada escritório e guarda uma num lugar acessível mesmo se o e-mail estiver fora do ar, junto com todos os telefones importantes.

### 9.2 A tomada de uma caixa postal

Três semanas depois, a assistente de um sócio comunica que clientes receberam da conta dela uma mensagem estranha pedindo que abrissem um documento. Daniel segue o procedimento. A empresa de suporte redefine a senha, encerra todas as sessões ativas, ativa um segundo fator e remove uma regra de encaminhamento que o atacante tinha acrescentado, que enviava cópias de todos os e-mails recebidos a um endereço externo. Daniel registra cada passo com os horários. Depois, ele pede à empresa de suporte que verifique se o atacante leu ou baixou algum documento de cliente durante o período em que controlou a conta.

### 9.3 Decisão sobre a notificação

A revisão mostra que a regra de encaminhamento do atacante copiou cerca de duas semanas de e-mails recebidos, incluindo algumas mensagens com documentos de identidade de clientes anexados. A Sra. Pike, com a orientação do consultor de proteção de dados da firma, decide que os clientes afetados precisam ser avisados e que o regulador precisa ser notificado dentro do prazo legal. Daniel prepara uma lista factual dos clientes afetados e do tipo de documentos envolvidos. A Sra. Ashby observa que a regra de encaminhamento transformou um incômodo numa violação que precisa ser notificada, e é por isso que procurar essas regras é um passo padrão.

### 9.4 Aprendizado posterior

Uma semana depois, Daniel faz uma breve revisão com as pessoas envolvidas. A causa foi uma senha roubada numa conta sem segundo fator; a assistente estava na lista da etapa seguinte da implantação. A firma antecipa a implantação para todos os funcionários restantes e acrescenta uma verificação mensal das regras de encaminhamento para endereços externos. Daniel escreve um resumo de uma página para os sócios, sem culpar a assistente, que comunicou prontamente. A Sra. Ashby elogia a revisão por se concentrar em corrigir as condições que permitiram o incidente, e não na pessoa.

### Exemplo resolvido

O procedimento de Daniel orienta a resposta a uma tomada sintética de caixa postal: sessões encerradas, uma regra de encaminhamento removida, clientes e regulador notificados e a implantação do segundo fator antecipada.

> **Caso sintético.** O incidente e os clientes são sintéticos.

### Erros e limites

Redefinir uma senha sem remover as regras de encaminhamento deixa o atacante recebendo os e-mails.

### Exercícios

- **EX041 — Coordenador.** Quem coordena os incidentes na Corbridge? *Rubrica:* 3 = Daniel;; 2 = parcialmente correto;; 1 = outra pessoa;; 0 = nenhuma.

- **EX042 — Regra escondida.** O que o atacante tinha acrescentado à caixa postal? *Rubrica:* 3 = uma regra de encaminhamento para um endereço externo;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX043 — Motivo da notificação.** Por que o incidente passou a exigir notificação? *Rubrica:* 3 = os e-mails encaminhados continham documentos de identidade de clientes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX044 — Causa raiz.** Qual foi a causa raiz? *Rubrica:* 3 = senha roubada sem segundo fator;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.

- **EX045 — Nova verificação.** Que verificação mensal foi acrescentada? *Rubrica:* 3 = regras de encaminhamento para endereços externos;; 2 = parcialmente correto;; 1 = vaga;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Continuidade e backups

### Objetivos de aprendizagem

Você vai (1) identificar o que precisa continuar funcionando; (2) verificar que os backups podem ser restaurados; (3) ensaiar um breve exercício de continuidade.

### 10.1 O que precisa continuar funcionando

Usando a lista de dependências do capítulo dois, Daniel identifica três serviços que precisam voltar depressa: o e-mail, o software de contabilidade e o portal dos clientes. Ele pergunta a cada provedor como faz backup dos dados e com que rapidez conseguiria restaurá-los. Ele descobre que o serviço de e-mail em nuvem guarda os itens apagados apenas por um período limitado, de modo que uma exclusão maliciosa percebida tarde poderia ser irrecuperável. A firma contrata um serviço de backup separado para o e-mail e os arquivos. A Sra. Ashby explica que um provedor de nuvem manter o serviço funcionando não é o mesmo que fazer backup dos seus dados.

### 10.2 Teste das restaurações

Daniel pede à empresa de suporte que restaure uma amostra de arquivos e uma caixa postal do novo serviço de backup numa área de teste. Os arquivos são restaurados corretamente, mas a restauração da caixa postal leva seis horas, mais do que o esperado. Daniel registra o tempo e pergunta se ele pode ser melhorado para os casos urgentes. Ele também verifica o backup do antigo servidor de arquivos e descobre que ele vinha copiando para um disco na mesma sala, que se perderia num incêndio ou numa inundação. A empresa de suporte acrescenta uma cópia externa. A Sra. Ashby lembra que um backup não testado é só uma esperança.

### 10.3 Um exercício de mesa

Daniel conduz um exercício de uma hora com a Sra. Pike, dois sócios e a empresa de suporte. O cenário: no início de janeiro, o fornecedor do software de contabilidade fica indisponível por três dias. O grupo discute que trabalho pode continuar, como os clientes seriam avisados e se os prazos de entrega poderiam ser cumpridos. Eles descobrem que ninguém sabe como pedir mais prazo à autoridade tributária num caso assim. Um sócio concorda em descobrir e documentar os passos. Daniel registra as decisões e as lacunas e agenda o exercício seguinte para seis meses depois.

### 10.4 Por escrito

Daniel transforma as decisões num plano de continuidade de três páginas: os três serviços principais, quem contatar para cada um, formas temporárias de trabalhar e os passos para pedir prorrogação de prazos. Ele guarda cópias impressas nos dois escritórios e uma com a Sra. Pike em casa. A Sra. Ashby observa que o principal valor do plano veio da conversa que o produziu, porque os sócios agora entendem os pontos fracos da firma. Ela sugere revisá-lo antes de cada temporada de muito trabalho, quando a equipe muda e os fornecedores podem ter mudado seus arranjos.

### Exemplo resolvido

Daniel acrescenta um serviço de backup separado, descobre uma restauração de caixa postal de seis horas e um disco de backup na mesma sala, conduz um exercício de mesa sobre a indisponibilidade de um fornecedor e escreve um plano de continuidade de três páginas.

> **Caso sintético.** Os serviços, os tempos e as decisões são sintéticos.

### Erros e limites

Presumir que um provedor de nuvem faz backup dos seus dados pode deixar os itens apagados irrecuperáveis.

### Exercícios

- **EX046 — Serviços principais.** Quais três serviços precisam voltar depressa? *Rubrica:* 3 = e-mail, software de contabilidade, portal dos clientes;; 2 = os três;; 1 = dois;; 0 = nenhuma.

- **EX047 — Tempo de restauração.** Quanto tempo levou a restauração da caixa postal? *Rubrica:* 3 = seis horas;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX048 — Disco na mesma sala.** O que havia de errado com o backup do servidor de arquivos? *Rubrica:* 3 = copiava para um disco na mesma sala;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX049 — Lacuna do exercício.** Que lacuna o exercício de mesa encontrou? *Rubrica:* 3 = ninguém sabia pedir prorrogação de prazo;; 2 = parcialmente correto;; 1 = vaga;; 0 = nenhuma.

- **EX050 — Revisão do plano.** Quando o plano deve ser revisado? *Rubrica:* 3 = antes de cada temporada de muito trabalho;; 2 = parcialmente correto;; 1 = outra resposta;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Política e obrigações

### Objetivos de aprendizagem

Você vai (1) escrever uma política de segurança curta e utilizável; (2) mapear as obrigações legais e profissionais da firma; (3) decidir se a certificação formal vale a pena.

### 11.1 Uma política utilizável

A política de segurança atual da Corbridge é um documento de vinte páginas copiado de um modelo, que ninguém leu. Daniel a substitui por uma política de duas páginas que cobre as regras de que a equipe realmente precisa: contas e segundos fatores, dispositivos, tratamento dos documentos dos clientes, e-mail e pagamentos, comunicações e uso de fornecedores. Cada regra tem um motivo de uma frase. Os procedimentos detalhados, como a regra da ligação de volta e o procedimento de incidentes, ficam em documentos separados, vinculados à política. A Sra. Pike assina a política, e cada funcionário confirma tê-la lido durante uma reunião de equipe.

### 11.2 Obrigações

Daniel mapeia o que a firma precisa fazer por lei e pelas regras profissionais. A lei de proteção de dados exige segurança adequada para os dados pessoais e a notificação de certas violações dentro de prazos definidos. O órgão profissional espera que seus membros protejam a confidencialidade dos clientes. Alguns clientes maiores exigem compromissos de segurança em seus contratos. Daniel lista cada obrigação com sua fonte e os controles que a cumprem. A Sra. Ashby o aconselha a confirmar os pontos jurídicos com o consultor de proteção de dados da firma, em vez de depender da própria leitura, porque as obrigações diferem entre países e mudam com o tempo.

### 11.3 Certificação

Um cliente grande pergunta se a Corbridge é certificada na ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022), a norma internacional para um sistema de gestão da segurança da informação. Daniel explica aos sócios que a certificação exige um sistema de gestão documentado, auditorias internas e uma auditoria externa por ano, o que tomaria um tempo considerável de uma firma de sessenta pessoas. Ele sugere um caminho intermediário: alinhar o trabalho da firma com as ideias principais da norma, como a avaliação de riscos, o compromisso da liderança e a revisão regular, e reconsiderar a certificação se mais clientes pedirem. Os sócios concordam, e Daniel escreve uma breve resposta para o cliente.

### 11.4 Manter atualizada

Daniel define um calendário simples para revisar a política e os documentos relacionados: a política uma vez por ano, o registro de riscos a cada três meses, as respostas dos fornecedores anualmente e o plano de continuidade antes de cada temporada de muito trabalho. Cada revisão tem um responsável nomeado. A Sra. Ashby explica que uma política deixada intocada por anos se afasta do modo como as pessoas realmente trabalham, e a equipe deixa de confiar nela. Ela elogia a política curta por ser legível e sugere que Daniel pergunte todo ano a dois funcionários se as regras fazem sentido para eles na prática.

### Exemplo resolvido

Daniel substitui um modelo de vinte páginas por uma política assinada de duas páginas, mapeia as obrigações legais e profissionais e recomenda alinhar-se à ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) em vez de buscar a certificação por enquanto.

> **Caso sintético.** A política, o pedido do cliente e as obrigações são sintéticos e gerais; os deveres jurídicos reais exigem orientação profissional.

### Erros e limites

Uma política longa de modelo que ninguém lê dá uma falsa sensação de conformidade.

### Exercícios

- **EX051 — Tamanho da política.** Qual é o tamanho da nova política de Daniel? *Rubrica:* 3 = duas páginas;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX052 — Procedimentos.** Onde ficam os procedimentos detalhados? *Rubrica:* 3 = em documentos separados e vinculados;; 2 = parcialmente correto;; 1 = outro lugar;; 0 = nenhuma.

- **EX053 — Custo da certificação.** O que a certificação exige? *Rubrica:* 3 = sistema de gestão, auditorias internas e externa anual;; 2 = tudo;; 1 = parte;; 0 = nenhuma.

- **EX054 — Caminho intermediário.** O que Daniel recomendou em vez de certificar agora? *Rubrica:* 3 = alinhar-se às ideias principais da norma;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX055 — Orientação jurídica.** Quem deve confirmar os pontos jurídicos? *Rubrica:* 3 = o consultor de proteção de dados;; 2 = parcialmente correto;; 1 = outra pessoa;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Relatórios à liderança e próximos passos

### Objetivos de aprendizagem

Você vai (1) relatar a situação da segurança em linguagem simples; (2) revisar seis meses de progresso; (3) planejar o próximo ano e a continuação dos estudos.

### 12.1 Um relatório de uma página

Daniel prepara a cada trimestre um relatório de uma página para os sócios. Ele mostra os principais riscos e se cada um está subindo ou caindo, cinco medidas com sua tendência, os incidentes recentes em uma linha cada e até três decisões necessárias. As medidas são a cobertura do segundo fator, os notebooks que cumprem a linha de base, os dias para desativar as contas de quem sai, os e-mails suspeitos comunicados e o último teste de restauração bem-sucedido. A Sra. Ashby o aconselha a colocar as decisões primeiro, porque os sócios têm pouco tempo, e a evitar termos técnicos que precisariam ser explicados antes de eles poderem responder.

### 12.2 Seis meses de progresso

Daniel compara o início do curso com hoje. A cobertura do segundo fator subiu de 62,9 por cento para todas as contas de pessoas, com as contas de serviço restringidas em vez disso. Os notebooks que cumprem a linha de base passaram de um número desconhecido para 55 de 60 e depois para todos os 60. As contas de quem sai agora são desativadas no último dia. Uma tentativa de fraude foi barrada, e um incidente foi tratado e notificado dentro do prazo legal. A Sra. Pike diz aos sócios que agora tem uma resposta clara para sua pergunta original e que os próximos passos são conhecidos.

### 12.3 O próximo ano

Daniel redige um plano para os próximos doze meses: concluir a limpeza do servidor de arquivos e levar os registros restantes para a nuvem, repetir o exercício de mesa com um cenário de ransomware, revisar as respostas dos fornecedores e conduzir sessões de conscientização sobre novos padrões de fraude. Ele estima o tempo e o custo de cada item e pede aos sócios que escolham. A Sra. Ashby sugere que ele também reserve tempo para o próprio aprendizado, já que as ameaças e os serviços mudam mais depressa do que qualquer curso consegue cobrir, e que participe de um grupo local de profissionais de segurança para ter apoio e ideias novas.

### 12.4 Continuação dos estudos

A Sra. Ashby revisa as opções com Daniel. Ele poderia fazer uma certificação introdutória reconhecida para formalizar seus conhecimentos, frequentar cursos curtos sobre tratamento de incidentes ou segurança em nuvem, ou passar mais tarde para uma qualificação mais longa. Ela também recomenda o curso de governança de dados que vem depois deste, já que boa parte do trabalho de Daniel, como a retenção e o tratamento dos dados pelos fornecedores, se sobrepõe ao modo como as organizações administram a informação como um ativo. Daniel decide começar o curso de governança de dados no período seguinte e buscar uma certificação em até um ano.

### Exemplo resolvido

Daniel escreve um relatório trimestral de uma página com as decisões primeiro, mostra seis meses de progresso, de 62,9 por cento de cobertura do segundo fator à cobertura total das pessoas, e planeja o próximo ano e a continuação dos estudos.

> **Caso sintético.** Os números de progresso são sintéticos.

### Erros e limites

Os relatórios cheios de detalhes técnicos sem decisões claras muitas vezes são ignorados pela liderança.

### Exercícios

- **EX056 — Ordem do relatório.** O que deve vir primeiro no relatório aos sócios? *Rubrica:* 3 = as decisões necessárias;; 2 = parcialmente correto;; 1 = outra coisa;; 0 = nenhuma.

- **EX057 — Cinco medidas.** Cite três das cinco medidas. *Rubrica:* 3 = MFA, linha de base, dias de desligamento, comunicações, teste de restauração;; 2 = três;; 1 = duas;; 0 = nenhuma.

- **EX058 — Mudança da cobertura.** Como mudou a cobertura do segundo fator? *Rubrica:* 3 = de 62,9 por cento para todas as contas de pessoas;; 2 = parcialmente correto;; 1 = parcial;; 0 = nenhuma.

- **EX059 — Próximo cenário.** Que cenário o próximo exercício de mesa vai usar? *Rubrica:* 3 = ransomware;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX060 — Próximo curso.** Que curso Daniel faz em seguida? *Rubrica:* 3 = governança de dados;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. Daniel Reyes, a Sra. Helen Ashby, o Kingsmere Professional Institute, a Corbridge Accountancy Partners e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX031.** A empresa de suporte, com acesso de administrador aos notebooks e ao e-mail.

**EX032.** Se a equipe usa um segundo fator e com que rapidez avisa de uma violação.

**EX033.** Os técnicos compartilhavam uma única conta de administrador.

**EX034.** Em até um dia útil.

**EX035.** Porque a firma continua controlando a própria resposta.

**EX036.** Quinze minutos, durante uma reunião de equipe.

**EX037.** Os recursos humanos mandavam e-mail à empresa de suporte só quando alguém se lembrava.

**EX038.** A lista de contas com a lista da folha de pagamento.

**EX039.** Nove mensagens suspeitas, além de um e-mail enviado ao destinatário errado.

**EX040.** Os resultados variam com a dificuldade do teste e podem deixar a equipe ressentida.

**EX041.** Daniel coordena; a Sra. Pike decide sobre as notificações.

**EX042.** Uma regra que encaminhava os e-mails recebidos a um endereço externo.

**EX043.** Os e-mails encaminhados incluíam documentos de identidade de clientes.

**EX044.** Uma senha roubada numa conta sem segundo fator.

**EX045.** Uma verificação mensal das regras que encaminham e-mails para fora da firma.

**EX046.** O e-mail, o software de contabilidade e o portal dos clientes.

**EX047.** Seis horas, mais do que o esperado.

**EX048.** Copiava para um disco na mesma sala do servidor.

**EX049.** Ninguém sabia como pedir mais prazo à autoridade tributária.

**EX050.** Antes de cada temporada de muito trabalho.

**EX051.** Duas páginas, com os motivos de cada regra.

**EX052.** Em documentos separados, vinculados à política.

**EX053.** Um sistema de gestão documentado, auditorias internas e uma auditoria externa anual.

**EX054.** Alinhar-se às ideias principais da norma e reconsiderar se mais clientes pedirem.

**EX055.** O consultor de proteção de dados da firma.

**EX056.** As decisões necessárias.

**EX057.** A cobertura do segundo fator, os notebooks que cumprem a linha de base e os dias para desativar as contas de quem sai.

**EX058.** De 62,9 por cento para todas as contas usadas por pessoas.

**EX059.** Um cenário de ransomware.

**EX060.** O curso de governança de dados, a partir do período seguinte.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (with Amd 1:2024). <https://www.iso.org/standard/27001>
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1
