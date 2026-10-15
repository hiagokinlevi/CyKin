# Segurança de TO, IoT e Sistemas Ciberfísicos: Prática e Liderança na Pós-Graduação

- Idioma: português do Brasil (`pt`); curso de pós-graduação, dois anos em tempo parcial; aproximadamente 600 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–12 de 12 têm texto didático escrito à mão; os exercícios EX001–EX060 têm resoluções correspondentes; os laboratórios offline usam a biblioteca padrão do Python 3, e suas saídas vêm de execuções reais. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto. Cobertura de capítulos em rascunho não é um livro concluído.
- Público: profissionais experientes que lideram decisões de segurança de TO, IoT e sistemas ciberfísicos em escala organizacional.
- Relação com os livros vizinhos: o [livro de bacharelado](../../../../bachelors-4-years/ot-iot-security/en/book/MANUSCRIPT.md) constrói os fundamentos; o [livro de mestrado](../../../../masters-2-years/ot-iot-security/en/book/MANUSCRIPT.md) ensina o ciclo de pesquisa. **Este livro é orientado pela prática**: decidir, avaliar, integrar e assegurar.
- Autoria: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é uma qualificação credenciada. Não concede autorização para acessar plantas reais. Todas as organizações, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Cada capítulo tem objetivos de aprendizagem, seções didáticas, um exemplo resolvido, um caso sintético identificado, erros e limites, cinco exercícios pontuados de 0 a 3, uma síntese e um bloco **Continue estudando**. Os laboratórios (Capítulos 1, 4, 6 e 9) rodam offline com `python3 file.py` sobre dados sintéticos com semente fixa.

### Caso sintético contínuo

| Elemento | Papel | Limite |
|---|---|---|
| **Bayside Water Reclamation Plant (BWRP)** — CLP de dosagem PLC-D, SCADA, historiador, 23 estações elevatórias com RTUs celulares, acesso remoto de fornecedores | Organização estudada ao longo do livro | Inventada |
| **Daniel Osei** | Líder de segurança de TO, subordinado ao diretor da planta | Inventado |

