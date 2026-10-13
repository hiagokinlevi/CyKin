# Segurança da Informação: Curso de Pós-Graduação

- Idioma: português do Brasil (`pt`); curso 140, curso de pós-graduação (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 12 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 1 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 7–12 (EX031–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: profissionais de TI experientes que constroem um programa de segurança da informação baseado em riscos para uma organização de saúde com várias unidades.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios medem a conformidade com as correções críticas por clínica sobre dados sintéticos de dispositivos e sinalizam domínios de remetente parecidos por distância de edição num log sintético de e-mail. As normas são citadas pela edição e parafraseadas. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham uma profissional desde a governança, a avaliação de riscos e o inventário, passando pelas correções, pelo acesso, pelo phishing, pela recuperação, pelos incidentes e pelos relatórios ao conselho, até um projeto final de prontidão contra ransomware e sua apresentação. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Elena Petrova** | Profissional na pós-graduação, gerente de TI e de segurança | Inventada |
| **Dr. Hamid Qureshi** | Tutor | Inventado |
| **Thornbury Business School** | Escola de negócios fictícia | Inventada |
| **Moorfield Dental Group** | Grupo odontológico fictício, com 22 clínicas e cerca de 600 funcionários | Inventado |

### Fontes principais

ISO/IEC 27000:2026; ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022); ISO/IEC 27002:2022; NIST SP 800-53 Rev. 5; NIST SP 800-30 Rev. 1; NIST CSWP 29 (CSF 2.0); Saltzer e Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939). Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — A profissional e o Moorfield Dental Group

### Objetivos de aprendizagem

Você vai (1) descrever o caso da profissional; (2) identificar o que um curso de pós-graduação acrescenta à experiência; (3) definir metas de aprendizagem ligadas a problemas do ambiente de trabalho.

### 1.1 A profissional

Elena Petrova trabalha com TI há doze anos e hoje gerencia a TI e a segurança do fictício Moorfield Dental Group. Ela se matricula num programa de pós-graduação de dois anos, em tempo parcial, em segurança da informação na fictícia Thornbury Business School, ministrado pelo Dr. Hamid Qureshi. Ela traz habilidade prática, mas pouca formação estruturada em governança, risco ou medição. O Dr. Qureshi explica que o curso pretende ajudar os profissionais experientes a transformar sua experiência em decisões estruturadas e defensáveis, que os conselhos e os auditores possam acompanhar e questionar.

### 1.2 A organização

O Moorfield mantém vinte e duas clínicas odontológicas, com cerca de seiscentos funcionários e aproximadamente quinhentos e setenta computadores, tablets e aparelhos de imagem. As clínicas guardam prontuários de pacientes, imagens de raio X, agendas de consultas e dados de pagamento. A maioria das clínicas não tem equipe de TI; três dependem de um contato local em tempo parcial. Uma equipe central de quatro pessoas, liderada por Elena, dá suporte a todos. Os pacientes esperam confidencialidade, e as clínicas não conseguem atender os pacientes se os sistemas estiverem indisponíveis, então a confidencialidade e a disponibilidade importam muito. A equipe de Elena também gerencia os servidores centrais e a rede da sede.

### 1.3 O que o curso acrescenta

A experiência de Elena lhe diz o que costuma quebrar e como consertar. O curso acrescenta frameworks para decidir o que importa mais, métodos para medir se os controles funcionam e habilidades para explicar a segurança a um conselho de dentistas e investidores. O Dr. Qureshi pede que cada estudante traga um problema do ambiente de trabalho para cada disciplina. Elena escolhe os atrasos nas correções nas clínicas pequenas, as tentativas recorrentes de phishing e os planos de recuperação pouco claros, que ela suspeita estarem ligados pelas mesmas lacunas de pessoal. Ela escreve cada problema no topo do seu caderno do curso.

### 1.4 Metas de aprendizagem

