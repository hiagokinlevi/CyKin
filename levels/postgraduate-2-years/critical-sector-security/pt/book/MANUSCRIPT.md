# Infraestrutura Crítica e Segurança Setorial: Prática Especializada Avançada

- Idioma: português do Brasil (`pt`); curso de pós-graduação de especialização, dois anos; aproximadamente 600 horas de estudo planejado (curso 161 de 207 da [trilha de estudo](../../../../../STUDY_PATH.md)). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–4 de 12 já estão escritos em português, com os exercícios EX001–EX020 e suas resoluções; os capítulos 5–12 (EX021–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas são idênticas às da edição em inglês. Revisão independente, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
- Público: profissionais experientes — engenheiros de segurança, gestores de TO e de TI, responsáveis por risco e resiliência, auditores, equipes técnicas de reguladores e consultores — que já trabalham num serviço essencial ou perto dele e agora precisam **liderar** as escolhas de segurança de uma organização inteira ou de um grupo de operadores interdependentes. Conhecimento de entrada: uma primeira graduação ou experiência profissional equivalente na área; conhecimento prático de redes, identidade, tratamento de incidentes e de pelo menos um setor operacional; familiaridade com proporções, valores esperados e intervalos de confiança; e a capacidade de executar um script curto em Python.
- Como este curso difere dos vizinhos. O [livro de bacharelado](../../../../bachelors-4-years/critical-sector-security/en/book/MANUSCRIPT.md) constrói os fundamentos disciplina por disciplina. O [livro de engenharia](../../../../engineering-5-years/critical-sector-security/en/book/MANUSCRIPT.md) projeta, constrói e verifica sistemas. O [livro de mestrado](../../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md) desenha e defende um estudo empírico; o [livro de doutorado](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md) faz uma contribuição de pesquisa original. **Este livro de pós-graduação trata do julgamento profissional avançado**: tomar, justificar, avaliar e assumir decisões na escala da organização sob incerteza, com evidências boas o bastante para um conselho de administração, um regulador e as pessoas que dependem do serviço. Ele lê pesquisas para usá-las, não para produzi-las, e só constrói sistemas o suficiente para comparar e testar escolhas de projeto.
- Autoria e responsabilidade editorial: [hiagokinlevi](https://github.com/hiagokinlevi). O texto didático original, de titularidade do mantenedor, é dedicado sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus próprios direitos e não são relicenciadas aqui.
- Limite educacional: este curso é um projeto educacional independente. Não é um programa de pós-graduação credenciado, não concede qualificação e não concede nenhuma autorização para acessar, varrer, testar ou estudar qualquer infraestrutura, operador, conjunto de dados ou pessoa reais. Toda organização, lugar, pessoa, registro, custo, probabilidade e resultado numérico de um exemplo resolvido é **sintético**, a menos que uma frase cite explicitamente uma fonte pública. Nada neste livro é um procedimento operacional para uma concessionária, um hospital, um porto ou uma rede elétrica reais, e nada nele é aconselhamento jurídico, clínico ou regulatório.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Padrão de livros](../../../../../BOOK_STANDARD.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os doze capítulos acompanham o trabalho de um especialista ao longo de dois anos. A Etapa 1 (Capítulos 1–3) constrói os três hábitos sobre os quais todo o resto se apoia: decidir bem sob incerteza, saber o que a boa prática atual de fato exige em cada setor e produzir evidências especializadas que resistam ao escrutínio. A Etapa 2 (Capítulos 4–6) os aplica às partes mais difíceis do trabalho: o risco quantificado com sua distribuição ética, a escolha entre arquiteturas e a avaliação dos controles antes de confiar neles. A Etapa 3 (Capítulos 7–9) passa à organização: integrar a segurança às operações, aos fornecedores e aos arranjos regionais de emergência; lidar com casos em que toda opção prejudica alguém; e liderar e assegurar uma função de segurança. A Etapa 4 (Capítulos 10–12) fecha o ciclo: ler criticamente pesquisas e alegações de fornecedores, conduzir um projeto aplicado com uma avaliação honesta e transferir o que foi aprendido para outro setor.

Cada capítulo tem objetivos de aprendizagem, seções didáticas com definições, um exemplo resolvido, uma atividade prática com um laboratório em Python, uma lista de erros comuns e limites, cinco exercícios numerados e uma síntese. Os laboratórios usam apenas a biblioteca padrão do Python 3 (as saídas deste rascunho foram produzidas com o Python 3.13); não precisam de rede, pacotes nem dados reais, e toda saída está impressa no texto para que você confira sua execução. Escreva sua resposta a cada exercício antes de abrir as [resoluções](#worked-results). Muitos exercícios têm mais de uma resposta defensável: a resolução mostra uma, e a rubrica mostra o que um avaliador experiente recompensaria.

Mantenha cinco rótulos em toda nota de trabalho: **observação** (o que uma fonte nomeada registrou), **inferência** (o que você conclui e sob quais pressupostos), **julgamento** (o que você pondera quando as evidências acabam), **decisão** (o que alguém escolheu, com autoridade para escolher) e **consequência** (o efeito sobre as pessoas que dependem do serviço). A falha mais comum no nível de especialista não é desconhecer um controle; é uma recomendação confiante cujas evidências, pressupostos e responsável não podem ser encontrados depois.

### O cenário sintético usado neste livro

| Elemento sintético | Papel no livro | Limite |
|---|---|---|
| **Merrow Bay** — uma região costeira de cerca de 230.000 habitantes | Cenário de todos os exemplos resolvidos. | Região inventada. |
| **Merrow Water (MW)** — água potável e esgoto; estações de tratamento em Hollin, Fenley, Upper Merrow, Kettle Ford, Ashby, Saltings e seis locais menores | A organização em que o leitor é **Especialista Principal de Segurança**, subordinado ao Diretor de Operações, com uma linha pontilhada para o Diretor de Segurança da Informação (CISO). | Inventada; nenhuma concessionária, equipe ou sistema real. |
| **Merrow Health (MH)**, **Merrow Energy Networks (ME)**, **Port of Merrow (PoM)** | Operadores vizinhos que compartilham fornecedores, energia e telecomunicações com a MW. | Inventados. |
| **Merrow Bay Resilience Forum (MBRF)** | Grupo regional multiagências de planejamento de emergências. | Inventado. |
| Fornecedores **Corvane Systems**, **Lumen Watch**, **BayTel**, **Halden Cloud** | Integrador de SCADA, provedor de detecção gerenciada, operadora de telecomunicações, hospedagem em nuvem. | Empresas inventadas; qualquer semelhança com empresas reais é acidental. |
| O conselho, os reguladores, a conta "vendor-svc", todo custo, probabilidade, linha de log e tempo de simulado | Contexto de decisão dos exercícios. | Valores inventados, escolhidos para o ensino. |

Como os dados são sintéticos, o livro às vezes pode dizer algo que um operador real nunca sabe — por exemplo, qual de duas explicações gerou um log. Use esse privilégio para aprender como os métodos falham, nunca como evidência sobre organizações reais.

### Política de fontes

Toda afirmação factual sobre uma lei, uma norma, um incidente público ou um estudo publicado remete a uma fonte consultada em outubro de 2026. Leis, normas e orientações mudam: cada uma é citada com sua versão ou data e deve ser verificada de novo antes que você se apoie nela, e nada aqui interpreta uma lei para uma organização em particular. Onde uma afirmação é vocabulário profissional ou estatístico padrão — por exemplo, que o valor esperado pondera cada resultado por sua probabilidade —, o texto diz isso em vez de inventar uma referência. Uma citação apoia a afirmação geral ao seu lado, nunca os detalhes sintéticos. Incidentes públicos são descritos apenas no nível de detalhe que seus editores divulgaram e, onde um primeiro relato foi revisado depois, ambos são citados.

## Sumário

1. [Tomada de decisão avançada em segurança](#ch-01) — enquadramento das decisões, objetivos em unidades de serviço, valor esperado, arrependimento e robustez, valor da informação, vieses e o registro de decisão.
2. [Infraestrutura crítica e segurança setorial: prática atual](#ch-02) — o que as linhas de base e os regimes exigem nos setores, cobertura declarada versus verificada e priorização pela consequência.
3. [Infraestrutura crítica e segurança setorial: evidências especializadas](#ch-03) — evidências em ambientes de TO e mistos, relógios e linhas do tempo, preservação sem perturbar o processo e constatações que separam observação de inferência.
4. [Risco avançado e ética](#ch-04) — risco quantificado com incerteza, excedência de perdas, apetite a risco em unidades de serviço e quem arca com o risco residual.

Capítulos 5–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-05), até a chegada dos próximos lotes.

Apêndices: [Resoluções e notas de avaliação](#worked-results) · [Glossário](#glossary) · [Referências](#references).

<a id="ch-01"></a>

## Capítulo 1 — Tomada de decisão avançada em segurança

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

1. Enquadrar uma decisão de segurança na escala da organização: quem decide, até quando, entre quais opções, segundo quais objetivos.
2. Expressar os objetivos em unidades do serviço essencial — horas de fornecimento perdidas, pacientes desviados, domicílios afetados — e não apenas em dinheiro ou em contagens de controles.
3. Comparar opções pelo valor esperado, pelo pior caso e pelo arrependimento minimax, e explicar quando cada regra é adequada.
4. Testar quão sensível uma recomendação é às probabilidades sobre as quais você tinha menos certeza e declarar o limiar em que ela muda.
5. Estimar o valor de mais informação antes de comprá-la.
6. Reconhecer os erros de julgamento que mais frequentemente distorcem as decisões de segurança em serviços essenciais.
7. Escrever um registro de decisão que um sucessor, um auditor ou um regulador consiga acompanhar.

Este capítulo estabelece os hábitos de decisão que todos os capítulos seguintes usam. O Capítulo 4 acrescenta o risco quantificado e sua distribuição entre as pessoas; o Capítulo 5 aplica o mesmo raciocínio às arquiteturas; o Capítulo 9 transforma os registros de decisão em asseguração.

### 1.1 O que torna uma decisão "da escala da organização"

Um profissional em estágios anteriores escolhe configurações, ferramentas e procedimentos. Um especialista que lidera a segurança de um serviço essencial escolhe **portfólios sob restrição**: qual de vários programas que valem a pena financiar neste ano, que risco aceitar, que fornecedor manter, quando desconectar uma planta de uma rede. Essas decisões têm cinco características em comum. São **irreversíveis ou caras de reverter** — um contrato de serviço gerenciado de três anos, uma rede de controle rearquitetada. Seus resultados são **incertos e raros**, de modo que a experiência sozinha dá um retorno pobre: uma concessionária pode passar uma década sem o evento para o qual um controle foi comprado. Têm **vários objetivos** que não podem ser reduzidos honestamente a um único número: continuidade do fornecimento, segurança dos funcionários e do público, custo, conformidade legal, privacidade e reputação. Têm **várias partes interessadas** com interesses legítimos, mas diferentes — o conselho, os operadores, o regulador, os clientes, os operadores vizinhos. E são **tomadas por alguém com autoridade**, que precisará explicá-las depois.

O trabalho do especialista raramente é tomar a decisão sozinho. É **estruturá-la** para que a pessoa com autoridade possa decidir bem, e tornar essa estrutura inspecionável. Essa distinção importa para a responsabilização (Capítulo 7) e para a ética (Capítulo 4): um analista que escolhe os pesos em silêncio tomou a decisão enquanto parecia apenas aconselhar.

### 1.2 Enquadramento: a declaração da decisão

A maioria das más decisões de segurança são respostas bem analisadas a perguntas mal enquadradas. Uma **declaração da decisão** fixa seis coisas antes de qualquer análise:

| Elemento | Pergunta | Exemplo da Merrow Water (sintético) |
|---|---|---|
| Tomador de decisão | Quem tem autoridade para escolher e para aceitar o risco residual? | Diretor de Operações, com aprovação do conselho acima de £500 mil por ano |
| Decisão | O que exatamente está sendo escolhido? | Qual programa de segurança financiar no próximo exercício a partir de um envelope fixo |
| Opções | Quais alternativas genuinamente diferentes estão na mesa, incluindo "adiar"? | A endurecimento do acesso remoto; B capacidade de operação manual; C metade de cada; D adiar |
| Objetivos | O que tentamos proteger ou alcançar, em quais unidades? | Minimizar o custo esperado e o de pior caso da perda do fornecimento de água tratada, incluindo o custo do programa; manter o público seguro; cumprir os deveres regulatórios |
| Horizonte e prazo | Em que período os resultados são julgados, e quando precisamos escolher? | Um ano orçamentário; decisão na reunião do conselho de março |
| Restrições | O que não pode ser violado, diga a análise o que disser? | Nenhuma opção pode reduzir a capacidade dos operadores de operar as plantas manualmente; nenhum aumento de quadro fora do orçamento |

A **opção "adiar"** merece atenção explícita. Ela está sempre disponível, é o que acontece quando ninguém decide e, em serviços essenciais, costuma ser pior do que parece, porque suas perdas se concentram em cenários raros e graves. Escrevê-la obriga a análise a mostrar seu custo.

Boas opções são **genuinamente diferentes**, e não uma opção favorita com dois espantalhos. Um teste útil: uma pessoa razoável e informada poderia preferir cada uma delas sob alguma visão plausível do mundo? Se não, o conjunto de opções é um exercício de justificação.

### 1.3 Objetivos em unidades de serviço

O NIST Cybersecurity Framework 2.0 coloca a função "Govern" (Governar) no centro da gestão de segurança e pede às organizações que entendam sua missão, suas partes interessadas e seu apetite a risco antes de escolher controles ([NIST, CSF 2.0, 2024](https://doi.org/10.6028/NIST.CSWP.29)). Para um serviço essencial, a missão é entregue em **unidades de serviço**: litros de água conforme, megawatts-hora entregues, pacientes atendidos dentro das metas de tempo clínico, contêineres movimentados, pagamentos liquidados. Um objetivo expresso em unidades de serviço faz três coisas que um objetivo monetário não consegue. Mantém visíveis as pessoas que dependem do serviço; permite que os operadores — que pensam em unidades de serviço — confiram a análise; e expõe os casos em que dinheiro e dano divergem, por exemplo quando uma interrupção barata recai sobre pessoas que não conseguem lidar com ela (Capítulo 4).

Na prática, você usará ambos: unidades de serviço para a consequência e dinheiro para o custo. Mantenha-os em colunas separadas até que o tomador de decisão concorde com uma taxa de conversão, e registre essa taxa como um julgamento, não como um fato. O Cyber Assessment Framework do National Cyber Security Centre do Reino Unido faz um movimento semelhante ao organizar seus objetivos em torno da função essencial, e não dos ativos de TI ([NCSC, Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf)).

### 1.4 Três regras de decisão

Suponha que você tenha uma tabela de opções por cenários, com o custo anual total (custo do programa mais a perda) em cada célula. Três regras de decisão leem essa tabela de modos diferentes.

**Valor esperado (VE).** Pondere o resultado de cada cenário por sua probabilidade e some. Escolha a opção com o menor custo esperado. O VE é a regra certa quando você enfrenta muitas decisões semelhantes e independentes e consegue absorver a variação, porque ao longo de muitas repetições a média é o que você paga. É o padrão no raciocínio de seguros e de portfólio. Suas fraquezas: depende de probabilidades que, para eventos ciberfísicos raros, ninguém conhece bem; e trata uma pequena chance de catástrofe como intercambiável com uma pequena perda certa.

**Minimax (pior caso).** Escolha a opção cujo pior resultado seja o menos ruim. O minimax é adequado quando um resultado seria inaceitável independentemente de sua probabilidade — perda de vidas, perda da organização, perda da confiança pública na água potável. Sua fraqueza é ignorar por completo as probabilidades e poder comprar uma proteção cara contra um cenário quase impossível.

**Arrependimento minimax.** Para cada cenário, encontre a melhor opção; o **arrependimento** de uma opção nesse cenário é quanto ela é pior do que essa melhor. Escolha a opção cujo maior arrependimento seja o menor ([Savage, 1951](https://doi.org/10.1080/01621459.1951.10500768)). O arrependimento captura como uma decisão parecerá depois — "deveríamos ter feito X" — e tende a favorecer opções equilibradas quando nenhum cenário domina. Sua fraqueza é que acrescentar ou retirar uma opção irrelevante pode mudar a resposta.

Nenhuma dessas regras é "a correta". Um especialista relata o que cada regra recomenda, explica por que elas diferem e ajuda o tomador de decisão a escolher uma regra *antes* de ver qual opção ela favorece. Quando as três concordam, a decisão é robusta. Quando discordam, a discordância é a coisa mais útil que você pode mostrar a um conselho.

### 1.5 Probabilidades que você não conhece: sensibilidade e limiares

As probabilidades de cenários de segurança raros são julgamentos, não medições. Três práticas as mantêm honestas. Primeiro, **elicite com cuidado**: peça intervalos, pergunte a várias pessoas de forma independente e pergunte pelas taxas de base antes do caso específico ([O'Hagan et al., 2006](https://doi.org/10.1002/0470033312)). Segundo, **mostre vários conjuntos de crenças** — o do analista, o de um pessimista, a visão implícita do regulador — em vez de um só. Terceiro, e mais útil, **encontre o limiar**: a probabilidade em que a recomendação muda. Um conselho dificilmente consegue dizer se a probabilidade de comprometimento do acesso remoto de TO é de 3% ou de 6% ao ano, mas muitas vezes consegue dizer se ela está acima ou abaixo de um limiar declarado, sobretudo se você lhe mostrar as evidências por trás de cada visão — por exemplo, alertas públicos que descrevem o pré-posicionamento em redes de infraestrutura ([CISA, AA24-038A, 2024](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a)).

### 1.6 Valor da informação

Antes de encomendar uma avaliação, um teste de intrusão ou um estudo de consultoria, pergunte o que ele poderia mudar. O **valor esperado da informação perfeita (VEIP)** é a diferença entre o custo esperado da melhor opção agora e o custo esperado se você pudesse saber, antes de escolher, qual cenário vai acontecer. É um limite superior para o que qualquer estudo vale para esta decisão: se o VEIP é de £50 mil, um estudo de £200 mil não pode se pagar apenas por meio desta decisão. Estudos reais dão informação imperfeita, então valem menos do que o VEIP; se um estudo não puder plausivelmente mover uma probabilidade para o outro lado do limiar encontrado na §1.5, ele vale pouco para a decisão, por mais interessante que seja. Esse é o raciocínio padrão da análise de decisão; o ponto para a prática é escrever, antes de comprar a informação, qual resultado mudaria qual escolha.

### 1.7 Erros de julgamento que distorcem as decisões de segurança

A pesquisa clássica sobre julgamento sob incerteza descreve heurísticas — disponibilidade, representatividade, ancoragem — que levam a erros sistemáticos ([Tversky e Kahneman, 1974](https://doi.org/10.1126/science.185.4157.1124)). Na segurança de serviços essenciais, elas aparecem em formas reconhecíveis:

- **Disponibilidade depois de uma manchete.** Um incidente amplamente noticiado em outro setor eleva a probabilidade percebida desse cenário e afasta cenários mais discretos e mais prováveis.
- **Ancoragem no orçamento do ano passado ou na primeira cotação de um fornecedor.**
- **Substituição pela conformidade.** Tratar "o regulador exige X" como se respondesse "X é o melhor uso da próxima libra". A conformidade é uma restrição (§1.2), não um objetivo.
- **Contagem de controles.** Preferir a opção que fecha mais constatações de auditoria em vez da que mais reduz a consequência.
- **Otimismo sobre o recurso manual.** Supor que os operadores conseguem operar uma planta à mão porque um dia conseguiram, sem um simulado recente (Capítulo 6).
- **Pensamento de grupo e deferência.** A pessoa mais graduada fala primeiro e os demais se ancoram nela.

Remédios estruturais funcionam melhor do que exortações: estimativas independentes antes da discussão; um cético designado; um **pré-mortem**, em que o grupo imagina que a decisão fracassou e escreve por quê ([Klein, 2007](https://hbr.org/2007/09/performing-a-project-premortem)); e um registro escrito das divergências.

### 1.8 O registro de decisão

Um **registro de decisão** é um documento curto, escrito no momento da decisão, que contém: a declaração da decisão; as opções e por que cada uma foi considerada; as evidências usadas, com as fontes; os julgamentos de probabilidade e de peso e quem os fez; o que cada regra de decisão recomendou; a análise de limiares; a escolha feita, por quem e com base em qual regra; o risco residual aceito e seu responsável; as divergências; e o **gatilho de revisão** — a observação que reabriria a decisão (por exemplo, "um alerta crível relatando o comprometimento de appliances de acesso remoto do tipo que usamos"). O registro protege os bons tomadores de decisão quando um evento raro acontece mesmo assim, e é o modo como as organizações aprendem: sem ele, a visão retrospectiva reescreve o que se sabia.

### 1.9 Exemplo resolvido: a escolha de programa da Merrow Water (sintético)

O envelope da Merrow Water permite uma de quatro opções para o próximo ano. O especialista e a equipe de operações montaram a tabela abaixo (milhares de libras por ano, incluindo o próprio custo de cada opção; menor é melhor). A opção A endurece o acesso remoto (sessões de fornecedores intermediadas, MFA resistente a phishing, remoção de contas permanentes). A opção B constrói a capacidade de operação manual (procedimentos, instrumentação local, simulados, cobertura de pessoal) para que as plantas continuem produzindo água segura quando os sistemas de controle forem perdidos. A opção C faz metade de cada. A opção D adia.

| Opção | Ransomware em TI | Comprometimento do acesso remoto de TO | Indisponibilidade de fornecedor/nuvem | Ano tranquilo |
|---|---:|---:|---:|---:|
| A endurecimento do acesso remoto | 700 | 240 | 650 | 170 |
| B capacidade de operação manual | 450 | 900 | 330 | 230 |
| C metade de cada | 560 | 520 | 470 | 200 |
| D adiar | 1.300 | 2.600 | 780 | 0 |

O raciocínio por trás de algumas células importa mais do que os números. B se sai bem sempre que os sistemas de controle são *perdidos* (ransomware, indisponibilidade), porque a planta continua funcionando à mão, mas mal quando eles são *mal utilizados* por um intruso, porque a capacidade manual não impede comandos maliciosos antes que sejam notados. A se sai bem contra o intruso, mas não contra a perda. D é a mais barata num ano tranquilo e catastrófica no cenário de TO, cujo custo inclui um aviso de fervura da água que afeta toda a zona de abastecimento de Hollin.

A equipe registrou três conjuntos de crenças para as probabilidades dos cenários: o do analista (15% / 3% / 10% / 72%), o de um pessimista (25% / 10% / 15% / 50%) e uma visão implícita do regulador, com mais peso no comprometimento de TO (10% / 8% / 5% / 77%). O Laboratório 1 calcula os resultados.

### 1.10 Atividade prática: uma decisão, três regras

Execute o laboratório e depois leia a interpretação.

```python
# Lab 1 - one decision, three decision rules (offline, standard library only)
# Synthetic: Merrow Water's annual security investment choice. Figures are invented, in GBP thousands per year,
# and already include each option's own annual cost. Lower is better (cost + expected/realized loss).
OPTIONS = ["A remote-access hardening", "B manual-operations capability", "C half of each", "D defer"]
SCEN = ["IT ransomware", "OT remote-access compromise", "vendor/cloud outage", "quiet year"]
COST = {  # option -> loss in each scenario (k GBP)
    "A remote-access hardening":      [ 700,  240,  650, 170],
    "B manual-operations capability": [ 450,  900,  330, 230],
    "C half of each":                 [ 560,  520,  470, 200],
    "D defer":                        [1300, 2600,  780,   0],
}
BELIEFS = {
    "analyst":    [0.15, 0.03, 0.10, 0.72],
    "pessimist":  [0.25, 0.10, 0.15, 0.50],
    "regulator":  [0.10, 0.08, 0.05, 0.77],
}
def ev(o, p): return sum(c * q for c, q in zip(COST[o], p))
for name, p in BELIEFS.items():
    assert abs(sum(p) - 1) < 1e-9
    ranked = sorted(OPTIONS, key=lambda o: ev(o, p))
    print(f"{name:10s}", "  ".join(f"{o[0]}={ev(o, p):7.1f}" for o in OPTIONS), " best:", ranked[0][0])
best_in = [min(COST[o][s] for o in OPTIONS) for s in range(len(SCEN))]
regret = {o: max(COST[o][s] - best_in[s] for s in range(len(SCEN))) for o in OPTIONS}
worst = {o: max(COST[o]) for o in OPTIONS}
print("max regret:", "  ".join(f"{o[0]}={regret[o]}" for o in OPTIONS), " minimax-regret:", min(OPTIONS, key=regret.get)[0])
print("worst case:", "  ".join(f"{o[0]}={worst[o]}" for o in OPTIONS), " minimax:", min(OPTIONS, key=worst.get)[0])
# Robustness: sweep P(OT compromise) from 0 to 0.30, keeping the analyst's other ratios, and report the EV winner.
base = BELIEFS["analyst"]
prev = None
for k in range(0, 31):
    q = k / 100
    rest = [base[0], base[2], base[3]]; s = sum(rest)
    p = [rest[0] / s * (1 - q), q, rest[1] / s * (1 - q), rest[2] / s * (1 - q)]
    win = min(OPTIONS, key=lambda o: ev(o, p))[0]
    if win != prev:
        print(f"P(OT compromise)={q:.2f}: EV winner {win}")
        prev = win
```

Saída esperada:

```text
analyst    A=  299.6  B=  293.1  C=  290.6  D=  351.0  best: C
pessimist  A=  381.5  B=  367.0  C=  362.5  D=  702.0  best: C
regulator  A=  252.6  B=  310.6  C=  275.1  D=  377.0  best: A
max regret: A=320  B=660  C=280  D=2360  minimax-regret: C
worst case: A=700  B=900  C=560  D=2600  minimax: C
P(OT compromise)=0.00: EV winner B
P(OT compromise)=0.03: EV winner C
P(OT compromise)=0.07: EV winner A
```

**Interpretação.** Sob as crenças do analista e do pessimista, C tem o menor custo esperado, mas por pouco: 290,6 contra 293,1 de B e 299,6 de A na visão do analista. Diferenças de £3 mil a £9 mil em estimativas tão grosseiras não são, por si sós, base para uma decisão. Sob as crenças do regulador, A vence. A varredura de limiares torna a estrutura visível: B vence apenas se a probabilidade de comprometimento de TO estiver abaixo de cerca de 3%; C entre cerca de 3% e 7%; A acima de cerca de 7%. O minimax e o arrependimento minimax escolhem ambos C, porque C nunca se sai muito mal. **C é, portanto, a recomendação robusta**: é a melhor ou quase a melhor sob todo conjunto de crenças e toda regra. O registro de decisão deve dizer exatamente isso e acrescentar o gatilho de revisão: evidências que empurrem a probabilidade de comprometimento de TO para acima de 7% (por exemplo, relatos críveis de exploração dos produtos de acesso remoto que a Merrow usa) movem a recomendação para A. Note também o que a tabela não consegue mostrar: o valor de C pressupõe que "metade de cada" entrega mais da metade do benefício de cada uma, o que é um julgamento que o diretor de operações precisa confirmar.

### 1.11 Erros comuns e limites

- Apresentar um único "escore de risco" por opção, o que esconde se o escore veio da frequência, da gravidade ou de uma ponderação arbitrária.
- Omitir a opção de adiar, ou atribuir-lhe custo zero.
- Escolher a regra de decisão depois de ver qual opção ela favorece.
- Relatar valores esperados até a libra quando os insumos são julgamentos grosseiros; relate, em vez disso, as diferenças que importam e os limiares.
- Tratar estatísticas de fornecedores ou de pesquisas com aparência precisa como probabilidades para a sua organização sem perguntar como foram produzidas (Capítulo 10).
- Deixar que os pesos do analista se tornem, em silêncio, a decisão.
- Escrever o registro de decisão depois, quando a visão retrospectiva já o moldou.

O principal limite da análise formal de decisão é que ela só é tão boa quanto o conjunto de opções e o modelo de consequências. Seu valor não está em produzir automaticamente a resposta certa, mas em tornar as razões de uma resposta **inspecionáveis** e **revisáveis** quando chegam novas evidências.

### Exercícios — capítulo 1

**EX001 — Enquadre uma decisão hospitalar.** *Objetivo:* escrever uma declaração da decisão para uma escolha com cara de real. *Insumos:* a Merrow Health precisa decidir se substitui neste ano seu sistema de laboratório de patologia sem suporte ou se o isola e o substitui em dois anos. *Restrições:* usar os seis elementos da §1.2; pelo menos três opções genuinamente diferentes, incluindo adiar; objetivos em unidades de serviço. *Passos:* (1) escrever a declaração; (2) aplicar a cada opção o teste "uma pessoa razoável poderia preferi-la"; (3) listar duas restrições que não sejam objetivos. *Evidência esperada:* declaração da decisão de uma página. *Rubrica:* 3 = todos os seis elementos, opções genuinamente diferentes, objetivos em unidades de serviço (por exemplo, o tempo de liberação dos resultados urgentes), restrições distinguidas dos objetivos; 2 = um elemento fraco; 1 = as opções são espantalhos ou os objetivos estão apenas em dinheiro; 0 = ausente.

**EX002 — Mude uma célula.** *Objetivo:* ver como as regras de decisão respondem a uma estimativa de consequência revisada. *Insumos:* Laboratório 1. *Restrições:* mudar apenas o custo de D no cenário de TO, de 2.600 para 1.200 (os engenheiros acreditam que um aviso de fervura poderia ficar restrito a uma zona). *Passos:* (1) reexecutar; (2) relatar o vencedor pelo VE sob cada conjunto de crenças, o arrependimento máximo de cada opção e a escolha pelo arrependimento minimax; (3) explicar por que D ainda não vence. *Evidência esperada:* saídas e explicação de 150 palavras. *Rubrica:* 3 = números corretos e uma explicação que liga o arrependimento de D ao cenário de ransomware, e não apenas ao de TO; 2 = números certos, explicação rasa; 1 = não executado; 0 = nada.

**EX003 — Valor da informação perfeita.** *Objetivo:* delimitar quanto vale um estudo adicional. *Insumos:* a tabela do Laboratório 1 e as crenças do analista. *Restrições:* calcular à mão ou com um pequeno acréscimo ao laboratório. *Passos:* (1) calcular o custo esperado da melhor opção agora; (2) calcular o custo esperado se você soubesse o cenário antes de escolher; (3) relatar o VEIP; (4) um consultor oferece uma avaliação de ameaças de TO por £60 mil — explicar sob que condição ela poderia valer a compra para esta decisão. *Evidência esperada:* cálculo e parágrafo. *Rubrica:* 3 = VEIP correto e a compra ligada a se o estudo poderia mover a probabilidade de TO para o outro lado dos limiares de 3% ou 7%; 2 = VEIP certo, ligação fraca; 1 = erros aritméticos; 0 = nada.

**EX004 — Registro de decisão com divergência.** *Objetivo:* produzir um registro inspecionável. *Insumos:* o exemplo resolvido e a saída do Laboratório 1. *Restrições:* uma página; todos os elementos da §1.8. *Passos:* (1) escrever o registro da escolha de C; (2) incluir uma divergência realista do gerente de operações, que prefere B; (3) declarar o gatilho de revisão e o responsável pelo risco residual. *Evidência esperada:* registro de decisão. *Rubrica:* 3 = completo, honesto sobre as margens estreitas de VE, divergência declarada com justiça, gatilho mensurável; 2 = falta um elemento; 1 = parece advocacia; 0 = nada.

**EX005 — Auditoria de vieses.** *Objetivo:* reconhecer erros de julgamento numa reunião. *Insumos:* ata sintética: "O presidente abriu mencionando o recente caso de ransomware no oleoduto e disse que a segurança de TO é agora a prioridade máxima. A proposta de £400 mil do fornecedor foi tomada como ponto de partida. O gerente de operações disse que operar manualmente 'não é problema — fizemos isso em 2009'. A responsável pela auditoria interna observou que a opção A fecha nove das onze constatações em aberto. Nenhuma outra opinião foi registrada." *Restrições:* nomear no máximo cinco erros da §1.7 e propor um remédio estrutural para cada um. *Passos:* identificar, explicar, remediar. *Evidência esperada:* tabela. *Rubrica:* 3 = disponibilidade, ancoragem, otimismo sobre o recurso manual, contagem de controles e deferência/pensamento de grupo identificados com remédios estruturais (estimativas independentes, pré-mortem, evidência de simulado, pontuação baseada na consequência, divergência registrada); 2 = três ou quatro; 1 = conselhos genéricos; 0 = nada.

### Síntese do capítulo

As decisões de segurança na escala da organização são irreversíveis, envolvem eventos raros, múltiplos objetivos e múltiplas partes interessadas, e pertencem a alguém com autoridade. A contribuição do especialista é a estrutura: uma declaração da decisão com opções genuinamente diferentes, incluindo adiar; objetivos em unidades de serviço; várias regras de decisão relatadas lado a lado; conjuntos de crenças em vez de uma única probabilidade; os limiares em que a recomendação muda; o valor de mais informação; defesas estruturais contra o julgamento enviesado; e um registro de decisão escrito no momento. Uma recomendação robusta é aquela que sobrevive a mudanças de regra e de crença; quando não sobrevive, mostre o limiar e deixe a pessoa responsável decidir com conhecimento de causa.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 12

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Infraestrutura crítica e segurança setorial: prática atual

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

1. Descrever as principais linhas de base e regimes, transversais e setoriais, que um operador de serviço essencial provavelmente encontrará, e que tipo de obrigação cada um cria.
2. Explicar por que setores que compartilham tecnologia ainda precisam de práticas diferentes: consequência, física, regulação e força de trabalho diferem.
3. Distinguir a implementação declarada, documentada e verificada de uma prática, e medir a lacuna.
4. Priorizar as lacunas pela consequência para o serviço essencial, e não pela contagem.
5. Criticar uma prática comum e propor uma alternativa mais bem fundamentada em evidências.

O Capítulo 1 deu a você um modo de escolher entre opções. Este capítulo fornece as opções que se espera que um especialista competente conheça e o padrão de evidências para dizer que elas estão implementadas. O Capítulo 3 pergunta, então, o que conta como evidência quando algo dá errado.

### 2.1 O que "prática atual" significa para um especialista

"Prática atual" não é uma lista única. É a sobreposição de três coisas: o que **reguladores e normas exigem** na sua jurisdição e no seu setor; o que **orientações autorizadas** recomendam com base em ataques observados; e o que **operadores comparáveis efetivamente fazem** e conseguem demonstrar. Um especialista precisa conhecer as três e precisa saber dizer quais afirmações de um programa de segurança vêm de qual fonte, porque elas têm pesos diferentes. Uma obrigação legal é uma restrição; o requisito de uma norma pode ser contratual ou certificável; uma orientação é um conselho a ser ponderado contra a sua própria análise de consequências.

A prática também envelhece. Alertas sobre o pré-posicionamento em redes de infraestrutura por atores patrocinados por Estados que usam ferramentas legítimas de administração ([CISA, AA24-038A, 2024](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a)) mudaram o que "registro adequado" e "higiene adequada de credenciais" significam para operadores que tratavam essas coisas como faxina de TI. Uma linha de base que era atual há três anos pode agora ser um piso.

### 2.2 Linhas de base transversais aos setores

Quatro famílias de documentos se repetem entre os setores:

- **Frameworks de resultados.** O NIST CSF 2.0 organiza os resultados em Govern, Identify, Protect, Detect, Respond e Recover (Governar, Identificar, Proteger, Detectar, Responder e Recuperar) ([NIST, 2024](https://doi.org/10.6028/NIST.CSWP.29)). O Cyber Assessment Framework do NCSC do Reino Unido estabelece quatro objetivos — gerir o risco de segurança, proteger contra ataques cibernéticos, detectar eventos de segurança cibernética e minimizar o impacto dos incidentes —, com indicadores de boa prática para cada princípio, e é desenhado em torno das funções essenciais ([NCSC, CAF](https://www.ncsc.gov.uk/collection/caf)). Os frameworks de resultados dizem *o que* precisa ser alcançado, não *como*; são bons para estruturar um programa e fracos como roteiros de teste.
- **Linhas de base priorizadas.** As Cross-Sector Cybersecurity Performance Goals da CISA listam um pequeno conjunto de práticas com alto valor de redução de risco para organizações de qualquer porte ([CISA, CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)); o Departamento de Saúde e Serviços Humanos dos EUA publicou metas de desempenho específicas para a saúde no mesmo espírito ([HHS, HPH CPGs, 2024](https://hphcyber.hhs.gov/performance-goals.html)). São úteis justamente por serem curtas; não são um programa completo.
- **Catálogos de controles.** A NIST SP 800-53 Rev. 5 é um catálogo abrangente de controles de segurança e privacidade ([NIST](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)); a NIST SP 800-82 Rev. 3 adapta as orientações à tecnologia operacional, incluindo overlays e as restrições particulares dos sistemas de controle ([NIST, 2023](https://doi.org/10.6028/NIST.SP.800-82r3)).
- **Normas industriais.** A série ISA/IEC 62443 trata da segurança dos sistemas de automação e controle industrial para proprietários de ativos, integradores e fornecedores de produtos, incluindo zonas e conduítes, níveis de segurança e desenvolvimento seguro de produtos ([visão geral da ISA](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). Sua parte de avaliação de riscos para o projeto de sistemas, a IEC 62443-3-2, é o ponto de partida usual de uma revisão de arquitetura de TO ([página do catálogo da IEC](https://webstore.iec.ch/en/publication/30727)).

### 2.3 Os regimes setoriais criam tipos diferentes de obrigação

Na escala da organização, a pergunta não é "qual framework é o melhor", mas "quais obrigações se aplicam a nós, e que evidências cada regulador vai esperar". Exemplos, todos a verificar de novo para a sua jurisdição e data:

| Regime | Escopo (resumo) | Tipo de obrigação | Evidências tipicamente esperadas |
|---|---|---|---|
| [Diretiva NIS2 (UE) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/) | Entidades essenciais e importantes dos setores listados, transposta para o direito nacional | Medidas de gestão de risco e notificação de incidentes em etapas (alerta precoce, notificação, relatório final) | Medidas aprovadas pelo órgão de administração, relatórios de incidentes dentro dos prazos nacionais |
| [Diretiva CER (UE) 2022/2557](https://eur-lex.europa.eu/eli/dir/2022/2557/oj) | Resiliência das entidades críticas frente a todos os perigos | Avaliação de riscos e medidas de resiliência, não apenas cibernéticas | Planos de resiliência, cooperação com as autoridades |
| [DORA, Regulamento (UE) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) | Entidades financeiras e seus prestadores terceiros críticos de serviços de TIC | Regras diretamente aplicáveis de risco de TIC, testes, incidentes e terceiros | Registros dos acordos com terceiros de TIC, resultados de testes |
| [Normas NERC CIP](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx) | Sistema elétrico de grande porte na América do Norte | Requisitos obrigatórios e auditáveis por categoria de impacto do ativo | Evidências de auditoria por requisito, muitas vezes altamente prescritivas |
| [America's Water Infrastructure Act 2018, s.2013](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans) | Sistemas comunitários de água dos EUA acima de um limiar de porte | Avaliação de risco e resiliência e plano de resposta a emergências, com certificação | Avaliações e planos certificados em ciclos |

Seguem-se duas lições. Primeiro, um operador que abrange vários setores — uma multiconcessionária, um porto com rede elétrica própria — pode estar sob vários regimes com relógios de notificação e estilos de evidência diferentes; harmonizá-los num único conjunto interno de controles com mapeamentos é uma tarefa central do especialista. Segundo, **a conformidade é um piso e uma restrição**, como o Capítulo 1 argumentou: dois operadores plenamente conformes com o mesmo regime podem ter resiliências muito diferentes.

### 2.4 Por que a prática setorial difere

A tecnologia compartilhada tenta as pessoas a copiar práticas entre setores. Quatro diferenças tornam isso inseguro:

1. **Consequência e tempo.** Os sistemas clínicos de um hospital falham em danos que chegam em minutos ou horas; um sistema de água com reservação pode ter de horas a dias; o dano de um sistema de pagamentos se acumula nas janelas de liquidação; o de um porto, no tempo de permanência da carga e nas cadeias de suprimento. O tempo até o dano define quanto recurso manual é necessário e quão rápida uma resposta precisa ser.
2. **Física e segurança operacional.** Na TO, uma ação de segurança pode ela mesma causar dano: uma varredura agressiva pode derrubar um controlador; isolar uma rede pode cegar os operadores. A NIST SP 800-82 enfatiza que as restrições de disponibilidade e de segurança operacional moldam quais controles de segurança são aceitáveis ([NIST, 2023](https://doi.org/10.6028/NIST.SP.800-82r3)).
3. **Regulação e cultura de evidências.** A eletricidade na América do Norte trabalha com requisitos auditáveis e prescritivos; muitas concessionárias de água trabalham com avaliações certificadas periódicas; a saúde trabalha sob a legislação de privacidade e a governança de segurança clínica, além das regras de segurança.
4. **Força de trabalho e fornecedores.** Concessionárias pequenas podem não ter nenhuma equipe de segurança; hospitais dependem dos fabricantes de dispositivos médicos para aplicar correções; portos dependem dos fornecedores de sistemas operacionais de terminais e das companhias de navegação. Quem consegue de fato implementar uma prática determina se ela é real.

### 2.5 Declarado, documentado e verificado

A maioria das avaliações de linha de base são autoavaliações. São úteis, mas um especialista precisa saber quanto de um "sim" é **verificado**. Use três graus de evidência:

- **Verificado (V):** a prática foi observada funcionando por teste, inspeção ou conciliação — uma restauração foi realizada e cronometrada; a configuração do provedor de identidade foi exportada e conferida; os logs do intermediador foram conciliados com as sessões do firewall.
- **Documentado (D):** existe uma política, um projeto ou um procedimento que diz que a prática está implementada, mas ninguém testou se a realidade corresponde.
- **Declaração (S):** alguém disse que sim.

Os métodos de avaliação do catálogo do NIST distinguem examinar, entrevistar e testar pela mesma razão ([NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)). A lacuna entre a cobertura declarada e a verificada costuma ser o número mais importante de um relatório de linha de base, e o mais frequentemente omitido. É também onde os incidentes moram: backups offline que "existem", mas nunca foram restaurados; acesso de fornecedores que é "intermediado", exceto por aquele modem legado.

### 2.6 Priorizar pela consequência

A importância de uma prática depende de quanto ela limita a perda do serviço essencial. Pondere as práticas pela consequência — não por quantas referências de frameworks elas mapeiam — e priorize as lacunas em que o peso é alto e a pontuação verificada é baixa. Os pesos são julgamentos; registre quem os definiu (Capítulo 1). Para Merrow Bay, o fórum concordou que MFA no acesso remoto, segmentação TI/TO, backups offline testados e acesso intermediado de fornecedores têm o maior peso, porque cada um limita diretamente um caminho para a perda do fornecimento observado em incidentes públicos — o comprometimento do acesso remoto de um sistema de tratamento de água foi objeto de um alerta conjunto de 2021 ([CISA, AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a)), ainda que o relato desse evento específico tenha sido contestado depois ([WUSF, 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)); a fraqueza de acesso remoto que o alerta descreveu continua sendo uma preocupação de projeto válida em qualquer caso.

### 2.7 Exemplo resolvido: as autoavaliações de quatro operadores (sintético)

O Merrow Bay Resilience Forum pediu a quatro operadores que autoavaliassem oito práticas, pontuando 0 (ausente), 1 (parcial) ou 2 (implementada), e que graduassem as evidências como V, D ou S. A tarefa do especialista é transformar as respostas num retrato regional sem ofender ninguém nem acreditar em tudo. Em vez de "rejeitar" as declarações, o Laboratório 2 lhes dá crédito **provisório** zero até que sejam testadas, e meio crédito aos documentos. Esses créditos são uma escolha de política; o EX007 testa seu efeito.

Duas convenções moldam os resultados. Os pesos de cada prática foram acordados pelo fórum, então o retrato regional reflete o julgamento dele sobre quais práticas limitam a perda do fornecimento. E os operadores são nomeados neste exemplo apenas porque ele é sintético; um relatório real do fórum normalmente mostraria a cada operador a sua própria linha e daria aos demais apenas o resumo regional. O especialista deve enviar a cada operador seu resultado em privado antes da reunião do fórum, para que ninguém descubra uma lacuna desconfortável diante dos pares.

### 2.8 Atividade prática: cobertura declarada versus verificada

```python
# Lab 2 - claimed versus verified baseline coverage, weighted by consequence (offline, standard library only)
# Synthetic: four Merrow Bay operators self-assess eight baseline practices (0 = absent, 1 = partial, 2 = in place)
# and say what evidence backs each answer: V = verified by test or inspection, D = document only, S = statement only.
PRACTICES = {  # practice -> consequence weight (how much it limits loss of the essential service; invented)
    "MFA on remote access": 3, "asset inventory incl. OT": 2, "IT/OT segmentation": 3,
    "offline backups restored in test": 3, "central logging retained 90d": 1,
    "incident plan exercised in 12 months": 2, "vendor access brokered and recorded": 3,
    "default credentials removed": 2,
}
ANSWERS = {  # operator -> list of (score, evidence) in PRACTICES order
    "Merrow Water":     [(2,"V"),(1,"D"),(2,"D"),(2,"S"),(1,"V"),(2,"V"),(1,"S"),(2,"S")],
    "Merrow Health":    [(2,"V"),(1,"D"),(1,"D"),(2,"V"),(2,"V"),(2,"D"),(1,"D"),(1,"S")],
    "Merrow Energy":    [(2,"V"),(2,"V"),(2,"V"),(1,"D"),(2,"V"),(2,"V"),(2,"D"),(2,"D")],
    "Port of Merrow":   [(2,"S"),(0,"S"),(1,"S"),(2,"S"),(1,"D"),(1,"S"),(0,"S"),(2,"S")],
}
CREDIT = {"V": 1.0, "D": 0.5, "S": 0.0}  # how much of a claimed score we accept without further testing
W = list(PRACTICES.values()); maxw = 2 * sum(W)
print(f"{'operator':16s} claimed  verified  gap(weighted points)")
gaps = []
for op, ans in ANSWERS.items():
    claimed = sum(w * s for w, (s, e) in zip(W, ans))
    verified = sum(w * s * CREDIT[e] for w, (s, e) in zip(W, ans))
    print(f"{op:16s} {claimed/maxw:6.0%}   {verified/maxw:6.0%}   {maxw-verified:5.1f}")
    for (name, w), (s, e) in zip(PRACTICES.items(), ans):
        unverified = w * (2 - s * CREDIT[e])
        if w == 3 and unverified >= 3:
            gaps.append((unverified, op, name, s, e))
print("\nHigh-consequence practices with >= 3 unverified weighted points:")
for u, op, name, s, e in sorted(gaps, reverse=True):
    print(f"  {u:4.1f}  {op:16s} {name}  (claimed {s}, evidence {e})")
```

Saída esperada:

```text
operator         claimed  verified  gap(weighted points)
Merrow Water        84%      39%    23.0
Merrow Health       74%      53%    18.0
Merrow Energy       92%      75%     9.5
Port of Merrow      58%       1%    37.5

High-consequence practices with >= 3 unverified weighted points:
   6.0  Port of Merrow   vendor access brokered and recorded  (claimed 0, evidence S)
   6.0  Port of Merrow   offline backups restored in test  (claimed 2, evidence S)
   6.0  Port of Merrow   MFA on remote access  (claimed 2, evidence S)
   6.0  Port of Merrow   IT/OT segmentation  (claimed 1, evidence S)
   6.0  Merrow Water     vendor access brokered and recorded  (claimed 1, evidence S)
   6.0  Merrow Water     offline backups restored in test  (claimed 2, evidence S)
   4.5  Merrow Health    vendor access brokered and recorded  (claimed 1, evidence D)
   4.5  Merrow Health    IT/OT segmentation  (claimed 1, evidence D)
   4.5  Merrow Energy    offline backups restored in test  (claimed 1, evidence D)
   3.0  Merrow Water     IT/OT segmentation  (claimed 2, evidence D)
   3.0  Merrow Energy    vendor access brokered and recorded  (claimed 2, evidence D)
```

**Interpretação.** A cobertura declarada vai de 58% a 92%; a verificada, de 1% a 75%. A posição da própria Merrow Water — 84% declarados, 39% verificados — é desconfortável para seu especialista: as duas lacunas de maior peso são declarações de que os backups offline são restauráveis e de que o acesso de fornecedores é intermediado. O 1% do Port of Merrow não significa que o porto não tenha segurança; significa que nada foi demonstrado. A lista priorizada é um **plano de verificação** antes de ser um plano de remediação: cada um dos onze itens se apoia numa declaração ou num documento, então a primeira ação para cada um é testar a alegação — barato em comparação com comprar controles, e às vezes suficiente para fechar a lacuna. A Merrow Energy, com evidências majoritariamente verificadas, é a melhor fonte de método prático da região — um ativo para o fórum, e não apenas uma pontuação.

### 2.9 Criticar uma prática comum

Espera-se que os especialistas questionem práticas que persistem por hábito. Tome o "teste de intrusão de TO" anual escrito em muitos contratos. Ele frequentemente produz uma lista de constatações sobre uma amostra de sistemas numa janela curta, usando técnicas que precisam ser contidas para evitar perturbar o processo, e costuma ter um escopo que evita os ativos de maior consequência. Alternativas com melhor valor de evidência incluem: uma revisão orientada pela consequência que parte do pior resultado físico crível e volta até os caminhos digitais que poderiam causá-lo ([Idaho National Laboratory, CCE](https://inl.gov/national-security/cce/)); a conciliação contínua dos registros de acesso remoto e de mudanças; e testes num ambiente de bancada representativo em vez da planta em operação (Capítulo 6). A crítica não é "nunca teste"; é "escolha o método de evidência que responde à pergunta que o conselho está de fato fazendo".

### 2.10 Erros comuns e limites

- Tratar um mapeamento de framework como evidência de implementação.
- Relatar apenas a cobertura declarada, ou fazer a média entre a declarada e a verificada num único número.
- Copiar a prática de outro setor sem verificar o tempo até o dano e as restrições de segurança operacional.
- Tratar a linha de base mais curta como o programa inteiro, ou o catálogo mais longo como uma lista de tarefas.
- Supor que o regulador de um setor aceitará evidências desenhadas para outro.
- Ponderar as práticas por quantas normas as mencionam, e não pela consequência.

O limite de qualquer linha de base é que ela descreve defesas que são comuns porque os ataques foram comuns. Ela diz pouco sobre caminhos raros, direcionados ou novos, e é por isso que os Capítulos 4 e 5 acrescentam a análise orientada pela consequência.

### Exercícios — capítulo 2

**EX006 — Mapeie uma prática entre frameworks.** *Objetivo:* ligar uma prática a obrigações e orientações sem confundi-las. *Insumos:* "acesso de fornecedores intermediado e registrado" na Merrow Water. *Restrições:* usar apenas as fontes citadas nas §2.2–2.3; não citar textos de normas pagas. *Passos:* (1) identificar a(s) função(ões) do CSF 2.0 e o objetivo do CAF que ela apoia; (2) declarar se ela aparece como meta transversal da CISA; (3) explicar como a ideia de zonas e conduítes da IEC 62443 a enquadra; (4) declarar, sem dar aconselhamento jurídico, se ela é uma obrigação legal para uma concessionária de água na sua jurisdição e como você verificaria isso. *Evidência esperada:* uma tabela curta de mapeamento e um parágrafo. *Rubrica:* 3 = mapeamentos corretos no nível de função e objetivo, obrigações mantidas separadas das orientações, um caminho de verificação por meio de aconselhamento jurídico declarado; 2 = um mapeamento errado; 1 = trata orientação como lei; 0 = nada.

**EX007 — Mude a política de evidências.** *Objetivo:* testar como uma política de pontuação muda o retrato. *Insumos:* Laboratório 2. *Restrições:* mudar o crédito de uma declaração de 0,0 para 0,25 e nada mais. *Passos:* (1) reexecutar e relatar a cobertura verificada de cada operador; (2) dizer quais conclusões da §2.8 sobrevivem; (3) defender uma política de crédito para o relatório do fórum. *Evidência esperada:* saídas e argumento de 200 palavras. *Rubrica:* 3 = números corretos, reconhecimento de que a ordem do ranking e a prioridade de testar as declarações sobrevivem, uma política defendida a partir do uso do relatório; 2 = números certos, argumento fraco; 1 = não executado; 0 = nada.

**EX008 — Plano de verificação.** *Objetivo:* transformar as maiores lacunas em testes. *Insumos:* os três itens de maior peso da Merrow Water na lista do Laboratório 2. *Restrições:* os testes precisam ser seguros para a planta em operação; nomear as evidências que contariam como V. *Passos:* para cada item, dar o método (teste, inspeção, conciliação), o responsável, as condições de segurança, o critério de aprovação e o custo esperado em dias de trabalho. *Evidência esperada:* tabela. *Rubrica:* 3 = os métodos testam genuinamente a realidade (por exemplo, a restauração cronometrada de um sistema nomeado num host isolado; a conciliação dos logs do intermediador com as sessões do firewall ao longo de 30 dias), condições de segurança explícitas, critérios de aprovação mensuráveis; 2 = um método apenas documental; 1 = "revisar a política"; 0 = nada.

**EX009 — Operador sob vários regimes.** *Objetivo:* planejar as evidências para regimes sobrepostos. *Insumos:* uma multiconcessionária sintética na UE que fornece água, opera uma pequena rede de distribuição de eletricidade e tem uma subsidiária de pagamentos. *Restrições:* identificar os regimes da §2.3 que podem se aplicar, sem decidir o escopo jurídico. *Passos:* (1) listar os regimes candidatos e por que cada um poderia se aplicar; (2) desenhar um único conjunto interno de controles com mapeamentos; (3) identificar os relógios de notificação de incidentes que precisam ser conciliados; (4) declarar o que você perguntaria ao jurídico. *Evidência esperada:* plano de uma página. *Rubrica:* 3 = regimes candidatos plausíveis, um conjunto de controles com mapeamentos, relógios de notificação identificados como um problema de projeto, perguntas jurídicas específicas; 2 = mapeamentos vagos; 1 = apresenta conclusões jurídicas como fato; 0 = nada.

**EX010 — Critique uma prática.** *Objetivo:* defender um método de evidência melhor. *Insumos:* o contrato da Merrow Health exige um "teste de intrusão externo anual da rede clínica". *Restrições:* 300 palavras; respeitar a segurança dos pacientes. *Passos:* (1) declarar a pergunta que o conselho quer ver respondida; (2) dizer o que o teste anual responde e o que não responde; (3) propor um portfólio alternativo de evidências; (4) declarar seus limites. *Evidência esperada:* memorando. *Rubrica:* 3 = pergunta explícita, limites dos testes pontuais identificados (amostra, janela, contenção das técnicas, dispositivos excluídos), alternativas ajustadas à pergunta, limites honestos; 2 = crítica sem alternativa; 1 = rejeita os testes por completo; 0 = nada.

### Síntese do capítulo

A prática atual é a sobreposição entre obrigação, orientação e prática demonstrada pelos pares, e cada uma tem um peso diferente. Conheça os frameworks de resultados, as linhas de base priorizadas, os catálogos de controles e as normas industriais, e saiba quais regimes obrigam a sua organização e que evidências cada um espera. Não copie práticas entre setores sem verificar o tempo até o dano, a física, a regulação e a força de trabalho. Gradue as evidências como verificadas, documentadas ou declarações, relate a lacuna com honestidade, pondere as práticas pela consequência e transforme as maiores lacunas em verificação antes da remediação. Questione as práticas habituais perguntando a qual pergunta suas evidências respondem.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Infraestrutura crítica e segurança setorial: evidências especializadas

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

1. Identificar as fontes de evidência disponíveis num ambiente misto de TI/TO e o que cada uma pode e não pode mostrar.
2. Reconstruir uma linha do tempo a partir de fontes cujos relógios discordam, usando eventos-âncora, e declarar a incerteza que resta.
3. Planejar a preservação de evidências sem pôr em risco o processo físico.
4. Gerar explicações concorrentes e identificar as evidências que discriminariam entre elas.
5. Escrever constatações que separem observação, inferência e julgamento, num nível de confiança que as evidências sustentem.
6. Cumprir as obrigações de notificação sem exagerar o que se sabe.

O Capítulo 2 graduou as evidências de que os controles estão implementados. Este capítulo trata das evidências sobre **o que aconteceu** — o material que um especialista leva a uma revisão de incidente, a um regulador, a uma seguradora ou a um tribunal. O Capítulo 6 aplica a mesma disciplina aos testes planejados.

### 3.1 O dever probatório do especialista

Quando algo inexplicado acontece num serviço essencial, muitas pessoas formarão uma história depressa: o fornecedor, os operadores, a imprensa, o regulador. O dever do especialista é estabelecer o que as evidências sustentam, com que confiança e o que continua desconhecido — e manter essas coisas separadas sob pressão. As recomendações de resposta a incidentes do NIST enquadram a resposta como parte da gestão de riscos como um todo, com a preparação, a detecção, a análise e a melhoria ligadas à governança ([NIST SP 800-61 Rev. 3, 2025](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). Para a TO, a NIST SP 800-82 Rev. 3 acrescenta que a resposta deve proteger primeiro a segurança operacional e o processo ([NIST, 2023](https://doi.org/10.6028/NIST.SP.800-82r3)).

O caso do setor de água do Capítulo 2 mostra por que isso importa. Em fevereiro de 2021, um alerta descreveu o comprometimento do sistema de controle de uma instalação de tratamento de água dos EUA por meio de um software de acesso remoto ([CISA, AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a)). Em 2023, noticiou-se que o ex-administrador da cidade teria dito que o evento provavelmente foi um erro de um funcionário, e não uma intrusão externa ([WUSF, 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)). Seja qual for a verdade, o episódio mostra como um relato público inicial pode se cristalizar antes que as evidências estejam completas, e quanto a análise posterior depende do que foi preservado na época.

### 3.2 Fontes de evidência num ambiente misto

| Fonte | O que pode mostrar | Fraquezas típicas |
|---|---|---|
| Logs de firewall e de VPN | Sessões, contas, endereços e horários na fronteira | Retenção curta; o NAT esconde os hosts; sem conteúdo |
| Logs do provedor de identidade e do jump host | Quem se autenticou, de onde, quais sessões | Contas compartilhadas ou de serviço frustram a atribuição |
| Logs de host Windows/Linux em IHMs e estações de engenharia | Logons, processos, alterações de arquivos | Frequentemente desabilitados em hosts de TO; buffers locais pequenos são sobrescritos |
| Historiador SCADA | Valores do processo e comandos dos operadores com etiquetas de origem | Horário do relógio do servidor do historiador; a compressão pode descartar eventos curtos; a "origem" pode ser uma estação, não uma pessoa |
| Estado e arquivos de projeto do controlador (CLP) | Lógica e configuração atuais; às vezes contadores de alterações | A leitura pode exigir ferramentas do fornecedor; a interação online traz risco ao processo |
| Capturas de rede na zona de controle | Exatamente quais comandos de protocolo foram enviados | Raramente coletadas de forma contínua; volumosas |
| Livros de registro dos operadores e passagens de turno | Observações e decisões humanas | Resolução de minutos ou pior; escritos depois do fato; relógios de parede não sincronizados |
| Entrevistas | Intenção, contexto, ações não registradas | A memória reconstrói; os incentivos moldam os relatos |
| Registros de fornecedores e prestadores | Sessões remotas, manutenção, atualizações | Mantidos por terceiros; o acesso exige cláusulas contratuais |

Um especialista conhece essas fontes **antes** de um incidente e corrige as fraquezas que mais importam: tempo sincronizado, retenção mais longa dos logs de fronteira e de identidade, contas nominais e acesso contratual aos registros dos fornecedores. O catálogo de controles do NIST inclui requisitos de conteúdo, retenção e carimbo de tempo dos registros de auditoria exatamente por esse motivo ([NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)).

### 3.3 O tempo é evidência

A ordem dos eventos costuma decidir a explicação: a sessão remota começou antes ou depois de o setpoint mudar? Cada fonte registra o tempo pelo seu próprio relógio, e os relógios de TO frequentemente estão dessincronizados, derivados ou ajustados à mão. Três práticas tornam as linhas do tempo defensáveis:

1. **Escolha um relógio de referência** cuja sincronização você consiga verificar (por exemplo, um firewall sincronizado com uma fonte de tempo conhecida e conferido) e expresse todos os eventos nele.
2. **Estime o deslocamento de cada fonte a partir de eventos-âncora** — um único momento do mundo real registrado por duas fontes, como as duas pontas da mesma sessão de rede ou uma consulta de sincronização passando por um firewall. Duas âncoras independentes por fonte são melhores do que uma; a discordância entre elas revela deriva.
3. **Declare a incerteza residual** de cada fonte — a precisão da própria âncora, a resolução (um registro manuscrito pode ter apenas minutos) e a deriva ao longo do intervalo — e verifique se alguma conclusão depende de uma ordenação mais próxima do que essa incerteza.

### 3.4 Preservação sem dano

A preservação de evidências em TO não pode criar o dano que ela investiga. Princípios:

- **Segurança operacional e processo em primeiro lugar.** O responsável pelas operações decide se um sistema pode ser tocado. As etapas de preservação são planejadas com ele, não impostas.
- **Colete primeiro da fonte menos intrusiva.** Logs de fronteira, logs de identidade, exportações do historiador e backups geralmente podem ser coletados sem tocar na rede de controle. O estado do controlador deve ser lido com as ferramentas suportadas pelo fornecedor, sob controle de mudanças, ou não ser lido até que o processo esteja seguro.
- **Preserve as evidências voláteis quando for seguro.** A memória e o estado das conexões ativas em IHMs e jump hosts baseados em Windows desaparecem com a reinicialização; capture-os se o host puder ser dispensado.
- **Registre a cadeia de custódia.** Quem coletou o quê, quando, como, com quais hashes — a mesma disciplina de qualquer trabalho forense. Um hash criptográfico como o SHA-256 ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)) mostra depois que um arquivo exportado não foi alterado.
- **Peça cedo aos fornecedores.** Os registros de sessões dos fornecedores e os logs de suporte remoto costumam ser sobrescritos segundo o cronograma do próprio fornecedor.

### 3.5 Explicações concorrentes

Uma mudança de setpoint com uma sessão remota por perto convida à história "um atacante fez isso". Um especialista lista toda explicação que poderia produzir as mesmas evidências e pergunta o que as distinguiria — o método das múltiplas hipóteses de trabalho ([Chamberlin, reimpressão de 1965](https://doi.org/10.1126/science.148.3671.754)). Para uma mudança de dosagem inexplicada, os candidatos incluem um intruso externo usando uma credencial roubada, um engenheiro legítimo do fornecedor fazendo uma mudança não registrada, um erro de um operador numa IHM local, um script ou receita automatizados, um erro de etiquetagem do historiador e uma falha de instrumento que o operador corrigiu manualmente. Cada um prevê rastros diferentes: a mudança de um intruso deveria vir da estação remota depois do logon remoto; o trabalho planejado de um fornecedor deveria corresponder a um chamado e a um padrão visto em outros locais; um erro de operador deveria vir de uma estação local; uma receita deveria se repetir segundo um cronograma; um erro de etiquetagem deveria discordar do registro do próprio controlador.

### 3.6 Escrever constatações

Uma constatação tem quatro partes: a **observação** com sua fonte; a **inferência** com seus pressupostos; a **confiança**, em palavras que correspondam a faixas explícitas se a sua organização as usar; e a **consequência** para as decisões. Por exemplo: "O historiador registra uma mudança do setpoint de dosagem de 1,8 para 2,6 mg/L atribuída à estação HMI-JH2 às 02:23:03 (horário do firewall, ±10 s). A estação HMI-JH2 é o cliente de IHM no jump host JH-2. A única sessão interativa no JH-2 naquele momento era a da conta vendor-svc, que se conectou pela VPN a partir das 02:11:40. Avaliamos com confiança moderada que a mudança foi feita dentro da sessão vendor-svc; ainda não podemos dizer quem usou essa conta. A conta é compartilhada por quatro engenheiros da Corvane." Isso é muito mais útil para um tomador de decisão do que "a conta do fornecedor foi comprometida".

### 3.7 Notificar sob obrigação

Muitos regimes exigem hoje a notificação precoce, em etapas, de incidentes significativos. A NIS2, por exemplo, prevê um alerta precoce, uma notificação mais completa e um relatório final em prazos fixos ([Diretiva (UE) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/)); a NERC CIP e outras regras setoriais têm seus próprios relógios. As notificações precoces precisam ser feitas antes que os fatos sejam conhecidos. A contribuição do especialista é torná-las **exatas quanto à incerteza**: dizer o que foi observado, o que está sendo investigado e o que ainda não se sabe, e evitar uma atribuição que evidências posteriores possam reverter. Acompanhe cada declaração externa para que as notificações posteriores possam corrigir explicitamente as anteriores.

### 3.8 Exemplo resolvido: uma noite em Hollin (sintético)

Na estação de tratamento de Hollin, o setpoint de dosagem de cloro subiu brevemente de 1,8 para 2,6 mg/L e voltou em menos de um minuto. O registro manuscrito do operador diz que ele notou um alarme às "02:20" e restaurou o setpoint. O especialista reuniu os registros do firewall, do jump host e do historiador. Lido de forma ingênua, o historiador mostra a mudança às 02:06, *antes* de a sessão VPN vendor-svc começar, às 02:11 — o que inocentaria a sessão remota. Mas sabe-se que o relógio do servidor do historiador não está sincronizado. Existem duas âncoras: o início de uma sessão TCP visto tanto pelo firewall quanto pelo jump host, e a própria consulta de sincronização do historiador passando pelo firewall.

### 3.9 Atividade prática: linha do tempo entre relógios que discordam

```python
# Lab 3 - reconstructing a timeline from sources whose clocks disagree (offline, standard library only)
# Synthetic: Merrow Water, Hollin treatment works, night of an unexplained chlorine dosing setpoint change.
# Each source records time in its own clock. Anchor events were seen by two sources at the same real moment.
from datetime import datetime, timedelta
T = lambda s: datetime.strptime(s, "%H:%M:%S")
EVENTS = [  # (source, local clock time, description)
    ("firewall",  "02:11:40", "VPN session opened for account vendor-svc"),
    ("firewall",  "02:13:05", "RDP from VPN pool to jump host JH-2 allowed"),
    ("jumphost",  "02:20:31", "interactive logon vendor-svc on JH-2"),
    ("jumphost",  "02:22:58", "HMI client launched on JH-2"),
    ("historian", "02:06:12", "dosing setpoint changed 1.8 -> 2.6 mg/L, source HMI-JH2"),
    ("historian", "02:06:50", "dosing setpoint restored 2.6 -> 1.8 mg/L, source HMI-OPS1"),
    ("ops-log",   "02:20",    "operator notices dosing alarm, restores setpoint (handwritten, minute only)"),
    ("firewall",  "02:31:10", "VPN session closed for vendor-svc"),
]
ANCHORS = [  # the same real moment seen by two sources: (source_a, time_a, source_b, time_b)
    ("firewall", "02:13:07", "jumphost", "02:20:33"),   # TCP session start seen at both ends
    ("firewall", "02:14:30", "historian", "01:57:39"),  # historian's NTP query passing the firewall
]
offset = {"firewall": timedelta(0)}  # firewall is the reference clock (NTP-synchronized, checked)
for a, ta, b, tb in ANCHORS:
    offset[b] = (T(ta) - T(tb)) + offset[a]
offset["ops-log"] = timedelta(0)  # a handwritten log has no known offset, only minute resolution
def show(title, rows):
    print(title)
    for t, src, d in rows: print(f"  {t.strftime('%H:%M:%S')}  {src:9s} {d}")
naive = sorted((T(t) if len(t) > 5 else T(t + ':00'), s, d) for s, t, d in EVENTS)
show("Naive order (raw clocks):", naive)
fixed = sorted(((T(t) if len(t) > 5 else T(t + ':00')) + offset[s], s, d) for s, t, d in EVENTS)
show("Corrected to firewall time:", fixed)
print("offsets:", {k: int(v.total_seconds()) for k, v in offset.items()}, "seconds")
```

Saída esperada:

```text
Naive order (raw clocks):
  02:06:12  historian dosing setpoint changed 1.8 -> 2.6 mg/L, source HMI-JH2
  02:06:50  historian dosing setpoint restored 2.6 -> 1.8 mg/L, source HMI-OPS1
  02:11:40  firewall  VPN session opened for account vendor-svc
  02:13:05  firewall  RDP from VPN pool to jump host JH-2 allowed
  02:20:00  ops-log   operator notices dosing alarm, restores setpoint (handwritten, minute only)
  02:20:31  jumphost  interactive logon vendor-svc on JH-2
  02:22:58  jumphost  HMI client launched on JH-2
  02:31:10  firewall  VPN session closed for vendor-svc
Corrected to firewall time:
  02:11:40  firewall  VPN session opened for account vendor-svc
  02:13:05  firewall  RDP from VPN pool to jump host JH-2 allowed
  02:13:05  jumphost  interactive logon vendor-svc on JH-2
  02:15:32  jumphost  HMI client launched on JH-2
  02:20:00  ops-log   operator notices dosing alarm, restores setpoint (handwritten, minute only)
  02:23:03  historian dosing setpoint changed 1.8 -> 2.6 mg/L, source HMI-JH2
  02:23:41  historian dosing setpoint restored 2.6 -> 1.8 mg/L, source HMI-OPS1
  02:31:10  firewall  VPN session closed for vendor-svc
offsets: {'firewall': 0, 'jumphost': -446, 'historian': 1011, 'ops-log': 0} seconds
```

**Interpretação.** O jump host está 446 segundos (7 min 26 s) adiantado em relação ao firewall; o historiador, 1.011 segundos (16 min 51 s) atrasado. Corrigida, a ordem se inverte: a sessão vendor-svc abre às 02:11:40, o logon no jump host segue a conexão RDP permitida no mesmo segundo (uma verificação de consistência que apoia a primeira âncora), o cliente de IHM inicia às 02:15:32 e a mudança de setpoint a partir da estação HMI-JH2 ocorre às 02:23:03, com uma restauração a partir da estação dos operadores 38 segundos depois. A linha do tempo ingênua teria inocentado a sessão remota; a corrigida coloca a mudança dentro dela. Note a inconsistência que resta: o "02:20" do registro manuscrito está três minutos *antes* da mudança que ele descreve. A explicação provável é que o relógio de parede da sala de controle esteja atrasado, mas isso é uma inferência; deve ser conferido com o relógio de parede e registrado, e não "corrigido" em silêncio. A constatação continua sendo sobre a **sessão**, não sobre uma pessoa, e as explicações concorrentes (§3.5) — a mudança legítima, mas não registrada, de um engenheiro do fornecedor versus o mau uso da conta compartilhada — continuam em aberto.

### 3.10 Erros comuns e limites

- Ordenar eventos de fontes diferentes pelos carimbos de tempo brutos.
- Corrigir relógios com uma única âncora e nunca conferi-la com uma segunda.
- Tratar uma etiqueta de "origem" do historiador como uma pessoa.
- Tocar nos controladores para coletar evidências sem a decisão do responsável pelas operações.
- Deixar a primeira história plausível definir quais evidências são coletadas.
- Escrever "comprometido" ou "ataque" em notificações precoces quando as evidências sustentam apenas "mudança inexplicada durante uma sessão remota".
- Esquecer que os registros dos fornecedores expiram.

O limite é que as evidências podem estreitar as explicações, mas raramente eliminam todas menos uma. Um especialista relata quais explicações restam e o que as separaria; a decisão de agir — por exemplo, suspender o acesso de um fornecedor — pode e muitas vezes deve ser tomada antes que a atribuição esteja resolvida.

### Exercícios — capítulo 3

**EX011 — Robustez da ordem.** *Objetivo:* quantificar quanto uma conclusão da linha do tempo depende de uma âncora. *Insumos:* Laboratório 3. *Restrições:* considerar erros apenas na âncora do historiador. *Passos:* (1) calcular quantos segundos mais cedo a mudança de setpoint corrigida teria de ocorrer para preceder o início do cliente de IHM no JH-2; (2) mudar em um minuto o horário de firewall da âncora do historiador (02:14:30 → 02:15:30), reexecutar e relatar se a ordem muda; (3) declarar que evidência independente confirmaria o deslocamento do historiador. *Evidência esperada:* cálculo, saída da reexecução e parágrafo. *Rubrica:* 3 = margem calculada (451 s), a reexecução mostra que a ordem não muda, uma segunda âncora independente proposta; 2 = falta uma parte; 1 = não executado; 0 = nada.

**EX012 — Plano de preservação.** *Objetivo:* planejar uma coleta de evidências segura. *Insumos:* o evento de Hollin. *Restrições:* a planta precisa continuar produzindo água; o responsável pelas operações tem autoridade sobre os sistemas de controle. *Passos:* listar as fontes na ordem de coleta, com o método, quem aprova, a volatilidade e o risco ao processo; incluir a cadeia de custódia e os pedidos aos fornecedores. *Evidência esperada:* tabela e uma justificativa de um parágrafo. *Rubrica:* 3 = menos intrusiva primeiro, captura volátil do JH-2 antes de qualquer reinicialização, leituras do controlador com aprovação das operações e ferramentas do fornecedor, hashes e custódia, registros de sessão da Corvane pedidos imediatamente; 2 = ordem parcialmente errada; 1 = põe o processo em risco; 0 = nada.

**EX013 — Escreva a constatação.** *Objetivo:* separar observação, inferência, confiança e consequência. *Insumos:* a saída do Laboratório 3. *Restrições:* 200 palavras; nenhuma atribuição a uma pessoa. *Passos:* escrever a constatação para o conselho e uma versão de uma frase para a notificação precoce ao regulador. *Evidência esperada:* os dois textos. *Rubrica:* 3 = observações com fonte, base de relógio e incerteza, inferência explícita, confiança declarada, consequência para as decisões (por exemplo, suspender a conta compartilhada) clara, frase ao regulador exata quanto ao que não se sabe; 2 = um elemento misturado; 1 = afirma o comprometimento como fato; 0 = nada.

**EX014 — Evidências discriminantes.** *Objetivo:* aplicar as múltiplas hipóteses de trabalho. *Insumos:* as seis explicações candidatas da §3.5. *Restrições:* para cada uma, uma previsão que as outras não compartilhem. *Passos:* montar uma tabela com a explicação, a previsão distintiva, a fonte de evidência e o estado atual (apoiada, contrariada, em aberto). *Evidência esperada:* tabela. *Rubrica:* 3 = previsões genuinamente discriminantes, estados coerentes com o Laboratório 3 (erro do operador numa estação local contrariado para a própria mudança; legítima do fornecedor versus mau uso em aberto), próximas evidências identificadas; 2 = algumas previsões compartilhadas; 1 = apenas uma lista; 0 = nada.

**EX015 — Notificação em etapas.** *Objetivo:* redigir declarações externas que sobrevivam às evidências posteriores. *Insumos:* o evento de Hollin; suponha que a Merrow Water esteja sujeita a um regime de notificação de incidentes em etapas semelhante ao do artigo 23 da NIS2. *Restrições:* não interpretar a lei real para uma entidade real; usar marcadores para os prazos. *Passos:* redigir o alerta precoce, a notificação e o esboço do relatório final, mostrando como cada um corrige ou amplia o anterior. *Evidência esperada:* três textos curtos. *Rubrica:* 3 = alerta precoce factual e explícito quanto à incerteza, a notificação acrescenta a linha do tempo corrigida e as ações, o esboço do relatório final inclui a causa raiz, as correções e as lições; 2 = o texto inicial exagera; 1 = atribuição afirmada; 0 = nada.

### Síntese do capítulo

As evidências especializadas são o material em que se apoiam as decisões e a responsabilização. Conheça suas fontes antes de um incidente e corrija as fraquezas que importam — tempo, retenção, contas nominais e acesso aos fornecedores. Trate o tempo como evidência: escolha um relógio de referência, estime os deslocamentos a partir de âncoras e declare a incerteza residual. Preserve sem prejudicar o processo, a menos intrusiva primeiro, com cadeia de custódia. Gere explicações concorrentes e busque as evidências que discriminam entre elas. Escreva constatações que mantenham separadas a observação, a inferência, a confiança e a consequência, e notifique cedo de um modo que as evidências posteriores ampliem, em vez de contradizer.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 12

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Risco avançado e ética

### Objetivos de aprendizagem e conexão

Ao final deste capítulo, você deverá ser capaz de:

1. Construir uma estimativa quantificada de risco com incerteza explícita de frequência e de gravidade, e lê-la como uma curva de excedência de perdas, e não como um número único.
2. Expressar o apetite e a tolerância a risco em unidades de serviço, com limites sobre a cauda, e não apenas sobre a média.
3. Elicitar e documentar o julgamento de especialistas de modo que ele possa ser contestado.
4. Analisar quem arca com o risco residual e reconhecer quando uma opção melhor na média é pior para um grupo específico.
5. Aplicar princípios éticos reconhecidos às decisões, aos testes e à divulgação de segurança em serviços essenciais.

O Capítulo 1 comparou opções numa tabela de cenários. Este capítulo substitui a tabela por distribuições e acrescenta a pergunta que as tabelas de decisão escondem: *para quem* uma opção é melhor? O Capítulo 8 aplica ambas as coisas a casos em que toda escolha prejudica alguém.

### 4.1 Por que estimativas pontuais enganam

Uma entrada de registro de riscos como "probabilidade 3, impacto 4, escore 12" esconde três coisas de que uma decisão precisa: com que frequência, quão grave e quão incerto. As orientações de avaliação de riscos do NIST descrevem o risco como função da ameaça, da vulnerabilidade, da probabilidade e do impacto, e advertem que as avaliações precisam declarar pressupostos e incerteza ([NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)). Multiplicar escores ordinais também faz aritmética com números que são apenas rótulos.

Um modelo mínimo melhor tem duas partes: uma distribuição de **frequência** para quantos eventos de perda ocorrem num ano e uma distribuição de **gravidade** para quão grave cada um é. Na infraestrutura, a gravidade costuma ser assimétrica à direita: a maioria das interrupções é curta, e poucas são muito longas. A distribuição lognormal é uma escolha comum e simples para grandezas assim; seus parâmetros devem ser ancorados em evidências (durações de interrupções passadas, resultados de exercícios, incidentes de pares), e a própria escolha deve ser registrada como um pressuposto. Simular muitos anos dá uma distribuição da perda anual, que você pode resumir de três modos: a **média** (o que você paga em média), a **probabilidade de exceder** limiares que importam e um **percentil alto**, como o 99º (um ano ruim de uma vez em cem anos). Plotar a probabilidade de excedência contra a perda dá a **curva de excedência de perdas** (LEC, na sigla em inglês).

### 4.2 Apetite e tolerância em unidades de serviço

O **apetite a risco** é a quantidade e o tipo de risco que uma organização está disposta a buscar ou a reter; a **tolerância** fixa os limites da variação aceitável. O NIST CSF 2.0 coloca ambos sob a governança ([NIST, 2024](https://doi.org/10.6028/NIST.CSWP.29)). Para um serviço essencial, as declarações de apetite devem estar em unidades de serviço e devem restringir a cauda. Por exemplo (sintético): "A Merrow Water não aceitará uma chance anual superior a 2% de uma interrupção de origem cibernética que exceda um milhão de domicílios-hora de fornecimento, nem nenhum cenário crível em que os domicílios de um único distrito fiquem sem fornecimento por mais de 48 horas sem provisão alternativa." A primeira cláusula limita a LEC; a segunda limita a *distribuição* — um tema ao qual voltamos na §4.5.

### 4.3 O julgamento de especialistas como evidência

Onde os dados são escassos, os parâmetros de frequência e de gravidade vêm de pessoas. A elicitação estruturada — definir as grandezas com precisão, treinar os especialistas em calibração, pedir quantis em vez de valores únicos, agregar vários especialistas e registrar a justificativa — torna o julgamento inspecionável ([O'Hagan et al., 2006](https://doi.org/10.1002/0470033312)). Regras práticas para o especialista: pergunte sobre grandezas observáveis ("quantas horas para restaurar o fornecimento de Upper Merrow após a perda total do SCADA?") em vez de probabilidades abstratas; peça primeiro um intervalo de 90% e depois uma mediana; peça as taxas de base de operadores comparáveis; e registre a pessoa, a data, a pergunta e a justificativa, para que a estimativa possa ser revista quando chegarem evidências.

### 4.4 Ética na segurança de serviços essenciais

As decisões de segurança na infraestrutura distribuem danos. Vários frameworks estabelecidos ajudam a raciocinar sobre elas:

- O **Menlo Report** adaptou os princípios da ética em pesquisa — respeito às pessoas, beneficência, justiça — à pesquisa em tecnologia da informação e comunicação e acrescentou o respeito à lei e ao interesse público ([Dittrich e Kenneally, 2012](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf)). Seus princípios se aplicam diretamente aos testes e à coleta de dados em ambientes operacionais.
- Códigos profissionais como o [Código de Ética da ACM](https://www.acm.org/code-of-ethics) e o [Código de Ética para Engenheiros da NSPE](https://www.nspe.org/resources/ethics/code-ethics) colocam o bem-estar e a segurança do público acima dos interesses do empregador ou do cliente, e exigem honestidade sobre os limites da própria competência e da segurança de um sistema.
- A legislação de proteção de dados impõe deveres ao tratamento de dados pessoais no monitoramento de segurança e no tratamento de incidentes ([GDPR, Regulamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)); no Brasil, a [LGPD, Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), fiscalizada pela ANPD, exige uma base legal para o tratamento (art. 7º) e medidas de segurança técnicas e administrativas (art. 46). Frameworks de privacidade como o [NIST Privacy Framework](https://www.nist.gov/privacy-framework) ajudam a gerir esses deveres no projeto.

Para um especialista, quatro perguntas éticas se repetem. **Distribuição:** quem arca com o risco residual da opção escolhida, e essas pessoas tiveram voz? **Proporcionalidade:** a intrusão de uma medida de segurança — o monitoramento dos funcionários, a restrição do acesso de pacientes ou clientes — é proporcional ao dano que ela evita? **Honestidade:** os riscos e as incertezas são comunicados com veracidade aos tomadores de decisão e, quando apropriado, ao público? **Divulgação:** quando você descobre uma fraqueza que também afeta outros — um produto de fornecedor usado por outras concessionárias —, como protegê-los sem armar os atacantes? Os processos de divulgação coordenada de vulnerabilidades existem exatamente para esse caso ([CISA, CVD Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program)).

### 4.5 Quem arca com o risco residual

Medidas agregadas — total de domicílios-hora perdidos, perda esperada — podem favorecer opções que protegem áreas densas e bem atendidas, porque proteger muita gente um pouco pontua mais do que proteger pouca gente muito. Um especialista deve, portanto, relatar, ao lado dos totais, a **carga per capita por grupo** (distrito, tipo de cliente) e a carga sobre as **pessoas menos capazes de lidar com a situação**, como os domicílios com dependência médica de água ou de energia. Nem os totais nem as medidas per capita resolvem a questão; a escolha entre eles é um julgamento de valor que pertence ao tomador de decisão responsável, informado pelos deveres legais (por exemplo, os deveres para com clientes vulneráveis) e pelo apetite declarado da organização. O dever ético do especialista é tornar a distribuição visível, para que o trade-off seja escolhido com conhecimento de causa.

### 4.6 Exemplo resolvido: duas opções com o mesmo orçamento (sintético)

A Merrow Water atende três distritos. Harbour é urbano (60.000 domicílios); Fenley, suburbano (25.000); Upper Merrow, rural (6.000 domicílios numa única adutora, com uma telemetria lenta de restaurar e longos tempos de deslocamento das equipes). As interrupções de fornecimento de origem cibernética são modeladas como eventos de Poisson com duração lognormal (mediana de 8 horas). A restauração de Upper Merrow hoje leva três vezes mais tempo. Duas opções custam o mesmo:

- **X: endurecer o SCADA central** — reduz a frequência dos eventos de 0,30 para 0,20 por ano em toda parte; não faz nada pela longa restauração de Upper Merrow.
- **Y: segunda alimentação e controle local para Upper Merrow** — mantém a frequência em 0,30, mas reduz a restauração de Upper Merrow a 0,75 da duração base.

Os domicílios vulneráveis (com necessidades médicas ou de cuidado registradas) são contados separadamente: 900 em Harbour, 500 em Fenley, 400 em Upper Merrow.

### 4.7 Atividade prática: excedência de perdas e distribuição

```python
# Lab 4 - same budget, different people: loss exceedance and the distribution of harm (offline, stdlib only)
# Synthetic: Merrow Water supply interruptions caused by cyber events. Two options cost the same.
import random, math
random.seed(4)
YEARS = 20000
DISTRICTS = {  # name: (households, share of interruption events that hit this district, vulnerable households)
    "Harbour (urban)":  (60000, 0.40, 900),
    "Fenley (suburban)": (25000, 0.25, 500),
    "Upper Merrow (rural, single main)": (6000, 0.35, 400),
}
def poisson(lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= random.random()
        if p < L: return k
        k += 1
def simulate(freq, hours_mu, hours_sigma, rural_hours_factor):
    annual_hh_hours = []; per_district = {d: 0.0 for d in DISTRICTS}; vuln = {d: 0.0 for d in DISTRICTS}
    for _ in range(YEARS):
        total = 0.0
        for _ in range(poisson(freq)):
            hours = random.lognormvariate(hours_mu, hours_sigma)
            r = random.random(); acc = 0
            for d, (hh, share, v) in DISTRICTS.items():
                acc += share
                if r < acc:
                    h = hours * (rural_hours_factor if d.startswith("Upper") else 1.0)
                    per_district[d] += hh * h; vuln[d] += v * h; total += hh * h
                    break
        annual_hh_hours.append(total)
    return annual_hh_hours, per_district, vuln
OPTIONS = {
    "X: harden central SCADA (fewer events)":      (0.20, math.log(8), 0.9, 3.0),
    "Y: second feed + local control Upper Merrow": (0.30, math.log(8), 0.9, 0.75),
}
for name, args in OPTIONS.items():
    loss, per, vul = simulate(*args)
    loss.sort()
    mean = sum(loss) / YEARS
    p_any = sum(1 for x in loss if x > 0) / YEARS
    p_big = sum(1 for x in loss if x > 1_000_000) / YEARS
    p99 = loss[int(0.99 * YEARS)]
    print(name)
    print(f"  mean household-hours/yr {mean:9.0f}  P(any)={p_any:.3f}  P(>1M hh-h)={p_big:.4f}  99th pct {p99:9.0f}")
    for d, (hh, share, v) in DISTRICTS.items():
        print(f"  {d:34s} hours per household/yr {per[d]/YEARS/hh:5.2f}   vulnerable-household-hours/yr {vul[d]/YEARS:7.0f}")
```

Saída esperada:

```text
X: harden central SCADA (fewer events)
  mean household-hours/yr     88346  P(any)=0.183  P(>1M hh-h)=0.0204  99th pct   1498603
  Harbour (urban)                    hours per household/yr  0.97   vulnerable-household-hours/yr     872
  Fenley (suburban)                  hours per household/yr  0.64   vulnerable-household-hours/yr     318
  Upper Merrow (rural, single main)  hours per household/yr  2.39   vulnerable-household-hours/yr     956
Y: second feed + local control Upper Merrow
  mean household-hours/yr    117262  P(any)=0.261  P(>1M hh-h)=0.0305  99th pct   1920694
  Harbour (urban)                    hours per household/yr  1.48   vulnerable-household-hours/yr    1332
  Fenley (suburban)                  hours per household/yr  0.91   vulnerable-household-hours/yr     453
  Upper Merrow (rural, single main)  hours per household/yr  0.96   vulnerable-household-hours/yr     386
```

**Interpretação.** Em toda medida agregada, X é melhor: perda média de 88.346 contra 117.262 domicílios-hora por ano; chance anual de 2,0% contra 3,1% de exceder um milhão de domicílios-hora; um 99º percentil mais baixo. Diante do apetite da §4.2, X fica sobre o limite de cauda de 2% (0,0204, dentro do erro de simulação do limite) e Y o viola claramente. Mas a **distribuição** inverte o retrato. Sob X, um domicílio de Upper Merrow perde em média 2,39 horas por ano — mais que o dobro de um domicílio urbano e quase quatro vezes um suburbano —, e os 400 domicílios vulneráveis de Upper Merrow arcam com 956 domicílios vulneráveis-hora por ano, mais do que os 900 domicílios de Harbour. Y reduz a carga rural a 0,96 hora por domicílio e os domicílios vulneráveis-hora rurais a 386, ao custo de cargas maiores nos outros distritos. O total de domicílios vulneráveis-hora é quase idêntico (cerca de 2.146 sob X e 2.171 sob Y): as opções não diferem muito em quanto dano recai sobre as pessoas vulneráveis no conjunto, mas diferem fortemente em *quais* pessoas vulneráveis arcam com ele. A segunda cláusula do apetite — nenhum distrito sem fornecimento além de 48 horas — exigiria olhar para a cauda de Upper Merrow, que o resumo não mostra; essa é a extensão do EX016.

A análise não decide entre X e Y. Ela mostra que "X é melhor" só é verdade sob uma visão utilitarista agregada e que a escolha concentra o risco numa pequena população rural. Uma recomendação defensável poderia combinar X com medidas não técnicas mais baratas para Upper Merrow (água engarrafada pré-posicionada, um cadastro prioritário de domicílios vulneráveis), e precisa registrar o julgamento de valor.

### 4.8 Erros comuns e limites

- Multiplicar escores ordinais e tratar o produto como uma grandeza.
- Relatar apenas a perda anual média para um risco de cauda pesada.
- Declarar o apetite a risco como uma cor ou um adjetivo, e não como um limite em unidades de serviço.
- Tratar números elicitados como dados e descartar o registro da elicitação.
- Relatar apenas o benefício agregado, de modo que o dano concentrado em pequenos grupos fique invisível.
- Apresentar um julgamento de valor (agregado versus distribuição) como um resultado técnico.
- Segurar uma vulnerabilidade que afeta outros operadores porque a divulgação é incômoda.

Os limites do modelo são os de seus pressupostos: a independência de Poisson ignora campanhas que atingem vários locais ao mesmo tempo; a lognormal pode subestimar as interrupções mais longas; as participações dos distritos são julgamentos. Mude-os e os números se movem; o *método* de mostrar a distribuição ao lado dos totais não.

### Exercícios — capítulo 4

**EX016 — Melhoria rural parcial.** *Objetivo:* ver como a distribuição responde a uma opção mais fraca. *Insumos:* Laboratório 4. *Restrições:* mudar o fator de duração rural de Y de 0,75 para 1,5 (a segunda alimentação atrasa; só o controle local é entregue). *Passos:* (1) reexecutar; (2) relatar as horas por domicílio e os domicílios vulneráveis-hora de Upper Merrow sob o Y modificado; (3) comparar com X e com o Y original; (4) estender o laboratório para relatar a probabilidade de que Upper Merrow tenha, num ano, uma única interrupção de mais de 48 horas sob X e sob Y. *Evidência esperada:* saídas e parágrafo. *Rubrica:* 3 = números do Y modificado corretos (1,93 hora; 771 domicílios vulneráveis-hora), ainda melhor para Upper Merrow do que X, mas muito menos do que o Y original, extensão de 48 horas implementada com uma verificação correta por evento; 2 = falta a extensão; 1 = não executado; 0 = nada.

**EX017 — Memorando de análise ética.** *Objetivo:* aplicar princípios éticos à escolha entre X e Y. *Insumos:* §4.4–4.7. *Restrições:* 400 palavras; princípios do Menlo Report e de um código profissional. *Passos:* (1) identificar os grupos afetados e sua voz; (2) analisar a beneficência e a justiça; (3) declarar o julgamento de valor que o conselho precisa fazer; (4) recomendar uma opção combinada com medidas não técnicas. *Evidência esperada:* memorando. *Rubrica:* 3 = grupos específicos, trade-off entre a visão agregada e a distributiva nomeado como um julgamento, recomendação combinada concreta, dever de honestidade para com o conselho observado; 2 = princípios listados, mas não aplicados; 1 = afirma X ou Y como tecnicamente correto; 0 = nada.

**EX018 — Protocolo de elicitação.** *Objetivo:* obter parâmetros de gravidade defensáveis. *Insumos:* a pergunta "quanto tempo levaria para restaurar o fornecimento de Upper Merrow após a perda total do SCADA?". *Restrições:* três especialistas; grandeza observável; quantis. *Passos:* (1) definir a grandeza com precisão; (2) escrever o roteiro de elicitação, incluindo uma pergunta de calibração; (3) explicar como você agregaria e registraria. *Evidência esperada:* protocolo. *Rubrica:* 3 = grandeza inequívoca (eventos de início e de fim definidos), quantis de 5%, 50% e 95% pedidos, elicitação independente antes da discussão, calibração e registro mantidos; 2 = pedidos valores únicos; 1 = probabilidade de um evento vago; 0 = nada.

**EX019 — Declaração de apetite.** *Objetivo:* escrever o apetite e a tolerância em unidades de serviço. *Insumos:* a Merrow Health (três hospitais, uma dependência de serviço de ambulâncias). *Restrições:* pelo menos um limite de cauda e um limite de distribuição; mensuráveis a partir dos próprios dados da organização. *Passos:* redigir; depois testá-la contra um cenário plausível e dizer se ela é violada. *Evidência esperada:* declaração e teste. *Rubrica:* 3 = unidades de serviço (por exemplo, horas de desvio do departamento de emergência, tratamentos tempo-dependentes atrasados), limites de cauda e de distribuição mensuráveis, teste honesto; 2 = apenas médias; 1 = adjetivos; 0 = nada.

**EX020 — Dilema de divulgação.** *Objetivo:* lidar com uma fraqueza que afeta outros. *Insumos:* durante uma revisão, a Merrow Water descobre que a ferramenta de suporte remoto da Corvane aceita uma credencial padrão numa porta de manutenção; a Corvane dá suporte a outras concessionárias da região. *Restrições:* nenhum teste além dos sistemas da própria Merrow; nenhuma divulgação pública antes de um processo coordenado. *Passos:* (1) ações de proteção imediatas para a Merrow; (2) via de notificação à Corvane e, se necessário, a um coordenador; (3) o que dizer ao fórum de resiliência, e quando; (4) justificativa ética. *Evidência esperada:* plano. *Rubrica:* 3 = proteger primeiro os próprios sistemas, notificação privada ao fornecedor com evidências, uso de um processo de divulgação coordenada se o fornecedor não agir, fórum informado de um modo que proteja os outros sem publicar detalhes de exploração, princípios citados; 2 = falta uma etapa; 1 = testa os sistemas de outras concessionárias ou publica; 0 = nada.

### Síntese do capítulo

Quantifique o risco como frequência e gravidade com incerteza explícita, e leia-o pela curva de excedência de perdas, não por um escore único. Escreva o apetite e a tolerância em unidades de serviço, com limites sobre a cauda e sobre a distribuição. Trate o julgamento de especialistas como evidência que precisa ser elicitada com cuidado e registrada. Mostre quem arca com o risco residual — per capita e para os menos capazes de lidar com ele —, porque opções melhores na média podem concentrar o dano. Aplique princípios éticos reconhecidos às escolhas, aos testes e à divulgação, e mantenha os julgamentos de valor visíveis como julgamentos para o tomador de decisão responsável.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 12

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 (inglês) →](../../en/book/MANUSCRIPT.md#ch-05)

Os próximos capítulos ainda estão apenas na edição em inglês.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções e notas de avaliação

Cada resolução mostra uma resposta defensável e explica o que a rubrica recompensa. Uma resposta diferente pode receber a pontuação máxima quando atende ao mesmo padrão de evidências, escopo e honestidade sobre os limites. Os resultados numéricos vêm dos laboratórios offline deste livro, executados com o Python 3 (a versão 3.13 foi usada neste rascunho) e apenas a biblioteca padrão; se sua saída for diferente, confira primeiro a versão do Python, a semente, quando houver, e se você mudou a ordem dos sorteios aleatórios. Todos os números descrevem dados sintéticos; nunca os apresente como constatações sobre operadores reais. Esta edição parcial traz as resoluções de EX001–EX020; as de EX021–EX060 estão na [edição em inglês](../../en/book/MANUSCRIPT.md#worked-results) até a tradução dos capítulos correspondentes.

### Capítulo 1: EX001–EX005

**EX001 — Enquadre uma decisão hospitalar.** *Tomador de decisão:* o Diretor de Operações (COO) da Merrow Health, com aprovação do conselho acima de um limiar de capital declarado. *Decisão:* se e quando substituir o sistema de informação do laboratório de patologia sem suporte. *Opções:* (A) substituir neste ano por um produto com suporte; (B) isolar o sistema atual, restringir suas interfaces e substituí-lo em dois anos; (C) substituir em dois anos sem isolamento adicional (uma opção fraca, que uma pessoa razoável só poderia preferir sob pressão orçamentária extrema — melhor trocá-la por uma terceira opção genuína, como migrar o trabalho urgente para o sistema de outra unidade); (D) adiar indefinidamente. *Objetivos (unidades de serviço):* maximizar a liberação dos resultados urgentes dentro das metas clínicas; minimizar os procedimentos eletivos cancelados; minimizar a exposição de dados que identifiquem pacientes. *Horizonte:* decisão neste trimestre; consequências ao longo de três anos. *Restrições:* nenhum aumento de quadro fora do orçamento; aprovação de segurança clínica exigida; deveres de proteção de dados. A nota máxima exige uma terceira opção genuína (não um espantalho), objetivos em unidades de serviço e restrições distinguidas dos objetivos.

**EX002 — Mude uma célula.** Com o custo de TO de D em 1.200: arrependimentos máximos A=320, B=660, C=280, D=960; o arrependimento minimax continua escolhendo C. Valores esperados: analista A 299,6, B 293,1, C 290,6, D 309,0 (C vence); pessimista A 381,5, B 367,0, C 362,5, D 562,0 (C vence); regulador A 252,6, B 310,6, C 275,1, D 265,0 (A continua vencendo, com D agora em segundo lugar). D não vence porque suas células de ransomware e de fornecedor/nuvem continuam caras: mesmo que o cenário de TO fosse ignorado, seu arrependimento no cenário de ransomware seria de 1.300 − 450 = 850 (em relação a B), muito acima do arrependimento máximo de C, de 280; com a célula revisada, seu maior arrependimento é 960, no cenário de TO, em relação aos 240 de A. O ponto: uma célula revisada raramente inverte uma recomendação robusta quando vários cenários contribuem.

**EX003 — Valor da informação perfeita.** A melhor opção agora é C, com custo esperado de 290,6. Com informação perfeita, o custo esperado é 0,15×450 + 0,03×240 + 0,10×330 + 0,72×0 = 107,7. VEIP ≈ 182,9 (milhares de libras). Uma avaliação de £60 mil vale a compra para esta decisão apenas se puder mover a probabilidade de comprometimento de TO para o outro lado dos limiares de 3% ou 7% que mudam a recomendação, e se seu valor esperado de informação *imperfeita* se aproximar do seu custo. Uma avaliação que não consegue mudar a escolha tem baixo valor para a decisão, qualquer que seja sua qualidade.

**EX004 — Registro de decisão com divergência.** Um registro de nota máxima inclui a declaração, a tabela, os três conjuntos de crenças, o limiar (B abaixo de ~3%, C entre ~3–7%, A acima de ~7%), as três regras preferindo C, a escolha de C pelo Diretor de Operações, o risco residual (exposição parcial do acesso remoto e capacidade manual parcial) assumido por esse diretor, a divergência do gerente de operações, que prefere B porque "podemos perder o SCADA amanhã", e um gatilho de revisão como "alerta crível relatando o comprometimento dos nossos produtos de acesso remoto, ou um incidente de TO numa concessionária par".

**EX005 — Auditoria de vieses.** Disponibilidade (o ransomware no oleoduto), ancoragem (a cotação de £400 mil), otimismo sobre o recurso manual (2009), contagem de controles (nove de onze constatações), deferência/pensamento de grupo (o presidente falou primeiro, nenhuma outra opinião). Remédios: estimativas independentes antes da discussão; pré-mortem; exigir evidência de um simulado recente; pontuar as opções pela consequência; registrar as divergências e alternar quem fala primeiro.

### Capítulo 2: EX006–EX010

**EX006 — Mapeie uma prática.** O acesso intermediado de fornecedores apoia as funções Protect e Detect do CSF e os princípios do CAF sob a proteção contra ataques cibernéticos e a detecção de eventos; aparece nas CPGs da CISA sob os temas de contas e acesso; a IEC 62443 o enquadra como um conduíte controlado para dentro de uma zona. Se ele é uma obrigação legal para uma concessionária de água depende da jurisdição e da transposição — verifique com o jurídico diante do regime aplicável (por exemplo, as medidas da NIS2) em vez de afirmá-lo. A nota máxima mantém a obrigação separada da orientação.

**EX007 — Mude a política de evidências.** Com crédito de 0,25 para as declarações: Merrow Water verificada em 48%, Health 54%, Energy 75%, Port 15%. A ordem do ranking e a prioridade de testar as declarações sobrevivem; só o número absoluto do porto parece menos catastrófico. Uma política defensável para um relatório do fórum: as declarações recebem crédito provisório zero (para motivar os testes), com uma nota de rodapé de que algumas declarações podem ser verdadeiras — porque o propósito do relatório é impulsionar a verificação.

**EX008 — Plano de verificação.** Backups offline: restauração cronometrada de um backup nomeado do SCADA num host isolado; aprovação = restauração bem-sucedida dentro de um tempo declarado; ~2 dias de trabalho. Acesso de fornecedores: conciliar os logs do intermediador com as sessões VPN do firewall ao longo de 30 dias; aprovação = toda sessão correspondida e aprovada; ~1 dia de trabalho. Segmentação TI/TO: inspecionar as regras do firewall e tentar um caminho permitido versus negado da rede corporativa até um host de controle que não seja de produção, sob regras de engajamento; aprovação = nenhum caminho inesperado; ~3 dias de trabalho. A nota máxima exige testes da realidade, não revisão de políticas.

**EX009 — Operador sob vários regimes.** Regimes candidatos: NIS2 (água e eletricidade como essenciais), CER (resiliência das entidades críticas), DORA (subsidiária de pagamentos), possivelmente códigos nacionais de eletricidade. Um único conjunto interno de controles mapeado para cada um; os relógios de notificação de incidentes (alerta precoce / notificação / relatório final na NIS2; notificação de incidentes de TIC no DORA; quaisquer relógios específicos da eletricidade) conciliados num único procedimento. Perguntas específicas ao jurídico: quais entidades são designadas; quais relógios obrigam qual subsidiária; se uma única notificação pode satisfazer vários regimes.

**EX010 — Critique uma prática.** O conselho quer saber se um atacante consegue perturbar o atendimento clínico. Um teste externo anual de uma amostra da rede clínica responde a uma pergunta estreita sobre aquela amostra naquela janela, com técnicas contidas por segurança e frequentemente excluindo os dispositivos médicos. Um portfólio melhor: revisão orientada pela consequência dos piores desfechos clínicos; monitoramento contínuo e testes de restauração; testes num ambiente representativo que não seja de produção; e uma avaliação focada dos caminhos via dispositivos médicos e fornecedores. Limites: nenhum portfólio elimina o risco residual; cada método precisa do consentimento das operações.

### Capítulo 3: EX011–EX015

**EX011 — Robustez da ordem.** A mudança corrigida está às 02:23:03 e o início do cliente de IHM às 02:15:32 — uma margem de 451 segundos. Deslocar a âncora do historiador em um minuto move a mudança para 02:24:03; a ordem não muda. Confirme o deslocamento com uma segunda âncora independente (por exemplo, um evento de processo registrado tanto pelo historiador quanto por um analisador com relógio conhecido, ou uma segunda consulta NTP).

**EX012 — Plano de preservação.** Ordem: logs de firewall e de VPN (exportar, calcular o hash); logs de identidade e do jump host; captura volátil do JH-2, se for seguro; exportação do historiador para a janela; livros de registro dos operadores; registros de sessão da Corvane (pedido contratual imediato); estado do controlador apenas com aprovação das operações e com as ferramentas do fornecedor. Cadeia de custódia para cada item. Nenhuma interação online com o controlador sem o responsável pelas operações.

**EX013 — Escreva a constatação.** Observação: linha do tempo corrigida, com deslocamentos e incerteza de ±10 s; mudança atribuída à HMI-JH2 durante a sessão vendor-svc. Inferência: mudança feita dentro dessa sessão; pessoa desconhecida porque a conta é compartilhada. Confiança: moderada. Consequência: suspender a conta compartilhada; exigir contas nominais; pedir à Corvane os registros de sessão. Frase ao regulador: "Ocorreu uma mudança inexplicada no setpoint de dosagem durante uma sessão remota de um fornecedor; o setpoint foi restaurado em menos de um minuto; a investigação continua; não há evidência de que água insegura tenha saído da estação."

**EX014 — Evidências discriminantes.** O intruso externo prevê um IP de origem desconhecido e técnicas novas — em aberto. A mudança legítima do fornecedor prevê um chamado e um padrão em outros locais — contrariada pela ausência de chamado; o padrão está em aberto. O erro local do operador prevê uma estação local como origem — contrariado para a mudança (HMI-JH2). A receita automatizada prevê um cronograma — em aberto, verificar no historiador. O erro de etiquetagem prevê discordância com o controlador — em aberto. O mau uso da conta compartilhada prevê uma sessão sem chamado correspondente — apoiado até agora. Próximos passos: os registros de sessão da Corvane e a comparação com contas nominais.

**EX015 — Notificação em etapas.** Alerta precoce: o fato do evento, o impacto no serviço (nenhum duradouro), investigação aberta. Notificação: linha do tempo corrigida, ações (conta suspensa, contas nominais exigidas), perguntas em aberto. Esboço final: causa raiz, correções das declarações anteriores, lições, risco residual. A nota máxima nunca afirma "ataque" nem nomeia uma pessoa cedo.

### Capítulo 4: EX016–EX020

**EX016 — Melhoria rural parcial.** Y modificado: Upper Merrow com 1,93 hora por domicílio por ano e 771 domicílios vulneráveis-hora — melhor do que X (2,39; 956), mas muito pior do que o Y original (0,96; 386). Estender o laboratório para relatar P(alguma interrupção em Upper Merrow > 48 h) dá cerca de 0,015 sob X, 0,001 sob o Y original e 0,007 sob o Y modificado (semente 4). A nota máxima implementa uma verificação da duração por evento para Upper Merrow.

**EX017 — Memorando de análise ética.** Grupos afetados: domicílios de Harbour e de Fenley, domicílios de Upper Merrow (incluindo os vulneráveis), funcionários. Beneficência e justiça (Menlo; primazia do bem-estar público na ACM e na NSPE): X reduz o dano total e cumpre o apetite de cauda; Y reduz o dano rural concentrado. O conselho precisa fazer o julgamento de valor; uma recomendação combinada (X mais medidas rurais não técnicas) é honesta sobre a concentração residual.

**EX018 — Protocolo de elicitação.** Grandeza: horas entre "SCADA declarado indisponível em Upper Merrow" e "água tratada fluindo para a zona sob procedimento manual documentado". Pedir a três especialistas, de forma independente, os percentis 5, 50 e 95 depois de uma pergunta de calibração; discutir; agregar (por exemplo, mediana das medianas com pesos iguais e envoltória dos intervalos); registrar a pessoa, a data e a justificativa.

**EX019 — Declaração de apetite.** Exemplo: "A Merrow Health não aceitará uma chance anual superior a 5% de desvio de departamento de emergência de origem cibernética que exceda 24 horas contínuas em qualquer hospital, nem nenhum cenário crível em que o atendimento de emergência tempo-dependente fique indisponível nos três hospitais ao mesmo tempo." Testá-la contra um cenário de ransomware que afete os sistemas clínicos de dois hospitais.

**EX020 — Dilema de divulgação.** Imediato: remover ou trocar a credencial padrão nos sistemas da Merrow; bloquear a porta; monitorar. Notificação privada à Corvane com evidências; se a Corvane não agir, acionar um processo de divulgação coordenada (CVD da CISA). Informar ao fórum que uma classe de ferramentas de suporte remoto precisa de revisão de credenciais, sem publicar detalhes de exploração. Justificar pela beneficência e pela justiça do Menlo e pelos deveres profissionais para com o público.

<a id="glossary"></a>

## Glossário

**Registro de decisão de arquitetura (ADR, architecture decision record).** Um registro curto de uma escolha de arquitetura: contexto, alternativas, decisão, consequências, verificação e gatilho de revisão.

**Caso de asseguração (assurance case).** Um argumento estruturado de que uma alegação é verdadeira, com subalegações, evidências e refutações consideradas.

**Relógio de reserva (backup clock).** Por quanto tempo um local consegue continuar sua função essencial depois que uma dependência falha, usando sua própria reservação, combustível, bateria ou alternativa manual.

**Acesso de emergência (break-glass).** Um caminho de acesso de emergência usado quando os controles de segurança primários estão indisponíveis; precisa ser alarmado, registrado e testado, e não pode se tornar rotina.

**Declarado / documentado / verificado.** Graus de evidência de uma prática: declaração, documento ou observação por teste ou inspeção.

**Conjunto de pontos de estrangulamento (chokepoint set).** O menor conjunto de nós cuja remoção (ou defesa perfeita) corta todo caminho dos pontos de entrada até um alvo num grafo de arquitetura.

**Projeto orientado pela consequência.** Projetar a segurança a partir do resultado físico ou de serviço intolerável, de trás para a frente, até os caminhos digitais que poderiam causá-lo.

**Registro de decisão.** Um registro contemporâneo de uma decisão: declaração, opções, evidências, julgamentos, regras aplicadas, escolha, risco residual, divergências e gatilho de revisão.

**Diferença em diferenças (DiD).** Uma estimativa do efeito de um projeto: a mudança no grupo piloto menos a mudança num grupo de comparação no mesmo período.

**Valor esperado da informação perfeita (VEIP; EVPI, em inglês).** O máximo que um tomador de decisão deveria pagar por uma informação que revelasse, antes da escolha, qual cenário vai ocorrer.

**Índice de Herfindahl–Hirschman (HHI).** Soma dos quadrados das participações percentuais; uma medida de concentração que vai de perto de 0 a 10.000 (monopólio).

**Curva de excedência de perdas (LEC).** A probabilidade de que a perda anual exceda cada nível; um modo de ler o risco que mostra a cauda.

**Minimax.** Escolher a opção cujo resultado no pior caso seja o menos ruim.

**Arrependimento minimax.** Escolher a opção cujo maior arrependimento (custo adicional em relação à melhor opção em cada cenário) seja o menor.

**Tendências paralelas.** O pressuposto, na diferença em diferenças, de que os grupos piloto e de comparação teriam mudado na mesma quantidade sem o projeto.

**Verificação por permutação.** Avaliar uma estimativa perguntando quão incomum ela é entre todas as maneiras de atribuir as unidades aos grupos.

**Gráfico de comportamento do processo (XmR).** Um gráfico que usa o próprio histórico de um indicador para separar a variação rotineira dos sinais de mudança.

**RACI.** Uma matriz que atribui os papéis de Responsável (Responsible), Aprovador (Accountable), Consultado (Consulted) e Informado (Informed) às atividades; cada atividade crítica deve ter exatamente um papel Aprovador.

**Gatilho de revisão.** Uma observação declarada de antemão que reabre uma decisão ou uma alegação de asseguração.

**Apetite / tolerância a risco.** Quanto risco, e de que tipo, uma organização reterá, e os limites da variação aceitável; idealmente declarados em unidades de serviço, com limites de cauda e de distribuição.

**Unidades de serviço.** Unidades da função essencial: domicílios-hora de fornecimento, pacientes desviados, megawatts-hora entregues e semelhantes.

**Paradoxo de Simpson.** Um padrão em que uma comparação agregada aponta na direção oposta à de todas as comparações dentro dos grupos, geralmente por causa de um fator de confusão, como o porte.

**Modelo das Três Linhas.** Um modelo de papéis do IIA: a gestão como dona do risco (primeira linha), as funções especializadas de risco e conformidade (segunda) e a asseguração independente (terceira).

**Intervalo de escore de Wilson.** Um intervalo de confiança para uma proporção que se comporta bem com amostras pequenas e taxas próximas de 0 ou de 1.

**Zonas e conduítes.** Conceitos da IEC 62443: grupos de ativos com requisitos de segurança comuns, e as comunicações controladas entre eles.

<a id="references"></a>

## Referências

Leis, orientações e páginas públicas mudam. As versões e datas abaixo são as consultadas para este rascunho (outubro de 2026); verifique-as de novo antes de se apoiar nelas. Uma citação apoia a afirmação geral ao seu lado no texto, nunca os detalhes do caso sintético. A lista é idêntica à da edição em inglês, com o acréscimo da LGPD, citada na §4.4.

### Políticas, leis e normas

- Bank for International Settlements, Committee on Payments and Market Infrastructures, and International Organization of Securities Commissions. [Guidance on Cyber Resilience for Financial Market Infrastructures](https://www.bis.org/cpmi/publ/d146.htm). June 2016.
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. Diário Oficial da União. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [National Security Memorandum on Critical Infrastructure Security and Resilience (overview)](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-security-memorandum-critical-infrastructure-security-and-resilience).
- Cybersecurity and Infrastructure Security Agency. [Secure by Design](https://www.cisa.gov/securebydesign).
- Cybersecurity and Infrastructure Security Agency. [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom).
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Official Journal, 4 May 2016.
- European Union. [Regulation (EU) 2022/2554 on digital operational resilience for the financial sector (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). Official Journal, 27 December 2022.
- International Electrotechnical Commission. [IEC 62443-3-2:2020, Security for industrial automation and control systems — Part 3-2: Security risk assessment for system design](https://webstore.iec.ch/en/publication/30727). Catalogue page.
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final).
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final).
- National Institute of Standards and Technology. [SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final).
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://doi.org/10.6028/NIST.SP.800-82r3).
- National Institute of Standards and Technology. [SP 800-160 Vol. 2 Rev. 1, Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1).
- National Institute of Standards and Technology. [SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final).
- National Institute of Standards and Technology. [SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://doi.org/10.6028/NIST.CSWP.29).
- National Institute of Standards and Technology. [NIST Privacy Framework](https://www.nist.gov/privacy-framework).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- North American Electric Reliability Corporation. [Critical Infrastructure Protection (CIP) Standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).
- U.S. Department of Health and Human Services. [Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). January 2024.
- U.S. Environmental Protection Agency. [America's Water Infrastructure Act of 2018: Risk Assessments and Emergency Response Plans](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans).
- U.S. Department of Justice. [Herfindahl-Hirschman Index](https://www.justice.gov/atr/herfindahl-hirschman-index).

### Incidentes e evidências setoriais

- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01).
- Cybersecurity and Infrastructure Security Agency. [PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure (AA24-038A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a). February 2024.
- Cybersecurity and Infrastructure Security Agency. [The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years). May 2023.
- Dameff, C., Tully, J., Chan, T. C., et al. [Ransomware Attack Associated With Disruptions at Adjacent Emergency Departments in the US](https://doi.org/10.1001/jamanetworkopen.2023.12270). *JAMA Network Open*, 6(5), e2312270, 2023.
- Ghafur, S., Kristensen, S., Honeyford, K., Martin, G., Darzi, A., and Aylin, P. [A Retrospective Impact Analysis of the WannaCry Cyberattack on the NHS](https://doi.org/10.1038/s41746-019-0161-6). *npj Digital Medicine*, 2, 98, 2019.
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- National Audit Office. [Investigation: WannaCry Cyber Attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.
- Neprash, H. T., McGlave, C. C., Cross, D. A., et al. [Trends in Ransomware Attacks on US Hospitals, Clinics, and Other Health Care Delivery Organizations, 2016–2021](https://doi.org/10.1001/jamahealthforum.2022.4873). *JAMA Health Forum*, 3(12), e224873, 2022.
- U.S. Department of Energy, Office of Cybersecurity, Energy Security, and Emergency Response. [Colonial Pipeline Cyber Incident](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident).
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.

### Métodos, análise de decisão e ética

- Association for Computing Machinery. [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics).
- Arp, D., Quiring, E., Pendlebury, F., et al. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). *USENIX Security*, 2022.
- Bochman, A., and Freeman, S. [Countering Cyber Sabotage: Introducing Consequence-Driven, Cyber-Informed Engineering (CCE)](https://www.routledge.com/Countering-Cyber-Sabotage-Introducing-Consequence-Driven-Cyber-Informed-Engineering-CCE/Bochman-Freeman/p/book/9780367673710). CRC Press, 2021.
- Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., and Havlin, S. [Catastrophic Cascade of Failures in Interdependent Networks](https://doi.org/10.1038/nature08932). *Nature*, 464, 1025–1028, 2010.
- Card, D., and Krueger, A. B. [Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania](https://www.jstor.org/stable/2118030). *American Economic Review*, 84(4), 772–793, 1994.
- Chamberlin, T. C. [The Method of Multiple Working Hypotheses](https://doi.org/10.1126/science.148.3671.754). *Science*, 148(3671), 754–759, 1965 (reprint of the 1890 paper).
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- Institute of Internal Auditors. [The IIA's Three Lines Model: An Update of the Three Lines of Defense](https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/). 2020.
- Kerr, N. L. [HARKing: Hypothesizing After the Results Are Known](https://doi.org/10.1207/s15327957pspr0203_4). *Personality and Social Psychology Review*, 2(3), 196–217, 1998.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *AAAI*, 2022.
- Klein, G. [Performing a Project Premortem](https://hbr.org/2007/09/performing-a-project-premortem). *Harvard Business Review*, September 2007.
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- National Society of Professional Engineers. [NSPE Code of Ethics for Engineers](https://www.nspe.org/resources/ethics/code-ethics).
- NIST/SEMATECH. [e-Handbook of Statistical Methods, 6.3.2 What are Variables Control Charts?](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc32.htm).
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *Proceedings of the National Academy of Sciences*, 115(11), 2600–2606, 2018.
- O'Hagan, A., Buck, C. E., Daneshkhah, A., et al. [Uncertain Judgements: Eliciting Experts' Probabilities](https://doi.org/10.1002/0470033312). Wiley, 2006.
- Pearl, J., and Bareinboim, E. [External Validity: From Do-Calculus to Transportability Across Populations](https://doi.org/10.1214/14-STS486). *Statistical Science*, 29(4), 579–595, 2014.
- Reason, J. [Human Error: Models and Management](https://doi.org/10.1136/bmj.320.7237.768). *BMJ*, 320, 768–770, 2000.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems Magazine*, 21(6), 11–25, 2001.
- Saltelli, A., Ratto, M., Andres, T., et al. [Global Sensitivity Analysis: The Primer](https://doi.org/10.1002/9780470725184). Wiley, 2008.
- Saltzer, J. H., and Schroeder, M. D. [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939). *Proceedings of the IEEE*, 63(9), 1278–1308, 1975.
- Savage, L. J. [The Theory of Statistical Decision](https://doi.org/10.1080/01621459.1951.10500768). *Journal of the American Statistical Association*, 46(253), 55–67, 1951.
- Simpson, E. H. [The Interpretation of Interaction in Contingency Tables](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x). *Journal of the Royal Statistical Society Series B*, 13(2), 238–241, 1951.
- Smith, W. E. [Various Optimizers for Single-Stage Production](https://doi.org/10.1002/nav.3800030106). *Naval Research Logistics Quarterly*, 3(1–2), 59–66, 1956.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). *IEEE Symposium on Security and Privacy*, 2010.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003.
- Tversky, A., and Kahneman, D. [Judgment under Uncertainty: Heuristics and Biases](https://doi.org/10.1126/science.185.4157.1124). *Science*, 185(4157), 1124–1131, 1974.
- Wilson, E. B. [Probable Inference, the Law of Succession, and Statistical Inference](https://doi.org/10.1080/01621459.1927.10502953). *Journal of the American Statistical Association*, 22(158), 209–212, 1927.
