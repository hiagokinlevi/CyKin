# Infraestrutura Crítica e Segurança Setorial: Fundamentos, Evidências e Prática

- Idioma: português do Brasil (`pt`); bacharelado, quatro anos; aproximadamente 3.200 horas de estudo planejado (curso 115 de 207 da [trilha de estudo](../../../../../STUDY_PATH.md)). Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **rascunho**. Os capítulos 1–40 de 40 têm texto didático escrito; os exercícios EX001–EX080 (dois por capítulo) têm resoluções correspondentes; catorze laboratórios offline estão incorporados com a sua saída verificada. Revisão independente por especialistas, nova verificação das fontes, revisão de acessibilidade, revisão linguística e a verificação de 300 páginas A4 continuam em aberto. A meta do plano, de três exercícios por capítulo, ainda não foi atingida. Cobertura de capítulos em rascunho não é um livro concluído.
- Público: estudantes de segurança e de computação, de formação ampla, que querem trabalhar nos serviços sem os quais as sociedades não funcionam — saúde, energia, água, transporte, finanças e serviços públicos. Conhecimento de entrada: matemática do ensino médio, uso básico de computador e a capacidade de ler e escrever prosa clara em inglês. O livro constrói probabilidade, programação, redes, dados, identidade e criptografia a partir do Capítulo 1.
- Relação com os outros livros desta área: o [livro de engenharia](../../../../engineering-5-years/critical-sector-security/en/book/MANUSCRIPT.md) ensina a *projetar, construir e verificar* um sistema seguro contra requisitos; o [livro de mestrado](../../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md) ensina a projetar e defender um estudo empírico com revisão ética; o [livro de doutorado](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md) pede uma contribuição original ao conhecimento. **Este livro de bacharelado trata de amplitude e de julgamento**: entender como vários setores críticos funcionam e dependem uns dos outros, ler evidências de forma crítica, comparar métodos e controles com premissas explícitas e participar com segurança do trabalho de proteção e de incidentes de uma organização real. O seu trabalho de conclusão (Capítulos 35–40) é um projeto comparativo, guiado por evidências, e não a construção de um sistema nem uma dissertação.
- Autoria e responsabilidade editorial: [hiagokinlevi](https://github.com/hiagokinlevi). O texto didático original, de titularidade do mantenedor, é dedicado sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus próprios direitos e não são relicenciadas aqui.
- Limite educacional: este curso é um projeto educacional independente. Não é um diploma credenciado e não concede nenhuma autorização para acessar, varrer, testar ou alterar qualquer sistema real. Toda organização, local, dispositivo, endereço, pessoa e número de um exemplo resolvido é **sintético**, a menos que uma frase cite explicitamente uma fonte pública. Nada aqui é um procedimento operacional para um hospital, uma concessionária, um banco ou um operador reais, e nada é aconselhamento jurídico.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Padrão de livros](../../../../../BOOK_STANDARD.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os quarenta capítulos acompanham os oito semestres do plano. **Os Capítulos 1–18** são os fundamentos de que todo graduado em segurança precisa — raciocínio matemático, computação, programação, escrita, letramento em segurança, estruturas discretas, redes, dados, ética, sistemas operacionais, probabilidade, identidade, privacidade, medição, arquitetura, criptografia e método de pesquisa —, cada um ensinado por meio de um exemplo de serviço crítico desde a primeira página. **Os Capítulos 19–32** são o núcleo da área: o que torna uma infraestrutura "crítica", os casos públicos que moldaram o campo, modelos de sistema da tecnologia operacional, dependências entre setores, métodos de avaliação de risco, controles, verificação, análise de falhas, operações e resposta a incidentes, com dois laboratórios (25, 30). **Os Capítulos 33–40** são prática de pesquisa, um projeto comparativo, prática de campo e a sequência do trabalho de conclusão, que termina numa tese e numa apresentação.

Todo capítulo tem objetivos de aprendizagem, seções didáticas com definições, um exemplo resolvido, uma atividade prática, erros comuns e limites, dois exercícios e uma síntese. Catorze capítulos incorporam um laboratório offline escrito para a biblioteca padrão do Python 3; as saídas impressas foram produzidas executando o código com o Python 3.13. Escreva sua resposta antes de abrir as [resoluções](#worked-results).

Mantenha quatro títulos nas suas notas de estudo para todo caso que analisar: **serviço** (do que as pessoas dependem, e com que rapidez o dano segue a sua perda), **dependência** (do que o serviço precisa — energia, comunicações, pessoas, fornecedores, dados), **evidência** (o que você realmente sabe, de qual fonte, com quais limites) e **decisão** (o que você recomendaria, comparado com qual alternativa e sob quais premissas). A falha mais comum no nível de bacharelado não é um fato ausente; é uma recomendação confiante que nunca declara as suas premissas nem se compara com nada.

### O condado sintético usado neste livro

| Elemento sintético | Papel | Limite |
|---|---|---|
| **Calder County** e a sua **County Resilience Partnership (CRP)** | Uma região cujos operadores compartilham planos e exercícios | Inventada; nenhum lugar real |
| **Calder Valley Hospital (CVH)** — 420 leitos, pronto-socorro, imagem, laboratório, sistema de gestão predial (BMS), geradores de reserva | Operador de saúde | Inventado |
| **Calder Power Networks (CPN)** — distribuição de eletricidade, Substation North, RTUs de alimentadores, sala de controle, gateway de acesso remoto | Operador de energia | Inventado; nenhum produto real nomeado |
| **Calder Water (CW)** — estação de tratamento, bombas, 10 horas de reservação de água tratada, telemetria | Operador de água | Inventado |
| **Calder Transit (CT)** — veículo leve sobre trilhos, com sinalização e bilhetagem | Operador de transporte | Inventado |
| **Calder Mutual** — um banco regional com serviços de cartão e de pagamento | Operador financeiro | Inventado |
| **County Emergency Dispatch Centre (CEDC)** — atendimento de chamadas e despacho assistido por computador (CAD) | Serviço público | Inventado |
| Todos os endereços IP (10.x, e 198.51.100.x da faixa de documentação), chaves, probabilidades, custos (em libras, £) e saídas de laboratório | Dados didáticos | Sintéticos; a chave de demonstração do Laboratório 8 é pública e nunca deve ser usada |

### Política de fontes

As afirmações factuais sobre leis, normas, incidentes e estudos publicados remetem a fontes públicas onde citadas. Este rascunho **não** passou por uma verificação independente, fonte por fonte, então os leitores devem conferir de novo a versão, a data e o escopo exatos antes de se apoiar numa afirmação. Resultados clássicos (o teorema de Bayes, a definição de função de hash e os princípios de Saltzer–Schroeder) são acompanhados de referências clássicas. A discussão sobre Oldsmar remete tanto a um relato inicial quanto a uma revisão posterior, para que a alegação inicial não seja confundida com uma conclusão firmada. Normas com acesso pago (incluindo a IEC 62443) são citadas por meio de páginas públicas de visão geral ou de catálogo; o rascunho não cita cláusulas não verificadas.

## Sumário

1. [Raciocínio matemático](#ch-01)
2. [Sistemas computacionais](#ch-02)
3. [Programação I](#ch-03)
4. [Escrita acadêmica](#ch-04)
5. [Letramento em segurança](#ch-05)
6. [Estruturas discretas](#ch-06)
7. [Redes e protocolos](#ch-07)
8. [Programação II](#ch-08)
9. [Dados e bancos de dados](#ch-09)
10. [Ética e prática autorizada](#ch-10)
11. [Sistemas operacionais](#ch-11)
12. [Probabilidade e estatística](#ch-12)
13. [Identidade e acesso](#ch-13)
14. [Fundamentos de privacidade](#ch-14)
15. [Evidência e medição](#ch-15)
16. [Arquitetura de segurança](#ch-16)
17. [Conceitos de criptografia](#ch-17)
18. [Métodos de pesquisa I](#ch-18)
19. [Infraestrutura crítica e segurança setorial: escopo e teoria](#ch-19)
20. [Infraestrutura crítica e segurança setorial: casos fundadores](#ch-20)
21. [Infraestrutura crítica e segurança setorial: modelos de sistema](#ch-21)
22. [Infraestrutura crítica e segurança setorial: dados e dependências](#ch-22)
23. [Infraestrutura crítica e segurança setorial: métodos I](#ch-23)
24. [Infraestrutura crítica e segurança setorial: controles](#ch-24)
25. [Laboratório I](#ch-25)
26. [Infraestrutura crítica e segurança setorial: métodos II](#ch-26)
27. [Infraestrutura crítica e segurança setorial: verificação](#ch-27)
28. [Infraestrutura crítica e segurança setorial: análise de falhas](#ch-28)
29. [Infraestrutura crítica e segurança setorial: operações](#ch-29)
30. [Laboratório II](#ch-30)
31. [Infraestrutura crítica e segurança setorial: casos avançados](#ch-31)
32. [Infraestrutura crítica e segurança setorial: interfaces interdisciplinares](#ch-32)
33. [Métodos de pesquisa II](#ch-33)
34. [Projeto comparativo](#ch-34)
35. [Proposta do trabalho de conclusão](#ch-35)
36. [Prática de campo ou comunitária](#ch-36)
37. [Seminário de revisão de evidências](#ch-37)
38. [Implementação do trabalho de conclusão](#ch-38)
39. [Avaliação do trabalho de conclusão](#ch-39)
40. [Monografia e apresentação](#ch-40)

As [resoluções](#worked-results) contêm EX001–EX080. Um [glossário](#glossary) e as [referências](#references) encerram o livro.

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) transformar uma preocupação vaga ("e se a central de despacho perder o seu link de internet?") numa grandeza com unidades; (2) calcular uma perda anual esperada e explicar por que ela não é o mesmo que o pior evento crível; (3) estimar ordens de grandeza e conferir um cálculo por limitação; e (4) declarar as premissas por trás de um número, para que outra pessoa possa discordar delas com precisão. O capítulo apresenta o condado sintético de Calder, usado ao longo do livro, e prepara o Capítulo 6 (estruturas discretas) e o Capítulo 12 (probabilidade e estatística).

### 1.1 Por que a segurança precisa de números — e por que os números não bastam

A segurança dos setores críticos está cheia de comparações. O Calder Valley Hospital deve gastar dinheiro num segundo link de rede ou em testar os seus geradores? A Calder Power Networks deve aplicar o patch num controlador de alimentador agora, durante uma interrupção planejada no mês que vem, ou nunca? Essas são decisões sob incerteza, e a única forma honesta de compará-las é tornar a incerteza explícita. **Raciocínio matemático**, aqui, não significa matemática avançada. Significa quatro hábitos: dar uma unidade a cada grandeza; anotar de onde veio cada número; conferir um resultado estimando-o de outra forma; e dizer o que mudaria a resposta.

Uma **grandeza** é um número com uma unidade: 4 horas, £2.000 por hora, 0,3 evento por ano. A maioria dos erros na aritmética de risco são erros de unidade: multiplicar uma probabilidade por ano por um custo por hora, ou somar um percentual a uma contagem. Escrever as unidades ao lado de cada termo — e cancelá-las à medida que avança — apanha esses erros antes que outra pessoa os apanhe.

### 1.2 Valor esperado e os seus limites

Num modelo anual de um único evento, se um evento tem probabilidade $p$ e custa $C$ quando acontece, a sua **perda anual esperada** (EAL) é $p \times C$. As perdas esperadas de componentes de custo distintos se somam mesmo quando os eventos são dependentes: essa é a linearidade da esperança. O analista ainda precisa evitar contar a *mesma* consequência duas vezes quando os cenários se sobrepõem. A independência é necessária para alguns cálculos de probabilidade, como multiplicar as probabilidades de duas falhas, mas não para somar custos esperados. O valor esperado ajuda a comparar o custo anual de um controle com a perda que ele poderia evitar. Ele também pode esconder diferenças importantes: uma catástrofe de 1 em 100 e um incômodo quase certo podem ter o mesmo produto. Para um hospital, uma perda de energia de 72 horas não é "o mesmo" que setenta e duas perdas de uma hora: os pacientes que precisam de ventilação, diálise ou cirurgia são prejudicados pela duração, e não por uma média. Por isso, toda tabela de valor esperado deste livro vem acompanhada de um **pior evento crível** — o resultado mais grave que você acredita que poderia realisticamente ocorrer, declarado com a sua duração.

As probabilidades usadas nessas tabelas raramente são medidas. São estimativas tiradas de registros de incidentes, de relatórios do setor ou do julgamento de especialistas. Isso só é aceitável se você o disser. Um bom hábito é escrever a fonte entre colchetes — "(estimativa, gerente de operações da CEDC, 2026)" — e testar o cálculo com a metade e com o dobro da estimativa. Se a decisão não mudar, a estimativa é boa o bastante; se mudar, ela precisa de mais evidências. O Capítulo 15 volta a essa ideia como **análise de sensibilidade**.

### 1.3 Ordens de grandeza e limitação

Antes de calcular com precisão, estime. Um hospital com 420 leitos poderia perder algo da ordem de milhares de libras por hora de interrupção, em procedimentos cancelados e ambulâncias desviadas, e não dezenas nem milhões. Uma estimativa que cai três ordens de grandeza longe do cálculo cuidadoso é sinal de que uma unidade ou uma vírgula decimal escapou. A **limitação** é a habilidade relacionada: se você não consegue estimar uma grandeza, encontre números entre os quais ela precisa estar. Se um programa de testes de geradores custa no mínimo £8.000 (tempo da equipe) e no máximo £15.000 (tempo da equipe mais combustível e terceirizado), uma decisão que se sustenta nos dois extremos não precisa do valor exato.

### 1.4 Caso resolvido: duas propostas no condado de Calder (sintético)

**Este caso é sintético.** A **County Resilience Partnership (CRP)** do condado de Calder tem dinheiro para uma de duas propostas.

- **A — segundo link de internet para a County Emergency Dispatch Centre (CEDC)**, custo de £18.000 por ano. Sem ele, a CRP estima uma chance anual de 0,30 de uma queda do link de 4 horas e uma chance de 0,02 de uma queda de 48 horas (um cabo cortado na rota única), cada uma custando £2.000 por hora em pessoal de contingência e atrasos.
- **B — um programa de testes de geradores para o Calder Valley Hospital**, custo de £12.000 por ano. Sem ele, a estimativa é uma chance de 0,10 de uma falha de partida de 12 horas durante uma queda da rede elétrica e uma chance de 0,01 de uma falha de 72 horas, cada uma custando £5.000 por hora.

Para A, EAL = 0,30 × 4 h × £2.000/h + 0,02 × 48 h × £2.000/h = £2.400 + £1.920 = £4.320 por ano. Para B, EAL = 0,10 × 12 × 5.000 + 0,01 × 72 × 5.000 = £6.000 + £3.600 = £9.600. Nenhuma das opções "se paga" em termos esperados (razões de 0,24 e 0,80), o que é comum nos gastos com resiliência: compramos proteção contra as caudas, não contra as médias. Os piores eventos críveis (£96.000 e £360.000) tornam B o caso mais forte — e o dano de B é aos pacientes, algo que nenhum valor em libras expressa por inteiro. A recomendação é B, com a premissa declarada de que as estimativas de probabilidade estão corretas dentro de um fator de dois.

### 1.5 Atividade prática: Laboratório 1

O laboratório reproduz a comparação. Mude uma probabilidade de cada vez por um fator de dois e veja se a classificação muda.

```python
# Lab 1 - expected loss versus worst credible case for two options (synthetic Calder data, offline)
options = {
    "A: second ISP link for dispatch centre": {"cost": 18_000, "scenarios": [(0.30, 4, 2_000), (0.02, 48, 2_000)]},
    "B: backup generator test programme":     {"cost": 12_000, "scenarios": [(0.10, 12, 5_000), (0.01, 72, 5_000)]},
}
# each scenario: (annual probability it occurs without the option, outage hours, loss per hour in GBP)
for name, o in options.items():
    eal = sum(p * h * c for p, h, c in o["scenarios"])
    worst = max(h * c for p, h, c in o["scenarios"])
    print(f"{name}: expected annual loss avoided = {eal:,.0f}; worst single event = {worst:,.0f}; cost = {o['cost']:,}")
    print(f"   ratio avoided/cost = {eal / o['cost']:.2f}")
```

Saída esperada:

```text
A: second ISP link for dispatch centre: expected annual loss avoided = 4,320; worst single event = 96,000; cost = 18,000
   ratio avoided/cost = 0.24
B: backup generator test programme: expected annual loss avoided = 9,600; worst single event = 360,000; cost = 12,000
   ratio avoided/cost = 0.80
```

O laboratório supõe que cada opção remove completamente os seus cenários. Os controles reais reduzem a probabilidade ou a duração apenas em parte; o Exercício EX002 pede que você modele isso.

Duas execuções mostram para que serve o laboratório. Reduzir à metade a probabilidade de 0,10 de B, para 0,05, baixa a sua perda esperada para £6.600, ainda acima dos £4.320 de A, então a classificação se mantém. Dobrar a chance de 0,02 de A de uma queda de 48 horas, para 0,04, eleva A para £6.240, ainda abaixo de B. Como nenhuma mudança isolada inverte a ordem, a recomendação do programa de geradores é robusta a um fator de dois em qualquer estimativa isolada, que é exatamente a afirmação que o caso resolvido fez.

### 1.6 Erros comuns e limites

- Multiplicar grandezas com unidades incompatíveis (por ano por por hora, sem converter).
- Apresentar uma probabilidade estimada como se fosse medida.
- Classificar as opções apenas pela perda esperada quando o dano às pessoas depende da duração.
- Esquecer que os controles raramente removem um risco por inteiro.
- Somar as probabilidades de eventos que não são mutuamente exclusivos (o Capítulo 12 mostra a regra correta).

Cada erro tem um exemplo em Calder. O colega do EX001 multiplicou uma probabilidade por ano por horas e chamou o resultado de libras por hora. Escrever "chance de 0,02" sem fonte faz o palpite da CEDC parecer uma taxa medida. Classificar A e B apenas pela perda esperada esconderia que a cauda de £360.000 de B são 72 horas sem energia confiável no hospital. E a própria premissa do laboratório, de que cada opção remove inteiramente os seus cenários, é o quarto erro, embutido de propósito num modelo didático.

### Exercícios — capítulo 1

**EX001 — Disciplina de unidades.** *Objetivo:* encontrar e corrigir erros de unidade. *Entradas:* um colega escreve "EAL = 0,02 por ano × 48 horas × £2.000 = £1.920 por hora". *Etapas:* (1) cancele as unidades termo a termo; (2) declare a unidade correta do resultado; (3) explique numa frase por que o erro importa para a comparação com um custo anual de £18.000. *Evidência esperada:* expressão corrigida, com unidades. *Rubrica:* 3 = unidade correta (£ por ano) e um motivo claro; 2 = unidade correta, motivo fraco; 1 = percebe um erro, mas o descreve mal; 0 = nada.

**EX002 — Eficácia parcial.** *Objetivo:* modelar um controle que apenas reduz um risco. *Entradas:* Laboratório 1. *Etapas:* suponha que a opção B reduza à metade a probabilidade de cada cenário, em vez de removê-lo; modifique o laboratório para calcular a perda evitada; depois dobre as duas probabilidades de B e recalcule. *Evidência esperada:* dois números e uma recomendação de duas frases. *Rubrica:* 3 = valores corretos (£4.800 e £9.600) e uma recomendação que mencione os piores eventos críveis; 2 = números certos, argumento fraco; 1 = um número; 0 = nada.

### Síntese do capítulo

As decisões de segurança são comparações sob incerteza. Dê unidades às grandezas, separe a perda esperada do pior dano crível, confira os resultados por estimativa e limitação, e diga quais premissas mudariam a decisão. Um número sem fonte ou sensibilidade declarada é uma opinião disfarçada.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 40

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) descrever as camadas de um sistema computacional — hardware, firmware, sistema operacional, aplicações, dados e pessoas — e dizer onde as decisões de segurança são tomadas em cada uma; (2) distinguir a tecnologia da informação (TI) da tecnologia operacional (TO) e explicar por que as suas prioridades diferem; (3) descrever o ciclo de vida de um dispositivo num serviço crítico, da aquisição ao descarte; e (4) explicar por que o componente mais antigo de um sistema muitas vezes define a sua segurança. O capítulo se apoia no hábito de grandezas explícitas do Capítulo 1 e prepara o Capítulo 3, em que você vai escrever código para inspecionar um inventário de dispositivos.

### 2.1 Camadas e confiança

Um computador é uma pilha. Na base está o **hardware**: processador, memória, armazenamento e interfaces. Acima dele está o **firmware**, o código de baixo nível guardado no dispositivo que o inicializa e controla o hardware. O **sistema operacional** (Capítulo 11) reparte o hardware entre os programas e impõe quem pode fazer o quê. As **aplicações** fazem o trabalho que interessa às pessoas — a biblioteca de medicamentos de uma bomba de infusão, um sistema de despacho, um switch de pagamentos. Os **dados** são o que as aplicações criam e consomem. As **pessoas** configuram, usam e mantêm tudo isso. Cada camada confia nas camadas abaixo dela: uma aplicação não pode ser mais confiável do que o sistema operacional em que roda, e um sistema operacional não consegue detectar um firmware que mente para ele. É por isso que a inicialização segura, o firmware assinado e o suporte do fornecedor importam tanto nos serviços críticos (Capítulo 17).

### 2.2 TI e TO

A **tecnologia da informação** trata informações: e-mail, prontuários, pagamentos, agendamentos. A **tecnologia operacional** monitora e controla processos físicos: válvulas, disjuntores, bombas, sinais, ventiladores. O NIST descreve a TO como sistemas que "interagem com o ambiente físico (ou gerenciam dispositivos que interagem com o ambiente físico)" ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). A distinção importa porque as consequências diferem. Quando um sistema de TI falha, a informação fica indisponível ou errada; quando um sistema de TO falha, a água pode parar, um disjuntor pode não abrir ou um trem pode não receber um sinal. Espera-se tipicamente que os dispositivos de TO funcionem por 15 a 25 anos; eles podem não tolerar uma reinicialização durante a operação e muitas vezes são certificados numa configuração específica, de modo que aplicar patches exige a aprovação do fornecedor. A saúde acrescenta uma terceira categoria, os **dispositivos médicos**, que são produtos regulados cujo software o hospital não pode simplesmente alterar.

### 2.3 O ciclo de vida do dispositivo

A segurança é decidida muito antes de um ataque. Na **aquisição**, um comprador pode exigir software com suporte, um processo de divulgação de vulnerabilidades e uma lista de materiais de software (SBOM — uma lista dos componentes de software, ver [CISA SBOM](https://www.cisa.gov/sbom)). Na **instalação**, os padrões podem ser alterados e o dispositivo colocado na zona de rede certa. Durante a **operação**, ele precisa de monitoramento, de patches onde for possível e de controles compensatórios onde não for. No **fim do suporte**, o fornecedor deixa de emitir correções; o dispositivo continua funcionando, e é exatamente por isso que permanece em serviço. No **descarte**, os dados precisam ser removidos. Uma estação de trabalho de imagem hospitalar comprada em 2014, sobre um sistema operacional cujo suporte terminou em 2020, não é uma anomalia por descuido; é a consequência normal de um dispositivo médico de 15 anos sobre um sistema operacional de 10 anos.

### 2.4 Caso resolvido: imagem no Calder Valley Hospital (sintético)

**Este caso é sintético.** O departamento de imagem do CVH opera a estação de trabalho IMG-01, ligada a um aparelho certificado pelo fabricante com um sistema operacional específico, cujo suporte terminou em 2020. O fabricante só oferece uma atualização junto com um aparelho novo (£400.000). As opções são: (a) substituir agora; (b) mantê-la e isolá-la — permitir apenas as conexões de que ela precisa com o arquivo de imagens, remover o e-mail e a navegação na web, monitorar o seu tráfego; (c) não fazer nada. A opção (c) deixa uma máquina sabidamente sem patches numa rede clínica plana. A opção (a) remove o risco, mas custa um orçamento de capital que o hospital não tem neste ano. A opção (b) é a resposta habitual: um **controle compensatório** que reduz a exposição até a substituição, com um dono nomeado e uma data de substituição. O registro da decisão diz qual risco permanece — um arquivo malicioso chegando pela conexão com o arquivo de imagens — e como ele é monitorado.

### 2.5 Atividade prática

Escolha um dispositivo que você usa todos os dias (um celular, um roteador doméstico, um notebook). Sem abri-lo nem mudar nada, descubra nas páginas públicas do fornecedor: a versão do firmware ou do sistema operacional, se ele ainda tem suporte e como as atualizações são entregues. Escreva uma nota de ciclo de vida de cinco linhas: aquisição, instalação, operação, fim do suporte, descarte. Faça o mesmo para um dispositivo *imaginado* num serviço crítico — uma bomba de infusão do CVH — e liste o que você precisaria perguntar ao fornecedor.

Para a bomba, pergunte ao fornecedor sobre o processo de atualização da biblioteca de medicamentos, a data de fim do suporte do firmware e quem pode instalar as atualizações.

### 2.6 Erros comuns e limites

- Supor que "ainda funciona" significa "ainda é seguro": os dispositivos sem suporte acumulam vulnerabilidades não corrigidas.
- Tratar a TO como TI: reiniciar um controlador durante a operação, ou varrê-lo de forma agressiva, pode perturbar o processo físico.
- Ignorar o firmware: ele é código, tem vulnerabilidades e raramente é inventariado.
- Esquecer as pessoas como camada: a maioria dos sistemas é configurada por alguém sob pressão de tempo.

No CVH, os quatro erros se encontram na IMG-01: ela ainda funciona, então ficou na rede clínica; a certificação do aparelho a torna semelhante à TO nas suas restrições de patches; ninguém listou o seu firmware; e os técnicos de radiologia que a usam escolheram as configurações compartilhadas da área de trabalho. O limite deste capítulo é que ele nomeia as camadas sem medir quantos dispositivos ficam em cada uma.

### Exercícios — capítulo 2

**EX003 — Localizar a decisão.** *Objetivo:* ligar as camadas aos controles. *Entradas:* cinco controles: atualizações de firmware assinadas, contas de usuário do sistema operacional, os limites da biblioteca de medicamentos de uma aplicação, backups do banco de dados, treinamento da equipe. *Etapas:* atribua cada um a uma camada e declare uma falha que cada controle não trata. *Evidência esperada:* uma tabela de cinco linhas. *Rubrica:* 3 = camadas corretas e uma lacuna plausível para cada; 2 = um erro; 1 = só as camadas; 0 = nada.

**EX004 — TI ou TO?** *Objetivo:* raciocinar sobre as consequências. *Entradas:* o sistema de faturamento da CPN, a RTU de alimentador da CPN, o sistema de administração de pacientes do CVH, o BMS do CVH que controla a ventilação do centro cirúrgico. *Etapas:* classifique cada um como TI, TO ou dispositivo médico; nomeie a pior consequência plausível da sua falha; diga se provavelmente é necessária uma janela de patches aprovada pelo fornecedor. *Evidência esperada:* tabela e duas frases sobre o BMS. *Rubrica:* 3 = classes corretas, consequências ligadas a efeitos físicos na TO; 2 = pequeno deslize; 1 = só as classes; 0 = nada.

### Síntese do capítulo

Os sistemas computacionais são pilhas de confiança, do hardware às pessoas. A TO e os dispositivos médicos controlam resultados físicos, vivem por décadas e nem sempre podem receber patches, então a segurança depende dos termos de aquisição, do posicionamento e dos controles compensatórios. O componente mais antigo e com menos suporte muitas vezes define a exposição real.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 40

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) escrever programas curtos em Python usando variáveis, condições, laços, funções, listas e dicionários; (2) ler texto estruturado (CSV) com a biblioteca padrão; (3) transformar uma pergunta sobre um sistema ("quais dispositivos passaram do fim do suporte?") num filtro, numa contagem e num relatório; e (4) testar um programa contra um caso pequeno cuja resposta você já conhece. O capítulo se apoia no ciclo de vida de dispositivos do Capítulo 2 e prepara o Capítulo 8, em que os programas se tornam robustos contra entradas ruins.

### 3.1 Por que um estudante de segurança programa

O trabalho de segurança nos serviços críticos trata, sobretudo, de saber o que você tem e de perceber o que mudou. As duas coisas exigem processamento de dados: inventários com milhares de linhas, logs com milhões de linhas, alertas publicados todos os dias. Uma planilha funciona para cinquenta linhas; um programa curto funciona para cinquenta mil e pode ser executado de novo amanhã. O Python é usado aqui porque a sua biblioteca padrão lê CSV, JSON, datas e bancos de dados sem instalar nada, e porque um código legível é mais fácil de revisar — uma propriedade que importa quando o seu resultado informa uma decisão sobre a segurança de pacientes.

### 3.2 As construções básicas

Uma **variável** dá nome a um valor (`year = 2026`). Uma **condição** escolhe entre caminhos (`if eos < year:`). Um **laço** repete o trabalho para cada item (`for row in rows:`). Uma **função** empacota uma etapa com um nome e entradas, para que possa ser testada sozinha. Uma **lista** guarda itens em ordem; um **dicionário** associa chaves a valores (`row["os"]`). O módulo `csv` transforma cada linha de um arquivo CSV num dicionário indexado pelo cabeçalho. A classe `collections.Counter` conta quantas vezes cada valor aparece. Com isso, você consegue responder à maioria das perguntas sobre inventários.

Duas disciplinas importam desde o início. Primeiro, **teste contra uma resposta conhecida**: antes de rodar no arquivo real, rode em cinco linhas que você conferiu à mão. Segundo, **imprima o que você excluiu**, e não só o que encontrou: um filtro que descarta silenciosamente as linhas com data em branco vai reportar "nenhum dispositivo sem suporte" justamente para os dispositivos que ninguém documentou.

### 3.3 Caso resolvido e Laboratório 2: triagem do inventário do CVH (sintético)

**Este caso é sintético.** A equipe de engenharia clínica do CVH exporta uma amostra de oito linhas do seu inventário de dispositivos. A pergunta: quais dispositivos rodam software que passou do fim do suporte, onde eles estão, e há algum dispositivo não clínico na rede clínica?

```python
# Lab 2 - triage a synthetic hospital device inventory with the standard library (offline)
import csv, io
from collections import Counter
DATA = """asset,type,os,os_end_of_support,network,clinical
INF-01,infusion pump,RTOS-x 2.1,2030,clinical-vlan,yes
INF-02,infusion pump,RTOS-x 1.4,2021,clinical-vlan,yes
IMG-01,imaging workstation,Windows 7,2020,clinical-vlan,yes
IMG-02,imaging workstation,Windows 10,2025,clinical-vlan,yes
LAB-01,lab analyser,Linux 3.10,2019,lab-vlan,yes
ADM-01,office pc,Windows 11,2031,corporate,no
ADM-02,office pc,Windows 10,2025,clinical-vlan,no
BMS-01,building controller,vendor fw 4,2027,bms-vlan,no
"""
YEAR = 2026
rows = list(csv.DictReader(io.StringIO(DATA)))
unsupported = [r for r in rows if int(r["os_end_of_support"]) < YEAR]
print("assets:", len(rows), "| unsupported:", len(unsupported))
for r in unsupported:
    print(f"  {r['asset']:7} {r['type']:20} {r['os']:12} EoS {r['os_end_of_support']} clinical={r['clinical']}")
print("by network:", dict(Counter(r["network"] for r in unsupported)))
misplaced = [r["asset"] for r in rows if r["clinical"] == "no" and r["network"] == "clinical-vlan"]
print("non-clinical devices on clinical VLAN:", misplaced)
```

Saída esperada:

```text
assets: 8 | unsupported: 5
  INF-02  infusion pump        RTOS-x 1.4   EoS 2021 clinical=yes
  IMG-01  imaging workstation  Windows 7    EoS 2020 clinical=yes
  IMG-02  imaging workstation  Windows 10   EoS 2025 clinical=yes
  LAB-01  lab analyser         Linux 3.10   EoS 2019 clinical=yes
  ADM-02  office pc            Windows 10   EoS 2025 clinical=no
by network: {'clinical-vlan': 4, 'lab-vlan': 1}
non-clinical devices on clinical VLAN: ['ADM-02']
```

Interpretação: quatro dispositivos clínicos estão sem suporte, o que é um problema de planejamento de substituição com controles compensatórios (Capítulo 2). O ADM-02 é diferente: um PC de escritório sem suporte na rede clínica é a constatação mais barata de corrigir — atualizá-lo e movê-lo. As linhas são dados didáticos: os rótulos dos dispositivos são inventados e, embora alguns nomes de sistemas operacionais sejam conhecidos, trate cada ano de fim de suporte aqui como entrada de exemplo e confira qualquer produto real na página de ciclo de vida publicada pelo seu fornecedor.

### 3.4 Atividade prática

Estenda o Laboratório 2: (1) acrescente uma linha com `os_end_of_support` vazio e observe o erro; (2) mude o programa para que essas linhas sejam reportadas como "desconhecido — precisa de dono", em vez de travar ou serem puladas; (3) escreva um `assert` que confira que a contagem de dispositivos sem suporte nas oito linhas originais é 5.

A etapa (2) é a importante. Uma linha reportada como "desconhecido — precisa de dono" põe um nome numa lacuna; uma linha pulada a esconde, e uma trava interrompe o relatório para todos. O `assert` da etapa (3) é um teste com resposta conhecida: se uma mudança posterior no filtro o fizer imprimir 4 ou 6, o teste falha antes que alguém leia um relatório errado.

### 3.5 Erros comuns e limites

- Comparar números guardados como texto (`"2025" < "2026"` por acaso funciona; `"9" < "10"` não).
- Pular silenciosamente as linhas malformadas.
- Fixar o ano atual no código, de modo que o relatório envelheça; leia-o do relógio, mas mantenha-o fixo nos testes.
- Tratar uma exportação de inventário como a verdade: ela só é tão boa quanto a última pessoa que a atualizou (Capítulo 22).

No Laboratório 2, o segundo erro teria escondido o VEN-01 do EX005, o terceiro teria feito os dispositivos de 2025 parecerem com suporte de novo se o ano tivesse ficado em 2025, e o quarto se aplica à exportação inteira: o ADM-02 aparece na VLAN clínica apenas porque alguém registrou corretamente a sua rede.

### Exercícios — capítulo 3

**EX005 — Desconhecidos são constatações.** *Objetivo:* tornar visíveis os dados ausentes. *Entradas:* o Laboratório 2 mais uma nona linha `VEN-01,ventilator,,,clinical-vlan,yes`. *Etapas:* modifique o programa para imprimir uma seção de "desconhecidos"; explique por que uma data de suporte desconhecida num ventilador deve ser escalada. *Evidência esperada:* mudança no código, saída e duas frases. *Rubrica:* 3 = sem trava, VEN-01 reportado como desconhecido, motivo de escalonamento ligado à consequência clínica; 2 = funciona sem raciocínio; 1 = trava evitada pulando a linha; 0 = nada.

**EX006 — Uma função que você consegue testar.** *Objetivo:* separar a lógica dos dados. *Entradas:* Laboratório 2. *Etapas:* escreva `def is_unsupported(row, year) -> bool`, teste-a com três linhas feitas à mão (com suporte, sem suporte, ano-limite igual a `year`) e declare a sua regra para o limite. *Evidência esperada:* função, testes e a regra. *Rubrica:* 3 = função correta, os três testes, regra do limite declarada e justificada; 2 = limite não discutido; 1 = só a função; 0 = nada.

### Síntese do capítulo

Programas curtos e legíveis transformam inventários em decisões. Filtre, conte e reporte — e reporte sempre o que você não conseguiu classificar. Teste contra casos que você conhece, mantenha a lógica em funções e lembre-se de que o programa só é tão verdadeiro quanto os seus dados.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 40

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) estruturar um argumento técnico curto como afirmação, evidência, raciocínio e limites; (2) citar fontes de modo que o leitor encontre exatamente aquilo em que você se apoiou; (3) escrever para dois públicos ao mesmo tempo — um especialista que vai conferir o seu raciocínio e um tomador de decisão que tem cinco minutos; e (4) distinguir a sua própria análise do que uma fonte diz. O capítulo se apoia nas premissas explícitas do Capítulo 1 e prepara o Capítulo 18 (métodos de pesquisa) e o trabalho de conclusão (Capítulo 40).

### 4.1 Escrever faz parte do trabalho de segurança

Nos serviços críticos, boa parte do trabalho de segurança termina como documento: uma avaliação de risco, um relatório de incidente, uma recomendação ao conselho, uma submissão a um regulador. Uma análise correta mal escrita muitas vezes é ignorada; uma análise bem escrita com uma premissa escondida pode induzir ao erro uma organização inteira. A escrita acadêmica é um treino para os dois problemas. O seu núcleo é o **argumento**: uma afirmação sustentada por evidências por meio de um raciocínio declarado, com os seus limites reconhecidos. O modelo de Toulmin nomeia essas partes — afirmação, dados (evidência), garantia (o raciocínio que as liga), apoio, qualificador e refutação ([Toulmin, *The Uses of Argument*](https://doi.org/10.1017/CBO9780511840005)). Você não precisa do vocabulário em todo parágrafo, mas deve conseguir apontar cada parte.

### 4.2 Estrutura para dois leitores

Ponha a conclusão primeiro. Um tomador de decisão lê o primeiro parágrafo; um especialista lê tudo. Uma estrutura útil para um relatório curto é: **resumo** (a recomendação e o seu principal motivo, em três frases); **contexto** (qual serviço, qual pergunta, qual escopo); **evidência** (o que você examinou e encontrou, com as fontes); **análise** (como a evidência sustenta a recomendação e as alternativas que você comparou); **limites** (o que você não examinou, o que mudaria a sua conclusão); **referências**. Use títulos que digam algo ("Os dispositivos sem suporte se concentram na imagem") em vez de rótulos ("Constatações").

### 4.3 Citação e honestidade

Cite uma fonte sempre que afirmar um fato que você mesmo não estabeleceu, e cite o documento específico — o número e a revisão da publicação do NIST, o identificador do alerta da agência, o DOI do artigo — e não "segundo o NIST". Cite literalmente com parcimônia e com exatidão; parafraseie com as suas próprias palavras e cite mesmo assim. Separe o **relato** ("o alerta da CISA afirma que…") da **inferência** ("isso sugere que…") e da **recomendação** ("o CVH deveria…"). Nunca cite uma fonte que você não leu; se você se apoia num resumo de uma norma paga, cite o resumo. Ferramentas generativas podem redigir um texto fluente que contém citações inventadas: toda referência no seu trabalho deve ser uma que você abriu e conferiu.

### 4.4 Exemplo resolvido: reescrever um parágrafo fraco (sintético)

**Fraco (rascunho sintético de estudante):** "Os hospitais são muito vulneráveis a ataques cibernéticos, como todo mundo sabe pelo WannaCry. O CVH tem muitos computadores velhos, então está em alto risco e deveria comprar um firewall novo."

Problemas: uma afirmação universal sem sustentação ("todo mundo sabe"); um incidente real usado sem fonte nem lição precisa; "muitos" e "alto" sem números; uma recomendação que não decorre da evidência (computadores velhos não se resolvem com um firewall).

**Revisado:** "O National Audit Office do Reino Unido constatou que o ransomware WannaCry, em 2017, perturbou pelo menos um terço dos NHS trusts da Inglaterra, e que as organizações afetadas tinham sistemas Windows sem patches ou sem suporte ([NAO, 2017](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/)). O inventário de amostra do CVH mostra quatro de cinco dispositivos clínicos depois do fim do suporte (Capítulo 3, Laboratório 2). Recomendamos isolar esses dispositivos nas conexões de que precisam e definir datas de substituição, em vez de confiar num firewall de perímetro, porque o caso do NAO mostra o dano se espalhando dentro das redes hospitalares. Esta recomendação supõe que a amostra é representativa; é preciso um inventário completo para confirmá-la."

### 4.5 Atividade prática

Pegue uma notícia de uma página sobre qualquer incidente de infraestrutura. Escreva um briefing de 250 palavras para a diretoria de um hospital: um resumo de três frases, o que se sabe (com a notícia e qualquer fonte primária que ela cite), o que é incerto e uma pergunta que o CVH deveria fazer a si mesmo. Marque cada frase com R (relato), I (inferência) ou C (recomendação).

Um bom briefing mantém os três tipos de frase visivelmente separados. "A concessionária informou uma interrupção de seis horas (R)" é relato; "a interrupção provavelmente começou no sistema de faturamento (I)" é inferência e deve nomear a sua base; "o CVH deveria verificar se o seu próprio sistema de faturamento pode parar o trabalho clínico (C)" é recomendação. Quando a notícia cita uma fonte primária, abra-a e cite-a no lugar da notícia.

### 4.6 Erros comuns e limites

- Enterrar a conclusão na página quatro.
- Citar um resumo secundário como se fosse a fonte primária.
- Palavras que escondem quantidades: "muitos", "significativo", "crítico" sem número nem definição.
- Recomendações que não decorrem da evidência apresentada.
- Plágio, inclusive paráfrase próxima sem citação e texto gerado por IA sem reconhecimento.

O parágrafo fraco do exemplo resolvido mostra quatro desses erros ao mesmo tempo: "todo mundo sabe" esconde uma fonte, "muitos computadores velhos" esconde uma contagem, "alto risco" esconde uma definição e "comprar um firewall novo" não decorre de dispositivos sem suporte. O quinto erro é o que os avaliadores conferem mecanicamente: uma frase próxima da redação do relatório do NAO sem citação é plágio, mesmo que os fatos estejam certos.

### Exercícios — capítulo 4

**EX007 — Encontre a garantia.** *Objetivo:* expor um raciocínio escondido. *Entradas:* "O sistema de pagamentos da Calder Mutual não teve nenhuma interrupção no ano passado, então ele é seguro." *Etapas:* identifique a afirmação, a evidência e a garantia não declarada; explique por que a garantia falha; reescreva a afirmação para que ela seja sustentada pela evidência. *Evidência esperada:* três partes rotuladas e uma frase reescrita. *Rubrica:* 3 = garantia identificada ("ausência de interrupção implica ausência de fraqueza"), falha explicada, reescrita defensável; 2 = parcial; 1 = só afirmação/evidência; 0 = nada.

**EX008 — Resumo primeiro.** *Objetivo:* escrever para um tomador de decisão. *Entradas:* o exemplo resolvido do Capítulo 1. *Etapas:* escreva um resumo de 120 palavras recomendando a opção B, incluindo o motivo principal, a premissa principal e o que mudaria a recomendação. *Evidência esperada:* o resumo. *Rubrica:* 3 = recomendação na primeira frase, motivo, premissa e condição de reversão, ≤ 120 palavras; 2 = falta um elemento; 1 = recomendação enterrada; 0 = nada.

### Síntese do capítulo

Uma boa escrita de segurança declara uma afirmação, mostra a evidência, torna o raciocínio explícito e admite os limites — conclusão primeiro, fontes exatas, relato separado da inferência e da recomendação. Escreva como se um especialista fosse conferir cada frase e um tomador de decisão fosse ler só as três primeiras.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 40

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) definir confidencialidade, integridade e disponibilidade e explicar por que os serviços críticos muitas vezes as ordenam de forma diferente da TI de escritório; (2) usar corretamente o vocabulário ativo, ameaça, vulnerabilidade, probabilidade, impacto, risco e controle; (3) descrever, em nível conceitual, as principais classes de agente de ameaça e de técnica de ataque; e (4) ler um alerta de segurança e extrair o que ele significa para uma dada organização. O capítulo se apoia nos Capítulos 1–4 e prepara o Capítulo 16 (arquitetura) e o Capítulo 19 (o escopo da área).

### 5.1 O vocabulário

Um **ativo** é algo de valor: um serviço, um sistema, dados, um prédio, o tempo das pessoas. Uma **ameaça** é uma causa potencial de dano — um agente (um grupo criminoso, um insider, um Estado) ou um evento (uma enchente, uma atualização que falhou). Uma **vulnerabilidade** é uma fraqueza que uma ameaça pode explorar: uma falha sem patch, uma senha compartilhada, uma rota única de cabo. A **probabilidade** é o quão provável é que uma ameaça explore uma vulnerabilidade num período; o **impacto** é o dano se isso acontecer. O **risco** combina os dois — informalmente "probabilidade × impacto", embora o Capítulo 23 mostre por que a multiplicação muitas vezes engana. Um **controle** (ou salvaguarda) é uma medida que reduz a probabilidade ou o impacto. O guia de avaliação de risco do NIST apresenta esse vocabulário e esse processo ([SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)).

### 5.2 A tríade CIA nos serviços críticos

**Confidencialidade** significa que a informação é revelada apenas a quem tem autorização; **integridade** significa que a informação e os sistemas não são alterados sem autorização; **disponibilidade** significa que eles funcionam quando necessário. A TI de escritório muitas vezes põe a confidencialidade em primeiro lugar, porque vazamentos de dados pessoais têm custos legais e de reputação. Na TO, a ordem muitas vezes se inverte: uma empresa de água se importa primeiro com que as bombas funcionem (disponibilidade) e com que os comandos e as leituras sejam genuínos (integridade); o sigilo do nível de um reservatório importa muito menos. O guia de TO do NIST faz essa observação e acrescenta a **segurança física das pessoas (safety)** como preocupação predominante ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). A saúde mistura os dois: os prontuários exigem confidencialidade, enquanto as bombas de infusão e os ventiladores exigem integridade e disponibilidade. Um profissional de segurança num setor crítico precisa perguntar, para cada ativo, qual propriedade, ao falhar, prejudicaria as pessoas primeiro.

### 5.3 Agentes e técnicas

Os agentes de ameaça diferem em motivação e capacidade. Os **grupos criminosos** buscam dinheiro, de forma mais visível por meio de ransomware que cifra os dados e ameaça publicá-los. Os **grupos patrocinados por Estados** podem buscar inteligência ou a capacidade de interromper serviços numa crise. Os **hacktivistas** buscam atenção. Os **insiders** podem ser maliciosos ou, com muito mais frequência, cometer erros. Os **acidentes** — atualizações que falham, configurações erradas, cabos cortados — causam muitas interrupções sem adversário algum. As técnicas são catalogadas em bases de conhecimento públicas como o MITRE ATT&CK; a versão para sistemas de controle industrial lista táticas desde o acesso inicial até "impair process control" (prejudicar o controle do processo) ([MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)). No bacharelado, você deve conseguir ler um catálogo desses e dizer quais técnicas um controle trata; não se pede que você as execute.

### 5.4 Exemplo resolvido: ler um alerta para a CPN (sintético)

**Este caso é sintético.** Um alerta de fornecedor (inventado) afirma: "As versões do gateway de acesso remoto VPN-G anteriores à 9.3 permitem que um atacante não autenticado execute código. Foi observada exploração. Corrigido na 9.3." A Calder Power Networks roda o VPN-G 9.1 na sede, acessível pela internet e usado pelos engenheiros para chegar à rede de controle.

Extração: *ativo* — o gateway e tudo o que é alcançável por meio dele; *vulnerabilidade* — a falha na 9.1; *ameaça* — qualquer agente varrendo a internet, mais provável por causa da exploração observada; *impacto* — acesso potencial à rede de controle e, portanto, à operação dos alimentadores; *opções de controle* — atualizar para a 9.3 agora, ou desativar o gateway até a atualização e usar uma alternativa supervisionada. Catálogos públicos como a lista Known Exploited Vulnerabilities da CISA existem justamente para elevar a prioridade de falhas exploradas na prática ([CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)). A decisão não é difícil; o letramento está em reconhecer que "acesso remoto à TO" mais "explorado" mais "exposto à internet" supera uma falha com nota mais alta num dispositivo isolado.

### 5.5 Atividade prática

Escolha um alerta recente dos [alertas de ICS da CISA](https://www.cisa.gov/news-events/ics-advisories). Sem testar nada, extraia o ativo, a vulnerabilidade, as versões afetadas, a situação de exploração, a correção do fornecedor e as mitigações recomendadas. Depois escreva duas frases sobre como a prioridade mudaria para um operador cujo dispositivo está (a) exposto à internet e (b) numa rede isolada.

Escreva a resposta sobre a exposição como uma mudança de prioridade com um motivo, e não como uma nota nova. Exposto à internet mais explorado normalmente leva um alerta ao tratamento de emergência, como no VPN-G 9.1 da CPN; a mesma falha num dispositivo alcançável apenas a partir de uma célula isolada pode esperar a próxima janela planejada, se os controles compensatórios forem conferidos.

### 5.6 Erros comuns e limites

- Usar "ameaça", "vulnerabilidade" e "risco" como sinônimos.
- Supor que a confidencialidade vem sempre em primeiro lugar.
- Tratar todo incidente como ataque; muitas interrupções são acidentes, e a resposta é diferente.
- Aprender técnicas de ataque de forma operacional sem autorização (Capítulo 10).

O EX010 mostra o primeiro erro: chamar o corte do cabo de vulnerabilidade confunde a ameaça (as obras na via) com a fraqueza (uma rota única de cabo). O segundo faz um controlador de dosagem da CW parecer um problema de privacidade, quando é a integridade que protege os consumidores. O terceiro trata um cabo cortado ou uma atualização que falhou como um incidente em que se deve procurar um atacante, atrasando o reparo. O quarto é o motivo de todo laboratório aqui ser offline.

### Exercícios — capítulo 5

**EX009 — Ordene as propriedades.** *Objetivo:* aplicar a CIA por ativo. *Entradas:* prontuários do CVH; controlador de dosagem de cloro da CW; serviço de autorização de cartões da Calder Mutual; gravações de chamadas do CEDC. *Etapas:* ordene C, I e A para cada um e justifique a propriedade do topo numa frase. *Evidência esperada:* tabela. *Rubrica:* 3 = ordenações defensáveis com motivos baseados em dano (dosagem: integridade/safety primeiro); 2 = uma fraca; 1 = ordenações sem motivos; 0 = nada.

**EX010 — Vocabulário sob pressão.** *Objetivo:* usar os termos com precisão. *Entradas:* "O risco é que o cabo seja cortado por obras na via, o que é uma vulnerabilidade para o CEDC." *Etapas:* reescreva usando corretamente ativo, ameaça, vulnerabilidade e impacto. *Evidência esperada:* uma ou duas frases. *Rubrica:* 3 = obras como ameaça, rota única de cabo como vulnerabilidade, disponibilidade do despacho como impacto; 2 = um termo fora do lugar; 1 = dois fora do lugar; 0 = nada.

### Síntese do capítulo

O letramento em segurança é vocabulário preciso aplicado a consequências reais. Ativos, ameaças, vulnerabilidades, probabilidade, impacto e controles são ideias distintas. Nos serviços críticos, a disponibilidade, a integridade e a safety muitas vezes superam a confidencialidade, e a prioridade certa de um alerta depende da exposição e da exploração, e não apenas de uma nota.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 40

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) usar conjuntos e operações de conjuntos para raciocinar sobre inventários e permissões; (2) escrever condições lógicas e conferi-las com tabelas-verdade; (3) modelar as dependências entre serviços como um grafo dirigido e calcular o que é afetado quando um nó falha; e (4) reconhecer quando uma verificação exaustiva é viável e quando o número de estados a torna impossível. O capítulo se apoia na programação do Capítulo 3 e prepara o Capítulo 13 (acesso), o Capítulo 22 (dependências) e o Capítulo 28 (análise de falhas).

### 6.1 Conjuntos e relações

Um **conjunto** é uma coleção de itens distintos. Os dispositivos da rede clínica formam um conjunto $C$; os dispositivos depois do fim do suporte formam um conjunto $U$; a sua **interseção** $C \cap U$ é o conjunto a isolar primeiro. A **união** $A \cup B$ reúne os itens de qualquer um dos dois; a **diferença** $A \setminus B$ mantém os itens de $A$ que não estão em $B$. O controle de acesso é raciocínio sobre conjuntos: as permissões efetivas de um usuário são a união das permissões dos seus papéis, e uma regra de segregação de funções diz que certos pares nunca podem estar ambos nessa união (Capítulo 13). Uma **relação** liga itens de dois conjuntos — "o usuário *u* tem o papel *r*", "o serviço *s* depende do serviço *t*". Muitas perguntas de segurança são perguntas sobre relações: quem alcança o quê, o que depende do quê.

### 6.2 Lógica

Uma **proposição** é verdadeira ou falsa. Combine proposições com **e** ($\wedge$), **ou** ($\vee$) e **não** ($\neg$). Uma regra como "um pagamento acima de £10.000 só é liberado se for criado por uma pessoa e aprovado por outra pessoa, ou se for uma transferência de emergência aprovada por dois diretores" é uma expressão lógica; escrevê-la formalmente expõe lacunas ("e se quem criou também for diretor?"). Uma **tabela-verdade** lista todas as combinações de entradas; com $n$ entradas, ela tem $2^n$ linhas. Para 4 entradas, são 16 linhas — fácil. Para 40 entradas, são cerca de $10^{12}$ linhas — impossível de conferir à mão, e é por isso que sistemas complexos precisam de estrutura, testes e argumentação, em vez de enumeração exaustiva. As **leis de De Morgan** — $\neg(A \wedge B) \equiv \neg A \vee \neg B$ — permitem reescrever condições de "não permitido" como condições de "permitido" e conferir que as duas dizem a mesma coisa.

### 6.3 Grafos

Um **grafo** é um conjunto de nós e arestas. Num **grafo dirigido**, as arestas têm direção; escrevemos $u \to v$ para dizer "$v$ depende de $u$". A partir de um nó que falhou, uma **busca em largura** visita todos os nós alcançáveis ao longo das arestas: esse conjunto é tudo o que pode ser afetado. O número de nós alcançáveis a partir de um nó é o seu **alcance**; nós com alcance alto são candidatos a proteção extra ou a redundância. Os grafos também expõem **pontos únicos de falha**: um nó cuja remoção desliga os serviços daquilo de que eles precisam. O artigo clássico de Rinaldi, Peerenboom e Kelly descreve as infraestruturas como interdependentes exatamente nesse sentido — física, cibernética, geográfica e logicamente ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131)).

### 6.4 Exemplo resolvido e Laboratório 3: dependências do Calder County (sintético)

**Este caso é sintético.** A CRP desenhou um primeiro mapa de dependências: a subestação de energia alimenta as bombas de água, a alimentação da rede elétrica do hospital, a central de telecomunicações e a sinalização ferroviária; a central de telecomunicações transporta o despacho, os pagamentos com cartão, a telemetria da água e o arquivo de imagens em nuvem do hospital.

```python
# Lab 3 - cross-sector dependency closure on a directed graph (synthetic Calder County, offline)
from collections import deque
# edge u -> v means "v depends on u"
DEPENDS = {
    "grid-substation-N": ["water-pumps", "hospital-main", "telecom-exchange", "rail-signalling"],
    "telecom-exchange": ["dispatch-cad", "card-payments", "water-telemetry", "hospital-pacs-cloud"],
    "water-pumps": ["hospital-water"],
    "water-telemetry": ["water-pumps"],
    "dispatch-cad": ["ambulance-dispatch"],
    "hospital-main": [],
    "card-payments": ["fuel-retail"],
    "rail-signalling": [], "hospital-water": [], "hospital-pacs-cloud": [],
    "ambulance-dispatch": [], "fuel-retail": [],
}
def affected(start):
    seen, q = {start}, deque([start])
    while q:
        for v in DEPENDS.get(q.popleft(), []):
            if v not in seen:
                seen.add(v); q.append(v)
    return sorted(seen - {start})
for node in ("grid-substation-N", "telecom-exchange", "water-telemetry"):
    a = affected(node)
    print(f"{node}: {len(a)} affected -> {', '.join(a)}")
fan = sorted(((len(affected(n)), n) for n in DEPENDS), reverse=True)[:3]
print("highest reach:", fan)
```

Saída esperada:

```text
grid-substation-N: 11 affected -> ambulance-dispatch, card-payments, dispatch-cad, fuel-retail, hospital-main, hospital-pacs-cloud, hospital-water, rail-signalling, telecom-exchange, water-pumps, water-telemetry
telecom-exchange: 8 affected -> ambulance-dispatch, card-payments, dispatch-cad, fuel-retail, hospital-pacs-cloud, hospital-water, water-pumps, water-telemetry
water-telemetry: 2 affected -> hospital-water, water-pumps
highest reach: [(11, 'grid-substation-N'), (8, 'telecom-exchange'), (2, 'water-telemetry')]
```

Leia o resultado com cuidado. O grafo diz *pode ser afetado*, e não *vai falhar*: ele ignora energia de reserva, armazenamento e operação manual. Isso é deliberado — o primeiro mapa encontra onde olhar; o Capítulo 22 acrescenta o tempo e a autonomia da reserva. Ele também revela uma escolha de modelagem: aqui, as bombas de água dependem da telemetria só se não puderem funcionar localmente. Cada aresta é uma afirmação que alguém deveria conseguir justificar.

### 6.5 Atividade prática

Acrescente uma aresta que você acha que falta (por exemplo, a água do hospital depende da estação de tratamento, que depende da subestação) e um caminho alternativo (uma segunda central de telecomunicações). Recalcule o alcance. Escreva três frases sobre o que a mudança mostra e o que não mostra.

Acrescentar "estação de tratamento → água do hospital" e "subestação → estação de tratamento" eleva ainda mais o alcance da subestação, enquanto uma segunda central não retira nada da simples contagem de alcançabilidade: a busca continua marcando todo nó que um caminho consegue alcançar. Essa é a limitação que o EX012 pede que você explique, e é o motivo para escrever as dependências do tipo E e do tipo OU de formas diferentes.

### 6.6 Erros comuns e limites

- Confundir a direção das arestas ("depende de" versus "fornece"); escreva a convenção no topo de todo diagrama.
- Tratar a alcançabilidade como certeza de falha.
- Construir um grafo a partir da visão de uma única organização: outros operadores conhecem dependências que você não conhece.
- Tentar enumerar espaços de estados exponencialmente grandes.

No Laboratório 3, a linha de convenção `edge u -> v means "v depends on u"` é o que torna legível o alcance de 11 nós da subestação; invertida, a mesma lista afirmaria que a subestação depende da venda de combustível. Alcance de 11 significa exposição, e não falha, já que o hospital tem 72 horas de autonomia de gerador. O mapa é a primeira visão da CRP e não tem o que os engenheiros da CW e da CPN sabem. E o argumento da tabela-verdade escala no sentido contrário: 40 entradas binárias dão cerca de um trilhão de linhas.

### Exercícios — capítulo 6

**EX011 — Conjuntos para triagem.** *Objetivo:* usar operações de conjuntos. *Entradas:* C = {INF-01, INF-02, IMG-01, IMG-02, ADM-02}; U = {INF-02, IMG-01, IMG-02, LAB-01, ADM-02}; K (dispositivos com uma falha sabidamente explorada) = {IMG-01, ADM-02}. *Etapas:* calcule $C \cap U$, $(C \cap U) \cap K$ e $U \setminus C$; diga sobre qual conjunto você agiria primeiro e por quê. *Evidência esperada:* três conjuntos e um motivo. *Rubrica:* 3 = tudo correto e prioridade para $(C \cap U) \cap K$ = {IMG-01, ADM-02}; 2 = um erro; 1 = dois erros; 0 = nada.

**EX012 — Um caminho alternativo.** *Objetivo:* ver como a redundância muda o alcance. *Entradas:* Laboratório 3. *Etapas:* modele que o dispatch-cad também pode usar um enlace por satélite independente da central, de modo que perder só a central já não para o despacho. Explique por que uma busca simples de alcançabilidade não consegue expressar isso e proponha uma mudança de modelagem. *Evidência esperada:* explicação e proposta. *Rubrica:* 3 = reconhece a dependência OU (precisa de qualquer um de vários fornecedores) versus a dependência E, propõe nós que exigem todas/qualquer das entradas; 2 = só reconhece o problema; 1 = edita as arestas de forma incorreta; 0 = nada.

### Síntese do capítulo

Os conjuntos descrevem inventários e permissões; a lógica torna as regras exatas e verificáveis; os grafos tornam as dependências visíveis e calculáveis. Cada modelo responde a uma pergunta mais estreita do que parece: a alcançabilidade mostra exposição, e não falha, e a verificação exaustiva só funciona enquanto o espaço de estados é pequeno.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 40

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) explicar as camadas, o endereçamento, as portas e a diferença entre o cliente e o servidor de uma conexão; (2) descrever como protocolos industriais como o Modbus diferem dos protocolos modernos da internet nas suas premissas de segurança; (3) expressar uma política de segmentação de rede como zonas, conduítes e uma allowlist; e (4) conferir os fluxos observados contra essa política e interpretar as violações. O capítulo se apoia nos Capítulos 3 e 6 e prepara o Capítulo 16 (arquitetura) e o Capítulo 24 (controles).

### 7.1 Camadas, endereços e portas

As redes são construídas em camadas. A camada de **enlace** move quadros entre dispositivos vizinhos (Ethernet, Wi-Fi). A camada de **internet** move pacotes entre redes usando endereços IP. A camada de **transporte** fornece um fluxo de bytes confiável (TCP; ver [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)) ou datagramas individuais (UDP) e usa **números de porta** para identificar o serviço num host. A camada de **aplicação** carrega o significado: HTTPS para a web, Modbus/TCP na porta 502 para a consulta industrial, OPC UA normalmente na porta 4840. Numa conexão TCP, o **cliente** abre a conexão para a porta de escuta do servidor; a resposta usa a mesma conexão. Quem inicia é relevante para a segurança: um controlador de campo que de repente *abre* conexões para a sala de controle está se comportando de modo diferente de um que só responde.

### 7.2 Protocolos industriais e as suas premissas

Muitos protocolos industriais foram projetados para enlaces seriais fechados entre as décadas de 1970 e 1990. O Modbus, por exemplo, define códigos de função para ler e escrever registradores e bobinas, e a sua forma clássica não tem autenticação: qualquer dispositivo que consiga enviar uma requisição bem formada a um controlador pode pedir que ele escreva ([especificação do Modbus](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf)). Isso não é um bug de uma implementação; é a premissa de projeto de que só dispositivos confiáveis alcançam o fio. Quando esses protocolos passam a rodar sobre redes IP, essa premissa precisa ser imposta pela rede: segmentação, allowlists e monitoramento. Os protocolos modernos acrescentam segurança (o TLS 1.3 fornece canais autenticados e cifrados — [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)), mas atualizar milhares de dispositivos de campo leva décadas.

### 7.3 Zonas, conduítes e allowlists

Uma **zona** é um grupo de ativos com requisitos de segurança semelhantes; um **conduíte** é o caminho de comunicação controlado entre zonas. A série ISA/IEC 62443 usa esses termos para sistemas industriais ([visão geral da ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). Uma concessionária típica tem uma zona corporativa, uma zona desmilitarizada (DMZ) onde os dados são trocados, uma zona de controle (servidores SCADA, IHMs de operadores) e uma zona de campo (controladores, RTUs). Uma política de **allowlist** nomeia os fluxos permitidos — zona de origem, zona de destino, porta, finalidade — e nega todo o resto. A política é só metade do controle; a outra metade é conferir se o tráfego observado corresponde a ela.

### 7.4 Exemplo resolvido e Laboratório 4: conferir os fluxos da CW (sintético)

**Este caso é sintético.** A Calder Water permite três conduítes: os usuários corporativos veem o historiador na DMZ por HTTPS; um coletor na DMZ lê da zona de controle por OPC UA; o servidor SCADA consulta os controladores de campo por Modbus/TCP. Um resumo de fluxos de uma hora é conferido contra a política.

```python
# Lab 4 - check observed flows against a zone-and-conduit allowlist (synthetic, offline)
ALLOW = {  # (source zone, destination zone, destination port): purpose
    ("corporate", "dmz", 443): "historian web view",
    ("dmz", "control", 4840): "OPC UA read from historian replica collector",
    ("control", "field", 502): "Modbus/TCP polling of field controllers",
}
ZONE = {"10.1.": "corporate", "10.5.": "dmz", "10.20.": "control", "10.30.": "field"}
def zone(ip):
    return next((z for p, z in ZONE.items() if ip.startswith(p)), "unknown")
FLOWS = [  # src, dst, dport  (synthetic NetFlow-style summary)
    ("10.1.4.22", "10.5.0.10", 443), ("10.5.0.11", "10.20.0.5", 4840),
    ("10.20.0.5", "10.30.1.7", 502), ("10.1.4.80", "10.20.0.5", 3389),
    ("10.20.0.9", "198.51.100.23", 443), ("10.30.1.7", "10.20.0.5", 502),
]
for s, d, p in FLOWS:
    key = (zone(s), zone(d), p)
    verdict = ALLOW.get(key)
    print(f"{s:>13} -> {d:<14} :{p:<5} {key[0]:>9}->{key[1]:<8} {'ALLOW ' + verdict if verdict else 'VIOLATION'}")
```

Saída esperada:

```text
    10.1.4.22 -> 10.5.0.10      :443   corporate->dmz      ALLOW historian web view
    10.5.0.11 -> 10.20.0.5      :4840        dmz->control  ALLOW OPC UA read from historian replica collector
    10.20.0.5 -> 10.30.1.7      :502     control->field    ALLOW Modbus/TCP polling of field controllers
    10.1.4.80 -> 10.20.0.5      :3389  corporate->control  VIOLATION
    10.20.0.9 -> 198.51.100.23  :443     control->unknown  VIOLATION
    10.30.1.7 -> 10.20.0.5      :502       field->control  VIOLATION
```

Três violações, três significados diferentes. Uma conexão de área de trabalho remota (porta 3389) do corporativo direto para a zona de controle contorna a DMZ — talvez um atalho de um engenheiro, talvez um intruso. Um host da zona de controle alcançando um endereço da internet (198.51.100.23 é um endereço de documentação no lugar de um real) pode ser a verificação de atualizações de um fornecedor ou dados saindo. Um dispositivo de campo *iniciando* Modbus para o servidor SCADA inverte a direção normal. Nenhuma delas prova um ataque; cada uma precisa de um dono que a explique, e a explicação se torna evidência (Capítulo 15).

### 7.5 Atividade prática

Num computador que é seu, liste as suas próprias conexões ativas (por exemplo, com `netstat` ou `ss`) e classifique cinco como cliente ou servidor, local ou remota, e esperada ou inesperada. Não varra nenhum outro sistema.

Use a coluna de estado do `ss` ou do `netstat`: um endereço local com uma porta em escuta é um servidor; uma conexão para uma porta remota 443 é um cliente. Marque tudo o que você não conseguir explicar e encontre o programa por trás com as ferramentas do seu sistema operacional, na sua própria máquina.

### 7.6 Erros comuns e limites

- Escrever allowlists só por porta, ignorando as zonas de origem e de destino.
- Supor que "interno" significa "confiável".
- Confundir o tráfego de resposta com conexões iniciadas ao ler logs de fluxo.
- Tratar uma violação como prova de comprometimento, e não como uma pergunta.

O Laboratório 4 mostra por quê: uma regra só por porta que permitisse a 502 teria deixado passar o dispositivo de campo que iniciou Modbus para o servidor SCADA, uma inversão da direção normal. A conexão RDP corporativa para o controle é "interna" e mesmo assim é uma violação. Nos logs de fluxo, as respostas do servidor SCADA na 502 não são conexões novas e não devem ser lidas como tal. E cada uma das três violações vai primeiro para um dono como pergunta.

### Exercícios — capítulo 7

**EX013 — Explique as violações.** *Objetivo:* raciocinar dos fluxos às hipóteses. *Entradas:* a saída do Laboratório 4. *Etapas:* para cada violação, dê uma explicação benigna e uma maliciosa e a evidência que as distinguiria. *Evidência esperada:* uma tabela de três linhas. *Rubrica:* 3 = pares plausíveis e evidência distintiva específica (tíquetes de mudança, logins de usuários, propriedade do destino, configuração do dispositivo); 2 = evidência genérica; 1 = só as explicações; 0 = nada.

**EX014 — Fluxo mínimo.** *Objetivo:* apertar uma política. *Entradas:* a tabela ALLOW. *Etapas:* proponha dois refinamentos que tornem a política mais estreita sem quebrar as suas finalidades (por exemplo, regras por host em vez de por zona, códigos de função só de leitura) e diga como cada um seria imposto e conferido. *Evidência esperada:* dois refinamentos com imposição e conferência. *Rubrica:* 3 = ambos mais estreitos, aplicáveis e verificáveis; 2 = um; 1 = vago; 0 = nada.

### Síntese do capítulo

As redes carregam as premissas dos seus protocolos. Os protocolos industriais clássicos confiam em quem consegue alcançá-los, então os serviços críticos impõem a confiança com zonas, conduítes e allowlists — e depois conferem os fluxos observados contra a política. Uma violação é uma pergunta a um dono, e não um veredicto.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 40

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) validar entradas não confiáveis com regras explícitas e rejeitar o que não está conforme; (2) tratar erros de modo que um programa falhe de forma segura e visível; (3) escrever testes de unidade, inclusive para casos de limite e malformados; e (4) explicar por que a análise sintática (parsing) é uma fronteira de segurança. O capítulo se apoia nos Capítulos 3 e 7 e prepara o Capítulo 9 (dados) e o Capítulo 27 (verificação).

### 8.1 A entrada é uma fronteira de segurança

Todo programa que lê dados de fora — um arquivo, uma mensagem de rede, a digitação de um operador — faz premissas sobre eles. Quando as premissas estão erradas, os programas travam, calculam errado ou, pior, fazem algo que um atacante escolheu. Os catálogos de fraquezas de software são dominados por erros de tratamento de entrada: injeção, leituras e escritas fora dos limites, validação de entrada inadequada ([CWE Top 25](https://cwe.mitre.org/top25/)). O padrão defensivo é **analisar, não adivinhar**: defina exatamente como é uma entrada válida, converta o texto bruto em valores tipados num só lugar e rejeite todo o resto com um erro claro.

### 8.2 Regras de validação

Para um setpoint enviado a uma estação de bombeamento, uma entrada válida poderia ser: um número; finito (não "NaN" nem infinito); dentro dos limites de engenharia (0,5–4,5 m); mudando não mais que 0,5 m em relação ao valor atual; de uma origem autorizada. Cada regra deve ser explícita, testada e registrada em log quando rejeita. A **allowlist** (aceitar só as formas sabidamente boas) é mais forte que a **denylist** (rejeitar as formas sabidamente ruins), porque os atacantes encontram formas em que você não pensou. O `float("nan")` do Python funciona, e `nan < 0.5` e `nan > 4.5` são ambos falsos — então uma verificação de faixa escrita como "rejeitar se estiver abaixo ou acima" *aceita* NaN silenciosamente. A verificação robusta é "aceitar só se `math.isfinite(x)` e `0.5 <= x <= 4.5`".

### 8.3 Erros e falha segura

Quando a validação falha, o programa precisa fazer algo definido: rejeitar o comando e manter o último valor bom, disparar um alarme, registrar o motivo. Ele não pode continuar com um valor padrão que por acaso seja perigoso (um setpoint de zero) nem engolir o erro em silêncio (`except: pass`). Em contextos de controle, "seguro" é uma decisão do processo — uma válvula pode precisar falhar fechada para o cloro, mas aberta para a água de resfriamento —, então o programador implementa um estado de falha que o dono do processo especificou, em vez de inventar um.

### 8.4 Testes

Um **teste de unidade** confere uma função contra casos conhecidos. Bons conjuntos de testes incluem valores **típicos**, **limites** (exatamente 0,5 e 4,5), valores **logo fora** dos limites (0,49, 4,51), entradas **malformadas** (string vazia, "abc", "1e309", "nan") e casos **dependentes de estado** (um valor válido que muda rápido demais). O módulo embutido `unittest` do Python ou simples instruções `assert` bastam neste nível. Um teste que nunca falhou nunca mostrou que funciona: rode cada teste novo uma vez contra uma versão deliberadamente quebrada.

Para o validador de setpoint da CW, a versão contra a qual falhar é a v1: o seu teste de "nan" retorna True e o seu teste de "abc" levanta uma exceção, então dois dos sete testes falham antes da correção e nenhum depois dela.

### 8.5 Exemplo resolvido: o validador de setpoint da CW (sintético)

**Este caso é sintético.** A interface de operador da Calder Water envia setpoints de nível de reservatório como texto. Versão 1 do validador:

```python
def accept_v1(text, current):
    x = float(text)
    if x < 0.5 or x > 4.5: return False
    if abs(x - current) > 0.5: return False
    return True
```

`accept_v1("nan", 3.0)` retorna True: as duas comparações com NaN são falsas, e `abs(nan - 3.0) > 0.5` também é falso. `accept_v1("abc", 3.0)` levanta uma exceção que, dependendo de quem chama, pode derrubar a interface. Versão 2:

```python
import math
def accept_v2(text, current):
    try:
        x = float(text)
    except ValueError:
        return False
    return math.isfinite(x) and 0.5 <= x <= 4.5 and abs(x - current) <= 0.5
```

A versão 2 declara o que é aceitável, e não o que não é. Testes: `("3.2", 3.0)` → True; `("4.5", 4.2)` → True; `("4.51", 4.2)` → False; `("nan", 3.0)` → False; `("inf", 3.0)` → False; `("abc", 3.0)` → False; `("2.0", 3.0)` → False (passo grande demais).

O bloco `try` transforma uma trava numa rejeição, e `math.isfinite` remove NaN e infinito antes de qualquer comparação. O que a v2 ainda não faz é dizer por que rejeitou: a interface de operador deveria registrar qual regra falhou.

### 8.6 Atividade prática

Implemente as duas versões e os sete testes acima. Rode os testes contra a v1 e registre quais falham; depois, contra a v2. Acrescente dois testes seus que você acha que a v2 ainda pode errar (dica: espaços em branco, strings muito longas, vírgula como separador decimal) e decida se o comportamento é aceitável.

Contra a v1, espere que o teste de "nan" falhe (ele retorna True) e que "abc" levante uma exceção em vez de retornar False. Contra a v2, os sete devem passar. Nos seus próprios testes, " 3.2 " com espaços é aceito pelo `float` do Python, o que provavelmente está bem; "3,2" é rejeitado, o que pode surpreender um operador que usa a vírgula decimal. Decida se essa rejeição deveria produzir uma mensagem clara, em vez de uma recusa silenciosa.

### 8.7 Erros comuns e limites

- Verificações de faixa que deixam passar NaN.
- Capturar toda exceção e continuar.
- Validação só na interface do usuário, e não onde o comando é executado.
- Testes que só cobrem valores típicos.
- Acreditar que a validação torna um canal autêntico: um comando forjado com aparência válida passa mesmo assim (o Capítulo 17 acrescenta a autenticação).

Na CW, o terceiro erro é o perigoso: se só a interface de operador confere os setpoints, qualquer outro cliente que alcance o PLC por Modbus contorna inteiramente a validação, como mostra o conduíte da zona de campo do Laboratório 4. O quinto erro se liga ao Laboratório 8: um setpoint bem formado de 2,0 m passa pela v2 quer tenha sido enviado por um operador, quer por um intruso.

### Exercícios — capítulo 8

**EX015 — Quebre a v1.** *Objetivo:* encontrar entradas que derrotam uma verificação por denylist. *Entradas:* `accept_v1`. *Etapas:* encontre três entradas distintas para as quais a v1 dá um resultado inseguro ou indefinido e explique cada uma. *Evidência esperada:* entradas e explicações. *Rubrica:* 3 = NaN aceito; texto não numérico (ou uma string vazia) levanta uma exceção não tratada; e um terceiro caso distinto, como um valor *atual* NaN, que faz a verificação de passo passar para qualquer setpoint dentro da faixa; 2 = dois; 1 = um; 0 = nada.

**EX016 — Especifique o estado de falha.** *Objetivo:* ligar o código à segurança do processo. *Entradas:* um setpoint rejeitado numa bomba de dosagem de cloro e numa válvula de entrada de água bruta. *Etapas:* para cada um, declare o que o programa deve fazer na rejeição, quem deve decidir isso e o que precisa ser registrado. *Evidência esperada:* duas especificações curtas. *Rubrica:* 3 = manter o último valor bom mais alarme, o dono do processo decide, campos de log nomeados (hora, origem, entrada bruta, regra que falhou); 2 = parcial; 1 = genérico; 0 = nada.

### Síntese do capítulo

A análise sintática é uma fronteira de segurança. Defina com precisão a entrada válida, aceite só ela, falhe para um estado que o dono do processo escolheu, registre toda rejeição e teste limites e casos malformados. A validação pega entradas malformadas; ela não prova que uma entrada bem formada veio de alguém autorizado.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 40

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Dados e bancos de dados

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) projetar um pequeno esquema relacional com chaves; (2) escrever consultas SQL que filtram, juntam e ordenam; (3) explicar por que os tipos de dados importam, usando números de versão como exemplo; e (4) prevenir a injeção de SQL com consultas parametrizadas. O capítulo se apoia nos Capítulos 3 e 8 e prepara o Capítulo 14 (privacidade), o Capítulo 15 (medição) e o Capítulo 22 (dependências).

### 9.1 Por que dados relacionais

As perguntas de segurança combinam fatos guardados em lugares diferentes: quais ativos existem, que software eles rodam, quais alertas afetam esse software, quem é o dono de cada ativo, quais estão expostos à internet. Um **banco de dados relacional** guarda cada tipo de fato uma única vez, numa **tabela** de linhas e colunas, e liga as tabelas por meio de **chaves** ([Codd, 1970](https://doi.org/10.1145/362384.362685)). Uma **chave primária** identifica uma linha de forma única (o ID de um ativo); uma **chave estrangeira** se refere a uma linha de outra tabela (o nome do produto de um ativo, que casa com o produto de um alerta). Uma **junção (join)** combina as linhas que casam. Guardar cada fato uma única vez evita a falha conhecida das planilhas: duas cópias que discordam.

### 9.2 SQL em quatro cláusulas

`SELECT` nomeia as colunas que você quer; `FROM ... JOIN ... ON` nomeia as tabelas e como elas casam; `WHERE` filtra as linhas; `ORDER BY` ordena. `GROUP BY` com `COUNT` resume. A biblioteca padrão do Python inclui o `sqlite3`, um banco de dados embutido completo, para você praticar sem servidor. Dois cuidados. Primeiro, uma junção descarta em silêncio as linhas sem correspondência: um ativo cujo nome de produto está escrito errado simplesmente desaparece de um relatório de vulnerabilidades. Use um `LEFT JOIN` e procure nulos quando a completude importar. Segundo, os **tipos** decidem as comparações. Strings de versão comparadas como texto põem "3.10" antes de "3.4", porque o caractere "1" vem antes de "4" na ordenação.

### 9.3 Injeção

Se um programa monta SQL colando a entrada do usuário numa string — `"... WHERE id = '" + user_input + "'"` —, uma entrada como `x' OR '1'='1` muda o significado da consulta. Isso é a **injeção de SQL**, persistentemente entre as fraquezas de software mais perigosas ([CWE Top 25](https://cwe.mitre.org/top25/)). A correção é estrutural: **consultas parametrizadas** (`db.execute("... WHERE id = ?", (user_input,))`) enviam os dados separados do código, de modo que a entrada nunca pode se tornar SQL.

No Laboratório 5, toda consulta com uma entrada, como buscar um ativo pelo ID, deve usar um marcador `?`.

### 9.4 Exemplo resolvido e Laboratório 5: casar alertas da CPN (sintético)

**Este caso é sintético.** A Calder Power Networks mantém uma tabela de ativos e importa alertas de fornecedores. A pergunta: quais ativos rodam uma versão mais antiga que a versão corrigida, ordenados de modo que os itens sabidamente explorados e expostos à internet venham primeiro? Uma pequena função personalizada compara as versões numericamente.

```python
# Lab 5 - asset and vulnerability joins in SQLite (synthetic Calder Power data, offline)
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE asset(id TEXT PRIMARY KEY, site TEXT, role TEXT, product TEXT, version TEXT, internet_exposed INTEGER);
CREATE TABLE advisory(product TEXT, fixed_in TEXT, severity TEXT, known_exploited INTEGER);
INSERT INTO asset VALUES
 ('RTU-11','Substation North','feeder RTU','RTU-K','3.2',0),
 ('RTU-12','Substation North','feeder RTU','RTU-K','3.4',0),
 ('HMI-01','Control room','operator HMI','HMI-S','7.0',0),
 ('VPN-01','Head office','remote access gateway','VPN-G','9.1',1),
 ('HIS-01','DMZ','historian replica','HIST-P','5.5',0);
INSERT INTO advisory VALUES
 ('RTU-K','3.4','high',0), ('VPN-G','9.3','critical',1), ('HIST-P','5.1','medium',0);
""")
def vkey(v): return tuple(int(x) for x in v.split("."))
db.create_function("vlt", 2, lambda a, b: int(vkey(a) < vkey(b)))
q = """SELECT a.id, a.role, a.version, v.fixed_in, v.severity, v.known_exploited, a.internet_exposed
       FROM asset a JOIN advisory v ON a.product = v.product
       WHERE vlt(a.version, v.fixed_in)
       ORDER BY v.known_exploited DESC, a.internet_exposed DESC, v.severity"""
for row in db.execute(q):
    print(row)
print("string comparison '3.10' < '3.4':", "3.10" < "3.4", "| numeric:", vkey("3.10") < vkey("3.4"))
```

Saída esperada:

```text
('VPN-01', 'remote access gateway', '9.1', '9.3', 'critical', 1, 1)
('RTU-11', 'feeder RTU', '3.2', '3.4', 'high', 0, 0)
string comparison '3.10' < '3.4': True | numeric: False
```

Dois ativos precisam de ação, o gateway primeiro (é o alerta do Capítulo 5). O HMI-01 não tem alerta e não aparece; o HIS-01 já passou da correção. Note que `ORDER BY v.severity` ordena as *palavras* alfabeticamente ("critical" < "high" < "medium"), o que por acaso está certo aqui e estaria errado com "low". Uma coluna de posição de severidade é o projeto robusto.

### 9.5 Atividade prática

(1) Mude a junção para um `LEFT JOIN` e liste os ativos sem registro de alerta — "nenhum alerta" é o mesmo que "nenhuma vulnerabilidade"? (2) Escreva uma consulta parametrizada que retorne um ativo pelo ID; depois mostre, com uma consulta montada por string deliberadamente insegura, apenas no seu banco de dados em memória, como `' OR '1'='1` retorna todas as linhas.

O `LEFT JOIN` mostra o HMI-01 com nulos nas colunas do alerta. "Nenhum alerta" significa nenhum alerta neste feed para o produto HMI-S, e não que a IHM não tem falha; ela pode ter um boletim do fornecedor fora do feed ou nenhum publicado ainda. Na parte (2), a consulta insegura só pode rodar contra o seu banco de dados em memória, nunca contra um real.

### 9.6 Erros comuns e limites

- Comparar versões, datas ou números guardados como texto.
- Junções internas que descartam em silêncio as linhas sem correspondência.
- Montar SQL por concatenação de strings.
- Confiar que os nomes de produtos casam exatamente entre os feeds dos fornecedores e os inventários locais.

O Laboratório 5 mostra onde três desses erros morderiam. A comparação de versões trataria "3.10" como mais antiga que "3.4" se fosse feita como texto, marcando erradamente como vulnerável uma RTU atualizada. A junção interna descarta o HMI-01 em silêncio. E os nomes de produto "RTU-K" e "VPN-G" só casam porque a amostra foi digitada de forma consistente; os feeds reais dos fornecedores escrevem os produtos de formas diferentes e precisam de uma tabela de mapeamento.

### Exercícios — capítulo 9

**EX017 — Conte por local.** *Objetivo:* resumir com SQL. *Entradas:* Laboratório 5. *Etapas:* escreva uma consulta que retorne, por local, o número de ativos que precisam de atualização. *Evidência esperada:* consulta e resultado. *Rubrica:* 3 = `GROUP BY` correto com o filtro de versão, resultado Head office 1, Substation North 1; 2 = conta todos os ativos; 1 = só a sintaxe; 0 = nada.

**EX018 — Ordem de severidade.** *Objetivo:* corrigir uma ordenação frágil. *Entradas:* Laboratório 5 com uma severidade extra de alerta "low". *Etapas:* explique por que `ORDER BY severity` poria "low" no lugar errado e dê duas correções. *Evidência esperada:* explicação e correções. *Rubrica:* 3 = a ordem alfabética põe "low" antes de "medium"; correções: uma coluna de posição numérica ou uma tabela de consulta/expressão `CASE`; 2 = uma correção; 1 = só a explicação; 0 = nada.

### Síntese do capítulo

Os dados relacionais permitem responder a perguntas de segurança transversais com uma única consulta, se as chaves, os tipos e as junções estiverem certos. Compare as versões numericamente, procure o que as junções descartam, ordene as severidades com números e nunca monte SQL a partir de strings não confiáveis.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 40

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Ética e prática autorizada

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) explicar por que é a autorização, e não a capacidade técnica, que define o trabalho de segurança legítimo; (2) escrever um documento simples de regras de engajamento para um exercício; (3) tratar uma descoberta acidental sobre um sistema real por meio da divulgação coordenada; e (4) raciocinar sobre conflitos entre segurança, safety, privacidade e continuidade do serviço usando um código profissional. O capítulo se apoia nos Capítulos 1–9 e rege toda atividade prática no restante do livro.

### 10.1 A autorização é a linha

O mesmo comando pode ser manutenção ou crime. O que os separa é a **autorização**: a permissão explícita de alguém com direito a concedê-la, para um escopo, um período e um método definidos. A maioria das jurisdições criminaliza o acesso não autorizado a sistemas computacionais, e nos serviços críticos o teste não autorizado também pode pôr pessoas em perigo: uma varredura inofensiva para um notebook pode derrubar um controlador. Então a regra deste livro é simples e absoluta — o trabalho prático usa os laboratórios sintéticos do livro, sistemas que são seus ou sistemas cujo dono deu permissão escrita e específica. A curiosidade sobre o dispositivo exposto de uma concessionária real não é permissão.

### 10.2 Regras de engajamento

Os exercícios autorizados são registrados por escrito em **regras de engajamento** (RoE): quem autoriza (por nome e papel); o escopo (quais sistemas, quais endereços e, explicitamente, o que está excluído — os sistemas de segurança costumam estar); a janela de tempo; os métodos permitidos; as condições de parada ("qualquer alarme de processo inesperado: pare e ligue para o engenheiro de turno"); o plano de comunicação; o tratamento dos dados encontrados; e como os resultados serão relatados. As RoE protegem o serviço, a organização e quem testa. Na TO, as RoE costumam ser acordadas com os engenheiros de operação e de safety, e não só com a equipe de segurança de TI, e muitas vezes limitam o teste à observação passiva ou a réplicas offline.

### 10.3 Divulgação

Se você encontrar uma vulnerabilidade por acaso — uma página pública expondo uma interface de controle, um e-mail enviado ao destinatário errado —, o caminho ético é parar, não explorar mais, e reportar em privado ao dono ou por meio de um coordenador. A **divulgação coordenada de vulnerabilidades** dá ao dono ou ao fornecedor tempo para corrigir antes que os detalhes sejam publicados; órgãos nacionais como a CISA mantêm programas que fazem a coordenação entre quem encontra e os fornecedores ([programa de CVD da CISA](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program)). Registre o que você viu e quando, mantenha isso em sigilo e não guarde dados a que você não tinha direito de acesso.

### 10.4 Códigos profissionais e conflitos

O Código de Ética da ACM pede aos profissionais de computação que contribuam para a sociedade e o bem-estar humano, evitem danos, sejam honestos e respeitem a privacidade, e que "acessem recursos de computação e comunicação apenas quando autorizados ou quando compelidos pelo bem público" ([ACM Code, 2018](https://www.acm.org/code-of-ethics)). Os dilemas reais põem esses deveres uns contra os outros. Um hospital deveria adiar um patch de segurança numa frota de ventiladores porque a atualização exige tirar os dispositivos de serviço durante um pico de doenças respiratórias? Uma concessionária deveria compartilhar os detalhes de um incidente com outras concessionárias quando os seus advogados aconselham silêncio? Uma abordagem estruturada ajuda: identifique as partes interessadas e os danos; identifique os deveres e quem os detém; considere alternativas (aplicar o patch num subconjunto, acrescentar um controle compensatório); decida; registre o raciocínio e quem aceitou o risco residual.

### 10.5 Exemplo resolvido: a IHM aberta (sintético)

**Este caso é sintético.** Um estudante procurando informações sobre estágio no site público da Calder Water segue um link que abre uma página web intitulada "Pump Station 4 — operator view". Nenhuma senha foi pedida. A resposta ética: não clicar em nada na página, não tentar outros links, fazer uma captura de tela só da barra de endereço e do título, apenas se for necessária para reportar, fechar a página e mandar um e-mail ao contato de segurança publicado da CW (ou, se não houver, ao CERT/CSIRT nacional) dizendo o que foi visto, quando e como foi alcançado. Não publicar nada sobre isso. Não "conferir se está mesmo ativo". O orientador de ética da universidade do estudante deve ser informado. Neste caso sintético, a CW agradece ao estudante, remove o link e descobre que a página era uma demonstração de fornecedor deixada num servidor web — um lembrete de que quem encontra raramente conhece o quadro completo.

### 10.6 Atividade prática

Escreva RoE de uma página para o Laboratório I (Capítulo 25), que roda apenas os laboratórios offline do livro no seu próprio computador. Mesmo para um escopo trivial, preencha todos os títulos: quem autoriza, escopo, exclusões, janela, métodos, condições de parada, tratamento de dados e relato.

Para as condições de parada, "qualquer comportamento inesperado do meu próprio computador, ou qualquer tentativa de um script de acessar a rede" é específico e observável. Nomeie a si mesmo como quem autoriza e quem testa no escopo, e o seu tutor como a pessoa avisada se ocorrer uma condição de parada.

### 10.7 Erros comuns e limites

- "Estava acessível publicamente, então era permitido."
- Autorização verbal, ou autorização de alguém que não é dono do sistema.
- Ampliação do escopo durante um teste ("já que estou aqui…").
- Guardar os dados encontrados durante um teste depois do engajamento.
- Tratar a ética como uma lista de conformidade, e não como um dever de raciocínio.

O exemplo resolvido da IHM aberta testa os três primeiros. A página estava acessível publicamente, mas ninguém na CW autorizou uma visita; um colega dizendo "pode ir" não é dono do sistema; e clicar em "só mais um link" para conferir se está ativa é ampliação de escopo. O quarto se aplicaria se o estudante guardasse a captura de tela depois de reportar. O quinto é o motivo de o estudante também ter avisado o orientador de ética.

### Exercícios — capítulo 10

**EX019 — Escreva as condições de parada.** *Objetivo:* proteger um serviço em operação durante um teste autorizado. *Entradas:* a CPN autoriza uma captura passiva de tráfego de rede na sua sala de controle por um dia. *Etapas:* escreva cinco condições de parada e diga quem é chamado em cada uma. *Evidência esperada:* lista. *Rubrica:* 3 = cinco condições específicas e observáveis (alarme de processo, comportamento inesperado de dispositivo, descoberta de tráfego de sistema de segurança fora do escopo, pedido de um operador, dados de tipo sensível) com papéis nomeados; 2 = genéricas; 1 = menos de três; 0 = nada.

**EX020 — O dilema do patch.** *Objetivo:* estruturar uma decisão ética. *Entradas:* o exemplo do patch dos ventiladores na discussão sobre códigos profissionais deste capítulo. *Etapas:* liste as partes interessadas e os danos, duas alternativas a "aplicar o patch em todos agora" ou "em nenhum", e escreva um registro de decisão de 150 palavras nomeando quem aceita o risco residual. *Evidência esperada:* a análise e o registro. *Rubrica:* 3 = danos dos dois lados, alternativas críveis (patch escalonado, isolamento mais monitoramento), donos clínico e de segurança nomeados; 2 = só um lado; 1 = opinião sem estrutura; 0 = nada.

### Síntese do capítulo

A autorização define o trabalho de segurança legítimo. Escreva regras de engajamento, pare quando topar com algo real e reporte em privado, e raciocine explicitamente sobre os conflitos entre deveres, registrando quem aceitou qual risco. Nos serviços críticos, um teste descuidado pode ferir pessoas.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 40

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operacionais

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) explicar processos, proteção de memória, permissões de arquivos e privilégio; (2) descrever como um sistema operacional impõe o menor privilégio e onde ele não consegue; (3) comparar sistemas operacionais de uso geral, de tempo real e embarcados nos serviços críticos; e (4) montar uma lista de hardening e uma decisão de patch para um dispositivo que não pode ser reiniciado à vontade. O capítulo se apoia nas camadas do Capítulo 2 e prepara o Capítulo 13 (identidade) e o Capítulo 24 (controles).

### 11.1 O que o sistema operacional faz

O **sistema operacional** (SO) reparte uma máquina entre muitos programas e usuários. Um **processo** é um programa em execução com a sua própria memória; o SO usa a proteção de memória do hardware para que um processo não consiga ler nem sobrescrever a memória de outro. O **kernel** é o núcleo privilegiado que gerencia o hardware; os programas de usuário pedem serviços a ele por meio de **chamadas de sistema**. Os arquivos têm **permissões** — em sistemas do tipo Unix, leitura, escrita e execução para o dono, um grupo e os demais — e o SO as confere a cada acesso. O **privilégio** é a capacidade de contornar essas verificações: a conta root do Unix, o Administrator do Windows. Os princípios de Saltzer e Schroeder do **menor privilégio** e da **mediação completa** — todo acesso conferido, todo programa recebendo só os direitos de que precisa — continuam sendo a base ([Saltzer and Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939)).

### 11.2 Tipos de SO nos serviços críticos

Os sistemas de **uso geral** (Windows, Linux, macOS) rodam servidores, estações de trabalho de operadores e PCs de escritório; são ricos em recursos, recebem patches com frequência e são amplamente atacados. Os **sistemas operacionais de tempo real** (RTOS) garantem que as tarefas cumpram prazos — um relé de proteção precisa agir em milissegundos — e rodam em controladores, relés e dispositivos médicos; são pequenos e recebem patches com menos frequência. O **firmware embarcado** em sensores e dispositivos simples pode não ter separação alguma entre programas. A consequência: as proteções de SO mais fortes existem nas máquinas mais fáceis de substituir, e as mais fracas, nas máquinas que duram mais.

### 11.3 Hardening

O **hardening** reduz o que um atacante pode usar. Uma lista prática: remover ou desativar serviços e softwares não usados; trocar contas e senhas padrão; rodar os serviços com contas sem privilégio; ativar os logs e enviá-los para fora do host; restringir mídias removíveis; ativar a allowlist de aplicações onde a carga de trabalho for estável (as estações de trabalho de operadores são boas candidatas — rodam os mesmos poucos programas por anos); manter o horário sincronizado para que os logs possam ser correlacionados. Cada item deve ser verificável — um padrão de hardening que não pode ser verificado é um desejo.

### 11.4 Patches na operação

Na TI de escritório, aplicar patches é rotina. Numa estação de trabalho de operador ou num controlador, um patch pode exigir validação do fornecedor, uma janela de manutenção e um plano de reversão, porque uma atualização que falha pode parar o processo. Uma **decisão de patch baseada em risco** pergunta: a falha é explorável neste dispositivo tal como está implantado (alcançável? exige acesso local?); ela é sabidamente explorada; o que o dispositivo controla; quais controles compensatórios existem; quando é a próxima janela? O resultado é um destes: aplicar agora (mudança emergencial), aplicar na próxima janela, mitigar e monitorar até a substituição, ou aceitar com um dono nomeado. O guia de TO do NIST discute esses trade-offs ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

### 11.5 Exemplo resolvido: a estação de sinalização da CT (sintético)

**Este caso é sintético.** A estação de trabalho de controle de sinalização da Calder Transit roda um SO de uso geral. Uma atualização mensal corrige uma falha que permite a um usuário local de baixo privilégio tornar-se administrador. A estação não tem acesso à internet nem e-mail, tem a allowlist de aplicações ativada e só três sinaleiros nomeados fazem login nela. O fornecedor valida as atualizações do SO trimestralmente; o próximo pacote validado sai em sete semanas. Decisão: **aplicar na próxima janela**, porque a exploração exige uma conta local numa máquina rigidamente controlada; enquanto isso, confirmar que a allowlist está sendo imposta e revisar as três contas. Se a falha fosse explorável remotamente por um serviço de rede que a estação expõe, a resposta seria uma mudança emergencial ou a desativação desse serviço.

### 11.6 Atividade prática

No seu próprio computador, liste os processos em execução e a conta com que cada um roda; encontre um serviço que você não usa e descubra como ele poderia ser desativado (não desative nada sobre o que você tenha dúvida). Escreva uma lista de hardening de cinco itens para uma estação de atendimento de chamadas do CEDC, cada item com a forma de verificá-lo.

Para a estação do CEDC, escreva itens como "os atendentes fazem login com contas individuais sem direitos de administrador; verificação: listar os administradores locais todo mês" ou "armazenamento USB bloqueado; verificação: inserir um pendrive de teste durante a revisão trimestral".

### 11.7 Erros comuns e limites

- Rodar tudo como administrador "para evitar problemas de permissão".
- Fazer o hardening uma vez e nunca verificar o desvio.
- Aplicar a cadência de patches da TI de escritório à TO sem validação e reversão.
- Supor que um dispositivo sem interface de usuário de SO não tem SO.

A estação de sinalização da CT mostra as alternativas: allowlist e três contas nomeadas em vez de uso de administrador, um pacote trimestral validado pelo fornecedor em vez da cadência mensal do escritório, e uma revisão que confere se a allowlist ainda está sendo imposta. O quarto erro abrange as bombas de infusão do CVH, que rodam um RTOS que precisa de atualizações do fornecedor.

### Exercícios — capítulo 11

**EX021 — Decisão de patch.** *Objetivo:* aplicar as perguntas baseadas em risco. *Entradas:* uma falha explorável remotamente na interface web de um controlador do BMS do CVH; a interface é alcançável a partir da rede corporativa; a correção do fornecedor exige reiniciar o controlador por 30 minutos; a ventilação do centro cirúrgico depende do BMS. *Etapas:* responda às cinco perguntas de decisão de patch baseada em risco deste capítulo e recomende. *Evidência esperada:* respostas e recomendação com controles provisórios. *Rubrica:* 3 = restringir imediatamente o acesso à interface, agendar a reinicialização com a manutenção predial e o centro cirúrgico numa janela planejada, monitorar; 2 = desfecho certo, controles provisórios fracos; 1 = "aplicar o patch imediatamente" sem considerar a ventilação; 0 = nada.

**EX022 — Hardening verificável.** *Objetivo:* tornar os controles verificáveis. *Entradas:* três itens vagos: "proteger as contas", "ligar os logs", "travar o USB". *Etapas:* reescreva cada um como uma afirmação específica e verificável, com a verificação. *Evidência esperada:* três itens reescritos. *Rubrica:* 3 = específicos, observáveis, com método de verificação; 2 = específicos, sem verificação; 1 = ainda vagos; 0 = nada.

### Síntese do capítulo

O SO impõe separação, permissões e privilégio; o menor privilégio e a mediação completa são as suas ideias orientadoras. Nos serviços críticos, os dispositivos mais duráveis muitas vezes têm as proteções mais fracas, então o hardening precisa ser verificável e os patches precisam ser baseados em risco, agendados e reversíveis.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 40

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Probabilidade e estatística

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) aplicar as regras da adição, do complemento e da multiplicação e dizer quando os eventos são independentes; (2) usar o teorema de Bayes para interpretar um alerta, incluindo o efeito da taxa de base; (3) calcular a chance de pelo menos uma falha em tentativas repetidas e a chance de que um número suficiente de $n$ unidades redundantes esteja disponível; e (4) resumir dados assimétricos com medianas e percentis. O capítulo se apoia no Capítulo 1 e prepara os Capítulos 15, 27 e 29.

### 12.1 Regras que você vai usar o tempo todo

As probabilidades são números entre 0 e 1. A regra do **complemento**: $P(\text{not } A) = 1 - P(A)$. Para eventos **independentes**, $P(A \text{ and } B) = P(A)P(B)$. Para quaisquer eventos, $P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$ — somar sem subtrair a sobreposição conta duas vezes. Os problemas de "pelo menos um" são mais fáceis pelo complemento: se um backup falha em silêncio num dado dia com probabilidade $p$, de forma independente a cada dia, a chance de pelo menos uma falha silenciosa em $n$ dias é $1 - (1-p)^n$. A independência é uma premissa, muitas vezes falsa: dois geradores alimentados pelo mesmo tanque de combustível falham juntos. Essas falhas de **causa comum** são o motivo de a redundância ser mais fraca do que a regra da multiplicação sugere.

### 12.2 Probabilidade condicional e Bayes

$P(A \mid B)$ é a probabilidade de $A$ dado que $B$ ocorreu. O teorema de Bayes relaciona as duas direções:
$$P(\text{malicious} \mid \text{alert}) = \frac{P(\text{alert} \mid \text{malicious})\,P(\text{malicious})}{P(\text{alert})}.$$
Um detector com **taxa de verdadeiros positivos** de 95% e **taxa de falsos positivos** de 1% parece excelente. Se só 1 evento em 1.000 é malicioso, a maioria dos alertas continua falsa: a **taxa de base** domina. Esta é a ideia estatística mais importante nas operações de segurança, e ela explica por que os analistas se afogam em alertas.

### 12.3 Raciocínio binomial para a redundância

Se $n$ unidades idênticas estão, cada uma, disponíveis com probabilidade $1-p$, de forma independente, o número de unidades disponíveis segue uma distribuição **binomial**: $P(k \text{ available}) = \binom{n}{k}(1-p)^k p^{n-k}$. Uma estação de bombeamento que precisa de pelo menos 10 das suas 12 bombas consegue calcular com que frequência atende à demanda.

Para a estação de 12 bombas do Laboratório 6, com cada bomba indisponível 10 % do tempo, a soma sobre 10, 11 e 12 bombas disponíveis dá 0,889. Uma equipe de manutenção compartilhada ou uma única alimentação elétrica quebra a premissa de independência, então o número real é menor. Acrescentar uma décima terceira bomba eleva o resultado para cerca de 0,966, que é o tipo de comparação de que um pedido de investimento precisa.

### 12.4 Descrever os dados

Os tempos para detectar incidentes e se recuperar deles são **assimétricos**: a maioria é curta, alguns são muito longos. A **média** é puxada para cima pela cauda longa; a **mediana** (o valor do meio) não é; os **percentis** (o 90º percentil, p90) descrevem a cauda. Reporte a mediana e o p90 juntos, com o tamanho da amostra (Capítulo 29, Laboratório 12).

O Laboratório 12 mostra o efeito: o seu tempo médio para detectar é de 27,2 horas, enquanto a mediana é de 4,0.

Para um conselho, a frase "metade dos incidentes foi detectada em até 4 horas; um em cada dez levou mais de cerca de 56" carrega mais informação do que qualquer média isolada.

### 12.5 Exemplo resolvido e Laboratório 6 (sintético)

**Este caso é sintético.** O serviço de monitoramento da Calder Mutual vê 20.000 eventos por dia; os analistas estimam que 1 em 1.000 é malicioso; as taxas do detector são as citadas acima. O backup noturno da telemetria da CW falha em silêncio com probabilidade de 0,002 por dia. Uma estação de bombeamento tem 12 bombas, cada uma indisponível 10% do tempo.

```python
# Lab 6 - base rates, alarm volume and repeated trials (synthetic, offline)
from math import comb
prior, tpr, fpr = 0.001, 0.95, 0.01
ppv = tpr * prior / (tpr * prior + fpr * (1 - prior))
print(f"P(malicious | alert) = {ppv:.3f}")
events_per_day = 20_000
print(f"expected false alerts/day = {events_per_day * (1 - prior) * fpr:.0f}; true = {events_per_day * prior * tpr:.0f}")
p_day = 0.002   # chance per day that a given backup fails silently
for days in (30, 365):
    print(f"P(at least one silent backup failure in {days} days) = {1 - (1 - p_day) ** days:.3f}")
n, p = 12, 0.1  # 12 independent pumps, each unavailable 10% of the time
need = 10
print(f"P(at least {need} of {n} available) = {sum(comb(n, k) * (1-p)**k * p**(n-k) for k in range(need, n+1)):.3f}")
```

Saída esperada:

```text
P(malicious | alert) = 0.087
expected false alerts/day = 200; true = 19
P(at least one silent backup failure in 30 days) = 0.058
P(at least one silent backup failure in 365 days) = 0.518
P(at least 10 of 12 available) = 0.889
```

Menos de 1 alerta em 11 é real; os analistas enfrentam cerca de 200 alertas falsos por dia. Uma falha diária "rara" de backup é mais provável do que improvável ao longo de um ano — e é por isso que os exercícios de restauração, e não os logs de backup, são a evidência que importa. E uma estação que precisa de 10 de 12 bombas fica aquém cerca de 11% do tempo sob essas premissas: se as indisponibilidades das bombas compartilham uma causa (uma equipe de manutenção, uma alimentação elétrica), será pior.

### 12.6 Erros comuns e limites

- Ignorar a taxa de base (a falácia do "95% de acerto").
- Multiplicar as probabilidades de eventos que compartilham uma causa.
- Reportar uma média para tempos assimétricos sem a mediana e a cauda.
- Tratar entradas estimadas como exatas; as saídas herdam a sua incerteza.

O Laboratório 6 dá um número a cada um: 95 % de detecção ainda resulta numa chance de 0,087 de que um alerta seja real; dois geradores que compartilham combustível falham juntos com muito mais frequência do que 0,05 ao quadrado (EX024); a média de 27,2 horas para detectar do Laboratório 12 não descreve incidente algum; e a taxa de falha diária de backup de 0,002 é ela própria uma estimativa, então o número anual de 0,518 herda a sua incerteza.

### Exercícios — capítulo 12

**EX023 — Mude a taxa de base.** *Objetivo:* ver como a probabilidade a priori e a taxa de falsos positivos determinam o valor de um alerta. *Entradas:* Laboratório 6. *Etapas:* calcule $P(\text{malicious}\mid\text{alert})$ para uma priori de 0,01 e, separadamente, para uma priori de 0,001 com FPR de 0,001. Explique qual mudança ajuda mais e o que ela significa operacionalmente. *Evidência esperada:* dois valores e uma explicação. *Rubrica:* 3 = ≈ 0,490 e ≈ 0,487, com a explicação de que baixar a FPR (ajuste, enriquecimento) é a alavanca que os analistas controlam; 2 = só os valores; 1 = um valor; 0 = nada.

**EX024 — Causa comum.** *Objetivo:* quantificar o efeito das causas compartilhadas. *Entradas:* dois geradores de reserva, cada um falhando em partir com probabilidade de 0,05; com probabilidade de 0,02, uma causa compartilhada (combustível comum contaminado) faz os dois falharem. *Etapas:* calcule a probabilidade de os dois falharem supondo independência e depois com a causa comum (aproxime como $0.02 + 0.05^2$), e comente. *Evidência esperada:* dois números e um comentário. *Rubrica:* 3 = 0,0025 versus ≈ 0,0225, cerca de nove vezes pior, e uma solução (combustível separado, teste do combustível); 2 = só os números; 1 = um número; 0 = nada.

### Síntese do capítulo

As regras da probabilidade são simples; as suas premissas, não. As taxas de base decidem se vale a pena ler um alerta, "raro por dia" vira "provável por ano", a redundância é enfraquecida por causas comuns e os dados assimétricos precisam de medianas e percentis. Declare as premissas de independência e teste o que acontece quando elas falham.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 40

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Identidade e acesso

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) distinguir identificação, autenticação e autorização; (2) comparar fatores de autenticação e explicar por que métodos resistentes a phishing importam para o acesso remoto a sistemas críticos; (3) projetar o acesso baseado em papéis com segregação de funções; e (4) conduzir uma revisão de acessos que encontre contas órfãs, inativas, compartilhadas e com combinações tóxicas. O capítulo se apoia no Capítulo 6 (conjuntos) e no Capítulo 11 (privilégio) e prepara o Capítulo 16 (arquitetura) e o Capítulo 24 (controles).

### 13.1 Três perguntas

A **identificação** responde a "quem você diz ser?" (um nome de usuário). A **autenticação** responde a "prove" — com algo que você sabe (uma senha), tem (um token ou celular) ou é (uma impressão digital). A **autorização** responde a "o que você pode fazer?" — as permissões ligadas à identidade autenticada. Os erros em cada etapa diferem: uma autenticação fraca deixa entrar a pessoa errada; uma autorização excessiva deixa a pessoa certa (ou quem roubou a sessão dela) fazer coisas demais. As diretrizes de identidade digital do NIST definem requisitos para os autenticadores e recomendam opções resistentes a phishing para níveis de garantia mais altos ([SP 800-63B](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final)).

### 13.2 Fatores e acesso remoto

As senhas são adivinhadas, reutilizadas e capturadas por phishing. Os códigos de uso único enviados por SMS ou digitados a partir de um aplicativo acrescentam um segundo fator, mas podem ser repassados por uma página de login falsa convincente. Os autenticadores **resistentes a phishing** ligam o login criptograficamente ao site genuíno, de modo que um site falso não recebe nada utilizável. Para o acesso remoto à TO e a outros sistemas críticos — o caminho do alerta da CPN no Capítulo 5 —, a autenticação forte é necessária, mas não suficiente: a sessão deve cair num jump host controlado, ter tempo limitado, ser aprovada sessão a sessão para fornecedores e ser gravada.

### 13.3 Papéis e segregação de funções

No **controle de acesso baseado em papéis** (RBAC), as permissões se ligam a papéis ("scada-operator", "payments-approve") e as pessoas recebem papéis. Os papéis tornam as revisões viáveis: confere-se cinquenta papéis, e não cinquenta mil permissões individuais. A **segregação de funções** proíbe certas combinações: quem cria um pagamento não pode aprová-lo; o engenheiro que altera a lógica de controle não deveria controlar também o firewall que registra a alteração. Expressa com conjuntos (Capítulo 6), uma **combinação tóxica** $T$ é violada quando $T \subseteq \text{roles}(u)$.

O Laboratório 7 codifica as duas regras como conjuntos TOXIC e sinaliza chloe, que tem payments-create e payments-approve, e dev, que tem scada-engineer e firewall-admin e, além disso, está inativo há 214 dias.

### 13.4 O ciclo de vida das contas e as revisões

As contas são criadas quando as pessoas entram (**admissão**), alteradas quando elas mudam de função (**movimentação**) e removidas quando saem (**desligamento**). As falhas se acumulam em cada etapa: quem muda de função mantém os papéis antigos ("acúmulo de privilégios"), as contas de quem saiu permanecem, as contas de fornecedores são criadas para um projeto e nunca removidas, e as contas compartilhadas de operadores tornam as ações não rastreáveis. Uma **revisão de acessos** compara as contas com uma fonte autoritativa (o sistema de RH, o registro de contratos de fornecedores) e com o uso.

O Laboratório 7 mostra cada falha: *ben* saiu, mas manteve a sua conta, *vendorx* não tem dono no RH e não faz login há 304 dias, e *ops1* é compartilhada. Os dados de uso importam tanto quanto a situação no RH: *dev* está ativo no RH, mas inativo há 214 dias num papel privilegiado.

### 13.5 Exemplo resolvido e Laboratório 7 (sintético)

**Este caso é sintético.** Uma revisão conjunta das contas do sistema de controle da CPN e do sistema de pagamentos da Calder Mutual (combinados aqui só para fins didáticos) usa a situação no RH, o último login e duas combinações tóxicas.

```python
# Lab 7 - access review: orphans, dormant accounts and toxic combinations (synthetic, offline)
from datetime import date
TODAY = date(2026, 10, 1)
HR = {"ana": "active", "ben": "left", "chloe": "active", "dev": "active"}
ACCOUNTS = [  # user, roles, last login, shared?
    ("ana",   {"scada-operator"},                       date(2026, 9, 30), False),
    ("ben",   {"scada-engineer"},                       date(2026, 5, 2),  False),
    ("chloe", {"payments-create", "payments-approve"},  date(2026, 9, 29), False),
    ("dev",   {"scada-engineer", "firewall-admin"},     date(2026, 3, 1),  False),
    ("ops1",  {"scada-operator"},                       date(2026, 9, 30), True),
    ("vendorx", {"remote-support"},                     date(2025, 12, 1), False),
]
TOXIC = [{"payments-create", "payments-approve"}, {"scada-engineer", "firewall-admin"}]
for user, roles, last, shared in ACCOUNTS:
    issues = []
    if user not in HR: issues.append("no HR owner")
    elif HR[user] != "active": issues.append("owner has left")
    if (TODAY - last).days > 90: issues.append(f"dormant {(TODAY - last).days} d")
    if shared: issues.append("shared account")
    issues += ["toxic: " + "+".join(sorted(t)) for t in TOXIC if t <= roles]
    print(f"{user:8} {', '.join(issues) if issues else 'ok'}")
```

Saída esperada:

```text
ana      ok
ben      owner has left, dormant 152 d
chloe    toxic: payments-approve+payments-create
dev      dormant 214 d, toxic: firewall-admin+scada-engineer
ops1     no HR owner, shared account
vendorx  no HR owner, dormant 304 d
```

Ações: desativar *ben* agora (desligamento); remover um dos papéis de pagamento de *chloe*; remover os papéis privilegiados inativos de *dev* e perguntar se ele precisa de algum deles; *ops1* é um login compartilhado da sala de controle — comum em operações 24/7, em que uma troca de turno rápida importa —, então substitua-o por logins individuais e troca rápida de usuário ou, no mínimo, registre quem está no turno; *vendorx* deve ser desativada e reativada a cada sessão de suporte, sob um patrocinador nomeado. Note o que o script não consegue ver: se o papel de *ana* ainda corresponde ao trabalho dela.

### 13.6 Erros comuns e limites

- Igualar "autenticado" a "autorizado".
- Revisões que confirmam que as contas existem, e não se elas são necessárias.
- Remover contas compartilhadas numa sala de controle sem uma alternativa viável, de modo que a equipe passa a compartilhar senhas.
- Esquecer as contas de serviço e de fornecedores, que não têm registro no RH.

No Laboratório 7, o script confirma que a conta de *ana* está "ok" só no sentido de que ela está ativa e não inativa; se ela ainda precisa de `scada-operator` exige a gestora dela. Remover *ops1* de uma vez levaria a sala de controle a compartilhar a senha de uma pessoa, o que é pior. E *ops1* e *vendorx* aparecem ambas com "no HR owner", que é o sinal de que as contas de serviço e de fornecedores precisam de outra fonte autoritativa, como o registro de contratos.

### Exercícios — capítulo 13

**EX025 — Projete os papéis.** *Objetivo:* aplicar o menor privilégio e a segregação de funções. *Entradas:* o CEDC precisa de atendentes, despachantes, supervisores, um administrador do CAD e um engenheiro de suporte do fornecedor. *Etapas:* defina cinco papéis com as permissões principais e duas combinações tóxicas. *Evidência esperada:* tabela de papéis e combinações. *Rubrica:* 3 = papéis sensatos de menor privilégio, pares tóxicos justificados (por exemplo, administrador do CAD + administrador do log de auditoria; suporte do fornecedor + acesso permanente); 2 = papéis sem combinações; 1 = vago; 0 = nada.

**EX026 — Estenda a revisão.** *Objetivo:* acrescentar uma regra. *Entradas:* Laboratório 7. *Etapas:* acrescente uma verificação que sinalize qualquer conta com um papel privilegiado (`scada-engineer`, `firewall-admin`, `payments-approve`) que não tenha sido reaprovada em 180 dias, dado um novo campo `approved` (uma data). Escolha as datas de modo que pelo menos uma conta seja sinalizada e mostre a saída. *Evidência esperada:* código e saída. *Rubrica:* 3 = lógica correta, dados de teste escolhidos para mostrar casos sinalizados e não sinalizados; 2 = funciona, teste fraco; 1 = erro de lógica; 0 = nada.

### Síntese do capítulo

A identidade responde a três perguntas diferentes. Use autenticação forte e resistente a phishing para o acesso remoto crítico, conceda permissões por meio de papéis, proíba combinações tóxicas e revise as contas contra fontes autoritativas e o uso real. As contas compartilhadas e de fornecedores precisam de alternativas viáveis, e não apenas de proibições.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue estudando — capítulo 13 de 40

[← Capítulo 12](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos de privacidade

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) explicar a diferença entre segurança e privacidade; (2) aplicar princípios de proteção de dados como licitude, limitação da finalidade, minimização e limitação da conservação; (3) identificar dados pessoais nos sistemas dos serviços críticos, inclusive dados que se tornam pessoais quando combinados; e (4) recomendar projetos que protegem a privacidade para o monitoramento e os dados de incidentes. O capítulo se apoia no Capítulo 9 (dados) e no Capítulo 10 (ética) e prepara o Capítulo 29 (operações) e os requisitos éticos do trabalho de conclusão.

### 14.1 Segurança não é privacidade

A segurança protege os sistemas e as informações contra acesso, alteração e perda não autorizados. A **privacidade** trata de saber se o tratamento de informações sobre pessoas — mesmo um tratamento autorizado — é apropriado, proporcional e justo. Um banco de dados hospitalar perfeitamente seguro ainda pode violar a privacidade se for usado para uma finalidade sobre a qual os pacientes nunca foram informados. O [NIST Privacy Framework](https://www.nist.gov/privacy-framework) trata o risco de privacidade como algo que surge do próprio tratamento de dados, sobreposto ao risco de cibersegurança, mas distinto dele.

A detecção de clonagem da CT é o exemplo: guardar com segurança dois anos de validações ainda seria um problema de privacidade.

### 14.2 Princípios

O Regulamento Geral sobre a Proteção de Dados da UE estabelece princípios amplamente espelhados em outros lugares: licitude, lealdade e transparência; limitação da finalidade; minimização dos dados; exatidão; limitação da conservação; integridade e confidencialidade; e responsabilidade ([Regulation (EU) 2016/679, Article 5](https://eur-lex.europa.eu/eli/reg/2016/679/oj)). Os dados de saúde são uma **categoria especial**, que exige condições adicionais. Você não precisa se tornar advogado, mas precisa reconhecer quando uma questão de projeto também é uma questão de proteção de dados e envolver o encarregado de proteção de dados da organização — e nunca deve apresentar o resumo deste livro como aconselhamento jurídico para um caso específico.

### 14.3 Dados pessoais em lugares inesperados

Os serviços críticos guardam dados pessoais óbvios (prontuários, contas bancárias, chamadas de emergência) e dados menos óbvios. As leituras de medidores inteligentes em intervalos curtos podem revelar quando uma família está em casa. Os dados de bilhetagem de um cartão de transporte traçam os deslocamentos de uma pessoa. Os logs de segurança registram quem fez login, de onde e quando — dados pessoais sobre a equipe. A **combinação** importa: nem um código postal nem uma data de nascimento sozinhos costumam identificar alguém, mas juntos e com o sexo muitas vezes identificam. A pseudonimização (substituir nomes por códigos) reduz o risco, mas não é anonimização se a chave existir ou se a reidentificação for possível.

### 14.4 Privacidade nas operações de segurança

O monitoramento de segurança coleta dados sobre pessoas por concepção. Uma prática que protege a privacidade: coletar o que a finalidade de detecção exige, e não tudo o que está disponível; restringir o acesso aos logs brutos; definir prazos de retenção; pseudonimizar onde a análise não precisa de nomes; documentar a finalidade e a base legal; e, num incidente, compartilhar indicadores (endereços, hashes de arquivos) em vez de dados pessoais sempre que possível. Durante uma violação que envolva dados pessoais, podem se aplicar deveres de notificação em prazos curtos, então os planos de incidente incluem o encarregado de proteção de dados desde o início.

O projeto revisado da CT aplica quatro dessas práticas: 30 dias de detalhe, pseudônimos com chave, dois analistas nomeados e uma finalidade declarada.

### 14.5 Exemplo resolvido: análise de bilhetagem da CT (sintético)

**Este caso é sintético.** A equipe de segurança da Calder Transit quer detectar cartões de transporte clonados procurando o mesmo cartão usado em duas estações distantes demais num intervalo curto demais. O projeto proposto copia toda validação de cartão (ID do cartão, estação, hora) por dois anos para a plataforma de análise de segurança. Uma revisão de privacidade pergunta: dois anos são necessários? (A detecção de clonagem precisa de minutos a dias; reter o detalhe completo por 30 dias e depois agregar.) O ID do cartão é necessário em claro? (Um pseudônimo com chave basta para o casamento; só os casos confirmados são reidentificados, pela equipe de fraude.) Quem pode consultá-lo? (Dois analistas nomeados, com registro.) O histórico de viagens dos passageiros está sendo criado como efeito colateral? (Sim — e é por isso que o projeto limita a retenção e o acesso.) O projeto revisado atende à finalidade de detecção com uma fração do risco de privacidade.

### 14.6 Atividade prática

Escolha um serviço que você usa (um cartão de transporte, um medidor inteligente, um aplicativo de hospital). A partir do aviso de privacidade público, liste os dados pessoais coletados, as finalidades declaradas e a retenção. Identifique um item de dado cuja finalidade não esteja clara e redija uma pergunta que você poderia enviar ao fornecedor do serviço.

Observe se o aviso declara a retenção em dias ou anos, ou apenas "pelo tempo necessário"; esta última vale uma pergunta. Observe se o monitoramento de segurança aparece sequer como finalidade. Redija a sua pergunta de forma educada e específica, por exemplo perguntando por quanto tempo os dados por viagem são mantidos antes da agregação e quem pode acessá-los.

### 14.7 Erros comuns e limites

- "Somos seguros, portanto estamos em conformidade."
- Coletar tudo "caso seja útil".
- Chamar dados pseudonimizados de anônimos.
- Esquecer os dados da equipe nos logs.
- Dar conclusões jurídicas sem os assessores jurídicos e de proteção de dados da organização.

Cada um aparece nos exemplos deste capítulo. A cópia original das validações por dois anos da CT era segura e mesmo assim desproporcional. "Caso seja útil" é como o ID completo do cartão foi parar na plataforma de análise. Os pseudônimos com chave são reversíveis pela equipe de fraude, então não são anônimos. A proposta de monitoramento de acessos do CVH no EX027 registra os nomes da equipe, que são dados pessoais da equipe. E nenhum desses projetos deveria ser chamado de lícito sem o encarregado de proteção de dados.

### Exercícios — capítulo 14

**EX027 — Minimize um log.** *Objetivo:* aplicar a minimização ao monitoramento de segurança. *Entradas:* uma proposta do CVH de registrar todo acesso da equipe a prontuários com o nome completo do paciente, o diagnóstico, o nome do profissional, a estação de trabalho e a hora, retidos indefinidamente, para detectar acessos inadequados. *Etapas:* proponha um projeto minimizado que atenda à mesma finalidade. *Evidência esperada:* lista de campos, retenção, acesso e uma frase sobre a finalidade. *Rubrica:* 3 = identificador do registro no lugar do diagnóstico, retenção definida, acesso restrito, finalidade declarada, equipe informada; 2 = parcial; 1 = "registrar menos" sem projeto; 0 = nada.

**EX028 — Risco de combinação.** *Objetivo:* reconhecer a reidentificação. *Entradas:* a CW publica o consumo horário "anonimizado" por medidor, com código postal e tipo de imóvel. *Etapas:* explique dois riscos de reidentificação e duas mitigações. *Evidência esperada:* explicação. *Rubrica:* 3 = códigos postais pequenos com tipos de imóvel únicos identificam domicílios, a ocupação é inferível pelos padrões horários; mitigações: limiares de agregação, tempo ou localização mais grosseiros, acordos de acesso; 2 = um de cada; 1 = vago; 0 = nada.

### Síntese do capítulo

A privacidade pergunta se o tratamento de dados sobre pessoas é apropriado, e não só se ele é seguro. Aplique a limitação da finalidade, a minimização e a limitação da conservação — especialmente ao próprio monitoramento de segurança —, reconheça que as combinações reidentificam e envolva especialistas em proteção de dados, em vez de oferecer conclusões jurídicas.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue estudando — capítulo 14 de 40

[← Capítulo 13](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Evidência e medição

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) distinguir uma medição, um indicador e uma afirmação; (2) julgar a evidência pela sua fonte, método, atualidade e independência; (3) projetar uma métrica de segurança válida, confiável e difícil de manipular; e (4) usar a análise de sensibilidade para decidir se uma evidência incerta é boa o bastante para uma decisão. O capítulo se apoia nos Capítulos 1, 4 e 12 e prepara o Capítulo 18 (métodos de pesquisa), o Capítulo 27 (verificação) e o Capítulo 37 (revisão de evidências).

### 15.1 O que conta como evidência

Uma **afirmação** é uma declaração de que algo é verdade ("os nossos backups conseguem restaurar o sistema de despacho em quatro horas"). A **evidência** é o que a sustenta ou a enfraquece. A evidência varia em força. Uma **demonstração** (um exercício de restauração cronometrado na configuração de produção, no mês passado) é mais forte que um **documento** (uma política de backup), que é mais forte que uma **asserção** ("o fornecedor diz que funciona"). Faça quatro perguntas a qualquer evidência: *Fonte* — quem a produziu, e essa pessoa tem interesse na resposta? *Método* — como ela foi produzida, e alguém conseguiria repeti-la? *Atualidade* — ela ainda descreve o sistema como ele é agora? *Independência* — ela foi conferida por alguém que não seja quem fez a afirmação?

### 15.2 Medição e métricas

Uma **medição** é um valor obtido por um procedimento definido (o tempo de restauração em minutos, medido do início até a primeira transação de despacho bem-sucedida). Um **indicador** ou **métrica** é uma medição usada para acompanhar algo que nos importa. As boas métricas são **válidas** (medem o que importa — a porcentagem de ativos críticos com uma restauração testada, e não o número de rotinas de backup), **confiáveis** (duas pessoas medindo obtêm o mesmo resultado), **tempestivas** e **difíceis de manipular**. Vale o alerta de Goodhart: quando uma medida vira meta, as pessoas otimizam a medida. Uma métrica de patches de "porcentagem de sistemas com patch em até 30 dias" incentiva excluir os sistemas difíceis do denominador; reporte o denominador e as exclusões.

### 15.3 Incerteza e sensibilidade

A maior parte da evidência de segurança é incerta: amostras pequenas (Capítulo 12), estimativas (Capítulo 1), indicadores indiretos. A **análise de sensibilidade** pergunta quanto a decisão muda quando uma entrada incerta muda. Se uma recomendação se mantém em toda a faixa plausível, a evidência é adequada para essa decisão, mesmo que imprecisa. Se ela se inverte, colete evidências melhores sobre essa entrada ou torne a decisão robusta (escolha a opção aceitável em toda a faixa). Este é um antídoto prático tanto para a falsa precisão quanto para a paralisia.

O Laboratório 1 é o modelo: B continua à frente quando qualquer probabilidade isolada é reduzida à metade ou dobrada.

### 15.4 Exemplo resolvido: o despacho do CEDC é restaurável? (sintético)

**Este caso é sintético.** O conselho do CEDC pergunta: "Conseguimos restaurar o despacho assistido por computador em quatro horas depois de um ransomware?" Evidências disponíveis:

| Evidência | Tipo | Fonte | Atualidade | Independente? |
|---|---|---|---|---|
| A política de backup diz backups noturnos, objetivo de restauração de 4 h | Documento | Equipe de TI | 2024 | Não |
| O software de backup informa 362/365 rotinas bem-sucedidas | Medição (do backup, não da restauração) | Ferramenta | Ano passado | Não |
| Exercício de restauração: banco de dados restaurado em 2 h 40 min, aplicação não testada | Demonstração parcial | Equipe de TI | Há 8 meses | Não |
| Declaração do fornecedor: "a restauração completa costuma levar menos de 3 horas" | Asserção | Fornecedor | Sem data | Não |

Avaliação: nenhuma evidência demonstra a *afirmação* — uma restauração do serviço de despacho inteiro, incluindo os servidores de aplicação, as integrações e as credenciais, em condições de ransomware (em que o próprio servidor de backup pode estar cifrado). A resposta honesta ao conselho é "desconhecido, com evidência parcial de que só o banco de dados é restaurado em quatro horas". Recomendação: um exercício de restauração de ponta a ponta num ambiente isolado, observado pela auditoria interna, medindo o tempo até o primeiro despacho de teste bem-sucedido; e a confirmação de que pelo menos uma cópia de backup está offline ou é imutável.

### 15.5 Atividade prática

Pegue uma afirmação sobre um serviço que você usa ("o meu celular faz backup das minhas fotos"). Liste as evidências que você tem, classifique cada item por tipo, fonte, atualidade e independência e projete um teste que demonstraria a afirmação. Não rode nada em sistemas que não são seus.

Para um backup de celular, o teste mais forte é restaurar uma foto em outro dispositivo seu, cronometrando e registrando a data. O "último backup: hoje" de um aplicativo de backup é uma medição do backup, e não da restauração.

### 15.6 Erros comuns e limites

- Tratar o sucesso do backup como evidência de restauração.
- Métricas que contam atividade em vez de resultados.
- Denominadores que excluem em silêncio os casos mais difíceis.
- Ignorar o interesse da fonte da evidência.
- Exigir uma precisão de que a decisão não precisa, ou aceitar uma confiança que não foi conquistada.

A tabela de evidências do CEDC mostra o primeiro: 362 de 365 rotinas bem-sucedidas não dizem nada sobre restaurar a aplicação. O segundo aparece quando uma equipe reporta o número de rotinas de backup em vez das restaurações testadas. O terceiro é a métrica de patches que deixa de fora os sistemas difíceis. O quarto é o "menos de 3 horas" sem data do fornecedor. O quinto corta para os dois lados: o conselho não precisa de minutos, mas não pode aceitar "provavelmente está tudo bem".

### Exercícios — capítulo 15

**EX029 — Classifique a evidência.** *Objetivo:* aplicar as quatro perguntas. *Entradas:* a afirmação "o serviço de cartões da Calder Mutual faz failover para o seu segundo data center em 15 minutos"; evidências: diagrama de arquitetura (2025), relatório do teste de failover do ano passado feito pela equipe de operações (14 min), nota do auditor de que o teste foi anunciado com uma semana de antecedência. *Etapas:* classifique cada item e declare o que a evidência mostra e o que não mostra. *Evidência esperada:* tabela e duas frases. *Rubrica:* 3 = reconhece o teste como uma demonstração real, mas anunciada e não independente, e pede um teste não anunciado ou observado de forma independente sob carga realista; 2 = parcial; 1 = aceita a afirmação; 0 = nada.

**EX030 — Corrija uma métrica.** *Objetivo:* projetar uma métrica válida e difícil de manipular. *Entradas:* "número de cursos de conscientização sobre phishing concluídos". *Etapas:* proponha uma métrica melhor para o risco de phishing de credenciais, defina a sua medição e nomeie uma forma de manipulá-la. *Evidência esperada:* definição e risco de manipulação. *Rubrica:* 3 = métrica orientada a resultados (por exemplo, a fração de contas privilegiadas com autenticação resistente a phishing, ou a taxa de reporte em simulações autorizadas) com procedimento definido e um risco de manipulação honesto; 2 = melhor, mas definida de forma frouxa; 1 = métrica de atividade; 0 = nada.

### Síntese do capítulo

A evidência tem uma fonte, um método, uma data e um grau de independência. Meça resultados em vez de atividade, reporte os denominadores e use a análise de sensibilidade para decidir se uma evidência incerta é boa o bastante. "Desconhecido, com evidência parcial" é muitas vezes a resposta mais honesta e mais útil.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue estudando — capítulo 15 de 40

[← Capítulo 14](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Arquitetura de segurança

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) aplicar os princípios clássicos de projeto — menor privilégio, padrões à prova de falha, economia de mecanismo, mediação completa, separação de privilégio; (2) descrever uma arquitetura de referência em camadas para um operador de serviço crítico, da empresa ao campo; (3) explicar a defesa em profundidade e o zero trust e os seus limites na tecnologia operacional; e (4) projetar um acesso remoto seguro para fornecedores. O capítulo se apoia nos Capítulos 7, 11 e 13 e prepara o Capítulo 21 (modelos de sistema) e o Capítulo 24 (controles).

### 16.1 Princípios que duram

Os princípios de Saltzer e Schroeder, de 1975, ainda enquadram a arquitetura de segurança ([Saltzer and Schroeder](https://doi.org/10.1109/PROC.1975.9939)): **economia de mecanismo** (manter tudo simples o bastante para ser verificado); **padrões à prova de falha** (negar a menos que seja permitido); **mediação completa** (conferir todo acesso); **projeto aberto** (a segurança não deve depender do sigilo do projeto); **separação de privilégio** (exigir mais de uma condição — duas pessoas, duas chaves); **menor privilégio**; **menor mecanismo comum** (minimizar os componentes compartilhados); e **aceitabilidade psicológica** (se for difícil demais de usar, as pessoas contornam). Cada um é uma lente para revisar um projeto: "o que aqui não é mediado? o que é compartilhado? o que os operadores vão contornar às 03:00?"

### 16.2 Uma arquitetura de referência em camadas

Os operadores de serviços críticos costumam separar: a zona **corporativa** (e-mail, escritório, sistemas de negócio); uma **DMZ** para a troca de dados (réplicas do historiador, servidores de patches, jump hosts de acesso remoto); **operações/controle** (servidores SCADA, IHMs, estações de engenharia); **campo** (controladores, RTUs, relés de proteção); e os sistemas de **segurança (safety)**, que agem de forma independente para evitar danos. O tráfego entre as camadas passa por conduítes com regras explícitas (Capítulo 7). O guia de TO do NIST e a série ISA/IEC 62443 descrevem essas arquiteturas ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). O ponto não é o desenho, e sim a **propriedade** que ele deveria garantir: nenhum caminho direto da internet ou do e-mail até qualquer coisa que controle um processo físico.

### 16.3 Defesa em profundidade e zero trust

A **defesa em profundidade** empilha controles independentes para que uma falha não seja catastrófica: segmentação, hardening, autenticação, monitoramento, backups, contingência manual. A sua fraqueza é o **modo comum**: camadas que compartilham uma conta de administrador ou um servidor de gerenciamento caem juntas. O **zero trust** elimina a confiança implícita baseada na localização na rede; toda requisição é autenticada e autorizada por recurso ([NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)). Na TI corporativa, é uma direção forte. Na TO, muitos dispositivos não conseguem autenticar requisições individuais, então as ideias de zero trust se aplicam sobretudo nas fronteiras — usuários, estações de engenharia, acesso remoto —, enquanto a segmentação protege os dispositivos que não conseguem se defender sozinhos.

### 16.4 Acesso remoto

Os fornecedores e os engenheiros precisam de acesso remoto; o acesso remoto descontrolado é um dos caminhos mais comuns para dentro da TO. Um padrão defensável: o acesso termina num **jump host** na DMZ, nunca diretamente na zona de controle; autenticação **multifator resistente a phishing**; **aprovação por sessão** pelo operador de turno para fornecedores; contas com **tempo limitado**; **gravação das sessões**; e um **botão de desligar** que a sala de controle possa usar. Cada elemento responde a uma falha específica.

O novo projeto da CPN usa todos os elementos: um jump host na DMZ, contas de fornecedores ativadas por tíquete por até quatro horas, MFA resistente a phishing, sessões gravadas e um interruptor na sala de controle. O que ele não consegue impedir é o mau uso dentro de uma sessão de fornecedor aprovada de quatro horas.

### 16.5 Exemplo resolvido: o acesso remoto da CPN (sintético)

**Este caso é sintético.** O projeto atual da CPN: o gateway VPN-G exposto à internet (Capítulo 5) põe os usuários diretamente na rede de controle; três fornecedores têm contas permanentes; só senhas. Novo projeto: o VPN-G é atualizado e passa a terminar num jump host na DMZ; as contas de fornecedores ficam desativadas por padrão e são ativadas por tíquete pelo supervisor da sala de controle por até quatro horas; MFA resistente a phishing para a equipe; sessões gravadas num servidor que os fornecedores não conseguem alcançar; um interruptor físico na sala de controle que desativa o conduíte de acesso remoto. Risco residual, declarado: uma sessão de fornecedor aprovada continua sendo confiável durante a sua janela; a gravação apoia a detecção e a responsabilização, mas não impede o mau uso em tempo real.

### 16.6 Atividade prática

Desenhe a arquitetura da Calder Water do Capítulo 7 com as suas zonas e os três conduítes permitidos. Anote em cada conduíte o princípio a que ele serve e o controle que o impõe. Marque o componente cujo comprometimento mais prejudicaria e explique por quê.

Na arquitetura da CW, cada conduíte serve a um princípio: a visualização por HTTPS do corporativo para a DMZ aplica o menor privilégio, a leitura OPC UA do coletor da DMZ aplica a mediação completa no conduíte, e a consulta Modbus do SCADA ao campo se apoia nos padrões à prova de falha, negando todo o resto. O servidor SCADA é um forte candidato a componente cujo comprometimento mais prejudica, porque ele consegue tanto ver quanto comandar todos os controladores de campo.

### 16.7 Erros comuns e limites

- Diagramas de arquitetura que mostram as conexões pretendidas, e não as reais.
- Máquinas "dual-homed" que ligam zonas e contornam o conduíte.
- Camadas que compartilham administradores, credenciais ou ferramentas de gerenciamento.
- Aplicar os slogans do zero trust a dispositivos que não conseguem se autenticar.

No caso da CW, a conexão RDP do Laboratório 4, do corporativo direto para o controle, é o primeiro erro: um caminho que o diagrama não mostra. Um notebook de engenharia dual-homed é a causa habitual. O servidor de gerenciamento do CVH que administra firewalls, proteção de endpoints e backups com uma única conta (EX032) é o terceiro. O quarto se aplica às RTUs e aos PLCs.

### Exercícios — capítulo 16

**EX031 — Revisão por princípios.** *Objetivo:* usar os princípios como lentes de revisão. *Entradas:* o projeto original de acesso remoto da CPN no exemplo resolvido deste capítulo. *Etapas:* nomeie quatro princípios de Saltzer–Schroeder que ele viola e como. *Evidência esperada:* quatro pares princípio–violação. *Rubrica:* 3 = quatro corretos (menor privilégio, padrões à prova de falha, mediação completa, separação de privilégio ou menor mecanismo comum) com explicação específica; 2 = três; 1 = um ou dois; 0 = nada.

**EX032 — Modo comum.** *Objetivo:* encontrar dependências compartilhadas escondidas. *Entradas:* o CVH tem firewalls de segmentação, proteção de endpoints e backups — todos administrados a partir de um servidor de gerenciamento usando uma única conta de administrador de domínio. *Etapas:* explique o risco de modo comum e proponha duas mudanças. *Evidência esperada:* explicação e mudanças. *Rubrica:* 3 = o comprometimento da conta/do servidor desativa as três camadas; mudanças como níveis/credenciais de administração separados e backups offline; 2 = uma mudança; 1 = vago; 0 = nada.

### Síntese do capítulo

A arquitetura transforma princípios em propriedades impostas: nenhum caminho direto da internet até qualquer coisa que mova o mundo físico. Empilhe controles independentes, fique atento aos modos comuns, aplique o zero trust onde os dispositivos podem participar e segmente onde não podem, e trate o acesso remoto como o conduíte mais importante a projetar bem.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue estudando — capítulo 16 de 40

[← Capítulo 15](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Conceitos de criptografia

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) explicar o que hash, cifração simétrica, códigos de autenticação de mensagens, cifração de chave pública e assinaturas digitais garantem e não garantem; (2) explicar por que a integridade e a autenticidade, mais que o sigilo, são as necessidades criptográficas dos sistemas de controle; (3) usar HMAC com um número de sequência para rejeitar comandos alterados e repetidos; e (4) tornar um log evidente a adulterações com uma cadeia de hashes e uma âncora externa. O capítulo se apoia nos Capítulos 5 e 8 e prepara o Capítulo 24 (controles) e o Capítulo 29 (operações).

### 17.1 As ferramentas e as suas garantias

Uma **função de hash criptográfica** como a SHA-256 mapeia qualquer entrada num resumo de tamanho fixo; é inviável encontrar duas entradas com o mesmo resumo ou recuperar a entrada ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)). Um hash sozinho não prova nada sobre *quem* produziu os dados: qualquer um pode recalculá-lo. A **cifração simétrica** (por exemplo, o AES, [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final)) fornece confidencialidade com uma chave compartilhada. Um **código de autenticação de mensagem** (MAC) como o HMAC ([RFC 2104](https://www.rfc-editor.org/rfc/rfc2104); [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final)) permite que quem tem a chave compartilhada verifique que uma mensagem foi produzida por outro detentor da chave e não foi alterada. A criptografia de **chave pública** ([Diffie and Hellman, 1976](https://doi.org/10.1109/TIT.1976.1055638); [Rivest, Shamir and Adleman, 1978](https://doi.org/10.1145/359340.359342)) permite as **assinaturas digitais**: qualquer um com a chave pública pode verificar, só quem tem a chave privada pode assinar — a base do firmware assinado e dos certificados. Protocolos como o TLS 1.3 combinam essas ferramentas para fornecer canais autenticados e cifrados ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)).

### 17.2 Do que os sistemas de controle precisam

Para um comando de disjuntor, o sigilo raramente é o ponto; o que importa é a **autenticidade** (veio do centro de controle), a **integridade** (não foi alterado) e o **frescor** (não é um comando antigo repetido). Um MAC fornece as duas primeiras. O frescor precisa de um **número de sequência** ou de um carimbo de tempo dentro da mensagem autenticada, e de um receptor que rejeite tudo o que não for mais novo que o último valor aceito. Sem frescor, um atacante que gravou o "OPEN" válido de ontem pode repeti-lo hoje.

O Laboratório 8 demonstra as duas coisas: o nome de disjuntor alterado falha no MAC, e a sequência 41 é rejeitada depois de já ter sido aceita.

### 17.3 As chaves são a parte difícil

A criptografia desloca o problema de proteger os dados para proteger as chaves. Quem gera as chaves, onde elas ficam guardadas, como são trocadas e revogadas, e o que acontece quando a chave de um dispositivo de campo vaza — isso determina a segurança real. As chaves nunca devem estar fixas em código publicado (a chave do Laboratório 8 é deliberadamente pública), nunca devem ser compartilhadas entre todos os dispositivos e devem ficar em hardware sempre que possível. Planejar com antecedência também importa: o NIST finalizou os seus primeiros padrões de criptografia pós-quântica em 2024 ([NIST, 2024](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)), e uma infraestrutura com vida útil de 20 anos precisa da capacidade de trocar de algoritmo ("agilidade criptográfica").

### 17.4 Exemplo resolvido e Laboratório 8 (sintético)

**Este caso é sintético.** A CPN autentica os comandos de disjuntor com HMAC-SHA-256 sobre uma mensagem que contém um número de sequência e mantém um log encadeado por hashes das ações dos operadores, cuja cabeça mais recente é copiada de hora em hora para um servidor separado (a **âncora**).

```python
# Lab 8 - HMAC message authentication and a hash-chained log (synthetic; DEMO KEY ONLY, offline)
import hmac, hashlib
KEY = b"demo-key-published-in-a-textbook-never-use"
def tag(msg): return hmac.new(KEY, msg, hashlib.sha256).hexdigest()[:16]
cmd = b"seq=41;breaker=F7;op=OPEN"
t = tag(cmd)
print("tag:", t)
print("valid original:", hmac.compare_digest(t, tag(cmd)))
print("valid altered :", hmac.compare_digest(t, tag(b"seq=41;breaker=F2;op=OPEN")))
last_seq = 41
print("replay of seq 41 accepted?", 41 > last_seq)
# hash chain: each entry commits to the previous head
def chain(entries):
    head, heads = "0" * 64, []
    for e in entries:
        head = hashlib.sha256((head + e).encode()).hexdigest(); heads.append(head)
    return heads
log = ["08:00 login ana", "08:05 setpoint PS2 4.1m", "08:09 logout ana"]
good = chain(log)
log[1] = "08:05 setpoint PS2 2.0m"
bad = chain(log)
print("anchored head:", good[-1][:12], "| recomputed after edit:", bad[-1][:12])
print("first differing entry:", next(i for i, (a, b) in enumerate(zip(good, bad)) if a != b))
```

Saída esperada:

```text
tag: 347e6a26d1844d03
valid original: True
valid altered : False
replay of seq 41 accepted? False
anchored head: c5754d1d1639 | recomputed after edit: 65e0b2a20fac
first differing entry: 1
```

O nome de disjuntor alterado falha na verificação; o número de sequência repetido é rejeitado; o log editado já não corresponde à cabeça ancorada, e a comparação mostra a primeira entrada alterada. Truncar a tag em 64 bits mantém a impressão curta; os sistemas reais usam a tag completa ou uma truncagem padronizada. A cadeia de hashes detecta a edição **somente** se a âncora estiver fora do alcance de quem edita — alguém que controla tanto o log quanto a âncora consegue reconstruir a cadeia inteira.

### 17.5 Erros comuns e limites

- Usar um hash simples onde é preciso um MAC ou uma assinatura.
- Autenticar mensagens sem frescor.
- Comparar tags com `==` em vez de uma comparação de tempo constante.
- Uma única chave compartilhada para todos os dispositivos.
- Acreditar que a cifração torna confiável um endpoint comprometido.

No Laboratório 8, um SHA-256 simples do comando permitiria a quem o altera calcular um resumo novo. O MAC sem `seq=` aceitaria o OPEN de ontem. O laboratório usa `hmac.compare_digest` em vez de `==`. Uma única chave em todas as RTUs significa que uma chave vazada compromete a rede. E a cifração não ajudaria se a própria IHM do centro de controle enviasse comandos forjados.

### Exercícios — capítulo 17

**EX033 — Escolha a primitiva.** *Objetivo:* casar necessidades com ferramentas. *Entradas:* (a) atualizações de firmware das bombas de infusão do CVH vindas do fabricante; (b) comandos do centro de controle da CPN para as suas próprias RTUs; (c) prontuários num notebook perdido; (d) detectar edições num log de auditoria. *Etapas:* escolha uma primitiva para cada um e justifique. *Evidência esperada:* quatro escolhas. *Rubrica:* 3 = assinaturas, MAC com frescor (ou um canal autenticado), cifração simétrica com proteção da chave, cadeia de hashes com âncora externa; 2 = uma errada; 1 = duas erradas; 0 = nada.

**EX034 — Quebre a âncora.** *Objetivo:* raciocinar sobre a confiança na âncora. *Entradas:* Laboratório 8. *Etapas:* explique como um administrador com acesso de escrita tanto ao servidor de logs quanto à âncora poderia esconder uma edição e proponha duas mudanças de projeto que impeçam isso. *Evidência esperada:* descrição do ataque e mudanças. *Rubrica:* 3 = recalcular a cadeia e sobrescrever a âncora; mudanças: âncora mantida por outra equipe/outro sistema com armazenamento só de acréscimo, publicação externa periódica ou carimbos de tempo assinados; 2 = uma mudança; 1 = só a descrição; 0 = nada.

### Síntese do capítulo

Cada primitiva garante algo específico: os hashes detectam mudanças só contra uma referência confiável, os MACs e as assinaturas dão autenticidade, os números de sequência dão frescor e a cifração dá sigilo. Nos sistemas de controle, a autenticidade, a integridade e o frescor são o que mais importa, e a segurança real depende da gestão de chaves e de manter as âncoras fora do alcance de um atacante.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue estudando — capítulo 17 de 40

[← Capítulo 16](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Métodos de pesquisa I

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) transformar um tema numa pergunta pesquisável; (2) escolher entre desenhos descritivos, comparativos, experimentais e de estudo de caso; (3) encontrar, triar e resumir a literatura de forma sistemática e registrar como fez isso; e (4) identificar ameaças à validade num estudo de segurança. O capítulo se apoia nos Capítulos 4, 12 e 15 e prepara o Capítulo 23 (métodos de risco), o Capítulo 33 (métodos de pesquisa II) e a proposta do trabalho de conclusão (Capítulo 35).

### 18.1 Do tema à pergunta

"Ransomware em hospitais" é um tema. Uma **pergunta de pesquisa** é específica o bastante para que evidências possam respondê-la e alguém possa discordar: "Nos incidentes de ransomware publicamente relatados que afetaram hospitais em 2017–2024, com que frequência os relatos descreveram um recurso a processos em papel, e quais limites desse recurso eles mencionaram?" Uma boa pergunta nomeia a população (quais hospitais, quais incidentes), as variáveis (recurso descrito, limites mencionados), o período e o tipo de resposta (uma proporção e temas). No bacharelado, as perguntas que comparam — opções, setores, métodos — se ajustam melhor ao resultado do curso do que as que pretendem descobrir algo novo.

### 18.2 Desenhos

Os estudos **descritivos** dizem o que existe (um levantamento de inventário; uma contagem de alertas por setor). Os estudos **comparativos** contrastam grupos ou opções usando os mesmos critérios. Os estudos **experimentais** mudam uma coisa deliberadamente e medem o efeito, idealmente contra um controle (o experimento de limiar do detector do Capítulo 27). Os **estudos de caso** examinam um ou poucos casos em profundidade, usando várias fontes; eles explicam como e por quê, mas generalizam com cautela. Escolha o desenho de que a pergunta precisa, e não o que parece mais científico.

Para a pergunta sobre os backups do CEDC, o desenho comparativo é o adequado: três estratégias pontuadas pelos mesmos critérios. Um experimento compararia exercícios em condições controladas, e um estudo de caso examinaria em profundidade uma restauração passada. Cada um responde a uma pergunta diferente, então escolha o desenho depois de escrever a pergunta.

### 18.3 Literatura, de forma sistemática

Procurar fontes é em si um método e deve ser registrado: bases e sites pesquisados, termos de busca, data, critérios de inclusão e exclusão, números encontrados e mantidos. Distinga as fontes **primárias** (um alerta de uma agência, um relatório de um regulador, um estudo revisado por pares) das **secundárias** (uma notícia ou um blog que as resume). Prefira as primárias, cite o que leu (Capítulo 4) e registre por que excluiu o que excluiu, para que outra pessoa possa repetir a triagem. Uma planilha simples — fonte, tipo, data, relevância, constatação principal, limites — basta.

### 18.4 Validade

Quatro ameaças clássicas. **Validade de construto**: a medida captura o conceito? (Contar "incidentes relatados" mede o relato, e não os incidentes.) **Validade interna**: a causa alegada é mesmo a causa? (Hospitais com mais pessoal de segurança podem relatar mais incidentes porque detectam mais.) **Validade externa**: o resultado se generaliza? (Constatações de grandes hospitais urbanos podem não se aplicar a clínicas rurais.) **Confiabilidade**: outro pesquisador obteria o mesmo resultado? (Dois codificadores que classificam relatos de incidentes devem concordar; meça a concordância deles.) A crítica de Sommer e Paxson à detecção de intrusões por aprendizado de máquina é um exemplo clássico de problemas de validade externa na pesquisa em segurança ([Sommer and Paxson, 2010](https://doi.org/10.1109/SP.2010.25)).

### 18.5 Exemplo resolvido: uma pergunta comparativa (plano sintético)

**Este plano é sintético.** Um estudante do programa de estágio da CRP pergunta: "Qual de três estratégias de backup melhor sustenta a restauração em quatro horas do serviço de despacho do CEDC?" Desenho: comparativo, usando os mesmos critérios (tempo de restauração medido num exercício isolado, resiliência ao comprometimento do servidor de backup, carga operacional, custo). Dados: três restaurações cronometradas num ambiente de teste isolado fornecido pelo CEDC sob autorização escrita, documentação do fornecedor e entrevistas com dois administradores. Notas de validade: três exercícios são uma amostra pequena (reportar intervalos, Capítulo 37); o ambiente de teste pode diferir da produção (validade externa — documentar as diferenças); o estudante desenhou os exercícios (confiabilidade — pedir a um administrador que repita um deles). Produto: uma recomendação com premissas declaradas, e não uma afirmação universal sobre produtos de backup.

### 18.6 Atividade prática

Escreva três perguntas de pesquisa sobre um tema da sua escolha em segurança de setores críticos: uma descritiva, uma comparativa e uma de estudo de caso. Para cada uma, nomeie a população, as variáveis, o período e o tipo de evidência de que você precisaria.

Por exemplo, sobre dispositivos médicos sem suporte: descritiva, "quantos dispositivos clínicos do CVH estavam depois do fim do suporte em 2026?"; comparativa, "qual de três abordagens mais reduz a exposição dentro de um orçamento?"; estudo de caso, "como um hospital gerenciou as suas estações de imagem durante um atraso na substituição?" Anote, para cada uma, se a evidência pode ser obtida sob autorização.

### 18.7 Erros comuns e limites

- Perguntas amplas demais para serem respondidas ou estreitas demais para importarem.
- Buscas de literatura não registradas, que não podem ser repetidas.
- Generalizar demais a partir de um caso.
- Confundir a correlação nos dados de incidentes com causa.
- Coletar dados sobre pessoas ou sistemas reais sem aprovação ética e autorização (Capítulo 10).

O plano de backup do CEDC evita esses erros ao nomear a população (o serviço de despacho do CEDC), limitar a afirmação a três estratégias, registrar as fontes e tratar três exercícios como uma amostra pequena. Um estudo sobre "ransomware em hospitais" falharia no primeiro teste. Um estudante que entrevistasse administradores do CEDC sem consentimento falharia no quinto, qualquer que fosse a qualidade da análise.

### Exercícios — capítulo 18

**EX035 — Afie a pergunta.** *Objetivo:* tornar um tema pesquisável. *Entradas:* o tema "phishing no setor de energia". *Etapas:* escreva uma pergunta de pesquisa com população, variáveis, período e tipo de resposta; declare qual desenho se ajusta. *Evidência esperada:* pergunta e desenho. *Rubrica:* 3 = específica, respondível com evidências obtíveis, desenho justificado; 2 = específica, mas com evidências impossíveis de obter; 1 = ainda um tema; 0 = nada.

**EX036 — Nomeie a ameaça.** *Objetivo:* identificar ameaças à validade. *Entradas:* "Os hospitais que compraram o produto X tiveram 40% menos incidentes de ransomware relatados, então X previne ransomware." *Etapas:* nomeie e explique três ameaças à validade. *Evidência esperada:* três ameaças. *Rubrica:* 3 = construto (relatados vs reais), interna (fatores de confusão como orçamento/maturidade, seleção), externa (quais hospitais) ou confiabilidade; 2 = duas; 1 = uma; 0 = nada.

### Síntese do capítulo

A pesquisa começa com uma pergunta específica o bastante para ser respondida e contestada. Escolha o desenho de que a pergunta precisa, busque e trie a literatura de um modo que outra pessoa possa repetir e nomeie as ameaças à validade antes que um revisor o faça.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue estudando — capítulo 18 de 40

[← Capítulo 17](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Infraestrutura crítica e segurança setorial: escopo e teoria

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) explicar o que torna uma infraestrutura "crítica" e comparar como os Estados Unidos, a União Europeia e o Reino Unido a definem e organizam; (2) usar as ideias de funções críticas, interdependência e resiliência para analisar um serviço; (3) comparar três lentes teóricas — risco, resiliência e safety/sistemas — e dizer o que cada uma vê e o que deixa escapar; e (4) situar uma organização no seu contexto regulatório e setorial. O capítulo abre o núcleo da área do livro e se apoia em todos os Capítulos 1–18.

### 19.1 O que "crítico" significa

Uma infraestrutura é **crítica** quando a sua interrupção prejudicaria gravemente a saúde, a segurança, a segurança econômica ou o funcionamento da sociedade. Os governos operacionalizam isso de formas diferentes. Os Estados Unidos designam dezesseis setores de infraestrutura crítica, da energia e da água à saúde e aos serviços financeiros ([CISA, Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors)), e complementam os setores com um conjunto de **Funções Críticas Nacionais** — funções como "fornecer água" ou "prestar atendimento médico", cuja interrupção seria debilitante ([CISA, NCF set](https://www.cisa.gov/national-critical-functions-set)). A União Europeia regula a cibersegurança das entidades "essenciais" e "importantes" de muitos setores por meio da Diretiva NIS2 ([Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/)), a resiliência física e operacional mais ampla das "entidades críticas" por meio da Diretiva CER ([Directive (EU) 2022/2557](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)) e a resiliência operacional digital das entidades financeiras por meio do DORA ([Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)). O National Cyber Security Centre do Reino Unido publica o Cyber Assessment Framework usado para avaliar os operadores de serviços essenciais ([NCSC CAF](https://www.ncsc.gov.uk/collection/caf)).

A **visão por funções** é muitas vezes mais útil que a visão por setores. O Calder Valley Hospital é "saúde", mas a função de que as pessoas precisam é "prestar atendimento de emergência", que depende de eletricidade, água, comunicações, despacho e cadeias de suprimento operados por outros setores.

### 19.2 Três lentes

O **risco** (Capítulo 23) pergunta: o que poderia acontecer, com que probabilidade, com que gravidade, e quais controles o reduzem mais pelo dinheiro investido? A sua força é a priorização; a sua fraqueza é que eventos raros, novos ou em cascata são mal capturados por estimativas de probabilidade. A **resiliência** pergunta: quando a perturbação acontece — qualquer que seja a sua causa —, como o serviço a absorve, se adapta e se recupera? Haimes define a resiliência como a capacidade de suportar uma perturbação grave dentro de uma degradação aceitável e de se recuperar em tempo e custo aceitáveis ([Haimes, 2009](https://doi.org/10.1111/j.1539-6924.2009.01216.x)); Bruneau e colegas a mediram como a perda de qualidade do serviço ao longo do tempo ([Bruneau et al., 2003](https://doi.org/10.1193/1.1623497)). A orientação de engenharia de ciber-resiliência do NIST aplica essas ideias a sistemas ([SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1)). As visões de **safety e de sistemas** tratam os acidentes como resultado de um controle inadequado sobre componentes que interagem, e não de falhas isoladas ([Leveson, 2004](https://doi.org/10.1016/S0925-7535(03)00047-X)), e lembram que o erro humano costuma ser um sintoma do projeto do sistema ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)). Um analista competente usa as três: o risco para priorizar, a resiliência para se preparar para o que a análise de risco deixou escapar, o pensamento sistêmico para entender como organizações e tecnologia falham juntas.

### 19.3 O que é próprio da área

Cinco características se repetem entre os setores: **consequências físicas** (danos às pessoas e ao meio ambiente, e não só aos dados); **tecnologia de vida longa** (Capítulo 2); **interdependência** (Capítulo 22); **regulação e prestação de contas pública**; e **propriedade mista** — a maior parte da infraestrutura é operada de forma privada, mas a sociedade depende dela, então os incentivos para investir em proteção contra eventos raros são fracos. Essas características explicam por que "aplicar o manual da TI corporativa" falha e por que o conhecimento específico de cada setor importa.

Em Calder, essas características são concretas: o dano do CVH é físico (pacientes), as RTUs da CPN duram décadas, a subestação alimenta outros quatro serviços (Laboratório 3), cada operador responde ao seu próprio regulador, e a maioria são empresas privadas cuja falha prejudica moradores do condado que não são seus clientes.

### 19.4 Exemplo resolvido: o perfil do CEDC (sintético)

**Este caso é sintético.** Um perfil setorial do County Emergency Dispatch Centre: *função* — receber chamadas de emergência e despachar ambulâncias, bombeiros e polícia; *dano pela perda* — resposta atrasada em questão de minutos; *dependências* — telecomunicações (chamadas e dados do CAD), energia (UPS e gerador), serviços em nuvem do fornecedor do CAD, pessoal; *contexto regulatório* — deveres de serviço público e, dependendo da jurisdição, obrigações de cibersegurança para entidades essenciais (a verificar com a assessoria jurídica); *lentes* — risco: o ransomware no CAD é o principal cenário; resiliência: a contingência com papel e rádio precisa sustentar o despacho por horas; sistemas: uma passagem para o papel às 2 da manhã é um problema de fatores humanos tanto quanto técnico. O perfil ainda não diz o que fazer; ele diz quais perguntas importam.

### 19.5 Atividade prática

Escolha um setor real do seu país. A partir de fontes oficiais, descubra: quem o designa como crítico, qual lei ou framework define as suas obrigações de cibersegurança, qual órgão o supervisiona e qual orientação pública se aplica. Registre cada fonte com a sua data. Não suponha que o modelo da UE, dos EUA ou do Reino Unido se aplica em outros lugares.

Registre a jurisdição e a data de cada fonte, porque as definições mudam: a UE substituiu a sua diretiva anterior de segurança de redes pela NIS2, e as datas de transposição nacional diferem. Onde um framework só se aplica acima de um limiar de porte, anote o limiar e se o operador que você escolheu o atinge.

### 19.6 Erros comuns e limites

- Igualar "infraestrutura crítica" a "TO".
- Ler uma lista de setores como uma lista de setores independentes.
- Usar uma lente e ignorar o que as outras revelam.
- Declarar obrigações legais sem conferir o texto atual e a jurisdição.

O CEDC mostra o primeiro erro: uma central de despacho quase não tem TO e mesmo assim é crítica. O Laboratório 3 mostra o segundo: as entradas da subestação, das telecomunicações e da água dependem umas das outras. Usar só a lente do risco no CEDC deixaria escapar o problema da passagem para o papel às 2 da manhã. E o perfil do CEDC deixa deliberadamente as suas obrigações legais "a verificar com a assessoria jurídica".

### Exercícios — capítulo 19

**EX037 — Funções, não setores.** *Objetivo:* aplicar a visão por funções. *Entradas:* Calder Mutual. *Etapas:* nomeie duas funções críticas que ela sustenta, as suas dependências de outros setores e a linha do tempo do dano se cada uma parar. *Evidência esperada:* um perfil curto. *Rubrica:* 3 = funções como "prestar serviços de pagamento" e "dar acesso a dinheiro em espécie", dependências de energia/telecomunicações/outras infraestruturas financeiras, linha do tempo do dano (horas para pagamentos, dias para salários/benefícios); 2 = só no nível do setor; 1 = vago; 0 = nada.

**EX038 — Três lentes.** *Objetivo:* comparar teorias num caso. *Entradas:* a estação de tratamento da CW. *Etapas:* escreva uma pergunta que cada lente faria e uma coisa que cada uma poderia deixar escapar. *Evidência esperada:* três pares. *Rubrica:* 3 = risco (cenários prováveis; deixa escapar cascatas novas), resiliência (recuperação/modos degradados; pode subestimar a economia da prevenção), sistemas (estrutura de controle, fatores humanos/organizacionais; mais difícil de quantificar); 2 = duas lentes; 1 = uma; 0 = nada.

### Síntese do capítulo

Uma infraestrutura é crítica porque a sociedade depende das suas funções. As jurisdições a organizam de formas diferentes, por setores, funções e leis como a NIS2, a CER e o DORA. O risco, a resiliência e o pensamento sistêmico são lentes complementares, e as características próprias da área — consequência física, longevidade, interdependência, regulação e propriedade mista — explicam por que ela precisa da sua própria disciplina.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Continue estudando — capítulo 19 de 40

[← Capítulo 18](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Infraestrutura crítica e segurança setorial: casos fundadores

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) resumir seis casos públicos que moldaram a área a partir das suas fontes primárias ou autorizadas; (2) separar o que as fontes estabelecem do que é comumente repetido; (3) extrair lições transferíveis e compará-las entre setores; e (4) lidar honestamente com relatos revisados. O capítulo se apoia no Capítulo 19 e prepara o Capítulo 31 (casos avançados) e o trabalho de conclusão. Todas as descrições ficam no nível das fontes citadas; nenhum caso é ensinado como técnica.

### 20.1 Ler um caso

Para cada caso, registre: **data e setor**; **o que aconteceu com o serviço** (alcance, duração, pessoas afetadas); **acesso inicial e propagação**, só como a fonte descreve; **resposta**; **tipo de fonte** (alerta governamental, relatório de auditoria, análise revisada por pares, comunicado de empresa, jornalismo); e **o que continua incerto**. Os primeiros relatos muitas vezes estão errados; os relatos posteriores muitas vezes os corrigem. Um bom analista cita os dois.

Para Oldsmar, esse registro tem duas datas: o alerta de 2021 e a declaração de 2023 que o revisou. As duas pertencem ao registro, com o relato do alerta rotulado como superado, e não apagado.

### 20.2 Seis casos

**Distribuição de energia na Ucrânia, dezembro de 2015.** O alerta da CISA descreve ataques coordenados a três distribuidoras regionais que causaram interrupções afetando aproximadamente 225.000 clientes, com operação remota de disjuntores, destruição de alguns sistemas e perturbação das centrais de atendimento; a energia foi restabelecida passando para a operação manual ([CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01); ver também a [análise da E-ISAC/SANS](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and)). *Lição:* a contingência manual e uma equipe capaz de operar sem automação foram decisivas.

**WannaCry e o NHS, maio de 2017.** O National Audit Office do Reino Unido constatou que o ransomware perturbou pelo menos um terço dos NHS trusts da Inglaterra, levou ao cancelamento de consultas e ao desvio de ambulâncias, e que as organizações afetadas tinham sistemas Windows sem patches ou sem suporte; o NHS não tinha ensaiado uma resposta nacional ([NAO, 2017](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/)). *Lição:* um malware não direcionado pode causar dano clínico; a higiene básica e a coordenação ensaiada importam.

**TRITON/HatMan, 2017.** O relatório de análise de malware da CISA descreve um malware projetado para interagir com um controlador específico de sistema instrumentado de segurança, a camada destinada a evitar danos físicos ([CISA MAR-17-352-01](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf)). *Lição:* os sistemas de safety são alvos, e a sua independência das redes de controle precisa ser real.

**Tratamento de água em Oldsmar, fevereiro de 2021.** O alerta da CISA relatou que agentes não identificados acessaram o sistema de controle de uma estação de tratamento de água por meio de um software de acesso remoto e aumentaram o setpoint de hidróxido de sódio, o que um operador percebeu e reverteu ([CISA AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a)). Em 2023, um ex-administrador municipal disse que o evento provavelmente foi um erro de um funcionário, e não uma intrusão ([WUSF, 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)). *Lição:* qualquer que seja a causa, o acesso remoto não gerenciado e a dependência de um único operador atento eram fraquezas — e as narrativas públicas podem ser revisadas.

**Colonial Pipeline, maio de 2021.** O alerta conjunto da CISA e do FBI sobre o ransomware DarkSide relata que os agentes implantaram ransomware contra a rede de TI de uma empresa de oleodutos, que não havia indicação de que as suas redes de TO tivessem sido diretamente afetadas e que a empresa desconectou proativamente certos sistemas de TO para garantir a sua segurança ([CISA AA21-131A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a)). A retrospectiva de dois anos da CISA nomeia a empresa e relembra as filas por combustível ao longo da costa leste que se seguiram ([CISA, 2023](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years)). *Lição:* um comprometimento da TI pode parar as operações de TO por meio de dependências de negócio e de decisões preventivas, sem tocar no sistema de controle.

**Atualização da CrowdStrike, julho de 2024.** Uma atualização defeituosa de um software de segurança derrubou máquinas Windows no mundo inteiro; a Microsoft estimou que cerca de 8,5 milhões de dispositivos foram afetados, perturbando companhias aéreas, hospitais e bancos ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)). *Lição:* nenhum adversário é necessário; uma dependência de software compartilhada é um ponto único de falha entre setores.

### 20.3 Comparar os casos

| Caso | Causa | Efeito no setor | Lição transferível |
|---|---|---|---|
| Ucrânia 2015 | Ataque deliberado | Corte de energia | Capacidade de operação manual |
| WannaCry 2017 | Malware não direcionado | Perturbação clínica | Higiene, coordenação ensaiada |
| TRITON 2017 | Malware direcionado | Camada de safety ameaçada | Independência do sistema de safety |
| Oldsmar 2021 | Contestada | Quase acidente na dosagem química | Governança do acesso remoto; relatos revisados |
| Colonial 2021 | Ransomware na TI | Parada preventiva da TO | Dependência de negócio entre TI e TO |
| CrowdStrike 2024 | Atualização defeituosa | Interrupção entre setores | Concentração em dependências compartilhadas |

A tabela comprime cada caso numa lição para que eles possam ser comparados; ela não é um resumo do que aconteceu. Leia a coluna "Causa" de cima a baixo: dois dos seis não envolvem nenhum ataque direcionado ao sistema de controle.

### 20.4 Exemplo resolvido: lições para o CVH (aplicação sintética)

**A aplicação é sintética; os casos estão citados acima.** Para o Calder Valley Hospital, as lições transferíveis são: (1) ensaiar a operação sem TI (processos em papel, como os operadores ucranianos fizeram sem automação); (2) inventariar e isolar os dispositivos sem suporte (WannaCry); (3) confirmar que um comprometimento do BMS não consegue parar os controles locais de segurança da ventilação do centro cirúrgico (a lição do TRITON sobre camadas independentes); (4) governar o acesso remoto ao BMS (Oldsmar); (5) mapear quais processos clínicos dependem da TI de negócio, como a administração de pacientes (Colonial); e (6) planejar para a falha em massa de um produto de endpoint compartilhado (CrowdStrike).

### 20.5 Erros comuns e limites

- Repetir detalhes vívidos que nenhuma fonte primária sustenta.
- Citar o primeiro relato e ignorar a correção.
- Tratar todo caso como ataque.
- Transformar um estudo de caso numa receita de ataque.

Exemplos comuns: afirmar que Oldsmar foi "um hack" sem a revisão de 2023; repetir durações de interrupção que não estão na fonte citada; chamar a CrowdStrike de ataque; ou descrever as técnicas do Stuxnet quando a lição é a premissa que falhou. Cada um dos seis resumos aqui fica no nível que a sua fonte sustenta, e o EX039 pede que você confira um deles.

### Exercícios — capítulo 20

**EX039 — Conferência da fonte primária.** *Objetivo:* separar a fonte da repetição. *Entradas:* um dos seis casos deste capítulo. *Etapas:* leia a fonte citada e liste três fatos que ela declara, uma afirmação comumente repetida que ela não declara (encontre uma numa notícia ou num blog) e como você formularia o caso para um relatório. *Evidência esperada:* lista e formulação. *Rubrica:* 3 = fatos exatos com a sua localização na fonte, uma afirmação sem sustentação identificada, formulação cuidadosa; 2 = só os fatos; 1 = fatos de fontes secundárias; 0 = nada.

**EX040 — Lição entre setores.** *Objetivo:* transferir uma lição. *Entradas:* Colonial Pipeline. *Etapas:* aplique a sua lição à Calder Transit: quais sistemas de TI de negócio poderiam forçar uma parada preventiva das operações ferroviárias, e o que poderia evitar isso? *Evidência esperada:* duas dependências e duas medidas. *Rubrica:* 3 = por exemplo, bilhetagem/receita, escala de tripulações, informação aos passageiros; medidas como regras de operação degradada acordadas previamente e separar as dependências operacionais das de negócio; 2 = uma de cada; 1 = genérico; 0 = nada.

### Síntese do capítulo

Os casos fundadores da área ensinam pela comparação: contingência manual, higiene, independência do sistema de safety, governança do acesso remoto, dependência de negócio entre TI e TO e concentração em dependências compartilhadas. Leia as fontes primárias, mantenha as revisões à vista e transfira lições, e não técnicas.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Continue estudando — capítulo 20 de 40

[← Capítulo 19](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Capítulo 21 — Infraestrutura crítica e segurança setorial: modelos de sistema

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) descrever uma malha de controle e os componentes de um sistema SCADA ou de controle industrial; (2) situar os ativos num modelo de referência em camadas, dos dispositivos de campo à empresa; (3) modelar um serviço como uma cadeia de funções com modos degradados; e (4) dizer a que tipos de ataque ou falha cada parte do modelo está exposta. O capítulo se apoia nos Capítulos 7, 16 e 19 e prepara o Capítulo 22 (dados e dependências) e o Capítulo 28 (análise de falhas).

### 21.1 A malha de controle

Todo processo físico controlado por computadores segue uma malha: um **sensor** mede (nível de reservatório, corrente de linha, posição do trem); um **controlador** compara a medição com um **setpoint** e calcula uma ação; um **atuador** age (velocidade da bomba, disparo do disjuntor, aspecto do sinal); o processo responde; o sensor mede de novo. Os **controladores lógicos programáveis** (PLCs) e as **unidades terminais remotas** (RTUs) rodam a malha localmente. Um sistema **SCADA** (supervisão e aquisição de dados) supervisiona muitas malhas numa área ampla: coleta as medições, mostra-as aos operadores em **interfaces homem–máquina** (IHMs), guarda o histórico num **historiador** e envia setpoints e comandos. Os **sistemas instrumentados de segurança** (SIS) vigiam condições perigosas e agem de forma independente para levar o processo a um estado seguro ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

A malha dá um vocabulário preciso para o que pode dar errado: **medições** falsas (o controlador age sobre uma mentira), **comandos** falsos (o atuador faz algo não pretendido), perda de **visão** (os operadores não conseguem ver), perda de **controle** (os operadores não conseguem agir) e comprometimento da **proteção** (o SIS não consegue agir). O MITRE ATT&CK for ICS organiza os impactos em termos semelhantes, como perda de visão, perda de controle e manipulação do controle ([ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)).

### 21.2 Um modelo de referência em camadas

Um modelo em camadas — amplamente conhecido como modelo de Purdue — situa os ativos por função: nível 0, o processo físico com sensores e atuadores; nível 1, o controle básico (PLCs, RTUs, SIS); nível 2, o controle supervisório (IHMs, SCADA local); nível 3, as operações do site (historiadores, estações de engenharia); uma DMZ; e os níveis 4–5, a TI corporativa. O modelo é um auxílio didático e de segmentação, e não uma lei da natureza: sensores conectados à nuvem, serviços remotos de fornecedores e dispositivos de campo sem fio atravessam os níveis. Use-o para perguntar "quais caminhos atravessam os níveis, e eles são controlados?"

### 21.3 Cadeias de serviço e modos degradados

Os operadores se importam com serviços, e não com níveis. Modele um serviço como uma cadeia de funções com **modos degradados**: o "fornecer água segura" da Calder Water = captar água bruta → tratar → monitorar a qualidade → armazenar → bombear → distribuir. Cada função tem estados normal, degradado e falho. "Monitorar a qualidade" degradado pode significar amostragem manual a cada hora em vez de analisadores contínuos; "bombear" degradado pode significar controle local pela equipe na estação, sem SCADA. Um modelo de serviço que inclui os modos degradados mostra por quanto tempo o serviço consegue continuar quando a automação é perdida — a pergunta que os operadores ucranianos responderam em 2015 (Capítulo 20).

### 21.4 Exemplo resolvido: restabelecimento de alimentador da CPN (sintético)

**Este caso é sintético.** O serviço da Calder Power Networks "restabelecer o fornecimento depois de uma falta num alimentador": um relé de proteção desliga o trecho com falta (nível 1, independente do SCADA); a RTU informa o desligamento (nível 1→2); o operador o vê na IHM (nível 2) e religa ou reconfigura remotamente (nível 2→1); os clientes são informados pelo sistema de interrupções (nível 4). Análise de falhas por elemento: se o relé falhar, a falta persiste — questão de safety; se o enlace da RTU falhar, os operadores perdem a visão desse alimentador — modo degradado: despachar uma equipe; se a IHM for comprometida, um estado falso poderia levar os operadores a energizar uma linha em que há equipes trabalhando — questão de safety que os procedimentos (bloqueios, permissões de trabalho, confirmação verbal) precisam pegar; se o sistema de interrupções falhar, os clientes não são informados — uma questão de qualidade do serviço. O modelo mostra que as consequências mais graves ficam onde a manipulação cibernética encontra os procedimentos de segurança humana.

### 21.5 Atividade prática

Desenhe a malha de controle e o modelo em camadas de um serviço de Calder que não seja água nem energia (sinalização ferroviária ou ventilação do centro cirúrgico do hospital). Rotule cada componente com o seu nível, qual de visão/controle/proteção ele sustenta e um modo degradado.

Para a ventilação do centro cirúrgico, o sensor pode ser um sensor de pressão no duto ou de trocas de ar no nível 0, o controlador do BMS no nível 1, a estação da manutenção predial no nível 2 e o servidor do BMS no nível 3. Um modo degradado é o controle manual local das unidades de tratamento de ar. Marque qual componente sustenta visão, controle ou proteção; um intertravamento de vazão mínima por fiação, se existir, é proteção.

### 21.6 Erros comuns e limites

- Tratar o modelo em camadas como uma descrição do tráfego real.
- Ignorar os sistemas de safety ou supor que eles são sempre independentes.
- Modelar os ativos sem o serviço que eles sustentam.
- Supor que a perda do SCADA significa a perda do serviço.

O modelo de alimentador da CPN mostra os dois primeiros: o relé fica no nível 1 e age sem o SCADA, mas, se estivesse em rede com a IHM, a sua independência precisaria de evidência. O terceiro erro listaria as RTUs sem dizer que elas servem ao restabelecimento dos alimentadores. O quarto ignora o modo degradado de despachar uma equipe quando um enlace de RTU falha.

### Exercícios — capítulo 21

**EX041 — Nomeie a perda.** *Objetivo:* usar o vocabulário da malha. *Entradas:* (a) uma indisponibilidade do historiador; (b) uma IHM mostrando valores congelados; (c) um setpoint forjado aceito por um PLC; (d) um disparo do SIS desativado. *Etapas:* classifique cada um como perda de visão, perda de controle, manipulação ou perda de proteção, e declare o risco imediato. *Evidência esperada:* quatro classificações. *Rubrica:* 3 = (a) perda da visão histórica, baixo risco imediato; (b) perda de visão, perigosa porque os operadores podem agir sobre dados velhos; (c) manipulação do controle; (d) perda de proteção, gravidade máxima; 2 = uma errada; 1 = duas erradas; 0 = nada.

**EX042 — Modos degradados.** *Objetivo:* modelar a continuidade sem automação. *Entradas:* o "operar um serviço ferroviário seguro" da Calder Transit. *Etapas:* escreva a cadeia de funções e um modo degradado para três funções, com a restrição que cada um impõe (por exemplo, frequência reduzida). *Evidência esperada:* cadeia e modos. *Rubrica:* 3 = cadeia sensata (sinalização, controle de trens, comunicação com a tripulação, informação aos passageiros, bilhetagem) com modos degradados e restrições realistas; 2 = cadeia sem restrições; 1 = vago; 0 = nada.

### Síntese do capítulo

Os sistemas de controle são malhas de medir, decidir e agir, supervisionadas pelo SCADA e protegidas por sistemas de safety independentes. Os modelos em camadas ajudam a segmentar; as cadeias de serviço com modos degradados mostram por quanto tempo um serviço sobrevive sem automação. As piores consequências surgem onde a manipulação encontra a safety e os procedimentos humanos.

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Continue estudando — capítulo 21 de 40

[← Capítulo 20](#ch-20) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 22 →](#ch-22)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-22"></a>

## Capítulo 22 — Infraestrutura crítica e segurança setorial: dados e dependências

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) construir e manter um inventário de ativos e dependências a partir de várias fontes imperfeitas; (2) acrescentar o tempo a um modelo de dependências usando a autonomia da reserva; (3) calcular quais serviços se perdem em interrupções de durações diferentes e identificar os elos fracos; e (4) declarar os limites de qualidade de dados desses modelos. O capítulo se apoia nos Capítulos 6, 9 e 21 e prepara o Capítulo 23 (métodos de risco) e o Capítulo 28 (análise de falhas).

### 22.1 O inventário é evidência, não uma lista

Nenhuma organização sabe exatamente o que tem. Os dados de ativos vêm de registros de compras, de observações da rede, de bancos de dados de configuração, da documentação dos fornecedores e de percorrer o local; cada fonte deixa escapar algo. Trate o inventário como evidência com fontes e datas (Capítulo 15): para cada ativo, registre quem o confirmou e quando. A observação **passiva** da rede encontra os dispositivos que se comunicam; ela deixa escapar os dispositivos ociosos e seriais. A varredura **ativa** encontra mais, mas pode perturbar dispositivos frágeis de TO e só pode ser feita sob autorização e com o acordo da operação (Capítulo 10). As dependências são ainda mais difíceis: vivem na cabeça das pessoas, nos contratos e em hábitos não escritos.

### 22.2 Tipos de dependência

Rinaldi e colegas distinguem as interdependências **físicas** (energia para as bombas), **cibernéticas** (telemetria pelas telecomunicações), **geográficas** (cabos na mesma vala) e **lógicas** (laços financeiros ou regulatórios) ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131)). Acrescente as **pessoas** (um engenheiro que conhece o sistema legado) e os **fornecedores** (um único fornecedor de CAD, uma região de nuvem). O grafo do Capítulo 6 mostrou *o que pode ser afetado*; o tempo o transforma em *o que será perdido quando*. Cada serviço tem uma **autonomia**: por quanto tempo ele continua com a sua própria reserva — baterias, geradores e combustível, água armazenada, processos em papel.

### 22.3 Exemplo resolvido e Laboratório 9 (sintético)

**Este caso é sintético.** A CRP coletou a autonomia de reserva dos principais serviços durante uma interrupção regional da rede elétrica. Os pagamentos com cartão dependem da central de telecomunicações A, que só tem baterias; a central B também tem um gerador.

```python
# Lab 9 - which services survive a grid outage of a given length? (synthetic backup autonomy, offline)
AUTONOMY_H = {  # hours each service keeps running on its own backup
    "hospital (generator, fuel on site)": 72, "telecom exchange A (batteries)": 4,
    "telecom exchange B (batteries + generator)": 48, "water pumps (no generator)": 0,
    "water treated storage": 10, "dispatch centre (UPS + generator)": 24,
    "card payments (relies on telecom)": None, "rail signalling (UPS)": 2,
}
for outage in (1, 6, 30):
    down = []
    for s, h in AUTONOMY_H.items():
        if h is None:   # dependent service: fails when 4-h exchange A fails
            h = AUTONOMY_H["telecom exchange A (batteries)"]
        if h < outage: down.append(s.split(" (")[0])
    print(f"outage {outage:>2} h -> {len(down)} services lost: {', '.join(down) or 'none'}")
```

Saída esperada:

```text
outage  1 h -> 1 services lost: water pumps
outage  6 h -> 4 services lost: telecom exchange A, water pumps, card payments, rail signalling
outage 30 h -> 6 services lost: telecom exchange A, water pumps, water treated storage, dispatch centre, card payments, rail signalling
```

Interpretação: as autonomias mais curtas definem o início da história — as bombas param de imediato (os consumidores ainda recebem água armazenada por cerca de 10 horas), a sinalização ferroviária para depois de 2 horas, e os pagamentos com cartão falham depois de 4 horas porque a central A não tem gerador. Em 30 horas, o abastecimento de água e o despacho estão perdidos. As 72 horas do hospital parecem tranquilizadoras, mas a sua água chega de um armazenamento que dura 10 horas: um prédio pode ter energia e mesmo assim estar inutilizável. O modelo é rudimentar — ignora as dependências das próprias reservas (quem reabastece o gerador do despacho depois de 24 horas, e por quais estradas?) —, mas já identifica três perguntas baratas: a central A pode receber um gerador; as bombas de água podem receber um ponto de conexão para gerador móvel; e quais acordos de entrega de combustível existem entre os operadores?

### 22.4 Qualidade dos dados

Cada número acima é uma afirmação de um operador. A autonomia de um gerador depende do combustível que de fato está no tanque, da confiabilidade da partida (Capítulo 12, EX024) e da carga. A autonomia das baterias se degrada com a idade. Registre a evidência por trás de cada autonomia — um teste, um valor de projeto, uma estimativa — e rode o modelo com valores pessimistas. Um modelo de dependências só é tão bom quanto o seu número menos conferido.

No Laboratório 9, reduzir à metade todas as autonomias (EX043) leva o armazenamento de água tratada para a lista de perdas de 6 horas.

Para o gerador do CEDC, a evidência seria a data do último teste de carga e o nível de combustível no dia do levantamento.

### 22.5 Erros comuns e limites

- Tratar uma única fonte de inventário como completa.
- Registrar as dependências sem o tempo.
- Tirar os números de autonomia de documentos de projeto sem testes.
- Esquecer as dependências de segunda ordem das reservas (combustível, pessoal, estradas).
- Varredura ativa da TO sem autorização e sem acordo operacional.

O Laboratório 9 ilustra os três primeiros: uma autonomia de projeto de 72 horas para o hospital supõe um tanque cheio, e as 4 horas da central A supõem baterias saudáveis. O quarto é a pergunta do reabastecimento por trás das 24 horas da central de despacho. O quinto é o motivo de o inventário da CRP ter se apoiado na observação passiva e nas declarações dos operadores, em vez de varreduras.

### Exercícios — capítulo 22

**EX043 — Corrija o elo fraco.** *Objetivo:* testar uma intervenção. *Entradas:* Laboratório 9. *Etapas:* dê aos pagamentos com cartão a autonomia da central B (48 h) e rode de novo. Depois reduza à metade todas as autonomias (caso pessimista) e rode de novo para 6 h. Reporte as duas e recomende. *Evidência esperada:* duas saídas e uma recomendação. *Rubrica:* 3 = os pagamentos com cartão sobrevivem até 48 h na primeira rodada; a rodada pessimista de 6 h perde a central de telecomunicações A, as bombas de água, o armazenamento de água tratada, os pagamentos com cartão e a sinalização ferroviária (5 serviços); a recomendação trata da evidência para os números de autonomia; 2 = rodadas sem recomendação; 1 = uma rodada; 0 = nada.

**EX044 — Dependências de segunda ordem.** *Objetivo:* olhar por trás das reservas. *Entradas:* o gerador de 24 horas da central de despacho. *Etapas:* liste quatro dependências dessa própria reserva e uma forma de evidenciar cada uma. *Evidência esperada:* lista. *Rubrica:* 3 = contrato de fornecimento de combustível e rota de entrega, pessoal para operar/reabastecer, confiabilidade da partida do gerador (registros de teste), resfriamento/ventilação ou quadro de manobra; cada um com evidência; 2 = três; 1 = uma ou duas; 0 = nada.

### Síntese do capítulo

Os inventários e os mapas de dependências são evidências com fontes, datas e lacunas. Acrescentar o tempo — a autonomia da reserva — transforma a exposição numa linha do tempo de perdas, expõe elos fracos como uma central só com baterias e revela que um prédio com energia ainda pode estar inutilizável. Teste as afirmações de autonomia e olhe por trás de cada reserva para as suas próprias dependências.

<!-- cyberabc:chapter-navigation:start ch-22 -->
### Continue estudando — capítulo 22 de 40

[← Capítulo 21](#ch-21) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 23 →](#ch-23)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-23"></a>

## Capítulo 23 — Infraestrutura crítica e segurança setorial: métodos I

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) realizar uma avaliação de risco estruturada seguindo as etapas do NIST SP 800-30; (2) explicar as fraquezas das matrizes de risco; (3) aplicar uma abordagem que começa pela consequência, partindo dos piores efeitos sobre o serviço; e (4) comparar as duas abordagens num caso e dizer quando cada uma é apropriada. O capítulo se apoia nos Capítulos 1, 12, 15 e 19–22 e prepara o Capítulo 24 (controles) e o Capítulo 26 (métodos II).

### 23.1 Uma avaliação de risco estruturada

O NIST SP 800-30 descreve a avaliação de risco em etapas: **preparar** (finalidade, escopo, premissas, fontes); **conduzir** (identificar as fontes e os eventos de ameaça, as vulnerabilidades e as condições predisponentes, determinar a probabilidade e o impacto, determinar o risco); **comunicar** os resultados; e **manter** a avaliação à medida que as coisas mudam ([SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)). A força do método é a disciplina: ele obriga você a escrever o escopo e as premissas e a dizer de onde veio cada julgamento. Os seus resultados costumam ser classificações qualitativas (de muito baixo a muito alto) em escalas que a organização define.

### 23.2 O problema das matrizes

Muitas organizações combinam as classificações de probabilidade e impacto numa **matriz de risco** 5×5. As matrizes são fáceis de comunicar, mas têm problemas conhecidos. Rótulos ordinais ("3 = possível") são multiplicados como se fossem números. Riscos muito diferentes recebem a mesma célula. Eventos raros e catastróficos caem na mesma cor que eventos frequentes e menores. As classificações dependem muito de quem está na sala. O hábito do Capítulo 1 ajuda: sempre que possível, ponha quantidades aproximadas por trás dos rótulos (uma faixa de probabilidade anual, uma duração de interrupção, um dano) e mostre a pior consequência crível separada da classificação.

### 23.3 Consequência primeiro

Nos serviços críticos, a probabilidade é muitas vezes a entrada menos conhecível: os adversários se adaptam, e os eventos que mais importam são raros. Uma abordagem de **consequência primeiro** começa pela outra ponta: identifique os desfechos que não podem acontecer (perda do abastecimento de água do hospital por mais de 8 horas; dosagem de cloro descontrolada), rastreie quais funções e sistemas poderiam causá-los e pergunte o que um adversário ou uma falha precisaria alcançar para cada um. A **Consequence-driven Cyber-informed Engineering** (CCE) do Idaho National Laboratory formaliza isso: identificar os eventos de alta consequência, mapear os sistemas envolvidos, iluminar os caminhos que um adversário tomaria e mitigar — de preferência com mudanças de engenharia que eliminem a possibilidade, em vez de detectá-la ([INL CCE](https://inl.gov/national-security/cce/)). A ISA/IEC 62443-3-2 também baseia a sua avaliação de risco para o projeto de sistemas em zonas, conduítes e consequências ([página de catálogo da IEC 62443-3-2](https://webstore.iec.ch/en/publication/30727)).

### 23.4 Exemplo resolvido: a dosagem de cloro na CW (sintético)

**Este caso é sintético.** *Visão da matriz de risco:* a ameaça "alteração não autorizada do setpoint de dosagem de cloro" recebe probabilidade 2 (improvável) e impacto 5 (grave) = 10, âmbar. O registro diz "monitorar". *Visão de consequência primeiro:* o desfecho inaceitável é "água saindo da estação com cloro fora dos limites seguros por tempo suficiente para prejudicar os consumidores". Caminhos: uma alteração de setpoint a partir da IHM (erro do operador ou comprometimento); um comando forjado para o PLC de dosagem pela rede de controle; um sensor informando um cloro residual falso, de modo que o controlador dose demais; um notebook de fornecedor conectado ao PLC. Mitigações de engenharia que não dependem de detectar o atacante: uma vazão máxima da bomba dosadora limitada por fiação; um analisador independente de cloro residual na saída que fecha a válvula de saída por um circuito separado; uma chave física para o modo de programação do PLC. A matriz dizia "monitorar"; a análise de consequências produziu três mudanças concretas, uma das quais (o limite físico) elimina o desfecho mais perigoso, não importa como o atacante tenha entrado.

### 23.5 Atividade prática

Pegue a sinalização do VLT da Calder Transit. Escreva uma consequência inaceitável, três caminhos até ela (pelo menos um não malicioso) e uma mitigação de engenharia que elimine ou limite a consequência. Depois classifique o mesmo cenário numa matriz 5×5 e compare o que cada abordagem lhe disse.

Para a sinalização, uma consequência inaceitável pode ser "dois trens autorizados no mesmo bloco". Os caminhos incluem uma configuração corrompida do intertravamento depois de uma manutenção (não malicioso), um comando forjado a partir de uma estação de controle comprometida e um circuito de via com falha lido como livre. Uma mitigação de engenharia é a própria lógica de segurança do intertravamento, independente da estação de controle. Numa matriz 5×5, o mesmo cenário pode receber 5 de impacto e 1 de probabilidade, dando uma célula que o subestima.

### 23.6 Erros comuns e limites

- Multiplicar rótulos ordinais como se fossem medições.
- Classificar a probabilidade de ações novas de adversários com falsa confiança.
- Tratar "monitorar" como mitigação.
- Uma análise de consequência primeiro que só lista consequências e nunca mapeia caminhos nem mitigações.
- Ignorar os caminhos não maliciosos até a mesma consequência.

O exemplo do cloro mostra diretamente o terceiro erro: o resultado "monitorar" da matriz deixou possível o desfecho perigoso. O primeiro erro produziu a sua nota de 10. A análise de consequências evitou o quarto ao nomear caminhos e mitigações, e o quinto ao listar o erro do operador e as leituras falsas de sensor como caminhos ao lado do comprometimento.

### Exercícios — capítulo 23

**EX045 — Mesma célula, risco diferente.** *Objetivo:* expor os limites da matriz. *Entradas:* risco A: probabilidade 5, impacto 2 (interrupções diárias incômodas do Wi-Fi da equipe); risco B: probabilidade 2, impacto 5 (perda da ventilação do centro cirúrgico do CVH). *Etapas:* calcule as duas notas da matriz, explique por que a nota igual engana e proponha como apresentá-los no lugar disso. *Evidência esperada:* notas e explicação. *Rubrica:* 3 = ambas 10; explica o mau uso dos ordinais e a natureza diferente do dano; propõe uma coluna separada de pior consequência crível ou faixas quantitativas; 2 = parcial; 1 = só as notas; 0 = nada.

**EX046 — Consequência primeiro.** *Objetivo:* aplicar o método. *Entradas:* o switch de pagamentos da Calder Mutual. *Etapas:* defina uma consequência inaceitável, mapeie três caminhos e dê uma mitigação de engenharia e uma procedimental. *Evidência esperada:* a análise. *Rubrica:* 3 = consequência específica (por exemplo, transferências fraudulentas de alto valor liberadas, ou pagamentos indisponíveis por > 4 h no dia do salário), caminhos plausíveis incluindo insider/erro, mitigação de engenharia (limites rígidos de transação, confirmação fora de banda) e uma procedimental; 2 = genérico; 1 = só a consequência; 0 = nada.

### Síntese do capítulo

A avaliação de risco estruturada traz disciplina ao escopo, às premissas e ao julgamento; as matrizes de risco simplificam a comunicação, mas distorcem as comparações. Os métodos de consequência primeiro, como a CCE, partem do que não pode acontecer e preferem mitigações de engenharia que limitam o dano, não importa quem seja o atacante. Use os dois e diga qual deles orienta cada recomendação.

<!-- cyberabc:chapter-navigation:start ch-23 -->
### Continue estudando — capítulo 23 de 40

[← Capítulo 22](#ch-22) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 24 →](#ch-24)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-24"></a>

## Capítulo 24 — Infraestrutura crítica e segurança setorial: controles

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) usar um framework — o NIST CSF 2.0, o CAF do Reino Unido ou metas setoriais — para organizar os controles; (2) classificar os controles por tipo (preventivo, detectivo, corretivo) e natureza (técnico, procedimental, físico, de engenharia); (3) mapear os controles aos cenários e às técnicas que eles tratam e encontrar lacunas; e (4) escolher controles adequados às restrições da TO. O capítulo se apoia nos Capítulos 16 e 23 e prepara o Laboratório I (Capítulo 25) e o Capítulo 27 (verificação).

### 24.1 Frameworks como organizadores

Um **framework** organiza os resultados para que nada grande seja esquecido. O Cybersecurity Framework 2.0 do NIST agrupa os resultados em seis funções: Govern, Identify, Protect, Detect, Respond e Recover (governar, identificar, proteger, detectar, responder e recuperar) ([NIST CSF 2.0](https://www.nist.gov/cyberframework)). O CAF do Reino Unido expressa resultados e indicadores de boas práticas para os operadores de serviços essenciais ([NCSC CAF](https://www.ncsc.gov.uk/collection/caf)). Também existem metas específicas de setor — por exemplo, as metas de desempenho em cibersegurança para a saúde do Department of Health and Human Services dos EUA ([HHS HPH CPGs](https://hphcyber.hhs.gov/performance-goals.html)). Os catálogos detalhados de controles, como o NIST SP 800-53, listam controles específicos ([SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)). Os frameworks dizem *quais resultados* alcançar; eles não dizem qual risco importa mais para o seu serviço — isso vem do Capítulo 23.

### 24.2 Tipos de controle

Os controles **preventivos** impedem um evento (allowlist, autenticação, um limite por fiação). Os controles **detectivos** o percebem (monitoramento, verificações de integridade, alarmes). Os controles **corretivos** ou de **recuperação** restauram o serviço (backups, procedimentos manuais, equipamentos sobressalentes). Quanto à natureza, os controles são **técnicos**, **procedimentais** (aprovação por duas pessoas, gestão de mudanças), **físicos** (armários trancados, chaves físicas) ou **de engenharia** (projetos que tornam impossível um estado danoso, como uma bomba dimensionada para não conseguir dosar demais). Na TO, os controles de engenharia e físicos costumam ser os mais confiáveis, porque continuam funcionando quando os computadores são comprometidos.

### 24.3 Mapeamento e lacunas

Um controle só tem valor contra alguma coisa. Construa um **mapeamento** dos cenários (ou das técnicas catalogadas, por exemplo do [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)) para os controles, com cada controle marcado como preventivo, detectivo ou corretivo. As lacunas aparecem como cenários só com controles detectivos (você vai saber, mas não vai impedir), sem controle corretivo (você não consegue se recuperar) ou cobertos apenas por controles que compartilham um ponto único de falha (o modo comum do Capítulo 16). O mapeamento também expõe os **controles órfãos**, que não tratam nada da sua lista — candidatos a revisão.

### 24.4 Restrições da TO

Alguns controles padrão na TI são arriscados ou impossíveis na TO: agentes de endpoint que consomem os recursos do controlador, aplicação automática de patches, varredura ativa, bloqueio de conta numa IHM de operador durante uma emergência (bloquear o operador pode ser mais perigoso que o atacante). As alternativas incluem o monitoramento passivo da rede, a allowlist de aplicações em estações de trabalho estáveis, diodos de dados só de leitura para fluxos de mão única, chaves físicas para os modos de programação e controles procedimentais ligados ao livro de turno do operador.

O mapa do BMS do CVH os aplica: monitoramento passivo da VLAN do BMS em vez de agentes no controlador, e um intertravamento de vazão mínima por fiação para a ventilação do centro cirúrgico, em vez de depender de bloqueio ou de patches.

### 24.5 Exemplo resolvido: mapa de controles do BMS do CVH (sintético)

**Este caso é sintético.**

| Cenário | Preventivo | Detectivo | Corretivo | Lacuna |
|---|---|---|---|---|
| Comprometimento remoto do BMS pela rede corporativa | Allowlist no firewall para o servidor do BMS; MFA para a administração do BMS | Monitoramento passivo da VLAN do BMS | Controle manual local das unidades de tratamento de ar | Nenhuma óbvia; verificar o exercício de controle manual |
| Alteração maliciosa ou equivocada dos setpoints de ventilação do centro cirúrgico | Direitos de alteração baseados em papéis | Alarme de trocas de ar fora da faixa | O plantão da manutenção predial restaura os setpoints | Nenhum limite independente: acrescentar um intertravamento de vazão mínima por fiação |
| Notebook de fornecedor no controlador do BMS | Armários trancados; acompanhamento do fornecedor | — | Restaurar a configuração do controlador a partir do backup | Sem detecção; backup da configuração não testado |

O mapa transforma um vago "o BMS é um risco" em duas ações específicas: um intertravamento de engenharia e uma restauração de configuração testada.

### 24.6 Erros comuns e limites

- Tratar o preenchimento de um framework como redução de risco.
- Contar controles em vez de mapeá-los aos cenários.
- Depender só da detecção para consequências que precisam de prevenção.
- Importar controles de TI para a TO sem considerar a segurança operacional.

O mapa do BMS do CVH evita cada um: não conta controles, mapeia-os a três cenários, acrescenta um intertravamento de engenharia onde só havia detecção e rejeita controles de TI como a aplicação automática de patches no controlador do BMS. Uma nota de framework de "Protect: implementado" não teria dito nada ao hospital sobre a vazão de ar do centro cirúrgico.

### Exercícios — capítulo 24

**EX047 — Classifique os controles.** *Objetivo:* usar tipo e natureza. *Entradas:* backups offline; aprovação de pagamentos por duas pessoas; analisador de cloro na saída que fecha uma válvula; alerta do SIEM sobre novas contas de administrador; chave física para a programação do PLC. *Etapas:* classifique cada um por tipo e natureza. *Evidência esperada:* tabela. *Rubrica:* 3 = backups corretivo/técnico; aprovação por duas pessoas preventivo/procedimental; disparo do analisador preventivo (limita a consequência)/de engenharia; alerta do SIEM detectivo/técnico; chave física preventivo/físico; 2 = um erro; 1 = dois erros; 0 = nada.

**EX048 — Encontre a lacuna.** *Objetivo:* mapear e julgar. *Entradas:* a tabela do CVH. *Etapas:* acrescente um cenário (ransomware no servidor do BMS) com controles em cada coluna e depois nomeie a melhoria isolada mais valiosa e justifique-a. *Evidência esperada:* linha e justificativa. *Rubrica:* 3 = controles plausíveis, incluindo restauração testada e controle manual local; melhoria justificada pela consequência; 2 = linha sem justificativa; 1 = linha incompleta; 0 = nada.

### Síntese do capítulo

Os frameworks organizam os resultados; a análise de risco decide as prioridades; os mapeamentos ligam os controles aos cenários que eles tratam e revelam as lacunas. Prefira combinações de prevenção, detecção e recuperação e, na TO, favoreça os controles de engenharia e físicos, que continuam funcionando quando os computadores não funcionam.

<!-- cyberabc:chapter-navigation:start ch-24 -->
### Continue estudando — capítulo 24 de 40

[← Capítulo 23](#ch-23) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 25 →](#ch-25)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-25"></a>

## Capítulo 25 — Laboratório I

### Objetivos de aprendizagem e conexão

Depois deste laboratório, você consegue (1) combinar evidências de inventário, de fluxos de rede, de vulnerabilidades e de acessos numa única avaliação de um operador sintético; (2) registrar métodos, versões e saídas de modo que outra pessoa consiga reproduzir os seus resultados; (3) separar constatações, interpretações e recomendações; e (4) avaliar o seu próprio trabalho contra uma rubrica. O laboratório integra os Laboratórios 2, 4, 5 e 7 (Capítulos 3, 7, 9 e 13) e os métodos dos Capítulos 15, 23 e 24. É o primeiro ponto de controle de projeto do curso.

### 25.1 Finalidade e regras

Este laboratório é uma avaliação contida dos operadores **sintéticos** de Calder usando apenas os laboratórios offline do livro. As suas regras de engajamento (Capítulo 10, atividade prática) se aplicam: o seu próprio computador, nenhum acesso de rede a sistemas reais, nenhum dado real. A habilidade avaliada não é rodar código — essa é a parte fácil —, e sim **reunir evidências num julgamento defensável** e documentá-lo de modo que outro estudante consiga reproduzi-lo.

As condições de parada dessas regras também se aplicam aqui: se algum script de laboratório de Calder tentar acessar a rede, pare, registre o hash do script e avise o seu tutor.

### 25.2 A tarefa

Você é estagiário da County Resilience Partnership. Produza uma **nota de avaliação** de 1.500 palavras respondendo: "Considerando as evidências disponíveis, quais são as três melhorias de segurança de maior prioridade para os operadores de Calder, e quão confiantes estamos?" Use:

1. **Laboratório 2** (inventário do CVH): dispositivos sem suporte e fora do lugar.
2. **Laboratório 4** (fluxos da CW): violações da política de conduítes.
3. **Laboratório 5** (alertas da CPN): ativos vulneráveis, ordenados por exploração e exposição.
4. **Laboratório 7** (revisão de acessos): contas órfãs, inativas, compartilhadas e tóxicas.

A pergunta pede três prioridades entre quatro operadores, o que obriga à comparação: uma violação de conduíte na CW e uma falha no gateway da CPN precisam ser ordenadas uma contra a outra pela consequência, e não reportadas em listas separadas.

### 25.3 Método e reprodutibilidade

Registre para cada laboratório: o nome do arquivo e um hash SHA-256 do script que você rodou (`python3 -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" lab05.py`), a versão do Python, a saída exata e qualquer mudança que você tenha feito. A reprodutibilidade é evidência: um leitor que roda o seu script de novo e obtém a mesma saída pode confiar na sua seção de constatações sem precisar confiar em você ([Sandve et al., 2013](https://doi.org/10.1371/journal.pcbi.1003285)).

Se você mudou a lista de versões do Laboratório 5 para testar o VPN-01 contra outra versão de correção, o hash no seu apêndice precisa ser o desse arquivo editado, com a mudança listada ao lado.

### 25.4 Estrutura da nota

1. **Resumo** — três prioridades, uma frase cada, com a confiança (alta/média/baixa) e o motivo.
2. **Escopo e método** — o que foi examinado, como, e o que não foi.
3. **Constatações** — só fatos das saídas (por exemplo, "o VPN-01 roda a 9.1; a correção é a 9.3; o alerta declara exploração").
4. **Análise** — raciocínio de consequência primeiro (Capítulo 23): quais constatações poderiam levar aos piores desfechos para qual serviço.
5. **Recomendações** — cada uma ligada às constatações, com o tipo de controle (Capítulo 24) e o dono.
6. **Limites** — tamanho da amostra, dados sintéticos, afirmações não verificadas.
7. **Apêndice** — hashes, versões, saídas.

"O VPN-01 roda a 9.1; a correção é a 9.3" pertence às constatações; "então o acesso remoto da CPN é a prioridade 1" pertence à análise, onde o raciocínio sobre a consequência pode ser contestado separadamente.

### 25.5 Exemplo resolvido: uma prioridade, totalmente argumentada (sintético)

**Prioridade 1 — atualizar e redesenhar o acesso remoto da CPN (confiança: alta).** *Constatação:* o VPN-01 (exposto à internet) roda uma versão mais antiga que a correção de uma falha crítica e explorada (Laboratório 5). *Constatação:* o projeto original põe os usuários remotos diretamente na rede de controle (Capítulo 16). *Análise:* este é o caminho mais curto da internet até o controle dos alimentadores; a consequência é a perda de controle da distribuição, o desfecho mais grave no modelo de serviço da CPN (Capítulo 21). *Recomendação:* atualização emergencial para a 9.3 (corretivo/técnico; dono: líder de infraestrutura da CPN, nesta semana) e, depois, terminar o acesso remoto num jump host na DMZ com aprovação por sessão para fornecedores (preventivo/técnico e procedimental; dono: segurança de TO da CPN, no próximo trimestre). *Confiança:* alta, porque a constatação vem diretamente dos dados de versão e do alerta, e a consequência decorre da arquitetura. *Limite:* o laboratório não consegue mostrar se a falha já foi explorada; recomenda-se uma avaliação de comprometimento do VPN-01.

### 25.6 Rubrica de avaliação

| Critério | 3 (forte) | 2 | 1 | 0 |
|---|---|---|---|---|
| Uso de evidências | Toda constatação rastreável até uma saída de laboratório | Majoritariamente rastreável | Algumas afirmações sem sustentação | Nenhuma evidência |
| Priorização | Consequência primeiro, comparada entre operadores | Fundamentada dentro de cada operador | Ordenada só por rótulos de severidade | Nenhuma |
| Recomendações | Ligadas às constatações, tipificadas, com dono e data | Ligadas, sem donos | Genéricas | Nenhuma |
| Limites e confiança | Específicos e honestos | Genéricos | Simbólicos | Ausentes |
| Reprodutibilidade | Hashes, versões, saídas | Só as saídas | Parcial | Nenhuma |

A rubrica recompensa os mesmos hábitos da prioridade resolvida: toda constatação rastreada até uma saída, consequências comparadas entre operadores, donos e datas nas recomendações, limites honestos e um apêndice reprodutível. Uma nota com 3 em evidências, mas 1 em priorização, listou constatações sem julgá-las.

### 25.7 Erros comuns e limites

- Listar todas as constatações em vez de priorizar.
- Recomendações que não decorrem de nenhuma constatação.
- Misturar fatos e interpretações na seção de constatações.
- Alegar uma certeza que dados sintéticos não podem fornecer.

Uma nota que lista os seis fluxos do Laboratório 4, os cinco dispositivos sem suporte e todas as contas do Laboratório 7 cometeu o primeiro erro. Recomendar MFA para a CW sem uma constatação sobre as contas da CW é o segundo. Escrever "a conexão RDP é um intruso" nas constatações é o terceiro. Alegar alta confiança sobre exploração no mundo real a partir de dados sintéticos é o quarto.

### Exercícios — capítulo 25

**EX049 — Prioridades 2 e 3.** *Objetivo:* completar a avaliação. *Entradas:* Laboratórios 2, 4, 7. *Etapas:* escreva as prioridades 2 e 3 no formato da prioridade resolvida acima. *Evidência esperada:* duas prioridades argumentadas. *Rubrica:* use a rubrica de avaliação do laboratório; 3 = por exemplo, os fluxos RDP corporativo→controle e controle→internet da CW investigados e fechados (Laboratório 4), e as contas de desligados/tóxicas/de fornecedor (Laboratório 7) ou o isolamento dos dispositivos clínicos sem suporte (Laboratório 2), cada uma com raciocínio de consequência, dono e confiança; notas menores conforme a rubrica.

**EX050 — Conferência de reprodutibilidade.** *Objetivo:* verificar o trabalho de um colega. *Entradas:* o apêndice de um colega (ou o seu, trocado). *Etapas:* rode cada script de novo, compare hashes e saídas e escreva uma declaração de verificação de 100 palavras. *Evidência esperada:* a declaração. *Rubrica:* 3 = hashes e saídas comparados, qualquer discrepância explicada (por exemplo, script editado, versão do Python); 2 = só as saídas; 1 = declaração sem rodar de novo; 0 = nada.

### Síntese do capítulo

O Laboratório I transforma exercícios separados num único julgamento. Rastreie toda constatação até uma saída reprodutível, raciocine a partir das consequências entre operadores, ligue as recomendações às constatações e aos donos e declare explicitamente a confiança e os limites.

<!-- cyberabc:chapter-navigation:start ch-25 -->
### Continue estudando — capítulo 25 de 40

[← Capítulo 24](#ch-24) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 26 →](#ch-26)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-26"></a>

## Capítulo 26 — Infraestrutura crítica e segurança setorial: métodos II

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) construir modelos estruturados de ameaças de um sistema usando diagramas de fluxo de dados e uma lista de ameaças; (2) aplicar a análise de perigos baseada na teoria de sistemas (STPA) para encontrar ações de controle inseguras; (3) projetar e conduzir um exercício de mesa como método para testar planos; e (4) comparar esses métodos com os métodos de risco do Capítulo 23 e escolher entre eles. O capítulo se apoia nos Capítulos 21–24 e prepara o Capítulo 27 (verificação) e o Capítulo 28 (análise de falhas).

### 26.1 Modelagem de ameaças com fluxos de dados

Um **diagrama de fluxo de dados** mostra processos, repositórios de dados, entidades externas, fluxos e **fronteiras de confiança** (onde os dados passam de um nível de confiança para outro). A modelagem de ameaças percorre cada elemento e faz uma lista de perguntas. Uma lista amplamente usada, o STRIDE, pergunta sobre **S**poofing (falsificação de identidade), **T**ampering (adulteração de dados), **R**epudiation (repúdio — negar uma ação), **I**nformation disclosure (divulgação de informações), **D**enial of service (negação de serviço) e **E**levation of privilege (elevação de privilégio). Todo fluxo que atravessa uma fronteira de confiança merece a lista completa. O resultado é uma lista de ameaças com o elemento, o tipo de ameaça e uma mitigação proposta.

### 26.2 STPA: perigos a partir da estrutura de controle

O modelo **STAMP** de Leveson trata os acidentes como resultado de um controle inadequado, e não de cadeias de falhas de componentes ([Leveson, 2004](https://doi.org/10.1016/S0925-7535(03)00047-X)). O seu método de análise, a **STPA**, procede assim: definir as perdas e os perigos; modelar a **estrutura de controle** (quem controla o quê, com qual realimentação); para cada ação de controle, identificar as **ações de controle inseguras** (UCAs) em quatro formas — não fornecida quando necessária, fornecida quando insegura, fornecida cedo/tarde demais ou fora de ordem, interrompida cedo demais ou aplicada por tempo demais; depois, encontrar os cenários causais, incluindo realimentação ou comandos manipulados. A STPA se ajusta aos serviços críticos porque trata operadores, procedimentos, software e atacantes dentro de uma única estrutura.

### 26.3 Exercícios de mesa

Um **exercício de mesa** conduz uma equipe por um cenário em discussão, passo a passo, com injeções ("são 03:40; as telas do CAD mostram uma nota de resgate"). Ele testa planos, papéis e comunicação sem tocar nos sistemas em operação. Bons exercícios de mesa têm objetivos (por exemplo, "testar a decisão de passar ao despacho em papel"), um cenário sintético realista, um facilitador, observadores que registram as decisões e os tempos, e um **debriefing imediato** seguido de um plano de melhorias. Eles só são evidência de preparo na medida em que as constatações são postas em prática.

### 26.4 Escolher os métodos

| Método | Melhor para | Fraqueza |
|---|---|---|
| Avaliação de risco (Cap. 23) | Priorizar entre muitos cenários | Estimativas de probabilidade fracas para ameaças novas |
| Consequência primeiro / CCE | Piores desfechos, mitigações de engenharia | Pode negligenciar danos moderados frequentes |
| Modelo de ameaças STRIDE | Software e fluxos de dados | Fraco no processo físico e nas pessoas |
| STPA | Estruturas de controle, interações entre pessoas e software | Trabalhosa; exige conhecimento do processo |
| Exercício de mesa | Planos, papéis, comunicação | Discussão não é execução |

Para o CEDC, a tabela sugere a STPA para o controle do despacho e um exercício de mesa para a contingência em papel, como o capítulo faz; uma avaliação de risco então ordena o trabalho resultante.

### 26.5 Exemplo resolvido: STPA do despacho do CEDC (sintético)

**Este caso é sintético.** Perda: resposta de emergência atrasada. Perigo: uma ambulância não é despachada para uma chamada com risco de vida dentro do tempo-alvo. Estrutura de controle: atendente → CAD → despachante → tripulação da ambulância (por rádio e terminais móveis de dados); realimentação do sistema de localização de veículos para o CAD. Ação de controle: "designar a ambulância disponível mais próxima". UCAs: *não fornecida* — a fila do CAD congelada depois de uma atualização que falhou; *fornecida quando insegura* — o CAD designa uma unidade mostrada como "disponível" porque a realimentação de localização está velha ou falsificada; *tarde demais* — a contingência manual adotada só depois de 20 minutos, porque ninguém é dono da decisão; *interrompida cedo demais* — um despachante cancela uma designação depois de um erro de fusão de chamadas duplicadas. Cada UCA leva a requisitos: um alarme de congelamento do CAD, indicadores de dados velhos nas localizações dos veículos, um dono nomeado da decisão de contingência com um gatilho de 5 minutos e confirmação antes de cancelar uma designação de alta prioridade. Note que duas UCAs não envolvem atacante algum.

### 26.6 Erros comuns e limites

- Modelos de ameaças sem fronteiras de confiança.
- STPA reduzida a uma lista de falhas de componentes.
- Exercícios de mesa sem objetivos nem acompanhamento.
- Escolher o método mais impressionante, em vez daquele de que a pergunta precisa.

A STPA do CEDC evitou o segundo erro ao nomear ações de controle inseguras, duas delas sem atacante algum. Uma revisão STRIDE do fluxo do historiador da CW sem marcar a fronteira de confiança DMZ–controle cometeria o primeiro. Um exercício de mesa sem o objetivo "decidir sobre o despacho em papel" comete o terceiro. E escolher a STPA para impressionar quando a pergunta é "qual estratégia de backup" comete o quarto.

### Exercícios — capítulo 26

**EX051 — STRIDE num fluxo.** *Objetivo:* aplicar a lista. *Entradas:* o fluxo da CW "o coletor do historiador na DMZ lê OPC UA do servidor SCADA". *Etapas:* escreva uma ameaça para cada letra do STRIDE, com uma mitigação. *Evidência esperada:* seis linhas. *Rubrica:* 3 = seis ameaças plausíveis com mitigações correspondentes (por exemplo, coletor falsificado → certificados mútuos; adulteração → sessão assinada/autenticada; DoS → limites de taxa do lado do SCADA); 2 = quatro ou cinco; 1 = menos; 0 = nada.

**EX052 — Projete um exercício de mesa.** *Objetivo:* planejar um exercício. *Entradas:* CVH, cenário "um ransomware cifra o sistema de administração de pacientes num sábado à noite". *Etapas:* escreva os objetivos (dois), os participantes, quatro injeções com horários e as evidências que você vai registrar. *Evidência esperada:* plano. *Rubrica:* 3 = objetivos mensuráveis, participantes clínicos e técnicos, injeções realistas e crescentes (incluindo decisões de proteção de dados e de comunicação), tempos e decisões registrados; 2 = parcial; 1 = só o cenário; 0 = nada.

### Síntese do capítulo

A modelagem de ameaças encontra ameaças onde os dados atravessam fronteiras de confiança; a STPA encontra ações de controle inseguras em estruturas sociotécnicas; os exercícios de mesa testam planos e pessoas. Cada um vê o que os outros deixam escapar, então escolha pela pergunta — e lembre-se de que muitos perigos não envolvem adversário algum.

<!-- cyberabc:chapter-navigation:start ch-26 -->
### Continue estudando — capítulo 26 de 40

[← Capítulo 25](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 →](#ch-27)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-27"></a>

## Capítulo 27 — Infraestrutura crítica e segurança setorial: verificação

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) distinguir a verificação ("construído certo") da validação ("construída a coisa certa") para controles de segurança; (2) projetar um teste capaz de mostrar que um controle *não* funciona; (3) avaliar um detector com precisão e revocação e escolher um limiar com trade-offs explícitos; e (4) reportar os resultados de verificação com as suas condições e limites. O capítulo se apoia nos Capítulos 8, 12, 15 e 24 e prepara o Capítulo 29 (operações) e o Laboratório II (Capítulo 30).

### 27.1 Verificação e validação

A **verificação** confere se um controle faz o que a sua especificação diz: o firewall bloqueia a porta 3389 do corporativo para o controle; o validador de setpoint rejeita NaN. A **validação** confere se o controle alcança a sua finalidade no ambiente real: os usuários corporativos não conseguem alcançar os sistemas de controle por *nenhum* caminho; os operadores não conseguem enviar setpoints inseguros. Um controle pode passar na verificação e falhar na validação (a regra do firewall funciona, mas um notebook de engenharia dual-homed a contorna). Uma boa verificação é **falseável**: ela é projetada de modo que um controle quebrado falharia no teste. Um teste que passaria quer o controle funcione, quer não, não prova nada.

### 27.2 Tipos de teste

A **revisão de configuração** compara as configurações com uma linha de base. Os **testes funcionais** exercitam o controle com entradas esperadas e proibidas (os testes de limite do Capítulo 8). Os **testes de fluxo** confirmam que os caminhos não permitidos estão bloqueados (Capítulo 7, sob autorização). Os **exercícios de restauração** verificam os controles de recuperação de ponta a ponta (Capítulo 15). Os **testes de detecção** reproduzem atividade sintética rotulada ou benigna-mas-suspeita para ver se o monitoramento alerta. Na TO, testar no processo em operação é restrito; use bancadas de teste, réplicas offline ou janelas planejadas acordadas com a operação.

Para a regra corporativo–controle da CW, um teste de fluxo a partir de um host corporativo autorizado para endereços do controle, numa janela planejada, é funcional; uma revisão de configuração sozinha não é.

### 27.3 Avaliar detectores

Um detector produz notas; um limiar as transforma em alertas. Compare os alertas com os rótulos de verdade: **verdadeiros positivos** (TP), **falsos positivos** (FP), **falsos negativos** (FN). **Precisão** = TP/(TP+FP): dos alertas, quantos eram reais? **Revocação** = TP/(TP+FN): dos eventos reais, quantos foram pegos? Elevar o limiar costuma aumentar a precisão e diminuir a revocação. Com eventos maliciosos raros (a taxa de base do Capítulo 12), a precisão pode ser ruim mesmo com taxas de erro por evento excelentes. Escolha um limiar perguntando quanto cada perda e cada alarme falso custam ao serviço — e lembre-se de que os dados rotulados de avaliação raramente correspondem às condições reais ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp)).

### 27.4 Exemplo resolvido e Laboratório 10 (sintético)

**Este caso é sintético.** A Calder Mutual avalia um detector de anomalias em 5.025 eventos rotulados, 25 deles maliciosos (semente 10).

```python
# Lab 10 - detection evaluation on a labelled synthetic event set (offline)
import random
random.seed(10)
events = []  # (score from a detector, truly malicious?)
for _ in range(5000):
    events.append((random.gauss(0.30, 0.12), False))
for _ in range(25):
    events.append((random.gauss(0.70, 0.15), True))
for thr in (0.5, 0.6, 0.7):
    tp = sum(1 for s, m in events if s >= thr and m)
    fp = sum(1 for s, m in events if s >= thr and not m)
    fn = sum(1 for s, m in events if s < thr and m)
    prec = tp / (tp + fp) if tp + fp else 0
    print(f"threshold {thr}: TP={tp:2} FP={fp:3} FN={fn:2} precision={prec:.2f} recall={tp/(tp+fn):.2f}")
```

Saída esperada:

```text
threshold 0.5: TP=23 FP=215 FN= 2 precision=0.10 recall=0.92
threshold 0.6: TP=20 FP= 36 FN= 5 precision=0.36 recall=0.80
threshold 0.7: TP=18 FP=  2 FN= 7 precision=0.90 recall=0.72
```

Em 0,5, a equipe pega 23 de 25, mas precisa vasculhar 215 alertas falsos; em 0,7, quase todo alerta é real, mas 7 ataques passam despercebidos. Nenhum dos dois é "correto". Uma escolha defensável poderia usar 0,7 para acionar o analista de plantão e 0,5 para uma fila de revisão diária — dois limiares para dois custos. O relatório declara as condições: notas sintéticas, uma única semente, 25 positivos (então as estimativas de revocação são grosseiras — Capítulo 37) e semelhança desconhecida com o tráfego real.

### 27.5 Erros comuns e limites

- Testes que não podem falhar.
- Reportar a acurácia em dados desbalanceados (99,5% de "acurácia" aqui, sem nunca alertar).
- Escolher limiares sem declarar os custos.
- Avaliar em dados que se parecem mais com os dados de treinamento do que com a realidade.
- Verificar em laboratório e alegar validação em produção.

O Laboratório 10 mostra numericamente o segundo erro: nunca alertar dá 99,5 % de acurácia. Escolher 0,5 ou 0,7 sem dizer quanto custam um ataque perdido ou 215 alertas falsos a mais é o terceiro. Uma regra de firewall testada só a partir da réplica do laboratório é o quinto. Um teste que reportaria "bloqueado" porque o host de teste estava desligado é o primeiro.

### Exercícios — capítulo 27

**EX053 — Torne-o falseável.** *Objetivo:* projetar um teste significativo. *Entradas:* a afirmação "o firewall da CW impede os usuários corporativos de alcançar a zona de controle". *Etapas:* projete um teste de verificação e um de validação, cada um com um resultado que mostraria que a afirmação é falsa, e a autorização necessária. *Evidência esperada:* dois projetos de teste. *Rubrica:* 3 = teste no nível da regra, a partir de um host corporativo para os endereços do controle em todas as portas, numa janela planejada, mais uma validação procurando caminhos alternativos (hosts dual-homed, acesso remoto, sem fio) por revisão de configuração e de fluxos; autorização declarada; 2 = um teste; 1 = não falseável; 0 = nada.

**EX054 — A armadilha da acurácia.** *Objetivo:* ver por que a acurácia engana. *Entradas:* Laboratório 10. *Etapas:* calcule a acurácia para o limiar 0,7 e para um detector que nunca alerta; explique por que os dois parecem "excelentes". *Evidência esperada:* dois números e explicação. *Rubrica:* 3 = (5025−2−7)/5025 ≈ 0,9982 e 5000/5025 ≈ 0,9950; explica o desbalanceamento de classes e recomenda precisão/revocação; 2 = só os números; 1 = um número; 0 = nada.

### Síntese do capítulo

A verificação pergunta se um controle funciona como especificado; a validação pergunta se ele alcança a sua finalidade. Projete testes que possam falhar, avalie os detectores com precisão e revocação em limiares escolhidos por custos declarados e reporte as condições e os limites junto com os números.

<!-- cyberabc:chapter-navigation:start ch-27 -->
### Continue estudando — capítulo 27 de 40

[← Capítulo 26](#ch-26) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 28 →](#ch-28)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-28"></a>

## Capítulo 28 — Infraestrutura crítica e segurança setorial: análise de falhas

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) construir uma árvore de falhas simples com portas E e OU e calcular a probabilidade do evento de topo sob independência; (2) realizar uma análise de modos e efeitos de falha (FMEA) para um sistema pequeno; (3) acrescentar um caminho cibernético a uma análise de safety e ver como ele muda o resultado; e (4) conduzir uma revisão pós-incidente sem culpabilização que procure as causas sistêmicas. O capítulo se apoia nos Capítulos 12, 21, 22 e 26 e prepara o Capítulo 29 (operações) e o Capítulo 31 (casos avançados).

### 28.1 Árvores de falhas

Uma **árvore de falhas** parte de um **evento de topo** indesejado e o decompõe em causas ligadas por **portas**. Uma porta **E** significa que todas as entradas precisam ocorrer; uma porta **OU** significa que qualquer uma basta. Com eventos básicos independentes, a porta E multiplica as probabilidades e a porta OU as combina como $1 - \prod (1 - p_i)$. As árvores de falhas tornam as premissas explícitas e mostram quais eventos básicos dominam. Elas são tradicionalmente construídas para falhas aleatórias; a análise de segurança acrescenta caminhos em que um adversário pode fazer um evento acontecer de propósito — e a "probabilidade" de um adversário não é uma propriedade do hardware.

### 28.2 FMEA

A **análise de modos e efeitos de falha** trabalha de baixo para cima: para cada componente, liste as formas como ele pode falhar (não parte, falha aberto, dá leitura falsa), o efeito sobre o sistema, como isso seria detectado e os controles existentes; depois, ordene. A FMEA encontra bem os problemas de componentes isolados e mal as interações, e é por isso que ela anda junto com a STPA (Capítulo 26) e as árvores de falhas.

O EX056 aplica a FMEA à bomba dosadora e ao analisador da CW.

Uma linha para a bomba dosadora da CW diz: componente bomba dosadora; modo funciona na vazão máxima; efeito supercloração na saída; detecção alarme do analisador de residual na saída; controle existente vazão máxima da bomba limitada por fiação.

### 28.3 Exemplo resolvido e Laboratório 11 (sintético)

**Este caso é sintético.** Evento de topo no CVH: "o hospital perde a energia com qualidade de rede para as cargas críticas". Fisicamente, isso exige uma interrupção da rede elétrica E a falha da reserva (o gerador não parte OU o combustível está contaminado OU a chave de transferência automática falha). Separadamente, o BMS do hospital consegue comandar o painel de alimentação essencial; um comprometimento do BMS poderia desligar as cargas críticas independentemente da rede.

```python
# Lab 11 - a small fault tree for "hospital loses mains-quality power" (synthetic annual probabilities)
P = {"grid": 0.05, "gen_fails_start": 0.02, "fuel_contaminated": 0.005, "ats_fails": 0.01, "cyber_bms": 0.002}
# top = grid AND (backup fails); backup fails = gen_fails_start OR fuel_contaminated OR ats_fails
# separately: a compromised building-management system can shed critical loads whatever the grid state
backup_fails = 1 - (1 - P["gen_fails_start"]) * (1 - P["fuel_contaminated"]) * (1 - P["ats_fails"])
top_physical = P["grid"] * backup_fails
top = 1 - (1 - top_physical) * (1 - P["cyber_bms"])
print(f"P(backup fails on demand) = {backup_fails:.5f}")
print(f"P(top) physical only = {top_physical:.6f}")
print(f"P(top) with BMS path  = {top:.6f}")
print(f"share from cyber path ~ {P['cyber_bms'] / top:.0%}")
```

Saída esperada:

```text
P(backup fails on demand) = 0.03465
P(top) physical only = 0.001733
P(top) with BMS path  = 0.003729
share from cyber path ~ 54%
```

Com esses números sintéticos, o projeto físico é bom: são necessárias duas falhas independentes. O caminho cibernético é um único evento que contorna a porta E e aproximadamente dobra a probabilidade do evento de topo. O ponto mais profundo não depende da estimativa de 0,002: um atacante não falha ao acaso, então um caminho que precisa de um único "evento" sob controle do adversário pode dominar qualquer número que você escreva. A resposta de engenharia é restaurar a estrutura E — tornar impossível desligar as cargas críticas a partir do BMS (um bloqueio por fiação, ou o controle do BMS limitado aos painéis não críticos) —, em vez de apenas baixar a probabilidade estimada.

### 28.4 Revisão pós-incidente sem culpabilização

Quando as falhas acontecem, uma **revisão sem culpabilização** pergunta como o sistema permitiu que a ação de uma pessoa razoável causasse dano, e não quem punir. O modelo de Reason dos acidentes organizacionais descreve as defesas como camadas com furos que ocasionalmente se alinham ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)). Pergunte: o que as pessoas sabiam no momento; o que fez a sua ação parecer certa; quais defesas estavam ausentes ou foram contornadas; o que vamos mudar no sistema? A culpa suprime os relatos, e os quase acidentes não relatados são evidência perdida.

No caso do Laboratório 11, uma revisão sem culpabilização de um evento de perda de energia perguntaria por que o BMS conseguia desligar as cargas críticas.

### 28.5 Erros comuns e limites

- Multiplicar as probabilidades de eventos com causas comuns (Capítulo 12).
- Tratar as ações de um adversário como falhas aleatórias.
- FMEA sem interações; árvores de falhas sem as pessoas.
- Revisões que terminam com "erro humano" e retreinamento.

O Laboratório 11 supõe a independência entre a falha do gerador e a contaminação do combustível; o EX024 mostra como um tanque de combustível compartilhado quebra isso. O caminho do BMS é o segundo erro tornado explícito: 0,002 não é uma propriedade do BMS. O terceiro aparece se uma FMEA do gerador ignorar o operador que precisa dar a partida manualmente. Uma revisão que termina com "erro do engenheiro da manutenção predial; retreinar" é o quarto.

### Exercícios — capítulo 28

**EX055 — Restaure a porta E.** *Objetivo:* ver o efeito de uma correção de engenharia. *Entradas:* Laboratório 11. *Etapas:* modele uma correção em que o BMS só consegue desligar as cargas críticas se também houver uma interrupção da rede (isto é, o caminho cibernético entra na porta E da rede como uma causa extra de falha da reserva). Calcule a nova probabilidade do evento de topo. *Evidência esperada:* código modificado e valor. *Rubrica:* 3 = falha da reserva = 1−(0,98)(0,995)(0,99)(0,998) ≈ 0,03658, topo ≈ 0,001829, com o comentário de que o caminho cibernético agora precisa de uma interrupção da rede coincidente; 2 = abordagem certa, deslize aritmético; 1 = estrutura inalterada; 0 = nada.

**EX056 — Linhas de FMEA.** *Objetivo:* aplicar a análise de baixo para cima. *Entradas:* a bomba dosadora de cloro da CW e o seu analisador de residual. *Etapas:* escreva quatro linhas de FMEA (componente, modo de falha, efeito, detecção, controle existente). *Evidência esperada:* tabela. *Rubrica:* 3 = modos realistas (bomba na vazão máxima, bomba para, analisador lê baixo, analisador congelado) com efeitos sobre a segurança da água e detecções críveis; 2 = três; 1 = vago; 0 = nada.

### Síntese do capítulo

As árvores de falhas e a FMEA tornam explícitas as premissas sobre falhas, de cima para baixo e de baixo para cima. Acrescentar caminhos cibernéticos revela eventos únicos que contornam a redundância projetada; a resposta mais forte restaura a independência estrutural, em vez de ajustar uma estimativa. Quando as falhas acontecem, revise o sistema, e não a pessoa.

<!-- cyberabc:chapter-navigation:start ch-28 -->
### Continue estudando — capítulo 28 de 40

[← Capítulo 27](#ch-27) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 29 →](#ch-29)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-29"></a>

## Capítulo 29 — Infraestrutura crítica e segurança setorial: operações

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) descrever as operações de segurança de um operador de serviço crítico — monitoramento, triagem, escalonamento, gestão de mudanças e de vulnerabilidades; (2) adaptar a resposta a incidentes à tecnologia operacional, em que manter o processo seguro vem primeiro; (3) medir o desempenho operacional com o tempo para detectar e o tempo para recuperar, usando medianas e percentis; e (4) escrever uma etapa de playbook que respeite tanto a segurança quanto as operações. O capítulo se apoia nos Capítulos 12, 15, 24, 27 e 28 e prepara o Laboratório II (Capítulo 30).

### 29.1 O que as operações de segurança fazem

No dia a dia, uma função de operações de segurança **monitora** (logs, tráfego de rede, alertas), **faz a triagem** (isto é real? quão grave?), **escalona** (para quem, com que rapidez), **coordena as mudanças** (nenhuma mudança surpresa nos sistemas de TO) e **gerencia as vulnerabilidades** (Capítulos 5, 9, 11). Para um operador de serviço crítico, a característica definidora é a parceria com as **operações**: a equipe da sala de controle, os engenheiros e os clínicos sabem como é o normal para o processo e são donos das decisões que o afetam. Operações de segurança que não conversam com a sala de controle vão interpretar mal os alertas e, pior, tomar ações que prejudicam o serviço.

### 29.2 Resposta a incidentes na TO

As recomendações de resposta a incidentes do NIST, revisadas em 2025, situam a resposta dentro da gestão geral de riscos de cibersegurança e das funções do CSF 2.0 ([SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). Na TO, a ordem das prioridades muda: **primeiro manter o processo seguro** (o que pode significar passar ao controle manual ou local), **depois conter** (isolar os segmentos de TI ou TO afetados sem cortar o que o processo precisa), **depois investigar e recuperar**. Desconectar um servidor comprometido é um reflexo na TI; na TO, o operador precisa primeiro saber o que esse servidor faz — tirar o historiador é inofensivo, tirar o único servidor SCADA pode cegar os operadores durante uma tempestade. A evidência também precisa ser preservada: imagens das estações de engenharia, configurações dos controladores, capturas de rede e o livro do operador. Os playbooks são acordados com antecedência com as operações, a safety e, onde dados pessoais puderem estar envolvidos, a proteção de dados (Capítulo 14).

### 29.3 Medir as operações

As medidas comuns são o **tempo para detectar** (TTD: da primeira atividade maliciosa ou com defeito até a detecção) e o **tempo para recuperar** (TTR: da detecção até o serviço restabelecido). As suas distribuições são assimétricas (Capítulo 12): a maioria dos incidentes é tratada rapidamente; alguns levam dias. Reporte a **mediana**, o **90º percentil** e o **tamanho da amostra**, e examine os valores atípicos individualmente — é na cauda longa que estão as lições. Cuidado com os incentivos: uma meta de TTD pode estimular registrar com generosidade a hora da "detecção".

Os 15 registros do Laboratório 12 mostram por quê: média de 27,2 horas, mediana de 4.

Examine individualmente a detecção de 240 horas; foi um uso indevido lento de credenciais.

### 29.4 Exemplo resolvido e Laboratório 12 (sintético)

**Este caso é sintético.** Os membros da CRP reuniram 15 registros de incidentes sanitizados dos últimos dois anos.

```python
# Lab 12 - time to detect and recover: mean, median and percentiles from synthetic tickets (offline)
import statistics as st
TTD_H = [0.5, 1, 1, 2, 2, 3, 3, 4, 6, 8, 12, 20, 36, 70, 240]   # hours from first malicious activity to detection
TTR_H = [2, 3, 3, 4, 5, 5, 6, 8, 8, 10, 12, 16, 24, 48, 96]
for name, xs in (("time to detect", TTD_H), ("time to recover", TTR_H)):
    q = st.quantiles(xs, n=10, method="inclusive")
    print(f"{name}: n={len(xs)} mean={st.mean(xs):.1f} median={st.median(xs):.1f} p90={q[8]:.1f} max={max(xs)}")
print("mean TTD without the 240 h outlier:", round(st.mean(TTD_H[:-1]), 1))
```

Saída esperada:

```text
time to detect: n=15 mean=27.2 median=4.0 p90=56.4 max=240
time to recover: n=15 mean=16.7 median=8.0 p90=38.4 max=96
mean TTD without the 240 h outlier: 12.0
```

O tempo médio para detectar (27,2 h) não descreve nenhum incidente real: metade foi detectada em até 4 horas, e um levou dez dias. Remover esse único registro corta a média em mais da metade. O relatório útil diz: "mediana de 4 h, 90º percentil de cerca de 56 h, n = 15; o caso de 240 horas foi um uso indevido lento de credenciais encontrado durante uma revisão de acessos" — e então pergunta por que o monitoramento o deixou escapar. Percentis sobre 15 registros são aproximados; o método de cálculo deve ser declarado (aqui, o método "inclusive" do `statistics.quantiles` do Python).

### 29.5 Uma etapa de playbook (sintético)

*Playbook da CPN, etapa 3 — suspeita de comprometimento de uma estação de engenharia:* (1) O analista de segurança informa o supervisor da sala de controle; o supervisor confirma que nenhuma operação de manobra depende da estação neste momento. (2) O supervisor autoriza o isolamento; o analista isola a porta de rede da estação, deixando-a ligada (para preservar a memória). (3) Um engenheiro confere as configurações dos controladores que a estação poderia ter alterado, comparando com o último backup sabidamente bom. (4) O analista registra os horários, as decisões e quem autorizou no log do incidente. Cada etapa nomeia quem decide e por que a ordem importa.

Se um engenheiro da CPN estivesse no meio de uma manobra de carga em torno da Substation North a partir daquela estação, tirar a sua porta de rede deixaria a operação pela metade, com a sala de controle sem saber quais disjuntores tinham se movido.

### 29.6 Erros comuns e limites

- Equipes de segurança agindo na TO sem a autorização das operações.
- Desligar a energia ou apagar sistemas antes de preservar a evidência.
- Reportar tempos médios para dados assimétricos.
- Playbooks que existem só nos sistemas que o incidente desativou.

O playbook da CPN evita os dois primeiros ao fazer o supervisor autorizar o isolamento e ao deixar a estação ligada. O Laboratório 12 mostra o terceiro. O quarto é o motivo de os membros da CRP manterem cópias impressas dos playbooks em cada sala de controle, já que um incidente pode desativar o sistema de documentos que os guarda.

### Exercícios — capítulo 29

**EX057 — Reporte a cauda.** *Objetivo:* resumir dados assimétricos com honestidade. *Entradas:* Laboratório 12. *Etapas:* escreva um resumo de 100 palavras para o conselho da CRP sobre o TTD e o TTR, incluindo o tamanho da amostra, uma limitação e uma pergunta sobre o caso mais longo. *Evidência esperada:* o resumo. *Rubrica:* 3 = medianas e p90 com n, distorção da média apontada, limitação (pequena, sanitizada, tempos de detecção autodeclarados), pergunta incisiva; 2 = números sem ressalva; 1 = só as médias; 0 = nada.

**EX058 — Contenção segura.** *Objetivo:* ordenar as ações na resposta em TO. *Entradas:* ransomware detectado no servidor do historiador da CW na zona de controle; os servidores SCADA parecem não afetados. *Etapas:* escreva as cinco primeiras ações em ordem, com quem decide cada uma. *Evidência esperada:* lista ordenada. *Rubrica:* 3 = confirmar o estado do processo com as operações; preparar a operação manual/local; isolar o historiador da zona de controle com a aprovação das operações; preservar a evidência; conferir o SCADA e os controladores contra o estado sabidamente bom, com os papéis nomeados; 2 = sensato, mas fora de ordem ou sem papéis; 1 = o "desligar tudo" ao estilo da TI; 0 = nada.

### Síntese do capítulo

Nos serviços críticos, as operações de segurança trabalham lado a lado com as operações: primeiro manter o processo seguro, conter sem cegar os operadores, preservar a evidência e recuperar. Meça com medianas, percentis e tamanhos de amostra, e investigue os valores atípicos que as médias escondem.

<!-- cyberabc:chapter-navigation:start ch-29 -->
### Continue estudando — capítulo 29 de 40

[← Capítulo 28](#ch-28) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 30 →](#ch-30)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-30"></a>

## Capítulo 30 — Laboratório II

### Objetivos de aprendizagem e conexão

Depois deste laboratório, você consegue (1) conduzir um exercício contido em duas partes — um exercício de mesa facilitado e uma análise de evidências offline — para um cenário entre setores; (2) reconstruir uma linha do tempo a partir de logs sintéticos e verificar a integridade dos logs; (3) avaliar as decisões contra os planos e as medidas; e (4) escrever um relatório pós-ação com um plano de melhorias. O laboratório integra os Capítulos 17, 21, 22, 26, 27 e 29 e é o segundo ponto de controle de projeto.

### 30.1 Cenário (sintético)

**Este cenário é sintético.** Às 02:10 de uma noite de inverno, a sala de controle da Calder Water informa que o setpoint de nível da estação de bombeamento PS2 mudou de 4,1 m para 2,0 m às 01:52. Ninguém assume a mudança. Às 02:30, a CPN informa uma falta na Substation North que levará 6 horas para ser reparada. O gerente de plantão do CEDC pergunta se o abastecimento de água do hospital está em risco. Equipes de quatro pessoas fazem os papéis de operações da CW, segurança da CW, controle da CPN e manutenção predial do CVH; um facilitador entrega as injeções.

A Calder Water poderia investigar a mudança do setpoint da PS2, e a CPN poderia reparar a Substation North em 6 horas; juntas, elas levantam a pergunta que nenhuma consegue responder sozinha: se a água do hospital se mantém enquanto as duas coisas não estão resolvidas.

### 30.2 Parte A — exercício de mesa (90 minutos)

Objetivos: (1) decidir em até 20 minutos se a PS2 passa ao controle local; (2) produzir até as 03:00 um quadro de situação consolidado entre operadores para o CEDC; (3) decidir quais evidências preservar. Injeções: 02:40 — a segurança da CW descobre que uma sessão remota de fornecedor esteve ativa das 01:45 às 01:58; 02:55 — a manutenção predial do CVH informa 72 h de combustível para o gerador, mas pergunta sobre a água; 03:20 — um jornalista local liga para a CW. Os observadores registram os horários das decisões, quem decidiu e com base em qual evidência.

Os observadores devem anotar o minuto em que cada decisão foi tomada, por quem e com base em qual evidência, para que o relatório pós-ação possa comparar os tempos com os objetivos. O objetivo de 20 minutos para a PS2 começa às 02:10.

### 30.3 Parte B — análise de evidências (offline)

Usando a função de cadeia de hashes do Laboratório 8, as equipes recebem três arquivos: o livro do operador, a cabeça ancorada vinda do servidor de âncora separado e o registro da sessão do fornecedor. Elas recalculam a cadeia, encontram qual entrada (se alguma) foi alterada e a alinham com os horários da sessão. Usando o modelo de autonomia do Laboratório 9 (Capítulo 22) com a interrupção de 6 horas, elas declaram quais serviços se perdem e quando, e se a água do hospital depende da PS2. Todo resultado precisa ser reprodutível: hash do script, versão do Python, saída.

Com 10 horas de armazenamento de água tratada contra uma interrupção de 6 horas, a água do hospital deveria se manter pelos números do Laboratório 9; a pergunta em aberto para as equipes é se esse número de armazenamento ainda vale com o setpoint da PS2 em 2,0 m, em vez dos 4,1 m normais.

### 30.4 Exemplo resolvido: a linha do tempo e os seus limites (sintético)

| Hora | Evento | Fonte | Confiança |
|---|---|---|---|
| 01:45 | A sessão remota do fornecedor é aberta | Registro de acesso remoto | Alta (registro do sistema) |
| 01:52 | Setpoint da PS2 4,1 → 2,0 m | Entrada 2 do livro do operador | Média — o recálculo da cadeia mostra que a entrada 2 não corresponde à cabeça ancorada, então o log foi alterado depois do fato |
| 01:58 | A sessão do fornecedor é encerrada | Registro de acesso remoto | Alta |
| 02:10 | Os operadores percebem | Livro de turno | Alta |
| 02:30 | Falta na Substation North (6 h) | Controle da CPN | Alta |

Interpretação: a mudança de setpoint coincide com a sessão do fornecedor, e a entrada do log que a registra foi alterada — o que é compatível com uma mudança maliciosa ou descuidada escondida depois, mas não prova quem a fez. Entre setores: com uma interrupção de 6 horas na rede elétrica, as bombas da CW param de imediato e o armazenamento de água tratada (10 h) sustenta o abastecimento (Laboratório 9); um setpoint rebaixado significa menos água armazenada do que o planejado, o que encurta essa autonomia — a interação perigosa é entre dois eventos que, isoladamente, são gerenciáveis. Decisões: passar a PS2 ao controle local e restaurar o setpoint (operações), suspender o acesso remoto de fornecedores (segurança, com o diretor da CW), preservar o registro da sessão do fornecedor, a imagem do servidor de logs e a âncora (segurança), informar o CEDC e o CVH com uma faixa estimada de autonomia da água (operações, até as 03:00) e encaminhar a imprensa ao porta-voz acordado.

### 30.5 Relatório pós-ação

Estrutura: os objetivos e se foram cumpridos (com os horários); o que deu certo; o que não deu; as causas raiz (sistêmicas, sem culpabilização — Capítulo 28); as ações de melhoria com donos e datas; o apêndice de evidências. Distinga os **artefatos do exercício** (coisas que só aconteceram porque era um exercício) das constatações reais.

Neste cenário, a ligação do jornalista às 03:20 testa um procedimento real; uma injeção atrasada do facilitador é um artefato do exercício. As ações de melhoria decorrem das causas raiz, como o acesso remoto de fornecedores não gerenciado, e não de erros individuais.

Para a ação sobre o acesso de fornecedores, a verificação seria conferir que a conta do fornecedor está desativada fora dos tíquetes aprovados e que o registro da sessão das 01:52 pode ser recuperado.

### 30.6 Rubrica de avaliação

| Critério | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| Decisões | Tempestivas, com dono, baseadas em evidências | Tempestivas ou baseadas em evidências | Atrasadas ou sem dono | Nenhuma |
| Linha do tempo | Com fontes, confiança graduada, integridade conferida | Com fontes | Sem fontes | Nenhuma |
| Raciocínio entre setores | Interação identificada e quantificada | Identificada | Um único setor | Nenhum |
| Relatório | Ações com dono e data; artefatos separados | Ações vagas | Só narrativa | Nenhum |

Uma equipe que restaura o setpoint rapidamente, mas não consegue dizer quem decidiu, recebe 2 em decisões. Uma linha do tempo cuja linha das 01:52 está marcada com confiança alta apesar da entrada de log alterada recebe 1. O raciocínio entre setores só recebe 3 se a autonomia de água encurtada for estimada, e não apenas mencionada.

### Exercícios — capítulo 30

**EX059 — Graduação da confiança.** *Objetivo:* justificar os pesos das evidências. *Entradas:* a linha do tempo resolvida deste laboratório. *Etapas:* explique a confiança de cada linha e qual evidência adicional elevaria a linha das 01:52 para alta. *Evidência esperada:* explicações. *Rubrica:* 3 = registros do sistema, alta; entrada de log alterada, média, porque a hora e o valor da entrada original são desconhecidos; elevá-la exige logs de eventos do PLC/controlador, a tendência do setpoint no historiador, a gravação da sessão do lado do fornecedor; 2 = parcial; 1 = asserções; 0 = nada.

**EX060 — Plano de melhorias.** *Objetivo:* transformar constatações em ações. *Entradas:* o cenário. *Etapas:* escreva cinco ações de melhoria com dono, data e como a conclusão será verificada. *Evidência esperada:* tabela. *Rubrica:* 3 = por exemplo, aprovação e gravação por sessão para fornecedores, alarmes de mudança de setpoint com limites, âncora no sistema de outra equipe, modelo de quadro de situação entre operadores, exercício conjunto com a CPN; cada uma verificável; 2 = ações sem verificação; 1 = vago; 0 = nada.

### Síntese do capítulo

O Laboratório II combina pessoas e evidências: decidir sob pressão de tempo, reconstruir linhas do tempo a partir de fontes com confiança graduada, verificar a integridade e raciocinar entre setores. As situações mais perigosas muitas vezes surgem da interação de dois eventos que, isoladamente, são gerenciáveis.

<!-- cyberabc:chapter-navigation:start ch-30 -->
### Continue estudando — capítulo 30 de 40

[← Capítulo 29](#ch-29) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 31 →](#ch-31)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-31"></a>

## Capítulo 31 — Infraestrutura crítica e segurança setorial: casos avançados

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) analisar casos em que o dano veio pelo processo físico, pelos sistemas de safety ou por fornecedores compartilhados, e não pelo roubo de dados; (2) comparar casos de forma sistemática por causa, caminho, consequência, detecção e recuperação; (3) raciocinar sobre o risco da cadeia de suprimentos e de concentração entre setores; e (4) extrair lições defensáveis e delimitadas para um operador. O capítulo se apoia no Capítulo 20 e nos Capítulos 21–30 e prepara o projeto comparativo (Capítulo 34).

### 31.1 Além da manchete

A análise avançada de casos não pergunta "o que aconteceu?", e sim "qual premissa falhou, e essa premissa está presente aqui?" Três famílias de casos ilustram premissas de que os serviços críticos dependem.

**Manipulação do processo projetada para ficar escondida.** A análise de Langner sobre o Stuxnet descreve um malware que manipulava controladores industriais que acionavam centrífugas enquanto apresentava aos operadores valores de aparência normal ([Langner, 2011](https://doi.org/10.1109/MSP.2011.67)). *Premissa que falhou:* o que o operador vê é o que o processo faz. *Lição transferível:* caminhos de medição independentes para as variáveis críticas e limites físicos que não dependam do controlador.

**Ataques à camada de safety.** A análise do TRITON/HatMan descreve um malware que tinha como alvo um controlador de sistema instrumentado de segurança ([CISA MAR-17-352-01](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf)). *Premissa que falhou:* o sistema de safety é independente das redes que um atacante consegue alcançar. *Lição:* impor fisicamente os modos de programação do SIS (chaves físicas), separar as redes do SIS e tratar as estações de engenharia do SIS como os ativos mais sensíveis.

**Falha de dependência compartilhada.** A atualização de segurança defeituosa de julho de 2024, que derrubou cerca de 8,5 milhões de dispositivos Windows ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)), e a parada preventiva de 2021 depois de um ransomware na rede de TI de uma empresa de oleodutos ([CISA AA21-131A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a)) mostram o dano chegando pelas dependências, e não pelo sistema de controle. *Premissa que falhou:* o nosso risco é limitado pelos nossos próprios sistemas. *Lição:* mapear a concentração (muitos serviços dependendo de um produto, fornecedor ou região de nuvem), escalonar as atualizações e planejar uma operação degradada que não precise da TI de negócio.

### 31.2 Cadeias de suprimentos

Todo operador roda software e hardware construídos por outros, muitas vezes por meio de longas cadeias de componentes. As medidas públicas incluem as **listas de materiais de software**, que listam os componentes ([CISA SBOM](https://www.cisa.gov/sbom)), frameworks para a integridade do build como o SLSA ([SLSA](https://slsa.dev/)), práticas de desenvolvimento seguro para fornecedores ([NIST SSDF, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)) e expectativas de "seguro por concepção" sobre os fabricantes ([CISA Secure by Design](https://www.cisa.gov/securebydesign)). No bacharelado, as alavancas do operador são sobretudo contratuais e arquiteturais: exigir SBOMs e divulgação de vulnerabilidades, testar as atualizações antes da implantação, escalonar a distribuição, manter a capacidade de reverter e evitar que a falha de um único fornecedor pare várias funções críticas ao mesmo tempo.

### 31.3 Um quadro de comparação

| Dimensão | Stuxnet (como analisado) | TRITON/HatMan | Interrupção da atualização de 2024 |
|---|---|---|---|
| Causa | Deliberada, direcionada | Deliberada, direcionada | Acidental |
| Caminho | Para dentro dos controladores | Para dentro do controlador de safety | Por meio de um produto compartilhado |
| Consequência | Dano físico escondido da visão | Perda potencial de proteção | Perda em massa de disponibilidade |
| Premissa que falhou | Visão = realidade | Independência do SIS | Risco limitado pelos próprios sistemas |
| Controle genérico | Medição independente, limites físicos | Controles físicos do SIS, segregação | Atualizações escalonadas, mapeamento da concentração, modos degradados |

Leia primeiro a linha "Premissa que falhou"; ela é a parte transferível. Cada controle genérico trata essa premissa, e não a técnica específica.

### 31.4 Exemplo resolvido: concentração em Calder (sintético)

**Este caso é sintético.** A CRP faz um levantamento entre os seus membros: o CVH, o CEDC e a Calder Mutual usam todos o mesmo produto de segurança de endpoints, configurado para atualizações automáticas; o CEDC e a CT usam a mesma região de nuvem para CAD/escalas; a CW e a CPN usam o mesmo integrador de TO, com acesso remoto a ambas. Eventos únicos que poderiam atingir vários setores de uma vez: uma atualização de endpoint defeituosa (hospital, despacho e banco simultaneamente); uma interrupção da região de nuvem (despacho e transporte); um comprometimento do integrador (água e energia). Recomendações: escalonar as atualizações de endpoint (um pequeno grupo canário primeiro, os consoles críticos de despacho por último); confirmar que a contingência com papel e rádio do CEDC não precisa da nuvem; exigir aprovação por sessão e credenciais separadas para o integrador em cada operador e incluí-lo no exercício conjunto. O ponto não é que esses fornecedores sejam ruins; é que o risco do condado é compartilhado e precisa ser analisado em conjunto.

### 31.5 Erros comuns e limites

- Tirar lições de detalhes vívidos, mas sem fonte.
- Tratar operações estatais direcionadas como a ameaça típica para todo operador.
- Ignorar falhas acidentais de dependências compartilhadas porque não há adversário envolvido.
- Ensinar técnicas em vez de premissas que falharam.

O exemplo da concentração em Calder evita esses erros: não usa nenhum detalhe de técnica, trata uma atualização acidental de endpoint com a mesma seriedade que um comprometimento do integrador e não supõe um agente estatal. Repetir afirmações sem fonte sobre a origem do Stuxnet seria o primeiro erro.

O quarto erro transformaria uma lição do TRITON numa descrição de como alcançar um controlador de safety.

### Exercícios — capítulo 31

**EX061 — Encontre a premissa.** *Objetivo:* abstrair um caso. *Entradas:* o caso da Ucrânia em 2015 (Capítulo 20). *Etapas:* declare duas premissas que falharam e uma premissa que se manteve e ajudou na recuperação, com apoio da fonte. *Evidência esperada:* três premissas. *Rubrica:* 3 = por exemplo, o acesso remoto/as estações dos operadores eram confiáveis (falhou), as centrais de atendimento continuariam acessíveis (falhou), a operação manual era possível (se manteve), cada uma ligada ao alerta da CISA; 2 = duas; 1 = uma; 0 = nada.

**EX062 — Mapa de concentração.** *Objetivo:* identificar dependências compartilhadas. *Entradas:* o levantamento de concentração de Calder no exemplo resolvido deste capítulo. *Etapas:* desenhe um mapa bipartido (fornecedores ↔ operadores), marque o fornecedor com o maior alcance e proponha uma medida por fornecedor. *Evidência esperada:* mapa e medidas. *Rubrica:* 3 = o produto de endpoint alcança três operadores em três setores (o maior), medidas específicas (atualizações escalonadas, independência da contingência, controles sobre o integrador); 2 = mapa sem medidas; 1 = lista; 0 = nada.

### Síntese do capítulo

Os casos avançados ensinam por meio das premissas que falharam: o que os operadores veem é real, os sistemas de safety são independentes, o risco é limitado pelos nossos próprios sistemas. Compare os casos por causa, caminho, consequência e premissa; gerencie o risco da cadeia de suprimentos e de concentração em conjunto entre os operadores; e transforme as lições em controles genéricos, e não em conhecimento de técnicas.

<!-- cyberabc:chapter-navigation:start ch-31 -->
### Continue estudando — capítulo 31 de 40

[← Capítulo 30](#ch-30) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 32 →](#ch-32)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-32"></a>

## Capítulo 32 — Infraestrutura crítica e segurança setorial: interfaces interdisciplinares

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) explicar como o direito e a regulação, a economia, a engenharia de safety, os fatores humanos e a comunicação pública moldam as decisões de segurança nos serviços críticos; (2) traduzir uma constatação técnica para advogados, responsáveis financeiros, clínicos, engenheiros e o público; (3) reconhecer quando um problema de segurança é na verdade um problema de incentivos ou organizacional; e (4) trabalhar entre disciplinas sem ultrapassar a sua competência. O capítulo se apoia nos Capítulos 10, 14, 19 e 28–31 e prepara a prática de campo (Capítulo 36) e o trabalho de conclusão.

### 32.1 Direito e regulação

Os serviços críticos são regulados. Exemplos consultados para este livro: a Diretiva NIS2 da UE estabelece obrigações de gestão de riscos e de notificação de incidentes para entidades essenciais e importantes ([NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/)); o DORA estabelece requisitos de risco de TIC para entidades financeiras ([DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)); na América do Norte, as normas de Critical Infrastructure Protection da NERC se aplicam ao sistema elétrico de grande porte ([NERC CIP](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx)); no setor de água dos EUA, o America's Water Infrastructure Act de 2018 exigiu avaliações de risco e resiliência e planos de resposta a emergências dos sistemas comunitários de água acima de um limiar de porte ([EPA, AWIA](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans)). Como profissional de segurança, você precisa saber que essas obrigações existem, onde encontrar o texto atual e quando envolver a assessoria jurídica — e não interpretá-las sozinho. A conformidade é um piso: atender a uma norma não prova que o serviço é resiliente.

### 32.2 Economia e incentivos

Grande parte da infraestrutura é operada de forma privada, mas a sua falha prejudica pessoas que não são suas clientes — uma **externalidade**. Os investimentos que protegem contra eventos raros competem com custos visíveis e de curto prazo, e o benefício (uma interrupção que não aconteceu) é invisível. A regulação, os seguros, os requisitos de compras e a divulgação pública são formas de mudar os incentivos. Reconhecer um problema de incentivos evita um erro comum: propor um controle tecnicamente excelente que nenhum detentor de orçamento tem motivo para financiar. O enquadramento de perda esperada e de pior evento crível do Capítulo 1 é a ponte para um público financeiro.

### 32.3 Engenharia de safety e fatores humanos

Os engenheiros de safety têm longa prática em analisar perigos, camadas independentes de proteção e gestão de mudanças (Capítulos 26 e 28). A segurança e a safety podem entrar em conflito — um bloqueio de conta que trava um operador numa emergência; um patch que invalida uma certificação de safety — e precisam ser conciliadas em conjunto. Os especialistas em fatores humanos estudam como as pessoas de fato trabalham: avalanches de alarmes, fadiga nos turnos da noite, contornos quando os procedimentos não se ajustam à realidade. O trabalho de Reason mostra os erros como consequências do projeto do sistema ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)). Um controle que os operadores não conseguem usar sob estresse será contornado (a aceitabilidade psicológica de Saltzer e Schroeder).

### 32.4 Comunicação

Públicos diferentes precisam de traduções diferentes da mesma constatação. Os **clínicos** precisam saber o efeito sobre o cuidado ao paciente e o que fazer de diferente. Os **engenheiros** precisam do mecanismo técnico e das restrições. O **financeiro** precisa dos custos, das perdas evitadas e das opções. Os **advogados** precisam dos fatos, das datas e das obrigações acionadas. O **público** precisa de informações honestas e tempestivas sobre o serviço e sobre o que deve fazer — sem detalhes que ajudem os atacantes. Porta-vozes acordados e modelos de mensagem pré-aprovados fazem parte da preparação para incidentes (a injeção do jornalista no Capítulo 30).

A constatação sobre o BMS do CVH é traduzida assim abaixo: uma verificação da ventilação para a liderança do centro cirúrgico, detalhes da VLAN e do intertravamento para a manutenção predial, cerca de £25.000 contra cirurgias canceladas para o financeiro e uma declaração de ausência de obrigações para o jurídico.

### 32.5 Exemplo resolvido: uma constatação, quatro públicos (sintético)

**Este caso é sintético.** Constatação: a ventilação do centro cirúrgico do CVH pode ser alterada a partir do BMS, que é alcançável pela rede corporativa com autenticação só por senha.

- *Liderança do centro cirúrgico:* "Um mau uso do sistema predial poderia reduzir as trocas de ar do centro cirúrgico. Até corrigirmos isso, a manutenção predial vai conferir as leituras da ventilação no início de cada lista cirúrgica, e vocês devem reportar imediatamente qualquer alarme."
- *Engenheiro da manutenção predial:* "Interface de administração do BMS alcançável a partir da VLAN corporativa; só senha. Proposta: allowlist para duas estações da manutenção predial, MFA, intertravamento de vazão mínima por fiação."
- *Financeiro:* "Custo de cerca de £25.000, pagamento único; trata um cenário cujo pior desfecho crível é o cancelamento de cirurgias por vários dias. As alternativas e os seus custos estão em anexo."
- *Proteção de dados e jurídico:* "Nenhum dado pessoal envolvido; nenhuma obrigação de notificação acionada pela constatação em si; vamos reavaliar se for detectada exploração."

### 32.6 Erros comuns e limites

- Dar pareceres jurídicos sem a assessoria jurídica.
- Propor controles sem um argumento de financiamento.
- Ignorar as consequências de safety ou clínicas dos controles de segurança.
- Uma única mensagem para todos os públicos.

O exemplo resolvido evita cada um: a mensagem ao jurídico diz o que foi conferido e quando será reavaliado; a mensagem ao financeiro dá um custo e o seu pior desfecho crível; a mensagem ao centro cirúrgico nomeia a verificação clínica; e quatro públicos recebem quatro mensagens. Um único e-mail técnico para todos teria falhado com a liderança do centro cirúrgico e com o financeiro.

### Exercícios — capítulo 32

**EX063 — Traduza para o conselho.** *Objetivo:* comunicar entre disciplinas. *Entradas:* o resultado do Laboratório 11 (o caminho cibernético aproximadamente dobra a probabilidade de perder a energia crítica no modelo sintético). *Etapas:* escreva uma nota de 120 palavras ao conselho do CVH com a constatação, a correção de engenharia proposta, o enquadramento de custos e os limites do modelo. *Evidência esperada:* a nota. *Rubrica:* 3 = linguagem simples, consequência para os pacientes, a correção restaura a independência, honesta sobre os números sintéticos e a não aleatoriedade do adversário; 2 = parcial; 1 = jargão; 0 = nada.

**EX064 — Conflito entre safety e segurança.** *Objetivo:* conciliar deveres. *Entradas:* uma política de bloquear as contas das IHMs depois de cinco logins falhos. *Etapas:* explique o risco de safety e proponha uma alternativa que atenda à finalidade de segurança. *Evidência esperada:* explicação e alternativa. *Rubrica:* 3 = operador bloqueado durante uma emergência; alternativas como console com acesso físico controlado e monitoramento, limitação de taxa sem bloqueio, alertas sobre as falhas, sobreposição de emergência com auditoria; 2 = uma; 1 = vago; 0 = nada.

### Síntese do capítulo

A segurança nos serviços críticos fica entre o direito, a economia, a safety, os fatores humanos e a comunicação. Saiba onde estão as obrigações e quando chamar a assessoria jurídica, reconheça os problemas de incentivos, concilie safety e segurança em conjunto, projete para pessoas sob estresse e traduza cada constatação para o público que precisa agir com base nela.

<!-- cyberabc:chapter-navigation:start ch-32 -->
### Continue estudando — capítulo 32 de 40

[← Capítulo 31](#ch-31) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 33 →](#ch-33)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-33"></a>

## Capítulo 33 — Métodos de pesquisa II

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) desenhar entrevistas e análise documental como métodos qualitativos, incluindo a aprovação ética e o consentimento; (2) codificar dados qualitativos com um livro de códigos e conferir a concordância entre codificadores; (3) tornar reprodutível uma análise quantitativa; e (4) combinar evidências qualitativas e quantitativas num desenho de métodos mistos. O capítulo se apoia no Capítulo 18 e prepara o projeto comparativo (Capítulo 34) e o trabalho de conclusão (Capítulos 35–40).

### 33.1 Métodos qualitativos

Muitas perguntas importantes na segurança de setores críticos tratam de pessoas e organizações: por que os operadores contornam um controle, como as decisões de incidentes foram tomadas, o que os profissionais acreditam que funciona. As **entrevistas semiestruturadas** seguem um roteiro de perguntas abertas, permitindo aprofundamentos. A **análise documental** examina planos, relatórios e políticas. As duas exigem **aprovação ética** da sua instituição quando envolvem pessoas, **consentimento informado** (os participantes conhecem a finalidade, o que será registrado e como será guardado, e podem desistir) e a proteção dos participantes e das suas organizações: nenhum detalhe que identifique uma pessoa ou exponha uma vulnerabilidade de um operador real deve aparecer na sua monografia. As anotações de entrevistas sobre fraquezas de segurança são dados sensíveis; guarde-as cifradas e apague-as no prazo previsto (Capítulo 14).

### 33.2 Codificação e concordância

A **codificação** atribui rótulos a trechos: "recurso ao papel", "dependência de fornecedor", "dono da decisão incerto". Um **livro de códigos** define cada código com regras de inclusão e exclusão e um exemplo. Para conferir a **confiabilidade**, duas pessoas codificam a mesma amostra de forma independente e medem a concordância. A concordância percentual bruta superestima a confiabilidade, porque parte da concordância acontece por acaso; o **kappa de Cohen** corrige isso: $\kappa = (p_o - p_e)/(1 - p_e)$, em que $p_o$ é a concordância observada e $p_e$ a concordância esperada por acaso a partir das frequências de rótulos de cada codificador. As discordâncias não são fracassos; discuti-las afia o livro de códigos.

### 33.3 Análise quantitativa reprodutível

Uma análise reprodutível mantém os dados brutos inalterados, faz todas as transformações em scripts, registra versões e sementes aleatórias e produz todo número do relatório a partir do código ([Sandve et al., 2013](https://doi.org/10.1371/journal.pcbi.1003285)). Os laboratórios deste livro seguem essas regras: sementes fixas, só a biblioteca padrão, saídas impressas reproduzidas no texto. Se uma simulação ou um modelo for usado, declare como ele foi conferido contra a realidade — a verificação e a validação de modelos de simulação são uma disciplina própria ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20)).

### 33.4 Métodos mistos

A evidência quantitativa diz **quanto**; a evidência qualitativa diz **como e por quê**. Um desenho de métodos mistos poderia contar, em 30 relatórios públicos de incidentes, quantos mencionam o recurso à operação manual (quantitativo) e depois entrevistar quatro operadores sobre o que faz a contingência manual funcionar (qualitativo). A combinação é mais forte que qualquer uma das partes, desde que cada parte seja bem feita e a integração — como uma informa a outra — seja explícita.

No desenho dos 30 relatórios, a ligação é fixada antes da coleta: qualquer condição de contingência que apareça em pelo menos cinco relatórios vira uma pergunta da entrevista.

No exemplo dos 30 relatórios, a contagem diz com que frequência os relatórios mencionam a contingência manual, e as entrevistas explicam por que a contingência às vezes falha, por exemplo porque a equipe não a praticou. Integrar significa que o roteiro de entrevista pergunta sobre as condições que a contagem revelou.

### 33.5 Exemplo resolvido: codificar relatórios de incidentes (dados sintéticos)

**Os dados são sintéticos.** Dois estudantes codificam 20 trechos de relatórios de incidentes quanto à presença do código "dono da decisão incerto". Eles concordam em 16 de 20 ($p_o = 0.80$). O estudante A aplicou o código a 8 trechos; o estudante B, a 6. Concordância por acaso: ambos "sim" $= (8/20)(6/20) = 0.12$; ambos "não" $= (12/20)(14/20) = 0.42$; $p_e = 0.54$. Kappa $= (0.80 - 0.54)/(1 - 0.54) = 0.26/0.46 \approx 0.57$ — concordância moderada. Os estudantes revisam as quatro discordâncias, descobrem que um deles codificou "decisão atrasada" como "dono incerto" mesmo quando o dono estava nomeado e apertam a definição: "aplica-se só quando o relatório declara ou mostra que os participantes não sabiam quem detinha a decisão".

### 33.6 Erros comuns e limites

- Entrevistar profissionais sem aprovação ética ou consentimento.
- Publicar detalhes identificáveis das fraquezas de operadores reais.
- Reportar a concordância percentual como confiabilidade.
- Etapas de análise feitas à mão e não registradas.
- "Métodos mistos" que são dois estudos separados, nunca integrados.

No exemplo de codificação, reportar 80 % de concordância em vez do kappa de 0,57 seria o terceiro erro. Entrevistar engenheiros da CRP sobre acesso remoto sem consentimento e aprovação seria o primeiro, e citar o gateway sem patch de um operador nomeado seria o segundo. Uma planilha editada à mão sem registro seria o quarto.

### Exercícios — capítulo 33

**EX065 — Calcule o kappa.** *Objetivo:* medir a confiabilidade. *Entradas:* dois codificadores, 40 trechos, concordam em 34; o codificador A aplicou o código 10 vezes, o codificador B, 12 vezes. *Etapas:* calcule $p_o$, $p_e$ e $\kappa$ e interprete. *Evidência esperada:* desenvolvimento e interpretação. *Rubrica:* 3 = $p_o = 0.85$; $p_e = 0.25 \times 0.30 + 0.75 \times 0.70 = 0.075 + 0.525 = 0.60$; $\kappa = 0.625$, concordância entre moderada e substancial, com a observação de que as escalas de interpretação são convenções; 2 = deslize aritmético; 1 = só $p_o$; 0 = nada.

**EX066 — Consentimento e proteção.** *Objetivo:* desenhar um trabalho qualitativo ético. *Entradas:* plano de entrevistar engenheiros de três operadores da CRP sobre práticas de acesso remoto. *Etapas:* escreva as informações de consentimento (cinco pontos) e três medidas de proteção de dados. *Evidência esperada:* listas. *Rubrica:* 3 = finalidade, participação voluntária/desistência, o que é registrado, armazenamento/retenção, como os resultados são anonimizados, mais cifração, pseudônimos, nenhum detalhe de vulnerabilidade nos produtos/revisão pelo anfitrião; 2 = parcial; 1 = genérico; 0 = nada.

### Síntese do capítulo

Os métodos qualitativos respondem ao como e ao por quê; eles precisam de aprovação ética, consentimento e proteção dos participantes e das organizações. Os livros de códigos e o kappa tornam a codificação confiável; os scripts, as sementes e as versões tornam a análise quantitativa reprodutível; os métodos mistos só são tão bons quanto a sua integração.

<!-- cyberabc:chapter-navigation:start ch-33 -->
### Continue estudando — capítulo 33 de 40

[← Capítulo 32](#ch-32) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 34 →](#ch-34)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-34"></a>

## Capítulo 34 — Projeto comparativo

### Objetivos de aprendizagem e conexão

Depois deste projeto, você consegue (1) comparar três ou mais opções contra critérios explícitos, com pesos e evidências; (2) testar quão sensível é a ordenação aos pesos; (3) apresentar uma comparação que um tomador de decisão possa contestar; e (4) reconhecer quando uma nota ponderada esconde uma consideração decisiva. O projeto se apoia nos Capítulos 1, 15, 23 e 24 e prepara a proposta do trabalho de conclusão (Capítulo 35). É a expressão central do resultado do curso: comparar métodos, avaliar evidências e projetar soluções defensáveis.

### 34.1 Comparação multicritério

As decisões sobre serviços críticos envolvem vários critérios que não compartilham uma unidade: redução da consequência, carga operacional, custo, tempo de implementação, força da evidência de que a opção funciona. A **análise de decisão multicritério** pontua cada opção em cada critério, pondera os critérios e os combina — no caso mais simples, como uma soma ponderada. O seu valor está menos no número final do que em tornar visíveis os critérios, as notas e os pesos, para que as pessoas possam discuti-los de forma produtiva.

Na avaliação do trabalho de conclusão sobre dispositivos sem suporte (Capítulo 39), o peso do custo é impresso ao lado de cada nota, e é assim que um leitor consegue ver que o gateway do fornecedor vence quando esse peso passa de 0,45.

### 34.2 Fazer isso com honestidade

Defina cada critério de modo que maior seja melhor (inverta custos e cargas). Pontue numa escala ancorada ("5 = elimina a pior consequência crível; 1 = nenhum efeito mensurável"). Registre a evidência por trás de cada nota (Capítulo 15). Defina os pesos *antes* de pontuar, de preferência com as partes interessadas, para evitar ajustar os pesos a uma opção favorita. Depois faça a **análise de sensibilidade**: varie os pesos e veja se a vencedora muda. Se ela só muda sob pesos implausíveis, a decisão é robusta; se pequenas mudanças a invertem, reporte que a decisão depende de um julgamento de valor e nomeie-o.

### 34.3 Quando uma nota não basta

Algumas considerações são **restrições**, e não critérios: uma obrigação legal, um requisito de safety, um nível mínimo de serviço. Uma opção que viola uma restrição é excluída, qualquer que seja a sua nota. Outras são **vetos** de pessoas com autoridade (a recusa de uma diretora clínica a uma opção que perturba o centro cirúrgico). Trate isso explicitamente antes de pontuar.

Para o CEDC, a exigência de um regulador de restauração em quatro horas é uma restrição (EX068), que exclui as opções que não conseguem demonstrá-la.

O veto de uma diretora clínica a uma opção que fecha o centro cirúrgico por uma semana é tratado da mesma forma.

### 34.4 Exemplo resolvido e Laboratório 13 (sintético)

**Este caso é sintético.** A CRP compara três opções de resiliência a ransomware para o CEDC em quatro critérios, com pesos 0,4, 0,2, 0,2, 0,2.

```python
# Lab 13 - weighted comparison of three options and weight sensitivity (synthetic scores, offline)
CRITERIA = ["consequence reduction", "operational burden (inverted)", "cost (inverted)", "evidence strength"]
W = [0.4, 0.2, 0.2, 0.2]
SCORES = {  # 1-5, higher is better
    "network segmentation project": [5, 2, 2, 4],
    "managed detection service":    [3, 4, 3, 3],
    "offline backups + restore drills": [4, 4, 4, 5],
}
def total(s, w): return sum(a * b for a, b in zip(s, w))
for name, s in SCORES.items():
    print(f"{name:33} {total(s, W):.2f}")
print("weight on consequence needed for segmentation to win:")
for wc in (0.4, 0.5, 0.6, 0.7, 0.8):
    rest = (1 - wc) / 3
    w = [wc, rest, rest, rest]
    best = max(SCORES, key=lambda k: total(SCORES[k], w))
    print(f"  w_consequence={wc:.1f} -> {best}")
```

Saída esperada:

```text
network segmentation project      3.60
managed detection service         3.20
offline backups + restore drills  4.20
weight on consequence needed for segmentation to win:
  w_consequence=0.4 -> offline backups + restore drills
  w_consequence=0.5 -> offline backups + restore drills
  w_consequence=0.6 -> offline backups + restore drills
  w_consequence=0.7 -> network segmentation project
  w_consequence=0.8 -> network segmentation project
```

Os backups com exercícios de restauração vencem sob os pesos acordados e continuam à frente até que a redução da consequência tenha entre 0,6 e 0,7 do peso total. O relatório, portanto, diz: "Recomendado: backups offline com exercícios de restauração. A recomendação só se inverte se a parceria der à redução da consequência mais de cerca de dois terços da decisão, caso em que a segmentação é preferida. As opções não são excludentes; a segmentação é a candidata mais forte para o segundo ano." Note o que as notas não capturam: os backups recuperam de um ransomware, mas não impedem o roubo de dados que muitas vezes o acompanha — uma consideração a declarar explicitamente, e não a esconder num número.

### 34.5 Produto do projeto

Um relatório comparativo de 2.500 palavras sobre uma pergunta da sua escolha dentro do caso de Calder ou de um tema público documentado (por exemplo, três abordagens de acesso remoto, três estratégias de backup, três opções de monitoramento): restrições, critérios com escalas ancoradas, evidência por nota, pesos definidos antecipadamente, análise de sensibilidade, recomendação com condições de reversão e limites.

Para a comparação do trabalho de conclusão sobre dispositivos sem suporte (Capítulo 39), esse peso é 0,45 no custo; abaixo dele, o isolamento com monitoramento vence; acima, vence o gateway do fornecedor.

Declare a condição de reversão em palavras, como faz o relatório do Laboratório 13: o peso em que a recomendação mudaria e o julgamento de valor que esse peso representa.

### 34.6 Erros comuns e limites

- Pontuar primeiro e escolher os pesos depois.
- Notas não ancoradas ("4 porque parece bom").
- Ignorar restrições e vetos.
- Apresentar um total ponderado como verdade objetiva.
- Tratar as opções como mutuamente excludentes quando elas podem ser combinadas.

O Laboratório 13 evita o primeiro ao fixar os pesos em 0,4, 0,2, 0,2, 0,2 antes de pontuar. O relatório também observa que a segmentação e os backups podem ser combinados, evitando o quinto erro. Uma nota 4 para a força da evidência precisa dos registros dos exercícios por trás dela; sem eles, é o segundo erro.

Apresentar 4,20 como prova seria o quarto.

### Exercícios — capítulo 34

**EX067 — Encontre o ponto de cruzamento.** *Objetivo:* localizar o ponto de reversão. *Entradas:* Laboratório 13. *Etapas:* calcule o peso exato da consequência em que a segmentação e os backups empatam, usando a regra da divisão igual para os outros pesos. *Evidência esperada:* dedução e valor. *Rubrica:* 3 = segmentação $5w + (2+2+4)(1-w)/3$, backups $4w + (4+4+5)(1-w)/3$; empate quando $w = 5(1-w)/3$, logo $w = 5/8 = 0.625$; 2 = busca numérica até 0,62–0,63; 1 = só a faixa 0,6–0,7; 0 = nada.

**EX068 — Acrescente uma restrição.** *Objetivo:* tratar um requisito não compensatório. *Entradas:* o regulador do CEDC exige restauração demonstrada em até 4 horas. *Etapas:* explique como isso muda a análise e qual evidência cada opção precisa fornecer. *Evidência esperada:* explicação. *Rubrica:* 3 = tratada como restrição, e não como critério; só se qualificam as opções que demonstram a restauração (backups com exercícios diretamente; segmentação/detecção não restauram, então precisam ser combinadas com uma capacidade de recuperação); 2 = tratada como peso alto; 1 = ignorada; 0 = nada.

### Síntese do capítulo

A comparação é a habilidade central do bacharelado: critérios explícitos, notas ancoradas, evidências, pesos definidos antecipadamente, análise de sensibilidade e condições de reversão declaradas. As restrições e os vetos vêm antes da pontuação, e um total ponderado é um argumento estruturado, e não um veredicto.

<!-- cyberabc:chapter-navigation:start ch-34 -->
### Continue estudando — capítulo 34 de 40

[← Capítulo 33](#ch-33) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 35 →](#ch-35)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-35"></a>

## Capítulo 35 — Proposta do trabalho de conclusão

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) escolher um tema de trabalho de conclusão que seja comparativo, viável, ético e útil; (2) escrever uma proposta com pergunta, contexto, método, plano de evidências, ética, riscos e cronograma; (3) definir com antecedência os critérios de sucesso e os produtos; e (4) obter as autorizações de que o seu projeto precisa. O capítulo se apoia nos Capítulos 18, 25, 30, 33 e 34 e inicia a sequência do trabalho de conclusão (Capítulos 35–40).

### 35.1 O que é um trabalho de conclusão de bacharelado

O trabalho de conclusão demonstra o resultado do curso: comparar teorias e métodos, avaliar evidências e projetar uma solução defensável para um problema de um setor crítico. Ele não é a construção de engenharia de um sistema completo (isso é o curso de engenharia) nem uma contribuição original ao conhecimento (isso é o doutorado). Um bom trabalho de conclusão de bacharelado pega um **problema de decisão real** — muitas vezes de uma organização anfitriã (Capítulo 36) ou de um tema público bem documentado —, compara **pelo menos três opções ou métodos** com critérios e evidências explícitos e termina com uma **recomendação e os seus limites**. Escala típica: cerca de 400 horas de trabalho ao longo de dois semestres, uma monografia de 10.000–12.000 palavras e uma apresentação.

### 35.2 Escolher um tema

Teste cada candidato contra cinco perguntas. **Comparativo?** Há alternativas reais a comparar? **Viável?** Você consegue obter as evidências no prazo — documentos, laboratórios, testes autorizados, entrevistas? **Ético e autorizado?** Ele precisa de aprovação ética, permissão do anfitrião, medidas de proteção de dados (Capítulos 10, 14, 33)? **Útil?** Alguém agiria com base na resposta? **Delimitado?** Você consegue dizer o que está fora do escopo? Os temas falham com mais frequência na viabilidade: "avaliar a segurança da rede elétrica nacional" não é um trabalho de conclusão; "comparar três abordagens de acesso remoto de fornecedores para uma pequena distribuidora, usando orientações públicas, um laboratório sintético e duas entrevistas com profissionais" é.

### 35.3 A proposta

1. **Título e pergunta** (Capítulo 18): população, variáveis, período, tipo de resposta.
2. **Contexto e motivação**: o serviço, a decisão, quem precisa dela.
3. **Literatura e fontes**: o que se sabe, com uma estratégia de busca registrada.
4. **Opções e critérios** (Capítulo 34): opções candidatas, restrições, critérios com escalas ancoradas, como os pesos serão definidos.
5. **Método e plano de evidências**: para cada critério, qual evidência e como obtê-la (documentos, medições de laboratório, testes autorizados, entrevistas).
6. **Ética e autorização**: aprovações necessárias, regras de engajamento, tratamento de dados.
7. **Riscos para o projeto**: acesso recusado, dados indisponíveis, ampliação do escopo — e as alternativas (por exemplo, dados sintéticos se o anfitrião retirar os seus dados).
8. **Critérios de sucesso e produtos**: o que existirá no fim e como será julgado.
9. **Cronograma**: marcos alinhados aos Capítulos 36–40.

### 35.4 Exemplo resolvido: o esboço de uma proposta (sintético)

**Esta proposta é sintética.** *Pergunta:* "Para um hospital de porte médio, qual de três abordagens para gerenciar dispositivos clínicos sem suporte — substituição acelerada, isolamento de rede com monitoramento ou gateways seguros gerenciados pelo fornecedor — melhor reduz a exposição dentro de um orçamento anual fixo, julgada pela redução da consequência, pela perturbação clínica, pelo custo e pela força da evidência?" *Contexto:* o CVH (anfitrião sintético) tem dispositivos de imagem e de laboratório sem suporte (Laboratório 2). *Fontes:* orientações públicas sobre segurança de dispositivos médicos e de TO, o relatório do NAO sobre o WannaCry, metas de desempenho setoriais. *Método:* um inventário sintético de 120 dispositivos construído a partir de categorias publicadas; um modelo de laboratório da exposição sob cada opção; duas entrevistas com engenheiros clínicos (aprovação ética solicitada). *Ética:* nenhum dado real de dispositivos; entrevistas anonimizadas; revisão dos produtos pelo anfitrião. *Riscos:* entrevistas recusadas → apoiar-se em documentos e declarar a lacuna. *Critérios de sucesso:* comparação com análise de sensibilidade e condições de reversão; recomendação defendida na apresentação. *Cronograma:* proposta aprovada na semana 4; coleta de evidências nas semanas 5–14; análise nas semanas 15–20; rascunho da monografia na semana 24; apresentação na semana 28.

### 35.5 Erros comuns e limites

- Temas só descritivos, sem comparação.
- Planos de evidências que supõem um acesso que você ainda não tem.
- Nenhuma alternativa quando um anfitrião desiste.
- Critérios de sucesso escritos depois dos resultados.

A proposta resolvida evita esses erros: compara três opções, solicita entrevistas, mas tem uma alternativa documental, e fixa os critérios de sucesso antes da coleta de evidências.

Cada erro tem um sintoma típico. Um tema como "o estado da segurança dos dispositivos hospitalares" produz uma descrição sem nada a recomendar. Um plano de evidências que supõe os dados do anfitrião antes de ele concordar desmorona na sexta semana. Um projeto sem alternativa trava quando um entrevistado desiste. Critérios de sucesso escritos depois dos resultados sempre parecem cumpridos, e é por isso que a proposta resolvida os fixa na semana quatro.

### Exercícios — capítulo 35

**EX069 — Triagem de temas.** *Objetivo:* aplicar os cinco testes. *Entradas:* três temas candidatos: (a) "A IA é boa para a segurança?"; (b) "Comparar três métodos para detectar dados falsos de sensores num modelo de reservatório de água, usando um conjunto de dados sintético"; (c) "Testar o firewall da minha empresa de água local". *Etapas:* aplique as cinco perguntas a cada um e escolha. *Evidência esperada:* tabela e escolha. *Rubrica:* 3 = (a) não delimitado nem comparativo como está formulado; (b) viável, comparativo, ético; (c) não autorizado e antiético — rejeitar; escolher (b); 2 = escolha certa, raciocínio fraco; 1 = escolha errada; 0 = nada.

**EX070 — Plano de evidências.** *Objetivo:* ligar os critérios às evidências. *Entradas:* o esboço de proposta resolvido deste capítulo. *Etapas:* para cada um dos quatro critérios, declare a evidência, a sua fonte e uma ameaça à sua validade. *Evidência esperada:* quatro linhas. *Rubrica:* 3 = evidência específica (saída do modelo de exposição do laboratório, dados de entrevistas sobre a perturbação, custos publicados, graduação da qualidade das fontes) com as ameaças à validade correspondentes; 2 = três; 1 = vago; 0 = nada.

### Síntese do capítulo

Um trabalho de conclusão de bacharelado responde a um problema de decisão real comparando opções com evidências e terminando numa recomendação delimitada. Uma boa proposta fixa a pergunta, os critérios, o plano de evidências, a ética, os riscos, os critérios de sucesso e o cronograma antes de o trabalho começar.

<!-- cyberabc:chapter-navigation:start ch-35 -->
### Continue estudando — capítulo 35 de 40

[← Capítulo 34](#ch-34) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 36 →](#ch-36)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-36"></a>

## Capítulo 36 — Prática de campo ou comunitária

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) preparar-se para um estágio com um operador de serviço crítico ou uma organização comunitária, incluindo acordos sobre escopo, confidencialidade e supervisão; (2) trabalhar de forma segura e útil num ambiente operacional como aprendiz; (3) manter um diário reflexivo de prática; e (4) produzir resultados que sirvam ao anfitrião sem expô-lo. O capítulo se apoia nos Capítulos 10, 14, 29, 32 e 35 e fornece evidências para o trabalho de conclusão.

### 36.1 Por que a prática importa

Os serviços críticos se aprendem no local: o cheiro de uma estação de bombeamento, o ritmo de uma troca de turno na sala de controle, a forma como os clínicos de fato usam os dispositivos. A prática de campo — um estágio com um operador, um regulador ou uma equipe de segurança, ou a prática comunitária, como ajudar uma pequena instituição de caridade, escola ou clínica a melhorar a segurança básica — testa o seu conhecimento contra a realidade e dá ao seu trabalho de conclusão evidências fundamentadas. Ela também ensina os comportamentos profissionais que nenhum laboratório ensina: ouvir primeiro, perguntar antes de tocar e guardar confidências.

### 36.2 O acordo de estágio

Antes de começar, acorde por escrito com o anfitrião e a sua universidade: o **supervisor** no local e o orientador acadêmico; as **atividades** permitidas (observação, revisão de documentos, tarefas autorizadas) e proibidas (qualquer alteração em sistemas em operação sem supervisão; qualquer teste sem RoE escritas); a **confidencialidade** — o que você pode registrar, o que pode levar embora, e que todo trabalho acadêmico é revisado pelo anfitrião antes da entrega; a **proteção de dados**; a integração de **saúde e segurança** (os locais de TO têm perigos físicos); e o que acontece se você descobrir algo grave (escalar imediatamente ao seu supervisor no local, e não aos seus colegas).

### 36.3 Trabalhar como aprendiz no local

A maior parte do seu valor como estudante vem de **olhos novos e tempo**: documentar o que a equipe experiente já não percebe, organizar um inventário, redigir um procedimento, comparar a prática atual com as orientações públicas. Não julgue antes de entender — uma "má prática" pode ser um contorno para uma restrição real (o login compartilhado da sala de controle do Capítulo 13). Pergunte por quê. Registre as suas observações de forma factual, separe-as da interpretação e confira-as com a pessoa envolvida.

Na entrada de diário da CW, os telefonemas dos operadores sobre leituras estranhas pareciam má prática até o supervisor explicar que a ferramenta de tíquetes é lenta à noite; a folha de papel de "consulta de sensor" do estudante funciona com essa restrição.

### 36.4 Prática comunitária

As pequenas organizações que apoiam comunidades — um banco de alimentos, uma clínica rural, um serviço voluntário de ambulâncias — muitas vezes dependem de serviços críticos e têm pouca capacidade de segurança. Uma contribuição estruturada e de baixo risco: uma lista de ativos, uma revisão de contas e de backups contra uma linha de base publicada simples, uma folha de contatos de incidentes de uma página e uma sessão curta com a equipe. As mesmas regras de autorização e confidencialidade se aplicam; o seu dever de cuidado é maior, e não menor, quando a organização não consegue julgar o seu conselho.

Para um serviço voluntário de ambulâncias, o acordo escrito poderia listar os quatro produtos, declarar que nenhum sistema será alterado pelo estudante e nomear quem guarda a folha de contatos depois.

### 36.5 Diário reflexivo

Mantenha um diário semanal com quatro títulos: **o que eu fiz**, **o que eu observei**, **o que me surpreendeu e por quê**, **o que eu faria diferente**. A reflexão transforma a experiência em aprendizado e fornece evidências para a avaliação. Mantenha o diário sanitizado desde o início: nenhum nome de sistema, endereço, credencial ou dado pessoal — escreva "o gateway de acesso remoto", e não o seu nome de host.

A entrada da CW escreve "7 de 42 estações remotas", e não os nomes das estações, para que possa ser mostrada a um avaliador sem edição.

A entrada da CW foi escrita depois do segundo turno da noite, enquanto a explicação sobre a lentidão dos tíquetes estava fresca, e ficou no diário do próprio estudante, e não na pasta compartilhada do anfitrião.

### 36.6 Exemplo resolvido: a entrada de diário de uma semana (sintético)

**Esta entrada é sintética.** *Fiz:* acompanhei a sala de controle da CW por dois turnos da noite; ajudei a reconciliar o inventário de telemetria com a lista de locais. *Observei:* 7 de 42 estações remotas do inventário não tinham versão de firmware registrada; os operadores telefonam para o técnico da estação quando uma leitura parece errada, em vez de abrir um tíquete. *Surpreendeu-me:* as verificações informais dos operadores pegam as falhas de sensores mais rápido que o sistema de alarmes — mas não deixam registro. *Diferente:* supus que os tíquetes ausentes eram descuido; o supervisor explicou que a ferramenta de tíquetes é lenta à noite. Proposta para o anfitrião: uma folha de papel de "consulta de sensor" com dois campos, transcrita toda manhã, para que o conhecimento vire evidência. Aprovada pelo supervisor no local para inclusão no trabalho acadêmico em forma sanitizada.

### 36.7 Erros comuns e limites

- Começar sem um acordo escrito.
- Tirar fotografias, arquivos ou anotações que o anfitrião não aprovou.
- Julgar a prática antes de entender as restrições.
- Diários reflexivos que descrevem a atividade, mas não o aprendizado.

A entrada de diário da CW evita os quatro: o estágio tinha um acordo, a proposta da folha de papel foi aprovada antes da inclusão, o estudante perguntou por que faltavam tíquetes antes de julgar, e a entrada registra uma premissa que mudou. O EX072 mostra o segundo erro na sua forma mais perigosa: uma credencial registrada.

Na CW, o supervisor aprovou a proposta da folha de papel em forma sanitizada; as lacunas de firmware das estações nomeadas ficaram no local.

### Exercícios — capítulo 36

**EX071 — Redija o acordo.** *Objetivo:* montar um estágio seguro. *Entradas:* um estágio de quatro semanas com a equipe de TI do CEDC. *Etapas:* escreva os títulos do acordo, com uma cláusula específica em cada um. *Evidência esperada:* o rascunho. *Rubrica:* 3 = supervisores, atividades permitidas/proibidas (sem acesso a alterações no CAD em operação), confidencialidade e revisão pelo anfitrião, proteção de dados (gravações de chamadas excluídas), segurança, caminho de escalonamento; 2 = cláusulas genéricas; 1 = faltam itens-chave; 0 = nada.

**EX072 — Sanitize um diário.** *Objetivo:* proteger o anfitrião. *Entradas:* "Terça: fiz login em vpn.caldermutual.example como jsmith/Summer2026 para olhar o gateway SWIFT 10.4.2.8; notei que ele ainda roda a versão 7." *Etapas:* reescreva de modo que seja seguro entregar e continue útil. *Evidência esperada:* a entrada reescrita e três coisas removidas. *Rubrica:* 3 = remove o nome de host, as credenciais, o endereço, a pessoa e a versão exata, mantém o aprendizado ("observei um componente desatualizado do gateway de pagamentos; levei ao supervisor"); também observa que a credencial nunca deveria ter sido registrada e precisa ser reportada para troca; 2 = remove a maior parte; 1 = parcial; 0 = nada.

### Síntese do capítulo

A prática de campo e comunitária ancora o curso na realidade. Acorde por escrito o escopo, a confidencialidade, a supervisão e o escalonamento; contribua com olhos novos e tempo; entenda as restrições antes de julgar; mantenha um diário reflexivo sanitizado; e deixe o anfitrião revisar tudo o que sair do local.

<!-- cyberabc:chapter-navigation:start ch-36 -->
### Continue estudando — capítulo 36 de 40

[← Capítulo 35](#ch-35) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 37 →](#ch-37)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-37"></a>

## Capítulo 37 — Seminário de revisão de evidências

### Objetivos de aprendizagem e conexão

Depois deste seminário, você consegue (1) revisar criticamente um estudo, relatório ou alegação de fornecedor sobre segurança usando uma lista estruturada; (2) quantificar a incerteza de resultados de amostras pequenas com intervalos de confiança; (3) dar e receber uma revisão por pares que melhore o trabalho; e (4) decidir quanto peso uma evidência merece no seu trabalho de conclusão. O seminário se apoia nos Capítulos 15, 18, 27 e 33 e prepara a implementação e a avaliação do trabalho de conclusão (Capítulos 38–39).

### 37.1 Uma lista de revisão

Para qualquer estudo, relatório ou alegação: **Pergunta** — o que exatamente se alega? **Dados** — de onde vieram, quantos, quão representativos? **Método** — poderia ser repetido; houve uma comparação ou um controle? **Resultados** — as incertezas são reportadas; os números fecham? **Validade** — construto, interna, externa, confiabilidade (Capítulo 18)? **Interesses** — quem financiou ou produziu o trabalho, e o que preferiria encontrar? **Limites** — o trabalho os declara, e as suas conclusões ficam dentro deles? Na segurança, as fraquezas comuns incluem a avaliação em dados irrealistas, o desprezo pela taxa de base e resultados que não se transferem para ambientes reais ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp); [Sommer and Paxson, 2010](https://doi.org/10.1109/SP.2010.25)). Na detecção de anomalias em séries temporais, Kim e colegas mostraram que um protocolo de avaliação popular pode fazer até notas aleatórias parecerem fortes ([Kim et al., 2022](https://ojs.aaai.org/index.php/AAAI/article/view/20680)).

### 37.2 Amostras pequenas e intervalos

A evidência dos serviços críticos muitas vezes vem de poucas observações: cinco exercícios de restauração, vinte exercícios, uma dúzia de incidentes. Uma estimativa pontual ("85% dos exercícios cumpriram o objetivo") esconde o quanto ela é incerta. Um **intervalo de confiança** dá uma faixa de valores plausíveis. Duas abordagens comuns para uma proporção: o **bootstrap**, que reamostra os dados observados muitas vezes ([Efron, 1979](https://doi.org/10.1214/aos/1176344552)), e o **intervalo de escore de Wilson**, uma fórmula que se comporta bem para amostras pequenas e proporções perto de 0 ou de 1 ([Wilson, 1927](https://doi.org/10.1080/01621459.1927.10502953)). O bootstrap é geral, mas se comporta mal em tamanhos pequenos e perto dos limites — ele nunca consegue produzir um valor acima do máximo observado, então, com 4 sucessos em 5, pode sugerir um limite superior de 100%.

### 37.3 Exemplo resolvido e Laboratório 14 (sintético)

**Este caso é sintético.** O CEDC fez 20 exercícios de restauração; 17 cumpriram o objetivo de 4 horas. Um operador menor fez 5; 4 o cumpriram.

```python
# Lab 14 - bootstrap confidence interval for a restore-drill success rate (synthetic, seed 14, offline)
import random
random.seed(14)
drills = [1] * 17 + [0] * 3          # 20 restore drills, 17 met the 4-hour objective
obs = sum(drills) / len(drills)
boots = sorted(sum(random.choice(drills) for _ in drills) / len(drills) for _ in range(10_000))
lo, hi = boots[249], boots[9749]
print(f"observed success = {obs:.2f}; 95% bootstrap interval = [{lo:.2f}, {hi:.2f}]")
small = [1, 1, 1, 0, 1]
boots = sorted(sum(random.choice(small) for _ in small) / len(small) for _ in range(10_000))
print(f"with only 5 drills (4 met): [{boots[249]:.2f}, {boots[9749]:.2f}]")
from math import sqrt
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d; h = z * sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
print("Wilson 95%% for 17/20: [%.2f, %.2f]; for 4/5: [%.2f, %.2f]" % (*wilson(17, 20), *wilson(4, 5)))
```

Saída esperada:

```text
observed success = 0.85; 95% bootstrap interval = [0.70, 1.00]
with only 5 drills (4 met): [0.40, 1.00]
Wilson 95% for 17/20: [0.64, 0.95]; for 4/5: [0.38, 0.96]
```

Os dois métodos dizem, em substância, a mesma coisa: 17 de 20 é compatível com uma taxa real de sucesso em qualquer ponto entre cerca de dois terços e cerca de 95%; 4 de 5 é compatível com qualquer coisa entre menos de 40% e quase sempre. O limite superior de 1,00 do bootstrap é um artefato de reamostrar dados que não contêm nenhum valor acima de 1; o intervalo de Wilson é a melhor escolha aqui. Para o conselho, a mensagem é: "temos evidências boas, mas não conclusivas, de que as restaurações costumam cumprir as quatro horas; uma falha em cada quatro não nos surpreenderia". Cinco exercícios não conseguem sustentar uma afirmação de confiabilidade.

### 37.4 Revisão por pares

Os grupos do seminário trocam os capítulos de evidências dos trabalhos de conclusão. Uma revisão útil declara o que o trabalho afirma, o que é convincente, os dois ou três problemas mais importantes (cada um com uma correção sugerida) e os pontos menores. Revise o trabalho, e não a pessoa; seja específico ("a afirmação sobre o tempo de restauração se apoia num único exercício num ambiente de teste; você pode acrescentar as condições do exercício e um intervalo?"). Os autores respondem ponto a ponto: aceito e alterado, ou recusado com os motivos.

Ao comentário sobre o tempo de restauração, por exemplo: "Acrescentei as condições do exercício; não é possível um intervalo a partir de um único exercício, então a afirmação agora está declarada como uma única observação."

### 37.5 Erros comuns e limites

- Reportar uma proporção sem o seu tamanho de amostra ou intervalo.
- Tratar os benchmarks dos fornecedores como evidência independente.
- Revisões que só elogiam ou só atacam.
- Ignorar como os protocolos de avaliação podem inflar os resultados.

O Laboratório 14 mostra o primeiro: "85 %" sem "de 20" e sem um intervalo esconde que a taxa real pode ser de 64 %. O próprio benchmark de um fornecedor de detectores (EX074) é o segundo. Uma revisão que diz só "ótimo trabalho" não ajuda ninguém. O quarto é o argumento de Kim e colegas sobre os protocolos de avaliação.

"A taxa de detecção se apoia nos 17 de 20 do Laboratório 14" nomeia a evidência; "os resultados parecem otimistas" não nomeia.

### Exercícios — capítulo 37

**EX073 — Quantos exercícios?** *Objetivo:* relacionar o tamanho da amostra com a precisão. *Entradas:* a função de Wilson do Laboratório 14. *Etapas:* calcule o intervalo de Wilson de 95% para 34/40 e 85/100 e comente como a evidência se acumula. *Evidência esperada:* dois intervalos e um comentário. *Rubrica:* 3 = aproximadamente [0,71, 0,93] e [0,77, 0,91], com a largura encolhendo aproximadamente com a raiz quadrada de n; recomenda um programa de exercícios; 2 = só os intervalos; 1 = um; 0 = nada.

**EX074 — Revise uma alegação.** *Objetivo:* aplicar a lista. *Entradas:* um folheto de fornecedor (sintético): "O nosso detector de anomalias de TO alcançou 99,7% de acurácia num conjunto de dados público de um testbed de água." *Etapas:* aplique a lista e liste quatro perguntas a fazer ao fornecedor. *Evidência esperada:* revisão e perguntas. *Rubrica:* 3 = a acurácia engana sob desbalanceamento (Capítulo 27), realismo e transferência do testbed, protocolo de avaliação, interesses; perguntas sobre precisão/revocação no limiar de operação, resultados de implantação real, alarmes falsos por dia, avaliação independente; 2 = parcial; 1 = genérico; 0 = nada.

### Síntese do capítulo

A revisão de evidências é ceticismo estruturado: pergunta, dados, método, resultados, validade, interesses e limites. Reporte os resultados de amostras pequenas com intervalos — Wilson para proporções — e deixe a revisão por pares melhorar o trabalho sendo específica, priorizada e respeitosa.

<!-- cyberabc:chapter-navigation:start ch-37 -->
### Continue estudando — capítulo 37 de 40

[← Capítulo 36](#ch-36) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 38 →](#ch-38)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-38"></a>

## Capítulo 38 — Implementação do trabalho de conclusão

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) executar o plano do trabalho de conclusão controlando o escopo e registrando as decisões; (2) coletar e gerenciar evidências de modo que todo resultado seja rastreável até a sua fonte; (3) construir um modelo ou laboratório pequeno e reprodutível que sustente a sua comparação; e (4) lidar com contratempos — acesso perdido, resultados surpreendentes — com honestidade. O capítulo se apoia nos Capítulos 25, 30, 34, 35 e 37 e prepara a avaliação (Capítulo 39).

### 38.1 Trabalhar segundo um plano

A implementação transforma a proposta (Capítulo 35) em evidências. Mantenha três documentos vivos. Um **diário do projeto** (data, o que você fez, o que decidiu e por quê). Um **registro de evidências** (item, fonte, data, tipo, como foi obtido, onde está guardado, qual critério sustenta — Capítulo 15). Um **registro de mudanças** para qualquer desvio da proposta, com a concordância do seu orientador. A ampliação do escopo é a falha mais comum dos trabalhos de conclusão: perguntas novas são interessantes, mas cada uma precisa substituir algo ou esperar pelos "trabalhos futuros".

No ponto de controle da semana 14, abaixo, o registro de mudanças declara o que substituiu a segunda entrevista recusada, uma revisão documental de duas fontes públicas de orientação, e o custo para a validade: a contribuição dos profissionais agora se apoia numa única entrevista.

### 38.2 Construir o modelo de apoio

A maioria dos trabalhos de conclusão de bacharelado precisa de um pequeno artefato: um modelo de exposição, uma simulação de dependências, uma comparação de detectores, um conjunto de dados codificado. Construa-o com os hábitos dos laboratórios: ferramentas padrão, sementes fixas, scripts em vez de etapas manuais, saídas guardadas com o hash do script, e **testes** que confiram o modelo em casos com respostas conhecidas antes de confiar nele em casos novos (Capítulo 8). Documente o que o modelo deixa de fora. Um modelo que reproduz um caso simples calculado à mão e declara as suas premissas vale mais do que um modelo elaborado que ninguém consegue conferir.

### 38.3 Coletar evidências de pessoas e anfitriões

As entrevistas seguem o protocolo aprovado e o consentimento (Capítulo 33). Os documentos do anfitrião são tratados segundo o acordo de estágio (Capítulo 36). Tudo o que diz respeito às vulnerabilidades de um operador real fica guardado com segurança e só aparece na monografia de forma sanitizada e aprovada pelo anfitrião. Se o acesso for retirado, use a alternativa da sua proposta e registre a mudança; não substitua dados por palpites em silêncio.

No ponto de controle da semana 14, a semente (38) e o hash do script de inventário entraram no registro no dia em que o script foi rodado.

No trabalho de conclusão sobre dispositivos sem suporte, as anotações das entrevistas são pseudonimizadas no mesmo dia, guardadas cifradas e apagadas no prazo do termo de consentimento. Se o anfitrião retirar a sua lista de dispositivos, o inventário sintético da proposta a substitui, e o registro de mudanças diz isso.

### 38.4 Resultados surpreendentes e negativos

Os resultados que contradizem a sua expectativa também são evidência. Se os exercícios de restauração no seu modelo de laboratório mostrarem que a opção que você esperava que vencesse não consegue cumprir o objetivo, reporte isso e investigue por quê — talvez uma dependência que você não modelou. Não ajuste os parâmetros até que o resultado "pareça certo"; se mudar um parâmetro, registre o motivo e mostre os dois resultados. Constatações negativas honestas estão entre os produtos mais úteis que um trabalho de conclusão pode gerar para um anfitrião.

O gateway do fornecedor foi o que menos reduziu a exposição dos dispositivos de imagem, porque eles também aceitam conexões do arquivo de imagens, que o gateway não medeia; o estudante manteve esse resultado e modelou controles do lado do arquivo como uma variante.

### 38.5 Exemplo resolvido: um ponto de controle da implementação (sintético)

**Este ponto de controle é sintético.** Semana 14 do trabalho de conclusão sobre dispositivos sem suporte (Capítulo 35). *Feito:* inventário sintético de 120 dispositivos construído a partir de categorias publicadas (script `make_inventory.py`, semente 38, hash registrado); modelo de exposição para três opções, com testes que reproduzem um caso de 5 dispositivos resolvido à mão; uma entrevista concluída, uma recusada. *Alterado:* a segunda entrevista é substituída por uma revisão documental de duas fontes públicas de orientação (registro de mudanças aprovado pelo orientador; nota de validade: a perspectiva dos profissionais agora se apoia numa única entrevista). *Surpresa:* a opção do gateway do fornecedor foi a que menos reduziu a exposição dos dispositivos de imagem, porque esses dispositivos também aceitam conexões do arquivo de imagens, que o gateway não medeia. Em vez de tratar isso como um erro, o estudante modela os controles do lado do arquivo como uma variante e registra a constatação. *Próximo:* análise de sensibilidade dos pesos; graduação das evidências; rascunho do capítulo de resultados.

### 38.6 Erros comuns e limites

- Perder a ligação entre os resultados e as evidências por trás deles.
- Etapas de análise manuais que não podem ser repetidas.
- Ajustar um modelo até ele concordar com as expectativas.
- Mudanças silenciosas de escopo ou de método.

O ponto de controle da semana 14 evita cada um: o script de inventário tem semente e hash, o modelo é testado num caso resolvido à mão, a surpresa do gateway é mantida e a substituição da entrevista é registrada. Mudar os parâmetros do gateway do fornecedor até a exposição dos dispositivos de imagem parecer menor teria sido o terceiro erro.

No ponto de controle, o hash do make_inventory.py e o registro de mudanças aprovado pelo orientador foram ambos escritos no próprio dia, e não reconstruídos na hora da monografia.

### Exercícios — capítulo 38

**EX075 — Registro de evidências.** *Objetivo:* tornar a rastreabilidade concreta. *Entradas:* o ponto de controle da semana 14 deste capítulo. *Etapas:* escreva cinco linhas do registro de evidências com todos os campos. *Evidência esperada:* tabela. *Rubrica:* 3 = cinco linhas completas (saída do script de inventário com hash, resultados dos testes do modelo, referência às anotações da entrevista, dois documentos de orientação), cada uma ligada a um critério; 2 = faltam campos; 1 = lista; 0 = nada.

**EX076 — Reporte uma surpresa.** *Objetivo:* lidar com honestidade com resultados inesperados. *Entradas:* a constatação sobre o gateway do ponto de controle da semana 14. *Etapas:* escreva um parágrafo de resultados de 150 palavras que reporte a constatação, a sua causa, a variante testada e os seus limites. *Evidência esperada:* parágrafo. *Rubrica:* 3 = constatação clara, mecanismo, resultado da variante reportado separadamente, limites (inventário sintético, um único modelo), sem exagero; 2 = parcial; 1 = esconde ou minimiza a surpresa; 0 = nada.

### Síntese do capítulo

A implementação é uma coleta disciplinada de evidências: registre as decisões, registre as evidências, registre as mudanças, construa modelos pequenos, testados e reprodutíveis, proteja os dados do anfitrião e dos participantes e reporte as surpresas como constatações. A credibilidade do trabalho de conclusão se apoia no rastro de cada afirmação até a sua evidência.

<!-- cyberabc:chapter-navigation:start ch-38 -->
### Continue estudando — capítulo 38 de 40

[← Capítulo 37](#ch-37) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 39 →](#ch-39)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-39"></a>

## Capítulo 39 — Avaliação do trabalho de conclusão

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) avaliar os resultados do seu trabalho de conclusão contra os critérios de sucesso fixados na proposta; (2) realizar verificações de sensibilidade e de robustez da sua comparação; (3) declarar as limitações de forma específica, com a sua provável direção de efeito; e (4) buscar uma revisão independente e responder a ela antes da monografia final. O capítulo se apoia nos Capítulos 34, 37 e 38 e prepara a monografia e a apresentação (Capítulo 40).

### 39.1 Contra os critérios que você definiu

A avaliação começa pelos critérios de sucesso da proposta (Capítulo 35). Eles foram cumpridos, parcialmente cumpridos ou não cumpridos? Reporte cada um com honestidade e com evidências. Depois avalie a própria **comparação**: as notas são sustentadas pelo registro de evidências; outra pessoa, usando as suas escalas ancoradas, daria notas semelhantes (pergunte a alguém); alguma restrição excluiu uma opção?

Houve uma entrevista e a segunda foi substituída por documentos, então o critério é reportado como parcialmente cumprido, e não descartado em silêncio.

Pedir a uma segunda pessoa que pontue duas opções com as suas escalas ancoradas é uma verificação rápida de confiabilidade; se as notas dela diferirem em mais de um ponto em qualquer critério, as suas âncoras precisam de uma redação mais clara antes da monografia.

### 39.2 Sensibilidade e robustez

Rode de novo a sua comparação sob variações plausíveis: pesos diferentes (Laboratório 13), evidências pessimistas e otimistas (a autonomia reduzida à metade do Capítulo 22), premissas alternativas do modelo (a variante do arquivo de imagens do Capítulo 38). Uma recomendação **robusta** se mantém na maioria das variações; uma **frágil** depende de uma premissa específica, que você precisa nomear. Apresente o resultado numa tabela curta: variação, vencedora, comentário.

Na avaliação resolvida, as variações além dos pesos acordados são um peso de custo de 0,4, um peso de custo de 0,6, controles do lado do arquivo acrescentados ao gateway e evidências pessimistas para o isolamento.

A avaliação resolvida mostra um resultado frágil: o gateway vence quando o peso do custo passa de 0,45, e a substituição acelerada vence quando se supõe que o monitoramento do isolamento não funciona. As duas coisas são nomeadas na conclusão como condições de reversão, para que o leitor veja em qual julgamento de valor e em qual premissa a recomendação se apoia.

### 39.3 Limitações com direção

"A amostra era pequena" é uma limitação fraca. Uma limitação útil diz **o quê**, **por que importa** e **em que direção** ela provavelmente enviesa o resultado. Por exemplo: "O modelo de exposição supõe que todo dispositivo sem suporte é igualmente explorável; na prática, os dispositivos próximos da internet estão mais expostos, então o modelo provavelmente *subestima* o benefício do isolamento para os dispositivos de imagem." As limitações com direção permitem que os leitores ajustem as suas conclusões, em vez de descartá-las.

A única entrevista provavelmente subestima a perturbação clínica do isolamento; o modelo de exposição, ao ignorar a escolha de alvos pelo atacante, provavelmente subestima o valor de remover primeiro os dispositivos mais expostos; a direção do inventário sintético é desconhecida.

Quando a direção for genuinamente desconhecida, como no inventário sintético, diga isso explicitamente, em vez de deixar a limitação sem direção por omissão.

### 39.4 Revisão independente

Antes de a monografia ficar pronta, peça a alguém de fora do seu projeto — um colega do seminário (Capítulo 37), o seu supervisor no anfitrião, um acadêmico não envolvido — que revise o capítulo de avaliação. Registre os pontos levantados e as suas respostas. A independência é o elo mais fraco da maioria das evidências (Capítulo 15); o trabalho de conclusão é onde você pratica fortalecê-la.

A pergunta do revisor foi o que acontece se os alertas do monitoramento não forem revisados.

Na avaliação resolvida, o ponto do revisor sobre o monitoramento sem pessoal mudou a tabela principal: a variação pessimista virou um resultado de destaque, e a recomendação tornou-se condicional. Registre o papel e a independência do revisor ao lado de cada ponto, para que um avaliador possa julgar quanto peso a revisão carrega.

### 39.5 Exemplo resolvido: tabela de avaliação (sintético)

**Esta avaliação é sintética.** Trabalho de conclusão sobre dispositivos sem suporte:

| Critério de sucesso (da proposta) | Resultado | Evidência |
|---|---|---|
| Comparação de três opções com escalas ancoradas | Cumprido | Linhas 1–14 do registro de evidências |
| Análise de sensibilidade com condições de reversão | Cumprido | O isolamento vence, a menos que o peso do custo seja > 0,45 |
| Contribuição dos profissionais sobre a perturbação clínica | Parcialmente cumprido | Uma entrevista; a segunda substituída por documentos |
| Recomendação defendida com limites | Cumprido (apresentação pendente) | Rascunho do capítulo 6 |

| Variação | Vencedora | Comentário |
|---|---|---|
| Pesos acordados | Isolamento com monitoramento | Linha de base |
| Peso de custo 0,4 | Isolamento com monitoramento | Robusto |
| Peso de custo 0,6 | Gateway do fornecedor | Frágil acima de 0,45 |
| Controles do lado do arquivo acrescentados ao gateway | Isolamento (por pouco) | Lacuna do gateway parcialmente fechada |
| Evidências pessimistas para o isolamento | Substituição acelerada | Depende de o monitoramento de fato funcionar |

Limitações (com direção): inventário sintético (direção desconhecida — declarada como tal); uma única entrevista com profissional (provavelmente *subestima* a perturbação clínica do isolamento, então a nota do isolamento pode ser otimista); o modelo de exposição ignora a escolha de alvos pelo atacante (provavelmente *subestima* o valor de remover primeiro os dispositivos mais expostos). Ponto principal do revisor: "a vantagem do isolamento depende de o monitoramento ter pessoal; mostre o que acontece se os alertas não forem revisados." Resposta: a variação pessimista trata disso e agora está na tabela principal.

### 39.6 Erros comuns e limites

- Mudar as regras do jogo: avaliar contra critérios inventados depois dos resultados.
- Análise de sensibilidade só sobre parâmetros irrelevantes.
- Limitações sem direção.
- Revisões feitas por pessoas que ajudaram a produzir o trabalho.

A avaliação resolvida evita o primeiro ao usar os critérios da proposta, varia os pesos que importam, dá uma direção a cada limitação e usa um revisor que não ajudou a produzir o trabalho.

O segundo erro é comum: variar o peso da força da evidência, que quase não muda a ordenação, deixando intocado o custo, que a inverte. Uma limitação como "uma entrevista" sem direção deixa o leitor incapaz de ajustar o resultado. Um revisor que ajudou a construir o modelo de exposição não consegue fazer uma revisão independente dele.

### Exercícios — capítulo 39

**EX077 — Limitações com direção.** *Objetivo:* escrever limitações úteis. *Entradas:* a comparação do Capítulo 34 (Laboratório 13). *Etapas:* escreva três limitações, cada uma com o quê, o porquê e a provável direção. *Evidência esperada:* três limitações. *Rubrica:* 3 = específicas (por exemplo, notas dadas por um único avaliador — direção desconhecida, resolver com um segundo avaliador; a nota dos backups ignora o roubo de dados — superestima o seu benefício contra o ransomware de dupla extorsão; as notas de custo excluem o tempo da equipe nos exercícios — superestimam a vantagem de custo dos backups); 2 = sem direção; 1 = genéricas; 0 = nada.

**EX078 — Responda à revisão.** *Objetivo:* lidar com a crítica. *Entradas:* o revisor diz "as suas evidências de tempo de restauração vêm de um único ambiente de teste e de cinco exercícios". *Etapas:* escreva uma resposta que aceite, aceite parcialmente ou recuse com os motivos, e declare qualquer mudança. *Evidência esperada:* resposta. *Rubrica:* 3 = aceita a limitação, acrescenta o intervalo de Wilson (Capítulo 37), declara as diferenças entre teste e produção e a direção do viés, ajusta a confiança na recomendação; 2 = aceita sem mudança; 1 = defensiva; 0 = nada.

### Síntese do capítulo

Avalie contra os critérios que você definiu antes dos resultados, teste a robustez da comparação, declare as limitações com a sua direção e convide uma revisão independente. Uma recomendação frágil rotulada com honestidade é mais útil do que uma de aparência robusta que esconde a sua premissa.

<!-- cyberabc:chapter-navigation:start ch-39 -->
### Continue estudando — capítulo 39 de 40

[← Capítulo 38](#ch-38) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 40 →](#ch-40)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-40"></a>

## Capítulo 40 — Monografia e apresentação

### Objetivos de aprendizagem e conexão

Depois deste capítulo, você consegue (1) estruturar uma monografia de bacharelado que relate um trabalho de conclusão comparativo e guiado por evidências; (2) escrever uma conclusão que responda à pergunta dentro das evidências; (3) apresentar e defender o trabalho para um público misto de acadêmicos e profissionais; e (4) lidar com perguntas, inclusive as que você não sabe responder, com honestidade. O capítulo conclui o curso, apoiando-se em todos os capítulos, especialmente no 4, no 15, no 34 e nos 35–39.

### 40.1 Estrutura da monografia

Uma monografia de bacharelado típica deste curso, com 10.000–12.000 palavras:

1. **Resumo** (≈ 250 palavras): pergunta, método, resultado principal, recomendação, limitação-chave.
2. **Introdução**: o serviço, o problema de decisão, a pergunta, por que ela importa, a estrutura.
3. **Fundamentação e literatura**: conceitos e trabalhos anteriores, com a estratégia de busca registrada.
4. **Método**: opções, restrições, critérios e escalas, pesos e como foram definidos, plano de evidências, modelos, ética e autorização.
5. **Resultados**: evidências por opção e critério, notas, análise de sensibilidade — fatos, e não interpretação.
6. **Discussão**: o que os resultados significam, comparação com a literatura, robustez, limitações com direção.
7. **Conclusão e recomendação**: a resposta, a recomendação, as condições de reversão, os trabalhos futuros.
8. **Referências** e **apêndices**: registro de evidências, scripts com hashes, termos de consentimento (em branco), aprovação do anfitrião.

Escreva primeiro o capítulo de método (você o conhece melhor), os resultados em segundo lugar, a introdução e a conclusão por último. Todo número dos resultados precisa vir de um script ou de uma entrada do registro.

### 40.2 A conclusão

Uma boa conclusão responde à pergunta feita — e não a uma mais ampla — e diz com que força. Compare: "O isolamento de rede é a melhor forma de proteger dispositivos médicos" (exagera) com "Para um hospital de porte médio com o inventário sintético estudado, o isolamento com conduítes monitorados foi o que mais reduziu a exposição por libra gasta, desde que os alertas sejam revisados diariamente; a recomendação se inverte se o custo dominar a decisão (peso acima de 0,45) ou se o monitoramento não tiver pessoal." A segunda é mais estreita e muito mais útil.

As condições de reversão dessa conclusão são um peso de custo acima de 0,45, em que vence o gateway do fornecedor, e alertas de monitoramento não revisados, em que vence a substituição acelerada.

### 40.3 A apresentação

Vinte minutos para uma banca mista: problema e pergunta (3 min), método (4), resultados (6), recomendação e limites (4), o que você faria em seguida (3). Uma ideia por slide; mostre a tabela de comparação e o resultado de sensibilidade; ponha os detalhes em slides de reserva. Ensaie em voz alta, com cronômetro e com alguém não especialista.

No trabalho de conclusão sobre dispositivos sem suporte, esse slide mostra as cinco variações e destaca as duas que mudam a vencedora.

No trabalho de conclusão sobre dispositivos sem suporte, os minutos de resultados mostram a tabela de comparação e a tabela de variações da avaliação; os minutos de limites nomeiam a condição de pessoal. Os slides de reserva guardam o registro de evidências e o teste do modelo. Um ensaio com um não especialista costuma revelar jargões como "conduíte", que precisam de uma frase de explicação.

### 40.4 Responder às perguntas

As perguntas se dividem em famílias: *escopo* ("por que não incluir X?"), *método* ("por que esses pesos?"), *evidência* ("como você sabe esta nota?"), *validade* ("isto se manteria num hospital grande?"), *ética* ("como você protegeu o anfitrião?") e *aplicação* ("o que o hospital deve fazer na segunda-feira?"). Prepare duas respostas para cada família. Quando não souber, diga isso, diga como descobriria e, se descobrir um erro, reconheça-o e corrija-o. As bancas valorizam mais a honestidade sobre os limites do que a improvisação confiante.

### 40.5 Exemplo resolvido: uma resposta defensável (sintético)

**Este diálogo é sintético.** *Banca:* "A sua recomendação depende de o monitoramento ter pessoal. Os hospitais têm falta de pessoal. A sua conclusão não é irrealista?" *Candidato:* "Essa é a principal fragilidade do meu resultado. Na variação pessimista, em que os alertas não são revisados, vence a substituição acelerada (Tabela 6.3). Então a minha recomendação é condicional: isolamento com monitoramento onde o hospital puder se comprometer com a revisão diária — por exemplo, por meio de um serviço compartilhado na parceria — e substituição acelerada dos dispositivos de imagem mais expostos onde não puder. Não consegui testar diretamente os níveis de pessoal; um estudo de acompanhamento mediria os tempos de revisão de alertas em vários hospitais."

### 40.6 Erros comuns e limites

- Resultados e discussão misturados.
- Conclusões mais amplas que as evidências.
- Slides lotados de texto; o tempo acaba antes da recomendação.
- Respostas defensivas ou inventadas a perguntas difíceis.
- Revelar nos slides informações que identificam o anfitrião.

O candidato responde ao desafio sobre o pessoal a partir da Tabela 6.3: se os alertas não forem revisados, vence a substituição acelerada, então a recomendação é condicionada à revisão diária.

Um capítulo de resultados que diz "o isolamento é claramente melhor" mistura interpretação nos resultados. Uma conclusão sobre "dispositivos médicos" em geral alega mais do que um inventário sintético de 120 dispositivos sustenta. Slides que chegam à recomendação no minuto 19 não deixam tempo para os limites. E os nomes dos dispositivos de um anfitrião num slide violam o acordo de estágio, mesmo que a monografia tenha sido sanitizada.

### Exercícios — capítulo 40

**EX079 — Escreva o resumo.** *Objetivo:* comprimir o trabalho de conclusão. *Entradas:* o trabalho de conclusão sintético dos Capítulos 35–39. *Etapas:* escreva um resumo de 200–250 palavras com a pergunta, o método, o resultado principal, a recomendação com a sua condição e uma limitação. *Evidência esperada:* resumo. *Rubrica:* 3 = os cinco elementos, números onde for relevante, sem exagero; 2 = falta um; 1 = só descritivo; 0 = nada.

**EX080 — Banco de perguntas.** *Objetivo:* preparar-se para a defesa. *Entradas:* o seu trabalho de conclusão (ou o sintético). *Etapas:* escreva uma pergunta por família listada em responder às perguntas e uma resposta de três frases para cada uma. *Evidência esperada:* seis perguntas e respostas. *Rubrica:* 3 = perguntas difíceis e realistas, com respostas honestas e ligadas às evidências e pelo menos uma resposta do tipo "não sei, mas…"; 2 = perguntas fáceis; 1 = só as perguntas; 0 = nada.

### Síntese do capítulo

A monografia relata uma comparação, e não uma história: método, resultados, discussão e uma conclusão que responde exatamente à pergunta feita, com as suas condições. Apresente com clareza a comparação e a sua sensibilidade, prepare-se para toda família de perguntas e responda às difíceis com honestidade — esse é o hábito profissional que este curso existe para construir.

<!-- cyberabc:chapter-navigation:start ch-40 -->
### Continue estudando — capítulo 40 de 40

[← Capítulo 39](#ch-39) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções e notas de avaliação

As respostas são resultados-modelo, e não as únicas aceitáveis. Aceite uma resposta diferente que atenda ao mesmo padrão de evidências, raciocínio e honestidade sobre os limites. Os números se referem aos dados sintéticos deste livro.

**EX001.** Unidades: (1/ano) × h × (£/h) = £/ano. O resultado é £1.920 **por ano**, e não por hora. Escrever "por hora" faria o cenário parecer 8.760 vezes maior do que é na comparação com um custo anual de £18.000, invertendo a decisão.

**EX002.** Reduzindo à metade as probabilidades de B, a perda evitada é metade de £9.600 = **£4.800** por ano (razão 0,40). Se as estimativas originais de probabilidade fossem dobradas e o controle ainda as reduzisse à metade, a perda evitada seria metade de £19.200 = **£9.600**. Recomendação: B continua preferível, porque o seu pior evento crível (72 h sem energia de reserva num hospital) é o dano maior às pessoas, e a comparação de valor esperado favorece B sob as duas premissas; a incerteza nas probabilidades não muda a ordenação.

**EX003.** Atualizações de firmware assinadas — camada de firmware (não trata uma atualização maliciosa, mas corretamente assinada, vinda de um fornecedor comprometido). Contas de usuário do SO — sistema operacional (não impedem o erro de um usuário autorizado). Limites da biblioteca de medicamentos — aplicação (não pegam um medicamento errado escolhido dentro dos limites). Backups do banco de dados — dados (não ajudam se os backups também forem cifrados, ou nunca forem restaurados). Treinamento da equipe — pessoas (não impede, toda vez, uma isca convincente e direcionada).

**EX004.** Faturamento — TI (pior caso: interrupção da receita e do atendimento ao cliente; patch normal). RTU de alimentador — TO (pior caso: perda de visão/controle da distribuição; janela aprovada pelo fornecedor). Administração de pacientes — TI, mas clinicamente importante (pior caso: atraso no atendimento pela perda de agendamentos e registros; patch normal com controle de mudanças clínico). BMS da ventilação das salas cirúrgicas — TO num ambiente de saúde (pior caso: trocas de ar inseguras que cancelam cirurgias ou arriscam infecção; coordenação entre a manutenção predial e a área clínica, e janela aprovada pelo fornecedor). O BMS mostra que os "sistemas prediais" são TO cujas consequências são clínicas.

**EX005.** Altere o filtro para tratar `row["os_end_of_support"] == ""` à parte: `unknown = [r for r in rows if not r["os_end_of_support"].strip()]`, relate-os sob "UNKNOWN — needs owner" e calcule `unsupported` apenas a partir das linhas com data. A saída acrescenta `VEN-01 ventilator`. Um ventilador com situação de suporte desconhecida é equipamento de suporte à vida na rede clínica cuja exposição a patches ninguém sabe dizer; escale para a engenharia clínica, pedindo a declaração de suporte do fornecedor e uma revisão do posicionamento.

**EX006.** `def is_unsupported(row, year): return int(row["os_end_of_support"]) < year`. Testes: EoS 2030 → False; 2020 → True; EoS igual a `year` (2026) → False sob esta regra. Regra declarada: um dispositivo cujo suporte termina *durante* o ano corrente ainda tem suporte agora, mas deve ser sinalizado numa lista separada de "termina este ano"; uma regra alternativa defensável trata `<=` como sem suporte, para ser conservadora. Qualquer uma é aceitável se for declarada e testada.

**EX007.** Afirmação: "o sistema de pagamentos é seguro". Evidência: "nenhuma interrupção no ano passado". Garantia: "a ausência de interrupção implica a ausência de fraqueza explorável" — falsa, porque as fraquezas podem não ter sido exploradas, e a exploração pode não causar interrupção (fraude, roubo de dados) ou passar despercebida. Reescrita sustentada: "O sistema de pagamentos da Calder Mutual não teve nenhuma interrupção registrada no ano passado; isso, por si só, nada diz sobre a sua exposição a ataques, que exige avaliação."

**EX008.** Modelo (≈ 100 palavras): "Recomendamos financiar o programa de testes dos geradores do hospital (opção B). Ele evita uma perda esperada estimada em £9.600 por ano contra um custo de £12.000, comparada com £4.320 contra £18.000 de um segundo enlace de despacho, e trata o pior caso mais grave: até 72 horas sem energia de reserva no Calder Valley Hospital. Estas estimativas pressupõem que as probabilidades de interrupção estejam corretas dentro de um fator de dois; a ordenação se mantém nesse intervalo. Revisitaríamos a escolha se novas evidências mostrassem a rota única de cabo do enlace de despacho sob risco muito maior, por exemplo durante obras viárias planejadas."

**EX009.** Prontuários de pacientes: C > I > A (a divulgação prejudica os pacientes e viola a lei; a integridade também importa para o atendimento). Dosagem de cloro: I/safety > A > C (um setpoint errado envenena ou desinfeta pouco a água). Autorização de cartões: I ≈ A > C (pagamentos fraudulentos ou indisponíveis; a confidencialidade dos dados de cartão também é regulada — aceite C alta com justificativa). Gravações de chamadas: C ≈ I > A (conteúdo pessoal sensível; integridade probatória; disponibilidade necessária para revisão, mas não em tempo real).

**EX010.** "O ativo é o serviço de despacho do CEDC. Um cabo cortado por obras viárias é uma ameaça; a rota única de cabo é uma vulnerabilidade; o impacto seria a perda de conectividade do despacho, atrasando a resposta de emergência."

**EX011.** $C \cap U$ = {INF-02, IMG-01, IMG-02, ADM-02}. $(C\cap U)\cap K$ = {IMG-01, ADM-02}. $U \setminus C$ = {LAB-01}. Aja primeiro sobre {IMG-01, ADM-02}: sem suporte, na rede clínica e com uma falha sabidamente explorada. ADM-02 também é o mais barato de corrigir.

**EX012.** A alcançabilidade trata toda aresta como "falha se o fornecedor falhar" (E sobre todos os fornecedores). Com uma alternativa por satélite, o despacho só falha se **tanto** a central **quanto** o enlace por satélite falharem (OU sobre os fornecedores). Mudança no modelo: marque cada nó como precisando de **todas** as suas entradas ou de **qualquer uma** delas, e propague a falha de acordo (um grafo de dependências E/OU, como o usado em árvores de falhas, Capítulo 28).

**EX013.** RDP corporativo→controle: benigno — atalho não documentado de um engenheiro; malicioso — intruso pivotando a partir de um PC alvo de phishing; distinga pelos tickets de mudança, pelo usuário logado em 10.1.4.80, pelos logs de autenticação em 10.20.0.5 e por a sessão ter ou não seguido um alerta de phishing. Controle→internet: benigno — verificação de atualização de software do fornecedor; malicioso — comando e controle ou exfiltração de dados; distinga pelo dono do destino, pelo processo que faz a conexão, pelo volume e pela periodicidade. Iniciação de Modbus campo→controle: benigno — dispositivo mal configurado após manutenção; malicioso — dispositivo de campo comprometido sondando a rede; distinga pela configuração do dispositivo comparada à linha de base, pelos registros de manutenção e pelos códigos de função usados.

**EX014.** (1) Regras por host: permitir que apenas o coletor 10.5.0.11 alcance apenas o servidor SCADA 10.20.0.5 na porta 4840, em vez de qualquer host da DMZ alcançar qualquer host de controle; aplicar no firewall; conferir com logs de fluxo. (2) Restringir o Modbus a códigos de função de leitura a partir do servidor SCADA, exceto para registradores de escrita nomeados, usando um firewall que entenda protocolos industriais; conferir revisando os logs de escritas rejeitadas. Outros refinamentos válidos: transferência unidirecional para o historiador, regras por horário para o acesso de engenharia.

**EX015.** (1) `"nan"` é aceito porque toda comparação com NaN é falsa. (2) `"abc"` (ou `""`) levanta `ValueError`, derrubando o chamador ou deixando-o num estado indefinido. (3) Se `current` for NaN (por exemplo, numa leitura de sensor falha), `abs(x - current) > 0.5` é falso para qualquer `x`, então qualquer setpoint dentro da faixa passa na verificação de passo. `"inf"` é rejeitado pela verificação de faixa — mas só porque é maior que 4,5, o que é sorte, e não projeto.

**EX016.** Bomba dosadora de cloro: manter o último setpoint bom, gerar um alarme ao operador, não mover em direção ao máximo; o dono do processo (gerente de qualidade da água) decide esse comportamento em falha. Válvula de entrada de água bruta: manter a última posição boa e alarmar; a operação decide se é necessária uma posição de recuo para proteger a capacidade de tratamento. Registrar para ambos: carimbo de tempo, origem (usuário/estação), entrada bruta, valor interpretado se houver, regra que falhou, valor atual, ação tomada.

**EX017.** `SELECT a.site, COUNT(*) FROM asset a JOIN advisory v ON a.product = v.product WHERE vlt(a.version, v.fixed_in) GROUP BY a.site;` → Head office 1; Substation North 1.

**EX018.** A ordenação de texto põe "critical" < "high" < "low" < "medium", então "low" fica antes de "medium" — errado. Correções: armazenar um `severity_rank` numérico (critical 4, high 3, medium 2, low 1) e ordenar por ele; ou ordenar com `CASE severity WHEN 'critical' THEN 4 ... END`, ou fazer junção com uma tabela de consulta.

**EX019.** Condições de parada e quem chamar: (1) qualquer alarme de processo inesperado ou anomalia relatada por operador — supervisor da sala de controle; (2) qualquer mudança de comportamento de dispositivo coincidente com a conexão do equipamento de captura — supervisor e engenheiro de TO; (3) observação de tráfego do sistema de segurança ou de redes fora do escopo — parar a captura, líder de segurança de TO; (4) o operador ou o supervisor pede para parar — obedecer imediatamente; (5) descoberta de dados pessoais ou credenciais em claro — parar, proteger os arquivos, encarregado de proteção de dados e líder de segurança de TO.

**EX020.** Partes interessadas: pacientes em ventiladores, clínicos, engenharia clínica, segurança, direção do hospital, fornecedor. Danos de aplicar o patch em todos agora: dispositivos indisponíveis no pico de demanda, possíveis falhas de atualização. Danos de não aplicar: exposição à exploração, causando mau funcionamento do dispositivo. Alternativas: aplicar o patch em lotes, à medida que os dispositivos saem de uso; isolar a frota num segmento de rede dedicado, com monitoramento, até a aplicação; atualização apoiada pelo fornecedor à beira do leito em períodos de baixa dependência. O registro de decisão nomeia o diretor clínico e o líder de segurança como donos conjuntos do risco e registra a justificativa, os controles provisórios e uma data de conclusão.

**EX021.** Explorável como implantado: sim, remotamente a partir da rede corporativa. Sabidamente explorada: presumir desconhecido; conferir. Controla: ventilação das salas cirúrgicas — consequência alta. Controles compensatórios: restringir agora o acesso à interface a duas estações da manutenção predial; monitorar. Janela: agendar a reinicialização de 30 minutos com a manutenção predial e o centro cirúrgico quando as salas não estiverem em uso (por exemplo, numa noite de fim de semana), com verificações manuais da ventilação. Recomendação: restringir agora, aplicar o patch na janela segura mais próxima, confirmar depois.

**EX022.** "Proteger as contas" → "Todo login de IHM é uma conta individual nominal; nenhuma conta padrão do fornecedor está habilitada; conferido mensalmente exportando a lista de contas e comparando-a com a escala." "Ligar os logs" → "Os logs de segurança e de aplicação são encaminhados ao servidor central de logs em até 5 minutos; conferido semanalmente confirmando o evento mais recente de cada host." "Bloquear o USB" → "O armazenamento em massa USB está desabilitado por política nas estações dos operadores; conferido por exportação trimestral da política e por um teste com um dispositivo aprovado."

**EX023.** Prior 0,01: $0.95 \times 0.01/(0.95\times0.01 + 0.01\times0.99) \approx 0.490$. Prior 0,001, FPR 0,001: $0.95\times0.001/(0.95\times0.001 + 0.001\times0.999) \approx 0.487$. Uma taxa de falsos positivos dez vezes menor ajuda tanto quanto uma taxa de base dez vezes maior. Os analistas não podem mudar a taxa de base, mas podem baixar a FPR com ajuste fino, enriquecimento de contexto e allowlisting — a alavanca prática.

**EX024.** Independentes: $0.05^2 = 0.0025$. Com causa comum: ≈ $0.02 + 0.0025 = 0.0225$, cerca de nove vezes pior. Remédio: fontes de combustível separadas ou teste e polimento do combustível, modelos de gerador ou sistemas de partida diferentes, e testes periódicos com carga.

**EX025.** Papéis: atendente de chamadas (criar incidentes, ver o CAD); despachante (designar unidades, atualizar incidentes); supervisor (sobrepor, redesignar, ver relatórios); administrador do CAD (configurar o sistema, gerenciar contas; sem despacho); suporte do fornecedor (acesso limitado no tempo e aprovado por sessão, ao ambiente de teste por padrão). Pares tóxicos: administrador do CAD + administrador do log de auditoria (poderia esconder as próprias mudanças); suporte do fornecedor + acesso permanente à produção; despachante + administrador do CAD (poderia alterar as regras e agir com base nelas sem ser visto).

**EX026.** Acrescente datas `approved` a cada tupla; sinalize se `roles & PRIV` e `(TODAY - approved).days > 180`. Com, por exemplo, *dev* aprovado em 2025-11-01 (334 dias) e *chloe* aprovada em 2026-07-01 (92 dias), a saída acrescenta "re-approval overdue 334 d" apenas a *dev*. O teste deve mostrar uma conta privilegiada sinalizada e uma não sinalizada.

**EX027.** Projeto minimizado: registrar o ID do funcionário, o identificador do prontuário do paciente (não o nome nem o diagnóstico), a estação de trabalho, o carimbo de tempo e o tipo de acesso; reter por 2 anos (ou pelo período definido pela política do hospital), com acesso restrito ao encarregado de privacidade e a dois auditores nomeados; finalidade declarada como detectar acessos inadequados; equipe informada por meio da política e de um aviso no login; reidentificação do paciente apenas em investigações confirmadas.

**EX028.** Riscos: em códigos postais pequenos, um tipo de imóvel único (por exemplo, a única casa isolada) identifica um domicílio; os padrões horários revelam ocupação, rotinas e ausências. Mitigações: publicar apenas agregados sobre um número mínimo de medidores (por exemplo, ≥ 10), tornar mais grosso o tempo (diário) ou a localização; fornecer dados finos apenas sob acordos de acesso a pesquisadores aprovados.

**EX029.** Diagrama (2025) — documento, produzido pela equipe, com um ano, não independente: mostra apenas a intenção do projeto. Relatório do teste de failover (14 min) — demonstração, pela operação, no ano passado, não independente: evidência real de que o failover *pode* funcionar. Nota do auditor — independente, recente: mostra que o teste foi anunciado, então a equipe estava preparada e as condições eram favoráveis. Conclusão: evidência de que o failover pode cumprir 15 minutos em condições preparadas; não de que o faria numa falha não anunciada e sob carga. Peça um teste não anunciado ou observado de forma independente, com a carga registrada.

**EX030.** Métrica: "proporção de contas privilegiadas e de acesso remoto que usam autenticação resistente a phishing", medida mensalmente a partir do sistema de identidade como (contas com autenticadores resistentes a phishing) / (todas as contas privilegiadas e de acesso remoto), com o denominador e as exclusões relatados. Risco de manipulação: reclassificar contas como não privilegiadas para encolher o denominador — mitigado por uma definição independente de privilégio. (Uma taxa de reporte em simulações autorizadas também é aceitável, com manipulação por meio de simulações previsíveis.)

**EX031.** Menor privilégio — os usuários remotos caem na rede de controle inteira; padrões à prova de falha — contas de fornecedor habilitadas permanentemente; mediação completa — nenhuma verificação, por sessão, de quem está se conectando nem por quê; separação de privilégio — uma senha sozinha concede acesso, sem segundo fator nem aprovação do operador; mecanismo menos comum — um único gateway compartilhado por todos os usuários e fornecedores, direto para o controle.

**EX032.** O comprometimento de uma conta ou de um servidor desabilita juntos as regras de firewall, a proteção de endpoints e os backups — as três "camadas" compartilham um único mecanismo. Mudanças: separar níveis administrativos e credenciais (e hosts de gerenciamento) para os sistemas de rede, de endpoints e de backup, com MFA resistente a phishing; manter pelo menos uma cópia de backup offline ou imutável, gerenciada fora do domínio.

**EX033.** (a) Assinaturas digitais — qualquer um pode verificar, só o fabricante pode assinar. (b) MAC com números de sequência (ou um canal com autenticação mútua, como TLS, onde os dispositivos o suportarem) — autenticidade, integridade e atualidade. (c) Cifração simétrica de disco, com a chave protegida por hardware e pela autenticação do usuário. (d) Cadeia de hashes com uma âncora mantida externamente (ou entradas de log assinadas).

**EX034.** Um administrador com acesso tanto ao log quanto à âncora edita uma entrada, recalcula todas as cabeças seguintes e sobrescreve a âncora com a nova cabeça; a verificação então passa. Prevenção: manter a âncora num sistema administrado por outra equipe, com armazenamento só de acréscimo; publicar ou contra-assinar periodicamente as cabeças com um serviço confiável de carimbo de tempo; alertar sobre qualquer reescrita da âncora.

**EX035.** Exemplo: "Entre os operadores de distribuição de eletricidade de [um país] que publicaram relatórios de incidentes ou anuais em 2020–2025, com que frequência são mencionados incidentes iniciados por phishing, e quais mitigações os relatórios descrevem?" — descritiva, com um elemento comparativo (as mitigações), com evidências de relatórios públicos. Alternativamente, uma pergunta comparativa sobre duas abordagens de autenticação resistente a phishing em laboratório.

**EX036.** Constructo: "incidentes relatados" mede o reporte e a detecção, e não os ataques. Interna: os hospitais que compram X podem também ter orçamentos maiores, mais pessoal ou exposição diferente (confusão); seleção — os compradores diferem sistematicamente. Externa: os achados dos hospitais estudados podem não se transferir. Confiabilidade: definições diferentes de "incidente de ransomware" entre os hospitais.

**EX037.** Funções: "prestar serviços de pagamento" (autorização de cartões, transferências) e "prover acesso a dinheiro em espécie". Dependências: energia, telecomunicações (centrais, operadoras), sistemas nacionais de pagamento e compensação, redes de cartão, provedores de nuvem, pessoal. Linha do tempo do dano: falhas nos pagamentos com cartão prejudicam em horas (combustível, compras de alimentos); pagamentos de salários e benefícios, em dias; a perda de acesso a dinheiro em espécie agrava o dano se os pagamentos com cartão também estiverem fora do ar.

**EX038.** Risco: "quais cenários na estação são mais prováveis e danosos?" — pode perder cascatas novas ou a adaptação do adversário. Resiliência: "por quanto tempo a estação consegue fornecer água segura em modos degradados, e com que rapidez se recupera?" — pode dar peso de menos à prevenção custo-efetiva. Sistemas: "quais ações de controle de operadores, software e procedimentos poderiam ser inseguras?" — mais difícil de quantificar e de priorizar.

**EX039.** Exemplo (Oldsmar): a CISA afirma que atores não identificados acessaram o sistema SCADA por meio de software de acesso remoto, aumentaram o setpoint de hidróxido de sódio, e um operador reverteu a mudança. Repetido com frequência, mas não sustentado por esse alerta: afirmações sobre a identidade do atacante. Redação do relatório: "Em fevereiro de 2021, a CISA relatou uma aparente mudança não autorizada na dosagem química numa estação de água da Flórida; em 2023, um ex-funcionário municipal disse que provavelmente foi erro de um empregado. De qualquer modo, o caso ilustra o risco do acesso remoto não gerenciado."

**EX040.** Dependências: sistemas de bilhetagem e de receita (a operação sem arrecadação pode ser recusada), escala e programação das tripulações, sistemas de informação aos passageiros, gestão da manutenção (registros de defeitos críticos para a segurança). Medidas: regras de operação degradada acordadas previamente (por exemplo, viagem gratuita, escalas em papel), aprovadas pela direção com antecedência; separação e backup dos dados operacionalmente necessários, como os registros de defeitos; exercícios regulares de operar trens sem a TI corporativa.

**EX041.** (a) Perda da visão histórica — risco imediato baixo, análise de tendências reduzida. (b) Perda de visão — perigosa: os operadores podem agir com base em dados desatualizados. (c) Manipulação do controle — efeito direto no processo. (d) Perda de proteção — gravidade máxima: a última barreira automática se foi.

**EX042.** Cadeia: sinalização (formação de rotas e detecção de trens) → controle/condução dos trens → comunicação da tripulação e do controle → informação aos passageiros → bilhetagem. Modos degradados: falha da sinalização — autorização manual para prosseguir, com velocidade e frequência reduzidas; falha do rádio — telefones fixos nas estações, trens retidos nas plataformas; falha da informação aos passageiros — anúncios pela equipe, avisos de serviço reduzido; falha da bilhetagem — viagem gratuita ou bilhetes em papel. Restrições: capacidade menor, mais pessoal, viagens mais longas.

**EX043.** Com 48 h de autonomia para os pagamentos com cartão: em 6 h, 3 serviços perdidos (central A, bombas de água, sinalização ferroviária); em 30 h, 5 perdidos (os pagamentos com cartão sobrevivem). Autonomias reduzidas à metade, em 6 h: 5 serviços perdidos — central telefônica A (2 h), bombas de água, reservação de água tratada (5 h), pagamentos com cartão (2 h), sinalização ferroviária (1 h). Recomendação: transferir os pagamentos com cartão para a central B ou acrescentar um gerador na central A, e substituir as autonomias de projeto por valores testados, já que o caso pessimista perde a reservação de água em 6 h.

**EX044.** Contrato de fornecimento de combustível e rota de entrega (evidência: contrato, teste de entrega durante um exercício); pessoal para operar e reabastecer (evidência: escala e registros de treinamento); confiabilidade de partida e de carga do gerador (evidência: logs de testes mensais sob carga); quadro de manobra/chave de transferência e refrigeração (evidência: registros de manutenção, teste da transferência automática).

**EX045.** Ambos têm nota 10. A nota igual esconde que A é frequente e menor enquanto B é raro e grave (cancelamento de cirurgias, dano a pacientes), e que rótulos ordinais não podem ser multiplicados de forma significativa. Apresente uma coluna de pior consequência crível e faixas quantitativas aproximadas (frequência por ano, duração da interrupção, dano), ou trate B com uma análise de consequência primeiro.

**EX046.** Consequência: "transferências fraudulentas de alto valor liberadas" (ou "pagamentos indisponíveis por > 4 h em dia de salário"). Caminhos: credenciais de operador comprometidas; um insider criando e aprovando por meio de uma combinação tóxica de papéis (Laboratório 7); mudança maliciosa nas regras do switch de pagamentos; carga equivocada de arquivo em lote. De engenharia: limites rígidos por transação e diários aplicados no switch, confirmação fora de banda para transferências acima de um limiar. Procedimental: aprovação por duas pessoas, com papéis separados.

**EX047.** Backups offline — corretivo, técnico. Aprovação por duas pessoas — preventivo, procedimental. Analisador de cloro na saída que aciona uma válvula — preventivo (limita a consequência), de engenharia. Alerta do SIEM sobre novas contas de administrador — detectivo, técnico. Chave física para programar o CLP — preventivo, físico.

**EX048.** Linha: "Ransomware no servidor do BMS" — preventivo: allowlisting de aplicações, acesso administrativo restrito, segmentação em relação à rede corporativa; detectivo: monitoramento do servidor do BMS e dos backups; corretivo: restauração testada do servidor e das configurações do BMS, controle manual local do tratamento de ar. Melhoria mais valiosa: uma restauração testada mais um procedimento de controle local ensaiado, porque o controle local mantém as salas cirúrgicas seguras qualquer que seja a causa da perda do BMS.

**EX049.** Prioridade 2 (confiança: média): investigar e fechar o fluxo RDP corporativo→controle da CW e o fluxo controle→internet (Laboratório 4) — eles contornam a DMZ, e o caminho de consequência leva ao controle do tratamento de água; donos: segurança de TO da CW (investigar esta semana), equipe de rede da CW (regras). Prioridade 3 (confiança: alta): desabilitar a conta do desligado, remover as combinações tóxicas e passar o acesso dos fornecedores para aprovação por sessão (Laboratório 7) — caminhos diretos para ações de controle não autorizadas e fraude em pagamentos; donos: donos dos sistemas, em até uma semana. O isolamento dos dispositivos clínicos sem suporte (Laboratório 2) é uma terceira prioridade alternativa aceitável, com raciocínio de consequência.

**EX050.** Declaração-modelo: "Reexecutei os Laboratórios 2, 4, 5 e 7 do apêndice com o Python 3.13. Os hashes de lab02, lab04 e lab07 coincidiram; o de lab05 não, porque o autor havia acrescentado uma consulta LEFT JOIN, documentada nas suas notas de mudança. Todas as saídas impressas coincidiram com o apêndice, incluindo a saída da consulta extra. A seção de achados é reprodutível."

**EX051.** S: um host intruso se passa pelo coletor — autenticação mútua por certificados, regras por host. T: valores alterados em trânsito — sessão OPC UA autenticada e com integridade protegida. R: o coletor nega as consultas — logs no lado do SCADA, com sincronização de tempo. I: o coletor expõe mais tags do que o necessário — conta somente leitura limitada às tags necessárias. D: polling excessivo sobrecarrega o servidor SCADA — limites de taxa e monitoramento de recursos. E: a conta do coletor pode escrever — papel somente leitura, aplicado no lado do servidor.

**EX052.** Objetivos: (1) decidir em até 30 minutos se passar à administração de pacientes em papel, (2) fazer a avaliação de proteção de dados e decidir sobre a notificação dentro do prazo do plano. Participantes: gestor de plantão, líder do pronto-socorro, plantão de TI, encarregado de proteção de dados, comunicação, manutenção predial. Injeções: 23:10 nota de resgate nas telas administrativas; 23:40 o pronto-socorro não consegue ver a situação dos leitos; 00:30 evidência de que dados de pacientes foram copiados para fora; 01:30 consulta de um jornalista. Registrar: horários das decisões, donos das decisões, informações usadas, desvios do plano.

**EX053.** Verificação: numa janela autorizada, a partir de um host de teste na rede corporativa, tentar conexões a cada endereço da zona de controle numa lista definida de portas; a afirmação é falsa se qualquer conexão tiver sucesso. Validação: revisar configurações e logs de fluxo em busca de caminhos alternativos — hosts com duas interfaces, gateways de acesso remoto, pontes sem fio, modems de fornecedores; a afirmação é falsa se existir qualquer caminho do corporativo para o controle. Autorização: RoE escritas da operação e da segurança da CW, com condições de parada.

**EX054.** Limiar 0,7: erros = FP 2 + FN 7 = 9; acurácia = 5.016/5.025 ≈ 0,9982. Nunca alertar: acurácia = 5.000/5.025 ≈ 0,9950. Ambos parecem excelentes porque 99,5% dos eventos são benignos; a acurácia recompensa ignorar a classe rara. Relate precisão e revocação (0,90/0,72 contra indefinida/0).

**EX055.** Com o caminho do BMS passando a exigir uma interrupção da rede: falha da reserva = $1 - 0.98 \times 0.995 \times 0.99 \times 0.998 \approx 0.03658$; topo = $0.05 \times 0.03658 \approx 0.001829$ — cerca de metade do 0,003729 anterior e apenas um pouco acima do 0,001733 só físico. O caminho cibernético agora precisa de uma interrupção da rede coincidente, restaurando a estrutura de dois eventos; um adversário capaz de causar também uma interrupção da rede continua a ser um risco residual.

**EX056.** A bomba dosadora funciona no máximo — superdosagem, água insegura — detectada pelo alarme alto do analisador de saída — limite de vazão por hardware, desarme pelo analisador. A bomba para — desinfecção insuficiente — alarme baixo do analisador, retorno de bomba em funcionamento — bomba de serviço/reserva. O analisador lê baixo (deriva) — o controlador aumenta a dosagem — comparação com amostra manual/segundo analisador — calendário de calibração. Analisador congelado — nenhuma resposta a mudanças reais — alarme de "valor estagnado" para uma leitura que não muda — verificações de manutenção.

**EX057.** Modelo: "Nos 15 incidentes compartilhados pelos membros da CRP, metade foi detectada em até 4 horas; o percentil 90 foi de cerca de 56 horas; um caso levou 240 horas. A recuperação levou uma mediana de 8 horas (percentil 90 de cerca de 38 horas). O tempo médio de detecção (27 h) é distorcido pelo único caso mais longo. Esses registros são poucos, sanitizados e dependem de horários de início autodeclarados. Por que o monitoramento deixou de ver, por dez dias, o uso indevido de credenciais de 240 horas?"

**EX058.** (1) A operação confirma o estado do processo e que o SCADA e os controladores se comportam normalmente — supervisor da sala de controle. (2) Preparar a operação local/manual das estações críticas para o caso de o SCADA ser afetado — gerente de operações. (3) Isolar o historiador da zona de controle (e dos conduítes da DMZ) — analista de segurança, com autorização do supervisor. (4) Preservar evidências: imagem de memória e de disco do historiador, logs de firewall e de fluxo — segurança. (5) Conferir os servidores SCADA, as estações de engenharia e as configurações dos controladores contra linhas de base sabidamente boas — engenheiro de TO, com a segurança. Depois, as decisões de recuperação e de notificação.

**EX059.** Os registros de sistema (logs de acesso remoto, controle da CPN) são altos porque são gerados automaticamente por sistemas separados. Os operadores percebendo às 02:10 é alto (log do turno, várias testemunhas). A mudança de setpoint às 01:52 é média: a cabeça ancorada mostra que o log foi alterado, então nem o horário nem o valor registrados merecem confiança. Elevá-la a alta exige o próprio log de eventos do CLP ou a trilha de auditoria de setpoints, a tendência do historiador para o setpoint e o nível do tanque, e a gravação da sessão do fornecedor.

**EX060.** Ações: aprovação por sessão do fornecedor, com gravação (segurança de TO da CW, 1 mês; verificar pelos logs de sessão); alarme para mudanças de setpoint fora dos limites ou da taxa (engenharia da CW, 2 meses; verificar com uma mudança de teste); mover a âncora do log para um sistema operado por outra equipe (TI da CW, 1 mês; verificar por revisão de acessos); modelo de situação entre operadores e lista de contatos (coordenador da CRP, 6 semanas; verificar no próximo exercício); exercício conjunto CW–CPN sobre eventos combinados de rede e de processo (CRP, 6 meses; verificar pelo relatório pós-ação).

**EX061.** Falharam: que as estações dos operadores e o acesso remoto só pudessem ser usados por pessoal legítimo (a CISA relata a operação remota de disjuntores); que as centrais de atendimento continuariam disponíveis aos clientes (a CISA relata a interrupção das centrais de atendimento aos clientes). Se manteve: que a operação manual das subestações era possível — a CISA relata que a energia foi restabelecida passando ao modo manual.

**EX062.** Mapa: produto de endpoint ↔ CVH, CEDC, Calder Mutual (alcance 3, três setores — o maior); região de nuvem ↔ CEDC, CT (alcance 2); integrador de TO ↔ CW, CPN (alcance 2). Medidas: atualizações escalonadas de endpoints, com grupos canário e um rollback testado; confirmar que os planos de contingência do CEDC e da CT funcionam sem a região de nuvem; credenciais do integrador separadas por operador, aprovação por sessão e monitoramento conjunto.

**EX063.** Modelo: "O nosso modelo de resiliência energética (números sintéticos) mostra que o projeto de reserva do CVH precisa de duas falhas para cortar a energia das áreas críticas — uma interrupção da rede e uma falha da reserva. Uma fraqueza contorna isso: o sistema de gestão predial pode desligar sozinho os circuitos críticos. Se ele fosse mal utilizado, os pacientes nas salas cirúrgicas e na terapia intensiva poderiam perder energia sem nenhum problema na rede. Propomos uma mudança de engenharia (cerca de £25.000, ilustrativo) para que o sistema predial não possa desligar circuitos críticos. As probabilidades do modelo são estimativas e um atacante não se comporta de forma aleatória, então o argumento se apoia na remoção do ponto único de falha, e não nos números exatos."

**EX064.** Risco: um operador que digita errado a senha sob estresse — ou um atacante que digita senhas erradas de propósito — bloqueia a IHM durante uma emergência, impedindo o controle. Alternativas: nenhum bloqueio nas IHMs da sala de controle, combinado com controle de acesso físico à sala, limitação de taxa, alerta para falhas repetidas e um procedimento de sobreposição de emergência com auditoria; autenticação forte onde ela não atrapalhe a resposta (por exemplo, cartões inteligentes).

**EX065.** $p_o = 34/40 = 0.85$. Codificador A: 10/40 = 0,25 sim; B: 12/40 = 0,30 sim. $p_e = 0.25 \times 0.30 + 0.75 \times 0.70 = 0.075 + 0.525 = 0.60$. $\kappa = (0.85 - 0.60)/(1 - 0.60) = 0.625$. Convencionalmente descrita como concordância substancial; as escalas são convenções, então relate o valor, discuta as discordâncias e refine o livro de códigos.

**EX066.** Informações do consentimento: finalidade do estudo; participação voluntária e direito de desistir até uma data declarada; o que é registrado (notas ou áudio) e por quê; como os dados são armazenados, por quanto tempo e quem os vê; como os resultados serão relatados (anonimizados, sem detalhes que identifiquem a organização ou vulnerabilidades, revisão pelo anfitrião). Proteção de dados: armazenamento cifrado, pseudônimos para pessoas e organizações, eliminação das notas brutas após a transcrição e no prazo previsto, e nenhum detalhe técnico de vulnerabilidade em nenhum produto.

**EX067.** Nota da segmentação $= 5w + 8(1-w)/3$; backups $= 4w + 13(1-w)/3$. Empate: $w = 5(1-w)/3 \Rightarrow 3w = 5 - 5w \Rightarrow w = 5/8 = 0.625$. Ambos têm nota 4,125 nesse ponto. Acima de 0,625, a segmentação vence.

**EX068.** O requisito é uma restrição, e não um critério ponderado: uma opção que não consegue demonstrar restauração em 4 horas é excluída. Backups com exercícios de restauração podem fornecer a demonstração diretamente (registros dos exercícios, de preferência observados de forma independente). A segmentação e a detecção gerenciada reduzem a probabilidade ou a propagação do ransomware, mas não restauram o serviço; só se qualificam combinadas com uma capacidade de recuperação demonstrada. A comparação passa a ser entre combinações que atendem à restrição.

**EX069.** (a) Não é comparativa nem delimitada, como está escrita; poderia ser reformulada. (b) Comparativa, viável com um conjunto de dados sintético, ética, útil para os operadores, delimitada — escolha (b). (c) Teste não autorizado de uma concessionária real — antiético e provavelmente ilegal; rejeite (Capítulo 10).

**EX070.** Redução da consequência — saídas do modelo de exposição do laboratório para cada opção; ameaça: as premissas simplificadas de exposição do modelo. Interrupção clínica — dados de entrevistas e orientações publicadas de engenharia clínica; ameaça: uma ou duas entrevistas podem não representar outros hospitais. Custo — faixas de preço publicadas e estimativas de tempo de pessoal; ameaça: os preços variam e podem estar desatualizados. Força da evidência — classificação das fontes com as perguntas do Capítulo 15; ameaça: classificação feita por uma única pessoa (mitigar com um segundo classificador).

**EX071.** Supervisores: o gerente de TI do CEDC nomeado e o orientador acadêmico. Permitido: observação, revisão de documentos, atualizações do inventário no ambiente de teste; proibido: qualquer mudança no CAD ou na telefonia em produção, qualquer teste sem RoE escritas. Confidencialidade: nenhum documento é retirado; os trabalhos do curso são revisados pelo CEDC antes da entrega. Proteção de dados: nenhum acesso a gravações de chamadas nem a registros de incidentes com dados pessoais. Segurança: integração ao local, incluindo os procedimentos de emergência. Escalonamento: qualquer descoberta grave é relatada imediatamente, apenas ao supervisor do local.

**EX072.** Versão segura: "Terça-feira: revisei o ambiente do gateway de pagamentos com o meu supervisor; observei um componente que parece mais antigo que a versão atualmente suportada; levei-o ao meu supervisor para acompanhamento." Removidos: nome do host, credenciais, endereço IP, nome de usuário da pessoa e versão exata. A credencial nunca deve ser registrada; relate ao supervisor que ela estava anotada, para que possa ser trocada.

**EX073.** 34/40: Wilson ≈ [0,71, 0,93]. 85/100: ≈ [0,77, 0,91]. A estimativa pontual é a mesma (0,85), mas o intervalo se estreita aproximadamente com $1/\sqrt{n}$; para afirmar a confiabilidade com precisão útil, o CEDC precisa de um programa de exercícios regulares, e não de uma única campanha.

**EX074.** Revisão: a "acurácia" num conjunto de dados desbalanceado não é informativa (Capítulo 27); um único testbed público pode não representar sistemas de água reais (validade externa); o protocolo de avaliação pode inflar os resultados (Kim et al., 2022); o fornecedor tem interesse. Perguntas: precisão e revocação no limiar que vocês recomendam; alarmes falsos por dia em implantações reais; protocolo de avaliação e se os dados de treino e de teste foram separados no tempo; alguma avaliação independente ou referências de clientes em concessionárias comparáveis.

**EX075.** Linhas (item / fonte / data / tipo / como foi obtido / armazenamento / critério): (1) inventário sintético, `make_inventory.py` semente 38 com hash / autor / semana 8 / medição / script / repositório do projeto / consequência; (2) resultados dos testes do modelo para o caso de 5 dispositivos / autor / semana 10 / verificação / script / repositório / força da evidência; (3) notas da entrevista 1, pseudônimo P1 / engenheiro clínico / semana 11 / qualitativa / entrevista consentida / armazenamento cifrado / interrupção clínica; (4) documento de orientação A / órgão público / ano / documento / download / pasta de referências / interrupção clínica; (5) documento de orientação B / órgão público / ano / documento / download / pasta de referências / consequência e custo.

**EX076.** Modelo: "Contrariando a expectativa, a opção de gateway do fornecedor foi a que menos reduziu a exposição dos dispositivos de imagem (Tabela 5.2). A causa é que os dispositivos de imagem também aceitam conexões do arquivo de imagens, que o gateway não intermedeia. Uma variante que acrescenta controles do lado do arquivo fechou parte da lacuna (Tabela 5.3), mas o isolamento ainda teve nota maior. Os dois resultados são relatados porque a configuração original reflete como os gateways costumam ser implantados. O achado se apoia num inventário sintético e num único modelo de exposição; deve ser conferido contra dados reais de rede antes de ser generalizado."

**EX077.** (1) As notas foram atribuídas por um único avaliador: direção desconhecida; mitigar com um segundo avaliador independente. (2) A nota dos backups ignora o roubo de dados no ransomware de dupla extorsão: provavelmente *superestima* o benefício dos backups em relação às opções que reduzem a intrusão. (3) As notas de custo excluem o tempo de pessoal dos exercícios de restauração: provavelmente *superestimam* a vantagem de custo dos backups. Outras limitações defensáveis são aceitáveis, com a direção.

**EX078.** Modelo: "Aceito. A evidência do tempo de restauração vem de cinco exercícios num único ambiente de teste. Acrescentei um intervalo de Wilson de 95% (0,38–0,96 para 4 de 5) e uma tabela das diferenças entre teste e produção (volume de dados, integrações, pessoal). Como as restaurações em produção envolvem mais dados e integrações, os exercícios provavelmente subestimam os tempos reais de restauração. Rebaixei a confiança da recomendação de alta para média e recomendei um exercício em escala de produção, observado de forma independente."

**EX079.** Modelo (≈ 220 palavras): "Os hospitais mantêm dispositivos clínicos cujo software não tem mais suporte, porque os dispositivos duram mais que os seus sistemas operacionais. Este trabalho de conclusão perguntou qual de três abordagens — substituição acelerada, isolamento de rede com monitoramento ou gateways seguros gerenciados pelo fornecedor — reduz melhor a exposição de um hospital de porte médio dentro de um orçamento fixo. Usando um inventário sintético de 120 dispositivos construído a partir de categorias publicadas, um modelo de exposição testado contra um caso resolvido à mão, uma entrevista com um profissional e orientações públicas, as opções foram comparadas quanto à redução da consequência, à interrupção clínica, ao custo e à força da evidência, com pesos definidos de antemão. O isolamento com monitoramento teve a maior nota e continuou preferido, a menos que o custo levasse mais de 45% do peso da decisão, caso em que os gateways do fornecedor foram preferidos, ou que os alertas de monitoramento não fossem revisados, caso em que a substituição acelerada dos dispositivos de imagem mais expostos foi preferida. Os gateways do fornecedor tiveram desempenho inferior para os dispositivos de imagem porque as conexões do arquivo os contornam. Recomendamos o isolamento com conduítes monitorados onde for possível assumir a revisão diária dos alertas, e a substituição priorizada nos demais casos. A principal limitação é o inventário sintético e a entrevista única, que provavelmente fazem a interrupção clínica do isolamento parecer menor do que é."

**EX080.** Exemplos de perguntas: escopo — "Por que não incluir imagem hospedada na nuvem?" (fora do escopo por projeto; mudaria a exposição; trabalho futuro). Método — "Por que esses pesos?" (definidos com o anfitrião antes da pontuação; sensibilidade mostrada; inversão em 0,45). Evidência — "Como você sabe a nota de interrupção do isolamento?" (uma entrevista mais orientações; reconhecida como fraca; limitação direcional). Validade — "Isso valeria num grande hospital universitário?" ("Não sei; o mix do inventário é diferente; eu testaria com a distribuição de categorias deles"). Ética — "Como você protegeu o anfitrião?" (dados sintéticos, entrevista anonimizada, revisão pelo anfitrião). Aplicação — "O que o hospital deve fazer na segunda-feira?" (restringir e monitorar os conduítes da imagem; iniciar o caso de substituição dos cinco dispositivos mais expostos).

<a id="glossary"></a>

## Glossário

- **Allowlist** — uma política que permite apenas os fluxos, programas, valores ou usuários listados; todo o resto é negado.
- **Âncora** — uma cópia confiável da cabeça de uma cadeia de hashes, mantida fora do alcance de quem controla o log.
- **Autonomia (da reserva)** — por quanto tempo um serviço continua com a sua própria energia de reserva, armazenamento ou processo manual.
- **Taxa de base** — o quão comum é uma condição antes de qualquer teste ou alerta; ela domina o significado de um alerta.
- **Causa comum / modo comum** — uma única causa que derrota várias salvaguardas supostamente independentes.
- **Controle compensatório** — uma medida que reduz a exposição quando o controle preferido (por exemplo, o patch) não é possível.
- **Conduíte** — um caminho de comunicação controlado entre zonas.
- **Análise de consequência primeiro** — análise de risco que parte dos desfechos inaceitáveis e rastreia os caminhos até eles (por exemplo, a CCE).
- **Restrição (decisão)** — um requisito que exclui opções, qualquer que seja a sua nota.
- **Função crítica** — uma função (por exemplo, "fornecer água") cuja interrupção prejudicaria gravemente a sociedade.
- **DMZ** — uma zona de rede entre os sistemas corporativos e os de controle, para a troca controlada de dados.
- **Perda anual esperada (EAL)** — a probabilidade por ano multiplicada pela perda por evento, somada sobre os cenários.
- **FMEA** — análise de modos e efeitos de falha; análise de baixo para cima de como os componentes falham e do que decorre disso.
- **Árvore de falhas** — um modelo de cima para baixo de um evento indesejado, construído com portas E e OU sobre eventos básicos.
- **HMAC** — um código de autenticação de mensagem com chave, construído a partir de uma função de hash.
- **IHM (HMI)** — interface homem–máquina usada pelos operadores para ver e controlar um processo.
- **Kappa (de Cohen)** — a concordância entre dois codificadores, corrigida pelo acaso.
- **Menor privilégio** — dar a cada usuário ou programa apenas o acesso de que ele precisa.
- **TO (tecnologia operacional)** — sistemas que monitoram ou controlam processos físicos.
- **Precisão / revocação** — a fração dos alertas que são reais / a fração dos eventos reais que são pegos.
- **Regras de engajamento (RoE)** — termos escritos que autorizam um teste ou exercício: escopo, métodos, janela, condições de parada.
- **SCADA** — supervisão e aquisição de dados; supervisão de malhas de controle numa área ampla.
- **Análise de sensibilidade** — conferir se uma decisão muda quando as entradas incertas ou os pesos mudam.
- **SIS** — sistema instrumentado de segurança; proteção automática independente que leva um processo a um estado seguro.
- **STPA** — análise de processos baseada na teoria de sistemas; encontra ações de controle inseguras numa estrutura de controle.
- **Combinação tóxica** — um conjunto de papéis que não pode ser detido por uma única pessoa (segregação de funções).
- **Validação / verificação** — alcançar a finalidade no ambiente real / atender à especificação.
- **Intervalo de Wilson** — um intervalo de confiança para uma proporção que se comporta bem com amostras pequenas.
- **Zona** — um grupo de ativos com requisitos de segurança semelhantes.

<a id="references"></a>

## Referências

Leis, normas, orientações e páginas de incidentes mudam. As versões e datas abaixo são as consultadas para este rascunho (outubro de 2026); verifique-as de novo antes de se apoiar nelas.

**Políticas, leis, normas e frameworks**

- Cybersecurity and Infrastructure Security Agency. [Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
- Cybersecurity and Infrastructure Security Agency. [ICS Advisories](https://www.cisa.gov/news-events/ics-advisories).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Cybersecurity and Infrastructure Security Agency. [Secure by Design](https://www.cisa.gov/securebydesign).
- Cybersecurity and Infrastructure Security Agency. [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom).
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Official Journal, 4 May 2016.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- European Union. [Regulation (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). Official Journal, 27 December 2022.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- International Electrotechnical Commission. [IEC 62443-3-2:2020 — Security risk assessment for system design (catalogue page)](https://webstore.iec.ch/en/publication/30727).
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- MITRE. [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/).
- Modbus Organization. [Modbus Application Protocol Specification](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework). February 2024.
- National Institute of Standards and Technology. [NIST Privacy Framework](https://www.nist.gov/privacy-framework).
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final). September 2012.
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025.
- National Institute of Standards and Technology. [SP 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final). September 2023.
- Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., and McQuaid, R. [SP 800-160 Vol. 2 Rev. 1, Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1). NIST, December 2021.
- National Institute of Standards and Technology. [SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final). August 2020.
- National Institute of Standards and Technology. [SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final). February 2022.
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final); [FIPS 197, Advanced Encryption Standard](https://csrc.nist.gov/pubs/fips/197/final); [FIPS 198-1, The Keyed-Hash Message Authentication Code (HMAC)](https://csrc.nist.gov/pubs/fips/198-1/final).
- National Institute of Standards and Technology. [NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). 13 August 2024.
- North American Electric Reliability Corporation. [Critical Infrastructure Protection (CIP) Standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).
- Open Source Security Foundation. [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/).
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, February 1997.
- Rescorla, E. [RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446). IETF, August 2018.
- Eddy, W. (ed.). [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293). IETF, August 2022.
- U.S. Department of Health and Human Services. [Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). January 2024.
- U.S. Environmental Protection Agency. [America's Water Infrastructure Act of 2018: Risk Assessments and Emergency Response Plans](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans).

**Ética profissional**

- Association for Computing Machinery. [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics). 2018.

**Incidentes e evidências setoriais**

- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency and Federal Bureau of Investigation. [DarkSide Ransomware: Best Practices for Preventing Business Disruption from Ransomware Attacks (AA21-131A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a). May 2021, updated July 2021.
- Cybersecurity and Infrastructure Security Agency. [The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years). May 2023.
- Cybersecurity and Infrastructure Security Agency. [MAR-17-352-01 HatMan — Safety System Targeted Malware (Update B)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf). 2019.
- E-ISAC and SANS. [Analysis of the Cyber Attack on the Ukrainian Power Grid: Defense Use Case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and). March 2016 (archived copy).
- Langner, R. [Stuxnet: Dissecting a Cyberwarfare Weapon](https://doi.org/10.1109/MSP.2011.67). *IEEE Security & Privacy*, 9(3), 49–51, 2011.
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- National Audit Office. [Investigation: WannaCry Cyber Attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems*, 21(6), 11–25, 2001.
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.

**Computação, segurança, safety e resiliência**

- Bruneau, M., Chang, S. E., Eguchi, R. T., et al. [A Framework to Quantitatively Assess and Enhance the Seismic Resilience of Communities](https://doi.org/10.1193/1.1623497). *Earthquake Spectra*, 19(4), 733–752, 2003.
- Codd, E. F. [A Relational Model of Data for Large Shared Data Banks](https://doi.org/10.1145/362384.362685). *Communications of the ACM*, 13(6), 377–387, 1970.
- Diffie, W., and Hellman, M. [New Directions in Cryptography](https://doi.org/10.1109/TIT.1976.1055638). *IEEE Transactions on Information Theory*, 22(6), 644–654, 1976.
- Haimes, Y. Y. [On the Definition of Resilience in Systems](https://doi.org/10.1111/j.1539-6924.2009.01216.x). *Risk Analysis*, 29(4), 498–501, 2009.
- Leveson, N. [A New Accident Model for Engineering Safer Systems](https://doi.org/10.1016/S0925-7535(03)00047-X). *Safety Science*, 42(4), 237–270, 2004.
- Reason, J. [Human Error: Models and Management](https://doi.org/10.1136/bmj.320.7237.768). *BMJ*, 320(7237), 768–770, 2000.
- Rivest, R. L., Shamir, A., and Adleman, L. [A Method for Obtaining Digital Signatures and Public-Key Cryptosystems](https://doi.org/10.1145/359340.359342). *Communications of the ACM*, 21(2), 120–126, 1978.
- Saltzer, J. H., and Schroeder, M. D. [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939). *Proceedings of the IEEE*, 63(9), 1278–1308, 1975.

**Evidência, pesquisa e argumentação**

- Arp, D., Quiring, E., Pendlebury, F., et al. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). *USENIX Security Symposium*, 2022.
- Efron, B. [Bootstrap Methods: Another Look at the Jackknife](https://doi.org/10.1214/aos/1176344552). *The Annals of Statistics*, 7(1), 1–26, 1979.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *AAAI*, 2022.
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLoS Computational Biology*, 9(10), e1003285, 2013.
- Sargent, R. G. [Verification and Validation of Simulation Models](https://doi.org/10.1057/jos.2012.20). *Journal of Simulation*, 7(1), 12–24, 2013.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). *IEEE Symposium on Security and Privacy*, 2010.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003 (first published 1958).
- Wilson, E. B. [Probable Inference, the Law of Succession, and Statistical Inference](https://doi.org/10.1080/01621459.1927.10502953). *Journal of the American Statistical Association*, 22(158), 209–212, 1927.