Elena escreve três metas de aprendizagem: construir um programa de segurança baseado em riscos que o conselho do Moorfield possa aprovar, medir os principais controles com definições claras e conduzir um projeto final de melhoria crível. O Dr. Qureshi pede que ela diga como vai saber que cada meta foi atingida. Ela acrescenta evidências para cada uma: um documento do programa aprovado pelo conselho, um conjunto mensal de medidas com definições e um relatório do projeto final revisado pelo conselho. Ela aprende que as metas com evidências são mais fáceis de perseguir e de avaliar. O Dr. Qureshi aprova as metas e suas evidências.

### Exemplo resolvido

Elena se matricula, descreve as vinte e duas clínicas e a equipe de quatro pessoas do Moorfield, liga o conteúdo do curso a três problemas do ambiente de trabalho e define metas de aprendizagem com evidências.

> **Caso sintético.** Elena, o Moorfield e a Thornbury são sintéticos.

### Erros e limites

A experiência sem métodos estruturados torna as decisões difíceis de defender.

### Exercícios

- **EX001 — Número de clínicas.** Quantas clínicas o Moorfield mantém? *Rubrica:* 3 = vinte e duas;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX002 — Equipe central.** Qual é o tamanho da equipe central de TI? *Rubrica:* 3 = quatro pessoas;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX003 — Problemas do ambiente de trabalho.** Cite um problema do ambiente de trabalho que Elena traz. *Rubrica:* 3 = atrasos nas correções nas clínicas pequenas;; 2 = um;; 1 = nada;; 0 = nenhuma.

- **EX004 — Acréscimo do curso.** O que o curso acrescenta à experiência de Elena? *Rubrica:* 3 = frameworks, medição e comunicação com o conselho;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX005 — Evidência da meta.** Que evidência mostra que a meta do programa foi atingida? *Rubrica:* 3 = um documento do programa aprovado pelo conselho;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Governança de segurança e o sistema de gestão

### Objetivos de aprendizagem

Você vai (1) projetar uma estrutura de governança para a segurança; (2) aplicar os conceitos de sistema de gestão da ISO/IEC 27001; (3) definir o apetite a risco com um conselho.

### 2.1 Estrutura de governança

O conselho do Moorfield é formado por três dentistas sócios e dois representantes dos investidores. As decisões de segurança vinham sendo tomadas informalmente por Elena e pelo diretor de operações. Elena propõe uma estrutura: o conselho aprova a política e o apetite a risco todos os anos, um comitê de segurança formado por Elena, pelo diretor de operações e por um líder clínico se reúne mensalmente e os gerentes das clínicas respondem pelos controles locais. O Dr. Qureshi observa que papéis claros tornam evidente quem decide, quem age e quem precisa ser informado. O conselho aprova a estrutura na sua reunião trimestral seguinte.

### 2.2 Conceitos de sistema de gestão

Elena estuda a ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022), que estabelece os requisitos de um sistema de gestão da segurança da informação. Ela pede que a organização entenda seu contexto e suas partes interessadas, obtenha o comprometimento da liderança, avalie e trate os riscos, forneça recursos, opere os controles, avalie o desempenho e melhore. A ISO/IEC 27000:2026 dá a visão geral da família e de seus termos. Elena percebe que o Moorfield já realiza muitas dessas atividades, mas sem registros, então não consegue mostrar que elas acontecem de forma coerente. Ela lista as atividades existentes do Moorfield em relação a cada cláusula e marca quais têm registros, quais têm registros parciais e quais não têm nenhum.

### 2.3 Apetite a risco

Elena redige uma declaração de apetite a risco para o conselho. O Moorfield aceitará um risco muito baixo para a confidencialidade dos prontuários dos pacientes, um risco baixo de indisponibilidade dos sistemas clínicos durante o horário de funcionamento e um risco moderado para os sistemas administrativos, como o de marketing. O conselho debate a redação e acrescenta que nenhuma clínica deve ficar impossibilitada de atender pacientes por mais de meio dia. O Dr. Qureshi observa que as declarações de apetite transformam valores em regras para priorizar o trabalho. A declaração final cabe numa página e é assinada pelo presidente do conselho.

