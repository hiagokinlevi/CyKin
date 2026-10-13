# Governança, Riscos e Compliance de Segurança: Curso de Pós-Graduação

- Idioma: português do Brasil (`pt`); curso 143, curso de pós-graduação (2 anos). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–12 de 12 têm texto didático escrito à mão; os exercícios EX001–EX060 têm resoluções correspondentes com rubricas de 0 a 3; os três laboratórios offline usam apenas a biblioteca padrão do Python 3 sobre dados sintéticos, e suas saídas foram incorporadas de execuções reais, idênticas às da edição em inglês. Revisão independente, revisão linguística e a verificação de 300 páginas A4 continuam em aberto.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

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
- **EX002 — Pulo com sorte.** Por que elogiar a revisão de fornecedor pulada foi um erro? *Rubrica:* 3 = premiou a sorte, não o raciocínio;; 2 = sorte;; 1 = vago;; 0 = nenhuma.
- **EX003 — Excesso de confiança.** O que o excesso de confiança faz com as faixas dos especialistas? *Rubrica:* 3 = deixa-as estreitas demais;; 2 = estreitas;; 1 = largas;; 0 = nenhuma.
- **EX004 — Fonte da calibração.** Que fonte descreve o treinamento de calibração para estimativas de segurança? *Rubrica:* 3 = Hubbard e Seiersen (2016);; 2 = Hubbard;; 1 = Cox;; 0 = nenhuma.
- **EX005 — Defesa contra o viés.** Cite uma defesa prática contra o viés. *Rubrica:* 3 = registrar as premissas e pedir faixas;; 2 = estrutura;; 1 = vago;; 0 = nenhuma.

### Síntese

Boas decisões de segurança são julgadas pelo raciocínio sob incerteza e protegidas contra vieses por métodos estruturados.

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
- **EX007 — Problema da matriz.** Por que o conselho tem dificuldade com a matriz cinco por cinco? *Rubrica:* 3 = é difícil compará-la com os riscos financeiros;; 2 = comparabilidade;; 1 = vago;; 0 = nenhuma.
- **EX008 — Fraqueza com fornecedores.** O que há de fraco na supervisão de fornecedores? *Rubrica:* 3 = questionários lentos, raramente lidos a fundo;; 2 = questionários;; 1 = vago;; 0 = nenhuma.
- **EX009 — Cautela com tendências.** Por que pesar as tendências contra a maturidade? *Rubrica:* 3 = métodos sem dados ou competências podem piorar a governança;; 2 = maturidade;; 1 = vago;; 0 = nenhuma.
- **EX010 — Combinar frameworks.** Por que as organizações maduras combinam frameworks? *Rubrica:* 3 = cada um responde a uma pergunta diferente;; 2 = complementares;; 1 = vago;; 0 = nenhuma.

### Síntese

A prática atual combina frameworks; as lacunas da Halbrook estão em expressar o risco, supervisionar fornecedores e informar o conselho.

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

- **EX011 — Decomposição do FAIR.** Em que dois fatores o FAIR decompõe o risco? *Rubrica:* 3 = frequência de eventos de perda e magnitude da perda;; 2 = dois;; 1 = vago;; 0 = nenhuma.
- **EX012 — Perda média.** Que perda anual média o laboratório relatou? *Rubrica:* 3 = cerca de 170 mil;; 2 = 170;; 1 = vago;; 0 = nenhuma.
- **EX013 — Anos tranquilos.** Em que proporção dos anos não houve perda? *Rubrica:* 3 = 68%;; 2 = 0,68;; 1 = vago;; 0 = nenhuma.
- **EX014 — Chance da cauda.** Qual é a chance de passar de um milhão num ano? *Rubrica:* 3 = cerca de 4%;; 2 = 0,041;; 1 = vago;; 0 = nenhuma.
- **EX015 — Persuasão.** O que torna as evidências especializadas convincentes para os comitês? *Rubrica:* 3 = tradução em termos familiares e incerteza visível;; 2 = tradução;; 1 = vago;; 0 = nenhuma.

### Síntese

Estimativas quantitativas de risco mostram tanto os anos tranquilos quanto as caudas graves quando explicadas em termos familiares.

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