### Fontes centrais

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [série ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [cybersecurity advisories](https://www.cisa.gov/news-events/cybersecurity-advisories); Giraldo et al. 2018; Urbina et al. 2016. Lista completa nas [Referências](#references).

## Sumário

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Tomada de decisão avançada em segurança

### Objetivos de aprendizagem

Você vai (1) enquadrar uma decisão de segurança de TO com opções, critérios, incerteza e um responsável pela decisão; (2) comparar opções pela perda esperada e pelo pior caso plausível ao mesmo tempo; (3) registrar uma decisão de modo que ela possa ser auditada depois; e (4) reconhecer quando uma decisão deve ser adiada para reunir informações.

### 1.1 Decisões, não constatações

No nível de pós-graduação, a entrega raramente é uma lista de vulnerabilidades; é uma decisão que alguém com orçamento e responsabilidade precisa tomar. Na Bayside Water Reclamation Plant (BWRP), sintética, o líder de segurança de TO Daniel Osei precisa decidir como os fornecedores chegam ao controlador de dosagem química PLC-D. Um enquadramento de decisão nomeia o responsável (o diretor da planta), as opções, os critérios, o que é incerto e a data até a qual a decisão deve ser tomada.

Para a decisão sobre o acesso dos fornecedores, o enquadramento também precisa do prazo que a força, como o vencimento do contrato atual de VPN, e das pessoas que devem ser consultadas: operações, o gestor de fornecedores e a engenharia. Escrever o enquadramento antes da análise impede que Daniel escolha os critérios depois de saber qual opção eles favorecem.

### 1.2 A perda esperada é necessária, mas não suficiente

A perda anual esperada — probabilidade vezes perda, somada sobre os cenários — permite comparar numa mesma escala opções com custos diferentes. Mas as concessionárias públicas não são neutras ao risco: um evento raro que contamina o efluente lançado numa baía, desencadeia uma ação regulatória e corrói a confiança pública pode ser inaceitável com qualquer probabilidade acima de um limiar. Por isso, os líderes relatam a perda esperada junto com o pior caso plausível e qualquer restrição regulatória ou de segurança que se imponha independentemente da aritmética.

```python
"""Lab 01: compare three synthetic BWRP options by expected annual loss and worst credible case."""
options = {  # name: (annual cost, [(probability per year, loss if it happens)])
    "A keep vendor VPN":        (10_000, [(0.10, 400_000), (0.02, 2_500_000)]),
    "B brokered sessions":      (35_000, [(0.03, 400_000), (0.005, 2_500_000)]),
    "C no remote access":       (90_000, [(0.01, 400_000), (0.004, 2_500_000)]),
}
for name, (cost, events) in options.items():
    eal = sum(p * l for p, l in events)
    worst = max(l for _, l in events)
    print(f"{name:20} cost={cost:>7,} expected_loss={eal:>9,.0f} total={cost+eal:>9,.0f} worst_case={worst:,}")
```

Execute com `python3 lab_decide.py`. Saída verificada:

```text
A keep vendor VPN    cost= 10,000 expected_loss=   90,000 total=  100,000 worst_case=2,500,000
B brokered sessions  cost= 35,000 expected_loss=   24,500 total=   59,500 worst_case=2,500,000
C no remote access   cost= 90,000 expected_loss=   14,000 total=  104,000 worst_case=2,500,000
```

### 1.3 Lendo a comparação

A opção B tem o menor total (59.500) porque o custo do seu controle compra uma grande redução na probabilidade de incidente. A opção C elimina mais risco, mas custa mais do que economiza sob essas estimativas. As três compartilham o mesmo pior caso, porque o cenário catastrófico continua possível por outros caminhos; nenhuma escolha de acesso remoto o elimina. Essa observação manda o líder olhar para salvaguardas independentes, e não para mais gastos com acesso remoto.

Os números também mostram quão sensível é a classificação. A opção A perde por causa das suas probabilidades de incidente; se as duas estimativas fossem reduzidas à metade, o total de A cairia para 55.000 e ultrapassaria os 59.500 de B. É por isso que o registro de Daniel nomeia um gatilho de revisão atrelado à estimativa de incidentes, e é por isso que a próxima pergunta é quão firmes essas probabilidades realmente são.

### 1.4 Valor da informação

Se as estimativas de probabilidade são contestadas — e, para ataques direcionados, sempre são —, pergunte se a decisão mudaria caso elas se movessem dentro da sua faixa plausível. Se B vence em toda essa faixa, decida agora. Se a classificação se inverte, um estudo curto (revisão dos registros dos fornecedores, um exercício de mesa) pode valer mais do que uma compra imediata.

Para a BWRP, a pergunta é se B ainda vence caso a probabilidade de incidente com fornecedores da opção A seja menor do que a estimada. Daniel pode testar isso no laboratório mudando um número de cada vez e anotando onde a classificação se inverte. Se uma inversão exigir uma estimativa fora do que os pares do setor relatam, a decisão se mantém; se não, duas semanas revisando os registros dos fornecedores podem ser o melhor primeiro gasto.

### Exemplo resolvido (BWRP sintética)

Registro de decisão de Daniel: "D-2026-14. Responsável: diretor da planta. Decisão: adotar sessões intermediadas para fornecedores (B). Base: menor custo total esperado sob as estimativas do anexo 1; mesmo pior caso entre as opções, de modo que uma ação separada (D-2026-15) revisa o intertravamento de limite alto da dosagem. Revisar se a estimativa de frequência de incidentes com fornecedores passar de 0,06 por ano ou após qualquer incidente de acesso remoto."

> **Caso sintético — Bayside Water Reclamation Plant.** A BWRP, Daniel Osei e todos os custos e probabilidades são inventados.

### Erros e limites

Estimativas pontuais para probabilidades adversariais transmitem uma falsa precisão; apresente faixas. A aritmética da perda esperada não captura o dano às pessoas a jusante, que precisa ser argumentado separadamente.

### Exercícios

- **EX001 — Custo total da opção A com uma probabilidade menor.** Se o cenário de 400.000 de A cair para 0,05 por ano, recalcule o total de A. *Rubrica:* 3 = 10.000 + 20.000 + 50.000 = 80.000, ainda acima de B; 2 = só o número; 1 = erro aritmético; 0 = nenhum.
- **EX002 — Por que o pior caso é idêntico.** Explique o que o pior caso compartilhado de 2,5 milhões implica para o líder. *Rubrica:* 3 = a escolha de acesso remoto não elimina o caminho catastrófico; investir numa salvaguarda independente; 2 = parcial; 1 = "todos iguais"; 0 = nenhum.
- **EX003 — Escrever um gatilho de revisão.** Acrescente mais um gatilho de revisão à D-2026-14. *Rubrica:* 3 = gatilho observável e específico; 2 = vago, mas relevante; 1 = "se as coisas mudarem"; 0 = nenhum.
- **EX004 — A classificação se inverte?** Encontre a probabilidade do cenário de 400.000 de B na qual o total de B se iguala aos 100.000 de A. *Rubrica:* 3 = (100.000 − 35.000 − 12.500)/400.000 ≈ 0,131; 2 = método; 1 = ignora o outro termo; 0 = nenhum.
- **EX005 — Quando ainda não decidir.** Descreva uma situação em que Daniel deveria adiar a D-2026-14 para reunir informações. *Rubrica:* 3 = a classificação se inverte dentro da faixa plausível e um estudo barato pode estreitá-la antes de um prazo; 2 = parcial; 1 = "quando houver dúvida"; 0 = nenhum.

### Síntese

Os líderes decidem com a perda esperada, o pior caso plausível, responsáveis explícitos e gatilhos de revisão, e compram informação quando ela pode mudar a escolha.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 12

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Segurança de TO, IoT e sistemas ciberfísicos: prática atual

### Objetivos de aprendizagem

Você vai (1) comparar o programa de segurança de TO de uma organização com os temas da NIST SP 800-82r3 e da IEC 62443-2-1; (2) distinguir a prática documentada da prática executada; (3) produzir uma lista de lacunas com evidências; e (4) priorizar as lacunas para a liderança.

### 2.1 O que as orientações atuais esperam

A NIST SP 800-82r3 organiza um programa de segurança de TO em torno de governança, gestão de riscos, arquitetura e das capacidades de segurança aplicadas aos sistemas de TO, e mapeia as considerações de TO nas funções do NIST Cybersecurity Framework. A IEC 62443-2-1 especifica requisitos para o programa de segurança de um proprietário de ativos. Nenhuma das duas é uma lista de verificação a marcar; ambas descrevem capacidades que um programa maduro demonstra.

Numa revisão, use cada documento para gerar perguntas, e não uma pontuação. Na BWRP, isso significa perguntar, por exemplo, como o acesso remoto é governado, como os ativos são inventariados e como seriam tratados incidentes no sistema de dosagem. As respostas então entram na lista de lacunas com evidências, de modo que a revisão relata o que a planta consegue mostrar, e não quantas cláusulas ela alega cumprir.

### 2.2 Documentado versus executado

Uma política que diz "o acesso remoto é revisado mensalmente" é prática documentada. Um registro mostrando as três últimas revisões mensais, com as constatações encerradas, é prática executada. Os avaliadores de pós-graduação procuram a segunda. Na BWRP, Daniel amostra evidências de cada prática alegada, em vez de aceitar as respostas das entrevistas.

A amostragem precisa ser escolhida antes de olhar, ou ela deriva para os casos que parecem bons. Daniel escolhe cinco práticas que ficam em caminhos para consequências e pede, para cada uma, o artefato mais recente que prove que ela foi realizada. Uma resposta de entrevista pode apontar para uma evidência, mas nunca a substitui na lista de lacunas.

### 2.3 Montando a lista de lacunas

Para cada capacidade: o que a orientação espera, o que a BWRP documenta, o que as evidências mostram que é executado, a lacuna, a consequência da lacuna e um responsável proposto. As estações elevatórias remotas conectadas por RTUs celulares são um ponto cego comum: aparecem no registro de ativos como "estações de bombeamento", mas não como pontos de rede.

Cada linha deve ser específica o suficiente para que o seu responsável consiga agir. Para a lacuna de inventário da BWRP, isso significa nomear as nove RTUs de estações elevatórias ainda não listadas, a consequência de que elas não podem ser monitoradas nem corrigidas e a pessoa que vai acrescentá-las. Uma linha que só diz "inventário incompleto" não dá tarefa a ninguém.

### 2.4 Priorizando

Priorize as lacunas que ficam em caminhos para consequências (dosagem, qualidade do efluente) e as que são baratas de fechar. A falta de inventário das RTUs celulares bloqueia várias outras capacidades — monitoramento, correções, delimitação de incidentes —, então ela fica no topo, mesmo sendo "só documentação".

Escreva a classificação com a sua razão, para que o diretor da planta veja por que uma tarefa de inventário supera uma nova ferramenta. Na BWRP, a revisão do acesso remoto vem em seguida, porque não é executada desde março e os fornecedores conseguem chegar ao PLC-D. O teste de restauração da lógica dos CLPs vem depois, pois cópias de segurança cuja restauração nunca foi testada podem falhar quando forem necessárias.

### Exemplo resolvido (BWRP sintética)

A amostra de cinco práticas de Daniel: inventário de ativos (documentado, executado em parte — 14 de 23 RTUs das estações elevatórias listadas); revisão do acesso remoto (documentada, não executada desde março); cópia de segurança da lógica dos CLPs (executada, restauração nunca testada); plano de resposta a incidentes (documentado, sem playbook específico de TO); correções (executadas nas IHMs Windows, não no firmware das RTUs).

> **Caso sintético — Bayside Water Reclamation Plant.** As contagens e datas são inventadas.

### Erros e limites

Uma comparação com um único documento pode deixar de fora a regulação setorial. Amostrar cinco práticas dá uma visão, não uma opinião de auditoria.

### Exercícios

- **EX006 — Classificar uma prática alegada.** "Testamos as restaurações anualmente" é declarado, mas não existe registro. Documentada ou executada? *Rubrica:* 3 = apenas documentada; pedir evidências; 2 = só o rótulo; 1 = executada; 0 = nenhum.
- **EX007 — Classificar a lacuna de inventário das RTUs.** Justifique por que a lacuna de inventário das RTUs fica acima da falta de playbook. *Rubrica:* 3 = bloqueia monitoramento, correções e delimitação; habilitadora; 2 = parcial; 1 = "mais importante"; 0 = nenhum.
- **EX008 — Uma linha da lista de lacunas.** Escreva a linha completa da lista de lacunas para "restauração nunca testada". *Rubrica:* 3 = expectativa, documentado, executado, lacuna, consequência, responsável; 2 = quatro campos; 1 = só a lacuna; 0 = nenhum.
- **EX009 — Escolher o documento de referência.** Quando a IEC 62443-2-1 seria uma referência de comparação melhor do que a SP 800-82r3 para a BWRP? *Rubrica:* 3 = quando se aplicam requisitos de certificação ou contratuais sobre o programa do proprietário de ativos; 2 = parcial; 1 = "ela é melhor"; 0 = nenhum.
- **EX010 — Cobertura da amostra.** O que pode e o que não pode ser concluído a partir da amostra de cinco práticas? *Rubrica:* 3 = lacunas indicativas; não é uma opinião de garantia completa; viés de amostragem; 2 = um lado; 1 = alega demais; 0 = nenhum.

### Síntese

As revisões da prática atual comparam evidências do que é feito, e não do que está escrito, e classificam as lacunas pelo seu efeito sobre as consequências e sobre as outras capacidades.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Segurança de TO, IoT e sistemas ciberfísicos: evidências especializadas

### Objetivos de aprendizagem

Você vai (1) avaliar a qualidade das fontes de evidência de segurança de TO; (2) conciliar evidências conflitantes de dados de rede, de host e de processo; (3) avaliar criticamente as alegações de fornecedores e de alertas; e (4) escrever uma avaliação de evidências que declare níveis de confiança.

### 3.1 As fontes e os seus pontos cegos

As capturas passivas de rede mostram quem falou com quem, mas não veem enlaces seriais nem o significado de cargas cifradas. Os registros de eventos dos controladores, quando existem, mostram mudanças de programa, mas muitas vezes são sobrescritos depois de algumas centenas de entradas. Os dados de processo no historiador mostram o efeito físico, mas não a causa. As trilhas de auditoria da IHM mostram as ações dos operadores, mas não as sessões das ferramentas de engenharia. O trabalho com evidências especializadas combina essas fontes porque cada uma deixa algo de fora.

Antes de confiar numa fonte, anote o que ela consegue e o que não consegue ver na BWRP. A captura cobre a rede da planta, mas não um técnico no painel de dosagem. O registro de eventos do PLC-D pode ter sido sobrescrito desde o evento. O historiador registra o setpoint, mas não quem o mudou. Essa lista diz a Daniel qual segunda fonte consultar para cada pergunta.

### 3.2 Conflitos são informação

Se o historiador mostra uma mudança de setpoint da dosagem às 14:02, mas nem a trilha de auditoria da IHM nem a captura de rede mostram uma escrita, as possibilidades são uma captura com falhas, uma defasagem de relógio, uma mudança local no painel ou uma lógica que altera o setpoint internamente. Cada hipótese prevê algo verificável: os registros da chave seletora do painel, uma comparação do programa do CLP, os contadores de perda de pacotes da captura.

Escreva cada hipótese com a verificação que a descartaria e execute primeiro as verificações mais baratas. Uma defasagem de relógio pode ser testada em minutos, comparando os carimbos de tempo de um evento conhecido entre sistemas. Registre o resultado de toda verificação, inclusive das que apenas eliminam uma possibilidade, porque são elas que tornam a conclusão final crível.

### 3.3 Avaliando alegações externas

Os alertas de ICS da CISA descrevem produtos afetados, versões, pontuações CVSS e mitigações coordenadas com os fornecedores; são evidência forte sobre a existência de uma vulnerabilidade e mais fraca sobre se ela é explorável na sua configuração. As declarações de fornecedores de que um produto "não é afetado" merecem um pedido do raciocínio. Os estudos de medição revisados por pares, como a análise do Mirai de Antonakakis et al. (USENIX Security 2017), trazem seções de método que você pode avaliar.

Na BWRP, um alerta que afeta um produto usado no PLC-D deve levar a duas perguntas: a versão afetada está instalada, e a função vulnerável é alcançável a partir de onde um atacante poderia estar? Registre as respostas ao lado do alerta no inventário. Quando um fornecedor disser que o produto não é afetado, arquive o seu raciocínio com a data, para que a alegação possa ser verificada depois.

### 3.4 Declarações de confiança

Declare a confiança explicitamente: alta (várias fontes independentes concordam), moderada (uma fonte forte, sem contradição), baixa (inferência a partir de dados indiretos). Os líderes agem de forma diferente em cada caso.

Associe o nível a cada conclusão, e não ao relatório como um todo, e diga quais fontes a sustentam. A constatação de Daniel sobre as 14:02 tem confiança alta porque a captura, a comparação do programa e o registro da chave seletora concordam. Uma conclusão apoiada só no registro da chave seletora seria moderada, e um palpite sobre quem estava no local, antes de conferir as escalas, seria baixa.

### Exemplo resolvido (BWRP sintética)

Às 14:02, o historiador mostra o setpoint de dosagem de hipoclorito no PLC-D passando de 4,0 para 6,5 mg/L. Nenhuma entrada na auditoria da IHM, nenhuma escrita Modbus na captura. Daniel verifica: os contadores de perda da captura mostram 0 pacotes descartados; a comparação do programa do CLP mostra um programa inalterado; o registro da chave seletora do painel local mostra "modo local 14:01–14:05". Avaliação: confiança alta de que a mudança foi feita localmente no painel; próximo passo, identificar quem estava no local.

> **Caso sintético — Bayside Water Reclamation Plant.** Horários, tags e valores são inventados.

### Erros e limites

A ausência de evidência numa captura só tem significado se a cobertura e a perda da captura forem conhecidas. Os registros podem ser alterados por um invasor capaz.

### Exercícios

- **EX011 — Previsões a partir das hipóteses.** Para a hipótese "defasagem de relógio", declare que evidência a confirmaria. *Rubrica:* 3 = escrita correspondente encontrada no horário defasado na captura ou no registro da IHM, com a defasagem medida; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX012 — Confiança para evidência de uma única fonte.** A única evidência de um login remoto é uma linha do registro da VPN. Que confiança e por quê? *Rubrica:* 3 = moderada, no máximo, fonte única, pode ter sido alterada ou atribuída erroneamente; 2 = só o nível; 1 = alta; 0 = nenhum.
- **EX013 — Interpretar uma alegação de "não afetado".** Um fornecedor diz que sua RTU não é afetada pela falha de biblioteca de um alerta. O que você pergunta? *Rubrica:* 3 = qual versão/componente, por que é inalcançável, evidências (SBOM, análise); 2 = uma; 1 = aceita; 0 = nenhum.
- **EX014 — O que os contadores de perda da captura provam.** Por que Daniel verificou os contadores de perda de pacotes antes de confiar em "nenhuma escrita vista"? *Rubrica:* 3 = a ausência só tem significado se a captura estiver completa; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX015 — Ponto cego dos dados de processo.** Nomeie uma coisa que o historiador nunca pode dizer sobre a mudança das 14:02. *Rubrica:* 3 = quem ou o que a iniciou (causa/identidade); 2 = vago; 1 = errado; 0 = nenhum.

### Síntese

O trabalho com evidências especializadas triangula fontes com pontos cegos conhecidos, trata os conflitos como hipóteses a testar e associa uma confiança a cada conclusão.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 12

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Risco e ética avançados

### Objetivos de aprendizagem

Você vai (1) modelar distribuições de perdas em vez de números únicos; (2) ler as perdas média, do percentil 95 e do percentil 99 numa simulação com semente fixa; (3) decidir quem arca com o risco residual e se essas partes consentiram; e (4) lidar com a tensão ética entre transparência e segurança numa concessionária pública.

### 4.1 Distribuições em vez de estimativas pontuais

A perda anual por paradas de TO é quase sempre zero e, de vez em quando, grande. Uma simulação de Monte Carlo sorteia, muitos milhares de vezes, se um incidente acontece e quanto tempo ele dura, produzindo uma distribuição cuja cauda é o que interessa aos conselhos e às seguradoras.

```python
"""Lab 04: Monte Carlo of annual outage loss for BWRP with and without a control (seeded, synthetic)."""
import random, statistics
def year(rnd, p_incident, hours_lo, hours_hi, cost_per_hour=12_000):
    if rnd.random() >= p_incident: return 0.0
    return rnd.uniform(hours_lo, hours_hi) * cost_per_hour
for label, p, lo, hi in [("baseline", 0.15, 4, 72), ("with segmentation", 0.06, 4, 48)]:
    rnd = random.Random(2026)
    losses = sorted(year(rnd, p, lo, hi) for _ in range(20_000))
    print(f"{label:18} mean={statistics.mean(losses):>8,.0f} p95={losses[int(0.95*len(losses))]:>9,.0f} p99={losses[int(0.99*len(losses))]:>9,.0f} P(loss>0)={sum(l>0 for l in losses)/len(losses):.3f}")
```

Execute com `python3 lab_mc.py`. Saída verificada:

```text
baseline           mean=  68,613 p95=  592,662 p99=  814,425 P(loss>0)=0.151
with segmentation  mean=  18,590 p95=  129,339 p99=  493,624 P(loss>0)=0.059
```

A simulação precisa de poucas entradas: a probabilidade de um incidente num ano, quanto tempo ele dura e quanto custa cada hora. Cada uma deve vir com sua fonte e uma faixa plausível. O Laboratório 4 usa uma semente fixa para que o conselho veja os mesmos números quando a execução for repetida e para que uma mudança no resultado possa ser rastreada até uma mudança nos pressupostos.

### 4.2 Lendo a cauda

A segmentação reduz a perda média de cerca de 68.600 para 18.600 e a probabilidade de qualquer perda de 15,1 % para 5,9 %. O percentil 99 cai de forma menos acentuada (de 814.000 para 494.000), porque, quando um incidente acontece, ele ainda pode durar dois dias. Se a tolerância do conselho é "não mais do que 1 % de chance de perder mais de 600.000 num ano", apenas o desenho segmentado a atende sob esses pressupostos.

Esses números dependem de pressupostos que merecem uma linha própria no slide: as probabilidades de incidente, as faixas de duração e um custo único por hora. Mudar a duração máxima do desenho segmentado de 48 para 72 horas elevaria a sua cauda. O conselho deve ver qual pressuposto determina o resultado da tolerância antes de tratar o limiar de 600.000 como atendido.

### 4.3 Quem arca com o risco

O risco residual numa estação de recuperação de água não é suportado só pela concessionária. Os moradores perto dos pontos de lançamento e o ecossistema da baía arcam com o risco de qualidade do efluente; os contribuintes arcam com o risco de custos. Eticamente, um líder deve identificar essas partes, perguntar se o regulador ou o órgão eleito aceitou o risco em nome delas e evitar aceitar em nome de outros aquilo que a organização não tem mandato para aceitar.

Na BWRP, a ata do conselho deixou isso explícito ao registrar que o risco de qualidade do efluente para os moradores está sujeito às condições da licença do regulador. O papel de Daniel é tornar visíveis as partes afetadas no registro de riscos e declarar quem aceitou o risco em nome delas. Onde ninguém tem esse mandato, o risco é escalado, e não aceito em silêncio.

### 4.4 Transparência versus exposição

Publicar uma avaliação de segurança detalhada constrói confiança pública, mas pode dar um mapa aos atacantes. Uma prática defensável é a divulgação em camadas: publicar a governança, as decisões de aceitação de riscos e as métricas de progresso; compartilhar os detalhes técnicos com os reguladores e com os organismos setoriais de compartilhamento de informações sob confidencialidade; divulgar os incidentes conforme o dever legal e prontamente às pessoas afetadas.

Na BWRP, isso poderia significar publicar a decisão de adotar sessões intermediadas para fornecedores e os números de progresso da segmentação, compartilhando o desenho da rede das estações elevatórias apenas com o regulador e com o grupo setorial de compartilhamento. A escolha do que vai para onde deve ser registrada e revisada, para que pedidos posteriores de jornalistas ou moradores recebam uma resposta consistente.

### Exemplo resolvido (BWRP sintética)

Daniel apresenta a simulação com seus pressupostos num único slide: probabilidade anual de incidente de 15 % na linha de base (de pares do setor, faixa de 8–25 %), duração uniforme de 4–72 horas, custo de 12.000 por hora, semente 2026. O conselho aceita a segmentação e registra em ata que o risco de qualidade do efluente para os moradores é coberto pelas condições da licença do regulador, e não apenas pelo apetite a riscos do conselho.

> **Caso sintético — Bayside Water Reclamation Plant.** Todos os parâmetros da simulação são inventados.

### Erros e limites

Durações uniformes são uma simplificação; distribuições de cauda pesada elevariam o percentil 99. Uma simulação com semente fixa é reprodutível, não correta.

### Exercícios

- **EX016 — Interpretar a mudança no p99.** Explique por que, com a segmentação, o p99 cai proporcionalmente menos do que a média. *Rubrica:* 3 = a segmentação reduz principalmente a probabilidade de incidente; a cauda condicional da duração continua longa; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX017 — Verificar uma tolerância.** A linha de base atende a "P(perda > 600.000) ≤ 1 %"? Use a saída. *Rubrica:* 3 = não, p99 = 814.425 > 600.000, então mais de 1 % excede; 2 = só a conclusão; 1 = sim; 0 = nenhum.
- **EX018 — Nomear as partes afetadas.** Liste três partes, além da concessionária, que arcam com o risco residual de TO da BWRP. *Rubrica:* 3 = três partes relevantes; 2 = duas; 1 = uma; 0 = nenhum.
- **EX019 — Um plano de divulgação em camadas.** Atribua cada item a público, somente regulador ou interno: (a) declaração de apetite a riscos, (b) base de regras do firewall, (c) contagem anual de incidentes de TO. *Rubrica:* 3 = público, interno (ou regulador), público; 2 = dois; 1 = um; 0 = nenhum.
- **EX020 — Sensibilidade ao modelo de duração.** Preveja como substituir a duração uniforme de 4–72 h por uma distribuição de cauda mais pesada muda a média e o p99. *Rubrica:* 3 = o p99 sobe mais do que a média; efeito da cauda; 2 = só a direção; 1 = nenhuma mudança; 0 = nenhum.

### Síntese

O trabalho avançado de risco relata distribuições e caudas, nomeia quem arca com o risco residual e equilibra deliberadamente transparência e exposição.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 12

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Segurança de TO, IoT e sistemas ciberfísicos: alternativas de projeto

### Objetivos de aprendizagem

Você vai (1) gerar alternativas de projeto genuinamente diferentes para proteger estações elevatórias remotas; (2) avaliá-las segundo critérios operacionais, de segurança e de ciclo de vida; (3) usar os conceitos de zonas e conduítes da IEC 62443 para descrever cada uma; e (4) documentar por que as alternativas rejeitadas foram rejeitadas.

### 5.1 O problema

As 23 estações elevatórias da BWRP bombeiam esgoto para a planta. Cada uma tem uma RTU com um modem celular que relata níveis e o estado das bombas ao SCADA e aceita comandos de partida e parada. Alguns modems têm endereços IP públicos, o que os coloca na categoria de exposição que o ATT&CK for ICS chama de T0883 *Internet Accessible Device*.

Os comandos são o que mais importa. Uma leitura de nível falsa poderia esconder um transbordamento, mas uma parada remota enviada a uma bomba durante uma tempestade poderia causar um. Por isso, qualquer projeto precisa responder a duas perguntas: quem consegue chegar às RTUs e se os comandos remotos são de fato necessários. As respostas variam de estação para estação, e é por isso que as alternativas são comparadas estação por estação.

### 5.2 Três alternativas

Alternativa 1 — APN privado: a operadora fornece um nome de ponto de acesso privado, de modo que os modems não têm endereços públicos; o tráfego chega à BWRP por um túnel gerenciado pela operadora. Alternativa 2 — VPN do lado da RTU: cada RTU (ou um pequeno roteador ao lado dela) estabelece um túnel IPsec até um concentrador da BWRP na DMZ. Alternativa 3 — enlace apenas de monitoramento com controle local: os comandos remotos são removidos; as RTUs executam o controle de nível localmente e apenas relatam, e os operadores despacham equipes para as exceções.

Cada alternativa muda uma coisa diferente. A primeira remove os endereços públicos, mas mantém a confiança na operadora. A segunda acrescenta a criptografia e a autenticação da própria BWRP, ao custo de mais equipamentos. A terceira remove a capacidade mais arriscada, os comandos remotos, e aceita uma resposta mais lenta. Elas são genuinamente diferentes, e é isso que torna útil compará-las.

### 5.3 Avaliando-as

A alternativa 1 é rápida e barata, mas confia no isolamento da operadora. A alternativa 2 dá à BWRP sua própria fronteira criptográfica, mas acrescenta 23 dispositivos a corrigir e certificados a gerenciar. A alternativa 3 é a que mais encolhe a superfície de ataque — sem comandos remotos não há manipulação remota das bombas —, mas alonga a resposta a algumas falhas, o que as operações precisam aceitar. Nos termos da 62443, cada alternativa define um conduíte diferente entre as zonas das estações elevatórias e a zona do SCADA, com capacidades de segurança diferentes.

Coloque a avaliação numa tabela com os mesmos critérios para cada alternativa, como tempo de implantação, custo em cinco anos, efeito sobre a resposta a transbordamentos e exposição remanescente. Pontue cada classe de estação separadamente, porque uma estação à beira da praia, com alta consequência de transbordamento, justifica mais do que uma estação no interior cujo transbordamento fica contido.

### 5.4 Registrando as rejeições

Um registro de projeto lista as alternativas rejeitadas e o motivo. Caso contrário, os revisores futuros voltam a propô-las sem conhecer o histórico.

Na BWRP, o registro anota que a alternativa 3 foi rejeitada porque partidas remotas de bombas evitaram três transbordamentos no ano passado. Se as operações mudarem depois, por exemplo acrescentando armazenamento local ou controle automático nas estações de alta consequência, o motivo pode deixar de valer, e o registro diz ao próximo revisor exatamente qual condição verificar. Date o registro e nomeie quem concordou com a rejeição.

### Exemplo resolvido (BWRP sintética)

Daniel recomenda a alternativa 1 imediatamente (remove a exposição pública em um mês) e a alternativa 2 para as seis estações com maior consequência de transbordamento (perto das praias), com a alternativa 3 rejeitada porque as operações mostraram que partidas remotas de bombas evitaram três transbordamentos no ano passado.

> **Caso sintético — Bayside Water Reclamation Plant.** As contagens de estações e o histórico de transbordamentos são inventados.

### Erros e limites

Um APN privado não é criptografia; as redes internas das operadoras estão fora do controle da BWRP. As alternativas precisam ser testadas quanto aos efeitos da latência sobre a telemetria.

### Exercícios

- **EX021 — O registro da opção rejeitada.** Escreva a entrada de rejeição da alternativa 3. *Rubrica:* 3 = motivo com evidência e condições para reconsideração; 2 = só o motivo; 1 = "não escolhida"; 0 = nenhum.
- **EX022 — Pressuposto de confiança num APN privado.** Declare o pressuposto de confiança do qual a alternativa 1 depende. *Rubrica:* 3 = a operadora isola o tráfego do APN e gerencia o acesso corretamente; 2 = vago; 1 = tentativa mínima; 0 = nenhum.
- **EX023 — Custo de ciclo de vida das VPNs nas RTUs.** Liste duas tarefas recorrentes que a alternativa 2 acrescenta. *Rubrica:* 3 = renovação/rotação de certificados, correção do firmware dos roteadores (ou manutenção do concentrador); 2 = uma; 1 = tarefas pontuais; 0 = nenhum.
- **EX024 — Justificar uma solução híbrida.** Justifique aplicar a alternativa 2 apenas a seis estações. *Rubrica:* 3 = classificação por consequência, custo proporcional ao risco; 2 = parcial; 1 = só o custo; 0 = nenhum.
- **EX025 — Descrição do conduíte.** Descreva o conduíte da alternativa 2 na linguagem de zonas e conduítes. *Rubrica:* 3 = conduíte de cada zona de estação elevatória pelo túnel IPsec até o concentrador na DMZ e depois à zona do SCADA, com os controles declarados; 2 = parcial; 1 = "VPN"; 0 = nenhum.

### Síntese

Um bom trabalho de projeto produz alternativas reais, avalia-as ao longo do ciclo de vida, escalona a proteção pela consequência e lembra por que as opções foram rejeitadas.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 12

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Segurança de TO, IoT e sistemas ciberfísicos: avaliação controlada

### Objetivos de aprendizagem

Você vai (1) planejar uma comparação controlada de dois conjuntos de regras de alerta sobre o mesmo replay rotulado; (2) estimar a revocação e a taxa de alertas falsos de cada um; (3) calcular um intervalo de confiança de bootstrap para a diferença; e (4) decidir se as evidências justificam uma mudança em produção.

### 6.1 Os mesmos dados, dois tratamentos

Comparar o conjunto de regras A (atual) com o conjunto de regras B (proposto) em semanas diferentes de dados confunde as regras com as semanas. Uma avaliação controlada reproduz as mesmas janelas rotuladas nos dois. Os rótulos vêm de um plano de testes: 40 janelas contêm comportamento de ataque injetado no replay, e 160 são operação normal.

```python
"""Lab 06: controlled evaluation of two alerting rule sets on the same synthetic replay, with bootstrap CI."""
import random
rnd = random.Random(6)
# 200 labelled replay windows: (is_attack, alert_by_A, alert_by_B)
data = []
for i in range(200):
    att = i < 40
    a = rnd.random() < (0.70 if att else 0.08)
    b = rnd.random() < (0.85 if att else 0.05)
    data.append((att, a, b))
def recall(rows, k): at = [r for r in rows if r[0]]; return sum(r[k] for r in at) / len(at)
def far(rows, k): be = [r for r in rows if not r[0]]; return sum(r[k] for r in be) / len(be)
print(f"A recall={recall(data,1):.3f} false-alert rate={far(data,1):.3f}")
print(f"B recall={recall(data,2):.3f} false-alert rate={far(data,2):.3f}")
diffs = []
for _ in range(2000):
    s = [rnd.choice(data) for _ in data]
    if any(r[0] for r in s): diffs.append(recall(s, 2) - recall(s, 1))
diffs.sort()
print(f"recall difference B-A 95% bootstrap CI: [{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Execute com `python3 lab_ab.py`. Saída verificada:

```text
A recall=0.650 false-alert rate=0.069
B recall=0.850 false-alert rate=0.037
recall difference B-A 95% bootstrap CI: [0.000, 0.388]
```

O plano de testes deve ser escrito antes de o replay ser construído, nomeando os comportamentos de ataque, quantas janelas cada um recebe e quem as rotula. Idealmente, a pessoa que injeta os ataques não projetou nenhum dos conjuntos de regras. O Laboratório 6 faz esse papel com resultados aleatórios de semente fixa, então seus números mostram o método, e não o desempenho real das regras da BWRP.

### 6.2 Lendo o resultado

A revocação de B é 0,85 contra 0,65 de A, e sua taxa de alertas falsos é menor (3,7 % vs 6,9 %). O intervalo de bootstrap para a diferença de revocação vai de 0,000 a 0,388: a extremidade inferior toca o zero. Com apenas 40 janelas de ataque, não podemos descartar que B não seja melhor do que A em revocação, mesmo que a estimativa pontual o favoreça fortemente. Cada janela reamostrada carrega os resultados dos dois conjuntos de regras, então o bootstrap acima já preserva o pareamento; um teste exato sobre as janelas em que A e B discordam seria a verificação cruzada natural.

Relate as contagens ao lado das taxas, para que o leitor possa julgar as evidências: 34 de 40 contra 26 de 40 janelas de ataque, e 6 contra 11 de 160 janelas normais. Com tão poucas janelas de ataque, um punhado de resultados diferentes mudaria o quadro. Esse é o principal motivo pelo qual Daniel pede um replay maior e construído de forma independente antes da próxima revisão.

### 6.3 Tomando a decisão

Os líderes raramente precisam de certeza estatística para agir; precisam conhecer o risco de cada escolha. B é mais barato em alertas falsos e provavelmente melhor em revocação. A desvantagem de trocar — se B, na verdade, não fosse melhor — é pequena. Daniel recomenda a troca, ampliando o conjunto de janelas de ataque para 120 antes da próxima revisão.

A decisão fica mais fácil porque B também produz menos alertas falsos, que os operadores notam em todo turno. Daniel registra a recomendação com a sua incerteza, define a data da próxima revisão e nomeia o colega que vai construir as 120 janelas de ataque. Se o replay maior não mostrar vantagem em revocação, a decisão é revista, e não defendida.

### 6.4 Ameaças à validade

Os ataques injetados refletem a imaginação de quem escreveu os testes; adversários reais podem ser diferentes. O replay omite a reação dos operadores. O conjunto de regras B foi projetado depois de ver alguns desses tipos de ataque, o que o favorece.

Cada ameaça tem um remédio parcial. Peça a um colega que não projetou B que escreva novas janelas de ataque. Registre que o replay mede alertas, e não se os operadores agem com base neles. Registre quais tipos de ataque informaram o projeto de B e relate os resultados de B nesses tipos separadamente dos demais, para que o leitor veja se a sua vantagem se mantém em comportamentos não vistos.

### Exemplo resolvido (BWRP sintética)

Nota de avaliação de Daniel: "Replay R-6 (200 janelas, 40 de ataque, semente 6). B: revocação 34/40, alertas falsos 6/160. A: revocação 26/40, alertas falsos 11/160. IC de bootstrap de 95 % para a diferença de revocação [0,000, 0,388]. Recomendação: adotar B; ampliar para 120 janelas de ataque construídas por um colega que não projetou B."

> **Caso sintético — Bayside Water Reclamation Plant.** Os rótulos do replay e os resultados dos alertas são gerados pelo script com semente fixa.

### Erros e limites

Intervalos de bootstrap com poucos positivos são instáveis. Os resultados de alerta do laboratório são sorteios aleatórios que fazem as vezes do comportamento real das regras.

### Exercícios

- **EX026 — As contagens por trás das taxas.** Converta a taxa de alertas falsos de A, 0,069, numa contagem das 160 janelas normais. *Rubrica:* 3 = 11 de 160; 2 = ≈11; 1 = 0,069 × 200; 0 = nenhum.
- **EX027 — Interpretar um IC que toca o zero.** O que um limite inferior de 0,000 diz a quem decide? *Rubrica:* 3 = os dados são compatíveis com nenhuma melhora de revocação; incerteza vinda de 40 positivos; 2 = parcial; 1 = "B é melhor"; 0 = nenhum.
- **EX028 — Por que reproduzir as mesmas janelas?** Explique o benefício de um desenho pareado aqui. *Rubrica:* 3 = remove a variação de semana para semana; as diferenças se devem às regras; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX029 — Autoria independente dos ataques.** Por que um colega deve construir as novas janelas de ataque? *Rubrica:* 3 = evita o viés de projeto a favor de B; 2 = parcial; 1 = carga de trabalho; 0 = nenhum.
- **EX030 — Desvantagem assimétrica.** Argumente por que trocar para B é razoável apesar do intervalo. *Rubrica:* 3 = menos alertas falsos e revocação provavelmente melhor; custo pequeno se forem iguais; reversível; 2 = parcial; 1 = "estatisticamente provado"; 0 = nenhum.

### Síntese

Uma avaliação controlada pareia os tratamentos sobre dados rotulados idênticos, relata contagens e intervalos e permite que os líderes ajam de forma proporcional com evidências incertas, mas úteis.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 12

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Segurança de TO, IoT e sistemas ciberfísicos: integração organizacional

### Objetivos de aprendizagem

Você vai (1) desenhar papéis e responsabilidades de segurança de TO entre TI, operações e engenharia; (2) montar uma matriz RACI para os principais processos de segurança de TO; (3) integrar a segurança de TO à gestão de mudanças; e (4) definir métricas que induzam o comportamento certo.

### 7.1 O problema da responsabilidade

Em muitas concessionárias, a TI é dona da rede até um firewall, as operações são donas do processo, a engenharia é dona dos controladores e ninguém é dono do espaço onde eles se encontram. A NIST SP 800-82r3 recomenda uma equipe multifuncional para a segurança de TO, com autoridade claramente atribuída. Integrar significa escrever quem decide, e não apenas quem aconselha.

Na BWRP, esse espaço inclui o firewall da DMZ, o intermediador de sessões dos fornecedores e os enlaces celulares com as estações elevatórias. Cada um precisa de um responsável nomeado, com autoridade para aprovar mudanças e para agir num incidente. Pôr isso por escrito muitas vezes revela que duas equipes acreditavam que a outra era a dona, que é exatamente a lacuna que um atacante ou uma falha explora.

### 7.2 Uma RACI para três processos

Para a aprovação de acesso remoto: o supervisor de turno é Responsável (R) por habilitar as sessões; o líder de segurança de TO é Aprovador (A) da política; o gestor de fornecedores é Consultado (C); a segurança de TI é Informada (I) de cada sessão. Para a mudança da lógica de um CLP: engenheiro de controle R, gerente de engenharia A, operações C, segurança de TO I e alertada. Para a declaração de incidente de TO: supervisor de turno R por levantá-lo, diretor da planta A, segurança de TO e TI C, regulador I quando os limiares forem atingidos.

Verifique se cada linha tem exatamente um Aprovador e pelo menos uma pessoa que executa o trabalho. Compartilhe a tabela com todos os papéis que ela nomeia e pergunte se concordam; um papel que descobre pela tabela que é Aprovador de algo ainda não aceitou essa responsabilidade. Revise a RACI depois de mudanças organizacionais e depois de qualquer incidente que a tenha posto à prova.

### 7.3 Gestão de mudanças

Toda mudança num sistema de TO passa por um comitê de mudanças que já existe para segurança física e confiabilidade. Acrescentar três perguntas de segurança ao seu formulário — esta mudança acrescenta um conduíte, altera uma conta ou modifica um firmware? — integra a segurança sem uma burocracia paralela.

Cada resposta "sim" então dispara uma ação definida: um novo conduíte precisa de uma regra de firewall e de um responsável; uma conta alterada precisa de uma revisão de quem pode usá-la; um firmware modificado precisa de uma verificação contra os alertas do fornecedor e de uma cópia de segurança feita antes. O comitê já entende perguntas de segurança física e de confiabilidade, então as perguntas de segurança devem ser formuladas da mesma maneira.

### 7.4 Métricas

Meça aquilo de que você quer mais. "Número de vulnerabilidades" recompensa não olhar. Melhor: porcentagem de ativos de TO no inventário com versões de firmware conhecidas; mediana de dias para aplicar correções de TO de alto risco dentro das janelas disponíveis; porcentagem de sessões de fornecedores com gravações revisadas. Cada métrica nomeia um denominador.

Cada métrica também precisa de uma linha de base e de uma data-alvo. O painel da BWRP parte de 14 de 23 RTUs no inventário e de 0 de 37 sessões de fornecedores revisadas desde março, de modo que o progresso fica visível desde o primeiro relatório. Revise cada definição com as pessoas que ela mede, para que a métrica mude o comportamento, e não apenas o relato.

### Exemplo resolvido (BWRP sintética)

Plano de integração de Daniel: o líder de segurança de TO se reporta ao diretor da planta, com linha pontilhada para o CISO; o formulário do comitê de mudanças ganha três perguntas; o painel trimestral mostra a completude do inventário (hoje, 14/23 RTUs mais 41/41 ativos da planta), a taxa de revisão das sessões de fornecedores (hoje, 0/37 sessões revisadas desde março) e a atualidade dos testes de restauração.

> **Caso sintético — Bayside Water Reclamation Plant.** A estrutura e os números são inventados.

### Erros e limites

As tabelas RACI falham se duas partes forem Aprovadoras ao mesmo tempo. As métricas podem ser manipuladas; revise as definições anualmente.

### Exercícios

- **EX031 — Detectar um erro na RACI.** Um rascunho lista tanto a segurança de TI quanto o diretor da planta como Aprovadores da declaração de incidente. O que está errado e como corrigir? *Rubrica:* 3 = apenas um Aprovador; diretor A, TI C; 2 = só o problema; 1 = aceita; 0 = nenhum.
- **EX032 — Três perguntas para o comitê de mudanças.** Reescreva as três perguntas de segurança de modo que um não especialista consiga respondê-las com sim/não. *Rubrica:* 3 = três perguntas claras de sim/não; 2 = duas; 1 = jargão; 0 = nenhum.
- **EX033 — Uma métrica que sai pela culatra.** Explique como "zero constatações de TO em aberto" poderia sair pela culatra. *Rubrica:* 3 = desestimula relatar/encontrar; incentiva encerrar sem corrigir; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX034 — Número da completude do inventário.** Calcule a completude combinada do inventário da BWRP. *Rubrica:* 3 = 55/64 ≈ 85,9 %; 2 = fração correta; 1 = só 14/23; 0 = nenhum.
- **EX035 — Escolha da linha de reporte.** Dê uma vantagem de o líder de segurança de TO se reportar ao diretor da planta, e não ao CISO. *Rubrica:* 3 = autoridade sobre as decisões de operações, contexto do processo; 2 = vago; 1 = tentativa mínima; 0 = nenhum.

### Síntese

Integração é autoridade explícita, perguntas de mudança incorporadas ao processo e métricas com denominadores que recompensam encontrar e corrigir.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 12

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Segurança de TO, IoT e sistemas ciberfísicos: casos difíceis

### Objetivos de aprendizagem

Você vai (1) liderar uma resposta quando a contenção e a segurança do processo entram em conflito; (2) lidar com um cenário de ameaça interna com justiça e evidências; (3) gerenciar o comprometimento de um fornecedor que afeta vários sites; e (4) comunicar-se sob incerteza com reguladores e com o público.

### 8.1 Quando a contenção põe o processo em risco

Suponha que as evidências sugiram um invasor no servidor SCADA da BWRP durante uma tempestade, quando as estações elevatórias precisam de partidas remotas das bombas para evitar transbordamentos. Desconectar o SCADA detém o invasor e, junto, o controle remoto dos operadores. O trabalho do líder é escolher a opção menos ruim: manter o SCADA conectado sob vigilância reforçada, com verificação manual de cada comando; despachar equipes para as estações de alta consequência para assumir o controle local; depois isolar. A NIST SP 800-82r3 enfatiza que a resposta a incidentes de TO precisa pesar o impacto das ações de resposta sobre a segurança física e a operação.

### 8.2 Ameaças internas

Uma mudança local inexplicada num painel de dosagem (o exemplo do Capítulo 3) pode ser um ajuste bem-intencionado de um técnico ou uma sabotagem. Trate-a primeiro como um desvio de processo, colete evidências sem acusar, envolva os recursos humanos e o jurídico antes das entrevistas e lembre-se de que culturas de culpa fazem as pessoas esconderem erros, o que é pior para a segurança.

Na BWRP, as evidências já apontavam para uma mudança local durante um período em que o painel estava em modo local. O próximo passo é conferir as escalas e as ordens de serviço daquela janela e perguntar ao técnico o que ele estava fazendo, conduzindo a conversa como uma revisão de processo. Só se a explicação não se encaixar é que o caso se torna uma questão disciplinar ou jurídica.

### 8.3 Comprometimento de fornecedor

Se um fornecedor de SCADA anuncia que seu servidor de atualizações distribuiu software adulterado, toda concessionária que o usa precisa determinar sua exposição. Os líderes precisam de um inventário das versões instaladas e de um registro da origem das atualizações. O compartilhamento de informações no setor ajuda; uma relação já existente com a equipe de segurança do fornecedor também.

Na BWRP, a primeira pergunta seria quais servidores SCADA e estações de engenharia receberam atualizações da fonte afetada, e quando. Isso exige registros mantidos antes do anúncio, e é por isso que o trabalho de inventário da lista de lacunas importa. Os contatos com a equipe de segurança do fornecedor e com o grupo setorial de compartilhamento devem ser estabelecidos antes de uma crise, não durante.

### 8.4 Comunicar sob incerteza

Diga aos reguladores o que você sabe, o que não sabe, o que está fazendo e quando vai atualizar. Evite tanto as garantias que você não consegue sustentar quanto as especulações sobre autoria.

Na BWRP, a declaração preliminar da 01:00 na noite da tempestade seguiu esse padrão: uma sessão desconhecida a partir do servidor SCADA, equipes nas estações à beira da praia, o caminho externo cortado e o horário da próxima atualização. Ela não fez nenhuma alegação sobre quem era o responsável. Prepare modelos para essas declarações com antecedência, para que possam ser emitidas depressa sem redação descuidada.

### Exemplo resolvido (BWRP sintética)

Noite de tempestade, 23:40: o monitoramento alerta para uma sessão de saída desconhecida a partir do servidor SCADA. Daniel e o supervisor de turno concordam: equipes nas seis estações à beira da praia até 00:30 para o controle local; o SCADA continua conectado, com verificação por duas pessoas de cada comando remoto; às 00:35, com o controle local confirmado, o caminho externo do SCADA é cortado no firewall da DMZ. O regulador recebe uma declaração preliminar à 01:00, conforme os termos de notificação da licença.

> **Caso sintético — Bayside Water Reclamation Plant.** O evento e os horários são inventados.

### Erros e limites

A verificação por duas pessoas desacelera as operações; é uma medida temporária. As declarações preliminares não devem ser atrasadas para aperfeiçoá-las.

### Exercícios

- **EX036 — Sequenciar a resposta na noite da tempestade.** Explique por que as equipes foram despachadas antes de cortar o caminho externo. *Rubrica:* 3 = manter a prevenção de transbordamentos por controle local antes de perder o controle remoto; 2 = parcial; 1 = rapidez; 0 = nenhum.
- **EX037 — Primeiros passos diante de uma possível ameaça interna.** Liste as três primeiras ações depois da mudança inexplicada no painel. *Rubrica:* 3 = colocar o processo em estado seguro/verificar o setpoint, preservar as evidências, envolver RH/jurídico antes das entrevistas; 2 = duas; 1 = acusar; 0 = nenhum.
- **EX038 — A pergunta da exposição ao fornecedor.** Quais dois registros permitem à BWRP responder "fomos afetados pela atualização adulterada?" *Rubrica:* 3 = versão instalada por host e histórico da origem/data das atualizações; 2 = um; 1 = lista de fornecedores; 0 = nenhum.
- **EX039 — Uma declaração preliminar.** Redija uma declaração preliminar de três frases para o regulador. *Rubrica:* 3 = o que se sabe, o que não se sabe, as ações e o horário da próxima atualização; 2 = três dos quatro; 1 = especulativa; 0 = nenhum.
- **EX040 — Encerrar a verificação por duas pessoas.** Declare um critério para encerrar a medida temporária. *Rubrica:* 3 = caminho do invasor fechado e integridade do SCADA verificada (por exemplo, reconstrução limpa ou hashes verificados), com aprovação do responsável; 2 = parcial; 1 = só baseado em tempo; 0 = nenhum.

### Síntese

Os casos difíceis exigem um sequenciamento que mantenha o processo seguro, justiça com as pessoas, inventários que respondam às perguntas sobre fornecedores e comunicação honesta.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 12

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Segurança de TO, IoT e sistemas ciberfísicos: liderança e garantia

### Objetivos de aprendizagem

Você vai (1) estruturar um argumento de garantia (assurance) de uma alegação principal até as evidências; (2) encontrar mecanicamente as alegações sem sustentação; (3) distinguir garantia de conformidade; e (4) apresentar a um conselho a situação da garantia sem exagerá-la.

### 9.1 Alegações, argumentos, evidências

Um caso de garantia enuncia uma alegação principal ("o risco de TO da BWRP é aceitável"), decompõe-na em subalegações e sustenta cada folha com evidências: relatórios de teste, revisões de configuração, registros de simulados. A Goal Structuring Notation é uma forma gráfica comum. O valor está em que toda lacuna fica visível como uma alegação sem nada embaixo.

```python
"""Lab 09: check a synthetic assurance argument: every claim needs evidence or fully supported sub-claims."""
arg = {
    "G1 BWRP OT risk is acceptable": ["G2 remote access controlled", "G3 dosing integrity protected", "G4 recovery tested"],
    "G2 remote access controlled": ["E1 broker config review 2026-09", "E2 session log sample"],
    "G3 dosing integrity protected": ["G5 setpoint limits enforced", "G6 writes monitored"],
    "G5 setpoint limits enforced": ["E3 bench test report"],
    "G6 writes monitored": [],
    "G4 recovery tested": ["E4 restore drill 2025-11"],
}
def supported(node, path=()):
    if node.startswith("E"): return True
    kids = arg.get(node, [])
    return bool(kids) and all(supported(k, path + (node,)) for k in kids)
for g in arg:
    print(f"{g:34} {'supported' if supported(g) else 'UNSUPPORTED'}")
```

Execute com `python3 lab_assure.py`. Saída verificada:

```text
G1 BWRP OT risk is acceptable      UNSUPPORTED
G2 remote access controlled        supported
G3 dosing integrity protected      UNSUPPORTED
G5 setpoint limits enforced        supported
G6 writes monitored                UNSUPPORTED
G4 recovery tested                 supported
```

Escrever o argumento dessa forma torna precisa a pergunta do conselho. Em vez de perguntar se a segurança de TO é boa, ela pergunta quais alegações estão sustentadas e quais não estão. Cada evidência também precisa de um responsável e de uma data, para que o caso possa ser atualizado. O argumento da BWRP no Laboratório 9 é deliberadamente pequeno, para mostrar a estrutura antes de ela crescer.

### 9.2 Lendo a verificação

G6 "escritas monitoradas" não tem evidência nem subalegações, então não está sustentada. G3 depende de G6 e por isso falha, e a alegação principal G1 falha junto. G2 e G4 estão sustentadas. A verificação é estrita de propósito: para um conselho, uma alegação principal não pode ser parcialmente verdadeira.

A verificação testa apenas a estrutura. Ela não consegue dizer se o teste de bancada de E3 era o teste certo, nem se a amostra de registros de sessão de E2 era grande o bastante. Esses são julgamentos para um revisor. Use a verificação mecânica para encontrar lacunas depressa e depois leia cada evidência para ver se ela realmente sustenta a sua alegação.

### 9.3 Garantia não é conformidade

A conformidade mostra que os controles exigidos existem. A garantia argumenta que o risco é aceitável dadas as ameaças e as consequências reais do sistema. Uma planta pode estar em conformidade com uma lista de verificação e ainda assim ter uma alegação sem sustentação na sua malha mais importante — aqui, a integridade da dosagem.

A BWRP poderia passar numa lista de verificação que pergunta se o acesso remoto é controlado e se a recuperação é testada, porque G2 e G4 estão sustentadas, enquanto a alegação que mais importa para os moradores, a integridade da dosagem, continua sem sustentação. A garantia coloca essa lacuna no topo do documento para o conselho, onde um relatório de conformidade a teria escondido entre os itens aprovados.

### 9.4 Atualidade das evidências

As evidências envelhecem. Um simulado de restauração de 2025-11 sustenta G4 hoje; daqui a dois anos, não sustentará. Os casos de garantia maduros associam um período de validade a cada item e fazem falhar as alegações cujas evidências expiraram.

Defina o período de validade pela rapidez com que a evidência pode se tornar errada. Uma revisão da configuração do intermediador pode precisar ser repetida depois de toda mudança importante, enquanto um simulado de restauração pode valer por um ano. Acrescente as datas de expiração ao próprio argumento, para que a verificação do Laboratório 9 possa marcar uma alegação como sem sustentação quando a sua evidência caducar.

### 9.5 Reportando a um conselho

Relate: a situação da alegação principal (ainda não sustentada), qual subalegação a bloqueia, que evidência está planejada e quando. Evite cores vermelho-âmbar-verde sem as alegações subjacentes; a cor esconde o raciocínio.

O documento de Daniel para o conselho segue essa estrutura. Ele diz claramente que G1 ainda não está sustentada, nomeia G6 como a alegação que bloqueia, dá a data até a qual a evidência existirá e identifica a evidência compensatória até lá. Um conselheiro consegue fazer uma pergunta mais precisa a partir desse documento do que a partir de uma única luz âmbar.

### Exemplo resolvido (BWRP sintética)

Documento de Daniel para o conselho: "G1 ainda não está sustentada porque o monitoramento de escritas no PLC-D (G6) não tem evidência. Planejado: implantar monitoramento passivo na rede de dosagem até janeiro e anexar a revisão dos alertas do primeiro mês como evidência E5. Até lá, a evidência compensatória é E3 (teste de bancada dos limites de setpoint)."

> **Caso sintético — Bayside Water Reclamation Plant.** A estrutura do argumento e os identificadores das evidências são inventados.

### Erros e limites

Uma árvore sustentada vale tanto quanto a relevância das suas evidências; um relatório de teste pode ser associado à alegação errada. As verificações mecânicas não julgam a qualidade das evidências.

### Exercícios

- **EX041 — Consertar a árvore.** Acrescente a evidência "E5 monitoring review 2027-01" sob G6. O que o laboratório imprime para G1? *Rubrica:* 3 = supported (todos os ramos agora chegam a evidências); 2 = correto, mas sem razão; 1 = continua UNSUPPORTED; 0 = nenhum.
- **EX042 — Uma regra de expiração.** Escreva uma regra que faça falhar evidências com mais de 18 meses e diga qual item falharia primeiro. *Rubrica:* 3 = a regra mais E4 (2025-11) como a mais antiga; 2 = um dos dois; 1 = vago; 0 = nenhum.
- **EX043 — Conformidade sem garantia.** Dê um exemplo em que a BWRP passa numa lista de verificação, mas G3 continua sem sustentação. *Rubrica:* 3 = a lista pede firewall/política, não o monitoramento de escritas da dosagem; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX044 — Evidência mal associada.** Explique por que associar um teste de intrusão da TI corporativa a G3 seria errado. *Rubrica:* 3 = não é relevante para a integridade da rede de dosagem; sistema diferente; 2 = parcial; 1 = aceitável; 0 = nenhum.
- **EX045 — Uma frase para o conselho.** Escreva uma frase que relate a situação de G1 sem códigos de cores. *Rubrica:* 3 = situação, alegação que bloqueia, plano e data; 2 = três; 1 = "âmbar"; 0 = nenhum.

### Síntese

A garantia torna auditáveis as alegações da liderança: toda alegação principal se decompõe em evidências atuais e relevantes, e as lacunas são relatadas como lacunas.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 12

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Leitura e crítica de pesquisa

### Objetivos de aprendizagem

Você vai (1) criticar o modelo de ameaça, o método e a avaliação de um artigo de segurança de TO revisado por pares; (2) julgar se os resultados se transferem para a sua organização; (3) fazer a síntese entre artigos; e (4) escrever uma crítica estruturada que um público de profissionais possa usar.

### 10.1 Escolhendo os artigos

Leia pesquisa primária que trate de uma decisão em aberto. Para o programa de detecção da BWRP, dois artigos enquadram o campo: Giraldo et al. (2018, *ACM Computing Surveys*, doi:10.1145/3203245), um levantamento da detecção de ataques baseada em física em sistemas ciberfísicos, e Urbina et al. (2016, ACM CCS, doi:10.1145/2976749.2978388), que defende avaliar os detectores pelo impacto que um atacante não detectado consegue obter.

Parta de uma decisão em pauta, como a forma de avaliar o monitor de dosagem planejado da BWRP, e escolha artigos que tenham relação com ela. Um levantamento dá o mapa, e um artigo focado dá um método para testar. Anote por que cada artigo foi escolhido, para que a lista de leitura possa ser revista quando a decisão mudar.

### 10.2 Criticando o modelo de ameaça

Pergunte o que o atacante pode observar, mudar e saber. Urbina et al. consideram um atacante que conhece o detector e fica abaixo do seu limiar — um pressuposto forte, mas realista para atores com muitos recursos. Um artigo que testa apenas ataques ingênuos superestima o valor do detector.

Para a BWRP, o atacante relevante é aquele que consegue mudar os valores de dosagem ou as leituras que os relatam. Escreva as capacidades desse atacante na crítica e compare-as com as do artigo. Se um artigo pressupõe que o atacante não consegue ver o detector, diga se isso é plausível para um caminho de acesso de fornecedor que chega ao PLC-D.

### 10.3 Criticando o método e a avaliação

Verifique a bancada ou o conjunto de dados (simulado, de laboratório ou operacional), as métricas, as linhas de base comparadas e se os limiares foram ajustados nos dados de avaliação. Levantamentos como o de Giraldo et al. são especialmente úteis para perceber hábitos do campo inteiro — por exemplo, métricas inconsistentes que tornam os artigos difíceis de comparar.

Anote o que a avaliação de cada artigo realmente mede e compare com o que a BWRP precisa saber. Um detector avaliado pela acurácia em dados balanceados diz pouco sobre os alertas falsos numa planta onde os ataques são raros. Anote também se os autores relatam o impacto que um atacante conseguiria obter permanecendo não detectado, a medida que Urbina et al. defendem.

### 10.4 Transferência para a prática

Mesmo um artigo sólido pode não se transferir. A detecção baseada em física precisa de um modelo do processo; o tratamento biológico da BWRP é lento e não linear, ao contrário das malhas mais rápidas de muitas bancadas. A transferência exige perguntar: o nosso processo tem a dinâmica, os sensores e a qualidade de dados que o método pressupõe?

Responda a cada pergunta com evidências da BWRP: quais sensores existem na malha de dosagem, com que frequência eles relatam e quão ruidosas são as leituras. Se as respostas ficarem aquém do que o método precisa, a transferência pode exigir novos instrumentos ou um modelo diferente. A crítica deve dizer qual, em vez de recomendar o método com base nos seus resultados publicados.

### 10.5 Escrevendo a crítica

Estrutura: pergunta e alegação; modelo de ameaça; método; evidências; transferência para a BWRP; o que testaríamos primeiro. Mantenha-a em duas páginas para os profissionais.

Cada parte deve ser curta e concreta. O parágrafo da transferência é o mais importante para os profissionais, porque diz o que precisaria ser verdade na BWRP para que os resultados do artigo se apliquem. Termine com um teste que a organização possa executar, como medir o desvio máximo de dosagem não detectado no seu próprio replay. Peça a um operador que a leia antes de ela circular.

### Exemplo resolvido (BWRP sintética)

A crítica de Daniel conclui: a métrica de impacto de Urbina et al. é a forma certa de avaliar o monitor de dosagem da BWRP, porque a malha de dosagem é onde um viés não detectado tem consequências de saúde pública; os resultados obtidos na bancada do artigo não se transferem diretamente, então a BWRP vai medir o desvio máximo de dosagem não detectado no seu próprio replay antes de escolher os limiares.

> **Caso sintético — Bayside Water Reclamation Plant.** A crítica é uma ilustração; os dois artigos são reais e seus DOIs foram verificados.

### Erros e limites

Resumos de artigos não são críticas. Não atribua a um artigo resultados que ele não relata; cite e referencie.

### Exercícios

- **EX046 — O pressuposto do atacante furtivo.** Por que pressupor que o atacante conhece o detector é razoável para a BWRP? *Rubrica:* 3 = atores capazes estudam seus alvos; documentação e fornecedores vazam; projeto conservador; 2 = parcial; 1 = não é razoável; 0 = nenhum.
- **EX047 — Verificar o ajuste no teste.** Que frase numa seção de método mostraria que os limiares foram ajustados nos dados de avaliação? *Rubrica:* 3 = limiares escolhidos para maximizar o desempenho no mesmo conjunto de dados relatado; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX048 — A pergunta da transferência para processos lentos.** Nomeie uma propriedade do processo que limita a transferência de resultados de detecção em malhas rápidas para o tratamento biológico. *Rubrica:* 3 = dinâmica lenta e não linear/constantes de tempo longas ou sensoriamento esparso; 2 = vago; 1 = errado; 0 = nenhum.
- **EX049 — Usar bem um levantamento.** Declare um uso apropriado e um uso inapropriado de Giraldo et al. *Rubrica:* 3 = apropriado: mapear o campo e encontrar artigos primários; inapropriado: citá-lo como evidência de que um detector específico funciona; 2 = um; 1 = vago; 0 = nenhum.
- **EX050 — O primeiro teste.** O que a BWRP deve testar primeiro depois de ler Urbina et al.? *Rubrica:* 3 = o desvio máximo de dosagem não detectado sob os limiares atuais no seu replay; 2 = parcial; 1 = taxa de detecção; 0 = nenhum.

### Síntese

A crítica avalia o modelo de ameaça, o método e a transferência e, depois, transforma um artigo no primeiro teste que a sua organização deve executar.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 12

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Projeto aplicado

### Objetivos de aprendizagem

Você vai (1) delimitar um projeto aplicado de segurança de TO dentro de uma restrição organizacional real; (2) planejar as partes interessadas, os marcos e os riscos; (3) entregar um artefato mais um dossiê de evidências; e (4) definir medidas de sucesso antes de começar.

### 11.1 Escolhendo o projeto

Um projeto aplicado de pós-graduação deve mudar algo numa organização, com o acordo escrito do responsável, e poder ser concluído num período letivo. Na BWRP, o projeto de Daniel é "monitoramento passivo de escritas para a rede de dosagem": ele fecha a alegação sem sustentação G6 do Capítulo 9, usa o método de avaliação do Capítulo 6 e a medida de impacto do Capítulo 10.

O projeto de monitoramento passa nesses testes. As operações e a engenharia são donas dos sistemas que ele toca e podem concordar com ele por escrito. Ele pode ser concluído em doze semanas. Fecha uma lacuna nomeada do caso de garantia, e o seu resultado será mensurável. Um projeto que só produz um relatório, sem mudar nada, não atenderia ao padrão.

### 11.2 Partes interessadas e restrições

As operações precisam aprovar o ponto de coleta do monitoramento (passivo, numa porta espelhada, instalado numa janela de manutenção). A engenharia fornece o mapa de registradores. A TI fornece o armazenamento dos registros. O regulador não precisa aprovar, mas verá os resultados no próximo relatório de garantia. A lista de restrições inclui: nenhum tráfego ativo na rede de dosagem, nenhuma mudança no PLC-D e retenção dos dados por 90 dias.

Escreva cada restrição como um teste que pode falhar e verifique-as a cada marco. Se a porta espelhada não puder ser instalada sem mexer na configuração do PLC-D, a restrição prevalece e o plano muda. Mantenha um breve registro das partes interessadas, com quem concordou com o quê e quando, porque o dossiê vai precisar dele.

### 11.3 Marcos e riscos

Semanas 1–2: acordo, ponto de coleta instalado e captura validada. Semanas 3–6: linha de base e regras. Semanas 7–9: avaliação controlada com um replay de ataques escrito de forma independente. Semanas 10–12: dossiê e passagem de responsabilidade. Riscos: perda de pacotes na porta espelhada (mitigação: monitorar os contadores de perda), fadiga de alertas dos operadores (mitigação: alertas primeiro para a segurança de TO durante 4 semanas), rotatividade da equipe (mitigação: runbook escrito).

Revise os riscos a cada marco e registre se cada mitigação está funcionando. Se a perda da captura não puder ser controlada até a semana 2, os resultados posteriores não seriam confiáveis, então o plano faz uma pausa em vez de levar adiante uma linha de base fraca. Proteja em particular as semanas 7 a 9, porque a avaliação é a primeira fase a ser espremida quando o trabalho anterior atrasa.

### 11.4 Medidas de sucesso

Definidas de antemão: perda da captura abaixo de 0,1 % ao longo de uma semana; revocação de pelo menos 0,8 no replay independente, com taxa de alertas falsos abaixo de 2 % das janelas normais; desvio máximo de dosagem não detectado relatado; runbook aceito pelas operações.

Registre essas medidas no acordo do projeto, com a data e as partes interessadas que as aceitaram. O desvio máximo de dosagem não detectado não tem meta, porque é uma constatação, não uma nota de aprovação, mas precisa ser relatado seja o que for que mostre. Não atingir uma medida é relatado como falha, como Daniel faz na semana 9.

### 11.5 O dossiê

O dossiê de evidências contém o acordo, a configuração, os relatórios de teste, os resultados da avaliação com intervalos, as questões em aberto e a passagem de responsabilidade. Ele se torna a evidência E5 do caso de garantia.

Organize o dossiê de modo que um revisor consiga acompanhar o projeto do acordo à passagem de responsabilidade sem precisar fazer perguntas. Inclua os números de perda da captura, as contagens da avaliação, a meta de alertas falsos não atingida na semana 9 e a nova execução. Quando ele se tornar evidência no caso de garantia, levará uma data, e o seu período de validade começa ali. Guarde-o nos registros controlados da planta.

### Exemplo resolvido (BWRP sintética)

Na semana 9, o replay independente dá revocação de 33/40 (0,825) e 4/160 alertas falsos (2,5 %): a meta de revocação é atingida, a de alertas falsos não. Daniel relata a falha, aperta uma regra que produziu três dos quatro alertas falsos e agenda uma nova execução, em vez de redefinir a meta.

> **Caso sintético — Bayside Water Reclamation Plant.** Os resultados do projeto são inventados.

### Erros e limites

Projetos em organizações vivas atrasam; proteja a fase de avaliação. Não deixe que as medidas de sucesso mudem depois que os resultados chegam.

### Exercícios

- **EX051 — Verificar as metas.** 33/40 e 4/160 atendem às medidas de sucesso? *Rubrica:* 3 = revocação sim (0,825 ≥ 0,8), alertas falsos não (2,5 % > 2 %); 2 = um certo; 1 = ambos sim; 0 = nenhum.
- **EX052 — Uma restrição e o seu motivo.** Explique "nenhum tráfego ativo na rede de dosagem" a um colega de TI. *Rubrica:* 3 = dispositivos legados podem se comportar mal; segurança da dosagem química; o passivo basta; 2 = parcial; 1 = política; 0 = nenhum.
- **EX053 — Mitigar a fadiga de alertas.** Por que encaminhar os alertas primeiro para a segurança de TO durante quatro semanas? *Rubrica:* 3 = ajustar os alertas falsos antes que os operadores os vejam; proteger a confiança; 2 = parcial; 1 = vago; 0 = nenhum.
- **EX054 — Conteúdo do dossiê.** Liste cinco itens para o dossiê. *Rubrica:* 3 = cinco relevantes; 2 = quatro; 1 = só o artefato; 0 = nenhum.
- **EX055 — Resistir à mudança da meta.** Um patrocinador sugere mudar a meta de alertas falsos para 3 % "já que estamos perto". Responda. *Rubrica:* 3 = manter a meta, relatar a falha, corrigir e executar de novo; explicar a integridade; 2 = parcial; 1 = concorda; 0 = nenhum.

### Síntese

Um projeto aplicado fecha uma lacuna real sob restrições reais, com o sucesso definido de antemão e relatado honestamente num dossiê que se torna evidência de garantia.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 12

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Revisão final e transferência

### Objetivos de aprendizagem

Você vai (1) revisar as decisões do curso como um portfólio; (2) transferir os métodos da BWRP para outro setor; (3) escrever um briefing de transferência para um sucessor; e (4) planejar o seu próprio desenvolvimento profissional contínuo em segurança de TO.

### 12.1 A visão de portfólio

Ao longo do curso, a BWRP tomou um conjunto de decisões: acesso intermediado de fornecedores (Cap. 1), prioridades das lacunas (Cap. 2), segmentação justificada pelo risco de cauda (Cap. 4), proteção escalonada das estações elevatórias (Cap. 5), conjunto de regras B (Cap. 6), RACI e métricas (Cap. 7), resposta na noite da tempestade (Cap. 8), o caso de garantia (Cap. 9) e o projeto de monitoramento (Cap. 11). Revisá-las juntas mostra se são consistentes: por exemplo, a integridade da dosagem aparece nos Capítulos 3, 9, 10 e 11 — sinal de que é a preocupação central da planta.

Procure tensões, além de consistência. Por exemplo, a decisão de segmentação e o projeto das estações elevatórias dependem ambos de mudanças de firewall e de conduítes, então seus cronogramas devem ser alinhados. A escolha do acesso de fornecedores e o caso de garantia dependem ambos das evidências do intermediador. Listar essas ligações mostra onde o atraso de uma decisão minaria outra.

### 12.2 Transferência para outro setor

Os métodos se transferem; os parâmetros, não. Ao passar para um operador de aquecimento urbano ou para uma fábrica de alimentos, o enquadramento de decisão, as distribuições de perdas, a avaliação controlada e a estrutura de garantia continuam valendo. O que muda: o modelo de consequências (perda de calor ou contaminação do produto em vez da qualidade do efluente), os reguladores, os protocolos dominantes e as normas de segurança em vigor.

Antes de transferir, anote os pressupostos que cada método assumiu na BWRP: probabilidades de incidente vindas de pares do setor de água, um custo por hora de parada e os comportamentos de ataque do replay. Cada um precisa ser substituído por números do novo setor. A estrutura de um registro de decisão ou de um caso de garantia se move sem mudanças; os números dentro deles, não.

### 12.3 Briefing de transferência

Um sucessor precisa de: as decisões em aberto e seus gatilhos de revisão, o caso de garantia com as evidências expiradas ou ausentes destacadas, as métricas e suas linhas de base, os relacionamentos (fornecedores, contatos no regulador, grupos setoriais de compartilhamento de informações) e os pontos fracos conhecidos. Duas páginas, com links para os registros completos.

Escreva o briefing para um leitor que nunca conheceu Daniel. Cada item em aberto deve nomear seu gatilho e sua data; cada métrica, seu denominador e sua linha de base; cada relacionamento, um contato e seu último uso. Aponte para os registros completos em vez de repeti-los e date o briefing na primeira linha.

### 12.4 Desenvolvimento contínuo

O campo se move: a NIST SP 800-82 foi revisada em 2023; as partes da IEC 62443 são atualizadas periodicamente; o MITRE ATT&CK for ICS acrescenta técnicas; a CISA publica alertas toda semana. Plano: acompanhar os alertas dos seus fornecedores, reler o resumo de mudanças de uma norma quando sair uma nova edição e apresentar um estudo de caso por ano aos pares.

Mantenha um breve registro do que você leu e do que mudou por causa disso, como um pressuposto revisto ou uma nova pergunta para um fornecedor. Revise o registro uma vez por ano com um colega. Desenvolvimento que não muda nada na prática é leitura; desenvolvimento que deixa um rastro nas suas decisões é o que mantém a credibilidade de um líder.

### Exemplo resolvido (BWRP sintética)

O briefing de transferência de Daniel começa assim: "Em aberto: D-2026-14, revisar se a estimativa de frequência de incidentes com fornecedores passar de 0,06 por ano ou após qualquer incidente de acesso remoto. Garantia: G1 sustentada desde fevereiro via E5; o simulado de restauração E4 expira em maio de 2027 — agendar agora. Métricas: inventário de RTUs 23/23 desde março; revisão de sessões de fornecedores 37/37. Ponto fraco: a correção do firmware dos roteadores das estações elevatórias não tem janela acordada com as operações."

> **Caso sintético — Bayside Water Reclamation Plant.** Todo o conteúdo do briefing é inventado.

### Erros e limites

Os briefings de transferência ficam desatualizados; date-os. As revisões de portfólio podem racionalizar escolhas passadas; procure contradições deliberadamente.

### Exercícios

- **EX056 — Detectar uma inconsistência.** Identifique uma tensão entre a decisão do Capítulo 5 e as métricas do Capítulo 7. *Rubrica:* 3 = os novos roteadores das RTUs (alternativa 2) acrescentam ativos/correções ainda não refletidos nas métricas; 2 = outra tensão plausível; 1 = vago; 0 = nenhum.
- **EX057 — Transferir o modelo de consequências.** Reescreva a preocupação central da BWRP para uma fábrica de alimentos. *Rubrica:* 3 = contaminação do produto/recall por manipulação da receita ou da temperatura; 2 = vago; 1 = igual à água; 0 = nenhum.
- **EX058 — A evidência que expira.** Quando o simulado de restauração precisa ser repetido para manter G4 sustentada sob a regra dos 18 meses? *Rubrica:* 3 = antes de maio de 2027; 2 = aproximadamente; 1 = errado; 0 = nenhum.
- **EX059 — Do que um sucessor precisa primeiro.** Escolha o item mais importante do briefing e justifique. *Rubrica:* 3 = escolha fundamentada (por exemplo, decisão em aberto com gatilho próximo ou ponto fraco); 2 = só a escolha; 1 = vago; 0 = nenhum.
- **EX060 — Um plano de desenvolvimento.** Escreva um plano anual de desenvolvimento com três itens. *Rubrica:* 3 = acompanhar alertas, revisar atualizações de normas, apresentação aos pares ou equivalente; 2 = dois; 1 = um; 0 = nenhum.

### Síntese

O curso termina onde a prática começa: um portfólio consistente de decisões, métodos que se transferem entre setores, um briefing datado para quem vier depois e um plano para continuar aprendendo.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 12

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. A Bayside Water Reclamation Plant, Daniel Osei e todos os números são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** 10.000 + 0,05 × 400.000 + 0,02 × 2.500.000 = 10.000 + 20.000 + 50.000 = 80.000 — ainda maior do que os 59.500 de B.

**EX002.** O cenário catastrófico pode ocorrer por caminhos que nenhuma opção de acesso remoto fecha, então gastar mais com acesso remoto não consegue reduzir o pior caso; o líder deve financiar uma salvaguarda independente (por exemplo, um limite alto de dosagem por fiação física) para mudar a cauda.

**EX003.** "Revisar se o fornecedor do intermediador relatar um incidente de segurança que afete o seu serviço de sessões, ou se o relatório de atestação do intermediador tiver mais de 12 meses."

**EX004.** Total de B = 35.000 + 400.000p + 0,005 × 2.500.000 = 47.500 + 400.000p. Igualando a 100.000, obtém-se p = 52.500 / 400.000 ≈ 0,131 por ano.

**EX005.** Se as estimativas críveis da probabilidade de incidente de A vão de 0,01 a 0,10 e a classificação entre A e B se inverte dentro dessa faixa, enquanto uma revisão de duas semanas dos registros de acesso dos fornecedores poderia estreitar a estimativa antes do prazo do contrato, adiar para fazer o estudo é melhor do que decidir agora.

**EX006.** Apenas documentada. Sem um registro de restauração, ela não pode ser contada como executada; peça o último registro de restauração ou agende um teste.

**EX007.** Nove RTUs não listadas não podem ser monitoradas, corrigidas nem incluídas na delimitação de incidentes, então a lacuna de inventário mina várias outras capacidades de uma vez, enquanto a lacuna do playbook afeta uma só; corrigir primeiro a habilitadora aumenta o valor de todo controle posterior.

**EX008.** Expectativa: as cópias de segurança de TO são restauráveis e testadas. Documentado: existe um procedimento de cópia de segurança. Executado: cópias semanais da lógica, sem teste de restauração. Lacuna: a restauração nunca foi demonstrada. Consequência: depois de um ransomware ou de uma corrupção da lógica, o tempo de recuperação é desconhecido e pode ser de dias. Responsável: engenheiro de sistemas de controle, teste até o fim do trimestre.

**EX009.** Quando a BWRP precisa demonstrar conformidade com um requisito contratual ou regulatório formulado com base na IEC 62443 (por exemplo, um esquema de certificação do programa de segurança do proprietário de ativos), ou quando integradores e fornecedores já usam os termos da 62443, a parte 2-1 alinha a comparação com essas obrigações.

**EX010.** Ela indica onde as lacunas são prováveis e dá exemplos concretos à liderança, mas não é uma opinião de garantia sobre o programa inteiro: as cinco práticas foram escolhidas por Daniel, podem não ser representativas, e as práticas não amostradas podem ser mais fracas ou mais fortes.

**EX011.** Uma escrita de setpoint no PLC-D aparece na captura ou na trilha de auditoria da IHM às 14:02 menos (ou mais) uma defasagem de relógio medida, e a mesma defasagem explica outros eventos pareados ao longo da manhã.

**EX012.** Moderada, no máximo: uma única fonte de registros sustenta um login, mas ele pode estar mal atribuído (conta compartilhada), ter sido alterado por um invasor ou estar errado no horário; a corroboração pelo jump host ou pela gravação da sessão elevaria a confiança.

**EX013.** Pergunte exatamente quais versões de firmware foram analisadas, se elas contêm a biblioteca afetada (e em qual versão, segundo o SBOM) e por que a função vulnerável é inalcançável — pedindo a análise ou as evidências de teste, e não apenas a conclusão.

**EX014.** "Nenhuma escrita na captura" só sustenta "nenhuma escrita pela rede" se a captura viu todos os pacotes; zero pacotes descartados na porta de monitoramento mostra que a ausência tem significado, e não que é uma falha de coleta.

**EX015.** Quem ou o que causou a mudança: o historiador registra o valor e o horário, não o usuário, o host ou a ação no painel que a iniciou.

**EX016.** A segmentação reduz principalmente a frequência dos incidentes (15 % → 6 %), mas, quando um acontece, sua duração ainda pode ser longa (até 48 h), então a cauda condicional encolhe menos do que a média, que é dominada pela frequência dos incidentes.

**EX017.** Não. O percentil 99 da linha de base é 814.425, então mais de 1 % dos anos simulados excede 600.000 — a tolerância é violada.

**EX018.** Os moradores perto do ponto de lançamento, os contribuintes que pagam os custos de recuperação e o ecossistema da baía (e os negócios que dependem dele, como os coletores de mariscos) — o regulador e os usuários de água a jusante também são aceitáveis.

**EX019.** (a) Público — mostra a governança. (b) Somente interno (compartilhado com o regulador, sob pedido, com confidencialidade) — é um mapa para o atacante. (c) Público — uma contagem agregada sustenta a prestação de contas sem revelar técnicas.

**EX020.** Uma cauda mais pesada acrescenta paradas raras e muito longas: a média sobe um pouco, mas o percentil 99 sobe muito mais, porque os anos extremos que definem o p99 se tornam mais extremos.

**EX021.** "Rejeitada: alternativa 3 (apenas monitoramento). Motivo: os registros das operações mostram que partidas remotas de bombas evitaram três transbordamentos no último ano; remover os comandos remotos elevaria o risco de transbordamento nas estações de alta consequência. Reconsiderar se o tempo de resposta das equipes cair abaixo de 20 minutos ou se o controle de nível local for atualizado com sensores redundantes."

**EX022.** Que a operadora mantém o tráfego do APN privado da BWRP isolado dos outros clientes e da internet, controla quais SIMs podem se juntar a ele e que a sua própria equipe e os seus sistemas não estão comprometidos.

**EX023.** Renovar e revogar os certificados de dispositivo dos 23 pontos de extremidade dos túneis e corrigir o firmware dos roteadores do lado das RTUs e do concentrador na DMZ.

**EX024.** As seis estações à beira da praia têm a pior consequência de transbordamento (saúde pública, interdições), então justificam o custo e o ônus de gestão mais altos da criptografia controlada pela BWRP, enquanto o APN privado dá uma redução de risco adequada para as estações de menor consequência.

**EX025.** Cada estação elevatória é a sua própria zona; o seu conduíte é um túnel IPsec do roteador da estação até um concentrador na zona da DMZ da BWRP, com autenticação mútua por certificados e um firewall que permite apenas o protocolo de varredura do SCADA seguir até a zona do SCADA.

**EX026.** 0,069 × 160 ≈ 11, então A gerou 11 alertas falsos nas 160 janelas normais (11/160 = 0,06875).

**EX027.** Os dados são compatíveis com B não ser melhor do que A em revocação: 40 janelas de ataque são poucas demais para excluir uma melhora nula, mesmo que a melhor estimativa seja 0,20 maior.

**EX028.** Os dois conjuntos de regras veem exatamente o mesmo tráfego, então as diferenças nos alertas vêm das regras, e não de semanas, clima ou modos de operação diferentes; a comparação pareada também permite que o bootstrap reamostre janelas com os dois resultados associados.

**EX029.** Daniel projetou B pensando em parte nesses tipos de ataque; janelas escritas por outra pessoa reduzem a chance de que o conjunto de teste seja inconscientemente moldado às forças de B.

**EX030.** B produz menos alertas falsos nos mesmos dados e muito provavelmente pega mais ataques; se na verdade for igual em revocação, a organização perde pouco e pode reverter, então o valor esperado da troca é positivo enquanto mais dados são reunidos.

**EX031.** Uma RACI precisa ter exatamente um Aprovador por processo. Mantenha o diretor da planta como Aprovador da declaração de um incidente de TO e torne a segurança de TI Consultada.

**EX032.** (1) Esta mudança vai permitir que algum dispositivo converse com um dispositivo com o qual não conseguia conversar antes? (2) Esta mudança vai acrescentar, remover ou alterar alguma conta de usuário ou senha? (3) Esta mudança vai instalar ou atualizar software ou firmware em algum dispositivo de controle?

**EX033.** As equipes podem parar de procurar problemas, registrar constatações como "aceitas" sem correção ou dividi-las em itens vagos, de modo que o painel mostra zero enquanto a exposição real cresce.

**EX034.** (14 + 41) / (23 + 41) = 55 / 64 ≈ 85,9 % — relatado junto com o número específico das RTUs, 14/23 (60,9 %), para que a lacuna não fique escondida pelos ativos da planta.

**EX035.** O diretor da planta controla as prioridades operacionais e as janelas de manutenção, então as recomendações do líder de segurança de TO chegam à pessoa que pode agendá-las, e as decisões são tomadas tendo em vista as consequências para o processo.

**EX036.** Cortar o caminho também remove o controle remoto das bombas pelos operadores; com as vazões de tempestade, perdê-lo poderia causar transbordamentos nas estações à beira da praia, então o controle local precisava estar estabelecido primeiro para manter o processo seguro.

**EX037.** (1) Confirmar que o setpoint de dosagem está no valor correto e que o processo está dentro dos limites; (2) preservar as evidências — comparação do programa do CLP, registro da chave seletora do painel, exportação do historiador com hashes; (3) envolver o RH e o jurídico antes de falar com as pessoas, tratando o caso como um desvio até que os fatos sejam estabelecidos.

**EX038.** Um registro, por host, das versões de software SCADA instaladas e um histórico de onde e quando cada atualização foi obtida (origem, data, hash) — juntos, mostram se uma versão adulterada foi instalada.

**EX039.** "Às 23:40, a BWRP detectou uma conexão de saída inesperada a partir do seu servidor SCADA; o tratamento e o bombeamento operam normalmente, sob controle local em seis estações. Ainda não sabemos se algum dado ou configuração foi alterado. A conexão externa foi fechada às 00:35, há uma investigação em andamento e enviaremos uma atualização até as 09:00."

**EX040.** Encerrar quando o caminho de acesso do invasor estiver confirmadamente fechado e o servidor SCADA tiver sido reconstruído a partir de mídia íntegra conhecida ou o seu software tiver sido verificado contra os hashes do fornecedor, com a aprovação do diretor da planta e do líder de segurança de TO.

**EX041.** Com E5 sob G6, G6 fica sustentada, então G3 (G5 e G6 ambas sustentadas) fica sustentada, e G1 imprime "supported", porque G2, G3 e G4 chegam todas a evidências.

**EX042.** Regra: extrair a data do rótulo de cada evidência e tratar um item como inválido se ele for de mais de 18 meses antes da data da avaliação. E4 (simulado de restauração, 2025-11) é a mais antiga e expiraria primeiro, em maio de 2027, fazendo falhar G4 e, portanto, G1.

**EX043.** Uma lista de verificação pode exigir uma política de firewall documentada e uma política de segurança de TO, ambas presentes na BWRP, sem perguntar se as escritas no controlador de dosagem são monitoradas; a BWRP está em conformidade enquanto G3, a alegação sobre a integridade da dosagem, continua sem evidências.

**EX044.** Um teste de intrusão da TI corporativa não diz nada sobre se os setpoints do PLC-D estão protegidos; ele cobre sistemas e ameaças diferentes, então associá-lo faria G3 parecer sustentada por evidências que não têm relação com a alegação.

**EX045.** "A BWRP ainda não pode alegar que o seu risco de TO é aceitável, porque as escritas no controlador de dosagem não são monitoradas; o monitoramento estará implantado em janeiro, e traremos a revisão do primeiro mês à reunião de fevereiro."

**EX046.** Atores com muitos recursos fazem reconhecimento e podem obter a documentação do fornecedor ou exportações de configuração; projetar para um atacante que conhece o detector evita uma segurança que depende do sigilo dos limiares e dá estimativas conservadoras para um processo de saúde pública.

**EX047.** Por exemplo: "Selecionamos o limiar que maximizou o F1 nos traços de teste" — ajustar e avaliar nos mesmos traços significa que o desempenho relatado é otimista.

**EX048.** O tratamento biológico tem constantes de tempo longas e respostas não lineares (horas, não segundos), então detectores baseados em resíduos ajustados em malhas rápidas de bancada podem ver os ataques só depois que o dano se acumula, e os modelos são mais difíceis de ajustar.

**EX049.** Apropriado: usá-lo para mapear as abordagens de detecção e localizar artigos primários e fragilidades comuns de avaliação. Inapropriado: citá-lo como prova de que um detector em particular funciona na BWRP, porque um levantamento relata as alegações de outros sem testá-las de novo.

**EX050.** Reproduzir os dados de dosagem da BWRP com um viés lento simulado e medir o maior desvio de dosagem que permanece abaixo dos limiares de alarme atuais ao longo de um período definido — o orçamento de impacto que um atacante não detectado tem hoje.

**EX051.** Revocação de 33/40 = 0,825 atende à meta de ≥ 0,8; 4/160 = 2,5 % de alertas falsos excede o limite de 2 %, então uma das duas medidas ainda não foi atingida.

**EX052.** Alguns controladores e RTUs da rede de dosagem são antigos e podem falhar com tráfego inesperado, e uma falha ali afeta a dosagem química da água tratada; uma captura passiva por porta espelhada dá a mesma visibilidade sem nenhuma chance de perturbar os dispositivos.

**EX053.** As primeiras semanas revelam regras ruidosas; se os operadores receberem esses alertas falsos, aprendem a ignorar o monitor. Encaminhar primeiro para a segurança de TO permite o ajuste, de modo que os operadores só vejam alertas que mereçam a sua confiança.

**EX054.** Acordo do responsável e escopo; configuração do ponto de coleta e da captura, com as medições de perda; conjunto de regras e sua versão; relatório da avaliação controlada com contagens e intervalos; questões em aberto, runbook e aprovação da passagem de responsabilidade.

**EX055.** "Definimos 2 % antes de ver os resultados, e mudar isso agora tornaria a medida de sucesso sem significado para o caso de garantia. A falha vem principalmente de uma regra; vou corrigi-la e executar de novo o replay independente, e relataremos o resultado de qualquer forma."

**EX056.** O Capítulo 5 acrescenta roteadores VPN em seis estações à beira da praia, mas as métricas de inventário e de correções do Capítulo 7 contam apenas as RTUs e os ativos da planta, então os novos roteadores poderiam ficar fora tanto do denominador do inventário quanto da métrica de latência de correções.

**EX057.** "Integridade dos parâmetros de temperatura de cozimento e de receita nos controladores da linha, porque uma manipulação poderia liberar produto contaminado e desencadear um recall" — substituindo a qualidade do efluente pela segurança dos alimentos.

**EX058.** E4 é de novembro de 2025, então, com uma validade de 18 meses, expira em maio de 2027; o simulado precisa ser repetido e documentado antes disso.

**EX059.** O ponto fraco da correção dos roteadores das estações elevatórias, porque é o único item sem nenhum processo acordado; as decisões em aberto já têm gatilhos e responsáveis, enquanto uma lacuna de correções sem dono cresce em silêncio.

**EX060.** (1) Revisar todo alerta de ICS da CISA que cite os fornecedores da BWRP até uma semana após a publicação. (2) Ler o resumo de mudanças de cada nova parte da IEC 62443 ou revisão da NIST SP 800-82 quando forem lançadas e atualizar a lista de lacunas. (3) Apresentar por ano um estudo de caso anonimizado da BWRP numa reunião setorial de compartilhamento de informações.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; normas e alertas são revisados, então verifique novamente as edições antes de citar. Os DOIs foram conferidos no Crossref.

- Antonakakis, M., et al. (2017). Understanding the Mirai Botnet. 26th USENIX Security Symposium. <https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/antonakakis>
- CISA. Cybersecurity advisories (ICS advisories are filterable). <https://www.cisa.gov/news-events/cybersecurity-advisories>
- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ISA/IEC 62443 series of standards (overview; part 2-1 and the zone and conduit concepts of part 3-2 are cited in the text). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS, including T0883 Internet Accessible Device. <https://attack.mitre.org/matrices/ics/>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