### 2.4 Escopo

Elena define o escopo do sistema de gestão do Moorfield: todas as clínicas, a sede, o sistema de prontuários, os sistemas de imagem e o processamento de pagamentos. O laboratório de prótese, administrado por uma empresa separada, fica excluído, mas é tratado como fornecedor. Ela escreve o escopo num parágrafo, com um diagrama. O Dr. Qureshi adverte que um escopo pouco claro causa confusão depois, sobretudo quando um auditor ou uma seguradora pergunta o que o programa realmente abrange. O conselho aprova o escopo, e Elena o acrescenta à abertura do documento do programa de segurança, para que todos os que lerem o programa saibam o que ele abrange.

### Exemplo resolvido

Elena projeta uma estrutura com conselho, comitê e gerentes de clínica, mapeia o Moorfield para os conceitos da ISO/IEC 27001, redige um apetite a risco com um limite clínico de meio dia e define o escopo.

> **Caso sintético.** Os arranjos do conselho são sintéticos; as normas são parafraseadas.

### Erros e limites

As atividades sem registros não conseguem mostrar que acontecem de forma coerente.

### Exercícios

- **EX006 — Membros do comitê.** Quem faz parte do comitê de segurança? *Rubrica:* 3 = Elena, o diretor de operações, um líder clínico;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX007 — Registros faltantes.** O que falta ao Moorfield, apesar de realizar as atividades? *Rubrica:* 3 = registros;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX008 — Acréscimo do conselho.** Que limite o conselho acrescenta? *Rubrica:* 3 = nenhuma clínica sem atender pacientes por mais de meio dia;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX009 — Parte excluída.** O que fica excluído do escopo? *Rubrica:* 3 = o laboratório de prótese;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX010 — Norma de visão geral.** Que norma dá a visão geral da família? *Rubrica:* 3 = ISO/IEC 27000:2026;; 2 = correto;; 1 = outra;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Avaliação de riscos para uma rede de clínicas

### Objetivos de aprendizagem

Você vai (1) conduzir uma avaliação de riscos estruturada; (2) classificar a probabilidade e o impacto de forma coerente; (3) escolher tratamentos alinhados ao apetite.

### 3.1 Método

Elena segue a abordagem da NIST SP 800-30 Revisão 1: identificar as fontes e os eventos de ameaça, as vulnerabilidades e as condições predisponentes e então julgar a probabilidade e o impacto. Ela conduz oficinas com os gerentes das clínicas, o líder clínico e a área financeira. As oficinas identificam como principais ameaças o ransomware, o phishing que leva ao comprometimento de contas, os tablets perdidos ou roubados, a falha de fornecedores e o uso indevido dos prontuários pela equipe. O Dr. Qureshi aconselha envolver as pessoas que executam o trabalho, porque elas sabem onde os processos realmente quebram. Cada oficina dura duas horas e produz uma lista de ameaças com exemplos.

### 3.2 Classificações coerentes

As classificações variam de pessoa para pessoa. Elena define escalas de cinco pontos com exemplos: impacto cinco significa que uma clínica não consegue atender pacientes por mais de um dia ou que muitos prontuários são expostos; probabilidade cinco significa que se espera que aconteça dentro de um ano. Ela pede que dois colegas classifiquem dez riscos de forma independente e compara os resultados. Onde eles diferem em mais de um ponto, discutem e chegam a um acordo. O Dr. Qureshi observa que os exercícios de calibração tornam as classificações mais coerentes e defensáveis. Três dos dez riscos precisaram de discussão, e as classificações acordadas são registradas com seus motivos.

### 3.3 Resultados

