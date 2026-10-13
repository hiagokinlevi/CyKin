# Segurança da Informação: Curso de Pós-Graduação

- Idioma: português do Brasil (`pt`); curso 140, curso de pós-graduação (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–12 de 12 têm texto didático escrito à mão; os exercícios EX001–EX060 têm resoluções correspondentes com rubricas de 0 a 3; os dois laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

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

- **EX001 — Número de clínicas.** Quantas clínicas o Moorfield mantém? *Rubrica:* 3 = vinte e duas;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX002 — Equipe central.** Qual é o tamanho da equipe central de TI? *Rubrica:* 3 = quatro pessoas;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX003 — Problemas do ambiente de trabalho.** Cite um problema do ambiente de trabalho que Elena traz. *Rubrica:* 3 = atrasos nas correções nas clínicas pequenas;; 2 = um;; 1 = vago;; 0 = nenhuma.

- **EX004 — Acréscimo do curso.** O que o curso acrescenta à experiência de Elena? *Rubrica:* 3 = frameworks, medição e comunicação com o conselho;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX005 — Evidência da meta.** Que evidência mostra que a meta do programa foi atingida? *Rubrica:* 3 = um documento do programa aprovado pelo conselho;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

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

- **EX006 — Membros do comitê.** Quem faz parte do comitê de segurança? *Rubrica:* 3 = Elena, o diretor de operações, um líder clínico;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX007 — Registros faltantes.** O que falta ao Moorfield, apesar de realizar as atividades? *Rubrica:* 3 = registros;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX008 — Acréscimo do conselho.** Que limite o conselho acrescenta? *Rubrica:* 3 = nenhuma clínica sem atender pacientes por mais de meio dia;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX009 — Parte excluída.** O que fica excluído do escopo? *Rubrica:* 3 = o laboratório de prótese;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX010 — Norma de visão geral.** Que norma dá a visão geral da família? *Rubrica:* 3 = ISO/IEC 27000:2026;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

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

- **EX011 — Exemplo de ameaça.** Cite uma das principais ameaças identificadas. *Rubrica:* 3 = ransomware;; 2 = uma;; 1 = vago;; 0 = nenhuma.

- **EX012 — Regra de calibração.** Quando os avaliadores discutem as diferenças? *Rubrica:* 3 = quando diferem em mais de um ponto;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX013 — Riscos ligados.** Que dois riscos agravam o dano do ransomware? *Rubrica:* 3 = atrasos nas correções e recuperação fraca;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX014 — Tratamento do uso indevido.** Como o uso indevido pela equipe é tratado? *Rubrica:* 3 = revisões de acessos e alertas sobre visualizações incomuns;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX015 — Método de transferência.** O que transfere parte da perda financeira? *Rubrica:* 3 = o seguro cibernético;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

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

- **EX016 — Dispositivos não registrados.** Que dispositivos não registrados Elena encontra? *Rubrica:* 3 = computadores de imagem comprados por dentistas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX017 — Sistemas antigos.** Por que os computadores de imagem rodam sistemas antigos? *Rubrica:* 3 = os fornecedores não certificaram versões mais novas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX018 — Dados restritos.** Que informações são restritas? *Rubrica:* 3 = prontuários clínicos, imagens e dados de pagamento;; 2 = parcialmente correto;; 1 = outras;; 0 = nenhuma.

- **EX019 — Correção do fornecedor.** O que Elena recomenda para o acesso do fornecedor de imagem? *Rubrica:* 3 = contas individuais, MFA, acesso só durante as sessões;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX020 — Dono dos prontuários.** Quem é o dono dos prontuários dos pacientes? *Rubrica:* 3 = o líder clínico;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

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

- **EX021 — Conformidade geral.** Qual é a conformidade geral com as correções? *Rubrica:* 3 = 513 de 566, 90,6 por cento;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX022 — Clínica mais baixa.** Qual é a clínica mais baixa? *Rubrica:* 3 = C19, com 50,0 por cento;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX023 — Fator comum.** O que as três clínicas mais baixas têm em comum? *Rubrica:* 3 = um contato local de TI em tempo parcial;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX024 — Correção do agendamento.** Como o agendamento das atualizações é alterado? *Rubrica:* 3 = hora do almoço, com reinicializações fora das consultas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX025 — Controle da imagem.** Como os computadores de imagem que não podem ser corrigidos são protegidos? *Rubrica:* 3 = segmento isolado e acesso restrito;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

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

- **EX026 — Visão da recepcionista.** O que as recepcionistas podem ver? *Rubrica:* 3 = as consultas e os dados de contato;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX027 — Revisão do acesso de emergência.** Quem revisa o uso do acesso de emergência? *Rubrica:* 3 = o líder clínico, semanalmente;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX028 — Acesso remanescente.** Que funcionários mais mantinham acessos? *Rubrica:* 3 = dentistas substitutos;; 2 = parcialmente correto;; 1 = outros;; 0 = nenhuma.

- **EX029 — Fator do administrador.** O que protege as contas de administrador? *Rubrica:* 3 = chaves de segurança físicas;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX030 — Gateway dos fornecedores.** Como os fornecedores se conectam? *Rubrica:* 3 = gateway gerenciado com MFA e sessões gravadas;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-07"></a>

## Capítulo 7 — Phishing e segurança do e-mail

### Objetivos de aprendizagem

Você vai (1) analisar os padrões de phishing nos dados de e-mail; (2) detectar domínios de remetente parecidos; (3) combinar controles técnicos e humanos contra o phishing.

### 7.1 O problema

As clínicas do Moorfield recebem e-mails de phishing com frequência, alguns fingindo vir da sede ou de fornecedores e pedindo pagamentos ou dados de login. No ano passado, uma gerente de clínica digitou sua senha numa página de login falsa, e a conta enviou phishing a pacientes antes de ser bloqueada. Elena quer entender os padrões. O Dr. Qureshi sugere começar pelos domínios dos remetentes, porque muitos ataques usam domínios quase idênticos aos genuínos, o que uma equipe ocupada raramente percebe. Ela pede ao provedor de e-mail uma exportação de três meses de logs.

### 7.2 O laboratório dos domínios parecidos

O laboratório lê um log sintético de 5.823 mensagens recebidas de 68 domínios de remetente distintos. Ele compara cada domínio com o domínio do próprio Moorfield usando a distância de edição, o número de mudanças de um único caractere necessárias para transformar um no outro. Quatro domínios estão a até duas mudanças, como o algarismo um no lugar da letra l ou um hífen inserido, e 23 mensagens vieram deles. Elena observa que os quatro passariam numa olhada rápida. Ela mostra os quatro domínios ao comitê de segurança lado a lado com o genuíno, e nenhum dos membros identifica todas as diferenças sem ajuda.

### Laboratório — Sinalizando domínios de remetente parecidos por distância de edição num log sintético de e-mail

```python
"""Flag lookalike sender domains by edit distance in a synthetic mail log (stdlib only)."""
import random
random.seed(30)
OWN = "moorfielddental.example"
def dist(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]
fakes = ["moorfie1ddental.example", "moorfielddentai.example", "moorfield-dental.example", "moorfielddental.examp1e"]
normal = [f"supplier{i}.example" for i in range(60)] + ["labwork.example", "dentalsupply.example", "bank.example"]
log = [random.choice(normal) for _ in range(5000)] + [OWN] * 800 + [random.choice(fakes) for _ in range(23)]
flag = {d for d in set(log) if d != OWN and dist(d, OWN) <= 2}
n_flag = sum(d in flag for d in log)
print(f"messages {len(log)}; distinct sender domains {len(set(log))}")
print(f"lookalike domains (distance <= 2): {sorted(flag)}; messages from them {n_flag}")
```

Execute com `python3 lab_lookalike.py`. Saída verificada:

```text
messages 5823; distinct sender domains 68
lookalike domains (distance <= 2): ['moorfie1ddental.example', 'moorfield-dental.example', 'moorfielddentai.example', 'moorfielddental.examp1e']; messages from them 23
```

### 7.3 Controles técnicos

Elena pede ao provedor de e-mail que coloque em quarentena as mensagens de domínios a até duas edições do domínio do Moorfield e dos domínios dos principais fornecedores, e que marque todas as mensagens externas com uma faixa visível. Ela publica registros de autenticação de e-mail para o domínio do Moorfield, para que os sistemas destinatários possam rejeitar as mensagens que alegam falsamente vir dele. Ela também ativa a autenticação multifator em todas as caixas postais, para que uma senha roubada sozinha não abra mais uma conta. Depois de um mês, a quarentena pega várias novas mensagens de domínios parecidos, e o provedor de e-mail confirma que as mensagens que usam falsamente o próprio domínio do Moorfield agora são rejeitadas.

### 7.4 Controles humanos

Os controles técnicos deixam passar alguns ataques. Elena introduz uma regra simples para as mudanças de pagamento e de dados bancários: sempre confirmar ligando para um número conhecido, nunca para um informado no e-mail. Ela acrescenta um botão de comunicação e agradece a cada pessoa que comunica. Breves exemplos mensais mostram domínios parecidos reais, com as diferenças destacadas. O Dr. Qureshi observa que as pessoas e a tecnologia juntas dão uma proteção melhor do que qualquer uma delas sozinha. Os gerentes das clínicas dizem que os exemplos mensais são úteis porque a equipe os discute nas reuniões. Em três meses, as comunicações de e-mails suspeitos dobram, e a equipe central encontra duas campanhas mais cedo do que antes.

### Exemplo resolvido

Elena analisa 5.823 mensagens sintéticas, encontra quatro domínios parecidos que enviaram 23 mensagens, coloca em quarentena os quase idênticos, acrescenta a autenticação de e-mail e a MFA e define uma regra de retorno de ligação.

> **Caso sintético.** Os dados de e-mail são sintéticos; as saídas vêm de lab_lookalike.py.

### Erros e limites

Os domínios parecidos passam numa olhada rápida, então depender de que a equipe os perceba fracassa.

### Exercícios

- **EX031 — Número de mensagens.** Quantas mensagens o log contém? *Rubrica:* 3 = 5.823;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX032 — Número de domínios parecidos.** Quantos domínios parecidos são sinalizados? *Rubrica:* 3 = quatro;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX033 — Mensagens dos domínios parecidos.** Quantas mensagens vieram de domínios parecidos? *Rubrica:* 3 = 23;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX034 — Distância de edição.** O que a distância de edição conta? *Rubrica:* 3 = as mudanças de um único caractere entre as cadeias;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX035 — Regra de pagamento.** Qual é a regra para as mudanças de pagamento? *Rubrica:* 3 = confirmar ligando para um número conhecido;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-08"></a>

## Capítulo 8 — Backup, ransomware e recuperação

### Objetivos de aprendizagem

Você vai (1) projetar backups resistentes ao ransomware; (2) testar a recuperação em relação aos objetivos; (3) planejar a continuidade das clínicas.

### 8.1 Projeto dos backups

O Moorfield faz backup noturno do sistema de prontuários para um servidor na sede, alcançável pela mesma rede. Elena reconhece que um ransomware poderia cifrar os dois. Ela acrescenta cópias imutáveis mantidas por um prestador de backup durante trinta dias, que não podem ser apagadas nem pelos administradores do Moorfield. Ela também separa as credenciais de administração dos backups das contas de administrador do dia a dia. O Dr. Qureshi observa que os grupos de ransomware muitas vezes miram primeiro os backups, então os backups precisam ser projetados contra ataques deliberados, e não apenas contra acidentes. O conselho aprova o custo anual do prestador.

### 8.2 Objetivos de recuperação

Elena acorda os objetivos com o líder clínico e com o diretor de operações, de forma coerente com o apetite do conselho. O sistema de prontuários precisa voltar em até quatro horas e perder no máximo uma hora de dados. Os sistemas de imagem precisam voltar em até um dia; enquanto isso, as clínicas podem continuar com anotações em papel. O e-mail pode esperar um dia. Ela aprende que os objetivos precisam ser acordados com quem arca com as consequências, porque as equipes técnicas sozinhas tendem a subestimar ou superestimar a urgência. Os objetivos são registrados no plano de recuperação e assinados pelos dois gerentes.

### 8.3 Testando

Elena testa uma restauração completa do sistema de prontuários num ambiente isolado. A restauração dá certo, mas leva seis horas, deixando de cumprir o objetivo de quatro horas, principalmente porque o banco de dados é copiado lentamente a partir do prestador. Ela providencia uma opção de recuperação mais rápida: um snapshot recente mantido localmente em armazenamento imutável. Um segundo teste se completa em três horas. Ela aprende que somente os testes cronometrados revelam se os objetivos podem ser alcançados. Ela registra passo a passo as linhas do tempo dos dois testes e acrescenta o procedimento do snapshot local ao runbook de recuperação, para que qualquer membro da equipe central possa segui-lo.

### 8.4 Continuidade das clínicas

Elena trabalha com os gerentes das clínicas em planos de continuidade para as interrupções dos sistemas: listas de consultas impressas todas as noites, anotações clínicas em papel lançadas depois no sistema e os contatos de emergência dos pacientes com consulta marcada. Uma clínica testa o plano durante uma atualização planejada do sistema e identifica que faltavam os formulários de consentimento em papel. Os formulários são acrescentados. O Dr. Qureshi observa que o planejamento da continuidade mantém o atendimento aos pacientes enquanto a recuperação técnica acontece. Cada clínica guarda uma pequena caixa de continuidade com os formulários impressos, a lista de consultas mais recente e os números de contato, e os gerentes das clínicas conferem seu conteúdo todo mês.

### Exemplo resolvido

Elena acrescenta backups imutáveis de trinta dias e credenciais separadas, acorda os objetivos de recuperação, melhora uma restauração de seis horas para três e testa as alternativas em papel nas clínicas.

> **Caso sintético.** Os testes são sintéticos.

### Erros e limites

Os backups alcançáveis com as credenciais de administrador do dia a dia podem ser destruídos por um ransomware.

### Exercícios

- **EX036 — Período imutável.** Por quanto tempo as cópias imutáveis são mantidas? *Rubrica:* 3 = trinta dias;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX037 — Objetivos dos prontuários.** Quais são os objetivos do sistema de prontuários? *Rubrica:* 3 = quatro horas, uma hora de dados;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX038 — Primeiro teste.** Quanto tempo levou a primeira restauração? *Rubrica:* 3 = seis horas;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX039 — Segundo teste.** Quanto tempo levou o segundo teste? *Rubrica:* 3 = três horas;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX040 — Formulários faltantes.** O que faltava no teste de continuidade? *Rubrica:* 3 = os formulários de consentimento em papel;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

<a id="ch-09"></a>

## Capítulo 9 — Resposta a incidentes e notificação

### Objetivos de aprendizagem

Você vai (1) construir um processo de resposta a incidentes para uma organização com várias unidades; (2) cumprir as obrigações de notificação; (3) aprender com os incidentes.

### 9.1 Processo

Elena escreve o processo de incidentes do Moorfield. Qualquer funcionário pode comunicar por um único número de telefone ou endereço de e-mail. A equipe central avalia a gravidade usando uma breve tabela. Os incidentes graves acionam um líder do incidente, um contato de comunicação e a notificação ao diretor de operações. O processo abrange a contenção, a investigação, a recuperação e o encerramento. Ela o alinha às funções Responder e Recuperar do NIST Cybersecurity Framework 2.0. O Dr. Qureshi aconselha manter o processo curto o bastante para ser usado sob pressão. O processo cabe em duas páginas, com uma tabela de gravidade.

### 9.2 Notificação

As violações de dados de saúde podem exigir a notificação aos reguladores e aos pacientes dentro de prazos rígidos, segundo a legislação de proteção de dados, que varia conforme o país. Elena trabalha com o encarregado de proteção de dados do Moorfield para definir quem decide se a notificação é necessária e como as evidências são reunidas rapidamente. O seguro cibernético também exige aviso imediato. Ela acrescenta uma lista de verificação para que essas obrigações sejam consideradas cedo, em vez de descobertas depois que os prazos já passaram. O encarregado de proteção de dados aprova a lista, e Elena a imprime no verso do processo de incidentes, para que os dois estejam sempre juntos. O número de notificação da seguradora é acrescentado à primeira página.

### 9.3 Exercício

Elena conduz um exercício: uma recepcionista de clínica comunica que pacientes estão recebendo mensagens de texto pedindo pagamento numa conta desconhecida, aparentemente enviadas pelo Moorfield. Os participantes rastreiam a causa até uma conta comprometida no fornecedor de mensagens de texto. Eles descobrem que o contrato do Moorfield não exige que o fornecedor notifique os incidentes prontamente. Elena acrescenta isso à revisão de fornecedores. O Dr. Qureshi observa que os exercícios muitas vezes revelam lacunas de fornecedores, porque os fornecedores raramente são incluídos no planejamento. O diretor de operações contata o fornecedor na semana seguinte para acordar novos termos.

### 9.4 Aprendizado

Depois de cada incidente real, Elena faz uma breve revisão sem culpa: o que aconteceu, por que os controles não o impediram, o que funcionou e o que vai mudar. Ela acompanha as ações até a conclusão. Ao longo de um ano, as revisões levam a melhorias na filtragem de e-mail, nos contratos com fornecedores e na expiração das contas dos substitutos. Ela aprende que os incidentes são lições caras, e que registrá-los e agir a partir deles é como uma organização extrai valor do custo. Ela mantém um registro das revisões e das ações, e o comitê de segurança confere o progresso das ações em aberto em cada reunião mensal.

### Exemplo resolvido

Elena escreve um processo de incidentes curto para várias unidades, alinhado às funções Responder e Recuperar do CSF 2.0, acrescenta uma lista de verificação de notificação, conduz um exercício envolvendo um fornecedor e faz revisões sem culpa.

> **Caso sintético.** Os incidentes são sintéticos; as regras de notificação variam conforme o país.

### Erros e limites

Descobrir tarde os prazos de notificação pode transformar um incidente numa infração regulatória.

### Exercícios

- **EX041 — Canal de comunicação.** Como os funcionários comunicam incidentes? *Rubrica:* 3 = um único número de telefone ou endereço de e-mail;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX042 — Alinhamento ao CSF.** Que funções do CSF 2.0 orientam o processo? *Rubrica:* 3 = Responder e Recuperar;; 2 = parcialmente correto;; 1 = outras;; 0 = nenhuma.

- **EX043 — Parceiro na notificação.** Quem ajuda a decidir sobre a notificação? *Rubrica:* 3 = o encarregado de proteção de dados;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX044 — Lacuna do exercício.** Que lacuna o exercício revelou? *Rubrica:* 3 = o fornecedor não era obrigado a notificar prontamente;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX045 — Resultado das revisões.** Cite uma melhoria resultante das revisões. *Rubrica:* 3 = a expiração das contas dos substitutos;; 2 = uma;; 1 = vago;; 0 = nenhuma.

<a id="ch-10"></a>

## Capítulo 10 — Métricas, relatórios e o conselho

### Objetivos de aprendizagem

Você vai (1) escolher medidas ligadas aos riscos; (2) relatar a um conselho não especialista; (3) usar as medidas para orientar as decisões.

### 10.1 Medidas

Elena seleciona seis medidas ligadas aos principais riscos: a conformidade com as correções críticas por clínica, a adesão à autenticação multifator, as mensagens de domínios parecidos colocadas em quarentena, os resultados dos testes cronometrados de recuperação, as contas de ex-funcionários encontradas nas revisões e os incidentes por tipo. Cada uma tem uma definição, uma fonte, um dono e uma meta. Ela evita contagens que apenas parecem impressionantes, como as conexões bloqueadas. O Dr. Qureshi observa que cada medida deve responder a uma pergunta que o conselho faria. Ela escreve cada definição no manual de medidas, e a equipe central testa se os números podem ser produzidos todo mês a partir dos sistemas existentes, sem esforço manual.

### 10.2 Linhas de base

Elena usa o trabalho do curso como linhas de base: a conformidade com as correções de 90,6 por cento, com três clínicas muito abaixo; quatro domínios parecidos na amostra sintética de e-mail; uma primeira restauração de seis horas; e várias contas de ex-funcionários na primeira revisão. Ela mostra a melhora desde então: a conformidade das clínicas com as correções acima de noventa por cento, a quarentena em funcionamento e uma restauração de três horas. As linhas de base tornam o progresso visível para o conselho. Ela mostra a linha de base e o valor mais recente de cada medida numa tabela simples, para que o conselho veja onde houve progresso e onde ainda há trabalho, incluindo as exceções de imagem ainda em aberto.

### 10.3 Relatório ao conselho

Elena projeta um relatório trimestral de duas páginas. A primeira página mostra as seis medidas com setas de tendência e uma frase sobre cada uma. A segunda página lista os principais riscos, as mudanças desde o último trimestre e as decisões necessárias. O conselho faz menos perguntas técnicas e mais perguntas sobre prioridades e recursos. Um sócio pergunta por que os computadores de imagem continuam como exceções, o que leva à decisão de pressionar o fornecedor em conjunto com outros grupos odontológicos. O conselho decide contatar dois outros grupos odontológicos que usam o mesmo software de imagem e enviar ao fornecedor um pedido conjunto de uma versão atualizada e suportada.

### 10.4 Orientando as decisões

As medidas importam quando mudam as decisões. Elena mostra como a medida de correções por clínica levou ao apoio às três clínicas e como o teste de restauração levou ao snapshot local. Ela propõe interromper uma medida que nunca muda as decisões. O Dr. Qureshi observa que os sistemas de medição devem ser podados, e não apenas ampliados, para que a atenção permaneça no que importa. O comitê concorda em deixar de relatar ao conselho o número de mensagens em quarentena, mantendo-o como medida interna da equipe central, porque ele subia e descia com a atividade dos atacantes, e não com algo que o Moorfield controlasse.

### Exemplo resolvido

Elena liga seis medidas aos riscos, usa os resultados do curso como linhas de base, escreve um relatório de duas páginas ao conselho e mostra como as medidas mudaram as decisões.

> **Caso sintético.** As medidas são sintéticas.

### Erros e limites

As medidas que nunca mudam as decisões desperdiçam atenção.

### Exercícios

- **EX046 — Número de medidas.** Quantas medidas Elena seleciona? *Rubrica:* 3 = seis;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX047 — Contagem evitada.** Que contagem Elena evita? *Rubrica:* 3 = as conexões bloqueadas;; 2 = parcialmente correto;; 1 = outra;; 0 = nenhuma.

- **EX048 — Extensão do relatório.** Qual é a extensão do relatório ao conselho? *Rubrica:* 3 = duas páginas;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX049 — Decisão sobre a imagem.** Que decisão decorre da pergunta sobre a imagem? *Rubrica:* 3 = pressionar o fornecedor em conjunto com outros grupos;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX050 — Poda.** O que Elena propõe para as medidas sem uso? *Rubrica:* 3 = interrompê-las;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-11"></a>

## Capítulo 11 — Projeto final

### Objetivos de aprendizagem

Você vai (1) definir um projeto final de melhoria; (2) entregá-lo com evidências; (3) avaliar os resultados em relação às metas.

### 11.1 Escolhendo o projeto

O projeto final de Elena trata do risco que o conselho classificou como o mais alto: o ransomware. Seu projeto combina três melhorias já iniciadas: o apoio às correções nas clínicas, os backups imutáveis com recuperação mais rápida e a autenticação multifator para todas as contas. A meta é que o Moorfield possa mostrar, com evidências, que um ataque de ransomware seria mais difícil de iniciar, mais lento para se espalhar e mais rápido de recuperar. O Dr. Qureshi aprova o projeto e pede critérios de sucesso claros. Ela escreve um termo de abertura do projeto de uma página, com o escopo, o cronograma e os critérios, aprovado pelo diretor de operações.

### 11.2 Critérios de sucesso

Elena define os critérios: conformidade com as correções críticas de pelo menos noventa e cinco por cento no geral e de noventa por cento em cada clínica; autenticação multifator para todas as contas, com as exceções documentadas; backups imutáveis para todos os sistemas críticos; e uma recuperação cronometrada do sistema de prontuários em até quatro horas. Cada critério tem uma medida e uma fonte de evidência. Ela aprende que critérios claros tornam a avaliação do projeto final simples e honesta. Ela lista os critérios numa tabela com a medida, a fonte dos dados e a data em que cada um será conferido. O diretor de operações e o líder clínico assinam a tabela.

### 11.3 Entrega

Ao longo de quatro meses, Elena entrega as melhorias. A conformidade com as correções sobe acima de noventa e cinco por cento no geral, embora uma clínica permaneça em noventa e dois por cento por causa de uma exceção de imagem. A adesão à autenticação multifator alcança todas as contas da equipe, com duas exceções de contas de serviço documentadas. Os backups imutáveis abrangem todos os sistemas críticos. Uma recuperação cronometrada final se completa em três horas e dez minutos. Ela registra evidências de cada um. Ela mantém um registro do projeto com a data em que cada marco foi alcançado e a evidência guardada para ele. O registro, com links para as evidências, forma um apêndice do seu relatório do projeto final.

### 11.4 Avaliação

Elena avalia com honestidade. Três critérios são cumpridos; o critério de correções por clínica deixa de ser cumprido por pouco numa clínica, com um motivo e um plano claros. Ela observa que o projeto mostra uma melhora na preparação, mas não pode provar que o Moorfield resistiria a um ataque real. Ela recomenda um teste independente da resposta a incidentes dentro do próximo ano. O Dr. Qureshi elogia a avaliação honesta como a parte mais importante. Ela apresenta a avaliação numa tabela que mostra cada critério, o resultado e se ele foi cumprido, com o motivo do critério não cumprido indicado ao lado.

### Exemplo resolvido

Elena define um projeto final sobre ransomware com quatro critérios, entrega as correções, a MFA, os backups imutáveis e uma recuperação de três horas e dez minutos e avalia um critério como não cumprido por pouco.

> **Caso sintético.** Os resultados são sintéticos.

### Erros e limites

Afirmar que um projeto prova a resiliência contra ataques reais exagera as evidências.

### Exercícios

- **EX051 — Risco do projeto final.** De que risco o projeto final trata? *Rubrica:* 3 = ransomware;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX052 — Critério por clínica.** Qual é o critério de correções por clínica? *Rubrica:* 3 = pelo menos noventa por cento em cada clínica;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX053 — Critério não cumprido.** Que critério deixa de ser cumprido por pouco? *Rubrica:* 3 = a conformidade com as correções por clínica;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX054 — Recuperação final.** Quanto tempo levou a recuperação final? *Rubrica:* 3 = três horas e dez minutos;; 2 = parcialmente correto;; 1 = errado;; 0 = nenhuma.

- **EX055 — Próximo passo.** O que Elena recomenda em seguida? *Rubrica:* 3 = um teste independente da resposta a incidentes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<a id="ch-12"></a>

## Capítulo 12 — Apresentação do projeto final e próximos passos

### Objetivos de aprendizagem

Você vai (1) apresentar um projeto final a examinadores e a um conselho; (2) responder a questionamentos; (3) planejar a melhoria contínua.

### 12.1 Apresentação

Elena apresenta seu projeto final ao Dr. Qureshi, a um examinador externo e ao conselho do Moorfield. Ela aborda o risco, os critérios, a entrega, as evidências e a avaliação em vinte minutos, com slides de apoio mostrando os dados. Ela usa a linguagem do conselho: clínicas capazes de atender os pacientes e prontuários dos pacientes protegidos. O Dr. Qureshi a havia aconselhado a começar pelo resultado para o negócio e a guardar os detalhes técnicos para as perguntas. Ela ensaia duas vezes com colegas do curso, que pedem que ela encurte a introdução e adiante um gráfico. Ela também prepara um folheto de uma página resumindo os critérios e os resultados para os membros do conselho.

### 12.2 Questionamentos

O examinador externo pergunta se a conformidade com as correções mede a exposição com precisão quando os computadores de imagem são excluídos por exceção. Elena explica os controles de isolamento e mostra os registros de exceção, aceitando que a exposição permanece. Um sócio pergunta sobre o custo; ela mostra que a maioria das melhorias usou licenças e tempo da equipe já existentes, com o prestador de backup como o principal custo novo. As duas respostas são claras e baseadas em evidências. O examinador também pergunta como ela saberia se as melhorias se deteriorassem com o tempo, e ela aponta as medidas trimestrais e o teste anual de recuperação.

### 12.3 Resultado

Elena é aprovada no projeto final com distinção. O conselho adota suas medidas como relatório trimestral permanente e aprova um teste independente da resposta a incidentes. Elena reflete que o curso lhe deu estruturas para organizar o que ela já sabia e a confiança para apresentar a segurança como uma questão de negócio. Ela observa que suas relações com os gerentes das clínicas melhoraram quando eles viram os problemas sendo resolvidos, em vez de atribuídos a culpados. Os gerentes das clínicas enviam uma breve mensagem agradecendo à equipe central pelo apoio nas correções. O Dr. Qureshi pede a permissão dela para usar o projeto final como exemplo para futuros alunos.

### 12.4 Próximos passos

Elena planeja os próximos passos: o teste independente, uma revisão da avaliação de riscos em um ano e a preparação para uma possível certificação ISO/IEC 27001, que grandes seguradoras começaram a solicitar. Ela também planeja orientar um membro júnior da equipe pelos mesmos métodos. O próximo curso nesta área, governança de dados, examina como são tomadas as decisões sobre a propriedade, a qualidade e o uso dos dados, o que complementa o programa de segurança que ela construiu. O conselho pede que ela apresente um plano de prontidão para a certificação dentro de seis meses.

### Exemplo resolvido

Elena apresenta seu projeto final em termos de negócio, responde aos questionamentos sobre as exceções de imagem e o custo, é aprovada com distinção e planeja a prontidão para a certificação.

> **Caso sintético.** A apresentação é sintética.

### Erros e limites

Começar pelos detalhes técnicos faz perder a atenção de um conselho.

### Exercícios

- **EX056 — Linguagem do conselho.** Que linguagem Elena usa com o conselho? *Rubrica:* 3 = clínicas capazes de atender os pacientes;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX057 — Principal custo novo.** Qual foi o principal custo novo? *Rubrica:* 3 = o prestador de backup;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX058 — Resultado do projeto final.** Que resultado Elena alcança? *Rubrica:* 3 = distinção;; 2 = parcialmente correto;; 1 = outro;; 0 = nenhuma.

- **EX059 — Adoção pelo conselho.** O que o conselho adota? *Rubrica:* 3 = as medidas de Elena como relatório trimestral;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

- **EX060 — Motivação da certificação.** Por que considerar a certificação ISO/IEC 27001? *Rubrica:* 3 = as seguradoras começaram a solicitá-la;; 2 = parcialmente correto;; 1 = vago;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. Elena Petrova, o Dr. Hamid Qureshi, a Thornbury Business School, o Moorfield Dental Group e todos os números são sintéticos; as respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX031.** 5.823 mensagens.

**EX032.** Quatro domínios.

**EX033.** 23 mensagens.

**EX034.** As mudanças de um único caractere necessárias para transformar um domínio em outro.

**EX035.** Sempre confirmar ligando para um número conhecido.

**EX036.** Trinta dias.

**EX037.** Voltar em até quatro horas e perder no máximo uma hora de dados.

**EX038.** Seis horas.

**EX039.** Três horas.

**EX040.** Os formulários de consentimento em papel.

**EX041.** Por um único número de telefone ou endereço de e-mail.

**EX042.** Responder e Recuperar.

**EX043.** O encarregado de proteção de dados.

**EX044.** O contrato do fornecedor não exigia a notificação imediata de incidentes.

**EX045.** A expiração das contas dos substitutos.

**EX046.** Seis medidas.

**EX047.** As conexões bloqueadas.

**EX048.** Duas páginas.

**EX049.** Pressionar o fornecedor em conjunto com outros grupos odontológicos.

**EX050.** Interromper as medidas que nunca mudam as decisões.

**EX051.** Ransomware, o risco mais bem classificado pelo conselho.

**EX052.** Pelo menos noventa por cento em cada clínica.

**EX053.** O critério de conformidade com as correções por clínica.

**EX054.** Três horas e dez minutos.

**EX055.** Um teste independente da resposta a incidentes.

**EX056.** Clínicas capazes de atender os pacientes e prontuários dos pacientes protegidos.

**EX057.** O prestador de backup.

**EX058.** A aprovação com distinção.

**EX059.** Suas medidas como relatório trimestral permanente.

**EX060.** Grandes seguradoras começaram a solicitá-la.

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