- **EX016 — Números mal usados.** Como os números podem ser mal usados na quantificação de riscos? *Rubrica:* 3 = entradas otimistas ou pessimistas escolhidas para justificar uma conclusão;; 2 = manipulação;; 1 = vago;; 0 = nenhuma.
- **EX017 — Interesses ausentes.** Os interesses de quem raramente aparecem nos modelos de perda? *Rubrica:* 3 = das pessoas afetadas, como os segurados;; 2 = segurados;; 1 = vago;; 0 = nenhuma.
- **EX018 — Medidas contra conflitos.** O que Daniel propôs para lidar com seus conflitos? *Rubrica:* 3 = revisão pela auditoria, declaração, decisores orçamentários separados;; 2 = três;; 1 = vago;; 0 = nenhuma.
- **EX019 — Posição sobre a notificação.** Por que Daniel se opôs a estreitar os incidentes notificáveis? *Rubrica:* 3 = prejudicaria os segurados e conflitaria com os deveres legais;; 2 = dano;; 1 = vago;; 0 = nenhuma.
- **EX020 — Mínimo do compliance.** Como cumprir a lei deve ser visto do ponto de vista ético? *Rubrica:* 3 = como um mínimo, não a medida completa;; 2 = mínimo;; 1 = vago;; 0 = nenhuma.

### Síntese

A prática ética de GRC documenta as estimativas, gerencia conflitos e protege quem é afetado pelo risco.

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

- **EX021 — Abordagem atual.** Como a Halbrook supervisiona hoje seus fornecedores? *Rubrica:* 3 = um único questionário longo para os trezentos;; 2 = questionário;; 1 = vago;; 0 = nenhuma.
- **EX022 — Evidências dos níveis.** Em que evidências se apoiam as revisões profundas? *Rubrica:* 3 = relatórios SOC 2 tipo 2 ou certificados ISO/IEC 27001:2022 mais perguntas direcionadas;; 2 = relatórios de garantia;; 1 = vago;; 0 = nenhuma.
- **EX023 — Limite dos ratings.** Qual é a limitação do serviço de ratings? *Rubrica:* 3 = a visão de fora para dentro não enxerga os controles internos;; 2 = de fora para dentro;; 1 = vago;; 0 = nenhuma.
- **EX024 — Definição de sucesso.** Como se define o sucesso dos níveis? *Rubrica:* 3 = revisões mais rápidas sem perder profundidade nos críticos;; 2 = critérios;; 1 = vago;; 0 = nenhuma.
- **EX025 — Avaliar primeiro.** Por que avaliar antes da implantação completa? *Rubrica:* 3 = mantém a organização aberta às evidências e reduz o custo do erro;; 2 = evidências;; 1 = vago;; 0 = nenhuma.

### Síntese

Projetar alternativas e avaliar a escolhida protege contra erros caros.

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

- **EX026 — Sorteio.** Por que as revisões foram sorteadas? *Rubrica:* 3 = para tornar os grupos comparáveis em média;; 2 = comparabilidade;; 1 = vago;; 0 = nenhuma.
- **EX027 — Durações médias.** Quais foram as durações médias? *Rubrica:* 3 = antigo 39,3 dias, com níveis 26,5 dias;; 2 = diferença de 12,8;; 1 = vago;; 0 = nenhuma.
- **EX028 — p da permutação.** Que p-valor unilateral o teste de permutação deu? *Rubrica:* 3 = cerca de 0,0002;; 2 = 0,0002;; 1 = 0,05;; 0 = nenhuma.
- **EX029 — Pontuação cega.** Por que o auditor não soube que processo foi usado? *Rubrica:* 3 = para evitar viés nas notas de profundidade;; 2 = cegamento;; 1 = vago;; 0 = nenhuma.
- **EX030 — Resultado de profundidade.** Os níveis perderam profundidade? *Rubrica:* 3 = não, foram um pouco melhores nos de nível alto;; 2 = não;; 1 = sim;; 0 = nenhuma.

### Síntese

Uma avaliação controlada, com verificações de profundidade às cegas, mostra se processos mais rápidos continuam minuciosos.

<a id="ch-07"></a>

## Capítulo 7 — Governança, riscos e compliance de segurança: integração organizacional

### Objetivos de aprendizagem

Você vai (1) integrar os níveis de fornecedores às compras e à gestão de riscos; (2) alinhar as três linhas de responsabilidade; (3) gerir a mudança entre departamentos.

### 7.1 Integração com as compras

Daniel trabalha com as compras para embutir os níveis no processo de aquisição. Um formulário curto de entrada agora pergunta sobre acesso a dados, criticidade e conectividade antes de qualquer contrato. As respostas definem o nível automaticamente, e fornecedores de nível alto não podem ser aprovados sem uma revisão de segurança concluída. Ele aprende que a integração funciona quando as etapas de governança ficam dentro dos fluxos de trabalho existentes, no ponto em que as decisões são tomadas, e não num processo à parte que as pessoas precisam lembrar de iniciar. Como o nível é definido na entrada, um fornecedor de nível alto não chega mais à assinatura sem que a revisão de segurança tenha começado.