O ransomware e o comprometimento por phishing ficam no topo, seguidos pelos atrasos nas correções nas clínicas sem equipe de TI e pelos testes de recuperação fracos. O uso indevido dos prontuários pela equipe recebe probabilidade moderada e impacto alto. Elena registra cada risco com um dono, os controles atuais e o tratamento planejado. Ela observa que os atrasos nas correções e a recuperação fraca tornam o ransomware mais danoso, então tratá-los reduz vários riscos de uma vez. Ela apresenta o registro ao comitê de segurança como um mapa de calor de uma página, com os cinco principais riscos listados abaixo, cada um com seu dono e a próxima ação planejada.

### 3.4 Tratamento

Elena escolhe tratamentos alinhados ao apetite. Para o ransomware, ela planeja correções mais rápidas, backups imutáveis e recuperação testada. Para o phishing, ela planeja a autenticação multifator e melhorias na filtragem de e-mail. Para o uso indevido, ela planeja revisões de acessos e alertas sobre visualizações incomuns de prontuários. O seguro cibernético transfere parte da perda financeira. O conselho aprova o plano, aceitando um risco residual moderado para os sistemas administrativos. O Dr. Qureshi observa que registrar os riscos aceitos protege todos mais tarde. Elena registra na ata a decisão do conselho e os riscos residuais aceitos, com uma data de revisão marcada para o ano seguinte.

### Exemplo resolvido

Elena conduz oficinas segundo a SP 800-30 Revisão 1, calibra escalas de cinco pontos, coloca o ransomware e o phishing no topo e escolhe tratamentos aprovados pelo conselho.

> **Caso sintético.** As avaliações são sintéticas.

### Erros e limites

As classificações não calibradas variam muito entre os avaliadores.

### Exercícios

- **EX011 — Exemplo de ameaça.** Cite uma das principais ameaças identificadas. *Rubrica:* 3 = ransomware;; 2 = uma;; 1 = nada;; 0 = nenhuma.

- **EX012 — Regra de calibração.** Quando os avaliadores discutem as diferenças? *Rubrica:* 3 = quando diferem em mais de um ponto;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX013 — Riscos ligados.** Que dois riscos agravam o dano do ransomware? *Rubrica:* 3 = atrasos nas correções e recuperação fraca;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX014 — Tratamento do uso indevido.** Como o uso indevido pela equipe é tratado? *Rubrica:* 3 = revisões de acessos e alertas sobre visualizações incomuns;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX015 — Método de transferência.** O que transfere parte da perda financeira? *Rubrica:* 3 = o seguro cibernético;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Inventário de ativos e de fornecedores

### Objetivos de aprendizagem

Você vai (1) montar um inventário de ativos confiável entre as unidades; (2) identificar os fornecedores com acesso a dados; (3) atribuir donos e classificações.

### 4.1 Ativos entre as unidades

O inventário de Elena fica numa planilha atualizada quando os dispositivos são comprados. Ela a compara com o sistema de gestão de dispositivos e com os registros da rede. Várias clínicas têm computadores de imagem comprados diretamente pelos dentistas e nunca registrados. Eles rodam sistemas operacionais antigos, porque os fornecedores do software de imagem não certificaram versões mais novas. O Dr. Qureshi observa que os dispositivos não registrados muitas vezes carregam o maior risco, porque ficam, por padrão, fora das correções, do monitoramento e do backup. Ela encontra onze computadores de imagem não registrados e os acrescenta ao inventário com a clínica, o fornecedor e a versão do sistema operacional.

### 4.2 Classificando a informação

Elena classifica as informações: os prontuários clínicos e as imagens dos pacientes como restritos, os dados de pagamento como restritos, os registros dos funcionários como confidenciais, as agendas de consultas como confidenciais e os materiais de marketing como internos. Cada classe tem regras de tratamento, como a cifração nos dispositivos portáteis para os dados restritos. Ela mantém o esquema em quatro níveis. A ISO/IEC 27002:2022 inclui orientações sobre a classificação e a rotulagem da informação, que ela usa como referência sem copiar seu texto. Ela imprime um guia de uma página para as clínicas, com exemplos de cada classe e as regras de tratamento, e os gerentes das clínicas o afixam nas salas da equipe.

