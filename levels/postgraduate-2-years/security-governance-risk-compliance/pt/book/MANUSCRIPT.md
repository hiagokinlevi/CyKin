# Governança, Riscos e Compliance de Segurança: Curso de Pós-Graduação

- Idioma: português do Brasil (`pt`); curso 143, curso de pós-graduação (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho parcial em português**. Os capítulos 1–6 de 12 já estão escritos em português, com os exercícios EX001–EX030 e suas resoluções com rubricas de 0 a 3 e 2 laboratório(s) com saídas idênticas às da edição em inglês; os capítulos 7–12 (EX031–EX060) estão, por enquanto, apenas na [edição em inglês](../../en/book/MANUSCRIPT.md) e serão acrescentados em lotes. Os laboratórios usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos. Revisão independente, revisão linguística e a verificação de páginas A4 continuam em aberto.
- Público: profissionais em pós-graduação que querem melhorar o modo como uma organização quantifica o risco cibernético, supervisiona fornecedores e informa seu conselho.
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limites: os laboratórios executam um modelo de perdas Monte Carlo no estilo FAIR, um teste de permutação sobre a duração das revisões e uma comparação com o apetite, sempre sobre dados sintéticos. Os números de risco são ilustrações, as normas são citadas pela edição e parafraseadas, e nada aqui é auditoria, atestação ou aconselhamento jurídico reais; os relatórios SOC 2 descritos são fictícios. Pessoas, organizações, sistemas e dados são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Leia na ordem. Os capítulos acompanham um gestor de riscos ao longo de um curso de pós-graduação: tomada de decisão, prática atual, evidências quantificadas, ética, alternativas de desenho para a supervisão de fornecedores, uma avaliação controlada, integração, casos difíceis, apetite e garantia ao conselho, crítica de pesquisas, o projeto aplicado e a revisão final. Execute cada laboratório onde ele aparece, tente os exercícios antes de consultar as resoluções e avalie-se com as rubricas.

### Caso sintético

| Elemento | Papel | Natureza |
|---|---|---|
| **Daniel Mensah** | Estudante de pós-graduação e gestor de risco operacional | Inventado |
| **Dra. Elena Varga** | Tutora | Inventada |
| **Wexford School of Management** | Escola fictícia | Inventada |
| **Halbrook Mutual** | Seguradora fictícia, 2.000 funcionários, 300 fornecedores | Inventada |

### Fontes principais

Freund e Jones (2015), [doi:10.1016/C2013-0-09966-5](https://doi.org/10.1016/C2013-0-09966-5); Hubbard e Seiersen (2016), [doi:10.1002/9781119162315](https://doi.org/10.1002/9781119162315); Gordon e Loeb (2002); Cox (2008); Spears e Barki (2010); ISO 31000:2018 (no Brasil, ABNT NBR ISO 31000:2018); ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022); NIST [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); COBIT 2019; trust services criteria da AICPA. Lista completa em [Referências](#references).

## Sumário

| Capítulos em português |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |

Capítulos 7–12: [edição em inglês](../../en/book/MANUSCRIPT.md#ch-07), até a chegada dos próximos lotes.

[Resoluções](#worked-results) · [Referências](#references)

<a id="ch-01"></a>

## Capítulo 1 — Tomada de decisão avançada em segurança

### Objetivos de aprendizagem

Você vai (1) enquadrar as decisões de segurança como escolhas sob incerteza; (2) separar a qualidade da decisão da qualidade do resultado; (3) identificar vieses nas decisões de risco.

### 1.1 Decisões sob incerteza

Daniel Mensah é estudante de pós-graduação na fictícia Wexford School of Management e gestor de risco operacional na Halbrook Mutual, uma seguradora fictícia com dois mil funcionários e uma grande rede de corretores e fornecedores de sinistros. Sua tutora, a Dra. Elena Varga, abre o curso perguntando o que é uma boa decisão de segurança. Daniel aprende a descrever as decisões como escolhas entre opções com consequências incertas, julgadas pelo sentido que a escolha fazia diante das informações, dos valores e do tempo disponíveis. Na Halbrook isso importa porque o comitê de riscos revisa as decisões meses depois, quando só o registro do que se sabia na época pode mostrar se a escolha foi razoável.

### 1.2 Decisão e resultado

Uma boa decisão pode ter um mau resultado, e uma decisão ruim pode ter sorte. A Halbrook certa vez pulou a revisão de um fornecedor para cumprir um prazo, e nada deu errado; os gestores elogiaram a rapidez. Daniel aprende a julgar essa decisão pelo raciocínio, e não pelo resultado. Alguém estimou o risco? O apetite foi respeitado? A decisão foi registrada e revisitada? Separar as duas coisas protege as organizações de aprender a lição errada com a sorte e de punir decisões sólidas que deram errado. Daniel sugere que as revisões pós-decisão da Halbrook perguntem o que se sabia no dia em que a revisão foi pulada, e não só se houve uma violação depois.

### 1.3 Vieses

Daniel estuda os vieses que afetam as decisões de risco: a disponibilidade, em que manchetes recentes inflam alguns riscos; o excesso de confiança, em que os especialistas dão faixas estreitas demais; a ancoragem, em que um primeiro número molda as estimativas seguintes; e o otimismo sobre os próprios controles. Hubbard e Seiersen (2016) descrevem um treinamento de calibração para reduzir o excesso de confiança nas estimativas de segurança. Ele aprende que métodos estruturados, como registrar as premissas e pedir faixas, são defesas práticas contra o viés nos comitês. Para o comitê da Halbrook, propõe que toda estimativa venha como faixa, com sua fonte, para que a ancoragem no primeiro número dito fique visível.

### Exemplo resolvido

Daniel enquadra as escolhas de risco como decisões sob incerteza, julga a revisão de fornecedor pulada pelo raciocínio, e não pelo resultado, e lista quatro vieses.

> **Caso sintético.** A Wexford, a Halbrook e todos os números são sintéticos; Hubbard e Seiersen (2016) é real.

### Erros e limites

Os rótulos de viés podem ser usados para descartar opiniões. Os registros do raciocínio podem estar incompletos.

### Exercícios

- **EX001 — Boa decisão.** Como uma boa decisão de segurança deve ser julgada? *Rubrica:* 3 = pelo sentido da escolha diante das informações, dos valores e do tempo;; 2 = raciocínio;; 1 = resultado;; 0 = nenhuma.
- **EX002 — Pulo com sorte.** Por que elogiar a revisão de fornecedor pulada foi um erro? *Rubrica:* 3 = premiou a sorte, não o raciocínio;; 2 = sorte;; 1 = nada;; 0 = nenhuma.
- **EX003 — Excesso de confiança.** O que o excesso de confiança faz com as faixas dos especialistas? *Rubrica:* 3 = deixa-as estreitas demais;; 2 = estreitas;; 1 = largas;; 0 = nenhuma.
- **EX004 — Fonte da calibração.** Que fonte descreve o treinamento de calibração para estimativas de segurança? *Rubrica:* 3 = Hubbard e Seiersen (2016);; 2 = Hubbard;; 1 = Cox;; 0 = nenhuma.
- **EX005 — Defesa contra o viés.** Cite uma defesa prática contra o viés. *Rubrica:* 3 = registrar as premissas e pedir faixas;; 2 = estrutura;; 1 = nada;; 0 = nenhuma.

<a id="ch-02"></a>

## Capítulo 2 — Governança, riscos e compliance de segurança: prática atual

### Objetivos de aprendizagem

Você vai (1) levantar os frameworks atuais de GRC e seus usos; (2) avaliar a prática da Halbrook contra eles; (3) identificar as tendências que moldam a área.

### 2.1 Frameworks em uso

Daniel mapeia os frameworks usados na Halbrook. O programa de segurança segue a ISO/IEC 27001:2022 (no Brasil, ABNT NBR ISO/IEC 27001:2022) e tem certificação. O conselho recebe relatórios estruturados pelas funções do NIST CSF 2.0. A gestão de riscos corporativos segue os princípios da ISO 31000:2018 (ABNT NBR ISO 31000:2018). A auditoria interna usa o COBIT 2019 nas revisões de governança de TI. Os fornecedores entregam relatórios SOC 2 ou certificados ISO. Ele observa que cada framework responde a uma pergunta diferente e que as organizações maduras os combinam, em vez de escolher um só. A ISO 31000 diz à Halbrook como gerir riscos; o SOC 2 de um fornecedor diz quanto ela pode confiar nos controles dele.

### 2.2 A prática da Halbrook

Daniel avalia a prática da Halbrook com franqueza. As políticas e a certificação são maduras. A avaliação de riscos usa uma matriz cinco por cinco que o conselho tem dificuldade de comparar com os riscos financeiros. A supervisão de fornecedores depende de questionários que levam semanas e raramente são lidos a fundo. Os relatórios ao conselho são longos e, em sua maioria, listam atividades. Ele conclui que as fraquezas da Halbrook estão menos nos controles do que no modo de expressar o risco, de supervisionar os fornecedores e de informar o conselho. Essas três fraquezas viram os fios de seu trabalho posterior: curvas de excedência de perda, níveis de fornecedores e apetite quantificado para o conselho.

### 2.3 Tendências

Daniel identifica tendências: o interesse crescente em quantificar o risco cibernético em termos financeiros; reguladores que esperam que os conselhos supervisionem diretamente o risco cibernético, o que se reflete na função Govern do NIST CSF 2.0; a gestão de riscos da cadeia de suprimentos ganhando centralidade; e o monitoramento contínuo de controles substituindo as fotografias anuais. Ele aprende que as tendências devem ser pesadas contra a maturidade da organização, e que adotar um método da moda sem dados ou competências para sustentá-lo pode piorar a governança. A Halbrook, com certificação madura mas poucos dados de perdas, só pode adotar a quantificação começando por poucos cenários e faixas honestas.

### Exemplo resolvido

Daniel mapeia cinco frameworks em uso na Halbrook, encontra fraquezas na expressão do risco, na supervisão de fornecedores e nos relatórios ao conselho e identifica quatro tendências.

> **Caso sintético.** A prática da Halbrook é sintética; os frameworks citados são reais.

### Erros e limites

As listas de tendências envelhecem depressa. A autoavaliação pode ser generosa.

### Exercícios

- **EX006 — Estrutura do conselho.** Que framework estrutura os relatórios ao conselho da Halbrook? *Rubrica:* 3 = NIST CSF 2.0;; 2 = CSF;; 1 = COBIT;; 0 = nenhuma.
- **EX007 — Problema da matriz.** Por que o conselho tem dificuldade com a matriz cinco por cinco? *Rubrica:* 3 = é difícil compará-la com os riscos financeiros;; 2 = comparabilidade;; 1 = nada;; 0 = nenhuma.
- **EX008 — Fraqueza com fornecedores.** O que há de fraco na supervisão de fornecedores? *Rubrica:* 3 = questionários lentos, raramente lidos a fundo;; 2 = questionários;; 1 = nada;; 0 = nenhuma.
- **EX009 — Cautela com tendências.** Por que pesar as tendências contra a maturidade? *Rubrica:* 3 = métodos sem dados ou competências podem piorar a governança;; 2 = maturidade;; 1 = nada;; 0 = nenhuma.
- **EX010 — Combinar frameworks.** Por que as organizações maduras combinam frameworks? *Rubrica:* 3 = cada um responde a uma pergunta diferente;; 2 = complementares;; 1 = nada;; 0 = nenhuma.

<a id="ch-03"></a>

## Capítulo 3 — Governança, riscos e compliance de segurança: evidências especializadas

### Objetivos de aprendizagem

Você vai (1) montar uma estimativa quantitativa de risco no estilo FAIR; (2) interpretar uma distribuição de perdas; (3) explicar evidências especializadas a não especialistas.

### 3.1 A estrutura do FAIR

Daniel estuda o modelo FAIR descrito por Freund e Jones (2015), que decompõe o risco em frequência de eventos de perda e magnitude da perda, cada uma estimada como faixa. Para um cenário de vazamento de dados num fornecedor de sinistros, ele trabalha com as áreas de sinistros, jurídica e de TI para estimar a frequência entre um evento em dez anos e quase um por ano, mais provavelmente cerca de um a cada três anos, e uma magnitude de perda com mediana perto de trezentos mil e uma cauda longa vinda de multas regulatórias e de remediação. Essas faixas, e não valores únicos, viram as entradas da simulação da seção seguinte.

### 3.2 A simulação

O laboratório simula vinte mil anos. A perda anual média é de cerca de cento e setenta mil. Em sessenta e oito por cento dos anos não há perda alguma, então o ano mediano não custa nada. O percentil noventa fica em cerca de quinhentos e cinquenta e cinco mil, e o noventa e nove em cerca de um vírgula nove milhão. A chance de perder mais de um milhão num ano é de cerca de quatro por cento. Daniel observa que a média sozinha esconderia tanto os muitos anos tranquilos quanto a cauda grave. Uma mediana zero também explica por que gestores que nunca viram uma perda podem duvidar de que o cenário seja real.

### Laboratório — Distribuição de perdas por Monte Carlo para um cenário de vazamento em fornecedor

```python
"""FAIR-style Monte Carlo: loss event frequency x loss magnitude (synthetic, stdlib)."""
import random
random.seed(11)
N = 20000
def year():
    n = 0; t = random.expovariate(random.triangular(0.1, 0.8, 0.3))
    while t < 1: n += 1; t += random.expovariate(random.triangular(0.1, 0.8, 0.3))
    return sum(random.lognormvariate(12.6, 0.9) for _ in range(n))
L = sorted(year() for _ in range(N))
print(f"mean annual loss {sum(L)/N/1000:,.0f}k")
print(f"P(no loss) {sum(x == 0 for x in L)/N:.2f}")
for q in (0.5, 0.9, 0.99): print(f"{int(q*100)}th percentile {L[int(q*N)]/1000:,.0f}k")
print(f"P(loss > 1,000k) {sum(x > 1e6 for x in L)/N:.3f}")
```

Execute com `python3 lab_fair.py`. Saída verificada:

```text
mean annual loss 170k
P(no loss) 0.68
50th percentile 0k
90th percentile 555k
99th percentile 1,930k
P(loss > 1,000k) 0.041
```

### 3.3 Explicar o resultado

Daniel apresenta o resultado ao comitê de riscos como uma afirmação de excedência de perda: em cerca de um ano a cada vinte e cinco, as perdas desse cenário poderiam passar de um milhão. Ele explica que os números dependem de faixas estimadas, mostra as premissas e convida à contestação. Os membros do comitê o comparam com os riscos de seguro e de crédito que já administram. Ele aprende que as evidências especializadas convencem quando são traduzidas em termos familiares e quando sua incerteza fica visível, e não escondida. Ligar o número cibernético à forma como o comitê já lê as exposições de seguro torna a afirmação de um ano em vinte e cinco utilizável na mesma discussão.

### Exemplo resolvido

Daniel monta uma simulação no estilo FAIR com média de 170 mil, 68% de anos sem perda, percentil 99 de 1.930 mil e 4% de chance de passar de um milhão.

> **Caso sintético.** As faixas e os resultados são sintéticos; Freund e Jones (2015) é real.

### Erros e limites

As estimativas dependem das faixas dos especialistas. Os modelos omitem eventos correlacionados.

### Exercícios

- **EX011 — Decomposição do FAIR.** Em que dois fatores o FAIR decompõe o risco? *Rubrica:* 3 = frequência de eventos de perda e magnitude da perda;; 2 = dois;; 1 = nada;; 0 = nenhuma.
- **EX012 — Perda média.** Que perda anual média o laboratório relatou? *Rubrica:* 3 = cerca de 170 mil;; 2 = 170;; 1 = nada;; 0 = nenhuma.
- **EX013 — Anos tranquilos.** Em que proporção dos anos não houve perda? *Rubrica:* 3 = 68%;; 2 = 0,68;; 1 = nada;; 0 = nenhuma.
- **EX014 — Chance da cauda.** Qual é a chance de passar de um milhão num ano? *Rubrica:* 3 = cerca de 4%;; 2 = 0,041;; 1 = nada;; 0 = nenhuma.
- **EX015 — Persuasão.** O que torna as evidências especializadas convincentes para os comitês? *Rubrica:* 3 = tradução em termos familiares e incerteza visível;; 2 = tradução;; 1 = nada;; 0 = nenhuma.

<a id="ch-04"></a>

## Capítulo 4 — Risco avançado e ética

### Objetivos de aprendizagem

Você vai (1) identificar questões éticas na quantificação de riscos e na garantia; (2) lidar com conflitos de interesse; (3) proteger as pessoas afetadas pelas decisões de risco.

### 4.1 A ética dos números

Daniel considera as questões éticas da quantificação. Os números podem ser usados para justificar o corte de controles, escolhendo entradas otimistas, ou para assustar os conselhos e fazê-los gastar, com entradas pessimistas. Ele aprende que a prática ética significa documentar as fontes de cada estimativa, convidar a contestação independente e relatar as faixas com honestidade. Também observa que as pessoas afetadas pelos riscos, como os segurados cujos dados podem ser expostos, raramente aparecem nos modelos de perda, então seus interesses precisam de atenção explícita. No cenário de vazamento no fornecedor, ele acrescenta ao lado dos números um relato curto do dano aos segurados.

### 4.2 Conflitos de interesse

O papel de Daniel cria possíveis conflitos. Ele estima riscos de controles operados por sua própria equipe, e seu bônus depende em parte de cumprir metas orçamentárias. A Dra. Varga pergunta como ele vai lidar com isso. Ele propõe que a auditoria interna revise suas principais estimativas, que ele declare o conflito ao comitê de riscos e que as decisões orçamentárias sejam tomadas por pessoas diferentes de quem estima. Aprende que os conflitos são normais na prática e se tornam prejudiciais sobretudo quando escondidos. Também registra a declaração na ata do comitê, para que revisores futuros vejam que o conflito era conhecido quando as estimativas foram aceitas.

### 4.3 Proteger as pessoas

A Halbrook considera reduzir os custos de notificação de violações estreitando o que conta como incidente notificável. Daniel aponta que as obrigações de notificação vêm da lei e que estreitá-las prejudicaria os segurados, que precisam se proteger. Ele recomenda, em vez disso, investir numa detecção mais rápida para que os incidentes sejam menores, o que também reduz o número de segurados afetados, algo que a abordagem da notificação só teria escondido. Ele aprende que os profissionais de GRC às vezes precisam defender pessoas de fora da organização, e que cumprir a lei é um mínimo, e não a medida completa da conduta ética.

### Exemplo resolvido

Daniel documenta as fontes das estimativas, declara e mitiga seus conflitos e defende os interesses dos segurados nas decisões de notificação.

> **Caso sintético.** Os casos são sintéticos.

### Erros e limites

Os julgamentos éticos podem ser contestados. Conflitos declarados ainda influenciam.

### Exercícios

- **EX016 — Números mal usados.** Como os números podem ser mal usados na quantificação de riscos? *Rubrica:* 3 = entradas otimistas ou pessimistas escolhidas para justificar uma conclusão;; 2 = manipulação;; 1 = nada;; 0 = nenhuma.
- **EX017 — Interesses ausentes.** Os interesses de quem raramente aparecem nos modelos de perda? *Rubrica:* 3 = das pessoas afetadas, como os segurados;; 2 = segurados;; 1 = nada;; 0 = nenhuma.
- **EX018 — Medidas contra conflitos.** O que Daniel propôs para lidar com seus conflitos? *Rubrica:* 3 = revisão pela auditoria, declaração, decisores orçamentários separados;; 2 = três;; 1 = nada;; 0 = nenhuma.
- **EX019 — Posição sobre a notificação.** Por que Daniel se opôs a estreitar os incidentes notificáveis? *Rubrica:* 3 = prejudicaria os segurados e conflitaria com os deveres legais;; 2 = dano;; 1 = nada;; 0 = nenhuma.
- **EX020 — Mínimo do compliance.** Como cumprir a lei deve ser visto do ponto de vista ético? *Rubrica:* 3 = como um mínimo, não a medida completa;; 2 = mínimo;; 1 = nada;; 0 = nenhuma.

<a id="ch-05"></a>

## Capítulo 5 — Governança, riscos e compliance de segurança: alternativas de desenho

### Objetivos de aprendizagem

Você vai (1) desenhar abordagens alternativas de supervisão de fornecedores; (2) compará-las em eficácia, custo e carga; (3) selecionar uma abordagem para avaliação.

### 5.1 Três alternativas

A Halbrook supervisiona trezentos fornecedores com um único questionário longo para todos. Daniel desenha alternativas. A primeira mantém o questionário, mas acrescenta entrevistas de acompanhamento com os fornecedores-chave. A segunda introduz níveis: os fornecedores são classificados por acesso a dados, criticidade e conectividade, com revisões profundas para os níveis altos, apoiadas em relatórios SOC 2 tipo 2 ou certificados ISO/IEC 27001:2022 e em perguntas direcionadas, e revisões leves para os demais. A terceira contrata um serviço externo de ratings. Cada alternativa precisa ser julgada pelos mesmos critérios, definidos na seção seguinte.

### 5.2 Comparação

Daniel compara as alternativas em critérios combinados com compras e segurança: profundidade da garantia para os fornecedores críticos, tempo de revisão, carga sobre os fornecedores, custo e aderência às expectativas regulatórias sobre terceirização. A opção das entrevistas acrescenta profundidade, mas aumenta o tempo. O serviço de ratings é rápido, mas dá uma visão de fora para dentro que não enxerga os controles internos. Os níveis concentram o esforço onde ele importa e reaproveitam relatórios de garantia já existentes. Ele registra as notas e o raciocínio numa tabela que os colegas podem contestar. A Dra. Varga observa que a tabela também mostra às compras por que as entrevistas perderam apesar da profundidade.

### 5.3 Seleção

O comitê seleciona os níveis para uma avaliação controlada antes da implantação completa. Daniel observa que o serviço de ratings poderia complementar os níveis, sinalizando mudanças entre as revisões, e o registra como possível acréscimo futuro. Também define o que seria sucesso: revisões mais rápidas sem perder profundidade nos fornecedores críticos, definição fixada antes do teste para que os resultados não possam ser reinterpretados depois a favor dos níveis. Ele aprende que selecionar uma abordagem para avaliação, em vez de declará-la a resposta, mantém a organização aberta às evidências e reduz o custo de errar.

### Exemplo resolvido

Daniel desenha três alternativas de supervisão de fornecedores, compara-as em cinco critérios e seleciona os níveis para avaliação.

> **Caso sintético.** As alternativas e as notas são sintéticas; o SOC 2 e a ISO/IEC 27001:2022 são reais.

### Erros e limites

Os pesos dos critérios são subjetivos. A qualidade dos serviços de ratings varia.

### Exercícios

- **EX021 — Abordagem atual.** Como a Halbrook supervisiona hoje seus fornecedores? *Rubrica:* 3 = um único questionário longo para os trezentos;; 2 = questionário;; 1 = nada;; 0 = nenhuma.
- **EX022 — Evidências dos níveis.** Em que evidências se apoiam as revisões profundas? *Rubrica:* 3 = relatórios SOC 2 tipo 2 ou certificados ISO/IEC 27001:2022 mais perguntas direcionadas;; 2 = relatórios de garantia;; 1 = nada;; 0 = nenhuma.
- **EX023 — Limite dos ratings.** Qual é a limitação do serviço de ratings? *Rubrica:* 3 = a visão de fora para dentro não enxerga os controles internos;; 2 = de fora para dentro;; 1 = nada;; 0 = nenhuma.
- **EX024 — Definição de sucesso.** Como se define o sucesso dos níveis? *Rubrica:* 3 = revisões mais rápidas sem perder profundidade nos críticos;; 2 = critérios;; 1 = nada;; 0 = nenhuma.
- **EX025 — Avaliar primeiro.** Por que avaliar antes da implantação completa? *Rubrica:* 3 = mantém a organização aberta às evidências e reduz o custo do erro;; 2 = evidências;; 1 = nada;; 0 = nenhuma.

<a id="ch-06"></a>

## Capítulo 6 — Governança, riscos e compliance de segurança: avaliação controlada

### Objetivos de aprendizagem

Você vai (1) desenhar uma comparação controlada entre processos de governança; (2) testar uma diferença com um teste de permutação; (3) conferir a profundidade, além da rapidez.

### 6.1 Desenho

Daniel avalia os níveis em vinte revisões de fornecedores previstas. Com a concordância do comitê, dez são sorteadas para o questionário antigo e dez para o processo com níveis. O sorteio torna os grupos comparáveis em média, evitando o risco de os fornecedores mais fáceis caírem todos num grupo. O desfecho é o número de dias entre o pedido e a revisão concluída. Para conferir a profundidade, um revisor independente da auditoria interna pontua cada revisão concluída quanto a ter identificado os riscos-chave daquele fornecedor. Não dizer ao auditor que processo produziu cada revisão impede que as expectativas sobre os níveis contaminem as notas de profundidade.

### 6.2 Rapidez

O laboratório compara as médias de dias. O processo antigo teve média de trinta e nove vírgula três dias, e o processo com níveis, de vinte e seis vírgula cinco, uma diferença de doze vírgula oito dias. Um teste de permutação embaralha os vinte resultados cinco mil vezes para ver com que frequência o acaso sozinho produz uma diferença tão grande. O p-valor unilateral é de cerca de dois em dez mil, então o acaso é uma explicação improvável. Daniel relata a diferença com a ressalva de que dez revisões por grupo é uma amostra pequena: um único fornecedor muito lento poderia mover a média de um grupo em vários dias, e por isso a conferência de profundidade importa.

### Laboratório — Teste de permutação sobre a duração das revisões

```python
"""Permutation test: days to complete supplier reviews, old vs tiered process (synthetic)."""
import random
random.seed(5)
old = [34, 41, 29, 52, 38, 45, 31, 47, 40, 36]
new = [22, 30, 19, 35, 27, 24, 33, 21, 28, 26]
obs = sum(old)/10 - sum(new)/10
pool = old + new; hits = 0
for _ in range(5000):
    random.shuffle(pool)
    if sum(pool[:10])/10 - sum(pool[10:])/10 >= obs: hits += 1
print(f"mean old {sum(old)/10:.1f} days; tiered {sum(new)/10:.1f} days; difference {obs:.1f}")
print(f"one-sided permutation p = {hits/5000:.4f}")
```

Execute com `python3 lab_perm.py`. Saída verificada:

```text
mean old 39.3 days; tiered 26.5 days; difference 12.8
one-sided permutation p = 0.0002
```

### 6.3 Profundidade

A rapidez sozinha enganaria se as revisões ficassem mais rasas. O auditor interno, sem saber que processo foi usado, pontua a profundidade. Os dois grupos identificaram os riscos-chave na maioria das revisões, e o grupo com níveis se saiu um pouco melhor nos fornecedores de nível alto, porque os revisores leram as exceções dos relatórios SOC 2 em vez de passar os olhos pelos questionários. Daniel conclui que os níveis foram mais rápidos sem perda de profundidade nesta amostra. Recomenda a implantação com monitoramento contínuo das notas de profundidade no primeiro ano, para evitar que os revisores fiquem rasos quando a rapidez virar a meta visível.

### Exemplo resolvido

Daniel sorteia vinte revisões, constata que os níveis são 12,8 dias mais rápidos, com p de permutação de 0,0002, e confirma a profundidade com pontuação cega.

> **Caso sintético.** Os dados das revisões são sintéticos.

### Erros e limites

Amostras pequenas. O cegamento pode ser imperfeito se os revisores reconhecerem os formatos.

### Exercícios

- **EX026 — Sorteio.** Por que as revisões foram sorteadas? *Rubrica:* 3 = para tornar os grupos comparáveis em média;; 2 = comparabilidade;; 1 = nada;; 0 = nenhuma.
- **EX027 — Durações médias.** Quais foram as durações médias? *Rubrica:* 3 = antigo 39,3 dias, com níveis 26,5 dias;; 2 = diferença de 12,8;; 1 = nada;; 0 = nenhuma.
- **EX028 — p da permutação.** Que p-valor unilateral o teste de permutação deu? *Rubrica:* 3 = cerca de 0,0002;; 2 = 0,0002;; 1 = 0,05;; 0 = nenhuma.
- **EX029 — Pontuação cega.** Por que o auditor não soube que processo foi usado? *Rubrica:* 3 = para evitar viés nas notas de profundidade;; 2 = cegamento;; 1 = nada;; 0 = nenhuma.
- **EX030 — Resultado de profundidade.** Os níveis perderam profundidade? *Rubrica:* 3 = não, foram um pouco melhores nos de nível alto;; 2 = não;; 1 = sim;; 0 = nenhuma.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX030 (as de EX031–EX060 estão na edição em inglês até a tradução dos capítulos correspondentes). Daniel Mensah, a Dra. Elena Varga, a Wexford School of Management, a Halbrook Mutual e todos os números são sintéticos; os relatórios SOC 2 descritos são fictícios. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

**EX001.** Pelo sentido que a escolha fazia diante das informações, dos valores e do tempo disponíveis.

**EX002.** Porque não dar errado foi sorte; a decisão em si não teve estimativa de risco nem registro.

**EX003.** Deixa-as estreitas demais.

**EX004.** Hubbard e Seiersen (2016).

**EX005.** Registrar as premissas e pedir faixas em vez de números únicos.

**EX006.** As funções do NIST CSF 2.0.

**EX007.** Porque as notas da matriz são difíceis de comparar com os riscos financeiros.

**EX008.** Depende de questionários que levam semanas e raramente são lidos a fundo.

**EX009.** Porque adotar um método sem dados ou competências para sustentá-lo pode piorar a governança.

**EX010.** Porque cada framework responde a uma pergunta diferente.

**EX011.** Frequência de eventos de perda e magnitude da perda.

**EX012.** Cerca de 170 mil.

**EX013.** 68%.

**EX014.** Cerca de 4,1%, aproximadamente um ano em vinte e cinco.

**EX015.** Traduzi-las em termos familiares e mostrar a incerteza abertamente.

**EX016.** Escolhendo entradas otimistas ou pessimistas para justificar cortar ou aumentar os gastos.

**EX017.** As pessoas afetadas pelos riscos, como os segurados.

**EX018.** Revisão das estimativas pela auditoria interna, declaração do conflito e decisões orçamentárias tomadas por outras pessoas.

**EX019.** Porque os deveres de notificação vêm da lei e estreitá-los prejudicaria os segurados.

**EX020.** Como um mínimo, e não a medida completa da conduta ética.

**EX021.** Com um único questionário longo para os trezentos fornecedores.

**EX022.** Relatórios SOC 2 tipo 2 ou certificados ISO/IEC 27001:2022, mais perguntas direcionadas.

**EX023.** Dá uma visão de fora para dentro que não enxerga os controles internos.

**EX024.** Revisões mais rápidas sem perder profundidade nos fornecedores críticos.

**EX025.** Porque mantém as decisões abertas às evidências e reduz o custo de errar.

**EX026.** Para tornar os grupos comparáveis em média, de modo que os fornecedores mais fáceis não se concentrem num grupo.

**EX027.** 39,3 dias no processo antigo e 26,5 dias com níveis.

**EX028.** Cerca de 0,0002.

**EX029.** Para evitar viés na pontuação da profundidade de cada revisão.

**EX030.** Não; foi um pouco melhor nos fornecedores de nível alto nesta amostra.

<a id="references"></a>
## Referências

Todos os DOIs foram resolvidos em doi.org em 12 de outubro de 2026, e as normas foram conferidas nas páginas de seus editores. A lista é idêntica à da edição em inglês e cobre o livro inteiro, acrescida apenas da ABNT NBR ISO 31000:2018 e da ABNT NBR ISO/IEC 27001:2022, citadas nesta edição como referências brasileiras e conferidas em suas fontes oficiais; as adoções brasileiras da ABNT listadas foram conferidas no catálogo oficial da ABNT, e as demais normas técnicas são citadas em sua edição internacional. Organizações, pessoas, sistemas e números dos casos são sintéticos; somente as obras abaixo são reais.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- Associação Brasileira de Normas Técnicas. (2018). *ABNT NBR ISO 31000:2018 — Gestão de riscos — Diretrizes*. ABNT. <https://www.abntcatalogo.com.br/>
- Associação Brasileira de Normas Técnicas. (2022). *ABNT NBR ISO/IEC 27001:2022 — Segurança da informação, segurança cibernética e proteção à privacidade — Sistemas de gestão da segurança da informação — Requisitos* (versão corrigida 2023). ABNT. <https://www.abntcatalogo.com.br/>
- Cox, L. A., Jr. (2008). What's wrong with risk matrices? *Risk Analysis*, 28(2), 497–512. <https://doi.org/10.1111/j.1539-6924.2008.01030.x>
- Freund, J., & Jones, J. (2015). *Measuring and managing information risk: A FAIR approach*. Butterworth-Heinemann. <https://doi.org/10.1016/C2013-0-09966-5>
- Gordon, L. A., & Loeb, M. P. (2002). The economics of information security investment. *ACM Transactions on Information and System Security*, 5(4), 438–457. <https://doi.org/10.1145/581271.581274>
- Hubbard, D. W., & Seiersen, R. (2016). *How to measure anything in cybersecurity risk*. Wiley. <https://doi.org/10.1002/9781119162315>
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. <https://www.iso.org/standard/65694.html>
- International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- ISACA. (2018). *COBIT 2019 framework: Introduction and methodology*. ISACA. <https://www.isaca.org/resources/cobit>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Spears, J. L., & Barki, H. (2010). User participation in information systems security risk management. *MIS Quarterly*, 34(3), 503–522. <https://doi.org/10.2307/25750689>
