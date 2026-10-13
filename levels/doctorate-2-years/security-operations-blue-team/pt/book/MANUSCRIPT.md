# Operações de Segurança e Blue Team: Trilha de Pesquisa de Doutorado

- Idioma: português do Brasil (`pt`); curso 199, trilha de pesquisa de doutorado (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–8 de 8 têm texto didático escrito à mão; os exercícios EX001–EX050 têm resoluções correspondentes com rubricas de 0 a 3; quatro laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre evidências sintéticas, e suas saídas foram incorporadas a partir de execuções reais. A revisão independente e a verificação de 300 páginas A4 continuam em aberto.
- Público: doutorandos que vão produzir pesquisa original e reprodutível sobre operações de segurança, qualidade de alertas e tomada de decisão de analistas.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite ético e legal: monitore e responda apenas em sistemas que você está autorizado a defender; nada de código de exploração, *payloads*, procedimentos de ataque ou instruções para escapar da detecção. As detecções são ensinadas do lado do defensor, com telemetria sintética. Todas as evidências, pessoas e organizações são **sintéticas**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia em ordem: os capítulos acompanham um único projeto de doutorado sobre triagem de alertas enriquecidos com contexto, da integridade na pesquisa à defesa. Execute cada laboratório onde ele aparece, tente os exercícios antes das resoluções e pontue-se com as rubricas.

### Caso contínuo sintético

| Elemento | Papel | Limite |
|---|---|---|
| **Nadia Ferreira** | Doutoranda | Inventada |
| **Prof. Elias Grant** | Orientador | Inventado |
| **Calder University** | Universidade fictícia | Inventada |
| **Northgate Shared SOC** | SOC parceiro fictício | Inventado |
| **Ruth Okonkwo** | Gerente do SOC | Inventada |

### Fontes principais

NIST [SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92), [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137) e [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE D3FEND](https://d3fend.mitre.org/); [Sigma](https://github.com/SigmaHQ/sigma); Knerler, Parker e Zimmerman, *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE, 2022). Lista completa em [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Integridade e métodos avançados de pesquisa

### Objetivos de aprendizagem

Você vai (1) aplicar princípios de integridade na pesquisa à pesquisa em operações de segurança; (2) separar qualidade de detecção, qualidade de triagem e resultado operacional como construtos distintos; (3) planejar estudos que usem dados operacionais sintéticos ou consentidos; (4) pré-registrar hipóteses, medidas e análise.

### 1.1 Por que a integridade importa na pesquisa sobre SOC

A pesquisa sobre SOC define como as organizações gastam o tempo escasso dos analistas. Um estudo que exagera o valor de um apoio à triagem pode levar um SOC a desligar alertas úteis ou a confiar numa ferramenta que deveria verificar. Vielberth et al. (2020), num estudo sistemático da literatura sobre SOC, encontraram uma área fragmentada e carente de avaliação empírica; Kokulu et al. (2019) mostraram, por meio de entrevistas, que gestores e analistas frequentemente discordam até sobre quais são os problemas do SOC. Um projeto de doutorado deve acrescentar evidências cuidadosas, não mais opinião.

### 1.2 Três construtos, mantidos separados

A **qualidade de detecção** pergunta se uma regra dispara na atividade que visa e fica em silêncio nos demais casos (precisão, *recall*). A **qualidade de triagem** pergunta se um analista, diante de um alerta, chega à disposição correta (acurácia, tempo, concordância). O **resultado operacional** pergunta se os incidentes são contidos mais cedo ou com menos dano. Um estudo pode melhorar um enquanto piora outro; as afirmações devem dizer qual construto foi medido. A tese de Nadia mede apenas a qualidade de triagem. Seus alertas sintéticos têm rótulos conhecidos, então a acurácia pode ser pontuada com exatidão, mas nada no desenho mostra se a Northgate conteria incidentes mais rápido. O capítulo de conclusão mantém esse limite.

### 1.3 Dados para pesquisa

Dados reais de SOC contêm dados pessoais, segredos de negócio e evidências de incidentes em andamento. Raramente podem ser compartilhados e podem não ter consentimento para pesquisa. Conjuntos sintéticos de alertas com verdade de referência conhecida permitem pontuação exata e publicação aberta. Quando dados operacionais são necessários, eles são usados sob um acordo de compartilhamento de dados, minimizados e pseudonimizados, com aprovação ética. O corpus de Nadia é sintético por esses motivos: a Northgate atende vários municípios, e seus alertas reais incluiriam dados de moradores e funcionários. Os únicos dados operacionais do estudo são os próprios logs de triagem dos analistas, coletados com consentimento e anonimizados antes da análise, com aprovação ética da Calder University.

### 1.4 Pré-registro

Antes do estudo principal, a candidata registra hipóteses, medidas primárias e secundárias, a justificativa do tamanho da amostra, o plano de análise e as regras de exclusão. Mudanças posteriores são permitidas, mas registradas com seus motivos, para que os leitores distingam resultados planejados de exploratórios. Nadia registra a acurácia como medida primária e o tempo até a disposição como secundária, com a análise pareada e a regra de exclusão para sessões incompletas. Seu registro de mudanças, que começa na versão 1.1 depois do piloto, documenta cada mudança posterior, para que os leitores vejam que mover os campos de contexto para o topo do cartão aconteceu antes do estudo principal, e não depois de os resultados serem conhecidos.

### 1.5 Interesses e ferramentas

Fornecedores podem financiar estudos sobre SOC ou fornecer ferramentas. Financiamento, relações e versões de ferramentas são declarados. Um estudo que testa um produto não pode deixar o fornecedor aprovar as conclusões. O estudo de Nadia não usa nenhum produto de fornecedor; os cartões de alerta são de autoria dela, e as regras são escritas no formato aberto Sigma. Ainda assim, ela registra a versão do Python usada para gerar os alertas e pontuar as decisões, e o formulário de declaração da Calder afirma que a Northgate não recebe pagamento nem benefício de produto pelo estudo. A tese lista essas declarações nos elementos pré-textuais, para que os examinadores as vejam antes dos resultados.

### 1.6 Ética com analistas como participantes

Quando analistas são participantes, seus dados de desempenho podem afetar carreiras. O consentimento é voluntário, os gestores não veem pontuações individuais e os participantes podem desistir. Na Northgate, Ruth Okonkwo aprovou a participação no horário de trabalho, mas concordou por escrito em não ver as pontuações individuais de acurácia. Os analistas recebem IDs aleatórios antes das sessões, e os resultados são relatados apenas de forma agregada. Um analista que desiste pode ter seus logs removidos até o momento da análise, e o termo de consentimento informa essa data. Nadia também prometeu apresentar os resultados primeiro aos analistas.

### Exemplo resolvido

**Nadia Ferreira**, doutoranda na fictícia **Calder University** sob orientação do **Prof. Elias Grant**, esboça o objetivo "alertas enriquecidos com contexto tornam os analistas melhores". Grant pergunta: melhores em quê, medidos como, contra que verdade, com que incerteza? Nadia reescreve: "Estimar a diferença na acurácia de triagem e na mediana do tempo até a disposição entre cartões de alerta de linha de base e cartões enriquecidos com contexto, em 160 alertas sintéticos com rótulos conhecidos, relatando intervalos de 95%."

> **Caso sintético.** A Calder University, Nadia, o Prof. Grant e todos os dados são inventados.

### Erros e limites

Alertas sintéticos simplificam as operações reais. Os resultados só se transferem na medida em que o conjunto de alertas se pareça com a mistura de um SOC real; a tese deve dizer quais características não foram modeladas.

### Exercícios

- **EX001 — Três construtos.** Diferencie qualidade de detecção, qualidade de triagem e resultado operacional. *Rubrica:* 3 = os três com uma medida cada; 2 = dois; 1 = um; 0 = nada.
- **EX002 — A lacuna da área.** O que Vielberth et al. (2020) relataram sobre a pesquisa em SOC? *Rubrica:* 3 = fragmentada, carente de avaliação empírica; 2 = parcial; 1 = vago; 0 = nada.
- **EX003 — Perspectivas diferentes.** O que Kokulu et al. (2019) constataram sobre gestores e analistas? *Rubrica:* 3 = frequentemente discordam sobre os problemas do SOC; 2 = parcial; 1 = vago; 0 = nada.
- **EX004 — Reescrever o objetivo.** Transforme "alertas enriquecidos tornam os analistas melhores" num objetivo testável. *Rubrica:* 3 = medidas, condições, verdade de referência, incerteza; 2 = três; 1 = vago; 0 = nada.
- **EX005 — Conteúdo do pré-registro.** Cite cinco coisas registradas antes do estudo principal. *Rubrica:* 3 = hipóteses, medidas, justificativa do tamanho da amostra, análise, exclusões; 2 = três; 1 = uma; 0 = nada.
- **EX006 — Proteção dos participantes.** Como os analistas participantes são protegidos? *Rubrica:* 3 = consentimento voluntário, nenhuma pontuação individual para gestores, desistência; 2 = duas; 1 = uma; 0 = nada.
- **EX007 — Limite do sintético.** Indique o principal limite dos conjuntos sintéticos de alertas. *Rubrica:* 3 = só se transferem na medida em que a mistura se pareça com a realidade; dizer o que falta; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

A pesquisa sobre SOC deve nomear o construto medido, usar dados compartilháveis ou devidamente governados, pré-registrar e proteger os participantes.

### Continue estudando — capítulo 01 de 08

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 (rascunho) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Operações de segurança e blue team: fronteira da pesquisa

### Objetivos de aprendizagem

Você vai (1) mapear problemas em aberto na pesquisa sobre operações de segurança; (2) explicar o problema da taxa de base para alertas; (3) relacionar a pesquisa sobre fadiga de alertas ao desenho da triagem; (4) posicionar uma tese na fronteira.

### 2.1 O problema da taxa de base

Axelsson (2000) mostrou que, como as intrusões genuínas são raras entre os eventos que um detector vê, até uma pequena taxa de falsos positivos produz, em sua maioria, alarmes falsos. A precisão depende da prevalência, e não só do detector. Para o estudo de Nadia, o argumento da taxa de base é a motivação: se as regras disparam principalmente em atividade benigna, a decisão do analista na triagem determina se um SOC é útil. Por isso, o experimento dela mede o que acontece nessa segunda etapa, em que os alertas que a detecção não conseguiu filtrar precisam ser separados por pessoas.

### Laboratório — precisão sob diferentes taxas de base

```python
"""Base-rate effect on alert precision (Axelsson 2000), synthetic figures."""
def ppv(tpr, fpr, prevalence):
    tp = tpr * prevalence
    fp = fpr * (1 - prevalence)
    return tp / (tp + fp)
for prev in (1e-2, 1e-3, 1e-4):
    for fpr in (1e-2, 1e-3):
        print(f"prevalence={prev:.0e} TPR=0.95 FPR={fpr:.0e} -> precision={ppv(0.95, fpr, prev):.3f}")
```

Execute com `python3 lab_baserate.py`. Saída verificada:

```text
prevalence=1e-02 TPR=0.95 FPR=1e-02 -> precision=0.490
prevalence=1e-02 TPR=0.95 FPR=1e-03 -> precision=0.906
prevalence=1e-03 TPR=0.95 FPR=1e-02 -> precision=0.087
prevalence=1e-03 TPR=0.95 FPR=1e-03 -> precision=0.487
prevalence=1e-04 TPR=0.95 FPR=1e-02 -> precision=0.009
prevalence=1e-04 TPR=0.95 FPR=1e-03 -> precision=0.087
```

### 2.2 Ler o resultado

Com taxa de verdadeiros positivos de 95% e taxa de falsos positivos de 1%, a precisão é 0.490 com prevalência de um em cem, 0.087 com um em mil e 0.009 com um em dez mil. Reduzir a taxa de falsos positivos para 0,1% eleva o caso de um em mil apenas a 0.487. A detecção de eventos raros precisa de taxas de falsos positivos muito baixas ou de uma segunda etapa, como a triagem por analistas, para ser útil. Nadia usa o laboratório para calibrar as expectativas sobre o corpus. Como os fluxos reais de alertas são dominados por disparos benignos, o corpus inclui muitos deles de propósito, para que as decisões de triagem sejam testadas nos alertas que os analistas mais veem.

### 2.3 Fadiga de alertas

Alahmadi, Axon e Martinovic (2022) entrevistaram profissionais de SOC e constataram que muitos alarmes chamados de "falsos positivos" são disparos benignos: a regra casou com um comportamento real que era legítimo naquele contexto. Eles propõem que os alarmes sejam confiáveis, explicáveis, analíticos, contextuais e transferíveis (*Reliable, Explainable, Analytical, Contextual, Transferable*). Hassan et al. (2019) usaram grafos de proveniência para ordenar alertas e reduzir a fadiga. A constatação sobre disparos benignos é o ponto de partida do projeto de Nadia: se muitos alarmes são correspondências corretas com atividade legítima, os analistas precisam de contexto para reconhecer rapidamente a legitimidade. Os cartões enriquecidos dela testam diretamente a propriedade contextual. Métodos de ordenação como o de Hassan et al. reduzem quantos alertas chegam aos analistas, o que complementa a pergunta dela em vez de concorrer com ela.

### 2.4 Cautela com aprendizado de máquina

Sommer e Paxson (2010) argumentaram que a detecção de anomalias se ajusta mal a mundos fechados: os ataques são raros, a variedade benigna é enorme e os erros custam caro para explicar. A crítica deles ainda orienta como o trabalho de fronteira deve ser avaliado. O estudo de Nadia evita totalmente a detecção de anomalias; suas regras são condições Sigma explícitas. Mesmo assim, a crítica molda o desenho, porque alerta que um método avaliado em dados convenientes pode falhar em operação. É por isso que ela relata o realismo como limitação e planeja um piloto operacional como o teste capaz de refutar sua afirmação.

### 2.5 Fatores humanos e organizacionais

Sundaramurthy et al. (2014) inseriram pesquisadores em SOCs e constataram que o conhecimento tácito e o atrito com as ferramentas eram centrais. Kokulu et al. (2019) enfatizaram os desencontros entre as métricas da gestão e a realidade dos analistas. Esses estudos lembram a Nadia que a triagem acontece dentro de uma organização, com hábitos e ferramentas que uma sessão de laboratório elimina. O piloto dela encontrou exatamente esse tipo de atrito: os analistas não viam um campo colocado na parte de baixo do cartão. O comentário posterior de um analista sênior, de que faltava a linha de comando bruta, veio do mesmo tipo de conhecimento tácito.

### 2.6 A posição de Nadia

A tese de Nadia fica entre a detecção e a triagem: ela testa se acrescentar contexto aos alertas, como sugere a propriedade "contextual", melhora as decisões dos analistas sobre disparos benignos sem esconder ataques verdadeiros. A posição torna a afirmação específica. Ela não testa se o contexto melhora a detecção, nem se encurta os incidentes; testa se os analistas que veem o contexto chegam à disposição correta com mais frequência. Sua preocupação desde o início era a segunda metade da frase: que o contexto também pudesse levar os analistas a descartar um ataque verdadeiro, e é por isso que os danos são medidos junto com a acurácia.

### Exemplo resolvido

O mapa da literatura de Nadia tem três colunas — trabalhos no nível do detector, no nível do alerta e no nível do analista — e situa o estudo dela na coluna do nível do alerta, citando Alahmadi et al. como motivação e Axelsson para explicar por que a triagem, e não só a detecção, determina a utilidade.

> **Caso sintético.** Os números vêm do script do laboratório.

### Erros e limites

As afirmações de fronteira envelhecem rápido; Nadia data sua revisão e registra os termos de busca para que ela possa ser atualizada.

### Exercícios

- **EX008 — Enunciado da taxa de base.** Enuncie numa frase o argumento de Axelsson sobre a taxa de base. *Rubrica:* 3 = intrusões raras fazem até uma FPR baixa gerar majoritariamente alarmes falsos; 2 = parcial; 1 = vago; 0 = nada.
- **EX009 — Leitura do laboratório.** Dê a precisão com prevalência 1e-3 para FPR 1e-2 e 1e-3. *Rubrica:* 3 = 0.087 e 0.487; 2 = um; 1 = errado; 0 = nada.
- **EX010 — Disparos benignos.** Em que os disparos benignos diferem dos falsos positivos? *Rubrica:* 3 = a regra casou com um comportamento real, mas legítimo; 2 = parcial; 1 = são iguais; 0 = nada.
- **EX011 — Propriedades REACT.** Liste as cinco propriedades de alarme propostas por Alahmadi et al. *Rubrica:* 3 = Reliable, Explainable, Analytical, Contextual, Transferable; 2 = três; 1 = uma; 0 = nada.
- **EX012 — Crítica do mundo fechado.** Resuma a cautela de Sommer e Paxson. *Rubrica:* 3 = ataques raros, enorme variedade benigna, erros caros de explicar; 2 = dois; 1 = um; 0 = nada.
- **EX013 — Posição da tese.** Onde fica a tese de Nadia, e por quê? *Rubrica:* 3 = nível do alerta/triagem; testa a propriedade contextual em disparos benignos sem esconder ataques; 2 = parcial; 1 = detector; 0 = nada.
- **EX014 — Atualizar revisões.** Como Nadia mantém sua revisão atualizável? *Rubrica:* 3 = data a revisão e registra os termos de busca; 2 = um; 1 = vago; 0 = nada.

### Síntese

A fronteira é moldada pelas taxas de base, pela qualidade dos alarmes e pelos fatores humanos; uma tese precisa se situar com precisão entre eles.

### Continue estudando — capítulo 02 de 08

[← Capítulo 01 (rascunho)](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 (rascunho) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Proposta de contribuição original

### Objetivos de aprendizagem

Você vai (1) enunciar com precisão uma contribuição original; (2) separar a contribuição do trabalho que a sustenta; (3) avaliar condições de detecção contra eventos sintéticos rotulados; (4) defender a novidade e a viabilidade da proposta.

### 3.1 O que conta como original

Uma contribuição original acrescenta conhecimento que outros podem usar e testar: um método validado, um efeito medido, um conjunto de dados reutilizável. Nadia propõe três itens: um corpus sintético rotulado de alertas com disparos benignos; um experimento controlado sobre enriquecimento com contexto; e uma análise de onde o enriquecimento falha. Cada item pode ser verificado separadamente por outros. O corpus pode ser reutilizado em experimentos diferentes; o efeito medido pode ser contestado com a repetição do estudo; e a análise de falhas dá aos projetistas casos concretos. A declaração de contribuição de Nadia nomeia os três itens para que os examinadores julguem cada um diante de sua evidência.

### 3.2 Trabalho de sustentação

As regras de detecção precisam ser boas o bastante para que a triagem, e não a detecção, seja o gargalo do experimento. Nadia avalia as regras candidatas em eventos sintéticos rotulados antes de montar os cartões de alerta. As regras são escritas no formato Sigma, do SigmaHQ, para que outros possam lê-las de forma neutra em relação a fornecedores. A avaliação das regras é trabalho de sustentação, não uma contribuição em si. Seu propósito é garantir que os alertas do experimento venham de regras plausíveis, incluindo uma que dispara em atividade benigna, para que as decisões de triagem sejam testadas em material realista.

### Laboratório — reprodução de condições de detecção

```python
"""Replay a Sigma-style detection condition over synthetic labelled events."""
events = [  # (process, parent, cmdline_has_encoded, label)
    ("powershell.exe", "winword.exe", True, "attack"),
    ("powershell.exe", "explorer.exe", False, "benign"),
    ("powershell.exe", "sccm_agent.exe", True, "benign"),
    ("powershell.exe", "excel.exe", True, "attack"),
    ("cmd.exe", "winword.exe", False, "attack"),
    ("powershell.exe", "explorer.exe", True, "benign"),
    ("powershell.exe", "outlook.exe", True, "attack"),
    ("powershell.exe", "sccm_agent.exe", True, "benign"),
]
office = {"winword.exe", "excel.exe", "outlook.exe"}
def v1(p, par, enc): return p == "powershell.exe" and enc
def v2(p, par, enc): return p in {"powershell.exe", "cmd.exe"} and par in office
for name, rule in (("v1 encoded-only", v1), ("v2 office-parent", v2)):
    tp = sum(rule(p, q, e) and l == "attack" for p, q, e, l in events)
    fp = sum(rule(p, q, e) and l == "benign" for p, q, e, l in events)
    fn = sum((not rule(p, q, e)) and l == "attack" for p, q, e, l in events)
    print(f"{name:17} TP={tp} FP={fp} FN={fn} precision={tp/(tp+fp):.2f} recall={tp/(tp+fn):.2f}")
```

Execute com `python3 lab_replay.py`. Saída verificada:

```text
v1 encoded-only   TP=3 FP=3 FN=1 precision=0.50 recall=0.75
v2 office-parent  TP=4 FP=0 FN=0 precision=1.00 recall=1.00
```

### 3.3 Ler o resultado

A condição v1 (linha de comando do PowerShell codificada) pega 3 de 4 ataques, mas também dispara em 3 eventos benignos — o agente de distribuição de software e um administrador —, com precisão de 0.50. A condição v2 (interpretador de scripts cujo processo pai é um aplicativo do Office) pega os 4 ataques sem nenhum alarme falso neste pequeno conjunto. Os disparos benignos de v1 são justamente o tipo de alerta que o contexto deveria ajudar os analistas a descartar, então Nadia mantém os alertas de v1 no corpus como material de triagem. Os dois resultados vêm de um pequeno conjunto rotulado, por isso Nadia não afirma que v2 seja uma regra melhor em geral; ela apenas verifica que cada regra se comporta como pretendido em eventos conhecidos. Os alertas do administrador e do agente de distribuição lhe dão disparos benignos cujo contexto, como o papel do usuário ou um histórico de fechamentos como benigno, é exatamente o que os cartões enriquecidos exibem.

### 3.4 Novidade

A revisão dela mostra que trabalhos anteriores mediram as percepções dos analistas (Alahmadi et al., 2022) e a ordenação automatizada (Hassan et al., 2019), mas há poucos experimentos controlados sobre contexto em cartões de alerta com verdade de referência conhecida. A lacuna é estreita, mas real: os profissionais relatam que o contexto ajuda, e os sistemas de ordenação reduzem o volume, mas poucos estudos medem se mostrar o contexto muda as decisões dos analistas sobre alertas de verdade conhecida. O mapa da literatura de Nadia sustenta essa afirmação, e ela guarda o registro da busca para que os examinadores possam conferi-lo. A busca abrangeu veículos de segurança e de fatores humanos, porque estudos sobre decisões de analistas costumam ser publicados fora das conferências de segurança.

### 3.5 Viabilidade

Oito analistas do fictício **Northgate Shared SOC**, que atende vários municípios, concordam em participar no horário de trabalho, com a aprovação da gerente **Ruth Okonkwo**; o corpus é sintético; o estudo cabe em dois semestres. Realizar as sessões no horário de trabalho, com a aprovação da gerente, evita pedir aos analistas que abram mão do próprio tempo, mas também significa que incidentes urgentes podem interromper uma sessão. O protocolo permite pausar e retomar uma sessão, com a pausa registrada. Dois semestres comportam o piloto, o estudo principal e a análise com alguma folga.

### 3.6 Riscos

O recrutamento pode ficar aquém do previsto; os analistas podem reconhecer padrões sintéticos. Mitigações: um grupo de reserva de um segundo SOC; revisão de realismo por dois analistas seniores. Reconhecer padrões sintéticos poderia inflar a acurácia nas duas condições, o que estreitaria qualquer diferença. A revisão de realismo verifica o corpus antes do estudo principal; o grupo de reserva do segundo SOC só é contatado se os voluntários da Northgate ficarem abaixo de oito. As duas mitigações constam da proposta com seus responsáveis. Nadia revisa a lista de riscos com o Prof. Grant todo mês até o fim do estudo principal.

### Exemplo resolvido

Declaração de contribuição de Nadia: "C1: um corpus sintético de alertas sob licença aberta, com 320 alertas, rótulos e anotações de disparos benignos. C2: um experimento cruzado que estima o efeito do enriquecimento com contexto sobre a acurácia e o tempo de triagem. C3: uma análise de falhas dos alertas em que o enriquecimento induziu os analistas ao erro."

> **Caso sintético.** Os eventos e as regras vêm do script do laboratório; a Northgate é inventada.

### Erros e limites

Oito eventos não validam uma regra; o laboratório mostra o método, não a qualidade da regra.

### Exercícios

- **EX015 — Lista de contribuições.** Enuncie as três contribuições de Nadia. *Rubrica:* 3 = corpus, experimento cruzado, análise de falhas; 2 = duas; 1 = uma; 0 = nada.
- **EX016 — Por que testar as regras primeiro.** Por que a detecção precisa ser avaliada antes do experimento de triagem? *Rubrica:* 3 = a triagem precisa ser o gargalo estudado; 2 = parcial; 1 = sem motivo; 0 = nada.
- **EX017 — Resultado da reprodução.** Dê a precisão e o *recall* de v1 e v2. *Rubrica:* 3 = v1 0.50/0.75, v2 1.00/1.00; 2 = uma regra; 1 = errado; 0 = nada.
- **EX018 — Manter os alertas de v1.** Por que manter no corpus os disparos benignos de v1? *Rubrica:* 3 = são material de triagem realista que o contexto deveria ajudar a descartar; 2 = parcial; 1 = engano; 0 = nada.
- **EX019 — Lacuna de novidade.** Que lacuna estabelece a novidade? *Rubrica:* 3 = poucos experimentos controlados sobre contexto em alertas com verdade de referência; 2 = parcial; 1 = vago; 0 = nada.
- **EX020 — Amostra pequena.** O que a reprodução com oito eventos não mostra? *Rubrica:* 3 = a validade da regra; ela só ilustra o método; 2 = parcial; 1 = prova a regra; 0 = nada.

### Síntese

Enuncie as contribuições com precisão, adeque o trabalho de sustentação ao seu propósito e mostre novidade e viabilidade com evidências.

### Continue estudando — capítulo 03 de 08

[← Capítulo 02 (rascunho)](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 (rascunho) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Replicação da linha de base e piloto

### Objetivos de aprendizagem

Você vai (1) replicar uma linha de base antes de testar uma intervenção; (2) medir a confiabilidade entre avaliadores dos rótulos de verdade de referência; (3) realizar um piloto para testar procedimentos; (4) revisar o protocolo a partir das evidências do piloto.

### 4.1 Por que replicar uma linha de base

Antes de afirmar que o enriquecimento ajuda, Nadia precisa mostrar que seu arranjo reproduz um comportamento conhecido: os analistas na condição de linha de base devem mostrar acurácia e confusão com disparos benignos semelhantes às que os profissionais relatam. Se a linha de base for estranha, a comparação não tem sentido. A verificação de Nadia é que os analistas da linha de base confundam disparos benignos com ataques numa taxa semelhante à descrita pelos profissionais. Se a acurácia da linha de base fosse quase perfeita, o enriquecimento não teria o que melhorar e o corpus seria fácil demais. Os resultados do piloto e da linha de base são comparados com os relatos de disparos benignos da literatura antes da análise principal.

### 4.2 Rótulos de verdade de referência

Os rótulos do corpus são escritos por Nadia quando ela gera os alertas, mas "malicioso" versus "benigno" pode ser discutível em casos limítrofes. Dois analistas seniores rotulam de forma independente 20 alertas de amostra para testar se os rótulos são claros. Se os dois analistas seniores discordarem com frequência, a própria verdade de referência é pouco clara e a acurácia não pode ser pontuada de forma justa. Os 20 alertas são sorteados de modo a incluir casos limítrofes, não só os óbvios, para que o teste seja exigente. Os analistas seniores não participam do estudo principal.

### Laboratório — concordância nos rótulos

```python
"""Cohen's kappa for two analysts labelling the same 20 synthetic alerts."""
from collections import Counter
a = "MMBBBMBBBBMBBBBBMBBB"   # M = malicious, B = benign (analyst A)
b = "MMBBBBBBBBMBBBMBMBBB"   # analyst B
n = len(a)
po = sum(x == y for x, y in zip(a, b)) / n
ca, cb = Counter(a), Counter(b)
pe = sum(ca[k] * cb[k] for k in "MB") / n**2
kappa = (po - pe) / (1 - pe)
print(f"n={n} observed agreement={po:.2f} chance={pe:.3f} kappa={kappa:.2f}")
```

Execute com `python3 lab_kappa.py`. Saída verificada:

```text
n=20 observed agreement=0.90 chance=0.625 kappa=0.73
```

### 4.3 Ler o resultado

Os dois analistas concordam em 18 de 20 alertas (0.90). A concordância ao acaso, dada a frequência com que cada um diz "malicioso", é 0.625, então o kappa de Cohen é 0.73 — "substancial" na escala de Landis e Koch (1977). As duas discordâncias são discutidas; um rótulo é corrigido e um alerta é reescrito para eliminar a ambiguidade. O kappa é menor do que a concordância bruta porque os dois analistas classificaram a maioria dos alertas como benignos, o que torna alta a concordância ao acaso. O rótulo corrigido e o alerta reescrito ficam no registro de mudanças, incluindo o alerta 17. Com essas correções, Nadia considera os rótulos do corpus confiáveis o bastante para pontuar o estudo principal.

### 4.4 O piloto

Dois analistas voluntários que não participam do estudo principal fazem a triagem de 40 alertas, 20 em cada condição. O piloto verifica o tempo, as instruções, o leiaute do cartão de alerta e o registro em log. Os analistas do piloto usam os mesmos cartões e instruções do estudo principal, então qualquer problema que encontrem também afetaria as sessões principais. Depois, eles são questionados sobre o que os confundiu, e Nadia observa uma sessão para ver onde hesitam. Seus logs são guardados à parte e não entram em nenhum efeito relatado. Os analistas do piloto também cronometram cada sessão, e foi assim que se descobriu a duração de 70 minutos para 40 alertas.

### 4.5 O que o piloto encontrou

Os analistas não notaram o campo de criticidade do ativo porque ele ficava na parte de baixo do cartão; o log não registrava as mudanças de disposição; 40 alertas levaram 70 minutos, causando fadiga. Nadia move os campos de contexto para perto do topo, corrige o log e divide os 40 alertas em duas sessões de 20 com um intervalo de 15 minutos. Cada mudança consta do registro de mudanças v1.1 antes do início do estudo principal. A constatação sobre a fadiga importa para a validade: analistas cansados erram mais no fim de uma sessão, o que poderia enviesar a condição que viesse em segundo lugar.

### 4.6 Dados do piloto

Os resultados do piloto não são usados para estimar efeitos; eles testam o procedimento. Isso consta do registro. Usar os dados do piloto para estimativas misturaria o teste de procedimento com a medição de resultados, e os cartões do piloto diferiam dos finais depois da mudança de leiaute. Mantê-los separados significa que os resultados principais vêm apenas do desenho registrado. Ainda assim, Nadia relata o que o piloto revelou sobre o procedimento, porque isso explica por que os cartões finais têm a aparência que têm. O plano registrado afirma que os logs do piloto ficam fora de toda estimativa relatada, para que os examinadores possam conferir isso no arquivo.

### Exemplo resolvido

Registro de mudanças do protocolo de Nadia: "v1.1 — campos de contexto movidos para cima do evento bruto; registro de mudanças de disposição acrescentado; sessões divididas em 2 × 20 alertas com intervalo de 15 minutos; alerta 17 reescrito após discordância de rótulo."

> **Caso sintético.** Os rótulos vêm do script do laboratório.

### Erros e limites

O kappa depende da prevalência; com rótulos muito desbalanceados, uma concordância alta ainda pode gerar um kappa baixo.

### Exercícios

- **EX021 — Propósito da linha de base.** Por que replicar primeiro o comportamento da linha de base? *Rubrica:* 3 = uma linha de base estranha torna a comparação sem sentido; 2 = parcial; 1 = hábito; 0 = nada.
- **EX022 — Resultado do kappa.** Relate a concordância observada, a concordância ao acaso e o kappa. *Rubrica:* 3 = 0.90, 0.625, 0.73; 2 = dois; 1 = um; 0 = nada.
- **EX023 — Interpretar o kappa.** Como 0.73 é descrito na escala de Landis e Koch? *Rubrica:* 3 = substancial (0.61–0.80); 2 = só substancial; 1 = errado; 0 = nada.
- **EX024 — Discordâncias.** O que aconteceu com as duas discordâncias? *Rubrica:* 3 = discutidas; um rótulo corrigido, um alerta reescrito; 2 = parcial; 1 = ignoradas; 0 = nada.
- **EX025 — Constatações do piloto.** Cite três constatações do piloto e suas correções. *Rubrica:* 3 = posição do campo, log, fadiga, com as correções; 2 = duas; 1 = uma; 0 = nada.
- **EX026 — Ressalva do kappa.** Que ressalva se aplica ao kappa? *Rubrica:* 3 = efeito da prevalência; rótulos desbalanceados baixam o kappa apesar da concordância; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Replique a linha de base, verifique a confiabilidade dos rótulos, teste os procedimentos num piloto e revise com transparência antes do estudo principal.

### Continue estudando — capítulo 04 de 08

[← Capítulo 03 (rascunho)](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (rascunho) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Estudo principal e validação independente

### Objetivos de aprendizagem

Você vai (1) conduzir um estudo cruzado controlado; (2) estimar efeitos com intervalos; (3) providenciar a validação independente da análise; (4) relatar os efeitos com honestidade, incluindo os danos.

### 5.1 Desenho

Oito analistas fazem, cada um, a triagem de 40 alertas: 20 cartões de linha de base e 20 cartões enriquecidos, em ordem contrabalançada, com os conjuntos de alertas trocados entre as metades. Cada um dos 320 alertas do corpus é triado por exatamente um analista, então o estudo tem 320 decisões, 160 por condição. Os cartões enriquecidos acrescentam a criticidade do ativo, o papel do usuário e a contagem de alertas semelhantes fechados como benignos nos últimos 30 dias. O contrabalanceamento significa que metade dos analistas vê primeiro os cartões de linha de base e metade vê primeiro os enriquecidos, de modo que o aprendizado e a fadiga afetem igualmente as duas condições. Trocar os conjuntos de alertas entre as metades garante que as diferenças venham dos cartões, e não de alertas mais fáceis numa das condições. Os três campos enriquecidos foram escolhidos a partir da propriedade contextual e do que os analistas da Northgate disseram consultar com mais frequência.

### 5.2 Medida primária

Acurácia: a proporção de disposições que coincidem com a verdade de referência. Somando todos os analistas, cada condição tem 160 decisões sobre alertas (8 analistas × 20), e todas entram no intervalo registrado. A acurácia é pontuada contra os rótulos do corpus confirmados pelos analistas seniores. As decisões são registradas automaticamente, incluindo qualquer mudança de disposição antes do envio, de modo que a decisão final é a pontuada. O tempo até a disposição é registrado no mesmo log, mas tratado como secundário, conforme o registro. Um alerta só é pontuado como correto quando a disposição coincide exatamente com o rótulo; escalar um alerta benigno conta como erro, assim como fechar um ataque, porque ambos custam tempo ou segurança a um SOC.

### Laboratório — intervalos para a acurácia

```python
"""Wilson 95% intervals for triage accuracy in two synthetic conditions."""
import math
def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d
    h = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
for name, k, n in (("baseline", 118, 160), ("enriched", 139, 160)):
    lo, hi = wilson(k, n)
    print(f"{name:9} {k}/{n} = {k/n:.3f}  95% CI [{lo:.3f}, {hi:.3f}]")
```

Execute com `python3 lab_wilson.py`. Saída verificada:

```text
baseline  118/160 = 0.738  95% CI [0.664, 0.800]
enriched  139/160 = 0.869  95% CI [0.808, 0.913]
```

### 5.3 Ler o resultado

A acurácia da linha de base é 118/160 = 0.738 (IC de 95% 0.664–0.800); a dos cartões enriquecidos é 139/160 = 0.869 (0.808–0.913). Os intervalos por pouco não se sobrepõem (0.800 contra 0.808), e a diferença de 13 pontos é compatível com a hipótese. Como os mesmos analistas fizeram as duas condições, a análise pareada registrada é o teste principal; os intervalos de Wilson descrevem cada condição. Eles tratam as 160 decisões agregadas como independentes, embora cada analista contribua com 20 delas, então provavelmente são um pouco estreitos demais se os analistas diferirem em habilidade; é por isso que são apenas descritivos. Nadia relata o intervalo de cada condição e deixa a inferência principal para o teste pareado registrado. Os dois intervalos juntos mostram aos leitores a escala da mudança. Nenhum intervalo é usado sozinho para afirmar significância, já que intervalos sobrepostos ou separados não constituem um teste formal.

### 5.4 Danos

Das 21 decisões corretas adicionais, a maioria foi de disparos benignos fechados corretamente. Mas dois ataques verdadeiros foram fechados por engano na condição enriquecida, ambos com a nota "alertas semelhantes fechados como benignos: 14". O contexto de histórico pode adormecer a atenção dos analistas. Isso é relatado com destaque. Nadia relata os dois ataques perdidos no resumo, e não só nos resultados, porque quem for adotar cartões enriquecidos precisa saber deles. Ela examina os dois alertas em detalhe como parte da análise de falhas, e o campo de histórico se torna o foco do estudo complementar e da crítica que se seguiu.

### 5.5 Validação independente

Uma estatística de outra universidade refaz a análise a partir dos logs brutos e dos scripts de Nadia sem ver os resultados dela. Os números dela coincidem até a terceira casa decimal, o que também verifica que os scripts estão completos. A estatística recebeu o plano registrado e os logs anonimizados, não as tabelas de Nadia, então a concordância mostra que a análise decorre do plano e dos dados. O relatório de validação está no arquivo, com o nome e a universidade dela. O Prof. Grant indicou a estatística por meio da Calder University: alguém sem nenhuma participação no estudo nem na orientação de Nadia.

### 5.6 Tempo

A mediana do tempo até a disposição caiu de 96 para 81 segundos; a diferença de tempo é secundária e identificada como tal. Como o tempo foi registrado como secundário, Nadia não o testa como hipótese principal nem constrói afirmações sobre ele. Ela observa que decisões mais rápidas nos cartões enriquecidos são compatíveis com analistas usando o contexto para resolver rapidamente disparos benignos, mas a mesma rapidez pode ter contribuído para os dois ataques perdidos. Os dados de tempo são publicados com os logs para que outros os analisem. A comparação de tempo também é relatada por analista, para que os leitores vejam se a queda de 96 para 81 segundos veio de poucas pessoas.

### Desvios do plano

Um analista perdeu uma sessão por doença e a concluiu uma semana depois. O registro permitia isso; o desvio é relatado com a data.

### Exemplo resolvido

Parágrafo de resultados de Nadia: "Os cartões enriquecidos elevaram a acurácia de 0.738 para 0.869 (diferença pareada 0.131, IC de 95% conforme a análise registrada). Dois ataques verdadeiros foram fechados incorretamente na condição enriquecida, ambos exibindo uma alta contagem de histórico benigno; tratamos isso como um risco de desenho."

> **Caso sintético.** Os números vêm do script do laboratório.

### Erros e limites

Oito analistas de um único SOC limitam a generalização; os efeitos dos analistas podem predominar.

### Exercícios

- **EX027 — Desenho cruzado.** Descreva o desenho cruzado. *Rubrica:* 3 = cada analista nas duas condições, ordem contrabalançada, conjuntos trocados; 2 = parcial; 1 = dois grupos; 0 = nada.
- **EX028 — Campos de enriquecimento.** Que contexto os cartões enriquecidos acrescentaram? *Rubrica:* 3 = criticidade do ativo, papel do usuário, contagem de histórico benigno; 2 = dois; 1 = um; 0 = nada.
- **EX029 — Resultados dos intervalos.** Relate as duas acurácias com seus intervalos. *Rubrica:* 3 = 0.738 [0.664, 0.800]; 0.869 [0.808, 0.913]; 2 = só os valores; 1 = errado; 0 = nada.
- **EX030 — Análise pareada.** Por que a análise pareada é o teste principal? *Rubrica:* 3 = os mesmos analistas nas duas condições; 2 = parcial; 1 = sem motivo; 0 = nada.
- **EX031 — Dano encontrado.** Que dano o enriquecimento causou? *Rubrica:* 3 = dois ataques fechados com alta contagem de histórico benigno; 2 = parcial; 1 = vago; 0 = nada.
- **EX032 — Método de validação.** Como a análise foi validada de forma independente? *Rubrica:* 3 = estatística externa refez a partir dos logs brutos sem ver os resultados; coincidiu; 2 = parcial; 1 = autoverificação; 0 = nada.

### Síntese

Desenhos controlados, estimativas por intervalo, reanálise independente e relato honesto dos danos tornam um estudo principal crível.

### Continue estudando — capítulo 05 de 08

[← Capítulo 04 (rascunho)](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 (rascunho) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Crítica de pares e revisão

### Objetivos de aprendizagem

Você vai (1) buscar e receber crítica estruturada; (2) classificar as críticas por gravidade; (3) revisar afirmações, análises e texto em resposta; (4) documentar as respostas com transparência.

### 6.1 Fontes de crítica

A banca de Nadia, um examinador externo em formação, os analistas seniores da Northgate e os revisores anônimos de um artigo para um *workshop* leem o rascunho. Cada um vê fraquezas diferentes. Cada fonte olha a tese de um jeito: a banca, o método; o examinador em formação, a estrutura; os analistas seniores, o realismo; e os revisores do *workshop*, a afirmação. Nadia registra cada comentário numa única tabela, com sua fonte, para que nenhum se perca entre as versões. A tabela também registra em que versão cada mudança entrou e se o autor do comentário viu o texto revisado, para que o Prof. Grant possa verificar que cada fonte teve a chance de responder às mudanças de Nadia.

### 6.2 As principais críticas

Revisor 1: "O corpus é sintético; os disparos benignos em SOCs reais são mais confusos." Revisor 2: "O campo de histórico benigno pode estar fazendo todo o trabalho; você não consegue separar os três campos." Revisor 3: "Dois ataques perdidos são uma questão de segurança, não uma nota de rodapé." Um analista sênior: "Seus cartões de alerta não têm a linha de comando bruta, que é a primeira coisa que sempre olhamos." O comentário do analista mostra como a prática pode ver o que os pesquisadores deixam passar: os cartões foram desenhados a partir da propriedade contextual, mas os analistas trabalham a partir do evento bruto.

### 6.3 Classificar a gravidade

Nadia separa as críticas em: ameaça a validade (Revisor 2), muda as conclusões (Revisor 3), limita o escopo (Revisor 1), melhora o realismo (analista). As ameaças à validade são respondidas primeiro. Responder primeiro às ameaças à validade faz sentido porque elas poderiam mudar o que os dados significam. O ponto do Revisor 2 levou ao estudo complementar exploratório com cartões de campo único, enquanto o ponto do Revisor 3 mudou o destaque dado aos ataques perdidos. O comentário do analista levou à volta da linha de comando bruta em todos os cartões. O ponto do Revisor 1 virou um limite declarado de realismo, com um plano para um piloto operacional.

### 6.4 Respostas

Ao Revisor 2, ela responde com um estudo complementar exploratório com quatro analistas e cartões de campo único; o histórico, sozinho, produz a maior parte do ganho e os dois ataques perdidos — evidência de que o contexto de histórico é poderoso e arriscado. Ao Revisor 3, ela leva o dano para o resumo e recomenda mostrar o histórico apenas junto com um aviso de "por que ainda poderia ser malicioso". Ao Revisor 1, ela acrescenta uma seção de limites e publica o gerador para que outros possam testar o realismo. O ponto do analista é aceito para o próximo estudo.

### 6.5 A carta de resposta

Cada crítica é citada, seguida da mudança feita (com números de página) ou de uma discordância fundamentada. A carta de Nadia responde ao Revisor 2 descrevendo o estudo complementar e identificando seu resultado como exploratório, para que o revisor veja que a confusão de fatores foi tratada sem exageros. Quando discorda, como no pedido de abandonar de vez o corpus sintético, ela explica o porquê com evidências da revisão de realismo e dos limites éticos para dados reais de SOC. Cada mudança traz um número de página. O Prof. Grant lê a carta antes do envio, verificando que cada mudança alegada pode ser encontrada na página citada.

### 6.6 Evitar a revisão defensiva

Grant lembra a ela que a réplica sem mudança raramente convence; quando um revisor está errado, mostre a evidência. No caso do Revisor 3, a réplica teria significado argumentar que dois ataques em muitas decisões eram um número pequeno. Em vez disso, Nadia levou os ataques perdidos para o resumo e acrescentou uma recomendação de desenho, o que convenceu o revisor mais do que qualquer argumento conseguiria. O lembrete de Grant vale tanto para os instintos dela quanto para o tom dos revisores. A carta de resposta mostra a mudança para cada crítica aceita.

### Exemplo resolvido

Trecho da resposta: "R2.1 — Concordamos que os campos estão confundidos. Um estudo complementar (n = 4 analistas, 40 alertas cada) com cartões de campo único sugere que o campo de histórico benigno responde pela maior parte da melhora e pelos dois ataques perdidos (relatado no capítulo de crítica, identificado como exploratório)."

> **Caso sintético.** As críticas e o estudo complementar são inventados.

### Erros e limites

Um estudo complementar com quatro analistas é exploratório; orienta trabalhos futuros, mas não resolve a atribuição.

### Exercícios

- **EX033 — Classes de gravidade.** Cite as quatro classes de gravidade usadas. *Rubrica:* 3 = validade, conclusões, escopo, realismo; 2 = três; 1 = uma; 0 = nada.
- **EX034 — Campos confundidos.** Qual foi a crítica do Revisor 2, e como foi respondida? *Rubrica:* 3 = campos confundidos; estudo complementar de campo único, histórico produz o ganho e as perdas; 2 = parcial; 1 = ignorada; 0 = nada.
- **EX035 — Enquadramento de segurança.** Como a crítica sobre os ataques perdidos foi tratada? *Rubrica:* 3 = levada ao resumo; recomenda contra-aviso junto com o histórico; 2 = parcial; 1 = nota de rodapé; 0 = nada.
- **EX036 — Resposta sobre realismo.** O que respondeu à crítica do corpus sintético? *Rubrica:* 3 = seção de limites; publicação do gerador para testes; 2 = um; 1 = vago; 0 = nada.
- **EX037 — Formato da carta.** Descreva uma boa entrada de carta de resposta. *Rubrica:* 3 = citação, mudança com localização ou discordância fundamentada; 2 = parcial; 1 = só réplica; 0 = nada.
- **EX038 — Status do estudo complementar.** Por que o estudo complementar é identificado como exploratório? *Rubrica:* 3 = pequeno, não planejado para confirmação; não resolve a atribuição; 2 = parcial; 1 = confirmatório; 0 = nada.

### Síntese

Reúna críticas de muitas fontes, ordene-as pela ameaça à validade, revise com evidências e documente cada resposta.

### Continue estudando — capítulo 06 de 08

[← Capítulo 05 (rascunho)](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 (rascunho) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Síntese da tese e arquivo de reprodutibilidade

### Objetivos de aprendizagem

Você vai (1) sintetizar as constatações num argumento de tese coerente; (2) montar um arquivo de reprodutibilidade; (3) separar resultados confirmatórios e exploratórios; (4) indicar implicações para a prática e para a pesquisa.

### 7.1 O argumento

A tese argumenta: (1) os disparos benignos dominam a carga de trabalho dos analistas, em linha com Alahmadi et al. (2022); (2) o contexto nos cartões de alerta melhora a acurácia da triagem; (3) o contexto de histórico benigno traz um risco específico de descartar ataques verdadeiros; (4) o desenho dos alertas deve combinar o contexto com avisos de contraevidência. Cada passo se apoia num tipo diferente de evidência: o primeiro, na literatura; o segundo, no experimento registrado; o terceiro, na análise de falhas e no estudo complementar exploratório; e o quarto, no julgamento de Nadia a partir dos três. A tese identifica o quarto como uma recomendação, não como uma constatação.

### 7.2 Confirmatório versus exploratório

Os resultados dos capítulos recebem etiquetas: o efeito sobre a acurácia é confirmatório (registrado); a atribuição aos campos e o efeito sobre o tempo são exploratórios. As tabelas marcam cada um. As etiquetas dizem aos leitores quanto peso cada resultado aguenta. O efeito confirmatório sobre a acurácia foi testado conforme o registro; a atribuição ao campo de histórico benigno vem de um pequeno estudo complementar com quatro analistas e é uma pista, não uma conclusão. A tabela-resumo de Nadia repete cada etiqueta ao lado do arquivo do pacote que reproduz o resultado. O resultado de tempo traz uma etiqueta de secundário, em linha com a forma como foi registrado antes do estudo principal.

### 7.3 O arquivo

O arquivo contém: o gerador de alertas e sua semente; o corpus de 320 alertas com rótulos; as regras em formato Sigma usadas; os logs anonimizados dos analistas; os scripts de análise com versões fixadas; o pré-registro e o registro de mudanças; e um README que explica como refazer cada tabela. O arquivo permite que outro pesquisador regenere, a partir da semente, cada alerta, correspondência de regra, cartão e tabela. Os logs anonimizados substituem os registros brutos de triagem, como os termos de consentimento prometiam. O registro de mudanças e o pré-registro mostram aos leitores quais escolhas foram fixadas antes dos dados e quais vieram depois.

### 7.4 Testar o arquivo

Um colega de doutorado baixa o arquivo numa máquina limpa e regenera todas as tabelas, usando apenas as instruções do próprio arquivo. Dois números diferem na quarta casa decimal por causa de uma chamada de arredondamento; Nadia corrige o script e anota a correção. As diferenças eram pequenas, mas encontrá-las mostra que o teste verifica o próprio arquivo, e não a máquina de Nadia. Nadia registra a correção no registro de mudanças e marca uma nova versão do arquivo, e a segunda execução do colega na máquina limpa faz as saídas coincidirem exatamente.

### 7.5 Licenciamento e privacidade

O corpus e o código são publicados sob licença aberta. Os logs dos analistas são anonimizados: os IDs dos analistas são aleatórios, os horários são deslocados e as notas em texto livre são removidas depois de revisadas quanto a conteúdo identificador. Remover as notas em texto livre depois da revisão impede que os analistas sejam identificados pela escrita ou por detalhes do local de trabalho. Os horários deslocados mantêm as durações exatas enquanto escondem quando as sessões ocorreram. A licença aberta permite que outros pesquisadores reutilizem o corpus em experimentos diferentes com cartões de alerta, que é o propósito da primeira contribuição. O README do arquivo explica cada passo de anonimização, para que quem reutilizar saiba quais campos foram removidos e por quê.

### 7.6 Implicações

Para SOCs: testar os campos de enriquecimento um de cada vez e monitorar as taxas de ataques perdidos; campos de histórico precisam de salvaguardas. Para a pesquisa: experimentos no nível do campo e estudos de realismo sobre corpora. O SOC-CMM (van Os, 2016) oferece aos SOCs uma forma de situar essas mudanças dentro da maturidade de capacidades. As implicações seguem as evidências: os ataques perdidos sustentam o conselho sobre os campos de histórico, enquanto a atribuição exploratória sustenta testar os campos um de cada vez. Cada implicação da tese nomeia o resultado em que se apoia, para que o leitor possa segui-la até a evidência e sua etiqueta confirmatória ou exploratória antes de aplicá-la no próprio SOC.

### 7.7 Mapeamento para frameworks

As constatações são mapeadas para a função Detect (Detectar) do NIST CSF 2.0 (análise de eventos adversos), para que os profissionais possam localizá-las. Mapear o trabalho para a análise de eventos adversos permite que um gerente de SOC veja que as constatações tratam de como os alertas são avaliados depois da detecção, e não de como as regras são escritas. Nadia também aponta as atividades relacionadas de Respond (Responder), já que descartar um ataque verdadeiro na triagem atrasa todas as etapas seguintes do tratamento do incidente. O mapeamento aparece no artigo para profissionais e também na tese. A tese cita o NIST CSF 2.0 para o mapeamento, usando suas funções Detect e Respond pelo nome.

### Exemplo resolvido

A tabela-resumo da tese de Nadia lista cada afirmação, o capítulo de evidência, o status (confirmatório ou exploratório) e o arquivo do pacote que a reproduz.

> **Caso sintético.** O arquivo e o teste são inventados.

### Erros e limites

Os arquivos se degradam à medida que o software muda; versões fixadas e uma descrição de contêiner retardam, mas não impedem, essa degradação.

### Exercícios

- **EX039 — Quatro afirmações.** Enuncie as quatro afirmações da tese. *Rubrica:* 3 = disparos benignos dominam; o contexto ajuda; risco do histórico; combinar com contra-avisos; 2 = três; 1 = uma; 0 = nada.
- **EX040 — Etiquetas de status.** Quais resultados são confirmatórios e quais são exploratórios? *Rubrica:* 3 = acurácia confirmatória; atribuição e tempo exploratórios; 2 = parcial; 1 = todos confirmatórios; 0 = nada.
- **EX041 — Conteúdo do arquivo.** Liste seis itens do arquivo. *Rubrica:* 3 = seis entre gerador, corpus, regras, logs, scripts, registro, README; 2 = quatro; 1 = dois; 0 = nada.
- **EX042 — Teste do arquivo.** O que o teste na máquina limpa revelou? *Rubrica:* 3 = diferença de arredondamento na quarta casa decimal; corrigida e anotada; 2 = parcial; 1 = vago; 0 = nada.
- **EX043 — Anonimização dos logs.** Como os logs dos analistas foram anonimizados? *Rubrica:* 3 = IDs aleatórios, horários deslocados, texto livre removido; 2 = dois; 1 = um; 0 = nada.
- **EX044 — Implicação para a prática.** Dê uma implicação para SOCs. *Rubrica:* 3 = testar campos isoladamente, monitorar perdas, proteger campos de histórico; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Uma tese conquista confiança com um argumento claro, etiquetas de status honestas e um arquivo que outros conseguem de fato reexecutar.

### Continue estudando — capítulo 07 de 08

[← Capítulo 06 (rascunho)](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 (rascunho) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Plano de defesa e de publicação

### Objetivos de aprendizagem

Você vai (1) preparar-se para uma defesa de doutorado; (2) antecipar perguntas difíceis; (3) planejar a publicação de artigos, corpus e código; (4) planejar um engajamento responsável com os profissionais.

### 8.1 A defesa

A defesa testa se a candidata consegue explicar, justificar e delimitar o trabalho. Nadia prepara uma apresentação de 40 minutos: problema, desenho, resultados, dano, limites, contribuições. Nadia dá à constatação do dano um slide próprio, logo depois do resultado de acurácia, para que os examinadores vejam os dois juntos. Ela ensaia com o Prof. Grant e com uma colega que faz o papel do examinador externo, e guarda slides de reserva para o estudo complementar e o teste do arquivo. Nadia termina com os limites de um corpus sintético e o piloto operacional planejado, para que as perguntas dos examinadores partam do que o estudo não consegue mostrar.

### 8.2 Perguntas difíceis

Examinadores simulados perguntam: "Por que um SOC deveria confiar num corpus sintético?" "Um ganho de 13 pontos compensa os dois ataques perdidos?" "Os resultados se manteriam para analistas com dois meses de experiência?" "O que refutaria sua afirmação?" Nadia responde com evidências e admite onde não sabe. Suas respostas se apoiam na tese: a revisão de realismo para o corpus sintético, a análise de falhas para os ataques perdidos e o perfil dos participantes para a experiência dos analistas, que ela admite não estar coberta pela amostra. Para a pergunta sobre refutação, ela aponta um piloto operacional em pelo menos dois SOCs.

### 8.3 A pergunta do custo-benefício

Sobre os ataques perdidos, Nadia evita um simples sim. Ela explica que o valor depende das taxas de base e dos custos do SOC (Axelsson, 2000): se os disparos benignos consomem a maior parte do tempo dos analistas, o ganho libera capacidade para investigações mais profundas, mas só se as salvaguardas reduzirem as perdas causadas pelo histórico. Ela propõe medir os dois num piloto operacional. Sua resposta mantém os dois resultados numa só frase, como faz a evidência, e usa o mesmo raciocínio sobre taxas de base que motivou o projeto desde o início.

### 8.4 Plano de publicação

Artigo 1 (experimento e dano) para um veículo de segurança; artigo 2 (corpus e gerador) para uma trilha de conjuntos de dados; um artigo para gerentes de SOC. O corpus e o código são publicados com o primeiro artigo. Publicar o corpus com o primeiro artigo permite que os revisores verifiquem diretamente o material do experimento. O artigo de conjunto de dados descreve o gerador, os rótulos e as anotações de disparos benignos para que outros possam ampliá-los. O artigo para profissionais começa pela recomendação de salvaguardas para os campos de histórico e declara os limites de um corpus sintético.

### 8.5 Engajamento com os profissionais

Nadia apresenta os resultados primeiro aos analistas da Northgate, como prometido nos termos de consentimento, e oferece uma nota de desenho sobre cartões de alerta. Ela evita linguagem de marketing. Apresentar primeiro aos analistas da Northgate cumpre a promessa feita quando consentiram e permite que eles saibam dos ataques perdidos antes de qualquer outra pessoa. Ruth Okonkwo recebe os mesmos resultados agregados; nenhum desempenho individual de analista é mostrado. A nota de desenho propõe campos de contexto com avisos de contraevidência, em linha com a recomendação da tese. Os analistas podem comentar a nota antes que ela vá para Ruth.

### 8.6 Depois da defesa

As correções exigidas pelos examinadores são acompanhadas e concluídas antes da entrega final; o arquivo é atualizado com uma etiqueta de versão. Cada correção é listada com o comentário do examinador, a mudança e a página, e qualquer mudança que afete um número dispara uma nova execução a partir do arquivo. A etiqueta da versão final é citada na tese e nos artigos, para que todos os produtos apontem para o mesmo estado reprodutível do trabalho. O Prof. Grant aprova cada correção depois de conferi-la com a lista dos examinadores, e a tese final é depositada na Calder com o link do arquivo.

### 8.7 Alinhamento estratégico

A nota de desenho dela faz referência à Estratégia 8 de Knerler, Parker e Zimmerman (2022), "Leverage tools to support analyst workflow" (usar ferramentas para apoiar o fluxo de trabalho do analista), para conectar a pesquisa à linguagem de planejamento de SOC. A conexão permite que gerentes de SOC situem a recomendação dela dentro de um plano que talvez já usem, em vez de tratá-la como uma ideia de pesquisa isolada. Nadia toma cuidado para não afirmar que a estratégia é validada pelo estudo; ela a cita como linguagem de planejamento, enquanto sua evidência diz respeito a uma única escolha de desenho dentro dela. O artigo para profissionais cita a mesma estratégia, para que gerentes de SOC que leiam só o artigo vejam o mesmo limite da afirmação.

### Exemplo resolvido

Na defesa simulada, diante da pergunta "O que refutaria sua afirmação?", Nadia responde: "Um piloto operacional em que os cartões enriquecidos com salvaguardas não mostrassem ganho de acurácia, ou mostrassem uma taxa de ataques perdidos maior que a da linha de base, em pelo menos dois SOCs."

> **Caso sintético.** A defesa e os planos são inventados.

### Erros e limites

Os prazos de publicação dependem dos revisores; planeje ciclos de revisão.

### Exercícios

- **EX045 — Estrutura da apresentação.** Esboce a apresentação da defesa. *Rubrica:* 3 = problema, desenho, resultados, dano, limites, contribuições; 2 = quatro; 1 = dois; 0 = nada.
- **EX046 — Resposta de custo-benefício.** Como Nadia respondeu à pergunta ganho versus perdas? *Rubrica:* 3 = depende das taxas de base e dos custos; ganho de capacidade só com salvaguardas; piloto operacional; 2 = parcial; 1 = sim/não; 0 = nada.
- **EX047 — Refutação.** O que refutaria a afirmação? *Rubrica:* 3 = piloto operacional sem ganho ou com mais perdas em dois SOCs; 2 = parcial; 1 = vago; 0 = nada.
- **EX048 — Produtos de publicação.** Liste os produtos planejados. *Rubrica:* 3 = artigo do experimento, artigo do corpus, artigo para profissionais, publicação aberta; 2 = três; 1 = um; 0 = nada.
- **EX049 — Northgate primeiro.** Por que apresentar primeiro aos analistas da Northgate? *Rubrica:* 3 = prometido no consentimento; respeito aos participantes; 2 = parcial; 1 = marketing; 0 = nada.
- **EX050 — Vínculo com a estratégia.** Que estratégia da MITRE a nota de desenho citou, e por quê? *Rubrica:* 3 = Estratégia 8, ferramentas que apoiam o fluxo de trabalho do analista; conecta à linguagem de planejamento; 2 = número ou nome; 1 = errado; 0 = nada.

### Síntese

Uma defesa forte explica, justifica e delimita o trabalho; os planos de publicação e de engajamento honram os participantes e ajudam a prática.

### Continue estudando — capítulo 08 de 08

[← Capítulo 07 (rascunho)](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções ↓](#worked-results) · [Próximo curso pelo índice de capítulos →](../SUBJECTS.md)

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX050. Nadia Ferreira, o Prof. Elias Grant, a Calder University, o Northgate Shared SOC, Ruth Okonkwo e todos os números são sintéticos. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Qualidade de detecção é se uma regra dispara corretamente (precisão e *recall*); qualidade de triagem é se os analistas chegam às disposições corretas (acurácia, tempo, concordância); resultado operacional é se os incidentes terminam mais cedo ou com menos dano (por exemplo, o tempo até a contenção).

**EX002.** Que a pesquisa sobre SOC é fragmentada e tem pouca avaliação empírica.

**EX003.** Gestores e analistas frequentemente veem problemas diferentes como as principais questões do SOC.

**EX004.** "Estimar a diferença na acurácia de triagem e na mediana do tempo até a disposição entre cartões de alerta de linha de base e cartões enriquecidos, em 160 alertas sintéticos com rótulos conhecidos, com intervalos de 95%."

**EX005.** Hipóteses, medidas primárias e secundárias, a justificativa do tamanho da amostra, o plano de análise e as regras de exclusão.

**EX006.** A participação é voluntária, os gestores nunca veem resultados individuais e qualquer pessoa pode desistir.

**EX007.** As constatações só se transferem na medida em que a mistura sintética se pareça com o tráfego real de alertas, então a tese precisa listar as características que deixou de fora.

**EX008.** Como as intrusões reais são raras entre os eventos, até uma taxa minúscula de falsos positivos faz com que a maioria dos alertas seja falsa.

**EX009.** 0.087 com taxa de falsos positivos de 1% e 0.487 com 0,1%.

**EX010.** Um disparo benigno é uma correspondência correta com um comportamento real que, no contexto, é legítimo; um falso positivo, em sentido estrito, é uma correspondência com um comportamento que a regra não pretendia pegar.

**EX011.** Reliable, Explainable, Analytical, Contextual e Transferable (confiável, explicável, analítico, contextual e transferível).

**EX012.** Os ataques são raros, o comportamento normal é extremamente variado e os erros custam caro para explicar, então a detecção de anomalias se ajusta mal sem uma avaliação cuidadosa.

**EX013.** No nível do alerta e da triagem: ela testa se a informação de contexto ajuda os analistas a descartar disparos benignos sem deixar de pegar ataques reais.

**EX014.** Ela data a revisão e guarda os termos de busca exatos para que a busca possa ser refeita.

**EX015.** Um corpus sintético aberto e rotulado de alertas, um experimento cruzado sobre enriquecimento com contexto e uma análise de falhas do enriquecimento que induz ao erro.

**EX016.** Se as regras fossem ruins, os erros de detecção encobririam o efeito de triagem que o estudo foi desenhado para medir.

**EX017.** v1 tem precisão 0.50 e *recall* 0.75; v2 tem precisão 1.00 e *recall* 1.00 neste conjunto.

**EX018.** São correspondências legítimas realistas, exatamente os casos que o enriquecimento deveria ajudar os analistas a fechar corretamente.

**EX019.** Estudos anteriores mediram percepções ou ordenação automatizada, mas poucos fizeram experimentos controlados sobre o contexto em cartões de alerta com rótulos conhecidos.

**EX020.** Se alguma das regras é válida em geral; oito eventos apenas demonstram como funciona a pontuação por reprodução.

**EX021.** Se a linha de base não se comportar como a triagem real, uma diferença causada pelo enriquecimento não pode ser interpretada.

**EX022.** Concordância observada 0.90, concordância ao acaso 0.625, kappa 0.73.

**EX023.** Concordância substancial, a faixa de 0.61 a 0.80.

**EX024.** As duas foram discutidas; um rótulo foi corrigido e o outro alerta foi reescrito para eliminar a ambiguidade.

**EX025.** O campo de criticidade passava despercebido (movido para o topo), o log não registrava as disposições alteradas (corrigido) e as sessões de 40 alertas causavam fadiga (divididas em duas, com intervalo).

**EX026.** Quando um rótulo é muito mais raro que o outro, a concordância ao acaso é alta, então o kappa pode ser baixo mesmo quando os avaliadores concordam na maior parte.

**EX027.** Cada analista fez a triagem nas duas condições, em ordem contrabalançada, com os conjuntos de alertas trocados entre as metades.

**EX028.** A criticidade do ativo, o papel do usuário e quantos alertas semelhantes tinham sido fechados como benignos nos últimos 30 dias.

**EX029.** Linha de base 0.738 (IC de 95% 0.664–0.800); enriquecido 0.869 (0.808–0.913).

**EX030.** Como cada analista contribuiu para as duas condições, uma comparação pareada elimina as diferenças entre analistas.

**EX031.** Dois ataques genuínos foram descartados na condição enriquecida, cada um exibindo uma grande contagem de histórico benigno.

**EX032.** Uma estatística de outra universidade repetiu a análise a partir dos logs brutos e dos scripts sem ver os números de Nadia, e obteve os mesmos valores.

**EX033.** Ameaça a validade, muda as conclusões, limita o escopo e melhora o realismo.

**EX034.** Os três campos de enriquecimento não podiam ser separados; um pequeno estudo complementar de campo único sugeriu que o campo de histórico benigno produziu a maior parte do ganho e os dois ataques perdidos.

**EX035.** O dano foi levado para o resumo, com a recomendação de combinar o histórico com um aviso que explique por que o alerta ainda poderia ser malicioso.

**EX036.** Foi acrescentada uma seção de limites e o gerador de alertas foi publicado para que outros possam testar o realismo.

**EX037.** Ela cita a crítica e depois informa a mudança feita, com referência de página, ou apresenta uma discordância fundamentada e com evidências.

**EX038.** Com quatro analistas e sem registro confirmatório, ele pode sugerir, mas não estabelecer, qual campo causou o efeito.

**EX039.** Os disparos benignos dominam a carga de trabalho; o contexto nos alertas melhora a acurácia; o contexto de histórico benigno traz o risco de descartar ataques verdadeiros; o contexto deve vir com avisos de contraevidência.

**EX040.** O efeito sobre a acurácia é confirmatório; a atribuição a campos individuais e a redução do tempo são exploratórias.

**EX041.** O gerador com sua semente, o corpus rotulado, as regras Sigma, os logs anonimizados, os scripts de análise com versões fixadas e o pré-registro com o registro de mudanças (e um README).

**EX042.** Dois números diferiam na quarta casa decimal por causa de arredondamento; o script foi corrigido e a correção, registrada.

**EX043.** Os analistas receberam IDs aleatórios, os horários foram deslocados e as notas em texto livre foram retiradas depois de verificadas quanto a conteúdo identificador.

**EX044.** Introduzir os campos de enriquecimento um de cada vez e acompanhar as taxas de ataques perdidos, acrescentando salvaguardas aos campos de histórico.

**EX045.** Problema, desenho do estudo, resultados, o dano encontrado, limites e contribuições.

**EX046.** Ela disse que depende da prevalência e do custo de cada erro: o ganho só libera tempo dos analistas se as salvaguardas reduzirem as perdas causadas pelo histórico, o que um piloto operacional deveria medir.

**EX047.** Um piloto operacional em pelo menos dois SOCs que, com salvaguardas em vigor, não mostrasse ganho de acurácia ou mostrasse mais ataques perdidos do que a linha de base.

**EX048.** Um artigo sobre o experimento e o dano, um artigo de conjunto de dados sobre o corpus e o gerador, um artigo para profissionais e a publicação aberta do corpus e do código.

**EX049.** Os termos de consentimento prometiam que os participantes ouviriam os resultados primeiro.

**EX050.** A Estratégia 8, "Leverage tools to support analyst workflow", porque ela liga as constatações à forma como os SOCs planejam suas ferramentas.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro; nenhuma das normas técnicas citadas foi verificada aqui como adotada pela ABNT, por isso são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- Alahmadi, B. A., Axon, L., & Martinovic, I. (2022). 99% false positives: A qualitative study of SOC analysts' perspectives on security alarms. *31st USENIX Security Symposium*, 2783–2800. <https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi>
- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Dempsey, K., Chawla, N. S., Johnson, A., Johnston, R., Jones, A. C., Orebaugh, A., Scholl, M., & Stine, K. (2011). *Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations* (NIST SP 800-137). <https://doi.org/10.6028/NIST.SP.800-137>
- Hassan, W. U., Guo, S., Li, D., Chen, Z., Jee, K., Li, Z., & Bates, A. (2019). NoDoze: Combatting threat alert fatigue with automated provenance triage. *NDSS Symposium*. <https://doi.org/10.14722/ndss.2019.23349>
- Kaloroumakis, P. E., & Smith, M. J. (2021). *Toward a Knowledge Graph of Cybersecurity Countermeasures* (MITRE D3FEND). The MITRE Corporation. <https://d3fend.mitre.org/resources/D3FEND.pdf>
- Kent, K., & Souppaya, M. (2006). *Guide to Computer Security Log Management* (NIST SP 800-92). <https://doi.org/10.6028/NIST.SP.800-92>
- Knerler, K., Parker, I., & Zimmerman, C. (2022). *11 Strategies of a World-Class Cybersecurity Operations Center* (2nd ed.). The MITRE Corporation. <https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center>
- Kokulu, F. B., Soneji, A., Bao, T., Shoshitaishvili, Y., Zhao, Z., Doupé, A., & Ahn, G.-J. (2019). Matched and mismatched SOCs: A qualitative study on security operations center issues. *ACM CCS 2019*, 1955–1970. <https://doi.org/10.1145/3319535.3354239>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident Response Recommendations and Considerations for Cybersecurity Risk Management* (NIST SP 800-61 Rev. 3). <https://doi.org/10.6028/NIST.SP.800-61r3>
- SigmaHQ. *Sigma: Generic signature format for SIEM systems* (rule specification and repository). <https://github.com/SigmaHQ/sigma>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018, rev. 2020). *MITRE ATT&CK: Design and Philosophy* (MP180360R1). The MITRE Corporation. <https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf>
- Sundaramurthy, S. C., Case, J., Truong, T., Zomlot, L., & Hoffmann, M. (2014). A tale of three security operation centers. *ACM Workshop on Security Information Workers (SIW '14)*, 43–50. <https://doi.org/10.1145/2663887.2663904>
- van Os, R. (2016). *SOC-CMM: Designing and Evaluating a Tool for Measurement of Capability Maturity in Security Operations Centers* (Master's thesis). Luleå University of Technology. <https://ltu.diva-portal.org/smash/get/diva2:1031560/FULLTEXT02>
- Vielberth, M., Böhm, F., Fichtinger, I., & Pernul, G. (2020). Security operations center: A systematic study and open challenges. *IEEE Access*, 8, 227756–227779. <https://doi.org/10.1109/ACCESS.2020.3045514>
- Zimmerman, C. (2014). *Ten Strategies of a World-Class Cybersecurity Operations Center*. The MITRE Corporation. ISBN 978-0-692-24310-7. <https://www.mitre.org/sites/default/files/publications/pr-13-1028-mitre-10-strategies-cyber-ops-center.pdf>