### 4.3 Fornecedores

O Moorfield usa fornecedores para o sistema de prontuários, o software de imagem, os pagamentos, o e-mail e o suporte de TI nas três clínicas com contatos em tempo parcial. Elena lista os acessos e os dados de cada fornecedor. O fornecedor de imagem se conecta remotamente aos computadores das clínicas usando uma senha compartilhada conhecida pela sua equipe de suporte. Elena recomenda contas individuais, autenticação multifator e acesso habilitado apenas durante sessões de suporte aprovadas. O fornecedor de imagem concorda depois que Elena explica as exigências da seguradora do Moorfield, e a mudança é concluída ao longo de dois meses. Ela registra os acessos dos fornecedores num registro revisado a cada trimestre pelo comitê de segurança.

### 4.4 Responsabilidade

Cada ativo e cada relação com fornecedor precisa de um dono. Elena designa os gerentes das clínicas como donos dos dispositivos locais, o líder clínico como dono dos prontuários dos pacientes e a si mesma como dona dos sistemas centrais. As relações com fornecedores ficam com a pessoa que gerencia cada contrato. Ela registra os donos no inventário. O Dr. Qureshi observa que a responsabilidade torna a prestação de contas concreta, sobretudo nas organizações com muitas unidades. Os gerentes das clínicas recebem uma breve orientação explicando o que a responsabilidade significa na prática: saber que dispositivos estão na sua clínica, comunicar mudanças e confirmar as listas de acesso em cada revisão trimestral.

### Exemplo resolvido

Elena concilia o inventário com os registros de dispositivos e da rede, encontra computadores de imagem não registrados, classifica as informações, restringe o acesso do fornecedor de imagem e atribui donos.

> **Caso sintético.** Os inventários são sintéticos.

### Erros e limites

Os dispositivos comprados fora das compras centrais muitas vezes escapam das correções e do backup.

### Exercícios

- **EX016 — Dispositivos não registrados.** Que dispositivos não registrados Elena encontra? *Rubrica:* 3 = computadores de imagem comprados por dentistas;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX017 — Sistemas antigos.** Por que os computadores de imagem rodam sistemas antigos? *Rubrica:* 3 = os fornecedores não certificaram versões mais novas;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX018 — Dados restritos.** Que informações são restritas? *Rubrica:* 3 = prontuários clínicos, imagens e dados de pagamento;; 2 = correto;; 1 = outras;; 0 = nenhuma.

- **EX019 — Correção do fornecedor.** O que Elena recomenda para o acesso do fornecedor de imagem? *Rubrica:* 3 = contas individuais, MFA, acesso só durante as sessões;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX020 — Dono dos prontuários.** Quem é o dono dos prontuários dos pacientes? *Rubrica:* 3 = o líder clínico;; 2 = correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Gestão de correções e de vulnerabilidades

### Objetivos de aprendizagem

Você vai (1) medir a conformidade com as correções entre as unidades; (2) encontrar as unidades que precisam de apoio; (3) projetar a correção para sistemas com restrições.

### 5.1 Medindo a conformidade

Elena define sua medida: a parcela de dispositivos com as atualizações críticas de segurança instaladas em até catorze dias do lançamento, por clínica. Ela extrai dados sintéticos do sistema de gestão de dispositivos. O Dr. Qureshi pede que ela relate tanto o número geral quanto a dispersão entre as clínicas, porque uma boa média pode esconder clínicas com lacunas graves, e os atacantes precisam de apenas um ponto fraco para entrar numa rede conectada. Ela escreve a definição no manual de medidas, com a fonte dos dados, o dono e a frequência do relatório, para que o mesmo número possa ser produzido todo mês.