### 7.2 Linhas de responsabilidade

A Halbrook usa um modelo em que as unidades de negócio são donas do risco e o gerenciam, uma função de riscos e compliance supervisiona e questiona, e a auditoria interna fornece garantia independente. Daniel esclarece o papel de cada linha no risco de fornecedores: compras e donos de negócio gerenciam, sua equipe define os métodos e questiona, e a auditoria interna testa o processo anualmente. Ele aprende que a confusão entre as linhas, como a equipe de riscos fazer revisões que deveria questionar, enfraquece a garantia e borra a responsabilização. Antes da mudança, sua equipe fazia ela mesma algumas revisões de fornecedores, e ninguém independente sobrava para questioná-las.

### 7.3 Gerir a mudança

Algumas unidades de negócio resistem aos níveis porque as revisões de nível alto atrasam os contratos. Daniel se reúne com elas, explica os motivos e oferece um engajamento antecipado, para que as revisões comecem antes de os contratos virarem urgência. Também publica os tempos de revisão, para que as unidades possam se planejar. A resistência cai. Ele aprende que a mudança dá certo quando as pessoas entendem os motivos, recebem ajuda prática e têm suas preocupações legítimas, como os prazos, atendidas em vez de descartadas como obstrução. Publicar os tempos também dá às unidades uma medida pela qual cobrar a equipe dele, o que gera confiança no novo processo.

### Exemplo resolvido

Daniel embute os níveis nas compras, esclarece as três linhas de responsabilidade e reduz a resistência com engajamento antecipado e tempos publicados.

> **Caso sintético.** Os processos são sintéticos.

### Erros e limites

Os formulários de entrada podem ser manipulados. Os modelos de linhas variam entre organizações.

### Exercícios

- **EX031 — Barreira na entrada.** O que impede que fornecedores de nível alto sejam aprovados sem revisão? *Rubrica:* 3 = o formulário de entrada das compras define o nível e bloqueia a aprovação;; 2 = barreira;; 1 = vago;; 0 = nenhuma.
- **EX032 — Primeira linha.** Quem gerencia o risco de fornecedores na primeira linha? *Rubrica:* 3 = compras e donos de negócio;; 2 = donos;; 1 = auditoria;; 0 = nenhuma.
- **EX033 — Confusão entre linhas.** O que enfraquece a garantia entre as linhas? *Rubrica:* 3 = a equipe de riscos fazer revisões que deveria questionar;; 2 = confusão;; 1 = vago;; 0 = nenhuma.
- **EX034 — Causa da resistência.** Por que algumas unidades resistiram aos níveis? *Rubrica:* 3 = as revisões de nível alto atrasavam os contratos;; 2 = atraso;; 1 = vago;; 0 = nenhuma.
- **EX035 — Solução da resistência.** Como a resistência foi reduzida? *Rubrica:* 3 = engajamento antecipado e tempos de revisão publicados;; 2 = engajamento;; 1 = vago;; 0 = nenhuma.

### Síntese

A integração coloca as etapas de governança dentro dos fluxos de trabalho e respeita linhas claras de responsabilidade.

<a id="ch-08"></a>

## Capítulo 8 — Governança, riscos e compliance de segurança: casos difíceis

### Objetivos de aprendizagem

Você vai (1) lidar com conflitos entre compliance e risco; (2) decidir com evidências incompletas; (3) escalar de forma adequada.

### 8.1 Um fornecedor crítico falha

O relatório SOC 2 tipo 2 de um fornecedor de sinistros de nível alto mostra exceções: as revisões de acesso não foram feitas durante dois trimestres. O fornecedor é crítico, e substituí-lo levaria um ano. Daniel precisa recomendar o que fazer. Ele considera as opções: aceitar com controles compensatórios, exigir um plano de remediação com marcos, aumentar o monitoramento ou iniciar um plano de saída. Recomenda um plano de remediação, monitoramento extra do acesso do fornecedor aos dados da Halbrook e uma avaliação de saída em paralelo. A avaliação de saída em paralelo evita que a Halbrook fique presa se os marcos da remediação atrasarem.

### 8.2 Evidências incompletas

