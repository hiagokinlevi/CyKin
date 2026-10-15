# Segurança de TO, IoT e Sistemas Ciberfísicos: Fundamentos e Trabalho de Conclusão do Bacharelado

- Idioma: português do Brasil (`pt`); curso de bacharelado, quatro anos; aproximadamente 3.200 horas de estudo planejado. Edição de referência: [inglês](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Os capítulos 1–40 de 40 têm texto didático escrito à mão; os exercícios EX001–EX120 têm resoluções correspondentes; os laboratórios offline usam a biblioteca padrão do Python 3, e as suas saídas foram incorporadas a partir de execuções reais. A revisão independente e a verificação de 300 páginas A4 continuam em aberto. Cobertura de capítulos em rascunho não é um livro concluído.
- Público: estudantes de segurança e de computação em geral que precisam de fundamentos rigorosos em segurança de TO, IoT e sistemas ciberfísicos, culminando num trabalho de conclusão e numa tese com escopo definido.
- Relação com os livros vizinhos: o [livro de engenharia](../../../../engineering-5-years/ot-iot-security/en/book/MANUSCRIPT.md) é centrado em projeto; o [livro de mestrado](../../../../masters-2-years/ot-iot-security/en/book/MANUSCRIPT.md) é guiado pela pesquisa. **Este livro equilibra fundamentos, teoria, casos, métodos e habilidades de pesquisa.**
- Autor: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original sob [CC0 1.0](../../../../../LICENSE); as obras citadas mantêm seus direitos.
- Limite educacional: não é um diploma credenciado. Não concede autorização para acessar plantas reais. Todas as plantas, pessoas e números dos exemplos são **sintéticos**, salvo quando uma frase cita uma fonte pública.

[Página do curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plano do livro](PLAN.md) · [Skill do curso](../../skill/SKILL.md) · [Resoluções](#worked-results)

## Como usar este rascunho

Os Capítulos 1–18 são fundamentos, cada um aplicado a uma planta desde a primeira página. Os Capítulos 19–32 formam o núcleo de TO, IoT e sistemas ciberfísicos, com o Laboratório I (25) e o Laboratório II (30). Os Capítulos 33–40 tratam de métodos de pesquisa, de um projeto comparativo, do trabalho de conclusão e da tese. Cada capítulo tem objetivos de aprendizagem, seções didáticas, um exemplo resolvido, um caso sintético identificado, erros e limites, três exercícios avaliados de 0 a 3, uma síntese e um bloco **Continue estudando**. Os laboratórios rodam offline com `python3 file.py`; nunca os aponte para um sistema real.

### Caso sintético recorrente

| Elemento | Papel | Limite |
|---|---|---|
| **Lakeside District Heating Plant (LDHP)** — CLP de controle da caldeira PLC-H, trip de segurança SIS-H, HMI-1, historiador HIST-1, estação de engenharia EWS-1, medidores de calor IoT e gateways de medidores | Sistema estudado ao longo de todo o livro | Inventado |
| **Maya Chen** | Estudante de graduação em estágio no escritório de engenharia da LDHP | Inventada |

### Fontes principais

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [série ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); alertas da CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a) e [AA22-103A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-103a); ICS-CERT [IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). Lista completa em [Referências](#references).

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
15. [Evidências e medição](#ch-15)
16. [Arquitetura de segurança](#ch-16)
17. [Conceitos de criptografia](#ch-17)
18. [Métodos de pesquisa I](#ch-18)
19. [Segurança de TO, IoT e sistemas ciberfísicos: escopo e teoria](#ch-19)
20. [Segurança de TO, IoT e sistemas ciberfísicos: casos fundamentais](#ch-20)
21. [Segurança de TO, IoT e sistemas ciberfísicos: modelos de sistema](#ch-21)
22. [Segurança de TO, IoT e sistemas ciberfísicos: dados e dependências](#ch-22)
23. [Segurança de TO, IoT e sistemas ciberfísicos: métodos I](#ch-23)
24. [Segurança de TO, IoT e sistemas ciberfísicos: controles](#ch-24)
25. [Laboratório I](#ch-25)
26. [Segurança de TO, IoT e sistemas ciberfísicos: métodos II](#ch-26)
27. [Segurança de TO, IoT e sistemas ciberfísicos: verificação](#ch-27)
28. [Segurança de TO, IoT e sistemas ciberfísicos: análise de falhas](#ch-28)
29. [Segurança de TO, IoT e sistemas ciberfísicos: operações](#ch-29)
30. [Laboratório II](#ch-30)
31. [Segurança de TO, IoT e sistemas ciberfísicos: casos avançados](#ch-31)
32. [Segurança de TO, IoT e sistemas ciberfísicos: interfaces interdisciplinares](#ch-32)
33. [Métodos de pesquisa II](#ch-33)
34. [Projeto comparativo](#ch-34)
35. [Proposta do trabalho de conclusão](#ch-35)
36. [Prática de campo ou comunitária](#ch-36)
37. [Seminário de revisão de evidências](#ch-37)
38. [Implementação do trabalho de conclusão](#ch-38)
39. [Avaliação do trabalho de conclusão](#ch-39)
40. [Tese e apresentação](#ch-40)

Apêndices: [Resoluções](#worked-results) · [Referências](#references).

<a id="ch-01"></a>

## Capítulo 1 — Raciocínio matemático

### Objetivos de aprendizagem

Ao final deste capítulo você será capaz de (1) transformar uma frase sobre a planta numa grandeza com unidades; (2) estimar uma ordem de grandeza antes de calcular; (3) enunciar a hipótese que torna um cálculo válido; e (4) reconhecer quando um número de aparência precisa esconde um palpite. O caso recorrente é a Lakeside District Heating Plant (LDHP), uma planta sintética de aquecimento distrital.

### 1.1 Por que um estudante de TO precisa de hábitos de prova

Afirmações de segurança sobre uma planta de aquecimento são quantitativas, admitamos isso ou não. "A mudança na rede é de baixo risco" quer dizer, na verdade, "a probabilidade de perder o controle da temperatura de ida, multiplicada pelo dano às residências, está abaixo de um limiar que aceitamos". O raciocínio matemático torna visíveis os termos ocultos. O hábito é simples: escreva toda grandeza com a sua unidade, nomeie a hipótese que a liga à grandeza seguinte e confira o resultado com uma estimativa grosseira feita antes de tocar em qualquer calculadora.

### 1.2 Unidades e verificações dimensionais

O aquecimento distrital mistura quilowatts, metros cúbicos por hora, graus Celsius e segundos. A potência térmica entregue é aproximadamente P = ρ · c · Q · ΔT, com densidade da água ρ ≈ 1000 kg/m³ e calor específico c ≈ 4,19 kJ/(kg·K). Se você escrever Q em m³/h, precisa dividir por 3600 para obter kg/s. Uma verificação dimensional pega esse deslize antes que ele vire um argumento errado de dimensionamento de caldeira num registro de riscos. O primeiro memorando de Maya precisava exatamente dessa verificação: um erro de 5 K no setpoint é um ΔT, de modo que o déficit escala com a vazão, e uma vazão expressa em m³/h dá um número 3600 vezes grande demais se não for convertida antes para kg/s.

### 1.3 Implicação, contrapositiva e contraexemplo

"Se o SIS é independente, então um comprometimento do SCADA não consegue desabilitar o trip." A contrapositiva — "se um comprometimento do SCADA consegue desabilitar o trip, o SIS não é independente" — é logicamente equivalente e muitas vezes mais fácil de testar. A recíproca não é equivalente: um trip que sobrevive a um teste não prova independência. Um único contraexemplo documentado, como uma estação de engenharia compartilhada que consegue fazer download para os dois controladores, refuta uma afirmação universal. Na LDHP, o contraexemplo a procurar é a EWS-1: se uma única estação de engenharia consegue baixar lógica tanto para o PLC-H quanto para o SIS-H, a afirmação de que o SIS-H é independente de um comprometimento da zona de controle é falsa, por mais testes de trip que o SIS-H tenha passado.

### Exemplo resolvido (LDHP sintética)

A LDHP bombeia Q = 180 m³/h com ΔT = 30 K. Primeiro, estime: 0,05 m³/s × 1000 kg/m³ × 4,19 kJ/(kg·K) × 30 K ≈ 6.300 kW. Cálculo exato: 180/3600 = 0,05 m³/s, logo P = 50 kg/s × 4,19 × 30 = 6.285 kW ≈ 6,3 MW. Se um atacante só conseguisse alterar o setpoint de ida em 5 K, o ΔT cairia para 25 K e o calor entregue cairia para 5.237,5 kW, um déficit de 1.047,5 kW. Esse déficit, e não o pacote, é a consequência que um dono de risco consegue pesar.

> **Caso sintético — Lakeside District Heating Plant.** A estudante Maya Chen entra no escritório de engenharia da LDHP. O seu primeiro memorando precisa expressar em quilowatts o déficit de calor causado por um erro de 5 K no setpoint, com todas as hipóteses listadas.

### Erros e limites

A fórmula do calor ignora as perdas na tubulação e o fato de que a densidade e a capacidade térmica variam com a temperatura. Uma resposta com dois algarismos significativos é honesta; seis dígitos sugerem um conhecimento que você não tem.

### Exercícios

- **EX001 — Calor com vazão reduzida.** A vazão da LDHP cai para 150 m³/h enquanto o ΔT continua em 30 K. Calcule a potência entregue e mostre a conversão de unidades. *Rubrica:* 3 = 5.237,5 kW com a conversão m³/h→kg/s mostrada; 2 = valor correto, sem conversão; 1 = esqueceu o /3600; 0 = nenhuma tentativa.
- **EX002 — Contrapositiva de uma afirmação de zoneamento.** Escreva a contrapositiva de "se o gateway de medidores não tem rota para a zona de controle, ele não consegue escrever no PLC-H". *Rubrica:* 3 = contrapositiva correta e por que ela é testável; 2 = apenas a forma correta; 1 = dá a recíproca; 0 = nada.
- **EX003 — Estimar antes de calcular.** Dê, numa linha, uma estimativa de ordem de grandeza do calor diário entregue a 6,3 MW. *Rubrica:* 3 = ≈150 MWh/dia com o método; 2 = ordem correta; 1 = erro de unidade; 0 = nada.

### Síntese

Grandezas com unidades, hipóteses ditas em voz alta e contraexemplos procurados: esses três hábitos transformam uma opinião de segurança sobre uma planta num argumento que outra pessoa consegue conferir.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue estudando — capítulo 01 de 40

[← Página do curso](../../README.md) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Sistemas computacionais

### Objetivos de aprendizagem

Você vai (1) descrever as camadas de um controlador lógico programável, da placa de E/S ao ciclo de varredura; (2) contrastar um CLP com um servidor de uso geral; (3) explicar por que a temporização determinística é uma propriedade de segurança em TO; e (4) listar o que uma imagem de firmware contém.

### 2.1 O ciclo de varredura

Um CLP lê entradas, executa a lógica, escreve saídas e atende às comunicações, repetidamente. Na LDHP, o PLC-H da caldeira completa esse laço a cada 20 ms. Se o tratamento das comunicações cresce — por exemplo, porque um historiador mal configurado consulta 400 registradores a cada 50 ms —, o tempo de varredura se alonga e o watchdog pode levar o controlador a uma parada segura. Em TO, uma negação de serviço pode, portanto, chegar como tráfego comum que é simplesmente demais. Maya encontrou isso na segunda semana: um projeto de painel pedia "todas as tags, a cada varredura". Convertido em tempo de varredura, esse pedido teria carregado o tratamento de comunicações do PLC-H em todo ciclo de 20 ms, então ela recomendou ler o historiador.

### 2.2 CLP versus servidor

Um servidor é projetado para rodar muitos programas, aceitar atualizações e se recuperar com uma reinicialização. Um CLP é projetado para rodar um único programa durante anos, muitas vezes sem contas de usuário, com registro limitado e com firmware que o fabricante assina (ou, em modelos mais antigos, não assina). Reiniciar um servidor é rotina; reiniciar um controlador numa casa de caldeiras em operação exige permissão de trabalho, presença do operador e um plano para manter o processo seguro. Para o PLC-H, isso significa que uma correção de firmware não pode simplesmente ser aplicada numa terça-feira à tarde: ela precisa da janela mensal de quatro horas, de uma permissão de trabalho e da presença do líder de turno.

### 2.3 O que vive no firmware

O firmware reúne um sistema operacional de tempo real, pilhas de protocolos, o runtime que executa ladder ou texto estruturado e um bootloader. Daí decorrem consequências de segurança: um defeito na pilha de protocolos pode afetar todos os programas do dispositivo, e um caminho de atualização não assinado permite que qualquer pessoa que alcance a porta de engenharia substitua o runtime. O NIST SP 800-82r3 trata a integridade do firmware e o download controlado de programas como práticas centrais de TO. Para o PLC-H, a pergunta prática é quem consegue alcançar a porta de engenharia: se a EWS-1 é o único host que consegue, proteger a EWS-1 protege o runtime; se a VLAN do escritório também alcança a porta 502, o comportamento de assinatura do firmware passa a ser a última barreira.

### Exemplo resolvido (LDHP sintética)

O PLC-H tem uma varredura-alvo de 20 ms e um watchdog de 100 ms. A lógica leva 9 ms, a E/S 4 ms, e cada requisição Modbus custa 0,6 ms para ser atendida. Com 10 requisições por varredura, o ciclo é 9 + 4 + 6 = 19 ms. Se um novo painel acrescenta 30 requisições por varredura, o ciclo passa a 37 ms: ainda abaixo do watchdog, mas a temporização de 20 ms que as malhas sintonizadas esperam se perde, e a qualidade do controle se degrada antes que qualquer alarme dispare.

> **Caso sintético — Lakeside District Heating Plant.** Maya encontra um projeto de painel que pede "todas as tags, a cada varredura". Ela converte o pedido em milissegundos de varredura e recomenda consultar o historiador, e não o controlador.

### Erros e limites

Os modelos de varredura dos fabricantes diferem; alguns atendem às comunicações numa tarefa separada. Nunca meça o impacto na varredura carregando um controlador em produção — use uma unidade de bancada ou os números do fabricante.

### Exercícios

- **EX004 — Carga de comunicações e tempo de varredura.** Com 9 ms de lógica, 4 ms de E/S e 0,6 ms por requisição, quantas requisições por varredura mantêm o PLC-H em 20 ms ou menos? *Rubrica:* 3 = 11 requisições, com o cálculo; 2 = número certo, sem cálculo; 1 = ignora a E/S; 0 = nada.
- **EX005 — Hábitos de servidor que prejudicam controladores.** Cite dois hábitos de administração de servidores que são inseguros num CLP em operação e dê a alternativa de TO para cada um. *Rubrica:* 3 = dois hábitos com alternativas; 2 = um par; 1 = hábitos sem alternativas; 0 = nada.
- **EX006 — Camadas do firmware e raio de impacto.** Explique por que uma vulnerabilidade na pilha de protocolos de um controlador tem impacto mais amplo que um defeito num degrau do ladder. *Rubrica:* 3 = a pilha compartilhada atende a todos os programas e é alcançável antes de a lógica rodar; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Um controlador é primeiro uma máquina temporizada e só depois um computador; a sua segurança começa por respeitar o ciclo de varredura e controlar o que pode ser carregado nele.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue estudando — capítulo 02 de 40

[← Capítulo 01](#ch-01) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Programação I

### Objetivos de aprendizagem

Você vai (1) ler dados estruturados com a biblioteca padrão do Python; (2) validar valores contra faixas de engenharia; (3) escrever saídas que um revisor consiga conferir linha a linha; e (4) explicar por que o código de validação é um artefato relevante para a segurança.

### 3.1 Tags como registros

Uma lista de tags de TO é uma tabela: nome da tag, unidade de engenharia, limites inferior e superior, valor atual. O módulo `csv` do Python lê essas tabelas sem pacotes de terceiros, o que importa em laptops de engenharia bloqueados, onde instalar software exige aprovação. Trate cada linha como um dicionário e mantenha o texto bruto separado dos números interpretados, para que uma falha de interpretação fique visível em vez de virar zero em silêncio. No laboratório de tags, é guardar o texto bruto que permite que a nota de Maya diga "FT-301 leu −3,0 m³/h" em vez de relatar um campo vazio ou um zero; o técnico de instrumentação pode então olhar o valor exato que o medidor enviou e decidir se a culpa é da escala ou da fiação.

### 3.2 Validação de faixa

Uma temperatura de 141 °C numa sonda calibrada para 20–130 °C é uma excursão real, um sensor com defeito ou um valor manipulado. O código não sabe dizer qual; ele pode sinalizar a linha e impedir que ela chegue a um relatório rotulado como "normal". O mesmo vale para uma vazão negativa, fisicamente impossível num medidor unidirecional e, portanto, sempre uma questão de qualidade ou de integridade dos dados. O laboratório de tags sinaliza exatamente essas duas linhas: TT-102 a 141,0 °C contra um limite de 130 °C, e FT-301 a −3,0 m³/h. Maya envia a primeira imediatamente ao operador e a segunda à instrumentação, como suspeita de falha de fiação ou de escala.

### 3.3 Saída legível

Imprima uma decisão por linha, junto com a entrada que a causou. Os revisores dos comitês de mudança da planta raramente são programadores; eles vão confiar numa saída que consigam rastrear até uma linha.

```python
"""Lab 03: validate a synthetic LDHP tag list (no plant access)."""
import csv, io
RAW = """tag,unit,lo,hi,value
TT-101,degC,20,130,96.5
TT-102,degC,20,130,141.0
PT-201,bar,0,16,9.8
FT-301,m3/h,0,250,-3.0
LT-401,pct,0,100,57
"""
bad = []
for row in csv.DictReader(io.StringIO(RAW)):
    v, lo, hi = float(row["value"]), float(row["lo"]), float(row["hi"])
    ok = lo <= v <= hi
    print(f"{row['tag']:7} {v:7.1f} {row['unit']:5} {'ok' if ok else 'OUT-OF-RANGE'}")
    if not ok: bad.append(row["tag"])
print("flagged:", ", ".join(bad))
```

Execute com `python3 lab_tags.py`. Saída verificada:

```text
TT-101     96.5 degC  ok
TT-102    141.0 degC  OUT-OF-RANGE
PT-201      9.8 bar   ok
FT-301     -3.0 m3/h  OUT-OF-RANGE
LT-401     57.0 pct   ok
flagged: TT-102, FT-301
```

Na LDHP, as duas linhas sinalizadas são impressas como `TT-102    141.0 degC  OUT-OF-RANGE` e `FT-301     -3.0 m3/h  OUT-OF-RANGE`, com o valor de entrada na mesma linha da decisão; encaminhar cada sinalização ao operador ou à instrumentação é um julgamento de Maya na sua nota, e não algo que o script decide. Um revisor do comitê de mudanças que é engenheiro de controle, e não programador, consegue conferir cada linha contra o índice de instrumentos em um minuto e não precisa ler o script. Se uma linha não pode ser rastreada até um registro, o revisor não tem motivo para confiar nela; por isso a saída nunca deve imprimir uma contagem-resumo sem as linhas que a sustentam.

### Exemplo resolvido (LDHP sintética)

O laboratório sinaliza TT-102 (141,0 °C, acima de 130) e FT-301 (−3,0 m³/h, abaixo de 0). A nota de Maya separa as duas: TT-102 pode ser uma leitura alta genuína e vai imediatamente para o operador; FT-301 é fisicamente impossível e vai para a instrumentação como suspeita de falha de fiação ou de escala, com revisão de integridade se a falha não puder ser explicada.

> **Caso sintético — Lakeside District Heating Plant.** A lista de tags do laboratório é inventada; os limites reais da LDHP viriam do índice de instrumentos mantido pelos engenheiros de controle.

### Erros e limites

Verificações de faixa pegam erros grosseiros, não manipulações sutis dentro da faixa. A comparação em ponto flutuante no limite exige uma regra declarada (aqui, inclusiva). O script lê uma string, não um sistema ao vivo.

### Exercícios

- **EX007 — Ampliando a tabela de tags.** Acrescente a linha `TT-103,degC,20,130,130.0`. O que o laboratório imprime para ela e por quê? *Rubrica:* 3 = ok, porque os limites são inclusivos; 2 = ok sem justificativa; 1 = diz fora da faixa; 0 = nada.
- **EX008 — Valores não interpretáveis.** Descreva o que o script faz se uma célula de valor contiver `n/a` e proponha uma correção. *Rubrica:* 3 = um ValueError interrompe a execução; capturá-lo e sinalizar BAD-VALUE; 2 = um dos dois; 1 = diz que vira zero; 0 = nada.
- **EX009 — Triagem de duas sinalizações.** Explique por que TT-102 e FT-301 vão para pessoas diferentes. *Rubrica:* 3 = excursão plausível vs valor impossível, operador vs instrumentação; 2 = parcial; 1 = trata as duas da mesma forma; 0 = nada.

### Síntese

Programas pequenos e legíveis, feitos só com a biblioteca padrão, que sinalizam em vez de corrigir, são a primeira ferramenta em que um estudante de segurança de TO deve confiar e que deve ser capaz de defender.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue estudando — capítulo 03 de 40

[← Capítulo 02](#ch-02) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Escrita acadêmica

### Objetivos de aprendizagem

Você vai (1) estruturar um memorando técnico como afirmação, evidência e limitação; (2) citar uma norma pelo seu identificador e edição exatos; (3) escrever para um operador, um engenheiro e um gestor sem mudar os fatos; e (4) evitar linguagem inflada em achados de segurança.

### 4.1 Afirmação, evidência, limitação

Todo parágrafo de um memorando de segurança de TO deve permitir que o leitor encontre três coisas: o que você afirma, o que você observou que sustenta a afirmação e onde ela termina. "A porta 502 do PLC-H é alcançável a partir da VLAN do escritório (observado na exportação aprovada das regras do firewall de 3 de março); não testamos se escritas são bem-sucedidas" é uma frase melhor que "o PLC-H está escancarado", porque é verificável e honesta quanto ao escopo. O memorando de Maya usou essa frase quase palavra por palavra, e a única pergunta do líder de turno, o que os operadores deveriam fazer de diferente esta noite, pôde ser respondida porque a limitação estava declarada.

### 4.2 Citar normas com precisão

Escreva "NIST SP 800-82 Rev. 3 (setembro de 2023)", e não "orientação do NIST". Na família 62443, nomeie a parte: a IEC 62443-3-3 trata de requisitos de segurança de sistema e de níveis de segurança; a IEC 62443-2-1 trata do programa de segurança do proprietário do ativo; a IEC 62443-4-2 trata de requisitos de componentes. O leitor precisa conseguir abrir o documento exato. Não cite um número de cláusula que você não leu. A proposta posterior de SL-T de Maya para a LDHP cita a IEC 62443-3-2 pela parte, para o método de zonas, e a IEC 62443-3-3 para os requisitos, em vez de "62443" para ambos. Um leitor que queira conferir o seu SL-T 3 para a zona de controle da caldeira precisa abrir a parte que define os níveis de segurança, e não uma família de catorze documentos.

### 4.3 Um fato, três públicos

O operador precisa saber o que observar; o engenheiro precisa do caminho técnico; o gestor precisa de custo, tempo de parada e risco residual. Mantenha os fatos idênticos entre as versões — só mudam a ênfase e o vocabulário. Se as versões discordam nos fatos, uma delas está errada. Para o achado do PLC-H, o operador ouve "se o setpoint de ida mudar sem uma solicitação da HMI-1, chame o líder de turno"; o engenheiro ouve "porta 502 alcançável a partir da VLAN do escritório segundo a exportação de regras de 3 de março; escritas não testadas"; o gestor ouve o custo da mudança no firewall e o risco residual até que ela seja feita. As três versões nomeiam a mesma porta, a mesma data e a mesma pergunta não testada.

### Exemplo resolvido (LDHP sintética)

Fraco: "Hackers poderiam assumir o controle da caldeira, o que é extremamente perigoso." Reescrito: "Um host na VLAN do escritório consegue abrir conexões Modbus/TCP com o PLC-H (regra 14 na exportação de 3 de março). Não testamos o acesso de escrita. O trip de alta temperatura do SIS-H é cabeado e não depende desse caminho. Recomendado: remover a regra 14 e encaminhar as leituras do historiador pela DMZ." A reescrita traz o local, a evidência, o escopo não testado, a salvaguarda independente e uma ação.

> **Caso sintético — Lakeside District Heating Plant.** O memorando de Maya é revisado pelo líder de turno da planta, que faz uma única pergunta: "O que os meus operadores devem fazer de diferente esta noite?" O memorando precisa respondê-la.

### Erros e limites

Evite "nível militar", "totalmente seguro" e "risco zero". A voz passiva que esconde quem observou o quê enfraquece a evidência. Uma revisão de literatura não substitui a sua própria observação.

### Exercícios

- **EX010 — Reescrevendo um achado inflado.** Reescreva "o historiador é uma backdoor enorme" como uma frase de afirmação–evidência–limitação para a LDHP. *Rubrica:* 3 = as três partes, com uma observação concreta; 2 = duas partes; 1 = continua inflada; 0 = nada.
- **EX011 — Escolhendo a parte certa da 62443.** Qual parte da IEC 62443 você citaria para um requisito sobre a capacidade de autenticação do próprio PLC-H, e qual para o programa de gestão de patches da planta? *Rubrica:* 3 = 4-2 e 2-1 (2-3 também aceitável para patches), com justificativas; 2 = uma correta; 1 = cita apenas "62443"; 0 = nada.
- **EX012 — Versão para o operador.** Escreva a versão em duas frases, para o operador, do achado da regra 14. *Rubrica:* 3 = sintoma observável mais ação; 2 = um dos dois; 1 = só jargão técnico; 0 = nada.

### Síntese

Boa escrita de TO é verificável: fontes exatas, evidência observada e limites declarados, em palavras com as quais cada público consegue agir.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue estudando — capítulo 04 de 40

[← Capítulo 03](#ch-03) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Letramento em segurança

### Objetivos de aprendizagem

Você vai (1) definir confidencialidade, integridade e disponibilidade para uma planta de aquecimento; (2) acrescentar segurança física (safety) e confiabilidade como propriedades de primeira classe; (3) separar ameaça, vulnerabilidade e consequência; e (4) mapear uma técnica pública do MITRE ATT&CK for ICS para um ativo da LDHP.

### 5.1 A ordem de preocupação em TO

Na TI de escritório, a confidencialidade costuma vir na frente. Numa planta de aquecimento distrital, a ordem em geral se inverte: primeiro a segurança das pessoas e dos equipamentos, depois a disponibilidade e a integridade do controle, e só então a confidencialidade dos dados. Tabelas de receitas ou leituras dos medidores dos clientes continuam importando — os dados dos medidores são dados pessoais —, mas uma planilha vazada não escalda ninguém, enquanto um setpoint manipulado pode escaldar. Maya aplicou isso quando o gerente da planta perguntou se devia criptografar primeiro o banco de dados do historiador: ela classificou acima a separação entre a rede do escritório e o PLC-H, porque uma escrita de setpoint pode cortar o calor das casas e uma cópia do banco de dados não pode.

### 5.2 Ameaça, vulnerabilidade, consequência

Uma ameaça é um agente ou evento com a intenção ou o potencial de causar dano. Uma vulnerabilidade é uma fraqueza que torna o dano possível. Uma consequência é o que de fato acontece com o processo. Os estudantes costumam confundi-las: "o Modbus não tem autenticação" é uma vulnerabilidade, "um terceirizado insatisfeito" é uma fonte de ameaça e "perda de calor para 4.000 casas em janeiro" é uma consequência. Declarações de risco precisam das três. A declaração de risco de Maya para o PLC-H as une: um terceirizado na rede do escritório (ameaça) consegue escrever no registrador 100 porque o Modbus não tem autenticação e a porta 502 é alcançável (vulnerabilidade), baixando o setpoint de ida para 30 °C e cortando o calor de 4.000 casas (consequência).

### 5.3 O ATT&CK for ICS como vocabulário

O MITRE ATT&CK for ICS cataloga comportamentos de adversários observados contra sistemas industriais. A técnica T0836 *Modify Parameter* descreve a alteração de parâmetros do controlador, como setpoints ou limites, para causar um efeito; a T0883 *Internet Accessible Device* descreve alcançar controladores expostos diretamente à internet. Use esses identificadores para descrever comportamentos com precisão — não como uma lista de verificação que alega ser completa. Na LDHP, a T0836 descreve o cenário ao qual este livro mais retorna: uma escrita no holding register 100, o setpoint de temperatura de ida. A T0883 descreve o controlador de aquecimento "real" do colega, encontrado num motor de busca no Capítulo 10. Nomeá-las permite que Maya ligue as suas notas a alertas públicos sem sugerir que a planta tenha sofrido qualquer uma delas.

### Exemplo resolvido (LDHP sintética)

Declaração: "Uma parte não autorizada com acesso à VLAN do escritório (ameaça) poderia usar o caminho Modbus não autenticado pela regra 14 (vulnerabilidade) para alterar o setpoint de ida, comportamento descrito pela técnica T0836 Modify Parameter do ATT&CK for ICS, reduzindo o calor entregue em cerca de 1 MW (consequência, do Capítulo 1); o SIS-H cabeado limita o dano por sobretemperatura." Cada oração é separável, e cada uma pode ser contestada.

> **Caso sintético — Lakeside District Heating Plant.** O gerente da planta pergunta se criptografar o banco de dados do historiador é a prioridade máxima. Maya o classifica abaixo da separação entre o escritório e o PLC-H e explica por quê, usando a ordem de preocupação de TO.

### Erros e limites

O ATT&CK lista comportamentos observados; a ausência de uma técnica não prova que ela não possa acontecer. Segurança física (safety) não é o mesmo que segurança da informação (security), e controles de segurança nunca podem enfraquecer uma função de segurança física.

### Exercícios

- **EX013 — Separando ameaça, fraqueza e dano.** Classifique: (a) "senha padrão no gateway de medidores", (b) "grupo de ransomware", (c) "a caldeira desarma e o distrito fica sem calor por seis horas". *Rubrica:* 3 = vulnerabilidade, ameaça, consequência; 2 = duas certas; 1 = uma; 0 = nada.
- **EX014 — Priorizando na LDHP.** Justifique colocar a integridade do setpoint acima da confidencialidade dos dados dos medidores na LDHP, sem dizer que a confidencialidade não importa. *Rubrica:* 3 = consequência física vs dano à privacidade, ambas mantidas; 2 = só a ordem; 1 = descarta a privacidade; 0 = nada.
- **EX015 — Mapeando um gateway exposto.** Qual ID de técnica do ATT&CK for ICS descreve o gateway de medidores alcançável a partir da internet, e o que esse mapeamento não prova? *Rubrica:* 3 = T0883 e "não prova exploração nem completude"; 2 = só o ID; 1 = ID errado; 0 = nada.

### Síntese

Letramento em segurança em TO significa falar com precisão sobre ameaças, fraquezas e consequências físicas, com a segurança física no topo e vocabulários compartilhados usados com honestidade.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue estudando — capítulo 05 de 40

[← Capítulo 04](#ch-04) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Estruturas discretas

### Objetivos de aprendizagem

Você vai (1) modelar zonas e conduítes como um grafo dirigido; (2) calcular alcançabilidade com busca em largura; (3) raciocinar sobre qual remoção de uma única aresta desconecta um nó crítico; e (4) usar conjuntos para expressar listas de permissão.

### 6.1 Zonas e conduítes como grafo

A IEC 62443-3-2 pede que os proprietários de ativos dividam um sistema em zonas (grupos de ativos que compartilham requisitos de segurança) ligadas por conduítes (os canais de comunicação entre zonas). Um grafo dirigido captura isso: os nós são zonas, e as arestas são conduítes na direção em que uma sessão pode ser aberta. Um caminho da zona corporativa até a zona de segurança é uma pergunta de alcançabilidade no grafo, que se torna mecânica depois que o grafo é desenhado com honestidade. No grafo do laboratório, Maya registra os conduítes como pares ordenados, de modo que MeterGW→SCADA e Control→SIS sejam arestas visíveis, e não linhas num desenho.

### 6.2 Busca em largura

A busca em largura (BFS) visita um nó inicial, depois todos os seus vizinhos, depois os vizinhos deles, marcando cada nó visitado uma única vez. Ela roda em tempo proporcional ao número de nós mais o de arestas, de modo que até a lista de conduítes de uma grande refinaria é verificada instantaneamente. O perigo não está no algoritmo, mas na entrada: um modem esquecido de um fornecedor ou um laptop com duas interfaces é uma aresta que o diagrama omite.

```python
"""Lab 06: reachability over a synthetic LDHP zone/conduit graph (BFS)."""
from collections import deque
CONDUITS = {"Enterprise": ["DMZ"], "DMZ": ["SCADA"], "SCADA": ["Control"],
            "Control": ["SIS"], "MeterCloud": ["MeterGW"], "MeterGW": ["SCADA"], "SIS": []}
def reach(src):
    seen, q = {src}, deque([src])
    while q:
        for n in CONDUITS.get(q.popleft(), []):
            if n not in seen: seen.add(n); q.append(n)
    return seen
for z in ["Enterprise", "MeterCloud", "SCADA"]:
    r = sorted(reach(z) - {z}); print(f"{z:10} -> {r}  SIS reachable: {'SIS' in r}")
CONDUITS["Control"] = []  # design change: SIS gets its own hardwired trip, no Control->SIS data conduit
print("after removing Control->SIS:", "SIS" in reach("Enterprise"))
```

Execute com `python3 lab_reach.py`. Saída verificada:

```text
Enterprise -> ['Control', 'DMZ', 'SCADA', 'SIS']  SIS reachable: True
MeterCloud -> ['Control', 'MeterGW', 'SCADA', 'SIS']  SIS reachable: True
SCADA      -> ['Control', 'SIS']  SIS reachable: True
after removing Control->SIS: False
```

Na LDHP, um modem de fornecedor que ninguém registrou, ou a EWS-1 ligada ao mesmo tempo às redes do escritório e de controle, acrescentaria uma aresta que o laboratório não tem como conhecer; a resposta da BFS só é tão verdadeira quanto a lista de conduítes.

### 6.3 Arestas de corte

Uma aresta cuja remoção desconecta as zonas expostas ao atacante da zona crítica é uma aresta de corte para esse par. No laboratório, Control→SIS é uma aresta assim: removê-la torna o SIS inalcançável a partir de Enterprise e de MeterCloud. A engenharia muitas vezes prefere remover por completo um conduíte de dados para um sistema de segurança e confiar em trips cabeados, que é exatamente o que a mudança de projeto do laboratório representa. A nota de Maya acrescenta o segundo passo: a aresta MeterGW→SCADA existe apenas para que o faturamento leia os totais de vazão, então substituí-la por uma exportação unidirecional a partir do historiador remove o outro caminho da nuvem de medidores em direção à zona de controle.

### Exemplo resolvido (LDHP sintética)

O laboratório mostra a nuvem de medidores alcançando o SIS por MeterGW → SCADA → Control → SIS. Maya expressa a lista de conduítes como um conjunto de pares ordenados e observa que a aresta MeterGW→SCADA existe apenas para que o faturamento leia os totais de vazão. Substituí-la por uma exportação unidirecional a partir do historiador remove um segundo caminho; remover Control→SIS remove o último.

> **Caso sintético — Lakeside District Heating Plant.** Os nomes de zonas e os conduítes do laboratório foram inventados para manter o grafo pequeno o bastante para ser conferido à mão.

### Erros e limites

A alcançabilidade diz que uma sessão pode ser aberta, não que ela terá sucesso nem o que ela pode fazer. Desenhos não dirigidos escondem a diferença entre "o SCADA consulta o gateway" e "o gateway consegue se conectar ao SCADA".

### Exercícios

- **EX016 — Seguindo uma BFS à mão.** Liste a ordem em que a BFS a partir de MeterCloud visita os nós no grafo original. *Rubrica:* 3 = MeterCloud, MeterGW, SCADA, Control, SIS; 2 = conjunto certo, ordem errada; 1 = falta um nó; 0 = nada.
- **EX017 — Um modem de fornecedor omitido.** Um modem de fornecedor dá à internet um conduíte direto para Control. Depois da mudança de projeto do laboratório, o SIS é alcançável a partir da internet? *Rubrica:* 3 = não, Control não tem aresta de saída para o SIS depois da mudança, mas o próprio Control agora está exposto; 2 = só "não"; 1 = "sim"; 0 = nada.
- **EX018 — Lista de permissão como conjunto.** Expresse "o HIST-1 pode ler do PLC-H; a HMI-1 pode ler e escrever no PLC-H" como um conjunto de tuplas (origem, destino, ação). *Rubrica:* 3 = três tuplas, nada a mais; 2 = pequeno excesso; 1 = usa faixas de hosts; 0 = nada.

### Síntese

Desenhar zonas e conduítes como um grafo dirigido transforma argumentos de segmentação em verificações que qualquer pessoa pode executar de novo — desde que o grafo inclua todas as arestas reais.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue estudando — capítulo 06 de 40

[← Capítulo 05](#ch-05) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Redes e protocolos

### Objetivos de aprendizagem

Você vai (1) decodificar o cabeçalho MBAP e o código de função do Modbus/TCP a partir de bytes brutos; (2) distinguir códigos de função de leitura e de escrita; (3) explicar por que o Modbus não oferece autenticação; e (4) dizer o que um decodificador de protocolo pode e não pode contar a um analista.

### 7.1 Modbus/TCP num quadro

O Modbus/TCP carrega um cabeçalho MBAP de sete bytes — identificador de transação (2 bytes), identificador de protocolo (2, sempre zero), comprimento (2) e identificador de unidade (1) —, seguido da unidade de dados de protocolo, que começa com um código de função de um byte. A Modbus Application Protocol Specification V1.1b3 define os códigos: 3 lê holding registers, 6 escreve um único registrador, 16 escreve vários registradores. No laboratório do decodificador, o quadro 2 traz o código de função 6 e o quadro 3, o código de função 16; ambos são escritas, e é por isso que a lista de permissão do Capítulo 27 se preocupa com o código de função antes do endereço.

### 7.2 Nenhuma identidade no protocolo

Nada no quadro diz quem o enviou. Qualquer host que consiga abrir a porta TCP 502 de um controlador pode emitir uma escrita, se o dispositivo aceitá-la. A segurança precisa, portanto, vir da rede (segmentação, listas de permissão) ou de uma variante protegida como o Modbus/TCP Security, que envolve o protocolo em TLS com papéis baseados em certificados.

```python
"""Lab 07: decode synthetic Modbus/TCP request headers (offline bytes only)."""
import struct
FC = {1: "read coils", 3: "read holding registers", 4: "read input registers",
      5: "write single coil", 6: "write single register", 16: "write multiple registers"}
frames = ["000100000006010300640002", "00020000000601060064012c", "000300000006011000c80001"]
for h in frames:
    b = bytes.fromhex(h)
    tid, pid, length, unit, fc = struct.unpack(">HHHBB", b[:8])
    addr, val = struct.unpack(">HH", b[8:12])
    kind = "WRITE" if fc in (5, 6, 15, 16) else "read"
    print(f"tid={tid} unit={unit} fc={fc} ({FC[fc]}) addr={addr} arg={val} -> {kind}")
```

Execute com `python3 lab_modbus.py`. Saída verificada:

```text
tid=1 unit=1 fc=3 (read holding registers) addr=100 arg=2 -> read
tid=2 unit=1 fc=6 (write single register) addr=100 arg=300 -> WRITE
tid=3 unit=1 fc=16 (write multiple registers) addr=200 arg=1 -> WRITE
```

Para o PLC-H, que não consegue autenticar clientes Modbus, esse é todo o argumento para os controles compensatórios do Capítulo 24: a lista de permissão do firewall que nomeia a HMI-1 e o HIST-1 como as únicas origens permitidas é a verificação de identidade que falta ao protocolo. Um host na VLAN do escritório que alcance a porta 502 é, para o PLC-H, indistinguível da HMI-1.

### 7.3 Lendo a saída

O quadro 2 escreve o valor 300 no registrador 100; o quadro 3 é uma escrita de vários registradores começando em 200. Observe que o decodificador imprime o endereço inicial e o primeiro argumento, mas não sabe o que o registrador 100 *significa* — isso vem do mapa de registradores do CLP, que é documentação da planta, e não protocolo. No mapa de registradores da LDHP, o registrador 100 guarda o setpoint de temperatura de ida em décimos de grau, de modo que o valor 300 significa 30,0 °C, muito abaixo do ponto de operação de 90 °C. Essa é a diferença entre "escrever um único registrador" e "possível perda de calor". A nota de Maya acrescenta uma coluna de mapa de registradores exatamente por isso, e marca a escrita de vários registradores do quadro 3, em 200, como inexplicada até que o mapa diga o que os registradores a partir de 200 controlam.

> **Caso sintético — Lakeside District Heating Plant.** Os quadros do laboratório foram compostos à mão; nenhum dispositivo ou rede foi contatado.

### Erros e limites

Alguns dispositivos usam endereçamento a partir de zero, e alguns documentos usam a numeração no estilo 40001; misturá-los causa erros de deslocamento de um. Decodificar o tráfego de uma planta que você não está autorizado a monitorar não é uma prática aceitável.

### Exercícios

- **EX019 — Decodificando um quarto quadro.** Decodifique `000400000006010400320004`. *Rubrica:* 3 = tid 4, fc 4 leitura de input registers, endereço 50, quantidade 4, leitura; 2 = código de função certo; 1 = ordem de bytes errada; 0 = nada.
- **EX020 — O que o quadro não consegue dizer.** Dê dois fatos sobre o quadro 2 que não podem ser obtidos a partir dos seus bytes. *Rubrica:* 3 = identidade/autorização de quem enviou e significado de engenharia do registrador 100; 2 = um; 1 = lista campos do cabeçalho; 0 = nada.
- **EX021 — Escalonando uma escrita de setpoint.** Usando a escala em décimos de grau da LDHP, que valor de registrador define 92,5 °C? *Rubrica:* 3 = 925; 2 = 92 ou 93 com a escala mencionada; 1 = 92,5; 0 = nada.

### Síntese

Um decodificador de protocolo dá a estrutura; a documentação da planta dá o significado; e a segmentação, não o protocolo, dá a identidade.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue estudando — capítulo 07 de 40

[← Capítulo 06](#ch-06) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Programação II

### Objetivos de aprendizagem

Você vai (1) estruturar uma ferramenta de análise como funções puras com testes; (2) usar o `unittest` da biblioteca padrão; (3) fazer as funções falharem fechadas; e (4) versionar um script para que um resultado possa ser reproduzido meses depois.

### 8.1 Funções puras são revisáveis

Uma função que recebe entradas e devolve uma decisão, sem ler a rede nem o relógio, pode ser testada exaustivamente. Para ferramentas de TO isso importa, porque o revisor muitas vezes é um engenheiro de controle que só aceitará uma ferramenta se o seu comportamento nos casos-limite for demonstrado. Mantenha a entrada e a saída (arquivos, impressão) nas bordas e a lógica de decisão no meio. O classificador de Maya foi escrito assim: `classify(code)` recebe um código de função e devolve uma palavra, de modo que um engenheiro de controle consegue ler a lista de testes e ver todas as decisões sem rodar uma captura.

### 8.2 Falhar fechado

Quando uma função de lista de permissão recebe uma origem desconhecida, um código de função desconhecido ou um endereço malformado, ela deve devolver "bloquear" em vez de levantar uma exceção que um chamador poderia capturar e ignorar. Falhar fechado numa ferramenta de monitoramento significa "sinalizar para revisão"; num dispositivo de imposição, significa "negar". Nenhum dos dois significa "supor que está tudo bem". O primeiro classificador de Maya falhava aberto: tudo o que estava fora do conjunto de escritas devolvia "read". Um revisor perguntou sobre o código 8, diagnósticos, cujas subfunções podem reiniciar as comunicações, e a resposta expôs o defeito. A correção dela devolve "unknown", o que, num monitor offline, significa sinalizar para revisão.

### 8.3 Testes como documentação

Uma pequena lista de casos de `unittest` se lê como uma especificação:

```python
import unittest
def classify(fc):
    return "write" if fc in (5, 6, 15, 16) else ("read" if fc in (1, 2, 3, 4) else "unknown")
class T(unittest.TestCase):
    def test_codes(self):
        self.assertEqual(classify(3), "read"); self.assertEqual(classify(16), "write")
        self.assertEqual(classify(8), "unknown"); self.assertEqual(classify(43), "unknown")
unittest.main(argv=["x"], exit=False)
```

Executá-lo imprime `Ran 1 test` e `OK`. O código 43 (encapsulated interface transport, usado para identificação de dispositivos) é deliberadamente "unknown" em vez de "read", porque o autor da ferramenta não raciocinou sobre ele.

A lista de testes é também a especificação que um revisor assina: `classify(3)` é leitura, `classify(16)` é escrita, `classify(8)` e `classify(43)` são desconhecidos. O defeito original de Maya teria sido pego pela única asserção de que o código 8 devolve "unknown"; essa asserção agora está na lista. Quando um novo código de função aparece numa captura da LDHP, a primeira mudança é uma nova asserção com a resposta esperada, escrita antes de o classificador ser editado.

### Exemplo resolvido (LDHP sintética)

O primeiro classificador de Maya devolvia "read" para tudo o que não estava no conjunto de escritas. Um revisor perguntou o que o código 8 (diagnósticos) devolveria. A resposta — "read" — estava errada: algumas subfunções de diagnóstico reiniciam as comunicações. Ela mudou o padrão para "unknown" e acrescentou o teste acima.

> **Caso sintético — Lakeside District Heating Plant.** O classificador é uma ferramenta didática para capturas offline, não um dispositivo de imposição.

### 8.4 Registrar decisões para revisão

Cada decisão que a ferramenta toma deve ser registrada com a entrada que a produziu, a regra que disparou e a versão do script, por exemplo `fc=8 -> unknown (rule: default) v=3f2a91c`. Um engenheiro de controle que revisa uma semana de capturas pode então filtrar por "unknown" e decidir, caso a caso, se o classificador precisa de uma nova regra. Esse registro também é o que permite mostrar, mais tarde, que um resultado surpreendente veio de uma versão conhecida do código, e não de uma edição feita depois.

### Erros e limites

Os testes provam os casos que você escreveu, não os que você esqueceu. Registre a versão do script (um hash de commit do git) ao lado de todo resultado que você publicar.

### Exercícios

- **EX022 — Classificando diagnósticos.** O que `classify(8)` devolve na versão final, e por que isso é preferível? *Rubrica:* 3 = "unknown"; diagnósticos podem alterar o estado do dispositivo, então não se deve supor leitura; 2 = só o valor; 1 = "read"; 0 = nada.
- **EX023 — Um caso de teste ausente.** Escreva uma asserção adicional que teria pego o defeito original de Maya. *Rubrica:* 3 = assertEqual(classify(8), "unknown") ou outro código semelhante que não seja de leitura; 2 = testa um código de escrita; 1 = testa o código 3; 0 = nada.
- **EX024 — Reproduzindo um resultado antigo.** Cite duas coisas a registrar junto com uma análise publicada para que ela possa ser reproduzida seis meses depois. *Rubrica:* 3 = hash do commit do script e hash/data exatos do arquivo de entrada; 2 = uma; 1 = "salvar a saída"; 0 = nada.

### Síntese

Ferramentas de TO revisáveis são puras, testadas, falham fechadas e são versionadas — propriedades que permitem a um engenheiro cético confiar na sua saída.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue estudando — capítulo 08 de 40

[← Capítulo 07](#ch-07) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Dados e bancos de dados

### Objetivos de aprendizagem

Você vai (1) modelar os dados do historiador como tempo, tag e valor; (2) agregar e filtrar com SQL no SQLite; (3) detectar lacunas de amostragem; e (4) explicar por que o historiador é ao mesmo tempo um ativo e um risco de segurança.

### 9.1 O papel do historiador

Um historiador de processo armazena séries temporais vindas dos controladores para tendências, relatórios e investigações. Como fica entre as redes de controle e de negócio, ele é muitas vezes a ponte que um intruso usa — e também o melhor registro de que um investigador dispõe. O NIST SP 800-82r3 recomenda colocar numa cópia na DMZ os dados de que os usuários de negócio precisam, para que os usuários corporativos nunca consultem diretamente o historiador da zona de controle. Na LDHP, o HIST-1 fica no nível 3 de Purdue. Os usuários de faturamento e de análise devem ler uma réplica na DMZ, para que uma conta de escritório comprometida nunca abra uma sessão com o historiador que também coleta do PLC-H.

### 9.2 Um esquema mínimo

Três colunas — carimbo de tempo, tag e valor — carregam a maior parte do conteúdo de um historiador; os sistemas de produção acrescentam códigos de qualidade e compressão. O SQLite, embutido no Python, é suficiente para aprender as consultas.

```python
"""Lab 09: query a synthetic historian in an in-memory SQLite database."""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("create table h(ts integer, tag text, v real)")
rows = [(t, "TT-101", 90 + (t % 5)) for t in range(0, 60, 5)] + [(t, "PT-201", 9.5) for t in range(0, 60, 10)]
rows.append((35, "TT-101", 128.0))
db.executemany("insert into h values(?,?,?)", rows)
for tag, n, mx, mean in db.execute("select tag,count(*),max(v),round(avg(v),2) from h group by tag order by tag"):
    print(f"{tag}: n={n} max={mx} mean={mean}")
print("excursions >120:", db.execute("select ts,v from h where tag='TT-101' and v>120").fetchall())
print("gap check PT-201 samples:", [r[0] for r in db.execute("select ts from h where tag='PT-201' order by ts")])
```

Execute com `python3 lab_hist.py`. Saída verificada:

```text
PT-201: n=6 max=9.5 mean=9.5
TT-101: n=13 max=128.0 mean=92.92
excursions >120: [(35, 128.0)]
gap check PT-201 samples: [0, 10, 20, 30, 40, 50]
```

A tabela do laboratório guarda amostras de TT-101 e PT-201 com carimbos de tempo inteiros, o suficiente para executar as duas perguntas que um operador mais faz: qual foi o extremo, e está faltando alguma coisa. A resposta de Maya sobre a sobretemperatura veio de uma consulta sobre essa tabela: `select ts, v from h where tag='TT-101' and v > 120`, que devolveu uma linha em t = 35, 128 °C, de 13 amostras examinadas. O painel de médias horárias não tinha mostrado nada de incomum no mesmo turno.

### 9.3 Agregados escondem eventos

A média de 92,92 °C de TT-101 parece normal; o máximo de 128,0 °C em t = 35, não. Sempre junte uma média a um extremo e a uma contagem. A verificação de lacunas confirma que PT-201 foi amostrado a cada 10 unidades de tempo, sem perdas; um carimbo de tempo ausente nessa lista seria o primeiro sinal de uma falha de coleta ou de supressão deliberada. O relatório de Maya declara os três: uma excursão a 128,0 °C em t = 35, 13 amostras examinadas e o ponto de trip suposto de 135 °C do SIS-H não alcançado. O painel de médias horárias tinha respondido "nenhuma sobretemperatura" à mesma pergunta.

### Exemplo resolvido (LDHP sintética)

Perguntam a Maya: "Houve alguma sobretemperatura no último turno?" Um painel de médias horárias diz que não. A consulta dela, `select ts, v from h where tag='TT-101' and v > 120`, devolve uma excursão em t = 35, 128 °C. Ela a relata com a contagem de amostras examinadas (13) e observa que o ponto de trip do SIS-H (suposto em 135 °C nesta planta sintética) não foi alcançado.

> **Caso sintético — Lakeside District Heating Plant.** Os valores, as tags e o ponto de trip de 135 °C foram inventados para o ensino.

### Erros e limites

A compressão do historiador (banda morta ou swinging door) pode descartar pontos que não mudaram "o suficiente", de modo que picos curtos podem estar ausentes. Os carimbos de tempo podem vir do historiador, e não do controlador. Nunca conceda acesso de escrita às tabelas do historiador para trabalho de análise.

### Exercícios

- **EX025 — Contando as amostras examinadas.** Por que o laboratório relata n = 13 para TT-101, e não 12? *Rubrica:* 3 = 12 amostras regulares (0–55, passo 5) mais a excursão inserida; 2 = nota a linha extra; 1 = chuta; 0 = nada.
- **EX026 — Consulta para uma lacuna de amostragem.** Escreva um SQL que devolva os carimbos de tempo de PT-201 em que a amostra seguinte chega mais de 10 unidades depois. *Rubrica:* 3 = função de janela LEAD (ou auto-junção) com diferença de ts > 10; 2 = ideia correta, deslize de sintaxe; 1 = só conta linhas; 0 = nada.
- **EX027 — Compressão por banda morta e picos.** Explique como a compressão por banda morta poderia esconder uma excursão breve. *Rubrica:* 3 = ponto armazenado apenas quando muda além da banda morta ou por exceção/heartbeat, então um pico curto entre pontos armazenados pode sumir; 2 = parcial; 1 = só "a compressão perde dados"; 0 = nada.

### Síntese

Peça ao historiador extremos, contagens e lacunas, e não só médias — e trate a sua localização e as suas permissões como projeto de segurança.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue estudando — capítulo 09 de 40

[← Capítulo 08](#ch-08) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Ética e prática autorizada

### Objetivos de aprendizagem

Você vai (1) distinguir autorização de mera possibilidade de acesso; (2) listar os elementos de uma permissão de trabalho escrita para testes em TO; (3) tratar vulnerabilidades descobertas por meio de divulgação coordenada; e (4) recusar pedidos que poriam pessoas em risco ou que excederiam o escopo.

### 10.1 A autorização vem do proprietário

Só o proprietário do ativo — ou alguém a quem ele tenha delegado por escrito — pode autorizar testes num sistema de TO. Um funcionário curioso da planta, um fornecedor que "já tem acesso mesmo" ou um professor que quer uma demonstração não podem concedê-la. No ambiente industrial, a autorização também precisa vir da operação: um teste legal, mas inseguro, continua inaceitável. O colega de Maya ofereceu exatamente esse tipo de falsa autoridade: o endereço IP de um controlador de aquecimento "real" encontrado num motor de busca e a sugestão de ler um registrador. Ninguém que fosse dono daquele controlador tinha concordado, então Maya recusou e sugeriu relatar a exposição ao CERT nacional.

### 10.2 A permissão de trabalho

Uma boa autorização de teste em TO nomeia os sistemas no escopo, a janela de tempo, as técnicas permitidas (apenas captura passiva, consultas somente de leitura ou testes de bancada), as pessoas na chamada, as condições de parada ("se ocorrer qualquer alarme de processo, pare e avise o líder de turno") e o plano de reversão. Ela é assinada pelo proprietário e pelo gerente de operação da área afetada. Para uma captura passiva no switch de controle da LDHP, a condição de parada poderia dizer: "qualquer alarme da HMI-1 ou qualquer mudança no tempo de varredura do PLC-H; parar a captura e informar o líder de turno". A reversão é remover a configuração da porta espelhada.

### 10.3 Divulgação coordenada

Se você encontrar uma falha num produto de fornecedor, relate-a ao fornecedor e, quando for o caso, à CISA, cujos alertas de ICS publicam correções coordenadas. A provisão 5.2 da ETSI EN 303 645 exige que fabricantes de IoT de consumo publiquem uma política de divulgação de vulnerabilidades; muitos fornecedores industriais mantêm programas semelhantes. Publicar detalhes de exploração antes de existir uma correção pode pôr em risco todas as plantas que usam aquele produto. Se o trabalho offline de Maya tivesse revelado uma falha real no firmware dos gateways de medidores, o caminho seria primeiro o contato de divulgação do fornecedor; o MTR-C, no Capítulo 30, é um aviso de que alguns fornecedores não têm nenhum, e nesse caso o CERT nacional ou a CISA coordenam no lugar dele.

### Exemplo resolvido (LDHP sintética)

Um colega oferece a Maya o endereço IP de um controlador de aquecimento "real" encontrado num motor de busca da internet e sugere "só ler um registrador para provar que funciona". Maya recusa: não há autorização do proprietário, não há permissão de trabalho e a consequência para o processo é desconhecida. Em vez disso, ela anota a categoria de exposição (ATT&CK for ICS T0883) e sugere que o colega relate a exposição ao CERT nacional, que pode contatar o proprietário.

> **Caso sintético — Lakeside District Heating Plant.** O colega e o controlador exposto são fictícios; o que importa é o raciocínio.

### Erros e limites

"Somente leitura" não é automaticamente inofensivo — alguns dispositivos legados travam com requisições inesperadas. Códigos de ética não substituem a lei; os estudantes precisam conhecer a lei sobre uso indevido de computadores da sua jurisdição.

### Exercícios

- **EX028 — Condição de parada da permissão.** Escreva uma condição de parada para uma captura de rede passiva no switch de controle da LDHP. *Rubrica:* 3 = gatilho observável mais ação e quem é avisado; 2 = só o gatilho; 1 = vago, "se houver problemas"; 0 = nada.
- **EX029 — Quem pode autorizar?** O gerente de projeto de uma terceirizada manda um e-mail: "podem varrer o PLC-H". Isso basta? *Rubrica:* 3 = não; precisa da aprovação do proprietário e da operação, com escopo e janela; 2 = não, sem justificativa; 1 = sim, com ressalvas; 0 = sim.
- **EX030 — Divulgando uma falha de fornecedor.** Liste os dois primeiros passos depois de encontrar um defeito que trava um modelo de controlador numa unidade de bancada. *Rubrica:* 3 = preservar a evidência em sigilo e contatar o fornecedor/PSIRT (e a CISA ou o CERT nacional); 2 = um; 1 = publicar nas redes sociais; 0 = nada.

### Síntese

Em TO, a prática ética é operacional: autorização escrita do proprietário, condições de parada explícitas e divulgação coordenada protegem pessoas, e não apenas reputações.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue estudando — capítulo 10 de 40

[← Capítulo 09](#ch-09) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operacionais

### Objetivos de aprendizagem

Você vai (1) identificar onde sistemas operacionais de uso geral aparecem numa arquitetura de TO; (2) explicar por que as matrizes de suporte dos fornecedores restringem o endurecimento; (3) aplicar listas de permissão de aplicações e controle de mídias removíveis; e (4) coletar evidências de hosts com privilégio mínimo.

### 11.1 Windows e Linux dentro da planta

Os CLPs rodam firmware de tempo real, mas HMIs, estações de engenharia, historiadores e servidores OPC rodam Windows ou Linux. É nesses hosts que caem cargas de phishing, pendrives infectados e ferramentas de acesso remoto. O NIST SP 800-82r3 os trata como ativos de TO com restrições de TO: podem não receber patches mensais, podem rodar software certificado apenas para uma versão antiga do sistema operacional e podem ser necessários 24 horas por dia. Na LDHP, esses hosts são a HMI-1, a EWS-1 e o HIST-1. A EWS-1 é a que mais importa, porque consegue baixar lógica para o PLC-H, e é por isso que a ferramenta que explora drivers descrita no AA22-103A é relevante mesmo para uma planta sem produtos nomeados.

### 11.2 Matrizes de suporte

O fornecedor da HMI certifica uma versão específica do sistema operacional, um service pack e um produto antivírus. Aplicar uma configuração de endurecimento não suportada — desabilitar um serviço que o runtime da HMI usa, por exemplo — pode deixar os operadores com uma tela em branco durante uma onda de frio. O endurecimento segue, portanto, a sequência teste em bancada, comitê de mudanças, implantação na janela, e as exceções são documentadas com controles compensatórios. Para a HMI-1, Maya propôs a lista de permissão em modo de auditoria por duas semanas antes da imposição, e o fornecedor confirmou; remover a conta de administrador local compartilhada exigia uma conta de serviço do runtime, que ela documentou como exceção em vez de forçar a mudança. Essa sequência é a matriz de suporte na prática.

### 11.3 Listas de permissão e controle de mídias

A lista de permissão de aplicações autoriza apenas executáveis conhecidos, o que combina com as HMIs, porque o seu conjunto de software raramente muda. O controle de mídias removíveis — quiosques de varredura, armazenamento USB bloqueado, mídias de transferência assinadas — trata da forma mais comum de o malware atravessar um air gap. Ambos são controles de host listados entre os requisitos de sistema da IEC 62443-3-3 para proteção contra código malicioso (SR 3.2). A proposta de Maya para a HMI-1 aplicou os dois: lista de permissão em modo de auditoria por duas semanas, depois imposição, e armazenamento USB em massa bloqueado, exceto pelo quiosque de varredura. O período de auditoria importa porque lista todos os executáveis que o runtime da HMI realmente inicia, inclusive os que a documentação do fornecedor esqueceu, antes de bloquear qualquer coisa.

### 11.4 Evidências com privilégio mínimo

Numa investigação, prefira exportar o log de eventos, a lista de software instalado e a lista de processos em execução com uma conta somente de leitura a gerar a imagem do disco de uma HMI em operação. A imagem pode exigir parada e copia receitas proprietárias. Na LDHP, um login suspeito na HMI-1 numa noite de inverno seria investigado primeiro a partir de exportações: o log de eventos do Windows para o login, a lista de processos mostrando se o runtime da HMI ou outra coisa estava rodando, e a lista de software instalado comparada com a versão certificada pelo fornecedor. Uma imagem completa da HMI-1 significaria tirar a tela dos operadores, o que exige o acordo do líder de turno e um plano para operar a caldeira pelos controles locais.

### Exemplo resolvido (LDHP sintética)

A HMI-1 da LDHP roda uma versão do Windows certificada pelo seu fornecedor. Maya propõe três mudanças: habilitar a lista de permissão em modo de auditoria por duas semanas e depois impô-la; bloquear o armazenamento USB em massa, exceto pelo quiosque de varredura; remover a conta de administrador local usada por todos os turnos e emitir contas nominais. O fornecedor confirma as duas primeiras; a terceira exige uma conta de serviço do runtime, que ela documenta como exceção.

> **Caso sintético — Lakeside District Heating Plant.** A resposta do fornecedor é inventada; fornecedores reais publicam os seus próprios guias de endurecimento.

### Erros e limites

Um modo de auditoria que nunca passa para imposição é teatro. Varreduras de antivírus durante o pico de carga podem deixar uma HMI lenta; agende-as.

### Exercícios

- **EX031 — Por que o modo de auditoria primeiro?** Explique o propósito de rodar a lista de permissão em modo de auditoria antes de impô-la na HMI-1. *Rubrica:* 3 = descobrir os executáveis legítimos sem bloquear a operação e depois impor uma lista revisada; 2 = parcial; 1 = "para testar"; 0 = nada.
- **EX032 — Escolhendo um método de evidência.** Diante de uma suspeita de infecção na HMI-1, escolha entre exportação ao vivo e imagem de disco e justifique. *Rubrica:* 3 = primeiro a exportação ao vivo somente de leitura; imagem apenas se justificada, permitida e agendada; 2 = só a escolha; 1 = imagem imediatamente; 0 = nada.
- **EX033 — Documentando uma exceção de endurecimento.** Escreva o registro de exceção para a conta de serviço do runtime. *Rubrica:* 3 = motivo, controle compensatório, responsável, data de revisão; 2 = três; 1 = só o motivo; 0 = nada.

### Síntese

Os hosts de uso geral são a camada mais frágil de uma planta; endureça-os dentro do suporte do fornecedor, controle o que roda e o que é conectado, e investigue-os com delicadeza.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue estudando — capítulo 11 de 40

[← Capítulo 10](#ch-10) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Probabilidade e estatística

### Objetivos de aprendizagem

Você vai (1) estimar uma taxa de alarmes falsos com um limite de confiança; (2) usar a regra de três para zero eventos observados; (3) comparar intervalos de Wilson com estimativas pontuais ingênuas; e (4) evitar a falácia da taxa-base ao avaliar alertas.

### 12.1 Zero não é zero

Um detector que não gerou nenhum alarme falso em 40 dias tranquilos tem estimativa pontual 0, mas a afirmação honesta é um limite. A regra de três dá um limite superior aproximado de 95 % de 3/n quando zero eventos são vistos em n tentativas independentes; com n = 40, isso dá 7,5 %. Essa é a afirmação que o engenheiro de controle faz no exemplo resolvido deste capítulo: um novo detector de temperatura de ida que "nunca dá alarme falso". A primeira pergunta de Maya foi o denominador, 40 dias, e a resposta dela foi o limite: 0 em 40 é compatível com uma taxa diária real de alarmes falsos de até vários por cento.

### 12.2 Intervalos de Wilson

O intervalo de escore de Wilson se comporta bem com contagens pequenas e com proporções próximas de 0 ou de 1, ao contrário da aproximação normal dos livros-texto, que pode produzir limites inferiores negativos.

```python
"""Lab 12: false-alarm estimates and rule-of-three bounds (synthetic counts)."""
import math
def wilson_upper(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    return (p + z*z/(2*n) + z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))) / d
for k, n in [(0, 40), (0, 300), (3, 300)]:
    r3 = 3 / n if k == 0 else float("nan")
    print(f"k={k:2} n={n:3} point={k/n:.4f} wilson95_upper={wilson_upper(k,n):.4f} rule_of_three={r3:.4f}")
```

Execute com `python3 lab_rule3.py`. Saída verificada:

```text
k= 0 n= 40 point=0.0000 wilson95_upper=0.0876 rule_of_three=0.0750
k= 0 n=300 point=0.0000 wilson95_upper=0.0126 rule_of_three=0.0100
k= 3 n=300 point=0.0100 wilson95_upper=0.0290 rule_of_three=nan
```

Para o detector da LDHP, o intervalo dos livros-texto para 0 alarmes falsos em 40 dias colapsa para de 0 % a 0 %, o que declara uma certeza que os dados não sustentam. O de Wilson dá de 0 % a 8,8 % para a mesma contagem, e esse limite superior é o que Maya escreveu na sua nota: "0 alarmes falsos em 40 dias; limite superior de 95 % ≈ 8,8 % por dia". O mesmo método volta a aparecer no Capítulo 25, para as 0 de 40 execuções com alarme falso do CUSUM.

### 12.3 Lendo os números

Para 0/40, o limite superior de Wilson (8,76 %) fica um pouco acima da regra de três (7,5 %); para 0/300, os dois encolhem para cerca de 1 %. Três alarmes falsos em 300 dão uma estimativa pontual de 1 %, mas um limite superior próximo de 2,9 %. Coletar mais dias tranquilos é a única forma de estreitar o intervalo. Maya usou a segunda linha para responder ao engenheiro de controle: seriam necessários cerca de 300 dias tranquilos para afirmar uma taxa de alarmes falsos abaixo de aproximadamente 1 %. A um dia por dia de operação, isso é a maior parte de um ano, e é por isso que estudos de simulação como o do Capítulo 25 usam muitas execuções com sementes fixas.

### 12.4 Taxas-base

Suponha que ataques reais ocorram em 1 dia a cada 1.000 e que um detector pegue 90 % deles, gerando um alarme falso em 2 % dos dias tranquilos. Em 1.000 dias, ele sinaliza cerca de 0,9 dia verdadeiro e 19,98 falsos — então cerca de 4 % dos alertas são reais. Operadores que aprendem que a maioria dos alertas é ruído começam a ignorá-los, e é por isso que a prática de gestão de alarmes trata as taxas de alarmes incômodos como uma questão de segurança física. Para a sala de controle da LDHP, onde um turno da noite vê três ou quatro alarmes de processo genuínos, um detector que produzisse cerca de 20 alarmes falsos para cada real seria desligado em uma semana.

### Exemplo resolvido (LDHP sintética)

O engenheiro de controle diz que um novo detector de temperatura de ida "nunca dá alarme falso". Maya pede o denominador: 40 dias. Ela escreve: "0 alarmes falsos em 40 dias; limite superior de 95 % ≈ 8,8 % por dia (Wilson); seriam necessários cerca de 300 dias tranquilos para afirmar menos de aproximadamente 1 %."

> **Caso sintético — Lakeside District Heating Plant.** As contagens são inventadas; os métodos são padrão.

### 12.5 Enquadramento por turno para os operadores

Os operadores pensam em turnos, não em proporções. Uma taxa de alarmes falsos de 2 % por dia num detector parece pequena, mas quarenta detectores assim produzem quase um alarme incômodo por dia. Converta as taxas em "alarmes esperados por turno" antes de pedir a uma sala de controle que aceite um novo detector. Na LDHP, com dois turnos de doze horas por dia, um único detector a 2 % por dia produz um alarme incômodo mais ou menos uma vez a cada 100 turnos, o que os operadores toleram. Quarenta detectores a essa taxa produzem cerca de 0,8 por dia, ou aproximadamente um a cada dois ou três turnos. O detector de faixa do Capítulo 25, que deu alarme falso em 9 de 40 execuções tranquilas, seria muito pior nessa escala.

### Erros e limites

Os limites supõem tentativas independentes; dias consecutivos no mesmo regime de clima são correlacionados, então a incerteza real é maior.

### Exercícios

- **EX034 — Limite superior para zero em 150.** Aplique a regra de três a 0 alarmes falsos em 150 dias. *Rubrica:* 3 = 2 % com "limite superior aproximado de 95 %"; 2 = só o número; 1 = diz 0 %; 0 = nada.
- **EX035 — Precisão dos alertas com taxa-base baixa.** Com uma taxa de 1 dia de ataque em 500, 95 % de detecção e 1 % de alarmes falsos, que fração dos alertas é real? *Rubrica:* 3 ≈ 16 % com o cálculo; 2 = método certo, deslize aritmético; 1 = responde 95 %; 0 = nada.
- **EX036 — Tentativas correlacionadas.** Por que 40 dias consecutivos de inverno superestimam a informação contida em "0/40"? *Rubrica:* 3 = os dias compartilham condições e, portanto, não são independentes; n efetivo menor; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Publique sempre as afirmações de detecção com uma contagem, um denominador e um limite; e julgue os alertas por quantas vezes acertam, e não só por quantos ataques pegam.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue estudando — capítulo 12 de 40

[← Capítulo 11](#ch-11) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Identidade e acesso

### Objetivos de aprendizagem

Você vai (1) projetar contas nominais e baseadas em papéis para operadores, engenheiros e fornecedores; (2) explicar o requisito fundamental da IEC 62443 para controle de identificação e autenticação; (3) separar os privilégios de "visualizar", "operar" e "engenharia"; e (4) projetar acesso de fornecedores limitado no tempo.

### 13.1 Contas compartilhadas quebram a atribuição

Historicamente, as salas de controle usavam um único login por turno. Quando um setpoint muda, o log mostra "operador" — e não qual operador. A IEC 62443-3-3 agrupa os requisitos em sete requisitos fundamentais; o FR 1, controle de identificação e autenticação, pede que os usuários humanos sejam identificados de forma única. Contas nominais permitem que uma investigação separe um erro honesto de um uso indevido. Na LDHP, antes do novo desenho de Maya, a HMI-1 usava um único login compartilhado por turno, de modo que uma mudança de setpoint às 02:00 não podia ser rastreada até uma pessoa; o log dizia apenas "operator". O novo desenho deu a cada operador uma conta nominal, para que a investigação do Capítulo 15 possa perguntar a uma pessoa identificada o que ela mudou.

### 13.2 Papéis que correspondem ao trabalho

Na LDHP, três papéis bastam para a HMI-1: *visualizar* (tendências e alarmes), *operar* (reconhecer alarmes, alterar setpoints dentro dos limites) e *engenharia* (alterar limites, baixar lógica a partir da estação de engenharia). O FR 2, controle de uso, trata da imposição desses privilégios. Privilégio mínimo significa que um terceirizado que revisa tendências recebe apenas *visualizar*. O desenho de Maya segue esses papéis. Um operador de turno pode mover o setpoint de ida dentro dos limites de 70–110 °C do PLC-H; só um engenheiro pode alterar esses limites ou baixar lógica a partir da EWS-1. A conta de diagnóstico do fornecedor é somente de visualização, a menos que um chamado a eleve para uma sessão. É no FR 2 que essa regra é imposta.

### 13.3 Acesso de emergência

Uma planta não pode trancar os operadores do lado de fora durante uma emergência porque um servidor de diretório caiu. Projete contas de quebra de vidro (break-glass): credenciais lacradas, autenticação local, alerta imediato quando usadas e revisão após o evento. É a disponibilidade e a segurança física moldando o desenho de identidade. O desenho de Maya põe o envelope de quebra de vidro da LDHP no cofre do líder de turno. O seu uso dispara um alerta para o engenheiro de plantão, e a senha é trocada e o envelope relacrado após cada uso. A revisão pergunta por que o login baseado em diretório falhou, e não quem abriu o cofre.

### 13.4 Acesso remoto de fornecedores

Os fornecedores precisam de acesso remoto para diagnóstico. O alerta da CISA AA21-042A, sobre o comprometimento, em 2021, do sistema de controle de uma estação de tratamento de água nos EUA por meio de software de acesso remoto, recomendou autenticação multifator, senhas fortes para as credenciais de área de trabalho remota, auditoria das conexões remotas e fechamento das portas RDP não usadas. Um desenho mais seguro: um jump host na DMZ, autenticação multifator, sessões habilitadas pelo líder de turno por uma janela fixa, e gravação. O ponto de partida da LDHP lembrava o caso de 2021: uma ferramenta de área de trabalho remota sempre ligada para o fornecedor. O desenho de Maya a substituiu por sessões pelo jump host da DMZ, habilitadas por quatro horas por chamado, gravadas e revisadas semanalmente.

### Exemplo resolvido (LDHP sintética)

Maya mapeia a prática atual: um login compartilhado na HMI, acesso do fornecedor por uma ferramenta de área de trabalho remota sempre ligada. O desenho dela: contas nominais em três papéis; envelope de quebra de vidro no cofre do líder de turno; sessões do fornecedor pelo jump host da DMZ, habilitadas por quatro horas por chamado, gravadas e revisadas semanalmente.

> **Caso sintético — Lakeside District Heating Plant.** As contas e o fornecedor da LDHP são inventados; o alerta citado descreve um incidente real.

### Erros e limites

MFA num console da sala de controle pode atrasar a resposta a emergências; use-a para acesso remoto e de engenharia, e confie na segurança física da sala de controle para a operação local onde isso se justificar.

### Exercícios

- **EX037 — Atribuindo um papel.** Um terceirizado de manutenção da caldeira precisa verificar tendências de combustão durante uma semana. Que papel e que limite de tempo? *Rubrica:* 3 = só visualizar, expirando após a semana, conta nominal; 2 = papel certo; 1 = operar; 0 = engenharia.
- **EX038 — Revisão da quebra de vidro.** Liste três coisas a verificar depois que a conta de quebra de vidro foi usada. *Rubrica:* 3 = quem a usou e por quê, ações realizadas, credencial trocada; 2 = duas; 1 = uma; 0 = nada.
- **EX039 — Lições do AA21-042A.** Cite duas medidas de acesso remoto recomendadas no alerta sobre a estação de água que se aplicam à LDHP. *Rubrica:* 3 = duas medidas corretas; 2 = uma; 1 = genérico, "usar antivírus"; 0 = nada.

### Síntese

Em TO, a identidade precisa tornar cada ação atribuível, fazer cada privilégio corresponder a uma função e tornar cada emergência sobrevivível.

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue estudando — capítulo 13 de 40

[← Capítulo 12](#ch-12) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos de privacidade

### Objetivos de aprendizagem

Você vai (1) reconhecer dados pessoais em fluxos de medidores inteligentes e de automação predial; (2) aplicar minimização de dados e limitação de finalidade; (3) escolher intervalos de agregação que atendam à operação sem revelar o comportamento das residências; e (4) relacionar privacidade com a provisão 5.8 da ETSI EN 303 645.

### 14.1 Medidores de calor revelam vidas

Os medidores IoT da LDHP informam o consumo de calor de cada residência. Leituras horárias mostram quando os moradores acordam, cozinham, viajam ou estão fora — o mesmo problema de inferência que tornou controversos os medidores inteligentes de eletricidade. Em muitas jurisdições, essas leituras são dados pessoais, porque se referem a uma residência identificável. Um perfil horário de um único medidor da LDHP pode mostrar uma residência que deixa de aquecer por dez dias em fevereiro, o que diz a qualquer pessoa que o leia que a casa está vazia. O faturamento não precisa de nada disso. É por isso que o pedido da equipe de análise de dados por leituras domiciliares a cada cinco minutos, no caso de Maya, encontrou resistência: nessa resolução, os dados mostram rotinas diárias, e não apenas consumo.

### 14.2 Minimização e finalidade

O faturamento precisa de um total mensal. O balanceamento da rede precisa da vazão por bairro, não de detalhes casa a casa. A detecção de falhas pode precisar de leituras individuais, mas talvez diárias e guardadas por semanas, não por anos. Escrever a finalidade ao lado de cada fluxo de dados força a pergunta "precisamos desta granularidade?". A resposta de Maya ao pedido da equipe de análise por dados domiciliares a cada cinco minutos pôs uma finalidade ao lado de cada fluxo: totais mensais para o faturamento, leituras diárias por residência guardadas por 60 dias para detecção de vazamentos e agregados horários por rua para o balanceamento. Os dados de cinco minutos simplesmente não foram coletados, porque nenhuma finalidade havia sido definida.

### 14.3 Agregação como controle

Agregar 40 residências de um trecho de rua antes que os dados saiam do gateway remove os padrões individuais e mantém o sinal operacional. A agregação não é perfeita: se uma moradia domina o trecho, o seu padrão continua visível, por isso os engenheiros verificam o tamanho mínimo do grupo. O desenho de Maya fixa o mínimo em 20 moradias por agregado para os dados de balanceamento. Um trecho de rua com menos moradias, ou com um grande edifício que usa a maior parte do calor, é fundido com o vizinho antes que o agregado horário saia do gateway, para que nenhum agregado seja, na prática, a leitura de uma única residência.

### 14.4 A linha de base de IoT de consumo

A provisão 5.8 da ETSI EN 303 645 pede que os dados pessoais em trânsito entre um dispositivo e os serviços associados sejam protegidos (por exemplo, criptografados), e a provisão 6 trata da proteção de dados de forma mais geral — informar os consumidores sobre quais dados são tratados e por quê. Um medidor de aquecimento distrital nem sempre é "IoT de consumo", mas as provisões são uma lista de verificação útil. Para os medidores da LDHP, a 5.8 aponta para o enlace de rádio e para o uplink do gateway, que carregam leituras domiciliares; a provisão 6 aponta para informar os moradores sobre o que é coletado e por quê, o que a lista de finalidades de Maya já faz.

### Exemplo resolvido (LDHP sintética)

A equipe de análise pede leituras domiciliares a cada cinco minutos "para aprendizado de máquina no futuro". A resposta de Maya: totais mensais para o faturamento; leituras diárias por residência guardadas por 60 dias para detecção de vazamentos; agregados horários por rua (mínimo de 20 moradias) para o balanceamento; dados domiciliares de cinco minutos não coletados sem uma finalidade definida e uma avaliação de impacto à privacidade.

> **Caso sintético — Lakeside District Heating Plant.** O pedido da equipe de análise e os prazos de retenção são exemplos inventados.

### Erros e limites

Pseudonimizar os IDs dos medidores não os anonimiza se os endereços forem guardados em outro lugar. As leis de privacidade variam; este capítulo é orientação, não aconselhamento jurídico.

### Exercícios

- **EX040 — Inferindo ocupação.** Dê duas coisas que um observador poderia inferir das leituras horárias de calor de um apartamento. *Rubrica:* 3 = duas inferências plausíveis (ausência, rotina diária, número de moradores); 2 = uma; 1 = vago; 0 = nada.
- **EX041 — Granularidade por finalidade.** Para detecção de vazamentos, proponha um intervalo de leitura e um prazo de retenção e justifique ambos. *Rubrica:* 3 = diário (ou horário) com retenção na escala de semanas e justificativa; 2 = só os valores; 1 = guardar tudo; 0 = nada.
- **EX042 — Quando a agregação falha.** Por que um trecho que contém uma grande escola e cinco apartamentos poderia falhar como agregado de privacidade? *Rubrica:* 3 = a escola domina; os padrões dos apartamentos se perdem, mas o da escola é revelado / grupo pequeno demais; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Dados operacionais de IoT muitas vezes são dados pessoais; colete-os para uma finalidade, na granularidade mais grossa que ainda seja útil, e proteja-os em trânsito e em repouso.

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue estudando — capítulo 14 de 40

[← Capítulo 13](#ch-13) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Evidências e medição

### Objetivos de aprendizagem

Você vai (1) corrigir o deslocamento de relógio ao combinar logs; (2) preservar a cadeia de custódia de evidências exportadas; (3) distinguir observação, inferência e suposição numa linha do tempo; e (4) declarar a incerteza de medição.

### 15.1 Os relógios discordam

Controladores, HMIs e historiadores muitas vezes mantêm relógios independentes, e um CLP sem sincronização de tempo pela rede pode derivar minutos por mês. Antes de sequenciar eventos, meça o deslocamento — por exemplo, comparando um evento conhecido (a mudança de setpoint feita por um operador) nos dois logs — e registre como ele foi medido.

```python
"""Lab 15: align two synthetic logs with a measured clock offset."""
from datetime import datetime, timedelta
hmi = [("2026-03-02T10:00:07", "operator changed SP TT-101 to 95"), ("2026-03-02T10:02:40", "alarm TT-101 HI")]
plc = [("2026-03-02T09:58:52", "SP write accepted"), ("2026-03-02T10:01:30", "valve CV-11 to 80%")]
offset = timedelta(seconds=75)  # measured: PLC clock is 75 s behind the reference
ev = [(datetime.fromisoformat(t), "HMI", m) for t, m in hmi] + [(datetime.fromisoformat(t) + offset, "PLC", m) for t, m in plc]
for t, src, m in sorted(ev):
    print(t.time(), src, m)
```

Execute com `python3 lab_clock.py`. Saída verificada:

```text
10:00:07 HMI operator changed SP TT-101 to 95
10:00:07 PLC SP write accepted
10:02:40 HMI alarm TT-101 HI
10:02:45 PLC valve CV-11 to 80%
```

Na LDHP, o evento conhecido foi a mudança de setpoint de um operador na HMI-1 às 10:00:07, que também aparece no log do PLC-H como "SP write accepted". Casar os dois deu um deslocamento de 75 segundos, com uma incerteza de cerca de dois segundos por causa da resolução dos logs.

### 15.2 O que a linha do tempo corrigida mostra

Depois de somar o deslocamento medido de 75 segundos, o "SP write accepted" do CLP se alinha com a entrada da HMI às 10:00:07, o que sustenta a hipótese de que a escrita veio da HMI-1. Sem a correção, o evento do CLP aparece 75 segundos antes de o operador agir — uma sequência que poderia ser mal interpretada como uma escrita externa seguida de uma reação do operador. A correção muda a história, e não só os números. Um gestor que lesse os logs sem correção poderia concluir que alguém de fora da sala de controle escreveu o setpoint e que o operador reagiu depois, o que dispararia um incidente de segurança. A linha do tempo corrigida mostra uma mudança comum feita pelo operador, desde que a suposição sobre o deslocamento se mantenha.

### 15.3 Cadeia de custódia

Para cada arquivo exportado, registre quem o exportou, de qual sistema, quando, por qual método, e o seu hash SHA-256. Guarde o original como somente leitura e trabalhe em cópias. É assim que uma linha do tempo vira uma evidência na qual um gestor, uma seguradora ou um tribunal podem confiar. Para a linha do tempo de Maya, o registro diria: log de eventos da HMI-1, exportado pelo engenheiro de turno às 11:20 com a conta somente de leitura, SHA-256 registrado; log de diagnóstico do PLC-H, exportado da EWS-1 pelo engenheiro de controle, SHA-256 registrado; os dois originais guardados como somente leitura no compartilhamento da investigação, e a linha do tempo corrigida de Maya construída apenas a partir de cópias. Se uma seguradora perguntar depois se o log do CLP foi editado, o hash responde.

### 15.4 Observação, inferência, suposição

Rotule cada entrada da linha do tempo. "Linha do log do CLP às 09:58:52, hora local do CLP" é uma observação. "A escrita partiu da HMI-1" é uma inferência. "O deslocamento do relógio do CLP foi constante durante toda a manhã" é uma suposição. Misturá-las é a falha mais comum em relatórios de incidentes. A tabela de Maya acrescenta uma coluna de rótulo exatamente para isso. A sua linha do deslocamento está marcada como A, porque "75 s ± 2 s, medido casando a mudança de setpoint das 10:00:07" depende de o deslocamento continuar constante das 09:30 às 10:30. Se alguém descobrir depois um ajuste do relógio do CLP às 10:15, só as linhas que dependem dessa suposição precisam ser revistas.

### Exemplo resolvido (LDHP sintética)

A tabela de Maya tem três colunas — hora corrigida, fonte, declaração — mais uma quarta para o rótulo (O/I/A). A linha do deslocamento diz: "Deslocamento de 75 s ± 2 s, medido casando a mudança de setpoint da HMI às 10:00:07 com a mensagem de aceitação do CLP (A: deslocamento constante durante 09:30–10:30)."

> **Caso sintético — Lakeside District Heating Plant.** As linhas de log e o deslocamento são inventados.

### Erros e limites

Um evento casado dá uma única medição do deslocamento; a deriva durante o período pode torná-la errada mais adiante. Fusos horários e mudanças de horário de verão são uma fonte de erro separada.

### Exercícios

- **EX043 — Aplicando o deslocamento.** Uma linha do log do CLP diz 10:04:10. Qual é a hora corrigida? *Rubrica:* 3 = 10:05:25; 2 = direção correta, deslize aritmético; 1 = subtrai; 0 = nada.
- **EX044 — Rotulando entradas da linha do tempo.** Rotule como O, I ou A: (a) "CV-11 foi para 80 % às 10:02:45", (b) "o movimento da válvula foi uma ação automática de controle", (c) "nenhum outro host escreveu no PLC-H". *Rubrica:* 3 = O, I, A; 2 = duas certas; 1 = uma; 0 = nada.
- **EX045 — Campos de custódia.** Liste cinco campos de um registro de custódia para o log do CLP exportado. *Rubrica:* 3 = cinco campos relevantes, incluindo o hash; 2 = quatro; 1 = sem hash; 0 = nada.

### Síntese

Em TO, uma evidência só é tão boa quanto os seus relógios, o seu registro de custódia e a sua honestidade sobre o que foi visto e o que foi concluído.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue estudando — capítulo 15 de 40

[← Capítulo 14](#ch-14) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Arquitetura de segurança

### Objetivos de aprendizagem

Você vai (1) posicionar os ativos da LDHP nos níveis de referência de Purdue; (2) projetar uma DMZ entre as zonas corporativa e de controle; (3) atribuir níveis de segurança-alvo às zonas usando os conceitos da IEC 62443-3-2; e (4) explicar a defesa em profundidade sem afirmar que alguma camada isolada é suficiente.

### 16.1 Os níveis de Purdue como mapa inicial

O modelo de Purdue numera os níveis a partir do processo físico (0), passando por sensores e atuadores (1), controle supervisório (2) e operações do local (3), até o nível corporativo (4–5). Ele é antigo e imperfeito — serviços em nuvem e gateways de IIoT borram os níveis —, mas oferece um vocabulário comum. Na LDHP, os transmissores e a caldeira ficam nos níveis 0–1, o PLC-H e o SIS-H no nível 1, o SCADA e a HMI no nível 2, o HIST-1 no nível 3, e o faturamento e o e-mail no nível 4. O valor do mapa está nos lugares em que os dispositivos da LDHP não se encaixam: os gateways de medidores e a nuvem de faturamento ficam fora dos níveis, e o SIS-H divide o nível 1 com o PLC-H, embora precise continuar independente dele.

### 16.2 A DMZ industrial

Entre os níveis 3 e 4 fica uma zona desmilitarizada que abriga os sistemas de que os dois lados precisam: uma réplica do historiador, um servidor de patches, um jump host para acesso remoto. A regra é que nenhuma sessão atravessa a DMZ de ponta a ponta; os usuários corporativos se conectam a serviços da DMZ, e os sistemas da zona de controle enviam dados para os serviços da DMZ ou são consultados por eles. O NIST SP 800-82r3 descreve esse padrão na sua discussão sobre arquitetura de defesa em profundidade. Na LDHP, a DMZ abrigaria a réplica do historiador que o faturamento e a equipe de análise leem, o servidor de patches da HMI-1 e o jump host que as sessões dos fornecedores alcançam antes de qualquer sistema da zona de controle.

### 16.3 Níveis de segurança

A IEC 62443 define os níveis de segurança SL 1–4 pelo atacante a que uma zona precisa resistir, desde a violação casual ou coincidente (SL 1) até meios sofisticados com recursos amplos (SL 4). A avaliação de risco fixa um nível-alvo (SL-T) por zona; os componentes precisam então de capacidades (SL-C) que, com medidas compensatórias, o alcancem (SL-A). A proposta de Maya fixa SL-T 3 para a zona de controle da caldeira, porque o seu comprometimento pode cortar o calor de milhares de casas, SL-T 2 para a zona dos medidores e nenhum conduíte roteável para o SIS-H. O SL-C do próprio PLC-H é baixo, já que ele não consegue autenticar clientes Modbus, então alcançar o SL-A 3 depende dos controles compensatórios ao seu redor.

### Exemplo resolvido (LDHP sintética)

Maya propõe SL-T 3 para a zona de controle da caldeira (PLC-H, HMI-1), SL-T 2 para a zona dos medidores IoT, e mantém o SIS-H como uma zona própria, sem nenhum conduíte roteável. Justificativa: o comprometimento da zona de controle pode causar perda de calor para milhares de casas; o comprometimento dos medidores afeta principalmente o faturamento e a privacidade; o SIS precisa continuar independente de ambos.

> **Caso sintético — Lakeside District Heating Plant.** As escolhas de nível de segurança aqui ilustram o raciocínio; uma avaliação real segue o processo documentado da IEC 62443-3-2.

### Erros e limites

Uma DMZ com uma regra de firewall "any → any" entre as suas metades é um diagrama, não um controle. Os níveis de Purdue não ditam a confiança; um sensor de IIoT pode falar diretamente com um serviço em nuvem e precisa ser zoneado pelos seus próprios méritos.

### Exercícios

- **EX046 — Posicionando o gateway de medidores.** Onde você posicionaria o gateway de medidores IoT da LDHP no modelo de Purdue ou ao redor dele, e por que ele não se encaixa bem? *Rubrica:* 3 = zona própria (muitas vezes ao lado do nível 3/DMZ), porque faz a ponte entre dispositivos de campo e um serviço em nuvem; 2 = nível sem justificativa; 1 = nível 1 dentro da zona de controle; 0 = nada.
- **EX047 — Um conjunto de regras para a DMZ.** Escreva duas regras de firewall que permitam aos usuários corporativos ver dados do historiador sem alcançar o HIST-1. *Rubrica:* 3 = HIST-1 → réplica na DMZ (envio) e Corporativo → réplica (leitura), sem Corporativo → HIST-1; 2 = uma; 1 = regra direta; 0 = nada.
- **EX048 — Justificando o SL-T 3.** Em duas frases, justifique o SL-T 3 para a zona de controle da caldeira. *Rubrica:* 3 = gravidade da consequência e atacante habilidoso plausível; 2 = um dos dois; 1 = "é importante"; 0 = nada.

### Síntese

Arquitetura é a arte de decidir quais sessões podem existir; zonas, conduítes, uma DMZ de verdade e níveis de segurança tornam essas decisões explícitas e testáveis.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue estudando — capítulo 16 de 40

[← Capítulo 15](#ch-15) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Conceitos de criptografia

### Objetivos de aprendizagem

Você vai (1) explicar códigos de autenticação de mensagem e por que, em TO, a integridade muitas vezes importa mais que o sigilo; (2) usar `hmac` e `hashlib` da biblioteca padrão; (3) impedir a repetição (replay) com contadores; e (4) listar os custos operacionais da criptografia em dispositivos com recursos limitados.

### 17.1 Integridade primeiro

A leitura de um medidor de calor não é segredo para o seu dono, mas uma leitura forjada muda uma conta, e um comando de controle forjado muda um processo. Um código de autenticação de mensagem (MAC) permite que um receptor que compartilha uma chave secreta verifique que a mensagem veio de quem tem a chave e não foi alterada. O HMAC com SHA-256 é uma construção muito usada, padronizada no FIPS 198-1. Na LDHP, o que está em jogo é uma conta e uma caldeira. Uma leitura de medidor forjada reduz a conta de uma residência; uma escrita forjada no registrador 100 do PLC-H muda o calor fornecido a todas as residências. O laboratório de HMAC usa leituras de medidores porque é ali que a questão da integridade fica mais clara.

### 17.2 Repetição

Uma mensagem válida capturada ontem continua criptograficamente válida hoje. Incluir um contador estritamente crescente (ou um carimbo de tempo verificado contra uma janela) dentro dos dados autenticados permite que o receptor rejeite repetições.

```python
"""Lab 17: HMAC-protected meter readings with a replay counter (synthetic key)."""
import hmac, hashlib
KEY = b"synthetic-lab-key-not-for-use"
def tag(ctr, kwh): return hmac.new(KEY, f"{ctr}|{kwh}".encode(), hashlib.sha256).hexdigest()[:16]
last = 0
msgs = [(1, 120.5, tag(1, 120.5)), (2, 121.0, tag(2, 121.0)), (2, 121.0, tag(2, 121.0)), (3, 99.0, tag(3, 121.4))]
for ctr, kwh, t in msgs:
    if not hmac.compare_digest(t, tag(ctr, kwh)): print(ctr, kwh, "REJECT bad tag")
    elif ctr <= last: print(ctr, kwh, "REJECT replay")
    else: last = ctr; print(ctr, kwh, "accept")
```

Execute com `python3 lab_hmac.py`. Saída verificada:

```text
1 120.5 accept
2 121.0 accept
2 121.0 REJECT replay
3 99.0 REJECT bad tag
```

No laboratório de HMAC, uma leitura aceita uma vez com o contador 2 é rejeitada quando os mesmos bytes chegam de novo, embora a sua tag esteja correta; só o significado do contador é diferente. Para os medidores da LDHP, isso impede que um morador com equipamento de rádio repita a leitura mais baixa do mês anterior, que é o caso de abuso escrito no Capítulo 26.

### 17.3 Lendo a execução

A mensagem 2 é aceita uma vez e rejeitada na segunda vez como repetição, mesmo com a tag correta. A mensagem 3 traz uma tag calculada para 121,4 kWh, mas declara 99,0 kWh, então a verificação falha. Observe o `hmac.compare_digest`, que compara em tempo constante e evita vazar quantos caracteres iniciais coincidiram. Para a LDHP, a segunda rejeição é o cenário do morador: uma leitura mais baixa capturada e repetida para a conta do mês seguinte falha no contador, embora todos os bytes da tag sejam genuínos. A terceira rejeição é adulteração em trânsito: um gateway ou atacante que muda 121,4 kWh para 99,0 kWh sem a chave do medidor não consegue produzir uma tag correspondente.

### 17.4 Custos operacionais

As chaves precisam ser provisionadas por dispositivo, trocadas e revogadas; um medidor substituído após uma falha precisa de uma chave nova, e uma chave compartilhada por toda a frota significa que uma única chave extraída forja todos os medidores. Dispositivos limitados podem não ter hardware para armazenamento seguro de chaves. A provisão 5.4 da ETSI EN 303 645 pede que os parâmetros sensíveis de segurança sejam armazenados com segurança e que não se usem parâmetros críticos de segurança fixos no código do software do dispositivo. A estimativa de tamanho de Maya põe o custo de rádio em 1,5 MB por dia para 4.000 medidores; o processo de chaves é o custo maior.

### Exemplo resolvido (LDHP sintética)

Maya calcula o acréscimo de tamanho: uma tag truncada de 16 caracteres hexadecimais (64 bits) mais um contador de 8 bytes acrescentam 16 bytes por leitura. A uma leitura por hora por medidor, em 4.000 medidores, isso dá 1,5 MB por dia — irrelevante para a rede, mas o processo de gestão de chaves é o custo real.

> **Caso sintético — Lakeside District Heating Plant.** A chave do laboratório é uma string de exemplo; nunca embuta chaves no código.

### Erros e limites

Truncar MACs reduz a resistência à falsificação; 64 bits é um mínimo comum nesse tipo de projeto. Um hash sozinho (sem chave) não oferece autenticação. Criptografia sem proteção de integridade pode ser maleável.

### Exercícios

- **EX049 — Detectando um contador reiniciado.** Depois de uma atualização de firmware do medidor, o contador recomeça em 1. O que o receptor do laboratório faz, e como o projeto deveria tratar isso? *Rubrica:* 3 = rejeita como repetição; trocar a chave ou persistir o contador com um campo de época da chave; 2 = só o comportamento; 1 = aceita; 0 = nada.
- **EX050 — Por que não SHA-256 puro?** Explique por que anexar SHA-256(leitura) não impede a falsificação. *Rubrica:* 3 = não há segredo: qualquer um pode recalcular o hash de um valor forjado; 2 = parcial; 1 = "o SHA-256 é fraco"; 0 = nada.
- **EX051 — Risco de uma chave para toda a frota.** Descreva a consequência de os 4.000 medidores compartilharem uma única chave HMAC. *Rubrica:* 3 = extraí-la de um medidor permite forjar leituras de qualquer medidor; chaves por dispositivo limitam o raio de impacto; 2 = parcial; 1 = vago; 0 = nada.

### Síntese

Para dados de TO, integridade autenticada com proteção contra repetição é o principal objetivo criptográfico, e é a gestão de chaves — não o algoritmo — que decide se ela funciona.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue estudando — capítulo 17 de 40

[← Capítulo 16](#ch-16) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Métodos de pesquisa I

### Objetivos de aprendizagem

Você vai (1) transformar uma preocupação vaga numa pergunta pesquisável; (2) escolher entre desenhos descritivos, comparativos e experimentais; (3) definir variáveis, medidas e ameaças à validade; e (4) buscar e avaliar literatura revisada por pares sobre segurança de TO.

### 18.1 Da preocupação à pergunta

"Os nossos detectores são bons?" não é uma pergunta que você consiga responder. "Nos dados sintéticos de temperatura de ida da LDHP, um detector CUSUM alcança uma taxa de alarmes falsos menor que uma faixa fixa, com a mesma taxa de detecção, para rampas lentas?" é. Ela nomeia a população (dados sintéticos), a comparação, as medidas de resultado e a classe de ataque. A versão de Maya dessa pergunta virou o seu plano de pesquisa: CUSUM contra uma faixa fixa em dados simulados de temperatura de ida, 40 sementes por condição, com alarmes falsos por execução, detecção em até 100 amostras e atraso médio como medidas, e a rampa lenta de 0,08 °C por amostra como classe de ataque.

### 18.2 Escolhas de desenho

Estudos descritivos caracterizam o que existe (inventário dos protocolos numa rede). Estudos comparativos contrastam grupos ou métodos sem controlar a alocação. Experimentos manipulam uma variável — o tipo de detector — mantendo as outras fixas, em TO tipicamente por simulação, porque experimentar em plantas em operação é inseguro. O estudo de detectores de Maya é um experimento nesse sentido: o tipo de detector é a variável manipulada, e o nível de ruído, a inclinação do ataque e as sementes são mantidos fixos entre as condições. Rodá-lo no próprio PLC-H significaria fazer derivar de propósito a temperatura de ida de uma rede de aquecimento distrital em operação, o que nenhuma permissão de trabalho autorizaria.

### 18.3 Validade

A validade interna pergunta se a diferença medida é causada pela variável manipulada; a validade externa pergunta se os resultados se generalizam para além da planta sintética. A validade de construto pergunta se "taxa de alarmes falsos por execução" mede de fato a carga sobre os operadores. Nomeie cada ameaça e o que você fez a respeito. Maya nomeou duas ameaças no seu plano: o ruído é gaussiano, o que os sensores reais de temperatura de ida podem não ser (validade externa), e ela ajustou os limiares à mão (validade interna). O seu trabalho de conclusão trata depois da segunda, ajustando num conjunto separado de 50 sementes e congelando o limiar.

### 18.4 Lendo a literatura

Giraldo et al. (2018, *ACM Computing Surveys*, doi:10.1145/3203245) revisam a detecção de ataques baseada em física em sistemas ciberfísicos e destacam que muitos artigos avaliam detectores sem um modelo de adversário consistente. Urbina et al. (CCS 2016, doi:10.1145/2976749.2978388) propõem avaliar detectores pelo impacto que um atacante furtivo ainda consegue causar sem ser detectado, e não apenas pela taxa de detecção. Esses dois artigos enquadram o laboratório de detectores do Capítulo 25. Para o estudo de Maya, a pergunta de Urbina et al. vira: quão lenta pode ser uma rampa para ficar abaixo do limiar do CUSUM, e quanto a temperatura de ida poderia derivar antes de ele alarmar? É por isso que, mais adiante, ela reduz a inclinação pela metade.

### Exemplo resolvido (LDHP sintética)

Maya redige: Pergunta — a comparação entre CUSUM e faixa acima. Desenho — experimento de simulação, 40 sementes por condição. Medidas — alarmes falsos por execução, detecção em até 100 amostras, atraso médio. Ameaças — o ruído sintético é gaussiano (validade externa); limiares ajustados à mão (validade interna).

> **Caso sintético — Lakeside District Heating Plant.** O plano de pesquisa é um exercício didático que usa apenas dados simulados.

### Erros e limites

Buscar apenas white papers de fornecedores rende marketing, não evidência. Não cite um artigo que você não abriu; verifique se os DOIs resolvem.

### Exercícios

- **EX052 — Afiando uma pergunta vaga.** Reescreva "A rede de medidores IoT é segura?" como uma pergunta pesquisável. *Rubrica:* 3 = população, medida e comparação declaradas; 2 = duas; 1 = continua vaga; 0 = nada.
- **EX053 — Nomeando uma ameaça à validade.** Identifique uma ameaça à validade externa no desenho de Maya e uma mitigação. *Rubrica:* 3 = ruído gaussiano/planta única; acrescentar perfis de ruído reais ou um segundo modelo; 2 = só a ameaça; 1 = ameaça interna; 0 = nada.
- **EX054 — A métrica de Urbina numa frase.** Enuncie a ideia de avaliação de Urbina et al. (2016). *Rubrica:* 3 = medir o impacto máximo que um atacante não detectado (furtivo) consegue alcançar, e não só a taxa de detecção; 2 = parcial; 1 = errado; 0 = nada.

### Síntese

A pesquisa começa com uma pergunta afiada, um desenho que se ajusta a ela, ameaças à validade declaradas com honestidade e fontes que você de fato leu.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue estudando — capítulo 18 de 40

[← Capítulo 17](#ch-17) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Segurança de TO, IoT e sistemas ciberfísicos: escopo e teoria

### Objetivos de aprendizagem

Você vai (1) definir TO, IIoT, IoT de consumo e sistemas ciberfísicos, e onde eles se sobrepõem; (2) explicar a malha de realimentação como o objeto a ser protegido; (3) identificar as normas centrais de cada domínio; e (4) descrever por que a engenharia de segurança física e a de segurança da informação precisam ser coordenadas.

### 19.1 Definições

Tecnologia operacional é o hardware e o software que monitoram ou controlam dispositivos e processos físicos. O NIST SP 800-82r3 ampliou o seu escopo de "sistemas de controle industrial" para a TO em geral, incluindo automação predial e transporte. Dispositivos IoT são coisas conectadas à rede com sensoriamento ou atuação; o NIST IR 8259 enquadra as atividades de base que os fabricantes devem realizar para eles. Um sistema ciberfísico é a combinação de computação, rede e processo físico numa malha fechada. A LDHP contém os três: o PLC-H e o SIS-H são TO, os medidores de calor e os gateways são IoT, e a malha de temperatura de ida é um sistema ciberfísico.

### 19.2 A malha como ativo

O que um defensor de TO protege não é um computador, mas uma malha de realimentação: sensor → controlador → atuador → processo → sensor. Um atacante pode falsificar a leitura do sensor, alterar a lógica ou os parâmetros do controlador, sobrepor-se ao atuador ou interromper a comunicação que os liga. Cada uma dessas ações corresponde a táticas do ATT&CK for ICS, como *Impair Process Control* e *Inhibit Response Function*. A malha da LDHP de Maya é TT-101 → PLC-H → válvula de combustível FV-12 → caldeira → TT-101. Para cada elemento, ela nomeia um ataque e a salvaguarda independente dele: o SIS-H, com o seu próprio transmissor TT-101S, cabeado ao corte de combustível.

### 19.3 Mapa das normas

A IEC 62443 cobre sistemas de automação e controle industrial para proprietários de ativos, integradores e fornecedores de produtos. O NIST SP 800-82r3 é um guia para programas de segurança de TO. O NIST IR 8259 (e o 8259A) fixa linhas de base de capacidades de cibersegurança de dispositivos IoT para fabricantes. A ETSI EN 303 645 é a linha de base europeia para IoT de consumo. Elas se sobrepõem, mas respondem a perguntas diferentes: quem precisa fazer o quê, para que tipo de sistema. Para a LDHP: a IEC 62443 para o PLC-H e a zona de controle, o SP 800-82r3 para o programa, o IR 8259 e a EN 303 645 para os medidores e os gateways.

### 19.4 Segurança física e segurança da informação

A segurança funcional (IEC 61508; IEC 61511 para as indústrias de processo) pressupõe falhas aleatórias e sistemáticas; a segurança da informação pressupõe um adversário. Um sistema instrumentado de segurança precisa continuar independente, para que uma perturbação de processo induzida por ataque cibernético ainda termine num estado seguro. Tanto a IEC 62443 quanto a IEC 61511 orientam os profissionais a coordenar as duas análises. Na LDHP, o SIS-H corta o fornecimento de combustível em alta temperatura usando o TT-101S, um transmissor separado do TT-101 do PLC-H, e o trip é cabeado. Um ataque cibernético que leve o PLC-H a superaquecer a caldeira ainda encontra um trip independente, desde que nada na rede consiga alterar o ponto de trip do SIS-H.

### Exemplo resolvido (LDHP sintética)

Maya mapeia a malha de temperatura de ida da LDHP: TT-101 → PLC-H → válvula de combustível FV-12 → caldeira → TT-101. Ela lista um ponto de ataque por elemento e a salvaguarda independente: o SIS-H, com o seu próprio transmissor de temperatura TT-101S, cabeado ao corte de combustível.

> **Caso sintético — Lakeside District Heating Plant.** As tags da malha são inventadas.

### Erros e limites

Rótulos como "TO" e "IoT" são conveniências; um sensor de gestão predial em Wi-Fi é as duas coisas. Não escolha uma norma pela familiaridade com a marca; escolha pelo papel e pelo tipo de sistema.

### Exercícios

- **EX055 — Quatro pontos de ataque numa malha.** Nomeie um ponto de ataque para cada elemento da malha do TT-101. *Rubrica:* 3 = quatro, um por elemento; 2 = três; 1 = dois; 0 = nada.
- **EX056 — Associando normas a papéis.** Qual documento serve para (a) a linha de base do produto do fabricante de medidores, (b) o próprio programa de segurança de TO da LDHP? *Rubrica:* 3 = NIST IR 8259 ou ETSI EN 303 645 / IEC 62443-4-2; e SP 800-82r3 ou IEC 62443-2-1; 2 = um; 1 = a mesma resposta para os dois; 0 = nada.
- **EX057 — Por que o TT-101S importa.** Explique por que o SIS-H usa o seu próprio transmissor em vez de ler o TT-101 por meio do PLC-H. *Rubrica:* 3 = um caminho TT-101/CLP falsificado ou com falha cegaria o SIS; independência; 2 = parcial; 1 = custo; 0 = nada.

### Síntese

A segurança de TO, IoT e sistemas ciberfísicos protege malhas de realimentação; a norma certa depende do seu papel, e a independência da segurança física é inegociável.

<!-- open-cyber-academy:chapter-navigation:start ch-19 -->
### Continue estudando — capítulo 19 de 40

[← Capítulo 18](#ch-18) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Segurança de TO, IoT e sistemas ciberfísicos: casos fundamentais

### Objetivos de aprendizagem

Você vai (1) resumir três incidentes documentados a partir de fontes primárias; (2) extrair de cada um o caminho de ataque e a lição defensiva; (3) distinguir o que está publicamente confirmado do que é especulação; e (4) relacionar cada caso com a LDHP.

### 20.1 Rede elétrica da Ucrânia, dezembro de 2015

O alerta IR-ALERT-H-16-056-01 do ICS-CERT dos EUA relata que três distribuidoras regionais de energia elétrica da Ucrânia sofreram ataques cibernéticos coordenados que causaram interrupções afetando cerca de 225.000 clientes. O alerta relata que os agentes provavelmente usaram credenciais legítimas obtidas de antemão para acesso remoto, apagaram sistemas com o malware KillDisk, sobrescreveram algumas HMIs e corromperam o firmware de dispositivos conversores serial-Ethernet nas subestações. A energia foi restabelecida, mas as empresas continuaram em operação restrita. Lição: credenciais roubadas e acesso remoto foram o caminho, e a recuperação dependeu de ser possível operar sem a automação danificada.

### 20.2 Mirai, 2016

Antonakakis et al. ("Understanding the Mirai Botnet", USENIX Security 2017) mediram uma botnet que infectou centenas de milhares de dispositivos IoT, em grande parte entrando com credenciais padrão de fábrica por Telnet, e depois lançou grandes ataques de negação de serviço. Lição: senhas padrão universais em larga escala são um risco de infraestrutura — exatamente o que a provisão 5.1 da ETSI EN 303 645 proíbe. O análogo na LDHP são os seus gateways de medidores: se eles fossem entregues com uma única senha padrão para toda a frota, uma varredura no estilo do Mirai encontraria cada um deles alcançável a partir da internet. O MTR-B do Capítulo 30, que falha na provisão 5.1, é o modelo de medidor nessa posição.

### 20.3 Estação de tratamento de água, fevereiro de 2021

O alerta da CISA AA21-042A descreve o acesso não autorizado ao sistema SCADA de uma estação de tratamento de água potável nos EUA por meio de software de acesso remoto, com uma tentativa de elevar os níveis de hidróxido de sódio. A equipe da planta percebeu e corrigiu a alteração antes que o software SCADA alarmasse. O alerta aponta um software de compartilhamento de área de trabalho e um sistema operacional em fim de vida como prováveis fraquezas. Lição: a vigilância do operador importa, e as ferramentas de acesso remoto fazem parte da superfície de ataque. O análogo na LDHP é a sua própria ferramenta de área de trabalho remota do fornecedor, sempre ligada, que Maya substituiu por sessões intermediadas de quatro horas.

### 20.4 Ler os casos com cuidado

Cada fonte documenta alguns fatos, e não outros. Escreva o que a fonte diz, cite-a e marque todo o resto como inferência. Recontagens populares muitas vezes acrescentam uma certeza que o relatório primário não tem. A tabela de casos de Maya segue essa regra. Para a estação de água de 2021, ela registra apenas o que o AA21-042A afirma — software de acesso remoto, compartilhamento de área de trabalho e um sistema operacional em fim de vida — e marca o seu análogo na LDHP, a ferramenta de área de trabalho remota do fornecedor sempre ligada, como inferência própria. Para o Mirai, o método de infecção vem da medição de Antonakakis et al., e não de resumos da imprensa. Para a Ucrânia, a lição que ela tira, manter procedimentos documentados de partida manual da caldeira, é rotulada como uma recomendação para a LDHP, e não como um achado da fonte.

### Exemplo resolvido (LDHP sintética)

Maya monta uma tabela: caso, acesso inicial, efeito, o que o deteve, análogo na LDHP. Para o caso da água de 2021, o análogo é a ferramenta de área de trabalho remota do fornecedor sempre ligada da LDHP (Capítulo 13); para o Mirai, as senhas padrão dos gateways de medidores; para a Ucrânia, a necessidade de operar depois que a automação é danificada — a LDHP mantém procedimentos documentados de partida manual da caldeira.

> **Caso sintético — Lakeside District Heating Plant.** Só os análogos na LDHP são sintéticos; os três casos vêm das fontes públicas citadas.

### Erros e limites

Afirmações de atribuição em reportagens não fazem parte das evidências deste capítulo. As lições dos casos só se generalizam onde as condições coincidem.

### Exercícios

- **EX058 — Detalhes da fonte primária.** A partir do alerta do ICS-CERT de 2016, informe o número aproximado de clientes afetados e uma ação dos agentes contra dispositivos de campo. *Rubrica:* 3 = ~225.000 e firmware dos conversores serial-Ethernet corrompido (ou KillDisk nas HMIs); 2 = um; 1 = número errado; 0 = nada.
- **EX059 — O método de entrada do Mirai.** O que o Mirai explorava principalmente para infectar dispositivos, e qual provisão da ETSI trata disso? *Rubrica:* 3 = credenciais padrão por Telnet; provisão 5.1; 2 = um; 1 = "um zero-day"; 0 = nada.
- **EX060 — Fato versus inferência.** Marque como fato da fonte ou inferência: (a) "um operador reverteu a alteração do hidróxido de sódio" (b) "o intruso pretendia um envenenamento em massa". *Rubrica:* 3 = (a) fato do AA21-042A, (b) inferência; 2 = um; 1 = os dois como fatos; 0 = nada.

### Síntese

Leia os incidentes a partir das fontes primárias, separe o fato da narrativa e transforme cada um numa pergunta concreta sobre a sua própria planta.

<!-- open-cyber-academy:chapter-navigation:start ch-20 -->
### Continue estudando — capítulo 20 de 40

[← Capítulo 19](#ch-19) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-21"></a>

## Capítulo 21 — Segurança de TO, IoT e sistemas ciberfísicos: modelos de sistema

### Objetivos de aprendizagem

Você vai (1) construir um modelo em tempo discreto de um tanque ou de uma malha; (2) explicar o controle proporcional e o seu erro de regime permanente; (3) usar um modelo para prever com que rapidez um setpoint manipulado altera o processo; e (4) dizer o que um modelo simplificado deixa de fora.

### 21.1 Por que modelar

Um modelo transforma "o atacante altera o setpoint" em "o nível alcança o alarme de transbordamento em 12 minutos". Os defensores usam esse tempo para dimensionar a detecção e a resposta: se o processo dá 12 minutos, um detector que leva 20 é inútil para esse cenário. Para a LDHP, a pergunta é concreta: se o registrador 100 for escrito com 30 °C às 02:10, quanto tempo até os radiadores do distrito esfriarem o bastante para os moradores perceberem, e quanto tempo até a tubulação das ruas mais frias correr risco? No exercício de mesa do Capítulo 29, o operador restabeleceu 90 °C às 02:15, cinco minutos depois do alerta. Um modelo diz se cinco minutos são confortáveis ou estão perto do limite e, portanto, se a detecção precisa ser o alerta do monitor, e não o telefonema de um morador.

### 21.2 Um tanque pulmão com controle proporcional

O vaso de expansão da LDHP amortece o volume de água conforme a temperatura muda. O laboratório modela o seu nível com um controlador proporcional que define a vazão de entrada como kp·(setpoint − nível), limitada à faixa 0–5 da bomba, contra uma vazão de saída constante.

```python
"""Lab 21: discrete-time model of a synthetic buffer tank with a proportional level loop."""
level, sp, kp = 40.0, 60.0, 0.08
for step in range(0, 61):
    inflow = max(0.0, min(5.0, kp * (sp - level) * 10))
    outflow = 2.0
    if step % 10 == 0: print(f"t={step:2} level={level:5.1f}% inflow={inflow:4.2f}")
    level += (inflow - outflow) * 0.5
print("steady-state error ~", round(sp - level, 1), "pct (P-only offset)")
```

Execute com `python3 lab_tank.py`. Saída verificada:

```text
t= 0 level= 40.0% inflow=5.00
t=10 level= 55.0% inflow=4.00
t=20 level= 57.5% inflow=2.01
t=30 level= 57.5% inflow=2.00
t=40 level= 57.5% inflow=2.00
t=50 level= 57.5% inflow=2.00
t=60 level= 57.5% inflow=2.00
steady-state error ~ 2.5 pct (P-only offset)
```

O laboratório usa kp = 0,08, multiplicado por 10 na linha da vazão de entrada, o que dá um ganho efetivo de 0,8, um setpoint de 60 %, um nível inicial de 40 % e a vazão de saída fixa em 2,0, de modo que a bomba começa no seu limite de 5,0. A saída imprime o nível a cada 10 passos: 55,0 % em t = 10, depois 57,5 % a partir de t = 20, com vazão de entrada de 2,01 em t = 20 e 2,00 a partir de t = 30. Os números são inventados para o vaso da LDHP, mas a forma é geral: uma malha proporcional que não consegue alcançar exatamente o seu setpoint.

### 21.3 Lendo o modelo

O nível sobe depressa enquanto a vazão de entrada está saturada em 5 e depois se estabiliza em 57,5 %, e não em 60 %. Essa diferença de 2,5 pontos é o clássico erro de regime do controle apenas proporcional: no equilíbrio, a vazão de entrada precisa igualar a de saída (2,0), o que exige um erro diferente de zero (2,0 / 0,8 = 2,5). A ação integral remove o erro de regime; os engenheiros costumam usar controle PI ou PID. Para a segurança, esse erro importa de um jeito fácil de passar despercebido: um operador acostumado a ver 57,5 % contra um setpoint de 60 % não vai notar uma pequena diferença adicional. Um viés de sensor ou uma alteração modesta de setpoint se esconde dentro de uma diferença que todos já aceitam como normal.

### 21.4 Usando o modelo para a segurança

Se um atacante move o setpoint de 60 % para 95 %, o modelo prevê quanto tempo o nível leva para cruzar um alarme de nível alto em 85 %. O mesmo modelo diz como um viés de sensor de +10 pontos faria o controlador encher o vaso de menos. Os modelos ligam ações cibernéticas ao tempo do processo. Para usar o laboratório assim, mude o setpoint numa cópia do script de 60 para 95 num passo escolhido e imprima o primeiro passo em que o nível passa de 85; com a bomba limitada a 5,0 contra a vazão de saída fixa em 2,0, o nível pode subir no máximo (5,0 − 2,0) × 0,5 = 1,5 ponto por passo. Registre a edição e a saída juntas. Um viés de sensor de +10 funciona ao contrário: o controlador vê o nível 10 pontos acima do real, então se estabiliza cerca de 10 pontos abaixo, e ninguém percebe isso na HMI-1.

### Exemplo resolvido (LDHP sintética)

Usando a dinâmica do laboratório, com a vazão de entrada saturada em 5 e a de saída em 2, o nível sobe (5 − 2) × 0,5 = 1,5 ponto por passo. Do regime permanente de 57,5 % até um alarme em 85 % são 27,5 pontos, ou seja, cerca de 18–19 passos. Se um passo representa 20 segundos, os operadores têm aproximadamente seis minutos.

> **Caso sintético — Lakeside District Heating Plant.** Os ganhos do tanque e a duração do passo são inventados.

### Erros e limites

Vasos reais têm geometria não linear, dinâmica de válvulas e ruído de medição. Um modelo validado na operação normal pode estar errado nos estados extremos que um atacante procura. Nunca derive limites reais da planta de um modelo de sala de aula.

### Exercícios

- **EX061 — Erro de regime com ganho maior.** Se kp = 0,16 (ganho ×10 = 1,6), que erro de regime permanente o modelo prevê? *Rubrica:* 3 = 2,0 / 1,6 = 1,25 ponto; 2 = método certo; 1 = diz zero; 0 = nada.
- **EX062 — Tempo até o alarme.** Partindo de 57,5 % com a vazão de entrada saturada, quantos passos até o nível passar de 70 %? *Rubrica:* 3 = 9 passos (57,5 + 1,5 × 9 = 71,0); 2 = 8–9 com justificativa; 1 = ignora a vazão de saída; 0 = nada.
- **EX063 — Efeito do viés do sensor.** Se o sensor de nível lê 10 pontos acima, onde o nível real se estabiliza? *Rubrica:* 3 = cerca de 47,5 % (o controlador mantém o valor medido em 57,5); 2 = direção certa; 1 = 67,5; 0 = nada.

### Síntese

Modelos simples de processo dão aos defensores um relógio: quanto tempo uma malha manipulada leva para chegar ao dano e, portanto, com que rapidez a detecção e a resposta precisam acontecer.

<!-- open-cyber-academy:chapter-navigation:start ch-21 -->
### Continue estudando — capítulo 21 de 40

[← Capítulo 20](#ch-20) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 22 →](#ch-22)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-22"></a>

## Capítulo 22 — Segurança de TO, IoT e sistemas ciberfísicos: dados e dependências

### Objetivos de aprendizagem

Você vai (1) construir um inventário de ativos e de dependências; (2) rastrear os fluxos de dados do dispositivo de campo até o uso no negócio; (3) encontrar pontos únicos de falha, incluindo pessoas e fornecedores; e (4) usar uma lista de materiais de software (SBOM) para raciocinar sobre vulnerabilidades herdadas.

### 22.1 Inventário primeiro

Você não consegue proteger o que não listou. O NIST SP 800-82r3 põe o inventário de ativos no início de um programa de segurança de TO. Um inventário útil registra não só fabricante, modelo e firmware, mas também função, zona, responsável, criticidade e o que depende do ativo. A lista de dependências de Maya neste capítulo parte de um inventário assim: TT-101, PLC-H com firmware v3.2, FV-12, switch de controle SW-2, HMI-1, servidor de licenças LIC-1, EWS-1 e o contrato de suporte do fornecedor. Registrar a v3.2 é o que permitiria à LDHP responder a um alerta de firmware de CLP no mesmo dia; registrar o LIC-1 como dependência da HMI-1 é o que expôs um ponto único de falha que nenhum diagrama de rede mostrava.

### 22.2 Cadeias de dependência

O PLC-H depende de alimentação de 24 V, dos seus módulos de E/S, do switch da rede de controle, da estação de engenharia para mudanças de lógica e do fornecedor para o firmware. A HMI-1 depende do Windows, do servidor de licenças do runtime da HMI e do controlador de domínio para as contas nominais. Uma queda do servidor de licenças que apague as HMIs é um incidente de disponibilidade com causa raiz cibernética, mesmo sem atacante. Maya marcou o LIC-1 como o ponto único de falha escondido e perguntou ao fornecedor da HMI sobre um período de carência da licença, que deixaria a HMI-1 continuar funcionando se o LIC-1 ficasse fora do ar por uma noite.

### 22.3 Dependências de fornecedores

O firmware do gateway de medidores embute uma pilha TCP/IP de código aberto e uma biblioteca TLS. Se uma vulnerabilidade for publicada nessa pilha, todos os gateways a herdam. Uma lista de materiais de software (SBOM) relaciona esses componentes para que, quando um alerta aparecer, a planta consiga responder "somos afetados?" em horas, e não em semanas. Os alertas de ICS da CISA identificam os produtos e as versões afetados, o que só ajuda se o seu inventário registrar versões. O MTR-C do Capítulo 30 é o caso em que um SBOM sozinho não basta: mesmo que ele mostre uma pilha afetada, o dispositivo não pode ser atualizado.

### 22.4 Pessoas como dependências

Se só um engenheiro consegue restaurar a lógica do PLC-H a partir do backup, essa pessoa é um ponto único de falha. Documente os procedimentos e treine mais gente. Na LDHP, o risco é maior à noite, no inverno. Se a lógica do PLC-H fosse corrompida, por um download malsucedido a partir da EWS-1 ou de propósito, restaurá-la exigiria o último arquivo de programa bom, a versão de firmware correspondente (v3.2 na lista de Maya) e alguém que conheça os passos de restauração naquele controlador. Se essa pessoa estiver de férias em janeiro, a caldeira opera em controle manual local até ela voltar. A recomendação de Maya foi um procedimento de restauração escrito, testado em bancada uma vez por ano por um segundo engenheiro, com o hash do arquivo de backup registrado ao lado de cada restauração testada.

### Exemplo resolvido (LDHP sintética)

Maya escreve a lista de dependências da função de temperatura de ida: TT-101, PLC-H (firmware v3.2), FV-12, switch de controle SW-2, HMI-1, servidor de licenças LIC-1, estação de engenharia EWS-1, contrato de suporte do fornecedor. Ela marca o LIC-1 como um ponto único de falha escondido e recomenda verificar com o fornecedor da HMI o período de carência da licença.

> **Caso sintético — Lakeside District Heating Plant.** As versões e os nomes são inventados.

### Erros e limites

Um inventário construído apenas por varredura de rede deixa de fora dispositivos seriais e peças reserva desligadas, e a varredura ativa pode perturbar dispositivos frágeis; combine captura passiva, exportações de configuração e inspeções em campo.

### Exercícios

- **EX064 — Campos de um registro de inventário.** Liste seis campos para uma entrada de inventário de ativos de TO. *Rubrica:* 3 = seis, incluindo versão de firmware, zona e criticidade; 2 = quatro ou cinco; 1 = só fabricante/modelo; 0 = nada.
- **EX065 — Respondendo a um alerta.** Um alerta da CISA lista como afetadas as versões 2.0–2.4 da biblioteca TLS do gateway. Quais dois fatos do inventário decidem se a LDHP é afetada? *Rubrica:* 3 = versão do firmware do gateway e versão do componente no seu SBOM; 2 = um; 1 = só o nome do fornecedor; 0 = nada.
- **EX066 — Um ponto único escondido.** Identifique um ponto único de falha da LDHP que não seja de rede e uma mitigação. *Rubrica:* 3 = por exemplo, um único engenheiro, servidor de licenças, peça reserva única; com mitigação; 2 = só o ponto; 1 = só dispositivo de rede; 0 = nada.

### Síntese

Inventários, cadeias de dependência e SBOMs permitem que uma planta raciocine sobre falhas e alertas antes que eles cheguem.

<!-- open-cyber-academy:chapter-navigation:start ch-22 -->
### Continue estudando — capítulo 22 de 40

[← Capítulo 21](#ch-21) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 23 →](#ch-23)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-23"></a>

## Capítulo 23 — Segurança de TO, IoT e sistemas ciberfísicos: métodos I

### Objetivos de aprendizagem

Você vai (1) realizar uma avaliação de risco orientada a consequências para uma zona; (2) usar com responsabilidade uma matriz de probabilidade–consequência; (3) relacionar a avaliação com o fluxo de trabalho da IEC 62443-3-2; e (4) registrar o risco residual com um responsável.

### 23.1 Começar pela consequência

Em TO, a avaliação começa perguntando o que o processo pode fazer que seria inaceitável — perda de calor no inverno, sobrepressão, escaldamento — e só depois quais caminhos cibernéticos poderiam causá-lo. Começar pelas vulnerabilidades produz longas listas de achados de baixo impacto; começar pela consequência concentra o esforço nas malhas que importam. Na LDHP, os resultados inaceitáveis são a perda de calor para 4.000 casas no inverno e a sobretemperatura na ida. O primeiro tem caminhos cibernéticos pelo registrador 100 e pela EWS-1; o segundo também tem um caminho, mas o trip independente do SIS-H limita a sua consequência. Começar por aí diz a Maya que ela deve examinar os conduítes do PLC-H antes das interfaces web dos gateways de medidores, embora os gateways fossem produzir mais achados numa varredura.

### 23.2 O fluxo de trabalho da 62443-3-2 em linhas gerais

A IEC 62443-3-2 descreve identificar o sistema em consideração, realizar uma avaliação de risco inicial de alto nível, dividi-lo em zonas e conduítes, realizar uma avaliação de risco detalhada por zona e documentar os requisitos de segurança e os níveis de segurança-alvo. Você não precisa da norma completa para praticar o raciocínio, mas cite-a corretamente. Aplicado à LDHP, o sistema em consideração é a planta da caldeira com os seus medidores. A avaliação inicial identifica a perda de calor como a consequência dominante. A divisão produz a zona de controle da caldeira, a zona dos medidores e o SIS-H como uma zona própria. A avaliação detalhada por zona produz, respectivamente, o SL-T 3, o SL-T 2 e a ausência de conduítes roteáveis propostos por Maya.

### 23.3 Matrizes e as suas armadilhas

Uma matriz 5 × 5 multiplica uma nota de probabilidade por uma nota de consequência. Ela é uma ferramenta de comunicação, não aritmética: "3 × 4 = 12" não significa duas vezes pior que 6. Erros de inversão de ordem acontecem quando as categorias são largas. Mantenha sempre o cenário narrativo ao lado da nota. Na LDHP, um cenário com nota 3 × 4 para a tomada de um gateway de medidores e outro com 2 × 5 para uma escrita de setpoint no PLC-H produzem 12 e 10, o que poria o gateway em primeiro lugar. As narrativas contam outra história: o gateway afeta o faturamento e a configuração de uma rua, a escrita de setpoint afeta o calor de todas as casas. Manter a narrativa ao lado do número é o que permite a um revisor pegar essa inversão, como faz a classificação de consequências de Maya no Capítulo 26 ao pôr a repetição de leituras por um morador abaixo da tomada de um gateway.

### 23.4 Risco residual

Depois dos controles, algum risco permanece. Ele precisa ter um responsável que o aceite por escrito, uma data de revisão e as suposições em que se apoia. Para o S-3, manipulação de setpoint, o risco residual após os controles do Capítulo 24 tem duas partes: um insider com acesso de engenharia, e uma escrita feita pela própria HMI-1, a origem que está na lista de permissão. O trabalho de conclusão de Maya mostra depois que a segunda é real: a única falha de detecção restante do seu monitor foi uma escrita originada na HMI. O responsável seria o gerente da planta da LDHP, como no exemplo resolvido abaixo, que o aceita por escrito supondo que as contas nominais tornam essas escritas atribuíveis, com data de revisão seis meses depois, ou antes, se a correlação do monitor com os logins dos operadores for construída.

### Exemplo resolvido (LDHP sintética)

Cenário S-3: um malware no escritório alcança o PLC-H pela regra 14 e baixa o setpoint de ida (ATT&CK for ICS T0836). Consequência 4 (perda de calor em todo o distrito por horas, sem feridos, porque o SIS-H trata a sobretemperatura, mas não a subtemperatura). Probabilidade 3 antes dos controles. Depois de remover a regra 14 e acrescentar uma lista de permissão, probabilidade 1. Residual: permanece o insider com acesso de engenharia; responsável: gerente da planta; revisão em seis meses.

> **Caso sintético — Lakeside District Heating Plant.** As notas são ilustrativas.

### Erros e limites

A probabilidade de ataques direcionados é um julgamento, não uma frequência; declare quem a julgou e com que base. Não deixe uma nota baixa esconder uma consequência catastrófica.

### Exercícios

- **EX067 — Consequência primeiro.** Escreva uma consequência inaceitável para a zona dos medidores IoT e o caminho cibernético que poderia causá-la. *Rubrica:* 3 = consequência concreta mais caminho; 2 = um; 1 = lista de vulnerabilidades; 0 = nada.
- **EX068 — Interpretando notas da matriz.** O cenário A tem nota 2 × 5 = 10 e o B, 5 × 2 = 10. Eles são igualmente urgentes? *Rubrica:* 3 = não; A tem consequência catastrófica e precisa de tratamento diferente; julgar pela narrativa; 2 = só "não"; 1 = sim; 0 = nada.
- **EX069 — Registro de risco residual.** Escreva a declaração de risco residual do S-3 depois dos controles. *Rubrica:* 3 = caminho restante, responsável, data de revisão, suposição; 2 = três; 1 = "risco aceito"; 0 = nada.

### Síntese

Avaliação orientada a consequências, uso honesto de matrizes e risco residual com responsável fazem de um registro de riscos de TO uma ferramenta de decisão, e não uma planilha.

<!-- open-cyber-academy:chapter-navigation:start ch-23 -->
### Continue estudando — capítulo 23 de 40

[← Capítulo 22](#ch-22) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 24 →](#ch-24)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-24"></a>

## Capítulo 24 — Segurança de TO, IoT e sistemas ciberfísicos: controles

### Objetivos de aprendizagem

Você vai (1) escolher controles preventivos, detectivos e corretivos para um cenário; (2) mapeá-los para os requisitos fundamentais da IEC 62443-3-3; (3) reconhecer controles que poderiam prejudicar a disponibilidade ou a segurança física; e (4) projetar controles compensatórios para dispositivos legados.

### 24.1 Famílias de controles

A IEC 62443-3-3 agrupa os requisitos de sistema em sete requisitos fundamentais: controle de identificação e autenticação (FR 1), controle de uso (FR 2), integridade do sistema (FR 3), confidencialidade dos dados (FR 4), fluxo de dados restrito (FR 5), resposta oportuna a eventos (FR 6) e disponibilidade de recursos (FR 7). Usá-los como títulos mantém um plano de controles equilibrado. A tabela de controles de Maya para o S-3 mostra o efeito: cinco controles distribuídos entre os FR 1, 3, 5, 6 e 7. Sem os títulos, um primeiro rascunho tende a listar três regras de firewall e nada para a recuperação, que é a preocupação do FR 7. As colunas vazias, aqui o FR 2 e o FR 4, não são automaticamente lacunas, mas cada uma precisa de uma frase explicando por que não se aplica a esse cenário.

### 24.2 Associando controles ao S-3

Para o cenário de manipulação de setpoint: restringir o fluxo de dados com uma lista de permissão no firewall (FR 5); exigir contas nominais na HMI-1 (FR 1); acrescentar à lógica do PLC-H limites de setpoint confirmados pelo operador (na prática, FR 3, e também um controle de processo); alertar sobre escritas de setpoint vindas de qualquer host que não seja a HMI-1 (FR 6); manter backups testados da lógica do CLP (FR 7). A tabela de Maya registra por completo a linha do limite de setpoint: o PLC-H rejeita setpoints de ida fora de 70–110 °C, a menos que o modo de engenharia esteja ativo, FR 3, preventivo, com o modo de falha de bloquear uma mudança legítima fora da faixa durante o comissionamento, mitigado pelo modo de engenharia registrado, sob responsabilidade da engenharia de controle.

### 24.3 Controles que prejudicam

Uma prevenção de intrusão ativa que descarta escritas Modbus "suspeitas" pode bloquear um comando de emergência legítimo. O bloqueio de conta após logins malsucedidos pode trancar um operador do lado de fora durante um incidente. Cada controle precisa de uma pergunta sobre o modo de falha: se ele disparar errado, o que acontece com o processo? A linha do limite de setpoint de Maya faz essa pergunta e a responde: durante o comissionamento, um setpoint legítimo fora de 70–110 °C seria recusado, então o modo de engenharia, com registro, existe para esse caso. A mesma pergunta aplicada a um dispositivo de prevenção de intrusão em linha com o PLC-H tem uma resposta pior: se ele descartar a escrita de emergência de um operador durante uma falha numa noite fria, o processo perde o seu único caminho rápido de recuperação. É por isso que a LDHP monitora de forma passiva e impõe com a lista de permissão do firewall, que bloqueia pela origem, e não tentando adivinhar a intenção.

### 24.4 Legados e controles compensatórios

O firmware do PLC-H não consegue autenticar clientes Modbus. A abordagem compensatória é cercá-lo: conduítes com lista de permissão, para que só a HMI-1 e o HIST-1 o alcancem, monitoramento passivo do tráfego e proteção da estação de engenharia que consegue alterar a sua lógica. A lista de permissão do Capítulo 27 torna a primeira medida testável: a HMI-1 pode escrever nos registradores 100–119, o HIST-1 só pode ler, e todas as outras origens são bloqueadas. O monitoramento é o sensor passivo no switch de controle, e a proteção da EWS-1 inclui encaminhar os seus eventos de carregamento de drivers, que Maya acrescenta depois de ler o AA22-103A no Capítulo 31. Nenhuma dessas medidas altera o PLC-H; juntas, elas decidem quem consegue alcançá-lo.

### Exemplo resolvido (LDHP sintética)

A tabela de Maya tem as colunas: controle, FR, previne/detecta/corrige, modo de falha, responsável. A linha do limite de setpoint diz: "O PLC-H rejeita setpoints de ida fora de 70–110 °C, a menos que o modo de engenharia esteja ativo — FR 3 — previne — modo de falha: bloqueia uma mudança legítima fora da faixa durante o comissionamento; mitigado pelo modo de engenharia com registro — responsável: engenharia de controle."

> **Caso sintético — Lakeside District Heating Plant.** Os limites e os responsáveis são inventados.

### Erros e limites

Controles listados, mas não testados, não oferecem garantia. O mapeamento para os FRs mostra a cobertura das categorias, não que um requisito esteja atendido no nível de segurança-alvo.

### Exercícios

- **EX070 — Mapeando um controle da zona dos medidores.** Dê um controle para cada um dos FR 1, FR 5 e FR 6 na zona dos medidores. *Rubrica:* 3 = três controles relevantes mapeados corretamente; 2 = dois; 1 = um; 0 = nada.
- **EX071 — Fazendo a pergunta do modo de falha.** Qual é o modo de falha de bloquear contas da HMI após três senhas erradas, e qual é uma alternativa mais segura? *Rubrica:* 3 = operador trancado do lado de fora numa emergência; alertar e atrasar, ou isentar os consoles da sala de controle protegidos fisicamente; 2 = um; 1 = vago; 0 = nada.
- **EX072 — Compensando um dispositivo que não autentica.** Liste três controles compensatórios para um gateway de medidores que não consegue mudar a sua senha padrão. *Rubrica:* 3 = isolar, restringir a interface de gerenciamento, monitorar, planejar a substituição (quaisquer três); 2 = dois; 1 = um; 0 = nada.

### Síntese

Um bom plano de controles de TO cobre os sete requisitos fundamentais, pergunta como cada controle falha e cerca aquilo que não pode ser corrigido.

<!-- open-cyber-academy:chapter-navigation:start ch-24 -->
### Continue estudando — capítulo 24 de 40

[← Capítulo 23](#ch-23) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 25 →](#ch-25)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-25"></a>

## Capítulo 25 — Laboratório I

### Objetivos de aprendizagem

Você vai (1) executar um experimento reprodutível com detectores, usando sementes fixas; (2) comparar uma faixa fixa com um detector CUSUM quanto a alarmes falsos, detecção e atraso; (3) relatar os resultados com denominadores; e (4) ligar os resultados à crítica de avaliação de Urbina et al. (2016).

### 25.1 O experimento

O laboratório simula a temperatura de ida da LDHP em 90 °C com ruído gaussiano (σ = 1 °C). Nas execuções com ataque, a partir da amostra 100, uma rampa lenta acrescenta 0,08 °C por amostra — uma deriva furtiva de setpoint no espírito da técnica T0836 do ATT&CK for ICS. O detector de faixa alarma quando a leitura sai de 90 ± 3,5 °C. O CUSUM acumula os desvios positivos menos uma folga de 0,5 °C e alarma acima de 12.

```python
"""Lab 25: compare a fixed band and a CUSUM detector on synthetic supply temperature."""
import random
def run(seed, attack):
    rnd = random.Random(seed); s = 0.0; band = cus = None
    for t in range(200):
        x = 90 + rnd.gauss(0, 1.0) + (0.08 * (t - 100) if attack and t >= 100 else 0)
        if band is None and abs(x - 90) > 3.5: band = t
        s = max(0.0, s + (x - 90) - 0.5)
        if cus is None and s > 12: cus = t
    return band, cus
fa_b = sum(run(s, False)[0] is not None for s in range(40)); fa_c = sum(run(s, False)[1] is not None for s in range(40))
det = [run(1000 + s, True) for s in range(40)]
db = [b for b, _ in det if b is not None and b >= 100]; dc = [c for _, c in det if c is not None and c >= 100]
print(f"band : false alarms {fa_b}/40, detections {len(db)}/40, mean delay {sum(b-100 for b in db)/max(1,len(db)):.1f}")
print(f"cusum: false alarms {fa_c}/40, detections {len(dc)}/40, mean delay {sum(c-100 for c in dc)/max(1,len(dc)):.1f}")
```

Execute com `python3 lab_detect.py`. Saída verificada:

```text
band : false alarms 9/40, detections 37/40, mean delay 28.8
cusum: false alarms 0/40, detections 40/40, mean delay 23.1
```

Com σ = 1 °C, os limites de ±3,5 °C da faixa ficam a 3,5 desvios-padrão, então os alarmes falsos são raros por amostra, mas não por execução de 200 amostras.

### 25.2 Interpretando a saída

Em 40 execuções tranquilas, a faixa gerou alarmes falsos em 9 execuções — com σ = 1 °C, uma única amostra além de 3,5 σ é rara, mas em 200 amostras por execução ela acontece —, enquanto o CUSUM não gerou nenhum. Contra a rampa, o CUSUM detectou as 40 execuções, com atraso médio de 23,1 amostras; a faixa detectou 37 de 40 (contando apenas alarmes na amostra 100 ou depois), com atraso médio de 28,8. Como a faixa também dispara com ruído, algumas das suas "detecções" são excursões de ruído com sorte. Os limites de Wilson tornam a comparação concreta: as 9 execuções com alarme falso em 40 da faixa dão aproximadamente de 12 % a 38 %.

### 25.3 Relato honesto

Escreva: "CUSUM 0/40 execuções com alarme falso (limite superior de Wilson de 95 % ≈ 8,8 %), 40/40 detecções, atraso médio de 23,1 amostras, sementes 0–39 tranquilas e 1000–1039 com ataque." Não escreva "o CUSUM é perfeito". Urbina et al. também perguntariam quão grande é a rampa que um atacante conseguiria sustentar abaixo do limiar do CUSUM — uma inclinação menor poderia escapar dele por muito mais tempo. A linha da faixa deve ser relatada da mesma forma: "faixa 9/40 execuções com alarme falso (intervalo de Wilson de 95 % de cerca de 12 % a 38 %), 37/40 detecções na amostra 100 ou depois, atraso médio de 28,8 amostras". O acompanhamento de Maya, reduzindo a inclinação pela metade para 0,04 °C por amostra com as mesmas sementes, responde à pergunta de Urbina para um ponto da curva.

### Exemplo resolvido (LDHP sintética)

Maya reduz a inclinação do ataque pela metade, para 0,04 °C/amostra, numa cópia do script e registra a mudança no atraso, mantendo as sementes. Isso transforma um resultado numa curva e mostra o compromisso do atacante entre velocidade e furtividade.

> **Caso sintético — Lakeside District Heating Plant.** Todos os dados são simulados; as sementes tornam a saída reprodutível.

### Erros e limites

Ruído gaussiano e independente é otimista. Os limiares foram definidos à mão na mesma família de dados em que são avaliados.

### Exercícios

- **EX073 — Lendo as execuções com alarme falso.** Informe a contagem de alarmes falsos do detector de faixa e dê um limite superior de 95 % para a do CUSUM. *Rubrica:* 3 = 9/40 para a faixa; CUSUM 0/40 com limite superior de ≈7,5–8,8 %; 2 = um; 1 = "CUSUM 0 %"; 0 = nada.
- **EX074 — Por que um termo de folga?** Explique o papel da folga de 0,5 °C no CUSUM. *Rubrica:* 3 = subtrai o ruído esperado, para que a soma volte a zero na operação normal e só cresça sob um deslocamento sustentado; 2 = parcial; 1 = "reduz alarmes"; 0 = nada.
- **EX075 — Aplicando a crítica da furtividade.** Descreva um experimento adicional inspirado em Urbina et al. *Rubrica:* 3 = varrer a inclinação/o tamanho do ataque para achar o maior impacto não detectado numa janela de tempo; 2 = variar o limiar; 1 = só mais sementes; 0 = nada.

### Síntese

Um resultado de laboratório é uma contagem sobre sementes, com limites e um modelo de atacante; mudar o atacante é o próximo experimento, e não um detalhe posterior.

<!-- open-cyber-academy:chapter-navigation:start ch-25 -->
### Continue estudando — capítulo 25 de 40

[← Capítulo 24](#ch-24) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 26 →](#ch-26)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-26"></a>

## Capítulo 26 — Segurança de TO, IoT e sistemas ciberfísicos: métodos II

### Objetivos de aprendizagem

Você vai (1) aplicar modelagem de ameaças no estilo STRIDE a um diagrama de fluxo de dados do sistema de medidores; (2) traduzir ameaças em técnicas do ATT&CK for ICS, quando aplicável; (3) escrever casos de abuso com pré-condições; e (4) priorizar mitigações pela classificação de consequências do Capítulo 23.

### 26.1 Diagramas de fluxo de dados

Desenhe processos (círculos), repositórios de dados (linhas paralelas), entidades externas (caixas) e fluxos de dados (setas), e então marque as fronteiras de confiança onde os dados passam de uma zona para outra. O sistema de medidores da LDHP: medidores → gateway (rádio) → gateway → nuvem de faturamento (TLS) → nuvem → banco de dados de faturamento → réplica do historiador (exportação unidirecional para o balanceamento da rede). Na LDHP, o enlace de rádio dos medidores até o gateway e o uplink TLS do gateway até a nuvem de faturamento são fronteiras de confiança, assim como a exportação unidirecional para a réplica do historiador. Cada fronteira é onde a tabela STRIDE de Maya faz as suas perguntas; um diagrama sem elas poria as leituras domiciliares e os dados da caldeira na mesma zona de confiança.

### 26.2 STRIDE por elemento

Spoofing (falsificação de identidade), Tampering (adulteração), Repudiation (repúdio), Information disclosure (divulgação de informação), Denial of service (negação de serviço) e Elevation of privilege (elevação de privilégio) formam uma lista de estímulos. No enlace de rádio medidor–gateway: falsificação de identidade (um medidor falso), adulteração (leituras alteradas), divulgação de informação (consumo domiciliar). No gateway: elevação de privilégio pela sua interface web. O STRIDE foi projetado para software, então acrescente um estímulo de TO: *consequência física* — esta ameaça consegue alterar o fornecimento de calor? A tabela de Maya produziu 14 ameaças no total. As três primeiras por consequência foram a tomada de um gateway que envia configuração maliciosa a todos os medidores da sua rua, a adulteração de leituras em trânsito e o comprometimento de uma conta na nuvem que expõe o histórico de todas as residências.

### 26.3 Casos de abuso

Um caso de abuso declara agente, pré-condição, ação e resultado. "Um morador com equipamento de rádio e conhecimento do protocolo do medidor (pré-condição: nenhuma autenticação de mensagens no enlace de rádio) repete as leituras mais baixas do mês anterior (ação) para que a conta seja reduzida (resultado)." Escrever as pré-condições torna a mitigação óbvia: autenticar as leituras e usar contadores, como no Capítulo 17. A repetição pelo morador fica baixa na tabela de Maya, porque o seu resultado é uma única conta reduzida; o caso de abuso ainda importa, porque o mesmo contador ausente permitiria que um atacante no nível do gateway repetisse uma rua inteira. O laboratório de HMAC do Capítulo 17 mostra a correção: a mensagem repetida é rejeitada pelo contador, mesmo com a tag correta.

### 26.4 Mapeando para o ATT&CK

Nem toda ameaça de IoT tem uma técnica no ATT&CK for ICS, e não há problema nisso. Onde tem — gateway alcançado a partir da internet (T0883), serviços remotos abusados (T0886) —, registre o ID para ligar com a inteligência de ameaças. Para o sistema de medidores da LDHP, a T0883 serve para uma interface de gerenciamento de gateway alcançável a partir da internet, e a T0886, para o abuso de um serviço remoto usado para gerenciar gateways. Ameaças no nível da residência, como um morador repetindo a leitura do mês anterior, não têm técnica no ATT&CK for ICS, porque o framework descreve ataques ao controle industrial, e não fraude de faturamento. A tabela de Maya deixa essas linhas em branco na coluna de técnica, em vez de forçar uma correspondência ruim, e anota a provisão da ETSI EN 303 645 que se aplica no lugar.

### Exemplo resolvido (LDHP sintética)

A tabela de Maya rende 14 ameaças. Classificadas por consequência, as três primeiras são: tomada de um gateway enviando configuração maliciosa a todos os medidores da sua rua; adulteração de leituras em trânsito; comprometimento de uma conta na nuvem expondo o histórico de todas as residências. A repetição por um morador fica mais abaixo: real, mas limitada a uma conta.

> **Caso sintético — Lakeside District Heating Plant.** A lista de ameaças é o resultado de um exercício, não uma avaliação de um produto real.

### Erros e limites

Um modelo de ameaças só é tão completo quanto o seu diagrama. O STRIDE lista ameaças, não probabilidades. Rode o modelo de novo quando a arquitetura mudar.

### Exercícios

- **EX076 — STRIDE na fronteira de confiança.** Nomeie uma ameaça para cada um de S, T e D no fluxo do gateway para a nuvem. *Rubrica:* 3 = três ameaças plausíveis; 2 = duas; 1 = uma; 0 = nada.
- **EX077 — Escrevendo um caso de abuso.** Escreva um caso de abuso para a interface web do gateway. *Rubrica:* 3 = agente, pré-condição, ação, resultado; 2 = três; 1 = vago; 0 = nada.
- **EX078 — Pondo a repetição abaixo da tomada do gateway.** Justifique a classificação. *Rubrica:* 3 = escopo do impacto (uma conta vs uma rua inteira/configuração) e consequência; 2 = parcial; 1 = só "menos provável"; 0 = nada.

### Síntese

A modelagem de ameaças transforma um diagrama numa lista classificada de casos de abuso cujas pré-condições apontam diretamente para as mitigações.

<!-- open-cyber-academy:chapter-navigation:start ch-26 -->
### Continue estudando — capítulo 26 de 40

[← Capítulo 25](#ch-25) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 27 →](#ch-27)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-27"></a>

## Capítulo 27 — Segurança de TO, IoT e sistemas ciberfísicos: verificação

### Objetivos de aprendizagem

Você vai (1) escrever vetores de teste para uma política de lista de permissão; (2) incluir casos de limite, negativos e de origem desconhecida; (3) rodar testes de conformidade offline antes de qualquer implantação; e (4) explicar por que a evidência de verificação faz parte do ciclo de vida da IEC 62443.

### 27.1 Políticas precisam de testes

Um firewall ou uma lista de permissão sensível ao protocolo é código, mesmo quando escrito como regras. Verificar significa mostrar, com evidência registrada, que a política permite o que a operação precisa e bloqueia o que deve bloquear. A IEC 62443-4-1 (ciclo de vida de desenvolvimento seguro de produtos) e as atividades de comissionamento do integrador de sistemas esperam testes documentados. A política da LDHP para o PLC-H é pequena o bastante para caber numa linha: a HMI-1 pode ler com o código de função 3 e escrever nos registradores 100–119 com o código de função 6, o HIST-1 pode ler com os códigos de função 3 e 4, e todas as outras origens e funções são bloqueadas. O laboratório transforma essa linha em seis vetores com resultados esperados. Uma política que nunca foi executada contra vetores como esses é um palpite sobre o que o firewall faz.

### 27.2 Projetando vetores

Bons vetores incluem: cada par (origem, função) permitido; cada limite de uma faixa de registradores (primeiro, último, um depois do último); uma origem permitida usando uma função proibida; uma origem desconhecida; e uma função de escrita que a planta nunca usa (16, escrever vários registradores). Os resultados esperados são escritos antes de rodar o teste.

```python
"""Lab 27: conformance test of a Modbus allow-list against a test vector table."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}
WRITE_RANGE = range(100, 120)
def permit(src, fc, reg):
    if (src, fc) not in ALLOW: return "BLOCK"
    if fc == 6 and reg not in WRITE_RANGE: return "BLOCK"
    return "PASS"
vectors = [("HMI-1", 3, 100, "PASS"), ("HMI-1", 6, 119, "PASS"), ("HMI-1", 6, 120, "BLOCK"),
           ("HIST-1", 6, 105, "BLOCK"), ("ENG-WS", 16, 100, "BLOCK"), ("HIST-1", 4, 10, "PASS")]
fails = 0
for src, fc, reg, want in vectors:
    got = permit(src, fc, reg); fails += got != want
    print(f"{src:6} fc={fc:2} reg={reg:3} want={want:5} got={got:5} {'ok' if got == want else 'FAIL'}")
print("failures:", fails, "of", len(vectors))
```

Execute com `python3 lab_allow.py`. Saída verificada:

```text
HMI-1  fc= 3 reg=100 want=PASS  got=PASS  ok
HMI-1  fc= 6 reg=119 want=PASS  got=PASS  ok
HMI-1  fc= 6 reg=120 want=BLOCK got=BLOCK ok
HIST-1 fc= 6 reg=105 want=BLOCK got=BLOCK ok
ENG-WS fc=16 reg=100 want=BLOCK got=BLOCK ok
HIST-1 fc= 4 reg= 10 want=PASS  got=PASS  ok
failures: 0 of 6
```

No laboratório, os seis vetores são: a HMI-1 lendo o registrador 100; a HMI-1 escrevendo no 119, o último registrador permitido; a HMI-1 escrevendo no 120, um depois do fim; o HIST-1 escrevendo no 105; a ENG-WS usando a função 16; e o HIST-1 lendo com a função 4.

### 27.3 Lendo o resultado

Os seis vetores coincidem. Observe o vetor 3: o registrador 120 está um depois do fim de `range(100, 120)`, então precisa ser bloqueado — o clássico limite com erro de deslocamento de um. O vetor 4 confirma que o historiador não consegue escrever, mesmo dentro da faixa gravável. Uma execução limpa é evidência apenas para esses seis casos; ela não diz nada sobre o código de função 23 (ler/escrever vários registradores), a menos que você o acrescente. O pedido de mudança do colega de Maya mostra como os vetores são mantidos: estender a faixa gravável da HMI-1 para incluir o registrador 120, para um novo setpoint de velocidade de bomba, significou mudar o resultado esperado do vetor 3 para PASS, acrescentar um novo vetor (HMI-1, 6, 121, BLOCK) e só então editar o `WRITE_RANGE`.

### 27.4 Do laboratório para a planta

Antes de implantar uma política no firewall da zona de controle da LDHP, os mesmos vetores são repetidos num ambiente de bancada com o dispositivo real, primeiro em modo de monitoramento, e o resultado é anexado ao chamado de mudança. Modo de monitoramento significa que o firewall registra o que teria bloqueado, sem bloquear. Na LDHP, esse período deve cobrir pelo menos uma semana inteira, incluindo a execução do relatório semanal e uma janela de manutenção, porque uma origem legítima que escreve só de vez em quando, como a EWS-1 durante uma mudança de lógica, apareceria de outro modo pela primeira vez como uma escrita bloqueada no meio do turno de um operador. O chamado de mudança leva então os resultados dos vetores na bancada, o log do modo de monitoramento e a concordância do líder de turno com a imposição.

### Exemplo resolvido (LDHP sintética)

Um colega propõe estender a faixa gravável da HMI-1 para incluir o registrador 120 (um novo setpoint de velocidade de bomba). Maya primeiro muda o resultado esperado do vetor 3 para PASS, acrescenta o vetor (HMI-1, 6, 121, BLOCK), depois edita o `WRITE_RANGE` para `range(100, 121)` e roda de novo. A mudança nos testes é revisada junto com a mudança na política.

> **Caso sintético — Lakeside District Heating Plant.** Os números de registradores são inventados.

### Erros e limites

Testes escritos depois do código tendem a confirmar o que o código faz, e não o que a planta precisa. A conformidade offline não prova o desempenho do dispositivo sob carga.

### Exercícios

- **EX079 — Um código de função ausente.** Acrescente um vetor para (HMI-1, 23, 105). O que ele deve esperar, e o que o laboratório devolve? *Rubrica:* 3 = esperar BLOCK; o laboratório devolve BLOCK porque (HMI-1, 23) não está em ALLOW; 2 = um; 1 = PASS; 0 = nada.
- **EX080 — Limites depois da mudança de faixa.** Depois de `WRITE_RANGE = range(100, 121)`, liste os dois vetores de limite que você manteria. *Rubrica:* 3 = registrador 120 PASS e registrador 121 BLOCK; 2 = um; 1 = só o 119; 0 = nada.
- **EX081 — Escrevendo as expectativas primeiro.** Por que escrever os resultados esperados antes de rodar? *Rubrica:* 3 = evita confirmar o comportamento do código; amarra os testes ao requisito operacional; 2 = parcial; 1 = "boa prática"; 0 = nada.

### Síntese

Verificação é uma lista escrita de decisões esperadas, incluindo limites e desconhecidos, executada antes da implantação e guardada como evidência.

<!-- open-cyber-academy:chapter-navigation:start ch-27 -->
### Continue estudando — capítulo 27 de 40

[← Capítulo 26](#ch-26) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 28 →](#ch-28)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-28"></a>

## Capítulo 28 — Segurança de TO, IoT e sistemas ciberfísicos: análise de falhas

### Objetivos de aprendizagem

Você vai (1) construir uma árvore de falhas para a perda de calor no distrito; (2) combinar portas E e OU com probabilidades simples; (3) acrescentar eventos induzidos por ataques cibernéticos a uma análise no estilo da segurança física; e (4) usar a análise de modos e efeitos de falha (FMEA) para um gateway IoT.

### 28.1 Árvores de falhas

Uma árvore de falhas começa com um evento topo indesejado e o decompõe em causas ligadas por portas. Uma porta OU significa que qualquer filho causa o pai; uma porta E precisa de todos os filhos. Para eventos independentes, P(OU) ≈ soma das probabilidades quando elas são pequenas, e P(E) = produto. Para o evento topo da LDHP, a árvore de perda de calor por quatro horas deste capítulo, a porta OU no topo significa que qualquer ramo basta; a porta E sob o ramo (c) significa que o ataque só tem sucesso se as suas três condições forem verdadeiras. Se cada uma dessas três tivesse probabilidade 0,1 e elas fossem de fato independentes, o ramo (c) seria 0,001; os próximos parágrafos explicam por que uma causa cibernética quebra essa suposição.

### 28.2 Acrescentando eventos cibernéticos

Evento topo: perda de calor no distrito por mais de quatro horas. Filhos da porta OU: (a) as duas caldeiras desarmam e não conseguem religar; (b) as bombas de circulação param; (c) o setpoint de ida é manipulado e não é detectado por quatro horas. O evento (c) é ele próprio uma porta E: escrita de setpoint não autorizada *e* os operadores não percebem *e* o detector falha. Eventos cibernéticos quebram a suposição de independência: um único intruso pode causar várias falhas "independentes" ao mesmo tempo, então trate a causa comum com cuidado. Na LDHP, um único intruso com acesso à HMI-1 poderia escrever o setpoint e também silenciar a tela de alarmes da qual os operadores dependem para percebê-lo.

### 28.3 FMEA para o gateway

A FMEA lista cada componente, os seus modos de falha, efeitos, detecção e severidade. Os modos de falha do gateway incluem perda de energia (leituras ausentes — detectada por heartbeat), firmware corrompido (dados malformados — detectado por validação), adulteração da configuração (leituras falsas plausíveis — difícil de detectar) e expiração do certificado (uplink recusado — detectada por monitoramento). Para a LDHP, a adulteração da configuração é a linha que merece atenção: um gateway configurado para escalar cada leitura por 0,9 produz números plausíveis que passam nas verificações de validação e de heartbeat, e só apareceriam numa comparação dos totais dos gateways com o calor que sai da planta. A classificação STRIDE de Maya põe a tomada do gateway em primeiro lugar por esse motivo. A expiração do certificado, ao contrário, é fácil de detectar e fácil de prevenir com um alerta de renovação, então fica baixa, apesar de interromper todas as leituras.

### Exemplo resolvido (LDHP sintética)

Probabilidades anuais (ilustrativas): escrita não autorizada 0,05; os operadores não a percebem por quatro horas 0,2; o detector falha 0,1. P(c) = 0,05 × 0,2 × 0,1 = 0,001. As duas caldeiras não religam 0,002; bombas 0,003. P(topo) ≈ 0,002 + 0,003 + 0,001 = 0,006 por ano. Mas se o intruso também conseguir suprimir os alarmes da HMI, "os operadores não percebem" deixa de ser 0,2 e a independência da porta E desmorona — P(c) pode se aproximar de 0,05 × 1 × 0,1 = 0,005.

> **Caso sintético — Lakeside District Heating Plant.** Todas as probabilidades são inventadas para ilustração e não devem ser reutilizadas.

### 28.4 Visão em gravata-borboleta

Um diagrama em gravata-borboleta (bow-tie) põe o evento topo no centro, as ameaças e as barreiras preventivas à esquerda, e as consequências com as barreiras mitigadoras à direita. Ele ajuda os operadores a ver que o SIS-H é uma barreira mitigadora para a sobretemperatura, mas não oferece nada para a subtemperatura causada por um setpoint rebaixado. A contribuição de Maya para o HAZOP no Capítulo 32 faz o mesmo argumento pelo outro lado: o trip de alta temperatura do SIS-H é a salvaguarda para um setpoint manipulado que superaquece a caldeira, mas um setpoint escrito para 30 °C, como no exercício de mesa do Capítulo 29, causa perda de calor sem jamais se aproximar de um ponto de trip. Para essa consequência, as barreiras ficam à esquerda da gravata-borboleta: a lista de permissão do firewall, as contas nominais, os limites de setpoint de 70–110 °C do PLC-H e o alerta do monitor.

### Erros e limites

As probabilidades de eventos adversariais são julgamentos; apresente-as como faixas. As árvores de falhas deixam escapar as interações que não foram desenhadas.

### Exercícios

- **EX082 — Calculando uma porta E cibernética.** Com escrita 0,1, operadores não percebem 0,3 e detector falha 0,2, calcule P(c). *Rubrica:* 3 = 0,006; 2 = método certo; 1 = soma em vez de multiplicar; 0 = nada.
- **EX083 — Causa comum.** Explique como uma única intrusão pode quebrar a independência da porta E. *Rubrica:* 3 = o mesmo agente suprime alarmes/cega o detector, então os eventos ficam correlacionados; 2 = parcial; 1 = vago; 0 = nada.
- **EX084 — Uma linha de FMEA.** Escreva a linha da FMEA para a expiração do certificado do gateway. *Rubrica:* 3 = modo, efeito, detecção, severidade, ação; 2 = quatro; 1 = só o modo; 0 = nada.

### Síntese

Árvores de falhas e FMEA trazem eventos cibernéticos para a engenharia de confiabilidade — desde que você questione a independência que os adversários são pagos para quebrar.

<!-- open-cyber-academy:chapter-navigation:start ch-28 -->
### Continue estudando — capítulo 28 de 40

[← Capítulo 27](#ch-27) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 29 →](#ch-29)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-29"></a>

## Capítulo 29 — Segurança de TO, IoT e sistemas ciberfísicos: operações

### Objetivos de aprendizagem

Você vai (1) projetar um fluxo de monitoramento de segurança de TO com os operadores no circuito; (2) escrever um passo de playbook de resposta a incidentes que respeite a segurança do processo; (3) planejar a aplicação de patches dentro das janelas de manutenção; e (4) conduzir um exercício de mesa.

### 29.1 Monitoramento em que os operadores confiam

O monitoramento passivo de rede no switch de controle da LDHP constrói uma linha de base de quem fala com quem. Os alertas — um novo host falando Modbus, uma escrita de uma origem inesperada, um download de firmware — vão para um analista de segurança, que liga para o líder de turno antes que alguém toque na planta. O NIST SP 800-82r3 enfatiza que a resposta a incidentes em TO precisa ser coordenada com a operação, porque as próprias ações de contenção podem causar uma perturbação no processo. Na LDHP, o alerta do exercício de mesa deste capítulo, uma escrita Modbus no registrador 100 feita por 10.20.4.17 na VLAN do escritório, é exatamente o caso de "origem inesperada".

### 29.2 Passos do playbook

Bons passos de playbook de TO nomeiam quem decide e qual é o estado seguro. "Isolar o PLC-H da rede" é perigoso se os operadores perderem a HMI. Melhor: "O líder de turno decide se passa a caldeira para controle manual local; só então o analista bloqueia a origem suspeita no firewall." O exercício de mesa deste capítulo seguiu essa ordem: o analista ligou para o líder de turno às 02:12, o operador restabeleceu o setpoint de ida de 30 °C para 90 °C às 02:15, e o líder de turno aprovou o bloqueio de 10.20.4.17 no firewall às 02:18. O bloqueio veio depois de o processo estar seguro, e não antes, e depois de uma pessoa identificada tê-lo decidido.

### 29.3 Patches nas janelas

A LDHP tem uma janela de manutenção mensal de quatro horas. Os patches são testados numa HMI de bancada, classificados por risco (exposição × consequência) e aplicados em ordem até a janela encher; o resto é adiado com um chamado datado e controles compensatórios. O IEC TR 62443-2-3 trata da gestão de patches em ambientes de IACS. Num mês com uma correção de firmware do PLC-H, uma atualização do Windows da HMI-1 e um patch do gateway, a classificação só põe o PLC-H em primeiro lugar se a correção tratar de um caminho exposto; caso contrário, a HMI-1, que guarda as contas nominais dos operadores e está voltada para a EWS-1 e para o jump host, pode vir primeiro. O que for adiado recebe um chamado datado e os controles compensatórios do Capítulo 24.

### 29.4 Exercícios de mesa

Um exercício de mesa ensaia um cenário no papel: quem é chamado, o que é decidido, que informação está faltando. Ele revela lacunas sem arriscar o processo. O exercício de mesa da LDHP começou a partir de um alerta às 02:10 numa noite de janeiro: uma escrita Modbus no registrador 100 do PLC-H feita por 10.20.4.17 na VLAN do escritório. O analista ligou para o líder de turno às 02:12, o operador confirmou que o setpoint de ida tinha mudado para 30 °C e restabeleceu 90 °C às 02:15, e o líder de turno aprovou o bloqueio do endereço às 02:18, depois do que começou a coleta de evidências. A lacuna encontrada foi banal e importante: ninguém tinha o telefone noturno do administrador do firewall. Um incidente real teria encontrado a mesma lacuna com menos tempo para corrigi-la.

> **Caso sintético — Lakeside District Heating Plant.** Os horários, os endereços e a lacuna são inventados.

### Erros e limites

Os playbooks apodrecem à medida que as equipes e as redes mudam; revise-os depois de cada exercício. O bloqueio automático em TO deve ser excepcional e combinado de antemão.

### Exercícios

- **EX085 — Reescrevendo um passo de playbook perigoso.** Reescreva de forma segura "Desligue o servidor SCADA imediatamente". *Rubrica:* 3 = quem decide, primeiro o estado seguro do processo, depois a contenção; 2 = parcial; 1 = inalterado; 0 = nada.
- **EX086 — Preenchendo uma janela.** Os patches precisam de 1,5 h (risco 9), 2 h (risco 6), 1 h (risco 8) e 1 h (risco 3) numa janela de 4 h. Quais entram? *Rubrica:* 3 = riscos 9, 8 e 3 (3,5 h), com o patch de risco 6 adiado num chamado datado; 2 = conjunto certo, sem registro do adiamento; 1 = estoura a janela; 0 = nada.
- **EX087 — Corrigindo a lacuna do exercício de mesa.** Proponha uma correção para o telefone que faltava e como testá-la. *Rubrica:* 3 = escala de plantão no playbook mais uma ligação de teste no próximo exercício; 2 = um; 1 = vago; 0 = nada.

### Síntese

A segurança das operações de TO mantém os operadores no comando do processo, aplica patches por risco dentro das janelas e ensaia até que as lacunas sejam encontradas no papel, e não às 2 da manhã.

<!-- open-cyber-academy:chapter-navigation:start ch-29 -->
### Continue estudando — capítulo 29 de 40

[← Capítulo 28](#ch-28) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 30 →](#ch-30)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-30"></a>

## Capítulo 30 — Laboratório II

### Objetivos de aprendizagem

Você vai (1) avaliar uma frota IoT sintética contra provisões selecionadas da ETSI EN 303 645; (2) relatar as lacunas por dispositivo e da frota inteira; (3) relacionar as provisões com as atividades do fabricante do NIST IR 8259; e (4) priorizar a remediação.

### 30.1 A linha de base

A ETSI EN 303 645 V2.1.1 fixa 13 provisões de cibersegurança para IoT de consumo, mais provisões de proteção de dados. Este laboratório verifica quatro: 5.1 (nenhuma senha padrão universal), 5.2 (implementar um meio de gerenciar relatos de vulnerabilidades), 5.3 (manter o software atualizado) e 5.5 (comunicar-se com segurança). O NIST IR 8259 cobre um terreno parecido pelo lado do processo do fabricante — por exemplo, planejar atualizações e comunicar-se com os clientes.

```python
"""Lab 30: score a synthetic IoT meter fleet against selected ETSI EN 303 645 provisions."""
fleet = {"MTR-A": {"unique_pw": True, "vuln_policy": True, "update": True, "tls": True},
         "MTR-B": {"unique_pw": False, "vuln_policy": True, "update": True, "tls": True},
         "MTR-C": {"unique_pw": True, "vuln_policy": False, "update": False, "tls": False}}
PROV = {"unique_pw": "5.1 no universal default passwords", "vuln_policy": "5.2 vulnerability disclosure",
        "update": "5.3 software updatable", "tls": "5.5 secure communication"}
for dev, f in fleet.items():
    miss = [PROV[k] for k, v in f.items() if not v]
    print(f"{dev}: {4-len(miss)}/4 met; missing: {miss or 'none'}")
print("fleet-wide gaps:", sorted({k for f in fleet.values() for k, v in f.items() if not v}))
```

Execute com `python3 lab_fleet.py`. Saída verificada:

```text
MTR-A: 4/4 met; missing: none
MTR-B: 3/4 met; missing: ['5.1 no universal default passwords']
MTR-C: 1/4 met; missing: ['5.2 vulnerability disclosure', '5.3 software updatable', '5.5 secure communication']
fleet-wide gaps: ['tls', 'unique_pw', 'update', 'vuln_policy']
```

Os três modelos de medidor do laboratório respondem a um pequeno questionário sobre essas quatro provisões; o script relata quais cada um atende e o que falta à frota.

### 30.2 Lendo o resultado da frota

O MTR-A atende às quatro. O MTR-B falha apenas na 5.1 — corrigível forçando credenciais únicas na instalação. O MTR-C falha em três provisões: nenhuma política de divulgação, nenhum mecanismo de atualização e nenhuma comunicação segura. A lista de lacunas da frota inteira contém as quatro provisões, o que parece alarmante, mas é causado por apenas dois modelos; relate as duas visões.

A visão por dispositivo diz a Maya o que corrigir em cada modelo de medidor, enquanto a visão da frota diz ao gestor da LDHP quais provisões faltam em algum ponto do parque. Ler apenas a lista da frota sugeriria quatro problemas distintos em todos os medidores, quando o MTR-A está limpo e três das quatro lacunas estão só no MTR-C.

### 30.3 Priorizando

A severidade depende da consequência e da facilidade de correção. A falta de capacidade de atualização do MTR-C é estrutural — ele não pode receber patches —, então o planejamento da substituição começa agora. A senha padrão do MTR-B é o vetor clássico do Mirai (Capítulo 20) e é urgente, mas barata. A tabela de remediação de Maya segue essa ordem. O MTR-B é corrigido em duas semanas, na próxima visita de leitura dos medidores. O MTR-C recebe controles compensatórios imediatamente, isolamento atrás do gateway com o TLS terminado ali, e uma substituição programada para dentro de 12 meses, porque a 5.3 não pode ser atendida por nenhuma mudança de configuração. O MTR-A não precisa de nada agora, mas é verificado de novo sempre que o seu firmware muda, já que um resultado aprovado descreve uma única versão.

### 30.4 Limites da avaliação por lista de verificação

"Atende à 5.3", neste laboratório, é um booleano vindo de um questionário. Uma avaliação real verifica evidências: o mecanismo de atualização verifica assinaturas, e as atualizações são de fato publicadas? Para os medidores da LDHP, isso significa pedir a cada fornecedor evidências, e não respostas. Para o "atende à 5.3" do MTR-A, significa um pacote de atualização assinado e a data da última atualização publicada. Para a 5.1, significa uma restauração de fábrica que ainda produza uma senha única. Para a 5.5, significa a versão do TLS e o tratamento de certificados observados na bancada. Só as afirmações do MTR-A precisariam ser verificadas dessa forma primeiro, porque as suas quatro respostas "sim" são as que hoje sustentam uma decisão de não fazer nada.

### Exemplo resolvido (LDHP sintética)

Tabela de remediação de Maya: MTR-B — redefinir senhas únicas na próxima visita de leitura dos medidores, 2 semanas. MTR-C — isolar atrás do gateway com terminação TLS como controle compensatório para a 5.5, pedir o contato de divulgação do fornecedor, programar a substituição para dentro de 12 meses porque a 5.3 não pode ser atendida. MTR-A — nenhuma ação, verificar de novo quando o firmware mudar.

> **Caso sintético — Lakeside District Heating Plant.** Os modelos de dispositivos e as respostas são inventados.

### 30.5 Reproduzindo e ampliando o laboratório

Mude o dicionário de um dispositivo por vez e rode de novo, registrando a saída ao lado da edição. Se dois estudantes obtiverem resultados diferentes a partir dos mesmos dicionários, compare as versões do Python e o arquivo exato; o script é determinístico e nunca deveria divergir. Uma primeira edição útil é pôr o `unique_pw` do MTR-B como verdadeiro e confirmar que a sua linha passa a 4/4, enquanto a lista de lacunas da frota inteira perde o `unique_pw` e mantém as três lacunas do MTR-C; uma segunda é dar ao MTR-C uma política de divulgação e verificar que só a 5.2 some da sua lista de faltantes. Se a lista da frota inteira não mudar como você previu, leia a agregação do script antes de confiar na sua edição.

### Erros e limites

A ETSI EN 303 645 se destina a dispositivos de consumo; medidores distritais podem estar sujeitos a outros regimes. As quatro provisões verificadas são um subconjunto.

### Exercícios

- **EX088 — Acrescentando uma provisão.** Acrescente `"secure_storage"`, mapeada para a 5.4, com MTR-A True, MTR-B True e MTR-C False. O que o MTR-C imprime agora? *Rubrica:* 3 = percebe o 4 fixo no código (imprime 0/4), corrige-o e obtém 1/5 com quatro provisões faltando; 2 = um dos dois; 1 = diz 1/4; 0 = nada.
- **EX089 — Por que as lacunas da frota inteira enganam.** Explique por que "lacunas da frota inteira: as quatro" poderia enganar um gestor. *Rubrica:* 3 = dois modelos as causam; a visão por dispositivo mostra a maioria dos problemas no MTR-C; 2 = parcial; 1 = vago; 0 = nada.
- **EX090 — Evidência para a 5.3.** Que evidência você pediria a um fornecedor para aceitar "software atualizável"? *Rubrica:* 3 = mecanismo de atualização assinado, histórico de atualizações publicado/período de suporte, teste de atualização em bancada; 2 = dois; 1 = o fornecedor diz que sim; 0 = nada.

### Síntese

Avaliações de linha de base são úteis quando relatadas por dispositivo e por frota, sustentadas por evidências e transformadas num plano de remediação datado.

<!-- open-cyber-academy:chapter-navigation:start ch-30 -->
### Continue estudando — capítulo 30 de 40

[← Capítulo 29](#ch-29) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 31 →](#ch-31)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-31"></a>

## Capítulo 31 — Segurança de TO, IoT e sistemas ciberfísicos: casos avançados

### Objetivos de aprendizagem

Você vai (1) analisar um framework modular de ataque a ICS a partir de um alerta da CISA; (2) distinguir capacidade de uso observado; (3) derivar oportunidades de detecção a partir de comportamentos documentados; e (4) comparar um alerta centrado em capacidades com um relatório de incidente.

### 31.1 Ferramentas voltadas a dispositivos ICS/SCADA

A CISA, com agências parceiras, publicou o alerta AA22-103A em abril de 2022, avisando que agentes de ameaça persistente avançada tinham desenvolvido ferramentas customizadas capazes de procurar, comprometer e controlar certos CLPs da Schneider Electric, CLPs OMRON Sysmac NEX e servidores OPC UA, uma vez que tivessem acesso à rede de TO. O mesmo alerta descreve uma ferramenta que explorava um driver vulnerável de placa-mãe ASRock para comprometer estações de engenharia baseadas em Windows. O alerta nomeia famílias de produtos e ferramentas, não vítimas, e isso molda a forma como a LDHP deve lê-lo.

### 31.2 Capacidade não é incidente

Ao contrário do alerta de 2015 sobre a Ucrânia, o AA22-103A não descreve uma interrupção numa vítima identificada. Ele descreve uma capacidade. A resposta certa é a preparação: inventariar as famílias de produtos afetadas, restringir os protocolos de engenharia às estações de engenharia, monitorar conexões inesperadas e proteger os drivers das estações. As mitigações do alerta incluem isolar as redes de ICS, impor autenticação multifator para acesso remoto e monitorar drivers incomuns. A leitura de Maya para a LDHP: nenhuma das famílias de produtos nomeadas está em uso, mas o servidor OPC UA do HIST-1 e os drivers da EWS-1 são as exposições genéricas que o alerta descreve.

### 31.3 Do comportamento à detecção

O comportamento documentado sugere detecções específicas: um novo host falando o protocolo de engenharia de um fabricante de CLP; upload ou download de programa fora de uma janela de mudança (ATT&CK for ICS T0843 *Program Download*); sessões OPC UA a partir de hosts que não sejam os clientes conhecidos; carregamento de um driver assinado sabidamente vulnerável numa estação. Maya acrescentou duas dessas ao monitoramento da LDHP: sessões OPC UA com o HIST-1 a partir de clientes não aprovados, e eventos de carregamento de drivers na EWS-1, agora na lista de encaminhamento de logs da estação. A terceira, download de programa para o PLC-H fora de uma janela de mudança, cabe no monitor passivo já existente no switch de controle, que já alerta sobre downloads de firmware; estendê-lo para downloads de lógica só exige o calendário das janelas de mudança como entrada.

### 31.4 Comparando tipos de caso

Relatórios de incidente ensinam o que aconteceu sob restrições reais; alertas de capacidade ensinam o que poderia acontecer em seguida. Os dois são necessários, e nenhum substitui o seu próprio inventário. A tabela de casos de Maya no Capítulo 20 usou relatórios de incidente: a estação de água de 2021 e o Mirai, cada um com um análogo na LDHP. O AA22-103A acrescenta um tipo diferente de entrada, porque a LDHP não usa nenhum dos produtos nomeados. A resposta dela, duas novas detecções para o HIST-1 e a EWS-1, veio do inventário, e não da lista de produtos do alerta. Uma planta que só conferisse a lista de produtos teria concluído que não havia nada a fazer.

### Exemplo resolvido (LDHP sintética)

A LDHP não usa nenhuma família de produtos nomeada no AA22-103A. Maya não para por aí: ela observa que o servidor OPC UA do HIST-1 é uma exposição genérica, acrescenta "sessões OPC UA a partir de clientes não aprovados" ao monitoramento e acrescenta "eventos de carregamento de drivers na EWS-1" à lista de encaminhamento de logs da estação.

> **Caso sintético — Lakeside District Heating Plant.** A combinação de produtos da LDHP é inventada; o AA22-103A é um alerta real.

### Erros e limites

Os alertas são retratos de um momento; procure atualizações. Não baixe nem execute ferramentas nomeadas em alertas fora de um ambiente de pesquisa autorizado e isolado.

### Exercícios

- **EX091 — Escopo do alerta.** Nomeie as duas famílias de fabricantes de CLP e o tipo de servidor listados no AA22-103A. *Rubrica:* 3 = Schneider Electric, OMRON (Sysmac NEX), servidores OPC UA; 2 = dois; 1 = um; 0 = nada.
- **EX092 — Uma detecção a partir da T0843.** Escreva uma ideia de regra de detecção baseada no comportamento de download de programa. *Rubrica:* 3 = alertar sobre download de programa para o CLP fora de uma janela de mudança aprovada ou a partir de um host que não seja de engenharia; 2 = parcial; 1 = "monitorar os CLPs"; 0 = nada.
- **EX093 — Não afetado, mas agindo.** Por que agir com base num alerta que nomeia produtos que você não tem? *Rubrica:* 3 = as técnicas se transferem (OPC UA, drivers de estações, protocolos de engenharia); o inventário pode estar incompleto; 2 = um; 1 = "por precaução"; 0 = nada.

### Síntese

Analisar casos avançados significa ler os alertas em busca de comportamentos, traduzir comportamentos em detecções e recusar-se a concluir "não é conosco" só a partir de uma lista de produtos.

<!-- open-cyber-academy:chapter-navigation:start ch-31 -->
### Continue estudando — capítulo 31 de 40

[← Capítulo 30](#ch-30) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 32 →](#ch-32)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-32"></a>

## Capítulo 32 — Segurança de TO, IoT e sistemas ciberfísicos: interfaces interdisciplinares

### Objetivos de aprendizagem

Você vai (1) explicar como o trabalho de segurança faz interface com a segurança de processo, a operação, as compras e o direito; (2) escrever requisitos de segurança para uma especificação de compra; (3) participar de uma revisão conjunta de segurança física e segurança da informação; e (4) comunicar-se com profissionais que não são de segurança usando os termos deles.

### 32.1 Engenheiros de segurança de processo

As equipes de segurança de processo conduzem estudos de perigos e operabilidade (HAZOP) e determinam os níveis de integridade de segurança das funções instrumentadas de segurança segundo a IEC 61511. Um engenheiro de segurança da informação entra para perguntar, para cada perigo, se uma causa cibernética poderia iniciá-lo ou desabilitar a camada de proteção. O resultado é compartilhado: um registro de perigos que lista as causas cibernéticas ao lado das falhas de equipamento. A contribuição de Maya para o HAZOP da LDHP é o exemplo deste capítulo: "setpoint manipulado por escrita de rede não autorizada", acrescentado como causa para o nó de alta temperatura de ida, ao lado da falha do controlador e de uma válvula travada aberta.

### 32.2 Compras

O momento mais barato para corrigir a segurança é antes da compra. Uma especificação pode exigir capacidades da IEC 62443-4-2 num nível de segurança declarado, conformidade com a ETSI EN 303 645 para dispositivos do tipo consumo, um SBOM, um processo de divulgação de vulnerabilidades, um período de suporte definido e firmware assinado. Sem essas cláusulas, a planta herda o que quer que o fornecedor entregue. Para a próxima compra de medidores da LDHP, essas cláusulas teriam barrado o MTR-C antes da entrega: ele não tem mecanismo de atualização, contato de divulgação nem comunicação segura, três falhas que agora custam uma substituição dentro de 12 meses.

### 32.3 Operação e manutenção

Os operadores julgam qualquer mudança pelo seu efeito no turno. Apresente as mudanças de segurança nos termos deles: "esta mudança no firewall significa que a tela de tendências do historiador atualiza a cada 10 s, em vez de a cada 2 s." Os técnicos de manutenção precisam de procedimentos que caibam nas suas ferramentas; exigir um laptop que eles não carregam falha em silêncio. Na LDHP, a mudança na lista de permissão do Capítulo 27 seria apresentada à equipe de turno assim: "a HMI-1 continua escrevendo os mesmos setpoints; o historiador não consegue mais escrever nada; se uma escrita legítima for recusada, chame o engenheiro de controle, que pode vê-la no log do firewall". Essa frase responde à pergunta dos operadores, o que muda esta noite, sem uma palavra sobre códigos de função.

### 32.4 Direito e regulação

Dependendo da jurisdição, o aquecimento distrital pode ser regulado como infraestrutura crítica, com deveres de notificação de incidentes. A equipe de segurança precisa conhecer os prazos de notificação e quem notifica. Este livro dá orientação, não aconselhamento jurídico. Para um estudante de segurança na LDHP, o passo prático é descobrir com o próprio responsável de conformidade da planta qual regime se aplica, o que conta como incidente notificável e quem o notifica. No exercício de mesa do Capítulo 29, uma escrita de setpoint a partir da VLAN do escritório que cortou o calor por cinco minutos poderia muito bem atingir um limiar de notificação. Saber disso às 02:18 muda quais evidências o analista preserva e para quem o líder de turno liga em seguida.

### Exemplo resolvido (LDHP sintética)

Na revisão HAZOP da LDHP para "alta temperatura de ida", as causas existentes eram falha do controlador e válvula travada aberta. Maya acrescenta "setpoint manipulado por escrita de rede não autorizada" como causa, com a salvaguarda existente do trip de alta temperatura do SIS-H (transmissor independente, cabeado) e uma salvaguarda adicional recomendada: os limites de setpoint do PLC-H (Capítulo 24).

> **Caso sintético — Lakeside District Heating Plant.** O nó do HAZOP e as recomendações são inventados.

### Erros e limites

Um engenheiro de segurança da informação não está qualificado para alterar determinações de SIL; recomende e deixe a equipe de segurança de processo decidir. As cláusulas de compra precisam ser verificadas na entrega.

### Exercícios

- **EX094 — Três cláusulas de compra.** Escreva três cláusulas de segurança para a próxima compra de gateways de medidores da LDHP. *Rubrica:* 3 = três cláusulas específicas e verificáveis; 2 = duas; 1 = "deve ser seguro"; 0 = nada.
- **EX095 — Uma causa cibernética no HAZOP.** Para o nó "baixa vazão de circulação", acrescente uma causa cibernética e a sua salvaguarda. *Rubrica:* 3 = causa cibernética plausível mais salvaguarda independente; 2 = só a causa; 1 = falha de equipamento; 0 = nada.
- **EX096 — Explicando uma mudança aos operadores.** Explique em termos de operador a imposição da lista de permissão na HMI-1. *Rubrica:* 3 = o que eles veem, o que fazer se algo for bloqueado, para quem ligar; 2 = dois; 1 = jargão; 0 = nada.

### Síntese

A segurança de TO tem sucesso por meio de outras disciplinas: revisões de segurança de processo, cláusulas de compra, mudanças centradas nos operadores e consciência dos deveres legais.

<!-- open-cyber-academy:chapter-navigation:start ch-32 -->
### Continue estudando — capítulo 32 de 40

[← Capítulo 31](#ch-31) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 33 →](#ch-33)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-33"></a>

## Capítulo 33 — Métodos de pesquisa II

### Objetivos de aprendizagem

Você vai (1) projetar um estudo de simulação replicável com hipóteses pré-registradas; (2) escolher tamanhos de amostra para estimativas de proporções; (3) relatar tamanhos de efeito e intervalos, e não apenas significância; e (4) escrever uma seção de ameaças à validade que um revisor aceite.

### 33.1 Pré-registro

Escrever as hipóteses, as medidas, a análise e as regras de parada antes de rodar o experimento impede que a análise seja ajustada ao resultado. Para um estudo de detectores: "H1: a proporção de alarmes falsos do CUSUM em 300 execuções tranquilas será menor que a da faixa; medida primária: execuções com qualquer alarme falso; análise: diferença de proporções com intervalo de 95 %."

No projeto final de Maya, a regra de parada é o número fixo de sementes: 300 execuções calmas e 300 de ataque, sem execuções extras se o primeiro resultado parecer fraco. Fixar a medida, execuções com qualquer alarme falso, também impede que ela troque depois para outra medida que por acaso favoreça o CUSUM.

### 33.2 Tamanho de amostra para uma proporção

Para estimar uma proporção próxima de p com margem de erro E a 95 %, n ≈ 1,96² p(1−p)/E². Para p = 0,2 e E = 0,05, n ≈ 246. Para afirmar uma taxa abaixo de 1 % quando nenhum evento é observado, a regra de três precisa de n ≈ 300. As 300 sementes tranquilas de Maya decorrem da segunda fórmula: com 0 alarmes falsos em 300 execuções, o limite superior fica em cerca de 1 %, que é a afirmação que ela quer poder fazer. Quarenta execuções, como no Capítulo 25, só sustentariam cerca de 8,8 %. As suas 300 sementes de ataque por inclinação vêm da primeira fórmula, dimensionadas para que uma proporção de detecção próxima de 0,8 tenha uma margem de cerca de 5 pontos.

### 33.3 Tamanhos de efeito

"p < 0,05" diz pouco sobre o tamanho. Relate a diferença: faixa 22,5 % vs CUSUM 0 % de execuções com alarme falso, diferença de 22,5 pontos (intervalo calculado). Os leitores podem então decidir se ela importa operacionalmente. Nos números do Capítulo 25, a faixa gerou alarmes falsos em 9 de 40 execuções tranquilas, e o CUSUM, em 0 de 40. A diferença, 22,5 pontos, importa para os operadores porque significa um alarme incômodo mais ou menos em uma execução a cada quatro, em vez de nenhum observado. Um valor-p diria apenas que a diferença dificilmente é acaso, que é o fato menos interessante sobre ela. Um operador que decide se aceita o CUSUM na HMI-1 precisa do tamanho e dos limites de cada lado.

### 33.4 Pacote de replicação

Publique o código, as sementes, os parâmetros, a versão do Python e o comando exato. Neste livro, os laboratórios embutem a sua saída verificada para que o leitor possa conferir se uma nova execução coincide. O pacote de replicação de Maya para o estudo de detectores contém `lab_detect.py`, as faixas de sementes (0–39 tranquilas e 1000–1039 com ataque para a execução do Capítulo 25; 0–299 e 1000–1299 previstas para o trabalho de conclusão), os valores de limiar e de folga, a versão do Python e a linha de comando. Quem o rodar de novo deve obter exatamente 9/40 e 0/40 execuções com alarme falso; uma contagem diferente significa que algo no pacote está errado, e não que o resultado é incerto.

### Exemplo resolvido (LDHP sintética)

O pré-registro do trabalho de conclusão de Maya fixa: 300 sementes tranquilas e 300 com ataque, três inclinações de ataque, limiar escolhido num conjunto de ajuste separado de 50 sementes e depois congelado. Resultado primário: execuções com qualquer alarme falso, a medida fixada na H1; a detecção em até 60 amostras é um resultado secundário. Ela também declara que resultado falsearia a H1.

> **Caso sintético — Lakeside District Heating Plant.** O plano é para um estudo simulado.

### 33.5 Resultados negativos

Se o CUSUM não superar a faixa no limiar congelado, isso é um achado publicável numa monografia de bacharelado, desde que o método tenha sido sólido. Relate-o com os mesmos intervalos que você teria usado para um resultado positivo e discuta qual suposição — modelo de ruído, inclinação do ataque ou escolha do limiar — mais provavelmente o explica. Esconder um resultado negativo e rodar de novo com novas configurações até que algo "funcione" é a prática que o pré-registro existe para impedir. O limiar congelado de Maya é o que torna esse resultado crível.

### 33.6 Controle de versão como caderno de laboratório

Faça o commit do arquivo de pré-registro antes da primeira execução experimental e faça o commit dos resultados com o comando exato que os produziu. O histórico de commits mostra então a ordem das decisões, que é o que um examinador confere quando um resultado parece surpreendentemente limpo. Para Maya, o primeiro commit guarda o pré-registro, com o desenho de 300 sementes e a regra do limiar congelado; o commit de ajuste, nas 50 sementes separadas, vem em seguida; o commit de avaliação, depois dele, registra o comando e as saídas. Um examinador consegue então confirmar que o limiar existia antes de qualquer semente de avaliação ser rodada.

### Erros e limites

Estudos de simulação são fáceis de replicar, mas podem não se transferir para plantas. Comparações múltiplas inflam as falsas descobertas; ajuste-as ou declare de antemão um resultado primário.

### Exercícios

- **EX097 — Tamanho de amostra para 10 % ± 3 %.** Calcule n para estimar uma proporção próxima de 0,10 com ±0,03 a 95 %. *Rubrica:* 3 ≈ 385; 2 = método; 1 = usa E = 3; 0 = nada.
- **EX098 — Por que congelar os limiares?** Explique por que o limiar é ajustado em sementes separadas. *Rubrica:* 3 = evita sobreajuste aos dados de avaliação; estimativa não enviesada; 2 = parcial; 1 = vago; 0 = nada.
- **EX099 — Um resultado que falseia.** Enuncie o resultado que falsearia a H1. *Rubrica:* 3 = proporção de alarmes falsos do CUSUM ≥ à da faixa (o intervalo inclui ou passa da diferença zero); 2 = parcial; 1 = "se o CUSUM falhar"; 0 = nada.

### Síntese

O rigor na pesquisa aplicada em TO vem do pré-registro, de amostras adequadas, de tamanhos de efeito com intervalos e de pacotes de replicação completos.

<!-- open-cyber-academy:chapter-navigation:start ch-33 -->
### Continue estudando — capítulo 33 de 40

[← Capítulo 32](#ch-32) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 34 →](#ch-34)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-34"></a>

## Capítulo 34 — Projeto comparativo

### Objetivos de aprendizagem

Você vai (1) comparar duas arquiteturas de acesso remoto de fornecedores contra critérios explícitos; (2) construir uma matriz de decisão ponderada e testar a sua sensibilidade; (3) documentar as suposições de cada opção; e (4) recomendar, declarando o risco residual.

### 34.1 As duas opções

Opção A — VPN permanente do fornecedor até um jump host na DMZ da LDHP, com MFA. Opção B — sessões intermediadas sob demanda: o líder de turno habilita uma sessão para um chamado, o fornecedor se conecta por um intermediário (broker) em nuvem até o jump host, a sessão é gravada e termina depois de quatro horas. As duas evitam conexões diretas com o PLC-H. Essas duas opções vieram do ponto de partida da LDHP, a ferramenta de área de trabalho remota do fornecedor sempre ligada. As duas fecham esse caminho. A pergunta é qual delas se ajusta a uma planta que precisa da ajuda do fornecedor à noite.

### 34.2 Critérios

Exposição (por quanto tempo um caminho existe), atribuição (usuários nominais, gravação), adequação operacional (um fornecedor consegue ajudar às 3 da manhã?), custo e dependência de terceiros. Os pesos refletem as prioridades da LDHP: exposição 0,3, atribuição 0,25, adequação operacional 0,25, custo 0,1, dependência de terceiros 0,1. Os pesos foram definidos antes da pontuação, numa reunião com o gerente de operação da LDHP, e é por isso que podem ser contestados sem acusar quem pontuou de tê-los escolhido para favorecer uma preferida. A exposição tem o maior peso porque o caso da água de 2021 e a própria ferramenta sempre ligada da LDHP giraram em torno de quanto tempo um caminho remoto ficou aberto. O custo pesa pouco porque a diferença entre as duas opções é pequena perto do custo de uma noite sem aquecimento.

### 34.3 Pontuação

Notas de 1 a 5. A: exposição 2, atribuição 3, adequação 5, custo 4, dependência 4 → 0,6 + 0,75 + 1,25 + 0,4 + 0,4 = 3,40. B: exposição 5, atribuição 5, adequação 3, custo 3, dependência 2 → 1,5 + 1,25 + 0,75 + 0,3 + 0,2 = 4,00. B fica à frente. A opção B ganha principalmente em exposição e atribuição: um caminho que só existe por quatro horas por chamado e uma sessão gravada com uma conta nominal do fornecedor. A opção A ganha em adequação operacional, porque uma VPN permanente está disponível às 3 da manhã sem que ninguém precise habilitá-la. A diferença de 0,60 vem quase toda da exposição, em que B tem 5 contra 2 de A, então a recomendação só é tão boa quanto esse par de notas. Se o broker em nuvem fosse julgado uma dependência mais fraca do que o mostrado, a vantagem de B diminuiria, embora não o bastante, por si só, para invertê-la.

### 34.4 Sensibilidade

Suba a adequação operacional para 0,45 e baixe a exposição para 0,1: A = 0,2 + 0,75 + 2,25 + 0,4 + 0,4 = 4,00; B = 0,5 + 1,25 + 1,35 + 0,3 + 0,2 = 3,60. A ordem se inverte, então a recomendação depende de quanto a planta valoriza a disponibilidade do fornecedor à noite. Diga isso explicitamente. A inversão acontece porque a adequação operacional é onde A tem 5 e B tem 3: com peso 0,45, essa diferença vale 0,9, mais que a vantagem de B em exposição com o peso reduzido de 0,1. A resposta de Maya não foi escolher a ponderação de que gostava mais, mas corrigir o critério mais fraco de B: um procedimento noturno em que o líder de turno habilita uma sessão por meio de uma ligação para o engenheiro de plantão.

### Exemplo resolvido (LDHP sintética)

Maya recomenda B com uma mudança para tratar o seu critério mais fraco: um procedimento noturno documentado em que o líder de turno pode habilitar uma sessão por meio de uma ligação para o engenheiro de plantão. Ela registra o risco residual de que o broker em nuvem é uma dependência de terceiros e pede o seu atestado de segurança.

> **Caso sintético — Lakeside District Heating Plant.** As notas são julgamentos da estudante sobre opções inventadas.

### 34.5 Evidência para cada nota

Associe uma justificativa a cada número. A nota 5 de atribuição de B se apoia na gravação das sessões e nas contas nominais dos fornecedores no broker; a nota 2 de exposição de A se apoia no fato de a VPN estar permanentemente alcançável, mesmo quando não há trabalho programado. Se um revisor contestar uma nota, a coluna de evidências mostra exatamente o que conferir, e o teste de sensibilidade mostra se a contestação poderia mudar a recomendação. A nota 2 de dependência de B se apoia no broker em nuvem, e é por isso que Maya pediu o seu atestado de segurança.

### 34.6 Apresentando a comparação

Mostre ao gerente da planta a matriz, o resultado da sensibilidade e um parágrafo por opção descrevendo uma chamada de suporte noturna em cada desenho. Cenários concretos são mais fáceis de julgar que totais ponderados. Para as duas opções da LDHP, o parágrafo noturno faz a maior parte do trabalho. Na A, um engenheiro do fornecedor é chamado às 03:00 por causa de uma falha na caldeira, conecta-se pela VPN que está sempre aberta e alcança o jump host em minutos. Na B, o líder de turno liga para o engenheiro de plantão, que habilita uma sessão de quatro horas para o chamado; o fornecedor se conecta pelo broker e a sessão é gravada. O gerente consegue ver que a B custa uma ligação e alguns minutos à noite, e que a A deixa o caminho aberto em todas as outras noites do ano.

### Erros e limites

Matrizes ponderadas misturam julgamento com aritmética; divulgue os pesos e rode verificações de sensibilidade. Notas sem evidências são opiniões.

### Exercícios

- **EX100 — Recalculando com pesos iguais.** Usando peso 0,2 para os cinco critérios, pontue A e B. *Rubrica:* 3 = A 3,6, B 3,6, empate observado; 2 = um certo; 1 = erros aritméticos; 0 = nada.
- **EX101 — Uma suposição por trás da nota de exposição de B.** Nomeie uma suposição por trás de dar exposição 5 a B. *Rubrica:* 3 = as sessões realmente terminam, o broker não consegue abrir sessões sozinho, a habilitação pelo líder de turno é imposta; 2 = vaga, mas relevante; 1 = nenhuma relevante; 0 = nada.
- **EX102 — Quando inverter a recomendação.** Declare a condição sob a qual A deveria ser escolhida. *Rubrica:* 3 = se a disponibilidade do fornecedor 24/7 pesar mais que a exposição (peso alto para adequação) e o risco de A for compensado; 2 = parcial; 1 = "se for mais barata"; 0 = nada.

### Síntese

O trabalho comparativo é honesto quando critérios, pesos, evidências e sensibilidade estão todos visíveis, e quando a recomendação diz em que condições mudaria.

<!-- open-cyber-academy:chapter-navigation:start ch-34 -->
### Continue estudando — capítulo 34 de 40

[← Capítulo 33](#ch-33) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 35 →](#ch-35)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-35"></a>

## Capítulo 35 — Proposta do trabalho de conclusão

### Objetivos de aprendizagem

Você vai (1) escrever uma proposta de trabalho de conclusão com problema, pergunta, escopo, método, ética e cronograma; (2) definir entregáveis que possam ser avaliados; (3) declarar os limites de segurança e de autorização; e (4) obter a aprovação do escopo pelo orientador.

### 35.1 Estrutura da proposta

Uma proposta de trabalho de conclusão para este curso tem sete partes: enunciado do problema (um parágrafo com uma fonte citada), pergunta de pesquisa ou de projeto, escopo e exclusões, método, limites de ética e de segurança, entregáveis com critérios de aceitação, e um cronograma com marcos. Mantenha-a com menos de quatro páginas; um orientador precisa conseguir aprová-la ou rejeitá-la numa única reunião. A proposta de Maya cabe em três páginas: um parágrafo de problema citando a técnica T0836 do ATT&CK for ICS e o alerta da CISA AA21-042A, uma pergunta sobre a precisão com que um monitor baseado em regras consegue classificar escritas Modbus, escopo offline e sintético, e entregáveis verificáveis.

### 35.2 Um escopo que caiba

Trabalhos de conclusão de bacharelado fracassam mais por escopo que por dificuldade. "Proteger a LDHP" não é um trabalho de conclusão. "Projetar, implementar e avaliar um monitor passivo de escritas Modbus para a captura sintética da zona de controle da LDHP, medindo precisão e revocação em seis classes de ataque" é. A pergunta do trabalho de conclusão de Maya é próxima da segunda: classificar escritas Modbus numa captura sintética da LDHP com as regras do Capítulo 27 mais uma regra de taxa, e medir precisão e revocação. Ela é estreita o bastante para terminar num semestre e ainda responde a algo que importa aos engenheiros da LDHP: se o monitoramento passivo teria pegado uma escrita como a do exercício de mesa do Capítulo 29. O escopo também diz o que fica de fora: outros protocolos, capturas ao vivo e qualquer imposição.

### 35.3 Limite de ética e de segurança

A proposta precisa declarar: todos os dados são sintéticos ou fornecidos por um proprietário mediante acordo escrito; nenhum controlador ou rede real será sondado; qualquer ferramenta é passiva e offline; resultados que revelem uma fraqueza num produto real passam por divulgação coordenada. Um orientador assina esta seção. Para o projeto de Maya, o limite é fácil de declarar e mesmo assim precisa ser assinado: as capturas são tráfego sintético da LDHP, o monitor lê arquivos e nunca abre um socket de rede, e nada é executado contra o PLC-H ou qualquer controlador real. Se o trabalho dela sugerisse uma falha num produto de CLP real, ela iria primeiro para o fornecedor.

### 35.4 Critérios de aceitação

Cada entregável precisa de uma verificação: "o monitor processa o conjunto de avaliação de 8 casos e relata VP/FP/FN/VN com precisão e revocação" é verificável; "uma boa ferramenta" não é. Os três critérios de Maya são verificáveis dessa forma: o monitor processa o conjunto de 8 casos e relata uma matriz de confusão; relata precisão e revocação com os seus denominadores; e detecta cada uma das seis classes de ataque. O terceiro é o que a avaliação dela marca depois como parcialmente atendido. Um critério que não pode falhar, como "o monitor é útil", não dá ao examinador nada para avaliar nem ao estudante nada para defender.

### Exemplo resolvido (LDHP sintética)

A proposta de Maya. Problema: escritas de setpoint não autorizadas, como as descritas na técnica T0836 do ATT&CK for ICS, muitas vezes passam despercebidas pelos operadores (motivado pelo CISA AA21-042A, em que a equipe só percebeu porque estava olhando a tela). Pergunta: com que precisão um monitor baseado em regras consegue classificar escritas Modbus numa captura sintética? Escopo: offline, sintético, apenas Modbus/TCP. Método: regras de lista de permissão do Capítulo 27 mais uma regra de taxa; conjunto de avaliação do Capítulo 38. Cronograma: 12 semanas, com marcos nas semanas 3, 7 e 10.

> **Caso sintético — Lakeside District Heating Plant.** O trabalho de conclusão usa apenas capturas sintéticas.

### Erros e limites

Prometer métricas demais numa proposta ("100 % de detecção") prepara o fracasso. As propostas devem prever que um resultado negativo seja aceitável se for bem evidenciado.

### Exercícios

- **EX103 — Estreitando uma ideia de trabalho de conclusão.** Reescreva "uma IA que protege o aquecimento distrital" como uma pergunta de trabalho de conclusão com escopo definido. *Rubrica:* 3 = dados, método, medida, limite; 2 = três; 1 = continua ampla; 0 = nada.
- **EX104 — O parágrafo de ética.** Escreva em três frases o limite de ética e de segurança do projeto de Maya. *Rubrica:* 3 = só dados sintéticos, nenhuma sondagem, caminho de divulgação; 2 = dois; 1 = genérico; 0 = nada.
- **EX105 — Um critério de aceitação.** Escreva um critério de aceitação para o entregável "relatório de avaliação". *Rubrica:* 3 = conteúdo e verificação específicos (matriz de confusão, intervalos, sementes); 2 = parcial; 1 = "relatório completo"; 0 = nada.

### Síntese

Uma proposta forte é pequena, verificável e delimitada por uma ética explícita — e admite um resultado negativo honesto.

<!-- open-cyber-academy:chapter-navigation:start ch-35 -->
### Continue estudando — capítulo 35 de 40

[← Capítulo 34](#ch-34) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 36 →](#ch-36)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-36"></a>

## Capítulo 36 — Prática de campo ou comunitária

### Objetivos de aprendizagem

Você vai (1) planejar um estágio supervisionado ou um projeto comunitário com uma concessionária, uma escola ou um município; (2) combinar um escopo escrito que exclua testes ao vivo; (3) entregar trabalho de conscientização ou de inventário que ajude um pequeno operador; e (4) refletir sobre a prática usando um diário estruturado.

### 36.1 O que um estudante de bacharelado pode oferecer com segurança

Pequenas concessionárias de água, escolas com sistemas de gestão predial e cooperativas comunitárias de aquecimento muitas vezes não têm equipe de segurança. Um estudante sob supervisão pode ajudar com trabalhos de baixo risco e centrados em documentação: uma lista de ativos a partir dos registros existentes, uma revisão dos arranjos de acesso remoto, uma lista de verificação de higiene de senhas, uma sessão de conscientização para os operadores. Nada disso exige tocar num controlador em operação.

Cada uma dessas tarefas usa registros ou conversas em vez de acesso a controladores, de modo que um erro custa tempo, mas não pode parar uma bomba ou uma caldeira. A lista de ativos de Maya para a cooperativa de aquecimento é um exemplo: feita a partir de faturas e desenhos, ainda assim encontrou um roteador celular não documentado na casa da caldeira.

### 36.2 O acordo

O acordo de estágio nomeia a pessoa responsável na organização anfitriã, o orientador, os entregáveis, as regras de tratamento de dados (o que sai do local, como é armazenado e quando é excluído) e uma proibição explícita de varreduras, sondagens ou mudanças de configuração. Se o anfitrião pedir "uma varredura rápida", o estudante encaminha o pedido ao orientador. Quando o gerente da cooperativa pediu a Maya que "rodasse uma varredura para ver se fomos invadidos", o acordo lhe deu a resposta: recusar educadamente, explicar que a varredura está fora do escopo combinado, oferecer no lugar a revisão da documentação e repassar o pedido ao seu orientador.

### 36.3 Trabalhando com pequenos operadores

Os conselhos precisam caber no orçamento e na equipe deles. "Implante um SOC" é inútil para uma cooperativa de três pessoas; "remova a ferramenta de área de trabalho remota sempre ligada e use o recurso de sessão sob demanda do fornecedor, habilitado pelo telefone do gerente" é acionável. Os recursos gratuitos da CISA para pequenos sistemas de água e esgoto são um exemplo de orientação escrita para esse público.

O exemplo de acesso remoto também serve a uma cooperativa de três pessoas porque não exige equipamento novo nem equipe de monitoramento, apenas uma mudança na forma como o fornecedor se conecta. A recomendação de Maya para o roteador da casa da caldeira segue o mesmo padrão: confirmar a finalidade, desativá-lo se for desnecessário e, caso contrário, permitir que o fornecedor o use só mediante pedido.

### 36.4 Diário reflexivo

Depois de cada visita, registre: o que fiz, o que observei, o que me surpreendeu, o que faria de outro jeito e qualquer questão ética que tenha surgido. A reflexão transforma atividade em aprendizado. A entrada de Maya depois da visita à casa de caldeiras poderia dizer: fiz, montei uma lista de ativos a partir de notas fiscais e desenhos; observei, um roteador celular na casa de caldeiras que nenhuma nota fiscal mencionava; surpreendeu-me, o gerente não sabia que ele existia, embora fosse anterior à sua gestão; de outro jeito, pedir os documentos de comissionamento do montador do painel antes da visita, e não depois; questão ética, o pedido do gerente para "rodar uma varredura", que ela recusou e repassou ao orientador. A entrada não nomeia nenhum endereço nem credencial, então pode ser mostrada a um avaliador do jeito que foi escrita.

### Exemplo resolvido (sintético)

O estágio de Maya numa cooperativa fictícia de aquecimento de um vilarejo produz uma lista de ativos de duas páginas, montada a partir de notas fiscais e dos desenhos do montador do painel, que descobre um roteador celular não documentado na casa de caldeiras. A recomendação dela: confirmar com o montador do painel para que ele serve, desabilitá-lo se não for necessário e, caso contrário, exigir que o fornecedor só o habilite sob pedido.

> **Caso sintético — cooperativa fictícia de um vilarejo.** A cooperativa e o roteador são inventados.

### Erros e limites

Um estudante não é um consultor; as recomendações são revisadas pelo orientador antes da entrega. O trabalho comunitário não deve criar uma dependência que o estudante não consiga sustentar depois do estágio.

### Exercícios

- **EX106 — Respondendo a um pedido de varredura.** O gerente da cooperativa pede a Maya que "rode uma varredura para ver se fomos invadidos". Escreva a resposta dela. *Rubrica:* 3 = recusa educadamente, explica o escopo, oferece uma alternativa segura, encaminha ao orientador; 2 = três; 1 = concorda com ressalvas; 0 = roda a varredura.
- **EX107 — Regra de tratamento de dados.** Escreva uma regra de tratamento de dados para a lista de ativos. *Rubrica:* 3 = onde é armazenada, quem pode acessar, data de exclusão; 2 = dois; 1 = "guardar com segurança"; 0 = nada.
- **EX108 — Uma entrada de diário.** Escreva a linha "o que me surpreendeu" sobre o roteador celular. *Rubrica:* 3 = observação específica e lição sobre caminhos não documentados; 2 = só a observação; 1 = genérico; 0 = nada.

### Síntese

A prática de campo permite que os estudantes ajudem pequenos operadores com documentação e julgamento, dentro de acordos escritos que mantêm intocados os sistemas em operação.

<!-- open-cyber-academy:chapter-navigation:start ch-36 -->
### Continue estudando — capítulo 36 de 40

[← Capítulo 35](#ch-35) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 37 →](#ch-37)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-37"></a>

## Capítulo 37 — Seminário de revisão de evidências

### Objetivos de aprendizagem

Você vai (1) revisar criticamente uma afirmação publicada sobre segurança de TO; (2) graduar a qualidade das evidências, da anedota à medição replicada; (3) verificar se as conclusões decorrem dos dados apresentados; e (4) dar e receber revisão por pares estruturada.

### 37.1 Uma escada de evidências

Da mais fraca à mais forte: afirmação de marketing de fornecedor; anedota isolada; relato de caso de uma fonte primária; medição sistemática num sistema; medição replicada em vários sistemas ou por equipes independentes. Um seminário pergunta de toda afirmação: em que degrau ela está, e a conclusão vai além dele? A revisão de Maya do relatório de um colega aplica a escada: "o CUSUM elimina os alarmes falsos no aquecimento distrital" alega um resultado replicado, mas a evidência é uma única medição sistemática em dados sintéticos, 0 de 40 execuções. Esse degrau sustenta "nenhum alarme falso observado, limite superior de cerca de 8,8 %", e não a eliminação, e não diz nada sobre plantas reais.

### 37.2 Lendo um artigo de medição

O estudo do Mirai de Antonakakis et al. (USENIX Security 2017) é um bom texto para seminário: ele combina várias fontes de dados — varreduras de um telescópio de rede, honeypots, dados de DNS e dados das vítimas dos ataques — para estimar o tamanho e o comportamento da infecção. Pergunte: o que cada fonte vê e o que deixa de ver? Como os dispositivos infectados foram contados, se os endereços IP mudam? Quais conclusões dependem de uma única fonte? Para o seminário da LDHP, o exercício útil é pegar uma conclusão, como a parcela das infecções por credenciais padrão de Telnet, e nomear a fonte em que ela se apoia.

### 37.3 Lendo uma revisão de literatura

Giraldo et al. (ACM Computing Surveys, 2018) classificam os trabalhos de detecção baseada em física. A força de uma revisão é a amplitude; o seu risco é relatar o que os artigos afirmam, em vez de testá-los de novo. Use-a para encontrar artigos primários e fraquezas recorrentes, como modelos de atacante inconsistentes. Para o estudo de detectores de Maya, Giraldo et al. apontaram para a avaliação baseada em impacto de Urbina et al., que moldou a decisão dela de variar a inclinação do ataque em vez de relatar uma única taxa de detecção. A revisão também a alertou de que muitos artigos sobre detectores não usam um modelo de atacante consistente, e é por isso que o pré-registro dela nomeia a rampa de 0,08 °C por amostra como a sua classe de ataque antes de qualquer execução.

### 37.4 Revisão por pares estruturada

Formato da revisão: resumo com as suas próprias palavras; principais pontos fortes; preocupações maiores (validade, comparações ausentes, conclusões que vão além dos dados); questões menores; uma recomendação. Comente o trabalho, não a pessoa.

A revisão de Maya sobre o relatório de CUSUM do colega segue exatamente essa ordem. O resumo reformula a afirmação, o ponto forte é o script reproduzível com sementes, a preocupação maior é que 0 de 40 execuções sintéticas não sustentam "elimina", e a questão menor é o atraso dado em amostras em vez de minutos. A recomendação, revisar a afirmação e acrescentar o limite de cerca de 8,8 %, diz ao autor o que mudar. Separar preocupações maiores de menores mostra qual mudança é essencial antes que o relatório se sustente.

### Exemplo resolvido (LDHP sintética)

O relatório de um colega afirma que "o CUSUM elimina os alarmes falsos no aquecimento distrital". A revisão de Maya: resumo; ponto forte — script reprodutível com sementes; preocupação maior — 0/40 execuções sintéticas sustentam "nenhum alarme falso observado, limite superior ≈ 8,8 %", e não a eliminação, e nada foi testado em dados reais de uma planta; menor — a unidade do atraso (amostras) não é convertida em minutos; recomendação — revisar a afirmação e acrescentar o limite.

> **Caso sintético — Lakeside District Heating Plant.** O relatório do colega é inventado.

### Erros e limites

A revisão por pares confere o raciocínio, não a verdade; os revisores também deixam passar erros. O prestígio de um veículo de publicação não é evidência de correção.

### Exercícios

- **EX109 — Posicionando afirmações na escada.** Posicione na escada de evidências: (a) um folheto de fornecedor dizendo "bloqueia 99,9 % dos ataques a ICS", (b) o AA21-042A. *Rubrica:* 3 = (a) afirmação de marketing, (b) relato de caso primário; 2 = um; 1 = invertidos; 0 = nada.
- **EX110 — Questionando uma conclusão de fonte única.** Identifique uma conclusão do estudo do Mirai que seria mais fraca se se baseasse apenas em dados de honeypots, e por quê. *Rubrica:* 3 = estimativa do tamanho da infecção/da população; os honeypots só veem os dispositivos que os contatam; 2 = parcial; 1 = vago; 0 = nada.
- **EX111 — Escrevendo uma preocupação maior.** Escreva a preocupação maior para um artigo que avalia um detector numa única planta simulada, com limiares ajustados à mão. *Rubrica:* 3 = generalização e viés de ajustar no teste, com a correção pedida; 2 = um; 1 = comentário de estilo; 0 = nada.

### Síntese

A revisão de evidências pergunta quão fortes são as evidências, se a conclusão se ajusta a elas e como dizer isso de forma construtiva.

<!-- open-cyber-academy:chapter-navigation:start ch-37 -->
### Continue estudando — capítulo 37 de 40

[← Capítulo 36](#ch-36) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 38 →](#ch-38)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-38"></a>

## Capítulo 38 — Implementação do trabalho de conclusão

### Objetivos de aprendizagem

Você vai (1) implementar o artefato do trabalho de conclusão em incrementos pequenos e testados; (2) manter um registro de mudanças e um registro de decisões; (3) avaliar o artefato num conjunto rotulado, com uma matriz de confusão; e (4) relatar precisão e revocação com os seus denominadores.

### 38.1 Incrementos

Construa primeiro a menor versão de ponta a ponta: ler um arquivo de captura, classificar cada escrita, imprimir as decisões. Depois acrescente as regras uma de cada vez, cada uma com testes (Capítulo 8) e vetores de conformidade (Capítulo 27). Uma ferramenta pequena funcionando na semana 4 vale mais que uma ambiciosa que nunca roda. A versão da semana 4 de Maya lia uma captura sintética, classificava cada escrita Modbus contra a lista de permissão do Capítulo 27 e imprimia uma decisão por linha. A regra de taxa veio depois, com os seus próprios testes, e a regra de mudança cumulativa só depois que a avaliação mostrou que o ataque de deriva passava despercebido. Cada incremento podia ser executado e conferido contra os oito casos rotulados antes de o próximo começar.

### 38.2 Registros de decisão

Quando você escolhe, registre o porquê: "Decisão 7: tratar escritas durante uma janela de manutenção programada como benign-maint apenas se o ID do chamado aparecer na lista da janela; alternativas consideradas: regra só por horário (rejeitada: insiders poderiam cronometrar ataques)." Os registros de decisão permitem que os examinadores sigam o raciocínio. As decisões posteriores de Maya seguem o mesmo formato. Depois da avaliação, um registro acrescenta uma regra de mudança cumulativa para o ataque de deriva não detectado, com a alternativa de um limiar mais baixo por escrita rejeitada porque sinalizava ajustes comuns dos operadores. Outro registra a correlação das escritas da HMI com os eventos de login dos operadores, para tratar a escrita de setpoint que veio da HMI-1, que está na lista de permissão.

### 38.3 Avaliação

O laboratório avalia a saída de um monitor em oito casos rotulados do conjunto sintético de Maya.

```python
"""Lab 38: capstone evaluation - precision/recall with denominators (synthetic results)."""
cases = [("replay", True, True), ("replay", True, True), ("setpoint", True, False), ("setpoint", True, True),
         ("benign-maint", False, True), ("benign", False, False), ("benign", False, False), ("drift", True, False)]
tp = sum(a and d for _, a, d in cases); fp = sum((not a) and d for _, a, d in cases)
fn = sum(a and not d for _, a, d in cases); tn = sum((not a) and not d for _, a, d in cases)
print(f"TP={tp} FP={fp} FN={fn} TN={tn}")
print(f"precision={tp}/{tp+fp}={tp/(tp+fp):.2f} recall={tp}/{tp+fn}={tp/(tp+fn):.2f}")
print("missed classes:", sorted({c for c, a, d in cases if a and not d}))
```

Execute com `python3 lab_eval.py`. Saída verificada:

```text
TP=3 FP=1 FN=2 TN=2
precision=3/4=0.75 recall=3/5=0.60
missed classes: ['drift', 'setpoint']
```

Os oito casos incluem cinco ataques e três escritas benignas, entre elas uma escrita de manutenção. O laboratório calcula a precisão e a revocação a partir dos rótulos do monitor e imprime a matriz de confusão. O conjunto é de brinquedo: o seu propósito é mostrar quais classes o monitor deixa passar, e um nono caso poderia mudar todas as taxas. O seu valor está em que cada caso tem uma resposta conhecida, escrita antes de o monitor ser executado, de modo que uma divergência é sempre um erro do monitor ou do rótulo, e Maya registra qual dos dois.

### 38.4 Lendo a matriz de confusão

Três verdadeiros positivos, um falso positivo (uma escrita de manutenção sinalizada), dois falsos negativos (um ataque de setpoint e o ataque de deriva não detectados), dois verdadeiros negativos. Precisão 3/4 = 0,75; revocação 3/5 = 0,60. Oito casos são poucos demais para taxas precisas — um intervalo de Wilson para 3/5 vai de aproximadamente 0,23 a 0,88 —, então o uso honesto desta tabela é encontrar classes de falha, e não classificar ferramentas.

O único falso positivo é a escrita de manutenção, que a Decisão 7 trata como benigna apenas quando o ID do chamado aparece na lista da janela. As duas falhas apontam para correções diferentes, uma regra de mudança cumulativa para o ataque de deriva e a correlação com logins para a escrita da HMI-1, e por isso Maya examina cada classe separadamente em vez de ajustar um único limiar.

### Exemplo resolvido (LDHP sintética)

Maya examina as duas falhas de detecção. O ataque de deriva usou muitas escritas pequenas, cada uma dentro da faixa da lista de permissão — um monitor baseado em regras sem uma regra de taxa ou de tendência não consegue vê-lo. O ataque de setpoint não detectado veio da própria HMI-1, que está na lista de permissão. Os dois levam a novos registros de decisão: acrescentar uma regra de mudança cumulativa e correlacionar as escritas da HMI com os eventos de login dos operadores.

> **Caso sintético — Lakeside District Heating Plant.** Os oito casos são um conjunto de brinquedo para ilustração.

### Erros e limites

Os rótulos só são tão bons quanto o autor do cenário; um ataque rotulado como "benigno" corrompe todas as métricas. Não ajuste as regras nos casos de avaliação para depois relatar os mesmos números.

### Exercícios

- **EX112 — Corrigindo o falso positivo.** Proponha uma mudança que evite sinalizar a escrita de manutenção sem esconder ataques reais. *Rubrica:* 3 = exigir chamado/janela correspondente e conta de engenharia, continuando a registrar; 2 = parcial; 1 = ignorar o horário de manutenção; 0 = nada.
- **EX113 — Revocação depois de uma correção.** Se a regra de mudança cumulativa pegar o caso de deriva e nada mais mudar, qual é a nova revocação? *Rubrica:* 3 = 4/5 = 0,80; 2 = número certo, sem fração; 1 = 0,75; 0 = nada.
- **EX114 — Por que o intervalo importa.** Explique por que a revocação de 0,60 não pode ser comparada com os 0,70 de outra ferramenta num conjunto diferente de 10 casos. *Rubrica:* 3 = amostras minúsculas, intervalos largos e sobrepostos, combinação diferente de casos; 2 = um; 1 = "ferramentas diferentes"; 0 = nada.

### Síntese

Implemente em incrementos testados, registre as decisões e use conjuntos de avaliação pequenos para encontrar classes de falha, e não para alegar taxas.

<!-- open-cyber-academy:chapter-navigation:start ch-38 -->
### Continue estudando — capítulo 38 de 40

[← Capítulo 37](#ch-37) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 39 →](#ch-39)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-39"></a>

## Capítulo 39 — Avaliação do trabalho de conclusão

### Objetivos de aprendizagem

Você vai (1) avaliar um trabalho de conclusão contra a sua própria proposta; (2) separar resultados, interpretação e limitações; (3) fazer uma autoavaliação estruturada contra a rubrica do curso; e (4) planejar o trabalho de que um sucessor precisaria.

### 39.1 Contra a proposta

Volte aos critérios de aceitação escritos no Capítulo 35. Para cada um, registre atendido, parcialmente atendido ou não atendido, com evidências. Um trabalho de conclusão que não atende a um critério, mas explica por quê — por exemplo, a classe de deriva não pôde ser detectada só com regras —, ainda pode receber uma nota alta.

A tabela de avaliação de Maya mostra os três resultados possíveis em uso. Os critérios 1 e 2 são atendidos, com a matriz de confusão e os denominadores como evidência, enquanto o critério 3 é parcialmente atendido: cinco de seis classes de ataque após a regra cumulativa, com a escrita interna originada na HMI ainda não detectada e o motivo declarado.

### 39.2 Resultados versus interpretação

Resultados são o que a avaliação produziu: "revocação de 4/5 no conjunto de oito casos". Interpretação é o que você acha que isso significa: "a regra cumulativa trata a manipulação lenta". As limitações delimitam a interpretação: "testado apenas em dados sintéticos, com um único perfil de deriva". Manter três títulos impede que os resultados absorvam opiniões em silêncio. Na tese de Maya, a revocação subiu para 4/5 no conjunto de oito casos depois que a regra de mudança cumulativa pegou o ataque de deriva; a escrita da HMI-1 continua sendo a falha de detecção. Essa frase é um resultado. "O monitor é adequado para a LDHP" seria uma interpretação que a limitação, um único perfil de deriva em dados sintéticos, ainda não sustenta.

### 39.3 Rubrica de autoavaliação

Dê a si mesmo notas de 0 a 3 em: enquadramento do problema, adequação do método, qualidade das evidências, segurança e ética, comunicação. Escreva uma frase de evidência por nota. Os orientadores usam a mesma rubrica; as diferenças abrem uma conversa útil. Maya deu a si mesma 2 em qualidade das evidências, com a frase "oito casos é um conjunto de brinquedo", e 3 em segurança e ética, com "apenas offline, documentado". As resoluções explicam por que 2, e não 3, é justo: a análise é reprodutível e relata denominadores, mas oito casos sintéticos com um único perfil de deriva não sustentam afirmações gerais. Uma autoavaliação de 3 nesse ponto teria sido o primeiro ponto de desacordo com o orientador.

### 39.4 Plano para um sucessor

Liste o que você faria com mais três meses: um segundo modelo de processo, capturas reais anonimizadas (fornecidas por um proprietário), um estudo de usabilidade com operadores. Classifique pelo valor para a pergunta. Para Maya, a classificação põe em primeiro lugar a escrita originada na HMI, porque é a classe que o seu monitor ainda deixa passar: correlacionar as escritas com os logins dos operadores em capturas anonimizadas fornecidas pelo proprietário testaria a solução. Um segundo modelo de processo, como o vaso de expansão do Capítulo 21, vem em seguida, já que um monitor ajustado a uma malha pode não se transferir. Um estudo de usabilidade com operadores vem por último, porque só importa depois que o monitor detecta as classes que importam.

### Exemplo resolvido (LDHP sintética)

A tabela de avaliação de Maya: critério 1 (processa o conjunto de 8 casos, relata a matriz de confusão) — atendido; critério 2 (precisão e revocação com denominadores) — atendido; critério 3 (detecta as seis classes de ataque) — parcialmente atendido, cinco de seis depois da regra cumulativa, com a escrita de insider originada na HMI ainda não detectada. Autoavaliação: qualidade das evidências 2 ("oito casos é um conjunto de brinquedo"), segurança 3 ("apenas offline, documentado").

> **Caso sintético — Lakeside District Heating Plant.** As notas são uma ilustração resolvida.

### 39.5 A visão do orientador

Os orientadores procuram o alinhamento entre a pergunta, as evidências e as afirmações. Um comentário frequente nesta etapa é que a seção de conclusão repete os resultados em vez de responder à pergunta de pesquisa. Reescreva a conclusão para que a primeira frase responda diretamente à pergunta do Capítulo 35, a segunda declare a limitação mais forte e a terceira nomeie o próximo estudo. A primeira frase de Maya responderia diretamente à pergunta da sua proposta: em capturas sintéticas da LDHP, o monitor baseado em regras classificou corretamente cinco de seis classes de ataque.

### Erros e limites

A autoavaliação tende a dar notas altas demais à comunicação e baixas demais à adequação do método. Não redefina os critérios de aceitação depois do fato para ajustá-los aos resultados.

### Exercícios

- **EX115 — Classificando três frases.** Rotule como resultado, interpretação ou limitação: (a) "precisão de 4/5"; (b) "a ferramenta está pronta para um piloto"; (c) "um único perfil de deriva testado". *Rubrica:* 3 = R, I, L; 2 = duas; 1 = uma; 0 = nada.
- **EX116 — Pontuando a qualidade das evidências.** Justifique uma nota 2 (e não 3) para a qualidade das evidências no trabalho de conclusão de Maya. *Rubrica:* 3 = reprodutível e correto, mas o pequeno conjunto sintético limita a generalidade; 2 = parcial; 1 = "poderia ser melhor"; 0 = nada.
- **EX117 — A principal tarefa do sucessor.** Qual tarefa do sucessor mais fortalece a pergunta de pesquisa, e por quê? *Rubrica:* 3 = modelo de processo adicional ou capturas fornecidas pelo proprietário para testar a generalização; 2 = só a tarefa; 1 = polir a interface; 0 = nada.

### Síntese

Avalie um trabalho de conclusão contra as suas próprias promessas, mantenha os resultados separados das opiniões e deixe um caminho classificado para quem continuar o trabalho.

<!-- open-cyber-academy:chapter-navigation:start ch-39 -->
### Continue estudando — capítulo 39 de 40

[← Capítulo 38](#ch-38) · [Índice de capítulos do curso](../SUBJECTS.md) · [Capítulo 40 →](#ch-40)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-40"></a>

## Capítulo 40 — Tese e apresentação

### Objetivos de aprendizagem

Você vai (1) estruturar uma monografia de bacharelado em segurança de TO; (2) projetar slides que mostrem evidências, e não decoração; (3) preparar-se para uma defesa oral com perguntas previstas; e (4) publicar um pacote de replicação de forma responsável.

### 40.1 Estrutura da tese

Introdução (problema, pergunta, contribuição); fundamentação (normas e trabalhos anteriores, citados com precisão — NIST SP 800-82r3, as partes relevantes da IEC 62443, técnicas do ATT&CK for ICS, artigos revisados por pares que você leu); método; resultados; discussão, incluindo as limitações; conclusão e trabalhos futuros; apêndices com o código e as descrições dos dados. Mantenha o rótulo de sintético visível em toda legenda de figura que use dados da LDHP. Na tese de Maya, o capítulo de fundamentação cita a técnica T0836 do ATT&CK for ICS e o CISA AA21-042A para o problema, a IEC 62443-3-3 para os controles de zonas e conduítes por trás da sua lista de permissão, e Urbina et al. para avaliar detectores pelo impacto do atacante. Toda figura construída a partir de capturas da LDHP traz "dados sintéticos" na legenda.

### 40.2 Slides

Uma mensagem por slide, enunciada no título: "O monitoramento baseado em regras não detectou a deriva lenta; uma regra cumulativa a recuperou". Mostre a matriz de confusão, os denominadores e o intervalo. Evite imagens de hackers e ícones de cadeado; os examinadores os leem como sinal de conteúdo fraco. O slide de resultados de Maya mostra a sua matriz de oito casos com as contagens em cada célula, três verdadeiros positivos, um falso positivo, dois falsos negativos, dois verdadeiros negativos, e o intervalo de Wilson para a revocação de 3/5, de aproximadamente 0,23 a 0,88. O seu título enuncia o achado, em vez de "Resultados". Uma banca pode então perguntar sobre o falso positivo, uma escrita de manutenção sinalizada, sem precisar antes decifrar o gráfico.

### 40.3 Prevendo as perguntas

Prepare respostas para: Por que dados sintéticos? Como isto falharia numa planta real? Qual é a carga de alarmes falsos sobre os operadores por turno? Por que essas classes de ataque? O que faria um atacante que conhece as suas regras? Responder "não sei, mas é assim que eu descobriria" é aceitável; inventar números não é. Para a pergunta sobre alarmes falsos, Maya pode responder com os seus próprios dados: um falso positivo em oito casos é pouco demais para estimar a carga por turno, e ela diz isso, com o número de horas tranquilas de que precisaria para medi-la. Para a pergunta sobre o atacante, as suas duas falhas de detecção já respondem a uma parte: muitas escritas pequenas dentro da faixa permitida, e escritas feitas pela própria HMI-1.

### 40.4 Publicação responsável

Publique o código, as sementes e os dados sintéticos sob uma licença aberta. Não publique nada que seja um ataque funcional contra produtos reais. Se o trabalho encontrou uma vulnerabilidade real, a publicação espera a divulgação coordenada (Capítulo 10). O repositório da tese de Maya conteria o código do monitor, as capturas sintéticas da LDHP com o seu gerador e as sementes, e os oito casos rotulados. Não conteria nada que envie escritas Modbus, porque o monitor só lê arquivos de captura. Se o trabalho dela tivesse revelado uma falha no tratamento do código de função 8 por um CLP real, a descrição na tese esperaria até que o fornecedor tivesse uma correção.

### Exemplo resolvido (LDHP sintética)

A defesa de Maya abre com a contribuição numa frase: "Um monitor de escritas Modbus baseado em regras, com uma regra de mudança cumulativa, detectou cinco de seis classes de ataque sintéticas em capturas da LDHP; a classe restante — escritas a partir de uma HMI legítima — exige correlação com a identidade do operador." O seu slide de encerramento lista três limitações e o plano para um sucessor do Capítulo 39.

> **Caso sintético — Lakeside District Heating Plant.** A tese é uma ilustração resolvida sobre dados simulados.

### Erros e limites

Uma tese é julgada mais pelo raciocínio e pela honestidade que pelo tamanho do resultado. Capítulos longos de literatura que resumem sem avaliar acrescentam páginas, não notas.

### Exercícios

- **EX118 — Um título de slide que carrega a afirmação.** Escreva o título do slide que mostra o resultado de revocação de 4/5. *Rubrica:* 3 = afirmação em frase completa, com ressalva; 2 = afirmação sem ressalva; 1 = "Resultados"; 0 = nada.
- **EX119 — Defendendo-se de um atacante informado.** Esboce uma resposta para "o que faria um atacante que conhece as suas regras?". *Rubrica:* 3 = admite a evasão (por exemplo, pela HMI ou abaixo do limiar cumulativo), cita um orçamento de impacto no estilo de Urbina, propõe uma defesa; 2 = dois; 1 = nega; 0 = nada.
- **EX120 — O que não publicar.** Nomeie um item que deve ficar fora do pacote de replicação público, e por quê. *Rubrica:* 3 = qualquer coisa utilizável contra produtos reais ou quaisquer dados fornecidos pelo proprietário; com justificativa; 2 = só o item; 1 = "o código"; 0 = nada.

### Síntese

Uma tese encerra o curso mostrando que você consegue enquadrar uma pergunta de segurança de TO, respondê-la com evidências honestas e comunicar os limites da resposta às pessoas que precisam agir com base nela.

<!-- open-cyber-academy:chapter-navigation:start ch-40 -->
### Continue estudando — capítulo 40 de 40

[← Capítulo 39](#ch-39) · [Índice de capítulos do curso](../SUBJECTS.md) · [Resoluções →](#worked-results)

Siga para a próxima lição escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Resoluções

Respostas-modelo para EX001–EX120. A Lakeside District Heating Plant, Maya Chen e todos os números da planta são sintéticos. Qualquer resposta que atenda à rubrica recebe a mesma nota.

**EX001.** 150/3600 = 0,04167 m³/s → 41,67 kg/s; P = 41,67 × 4,19 × 30 ≈ 5.237,5 kW (cerca de 5,2 MW), aproximadamente 1 MW abaixo do caso de 180 m³/h.

**EX002.** "Se o gateway de medidores consegue escrever no PLC-H, então ele tem uma rota para a zona de controle." Ela é testável porque encontrar qualquer caminho de escrita bem-sucedido obriga a procurar a rota, e não encontrar nenhum sustenta (mas não prova) a afirmação original.

**EX003.** 6,3 MW × 24 h ≈ 151 MWh por dia, ou seja, "cerca de 150 MWh/dia"; a estimativa supõe carga constante, o que um perfil de noite de inverno violaria.

**EX004.** 9 + 4 = 13 ms deixa 7 ms; 7 / 0,6 = 11,67, portanto no máximo 11 requisições por varredura (11 × 0,6 = 6,6 ms → 19,6 ms).

**EX005.** (1) Reiniciar para limpar uma falha → programar uma parada controlada, com os operadores mantendo o processo seguro. (2) Instalar atualizações imediatamente → preparar o firmware numa unidade de bancada e implantá-lo numa janela de manutenção, com reversão. Desabilitar serviços de improviso ou rodar scanners também são exemplos aceitáveis.

**EX006.** A pilha de protocolos é compartilhada por todo o dispositivo e interpreta a entrada de rede antes que qualquer lógica do usuário seja executada, de modo que uma falha nela pode derrubar ou controlar o controlador, seja qual for o programa carregado; um defeito no ladder afeta apenas a função que aquele degrau implementa.

**EX007.** `TT-103 130.0 degC ok` — a comparação `lo <= v <= hi` é inclusiva, então uma leitura exatamente no limite superior passa.

**EX008.** `float("n/a")` levanta um ValueError e o script para com um traceback antes de imprimir as linhas restantes. Envolva a conversão em try/except, imprima `BAD-VALUE` para aquela tag e acrescente-a à lista de sinalizadas, para que um valor ausente nunca seja ignorado em silêncio.

**EX009.** 141 °C é fisicamente possível e pode ser um superaquecimento real, então o operador precisa verificar o processo agora; −3 m³/h não pode ocorrer num medidor unidirecional, então aponta para fiação, escala ou adulteração e cabe à instrumentação, com acompanhamento de integridade.

**EX010.** "O HIST-1 aceita conexões de entrada da VLAN do escritório na sua porta SQL (exportação do firewall, 3 de março) e mantém uma sessão de saída com o PLC-H; não testamos se o caminho do escritório consegue alcançar o PLC-H através dele."

**EX011.** IEC 62443-4-2 (requisitos de segurança de componentes, por exemplo autenticação de usuários humanos num dispositivo embarcado) para a capacidade do PLC-H; IEC 62443-2-1 para o programa de segurança do proprietário do ativo que inclui a gestão de patches, com o IEC TR 62443-2-3 como o relatório técnico específico de gestão de patches.

**EX012.** "Se você vir uma mudança de setpoint no PLC-H que ninguém do turno fez, chame o engenheiro de controle e anote o horário. Até a regra 14 ser removida, não acesse o e-mail do escritório pelo PC da sala da HMI."

**EX013.** (a) vulnerabilidade; (b) fonte de ameaça; (c) consequência.

**EX014.** Um setpoint manipulado produz dano físico imediato — casas frias ou estresse nos equipamentos — e pode ser irreversível em minutos, enquanto um vazamento de dados dos medidores fere a privacidade e ainda precisa ser evitado por força dos deveres de proteção de dados; a integridade do controle vem primeiro porque a sua consequência é física e crítica no tempo, não porque a privacidade possa ser negligenciada.

**EX015.** T0883 Internet Accessible Device. O mapeamento mostra apenas exposição; não prova que alguém tenha explorado o gateway, nem que a lista de técnicas mapeadas cubra todas as formas de atacar a LDHP.

**EX016.** MeterCloud → MeterGW → SCADA → Control → SIS (cada nó tem uma única aresta de saída, então a ordem da fila é única).

**EX017.** Não: depois da mudança, Control não tem conduíte de saída, então a nova aresta Internet→Control não alcança o SIS. Ela, porém, expõe o controle no nível do CLP diretamente à internet, o que é um achado grave por si só.

**EX018.** {(HIST-1, PLC-H, read), (HMI-1, PLC-H, read), (HMI-1, PLC-H, write)}.

**EX019.** tid=4, protocolo 0, comprimento 6, unidade 1, fc=4 (leitura de input registers), endereço inicial 0x0032 = 50, quantidade 0x0004 = 4 → uma leitura.

**EX020.** Os bytes não mostram quem o enviou nem se aquele host estava autorizado, e não mostram que o registrador 100 é o setpoint de ida em décimos de grau — as duas coisas vêm do contexto de rede e do mapa de registradores da planta.

**EX021.** 925 (0x039D), porque o registrador guarda décimos de grau Celsius.

**EX022.** "unknown". As subfunções do código 8 incluem reiniciar as comunicações ou zerar contadores, então rotulá-lo como "read" subestimaria o seu efeito; "unknown" obriga uma pessoa a olhar.

**EX023.** `self.assertEqual(classify(8), "unknown")` — com o código original, isso devolvia "read" e o teste falharia.

**EX024.** O hash de commit do git do script que produziu o resultado e um hash SHA-256 (mais a data da captura) do arquivo de entrada exato; a versão do Python é um terceiro item útil.

**EX025.** Doze linhas regulares de TT-101 são inseridas para t = 0, 5, …, 55, e o script acrescenta uma linha extra (35, 128.0), totalizando 13.

**EX026.** `select ts from (select ts, lead(ts) over (order by ts) as nxt from h where tag='PT-201') where nxt - ts > 10;` (o SQLite ≥ 3.25 suporta LEAD; uma auto-junção com o próximo carimbo de tempo maior também funciona). Nos dados do laboratório, ela não devolve nenhuma linha.

**EX027.** Com compressão por banda morta (por exceção), um novo valor só é arquivado quando difere do último valor arquivado em mais que a banda morta; se um pico sobe e desce entre dois pontos arquivados — ou se o ponto arquivado depois dele já voltou para dentro da banda —, o pico nunca é armazenado, e o historiador mostra uma tendência suave.

**EX028.** "Se qualquer alarme aparecer na HMI da caldeira da LDHP ou se a porta do switch mostrar erros durante a captura, pare a captura, remova o tap apenas com o consentimento do líder de turno e informe imediatamente o líder de turno e o engenheiro de controle."

**EX029.** Não. O gerente de uma terceirizada não é o proprietário do ativo; a varredura exige autorização escrita da LDHP (ou do seu delegado) e do gerente de operação, nomeando o PLC-H, a janela, a técnica permitida e as condições de parada — e uma varredura ativa de um controlador em operação provavelmente seria recusada em favor de métodos passivos.

**EX030.** Registrar a versão do firmware, a entrada e a evidência do travamento no sistema de bancada sem compartilhá-las publicamente, e então relatar pelo PSIRT ou pela política de divulgação do fornecedor (e à CISA ou ao CERT nacional se o fornecedor não responder), combinando um cronograma de divulgação.

**EX031.** O modo de auditoria registra todo executável que teria sido bloqueado, sem interrompê-lo, de modo que a equipe consegue montar uma lista completa dos binários legítimos da HMI durante a operação real; impor uma lista não testada poderia bloquear o runtime da HMI e tirar dos operadores a visão do processo.

**EX032.** Comece com uma exportação ao vivo, somente de leitura, dos logs de eventos, da lista de processos, das conexões de rede e do software instalado, usando uma conta nominal de investigação; gere uma imagem de disco apenas se a evidência a justificar, se o proprietário aprovar a parada e se uma HMI reserva ou redundante mantiver os operadores com visão da planta.

**EX033.** "Exceção HMI-1/SA-01: conta de serviço local `hmirt` mantida porque o runtime do fornecedor a exige (carta do fornecedor ref. V-221). Controles compensatórios: logon interativo negado, senha guardada em cofre e trocada trimestralmente, eventos de logon encaminhados ao SIEM. Responsável: líder de engenharia de controle. Revisão: 1º de março do ano que vem."

**EX034.** 3/150 = 0,02, ou seja, um limite superior de cerca de 2 % por dia com aproximadamente 95 % de confiança; a estimativa pontual de 0 não é uma afirmação de impossibilidade.

**EX035.** Por 500 dias: 0,95 alerta verdadeiro e 499 × 0,01 = 4,99 alertas falsos; precisão = 0,95 / 5,94 ≈ 0,16, então só cerca de 16 % dos alertas são reais.

**EX036.** Dias consecutivos compartilham clima, carga e equipe, então o comportamento de um detector no dia 12 prevê o seu comportamento no dia 13; as observações são positivamente correlacionadas e o tamanho efetivo da amostra é menor que 40, o que torna o limite superior real maior que 7,5–8,8 %.

**EX037.** Uma conta nominal de *visualizar* na HMI-1 (ou na réplica do historiador na DMZ), configurada para expirar no fim da semana; sem privilégios de operar ou de engenharia.

**EX038.** (1) Identificar a pessoa e a emergência que justificou o uso; (2) revisar nos logs todas as ações realizadas durante a sessão; (3) trocar e relacrar a credencial e confirmar que o alerta disparou como projetado.

**EX039.** Quaisquer duas entre: usar autenticação multifator; usar senhas fortes nas credenciais de RDP; auditar a rede em busca de RDP e fechar as portas RDP não usadas; registrar e auditar todas as tentativas de conexão remota; migrar para um sistema operacional suportado.

**EX040.** Quaisquer duas: quando o apartamento fica vazio por dias (férias), os horários em que os moradores acordam e dormem, se alguém trabalha em casa, aproximadamente quantas pessoas moram ali.

**EX041.** Totais diários por residência guardados por cerca de 60 dias: um vazamento aparece como um aumento sustentado do consumo ao longo de dias, então dados diários o detectam, e dois meses bastam para comparar com o período anterior antes da exclusão.

**EX042.** O consumo da escola é tão maior que o agregado passa a ser, na prática, o perfil da escola, revelando a sua ocupação, enquanto os cinco apartamentos são poucos demais para formar uma multidão significativa; são necessários um tamanho mínimo de grupo e uma verificação de dominância (nenhum local acima de, digamos, 30 % do total).

**EX043.** 10:04:10 + 75 s = 10:05:25 na hora de referência.

**EX044.** (a) O — é uma observação registrada (após a correção); (b) I — inferida a partir da lógica e da temporização do controlador; (c) A — uma suposição, a menos que a captura de rede que cobre o período tenha sido revisada.

**EX045.** Nome de quem exportou, sistema de origem e método de exportação, data e hora da exportação, hash SHA-256 do arquivo, local de armazenamento do original somente leitura (mais quaisquer transferências posteriores, com assinaturas).

**EX046.** Numa zona IoT própria ligada à DMZ (aproximadamente nível 3,5), porque ele coleta dados de campo como um dispositivo de nível 1–2, mas fala com um serviço em nuvem externo como um sistema de nível 4; forçá-lo para dentro da zona de controle daria à nuvem um caminho até o PLC-H.

**EX047.** Regra A: permitir HIST-1 (zona de controle) → HIST-R (DMZ) apenas na porta de replicação, com a conexão iniciada pelo HIST-1. Regra B: permitir usuários corporativos → HIST-R por HTTPS. A negação implícita bloqueia qualquer sessão Corporativo → HIST-1.

**EX048.** Manipular o PLC-H poderia interromper o calor de milhares de residências no inverno, uma consequência pública grave. Atacantes com habilidades específicas de ICS e recursos moderados — do tipo descrito no alerta da CISA AA22-103A sobre ferramentas voltadas a dispositivos ICS/SCADA — são plausíveis, e esse é o perfil de atacante do SL 3.

**EX049.** O contador `last` do receptor continua alto, então toda nova mensagem com contador ≤ last é rejeitada como repetição e o medidor fica mudo. Correção de projeto: persistir o contador entre atualizações, ou incluir um número de época da chave para que um medidor com chave nova comece um novo espaço de contador que o receptor aceite.

**EX050.** O SHA-256 não tem entrada secreta: um atacante que muda a leitura simplesmente recalcula o SHA-256 do novo valor, e o receptor vê um hash correspondente; só um MAC com chave amarra a tag a um segredo que o atacante não tem.

**EX051.** Extrair a chave de um único medidor fisicamente acessível permite que um atacante produza tags válidas para as leituras de qualquer medidor, de modo que um único comprometimento mina a integridade do faturamento de todo o distrito; chaves por dispositivo derivadas de uma chave-mestra protegida limitam o dano a um medidor.

**EX052.** "Das 4.000 configurações sintéticas de medidores da LDHP, que proporção atende às provisões 5.1, 5.3 e 5.5 da ETSI EN 303 645, e essa proporção difere entre os dois fornecedores de medidores?"

**EX053.** Ameaça: o ruído é um gaussiano idealizado, então os resultados podem não se manter em dados reais da planta, com deriva e quantização. Mitigação: acrescentar perfis de ruído extraídos de dados de processo publicados (ou um segundo modelo simulado com ruído autocorrelacionado) e relatar se a classificação muda.

**EX054.** Urbina et al. avaliam um detector por quanto dano um atacante ainda consegue causar mantendo-se abaixo do seu limiar de alarme, de modo que um detector com menos alarmes falsos, mas com um grande orçamento de impacto não detectável, é julgado mais fraco.

**EX055.** Sensor: falsificar ou enviesar o sinal do TT-101. Controlador: alterar o setpoint ou a lógica do PLC-H. Atuador: forçar a abertura da FV-12 por uma sobreposição manual ou manipulação de E/S. Comunicação: interromper ou atrasar o enlace PLC-H ↔ HMI, para que os operadores percam a visibilidade.

**EX056.** (a) NIST IR 8259 (com o IR 8259A) ou ETSI EN 303 645 para o fabricante do medidor; IEC 62443-4-2 se o medidor for vendido como componente industrial. (b) NIST SP 800-82r3 ou IEC 62443-2-1 para o programa da LDHP como proprietária do ativo.

**EX057.** Se o SIS-H lesse a temperatura por meio do PLC-H, um atacante que comprometesse o PLC-H ou falsificasse o TT-101 também cegaria o trip. Um transmissor separado, ligado diretamente ao SIS-H, mantém a função de segurança independente do sistema de controle que ela protege.

**EX058.** Cerca de 225.000 clientes foram afetados; os agentes corromperam o firmware dos dispositivos conversores serial-Ethernet nas subestações (o apagamento de HMIs com o KillDisk também é uma resposta aceitável).

**EX059.** Nomes de usuário e senhas padrão de fábrica ou fracos, alcançáveis por Telnet; a provisão 5.1 da ETSI EN 303 645 (nenhuma senha padrão universal) trata disso.

**EX060.** (a) Fato relatado no CISA AA21-042A. (b) Inferência — o alerta relata a tentativa de alteração, não a intenção do intruso.

**EX061.** No equilíbrio, vazão de entrada = vazão de saída = 2,0 = 1,6 × erro, logo erro = 1,25 ponto; o nível se estabiliza em cerca de 58,75 %.

**EX062.** Cada passo saturado acrescenta 1,5 ponto: depois de 8 passos, 69,5 %; depois de 9 passos, 71,0 %; portanto, 9 passos.

**EX063.** O controlador leva o nível *medido* a 57,5 %; com um viés de +10, o nível real é 47,5 % — o vaso fica com menos água enquanto a HMI parece normal.

**EX064.** Tag e função do ativo, fabricante e modelo, versão de firmware/software, zona e endereço de rede (ou enlace serial), responsável, classificação de criticidade (mais localização e dependências).

**EX065.** A versão de firmware instalada em cada gateway da LDHP e a versão da biblioteca TLS que esse firmware contém segundo o seu SBOM (ou declaração do fornecedor); se a biblioteca estiver entre 2.0 e 2.4, os gateways são afetados.

**EX066.** Só um engenheiro sabe restaurar a lógica do PLC-H a partir do backup; mitigar com um procedimento de restauração escrito e testado e um segundo engenheiro treinado. (O servidor de licenças da HMI ou uma única placa de E/S reserva também são respostas válidas.)

**EX067.** Consequência: leituras de consumo forjadas para uma rua inteira geram contas erradas e escondem um vazamento real por semanas. Caminho: a senha padrão do gateway de medidores permite que um atacante altere as leituras antes de elas serem assinadas e enviadas à nuvem.

**EX068.** Não. A (raro, mas catastrófico) pode exigir mudanças de projeto, como salvaguardas independentes, mesmo sendo improvável; B (frequente, mas menor) pode ser tratado operacionalmente. Produtos iguais escondem situações muito diferentes, então decida pelos cenários, e não pelo número.

**EX069.** "Residual do S-3: um insider com credenciais de engenharia na EWS-1 ainda poderia alterar setpoints do PLC-H. Supõe que as contas nominais e o registro estão implantados. Aceito pelo gerente da planta; revisão em 1º de abril do ano que vem ou após qualquer mudança no acesso de engenharia."

**EX070.** FR 1: credenciais únicas por dispositivo e contas administrativas nominais nos gateways. FR 5: os gateways só podem abrir TLS de saída para a nuvem de faturamento; nenhuma sessão de entrada vinda dela para a zona de controle. FR 6: alertar quando a configuração de um gateway mudar ou quando ele contatar um destino desconhecido.

**EX071.** Um operador que erra a digitação durante uma perturbação estressante fica trancado do lado de fora justamente quando o controle é necessário. Mais seguro: atraso progressivo e um alerta ao líder de turno, com o bloqueio desabilitado nos consoles da sala de controle protegidos fisicamente.

**EX072.** Colocá-lo numa VLAN própria, com um firewall que só permita os fluxos necessários; bloquear a sua interface de gerenciamento a partir de qualquer lugar, exceto um jump host; monitorar o seu tráfego em busca de destinos novos; programar a substituição por um modelo conforme.

**EX073.** Faixa: alarmes falsos em 9 de 40 execuções tranquilas. CUSUM: 0 de 40, com limite superior de 95 % de cerca de 7,5 % (regra de três) ou 8,8 % (Wilson), ou seja, "nenhum alarme falso observado", e não "nunca".

**EX074.** A folga (valor de referência) é subtraída de cada desvio para que, sob o ruído normal, a soma cumulativa continue voltando a zero; só um deslocamento sustentado maior que a folga a faz crescer até o limiar, o que suprime alarmes de ruído de uma única amostra.

**EX075.** Varrer a inclinação da rampa (por exemplo, 0,005–0,08 °C/amostra) e, para cada uma, registrar o desvio de temperatura alcançado antes de o CUSUM alarmar; o maior desvio alcançado sem detecção num horizonte fixo é a métrica de impacto de ataque furtivo que Urbina et al. recomendam.

**EX076.** S: um atacante apresenta ao gateway um falso endpoint de nuvem (servidor falsificado) se a validação de certificados for fraca. T: leituras alteradas no caminho por um proxy comprometido. D: o uplink do gateway é inundado ou o seu modem celular é bloqueado por interferência, de modo que as leituras não são entregues.

**EX077.** Agente: um atacante externo na internet. Pré-condição: a interface web do gateway é alcançável a partir da internet e ainda usa a senha padrão do fornecedor. Ação: entra e carrega firmware ou configuração modificados. Resultado: todos os 40 medidores atrás daquele gateway informam leituras falsas, e o gateway pode ser usado como ponto de apoio em direção à DMZ.

**EX078.** A repetição por um morador afeta a conta de uma residência e tem valor limitado, enquanto a tomada de um gateway afeta todos os medidores da sua rua e pode dar um ponto de apoio em direção a outras zonas; o raio de impacto maior e o possível efeito operacional a põem acima.

**EX079.** Esperado BLOCK, e `permit("HMI-1", 23, 105)` devolve BLOCK porque o par (HMI-1, 23) não está em ALLOW — a política nega por padrão as funções não listadas.

**EX080.** (HMI-1, 6, 120) → PASS, o novo último registrador gravável; (HMI-1, 6, 121) → BLOCK, o primeiro registrador depois da faixa.

**EX081.** Se as expectativas vierem da execução do código, um defeito vira o resultado esperado. Escrevê-las primeiro a partir do requisito operacional (de quais registradores a HMI-1 realmente precisa) permite que o teste pegue a divergência.

**EX082.** 0,1 × 0,3 × 0,2 = 0,006 por ano.

**EX083.** Um único intruso que escreve o setpoint também pode suprimir os alarmes da HMI ou desabilitar o detector, de modo que "os operadores não percebem" e "o detector falha" se tornam prováveis dada a escrita; multiplicar as probabilidades marginais subestima então P(c).

**EX084.** Componente: gateway de medidores. Modo: o certificado de cliente TLS expira. Efeito: a nuvem recusa o uplink; as leituras ficam em fila e depois são descartadas quando o buffer enche. Detecção: monitoramento de expiração de certificados com 30 dias de antecedência e alerta de heartbeat ausente. Severidade: média (atraso no faturamento, sem efeito no processo). Ação: renovação automatizada com alerta em caso de falha.

**EX085.** "O analista informa o líder de turno. O líder de turno confirma que os operadores conseguem manter a caldeira segura pelos painéis locais ou pela HMI reserva e então autoriza desconectar o enlace de rede do servidor SCADA (sem desligá-lo, para preservar as evidências)."

**EX086.** Guloso por risco: os de risco 9 (1,5 h) e 8 (1 h) usam 2,5 h; o de risco 6 precisa de 2 h e estouraria para 4,5 h, então é adiado; o de risco 3 (1 h) cabe, total de 3,5 h. Aplique 9, 8 e 3; adie o patch de risco 6 com um chamado datado e controles compensatórios (ou divida o plano da janela se o item de risco 6 puder ser encurtado).

**EX087.** Acrescentar à primeira página do playbook uma escala de plantão com os telefones noturnos do administrador do firewall e do engenheiro de controle, e incluir uma ligação de teste real para cada número no início do próximo exercício de mesa.

**EX088.** O laço usa `4-len(miss)`, então imprimiria `MTR-C: 0/4 met`, a menos que o 4 seja trocado; depois de trocá-lo por `len(f)-len(miss)`, o MTR-C imprime 1/5 met, com 5.2, 5.3, 5.4 e 5.5 faltando. Perceber o 4 fixo no código faz parte da resposta.

**EX089.** Todas as provisões aparecem como lacunas da frota, mas o MTR-A passa em todas e o MTR-B falha em apenas uma; o gestor poderia financiar a substituição da frota inteira quando o problema real está concentrado no MTR-C, mais uma redefinição de senha barata para o MTR-B.

**EX090.** Uma descrição de como as atualizações são assinadas criptograficamente e verificadas no dispositivo, o histórico de atualizações publicado pelo fornecedor e o período de suporte declarado, e uma demonstração em bancada aplicando uma atualização e rejeitando uma adulterada.

**EX091.** CLPs da Schneider Electric, CLPs OMRON Sysmac NEX e servidores Open Platform Communications Unified Architecture (OPC UA).

**EX092.** Alertar sempre que o monitoramento passivo vir uma operação de download de programa (ou de mudança de lógica) para o PLC-H que não parta da EWS-1 ou que ocorra fora de uma janela de mudança registrada no sistema de manutenção.

**EX093.** As técnicas — abusar de OPC UA, de protocolos de engenharia e de drivers vulneráveis de estações — se aplicam a outros produtos, e um inventário que diz "não temos nenhum" pode estar incompleto; agir com detecções genéricas reduz a exposição à próxima variante.

**EX094.** (1) O fornecedor deverá fornecer um SBOM para cada versão de firmware, em formato SPDX ou CycloneDX. (2) O gateway não deverá ter senha padrão universal e deverá forçar uma credencial única no comissionamento (provisão 5.1 da ETSI EN 303 645). (3) O fornecedor deverá publicar uma política de divulgação de vulnerabilidades e fornecer atualizações de segurança por pelo menos sete anos após a entrega.

**EX095.** Causa: uma escrita não autorizada para a bomba de circulação P-2 por meio da interface de rede do seu inversor de frequência. Salvaguarda: chave de baixa vazão cabeada que desarma os queimadores da caldeira pelo SIS-H, independente da rede dos inversores.

**EX096.** "A partir de segunda-feira, a HMI-1 só vai rodar o programa da HMI e as ferramentas aprovadas. Se algo que você costuma usar não abrir, vai aparecer uma mensagem — nada muda na planta. Anote o que você tentou e ligue para o engenheiro de controle no ramal 214; não tente contornar."

**EX097.** n = 1,96² × 0,10 × 0,90 / 0,03² = 3,8416 × 0,09 / 0,0009 ≈ 384,2, ou seja, cerca de 385 execuções.

**EX098.** Escolher o limiar nas mesmas execuções usadas para a avaliação o ajusta ao ruído dessas execuções e torna otimistas as estimativas de alarmes falsos e de detecção; ajustar em sementes separadas e congelar dá uma estimativa honesta do desempenho em dados não vistos.

**EX099.** A H1 é falseada se, nas 300 execuções tranquilas, a proporção de execuções com alarme falso do CUSUM não for menor que a da faixa — isto é, se o intervalo de 95 % para (faixa − CUSUM) incluir zero ou ficar abaixo dele.

**EX100.** A = 0,2 × (2 + 3 + 5 + 4 + 4) = 3,6; B = 0,2 × (5 + 5 + 3 + 3 + 2) = 3,6 — um empate exato, o que mostra que são os pesos que separam as opções.

**EX101.** Que o broker não consegue iniciar sessões sem a aprovação do líder de turno e que as sessões são encerradas automaticamente em quatro horas; se qualquer uma dessas coisas falhar, B tem um caminho permanente como A.

**EX102.** Escolher A quando a planta julgar a disponibilidade do fornecedor 24 horas por dia mais importante que a exposição do caminho — por exemplo, se a adequação tiver peso ≥ 0,45, como na execução de sensibilidade — e apenas com controles compensatórios, como gravação das sessões e revisões mensais de acesso.

**EX103.** "Um classificador de regressão logística treinado com 20 atributos sintéticos de temperatura de ida da LDHP consegue distinguir a deriva lenta de setpoint das mudanças normais de carga, medido pela revocação a uma taxa fixa de 5 % de alarmes falsos em execuções simuladas reservadas, sem nenhum acesso a uma planta real?"

**EX104.** "Todos os dados deste projeto são sintéticos e gerados pelos scripts do repositório; nenhum controlador, rede ou serviço real será contatado. O monitor apenas lê arquivos de captura offline. Se o trabalho revelar uma fraqueza em qualquer produto real, ela será relatada pelo processo de divulgação do fornecedor e não será publicada até que a divulgação seja coordenada."

**EX105.** "O relatório de avaliação contém a matriz de confusão do conjunto de 8 casos, a precisão e a revocação com numeradores e denominadores, a lista de classes de ataque não detectadas, o hash de commit do script e as sementes, e os seus números coincidem com uma nova execução de `lab_eval.py`."

**EX106.** "Obrigada pela confiança. O meu acordo de estágio não me permite varrer nem sondar os seus sistemas, porque até varreduras simples podem perturbar controladores mais antigos. O que posso fazer esta semana é revisar com você os arranjos e os registros de acesso remoto, e vou perguntar ao meu orientador se uma empresa qualificada deveria fazer uma avaliação técnica."

**EX107.** "A lista de ativos fica armazenada apenas na pasta criptografada do projeto na universidade, compartilhada com o orientador e com o gerente da cooperativa, e é excluída de todos os dispositivos do estudante no último dia do estágio."

**EX108.** "Fiquei surpresa que um roteador celular pudesse estar na casa de caldeiras sem aparecer em nenhum desenho nem nota fiscal — isso significa que o diagrama de rede da cooperativa não é um mapa confiável de como pessoas de fora conseguem alcançar a caldeira."

**EX109.** (a) Degrau mais baixo — uma afirmação de marketing não verificada, sem método nem denominador. (b) Um relato de caso primário de uma fonte governamental: mais forte, mas um único incidente.

**EX110.** A estimativa de quantos dispositivos foram infectados: os honeypots só observam os bots que por acaso os varrem ou atacam, então subcontam e são enviesados pela localização dos honeypots; os dados do telescópio dão a visão mais ampla da população.

**EX111.** "O detector é ajustado e avaliado na mesma planta simulada, então as taxas de alarmes falsos e de detecção relatadas provavelmente são otimistas e podem não se generalizar. Por favor, ajuste os limiares em sementes separadas, congele-os e avalie em pelo menos um modelo de processo adicional ou num conjunto de dados publicado."

**EX112.** Classificar uma escrita como benign-maint apenas quando ela vem da EWS-1, sob uma conta nominal de engenheiro, e o seu horário cai dentro de uma janela de manutenção vinculada a um chamado aberto; continuar registrando a escrita e incluí-la na revisão diária, para que um insider não consiga se esconder atrás da janela.

**EX113.** Os VP sobem para 4 e os FN caem para 1, então revocação = 4/5 = 0,80; a precisão fica em 4/5 = 0,80 se o falso positivo permanecer.

**EX114.** Com 5 casos de ataque, 0,60 tem um intervalo de 95 % de aproximadamente 0,23–0,88, e um conjunto de 10 casos tem um intervalo igualmente largo e classes de ataque diferentes, então os dois números se sobrepõem quase por completo e medem coisas diferentes.

**EX115.** (a) Resultado. (b) Interpretação — e uma que vai além do que estas evidências permitem. (c) Limitação.

**EX116.** A análise é reprodutível, usa as métricas corretas e relata os denominadores, mas oito casos sintéticos com um único perfil de deriva não sustentam afirmações gerais, então as evidências são sólidas, mas estreitas — um 2, e não um 3.

**EX117.** Testar num segundo modelo de processo construído de forma independente (ou em capturas anonimizadas fornecidas por um proprietário mediante acordo), porque a principal questão em aberto é se o conjunto de regras se generaliza para além da planta para a qual foi projetado.

**EX118.** "Acrescentar uma regra de mudança cumulativa elevou a revocação de 3/5 para 4/5 no conjunto sintético de oito casos — um achado sobre classes de falha, não uma estimativa de taxa."

**EX119.** "Eles fariam escritas a partir da própria HMI-1 ou manteriam cada mudança abaixo do limiar cumulativo, como Urbina et al. descrevem para ataques furtivos. O meu monitor não consegue impedir isso; ele limita o quanto o setpoint pode se mover sem ser notado, e correlacionar as escritas com os logins dos operadores é a próxima defesa que eu testaria."

**EX120.** Qualquer exportação de configuração, captura ou mapa de registradores fornecido por um proprietário real, mesmo anonimizado, porque pode revelar a sua arquitetura; isso fica sob o acordo de dados, enquanto o pacote público contém apenas os geradores sintéticos e as sementes.

<a id="references"></a>

## Referências

Links verificados em 12 de outubro de 2026; normas e alertas são revisados, por isso confirme as edições antes de citar. Os DOIs foram conferidos no Crossref.

- Antonakakis, M., et al. (2017). Understanding the Mirai Botnet. 26th USENIX Security Symposium. <https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/antonakakis>
- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA, DOE, NSA, FBI (2022). AA22-103A: APT Cyber Tools Targeting ICS/SCADA Devices. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-103a>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ICS-CERT (2016). IR-ALERT-H-16-056-01: Cyber-Attack Against Ukrainian Critical Infrastructure. <https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01>
- ISA/IEC 62443 series of standards (overview; parts 2-1, 2-3, 3-2, 3-3, 4-1 and 4-2 are cited in the text). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS, including T0836 Modify Parameter, T0843 Program Download, T0883 Internet Accessible Device and T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- Modbus Organization. Modbus Application Protocol Specification V1.1b3. Listed at <https://www.modbus.org/modbus-specifications>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- NIST FIPS 198-1 (2008). The Keyed-Hash Message Authentication Code (HMAC). <https://csrc.nist.gov/pubs/fips/198-1/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