### 5.2 O laboratório de correções

O laboratório abrange 566 dispositivos sintéticos em vinte e duas clínicas. No geral, 513 dispositivos, 90,6 por cento, receberam as atualizações críticas em até catorze dias. As três clínicas mais baixas são a C19, com 10 de 20 dispositivos, 50,0 por cento; a C15, com 20 de 28, 71,4 por cento; e a C07, com 22 de 30, 73,3 por cento. As três são as clínicas que dependem de um contato local de TI em tempo parcial. Elena observa que o número geral teria escondido essas clínicas por completo. Ela apresenta os resultados por clínica ao comitê de segurança com um breve gráfico, e o comitê concorda que as três clínicas devem receber apoio extra imediatamente, em vez de esperar a revisão trimestral seguinte.

### Laboratório — Conformidade com as correções críticas por clínica sobre dados sintéticos de dispositivos

```python
"""Critical patch compliance per clinic on synthetic device data (stdlib only)."""
import random
random.seed(14)
rows = []
for c in range(1, 23):
    late_p = 0.06 if c not in (7, 15, 19) else 0.30          # three clinics with a part-time IT contact
    for d in range(random.randint(20, 34)):
        rows.append((f"C{c:02d}", random.random() >= late_p))
by = {}
for clinic, ok in rows:
    t = by.setdefault(clinic, [0, 0]); t[0] += ok; t[1] += 1
total_ok = sum(ok for _, ok in rows)
print(f"devices {len(rows)}; patched within 14 days {total_ok} ({total_ok/len(rows):.1%})")
worst = sorted(by.items(), key=lambda kv: kv[1][0] / kv[1][1])[:3]
for c, (ok, n) in worst:
    print(f"{c}: {ok}/{n} ({ok/n:.1%})")
```

Execute com `python3 lab_patch.py`. Saída verificada:

```text
devices 566; patched within 14 days 513 (90.6%)
C19: 10/20 (50.0%)
C15: 20/28 (71.4%)
C07: 22/30 (73.3%)
```

### 5.3 Causas e apoio

Elena visita as três clínicas. Os dispositivos muitas vezes ficam desligados durante a noite, quando as atualizações estão agendadas, e os contatos em tempo parcial não têm tempo para ir atrás deles. Ela muda o agendamento das atualizações para a hora do almoço, com reinicializações automáticas fora dos horários de consulta, e pede ao sistema de gestão de dispositivos que a alerte quando um dispositivo perder dois ciclos. Ela também organiza uma conferência remota mensal pela equipe central. O Dr. Qureshi observa que a correção trata as causas, em vez de culpar a equipe local. Depois de dois meses, as três clínicas passam de noventa por cento.

### 5.4 Sistemas com restrições

Os computadores de imagem nem sempre podem receber atualizações do sistema operacional, porque os fornecedores as restringem. Elena os isola num segmento de rede separado, bloqueia o acesso à internet, exceto ao serviço de atualização do fornecedor, e restringe que dispositivos podem se conectar a eles. Ela registra cada um como uma exceção com data de expiração e um pedido ao fornecedor de uma versão suportada. Ela aprende que, quando corrigir é impossível, reduzir a exposição é o melhor controle seguinte. O fornecedor promete uma versão suportada dentro do ano, e Elena acompanha o compromisso no registro de riscos.

### Exemplo resolvido

Elena mede 90,6 por cento de conformidade geral, encontra três clínicas entre 50,0 e 73,3 por cento, corrige as causas no agendamento e isola os computadores de imagem que não podem ser corrigidos.

> **Caso sintético.** Os dispositivos são sintéticos; as saídas vêm de lab_patch.py.

### Erros e limites

Um número geral de conformidade pode esconder clínicas com lacunas graves.

### Exercícios