Um novo provedor de nuvem para análise de fraudes oferece apenas um certificado ISO/IEC 27001:2022 recente, cujo escopo não inclui claramente o serviço de análise. Daniel não consegue confirmar os controles diretamente. Recomenda um piloto limitado com dados sintéticos, direitos contratuais de auditoria e o pedido de uma declaração de escopo. Ele aprende que os casos difíceis raramente oferecem evidências completas, e que a boa prática é limitar a exposição enquanto as evidências são reunidas, em vez de escolher entre confiança cega e recusa. O piloto com dados sintéticos permite que os analistas de fraude testem o serviço sem expor dados de segurados a controles não confirmados.

### 8.3 Escalonamento

Um diretor de negócio quer seguir com o provedor de análise usando dados reais de segurados antes que a declaração de escopo chegue. Daniel escala para o diretor de riscos (CRO) com um memorando curto: a decisão necessária, as opções, o risco e sua recomendação. O CRO apoia o piloto apenas com dados sintéticos. Daniel aprende que o escalonamento é uma ferramenta normal de governança, e que um memorando claro faz dele um processo de decisão, e não uma disputa pessoal. O memorando também deixa um registro mostrando que tanto o pedido do diretor quanto o raciocínio de risco foram considerados.

### Exemplo resolvido

Daniel trata as exceções do SOC 2 num fornecedor crítico, limita a exposição a um provedor incerto e escala uma decisão sobre dados com um memorando claro.

> **Caso sintético.** Os fornecedores e as decisões são sintéticos; o SOC 2 e a ISO/IEC 27001:2022 são reais.

### Erros e limites

Os controles compensatórios podem mascarar o risco. O escalonamento pode desgastar relações.

### Exercícios

- **EX036 — Exceção no SOC 2.** Que exceção o relatório do fornecedor mostrou? *Rubrica:* 3 = revisões de acesso não feitas durante dois trimestres;; 2 = revisão de acesso;; 1 = vago;; 0 = nenhuma.
- **EX037 — Plano para o fornecedor crítico.** O que Daniel recomendou para o fornecedor crítico? *Rubrica:* 3 = plano de remediação, monitoramento extra e avaliação de saída em paralelo;; 2 = três;; 1 = substituir imediatamente;; 0 = nenhuma.
- **EX038 — Dúvida de escopo.** Por que o certificado do provedor era insuficiente? *Rubrica:* 3 = o escopo não incluía claramente o serviço de análise;; 2 = escopo;; 1 = vago;; 0 = nenhuma.
- **EX039 — Exposição limitada.** Como Daniel limitou a exposição enquanto reunia evidências? *Rubrica:* 3 = piloto com dados sintéticos e direitos de auditoria;; 2 = piloto;; 1 = vago;; 0 = nenhuma.
- **EX040 — Memorando de escalonamento.** O que continha o memorando de Daniel? *Rubrica:* 3 = decisão necessária, opções, risco e recomendação;; 2 = memorando;; 1 = vago;; 0 = nenhuma.

### Síntese

Casos difíceis exigem limitar a exposição, ler a garantia com cuidado e escalar com clareza.

<a id="ch-09"></a>

## Capítulo 9 — Governança, riscos e compliance de segurança: liderança e garantia

### Objetivos de aprendizagem

Você vai (1) expressar o apetite a risco em termos quantitativos; (2) comparar as estimativas de risco com o apetite; (3) conduzir conversas de garantia com o conselho.

### 9.1 Apetite quantificado

O conselho da Halbrook tem uma declaração de apetite qualitativa: baixa tolerância ao risco cibernético. Daniel ajuda a traduzi-la em limites de excedência: a probabilidade de as perdas cibernéticas anuais passarem de determinados valores não deve superar limiares acordados, por exemplo, no máximo cinco por cento de chance de passar de um milhão num ano. Ele aprende que o apetite quantificado torna concretas as discussões de risco e permite ao conselho comparar o risco cibernético com suas tolerâncias para outros riscos financeiros. O limite de cinco por cento em um milhão vira a referência contra a qual a curva combinada é testada na seção seguinte.

### 9.2 Comparar com o apetite

A equipe de Daniel estima uma curva de excedência de perda para todos os cenários cibernéticos combinados. O laboratório compara cinco pontos com o apetite. As estimativas ficam dentro do apetite em duzentos e cinquenta mil e em quinhentos mil, mas o excedem em um milhão, dois milhões e cinco milhões: por exemplo, oito por cento de chance de passar de um milhão contra um apetite de cinco por cento. É a cauda, e não o ano típico, que viola o apetite. Ele recomenda tratamentos voltados aos cenários graves. Tratamentos como o isolamento de backups encolhem a cauda sem mudar muito os anos comuns.

### Laboratório — Estimativas de excedência de perda contra o apetite do conselho