- **EX021 — Conformidade geral.** Qual é a conformidade geral com as correções? *Rubrica:* 3 = 513 de 566, 90,6 por cento;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX022 — Clínica mais baixa.** Qual é a clínica mais baixa? *Rubrica:* 3 = C19, com 50,0 por cento;; 2 = correto;; 1 = errado;; 0 = nenhuma.

- **EX023 — Fator comum.** O que as três clínicas mais baixas têm em comum? *Rubrica:* 3 = um contato local de TI em tempo parcial;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX024 — Correção do agendamento.** Como o agendamento das atualizações é alterado? *Rubrica:* 3 = hora do almoço, com reinicializações fora das consultas;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX025 — Controle da imagem.** Como os computadores de imagem que não podem ser corrigidos são protegidos? *Rubrica:* 3 = segmento isolado e acesso restrito;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Identidade e acesso

### Objetivos de aprendizagem

Você vai (1) projetar o acesso baseado em papéis para os sistemas clínicos; (2) revisar os acessos entre as unidades; (3) proteger o acesso privilegiado e o remoto.

### 6.1 Papéis

Elena projeta papéis para o sistema de prontuários: dentista, higienista, auxiliar de saúde bucal, recepcionista, gerente de clínica e administrador central. Cada papel tem permissões definidas. As recepcionistas veem as consultas e os dados de contato, mas não as anotações clínicas; as auxiliares veem as anotações clínicas dos pacientes da sua clínica. Antes, muitos funcionários tinham acessos amplos, copiados de colegas. O Dr. Qureshi observa que os ambientes clínicos precisam de acesso rápido em emergências, então os papéis precisam ser projetados com os clínicos, e não impostos a eles. Ela conduz duas oficinas com os clínicos para testar os papéis.

### 6.2 Acesso de emergência

Às vezes os clínicos precisam de prontuários de outra clínica, por exemplo, quando um paciente é atendido numa unidade que não é a sua. Elena projeta um acesso de emergência, do tipo quebra-vidro: os funcionários podem abrir esse prontuário depois de declarar um motivo, a ação é registrada em log e o líder clínico revisa um relatório semanal. A maioria dos usos é legítima. O Dr. Qureshi explica que o acesso de emergência equilibra o cuidado com o paciente e a privacidade, desde que as revisões de fato aconteçam e os funcionários saibam disso. O líder clínico revisa o relatório do primeiro mês e encontra todos os usos explicados, o que tranquiliza a equipe e os representantes dos pacientes. Elena registra a revisão na ata do comitê de segurança.

### 6.3 Revisões de acessos

Elena conduz revisões trimestrais comparando as contas do sistema com a lista de funcionários dos recursos humanos. A primeira revisão encontra ex-funcionários com contas ativas, na maioria dentistas substitutos cujos contratos terminaram. Ela acrescenta as datas de término dos substitutos ao sistema dos recursos humanos, para que as contas expirem automaticamente. Ela aprende que a equipe temporária é uma fonte comum de acessos remanescentes nos ambientes clínicos. A primeira revisão leva dois dias; ela espera que as seguintes sejam mais rápidas à medida que as contas remanescentes forem eliminadas. A segunda revisão, três meses depois, encontra apenas uma conta de ex-funcionário, que pertencia a um substituto cuja data de término tinha sido lançada incorretamente.

### 6.4 Acesso privilegiado e remoto

Os administradores centrais e os fornecedores têm acessos poderosos. Elena exige contas de administrador separadas, com chaves de segurança físicas, e acesso de fornecedores apenas por meio de um gateway gerenciado, com autenticação multifator e sessões gravadas. Ela elimina as senhas de administrador compartilhadas. Ela observa que o princípio do menor privilégio de Saltzer e Schroeder e as orientações de controle de acesso da NIST SP 800-53 Revisão 5 sustentam essas medidas. O Dr. Qureshi pede que ela meça a adesão. Em um mês, todos os administradores centrais usam chaves físicas, e os três fornecedores com acesso remoto usam o gateway. Ela relata os números de adesão ao comitê de segurança.

### Exemplo resolvido

Elena projeta seis papéis clínicos com os clínicos, acrescenta um acesso de emergência registrado em log, liga as datas de término dos substitutos à expiração das contas e protege o acesso privilegiado e o dos fornecedores.

> **Caso sintético.** Os sistemas são sintéticos.

### Erros e limites

Copiar os acessos dos colegas espalha direitos em excesso pelas clínicas.

### Exercícios

- **EX026 — Visão da recepcionista.** O que as recepcionistas podem ver? *Rubrica:* 3 = as consultas e os dados de contato;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX027 — Revisão do acesso de emergência.** Quem revisa o uso do acesso de emergência? *Rubrica:* 3 = o líder clínico, semanalmente;; 2 = correto;; 1 = nada;; 0 = nenhuma.

- **EX028 — Acesso remanescente.** Que funcionários mais mantinham acessos? *Rubrica:* 3 = dentistas substitutos;; 2 = correto;; 1 = outros;; 0 = nenhuma.

- **EX029 — Fator do administrador.** O que protege as contas de administrador? *Rubrica:* 3 = chaves de segurança físicas;; 2 = correto;; 1 = outro;; 0 = nenhuma.

- **EX030 — Gateway dos fornecedores.** Como os fornecedores se conectam? *Rubrica:* 3 = gateway gerenciado com MFA e sessões gravadas;; 2 = correto;; 1 = nada;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). Elena Petrova, o Dr. Hamid Qureshi, a Thornbury Business School, o Moorfield Dental Group e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Vinte e duas clínicas.

**EX002.** Quatro pessoas, lideradas por Elena.

**EX003.** Os atrasos nas correções nas clínicas pequenas.

**EX004.** Frameworks, métodos de medição e habilidades de comunicação com o conselho.

**EX005.** Um documento do programa aprovado pelo conselho.

**EX006.** Elena, o diretor de operações e um líder clínico.

**EX007.** Registros que mostrem que as atividades acontecem de forma coerente.

**EX008.** Nenhuma clínica impossibilitada de atender pacientes por mais de meio dia.

**EX009.** O laboratório de prótese, tratado como fornecedor.

**EX010.** ISO/IEC 27000:2026.

**EX011.** O ransomware.

**EX012.** Quando as classificações diferem em mais de um ponto.

**EX013.** Os atrasos nas correções e os testes de recuperação fracos.

**EX014.** Revisões de acessos e alertas sobre visualizações incomuns de prontuários.

**EX015.** O seguro cibernético.

**EX016.** Computadores de imagem comprados diretamente pelos dentistas.

**EX017.** Os fornecedores de imagem não certificaram versões mais novas.

**EX018.** Os prontuários clínicos dos pacientes, as imagens e os dados de pagamento.

**EX019.** Contas individuais, autenticação multifator e acesso apenas durante as sessões.

**EX020.** O líder clínico.

**EX021.** 513 de 566 dispositivos, 90,6 por cento.

**EX022.** A C19, com 10 de 20 dispositivos, 50,0 por cento.

**EX023.** Elas dependem de um contato local de TI em tempo parcial.

**EX024.** Para a hora do almoço, com reinicializações automáticas fora dos horários de consulta.

**EX025.** Isolando-os num segmento separado, com acesso restrito.

**EX026.** As consultas e os dados de contato, mas não as anotações clínicas.

**EX027.** O líder clínico, por meio de um relatório semanal.

**EX028.** Dentistas substitutos cujos contratos terminaram.

**EX029.** Chaves de segurança físicas.

**EX030.** Por um gateway gerenciado, com autenticação multifator e sessões gravadas.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO/IEC 27001:2022, citada nesta edição como referência brasileira e conferida em sua fonte oficial; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (with Amd 1:2024). <https://www.iso.org/standard/27001>
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939