```python
"""Compare loss exceedance points with board appetite (synthetic, thousands)."""
lec = {250: 0.42, 500: 0.21, 1000: 0.08, 2000: 0.02, 5000: 0.004}
appetite = {250: 0.50, 500: 0.25, 1000: 0.05, 2000: 0.01, 5000: 0.002}
for x in lec:
    s = "within" if lec[x] <= appetite[x] else "EXCEEDS"
    print(f"P(loss > {x}k): estimate {lec[x]:.3f} appetite {appetite[x]:.3f} {s}")
```

Execute com `python3 lab_appetite.py`. Saída verificada:

```text
P(loss > 250k): estimate 0.420 appetite 0.500 within
P(loss > 500k): estimate 0.210 appetite 0.250 within
P(loss > 1000k): estimate 0.080 appetite 0.050 EXCEEDS
P(loss > 2000k): estimate 0.020 appetite 0.010 EXCEEDS
P(loss > 5000k): estimate 0.004 appetite 0.002 EXCEEDS
```

### 9.3 Garantia ao conselho

Daniel apresenta a comparação ao conselho com a incerteza por trás da curva e os tratamentos propostos: melhor isolamento dos backups e uma revisão do seguro. Um conselheiro pergunta se as estimativas são confiáveis. Ele explica como as entradas foram reunidas, que a auditoria interna revisou o método e que os resultados são faixas. O conselho aprova os tratamentos e pede uma atualização em seis meses. Ele aprende que a garantia ao conselho depende tanto da transparência sobre os métodos quanto dos números. A Dra. Varga observa que a atualização em seis meses dá ao conselho um meio de ver se os tratamentos realmente moveram a cauda.

### Exemplo resolvido

Daniel traduz o apetite em limites de excedência, constata que a cauda excede o apetite em três pontos e conduz uma discussão transparente com o conselho.

> **Caso sintético.** As curvas e o apetite são sintéticos.

### Erros e limites

As curvas combinadas dependem de premissas de correlação. Os limiares de apetite são julgamentos.

### Exercícios

- **EX041 — Exemplo de apetite.** Dê o exemplo de limite de excedência. *Rubrica:* 3 = no máximo 5% de chance de passar de 1 milhão;; 2 = 5% em 1 milhão;; 1 = vago;; 0 = nenhuma.
- **EX042 — Dentro do apetite.** Em que pontos a estimativa está dentro do apetite? *Rubrica:* 3 = 250 mil e 500 mil;; 2 = dois;; 1 = vago;; 0 = nenhuma.
- **EX043 — Violação em um milhão.** Qual é a estimativa em um milhão em relação ao apetite? *Rubrica:* 3 = 8% contra 5%;; 2 = excede;; 1 = vago;; 0 = nenhuma.
- **EX044 — Onde ocorre a violação.** Que parte da curva viola o apetite? *Rubrica:* 3 = a cauda;; 2 = cauda, hesitando com outra opção;; 1 = ano típico;; 0 = nenhuma.
- **EX045 — Resposta sobre confiança.** Como Daniel respondeu se as estimativas eram confiáveis? *Rubrica:* 3 = explicou as entradas, a revisão da auditoria e as faixas;; 2 = transparência;; 1 = vago;; 0 = nenhuma.

### Síntese

Um apetite quantificado permite aos conselhos ver onde riscos graves ultrapassam a tolerância e governar os tratamentos.

<a id="ch-10"></a>

## Capítulo 10 — Leitura e crítica de pesquisas

### Objetivos de aprendizagem

Você vai (1) ler pesquisas de GRC com olhar crítico; (2) avaliar métodos e afirmações; (3) relacionar os achados à prática.

### 10.1 Estratégia de leitura

Daniel lê quatro fontes: Gordon e Loeb (2002), sobre a economia do investimento em segurança; Cox (2008), sobre matrizes de risco; Spears e Barki (2010), sobre a participação dos usuários na gestão de riscos de segurança; e Hubbard e Seiersen (2016), sobre mensuração. Para cada uma, registra a pergunta, o método, os dados, a afirmação principal e os limites. Ele aprende que ler pesquisas para a prática significa perguntar não só se uma afirmação é verdadeira, mas se ela se aplica ao contexto da sua organização. Registrar os mesmos cinco campos para cada fonte facilita comparar os trabalhos analíticos, de survey e baseados na prática que vêm a seguir.

### 10.2 Avaliar os métodos

Gordon e Loeb oferecem um modelo analítico com premissas sobre as funções de vulnerabilidade e de perda; a ideia de que o investimento ótimo é limitado é robusta, mas os números exatos dependem das premissas. Cox analisa propriedades matemáticas das matrizes; suas conclusões são lógicas, e não empíricas. Spears e Barki usam dados de survey e entrevistas com gestores; os achados dependem do contexto. Hubbard e Seiersen sintetizam prática e pesquisa para defender a quantificação. Daniel observa os diferentes tipos de evidência de cada um. Um argumento lógico como o de Cox pode mostrar que as matrizes enganam em princípio, mas não diz com que frequência enganaram o comitê da Halbrook.

### 10.3 Relacionar à prática

Daniel relaciona cada fonte à Halbrook. Gordon e Loeb apoiam comparar os investimentos com a redução esperada de perdas. Cox apoia abandonar as matrizes nos relatórios ao conselho. Spears e Barki apoiam envolver os donos de negócio nas decisões de risco de fornecedores, o que os níveis fizeram. Hubbard e Seiersen apoiam o treinamento de calibração para quem estima. Ele escreve uma crítica observando que nenhuma estudou diretamente a supervisão de fornecedores de uma seguradora, de modo que sua própria avaliação acrescenta evidência local. A avaliação dos níveis em vinte revisões é a evidência local que as fontes publicadas não podiam oferecer.

### Exemplo resolvido

Daniel lê quatro fontes, registra método e limites, distingue evidência analítica de empírica e liga cada uma à prática da Halbrook.

> **Caso sintético.** A crítica é sintética; as quatro fontes são reais.

### Erros e limites

Os resumos simplificam as fontes. Os contextos diferem do da Halbrook.

### Exercícios

- **EX046 — Campos de leitura.** O que Daniel registra para cada fonte? *Rubrica:* 3 = pergunta, método, dados, afirmação principal, limites;; 2 = cinco;; 1 = vago;; 0 = nenhuma.
- **EX047 — Evidência de Cox.** Que tipo de evidência Cox (2008) oferece? *Rubrica:* 3 = análise lógica das propriedades das matrizes;; 2 = analítica;; 1 = empírica;; 0 = nenhuma.
- **EX048 — Método de Spears.** Que método Spears e Barki (2010) usam? *Rubrica:* 3 = dados de survey e entrevistas com gestores;; 2 = survey;; 1 = vago;; 0 = nenhuma.
- **EX049 — Gordon-Loeb na prática.** Como o trabalho de Gordon e Loeb se aplica na Halbrook? *Rubrica:* 3 = comparar investimentos com a redução esperada de perdas;; 2 = investimento;; 1 = vago;; 0 = nenhuma.
- **EX050 — Lacuna de pesquisa.** Que lacuna a avaliação de Daniel preenche? *Rubrica:* 3 = nenhuma estudou diretamente a supervisão de fornecedores de seguradoras;; 2 = evidência local;; 1 = vago;; 0 = nenhuma.

### Síntese

A leitura crítica separa os tipos de evidência e verifica se as descobertas se aplicam ao contexto.

<a id="ch-11"></a>

## Capítulo 11 — Projeto aplicado

### Objetivos de aprendizagem

Você vai (1) entregar uma melhoria aplicada de GRC; (2) medir os resultados contra os objetivos; (3) documentar para a passagem de bastão.

### 11.1 Escopo do projeto

O projeto aplicado de Daniel reúne seu trabalho: relatórios de risco quantificados para o conselho, níveis de fornecedores e apetite em termos de excedência. Ao longo de seis meses, ele implanta os níveis para os trezentos fornecedores, introduz relatórios de excedência de perda para os dez principais cenários cibernéticos e treina seis estimadores em calibração. Os objetivos incluem reduzir pela metade o tempo médio de revisão, concluir revisões profundas de todos os fornecedores de nível alto e apresentar os cenários em termos financeiros em todas as reuniões do conselho. Cada objetivo é mensurável, para que a seção de resultados possa relatá-lo como cumprido, parcialmente cumprido ou não cumprido.

### 11.2 Resultados

Depois de seis meses, o tempo médio de revisão caiu de cerca de trinta e nove para vinte e quatro dias, perto do objetivo. Os quarenta e dois fornecedores de nível alto concluíram revisões profundas, que revelaram três com exceções significativas, agora em remediação. O conselho recebe cenários quantificados todo trimestre e aprovou dois tratamentos. Os testes de calibração mostram que as faixas dos estimadores capturam as respostas verdadeiras com mais frequência após o treinamento. Daniel relata um objetivo, reduzir à metade o tempo de revisão, como quase, mas não totalmente, cumprido. Os três fornecedores com exceções significativas mostram que as revisões profundas acharam problemas que os questionários antigos tinham deixado passar.

### 11.3 Passagem de bastão

Daniel documenta os métodos, as ferramentas, as orientações aos estimadores e as regras dos níveis, e treina um colega para conduzir o processo. Registra as limitações conhecidas: as estimativas dependem de um pequeno grupo de especialistas, e os dados de perdas são escassos. Recomenda coletar dados internos de custo de incidentes para melhorar as estimativas futuras. Ele aprende que os projetos aplicados só geram valor duradouro quando outros podem continuá-los, e que relatar com honestidade os objetivos parcialmente cumpridos gera credibilidade. Registrar a dependência de um pequeno grupo de especialistas avisa seu sucessor de onde as estimativas são mais frágeis.

### Exemplo resolvido

Daniel implanta os níveis e os relatórios quantificados, quase reduz à metade o tempo de revisão, conclui quarenta e duas revisões profundas e passa o bastão com os limites documentados.

> **Caso sintético.** Os resultados são sintéticos.

### Erros e limites

Seis meses é pouco tempo. Os ganhos de calibração podem se dissipar.

### Exercícios

- **EX051 — Resultado do tempo de revisão.** Como mudou o tempo médio de revisão? *Rubrica:* 3 = de cerca de trinta e nove para vinte e quatro dias;; 2 = quase pela metade;; 1 = vago;; 0 = nenhuma.
- **EX052 — Revisões de nível alto.** Quantos fornecedores de nível alto concluíram revisões profundas? *Rubrica:* 3 = quarenta e dois;; 2 = 42;; 1 = vago;; 0 = nenhuma.
- **EX053 — Exceções encontradas.** Quantos fornecedores de nível alto tinham exceções significativas? *Rubrica:* 3 = três;; 2 = 3;; 1 = vago;; 0 = nenhuma.
- **EX054 — Parcialmente cumprido.** Que objetivo foi apenas quase cumprido? *Rubrica:* 3 = reduzir à metade o tempo de revisão;; 2 = tempo de revisão;; 1 = vago;; 0 = nenhuma.
- **EX055 — Recomendação de dados.** Que dados Daniel recomenda coletar? *Rubrica:* 3 = dados internos de custo de incidentes;; 2 = custos de incidentes;; 1 = vago;; 0 = nenhuma.

### Síntese

Projetos aplicados dão certo quando os resultados são medidos com honestidade e o trabalho é repassado.

<a id="ch-12"></a>

## Capítulo 12 — Revisão final e transferência

### Objetivos de aprendizagem

Você vai (1) revisar criticamente o que aprendeu na pós-graduação; (2) transferir métodos para novos contextos; (3) planejar o desenvolvimento contínuo.

### 12.1 Revisão final

Daniel apresenta seu trabalho à Dra. Varga e a um examinador externo de outra seguradora. Resume as decisões, as evidências e os resultados e responde às perguntas. O examinador pergunta se a quantificação vai sobreviver à saída dele. Daniel aponta a passagem de bastão, o colega treinado e a revisão do método pela auditoria interna. A Dra. Varga pergunta o que ele faria diferente; ele responde que coletaria dados de custo de incidentes desde o início e envolveria os corretores mais cedo. As duas respostas apontam para dados e partes interessadas que ele poderia ter envolvido antes, e não para falhas nos próprios métodos.

### 12.2 Transferência

Daniel considera como seus métodos se transferem. Os níveis se aplicam a qualquer organização com muitos fornecedores. Os relatórios de excedência de perda servem a organizações cujos conselhos estão acostumados ao risco financeiro, como bancos ou fundos de pensão, mas podem precisar de simplificação para pequenas organizações beneficentes. O treinamento de calibração se aplica onde quer que especialistas estimem quantidades incertas. Ele aprende que os métodos se transferem melhor quando suas premissas são explícitas, para que novos usuários verifiquem se elas valem no seu contexto. Numa pequena entidade beneficente, por exemplo, uma única regra de nível baseada no acesso a dados pode bastar, onde a Halbrook precisou de três critérios.

### 12.3 Desenvolvimento contínuo

Daniel planeja seu desenvolvimento contínuo: estudo mais profundo de estatística para riscos, acompanhamento das atualizações do NIST CSF e das normas ISO e participação numa comunidade profissional de quantificação de riscos. Também se compromete a ser mentor de um colega júnior. A Dra. Varga observa que a prática de GRC muda depressa e que seus hábitos de leitura crítica, avaliação controlada e relato transparente continuarão úteis à medida que os frameworks específicos mudarem. Ela também sugere que ele guarde seus registros de calibração, para poder verificar mais tarde se as próprias estimativas continuam bem calibradas.

### Exemplo resolvido

Daniel defende seu trabalho, explica como os métodos se transferem com premissas explícitas e planeja seu desenvolvimento contínuo.

> **Caso sintético.** A revisão é sintética.

### Erros e limites

A autoavaliação pode ser generosa. A transferência exige teste local.

### Exercícios

- **EX056 — Resposta sobre a continuidade.** Como Daniel mostrou que a quantificação sobreviveria à sua saída? *Rubrica:* 3 = passagem de bastão, colega treinado e revisão da auditoria;; 2 = continuidade;; 1 = vago;; 0 = nenhuma.
- **EX057 — Fazer diferente.** O que Daniel faria diferente? *Rubrica:* 3 = coletar dados de custo de incidentes desde o início e envolver os corretores mais cedo;; 2 = retrospectiva;; 1 = vago;; 0 = nenhuma.
- **EX058 — Condição de transferência.** Quando os métodos se transferem melhor? *Rubrica:* 3 = quando as premissas são explícitas;; 2 = premissas;; 1 = vago;; 0 = nenhuma.
- **EX059 — Pequenas beneficentes.** Que ajuste os relatórios de excedência de perda podem exigir em pequenas organizações beneficentes? *Rubrica:* 3 = simplificação;; 2 = mais simples;; 1 = vago;; 0 = nenhuma.
- **EX060 — Hábitos duradouros.** Que hábitos continuarão úteis quando os frameworks mudarem? *Rubrica:* 3 = leitura crítica, avaliação controlada, relato transparente;; 2 = hábitos;; 1 = vago;; 0 = nenhuma.

### Síntese

A revisão final consolida o aprendizado e prepara os métodos para a transferência a novos contextos.

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX060. Daniel Mensah, a Dra. Elena Varga, a Wexford School of Management, a Halbrook Mutual e todos os números são sintéticos; os relatórios SOC 2 descritos são fictícios. As respostas dos laboratórios citam saídas verificadas. Qualquer resposta que atenda à rubrica recebe a mesma pontuação.

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

**EX031.** O formulário de entrada define o nível, e a aprovação fica bloqueada até a revisão de segurança ser concluída.

**EX032.** Compras e donos de negócio.

**EX033.** Confusões como a equipe de riscos fazer revisões que deveria questionar de forma independente.

**EX034.** Porque as revisões de nível alto atrasavam seus contratos.

**EX035.** Com engajamento antecipado e a publicação dos tempos de revisão, para que as unidades pudessem se planejar.

**EX036.** As revisões de acesso não foram feitas durante dois trimestres.

**EX037.** Um plano de remediação com marcos, monitoramento extra e uma avaliação de saída em paralelo.

**EX038.** Seu escopo não incluía claramente o serviço de análise.

**EX039.** Um piloto limitado com dados sintéticos, direitos de auditoria e o pedido de uma declaração de escopo.

**EX040.** A decisão necessária, as opções, o risco e sua recomendação.

**EX041.** No máximo 5% de chance de as perdas cibernéticas anuais passarem de um milhão.

**EX042.** Em 250 mil e 500 mil.

**EX043.** Uma chance estimada de 8% contra um apetite de 5%.

**EX044.** A cauda, que cobre as perdas graves.

**EX045.** Explicando como as entradas foram reunidas, que a auditoria interna revisou o método e que os resultados são faixas.

**EX046.** A pergunta, o método, os dados, a afirmação principal e os limites.

**EX047.** Análise lógica e matemática das propriedades das matrizes de risco.

**EX048.** Dados de survey e entrevistas com gestores.

**EX049.** Apoia comparar os investimentos em segurança com a redução esperada de perdas.

**EX050.** Nenhuma das fontes estudou diretamente a supervisão de fornecedores de uma seguradora.

**EX051.** De cerca de trinta e nove para vinte e quatro dias.

**EX052.** Todos os quarenta e dois.

**EX053.** Três, agora em remediação.

**EX054.** Reduzir à metade o tempo médio de revisão.

**EX055.** Dados internos de custo de incidentes, para melhorar as estimativas futuras.

**EX056.** Apontando a passagem de bastão, o colega treinado e a revisão do método pela auditoria interna.

**EX057.** Coletar dados de custo de incidentes desde o início e envolver os corretores mais cedo.

**EX058.** Quando suas premissas são explícitas, para que novos usuários possam verificá-las.

**EX059.** Simplificação.

**EX060.** Leitura crítica, avaliação controlada e relato transparente.

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
